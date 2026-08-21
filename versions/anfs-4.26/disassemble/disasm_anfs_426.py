import os
from pathlib import Path
import dasmos
from dasmos.expr import sym, lo, hi
from dasmos import Align
from dasmos.hooks import stringhi_hook, stringz_hook

_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get("FANTASM_ROM", str(_version_dirpath / "rom" / "anfs-4.26.rom"))
_output_dirpath = Path(os.environ.get("FANTASM_OUTPUT_DIR", str(_version_dirpath / "output")))
d = dasmos.Disassembler.create(
    cpu="65C02",
    auto_label_data_prefix="l",
    auto_label_code_prefix="c",
    auto_label_subroutine_prefix="sub_c",
    auto_label_loop_prefix="loop_c",
)
d.load(_rom_filepath, 0x8000)
_netv_dispatch_entries = [
    (0x0000, "dispatch_rts", "no-op (RTS only)"),
    (0x0001, "netv_print_data", "NETV reason 1: print data"),
    (0x0002, "netv_print_data", "NETV reason 2: print data (alias)"),
    (0x0003, "netv_print_data", "NETV reason 3: print data (alias)"),
    (0x0004, "osword_4_handler", "NETV reason 4: OSWORD &04"),
    (0x0005, "netv_spool_check", "NETV reason 5: spool check"),
    (0x0006, "dispatch_rts", "no-op (RTS only)"),
    (0x0007, "netv_claim_release", "NETV reason 7: claim/release"),
    (0x0008, "osword_8_handler", "NETV reason 8: OSWORD &08"),
]

_osword_13_entries = [
    (0x0000, "osword_13_read_station", "read FS station"),
    (0x0001, "osword_13_set_station", "set FS station"),
    (0x0002, "osword_13_read_ws_pair", "read workspace pair"),
    (0x0003, "osword_13_write_ws_pair", "write workspace pair"),
    (0x0004, "osword_13_read_prot", "read protection mask"),
    (0x0005, "osword_13_write_prot", "write protection mask"),
    (0x0006, "osword_13_read_handles", "read transfer handles"),
    (0x0007, "osword_13_set_handles", "set transfer handles"),
    (0x0008, "osword_13_read_rx_flag", "read RX flag"),
    (0x0009, "osword_13_read_rx_port", "read RX port"),
    (0x000A, "osword_13_read_error", "read last error"),
    (0x000B, "osword_13_read_context", "read context"),
    (0x000C, "osword_13_read_csd", "read CSD"),
    (0x000D, "osword_13_write_csd", "write CSD"),
    (0x000E, "osword_13_read_free_bufs", "read free buffers"),
    (0x000F, "osword_13_read_ctx_3", "read context byte 3"),
    (0x0010, "osword_13_write_ctx_3", "write context byte 3"),
    (0x0011, "osword_13_bridge_query", "bridge query"),
]
_svc_dispatch_entries = [
    (0x0000, 0xE905, None, "placeholder (never reached)"),
    (0x0001, 0x8E8A, "dispatch_rts", "no-op (RTS only)"),
    (0x0002, 0x8D2D, "svc_dispatch_idx_2", "workspace claim helper (CMOS bit 0)"),
    (0x0003, 0x8F2A, "svc_2_priv_ws", "svc &02: private workspace pages"),
    (0x0004, 0x8CEE, "svc_3_autoboot", "svc &03: auto-boot"),
    (0x0005, 0x8C69, "svc_4_star_command", "svc &04: unrecognised *command"),
    (0x0006, 0x802A, "svc5_irq_check", "svc &05: IRQ check"),
    (0x0007, 0x8E8A, "dispatch_rts", "no-op (RTS only)"),
    (0x0008, 0x8EF2, "svc_7_osbyte", "svc &07: unrecognised OSBYTE"),
    (0x0009, 0xA857, "svc_8_osword_disp", "svc &08: OSWORD dispatch"),
    (0x000A, 0x8C78, "svc_9_help", "svc &09: *HELP"),
    (0x000B, 0x8E8A, "dispatch_rts", "no-op (RTS only)"),
    (0x000C, 0x806E, "econet_restore", "svc &0B: NMI release"),
    (0x000D, 0x89DB, "wait_idle_and_reset", "svc &0D: wait idle and reset"),
    (0x000E, 0x8B6D, "svc_18_fs_select", "svc &12: FS select"),
    (0x0F, 0x9692, "match_on_suffix", "svc &18: interactive HELP 'ON ' matcher"),
    (0x0010, 0x8F03, "raise_y_to_c8", "svc &21: static workspace claim"),
    (0x0011, 0x8F18, "set_rom_ws_page", "svc &22: dynamic workspace offer"),
    (0x0012, 0x8F0A, "store_ws_page_count", "svc &23: top-of-static-workspace"),
    (0x0013, 0x8E8B, "noop_dey_rts", "svc &24: dynamic workspace claim"),
    (0x0014, 0x8E8D, "copy_template_to_zp", "svc &25: FS name + info reply"),
    (0x0015, 0x8EA4, "svc_26_close_all_files", "svc &26: close all files"),
    (0x0016, 0x8F52, "nfs_init_body", "svc &27: post-hard-reset re-init"),
    (0x0017, 0x95A1, "print_fs_ps_help", "svc &28: print *FS/*PS no-arg syntax help"),
    (0x0018, 0x9631, "svc_29_status", "svc &29: *STATUS handler"),
    (0x0019, 0x98AF, "lang_0_insert_key", "language reply 0: insert remote key"),
    (0x001A, 0x9850, "lang_1_remote_boot", "language reply 1: remote boot"),
    (0x001B, 0xB051, "lang_2_save_palette_vdu", "language reply 2: save palette/VDU"),
    (0x001C, 0x987E, "lang_3_exec_0100", "language reply 3: execute at &0100"),
    (0x001D, 0x989F, "lang_4_validated", "language reply 4: remote validated"),
    (0x001E, 0xA0D1, "fscv_0_opt_entry", "FSCV 0: *OPT"),
    (0x001F, 0xA133, "fscv_1_eof", "FSCV 1: EOF"),
    (0x0020, 0xA507, "cmd_run_via_urd", "FSCV 2: *RUN"),
    (0x0021, 0xA445, "fscv_3_star_cmd", "FSCV 3: *command"),
    (0x0022, 0xA507, "cmd_run_via_urd", "FSCV 4: *RUN (alias)"),
    (0x0023, 0xB14D, "fscv_5_cat", "FSCV 5: *CAT"),
    (0x0024, 0x907A, "fscv_6_shutdown", "FSCV 6: shutdown"),
    (0x0025, 0x93F9, "fscv_7_read_handles", "FSCV 7: read handles"),
    (0x0026, 0x8E8A, "dispatch_rts", "no-op (RTS only)"),
    (0x0027, 0xB133, "ps_scan_resume", "PS scan tail (after pop_requeue)"),
    (0x0028, 0xB38C, "cmd_info_dispatch", "*Info dispatch"),
    (0x0029, 0xA4F2, "check_urd_present", "URD-present check"),
    (0x002A, 0xB310, "ex_init_scan_x0", "*Ex scan init"),
    (0x002B, 0xA6EB, "fsreply_1_boot", "FS reply 1: copy handles + boot"),
    (0x002C, 0xA6FB, "fsreply_2_copy_handles", "FS reply 2: copy handles"),
    (0x002D, 0xA64E, "fsreply_3_set_csd", "FS reply 3: set CSD"),
    (0x002E, 0xA507, "cmd_run_via_urd", "FS reply 4: *RUN (alias)"),
    (0x002F, 0xA654, "fsreply_5_set_lib", "FS reply 5: set library"),
    (0x0030, 0xA415, "net_1_read_handle", "net handle 1: read handle"),
    (0x0031, 0xA41B, "net_2_read_entry", "net handle 2: read handle entry"),
    (0x0032, 0xA42B, "net_3_close_handle", "net handle 3: close handle"),
]
_cmd_table_fs_entries = [
(0xA782, 'Net', 0xA785, 0x0080, 0xA786, 'cmd_net_check_hw', 'Econet HW check + select NFS'),
(0xA788, 'Pollps', 0xA78E, 0x0088, 0xA78F, 'cmd_pollps', 'syn 8: (<stn. id.>|<ps type>)'),
(0xA791, 'Prot', 0xA795, 0x0080, 0xA796, 'cmd_prot', 'toggle CMOS protection bit'),
(0xA798, 'PS', 0xA79A, 0x0088, 0xA79B, 'cmd_ps', 'syn 8: (<stn. id.>|<ps type>)'),
(0xA79D, 'Roff', 0xA7A1, 0x0080, 0xA7A2, 'cmd_roff', 'printer offline'),
(0xA7A4, 'Unprot', 0xA7AA, 0x0080, 0xA7AB, 'cmd_unprot', 'toggle CMOS protection bit'),
(0xA7AD, 'Wdump', 0xA7B2, 0x00C4, 0xA7B3, 'cmd_dump', 'syn 4 -- *DUMP alias'),
(0xA7B7, 'Access', 0xA7BD, 0x00C9, 0xA7BE, 'cmd_fs_operation', 'syn 9: <obj> (L)(W)(R)...'),
(0xA7C0, 'Bye', 0xA7C3, 0x0080, 0xA7C4, 'cmd_bye', 'log off FS'),
(0xA7C6, 'Cdir', 0xA7CA, 0x00C6, 0xA7CB, 'cmd_cdir', 'syn 6 -- create directory'),
(0xA7CD, 'Dir', 0xA7D0, 0x0081, 0xA7D1, 'cmd_dir', 'syn 1: (<dir>)'),
(0xA7D3, 'Flip', 0xA7D7, 0x0080, 0xA7D8, 'cmd_flip', 'swap fs/private workspace'),
(0xA7DA, 'FS', 0xA7DC, 0x008B, 0xA7DD, 'cmd_fs', 'syn &B -- file-server selection'),
(0xA7DF, 'I am', 0xA7E3, 0x00C2, 0xA7E4, 'cmd_iam_save_ctx', 'syn 2: (<stn>) <user>...'),
(0xA7E6, 'Lcat', 0xA7EA, 0x0081, 0xA7EB, 'cmd_lcat', 'syn 1: (<dir>) -- *CAT of library'),
(0xA7ED, 'Lex', 0xA7F0, 0x0081, 0xA7F1, 'cmd_lex', 'syn 1: (<dir>) -- *EX of library'),
(0xA7F3, 'Lib', 0xA7F6, 0x00C5, 0xA7F7, 'cmd_fs_operation', 'syn 5: <dir> -- set library'),
(0xA7F9, 'Pass', 0xA7FD, 0x00C7, 0xA7FE, 'cmd_pass', 'syn 7: <pass> ...'),
(0xA800, 'Rename', 0xA806, 0x00CA, 0xA807, 'cmd_rename', 'syn &A: <old> <new>'),
(0xA809, 'Wipe', 0xA80D, 0x0081, 0xA80E, 'cmd_wipe', 'syn 1: (<dir>) -- delete with confirm'),
(0xA818, 'Net', 0xA81B, 0x0080, 0xA81C, 'help_net', '*HELP NET'),
(0xA81E, 'Utils', 0xA823, 0x0080, 0xA824, 'help_utils', '*HELP UTILS'),
(0xA827, 'FS', 0xA829, 0x00C1, 0xA82A, 'set_fs_or_ps_cmos_station', 'FS not selected'),
(0xA82C, 'PS', 0xA82E, 0x00C3, 0xA82F, 'set_fs_or_ps_cmos_station', 'PS not selected'),
(0xA831, 'NoSpace', 0xA838, 0x0080, 0xA839, None, 'caller &9625'),
(0xA83B, 'Space', 0xA840, 0x0080, 0xA841, None, 'caller &961B'),
(0xA844, 'FS', 0xA846, 0x0081, 0xA847, 'print_fs_address', 'caller &9672'),
(0xA849, 'PS', 0xA84B, 0x0083, 0xA84C, 'print_ps_address', 'caller &9661'),
(0xA84E, 'Space', 0xA853, 0x0080, 0xA854, None, 'caller &9643'),
]
_ev_dispatch = ["ev_filev", "ev_argsv", "ev_bgetv", "ev_bputv", "ev_gbpbv", "ev_findv", "ev_fscv"]
handler_names = [
    ("FILEV", "filev_handler"),
    ("ARGSV", "argsv_handler"),
    ("BGETV", "bgetv_handler"),
    ("BPUTV", "bputv_handler"),
    ("GBPBV", "gbpbv_handler"),
    ("FINDV", "findv_handler"),
    ("FSCV", "fscv_handler"),
]
d.use_environment("acorn_mos")
d.use_environment("acorn_master_hardware")
d.use_environment(
    "acorn_sideways_rom", rom_title="ANFS ROM 4.26 disassembly (Acorn Advanced Network Filing System)"
)
d.index_base(0x0000, "zp_ptr_lo", length=1, group="zero_page")

# 4.26 dispatch-table bases (read from each dispatcher's operand; the
# tables hold shifted handler addresses so they don't opcode-map).
for idx, name, role in _netv_dispatch_entries:
    d.expr(0xAD42 + idx, lo(sym(name) - 1))
    d.expr(0xAD4B + idx, hi(sym(name) - 1))
    d.comment(0xAD42 + idx, "reason &%02X: %s (%s)" % (idx, name, role), align=Align.INLINE)
    d.comment(0xAD4B + idx, "reason &%02X: %s" % (idx, name), align=Align.INLINE)
for idx, name, role in _osword_13_entries:
    d.expr(0xA9CA + idx, lo(sym(name) - 1))
    d.expr(0xA9DC + idx, hi(sym(name) - 1))
    d.comment(0xA9CA + idx, "sub &%02X: %s (%s)" % (idx, name, role), align=Align.INLINE)
    d.comment(0xA9DC + idx, "sub &%02X: %s" % (idx, name), align=Align.INLINE)

for idx, target, name, desc in _svc_dispatch_entries:
    if name is not None:
        d.expr(0x8A25 + idx, lo(sym(name) - 1))
        d.expr(0x8A58 + idx, hi(sym(name) - 1))
    d.comment(0x8A25 + idx, "&%02X: %s" % (idx, desc), align=Align.INLINE)
    d.comment(0x8A58 + idx, "&%02X: %s" % (idx, desc), align=Align.INLINE)
d.index_base(0x0001, "zp_ptr_hi", length=1, group="zero_page")

d.index_base(0x0002, "zp_work_2", length=1, group="zero_page")

for i, (name, handler_label) in enumerate(handler_names):
    base_addr = 0x8ECF + i * 3
    d.word(base_addr)
    d.expr(base_addr, sym(handler_label))
    d.comment(base_addr, "%s handler" % name, align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, "(ROM bank — not read)", align=Align.INLINE)

d.index_base(0x0003, "zp_work_3", length=1, group="zero_page")

d.label(0x0010, "zp_temp_10", length=1, group="zero_page", access="rw")

d.label(0x0011, "zp_temp_11", length=1, group="zero_page", access="rw")

d.label(0x0012, "tube_data_ptr", length=1, group="zero_page", access="rw")

d.label(0x0013, "tube_data_ptr_hi", length=1, group="zero_page", access="rw")

d.constant(20, "osbyte_explode_chars")
d.label(0x0014, "tube_claim_flag", length=1, group="zero_page", access="rw")

d.index_base(0x0015, "tube_claimed_id", length=1, group="zero_page")

d.index_base(0x0020, "tx_buffer_scratch", length=1, group="zero_page")

d.label(0x0026, "parse_separator_flag", length=1, group="zero_page", access="rw")

d.label(0x0063, "zp_0063", description="(false ref from inline string data)", length=1, group="zero_page", access="rw")

d.constant(120, "osbyte_write_keys_pressed")
d.label(0x0078, "zp_0078", description="(false ref from inline string data)", length=1, group="zero_page", access="rw")

d.constant(0x7F, "rx_ready")
d.constant(0x80, "tx_flag")
d.constant(143, "osbyte_issue_service_request")
d.constant(0x90, "port_reply")
d.constant(0x91, "port_save_ack")
d.constant(0x92, "port_load_data")
d.constant(0x93, "port_remote")
d.label(0x0097, "escapable", description="b7=respond to Escape flag", length=1, group="zero_page", access="rw")

d.label(0x0098, "need_release_tube", description="b7=need to release Tube", length=1, group="zero_page", access="rw")

d.constant(0x99, "port_command")
d.label(
    0x0099,
    "prot_flags",
    description="PFLAGS: printer / protocol status flags.",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(0x009A, "net_tx_ptr", description="NetTx control block pointer (low)", length=1, group="zero_page", access="rw")

d.label(
    0x009B, "net_tx_ptr_hi", description="NetTx control block pointer (high)", length=1, group="zero_page", access="rw"
)

d.label(
    0x009C,
    "net_rx_ptr",
    description="NetRx control blocks pointer (low byte). Pairs with [`net_rx_ptr_hi`](label:net_rx_ptr_hi).",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(
    0x009D,
    "net_rx_ptr_hi",
    description="NetRx control blocks pointer (high byte). Pairs with [`net_rx_ptr`](label:net_rx_ptr) (low).",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(
    0x009E, "nfs_workspace", description="General NFS workspace pointer (low)", length=1, group="zero_page", access="rw"
)

d.label(
    0x009F,
    "nfs_workspace_hi",
    description="General NFS workspace pointer (high)",
    length=1,
    group="zero_page",
    access="rw",
)

d.constant(0xA0, "err_line_jammed")
d.label(
    0x00A0,
    "nmi_tx_block",
    description="NMI TX block pointer (low byte). Address of the TX control block currently being transmitted by the NMI handler.",
    length=1,
    group="zero_page",
    access="rw",
)

d.constant(0xA1, "err_net_error")
d.label(
    0x00A1, "nmi_tx_block_hi", description="Block to be transmitted (high)", length=1, group="zero_page", access="rw"
)

d.constant(0xA2, "err_not_listening")
d.label(0x00A2, "port_buf_len", description="Open port buffer length (low)", length=1, group="zero_page", access="rw")

d.constant(0xA3, "err_no_clock")
d.label(
    0x00A3, "port_buf_len_hi", description="Open port buffer length (high)", length=1, group="zero_page", access="rw"
)

d.constant(0xA4, "err_tx_cb_error")
d.label(0x00A4, "open_port_buf", description="Open port buffer address (low)", length=1, group="zero_page", access="rw")

d.constant(0xA5, "err_no_reply")
d.label(
    0x00A5, "open_port_buf_hi", description="Open port buffer address (high)", length=1, group="zero_page", access="rw"
)

d.label(0x00A6, "port_ws_offset", description="Port workspace offset", length=1, group="zero_page", access="rw")

d.label(0x00A7, "rx_buf_offset", description="Receive buffer offset", length=1, group="zero_page", access="rw")

d.constant(0xA8, "err_fs_cutoff")
d.constant(168, "osbyte_read_rom_ptr_table_low")

d.label(0x00A8, "ws_page", description="Multi-purpose workspace page", length=1, group="zero_page", access="rw")

d.label(0x00A9, "svc_state", description="Multi-purpose service state", length=1, group="zero_page", access="rw")

d.label(0x00AA, "osword_flag", description="OSWORD param byte", length=1, group="zero_page", access="rw")

d.label(0x00AB, "ws_ptr_lo", description="Workspace indirect pointer (lo)", length=1, group="zero_page", access="rw")

d.label(0x00AC, "ws_ptr_hi", description="Workspace indirect pointer (hi)", length=1, group="zero_page", access="rw")

d.label(0x00AD, "table_idx", description="OSBYTE/palette table index counter", length=1, group="zero_page", access="rw")

d.label(
    0x00AE, "work_ae", description="Indexed workspace (multi-purpose scratch)", length=1, group="zero_page", access="rw"
)

d.label(
    0x00AF,
    "addr_work",
    description="Address work byte for comparison (indexed)",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(
    0x00B0, "fs_load_addr", description="WORK: load/start address (4 bytes)", length=4, group="zero_page", access="rw"
)

d.label(0x00B1, "fs_load_addr_hi", length=1, group="zero_page", access="rw")

d.label(0x00B2, "fs_load_addr_2", length=1, group="zero_page", access="rw")

d.label(0x00B3, "fs_load_addr_3", length=1, group="zero_page", access="rw")

d.label(0x00B4, "fs_work_4", length=1, group="zero_page", access="rw")

d.label(
    0x00B5,
    "fs_work_5",
    description="FS scratch byte 5. Multi-purpose: *Wipe iteration counter, parsed FS station number, spool drive number, etc.",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(
    0x00B6,
    "fs_work_6",
    description="FS scratch byte 6. Multi-purpose: *Wipe end-of-buffer offset, parsed FS network number, etc.",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(0x00B7, "fs_work_7", length=1, group="zero_page", access="rw")

d.label(0x00B8, "fs_error_ptr", length=1, group="zero_page", access="rw")

d.label(0x00B9, "fs_crflag", length=1, group="zero_page", access="rw")

d.label(0x00BA, "fs_spool_handle", length=1, group="zero_page", access="rw")

d.label(0x00BB, "fs_options", length=1, group="zero_page", access="rw")

d.label(0x00BC, "fs_block_offset", length=1, group="zero_page", access="rw")

d.label(0x00BD, "fs_last_byte_flag", length=1, group="zero_page", access="rw")

d.label(0x00BE, "fs_crc_lo", length=1, group="zero_page", access="rw")

d.label(0x00BF, "fs_crc_hi", length=1, group="zero_page", access="rw")

d.label(0x00C0, "txcb_ctrl", length=1, group="zero_page", access="rw")

d.label(0x00C1, "txcb_port", length=1, group="zero_page", access="rw")

d.index_base(0x00C2, "txcb_dest", length=1, group="zero_page")

d.label(0x00C4, "txcb_start", length=1, group="zero_page", access="rw")

d.index_base(0x00C7, "txcb_pos", length=1, group="zero_page")

d.label(0x00C8, "txcb_end", length=1, group="zero_page", access="rw")

d.label(
    0x00CC,
    "fs_ws_ptr",
    description="FS workspace page pointer (lo, always 0)",
    length=1,
    group="zero_page",
    access="rw",
)

d.label(0x00CD, "nfs_temp", length=1, group="zero_page", access="rw")

d.label(0x00CE, "rom_svc_num", length=1, group="zero_page", access="rw")

d.label(0x00CF, "fs_spool0", length=1, group="zero_page", access="rw")

d.label(0x00D0, "vdu_status", description="VDU status register (OSBYTE &75)", length=1, group="zero_page", access="rw")

d.constant(0xD1, "port_printer")
d.index_base(0x00ED, "tx_imm_idx_base", length=1, group="zero_page")

d.label(0x00EF, "osbyte_a_copy", length=1, group="zero_page", access="rw")

d.label(0x00F0, "osword_pb_ptr", length=1, group="zero_page", access="rw")

d.label(0x00F1, "osword_pb_ptr_hi", length=1, group="zero_page", access="rw")

d.label(0x00F3, "os_text_ptr_hi", length=1, group="zero_page", access="rw")

d.label(0x00F7, "osrdsc_ptr_hi", length=1, group="zero_page", access="rw")

d.constant(0xFC, "cb_fill")
d.constant(0xFD, "cb_skip")
d.label(0x00FD, "brk_ptr", length=1, group="zero_page", access="rw")

d.constant(0xFE, "cb_stop")
d.label(0x00FF, "escape_flag", length=1, group="zero_page", access="rw")

d.label(0x0100, "error_block")

d.label(0x0101, "error_text")

d.index_base(0x0102, "stack_page_2", group="stack")

d.index_base(0x0103, "stack_page_3", group="stack")

d.index_base(0x0104, "stack_page_4", group="stack")

d.index_base(0x0106, "stack_page_6", group="stack")

d.index_base(
    0x0212,
    "vec_filev",
    description="FILEV pointer (lo, hi, rom). Patched to ANFS's FILE handler at init.",
    length=2,
    group="ram_workspace",
)

d.label(
    0x0214,
    "vec_argsv",
    description="ARGSV pointer (lo, hi, rom). Patched to ANFS's ARGS handler at init.",
    length=2,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0216,
    "vec_bgetv",
    description="BGETV pointer (lo, hi, rom). Patched to ANFS's BGET handler at init.",
    length=2,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0218,
    "vec_bputv",
    description="BPUTV pointer (lo, hi, rom). Patched to ANFS's BPUT handler at init.",
    length=2,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x021A,
    "vec_gbpbv",
    description="GBPBV pointer (lo, hi, rom). Patched to ANFS's GBPB handler at init.",
    length=2,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x021C,
    "vec_findv",
    description="FINDV pointer (lo, hi, rom). Patched to ANFS's FIND handler at init.",
    length=2,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x021E,
    "vec_fscv",
    description="FSCV pointer (lo, hi, rom). Patched to ANFS's FSC handler at init.",
    length=2,
    group="ram_workspace",
    access="rw",
)
d.label(0x028D, "last_break_type")

d.index_base(0x02A0, "rom_type_table", group="ram_workspace")

d.label(
    0x0350, "vdu_screen_mode", description="VDU screen mode set by the OS.", length=1, group="ram_workspace", access="r"
)

d.label(
    0x0351,
    "vdu_display_start_hi",
    description="VDU display start address (high byte).",
    length=1,
    group="ram_workspace",
    access="r",
)

d.label(
    0x0355,
    "vdu_mode",
    description="""VDU current output stream selector.
Determines whether `OSWRCH` writes to the screen, printer, serial port, etc. ANFS reads this to decide whether to wrap *HELP syntax lines for serial output.""",
    length=1,
    group="ram_workspace",
    access="r",
)

d.label(0x0406, "tube_addr_data_dispatch")

d.index_base(0x0CFF, "nmi_code_base", group="ram_workspace")

d.label(
    0x0D07,
    "nmi_romsel",
    description="""ROM-bank number patched into the NMI shim.
The NMI handler runs in the active sideways slot, so the shim begins by paging in the NFS ROM bank (this byte) before dispatching to the body.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D0C,
    "nmi_jmp_lo",
    description="""NMI dispatch JMP-target low byte.
Patched by [`set_nmi_vector`](label:set_nmi_vector) and [`install_nmi_handler`](label:install_nmi_handler). The NMI shim does `JMP (nmi_jmp_lo)` to reach the current handler.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D0D,
    "nmi_jmp_hi",
    description="""NMI dispatch JMP-target high byte.
Paired with [`nmi_jmp_lo`](label:nmi_jmp_lo). Only [`set_nmi_vector`](label:set_nmi_vector) writes this; [`install_nmi_handler`](label:install_nmi_handler) leaves it alone (same-page optimisation).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D0E,
    "set_nmi_vector",
    description="""NMI vector update (both bytes).
`STY` [nmi_jmp_hi](label:nmi_jmp_hi) then `STA` [nmi_jmp_lo](label:nmi_jmp_lo), writing the full 16-bit NMI handler address into the JMP-target slot. Falls through to [`nmi_rti`](label:nmi_rti).""",
    length=3,
    group="ram_workspace",
    access="r",
)

d.label(
    0x0D11,
    "install_nmi_handler",
    description="""NMI vector update (low byte only).
`STA` [nmi_jmp_lo](label:nmi_jmp_lo) only, leaving the existing high byte at [`nmi_jmp_hi`](label:nmi_jmp_hi) in place. Same-page optimisation used when the next handler is in the same page as the current one. Falls through to [`nmi_rti`](label:nmi_rti).""",
    length=3,
    group="ram_workspace",
    access="r",
)

d.label(
    0x0D14,
    "nmi_rti",
    description="""NMI exit shim.
Restores the previous ROM bank, pulls Y and A off the stack, reads `BIT enable_net_nmis` (INTON, re-enables /NMI), and `RTI`s. Reached either as a fall-through from [`set_nmi_vector`](label:set_nmi_vector) / [`install_nmi_handler`](label:install_nmi_handler), or as a direct branch from any NMI handler that has finished early.""",
    length=11,
    group="ram_workspace",
    access="r",
)

d.index_base(0x0D1A, "imm_param_base", group="ram_workspace")

d.index_base(0x0D1E, "tx_addr_base", group="ram_workspace")

d.label(
    0x0D20,
    "tx_dst_stn",
    description="Destination station for next TX scout/ACK frame.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D21,
    "tx_dst_net",
    description="Destination network for next TX scout/ACK frame.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D22,
    "tx_src_stn",
    description="""Source-station byte (our local station number). Loaded at init
from the Econet control block at `(net_rx_ptr)+1`. On the Master the
station number is configured in CMOS (`*CONFIGURE STATION nnn`).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D23,
    "tx_src_net",
    description="Source-network byte for outgoing scout/ACK frames (typically 0 for local network).",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D24,
    "tx_ctrl_byte",
    description="Control byte for next TX scout frame.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D25,
    "tx_port",
    description="Destination port for next TX scout frame.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.index_base(
    0x0D26,
    "tx_data_start",
    description="Start of TX data buffer (used by scout/data frame construction).",
    length=1,
    group="ram_workspace",
)

d.label(
    0x0D2A,
    "tx_data_len",
    description="Length of the TX data buffer payload, used during scout/data frame construction.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D2E,
    "scout_buf",
    description="""Base of the 12-byte RX scout data buffer.
Holds the most recently received scout frame during reception and ACK transmission.""",
    length=12,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D2F,
    "scout_src_net",
    description="Scout source network byte ([`scout_buf`](label:scout_buf)+1).",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D30,
    "scout_ctrl",
    description="""Scout control byte ([`scout_buf`](label:scout_buf)+2).
Carries the immediate-op code (`&81`..`&88`) for port-0 scouts; checked by [`immediate_op`](label:immediate_op).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D31,
    "scout_port",
    description="Scout port byte ([`scout_buf`](label:scout_buf)+3).",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.index_base(
    0x0D32,
    "scout_data",
    description="""Scout data payload base ([`scout_buf`](label:scout_buf)+4).
Holds the 4-byte remote address for JSR / UserProc / OSProc immediate ops.""",
    length=8,
    group="ram_workspace",
)

d.label(
    0x0D3D,
    "rx_src_stn",
    description="""Source station of the received scout frame.
First address byte read by [`nmi_rx_scout`](label:nmi_rx_scout) and validated against our station ID.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D3E,
    "net_frame_flags",
    description="""TX / transfer flags for the current Econet frame, initialised during
scout receive and carried through the reply and data-TX phases:

| Bit | Meaning |
|-----|---------|
| 0 | handshake-data pending |
| 1 | data transfer routes into the Tube buffer |
| 6 | broadcast frame (scout addressed to station &FF) |
| 7 | reply pending / data-TX phase / error-path selector |""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D3F,
    "rx_ctrl",
    description="Control byte of the received scout frame.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D40,
    "rx_port",
    description="""Port byte of the received scout frame.
Matched against the open RXCB list to find a listener (or the immediate-op port range &80..&88).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D41,
    "rx_remote_addr",
    description="Remote address byte for received TX setup.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D42, "rx_extra_byte", description="Extra trailing RX data byte.", length=1, group="ram_workspace", access="rw"
)

d.label(
    0x0D43,
    "saved_nmi_lo",
    description="""Saved next NMI handler address (low byte).
Written by [`ack_tx_write_dest`](label:ack_tx_write_dest) from the (A=lo, Y=hi) pair on entry, then consumed when the next NMI fires.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D44,
    "saved_nmi_hi",
    description="""Saved next NMI handler address (high byte).
Paired with [`saved_nmi_lo`](label:saved_nmi_lo).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D4A,
    "tx_flags",
    description="""TX path control flags.
Bit 7: TX path is active (used by [`nmi_error_dispatch`](label:nmi_error_dispatch) to choose between RX-error reset and TX-fail dispatch).
Bit 0: handshake-data pending.
Bit 1: data-RX into Tube buffer (selected by [`install_data_rx_handler`](label:install_data_rx_handler)).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D4B,
    "nmi_next_lo",
    description="""Next NMI handler address (low byte).
Saved by the scout / data-RX handler; consumed by [`ack_tx`](label:ack_tx) when installing the post-ACK NMI handler.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D4C,
    "nmi_next_hi",
    description="""Next NMI handler address (high byte).
Paired with [`nmi_next_lo`](label:nmi_next_lo).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D4F,
    "tx_index",
    description="Index into the TX buffer (current byte position).",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D50,
    "tx_length",
    description="Total length of the TX data payload.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D60,
    "tx_complete_flag",
    description="""TX completion semaphore.
Bit 7 set by the NMI TX-completion handler; polled by `wait_net_tx_ack` to detect frame completion.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D61,
    "econet_flags",
    description="""Econet control flags.
Bit 7: port-list active. Bit 2: halt requested.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D62,
    "econet_init_flag",
    description="""Econet-initialised flag.
Bit 7 set when the NMI shim has been installed; checked at every NMI to reject pre-init interrupts.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D63,
    "tube_present",
    description="""Tube co-processor presence flag.
Probed at init via OSBYTE `&EA`; read by every TX/RX path that needs to forward data through the Tube.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(0x0D64, "ws_0d64", description="ANFS workspace byte (role TBD).", length=1, group="ram_workspace", access="rw")

d.label(
    0x0D65,
    "tx_op_type",
    description="""Deferred-work / TX-operation type flag.
Set by NMI handlers to mark pending work; polled by [`svc5_irq_check`](label:svc5_irq_check) as the dispatch trigger.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D66,
    "exec_addr_lo",
    description="""Remote execution address (low byte).
Stored by remote-JSR / immediate-op paths; consumed when the queued operation runs.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D67,
    "exec_addr_hi",
    description="""Remote execution address (high byte).
Paired with [`exec_addr_lo`](label:exec_addr_lo).""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(0x0D68, "prot_status", description="Econet per-station protection mask (LSTAT): one bit per immediate operation; a set bit bars that operation. Tested by immediate_op; bits 2-4 (JSR/UserProc/OSProc) are raised during a deferred remote call for re-entrancy protection.", length=1, group="ram_workspace", access="rw")

d.label(0x0D69, "prot_status_save", description="Saved copy of the prot_status protection mask (OLDJSR in Acorn's DNFS source), preserved while bits 2-4 are raised during a deferred remote call so the original mask can be restored afterwards.", length=1, group="ram_workspace", access="rw")

d.label(0x0D6A, "ws_0d6a", description="ANFS workspace byte (role TBD).", length=1, group="ram_workspace", access="rw")

d.label(
    0x0D6B,
    "spool_buf_idx",
    description="Spool / printer buffer write index.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D6C,
    "fs_flags",
    description="""Filing-system status flags.
Bit 7: NFS is currently the selected FS; cleared when another FS takes over.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D6D,
    "tx_retry_count",
    description="""Transmit retry count (default `&FF` = 255).
Settable via OSWORD `&13` PB[1].""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D6E,
    "rx_wait_timeout",
    description="""Receive wait timeout (default `&28` = 40).
Settable via OSWORD `&13` PB[2].""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D6F,
    "peek_retry_count",
    description="""Machine peek retry count (default `&0A` = 10).
Settable via OSWORD `&13` PB[3].""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D71,
    "spool_control_flag",
    description="Multi-purpose: spool-buffer control flag (printer spooling); also doubles as the bridge-routing-table status byte read by [`init_bridge_poll`](label:init_bridge_poll) (`&FF` = uninitialised, anything else = bridge already polled).",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(
    0x0D72,
    "bridge_status",
    description="""Bridge station number (`&FF` = no bridge).
Set by the bridge-discovery scout reply; checked before any cross-network operation.""",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(0x0DE6, "txcb_default_base")

d.index_base(
    0x0DF0,
    "rom_ws_pages",
    description="MOS per-ROM workspace page table (16 bytes, one per sideways-ROM slot). Each entry is the high byte of the page allocated to that ROM's absolute workspace.",
    length=16,
    group="ram_workspace",
)

d.label(0x0DFA, "fs_context_save")

d.label(0x0DFE, "osword_ws_base")

d.label(0x0DFF, "fs_server_base")

d.label(0x0E00, "fs_server_stn")

d.label(0x0E01, "fs_server_net")

d.label(0x0E02, "fs_urd_handle")

d.label(0x0E03, "fs_csd_handle")

d.label(0x0E04, "fs_lib_handle")

d.label(0x0E05, "fs_boot_option")

d.label(0x0E06, "fs_messages_flag")

d.label(0x0E07, "fs_eof_flags")

d.label(0x0E09, "fs_last_error")

d.label(0x0E0A, "fs_cmd_context")

d.label(0x0E0B, "fs_context_hi")

d.label(0x0E16, "fs_work_16")

d.label(0x0E2F, "fs_filename_buf_m1")

d.label(0x0E30, "fs_filename_buf")

d.label(0x0E31, "fs_filename_buf_1")

d.label(0x0E32, "fs_filename_buf_2")

d.label(0x0E38, "fs_filename_backup")

d.label(0x0EF7, "fs_reply_data")

d.label(0x0F00, "txcb_reply_port")

d.label(0x0F01, "fs_cmd_y_param")

d.label(0x0F02, "fs_cmd_urd")

d.label(
    0x0F03,
    "fs_cmd_csd",
    description="TXCB port byte / CSD (current selected directory) handle.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(0x0F04, "fs_cmd_lib")

d.label(
    0x0F05,
    "fs_cmd_data",
    description="TX buffer data start / FS reply data.",
    length=1,
    group="ram_workspace",
    access="rw",
)

d.label(0x0F06, "fs_func_code")

d.label(0x0F07, "fs_data_count")

d.label(0x0F08, "fs_reply_cmd")

d.label(0x0F09, "fs_load_vector")

d.label(0x0F0A, "fs_handle_check")

d.label(0x0F0B, "fs_load_upper")

d.label(0x0F0C, "fs_addr_check")

d.label(0x0F0D, "fs_file_len")

d.label(0x0F0E, "fs_file_attrs")

d.label(0x0F10, "fs_file_len_3")

d.label(0x0F11, "fs_obj_type")

d.label(0x0F12, "fs_access_level")

d.label(0x0F13, "fs_reply_stn")

d.label(0x0F14, "fs_len_clear")

d.label(0x0F16, "fs_boot_data")

d.label(0x0F2F, "fs_exam_attr_char")

d.label(0x0F30, "fs_exam_dir_flag")

d.label(0x0FDC, "fs_putb_buf")

d.label(0x0FDD, "fs_getb_buf")

d.label(0x0FDE, "fs_handle_mask")

d.label(0x0FDF, "fs_error_flags")

d.label(0x0FE0, "fcb_xfer_count_lo")

d.label(0x0FF0, "fcb_xfer_count_mid")

d.label(0x1000, "fcb_count_lo")

d.label(0x1010, "fcb_attr_or_count_mid")

d.label(0x1020, "fcb_station_or_count_hi")

d.label(0x1030, "fcb_net_or_port")

d.label(0x1040, "fcb_flags")

d.label(0x1050, "fcb_net_num")

d.label(0x1060, "chan_status")

d.label(0x1070, "cur_dir_handle")

d.label(0x1071, "fs_lib_flags")

d.label(0x1072, "handle_1_fcb")

d.label(0x1073, "handle_2_fcb")

d.label(0x1074, "handle_3_fcb")

d.label(0x1078, "fcb_stn_lo")

d.label(0x1088, "fcb_stn_hi")

d.label(0x1098, "fcb_buf_offset")

d.label(0x10A8, "fcb_attr_ref")

d.label(0x10B8, "fcb_status")

d.label(0x10C8, "cur_fcb_index")

d.label(0x10C9, "cur_chan_attr")

d.label(0x10CA, "cur_attr_ref")

d.label(0x10CB, "xfer_count_lo")

d.label(0x10CC, "fcb_buf_page")

d.label(0x10CD, "xfer_sentinel_1")

d.label(0x10CE, "xfer_sentinel_2")

d.label(0x10CF, "xfer_offset")

d.label(0x10D0, "xfer_pass_count")

d.label(0x10D1, "xfer_counter")

d.label(0x10D4, "work_stn_lo")

d.label(0x10D5, "work_stn_hi")

d.label(0x10D6, "xfer_flag")

d.label(0x10D7, "osbput_saved_byte")

d.label(0x10D8, "quote_mode")

d.label(0x10D9, "fcb_ctx_save")

d.label(
    0x10F3,
    "filename_buf",
    description="Filename display buffer (12 bytes). Used by directory listing and *Info to format filenames.",
    length=12,
    group="ram_workspace",
    access="rw",
)

d.label(0x2048, "ws_template_source")

d.label(0x2322, "separator_parse_dispatch")

d.index_base(0x4898, "cdir_unused_dispatch_table", group="ram_workspace")

d.label(0x688B, "ws_precomputed_value")

d.label(0x6F6E, "false_ref_6f6e")

d.label(0x8001, "rom_header_byte1")

d.label(0x8002, "rom_header_byte2")

d.label(0x801A, "copyright_string")

d.entry(0x802A)


d.subroutine(
    0x802A,
    "svc5_irq_check",
    title="Service 5: unrecognised interrupt (dispatch)",
    description="""Delivers work deferred out of the Econet NMI receive handler.
An execute-class immediate operation -- a remote JSR, a user/OS
procedure call, halt or continue -- cannot safely JSR into user
code or call an OS routine from NMI context, so the NMI handler
records it instead: [`setup_sr_tx`](label:setup_sr_tx) stores the
operation type in [`tx_op_type`](label:tx_op_type) and sets the
Master 128 ACCCON IRR latch (bit 7 at `&FE34`) via `TSB`. The
latch raises an ordinary IRQ once the NMI handler has returned,
which reaches the ROM here as service call `&05` (unrecognised
interrupt) -- the normal IRQ path, where it is safe to run the
deferred operation.

Reads the deferred-work flag at `&0D65`; if zero, returns early via
`PLX`/`PLY`/`RTS`. Otherwise clears bit 7 of the Master 128 `ACCCON`
register at `&FE34` (`TRB`), zeros `&0D65`, then dispatches one of
two ways depending on bit 7 of the saved `Y`:

| Caller `Y` bit 7 | Action |
|---|---|
| Set | Dispatch via the `PHA`/`PHA`/`RTS` table at [`dispatch_svc5`](label:dispatch_svc5) |
| Clear | Fire Econet RX event `&FE` via [`generate_event`](label:generate_event), then `JMP` to [`tx_done_exit`](label:tx_done_exit) |""",
    on_entry={"a": "5 (service call number)", "x": "ROM slot", "y": "parameter (high bit selects dispatch path)"},
)


d.comment(0x802A, "Save X (the ROM slot we're being called on behalf of)", align=Align.INLINE)
d.comment(0x802B, "Save Y (the dispatch-path selector via its high bit)", align=Align.INLINE)
d.comment(0x802C, "Read deferred-work flag at &0D65 (set by NMI when work queued)", align=Align.INLINE)
d.comment(0x802F, "Non-zero: there's work to dispatch", align=Align.INLINE)
d.comment(0x8031, "Zero: no work; restore Y", align=Align.INLINE)
d.comment(0x8032, "Restore X", align=Align.INLINE)
d.comment(0x8033, "Return to MOS (service unclaimed)", align=Align.INLINE)
d.comment(0x8034, "A=&80: bit 7 -- the bit to clear in ACCCON", align=Align.INLINE)
d.label(0x8034, "irq_check_dispatch")

d.comment(0x8036, "Clear ACCCON bit 7 (drop the software IRQ)", align=Align.INLINE)
d.comment(0x8039, "Zero the deferred-work flag (we're handling it now)", align=Align.INLINE)
d.comment(0x803C, "Copy to A for sign test", align=Align.INLINE)
d.comment(0x803D, "Bit 7 set: dispatch via table", align=Align.INLINE)
d.comment(0x803F, "A=&FE: Econet receive event", align=Align.INLINE)
d.comment(0x8041, "Call event vector handler", align=Align.INLINE)
d.comment(0x8044, "Fire event (enable: *FX52,150)", align=Align.INLINE)
d.subroutine(
    0x8047,
    "generate_event",
    title="Generate event via EVNTV",
    description="""Single-instruction `JMP (evntv)` that hands control to whatever
handler is hooked into the MOS event vector. Called via service
call &05 (`svc5_irq_check`) on a 'transmit complete' or 'receive
complete' edge so user/MOS code can react to network events.""",
    on_entry={"A": "event number"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"},
)


d.comment(0x8047, "Dispatch through event vector", align=Align.INLINE)
d.subroutine(
    0x804A,
    "dispatch_svc5",
    title="Service-5 PHA/PHA/RTS dispatch tail",
    description="""Builds an `RTS`-target on the stack from the
[`svc5_dispatch_lo`](label:svc5_dispatch_lo) low-byte table and a hard-
coded high byte of `&85`, then falls through into the shared
[`svc_5_unknown_irq`](label:svc_5_unknown_irq) `RTS` to land on the matching
[`svc5_dispatch_lo`](label:svc5_dispatch_lo)+`Y` page-`&85` handler.""",
    on_entry={"y": "svc5_dispatch_lo offset (post-&83 base bias)"},
)


d.comment(0x804A, "Push return addr high (&85)", align=Align.INLINE)
d.comment(0x804C, "High byte on stack for RTS", align=Align.INLINE)
d.comment(0x804D, "Load dispatch target low byte", align=Align.INLINE)
d.comment(0x8050, "Low byte on stack for RTS", align=Align.INLINE)
d.subroutine(
    0x8051,
    "svc_5_unknown_irq",
    title="Service-5 unknown-IRQ tail (PHA/PHA/RTS landing)",
    description="""Bare `RTS` reused as the final step of every
[`dispatch_svc5`](label:dispatch_svc5) entry. With the target's
high/low bytes already pushed by the caller, `RTS` jumps to the
selected handler. Also reached as the unclaimed-IRQ tail of the
service-5 prologue when no ANFS handler matches.""",
)


d.entry(0x8051)
d.comment(0x8051, "RTS = dispatch to PHA'd address", align=Align.INLINE)
d.subroutine(
    0x8052,
    "adlc_init",
    title="ADLC initialisation",
    description="""Initialise ADLC hardware and Econet workspace. Disables NMIs via
`BIT disable_net_nmis` (the Master 128 INTOFF register at &FE38).
Performs a full ADLC reset via
[`adlc_full_reset`](label:adlc_full_reset), then probes for a Tube
co-processor via OSBYTE `&EA` and stores the result in
[`tube_present`](label:tube_present). Issues an NMI-claim service
request (OSBYTE `&8F`, `X=&0C`). Falls through to
[`init_nmi_workspace`](label:init_nmi_workspace) to copy the NMI shim to
RAM.""",
)


d.comment(0x8052, "INTOFF: disable NMIs (Master &FE38)", align=Align.INLINE)
d.comment(0x8055, "Full ADLC hardware reset", align=Align.INLINE)
d.comment(0x8058, "OSBYTE &EA: check Tube co-processor", align=Align.INLINE)
d.comment(0x805A, "X=0 for OSBYTE", align=Align.INLINE)
d.comment(0x805C, "Clear Econet init flag before setup", align=Align.INLINE)
d.comment(0x805F, "Check Tube presence via OSBYTE &EA", align=Align.INLINE)
d.comment(0x8062, "Store Tube presence flag from OSBYTE &EA", align=Align.INLINE)
d.comment(0x8065, "OSBYTE &8F: issue service request", align=Align.INLINE)
d.comment(0x8067, "X=&0C: NMI claim service", align=Align.INLINE)
d.comment(0x8069, "Issue NMI claim service request", align=Align.INLINE)
d.comment(0x806C, "Y=5: NMI claim service number", align=Align.INLINE)
d.label(0x806E, "econet_restore")

d.comment(0x806E, "Check if NMI service was claimed (Y changed)", align=Align.INLINE)
d.comment(0x8070, "Service claimed by other ROM: skip init", align=Align.INLINE)
d.label(0x8072, "init_nmi_workspace")

d.subroutine(
    0x8072,
    "init_nmi_workspace",
    title="Initialise NMI workspace (skip service request)",
    description="""Copies 32 bytes of NMI shim code from ROM (`listen_jmp_hi`) to the
start of the NFS workspace RAM block, then patches the current ROM
bank number into the self-modifying code at `nmi_romsel` (`&0D07`).

The shim includes the INTOFF/INTON pair (`BIT disable_net_nmis`
at entry, `BIT enable_net_nmis` before `RTI`) that toggles the
Econet NMI-enable flip-flop, guaranteeing edge re-triggering
on /NMI.

Workspace fields written:

| Address / label | Value | Role |
|---|---|---|
| `tx_src_net`         | `0`    | clear |
| `need_release_tube`  | `0`    | clear |
| `tx_op_type`         | `0`    | clear |
| `tx_src_stn` (`&0D22`) | station ID | from `(net_rx_ptr)+1` |
| `tx_complete_flag`   | `&80`  | mark idle |
| `econet_init_flag`   | `&80`  | mark initialised |

Finally re-enables NMIs via INTON (`enable_net_nmis` read).""",
)


d.comment(0x8072, "Copy NMI shim from ROM to &0D0C area", align=Align.INLINE)
d.label(0x8074, "copy_nmi_shim")

d.comment(0x8074, "Read byte from NMI shim ROM source", align=Align.INLINE)
d.comment(0x8077, "Write to NMI shim RAM (start of NFS workspace)", align=Align.INLINE)
d.comment(0x807A, "Next byte (descending)", align=Align.INLINE)
d.comment(0x807B, "Loop until all 32 bytes copied", align=Align.INLINE)
d.comment(0x807D, "Patch current ROM bank into NMI shim", align=Align.INLINE)
d.comment(0x807F, "Self-modifying code: ROM bank at &0D07", align=Align.INLINE)
d.comment(0x8082, "Clear source network (Y=0 from copy loop)", align=Align.INLINE)
d.comment(0x8085, "Clear Tube release flag", align=Align.INLINE)
d.comment(0x8087, "Clear TX operation type", align=Align.INLINE)
d.comment(0x808A, "Y=1: tx_src_stn offset in NMI block", align=Align.INLINE)
d.comment(0x808C, "Read TX source station from (net_rx_ptr)+1", align=Align.INLINE)
d.comment(0x808E, "Store as tx_src_stn", align=Align.INLINE)
d.comment(0x8091, "&80 = Econet initialised", align=Align.INLINE)
d.comment(0x8093, "Mark TX as complete (ready)", align=Align.INLINE)
d.comment(0x8096, "Mark Econet as initialised", align=Align.INLINE)
d.comment(0x8099, "INTON: re-enable NMIs (Master &FE3C)", align=Align.INLINE)
d.label(0x809C, "adlc_init_done")

d.comment(0x809C, "Return", align=Align.INLINE)
d.entry(0x809D)
d.subroutine(
    0x809D,
    "nmi_rx_scout",
    title="NMI RX scout handler (initial byte)",
    description="""Default NMI handler for incoming scout frames. Checks whether the
frame is addressed to us or is a broadcast. Installed as the NMI
target during idle RX listen mode.

Tests `SR2` bit 0 (`AP` = Address Present) to detect incoming
data. Reads the first byte (destination station) from the RX FIFO
and compares it against our station ID (the workspace copy in
`tx_src_stn`).""",
)


d.comment(0x809D, "A=&01: mask for SR2 bit0 (AP = Address Present)", align=Align.INLINE)
d.comment(0x809F, "Z = A AND SR2 -- tests if AP is set", align=Align.INLINE)
d.comment(0x80A2, "AP not set, no incoming data -- check for errors", align=Align.INLINE)
d.comment(0x80A4, "Read first RX byte (destination station address)", align=Align.INLINE)
d.comment(0x80A7, "Compare to our station ID (tx_src_stn copy)", align=Align.INLINE)
d.comment(0x80AA, "Match -- accept frame", align=Align.INLINE)
d.comment(0x80AC, "Check for broadcast address (&FF)", align=Align.INLINE)
d.comment(0x80AE, "Neither our address nor broadcast -- reject frame", align=Align.INLINE)
d.comment(0x80B0, "Flag &40 = broadcast frame", align=Align.INLINE)
d.comment(0x80B2, "Store broadcast flag in net_frame_flags", align=Align.INLINE)
d.label(0x80B5, "accept_frame")

d.comment(0x80B5, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x80B7, "Install next handler", align=Align.INLINE)
d.entry(0x80BA)
d.subroutine(
    0x80BA,
    "nmi_rx_scout_net",
    title="RX scout second byte handler",
    description="""Reads the second byte of an incoming scout (destination network).

| Value | Meaning | Action |
|---|---|---|
| `0`   | local network | accept |
| `&FF` | broadcast | accept and flag |
| other | foreign network | reject |

Installs [`copy_scout_to_buffer`](label:copy_scout_to_buffer) as the
scout-data reading loop handler.""",
)


d.comment(0x80BA, "Test SR2 for RDA (bit7 = data available)", align=Align.INLINE)
d.comment(0x80BD, "No RDA -- check errors", align=Align.INLINE)
d.comment(0x80BF, "Read destination network byte", align=Align.INLINE)
d.comment(0x80C2, "Network = 0 -- local network, accept", align=Align.INLINE)
d.comment(0x80C4, "Test if network = &FF (broadcast)", align=Align.INLINE)
d.comment(0x80C6, "Broadcast network -- accept", align=Align.INLINE)
d.label(0x80C8, "scout_reject")

d.comment(0x80C8, "Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE", align=Align.INLINE)
d.comment(0x80CA, "Write CR1 to discontinue RX", align=Align.INLINE)
d.comment(0x80CD, "Return to idle scout listening", align=Align.INLINE)
d.label(0x80D0, "accept_local_net")

d.comment(0x80D0, "Network = 0 (local): clear tx_flags", align=Align.INLINE)
d.label(0x80D3, "accept_scout_net")

d.comment(0x80D3, "Store Y offset for scout data buffer", align=Align.INLINE)
d.comment(0x80D5, "Install scout-data reader (low)", align=Align.INLINE)
d.comment(0x80D7, "Install scout data loop", align=Align.INLINE)
d.subroutine(
    0x80DA,
    "scout_error",
    title="Scout error/discard handler",
    description="""Handles scout reception errors and end-of-frame conditions. Reads
`SR2` and tests `AP|RDA` (bits 0 and 7):

- **Neither set** – the frame ended cleanly; simply discard.
- **Either set** – unexpected data is present; perform a full ADLC
  reset.

Also serves as the common discard path for address/network
mismatches from [`nmi_rx_scout`](label:nmi_rx_scout) and
[`scout_complete`](label:scout_complete) – reached by 5 branch sites
across the scout reception chain.""",
)


d.comment(0x80DA, "Read SR2", align=Align.INLINE)
d.comment(0x80DD, "Test AP (b0) | RDA (b7)", align=Align.INLINE)
d.comment(0x80DF, "Neither set -- clean end, discard frame", align=Align.INLINE)
d.comment(0x80E1, "Unexpected data/status: full ADLC reset", align=Align.INLINE)
d.comment(0x80E4, "Discard and return to idle", align=Align.INLINE)
d.label(0x80E7, "scout_discard")

d.comment(0x80E7, "Gentle discard: RX_DISCONTINUE", align=Align.INLINE)
d.entry(0x80EA)
d.comment(0x80EA, "Y = buffer offset", align=Align.INLINE)
d.comment(0x80EC, "Read SR2", align=Align.INLINE)
d.label(0x80EF, "scout_loop_rda")

d.comment(0x80EF, "No RDA -- error handler", align=Align.INLINE)
d.comment(0x80F1, "Read data byte from RX FIFO", align=Align.INLINE)
d.comment(0x80F4, "Store at &0D3D+Y (scout buffer)", align=Align.INLINE)
d.comment(0x80F7, "Advance buffer index", align=Align.INLINE)
d.comment(0x80F8, "Read SR2 again (FV detection point)", align=Align.INLINE)
d.comment(0x80FB, "RDA set -- more data, read second byte", align=Align.INLINE)
d.comment(0x80FD, "SR2 non-zero (FV or other) -- scout completion", align=Align.INLINE)
d.label(0x80FF, "scout_loop_second")

d.comment(0x80FF, "Read second byte of pair", align=Align.INLINE)
d.comment(0x8102, "Store at &0D3D+Y", align=Align.INLINE)
d.comment(0x8105, "Advance and check buffer limit", align=Align.INLINE)
d.comment(0x8106, "Copied all 12 scout bytes?", align=Align.INLINE)
d.comment(0x8108, "Buffer full (Y=12) -- force completion", align=Align.INLINE)
d.comment(0x810A, "Save final buffer offset", align=Align.INLINE)
d.comment(0x810C, "Read SR2 for next pair", align=Align.INLINE)
d.comment(0x810F, "SR2 non-zero -- loop back for more bytes", align=Align.INLINE)
d.comment(0x8111, "SR2 = 0 -- wait for next NMI", align=Align.INLINE)
d.subroutine(
    0x8114,
    "scout_complete",
    title="Scout completion handler",
    description="""Processes a completed scout frame. Writes `CR1=&00` and `CR2=&84`
to disable `PSE` and suppress `FV`, then tests `SR2` for `FV`
(frame valid). If `FV` is set with `RDA`, reads the remaining
scout data bytes in pairs into the buffer at `&0D3D`.

Matches the port byte (`&0D40`) against open receive control
blocks to find a listener:

- **On match** – calculates the transfer size via
  [`tx_calc_transfer`](label:tx_calc_transfer), sets up the data RX
  handler chain, and sends a scout ACK.
- **On no match or error** – discards the frame via
  [`scout_error`](label:scout_error).""",
)


d.comment(0x8114, "Save Y for next iteration", align=Align.INLINE)
d.comment(0x8116, "Write CR1", align=Align.INLINE)
d.comment(0x8119, "CR2=&84: disable PSE, enable RDA_SUPPRESS_FV", align=Align.INLINE)
d.comment(0x811B, "Write CR2", align=Align.INLINE)
d.comment(0x811E, "A=&02: FV mask for SR2 bit1", align=Align.INLINE)
d.comment(0x8120, "Test SR2 FV (Z) and RDA (N)", align=Align.INLINE)
d.comment(0x8123, "No FV -- not a valid frame end, error", align=Align.INLINE)
d.comment(0x8125, "FV set but no RDA -- missing last byte, error", align=Align.INLINE)
d.comment(0x8127, "Read last byte from RX FIFO", align=Align.INLINE)
d.comment(0x812A, "Store last byte at &0D3D+Y", align=Align.INLINE)
d.comment(0x812D, "CR1=&44: RX_RESET | TIE (switch to TX for ACK)", align=Align.INLINE)
d.comment(0x812F, "Write CR1: switch to TX mode", align=Align.INLINE)
d.comment(0x8132, "Set bit7 of need_release_tube flag", align=Align.INLINE)
d.comment(0x8133, "Rotate C=1 into bit7: mark Tube release needed", align=Align.INLINE)
d.comment(0x8135, "Check port byte: 0 = immediate op, non-zero = data transfer", align=Align.INLINE)
d.comment(0x8138, "Port non-zero -- look for matching receive block", align=Align.INLINE)
d.label(0x813A, "scout_no_match")

d.comment(0x813A, "Port = 0 -- immediate operation handler", align=Align.INLINE)
d.label(0x813D, "scout_match_port")

d.comment(0x813D, "Check if broadcast (bit6 of tx_flags)", align=Align.INLINE)
d.comment(0x8140, "Not broadcast -- skip CR2 setup", align=Align.INLINE)
d.comment(0x8142, "CR2=&07: broadcast prep", align=Align.INLINE)
d.comment(0x8144, "Write CR2: broadcast frame prep", align=Align.INLINE)
d.label(0x8147, "scan_port_list")

d.comment(0x8147, "Check if RX port list active (bit7)", align=Align.INLINE)
d.comment(0x814A, "No active ports -- try NFS workspace", align=Align.INLINE)
d.comment(0x814C, "Start scanning port list at page &C0", align=Align.INLINE)
d.comment(0x814E, "Y=0: start offset within each port slot", align=Align.INLINE)
d.label(0x8151, "scan_nfs_port_list")

d.comment(0x8151, "Store page to workspace pointer low", align=Align.INLINE)
d.comment(0x8153, "Store page high byte for slot scanning", align=Align.INLINE)
d.label(0x8155, "check_port_slot")

d.comment(0x8155, "Y=0: read control byte from start of slot", align=Align.INLINE)
d.label(0x8157, "scout_ctrl_check")

d.comment(0x8157, "Read port control byte from slot", align=Align.INLINE)
d.comment(0x8159, "Zero = end of port list, no match", align=Align.INLINE)
d.comment(0x815B, "&7F = any-port wildcard", align=Align.INLINE)
d.comment(0x815D, "Not wildcard -- check specific port match", align=Align.INLINE)
d.comment(0x815F, "Y=1: advance to port byte in slot", align=Align.INLINE)
d.comment(0x8160, "Read port number from slot (offset 1)", align=Align.INLINE)
d.comment(0x8162, "Zero port in slot = match any port", align=Align.INLINE)
d.comment(0x8164, "Check if port matches this slot", align=Align.INLINE)
d.comment(0x8167, "Port mismatch -- try next slot", align=Align.INLINE)
d.label(0x8169, "check_station_filter")

d.comment(0x8169, "Y=2: advance to station byte", align=Align.INLINE)
d.comment(0x816A, "Read station filter from slot (offset 2)", align=Align.INLINE)
d.comment(0x816C, "Zero station = match any station, accept", align=Align.INLINE)
d.comment(0x816E, "Check if source station matches", align=Align.INLINE)
d.comment(0x8171, "Station mismatch -- try next slot", align=Align.INLINE)
d.label(0x8173, "scout_port_match")

d.comment(0x8173, "Y=3: advance to network byte", align=Align.INLINE)
d.comment(0x8174, "Read network filter from slot (offset 3)", align=Align.INLINE)
d.comment(0x8176, "Zero = accept any network", align=Align.INLINE)
d.comment(0x8178, "Check if source network matches", align=Align.INLINE)
d.comment(0x817B, "Network matches or zero = accept", align=Align.INLINE)
d.label(0x817D, "next_port_slot")

d.comment(0x817D, "Check if NFS workspace search pending", align=Align.INLINE)
d.comment(0x817F, "No NFS workspace -- try fallback path", align=Align.INLINE)
d.comment(0x8181, "Load current slot base address", align=Align.INLINE)
d.comment(0x8183, "For 12-byte slot advance", align=Align.INLINE)
d.comment(0x8184, "Advance to next 12-byte port slot", align=Align.INLINE)
d.comment(0x8186, "Update workspace pointer to next slot", align=Align.INLINE)
d.comment(0x8188, "Always branches (page &C0 won't overflow)", align=Align.INLINE)
d.label(0x818A, "discard_no_match")

d.comment(0x818A, "No match found -- discard frame", align=Align.INLINE)
d.label(0x818D, "try_nfs_port_list")

d.comment(0x818D, "Try NFS workspace if paged list exhausted", align=Align.INLINE)
d.comment(0x8190, "No NFS workspace RX (bit6 clear) -- discard", align=Align.INLINE)
d.comment(0x8192, "NFS workspace starts at offset 0 in page", align=Align.INLINE)
d.comment(0x8194, "NFS workspace high byte for port list", align=Align.INLINE)
d.comment(0x8196, "Scan NFS workspace port list", align=Align.INLINE)
d.label(0x8198, "port_match_found")

d.subroutine(
    0x8198,
    "port_match_found",
    title="Scout matched: arm data RX, ACK or discard",
    description="""Sets `scout_status=3` (match found) at `rx_port`, calls
[`tx_calc_transfer`](label:tx_calc_transfer) to compute the transfer
parameters from the RXCB, then triages:

| Carry | `net_frame_flags` (V) | Action |
|---|---|---|
| `C=0` | – | no Tube claimed → [`nmi_error_dispatch`](label:nmi_error_dispatch) (discard) |
| `C=1` | broadcast | discard (broadcasts get no ACK) |
| `C=1` | unicast   | [`send_data_rx_ack`](label:send_data_rx_ack) |

Four inbound refs (one `JSR` from `&84B9` and three branches from
the [`scout_complete`](label:scout_complete) dispatch).""",
    on_exit={"a": "3 (scout_status)"},
)


d.comment(0x8198, "Match found: set scout_status = 3", align=Align.INLINE)
d.comment(0x819A, "Record match for completion handler", align=Align.INLINE)
d.comment(0x819D, "Calculate transfer parameters", align=Align.INLINE)
d.comment(0x81A0, "C=0: no Tube claimed -- discard", align=Align.INLINE)
d.comment(0x81A2, "Check broadcast flag for ACK path", align=Align.INLINE)
d.comment(0x81A5, "Not broadcast -- normal ACK path", align=Align.INLINE)
d.comment(0x81A7, "Broadcast: different completion path", align=Align.INLINE)
d.label(0x81AA, "send_data_rx_ack")

d.subroutine(
    0x81AA,
    "send_data_rx_ack",
    title="Send scout ACK and arm data-RX continuation",
    description="""Switches the ADLC to TX mode for the scout ACK frame: writes
`CR1=&44` (`RX_RESET | TIE`), `CR2=&A7` (`RTS | CLR_TX_ST |
FC_TDRA | PSE`), then loads `(A,Y) = (&B8, &81)` – the address
of [`data_rx_setup`](label:data_rx_setup) – and `JMP`s to
[`ack_tx_write_dest`](label:ack_tx_write_dest) which saves the pair into
`saved_nmi_lo`/`saved_nmi_hi` (so the NMI handler will install it
later) and writes the ACK destination address bytes to the TX
FIFO.

Two callers: the dispatch in [`scout_complete`](label:scout_complete)
at `&81A2` and the immediate-op POKE path at `&84AE`
(`jmp_send_data_rx_ack`).""",
    on_exit={"a": "&B8 (low byte of data_rx_setup)", "y": "&81 (high byte of data_rx_setup)"},
)


d.comment(0x81AA, "CR1=&44: RX_RESET | TIE", align=Align.INLINE)
d.comment(0x81AC, "Write CR1: TX mode for ACK", align=Align.INLINE)
d.comment(0x81AF, "CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE", align=Align.INLINE)
d.comment(0x81B1, "Write CR2: enable TX with PSE", align=Align.INLINE)
d.comment(0x81B4, "Install data_rx_setup at &81B8", align=Align.INLINE)
d.comment(0x81B6, "High byte of data_rx_setup handler", align=Align.INLINE)
d.comment(0x81B8, "Send ACK with data_rx_setup as next NMI", align=Align.INLINE)
d.label(0x81BB, "data_rx_setup")

d.entry(0x81BB)
d.subroutine(
    0x81BB,
    "data_rx_setup",
    title="NMI handler: switch ADLC to RX for the data frame",
    description="""NMI continuation entry installed by
[`send_data_rx_ack`](label:send_data_rx_ack) (which pushes
`(&81B8 - 1)` on the stack and routes it through
[`ack_tx_write_dest`](label:ack_tx_write_dest)). When the next NMI fires,
this body writes `CR1 = &82` (`TX_RESET | RIE`) to switch the
ADLC from scout-ACK TX mode to data-frame RX mode, then `JMP`s to
`install_nmi_handler` to install
[`nmi_data_rx`](label:nmi_data_rx) as the next NMI handler.""",
)


d.comment(0x81BB, "CR1=&82: TX_RESET | RIE (switch to RX for data frame)", align=Align.INLINE)
d.comment(0x81BD, "Write CR1: switch to RX for data frame", align=Align.INLINE)
d.comment(0x81C0, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x81C2, "Install nmi_data_rx and return from NMI", align=Align.INLINE)
d.entry(0x81C5)
d.subroutine(
    0x81C5,
    "nmi_data_rx",
    title="Data frame RX handler (four-way handshake)",
    description="""Receives the data frame after the scout ACK has been sent. First
checks AP (Address Present) for the start of the data frame. Reads
and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: this routine (AP + dest-stn check) →
[`nmi_data_rx_net`](label:nmi_data_rx_net) (dest-net check) →
[`nmi_data_rx_skip`](label:nmi_data_rx_skip) (skip ctrl + port) →
[`nmi_data_rx_bulk`](label:nmi_data_rx_bulk) (bulk data read) →
[`data_rx_complete`](label:data_rx_complete) (completion).""",
)


d.comment(0x81C5, "A=1: AP mask for SR2 bit test", align=Align.INLINE)
d.comment(0x81C7, "Test SR2 AP bit", align=Align.INLINE)
d.comment(0x81CA, "No AP: wrong frame or error", align=Align.INLINE)
d.comment(0x81CC, "Read first byte (dest station)", align=Align.INLINE)
d.comment(0x81CF, "Compare to our station ID (tx_src_stn copy)", align=Align.INLINE)
d.comment(0x81D2, "Not for us: error path", align=Align.INLINE)
d.comment(0x81D4, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x81D6, "Set NMI vector via RAM shim", align=Align.INLINE)
d.label(0x81D9, "nmi_data_rx_net")

d.entry(0x81D9)
d.subroutine(
    0x81D9,
    "nmi_data_rx_net",
    title="NMI handler: validate dest-net byte of data frame",
    description="""NMI continuation entry installed by [`nmi_data_rx`](label:nmi_data_rx)
once the AP and dest-station bytes have validated. Polls SR2
(`BIT econet_control23_or_status2`); on no RDA, branches to
[`nmi_error_dispatch`](label:nmi_error_dispatch). Otherwise reads the dest-
network byte from the ADLC FIFO and falls through to the
control/port skip step.""",
    on_exit={"a": "dest-network byte (validated against local)"},
)


d.comment(0x81D9, "Validate source network = 0", align=Align.INLINE)
d.comment(0x81DC, "SR2 bit7 clear: no data ready -- error", align=Align.INLINE)
d.comment(0x81DE, "Read dest network byte", align=Align.INLINE)
d.comment(0x81E1, "Network != 0: wrong network -- error", align=Align.INLINE)
d.comment(0x81E3, "Install skip handler at &8211", align=Align.INLINE)
d.comment(0x81E5, "High byte of &8211 handler", align=Align.INLINE)
d.comment(0x81E7, "SR1 bit7: IRQ, data already waiting", align=Align.INLINE)
d.comment(0x81EA, "Data ready: skip directly, no return", align=Align.INLINE)
d.comment(0x81EC, "Install handler and return", align=Align.INLINE)
d.label(0x81EF, "nmi_data_rx_skip")

d.entry(0x81EF)
d.subroutine(
    0x81EF,
    "nmi_data_rx_skip",
    title="NMI handler: skip control + port bytes",
    description="""NMI continuation entry that consumes the control and port bytes of
the data frame (already known from the scout) and proceeds to the
bulk-data-read continuation. Polls SR2 for RDA on entry; on no
RDA, branches to [`nmi_error_dispatch`](label:nmi_error_dispatch).""",
)


d.comment(0x81EF, "Test SR2 RDA (RX data byte ready)", align=Align.INLINE)
d.comment(0x81F2, "SR2 bit7 clear: error", align=Align.INLINE)
d.comment(0x81F4, "Discard control byte", align=Align.INLINE)
d.comment(0x81F7, "Discard port byte", align=Align.INLINE)
d.label(0x81FA, "install_data_rx_handler")

d.subroutine(
    0x81FA,
    "install_data_rx_handler",
    title="Install data RX bulk or Tube handler",
    description="""Selects between the normal bulk-RX handler at
[`nmi_data_rx_bulk`](label:nmi_data_rx_bulk) and the Tube RX handler at
[`nmi_data_rx_tube`](label:nmi_data_rx_tube) based on bit 1 of
`net_frame_flags` (`tx_flags`).

| `net_frame_flags` bit 1 | Handler |
|---|---|
| clear | [`nmi_data_rx_bulk`](label:nmi_data_rx_bulk) (`A=&23`, `Y=&82`) |
| set   | [`nmi_data_rx_tube`](label:nmi_data_rx_tube) (`A=&91`, `Y=&82`) |

In the bulk path, after loading the handler address, checks `SR1`
bit 7. If `IRQ` is already asserted (more data waiting), jumps
directly to [`nmi_data_rx_bulk`](label:nmi_data_rx_bulk) to avoid NMI
re-entry overhead. Otherwise installs the handler via
[`set_nmi_vector`](label:set_nmi_vector) (the `(A,Y)` pair becomes the
NMI dispatch target) and returns via `RTI`.""",
)


d.comment(0x81FA, "A=2: Tube transfer flag mask", align=Align.INLINE)
d.comment(0x81FC, "Check if Tube transfer active", align=Align.INLINE)
d.comment(0x81FF, "Tube active: use Tube RX path", align=Align.INLINE)
d.comment(0x8201, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8203, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x8205, "SR1 bit7: more data already waiting?", align=Align.INLINE)
d.comment(0x8208, "Yes: enter bulk read directly", align=Align.INLINE)
d.comment(0x820A, "No: install handler", align=Align.INLINE)
d.label(0x820D, "install_tube_rx")

d.comment(0x820D, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x820F, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x8211, "Install Tube handler", align=Align.INLINE)
d.comment(
    0x8214,
    """Page-overflow exit from nmi_data_rx_bulk: restores the Master 128 ACCCON
that was saved at &822A before falling through to the RXCB-update path.""",
)
d.comment(0x8214, "Pull saved ACCCON from stack", align=Align.INLINE)
d.label(0x8214, "page_boundary_restore")

d.comment(0x8215, "Restore caller's ACCCON on page-overflow exit", align=Align.INLINE)
d.label(0x8218, "nmi_error_dispatch")

d.subroutine(
    0x8218,
    "nmi_error_dispatch",
    title="NMI error handler dispatch",
    description="""Common error/abort entry used by 11 call sites. The dispatch byte
at [`net_frame_flags`](label:net_frame_flags) doubles as a TX-state flag here:
bit 7 distinguishes whether the NMI handler reached this point on
an RX-error path or a TX not-listening path.

| `net_frame_flags` bit 7 | Path |
|---|---|
| clear | RX error – full ADLC reset; return to idle listen |
| set   | TX not-listening – `JMP` [`tx_result_fail`](label:tx_result_fail) |

**What raises the NMI that lands here after an unanswered
transmit.** While waiting for a scout ACK or final ACK the ADLC
runs with CR1 = &82 (TX_RESET | RIE), so receiver conditions
raise the interrupt. A listening station holds the line in flag
fill; the *absence* of a listener lets the line fall to all-ones
idle, which latches SR2 bit 2 (Inactive Idle Received). SR2's
stored conditions (all but RDA) are ORed into SR1 bit 1 (S2RQ),
and RIE turns that into the NMI. The handler then finds AP
clear and falls through to the error path. In other words the
interrupt meaning "nobody answered" is the line going idle,
not a timeout — see [`poll_adlc_tx_status`](label:poll_adlc_tx_status)
for the consequence when that interrupt never arrives.""",
)


d.comment(0x8218, "Check tx_flags for error path", align=Align.INLINE)
d.comment(0x821B, "Bit7 clear: RX error path", align=Align.INLINE)
d.comment(0x821D, "Bit7 set: TX result = not listening", align=Align.INLINE)
d.label(0x8220, "rx_error_reset")

d.comment(0x8220, "Full ADLC reset on RX error", align=Align.INLINE)
d.comment(0x8223, "Discard and return to idle listen", align=Align.INLINE)
d.entry(0x8226)
d.subroutine(
    0x8226,
    "nmi_data_rx_bulk",
    title="Data frame bulk read loop",
    description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at `(open_port_buf),Y`. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.

- SR2 non-zero (FV or other) → completion via
  [`data_rx_complete`](label:data_rx_complete).
- SR2 = 0 → RTI, wait for next NMI to continue.""",
)


d.comment(0x8226, "Y = buffer offset, resume from last position", align=Align.INLINE)
d.comment(0x8228, "Read SR2 for next pair", align=Align.INLINE)
d.label(0x822B, "data_rx_loop")

d.comment(0x822B, "SR2 bit7 clear: frame complete (FV)", align=Align.INLINE)
d.comment(
    0x822D,
    """Save/restore ACCCON across the (open_port_buf),Y stores
in this bulk-read loop. Same idiom as in copy_scout_to_buffer; workspace
&97 holds the desired ACCCON value pre-loaded by the caller.""",
)
d.comment(0x822D, "Save current ACCCON on stack", align=Align.INLINE)
d.comment(0x8230, "Push ACCCON snapshot", align=Align.INLINE)
d.comment(0x8231, "Load desired ACCCON from workspace &97", align=Align.INLINE)
d.comment(0x8233, "Set ACCCON for the upcoming buffer stores", align=Align.INLINE)
d.comment(0x8236, "Read first byte of pair from RX FIFO", align=Align.INLINE)
d.comment(0x8239, "Store byte to buffer", align=Align.INLINE)
d.comment(0x823B, "Advance buffer offset", align=Align.INLINE)
d.comment(0x823C, "Y != 0: no page boundary crossing", align=Align.INLINE)
d.comment(0x823E, "Crossed page: increment buffer high byte", align=Align.INLINE)
d.comment(0x8240, "Decrement remaining page count", align=Align.INLINE)
d.comment(0x8242, "No pages left: handle as complete", align=Align.INLINE)
d.label(0x8244, "read_sr2_between_pairs")

d.comment(0x8244, "Read SR2 between byte pairs", align=Align.INLINE)
d.comment(0x8247, "SR2 bit7 set: more data available", align=Align.INLINE)
d.comment(0x8249, "SR2 non-zero, bit7 clear: frame done", align=Align.INLINE)
d.label(0x824B, "read_second_rx_byte")

d.comment(0x824B, "Read second byte of pair from RX FIFO", align=Align.INLINE)
d.comment(0x824E, "Store byte to buffer", align=Align.INLINE)
d.comment(0x8250, "Advance buffer offset", align=Align.INLINE)
d.comment(0x8251, "Save updated buffer position", align=Align.INLINE)
d.comment(0x8253, "Y != 0: no page boundary crossing", align=Align.INLINE)
d.comment(0x8255, "Crossed page: increment buffer high byte", align=Align.INLINE)
d.comment(0x8257, "Decrement remaining page count", align=Align.INLINE)
d.comment(0x8259, "No pages left: frame complete", align=Align.INLINE)
d.comment(0x825B, "Pull saved ACCCON from stack", align=Align.INLINE)
d.label(0x825B, "byte_pair_restore")

d.comment(0x825C, "Restore caller's ACCCON between byte pairs", align=Align.INLINE)
d.label(0x825F, "check_sr2_loop_again")

d.comment(0x825F, "Re-poll ADLC SR2 for next byte pair", align=Align.INLINE)
d.comment(0x8262, "More data: loop back to data_rx_loop", align=Align.INLINE)
d.comment(0x8264, "No more data: return from NMI", align=Align.INLINE)
d.comment(0x8267, "Pull saved ACCCON (frame-complete path)", align=Align.INLINE)
d.label(0x8267, "frame_complete_restore")

d.comment(0x8268, "Restore caller's ACCCON before completion", align=Align.INLINE)
d.subroutine(
    0x826B,
    "data_rx_complete",
    title="Data frame completion",
    description="""Reached when `SR2` non-zero during data RX (`FV` detected). Same
pattern as scout completion: disables `PSE` (`CR2=&84`, `CR1=&00`),
then tests `FV` and `RDA`. If `FV+RDA`, reads the last byte; if
extra data is available and buffer space remains, stores it.
Proceeds to send the final ACK via [`ack_tx`](label:ack_tx).""",
)


d.comment(0x826B, "A=&84: CR2 value (disable PSE)", align=Align.INLINE)
d.comment(0x826D, "Write CR2 = &84 to disable PSE for bit testing", align=Align.INLINE)
d.comment(0x8270, "A=0: CR1 value (disable all interrupts)", align=Align.INLINE)
d.comment(0x8272, "Write CR1 = 0 to disable all interrupts", align=Align.INLINE)
d.comment(0x8275, "Save Y (byte count from data RX loop)", align=Align.INLINE)
d.comment(0x8277, "A=&02: FV mask", align=Align.INLINE)
d.comment(0x8279, "Test SR2 FV (Z) and RDA (N)", align=Align.INLINE)
d.comment(0x827C, "No FV -- error", align=Align.INLINE)
d.comment(0x827E, "FV set, no RDA -- proceed to ACK", align=Align.INLINE)
d.comment(0x8280, "Check if buffer space remains", align=Align.INLINE)
d.label(0x8282, "read_last_rx_byte")

d.comment(0x8282, "No buffer space: error/discard frame", align=Align.INLINE)
d.comment(0x8284, "FV+RDA: read and store last data byte", align=Align.INLINE)
d.comment(0x8290, "Y = current buffer write offset", align=Align.INLINE)
d.comment(0x8292, "Store last byte in port receive buffer", align=Align.INLINE)
d.comment(0x8298, "Advance buffer write offset", align=Align.INLINE)
d.comment(0x829A, "No page wrap: proceed to send ACK", align=Align.INLINE)
d.comment(0x829C, "Page boundary: advance buffer page", align=Align.INLINE)
d.label(0x829E, "send_ack")

d.comment(0x829E, "Send ACK frame to complete handshake", align=Align.INLINE)
d.label(0x82A1, "nmi_data_rx_tube")

d.entry(0x82A1)
d.subroutine(
    0x82A1,
    "nmi_data_rx_tube",
    title="NMI handler: data-frame RX into Tube buffer",
    description="""NMI continuation entry for the Tube data-RX path. Polls SR2 for
RDA, reads the next data byte from the ADLC RX FIFO, and writes it
to the Tube data register, advancing the Tube transfer pointer
each iteration. Tests for end-of-frame via FV and either continues
the tight inner loop or returns via `RTI`. Reached only via the
NMI vector after `install_tube_rx` configures the handler.""",
)


d.comment(0x82A1, "Read SR2 for Tube data receive path", align=Align.INLINE)
d.label(0x82A4, "rx_tube_data")

d.comment(0x82A4, "RDA clear: no more data, frame complete", align=Align.INLINE)
d.comment(0x82A6, "Read data byte from ADLC RX FIFO", align=Align.INLINE)
d.comment(0x82A9, "Check buffer limits and transfer size", align=Align.INLINE)
d.comment(0x82AC, "Zero: buffer full, handle as error", align=Align.INLINE)
d.comment(0x82AE, "Send byte to Tube data register 3", align=Align.INLINE)
d.comment(0x82B1, "Read second data byte (paired transfer)", align=Align.INLINE)
d.comment(0x82B4, "Send second byte to Tube", align=Align.INLINE)
d.comment(0x82B7, "Check limits after byte pair", align=Align.INLINE)
d.comment(0x82BA, "Zero: Tube transfer complete", align=Align.INLINE)
d.comment(0x82BC, "Re-read SR2 for next byte pair", align=Align.INLINE)
d.comment(0x82BF, "More data available: continue loop", align=Align.INLINE)
d.label(0x82C1, "data_rx_tube_error")

d.comment(0x82C1, "Unexpected end: return from NMI", align=Align.INLINE)
d.label(0x82C4, "data_rx_tube_complete")

d.comment(0x82C4, "CR1=&00: disable all interrupts", align=Align.INLINE)
d.comment(0x82C6, "Write CR1 for individual bit testing", align=Align.INLINE)
d.comment(0x82C9, "CR2=&84: disable PSE", align=Align.INLINE)
d.comment(0x82CB, "Write CR2: same pattern as main path", align=Align.INLINE)
d.comment(0x82CE, "A=&02: FV mask for Tube completion", align=Align.INLINE)
d.comment(0x82D0, "Test SR2 FV (Z) and RDA (N)", align=Align.INLINE)
d.comment(0x82D3, "No FV: incomplete frame, error", align=Align.INLINE)
d.comment(0x82D5, "FV set, no RDA: proceed to ACK", align=Align.INLINE)
d.comment(0x82D7, "Check if any buffer was allocated", align=Align.INLINE)
d.comment(0x82D9, "OR all 4 buffer pointer bytes together", align=Align.INLINE)
d.comment(0x82DB, "Check buffer low byte", align=Align.INLINE)
d.comment(0x82DD, "Check buffer high byte", align=Align.INLINE)
d.comment(0x82DF, "All zero (null buffer): error", align=Align.INLINE)
d.comment(0x82E1, "Read extra trailing byte from FIFO", align=Align.INLINE)
d.comment(0x82E4, "Save extra byte in workspace for later use", align=Align.INLINE)
d.comment(0x82E7, "Bit5 = extra data byte available flag", align=Align.INLINE)
d.comment(0x82E9, "Set extra byte flag in tx_flags", align=Align.INLINE)
d.comment(0x82EC, "Store updated flags", align=Align.INLINE)
d.subroutine(
    0x82EF,
    "ack_tx",
    title="ACK transmission",
    description="""Sends a scout ACK or final ACK frame as part of the four-way
handshake. Tests bit 7 of [`net_frame_flags`](label:net_frame_flags) (used as
TX-flags here): if set this is a final ACK and completion runs
through [`tx_result_ok`](label:tx_result_ok). Otherwise configures
for TX (`CR1=&44`, `CR2=&A7`) and writes the ACK address frame:
destination station from [`scout_buf`](label:scout_buf), destination
network from [`scout_src_net`](label:scout_src_net), source station
from the workspace copy [`tx_src_stn`](label:tx_src_stn), and
`src_net=0`. The ACK frame has no data payload -- just address
bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from `saved_nmi_lo`/`saved_nmi_hi` (saved by the
scout/data RX handler via [`ack_tx_write_dest`](label:ack_tx_write_dest))
and sends `TX_LAST_DATA` (`CR2=&3F`) to close the frame.""",
)


d.comment(0x82EF, "Load TX flags to check ACK type", align=Align.INLINE)
d.comment(0x82F2, "Bit7 clear: normal scout ACK", align=Align.INLINE)
d.comment(0x82F4, "Final ACK: call completion handler", align=Align.INLINE)
d.comment(0x82F7, "Jump to TX success result", align=Align.INLINE)
d.label(0x82FA, "ack_tx_configure")

d.comment(0x82FA, "CR1=&44: RX_RESET | TIE (switch to TX mode)", align=Align.INLINE)
d.comment(0x82FC, "Write CR1: switch to TX mode", align=Align.INLINE)
d.comment(0x82FF, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE", align=Align.INLINE)
d.comment(0x8301, "Write CR2: enable TX with status clear", align=Align.INLINE)
d.comment(0x8304, "Install saved next handler (scout ACK path)", align=Align.INLINE)
d.comment(0x8306, "High byte of post-ACK handler", align=Align.INLINE)
d.label(0x8308, "ack_tx_write_dest")

d.subroutine(
    0x8308,
    "ack_tx_write_dest",
    title="Begin ACK transmit: write destination address to ADLC",
    description="""First step of the four-byte ACK frame transmission. Saves the
caller-supplied `(A=lo, Y=hi)` next-NMI handler address into
`saved_nmi_lo` / `saved_nmi_hi`, loads the destination station
from [`scout_buf`](label:scout_buf) and tests `SR1` bit 6 (`TDRA`,
TX Data Register Available) via `BIT econet_control1_or_status1`. If `TDRA` is
clear the TX FIFO isn't ready and control branches to
[`dispatch_nmi_error`](label:dispatch_nmi_error) to abort.

When `TDRA` is set, writes the destination station and network
bytes (from [`scout_src_net`](label:scout_src_net)) into `econet_data_continue_frame`, then
installs [`nmi_ack_tx_src`](label:nmi_ack_tx_src) as the next NMI handler
via [`set_nmi_vector`](label:set_nmi_vector) -- that handler will write
the source-address pair on the next NMI.

Two callers: [`send_data_rx_ack`](label:send_data_rx_ack)'s tail `JMP` and
[`imm_op_build_reply`](label:imm_op_build_reply).""",
    on_entry={"a": "low byte of next NMI handler", "y": "high byte of next NMI handler"},
)


d.comment(0x8308, "Store next handler low byte", align=Align.INLINE)
d.comment(0x830B, "Store next handler high byte", align=Align.INLINE)
d.comment(0x830E, "Load dest station from RX scout buffer", align=Align.INLINE)
d.comment(0x8311, "Test SR1 TDRA (V=bit6)", align=Align.INLINE)
d.comment(0x8314, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x8316, "Write dest station to TX FIFO", align=Align.INLINE)
d.comment(0x8319, "Load dest network from RX scout buffer", align=Align.INLINE)
d.comment(0x831C, "Write dest net byte to FIFO", align=Align.INLINE)
d.comment(0x831F, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8321, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x8323, "Set NMI vector to ack_tx_src handler", align=Align.INLINE)
d.entry(0x8326)
d.subroutine(
    0x8326,
    "nmi_ack_tx_src",
    title="ACK TX continuation",
    description="""Continuation of ACK frame transmission, reached via NMI after
[`ack_tx_write_dest`](label:ack_tx_write_dest) installed it as the next
handler. Reads our station ID from the workspace copy
[`tx_src_stn`](label:tx_src_stn), tests `TDRA` via `SR1`, and writes
`(station, network=0)` to the TX FIFO -- completing the 4-byte
ACK address header.

Then dispatches on [`net_frame_flags`](label:net_frame_flags) bit 7 (which the
caller uses as a TX-flags byte):

| Bit 7 | Action |
|---|---|
| set   | branch to `start_data_tx` to begin the data phase |
| clear | write `CR2=&3F` (TX_LAST_DATA) and fall through to [`post_ack_scout`](label:post_ack_scout) |""",
)


d.comment(0x8326, "Load our station ID from workspace copy", align=Align.INLINE)
d.comment(0x8329, "Test SR1 TDRA", align=Align.INLINE)
d.comment(0x832C, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x832E, "Write our station to TX FIFO", align=Align.INLINE)
d.comment(0x8331, "Write network=0 to TX FIFO", align=Align.INLINE)
d.comment(0x8333, "Write network=0 (local) to TX FIFO", align=Align.INLINE)
d.comment(0x8336, "Check tx_flags for data phase", align=Align.INLINE)
d.comment(0x8339, "bit7 set: start data TX phase", align=Align.INLINE)
d.comment(0x833B, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", align=Align.INLINE)
d.subroutine(
    0x833D,
    "post_ack_scout",
    title="Post-ACK scout processing",
    description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer starting at
[`rx_src_stn`](label:rx_src_stn) (scout-ACK destination
addresses). Checks the port byte at
[`rx_port`](label:rx_port) against open receive blocks to find
a matching listener.

- **Match** – sets up the data-RX handler chain for the four-way-
  handshake data phase.
- **No match** – discards the frame.""",
)


d.comment(0x833D, "Write CR2 to clear status after ACK TX", align=Align.INLINE)
d.comment(0x8340, "Install saved handler from &0D4B/&0D4C", align=Align.INLINE)
d.comment(0x8343, "Load saved next handler high byte", align=Align.INLINE)
d.comment(0x8346, "Install next NMI handler", align=Align.INLINE)
d.label(0x8349, "start_data_tx")

d.comment(0x8349, "Jump to start data TX phase", align=Align.INLINE)
d.label(0x834C, "dispatch_nmi_error")

d.comment(0x834C, "Jump to error handler", align=Align.INLINE)
d.label(0x834F, "advance_rx_buffer_ptr")

d.subroutine(
    0x834F,
    "advance_rx_buffer_ptr",
    title="Advance RX buffer pointer after transfer",
    description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.

Reads:

- [`tx_flags`](label:tx_flags) bit 1 – data transfer in progress
- [`tx_flags`](label:tx_flags) bit 5 – Tube transfer
- 4-byte transfer count from `net_tx_ptr,Y` (`Y=8..&0B`)
- RXCB pointer at `(port_ws_offset),Y`

Updates the RXCB in place. Clobbers `A` and `Y`; preserves `X`
across the Tube branch (saved/restored via stack).""",
    on_exit={"a": "&FF when transfer was active, else preserved entry value"},
)


d.comment(0x834F, "A=2: test bit1 of tx_flags", align=Align.INLINE)
d.comment(0x8351, "Check tx_flags data-transfer bit", align=Align.INLINE)
d.comment(0x8354, "Bit1 clear: no transfer -- return", align=Align.INLINE)
d.comment(0x8356, "Init carry for 4-byte add", align=Align.INLINE)
d.comment(0x8357, "Save carry on stack for loop", align=Align.INLINE)
d.comment(0x8358, "Y=8: start at byte 0 of the 4-byte RXCB pointer", align=Align.INLINE)
d.label(0x835B, "add_rxcb_ptr")

d.comment(0x835B, "Load RXCB[Y] (buffer pointer byte)", align=Align.INLINE)
d.comment(0x835D, "Restore carry from stack", align=Align.INLINE)
d.comment(0x835E, "Add transfer count byte", align=Align.INLINE)
d.comment(0x8361, "Store updated pointer back to RXCB", align=Align.INLINE)
d.comment(0x8363, "Next byte", align=Align.INLINE)
d.comment(0x8364, "Save carry for next iteration", align=Align.INLINE)
d.comment(0x8365, "Done 4 bytes? (Y reaches &0C)", align=Align.INLINE)
d.comment(0x8367, "No: continue adding", align=Align.INLINE)
d.comment(0x8369, "Discard final carry", align=Align.INLINE)
d.comment(0x836A, "A=&20: test bit5 of tx_flags", align=Align.INLINE)
d.comment(0x836C, "Check tx_flags Tube bit", align=Align.INLINE)
d.comment(0x836F, "No Tube: skip Tube update", align=Align.INLINE)
d.entry(0x8371)
d.comment(0x8371, "Save X on stack", align=Align.INLINE)
d.comment(0x8372, "Push X", align=Align.INLINE)
d.comment(0x8373, "A=8: offset for Tube address", align=Align.INLINE)
d.comment(0x8375, "For address calculation", align=Align.INLINE)
d.comment(0x8376, "Add workspace base offset", align=Align.INLINE)
d.comment(0x8378, "X = address low for Tube claim", align=Align.INLINE)
d.comment(0x8379, "Y = address high for Tube claim", align=Align.INLINE)
d.comment(0x837B, "A=1: Tube claim type (read)", align=Align.INLINE)
d.comment(0x837D, "Claim Tube address for transfer", align=Align.INLINE)
d.comment(0x8380, "Load extra RX data byte", align=Align.INLINE)
d.comment(0x8383, "Send to Tube via R3", align=Align.INLINE)
d.comment(0x8386, "Init carry for increment", align=Align.INLINE)
d.comment(0x8387, "Y=8: start at byte 0 of the 4-byte RXCB pointer", align=Align.INLINE)
d.label(0x8389, "inc_rxcb_ptr")

d.comment(0x8389, "A=0: add carry only (increment)", align=Align.INLINE)
d.comment(0x838B, "Add carry to pointer byte", align=Align.INLINE)
d.comment(0x838D, "Store back to RXCB", align=Align.INLINE)
d.comment(0x838F, "Next byte", align=Align.INLINE)
d.comment(0x8390, "Keep going while carry propagates", align=Align.INLINE)
d.comment(0x8392, "Restore X from stack", align=Align.INLINE)
d.comment(0x8393, "Transfer to X register", align=Align.INLINE)
d.label(0x8394, "skip_tube_update")

d.comment(0x8394, "A=&FF: return value (transfer done)", align=Align.INLINE)
d.label(0x8396, "return_rx_complete")

d.comment(0x8396, "Return", align=Align.INLINE)
d.entry(0x8398)
d.subroutine(
    0x8398,
    "nmi_post_ack_dispatch",
    title="Post-ACK frame-complete NMI handler",
    description="""Installed by `ack_tx_configure` via
[`saved_nmi_lo`](label:saved_nmi_lo) / [`saved_nmi_hi`](label:saved_nmi_hi).
Fires as an NMI after the ACK frame (CRC + closing flag) has been
fully transmitted by the ADLC. Dispatches on `scout_port`:

| `scout_port` | Control | Target |
|---|---|---|
| `≠ 0` | – | [`rx_complete_update_rxcb`](label:rx_complete_update_rxcb) (finalise data transfer, mark RXCB complete) |
| `0`   | `&82` (POKE) | [`rx_complete_update_rxcb`](label:rx_complete_update_rxcb) (same path) |
| `0`   | other | `imm_op_build_reply` |""",
)


d.comment(0x8398, "Load received port byte", align=Align.INLINE)
d.comment(0x839B, "Port != 0: data transfer frame", align=Align.INLINE)
d.comment(0x839D, "Port=0: load control byte", align=Align.INLINE)
d.comment(0x83A0, "Ctrl = &82 (POKE)?", align=Align.INLINE)
d.comment(0x83A2, "Yes: POKE also needs data transfer", align=Align.INLINE)
d.comment(0x83A4, "Other port-0 ops: immediate dispatch", align=Align.INLINE)
d.label(0x83A7, "rx_complete_update_rxcb")

d.subroutine(
    0x83A7,
    "rx_complete_update_rxcb",
    title="Complete RX and update RXCB",
    description="""Called from [`nmi_post_ack_dispatch`](label:nmi_post_ack_dispatch) after the
final ACK has been transmitted. Finalises the received data
transfer:

1. Calls [`advance_rx_buffer_ptr`](label:advance_rx_buffer_ptr) to update the
   4-byte buffer pointer with the transfer count (and handle Tube
   re-claim if needed).
2. Stores the source station, network, and port into the RXCB.
3. ORs `&80` into the RXCB control byte (bit 7 = complete).

This is the **NMI-to-foreground synchronisation point**:
`wait_net_tx_ack` polls bit 7 of the RXCB control byte to detect
that the reply has arrived.

Falls through to [`discard_reset_rx`](label:discard_reset_rx) to reset
the ADLC to idle RX-listen mode.

**Setting bit 7 also closes the block.** The slot scanner at
[`scout_ctrl_check`](label:scout_ctrl_check) only accepts a
slot whose control byte is exactly &7F; the `ORA #&80` here
turns it into &FF, so from that instruction onwards the slot
matches nothing. An RXCB is one-shot.

The consequence is that the ROM has no duplicate detection on
inbound frames. A retransmission of a reply the ROM has already
consumed walks the port list, matches no open slot, and is
discarded silently at
[`discard_no_match`](label:discard_no_match) — no ACK, no NAK,
no error. On a real Econet wire this cannot arise: the four-way
handshake is synchronous and retransmission is handled beneath
the ROM. The ROM assumes the layer below it de-duplicates,
which is an assumption a datagram transport such as AUN over
UDP does not satisfy.""",
)


d.comment(0x83A7, "Update buffer pointer and check for Tube", align=Align.INLINE)
d.comment(0x83AA, "Transfer not done: skip buffer update", align=Align.INLINE)
d.label(0x83AC, "add_buf_to_base")

d.comment(0x83AC, "Load buffer bytes remaining", align=Align.INLINE)
d.comment(0x83AE, "For address add", align=Align.INLINE)
d.comment(0x83AF, "Add to buffer base address", align=Align.INLINE)
d.comment(0x83B1, "No carry: skip high byte increment", align=Align.INLINE)
d.label(0x83B3, "inc_rxcb_buf_hi")

d.comment(0x83B3, "Carry: increment buffer high byte", align=Align.INLINE)
d.label(0x83B5, "store_buf_ptr_lo")

d.comment(0x83B5, "Y=8: store updated buffer position", align=Align.INLINE)
d.label(0x83B7, "store_rxcb_buf_ptr")

d.comment(0x83B7, "Store updated low byte to RXCB", align=Align.INLINE)
d.comment(0x83B9, "Y=9: buffer high byte offset", align=Align.INLINE)
d.comment(0x83BA, "Load updated buffer high byte", align=Align.INLINE)
d.label(0x83BC, "store_rxcb_buf_hi")

d.comment(0x83BC, "Store high byte to RXCB", align=Align.INLINE)
d.label(0x83BE, "skip_buf_ptr_update")

d.comment(0x83BE, "Check port byte again", align=Align.INLINE)
d.comment(0x83C1, "Port=0: immediate op, discard+listen", align=Align.INLINE)
d.comment(0x83C3, "Load source network from scout buffer", align=Align.INLINE)
d.comment(0x83C6, "Y=3: RXCB source network offset", align=Align.INLINE)
d.comment(0x83C8, "Store source network to RXCB", align=Align.INLINE)
d.comment(0x83CA, "Y=2: source station offset", align=Align.INLINE)
d.comment(0x83CB, "Load source station from scout buffer", align=Align.INLINE)
d.comment(0x83CE, "Store source station to RXCB", align=Align.INLINE)
d.comment(0x83D0, "Y=1: port byte offset", align=Align.INLINE)
d.comment(0x83D1, "Load port byte", align=Align.INLINE)
d.comment(0x83D4, "Store port to RXCB", align=Align.INLINE)
d.comment(0x83D6, "Y=0: control/flag byte offset", align=Align.INLINE)
d.comment(0x83D7, "Load control byte from scout", align=Align.INLINE)
d.comment(0x83DA, "Set bit7: signals wait_net_tx_ack that reply arrived", align=Align.INLINE)
d.comment(0x83DC, "Store to RXCB byte 0 (bit 7 set = complete)", align=Align.INLINE)
d.comment(0x83DE, "Load callback event flags", align=Align.INLINE)
d.comment(0x83E1, "Shift bit 0 into carry", align=Align.INLINE)
d.comment(0x83E2, "Bit 0 clear: no callback, skip to reset", align=Align.INLINE)
d.comment(0x83E4, "Load RXCB workspace pointer low byte (carry set on entry)", align=Align.INLINE)
d.label(0x83E6, "loop_count_rxcb_slot")
d.comment(0x83E6, "Count slots", align=Align.INLINE)
d.comment(0x83E7, "Subtract 12 bytes per RXCB slot", align=Align.INLINE)
d.comment(0x83E9, "Loop until pointer exhausted", align=Align.INLINE)
d.comment(0x83EB, "Adjust for off-by-one", align=Align.INLINE)
d.comment(0x83EC, "Check slot index >= 3", align=Align.INLINE)
d.comment(0x83EE, "Slot < 3: no callback, skip to reset", align=Align.INLINE)
d.comment(0x83F0, "Discard scout and reset listen state", align=Align.INLINE)
d.comment(0x83F3, "Pass slot index as callback parameter", align=Align.INLINE)
d.comment(0x83F4, "Jump to TX completion with slot index", align=Align.INLINE)
d.label(0x83F7, "discard_reset_rx")

d.subroutine(
    0x83F7,
    "discard_reset_rx",
    title="Discard scout, reset ADLC, install RX-scout NMI",
    description="""Three-stage idle-restore chain:

1. [`discard_reset_listen`](label:discard_reset_listen) – abandon any
   in-flight scout and release a held Tube claim.
2. [`reset_adlc_rx_listen`](label:reset_adlc_rx_listen) – call
   `adlc_rx_listen` (reset `CR1`/`CR2` and re-arm RX).
3. [`set_nmi_rx_scout`](label:set_nmi_rx_scout) – install
   [`nmi_rx_scout`](label:nmi_rx_scout) as the active NMI handler
   and `JMP` out via [`set_nmi_vector`](label:set_nmi_vector).

Used as the standard "something went wrong, get back to listening"
exit.""",
)


d.comment(0x83F7, "Discard scout and reset RX listen", align=Align.INLINE)
d.label(0x83FA, "reset_adlc_rx_listen")

d.subroutine(
    0x83FA,
    "reset_adlc_rx_listen",
    title="Reset ADLC and install RX-scout NMI",
    description="""Tail of the [`discard_reset_rx`](label:discard_reset_rx) chain entered
directly when no scout needs discarding. Calls `adlc_rx_listen`
to reset `CR1`/`CR2` to RX-only mode, then falls through to
[`set_nmi_rx_scout`](label:set_nmi_rx_scout).

Two inbound `JSR`s plus one fall-through (from
[`discard_reset_rx`](label:discard_reset_rx)).""",
)


d.comment(0x83FA, "Reset ADLC and return to RX listen", align=Align.INLINE)
d.label(0x83FD, "set_nmi_rx_scout")

d.subroutine(
    0x83FD,
    "set_nmi_rx_scout",
    title="Install nmi_rx_scout as NMI handler",
    description="""Loads `(A=&9B, Y=&80)` -- the address of
[`nmi_rx_scout`](label:nmi_rx_scout) -- and `JMP`s to
[`set_nmi_vector`](label:set_nmi_vector), which writes both bytes into
the NMI JMP-target slot at `nmi_jmp_lo`/`nmi_jmp_hi`. Tail of
the [`discard_reset_rx`](label:discard_reset_rx) /
[`reset_adlc_rx_listen`](label:reset_adlc_rx_listen) chain, used to put the
NMI vector back to scout-handling after a discard or reset.

Two callers: `&80CD` (after init) and `&80E4` (after error).""",
)


d.comment(0x83FD, "Next NMI handler address (low)", align=Align.INLINE)
d.expr_label(0x83FF, "imm_op_dispatch_lo-&81")

d.comment(0x83FF, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x8401, "Install nmi_rx_scout as NMI handler", align=Align.INLINE)
d.subroutine(
    0x8404,
    "discard_reset_listen",
    title="Discard with Tube release",
    description="""Checks whether a Tube transfer is active by ANDing bit 1 of
[`tube_present`](label:tube_present) with
[`net_frame_flags`](label:net_frame_flags) (`tx_flags`). If a Tube claim is
held, calls [`release_tube`](label:release_tube) to free it before
returning.

Used as the clean-up path after RXCB completion and after ADLC
reset to ensure no stale Tube claims persist.""",
)


d.comment(0x8404, "Tube flag bit 1 AND tx_flags bit 1", align=Align.INLINE)
d.comment(0x8406, "Check if Tube transfer active", align=Align.INLINE)
d.comment(0x8409, "Test tx_flags for Tube transfer", align=Align.INLINE)
d.comment(0x840C, "No Tube transfer active -- skip release", align=Align.INLINE)
d.comment(0x840E, "Release Tube claim before discarding", align=Align.INLINE)
d.label(0x8411, "rts_discard_reset")

d.comment(0x8411, "Return", align=Align.INLINE)
d.label(0x8412, "copy_scout_to_buffer")

d.subroutine(
    0x8412,
    "copy_scout_to_buffer",
    title="Copy scout data to port buffer (entry point)",
    description="""Five-instruction prologue that prepares to copy scout-payload
bytes (offsets `4..&0B`) from [`scout_buf`](label:scout_buf) into the
open port buffer. Saves `X` on the stack, loads `X=4` (the first
scout-data offset) and `A=&02` (Tube-flag mask), then `BIT`s
[`net_frame_flags`](label:net_frame_flags) (`tx_flags`) so the immediately
following `BNE` in
[`save_acccon_for_shadow_ram`](label:save_acccon_for_shadow_ram) can dispatch:

| Bit 1 | Path |
|---|---|
| clear | fall through into `save_acccon_for_shadow_ram` (direct memory store via `(open_port_buf),Y`, with ACCCON saved/restored on Master 128) |
| set   | branch to [`copy_scout_via_tube`](label:copy_scout_via_tube) (Tube R3 write) |

Both paths walk the four-byte buffer pointer and end via
[`scout_copy_done`](label:scout_copy_done) which restores `X` and returns.
Single caller: [`port_match_found`](label:port_match_found) at `&81A7`.""",
)


d.comment(0x8412, "Save X on stack", align=Align.INLINE)
d.comment(0x8413, "Push X", align=Align.INLINE)
d.comment(0x8414, "X=4: start at scout byte offset 4", align=Align.INLINE)
d.comment(0x8416, "A=2: Tube transfer check mask", align=Align.INLINE)
d.label(0x8418, "copy_scout_select")

d.comment(0x8418, "Check tx_flags Tube bit", align=Align.INLINE)
d.comment(0x841B, "Tube active: use R3 write path", align=Align.INLINE)
d.subroutine(
    0x841B,
    "save_acccon_for_shadow_ram",
    title="Save ACCCON across scout-buffer access",
    description="""Saves the current [`acccon`](label:acccon) value, sets ACCCON
for the upcoming `(open_port_buf),Y` stores (so writes go to the
right shadow / main RAM bank on the Master 128), performs the
copy, then restores the saved ACCCON before returning. Wraps the
inner copy loop with shadow-RAM gating so scout-buffer writes
land in the caller's address space rather than the FS-private
HAZEL window.""",
)

d.label(0x8494, "imm_op_handler_lo_table")

d.comment(
    0x841D,
    """Save/restore ACCCON across the (open_port_buf),Y stores.
The destination port buffer may live in shadow RAM; bit 0 of ACCCON (D)
controls whether (zp),Y addressing hits shadow vs main RAM. Workspace &97
holds the desired ACCCON value pre-loaded by the caller.""",
)
d.comment(0x841D, "Save current ACCCON on stack", align=Align.INLINE)
d.comment(0x8420, "Push ACCCON snapshot", align=Align.INLINE)
d.comment(0x8421, "Load desired ACCCON from workspace &97", align=Align.INLINE)
d.comment(0x8423, "Set ACCCON for the upcoming (open_port_buf),Y stores", align=Align.INLINE)
d.comment(0x8426, "Y = current buffer position", align=Align.INLINE)
d.label(0x8428, "copy_scout_bytes")

d.comment(0x8428, "Load scout data byte", align=Align.INLINE)
d.comment(0x842B, "Store to port buffer", align=Align.INLINE)
d.comment(0x842D, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x842E, "No page crossing", align=Align.INLINE)
d.comment(0x8430, "Page crossing: inc buffer high byte", align=Align.INLINE)
d.comment(0x8432, "Decrement remaining page count", align=Align.INLINE)
d.comment(0x8434, "No pages left: overflow", align=Align.INLINE)
d.label(0x8436, "next_scout_byte")

d.comment(0x8436, "Next scout data byte", align=Align.INLINE)
d.comment(0x8437, "Save updated buffer position", align=Align.INLINE)
d.comment(0x8439, "Done all scout data? (X reaches &0C)", align=Align.INLINE)
d.comment(0x843B, "No: continue copying", align=Align.INLINE)
d.label(0x843D, "scout_copy_done")

d.comment(0x843D, "Pull saved ACCCON from stack", align=Align.INLINE)
d.comment(0x843E, "Restore caller's ACCCON before continuing", align=Align.INLINE)
d.comment(0x8441, "Pull saved X from stack", align=Align.INLINE)
d.label(0x8441, "scout_done_restore_x")

d.comment(0x8443, "Tail-jump to rx_complete_update_rxcb", align=Align.INLINE)
d.comment(0x8446, "Reset ADLC if carry set", align=Align.INLINE)
d.label(0x8446, "dispatch_imm_op_fail")

d.label(0x8448, "copy_scout_via_tube")

d.comment(0x8448, "Tube path: load scout data byte", align=Align.INLINE)
d.comment(0x844B, "Send byte to Tube via R3", align=Align.INLINE)
d.comment(0x844E, "Increment buffer position counters", align=Align.INLINE)
d.comment(0x8451, "Counter overflow: handle end of buffer", align=Align.INLINE)
d.comment(0x8453, "Next scout data byte", align=Align.INLINE)
d.comment(0x8454, "Done all scout data?", align=Align.INLINE)
d.comment(0x8456, "No: continue Tube writes", align=Align.INLINE)
d.label(0x845A, "release_tube")

d.subroutine(
    0x845A,
    "release_tube",
    title="Release Tube co-processor claim",
    description="""Tests bit 7 of [`prot_flags`](label:prot_flags) -- the bit ANFS uses
to track whether the Tube is currently still claimed:

| Bit 7 | State | Action |
|---|---|---|
| set | already released | branch to `clear_release_flag` (skips the release call) |
| clear | claim held | `JSR tube_addr_data_dispatch` with `A=&82` to release the claim, then fall through |

Both paths end at `clear_release_flag` which `LSR`s `prot_flags`
(shifting bit 7 to 0) before returning.

Called after completed RX transfers and during discard paths to
ensure no stale Tube claims persist.

**Idempotent:** safe to call when the Tube has already been
released. Clobbers `A`; preserves `X` and `Y`.""",
    on_exit={"a": "clobbered"},
)


d.comment(0x845A, "Check if Tube needs releasing", align=Align.INLINE)
d.comment(0x845C, "Bit7 set: already released", align=Align.INLINE)
d.comment(0x845E, "A=&82: Tube release claim type", align=Align.INLINE)
d.comment(0x8460, "Release Tube address claim", align=Align.INLINE)
d.label(0x8463, "clear_release_flag")

d.comment(0x8463, "Clear release flag (LSR clears bit7)", align=Align.INLINE)
d.comment(0x8465, "Return", align=Align.INLINE)
d.subroutine(
    0x8466,
    "immediate_op",
    title="Immediate operation handler (port = 0)",
    description="""Checks the control byte at [`scout_ctrl`](label:scout_ctrl) for
immediate-operation codes:

| Range | Op | Treatment |
|---|---|---|
| `< &81` or `> &88` | – | out of range; discarded |
| `&81`..`&86` | PEEK / POKE / JSR / UserProc / OSProc / HALT | gated by the [`prot_status`](label:prot_status) protection mask |
| `&87`..`&88` | CONTINUE / machine-type | bypass the mask check |

For `&81`..`&86`, converts the code to a 0-based index and tests
against the per-station protection mask
[`prot_status`](label:prot_status) to determine whether this
station accepts the operation. If accepted, dispatches via
the immediate-op dispatch table (PHA/PHA/RTS).

The execute-class operations (`&83` JSR, `&84` UserProc, `&85`
OSProc, `&86` HALT, `&87` CONTINUE) cannot run inside the NMI
receive handler -- a JSR into user code or an OS call is unsafe
there -- so they are not run inline. They are completed later
from normal IRQ context: [`setup_sr_tx`](label:setup_sr_tx) records the
operation in [`tx_op_type`](label:tx_op_type) and sets the Master 128
ACCCON IRR latch (bit 7 at `&FE34`), which raises an IRQ that the
ROM picks up as service call `&05`
([`svc5_irq_check`](label:svc5_irq_check)) and dispatches via the
[`svc5_dispatch_lo`](label:svc5_dispatch_lo) table. PEEK, POKE and
machine-type (`&81` / `&82` / `&88`) only touch memory and reply
immediately, so they run here.

Builds the reply by storing data length, station / network, and
control byte into the RX buffer header.""",
)


d.comment(0x8466, "Control byte &81-&88 range check", align=Align.INLINE)
d.comment(0x8469, "Below &81: not an immediate op", align=Align.INLINE)
d.comment(0x846B, "Out of range low: jump to discard", align=Align.INLINE)
d.comment(0x846D, "Above &88: not an immediate op", align=Align.INLINE)
d.comment(0x846F, "Out of range high: jump to discard", align=Align.INLINE)
d.comment(0x8471, "CONTINUE(&87)/mc-type(&88) skip protection", align=Align.INLINE)
d.comment(0x8473, "Ctrl >= &87: dispatch without mask check", align=Align.INLINE)
d.comment(0x8475, "Convert ctrl byte to 0-based index for mask", align=Align.INLINE)
d.comment(0x8477, "For subtract", align=Align.INLINE)
d.comment(0x8478, "A = ctrl - &81 (0-based operation index)", align=Align.INLINE)
d.comment(0x847A, "Y = index for mask rotation count", align=Align.INLINE)
d.comment(0x847B, "Load protection mask from LSTAT", align=Align.INLINE)
d.label(0x847E, "rotate_prot_mask")

d.comment(0x847E, "Rotate mask right by control byte index", align=Align.INLINE)
d.comment(0x847F, "Decrement rotation counter", align=Align.INLINE)
d.comment(0x8480, "Loop until bit aligned", align=Align.INLINE)
d.comment(0x8482, "Bit set = operation disabled, discard", align=Align.INLINE)
d.label(0x8484, "dispatch_imm_op")

d.comment(0x8484, "Reload ctrl byte for dispatch table", align=Align.INLINE)
d.comment(0x8487, "Hi byte: all handlers are in page &84", align=Align.INLINE)
d.comment(0x8489, "Push hi byte for PHA/PHA/RTS dispatch", align=Align.INLINE)
d.comment(0x848A, "Load handler low byte from jump table", align=Align.INLINE)
d.comment(0x848D, "Push handler low byte", align=Align.INLINE)
d.comment(0x848E, "RTS dispatches to handler", align=Align.INLINE)
d.label(0x848F, "scout_page_overflow")

d.comment(0x848F, "Increment port buffer length", align=Align.INLINE)
d.comment(
    0x8491,
    """Tube-path overflow exit from copy_scout_to_buffer: restores the Master 128
ACCCON that was saved at &840B before re-joining the scout-done path.""",
)
d.comment(0x8491, "Pull saved ACCCON from stack", align=Align.INLINE)
d.label(0x8491, "tube_overflow_restore")

d.comment(0x8492, "Restore caller's ACCCON on Tube-overflow exit", align=Align.INLINE)
d.label(0x8495, "check_scout_done")

d.comment(0x8495, "Check if scout data index reached 11", align=Align.INLINE)
d.comment(0x8497, "Yes: loop back to continue reading", align=Align.INLINE)
d.comment(0x8499, "Restore A from stack", align=Align.INLINE)
d.comment(0x849A, "Transfer to X", align=Align.INLINE)
d.label(0x849B, "imm_op_out_of_range")

d.comment(0x849B, "Jump to discard handler", align=Align.INLINE)
d.subroutine(
    0x8515,
    "imm_op_dispatch_lo",
    title="Immediate-op dispatch lo-byte table (8 entries)",
    description="""Eight low-byte entries at `&8515`-`&851C` indexed by the
immediate-op control byte (`&81`-`&88`) via
`LDA imm_op_handler_lo_table,Y` at the dispatch site (the table's
nominal base [`imm_op_handler_lo_table`](label:imm_op_handler_lo_table)
so the entry for control byte N sits at that base plus N). Each byte
is the low byte of `(handler-1)` so the PHA/PHA/RTS dispatch (constant
high byte `&84`) lands on the handler in page `&84xx`. Per-entry
inline comments identify each control byte's handler.""",
    is_entry_point=False,
)
for _addr in range(0x8515, 0x851D):
    d.byte(_addr)
d.expr(0x8515, lo(sym("rx_imm_peek") - 1))
d.comment(0x8515, "ctrl &81: PEEK", align=Align.INLINE)
d.expr(0x8516, lo(sym("rx_imm_poke") - 1))
d.comment(0x8516, "ctrl &82: POKE", align=Align.INLINE)
d.expr(0x8517, lo(sym("rx_imm_exec") - 1))
d.comment(0x8517, "ctrl &83: JSR", align=Align.INLINE)
d.expr(0x8518, lo(sym("rx_imm_exec") - 1))
d.comment(0x8518, "ctrl &84: UserProc", align=Align.INLINE)
d.expr(0x8519, lo(sym("rx_imm_exec") - 1))
d.comment(0x8519, "ctrl &85: OSProc", align=Align.INLINE)
d.expr(0x851A, lo(sym("rx_imm_halt_cont") - 1))
d.comment(0x851A, "ctrl &86: HALT", align=Align.INLINE)
d.expr(0x851B, lo(sym("rx_imm_halt_cont") - 1))
d.comment(0x851B, "ctrl &87: CONTINUE", align=Align.INLINE)
d.expr(0x851C, lo(sym("rx_imm_machine_type") - 1))
d.comment(0x851C, "ctrl &88: machine-type", align=Align.INLINE)


d.subroutine(
    0x849E,
    "rx_imm_exec",
    title="RX immediate: JSR / UserProc / OSProc setup",
    description="""Sets up the port buffer to receive remote-procedure data. Copies
the 2-byte remote address from [`scout_data`](label:scout_data)
into the execution-address workspace at
[`exec_addr_lo`](label:exec_addr_lo) / [`exec_addr_hi`](label:exec_addr_hi),
then jumps to the common data-receive path via
[`send_data_rx_ack`](label:send_data_rx_ack).

Used for operation types `&83` (JSR), `&84` (UserProc), and
`&85` (OSProc).""",
)


d.comment(0x849E, "A=0: port buffer lo at page boundary", align=Align.INLINE)
d.comment(0x84A0, "Set port buffer lo", align=Align.INLINE)
d.comment(0x84A2, "Buffer length lo = &82", align=Align.INLINE)
d.comment(0x84A4, "Set buffer length lo", align=Align.INLINE)
d.comment(0x84A6, "Buffer length hi = 1", align=Align.INLINE)
d.comment(0x84A8, "Set buffer length hi", align=Align.INLINE)
d.comment(0x84AA, "Load RX page hi for buffer", align=Align.INLINE)
d.comment(0x84AC, "Set port buffer hi", align=Align.INLINE)
d.comment(0x84AE, "Y=1: copy 2 bytes (1 down to 0)", align=Align.INLINE)
d.label(0x84B0, "copy_addr_loop")

d.comment(0x84B0, "Load remote address byte", align=Align.INLINE)
d.comment(0x84B3, "Store to exec address workspace", align=Align.INLINE)
d.comment(0x84B6, "Next byte (descending)", align=Align.INLINE)
d.comment(0x84B7, "Loop until all 4 bytes copied", align=Align.INLINE)
d.label(0x84B9, "jmp_send_data_rx_ack")

d.comment(0x84B9, "Enter common data-receive path", align=Align.INLINE)
d.label(0x84BC, "svc5_dispatch_lo")

d.subroutine(
    0x84BC,
    "rx_imm_poke",
    title="RX immediate: POKE setup",
    description="""Sets up workspace offsets for receiving POKE data:
`port_ws_offset = &2E`, `rx_buf_offset = &0D`. Jumps to the
POKE data-receive path at [`port_match_found`](label:port_match_found).
POKE (`&82`) only writes
memory and replies, so it is serviced inline in the receive
path -- not deferred like the execute-class operations
`&83`-`&87`.""",
)


d.comment(0x84BC, "Port workspace offset = &2E", align=Align.INLINE)
d.comment(0x84BE, "Store as port_ws_offset", align=Align.INLINE)
d.comment(0x84C0, "RX buffer page = &0D", align=Align.INLINE)
d.comment(0x84C2, "Store as rx_buf_offset", align=Align.INLINE)
d.expr_label(0x84C3, "tx_done_dispatch_lo-&83")
d.comment(0x84C4, "Enter POKE data-receive path", align=Align.INLINE)
d.subroutine(
    0x84C7,
    "rx_imm_peek",
    title="RX immediate: PEEK setup",
    description="""Sets up workspace offsets for a PEEK response:
`port_ws_offset = &2E`, `rx_buf_offset = &0D`, `rx_port = 2`
(PEEK response status), then calls
[`tx_calc_transfer`](label:tx_calc_transfer) to send the requested
memory back to the requesting station. PEEK (`&81`) only reads
memory and replies, so it is serviced inline in the receive path --
not deferred like the execute-class operations `&83`-`&87`.

Reached via the immediate-op dispatch table
([`imm_op_handler_lo_table`](label:imm_op_handler_lo_table)) for
control byte `&81`.""",
)


d.comment(0x84C7, "Port workspace offset = &2E", align=Align.INLINE)
d.comment(0x84C9, "Store as port_ws_offset", align=Align.INLINE)
d.comment(0x84CB, "RX buffer page = &0D", align=Align.INLINE)
d.comment(0x84CD, "Store as rx_buf_offset", align=Align.INLINE)
d.comment(0x84CF, "Scout status = 2 (PEEK response)", align=Align.INLINE)
d.comment(0x84D1, "Store scout status", align=Align.INLINE)
d.comment(0x84D4, "Calculate transfer size for response", align=Align.INLINE)
d.comment(0x84D7, "C=0: transfer not set up, discard", align=Align.INLINE)
d.label(0x84D9, "set_tx_reply_flag")

d.comment(0x84D9, "Mark TX flags bit 7 (reply pending)", align=Align.INLINE)
d.comment(0x84DC, "Set reply pending flag", align=Align.INLINE)
d.comment(0x84DE, "Store updated TX flags", align=Align.INLINE)
d.label(0x84E1, "rx_imm_halt_cont")

d.comment(0x84E1, "CR1=&44: TIE | TX_LAST_DATA", align=Align.INLINE)
d.comment(0x84E3, "Write CR1: enable TX interrupts", align=Align.INLINE)
d.label(0x84E6, "tx_cr2_setup")

d.comment(0x84E6, "CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE", align=Align.INLINE)
d.comment(0x84E8, "Write CR2 for TX setup", align=Align.INLINE)
d.label(0x84EB, "tx_nmi_setup")

d.comment(0x84EB, "NMI handler lo byte (self-modifying)", align=Align.INLINE)
d.comment(0x84ED, "Y=&85: NMI handler high byte", align=Align.INLINE)
d.comment(0x84EF, "Acknowledge and write TX dest", align=Align.INLINE)
# UNMAPPED: d.label(0x84F9, "imm_op_build_reply")

# UNMAPPED: d.entry(0x84F9)
# UNMAPPED: d.subroutine(
# UNMAPPED:     0x84F9,
# UNMAPPED:     "imm_op_build_reply",
# UNMAPPED:     title="Build immediate-operation reply header",
# UNMAPPED:     description="""Writes the reply-frame header for a port-0 immediate operation
# UNMAPPED: into the RX buffer at offsets `&7F..&81`:
# UNMAPPED: 
# UNMAPPED: | RX offset | Source | Meaning |
# UNMAPPED: |---|---|---|
# UNMAPPED: | `&7F` | `port_buf_len + &80` | reply data length (raw count + header offset) |
# UNMAPPED: | `&80` | [`scout_buf`](label:scout_buf) | requesting station |
# UNMAPPED: | `&81` | [`scout_src_net`](label:scout_src_net) | requesting network |
# UNMAPPED: 
# UNMAPPED: Then loads the control byte from
# UNMAPPED: [`scout_ctrl`](label:scout_ctrl) into `A` and falls through into
# UNMAPPED: [`setup_sr_tx`](label:setup_sr_tx), which records `A` as
# UNMAPPED: [`tx_op_type`](label:tx_op_type) and (for execute-class ops) arms the
# UNMAPPED: deferred dispatch by setting the Master 128 ACCCON IRR latch so the
# UNMAPPED: operation completes from normal IRQ context. Reached via the
# UNMAPPED: immediate-op dispatch path.""",
# UNMAPPED: )
d.comment(0x851D, "Get buffer position for reply header", align=Align.INLINE)
# UNMAPPED: d.comment(0x84FB, "Clear carry for offset addition", align=Align.INLINE)
d.comment(0x8520, "Data offset = buf_len + &80 (past header)", align=Align.INLINE)
d.comment(0x8522, "Y=&7F: reply data length slot", align=Align.INLINE)
d.comment(0x8524, "Store reply data length in RX buffer", align=Align.INLINE)
d.comment(0x8526, "Y=&80: source station slot", align=Align.INLINE)
d.comment(0x8528, "Load requesting station number", align=Align.INLINE)
d.comment(0x852B, "Store source station in reply header", align=Align.INLINE)
d.comment(0x852E, "Load requesting network number", align=Align.INLINE)
d.comment(0x8531, "Store source network in reply header", align=Align.INLINE)
d.comment(0x8533, "Load control byte from received frame", align=Align.INLINE)
d.label(0x8536, "setup_sr_tx")

d.subroutine(
    0x8536,
    "setup_sr_tx",
    title="Save TX op type and raise JSR re-entrancy protection",
    description="""Stores the TX operation type in [`tx_op_type`](label:tx_op_type),
then (at [`enable_irq_pending`](label:enable_irq_pending)) sets the ACCCON IRR
latch to arm the deferred dispatch -- see [`svc5_irq_check`](label:svc5_irq_check).

| Op code | Path |
|---|---|
| `≥ &86` (HALT / CONTINUE / machine-type) | branch forward to the ACCCON IRR set; the protection mask is left untouched |
| `< &86` (JSR / UserProc / OSProc) | load the [`prot_status`](label:prot_status) protection mask, copy it to [`prot_status_save`](label:prot_status_save), `ORA` in bits 2-4 to *disable* further JSR / UserProc / OSProc, then write the raised mask back to `prot_status` |

Raising bits 2-4 of the LSTAT protection mask is re-entrancy
protection: while the deferred remote routine runs (it is a JSR into
user code, or an OS call), the station will not accept another remote
execute operation. The previous mask is preserved in
`prot_status_save` so it can be restored once the call returns. (The
bit pattern `&1C` happens to equal the System VIA ACR
shift-register mode-field mask, but here it is applied to the LSTAT
mask, not the VIA -- the Model B ROMs raise the same bits in a
separate step on the dispatch side.) Single caller (`&83E2` in
[`scout_complete`](label:scout_complete)).""",
    on_entry={"a": "TX operation type"},
)


d.comment(0x8536, "Save TX operation type for SR dispatch", align=Align.INLINE)
d.comment(0x8539, "Ops >= &86 run no code: skip JSR protection", align=Align.INLINE)
d.comment(0x853B, "Skip ahead to the ACCCON IRR set", align=Align.INLINE)
d.comment(0x853D, "Load LSTAT protection mask", align=Align.INLINE)
d.comment(0x8540, "Save old mask in prot_status_save for restore", align=Align.INLINE)
d.comment(0x8543, "Set bits 2-4: disable JSR/UserProc/OSProc", align=Align.INLINE)
d.comment(0x8545, "Write raised protection mask back", align=Align.INLINE)
d.comment(0x8548, "A=&80: ACCCON bit 7 (IRR -- raise interrupt)", align=Align.INLINE)
d.label(0x8548, "enable_irq_pending")

d.comment(0x854A, "Set ACCCON IRR to flag a pending interrupt to MOS", align=Align.INLINE)
d.label(0x854D, "imm_op_discard")

d.comment(0x854D, "Return to idle listen mode", align=Align.INLINE)
d.subroutine(
    0x8550,
    "advance_buffer_ptr",
    title="Increment 4-byte receive-buffer pointer",
    description="""Adds 1 to the 4-byte counter at `&A2..&A5` (`port_buf_len` lo/hi,
`open_port_buf` lo/hi), cascading overflow through all four
bytes. Called after each byte is stored during scout-data copy
and data-frame reception to track the current write position in
the receive buffer.

Preserves `A`, `X`, `Y` (uses `INC zp` throughout).""",
    on_exit={"a, x, y": "preserved (INC zp only)"},
)


d.comment(0x8550, "Increment buffer length low byte", align=Align.INLINE)
d.comment(0x8552, "No overflow: done", align=Align.INLINE)
d.comment(0x8554, "Increment buffer length high byte", align=Align.INLINE)
d.comment(0x8556, "No overflow: done", align=Align.INLINE)
d.comment(0x8558, "Increment buffer pointer low byte", align=Align.INLINE)
d.comment(0x855A, "No overflow: done", align=Align.INLINE)
d.comment(0x855C, "Increment buffer pointer high byte", align=Align.INLINE)
d.label(0x855E, "rts_advance_buf")

d.comment(0x855E, "Return", align=Align.INLINE)
# UNMAPPED: d.subroutine(
# UNMAPPED:     0x853B,
# UNMAPPED:     "tx_done_dispatch_lo",
# UNMAPPED:     title="TX done dispatch lo-byte table (5 entries)",
# UNMAPPED:     description="""Low bytes of PHA/PHA/RTS dispatch targets for TX operation types
# UNMAPPED: `&83`-`&87`. Read by the dispatch at
# UNMAPPED: [`dispatch_svc5`](label:dispatch_svc5) via
# UNMAPPED: `LDA tx_done_dispatch_lo-&83,Y` (the operand lands mid-instruction
# UNMAPPED: inside [`set_rx_buf_len_hi`](label:set_rx_buf_len_hi)). The dispatch
# UNMAPPED: trampoline pushes `&85` as the high byte, so targets are
# UNMAPPED: `&85xx+1`. Entries for `Y < &83` read from preceding code bytes
# UNMAPPED: and are not valid operation types. Per-entry inline comments
# UNMAPPED: identify each TX operation type's handler.""",
# UNMAPPED: )
# UNMAPPED: for i in range(5):
# UNMAPPED:     d.byte(0x853B + i)
# UNMAPPED: d.expr(0x853B, "<(tx_done_jsr-1)")
# UNMAPPED: d.comment(0x853B, "op &83: remote JSR", align=Align.INLINE)
# UNMAPPED: d.expr(0x853C, "<(tx_done_econet_event-1)")
# UNMAPPED: d.comment(0x853C, "op &84: fire Econet event", align=Align.INLINE)
# UNMAPPED: d.expr(0x853D, "<(tx_done_os_proc-1)")
# UNMAPPED: d.comment(0x853D, "op &85: OSProc call", align=Align.INLINE)
# UNMAPPED: d.expr(0x853E, "<(tx_done_halt-1)")
# UNMAPPED: d.comment(0x853E, "op &86: HALT", align=Align.INLINE)
# UNMAPPED: d.expr(0x853F, "<(tx_done_continue-1)")
# UNMAPPED: d.comment(0x853F, "op &87: CONTINUE", align=Align.INLINE)
d.entry(0x8564)


d.subroutine(
    0x8564,
    "tx_done_jsr",
    title="TX done: remote JSR execution",
    description="""Executes the Econet Remote Subroutine Jump (immediate operation
`&83`), now running in deferred IRQ context after
[`svc5_irq_check`](label:svc5_irq_check) picked up the ACCCON IRR latch --
so the JSR happens safely outside the NMI handler.

Pushes ([`tx_done_exit`](label:tx_done_exit) ` - 1`) on the stack so
`RTS` returns to [`tx_done_exit`](label:tx_done_exit) when the remote
routine completes, then does `JMP` indirect through
[`exec_addr_lo`](label:exec_addr_lo) to call the remote-supplied JSR
target. When that routine returns via `RTS`, control resumes at
[`tx_done_exit`](label:tx_done_exit) which tidies up TX state.""",
)


d.comment(0x8564, "tx_done_exit RTS target (high)", align=Align.INLINE)
d.comment(0x8566, "Push hi byte on stack", align=Align.INLINE)
d.comment(0x8567, "tx_done_exit RTS target (low)", align=Align.INLINE)
d.comment(0x8569, "Push lo byte on stack", align=Align.INLINE)
d.comment(0x856A, "Call remote JSR; RTS to tx_done_exit", align=Align.INLINE)


d.label(0x856D, "tx_done_econet_event")

d.subroutine(
    0x856D,
    "tx_done_econet_event",
    title="TX done: fire Econet event",
    description="""Handler for TX operation type `&84`. Loads the remote address
from [`exec_addr_lo`](label:exec_addr_lo) /
[`exec_addr_hi`](label:exec_addr_hi) into `X` / `A` and sets `Y=8`
(Econet event number), then falls through to `tx_done_fire_event`
to call OSEVEN.

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi. The dispatcher
pushed the caller's `X` and `Y` onto the stack before
transferring control, and the shared
[`tx_done_exit`](label:tx_done_exit) restores them via
`PLA`/`TAY`/`PLA`/`TAX` before returning `A=0`.""",
    on_exit={"a": "0 (success status)", "x, y": "restored from stack via tx_done_exit"},
)


d.comment(0x856D, "X = remote address lo from exec_addr_lo", align=Align.INLINE)
d.entry(0x856D)
d.comment(0x8570, "A = remote address hi from exec_addr_hi", align=Align.INLINE)
d.comment(0x8573, "Y = 8: Econet event number", align=Align.INLINE)
d.label(0x8575, "tx_done_fire_event")

d.comment(0x8578, "Exit TX done handler", align=Align.INLINE)
d.subroutine(
    0x857B,
    "tx_done_os_proc",
    title="TX done: OSProc call",
    description="""Calls the ROM service entry point with
`X = `[`exec_addr_lo`](label:exec_addr_lo)`, Y = `[`exec_addr_hi`](label:exec_addr_hi).
This invokes an OS-level procedure on behalf of the remote
station, then exits via [`tx_done_exit`](label:tx_done_exit).

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi.""",
    on_exit={"a": "0 (success status)", "x, y": "restored from stack via tx_done_exit"},
)


d.comment(0x857B, "X = remote address lo", align=Align.INLINE)
d.comment(0x857E, "Y = remote address hi", align=Align.INLINE)
d.comment(0x8581, "Call ROM entry point at &8000", align=Align.INLINE)
d.comment(0x8584, "Exit TX done handler", align=Align.INLINE)
d.subroutine(
    0x8587,
    "tx_done_halt",
    title="TX done: HALT",
    description="""Sets bit 2 of [`econet_flags`](label:econet_flags), enables
interrupts, and spin-waits until bit 2 is cleared (by a CONTINUE
from the remote station). If bit 2 is already set, skips to exit.

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi. Falls through to
[`tx_done_continue`](label:tx_done_continue) after the spin completes;
on the already-halted path it branches directly to
[`tx_done_exit`](label:tx_done_exit).""",
    on_exit={
        "a": "0 (success status, set by tx_done_exit)",
        "i flag": "interrupts enabled (CLI inside the spin)",
        "x, y": "restored from stack via tx_done_exit",
    },
)


d.comment(0x8587, "A=&04: bit 2 mask (halt flag in econet_flags)", align=Align.INLINE)
d.comment(0x8589, "Test if already halted", align=Align.INLINE)
d.comment(0x858C, "Already halted: skip to exit", align=Align.INLINE)
d.comment(0x858E, "Set bit 2 in econet_flags (halt)", align=Align.INLINE)
d.comment(0x8591, "Store halt flag", align=Align.INLINE)
d.comment(0x8594, "A=4: re-load halt bit mask", align=Align.INLINE)
d.comment(0x8596, "Enable interrupts during halt wait", align=Align.INLINE)
d.label(0x8597, "halt_spin_loop")

d.comment(0x8597, "Test halt flag", align=Align.INLINE)
d.comment(0x859A, "Still halted: keep spinning", align=Align.INLINE)
d.subroutine(
    0x859E,
    "tx_done_continue",
    title="TX done: CONTINUE",
    description="""Clears bit 2 of [`econet_flags`](label:econet_flags), releasing any
station that is halted and spinning in
[`tx_done_halt`](label:tx_done_halt).

Reached either as a fall-through from
[`tx_done_halt`](label:tx_done_halt) or directly via
`PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi. Falls through to
[`tx_done_exit`](label:tx_done_exit) which restores `X` and `Y`
from the stack and returns `A=0`.""",
    on_exit={"a": "0 (success status)", "x, y": "restored from stack via tx_done_exit"},
)


d.comment(0x859E, "Load current econet_flags", align=Align.INLINE)
d.comment(0x85A1, "Clear bit 2: release halted station", align=Align.INLINE)
d.comment(0x85A3, "Store updated flags", align=Align.INLINE)
d.label(0x85A6, "tx_done_exit")

d.subroutine(
    0x85A6,
    "tx_done_exit",
    title="Shared TX-done exit: restore X/Y, return A=0",
    description="""Common cleanup tail used by every entry in the
[`tx_done_dispatch_lo`](address:853B) table. Pulls the saved
`Y` and `X` off the stack (the dispatcher pushed them before the
`PHA`/`PHA`/`RTS` jump), loads `A=0` (success status), and `RTS`
to the caller.

Five inbound refs: a tail-jump from `&8044` (the SVC 5 IRQ-check
path in [`svc5_irq_check`](label:svc5_irq_check)), plus the JMPs at
`&8554`, `&8584`, `&858C`, and the fall-through at `&8578`.""",
    on_exit={"a": "0 (success status)", "x, y": "restored from stack"},
)


d.comment(0x85A6, "Restore Y from stack", align=Align.INLINE)
d.comment(0x85A7, "Transfer to Y register", align=Align.INLINE)
d.comment(0x85A8, "Restore X from stack", align=Align.INLINE)
d.comment(0x85A9, "Transfer to X register", align=Align.INLINE)
d.comment(0x85AA, "A=0: success status", align=Align.INLINE)
d.comment(0x85AC, "Store success status (A=0) to svc_state", align=Align.INLINE)
d.comment(0x85AE, "Return with A=0 (success)", align=Align.INLINE)
# UNMAPPED: d.label(0x8589, "tx_begin")

# UNMAPPED: d.subroutine(
# UNMAPPED:     0x8589,
# UNMAPPED:     "tx_begin",
# UNMAPPED:     title="Begin TX operation",
# UNMAPPED:     description="""Main TX initiation entry point (called via the NETV trampoline).
# UNMAPPED: 
# UNMAPPED: 1. Copies destination station / network from the TXCB to the
# UNMAPPED:    scout buffer.
# UNMAPPED: 2. Dispatches: control byte `≥ &81` → immediate-op setup; else
# UNMAPPED:    normal data transfer.
# UNMAPPED: 3. Calculates transfer sizes via
# UNMAPPED:    [`tx_calc_transfer`](label:tx_calc_transfer); copies extra
# UNMAPPED:    parameters into the workspace.
# UNMAPPED: 4. Checks DCD (SR2 bit 5): no clock on the line aborts with
# UNMAPPED:    'No Clock'.
# UNMAPPED: 5. Enters the INACTIVE polling loop at
# UNMAPPED:    [`inactive_poll`](label:inactive_poll).""",
# UNMAPPED: )


# UNMAPPED: d.comment(0x8589, "Save X on stack", align=Align.INLINE)
d.comment(0x864D, "Push X", align=Align.INLINE)
d.comment(0x864E, "Y=2: TXCB offset for dest station", align=Align.INLINE)
d.comment(0x8650, "Load dest station from TX control block", align=Align.INLINE)
d.comment(0x8652, "Store to TX scout buffer", align=Align.INLINE)
d.comment(0x8656, "Load dest network from TX control block", align=Align.INLINE)
d.comment(0x8658, "Store to TX scout buffer", align=Align.INLINE)
d.comment(0x865B, "Y=0: first byte of TX control block", align=Align.INLINE)
d.comment(0x865D, "Load control/flag byte", align=Align.INLINE)
d.comment(0x865F, "Bit7 set: immediate operation ctrl byte", align=Align.INLINE)
d.comment(0x8661, "Bit7 clear: normal data transfer", align=Align.INLINE)
d.label(0x8664, "tx_imm_op_setup")

d.comment(0x8664, "Store control byte to TX scout buffer", align=Align.INLINE)
d.comment(0x8667, "X = control byte for range checks", align=Align.INLINE)
d.comment(0x8668, "Y=1: port byte offset", align=Align.INLINE)
d.comment(0x8669, "Load port byte from TX control block", align=Align.INLINE)
d.comment(0x866B, "Store port byte to TX scout buffer", align=Align.INLINE)
d.comment(0x866E, "Port != 0: skip immediate op setup", align=Align.INLINE)
d.comment(0x8670, "Ctrl < &83: PEEK/POKE need address calc", align=Align.INLINE)
d.comment(0x8672, "Ctrl >= &83: skip to range check", align=Align.INLINE)
d.comment(0x8674, "Init borrow for 4-byte subtract", align=Align.INLINE)
d.comment(0x8675, "Save carry on stack for loop", align=Align.INLINE)
d.comment(0x8676, "Y=8: high pointer offset in TXCB", align=Align.INLINE)
d.label(0x8678, "calc_peek_poke_size")

d.comment(0x8678, "Load TXCB[Y] (end addr byte)", align=Align.INLINE)
d.comment(0x867A, "Y -= 4: back to start addr offset", align=Align.INLINE)
d.comment(0x867B, "(continued)", align=Align.INLINE)
d.comment(0x867C, "(continued)", align=Align.INLINE)
d.comment(0x867D, "(continued)", align=Align.INLINE)
d.comment(0x867E, "Restore borrow from stack", align=Align.INLINE)
d.comment(0x867F, "end - start = transfer size byte", align=Align.INLINE)
d.comment(0x8681, "Store result to tx_data_start", align=Align.INLINE)
d.comment(0x8684, "Y += 5: advance to next end byte", align=Align.INLINE)
d.comment(0x8685, "(continued)", align=Align.INLINE)
d.comment(0x8686, "(continued)", align=Align.INLINE)
d.comment(0x8687, "(continued)", align=Align.INLINE)
d.comment(0x8688, "(continued)", align=Align.INLINE)
d.comment(0x8689, "Save borrow for next byte", align=Align.INLINE)
d.comment(0x868A, "Done all 4 bytes? (Y reaches &0C)", align=Align.INLINE)
d.comment(0x868C, "No: next byte pair", align=Align.INLINE)
d.comment(0x868E, "Discard final borrow", align=Align.INLINE)
d.label(0x868F, "tx_ctrl_range_check")

d.comment(0x868F, "Ctrl < &81: not an immediate op", align=Align.INLINE)
d.comment(0x8691, "Below range: normal data transfer", align=Align.INLINE)
d.label(0x8693, "check_imm_range")

d.comment(0x8693, "Ctrl >= &89: out of immediate range", align=Align.INLINE)
d.comment(0x8695, "Above range: normal data transfer", align=Align.INLINE)
d.comment(0x8697, "Y=&0C: start of extra data in TXCB", align=Align.INLINE)
d.label(0x8699, "copy_imm_params")

d.comment(0x8699, "Load extra parameter byte from TXCB", align=Align.INLINE)
d.comment(0x869B, "Copy to NMI shim workspace at &0D1A+Y", align=Align.INLINE)
d.comment(0x869E, "Next byte", align=Align.INLINE)
d.comment(0x869F, "Done 4 bytes? (Y reaches &10)", align=Align.INLINE)
d.comment(0x86A1, "No: continue copying", align=Align.INLINE)
d.label(0x86A3, "tx_dcd_clock_check")

d.comment(0x86A3, "A=&20: mask for SR2 DCD (clock/carrier detect)", align=Align.INLINE)
d.comment(0x86A5, "Test SR2 DCD -- is there a clock?", align=Align.INLINE)
d.comment(0x86A8, "DCD set: no clock on the line, abandon TX", align=Align.INLINE)
d.comment(0x86AA, "A=&FD: high byte of timeout counter", align=Align.INLINE)
d.comment(0x86AC, "Push timeout high byte to stack", align=Align.INLINE)
d.comment(0x86AD, "Scout frame = 6 address+ctrl bytes", align=Align.INLINE)
d.comment(0x86AF, "Store scout frame length", align=Align.INLINE)
d.comment(0x86B2, "A=0: init low byte of timeout counter", align=Align.INLINE)
d.entry(0x86B4)
d.subroutine(
    0x86B4,
    "inactive_poll",
    title="INACTIVE polling loop",
    description="""Entry point for the Econet line-idle detection loop.

1. Saves the TX index in [`rx_remote_addr`](label:rx_remote_addr).
2. Pushes two timeout-counter bytes onto the stack.
3. Loads `Y = &E7` (CR2 value for TX preparation).
4. Loads the INACTIVE bit mask (`&04`) into `A`.
5. Falls through to [`intoff_test_inactive`](address:85FC)
   to begin polling `SR2` with interrupts disabled.""",
    on_exit={"y": "&E7 (CR2 value for tx_prepare)"},
)


d.comment(0x86B4, "Save TX index", align=Align.INLINE)
d.comment(0x86B7, "Push timeout byte 1 on stack", align=Align.INLINE)
d.comment(0x86B8, "Push timeout byte 2 on stack", align=Align.INLINE)
d.comment(0x86B9, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", align=Align.INLINE)
# UNMAPPED: d.label(0x85F8, "reload_inactive_mask")

d.comment(0x86C5, "A=&04: INACTIVE bit mask for SR2 test", align=Align.INLINE)
# UNMAPPED: d.label(0x85FA, "test_inactive_retry")

# UNMAPPED: d.comment(0x85FA, "Save interrupt state", align=Align.INLINE)
# UNMAPPED: d.comment(0x85FB, "Disable interrupts for ADLC access", align=Align.INLINE)
# UNMAPPED: d.label(0x85FC, "intoff_test_inactive")

# UNMAPPED: d.subroutine(
# UNMAPPED:     0x85FC,
# UNMAPPED:     "intoff_test_inactive",
# UNMAPPED:     title="Disable NMIs and test INACTIVE",
# UNMAPPED:     description="""Disables NMIs via two `BIT` reads of
# UNMAPPED: [`disable_net_nmis`](label:disable_net_nmis) (the Master 128 INTOFF register),
# UNMAPPED: then polls `SR2` for the INACTIVE bit (bit 2):
# UNMAPPED: 
# UNMAPPED: | `SR2` INACTIVE | Action |
# UNMAPPED: |---|---|
# UNMAPPED: | set   | read `SR1`, write `CR2=&67` to clear status, then test `CTS` (`SR1` bit 4); if `CTS` present, branch to [`tx_prepare`](label:tx_prepare) |
# UNMAPPED: | clear | re-enable NMIs via [`enable_net_nmis`](label:enable_net_nmis) (INTON) and decrement the 3-byte timeout counter on the stack |
# UNMAPPED: 
# UNMAPPED: On timeout, falls through to
# UNMAPPED: [`tx_line_jammed`](label:tx_line_jammed).""",
# UNMAPPED:     on_entry={"a": "&04 (INACTIVE bit mask)", "y": "&E7 (CR2 value for tx_prepare)"},
# UNMAPPED: )


d.comment(0x86C2, "INTOFF -- disable NMIs", align=Align.INLINE)
# UNMAPPED: d.expr_label(0x85FD, "tx_ctrl_dispatch_lo-&81")

# UNMAPPED: d.comment(0x85FF, "INTOFF again (belt-and-braces)", align=Align.INLINE)
# UNMAPPED: d.label(0x8602, "test_line_idle")

d.comment(0x86C7, "Z = &04 AND SR2 -- tests INACTIVE", align=Align.INLINE)
# UNMAPPED: d.comment(0x8605, "INACTIVE not set -- re-enable NMIs and loop", align=Align.INLINE)
d.comment(0x86CC, "Read SR1 -- arms the CLR_RX_ST below", align=Align.INLINE)
d.comment(0x86D1, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", align=Align.INLINE)
d.comment(0x86D3, "Write CR2: clear status, prepare TX", align=Align.INLINE)
d.comment(0x86D6, "A=&10: CTS mask for SR1 bit4", align=Align.INLINE)
d.comment(0x86D8, "Test SR1 CTS present", align=Align.INLINE)
d.comment(0x86DB, "CTS set -- clock hardware detected, start TX", align=Align.INLINE)
d.label(0x86E2, "inactive_retry")

d.comment(0x86E2, "INTON -- re-enable NMIs (Master &FE3C)", align=Align.INLINE)
d.comment(0x86E5, "Restore interrupt state", align=Align.INLINE)
d.comment(0x86E6, "3-byte timeout counter on stack", align=Align.INLINE)
d.comment(0x86E7, "Increment timeout counter byte 1", align=Align.INLINE)
d.comment(0x86EA, "Not overflowed: retry INACTIVE test", align=Align.INLINE)
d.comment(0x86EC, "Increment timeout counter byte 2", align=Align.INLINE)
d.comment(0x86EF, "Not overflowed: retry INACTIVE test", align=Align.INLINE)
d.comment(0x86F1, "Increment timeout counter byte 3", align=Align.INLINE)
d.comment(0x86F4, "Not overflowed: retry INACTIVE test", align=Align.INLINE)
d.label(0x86F8, "tx_bad_ctrl_error")

d.subroutine(
    0x86F8,
    "tx_bad_ctrl_error",
    title="Raise TX 'Bad control byte' (&44) error",
    description="""Loads error code `&44` ("Bad control") and ALWAYS-branches to
`store_tx_error`, which records it in the TX control block and
finishes the TX attempt.

Reached from three early-validation sites in
[`tx_begin`](address:8589) (`&859E`, `&85CE`, `&85D2`) when the
operation type is out of range.""",
    on_exit={"a": "&44 (TX 'Bad control' error code)"},
)


d.comment(0x86F8, "Error &44: control byte out of valid range", align=Align.INLINE)
d.subroutine(
    0x86FC,
    "tx_line_jammed",
    title="TX timeout error handler (Line Jammed)",
    description="""Reached when the [`inactive_poll`](label:inactive_poll) /
[`intoff_test_inactive`](address:85FC) loop times out without
detecting a quiet line.

1. Writes `CR2=&07` (`FC_TDRA | 2_1_BYTE | PSE`) to abort the TX
   attempt.
2. Pulls the 3-byte timeout state from the stack.
3. Stores error code `&40` ("Line Jammed") in the TX control
   block via `store_tx_error`.""",
)


d.comment(0x86FC, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", align=Align.INLINE)
d.comment(0x86FE, "Write CR2 to abort TX", align=Align.INLINE)
d.comment(0x8701, "Clean 3 bytes of timeout loop state", align=Align.INLINE)
d.comment(0x8702, "Pop saved register", align=Align.INLINE)
d.comment(0x8703, "Pop saved register", align=Align.INLINE)
d.comment(0x8704, "Error &40 = 'Line Jammed'", align=Align.INLINE)
d.comment(0x8706, "ALWAYS branch to shared error handler", align=Align.INLINE)
d.label(0x8708, "tx_no_clock_error")

d.comment(0x8708, "Error &43 = 'No Clock'", align=Align.INLINE)
d.label(0x870A, "store_tx_error")

d.comment(0x870A, "Offset 0 = error byte in TX control block", align=Align.INLINE)
d.comment(0x870C, "Store error code in TX CB byte 0", align=Align.INLINE)
d.comment(0x870E, "&80 = TX complete flag", align=Align.INLINE)
d.comment(0x8710, "Signal TX operation complete", align=Align.INLINE)
d.comment(0x8713, "Restore X saved by caller", align=Align.INLINE)
d.comment(0x8714, "Move to X register", align=Align.INLINE)
d.comment(0x8715, "Return to TX caller", align=Align.INLINE)
d.subroutine(
    0x8716,
    "tx_prepare",
    title="TX preparation",
    description="""Configures the ADLC for frame transmission and dispatches to the
control-byte handler.

1. Writes `CR2 = Y` (`&E7`) and `CR1 = &44` to enable TX with
   interrupts (`RX_RESET` + transmit-IRQ enable).
2. Installs [`nmi_tx_data`](label:nmi_tx_data) as the next NMI handler
   by writing `&E7,&86` directly into `nmi_jmp_lo` / `nmi_jmp_hi`.
3. Sets bit 7 of [`prot_flags`](label:prot_flags) (Tube-claimed
   marker, paired with [`release_tube`](label:release_tube)) via
   `SEC` / `ROR prot_flags`.
4. `BIT enable_net_nmis` re-enables NMIs so `TDRA` can fire.

Then dispatches on [`tx_port`](label:tx_port):

| `tx_port` | Path |
|---|---|
| non-zero | branch to `setup_data_xfer` (standard data transfer) |
| zero (immediate op) | look up `tx_flags` / `tx_length` from `tx_flags_table` / `tx_length_table` indexed by [`tx_ctrl_byte`](label:tx_ctrl_byte), push `&86` (high byte) and `tx_ctrl_dispatch_lo[Y-&81]` (low byte) and `RTS` to the control-byte handler |

The 4-byte destination-address write to the TX FIFO happens in
the dispatched-to handler (e.g. `setup_data_xfer`,
[`tx_ctrl_machine_type`](address:8686), etc.), not here.""",
    on_entry={"y": "&E7 (CR2 prep value)"},
)


d.comment(0x8716, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", align=Align.INLINE)
d.comment(0x8719, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", align=Align.INLINE)
d.comment(0x871B, "Write to ADLC CR1", align=Align.INLINE)
d.comment(0x871E, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8720, "High byte of NMI handler address", align=Align.INLINE)
d.comment(0x8722, "Write NMI vector low byte directly", align=Align.INLINE)
d.comment(0x8725, "Write NMI vector high byte directly", align=Align.INLINE)
d.comment(0x8728, "SEC: prepare carry for ROR into bit 7", align=Align.INLINE)
d.comment(0x8729, "Rotate carry into bit 7 of prot_flags (Tube-claimed)", align=Align.INLINE)
d.comment(0x8730, "INTON -- NMIs now fire for TDRA (Master &FE3C)", align=Align.INLINE)
d.comment(0x8733, "Load destination port number", align=Align.INLINE)
d.comment(0x8736, "Port != 0: standard data transfer", align=Align.INLINE)
d.comment(0x8738, "Port 0: load control byte for table lookup", align=Align.INLINE)
d.comment(0x873B, "Look up tx_flags from table", align=Align.INLINE)
d.comment(0x873E, "Store operation flags", align=Align.INLINE)
d.comment(0x8741, "Look up tx_length from table", align=Align.INLINE)
d.comment(0x8744, "Store expected transfer length", align=Align.INLINE)
d.comment(0x8747, "A=&87: high byte of tx_ctrl_* dispatch target", align=Align.INLINE)
d.comment(0x8749, "Push high byte for PHA/PHA/RTS dispatch", align=Align.INLINE)
d.comment(0x874A, "Look up handler address low from table", align=Align.INLINE)
d.comment(0x874D, "Push low byte for PHA/PHA/RTS dispatch", align=Align.INLINE)
d.comment(0x874E, "RTS dispatches to control-byte handler", align=Align.INLINE)


# UNMAPPED: d.subroutine(
# UNMAPPED:     0x867E,
# UNMAPPED:     "tx_ctrl_dispatch_lo",
# UNMAPPED:     title="TX ctrl dispatch lo-byte table (8 entries)",
# UNMAPPED:     description="""Low bytes of PHA/PHA/RTS dispatch targets for TX control byte
# UNMAPPED: types `&81`-`&88`. Read by the dispatch at `&8679` via
# UNMAPPED: `LDA tx_ctrl_dispatch_lo-&81,Y` (the operand lands mid-
# UNMAPPED: instruction inside
# UNMAPPED: [`intoff_test_inactive`](address:85FC)). High byte pushed by
# UNMAPPED: the dispatcher is always `&86`, so targets are `&86xx+1`. Last
# UNMAPPED: entry (`&88`) dispatches to
# UNMAPPED: [`tx_ctrl_machine_type`](address:8686), the 4 bytes immediately
# UNMAPPED: after the table.""",
# UNMAPPED: )
# UNMAPPED: for i in range(8):
# UNMAPPED:     d.byte(0x867E + i)
# UNMAPPED: d.expr(0x867E, "<(tx_ctrl_peek-1)")
# UNMAPPED: d.comment(0x867E, "ctrl &81: PEEK", align=Align.INLINE)
# UNMAPPED: d.expr(0x867F, "<(tx_ctrl_poke-1)")
# UNMAPPED: d.comment(0x867F, "ctrl &82: POKE", align=Align.INLINE)
# UNMAPPED: d.expr(0x8680, "<(proc_op_status2-1)")
# UNMAPPED: d.comment(0x8680, "ctrl &83: JSR", align=Align.INLINE)
# UNMAPPED: d.expr(0x8681, "<(proc_op_status2-1)")
# UNMAPPED: d.comment(0x8681, "ctrl &84: UserProc", align=Align.INLINE)
# UNMAPPED: d.expr(0x8682, "<(proc_op_status2-1)")
# UNMAPPED: d.comment(0x8682, "ctrl &85: OSProc", align=Align.INLINE)
# UNMAPPED: d.expr(0x8683, "<(tx_ctrl_exit-1)")
# UNMAPPED: d.comment(0x8683, "ctrl &86: HALT", align=Align.INLINE)
# UNMAPPED: d.expr(0x8684, "<(tx_ctrl_exit-1)")
# UNMAPPED: d.comment(0x8684, "ctrl &87: CONTINUE", align=Align.INLINE)
# UNMAPPED: d.expr(0x8685, "<(tx_ctrl_machine_type-1)")
# UNMAPPED: d.comment(0x8685, "ctrl &88: machine type", align=Align.INLINE)
# UNMAPPED: d.label(0x8686, "tx_ctrl_machine_type")

# UNMAPPED: d.subroutine(
# UNMAPPED:     0x8686,
# UNMAPPED:     "tx_ctrl_machine_type",
# UNMAPPED:     title="TX ctrl: machine-type query setup",
# UNMAPPED:     description="""Handler for control byte `&88`. Sets `scout_status = 3` and
# UNMAPPED: branches to `store_status_copy_ptr`, skipping the 4-byte address
# UNMAPPED: addition (no address parameters needed for a machine-type query).
# UNMAPPED: 
# UNMAPPED: Reached only via `PHA`/`PHA`/`RTS` dispatch from
# UNMAPPED: [`tx_ctrl_dispatch_lo`](address:867E) entry `&88`.""",
# UNMAPPED:     on_exit={"a": "3 (scout_status for machine type query)"},
# UNMAPPED: )


# UNMAPPED: d.comment(0x8686, "A=3: scout_status for machine type query", align=Align.INLINE)
# UNMAPPED: d.entry(0x8686)
d.comment(0x8751, "Skip address addition, store status", align=Align.INLINE)
d.subroutine(
    0x8753,
    "tx_ctrl_peek",
    title="TX ctrl: PEEK transfer setup",
    description="""Sets `A=3` (scout_status for PEEK) and branches to
[`tx_ctrl_store_and_add`](label:tx_ctrl_store_and_add) to store the status
and perform the 4-byte transfer-address addition.""",
    on_exit={"a": "3 (scout_status for PEEK)"},
)


d.comment(0x8753, "A=3: scout_status for PEEK op", align=Align.INLINE)
d.subroutine(
    0x8757,
    "tx_ctrl_poke",
    title="TX ctrl: POKE transfer setup",
    description="""Sets `A=2` (scout_status for POKE) and falls through to
[`tx_ctrl_store_and_add`](label:tx_ctrl_store_and_add) to store the status
and perform the 4-byte transfer-address addition.""",
    on_exit={"a": "2 (scout_status for POKE)"},
)


d.comment(0x8757, "Scout status = 2 (POKE transfer)", align=Align.INLINE)
d.subroutine(
    0x8759,
    "tx_ctrl_store_and_add",
    title="TX ctrl: store status and add transfer address",
    description="""Shared path for PEEK (`A=3`) and POKE (`A=2`):

1. Stores `A` as the scout status byte at
   [`rx_port`](label:rx_port).
2. Performs a 4-byte addition with carry propagation. For
   `Y=&0C..&0F` it adds `(nmi_tx_block),Y` (i.e. TXCB bytes
   12..15 from the block pointed to by
   [`nmi_tx_block`](label:nmi_tx_block)) into `tx_addr_base,Y` --
   `tx_addr_base+&0C..&0F` is the 4-byte transfer-length
   workspace at [`tx_data_len`](label:tx_data_len) (4 bytes).
3. Falls through to [`tx_ctrl_proc`](label:tx_ctrl_proc) which
   checks the loop boundary, then continues to
   [`tx_calc_transfer`](label:tx_calc_transfer) and `tx_ctrl_exit`.""",
    on_entry={"a": "scout status (3=PEEK, 2=POKE)"},
)


d.comment(0x8759, "Store scout status", align=Align.INLINE)
d.comment(0x875C, "Clear carry for 4-byte addition", align=Align.INLINE)
d.comment(0x875D, "Save carry on stack", align=Align.INLINE)
d.comment(0x875E, "Y=&0C: start at offset 12", align=Align.INLINE)
d.label(0x8760, "add_bytes_loop")

d.comment(0x8760, "Load workspace address byte", align=Align.INLINE)
d.comment(0x8763, "Restore carry from previous byte", align=Align.INLINE)
d.comment(0x8764, "Add TXCB address byte", align=Align.INLINE)
d.comment(0x8766, "Store updated address byte", align=Align.INLINE)
d.comment(0x8769, "Next byte", align=Align.INLINE)
d.comment(0x876A, "Save carry for next addition", align=Align.INLINE)
d.subroutine(
    0x876B,
    "tx_ctrl_proc",
    title="TX ctrl: tail of address-add loop + setup_data_xfer entry",
    description="""Tail of the 4-byte transfer-address addition loop that started in
[`tx_ctrl_store_and_add`](label:tx_ctrl_store_and_add): `CPY #&10` ends the
loop when Y reaches `&10`, `PLP` restores the saved carry, and
`BNE` skips the buffer-setup code if the transfer size is zero.

Falls through (or is reached via the dispatch from
[`tx_prepare`](label:tx_prepare) when port != 0) to
`setup_data_xfer` at `&8770`, which dispatches between broadcast
and unicast based on whether `tx_dst_stn` and `tx_dst_net` are
both `&FF`.""",
)


d.comment(0x876B, "Compare Y with 16-byte boundary", align=Align.INLINE)
d.comment(0x876D, "Below boundary: continue addition", align=Align.INLINE)
d.comment(0x876F, "Restore processor flags", align=Align.INLINE)
d.comment(0x8770, "Skip buffer setup if transfer size is zero", align=Align.INLINE)
d.label(0x8772, "setup_data_xfer")

d.comment(0x8772, "Load dest station for broadcast check", align=Align.INLINE)
d.comment(0x8775, "AND with dest network", align=Align.INLINE)
d.comment(0x8778, "Both &FF = broadcast address?", align=Align.INLINE)
d.comment(0x877A, "Not broadcast: unicast path", align=Align.INLINE)
d.comment(0x877C, "Broadcast scout: 14 bytes total", align=Align.INLINE)
d.comment(0x877E, "Store broadcast scout length", align=Align.INLINE)
d.comment(0x8781, "A=&40: broadcast flag", align=Align.INLINE)
d.comment(0x8783, "Set broadcast flag in tx_flags", align=Align.INLINE)
d.comment(0x8786, "Y=4: start of address data in TXCB", align=Align.INLINE)
d.label(0x8788, "copy_bcast_addr")

d.comment(0x8788, "Copy TXCB address bytes to scout buffer", align=Align.INLINE)
d.comment(0x878A, "Store to TX source/data area", align=Align.INLINE)
d.comment(0x878D, "Next byte", align=Align.INLINE)
d.comment(0x878E, "Done 8 bytes? (Y reaches &0C)", align=Align.INLINE)
d.comment(0x8790, "No: continue copying", align=Align.INLINE)
d.label(0x8794, "setup_unicast_xfer")

d.comment(0x8794, "A=0: clear flags for unicast", align=Align.INLINE)
d.comment(0x8796, "Clear tx_flags", align=Align.INLINE)
d.label(0x8799, "proc_op_status2")

d.comment(0x8799, "scout_status=2: data transfer pending", align=Align.INLINE)
d.label(0x879B, "store_status_copy_ptr")

d.comment(0x879B, "Store scout status", align=Align.INLINE)
d.label(0x879E, "skip_buf_setup")

d.comment(0x879E, "Copy TX block pointer to workspace ptr", align=Align.INLINE)
d.comment(0x87A0, "Store low byte", align=Align.INLINE)
d.comment(0x87A2, "Copy TX block pointer high byte", align=Align.INLINE)
d.comment(0x87A4, "Store high byte", align=Align.INLINE)
d.comment(0x87A6, "Calculate transfer size from RXCB", align=Align.INLINE)
d.label(0x87A9, "tx_ctrl_exit")

d.comment(0x87A9, "Restore processor status from stack", align=Align.INLINE)
d.comment(0x87AA, "Restore stacked registers (4 PLAs)", align=Align.INLINE)
d.comment(0x87AE, "Restore X from A", align=Align.INLINE)
d.comment(0x87AF, "Return to caller", align=Align.INLINE)
d.entry(0x87B8)
d.subroutine(
    0x87B8,
    "nmi_tx_data",
    title="NMI TX data handler",
    description="""Writes 2 bytes per NMI invocation to the TX FIFO at
[`econet_data_continue_frame`](label:econet_data_continue_frame). Uses `BIT`
[`econet_control1_or_status1`](label:econet_control1_or_status1)
on `SR1` to test `TDRA` (`V` flag = bit 6) and `IRQ` (`N` flag =
bit 7).

After writing 2 bytes, checks if the frame is complete:

| `SR1` bit 7 (`IRQ`) | Action |
|---|---|
| set   | tight loop: write 2 more bytes without returning from NMI |
| clear | return via `RTI` and wait for the next NMI |""",
)


d.comment(0x87B8, "Load TX buffer index", align=Align.INLINE)
d.comment(0x87BB, "SR1: V=bit6(TDRA), N=bit7(IRQ)", align=Align.INLINE)
d.label(0x87BE, "tx_fifo_write")

d.comment(0x87BE, "TDRA not set -- TX error", align=Align.INLINE)
d.comment(0x87C0, "Load byte from TX buffer", align=Align.INLINE)
d.comment(0x87C3, "Write to TX_DATA (continue frame)", align=Align.INLINE)
d.comment(0x87C6, "Next TX buffer byte", align=Align.INLINE)
d.comment(0x87C7, "Load second byte from TX buffer", align=Align.INLINE)
d.comment(0x87CA, "Advance TX index past second byte", align=Align.INLINE)
d.comment(0x87CB, "Save updated TX buffer index", align=Align.INLINE)
d.comment(0x87CE, "Write second byte to TX_DATA", align=Align.INLINE)
d.comment(0x87D1, "Compare index to TX length", align=Align.INLINE)
d.comment(0x87D4, "Frame complete -- go to TX_LAST_DATA", align=Align.INLINE)
d.comment(0x87D6, "Check if we can send another pair", align=Align.INLINE)
d.comment(0x87D9, "IRQ set -- send 2 more bytes (tight loop)", align=Align.INLINE)
d.comment(0x87DB, "Wait for next NMI", align=Align.INLINE)
d.label(0x87DE, "tx_error")

d.entry(0x87DE)
d.comment(0x87DE, "Error &42", align=Align.INLINE)
d.label(0x87E2, "tx_fifo_not_ready")

d.comment(0x87E2, "CR2=&67: clear status, return to listen", align=Align.INLINE)
d.comment(0x87E4, "Write CR2: clear status, idle listen", align=Align.INLINE)
d.comment(0x87E7, "Error &41 (TDRA not ready)", align=Align.INLINE)
d.label(0x87E9, "tx_store_error")

d.comment(0x87E9, "INTOFF: disable NMIs (Master &FE38)", align=Align.INLINE)
d.label(0x87EC, "delay_nmi_disable")

d.comment(0x87EC, "PHA/PLA delay loop (256 iterations for NMI disable)", align=Align.INLINE)
d.comment(0x87ED, "PHA/PLA delay (~7 cycles each)", align=Align.INLINE)
d.comment(0x87EE, "Increment delay counter", align=Align.INLINE)
d.comment(0x87EF, "Loop 256 times for NMI disable", align=Align.INLINE)
d.comment(0x87F1, "Store error and return to idle", align=Align.INLINE)
d.entry(0x87F4)
d.subroutine(
    0x87F4,
    "tx_last_data",
    title="TX_LAST_DATA and frame completion",
    description="""Signals end of TX frame by writing `CR2=&3F` (TX_LAST_DATA), then
installs [`nmi_tx_complete`](label:nmi_tx_complete) as the next NMI
handler.

`CR2=&3F` = `%0011_1111`, with each bit selecting an ADLC
control function:

| Bit | Mnemonic | Effect |
|-----|----------|--------|
| 7   | (RTS)    | **0** – drops RTS after frame |
| 6   | (CLR_TX_ST) | **0** – do *not* clear TX status |
| 5   | CLR_RX_ST | clears `fv_stored_` (prepares for RX of reply) |
| 4   | TX_LAST_DATA | tells the ADLC this is the final data byte |
| 3   | FLAG_IDLE | send flags / idle after the frame |
| 2   | FC_TDRA  | force clear TDRA |
| 1   | 2_1_BYTE | two-byte transfer mode |
| 0   | PSE      | prioritised status enable |

The routine exits via `JMP` to
[`set_nmi_vector`](label:set_nmi_vector), which installs
[`nmi_tx_complete`](label:nmi_tx_complete) and falls through to
[`nmi_rti`](label:nmi_rti). The `BIT` of
[`enable_net_nmis`](label:enable_net_nmis) (INTON) inside
[`nmi_rti`](label:nmi_rti) creates the /NMI edge for the
frame-complete interrupt – essential because the ADLC IRQ may
transition atomically from TDRA to frame-complete without
de-asserting in between.""",
)


d.comment(0x87F4, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", align=Align.INLINE)
d.comment(0x87F6, "Write to ADLC CR2", align=Align.INLINE)
d.comment(0x87F9, "Install TX->RX switch handler (low)", align=Align.INLINE)
# UNMAPPED: d.comment(0x872A, "High byte of handler address", align=Align.INLINE)
d.comment(0x87FB, "Install and return via set_nmi_vector", align=Align.INLINE)
d.entry(0x87FE)
d.subroutine(
    0x87FE,
    "nmi_tx_complete",
    title="TX completion: switch to RX mode",
    description="""Called via NMI after the frame (including CRC and closing flag)
has been fully transmitted. Writes `CR1=&82` (`TX_RESET | RIE`)
to clear `RX_RESET` and enable RX interrupts – the **TX-to-RX
pivot** in the four-way handshake. The scout ACK can only be
received after this point.

Full `CR1` sequence through a handshake:

| Step | `CR1` | Meaning |
|---|---|---|
| 1 | `&44` | scout TX |
| 2 | `&82` | await scout ACK |
| 3 | `&44` | data TX |
| 4 | `&82` | await data ACK |

Dispatches on [`net_frame_flags`](label:net_frame_flags) flags:

| Flag | Action |
|---|---|
| bit 6 set (broadcast) | jump to [`tx_result_ok`](label:tx_result_ok) |
| bit 0 set (handshake data pending) | jump to [`handshake_await_ack`](label:handshake_await_ack) |
| both clear | install [`nmi_reply_scout`](label:nmi_reply_scout) for scout ACK reception |""",
)


d.comment(0x87FE, "Jump to error handler", align=Align.INLINE)
d.comment(0x8800, "Write CR1 to switch from TX to RX", align=Align.INLINE)
d.comment(0x8803, "Test workspace flags", align=Align.INLINE)
d.comment(0x8806, "bit6 not set -- check bit0", align=Align.INLINE)
d.comment(0x8808, "bit6 set -- TX completion", align=Align.INLINE)
d.label(0x880B, "check_handshake_bit")

d.comment(0x880B, "A=1: mask for bit0 test", align=Align.INLINE)
d.comment(0x880D, "Test tx_flags bit0 (handshake)", align=Align.INLINE)
d.comment(0x8810, "bit0 clear: install reply handler", align=Align.INLINE)
d.comment(0x8812, "bit0 set -- four-way handshake data phase", align=Align.INLINE)
d.label(0x8815, "install_reply_scout")

d.comment(0x8815, "Install nmi_reply_scout (low)", align=Align.INLINE)
d.comment(0x8819, "Install handler", align=Align.INLINE)
d.entry(0x881C)
d.subroutine(
    0x881C,
    "nmi_reply_scout",
    title="RX reply-scout handler",
    description="""NMI handler installed before the reply-scout reception phase.
Tests `SR2` bit 0 (`AP`) for an incoming address; on `AP` clear
falls through to `tx_error`. Otherwise reads the first RX byte
(destination station) and compares it against the workspace copy
[`tx_src_stn`](label:tx_src_stn). On mismatch branches to
[`reject_reply`](label:reject_reply); on match installs
[`nmi_reply_cont`](label:nmi_reply_cont) as the next NMI handler via
[`install_nmi_handler`](label:install_nmi_handler) (low-byte only -- the high
byte stays at `&87`).""",
)


d.comment(0x881C, "A=&01: AP mask for SR2", align=Align.INLINE)
d.comment(0x881E, "Test SR2 AP (Address Present)", align=Align.INLINE)
d.comment(0x8821, "No AP -- error", align=Align.INLINE)
d.comment(0x8823, "Read first RX byte (destination station)", align=Align.INLINE)
d.comment(0x8826, "Compare to our station ID (workspace copy)", align=Align.INLINE)
d.comment(0x8829, "Not our station -- error/reject", align=Align.INLINE)
d.comment(0x882B, "Install reply-continuation handler (low)", align=Align.INLINE)
d.comment(0x882D, "Install continuation handler", align=Align.INLINE)
d.entry(0x8830)
d.subroutine(
    0x8830,
    "nmi_reply_cont",
    title="RX reply continuation handler",
    description="""Reads the second byte of the reply scout (destination network)
and validates it is zero (local network). Loads `A=&76`, the low
byte of [`nmi_reply_validate`](label:nmi_reply_validate), to install it as
the next NMI handler.

**Optimisation:** before installing, checks `SR1` bit 7 (`IRQ`
still asserted) via `BIT econet_control1_or_status1` / `BMI`. When `IRQ` is still
set the next byte is already in the FIFO, so the routine falls
through directly to [`nmi_reply_validate`](label:nmi_reply_validate) without
an intermediate `RTI`, avoiding NMI re-entry overhead for short
frames where all bytes arrive in quick succession.""",
)


d.comment(0x8830, "Read RX byte (destination station)", align=Align.INLINE)
d.comment(0x8833, "No RDA -- error", align=Align.INLINE)
d.comment(0x8835, "Read destination network byte", align=Align.INLINE)
d.comment(0x8838, "Non-zero -- network mismatch, error", align=Align.INLINE)
d.comment(0x883A, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x883C, "Test SR1 IRQ (N=bit7) -- more data ready?", align=Align.INLINE)
d.comment(0x883F, "IRQ set -- fall through to &884A", align=Align.INLINE)
d.comment(0x8841, "IRQ not set -- install handler", align=Align.INLINE)
d.label(0x8844, "reject_reply")

d.subroutine(
    0x8844,
    "reject_reply",
    title="Abandon reply scout (1-instruction trampoline)",
    description="""Single `JMP` to [`tx_result_fail`](label:tx_result_fail). Acts as a
near-target for the `BPL`/`BNE` exits scattered through
[`nmi_reply_scout`](label:nmi_reply_scout),
[`nmi_reply_validate`](label:nmi_reply_validate), and
[`nmi_scout_ack_src`](label:nmi_scout_ack_src) that need to abort the
reply path – the unconditional `JMP` at `&8775` takes them to
[`tx_result_fail`](label:tx_result_fail) (which stores the error and
returns to idle).

Seven inbound refs in total (one `JSR` plus six branches).""",
)


d.comment(0x8844, "Store error and return to idle", align=Align.INLINE)
d.entry(0x8847)
d.subroutine(
    0x8847,
    "nmi_reply_validate",
    title="RX reply validation (Path 2 for FV/PSE interaction)",
    description="""Reads the source station and source network from the reply scout
and validates them against the original TX destination
([`tx_dst_stn`](label:tx_dst_stn) /
[`tx_dst_net`](label:tx_dst_net)).

1. Check SR2 bit 7 (RDA) -- must see data available.
2. Read source station, compare to `tx_dst_stn`.
3. Read source network, compare to `tx_dst_net`.
4. Check SR2 bit 1 (FV) -- must see frame complete.

If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (`CR2=&A7` for RTS, `CR1=&44` for TX mode).""",
)


d.comment(0x8847, "Test SR2 RDA (bit7). Must be set for valid reply.", align=Align.INLINE)
d.comment(0x884A, "No RDA -- error (FV masking RDA via PSE would cause this)", align=Align.INLINE)
d.comment(0x884C, "Read source station", align=Align.INLINE)
d.comment(0x884F, "Compare to original TX destination station (&0D20)", align=Align.INLINE)
d.comment(0x8852, "Mismatch -- not the expected reply, error", align=Align.INLINE)
d.comment(0x8854, "Read source network", align=Align.INLINE)
d.comment(0x8857, "Compare to original TX destination network (&0D21)", align=Align.INLINE)
d.comment(0x885A, "Mismatch -- error", align=Align.INLINE)
d.comment(0x885C, "A=&02: FV mask for SR2 bit1", align=Align.INLINE)
d.comment(0x885E, "Test SR2 FV -- frame must be complete", align=Align.INLINE)
d.comment(0x8861, "No FV -- incomplete frame, error", align=Align.INLINE)
d.comment(0x8863, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", align=Align.INLINE)
d.comment(0x8865, "Write CR2: enable RTS for TX handshake", align=Align.INLINE)
d.comment(0x8868, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", align=Align.INLINE)
d.comment(0x886A, "Write CR1: reset RX, enable TX interrupt", align=Align.INLINE)
d.comment(0x886D, "Install handshake_await_ack into &0D43/&0D44 (four-way data phase)", align=Align.INLINE)
d.comment(0x886F, "High byte &88 of next handler address", align=Align.INLINE)
d.comment(0x8871, "Store low byte to nmi_next_lo", align=Align.INLINE)
d.comment(0x8874, "Store high byte to nmi_next_hi", align=Align.INLINE)
d.comment(0x8877, "Load dest station for scout ACK TX", align=Align.INLINE)
d.comment(0x887A, "Test SR1 TDRA (V=bit6)", align=Align.INLINE)
d.comment(0x887D, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x887F, "Write dest station to TX FIFO", align=Align.INLINE)
d.comment(0x8882, "Write dest network to TX FIFO", align=Align.INLINE)
d.comment(0x8885, "Write dest network to TX FIFO", align=Align.INLINE)
d.comment(0x8888, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x888A, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x888C, "Set NMI vector and return", align=Align.INLINE)
d.entry(0x888F)
d.subroutine(
    0x888F,
    "nmi_scout_ack_src",
    title="TX scout ACK: write source address",
    description="""Continuation of the TX-side scout ACK. Reads our station ID from
the workspace copy [`tx_src_stn`](label:tx_src_stn), tests `TDRA`
via `SR1`, and writes `(station, network=0)` to the TX FIFO.

Then dispatches on bit 1 of [`net_frame_flags`](label:net_frame_flags) to
select the next NMI handler:

| Bit 1 | Handler |
|---|---|
| set   | immediate-op data NMI handler |
| clear | normal [`nmi_tx_data`](label:nmi_tx_data) |

Installs the chosen handler via
[`set_nmi_vector`](label:set_nmi_vector). Shares the
[`tx_check_tdra_ready`](label:tx_check_tdra_ready) entry with
[`ack_tx`](label:ack_tx).""",
)


d.comment(0x888F, "Load our station ID from workspace copy", align=Align.INLINE)
d.comment(0x8892, "Test SR1 TDRA", align=Align.INLINE)
d.label(0x8895, "tx_check_tdra_ready")

d.comment(0x8895, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x8897, "Write our station to TX FIFO", align=Align.INLINE)
d.comment(0x889A, "Write network=0 to TX FIFO", align=Align.INLINE)
d.comment(0x889C, "Write network byte to TX FIFO", align=Align.INLINE)
d.label(0x889F, "data_tx_begin")

d.subroutine(
    0x889F,
    "data_tx_begin",
    title="Begin data-frame TX: install nmi_data_tx or alt",
    description="""Tests bit 1 of [`net_frame_flags`](label:net_frame_flags)
([`tx_flags`](label:tx_flags)):

| Bit 1 | Path |
|---|---|
| set (immediate-op) | branch to `install_imm_data_nmi` to use the alternative handler |
| clear | install the [`nmi_data_tx`](label:nmi_data_tx) alt-entry at `&87ED` (lo=`&EB`, hi=`&87`) into the NMI vector. The alt-entry skips the page-counter check and goes straight to the byte-count load |

Single caller (`&8339` inside [`ack_tx`](label:ack_tx)).""",
)


d.comment(0x889F, "Test bit 1 of tx_flags", align=Align.INLINE)
d.comment(0x88A1, "Check if immediate-op or data-transfer", align=Align.INLINE)
d.comment(0x88A4, "Bit 1 set: immediate op, use alt handler", align=Align.INLINE)
d.comment(0x88A6, "Install nmi_data_tx alt-entry (low)", align=Align.INLINE)
d.comment(0x88A8, "Y=&88: high byte of nmi_data_tx", align=Align.INLINE)
d.comment(0x88AA, "Install and return via set_nmi_vector", align=Align.INLINE)
d.label(0x88AD, "install_imm_data_nmi")

d.comment(0x88AD, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x88AF, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x88B1, "Install and return via set_nmi_vector", align=Align.INLINE)
d.entry(0x88B4)
d.subroutine(
    0x88B4,
    "nmi_data_tx",
    title="TX data phase: send payload",
    description="""NMI handler that transmits the data payload of a four-way
handshake. Loads bytes from `(open_port_buf),Y` (or from Tube
R3 in the immediate-op variant), writing pairs to the TX FIFO.
After each pair, decrements the byte counters
(`port_buf_len`/`port_buf_len_hi`):

| Condition | Action |
|---|---|
| `port_buf_len_hi = 0` (final partial page) | branch to `data_tx_last` (internal label) to send the remaining bytes and tail-call [`tx_last_data`](label:tx_last_data) |
| count > 0, `SR1` IRQ still set | tight loop: write another pair without returning from NMI |
| count > 0, `SR1` IRQ clear | return via `RTI` and wait for next NMI |

The alt-entry at `&87ED` (used by
[`data_tx_begin`](label:data_tx_begin)) skips the page-counter check
and starts at the byte-count load.""",
)


d.comment(0x88B4, "Y = buffer offset, resume from last position", align=Align.INLINE)
d.comment(0x88B6, "No pages left: send final partial page", align=Align.INLINE)
d.comment(0x88B8, "Load remaining byte count", align=Align.INLINE)
d.comment(0x88BA, "Zero bytes left: skip to TDRA check", align=Align.INLINE)
d.comment(0x88BC, "Load remaining byte count (alt entry)", align=Align.INLINE)
d.comment(0x88BE, "Zero: loop back to top of handler", align=Align.INLINE)
d.label(0x88C0, "check_tdra_status")

d.comment(0x88C0, "Test SR1 TDRA (V=bit6)", align=Align.INLINE)
d.label(0x88C3, "data_tx_check_fifo")

d.comment(0x88C3, "TDRA not ready -- error", align=Align.INLINE)
d.comment(
    0x88C5,
    """Save/restore ACCCON across the (open_port_buf),Y reads
in this TX FIFO loop. Same idiom as copy_scout_to_buffer / nmi_data_rx_bulk;
workspace &97 holds the desired ACCCON value pre-loaded by the caller.""",
)
d.comment(0x88C5, "Save current ACCCON on stack", align=Align.INLINE)
d.comment(0x88C8, "Push ACCCON snapshot", align=Align.INLINE)
d.comment(0x88C9, "Load desired ACCCON from workspace &97", align=Align.INLINE)
d.comment(0x88CB, "Set ACCCON for the upcoming buffer reads", align=Align.INLINE)
d.comment(0x88CE, "Write data byte to TX FIFO", align=Align.INLINE)
d.comment(0x88D0, "Write first byte of pair to FIFO", align=Align.INLINE)
d.comment(0x88D3, "Advance buffer offset", align=Align.INLINE)
d.comment(0x88D4, "No page crossing", align=Align.INLINE)
d.comment(0x88D6, "Page crossing: decrement page count", align=Align.INLINE)
d.comment(0x88D8, "No pages left: send last data", align=Align.INLINE)
d.comment(0x88DA, "Increment buffer high byte", align=Align.INLINE)
d.label(0x88DC, "write_second_tx_byte")

d.comment(0x88DC, "Load second byte of pair", align=Align.INLINE)
d.comment(0x88DE, "Write second byte to FIFO", align=Align.INLINE)
d.comment(0x88E1, "Advance buffer offset", align=Align.INLINE)
d.comment(0x88E2, "Save updated buffer position", align=Align.INLINE)
d.comment(0x88E4, "No page crossing", align=Align.INLINE)
d.comment(0x88E6, "Page crossing: decrement page count", align=Align.INLINE)
d.comment(0x88E8, "No pages left: send last data", align=Align.INLINE)
d.comment(0x88EA, "Increment buffer high byte", align=Align.INLINE)
d.comment(0x88EC, "Pull saved ACCCON from stack", align=Align.INLINE)
d.label(0x88EC, "check_fifo_loop")

d.comment(0x88ED, "Restore caller's ACCCON between byte pairs", align=Align.INLINE)
d.label(0x88F0, "check_irq_loop")

d.comment(0x88F0, "Test ADLC SR1 IRQ flag for next byte pair", align=Align.INLINE)
d.comment(0x88F3, "IRQ still set: more bytes to send", align=Align.INLINE)
d.comment(0x88F5, "IRQ cleared: return from NMI", align=Align.INLINE)
d.comment(0x88F8, "Pull saved ACCCON (frame-end path)", align=Align.INLINE)
d.label(0x88F8, "frame_end_restore")

d.comment(0x88F9, "Restore caller's ACCCON before TX_LAST_DATA", align=Align.INLINE)
d.label(0x88FC, "data_tx_last")

d.comment(0x88FC, "CR2=&3F: TX_LAST_DATA (close data frame)", align=Align.INLINE)
d.comment(0x88FE, "Write CR2 to close frame", align=Align.INLINE)
d.comment(0x8901, "Check tx_flags for next action", align=Align.INLINE)
d.comment(0x8904, "Bit7 clear: error, install saved handler", align=Align.INLINE)
d.comment(0x8906, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8908, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x890A, "Set NMI vector and return", align=Align.INLINE)
d.label(0x890D, "install_saved_handler")

d.comment(0x890D, "Load saved next handler low byte", align=Align.INLINE)
d.comment(0x8910, "Load saved next handler high byte", align=Align.INLINE)
d.comment(0x8913, "Install saved handler and return", align=Align.INLINE)
d.label(0x8916, "nmi_data_tx_tube")

d.entry(0x8916)
d.subroutine(
    0x8916,
    "nmi_data_tx_tube",
    title="NMI handler: TX FIFO write from Tube buffer",
    description="""NMI continuation handler used during TX of a Tube-sourced data
frame. Tests SR1 TDRA via `BIT
econet_control1_or_status1`, writes the next pair of bytes from
the Tube buffer to the ADLC TX FIFO (the `tube_tx_fifo_write`
shared body at `&884A`), and either continues the tight inner loop
on a continuing IRQ or returns via `RTI`. Reached only via the NMI
vector after [`tx_prepare`](label:tx_prepare) installs it.""",
)


d.comment(0x8916, "Tube TX: test SR1 TDRA", align=Align.INLINE)
d.label(0x8919, "tube_tx_fifo_write")

d.comment(0x8919, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x891B, "Read byte from Tube R3", align=Align.INLINE)
d.comment(0x891E, "Write to TX FIFO", align=Align.INLINE)
d.comment(0x8921, "Increment 4-byte buffer counter", align=Align.INLINE)
d.comment(0x8923, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x8925, "Carry into second byte", align=Align.INLINE)
d.comment(0x8927, "No further carry", align=Align.INLINE)
d.comment(0x8929, "Carry into third byte", align=Align.INLINE)
d.comment(0x892B, "No further carry", align=Align.INLINE)
d.comment(0x892D, "Carry into fourth byte", align=Align.INLINE)
d.comment(0x892F, "Counter wrapped to zero: last data", align=Align.INLINE)
d.label(0x8931, "write_second_tube_byte")

d.comment(0x8931, "Read second Tube byte from R3", align=Align.INLINE)
d.comment(0x8934, "Write second byte to TX FIFO", align=Align.INLINE)
d.comment(0x8937, "Increment 4-byte counter (second byte)", align=Align.INLINE)
d.comment(0x8939, "Low byte didn't wrap", align=Align.INLINE)
d.label(0x893B, "tube_tx_inc_byte2")

d.comment(0x893B, "Carry into second byte", align=Align.INLINE)
d.comment(0x893D, "No further carry", align=Align.INLINE)
d.label(0x893F, "tube_tx_inc_byte3")

d.comment(0x893F, "Carry into third byte", align=Align.INLINE)
d.label(0x85BB, "tx_length_table")

d.comment(0x8941, "No further carry", align=Align.INLINE)
d.label(0x8943, "tube_tx_inc_byte4")

d.comment(0x8943, "Carry into fourth byte", align=Align.INLINE)
d.comment(0x8945, "Counter wrapped to zero: last data", align=Align.INLINE)
d.label(0x8947, "check_tube_irq_loop")

d.comment(0x8947, "Test SR1 IRQ for tight loop", align=Align.INLINE)
d.label(0x85C3, "tx_flags_table")

d.comment(0x894A, "IRQ still set: write 2 more bytes", align=Align.INLINE)
d.comment(0x894C, "No IRQ: return, wait for next NMI", align=Align.INLINE)
d.label(0x894F, "tx_tdra_error")

d.comment(0x894F, "TX error: check flags for path", align=Align.INLINE)
d.comment(0x8952, "Bit7 clear: TX result = not listening", align=Align.INLINE)
d.comment(0x8954, "Bit7 set: discard and return to listen", align=Align.INLINE)
d.entry(0x8957)
d.subroutine(
    0x8957,
    "handshake_await_ack",
    title="Four-way handshake: switch to RX for final ACK",
    description="""Called via JMP from [`nmi_tx_complete`](label:nmi_tx_complete) when bit 0
of [`tx_flags`](label:tx_flags) is set (four-way handshake in
progress). Writes `CR1=&82` (`TX_RESET|RIE`) to switch the ADLC
from TX mode to RX mode, listening for the final ACK from the
remote station. Installs [`nmi_final_ack`](label:nmi_final_ack) as the
next NMI handler via [`set_nmi_vector`](label:set_nmi_vector).""",
)


d.comment(0x8957, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", align=Align.INLINE)
d.comment(0x8959, "Write to ADLC CR1", align=Align.INLINE)
d.comment(0x895C, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x895E, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x8960, "Install and return via set_nmi_vector", align=Align.INLINE)
d.entry(0x8963)
d.subroutine(
    0x8963,
    "nmi_final_ack",
    title="RX final ACK handler",
    description="""Receives the final ACK in a four-way handshake. Same validation
pattern as [`nmi_reply_validate`](label:nmi_reply_validate):

1. Check AP, read dest_stn, compare to our station.
2. Check RDA, read dest_net, validate = 0.
3. Check RDA, read src_stn / src_net, compare to TX dest.
4. Check FV for frame completion.

On success, stores result=0 via
[`tx_result_ok`](label:tx_result_ok). On failure, error &41.""",
)


d.comment(0x8963, "A=&01: AP mask", align=Align.INLINE)
d.comment(0x8965, "Test SR2 AP", align=Align.INLINE)
d.comment(0x8968, "No AP -- error", align=Align.INLINE)
d.comment(0x896A, "Read dest station", align=Align.INLINE)
d.comment(0x896D, "Compare to our station (workspace copy)", align=Align.INLINE)
d.comment(0x8970, "Not our station -- error", align=Align.INLINE)
d.comment(0x8972, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8974, "Install continuation handler", align=Align.INLINE)
d.label(0x8977, "nmi_final_ack_net")

d.entry(0x8977)
d.subroutine(
    0x8977,
    "nmi_final_ack_net",
    title="NMI handler: final-ACK source-net validation",
    description="""NMI continuation entry installed by `nmi_final_ack`. Polls SR2 for
RDA, reads the source-network byte from the ADLC RX FIFO, and
compares with the original TX destination network (`tx_dst_net`,
`&0D21`). On mismatch, branches to
[`tx_result_fail`](label:tx_result_fail). On match, falls through into
[`nmi_final_ack_validate`](label:nmi_final_ack_validate) for the source-station
check. Reached only via the NMI vector (no static caller).""",
    on_exit={"a": "source-network byte read from FIFO"},
)


d.comment(0x8977, "Test SR2 RDA", align=Align.INLINE)
d.comment(0x897A, "No RDA -- error", align=Align.INLINE)
d.comment(0x897C, "Read dest network", align=Align.INLINE)
d.comment(0x897F, "Non-zero -- network mismatch, error", align=Align.INLINE)
d.comment(0x8981, "Install nmi_final_ack_validate handler", align=Align.INLINE)
d.comment(0x8983, "Test SR1 IRQ -- more data ready?", align=Align.INLINE)
d.comment(0x8986, "IRQ set -- fall through to validate", align=Align.INLINE)
d.comment(0x8988, "Install handler", align=Align.INLINE)
d.entry(0x898B)
d.subroutine(
    0x898B,
    "nmi_final_ack_validate",
    title="Final ACK validation",
    description="""Continuation of [`nmi_final_ack`](label:nmi_final_ack). Tests `SR2`
for `RDA`, then reads the source station and source network
bytes from the RX FIFO, comparing each against the original TX
destination at [`tx_dst_stn`](label:tx_dst_stn) and
[`tx_dst_net`](label:tx_dst_net). Finally tests `SR2` bit 1
(`FV`) for frame completion.

Any mismatch or missing `FV` branches to
[`tx_result_fail`](label:tx_result_fail). On success, falls through
to [`tx_result_ok`](label:tx_result_ok).""",
)


d.comment(0x898B, "Test SR2 RDA", align=Align.INLINE)
d.comment(0x898E, "No RDA -- error", align=Align.INLINE)
d.comment(0x8990, "Read source station", align=Align.INLINE)
d.comment(0x8993, "Compare to TX dest station (&0D20)", align=Align.INLINE)
d.comment(0x8996, "Mismatch -- error", align=Align.INLINE)
d.comment(0x8998, "Read source network", align=Align.INLINE)
d.comment(0x899B, "Compare to TX dest network (&0D21)", align=Align.INLINE)
d.comment(0x899E, "Mismatch -- error", align=Align.INLINE)
d.comment(0x89A0, "Load TX flags for next action", align=Align.INLINE)
d.comment(0x89A3, "bit7 clear: no data phase", align=Align.INLINE)
d.comment(0x89A5, "Install data RX handler", align=Align.INLINE)
d.label(0x89A8, "check_fv_final_ack")

d.comment(0x89A8, "A=&02: FV mask for SR2 bit1", align=Align.INLINE)
d.comment(0x89AA, "Test SR2 FV -- frame must be complete", align=Align.INLINE)
d.comment(0x89AD, "No FV -- error", align=Align.INLINE)
d.entry(0x89AF)
d.subroutine(
    0x89AF,
    "tx_result_ok",
    title="TX completion handler",
    description="""Loads `A=0` (success) and branches unconditionally to
[`tx_store_result`](label:tx_store_result) (`BEQ` is always taken since
A=0, skipping the `tx_result_fail` body at &88E2). This two-
instruction entry point exists so that `JMP` sites can target
the success path without needing to set `A`. Called from
[`ack_tx`](label:ack_tx) for final-ACK completion and from
[`nmi_tx_complete`](label:nmi_tx_complete) for immediate-op completion
where no ACK is expected.""",
    on_exit={"a": "0 (TX success)"},
)


d.comment(0x89AF, "A=0: success result code", align=Align.INLINE)
d.comment(0x89B1, "Always taken (A=0)", align=Align.INLINE)
d.label(0x89B3, "tx_result_fail")

d.subroutine(
    0x89B3,
    "tx_result_fail",
    title="TX failure: not listening",
    description="""Loads error code `&41` ("not listening") and falls through to
[`tx_store_result`](label:tx_store_result). The most common TX-error
path – reached from 11 sites across the final-ACK validation
chain when the remote station doesn't respond or the frame is
malformed.""",
    on_exit={"a": "&41 ('not listening' TX error)"},
)


d.comment(0x89B3, "A=&41: not listening error code", align=Align.INLINE)
d.entry(0x89B5)
d.subroutine(
    0x89B5,
    "tx_store_result",
    title="TX result store and completion",
    description="""Stores the TX result code (in `A`) at offset 0 of the TX control
block via `(nmi_tx_block),Y=0`. Sets
[`tx_complete_flag`](label:tx_complete_flag) to `&80` to signal TX
completion to the foreground polling loop. Then jumps to
[`discard_reset_rx`](label:discard_reset_rx) for a full ADLC reset and
return to idle RX-listen mode.""",
    on_entry={"a": "result code (0=success, &40=jammed, &41=not listening)"},
)


d.comment(0x89B5, "Y=0: index into TX control block", align=Align.INLINE)
d.comment(0x89B7, "Store result/error code at (nmi_tx_block),0", align=Align.INLINE)
d.comment(0x89B9, "A=&80: TX-complete signal for tx_complete_flag", align=Align.INLINE)
d.comment(0x89BB, "Signal TX complete", align=Align.INLINE)
d.comment(0x89BE, "Full ADLC reset and return to idle listen", align=Align.INLINE)


# UNMAPPED: d.subroutine(
# UNMAPPED:     0x8900,
# UNMAPPED:     "tx_calc_transfer",
# UNMAPPED:     title="Calculate transfer size and reclaim Tube buffer",
# UNMAPPED:     description="""Inspects `RXCB[6..7]` (buffer end address byte 2 and high) to
# UNMAPPED: detect a Tube buffer (high=`&FF`, byte 2 in `[&FE, &FF]`).
# UNMAPPED: 
# UNMAPPED: | Buffer type | Action |
# UNMAPPED: |---|---|
# UNMAPPED: | Tube | compute 4-byte transfer size by subtracting `RXCB[8..&B]` (start) from `RXCB[4..7]` (end); store via `(port_ws_offset),Y`; re-claim Tube via `JSR &0406` with claim type `&C2` |
# UNMAPPED: | Non-Tube | fall through to `fallback_calc_transfer` for a 1-byte size subtraction without the Tube reclaim |
# UNMAPPED: 
# UNMAPPED: Three callers: [`scout_complete`](label:scout_complete) (`&819A`),
# UNMAPPED: [`rx_imm_peek`](address:84CE) (`&84DB`),
# UNMAPPED: [`tx_ctrl_proc`](label:tx_ctrl_proc) (`&86DD`).""",
# UNMAPPED:     on_entry={"y": "0 -- caller convention"},
# UNMAPPED:     on_exit={"a": "transfer status", "c": "set if Tube address claimed, clear otherwise"},
# UNMAPPED: )


d.comment(0x85B0, "Read ACCCON (access-control register)", align=Align.INLINE)
d.comment(0x85B3, "Set bit 3 of A (transfer-mode flag)", align=Align.INLINE)
d.comment(0x85B5, "Store as escapable mode", align=Align.INLINE)
d.comment(0x85B7, "Y=7: scout-bytes counter", align=Align.INLINE)
d.comment(0x85B9, "Read RXCB[7] (buffer addr high byte)", align=Align.INLINE)
d.comment(0x85BB, "Compare to &FF", align=Align.INLINE)
d.comment(0x85BD, "Not &FF: normal buffer, skip Tube check", align=Align.INLINE)
d.comment(0x85C0, "Read RXCB[6] (buffer addr byte 2)", align=Align.INLINE)
d.comment(0x85C2, "Check if addr byte 2 >= &FE (Tube range)", align=Align.INLINE)
d.comment(0x85C4, "C clear: no Tube, plain transfer path", align=Align.INLINE)
d.comment(0x85C6, "Z clear (other state set): use fallback path", align=Align.INLINE)
d.comment(0x85C8, "Z set: re-read ACCCON for second decision", align=Align.INLINE)
d.comment(0x85CB, "Rotate bit 0 (E flag) into C", align=Align.INLINE)
d.comment(0x85CC, "C clear: shadow not enabled, fallback path", align=Align.INLINE)
d.comment(0x85CE, "Shadow enabled: set bit 2 of escapable", align=Align.INLINE)
d.comment(0x85D0, "Atomic bit-set on escapable", align=Align.INLINE)
d.comment(0x85D2, "Branch to fallback_calc_transfer (always)", align=Align.INLINE)
d.label(0x85D2, "shadow_enable_flag")

d.label(0x85D4, "check_tx_in_progress")

d.comment(0x85D4, "Transmit in progress?", align=Align.INLINE)
d.comment(0x85D7, "No: fallback path", align=Align.INLINE)
d.comment(0x85D9, "Load TX flags for transfer setup", align=Align.INLINE)
d.comment(0x85DC, "Set bit 1 (transfer complete)", align=Align.INLINE)
d.comment(0x85DE, "Store with bit 1 set (Tube xfer)", align=Align.INLINE)
d.comment(0x85E1, "Init borrow for 4-byte subtract", align=Align.INLINE)
d.comment(0x85E2, "Save carry on stack", align=Align.INLINE)
d.comment(0x85E3, "Y=4: start at RXCB offset 4", align=Align.INLINE)
d.label(0x85E5, "calc_transfer_size")

d.comment(0x85E5, "Load RXCB[Y] (current ptr byte)", align=Align.INLINE)
d.comment(0x85E7, "Y += 4: advance to RXCB[Y+4]", align=Align.INLINE)
d.comment(0x85E8, "(continued)", align=Align.INLINE)
d.comment(0x85E9, "(continued)", align=Align.INLINE)
d.comment(0x85EA, "(continued)", align=Align.INLINE)
d.comment(0x85EB, "Restore borrow from previous byte", align=Align.INLINE)
d.comment(0x85EC, "Subtract RXCB[Y+4] (start ptr byte)", align=Align.INLINE)
d.comment(0x85EE, "Store result byte", align=Align.INLINE)
d.comment(0x85F1, "Y -= 3: next source byte", align=Align.INLINE)
d.comment(0x85F2, "(continued)", align=Align.INLINE)
d.comment(0x85F3, "(continued)", align=Align.INLINE)
d.comment(0x85F4, "Save borrow for next byte", align=Align.INLINE)
d.comment(0x85F5, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0x85F7, "No: next byte pair", align=Align.INLINE)
d.comment(0x85F9, "Discard final borrow", align=Align.INLINE)
d.comment(0x85FA, "Save X", align=Align.INLINE)
d.comment(0x85FB, "Save X", align=Align.INLINE)
d.comment(0x85FC, "Compute address of RXCB+4", align=Align.INLINE)
d.comment(0x85FE, "For base pointer addition", align=Align.INLINE)
d.comment(0x85FF, "Add RXCB base to get RXCB+4 addr", align=Align.INLINE)
d.comment(0x8601, "X = low byte of RXCB+4", align=Align.INLINE)
d.comment(0x8602, "Y = high byte of RXCB ptr", align=Align.INLINE)
d.comment(0x8604, "Tube claim type &C2", align=Align.INLINE)
d.comment(0x8606, "Claim Tube transfer address", align=Align.INLINE)
d.comment(0x8609, "No Tube: skip reclaim", align=Align.INLINE)
d.comment(0x860B, "Tube: reclaim with scout status", align=Align.INLINE)
d.comment(0x860E, "Reclaim with scout status type", align=Align.INLINE)
d.comment(0x8611, "Release Tube claim after reclaim", align=Align.INLINE)
d.comment(0x8614, "C=1: Tube address claimed", align=Align.INLINE)
d.label(0x8615, "restore_x_and_return")

d.comment(0x8615, "Restore X", align=Align.INLINE)
d.comment(0x8616, "Restore X from stack", align=Align.INLINE)
d.comment(0x8617, "Return with C = transfer status", align=Align.INLINE)
d.label(0x8618, "fallback_calc_transfer")

d.entry(0x8618)
d.comment(0x8618, "Y=4: RXCB current pointer offset", align=Align.INLINE)
d.comment(0x861A, "Load RXCB[4] (current ptr lo)", align=Align.INLINE)
d.comment(0x861C, "Y=8: RXCB start address offset", align=Align.INLINE)
d.comment(0x861E, "Set carry for subtraction", align=Align.INLINE)
d.comment(0x861F, "Subtract RXCB[8] (start ptr lo)", align=Align.INLINE)
d.comment(0x8621, "Store transfer size lo", align=Align.INLINE)
d.comment(0x8623, "Y=5: current ptr hi offset", align=Align.INLINE)
d.comment(0x8625, "Load RXCB[5] (current ptr hi)", align=Align.INLINE)
d.comment(0x8627, "Propagate borrow only", align=Align.INLINE)
d.comment(0x8629, "Temp store of adjusted hi byte", align=Align.INLINE)
d.comment(0x862B, "Y=8: start address lo offset", align=Align.INLINE)
d.comment(0x862D, "Copy RXCB[8] to open port buffer lo", align=Align.INLINE)
d.comment(0x862F, "Store to scratch (side effect)", align=Align.INLINE)
d.comment(0x8631, "Y=9: start address hi offset", align=Align.INLINE)
d.comment(0x8633, "Load RXCB[9]", align=Align.INLINE)
d.comment(0x8635, "Set carry for subtraction", align=Align.INLINE)
d.comment(0x8636, "Subtract adjusted hi byte", align=Align.INLINE)
d.comment(0x8638, "Store transfer size hi", align=Align.INLINE)
d.comment(0x863A, "Return with C=1", align=Align.INLINE)
d.label(0x863B, "nmi_shim_rom_src")

d.comment(0x863B, "Return with C=1 (success)", align=Align.INLINE)
d.subroutine(
    0x89C1,
    "adlc_full_reset",
    title="ADLC full reset",
    description="""Performs a full ADLC hardware reset:

1. Writes `CR1=&C1` (`TX_RESET | RX_RESET | AC`) to put both TX
   and RX sections in reset with address-control enabled.
2. Configures `CR4=&1E` (8-bit RX word, abort extend, NRZ
   encoding).
3. Configures `CR3=&00` (no loopback, no AEX, NRZ, no DTR).
4. Falls through to [`adlc_rx_listen`](label:adlc_rx_listen) to
   re-enter RX-listen mode.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0x89C1, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", align=Align.INLINE)
d.comment(0x89C3, "Write CR1 to ADLC register 0", align=Align.INLINE)
d.comment(0x89C6, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", align=Align.INLINE)
d.comment(0x89C8, "Write CR4 to ADLC register 3", align=Align.INLINE)
d.comment(0x89CB, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", align=Align.INLINE)
d.comment(0x89CD, "Write CR3 to ADLC register 1", align=Align.INLINE)
d.subroutine(
    0x89D0,
    "adlc_rx_listen",
    title="Enter RX-listen mode",
    description="""Configures the ADLC for passive RX-listen mode:

| Register | Value | Meaning |
|---|---|---|
| `CR1` | `&82` | `TX_RESET \\| RIE` – TX section held in reset, RX interrupts enabled |
| `CR2` | `&67` | `CLR_TX_ST \\| CLR_RX_ST \\| FC_TDRA \\| 2_1_BYTE \\| PSE` – clear all pending status, enable prioritised status |

This is the idle state where the ADLC listens for incoming scout
frames via NMI.""",
    on_entry={},
    on_exit={"a, x": "clobbered (control byte writes)", "y": "preserved"},
)


d.comment(0x89D0, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", align=Align.INLINE)
d.comment(0x89D2, "Write to ADLC CR1", align=Align.INLINE)
d.comment(0x89D5, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", align=Align.INLINE)
d.comment(0x89D7, "Write to ADLC CR2", align=Align.INLINE)
d.comment(0x89DA, "Return; ADLC now in RX listen mode", align=Align.INLINE)
d.label(0x89DB, "wait_idle_and_reset")

d.subroutine(
    0x89DB,
    "wait_idle_and_reset",
    title="Wait for idle NMI state and reset Econet",
    description="""Service-13 (`&0D`) handler -- the post-hard-reset Econet
shutdown path. Reached via
[`svc_dispatch`](label:svc_dispatch) slot &0D. Checks
[`econet_init_flag`](label:econet_init_flag) to see if Econet has been
initialised; if not, skips straight to
[`adlc_rx_listen`](label:adlc_rx_listen). Otherwise spins in a tight
loop comparing the NMI handler vector at
[`nmi_jmp_lo`](label:nmi_jmp_lo) /
[`nmi_jmp_hi`](label:nmi_jmp_hi) against the address of
[`nmi_rx_scout`](label:nmi_rx_scout) to wait until the in-flight
NMI handler chain has unwound back to scout-listening.

When the NMI vector matches `nmi_rx_scout` again, falls through
to [`save_econet_state`](address:89B9) to clear the initialised
flags and re-enter RX-listen mode. (Service &0B 'NMI release'
is handled by the separate [`econet_restore`](label:econet_restore).)""",
    on_entry={"a": "13 (service call number, &0D)"},
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0x89DB, "Check if Econet has been initialised", align=Align.INLINE)
d.comment(0x89DE, "Not initialised: skip to RX listen", align=Align.INLINE)
d.label(0x89E0, "poll_nmi_idle")

d.comment(0x89E0, "Read current NMI handler low byte", align=Align.INLINE)
d.comment(0x89E3, "Expected: &B3 (nmi_rx_scout low)", align=Align.INLINE)
d.comment(0x89E5, "Not idle: spin and wait", align=Align.INLINE)
d.comment(0x89E7, "Read current NMI handler high byte", align=Align.INLINE)
# UNMAPPED: d.comment(0x89B5, "Test if high byte = &80 (page of nmi_rx_scout)", align=Align.INLINE)
d.comment(0x89EC, "Not idle: spin and wait", align=Align.INLINE)
# UNMAPPED: d.subroutine(
# UNMAPPED:     0x89B9,
# UNMAPPED:     "save_econet_state",
# UNMAPPED:     title="Reset Econet flags and enter RX-listen",
# UNMAPPED:     description="""Disables NMIs via `BIT disable_net_nmis` (the Master 128 dedicated
# UNMAPPED: INTOFF at &FE38), then clears
# UNMAPPED: [`tx_complete_flag`](label:tx_complete_flag) and
# UNMAPPED: [`econet_init_flag`](label:econet_init_flag) by storing the current `A`
# UNMAPPED: value. Sets `Y=5` (service-call workspace page) and jumps to
# UNMAPPED: [`adlc_rx_listen`](label:adlc_rx_listen) to configure the ADLC for
# UNMAPPED: passive listening.
# UNMAPPED: 
# UNMAPPED: Used during the wait-idle-and-reset path (svc &0D) to safely
# UNMAPPED: tear down the Econet state before another ROM can claim the
# UNMAPPED: NMI workspace.""",
# UNMAPPED:     on_entry={"a": "value to store into tx_complete_flag / econet_init_flag (typically 0 to clear)"},
# UNMAPPED:     on_exit={"y": "5 (service-call workspace page)"},
# UNMAPPED: )


d.comment(0x89F3, "INTOFF: disable NMIs", align=Align.INLINE)
# UNMAPPED: d.comment(0x89BC, "INTOFF again (belt-and-braces)", align=Align.INLINE)
d.comment(0x89F8, "TX not in progress", align=Align.INLINE)
d.comment(0x89FB, "Econet not initialised", align=Align.INLINE)
d.comment(0x89FE, "Y=5: service call workspace page", align=Align.INLINE)
d.label(0x8A00, "reset_enter_listen")
d.comment(0x8A00, "Set ADLC to RX listen mode", align=Align.INLINE)
d.label(0x8A02, "nmi_shim_source")

d.entry(0x8A03)
d.subroutine(
    0x8A03,
    "nmi_bootstrap_entry",
    title="Bootstrap NMI entry point (in ROM)",
    description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM shim at the start of the NFS workspace block. Unlike
the RAM shim (which uses a self-modifying `JMP` to dispatch to
different handlers), this one hardcodes
`JMP `[`nmi_rx_scout`](label:nmi_rx_scout). Used as the initial
NMI handler before the workspace has been properly set up during
initialisation.

Same sequence as the RAM shim:

```6502
BIT disable_net_nmis      ; INTOFF (Master 128 dedicated register)
PHA
TYA
PHA
LDA #romsel-bank
STA romsel
JMP nmi_rx_scout
```

The `BIT` of [`disable_net_nmis`](label:disable_net_nmis) (INTOFF) at
entry and `BIT` of [`enable_net_nmis`](label:enable_net_nmis) (INTON)
before `RTI` in [`nmi_rti`](label:nmi_rti) are essential for
edge-triggered NMI re-delivery.

The 6502 /NMI is falling-edge triggered; the Econet NMI-enable
flip-flop gates the ADLC IRQ onto /NMI. INTOFF clears the
flip-flop, forcing /NMI high; INTON sets it, allowing the ADLC
IRQ through. This creates a guaranteed high-to-low edge on /NMI
even when the ADLC IRQ is continuously asserted (e.g. when it
transitions atomically from TDRA to frame-complete without
de-asserting). Without this mechanism,
[`nmi_tx_complete`](label:nmi_tx_complete) would never fire after
[`tx_last_data`](label:tx_last_data).""",
)


d.comment(0x8A03, "INTOFF: force /NMI high (clear NMI flip-flop)", align=Align.INLINE)
d.comment(0x8A06, "Save A", align=Align.INLINE)
d.comment(0x8A07, "Transfer Y to A", align=Align.INLINE)
d.comment(0x8A08, "Save Y (via A)", align=Align.INLINE)
d.comment(0x8A09, "ROM bank 0 (patched during init for actual bank)", align=Align.INLINE)
d.comment(0x8A0B, "Select Econet ROM bank via ROMSEL", align=Align.INLINE)
d.comment(0x8A0E, "Jump to scout handler in ROM", align=Align.INLINE)
d.entry(0x8A11)


d.subroutine(
    0x8A11,
    "rom_set_nmi_vector",
    title="ROM copy of set_nmi_vector + nmi_rti",
    description="""ROM-resident version of the NMI-exit sequence; also the source
for the initial copy to RAM at
[`set_nmi_vector`](label:set_nmi_vector).

| RAM target | Function |
|---|---|
| [`set_nmi_vector`](label:set_nmi_vector) | writes both hi and lo bytes of the `JMP` target at [`nmi_jmp_lo`](label:nmi_jmp_lo) / [`nmi_jmp_hi`](label:nmi_jmp_hi) |
| [`nmi_rti`](label:nmi_rti) | restores the original ROM bank, pulls `Y` and `A` from the stack, then `BIT` of [`enable_net_nmis`](label:enable_net_nmis) (INTON) to re-enable the NMI flip-flop before `RTI` |

The INTON creates a guaranteed falling edge on /NMI if the ADLC
IRQ is already asserted, ensuring the next handler fires
immediately.""",
)


d.comment(0x8A11, "Store handler high byte at &0D0D", align=Align.INLINE)
d.comment(0x8A14, "Store handler low byte at &0D0C", align=Align.INLINE)
d.comment(0x8A17, "Restore NFS ROM bank", align=Align.INLINE)
d.comment(0x8A19, "Page in via hardware latch", align=Align.INLINE)
d.comment(0x8A1C, "Restore Y from stack", align=Align.INLINE)
d.comment(0x8A1D, "Transfer ROM bank to Y", align=Align.INLINE)
d.comment(0x8A1E, "Restore A from stack", align=Align.INLINE)
d.comment(0x8A1F, "INTON: guaranteed /NMI edge if ADLC IRQ asserted", align=Align.INLINE)
d.comment(0x8A22, "Return from interrupt", align=Align.INLINE)
# UNMAPPED: d.index_base(0x89ED, "svc_dispatch_lo")
# UNMAPPED: d.banner(
# UNMAPPED:     0x89ED,
# UNMAPPED:     title="svc_dispatch low-byte table (51 entries)",
# UNMAPPED:     description="""Low-byte half of the `PHA`/`PHA`/`RTS` dispatch table read by
# UNMAPPED: [`svc_dispatch`](label:svc_dispatch) as `LDA &8A23,X`. Paired with
# UNMAPPED: the high-byte half at [`svc_dispatch_hi`](label:svc_dispatch_hi).
# UNMAPPED: 
# UNMAPPED: Index 0 is a placeholder (target value unused – never reached);
# UNMAPPED: indices 1..50 cover:
# UNMAPPED: 
# UNMAPPED: - service handlers
# UNMAPPED: - language reply handlers
# UNMAPPED: - FSCV reasons
# UNMAPPED: - FS reply handlers
# UNMAPPED: - net-handle / OSWORD `&13` trampolines
# UNMAPPED: 
# UNMAPPED: Per-entry inline comments give the index and the call/reply each
# UNMAPPED: slot dispatches.""",
# UNMAPPED: )
# UNMAPPED: for addr in range(0x89ED, 0x8A20):
# UNMAPPED (orphan body):     d.byte(addr)
# UNMAPPED (orphan body): 
# UNMAPPED: d.index_base(0x8A20, "svc_dispatch_hi")
# UNMAPPED: d.banner(
# UNMAPPED:     0x8A20,
# UNMAPPED:     title="svc_dispatch high-byte table (51 entries + 1 padding)",
# UNMAPPED:     description="""High-byte half of the `PHA`/`PHA`/`RTS` dispatch table read by
# UNMAPPED: [`svc_dispatch`](label:svc_dispatch) as `LDA &8A22,X`. The
# UNMAPPED: dispatcher pushes the hi byte first then the lo, so `RTS` lands
# UNMAPPED: on `target` (the table stores `target-1`). The trailing byte at
# UNMAPPED: `&8A53` is 1-byte padding – there are only 51 valid entries
# UNMAPPED: (0..50).""",
# UNMAPPED: )
# UNMAPPED: for addr in range(0x8A20, 0x8A54):
# UNMAPPED (orphan body):     d.byte(addr)
# UNMAPPED: d.comment(0x8A53, "padding (table has only 51 entries)", align=Align.INLINE)


d.subroutine(
    0x8A8C,
    "service_handler",
    title="Service call dispatch",
    description="""Normalises the incoming service-call number through a
`CMP`/`SBC` chain into a dispatch index, then jumps to the handler
via the PHA/PHA/RTS table at `svc_dispatch_lo` / `svc_dispatch_hi`.
Service call &0F (15, vectors claimed) is special-cased first — it
runs the OS-version check below and then falls through the chain as
a no-op.

The full set of service calls ANFS acts on (service values shown in
decimal and hex):

| Dec |  Hex | Idx | Handler                  | Purpose                     |
|----:|-----:|----:|--------------------------|-----------------------------|
| 0–12| &00–&0C | 1–13 | (service 1–12 handlers) | Standard low service calls |
|  15 |  &0F | — | (prologue)                 | Vectors claimed — OS check  |
|  18 |  &12 | 14 | `svc_18_fs_select`        | FS select                   |
|  24 |  &18 | 15 | `match_on_suffix`         | Interactive `*HELP` `ON ` matcher |
|  33 |  &21 | 16 | `raise_y_to_c8`           | Static workspace claim      |
|  34 |  &22 | 17 | `set_rom_ws_page`         | Dynamic workspace offer     |
|  35 |  &23 | 18 | `store_ws_page_count`     | Top of static workspace     |
|  36 |  &24 | 19 | `noop_dey_rts`            | Dynamic workspace claim     |
|  37 |  &25 | 20 | `copy_template_to_zp`     | FS name + info reply        |
|  38 |  &26 | 21 | `svc_26_close_all_files`  | Close all files             |
|  39 |  &27 | 22 | `nfs_init_body`           | Post-hard-reset re-init     |
|  40 |  &28 | 23 | `print_fs_ps_help`        | `*FS` / `*PS` syntax help   |
|  41 |  &29 | 24 | `svc_29_status`           | `*STATUS` handler           |

Every other value (&0D–&11, &13–&17, &19–&20, &2A and up) falls
through to index 1 (`dispatch_rts`, a no-op) and returns the call
unclaimed — deliberately ignoring e.g. &15 (100 Hz poll) and &2A
(language-ROM startup).

On service &0F (15, vectors claimed) the ROM verifies the host OS
via OSBYTE 0 with the input `X=1`, which returns the OS version
code:

| OSBYTE 1 value | Host                                |
|---------------:|-------------------------------------|
|              0 | OS 1.00 (early BBC B or Electron)   |
|              1 | OS 1.20 or American OS              |
|              2 | OS 2.00 (BBC B+)                    |
|              3 | OS 3.2 / 3.5 (Master 128)           |
|              4 | OS 4.0 (Master Econet Terminal)     |
|              5 | OS 5.0 (Master Compact)             |

Only Master 128 and Master Econet Terminal are supported. Any
other version gets a `Bad ROM <slot>` message printed and its
workspace byte cleared at `&02A0 + adjusted-slot`, effectively
rejecting the ROM.""",
    on_entry={"a": "service call number", "x": "ROM slot", "y": "parameter"},
)

d.comment(0x8A8C, "Save service call number", align=Align.INLINE)
d.comment(0x8A8D, "Service call &0F (vectors claimed)?", align=Align.INLINE)
d.comment(0x8A8F, "No: skip vectors-claimed handling", align=Align.INLINE)
d.comment(0x8A91, "Save Y on stack across the version-check", align=Align.INLINE)
d.comment(0x8A92, "OSBYTE 0: read OS version", align=Align.INLINE)
d.comment(0x8A94, "X=1 to request version number", align=Align.INLINE)
d.comment(0x8A9F, "OS 3.2/3.5 (Master 128)?", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A63, "Yes: target OS, skip Bad ROM message", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A65, "OS 4.0 (Master Econet Terminal)?", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A67, "Yes: target OS, skip Bad ROM message", align=Align.INLINE)
d.comment(0x8AA3, "Transfer OS version to A", align=Align.INLINE)
d.comment(0x8AA4, "Save flags (Z set if OS 1.00) across print", align=Align.INLINE)
d.comment(0x8AA5, "Print '<CR>Bad ROM ' to mark non-Master OS", align=Align.INLINE)
d.comment(0x8AA8, "svc 13 fail path", align=Align.INLINE)
d.comment(0x8AB1, "Load this ROM's slot number", align=Align.INLINE)
d.comment(0x8AB3, "Print slot number as decimal", align=Align.INLINE)
d.comment(0x8AB6, "Print trailing newline, bypassing *SPOOL", align=Align.INLINE)
d.comment(0x8AB9, "Reload ROM slot for workspace clearing", align=Align.INLINE)
d.comment(0x8ABB, "Restore flags", align=Align.INLINE)
d.comment(0x8ABC, "OS 1.00: skip INX (table starts at slot 0)", align=Align.INLINE)
d.comment(0x8ABE, "Adjust index for OS 1.20/2.00/5.00 layout", align=Align.INLINE)
d.label(0x8ABF, "clear_workspace_byte")

d.comment(0x8ABF, "A=0", align=Align.INLINE)
d.comment(0x8AC1, "Clear workspace byte for this ROM", align=Align.INLINE)
d.label(0x8AC4, "restore_rom_slot")

d.comment(0x8AC4, "Restore ROM slot to X", align=Align.INLINE)
d.comment(0x8AC6, "Restore Y from stack", align=Align.INLINE)
d.comment(0x8AC7, "Pop service call number into A", align=Align.INLINE)
d.label(0x8AC7, "restore_rom_slot_entry")

d.comment(0x8AC8, "Re-save service call number", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A8F, "Service call &24 (Dynamic Workspace requirements)?", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A91, "No: skip ADLC check", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A93, "Read ADLC status register 1", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A96, "Mask relevant status bits", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A98, "Non-zero: ADLC absent, set flag", align=Align.INLINE)
# UNMAPPED: d.label(0x8A9A, "set_adlc_absent")

# UNMAPPED: d.comment(0x8A9A, "Shift bit 7 into carry", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A9D, "Set carry to mark ADLC absent", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A9E, "Rotate carry into bit 7 of slot flag", align=Align.INLINE)
d.label(0x8AC9, "check_adlc_flag")

d.comment(0x8AC9, "Load ROM slot flag byte", align=Align.INLINE)
d.comment(0x8ACC, "Shift bit 7 (ADLC absent) into carry", align=Align.INLINE)
d.comment(0x8ACD, "Restore service call number", align=Align.INLINE)
d.comment(0x8ACE, "ADLC present: continue dispatch", align=Align.INLINE)
d.comment(0x8AD0, "ADLC absent: decline service, return", align=Align.INLINE)
d.label(0x8AD1, "dispatch_svc_with_state")

d.comment(0x8AD1, "Transfer service number to X", align=Align.INLINE)
d.comment(0x8AD2, "Save current service state", align=Align.INLINE)
d.comment(0x8AD4, "Push old state", align=Align.INLINE)
d.comment(0x8AD5, "Restore service number to A", align=Align.INLINE)
d.comment(0x8AD6, "Store as current service state", align=Align.INLINE)
d.comment(0x8AD8, "Service < 13?", align=Align.INLINE)
d.comment(0x8ADA, "Yes: use as dispatch index directly", align=Align.INLINE)
d.comment(0x8ADC, "Subtract 5 (map 13-17 to 8-12)", align=Align.INLINE)
d.comment(0x8ADE, "Mapped value = 13? (original was 18)", align=Align.INLINE)
d.comment(0x8AE0, "Yes: valid service 18 (FS select)", align=Align.INLINE)
d.comment(
    0x8AE2, "C clear: service number was below the prior CMP threshold, take dispatch fall-through", align=Align.INLINE
)
d.comment(0x8AE4, "Subtract 5 to remap service range", align=Align.INLINE)
d.comment(0x8AE6, "Compare with &0E", align=Align.INLINE)
d.comment(0x8AE8, "Equal: dispatch directly", align=Align.INLINE)
d.comment(0x8AEA, "Below: take dispatch fall-through", align=Align.INLINE)
d.comment(0x8AEC, "Subtract 8 to remap further", align=Align.INLINE)
d.comment(0x8AEE, "Compare with &0F", align=Align.INLINE)
d.comment(0x8AF0, "Below: dispatch fall-through", align=Align.INLINE)
d.comment(0x8AF2, "Compare with &18", align=Align.INLINE)
d.comment(0x8AF4, "Below: dispatch index now in A", align=Align.INLINE)
d.label(0x8AF6, "dispatch_svc_state_check")

d.comment(0x8AF6, "Unknown service: set index to 0", align=Align.INLINE)
d.label(0x8AF8, "dispatch_svc_index")

d.comment(0x8AF8, "Transfer dispatch index to X", align=Align.INLINE)
d.comment(0x8AF9, "Index 0: unhandled service, skip", align=Align.INLINE)
d.comment(0x8AFB, "Save current workspace page", align=Align.INLINE)
d.comment(0x8AFD, "Push old page", align=Align.INLINE)
d.comment(0x8AFE, "Set workspace page from Y parameter", align=Align.INLINE)
d.comment(0x8B00, "Transfer Y to A", align=Align.INLINE)
d.comment(0x8B01, "Y=0 for dispatch offset", align=Align.INLINE)
d.comment(0x8B03, "Dispatch to service handler via table", align=Align.INLINE)
d.comment(0x8B06, "Restore old workspace page", align=Align.INLINE)
d.comment(0x8B07, "Store it back", align=Align.INLINE)
d.label(0x8B09, "restore_svc_state")

d.comment(0x8B09, "Get service state (return code)", align=Align.INLINE)
d.comment(0x8B0B, "Restore old service state", align=Align.INLINE)
d.comment(0x8B0C, "Store it back", align=Align.INLINE)
d.comment(0x8B0E, "Transfer return code to A", align=Align.INLINE)
d.label(0x8B0F, "restore_romsel_rts")

d.comment(0x8B0F, "Restore ROM slot to X", align=Align.INLINE)
d.comment(0x8B11, "Return to MOS", align=Align.INLINE)
d.comment(0x8B12, "Offset 0 in receive block", align=Align.INLINE)
d.entry(0x8B12)
d.label(0x8B12, "cmd_roff")


d.subroutine(
    0x8B12,
    "cmd_roff",
    title="*ROFF command handler",
    description="""Disables remote operation by clearing the flag at offset 0 in the
receive block. If remote operation was active, re-enables the
keyboard via OSBYTE `&C9` (with `X=0`, `Y=0`) and calls
`tx_econet_abort` with `A=&0A` to reinitialise the workspace
area. Falls through to [`scan_remote_keys`](label:scan_remote_keys)
which clears `svc_state` and `nfs_workspace`.""",
    on_entry={"y": "command line offset (unused -- *ROFF takes no args)"},
    on_exit={"a, x, y": "clobbered"},
)
d.comment(0x8B14, "Load remote operation flag", align=Align.INLINE)
d.comment(0x8B16, "Zero: already off, skip to cleanup", align=Align.INLINE)
d.comment(0x8B18, "A=0", align=Align.INLINE)
d.comment(0x8B1B, "Clear remote operation flag", align=Align.INLINE)
d.comment(0x8B1E, "OSBYTE &C9: keyboard disable", align=Align.INLINE)
d.comment(0x8B23, "A=&0A: workspace init parameter", align=Align.INLINE)
d.comment(0x8B25, "Initialise workspace area", align=Align.INLINE)
d.label(0x8B28, "scan_remote_keys")

d.subroutine(
    0x8B28,
    "scan_remote_keys",
    title="Scan keyboard for remote-operation keys",
    description="""Uses OSBYTE `&7A` with `Y=&7F` to check whether remote-operation
keys (`&CE`..`&CF`) are currently pressed. If neither key is
detected, clears `svc_state` and `nfs_workspace` to zero via the
`clear_svc_and_ws` entry point (also used directly by
[`cmd_roff`](label:cmd_roff)). Called by `check_escape`.

`X` is saved into `nfs_workspace` across the OSBYTE call and
restored each iteration – the loop reuses `A` as the key-code
counter without needing `X`. `clear_svc_and_ws` is also entered
directly (label) by [`cmd_roff`](label:cmd_roff) with no
register pre-conditions.""",
    on_entry={"x": "preserved by being saved to nfs_workspace and reloaded each iteration (no other preconditions)"},
    on_exit={
        "a": "0 (when no key pressed -- the cleared path)",
        "x": "may be modified by OSBYTE",
        "y": "&7F (left over from OSBYTE call setup)",
    },
)


d.comment(0x8B28, "Save X in workspace", align=Align.INLINE)
d.comment(0x8B2A, "A=&CE: start of key range", align=Align.INLINE)
d.label(0x8B2C, "loop_scan_key_range")

d.comment(0x8B2C, "Restore X from workspace", align=Align.INLINE)
d.comment(0x8B2E, "Y=&7F: OSBYTE scan parameter", align=Align.INLINE)
d.comment(0x8B30, "OSBYTE: scan keyboard", align=Align.INLINE)
d.comment(0x8B33, "Advance to next key code", align=Align.INLINE)
d.comment(0x8B35, "Reached &D0?", align=Align.INLINE)
d.comment(0x8B37, "No: loop back (scan &CE and &CF)", align=Align.INLINE)
d.label(0x8B39, "clear_svc_and_ws")

d.comment(0x8B39, "A=0", align=Align.INLINE)
d.comment(0x8B3B, "Clear service state", align=Align.INLINE)
d.comment(0x8B3D, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8B3F, "Return", align=Align.INLINE)
d.label(0x8B40, "save_text_ptr")

d.subroutine(
    0x8B40,
    "save_text_ptr",
    title="Save OS text pointer for later retrieval",
    description="""Copies `&F2`/`&F3` (`os_text_ptr`) into `fs_crc_lo` /
`fs_crc_hi`. Called by [`svc_4_star_command`](label:svc_4_star_command)
and [`svc_9_help`](label:svc_9_help) before attempting command
matches, and by `match_fs_cmd` during iterative help-topic
matching. Preserves `A` via `PHA`/`PLA`.""",
    on_exit={"a": "preserved"},
)


d.comment(0x8B40, "Save A", align=Align.INLINE)
d.comment(0x8B41, "Copy OS text pointer low", align=Align.INLINE)
d.comment(0x8B43, "to fs_crc_lo", align=Align.INLINE)
d.comment(0x8B45, "Copy OS text pointer high", align=Align.INLINE)
d.comment(0x8B47, "to fs_crc_hi", align=Align.INLINE)
d.comment(0x8B49, "Restore A", align=Align.INLINE)
d.label(0x8B4A, "rts_save_text_ptr")

d.comment(0x8B4A, "Return", align=Align.INLINE)
d.comment(0x8B4B, "Get workspace page for this ROM slot", align=Align.INLINE)
d.label(0x8B4B, "cmd_net_fs")

d.subroutine(
    0x8B4B,
    "cmd_net_fs",
    title="Select Econet network filing system",
    description="""Computes a checksum over the first `&77` bytes of the workspace
page and verifies against the stored value; raises an error on
mismatch. On success:

1. Notifies the OS via FSCV reason 6
   ([`notify_new_fs`](label:notify_new_fs)).
2. Copies the FS context block from the receive block to the
   HAZEL FS state at [`hazel_fs_station`](label:hazel_fs_station)
   (offsets 0..9), via the `hazel_minus_2,Y` indexing-base
   trick.
3. Installs 7 filing-system vectors (FILEV etc.) from
   [`fs_vector_table`](label:fs_vector_table).
4. Initialises the ADLC and extended vectors.
5. Sets up the channel table.
6. Sets bit 7 of [`fs_flags`](label:fs_flags) to mark the FS as
   selected.
7. Issues service call 15 (vectors claimed) via
   [`issue_svc_15`](label:issue_svc_15).""",
    on_entry={"y": "command line offset in text pointer (unused for *NET FS but supplied by star-cmd dispatch)"},
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0x8B4E, "Store as high byte of load address", align=Align.INLINE)
d.comment(0x8B50, "A=0", align=Align.INLINE)
d.comment(0x8B52, "Clear low byte of load address", align=Align.INLINE)
d.comment(0x8B54, "Clear carry for addition", align=Align.INLINE)
d.comment(0x8B55, "Y=&76: checksum range end", align=Align.INLINE)
d.label(0x8B57, "loop_sum_rom_bytes")

d.comment(0x8B57, "Add byte to running checksum", align=Align.INLINE)
d.comment(0x8B59, "Decrement index", align=Align.INLINE)
d.comment(0x8B5A, "Loop until all bytes summed", align=Align.INLINE)
d.comment(0x8B5C, "Y=&77: checksum storage offset", align=Align.INLINE)
d.comment(0x8B5E, "Compare with stored checksum", align=Align.INLINE)
d.comment(0x8B60, "Return -- last instruction of cmd_net_fs body", align=Align.INLINE)
d.comment(0x8B61, "A=&20: ADLC IRQ-status mask (CR2 bit 5)", align=Align.INLINE)
d.entry(0x8B61)

d.label(0x8B61, "cmd_net_check_hw")
d.comment(0x8B63, "Read ADLC CR2/SR2 (&FEA1)", align=Align.INLINE)
d.comment(0x8B66, "Z set (no carrier): proceed to FS-select", align=Align.INLINE)
d.comment(0x8B68, "A=3: 'ROM has no NFS' error code", align=Align.INLINE)
d.comment(0x8B6A, "Raise via build_simple_error (never returns)", align=Align.INLINE)
d.comment(0x8B6D, "Service 18 carries FS number in Y; Econet is FS 5", align=Align.INLINE)
d.entry(0x8B6D)


d.subroutine(
    0x8B6D,
    "svc_18_fs_select",
    title="Service 18: filing-system selection request",
    description="""Service-18 entry point.

| Condition | Action |
|---|---|
| `Y ≠ 5`   | return unclaimed (not the Econet FS) |
| Bit 7 of [`fs_flags`](label:fs_flags) set | return (FS already selected) |
| else | fall through to [`cmd_net_fs`](label:cmd_net_fs) for the full network-FS selection sequence |""",
    on_entry={"y": "filing system number requested"},
)
d.comment(0x8B6F, "Not us: pass the call on (RTS via shared return)", align=Align.INLINE)
d.comment(0x8B71, "A=0 to claim the service", align=Align.INLINE)
d.comment(0x8B73, "Clear svc_state and fall into ensure_fs_selected", align=Align.INLINE)
d.subroutine(
    0x8B75,
    "ensure_fs_selected",
    title="Ensure ANFS is the active filing system",
    description="""If bit 7 of `fs_flags` is set (ANFS already active), `RTS` via
`rts_save_text_ptr`. Otherwise calls `cmd_net_fs` to select
ANFS now; on failure, `JMP`s to
[`error_net_checksum`](label:error_net_checksum) to raise the `net checksum`
error. After successful selection, falls through to the body at
`&8B5A` which sets up the OSWORD parameter block pointer and
continues the caller's work.""",
    on_entry={"x, y": "OSWORD parameter block pointer (preserved across the cmd_net_fs call when selection happens)"},
)


d.comment(0x8B75, "Test fs_flags bit 7 (ANFS active)", align=Align.INLINE)
d.comment(0x8B78, "Already active: tail-RTS via shared exit", align=Align.INLINE)
d.comment(0x8B7A, "Auto-select ANFS via the *NFS handler", align=Align.INLINE)
d.subroutine(
    0x8B7A,
    "select_fs_via_cmd_net_fs",
    title="Force ANFS selection (raise net checksum on failure)",
    description="""Tail-fragment of [`ensure_fs_selected`](label:ensure_fs_selected) used directly
by `svc_3_autoboot` when an autoboot needs to force-select ANFS as
the active filing system. Calls `cmd_net_fs` to perform the actual
selection; on failure (`BEQ` not taken), `JMP`s to
[`error_net_checksum`](label:error_net_checksum) to raise the `net checksum`
error. Used when there is no clean `BIT fs_flags` / `BMI` shortcut
for early-return.""",
    on_entry={"x, y": "preserved across cmd_net_fs (as per the ensure_fs_selected calling contract)"},
    on_exit={"a": "current FS state byte if selection succeeded"},
)


d.comment(0x8B7D, "Z=1 (A=0): selection succeeded", align=Align.INLINE)
d.comment(0x8B7F, "Otherwise raise 'net checksum' error", align=Align.INLINE)
d.comment(0x8B82, "Read osword_pb_ptr_hi", align=Align.INLINE)
d.label(0x8B82, "select_fs_cmd_net_fs")

d.comment(0x8B84, "Push it", align=Align.INLINE)
d.comment(0x8B85, "Read osword_pb_ptr lo", align=Align.INLINE)
d.comment(0x8B87, "Push it", align=Align.INLINE)
d.label(0x8B88, "done_rom_checksum")

d.comment(0x8B88, "Call FSCV with A=6 (new FS)", align=Align.INLINE)
d.comment(0x8B8B, "Y=9: end of FS context block", align=Align.INLINE)
d.label(0x8B8D, "loop_copy_fs_ctx")

d.comment(0x8B8D, "Load byte from receive block", align=Align.INLINE)
d.comment(0x8B8F, "Store into FS workspace", align=Align.INLINE)
d.comment(0x8B92, "Decrement index", align=Align.INLINE)
d.comment(0x8B93, "Reached offset 1?", align=Align.INLINE)
d.comment(0x8B95, "No: continue copying", align=Align.INLINE)
d.comment(0x8B97, "Shift bit 7 of FS flags into carry", align=Align.INLINE)
d.comment(0x8B9A, "Clear carry", align=Align.INLINE)
d.comment(0x8B9B, "Clear bit 7 of FS flags", align=Align.INLINE)
d.comment(0x8B9E, "Y=&0D: vector table size - 1", align=Align.INLINE)
d.label(0x8BA0, "loop_set_vectors")

d.comment(0x8BA0, "Load FS vector address", align=Align.INLINE)
d.comment(0x8BA3, "Store into FILEV vector table", align=Align.INLINE)
d.comment(0x8BA6, "Decrement index", align=Align.INLINE)
d.comment(0x8BA7, "Loop until all vectors installed", align=Align.INLINE)
d.comment(0x8BA9, "Initialise ADLC and NMI workspace", align=Align.INLINE)
d.comment(0x8BAC, "Y=&1B: extended vector offset", align=Align.INLINE)
d.comment(0x8BAE, "X=7: two more vectors to set up", align=Align.INLINE)
d.comment(0x8BB0, "Set up extended vectors", align=Align.INLINE)
d.comment(0x8BB3, "A=0", align=Align.INLINE)
d.comment(0x8BB5, "Clear FS state byte", align=Align.INLINE)
d.comment(0x8BB8, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8BBB, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8BBE, "Clear receive attribute byte", align=Align.INLINE)
d.comment(0x8BC1, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8BC4, "Set up workspace pointers", align=Align.INLINE)
d.comment(0x8BC7, "Initialise FS state", align=Align.INLINE)
d.comment(0x8BCA, "Y=&77: workspace block size - 1", align=Align.INLINE)
d.label(0x8BCC, "loop_copy_ws_page")

d.comment(0x8BCC, "Load byte from source workspace", align=Align.INLINE)
d.comment(0x8BCE, "Store to the HAZEL &C2 FCB shadow copy", align=Align.INLINE)
d.comment(0x8BD1, "Decrement index", align=Align.INLINE)
d.comment(0x8BD2, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x8BD4, "A=&80: FS selected flag", align=Align.INLINE)
d.comment(0x8BD6, "Set bit 0 of fs_flags (= NFS active)", align=Align.INLINE)
d.comment(0x8BD9, "Issue Master service call &0F (vector update)", align=Align.INLINE)
d.comment(0x8BDC, "Pop saved osword_pb_ptr lo", align=Align.INLINE)
d.comment(0x8BDD, "Restore osword_pb_ptr lo", align=Align.INLINE)
d.comment(0x8BDF, "Pop saved osword_pb_ptr hi", align=Align.INLINE)
d.comment(0x8BE0, "Restore osword_pb_ptr hi", align=Align.INLINE)
d.comment(0x8BE2, "Return", align=Align.INLINE)
d.label(0x8BE3, "help_print_nfs_cmds")

d.subroutine(
    0x8BE3,
    "help_print_nfs_cmds",
    title="*HELP NFS topic: print NFS-specific commands",
    description="""Loads `X=&35` (the offset of the first NFS-specific command in
`cmd_table_fs`) and tail-falls into
[`print_cmd_table`](label:print_cmd_table) to emit the listing. Single
caller (the `*HELP` topic dispatch at `&8C70`).""",
    on_exit={"x": "&35 + advance through the table"},
)


d.comment(0x8BE3, "X=&35: NFS command table offset", align=Align.INLINE)
d.comment(0x8BE5, "Print help for NFS commands", align=Align.INLINE)
d.comment(0x8BE8, "X=0: utility command table offset", align=Align.INLINE)
d.entry(0x8BE8)

d.label(0x8BE8, "help_utils")


d.subroutine(
    0x8BE8,
    "help_utils",
    title="*HELP UTILS topic handler",
    description="""Sets `X = 0` to select the utility command sub-table and branches
to [`print_cmd_table`](label:print_cmd_table) to display the command
list. Prints the version header followed by all utility
commands.""",
    on_entry={"y": "command-line offset (PHA/PHA/RTS dispatch contract)"},
    on_exit={"a, x, y": "clobbered"},
)
d.comment(0x8BEC, "X=&35: NFS command table offset", align=Align.INLINE)
d.entry(0x8BEC)
d.label(0x8BEC, "help_net")

d.subroutine(
    0x8BEC,
    "help_net",
    title="*HELP NET topic handler",
    description="""Sets `X = &35` (the NFS command sub-table offset) and falls
through to [`print_cmd_table`](label:print_cmd_table) to display the
NFS command list with version header.""",
    on_entry={"y": "command-line offset (PHA/PHA/RTS dispatch contract)"},
    on_exit={"a, x, y": "clobbered (print_cmd_table)"},
)


d.label(0x8BEE, "print_cmd_table")

d.subroutine(
    0x8BEE,
    "print_cmd_table",
    title="Print *HELP command listing with optional header",
    description="""| `V` flag | Action |
|---|---|
| set   | save `X`/`Y`, call [`print_version_header`](label:print_version_header) to show the ROM version string and station number, restore `X`/`Y` |
| clear | output a newline only |

Either path then falls through to
[`print_cmd_table`](label:print_cmd_table) to enumerate
commands.""",
    on_entry={"x": "offset into cmd_table_fs", "v": "set=print version header, clear=newline only"},
)


d.comment(0x8BEE, "V clear: take newline-only path (skip version header)", align=Align.INLINE)
d.comment(0x8BF0, "Save X (cmd-table offset)", align=Align.INLINE)
d.comment(0x8BF1, "Save Y (text-pointer offset)", align=Align.INLINE)
d.comment(0x8BF2, "Print the version-banner header", align=Align.INLINE)
d.comment(0x8BF7, "Clear overflow flag", align=Align.INLINE)
d.label(0x8BFA, "print_table_newline")

# UNMAPPED: d.label(0x8BD5, "print_cmd_table_loop")

# UNMAPPED: d.subroutine(
# UNMAPPED:     0x8BD5,
# UNMAPPED:     "print_cmd_table_loop",
# UNMAPPED:     title="Enumerate and print command table entries",
# UNMAPPED:     description="""Walks the ANFS command table from offset `X`, printing each
# UNMAPPED: command name padded to 9 characters followed by its syntax
# UNMAPPED: description.
# UNMAPPED: 
# UNMAPPED: | Entry byte bit 7 | Treatment |
# UNMAPPED: |---|---|
# UNMAPPED: | clear | print this entry |
# UNMAPPED: | set   | mark end-of-table |
# UNMAPPED: 
# UNMAPPED: The syntax descriptor byte's low 5 bits index into
# UNMAPPED: `cmd_syntax_table`; index `&0E` triggers special handling that
# UNMAPPED: lists shared command names in parentheses. Calls
# UNMAPPED: [`help_wrap_if_serial`](label:help_wrap_if_serial) to handle line
# UNMAPPED: continuation on serial output streams. Preserves `Y`.""",
# UNMAPPED:     on_entry={"x": "offset into cmd_table_fs"},
# UNMAPPED: )


# UNMAPPED: d.comment(0x8BD5, "Save Y (command line offset)", align=Align.INLINE)
# UNMAPPED: d.comment(0x8BD6, "Push it", align=Align.INLINE)
d.comment(0x8BFE, "Save processor status", align=Align.INLINE)
d.label(0x8BFF, "loop_next_entry")

d.subroutine(
    0x8BFF,
    "loop_next_entry",
    title="*HELP table walker per-entry body",
    description="""Loads `cmd_table_fs,X` (entry byte at offset `X`):

| Bit 7 | Target |
|---|---|
| clear | `print_indent` (continue with this entry) |
| set   | `JMP done_print_table` (end of table reached) |

Single caller (the `BNE` retry at `&8C47` in
[`print_cmd_table`](label:print_cmd_table)'s outer loop).""",
    on_entry={"x": "current cmd_table_fs offset"},
)


d.comment(0x8BFF, "Load byte from command table", align=Align.INLINE)
d.comment(0x8C02, "Bit 7 clear: valid entry, continue", align=Align.INLINE)
d.comment(0x8C04, "End of table: finish up", align=Align.INLINE)
d.label(0x8C07, "print_indent")

d.comment(0x8C07, "Print two-space indent", align=Align.INLINE)
d.comment(0x8C0C, "Y=9: cmd_table_fs sub-table 1 offset", align=Align.INLINE)
d.comment(0x8C0E, "Read cmd_table_fs+X (entry name byte)", align=Align.INLINE)
# UNMAPPED: d.comment(0x8BE7, "Read cmd_table_fs+X (entry name byte)", align=Align.INLINE)
d.label(0x8C11, "loop_print_cmd_name")


d.comment(0x8C14, "Advance table pointer", align=Align.INLINE)
d.comment(0x8C15, "Decrement padding counter", align=Align.INLINE)
d.comment(0x8C16, "Load next character", align=Align.INLINE)
d.comment(0x8C19, "Bit 7 clear: more chars, continue", align=Align.INLINE)
d.label(0x8C1B, "loop_pad_spaces")

d.comment(0x8C1B, "Pad with spaces", align=Align.INLINE)
d.comment(0x8C20, "Decrement remaining pad count", align=Align.INLINE)
d.comment(0x8C21, "More padding needed: loop", align=Align.INLINE)
d.comment(0x8C23, "Load syntax descriptor byte", align=Align.INLINE)
d.comment(0x8C26, "Mask to get syntax string index", align=Align.INLINE)
d.comment(0x8C28, "Use index as Y", align=Align.INLINE)
d.comment(0x8C29, "Look up syntax string offset", align=Align.INLINE)
d.comment(0x8C2C, "Transfer offset to Y", align=Align.INLINE)
d.label(0x8C2D, "loop_print_syntax")

d.subroutine(
    0x8C2D,
    "loop_print_syntax",
    title="Per-character body of *HELP syntax string emit",
    description="""`INY` / load `syn_opt_dir,Y` / detect terminator or
line-break:

| Byte | Action |
|---|---|
| `0`  | terminator – stop |
| `CR` (`&0D`) | line-break – wrap |
| other | print the character |

Two callers: the `BNE` at `&8C15` (continue with current char)
and the `BEQ` at `&8C19` (fall-through from the line-wrap
path).""",
    on_entry={"y": "current index into syn_opt_dir"},
)


d.comment(0x8C2D, "Advance to next character", align=Align.INLINE)
d.comment(0x8C2E, "Load syntax string character", align=Align.INLINE)
d.comment(0x8C31, "Zero terminator: end of syntax", align=Align.INLINE)
d.comment(0x8C33, "Carriage return: line continuation", align=Align.INLINE)
d.comment(0x8C35, "No: print the character", align=Align.INLINE)
d.comment(0x8C37, "Handle line wrap in syntax output", align=Align.INLINE)
d.comment(0x8C3A, "Continue with next character", align=Align.INLINE)
d.label(0x8C3D, "print_syntax_char")

d.comment(0x8C40, "Continue with next character", align=Align.INLINE)
d.label(0x8C43, "done_entry_newline")

d.comment(0x8C46, "X += 3: skip syntax descriptor and address", align=Align.INLINE)
d.comment(0x8C47, "(continued)", align=Align.INLINE)
d.comment(0x8C48, "(continued)", align=Align.INLINE)
d.comment(0x8C49, "Loop for next command", align=Align.INLINE)
d.label(0x8C4C, "done_print_table")

d.subroutine(
    0x8C4C,
    "done_print_table",
    title="Cleanup epilogue for print_cmd_table",
    description="""Pops the saved `P` and `Y` registers off the stack and `RTS`.
Used as the shared exit for [`print_cmd_table`](label:print_cmd_table)
after it has emitted a help listing or detected end-of-table.
Single caller (the `BEQ` at `&8BDD` in
[`print_cmd_table`](label:print_cmd_table) when `V` was set on entry,
indicating the saved state needs restoring).""",
    on_exit={"y": "restored from stack", "p (flags)": "restored from stack"},
)


d.comment(0x8C4C, "Restore processor status", align=Align.INLINE)
d.comment(0x8C4D, "Restore Y", align=Align.INLINE)
d.comment(0x8C4E, "Transfer to Y", align=Align.INLINE)
d.comment(0x8C4F, "Return", align=Align.INLINE)
d.label(0x8C50, "help_wrap_if_serial")

d.subroutine(
    0x8C50,
    "help_wrap_if_serial",
    title="Wrap *HELP syntax lines for serial output",
    description="""Checks the output destination via [`vdu_mode`](label:vdu_mode):

| Stream | Action |
|---|---|
| 0 (VDU) | return immediately |
| 3 (printer) | return immediately |
| serial | output newline + 12 spaces of indentation to align continuation lines with the syntax-description column |""",
    on_exit={"y": "preserved (saved/restored via PHY/PLY)", "a": "clobbered (last char written via OSWRCH)"},
)


d.comment(0x8C50, "Read output stream type", align=Align.INLINE)
d.entry(0x8C50)
d.comment(0x8C53, "Stream 0 (VDU): no wrapping", align=Align.INLINE)
d.comment(0x8C55, "Stream 3 (printer)?", align=Align.INLINE)
d.comment(0x8C57, "Yes: no wrapping", align=Align.INLINE)
d.comment(0x8C59, "Save Y across OS call", align=Align.INLINE)
d.comment(0x8C5D, "Y=&0B: indent width - 1", align=Align.INLINE)
d.comment(0x8C5F, "Space character", align=Align.INLINE)
d.label(0x8C61, "loop_indent_spaces")

d.comment(0x8C64, "Decrement indent counter", align=Align.INLINE)
d.comment(0x8C65, "More spaces needed: loop", align=Align.INLINE)
d.label(0x8C68, "rts_help_wrap")

d.comment(0x8C68, "Return", align=Align.INLINE)
d.comment(0x8C69, "X=0: start of utility command table", align=Align.INLINE)
d.entry(0x8C69)
d.label(0x8C69, "svc_4_star_command")

d.subroutine(
    0x8C69,
    "svc_4_star_command",
    title="Service 4: unrecognised star command",
    description="""Saves the OS text pointer, then calls match_fs_cmd
to search the command table starting at offset 0
(all command sub-tables). If no match is found (carry
set), returns with the service call unclaimed. On
a match, JMPs to cmd_fs_reentry to execute the
matched command handler via the PHA/PHA/RTS
dispatch mechanism.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0x8C6B, "Get command line offset", align=Align.INLINE)
d.label(0x8C6D, "svc4_dispatch_lookup")

d.comment(0x8C6D, "Save text pointer to fs_crc", align=Align.INLINE)
d.comment(0x8C70, "Try to match command in table", align=Align.INLINE)
d.comment(0x8C73, "No match: return to caller", align=Align.INLINE)
d.comment(0x8C75, "Match found: execute command", align=Align.INLINE)
d.comment(0x8C78, "Check for credits Easter egg", align=Align.INLINE)
d.entry(0x8C78)
d.label(0x8C78, "svc_9_help")

d.subroutine(
    0x8C78,
    "svc_9_help",
    title="Service 9: *HELP",
    description="""Handles MOS service call 9 (*HELP). First checks
for the credits Easter egg. For bare *HELP (CR
at text pointer), prints the version header and
full command list starting at table offset &91.
For *HELP with an argument, handles '.' as a
shortcut to list all NFS commands, otherwise
iterates through help topics using PHA/PHA/RTS
dispatch to print matching command groups.
Returns with Y = ws_page (unclaimed).""",
    on_entry={"a": "9 (service call number)", "y": "command-line offset of *HELP argument"},
    on_exit={"y": "ws_page (workspace page) -- the service call is left UNCLAIMED so MOS continues to the next ROM"},
)
d.comment(0x8C7B, "Get command line offset", align=Align.INLINE)
d.comment(0x8C7D, "Load character at offset", align=Align.INLINE)
d.comment(0x8C7F, "Is it CR (bare *HELP)?", align=Align.INLINE)
d.comment(0x8C81, "No: check for specific topic", align=Align.INLINE)
d.comment(0x8C83, "Print version string", align=Align.INLINE)
d.comment(0x8C86, "X=&91: start of help command list", align=Align.INLINE)
d.comment(0x8C88, "Print command list from table", align=Align.INLINE)
d.label(0x8C8B, "svc_return_unclaimed")

d.subroutine(
    0x8C8B,
    "svc_return_unclaimed",
    title="Restore Y and return service-call unclaimed",
    description="""Reloads `Y` from `ws_page` (the saved command-line offset) and
`RTS` to the caller without clearing `A` – preserving the
original service number so the next ROM in the chain sees the
unclaimed call.

Reached from the four service-handler escape paths at `&8C4C`,
`&8C91`, `&8CFA`, and `&95BF` that hand a request back to MOS
without acting on it.""",
    on_exit={"y": "ws_page (restored command-line offset)"},
)


d.comment(0x8C8B, "Restore Y (command line offset)", align=Align.INLINE)
d.comment(0x8C8D, "Return unclaimed", align=Align.INLINE)
d.label(0x8C8E, "check_help_topic")

d.comment(0x8C8E, "Test for topic match (sets flags)", align=Align.INLINE)
d.comment(0x8C91, "Is first char '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8C93, "No: try topic-specific help", align=Align.INLINE)
d.comment(0x8C95, "'.' found: show full command list", align=Align.INLINE)
d.label(0x8C98, "match_help_topic")

d.comment(0x8C98, "Save text pointer to fs_crc", align=Align.INLINE)
d.label(0x8C9B, "loop_dispatch_help")

d.comment(0x8C9B, "Save flags", align=Align.INLINE)
d.comment(0x8C9C, "X=&96: help command table start", align=Align.INLINE)
d.comment(0x8C9E, "Try to match help topic in table", align=Align.INLINE)
d.comment(0x8CA1, "No match: try next topic", align=Align.INLINE)
d.comment(0x8CA3, "Restore flags", align=Align.INLINE)
d.comment(0x8CA4, "Push return address high (&8C)", align=Align.INLINE)
d.comment(0x8CA6, "Push it for RTS dispatch", align=Align.INLINE)
d.comment(0x8CA7, "Push return address low (&74)", align=Align.INLINE)
d.comment(0x8CA9, "Push it for RTS dispatch", align=Align.INLINE)
d.comment(0x8CAA, "Load dispatch address high", align=Align.INLINE)
d.comment(0x8CAD, "Push dispatch high for RTS", align=Align.INLINE)
d.comment(0x8CAE, "Load dispatch address low", align=Align.INLINE)
d.comment(0x8CB1, "Push dispatch low for RTS", align=Align.INLINE)
d.comment(0x8CB2, "Dispatch via RTS (returns to &8CA7)", align=Align.INLINE)
d.label(0x8CB3, "skip_if_no_match")

d.comment(0x8CB3, "Restore flags from before match", align=Align.INLINE)
d.comment(0x8CB4, "End of command line?", align=Align.INLINE)
d.comment(0x8CB6, "No: try matching next topic", align=Align.INLINE)
d.label(0x8CBA, "print_version_header")

d.subroutine(
    0x8CBA,
    "print_version_header",
    title="Print ANFS version string and station number",
    description="""Uses an inline string after `JSR` to
[`print_inline`](label:print_inline): `CR + "Advanced NFS 4.26" +
CR`. After the inline string, `JMP`s to
[`print_station_id`](label:print_station_id) to append the local Econet
station number.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered (print_inline + print_station_id)"},
)


d.comment(0x8CBA, "Print version string via inline", align=Align.INLINE)
d.label(0x8CBD, "version_string_cr")

d.comment(0x8CD0, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0x8CD1, "Tail-call print_station_id to append ' Econet Station <n>' (and ' No Clock' if appropriate)", align=Align.INLINE)
# UNMAPPED: d.comment(
# UNMAPPED:     0x8CAA,
# UNMAPPED:     "Tail-call print_station_id to append ' Econet Station <n>' (and ' No Clock' if appropriate)",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
d.subroutine(
    0x8CD4,
    "get_ws_page",
    title="Read workspace page number for current ROM slot",
    description="""Indexes into the MOS per-ROM workspace table
[`rom_ws_pages`](label:rom_ws_pages) using `romsel_copy` (`&F4`) as
the ROM slot. Holds a copy of the slot byte in `Y`, then runs a
`ROL` / `PHP` / `ROR` / `PLP` sequence at `&8CDA`–`&8CB6` that
restores `A` to the original byte while leaving the saved-flags
register reflecting bit 6 of the original byte (the ADLC-absent
flag). Falls through to whichever caller-specific tail follows.""",
    on_exit={
        "a": "workspace page byte (preserved through ROL/ROR)",
        "y": "same byte (set by `TAY` before the rotate trick)",
        "n": "set to bit 6 of the original byte (ADLC-absent flag)",
    },
)


d.comment(0x8CD4, "Y = current ROM slot number from MOS copy at &F4", align=Align.INLINE)
d.comment(0x8CD6, "Load workspace page byte for this ROM slot", align=Align.INLINE)
d.comment(0x8CD9, "Hold a copy of the slot byte in Y while we test bit 6", align=Align.INLINE)
d.comment(0x8CDA, "ROL puts pre-ROL bit 6 into the post-ROL N flag (and pre-ROL bit 7 into C)", align=Align.INLINE)
d.comment(0x8CDB, "Save those flags so the upcoming ROR doesn't lose N", align=Align.INLINE)
d.comment(0x8CDC, "ROR restores A to its original value (using the saved C)", align=Align.INLINE)
d.comment(0x8CDD, "Restore the ROL flags: N is now pre-ROL bit 6", align=Align.INLINE)
d.comment(0x8CDE, "Bit 6 clear: skip the OR (no ADLC-absent flag)", align=Align.INLINE)
d.comment(
    0x8CE0,
    "Bit 6 set: re-set bit 7 in the returned page byte (the ADLC-absent flag uses bit 7 in callers)",
    align=Align.INLINE,
)
d.label(0x8CE2, "get_ws_page_loop")

d.comment(0x8CE2, "Transfer to Y", align=Align.INLINE)
d.comment(0x8CE3, "Return with page in A and Y", align=Align.INLINE)
d.label(0x8CE4, "setup_ws_ptr")

d.subroutine(
    0x8CE4,
    "setup_ws_ptr",
    title="Set up zero-page pointer to workspace page",
    description="""Calls [`get_ws_page`](label:get_ws_page) to read the page number,
stores it as the high byte in `nfs_temp` (`&CD`), and clears the
low byte at `&CC` to zero. This gives a page-aligned pointer used
by FS initialisation and [`cmd_net_fs`](label:cmd_net_fs) to
access the private workspace.""",
    on_exit={"a": "0", "y": "workspace page number"},
)


d.comment(0x8CE4, "Get workspace page for ROM slot", align=Align.INLINE)
d.comment(0x8CE7, "Store page in nfs_temp", align=Align.INLINE)
d.comment(0x8CE9, "A=0", align=Align.INLINE)
d.comment(0x8CEB, "Clear low byte of pointer", align=Align.INLINE)
d.label(0x8CED, "rts_setup_ws_ptr")

d.comment(0x8CED, "Return", align=Align.INLINE)
d.comment(0x8CEE, "OSBYTE &7A: scan keyboard from key 16", align=Align.INLINE)
d.entry(0x8CEE)
d.label(0x8CEE, "svc_3_autoboot")

d.subroutine(
    0x8CEE,
    "svc_3_autoboot",
    title="Service 3: auto-boot on reset",
    description="""Scans the keyboard via OSBYTE &7A for the 'N' key
(&19 or &55 EOR'd with &55). If pressed, records
the key state via OSBYTE &78. Selects the network
filing system by calling cmd_net_fs, prints the
station ID, then checks if this is the first boot
(ws_page = 0). If so, sets the auto-boot flag in
&1071 and JMPs to cmd_fs_entry to execute the boot
file.""",
    on_entry={"a": "3 (service call number)", "x": "ROM slot", "y": "parameter (service-call dispatch)"},
)


d.comment(0x8CF4, "No key pressed: select Net FS", align=Align.INLINE)
d.comment(0x8CF6, "Key &19 (N)?", align=Align.INLINE)
d.comment(0x8CF8, "Yes: write key state and boot", align=Align.INLINE)
d.comment(0x8CFA, "EOR with &55: maps to zero if 'N'", align=Align.INLINE)
d.comment(0x8CFC, "Not N key: return unclaimed", align=Align.INLINE)
d.label(0x8CFE, "write_key_state")

d.comment(0x8CFF, "OSBYTE &78: write keys pressed", align=Align.INLINE)
d.label(0x8D04, "select_net_fs")

d.comment(0x8D04, "Select NFS as current filing system", align=Align.INLINE)
d.comment(0x8D0D, "A=0: clear svc_state marker", align=Align.INLINE)
d.comment(0x8D0F, "Store -> svc_state", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CE4, "Print station number", align=Align.INLINE)
d.comment(0x8D11, "Get workspace page", align=Align.INLINE)
d.comment(0x8D13, "Non-zero: already initialised, return", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CEE, "Load boot flags", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CF1, "Set bit 2 (auto-boot in progress)", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CF3, "Store updated boot flags", align=Align.INLINE)
d.comment(0x8D1A, "X=&40: boot filename address low", align=Align.INLINE)
d.comment(0x8D1C, "Y=&8D: boot filename address high", align=Align.INLINE)
d.comment(0x8D1E, "Execute boot file", align=Align.INLINE)
d.label(0x8D21, "notify_new_fs")

d.subroutine(
    0x8D21,
    "notify_new_fs",
    title="Notify OS of filing-system selection",
    description="""Loads `A=6` (FSCV reason: filing system change) and falls
through to [`call_fscv`](label:call_fscv), which `JMP`-indirects
through `vec_fscv` to invoke the FSCV vector. The FSCV handler
returns to whatever invoked `notify_new_fs` -- this is a
fire-and-forget notification, not a return-to-caller call.

Single caller (&8B88 inside the FS-selection sequence).""",
    on_entry={},
    on_exit={"a": "6 (clobbered by FSCV handler)"},
)


d.comment(0x8D21, "A=6: notify new filing system", align=Align.INLINE)
d.label(0x8D23, "call_fscv")

d.subroutine(
    0x8D23,
    "call_fscv",
    title="Dispatch to filing-system control vector (FSCV)",
    description="""Indirect `JMP` through `FSCV` at [`vec_fscv`](label:vec_fscv),
providing OS-level filing-system services such as FS-selection
notification (`A=6`) and `*RUN` handling.

Also contains [`issue_svc_15`](label:issue_svc_15) and
`issue_svc_osbyte` entry points that issue paged-ROM service
requests via OSBYTE `&8F`.""",
    on_entry={"a": "FSCV reason code"},
)


d.comment(0x8D23, "Tail-jump via FSCV vector (filing-system change service)", align=Align.INLINE)
d.label(0x8D26, "issue_svc_15")

d.comment(0x8D26, "X=&0F: service 15 (vectors claimed)", align=Align.INLINE)
d.subroutine(
    0x8D26,
    "issue_svc_15",
    title="Issue OSBYTE 143 service 15 (vectors-claimed) request",
    description="Tail-call wrapper that loads X=&0F (service number 15) and tail-jumps to OSBYTE 143 (issue paged ROM service request), which broadcasts service 15 to all sideways ROMs. ANFS calls this from svc_2_private_workspace after claiming its workspace, to give other ROMs a chance to react.",
    on_entry={"a": "OSBYTE result is irrelevant -- this is fire-and-forget"},
)


d.label(0x8D28, "issue_svc_osbyte")

d.comment(0x8D28, "A=&8F: OSBYTE 'Issue paged-ROM service request'", align=Align.INLINE)
d.subroutine(
    0x8D2D,
    "svc_dispatch_idx_2",
    title="svc_dispatch table[2] handler",
    description="""Reached only via PHA/PHA/RTS dispatch from the
[`svc_dispatch_lo`](label:svc_dispatch_lo) table at index 2. Pushes `Y`
onto the stack via `PHY`, sets `X=&11` (CMOS RAM offset for the
Econet station-flags byte), calls [`osbyte_a1`](label:osbyte_a1) to
read it, then ANDs the result with `&01` (bit 0 = "use page &0B
fallback") and pulls `Y` back. Used by the workspace-allocation
path to discover whether the user has overridden the default
private workspace base.""",
    on_exit={"a": "0 or 1 (CMOS bit 0 of station-flags byte)"},
)


d.entry(0x8D2D)
d.comment(0x8D2D, "Save Y on stack", align=Align.INLINE)
d.comment(0x8D2E, "X=&11: CMOS offset for Econet station-flags", align=Align.INLINE)
d.comment(0x8D30, "Read CMOS byte: result in Y", align=Align.INLINE)
d.comment(0x8D33, "A = CMOS byte", align=Align.INLINE)
d.comment(0x8D34, "Restore caller's Y", align=Align.INLINE)
d.comment(0x8D35, "Isolate bit 0 (page-&0B fallback flag)", align=Align.INLINE)
d.comment(0x8D37, "Bit clear: keep caller's Y", align=Align.INLINE)
d.comment(0x8D39, "Caller's Y already >= &10?", align=Align.INLINE)
d.comment(0x8D3B, "Yes: keep it", align=Align.INLINE)
d.comment(0x8D3D, "Y < &10 with bit set: clamp to &10", align=Align.INLINE)
d.comment(0x8D3F, "Return", align=Align.INLINE)
d.subroutine(
    0x8D48,
    "check_credits_easter_egg",
    title="Easter egg: match *HELP keyword to author credits",
    description="""Matches the `*HELP` argument against a keyword embedded in the
credits data at `credits_keyword_start`. Starts matching from
offset 5 in the data (`X=5`) and checks each byte against the
command-line text until a mismatch or `X` reaches `&0D`.

On a full match, prints the ANFS author credits:

- B Cockburn
- J Dunn
- B Robertson
- J Wills

Each name is terminated by `CR`.""",
)


d.comment(0x8D48, "Y = ws_page (workspace high page)", align=Align.INLINE)
d.comment(0x8D4A, "X=5: start of credits keyword", align=Align.INLINE)
d.label(0x8D4C, "loop_match_credits")

d.comment(0x8D4C, "Load character from command line", align=Align.INLINE)
d.comment(0x8D4E, "Compare with credits keyword", align=Align.INLINE)
d.comment(0x8D51, "Mismatch: check if keyword complete", align=Align.INLINE)
d.comment(0x8D53, "Advance command line pointer", align=Align.INLINE)
d.comment(0x8D54, "Advance keyword pointer", align=Align.INLINE)
d.comment(0x8D55, "Continue matching", align=Align.INLINE)
d.label(0x8D57, "done_credits_check")

d.comment(0x8D57, "Reached end of keyword (X=&0C)?", align=Align.INLINE)
d.comment(0x8D59, "No: keyword not fully matched, return", align=Align.INLINE)
d.comment(0x8D5B, "Print the credits string inline (high-bit terminated)", align=Align.INLINE)

# The credits string is emitted by print_inline (high-bit terminated),
# not by the manual emit loop the earlier ANFS versions used. The bytes
# at &8D5C..&8D9C are the inline string, consumed by the print_inline
# hook; the &EA (NOP) terminator at &8D9D doubles as the resume opcode
# and falls through to the RTS at &8D9E. The same string doubles as the
# keyword matched by the CMP loop above (credits_keyword_start).
d.index_base(0x8D5E, "credits_keyword_start")

d.label(0x8DA0, "rts_credits_check")
d.comment(0x8DA0, "Return", align=Align.INLINE)

d.comment(0x8DA1, "Save caller Y", align=Align.INLINE)
d.entry(0x8DA1)

d.label(0x8DA1, "cmd_iam_save_ctx")
d.comment(0x8DA2, "Read fs_last_byte_flag (work_bd)", align=Align.INLINE)
d.comment(0x8DA4, "Read fs_options (work_bb)", align=Align.INLINE)
d.comment(0x8DA6, "Read fs_block_offset (work_bc)", align=Align.INLINE)
d.comment(0x8DA8, "Push fs_last_byte_flag for restore on return", align=Align.INLINE)
d.comment(0x8DAB, "OSBYTE &77: close SPOOL/EXEC", align=Align.INLINE)
d.entry(0x8DAB)


d.subroutine(
    0x8DAB,
    "cmd_iam",
    title="*I AM command handler (file server logon)",
    description="""Closes any *SPOOL/*EXEC files via OSBYTE &77,
resets all file control blocks via
process_all_fcbs, then parses the command line
for an optional station number and file server
address. If a station number is present, stores
it and calls clear_if_station_match to validate.
Copies the logon command template from
cmd_table_nfs_iam into the transmit buffer and
sends via copy_arg_validated. Falls through to
cmd_pass for password entry.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0x8DAD, "Store as pending operation marker", align=Align.INLINE)
d.comment(0x8DB3, "Y=0", align=Align.INLINE)
d.comment(0x8DB5, "Clear password entry flag", align=Align.INLINE)
d.comment(0x8DB7, "Reset FS connection state", align=Align.INLINE)
d.comment(0x8DBA, "Clear hazel_fs_pending_state (connection-attempt flag)", align=Align.INLINE)
d.comment(0x8DBF, "Pop and discard saved fs_last_byte_flag", align=Align.INLINE)
d.comment(0x8DC0, "Set up transfer parameters", align=Align.INLINE)
d.subroutine(
    0x8DC0,
    "load_transfer_params",
    title="Set FS transfer parameters via set_xfer_params",
    description="""3-byte trampoline that calls
[`set_xfer_params`](label:set_xfer_params) and falls through into
[`cmd_pass`](label:cmd_pass)'s argument-parse prologue. Reached
from `init_txcb_and_load_xfer` at `&B3DB` to install the FS
transfer context (byte count + source pointer in `fs_last_byte_flag`
/ `fs_crc_lo`/`hi`) before continuing into the *I am / *Pass
station-and-credential parser.""",
)

# UNMAPPED: d.label(0x8DA7, "ps_template_base")

d.comment(0x8DC4, "Load first option byte", align=Align.INLINE)
d.comment(0x8DC6, "Parse station number if present", align=Align.INLINE)
d.comment(0x8DC9, "Not a digit: skip to password entry", align=Align.INLINE)
d.comment(0x8DCB, "Parse user ID string", align=Align.INLINE)
d.comment(0x8DCE, "No user ID: go to password", align=Align.INLINE)
d.comment(0x8DD0, "Store file server station low", align=Align.INLINE)
d.comment(0x8DD3, "Check and store FS network", align=Align.INLINE)
d.comment(0x8DD6, "Skip separator", align=Align.INLINE)
d.comment(0x8DD7, "Parse next argument", align=Align.INLINE)
d.label(0x8DDA, "skip_no_fs_addr")

d.comment(0x8DDA, "No FS address: skip to password", align=Align.INLINE)
d.comment(0x8DDC, "Store file server station high", align=Align.INLINE)
d.comment(0x8DDF, "X=&FF: pre-decrement for loop", align=Align.INLINE)
d.label(0x8DE1, "loop_copy_logon_cmd")

d.comment(0x8DE1, "Advance index", align=Align.INLINE)
d.comment(0x8DE2, "Load logon command template byte", align=Align.INLINE)
d.comment(0x8DE5, "Store into transmit buffer", align=Align.INLINE)
d.comment(0x8DE8, "Bit 7 clear: more bytes, loop", align=Align.INLINE)
d.comment(0x8DEA, "Send logon with file server lookup", align=Align.INLINE)
d.comment(0x8DED, "Success: skip to password entry", align=Align.INLINE)
d.comment(0x8DEF, "Build FS command packet", align=Align.INLINE)
d.entry(0x8DEF)
d.label(0x8DEF, "cmd_pass")

d.subroutine(
    0x8DEF,
    "cmd_pass",
    title="*PASS command handler (change password)",
    description="""Builds the FS command packet via copy_arg_to_buf_x0,
then scans the reply buffer for a ':' separator
indicating a password prompt. If found, reads
characters from the keyboard without echo, handling
Delete (&7F) for backspace and NAK (&15) to restart
from the colon position. Sends the completed
password to the file server via save_net_tx_cb and
branches to send_cmd_and_dispatch for the reply.""",
    on_entry={"y": "command line offset in text pointer (also the entry point for cmd_iam fall-through)"},
)


d.label(0x8DF2, "scan_pass_prompt")

d.comment(0x8DF2, "Y=&FF: pre-increment for loop", align=Align.INLINE)
d.label(0x8DF4, "loop_scan_colon")

d.comment(0x8DF4, "Advance to next byte", align=Align.INLINE)
d.comment(0x8DF5, "Load byte from reply buffer", align=Align.INLINE)
d.comment(0x8DF8, "Is it CR (end of prompt)?", align=Align.INLINE)
d.comment(0x8DFA, "Yes: no colon found, skip to send", align=Align.INLINE)
d.comment(0x8DFC, "Is it ':' (password prompt)?", align=Align.INLINE)
d.comment(0x8DFE, "No: keep scanning", align=Align.INLINE)
d.comment(0x8E00, "Print byte no-spool", align=Align.INLINE)
d.comment(0x8E03, "Save position of colon", align=Align.INLINE)
d.label(0x8E05, "read_pw_char")

d.comment(0x8E05, "A=&FF: mark as escapable", align=Align.INLINE)
d.comment(0x8E07, "Set escape flag", align=Align.INLINE)
d.comment(0x8E09, "Check for escape condition", align=Align.INLINE)
d.comment(0x8E11, "Not NAK (&15): check other chars", align=Align.INLINE)
d.comment(0x8E13, "Restore colon position", align=Align.INLINE)
d.comment(0x8E15, "Non-zero: restart from colon", align=Align.INLINE)
d.label(0x8E17, "loop_erase_pw")

d.comment(0x8E17, "At colon position?", align=Align.INLINE)
d.comment(0x8E19, "Yes: restart password input", align=Align.INLINE)
d.comment(0x8E1B, "Backspace: move back one character", align=Align.INLINE)
d.comment(0x8E1C, "If not at start: restart input", align=Align.INLINE)
d.label(0x8E1E, "check_pw_special")

d.comment(0x8E1E, "Delete key (&7F)?", align=Align.INLINE)
d.comment(0x8E20, "Yes: handle backspace", align=Align.INLINE)
d.comment(0x8E22, "Store character in password buffer", align=Align.INLINE)
d.comment(0x8E25, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x8E26, "Is it CR (end of password)?", align=Align.INLINE)
d.comment(0x8E28, "No: read another character", align=Align.INLINE)
d.comment(0x8E2A, "Print newline no-spool", align=Align.INLINE)
d.label(0x8E2D, "send_pass_to_fs")

d.comment(0x8E2D, "Transfer string length to A", align=Align.INLINE)
d.comment(0x8E2E, "Save string length", align=Align.INLINE)
d.comment(0x8E2F, "Set up transmit control block", align=Align.INLINE)
d.comment(0x8E32, "Send to file server and get reply", align=Align.INLINE)
d.comment(0x8E36, "Include terminator", align=Align.INLINE)
d.comment(0x8E37, "Y=0", align=Align.INLINE)
d.label(0x8E3B, "clear_if_station_match")

d.subroutine(
    0x8E3B,
    "clear_if_station_match",
    title="Clear hazel_fs_network if it matches the bridge status byte",
    description="""Calls [`init_bridge_poll`](label:init_bridge_poll) (returning the
[`spool_control_flag`](label:spool_control_flag) bridge status byte in `A`,
either freshly populated or already cached from a previous
invocation) and EORs it with
[`hazel_fs_network`](label:hazel_fs_network). When the two match (`EOR`
result is zero), zeroes `hazel_fs_network` so subsequent FS
operations fall back to the local network.

Called by [`cmd_iam`](label:cmd_iam) and
[`osword_13_set_station`](label:osword_13_set_station) when reconciling a
parsed file-server station address against the bridge state.""",
    on_exit={"a": "0 if cleared (match), bridge-XOR-network otherwise"},
)


d.comment(0x8E3B, "Ensure bridge initialised; A=spool_control_flag (bridge status)", align=Align.INLINE)
d.comment(0x8E3E, "EOR with hazel_fs_network: zero result if equal", align=Align.INLINE)
d.comment(0x8E41, "Different: return without clearing", align=Align.INLINE)
d.comment(0x8E43, "Same: clear station byte", align=Align.INLINE)
d.label(0x8E46, "rts_station_match")

d.comment(0x8E46, "Return", align=Align.INLINE)
d.subroutine(
    0x8E47,
    "check_urd_prefix",
    title="Branch to *RUN handler if first arg char is '&'",
    description="""Reads the first character of the parsed command text via
`(fs_crc_lo),Y`:

| First char | Path |
|---|---|
| `'&'` (URD prefix marker) | `JMP cmd_run_via_urd` |
| any other | fall through to `pass_send_cmd` (send as normal FS request) |

Single caller (the FS command-name post-match path at
`&959E`).""",
)


d.comment(0x8E47, "Y=0: first character offset", align=Align.INLINE)
d.comment(0x8E49, "Load first character of command text", align=Align.INLINE)
d.comment(0x8E4B, "Is it '&' (URD prefix)?", align=Align.INLINE)
d.comment(0x8E4D, "No: send as normal FS command", align=Align.INLINE)
d.comment(0x8E4F, "Yes: route via *RUN for URD prefix handling", align=Align.INLINE)
d.label(0x8E52, "pass_send_cmd")

d.comment(0x8E52, "Build FS command packet", align=Align.INLINE)
d.comment(0x8E55, "Transfer result to Y", align=Align.INLINE)
d.label(0x8E56, "send_cmd_and_dispatch")

d.subroutine(
    0x8E56,
    "send_cmd_and_dispatch",
    title="Send FS command and dispatch the reply",
    description="""1. `JSR save_net_tx_cb` to set up and transmit the command.
2. Read the reply function code from
   [`hazel_txcb_network`](label:hazel_txcb_network).

| Reply code | Action |
|---|---|
| `0`     | branch to the no-reply path (`dispatch_rts`) |
| non-zero | load [`hazel_txcb_data`](label:hazel_txcb_data) (first reply byte), `Y=&25` (dispatch offset for the standard reply table), continue into the reply-dispatch chain |

Two callers: the fall-through from
[`check_urd_prefix`](label:check_urd_prefix) (`&8E37` via
`pass_send_cmd`) and the `JMP` from `send_fs_request` (`&9465`).""",
    on_entry={"y": "extra dispatch offset (0 from send_fs_request, non-zero for some specialised paths)"},
)


d.comment(0x8E56, "Set up command and send to FS", align=Align.INLINE)
d.comment(0x8E59, "Load reply function code", align=Align.INLINE)
d.comment(0x8E5C, "Zero: no reply, return", align=Align.INLINE)
d.comment(0x8E5E, "Load first reply byte", align=Align.INLINE)
d.comment(0x8E61, "Y=&25: logon dispatch offset", align=Align.INLINE)
d.comment(0x8E65, "Parse reply as decimal number", align=Align.INLINE)
d.label(0x8E65, "fscv_handler")
for i, ev in enumerate(_ev_dispatch):
    addr = 0x8EC1 + i * 2
    d.word(addr)
    d.expr(addr, sym(ev))
    d.comment(addr, "%s dispatch" % ev[3:].upper(), align=Align.INLINE)
d.comment(0x8E68, "Result >= 8?", align=Align.INLINE)
d.comment(0x8E6A, "Yes: out of range, return", align=Align.INLINE)
d.comment(0x8E6C, "Transfer handle to X", align=Align.INLINE)
d.comment(0x8E6D, "Look up in open files table", align=Align.INLINE)
d.comment(0x8E70, "Transfer result to A", align=Align.INLINE)
d.comment(0x8E71, "Y=&1D: handle dispatch offset", align=Align.INLINE)
d.label(0x8E75, "dir_op_dispatch")

d.subroutine(
    0x8E75,
    "dir_op_dispatch",
    title="Dispatch directory operation via PHA/PHA/RTS",
    description="""Validates `X < 5` and sets `Y = &18` as the dispatch offset,
then falls through into [`svc_dispatch`](label:svc_dispatch). The
`INX`/`DEY`/`BPL` loop in
[`svc_dispatch`](label:svc_dispatch) then settles `X_final =
X_caller + Y + 1`, landing on indices `&19..&1D` of the
[`svc_dispatch_lo`](label:svc_dispatch_lo) /
[`svc_dispatch_hi`](label:svc_dispatch_hi) tables. Those slots map to
the language-reply handlers `lang_0_insert_key`
(idx `&19`) through `lang_4_validated` (idx `&1D`).""",
    on_entry={"x": "directory operation code (0-4)"},
)


d.comment(0x8E75, "Handle >= 5?", align=Align.INLINE)
d.comment(0x8E77, "Yes: out of range, return", align=Align.INLINE)
d.comment(0x8E79, "Y=&18: settles X_final to &19..&1D (lang reply 0..4)", align=Align.INLINE)
d.comment(0x8E7B, "Advance X to target index", align=Align.INLINE)
d.subroutine(
    0x8E7B,
    "svc_dispatch",
    title="PHA/PHA/RTS table dispatch",
    description="""Computes a target index by incrementing `X` and decrementing `Y`
until `Y` goes negative, effectively calculating `X+Y+1`. Pushes
the target address (high then low byte) from
[`svc_dispatch_lo`](label:svc_dispatch_lo) /
[`svc_dispatch_hi`](label:svc_dispatch_hi) onto the stack, loads
`fs_options` into `X`, then `RTS` jumps to the target
subroutine. Used for all service dispatch, FS command execution,
and OSBYTE handler routing.

Routine extent is &8E61-&8E88 (the `RTS` is the dispatch). The
short Master service handlers at
[`noop_dey_rts`](label:noop_dey_rts) (svc &24),
[`copy_template_to_zp`](label:copy_template_to_zp) (svc &25) and
[`svc_26_close_all_files`](label:svc_26_close_all_files) sit immediately after.""",
    on_entry={"x": "base dispatch index", "y": "additional offset"},
    on_exit={"x": "fs_options value"},
)


d.comment(0x8E7C, "Decrement Y offset counter", align=Align.INLINE)
d.comment(0x8E7D, "Y still positive: continue counting", align=Align.INLINE)
d.comment(0x8E7F, "Y=&FF: will be ignored by caller", align=Align.INLINE)
d.comment(0x8E80, "Load dispatch address high byte", align=Align.INLINE)
d.comment(0x8E83, "Push high byte for RTS dispatch", align=Align.INLINE)
d.label(0x8E84, "push_dispatch_lo")

d.comment(0x8E84, "Load dispatch address low byte", align=Align.INLINE)
d.comment(0x8E87, "Push low byte for RTS dispatch", align=Align.INLINE)
d.comment(0x8E88, "Load FS options pointer", align=Align.INLINE)
d.label(0x8E8A, "dispatch_rts")

d.comment(0x8E8A, "Dispatch via RTS", align=Align.INLINE)
d.comment(0x8E8B, "Claim 1 page (DEY = decrement Y by 1)", align=Align.INLINE)
d.entry(0x8E8B)
d.subroutine(
    0x8E8B,
    "noop_dey_rts",
    title="Service &24: dynamic workspace claim (1 page)",
    description="""Two-byte handler reached via [`svc_dispatch`](label:svc_dispatch) slot
&13. `DEY` decrements the caller's first-available-page count by 1
to claim a single workspace page; `RTS` returns to the dispatcher.""",
)


d.comment(0x8E8C, "Return", align=Align.INLINE)
d.comment(0x8E8D, "X = 10 (top of 11-byte template)", align=Align.INLINE)
d.entry(0x8E8D)
d.subroutine(
    0x8E8D,
    "copy_template_to_zp",
    title="Service &25: FS name + info reply",
    description="""Reached via [`svc_dispatch`](label:svc_dispatch) slot &14. Copies the
11-byte template at [`fs_info_template`](label:fs_info_template) into the
caller's workspace at `(os_text_ptr),Y`. The loop counts `X`
down from 10 to 0 reading from `template[X]`, while `Y`
increments from the caller's value, so the destination ends up
holding the template byte-reversed (`'NET      /' + length-byte`).
Returns via the shared `RTS` at
[`fs_template_done`](label:fs_template_done).""",
)


d.label(0x8E8F, "loop_copy_return_template")

d.comment(0x8E8F, "Load template byte X from &8E99+X", align=Align.INLINE)
d.comment(0x8E92, "Store at (&F2),Y", align=Align.INLINE)
d.comment(0x8E94, "Advance destination cursor", align=Align.INLINE)
d.comment(0x8E95, "Step to previous template byte", align=Align.INLINE)
d.comment(0x8E96, "Loop until X has wrapped past 0", align=Align.INLINE)
d.label(0x8E98, "fs_template_done")

d.comment(0x8E98, "Return", align=Align.INLINE)
d.index_base(0x8E99, "fs_info_template")
d.banner(
    0x8E99,
    title="FS-name reply template (11 bytes, byte-reversed)",
    description="""Source data for the byte-reverse copy in
[`copy_template_to_zp`](label:copy_template_to_zp). When stored at
`(os_text_ptr),Y` in reverse order the destination reads
`"NET" + 6 spaces + "/" + length-byte 5`, which is the FS name
the ROM reports for service &25 (FS name + info reply).""",
)

d.comment(
    0x8E9A,
    "11-byte template (length 5 in [0], then '       TEN'); copied to (&F2),Y by copy_template_to_zp",
    align=Align.INLINE,
)
d.comment(0x8EA4, "Test bit 6 of fs_flags (NFS currently selected?)", align=Align.INLINE)
d.entry(0x8EA4)
d.subroutine(
    0x8EA4,
    "svc_26_close_all_files",
    title="Service &26: close all files (FILEV via Y=0)",
    description="""Reached via [`svc_dispatch`](label:svc_dispatch) slot &15. Tests bit 6
of [`fs_flags`](label:fs_flags) (NFS-active flag). If clear, branches
back to the shared `RTS` at [`fs_template_done`](label:fs_template_done)
without acting. Otherwise calls
[`ensure_fs_selected`](label:ensure_fs_selected) to make NFS the current
filing system, sets `A=Y=0` and tail-calls
[`findv_handler`](label:findv_handler) — the FILEV `Y=0` path closes all
open NFS channels.""",
)


d.comment(0x8EA7, "Clear: return without acting", align=Align.INLINE)
d.comment(0x8EA9, "Ensure NFS is the selected FS", align=Align.INLINE)
d.comment(0x8EAC, "A=0", align=Align.INLINE)
d.comment(0x8EAE, "Y=0 -- FILEV 'close all files' sub-call", align=Align.INLINE)
d.comment(0x8EAF, "Tail-call findv_handler (= FILEV)", align=Align.INLINE)
d.subroutine(
    0x8EB2,
    "read_cmos_byte_0",
    title="Read CMOS RAM byte 0",
    description="""Sets `X=0` and falls through to [`osbyte_a1`](label:osbyte_a1),
which issues OSBYTE `&A1` to read CMOS RAM byte 0 – the
file-system / language byte holding the default boot mode and FS
selection.

Single caller (`&8FBD`, inside
[`nfs_init_body`](label:nfs_init_body)'s CMOS-read sequence).""",
    on_exit={"y": "CMOS byte 0 (returned by OSBYTE &A1)"},
)


d.comment(0x8EB2, "X=0: CMOS RAM index 0 (station ID)", align=Align.INLINE)
d.comment(0x8EB4, "A=&A1: OSBYTE &A1 = read CMOS RAM", align=Align.INLINE)
d.subroutine(
    0x8EB4,
    "osbyte_a1",
    title="OSBYTE &A1 (read Master CMOS RAM byte)",
    description="""Loads `A=&A1` and tail-jumps to `OSBYTE` – reads the Master 128
CMOS RAM byte indexed by `X`. Two callers:
[`format_filename_field`](label:format_filename_field) and
[`flip_set_station_boot`](label:flip_set_station_boot).

**Dual-use trick:** the 5 bytes `A9 A1 4C F4 FF` also serve as
the leading slot of the vector-dispatch table that
[`write_vector_entry`](label:write_vector_entry) reads via
`LDA osbyte_a1,Y` – a deliberate overlap so the routine's body
doubles as table data.""",
    on_entry={"x": "CMOS RAM byte index"},
    on_exit={"y": "CMOS byte read", "x": "preserved"},
)


d.comment(
    0x8EB9,
    """Printer server template (8 bytes)

Default printer server configuration data, read
indirectly by copy_ps_data via LDA ps_template_base,X
with X=&F8..&FF (reaching ps_template_base+&F8 =
&8EB9). Contains "PRINT " (6 bytes) as the default
printer server name, followed by &01 and &00 as
default status bytes. Absent from NFS versions;
unique to ANFS.""",
)
d.comment(0x8EB9, 'PS template: default name "PRINT "', align=Align.INLINE)
d.label(0x8EB9, "ps_template_data")
d.banner(
    0x8EB9,
    title="Printer-server name template (8 bytes)",
    description="""Eight bytes (`"PRINT "` then `&01 &00`) read by
[`copy_ps_data`](label:copy_ps_data) via the indexed-base trick
`LDA ps_template_base+X` with `X=&F8..&FF`. The base label
`ps_template_base` resolves to `ps_template_data - &F8` so the
indexed access lands on the bytes here. Default contents installed
into the Printer-Server name slot during ANFS initialisation.""",
)

d.subroutine(
    0x8EC1,
    "fs_vector_table",
    title="FS vector dispatch and handler addresses (34 bytes)",
    description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by loop_set_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the extended vector table.

Bytes 14-33: handler address pairs read by write_vector_entry.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (write_vector_entry writes the current ROM
bank number instead). The last entry (FSCV) has no padding
byte.""",
)

d.comment(0x8EE3, "X=0 then fall through into osbyte_yff", align=Align.INLINE)
d.subroutine(
    0x8EE3,
    "osbyte_x0",
    title="OSBYTE wrapper with X=0, Y=&FF",
    description="""Sets X=0 and falls through to osbyte_yff to also
set Y=&FF. Provides a single call to execute
OSBYTE with A as the function code. Used by
adlc_init, init_adlc_and_vectors, and Econet
OSBYTE handling.""",
    on_entry={"a": "OSBYTE function code"},
    on_exit={"x": "0", "y": "&FF"},
)


d.label(0x8EE3, "osbyte_x0")

d.comment(0x8EE5, "Y=&FF: 'read' parameter for OSBYTE", align=Align.INLINE)
d.subroutine(
    0x8EE5,
    "osbyte_yff",
    title="OSBYTE wrapper with Y=&FF",
    description="""Sets Y=&FF and JMPs to the MOS OSBYTE entry
point. X must already be set by the caller. The
osbyte_x0 entry point falls through to here after
setting X=0.""",
    on_entry={"a": "OSBYTE function code", "x": "OSBYTE X parameter"},
    on_exit={"y": "&FF"},
)

d.label(0x8EE5, "osbyte_yff")


d.label(0x8EE7, "jmp_osbyte")

d.comment(0x8EE7, "Tail-call OSBYTE", align=Align.INLINE)
d.subroutine(
    0x8EEC,
    "osbyte_x0_y0",
    title="OSBYTE wrapper with X=0, Y=0",
    description="""Sets `X=0` and `Y=0` then branches to `jmp_osbyte`. Called from
the Econet OSBYTE dispatch chain to handle OSBYTEs that require
both `X` and `Y` cleared. The unconditional `BEQ` (after `LDY
#0` sets `Z`) reaches the `JMP osbyte` instruction.""",
    on_entry={"a": "OSBYTE number"},
    on_exit={"x": "0", "y": "0"},
)


d.comment(0x8EEC, "X=0: clear OSBYTE X arg", align=Align.INLINE)
d.comment(0x8EEE, "Y=0", align=Align.INLINE)
d.comment(0x8EF2, "Get original OSBYTE A parameter", align=Align.INLINE)
d.entry(0x8EF2)
d.label(0x8EF2, "svc_7_osbyte")

d.subroutine(
    0x8EF2,
    "svc_7_osbyte",
    title="Service 7: unrecognised OSBYTE",
    description="""Maps Econet OSBYTE codes &32-&35 to dispatch
indices 0-3 by subtracting &31 (with carry from
a preceding SBC). Returns unclaimed if the OSBYTE
number is outside this range. For valid codes,
claims the service (sets svc_state to 0) and
JMPs to svc_dispatch with Y=&21 to reach the
Econet OSBYTE handler table.""",
    on_entry={"a": "OSBYTE number (from osbyte_a_copy at &EF)"},
)
d.comment(0x8EF4, "Subtract &31 (map &32-&35 to 1-4)", align=Align.INLINE)
d.comment(0x8EF6, "In range 0-3?", align=Align.INLINE)
d.comment(0x8EF8, "No: not ours, return unclaimed", align=Align.INLINE)
d.comment(0x8EFA, "Transfer to X as dispatch index", align=Align.INLINE)
d.comment(0x8EFB, "Clear svc_state", align=Align.INLINE)
d.comment(0x8EFD, "Transfer Y to A (OSBYTE Y param)", align=Align.INLINE)
d.comment(0x8EFE, "Y=&2F: OSBYTE dispatch offset", align=Align.INLINE)
d.comment(0x8F00, "Dispatch to OSBYTE handler via table", align=Align.INLINE)
d.comment(0x8F03, "Y already >= &C8?", align=Align.INLINE)
d.entry(0x8F03)

d.label(0x8F03, "raise_y_to_c8")

d.subroutine(
    0x8F03,
    "raise_y_to_c8",
    title="Service &21 handler: claim static hidden-RAM workspace",
    description="""Four-instruction stub: `CPY #&C8 / BCS return / LDY #&C8 / RTS`.
Reached when MOS issues service call `&21` ("Offer Static Workspace
in Hidden RAM") to all sideways ROMs at reset. Per the *Advanced
Reference Manual for the BBC Master*, hidden-RAM static workspace
runs from page `&C0` up to page `&DB`; each filing-system ROM that
wants a slice raises Y to its required base page. ANFS demands its
static workspace base at page `&C8`, so it raises Y to `&C8` if a
previous ROM hasn't already.""",
    on_entry={"y": "current bottom of static workspace claim (some page in &C0..&DB)"},
    on_exit={"y": ">= &C8 (ANFS static workspace base)"},
)


d.comment(0x8F05, "Yes: return Y unchanged", align=Align.INLINE)
d.comment(0x8F07, "No: raise Y to &C8", align=Align.INLINE)
d.label(0x8F09, "rts_raise_y_to_c8")

d.comment(0x8F09, "Return", align=Align.INLINE)
d.label(0x8F0A, "store_ws_page_count")

d.subroutine(
    0x8F0A,
    "store_ws_page_count",
    title="Record workspace page count (capped at &D3)",
    description="""Stores the workspace allocation from service 1 into offset `&0B` of
the receive control block, capping the value at `&D3` to prevent
overflow into adjacent workspace areas. Called by
[`svc_2_priv_ws`](label:svc_2_priv_ws) after issuing the
absolute workspace claim service call.""",
    on_entry={"y": "workspace page count from service 1"},
)
d.comment(0x8F0A, "Transfer Y to A", align=Align.INLINE)
d.comment(0x8F0B, "Push for save", align=Align.INLINE)
d.comment(0x8F0C, "Y >= &D3?", align=Align.INLINE)
d.comment(0x8F0E, "No: use Y as-is", align=Align.INLINE)
d.comment(0x8F10, "Cap at &D3", align=Align.INLINE)
d.label(0x8F12, "done_cap_ws_count")

d.comment(0x8F12, "Offset &0B in receive block", align=Align.INLINE)
d.comment(0x8F14, "Store workspace page count", align=Align.INLINE)
d.comment(0x8F16, "Pop -- save Y temporarily", align=Align.INLINE)
d.comment(0x8F17, "Return -- ws_page count saved", align=Align.INLINE)
d.entry(0x8F18)
d.label(0x8F18, "set_rom_ws_page")

d.comment(0x8F18, "Caller's page (in Y) into A", align=Align.INLINE)
d.comment(0x8F19, "Y = current ROM slot from romsel_copy", align=Align.INLINE)
d.comment(0x8F1B, "Push restored value", align=Align.INLINE)
d.comment(0x8F1C, "Mask bit 7 (workspace flag)", align=Align.INLINE)
d.comment(0x8F1E, "Publish page into rom_ws_pages[slot] (bit 7 cleared = workspace claimed)", align=Align.INLINE)
d.comment(0x8F21, "Discarded read of 1770 data reg (&FE2B)", align=Align.INLINE)
d.comment(0x8F24, "Discarded read of 1770 status reg (&FE28)", align=Align.INLINE)
d.comment(0x8F27, "Pop saved Y", align=Align.INLINE)
d.comment(0x8F28, "Increment for next page", align=Align.INLINE)
d.comment(0x8F29, "Return", align=Align.INLINE)
d.entry(0x8F2A)
d.subroutine(
    0x8F2A,
    "svc_2_priv_ws",
    title="Service-2 page-allocation prologue",
    description="""Reads CMOS byte `&11` to test bit 2 of the saved Econet status;
either advances the caller's first-available-page (`Y`) by 2 and
uses it, or forces page `&0B` as a fallback. Sets `net_rx_ptr_hi` /
`nfs_workspace_hi` to the chosen page pair, clears the corresponding
lo bytes, and calls [`get_ws_page`](label:get_ws_page). If the resulting
page is `>= &DC`, branches to the helper at
[`&8EFE`](address:8EFE) which publishes the page into
`rom_ws_pages[romsel_copy]` with bit 7 masked off.

This routine handles only the workspace-page allocation half of
service 2. The bring-up remainder (station ID, FS workspace zero,
`cmd_net_fs`, [`init_adlc_and_vectors`](label:init_adlc_and_vectors)) lives at
[`nfs_init_body`](label:nfs_init_body) and is dispatched separately – see
the comment block above.""",
    on_entry={"y": "first available private workspace page"},
)


d.comment(0x8F2A, "Save Y on stack (caller's claim)", align=Align.INLINE)
d.comment(0x8F2B, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0x8F2D, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0x8F30, "A = CMOS &11 value", align=Align.INLINE)
d.comment(0x8F31, "Mask bit 2 (workspace-size flag)", align=Align.INLINE)
d.comment(0x8F33, "Bit 2 set: keep caller's Y, advance by 2", align=Align.INLINE)
d.comment(0x8F35, "Bit 2 clear: A=&0B (use 11-page minimum)", align=Align.INLINE)
d.comment(0x8F37, "BRA to common tail", align=Align.INLINE)
d.comment(0x8F39, "Bit-2-set path: restore Y", align=Align.INLINE)
d.label(0x8F39, "private_ws_set_bit")

d.comment(0x8F3A, "TYA / INY / INY -- raise Y by 2 pages", align=Align.INLINE)
d.comment(0x8F3B, "Y += 1", align=Align.INLINE)
d.comment(0x8F3C, "Y += 1 again (total +2)", align=Align.INLINE)
d.comment(0x8F3D, "Push raised Y", align=Align.INLINE)
d.comment(0x8F3E, "Store final page count high to net_rx_ptr_hi", align=Align.INLINE)
d.label(0x8F3E, "commit_workspace_pages")

d.comment(0x8F40, "Increment for nfs_workspace_hi", align=Align.INLINE)
d.comment(0x8F41, "Store workspace high page", align=Align.INLINE)
d.comment(0x8F43, "A=0: clear-byte for the lo halves below", align=Align.INLINE)
d.comment(0x8F45, "Clear net_rx_ptr_lo (page-aligned)", align=Align.INLINE)
d.comment(0x8F47, "Clear nfs_workspace_lo (page-aligned)", align=Align.INLINE)
d.comment(0x8F49, "Compute workspace start page via get_ws_page", align=Align.INLINE)
d.comment(0x8F4C, "Y >= &DC?", align=Align.INLINE)
d.comment(0x8F4E, "Restore Y from stack", align=Align.INLINE)
d.comment(0x8F4F, "Yes: jump to set_rom_ws_page (error path)", align=Align.INLINE)
d.comment(0x8F51, "Return", align=Align.INLINE)
d.entry(0x8F52)


d.subroutine(
    0x8F52,
    "nfs_init_body",
    title="ANFS initialisation body",
    description="""Reached only via PHA/PHA/RTS dispatch (table index 22 in the
svc_dispatch table at `&8A23` / `&8A22`). Carries out the bring-up
sequence after page allocation:

- Clears `ws_page` / `tx_complete_flag` and the receive-block
  remote-op flag.
- On warm reset (`last_break_type` non-zero) and `fs_flags` bit 4
  set, calls [`setup_ws_ptr`](label:setup_ws_ptr) and zeroes the FS
  workspace page in a 256-byte loop.
- Calls [`copy_ps_data_y1c`](label:copy_ps_data_y1c) to install the printer-
  server template.
- Reads CMOS bytes `&01..&04` via `osbyte_a1`, storing each into
  the workspace identity block at `nfs_workspace+{0..3}`.
- Reads CMOS byte `&11` (Econet station): if zero, prints
  `Station number in CMOS RAM invalid. Using 1 instead!` and
  defaults to station 1.
- Stores station ID into the receive block.
- Calls `cmd_net_fs` to select ANFS as the active filing system,
  then [`init_adlc_and_vectors`](label:init_adlc_and_vectors) to install NETV /
  FSCV / etc., `handle_spool_ctrl_byte` and `init_bridge_poll`
  for protection setup.

Returns via `RTS` at `&9042`.

Reached via Master 128 service call `&27` (= 39 decimal),
documented in the *Advanced Reference Manual for the BBC Master*:

> Reset has occurred. Call made after hard reset. Mainly for
> Econet Filing system so that it can claim NMIs. This call is
> now required since the MOS no longer offers workspace on a
> soft BREAK. A Sideways ROM should therefore re-initialise
> itself.

The full set of Master 128 service calls ANFS handles, dispatched
via the CMP/SBC normalisation chain in
[`service_handler`](label:service_handler):

| dec   | hex        | handler                   | purpose                |
| ----- | ---------- | ------------------------- | ---------------------- |
| 0..12 | `&00..&0C` | (svc-1..12 handlers)      | service-1 .. service-12 |
| 18    | `&12`      | `svc_18_fs_select`        | FS select              |
| 24    | `&18`      | `match_on_suffix`         | Interactive HELP       |
| 33    | `&21`      | `raise_y_to_c8`           | static ws claim        |
| 34    | `&22`      | `set_rom_ws_page`         | dynamic ws offer       |
| 35    | `&23`      | `store_ws_page_count`     | top-of-static-ws       |
| 36    | `&24`      | `noop_dey_rts`            | dynamic ws claim (1 pg) |
| 37    | `&25`      | `copy_template_to_zp`     | FS name + info reply   |
| 38    | `&26`      | `svc_26_close_all_files`  | close all files        |
| 39    | `&27`      | `nfs_init_body` (this)    | reset re-init          |
| 40    | `&28`      | `print_fs_ps_help`        | *CONFIGURE option      |
| 41    | `&29`      | `svc_29_status`           | *STATUS option         |

Everything else (svc `&0D..&11`, `&13..&17`, `&19..&20`, `&2A+`)
falls through to
[`dispatch_svc_state_check`](label:dispatch_svc_state_check) with `A := 0` and
dispatches to idx 1 = `dispatch_rts` (no-op) – deliberately
ignoring svc `&15` (100 Hz poll), svc `&2A` (language ROM
startup), etc.""",
)

d.comment(0x8F52, "A=0: clear-byte for the next four stores", align=Align.INLINE)
d.comment(0x8F54, "Clear ws_page (workspace page count)", align=Align.INLINE)
d.comment(0x8F56, "Clear tx_complete_flag", align=Align.INLINE)
d.comment(0x8F59, "Y=0: receive-block offset 0 (remote-op flag)", align=Align.INLINE)
d.comment(0x8F5B, "Clear remote-op flag at (net_rx_ptr)+0", align=Align.INLINE)
d.comment(0x8F5D, "Read l028D (current ROM number)", align=Align.INLINE)
d.comment(0x8F60, "Non-zero (re-init): take nfs_init_check_fs_flags path", align=Align.INLINE)
d.comment(0x8F62, "A=&10: fs_flags bit 4 mask (checks 'workspace already set up')", align=Align.INLINE)
d.comment(0x8F67, "Zero: first ROM init, skip FS setup", align=Align.INLINE)
d.label(0x8F69, "nfs_init_check_fs_flags")

d.comment(0x8F69, "Set up workspace pointers", align=Align.INLINE)
d.comment(0x8F6C, "Clear FS flags", align=Align.INLINE)
d.comment(0x8F73, "A=0, transfer to Y", align=Align.INLINE)
d.label(0x8F74, "loop_zero_workspace")

d.comment(0x8F74, "Clear byte in FS workspace", align=Align.INLINE)
d.comment(0x8F76, "Next workspace byte", align=Align.INLINE)
d.comment(0x8F77, "Loop until full page (256 bytes) cleared", align=Align.INLINE)
d.comment(0x8F79, "Copy initial PS template (1C bytes) into ws", align=Align.INLINE)
d.comment(0x8F7C, "X=1: CMOS &01 = port number", align=Align.INLINE)
d.comment(0x8F7E, "Read CMOS &01", align=Align.INLINE)
d.comment(0x8F81, "Store at hazel_fs_station (workspace+0)", align=Align.INLINE)
d.comment(0x8F84, "X=2: CMOS &02 = network number", align=Align.INLINE)
d.comment(0x8F86, "Read CMOS &02", align=Align.INLINE)
d.comment(0x8F89, "Store at hazel_fs_network", align=Align.INLINE)
d.comment(0x8F8C, "X=3: CMOS &03 = FS station", align=Align.INLINE)
d.comment(0x8F8E, "Read CMOS &03", align=Align.INLINE)
d.comment(0x8F91, "A = FS station", align=Align.INLINE)
d.comment(0x8F92, "Y=2: nfs_workspace offset for FS station", align=Align.INLINE)
d.comment(0x8F94, "Store FS station at (nfs_workspace)+2", align=Align.INLINE)
d.comment(0x8F96, "X=4: CMOS &04 = FS network", align=Align.INLINE)
d.comment(0x8F98, "Read CMOS &04 (FS network)", align=Align.INLINE)
d.comment(0x8F9B, "A = FS network", align=Align.INLINE)
d.comment(0x8F9C, "Y=3: nfs_workspace offset for FS network", align=Align.INLINE)
d.comment(0x8F9E, "Store at NFS workspace offset 2", align=Align.INLINE)
d.comment(0x8FA0, "X=3: init data byte count", align=Align.INLINE)
d.label(0x8FA2, "loop_copy_init_data")

d.comment(0x8FA2, "Load initialisation data byte", align=Align.INLINE)
d.comment(0x8FA5, "Store in workspace", align=Align.INLINE)
d.comment(0x8FA8, "Decrement counter", align=Align.INLINE)
d.comment(0x8FA9, "More bytes: loop", align=Align.INLINE)
d.comment(0x8FAB, "Clear workspace flag", align=Align.INLINE)
d.comment(0x8FAE, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8FB1, "Initialise ADLC protection table", align=Align.INLINE)
d.comment(0x8FB4, "X=&FF (underflow from X=0)", align=Align.INLINE)
d.comment(0x8FB5, "Initialise workspace flag to &FF", align=Align.INLINE)
d.comment(0x8FB8, "X=&11: CMOS &11 (ANFS settings)", align=Align.INLINE)
d.comment(0x8FBA, "Read CMOS &11", align=Align.INLINE)
d.comment(0x8FBD, "A = settings byte", align=Align.INLINE)
d.comment(0x8FBE, "Mask bit 6 (CMOS protection-state flag)", align=Align.INLINE)
d.comment(0x8FC0, "Bit clear: skip the &FF substitution", align=Align.INLINE)
d.comment(0x8FC2, "A=&FF -- enable protection", align=Align.INLINE)
d.comment(0x8FC4, "Set prot_status/prot_status_save pair", align=Align.INLINE)
d.label(0x8FC4, "init_copy_skip_cmos")

d.label(0x8FC7, "loop_alloc_handles")

d.comment(0x8FC7, "Get current workspace page", align=Align.INLINE)
d.comment(0x8FC9, "Allocate FS handle page", align=Align.INLINE)
d.comment(0x8FCC, "Allocation failed: finish init", align=Align.INLINE)
d.comment(0x8FCE, "A=&3F: default handle permissions", align=Align.INLINE)
d.comment(0x8FD0, "Store handle permissions", align=Align.INLINE)
d.comment(0x8FD2, "Advance to next page", align=Align.INLINE)
d.comment(0x8FD4, "Continue allocating: loop", align=Align.INLINE)
d.label(0x8FD6, "done_alloc_handles")


d.comment(0x8FD6, "Restore FS context from saved state", align=Align.INLINE)
d.comment(0x8FD9, "Read CMOS &00 (= station ID byte)", align=Align.INLINE)
d.label(0x8FD9, "alloc_post_restore_check")

d.comment(0x8FDC, "Y (CMOS value) into A", align=Align.INLINE)
d.comment(0x8FDD, "Non-zero: station ID valid -> alloc_common_entry", align=Align.INLINE)
d.comment(0x8FDF, "Print 'Station number in CMOS RAM invalid...' warning", align=Align.INLINE)
d.label(0x8FDF, "alloc_error_overflow")

d.comment(0x9004, "A=1: default station ID", align=Align.INLINE)
d.comment(0x9006, "BRA to alloc_store_station_id with default", align=Align.INLINE)
d.comment(0x9008, "Check next byte (CMOS station ID hi?)", align=Align.INLINE)
d.label(0x9008, "alloc_common_entry")

d.comment(
    0x9009,
    "INY wrapped past 0 (station=&FF then INY=&00): report 'CMOS RAM invalid' and default to 1",
    align=Align.INLINE,
)
d.comment(0x900B, "BRA to alloc_store_station_id (always)", align=Align.INLINE)
d.comment(0x900D, "Y=1: net_rx_ptr offset for station-ID byte", align=Align.INLINE)
d.label(0x900D, "alloc_store_station_id")

d.comment(0x900F, "Store station ID into (net_rx_ptr)+1", align=Align.INLINE)
d.comment(0x9011, "X=&40: econet_flags init value", align=Align.INLINE)
d.comment(0x9013, "Initialise econet_flags", align=Align.INLINE)
d.comment(0x9016, "Call cmd_net_fs to select NFS", align=Align.INLINE)
d.comment(0x9019, "Z: selection succeeded", align=Align.INLINE)
d.comment(0x901B, "A=&10: bit 4 marker for fs_flags", align=Align.INLINE)
d.comment(0x9020, "Store updated fs_flags", align=Align.INLINE)
d.comment(0x9023, "Initialise ADLC and FILEV/ARGSV/...vectors", align=Align.INLINE)
d.label(0x9023, "complete_nfs_init")

d.comment(0x9026, "A=3: spool-ctrl byte 'init'", align=Align.INLINE)
d.comment(0x9028, "Initialise *SPOOL handle in workspace", align=Align.INLINE)
d.comment(0x902B, "Send a bridge-discovery packet and poll", align=Align.INLINE)
d.comment(0x902E, "Save current bridge byte", align=Align.INLINE)
d.comment(0x902F, "With stored hazel_fs_network (network number)", align=Align.INLINE)
d.comment(0x9032, "Different: take verify_copy_station_id path", align=Align.INLINE)
d.comment(0x9034, "Same: store as new hazel_fs_network", align=Align.INLINE)
d.comment(0x9037, "Y=3: net_rx_ptr offset 3", align=Align.INLINE)
d.comment(0x9039, "Store at (net_rx_ptr)+3", align=Align.INLINE)
d.comment(0x903B, "Restore saved byte", align=Align.INLINE)
d.label(0x903B, "verify_copy_station_id")

d.comment(0x903C, "Y=3: workspace offset", align=Align.INLINE)
d.comment(0x9040, "Mismatch: skip store", align=Align.INLINE)
d.comment(0x9042, "Match: store at (nfs_workspace)+3", align=Align.INLINE)
d.comment(0x9044, "Return", align=Align.INLINE)
d.label(0x9045, "init_adlc_and_vectors")

d.subroutine(
    0x9045,
    "init_adlc_and_vectors",
    title="Initialise ADLC and install extended vectors",
    description="""Reads the ROM pointer table via OSBYTE `&A8`, writes vector
addresses and ROM ID into the extended vector table for `NETV`
and one additional vector, then restores any previous FS context
via [`restore_fs_context`](label:restore_fs_context). Falls through into
[`write_vector_entry`](label:write_vector_entry).""",
    on_exit={"a, x, y": "clobbered (falls through into write_vector_entry)"},
)


d.comment(0x9045, "Initialise ADLC hardware", align=Align.INLINE)
d.comment(0x9048, "OSBYTE &A8: read ROM pointer table", align=Align.INLINE)
d.comment(0x904A, "Read ROM pointer table address", align=Align.INLINE)
d.comment(0x904D, "Store table pointer low", align=Align.INLINE)
d.comment(0x904F, "Store table pointer high", align=Align.INLINE)
d.comment(0x9051, "Y=&36: NETV vector offset", align=Align.INLINE)
d.comment(0x9053, "Set NETV address", align=Align.INLINE)
d.comment(0x9056, "X=1: one more vector pair to set", align=Align.INLINE)
d.label(0x9058, "write_vector_entry")

d.subroutine(
    0x9058,
    "write_vector_entry",
    title="Install extended-vector table entries",
    description="""Copies vector addresses from the dispatch table at
`svc_dispatch_lo_offset+Y` into the MOS extended-vector table
pointed to by `fs_error_ptr`. For each entry, writes address low,
high, then the current ROM ID from `romsel_copy` (`&F4`). Loops
`X` times.

After the loop, stores `&FF` at
[`bridge_status`](label:bridge_status) as an installed flag, calls
`deselect_fs_if_active` and [`get_ws_page`](label:get_ws_page) to
restore FS state.""",
    on_entry={"x": "number of vectors to install", "y": "starting offset in extended vector table"},
    on_exit={"y": "workspace page number + 1"},
)


d.comment(0x9058, "Load vector address low byte", align=Align.INLINE)
d.comment(0x905B, "Store into extended vector table", align=Align.INLINE)
d.comment(0x905D, "Advance to high byte", align=Align.INLINE)
d.comment(0x905E, "Load vector address high byte", align=Align.INLINE)
d.comment(0x9061, "Store into extended vector table", align=Align.INLINE)
d.comment(0x9063, "Advance to ROM ID byte", align=Align.INLINE)
d.comment(0x9064, "Load current ROM slot number", align=Align.INLINE)
d.comment(0x9066, "Store ROM ID in extended vector", align=Align.INLINE)
d.comment(0x9068, "Advance to next vector entry", align=Align.INLINE)
d.comment(0x9069, "Decrement vector counter", align=Align.INLINE)
d.comment(0x906A, "More vectors to set: loop", align=Align.INLINE)
d.comment(0x906C, "Return", align=Align.INLINE)
d.label(0x906D, "restore_fs_context")

d.subroutine(
    0x906D,
    "restore_fs_context",
    title="Restore FS context from HAZEL into RX block",
    description="""Copies 8 bytes (offsets 2..9) from the HAZEL FS state block into
the receive control block at `(net_rx_ptr)+Y`. The source uses
the [`hazel_minus_2`](label:hazel_minus_2) indexing-base trick:
`LDA hazel_minus_2,Y` with `Y` running 9 down to 2 lands at
`&C007..&C000` (the [`hazel_fs_station`](label:hazel_fs_station) block --
station, network, saved station, CSD/lib slots, FS flags, etc.).
Restores those bytes into the RX control block when the caller
needs to re-publish the FS context (e.g. after a flip-set boot).

Called by [`svc_2_priv_ws`](label:svc_2_priv_ws) during init,
`deselect_fs_if_active` during FS teardown, and
`flip_set_station_boot`.""",
    on_exit={"a, y": "clobbered (loop counter / data byte)"},
)


d.comment(0x906D, "Y=9: end of FS context block", align=Align.INLINE)
d.label(0x906F, "loop_restore_ctx")

d.comment(0x906F, "Load FS context byte", align=Align.INLINE)
d.comment(0x9072, "Store into receive block", align=Align.INLINE)
d.comment(0x9074, "Decrement index", align=Align.INLINE)
d.comment(0x9075, "Reached offset 1?", align=Align.INLINE)
d.comment(0x9077, "No: continue copying", align=Align.INLINE)
d.comment(0x9079, "Return", align=Align.INLINE)
d.label(0x907A, "fscv_6_shutdown")

d.subroutine(
    0x907A,
    "fscv_6_shutdown",
    title="Deselect filing system and save workspace",
    description="""If the filing system is currently selected (bit 7 of
[`fs_flags`](label:fs_flags) set):

1. Closes all open FCBs.
2. Closes `*SPOOL`/`*EXEC` files via OSBYTE `&77`.
3. Saves the FS workspace to page `&10` shadow with checksum.
4. Clears the selected flag.""",
)


d.comment(0x907A, "FS currently selected?", align=Align.INLINE)
d.entry(0x907A)
d.comment(0x907D, "No (bit 7 clear): return", align=Align.INLINE)
d.comment(0x907F, "Y=0", align=Align.INLINE)
d.comment(0x9081, "Close all FCBs (process_all_fcbs)", align=Align.INLINE)
d.comment(0x9084, "Restore FS context to receive block", align=Align.INLINE)
d.comment(0x9087, "Y=&76: checksum range end", align=Align.INLINE)
d.comment(0x9089, "A=0: checksum accumulator", align=Align.INLINE)
d.comment(0x908B, "Clear carry for addition", align=Align.INLINE)
d.label(0x908C, "loop_checksum_byte")

d.comment(0x908C, "Add byte from the HAZEL &C2 FCB shadow", align=Align.INLINE)
d.comment(0x908F, "Decrement index", align=Align.INLINE)
d.comment(0x9090, "Loop until all bytes summed", align=Align.INLINE)
d.comment(0x9092, "Y=&77: checksum storage offset", align=Align.INLINE)
d.label(0x9096, "loop_copy_to_ws")

d.comment(0x9096, "Load byte from the HAZEL &C2 FCB shadow", align=Align.INLINE)
d.label(0x9099, "store_ws_byte")

d.comment(0x9099, "Copy to FS workspace", align=Align.INLINE)
d.comment(0x909B, "Decrement index", align=Align.INLINE)
d.comment(0x909C, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x909E, "Load FS flags", align=Align.INLINE)
d.comment(0x90A1, "Clear bit 7 (FS no longer selected)", align=Align.INLINE)
d.comment(0x90A3, "Store updated flags", align=Align.INLINE)
d.label(0x90A6, "rts_fs_shutdown")

d.comment(0x90A6, "Return", align=Align.INLINE)
d.label(0x90A7, "verify_ws_checksum")

d.subroutine(
    0x90A7,
    "verify_ws_checksum",
    title="Verify workspace checksum integrity",
    description="""Sums bytes 0..`&76` of the workspace page via the zero-page
pointer at `&CC`/`&CD` and compares with the stored value at
offset `&77`. On mismatch, raises a 'net sum' error (`&AA`) via
[`error_net_checksum`](label:error_net_checksum).

The checksummed page holds open-file information (preserved when
ANFS is not the current filing system) and the current printer
type. Can only be reset by a control-BREAK.

Preserves `A`, `Y`, and processor flags using `PHP`/`PHA`. Called
by 5 sites across `format_filename_field`, `adjust_fsopts_4bytes`,
and `start_wipe_pass` before workspace access.""",
    on_exit={"a": "preserved (PHA/PLA)", "y": "preserved", "p (flags)": "preserved (PHP/PLP)"},
)


d.comment(0x90A7, "Save processor status", align=Align.INLINE)
d.comment(0x90A8, "Save A", align=Align.INLINE)
d.comment(0x90AA, "Y=&76: checksum range end", align=Align.INLINE)
d.comment(0x90AC, "A=0: checksum accumulator", align=Align.INLINE)
d.comment(0x90AE, "Clear carry for addition", align=Align.INLINE)
d.label(0x90AF, "loop_sum_ws")

d.comment(0x90AF, "Add byte from FS workspace", align=Align.INLINE)
d.comment(0x90B1, "Decrement index", align=Align.INLINE)
d.comment(0x90B2, "Loop until all bytes summed", align=Align.INLINE)
d.comment(0x90B4, "Y=&77: checksum storage offset", align=Align.INLINE)
d.comment(0x90B6, "Compare with stored checksum", align=Align.INLINE)
d.comment(0x90B8, "Mismatch: raise checksum error", align=Align.INLINE)
d.comment(0x90BB, "Restore A", align=Align.INLINE)
d.comment(0x90BC, "Restore processor status", align=Align.INLINE)
d.comment(0x90BD, "Return (checksum valid)", align=Align.INLINE)
d.label(0x90BE, "error_net_checksum")

d.subroutine(
    0x90BE,
    "error_net_checksum",
    title="Raise 'net checksum' BRK error",
    description="""Loads error code `&AA` and tail-calls `error_bad_inline` with the
inline string 'net checksum'. Reached when
[`ensure_fs_selected`](label:ensure_fs_selected) (auto-select path)
cannot bring ANFS up, or when
[`verify_ws_checksum`](label:verify_ws_checksum) detects that the saved
workspace checksum at offset `&77` doesn't match the live sum –
only resettable by a control-BREAK. Never returns.""",
)


d.comment(0x90BE, "Error number &AA", align=Align.INLINE)
d.comment(0x90C0, "Raise 'net checksum' error", align=Align.INLINE)
d.subroutine(
    0x90D0,
    "print_station_id",
    title="Print Econet station number and clock status",
    description="""Uses [`print_inline`](label:print_inline) to output `'Econet
Station '`, then reads the station ID from offset 1 of the
receive control block and prints it as a decimal number via
`print_num_no_leading`. Tests ADLC status register 2
([`econet_control23_or_status2`](label:econet_control23_or_status2)) to detect the Econet clock; if
absent, appends `' No Clock'` via a second inline string.
Finishes with `OSNEWL`.

Called by [`print_version_header`](label:print_version_header) and
[`svc_3_autoboot`](label:svc_3_autoboot).""",
    on_exit={"a, x, y": "clobbered (print_inline + print_num_no_leading + OSNEWL)"},
)


d.comment(0x90D0, "Print 'Station ' inline string", align=Align.INLINE)
d.comment(0x90D5, "Print 'Econet Station ' via inline", align=Align.INLINE)
d.comment(0x90E2, "Y=1: PB station-byte offset", align=Align.INLINE)
d.comment(0x90E4, "Read RX[1] = station number", align=Align.INLINE)
d.comment(0x90E6, "Print as decimal (no leading zeros)", align=Align.INLINE)
# UNMAPPED: d.comment(0x90DD, "Print as decimal (no leading zeros)", align=Align.INLINE)
d.comment(0x90E9, "Space character", align=Align.INLINE)
d.comment(0x90EB, "Check ADLC status register 2", align=Align.INLINE)
d.comment(0x90EE, "Clock present: skip warning", align=Align.INLINE)
d.comment(0x90F0, "Print ' No Clock' via inline", align=Align.INLINE)
d.comment(0x90FC, "String terminator", align=Align.INLINE)
d.label(0x90FD, "done_print_newline")

d.comment(0x9100, "Return", align=Align.INLINE)
d.index_base(0x9101, "cmd_syntax_strings")
d.banner(
    0x9101,
    title="*HELP / *SYNTAX argument strings (8 messages)",
    description="""Eight zero-terminated argument-syntax strings used by the *HELP
text builder. Each string describes the argument shape of a
particular command group; their offsets within this table are
stored in [`cmd_syntax_table`](label:cmd_syntax_table), keyed by command
index. Read by [`do_print_no_spool`](label:do_print_no_spool) when no command
argument was supplied.""",
)

d.index_base(0x9101, "syn_opt_dir")

d.comment(
    0x9101,
    """*HELP command syntax strings

13 null-terminated syntax help strings displayed
by *HELP after each command name. Multi-line
entries use &0D as a line break. Indexed by
cmd_syntax_table via the low 5 bits of each
command's syntax descriptor byte.""",
)
d.comment(0x9101, "Syn 1: *Dir, *LCat, *LEx, *Wipe", align=Align.INLINE)
d.label(0x9109, "syn_iam")

d.comment(0x9109, "Syn 2: *I Am (login)", align=Align.INLINE)
d.comment(0x9121, "Line break", align=Align.INLINE)
d.comment(0x9122, "syntax help for *Pass / *I am", align=Align.INLINE)
d.label(0x9136, "syn_object")

d.comment(0x9136, "Syn 3: *Delete, *FS, *Remove", align=Align.INLINE)
d.comment(0x914F, "Store as string pointer low", align=Align.INLINE)
d.comment(0x9152, "Store as string pointer high", align=Align.INLINE)
d.comment(0x9155, "Syn 4 continued: address clause", align=Align.INLINE)
d.comment(0x9161, "Null terminator", align=Align.INLINE)
d.label(0x9162, "syn_dir")

d.comment(0x9162, "Syn 5: *Lib", align=Align.INLINE)
d.label(0x9179, "syn_password")

d.comment(0x9179, "Syn 7: *Pass", align=Align.INLINE)
d.comment(0x918D, "Syn 7 continued: new password", align=Align.INLINE)
d.comment(0x919C, "syntax help for *PS / *Pollps", align=Align.INLINE)
d.label(0x91B5, "syn_access")

d.comment(0x91B5, "Syn 9: *Access", align=Align.INLINE)
d.comment(0x91D0, "Null terminator", align=Align.INLINE)
d.label(0x91D1, "syn_rename")

d.comment(0x91D1, "Syn 10: *Rename", align=Align.INLINE)
d.comment(0x91EA, "Null terminator", align=Align.INLINE)
d.label(0x91EB, "syn_opt_stn")

d.comment(0x91EB, "Syn 11: (station id. argument)", align=Align.INLINE)
# UNMAPPED: d.comment(0x91EC, "Null terminator", align=Align.INLINE)
d.index_base(0x91F7, "cmd_syntax_table")
d.banner(
    0x91F7,
    title="Argument-syntax offset table (12 entries)",
    description="""Twelve byte offsets indexing into
[`syn_opt_dir`](label:syn_opt_dir). Each entry is computed as
`<syn_X> - syn_opt_dir - 1` so the print loop can `INY`
before `LDA` and still land on the first byte of the chosen
string. The byte at &91F9 immediately after the table is the
entry point of [`print_no_spool`](address:91F9).""",
)
for i in range(12):
    d.byte(0x91F7 + i)
d.expr(0x91F7, sym("syn_iam") - sym("syn_opt_dir") - 2)
d.comment(
    0x91F7,
    """Command syntax string offset table

13 offsets into syn_opt_dir (&9022).
Indexed by the low 5 bits of each command table
syntax descriptor byte. Index &0E is handled
separately as a shared-commands list. The print
loop at &8BD5 does INY before LDA, so each offset
points to the byte before the first character.""",
)
d.comment(0x91F7, "Idx 0: 'opt_dir' (offset -2 variant for *Dir's INY-twice walker)", align=Align.INLINE)
d.comment(0x91F8, "Idx 1: &FF = no syntax string for this index", align=Align.INLINE)
d.expr(0x91F9, sym("syn_iam") - sym("syn_opt_dir") - 1)
d.comment(0x91F9, 'Idx 2: \\"(<stn.id.>) <user id.>...\\"', align=Align.INLINE)
d.expr(0x91FA, sym("syn_object") - sym("syn_opt_dir") - 1)
d.comment(0x91FA, 'Idx 3: \\"<object>\\"', align=Align.INLINE)
d.comment(0x91FB, 'Idx 4: \\"<filename> (<offset>...)\\"', align=Align.INLINE)
d.comment(0x91FC, "Idx 5: '<dir>' (offset 0x60 = syn_dir)", align=Align.INLINE)
d.comment(0x91FD, "Idx 6: continued <dir> string region", align=Align.INLINE)
d.comment(0x91FE, 'Idx 7: \\"(:<CR>) <password>...\\"', align=Align.INLINE)
d.comment(0x91FF, 'Idx 8: \\"(<stn.id.>|<ps type>)\\"', align=Align.INLINE)
# UNMAPPED: d.expr(0x91F6, "syn_access - syn_opt_dir - 1")
# UNMAPPED: d.comment(0x91F6, 'Idx 9: \\"<object> (L)(W)(R)...\\"', align=Align.INLINE)
# UNMAPPED: d.comment(0x91F7, "Idx 10: '<filename> <new filename>' (syn_rename)", align=Align.INLINE)
# UNMAPPED: d.expr(0x91F8, "syn_opt_stn - syn_opt_dir - 1")

# UNMAPPED: d.comment(0x91F8, 'Idx 11: \\"(<stn. id.>)\\"', align=Align.INLINE)
d.subroutine(
    0x9204,
    "print_newline_no_spool",
    title="Print CR via OSASCI, bypassing any open *SPOOL file",
    description="""Loads `A=&0D` and falls into
[`print_char_no_spool`](label:print_char_no_spool). The underlying
mechanism temporarily writes `0` to the `*SPOOL` file handle
(OSBYTE `&C7` with `X=0`, `Y=0`) so the printed `CR` is not
captured by spool, then restores the previous handle on exit.

Called from [`service_handler`](label:service_handler) (`&8AB6`) after
the `'Bad ROM <slot>'` message, and from two other diagnostic
sites (`&8E2A`, `&9D3E`).""",
    on_entry={},
    on_exit={
        "a, x, y, p": "preserved (print_char_no_spool brackets the call with full register save/restore via PHA/PHP/PLP/PLA)"
    },
)


d.comment(0x9204, "A=&0D (CR) for OSASCI translation; fall through", align=Align.INLINE)
d.subroutine(
    0x9206,
    "print_char_no_spool",
    title="Print A via OSASCI, bypassing any open *SPOOL file",
    description="""Pushes the caller's flags, then forces `V=1` via the `BIT &9769`
/ `BVS` trick (`&9769` is a constant `&FF` byte in ROM). Saves
`X`, `Y`, `A` and a copy of the (now `V=1`) flags.

1. Calls OSBYTE `&C7` with `X=0`, `Y=0` to write `0` to the
   `*SPOOL` file handle, returning the previous handle in `X`.
2. If the previous handle was in the NFS-issued range
   `&21..&2F`, calls OSBYTE `&C7` again with `X=OLD`, `Y=0` to
   **restore** the spool *before* the print (so the print is
   captured); otherwise leaves spool closed for the duration of
   the print.
3. `PLP`s the inner `P`, then routes to OSASCI (the `BIT` trick
   set `V=1`, so the `BVC` at `&9229` is not taken).
4. Final OSBYTE `&C7` with `Y=&FF` either no-ops (if spool
   already restored) or writes `OLD` back (if it was deferred).
5. Pulls `A`, `Y`, `X`, `P` and returns.

Eight inner-ROM callers: `&9268`, `&92AD`, `&9D30`, `&9D5A`,
`&B21F`, `&B2FB`, `&B321`, `&B77D`.""",
    on_entry={"a": "byte to print as ASCII char (CR is translated by OSASCI)"},
)


d.comment(0x9206, "Save caller's flags (V from caller is irrelevant — see &91FC)", align=Align.INLINE)
d.comment(0x9207, "Unconditionally sets V=1 (bit 6 of operand &FF)", align=Align.INLINE)
d.comment(0x920A, "V=1 always, branch always taken (skips the CLV path)", align=Align.INLINE)
d.subroutine(
    0x920C,
    "print_byte_no_spool",
    title="Print A via OSWRCH (raw, no CR translation), bypass *SPOOL",
    description="""As [`print_char_no_spool`](label:print_char_no_spool) but the inner
`PHP`/`CLV` at `&9201` forces `V=0` in the saved flags, so the
`BVC` at `&9229` takes the `OSWRCH` branch instead of `OSASCI`.

Used when the caller wants to emit a raw byte (e.g. a VDU
control code) without `CR` translation. Sole caller in this ROM
is at `&8DE8`.""",
    on_entry={"a": "raw byte to print via OSWRCH"},
)


d.comment(0x920C, "Alt entry: save caller's flags BEFORE forcing V=0", align=Align.INLINE)
d.comment(0x920D, "Force V=0 -> OSWRCH path at &9229 (raw byte)", align=Align.INLINE)
d.label(0x920E, "save_regs_print_no_spool")

d.comment(0x920E, "Save X", align=Align.INLINE)
d.comment(0x920F, "Save Y", align=Align.INLINE)
d.comment(0x9210, "Save A (the byte to print)", align=Align.INLINE)
d.comment(0x9211, "Save inner P — V here picks OSASCI vs OSWRCH later", align=Align.INLINE)
d.comment(0x9212, "OSBYTE 199 (read/write *SPOOL file handle)", align=Align.INLINE)
d.comment(0x9214, "X=0: handle value to write", align=Align.INLINE)
d.comment(0x9216, "Y=0: write mode (NEW = (OLD AND 0) EOR X = X = 0)", align=Align.INLINE)
d.comment(0x9218, "Closes spool; X returns OLD handle", align=Align.INLINE)
d.comment(0x921B, "OLD < ' '? (likely 0 = was already closed)", align=Align.INLINE)
d.comment(0x921D, "Yes: leave spool closed for the print", align=Align.INLINE)
d.comment(0x921F, "OLD >= '0'?", align=Align.INLINE)
d.comment(0x9221, "Yes (>= &30): leave spool closed", align=Align.INLINE)
d.comment(0x9223, "OLD in [&20,&2F] (NFS handle range): re-open spool with X=OLD", align=Align.INLINE)
d.comment(0x9226, "Clear X for the post-print restore", align=Align.INLINE)
d.label(0x9228, "do_print_no_spool")

d.comment(0x9228, "Restore inner P (V=1 OSASCI / V=0 OSWRCH)", align=Align.INLINE)
d.comment(0x9229, "Pull A (the byte)", align=Align.INLINE)
d.comment(0x922A, "Push it back so the final epilogue PLA still works", align=Align.INLINE)
d.comment(0x922B, "V=0 -> OSWRCH (raw); V=1 -> OSASCI (CR translation)", align=Align.INLINE)
d.comment(0x922D, "OSASCI: writes A, translating CR to CR/LF", align=Align.INLINE)
d.comment(0x9230, "Skip OSWRCH branch", align=Align.INLINE)
d.label(0x9232, "print_via_oswrch")

d.comment(0x9232, "OSWRCH: writes A as a raw byte", align=Align.INLINE)
d.label(0x9235, "restore_spool_and_return")

d.comment(0x9235, "OSBYTE 199 again to restore spool state", align=Align.INLINE)
d.comment(0x9237, "Y=&FF (read mode): NEW = OLD EOR X", align=Align.INLINE)
d.comment(0x9239, "X=0 -> no change; X=OLD -> writes OLD back", align=Align.INLINE)
d.comment(0x923C, "Pull A (preserved across the call)", align=Align.INLINE)
d.comment(0x923D, "Pull Y", align=Align.INLINE)
d.comment(0x923E, "Pull X", align=Align.INLINE)
d.comment(0x923F, "Pull caller's original flags", align=Align.INLINE)
d.comment(0x9240, "Return", align=Align.INLINE)
d.label(0x9241, "print_hex_byte")

d.subroutine(
    0x9241,
    "print_hex_byte",
    title="Print A as two hexadecimal digits",
    description="""Saves `A` on the stack, shifts right four times to isolate the
high nybble, calls [`print_hex_nybble`](label:print_hex_nybble) to
print it, then restores the full byte and falls through to
[`print_hex_nybble`](label:print_hex_nybble) for the low nybble.

Callers: `print_5_hex_bytes`, [`cmd_ex`](label:cmd_ex),
[`cmd_dump`](label:cmd_dump), and `print_dump_header`.""",
    on_entry={"a": "byte to print"},
    on_exit={"a": "original byte value"},
)


d.comment(0x9241, "Save full byte", align=Align.INLINE)
d.comment(0x9242, "Shift high nybble to low", align=Align.INLINE)
d.comment(0x9243, "Continue shifting", align=Align.INLINE)
d.comment(0x9244, "Continue shifting", align=Align.INLINE)
d.comment(0x9245, "High nybble now in bits 0-3", align=Align.INLINE)
d.comment(0x9246, "Print high nybble as hex digit", align=Align.INLINE)
d.comment(0x9249, "Restore full byte", align=Align.INLINE)
d.label(0x924A, "print_hex_nybble")

d.subroutine(
    0x924A,
    "print_hex_nybble",
    title="Print low nybble of A as hex digit",
    description="""Masks `A` to the low 4 bits, then converts to ASCII:

1. Adds 7 for letters `A`..`F` (via `ADC #6` with carry set from
   the `CMP`).
2. `ADC #&30` for the final `'0'`..`'F'` character.
3. Outputs via `JMP OSASCI`.""",
    on_entry={"a": "value (low nybble used)"},
)


d.comment(0x924A, "Mask to low nybble", align=Align.INLINE)
d.comment(0x924C, "Digit >= &0A?", align=Align.INLINE)
d.comment(0x924E, "No: skip letter adjustment", align=Align.INLINE)
d.comment(0x9250, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.label(0x9252, "add_ascii_base")

d.comment(0x9252, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.subroutine(
    0x9257,
    "print_hex_byte_no_spool",
    title="Print A as two hex digits, *SPOOL-bypassing",
    description="""As [`print_hex_byte`](label:print_hex_byte) but emits each digit via
[`print_char_no_spool`](label:print_char_no_spool) (the *SPOOL-bypassing OSASCI
wrapper), so the digits don't appear in any active spool capture.
Saves `A`, extracts the high nibble (`LSR` x4), prints it via
[`print_hex_nybble_no_spool`](label:print_hex_nybble_no_spool), then restores `A` and
falls through for the low nibble. Sole caller:
[`print_5_hex_bytes`](label:print_5_hex_bytes) at `&9D51`.""",
    on_entry={"a": "byte to print"},
    on_exit={"a": "preserved"},
)


d.comment(0x9257, "Save full byte", align=Align.INLINE)
d.comment(0x9258, "Shift high nybble to low (LSR x4)", align=Align.INLINE)
d.comment(0x9259, "LSR / LSR / LSR -- shift hi nibble down to lo", align=Align.INLINE)
d.comment(0x925A, "(continued)", align=Align.INLINE)
d.comment(0x925B, "(continued)", align=Align.INLINE)
d.comment(0x925C, "Print high nybble as hex digit", align=Align.INLINE)
d.comment(0x925F, "Restore full byte; fall through for low nybble", align=Align.INLINE)
d.subroutine(
    0x9260,
    "print_hex_nybble_no_spool",
    title="Print low nybble of A as one hex digit, *SPOOL-bypassing",
    description="As print_hex_nybble (&923F) but emits via the print_char_no_spool tail-call instead of OSASCI directly, so the digit is not captured by any active *SPOOL file. Standard AND #&0F / CMP #&0A / +6-or-not / + #&30 mapping for hex digits 0-9 / A-F. Tail-jumps to print_char_no_spool via BRA.",
    on_entry={"a": "value (low nybble used)"},
)


d.comment(0x9260, "Mask to low nybble", align=Align.INLINE)
d.comment(0x9262, "Digit >= &0A?", align=Align.INLINE)
d.comment(0x9264, "No: skip letter adjustment", align=Align.INLINE)
d.comment(0x9266, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.label(0x9268, "print_nybble_leading_zero")

d.comment(0x9268, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.comment(0x926A, "Tail-jump to *SPOOL-bypassing print", align=Align.INLINE)
d.hook_subroutine(0x926C, "print_inline", stringhi_hook)
d.subroutine(
    0x926C,
    "print_inline",
    title="Print inline string, high-bit terminated",
    description="""Pops the return address from the stack, prints each byte via
`OSASCI` until a byte with bit 7 set is found, then jumps to that
address. The high-bit byte serves as both the string terminator
and the opcode of the first instruction after the string.

Common terminators:

| Byte | Opcode | Effect |
|---|---|---|
| `&EA` | `NOP`  | fall-through |
| `&B8` | `CLV`  | followed by `BVC` for an unconditional forward branch |""",
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)", "x": "corrupted (by OSASCI)", "y": "0"},
)


d.comment(0x926C, "Pop return address (low) — points to last byte of JSR", align=Align.INLINE)
d.comment(0x926D, "Store as fs_error_ptr (return-addr saved)", align=Align.INLINE)
d.comment(0x926F, "Pop return address (high)", align=Align.INLINE)
d.comment(0x9270, "Store as fs_crflag (entry flag)", align=Align.INLINE)
d.comment(0x9272, "Y=0: start scanning at offset 0", align=Align.INLINE)
d.label(0x9274, "loop_next_char")

d.subroutine(
    0x9274,
    "loop_next_char",
    title="print_inline pointer-advance step",
    description="""`INC fs_error_ptr` (lo); on overflow `INC fs_crflag` (hi). Single
caller (the loop tail at `&9284` inside
[`print_inline`](label:print_inline)). Falls through to `load_char`
which reads the next inline-string byte.""",
)


d.comment(0x9274, "Advance pointer to next character", align=Align.INLINE)
d.comment(0x9276, "Z clear: continue with this char", align=Align.INLINE)
d.comment(0x9278, "Z set (CR): increment fs_crflag", align=Align.INLINE)
d.label(0x927A, "load_char")

d.comment(0x927A, "Load next byte from inline string", align=Align.INLINE)
d.comment(0x927C, "Bit 7 set? Done — this byte is the next opcode", align=Align.INLINE)
d.comment(0x927E, "Read fs_error_ptr (saved across OSASCI)", align=Align.INLINE)
d.comment(0x9280, "Push it", align=Align.INLINE)
d.comment(0x9281, "Read fs_crflag", align=Align.INLINE)
d.comment(0x9283, "Push it", align=Align.INLINE)
d.comment(0x9284, "Reload character (pointer may have been clobbered)", align=Align.INLINE)
d.comment(0x9286, "Print character via OSASCI", align=Align.INLINE)
d.comment(0x9289, "Pop saved fs_crflag", align=Align.INLINE)
d.comment(0x928A, "Restore fs_crflag", align=Align.INLINE)
d.comment(0x928C, "Pop saved fs_error_ptr", align=Align.INLINE)
d.comment(0x928D, "Restore fs_error_ptr", align=Align.INLINE)
d.comment(0x928F, "Loop back", align=Align.INLINE)
d.label(0x9292, "resume_caller")

d.comment(0x9292, "Jump to address of high-bit byte (resumes code)", align=Align.INLINE)


d.hook_subroutine(0x9295, "print_inline_no_spool", stringhi_hook)
d.subroutine(
    0x9295,
    "print_inline_no_spool",
    title="Print inline string, high-bit terminated, *SPOOL-bypassing",
    description="""As [`print_inline`](label:print_inline), but each character is
emitted via [`print_char_no_spool`](label:print_char_no_spool) instead of
`OSASCI` directly, so the printed text does not appear in any
active `*SPOOL` capture.

Used by status output that should not be saved to a spool file
(e.g. `*Wipe` `'(Y/N) '` prompts, `*Ex` column separators, the
`'Bad ROM'` service-handler message via the
`recv_and_process_reply` `'Data Lost'` warning, and inline-string
arguments inside [`cmd_ex`](label:cmd_ex)'s directory
listing).

Six callers: `&9818` (`recv_and_process_reply`), `&B18D`/`&B197`
([`cmd_ex`](label:cmd_ex)), `&B323` (`ex_print_col_sep`),
`&B787` ([`cmd_wipe`](label:cmd_wipe)), `&B7CB`
(`prompt_yn`).""",
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)", "x": "corrupted (by print_char_no_spool)", "y": "0"},
)
d.comment(0x9295, "Pop return-addr low byte (-> string pointer low)", align=Align.INLINE)
d.comment(0x9296, "Save in fs_error_ptr (the loop's pointer low)", align=Align.INLINE)
d.comment(0x9298, "Pop return-addr high byte", align=Align.INLINE)
d.comment(0x9299, "Save in fs_crflag (the loop's pointer high)", align=Align.INLINE)
d.comment(0x929B, "Y=0: indirect index for (fs_error_ptr),Y", align=Align.INLINE)
d.label(0x929D, "loop_print_inline_string")


d.comment(0x929D, "Step pointer low byte to next char", align=Align.INLINE)
d.comment(0x929F, "No carry: skip high-byte INC", align=Align.INLINE)
d.comment(0x92A1, "Page wrap: bump pointer high", align=Align.INLINE)
d.label(0x92A3, "print_next_string_char")

d.comment(0x92A3, "Read next character from inline string", align=Align.INLINE)
d.comment(0x92A5, "Bit 7 set: terminator -- this byte is the next opcode", align=Align.INLINE)
d.comment(0x92A7, "Save pointer low (print_char_no_spool may clobber)", align=Align.INLINE)
d.comment(0x92A9, "Push it", align=Align.INLINE)
d.comment(0x92AA, "Save pointer high", align=Align.INLINE)
d.comment(0x92AC, "Push it", align=Align.INLINE)
d.comment(0x92AD, "Reload the character we're about to print", align=Align.INLINE)
d.comment(0x92AF, "Print it via the *SPOOL-bypassing OSASCI wrapper", align=Align.INLINE)
d.comment(0x92B2, "Pop pointer high back", align=Align.INLINE)
d.comment(0x92B3, "Restore", align=Align.INLINE)
d.comment(0x92B5, "Pop pointer low back", align=Align.INLINE)
d.comment(0x92B6, "Restore", align=Align.INLINE)
d.comment(0x92B8, "Always taken (BRA-style; A is non-zero from print)", align=Align.INLINE)
d.label(0x92BA, "print_char_terminator")

d.comment(
    0x92BA, "Resume execution at the terminator byte's address (JMP indirect via fs_error_ptr)", align=Align.INLINE
)
d.subroutine(
    0x92BD,
    "parse_addr_arg",
    title="Parse decimal or hex station address argument",
    description="""Reads characters from the command argument at `(fs_crc_lo),Y`.
Supports `&` prefix for hex, `.` separator for net.station
addresses, and plain decimal. Returns the result in `fs_load_addr_2`
(and `A`). Raises [`Bad hex`](address:934A), `Bad number`,
[`Bad station number`](address:9360), and overflow errors as
appropriate. The body uses the standard 6502 idioms: `ASL ASL ASL
ASL` + `ADC` for hex-digit accumulation, and `result*2 + result*8`
for decimal `*10`. Two named callers: from `&A3C9` and `&A3F2`.""",
    on_entry={"y": "index into command-string buffer at (fs_crc_lo),Y", "a": "ignored"},
    on_exit={"c": "set if a number was parsed"},
)


d.comment(0x92BD, "Zero the accumulator (fs_load_addr_2)", align=Align.INLINE)
d.comment(0x92BF, "Read first command-line byte", align=Align.INLINE)
d.comment(0x92C1, "Hex prefix '&'?", align=Align.INLINE)
d.comment(0x92C3, "No: try decimal path", align=Align.INLINE)
d.comment(0x92C5, "Yes: skip the '&'", align=Align.INLINE)
d.comment(0x92C6, "Read first hex digit", align=Align.INLINE)
d.comment(0x92C8, "Always taken (CMP #'&' set C if A>='&'); jump into the hex digit-range check", align=Align.INLINE)
d.label(0x92CA, "next_hex_char")

d.comment(0x92CA, "Step to next character", align=Align.INLINE)
d.comment(0x92CB, "Read next hex digit candidate", align=Align.INLINE)
d.comment(0x92CD, "Dot? Net.station separator", align=Align.INLINE)
d.comment(0x92CF, "Yes: switch to station-parsing mode", align=Align.INLINE)
d.comment(0x92D1, "Below '!' (CR/space)? End of argument", align=Align.INLINE)
d.comment(0x92D3, "Yes: number complete", align=Align.INLINE)
d.label(0x92D5, "check_digit_range")

d.comment(0x92D5, "Below '0'?", align=Align.INLINE)
d.comment(0x92D7, "Yes: not a hex digit", align=Align.INLINE)
d.comment(0x92D9, "Above '9'? (CMP #':')", align=Align.INLINE)
d.comment(0x92DB, "No (it's '0'-'9'): straight to digit extraction", align=Align.INLINE)
d.comment(0x92DD, "Force uppercase via AND #&5F", align=Align.INLINE)
d.comment(0x92DF, "Map 'A'-'F' to &FA-&FF (ADC #&B8 with C from earlier CMP #':' which set C)", align=Align.INLINE)
d.comment(0x92E1, "Carry out of ADC: was below 'A' -- bad hex", align=Align.INLINE)
d.comment(0x92E3, "Below &FA? (digit > 'F' overflowed past)", align=Align.INLINE)
d.label(0x92E5, "skip_if_not_hex")

d.comment(0x92E5, "Yes: bad hex (out of [&FA,&FF])", align=Align.INLINE)
d.label(0x92E7, "extract_digit_value")

d.comment(0x92E7, "Mask to nibble", align=Align.INLINE)
d.comment(0x92E9, "Stash digit value in fs_load_addr_3", align=Align.INLINE)
d.comment(0x92EB, "Load accumulator", align=Align.INLINE)
d.comment(0x92ED, "Above 16? (would overflow when shifted left 4)", align=Align.INLINE)
d.comment(0x92EF, "Yes: overflow", align=Align.INLINE)
d.comment(0x92F1, "Shift accumulator left 4 (multiply by 16)", align=Align.INLINE)
d.comment(0x92F2, "(shift 2)", align=Align.INLINE)
d.comment(0x92F3, "(shift 3)", align=Align.INLINE)
d.comment(0x92F4, "(shift 4)", align=Align.INLINE)
d.comment(0x92F5, "Add new nibble", align=Align.INLINE)
d.comment(0x92F7, "Save updated accumulator", align=Align.INLINE)
d.comment(0x92F9, "No carry: continue (always taken since accumulator was checked < 16 above)", align=Align.INLINE)
d.label(0x92FB, "next_dec_char")

d.comment(0x92FB, "Read next decimal-digit candidate", align=Align.INLINE)
d.comment(0x92FD, "Dot? Net.station separator", align=Align.INLINE)
d.comment(0x92FF, "Yes: switch to station-parsing mode", align=Align.INLINE)
d.comment(0x9301, "Below '!' (CR/space)?", align=Align.INLINE)
d.comment(0x9303, "Yes: number complete", align=Align.INLINE)
d.comment(0x9305, "Test for '0'-'9' and reject '&'/'.'", align=Align.INLINE)
d.comment(0x9308, "Not a decimal digit: bad number", align=Align.INLINE)
d.comment(0x930A, "Mask to nibble", align=Align.INLINE)
d.comment(0x930C, "Stash digit", align=Align.INLINE)
d.comment(0x930E, "Accumulator * 2", align=Align.INLINE)
d.comment(0x9310, "Overflowed: too big for byte", align=Align.INLINE)
d.comment(0x9312, "Reload doubled value", align=Align.INLINE)
d.comment(0x9314, "* 2 again (now * 4)", align=Align.INLINE)
d.comment(0x9315, "Overflow check", align=Align.INLINE)
d.comment(0x9317, "* 2 again (now * 8)", align=Align.INLINE)
d.comment(0x9318, "Overflow check", align=Align.INLINE)
d.comment(0x931A, "+ accumulator (now * 8 + * 2 = * 10)", align=Align.INLINE)
d.comment(0x931C, "Overflow check", align=Align.INLINE)
d.comment(0x931E, "+ new digit", align=Align.INLINE)
d.comment(0x9320, "Overflow check", align=Align.INLINE)
d.comment(0x9322, "Save * 10 + digit", align=Align.INLINE)
d.comment(0x9324, "Step input cursor", align=Align.INLINE)
d.comment(0x9325, "Always taken (Y wraps at 256, never zero in practice)", align=Align.INLINE)
d.label(0x9327, "done_parse_num")

d.comment(0x9327, "Read mode flag", align=Align.INLINE)
d.comment(0x9329, "Bit 7 clear: in net.station mode -- validate result", align=Align.INLINE)
d.comment(0x932B, "Decimal-only mode: get result", align=Align.INLINE)
d.comment(0x932D, "Result is zero: bad parameter", align=Align.INLINE)
d.comment(0x932F, "Return with parsed result in A (decimal-only path)", align=Align.INLINE)
d.label(0x9330, "validate_station")

d.comment(0x9330, "Reload result", align=Align.INLINE)
d.comment(0x9332, "Station 255 is reserved (broadcast)", align=Align.INLINE)
d.comment(0x9334, "Yes: bad station number", align=Align.INLINE)
d.comment(0x9336, "Reload result for the next test", align=Align.INLINE)
d.comment(0x9338, "Non-zero: valid station, return", align=Align.INLINE)
d.comment(0x933A, "Zero result: must have followed a dot to be valid", align=Align.INLINE)
d.comment(0x933C, "No dot was seen: bad station number", align=Align.INLINE)
d.comment(0x933E, "Dot seen: peek the byte before current cursor", align=Align.INLINE)
d.comment(0x933F, "Read previous byte", align=Align.INLINE)
d.comment(0x9341, "Restore Y", align=Align.INLINE)
d.comment(0x9342, "Was previous char '.'?", align=Align.INLINE)
d.comment(0x9344, "No: bad station number", align=Align.INLINE)
d.label(0x9346, "return_parsed")

d.comment(0x9346, "All checks passed: C=1 marks 'parsed successfully'", align=Align.INLINE)
d.comment(0x9347, "Return", align=Align.INLINE)
d.label(0x9348, "handle_dot_sep")

d.comment(0x9348, "Dot already seen?", align=Align.INLINE)
d.comment(0x934A, "Yes: 'Bad number' (multiple dots)", align=Align.INLINE)
d.comment(0x934C, "Set dot-seen flag", align=Align.INLINE)
d.comment(0x934E, "Get parsed network number (before dot)", align=Align.INLINE)
d.comment(0x9350, "Network 255 is reserved", align=Align.INLINE)
d.comment(0x9352, "Yes: 'Bad network number'", align=Align.INLINE)
d.comment(0x9354, "Return; caller continues parsing the station", align=Align.INLINE)
d.label(0x9355, "err_bad_hex")

d.subroutine(
    0x9355,
    "err_bad_hex",
    title="Raise 'Bad hex' BRK error",
    description="""Loads error code `&F1` and tail-calls `error_bad_inline` with
the inline string `'hex'` – `error_bad_inline` prepends `'Bad '`
to produce the final `'Bad hex'` message. Called from
[`parse_addr_arg`](label:parse_addr_arg) and the `*DUMP` / `*LIST`
hex parsers when a digit is out of range. Never returns.""",
)


d.comment(0x9355, "Error code &F1", align=Align.INLINE)
d.comment(0x9357, "Raise 'Bad hex' error", align=Align.INLINE)
d.label(0x935E, "error_overflow")

d.comment(0x935E, "Test fs_work_4 bit 7", align=Align.INLINE)
d.comment(0x9360, "Bit 7 set: redirect to error_bad_param", align=Align.INLINE)
d.label(0x9362, "err_bad_station_num")

d.comment(0x9362, "A=&D0: 'Bad station' error code", align=Align.INLINE)
d.comment(0x9364, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x9376, "error_bad_number")

d.comment(0x9376, "A=&F0: 'Bad number' error code", align=Align.INLINE)
d.comment(0x9378, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x9382, "error_bad_param")

d.comment(0x9382, "A=&94: 'Bad parameter' error code", align=Align.INLINE)
d.comment(0x9384, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x9391, "error_bad_net_num")

d.comment(0x9391, "A=&D1: 'Bad net number' error code", align=Align.INLINE)
d.comment(0x9393, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x93A1, "is_decimal_digit")

d.subroutine(
    0x93A1,
    "is_decimal_digit",
    title="Test for digit, '&', or '.' separator",
    description="""Compares `A` against `'&'` and `'.'` first; if either matches,
returns with carry set via the shared `rts_digit_test` exit.
Otherwise falls through to
[`is_dec_digit_only`](label:is_dec_digit_only) for the `'0'`..`'9'`
range test.

Called by [`cmd_iam`](label:cmd_iam),
[`cmd_ps`](label:cmd_ps), and
[`cmd_pollps`](label:cmd_pollps) when parsing station
addresses.""",
    on_entry={"a": "character to test"},
    on_exit={"c": "set if digit/&/., clear otherwise"},
)


d.comment(0x93A1, "Hex prefix '&'?", align=Align.INLINE)
d.comment(0x93A3, "Yes: treat as digit-like (carry set on exit)", align=Align.INLINE)
d.comment(0x93A5, "Network/station separator '.'?", align=Align.INLINE)
d.comment(0x93A7, "Yes: also digit-like; else fall through to decimal test", align=Align.INLINE)
d.label(0x93A9, "is_dec_digit_only")

d.subroutine(
    0x93A9,
    "is_dec_digit_only",
    title="Test for decimal digit '0'..'9'",
    description="""Uses two `CMP`s to bracket-test `A` against the range
`&30..&39`:

1. `CMP #&3A` sets carry if `A >= ':'` (above digits).
2. `CMP #&30` sets carry if `A >= '0'`.

The net effect: carry set only for `'0'..'9'`. Called by
[`parse_addr_arg`](label:parse_addr_arg).""",
    on_entry={"a": "character to test"},
    on_exit={"c": "set if '0'-'9', clear otherwise"},
)


d.comment(0x93A9, "Above '9'? (CMP #':')", align=Align.INLINE)
d.comment(0x93AB, "Yes: not a digit -- jump to clear-carry exit", align=Align.INLINE)
d.comment(0x93AD, "Below '0'? (CMP sets carry if A >= '0')", align=Align.INLINE)
d.label(0x93AF, "rts_digit_test")

d.comment(0x93AF, "Carry now reflects '0'-'9' membership; return", align=Align.INLINE)
d.label(0x93B0, "not_a_digit")

d.comment(0x93B0, "Out-of-range exit: clear carry to signal not-a-digit", align=Align.INLINE)
d.comment(0x93B1, "Return", align=Align.INLINE)
d.label(0x93B2, "get_access_bits")

d.subroutine(
    0x93B2,
    "get_access_bits",
    title="Read and encode directory entry access byte",
    description="""Loads the access byte from offset &0E of the directory entry via
`(fs_options),Y`, masks to 6 bits (`AND #&3F`), then sets `X=4`
and branches to [`begin_prot_encode`](label:begin_prot_encode) to map through
[`prot_bit_encode_table`](label:prot_bit_encode_table). Called by
[`check_and_setup_txcb`](label:check_and_setup_txcb) for owner and public
access.""",
    on_exit={"a": "encoded access flags", "x": "&FF + bits-set (left in this state by get_prot_bits fall-through)"},
)


d.comment(0x93B2, "Y=&0E: directory entry access byte offset", align=Align.INLINE)
d.comment(0x93B4, "Read access byte through fs_options pointer", align=Align.INLINE)
d.comment(0x93B6, "Mask to 6 protection bits (clears the unused top two)", align=Align.INLINE)
d.comment(0x93B8, "X=4: encode-table column index for owner-access bits", align=Align.INLINE)
d.comment(0x93BA, "Always taken: LDX #4 cleared Z, so BNE is unconditional", align=Align.INLINE)
d.label(0x93BC, "get_prot_bits")

d.subroutine(
    0x93BC,
    "get_prot_bits",
    title="Encode protection bits via lookup table",
    description="""Masks `A` to 5 bits (`AND #&1F`), sets `X=&FF` to start at table
index 0, then enters the shared encoding loop at
[`begin_prot_encode`](label:begin_prot_encode). Shifts out each source bit
and ORs in the corresponding value from
[`prot_bit_encode_table`](label:prot_bit_encode_table). Called by
[`send_txcb_swap_addrs`](label:send_txcb_swap_addrs) and
[`check_and_setup_txcb`](label:check_and_setup_txcb).""",
    on_entry={"a": "raw protection bits (low 5 used)"},
    on_exit={"a": "encoded protection flags"},
)


d.comment(0x93BC, "Mask to 5 protection bits (low 5)", align=Align.INLINE)
d.comment(0x93BE, "X=&FF; INX inside the loop bumps to 0 for column 0", align=Align.INLINE)
d.label(0x93C0, "begin_prot_encode")

d.comment(0x93C0, "Park source bits in fs_error_ptr -- the LSR target", align=Align.INLINE)
d.comment(0x93C2, "A=0: accumulator for encoded result", align=Align.INLINE)
d.label(0x93C4, "loop_encode_prot")

d.comment(0x93C4, "Advance table column index", align=Align.INLINE)
d.comment(0x93C5, "Shift next source bit into carry", align=Align.INLINE)
d.comment(0x93C7, "Source bit was 0: skip the OR for this column", align=Align.INLINE)
d.comment(0x93C9, "Source bit was 1: OR in this column's encoded mask", align=Align.INLINE)
d.label(0x93CC, "skip_clear_prot")


d.comment(
    0x93CC,
    "Continue while either fs_error_ptr or A is non-zero (loop ends when source exhausted and result still 0)",
    align=Align.INLINE,
)
d.comment(0x93CE, "Return with encoded value in A", align=Align.INLINE)
d.subroutine(
    0x93CF,
    "prot_bit_encode_table",
    title="Bit-permutation table for protection / access encoding",
    description="""11-byte lookup table used by [`get_prot_bits`](label:get_prot_bits) and
[`get_access_bits`](label:get_access_bits) to map source bits (the raw 5-bit
or 6-bit access mask read from the directory entry) into the FS
protocol's 8-bit protection-flag layout. The encoder loop at
[`begin_prot_encode`](label:begin_prot_encode) shifts each source bit out via
`LSR`; whenever the bit is 1 it ORs the corresponding entry into
the result, then advances `X`.

Two callers partition the table:

- [`get_prot_bits`](label:get_prot_bits) enters at index 0 with 5 source
  bits (raw protection mask, `AND #&1F`).
- [`get_access_bits`](label:get_access_bits) enters at index 5 with 6 source
  bits (directory access byte, `AND #&3F`).

| idx | caller            | src bit | mask  | output bits |
| --- | ----------------- | ------- | ----- | ----------- |
|   0 | `get_prot_bits`   |       0 | `&50` | 6, 4        |
|   1 | `get_prot_bits`   |       1 | `&20` | 5           |
|   2 | `get_prot_bits`   |       2 | `&05` | 2, 0        |
|   3 | `get_prot_bits`   |       3 | `&02` | 1           |
|   4 | `get_prot_bits`   |       4 | `&88` | 7, 3        |
|   5 | `get_access_bits` |       0 | `&04` | 2           |
|   6 | `get_access_bits` |       1 | `&08` | 3           |
|   7 | `get_access_bits` |       2 | `&80` | 7           |
|   8 | `get_access_bits` |       3 | `&10` | 4           |
|   9 | `get_access_bits` |       4 | `&01` | 0           |
|  10 | `get_access_bits` |       5 | `&02` | 1           |""",
)
for i in range(11):
    d.byte(0x93CF + i)
d.comment(0x93CF, "prot src bit 0 -> out bits 6,4", align=Align.INLINE)
d.comment(0x93D0, "prot src bit 1 -> out bit 5", align=Align.INLINE)
d.comment(0x93D1, "prot src bit 2 -> out bits 2,0", align=Align.INLINE)
d.comment(0x93D2, "prot src bit 3 -> out bit 1", align=Align.INLINE)
d.comment(0x93D3, "prot src bit 4 -> out bits 7,3", align=Align.INLINE)
d.comment(0x93D4, "access src bit 0 -> out bit 2", align=Align.INLINE)
d.comment(0x93D5, "access src bit 1 -> out bit 3", align=Align.INLINE)
d.comment(0x93D6, "access src bit 2 -> out bit 7", align=Align.INLINE)
d.comment(0x93D7, "access src bit 3 -> out bit 4", align=Align.INLINE)
d.comment(0x93D8, "access src bit 4 -> out bit 0", align=Align.INLINE)
d.comment(0x93D9, "access src bit 5 -> out bit 1", align=Align.INLINE)

d.label(0x93DA, "set_text_and_xfer_ptr")

d.subroutine(
    0x93DA,
    "set_text_and_xfer_ptr",
    title="Set OS text pointer then transfer parameters",
    description="""Stores `X`/`Y` into the MOS text pointer at `os_text_ptr` /
`os_text_ptr_hi` (`&F2`/`&F3`), then falls through to
[`set_xfer_params`](label:set_xfer_params) and
[`set_options_ptr`](label:set_options_ptr) to configure the full FS
transfer context. Two callers:
[`fscv_3_star_cmd`](label:fscv_3_star_cmd) (FSCV reason 3) and
[`ps_scan_resume`](label:ps_scan_resume) (PS scan tail).""",
    on_entry={"x": "text pointer low byte", "y": "text pointer high byte"},
)


d.comment(0x93DA, "Save text pointer low byte (where caller wants OS to scan from)", align=Align.INLINE)
d.comment(0x93DC, "Save text pointer high byte; fall through to set_xfer_params", align=Align.INLINE)
d.label(0x93DE, "set_xfer_params")

d.subroutine(
    0x93DE,
    "set_xfer_params",
    title="Set FS transfer byte count and source pointer",
    description="""Stores `A` into `fs_last_byte_flag` (`&BD`) as the transfer byte
count, and `X`/`Y` into `fs_crc_lo`/`hi` (`&BE`/`&BF`) as the
source-data pointer. Falls through to
[`set_options_ptr`](label:set_options_ptr) to complete the
transfer-context setup.

Called by 5 sites across [`cmd_ex`](label:cmd_ex),
`format_filename_field`, and `gsread_to_buf`.""",
    on_entry={"a": "transfer byte count", "x": "source pointer low", "y": "source pointer high"},
)


d.comment(0x93DE, "Stash transfer byte count (in A)", align=Align.INLINE)
d.comment(0x93E0, "Source pointer low byte", align=Align.INLINE)
d.comment(0x93E2, "Source pointer high byte; fall through to set_options_ptr", align=Align.INLINE)
d.label(0x93E4, "set_options_ptr")

d.subroutine(
    0x93E4,
    "set_options_ptr",
    title="Set FS options pointer and clear escape flag",
    description="""Stores `X`/`Y` into `fs_options`/`fs_block_offset` (`&BB`/`&BC`)
as the options-block pointer. Then enters
[`clear_escapable`](label:clear_escapable) which uses
`PHP`/`LSR`/`PLP` to clear bit 0 of the escape flag at `&97`
without disturbing processor flags.

Called by `format_filename_field` and `send_and_receive`.""",
    on_entry={"x": "options pointer low", "y": "options pointer high"},
)


d.comment(0x93E4, "Options pointer low byte (parameter block base)", align=Align.INLINE)
d.comment(0x93E6, "Options pointer high byte; fall through to clear_escapable", align=Align.INLINE)
d.label(0x93E8, "clear_escapable")

d.subroutine(
    0x93E8,
    "clear_escapable",
    title="Clear bit 0 of need_release_tube preserving flags",
    description="""PHP / LSR need_release_tube / PLP / RTS. Shifts bit 0 of
need_release_tube into carry while clearing it, then restores the
caller's flags so the operation is invisible to NZC-sensitive
code. Single caller (&9B70 in the recv-and-classify reply path).""",
)


d.comment(0x93E8, "Save flags so the LSR doesn't disturb caller's NZC", align=Align.INLINE)
d.comment(0x93E9, "Shift bit 0 of need_release_tube into carry, clearing the bit", align=Align.INLINE)
d.comment(0x93EB, "Restore caller's flags", align=Align.INLINE)
d.comment(0x93EC, "Return", align=Align.INLINE)
d.label(0x93ED, "cmp_5byte_handle")

d.subroutine(
    0x93ED,
    "cmp_5byte_handle",
    title="Compare 5-byte handle buffers for equality",
    description="""Loops `X` from 4 down to 1, comparing each byte of
`addr_work+X` with `fs_load_addr_3+X` using `EOR`. Returns on
the first mismatch (`Z=0`) or after all 5 bytes match (`Z=1`).

Called by `send_txcb_swap_addrs` and `check_and_setup_txcb` to
verify station/handle identity.""",
    on_exit={
        "z": "set if bytes 1..4 match (byte 0 is not compared)",
        "a": "EOR of last compared bytes",
        "x": "0 if all matched, else mismatch index",
    },
)


d.comment(0x93ED, "X=4: loop from offset 4 down to 1 (skips offset 0)", align=Align.INLINE)
d.label(0x93EF, "loop_cmp_handle")

d.comment(0x93EF, "Load saved-handle byte from addr_work[X]", align=Align.INLINE)
d.comment(0x93F1, "EOR with parsed handle byte; Z set iff bytes match", align=Align.INLINE)
d.comment(0x93F3, "Mismatch: bail out with Z clear", align=Align.INLINE)
d.comment(0x93F5, "Decrement to next byte", align=Align.INLINE)
d.comment(0x93F6, "Loop while X != 0 (offset 0 is intentionally not compared)", align=Align.INLINE)
d.label(0x93F8, "rts_cmp_handle")

d.comment(0x93F8, "Return; Z reflects last EOR (set = match, clear = mismatch)", align=Align.INLINE)
d.label(0x93F9, "fscv_7_read_handles")

d.subroutine(
    0x93F9,
    "fscv_7_read_handles",
    title="FSCV reason 7: report FCB handle range",
    description="""Returns the FCB handle range to the caller: `X=&20` (lowest valid
handle) and `Y=&2F` (highest valid handle), then `RTS`. Reached
via the FSCV vector with reason code 7. Used by the OS to discover
which handle values this filing system claims.""",
    on_exit={"x": "&20 (first valid FCB handle)", "y": "&2F (last valid FCB handle)"},
)


d.comment(0x93F9, "X=&20: handle-table base offset", align=Align.INLINE)
d.entry(0x93F9)
d.comment(0x93FB, "Y=&2F: handle count + flag", align=Align.INLINE)
d.comment(0x93FD, "Return", align=Align.INLINE)
d.label(0x93FE, "set_conn_active")

d.subroutine(
    0x93FE,
    "set_conn_active",
    title="Set connection-active flag in channel table",
    description="""Saves registers on the stack, recovers the original `A` from the
stack via `TSX`/`LDA &0102,X`, then calls `attr_to_chan_index` to
find the channel slot. `ORA`s bit 6 (`&40`) into the channel
status byte at [`hazel_fcb_status`](label:hazel_fcb_status)`+X`.
Preserves `A`, `X`, and processor flags via
`PHP`/`PHA`/`PLA`/`PLP`.

Called by `format_filename_field` and `adjust_fsopts_4bytes`.""",
    on_entry={"a": "channel attribute byte"},
)


d.comment(0x93FE, "Save flags so the rest of the routine is transparent", align=Align.INLINE)
d.entry(0x93FE)
d.comment(0x93FF, "Save A (the attribute byte we need to recover via stack)", align=Align.INLINE)
d.comment(0x9400, "Save X", align=Align.INLINE)
d.comment(0x9401, "Capture S into X to address stack from below", align=Align.INLINE)
d.comment(0x9402, "Re-read the original A from stack[X+2] (above PHX/PHA)", align=Align.INLINE)
d.comment(0x9405, "Convert attribute byte to channel-table index", align=Align.INLINE)
d.comment(0x9408, "No matching channel: skip the flag set, just restore", align=Align.INLINE)
d.comment(0x940A, "A=&40: bit 6 = connection-active mask", align=Align.INLINE)
d.comment(0x940C, "OR with current status byte for this channel", align=Align.INLINE)
d.comment(0x940F, "Write back the updated status", align=Align.INLINE)
d.comment(0x9412, "Always taken (A is non-zero after the OR with &40); join shared exit", align=Align.INLINE)
d.label(0x9414, "clear_conn_active")

d.subroutine(
    0x9414,
    "clear_conn_active",
    title="Clear connection-active flag in channel table",
    description="""Mirror of [`set_conn_active`](label:set_conn_active) but `AND`s the
channel status byte with `&BF` (bit-6 clear mask) instead of
`ORA`ing. Uses the same register-preservation pattern:
`PHP`/`PHA`/`TSX` to recover `A`, then `attr_to_chan_index` to
find the slot. Shares the `done_conn_flag` exit with
[`set_conn_active`](label:set_conn_active).""",
    on_entry={"a": "channel attribute byte"},
)


d.comment(0x9414, "Save flags", align=Align.INLINE)
d.comment(0x9415, "Save A", align=Align.INLINE)
d.comment(0x9416, "Save X", align=Align.INLINE)
d.comment(0x9417, "Capture S into X for stack-relative reads", align=Align.INLINE)
d.comment(0x9418, "Re-read the attribute byte from stack[X+2]", align=Align.INLINE)
d.comment(0x941B, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0x941E, "No matching channel: just restore", align=Align.INLINE)
d.comment(0x9420, "A=&BF: bit 6 clear mask", align=Align.INLINE)
d.comment(0x9425, "Write back the updated status", align=Align.INLINE)
d.comment(0x9428, "Restore X (saved at PHX)", align=Align.INLINE)
d.label(0x9428, "clear_channel_flag")

d.comment(0x9429, "Restore A", align=Align.INLINE)
d.comment(0x942A, "Restore flags", align=Align.INLINE)
d.comment(0x942B, "Return; A and X preserved across the call", align=Align.INLINE)
d.entry(0x942C)
d.label(0x942C, "cmd_fs_operation")

d.subroutine(
    0x942C,
    "cmd_fs_operation",
    title="Shared *Access / *Delete / *Info / *Lib command handler",
    description="""Copies the command name to the TX buffer, parses a quoted
filename argument via [`parse_quoted_arg`](label:parse_quoted_arg), and
checks the access prefix. Validates the filename does not start
with `'&'`, then falls through to
[`read_filename_char`](label:read_filename_char) to copy remaining
characters and send the request. Raises
[`Bad file name`](address:943C) if a bare `CR` is found where
a filename was expected.""",
    on_entry={
        "y": "command line offset in text pointer",
        "x": "byte offset within cmd_table_fs identifying which of the four shared commands was matched (Access, Delete, Info, or Lib)",
    },
)


d.comment(0x942C, "Copy command name 'Access'/'Delete'/'Info'/'Lib' to TX buffer", align=Align.INLINE)
d.comment(0x9430, "Parse quoted filename argument from command line", align=Align.INLINE)
d.comment(0x9433, "Parse the access prefix (e.g. L,W,R) into a bitmask", align=Align.INLINE)
d.comment(0x9437, "Reject '&' character in filename", align=Align.INLINE)
d.comment(0x943A, "End of line?", align=Align.INLINE)
d.comment(0x943C, "No: copy filename chars to buffer", align=Align.INLINE)
d.label(0x943E, "error_bad_filename")

d.subroutine(
    0x943E,
    "error_bad_filename",
    title="Raise 'Bad file name' BRK error",
    description="""Loads error code `&CC` and tail-calls `error_bad_inline` with
the inline string `'file name'` – `error_bad_inline` prepends
`'Bad '` to produce the final `'Bad file name'` message. Used
by [`check_not_ampersand`](label:check_not_ampersand) and other filename
validators. Never returns.""",
)


d.comment(0x943E, "Error number &CC", align=Align.INLINE)
d.comment(0x9440, "Raise 'Bad file name' error", align=Align.INLINE)
d.label(0x944D, "check_not_ampersand")

d.subroutine(
    0x944D,
    "check_not_ampersand",
    title="Reject '&' as filename character",
    description="""Loads the first character from the parse buffer at `&0E30` and
compares with `'&'` (`&26`). Branches to
[`error_bad_filename`](label:error_bad_filename) if matched, otherwise
returns.

Also contains [`read_filename_char`](label:read_filename_char) which
loops reading characters from the command line into the TX
buffer at `hazel_txcb_data` (`&C105`), calling
`strip_token_prefix` on each byte and terminating on `CR`. Used
by [`cmd_fs_operation`](label:cmd_fs_operation) and
[`cmd_rename`](label:cmd_rename).""",
    on_exit={"a": "first byte of parse buffer (preserved unchanged on the non-error path)"},
)


d.comment(0x944D, "Load first parsed character", align=Align.INLINE)
d.comment(0x9450, "Is it '&'?", align=Align.INLINE)
d.comment(0x9452, "Yes: invalid filename", align=Align.INLINE)
d.comment(0x9454, "Return", align=Align.INLINE)
d.label(0x9455, "read_filename_char")

d.subroutine(
    0x9455,
    "read_filename_char",
    title="Loop reading filename chars into TX buffer",
    description="""Per-character loop body of the filename-copy logic in
[`check_not_ampersand`](label:check_not_ampersand):

1. `JSR` to [`check_not_ampersand`](label:check_not_ampersand) to reject `'&'`.
2. Store the byte at [`hazel_txcb_data`](label:hazel_txcb_data)`+X`
   (TX buffer area).
3. Increment `X`.
4. Branch to [`send_fs_request`](label:send_fs_request) on `CR`, or
   strip a BASIC token prefix via `strip_token_prefix` and
   re-enter the loop.

Three callers: the loop's own `BRA` at `&945C`, plus `&9437`
([`cmd_rename`](label:cmd_rename)'s first-arg copy) and `&950F`
([`cmd_fs_operation`](label:cmd_fs_operation)'s filename pickup).""",
    on_entry={"a": "current character to copy", "x": "TX-buffer write index"},
    on_exit={"x": "advanced past the CR terminator"},
)


d.comment(0x9455, "Reject '&' in current char", align=Align.INLINE)
d.comment(0x9458, "Store character in TX buffer", align=Align.INLINE)
d.comment(0x945B, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x945C, "End of line?", align=Align.INLINE)
d.comment(0x945E, "Yes: send request to file server", align=Align.INLINE)
d.comment(0x9460, "Strip BASIC token prefix byte", align=Align.INLINE)
d.comment(0x9463, "BRA back to read_filename_char", align=Align.INLINE)
d.label(0x9465, "send_fs_request")

d.subroutine(
    0x9465,
    "send_fs_request",
    title="Send FS command with no extra dispatch offset",
    description="""Loads `Y=0` (so dispatch lookups don't add an offset) and
tail-jumps to [`send_cmd_and_dispatch`](label:send_cmd_and_dispatch). Two
callers: [`read_filename_char`](label:read_filename_char)'s `BEQ` on
`CR` (`&945C`) and the `*RUN` argument-handling tail at
`&953C`.""",
)


d.comment(0x9465, "Y=0: ensure offset starts from beginning of TX command buffer", align=Align.INLINE)
d.comment(0x9467, "Send the FS command and dispatch the reply", align=Align.INLINE)
d.subroutine(
    0x946A,
    "copy_fs_cmd_name",
    title="Copy matched command name to TX buffer",
    description="""Scans backwards in `cmd_table_fs` from the current position to find
the bit-7 flag byte marking the start of the command name. Copies
each character forward into the TX buffer at `&C105` until the next
bit-7 byte (end of name), then appends a space separator.""",
    on_entry={
        "x": "byte offset within cmd_table_fs (just past the matched command's last name char)",
        "y": "current command-line offset (saved/restored)",
    },
    on_exit={"x": "TX buffer offset past name+space", "y": "command line offset (restored)", "a": "clobbered"},
)


d.comment(0x946A, "Save Y on entry", align=Align.INLINE)
d.label(0x946B, "loop_scan_flag")

d.comment(0x946B, "Scan backwards in command table", align=Align.INLINE)
d.comment(0x946C, "Load table byte", align=Align.INLINE)
d.comment(0x946F, "Bit 7 clear: keep scanning", align=Align.INLINE)
d.comment(0x9471, "Point past flag byte to name start", align=Align.INLINE)
d.comment(0x9472, "Y=0: TX buffer offset", align=Align.INLINE)
d.label(0x9474, "loop_copy_name")

d.comment(0x9474, "Load command name character", align=Align.INLINE)
d.comment(0x9477, "Bit 7 set: end of name", align=Align.INLINE)
d.comment(0x9479, "Store character in TX buffer", align=Align.INLINE)
d.comment(0x947C, "Advance table pointer", align=Align.INLINE)
d.comment(0x947D, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x947E, "Continue copying name", align=Align.INLINE)
d.label(0x9480, "append_space")

d.comment(0x9480, "Space separator", align=Align.INLINE)
d.comment(0x9482, "Append space after command name", align=Align.INLINE)
d.comment(0x9485, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x9486, "Transfer length to A", align=Align.INLINE)
d.comment(0x9487, "And to X (buffer position)", align=Align.INLINE)
d.label(0x9489, "rts_copy_cmd_name")

d.comment(0x9489, "Return", align=Align.INLINE)
d.label(0x948A, "parse_quoted_arg")

d.subroutine(
    0x948A,
    "parse_quoted_arg",
    title="Parse possibly-quoted filename argument",
    description="""Reads from the command line at `(fs_crc_lo),Y` (`&BE`). Handles
double-quote delimiters and stores the result in the parse
buffer at `&0E30`. Raises `'Bad string'` on unbalanced quotes.""",
    on_entry={"y": "current offset within the command line"},
    on_exit={"y": "advanced past the parsed argument", "a": "clobbered (last byte read)"},
)


d.comment(0x948A, "A=0: no quote mode", align=Align.INLINE)
d.comment(0x948D, "Clear quote tracking flag", align=Align.INLINE)
d.label(0x9490, "loop_skip_spaces")

d.comment(0x9490, "Load char from command line", align=Align.INLINE)
d.comment(0x9492, "Space?", align=Align.INLINE)
d.comment(0x9494, "No: check for opening quote", align=Align.INLINE)
d.comment(0x9496, "Skip leading space", align=Align.INLINE)
d.comment(0x9497, "Continue skipping spaces", align=Align.INLINE)
d.label(0x9499, "check_open_quote")

d.comment(0x9499, "Double-quote character?", align=Align.INLINE)
d.comment(0x949B, "No: start reading filename", align=Align.INLINE)
d.comment(0x949D, "Skip opening quote", align=Align.INLINE)
d.comment(0x949E, "Toggle quote mode flag", align=Align.INLINE)
d.comment(0x94A1, "Store updated quote mode", align=Align.INLINE)
d.label(0x94A4, "loop_copy_arg_char")

d.comment(0x94A4, "Load char from command line", align=Align.INLINE)
d.comment(0x94A6, "Double-quote?", align=Align.INLINE)
d.comment(0x94A8, "No: store character as-is", align=Align.INLINE)
d.comment(0x94AA, "Toggle quote mode", align=Align.INLINE)
d.comment(0x94AD, "Store updated quote mode", align=Align.INLINE)
d.comment(0x94B0, "Replace closing quote with space", align=Align.INLINE)
d.label(0x94B2, "store_arg_char")

d.comment(0x94B2, "Store character in parse buffer", align=Align.INLINE)
d.comment(0x94B5, "Advance command line pointer", align=Align.INLINE)
d.comment(0x94B6, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x94B7, "End of line?", align=Align.INLINE)
d.comment(0x94B9, "No: continue parsing", align=Align.INLINE)
d.comment(0x94BB, "Check quote balance flag", align=Align.INLINE)
d.comment(0x94BE, "Balanced: return OK", align=Align.INLINE)
# UNMAPPED: d.comment(0x94C0, "Unbalanced: use BRK ptr for error", align=Align.INLINE)
d.comment(0x94C2, "Raise 'Bad string' error", align=Align.INLINE)
d.comment(0x94C5, "Store to TXCB", align=Align.INLINE)
d.entry(0x94CC)
d.label(0x94CC, "cmd_rename")

d.subroutine(
    0x94CC,
    "cmd_rename",
    title="*Rename command handler",
    description="""Parses two space-separated filenames from the command line, each
with its own access prefix. Sets the owner-only access mask
before parsing each name. Validates that both names resolve to
the same file server by comparing the FS-options word – raises
`'Bad rename'` if they differ. Falls through to
[`read_filename_char`](label:read_filename_char) to copy the second
filename into the TX buffer and send the request.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0x94CC, "Copy 'Rename ' to TX buffer", align=Align.INLINE)
d.comment(0x94D0, "Clear owner-only access bits before parsing", align=Align.INLINE)
d.comment(0x94D3, "Parse the quoted source filename", align=Align.INLINE)
d.comment(0x94D6, "Parse access prefix on the source filename", align=Align.INLINE)
d.label(0x94DA, "loop_copy_rename")

d.comment(0x94DA, "Load next parsed character", align=Align.INLINE)
d.comment(0x94DD, "End of line?", align=Align.INLINE)
d.comment(0x94DF, "No: store character", align=Align.INLINE)
d.label(0x94E1, "error_bad_rename")

d.comment(0x94E1, "Error number &B0", align=Align.INLINE)
d.comment(0x94E3, "Raise 'Bad rename' error", align=Align.INLINE)
d.comment(0x94EB, "Add 5 for header size", align=Align.INLINE)
d.label(0x94ED, "store_rename_char")

d.comment(0x94ED, "Store character in TX buffer", align=Align.INLINE)
d.comment(0x94F0, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x94F1, "Space (name separator)?", align=Align.INLINE)
d.comment(0x94F3, "Yes: first name complete", align=Align.INLINE)
d.comment(0x94F5, "Strip BASIC token prefix byte", align=Align.INLINE)
d.comment(0x94F8, "BRA back to loop_copy_rename", align=Align.INLINE)
d.label(0x94FA, "skip_rename_spaces")

d.comment(0x94FA, "Strip token from next char", align=Align.INLINE)
d.comment(0x94FD, "Load next parsed character", align=Align.INLINE)
d.comment(0x9500, "Still a space?", align=Align.INLINE)
d.comment(0x9502, "Yes: skip multiple spaces", align=Align.INLINE)
d.comment(0x9504, "Save current FS options", align=Align.INLINE)
d.comment(0x9507, "Push them", align=Align.INLINE)
d.comment(0x9508, "Reset access mask for second name", align=Align.INLINE)
d.comment(0x950B, "Save loop index across the access parse", align=Align.INLINE)
d.comment(0x950C, "Parse access prefix on the second filename", align=Align.INLINE)
d.comment(0x950F, "Restore loop index", align=Align.INLINE)
d.comment(0x9510, "Restore original FS options", align=Align.INLINE)
d.comment(0x9511, "Options changed (cross-FS)?", align=Align.INLINE)
d.comment(0x9514, "Yes: error (can't rename across FS)", align=Align.INLINE)
d.comment(0x9516, "Copy second filename and send", align=Align.INLINE)
d.entry(0x9519)
d.label(0x9519, "cmd_dir")

d.subroutine(
    0x9519,
    "cmd_dir",
    title="*Dir command handler",
    description="""Handles three argument syntaxes:

| Argument | Action |
|---|---|
| plain path        | delegates to `pass_send_cmd` |
| `'&'` alone       | root directory |
| `'&N.dir'`        | cross-filesystem directory change |

The cross-FS form sends a file-server selection command (code
`&12`) to locate the target server, raising `'Not found'` on
failure, then sends the directory change (code 6) and calls
`find_fs_and_exit` to update the active FS context.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0x9519, "Get first char of argument", align=Align.INLINE)
d.comment(0x951B, "Is it '&' (FS selector prefix)?", align=Align.INLINE)
d.comment(0x951D, "No: simple dir change", align=Align.INLINE)
d.comment(0x951F, "Skip '&'", align=Align.INLINE)
d.comment(0x9520, "Get char after '&'", align=Align.INLINE)
d.comment(0x9522, "End of line?", align=Align.INLINE)
d.comment(0x9524, "Yes: '&' alone (root directory)", align=Align.INLINE)
d.comment(0x9526, "Space?", align=Align.INLINE)
d.comment(0x9528, "No: check for '.' separator", align=Align.INLINE)
d.label(0x952A, "setup_fs_root")

d.comment(0x952A, "Y=&FF: pre-increment for loop", align=Align.INLINE)
d.label(0x952C, "loop_copy_fs_num")

d.comment(0x952C, "Advance index", align=Align.INLINE)
d.comment(0x952D, "Load char from command line", align=Align.INLINE)
d.comment(0x952F, "Copy to TX buffer", align=Align.INLINE)
d.comment(0x9532, "Is it '&' (end of FS path)?", align=Align.INLINE)
d.comment(0x9534, "No: keep copying", align=Align.INLINE)
d.comment(0x9536, "Replace '&' with CR terminator", align=Align.INLINE)
d.comment(0x9538, "Store CR in buffer", align=Align.INLINE)
d.comment(0x953B, "Point past CR", align=Align.INLINE)
d.comment(0x953C, "Transfer length to A", align=Align.INLINE)
d.comment(0x953D, "And to X (byte count)", align=Align.INLINE)
d.comment(0x953E, "Send directory request to server", align=Align.INLINE)
d.label(0x9541, "check_fs_dot")

d.comment(0x9541, "Is char after '&' a dot?", align=Align.INLINE)
d.comment(0x9543, "Yes: &FS.dir format", align=Align.INLINE)
d.comment(0x9545, "No: invalid syntax", align=Align.INLINE)
d.label(0x9548, "parse_fs_dot_dir")

d.comment(0x9548, "Skip '.'", align=Align.INLINE)
d.comment(0x9549, "Save dir path start position", align=Align.INLINE)
d.comment(0x954B, "FS command 4: examine directory", align=Align.INLINE)
d.comment(0x954D, "Store in TX buffer", align=Align.INLINE)
d.comment(0x9550, "Load FS flags", align=Align.INLINE)
d.comment(0x9553, "Set bit 6 (FS selection active)", align=Align.INLINE)
d.comment(0x9555, "Store updated flags", align=Align.INLINE)
d.comment(0x9558, "X=1: buffer offset", align=Align.INLINE)
d.comment(0x955A, "Copy FS number to buffer", align=Align.INLINE)
d.comment(0x955D, "Y=&12: select FS command code", align=Align.INLINE)
d.comment(0x955F, "Send FS selection command", align=Align.INLINE)
d.comment(0x9562, "Load reply status", align=Align.INLINE)
d.comment(0x9565, "Status 2 (found)?", align=Align.INLINE)
d.comment(0x9567, "Yes: proceed to dir change", align=Align.INLINE)
d.comment(0x9569, "Error number &D6", align=Align.INLINE)
d.comment(0x956B, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0x956E, "Store null terminator (A=0 from EOR)", align=Align.INLINE)
d.comment(0x9571, "Get message length", align=Align.INLINE)
d.comment(0x9574, "Go to error dispatch", align=Align.INLINE)
d.label(0x9578, "dir_found_send")

d.comment(0x9578, "Load current FS station byte", align=Align.INLINE)
d.comment(0x957B, "Store in TX buffer", align=Align.INLINE)
d.comment(0x957E, "X=1: buffer offset", align=Align.INLINE)
d.comment(0x9580, "Y=7: change directory command code", align=Align.INLINE)
d.comment(0x9582, "Send directory change request", align=Align.INLINE)
d.comment(0x9585, "X=1", align=Align.INLINE)
d.comment(0x9587, "Store start marker in buffer", align=Align.INLINE)
d.comment(0x958A, "Store start marker in buffer+1", align=Align.INLINE)
d.comment(0x958D, "Non-zero: commit state and return", align=Align.INLINE)
d.comment(0x958E, "Restore dir path start position", align=Align.INLINE)
d.comment(0x9590, "Copy directory path to buffer", align=Align.INLINE)
d.comment(0x9593, "Y=6: set directory command code", align=Align.INLINE)
d.comment(0x9595, "Send set directory command", align=Align.INLINE)
d.comment(0x9598, "Load reply handle", align=Align.INLINE)
d.comment(0x959B, "Select FS and return", align=Align.INLINE)
d.label(0x959E, "dir_pass_simple")

d.comment(0x959E, "Simple: pass command to FS", align=Align.INLINE)
d.label(0x95A1, "print_fs_ps_help")

d.comment(0x95A1, "Read first command-line char at (os_text_ptr),Y", align=Align.INLINE)
d.entry(0x95A1)
d.comment(0x95A3, "Is it CR (no argument supplied)?", align=Align.INLINE)
d.comment(0x95A5, "Non-CR: argument present -- exit via dispatch_fs_ps_with_arg (X=&A0)", align=Align.INLINE)
d.comment(0x95A7, "CR: print 'FS       ' header", align=Align.INLINE)
d.comment(0x95AA, "Print '[<D>.]<D>\\r'", align=Align.INLINE)
d.comment(0x95AD, "Print 'PS       ' header", align=Align.INLINE)
d.comment(0x95B0, "Print '[<D>.]<D>\\r' again", align=Align.INLINE)
d.comment(0x95B3, "Print final 'Space\\rNoSpace\\r' lines", align=Align.INLINE)
# UNMAPPED: d.comment(0x95BD, "NOP -- bit-7 terminator + resume opcode for the preceding inline string", align=Align.INLINE)
d.label(0x95BF, "bra_target_svc_return")

d.comment(0x95BF, "JMP to svc_return_unclaimed (long-distance via this 3-byte trampoline)", align=Align.INLINE)
d.comment(0x95C2, "Print 'P' prefix", align=Align.INLINE)
d.subroutine(
    0x95C2,
    "print_station_low",
    title="Print 'PS       ' 9-column header",
    description="""Calls [`print_inline`](label:print_inline) with `'P'` then falls
through (via the 1-byte CLV terminator and BVC) into
[`print_field_tail_s`](label:print_field_tail_s), so the combined output is
`'PS       '` -- the 9-column 'PS' field used in the `*FS`/`*PS`
no-arg help and `*STATUS` displays.""",
)


d.comment(
    0x95C6,
    "CLV -- bit-7 terminator + resume (V flag is irrelevant here, used as 1-byte resume opcode)",
    align=Align.INLINE,
)
d.comment(
    0x95C7,
    "BVC: V was just cleared -> always taken; falls into the shared 'S       ' tail at &95CC",
    align=Align.INLINE,
)
d.comment(0x95C9, "Print 'F' prefix", align=Align.INLINE)
d.subroutine(
    0x95C9,
    "print_fs_station",
    title="Print 'FS       ' 9-column header",
    description="""Calls [`print_inline`](label:print_inline) with `'F'` then falls
through (via the 1-byte NOP terminator) into
[`print_field_tail_s`](label:print_field_tail_s), so the combined output is
`'FS       '` -- the 9-column 'FS' field used in the `*FS`/`*PS`
no-arg help and `*STATUS` displays.""",
)


d.comment(0x95CD, "NOP -- bit-7 terminator; falls through into the shared 'S       ' tail at &95CC", align=Align.INLINE)
d.label(0x95CE, "print_field_tail_s")

d.comment(
    0x95CE,
    "Print 'S       ' (S + 7 spaces) -- the shared 8-char field used by both 'FS' and 'PS' callers",
    align=Align.INLINE,
)
d.comment(0x95D9, "Bit-7 terminator", align=Align.INLINE)
d.comment(0x95DA, "Return", align=Align.INLINE)
d.comment(
    0x95DB,
    "Print '[<D>.]<D>\\r' (file-name syntax fragment, shared between *FS/*PS no-arg help and *Dir)",
    align=Align.INLINE,
)
d.subroutine(
    0x95DB,
    "print_dir_syntax",
    title="Print '[<D>.]<D>\\\\r' directory-name syntax fragment",
    description="""3-byte JSR + inline `'[<D>.]<D>'` + CR + NOP terminator. Used as
a shared fragment by both `*Dir`'s syntax help and the `*FS`/`*PS`
no-argument help via [`print_fs_ps_help`](label:print_fs_ps_help).""",
)


d.comment(0x95E8, "Bit-7 terminator", align=Align.INLINE)
d.comment(0x95E9, "Return", align=Align.INLINE)
d.label(0x95EA, "dispatch_fs_ps_with_arg")

d.comment(0x95EA, "X=&A5: index into svc4 dispatch table (no-arg path)", align=Align.INLINE)
d.comment(0x95EC, "Tail-jump to svc4_dispatch_lookup with X=&A0", align=Align.INLINE)
d.subroutine(
    0x95EF,
    "set_fs_or_ps_cmos_station",
    title="Write FS/PS station+network to CMOS RAM",
    description="""Reached via PHA/PHA/RTS dispatch from cmd_table_fs sub-table 4
(`*FS` at [`&A82A`](address:A82A), `*PS` at
[`&A82F`](address:A82F)) when the caller supplies a `<net>.<stn>`
argument or wants to inspect/update the saved address.

The flag byte's low 6 bits (`AND #&3F`) double as the CMOS byte
index for the relevant station:

| command | flag | idx | CMOS bytes      |
| ------- | ---- | --- | --------------- |
| `*FS`   | `&C1` | 1   | 1 = FS station, 2 = FS network |
| `*PS`   | `&C3` | 3   | 3 = PS station, 4 = PS network |

Pre-reads existing CMOS[idx] and CMOS[idx+1] into `fs_work_5` /
`fs_work_6` so that the no-argument path leaves the saved values
unchanged. Calls
[`parse_fs_ps_args`](label:parse_fs_ps_args) which conditionally overwrites
`fs_work_5` (station), `fs_work_6` (canonical network: 0=local,
non-zero=remote) and `fs_work_7` (raw parsed network).

Writes the station via [`osbyte_a2`](label:osbyte_a2), then falls
through into `osbyte_a2` itself to write the raw network at
CMOS[idx+1]. Final `BRA` inside `osbyte_a2` returns via
[`svc_return_unclaimed`](label:svc_return_unclaimed).""",
    on_entry={"x": "offset in cmd_table_fs of the matched entry's flag byte"},
)


d.entry(0x95EF)
d.comment(0x95EF, "Read flag byte for matched cmd entry (syntax idx in bits 0..4)", align=Align.INLINE)
d.comment(0x95F2, "Mask off end-marker (bit 7) and V-if-no-arg flag (bit 6)", align=Align.INLINE)
d.comment(0x95F4, "X = CMOS byte index (1=FS stn, 3=PS stn)", align=Align.INLINE)
d.comment(0x95F5, "Save CMOS index", align=Align.INLINE)
d.comment(0x95F6, "Save caller's command-line cursor", align=Align.INLINE)
d.comment(0x95F7, "Save CMOS index again (consumed by first PLX below)", align=Align.INLINE)
d.comment(0x95F8, "Read existing CMOS[idx] (current station)", align=Align.INLINE)
d.comment(0x95FB, "Default station if user gives no args", align=Align.INLINE)
d.comment(0x95FD, "Recover CMOS index from stack", align=Align.INLINE)
d.comment(0x95FE, "X+=1: advance to network byte", align=Align.INLINE)
d.comment(0x95FF, "Read existing CMOS[idx+1] (current network)", align=Align.INLINE)
d.comment(0x9602, "Default network if user gives no args", align=Align.INLINE)
d.comment(0x9604, "Restore command-line cursor", align=Align.INLINE)
d.comment(0x9605, "Parse '<net>.<stn>'; updates fs_work_5/6/7 if args present", align=Align.INLINE)
d.comment(0x9608, "Recover CMOS index from stack", align=Align.INLINE)
d.comment(0x9609, "Re-save CMOS index for second write", align=Align.INLINE)
d.comment(0x960A, "Y = station (parsed or pre-read default)", align=Align.INLINE)
d.comment(0x960C, "Write CMOS[idx] = station", align=Align.INLINE)
d.comment(0x960F, "Recover CMOS index from stack", align=Align.INLINE)
d.comment(0x9610, "X+=1: advance to network byte", align=Align.INLINE)
d.comment(
    0x9611,
    "Y = raw parsed network (NOT canonical fs_work_6); fall through into osbyte_a2 to write CMOS[idx+1]",
    align=Align.INLINE,
)
d.comment(0x9613, "A=&A2: write CMOS RAM byte via OSBYTE", align=Align.INLINE)
d.subroutine(
    0x9613,
    "osbyte_a2",
    title="OSBYTE &A2 (write Master CMOS RAM byte)",
    description="""Three instructions: `LDA #&A2 / JSR OSBYTE / BRA &95BF`. Writes
the Master 128 CMOS RAM byte indexed by `X` with the value in `Y`.
The trailing `BRA` lands on
[`bra_target_svc_return`](label:bra_target_svc_return) (a 3-byte `JMP` trampoline
to [`svc_return_unclaimed`](label:svc_return_unclaimed), reached this way
because `BRA`'s 8-bit displacement can't span &9618 → &8C8B).

`osbyte_a2` ends at [`&961A`](address:961A) (3 instructions, 7 bytes);
the next labelled routine is [`cmd_space`](label:cmd_space). Counterpart of
[`osbyte_a1`](label:osbyte_a1) (read).

Callers: [`set_fs_or_ps_cmos_station`](label:set_fs_or_ps_cmos_station) (once via
`JSR`, once via fall-through), the `BRA` shortcut at
`&962F` inside [`cmd_nospace`](label:cmd_nospace), and
an `OSARGS`-related read-modify-write of CMOS byte &11 ending at
[`osopt_cmos_writeback_jsr`](label:osopt_cmos_writeback_jsr).""",
    on_entry={"x": "CMOS RAM byte index", "y": "value to write"},
)


d.comment(0x9618, "BRA -91 -> bra_target_svc_return", align=Align.INLINE)
d.comment(0x961A, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.subroutine(
    0x961A,
    "cmd_space",
    title="*Space command: enable space-remaining display",
    description="""Reached via the [`cmd_table_fs`](label:cmd_table_fs) dispatch entry for
`*Space`. Reads CMOS byte &11 with [`osbyte_a1`](label:osbyte_a1),
sets bit 0 of the value, then `BRA`s to the shared write-back tail
at [`osbyte_a2_value_tya`](label:osbyte_a2_value_tya).""",
)


d.entry(0x961A)
d.comment(0x961C, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0x961F, "A = current CMOS &11 value", align=Align.INLINE)
d.comment(0x9620, "Set bit 0 in A", align=Align.INLINE)
d.comment(0x9622, "BRA osbyte_a2_value_tya: shared write-back tail", align=Align.INLINE)
d.comment(0x9624, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.subroutine(
    0x9624,
    "cmd_nospace",
    title="*NoSpace command: disable space-remaining display",
    description="""Reached via the [`cmd_table_fs`](label:cmd_table_fs) dispatch entry for
`*NoSpace`. Reads CMOS byte &11 with [`osbyte_a1`](label:osbyte_a1),
clears bit 0 of the value, falls through to
[`osbyte_a2_value_tya`](label:osbyte_a2_value_tya), and `BRA`s back into
[`osbyte_a2`](label:osbyte_a2) to write CMOS &11 = `Y`.""",
)


d.entry(0x9624)
d.comment(0x9626, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0x9629, "A = current CMOS &11 value", align=Align.INLINE)
d.comment(0x962A, "Clear bit 0 in A", align=Align.INLINE)
d.comment(0x962C, "New CMOS value to Y", align=Align.INLINE)
d.subroutine(
    0x962C,
    "osbyte_a2_value_tya",
    title="Shared CMOS write-back tail",
    description="""Common tail used by [`cmd_space`](label:cmd_space) (via `BRA` from
&9620 with the new value already in `A`) and
[`cmd_nospace`](label:cmd_nospace) (fall-through with the new value in
`A`). `TAY` moves the byte to `Y`, then `LDX #&11` reloads the
CMOS index and `BRA osbyte_a2` performs the write.""",
)


d.comment(0x962D, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0x962F, "BRA osbyte_a2: write CMOS &11 = Y", align=Align.INLINE)
d.comment(0x9631, "Read first command-line char", align=Align.INLINE)
d.subroutine(
    0x9631,
    "svc_29_status",
    title="Service &29: *STATUS handler",
    description="""Reached via `svc_dispatch` slot &18. With no argument on the
command line (first byte = `CR`) prints the FS and PS station
addresses from CMOS &01-&04, then a single FS-active flag drawn
from bit 0 of CMOS &11 (the same bit that
[`cmd_space`](label:cmd_space) / [`cmd_nospace`](label:cmd_nospace) set
and clear). With an argument, branches to
[`help_dispatch_setup`](label:help_dispatch_setup) to parse it.""",
)


d.entry(0x9631)
d.comment(0x9633, "Is it CR (no argument)?", align=Align.INLINE)
d.comment(0x9635, "Non-CR: parse the argument at help_dispatch_setup", align=Align.INLINE)
d.comment(0x9637, "Print 'FS       ' header", align=Align.INLINE)
d.comment(0x963A, "Print FS network.station from CMOS &02/&01", align=Align.INLINE)
d.comment(0x963D, "Print 'PS       ' header", align=Align.INLINE)
d.comment(0x9640, "Print PS network.station from CMOS &04/&03", align=Align.INLINE)
d.comment(0x9643, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0x9645, "Read CMOS &11 (FS state)", align=Align.INLINE)
d.comment(0x9648, "A = CMOS &11", align=Align.INLINE)
d.comment(0x9649, "Mask bit 0 (FS-active flag)", align=Align.INLINE)
d.comment(0x964B, "Bit set: skip 'No ' prefix", align=Align.INLINE)
d.comment(0x964D, "Print 'No ' prefix via inline", align=Align.INLINE)
d.comment(0x9653, "Bit-7 terminator + resume", align=Align.INLINE)
d.comment(0x9654, "Print 'Space        ' or similar via inline", align=Align.INLINE)
d.label(0x9654, "parse_object_space_print")

d.comment(0x965E, "Bit-7 terminator + resume opcode", align=Align.INLINE)
d.subroutine(
    0x9664,
    "print_ps_address",
    title="Print printer-server address from CMOS",
    description="""Prints the printer server's saved `network.station` from
CMOS RAM. Sets `X=4` (the PS network byte) and branches into the shared
tail at [`print_cmos_pair`](label:print_cmos_pair), which prints CMOS[X] then
CMOS[X-1] separated by a `.`.

In 4.26 the two entry points share one body: `print_fs_address` (`X=2`)
falls straight in, while `print_ps_address` (`X=4`) reaches it by `BRA`,
skipping the `LDX #2`.""",
)

d.comment(0x9664, "X=4: CMOS RAM byte 4 (PS network number)", align=Align.INLINE)
d.comment(0x9666, "Branch into shared tail (X already set)", align=Align.INLINE)
d.subroutine(
    0x9668,
    "print_fs_address",
    title="Print file-server address from CMOS",
    description="""Prints the file server's saved `network.station` from
CMOS RAM. Sets `X=2` (the FS network byte) and falls into the shared tail
[`print_cmos_pair`](label:print_cmos_pair). See [`print_ps_address`](label:print_ps_address)
for the shared-body structure.""",
)

d.comment(0x9668, "X=2: CMOS RAM byte 2 (FS network number)", align=Align.INLINE)
d.label(0x966A, "print_cmos_pair")
d.comment(0x966A, "Save network-byte index across the first print", align=Align.INLINE)
d.comment(0x966B, "Read CMOS[X] (network number) via osbyte_a1", align=Align.INLINE)
d.comment(0x966E, "A = CMOS network byte", align=Align.INLINE)
d.comment(0x966F, "Print as decimal (no leading zeros)", align=Align.INLINE)
d.comment(0x9672, "Print '.' separator via inline", align=Align.INLINE)
d.comment(0x9676, "PLX terminator: restore X (network index)", align=Align.INLINE)
d.comment(0x9677, "X-1: the station byte sits just below the network byte", align=Align.INLINE)
d.label(0x9678, "print_cmos_decimal_nl")

d.comment(0x9678, "Read CMOS X via osbyte_a1", align=Align.INLINE)
d.comment(0x967B, "A = CMOS value", align=Align.INLINE)
d.comment(0x967C, "Print as decimal", align=Align.INLINE)
d.label(0x9682, "print_cmos_done")

d.comment(0x9682, "JMP svc_return_unclaimed (release service call)", align=Align.INLINE)
d.comment(0x9685, "X=&C2: setup index for the dispatch chain", align=Align.INLINE)
d.label(0x9685, "help_dispatch_setup")

d.comment(0x9687, "JMP svc4_dispatch_lookup -- shared parser dispatch", align=Align.INLINE)
d.subroutine(
    0x9687,
    "dispatch_help_command",
    title="Dispatch *HELP-style argument via svc4_dispatch_lookup",
    description="""3-byte trampoline: `JMP svc4_dispatch_lookup` with `X = &BD` from
the caller. Used by [`svc_29_status`](label:svc_29_status)'s
non-CR path so an argument after `*STATUS` (or similar *HELP-like
cmd) gets parsed and dispatched through the same shared parser as
the regular cmd-table dispatch. Note the `'!Help.'` bytes
immediately following are an unrelated inline string used by the
filename walker, not part of this routine's body.""",
)

d.label(0x9688, "help_topic_template")

d.comment(
    0x968A,
    "'!Help.' filename template copied into the TXCB command buffer to open the help file",
    align=Align.INLINE,
)

d.subroutine(
    0x9692,
    "match_on_suffix",
    title="svc &18: interactive-HELP 'ON ' matcher and help-topic printer",
    description="""Interactive-HELP service handler (svc &18). Reads the command
line at [`os_text_ptr`](label:os_text_ptr) and tests for the
two-letter `ON` keyword (case-insensitive, `EOR #'O'` / `EOR #'N'`
with `AND #&5F`); if it is absent the call returns unclaimed. On a
match it copies the `'!Help.'` template plus the requested topic
name into the TXCB command buffer, opens the resulting help file
and prints it byte-by-byte via [`osbget`](label:osbget) /
[`oswrch`](label:oswrch), honouring paged mode and Escape.""",
)


# --- svc &18 interactive-HELP handler: labels + inline comments ---
d.label(0x026A, "vdu_queue_count")

d.label(0x96B1, "help_return")
d.label(0x96B3, "help_on_matched")
d.label(0x96B8, "loop_skip_help_spaces")
d.label(0x96C4, "help_have_topic_char")
d.label(0x96C5, "help_build_cmd")
d.label(0x96CD, "loop_copy_command_suffix")
d.label(0x96DD, "check_template_dot")
d.label(0x96E1, "loop_copy_topic_name")
d.label(0x96E5, "store_topic_char")
d.label(0x96F4, "start_help_file_load")
d.label(0x970A, "loop_print_help_byte")
d.label(0x9717, "help_next_topic")
d.label(0x971A, "loop_help_next_topic")
d.label(0x9725, "help_print_start")
d.label(0x972C, "help_emit_char")

d.comment(0x9692, "Save caller's command-line index Y", align=Align.INLINE)
d.comment(0x9693, "Test fs_flags: bit 6 = interactive HELP armed", align=Align.INLINE)
d.comment(0x9696, "Bit 6 clear: not our HELP call -> return", align=Align.INLINE)
d.comment(0x9698, "Point work_ae at the command line (lo)", align=Align.INLINE)
d.comment(0x969A, "Store command-line pointer lo", align=Align.INLINE)
d.comment(0x969C, "Command-line pointer hi", align=Align.INLINE)
d.comment(0x969E, "Store pointer hi (addr_work)", align=Align.INLINE)
d.comment(0x96A0, "Read first keyword character", align=Align.INLINE)
d.comment(0x96A2, "Compare with 'O' ...", align=Align.INLINE)
d.comment(0x96A4, "... case-insensitively (mask bit 5)", align=Align.INLINE)
d.comment(0x96A6, "Not 'O': return (line is not '...ON ')", align=Align.INLINE)
d.comment(0x96A8, "Advance to second character", align=Align.INLINE)
d.comment(0x96A9, "Read second keyword character", align=Align.INLINE)
d.comment(0x96AB, "Compare with 'N' ...", align=Align.INLINE)
d.comment(0x96AD, "... case-insensitively", align=Align.INLINE)
d.comment(0x96AF, "'ON' matched: handle the topic", align=Align.INLINE)
d.comment(0x96B1, "Restore caller's Y", align=Align.INLINE)
d.comment(0x96B2, "Return to service dispatcher", align=Align.INLINE)
d.comment(0x96B3, "Save Y across FS-select", align=Align.INLINE)
d.comment(0x96B4, "Ensure NFS is the current filing system", align=Align.INLINE)
d.comment(0x96B7, "Restore Y", align=Align.INLINE)
d.comment(0x96B8, "Advance to next command-line character", align=Align.INLINE)
d.comment(0x96B9, "Read it", align=Align.INLINE)
d.comment(0x96BB, "Set V (topic-char marker) from &9767 bit 6", align=Align.INLINE)
d.comment(0x96BE, "Space?", align=Align.INLINE)
d.comment(0x96C0, "Control char (<space): stop scanning", align=Align.INLINE)
d.comment(0x96C2, "Space: keep skipping leading spaces", align=Align.INLINE)
d.comment(0x96C4, "Real char: clear V (topic present)", align=Align.INLINE)
d.comment(0x96C5, "Save command-buffer index", align=Align.INLINE)
d.comment(0x96C8, "Save it as the command flag too", align=Align.INLINE)
d.comment(0x96CB, "X=1: template-walk index", align=Align.INLINE)
d.comment(0x96CD, "Advance template index", align=Align.INLINE)
d.comment(0x96CE, "Read '!Help.' template byte", align=Align.INLINE)
d.comment(0x96D1, "Store into the command buffer", align=Align.INLINE)
d.comment(0x96D4, "V clear (real topic char): check '.' terminator", align=Align.INLINE)
d.comment(0x96D6, "V set (line ended): CR?", align=Align.INLINE)
d.comment(0x96D8, "Not CR: keep copying template", align=Align.INLINE)
d.comment(0x96DA, "Skip the CR", align=Align.INLINE)
d.comment(0x96DB, "Open the help file", align=Align.INLINE)
d.comment(0x96DD, "Template terminator '.'?", align=Align.INLINE)
d.comment(0x96DF, "No: keep copying template", align=Align.INLINE)
d.comment(0x96E1, "Advance destination index", align=Align.INLINE)
d.comment(0x96E2, "Read topic-name character", align=Align.INLINE)
d.comment(0x96E4, "Advance source index", align=Align.INLINE)
d.comment(0x96E5, "Store topic character", align=Align.INLINE)
d.comment(0x96E8, "CR (end of name)?", align=Align.INLINE)
d.comment(0x96EA, "Yes: open the help file", align=Align.INLINE)
d.comment(0x96EC, "Space (terminator)?", align=Align.INLINE)
d.comment(0x96EE, "No: keep copying the name", align=Align.INLINE)
d.comment(0x96F0, "Replace trailing space with CR", align=Align.INLINE)
d.comment(0x96F2, "Store the CR terminator", align=Align.INLINE)
d.comment(0x96F4, "Save command-buffer index", align=Align.INLINE)
d.comment(0x96F5, "Account for the last character", align=Align.INLINE)
d.comment(0x96F6, "Read fs_lib_flags", align=Align.INLINE)
d.comment(0x96F9, "Clear the top two bits", align=Align.INLINE)
d.comment(0x96FB, "Set bit 7 (load pending)", align=Align.INLINE)
d.comment(0x96FD, "Store fs_lib_flags back", align=Align.INLINE)
d.comment(0x9700, "A=&40: load-mode flag", align=Align.INLINE)
d.comment(0x9702, "Set last-byte flag", align=Align.INLINE)
d.comment(0x9704, "Open the help-topic file", align=Align.INLINE)
d.comment(0x9707, "File handle -> Y (0 = open failed)", align=Align.INLINE)
d.comment(0x9708, "Open failed: skip to next topic", align=Align.INLINE)
d.comment(0x970A, "Read next byte from the help file", align=Align.INLINE)
d.comment(0x970D, "C clear: byte read OK -> print it", align=Align.INLINE)
d.comment(0x970F, "A=0: OSFIND close mode", align=Align.INLINE)
d.comment(0x9714, "Print a newline after the file", align=Align.INLINE)
d.comment(0x9717, "Restore command-line index", align=Align.INLINE)
d.comment(0x9718, "Back up over the first consumed char", align=Align.INLINE)
d.comment(0x9719, "Back up over the second consumed char", align=Align.INLINE)
d.comment(0x971A, "Advance to next character", align=Align.INLINE)
d.comment(0x971B, "Read it", align=Align.INLINE)
d.comment(0x971D, "Space?", align=Align.INLINE)
d.comment(0x971F, "Control char: no more topics -> return", align=Align.INLINE)
d.comment(0x9721, "Space: keep scanning", align=Align.INLINE)
d.comment(0x9723, "Real char: process the next topic", align=Align.INLINE)
d.comment(0x9725, "Check the Escape flag", align=Align.INLINE)
d.comment(0x9727, "Bit 7 clear: not escaping -> print", align=Align.INLINE)
d.comment(0x9729, "Escape pressed: abort with error", align=Align.INLINE)
d.comment(0x972C, "Print the byte", align=Align.INLINE)
d.comment(0x972F, "Was it a CR?", align=Align.INLINE)
d.comment(0x9731, "No: read the next byte", align=Align.INLINE)
d.comment(0x9733, "CR: read paged-mode line count", align=Align.INLINE)
d.comment(0x9736, "Non-zero: no pause, continue", align=Align.INLINE)
d.comment(0x9738, "Emit newline", align=Align.INLINE)
d.comment(0x973B, "Loop for the next byte", align=Align.INLINE)


# svc &18 help handler: genuine ASCII-character operands
d.char_literal(0x96A3)
d.char_literal(0x96AC)
d.char_literal(0x96BF)
d.char_literal(0x96DE)
d.char_literal(0x96ED)
d.char_literal(0x971E)

d.label(0x973D, "init_txcb_bye")

d.subroutine(
    0x973D,
    "init_txcb_bye",
    title="Set up open receive for FS reply on port &90",
    description="""Loads `A=&90` (the FS command/reply port) and falls through to
[`init_txcb_port`](label:init_txcb_port), which creates an open
receive control block: the template sets `txcb_ctrl` to `&80`,
then `DEC` makes it `&7F` (bit 7 clear = awaiting reply). The
NMI RX handler sets bit 7 when a reply arrives on this port,
which [`wait_net_tx_ack`](label:wait_net_tx_ack) polls for.""",
    on_entry={},
)


d.comment(0x973D, "A=&90: bye command port", align=Align.INLINE)
d.label(0x973F, "init_txcb_port")

d.subroutine(
    0x973F,
    "init_txcb_port",
    title="Create open receive control block on specified port",
    description="""Calls [`init_txcb`](label:init_txcb) to copy the 12-byte
template into the TXCB workspace at `&00C0`, then stores `A` as
the port (`txcb_port` at `&C1`) and sets `txcb_start` to 3. The
`DEC txcb_ctrl` changes the control byte from `&80` to `&7F`
(bit 7 clear), creating an open receive: the NMI RX handler
will set bit 7 when a reply frame arrives on this port, which
[`wait_net_tx_ack`](label:wait_net_tx_ack) polls for.""",
    on_entry={"a": "port number"},
)


d.comment(0x973F, "Initialise TXCB from template", align=Align.INLINE)
d.comment(0x9742, "Set transmit port", align=Align.INLINE)
d.comment(0x9744, "A=3: data start offset", align=Align.INLINE)
d.comment(0x9746, "Set TXCB start offset", align=Align.INLINE)
d.comment(0x9748, "Open receive: &80->&7F (bit 7 clear = awaiting reply)", align=Align.INLINE)
d.comment(0x974A, "Return", align=Align.INLINE)
d.label(0x974B, "init_txcb")

d.subroutine(
    0x974B,
    "init_txcb",
    title="Initialise TX control block from ROM template",
    description="""Copies 12 bytes from [`txcb_init_template`](label:txcb_init_template) into the
TXCB workspace at `&00C0`. For the first two bytes (`Y=0,1`),
also copies the destination station/network from `&0E00` into
`txcb_dest` (`&C2`). Preserves `A` via `PHA`/`PLA`.

Called by 4 sites including [`cmd_pass`](label:cmd_pass),
[`init_txcb_port`](label:init_txcb_port),
[`prep_send_tx_cb`](label:prep_send_tx_cb), and `send_wipe_request`.""",
    on_exit={"a": "preserved", "x, y": "clobbered (Y left at &FF on loop exit)"},
)


d.comment(0x974B, "Save A", align=Align.INLINE)
d.comment(0x974C, "Y=&0B: template size - 1", align=Align.INLINE)
d.label(0x974E, "loop_init_txcb")

d.comment(0x974E, "Load byte from TXCB template", align=Align.INLINE)
d.comment(0x9751, "Store to TXCB workspace", align=Align.INLINE)
d.comment(0x9754, "Index >= 2?", align=Align.INLINE)
d.comment(0x9756, "Yes: skip dest station copy", align=Align.INLINE)
d.comment(0x9758, "Load dest station byte", align=Align.INLINE)
d.comment(0x975B, "Store to TXCB destination", align=Align.INLINE)
d.label(0x975E, "skip_txcb_dest")

d.comment(0x975E, "Decrement index", align=Align.INLINE)
d.comment(0x975F, "More bytes: continue", align=Align.INLINE)
d.comment(0x9761, "Restore A", align=Align.INLINE)
d.comment(0x9762, "Return", align=Align.INLINE)
d.index_base(0x9763, "txcb_init_template")
d.banner(
    0x9763,
    title="TXCB initialisation template (12 bytes)",
    description="""Copied byte-for-byte by [`init_txcb`](label:init_txcb) into the
TXCB workspace at `&00C0`. The Nth template byte (at `&9763 + N`)
ends up at TXCB offset N (`&00C0 + N`).

Bytes 2 and 3 (placeholders `&00 &00` here) are overwritten
during the copy: while writing TXCB[0] and TXCB[1] the loop also
copies `hazel_fs_station[0..1]` (HAZEL `&C000..&C001`) into
`txcb_dest` (`&00C2..&00C3`), so the runtime destination station
and network come from the live FS state rather than this
template.

The `&FF` byte at offset 6 ([`always_set_v_byte`](label:always_set_v_byte))
serves double duty: it is part of this template AND a `BIT $abs`
target used by 22 callers to set V and N flags without clobbering
`A`.""",
)
for i in range(12):
    d.byte(0x9763 + i)

d.comment(0x9763, "Offset 0: txcb_ctrl = &80 (TX command)", align=Align.INLINE)
d.comment(0x9764, "Offset 1: txcb_port = &99 (FS command port)", align=Align.INLINE)
d.comment(0x9765, "Offset 2: txcb_dest lo placeholder (overwritten with hazel_fs_station[0])", align=Align.INLINE)
d.comment(0x9766, "Offset 3: txcb_dest hi placeholder (overwritten with hazel_fs_station[1])", align=Align.INLINE)
d.comment(0x9767, "Offset 4: txcb_start lo = 0", align=Align.INLINE)
d.comment(0x9768, "Offset 5: txcb_start hi = &C1 (data buffer starts at &C100 in HAZEL)", align=Align.INLINE)
d.label(0x9769, "always_set_v_byte")

d.comment(0x9769, "Offset 6: padding &FF; doubles as the always_set_v_byte BIT $abs target", align=Align.INLINE)
d.label(0x976A, "bit_test_ff")

d.comment(0x976A, "Offset 7: txcb_pos = &FF (also labelled bit_test_ff)", align=Align.INLINE)
d.comment(0x976B, "Offset 8: txcb_end lo = &FF", align=Align.INLINE)
d.comment(0x976C, "Offset 9: txcb_end hi = &C1 (buffer end &C1FF)", align=Align.INLINE)
d.comment(0x976D, "Offset 10: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x976E, "Offset 11: extended-addr fill (&FF)", align=Align.INLINE)
d.label(0x976F, "send_request_nowrite")

d.subroutine(
    0x976F,
    "send_request_nowrite",
    title="Send read-only FS request (carry set)",
    description="""Pushes `A` and sets carry to indicate no-write mode, then
branches to `txcb_copy_carry_set` to enter the common TXCB copy,
send, and reply-processing path. The carry flag controls whether
a disconnect is sent on certain reply codes. Called by
`setup_transfer_workspace`.""",
    on_entry={
        "y": "FS function code (stored as TX[1] = txcb_func by txcb_copy_carry_set)",
        "a": "saved on stack at entry (consumed by the txcb send/receive path)",
    },
)


d.comment(0x976F, "Save A", align=Align.INLINE)
d.comment(0x9770, "Set carry (read-only mode)", align=Align.INLINE)
d.label(0x9773, "send_request_write")

d.subroutine(
    0x9773,
    "send_request_write",
    title="Send read-write FS request (V clear)",
    description="""Clears `V` flag and branches unconditionally to
`txcb_copy_carry_clr` (via `BVC`, always taken after `CLV`) to
enter the common TXCB copy, send, and reply-processing path with
carry clear (write mode). Called by `do_fs_cmd_iteration` and
`send_txcb_swap_addrs`.""",
    on_entry={
        "y": "FS function code (stored as TX[1] = txcb_func by txcb_copy_carry_clr)",
        "a": "request payload byte (used by the txcb send path)",
    },
)


d.comment(0x9773, "Clear V", align=Align.INLINE)
d.comment(0x9776, "Y=0: process_all_fcbs filter (0 = all FCBs)", align=Align.INLINE)
d.entry(0x9776)
d.label(0x9776, "cmd_bye")

d.subroutine(
    0x9776,
    "cmd_bye",
    title="*Bye command handler",
    description="""Closes all open file control blocks via
process_all_fcbs, shuts down any *SPOOL/*EXEC files
with OSBYTE &77, and closes all network channels.
Falls through to save_net_tx_cb with function code
&17 to send the bye request to the file server.""",
)
d.comment(0x9778, "Walk all 16 FCB slots, calling start_wipe_pass on each", align=Align.INLINE)
d.comment(0x977B, "OSBYTE &77 = close *SPOOL and *EXEC files", align=Align.INLINE)
d.comment(0x977D, "Close any open *SPOOL/*EXEC handles", align=Align.INLINE)
d.comment(0x9780, "A=&40: bit 6 of fs_flags = 'FS in active session'", align=Align.INLINE)
d.comment(0x9782, "Clear bit 6: mark FS session inactive", align=Align.INLINE)
d.comment(0x9785, "Close every Econet client channel", align=Align.INLINE)
d.comment(0x9788, "Y=&17: FS function code 'Bye' (logoff request)", align=Align.INLINE)
d.label(0x978A, "save_net_tx_cb")

d.subroutine(
    0x978A,
    "save_net_tx_cb",
    title="Save FS state and send command to file server",
    description="""Copies station address and function code (`Y`) to the TX buffer,
builds the TXCB via [`init_txcb`](label:init_txcb), sends the
packet through [`prep_send_tx_cb`](label:prep_send_tx_cb), and waits
for the reply via [`recv_and_process_reply`](label:recv_and_process_reply).
`V` is clear for standard mode.""",
    on_entry={
        "y": "FS function code (becomes TX[1] = txcb_func)",
        "x": "TX buffer payload length (prep_send_tx_cb uses X+5 as txcb_end)",
    },
    on_exit={"a": "FS reply status"},
)


d.comment(
    0x978A,
    "Clear V: standard send mode (callers set V via save_net_tx_cb_vset for the lib-flag variant)",
    align=Align.INLINE,
)
d.label(0x978B, "save_net_tx_cb_vset")

d.subroutine(
    0x978B,
    "save_net_tx_cb_vset",
    title="Save and send TXCB with V flag set",
    description="""Variant of [`save_net_tx_cb`](label:save_net_tx_cb) for callers that
have already set `V`. Copies the FS station address from `&0E02`
to `&0F02`, then falls through to `txcb_copy_carry_clr` which
clears carry and enters the common TXCB copy, send, and reply
path.

Called by `check_and_setup_txcb`, `format_filename_field`, and
`cmd_remove`.""",
    on_entry={
        "y": "FS function code",
        "x": "TX buffer payload length",
        "v flag": "set by caller (selects this variant via the 'no CLV' fall-through from save_net_tx_cb)",
    },
    on_exit={"a": "FS reply status"},
)


d.comment(0x978B, "Read FS station from &C002 (saved from selection time)", align=Align.INLINE)
d.comment(0x978E, "Copy into TX buffer at &C102 (dest station for header)", align=Align.INLINE)
d.label(0x9791, "txcb_copy_carry_clr")

d.comment(0x9791, "Clear C: caller wants four-way handshake (not disconnect)", align=Align.INLINE)
d.label(0x9792, "txcb_copy_carry_set")

d.comment(0x9792, "Save flags so we can keep V across the loop", align=Align.INLINE)
d.comment(0x9793, "Save Y -- the entry function code -- into TX[1]", align=Align.INLINE)
d.comment(0x9796, "Y=1: copy 2 bytes (network/control) starting at index 1", align=Align.INLINE)
d.label(0x9798, "loop_copy_vset_stn")

d.comment(0x9798, "Read source byte at &C003+Y", align=Align.INLINE)
d.comment(0x979B, "Write to TX buffer at &C103+Y", align=Align.INLINE)
d.comment(0x979E, "Step backwards", align=Align.INLINE)
d.comment(0x979F, "Loop while Y >= 0 (covers indices 1, 0)", align=Align.INLINE)
d.comment(0x97A1, "Test fs_lib_flags: bit 6 = use library, bit 7 = *-prefix-stripped", align=Align.INLINE)
d.comment(0x97A4, "V (bit 6) set: use the library station instead", align=Align.INLINE)
d.comment(0x97A6, "Neither bit set: leave the FS station copy intact", align=Align.INLINE)
d.comment(0x97A8, "Bit 7 (FS-prefix) set: substitute the saved-prefix station from &C004", align=Align.INLINE)
d.comment(0x97AB, "Override TX[3]'s station byte", align=Align.INLINE)
d.comment(0x97AE, "Always taken: V was clear when we entered (BVS at &97A4 didn't fire)", align=Align.INLINE)
d.label(0x97B0, "use_lib_station")

d.comment(
    0x97B0,
    "use_lib_station: substitute the library station from &C002 (the original FS station, but bit 6 of fs_lib_flags redirects via lib path)",
    align=Align.INLINE,
)
d.comment(0x97B3, "Override TX[3] with the library station byte", align=Align.INLINE)
d.label(0x97B6, "done_vset_station")

d.comment(0x97B6, "Restore the saved flags (V/C control downstream init_txcb behaviour)", align=Align.INLINE)
d.label(0x97B7, "prep_send_tx_cb")

d.subroutine(
    0x97B7,
    "prep_send_tx_cb",
    title="Build TXCB from scratch, send, and receive reply",
    description="""Full send/receive cycle comprising two separate Econet
transactions:

1. Save flags, set reply port `&90`.
2. Call [`init_txcb`](label:init_txcb), compute `txcb_end =
   X + 5`.
3. Dispatch on carry:

   | `C` | Path |
   |---|---|
   | set   | `handle_disconnect` |
   | clear | `init_tx_ptr_and_send` for a client-initiated four-way handshake (scout, ACK, data, ACK) to deliver the command |

4. After TX completes, the ADLC returns to idle RX-listen.
5. Falls through to [`recv_and_process_reply`](label:recv_and_process_reply)
   which waits for the server to independently initiate a new
   four-way handshake with the reply on port `&90`. There is no
   reply data in the original ACK payload.""",
    on_entry={
        "x": "TX buffer payload length (txcb_end = X + 5)",
        "y": "FS function code (already stashed by the txcb-copy entry path)",
        "c flag": "set = disconnect path (handle_disconnect); clear = normal four-way handshake send",
    },
    on_exit={"a": "FS reply status (or doesn't return on error)"},
)


d.comment(0x97B7, "Save flags so C survives the init_txcb call", align=Align.INLINE)
d.comment(0x97B8, "Reply port = &90 (FS reply port)", align=Align.INLINE)
d.comment(0x97BA, "Stash port in TXCB[0]", align=Align.INLINE)
d.comment(0x97BD, "Build the rest of the TXCB (control, dest stn/net, etc.)", align=Align.INLINE)
d.comment(0x97C0, "Move TX-buffer end pointer (returned in X) into A", align=Align.INLINE)
d.comment(0x97C1, "Add 5 bytes of slack for trailing reply data", align=Align.INLINE)
d.comment(0x97C3, "Stash the resulting end-of-buffer offset", align=Align.INLINE)
d.comment(0x97C5, "Restore the original C flag from caller", align=Align.INLINE)
d.comment(0x97C6, "C set: this is a disconnect; jump to handle_disconnect", align=Align.INLINE)
d.comment(0x97C8, "Save flags again across the actual TX (TX clobbers them)", align=Align.INLINE)
d.comment(0x97C9, "Send the four-way-handshake-initiated command packet", align=Align.INLINE)
d.comment(0x97CC, "Restore caller's flags before falling into recv_and_process_reply", align=Align.INLINE)
d.label(0x97CD, "recv_and_process_reply")

d.subroutine(
    0x97CD,
    "recv_and_process_reply",
    title="Receive FS reply and dispatch on status codes",
    description="""Waits for a server-initiated reply transaction. After the
command TX completes (a separate client-initiated four-way
handshake), calls [`init_txcb_bye`](label:init_txcb_bye) to set up
an open receive on port `&90` (`txcb_ctrl = &7F`). The server
independently initiates a new four-way handshake to deliver the
reply; the NMI RX handler matches the incoming scout against
this RXCB and sets bit 7 on completion.
[`wait_net_tx_ack`](label:wait_net_tx_ack) polls for this.

Iterates over reply bytes:

| Byte / state | Action |
|---|---|
| `0` | terminates |
| `V` set | adjust by `+&2B` |
| non-zero, `V` clear | dispatch to `store_reply_status` |

Handles disconnect requests (`C` set from
[`prep_send_tx_cb`](label:prep_send_tx_cb)) and `'Data Lost'`
warnings when channel status bits indicate pending writes were
interrupted.""",
    on_entry={"c flag": "set = disconnect mode (caller sent a disconnect scout; handle the server's matching reply)"},
    on_exit={"a": "FS reply status byte"},
)


d.comment(0x97CD, "Save flags so caller's V/C survive the receive", align=Align.INLINE)
d.comment(0x97CE, "Set up open RX on port &90 for the FS reply (TXCB[0] = &90, ctrl = &7F)", align=Align.INLINE)
d.comment(0x97D1, "Wait for the reply via the 3-level stack timer", align=Align.INLINE)
d.comment(0x97D4, "Restore caller's flags", align=Align.INLINE)
d.label(0x97D5, "loop_next_reply")

d.comment(0x97D5, "Step Y to next reply byte", align=Align.INLINE)
d.comment(0x97D6, "Read reply byte at txcb_start+Y", align=Align.INLINE)
d.comment(0x97D8, "Stash for the dispatch tests below", align=Align.INLINE)
d.comment(0x97D9, "Zero terminates: return", align=Align.INLINE)
d.comment(0x97DB, "V clear (caller's V): use code as-is", align=Align.INLINE)
d.comment(0x97DD, "V set: shift the code by +&2A (extended-error mapping)", align=Align.INLINE)
d.label(0x97DF, "process_reply_code")

d.comment(0x97DF, "Non-zero: dispatch as an error", align=Align.INLINE)
d.label(0x97E1, "rts_recv_reply")

d.comment(0x97E1, "Return", align=Align.INLINE)
d.label(0x97E2, "handle_disconnect")

d.comment(0x97E2, "Pull caller's pushed return state", align=Align.INLINE)
d.comment(0x97E3, "X=&C0: 'remote disconnect' status", align=Align.INLINE)
d.comment(0x97E5, "Step Y past the disconnect byte", align=Align.INLINE)
d.comment(0x97E6, "Send disconnect notification to remote", align=Align.INLINE)
d.comment(0x97E9, "C clear (success): continue scanning replies", align=Align.INLINE)
d.label(0x97EB, "store_reply_status")

d.comment(0x97EB, "Save the error code into &C009", align=Align.INLINE)
d.comment(0x97EE, "Read FS state byte at &C007", align=Align.INLINE)
d.comment(0x97F1, "Save flags so we can branch later", align=Align.INLINE)
d.comment(0x97F2, "FS state non-zero: data-loss check needed", align=Align.INLINE)
d.comment(0x97F4, "Reply was &BF (special: not a real error)?", align=Align.INLINE)
d.comment(0x97F6, "No: build error block", align=Align.INLINE)
d.label(0x97F8, "check_data_loss")

d.comment(0x97F8, "A=&40: 'channel-active' bitmask", align=Align.INLINE)
d.comment(0x97FA, "Push it onto the OR-accumulator", align=Align.INLINE)
d.comment(0x97FB, "Clear the FS-active bit (we're losing the connection)", align=Align.INLINE)
d.comment(0x97FE, "X=&F0: scan from channel offset &F0 upwards", align=Align.INLINE)
d.label(0x9800, "loop_scan_channels")

d.comment(0x9800, "Pull current OR accumulator", align=Align.INLINE)
d.comment(0x9801, "OR with channel status byte at &C1C8+X", align=Align.INLINE)
d.comment(0x9804, "Push back updated accumulator", align=Align.INLINE)
d.comment(0x9805, "Reload channel byte", align=Align.INLINE)
d.comment(0x9808, "Mask to top 2 bits (preserve TX/RX state)", align=Align.INLINE)
d.comment(0x980A, "Write back trimmed status", align=Align.INLINE)
d.comment(0x980D, "Step channel index", align=Align.INLINE)
d.comment(0x980E, "Loop while X bit 7 set (covers &F0..&FF)", align=Align.INLINE)
d.comment(0x9810, "Clear the FS state byte (no longer active)", align=Align.INLINE)
d.comment(0x9813, "Force-close all client channels", align=Align.INLINE)
d.comment(0x9816, "Pull final OR accumulator", align=Align.INLINE)
d.comment(0x9817, "Bit 0 (was bit 6 of any &40 byte) -> C", align=Align.INLINE)
d.comment(0x9818, "Any channel was active: skip the warning", align=Align.INLINE)
d.comment(0x981A, "No active channels were lost: print 'Data Lost' warning via inline string", align=Align.INLINE)
d.label(0x9827, "scan_channel_store_reply")

d.comment(0x9827, "Reload error code from &C009", align=Align.INLINE)
d.comment(0x982A, "Restore saved flags (was bit 7 of fs_flags)", align=Align.INLINE)
d.comment(0x982B, "Z set (no error): build the error block anyway", align=Align.INLINE)
d.comment(0x982D, "Pull caller's saved return state (3 bytes from PHP earlier)", align=Align.INLINE)
d.comment(0x9830, "Return -- caller dispatched on a non-error reply", align=Align.INLINE)
d.label(0x9831, "build_error_block")

d.comment(0x9831, "Y=1: skip past the leading TXCB control byte", align=Align.INLINE)
d.comment(0x9833, "Error code below &A8 (extended)?", align=Align.INLINE)
d.comment(0x9835, "No (>= &A8): proceed to copy", align=Align.INLINE)
d.comment(0x9837, "Yes: clamp to &A8 (truncate range)", align=Align.INLINE)
d.comment(0x9839, "Write clamped code back into TXCB", align=Align.INLINE)
d.label(0x983B, "setup_error_copy")

d.comment(0x983B, "Y=&FF: INY in loop bumps to 0", align=Align.INLINE)
d.label(0x983D, "loop_copy_error")

d.comment(0x983D, "Step Y", align=Align.INLINE)
d.comment(0x983E, "Read TXCB byte (error block content)", align=Align.INLINE)
d.comment(0x9840, "Copy to BRK error block at &0100+Y", align=Align.INLINE)
d.comment(0x9843, "EOR with CR; Z set when we just copied the terminator", align=Align.INLINE)
d.comment(0x9845, "Not yet at CR: continue copying", align=Align.INLINE)
d.comment(0x9847, "Write the CR terminator (Z still set so A=0; ensures cleanly terminated)", align=Align.INLINE)
d.comment(0x984A, "Step Y back so it points at the CR position", align=Align.INLINE)
d.comment(0x984B, "Move Y into A for the BRK", align=Align.INLINE)
d.comment(0x984C, "Move Y into X (caller convention)", align=Align.INLINE)
d.comment(0x984D, "Tail-jump into the BRK-dispatch error path", align=Align.INLINE)
d.label(0x9850, "lang_1_remote_boot")

d.subroutine(
    0x9850,
    "lang_1_remote_boot",
    title="Language reply 1: remote-boot init / continue",
    description="""Reads the reply byte at `(net_rx_ptr),0`. If zero, branches to
[`init_remote_session`](label:init_remote_session) to (re)initialise the
remote session. Otherwise falls through to `done_commit_state`
which finalises the boot state byte for the active session.""",
)


d.comment(0x9850, "Y=0: status byte offset", align=Align.INLINE)
d.entry(0x9850)
d.comment(0x9852, "Read RX status byte", align=Align.INLINE)
d.comment(0x9854, "Zero: re-init the session", align=Align.INLINE)
d.label(0x9856, "done_commit_state")

d.comment(0x9856, "Non-zero: commit state and continue", align=Align.INLINE)
d.label(0x9859, "init_remote_session")

d.comment(0x9859, "Mark session as 'remote boot'", align=Align.INLINE)
d.comment(0x985B, "Store updated status byte back to RX[0]", align=Align.INLINE)
d.comment(0x985D, "X=&80: caller machine-id byte offset", align=Align.INLINE)
d.comment(0x985F, "Y=&80: same offset", align=Align.INLINE)
d.comment(0x9861, "Read remote machine ID", align=Align.INLINE)
d.comment(0x9863, "Push -- save across the workspace store", align=Align.INLINE)
d.comment(0x9865, "Re-read for the second store target", align=Align.INLINE)
d.comment(0x9867, "Y=&0F: workspace machine-ID lo offset", align=Align.INLINE)
d.comment(0x9869, "Store at (nfs_workspace)+&0F", align=Align.INLINE)
d.comment(0x986B, "Y=&0E", align=Align.INLINE)
d.comment(0x986C, "Pop saved machine ID", align=Align.INLINE)
d.comment(0x986D, "Store at (nfs_workspace)+&0F (reuse)", align=Align.INLINE)
d.comment(0x986F, "Scan remote-key flags", align=Align.INLINE)
d.comment(0x9872, "Initialise narrow workspace template", align=Align.INLINE)
d.comment(0x9875, "X=1: enable Econet keyboard", align=Align.INLINE)
d.comment(0x9877, "Y=0", align=Align.INLINE)
d.comment(0x9879, "OSBYTE &C9: read/write Econet keyboard disable", align=Align.INLINE)
d.label(0x987E, "lang_3_exec_0100")

d.subroutine(
    0x987E,
    "lang_3_exec_0100",
    title="Language reply 3: raise 'Remoted' error at &0100",
    description="""Calls [`commit_state_byte`](label:commit_state_byte) to record the new state,
loads `A=0` and tail-calls [`error_inline_log`](label:error_inline_log) with
the inline string `Remoted` followed by `&07` (BEL). Used by
remote-language replies that need to abort the current operation
with a terminal beep + error. Never returns.""",
)


d.comment(0x987E, "Commit the language-reply state byte", align=Align.INLINE)
d.entry(0x987E)
d.comment(0x9881, "A=0: 'Bad' error code", align=Align.INLINE)
d.comment(0x9883, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.comment(0x988F, "Read escape_flag", align=Align.INLINE)
d.subroutine(
    0x988F,
    "check_escape_and_classify",
    title="Acknowledge escape (if pressed) and classify reply",
    description="""If escape_flag bit 7 is clear OR need_release_tube bit 7 is clear (so AND result has bit 7 clear), returns immediately via return_1. Otherwise acknowledges escape via OSBYTE &7E (clears the escape condition and runs escape effects), loads A=6 (a synthesized 'Escape' error class), and tail-jumps to classify_reply_error to build the 'Escape' BRK error block.

Two callers: cmd_pass (&8E07) for password-entry escape, and send_net_packet (&9B46) for in-flight TX escape.""",
    on_entry={},
    on_exit={"a": "preserved (return) or never returns (escape path)"},
)


d.comment(0x9891, "Mask with need_release_tube (escape-disable)", align=Align.INLINE)
d.comment(0x9893, "Bit 7 clear: not escaping, return", align=Align.INLINE)
d.subroutine(
    0x9895,
    "raise_escape_error",
    title="Acknowledge escape and raise classified error",
    description="""Issues OSBYTE &7E (acknowledge_escape -- clears the escape condition
and runs any registered escape effects), loads A=6, and tail-jumps to
classify_reply_error which builds the Escape error. Reached from
&98EF (after recv_and_process_reply detects escape) and &B808
(cmd_wipe's per-iteration escape check). Never returns -- the
classify_reply_error path triggers BRK.""",
    on_exit={"a": "6 (Escape error code passed to classify_reply_error)"},
)


d.comment(0x9895, "A=&7E: OSBYTE &7E = acknowledge Escape", align=Align.INLINE)
d.comment(0x989A, "A=6: error class for 'Escape'", align=Align.INLINE)
d.comment(0x989C, "JMP classify_reply_error (never returns)", align=Align.INLINE)
d.label(0x989F, "lang_4_validated")

d.subroutine(
    0x989F,
    "lang_4_validated",
    title="Language reply 4: validate remote session and apply",
    description="""Reads the first reply byte at `(net_rx_ptr),0`. If zero, branches
to [`init_remote_session`](label:init_remote_session) to set up a fresh remote
session. Otherwise reads the validation byte at offset `&80` and
the local stored value at workspace offset `&0E`; on mismatch,
the remote session is rejected.""",
)


d.comment(0x989F, "Y=0: status byte offset", align=Align.INLINE)
d.entry(0x989F)
d.comment(0x98A1, "Read RX status byte", align=Align.INLINE)
d.comment(0x98A3, "Zero status: re-init the session", align=Align.INLINE)
d.comment(0x98A5, "Y=&80: session-ID byte offset in RX", align=Align.INLINE)
d.comment(0x98A7, "Read remote session-ID", align=Align.INLINE)
d.comment(0x98A9, "Y=&0E: stored session-ID offset in workspace", align=Align.INLINE)
d.comment(0x98AB, "Compare with stored ID", align=Align.INLINE)
d.comment(0x98AD, "Mismatch: skip the commit (treat as foreign)", align=Align.INLINE)
d.label(0x98AF, "lang_0_insert_key")

d.subroutine(
    0x98AF,
    "lang_0_insert_key",
    title="Language reply 0: insert remote keypress",
    description="""Reads the keycode from the reply at `(net_rx_ptr),&82` into `Y`,
sets `X=0`, calls [`commit_state_byte`](label:commit_state_byte) to record
the state change, and issues `OSBYTE &99` (insert into keyboard
buffer) to deliver the keypress to the local machine.""",
    on_entry={"a": "ignored (entry from reply dispatch)"},
)


d.comment(0x98AF, "Y=&82: keypress byte offset in RX", align=Align.INLINE)
d.entry(0x98AF)
d.comment(0x98B1, "Read remote keypress code", align=Align.INLINE)
d.comment(0x98B3, "Y = key code", align=Align.INLINE)
d.comment(0x98B4, "X=0: keyboard buffer ID", align=Align.INLINE)
d.comment(0x98B6, "Commit the language-reply state", align=Align.INLINE)
d.comment(0x98B9, "OSBYTE &99: insert byte into input buffer", align=Align.INLINE)
d.label(0x98BE, "wait_net_tx_ack")

d.subroutine(
    0x98BE,
    "wait_net_tx_ack",
    title="Wait for reply on open receive with timeout",
    description="""Despite the name, this does **not** wait for a TX acknowledgment.
It polls an open receive control block (bit 7 of `txcb_ctrl`,
set to `&7F` by [`init_txcb_port`](label:init_txcb_port)) until the
NMI RX handler delivers a reply frame and sets bit 7.

Uses a three-level nested polling loop:

| Loop | Source | Default | Iterations |
|---|---|---|---|
| inner  | wraps from 0 | – | 256 |
| middle | wraps from 0 | – | 256 |
| outer  | [`rx_wait_timeout`](label:rx_wait_timeout) | `&28` (40) | 40 |

Total: `256 × 256 × 40 = 2,621,440` poll iterations. At ~17
cycles per poll on a 2 MHz 6502, the default gives ~22 seconds.

On timeout, branches to `build_no_reply_error` to raise
`'No reply'`. Called by 6 sites across the protocol stack.""",
)


d.comment(0x98BE, "Read the configurable rx-wait timeout (&0D6E, default &28 = ~22s on 2 MHz)", align=Align.INLINE)
d.comment(0x98C1, "Push it as the outermost counter (read back via stack-X indexing later)", align=Align.INLINE)
d.comment(0x98C2, "Read econet_flags so we can preserve it across the wait", align=Align.INLINE)
d.comment(0x98C5, "Push it (we'll temporarily set bit 7 to mark waiting)", align=Align.INLINE)
d.comment(0x98C6, "Check whether net_tx_ptr_hi is non-zero (TX in flight?)", align=Align.INLINE)
d.comment(0x98C8, "Yes: skip the flag-set; counters initialise either way", align=Align.INLINE)
d.comment(0x98CA, "TX idle: set bit 7 of econet_flags (signal RX-only wait)", align=Align.INLINE)
d.comment(0x98CC, "Write the modified flags back", align=Align.INLINE)
d.label(0x98CF, "init_poll_counters")

d.comment(0x98CF, "A=0: initial value for inner+middle counters", align=Align.INLINE)
d.comment(0x98D1, "Push it -- middle counter at stack[X+2]", align=Align.INLINE)
d.comment(0x98D2, "Push it again -- inner counter at stack[X+1]", align=Align.INLINE)
d.comment(0x98D3, "Y=0: indirect index for net_tx_ptr poll", align=Align.INLINE)
d.comment(0x98D4, "Capture S into X so we can address the stack counters", align=Align.INLINE)
d.label(0x98D5, "loop_poll_tx")

d.comment(0x98D5, "Read RX/TX flags through net_tx_ptr -- bit 7 set means complete", align=Align.INLINE)
d.comment(0x98D7, "Bit 7 set: reply received, exit poll", align=Align.INLINE)
d.comment(0x98D9, "Decrement inner counter at stack[X+1]", align=Align.INLINE)
d.comment(0x98DC, "Inner not zero yet: poll again", align=Align.INLINE)
d.comment(0x98DE, "Inner wrapped: decrement middle at stack[X+2]", align=Align.INLINE)
d.comment(0x98E1, "Middle not zero: poll again", align=Align.INLINE)
d.comment(0x98E3, "Middle wrapped: decrement outer at stack[X+4] (the saved timeout value)", align=Align.INLINE)
d.comment(0x98E6, "Outer not zero: poll again", align=Align.INLINE)
d.comment(0x98E8, "Reload the original timeout to test for timeout=0 mode", align=Align.INLINE)
d.comment(0x98EB, "Configured timeout was non-zero: declare timeout", align=Align.INLINE)
d.comment(0x98ED, "Timeout=0 (poll forever): check escape flag", align=Align.INLINE)
d.comment(0x98EF, "Escape pressed: jump to escape handler at &9895", align=Align.INLINE)
d.comment(0x98F1, "Reset outer counter so we keep polling", align=Align.INLINE)
d.comment(0x98F4, "Always taken (INC's result is always non-zero here): back to inner", align=Align.INLINE)
d.label(0x98F6, "done_poll_tx")

d.comment(0x98F6, "done_poll_tx: discard inner counter", align=Align.INLINE)
d.comment(0x98F7, "Discard middle counter", align=Align.INLINE)
d.comment(0x98F8, "Pull saved econet_flags", align=Align.INLINE)
d.comment(0x98F9, "Restore them (clearing bit 7 if we set it)", align=Align.INLINE)
d.comment(0x98FC, "Pull saved rx_wait_timeout into A", align=Align.INLINE)
d.comment(0x98FD, "If timeout reached zero, raise 'No reply'", align=Align.INLINE)
d.comment(0x98FF, "Reply received normally: return", align=Align.INLINE)
d.label(0x9900, "cond_save_error_code")

d.subroutine(
    0x9900,
    "cond_save_error_code",
    title="Conditionally store error code to workspace",
    description="""Tests bit 7 of [`fs_flags`](label:fs_flags) (FS-selected
flag):

| Bit 7 | Action |
|---|---|
| clear | return immediately |
| set   | store `A` into `hazel_fs_last_error` (`&0E09`) |

This guards against writing error state when no filing system
is active. Called internally by the error-classification chain
and by `error_inline_log`.""",
    on_entry={"a": "error code to store"},
)


d.comment(0x9900, "Test bit 7 of fs_flags (FS-active flag)", align=Align.INLINE)
d.comment(0x9903, "FS not active: skip the save", align=Align.INLINE)
d.comment(0x9905, "FS active: store error code at &C009 (last-error byte)", align=Align.INLINE)
d.label(0x9908, "rts_cond_save_err")

d.comment(0x9908, "Return", align=Align.INLINE)
d.label(0x9909, "build_no_reply_error")

d.comment(0x9909, "X=8: net_error_lookup_data offset for 'No reply' message", align=Align.INLINE)
d.comment(0x990B, "Y = message offset within the string table (&9AA4 base)", align=Align.INLINE)
d.comment(0x990E, "X=0: error-text buffer index", align=Align.INLINE)
d.comment(0x9910, "Zero the &0100 length byte (length will be filled in later)", align=Align.INLINE)
d.comment(0x9913, "Read first message byte (the error code)", align=Align.INLINE)
d.comment(0x9916, "Conditionally save it as last-error", align=Align.INLINE)
d.label(0x9919, "loop_copy_no_reply_msg")

d.comment(0x9919, "Read next message byte", align=Align.INLINE)
d.comment(0x991C, "Append to error-text buffer at &0101+X", align=Align.INLINE)
d.comment(0x991F, "Null terminator: message done", align=Align.INLINE)
d.comment(0x9921, "Step buffer index", align=Align.INLINE)
d.comment(0x9922, "Step source offset", align=Align.INLINE)
d.comment(0x9923, "Loop while Y != 0 (Y wraps at 256, not expected)", align=Align.INLINE)
d.label(0x9925, "done_no_reply_msg")

d.comment(0x9925, "Append ' on drive <num>' or similar context", align=Align.INLINE)
d.comment(0x9928, "A=0: null terminator", align=Align.INLINE)
d.comment(0x992A, "Store at end of message", align=Align.INLINE)
d.comment(0x992D, "Tail-jump to dispatch the BRK error", align=Align.INLINE)
d.label(0x9930, "fixup_reply_status_a")

d.subroutine(
    0x9930,
    "fixup_reply_status_a",
    title="Substitute 'B' for 'A' in reply status byte",
    description="""Reads the FS reply status byte at (net_tx_ptr,X). If it is 'A'
(Acknowledge with no error), substitutes 'B' so downstream code
treats it as a soft error. CLV before falling through into
mask_error_class to ensure the no-extended-error path is taken.""",
    on_entry={"x": "indirect index into net_tx_ptr"},
    on_exit={"a": "reply status byte (with A->B substitution)", "v": "0 (clear)"},
)


d.comment(0x9930, "Read FS reply status byte at (net_tx_ptr,X)", align=Align.INLINE)
d.comment(0x9932, "Status 'A'? (Acknowledge with no error)", align=Align.INLINE)
d.comment(0x9934, "Not 'A': pass through unchanged", align=Align.INLINE)
d.comment(0x9936, "Substitute 'B' for 'A' (handle ACK as a soft error)", align=Align.INLINE)
d.label(0x9938, "skip_if_not_a")

d.comment(0x9938, "Clear V to take the standard mask path", align=Align.INLINE)
d.comment(0x9939, "Always taken: use the standard masked-error path", align=Align.INLINE)
d.label(0x993B, "load_reply_and_classify")

d.subroutine(
    0x993B,
    "load_reply_and_classify",
    title="Load reply byte and classify error",
    description="""Single-byte prologue to
[`classify_reply_error`](label:classify_reply_error): `LDA (net_tx_ptr,X)`
reads the FS reply status byte, then falls through. Single
caller (`&9B6C`, after a recv-and-classify path that already
has `X` set).""",
    on_entry={"x": "indirect index into net_tx_ptr"},
)


d.comment(0x993B, "Read FS reply status byte", align=Align.INLINE)
d.label(0x993D, "classify_reply_error")

d.subroutine(
    0x993D,
    "classify_reply_error",
    title="Classify FS reply error code",
    description="""Forces `V=1` via `BIT always_set_v_byte` (signals the
extended-error path), masks the error code in `A` to 3 bits (the
error class 0..7), saves the class on the stack, and dispatches:

| Class | Path |
|---|---|
| 2 (station-related) | multi-line `build_no_reply_error` |
| other | `build_simple_error` |

Two callers: [`raise_escape_error`](label:raise_escape_error) (with
`A=6`) and the FS reply dispatch at `&A0E3`.""",
    on_entry={"a": "error code byte"},
)


d.comment(0x993D, "BIT $always_set_v_byte: force V=1 (extended-error path)", align=Align.INLINE)
d.label(0x9940, "mask_error_class")

d.comment(0x9940, "Mask to 3 bits (error class 0..7)", align=Align.INLINE)
d.comment(0x9942, "Save error class on stack", align=Align.INLINE)
d.comment(0x9943, "Class 2 = 'station-related' family?", align=Align.INLINE)
d.comment(0x9945, "No: build a simple one-line error", align=Align.INLINE)
d.comment(0x9947, "Class 2 yes: save flags so we can branch on V later", align=Align.INLINE)
d.comment(0x9948, "X = error class (=2)", align=Align.INLINE)
d.comment(0x9949, "Y = lookup-table offset", align=Align.INLINE)
d.comment(0x994C, "Read first message byte (error code)", align=Align.INLINE)
d.comment(0x994F, "Conditionally save it", align=Align.INLINE)
d.comment(0x9952, "X=0: text-buffer index", align=Align.INLINE)
d.comment(0x9954, "Zero length byte", align=Align.INLINE)
d.label(0x9957, "loop_copy_station_msg")

d.comment(0x9957, "Read message byte", align=Align.INLINE)
d.comment(0x995A, "Append to buffer", align=Align.INLINE)
d.comment(0x995D, "Null terminator -- station message done", align=Align.INLINE)
d.comment(0x995F, "Advance Y", align=Align.INLINE)
d.comment(0x9960, "Advance X", align=Align.INLINE)
d.comment(0x9961, "Loop until X wraps", align=Align.INLINE)
d.label(0x9963, "done_station_msg")

d.comment(0x9963, "Append ' on drive <num>' suffix", align=Align.INLINE)
d.comment(0x9966, "Restore the saved class flags", align=Align.INLINE)
d.comment(0x9967, "V was set: use 'not listening' suffix", align=Align.INLINE)
d.comment(0x9969, "A=&A4: 'station <n> not available' error code", align=Align.INLINE)
d.comment(0x996B, "Save the alternative error code", align=Align.INLINE)
d.comment(0x996E, "Patch error-text buffer length byte", align=Align.INLINE)
d.comment(0x9971, "Y=&0B: lookup index for the listening-station suffix", align=Align.INLINE)
d.comment(0x9973, "Always taken (Y is non-zero); jump to load_suffix_offset", align=Align.INLINE)
d.label(0x9975, "suffix_not_listening")

d.comment(0x9975, "V was clear: 'not listening' suffix variant", align=Align.INLINE)
d.label(0x9977, "load_suffix_offset")

d.comment(0x9977, "Read suffix offset from lookup", align=Align.INLINE)
d.comment(0x997A, "Y = suffix offset", align=Align.INLINE)
d.label(0x997B, "loop_copy_suffix")

d.comment(0x997B, "Read suffix byte", align=Align.INLINE)
d.comment(0x997E, "Append", align=Align.INLINE)
d.comment(0x9981, "Null: suffix done", align=Align.INLINE)
d.comment(0x9983, "Step Y", align=Align.INLINE)
d.label(0x9984, "suffix_copy_loop")

d.comment(0x9984, "Step X", align=Align.INLINE)
d.comment(0x9985, "Loop while X != 0 (max 255 chars)", align=Align.INLINE)
d.label(0x9987, "done_suffix")

d.comment(0x9987, "Always taken (Z still set from BEQ): final terminator check", align=Align.INLINE)
d.label(0x9989, "build_simple_error")

d.comment(0x9989, "X = error class", align=Align.INLINE)
d.comment(0x998A, "Y = lookup-table offset", align=Align.INLINE)
d.comment(0x998D, "X=0: buffer index", align=Align.INLINE)
d.comment(0x998F, "Zero length", align=Align.INLINE)
d.comment(0x9992, "Read first message byte (error code)", align=Align.INLINE)
d.comment(0x9995, "Conditionally save it", align=Align.INLINE)
d.label(0x9998, "loop_copy_error_msg")

d.comment(0x9998, "Read next message byte", align=Align.INLINE)
d.comment(0x999B, "Append to buffer", align=Align.INLINE)
d.label(0x999E, "check_msg_terminator")

d.comment(0x999E, "Null terminator -> dispatch", align=Align.INLINE)
d.comment(0x99A0, "Step Y", align=Align.INLINE)
d.comment(0x99A1, "Step X", align=Align.INLINE)
d.label(0x99A2, "bad_str_anchor")

d.comment(0x99A2, "Loop while X != 0", align=Align.INLINE)
d.label(0x99A3, "bad_prefix_table")

d.hook_subroutine(0x99A7, "error_bad_inline", stringz_hook)

d.subroutine(
    0x99A7,
    "error_bad_inline",
    title="Generate 'Bad ...' BRK error from inline string",
    description="""Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""",
    on_entry={"a": "error number"},
)
d.comment(0x99A7, "Conditionally log error code to workspace", align=Align.INLINE)
d.comment(0x99AA, "Save error number in Y", align=Align.INLINE)
d.comment(0x99AB, "Pop return address (low) — points to last byte of JSR", align=Align.INLINE)
d.comment(0x99AC, "Store return address low", align=Align.INLINE)
d.comment(0x99AE, "Pop return address (high)", align=Align.INLINE)
d.comment(0x99AF, "Store return address high", align=Align.INLINE)
d.comment(0x99B1, "X=0: start of prefix string", align=Align.INLINE)
d.label(0x99B3, "loop_copy_bad_prefix")

d.comment(0x99B3, "Copy 'Bad ' prefix from lookup table", align=Align.INLINE)
d.comment(0x99B4, "Get next prefix character", align=Align.INLINE)
d.comment(0x99B7, "Store in error text buffer", align=Align.INLINE)
d.comment(0x99BA, "Is it space (end of 'Bad ')?", align=Align.INLINE)
d.comment(0x99BC, "No: copy next prefix character", align=Align.INLINE)
d.hook_subroutine(0x99C0, "error_inline_log", stringz_hook)
d.subroutine(
    0x99C0,
    "error_inline_log",
    title="Generate BRK error from inline string (with logging)",
    description="""Like error_inline, but first conditionally logs the error code to
workspace via cond_save_error_code before building the error block.""",
    on_entry={"a": "error number"},
)
d.comment(0x99C0, "Conditionally log error code to workspace", align=Align.INLINE)


d.hook_subroutine(0x99C3, "error_inline", stringz_hook)
d.subroutine(
    0x99C3,
    "error_inline",
    title="Generate BRK error from inline string",
    description="""Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""",
    on_entry={"a": "error number (stored in error block at &0101)"},
)
d.comment(0x99C3, "Save error number in Y", align=Align.INLINE)
d.comment(0x99C4, "Pop return address (low) — points to last byte of JSR", align=Align.INLINE)
d.comment(0x99C5, "Store return address low", align=Align.INLINE)
d.comment(0x99C7, "Pop return address (high)", align=Align.INLINE)


d.comment(0x99C8, "Store return address high", align=Align.INLINE)
d.comment(0x99CA, "X=0: error text index", align=Align.INLINE)
d.label(0x99CC, "write_error_num_and_str")

d.comment(0x99CC, "Store error number in error block", align=Align.INLINE)
d.comment(0x99CF, "Copy error number to A", align=Align.INLINE)
d.comment(0x99D0, "Push error number on stack", align=Align.INLINE)
d.comment(0x99D1, "Y=0: inline string index", align=Align.INLINE)
d.comment(0x99D3, "Zero the BRK byte at &0100", align=Align.INLINE)
d.label(0x99D6, "loop_copy_inline_str")

d.comment(0x99D6, "Copy inline string into error block", align=Align.INLINE)
d.comment(0x99D7, "Advance string index", align=Align.INLINE)
d.comment(0x99D8, "Read next byte from inline string", align=Align.INLINE)
d.comment(0x99DA, "Store byte in error block", align=Align.INLINE)
d.comment(0x99DD, "Loop until null terminator", align=Align.INLINE)
d.label(0x99DF, "check_net_error_code")

d.subroutine(
    0x99DF,
    "check_net_error_code",
    title="Translate net error: 'OK' → return, 'FS error' → append",
    description="""Reads the receive-attribute byte:

| Receive attribute | Action |
|---|---|
| non-zero | network error – branch to `handle_net_error` |
| zero, saved error = `&DE` (FS error code) | branch to `append_error_number` to add the FS-specific code to the error text |
| zero, saved error other | tail-jump to `&0100` (BRK error block) to trigger BRK and let MOS dispatch |

**How the compound "Station n.n ..." message picks its
suffix.** The status byte is masked to an error class
(`AND #7`); class 2 ("Station") appends the station address and
then one of two suffixes, chosen by the **V flag**:

| V | Suffix appended  | Set by                            |
|---|------------------|-----------------------------------|
| 1 | " not listening" | [`classify_reply_error`](label:classify_reply_error) — `BIT bit_test_ff` |
| 0 | " not present"   | this entry — the `CLV` below      |

So the two halves come from different sources, not different
failures: "not listening" is what a *remote reply* or the
general [`send_net_packet`](label:send_net_packet) path
produces, while "not present" is reserved for the probe that
reaches the classifier through here.

The `'A'` → `'B'` fixup exists to make that work. A local TX
failure stores &41 (`'A'`, 'not listening') in TXCB byte 0, and
&41 AND 7 = 1 would classify as "Net error". Rewriting it to
&42 (`'B'`) yields class 2, so the message becomes
"Station n.n" — and the `CLV` two instructions later selects
"not present" for it. This is why a MachinePeek at an absent
station reports `Station n.n not present` rather than "not
listening", even though the underlying TX result code is the
not-listening one.""",
)


d.comment(0x99DF, "Read receive attribute byte", align=Align.INLINE)
d.comment(0x99E2, "Non-zero: network returned an error", align=Align.INLINE)
d.comment(0x99E4, "Pop saved error number", align=Align.INLINE)
d.comment(0x99E5, "Was it &DE (file server error)?", align=Align.INLINE)
d.comment(0x99E7, "Yes: append error number and trigger BRK", align=Align.INLINE)
d.label(0x99E9, "trigger_brk")

d.comment(0x99E9, "Jump to BRK via error block", align=Align.INLINE)
d.label(0x99EC, "handle_net_error")

d.comment(0x99EC, "Store error code in workspace", align=Align.INLINE)
d.comment(0x99EF, "Push error code", align=Align.INLINE)
d.comment(0x99F0, "Save X (error text index)", align=Align.INLINE)
d.comment(0x99F1, "Push X", align=Align.INLINE)
d.comment(0x99F2, "Read receive attribute byte", align=Align.INLINE)
d.comment(0x99F5, "Save to fs_load_addr as spool handle", align=Align.INLINE)
d.comment(0x99F7, "A=0: clear error code in RX buffer", align=Align.INLINE)
d.comment(0x99F9, "Zero the error code byte in buffer", align=Align.INLINE)
d.comment(0x99FB, "A=&C6: OSBYTE read spool handle", align=Align.INLINE)
d.comment(0x99FD, "Read current spool file handle", align=Align.INLINE)
d.comment(0x9A00, "Compare Y result with saved handle", align=Align.INLINE)
d.comment(0x9A02, "Match: close the spool file", align=Align.INLINE)
d.comment(0x9A04, "Compare X result with saved handle", align=Align.INLINE)
d.comment(0x9A06, "No match: skip spool close", align=Align.INLINE)
d.comment(0x9A08, "Push A (preserved)", align=Align.INLINE)
d.comment(0x9A09, "A=&C6: disable spool with OSBYTE", align=Align.INLINE)
d.comment(0x9A0B, "ALWAYS branch to close spool", align=Align.INLINE)
d.label(0x9A0D, "net_error_close_spool")

d.comment(0x9A0E, "A=&C7: OSBYTE 'flush input buffer'", align=Align.INLINE)
d.label(0x9A10, "close_spool_exec")

d.comment(0x9A10, "Tail-call OSBYTE with X=0/Y=0", align=Align.INLINE)
d.comment(0x9A14, "A=0: close file", align=Align.INLINE)
d.comment(0x9A16, "Close the spool/exec file", align=Align.INLINE)
d.label(0x9A19, "done_close_files")

d.comment(0x9A19, "Pull saved X (error text index)", align=Align.INLINE)
d.comment(0x9A1A, "Restore X", align=Align.INLINE)
d.comment(0x9A1B, "Y=&0A: lookup index for 'on channel'", align=Align.INLINE)
d.comment(0x9A1D, "Load message offset from lookup table", align=Align.INLINE)
d.comment(0x9A20, "Transfer offset to Y", align=Align.INLINE)
d.label(0x9A21, "loop_copy_channel_msg")

d.comment(0x9A21, "Load error message byte", align=Align.INLINE)
d.comment(0x9A24, "Append to error text buffer", align=Align.INLINE)
d.comment(0x9A27, "Null terminator: done copying", align=Align.INLINE)
d.comment(0x9A29, "Advance error text index", align=Align.INLINE)
d.comment(0x9A2A, "Advance message index", align=Align.INLINE)
d.comment(0x9A2B, "Loop until full message copied", align=Align.INLINE)
d.label(0x9A2D, "append_error_number")

d.comment(0x9A2D, "Save error text end position", align=Align.INLINE)
d.comment(0x9A2F, "Pull saved error number", align=Align.INLINE)
d.comment(0x9A30, "Append ' nnn' error number suffix", align=Align.INLINE)
d.comment(0x9A33, "A=0: null terminator", align=Align.INLINE)
d.comment(0x9A35, "Terminate error text string", align=Align.INLINE)
d.comment(0x9A38, "ALWAYS branch to trigger BRK error", align=Align.INLINE)
d.label(0x9A3A, "append_drv_dot_num")

d.subroutine(
    0x9A3A,
    "append_drv_dot_num",
    title="Append 'net.station' decimal string to error text",
    description="""Reads network and station numbers from the TX control block at
offsets 3 and 2. Writes:

1. A space separator.
2. The network number as decimal (if non-zero).
3. A dot (`'.'`).
4. The station number as decimal digits.

into the error-text buffer at the current position.""",
    on_entry={"x": "error text buffer index"},
    on_exit={"x": "updated buffer index past appended text"},
)


d.comment(0x9A3A, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9A3C, "Append space to error text", align=Align.INLINE)
d.comment(0x9A3F, "Advance error text index", align=Align.INLINE)
d.comment(0x9A40, "Save position for number formatting", align=Align.INLINE)
d.comment(0x9A42, "Y=3: offset to network number in TX CB", align=Align.INLINE)
d.comment(0x9A44, "Load network number", align=Align.INLINE)
d.comment(0x9A46, "Zero: skip network part (local)", align=Align.INLINE)
d.comment(0x9A48, "Append network number as decimal", align=Align.INLINE)
d.comment(0x9A4B, "Reload error text position", align=Align.INLINE)
d.comment(0x9A4D, "A='.': dot separator", align=Align.INLINE)
d.comment(0x9A4F, "Append dot to error text", align=Align.INLINE)
d.comment(0x9A52, "Advance past dot", align=Align.INLINE)
d.label(0x9A54, "append_station_num")

d.comment(0x9A54, "Y=2: offset to station number in TX CB", align=Align.INLINE)
d.comment(0x9A56, "Load station number", align=Align.INLINE)
d.comment(0x9A58, "Append station number as decimal", align=Align.INLINE)
d.comment(0x9A5B, "Reload error text position", align=Align.INLINE)
d.comment(0x9A5D, "Return", align=Align.INLINE)
d.label(0x9A5E, "append_space_and_num")

d.subroutine(
    0x9A5E,
    "append_space_and_num",
    title="Append space and decimal number to error text",
    description="""Writes a space character to the error text buffer
at the current position (fs_load_addr_2), then falls
through to append_decimal_num to convert the value
in A to decimal digits with leading zero suppression.""",
    on_entry={"a": "number to append (0-255)"},
)


d.comment(0x9A5E, "Save number in Y", align=Align.INLINE)
d.comment(0x9A5F, "A=' ': space prefix", align=Align.INLINE)
d.comment(0x9A61, "Load current error text position", align=Align.INLINE)
d.comment(0x9A63, "Append space to error text", align=Align.INLINE)
d.comment(0x9A66, "Advance position past space", align=Align.INLINE)
d.comment(0x9A68, "Restore number to A", align=Align.INLINE)
d.label(0x9A69, "append_decimal_num")

d.subroutine(
    0x9A69,
    "append_decimal_num",
    title="Convert byte to decimal and append to error text",
    description="""Extracts hundreds, tens and units digits by three
successive calls to append_decimal_digit. Uses the
V flag to suppress leading zeros — hundreds and tens
are skipped when zero, but the units digit is always
emitted.""",
    on_entry={"a": "number to convert (0-255)"},
)


d.comment(0x9A69, "Save number in Y for division", align=Align.INLINE)
d.comment(0x9A6A, "Set V: suppress leading zeros", align=Align.INLINE)
d.comment(0x9A6D, "A=100: hundreds digit divisor", align=Align.INLINE)
d.comment(0x9A6F, "Extract and append hundreds digit", align=Align.INLINE)
d.comment(0x9A72, "A=10: tens digit divisor", align=Align.INLINE)
d.comment(0x9A74, "Extract and append tens digit", align=Align.INLINE)
d.comment(0x9A77, "A=1: units digit (remainder)", align=Align.INLINE)
d.comment(0x9A79, "Clear V: always print units digit", align=Align.INLINE)
d.label(0x9A7A, "append_decimal_digit")

d.subroutine(
    0x9A7A,
    "append_decimal_digit",
    title="Extract and append one decimal digit",
    description="""Divides Y by A using repeated subtraction to extract
a single decimal digit. Stores the ASCII digit in the
error text buffer at fs_load_addr_2 unless V is set
and the quotient is zero (leading zero suppression).
Returns the remainder in Y for subsequent digit
extraction.""",
    on_entry={"a": "divisor (100, 10, or 1)", "y": "number to divide", "v": "set to suppress leading zero"},
    on_exit={"y": "remainder after division", "v": "clear once a non-zero digit is emitted"},
)


d.comment(0x9A7A, "Store divisor", align=Align.INLINE)
d.comment(0x9A7C, "Copy number to A for division", align=Align.INLINE)
d.comment(0x9A7D, "X='0'-1: digit counter (ASCII offset)", align=Align.INLINE)
d.comment(0x9A7F, "Save V flag (leading zero suppression)", align=Align.INLINE)
d.comment(0x9A80, "Set carry for subtraction", align=Align.INLINE)
d.label(0x9A81, "loop_count_digit")

d.comment(0x9A81, "Increment digit counter", align=Align.INLINE)
d.comment(0x9A82, "Subtract divisor", align=Align.INLINE)
d.comment(0x9A84, "Not negative yet: continue counting", align=Align.INLINE)
d.comment(0x9A86, "Add back divisor (restore remainder)", align=Align.INLINE)
d.comment(0x9A88, "Restore V flag", align=Align.INLINE)
d.comment(0x9A89, "Save remainder back to Y", align=Align.INLINE)
d.comment(0x9A8A, "Digit counter to A (ASCII digit)", align=Align.INLINE)
d.comment(0x9A8B, "Is digit '0'?", align=Align.INLINE)
d.comment(0x9A8D, "Non-zero: always print", align=Align.INLINE)
d.comment(0x9A8F, "V set (suppress leading zeros): skip", align=Align.INLINE)
d.label(0x9A91, "store_digit")

d.comment(0x9A91, "Clear V: first non-zero digit seen", align=Align.INLINE)
d.comment(0x9A92, "Load current text position", align=Align.INLINE)
d.comment(0x9A94, "Store ASCII digit in error text", align=Align.INLINE)
d.comment(0x9A97, "Advance text position", align=Align.INLINE)
d.label(0x9A99, "rts_store_digit")

d.comment(0x9A99, "Return", align=Align.INLINE)
d.index_base(0x9A9A, "net_error_lookup_data")
d.banner(
    0x9A9A,
    title="Net-error class -> error_msg_table offset (12 bytes)",
    description="""Maps Econet network-error classes to byte offsets into
[`error_msg_table`](label:error_msg_table).

- Indices 0-7 are keyed by error class (the reply byte AND `7`).
- Index 8 is used by `build_no_reply_error` to locate the
  '`No reply from station`' message head.
- Indices 9-11 point to the suffix strings appended after the
  station address in compound errors ('` not listening`',
  '` on channel`', '` not present`').

Each byte is computed as `<message-label> - error_msg_table` so the
table reflows automatically if a message string is edited.""",
)
for i in range(12):
    d.byte(0x9A9A + i)
d.expr(0x9A9B, sym("msg_net_error") - sym("error_msg_table"))
d.expr(0x9A9C, sym("msg_station") - sym("error_msg_table"))
d.expr(0x9A9D, sym("msg_no_clock") - sym("error_msg_table"))
d.expr(0x9A9E, sym("msg_escape") - sym("error_msg_table"))
d.expr(0x9A9F, sym("msg_escape") - sym("error_msg_table"))
d.expr(0x9AA0, sym("msg_escape") - sym("error_msg_table"))
d.expr(0x9AA1, sym("msg_bad_option") - sym("error_msg_table"))
d.expr(0x9AA2, sym("msg_no_reply") - sym("error_msg_table"))
d.expr(0x9AA3, sym("msg_not_listening") - sym("error_msg_table"))
d.expr(0x9AA4, sym("msg_on_channel") - sym("error_msg_table"))
d.expr(0x9AA5, sym("msg_not_present") - sym("error_msg_table"))

d.index_base(0x9AA6, "error_msg_table")
d.banner(
    0x9AA6,
    title="Net-error message strings",
    description="""Body of error-text fragments referenced by
[`net_error_lookup_data`](label:net_error_lookup_data). Two layouts coexist:

1. **Error entries** (offsets 0..&3F) — one byte holding the BRK
   error code, immediately followed by the null-terminated
   message string:

   ```
   <err_code> <message-bytes...> &00
   ```

2. **Suffix entries** (offsets &56, &65, &71) — bare
   null-terminated strings appended to a built-up error message;
   no leading error-code byte.

Per-byte inline comments below name each error code and message;
the bytes from this table are read by `build_simple_error` and
`build_no_reply_error` when classifying a network reply.""",
)

d.comment(0x9AA7, "err_line_jammed = &A0", align=Align.INLINE)
d.comment(0x9AB2, "Null terminator", align=Align.INLINE)
d.label(0x9AB3, "msg_net_error")

d.comment(0x9AB3, "Error &A1: Net error", align=Align.INLINE)
d.comment(0x9AB4, "err_net_error = &A1", align=Align.INLINE)
d.comment(0x9ABD, "Null terminator", align=Align.INLINE)
d.label(0x9ABE, "msg_station")

d.comment(0x9ABE, "Error &A2: Station", align=Align.INLINE)
d.label(0x9AC7, "msg_no_clock")

d.byte(0x9AD0)
d.comment(0x9AD0, "Null terminator", align=Align.INLINE)
d.label(0x9AD1, "msg_escape")

d.byte(0x9AD1)
d.comment(0x9AD1, "Error &11: Escape", align=Align.INLINE)
d.label(0x9AD9, "msg_bad_option")

d.byte(0x9AD9)
d.comment(0x9AD9, "Error &CB: Bad option", align=Align.INLINE)
d.comment(0x9AE4, "Null terminator + Error &A5: No reply from station", align=Align.INLINE)
d.label(0x9AE5, "msg_no_reply")

d.comment(0x9AE6, "err_no_reply = &A5 message body", align=Align.INLINE)
d.comment(0x9AFB, "Null terminator", align=Align.INLINE)
d.label(0x9AFC, "msg_not_listening")

d.comment(0x9AFC, "Suffix string (offset &56 in lookup)", align=Align.INLINE)
d.byte(0x9B0A)
d.comment(0x9B0A, "Null terminator", align=Align.INLINE)
d.label(0x9B0B, "msg_on_channel")

d.comment(0x9B0B, 'Suffix: \\" on channel\\"', align=Align.INLINE)
d.byte(0x9B16)
d.comment(0x9B16, "Null terminator", align=Align.INLINE)
d.label(0x9B17, "msg_not_present")
d.comment(0x9B17, 'Suffix: \\" not present\\"', align=Align.INLINE)
d.comment(0x9B23, "Null terminator", align=Align.INLINE)
d.label(0x9B24, "init_tx_ptr_and_send")

d.subroutine(
    0x9B24,
    "init_tx_ptr_and_send",
    title="Point TX at zero-page TXCB and send",
    description="""Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the
standard TXCB location in zero page), then falls
through to send_net_packet for transmission with
retry logic.""",
    on_exit={"a": "TX result code (0 = success; &40 jammed; &41 not listening; etc.) -- see send_net_packet"},
)


d.comment(0x9B24, "X=&C0: TX control block base (low)", align=Align.INLINE)
d.comment(0x9B26, "Set TX pointer low", align=Align.INLINE)
d.comment(0x9B28, "X=0: TX control block base (high)", align=Align.INLINE)
d.comment(0x9B2A, "Set TX pointer high (page 0)", align=Align.INLINE)
d.label(0x9B2C, "send_net_packet")

d.subroutine(
    0x9B2C,
    "send_net_packet",
    title="Transmit Econet packet with retry",
    description="""Two-phase transmit with retry. Loads retry count from
[`tx_retry_count`](label:tx_retry_count) (default `&FF` = 255; 0
means retry forever). Each failed attempt waits in a nested
delay loop: `X` = TXCB control byte (typically `&80`), `Y` =
`&60`; total ~61 ms at 2 MHz (ROM-only fetches, unaffected by
video mode).

| Phase | Activation | Behaviour |
|---|---|---|
| 1 | always | runs the full count with escape disabled |
| 2 | only when `tx_retry_count = 0` | sets `need_release_tube` to enable escape checking, retries indefinitely |

With default `&FF`, phase 2 is never entered. Failures go to
[`load_reply_and_classify`](label:load_reply_and_classify) (`'Line jammed'`,
`'Net error'`, etc.), distinct from the `'No reply'` timeout in
[`wait_net_tx_ack`](label:wait_net_tx_ack).""",
    on_exit={"a": "TX result (0 = success; non-zero = error class consumed by the BRK path)"},
)


d.comment(0x9B2C, "Load retry count from workspace", align=Align.INLINE)
d.comment(0x9B2F, "Non-zero: use configured retry count", align=Align.INLINE)
d.comment(0x9B31, "A=&FF: default retry count (255)", align=Align.INLINE)
d.label(0x9B33, "set_timeout")

d.comment(0x9B33, "Y=&60: timeout value", align=Align.INLINE)
d.comment(0x9B35, "Push retry count", align=Align.INLINE)
d.comment(0x9B36, "A=&60: copy timeout to A", align=Align.INLINE)
d.comment(0x9B37, "Push timeout", align=Align.INLINE)
d.comment(0x9B38, "X=0: TX pointer index", align=Align.INLINE)
d.comment(0x9B3A, "Load first byte of TX control block", align=Align.INLINE)
d.label(0x9B3C, "start_tx_attempt")

d.comment(0x9B3C, "Restore control byte (overwritten by result code on retry)", align=Align.INLINE)
d.comment(0x9B3E, "Push control byte", align=Align.INLINE)
d.comment(0x9B3F, "Poll ADLC until line idle", align=Align.INLINE)
d.comment(0x9B42, "Bit 6 (error flag) into N", align=Align.INLINE)
d.comment(0x9B43, "N=0 (bit 6 clear): success", align=Align.INLINE)
d.comment(0x9B45, "Shift away error flag, keep error type", align=Align.INLINE)
d.comment(0x9B46, "Z=1 (no type bits): fatal; Z=0: retryable", align=Align.INLINE)
d.comment(0x9B48, "Check for escape condition", align=Align.INLINE)
d.comment(0x9B4B, "Pull control byte", align=Align.INLINE)
d.comment(0x9B4C, "Restore to X", align=Align.INLINE)
d.comment(0x9B4D, "Pull timeout", align=Align.INLINE)
d.comment(0x9B4E, "Restore to Y", align=Align.INLINE)
d.comment(0x9B4F, "Pull retry count", align=Align.INLINE)
d.comment(0x9B50, "Zero retries remaining: try alternate", align=Align.INLINE)
d.label(0x9B52, "loop_retry_tx")

d.comment(0x9B52, "Decrement retry counter", align=Align.INLINE)
d.comment(0x9B54, "Push updated retry count", align=Align.INLINE)
d.comment(0x9B55, "Copy timeout to A", align=Align.INLINE)
d.comment(0x9B56, "Push timeout for delay loop", align=Align.INLINE)
d.comment(0x9B57, "Copy control byte to A", align=Align.INLINE)
d.label(0x9B58, "loop_tx_delay")

d.comment(0x9B58, "Inner delay: decrement X", align=Align.INLINE)
d.comment(0x9B59, "Loop until X=0", align=Align.INLINE)
d.comment(0x9B5B, "Decrement outer counter Y", align=Align.INLINE)
d.comment(0x9B5C, "Loop until Y=0", align=Align.INLINE)
d.comment(0x9B5E, "ALWAYS branch: retry transmission", align=Align.INLINE)
d.label(0x9B60, "try_alternate_phase")

d.comment(0x9B60, "Compare retry count with alternate", align=Align.INLINE)
d.comment(0x9B63, "Different: go to error handling", align=Align.INLINE)
d.comment(0x9B65, "A=&80: set escapable flag", align=Align.INLINE)
d.comment(0x9B67, "Mark as escapable for second phase", align=Align.INLINE)
d.comment(0x9B69, "ALWAYS branch: retry with escapable", align=Align.INLINE)
d.label(0x9B6B, "tx_send_error")

d.comment(0x9B6B, "Result code to X", align=Align.INLINE)
d.comment(0x9B6C, "Jump to classify reply and return", align=Align.INLINE)
d.label(0x9B6F, "tx_success")

d.comment(0x9B6F, "Pull control byte", align=Align.INLINE)
d.comment(0x9B70, "Pull timeout", align=Align.INLINE)
d.comment(0x9B71, "Pull retry count", align=Align.INLINE)
d.comment(0x9B72, "Clear escapable flag and return", align=Align.INLINE)
d.index_base(0x9B75, "pass_txbuf_init_table")
d.banner(
    0x9B75,
    title="Pass-through TX buffer template (12 bytes)",
    description="""Overlaid onto the TX control block by
[`setup_pass_txbuf`](label:setup_pass_txbuf) for pass-through operations.
The 12 bytes follow the Econet TXCB layout used elsewhere in this
ROM (compare [`bridge_rxcb_init_data`](label:bridge_rxcb_init_data)):

| Offset | Field |
|---|---|
| 0     | TX control byte (`&88` = immediate TX)        |
| 1     | TX port (`&00` = immediate op)                |
| 2-3   | dest station / network (`&FD` skip = preserve)|
| 4-5   | buffer start address (lo, hi)                  |
| 6-7   | extended-address fill (`&FF&FF`)               |
| 8-9   | buffer end address (lo, hi)                    |
| 10-11 | extended-address fill (`&FF&FF`)               |

The buffer spans [`&0D3A`..`&0D3E`](address:0D3D) -- the bytes
immediately preceding [`rx_src_stn`](label:rx_src_stn) through
[`net_frame_flags`](label:net_frame_flags) -- so the same RX-area bytes are
echoed back as the TX payload (hence "pass-through"). The
`&FF&FF` filler bytes at offsets 6-7 and 10-11 are a software
convention left over from a 4-byte-address format the BBC
Econet driver anticipated; for main-RAM buffers they're left
as `&FF&FF`. Original TX buffer values are pushed on the stack
and restored after transmission.

At the default 255 retries the inter-attempt delays alone come
to roughly 255 x 61 ms, about 15.5 seconds, on top of however
long each attempt spends inside
[`poll_adlc_tx_status`](label:poll_adlc_tx_status) — which is
itself unbounded, so this count places no ceiling on the total
wait.""",
)
for i in range(12):
    d.byte(0x9B75 + i)

d.comment(0x9B75, "Offset 0: ctrl = &88 (immediate TX)", align=Align.INLINE)
d.comment(0x9B76, "Offset 1: port = &00 (immediate op)", align=Align.INLINE)
d.comment(0x9B77, "Offset 2: &FD skip (preserve dest stn)", align=Align.INLINE)
d.comment(0x9B78, "Offset 3: &FD skip (preserve dest net)", align=Align.INLINE)
d.comment(0x9B79, "Offset 4: buf start lo (&3A) -> &0D3A", align=Align.INLINE)
d.comment(0x9B7A, "Offset 5: buf start hi (&0D) -> &0D3A", align=Align.INLINE)
d.comment(0x9B7B, "Offset 6: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x9B7C, "Offset 7: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x9B7D, "Offset 8: buf end lo (&3E) -> &0D3E", align=Align.INLINE)
d.comment(0x9B7E, "Offset 9: buf end hi (&0D) -> &0D3E", align=Align.INLINE)
d.comment(0x9B7F, "Offset 10: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x9B80, "Offset 11: extended-addr fill (&FF)", align=Align.INLINE)
d.label(0x9B81, "init_tx_ptr_for_pass")

d.subroutine(
    0x9B81,
    "init_tx_ptr_for_pass",
    title="Set up TX pointer and send pass-through packet",
    description="""Copies the template into the TX buffer (skipping
&FD markers), saves original values on stack,
then polls the ADLC and retries until complete.""",
    on_exit={"a": "TX result (from poll_adlc_tx_status)"},
)


d.comment(0x9B81, "Y=&C0: TX control block base (low)", align=Align.INLINE)
d.comment(0x9B83, "Set TX pointer low byte", align=Align.INLINE)
d.comment(0x9B85, "Y=0: TX control block base (high)", align=Align.INLINE)
d.comment(0x9B87, "Set TX pointer high byte", align=Align.INLINE)
d.label(0x9B89, "setup_pass_txbuf")

d.subroutine(
    0x9B89,
    "setup_pass_txbuf",
    title="Initialise TX buffer from pass-through template",
    description="""Copies 12 bytes from pass_txbuf_init_table into the
TX control block, pushing the original values on the
stack for later restoration. Skips offsets marked &FD
in the template. Starts transmission via
poll_adlc_tx_status and retries on failure, restoring
the original TX buffer contents when done.""",
    on_exit={"a": "TX result (from poll_adlc_tx_status)"},
)


d.comment(0x9B89, "Y=&0B: 12 bytes to process (0-11)", align=Align.INLINE)
d.label(0x9B8B, "loop_copy_template")

d.comment(0x9B8B, "Load template byte for this offset", align=Align.INLINE)
d.comment(0x9B8E, "Is it &FD (skip marker)?", align=Align.INLINE)
d.comment(0x9B90, "Yes: skip this offset, don't modify", align=Align.INLINE)
d.comment(0x9B92, "Load existing TX buffer byte", align=Align.INLINE)
d.comment(0x9B94, "Save original value on stack", align=Align.INLINE)
d.comment(0x9B95, "Copy template value to A", align=Align.INLINE)
d.comment(0x9B96, "Store template value to TX buffer", align=Align.INLINE)
d.label(0x9B98, "skip_template_byte")

d.comment(0x9B98, "Next offset (descending)", align=Align.INLINE)
d.comment(0x9B99, "Loop until all 12 bytes processed", align=Align.INLINE)
d.comment(0x9B9B, "Load pass-through control value", align=Align.INLINE)
d.comment(0x9B9E, "Push control value", align=Align.INLINE)
d.comment(0x9B9F, "A=&FF (Y is &FF after loop)", align=Align.INLINE)
d.comment(0x9BA0, "Push &FF as timeout", align=Align.INLINE)
d.comment(0x9BA1, "X=0: TX pointer index", align=Align.INLINE)
d.comment(0x9BA3, "Load control byte from TX CB", align=Align.INLINE)
d.label(0x9BA5, "start_pass_tx")

d.comment(0x9BA5, "Write control byte to start TX", align=Align.INLINE)
d.comment(0x9BA7, "Save control byte on stack", align=Align.INLINE)
d.comment(0x9BA8, "Poll ADLC until line idle", align=Align.INLINE)
d.comment(0x9BAB, "Shift result: check bit 6 (success)", align=Align.INLINE)
d.comment(0x9BAC, "Bit 6 clear: transmission complete", align=Align.INLINE)
d.comment(0x9BAE, "Shift result: check bit 5 (fatal)", align=Align.INLINE)
d.comment(0x9BAF, "Non-zero (not fatal): retry", align=Align.INLINE)
d.label(0x9BB1, "done_pass_retries")

d.comment(0x9BB1, "X=0: clear error status", align=Align.INLINE)
d.comment(0x9BB3, "Jump to fix up reply status", align=Align.INLINE)
d.subroutine(
    0x9BB6,
    "poll_adlc_tx_status",
    title="Wait for TX ready, then start new transmission",
    description="""1. Polls [`tx_complete_flag`](label:tx_complete_flag) via `ASL`
   (testing bit 7) until set, indicating any previous TX
   operation has completed and the ADLC is back in idle
   RX-listen mode.
2. Copies the TX control-block pointer from `net_tx_ptr` to
   `nmi_tx_block`.
3. Calls [`tx_begin`](address:8589), which performs a
   complete transmission from scratch (copies destination from
   TXCB to scout buffer, polls for INACTIVE, configures ADLC
   `CR1=&44 RX_RESET|TIE`, `CR2=&E7 RTS|CLR`, runs the full
   four-way handshake via NMI).
4. After [`tx_begin`](address:8589) returns, polls the TXCB
   first byte until bit 7 clears (NMI handler stores result
   there).

Result in `A`:

| Code | Meaning |
|---|---|
| `&00` | success |
| `&40` | jammed |
| `&41` | not listening |
| `&43` | no clock |
| `&44` | bad control byte |

**This poll has no timeout.** The opening
`ASL tx_complete_flag` / `BCC` pair is an unbounded spin, and
[`tx_complete_flag`](label:tx_complete_flag) is set only by the
NMI completion and error paths
([`tx_store_result`](label:tx_store_result),
[`store_tx_error`](label:store_tx_error)). The retry loop in
[`send_net_packet`](label:send_net_packet) is therefore *not*
an independent watchdog — every one of its attempts blocks here
until an NMI arrives. If the ADLC never raises the interrupt
described at
[`nmi_error_dispatch`](label:nmi_error_dispatch), the ROM waits
forever.

The ROM's software timeouts sit either side of this window,
never inside it: the pre-transmit INACTIVE poll times out to
'Line Jammed', and the post-transmit reply wait in
[`wait_net_tx_ack`](label:wait_net_tx_ack) times out (~22 s by
default) to 'No reply'. The handshake itself relies wholly on
the ADLC, which is sound on a real wire — the line always falls
idle after a frame — but leaves no backstop for an ADLC
implementation that fails to signal Inactive Idle.""",
    on_exit={"a": "TX result (&00 success / &40 jammed / &41 not listening / &43 no clock / &44 bad control byte)"},
)


d.comment(0x9BB6, "Shift ws_0d60 left to poll ADLC", align=Align.INLINE)
d.comment(0x9BB9, "Bit not set: keep polling", align=Align.INLINE)
d.comment(0x9BBB, "Copy TX pointer low to NMI TX block", align=Align.INLINE)
d.comment(0x9BBD, "Store in NMI TX block low", align=Align.INLINE)
d.comment(0x9BBF, "Copy TX pointer high", align=Align.INLINE)
d.comment(0x9BC1, "Store in NMI TX block high", align=Align.INLINE)
d.comment(0x9BC3, "Begin Econet frame transmission", align=Align.INLINE)
d.label(0x9BC6, "loop_poll_pass_tx")

d.comment(0x9BC6, "Read TX status byte", align=Align.INLINE)
d.comment(0x9BC8, "Bit 7 set: still transmitting", align=Align.INLINE)
d.comment(0x9BCA, "Return with result in A", align=Align.INLINE)
d.label(0x9BCB, "restore_retry_state")

d.comment(0x9BCB, "Pull control byte", align=Align.INLINE)
d.comment(0x9BCC, "Restore to X", align=Align.INLINE)
d.comment(0x9BCD, "Pull timeout", align=Align.INLINE)
d.comment(0x9BCE, "Restore to Y", align=Align.INLINE)
d.comment(0x9BCF, "Pull retry count", align=Align.INLINE)
d.comment(0x9BD0, "Zero retries: go to error handling", align=Align.INLINE)
d.comment(0x9BD2, "Decrement retry counter", align=Align.INLINE)
d.comment(0x9BD4, "Push updated retry count", align=Align.INLINE)
d.comment(0x9BD5, "Copy timeout to A", align=Align.INLINE)
d.comment(0x9BD6, "Push timeout", align=Align.INLINE)
d.comment(0x9BD7, "Copy control byte to A", align=Align.INLINE)
d.label(0x9BD8, "loop_pass_tx_delay")

d.comment(0x9BD8, "Inner delay loop: decrement X", align=Align.INLINE)
d.comment(0x9BD9, "Loop until X=0", align=Align.INLINE)
d.comment(0x9BDB, "Decrement outer counter Y", align=Align.INLINE)
d.comment(0x9BDC, "Loop until Y=0", align=Align.INLINE)
d.comment(0x9BDE, "ALWAYS branch: retry transmission", align=Align.INLINE)
d.label(0x9BE0, "pass_tx_success")

d.comment(0x9BE0, "Pull control byte (discard)", align=Align.INLINE)
d.comment(0x9BE1, "Pull timeout (discard)", align=Align.INLINE)
d.comment(0x9BE2, "Pull retry count (discard)", align=Align.INLINE)
d.comment(0x9BE3, "Y=0: start restoring from offset 0", align=Align.INLINE)
d.label(0x9BE5, "loop_restore_txbuf")

d.comment(0x9BE5, "Load template byte for this offset", align=Align.INLINE)
d.comment(0x9BE8, "Is it &FD (skip marker)?", align=Align.INLINE)
d.comment(0x9BEA, "Yes: don't restore this offset", align=Align.INLINE)
d.comment(0x9BEC, "Pull original value from stack", align=Align.INLINE)
d.comment(0x9BED, "Restore original TX buffer byte", align=Align.INLINE)
d.label(0x9BEF, "skip_restore_byte")

d.comment(0x9BEF, "Next offset (ascending)", align=Align.INLINE)
d.comment(0x9BF0, "Processed all 12 bytes?", align=Align.INLINE)
d.comment(0x9BF2, "No: continue restoring", align=Align.INLINE)
d.comment(0x9BF4, "Return with TX buffer restored", align=Align.INLINE)
d.label(0x9BF5, "load_text_ptr_and_parse")

d.subroutine(
    0x9BF5,
    "load_text_ptr_and_parse",
    title="Copy text pointer from FS options and parse string",
    description="""Reads a 2-byte address from (fs_options)+0/1 into
os_text_ptr (&00F2), resets Y to zero, then falls
through to gsread_to_buf to parse the string at that
address into the &0E30 buffer.""",
    on_exit={"y": "0 (reset before GSINIT)"},
)


d.comment(0x9BF5, "Y=1: start at second byte of pointer", align=Align.INLINE)
d.label(0x9BF7, "loop_copy_text_ptr")

d.comment(0x9BF7, "Load pointer byte from FS options", align=Align.INLINE)
d.comment(0x9BF9, "Store in OS text pointer", align=Align.INLINE)
d.comment(0x9BFC, "Decrement index", align=Align.INLINE)
d.comment(0x9BFD, "Loop until both bytes copied", align=Align.INLINE)
d.comment(0x9BFF, "Y=0: reset index for string reading", align=Align.INLINE)
d.label(0x9C00, "gsread_to_buf")

d.subroutine(
    0x9C00,
    "gsread_to_buf",
    title="Parse command line via GSINIT/GSREAD into hazel_parse_buf",
    description="""Calls GSINIT to initialise string reading, then loops calling
GSREAD to copy characters into [`hazel_parse_buf`](label:hazel_parse_buf)
until end-of-string. Appends a CR terminator and sets
`fs_crc_lo`/`hi` to point at the buffer for subsequent parsing
routines.""",
    on_entry={"y": "current command-line offset (consumed by GSINIT)"},
    on_exit={"y": "advanced past the parsed source"},
)


d.comment(0x9C00, "X=&FF: pre-increment for buffer index", align=Align.INLINE)
d.comment(0x9C02, "C=0: initialise for string input", align=Align.INLINE)
d.comment(0x9C03, "GSINIT: initialise string reading", align=Align.INLINE)
d.comment(0x9C06, "Z set (empty string): store terminator", align=Align.INLINE)
d.label(0x9C08, "loop_gsread_char")

d.comment(0x9C08, "GSREAD: read next character", align=Align.INLINE)
d.comment(0x9C0B, "C set: end of string reached", align=Align.INLINE)
d.comment(0x9C0D, "Advance buffer index", align=Align.INLINE)
d.comment(0x9C0E, "Store character in fs_filename_buf buffer", align=Align.INLINE)
d.comment(0x9C11, "ALWAYS branch: read next character", align=Align.INLINE)
d.label(0x9C13, "terminate_buf")

d.comment(0x9C13, "Advance past last character", align=Align.INLINE)
d.comment(0x9C14, "A=CR: terminate filename", align=Align.INLINE)
d.comment(0x9C16, "Store CR terminator in buffer", align=Align.INLINE)
d.comment(0x9C19, "Parse-buffer pointer (low)", align=Align.INLINE)
d.comment(0x9C1B, "Set command text pointer low", align=Align.INLINE)
d.comment(0x9C1D, "Parse-buffer pointer (high)", align=Align.INLINE)
d.comment(0x9C1F, "Set command text pointer high", align=Align.INLINE)
d.comment(0x9C21, "Return with buffer filled", align=Align.INLINE)
d.subroutine(
    0x9C22,
    "filev_handler",
    title="FILEV vector handler: OSFILE",
    description="""Reached via the FILEV vector at `&0212`. Sets up transfer
parameters via [`set_xfer_params`](label:set_xfer_params), loads the OS text
pointer and parses the filename via
[`load_text_ptr_and_parse`](label:load_text_ptr_and_parse),
[`mask_owner_access`](label:mask_owner_access) clears the FS-selection bits,
and [`parse_access_prefix`](label:parse_access_prefix) records any access-byte
prefix. Routes by `fs_last_byte_flag` bit: positive (read /
display) goes to `check_display_type`; negative (write / save)
falls into the create-new-file path.""",
    on_entry={"a": "OSFILE function code", "x, y": "control-block pointer (low, high)"},
)


d.entry(0x9C22)
d.comment(0x9C22, "Set up transfer parameters", align=Align.INLINE)
d.comment(0x9C25, "Load text pointer and parse filename", align=Align.INLINE)
d.comment(0x9C28, "Set owner-only access mask", align=Align.INLINE)
d.comment(0x9C2B, "Parse access prefix from filename", align=Align.INLINE)
d.comment(0x9C2E, "Load last byte flag", align=Align.INLINE)
d.comment(0x9C30, "Positive (not last): display file info", align=Align.INLINE)
d.comment(0x9C32, "Is it &FF (last entry)?", align=Align.INLINE)
d.comment(0x9C34, "Yes: copy arg and iterate", align=Align.INLINE)
d.comment(0x9C36, "Other value: return with flag", align=Align.INLINE)
d.label(0x9C39, "copy_arg_and_enum")

d.comment(0x9C39, "Copy argument to buffer at X=0", align=Align.INLINE)
d.comment(0x9C3C, "Y=2: enumerate directory command", align=Align.INLINE)
d.label(0x9C3E, "do_fs_cmd_iteration")

d.subroutine(
    0x9C3E,
    "do_fs_cmd_iteration",
    title="Execute one iteration of a multi-step FS command",
    description="""Called by match_fs_cmd for commands that enumerate
directory entries. Sets port &92, sends the initial
request via send_request_write, then synchronises the
FS options and workspace state (order depends on the
cycle flag at offset 6). Copies 4 address bytes,
formats the filename field, sends via
send_txcb_swap_addrs, and receives the reply.""",
    on_entry={"y": "FS function code (matches send_request_write contract)"},
    on_exit={"a": "FS reply status"},
)


d.comment(0x9C3E, "A=&92: FS port number", align=Align.INLINE)
d.comment(0x9C40, "Set escapable flag to &92", align=Align.INLINE)
d.comment(0x9C42, "Store port number in TX buffer", align=Align.INLINE)
d.comment(0x9C45, "Send request to file server", align=Align.INLINE)
d.comment(0x9C48, "Y=6: offset to response cycle flag", align=Align.INLINE)
d.comment(0x9C4A, "Load cycle flag from FS options", align=Align.INLINE)
d.comment(0x9C4C, "Non-zero: already initialised", align=Align.INLINE)
d.comment(0x9C4E, "Copy FS options to zero page first", align=Align.INLINE)
d.comment(0x9C51, "Then copy workspace to FS options", align=Align.INLINE)
d.comment(0x9C54, "Branch to continue (C clear from JSR)", align=Align.INLINE)
d.label(0x9C56, "copy_ws_then_fsopts")

d.comment(0x9C56, "Copy workspace to FS options first", align=Align.INLINE)
d.comment(0x9C59, "Then copy FS options to zero page", align=Align.INLINE)
d.label(0x9C5C, "setup_txcb_addrs")

d.comment(0x9C5C, "Y=4: loop counter", align=Align.INLINE)
d.label(0x9C5E, "loop_copy_addrs")

d.comment(0x9C5E, "Load address byte from zero page", align=Align.INLINE)
d.comment(0x9C60, "Save to TXCB end pointer", align=Align.INLINE)
d.comment(0x9C62, "Add offset from buffer", align=Align.INLINE)
d.comment(0x9C65, "Store sum in fs_work area", align=Align.INLINE)
d.comment(0x9C67, "Advance to next byte", align=Align.INLINE)
d.comment(0x9C68, "Decrement counter", align=Align.INLINE)
d.comment(0x9C69, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9C6B, "Set carry for subtraction", align=Align.INLINE)
d.comment(0x9C6C, "Subtract high offset", align=Align.INLINE)
d.comment(0x9C6F, "Store result in fs_work_7", align=Align.INLINE)
d.comment(0x9C71, "Format filename for display", align=Align.INLINE)
d.comment(0x9C74, "Send TXCB and swap addresses", align=Align.INLINE)
d.comment(0x9C77, "X=2: copy 3 offset bytes", align=Align.INLINE)
d.label(0x9C79, "loop_copy_offsets")

d.comment(0x9C79, "Load offset byte from fs_file_len_3", align=Align.INLINE)
d.comment(0x9C7C, "Store in fs_cmd_data for next iteration", align=Align.INLINE)
d.comment(0x9C7F, "Decrement counter", align=Align.INLINE)
d.comment(0x9C80, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x9C82, "Jump to receive and process reply", align=Align.INLINE)
d.label(0x9C85, "send_txcb_swap_addrs")

d.subroutine(
    0x9C85,
    "send_txcb_swap_addrs",
    title="Send TXCB and swap start/end addresses",
    description="""If the 5-byte handle matches, returns
immediately. Otherwise sets port &92, copies
addresses, sends, waits for acknowledgment,
and retries on address mismatch.""",
    on_exit={
        "a": "FS reply status (or unchanged if handles matched -- the routine returns early when no work is needed)"
    },
)


d.comment(0x9C85, "Compare 5-byte handle with current", align=Align.INLINE)
d.comment(0x9C88, "Match: no need to send, return", align=Align.INLINE)
d.comment(0x9C8A, "A=&92: FS reply port number", align=Align.INLINE)
d.comment(0x9C8C, "Set TXCB port", align=Align.INLINE)
d.label(0x9C8E, "loop_swap_and_send")

d.comment(0x9C8E, "X=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9C90, "loop_copy_start_end")

d.comment(0x9C90, "Load TXCB end pointer byte", align=Align.INLINE)
d.comment(0x9C92, "Store in TXCB start pointer", align=Align.INLINE)
d.comment(0x9C94, "Load new end address from fs_work", align=Align.INLINE)
d.comment(0x9C96, "Store in TXCB end pointer", align=Align.INLINE)
d.comment(0x9C98, "Decrement counter", align=Align.INLINE)
d.comment(0x9C99, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9C9B, "A=&7F: control byte for data transfer", align=Align.INLINE)
d.comment(0x9C9D, "Set TXCB control byte", align=Align.INLINE)
d.comment(0x9C9F, "Wait for network TX acknowledgement", align=Align.INLINE)
d.comment(0x9CA2, "Y=3: compare 4 bytes", align=Align.INLINE)
d.label(0x9CA4, "loop_verify_addrs")

d.comment(0x9CA4, "Load TXCB end byte", align=Align.INLINE)
d.comment(0x9CA7, "Compare with expected end address", align=Align.INLINE)
d.comment(0x9CAA, "Mismatch: resend from start", align=Align.INLINE)
d.comment(0x9CAC, "Decrement counter", align=Align.INLINE)
d.comment(0x9CAD, "Loop until all 4 bytes match", align=Align.INLINE)
d.label(0x9CAF, "rts_txcb_swap")

d.comment(0x9CAF, "Return (all bytes match)", align=Align.INLINE)
d.label(0x9CB0, "check_display_type")

d.comment(0x9CB0, "Z set: directory entry display", align=Align.INLINE)
d.comment(0x9CB2, "Non-zero: jump to OSWORD dispatch", align=Align.INLINE)
d.label(0x9CB5, "setup_dir_display")

d.subroutine(
    0x9CB5,
    "setup_dir_display",
    title="Compute display deltas and prep FS info request",
    description="""Iterates 4 times over paired (lo, hi) address words in the FS options
block at offsets &0E and &0A (loop body advances Y by 5 each pass).
For each pair, computes (high - low), saves both originals to
workspace at &00A6+Y (port_ws_offset region), and overwrites the
options entry with the difference so the caller can render 'load
addr', 'exec addr', 'length', etc. without redoing the subtraction.
Then copies 9 bytes of FS-options metadata into the TX buffer at
&C103, sets need_release_tube as the escapable flag, and stores FS
port &91 (info request) at &C102. Final tail-call dispatches the
request via send_request_write.""",
    on_exit={"a": "&91 (FS port for info request)", "x, y": "clobbered"},
)


d.comment(0x9CB5, "X=4: loop counter for 4 iterations", align=Align.INLINE)
d.comment(0x9CB7, "Y=&0E: FS options offset for addresses", align=Align.INLINE)
d.comment(0x9CB9, "Set carry for subtraction", align=Align.INLINE)
d.label(0x9CBA, "loop_compute_diffs")

d.comment(0x9CBA, "Load address byte from FS options", align=Align.INLINE)
d.comment(0x9CBC, "Save to workspace (port_ws_offset)", align=Align.INLINE)
d.comment(0x9CBF, "Y -= 4 to point to paired offset", align=Align.INLINE)
d.comment(0x9CC2, "Subtract paired value", align=Align.INLINE)
d.comment(0x9CC4, "Store difference in fs_cmd_csd buffer", align=Align.INLINE)
d.comment(0x9CC7, "Push difference", align=Align.INLINE)
d.comment(0x9CC8, "Load paired value from FS options", align=Align.INLINE)
d.comment(0x9CCA, "Save to workspace", align=Align.INLINE)
d.comment(0x9CCD, "Pull difference back", align=Align.INLINE)
d.comment(0x9CCE, "Store in FS options for display", align=Align.INLINE)
d.comment(0x9CD0, "Advance Y by 5 for next field", align=Align.INLINE)
d.comment(0x9CD3, "Decrement loop counter", align=Align.INLINE)
d.comment(0x9CD4, "Loop for all 4 address pairs", align=Align.INLINE)
d.comment(0x9CD6, "Y=9: copy 9 bytes of options data", align=Align.INLINE)
d.label(0x9CD8, "loop_copy_fs_options")

d.comment(0x9CD8, "Load FS options byte", align=Align.INLINE)
d.comment(0x9CDA, "Store in fs_cmd_csd buffer", align=Align.INLINE)
d.comment(0x9CDD, "Decrement index", align=Align.INLINE)
d.comment(0x9CDE, "Loop until all 9 bytes copied", align=Align.INLINE)
d.comment(0x9CE0, "A=&91: FS port for info request", align=Align.INLINE)
d.comment(0x9CE2, "Set escapable flag", align=Align.INLINE)
d.comment(0x9CE4, "Store port in TX buffer", align=Align.INLINE)
d.comment(0x9CE7, "Store in fs_error_ptr", align=Align.INLINE)
d.comment(0x9CE9, "X=&0B: copy argument at offset 11", align=Align.INLINE)
d.comment(0x9CEB, "Copy argument to TX buffer", align=Align.INLINE)
d.comment(0x9CEE, "Y=1: info sub-command", align=Align.INLINE)
d.comment(0x9CF0, "Load last byte flag", align=Align.INLINE)
d.comment(0x9CF2, "Is it 7 (catalogue info)?", align=Align.INLINE)
d.comment(0x9CF4, "Save comparison result", align=Align.INLINE)
d.comment(0x9CF5, "Not 7: keep Y=1", align=Align.INLINE)
d.comment(0x9CF7, "Y=&1D: extended info command", align=Align.INLINE)
d.label(0x9CF9, "send_info_request")

d.comment(0x9CF9, "Send request to file server", align=Align.INLINE)
d.comment(0x9CFC, "Format filename for display", align=Align.INLINE)
d.comment(0x9CFF, "Restore comparison flags", align=Align.INLINE)
d.comment(0x9D00, "Not catalogue info: show short format", align=Align.INLINE)
d.comment(0x9D02, "X=0: start at first byte", align=Align.INLINE)
d.comment(0x9D04, "ALWAYS branch to store and display", align=Align.INLINE)
d.label(0x9D06, "setup_txcb_transfer")

d.comment(0x9D06, "Load file handle from fs_cmd_data", align=Align.INLINE)
d.comment(0x9D09, "Check and set up TXCB for transfer", align=Align.INLINE)
d.label(0x9D0C, "recv_reply")

d.subroutine(
    0x9D0C,
    "recv_reply",
    title="Receive FS reply and stash result byte",
    description="""JSRs recv_and_process_reply, then falls through to store_result
(STX hazel_txcb_result; LDY #&0E to point at the protection-bits offset).
Single caller (the dispatch at &9C80).""",
    on_exit={"x": "FS result byte (also written to hazel_txcb_result)", "y": "&0E (FS options offset for protection)"},
)


d.comment(0x9D0C, "Receive and process reply", align=Align.INLINE)
d.label(0x9D0F, "store_result")

d.comment(0x9D0F, "Store result byte in fs_reply_cmd", align=Align.INLINE)
d.comment(0x9D12, "Y=&0E: protection bits offset", align=Align.INLINE)
d.comment(0x9D14, "Load access byte from fs_cmd_data", align=Align.INLINE)
d.comment(0x9D17, "Extract protection bit flags", align=Align.INLINE)
d.comment(0x9D1A, "Zero: use reply buffer data", align=Align.INLINE)
d.label(0x9D1C, "loop_copy_file_info")

d.comment(0x9D1C, "Load file info byte from fs_reply_data", align=Align.INLINE)
d.label(0x9D1F, "store_prot_byte")

d.comment(0x9D1F, "Store in FS options at offset Y", align=Align.INLINE)
d.comment(0x9D21, "Advance to next byte", align=Align.INLINE)
d.comment(0x9D22, "Y=&12: end of protection fields?", align=Align.INLINE)
d.comment(0x9D24, "No: copy next byte", align=Align.INLINE)
d.comment(0x9D26, "Load display flag from fs_messages_flag", align=Align.INLINE)
d.comment(0x9D29, "Zero: skip display, return", align=Align.INLINE)
d.comment(0x9D2B, "Y=&F4: index into hazel_display_buf for filename", align=Align.INLINE)
d.label(0x9D2D, "loop_print_filename")

d.comment(0x9D2D, "Load filename character from filename_buf", align=Align.INLINE)
d.comment(0x9D30, "Print character via OSASCI", align=Align.INLINE)
d.comment(0x9D33, "Advance to next character", align=Align.INLINE)
d.comment(0x9D34, "Printed all 12 characters?", align=Align.INLINE)
d.comment(0x9D36, "Y=5: offset for access string", align=Align.INLINE)
d.comment(0x9D38, "Print 5 hex bytes (access info)", align=Align.INLINE)
d.comment(0x9D3B, "Print load and exec addresses", align=Align.INLINE)
d.comment(0x9D3E, "Print newline", align=Align.INLINE)
d.comment(0x9D41, "Jump to return with last flag", align=Align.INLINE)
d.label(0x9D44, "print_load_exec_addrs")

d.subroutine(
    0x9D44,
    "print_load_exec_addrs",
    title="Print exec address and file length in hex",
    description="""Prints the exec address as 5 hex bytes from
(fs_options) offset 9 downwards, then the file
length as 3 hex bytes from offset &0C. Each group
is followed by a space separator via OSASCI.""",
    on_exit={"a, x, y": "clobbered (print_hex_byte + OSASCI)"},
)


d.comment(0x9D44, "Y=9: offset for exec address", align=Align.INLINE)
d.comment(0x9D46, "Print 5 hex bytes (exec address)", align=Align.INLINE)
d.comment(0x9D49, "Y=&0C: offset for length (3 bytes)", align=Align.INLINE)
d.comment(0x9D4B, "X=3: print 3 bytes only", align=Align.INLINE)
d.comment(0x9D4D, "ALWAYS branch to print routine", align=Align.INLINE)
d.label(0x9D4F, "print_5_hex_bytes")

d.subroutine(
    0x9D4F,
    "print_5_hex_bytes",
    title="Print hex byte sequence from FS options",
    description="""Outputs `X+1` bytes from `(fs_options)` starting at offset `Y`,
decrementing `Y` for each byte (big-endian display order). Each
byte is printed as two hex digits via
[`print_hex_byte`](label:print_hex_byte). Finishes with a trailing
space via OSASCI.

The default entry with `X=4` prints 5 bytes (a full 32-bit
address plus extent).""",
    on_entry={"x": "byte count minus 1 (default 4 for 5 bytes)", "y": "starting offset in (fs_options)"},
)


d.comment(0x9D4F, "X=4: print 5 bytes (4 to 0)", align=Align.INLINE)
d.label(0x9D51, "loop_print_hex_byte")

d.comment(0x9D51, "Load byte from FS options at offset Y", align=Align.INLINE)
d.comment(0x9D53, "Print as 2-digit hex", align=Align.INLINE)
d.comment(0x9D56, "Decrement byte offset", align=Align.INLINE)
d.comment(0x9D57, "Decrement byte count", align=Align.INLINE)
d.comment(0x9D58, "Loop until all bytes printed", align=Align.INLINE)
d.comment(0x9D5A, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9D5C, "Print space via OSASCI and return", align=Align.INLINE)
d.label(0x9D5F, "copy_fsopts_to_zp")

d.subroutine(
    0x9D5F,
    "copy_fsopts_to_zp",
    title="Copy FS options address bytes to zero page",
    description="""Copies 4 bytes from (fs_options) at offsets 2-5
into zero page at &00AE+Y. Used by
do_fs_cmd_iteration to preserve the current address
state. Falls through to skip_one_and_advance5 to
advance Y past the copied region.""",
    on_entry={
        "y": "destination offset within the &00AE.. zero-page region (also indexes the source via (fs_options),Y)"
    },
    on_exit={"y": "advanced by 5 (via skip_one_and_advance5 fall-through)", "a": "clobbered"},
)


d.comment(0x9D5F, "Y=5: copy 4 bytes (offsets 2-5)", align=Align.INLINE)
d.label(0x9D61, "loop_copy_fsopts_byte")

d.comment(0x9D61, "Load byte from FS options", align=Align.INLINE)
d.comment(0x9D63, "Store in zero page at work_ae+Y", align=Align.INLINE)
d.comment(0x9D66, "Decrement index", align=Align.INLINE)
d.comment(0x9D67, "Below offset 2?", align=Align.INLINE)
d.comment(0x9D69, "No: copy next byte", align=Align.INLINE)
d.label(0x9D6B, "skip_one_and_advance5")

d.subroutine(
    0x9D6B,
    "skip_one_and_advance5",
    title="Advance Y by 5",
    description="""Entry point one INY before advance_y_by_4, giving
a total Y increment of 5. Used to skip past a
5-byte address/length structure in the FS options
block.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset + 5", "a, x": "preserved"},
)


d.comment(0x9D6B, "Y += 5", align=Align.INLINE)
d.label(0x9D6C, "advance_y_by_4")

d.subroutine(
    0x9D6C,
    "advance_y_by_4",
    title="Advance Y by 4",
    description="""Four consecutive INY instructions. Used as a
subroutine to step Y past a 4-byte address field
in the FS options or workspace structure.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset + 4"},
)


d.comment(0x9D6C, "Y += 4", align=Align.INLINE)
d.comment(0x9D6D, "(continued)", align=Align.INLINE)
d.comment(0x9D6E, "(continued)", align=Align.INLINE)
d.comment(0x9D6F, "(continued)", align=Align.INLINE)
d.label(0x9D70, "rts_advance_y")

d.comment(0x9D70, "Return", align=Align.INLINE)
d.label(0x9D71, "copy_workspace_to_fsopts")

d.subroutine(
    0x9D71,
    "copy_workspace_to_fsopts",
    title="Copy workspace reply data to FS options",
    description="""Copies bytes from the reply buffer at &0F02+Y
into (fs_options) at offsets &0D down to 2. Used
to update the FS options block with data returned
from the file server. Falls through to
retreat_y_by_4.""",
    on_entry={"y": "current offset (controls how many bytes are copied before the loop terminates)"},
    on_exit={"y": "decremented by 4 (via retreat_y_by_4 fall-through)", "a": "clobbered"},
)


d.comment(0x9D71, "Y=&0D: copy bytes from offset &0D down", align=Align.INLINE)
d.comment(0x9D73, "Transfer X to A", align=Align.INLINE)
d.label(0x9D74, "loop_copy_ws_byte")

d.comment(0x9D74, "Store byte in FS options at offset Y", align=Align.INLINE)
d.comment(0x9D76, "Load next workspace byte from fs_cmd_urd+Y", align=Align.INLINE)
d.comment(0x9D79, "Decrement index", align=Align.INLINE)
d.comment(0x9D7A, "Below offset 2?", align=Align.INLINE)
d.comment(0x9D7C, "No: copy next byte", align=Align.INLINE)
d.label(0x9D7E, "retreat_y_by_4")

d.subroutine(
    0x9D7E,
    "retreat_y_by_4",
    title="Retreat Y by 4",
    description="""Four consecutive DEY instructions. Companion to
advance_y_by_4 for reverse traversal of address
structures.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 4"},
)


d.comment(0x9D7E, "Y -= 4", align=Align.INLINE)
d.label(0x9D7F, "retreat_y_by_3")

d.subroutine(
    0x9D7F,
    "retreat_y_by_3",
    title="Retreat Y by 3",
    description="""Three consecutive DEY instructions. Used by
setup_transfer_workspace to step back through
interleaved address pairs in the FS options block.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 3"},
)


d.comment(0x9D7F, "Y -= 3", align=Align.INLINE)
d.comment(0x9D80, "(continued)", align=Align.INLINE)
d.comment(0x9D81, "(continued)", align=Align.INLINE)
d.comment(0x9D82, "Return", align=Align.INLINE)
d.label(0x9D83, "discard_handle_match")

d.comment(0x9D83, "Discard stacked value", align=Align.INLINE)
d.comment(0x9D84, "Restore Y from fs_block_offset", align=Align.INLINE)
d.comment(0x9D86, "Return (handle already matches)", align=Align.INLINE)
d.label(0x9D87, "check_and_setup_txcb")

d.subroutine(
    0x9D87,
    "check_and_setup_txcb",
    title="Set up data-transfer TXCB and dispatch reply",
    description="""Compares the 5-byte handle via
[`cmp_5byte_handle`](label:cmp_5byte_handle); if unchanged, returns.
Otherwise:

1. Computes start / end addresses with overflow clamping.
2. Sets the port and control byte.
3. Sends the packet.
4. Dispatches on the reply sub-operation code.""",
    on_exit={"a": "FS reply sub-operation code (drives downstream dispatch)"},
)


d.comment(0x9D87, "Save port/sub-function on stack", align=Align.INLINE)
d.comment(0x9D88, "Compare 5-byte handle with current", align=Align.INLINE)
d.comment(0x9D8B, "Match: discard port and return", align=Align.INLINE)
d.label(0x9D8D, "init_transfer_addrs")

d.comment(0x9D8D, "X=0: loop start", align=Align.INLINE)
d.comment(0x9D8F, "Y=4: copy 4 bytes", align=Align.INLINE)
d.comment(0x9D91, "Clear fs_reply_cmd (transfer size low)", align=Align.INLINE)
d.comment(0x9D94, "Clear fs_load_vector (transfer size high)", align=Align.INLINE)
d.comment(0x9D97, "Clear carry for addition", align=Align.INLINE)
d.label(0x9D98, "loop_copy_addr_offset")

d.comment(0x9D98, "Load address byte from zero page", align=Align.INLINE)
d.comment(0x9D9A, "Store in TXCB start pointer", align=Align.INLINE)
d.comment(0x9D9C, "Add offset from fs_func_code", align=Align.INLINE)
d.comment(0x9D9F, "Store sum in TXCB end pointer", align=Align.INLINE)
d.comment(0x9DA1, "Also update load address", align=Align.INLINE)
d.comment(0x9DA3, "Advance to next byte", align=Align.INLINE)
d.comment(0x9DA4, "Decrement counter", align=Align.INLINE)
d.comment(0x9DA5, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9DA7, "Carry set: overflow, use limit", align=Align.INLINE)
d.comment(0x9DA9, "Set carry for subtraction", align=Align.INLINE)
d.label(0x9DAA, "loop_check_vs_limit")

d.comment(0x9DAA, "Load computed end address", align=Align.INLINE)
d.comment(0x9DAD, "Subtract maximum from fs_work_4", align=Align.INLINE)
d.comment(0x9DB0, "Advance to next byte", align=Align.INLINE)
d.comment(0x9DB1, "Decrement counter", align=Align.INLINE)
d.comment(0x9DB2, "Loop for all bytes", align=Align.INLINE)
d.comment(0x9DB4, "Below limit: keep computed end", align=Align.INLINE)
d.label(0x9DB6, "clamp_end_to_limit")

d.comment(0x9DB6, "X=3: copy 4 bytes of limit", align=Align.INLINE)
d.label(0x9DB8, "loop_copy_limit")

d.comment(0x9DB8, "Load limit from fs_work_4", align=Align.INLINE)
d.comment(0x9DBA, "Store as TXCB end", align=Align.INLINE)
d.comment(0x9DBC, "Decrement counter", align=Align.INLINE)
d.comment(0x9DBD, "Loop for all 4 bytes", align=Align.INLINE)
d.label(0x9DBF, "set_port_and_ctrl")

d.comment(0x9DBF, "Pull port from stack", align=Align.INLINE)
d.comment(0x9DC0, "Push back (keep for later)", align=Align.INLINE)
d.comment(0x9DC1, "Save flags (carry = overflow state)", align=Align.INLINE)
d.comment(0x9DC2, "Set TXCB port number", align=Align.INLINE)
d.comment(0x9DC4, "A=&80: control byte for data request", align=Align.INLINE)
d.comment(0x9DC6, "Set TXCB control byte", align=Align.INLINE)
d.comment(0x9DC8, "Init TX pointer and send packet", align=Align.INLINE)
d.comment(0x9DCB, "Load error pointer", align=Align.INLINE)
d.comment(0x9DCD, "Init TXCB port from error pointer", align=Align.INLINE)
d.comment(0x9DD0, "Restore overflow flags", align=Align.INLINE)
d.comment(0x9DD1, "Carry set: discard and return", align=Align.INLINE)
d.comment(0x9DD3, "A=&91: FS reply port", align=Align.INLINE)
d.comment(0x9DD5, "Set TXCB port for reply", align=Align.INLINE)
d.comment(0x9DD7, "Wait for TX acknowledgement", align=Align.INLINE)
d.comment(0x9DDA, "Non-zero (not done): retry send", align=Align.INLINE)
d.label(0x9DDC, "dispatch_osword_op")

d.subroutine(
    0x9DDC,
    "dispatch_osword_op",
    title="OSWORD &13 sub-operation triage (1-7)",
    description="""Stores the sub-operation code in
[`hazel_txcb_data`](label:hazel_txcb_data) and triages by value:

| Value | Target |
|---|---|
| `0..6` | `dispatch_ops_1_to_6` |
| `7`    | [`setup_dir_display`](label:setup_dir_display) (`*INFO` expansion) |
| `> 7`  | `skip_if_error` (routes through [`finalise_and_return`](label:finalise_and_return)) |

Single caller (`&9CB0` in the OSWORD `&13` handler entry).""",
    on_entry={"a": "OSWORD sub-op code"},
)


d.comment(0x9DDC, "Store sub-operation code", align=Align.INLINE)
d.comment(0x9DDF, "Compare with 7", align=Align.INLINE)
d.comment(0x9DE1, "Below 7: handle operations 1-6", align=Align.INLINE)
d.comment(0x9DE3, "Above 7: jump to handle via finalise", align=Align.INLINE)
d.comment(0x9DE5, "Equal to 7: jump to directory display", align=Align.INLINE)
d.label(0x9DE8, "dispatch_ops_1_to_6")

d.comment(0x9DE8, "Compare with 6", align=Align.INLINE)
d.comment(0x9DEA, "6: delete file operation", align=Align.INLINE)
d.comment(0x9DEC, "Compare with 5", align=Align.INLINE)
d.comment(0x9DEE, "5: read catalogue info", align=Align.INLINE)
d.comment(0x9DF0, "Compare with 4", align=Align.INLINE)
d.comment(0x9DF2, "4: write file attributes", align=Align.INLINE)
d.comment(0x9DF4, "Compare with 1", align=Align.INLINE)
d.comment(0x9DF6, "1: read file info", align=Align.INLINE)
d.comment(0x9DF8, "Shift left twice: A*4", align=Align.INLINE)
d.comment(0x9DF9, "A*4", align=Align.INLINE)
d.comment(0x9DFA, "Copy to Y as index", align=Align.INLINE)
d.comment(0x9DFB, "Y -= 3 to get FS options offset", align=Align.INLINE)
d.comment(0x9DFE, "X=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9E00, "loop_copy_fsopts_4")

d.comment(0x9E00, "Load byte from FS options at offset Y", align=Align.INLINE)
d.comment(0x9E02, "Store in fs_func_code buffer", align=Align.INLINE)
d.comment(0x9E05, "Decrement source offset", align=Align.INLINE)
d.comment(0x9E06, "Decrement byte count", align=Align.INLINE)
d.comment(0x9E07, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9E09, "X=5: copy arg to buffer at offset 5", align=Align.INLINE)
d.comment(0x9E0B, "ALWAYS branch to copy and send", align=Align.INLINE)
d.label(0x9E0D, "setup_save_access")

d.comment(0x9E0D, "Get access bits for file", align=Align.INLINE)
d.comment(0x9E10, "Store access byte in fs_file_attrs", align=Align.INLINE)
d.comment(0x9E13, "Y=9: source offset in FS options", align=Align.INLINE)
d.comment(0x9E15, "X=8: copy 8 bytes to buffer", align=Align.INLINE)
d.label(0x9E17, "loop_copy_fsopts_8")

d.comment(0x9E17, "Load FS options byte", align=Align.INLINE)
d.comment(0x9E19, "Store in fs_cmd_data buffer", align=Align.INLINE)
d.comment(0x9E1C, "Decrement source offset", align=Align.INLINE)
d.comment(0x9E1D, "Decrement byte count", align=Align.INLINE)
d.comment(0x9E1E, "Loop for all 8 bytes", align=Align.INLINE)
d.comment(0x9E20, "X=&0A: buffer offset for argument", align=Align.INLINE)
d.label(0x9E22, "send_save_or_access")

d.comment(0x9E22, "Copy argument to buffer", align=Align.INLINE)
d.comment(0x9E25, "Y=&13: OSWORD &13 (NFS operation)", align=Align.INLINE)
d.comment(0x9E27, "ALWAYS branch to send request", align=Align.INLINE)
d.label(0x9E29, "send_delete_request")

d.comment(0x9E29, "Copy argument to buffer at X=0", align=Align.INLINE)
d.comment(0x9E2C, "Y=&14: delete file command", align=Align.INLINE)
d.label(0x9E2E, "send_request_vset")

d.comment(0x9E2E, "Set V flag (no directory check)", align=Align.INLINE)
d.comment(0x9E31, "Send request with V set", align=Align.INLINE)
d.label(0x9E34, "skip_if_error")

d.comment(0x9E34, "Carry set: error, jump to finalise", align=Align.INLINE)
d.comment(0x9E36, "No error: return with last flag", align=Align.INLINE)
d.label(0x9E39, "setup_write_access")

d.comment(0x9E39, "Get access bits for file", align=Align.INLINE)
d.comment(0x9E3C, "Store in fs_func_code", align=Align.INLINE)
d.comment(0x9E3F, "X=2: buffer offset", align=Align.INLINE)
d.comment(0x9E41, "ALWAYS branch to copy and send", align=Align.INLINE)
d.label(0x9E43, "read_cat_info")

d.comment(0x9E43, "X=1: buffer offset", align=Align.INLINE)
d.comment(0x9E45, "Copy argument to buffer", align=Align.INLINE)
d.comment(0x9E48, "Y=&12: open file command", align=Align.INLINE)
d.comment(0x9E4A, "Send open file request", align=Align.INLINE)
d.comment(0x9E4D, "Load reply handle from fs_obj_type", align=Align.INLINE)
d.comment(0x9E50, "Clear fs_obj_type", align=Align.INLINE)
d.comment(0x9E53, "Clear fs_len_clear", align=Align.INLINE)
d.comment(0x9E56, "Get protection bits", align=Align.INLINE)
d.comment(0x9E59, "Load file handle from fs_cmd_data", align=Align.INLINE)
d.comment(0x9E5C, "Zero: file not found, return", align=Align.INLINE)
d.comment(0x9E5E, "Y=&0E: store access bits", align=Align.INLINE)
d.comment(0x9E60, "Store access byte in FS options", align=Align.INLINE)
d.comment(0x9E62, "Y=&0D", align=Align.INLINE)
d.comment(0x9E63, "X=&0C: copy 12 bytes of file info", align=Align.INLINE)
d.label(0x9E65, "loop_copy_cat_info")

d.comment(0x9E65, "Load reply byte from fs_cmd_data+X", align=Align.INLINE)
d.comment(0x9E68, "Store in FS options at offset Y", align=Align.INLINE)
d.comment(0x9E6A, "Decrement destination offset", align=Align.INLINE)
d.comment(0x9E6B, "Decrement source counter", align=Align.INLINE)
d.comment(0x9E6C, "Loop for all 12 bytes", align=Align.INLINE)
d.comment(0x9E6E, "X=1 (INX from 0)", align=Align.INLINE)
d.comment(0x9E6F, "X=2", align=Align.INLINE)
d.comment(0x9E70, "Y=&11: FS options offset", align=Align.INLINE)
d.label(0x9E72, "loop_copy_ext_info")

d.comment(0x9E72, "Load extended info byte from fs_access_level", align=Align.INLINE)
d.comment(0x9E75, "Store in FS options", align=Align.INLINE)
d.comment(0x9E77, "Decrement destination offset", align=Align.INLINE)
d.comment(0x9E78, "Decrement source counter", align=Align.INLINE)
d.comment(0x9E79, "Loop until all copied", align=Align.INLINE)
d.comment(0x9E7B, "Reload file handle", align=Align.INLINE)
d.label(0x9E7E, "return_with_handle")

d.comment(0x9E7E, "Transfer to A", align=Align.INLINE)
d.label(0x9E7F, "done_osword_op")

d.entry(0x9E7F)
d.comment(0x9E7F, "Jump to finalise and return", align=Align.INLINE)
d.label(0x9E82, "format_filename_field")

d.subroutine(
    0x9E82,
    "format_filename_field",
    title="Format filename into fixed-width display field",
    description="""Builds a 12-character space-padded filename at
[`filename_buf`](label:filename_buf) for directory listing
output. Sources the name from either the command line
or the [`fs_cmd_data`](label:fs_cmd_data) reply buffer
depending on the value in [`fs_cmd_csd`](label:fs_cmd_csd).
Truncates or pads to exactly 12 characters.""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0x9E82, "Y=0: start writing at filename_buf[0]", align=Align.INLINE)
d.comment(0x9E84, "Load source offset from fs_cmd_csd", align=Align.INLINE)
d.comment(0x9E87, "Non-zero: copy from fs_cmd_data buffer", align=Align.INLINE)
d.label(0x9E89, "loop_copy_cmdline_char")

d.comment(0x9E89, "Load character from command line", align=Align.INLINE)
d.comment(0x9E8B, "Below '!' (control/space)?", align=Align.INLINE)
d.comment(0x9E8D, "Yes: pad with spaces", align=Align.INLINE)
d.comment(0x9E8F, "Store printable character in filename_buf", align=Align.INLINE)
d.comment(0x9E92, "Advance to next character", align=Align.INLINE)
d.comment(0x9E93, "Loop for more characters", align=Align.INLINE)
d.label(0x9E95, "pad_with_spaces")

d.comment(0x9E95, "A=' ': space for padding", align=Align.INLINE)
d.comment(0x9E97, "Store space in display buffer", align=Align.INLINE)
d.comment(0x9E9A, "Advance index", align=Align.INLINE)
d.comment(0x9E9B, "Filled all 12 characters?", align=Align.INLINE)
d.comment(0x9E9D, "No: pad more spaces", align=Align.INLINE)
d.comment(0x9E9F, "Return with field formatted", align=Align.INLINE)
d.label(0x9EA0, "loop_copy_buf_char")

d.comment(0x9EA0, "Advance source and destination", align=Align.INLINE)
d.label(0x9EA2, "copy_from_buf_entry")

d.comment(0x9EA2, "Load byte from fs_cmd_data buffer", align=Align.INLINE)
d.comment(0x9EA5, "Store in filename_buf", align=Align.INLINE)
d.comment(0x9EA8, "Bit 7 clear: more characters", align=Align.INLINE)
d.comment(0x9EAA, "Return (bit 7 set = terminator)", align=Align.INLINE)
d.subroutine(
    0x9EAB,
    "argsv_handler",
    title="ARGSV vector handler: OSARGS",
    description="""Reached via the ARGSV vector at `&0214`. Verifies the FS workspace
checksum, stores the result as the last-byte flag, and sets the FS
options pointer. Routes by `A`: positive (`bit 7 clear`) dispatches
to a sub-operation table; bit 6 vs bit 5 of `A` then selects
between read-and-write paths via further branching.""",
    on_entry={"a": "OSARGS function code", "x": "control-block low byte", "y": "channel handle"},
)


d.entry(0x9EAB)
d.comment(0x9EAB, "Verify workspace checksum", align=Align.INLINE)
d.comment(0x9EAE, "Store result as last byte flag", align=Align.INLINE)
d.comment(0x9EB0, "Set FS options pointer", align=Align.INLINE)
d.comment(0x9EB3, "OR with 0 to set flags", align=Align.INLINE)
d.comment(0x9EB5, "Positive: handle sub-operations", align=Align.INLINE)
d.comment(0x9EB7, "Shift left to check bit 6", align=Align.INLINE)
d.comment(0x9EB8, "Zero (was &80): close channel", align=Align.INLINE)
d.comment(0x9EBA, "Other: process all FCBs first", align=Align.INLINE)
d.label(0x9EBD, "validate_chan_close")

d.comment(0x9EBD, "Transfer Y to A", align=Align.INLINE)
d.comment(0x9EBE, "Compare with &20 (space)", align=Align.INLINE)
d.comment(0x9EC0, "Above &20: check further", align=Align.INLINE)
d.label(0x9EC2, "error_invalid_chan")

d.comment(0x9EC2, "Below &20: invalid channel char", align=Align.INLINE)
d.label(0x9EC5, "check_chan_range")

d.comment(0x9EC5, "Compare with '0'", align=Align.INLINE)
d.comment(0x9EC7, "Above '0': invalid channel char", align=Align.INLINE)
d.comment(0x9EC9, "Process all matching FCBs", align=Align.INLINE)
d.comment(0x9ECC, "Transfer Y to A (FCB index)", align=Align.INLINE)
d.comment(0x9ECD, "Push FCB index", align=Align.INLINE)
d.comment(0x9ECE, "Copy to X", align=Align.INLINE)
d.comment(0x9ECF, "Y=0: clear counter", align=Align.INLINE)
d.comment(0x9ED1, "Clear last byte flag", align=Align.INLINE)
d.comment(0x9ED3, "Clear block offset", align=Align.INLINE)
d.label(0x9ED5, "loop_copy_fcb_fields")

d.comment(0x9ED5, "Load channel data from fcb_attr_or_count_mid+X", align=Align.INLINE)
d.comment(0x9ED8, "Store in FS options at Y", align=Align.INLINE)
d.comment(0x9EDA, "Advance X by 8 (next FCB field)", align=Align.INLINE)
d.comment(0x9EDD, "Advance destination index", align=Align.INLINE)
d.comment(0x9EDE, "Copied all 4 channel fields?", align=Align.INLINE)
d.comment(0x9EE0, "No: copy next field", align=Align.INLINE)
d.comment(0x9EE2, "Pull saved FCB index", align=Align.INLINE)
d.comment(0x9EE3, "Restore to fs_block_offset", align=Align.INLINE)
d.label(0x9EE5, "dispatch_osfind_op")

d.comment(0x9EE5, "Compare with 5", align=Align.INLINE)
d.comment(0x9EE7, "5 or above: return with last flag", align=Align.INLINE)
d.comment(0x9EE9, "Compare Y with 0", align=Align.INLINE)
d.comment(0x9EEB, "Non-zero: handle OSFIND with channel", align=Align.INLINE)
d.comment(0x9EED, "Y=0 (close): jump to OSFIND open", align=Align.INLINE)
d.label(0x9EF0, "osfind_with_channel")

d.comment(0x9EF0, "Push sub-function", align=Align.INLINE)
# UNMAPPED: d.comment(0x9EF1, "Transfer X to A", align=Align.INLINE)
# UNMAPPED: d.comment(0x9EF2, "Push X (FCB slot)", align=Align.INLINE)
d.comment(0x9EF2, "Transfer Y to A", align=Align.INLINE)
d.comment(0x9EF3, "Push Y (channel char)", align=Align.INLINE)
d.comment(0x9EF4, "Check file is not a directory", align=Align.INLINE)
d.comment(0x9EF7, "Pull channel char", align=Align.INLINE)
d.comment(0x9EF8, "Store channel char as receive attribute", align=Align.INLINE)
d.comment(0x9EFB, "Load FCB flag byte from fcb_net_or_port", align=Align.INLINE)
d.comment(0x9EFE, "Store in fs_cmd_data", align=Align.INLINE)
# UNMAPPED: d.comment(0x9F02, "Pull X (FCB slot)", align=Align.INLINE)
# UNMAPPED: d.comment(0x9F03, "Restore X", align=Align.INLINE)
d.comment(0x9F02, "Pull sub-function", align=Align.INLINE)
d.comment(0x9F03, "Shift right: check bit 0", align=Align.INLINE)
d.comment(0x9F04, "Zero (OSFIND close): handle close", align=Align.INLINE)
d.comment(0x9F06, "Save flags (carry from LSR)", align=Align.INLINE)
d.comment(0x9F07, "Push sub-function", align=Align.INLINE)
d.comment(0x9F08, "Load FS options pointer low", align=Align.INLINE)
d.comment(0x9F0A, "Load block offset", align=Align.INLINE)
d.comment(0x9F0C, "Process all matching FCBs", align=Align.INLINE)
d.comment(0x9F0F, "Load updated data from fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0x9F12, "Store in fs_cmd_data", align=Align.INLINE)
d.comment(0x9F15, "Pull sub-function", align=Align.INLINE)
d.comment(0x9F16, "Store in fs_func_code", align=Align.INLINE)
d.comment(0x9F19, "Restore flags", align=Align.INLINE)
d.comment(0x9F1A, "Transfer Y to A", align=Align.INLINE)
d.comment(0x9F1B, "Push Y (offset)", align=Align.INLINE)
d.comment(0x9F1C, "Carry clear: read operation", align=Align.INLINE)
d.comment(0x9F1E, "Y=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9F20, "loop_copy_zp_to_buf")

d.comment(0x9F20, "Load zero page data", align=Align.INLINE)
d.comment(0x9F22, "Store in fs_data_count buffer", align=Align.INLINE)
d.comment(0x9F25, "Decrement source", align=Align.INLINE)
d.comment(0x9F26, "Decrement counter", align=Align.INLINE)
d.comment(0x9F27, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9F29, "Y=&0D: TX buffer size", align=Align.INLINE)
d.comment(0x9F2B, "X=5: argument offset", align=Align.INLINE)
d.comment(0x9F2D, "Send TX control block to server", align=Align.INLINE)
d.comment(0x9F30, "Store X in last byte flag", align=Align.INLINE)
d.comment(0x9F32, "Pull saved offset", align=Align.INLINE)
d.comment(0x9F33, "Set connection active flag", align=Align.INLINE)
d.label(0x9F36, "done_return_flag")

d.comment(0x9F36, "Return with last flag", align=Align.INLINE)
d.label(0x9F39, "osargs_read_op")

d.comment(0x9F39, "Y=&0C: TX buffer size (smaller)", align=Align.INLINE)
d.comment(0x9F3B, "X=2: argument offset", align=Align.INLINE)
d.comment(0x9F3D, "Send TX control block", align=Align.INLINE)
d.comment(0x9F40, "Store A in last byte flag", align=Align.INLINE)
d.comment(0x9F42, "Load FS options pointer low", align=Align.INLINE)
d.comment(0x9F44, "Y=2: zero page offset", align=Align.INLINE)
d.comment(0x9F46, "Store A in zero page", align=Align.INLINE)
d.label(0x9F48, "loop_copy_reply_to_zp")

d.comment(0x9F48, "Load buffer byte from fs_cmd_data+Y", align=Align.INLINE)
d.comment(0x9F4B, "Store in zero page at offset", align=Align.INLINE)
d.comment(0x9F4D, "Decrement source X", align=Align.INLINE)
d.comment(0x9F4E, "Decrement counter Y", align=Align.INLINE)
d.comment(0x9F4F, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x9F51, "Pull saved offset", align=Align.INLINE)
d.comment(0x9F52, "Return with last flag", align=Align.INLINE)
d.label(0x9F55, "osargs_ptr_dispatch")

d.comment(0x9F55, "Carry set: write file pointer", align=Align.INLINE)
d.comment(0x9F57, "Load block offset", align=Align.INLINE)
d.comment(0x9F59, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0x9F5C, "Load FS options pointer", align=Align.INLINE)
d.comment(0x9F5E, "Load FCB low byte from fcb_count_lo", align=Align.INLINE)
d.comment(0x9F61, "Store in zero page pointer low", align=Align.INLINE)
d.comment(0x9F64, "Load FCB high byte from fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0x9F67, "Store in zero page pointer high", align=Align.INLINE)
d.comment(0x9F6A, "Load FCB extent from fcb_station_or_count_hi", align=Align.INLINE)
d.comment(0x9F6D, "Store in zero page work area", align=Align.INLINE)
d.comment(0x9F70, "A=0: clear high byte", align=Align.INLINE)
d.comment(0x9F72, "Store zero in work area high", align=Align.INLINE)
d.comment(0x9F75, "ALWAYS branch to return with flag", align=Align.INLINE)
d.label(0x9F77, "osargs_write_ptr")

d.comment(0x9F77, "Store write value in fs_func_code", align=Align.INLINE)
d.comment(0x9F7A, "Transfer X to A", align=Align.INLINE)
d.comment(0x9F7B, "Push X (zero page offset)", align=Align.INLINE)
d.comment(0x9F7C, "Y=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9F7E, "loop_copy_ptr_to_buf")

d.comment(0x9F7E, "Load zero page data at offset", align=Align.INLINE)
d.comment(0x9F80, "Store in fs_data_count buffer", align=Align.INLINE)
d.comment(0x9F83, "Decrement source", align=Align.INLINE)
d.comment(0x9F84, "Decrement counter", align=Align.INLINE)
d.comment(0x9F85, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9FB1, "Y=&0D: TX buffer size", align=Align.INLINE)
d.comment(0x9FB3, "X=5: argument offset", align=Align.INLINE)
d.comment(0x9FB5, "Send TX control block", align=Align.INLINE)
d.comment(0x9FB8, "Store X in last byte flag", align=Align.INLINE)
d.comment(0x9FBA, "Pull saved zero page offset", align=Align.INLINE)
d.comment(0x9FBB, "Transfer to Y", align=Align.INLINE)
d.comment(0x9FBC, "Load block offset (attribute)", align=Align.INLINE)
d.comment(0x9FBE, "Clear connection active flag", align=Align.INLINE)
d.comment(0x9FC1, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0x9FC4, "Load zero page pointer low", align=Align.INLINE)
d.comment(0x9FC7, "Store back to FCB fcb_count_lo", align=Align.INLINE)
d.comment(0x9FCA, "Load zero page pointer high", align=Align.INLINE)
d.comment(0x9FCD, "Store back to FCB fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0x9FD0, "Load zero page work byte", align=Align.INLINE)
d.comment(0x9FD3, "Store back to FCB fcb_station_or_count_hi", align=Align.INLINE)
d.comment(0x9FD6, "Return with last flag", align=Align.INLINE)
d.label(0x9FD9, "close_all_fcbs")

d.subroutine(
    0x9FD9,
    "close_all_fcbs",
    title="Close all FCBs (process_all_fcbs + finalise)",
    description="""Single-instruction wrapper: JSR process_all_fcbs to walk every FCB
slot and close each open file in turn, then fall through to
return_with_last_flag (which loads fs_last_byte_flag and finalises
caller state). Single caller (the OSFIND close-all path at &9EB8).""",
    on_exit={"a": "fs_last_byte_flag (loaded by return_with_last_flag)"},
)


d.comment(0x9FD9, "Process all matching FCBs first", align=Align.INLINE)
d.label(0x9FDC, "return_with_last_flag")

d.subroutine(
    0x9FDC,
    "return_with_last_flag",
    title="Load last-byte flag and finalise",
    description="""Loads fs_last_byte_flag (&BD) into A and falls through to
finalise_and_return, which clears the receive-attribute byte and
restores caller's X/Y. The 12 inbound refs are mostly fall-through
exits from FS reply handlers that need to return the last-byte
status to their caller; only one site (&9FD6) reaches it via JSR.""",
    on_exit={
        "a": "fs_last_byte_flag",
        "x": "fs_options (restored by finalise_and_return)",
        "y": "fs_block_offset (restored by finalise_and_return)",
    },
)


d.comment(0x9FDC, "Load last byte flag", align=Align.INLINE)
d.label(0x9FDE, "finalise_and_return")

d.subroutine(
    0x9FDE,
    "finalise_and_return",
    title="Clear receive-attribute and restore caller's X/Y",
    description="""Common 7-byte exit sequence used at the end of format_filename_field, several FS reply handlers, and match_fs_cmd. Saves A across a call to store_rx_attribute(0) (which clears the receive-attribute byte), then restores X from fs_options and Y from fs_block_offset before returning. Effectively: 'finish processing, clear network state, restore caller's pointers'.

One JSR caller (match_fs_cmd at &A599) plus 6 branch entries from format_filename_field's various exit paths.""",
    on_entry={"a": "result code to return"},
    on_exit={"a": "preserved", "x": "fs_options low byte", "y": "fs_block_offset low byte"},
)


d.comment(0x9FDE, "Push result on stack", align=Align.INLINE)
d.comment(0x9FDF, "A=0: clear error flag", align=Align.INLINE)
d.comment(0x9FE1, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0x9FE4, "Pull result back", align=Align.INLINE)
d.comment(0x9FE5, "Restore X from FS options pointer", align=Align.INLINE)
d.comment(0x9FE7, "Restore Y from block offset", align=Align.INLINE)
d.comment(0x9FE9, "Return to caller", align=Align.INLINE)
d.label(0x9FEA, "osfind_close_or_open")

d.subroutine(
    0x9FEA,
    "osfind_close_or_open",
    title="OSFIND dispatch: close-all, close-one, or open",
    description="""Triages the OSFIND function code in `A`:

| `A` | Meaning | Path |
|---|---|---|
| `≥ 2` | open for input / output / update | branch to `done_file_open` |
| `1`   | close one channel | go to `done_file_open` |
| `0`   | close all channels | load `A=5` (close-all return code) and fall through |

Single caller (the OSFIND vector table at `&9EEB`).""",
    on_entry={"a": "OSFIND function code (0=close-all, 1=close-one, >=2 = open variants)"},
)


d.entry(0x9FEA)
d.comment(0x9FEA, "Compare with 2 (open for output)", align=Align.INLINE)
d.comment(0x9FEC, "2 or above: handle file open", align=Align.INLINE)
d.comment(0x9FEE, "Transfer to Y (Y=0 or 1)", align=Align.INLINE)
d.comment(0x9FEF, "Non-zero (1 = read pointer): copy data", align=Align.INLINE)
d.comment(0x9FF1, "A=5: return code for close-all", align=Align.INLINE)
d.comment(0x9FF3, "ALWAYS branch to finalise", align=Align.INLINE)
d.label(0x9FF5, "done_file_open")

d.comment(0x9FF5, "Z set: jump to clear A and return", align=Align.INLINE)
d.label(0x9FF7, "clear_result")

d.subroutine(
    0x9FF7,
    "clear_result",
    title="Set A=0 and finalise",
    description="""Loads A=0 and falls through to shift_and_finalise (LSR A / BPL
finalise_and_return). The LSR-then-BPL is the standard FS-handler
'success exit with carry clear' idiom. Two callers: the post-
return path at &9FFC and the catalogue tail at tail_update_
catalogue (&A33F).""",
    on_exit={"a": "0", "c": "0 (LSR of 0)"},
)


d.comment(0x9FF7, "A=0: clear result", align=Align.INLINE)
d.label(0x9FF9, "shift_and_finalise")

d.comment(0x9FF9, "Shift right (always positive)", align=Align.INLINE)
d.comment(0x9FFA, "Positive: jump to finalise", align=Align.INLINE)
d.label(0x9FFC, "alloc_fcb_for_open")

d.comment(0x9FFC, "Mask to 6-bit access value", align=Align.INLINE)
d.comment(0x9FFE, "Non-zero: clear A and finalise", align=Align.INLINE)
d.comment(0xA000, "Transfer X to A (options pointer)", align=Align.INLINE)
d.comment(0xA001, "Allocate FCB slot or raise error", align=Align.INLINE)
d.comment(0xA004, "Toggle bit 7", align=Align.INLINE)
d.comment(0xA006, "Shift left: build open mode", align=Align.INLINE)
d.comment(0xA007, "Store open mode in fs_cmd_data", align=Align.INLINE)
d.comment(0xA00A, "Rotate to complete mode byte", align=Align.INLINE)
d.comment(0xA00B, "Store in fs_func_code", align=Align.INLINE)
d.comment(0xA00E, "Parse command argument (Y=0)", align=Align.INLINE)
d.comment(0xA011, "X=2: buffer offset", align=Align.INLINE)
d.comment(0xA013, "Copy argument to TX buffer", align=Align.INLINE)
d.subroutine(
    0xA016, "send_open_file_request", description="Send file open request with V flag set for directory check."
)

d.comment(0xA016, "Y=6: open file command", align=Align.INLINE)
d.comment(0xA018, "Set V flag (skip directory check)", align=Align.INLINE)
d.comment(0xA01B, "Set carry", align=Align.INLINE)
d.comment(0xA01C, "Rotate carry into escapable flag bit 7", align=Align.INLINE)
d.comment(0xA01E, "Send open request with V set", align=Align.INLINE)
d.comment(0xA021, "Carry set (error): jump to finalise", align=Align.INLINE)
d.comment(0xA023, "A=&FF: mark as newly opened", align=Align.INLINE)
d.comment(0xA025, "Store &FF as receive attribute", align=Align.INLINE)
d.comment(0xA028, "Load handle from fs_cmd_data", align=Align.INLINE)
d.comment(0xA02B, "Push handle", align=Align.INLINE)
d.comment(0xA02C, "A=4: file info sub-command", align=Align.INLINE)
d.comment(0xA02E, "Store sub-command", align=Align.INLINE)
d.comment(0xA031, "X=1: shift filename", align=Align.INLINE)
d.label(0xA033, "loop_shift_filename")

d.comment(0xA033, "Load filename byte from fs_func_code+X", align=Align.INLINE)
d.comment(0xA036, "Shift down to fs_cmd_data+X", align=Align.INLINE)
d.comment(0xA039, "Advance source index", align=Align.INLINE)
d.comment(0xA03A, "Is it CR (end of filename)?", align=Align.INLINE)
d.comment(0xA03C, "No: continue shifting", align=Align.INLINE)
d.comment(0xA03E, "Y=&12: file info request", align=Align.INLINE)
d.comment(0xA040, "Send file info request", align=Align.INLINE)
d.comment(0xA043, "Load last byte flag", align=Align.INLINE)
d.comment(0xA045, "Clear bit 6 (read/write bits)", align=Align.INLINE)
d.comment(0xA047, "OR with reply access byte", align=Align.INLINE)
d.comment(0xA04A, "Set bit 0 (file is open)", align=Align.INLINE)
d.comment(0xA04C, "Transfer to Y (access flags)", align=Align.INLINE)
d.comment(0xA04D, "Check bit 1 (write access)", align=Align.INLINE)
d.comment(0xA04F, "No write access: check read-only", align=Align.INLINE)
d.comment(0xA051, "Pull handle from stack", align=Align.INLINE)
d.comment(0xA052, "Allocate FCB slot for channel", align=Align.INLINE)
d.comment(0xA055, "Non-zero: FCB allocated, store flags", align=Align.INLINE)
d.label(0xA057, "findv_handler")

d.comment(0xA057, "Verify workspace checksum", align=Align.INLINE)
d.comment(0xA05A, "Set up transfer parameters", align=Align.INLINE)
d.comment(0xA05D, "Transfer A to X", align=Align.INLINE)
d.comment(0xA05E, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xA061, "Transfer X back to A", align=Align.INLINE)
d.comment(0xA062, "Zero: close file, process FCBs", align=Align.INLINE)
d.comment(0xA064, "Save text pointer for OS", align=Align.INLINE)
d.comment(0xA067, "Load current directory handle", align=Align.INLINE)
d.comment(0xA06A, "Zero: allocate new FCB", align=Align.INLINE)
d.comment(0xA06C, "Transfer Y to A", align=Align.INLINE)
d.comment(0xA06D, "X=0: clear directory handle", align=Align.INLINE)
d.comment(0xA06F, "Store zero (clear handle)", align=Align.INLINE)
d.comment(0xA072, "ALWAYS branch to finalise", align=Align.INLINE)
d.label(0xA074, "check_open_mode")

d.comment(0xA074, "Load access/open mode byte", align=Align.INLINE)
d.comment(0xA077, "Rotate right: check bit 0", align=Align.INLINE)
d.comment(0xA078, "Carry set (bit 0): check read permission", align=Align.INLINE)
d.comment(0xA07A, "Rotate right: check bit 1", align=Align.INLINE)
d.comment(0xA07B, "Carry clear (no write): skip", align=Align.INLINE)
d.comment(0xA07D, "Test bit 7 of fs_data_count (lock flag)", align=Align.INLINE)
d.comment(0xA080, "Not locked: skip", align=Align.INLINE)
d.comment(0xA082, "Transfer Y to A (flags)", align=Align.INLINE)
d.comment(0xA083, "Set bit 5 (locked file flag)", align=Align.INLINE)
d.comment(0xA085, "Transfer back to Y", align=Align.INLINE)
d.label(0xA086, "alloc_fcb_with_flags")

d.comment(0xA086, "Pull handle from stack", align=Align.INLINE)
d.comment(0xA087, "Allocate FCB slot for channel", align=Align.INLINE)
d.label(0xA08A, "store_fcb_flags")

d.comment(0xA08A, "Transfer to X", align=Align.INLINE)
d.comment(0xA08B, "Transfer Y to A (flags)", align=Align.INLINE)
d.comment(0xA08C, "Store flags in FCB table fcb_flags", align=Align.INLINE)
d.comment(0xA08F, "Transfer X back to A (handle)", align=Align.INLINE)
d.label(0xA090, "done_osfind")

d.comment(0xA090, "Jump to finalise and return", align=Align.INLINE)
d.label(0xA093, "close_all_channels")

d.comment(0xA093, "Process all matching FCBs", align=Align.INLINE)
d.comment(0xA096, "Transfer Y to A", align=Align.INLINE)
d.comment(0xA097, "Non-zero channel: close specific", align=Align.INLINE)
d.comment(0xA099, "Load FS options pointer low", align=Align.INLINE)
d.comment(0xA09B, "Push (save for restore)", align=Align.INLINE)
d.comment(0xA09C, "A=&77: OSBYTE close spool/exec files", align=Align.INLINE)
d.comment(0xA09E, "Close any *SPOOL and *EXEC files", align=Align.INLINE)
d.comment(0xA0A1, "Pull saved options pointer", align=Align.INLINE)
d.comment(0xA0A2, "Restore FS options pointer", align=Align.INLINE)
d.comment(0xA0A4, "A=0: clear flags", align=Align.INLINE)
d.comment(0xA0A6, "Save to fs_work_5", align=Align.INLINE)
d.comment(0xA0A8, "Load current FS station low", align=Align.INLINE)
d.comment(0xA0AA, "ALWAYS branch to send close request", align=Align.INLINE)
d.comment(0xA0AB, "Save to fs_work_6", align=Align.INLINE)
d.label(0xA0AC, "close_specific_chan")

d.comment(0xA0AC, "Validate channel character", align=Align.INLINE)
d.comment(0xA0AF, "Is it CR (no argument)?", align=Align.INLINE)
d.label(0xA0B2, "send_close_request")

d.comment(0xA0B2, "Store as fs_cmd_data (file handle)", align=Align.INLINE)
d.comment(0xA0B5, "X=1: argument size", align=Align.INLINE)
d.comment(0xA0B7, "Y=7: close file command", align=Align.INLINE)
d.comment(0xA0B9, "Send close file request", align=Align.INLINE)
d.comment(0xA0BC, "Parameter block low", align=Align.INLINE)
d.comment(0xA0BE, "Parameter block high", align=Align.INLINE)
d.comment(0xA0C0, "Clear V flag", align=Align.INLINE)
d.comment(0xA0C1, "Scan and clear all FCB flags", align=Align.INLINE)
d.label(0xA0C4, "done_close")

d.comment(0xA0C4, "Return with last flag", align=Align.INLINE)
d.label(0xA0C7, "clear_single_fcb")

d.comment(0xA0C7, "A=0: clear FCB entry", align=Align.INLINE)
d.comment(0xA0C9, "Clear hazel_fcb_addr_mid for slot Y", align=Align.INLINE)
d.comment(0xA0CC, "Clear hazel_fcb_state_byte for slot Y", align=Align.INLINE)
d.comment(0xA0CF, "Z still set from LDA #0: always branch to done_close", align=Align.INLINE)
d.label(0xA0D1, "fscv_0_opt_entry")

d.subroutine(
    0xA0D1,
    "fscv_0_opt_entry",
    title="FSCV reason 0: read OSARGS",
    description="""Handles OSARGS via the FSCV vector. If `A=0` (initialise dot-seen
flag) clears the flag and proceeds. Compares `X` against 4 (number
of args): out-of-range exits via the OSARGS dispatch chain to a
shared error path; otherwise dispatches to the per-argument
handler. Reached via the FSCV vector with reason code 0.""",
    on_entry={"a": "OSARGS sub-function (0 = initialise)", "x": "argument index (0-3)"},
)


d.entry(0xA0D1)
d.comment(0xA0D1, "A=0 (init sub-code): jump to store_display_flag", align=Align.INLINE)
d.comment(0xA0D3, "Non-zero A: X==4? (read OSARGS args)", align=Align.INLINE)
d.comment(0xA0D5, "X != 4: take normal OSARGS dispatch", align=Align.INLINE)
d.comment(0xA0D7, "X==4 path: Y < 4?", align=Align.INLINE)
d.comment(0xA0D9, "Yes: send OSARGS request via TXCB", align=Align.INLINE)
d.label(0xA0DB, "osargs_dispatch")

d.comment(0xA0DB, "X-- (osargs_dispatch entry): step sub-code down", align=Align.INLINE)
d.comment(0xA0DC, "X != 1: take store-ptr-lo path", align=Align.INLINE)
d.label(0xA0DE, "store_display_flag")

d.comment(0xA0DE, "Store Y as hazel_fs_messages_flag (display control)", align=Align.INLINE)
d.comment(0xA0E1, "Tail-branch to done_close", align=Align.INLINE)
d.label(0xA0E3, "error_osargs")

d.comment(0xA0E3, "A=7: error code (out-of-range OSARGS sub-code)", align=Align.INLINE)
d.comment(0xA0E5, "Raise BRK error", align=Align.INLINE)
d.label(0xA0E8, "send_osargs_request")

d.comment(0xA0E8, "Store Y as TXCB data byte (OSARGS payload)", align=Align.INLINE)
d.comment(0xA0EB, "Y=&16: TXCB function code (OSARGS request)", align=Align.INLINE)
d.comment(0xA0ED, "Send OSARGS request via TX control block", align=Align.INLINE)
d.comment(0xA0F0, "Reload Y from fs_block_offset", align=Align.INLINE)
d.comment(0xA0F2, "Update hazel_fs_flags from OSARGS reply", align=Align.INLINE)
d.comment(0xA0F5, "No error (positive): tail to done_close", align=Align.INLINE)
d.label(0xA0F7, "osargs_store_ptr_lo")

d.comment(0xA0F7, "X >= 8?", align=Align.INLINE)
d.comment(0xA0F9, "Yes: out-of-range OSARGS sub-code", align=Align.INLINE)
d.comment(0xA0FB, "X == 4?", align=Align.INLINE)
d.comment(0xA0FD, "Yes: take fast read path (osargs_check_length)", align=Align.INLINE)
d.comment(0xA0FF, "Y < 4?", align=Align.INLINE)
d.comment(0xA101, "Yes: take CMOS-protect path", align=Align.INLINE)
d.label(0xA103, "osargs_check_length")

d.comment(0xA103, "Y >= 2?", align=Align.INLINE)
d.comment(0xA105, "Yes: argument out of range", align=Align.INLINE)
d.label(0xA107, "osopt_check_cmos_protect")

d.comment(0xA108, "Save sub-code across the CMOS read", align=Align.INLINE)
d.comment(0xA109, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0xA10B, "Read CMOS &11 (Econet status) -> Y", align=Align.INLINE)
d.comment(0xA10E, "Restore sub-code", align=Align.INLINE)
d.comment(0xA10F, "Read CMOS &11 result to A", align=Align.INLINE)
d.comment(0xA110, "Mask CMOS &11 with cmos_opt_mask_table[X]", align=Align.INLINE)
d.comment(0xA114, "Push CMOS value", align=Align.INLINE)
d.comment(0xA115, "Load shift count from cmos_attr_table[X]", align=Align.INLINE)
d.comment(0xA118, "Value to X", align=Align.INLINE)
d.comment(0xA119, "Caller's Y back to A as the value to shift", align=Align.INLINE)
d.comment(0xA11A, "Shift CMOS bits", align=Align.INLINE)
d.label(0xA11A, "loop_extract_attr_bits")

d.comment(0xA11B, "Count down shift iterations", align=Align.INLINE)
d.comment(0xA11C, "Loop until X reaches 0", align=Align.INLINE)
d.comment(0xA11E, "Stash shifted value in fs_load_addr scratch", align=Align.INLINE)
d.comment(0xA120, "Pop saved value", align=Align.INLINE)
d.comment(0xA121, "OR with the CMOS-masked value", align=Align.INLINE)
d.comment(0xA124, "X=&11: target CMOS byte for write-back", align=Align.INLINE)
d.label(0xA126, "osopt_cmos_writeback_jsr")

d.comment(0xA126, "Write CMOS RAM byte (Y) to byte index (X)", align=Align.INLINE)
# UNMAPPED: d.label(
# UNMAPPED:     0xA0FF,
# UNMAPPED:     "cmos_attr_table",
# UNMAPPED:     description="""Indexing-base alias of [`cmos_opt_mask_table`](label:cmos_opt_mask_table) - 4.
# UNMAPPED: `LDA cmos_attr_table,X` at &A0ED with X=4..7 reads the read-masks 1, 2, 4, 6 from the underlying table; those values double as bit-shift counts that left-align the new field into CMOS &11. The byte at &A0FF is inside the operand of the JSR at &A0FE and is never read directly.""",
# UNMAPPED:     length=1,
# UNMAPPED:     group="idx_base",
# UNMAPPED:     access="r",
# UNMAPPED: )

d.comment(0xA129, "Tail-branch into the OSARGS done path", align=Align.INLINE)
d.index_base(0xA12B, "cmos_opt_mask_table")
d.banner(
    0xA12B,
    title="CMOS &11 bit-field masks for OSARGS / *OPT 4 (8 bytes)",
    description="""Used by the OSARGS-via-FSCV / *OPT 4 path
([`osopt_check_cmos_protect`](label:osopt_check_cmos_protect)) to read or update bit
fields inside CMOS RAM byte `&11` (the Econet status byte holding
the auto-boot type and printer/messages flags).

- **Indices 0-3** are extraction masks: `AND CMOS_&11` with
  `&01`, `&02`, `&04`, `&06` returns bit 0, bit 1, bit 2 or
  bits 1+2 respectively.
- **Indices 4-7** are clear masks: `AND CMOS_&11` with `&FD`,
  `&F3`, `&CF`, `&3F` zeroes bits 1, 2-3, 4-5 or 6-7 in turn,
  before OR-ing the new value back in.

A second indexed-base trick reads the same eight bytes through
[`cmos_attr_table`](address:A0FF) (this label - 4): for write
sub-codes 4-7 the read-masks at indices 0-3 (1, 2, 4, 6) double
as the bit-shift counts that left-align the new value into its
target field.""",
)
for _i in range(8):
    d.byte(0xA12B + _i)
del _i
d.comment(0xA12B, "Idx 0: AND mask = &01 (extract CMOS &11 bit 0)", align=Align.INLINE)
d.comment(0xA12C, "Idx 1: AND mask = &02 (extract CMOS &11 bit 1)", align=Align.INLINE)
d.comment(0xA12D, "Idx 2: AND mask = &04 (extract CMOS &11 bit 2)", align=Align.INLINE)
d.comment(0xA12E, "Idx 3: AND mask = &06 (extract CMOS &11 bits 1,2)", align=Align.INLINE)
d.comment(0xA12F, "Idx 4: AND mask = &FD (clear CMOS &11 bit 1)", align=Align.INLINE)
d.comment(0xA130, "Idx 5: AND mask = &F3 (clear CMOS &11 bits 2,3)", align=Align.INLINE)
d.comment(0xA131, "Idx 6: AND mask = &CF (clear CMOS &11 bits 4,5)", align=Align.INLINE)
d.comment(0xA132, "Idx 7: AND mask = &3F (clear CMOS &11 bits 6,7)", align=Align.INLINE)

d.label(0xA133, "fscv_1_eof")

d.subroutine(
    0xA133,
    "fscv_1_eof",
    title="FSCV reason 1: EOF check",
    description="""Verifies the FS workspace checksum, then loads the channel's
block-offset byte (`fs_block_offset`, `&BC`), pushes it on the
stack and stores the per-channel attribute reference in `hazel_chan_attr`.
The body proceeds to compare the buffer byte count with the file
length to decide whether the channel is at EOF. Reached via the
FSCV vector with reason code 1.""",
    on_entry={"y": "channel handle"},
    on_exit={"a": "0 = not at EOF, non-zero = EOF"},
)


d.entry(0xA133)
d.comment(0xA133, "Verify workspace checksum", align=Align.INLINE)
d.comment(0xA136, "Push checksum-verify result -- preserve it across the FCB lookups below", align=Align.INLINE)
d.comment(0xA137, "Load block offset", align=Align.INLINE)
d.comment(0xA139, "Push block offset", align=Align.INLINE)
d.comment(0xA13A, "Store X in cur_chan_attr", align=Align.INLINE)
d.comment(0xA13D, "Find matching FCB entry", align=Align.INLINE)
d.comment(0xA140, "Zero: no match found", align=Align.INLINE)
d.comment(0xA142, "Load FCB low byte from fcb_count_lo", align=Align.INLINE)
d.comment(0xA145, "Compare with stored offset fcb_buf_offset", align=Align.INLINE)
d.comment(0xA148, "FCB lo-byte below stored offset -> not the matching FCB; mark_not_found", align=Align.INLINE)
d.comment(0xA14A, "X=&FF: mark as found (all bits set)", align=Align.INLINE)
d.comment(0xA14C, "ALWAYS branch (negative)", align=Align.INLINE)
d.label(0xA14E, "mark_not_found")

d.comment(0xA14E, "X=0: mark as not found", align=Align.INLINE)
d.label(0xA150, "restore_and_return")

d.comment(0xA150, "Restore block offset from stack", align=Align.INLINE)
d.comment(0xA151, "Generate 'Syntax' error", align=Align.INLINE)
d.comment(0xA152, "Restore result from stack", align=Align.INLINE)
d.comment(0xA153, "Return", align=Align.INLINE)
d.label(0xA154, "update_addr_from_offset9")

d.subroutine(
    0xA154,
    "update_addr_from_offset9",
    title="Update both address fields in FS options",
    description="""Calls [`add_workspace_to_fsopts`](label:add_workspace_to_fsopts) for offset
9 (the high address / exec address field), then falls through to
[`update_addr_from_offset1`](label:update_addr_from_offset1) to process offset
1 (the low address / load address field).""",
    on_exit={"a, x, y, c flag": "clobbered (4-byte arithmetic loop)"},
)


d.comment(0xA154, "Y=9: FS options offset for high address", align=Align.INLINE)
d.comment(0xA156, "Add workspace values to FS options", align=Align.INLINE)
d.label(0xA159, "update_addr_from_offset1")

d.subroutine(
    0xA159,
    "update_addr_from_offset1",
    title="Update low address field in FS options",
    description="""Sets Y=1 and falls through to
add_workspace_to_fsopts to add the workspace
adjustment bytes to the load address field at
offset 1 in the FS options block.""",
    on_entry={"c": "carry state passed to add_workspace_to_fsopts"},
)


d.comment(0xA159, "Y=1: FS options offset for low address", align=Align.INLINE)
d.label(0xA15B, "add_workspace_to_fsopts")

d.subroutine(
    0xA15B,
    "add_workspace_to_fsopts",
    title="Add workspace bytes to FS options with clear carry",
    description="""Clears carry and falls through to
adjust_fsopts_4bytes. Provides a convenient entry
point when the caller needs addition without a
preset carry.""",
    on_entry={"y": "FS options offset for first byte"},
)


d.comment(0xA15B, "Clear carry for the upcoming 4-byte add", align=Align.INLINE)
d.label(0xA15C, "adjust_fsopts_4bytes")

d.subroutine(
    0xA15C,
    "adjust_fsopts_4bytes",
    title="Add or subtract 4 workspace bytes from FS options",
    description="""Processes 4 consecutive bytes at `(fs_options)+Y`, adding or
subtracting the corresponding 4-byte transfer-address record
from ANFS workspace.

The direction is controlled by bit 7 of `fs_load_addr_2`:

| Bit 7 | Operation |
|---|---|
| set   | subtract |
| clear | add |

Carry propagates across all 4 bytes for correct multi-byte
arithmetic.""",
    on_entry={"y": "FS options offset for first byte", "c": "carry input for first byte"},
)

d.comment(0xA15C, "X=&FC: loop counter (-4 to -1)", align=Align.INLINE)
d.label(0xA15E, "loop_adjust_byte")

d.comment(0xA15E, "Load FS options byte at offset Y", align=Align.INLINE)
d.comment(0xA160, "Test fs_load_addr_2 bit 7 (add/subtract)", align=Align.INLINE)
d.comment(0xA162, "Push high byte", align=Align.INLINE)
d.comment(0xA164, "Add workspace byte to FS options", align=Align.INLINE)
d.comment(0xA167, "RTS dispatches to command handler", align=Align.INLINE)
d.label(0xA16A, "subtract_ws_byte")

d.comment(0xA16A, "Subtract workspace byte from FS options", align=Align.INLINE)
d.label(0xA16D, "store_adjusted_byte")

d.subroutine(
    0xA16D,
    "store_adjusted_byte",
    title="Store adjusted byte and step the loop",
    description="""Tail of the address-adjustment 4-byte loop: STA (fs_options),Y /
INY / INX / BNE loop_adjust_byte / RTS. The BNE retries until X
has cycled through all 4 bytes; once X overflows back to 0 the
loop exits and the RTS returns. Single caller (the loop-body fall-
through at &A167).""",
    on_entry={"a": "byte to store", "y": "current FS-options index", "x": "remaining-byte counter"},
)


d.comment(0xA16D, "Store result back to FS options", align=Align.INLINE)
d.comment(0xA16F, "Advance to next byte", align=Align.INLINE)
d.comment(0xA170, "Advance counter", align=Align.INLINE)
d.comment(0xA171, "Loop until 4 bytes processed", align=Align.INLINE)
d.comment(0xA173, "Return", align=Align.INLINE)
d.subroutine(
    0xA174,
    "gbpbv_handler",
    title="GBPBV vector handler: OSGBPB",
    description="""Reached via the GBPBV vector at
[`vec_gbpbv`](label:vec_gbpbv) after the
[`fs_vector_table`](label:fs_vector_table) has copied the entry.
Verifies the FS workspace checksum, sets up transfer parameters,
masks the access prefix, and dispatches the OSGBPB sub-operation
in `A`:

| `A` | Operation |
|---|---|
| `1` | PUT bytes with pointer |
| `2` | PUT bytes |
| `3` | GET bytes with pointer |
| `4` | GET bytes |
| `5` | read disc title |
| `6` | read CSD |
| `7` | read library |
| `8` | read files in CSD |""",
    on_entry={"a": "OSGBPB function code (1-8)", "x, y": "control-block pointer (low, high)"},
)


d.entry(0xA174)
d.comment(0xA174, "Verify workspace checksum", align=Align.INLINE)
d.comment(0xA177, "Set up transfer parameters", align=Align.INLINE)
d.comment(0xA17A, "Push transfer type on stack", align=Align.INLINE)
d.comment(0xA17B, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xA17E, "Pull transfer type", align=Align.INLINE)
d.comment(0xA17F, "Transfer to X", align=Align.INLINE)
d.comment(0xA180, "Zero: no valid operation, return", align=Align.INLINE)
d.comment(0xA182, "Decrement (convert 1-based to 0-based)", align=Align.INLINE)
d.comment(0xA183, "Compare with 8 (max operation)", align=Align.INLINE)
d.comment(0xA185, "Below 8: valid operation", align=Align.INLINE)
d.label(0xA187, "skip_if_out_of_range")

d.comment(0xA187, "Out of range: return with flag", align=Align.INLINE)
d.label(0xA18A, "valid_osgbpb_op")

d.comment(0xA18A, "Transfer operation code to A", align=Align.INLINE)
d.comment(0xA18B, "Y=0: buffer offset", align=Align.INLINE)
d.comment(0xA18D, "Push operation code", align=Align.INLINE)
d.comment(0xA18E, "Compare with 4 (write operations)", align=Align.INLINE)
d.comment(0xA190, "Below 4: read operation", align=Align.INLINE)
d.comment(0xA192, "4 or above: write data block", align=Align.INLINE)
d.label(0xA195, "load_chan_handle")

d.comment(0xA195, "Load channel handle from FS options", align=Align.INLINE)
d.comment(0xA197, "Push handle", align=Align.INLINE)
d.comment(0xA198, "Check file is not a directory", align=Align.INLINE)
# UNMAPPED: d.comment(0xA173, "Pull handle", align=Align.INLINE)
# UNMAPPED: d.comment(0xA174, "Transfer to Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xA175, "Process all matching FCBs", align=Align.INLINE)
# UNMAPPED: d.comment(0xA178, "Load FCB flag byte from fcb_net_or_port", align=Align.INLINE)
# UNMAPPED: d.comment(0xA17B, "Store file handle in fs_cmd_data", align=Align.INLINE)
# UNMAPPED: d.comment(0xA17E, "A=0: clear direction flag", align=Align.INLINE)
# UNMAPPED: d.comment(0xA180, "Store in fs_func_code", align=Align.INLINE)
# UNMAPPED: d.comment(0xA183, "Load FCB low byte (position)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA186, "Store in fs_data_count", align=Align.INLINE)
# UNMAPPED: d.comment(0xA189, "Load FCB high byte", align=Align.INLINE)
# UNMAPPED: d.comment(0xA18C, "Store in fs_reply_cmd", align=Align.INLINE)
# UNMAPPED: d.comment(0xA18F, "Load FCB extent byte", align=Align.INLINE)
# UNMAPPED: d.comment(0xA192, "Store in fs_load_vector", align=Align.INLINE)
# UNMAPPED: d.comment(0xA195, "Y=&0D: TX buffer size", align=Align.INLINE)
# UNMAPPED: d.comment(0xA197, "X=5: argument count", align=Align.INLINE)
d.comment(0xA19C, "Send TX control block to server", align=Align.INLINE)
d.comment(0xA19F, "Pull operation code", align=Align.INLINE)
d.comment(0xA1A0, "Set up transfer workspace", align=Align.INLINE)
d.comment(0xA1A3, "Save flags (carry from setup)", align=Align.INLINE)
d.comment(0xA1A4, "Y=0: index for channel handle", align=Align.INLINE)
d.comment(0xA1A6, "Load channel handle from FS options", align=Align.INLINE)
d.comment(0xA1A8, "Carry set (write): set active", align=Align.INLINE)
d.comment(0xA1AA, "Read: clear connection active", align=Align.INLINE)
d.comment(0xA1AD, "Branch to continue (always positive)", align=Align.INLINE)
d.label(0xA1AF, "set_write_active")

d.comment(0xA1AF, "Write: set connection active", align=Align.INLINE)
d.label(0xA1B2, "setup_gbpb_request")

d.comment(0xA1B2, "Clear fs_func_code (Y=0)", align=Align.INLINE)
d.comment(0xA1B5, "Look up channel slot data", align=Align.INLINE)
d.comment(0xA1B8, "Store flag byte in fs_cmd_data", align=Align.INLINE)
d.comment(0xA1BB, "Y=&0C: TX buffer size (short)", align=Align.INLINE)
d.comment(0xA1BD, "X=2: argument count", align=Align.INLINE)
d.comment(0xA1BF, "Send TX control block", align=Align.INLINE)
d.comment(0xA1C2, "Look up channel entry at Y=0", align=Align.INLINE)
d.comment(0xA1C5, "Y=9: FS options offset for position", align=Align.INLINE)
d.comment(0xA1C7, "Load new position low from fs_cmd_data", align=Align.INLINE)
d.comment(0xA1CA, "Update FCB low byte in fcb_count_lo", align=Align.INLINE)
d.comment(0xA1CD, "Store in FS options at Y=9", align=Align.INLINE)
d.comment(0xA1CF, "Y=&0A", align=Align.INLINE)
d.comment(0xA1D0, "Load new position high from fs_func_code", align=Align.INLINE)
d.comment(0xA1D3, "Update FCB high byte in fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0xA1D6, "Store in FS options at Y=&0A", align=Align.INLINE)
d.comment(0xA1D8, "Y=&0B", align=Align.INLINE)
d.comment(0xA1D9, "Load new extent from fs_data_count", align=Align.INLINE)
d.comment(0xA1DC, "Update FCB extent in fcb_station_or_count_hi", align=Align.INLINE)
d.comment(0xA1DF, "Store in FS options at Y=&0B", align=Align.INLINE)
d.comment(0xA1E1, "A=0: clear high byte of extent", align=Align.INLINE)
d.comment(0xA1E3, "Y=&0C", align=Align.INLINE)
d.comment(0xA1E4, "Store zero in FS options at Y=&0C", align=Align.INLINE)
d.comment(0xA1E6, "Restore flags", align=Align.INLINE)
d.comment(0xA1E7, "Carry clear: skip last-byte check", align=Align.INLINE)
d.comment(0xA1E9, "Load last-byte-of-transfer flag", align=Align.INLINE)
d.comment(0xA1EB, "Is transfer still pending (flag=3)?", align=Align.INLINE)
d.label(0xA1ED, "return_success")


d.comment(0xA1ED, "A=0: success", align=Align.INLINE)
d.comment(0xA1EF, "Jump to finalise and return", align=Align.INLINE)
d.label(0xA1F2, "lookup_cat_entry_0")

d.subroutine(
    0xA1F2,
    "lookup_cat_entry_0",
    title="Look up channel from FS options offset 0",
    description="""Loads the channel handle from (fs_options) at
offset 0, then falls through to lookup_cat_slot_data
to find the corresponding FCB entry.""",
    on_exit={"a": "FCB flag byte from hazel_fcb_slot_attr,X", "x": "channel slot index"},
)


d.comment(0xA1F2, "Y=0: offset for channel handle", align=Align.INLINE)
d.comment(0xA1F4, "Load channel handle from FS options", align=Align.INLINE)
d.label(0xA1F6, "lookup_cat_slot_data")

d.subroutine(
    0xA1F6,
    "lookup_cat_slot_data",
    title="Look up channel and return FCB flag byte",
    description="""Calls [`lookup_chan_by_char`](label:lookup_chan_by_char) to find the channel
slot for handle `A` in the channel table, then loads the FCB
slot-attribute byte from
[`hazel_fcb_slot_attr`](label:hazel_fcb_slot_attr)+`X`.""",
    on_entry={"a": "channel handle"},
    on_exit={"a": "FCB slot-attribute byte", "x": "channel slot index"},
)


d.comment(0xA1F6, "Look up channel by character", align=Align.INLINE)
d.comment(0xA1F9, "Load slot-attribute byte from hazel_fcb_slot_attr,X", align=Align.INLINE)
d.comment(0xA1FC, "Return with flag in A", align=Align.INLINE)
d.label(0xA1FD, "setup_transfer_workspace")

d.subroutine(
    0xA1FD,
    "setup_transfer_workspace",
    title="Prepare workspace for OSGBPB data transfer",
    description="""Orchestrates the setup for OSGBPB (get/put multiple bytes)
operations:

1. Look up the channel.
2. Copy the 6-byte address structure from FS options (skipping
   the hole at offset 8).
3. Determine transfer direction from the operation code:

   | Operation code parity | Direction | FS port |
   |---|---|---|
   | even | read  | `&91` |
   | odd  | write | `&92` |

4. Send the FS request.
5. Configure the TXCB address pairs for the actual
   data-transfer phase.
6. Dispatch to the appropriate handler.""",
    on_exit={"a": "FS reply status from the data-transfer phase"},
)


d.comment(0xA1FD, "Push operation code on stack", align=Align.INLINE)
d.comment(0xA1FE, "Look up channel entry at Y=0", align=Align.INLINE)
d.comment(0xA201, "Store flag byte in fs_cmd_data", align=Align.INLINE)
d.comment(0xA205, "Y=&0B: source offset in FS options", align=Align.INLINE)
d.comment(0xA207, "X=6: copy 6 bytes", align=Align.INLINE)
d.label(0xA209, "loop_copy_opts_to_buf")

d.comment(0xA209, "Load FS options byte", align=Align.INLINE)
d.comment(0xA20B, "Store in fs_func_code buffer", align=Align.INLINE)
d.comment(0xA20E, "Decrement source index", align=Align.INLINE)
d.comment(0xA20F, "Skip offset 8?", align=Align.INLINE)
d.comment(0xA211, "No: continue copy", align=Align.INLINE)
d.comment(0xA213, "Skip offset 8 (hole in structure)", align=Align.INLINE)
d.label(0xA214, "skip_struct_hole")

d.comment(0xA214, "Decrement destination counter", align=Align.INLINE)
d.comment(0xA215, "Loop until all 6 bytes copied", align=Align.INLINE)
# UNMAPPED: d.comment(0xA213, "Pull operation code", align=Align.INLINE)
# UNMAPPED: d.comment(0xA214, "Shift right: check bit 0 (direction)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA215, "Push updated code", align=Align.INLINE)
# UNMAPPED: d.comment(0xA216, "Carry clear: OSBGET (read)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA218, "Carry set: OSBPUT (write), X=1", align=Align.INLINE)
d.label(0xA22F, "store_direction_flag")

d.comment(0xA22F, "Store direction flag in fs_func_code", align=Align.INLINE)
d.comment(0xA232, "Y=&0B: TX buffer size", align=Align.INLINE)
d.comment(0xA234, "X=&91: port for OSBGET", align=Align.INLINE)
d.comment(0xA236, "Pull operation code", align=Align.INLINE)
d.comment(0xA237, "Push back (keep on stack)", align=Align.INLINE)
d.comment(0xA238, "Zero (OSBGET): keep port &91", align=Align.INLINE)
d.comment(0xA23A, "X=&92: port for OSBPUT", align=Align.INLINE)
d.comment(0xA23C, "Y=&0A: adjusted buffer size", align=Align.INLINE)
d.label(0xA23D, "store_port_and_send")

d.comment(0xA23D, "Store port in fs_cmd_urd", align=Align.INLINE)
d.comment(0xA240, "Store port in fs_error_ptr", align=Align.INLINE)
d.comment(0xA242, "X=8: argument count", align=Align.INLINE)
d.comment(0xA244, "Load file handle from fs_cmd_data", align=Align.INLINE)
d.comment(0xA247, "Send request (no write data)", align=Align.INLINE)
d.comment(0xA24A, "X=0: index", align=Align.INLINE)
d.comment(0xA24C, "Load channel handle from FS options", align=Align.INLINE)
d.comment(0xA24E, "Transfer to X as index", align=Align.INLINE)
d.comment(0xA24F, "Load FCB flags from fcb_flags", align=Align.INLINE)
d.comment(0xA252, "Toggle bit 0 (transfer direction)", align=Align.INLINE)
d.comment(0xA254, "Store updated flags", align=Align.INLINE)
d.comment(0xA257, "Clear carry for addition", align=Align.INLINE)
d.comment(0xA258, "X=4: process 4 address bytes", align=Align.INLINE)
d.label(0xA25A, "loop_setup_addr_bytes")

d.comment(0xA25A, "Load FS options address byte", align=Align.INLINE)
d.comment(0xA25C, "Store in zero page address area", align=Align.INLINE)
d.comment(0xA25F, "Store in TXCB position", align=Align.INLINE)
d.comment(0xA262, "Advance Y by 4", align=Align.INLINE)
d.comment(0xA265, "Add offset from FS options", align=Align.INLINE)
d.comment(0xA267, "Store computed end address", align=Align.INLINE)
d.comment(0xA26A, "Retreat Y by 3 for next pair", align=Align.INLINE)
d.comment(0xA26D, "Decrement byte counter", align=Align.INLINE)
d.comment(0xA26E, "Loop for all 4 address bytes", align=Align.INLINE)
d.comment(0xA270, "X=1 (INX from 0)", align=Align.INLINE)
d.label(0xA271, "loop_copy_offset")

d.comment(0xA271, "Load offset from fs_cmd_csd", align=Align.INLINE)
d.comment(0xA274, "Copy to fs_func_code", align=Align.INLINE)
d.comment(0xA277, "Decrement counter", align=Align.INLINE)
d.comment(0xA278, "Loop until both bytes copied", align=Align.INLINE)
d.comment(0xA27A, "Pull operation code", align=Align.INLINE)
d.comment(0xA27B, "Non-zero (OSBPUT): swap addresses", align=Align.INLINE)
d.comment(0xA27D, "Load port from fs_cmd_urd", align=Align.INLINE)
d.comment(0xA280, "Check and set up TXCB", align=Align.INLINE)
d.comment(0xA283, "Carry set: skip swap", align=Align.INLINE)
d.label(0xA285, "send_with_swap")

d.comment(0xA285, "Send TXCB and swap start/end addresses", align=Align.INLINE)
d.label(0xA288, "recv_and_update")

d.comment(0xA288, "Receive and process reply", align=Align.INLINE)
d.comment(0xA28B, "Store result in fs_load_addr_2", align=Align.INLINE)
d.comment(0xA28D, "Update addresses from offset 9", align=Align.INLINE)
d.comment(0xA290, "Decrement fs_load_addr_2", align=Align.INLINE)
d.comment(0xA292, "Set carry for subtraction", align=Align.INLINE)
d.comment(0xA293, "Adjust FS options by 4 bytes", align=Align.INLINE)
d.comment(0xA296, "Shift fs_cmd_data left (update status)", align=Align.INLINE)
d.comment(0xA299, "Return", align=Align.INLINE)
d.subroutine(
    0xA29A,
    "recv_reply_preserve_flags",
    title="Receive and process reply, preserving flags",
    description="""Wrapper around recv_and_process_reply that
saves and restores the processor status register,
so the caller's flag state is not affected by
the reply processing.""",
    on_exit={"a": "FS reply status", "p (flags)": "preserved across the call (PHP/PLP)"},
)


d.comment(0xA29A, "Save flags before reply processing", align=Align.INLINE)
d.comment(0xA29B, "Process server reply", align=Align.INLINE)
d.comment(0xA29E, "Restore flags after reply processing", align=Align.INLINE)
d.comment(0xA29F, "Return", align=Align.INLINE)
d.label(0xA2A0, "send_osbput_data")

d.subroutine(
    0xA2A0,
    "send_osbput_data",
    title="Send OSBPUT data block to file server",
    description="""Sets `Y=&15` (TX buffer size for OSBPUT data) and calls
[`save_net_tx_cb`](label:save_net_tx_cb) to dispatch the TX. Then copies
the display flag from `hazel_fs_flags` to `hazel_txcb_byte_16` (TX header continuation).
Single caller in the OSBPUT-buffered-write path.""",
)


d.entry(0xA2A0)
d.comment(0xA2A0, "Y=&15: TX buffer size for OSBPUT data", align=Align.INLINE)
d.comment(0xA2A2, "Send TX control block", align=Align.INLINE)
d.comment(0xA2A5, "Load display flag from hazel_fs_flags", align=Align.INLINE)
d.comment(0xA2A8, "Store in hazel_txcb_byte_16", align=Align.INLINE)
d.comment(0xA2AB, "Clear fs_load_addr (X=0)", align=Align.INLINE)
d.comment(0xA2AD, "Clear fs_load_addr_hi", align=Align.INLINE)
d.comment(0xA2AF, "A=&12: byte count for data block", align=Align.INLINE)
d.comment(0xA2B1, "Store in fs_load_addr_2", align=Align.INLINE)
d.comment(0xA2B3, "ALWAYS branch to write data block", align=Align.INLINE)
d.label(0xA2B5, "write_block_entry")

d.subroutine(
    0xA2B5,
    "write_block_entry",
    title="Pre-write Tube-station check, fall into write_data_block",
    description="""Y=4 (FS-options offset for station). If tube_present is zero
(no Tube co-pro), branch forward to store_station_result and skip
the next compare; otherwise CMP (fs_options),Y to validate the
caller's station matches the saved Tube station. Falls through to
write_data_block. Single caller (&A190 in the OSWORD write path).""",
    on_entry={"y": "ignored (forced to 4)"},
)


d.comment(0xA2B5, "Y=4: offset for station comparison", align=Align.INLINE)
d.comment(0xA2B7, "Load stored station from tube_present", align=Align.INLINE)
d.comment(0xA2BA, "Zero: skip station check", align=Align.INLINE)
d.comment(0xA2BC, "Compare with FS options station", align=Align.INLINE)
d.comment(0xA2BE, "Mismatch: skip subtraction", align=Align.INLINE)
d.comment(0xA2C0, "Y=3", align=Align.INLINE)
d.comment(0xA2C1, "Subtract FS options value", align=Align.INLINE)
d.label(0xA2C3, "store_station_result")

d.comment(0xA2C3, "Store result in svc_state", align=Align.INLINE)
d.label(0xA2C5, "loop_copy_opts_to_ws")

d.comment(0xA2C5, "Load FS options byte at Y", align=Align.INLINE)
d.comment(0xA2C7, "Store in workspace at fs_last_byte_flag+Y", align=Align.INLINE)
d.comment(0xA2CA, "Decrement index", align=Align.INLINE)
d.comment(0xA2CB, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0xA2CD, "Pull operation code", align=Align.INLINE)
d.comment(0xA2CE, "Mask to 2-bit sub-operation", align=Align.INLINE)
d.comment(0xA2D0, "Zero: send OSBPUT data", align=Align.INLINE)
d.comment(0xA2D2, "Shift right: check bit 0", align=Align.INLINE)
d.comment(0xA2D3, "Zero (bit 0 clear): handle read", align=Align.INLINE)
d.comment(0xA2D5, "Carry set: handle catalogue update", align=Align.INLINE)
d.label(0xA2D7, "handle_cat_update")

d.comment(0xA2D7, "Transfer to Y (Y=0)", align=Align.INLINE)
d.comment(0xA2D8, "Load data byte from fs_csd_handle", align=Align.INLINE)
d.comment(0xA2DB, "Store in fs_cmd_csd", align=Align.INLINE)
d.comment(0xA2DE, "Load high data byte from fs_lib_handle", align=Align.INLINE)
d.comment(0xA2E1, "Store in fs_cmd_lib", align=Align.INLINE)
d.comment(0xA2E4, "Load port from fs_urd_handle", align=Align.INLINE)
d.comment(0xA2E7, "Store in fs_cmd_urd", align=Align.INLINE)
d.comment(0xA2EA, "X=&12: buffer size marker", align=Align.INLINE)
d.comment(0xA2EC, "Store in fs_cmd_y_param", align=Align.INLINE)
d.comment(0xA2EF, "A=&0D: count value", align=Align.INLINE)
d.comment(0xA2F1, "Store in fs_func_code", align=Align.INLINE)
d.comment(0xA2F4, "Store in fs_load_addr_2", align=Align.INLINE)
d.comment(0xA2F6, "Shift right (A=6)", align=Align.INLINE)
d.comment(0xA2F7, "Store in fs_cmd_data", align=Align.INLINE)
d.comment(0xA2FA, "Clear carry for addition", align=Align.INLINE)
d.comment(0xA2FB, "Prepare and send TX control block", align=Align.INLINE)
d.comment(0xA2FE, "Store X in fs_load_addr_hi (X=0)", align=Align.INLINE)
d.comment(0xA300, "X=1 (after INX)", align=Align.INLINE)
d.comment(0xA301, "Store X in fs_load_addr", align=Align.INLINE)
d.label(0xA303, "write_data_block")

d.subroutine(
    0xA303,
    "write_data_block",
    title="Write data block to destination or Tube",
    description="""| `tube_present` | Action |
|---|---|
| zero (no Tube) | copy directly from the `fs_cmd_data` buffer via `(fs_crc_lo)` |
| non-zero       | claim the Tube, set up the transfer address, write via R3 |""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xA303, "Load svc_state (tube flag)", align=Align.INLINE)
d.comment(0xA305, "Non-zero: write via tube", align=Align.INLINE)
d.comment(0xA307, "Load source index from fs_load_addr", align=Align.INLINE)
d.comment(0xA309, "Load destination index from fs_load_addr_hi", align=Align.INLINE)
d.label(0xA30B, "loop_copy_to_host")

d.comment(0xA30B, "Load data byte from fs_cmd_data buffer", align=Align.INLINE)
d.comment(0xA30E, "Store to destination via fs_crc pointer", align=Align.INLINE)
d.comment(0xA310, "Advance source index", align=Align.INLINE)
d.comment(0xA311, "Advance destination index", align=Align.INLINE)
d.comment(0xA312, "Decrement byte counter", align=Align.INLINE)
d.comment(0xA314, "Loop until all bytes transferred", align=Align.INLINE)
d.comment(0xA316, "X=&10: scan 16 slots (15 to 0)", align=Align.INLINE)
d.label(0xA318, "tube_write_setup")

d.comment(0xA318, "Clear V", align=Align.INLINE)
d.comment(0xA31B, "A=1: tube transfer type (write)", align=Align.INLINE)
d.comment(0xA31D, "Load destination low from fs_options", align=Align.INLINE)
d.comment(0xA31F, "No match: try next", align=Align.INLINE)
d.comment(0xA321, "Load slot status byte", align=Align.INLINE)
d.comment(0xA322, "No wrap: skip high increment", align=Align.INLINE)
d.comment(0xA324, "Test bit 2 (PS active flag)?", align=Align.INLINE)
d.label(0xA325, "set_tube_addr")

d.comment(0xA325, "Set up tube transfer address", align=Align.INLINE)
d.comment(0xA328, "Transfer Y to A", align=Align.INLINE)
d.label(0xA32A, "loop_write_to_tube")

d.comment(0xA32A, "Load data byte from buffer", align=Align.INLINE)
d.comment(0xA32D, "Write to tube data register 3", align=Align.INLINE)
d.comment(0xA32F, "Store Y to fs_urd_handle", align=Align.INLINE)
d.comment(0xA330, "Advance source index", align=Align.INLINE)
d.comment(0xA331, "Y=6: tube write delay", align=Align.INLINE)
d.label(0xA333, "loop_tube_delay")

d.comment(0xA333, "Delay loop: decrement Y", align=Align.INLINE)
d.comment(0xA334, "Transfer Y to A", align=Align.INLINE)
d.comment(0xA336, "Decrement byte counter", align=Align.INLINE)
d.comment(0xA338, "Store allocation result", align=Align.INLINE)
d.comment(0xA33A, "A=&83: release tube claim", align=Align.INLINE)
d.comment(0xA33C, "Release tube", align=Align.INLINE)
d.label(0xA33F, "tail_update_catalogue")

d.subroutine(
    0xA33F,
    "tail_update_catalogue",
    title="Catalogue-update exit (JMP clear_result)",
    description="""Single-instruction tail: JMP clear_result -- shared exit for the
catalogue-update paths after they have finished writing the new
entry. Two callers: &A314 (the success path) and &A38F (the
no-change path). Never returns directly (clear_result loads A=0
and tail-falls into finalise_and_return).""",
)


d.comment(0xA33F, "Jump to clear A and finalise return", align=Align.INLINE)
d.label(0xA342, "update_cat_position")

d.comment(0xA342, "Y=9: offset for position byte", align=Align.INLINE)
d.comment(0xA344, "Try next slot", align=Align.INLINE)
d.comment(0xA346, "Store in fs_func_code", align=Align.INLINE)
d.comment(0xA349, "Y=5: offset for extent byte", align=Align.INLINE)
d.comment(0xA34B, "Load extent byte from FS options", align=Align.INLINE)
d.comment(0xA34D, "Store in fs_data_count", align=Align.INLINE)
d.comment(0xA350, "X=&0D: byte count", align=Align.INLINE)
d.comment(0xA352, "Store in fs_reply_cmd", align=Align.INLINE)
d.comment(0xA355, "Y=2: command sub-type", align=Align.INLINE)
d.comment(0xA357, "Set V (found match)", align=Align.INLINE)
d.comment(0xA359, "Store in fs_cmd_data", align=Align.INLINE)
d.comment(0xA35A, "Store Y to fs_csd_handle", align=Align.INLINE)
d.comment(0xA35C, "Y=3: TX buffer command byte", align=Align.INLINE)
d.comment(0xA35D, "V set: found, skip allocation", align=Align.INLINE)
d.comment(0xA360, "Allocate FCB slot", align=Align.INLINE)
d.comment(0xA362, "Load data offset from fs_func_code", align=Align.INLINE)
d.comment(0xA365, "Store as first byte of FS options", align=Align.INLINE)
d.comment(0xA367, "Load data count from fs_cmd_data", align=Align.INLINE)
d.comment(0xA36A, "Y=9: position offset in FS options", align=Align.INLINE)
d.comment(0xA36C, "Add to current position", align=Align.INLINE)
d.comment(0xA36E, "Store updated position", align=Align.INLINE)
d.comment(0xA370, "Load TXCB end byte", align=Align.INLINE)
d.comment(0xA372, "Subtract 7 (header overhead)", align=Align.INLINE)
d.comment(0xA374, "Store remaining data size", align=Align.INLINE)
d.comment(0xA377, "Store in fs_load_addr_2 (byte count)", align=Align.INLINE)
d.comment(0xA379, "Zero bytes: skip write", align=Align.INLINE)
d.comment(0xA37B, "Write data block to host/tube", align=Align.INLINE)
d.label(0xA37E, "clear_buf_after_write")

d.comment(0xA37E, "X=2: clear 3 bytes (indices 0-2)", align=Align.INLINE)
d.label(0xA380, "loop_clear_buf")

d.comment(0xA380, "Clear fs_data_count+X", align=Align.INLINE)
d.comment(0xA383, "Decrement index", align=Align.INLINE)
d.comment(0xA384, "Loop until all cleared", align=Align.INLINE)
d.comment(0xA386, "Update addresses from offset 1", align=Align.INLINE)
d.comment(0xA389, "Set carry for subtraction", align=Align.INLINE)
d.comment(0xA38A, "Decrement fs_load_addr_2", align=Align.INLINE)
d.comment(0xA38C, "Load data count from fs_cmd_data", align=Align.INLINE)
d.comment(0xA38F, "Copy to fs_func_code", align=Align.INLINE)
d.comment(0xA392, "Adjust FS options by 4 bytes (subtract)", align=Align.INLINE)
d.comment(0xA395, "X=3: check 4 bytes", align=Align.INLINE)
d.comment(0xA397, "Y=5: starting offset", align=Align.INLINE)
d.comment(0xA399, "Set carry for comparison", align=Align.INLINE)
d.label(0xA39A, "loop_check_remaining")

d.comment(0xA39A, "Load FS options byte", align=Align.INLINE)
d.comment(0xA39C, "Non-zero: more data remaining", align=Align.INLINE)
d.comment(0xA39E, "Advance to next byte", align=Align.INLINE)
d.comment(0xA39F, "Decrement counter", align=Align.INLINE)
d.comment(0xA3A0, "Loop until all bytes checked", align=Align.INLINE)
d.comment(0xA3A2, "All zero: clear carry (transfer complete)", align=Align.INLINE)
d.label(0xA3A3, "done_write_block")

d.comment(0xA3A3, "Jump to update catalogue and return", align=Align.INLINE)
d.label(0xA3A6, "tube_claim_c3")

d.subroutine(
    0xA3A6,
    "tube_claim_c3",
    title="Claim the Tube via protocol &C3",
    description="""Loops calling tube_addr_data_dispatch with
protocol byte &C3 until the claim succeeds
(carry set on return). Used before Tube data
transfers to ensure exclusive access to the
Tube co-processor interface.""",
    on_entry={},
    on_exit={
        "a": "&C3 (the claim protocol byte left in A)",
        "c flag": "set (the claim succeeded -- this is the loop termination condition)",
    },
)


d.comment(0xA3A6, "A=&C3: tube claim protocol", align=Align.INLINE)
d.comment(0xA3A8, "Dispatch tube address/data claim", align=Align.INLINE)
d.comment(0xA3AB, "Carry clear: claim failed, retry", align=Align.INLINE)
d.comment(0xA3AD, "Return (tube claimed)", align=Align.INLINE)
d.comment(0xA3AE, "Read current FS station from workspace", align=Align.INLINE)
d.entry(0xA3AE)
d.label(0xA3AE, "cmd_fs")

d.subroutine(
    0xA3AE,
    "cmd_fs",
    title="*FS command handler",
    description="""Saves the current file server station address, then
checks for a command-line argument. With no argument,
falls through to print_current_fs to display the active
server. With an argument, parses the station number via
parse_fs_ps_args and issues OSWORD &13 (sub-function 1)
to select the new file server.""",
    on_entry={"y": "command line offset in text pointer"},
)
d.comment(0xA3B1, "Save in fs_work_5 (so 'no-arg' path can print it)", align=Align.INLINE)
d.comment(0xA3B3, "Read current FS network", align=Align.INLINE)
d.comment(0xA3B6, "Save in fs_work_6", align=Align.INLINE)
d.comment(0xA3B8, "Look at the first command-line byte", align=Align.INLINE)
d.comment(0xA3BA, "Is it CR (no argument)?", align=Align.INLINE)
d.comment(0xA3BC, "Yes: print the current FS address", align=Align.INLINE)
d.comment(0xA3BE, "Parse 'net.station' arg into fs_work_5/6", align=Align.INLINE)
d.comment(0xA3C1, "A=1: OSWORD &13 sub-function 1 = set file server station", align=Align.INLINE)
d.comment(0xA3C3, "Store sub-function in PB[0]", align=Align.INLINE)
d.comment(0xA3C5, "A=&13: OSWORD &13", align=Align.INLINE)
d.comment(0xA3C7, "X = lo of PB pointer (fs_work_4 = &B4)", align=Align.INLINE)
d.comment(0xA3C9, "Y = hi of PB pointer (=0, since fs_work_4 is in zero page)", align=Align.INLINE)
d.comment(0xA3CB, "Tail-jump into OSWORD; the OS routes us back through osword_13_set_station", align=Align.INLINE)
d.label(0xA3CE, "print_current_fs")

d.comment(0xA3CE, "Print 'File server is ' fragment", align=Align.INLINE)
d.label(0xA3D1, "print_fs_info_newline")

d.subroutine(
    0xA3D1,
    "print_fs_info_newline",
    title="Print station address and newline",
    description="""Sets V (suppressing leading-zero padding on
the network number) then prints the station
address followed by a newline via OSNEWL.
Used by *FS and *PS output formatting.""",
    on_exit={"a, x, y": "clobbered (print_station_addr + OSNEWL)"},
)


d.comment(
    0xA3D1,
    "Set V so print_station_addr suppresses the leading '0.' when the network number is zero",
    align=Align.INLINE,
)
d.comment(0xA3D4, "Print the station/network address", align=Align.INLINE)
d.comment(0xA3D7, "Tail-call OSNEWL for the trailing CR/LF", align=Align.INLINE)
d.subroutine(
    0xA3DA,
    "parse_fs_ps_args",
    title="Parse station address from *FS/*PS arguments",
    description="""Reads a station address in `net.station` format from the command
line, with the network number optional (defaults to local network).
Calls [`init_bridge_poll`](label:init_bridge_poll) to ensure the bridge
routing table is populated, then validates the parsed address
against known stations. The parsed-station value is stored in
`fs_work_7` (`&B7`).""",
    on_entry={"y": "current command-line offset"},
    on_exit={"x, y": "preserved (saved/restored via PHX/PHY)"},
)


d.comment(0xA3DA, "Save caller's X (command-line offset cursor)", align=Align.INLINE)
d.comment(0xA3DB, "A=0: clear the dot-seen flag for parse_addr_arg", align=Align.INLINE)
d.comment(0xA3DD, "Store cleared dot-seen flag", align=Align.INLINE)
d.comment(0xA3DF, "Parse first number (network or standalone station)", align=Align.INLINE)
d.comment(0xA3E2, "C set: parse_addr_arg saw an empty argument -- skip station storage", align=Align.INLINE)
d.comment(0xA3E4, "Save the network number in fs_work_7", align=Align.INLINE)
d.comment(0xA3E6, "Save Y (current command-line cursor) for after the bridge poll", align=Align.INLINE)
d.comment(0xA3E7, "Populate the bridge routing table -- returns local network number in A", align=Align.INLINE)
d.comment(0xA3EA, "EOR with parsed network: Z set iff parse matched local", align=Align.INLINE)
d.comment(0xA3EC, "Match: keep A=0 to mark local network", align=Align.INLINE)
d.comment(0xA3EE, "Mismatch: A = parsed network number", align=Align.INLINE)
d.label(0xA3F0, "store_station_lo")

d.comment(
    0xA3F0, "Store network number into fs_work_6 (the canonical form: 0=local, non-zero=remote)", align=Align.INLINE
)
d.comment(0xA3F2, "Restore Y", align=Align.INLINE)
d.comment(0xA3F3, "Step Y past the dot separator", align=Align.INLINE)
d.comment(0xA3F4, "Parse station number after the dot", align=Align.INLINE)
d.label(0xA3F7, "skip_if_no_station")

d.comment(0xA3F7, "C set: no station after dot -- leave fs_work_5 alone", align=Align.INLINE)
d.comment(0xA3F9, "Store parsed station in fs_work_5", align=Align.INLINE)
d.comment(0xA3FB, "Restore caller's X", align=Align.INLINE)
d.label(0xA3FB, "no_station_loop")

d.comment(0xA3FC, "Return", align=Align.INLINE)
d.label(0xA3FD, "get_pb_ptr_as_index")

d.subroutine(
    0xA3FD,
    "get_pb_ptr_as_index",
    title="Convert parameter block pointer to table index",
    description="""Reads the first byte from the OSWORD parameter
block pointer and falls through to
byte_to_2bit_index to produce a 12-byte-aligned
table index in Y.""",
    on_exit={"a": "PB[0] (preserved through byte_to_2bit_index)", "y": "byte offset (0, 6, 12, ... up to &42)"},
)


d.comment(
    0xA3FD, "Read PB[0] (the OSWORD sub-function code in most calls); fall into byte_to_2bit_index", align=Align.INLINE
)
d.label(0xA3FF, "byte_to_2bit_index")

d.subroutine(
    0xA3FF,
    "byte_to_2bit_index",
    title="Convert byte to 12-byte-aligned table index",
    description="""Computes Y = A * 6 (via A*12/2) for indexing
into the OSWORD handler workspace tables.
Clamps Y to zero if the result exceeds &48,
preventing out-of-bounds access.""",
    on_entry={"a": "table entry number"},
    on_exit={"y": "byte offset (0, 6, 12, ... up to &42)"},
)


d.comment(0xA3FF, "Multiply A by 2", align=Align.INLINE)
d.comment(0xA400, "Multiply A by 2 again -- A is now A_orig * 4", align=Align.INLINE)
d.comment(0xA401, "Stash A_orig * 4 on the stack", align=Align.INLINE)
d.comment(0xA402, "Multiply A by 2 -- A is now A_orig * 8 (C = bit 7 of A_orig*4)", align=Align.INLINE)
d.comment(0xA403, "Capture S so we can read the just-pushed value", align=Align.INLINE)
d.comment(0xA404, "Save the C flag from the third ASL", align=Align.INLINE)
d.comment(
    0xA405,
    "ADC stack[X+1] = A_orig*4 (with C from the ASL): A = A_orig*8 + A_orig*4 + C = A_orig*12 + C",
    align=Align.INLINE,
)
d.comment(0xA408, "Halve the result, putting the new C as bit 7", align=Align.INLINE)
d.comment(0xA409, "Restore the saved C (from the third ASL)", align=Align.INLINE)
d.comment(
    0xA40A, "ASL doubles the halved value (effectively undoes the ROR's divide while reusing C)", align=Align.INLINE
)
d.comment(0xA40B, "Y = A_orig * 12 (the 12-byte-aligned index)", align=Align.INLINE)
d.comment(0xA40C, "Recover A_orig * 4 (left on the stack at &A3FF)", align=Align.INLINE)
d.comment(0xA40D, "Above &48 (i.e. A_orig * 4 >= 72, A_orig >= 18)?", align=Align.INLINE)
d.comment(0xA40F, "No: keep computed Y", align=Align.INLINE)
d.comment(0xA411, "Yes: clamp Y to 0 (out of range)", align=Align.INLINE)
d.comment(0xA413, "Mirror Y -> A so callers can test Z", align=Align.INLINE)
d.label(0xA414, "rts_2bit_index")

d.comment(0xA414, "Return; Y holds 12-byte-aligned offset, A is non-zero on success", align=Align.INLINE)
d.label(0xA415, "net_1_read_handle")

d.subroutine(
    0xA415,
    "net_1_read_handle",
    title="FS reply: read handle byte (no workspace lookup)",
    description="""Reads the inline handle byte directly from the RX buffer at
`(net_rx_ptr),Y` with `Y=&6F`, then branches into the shared
PB-store path. Used when the caller wants the raw handle byte from
the FS reply rather than the workspace-tracked value.""",
    on_exit={"a": "handle byte from RX buffer"},
)


d.comment(0xA415, "Y=&6F: net_rx_ptr offset for the 'inline' handle byte", align=Align.INLINE)
d.entry(0xA415)
d.comment(0xA417, "Read handle byte directly from RX buffer", align=Align.INLINE)
d.comment(0xA419, "C clear: read-handle path -- store directly to PB", align=Align.INLINE)
d.label(0xA41B, "net_2_read_entry")

d.subroutine(
    0xA41B,
    "net_2_read_entry",
    title="FS reply: read handle byte from workspace table",
    description="""Calls [`get_pb_ptr_as_index`](label:get_pb_ptr_as_index) to convert the OSWORD
parameter-block pointer to a workspace-table index. On out-of-range
(`C=1`), returns zero. Otherwise reads the handle byte from
`nfs_workspace,Y`; if the slot is `?` (uninitialised marker), falls
through to the zero-return path; otherwise stores the real handle
into PB[0].""",
)


d.comment(0xA41B, "Convert PB pointer to workspace table offset", align=Align.INLINE)
d.entry(0xA41B)
d.comment(0xA41E, "Out of range: return zero (uninitialised)", align=Align.INLINE)
d.comment(0xA420, "Read workspace handle byte", align=Align.INLINE)
d.comment(0xA422, "Slot marked '?' (uninitialised)?", align=Align.INLINE)
d.comment(0xA424, "Has a real handle: keep it and store", align=Align.INLINE)
d.label(0xA426, "return_zero_uninit")

d.comment(0xA426, "Force result to zero (uninitialised marker)", align=Align.INLINE)
d.label(0xA428, "store_pb_result")

d.comment(0xA428, "Write into PB[0] (handle return slot)", align=Align.INLINE)
d.comment(0xA42A, "Return", align=Align.INLINE)
d.label(0xA42B, "net_3_close_handle")

d.subroutine(
    0xA42B,
    "net_3_close_handle",
    title="FS reply: close handle entry",
    description="""Calls [`get_pb_ptr_as_index`](label:get_pb_ptr_as_index) to look up the
workspace slot. On out-of-range, marks the workspace as
uninitialised. Otherwise rotates `fs_flags` bit 0 into carry (state
save), reads PB[0] (the handle to close), and proceeds with the
close path.""",
)


d.comment(0xA42B, "Convert PB pointer to workspace table offset", align=Align.INLINE)
d.entry(0xA42B)

d.comment(0xA42E, "Out of range: mark as uninitialised", align=Align.INLINE)
d.comment(0xA430, "Shift bit 0 of fs_flags into C (save state)", align=Align.INLINE)
d.comment(0xA433, "Read PB[0] (the handle to close)", align=Align.INLINE)
d.comment(0xA435, "Shift bit 7 of A into C", align=Align.INLINE)
d.comment(0xA436, "Restore C into bit 0 of fs_flags", align=Align.INLINE)
d.comment(0xA439, "Return; the close action is dispatched elsewhere based on the saved C state", align=Align.INLINE)
d.label(0xA43A, "mark_ws_uninit")

d.comment(0xA43A, "Save bit 0 of econet_flags", align=Align.INLINE)
d.comment(0xA43D, "A='?': uninitialised marker", align=Align.INLINE)
d.comment(0xA43F, "Write '?' to workspace[Y] (the slot is now free)", align=Align.INLINE)
d.comment(0xA441, "Restore bit 0 of econet_flags", align=Align.INLINE)
d.comment(0xA444, "Return", align=Align.INLINE)
d.label(0xA445, "fscv_3_star_cmd")

d.subroutine(
    0xA445,
    "fscv_3_star_cmd",
    title="FSCV reason 3: process *<command> via FS",
    description="""Sets up text and transfer pointers via set_text_and_xfer_ptr, marks
spool / Tube state as inactive (fs_spool_handle = need_release_tube
= &FF), then calls match_fs_cmd with X=&35, Y=0 to look up the user's
text in the FS command table. The match-or-error result feeds into
the FS dispatch chain that follows. Single caller (the FSCV vector
table at &8CFA).""",
)


d.comment(0xA445, "Set text/transfer pointers from FS context", align=Align.INLINE)
d.entry(0xA445)
d.comment(0xA448, "Y=&FF -- mark spool/Tube state inactive", align=Align.INLINE)
d.comment(0xA44A, "Store fs_spool_handle = &FF", align=Align.INLINE)
d.comment(0xA44C, "Store need_release_tube = &FF", align=Align.INLINE)
d.comment(0xA44F, "X=&35: NFS-commands sub-table offset", align=Align.INLINE)
d.comment(0xA451, "Match against the NFS sub-table", align=Align.INLINE)
d.comment(0xA454, "C set: no match -> dispatch via fall-through", align=Align.INLINE)
d.label(0xA456, "cmd_fs_reentry")

d.subroutine(
    0xA456,
    "cmd_fs_reentry",
    title="FS-command re-entry guard (BVC dispatch_fs_cmd)",
    description="""Single-instruction prologue: BVC dispatch_fs_cmd. Reached as the
fall-through target after a *RUN failure -- if V is clear (the
re-entry path is permitted) it branches into dispatch_fs_cmd to
re-attempt the command; otherwise falls through to error_syntax to
raise 'Syntax'. Single caller (the FS dispatch table at &8C4E).""",
)


d.comment(0xA456, "V clear: re-enter dispatch_fs_cmd", align=Align.INLINE)
d.label(0xA458, "error_syntax")

d.comment(0xA458, "Error code &DC", align=Align.INLINE)
d.comment(0xA45A, "Raise 'Syntax' error", align=Align.INLINE)
d.label(0xA464, "dispatch_fs_cmd")

d.comment(0xA464, "A=0: clear svc_state", align=Align.INLINE)
d.comment(0xA466, "Store -> svc_state", align=Align.INLINE)
d.comment(0xA468, "Load dispatch hi byte from cmd_dispatch_hi_table+X", align=Align.INLINE)
d.comment(0xA46B, "Push hi for RTS dispatch", align=Align.INLINE)
d.comment(0xA46C, "Load dispatch lo byte from cmd_dispatch_lo_table+X", align=Align.INLINE)
d.comment(0xA46F, "Push lo for RTS dispatch", align=Align.INLINE)
d.comment(0xA470, "RTS -> dispatched command handler", align=Align.INLINE)
d.label(0xA471, "match_fs_cmd")

d.subroutine(
    0xA471,
    "match_fs_cmd",
    title="Match command name against FS command table",
    description="""Case-insensitive compare of the command line against
`cmd_table_fs` entries with bit-7-terminated names. Returns with
the matched entry address on success.""",
    on_entry={
        "x": "starting offset within cmd_table_fs (selects which sub-table is searched: NFS commands, FS commands, etc.)"
    },
    on_exit={
        "x": "byte offset just past the matched command name in cmd_table_fs (or end-of-table if no match)",
        "y": "command-line offset of the first non-name character (typically the argument start)",
        "z flag": "set on match, clear on no-match",
    },
)


d.comment(0xA471, "Save command-line offset Y on stack", align=Align.INLINE)
d.comment(0xA472, "Push for save/restore", align=Align.INLINE)
d.label(0xA473, "restart_table_scan")

d.comment(0xA473, "Reload saved Y (peek without popping)", align=Align.INLINE)
d.comment(0xA474, "Push it back to keep on stack", align=Align.INLINE)
d.comment(0xA475, "Y = saved command-line offset", align=Align.INLINE)
d.comment(0xA476, "First char of current entry name", align=Align.INLINE)
d.comment(0xA479, "Bit 7 set already: end of table", align=Align.INLINE)
d.label(0xA47B, "loop_match_char")

d.comment(0xA47B, "Next char from table", align=Align.INLINE)
d.comment(0xA47E, "Bit 7 set: name fully matched", align=Align.INLINE)
d.comment(0xA482, "Mask off case bit (5)", align=Align.INLINE)
d.comment(0xA484, "Mismatch (after case mask): skip entry", align=Align.INLINE)
d.comment(0xA486, "Advance command-line offset", align=Align.INLINE)
d.comment(0xA487, "Advance table offset", align=Align.INLINE)
d.comment(0xA488, "ALWAYS branch: continue matching", align=Align.INLINE)
d.label(0xA48A, "skip_entry_chars")

d.comment(0xA48A, "Skip remaining name chars", align=Align.INLINE)
d.comment(0xA48B, "Load next table byte", align=Align.INLINE)
d.comment(0xA48E, "Bit 7 clear: continue skipping", align=Align.INLINE)
d.comment(0xA490, "Char on command line at current Y", align=Align.INLINE)
d.comment(0xA492, "Is it `.` (abbreviation)?", align=Align.INLINE)
d.comment(0xA494, "Yes: accept abbreviated match", align=Align.INLINE)
d.label(0xA496, "loop_skip_to_next")

d.comment(0xA496, "Skip 3-byte handler trailer (flag, lo, hi)", align=Align.INLINE)
d.comment(0xA497, "(continued)", align=Align.INLINE)
d.comment(0xA498, "(continued)", align=Align.INLINE)
d.comment(0xA499, "ALWAYS branch: try next entry", align=Align.INLINE)
d.label(0xA49B, "check_separator")

d.comment(0xA49B, "Save matched-name length on stack", align=Align.INLINE)
d.comment(0xA49C, "Push for stack-based comparison", align=Align.INLINE)
d.comment(0xA49D, "Char on command line just past name", align=Align.INLINE)
d.comment(0xA49F, "Y=9: separator-table size - 1", align=Align.INLINE)
d.label(0xA4A1, "loop_check_sep_table")

d.comment(0xA4A1, "Compare with separator", align=Align.INLINE)
d.comment(0xA4A4, "Match: valid command boundary", align=Align.INLINE)
d.comment(0xA4A6, "Try next separator", align=Align.INLINE)
d.comment(0xA4A7, "Loop through 10 separators", align=Align.INLINE)
d.comment(0xA4A9, "Restore matched-name length", align=Align.INLINE)
d.comment(0xA4AA, "A = matched offset, save in Y", align=Align.INLINE)
d.comment(0xA4AB, "ALWAYS branch: try next entry", align=Align.INLINE)
d.label(0xA4AD, "sep_table_data")

d.comment(0xA4AD, "Dispatch helper (sep_table_data path)", align=Align.INLINE)
d.comment(0xA4B0, "Check separator flag (zp_0026)", align=Align.INLINE)
d.comment(0xA4B4, "Effective unconditional jump", align=Align.INLINE)
d.comment(0xA4B5, "CR (carriage return)", align=Align.INLINE)
d.label(0xA4B6, "separator_char_table")

d.comment(0xA4B6, "Restore matched-name length", align=Align.INLINE)
d.comment(0xA4B7, "Y = matched-name length", align=Align.INLINE)
d.label(0xA4B8, "loop_skip_trail_spaces")

d.subroutine(
    0xA4B8,
    "loop_skip_trail_spaces",
    title="Skip trailing spaces from FS command-line args",
    description="""Reads (fs_crc_lo),Y; on space, falls through to the per-char
advance; non-space exits to check_cmd_flags. Shared body with
skip_dot_and_spaces at &A4AA (alt-entry that also accepts dots).
Single caller (the BNE retry at &A4A9).""",
    on_entry={"y": "current command-line offset"},
)


d.comment(0xA4B8, "Char on command line at current Y", align=Align.INLINE)
d.comment(0xA4BA, "Is it space?", align=Align.INLINE)
d.comment(0xA4BC, "No: check the entry's no-arg flag", align=Align.INLINE)
d.label(0xA4BE, "skip_dot_and_spaces")

d.comment(0xA4BE, "Advance past the space (or `.`)", align=Align.INLINE)
d.comment(0xA4BF, "Loop: keep skipping", align=Align.INLINE)
d.label(0xA4C2, "check_cmd_flags")

d.comment(0xA4C2, "Load entry's flag byte (post-name)", align=Align.INLINE)
d.comment(0xA4C5, "Shift bit 7 into C: the no-arg bit", align=Align.INLINE)
d.comment(0xA4C6, "C=0: entry allows arguments", align=Align.INLINE)
d.comment(0xA4C8, "Char on command line", align=Align.INLINE)
d.comment(0xA4CA, "Is it CR (no argument)?", align=Align.INLINE)
d.comment(0xA4CC, "Argument present, V clear", align=Align.INLINE)
d.comment(0xA4CE, "Force V=1: entry validated as match", align=Align.INLINE)
d.comment(0xA4D1, "V set: skip the CLV", align=Align.INLINE)
d.label(0xA4D3, "clear_v_flag")

d.comment(0xA4D3, "Clear V (no-arg flag not asserted)", align=Align.INLINE)
d.label(0xA4D4, "clear_c_flag")

d.comment(0xA4D4, "Clear C (no error / no-arg path)", align=Align.INLINE)
d.label(0xA4D5, "return_with_result")

d.comment(0xA4D5, "Discard saved Y on stack", align=Align.INLINE)
d.comment(0xA4D6, "A = current command-line char", align=Align.INLINE)
d.comment(0xA4D8, "Return (Z=1 on match, C and V set per result)", align=Align.INLINE)
d.label(0xA4D9, "loop_scan_past_word")

d.comment(0xA4D9, "Advance command-line offset", align=Align.INLINE)
d.label(0xA4DA, "check_char_type")

d.comment(0xA4DA, "Char on command line", align=Align.INLINE)
d.comment(0xA4DC, "Is it CR (end of input)?", align=Align.INLINE)
d.comment(0xA4DE, "Yes: set C and return (no match)", align=Align.INLINE)
d.comment(0xA4E0, "Is it `.`?", align=Align.INLINE)
d.comment(0xA4E2, "Yes: skip separator spaces", align=Align.INLINE)
d.comment(0xA4E4, "Is it space?", align=Align.INLINE)
d.comment(0xA4E6, "No: keep scanning past word", align=Align.INLINE)
d.label(0xA4E8, "skip_sep_spaces")

d.comment(0xA4E8, "Advance past space", align=Align.INLINE)
d.comment(0xA4E9, "Load next char", align=Align.INLINE)
d.comment(0xA4EB, "Still space?", align=Align.INLINE)
d.comment(0xA4ED, "Yes: keep skipping", align=Align.INLINE)
d.label(0xA4EF, "set_c_and_return")

d.comment(0xA4EF, "Set C: signal no-match return path", align=Align.INLINE)
d.comment(0xA4F0, "ALWAYS branch to common return", align=Align.INLINE)
d.comment(0xA4F2, "Test fs_flags bit 6", align=Align.INLINE)
d.label(0xA4F2, "check_urd_present")

d.comment(0xA4F5, "Bit 6 set: take fscv_2_star_run", align=Align.INLINE)
d.comment(0xA4F7, "Bit 6 clear: raise 'Bad command'", align=Align.INLINE)
d.label(0xA4FA, "fscv_2_star_run")

d.subroutine(
    0xA4FA,
    "fscv_2_star_run",
    title="FSCV reason 2: handle *RUN",
    description="""Saves the OS text pointer via
[`save_ptr_to_os_text`](label:save_ptr_to_os_text), calls
[`mask_owner_access`](label:mask_owner_access) to clear the FS-selection bit,
ORs in bit 1 (the *RUN-in-progress flag), and stores back to
[`hazel_fs_lib_flags`](label:hazel_fs_lib_flags). Falls through to the run-handling chain
that opens the file and starts execution. Reached via the FSCV
vector dispatch with reason code 2.""",
)


d.comment(0xA4FA, "Save text pointer (for GSREAD-driven parsing)", align=Align.INLINE)
d.entry(0xA4FA)
d.comment(0xA4FD, "Reset fs_lib_flags low bits to 5-bit access mask", align=Align.INLINE)
d.comment(0xA500, "Set bit 1 of A (mark *RUN-style invocation)", align=Align.INLINE)
d.comment(0xA502, "Update hazel_fs_lib_flags with the result", align=Align.INLINE)
d.subroutine(
    0xA507,
    "cmd_run_via_urd",
    title="*RUN entry for URD-prefixed argument",
    description="""Reached from cmd_fs_operation at &8E35 when the first character of
the *RUN argument is '&' (the URD = User Root Directory prefix).
Saves the OS text pointer via save_ptr_to_os_text, masks the access
bits via mask_owner_access, clears bit 1 of the result, and stores
into hazel_fs_lib_flags. Falls through to cmd_run_load_mask which calls
parse_cmd_arg_y0 to begin parsing the rest of the *RUN argument.
Single caller; never returns directly (continues into the run
flow).""",
)


d.comment(0xA507, "Save current OS text pointer", align=Align.INLINE)
d.comment(0xA50A, "Mask access bits", align=Align.INLINE)
d.comment(0xA50D, "Clear bit 1 of mask", align=Align.INLINE)
d.comment(0xA50F, "Save into fs_lib_flags", align=Align.INLINE)
d.label(0xA512, "cmd_run_load_mask")

d.comment(0xA512, "Begin parsing the *RUN argument", align=Align.INLINE)
d.label(0xA515, "open_file_for_run")

d.comment(0xA515, "X=1: TX-buffer write index for argument", align=Align.INLINE)
d.comment(0xA517, "Copy argument to TX buffer", align=Align.INLINE)
d.comment(0xA51A, "A=2: open-input mode for OSFIND", align=Align.INLINE)
d.comment(0xA51C, "Next byte down", align=Align.INLINE)
d.comment(0xA51F, "Y=&12: cmd code for *RUN", align=Align.INLINE)
d.comment(0xA521, "Send the request and wait for reply", align=Align.INLINE)
d.comment(0xA524, "Read reply status from TX[5]", align=Align.INLINE)
d.comment(0xA527, "Compare with 1 (not-found)", align=Align.INLINE)
d.comment(0xA529, "Loop until all 6 restored", align=Align.INLINE)
d.comment(0xA52B, "Return from svc_8_osword", align=Align.INLINE)
d.label(0xA52D, "loop_check_handles")

d.comment(0xA52D, "Increment handle byte", align=Align.INLINE)
d.comment(0xA530, "Load handler address low byte", align=Align.INLINE)
d.comment(0xA532, "Non-zero: handle valid, execute", align=Align.INLINE)
d.label(0xA535, "alloc_run_fcb")

d.comment(0xA535, "Decrement X (post-find adjustment)", align=Align.INLINE)
d.comment(0xA536, "Loop while X >= 0 (scan all 4 handle slots)", align=Align.INLINE)
d.comment(0xA538, "RTS dispatches to pushed handler", align=Align.INLINE)
d.comment(0xA53B, "X=1: target offset for the *RUN-channel command", align=Align.INLINE)
d.comment(0xA53D, "Store X to hazel_txcb_data (cmd byte)", align=Align.INLINE)
d.comment(0xA540, "Store X to hazel_txcb_flag (cmd flag)", align=Align.INLINE)
d.comment(0xA543, "X=2", align=Align.INLINE)
d.comment(0xA544, "Copy filename arg into TX buffer", align=Align.INLINE)
d.comment(0xA547, "Test station active flag", align=Align.INLINE)
d.comment(0xA549, "Send re-open request", align=Align.INLINE)
d.comment(0xA54C, "C set: error from save_net_tx_cb -- abort *RUN", align=Align.INLINE)
d.comment(0xA54E, "Yes: handle clock read", align=Align.INLINE)
d.label(0xA551, "done_run_dispatch")

d.comment(0xA551, "Jump to finalise and return", align=Align.INLINE)
d.label(0xA554, "try_library_path")

d.comment(0xA554, "Return", align=Align.INLINE)
d.comment(0xA557, "Y=&10: length of TXCB to save", align=Align.INLINE)
d.comment(0xA559, "Save current TX control block", align=Align.INLINE)
d.comment(0xA55B, "Load library flag byte", align=Align.INLINE)
d.comment(0xA55E, "Bit 7 set: library already tried", align=Align.INLINE)
d.comment(0xA560, "Shift bit 7 into carry", align=Align.INLINE)
d.comment(0xA562, "Store BCD seconds", align=Align.INLINE)
d.comment(0xA564, "Carry set: bad command", align=Align.INLINE)
d.comment(0xA566, "X=&FF -- start scan from end", align=Align.INLINE)
d.label(0xA568, "loop_find_name_end")

d.comment(0xA568, "Convert binary to BCD", align=Align.INLINE)
d.comment(0xA569, "Load filename byte", align=Align.INLINE)
d.comment(0xA56C, "Compare with CR (terminator)", align=Align.INLINE)
d.comment(0xA56E, "Load hours from clock workspace", align=Align.INLINE)
d.label(0xA570, "loop_shift_name_right")

d.comment(0xA570, "Shift filename right by 8 bytes", align=Align.INLINE)
d.comment(0xA573, "Store shifted byte", align=Align.INLINE)
d.comment(0xA576, "Decrement scan index", align=Align.INLINE)
d.comment(0xA577, "Clear hours high position", align=Align.INLINE)
d.comment(0xA579, "Store zero", align=Align.INLINE)
d.label(0xA57B, "loop_copy_lib_prefix")

d.comment(0xA57B, "Copy 'Library.' prefix", align=Align.INLINE)
d.comment(0xA57E, "Store prefix byte", align=Align.INLINE)
d.comment(0xA581, "Decrement scan index", align=Align.INLINE)
d.comment(0xA582, "Loop until prefix copied", align=Align.INLINE)
d.comment(0xA584, "Load library flag", align=Align.INLINE)
d.comment(0xA587, "Mark byte as 'argument'", align=Align.INLINE)
d.comment(0xA589, "Restore day+month byte", align=Align.INLINE)
d.label(0xA58C, "retry_with_library")

d.comment(0xA58C, "Retry file open with library path", align=Align.INLINE)
d.label(0xA58E, "restore_filename")

d.comment(0xA58E, "X=&FF -- restart scan from end", align=Align.INLINE)
d.label(0xA590, "loop_restore_name")

d.comment(0xA590, "Store BCD month", align=Align.INLINE)
d.comment(0xA591, "Load backup byte", align=Align.INLINE)
d.comment(0xA594, "Shift high nibble down", align=Align.INLINE)
d.comment(0xA597, "4th shift: isolate high nibble", align=Align.INLINE)
d.comment(0xA599, "No: continue restoring", align=Align.INLINE)
d.comment(0xA59B, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xA59E, "Mark caller's flags", align=Align.INLINE)
d.comment(0xA5A0, "Copy 7 bytes (Y=6 down to 0)", align=Align.INLINE)
d.label(0xA5A5, "library_tried")

d.comment(0xA5A5, "Store to parameter block", align=Align.INLINE)
d.comment(0xA5A8, "Loop for all 7 bytes", align=Align.INLINE)
d.comment(0xA5AA, "Test hazel_fs_lib_flags bits 6 / 7", align=Align.INLINE)
d.comment(0xA5AD, "Either bit set: this is an invalid command path", align=Align.INLINE)
d.comment(0xA5AF, "Otherwise finalise and return", align=Align.INLINE)
d.comment(0xA5B2, "A=&0B: FSCV reason 11 (filing-system change)", align=Align.INLINE)
d.comment(0xA5B4, "Tail-call FSCV", align=Align.INLINE)
d.subroutine(
    0xA5B7,
    "error_bad_command",
    title="Raise 'Bad command' BRK error",
    description="""Loads error code &FE and tail-calls error_bad_inline with the inline
string 'command' -- error_bad_inline prepends 'Bad ' to produce the
final 'Bad command' message. Used by the FS command parser when no
table entry matches the user's input. Never returns.""",
)


d.comment(0xA5B7, "Error code &FE", align=Align.INLINE)
d.comment(0xA5B9, "Raise 'Bad command' error", align=Align.INLINE)
d.label(0xA5C4, "check_exec_addr")

d.subroutine(
    0xA5C4,
    "check_exec_addr",
    title="Validate exec address is non-zero",
    description="""Iterates X = 3..0 over the 4-byte exec-address copy at hazel_txcb_flag..hazel_exec_addr,
incrementing each byte. If any byte becomes non-zero (BNE),
branches forward to library_path_string (the OSCLI dispatch path). When all four
INC operations leave a zero result the address was &FFFFFFFF + 1 =
0 -- not a valid exec address -- and the routine falls through to
the no-exec-address handler. Single caller (&A530 in the *RUN
handler).""",
    on_entry={"a": "exec address bytes already in hazel_txcb_flag..hazel_exec_addr"},
    on_exit={"x": "0 if no valid exec; non-zero branch otherwise"},
)


d.comment(0xA5C4, "X=3: check 4 execution bytes", align=Align.INLINE)
d.label(0xA5C6, "loop_check_exec_bytes")

d.comment(0xA5C6, "Increment execution address byte", align=Align.INLINE)
d.comment(0xA5C9, "Low byte = &6F", align=Align.INLINE)
d.comment(0xA5CB, "Set osword_flag", align=Align.INLINE)
d.comment(0xA5CC, "Loop until all checked", align=Align.INLINE)
d.comment(0xA5CE, "A=&93: error code 'Bad command'", align=Align.INLINE)
d.comment(0xA5D0, "Generate 'No!' error", align=Align.INLINE)
d.label(0xA5D9, "alloc_run_channel")

d.subroutine(
    0xA5D9,
    "alloc_run_channel",
    title="Allocate FCB slot for *RUN target file",
    description="""Loads the saved OSWORD parameter byte at hazel_txcb_data, calls alloc_fcb_slot
to obtain a free channel index in A, transfers it into Y, then
clears the per-channel attribute byte at hazel_fcb_status,X. Used by the
*RUN argument-handling path at &A54C once the file is opened, to
reserve a channel for the running program.""",
    on_exit={"a": "channel attribute byte (cleared to 0)", "x": "FCB slot index", "y": "FCB slot index (copy of X)"},
)


d.comment(0xA5D9, "Set workspace pointer high", align=Align.INLINE)
d.comment(0xA5DC, "Allocate FCB slot", align=Align.INLINE)
d.comment(0xA5DF, "A = parsed character", align=Align.INLINE)
d.comment(0xA5E0, "Y=OSWORD flag (slot specifier)", align=Align.INLINE)
d.comment(0xA5E2, "Clear status in channel table", align=Align.INLINE)
d.comment(0xA5E5, "A=3: start searching from slot 3", align=Align.INLINE)
d.comment(0xA5E8, "Y=3: skip past 3-byte FS header", align=Align.INLINE)
d.comment(0xA5EA, "C set: slot invalid, store result", align=Align.INLINE)
d.index_base(0xA5ED, "library_dir_prefix")

d.comment(0xA5ED, "Continue shift", align=Align.INLINE)
# UNMAPPED: d.label(0xA5DF, "library_path_string")

# UNMAPPED: d.comment(0xA5DF, "Copy parsed arg to TX buffer with X=0", align=Align.INLINE)
d.comment(0xA5F8, "Y=0", align=Align.INLINE)
d.comment(0xA5FA, "For the loop entry", align=Align.INLINE)
d.comment(0xA5FB, "Transfer found slot to A", align=Align.INLINE)
d.label(0xA5FE, "loop_read_gs_string")

d.comment(0xA5FE, "Store slot number to PB byte 0", align=Align.INLINE)
d.comment(0xA601, "Always (BCC after CLC) loop back", align=Align.INLINE)
d.comment(0xA603, "C set: slot invalid, store result", align=Align.INLINE)
d.label(0xA604, "loop_skip_trailing")

d.comment(0xA604, "Advance Y past trailing space", align=Align.INLINE)
d.comment(0xA605, "Y=Y-1: adjust workspace offset", align=Align.INLINE)
d.comment(0xA607, "Is it space?", align=Align.INLINE)
d.comment(0xA609, "Yes: skip it", align=Align.INLINE)
d.comment(0xA60B, "Test for CR (terminator)", align=Align.INLINE)
d.comment(0xA60D, "Clear C for arithmetic", align=Align.INLINE)
d.comment(0xA60E, "Compare Y with OSWORD flag", align=Align.INLINE)
d.comment(0xA60F, "Add to text pointer low", align=Align.INLINE)
d.comment(
    0xA611, "Store low byte of (os_text_ptr + Y) -> fs_crc_lo (repurposed as a generic pointer)", align=Align.INLINE
)
d.comment(0xA613, "Load os_text_ptr_hi for the high-byte add", align=Align.INLINE)
d.comment(0xA615, "Add carry from low add (no extra increment)", align=Align.INLINE)
d.comment(0xA617, "Store result high byte -> fs_crc_hi", align=Align.INLINE)
d.comment(0xA619, "Save text pointer for later", align=Align.INLINE)
d.comment(0xA61C, "X=&C0: pointer-to-options high byte", align=Align.INLINE)
d.comment(0xA61E, "Y=1: workspace flag offset", align=Align.INLINE)
d.comment(0xA620, "Store pending marker to workspace", align=Align.INLINE)
d.comment(0xA622, "Store as fs_options", align=Align.INLINE)
d.comment(0xA624, "Increment retry counter", align=Align.INLINE)
d.comment(0xA627, "X=&4A: FS command table offset", align=Align.INLINE)
d.comment(0xA629, "Store result A to PB via Y", align=Align.INLINE)
d.comment(0xA62B, "Rotate Econet flags back (restore state)", align=Align.INLINE)
d.comment(0xA62E, "Return from OSWORD 11 handler", align=Align.INLINE)
d.comment(0xA631, "Store to ws_ptr_lo", align=Align.INLINE)
d.comment(0xA633, "Y=&7F: last byte of RX buffer", align=Align.INLINE)
d.comment(0xA639, "All &FF?", align=Align.INLINE)
d.comment(0xA63B, "X-1: adjust count", align=Align.INLINE)
d.comment(0xA63D, "Claim tube for data transfer", align=Align.INLINE)
d.comment(0xA640, "X=9: parameter count", align=Align.INLINE)
d.comment(0xA642, "Y=&C1: high byte of TX buffer pointer", align=Align.INLINE)
d.comment(0xA644, "A=4: option byte for *RUN", align=Align.INLINE)
d.comment(0xA646, "Relocated execute path", align=Align.INLINE)
d.label(0xA649, "dispatch_via_vector")

d.comment(0xA649, "A=1: dispatch flag", align=Align.INLINE)
d.comment(0xA64B, "Indirect jump via workspace vector", align=Align.INLINE)
d.label(0xA64E, "fsreply_3_set_csd")

d.subroutine(
    0xA64E,
    "fsreply_3_set_csd",
    title="FS reply handler: select CSD station",
    description="""Single-instruction wrapper: JSR find_station_bit3 to record the
new current-selected-directory (CSD) station in the table, then
JMP return_with_last_flag to clean up and return. Single caller
(the FS reply dispatch at &959B).""",
    on_exit={"a": "fs_last_byte_flag (loaded by return_with_last_flag)"},
)


d.comment(0xA64E, "Find station-bit-3 entry", align=Align.INLINE)
d.entry(0xA64E)
d.label(0xA654, "fsreply_5_set_lib")

d.subroutine(
    0xA654,
    "fsreply_5_set_lib",
    title="FS reply handler: set library station",
    description="""Two-instruction wrapper: `JSR
`[`flip_set_station_boot`](label:flip_set_station_boot) to record the new library
station, then `JMP`
[`return_with_last_flag`](label:return_with_last_flag). Reached only via the FS
reply dispatch table.""",
)


d.comment(0xA654, "Record library station in station table", align=Align.INLINE)
d.entry(0xA654)
d.label(0xA65A, "find_station_bit2")

d.subroutine(
    0xA65A,
    "find_station_bit2",
    title="Find printer server station in table (bit 2)",
    description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 2 set (printer server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""",
    on_exit={
        "v flag": "set if matching slot already had bit 2; clear if newly allocated",
        "x": "table slot index of the matched/allocated entry",
    },
)


d.comment(0xA65A, "X=&10: scan 16 entries", align=Align.INLINE)
d.comment(0xA65C, "Clear V (no-match marker)", align=Align.INLINE)
d.label(0xA65D, "loop_search_stn_bit2")

d.comment(0xA65D, "Step to previous entry", align=Align.INLINE)
d.comment(0xA65E, "Below 0: scan complete", align=Align.INLINE)
d.comment(0xA660, "Compare entry X's stn/net with caller's", align=Align.INLINE)
d.comment(0xA663, "No match: continue", align=Align.INLINE)
d.comment(0xA665, "Match: read entry's flag byte at hazel_fcb_status+X", align=Align.INLINE)
d.comment(0xA668, "Mask bit 2", align=Align.INLINE)
d.comment(0xA66A, "Bit 2 clear: keep scanning", align=Align.INLINE)
d.comment(0xA66C, "Bit 2 set: A = matched entry index (Y)", align=Align.INLINE)
d.comment(0xA66D, "Store Y at hazel_fcb_slot_attr+X (link entry to slot)", align=Align.INLINE)
d.comment(0xA670, "BIT always_set_v_byte: V <- 1 (match found)", align=Align.INLINE)
d.label(0xA673, "done_search_bit2")

d.comment(0xA673, "Save Y at hazel_fs_saved_station (matched entry index)", align=Align.INLINE)
d.comment(0xA676, "V set: skip new-slot alloc", align=Align.INLINE)
d.comment(0xA678, "A = caller's index", align=Align.INLINE)
d.comment(0xA679, "Allocate a fresh FCB slot", align=Align.INLINE)
d.comment(0xA67C, "Save FCB slot index at hazel_fcb_slot_1", align=Align.INLINE)
d.comment(0xA67F, "Z set: alloc failed -> restore FS context", align=Align.INLINE)
d.label(0xA681, "set_flags_bit2")

d.comment(0xA681, "A=&26: workspace flag for bit 2 search", align=Align.INLINE)
d.label(0xA685, "find_station_bit3")

d.subroutine(
    0xA685,
    "find_station_bit3",
    title="Find file server station in table (bit 3)",
    description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 3 set (file server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""",
    on_exit={
        "v flag": "set if matching slot already had bit 3; clear if newly allocated",
        "x": "table slot index of the matched/allocated entry",
    },
)


d.comment(0xA685, "X=&10: scan 16 entries", align=Align.INLINE)
d.comment(0xA687, "Clear V (no-match marker)", align=Align.INLINE)
d.label(0xA688, "loop_search_stn_bit3")

d.comment(0xA688, "Step to previous entry", align=Align.INLINE)
d.comment(0xA689, "Below 0: scan complete", align=Align.INLINE)
d.comment(0xA68B, "Compare entry's stn/net with caller's", align=Align.INLINE)
d.comment(0xA68E, "No match: continue", align=Align.INLINE)
d.comment(0xA690, "Match: read entry's flag byte at hazel_fcb_status+X", align=Align.INLINE)
d.comment(0xA693, "Mask bit 3", align=Align.INLINE)
d.comment(0xA695, "Bit 3 clear: keep scanning", align=Align.INLINE)
d.comment(0xA697, "Bit 3 set: A = matched entry index (Y)", align=Align.INLINE)
d.comment(0xA698, "Store Y at hazel_fcb_slot_attr+X (link entry to slot)", align=Align.INLINE)
d.comment(0xA69B, "BIT always_set_v_byte: V <- 1 (match found)", align=Align.INLINE)
d.label(0xA69E, "done_search_bit3")

d.comment(0xA69E, "Save Y at hazel_fs_context_copy (matched entry index)", align=Align.INLINE)
d.comment(0xA6A1, "V set: skip new-slot alloc", align=Align.INLINE)
d.comment(0xA6A3, "A = caller's index", align=Align.INLINE)
d.comment(0xA6A4, "Allocate a fresh FCB slot", align=Align.INLINE)
d.comment(0xA6A7, "Save FCB slot index at hazel_fcb_slot_2", align=Align.INLINE)
d.comment(0xA6AA, "Z set: alloc failed -> restore FS context", align=Align.INLINE)
d.label(0xA6AC, "set_flags_bit3")

d.comment(0xA6AC, "A=&2A: workspace flag for bit 3 search", align=Align.INLINE)
d.entry(0xA6B0)
d.label(0xA6B0, "cmd_flip")

d.subroutine(
    0xA6B0,
    "cmd_flip",
    title="*Flip command handler",
    description="""Exchanges the CSD and CSL (library) handles. Saves the current
CSD handle from [`hazel_fs_context_copy`](label:hazel_fs_context_copy), loads
the library handle from [`hazel_fs_prefix_stn`](label:hazel_fs_prefix_stn)
into Y, and calls [`find_station_bit3`](label:find_station_bit3) to install
it as the new CSD. Restores the original CSD handle and falls
through to [`flip_set_station_boot`](label:flip_set_station_boot) to install
it as the new library. Useful when files to be LOADed are in
the library and *DIR/*LIB would be inconvenient.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xA6B0, "Load current CSD handle", align=Align.INLINE)
d.comment(0xA6B3, "Save CSD handle", align=Align.INLINE)
d.comment(0xA6B4, "Load library handle into Y", align=Align.INLINE)
d.comment(0xA6B7, "Install library as new CSD", align=Align.INLINE)
d.comment(0xA6BA, "Restore original CSD handle", align=Align.INLINE)
d.comment(0xA6BB, "Y = original CSD (becomes library)", align=Align.INLINE)
d.label(0xA6BC, "flip_set_station_boot")

d.subroutine(
    0xA6BC,
    "flip_set_station_boot",
    title="Set boot option for a station in the table",
    description="""Scans up to 16 station table entries for one
matching the current address with bit 4 set
(boot-eligible). Stores the requested boot type
in the matching entry and calls
restore_fs_context to re-establish the filing
system state.""",
    on_entry={"a": "boot type code to store"},
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xA6BC, "X=&10: max 16 station entries", align=Align.INLINE)
d.comment(0xA6BE, "Clear V (no match found yet)", align=Align.INLINE)
d.label(0xA6BF, "loop_search_stn_boot")

d.comment(0xA6BF, "Decrement station index", align=Align.INLINE)
d.comment(0xA6C0, "All searched: exit loop", align=Align.INLINE)
d.comment(0xA6C2, "Check if station[X] matches", align=Align.INLINE)
d.comment(0xA6C5, "No match: try next station", align=Align.INLINE)
d.comment(0xA6C7, "Load station flags byte", align=Align.INLINE)
d.comment(0xA6CA, "Test bit 4 (active flag)", align=Align.INLINE)
d.comment(0xA6CC, "Not active: try next station", align=Align.INLINE)
d.comment(0xA6CE, "Transfer boot type to A", align=Align.INLINE)
d.comment(0xA6CF, "Store boot setting for station", align=Align.INLINE)
d.comment(0xA6D2, "Set V flag (station match found)", align=Align.INLINE)
d.label(0xA6D5, "done_search_boot")

d.comment(0xA6D5, "Store boot type", align=Align.INLINE)
d.comment(0xA6D8, "V set (matched): skip allocation", align=Align.INLINE)
d.comment(0xA6DA, "Boot type to A", align=Align.INLINE)
d.comment(0xA6DB, "Allocate FCB slot for new entry", align=Align.INLINE)
d.comment(0xA6DE, "Store allocation result", align=Align.INLINE)
d.comment(0xA6E1, "Zero: allocation failed, exit", align=Align.INLINE)
d.label(0xA6E3, "set_flags_boot")

d.comment(0xA6E3, "A=&32: station flags (active+boot)", align=Align.INLINE)
d.label(0xA6E5, "store_stn_flags_restore")

d.comment(0xA6E5, "Store station flags", align=Align.INLINE)
d.label(0xA6E8, "jmp_restore_fs_ctx")

d.comment(0xA6E8, "Restore FS context and return", align=Align.INLINE)
d.label(0xA6EB, "fsreply_1_boot")

d.subroutine(
    0xA6EB,
    "fsreply_1_boot",
    title="FS reply 1: flag boot pending, then fall into handle-copy",
    description="""Closes all network channels via
[`close_all_net_chans`](label:close_all_net_chans), sets bit 6 of `fs_flags`
(`TSB &0D6C`, marking the boot-pending state), `SEC`s to signal
boot-pending downstream, loads the boot-type byte from the FS
reply ([`hazel_txcb_result`](label:hazel_txcb_result)) into
[`hazel_fs_flags`](label:hazel_fs_flags), pushes it on the stack, and
falls through into [`fsreply_2_copy_handles`](label:fsreply_2_copy_handles).

The pushed byte is **not** consumed by `fsreply_2_copy_handles`
itself — that routine only copies the per-handle table and uses
`PHP`/`PLP` for its own Carry handling. The matching `PLA` lives
much further down the boot chain, in
[`boot_persist_fs_maybe`](label:boot_persist_fs_maybe) at `&A732`, which
tests the recovered boot-type byte against `2` to decide whether
to call OSBYTE `&6D`. Anyone following the stack across this
fall-through should look past `fsreply_2_copy_handles` and
`boot_try_findlib` to find the pop.""",
)


d.entry(0xA6EB)
d.comment(0xA6EB, "Close all network channels", align=Align.INLINE)
d.comment(0xA6EE, "A=&40: bit-6 mask for fs_flags (boot-pending flag)", align=Align.INLINE)
d.comment(0xA6F0, "Set boot-pending bit on fs_flags (TSB = test-and-set)", align=Align.INLINE)
d.comment(0xA6F3, "C=1: signal boot-pending to fsreply_2_copy_handles (its BCS at &A6FB takes the boot path)", align=Align.INLINE)
d.comment(0xA6F4, "Load boot-type byte from FS reply (hazel_txcb_result)", align=Align.INLINE)
d.comment(0xA6F7, "Store boot type as hazel_fs_flags (consumed later by boot_select_cmd)", align=Align.INLINE)
d.comment(0xA6FA, "Push boot-type byte (popped later by boot_persist_fs_maybe at &A732)", align=Align.INLINE)
d.label(0xA6FB, "fsreply_2_copy_handles")

d.subroutine(
    0xA6FB,
    "fsreply_2_copy_handles",
    title="FS reply 2: install handles and (optionally) boot",
    description="""Records the file-server / printer-server / library handles from
the I-AM reply into the station table by calling
[`find_station_bit2`](label:find_station_bit2),
[`find_station_bit3`](label:find_station_bit3), and
[`flip_set_station_boot`](label:flip_set_station_boot) in turn with the three
handle bytes loaded from the TXCB reply
([`hazel_txcb_data`](label:hazel_txcb_data),
[`hazel_txcb_flag`](label:hazel_txcb_flag),
[`hazel_txcb_count`](label:hazel_txcb_count)). PHP/PLP carry a flag across
the calls: when Carry is clear on entry the routine returns via
[`return_with_last_flag`](label:return_with_last_flag); when Carry is set it
continues into the boot path at
[`boot_try_findlib`](label:boot_try_findlib), which OSCLIs
`-NET-FindLib`, then falls into
[`boot_persist_fs_maybe`](label:boot_persist_fs_maybe) (OSBYTE `&6D`
when boot type ≥ 2), clears the auto-boot flag in
[`hazel_fs_lib_flags`](label:hazel_fs_lib_flags), and (unless CTRL is held)
falls through to [`boot_select_cmd`](label:boot_select_cmd) to execute the
`!Boot` command.

Two entry contracts:

- **Direct dispatch** via the FS-reply table entry at `&2C` —
  the dispatcher arrives with Carry clear, so `BCS` at `&A6FB`
  is not taken and the routine exits via
  `JMP return_with_last_flag` without ever reaching the `PLA`
  at `&A732`. The stack contract is satisfied trivially.
- **Fall-through from [`fsreply_1_boot`](label:fsreply_1_boot)** —
  fsreply_1_boot pushes A (the boot-type byte) and `SEC`s
  before falling in, so `BCS` is taken and the boot path runs;
  the `PLA` at `&A732` then pops the boot-type byte cleanly.

Direct dispatch with Carry set is not part of the contract;
the boot path requires the pre-pushed A from fsreply_1_boot.""",
    on_entry={
        "a": "boot-type byte (pushed by fsreply_1_boot when arriving via fall-through; ignored on direct-dispatch C-clear path)",
        "carry": "set when boot processing should follow (only legal via fsreply_1_boot fall-through)",
    },
)


d.entry(0xA6FB)
d.comment(0xA6FB, "Save processor status", align=Align.INLINE)
d.comment(0xA6FC, "Load station number from reply", align=Align.INLINE)
d.comment(0xA6FF, "Find station entry with bit 2", align=Align.INLINE)
d.comment(0xA702, "Load network number from reply", align=Align.INLINE)
d.comment(0xA705, "Find station entry with bit 3", align=Align.INLINE)
d.comment(0xA708, "Load boot type from reply", align=Align.INLINE)
d.comment(0xA70B, "Set boot config for station", align=Align.INLINE)
d.comment(0xA70E, "Restore processor status", align=Align.INLINE)
d.comment(0xA70F, "Carry set: proceed with boot", align=Align.INLINE)
d.comment(0xA711, "Return with last flag", align=Align.INLINE)
d.label(0xA714, "findlib_oscli_cmd")
d.banner(
    0xA714,
    title="OSCLI command string '-NET-FindLib'<CR>",
    description="""Passed to OSCLI by [`boot_try_findlib`](label:boot_try_findlib). The
`-NET-` prefix is the MOS hyphen-bracketed FS-selector form —
see that subroutine's description for the convention and why
it's used here rather than a plain `*FindLib`.""",
)


d.subroutine(
    0xA721,
    "boot_try_findlib",
    title="If CMOS auto-CLI bit set, OSCLI '-NET-FindLib'",
    description="""Reads CMOS byte `&11` via OSBYTE `&A1` and tests bit 1
(the auto-CLI / auto-run-FindLib flag). If clear, returns
immediately; if set, OSCLIs [`findlib_oscli_cmd`](label:findlib_oscli_cmd)
(`-NET-FindLib<CR>`). Falls through to
[`boot_persist_fs_maybe`](label:boot_persist_fs_maybe) in either case.

#### Why the `-NET-` prefix

`-NET-` is MOS's hyphen-bracketed filing-system selector. The
general form `-FS-COMMAND` makes `FS` the temporary *active* FS
for this OSCLI without touching the currently-selected default,
then parses `COMMAND`. If `COMMAND` matches an internal MOS
command it runs normally; on the unknown-command fallthrough
the temp-FS bit suppresses the service-4 ROM broadcast and
dispatches via FSCV,3 directly to the selected FS. `NET` is
the short name registered by the NFS / ANFS ROM (others
register `DISC`, `ADFS`, `TAPE`).

NFS is already the current FS by the time this code runs.
[`svc_3_autoboot`](label:svc_3_autoboot) selects it via
[`select_fs_via_cmd_net_fs`](label:select_fs_via_cmd_net_fs) before the
synchronous `*I AM` exchange on the cold-boot path, and the
user-typed `*I AM` route requires `*NET` first because `*I AM`
is itself an NFS `*` command.

The prefix therefore provides defensive routing, not FS
selection. A plain `*FindLib` would broadcast service-4 to all
sideways ROMs before falling through to FSCV,3, exposing the
command to interception by any ROM that has claimed `FindLib`
(including by abbreviation). The `-NET-` form sets the temp-FS
bit, which suppresses the broadcast and dispatches via FSCV,3
directly to NFS, so the lookup deterministically hits NFS's
`*RUN`-from-library path.

The same routing is used by
[`boot_cmd_load_str`](label:boot_cmd_load_str) (`L.-NET-!Boot`) and
[`boot_cmd_exec_str`](label:boot_cmd_exec_str) (`E.-NET-!Boot`).""",
)


d.comment(0xA721, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0xA723, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0xA726, "Result to A", align=Align.INLINE)
d.comment(0xA727, "Mask bit 1 (auto-CLI flag)", align=Align.INLINE)
d.comment(0xA729, "Bit clear: skip auto-CLI", align=Align.INLINE)
# UNMAPPED: d.expr(0xA716, "<findlib_oscli_cmd")
# UNMAPPED: d.expr(0xA718, ">findlib_oscli_cmd")
d.comment(0xA72F, "OSCLI '-NET-FindLib': dispatch to NFS via FSCV,3 (bypass service-4 broadcast)", align=Align.INLINE)
d.comment(0xA732, "Pop saved A", align=Align.INLINE)
d.label(0xA732, "boot_persist_fs_maybe")

d.comment(0xA733, "Compare with 2", align=Align.INLINE)
d.comment(0xA735, "Below: skip making FS permanent", align=Align.INLINE)
d.comment(0xA737, "Boot type >= 2 (NFS-resident !Boot): A=&6D to commit NFS as default FS", align=Align.INLINE)
d.label(0xA73C, "check_auto_boot_flag")

d.subroutine(
    0xA73C,
    "check_auto_boot_flag",
    title="Test+clear bit 2 of fs_lib_flags; on CTRL, bail out",
    description="""Atomically tests and clears bit 2 of
[`hazel_fs_lib_flags`](label:hazel_fs_lib_flags) — the auto-boot flag — then
dispatches based on the test result:

- **Bit 2 was set**: skip the CTRL-key check and `BNE` straight
  into [`boot_select_cmd`](label:boot_select_cmd) to issue the boot OSCLI.
- **Bit 2 was clear**: fall through and test for the CTRL key via
  OSBYTE `&79`. CTRL held → fall into
  [`boot_cancel_rts`](label:boot_cancel_rts) (boot cancelled). CTRL not
  held → `BPL` into [`boot_select_cmd`](label:boot_select_cmd) anyway.

The body uses the classic 6502 "test bit, modify, restore test
result" idiom: load the flags, copy to X, `AND` with the bit to
isolate it, `PHP` to stash the Z flag from that test, then `TXA`
back, `AND` with the complement mask to clear the bit, store the
modified flags, `PLP` to recover the original Z. This way the
flag byte is updated unconditionally but the dispatch decision is
made on the *pre-update* state — saving a separate read-modify
sequence.""",
)


d.comment(0xA73C, "Load config flags", align=Align.INLINE)
d.comment(0xA73F, "Save copy in X", align=Align.INLINE)
d.comment(0xA740, "Test bit 2 (auto-boot flag)", align=Align.INLINE)
d.comment(0xA742, "Save bit 2 test result", align=Align.INLINE)
d.comment(0xA743, "Restore full flags", align=Align.INLINE)
d.comment(0xA744, "Clear bit 2 (consume flag)", align=Align.INLINE)
d.comment(0xA746, "Store cleared flags", align=Align.INLINE)
d.comment(0xA749, "Restore bit 2 test result", align=Align.INLINE)
d.comment(0xA74A, "Auto-boot flag was set: skip CTRL check, dispatch boot via boot_select_cmd", align=Align.INLINE)
d.comment(0xA74C, "OSBYTE &79: scan keyboard", align=Align.INLINE)
d.comment(0xA74E, "X = CTRL key scan code (negative-X INKEY form for OSBYTE &79)", align=Align.INLINE)
d.comment(0xA754, "CTRL not pressed: proceed to boot", align=Align.INLINE)
d.label(0xA756, "boot_cancel_rts")
d.label(0xA757, "boot_cmd_load_str")
d.label(0xA764, "boot_cmd_exec_str")


d.comment(0xA756, "Cancel boot, return (CTRL held, or boot type 0 via BEQ at &A764)", align=Align.INLINE)
d.comment(0xA757, "Boot cmd '*LOAD -NET-!Boot' (load !Boot via NFS, bypassing service-4 broadcast — see boot_try_findlib)", align=Align.INLINE)
d.comment(0xA763, "CR terminator", align=Align.INLINE)
d.comment(0xA764, "Boot cmd '*EXEC -NET-!Boot' (exec !Boot via NFS, bypassing service-4 broadcast — see boot_try_findlib)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA75A, "CR terminator", align=Align.INLINE)
# UNMAPPED: d.index_base(0xA75B, "boot_cmd_lo_table")

# UNMAPPED: d.banner(
# UNMAPPED:     0xA75B,
# UNMAPPED:     title="Boot-command low-byte index table",
# UNMAPPED:     description="""Four-byte table of OSCLI-pointer low bytes, indexed by `Y` in
# UNMAPPED: [`boot_cmd_oscli`](label:boot_cmd_oscli). Combined with `Y=&A7` (high
# UNMAPPED: byte, supplied by `boot_cmd_oscli` after the lookup), each entry
# UNMAPPED: yields a pointer to a CR-terminated boot command in the `&A7xx`
# UNMAPPED: page.
# UNMAPPED: 
# UNMAPPED: Three reachable entries (`Y` = 1, 2, 3); `Y=0` is unreachable
# UNMAPPED: because [`boot_select_cmd`](label:boot_select_cmd) `BEQ`s out when
# UNMAPPED: `hazel_fs_flags` is zero.
# UNMAPPED: 
# UNMAPPED: Index 2 (`&48`) lands inside
# UNMAPPED: [`boot_cmd_load_str`](label:boot_cmd_load_str) — at offset 7, on its `!`
# UNMAPPED: byte — so OSCLI reads `"!Boot<CR>"` from the middle of the same
# UNMAPPED: string used at index 1. This packs the "run `*!Boot` on the
# UNMAPPED: current FS" variant into the same data as the load-via-NFS
# UNMAPPED: form, saving a third CR-terminated string.""",
# UNMAPPED: )

# UNMAPPED: d.byte(0xA75B)
# UNMAPPED: d.byte(0xA75C)
# UNMAPPED: d.byte(0xA75D)
# UNMAPPED: d.byte(0xA75E)
# UNMAPPED: d.comment(0xA75B, "Y=0: unreachable (boot_select_cmd BEQs out when hazel_fs_flags=0); value is dead", align=Align.INLINE)
# UNMAPPED: d.expr(0xA75C, "<boot_cmd_load_str")
# UNMAPPED: d.comment(0xA75C, "Y=1: lo byte of boot_cmd_load_str (&A741) — 'L.-NET-!Boot'", align=Align.INLINE)
# UNMAPPED: d.expr(0xA75D, "<(boot_cmd_load_str + 7)")
# UNMAPPED: d.comment(0xA75D, "Y=2: lo byte of &A74A (offset 7 into boot_cmd_load_str, on '!') — '!Boot' on current FS", align=Align.INLINE)
# UNMAPPED: d.expr(0xA75E, "<boot_cmd_exec_str")
# UNMAPPED: d.comment(0xA75E, "Y=3: lo byte of boot_cmd_exec_str (&A74E) — 'E.-NET-!Boot'", align=Align.INLINE)
d.label(0xA775, "boot_select_cmd")

d.subroutine(
    0xA775,
    "boot_select_cmd",
    title="Branch to boot_cancel_rts on boot type 0, else fall into boot_cmd_oscli",
    description="""Two-instruction gate at the head of the boot-OSCLI dispatch.
Loads `Y` from [`hazel_fs_flags`](label:hazel_fs_flags) (the boot-type
byte the FS reply stashed in fsreply_1_boot at `&A6E1`); if zero,
`BEQ`s into [`boot_cancel_rts`](label:boot_cancel_rts) — the empty / no-op
boot case. Otherwise falls through into
[`boot_cmd_oscli`](label:boot_cmd_oscli) with `Y` already loaded as the
index into [`boot_cmd_lo_table`](label:boot_cmd_lo_table).

Two callers, both from [`check_auto_boot_flag`](label:check_auto_boot_flag):
the `BNE` at `&A74A` (auto-boot flag was set, skip CTRL check)
and the `BPL` at `&A740` (CTRL not pressed, proceed to boot).""",
)


d.comment(0xA775, "Y = boot-type byte from FS reply (0..3)", align=Align.INLINE)
d.comment(0xA778, "Z (boot type 0): cancel boot via boot_cancel_rts", align=Align.INLINE)
d.label(0xA77A, "boot_cmd_oscli")

d.subroutine(
    0xA77A,
    "boot_cmd_oscli",
    title="Look up boot command in boot_cmd_lo_table and OSCLI it",
    description="""Loads `X = boot_cmd_lo_table,Y` (low byte of the boot-command
address), sets `Y=&A7` (high byte — boot strings live in `&A7xx`),
then `JMP`s to `oscli` with `(X,Y)` pointing at a CR-terminated
command string.

Two entry paths:

- `JMP` tail-call from `&A5E8` with `Y=3` hardcoded — forces the
  exec-via-NFS boot ([`boot_cmd_exec_str`](label:boot_cmd_exec_str)).
- Fall-through from [`boot_select_cmd`](label:boot_select_cmd) with `Y` already
  loaded from [`hazel_fs_flags`](label:hazel_fs_flags) — the normal logon-boot
  path, dispatching on the FS-supplied boot type.""",
    on_entry={"y": "boot-command index (1=load, 2=run-on-current-FS, 3=exec)"},
)


d.comment(0xA77A, "Load boot-command low byte from boot_cmd_lo_table[Y]", align=Align.INLINE)
d.comment(0xA77D, "Y=&A7: high byte (boot strings live in &A7xx)", align=Align.INLINE)
d.comment(0xA77F, "Tail-jump to OSCLI to execute the boot command", align=Align.INLINE)
d.index_base(0xA782, "cmd_table_fs")
d.banner(
    0xA782,
    title="ANFS *command dispatch tables (5 concatenated sub-tables)",
    description="""See the comment block immediately above the
[`cmd_table_fs`](label:cmd_table_fs) declaration in the driver for the
sub-table layout, walker contract, and flag-byte encoding. Each
entry's two-byte dispatch word stores `target-1`; PHA/PHA/RTS
arrives at `target`. Per-entry inline comments below name the
command, syntax-template index, and dispatch target.""",
)
for name_addr, name, flag_addr, flag_byte, lo_addr, target_label, role in _cmd_table_fs_entries:
    name_len = flag_addr - name_addr
    if name_len > 1:
        d.string(name_addr, name_len)
    else:
        d.byte(name_addr)
    d.byte(flag_addr)
    d.word(lo_addr)
    if target_label is not None:
        d.expr(lo_addr, sym(target_label) - 1)
    d.comment(name_addr, role, align=Align.INLINE)
    syn_idx = flag_byte & 0x001F
    flag_parts = ["no syn"] if syn_idx == 0 else ["syn &%X" % syn_idx]
    if flag_byte & 0x0040:
        flag_parts.append("V if no arg")
    d.comment(flag_addr, ", ".join(flag_parts), align=Align.INLINE)
d.label(0xA783, "cmd_dispatch_lo_table")

d.label(0xA784, "cmd_dispatch_hi_table")

d.byte(0xA7B5)
d.comment(0xA7B5, "Sub-table 1 end (walker reads &80 -> stop)", align=Align.INLINE)
d.byte(0xA7B6)
d.comment(0xA7B6, "Padding (alignment before sub-table 2)", align=Align.INLINE)
d.label(0xA7B7, "cmd_table_nfs")

d.index_base(0xA7DF, "cmd_table_nfs_iam")

# UNMAPPED: d.byte(0xA7FA)
# UNMAPPED: d.comment(0xA7FA, "Sub-table 2 end (walker reads &80 -> stop)", align=Align.INLINE)
# UNMAPPED: d.byte(0xA7FB)
# UNMAPPED: d.comment(0xA7FB, "Padding -- &2C 8E happens to spell &8E2D = check_urd_prefix but is never read", align=Align.INLINE)
# UNMAPPED: d.byte(0xA7FC)
# UNMAPPED: d.comment(0xA7FC, "Padding (continued)", align=Align.INLINE)
# UNMAPPED: d.label(0xA7FD, "cmd_table_help_topics")

d.byte(0xA826)
d.comment(0xA826, "Sub-table 3 end (walker reads &80 -> stop)", align=Align.INLINE)
d.label(0xA827, "cmd_table_syntax_help")
d.byte(0xA843)
d.comment(0xA843, "Sub-tables 4/5 separator", align=Align.INLINE)

d.comment(0xA856, "BRA osword_store_svc_state -- skip past 22-byte caller-cleanup frame", align=Align.INLINE)
d.entry(0xA856)


d.subroutine(
    0xA856,
    "svc_8_osword",
    title="Service 8: unrecognised OSWORD",
    description="""Handles MOS service call 8 (unrecognised OSWORD).
Filters OSWORD codes &0E-&14 by subtracting &0E (via
CLC/SBC &0D) and rejecting values outside 0-6. For
valid codes, calls osword_setup_handler to push the
dispatch address, then copies 3 bytes from the RX
buffer to osword_flag workspace.""",
    on_entry={"a": "OSWORD number (from osbyte_a_copy)", "y": "parameter passed by service-call dispatch"},
)


d.label(0xA857, "svc_8_osword_disp")

d.comment(0xA857, "CLC so SBC subtracts value+1", align=Align.INLINE)
d.comment(0xA858, "OSWORD setup state (13 bytes -- constants and offsets used by svc_8_osword)", align=Align.INLINE)
d.comment(0xA85A, "A = OSWORD - &0E (CLC+SBC = -&0E)", align=Align.INLINE)
d.comment(0xA85C, "Below &0E: not ours, return", align=Align.INLINE)
d.comment(0xA85E, "Index >= 7? (OSWORD > &14)", align=Align.INLINE)
d.comment(0xA860, "Above &14: not ours, return", align=Align.INLINE)
d.comment(0xA862, "X=OSWORD handler index (0-6)", align=Align.INLINE)
d.comment(0xA863, "Y=6: save 6 workspace bytes", align=Align.INLINE)
d.comment(0xA865, "Read svc_state[Y] (frame slot)", align=Align.INLINE)
d.label(0xA865, "loop_save_osword_ws")

d.comment(0xA868, "Save on stack", align=Align.INLINE)
d.comment(0xA869, "Load OSWORD parameter byte", align=Align.INLINE)
d.comment(0xA86C, "Copy parameter to workspace", align=Align.INLINE)
d.comment(0xA86F, "Next slot", align=Align.INLINE)
d.comment(0xA870, "Loop until Y wraps", align=Align.INLINE)
d.label(0xA870, "osword_store_svc_state")

d.comment(0xA872, "Set up dispatch and save state", align=Align.INLINE)
d.comment(0xA875, "Y=&FA: restore 6 workspace bytes", align=Align.INLINE)
d.label(0xA877, "loop_restore_osword_ws")


d.comment(0xA877, "Restore saved workspace byte", align=Align.INLINE)
d.comment(0xA878, "Store to osword_flag workspace", align=Align.INLINE)
d.comment(0xA87B, "Next byte", align=Align.INLINE)
d.comment(0xA87C, "Loop until all 6 restored", align=Align.INLINE)
d.comment(0xA87E, "Return from svc_8_osword", align=Align.INLINE)
d.label(0xA87F, "osword_setup_handler")

d.subroutine(
    0xA87F,
    "osword_setup_handler",
    title="Push OSWORD handler address for RTS dispatch",
    description="""Indexes the OSWORD dispatch table by X to
push a handler address (hi then lo) onto the
stack. Copies 3 bytes from the osword_flag
workspace into the RX buffer, loads PB byte 0
(the OSWORD sub-code), and clears svc_state.
The subsequent RTS dispatches to the pushed
handler address.""",
    on_entry={"x": "OSWORD handler index (0-6)"},
)


d.comment(0xA87F, "X = OSWORD index (0-6)", align=Align.INLINE)
d.comment(0xA882, "Push for stack frame manipulation", align=Align.INLINE)
d.comment(0xA883, "Load handler address low byte", align=Align.INLINE)
d.comment(0xA886, "Push again", align=Align.INLINE)
d.comment(0xA887, "Copy 3 bytes (Y=2,1,0)", align=Align.INLINE)
d.comment(0xA889, "Load from osword_flag workspace", align=Align.INLINE)
d.label(0xA88B, "rts_osword_setup")

d.comment(0xA88B, "RTS dispatches to pushed handler", align=Align.INLINE)
# UNMAPPED: d.comment(
# UNMAPPED:     0xA871,
# UNMAPPED:     "PB-ready / parameter table (3 bytes) read by osword_setup_handler at &A868 via LDA osword_pb_ready,X",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
# UNMAPPED: d.index_base(0xA871, "osword_pb_ready")

# UNMAPPED: d.label(0xA874, "osword_0e_handler")

# UNMAPPED: d.comment(
# UNMAPPED:     0xA874,
# UNMAPPED:     "BIT $abs -- 3-byte skip-trick that jumps over the extract_osword_subcode prologue when called via &A874",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
# UNMAPPED: d.entry(0xA874)
# UNMAPPED: d.comment(0xA877, "Shift ws_page right -- splits parameter byte into upper / lower nibbles", align=Align.INLINE)
# UNMAPPED: d.subroutine(
# UNMAPPED:     0xA877,
# UNMAPPED:     "extract_osword_subcode",
# UNMAPPED:     title="Decode OSWORD &0E parameter byte and branch to handler",
# UNMAPPED:     description="""Right-shifts `ws_page` (PB[0]) into `A`, transfers it to `Y` for
# UNMAPPED: the dispatcher, then runs an EOR/CMP chain against
# UNMAPPED: `ws_precomputed_value` to classify the requested sub-code:
# UNMAPPED: 
# UNMAPPED: | Test          | Path                              |
# UNMAPPED: | ------------- | --------------------------------- |
# UNMAPPED: | `CMP #4` =    | `save_txcb_and_convert` (clock)   |
# UNMAPPED: | `CMP #3` =    | `save_txcb_done` (write back)     |
# UNMAPPED: | anything else | set `svc_state = 8` and `RTS`     |
# UNMAPPED: 
# UNMAPPED: The two `LDA #&A9` filler bytes preceding the EOR are a 4-byte
# UNMAPPED: BIT-trick skip used when the alternate entry [`osword_0e_handler`
# UNMAPPED: ](address:A874) is taken via the `BIT $abs` at `&A874`. Reached
# UNMAPPED: only via the OSWORD `&0E` (CMOS clock read) handler chain.""",
# UNMAPPED: )

# UNMAPPED: d.label(0xA878, "osword_subcode_dispatch")

# UNMAPPED: d.comment(0xA879, "A = sub-code", align=Align.INLINE)
# UNMAPPED: d.comment(0xA87A, "LDA #&A9 -- 2-byte BIT-trick filler (skipped when entered at &A87E)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA87C, "LDA #&A9 -- 2-byte BIT-trick filler", align=Align.INLINE)
d.comment(0xA899, "Load template source pointer", align=Align.INLINE)
# UNMAPPED: d.comment(0xA884, "Compare with &04", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8A7, "Equal: take save_txcb_and_convert path", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8A9, "Restore A (OSWORD sub-code)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8AB, "Equal: take save_txcb_done path", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8AD, "Other sub-codes: set state = 8", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8AF, "Store service state", align=Align.INLINE)
# UNMAPPED: d.label(0xA8B1, "rts_osword_0e")

# UNMAPPED: d.comment(0xA8B1, "Return", align=Align.INLINE)
# UNMAPPED: d.label(0xA8B2, "save_txcb_and_convert")

# UNMAPPED: d.comment(0xA8B2, "X=0: start of TX control block", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8B4, "Y=&10: length of TXCB to save", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8B6, "Save current TX control block", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8B9, "Load seconds from clock workspace", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8BC, "Convert binary to BCD", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8BF, "Store BCD seconds", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8C2, "Load minutes from clock workspace", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8C5, "Convert binary to BCD", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8C8, "Store BCD minutes", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8CB, "Load hours from clock workspace", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8CE, "Convert binary to BCD", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8D1, "Store BCD hours", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8D4, "Clear hours high position", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8D6, "Store zero", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8D9, "Load day+month byte", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8DC, "Save for later high nibble extract", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8DD, "Load day value", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8E0, "Convert day to BCD", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8E3, "Store BCD day", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8E6, "Restore day+month byte", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8E7, "Push current A", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8E8, "Mask low nibble (month low bits)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8EA, "Convert to BCD", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8ED, "Store BCD month", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F0, "Pop saved value", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F1, "Shift high nibble down", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F2, "Divide by 4", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F3, "(continued)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F4, "4th shift: isolate high nibble", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F6, "Add &51 (offset base)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8F8, "Convert year to BCD", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8FB, "Store BCD year", align=Align.INLINE)
# UNMAPPED: d.comment(0xA8FE, "Copy 7 bytes (Y=6 down to 0)", align=Align.INLINE)
# UNMAPPED: d.label(0xA900, "loop_copy_bcd_to_pb")

# UNMAPPED: d.comment(0xA900, "Load BCD byte from workspace", align=Align.INLINE)
# UNMAPPED: d.comment(0xA903, "Store to parameter block", align=Align.INLINE)
# UNMAPPED: d.comment(0xA905, "Next byte down", align=Align.INLINE)
# UNMAPPED: d.comment(0xA906, "Loop for all 7 bytes", align=Align.INLINE)
# UNMAPPED: d.comment(0xA908, "Return", align=Align.INLINE)
# UNMAPPED: d.comment(0xA909, "Convert TXCB date/time bytes to BCD", align=Align.INLINE)
# UNMAPPED: d.label(0xA909, "save_txcb_done")

# UNMAPPED: d.comment(0xA90C, "Y=7: copy 8 bytes (Y=7 down to 0)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA90E, "Load BCD byte from TXCB area (hazel_txcb_lib + Y)", align=Align.INLINE)
# UNMAPPED: d.label(0xA90E, "loop_copy_pbytes_to_ws")

# UNMAPPED: d.comment(0xA911, "Store to PB[Y]", align=Align.INLINE)
# UNMAPPED: d.comment(0xA913, "Decrement Y (advance backwards)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA914, "Loop until Y wraps", align=Align.INLINE)
# UNMAPPED: d.comment(0xA916, "A=2: PB[0] parameter for OSWORD &0E (seconds-since-midnight format)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA918, "Store parameter at PB[0]", align=Align.INLINE)
# UNMAPPED: d.comment(0xA91A, "A=&0E: OSWORD &0E (read CMOS RTC)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA91C, "X = PB pointer low", align=Align.INLINE)
# UNMAPPED: d.comment(0xA91E, "Y = PB pointer high (via table_idx scratch)", align=Align.INLINE)
# UNMAPPED: d.label(0xA923, "bin_to_bcd")

# UNMAPPED: d.subroutine(
# UNMAPPED:     0xA923,
# UNMAPPED:     "bin_to_bcd",
# UNMAPPED:     title="Convert binary byte to BCD",
# UNMAPPED:     description="""Uses decimal mode (SED) with a count-up loop:
# UNMAPPED: starts at BCD 0 and adds 1 in decimal mode for
# UNMAPPED: each decrement of the binary input. Saves and
# UNMAPPED: restores the processor flags to avoid leaving
# UNMAPPED: decimal mode active. Called 6 times by
# UNMAPPED: save_txcb_and_convert for clock date/time
# UNMAPPED: conversion.""",
# UNMAPPED:     on_entry={"a": "binary value (0-99)"},
# UNMAPPED:     on_exit={"a": "BCD equivalent"},
# UNMAPPED: )


# UNMAPPED: d.comment(0xA923, "Save caller flags (D may be in any state)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA924, "Save A across decimal-mode arithmetic", align=Align.INLINE)
# UNMAPPED: d.comment(0xA925, "Zero: result is 0, skip loop", align=Align.INLINE)
# UNMAPPED: d.comment(0xA927, "Enter decimal mode", align=Align.INLINE)
# UNMAPPED: d.comment(0xA928, "Start BCD result at 0", align=Align.INLINE)
# UNMAPPED: d.label(0xA929, "loop_bcd_add")

# UNMAPPED: d.comment(0xA92A, "Clear carry for BCD add", align=Align.INLINE)
# UNMAPPED: d.comment(0xA92B, "Add 1 in decimal mode", align=Align.INLINE)
# UNMAPPED: d.comment(0xA92D, "Count down binary value", align=Align.INLINE)
# UNMAPPED: d.comment(0xA92E, "Loop until zero", align=Align.INLINE)
# UNMAPPED: d.label(0xA930, "done_bcd_convert")

# UNMAPPED: d.comment(0xA930, "Restore caller flags (incl. D)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA931, "Return with BCD result in A", align=Align.INLINE)
d.label(0xA932, "osword_10_handler")

d.subroutine(
    0xA932,
    "osword_10_handler",
    title="OSWORD &10 handler: send network packet",
    description="""ASL on [`tx_complete_flag`](label:tx_complete_flag) shifts the old bit 7
into Carry. When that bit was clear (`C=0`, TX in progress) the
handler stores Y back through the parameter-block pointer at
`(ws_ptr_hi),Y` and RTS, leaving the caller a status byte. When
it was set (`C=1`, TX idle) execution falls through to the start
path at [`setup_ws_rx_ptrs`](label:setup_ws_rx_ptrs), which seeds the
workspace pointers from [`net_rx_ptr_hi`](label:net_rx_ptr_hi)/`#&6F`,
copies 16 bytes of the parameter block into the workspace via
[`copy_pb_byte_to_ws`](label:copy_pb_byte_to_ws) and JMPs to
[`tx_begin`](address:8589) to launch the transmission.""",
    on_entry={"x, y": "OSWORD parameter block pointer (low, high)"},
)


d.entry(0xA932)
d.comment(0xA932, "ASL tx_complete_flag: old bit 7 -> C", align=Align.INLINE)
d.comment(0xA935, "A = Y (saved index)", align=Align.INLINE)
d.comment(0xA936, "C=1 (TX idle): start new transmission", align=Align.INLINE)
d.comment(0xA938, "C=0 (TX busy): write status byte back to PB", align=Align.INLINE)
d.comment(0xA93A, "Return (TX still in progress)", align=Align.INLINE)
d.label(0xA93B, "setup_ws_rx_ptrs")

d.comment(0xA93B, "Read net_rx_ptr_hi", align=Align.INLINE)
d.comment(0xA93D, "Copy to ws_ptr_lo", align=Align.INLINE)
d.comment(0xA93F, "Also set as NMI TX block high", align=Align.INLINE)
d.comment(0xA941, "Low byte = &6F", align=Align.INLINE)
d.comment(0xA943, "Set osword_flag", align=Align.INLINE)
d.comment(0xA945, "Set NMI TX block low", align=Align.INLINE)
d.comment(0xA947, "X=&0F: byte count for copy", align=Align.INLINE)
d.comment(0xA949, "Copy data and begin transmission", align=Align.INLINE)
d.comment(0xA94C, "Jump to begin Econet transmission", align=Align.INLINE)
d.subroutine(
    0xA94F,
    "osword_11_handler",
    title="OSWORD &11 handler: receive network packet",
    description="""Reached via the OSWORD dispatch as well as via fall-through from
[`osword_10_handler`](label:osword_10_handler). Configures the workspace
pointer from `nfs_workspace_hi`, saves the Econet interrupt state
via `ROR econet_flags`, and either uses the slot specified by the
caller (Y non-zero) or scans from slot 3 onwards via
[`byte_to_2bit_index`](label:byte_to_2bit_index) to find a free slot. Stores
the resulting status byte and the copied PB bytes back into the
caller's parameter block.""",
    on_entry={"x, y": "OSWORD parameter block pointer (low, high)"},
)


d.entry(0xA94F)
d.comment(0xA94F, "Load NFS workspace page high byte", align=Align.INLINE)
d.comment(0xA951, "Set workspace pointer high", align=Align.INLINE)
d.comment(0xA953, "Set workspace pointer low from Y", align=Align.INLINE)
d.comment(0xA955, "Rotate Econet flags (save interrupt state)", align=Align.INLINE)
d.comment(0xA958, "Y=OSWORD flag (slot specifier)", align=Align.INLINE)
d.comment(0xA959, "Store OSWORD flag", align=Align.INLINE)
d.comment(0xA95B, "Non-zero: use specified slot", align=Align.INLINE)
d.comment(0xA95D, "A=3: start searching from slot 3", align=Align.INLINE)
d.label(0xA95F, "loop_find_rx_slot")

d.comment(0xA95F, "Convert slot to 2-bit workspace index", align=Align.INLINE)
d.comment(0xA962, "C set: slot invalid, store result", align=Align.INLINE)
d.comment(0xA964, "Divide by 2", align=Align.INLINE)
d.comment(0xA965, "Continue shift", align=Align.INLINE)
d.comment(0xA966, "Index to X", align=Align.INLINE)
d.comment(0xA967, "Load workspace byte at offset", align=Align.INLINE)
d.comment(0xA969, "Zero: slot empty, store result", align=Align.INLINE)
d.comment(0xA96B, "Compare with &3F ('?' marker)", align=Align.INLINE)
d.comment(0xA96D, "Match: slot found for receive", align=Align.INLINE)
d.comment(0xA96F, "Step to next slot", align=Align.INLINE)
d.comment(0xA970, "Transfer back to A", align=Align.INLINE)
d.comment(0xA971, "Loop back (A != 0)", align=Align.INLINE)
d.label(0xA973, "store_rx_slot_found")

d.comment(0xA973, "Found slot index", align=Align.INLINE)
d.comment(0xA974, "X=0: index for indirect store", align=Align.INLINE)
d.comment(0xA976, "Store slot number to PB byte 0", align=Align.INLINE)
d.label(0xA978, "use_specified_slot")

d.comment(0xA978, "Convert specified slot to workspace index", align=Align.INLINE)
d.comment(0xA97B, "C set: slot invalid, store result", align=Align.INLINE)
d.comment(0xA97D, "Back up scan", align=Align.INLINE)
d.comment(0xA97E, "Update workspace pointer low", align=Align.INLINE)
d.comment(0xA980, "A=&C0: slot active marker", align=Align.INLINE)
d.comment(0xA982, "Y=1: result-byte offset", align=Align.INLINE)
d.comment(0xA984, "X=&0B: byte count for PB copy", align=Align.INLINE)
d.comment(0xA986, "Compare Y with OSWORD flag", align=Align.INLINE)
d.comment(0xA988, "Add workspace byte (check slot state)", align=Align.INLINE)
d.comment(0xA98A, "Zero: slot ready, copy PB and mark", align=Align.INLINE)
d.comment(0xA98C, "Negative: slot busy, increment and retry", align=Align.INLINE)
d.label(0xA98E, "loop_copy_slot_data")

d.comment(0xA98E, "For the ADC chain", align=Align.INLINE)
d.label(0xA98F, "copy_pb_and_mark")

d.comment(0xA98F, "Copy PB byte to workspace slot", align=Align.INLINE)
d.comment(0xA992, "C set: copy done, finish", align=Align.INLINE)
d.comment(0xA994, "A=&3F: mark slot as pending ('?')", align=Align.INLINE)
d.comment(0xA996, "Y=1: workspace flag offset", align=Align.INLINE)
d.comment(0xA998, "Store pending marker to workspace", align=Align.INLINE)
d.label(0xA99C, "increment_and_retry")

d.comment(0xA99C, "Increment retry counter", align=Align.INLINE)
d.comment(0xA99E, "Non-zero: retry copy loop", align=Align.INLINE)
d.comment(0xA9A0, "Decrement Y (adjust offset)", align=Align.INLINE)
d.label(0xA9A1, "store_rx_result")

d.comment(0xA9A1, "Store result A to PB via Y", align=Align.INLINE)
d.label(0xA9A3, "osword_11_done")

d.comment(0xA9A3, "Rotate Econet flags back (restore state)", align=Align.INLINE)
d.comment(0xA9A6, "Return from OSWORD 11 handler", align=Align.INLINE)
d.label(0xA9A7, "osword_12_handler")

d.subroutine(
    0xA9A7,
    "osword_12_handler",
    title="OSWORD &12 handler: receive packet from workspace",
    description="""Reads `net_rx_ptr_hi` into `ws_ptr_lo`, sets `Y=&7F` and reads the
status byte from the RX block, then `Y=&80` to flag the packet as
processed. The body proceeds to copy the packet payload from the
RX buffer into the OSWORD parameter block via
[`copy_pb_byte_to_ws`](label:copy_pb_byte_to_ws).""",
    on_entry={"x, y": "OSWORD parameter block pointer (low, high)"},
)
d.entry(0xA9A7)
d.comment(0xA9A7, "Set workspace from RX ptr high", align=Align.INLINE)
d.comment(0xA9A9, "Store to ws_ptr_lo", align=Align.INLINE)
d.comment(0xA9AB, "Y=&7F: last byte of RX buffer", align=Align.INLINE)
d.comment(0xA9AD, "Load port/count from RX buffer", align=Align.INLINE)
d.comment(0xA9AF, "Y=&80: set workspace pointer", align=Align.INLINE)
d.comment(0xA9B0, "Store as osword_flag", align=Align.INLINE)
d.comment(0xA9B2, "X = port/count value", align=Align.INLINE)
d.comment(0xA9B3, "X-1: adjust count", align=Align.INLINE)
d.comment(0xA9B4, "Y=0 for copy", align=Align.INLINE)
d.comment(0xA9B6, "Copy workspace data", align=Align.INLINE)
d.comment(0xA9B9, "Update state and return", align=Align.INLINE)
d.label(0xA9BC, "osword_13_dispatch")

d.entry(0xA9BC)
d.comment(0xA9BC, "X = sub-code", align=Align.INLINE)
d.comment(0xA9BD, "Sub-code < &13?", align=Align.INLINE)
d.comment(0xA9BF, "Out of range: return", align=Align.INLINE)
d.comment(0xA9C1, "Read dispatch hi from osword_13_dispatch_hi+X", align=Align.INLINE)
d.comment(0xA9C4, "Push hi for RTS dispatch", align=Align.INLINE)
d.comment(0xA9C5, "Read dispatch lo from osword_13_dispatch_lo+X", align=Align.INLINE)
d.comment(0xA9C8, "Push lo for RTS dispatch", align=Align.INLINE)
d.label(0xA9C9, "rts_osword_13")
d.comment(0xA9C9, "RTS -> dispatched OSWORD &13 sub-handler", align=Align.INLINE)
# UNMAPPED: d.index_base(0xA9A8, "osword_13_dispatch_lo")
# UNMAPPED: d.banner(
# UNMAPPED:     0xA9A8,
# UNMAPPED:     title="OSWORD &13 dispatch low-byte table (18 entries)",
# UNMAPPED:     description="""Read by [`osword_13_dispatch`](label:osword_13_dispatch) as `LDA &A9A8,X`. Paired
# UNMAPPED: with the high-byte half at [`osword_13_dispatch_hi`](label:osword_13_dispatch_hi).
# UNMAPPED: Sub-codes 0..&11 cover read/set station, read/write workspace pair,
# UNMAPPED: read/write protection, read/set handles, read RX flag/port/error,
# UNMAPPED: read context, read/write CSD, read free buffers, read/write context
# UNMAPPED: 3, and bridge query.""",
# UNMAPPED: )
# UNMAPPED: for addr in range(0xA9A8, 0xA9BA):
# UNMAPPED (orphan body):     d.byte(addr)
# UNMAPPED (orphan body): 
d.index_base(0xA9DC, "osword_13_dispatch_hi")
d.banner(
    0xA9DC,
    title="OSWORD &13 dispatch high-byte table (18 entries)",
    description="""Read by [`osword_13_dispatch`](label:osword_13_dispatch) as `LDA &A9BA,X`. The
dispatcher pushes the hi byte first then the lo, so RTS lands on
`target` (the table stores `target-1`).""",
)
for addr in range(0xA9DC, 0xA9EE):
    d.byte(addr)
d.entry(0xA9EE)


d.subroutine(
    0xA9EE,
    "osword_13_read_station",
    title="OSWORD &13 sub 0: read file server station",
    description="""Returns the current file server station and network numbers in
`PB[1..2]`. If ANFS is not active,
[`ensure_fs_selected`](label:ensure_fs_selected) auto-selects it (raising `net
checksum` on failure) before the body runs.""",
)
d.comment(0xA9EE, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.label(0xA9F1, "read_station_bytes")

d.comment(0xA9F1, "Y=2: copy 2 bytes", align=Align.INLINE)
d.label(0xA9F3, "loop_copy_station")

d.comment(0xA9F3, "Load station byte", align=Align.INLINE)
d.comment(0xA9F6, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xA9F8, "Step back", align=Align.INLINE)
d.comment(0xA9F9, "Loop for bytes 2..1", align=Align.INLINE)
d.comment(0xA9FB, "Return", align=Align.INLINE)
d.entry(0xA9FC)


d.subroutine(
    0xA9FC,
    "osword_13_set_station",
    title="OSWORD &13 sub 1: set file server station",
    description="""Sets the file server station and network numbers from `PB[1..2]`.
The prologue at `&A9DC` calls
[`ensure_fs_selected`](label:ensure_fs_selected) to verify ANFS is active
(auto-selecting it if not), then the body at
[`osword_13_set_station_body`](label:osword_13_set_station_body) processes all FCBs
and scans the 16-entry FCB table to reassign handles matching the
new station.""",
)

d.comment(0xA9FC, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.label(0xA9FF, "osword_13_set_station_body")


d.comment(0xA9FF, "Y=0 for process_all_fcbs", align=Align.INLINE)
d.comment(0xAA01, "Close all open FCBs", align=Align.INLINE)
d.comment(0xAA04, "Y=2: copy 2 bytes", align=Align.INLINE)
d.label(0xAA06, "loop_store_station")

d.comment(0xAA06, "Load new station byte from PB", align=Align.INLINE)
d.comment(0xAA08, "Store to fs_server_base", align=Align.INLINE)
d.comment(0xAA0B, "Step back to previous byte", align=Align.INLINE)
d.comment(0xAA0C, "Loop for bytes 2..1", align=Align.INLINE)
d.comment(0xAA0E, "Clear handles if station matches", align=Align.INLINE)
d.comment(0xAA11, "A=&0E: bits 1..3 (FS-state mask)", align=Align.INLINE)
d.comment(0xAA13, "Set fs_flags bits 1..3", align=Align.INLINE)
d.comment(0xAA16, "A=&40: FS-active flag bit", align=Align.INLINE)
d.comment(0xAA18, "Clear FS-active flag (bit 6)", align=Align.INLINE)
d.comment(0xAA1B, "X=&0F: scan all 16 FCB slots (X = 15 down to 0)", align=Align.INLINE)
d.label(0xAA1D, "scan_fcb_entry")

d.comment(0xAA1D, "Load FCB flags", align=Align.INLINE)
d.comment(0xAA20, "Save flags in Y", align=Align.INLINE)
d.comment(0xAA21, "Test bit 1 (FCB allocated?)", align=Align.INLINE)
d.comment(0xAA23, "No: skip to next entry", align=Align.INLINE)
d.comment(0xAA25, "Entry index to A", align=Align.INLINE)
d.comment(0xAA26, "Mask bit 5", align=Align.INLINE)
d.comment(0xAA28, "Store updated flags", align=Align.INLINE)
d.comment(0xAA2B, "Save in Y", align=Align.INLINE)
d.comment(0xAA2C, "Does FCB match new station?", align=Align.INLINE)
d.comment(0xAA2F, "No match: skip to next", align=Align.INLINE)
d.comment(0xAA31, "Clear carry", align=Align.INLINE)
d.comment(0xAA32, "Restore flags", align=Align.INLINE)
d.comment(0xAA33, "Test bit 2 (handle 1 active?)", align=Align.INLINE)
d.comment(0xAA35, "No: check handle 2", align=Align.INLINE)
d.comment(0xAA37, "Restore flags", align=Align.INLINE)
d.comment(0xAA38, "Set bit 5 (handle reassigned)", align=Align.INLINE)
d.comment(0xAA3B, "Get FCB high byte", align=Align.INLINE)
d.comment(0xAA3E, "Store as handle 1 station", align=Align.INLINE)
d.comment(0xAA41, "FCB index", align=Align.INLINE)
d.comment(0xAA42, "Add &20 for FCB table offset", align=Align.INLINE)
d.comment(0xAA44, "Store as handle 1 FCB index", align=Align.INLINE)
d.comment(0xAA47, "A=2: fs_flags bit 1 mask", align=Align.INLINE)
d.comment(0xAA49, "Clear fs_flags bit 1", align=Align.INLINE)
d.label(0xAA4C, "check_handle_2")

d.comment(
    0xAA4C,
    "Y still holds the saved FCB status -- TYA so we can re-test bit 3 (handle-2 active flag)",
    align=Align.INLINE,
)
d.comment(0xAA4D, "Test bit 3 (handle 2 active?)", align=Align.INLINE)
d.comment(0xAA4F, "No: check handle 3", align=Align.INLINE)
d.comment(0xAA52, "Set bit 5", align=Align.INLINE)
d.comment(0xAA55, "Get FCB high byte", align=Align.INLINE)
d.comment(0xAA58, "Store as handle 2 station", align=Align.INLINE)
d.comment(0xAA5B, "FCB index", align=Align.INLINE)
d.comment(0xAA5C, "Add &20 for FCB table offset", align=Align.INLINE)
d.comment(0xAA5E, "Store as handle 2 FCB index", align=Align.INLINE)
d.comment(0xAA61, "A=4: fs_flags bit 2 mask", align=Align.INLINE)
d.comment(0xAA63, "Clear fs_flags bit 2", align=Align.INLINE)
d.label(0xAA66, "check_handle_3")

d.comment(
    0xAA66,
    "Y still holds the saved FCB status -- TYA so we can re-test bit 4 (handle-3 active flag)",
    align=Align.INLINE,
)
d.comment(0xAA67, "Test bit 4 (handle 3 active?)", align=Align.INLINE)
d.comment(0xAA69, "No: store final flags", align=Align.INLINE)
d.comment(0xAA6B, "Restore flags", align=Align.INLINE)
d.comment(0xAA6C, "Set bit 5", align=Align.INLINE)
d.comment(0xAA6E, "Save updated flags", align=Align.INLINE)
d.comment(0xAA6F, "Get FCB high byte", align=Align.INLINE)
d.comment(0xAA72, "Store as handle 3 station", align=Align.INLINE)
d.comment(0xAA75, "FCB index", align=Align.INLINE)
d.comment(0xAA76, "Add &20 for FCB table offset", align=Align.INLINE)
d.comment(0xAA78, "Store as handle 3 FCB index", align=Align.INLINE)
d.comment(0xAA7B, "A=8: fs_flags bit 3 (FS-error pending)", align=Align.INLINE)
d.comment(0xAA7D, "Clear FS-error-pending flag", align=Align.INLINE)
d.label(0xAA80, "store_updated_status")

d.comment(0xAA80, "A = Y for store", align=Align.INLINE)
d.comment(0xAA81, "Store updated status into hazel_fcb_status[X]", align=Align.INLINE)
d.label(0xAA84, "next_fcb_entry")

d.comment(0xAA84, "Decrement entry counter", align=Align.INLINE)
d.comment(0xAA85, "Loop while X >= 0 (scan all FCBs)", align=Align.INLINE)
d.comment(0xAA87, "A=&0E: status flag value", align=Align.INLINE)
d.comment(0xAA89, "Test fs_flags bits 1..3", align=Align.INLINE)
d.comment(0xAA8C, "Non-zero: skip the FS-active set", align=Align.INLINE)
d.comment(0xAA8E, "A=&40: FS-active flag bit", align=Align.INLINE)
d.comment(0xAA90, "Set FS-active flag (bit 6 of fs_flags)", align=Align.INLINE)
d.comment(0xAA93, "Return -- FCB-status update complete", align=Align.INLINE)
d.entry(0xAA94)
d.subroutine(
    0xAA94,
    "osword_13_read_csd",
    title="OSWORD &13 sub 12: read CSD path",
    description="""Reads 5 current selected directory path bytes
from the RX workspace at offset &17 into
PB[1..5]. Sets carry clear to select the
workspace-to-PB copy direction.""",
)


d.comment(0xAA94, "WS-to-PB direction (read)", align=Align.INLINE)
d.comment(0xAA95, "Skip SEC", align=Align.INLINE)
d.entry(0xAA97)

d.subroutine(
    0xAA97,
    "osword_13_write_csd",
    title="OSWORD &13 sub 13: write CSD path",
    description="""Writes 5 current selected directory path bytes
from PB[1..5] into the RX workspace at offset
&17. Sets carry to select the PB-to-workspace
copy direction.""",
)


d.comment(0xAA97, "C=1: PB-to-workspace direction", align=Align.INLINE)
d.label(0xAA98, "setup_csd_copy")

d.comment(0xAA98, "Workspace offset &17", align=Align.INLINE)
d.comment(0xAA9A, "Save A as osword_flag (counter)", align=Align.INLINE)
d.comment(0xAA9C, "Page from RX pointer high byte", align=Align.INLINE)
d.comment(0xAA9E, "Set ws_ptr_hi", align=Align.INLINE)
d.comment(0xAAA0, "Y=1: first PB data byte", align=Align.INLINE)
d.comment(0xAAA2, "X=5: copy 5 bytes", align=Align.INLINE)
d.subroutine(
    0xAAA4,
    "copy_pb_byte_to_ws",
    title="Conditionally copy parameter block byte to workspace",
    description="""If carry is set, loads a byte from the OSWORD
parameter block at offset Y; if clear, uses
the value already in A. Stores the result to
workspace at the current offset. Decrements X
and loops until the requested byte count is
transferred.""",
    on_entry={"c": "set to load from PB, clear to use A", "x": "byte count", "y": "PB source offset"},
)


d.comment(0xAAA4, "C=0: skip PB-to-WS copy", align=Align.INLINE)
d.comment(0xAAA6, "C=1: load from parameter block", align=Align.INLINE)
d.comment(0xAAA8, "Store to workspace", align=Align.INLINE)
d.label(0xAAAA, "copy_ws_byte_to_pb")

d.comment(0xAAAA, "Load from workspace", align=Align.INLINE)
d.comment(0xAAAC, "Store to parameter block", align=Align.INLINE)
d.comment(0xAAAE, "Next byte", align=Align.INLINE)
d.comment(0xAAAF, "Count down", align=Align.INLINE)
d.comment(0xAAB0, "Loop for all bytes", align=Align.INLINE)
d.comment(0xAAB2, "Return", align=Align.INLINE)
d.subroutine(
    0xAAB3,
    "osword_13_read_ws_pair",
    title="OSWORD &13 sub 2: read workspace byte pair",
    description="""Reads 2 bytes from the NFS workspace page
starting at offset 1 into PB[1..2]. Uses
nfs_workspace_hi as the page and
copy_pb_byte_to_ws with carry clear for the
workspace-to-PB direction.""",
)


d.comment(0xAAB3, "Load workspace page high byte", align=Align.INLINE)
d.comment(0xAAB5, "Set ws_ptr_hi", align=Align.INLINE)
d.comment(0xAAB7, "Y=1", align=Align.INLINE)
d.comment(0xAAB8, "A = current byte index", align=Align.INLINE)
d.comment(0xAAB9, "Set ws_ptr_lo = 1", align=Align.INLINE)
d.comment(0xAABB, "X=1: copy 2 bytes", align=Align.INLINE)
d.comment(0xAABC, "WS-to-PB direction", align=Align.INLINE)
d.comment(0xAABD, "Copy via copy_pb_byte_to_ws", align=Align.INLINE)
d.subroutine(
    0xAABF,
    "osword_13_write_ws_pair",
    title="OSWORD &13 sub 3: write workspace byte pair",
    description="""Writes 2 bytes from PB[1..2] into the NFS
workspace at offsets 2 and 3. Then calls
init_bridge_poll and conditionally clears
the workspace byte if the bridge status
changed.""",
)


d.comment(0xAABF, "Y=1: first PB data byte", align=Align.INLINE)
d.comment(0xAAC0, "Load PB[1]", align=Align.INLINE)
d.comment(0xAAC2, "Next byte", align=Align.INLINE)
d.comment(0xAAC3, "Store to (nfs_workspace)+2", align=Align.INLINE)
d.comment(0xAAC5, "Load PB[2]", align=Align.INLINE)
d.comment(0xAAC7, "Y=3", align=Align.INLINE)
d.comment(0xAAC8, "Store to (nfs_workspace)+3", align=Align.INLINE)
d.comment(0xAACA, "Reinitialise bridge routing", align=Align.INLINE)
d.comment(0xAACD, "Compare result with workspace", align=Align.INLINE)
d.comment(0xAACF, "Different: leave unchanged", align=Align.INLINE)
d.comment(0xAAD1, "Same: clear workspace byte", align=Align.INLINE)
d.label(0xAAD3, "rts_write_ws_pair")

d.comment(0xAAD3, "Return", align=Align.INLINE)
d.subroutine(
    0xAAD4,
    "osword_13_read_prot",
    title="OSWORD &13 sub 4: read protection mask",
    description="""Returns the current protection mask (prot_status)
in PB[1].""",
)


d.comment(0xAAD4, "Load protection mask", align=Align.INLINE)
d.comment(0xAAD7, "Store to PB[1] and return", align=Align.INLINE)
d.subroutine(
    0xAADA,
    "osword_13_write_prot",
    title="OSWORD &13 sub 5: write protection mask",
    description="""Loads the new protection mask from `PB[1]` and falls through into
[`set_ws_pair_0d68_0d69`](label:set_ws_pair_0d68_0d69) which mirrors it into the
ACR/SR-format byte pair at `&0D68` / `&0D69` that ANFS uses for its
own state tracking.""",
)


d.comment(0xAADA, "Y=1: PB data offset", align=Align.INLINE)
d.comment(0xAADB, "Load new mask from PB[1]", align=Align.INLINE)
d.subroutine(
    0xAADD,
    "set_ws_pair_0d68_0d69",
    title="Store A in both prot_status and prot_status_save",
    description="""Copies `A` to both [`prot_status`](label:prot_status) and
[`prot_status_save`](label:prot_status_save), then `RTS`. The bytes carry ACR/SR-style
flag layouts that ANFS uses internally; nothing in this ROM flushes
them to the live System VIA. Two callers:
[`nfs_init_body`](label:nfs_init_body) at `&8FA8` (where A is `0` or
`&FF` based on FS-options bit 6) and
[`cmd_prot`](label:cmd_prot) at `&B704` (the *Prot path).
A 2-store-and-return convenience to keep both call sites flat.""",
    on_entry={"a": "value to mirror into both workspace bytes"},
)
d.comment(0xAADD, "Mirror A into prot_status (ACR-format byte)", align=Align.INLINE)
d.comment(0xAAE0, "Mirror A into prot_status_save (IER-format byte)", align=Align.INLINE)
d.comment(0xAAE3, "Return", align=Align.INLINE)
d.entry(0xAAE4)


d.subroutine(
    0xAAE4,
    "osword_13_read_handles",
    title="OSWORD &13 sub 6: read FCB handle info",
    description="""Returns the 3-byte FCB handle/port data from the workspace at
`C271[1..3]` into `PB[1..3]`. If ANFS is not active,
[`ensure_fs_selected`](label:ensure_fs_selected) auto-selects it before the
body runs.""",
)
d.comment(0xAAE4, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.comment(0xAAE7, "Y=3: copy 3 bytes", align=Align.INLINE)
d.label(0xAAE9, "loop_copy_handles")

d.comment(0xAAE9, "Load handle byte", align=Align.INLINE)
d.comment(0xAAEC, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xAAEE, "Previous byte", align=Align.INLINE)
d.comment(0xAAEF, "Loop for bytes 3..1", align=Align.INLINE)
d.comment(0xAAF1, "Return", align=Align.INLINE)
d.entry(0xAAF2)


d.subroutine(
    0xAAF2,
    "osword_13_set_handles",
    title="OSWORD &13 sub 7: set FCB handles",
    description="""Validates and assigns up to 3 FCB handles
from PB[1..3]. Each handle value (&20-&2F)
indexes the channel tables. For valid handles
with the appropriate flag bit, stores the
station and FCB index, then updates flag bits
across all FCB entries via update_fcb_flag_bits.""",
)


d.comment(0xAAF2, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.label(0xAAF5, "start_set_handles")

d.comment(0xAAF5, "Y=1: first handle in PB", align=Align.INLINE)
d.label(0xAAF7, "validate_handle")

d.comment(0xAAF7, "Load handle value from PB[Y]", align=Align.INLINE)
d.comment(0xAAF9, "Must be >= &20", align=Align.INLINE)
d.comment(0xAAFB, "Below range: invalid", align=Align.INLINE)
d.comment(0xAAFD, "Must be < &30", align=Align.INLINE)
d.comment(0xAAFF, "Above range: invalid", align=Align.INLINE)
d.comment(0xAB01, "X = handle value", align=Align.INLINE)
d.comment(0xAB02, "Load fcb_attr_or_count_mid[handle]", align=Align.INLINE)
d.comment(0xAB05, "Non-zero: FCB exists", align=Align.INLINE)
d.label(0xAB07, "handle_invalid")

d.comment(0xAB07, "A=0: invalid-handle marker", align=Align.INLINE)
d.comment(0xAB0A, "Clear PB[0] status", align=Align.INLINE)
d.comment(0xAB0C, "Skip to next handle", align=Align.INLINE)
d.label(0xAB0E, "check_handle_alloc")

d.comment(0xAB0E, "Load fcb_flags[handle] flags", align=Align.INLINE)
d.comment(0xAB11, "Test bit 1 (allocated?)", align=Align.INLINE)
d.comment(0xAB13, "Not allocated: invalid", align=Align.INLINE)
d.comment(0xAB15, "X = handle value", align=Align.INLINE)
d.comment(0xAB16, "Store handle to fs_lib_flags+Y", align=Align.INLINE)
d.comment(0xAB19, "Load station from fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0xAB1C, "Store station to fs_server_net+Y", align=Align.INLINE)
d.comment(0xAB1F, "Is this handle 1 (Y=1)?", align=Align.INLINE)
d.comment(0xAB21, "No: check handle 2", align=Align.INLINE)
d.comment(0xAB23, "Save Y for processing", align=Align.INLINE)
d.comment(0xAB24, "Push Y", align=Align.INLINE)
d.comment(0xAB25, "Bit mask &04 for handle 1", align=Align.INLINE)
d.comment(0xAB27, "Update flags across all FCBs", align=Align.INLINE)
d.comment(0xAB2A, "Pop saved Y", align=Align.INLINE)
d.comment(0xAB2B, "Back to Y", align=Align.INLINE)
d.comment(0xAB2C, "Reload fcb_flags flags", align=Align.INLINE)
d.comment(0xAB2F, "Set bits 2+5 (active+updated)", align=Align.INLINE)
d.comment(0xAB31, "Store updated flags", align=Align.INLINE)
d.label(0xAB34, "next_handle_slot")

d.comment(0xAB34, "Next handle slot", align=Align.INLINE)
d.comment(0xAB35, "Compare with 4", align=Align.INLINE)
d.comment(0xAB37, "No: process next handle", align=Align.INLINE)
d.comment(0xAB39, "Y=3 for return", align=Align.INLINE)
d.comment(0xAB3A, "Return", align=Align.INLINE)
d.label(0xAB3B, "assign_handle_2")

d.comment(0xAB3B, "Is this handle 2 (Y=2)?", align=Align.INLINE)
d.comment(0xAB3D, "No: must be handle 3", align=Align.INLINE)
d.comment(0xAB3F, "Save current Y", align=Align.INLINE)
d.comment(0xAB40, "Push Y", align=Align.INLINE)
d.comment(0xAB41, "Y=8 (handle-bit shift index)", align=Align.INLINE)
d.comment(0xAB43, "Update flags across all FCBs", align=Align.INLINE)
d.comment(0xAB46, "Restore Y", align=Align.INLINE)
d.comment(0xAB47, "Back to Y", align=Align.INLINE)
d.comment(0xAB48, "Reload fcb_flags flags", align=Align.INLINE)
d.comment(0xAB4B, "Set bits 3 and 5", align=Align.INLINE)
d.comment(0xAB4D, "Store updated flags", align=Align.INLINE)
d.comment(0xAB50, "Next handle slot", align=Align.INLINE)
d.label(0xAB52, "assign_handle_3")

d.comment(0xAB52, "Handle 3: save Y", align=Align.INLINE)
d.comment(0xAB53, "Push for save/restore", align=Align.INLINE)
d.comment(0xAB54, "Bit mask &10 for handle 3", align=Align.INLINE)
d.comment(0xAB56, "Update flags across all FCBs", align=Align.INLINE)
d.comment(0xAB59, "Pop saved value", align=Align.INLINE)
d.comment(0xAB5A, "Back to Y", align=Align.INLINE)
d.comment(0xAB5B, "Reload fcb_flags flags", align=Align.INLINE)
d.comment(0xAB5E, "Set bits 4+5 (active+updated)", align=Align.INLINE)
d.comment(0xAB60, "Store updated flags", align=Align.INLINE)
d.comment(0xAB63, "Next handle slot", align=Align.INLINE)
d.subroutine(
    0xAB65,
    "update_fcb_flag_bits",
    title="Update FCB flag bits across all entries",
    description="""Scans all 16 FCB entries in hazel_fcb_status. For each
entry with bit 6 set, tests the Y-specified
bit mask: if matching, ORs bit 5 into the
flags; if not, leaves bit 5 clear. In both
cases, inverts and clears the tested bits.
Preserves X.""",
    on_entry={"y": "flag bit mask to test", "x": "current FCB index (preserved)"},
)


d.comment(0xAB65, "A = caller X", align=Align.INLINE)
d.comment(0xAB66, "Push X", align=Align.INLINE)
d.comment(0xAB67, "X=&0F: scan all 16 FCB slots", align=Align.INLINE)
d.label(0xAB69, "loop_scan_fcb_flags")

d.comment(0xAB69, "Load FCB flags", align=Align.INLINE)
d.comment(0xAB6C, "Shift bits 6-7 into bits 7-0", align=Align.INLINE)
d.comment(0xAB6D, "Shift bit into carry for test", align=Align.INLINE)
d.comment(0xAB6E, "Bit 6 clear: skip entry", align=Align.INLINE)
d.comment(0xAB70, "Restore Y (bit mask)", align=Align.INLINE)
d.comment(0xAB71, "Test mask bits against flags", align=Align.INLINE)
d.comment(0xAB74, "Zero: no matching bits", align=Align.INLINE)
d.comment(0xAB76, "Matching: restore Y", align=Align.INLINE)
d.comment(0xAB77, "Set bit 5 (updated)", align=Align.INLINE)
d.comment(0xAB79, "Skip clear path", align=Align.INLINE)
d.label(0xAB7B, "no_flag_match")

d.comment(0xAB7B, "No match: restore Y", align=Align.INLINE)
d.label(0xAB7C, "clear_flag_bits")

d.comment(0xAB7C, "Invert all bits", align=Align.INLINE)
d.comment(0xAB7E, "Clear tested bits in flags", align=Align.INLINE)
d.comment(0xAB81, "Store updated flags", align=Align.INLINE)
d.label(0xAB84, "next_flag_entry")

d.comment(0xAB84, "Decrement FCB index", align=Align.INLINE)
d.comment(0xAB85, "Loop for all 16 entries", align=Align.INLINE)
d.comment(0xAB87, "Restore original X", align=Align.INLINE)
d.comment(0xAB88, "Back to X", align=Align.INLINE)
d.comment(0xAB89, "Return", align=Align.INLINE)
d.subroutine(
    0xAB8A,
    "osword_13_read_rx_flag",
    title="OSWORD &13 sub 8: read RX control block flag",
    description="""Returns byte 1 of the current RX control
block in PB[1].""",
)


d.comment(0xAB8A, "Y=1: PB[1] = RX flag location", align=Align.INLINE)
d.comment(0xAB8C, "Load (net_rx_ptr)+1", align=Align.INLINE)
d.comment(0xAB8E, "Y=0", align=Align.INLINE)
d.comment(0xAB90, "Store to PB[1] and return", align=Align.INLINE)
d.subroutine(
    0xAB93,
    "osword_13_read_rx_port",
    title="OSWORD &13 sub 9: read RX port byte",
    description="""Returns byte &7F of the current RX control
block in PB[1], and stores &80 in PB[2].""",
)


d.comment(0xAB93, "Y=&7F: port byte offset", align=Align.INLINE)
d.comment(0xAB95, "Load (net_rx_ptr)+&7F", align=Align.INLINE)
d.comment(0xAB97, "Y=1", align=Align.INLINE)
d.comment(0xAB99, "Store to PB[1]", align=Align.INLINE)
d.comment(0xAB9C, "A=&80", align=Align.INLINE)
d.comment(0xAB9E, "Store &80 to PB[2]", align=Align.INLINE)
d.comment(0xABA0, "Return", align=Align.INLINE)
d.subroutine(
    0xABA1,
    "osword_13_read_error",
    title="OSWORD &13 sub 10: read error flag",
    description="""Returns the latched FS last-error byte
([`hazel_fs_last_error`](label:hazel_fs_last_error)) in `PB[1]`. Falls through
into [`store_a_to_pb_1`](label:store_a_to_pb_1).""",
)


d.comment(0xABA1, "Load error flag", align=Align.INLINE)
d.label(0xABA4, "store_a_to_pb_1")

d.subroutine(
    0xABA4,
    "store_a_to_pb_1",
    title="Store A to OSWORD parameter block at offset 1",
    description="""Increments Y to 1 and stores A into the
OSWORD parameter block via (ws_ptr_hi),Y.
Used by OSWORD 13 sub-handlers to return a
single result byte.""",
    on_entry={"A": "value to store"},
    on_exit={"Y": "1"},
)


d.comment(0xABA4, "Y=1: parameter block offset 1", align=Align.INLINE)
d.comment(0xABA5, "Store result to PB[1]", align=Align.INLINE)
d.comment(0xABA7, "Return", align=Align.INLINE)
d.subroutine(
    0xABA8,
    "osword_13_read_context",
    title="OSWORD &13 sub 11: read context byte",
    description="""Returns the FS context/error code
([`hazel_fs_error_code`](label:hazel_fs_error_code)) in `PB[1]` when bit 7 is
clear; if bit 7 is set the value is left alone (the BPL skips the
store). Tail-merges into [`store_a_to_pb_1`](label:store_a_to_pb_1).""",
)


d.comment(0xABA8, "Load context byte", align=Align.INLINE)
d.comment(0xABAB, "Bit 7 clear: store context to PB", align=Align.INLINE)
d.subroutine(
    0xABAD,
    "osword_13_read_free_bufs",
    title="OSWORD &13 sub 14: read printer buffer free space",
    description="""Returns the number of free bytes remaining in
the printer spool buffer (&6F minus spool_buf_idx)
in PB[1]. The buffer starts at offset &25 and can
hold up to &4A bytes of spool data.""",
)


d.comment(0xABAD, "Total buffers = &6F", align=Align.INLINE)
d.comment(0xABAF, "PB-to-WS direction (write)", align=Align.INLINE)
d.comment(0xABB0, "Free = &6F - spool_buf_idx", align=Align.INLINE)
d.comment(0xABB3, "Non-negative: store free count to PB", align=Align.INLINE)
d.subroutine(
    0xABB5,
    "osword_13_read_ctx_3",
    title="OSWORD &13 sub 15: read retry counts",
    description="""Returns the three retry count values in
PB[1..3]: PB[1] = transmit retry count
(default &FF = 255), PB[2] = receive poll
count (default &28 = 40), PB[3] = machine
peek retry count (default &0A = 10). Setting
transmit retries to 0 means retry forever.""",
)


d.comment(0xABB5, "Next ctx byte", align=Align.INLINE)
d.comment(0xABB6, "Return", align=Align.INLINE)
d.comment(0xABB9, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xABBB, "Done 3 bytes?", align=Align.INLINE)
d.comment(0xABBD, "No: loop", align=Align.INLINE)
d.comment(0xABBF, "Return", align=Align.INLINE)
d.subroutine(
    0xABC0,
    "osword_13_write_ctx_3",
    title="OSWORD &13 sub 16: write retry counts",
    description="""Sets the three retry count values from
PB[1..3]: PB[1] = transmit retry count,
PB[2] = receive poll count, PB[3] = machine
peek retry count.""",
)


d.comment(0xABC0, "Next byte offset", align=Align.INLINE)
d.comment(0xABC1, "Load PB[Y]", align=Align.INLINE)
d.comment(0xABC3, "Store to tx_retry_count[Y]", align=Align.INLINE)
d.comment(0xABC6, "Done 3 bytes?", align=Align.INLINE)
d.comment(0xABC8, "No: loop", align=Align.INLINE)
d.comment(0xABCA, "Return", align=Align.INLINE)
d.subroutine(
    0xABCB,
    "osword_13_bridge_query",
    title="OSWORD &13 sub 17: query bridge status",
    description="""Calls init_bridge_poll, then returns the
bridge status. If bridge_status is &FF (no bridge),
stores 0 in PB[0]. Otherwise stores bridge_status
in PB[1] and conditionally updates PB[3]
based on station comparison.""",
)


d.comment(0xABCB, "Poll for bridge", align=Align.INLINE)
d.comment(0xABCE, "Y=0", align=Align.INLINE)
d.comment(0xABD0, "Load bridge status", align=Align.INLINE)
d.comment(0xABD3, "Is it &FF (no bridge)?", align=Align.INLINE)
d.comment(0xABD5, "No: bridge found", align=Align.INLINE)
d.comment(0xABD8, "PB[0] = 0 (no bridge)", align=Align.INLINE)
d.label(0xABDD, "bridge_found")

d.comment(0xABDD, "Y=1", align=Align.INLINE)
d.comment(0xABDE, "PB[1] = bridge status", align=Align.INLINE)
d.comment(0xABE0, "Advance Y", align=Align.INLINE)
d.comment(0xABE1, "Y=3", align=Align.INLINE)
d.comment(0xABE2, "Load PB[3] (caller value)", align=Align.INLINE)
d.comment(0xABE4, "Zero: use default station", align=Align.INLINE)
d.label(0xABE6, "compare_bridge_status")

d.comment(0xABE6, "Compare with bridge status", align=Align.INLINE)
# UNMAPPED: d.label(0xABC5, "bridge_err_table")

d.comment(0xABE9, "Non-zero: take return path", align=Align.INLINE)
d.comment(0xABEB, "Same: confirm station", align=Align.INLINE)
d.label(0xABED, "use_default_station")

d.comment(0xABED, "Load default from fs_server_net", align=Align.INLINE)
d.label(0xABF0, "store_bridge_station")

d.comment(0xABF0, "Store to PB[3]", align=Align.INLINE)
d.label(0xABF2, "rts_bridge_query")

d.comment(0xABF2, "Return", align=Align.INLINE)
d.index_base(0xABF3, "bridge_txcb_init_table")

for i in range(4):
    d.byte(0xABF3 + i)

d.comment(0xABF3, "TX 0: ctrl = &82 (immediate mode)", align=Align.INLINE)
d.comment(0xABF4, "TX 1: port = &9C (bridge discovery)", align=Align.INLINE)
d.comment(0xABF5, "TX 2: dest station = &FF (broadcast)", align=Align.INLINE)
d.comment(0xABF6, "TX 3: dest network = &FF (all nets)", align=Align.INLINE)
d.comment(0xABF7, "TX 4-9: immediate data payload", align=Align.INLINE)
d.comment(0xABFE, "TX 11: &00 (terminator)", align=Align.INLINE)
d.label(0xABFF, "bridge_rxcb_init_data")
d.comment(0xABFF, "RX 0: ctrl = &7F (receive)", align=Align.INLINE)
d.comment(0xAC00, "RX 1: port = &9C (bridge discovery)", align=Align.INLINE)
d.comment(0xAC01, "RX 2: station = &00 (any)", align=Align.INLINE)
d.comment(0xAC02, "RX 3: network = &00 (any)", align=Align.INLINE)
d.comment(0xAC05, "RX 6: extended addr fill (&FF)", align=Align.INLINE)
d.comment(0xAC06, "RX 7: extended addr fill (&FF)", align=Align.INLINE)
d.comment(0xAC08, "RX 9: buf end hi (&0D) -> &0D74", align=Align.INLINE)
d.label(0xAC0B, "init_bridge_poll")

d.subroutine(
    0xAC0B,
    "init_bridge_poll",
    title="Initialise Econet bridge routing table",
    description="""Checks the bridge status byte: if &FF
(uninitialised), broadcasts a bridge query
packet and polls for replies. Each reply
adds a network routing entry to the bridge
table. Skips the broadcast if the table has
already been populated from a previous call.""",
    on_exit={"a, x, y": "clobbered when the broadcast path runs"},
)


d.comment(0xAC0B, "Check bridge status", align=Align.INLINE)
d.comment(0xAC0E, "Is it &FF (uninitialised)?", align=Align.INLINE)
d.comment(0xAC10, "No: bridge already active, return", align=Align.INLINE)
d.comment(0xAC12, "Save Y", align=Align.INLINE)
d.comment(0xAC13, "Preserve Y on stack", align=Align.INLINE)
d.comment(0xAC14, "Y=&18: workspace offset for init", align=Align.INLINE)
d.comment(0xAC16, "X=&0B: 12 bytes to copy", align=Align.INLINE)
d.comment(0xAC18, "Rotate econet_flags right (save flag)", align=Align.INLINE)
d.label(0xAC1B, "loop_copy_bridge_init")

d.comment(0xAC1B, "Load init data byte", align=Align.INLINE)
d.comment(0xAC1E, "Store to workspace", align=Align.INLINE)
d.comment(0xAC20, "Load TXCB template byte", align=Align.INLINE)
d.comment(0xAC23, "Store to TX control block", align=Align.INLINE)
d.comment(0xAC25, "Next workspace byte", align=Align.INLINE)
d.comment(0xAC26, "Next template byte", align=Align.INLINE)
d.comment(0xAC27, "Loop for all 12 bytes", align=Align.INLINE)
d.comment(0xAC29, "Store X (-1) as bridge counter", align=Align.INLINE)
d.comment(0xAC2C, "Restore econet_flags flag", align=Align.INLINE)
d.label(0xAC2F, "loop_wait_ws_status")

d.comment(0xAC2F, "Shift ws_0d60 left (check status)", align=Align.INLINE)
d.comment(0xAC32, "C=0: status clear, retry", align=Align.INLINE)
d.comment(0xAC34, "Control byte &82 for TX", align=Align.INLINE)
d.comment(0xAC36, "Set in TX control block", align=Align.INLINE)
d.comment(0xAC38, "Data block at &00C0", align=Align.INLINE)
d.comment(0xAC3A, "Set NMI TX block low", align=Align.INLINE)
d.comment(0xAC3C, "High byte = 0 (page 0)", align=Align.INLINE)
d.comment(0xAC3E, "Set NMI TX block high", align=Align.INLINE)
d.comment(0xAC40, "Begin Econet transmission", align=Align.INLINE)
d.label(0xAC43, "loop_wait_tx_done")

d.comment(0xAC43, "Test TX control block bit 7", align=Align.INLINE)
d.comment(0xAC45, "Negative: TX still in progress", align=Align.INLINE)
d.comment(0xAC47, "Push X (saved across delay)", align=Align.INLINE)
d.comment(0xAC48, "A=&13: OSBYTE 'wait for VSYNC'", align=Align.INLINE)
d.comment(0xAC4D, "Restore caller's X", align=Align.INLINE)
d.comment(0xAC4E, "Y=&18: status-byte offset", align=Align.INLINE)
d.comment(0xAC50, "Load bridge response", align=Align.INLINE)
d.comment(0xAC52, "Negative: bridge responded", align=Align.INLINE)
d.comment(0xAC54, "Advance retry counter by 8", align=Align.INLINE)
d.comment(0xAC57, "Positive: retry poll loop", align=Align.INLINE)
d.label(0xAC59, "bridge_responded")

d.comment(0xAC59, "Set response to &3F (OK)", align=Align.INLINE)
d.comment(0xAC5B, "Store to workspace", align=Align.INLINE)
d.comment(0xAC5D, "Restore saved Y", align=Align.INLINE)
d.comment(0xAC5E, "Result byte to Y", align=Align.INLINE)
d.comment(0xAC5F, "Load bridge status", align=Align.INLINE)
d.comment(0xAC62, "X = bridge status", align=Align.INLINE)
d.comment(0xAC63, "Invert (presence -> absence)", align=Align.INLINE)
d.comment(0xAC65, "Status was &FF: return (no bridge)", align=Align.INLINE)
d.comment(0xAC67, "Return bridge station in A", align=Align.INLINE)
d.label(0xAC68, "rts_bridge_poll")

d.comment(0xAC68, "Return", align=Align.INLINE)
d.label(0xAC69, "osword_14_handler")

d.subroutine(
    0xAC69,
    "osword_14_handler",
    title="OSWORD &14 handler: bridge poll / station status",
    description="""Triages by `A`: `A >= 1` branches via `BCS` to
[`handle_tx_request`](label:handle_tx_request) which reads the station and
network from `PB[1]`/`PB[2]` into the RX-block destination slots
and falls through to the burst-transfer body. `A = 0` (the
bridge-poll sub-code) falls through here: pushes `A`, calls
[`ensure_fs_selected`](label:ensure_fs_selected) to bring ANFS up if needed,
pulls `A` back, sets `Y=&23` and calls
[`mask_owner_access`](label:mask_owner_access) to clear FS-selection bits,
then runs the bridge-poll body.""",
    on_entry={"a": "OSWORD &14 sub-function code", "x, y": "OSWORD parameter block pointer (low, high)"},
)


d.entry(0xAC69)
d.comment(0xAC69, "Compare sub-code with 1", align=Align.INLINE)
d.comment(0xAC6B, "Sub-code >= 1: handle TX request", align=Align.INLINE)
d.comment(0xAC6D, "Save state", align=Align.INLINE)
d.comment(0xAC6E, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.comment(0xAC71, "Pop saved A from the stack frame", align=Align.INLINE)
d.comment(0xAC72, "Y=&23: workspace offset for params", align=Align.INLINE)
d.comment(0xAC74, "Set owner access mask", align=Align.INLINE)
d.label(0xAC77, "loop_copy_txcb_init")

d.comment(0xAC77, "Load TXCB init byte", align=Align.INLINE)
d.comment(0xAC7A, "Non-zero: use template value", align=Align.INLINE)
d.comment(0xAC7C, "Zero: use workspace default value", align=Align.INLINE)
d.label(0xAC7F, "store_txcb_init_byte")

d.comment(0xAC7F, "Store to workspace", align=Align.INLINE)
d.comment(0xAC81, "Next byte down", align=Align.INLINE)
d.comment(0xAC82, "Until Y reaches &17", align=Align.INLINE)
d.comment(0xAC84, "Loop for all bytes", align=Align.INLINE)
d.comment(0xAC86, "Next byte", align=Align.INLINE)
d.comment(0xAC87, "Set net_tx_ptr low byte", align=Align.INLINE)
d.label(0xAC89, "store_osword_pb_ptr")

d.subroutine(
    0xAC89,
    "store_osword_pb_ptr",
    title="Store workspace pointer+1 to NFS workspace",
    description="""Computes ws_ptr_hi + 1 and stores the resulting
16-bit address at workspace offset &1C via
store_ptr_at_ws_y. Then reads PB byte 1 (the
transfer length) and adds ws_ptr_hi to compute
the buffer end pointer, stored at workspace
offset &20.""",
)


d.comment(0xAC89, "Y=&1C: workspace offset for PB pointer", align=Align.INLINE)
d.comment(0xAC8B, "Load PB page number", align=Align.INLINE)
d.comment(0xAC8D, "PB starts at next page boundary (+1)", align=Align.INLINE)
d.comment(0xAC8F, "Store PB start pointer at ws[&1C]", align=Align.INLINE)
d.comment(0xAC92, "Y=1: PB byte 1 (transfer length)", align=Align.INLINE)
d.comment(0xAC94, "Load transfer length from PB", align=Align.INLINE)
d.comment(0xAC96, "Y=&20: TXCB offset", align=Align.INLINE)
d.comment(0xAC98, "Add PB base for buffer end address", align=Align.INLINE)
d.comment(0xAC9A, "Store PB pointer to workspace", align=Align.INLINE)
d.comment(0xAC9D, "Y=2: parameter offset", align=Align.INLINE)
d.comment(0xAC9F, "Control byte &90", align=Align.INLINE)
d.comment(0xACA1, "Set escapable flag", align=Align.INLINE)
d.comment(0xACA3, "Store control byte to PB", align=Align.INLINE)
d.label(0xACA7, "loop_copy_ws_to_pb")

d.comment(0xACA7, "Load workspace data", align=Align.INLINE)
d.comment(0xACAA, "Store to parameter block", align=Align.INLINE)
d.comment(0xACAC, "Next byte", align=Align.INLINE)
d.comment(0xACAD, "Until Y reaches 7", align=Align.INLINE)
d.comment(0xACAF, "Loop for 3 bytes (Y=4,5,6)", align=Align.INLINE)
d.comment(0xACB1, "Read nfs_workspace_hi", align=Align.INLINE)
d.comment(0xACB3, "Store to net_tx_ptr_hi", align=Align.INLINE)
d.comment(0xACB5, "Enable interrupts", align=Align.INLINE)
d.comment(0xACB8, "Y=&20: workspace offset", align=Align.INLINE)
d.comment(0xACBA, "Set to &FF (pending)", align=Align.INLINE)
d.comment(0xACBC, "Mark send pending in workspace", align=Align.INLINE)
d.comment(0xACBF, "Also mark offset &21", align=Align.INLINE)
d.comment(0xACC1, "Y=&19: control offset", align=Align.INLINE)
d.comment(0xACC3, "Control byte &90", align=Align.INLINE)
d.comment(0xACC5, "Store to workspace", align=Align.INLINE)
d.comment(0xACC7, "Y=&18: RX control offset", align=Align.INLINE)
d.comment(0xACC8, "Control byte &7F", align=Align.INLINE)
d.comment(0xACCA, "Store RX control", align=Align.INLINE)
d.comment(0xACCC, "Wait for TX acknowledgement", align=Align.INLINE)
d.label(0xACCF, "store_ptr_at_ws_y")

d.subroutine(
    0xACCF,
    "store_ptr_at_ws_y",
    title="Store 16-bit pointer at workspace offset Y",
    description="""Writes a 16-bit address to (nfs_workspace)+Y.
The low byte comes from A; the high byte is
computed from table_idx plus carry,
supporting pointer arithmetic across page
boundaries.""",
    on_entry={"a": "pointer low byte", "y": "workspace offset", "c": "carry for high byte addition"},
)


d.comment(0xACCF, "Store address low byte at ws[Y]", align=Align.INLINE)
d.comment(0xACD1, "Advance to high byte offset", align=Align.INLINE)
d.comment(0xACD2, "Load high byte base (table_idx)", align=Align.INLINE)
d.comment(0xACD4, "Add carry for page crossing", align=Align.INLINE)
d.comment(0xACD6, "Store address high byte at ws[Y+1]", align=Align.INLINE)
d.comment(0xACD8, "Return", align=Align.INLINE)
d.label(0xACD9, "handle_tx_request")

d.subroutine(
    0xACD9,
    "handle_tx_request",
    title="Sub-code 0: copy PB station/network into RX block, dispatch burst",
    description="""Sub-code-0 path of [`osword_14_handler`](label:osword_14_handler), reached
via the `BCC handle_tx_request` at `&AC69` when the caller's `A`
is 0. Reads two bytes from the OSWORD parameter block:

| Reg setup | Source     | Stored at        |
| --------- | ---------- | ---------------- |
| `Y=1`     | `PB[1]`    | (parked in `X`)  |
| `Y=2`     | `PB[2]`    | `(net_rx_ptr)+&72` (dest network) |
| `Y=3`     | (saved as `osword_flag` for the next byte read) | |
| `Y=&71`   | `X` (PB[1])| `(net_rx_ptr)+&71` (dest station) |

Wraps the body in `PHP`/`PLP` so the entry flags (carry clear from
the `BCC`) survive the workspace stores; the `BNE` after `PLP`
then dispatches to [`handle_burst_xfer`](label:handle_burst_xfer) when the
caller's `A` was non-zero (a defensive branch -- the `BCC` entry
guarantees `A=0`, but the same body is the entry point
the burst path piggy-backs on).""",
    on_entry={
        "a": "OSWORD &14 sub-function code (caller's A; 0 via the BCC entry from osword_14_handler)",
        "ws_ptr_hi": "OSWORD parameter-block high byte",
    },
)


d.comment(0xACD9, "Save processor flags", align=Align.INLINE)
d.comment(0xACDA, "Y=1: workspace offset", align=Align.INLINE)
d.comment(0xACDC, "Load station number from PB", align=Align.INLINE)
d.comment(0xACDE, "X = station number", align=Align.INLINE)
d.comment(0xACE0, "Load network number from PB", align=Align.INLINE)
d.comment(0xACE2, "Y=3: workspace start offset", align=Align.INLINE)
d.comment(0xACE3, "Store Y as ws_ptr_lo", align=Align.INLINE)
d.comment(0xACE5, "Y=&72: workspace offset for dest", align=Align.INLINE)
d.comment(0xACE7, "Store network to workspace", align=Align.INLINE)
d.comment(0xACE9, "Y=&71", align=Align.INLINE)
d.comment(0xACEA, "A = station (from X)", align=Align.INLINE)
d.comment(0xACEB, "Store station to workspace", align=Align.INLINE)
d.comment(0xACED, "Restore flags from PHP", align=Align.INLINE)
d.comment(0xACEE, "Non-zero sub-code: handle burst", align=Align.INLINE)
d.label(0xACF0, "loop_send_pb_chars")

d.comment(0xACF0, "Load current offset", align=Align.INLINE)
d.comment(0xACF2, "Advance offset for next byte", align=Align.INLINE)
d.comment(0xACF4, "Load next char from PB", align=Align.INLINE)
d.comment(0xACF6, "Zero: end of data, return", align=Align.INLINE)
d.comment(0xACF8, "Y=&7D: workspace pointer offset", align=Align.INLINE)
d.comment(0xACFA, "Store char to RX buffer", align=Align.INLINE)
d.comment(0xACFC, "Save char for later test", align=Align.INLINE)
d.comment(0xACFD, "Init workspace copy for wide xfer", align=Align.INLINE)
d.comment(0xAD00, "Set carry", align=Align.INLINE)
d.comment(0xAD01, "Set bit 7: Tube needs release", align=Align.INLINE)
d.comment(0xAD03, "Enable IRQ and send packet", align=Align.INLINE)
d.label(0xAD06, "loop_bridge_tx_delay")

d.comment(0xAD06, "Delay countdown", align=Align.INLINE)
d.comment(0xAD07, "Loop while X != 0", align=Align.INLINE)
d.comment(0xAD09, "Restore char", align=Align.INLINE)
d.comment(0xAD0A, "Test if char was CR (&0D)", align=Align.INLINE)
d.comment(0xAD0C, "Loop while not CR", align=Align.INLINE)
d.comment(0xAD0E, "CR sent: return", align=Align.INLINE)
d.label(0xAD0F, "handle_burst_xfer")

d.subroutine(
    0xAD0F,
    "handle_burst_xfer",
    title="OSWORD &14 burst-transfer path: extend buffer end and TX",
    description="""Reached from [`handle_tx_request`](label:handle_tx_request)'s `BNE` at
`&ACEE`. Calls [`init_ws_copy_wide`](label:init_ws_copy_wide) to copy the
workspace TXCB template into the wide-mode workspace slot, then
extends the buffer end-byte at `(net_rx_ptr)+&7B` by `3` to
account for the 3-byte burst header before falling through into
[`enable_irq_and_poll`](label:enable_irq_and_poll), which re-enables IRQs and
tail-jumps to [`send_net_packet`](label:send_net_packet).""",
    on_entry={"net_rx_ptr": "set up by handle_tx_request (dest station/network already stored at +&71/&72)"},
)


d.comment(0xAD0F, "Init workspace for wide copy", align=Align.INLINE)
d.comment(0xAD12, "Y=&7B: end-byte offset", align=Align.INLINE)
d.comment(0xAD14, "Load buffer size", align=Align.INLINE)
d.comment(0xAD16, "Add 3 (end-of-buffer adjust)", align=Align.INLINE)
d.comment(0xAD18, "Store adjusted size", align=Align.INLINE)
d.label(0xAD1A, "enable_irq_and_poll")

d.subroutine(
    0xAD1A,
    "enable_irq_and_poll",
    title="Enable interrupts and send Econet packet",
    description="""Executes CLI to re-enable interrupts, then
falls through to send_net_packet. Used after
a sequence that ran with interrupts disabled
to ensure the packet is sent with normal
interrupt handling active.""",
    on_entry={"i flag": "may be set (caller had IRQs off); CLI clears it"},
    on_exit={"i flag": "clear (interrupts enabled)"},
)


d.comment(0xAD1A, "Re-enable IRQs", align=Align.INLINE)
d.comment(0xAD1B, "Send packet and return", align=Align.INLINE)
d.subroutine(
    0xAD1E,
    "netv_handler",
    title="NETV handler: OSWORD dispatch",
    description="""Installed as the NETV handler via `write_vector_entry`. Saves all
registers, reads the OSWORD number from the stack, and dispatches
OSWORDs 0-8 via [`push_osword_handler_addr`](label:push_osword_handler_addr).
OSWORDs `>= 9` are ignored (registers restored, RTS returns to
MOS). The handler's address lives in the extended vector data
area together with the other [`fs_vector_table`](label:fs_vector_table)
entries.""",
    on_entry={
        "a": "OSWORD number (read from stacked A on entry)",
        "x, y": "PB pointer low/high (per OSWORD calling convention)",
    },
    on_exit={"a, x, y, p": "restored from stack"},
)


d.entry(0xAD1E)
d.label(0xAD1E, "netv_handler")

d.comment(0xAD1E, "Save processor flags", align=Align.INLINE)
d.comment(0xAD1F, "Save A", align=Align.INLINE)
d.comment(0xAD20, "Save X", align=Align.INLINE)
d.comment(0xAD21, "Push X", align=Align.INLINE)
d.comment(0xAD22, "Save Y", align=Align.INLINE)
d.comment(0xAD23, "Push Y", align=Align.INLINE)
d.comment(0xAD24, "Get stack pointer", align=Align.INLINE)
d.comment(0xAD25, "Read OSWORD number from stack", align=Align.INLINE)
d.comment(0xAD28, "OSWORD >= 9?", align=Align.INLINE)
d.comment(0xAD2A, "Yes: out of range, restore + return", align=Align.INLINE)
d.comment(0xAD2C, "X = OSWORD number", align=Align.INLINE)
d.comment(0xAD2D, "Push handler address for dispatch", align=Align.INLINE)
d.label(0xAD30, "restore_regs_return")

d.comment(0xAD30, "Restore Y", align=Align.INLINE)
d.comment(0xAD31, "Back to Y", align=Align.INLINE)
d.comment(0xAD32, "Restore X", align=Align.INLINE)
d.comment(0xAD33, "Back to X", align=Align.INLINE)
d.comment(0xAD34, "Restore A", align=Align.INLINE)
d.comment(0xAD35, "Restore flags", align=Align.INLINE)
d.comment(0xAD36, "Return", align=Align.INLINE)
d.label(0xAD37, "push_osword_handler_addr")

d.subroutine(
    0xAD37,
    "push_osword_handler_addr",
    title="Push OSWORD handler address for RTS dispatch",
    description="""Indexes the OSWORD handler dispatch table
using the current OSWORD number to push the
handler's address (hi/lo) onto the stack.
Reloads the OSWORD number from osbyte_a_copy
so the dispatched handler can identify the
specific call.""",
    on_entry={"a": "OSWORD number (0-8) -- table index"},
    on_exit={"a": "OSWORD number (re-loaded for the handler's use)"},
)
d.comment(0xAD37, "Load handler high byte from hi-table column X", align=Align.INLINE)
d.comment(0xAD3A, "Push for the eventual RTS dispatch", align=Align.INLINE)
d.comment(0xAD3B, "Load handler low byte from lo-table column X", align=Align.INLINE)
d.comment(0xAD3E, "Push lo so RTS pulls (lo, hi)+1 -> handler entry", align=Align.INLINE)
d.comment(0xAD3F, "Reload original OSWORD number into A for the handler", align=Align.INLINE)
d.comment(0xAD41, "RTS jumps to handler with A=OSWORD number", align=Align.INLINE)
# UNMAPPED: d.index_base(0xAD20, "netv_dispatch_lo")
# UNMAPPED: d.banner(
# UNMAPPED:     0xAD20,
# UNMAPPED:     title="NETV reason-code dispatch low-byte table (9 entries)",
# UNMAPPED:     description="""Read by [`push_osword_handler_addr`](label:push_osword_handler_addr) as
# UNMAPPED: `LDA &AD20,X`. Paired with the high-byte half at
# UNMAPPED: [`netv_dispatch_hi`](label:netv_dispatch_hi). The wrapper at
# UNMAPPED: [`netv_handler`](label:netv_handler) reads the original A from the MOS
# UNMAPPED: stack frame (`&0103,X` after TSX) and gates 9..&FF away to
# UNMAPPED: [`return_6`](label:return_6) before dispatching reasons 0..8.""",
# UNMAPPED: )
# UNMAPPED: for addr in range(0xAD20, 0xAD29):
# UNMAPPED (orphan body):     d.byte(addr)
# UNMAPPED (orphan body): 
d.index_base(0xAD4B, "netv_dispatch_hi")
d.banner(
    0xAD4B,
    title="NETV reason-code dispatch high-byte table (9 entries)",
    description="""Read by [`push_osword_handler_addr`](label:push_osword_handler_addr) as
`LDA &AD29,X`. The dispatcher pushes the hi byte first then the
lo, so RTS lands on `target` (the table stores `target-1`).""",
)
for addr in range(0xAD4B, 0xAD54):
    d.byte(addr)
d.entry(0xAD54)


d.subroutine(
    0xAD54,
    "osword_4_handler",
    title="OSWORD &04 handler: clear C, send abort",
    description="""Reaches the stack via `TSX`, clears bit 0 of the stacked processor
status (`ROR stack_page_6,X` then `ASL stack_page_6,X` -- a
read-modify cycle that lands the carry-out where bit 0 of the
saved P was), so the caller resumes with `C=0`. Stores the
caller's `Y` into NFS workspace at offset `&DA`, then falls
through to [`tx_econet_abort`](label:tx_econet_abort) with `A=0` to
transmit a clean disconnect packet.""",
    on_entry={"y": "OSWORD parameter byte (saved into nfs_workspace+&DA)"},
)


d.comment(0xAD54, "Read the MOS stack frame holding caller flags", align=Align.INLINE)
d.comment(0xAD55, "Shift carry out of caller P (stack[&106+X])", align=Align.INLINE)
d.comment(0xAD58, "Carry is now cleared in caller P", align=Align.INLINE)
d.comment(0xAD5B, "A = original Y", align=Align.INLINE)
d.comment(0xAD5C, "Y=&DA: workspace osword-4 result offset", align=Align.INLINE)
d.comment(0xAD5E, "Store Y at (nfs_workspace)+&DA", align=Align.INLINE)
d.comment(0xAD60, "A=0: clear A for the abort path", align=Align.INLINE)
d.label(0xAD62, "tx_econet_abort")

d.subroutine(
    0xAD62,
    "tx_econet_abort",
    title="Send Econet abort/disconnect packet",
    description="""Stores the abort code in workspace, configures
the TX control block with control byte &80
(immediate operation flag), and transmits the
abort packet. Used to cleanly disconnect from
a remote station during error recovery.""",
    on_entry={"a": "abort code (stored in workspace before TX)"},
)


d.comment(0xAD62, "Y=&D9: workspace offset for the abort code byte", align=Align.INLINE)
d.comment(0xAD64, "Store the abort code (passed in A) at workspace[&D9]", align=Align.INLINE)
d.comment(0xAD66, "A=&80: control = immediate-operation flag", align=Align.INLINE)
d.comment(0xAD68, "Y=&0C: TXCB control-byte offset", align=Align.INLINE)
d.comment(0xAD6A, "Set TXCB[&0C] = &80 (immediate / abort)", align=Align.INLINE)
d.comment(0xAD6C, "Save current net_tx_ptr low (we'll repoint TX at the abort packet)", align=Align.INLINE)
d.comment(0xAD6E, "Push it for restore on exit", align=Align.INLINE)
d.comment(0xAD6F, "Save net_tx_ptr high too", align=Align.INLINE)
d.comment(0xAD71, "Push it", align=Align.INLINE)
d.comment(0xAD72, "TX low = &0C (abort packet starts at workspace[&0C])", align=Align.INLINE)
d.comment(0xAD74, "Get nfs_workspace high byte", align=Align.INLINE)
d.comment(
    0xAD76, "TX high = workspace page (so net_tx_ptr now points at the abort packet in workspace)", align=Align.INLINE
)
d.comment(0xAD78, "Send the abort packet via the standard TX path", align=Align.INLINE)
d.comment(0xAD7B, "A=&3F: TXCB status = abort-complete sentinel", align=Align.INLINE)
d.comment(0xAD7D, "Write status via (net_tx_ptr,X) -- mark TX done", align=Align.INLINE)
d.comment(0xAD7F, "Pull saved net_tx_ptr high", align=Align.INLINE)
d.comment(0xAD80, "Restore", align=Align.INLINE)
d.comment(0xAD82, "Pull saved net_tx_ptr low", align=Align.INLINE)
d.comment(0xAD83, "Restore -- caller's TX state intact", align=Align.INLINE)
d.comment(0xAD85, "Return", align=Align.INLINE)
d.label(0xAD86, "netv_claim_release")

d.subroutine(
    0xAD86,
    "netv_claim_release",
    title="OSWORD 7 handler: claim/release network resources",
    description="""Handles OSWORD 7 (SOUND) intercepted via NETV.
Searches the claim code table in two passes:
first 11 entries (state 2), then all 18 (state
3). On match, saves 3 tube state bytes to
workspace and sends an abort with the state
code. For state 3 matches, also polls workspace
for a response and restores the caller's stack
frame from the saved bytes.""",
    on_entry={"a": "OSWORD 7 number (validated by caller)"},
)


d.comment(
    0xAD86,
    "Y = OSWORD parameter-block pointer high byte (used as an 'unrecognised' sentinel below)",
    align=Align.INLINE,
)
d.entry(0xAD86)
d.comment(0xAD88, "Code &81? (compatibility shortcut for one specific claim type)", align=Align.INLINE)
d.comment(0xAD8A, "Yes: skip table scan, use match-result with Y already set non-zero", align=Align.INLINE)
d.comment(0xAD8C, "Y=1: state 2 marker", align=Align.INLINE)
d.comment(0xAD8E, "X=&0A: scan first 11 entries (table indices 0..&0A)", align=Align.INLINE)
d.comment(0xAD90, "Look up A in the claim code table", align=Align.INLINE)
d.comment(0xAD93, "Match: handle as state 2", align=Align.INLINE)
d.comment(0xAD95, "DEY: Y=0 (state 3 marker, two DEYs from 1)", align=Align.INLINE)
d.comment(0xAD96, "Y=-1: flag second range", align=Align.INLINE)
d.comment(0xAD97, "X=&11: scan all 18 entries (state 3 also accepts the extended range)", align=Align.INLINE)
d.comment(0xAD99, "Look up A again with extended range", align=Align.INLINE)
d.comment(0xAD9C, "Match: handle as state 3", align=Align.INLINE)
d.comment(0xAD9E, "Y=1 again (no match found, will return below)", align=Align.INLINE)
d.label(0xAD9F, "process_match_result")

d.comment(0xAD9F, "X=2: default state code passed to tx_econet_abort", align=Align.INLINE)
d.comment(0xADA1, "Move match marker (Y) into A for the BEQ test", align=Align.INLINE)
d.comment(0xADA2, "Y=0 (no match): return without action", align=Align.INLINE)
d.comment(0xADA4, "Save flags so we can branch later on Y's sign", align=Align.INLINE)
d.comment(0xADA5, "Y > 0 (state 2): skip the X bump", align=Align.INLINE)
d.comment(0xADA7, "State 3: X=3 (different abort code)", align=Align.INLINE)
d.label(0xADA8, "save_tube_state")

d.comment(0xADA8, "Y=&DC: workspace offset for tube state bytes", align=Align.INLINE)
d.label(0xADAA, "loop_save_tube_bytes")

d.comment(0xADAA, "Read tube_claimed_id,Y", align=Align.INLINE)
d.comment(0xADAD, "Save in workspace[&DC..]", align=Align.INLINE)
d.comment(0xADAF, "Step backwards", align=Align.INLINE)
d.comment(0xADB0, "Done at &DA?", align=Align.INLINE)
d.comment(0xADB2, "Loop while Y > &DA (saves &DA, &DB, &DC -- 3 bytes)", align=Align.INLINE)
d.comment(0xADB4, "Move state code (2 or 3) into A for the abort", align=Align.INLINE)
d.comment(0xADB5, "Send abort with the state code", align=Align.INLINE)
d.comment(0xADB8, "Restore the saved flags (Y's sign)", align=Align.INLINE)
d.comment(0xADB9, "Y was positive (state 2): just return", align=Align.INLINE)
d.comment(0xADBB, "A=&7F: 'pending response' control value", align=Align.INLINE)
d.comment(0xADBD, "Y=&0C: TXCB control offset", align=Align.INLINE)
d.comment(0xADBF, "Mark TXCB as pending", align=Align.INLINE)
d.label(0xADC1, "loop_poll_ws_status")

d.comment(0xADC1, "Read TXCB status byte", align=Align.INLINE)
d.comment(0xADC3, "Bit 7 still clear: keep polling for response", align=Align.INLINE)
d.comment(0xADC5, "Capture S so we can patch the caller's stack frame", align=Align.INLINE)
d.comment(0xADC6, "Y=&DD: highest workspace offset for the response copy", align=Align.INLINE)
d.comment(0xADC8, "Read first response byte (workspace[&DD])", align=Align.INLINE)
d.comment(0xADCA, "Set bit 6 and bit 2", align=Align.INLINE)
d.comment(
    0xADCC, "Always taken (after ORA result is non-zero); store into stack[&106+X] then walk down", align=Align.INLINE
)
d.label(0xADCE, "loop_restore_stack")

d.comment(0xADCE, "Step Y down", align=Align.INLINE)
d.comment(0xADCF, "Step X down (stack offset)", align=Align.INLINE)
d.comment(0xADD0, "Read next workspace byte", align=Align.INLINE)
d.label(0xADD2, "store_stack_byte")

d.comment(0xADD2, "Patch caller's stack frame at &106+X", align=Align.INLINE)
d.comment(0xADD5, "Reached &DA (lower workspace bound)?", align=Align.INLINE)
d.comment(0xADD7, "No: keep restoring", align=Align.INLINE)
d.label(0xADD9, "rts_claim_release")

d.comment(0xADD9, "Return", align=Align.INLINE)
d.subroutine(
    0xADDA,
    "match_rx_code",
    title="Search receive code table for match",
    description="""Scans a table of receive operation codes
starting at index X, comparing each against A.
Returns with Z set if a match is found, Z clear
if the end-of-table marker is reached.""",
    on_entry={"a": "receive code to match", "x": "starting table index"},
    on_exit={"z": "set if match found"},
)


d.comment(0xADDA, "Compare A with table entry at index X", align=Align.INLINE)
d.comment(0xADDD, "Match: return with Z set", align=Align.INLINE)
d.comment(0xADDF, "Step to next earlier table entry", align=Align.INLINE)
d.comment(0xADE0, "Loop while X >= 0 (table walked top-down)", align=Align.INLINE)
d.label(0xADE2, "rts_match_rx_code")

d.comment(0xADE2, "Return; Z reflects last CMP", align=Align.INLINE)
d.index_base(0xADE3, "osword_claim_codes")
d.banner(
    0xADE3,
    title="OSWORD per-claim-code lookup table (18 bytes)",
    description="""Looked up by [`match_rx_code`](label:match_rx_code) when an Econet RX
event triggers an OSWORD-related claim. The X register selects an
18-byte slice; bytes encode the claim type (immediate-op,
broadcast, port-specific) used by the dispatcher to decide which
handler chain to install. Per-byte inline comments document each
entry.""",
)
for i in range(18):
    d.byte(0xADE3 + i)

d.comment(0xADE3, "Range 1+2: OSWORD &04", align=Align.INLINE)
d.comment(0xADE4, "Range 1+2: OSWORD &09", align=Align.INLINE)
d.comment(0xADE6, "Range 1+2: OSWORD &14", align=Align.INLINE)
d.comment(0xADE7, "Range 1+2: OSWORD &15", align=Align.INLINE)
d.comment(0xADE9, "Range 1+2: OSWORD &9B", align=Align.INLINE)
d.comment(0xADEA, "Range 1+2: OSWORD &E1", align=Align.INLINE)
d.comment(0xADEC, "Range 1+2: OSWORD &E3", align=Align.INLINE)
d.comment(0xADED, "Range 1+2: OSWORD &E4", align=Align.INLINE)
d.comment(0xADEF, "Range 2 only: OSWORD &0C", align=Align.INLINE)
d.comment(0xADF0, "Range 2 only: OSWORD &0F", align=Align.INLINE)
d.comment(0xADF1, "Range 2 only: OSWORD &79", align=Align.INLINE)
d.comment(0xADF4, "Range 2 only: OSWORD &87", align=Align.INLINE)
d.subroutine(
    0xADF5,
    "osword_8_handler",
    title="OSWORD 7/8 handler: copy PB to workspace and abort",
    description="""Handles OSWORD 7 or 8 by copying 15 bytes from
the parameter block to workspace at offset &DB,
storing the OSWORD number at offset &DA, setting
control value &E9, and sending an abort packet.
Returns via tx_econet_abort. Rejects other
OSWORD numbers by returning immediately.""",
    on_entry={"a": "OSWORD number (must be 7 or 8 to be processed)"},
)


d.comment(0xADF5, "Y=&0E: scan 15 bytes (offsets 14..0) of the PB", align=Align.INLINE)
d.comment(0xADF7, "Is the OSWORD number 7?", align=Align.INLINE)
d.comment(0xADF9, "Yes: handle as either 7 or 8 -- both copy PB to ws", align=Align.INLINE)
d.comment(0xADFB, "Is the OSWORD number 8?", align=Align.INLINE)
d.comment(0xADFD, "Neither 7 nor 8: return early (other OSWORDs handled elsewhere)", align=Align.INLINE)
d.label(0xADFF, "copy_pb_to_ws")

d.comment(0xADFF, "X=&DB: workspace offset for the PB copy", align=Align.INLINE)
d.comment(
    0xAE01,
    "Temporarily reuse nfs_workspace as the destination low byte (high byte already points at the workspace page)",
    align=Align.INLINE,
)
d.label(0xAE03, "loop_copy_pb_to_ws")

d.comment(0xAE03, "Read PB[Y]", align=Align.INLINE)
d.comment(0xAE05, "Write to (nfs_workspace),Y -- effectively writes to workspace[&DB+Y]", align=Align.INLINE)
d.comment(0xAE07, "Step backwards through the 15 bytes", align=Align.INLINE)
d.comment(0xAE08, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xAE0A, "Bring Y back to 0 for the next single-byte write", align=Align.INLINE)
d.comment(
    0xAE0B,
    "Decrement nfs_workspace low byte: now points at workspace[&DA] (one before the copied region)",
    align=Align.INLINE,
)
d.comment(0xAE0D, "Read original OSWORD number from osbyte_a_copy", align=Align.INLINE)
d.comment(0xAE0F, "Store at workspace[&DA] -- so the abort packet header carries the OSWORD number", align=Align.INLINE)
d.comment(0xAE11, "Restore nfs_workspace to its proper low byte (Y=0)", align=Align.INLINE)
d.comment(0xAE13, "Y=&14: TXCB control offset", align=Align.INLINE)
d.comment(0xAE15, "A=&E9: status code for OSWORD-passthrough abort", align=Align.INLINE)
d.comment(0xAE17, "Store status at TXCB[&14]", align=Align.INLINE)
d.comment(0xAE19, "A=1: abort code for tx_econet_abort", align=Align.INLINE)
d.comment(0xAE1B, "Send the abort packet", align=Align.INLINE)
d.comment(0xAE1E, "Restore nfs_workspace from X (X is unchanged across tx_econet_abort)", align=Align.INLINE)
d.label(0xAE20, "init_ws_copy_wide")

d.subroutine(
    0xAE20,
    "init_ws_copy_wide",
    title="Initialise workspace copy in wide mode (14 bytes)",
    description="""Copies 14 bytes to workspace offset &7C.
Falls through to the template-driven copy
loop which handles &FD (skip), &FE (end),
and &FC (page pointer) markers.""",
    on_entry={"x": "template source offset (within ws_txcb_template_data)"},
)


d.comment(0xAE20, "X=&0D: 14 template bytes to process", align=Align.INLINE)
d.comment(0xAE22, "Y=&7C: workspace destination offset for wide variant", align=Align.INLINE)
d.comment(0xAE24, "BIT &FF unconditionally sets V (the always_set_v_byte trick)", align=Align.INLINE)
d.comment(0xAE27, "V=1 always: skip the narrow-mode prologue and CLV", align=Align.INLINE)
d.label(0xAE29, "init_ws_copy_narrow")

d.subroutine(
    0xAE29,
    "init_ws_copy_narrow",
    title="Initialise workspace copy in narrow mode (27 bytes)",
    description="""Sets up a 27-byte copy to workspace offset &17,
then falls through to ws_copy_vclr_entry for
the template-driven copy loop. Used for the
compact workspace initialisation variant.""",
    on_entry={"x": "template source offset"},
)


d.comment(0xAE29, "Y=&17: workspace destination offset for narrow variant", align=Align.INLINE)
d.comment(0xAE2B, "X=&1A: 27 template bytes to process; fall into ws_copy_vclr_entry which CLVs", align=Align.INLINE)
d.label(0xAE2D, "ws_copy_vclr_entry")

d.subroutine(
    0xAE2D,
    "ws_copy_vclr_entry",
    title="Template-driven workspace copy with V clear",
    description="""Processes a template byte array to initialise
workspace. Special marker bytes: &FE terminates
the copy, &FD skips the current offset, and &FC
substitutes the workspace page pointer. All
other values are stored directly to the
workspace at the current offset.""",
    on_entry={
        "x": "template source offset",
        "y": "destination offset within NFS workspace",
        "v flag": "clear (controls a downstream branch in the shared body; init_ws_copy_wide / _narrow enter with V=0)",
    },
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xAE2D, "Clear V: narrow mode (writes via nfs_workspace pointer)", align=Align.INLINE)
d.label(0xAE2E, "loop_copy_ws_template")

d.comment(0xAE2E, "Read next template byte", align=Align.INLINE)
d.comment(0xAE31, "&FE: end-of-template marker?", align=Align.INLINE)
d.comment(0xAE33, "Yes: finalise and return", align=Align.INLINE)
d.comment(0xAE35, "&FD: skip-this-offset marker?", align=Align.INLINE)
d.comment(0xAE37, "Yes: advance index without storing", align=Align.INLINE)
d.comment(0xAE39, "&FC: substitute-workspace-page-pointer marker?", align=Align.INLINE)
d.comment(0xAE3B, "No special marker: store this byte verbatim", align=Align.INLINE)
d.comment(0xAE3D, "Wide path: page pointer is net_rx_ptr's high byte", align=Align.INLINE)
d.comment(0xAE3F, "V=1 (wide): keep the rx_ptr high byte", align=Align.INLINE)
d.comment(0xAE41, "V=0 (narrow): use nfs_workspace high byte instead", align=Align.INLINE)
d.label(0xAE43, "store_tx_ptr_hi")

d.comment(0xAE43, "Stash whichever page byte we picked into net_tx_ptr_hi", align=Align.INLINE)
d.label(0xAE45, "select_store_target")

d.comment(0xAE45, "V=1 (wide): store via net_rx_ptr,Y", align=Align.INLINE)
d.comment(0xAE47, "V=0 (narrow): store via nfs_workspace,Y", align=Align.INLINE)
d.comment(0xAE49, "Always branch: V is still clear here", align=Align.INLINE)
d.label(0xAE4B, "store_via_rx_ptr")

d.comment(0xAE4B, "Wide-mode store via net_rx_ptr", align=Align.INLINE)
d.label(0xAE4D, "advance_template_idx")

d.comment(0xAE4D, "Step Y down (workspace offset)", align=Align.INLINE)
d.comment(0xAE4E, "Step X down (template index)", align=Align.INLINE)
d.comment(0xAE4F, "Loop while X >= 0", align=Align.INLINE)
d.label(0xAE51, "done_ws_template_copy")

d.comment(0xAE51, "Bump Y back to first written offset", align=Align.INLINE)
d.comment(0xAE52, "Save it as net_tx_ptr low for the caller", align=Align.INLINE)
d.comment(0xAE54, "Return", align=Align.INLINE)
d.index_base(0xAE55, "ws_txcb_template_data")
d.banner(
    0xAE55,
    title="Workspace TXCB template (39 bytes, three overlapping regions)",
    description="""Three overlapping copy regions indexed by different callers:

| Caller | X / Y / V | Range | Destination |
|---|---|---|---|
| Wide   | `X=&0D`, `Y=&7C`, `V=1` | bytes 0..13  | `ws+&6F..&7C` via `net_rx_ptr` |
| Narrow | `X=&1A`, `Y=&17`, `V=0` | bytes 14..26 | `ws+&0C..&17` via `nfs_workspace` |
| Vclr   | `X=&26`, `Y=&20`, `V=0` | bytes 27..38 | `ws+&15..&20` via `nfs_workspace` |

Per-byte inline comments below describe each entry's role in the
TXCB it ends up in.""",
)
for i in range(39):
    d.byte(0xAE55 + i)

d.comment(0xAE55, "Wide &6F: ctrl=&85", align=Align.INLINE)
d.comment(0xAE57, "Wide &71: skip (dest station)", align=Align.INLINE)
d.comment(0xAE5A, "Wide &74: buf start hi=page ptr", align=Align.INLINE)
d.comment(0xAE5B, "Wide &75: buf start ext lo", align=Align.INLINE)
d.comment(0xAE5C, "Wide &76: buf start ext hi", align=Align.INLINE)
d.comment(0xAE5D, "Wide &77: buf end lo=&7E", align=Align.INLINE)
d.comment(0xAE60, "Wide &7A: buf end ext hi", align=Align.INLINE)
d.comment(0xAE61, "Wide &7B: zero", align=Align.INLINE)
d.comment(0xAE62, "Wide &7C: zero", align=Align.INLINE)
d.comment(0xAE63, "Narrow stop (&FE terminator)", align=Align.INLINE)
d.comment(0xAE66, "Narrow &0E: skip (dest station)", align=Align.INLINE)
d.comment(0xAE69, "Narrow &11: buf start hi=page ptr", align=Align.INLINE)
d.comment(0xAE6A, "Narrow &12: buf start ext lo", align=Align.INLINE)
d.comment(0xAE6B, "Narrow &13: buf start ext hi", align=Align.INLINE)
d.comment(0xAE6C, "Narrow &14: buf end lo=&DE", align=Align.INLINE)
d.comment(0xAE6F, "Narrow &17: buf end ext hi", align=Align.INLINE)
d.comment(0xAE70, "Spool stop (&FE terminator)", align=Align.INLINE)
d.comment(0xAE73, "Spool &03: skip (dest network)", align=Align.INLINE)
d.comment(0xAE76, "Spool &06: buf start ext lo", align=Align.INLINE)
d.comment(0xAE77, "Spool &07: buf start ext hi", align=Align.INLINE)
d.comment(0xAE78, "Spool &08: skip (buf end lo)", align=Align.INLINE)
d.comment(0xAE7B, "Spool &0B: buf end ext hi", align=Align.INLINE)
d.label(0xAE7C, "netv_spool_check")

d.subroutine(
    0xAE7C,
    "netv_spool_check",
    title="OSWORD 5 handler: check spool PB and reset buffer",
    description="""Handles OSWORD 5 intercepted via NETV. Checks
if X-1 matches osword_pb_ptr and bit 0 of
&00D0 is clear. If both conditions are met,
falls through to reset_spool_buf_state to
reinitialise the spool buffer for new data.""",
    on_entry={"x": "OSWORD parameter block low byte (X-1 compared against osword_pb_ptr)"},
)


d.comment(0xAE7C, "Step counter", align=Align.INLINE)
d.comment(0xAE7D, "Match osword_pb_ptr?", align=Align.INLINE)
d.comment(0xAE7F, "No: return (not our PB)", align=Align.INLINE)
d.comment(0xAE81, "Load spool state byte", align=Align.INLINE)
d.comment(0xAE83, "Shift bit 0 into C", align=Align.INLINE)
d.comment(0xAE84, "C=1: already active, return", align=Align.INLINE)
d.label(0xAE86, "reset_spool_buf_state")

d.subroutine(
    0xAE86,
    "reset_spool_buf_state",
    title="Reset spool buffer to initial state",
    description="""Sets the spool buffer pointer (`spool_buf_idx`)
to `&21` and the control byte (`ws_0d6a`) to `&41`
(ready for new data). Called after processing a
complete spool data block.""",
    on_entry={},
    on_exit={"a, y": "clobbered"},
)


d.comment(0xAE86, "Buffer start offset = &21", align=Align.INLINE)
d.comment(0xAE88, "Store as buffer pointer", align=Align.INLINE)
d.comment(0xAE8B, "Control state &41", align=Align.INLINE)
d.comment(0xAE8D, "Store as spool control state", align=Align.INLINE)
d.label(0xAE90, "rts_spool_reset")

d.comment(0xAE90, "Return", align=Align.INLINE)
d.label(0xAE91, "netv_print_data")

d.subroutine(
    0xAE91,
    "netv_print_data",
    title="OSWORD 1-3 handler: drain printer buffer",
    description="""Handles OSWORDs 1-3 intercepted via NETV.
When X=1, drains the printer buffer (OSBYTE
&91, buffer 3) into the receive buffer, sending
packets via process_spool_data when the buffer
exceeds &6E bytes. When X>1, routes to
handle_spool_ctrl_byte for spool state control.""",
    on_entry={"x": "1 = drain printer buffer; >1 = control byte path"},
)


d.entry(0xAE91)
d.comment(0xAE91, "Check Y == 4", align=Align.INLINE)
d.comment(0xAE93, "Non-zero: nothing to print, return", align=Align.INLINE)
d.comment(0xAE95, "A = X (control byte)", align=Align.INLINE)
d.comment(0xAE96, "Step counter back", align=Align.INLINE)
d.comment(0xAE97, "Non-zero: handle spool ctrl byte", align=Align.INLINE)
d.comment(0xAE99, "Read MOS stack frame", align=Align.INLINE)
d.comment(0xAE9A, "OR with stack value", align=Align.INLINE)
d.comment(0xAE9D, "Store back to stack", align=Align.INLINE)
d.label(0xAEA0, "loop_drain_printer_buf")

d.comment(0xAEA0, "OSBYTE &91: read buffer", align=Align.INLINE)
d.comment(0xAEA2, "X=3: printer buffer", align=Align.INLINE)
d.comment(0xAEA4, "Read character from buffer", align=Align.INLINE)
d.comment(0xAEA7, "C set: return path", align=Align.INLINE)
d.comment(0xAEA9, "A = extracted character", align=Align.INLINE)
d.comment(0xAEAA, "Add byte to RX buffer", align=Align.INLINE)
d.comment(0xAEAD, "Buffer past &6E limit?", align=Align.INLINE)
d.comment(0xAEAF, "No: read more from buffer", align=Align.INLINE)
d.comment(0xAEB1, "Print accumulated spool data", align=Align.INLINE)
d.comment(0xAEB4, "More room: continue reading", align=Align.INLINE)
d.label(0xAEB6, "append_byte_to_rxbuf")

d.subroutine(
    0xAEB6,
    "append_byte_to_rxbuf",
    title="Append byte to receive buffer",
    description="""Stores A in the receive buffer at the current
buffer index (ws_ptr_lo), then increments the
index. Used to accumulate incoming spool data
bytes before processing.""",
    on_entry={"a": "byte to append"},
)


d.comment(0xAEB6, "Y = spool_buf_idx", align=Align.INLINE)
d.comment(0xAEB9, "Store A at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAEBB, "Advance spool_buf_idx", align=Align.INLINE)
d.comment(0xAEBE, "Return", align=Align.INLINE)
d.label(0xAEBF, "handle_spool_ctrl_byte")

d.subroutine(
    0xAEBF,
    "handle_spool_ctrl_byte",
    title="Handle spool control byte and flush buffer",
    description="""Rotates bit 0 of the control byte into carry
for mode selection (print vs spool), appends
the byte to the buffer, calls process_spool_data
to transmit the accumulated data, and resets
the buffer state ready for the next block.""",
    on_entry={"a": "control byte (bit 0 selects mode: 0 = print, 1 = spool)"},
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xAEBF, "Rotate bit 0 into carry", align=Align.INLINE)
d.comment(0xAEC0, "C clear: take check_spool_state path", align=Align.INLINE)
d.comment(0xAEC2, "Load spool control state", align=Align.INLINE)
d.comment(0xAEC4, "Equal: take fill path", align=Align.INLINE)
d.comment(0xAEC5, "Save state byte", align=Align.INLINE)
d.comment(0xAEC6, "Rotate bit 0 into carry", align=Align.INLINE)
d.comment(0xAEC7, "Restore state", align=Align.INLINE)
d.comment(0xAEC8, "C=1: already started, reset", align=Align.INLINE)
d.comment(0xAECA, "Set bits 0-1 (active + pending)", align=Align.INLINE)
d.comment(0xAECC, "Store updated state", align=Align.INLINE)
d.comment(0xAECE, "Stop: process_spool_data and return", align=Align.INLINE)
d.comment(0xAECF, "A=3: spool-data result code", align=Align.INLINE)
d.comment(0xAED1, "Append result to RX buffer", align=Align.INLINE)
d.comment(0xAED4, "Process the accumulated spool data", align=Align.INLINE)
d.label(0xAED7, "done_spool_ctrl")

d.comment(0xAED7, "Reset spool buffer state", align=Align.INLINE)
d.subroutine(
    0xAEDA,
    "process_spool_data",
    title="Transmit accumulated spool buffer data",
    description="""Copies the workspace state to the TX control
block, sends a disconnect reply if the previous
transfer requires acknowledgment, then handles
the spool output sequence by setting up and
sending the pass-through TX buffer.""",
    on_exit={"a": "TX result (from setup_pass_txbuf)"},
)


d.comment(0xAEDA, "Y=8: buf_start_lo TXCB offset", align=Align.INLINE)
d.comment(0xAEDC, "Load current spool-buffer index", align=Align.INLINE)
d.comment(0xAEDF, "Store at workspace+8 (buf_start_lo)", align=Align.INLINE)
d.comment(0xAEE1, "Load RX page (= net_rx_ptr_hi)", align=Align.INLINE)
d.comment(0xAEE4, "Store at workspace+9 (buf_start_hi)", align=Align.INLINE)
d.comment(0xAEE6, "Y=5: alt buf_start_hi offset", align=Align.INLINE)
d.comment(0xAEE8, "Store at workspace+5 (also buf-start hi)", align=Align.INLINE)
d.comment(0xAEEA, "Y=&0B: TXCB offset for following copy", align=Align.INLINE)
d.comment(0xAEEC, "X=&26: template offset for vclr region", align=Align.INLINE)
d.comment(0xAEEE, "Copy 12-byte ws-template region (V-clear)", align=Align.INLINE)
d.comment(0xAEF1, "Step back to offset &0A", align=Align.INLINE)
d.comment(0xAEF2, "Read shadow ACR (ws_0d6a)", align=Align.INLINE)
d.comment(0xAEF5, "Save state", align=Align.INLINE)
d.comment(0xAEF6, "Shift bit 7 into C", align=Align.INLINE)
d.comment(0xAEF7, "Restore state", align=Align.INLINE)
d.comment(0xAEF8, "Toggle bit 7", align=Align.INLINE)
d.comment(0xAEFA, "Store updated shadow back to ws_0d6a", align=Align.INLINE)
d.comment(0xAEFD, "Shift bit 0 into bit 1", align=Align.INLINE)
d.comment(0xAEFE, "Store at workspace+&0A", align=Align.INLINE)
d.comment(0xAF00, "Read vdu_status", align=Align.INLINE)
d.comment(0xAF02, "Push for later restore", align=Align.INLINE)
d.comment(0xAF03, "Clear bit 0 of vdu_status", align=Align.INLINE)
d.comment(0xAF05, "Store updated", align=Align.INLINE)
d.comment(0xAF07, "Y=&22: spool_buf_idx reset value", align=Align.INLINE)
d.comment(0xAF09, "Reset spool_buf_idx", align=Align.INLINE)
d.comment(0xAF0C, "A=0", align=Align.INLINE)
d.comment(0xAF0E, "X=0", align=Align.INLINE)
d.comment(0xAF0F, "Y = workspace high page", align=Align.INLINE)
d.comment(0xAF11, "Re-enable IRQs (NMI window over)", align=Align.INLINE)
d.comment(0xAF12, "Send disconnect reply", align=Align.INLINE)
d.comment(0xAF15, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF16, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF18, "Return", align=Align.INLINE)
d.label(0xAF19, "check_spool_state")

d.comment(0xAF19, "Read shadow ACR", align=Align.INLINE)
d.comment(0xAF1C, "Shift bit 0 into C", align=Align.INLINE)
d.comment(0xAF1D, "C clear: re-process spool data", align=Align.INLINE)
d.comment(0xAF1F, "Read vdu_status", align=Align.INLINE)
d.comment(0xAF21, "Push for restore", align=Align.INLINE)
d.comment(0xAF22, "Clear bit 0 of vdu_status", align=Align.INLINE)
d.comment(0xAF24, "Store updated", align=Align.INLINE)
d.comment(0xAF26, "A=&14: TX command byte", align=Align.INLINE)
d.label(0xAF28, "start_spool_retry")

d.comment(0xAF28, "Save TX command", align=Align.INLINE)
d.comment(0xAF29, "X=&0B: tx_econet_txcb_template offset", align=Align.INLINE)
d.comment(0xAF2B, "Y=&2D: dest TXCB offset", align=Align.INLINE)
d.label(0xAF2D, "loop_copy_spool_tx")

d.comment(0xAF2D, "Read template byte at tx_econet_txcb_template+X", align=Align.INLINE)
d.comment(0xAF30, "Store at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAF32, "Decrement Y", align=Align.INLINE)
d.comment(0xAF33, "Decrement X", align=Align.INLINE)
d.comment(0xAF34, "Loop until X wraps below 0", align=Align.INLINE)
d.comment(0xAF36, "Store X (= &FF) as need_release_tube", align=Align.INLINE)
d.comment(0xAF38, "Y=2: workspace offset for source", align=Align.INLINE)
d.comment(0xAF3A, "Read (nfs_workspace)+2", align=Align.INLINE)
d.comment(0xAF3C, "Save station", align=Align.INLINE)
d.comment(0xAF3D, "Y=3", align=Align.INLINE)
d.comment(0xAF3E, "Read (nfs_workspace)+3", align=Align.INLINE)
d.comment(0xAF40, "Y=&25: dest offset in TXCB", align=Align.INLINE)
d.comment(0xAF42, "Store at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAF44, "Y=&23", align=Align.INLINE)
d.comment(0xAF45, "Restore station", align=Align.INLINE)
d.comment(0xAF46, "Store at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAF48, "X=&0B: rx_palette_txcb_template offset", align=Align.INLINE)
d.comment(0xAF4A, "Y=&0B: dest offset in workspace", align=Align.INLINE)
d.label(0xAF4C, "loop_copy_spool_rx")

d.comment(0xAF4C, "Read template byte at rx_palette_txcb_template+X", align=Align.INLINE)
d.comment(0xAF4F, "Compare with &FD (skip-byte marker)", align=Align.INLINE)
d.comment(0xAF51, "Equal: skip this byte", align=Align.INLINE)
d.comment(0xAF53, "Compare with &FC (page-ptr marker)", align=Align.INLINE)
d.comment(0xAF55, "Not &FC: store as-is", align=Align.INLINE)
d.comment(0xAF57, "&FC: substitute net_rx_ptr_hi", align=Align.INLINE)
d.label(0xAF59, "store_spool_rx_byte")

d.comment(0xAF59, "Store at (nfs_workspace)+Y", align=Align.INLINE)
d.label(0xAF5B, "advance_spool_rx_idx")

d.comment(0xAF5B, "Next dest", align=Align.INLINE)
d.comment(0xAF5C, "Next source", align=Align.INLINE)
d.comment(0xAF5D, "Loop until X wraps", align=Align.INLINE)
d.comment(0xAF5F, "A=&22: TXCB control byte", align=Align.INLINE)
d.comment(0xAF61, "Store at net_tx_ptr lo", align=Align.INLINE)
d.comment(0xAF63, "Read net_rx_ptr_hi", align=Align.INLINE)
d.comment(0xAF65, "Store as net_tx_ptr hi", align=Align.INLINE)
d.comment(0xAF67, "Set up the pass-through TX buffer", align=Align.INLINE)
d.comment(0xAF6A, "Send the TX packet", align=Align.INLINE)
d.comment(0xAF6D, "A=0: clear net_tx_ptr lo", align=Align.INLINE)
d.comment(0xAF6F, "Store -> net_tx_ptr lo", align=Align.INLINE)
d.comment(0xAF71, "Read nfs_workspace_hi", align=Align.INLINE)
d.comment(0xAF73, "Store -> net_tx_ptr hi", align=Align.INLINE)
d.comment(0xAF75, "Wait for TX ack", align=Align.INLINE)
d.comment(0xAF78, "Y=&2E: spool result-byte offset", align=Align.INLINE)
d.comment(0xAF7A, "Read result via (net_rx_ptr)+Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF5A, "Z: success path", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF5C, "Compare with 3 (retry threshold)", align=Align.INLINE)
d.comment(0xAF7F, "Other: take retry path", align=Align.INLINE)
d.label(0xAF81, "spool_tx_succeeded")

d.comment(0xAF81, "Discard saved TX cmd", align=Align.INLINE)
d.comment(0xAF82, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF83, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF85, "A=0: success-return code", align=Align.INLINE)
d.comment(0xAF87, "Append byte to RX buffer", align=Align.INLINE)
d.comment(0xAF8A, "Recurse: process_spool_data", align=Align.INLINE)
d.comment(0xAF8D, "Read shadow ACR", align=Align.INLINE)
d.comment(0xAF90, "Mask high nibble", align=Align.INLINE)
d.comment(0xAF92, "Store updated shadow", align=Align.INLINE)
d.comment(0xAF95, "Return", align=Align.INLINE)
# UNMAPPED: d.label(0xAF75, "spool_tx_retry")

# UNMAPPED: d.comment(0xAF75, "Save retry counter", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF76, "Pop saved TX cmd", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF77, "Set carry", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF78, "Decrement retry", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF7A, "Non-zero: retry from start_spool_retry", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF7C, "Check the saved retry counter", align=Align.INLINE)
d.comment(0xAF9B, "Not 1: take printer_busy_msg path", align=Align.INLINE)
d.label(0xAF9D, "err_printer_busy")

d.subroutine(
    0xAF9D,
    "err_printer_busy",
    title="Raise 'Printer busy' error",
    description="""Loads error code &A6 and tail-calls error_inline_log with the inline
string 'Printer busy'. Called when an attempt is made to enable a
printer server while one is already active. Never returns.""",
)


d.comment(0xAF9D, "A=&A6: 'Printer busy' error code", align=Align.INLINE)
d.comment(0xAF9F, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.comment(0xAFC9, "A=&A7: 'Printer jammed' error code", align=Align.INLINE)
# UNMAPPED: d.label(0xAF92, "printer_busy_msg")

d.comment(0xAFCB, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.label(0xAFDD, "send_disconnect_reply")

d.subroutine(
    0xAFDD,
    "send_disconnect_reply",
    title="Send Econet disconnect reply packet",
    description="""Sets up the TX pointer, copies station
addresses, matches the station in the table,
and sends the response. Waits for
acknowledgment before returning.""",
    on_exit={"a": "TX result code"},
)


d.comment(0xAFDD, "X = caller's TX-ptr low byte", align=Align.INLINE)
d.comment(0xAFDF, "Y = caller's TX-ptr high byte", align=Align.INLINE)
d.comment(0xAFE1, "Save A (the disconnect status to send)", align=Align.INLINE)
d.comment(0xAFE2, "Test if A=0 (broadcast disconnect)", align=Align.INLINE)
d.comment(0xAFE4, "Yes: skip the per-station scan", align=Align.INLINE)
d.comment(0xAFE6, "X=&FF: scan counter -- INX in loop bumps to 0", align=Align.INLINE)
d.comment(0xAFE8, "Y=A: status code (also used as station-table key)", align=Align.INLINE)
d.label(0xAFE9, "loop_scan_disconnect")

d.comment(0xAFE9, "Restore status into A for the compare", align=Align.INLINE)
d.comment(0xAFEA, "Step station-table index", align=Align.INLINE)
d.comment(0xAFEB, "Compare with table[X] at &C230 (per-station status)", align=Align.INLINE)
d.comment(0xAFEE, "Match: verify station address still matches", align=Align.INLINE)
d.comment(0xAFF0, "Reached end of 16-slot table?", align=Align.INLINE)
d.comment(0xAFF2, "No: keep scanning", align=Align.INLINE)
d.comment(0xAFF4, "All slots tested, no match: A=0", align=Align.INLINE)
d.comment(0xAFF6, "Always taken: jump to send-status", align=Align.INLINE)
d.label(0xAFF8, "verify_stn_match")

d.comment(0xAFF8, "Y = matching index", align=Align.INLINE)
d.comment(0xAFF9, "Verify station/network at this slot still matches caller", align=Align.INLINE)
d.comment(0xAFFC, "Mismatch: station moved, keep scanning", align=Align.INLINE)
d.comment(0xAFFE, "Read connection-active flag at &C260+X", align=Align.INLINE)
d.comment(0xB001, "Mask to bit 0 (active flag)", align=Align.INLINE)
d.label(0xB003, "send_disconnect_status")

d.comment(0xB003, "Y=0: TX[0] = control byte", align=Align.INLINE)
d.comment(0xB005, "OR active-flag bit into the status", align=Align.INLINE)
d.comment(0xB007, "Save the combined status", align=Align.INLINE)
d.comment(0xB008, "Write it to TX[0]", align=Align.INLINE)
d.comment(0xB00A, "Send the disconnect packet via four-way handshake", align=Align.INLINE)
d.comment(0xB00D, "A=&FF: sentinel", align=Align.INLINE)
d.comment(0xB00F, "Y=8: TX[8] / TX[9] = packet trailer markers", align=Align.INLINE)
d.comment(0xB011, "Write &FF at TX[8]", align=Align.INLINE)
d.comment(0xB013, "Step Y", align=Align.INLINE)
d.comment(0xB014, "Write &FF at TX[9]", align=Align.INLINE)
d.comment(0xB016, "Pull the saved status", align=Align.INLINE)
d.comment(0xB017, "Move into X for the test", align=Align.INLINE)
d.comment(0xB018, "Y=&D1: control byte for ack-mode TXCB[1]", align=Align.INLINE)
d.comment(0xB01A, "Pull caller's original A again (was double-saved)", align=Align.INLINE)
d.comment(0xB01B, "Push it back", align=Align.INLINE)
d.comment(0xB01C, "A=0: skip the override", align=Align.INLINE)
d.comment(0xB01E, "Non-zero: use Y=&90 (FS reply port instead)", align=Align.INLINE)
d.label(0xB020, "store_tx_ctrl_byte")

d.comment(0xB020, "Move chosen control/port into A", align=Align.INLINE)
d.comment(0xB021, "Y=1: TX[1] is the port byte", align=Align.INLINE)
d.comment(0xB023, "Write to TX[1]", align=Align.INLINE)
d.comment(0xB025, "Move saved status into A", align=Align.INLINE)
d.comment(0xB026, "Y=0: TX[0] for ack poll", align=Align.INLINE)
d.comment(0xB027, "Push the status (we'll EOR with reply below)", align=Align.INLINE)
d.label(0xB028, "loop_wait_disc_tx_ack")

d.comment(0xB028, "A=&7F: marker pattern", align=Align.INLINE)
d.comment(0xB02A, "Write to TX[0]", align=Align.INLINE)
d.comment(0xB02C, "Wait for the TX/RX flip", align=Align.INLINE)
d.comment(0xB02F, "Pull saved status (peek without consuming)", align=Align.INLINE)
d.comment(0xB030, "Push it back", align=Align.INLINE)
d.comment(0xB031, "EOR with TX[0]: zero iff reply matches saved", align=Align.INLINE)
d.comment(0xB033, "Rotate result; C set if bit 0 differs", align=Align.INLINE)
d.comment(0xB034, "C set: keep waiting", align=Align.INLINE)
d.comment(0xB036, "Discard saved status", align=Align.INLINE)
d.comment(0xB037, "Discard caller's saved A", align=Align.INLINE)
d.comment(0xB038, "Return", align=Align.INLINE)
d.index_base(0xB039, "tx_econet_txcb_template")
d.banner(
    0xB039,
    title="Spool / disconnect TX control-block template (12 bytes)",
    description="""12-byte Econet TXCB initialisation template used by the spool /
disconnect TX paths. Copied into the workspace TXCB at offsets
`&21..&2C` via `(net_rx_ptr),Y`. Destination station and network
are filled in afterwards by the caller. Per-byte inline comments
identify each TXCB field.""",
)
for i in range(12):
    d.byte(0xB039 + i)

d.comment(0xB039, "ctrl=&80 (standard TX)", align=Align.INLINE)
d.comment(0xB03A, "port=&9F", align=Align.INLINE)
d.comment(0xB03B, "dest station=&00 (filled later)", align=Align.INLINE)
d.comment(0xB03C, "dest network=&00 (filled later)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB006, "buf start lo (&9F)", align=Align.INLINE)
d.comment(0xB03E, "buf start hi (&8E); start = &8EB9", align=Align.INLINE)
d.comment(0xB03F, "buf start ext lo=&FF", align=Align.INLINE)
d.comment(0xB040, "buf start ext hi=&FF", align=Align.INLINE)
# UNMAPPED: d.comment(0xB00A, "buf end lo (&A7)", align=Align.INLINE)
d.comment(0xB042, "buf end hi (&8E); end = &8EA7", align=Align.INLINE)
d.comment(0xB043, "buf end ext lo=&FF", align=Align.INLINE)
d.comment(0xB044, "buf end ext hi=&FF", align=Align.INLINE)
d.index_base(0xB045, "rx_palette_txcb_template")
d.banner(
    0xB045,
    title="Palette-RX control-block template (12 bytes)",
    description="""12-byte template used by the *PS / palette-RX paths. Copied with
marker processing: `&FD` skips the destination byte (preserving
the existing field), `&FC` substitutes `net_rx_ptr_hi` (the
caller's RX-buffer page). Filled in over the workspace TXCB by
the broadcast-RX setup before the request is dispatched.""",
)
for i in range(12):
    d.byte(0xB045 + i)

d.comment(0xB045, "ctrl=&7F (RX listen)", align=Align.INLINE)
d.comment(0xB046, "port=&9E", align=Align.INLINE)
# UNMAPPED: d.comment(0xB010, "skip: preserve dest station", align=Align.INLINE)
d.comment(0xB04A, "buf start hi=page ptr (&FC)", align=Align.INLINE)
d.comment(0xB04B, "buf start ext lo=&FF", align=Align.INLINE)
d.comment(0xB04C, "buf start ext hi=&FF", align=Align.INLINE)
d.comment(0xB04F, "buf end ext lo=&FF", align=Align.INLINE)
d.comment(0xB050, "buf end ext hi=&FF", align=Align.INLINE)
d.label(0xB051, "lang_2_save_palette_vdu")

d.subroutine(
    0xB051,
    "lang_2_save_palette_vdu",
    title="Language reply 2: save palette / VDU state",
    description="""Reached via the language-reply dispatch table when a remote sends
reply code 2 ('save palette and VDU state'). Saves the current
template byte from `osword_flag` on the stack, sets up the
workspace pointer (`nfs_workspace`) to the appropriate offset, and
copies the palette / VDU state from MOS workspace at `&0350` into
the workspace transmit buffer for forwarding back to the
station.""",
)


d.comment(0xB051, "Read osword_flag (preserved across the dispatch)", align=Align.INLINE)
d.entry(0xB051)
d.comment(0xB053, "Save state byte", align=Align.INLINE)
d.comment(0xB054, "A=&E9: workspace start lo for palette save", align=Align.INLINE)
d.comment(0xB056, "Store as nfs_workspace lo", align=Align.INLINE)
d.comment(0xB058, "Y=0", align=Align.INLINE)
d.comment(0xB05A, "Reset osword_flag = 0", align=Align.INLINE)
d.comment(0xB05C, "Read vdu_screen_mode (MOS state byte)", align=Align.INLINE)
d.comment(0xB05F, "Store at (nfs_workspace)+0", align=Align.INLINE)
d.comment(0xB061, "Advance nfs_workspace lo", align=Align.INLINE)
d.comment(0xB063, "Read vdu_display_start_hi (next MOS byte)", align=Align.INLINE)
d.comment(0xB066, "Save another byte", align=Align.INLINE)
d.comment(0xB067, "A=0 for first palette entry", align=Align.INLINE)
d.label(0xB068, "loop_read_palette")

d.comment(0xB068, "Store at (nfs_workspace)", align=Align.INLINE)
d.comment(0xB06A, "Read updated nfs_workspace lo", align=Align.INLINE)
d.comment(0xB06C, "Read nfs_workspace hi", align=Align.INLINE)
d.comment(0xB06E, "A=&0B: OSWORD &0B = read palette entry", align=Align.INLINE)
d.comment(0xB070, "Read palette entry", align=Align.INLINE)
d.comment(0xB073, "Restore inner saved", align=Align.INLINE)
d.comment(0xB074, "Y=0", align=Align.INLINE)
d.comment(0xB076, "Store palette result at workspace", align=Align.INLINE)
d.comment(0xB078, "Y=1: physical colour offset", align=Align.INLINE)
d.comment(0xB079, "Re-read palette result", align=Align.INLINE)
d.comment(0xB07B, "Save for next iteration", align=Align.INLINE)
d.comment(0xB07C, "Read updated workspace lo", align=Align.INLINE)
d.comment(0xB07E, "Advance workspace", align=Align.INLINE)
d.comment(0xB080, "Increment osword_flag (palette index)", align=Align.INLINE)
d.comment(0xB082, "Y=0", align=Align.INLINE)
d.comment(0xB083, "Read updated osword_flag", align=Align.INLINE)
d.comment(0xB085, "Compare with &F9 (last palette entry)", align=Align.INLINE)
d.comment(0xB087, "Not done: loop", align=Align.INLINE)
d.comment(0xB089, "Restore outer saved", align=Align.INLINE)
d.comment(0xB08A, "Reset osword_flag = 0 after palette loop", align=Align.INLINE)
d.comment(0xB08C, "Advance workspace", align=Align.INLINE)
d.comment(0xB08E, "Serialise the next palette entry", align=Align.INLINE)
d.comment(0xB091, "Advance workspace", align=Align.INLINE)
d.comment(0xB093, "Restore final saved", align=Align.INLINE)
d.comment(0xB094, "Save osword_flag", align=Align.INLINE)
d.label(0xB096, "commit_state_byte")

d.subroutine(
    0xB096,
    "commit_state_byte",
    title="Copy current state byte to committed state",
    description="""Reads the working state byte from workspace and
stores it to the committed state location. Used
to finalise a state transition after all related
workspace fields have been updated.""",
    on_exit={"a": "= the committed value"},
)


d.comment(0xB096, "Read saved copy of prot_status from prot_status_save", align=Align.INLINE)
d.comment(0xB099, "Store back to prot_status", align=Align.INLINE)
d.comment(0xB09C, "Return", align=Align.INLINE)
d.label(0xB09D, "serialise_palette_entry")

d.subroutine(
    0xB09D,
    "serialise_palette_entry",
    title="Serialise palette register to workspace",
    description="""Reads the current logical colour for a palette
register via OSBYTE &0B and stores both the
palette value and the display mode information
in the workspace block. Used during remote
screen state capture.""",
    on_entry={"x": "palette register index (0-15)", "y": "destination workspace offset (palette + mode pair)"},
    on_exit={"y": "advanced past the 2-byte pair", "a, x": "clobbered (OSBYTE)"},
)


d.comment(0xB09D, "Read vdu_mode (current palette index)", align=Align.INLINE)
d.comment(0xB0A1, "Mark as palette entry", align=Align.INLINE)
# UNMAPPED: d.comment(0xB06B, "Store at (nfs_workspace)+Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB06D, "Read vdu_mode", align=Align.INLINE)
d.comment(0xB0A5, "Advance workspace", align=Align.INLINE)
d.comment(0xB0A7, "A = current Y (= 0)", align=Align.INLINE)
d.comment(0xB0A8, "Store 0 at (nfs_workspace)+Y", align=Align.INLINE)
d.comment(0xB0AA, "Read lookup byte from read_osbyte_table+X", align=Align.INLINE)
d.comment(0xB0AD, "X=0: indexed-indirect mode", align=Align.INLINE)
d.comment(0xB0AF, "Advance workspace", align=Align.INLINE)
d.comment(0xB0B1, "Store at (nfs_workspace,X)", align=Align.INLINE)
d.comment(0xB0B3, "Read OSBYTE result via x=0 helper", align=Align.INLINE)
d.label(0xB0B6, "read_osbyte_to_ws_x0")

d.subroutine(
    0xB0B6,
    "read_osbyte_to_ws_x0",
    title="Read OSBYTE with X=0 and store to workspace",
    description="""Sets X=0 then falls through to read_osbyte_to_ws
to issue the OSBYTE call and store the result.
Used when the OSBYTE parameter X must be zero.""",
    on_entry={"y": "destination workspace offset"},
    on_exit={"y": "incremented past the stored byte", "a, x": "clobbered (OSBYTE)"},
)


d.comment(0xB0B6, "X=0: zero-arg helper entry", align=Align.INLINE)
d.label(0xB0B8, "read_osbyte_to_ws")

d.subroutine(
    0xB0B8,
    "read_osbyte_to_ws",
    title="Issue OSBYTE from table and store result",
    description="""Loads the OSBYTE function code from the next
entry in the OSBYTE table, issues the call, and
stores the Y result in workspace at the current
offset. Advances the table pointer for the next
call.""",
    on_entry={"x": "OSBYTE X parameter", "y": "destination workspace offset"},
    on_exit={"y": "incremented past the stored byte", "a, x": "clobbered"},
)


d.comment(0xB0B8, "Y = osword_flag (OSBYTE-table index)", align=Align.INLINE)
d.comment(0xB0BA, "Increment osword_flag for next call", align=Align.INLINE)
d.comment(0xB0BC, "Advance nfs_workspace", align=Align.INLINE)
d.comment(0xB0BE, "Load OSBYTE number from read_osbyte_return+Y", align=Align.INLINE)
d.comment(0xB0C1, "Y=&FF -- OSBYTE arg (read mode)", align=Align.INLINE)
d.comment(0xB0C3, "Issue OSBYTE", align=Align.INLINE)
d.comment(0xB0C6, "Result to A", align=Align.INLINE)
d.comment(0xB0C7, "X=0: indexed-indirect mode", align=Align.INLINE)
d.comment(0xB0C9, "Store at (nfs_workspace,X)", align=Align.INLINE)
d.comment(0xB0CB, "Return", align=Align.INLINE)
d.index_base(0xB0CC, "read_osbyte_return")

d.index_base(0xB0CE, "read_osbyte_table")

d.comment(0xB0D5, "JMP (cdir_unused_dispatch_table,X) -- never executed; see cmd_cdir", align=Align.INLINE)
d.label(0xB0D5, "cmd_cdir_indirect_dispatch")

d.entry(0xB0D5)
d.entry(0xB0D6)


d.subroutine(
    0xB0D6,
    "cmd_cdir",
    title="*CDir command handler",
    description="""Parses an optional allocation size argument: if absent, defaults to
index 2 (standard 19-entry directory, `&200` bytes); if present,
parses the decimal value and searches a 26-entry threshold table to
find the matching allocation size index. Parses the directory name
via `parse_filename_arg`, copies it to the TX buffer, and sends FS
command code `&1B` to create the directory.

Reached via PHA/PHA/RTS dispatch from `cmd_table_fs` entry
[`*Cdir`](address:A7B0); the byte at the entry-1 address `&B0D5`
happens to decode as `JMP (cdir_unused_dispatch_table,X)` but is never executed.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xB0D6, "Save command line offset", align=Align.INLINE)
d.comment(0xB0D7, "Push onto stack", align=Align.INLINE)
d.entry(0xB0D8)
d.comment(0xB0D8, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xB0DB, "Skip to optional size argument", align=Align.INLINE)
d.comment(0xB0DE, "End of line?", align=Align.INLINE)
d.comment(0xB0E0, "No: parse size argument", align=Align.INLINE)
d.comment(0xB0E2, "Default allocation size index = 2", align=Align.INLINE)
d.label(0xB0E6, "parse_cdir_size")

d.comment(0xB0E6, "A=&FF: mark as decimal parse", align=Align.INLINE)
d.comment(0xB0E8, "Store decimal parse flag", align=Align.INLINE)
d.comment(0xB0EA, "Parse numeric size argument", align=Align.INLINE)
d.comment(0xB0ED, "X=&1B: top of 26-entry size table", align=Align.INLINE)
d.label(0xB0EF, "loop_find_alloc_size")

d.comment(0xB0EF, "Try next lower index", align=Align.INLINE)
d.comment(0xB0F0, "Compare size with threshold", align=Align.INLINE)
d.comment(0xB0F3, "A < threshold: keep searching", align=Align.INLINE)
d.label(0xB0F5, "done_cdir_size")
d.comment(0xB0F5, "Store allocation size index", align=Align.INLINE)
d.comment(0xB0F8, "Restore command line offset", align=Align.INLINE)
d.comment(0xB0F9, "Transfer to Y", align=Align.INLINE)
d.comment(0xB0FA, "Save text pointer for filename parse", align=Align.INLINE)
d.comment(0xB0FD, "Parse directory name argument", align=Align.INLINE)
d.comment(0xB100, "X=1: one argument to copy", align=Align.INLINE)
d.comment(0xB102, "Copy directory name to TX buffer", align=Align.INLINE)
d.comment(0xB105, "Y=&1B: *CDir FS command code", align=Align.INLINE)
d.label(0xB107, "cdir_dispatch_col")

d.comment(0xB107, "Send command to file server", align=Align.INLINE)

d.label(0xB109, "cdir_size_thresholds")

for i in range(27):
    d.byte(0xB10A + i)

d.label(0xB10A, "cdir_alloc_size_table")
d.banner(
    0xB10A,
    title="*CDir allocation size threshold table (26 entries)",
    description="""26 thresholds dividing 0-255 into size classes for the *CDir
directory-size argument. Table base is at `cdir_dispatch_col+2`
(overlapping the JMP operand high byte just before the table); the search
loop (`LDX #&1B` / `DEX` / `CMP table,X` / `BCC`) scans indices
26 down to 0. Index 0 reads `&94` from the JMP and is unreachable
because index 1 (threshold `&00`) always matches first. The
resulting `X` (1-26) is the allocation size class sent to the
file server. Default when no size argument is given: index 2.""",
)
d.comment(0xB10A, "Index 1: threshold 0 (catch-all)", align=Align.INLINE)
d.comment(0xB10B, "Index 2: threshold 10 (default)", align=Align.INLINE)
d.comment(0xB10C, "Index 3: threshold 20", align=Align.INLINE)
d.comment(0xB10D, "Index 4: threshold 29", align=Align.INLINE)
d.comment(0xB110, "Index 7: threshold 59", align=Align.INLINE)
d.comment(0xB111, "Index 8: threshold 69", align=Align.INLINE)
d.comment(0xB113, "Index 10: threshold 88", align=Align.INLINE)
d.comment(0xB114, "Index 11: threshold 98", align=Align.INLINE)
d.comment(0xB115, "Index 12: threshold 108", align=Align.INLINE)
d.comment(0xB118, "Index 15: threshold 138", align=Align.INLINE)
d.comment(0xB119, "Index 16: threshold 148", align=Align.INLINE)
d.comment(0xB11B, "Index 18: threshold 167", align=Align.INLINE)
d.comment(0xB11C, "Index 19: threshold 177", align=Align.INLINE)
d.comment(0xB11E, "Index 21: threshold 197", align=Align.INLINE)
d.comment(0xB120, "Index 23: threshold 216", align=Align.INLINE)
d.comment(0xB121, "Index 24: threshold 226", align=Align.INLINE)
d.comment(0xB122, "Index 25: threshold 236", align=Align.INLINE)
d.index_base(0xB123, "cdir_size_done")
d.comment(
    0xB123,
    "Index 26: threshold &F6 (246) -- last cdir-size threshold; doubles as cdir_size_done[0] (unread by init loop)",
    align=Align.INLINE,
)
d.comment(0xB124, "cdir_size_done[1] = &FF -> tx_retry_count (retry counter init)", align=Align.INLINE)
d.byte(0xB125)
d.comment(0xB125, "cdir_size_done[2] = &28 -> rx_wait_timeout (40 retries)", align=Align.INLINE)
d.byte(0xB126)
d.comment(0xB126, "cdir_size_done[3] = &0A -> peek_retry_count (10 retries)", align=Align.INLINE)

d.entry(0xB127)
d.label(0xB127, "cmd_lcat")

d.subroutine(
    0xB127,
    "cmd_lcat",
    title="*LCat command handler",
    description="""Rotates the caller's carry into bit 7 of
[`hazel_fs_lib_flags`](label:hazel_fs_lib_flags) (the dispatch path enters
with C=1 so this sets the 'library' flag), then `SEC` / `BCS`
unconditionally jumps to `cat_set_lib_flag` inside
[`cmd_ex`](label:cmd_ex) to catalogue the library directory
with three entries per column.""",
    on_entry={"y": "command line offset in text pointer", "c": "1 (set by the cmd_table_fs dispatch path)"},
)


d.comment(0xB127, "Rotate carry into lib flag bit 7", align=Align.INLINE)
d.comment(0xB12A, "Set carry (= library directory)", align=Align.INLINE)
d.entry(0xB12D)
d.label(0xB12D, "cmd_lex")

d.subroutine(
    0xB12D,
    "cmd_lex",
    title="*LEx command handler",
    description="""Rotates the caller's carry into bit 7 of
[`hazel_fs_lib_flags`](label:hazel_fs_lib_flags) (the dispatch path enters
with C=1 so this sets the 'library' flag), then jumps to
`ex_set_lib_flag` inside [`cmd_ex`](label:cmd_ex) to examine
the library directory with one entry per line.""",
    on_entry={"y": "command line offset in text pointer", "c": "1 (set by the cmd_table_fs dispatch path)"},
)


d.comment(0xB12D, "Rotate carry into lib flag bit 7", align=Align.INLINE)
d.comment(0xB130, "Set carry (= library directory)", align=Align.INLINE)
d.label(0xB133, "ps_scan_resume")

d.comment(0xB133, "Set OS text pointer and FS-options transfer ptr", align=Align.INLINE)
d.comment(0xB136, "Y=0: TX-buffer offset for the first byte", align=Align.INLINE)
d.entry(0xB138)
d.label(0xB138, "cmd_ex")

d.subroutine(
    0xB138,
    "cmd_ex",
    title="*Ex command handler",
    description="""Unified handler for *Ex, *LCat, and *LEx. Sets the
library flag from carry (CLC for current, SEC for library).
Configures column format: 1 entry per line for Ex
(command 3), 3 per column for Cat (command &0B). Sends the
examine request (code &12), then prints the directory
header: title, cycle number, Owner/Public label, option
name, Dir. and Lib. paths. Paginates through entries,
printing each via ex_print_col_sep until the server
returns zero entries.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xB138, "Rotate carry into lib flag bit 7", align=Align.INLINE)
d.comment(0xB13B, "Clear carry (= current directory)", align=Align.INLINE)
d.label(0xB13C, "ex_set_lib_flag")

d.comment(0xB13C, "Rotate carry back, clearing bit 7", align=Align.INLINE)
d.comment(0xB13F, "A=&FF: initial column counter", align=Align.INLINE)
d.comment(0xB141, "Store column counter", align=Align.INLINE)
d.comment(0xB143, "One entry per line (Ex format)", align=Align.INLINE)
d.comment(0xB145, "Store entries per page", align=Align.INLINE)
d.comment(0xB147, "FS command code 3: Examine", align=Align.INLINE)
d.comment(0xB149, "Store command code", align=Align.INLINE)
d.label(0xB14D, "fscv_5_cat")

d.subroutine(
    0xB14D,
    "fscv_5_cat",
    title="FSCV reason 5: catalogue (*CAT)",
    description="""Sets up transfer parameters via [`set_xfer_params`](label:set_xfer_params),
clears the library bit in `hazel_fs_lib_flags` via the
`ROR`/`CLC`/`ROL` idiom that uses carry to preserve other flags,
and falls through to `cat_set_lib_flag` to issue the FS examine
request. Reached via the FSCV vector with reason code 5.""",
)


d.entry(0xB14D)
d.comment(0xB14D, "Set transfer parameters", align=Align.INLINE)
d.comment(0xB150, "Y=0: start from entry 0", align=Align.INLINE)
d.comment(0xB152, "Rotate carry into lib flag", align=Align.INLINE)
d.comment(0xB155, "Clear carry (= current directory)", align=Align.INLINE)
d.label(0xB156, "cat_set_lib_flag")

d.comment(0xB156, "Rotate carry back, clearing bit 7", align=Align.INLINE)
d.comment(0xB159, "Three entries per column (Cat)", align=Align.INLINE)
d.comment(0xB15B, "Store column counter", align=Align.INLINE)
d.comment(0xB15D, "Store entries per page", align=Align.INLINE)
d.comment(0xB15F, "FS command code &0B: Catalogue", align=Align.INLINE)
d.comment(0xB161, "Store command code", align=Align.INLINE)
d.label(0xB163, "setup_ex_request")

d.comment(0xB163, "Save text pointer", align=Align.INLINE)
d.comment(0xB166, "A=&FF: enable escape checking", align=Align.INLINE)
d.comment(0xB168, "Set escapable flag", align=Align.INLINE)
d.comment(0xB16A, "Command code 6", align=Align.INLINE)
d.comment(0xB16C, "Store in TX buffer", align=Align.INLINE)
d.comment(0xB16F, "Parse directory argument", align=Align.INLINE)
d.comment(0xB172, "X=1: offset in buffer", align=Align.INLINE)
d.comment(0xB174, "Copy argument to TX buffer", align=Align.INLINE)
d.comment(0xB177, "Get library/FS flags", align=Align.INLINE)
d.comment(0xB17A, "Shift bit 0 to carry", align=Align.INLINE)
d.comment(0xB17B, "Bit 0 clear: skip", align=Align.INLINE)
d.comment(0xB17D, "Set bit 6 (owner access flag)", align=Align.INLINE)
d.label(0xB17F, "store_owner_flags")

d.comment(0xB17F, "Rotate back", align=Align.INLINE)
d.comment(0xB180, "Store modified flags", align=Align.INLINE)
d.comment(0xB183, "Y=&12: FS command for examine", align=Align.INLINE)
d.comment(0xB185, "Send request to file server", align=Align.INLINE)
d.comment(0xB188, "X=3: offset to directory title", align=Align.INLINE)
d.comment(0xB18A, "Print directory title (10 chars)", align=Align.INLINE)
d.comment(0xB18D, "Print '('", align=Align.INLINE)
d.comment(0xB191, "Load FS object-type code from hazel_txcb_objtype (file/dir/etc)", align=Align.INLINE)
d.comment(0xB197, "Print ')     ' to close the type-code field", align=Align.INLINE)
d.comment(0xB1A0, "Read hazel_txcb_type (FS reply opcode)", align=Align.INLINE)
d.comment(0xB1A3, "Non-zero (private library): take the public-label branch", align=Align.INLINE)
d.comment(0xB1A5, "Print 'Owner' + CR", align=Align.INLINE)
d.comment(0xB1AE, "Non-zero: branch to cat_after_label_print", align=Align.INLINE)
d.label(0xB1B0, "print_public_label")

d.comment(0xB1B0, "Print 'Public' + CR", align=Align.INLINE)
d.label(0xB1BA, "cat_after_label_print")

d.comment(0xB1BA, "Read hazel_fs_lib_flags", align=Align.INLINE)
d.comment(0xB1BD, "Push for stack-based saves", align=Align.INLINE)
d.comment(0xB1BE, "Mask owner access bits", align=Align.INLINE)
d.comment(0xB1C1, "Y=&15: FS command for dir info", align=Align.INLINE)
d.comment(0xB1C3, "Send request to file server", align=Align.INLINE)
d.comment(0xB1C6, "Advance X past header", align=Align.INLINE)
d.comment(0xB1C7, "Y=&10: print 16 chars", align=Align.INLINE)
d.comment(0xB1C9, "Print file entry", align=Align.INLINE)
d.comment(0xB1CC, "Print '    Option '", align=Align.INLINE)
d.comment(0xB1DA, "Read hazel_fs_flags", align=Align.INLINE)
d.comment(0xB1DD, "Transfer to X for table lookup", align=Align.INLINE)
d.comment(0xB1DE, "Print option as hex", align=Align.INLINE)
d.comment(0xB1E1, "Print ' ('", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1B1, "Look up option-string offset for index X", align=Align.INLINE)
# UNMAPPED: d.label(0xB1B4, "loop_print_dir_format")

# UNMAPPED: d.comment(0xB1B4, "Look up option byte at the resolved offset", align=Align.INLINE)
d.comment(0xB1E6, "Look up option-string offset for index X", align=Align.INLINE)
d.comment(0xB1E9, "Look up option byte at the resolved offset", align=Align.INLINE)
d.comment(0xB1EC, "Bit 7 of A set (negative): print directory header", align=Align.INLINE)
d.comment(0xB1EE, "Print char (no spool)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1B9, "Print char (no spool)", align=Align.INLINE)
d.comment(0xB1F1, "Advance Y", align=Align.INLINE)
d.comment(0xB1F2, "Loop until Y wraps", align=Align.INLINE)
d.label(0xB1F4, "print_dir_header")

d.comment(0xB1F4, "Print ')\\rDir. ' header for the directory listing", align=Align.INLINE)
d.comment(0xB1FE, "X=&11: filename offset in TX buffer", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1CB, "Print 10-char filename", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1CE, "Print inline 'attr-bits' fragment", align=Align.INLINE)
d.comment(0xB200, "Print 10-char filename", align=Align.INLINE)
d.comment(0xB203, "Print inline 'attr-bits' fragment", align=Align.INLINE)
d.comment(0xB206, "label for *Ex output", align=Align.INLINE)
d.comment(0xB210, "X=&1B: extension offset in TX buffer", align=Align.INLINE)
d.comment(0xB212, "Print 10-char extension", align=Align.INLINE)
d.comment(0xB215, "Print newline", align=Align.INLINE)
d.comment(0xB218, "Pop saved counter", align=Align.INLINE)
d.comment(0xB219, "Store as fs_lib_flags", align=Align.INLINE)
d.label(0xB21C, "setup_ex_pagination")

d.comment(0xB21C, "Save Y as hazel_txcb_flag (next-entry index)", align=Align.INLINE)
d.comment(0xB21F, "Save Y as fs_work_4", align=Align.INLINE)
d.comment(0xB221, "Load fs_work_5 (page count)", align=Align.INLINE)
d.comment(0xB223, "Store at hazel_txcb_count", align=Align.INLINE)
d.comment(0xB226, "Load fs_work_7", align=Align.INLINE)
d.comment(0xB228, "Store at hazel_txcb_data", align=Align.INLINE)
d.comment(0xB22B, "X=3: TX[3] is start of arg buffer", align=Align.INLINE)
d.comment(0xB22D, "Copy filename arg", align=Align.INLINE)
d.comment(0xB230, "Y=3: cmd code 3 (catalog)", align=Align.INLINE)
d.comment(0xB232, "Send TX request", align=Align.INLINE)
d.comment(0xB235, "X advances entry counter", align=Align.INLINE)
d.comment(0xB236, "Read reply status", align=Align.INLINE)
d.comment(0xB239, "Z: empty reply -> exit cat", align=Align.INLINE)
d.comment(0xB23B, "Push reply status", align=Align.INLINE)
d.label(0xB23C, "loop_scan_entry_data")

d.comment(0xB23C, "Advance Y", align=Align.INLINE)
d.comment(0xB23D, "Read entry byte from hazel_txcb_data+Y", align=Align.INLINE)
d.comment(0xB240, "Bit 7 clear: keep scanning", align=Align.INLINE)
d.comment(0xB242, "Store with high-bit clear at hazel_txcb_lib+Y", align=Align.INLINE)
d.comment(0xB245, "Print column separator", align=Align.INLINE)
d.comment(0xB248, "Pop saved status", align=Align.INLINE)
d.comment(0xB249, "Clear carry for the ADC below", align=Align.INLINE)
d.comment(0xB24A, "Add fs_work_4 (page accumulator)", align=Align.INLINE)
d.comment(0xB24C, "New index", align=Align.INLINE)
d.comment(0xB24D, "Non-zero: continue paging", align=Align.INLINE)
d.label(0xB24F, "print_10_chars")

d.subroutine(
    0xB24F,
    "print_10_chars",
    title="Print 10 characters from reply buffer",
    description="""Sets Y=10 and falls through to
print_chars_from_buf. Used by cmd_ex to print
fixed-width directory title, directory name, and
library name fields.""",
    on_entry={"x": "buffer offset to start printing from"},
)


d.comment(0xB24F, "Y=10: ten characters to print (fixed-width field)", align=Align.INLINE)
d.subroutine(
    0xB251,
    "print_chars_from_buf",
    title="Print Y characters from buffer via OSASCI",
    description="""Loops Y times, loading each byte from fs_cmd_data+X
and printing it via OSASCI. Advances X after
each character, leaving X pointing past the
last printed byte.""",
    on_entry={"x": "buffer offset", "y": "character count"},
)


d.comment(0xB251, "Read next character from reply buffer at offset X", align=Align.INLINE)
d.comment(0xB254, "Print via OSASCI, bypassing the *SPOOL file", align=Align.INLINE)
d.comment(0xB257, "Step buffer offset", align=Align.INLINE)
d.comment(0xB258, "Step character counter", align=Align.INLINE)
d.comment(0xB259, "Loop until Y=0", align=Align.INLINE)
d.comment(0xB25B, "Return; X points just past the last printed byte", align=Align.INLINE)
d.label(0xB25C, "jmp_osnewl")

d.label(0xB25F, "parse_cmd_arg_y0")

d.subroutine(
    0xB25F,
    "parse_cmd_arg_y0",
    title="Parse command argument from offset zero",
    description="""Sets Y=0 and falls through to parse_filename_arg
for GSREAD-based filename parsing with prefix
character handling.""",
    on_exit={"y": "advanced past the parsed argument"},
)


d.comment(0xB25F, "Y=0: scan from start of command line", align=Align.INLINE)
d.label(0xB261, "parse_filename_arg")

d.subroutine(
    0xB261,
    "parse_filename_arg",
    title="Parse filename via GSREAD with prefix handling",
    description="""Calls [`gsread_to_buf`](label:gsread_to_buf) to read the command-line
string into [`hazel_parse_buf`](label:hazel_parse_buf) (the 4.21 HAZEL
parse buffer at &C030), then falls through to
[`parse_access_prefix`](label:parse_access_prefix) to process `'&'`, `':'`,
`'.'` and `'#'` prefix characters.""",
    on_entry={"y": "current command-line offset (consumed by gsread_to_buf)"},
    on_exit={"y": "advanced past the parsed argument"},
)


d.comment(
    0xB261,
    "Read the GSREAD-style filename argument into the &C030 buffer, then fall into parse_access_prefix",
    align=Align.INLINE,
)
d.label(0xB264, "parse_access_prefix")

d.subroutine(
    0xB264,
    "parse_access_prefix",
    title="Parse access and FS selection prefix characters",
    description="""Examines the first character(s) of the parsed
buffer at &C030 for prefix characters: '&' sets
the FS selection flag (bit 6 of hazel_fs_lib_flags) and
strips the prefix, ':' with '.' also triggers FS
selection, '#' is accepted as a channel prefix.
Raises 'Bad file name' for invalid combinations
like '&.' followed by CR.""",
)


d.comment(0xB264, "Read first parsed-buffer character (the candidate prefix)", align=Align.INLINE)
d.comment(0xB267, "EOR with '&'; Z set iff the byte was '&'", align=Align.INLINE)
d.comment(0xB269, "Not '&': try ':' (and '#') instead", align=Align.INLINE)
d.comment(0xB26B, "Read fs_lib_flags", align=Align.INLINE)
d.comment(0xB26E, "Set bit 6 (URD-relative resolution flag)", align=Align.INLINE)
d.comment(0xB270, "Write back updated flags", align=Align.INLINE)
d.comment(0xB273, "Strip the '&' from the buffer (shift left + trim)", align=Align.INLINE)
d.comment(0xB276, "Step caller's X back to account for the consumed character", align=Align.INLINE)
d.comment(0xB277, "Re-read the (now first) buffer byte after the strip", align=Align.INLINE)
d.comment(0xB27A, "EOR with '.'; Z set iff '&.' pair (URD root)", align=Align.INLINE)
d.comment(0xB27C, "Not '&.': just '&' alone -- check for trailing '#'", align=Align.INLINE)
d.comment(0xB27E, "It was '&.': peek the byte after the dot", align=Align.INLINE)
d.comment(0xB281, "EOR with CR; Z set iff '&.<CR>' (illegal: dot needs a name to follow)", align=Align.INLINE)
d.comment(0xB283, "'&.<CR>' is invalid: raise 'Bad filename'", align=Align.INLINE)
d.comment(0xB285, "Valid '&.<name>': step X back for the dot too", align=Align.INLINE)
d.label(0xB286, "strip_token_prefix")

d.subroutine(
    0xB286,
    "strip_token_prefix",
    title="Strip first character from parsed token buffer",
    description="""Shifts all bytes in the &C030 buffer left by
one position (removing the first character),
then trims any trailing spaces by replacing
them with CR terminators. Used after consuming
a prefix character like '&' or ':'.""",
    on_exit={"x": "preserved (saved/restored via PHA/PLA)", "a": "clobbered"},
)


d.comment(0xB286, "Save caller's X (TX buffer offset)", align=Align.INLINE)
d.comment(0xB287, "Push it", align=Align.INLINE)
d.comment(0xB288, "X=&FF: INX in loop bumps to 0 for first byte", align=Align.INLINE)
d.label(0xB28A, "loop_shift_str_left")

d.comment(0xB28A, "Step to next byte position", align=Align.INLINE)
d.comment(0xB28B, "Read byte X+1 (the next character)", align=Align.INLINE)
d.comment(0xB28E, "Store it back at byte X (shifting left by one)", align=Align.INLINE)
d.comment(0xB291, "EOR with CR; Z set if we just shifted the terminator", align=Align.INLINE)
d.comment(0xB293, "More to shift: continue", align=Align.INLINE)
d.comment(0xB295, "X is now the buffer length (excluding CR)", align=Align.INLINE)
d.comment(0xB296, "Empty after shift: skip trim, restore X, return", align=Align.INLINE)
d.label(0xB298, "loop_trim_trailing")

d.comment(0xB298, "Read last buffer byte (X-1 because we count from 0)", align=Align.INLINE)
d.comment(0xB29B, "EOR with space; Z set iff it's a trailing space", align=Align.INLINE)
d.comment(0xB29D, "Not a space: trim done, restore X, return", align=Align.INLINE)
d.comment(0xB29F, "It is a space: replace with CR (truncate the string)", align=Align.INLINE)
d.comment(0xB2A1, "Store CR at the now-trimmed position", align=Align.INLINE)
d.comment(0xB2A4, "Step backwards", align=Align.INLINE)
d.comment(0xB2A5, "Loop while X > 0", align=Align.INLINE)
d.label(0xB2A7, "done_strip_prefix")

d.comment(0xB2A7, "Restore caller's TX buffer offset", align=Align.INLINE)
d.comment(0xB2A8, "Transfer back to X", align=Align.INLINE)
d.label(0xB2A9, "rts_strip_prefix")

d.comment(0xB2A9, "Return", align=Align.INLINE)
d.label(0xB2AA, "check_hash_prefix")

d.comment(0xB2AA, "Test for '#' prefix (3 ^ &23 = 0)", align=Align.INLINE)
d.comment(0xB2AC, "Equal: '#' was the prefix, return", align=Align.INLINE)
d.label(0xB2AE, "error_bad_prefix")

d.comment(0xB2AE, "Other: not a recognised prefix -> error", align=Align.INLINE)
d.label(0xB2B1, "check_colon_prefix")

d.comment(0xB2B1, "Test for ':' (&3F ^ &1C)", align=Align.INLINE)
d.comment(0xB2B3, "Different: caller had no prefix, return", align=Align.INLINE)
d.comment(0xB2B5, "':' confirmed -- read next char from parse buffer", align=Align.INLINE)
d.comment(0xB2B8, "Test for '.' (path separator)", align=Align.INLINE)
d.comment(0xB2BA, "Equal: ':.' qualified prefix", align=Align.INLINE)
d.comment(0xB2BC, "Test for '#'", align=Align.INLINE)
d.comment(0xB2BE, "Other: no recognised tail prefix, return", align=Align.INLINE)
d.label(0xB2C0, "set_fs_select_flag")

d.comment(0xB2C0, "Recognised: load fs_lib_flags", align=Align.INLINE)
d.comment(0xB2C3, "Set bit 6 (FS-select pending)", align=Align.INLINE)
d.comment(0xB2C5, "Store updated fs_lib_flags", align=Align.INLINE)
d.comment(0xB2C8, "Recurse to strip the trailing component", align=Align.INLINE)
d.comment(0xB2CB, "Decrement X (consume processed char)", align=Align.INLINE)
d.comment(0xB2CC, "Return", align=Align.INLINE)
d.index_base(0xB2CD, "option_str_offset_data")

d.comment(0xB2CD, "Data: option string offset table", align=Align.INLINE)
d.index_base(0xB2D1, "option_offset_table")

d.label(0xB2D4, "copy_arg_to_buf_x0")

d.subroutine(
    0xB2D4,
    "copy_arg_to_buf_x0",
    title="Copy argument to TX buffer from offset zero",
    description="""Sets X=0 and falls through to copy_arg_to_buf
then copy_arg_validated. Provides the simplest
entry point for copying a single parsed argument
into the TX buffer at position zero.""",
    on_exit={"x": "TX buffer offset just past the copied argument", "y": "advanced past the source argument"},
)


d.comment(
    0xB2D4, "X=0: place the argument at the start of the TX buffer; fall into copy_arg_to_buf", align=Align.INLINE
)
d.label(0xB2D6, "copy_arg_to_buf")

d.subroutine(
    0xB2D6,
    "copy_arg_to_buf",
    title="Copy argument to TX buffer with Y=0",
    description="""Sets Y=0 and falls through to copy_arg_validated
with carry set, enabling '&' character validation.
X must already contain the destination offset
within the TX buffer.""",
    on_entry={"x": "destination offset within the TX buffer"},
    on_exit={"x": "TX buffer offset just past the copied argument", "y": "advanced past the source argument"},
)


d.comment(0xB2D6, "Y=0: scan from start of command line (CLC entry skips '&' validation)", align=Align.INLINE)
d.label(0xB2D8, "copy_arg_validated")

d.subroutine(
    0xB2D8,
    "copy_arg_validated",
    title="Copy command line characters to TX buffer",
    description="""Copies characters from (fs_crc_lo)+Y to fs_cmd_data+X
until a CR terminator is reached. With carry set,
validates each character against '&' — raising
'Bad file name' if found — to prevent FS selector
characters from being embedded in filenames.""",
    on_entry={
        "x": "TX buffer destination offset",
        "y": "command line source offset",
        "c": "set to enable '&' validation",
    },
)

d.comment(0xB2D8, "Set C: this entry validates against '&'", align=Align.INLINE)
d.label(0xB2D9, "loop_copy_char")

d.comment(0xB2D9, "Read next source byte through fs_crc_lo pointer", align=Align.INLINE)
d.comment(0xB2DB, "Store into TX buffer at offset X", align=Align.INLINE)
d.comment(0xB2DE, "Validation off (C clear): just advance positions", align=Align.INLINE)
d.comment(0xB2E0, "Test against '!' to bias the EOR comparison", align=Align.INLINE)
d.comment(0xB2E2, "EOR with '&'; Z set iff source byte was '&'", align=Align.INLINE)
d.comment(0xB2E4, "'&' inside the argument is illegal: raise 'Bad filename'", align=Align.INLINE)
d.label(0xB2E6, "restore_after_check")

d.comment(
    0xB2E6,
    "Restore A by undoing the EOR (so the loop terminator test below sees the original byte)",
    align=Align.INLINE,
)
d.label(0xB2E8, "advance_positions")

d.comment(0xB2E8, "Advance TX buffer offset", align=Align.INLINE)
d.comment(0xB2E9, "Advance command-line offset", align=Align.INLINE)
d.comment(0xB2EA, "EOR with CR; Z set iff we just stored the terminator", align=Align.INLINE)
d.comment(0xB2EC, "More to copy: continue", align=Align.INLINE)
d.comment(0xB2EE, "Look at the byte just before the CR we stopped on", align=Align.INLINE)
d.label(0xB2EE, "loop_trim_trailing_spaces")

d.comment(0xB2F1, "EOR with space; Z set iff that byte was a trailing space", align=Align.INLINE)
d.comment(0xB2F3, "Not a space: trim done", align=Align.INLINE)
d.comment(0xB2F5, "Step back over the space", align=Align.INLINE)
d.comment(0xB2F6, "A=&0D: replace the trailing space with CR", align=Align.INLINE)
d.comment(0xB2F8, "Store CR at the now-truncated end", align=Align.INLINE)
d.comment(0xB2FB, "Always taken (A=&0D from LDA #&0D so Z is clear); look at the next byte back", align=Align.INLINE)
d.label(0xB2FD, "done_trim_spaces")


d.comment(0xB2FD, "All trailing spaces consumed (or none present)", align=Align.INLINE)
d.label(0xB2FF, "rts_copy_arg")

d.comment(0xB2FF, "Return", align=Align.INLINE)
d.subroutine(
    0xB304,
    "mask_owner_access",
    title="Clear FS selection flags from options word",
    description="""`AND`s the `&C271` (`hazel_fs_lib_flags`) byte with `&1F`, clearing the
FS selection flag (bit 6) and other high bits to retain only the
5-bit owner-access mask. Called before parsing to reset the prefix
state from a previous command. 12 callers.""",
    on_exit={"a": "masked value"},
)


d.comment(0xB304, "Read fs_lib_flags (&C271)", align=Align.INLINE)
d.comment(0xB307, "Keep only the 5-bit owner access mask", align=Align.INLINE)
d.comment(0xB309, "Store back, clearing FS-selection and other high bits", align=Align.INLINE)
d.comment(0xB30C, "Return", align=Align.INLINE)
d.comment(0xB310, "X=0: scan from start of TX entry", align=Align.INLINE)
d.label(0xB310, "ex_init_scan_x0")

d.entry(0xB310)
d.label(0xB312, "loop_scan_entries")

d.comment(0xB312, "Read entry byte at hazel_txcb_data+X", align=Align.INLINE)
d.comment(0xB315, "Bit 7 set: end-of-entries -> return", align=Align.INLINE)
d.comment(0xB317, "Non-printable: take CR-newline path at col_sep_print_cr", align=Align.INLINE)
d.label(0xB319, "ex_print_col_sep")

d.subroutine(
    0xB319,
    "ex_print_col_sep",
    title="Print column separator or newline for *Ex/*Cat",
    description="""In *Cat mode, increments a column counter modulo 4
and prints a two-space separator between entries,
with a newline at the end of each row. In *Ex
mode (fs_spool_handle negative), prints a newline
after every entry. Scans the entry data and loops
back to print the next entry's characters.""",
)


d.comment(0xB319, "Read fs_spool_handle (also column counter in *Cat mode)", align=Align.INLINE)
d.comment(0xB31B, "Negative: *Ex mode (one-per-line) -- skip column logic, just print newline", align=Align.INLINE)
d.comment(0xB31D, "Bump column counter", align=Align.INLINE)
d.comment(0xB31E, "Get the new value into A", align=Align.INLINE)
d.comment(0xB31F, "Wrap to 0..3 (4 columns per row)", align=Align.INLINE)
d.comment(0xB321, "Save the new column index", align=Align.INLINE)
d.comment(0xB323, "Wrapped to 0: end of row, print newline", align=Align.INLINE)
d.comment(0xB325, "Mid-row: print 2-space column separator via inline", align=Align.INLINE)
d.comment(0xB32A, "Non-zero: take col_sep_print_char tail", align=Align.INLINE)
d.comment(0xB32C, "A=&0D: CR character", align=Align.INLINE)
d.comment(0xB32E, "Print CR (no spool)", align=Align.INLINE)
d.label(0xB32C, "col_sep_eol_check")

# UNMAPPED: d.comment(0xB2F9, "Print CR (no spool)", align=Align.INLINE)
# UNMAPPED: d.label(0xB2F9, "col_sep_print_cr")

d.comment(0xB331, "Next entry", align=Align.INLINE)
d.label(0xB331, "col_sep_print_char")

d.comment(0xB332, "Loop until X wraps", align=Align.INLINE)
d.comment(0xB338, "Y = value to convert (digits read off via successive divisions)", align=Align.INLINE)
d.subroutine(
    0xB338,
    "print_dec_3dig_no_spool",
    title="Print 3-digit decimal via *SPOOL-bypassing print",
    description="As print_decimal_3dig (&B32A) but each digit is emitted via print_char_no_spool, which closes the *SPOOL handle around OSASCI so the digit doesn't appear in any active capture. Always prints all three digits (no leading-zero suppression).",
    on_entry={"a": "value 0-255"},
)


d.comment(0xB339, "Divisor for hundreds digit", align=Align.INLINE)
d.comment(0xB33B, "Print hundreds digit", align=Align.INLINE)
d.comment(0xB33E, "Divisor for tens digit", align=Align.INLINE)
d.comment(0xB340, "Print tens digit", align=Align.INLINE)
d.comment(
    0xB343, "Divisor for units digit (always print at least the units to avoid the empty 0 case)", align=Align.INLINE
)
d.comment(0xB345, "Stash divisor in fs_error_ptr (the SBC target below)", align=Align.INLINE)
d.subroutine(
    0xB345,
    "print_dec_digit_no_spool",
    title="Print one decimal digit, *SPOOL-bypassing",
    description="As print_decimal_digit (&B36B) but emits via print_char_no_spool. fs_error_ptr is used as scratch storage for the divisor and is preserved across the print.",
    on_entry={"a": "divisor (100, 10, or 1)", "y": "value to divide"},
    on_exit={"y": "remainder after division"},
)


d.entry(0xB347)
d.comment(0xB347, "Convert remaining value to A", align=Align.INLINE)
d.comment(0xB348, "X = '0'-1: digit counter, INX in the loop steps to '0' first", align=Align.INLINE)
d.comment(0xB34A, "Set carry", align=Align.INLINE)
d.comment(0xB34B, "Step quotient digit", align=Align.INLINE)
d.label(0xB34B, "loop_divide_decimal_digit")

d.comment(0xB34C, "Subtract divisor", align=Align.INLINE)
d.comment(0xB34E, "No underflow: keep dividing", align=Align.INLINE)
d.comment(0xB350, "Underflow: add divisor back to recover the remainder", align=Align.INLINE)
d.comment(0xB352, "Remainder -> Y, ready for the next digit", align=Align.INLINE)
d.comment(0xB353, "Move digit ('0'-'9') from X into A for printing", align=Align.INLINE)
d.comment(
    0xB354, "Save divisor in X across the print (print_char_no_spool preserves X is not guaranteed)", align=Align.INLINE
)
d.comment(0xB356, "Print the digit, bypassing *SPOOL", align=Align.INLINE)
d.comment(0xB359, "Restore divisor from X", align=Align.INLINE)
d.comment(0xB35B, "Return", align=Align.INLINE)
d.label(0xB35C, "print_num_no_leading")

d.subroutine(
    0xB35C,
    "print_num_no_leading",
    title="Print decimal number with leading zero suppression",
    description="""Sets `V=1` via `BIT always_set_v_byte` (the `&FF` constant at
&9769, whose bit 6 sets V) to enable leading-zero suppression
in [`print_decimal_3dig`](label:print_decimal_3dig), then falls through to
that routine. Used by [`print_station_id`](label:print_station_id) for
compact station number display.""",
    on_entry={"a": "number to print (0-255)"},
)


d.comment(0xB35C, "Set V (suppress leading zeros)", align=Align.INLINE)
d.label(0xB35F, "print_decimal_3dig")

d.subroutine(
    0xB35F,
    "print_decimal_3dig",
    title="Print byte as 3-digit decimal via OSASCI",
    description="""Extracts hundreds, tens and units digits by
successive calls to print_decimal_digit. The V
flag controls leading zero suppression: if set,
zero digits are skipped until a non-zero digit
appears. V is always cleared before the units
digit to ensure at least one digit is printed.""",
    on_entry={"a": "number to print (0-255)", "v": "set to suppress leading zeros"},
)


d.comment(0xB35F, "Transfer value to Y (remainder)", align=Align.INLINE)
d.comment(0xB360, "A=100: hundreds divisor", align=Align.INLINE)
d.comment(0xB362, "Print hundreds digit", align=Align.INLINE)
d.comment(0xB365, "A=10: tens divisor", align=Align.INLINE)
d.comment(0xB367, "Print tens digit", align=Align.INLINE)
d.comment(0xB36A, "Clear V (always print units)", align=Align.INLINE)
d.comment(0xB36B, "A=1: units divisor", align=Align.INLINE)
d.label(0xB36D, "print_decimal_digit")

d.subroutine(
    0xB36D,
    "print_decimal_digit",
    title="Print one decimal digit by repeated subtraction",
    description="""Initialises X to '0'-1 and loops, incrementing X
while subtracting the divisor from Y. On underflow,
adds back the divisor to get the remainder in Y.
If V is set, suppresses leading zeros by skipping
the OSASCI call when the digit is '0'.""",
    on_entry={"a": "divisor", "y": "value to divide"},
    on_exit={"y": "remainder after division"},
)


d.comment(0xB36D, "Store divisor", align=Align.INLINE)
d.comment(0xB36F, "Get remaining value", align=Align.INLINE)
d.comment(0xB370, "X='0'-1: digit counter", align=Align.INLINE)
d.comment(0xB372, "Set carry for subtraction", align=Align.INLINE)
d.comment(0xB373, "Save V flag for leading zero check", align=Align.INLINE)
d.label(0xB374, "loop_divide_digit")

d.comment(0xB374, "Count quotient digit", align=Align.INLINE)
d.comment(0xB375, "Subtract divisor", align=Align.INLINE)
d.comment(0xB377, "No underflow: continue dividing", align=Align.INLINE)
d.comment(0xB379, "Add back divisor (get remainder)", align=Align.INLINE)
d.comment(0xB37B, "Remainder to Y for next digit", align=Align.INLINE)
d.comment(0xB37C, "Digit character to A", align=Align.INLINE)
d.comment(0xB37D, "Restore V flag", align=Align.INLINE)
d.comment(0xB37E, "V clear: always print digit", align=Align.INLINE)
d.comment(0xB380, "V set: is digit '0'?", align=Align.INLINE)
d.comment(0xB382, "Yes: suppress leading zero", align=Align.INLINE)
d.label(0xB384, "print_nonzero_digit")

d.comment(0xB384, "Save divisor across OSASCI call", align=Align.INLINE)
d.comment(0xB389, "Restore divisor", align=Align.INLINE)
d.label(0xB38B, "rts_print_digit")

d.comment(0xB38B, "Return", align=Align.INLINE)
d.subroutine(
    0xB38C,
    "cmd_info_dispatch",
    title="*Info command handler",
    description="""Dispatched from the star-command table at index &28. Clears the
owner-only access bits via [`mask_owner_access`](label:mask_owner_access),
then writes the two-byte FS command prefix `'i' '.'` into
[`hazel_txcb_data`](label:hazel_txcb_data)/[`hazel_txcb_flag`](label:hazel_txcb_flag),
saves the command-line pointer with
[`save_ptr_to_os_text`](label:save_ptr_to_os_text), parses the *Info argument
via [`parse_cmd_arg_y0`](label:parse_cmd_arg_y0), copies it into the TX
buffer at offset 2 with [`copy_arg_to_buf`](label:copy_arg_to_buf), and
JMPs to [`send_cmd_and_dispatch`](label:send_cmd_and_dispatch) to send the
request to the file server.""",
    on_entry={"y": "command-line offset in text pointer"},
)


d.comment(0xB38C, "Clear owner-only access bits before checking the URD", align=Align.INLINE)
d.label(0xB38C, "cmd_info_dispatch")

d.entry(0xB38C)
d.comment(0xB38F, "A=&69: 'i' character (info prefix)", align=Align.INLINE)
d.comment(0xB391, "Store 'i' as start of FS command name in the TX buffer", align=Align.INLINE)
d.comment(0xB394, "A='.': abbreviation terminator", align=Align.INLINE)
d.comment(0xB396, "Store '.' as command-name terminator", align=Align.INLINE)
d.comment(0xB399, "Save the command-line pointer for the dispatcher", align=Align.INLINE)
d.comment(0xB39C, "Parse the *Info argument from the command line", align=Align.INLINE)
d.comment(0xB39F, "X=2: TX-buffer offset to copy the arg into (after 'i.')", align=Align.INLINE)
d.comment(0xB3A1, "Append parsed argument to the TX command buffer", align=Align.INLINE)
d.comment(0xB3A4, "A = next index", align=Align.INLINE)
d.comment(0xB3A5, "Send the FS command and dispatch the reply", align=Align.INLINE)
d.label(0xB3A8, "save_ptr_to_os_text")

d.subroutine(
    0xB3A8,
    "save_ptr_to_os_text",
    title="Copy text pointer to OS text pointer workspace",
    description="""Saves fs_crc_lo/hi into the MOS text pointer
locations at &00F2/&00F3. Preserves A on the
stack. Called before GSINIT/GSREAD sequences
that need to parse from the current command
line position.""",
    on_exit={"a": "preserved (PHA/PLA)"},
)


d.comment(0xB3A8, "Save A", align=Align.INLINE)
d.comment(0xB3A9, "Copy text pointer low byte", align=Align.INLINE)
d.comment(0xB3AB, "To OS text pointer low", align=Align.INLINE)
d.comment(0xB3AD, "Copy text pointer high byte", align=Align.INLINE)
d.comment(0xB3AF, "To OS text pointer high", align=Align.INLINE)
d.comment(0xB3B1, "Restore A", align=Align.INLINE)
d.comment(0xB3B2, "Return", align=Align.INLINE)
d.label(0xB3B3, "loop_advance_char")

d.comment(0xB3B3, "Advance past current character", align=Align.INLINE)
d.label(0xB3B4, "skip_to_next_arg")

d.subroutine(
    0xB3B4,
    "skip_to_next_arg",
    title="Advance past spaces to the next command argument",
    description="""Scans (fs_crc_lo)+Y for space characters,
advancing Y past each one. Returns with A
holding the first non-space character, or CR
if the end of line is reached. Used by *CDir
and *Remove to detect extra arguments.""",
    on_entry={"y": "starting offset (where to begin scanning)"},
    on_exit={"a": "first non-space character or CR", "y": "offset of that character"},
)


d.comment(0xB3B4, "Load char from command line", align=Align.INLINE)
d.comment(0xB3B6, "Space?", align=Align.INLINE)
d.comment(0xB3B8, "Yes: skip trailing spaces", align=Align.INLINE)
d.comment(0xB3BA, "CR (end of line)?", align=Align.INLINE)
d.comment(0xB3BC, "Yes: return (at end)", align=Align.INLINE)
d.label(0xB3C0, "loop_skip_space_chars")

d.comment(0xB3C0, "Advance past space", align=Align.INLINE)
d.comment(0xB3C1, "Load next character", align=Align.INLINE)
d.comment(0xB3C3, "Still a space?", align=Align.INLINE)
d.comment(0xB3C5, "Yes: skip multiple spaces", align=Align.INLINE)
d.label(0xB3C7, "rts_skip_arg")

d.comment(0xB3C7, "Return (at next argument)", align=Align.INLINE)
d.label(0xB3C8, "save_ptr_to_spool_buf")

d.subroutine(
    0xB3C8,
    "save_ptr_to_spool_buf",
    title="Copy text pointer to spool buffer pointer",
    description="""Saves fs_crc_lo/hi into fs_options/fs_block_offset
for use as the spool buffer pointer. Preserves A
on the stack. Called by *PS and *PollPS before
parsing their arguments.""",
    on_exit={"a": "preserved (PHA/PLA)"},
)


d.comment(0xB3C8, "Save A", align=Align.INLINE)
d.comment(0xB3C9, "Copy text pointer low byte", align=Align.INLINE)
d.comment(0xB3CB, "To spool buffer pointer low", align=Align.INLINE)
d.comment(0xB3CD, "Copy text pointer high byte", align=Align.INLINE)
d.comment(0xB3CF, "To spool buffer pointer high", align=Align.INLINE)
d.comment(0xB3D1, "Restore A", align=Align.INLINE)
d.comment(0xB3D2, "Return", align=Align.INLINE)
d.label(0xB3D3, "init_spool_drive")

d.subroutine(
    0xB3D3,
    "init_spool_drive",
    title="Initialise spool drive page pointers",
    description="""Calls get_ws_page to read the workspace page
number for the current ROM slot, stores it as
the spool drive page high byte (addr_work), and
clears the low byte (work_ae) to zero. Preserves
Y on the stack.""",
    on_exit={"a": "0", "y": "preserved (PHY/PLY)"},
)


d.comment(0xB3D3, "Save Y", align=Align.INLINE)
d.comment(0xB3D4, "Push it", align=Align.INLINE)
d.comment(0xB3D5, "Get workspace page number", align=Align.INLINE)
d.comment(0xB3D8, "Store as spool drive page high", align=Align.INLINE)
d.comment(0xB3DA, "Restore Y", align=Align.INLINE)
d.comment(0xB3DB, "Transfer to Y", align=Align.INLINE)
d.comment(0xB3DC, "A=0", align=Align.INLINE)
d.comment(0xB3DE, "Clear spool drive page low", align=Align.INLINE)
d.comment(0xB3E0, "Return", align=Align.INLINE)
d.entry(0xB3E1)
d.label(0xB3E1, "cmd_ps")

d.subroutine(
    0xB3E1,
    "cmd_ps",
    title="*PS command handler",
    description="""Checks the printer server availability flag; raises
'Printer busy' if unavailable. Initialises the spool
drive and buffer pointer, then dispatches on argument
type: no argument branches to no_ps_name_given, a
leading digit branches to save_ps_cmd_ptr as a station
number, otherwise parses a named PS address via
load_ps_server_addr and parse_fs_ps_args.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xB3E1, "A=1: check printer ready", align=Align.INLINE)
d.comment(0xB3E3, "Test printer server workspace flag", align=Align.INLINE)
d.comment(0xB3E6, "Non-zero: printer available", align=Align.INLINE)
d.comment(0xB3E8, "Printer not available: error", align=Align.INLINE)
d.label(0xB3EB, "done_ps_available")

d.comment(0xB3EB, "Initialise spool drive", align=Align.INLINE)
d.comment(0xB3EE, "Save pointer to spool buffer", align=Align.INLINE)
d.comment(0xB3F9, "Read fs_options[Y]", align=Align.INLINE)
d.comment(0xB3FB, "End of command line?", align=Align.INLINE)
d.comment(0xB3FD, "Yes: no argument given", align=Align.INLINE)
d.comment(0xB3FF, "Clear V (= explicit PS name given)", align=Align.INLINE)
d.comment(0xB400, "Is first char a decimal digit?", align=Align.INLINE)
d.comment(0xB403, "C clear: save ptr and continue", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3C8, "A = current Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3C9, "Save Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3CA, "Load PS server address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3CD, "Restore Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3CE, "Back to Y register", align=Align.INLINE)
d.comment(0xB40A, "Parse FS/PS arguments", align=Align.INLINE)
d.comment(0xB40D, "Jump to store station address", align=Align.INLINE)
d.label(0xB410, "copy_ps_data_y1c")

d.subroutine(
    0xB410,
    "copy_ps_data_y1c",
    title="Copy printer server template at offset &18",
    description="""Sets Y=&18 and falls through to copy_ps_data.
Called during workspace initialisation
(svc_2_private_workspace) to set up the printer
server template at the standard offset.""",
    on_exit={"y": "&20 (advanced past the copied 8 bytes)"},
)


d.comment(0xB410, "Y=&18: standard offset for the PS template; fall into copy_ps_data", align=Align.INLINE)
d.label(0xB412, "copy_ps_data")

d.subroutine(
    0xB412,
    "copy_ps_data",
    title="Copy 8-byte printer server template to RX buffer",
    description="""Copies 8 bytes of default printer server data into the RX buffer
at the current `Y` offset. Uses indexed addressing: `LDA
ps_template_base,X` with `X` starting at `&F8`, so the effective
read address is `ps_template_base+&F8 = ps_template_data`
(`&8EB9`). The 6502 trick reaches data 248
bytes past the base label in a single instruction; the base
address (`ps_template_base`) deliberately falls inside the operand
byte of a JSR instruction at `&8DA6` -- see
docs/analysis/authors-easter-egg.md.""",
    on_entry={"y": "destination offset within the RX buffer"},
    on_exit={"y": "advanced by 8", "x": "0 (loop terminator)", "a": "last template byte"},
)

d.comment(
    0xB412,
    "X=&F8: walks 0..7 via wraparound (loads from ps_template_base+&F8 = ps_template_data &8EB9)",
    align=Align.INLINE,
)
d.label(0xB414, "loop_copy_ps_tmpl")

d.comment(0xB414, "Read template byte from ps_template_data + (X-&F8)", align=Align.INLINE)
d.comment(0xB417, "Store into RX buffer at offset Y", align=Align.INLINE)
d.comment(0xB419, "Step destination", align=Align.INLINE)
d.comment(0xB41A, "Step source -- wraps from &FF to &00 to terminate", align=Align.INLINE)
d.comment(0xB41B, "Loop while X != 0 (8 iterations: &F8..&FF)", align=Align.INLINE)
d.comment(0xB41D, "Return", align=Align.INLINE)
d.label(0xB41E, "no_ps_name_given")

d.comment(0xB41E, "Set V (= no explicit PS name)", align=Align.INLINE)
d.label(0xB421, "save_ps_cmd_ptr")

d.comment(0xB421, "Save Y at ws_ptr_hi", align=Align.INLINE)
d.comment(0xB423, "V set: skip PS name parsing", align=Align.INLINE)
d.comment(0xB425, "Max 6 characters for PS name", align=Align.INLINE)
d.comment(0xB427, "Buffer offset &1C for PS name", align=Align.INLINE)
d.comment(0xB429, "Space character", align=Align.INLINE)
d.label(0xB42B, "loop_pad_ps_name")

d.comment(0xB42B, "Fill buffer with space", align=Align.INLINE)
d.comment(0xB42D, "Advance Y past padding", align=Align.INLINE)
d.comment(0xB42E, "Count down", align=Align.INLINE)
d.comment(0xB42F, "Loop while Y wraps", align=Align.INLINE)
d.comment(0xB431, "Save text pointer", align=Align.INLINE)
d.comment(0xB434, "Restore Y from ws_ptr_hi", align=Align.INLINE)
d.comment(0xB436, "Initialise string reading", align=Align.INLINE)
d.comment(0xB439, "Empty string: skip to send", align=Align.INLINE)
d.comment(0xB43B, "X=6: scan up to 6 PS slots", align=Align.INLINE)
d.comment(0xB43D, "Save updated string pointer", align=Align.INLINE)
d.comment(0xB43F, "Buffer offset for PS name", align=Align.INLINE)
d.comment(0xB441, "Save buffer position", align=Align.INLINE)
d.label(0xB443, "loop_read_ps_char")

d.comment(0xB443, "Restore string pointer", align=Align.INLINE)
d.comment(0xB445, "Read next character", align=Align.INLINE)
d.comment(0xB448, "Save updated pointer", align=Align.INLINE)
d.comment(0xB44A, "C set: end of slots", align=Align.INLINE)
d.comment(0xB44C, "Store char uppercased in buffer", align=Align.INLINE)
d.comment(0xB44F, "Loop for more characters", align=Align.INLINE)
d.label(0xB451, "done_ps_name_parse")

d.comment(0xB451, "Copy reversed PS name to TX", align=Align.INLINE)
d.comment(0xB454, "Send PS status request", align=Align.INLINE)
d.comment(0xB457, "Pop and requeue PS scan", align=Align.INLINE)
d.comment(0xB45A, "Load PS server address", align=Align.INLINE)
d.comment(0xB45D, "A=0", align=Align.INLINE)
d.comment(0xB460, "Offset &24 in buffer", align=Align.INLINE)
d.comment(0xB462, "Clear PS status byte", align=Align.INLINE)
d.label(0xB464, "loop_pop_ps_slot")

d.comment(0xB464, "Pop saved slot index", align=Align.INLINE)
d.comment(0xB465, "Zero: all slots done", align=Align.INLINE)
d.comment(0xB467, "Push it back (for retry)", align=Align.INLINE)
d.comment(0xB468, "Transfer to Y", align=Align.INLINE)
d.comment(0xB469, "Read slot status", align=Align.INLINE)
d.comment(0xB46B, "Bit 7 clear: slot inactive", align=Align.INLINE)
d.comment(0xB46D, "Advance Y by 4 (next slot)", align=Align.INLINE)
d.comment(0xB470, "Read ws byte at (nfs_workspace)+Y", align=Align.INLINE)
d.comment(0xB472, "Save as work_ae lo", align=Align.INLINE)
d.comment(0xB474, "Read indirect via (work_ae,X)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB43B, "Z set: zero -> read station addr", align=Align.INLINE)
# UNMAPPED: d.comment(0xB43D, "Compare with 3", align=Align.INLINE)
d.comment(0xB478, "Other than 3: skip slot mark", align=Align.INLINE)
d.label(0xB47A, "read_ps_station_addr")


d.comment(0xB47A, "Back up to network byte", align=Align.INLINE)
d.comment(0xB47B, "Read network byte", align=Align.INLINE)
d.comment(0xB47D, "Save as fs_work_6", align=Align.INLINE)
d.comment(0xB47F, "Back up to station byte", align=Align.INLINE)
d.comment(0xB480, "Read station byte", align=Align.INLINE)
d.comment(0xB482, "Save as fs_work_5", align=Align.INLINE)
d.comment(0xB484, "Y=&20: PS marker offset", align=Align.INLINE)
d.comment(0xB486, "Store station to (net_rx_ptr)+&20", align=Align.INLINE)
d.label(0xB488, "done_ps_slot_mark")

d.comment(0xB488, "Pop saved slot index", align=Align.INLINE)
d.comment(0xB489, "Transfer to Y", align=Align.INLINE)
d.comment(0xB48A, "A=&3F: 'processed' marker", align=Align.INLINE)
d.comment(0xB48C, "Mark slot as processed", align=Align.INLINE)
d.label(0xB490, "done_ps_scan")

d.comment(0xB490, "Print 'Printer server is ' fragment", align=Align.INLINE)
d.comment(0xB493, "Y=&20: marker offset", align=Align.INLINE)
d.comment(0xB495, "Read marker byte", align=Align.INLINE)
d.comment(0xB497, "Non-zero: print 'now <stn>'", align=Align.INLINE)
d.comment(0xB499, "Print 'still ' fragment", align=Align.INLINE)
d.comment(0xB4A2, "Bit-7 terminator (next opcode)", align=Align.INLINE)
d.label(0xB4A5, "print_ps_now")

d.comment(0xB4A5, "Print 'now ' fragment", align=Align.INLINE)
# UNMAPPED: d.comment(0xB473, "Bit-7 terminator", align=Align.INLINE)
# UNMAPPED: d.comment(0xB474, "Print station number and newline", align=Align.INLINE)
# UNMAPPED: d.label(0xB474, "print_ps_padding")

d.label(0xB4B4, "store_ps_station")

d.subroutine(
    0xB4B4,
    "store_ps_station",
    title="Write printer-server station number into NFS workspace",
    description="""Stores fs_work_5/fs_work_6 (the parsed station/network bytes) into
nfs_workspace offsets 2 and 3 (the printer-server slot's station/
net pair). Single caller (cmd_ps's parse-success path at &B3D2).""",
)


d.comment(0xB4B4, "Y=2: workspace offset for stored station", align=Align.INLINE)
d.comment(0xB4B6, "Load station number", align=Align.INLINE)
d.comment(0xB4B8, "Store at (nfs_workspace)+2", align=Align.INLINE)
d.comment(0xB4BB, "Load network number", align=Align.INLINE)
d.comment(0xB4BD, "Store at (nfs_workspace)+3", align=Align.INLINE)
d.comment(0xB4BF, "Return", align=Align.INLINE)
d.label(0xB4C0, "print_file_server_is")

d.subroutine(
    0xB4C0,
    "print_file_server_is",
    title="Print 'File server ' prefix",
    description="""Uses print_inline to output 'File' then falls through
to the shared ' server is ' suffix at
print_printer_server_is.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered (OSASCI via print_inline)"},
)


d.comment(0xB4C0, "Print 'File' via inline string", align=Align.INLINE)
d.comment(0xB4C7, "Clear V so the BVC below is taken", align=Align.INLINE)
d.comment(
    0xB4C8,
    "Always taken (V was just cleared); skip the 'Printer' prologue and reach the shared ' server is ' suffix",
    align=Align.INLINE,
)
d.label(0xB4CA, "print_printer_server_is")

d.subroutine(
    0xB4CA,
    "print_printer_server_is",
    title="Print 'Printer server is ' prefix",
    description="""Uses print_inline to output the full label
'Printer server is ' with trailing space.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered (OSASCI via print_inline)"},
)


d.comment(0xB4CA, "Print 'Printer' via inline string", align=Align.INLINE)
d.comment(0xB4D4, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.label(0xB4D5, "print_server_is_suffix")

d.comment(0xB4D5, "Print ' server is ' via inline string", align=Align.INLINE)
d.comment(0xB4D8, "fragment for 'File/Printer server is ...' messages", align=Align.INLINE)
d.comment(0xB4E3, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0xB4E4, "Return; caller now prints the actual server (file or printer) address", align=Align.INLINE)
d.label(0xB4E5, "load_ps_server_addr")

d.subroutine(
    0xB4E5,
    "load_ps_server_addr",
    title="Load printer server address from workspace",
    description="""Reads the station and network bytes from workspace
offsets 2 and 3 into the station/network variables.""",
    on_exit={"a, y": "clobbered"},
)


d.comment(0xB4E5, "Y=2: workspace offset of PS station byte", align=Align.INLINE)
d.comment(0xB4E7, "Read station byte", align=Align.INLINE)
d.comment(0xB4E9, "Stash in fs_work_5 (PS station)", align=Align.INLINE)
d.comment(0xB4EB, "Y=3: workspace offset of PS network byte", align=Align.INLINE)
d.comment(0xB4EC, "Read network byte", align=Align.INLINE)
d.comment(0xB4EE, "Stash in fs_work_6 (PS network)", align=Align.INLINE)
d.comment(0xB4F0, "Return", align=Align.INLINE)
d.label(0xB4F1, "pop_requeue_ps_scan")

d.subroutine(
    0xB4F1,
    "pop_requeue_ps_scan",
    title="Pop return address and requeue PS slot scan",
    description="""Converts the PS slot flags to a workspace index,
writes slot data, and jumps back into the PS scan
loop to continue processing.""",
    on_entry={"a": "PS slot flags byte to convert into a workspace index"},
)


d.comment(0xB4F1, "Pull saved upper byte of ws_ptr_lo+osword_flag pair", align=Align.INLINE)
d.comment(0xB4F2, "Save into osword_flag", align=Align.INLINE)
d.comment(0xB4F4, "Pull lower byte", align=Align.INLINE)
d.comment(0xB4F5, "Save into ws_ptr_lo", align=Align.INLINE)
d.comment(0xB4F7, "Push 0 -- placeholder, will be the stacked return marker", align=Align.INLINE)
d.comment(0xB4F9, "Push it", align=Align.INLINE)
d.comment(0xB4FA, "ws_ptr_hi base = &84 (start of PS slot table area)", align=Align.INLINE)
d.comment(0xB4FC, "Save base", align=Align.INLINE)
d.comment(0xB4FE, "Shift bit 0 of econet_flags into C (saved scan state)", align=Align.INLINE)
d.comment(0xB501, "A=3: PS slot index counter", align=Align.INLINE)
d.label(0xB503, "loop_scan_ps_slots")

d.comment(0xB503, "Convert slot index to 12-byte-aligned table offset", align=Align.INLINE)
d.comment(0xB506, "Out of range (clamped to 0): all slots scanned", align=Align.INLINE)
d.comment(0xB508, "A /= 2 (shift down)", align=Align.INLINE)
d.comment(0xB509, "A /= 2 again (now slot index * 4 / 4 = slot index)", align=Align.INLINE)
d.comment(0xB50A, "X = slot index", align=Align.INLINE)
d.comment(0xB50B, "Read slot's status byte at workspace[Y]", align=Align.INLINE)
d.comment(0xB50D, "Slot empty (0): scan done", align=Align.INLINE)
d.comment(0xB50F, "Slot is '?' (uninitialised marker)?", align=Align.INLINE)
d.comment(0xB511, "Yes: re-init this slot's data", align=Align.INLINE)
d.label(0xB513, "skip_next_ps_slot")

d.subroutine(
    0xB513,
    "skip_next_ps_slot",
    title="Advance to next PS slot, wrap if all 256 done",
    description="""INX / TXA / BNE loop_scan_ps_slots. Slot index in X advances; the
BNE re-enters the scan unless X has wrapped to zero (all 256
slots scanned). Single caller (the no-match path at &B501 in the
PS slot scanner).""",
    on_entry={"x": "current slot index"},
)


d.comment(0xB513, "Step slot index", align=Align.INLINE)
d.comment(0xB514, "Move to A for next iteration", align=Align.INLINE)
d.comment(0xB515, "Loop while X != 0 (wraps when all slots done)", align=Align.INLINE)
d.label(0xB517, "reinit_ps_slot")

d.comment(0xB517, "Save Y (slot table offset)", align=Align.INLINE)
d.comment(0xB518, "Push it", align=Align.INLINE)
d.comment(0xB519, "A=&7F: slot status 'busy/active'", align=Align.INLINE)
d.comment(0xB51B, "Mark slot active", align=Align.INLINE)
d.comment(0xB51D, "Step Y to control byte", align=Align.INLINE)
d.comment(0xB51E, "A=&9E: control byte (PS-init pattern)", align=Align.INLINE)
d.comment(0xB520, "Store control byte", align=Align.INLINE)
d.comment(0xB522, "A=0: zero-fill the next two bytes", align=Align.INLINE)
d.comment(0xB524, "Write two zeros, advance Y", align=Align.INLINE)
d.comment(0xB527, "Read current ws_ptr_hi", align=Align.INLINE)
d.comment(0xB529, "Store as buffer-link low byte", align=Align.INLINE)
d.comment(0xB52B, "Clear C ready for the +3", align=Align.INLINE)
d.comment(0xB52C, "Save flags so the ADC's C doesn't leak", align=Align.INLINE)
d.comment(0xB52D, "Bump ws_ptr_hi by 3 (next slot's base)", align=Align.INLINE)
d.comment(0xB52F, "Restore flags", align=Align.INLINE)
d.comment(0xB530, "Save updated ws_ptr_hi", align=Align.INLINE)
d.comment(0xB532, "Write buffer page + two &FF sentinels", align=Align.INLINE)
d.comment(0xB535, "Read ws_ptr_hi (now updated)", align=Align.INLINE)
d.comment(0xB537, "Store as second-link byte", align=Align.INLINE)
d.label(0xB539, "write_ps_slot_hi_link")

d.comment(0xB539, "Write another buffer page + two &FF sentinels", align=Align.INLINE)
# UNMAPPED: d.label(0xB4FD, "ps_print_template")

d.comment(0xB53C, "Continue scanning slots", align=Align.INLINE)
d.label(0xB53F, "done_ps_slot_scan")

d.comment(0xB53F, "Restore bit 0 of econet_flags via ASL (recovers from the LSR at &B4C3)", align=Align.INLINE)
d.comment(0xB542, "Pull saved ws_ptr_lo", align=Align.INLINE)
d.comment(0xB544, "Push it back (the caller's return-resume sequence)", align=Align.INLINE)
d.comment(0xB545, "Pull saved osword_flag", align=Align.INLINE)
d.comment(0xB547, "Push it back", align=Align.INLINE)
d.comment(0xB548, "A=&0A: outer counter", align=Align.INLINE)
d.comment(0xB54A, "Y=&0A: inner counter", align=Align.INLINE)
d.comment(0xB54B, "X=&0A: middle counter", align=Align.INLINE)
d.comment(0xB54C, "Save outer in fs_work_4", align=Align.INLINE)
d.label(0xB54E, "loop_ps_delay")

d.comment(0xB54E, "Decrement inner counter", align=Align.INLINE)
d.comment(0xB54F, "Inner not zero: keep delaying", align=Align.INLINE)
d.comment(0xB551, "Decrement middle", align=Align.INLINE)
d.comment(0xB552, "Middle not zero: refresh inner and continue", align=Align.INLINE)
d.comment(0xB554, "Decrement outer in fs_work_4", align=Align.INLINE)
d.comment(0xB556, "Outer not zero: another full sweep (~1000 cycles)", align=Align.INLINE)
d.comment(0xB558, "Return", align=Align.INLINE)
d.label(0xB559, "write_ps_slot_byte_ff")

d.subroutine(
    0xB559,
    "write_ps_slot_byte_ff",
    title="Write buffer page byte and two &FF markers",
    description="""Stores the buffer page byte at the current Y offset
in workspace, followed by two &FF sentinel bytes.
Advances Y after each write.""",
    on_entry={"a": "buffer page byte to store at workspace+Y", "y": "starting workspace offset"},
    on_exit={"a": "&FF (the sentinel value left in A)", "y": "workspace offset advanced by 3 (one byte + two markers)"},
)


d.comment(0xB559, "Step Y to next workspace slot byte", align=Align.INLINE)
d.comment(0xB55A, "Load buffer page byte from addr_work", align=Align.INLINE)
d.comment(0xB55C, "Write at offset Y", align=Align.INLINE)
d.comment(0xB55E, "A=&FF: sentinel; fall into write_two_bytes_inc_y to store two of them", align=Align.INLINE)
d.label(0xB560, "write_two_bytes_inc_y")

d.subroutine(
    0xB560,
    "write_two_bytes_inc_y",
    title="Write A to two consecutive workspace bytes",
    description="""Stores A at the current Y offset via (nfs_workspace),Y
then again at Y+1, advancing Y after each write.""",
    on_entry={"a": "byte to store", "y": "workspace offset"},
)


d.comment(0xB560, "Step Y to next destination", align=Align.INLINE)
d.comment(0xB561, "Write A at workspace offset Y", align=Align.INLINE)
d.comment(0xB563, "Step Y again", align=Align.INLINE)
d.comment(0xB564, "Write A at the next offset (two consecutive copies)", align=Align.INLINE)
d.comment(0xB566, "Final INY leaves Y pointing past the second write", align=Align.INLINE)
d.comment(0xB567, "Return", align=Align.INLINE)
d.label(0xB568, "reverse_ps_name_to_tx")

d.subroutine(
    0xB568,
    "reverse_ps_name_to_tx",
    title="Reverse-copy printer server name to TX buffer",
    description="""Copies 8 bytes from the RX buffer at offsets `&18..&1F`
(`(net_rx_ptr)+&18..+&1F`) to the TX buffer at offsets
`&10..&17` (`(net_rx_ptr)+&10..+&17`) in reversed byte order.
Implementation: pushes the 8 RX bytes onto the stack, then pops
them back to the TX area; the LIFO order achieves the reversal.""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xB568, "Y=&18: source offset (start of PS name in RX buffer)", align=Align.INLINE)
d.label(0xB56A, "loop_push_ps_name")

d.comment(0xB56A, "Read RX byte at offset Y", align=Align.INLINE)
d.comment(0xB56C, "Push it (the stack reverses the order)", align=Align.INLINE)
d.comment(0xB56D, "Step source", align=Align.INLINE)
d.comment(0xB56E, "Reached &20 (one past the 8-byte name)?", align=Align.INLINE)
d.comment(0xB570, "No: continue pushing", align=Align.INLINE)
d.comment(0xB572, "Y=&17: destination offset for the reversed name", align=Align.INLINE)
d.label(0xB574, "loop_pop_ps_name")

d.comment(0xB574, "Pull next pushed byte (LIFO -> reversed order)", align=Align.INLINE)
d.comment(0xB575, "Store at destination offset Y", align=Align.INLINE)
d.comment(0xB577, "Step destination back", align=Align.INLINE)
d.comment(0xB578, "Reached &0F (one before the destination range)?", align=Align.INLINE)
d.comment(0xB57A, "No: continue popping", align=Align.INLINE)
d.comment(
    0xB57C, "Copy net_rx_ptr_hi as the TX page (TX shares the same page as RX for this packet)", align=Align.INLINE
)
d.comment(0xB57E, "Set net_tx_ptr_hi", align=Align.INLINE)
d.comment(0xB580, "TX low byte = &0C: skip past the TX header to where the reversed name lives", align=Align.INLINE)
d.comment(0xB582, "Set net_tx_ptr lo", align=Align.INLINE)
d.comment(0xB584, "Y=3: copy 4-byte TX header (offsets 3..0)", align=Align.INLINE)
d.label(0xB586, "loop_copy_tx_hdr")

d.comment(0xB586, "Read template byte", align=Align.INLINE)
d.comment(0xB589, "Write to TX buffer at offset Y", align=Align.INLINE)
d.comment(0xB58B, "Step backwards", align=Align.INLINE)
d.comment(0xB58C, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xB58E, "Return", align=Align.INLINE)
d.index_base(0xB58F, "ps_tx_header_template")
d.banner(
    0xB58F,
    title="Printer-server TX header template (4 bytes)",
    description="""Four bytes copied to the head of the printer-server transmit
buffer by [`reverse_ps_name_to_tx`](label:reverse_ps_name_to_tx): control byte
`&80` (immediate-TX request), port `&D1` (printer block port),
function-code stub, and reply-port byte. Filled-in destination
fields follow from the caller's PS slot.""",
)
for i in range(4):
    d.byte(0xB58F + i)

d.comment(0xB58F, "Control byte &80 (immediate TX)", align=Align.INLINE)
d.comment(0xB590, "Port &9F (printer server)", align=Align.INLINE)
d.comment(0xB591, "Station &FF (any)", align=Align.INLINE)
d.comment(0xB592, "Network &FF (any)", align=Align.INLINE)
d.label(0xB593, "print_station_addr")

d.subroutine(
    0xB593,
    "print_station_addr",
    title="Print station address as decimal net.station",
    description="""If the network number is zero, prints only the
station number. Otherwise prints network.station
separated by a dot. V flag controls padding with
leading spaces for column alignment.""",
    on_entry={"v flag": "set = no leading-space padding; clear = pad to align in a column"},
    on_exit={"a, x, y": "clobbered (print_decimal_3dig and OSASCI)"},
)


d.comment(0xB593, "Save caller's V (controls leading-zero padding via the BVS at &B566)", align=Align.INLINE)
d.comment(0xB594, "Read network number (fs_work_6)", align=Align.INLINE)
d.comment(0xB596, "Network 0 means local: skip the 'NN.' prefix", align=Align.INLINE)
d.comment(0xB598, "Network non-zero: print as 3-digit decimal", align=Align.INLINE)
d.comment(0xB59B, "A='.': separator between network and station", align=Align.INLINE)
d.comment(0xB59D, "Print the dot", align=Align.INLINE)
d.comment(
    0xB5A0,
    "Set V so the next BVS branches over the padding (we just printed digits, no padding needed)",
    align=Align.INLINE,
)
d.label(0xB5A3, "skip_if_local_net")

d.comment(0xB5A3, "V set: skip leading-space padding", align=Align.INLINE)
d.comment(0xB5A5, "V clear (caller wanted padding): print 4 leading spaces via inline string", align=Align.INLINE)
d.comment(0xB5AC, "Read station number (fs_work_5)", align=Align.INLINE)
d.label(0xB5AC, "local_net_prefix")

d.comment(
    0xB5AE, "Restore caller's V (so print_decimal_3dig honours its own leading-zero suppression)", align=Align.INLINE
)
d.comment(0xB5AF, "Tail-call print_decimal_3dig for the station number", align=Align.INLINE)
d.label(0xB5B2, "ps_slot_txcb_template")
d.banner(
    0xB5B2,
    title="Printer-server slot TXCB template (12 bytes)",
    description="""12-byte Econet TXCB template for printer-server slot buffers.
Copied by [`init_ps_slot_from_rx`](label:init_ps_slot_from_rx) into workspace
offsets `&78`-`&83` via indexed addressing from
`write_ps_slot_link_addr` (`write_ps_slot_hi_link+1`). Substitutes
`net_rx_ptr_hi` at offsets `&7D` and `&81` (the hi bytes of the
two buffer pointers) so they point into the current RX buffer
page.

Structure: 4-byte header (control, port, station, network)
followed by two 4-byte buffer descriptors (lo address, hi page,
end lo, end hi). End bytes `&FF` are placeholders filled in later
by the caller.""",
)
for i in range(12):
    d.byte(0xB5B2 + i)

d.comment(0xB5B2, "Offset 0: txcb_ctrl = &80 (standard)", align=Align.INLINE)
d.comment(0xB5B3, "Offset 1: txcb_port = &9F (PS port)", align=Align.INLINE)
d.comment(0xB5B4, "Offset 2: dest station (placeholder, &00)", align=Align.INLINE)
d.comment(0xB5B5, "Offset 3: dest network (placeholder, &00)", align=Align.INLINE)
d.comment(0xB5B6, "Offset 4: buf1 start lo = &10", align=Align.INLINE)
d.comment(0xB5B7, "Offset 5: buf1 start hi (page from net_rx_ptr)", align=Align.INLINE)
d.comment(0xB5B8, "Offset 6: buf1 end lo placeholder = &FF", align=Align.INLINE)
d.comment(0xB5B9, "Offset 7: buf1 end hi placeholder = &FF", align=Align.INLINE)
d.comment(0xB5BA, "Offset 8: buf2 start lo = &18", align=Align.INLINE)
d.comment(0xB5BB, "Offset 9: buf2 start hi (page from net_rx_ptr)", align=Align.INLINE)
d.comment(0xB5BC, "Offset 10: buf2 end lo placeholder = &FF", align=Align.INLINE)
d.comment(0xB5BD, "Offset 11: buf2 end hi placeholder = &FF", align=Align.INLINE)
d.entry(0xB5BE)
d.label(0xB5BE, "cmd_pollps")

d.subroutine(
    0xB5BE,
    "cmd_pollps",
    title="*Pollps command handler",
    description="""Initialises the spool drive, copies the PS name to
the TX buffer, and parses an optional station number
or PS name argument. Sends a poll request, then
prints the server address and name. Iterates through
PS slots, displaying each station's status as
'ready', 'busy' (with client station), or 'jammed'.
Marks processed slots with &3F.""",
    on_entry={"y": "command line offset in text pointer"},
)
d.comment(0xB5BE, "Save command line pointer high", align=Align.INLINE)
d.comment(0xB5C0, "Initialise spool/print drive", align=Align.INLINE)
# UNMAPPED: d.comment(0xB586, "Save spool drive number", align=Align.INLINE)
d.comment(0xB5C3, "Copy PS name to TX buffer", align=Align.INLINE)
d.comment(0xB5C6, "Init PS slot from RX data", align=Align.INLINE)
d.comment(0xB5C9, "Restore command line pointer", align=Align.INLINE)
d.comment(0xB5CB, "Save pointer to spool buffer", align=Align.INLINE)
d.comment(0xB5CE, "Get first argument character", align=Align.INLINE)
d.comment(0xB5D0, "End of command line?", align=Align.INLINE)
d.comment(0xB5D2, "Yes: no argument given", align=Align.INLINE)
# UNMAPPED: d.comment(0xB599, "Clear V (= explicit PS name given)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB59A, "Is first char a decimal digit?", align=Align.INLINE)
# UNMAPPED: d.comment(0xB59D, "Yes: station number, skip PS name", align=Align.INLINE)
# UNMAPPED: d.comment(0xB59F, "PS name follows", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5A0, "Save Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5A1, "Load PS server address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5A4, "Restore Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5A5, "Back to Y register", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5A6, "Parse FS/PS arguments", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5A9, "Offset &7A in slot buffer", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5AB, "Get parsed station low", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5AD, "Store station number low", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5B0, "Get parsed network number", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5B2, "Store station number high", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5B4, "Offset &14 in TX buffer", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5B6, "Copy PS data to TX buffer", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5B9, "Get buffer page high", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5BB, "Set TX pointer high byte", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5BD, "Offset &78 in buffer", align=Align.INLINE)
# UNMAPPED: d.comment(0xB5BF, "Set TX pointer low byte", align=Align.INLINE)
# UNMAPPED: d.label(0xB5C3, "no_poll_name_given")

# UNMAPPED: d.comment(0xB5C3, "Set V (= no explicit PS name)", align=Align.INLINE)
# UNMAPPED: d.label(0xB5C6, "skip_if_no_poll_arg")

# UNMAPPED: d.comment(0xB5C6, "V set (no arg): skip to send", align=Align.INLINE)
d.comment(0xB5D4, "Max 6 characters for PS name", align=Align.INLINE)
d.comment(0xB5D6, "Buffer offset for PS name", align=Align.INLINE)
d.comment(0xB5D8, "Space character", align=Align.INLINE)
d.label(0xB5DA, "loop_pad_poll_name")

d.comment(0xB5DA, "Fill buffer position with space", align=Align.INLINE)
d.comment(0xB5DC, "Next position", align=Align.INLINE)
d.comment(0xB5DD, "Count down", align=Align.INLINE)
d.comment(0xB5DE, "Loop until 6 spaces filled", align=Align.INLINE)
d.comment(0xB5E0, "Save pointer to OS text", align=Align.INLINE)
d.comment(0xB5E3, "Restore command line pointer", align=Align.INLINE)
d.comment(0xB5E5, "Initialise string reading", align=Align.INLINE)
d.comment(0xB5E8, "Empty string: skip to send", align=Align.INLINE)
d.comment(0xB5EA, "Max 6 characters", align=Align.INLINE)
d.comment(0xB5EC, "Save updated string pointer", align=Align.INLINE)
d.comment(0xB5EE, "Buffer offset for PS name", align=Align.INLINE)
d.comment(0xB5F0, "Save buffer position", align=Align.INLINE)
d.label(0xB5F2, "loop_read_poll_char")

d.comment(0xB5F2, "Restore string pointer", align=Align.INLINE)
d.comment(0xB5F4, "Read next char from string", align=Align.INLINE)
d.comment(0xB5F7, "Save updated string pointer", align=Align.INLINE)
d.comment(0xB5F9, "End of string: go to send", align=Align.INLINE)
d.comment(0xB5FB, "Store char uppercased in buffer", align=Align.INLINE)
d.comment(0xB5FE, "Loop if more chars to copy", align=Align.INLINE)
d.label(0xB600, "done_poll_name_parse")

d.comment(0xB600, "Enable escape checking", align=Align.INLINE)
d.comment(0xB602, "Set escapable flag", align=Align.INLINE)
d.comment(0xB604, "Send the poll request packet", align=Align.INLINE)
d.comment(0xB607, "Pop and requeue PS scan", align=Align.INLINE)
d.comment(0xB60A, "Print 'Printer server '", align=Align.INLINE)
# UNMAPPED: d.comment(0xB601, "Load PS server address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB604, "Set V and N flags", align=Align.INLINE)
# UNMAPPED: d.comment(0xB607, "Print station address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB60A, "Print ' \"'", align=Align.INLINE)
d.comment(0xB617, "Y=&18: name field offset in RX buffer", align=Align.INLINE)
d.label(0xB619, "loop_print_poll_name")

d.comment(0xB619, "Get character from name field", align=Align.INLINE)
d.comment(0xB61B, "Is it a space?", align=Align.INLINE)
d.comment(0xB61D, "Yes: end of name", align=Align.INLINE)
d.comment(0xB622, "Next character", align=Align.INLINE)
d.comment(0xB623, "Past end of name field?", align=Align.INLINE)
d.comment(0xB625, "No: continue printing name", align=Align.INLINE)
d.label(0xB627, "done_poll_name_print")

d.comment(0xB627, "Print '\"' + CR", align=Align.INLINE)
# UNMAPPED: d.comment(0xB624, "Bit-7 terminator from preceding stringhi", align=Align.INLINE)
# UNMAPPED: d.comment(0xB625, "Pop saved slot index", align=Align.INLINE)
# UNMAPPED: d.label(0xB625, "loop_pollps_next_slot")

d.comment(0xB63A, "Zero: all slots done, return", align=Align.INLINE)
d.comment(0xB63C, "Save slot offset", align=Align.INLINE)
d.comment(0xB63D, "Transfer to Y", align=Align.INLINE)
d.comment(0xB63E, "Read slot status byte", align=Align.INLINE)
d.comment(0xB640, "Bit 7 clear: slot inactive", align=Align.INLINE)
d.comment(0xB642, "Advance to station number", align=Align.INLINE)
d.comment(0xB643, "Offset+2 in slot", align=Align.INLINE)
d.comment(0xB644, "Read station number low", align=Align.INLINE)
d.comment(0xB646, "Store station low", align=Align.INLINE)
d.comment(0xB648, "Next byte (offset+3)", align=Align.INLINE)
d.comment(0xB649, "Read network number", align=Align.INLINE)
d.comment(0xB64B, "Store network number", align=Align.INLINE)
d.comment(0xB64D, "Next byte (offset+4)", align=Align.INLINE)
d.comment(0xB64E, "Read status page pointer", align=Align.INLINE)
d.comment(0xB650, "Store pointer low", align=Align.INLINE)
d.comment(0xB652, "Clear V flag", align=Align.INLINE)
d.comment(0xB653, "Print station address (V=0)", align=Align.INLINE)
d.comment(0xB656, "Print ' is '", align=Align.INLINE)
d.comment(0xB65D, "X=0: indexed-indirect access mode", align=Align.INLINE)
d.comment(0xB65F, "Read printer status byte", align=Align.INLINE)
d.comment(0xB661, "Non-zero: not ready", align=Align.INLINE)
d.comment(0xB663, "Print 'ready'", align=Align.INLINE)
# UNMAPPED: d.comment(0xB657, "Ensure V clear so next BVC always taken", align=Align.INLINE)
# UNMAPPED: d.label(0xB65A, "check_poll_jammed")

# UNMAPPED: d.comment(0xB65A, "Status = 2?", align=Align.INLINE)
# UNMAPPED: d.comment(0xB65C, "No: check for busy", align=Align.INLINE)
# UNMAPPED: d.label(0xB65E, "print_poll_jammed")

# UNMAPPED: d.comment(0xB65E, "Print 'jammed'", align=Align.INLINE)
# UNMAPPED: d.comment(0xB667, "Clear V", align=Align.INLINE)
# UNMAPPED: d.label(0xB66A, "check_poll_busy")

# UNMAPPED: d.comment(0xB66A, "Status = 1?", align=Align.INLINE)
# UNMAPPED: d.comment(0xB66C, "Not 1 or 2: default to jammed", align=Align.INLINE)
d.comment(0xB6A2, "Print 'busy'", align=Align.INLINE)
d.comment(0xB6A9, "Advance work_ae to next status byte (lo)", align=Align.INLINE)
d.comment(0xB6AB, "Read client station number", align=Align.INLINE)
d.comment(0xB6AD, "Store station low", align=Align.INLINE)
d.comment(0xB6AF, "Zero: no client info, skip", align=Align.INLINE)
d.comment(0xB6B1, "Print ' with station '", align=Align.INLINE)
d.comment(0xB6C2, "Advance work_ae to next status byte (lo)", align=Align.INLINE)
d.comment(0xB6C4, "Read network number byte via (work_ae,X)", align=Align.INLINE)
d.comment(0xB6C6, "Store network number", align=Align.INLINE)
d.comment(0xB6C8, "Set V flag", align=Align.INLINE)
d.comment(0xB6CB, "Print client station address", align=Align.INLINE)
# UNMAPPED: d.label(0xB69A, "done_poll_status_line")

# UNMAPPED: d.label(0xB69D, "done_poll_slot_mark")

# UNMAPPED: d.comment(0xB69D, "Retrieve slot offset", align=Align.INLINE)
# UNMAPPED: d.comment(0xB69E, "Transfer to Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB69F, "Mark slot as processed (&3F)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB6A1, "Write marker to workspace", align=Align.INLINE)
# UNMAPPED: d.label(0xB6A5, "rts_poll_slots")

# UNMAPPED: d.comment(0xB6A5, "Return", align=Align.INLINE)
d.label(0xB6D1, "init_ps_slot_from_rx")

d.subroutine(
    0xB6D1,
    "init_ps_slot_from_rx",
    title="Initialise PS slot buffer from template data",
    description="""Copies the 12-byte
[`ps_slot_txcb_template`](label:ps_slot_txcb_template) into workspace at
offsets &78-&83 via indexed addressing from
`write_ps_slot_link_addr` (`write_ps_slot_hi_link+1`).
Substitutes `net_rx_ptr_hi` at offsets &7D and &81 (the hi bytes
of the two buffer pointers) so they point into the current RX
buffer page.""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xB6D1, "Start at offset &78", align=Align.INLINE)
d.label(0xB6D3, "loop_copy_slot_tmpl")

d.comment(0xB6D3, "Load template byte", align=Align.INLINE)
d.comment(0xB6D6, "At offset &7D?", align=Align.INLINE)
d.comment(0xB6D8, "Yes: substitute RX page", align=Align.INLINE)
d.comment(0xB6DA, "At offset &81?", align=Align.INLINE)
d.comment(0xB6DC, "No: use template byte", align=Align.INLINE)
d.label(0xB6DE, "subst_rx_page_byte")

d.comment(0xB6DE, "Use RX buffer page instead", align=Align.INLINE)
d.label(0xB6E0, "store_slot_tmpl_byte")

d.comment(0xB6E0, "Store byte in slot buffer", align=Align.INLINE)
d.comment(0xB6E2, "Next offset", align=Align.INLINE)
d.comment(0xB6E3, "Past end of slot (&84)?", align=Align.INLINE)
d.comment(0xB6E5, "No: continue copying", align=Align.INLINE)
d.comment(0xB6E7, "Return", align=Align.INLINE)
d.label(0xB6E8, "store_char_uppercase")

d.subroutine(
    0xB6E8,
    "store_char_uppercase",
    title="Convert to uppercase and store in RX buffer",
    description="""If the character in A is lowercase (&61-&7A), converts
to uppercase by clearing bit 5. Stores the result in
the RX buffer at the current position, advances the
buffer pointer, and decrements the character count.""",
    on_entry={"a": "character to store"},
)


d.comment(0xB6E8, "Y = current buffer position", align=Align.INLINE)
d.comment(0xB6EA, "Strip high bit", align=Align.INLINE)
d.comment(0xB6EC, "Is it lowercase 'a' or above?", align=Align.INLINE)
d.comment(0xB6EE, "Below 'a': not lowercase", align=Align.INLINE)
d.comment(0xB6F0, "Above 'z'?", align=Align.INLINE)
d.comment(0xB6F2, "Yes: not lowercase", align=Align.INLINE)
d.comment(0xB6F4, "Convert to uppercase", align=Align.INLINE)
d.label(0xB6F6, "done_uppercase_store")

d.comment(0xB6F6, "Store in RX buffer", align=Align.INLINE)
d.comment(0xB6F8, "Next buffer position", align=Align.INLINE)
d.comment(0xB6F9, "Update buffer position", align=Align.INLINE)
d.comment(0xB6FB, "Decrement character count", align=Align.INLINE)
d.comment(0xB6FC, "Return (Z set if count=0)", align=Align.INLINE)
d.entry(0xB6FD)
d.entry(0xB6FD)
d.subroutine(
    0xB6FD,
    "cmd_prot",
    title="*Prot command handler",
    description="""Loads `A=&FF` (full protection mask) and falls through (via an
always-taken `BNE`) to the shared protection-update body at
`&B6D8`, which:

1. Saves the new flag (`Z=0` for *Prot, `Z=1` for *Unprot) on the
   stack via `PHP`.
2. Calls [`set_via_shadow_pair`](address:AABB) to mirror `A` into
   the workspace shadow ACR (`prot_status`) and shadow IER
   (`prot_status_save`).
3. Reads CMOS RAM byte `&11` (Econet station/protection flags)
   via [`osbyte_a1`](label:osbyte_a1) into `Y`, copies to `A`.
4. Restores the saved flag and selects:
   - *Prot path: `ORA #&40` (set bit 6 = protection on).
   - *Unprot path: `AND #&BF` (clear bit 6).
5. Writes the updated byte back to CMOS via OSBYTE `&A2`
   (write CMOS RAM).

The ANFS protection state lives in CMOS bit 6 of byte `&11`, so it
survives BREAK and power-cycle until explicitly toggled.""",
    on_entry={"y": "command line offset (unused; *Prot takes no args)"},
)


d.comment(0xB6FD, "Load &FF (protect)", align=Align.INLINE)
d.entry(0xB701)
d.entry(0xB701)


d.subroutine(
    0xB701,
    "cmd_unprot",
    title="*Unprot command handler",
    description="""Loads `A=&00` (no protection) and falls through to the shared
protection-update body at `&B6D8`, which clears bit 6 of CMOS RAM
byte `&11` (the Econet protection flag). See
[`cmd_prot`](label:cmd_prot) for the full body description.""",
    on_entry={"y": "command line offset (unused; *Unprot takes no args)"},
)


d.comment(0xB701, "Load &00 (unprotect)", align=Align.INLINE)
d.label(0xB703, "unprot_clear")

d.comment(0xB703, "Save Z flag (1 = unprot, 0 = prot) for later", align=Align.INLINE)
d.comment(0xB704, "Mirror A into prot_status / prot_status_save pair", align=Align.INLINE)
d.comment(0xB707, "X=&11: CMOS offset for Econet flags", align=Align.INLINE)
d.comment(0xB709, "OSBYTE &A1 reads CMOS byte &11 -> Y", align=Align.INLINE)
d.comment(0xB70C, "A = current CMOS byte", align=Align.INLINE)
d.comment(0xB70D, "Restore the saved Z flag", align=Align.INLINE)
d.comment(0xB70E, "Z=1: unprot path", align=Align.INLINE)
d.comment(0xB710, "Set bit 6 (protection on)", align=Align.INLINE)
d.comment(0xB712, "ALWAYS branch to write-back", align=Align.INLINE)
d.label(0xB714, "unprot_check")

d.comment(0xB714, "Clear bit 6 (protection off)", align=Align.INLINE)
d.label(0xB716, "unprot_apply")

d.comment(0xB716, "Y = new flag byte", align=Align.INLINE)
d.comment(0xB717, "OSBYTE &A2: write CMOS byte", align=Align.INLINE)
d.label(0xB719, "loop_match_prot_attr")

d.comment(0xB719, "X=&11: CMOS offset for Econet flags", align=Align.INLINE)
d.comment(0xB71B, "Tail-call OSBYTE", align=Align.INLINE)
d.comment(0xB71E, "Reset access flags before parsing the new argument", align=Align.INLINE)
d.entry(0xB71E)

d.label(0xB71E, "cmd_wipe")


d.subroutine(
    0xB71E,
    "cmd_wipe",
    title="*Wipe command handler",
    description="""Setup half of *Wipe. Masks owner access via
[`mask_owner_access`](label:mask_owner_access), zeroes the file-iteration
counter [`fs_work_5`](label:fs_work_5), preserves the command-line
pointer with [`save_ptr_to_os_text`](label:save_ptr_to_os_text), parses the
wildcard filename via [`parse_filename_arg`](label:parse_filename_arg), and
records the end-of-argument offset (X+1) in
[`fs_work_6`](label:fs_work_6). Falls through to
[`request_next_wipe`](label:request_next_wipe), which drives the per-file
examine/prompt/delete loop until the wildcard is exhausted.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xB721, "A=0: clear the file-iteration counter", align=Align.INLINE)
d.comment(0xB723, "Store iteration counter (steps to next file each loop)", align=Align.INLINE)
d.comment(0xB725, "Save text pointer for re-reading the wildcard each iteration", align=Align.INLINE)
d.comment(0xB728, "Parse the wildcard filename into the &C030 buffer", align=Align.INLINE)
d.comment(0xB72B, "Step X past the CR terminator (so X = filename length+1)", align=Align.INLINE)
d.comment(0xB72C, "Save end-of-buffer offset", align=Align.INLINE)
d.label(0xB72E, "request_next_wipe")

d.subroutine(
    0xB72E,
    "request_next_wipe",
    title="Build 'examine directory' TXCB for next wipe iteration",
    description="""Issues FS function-code 1 ('examine directory entry') for the
current iteration in fs_work_5. Writes the function code into
TXCB[5] and TXCB[7], copies the iteration index to TXCB[6], and
falls through to the TXCB-build / send sequence. Single caller
(the BNE retry at &B768 that loops cmd_wipe over each match).""",
)


d.comment(0xB72E, "FS function code byte 0 = 1 (examine)", align=Align.INLINE)
d.comment(0xB730, "TXCB[5] = 1: 'examine directory entry'", align=Align.INLINE)
d.comment(0xB733, "TXCB[7] = 1: ditto for the second buffer slot", align=Align.INLINE)
d.comment(0xB736, "Load current iteration index", align=Align.INLINE)
d.comment(0xB738, "TXCB[6] = iteration index (which directory entry)", align=Align.INLINE)
d.comment(0xB73B, "X=3: copy starting at TX[3] (after the FS header bytes)", align=Align.INLINE)
d.comment(0xB73D, "Copy the parsed filename into the TX buffer", align=Align.INLINE)
d.comment(0xB740, "Y=3: FS function code 'Examine'", align=Align.INLINE)
d.comment(0xB742, "A=&80: set bit 7 of need_release_tube to flag long-lived TX", align=Align.INLINE)
d.comment(0xB744, "Store flag", align=Align.INLINE)
d.comment(0xB746, "Send the examine request and wait for reply", align=Align.INLINE)
d.comment(0xB749, "Read FS reply byte 0 (status code)", align=Align.INLINE)
d.comment(0xB74C, "Non-zero status: process the response", align=Align.INLINE)
d.comment(0xB74E, "OSBYTE &0F: flush input buffer class", align=Align.INLINE)
d.comment(0xB750, "X=1: flush keyboard buffer", align=Align.INLINE)
d.comment(0xB752, "Flush keyboard buffer (clear pending Y/N keypress)", align=Align.INLINE)
d.comment(0xB755, "OSBYTE &7A: scan keyboard from key 16 (clear keypress queue)", align=Align.INLINE)
d.comment(0xB757, "Run the scan", align=Align.INLINE)
d.comment(0xB75A, "Y=0: no key", align=Align.INLINE)
d.comment(0xB75C, "OSBYTE &78: write keys-pressed state", align=Align.INLINE)
d.comment(0xB75E, "Tail-call OSBYTE: clean up and return", align=Align.INLINE)
d.label(0xB761, "check_wipe_attr")

d.comment(0xB761, "Read attribute byte from FS reply (TXCB[&2F])", align=Align.INLINE)
d.label(0xB764, "loop_check_if_locked")

d.comment(0xB764, "Is it 'L' (locked)?", align=Align.INLINE)
d.comment(0xB766, "Not locked: check for directory", align=Align.INLINE)
d.label(0xB768, "skip_wipe_locked")

d.comment(0xB768, "Locked: skip this file, advance to next", align=Align.INLINE)
d.comment(0xB76A, "Loop back to request the next directory entry", align=Align.INLINE)
d.label(0xB76D, "check_wipe_dir")

d.comment(0xB76D, "Is it 'D' (directory)?", align=Align.INLINE)
d.comment(0xB76F, "Not a directory: prompt the user", align=Align.INLINE)
d.comment(0xB771, "Directory: check second attribute byte (size)", align=Align.INLINE)
d.comment(0xB774, "Loop back to attribute test (re-checks if non-empty)", align=Align.INLINE)
d.label(0xB776, "show_wipe_prompt")

d.comment(0xB776, "X=1: scan name starting at TX[1]", align=Align.INLINE)
d.comment(0xB778, "Y = end-of-buffer offset (saved earlier in fs_work_6)", align=Align.INLINE)
d.label(0xB77A, "loop_copy_wipe_name")

d.comment(0xB77A, "Read filename byte from TX[6+X]", align=Align.INLINE)
d.comment(0xB77D, "Print via *SPOOL-bypassing OSASCI", align=Align.INLINE)
d.comment(0xB780, "Also store into the parse buffer for later use", align=Align.INLINE)
d.comment(0xB783, "Step parse-buffer offset", align=Align.INLINE)
d.comment(0xB784, "Step TX-buffer offset", align=Align.INLINE)
d.comment(0xB785, "Reached &0C (12 chars)?", align=Align.INLINE)
d.comment(0xB787, "No: continue copying", align=Align.INLINE)
d.comment(0xB789, "Print '(?/' prompt prefix and read response", align=Align.INLINE)
d.comment(0xB78C, "Inline string '(?/' is read by the hook above", align=Align.INLINE)
d.comment(0xB78F, "NOP -- bit-7 terminator + resume opcode for the '(?/' stringhi", align=Align.INLINE)
d.comment(0xB790, "Print 'Y/N) ' via prompt_yn (reads keypress)", align=Align.INLINE)
d.comment(0xB793, "Was the keypress '?' (help)?", align=Align.INLINE)
d.comment(0xB795, "Not '?': process Y/N response", align=Align.INLINE)
d.comment(0xB797, "'?': print CR before help text", align=Align.INLINE)
d.comment(0xB799, "Print CR character", align=Align.INLINE)
d.comment(0xB79C, "X=2: start of name in TX[2]", align=Align.INLINE)
d.label(0xB79E, "loop_print_wipe_info")

d.comment(0xB79E, "Read name byte from TX[5+X] (FS reply)", align=Align.INLINE)
d.comment(0xB7A1, "Print name char (no spool)", align=Align.INLINE)
d.comment(0xB7A4, "Advance index", align=Align.INLINE)
d.comment(0xB7A5, "End of TX[5+X] name field at offset &3E?", align=Align.INLINE)
d.comment(0xB7A7, "No: continue printing", align=Align.INLINE)
d.comment(0xB7A9, "Print 'Wipe? ' help suffix via inline string", align=Align.INLINE)
d.comment(0xB7AE, "Bit-7 terminator + resume", align=Align.INLINE)
d.comment(0xB7AF, "Re-prompt user with prompt_yn", align=Align.INLINE)
d.label(0xB7B2, "check_wipe_response")

d.comment(0xB7B2, "Mask to upper-case ('A'..'Z' map to themselves)", align=Align.INLINE)
d.comment(0xB7B4, "Was the response 'Y'?", align=Align.INLINE)
d.comment(0xB7B6, "No: skip this entry, advance to next", align=Align.INLINE)
d.comment(0xB7B8, "Yes: echo the keypress", align=Align.INLINE)
d.comment(0xB7BB, "X=0: start scanning the parse-buffer name", align=Align.INLINE)
d.comment(0xB7BD, "Read first parse-buffer byte at hazel_parse_buf", align=Align.INLINE)
d.comment(0xB7C0, "Is it CR (no path component)?", align=Align.INLINE)
d.comment(0xB7C2, "Yes: use leaf-name only path at &B7E8", align=Align.INLINE)
d.label(0xB7C4, "loop_build_wipe_cmd")

d.comment(0xB7C4, "Read parse-buffer byte at hazel_parse_buf+X", align=Align.INLINE)
d.comment(0xB7C7, "Is it CR (end of name)?", align=Align.INLINE)
d.comment(0xB7C9, "No: check for space separator", align=Align.INLINE)
d.comment(0xB7CB, "CR: substitute '.' so the dir prefix terminates with a separator", align=Align.INLINE)
d.label(0xB7CD, "skip_if_not_space")

d.comment(0xB7CD, "Is it space?", align=Align.INLINE)
d.comment(0xB7CF, "No: store byte as-is", align=Align.INLINE)
d.label(0xB7D1, "set_wipe_cr_end")

d.comment(0xB7D1, "Yes: substitute CR (end-of-cmd)", align=Align.INLINE)
d.label(0xB7D3, "store_wipe_tx_char")

d.comment(0xB7D3, "Store byte into TX[5+X] (delete-command buffer)", align=Align.INLINE)
d.comment(0xB7D6, "Advance index", align=Align.INLINE)
d.comment(0xB7D7, "Was that byte CR (just stored)?", align=Align.INLINE)
d.comment(0xB7D9, "No: continue copying", align=Align.INLINE)
d.comment(0xB7DB, "Y=&14: FS function code &14 = delete", align=Align.INLINE)
d.comment(0xB7DD, "Send the delete request and wait for reply", align=Align.INLINE)
d.comment(0xB7E0, "Decrement iteration counter so we re-examine the now-shifted-up slot", align=Align.INLINE)
d.label(0xB7E2, "skip_wipe_to_next")

d.comment(0xB7E2, "Print newline before next entry", align=Align.INLINE)
d.comment(0xB7E5, "Loop back to skip_wipe_locked (= request next entry)", align=Align.INLINE)
d.label(0xB7E8, "use_wipe_leaf_name")

d.comment(0xB7E8, "DEX: pre-decrement before the INX in the loop", align=Align.INLINE)
d.label(0xB7E9, "loop_copy_wipe_leaf")

d.comment(0xB7E9, "Advance index", align=Align.INLINE)
d.comment(0xB7EA, "Read parse-buffer byte at hazel_parse_buf_1+X (skip CR at hazel_parse_buf)", align=Align.INLINE)
d.comment(0xB7ED, "Store into TX[5+X] (delete-command buffer)", align=Align.INLINE)
d.comment(0xB7F0, "Reached space (end-of-leaf)?", align=Align.INLINE)
d.comment(0xB7F2, "No: continue copying", align=Align.INLINE)
d.comment(0xB7F6, "Print 'Y/N) ' via the inline-string helper", align=Align.INLINE)
d.subroutine(
    0xB7F6,
    "prompt_yn",
    title="Print Y/N prompt and read user response",
    description="""Prints 'Y/N) ' via inline string, flushes
the input buffer, and reads a single character
from the keyboard.""",
    on_entry={},
    on_exit={"A": "character read from keyboard (after the 'Y/N) ' prompt)"},
)
d.comment(0xB7F9, "Inline string body — bytes consumed by print_inline_no_spool (above)", align=Align.INLINE)
d.label(0xB7FE, "flush_and_read_char")

d.subroutine(
    0xB7FE,
    "flush_and_read_char",
    title="Flush keyboard buffer and read one character",
    description="""Calls OSBYTE &0F to flush the input buffer, then
OSRDCH to read a single character. Raises an escape
error if escape was pressed (carry set on return).""",
    on_entry={},
    on_exit={"a": "character read from keyboard", "x, y": "clobbered (OSBYTE/OSRDCH)"},
)


d.comment(0xB7FE, "OSBYTE &0F: flush buffer class", align=Align.INLINE)
d.comment(0xB800, "X=1: flush input buffers", align=Align.INLINE)
d.comment(0xB802, "Flush keyboard buffer before read", align=Align.INLINE)
d.comment(0xB805, "Read character from input stream", align=Align.INLINE)
d.comment(0xB808, "C clear: character read OK", align=Align.INLINE)
d.comment(0xB80A, "Escape pressed: raise error", align=Align.INLINE)
d.comment(0xB80D, "Return with character in A", align=Align.INLINE)
d.label(0xB80E, "init_channel_table")

d.subroutine(
    0xB80E,
    "init_channel_table",
    title="Initialise channel allocation table",
    description="""Clears all 256 bytes of the table, then marks
available channel slots based on the count from
the receive buffer. Sets the first slot to &C0
(active channel marker).""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xB80E, "A=0: clear value", align=Align.INLINE)
d.comment(0xB810, "Y=0: start index", align=Align.INLINE)
d.label(0xB811, "loop_clear_chan_table")

d.comment(0xB811, "Clear channel table entry", align=Align.INLINE)
d.comment(0xB814, "Next entry", align=Align.INLINE)
d.comment(0xB815, "Loop until all 256 bytes cleared", align=Align.INLINE)
d.comment(0xB817, "Offset &0F in receive buffer", align=Align.INLINE)
d.comment(0xB819, "Get number of available channels", align=Align.INLINE)
d.comment(0xB81B, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB81C, "Subtract 'Z' to get negative count", align=Align.INLINE)
d.comment(0xB81E, "Y = negative channel count (index)", align=Align.INLINE)
d.comment(0xB81F, "Channel marker &40 (available)", align=Align.INLINE)
d.label(0xB821, "loop_mark_chan_avail")

d.comment(0xB821, "Mark channel slot as available", align=Align.INLINE)
d.comment(0xB824, "Previous channel slot", align=Align.INLINE)
d.comment(0xB825, "Reached start of channel range?", align=Align.INLINE)
d.comment(0xB827, "No: continue marking channels", align=Align.INLINE)
d.comment(0xB829, "Point to first channel slot", align=Align.INLINE)
d.comment(0xB82A, "Active channel marker &C0", align=Align.INLINE)
d.comment(0xB82C, "Mark first channel as active", align=Align.INLINE)
d.comment(0xB82F, "Return", align=Align.INLINE)
d.label(0xB830, "attr_to_chan_index")

d.subroutine(
    0xB830,
    "attr_to_chan_index",
    title="Convert channel attribute to table index",
    description="""Subtracts &20 from the attribute byte and clamps
to the range 0-&0F. Returns &FF if out of range.
Preserves processor flags via PHP/PLP.""",
    on_entry={"a": "channel attribute byte"},
    on_exit={"a": "table index (0-&0F) or &FF if invalid"},
)


d.comment(0xB830, "Save flags", align=Align.INLINE)
d.comment(0xB831, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB832, "Subtract &20 to get table index", align=Align.INLINE)
d.comment(0xB834, "Negative: out of valid range", align=Align.INLINE)
d.comment(0xB836, "Above maximum channel index &0F?", align=Align.INLINE)
d.comment(0xB838, "In range: valid index", align=Align.INLINE)
d.label(0xB83A, "error_chan_out_of_range")

d.comment(0xB83A, "Out of range: return &FF (invalid)", align=Align.INLINE)
d.label(0xB83C, "return_chan_index")

d.comment(0xB83C, "Restore flags", align=Align.INLINE)
d.comment(0xB83D, "X = channel index (or &FF)", align=Align.INLINE)
d.comment(0xB83E, "Return", align=Align.INLINE)
d.label(0xB83F, "check_chan_char")

d.subroutine(
    0xB83F,
    "check_chan_char",
    title="Validate channel character and look up entry",
    description="""Characters below '0' are looked up directly in
the channel table. Characters '0' and above are
converted to a table index via attr_to_chan_index.
Raises 'Net channel' error if invalid.""",
    on_entry={"a": "channel character"},
)


d.comment(0xB83F, "Below space?", align=Align.INLINE)
d.comment(0xB841, "Yes: invalid channel character", align=Align.INLINE)
d.comment(0xB843, "Below '0'?", align=Align.INLINE)
d.comment(0xB845, "In range &20-&2F: look up channel", align=Align.INLINE)
d.label(0xB847, "err_net_chan_invalid")

d.subroutine(
    0xB847,
    "err_net_chan_invalid",
    title="Raise 'Net channel' error (saving channel char on stack)",
    description="""Pushes the bad channel character on the stack, then falls through to
error_chan_not_found which loads error code &DE and tail-calls
error_inline_log with the inline string 'Net channel'. The PHA at
entry differs from the &B81F error_chan_not_found alt-entry: this
form is reached when the caller has the channel character in A and
wants it preserved on the stack for the error handler to inspect.
Never returns -- error_inline_log triggers a BRK.""",
    on_entry={"a": "channel character (saved on stack)"},
)


d.comment(0xB847, "Save channel character", align=Align.INLINE)
d.label(0xB848, "error_chan_not_found")

d.comment(0xB848, "Error code &DE", align=Align.INLINE)
d.label(0xB84A, "err_net_chan_not_found")

d.comment(0xB84A, "Generate 'Net channel' error", align=Align.INLINE)
d.label(0xB84C, "net_chan_err_strings")
d.comment(0xB859, "Error string continuation (unreachable)", align=Align.INLINE)
d.comment(0xB85C, "Clear tx_buffer_scratch+X scratch", align=Align.INLINE)
d.label(0xB872, "lookup_chan_by_char")

d.subroutine(
    0xB872,
    "lookup_chan_by_char",
    title="Look up channel by character code",
    description="""Subtracts `&20` from the character to produce a table index
(inlining the same arithmetic as
[`attr_to_chan_index`](label:attr_to_chan_index) without the bounds check),
loads the channel slot's `hazel_fcb_slot_attr` byte; on zero
raises `error_chan_not_found`. Otherwise verifies station/network
via [`match_station_net`](label:match_station_net) and returns the slot's
flags in `A`.""",
    on_entry={"a": "channel character"},
    on_exit={"a": "channel flags"},
)


d.comment(0xB872, "Save channel character", align=Align.INLINE)
d.comment(0xB873, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB874, "Convert char to table index", align=Align.INLINE)
d.comment(0xB876, "X = channel table index", align=Align.INLINE)
d.comment(0xB877, "Look up network number for channel", align=Align.INLINE)
d.comment(0xB87A, "Zero: channel not found, raise error", align=Align.INLINE)
d.comment(0xB87C, "Check station/network matches current", align=Align.INLINE)
d.comment(0xB87F, "No match: build detailed error msg", align=Align.INLINE)
d.comment(0xB881, "Discard saved channel character", align=Align.INLINE)
d.comment(0xB882, "Load channel status flags", align=Align.INLINE)
d.comment(0xB885, "Return; A = channel flags", align=Align.INLINE)
d.label(0xB886, "error_chan_not_here")

d.comment(0xB886, "Error code &DE", align=Align.INLINE)
d.comment(0xB888, "Store error code in error block", align=Align.INLINE)
d.comment(0xB88B, "BRK opcode", align=Align.INLINE)
d.comment(0xB88D, "Store BRK at start of error block", align=Align.INLINE)
d.comment(0xB890, "X=0: copy index", align=Align.INLINE)
d.label(0xB891, "loop_copy_chan_err_str")

d.comment(0xB891, "Advance copy position", align=Align.INLINE)
d.comment(0xB892, "Load 'Net channel' string byte", align=Align.INLINE)
d.comment(0xB895, "Copy to error text", align=Align.INLINE)
d.comment(0xB898, "Continue until NUL terminator", align=Align.INLINE)
d.comment(0xB89A, "Save end-of-string position", align=Align.INLINE)
d.comment(0xB89C, "Save for suffix append", align=Align.INLINE)
d.comment(0xB89E, "Retrieve channel character", align=Align.INLINE)
d.comment(0xB89F, "Append ' N' (channel number)", align=Align.INLINE)
d.comment(0xB8A2, "Load 'Net channel' end position", align=Align.INLINE)
d.label(0xB8A4, "loop_append_err_suffix")

d.comment(0xB8A4, "Skip past NUL to suffix string", align=Align.INLINE)
d.comment(0xB8A5, "Advance destination position", align=Align.INLINE)
d.comment(0xB8A6, "Load ' not on this...' suffix byte", align=Align.INLINE)
d.comment(0xB8A9, "Append to error message", align=Align.INLINE)
d.comment(0xB8AC, "Continue until NUL", align=Align.INLINE)
d.comment(0xB8AE, "Raise the constructed error", align=Align.INLINE)
d.label(0xB8B1, "store_result_check_dir")

d.subroutine(
    0xB8B1,
    "store_result_check_dir",
    title="Store channel attribute and check not directory",
    description="""Writes the current channel attribute to the receive
buffer, then tests the directory flag (bit 1). Raises
'Is a dir.' error if the attribute refers to a
directory rather than a file.""",
    on_entry={"a": "channel attribute byte to store and check"},
)


d.comment(0xB8B1, "Load current channel attribute", align=Align.INLINE)
d.comment(0xB8B4, "Store channel attribute to RX buffer", align=Align.INLINE)
d.label(0xB8B7, "check_not_dir")

d.subroutine(
    0xB8B7,
    "check_not_dir",
    title="Validate channel is not a directory",
    description="""Calls check_chan_char to validate the channel, then
tests the directory flag (bit 1). Raises 'Is a dir.'
error if the channel refers to a directory.""",
    on_entry={"a": "channel character (validated by check_chan_char)"},
)


d.comment(0xB8B7, "Validate and look up channel", align=Align.INLINE)
d.comment(0xB8BA, "Test directory flag (bit 1)", align=Align.INLINE)
d.comment(0xB8BC, "Not a directory: return OK", align=Align.INLINE)
d.comment(0xB8BE, "Error code &A8", align=Align.INLINE)
d.comment(0xB8C0, "Generate 'Is a dir.' error", align=Align.INLINE)
d.comment(0xB8D2, "Return", align=Align.INLINE)
d.label(0xB8D3, "alloc_fcb_slot")

d.subroutine(
    0xB8D3,
    "alloc_fcb_slot",
    title="Allocate a free file control block slot",
    description="""Scans FCB slots &20-&2F for an empty entry.
Returns Z=0 with X=slot index on success, or
Z=1 with A=0 if all slots are occupied.""",
    on_exit={"x": "slot index (if Z=0)", "z": "0=success, 1=no free slot"},
)


d.comment(0xB8D3, "Save channel attribute", align=Align.INLINE)
d.comment(0xB8D4, "Start scanning from FCB slot &20", align=Align.INLINE)
d.label(0xB8D6, "loop_scan_fcb_slots")

d.comment(0xB8D6, "Load FCB station byte", align=Align.INLINE)
d.comment(0xB8D9, "Zero: slot is free, use it", align=Align.INLINE)
d.comment(0xB8DB, "Try next slot", align=Align.INLINE)
d.comment(0xB8DC, "Past last FCB slot &2F?", align=Align.INLINE)
d.comment(0xB8DE, "No: check next slot", align=Align.INLINE)
d.comment(0xB8E0, "No free slot: discard saved attribute", align=Align.INLINE)
d.comment(0xB8E1, "A=0: return failure (Z set)", align=Align.INLINE)
d.comment(0xB8E3, "Return", align=Align.INLINE)
d.label(0xB8E4, "done_found_free_slot")

d.comment(0xB8E4, "Restore channel attribute", align=Align.INLINE)
d.comment(0xB8E5, "Store attribute in FCB slot", align=Align.INLINE)
d.comment(0xB8E8, "A=0: clear value", align=Align.INLINE)
d.comment(0xB8EA, "Clear FCB transfer count low", align=Align.INLINE)
d.comment(0xB8ED, "Clear FCB transfer count mid", align=Align.INLINE)
d.comment(0xB8F0, "Clear FCB transfer count high", align=Align.INLINE)
d.comment(0xB8F3, "Load current station number", align=Align.INLINE)
d.comment(0xB8F6, "Store station in FCB", align=Align.INLINE)
d.comment(0xB8F9, "Load current network number", align=Align.INLINE)
d.comment(0xB8FC, "Store network in FCB", align=Align.INLINE)
d.comment(0xB8FF, "Get FCB slot index", align=Align.INLINE)
d.comment(0xB900, "Save slot index", align=Align.INLINE)
d.comment(0xB901, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB902, "Convert slot to channel index (0-&0F)", align=Align.INLINE)
d.comment(0xB904, "X = channel index", align=Align.INLINE)
d.comment(0xB905, "Restore A = FCB slot index", align=Align.INLINE)
d.comment(0xB906, "Return; A=slot, X=channel, Z clear", align=Align.INLINE)
d.label(0xB907, "alloc_fcb_or_error")

d.subroutine(
    0xB907,
    "alloc_fcb_or_error",
    title="Allocate FCB slot or raise error",
    description="""Calls alloc_fcb_slot and raises 'No more FCBs'
if no free slot is available. Preserves the
caller's argument on the stack.""",
    on_entry={"a": "caller's argument byte (saved/restored via PHA/PLA across the alloc call)"},
    on_exit={"x": "newly allocated FCB slot index (&20-&2F)", "a": "preserved"},
)


d.comment(0xB907, "Save argument", align=Align.INLINE)
d.comment(0xB908, "A=0: allocate any available slot", align=Align.INLINE)
d.comment(0xB90A, "Try to allocate an FCB slot", align=Align.INLINE)
d.comment(0xB90D, "Success: slot allocated", align=Align.INLINE)
d.comment(0xB90F, "Error code &C0", align=Align.INLINE)
d.comment(0xB911, "Generate 'No more FCBs' error", align=Align.INLINE)
d.label(0xB928, "return_alloc_success")

d.comment(0xB928, "Restore argument", align=Align.INLINE)
d.comment(0xB929, "Return", align=Align.INLINE)
d.label(0xB92A, "close_all_net_chans")

d.subroutine(
    0xB92A,
    "close_all_net_chans",
    title="Close all network channels for current station",
    description="""Scans FCB slots &0F down to 0, closing those
matching the current station. C=0 closes all
matching entries; C=1 closes with write-flush.""",
    on_entry={"c": "0=close all, 1=close with write-flush"},
)


d.comment(0xB92A, "C=0: close all matching channels", align=Align.INLINE)
d.label(0xB92B, "skip_set_carry")

d.comment(0xB92B, "Branch always to scan entry", align=Align.INLINE)
d.label(0xB92E, "scan_fcb_flags")

d.subroutine(
    0xB92E,
    "scan_fcb_flags",
    title="Scan FCB slot flags from &10 downward",
    description="""Iterates through FCB slots starting at &10,
checking each slot's flags byte. Returns when
all slots have been processed.""",
    on_exit={
        "x": "last scanned FCB index",
        "z flag": "set if a matching slot was found (via fall-through into match_station_net)",
    },
)


d.comment(0xB92E, "Start from FCB slot &10", align=Align.INLINE)
d.label(0xB930, "loop_scan_fcb_down")

d.comment(0xB930, "Previous FCB slot", align=Align.INLINE)
d.comment(0xB931, "More slots to check", align=Align.INLINE)
d.comment(0xB933, "All FCB slots processed, return", align=Align.INLINE)
d.label(0xB934, "skip_if_slots_done")

d.comment(0xB934, "Load channel flags for this slot", align=Align.INLINE)
d.comment(0xB937, "Save flags in Y", align=Align.INLINE)
d.comment(0xB938, "Test active flag (bit 1)", align=Align.INLINE)
d.comment(0xB93A, "Not active: check station match", align=Align.INLINE)
d.comment(0xB93C, "V clear (close all): next slot", align=Align.INLINE)
d.comment(0xB93E, "C clear: check station match", align=Align.INLINE)
d.comment(0xB940, "Restore original flags", align=Align.INLINE)
d.comment(0xB941, "Clear write-pending flag (bit 5)", align=Align.INLINE)
d.comment(0xB943, "Update channel flags", align=Align.INLINE)
d.comment(0xB946, "Next slot (V always set here)", align=Align.INLINE)
d.label(0xB948, "done_check_station")

d.comment(0xB948, "Check if channel belongs to station", align=Align.INLINE)
d.comment(0xB94B, "No match: skip to next slot", align=Align.INLINE)
d.comment(0xB94D, "A=0: clear channel", align=Align.INLINE)
d.comment(0xB94F, "Clear channel flags (close it)", align=Align.INLINE)
d.comment(0xB952, "Clear network number", align=Align.INLINE)
d.comment(0xB955, "Continue to next slot", align=Align.INLINE)
d.label(0xB957, "match_station_net")

d.subroutine(
    0xB957,
    "match_station_net",
    title="Check FCB slot matches current station/network",
    description="""Compares the station and network numbers in the
FCB at slot X against the current values using
EOR. Returns Z=1 if both match, Z=0 if either
differs.""",
    on_entry={"x": "FCB slot index"},
    on_exit={"z": "1=match, 0=no match"},
)


d.comment(0xB957, "Load FCB station number", align=Align.INLINE)
d.comment(0xB95A, "Compare with current station", align=Align.INLINE)
d.comment(0xB95D, "Different: Z=0, no match", align=Align.INLINE)
d.comment(0xB95F, "Load FCB network number", align=Align.INLINE)
d.comment(0xB962, "Compare with current network", align=Align.INLINE)
d.label(0xB965, "rts_match_stn")

d.comment(0xB965, "Return; Z=1 if match, Z=0 if not", align=Align.INLINE)
d.label(0xB966, "find_open_fcb")

d.subroutine(
    0xB966,
    "find_open_fcb",
    title="Find next open FCB slot for current connection",
    description="""Scans from the current index, wrapping around at
the end. On the first pass finds active entries
matching the station; on the second pass finds
empty slots for new allocations.""",
    on_entry={"x": "starting FCB index (search wraps)"},
    on_exit={
        "x": "FCB slot index of the matched (active) or first empty slot",
        "z flag": "match status (set when an entry was found)",
    },
)


d.comment(0xB966, "Load current FCB index", align=Align.INLINE)
d.comment(0xB969, "Set V flag (first pass marker)", align=Align.INLINE)
d.label(0xB96C, "loop_find_fcb")

d.comment(0xB96C, "Next FCB slot", align=Align.INLINE)
d.comment(0xB96D, "Past end of table (&10)?", align=Align.INLINE)
d.comment(0xB96F, "No: continue checking", align=Align.INLINE)
d.comment(0xB971, "Wrap around to slot 0", align=Align.INLINE)
d.label(0xB973, "skip_if_no_wrap")

d.comment(0xB973, "Back to starting slot?", align=Align.INLINE)
d.comment(0xB976, "No: check this slot", align=Align.INLINE)
d.comment(0xB978, "V clear (second pass): scan empties", align=Align.INLINE)
d.comment(0xB97A, "Clear V for second pass", align=Align.INLINE)
d.comment(0xB97B, "Continue scanning", align=Align.INLINE)
d.label(0xB97D, "done_check_fcb_status")

d.comment(0xB97D, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB980, "Shift bit 7 (in-use) into carry", align=Align.INLINE)
d.comment(0xB981, "Not in use: skip", align=Align.INLINE)
d.comment(0xB983, "Test bit 2 (modified flag)", align=Align.INLINE)
d.comment(0xB985, "Modified: check further conditions", align=Align.INLINE)
d.label(0xB987, "done_select_fcb")

d.comment(0xB987, "Adjust for following INX", align=Align.INLINE)
d.label(0xB988, "loop_scan_empty_fcb")

d.comment(0xB988, "Next FCB slot", align=Align.INLINE)
d.comment(0xB989, "Past end of table?", align=Align.INLINE)
d.comment(0xB98B, "No: continue", align=Align.INLINE)
d.comment(0xB98D, "Wrap around to slot 0", align=Align.INLINE)
d.label(0xB98F, "done_test_empty_slot")

d.comment(0xB98F, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB992, "Shift bit 7 into carry", align=Align.INLINE)
d.comment(0xB993, "Not in use: continue scanning", align=Align.INLINE)
d.comment(0xB995, "Set carry", align=Align.INLINE)
d.comment(0xB996, "Restore original flags", align=Align.INLINE)
d.comment(0xB997, "Save flags back (mark as found)", align=Align.INLINE)
d.comment(0xB99A, "Restore original FCB index", align=Align.INLINE)
d.comment(0xB99D, "Return with found slot in X", align=Align.INLINE)
d.label(0xB99E, "skip_if_modified_fcb")

d.comment(0xB99E, "V set (first pass): skip modified", align=Align.INLINE)
d.comment(0xB9A0, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB9A3, "Test bit 5 (offset pending)", align=Align.INLINE)
d.comment(0xB9A5, "Bit 5 set: skip this slot", align=Align.INLINE)
d.comment(0xB9A7, "Use this slot", align=Align.INLINE)
d.label(0xB9A9, "init_wipe_counters")

d.subroutine(
    0xB9A9,
    "init_wipe_counters",
    title="Initialise byte counters for wipe/transfer",
    description="""Sets `hazel_pass_counter` to 1 and clears
`hazel_byte_counter_lo`, `hazel_offset_counter` and
`hazel_transfer_flag`. Then stores `&FF` sentinels in
[`hazel_sentinel_cd`](label:hazel_sentinel_cd) /
[`hazel_sentinel_ce`](label:hazel_sentinel_ce). The HAZEL FS-state region
is at &C2xx.""",
    on_entry={},
    on_exit={"x": "small loop counter (last DEX value)", "y": "0 (cleared by the TYA path)"},
)


d.comment(0xB9A9, "Initial pass count = 1", align=Align.INLINE)
d.comment(0xB9AB, "Store pass counter", align=Align.INLINE)
d.comment(0xB9AE, "Y=0", align=Align.INLINE)
d.comment(0xB9AF, "Clear byte counter low", align=Align.INLINE)
d.comment(0xB9B2, "Clear offset counter", align=Align.INLINE)
d.comment(0xB9B5, "Clear transfer flag", align=Align.INLINE)
d.comment(0xB9B8, "A=0", align=Align.INLINE)
d.comment(0xB9B9, "Clear 3 counter bytes", align=Align.INLINE)
d.label(0xB9BB, "loop_clear_counters")

d.comment(0xB9BB, "Clear counter byte", align=Align.INLINE)
d.comment(0xB9BE, "Next byte", align=Align.INLINE)
d.comment(0xB9BF, "Loop for indices 2, 1, 0", align=Align.INLINE)
d.comment(0xB9C1, "Store &FF as sentinel in xfer_sentinel_1", align=Align.INLINE)
d.comment(0xB9C4, "Store &FF as sentinel in xfer_sentinel_2", align=Align.INLINE)
d.comment(0xB9C7, "X=&CA: workspace offset", align=Align.INLINE)
d.comment(0xB9C9, "Y=&C2: HAZEL workspace page &C2", align=Align.INLINE)
d.comment(0xB9CB, "Return; X/Y point to &C2CA", align=Align.INLINE)
d.label(0xB9CC, "start_wipe_pass")

d.subroutine(
    0xB9CC,
    "start_wipe_pass",
    title="Start wipe pass for current FCB",
    description="""Verifies the workspace checksum, saves the station
context (pushing station low/high), initialises
transfer counters via init_wipe_counters, and sends
the initial request via send_and_receive. Clears the
active and offset flags on completion.""",
    on_entry={"x": "FCB slot index"},
)


d.comment(0xB9CC, "Verify workspace checksum integrity", align=Align.INLINE)
d.comment(0xB9CF, "Save current FCB index", align=Align.INLINE)
d.comment(0xB9D2, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB9D5, "Shift bit 0 (active) into carry", align=Align.INLINE)
d.comment(0xB9D6, "Not active: clear status and return", align=Align.INLINE)
d.comment(0xB9D8, "Save current station low to stack", align=Align.INLINE)
d.comment(0xB9DB, "Push station low", align=Align.INLINE)
d.comment(0xB9DC, "Save current station high", align=Align.INLINE)
d.comment(0xB9DF, "Push station high", align=Align.INLINE)
d.comment(0xB9E0, "Load FCB station low", align=Align.INLINE)
d.comment(0xB9E3, "Set as working station low", align=Align.INLINE)
d.comment(0xB9E6, "Load FCB station high", align=Align.INLINE)
d.comment(0xB9E9, "Set as working station high", align=Align.INLINE)
d.comment(0xB9EC, "Reset transfer counters", align=Align.INLINE)
d.comment(0xB9EF, "Set offset to &FF (no data yet)", align=Align.INLINE)
d.comment(0xB9F2, "Set pass counter to 0 (flush mode)", align=Align.INLINE)
d.comment(0xB9F5, "Reload FCB index", align=Align.INLINE)
d.comment(0xB9F8, "Transfer to A", align=Align.INLINE)
d.comment(0xB9F9, "Prepare addition", align=Align.INLINE)
d.comment(0xB9FA, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xB9FC, "Store buffer address high byte", align=Align.INLINE)
d.comment(0xB9FF, "Load FCB status flags", align=Align.INLINE)
d.comment(0xBA02, "Test bit 5 (has saved offset)", align=Align.INLINE)
d.comment(0xBA04, "No offset: skip restore", align=Align.INLINE)
d.comment(0xBA06, "Load saved byte offset", align=Align.INLINE)
d.comment(0xBA09, "Restore offset counter", align=Align.INLINE)
d.label(0xBA0C, "done_restore_offset")

d.comment(0xBA0C, "Load FCB attribute reference", align=Align.INLINE)
d.comment(0xBA0F, "Store as current reference", align=Align.INLINE)
d.comment(0xBA12, "Transfer to X", align=Align.INLINE)
d.comment(0xBA13, "Read saved receive attribute", align=Align.INLINE)
d.comment(0xBA16, "Push to stack", align=Align.INLINE)
d.comment(0xBA17, "Restore attribute to A", align=Align.INLINE)
d.comment(0xBA18, "Set attribute in receive buffer", align=Align.INLINE)
d.comment(0xBA1A, "X=&CA: workspace offset", align=Align.INLINE)
d.comment(0xBA1C, "Y=&C2: HAZEL workspace page &C2", align=Align.INLINE)
d.comment(0xBA1E, "A=0: standard transfer mode", align=Align.INLINE)
d.comment(0xBA20, "Send data and receive response", align=Align.INLINE)
d.comment(0xBA23, "Reload FCB index", align=Align.INLINE)
d.comment(0xBA26, "Restore saved receive attribute", align=Align.INLINE)
d.comment(0xBA27, "Restore receive attribute", align=Align.INLINE)
d.comment(0xBA2A, "Restore station high", align=Align.INLINE)
d.comment(0xBA2B, "Store station high", align=Align.INLINE)
d.comment(0xBA2E, "Restore station low", align=Align.INLINE)
d.comment(0xBA2F, "Store station low", align=Align.INLINE)
d.label(0xBA32, "done_clear_fcb_active")

d.comment(0xBA32, "Mask &DC: clear bits 0, 1, 5", align=Align.INLINE)
d.comment(0xBA34, "Clear active and offset flags", align=Align.INLINE)
d.comment(0xBA37, "Update FCB status", align=Align.INLINE)
d.comment(0xBA3A, "Return", align=Align.INLINE)
d.label(0xBA3B, "save_fcb_context")

d.subroutine(
    0xBA3B,
    "save_fcb_context",
    title="Save FCB context and process pending slots",
    description="""Copies 13 bytes from the TX buffer (&0F00) and
fs_load_addr workspace to temporary storage at
&10D9. If Y=0, skips to the restore loop. Otherwise
scans for pending FCB slots (bits 7+6 set), flushes
each via start_wipe_pass, allocates new slots via
find_open_fcb, and sends directory requests. Falls
through to restore_catalog_entry.""",
    on_entry={"y": "filter attribute (0=process all)"},
)


d.comment(0xBA3B, "Copy 13 bytes (indices 0 to &0C)", align=Align.INLINE)
d.label(0xBA3D, "loop_save_tx_context")

d.comment(0xBA3D, "Load TX buffer byte", align=Align.INLINE)
d.comment(0xBA40, "Save to context buffer at &10D9", align=Align.INLINE)
d.comment(0xBA43, "Load workspace byte from fs_load_addr", align=Align.INLINE)
d.comment(0xBA45, "Save to stack", align=Align.INLINE)
d.comment(0xBA46, "Next byte down", align=Align.INLINE)
d.comment(0xBA47, "Loop for all 13 bytes", align=Align.INLINE)
d.comment(0xBA49, "Y=0? (no FCB to process)", align=Align.INLINE)
d.comment(0xBA4B, "Non-zero: scan and process FCBs", align=Align.INLINE)
d.comment(0xBA4D, "Y=0: skip to restore workspace", align=Align.INLINE)
d.label(0xBA50, "done_save_context")

d.comment(0xBA50, "Save flags", align=Align.INLINE)
d.comment(0xBA51, "X=&FF: start scanning from -1", align=Align.INLINE)
d.label(0xBA53, "loop_find_pending_fcb")

d.comment(0xBA53, "Next FCB slot", align=Align.INLINE)
d.comment(0xBA54, "Load FCB status flags", align=Align.INLINE)
d.comment(0xBA57, "Bit 7 clear: not pending, skip", align=Align.INLINE)
d.comment(0xBA59, "Shift bit 6 to bit 7", align=Align.INLINE)
d.comment(0xBA5A, "Bit 6 clear: skip", align=Align.INLINE)
d.comment(0xBA5C, "Flush this FCB's pending data", align=Align.INLINE)
d.comment(0xBA5F, "Pending marker &40", align=Align.INLINE)
d.comment(0xBA61, "Mark FCB as pending-only", align=Align.INLINE)
d.comment(0xBA64, "Save flags", align=Align.INLINE)
d.comment(0xBA65, "Find next available FCB slot", align=Align.INLINE)
d.comment(0xBA68, "Restore flags", align=Align.INLINE)
d.comment(0xBA69, "Load current channel attribute", align=Align.INLINE)
d.comment(0xBA6C, "Store as current reference", align=Align.INLINE)
d.comment(0xBA6F, "Save attribute", align=Align.INLINE)
d.comment(0xBA70, "Prepare attribute-to-channel conversion", align=Align.INLINE)
d.comment(0xBA71, "Convert attribute (&20+) to channel index", align=Align.INLINE)
d.comment(0xBA73, "Y = attribute index", align=Align.INLINE)
d.comment(0xBA74, "Load station for this attribute", align=Align.INLINE)
d.comment(0xBA77, "Store station in TX buffer", align=Align.INLINE)
d.comment(0xBA7A, "Restore attribute", align=Align.INLINE)
d.comment(0xBA7B, "Store attribute in FCB slot", align=Align.INLINE)
d.comment(0xBA7E, "Load working station low", align=Align.INLINE)
d.comment(0xBA81, "Store in TX buffer", align=Align.INLINE)
d.comment(0xBA84, "Load working station high", align=Align.INLINE)
d.comment(0xBA87, "Store in TX buffer", align=Align.INLINE)
d.comment(0xBA8A, "Get FCB slot index", align=Align.INLINE)
d.comment(0xBA8B, "Prepare addition", align=Align.INLINE)
d.comment(0xBA8C, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xBA8E, "Store buffer address high byte", align=Align.INLINE)
d.comment(0xBA91, "Restore flags", align=Align.INLINE)
d.comment(0xBA92, "V clear: skip directory request", align=Align.INLINE)
d.comment(0xBA94, "Command byte = 0", align=Align.INLINE)
d.label(0xBA97, "done_init_wipe")

d.comment(0xBA97, "Reset transfer counters", align=Align.INLINE)
d.comment(0xBA9A, "Read saved receive attribute", align=Align.INLINE)
d.comment(0xBA9D, "Function code &0D", align=Align.INLINE)
d.comment(0xBA9E, "Load current reference", align=Align.INLINE)
d.comment(0xBAA1, "Set in receive buffer", align=Align.INLINE)
d.comment(0xBAA3, "Y=&C2: HAZEL workspace page &C2", align=Align.INLINE)
d.comment(0xBAA5, "A=2: transfer mode 2", align=Align.INLINE)
d.comment(0xBAA7, "Send and receive data", align=Align.INLINE)
d.comment(0xBAAA, "Restore receive attribute", align=Align.INLINE)
d.comment(0xBAAB, "Restore receive attribute", align=Align.INLINE)
d.comment(0xBAAE, "Reload FCB index", align=Align.INLINE)
d.comment(0xBAB1, "Load pass counter", align=Align.INLINE)
d.comment(0xBAB4, "Non-zero: data received, calc offset", align=Align.INLINE)
d.comment(0xBAB6, "Load offset counter", align=Align.INLINE)
d.comment(0xBAB9, "Zero: no data received at all", align=Align.INLINE)
d.label(0xBABB, "done_calc_offset")

d.comment(0xBABB, "Load offset counter", align=Align.INLINE)
d.comment(0xBABE, "Negate (ones complement)", align=Align.INLINE)
d.comment(0xBAC0, "Clear carry for add", align=Align.INLINE)
d.comment(0xBAC1, "Complete twos complement negation", align=Align.INLINE)
d.comment(0xBAC3, "Store negated offset in FCB", align=Align.INLINE)
d.comment(0xBAC6, "Set bit 5 (has saved offset)", align=Align.INLINE)
d.comment(0xBAC8, "Add to FCB flags", align=Align.INLINE)
d.comment(0xBACB, "Update FCB status", align=Align.INLINE)
d.comment(0xBACE, "Load buffer address high byte", align=Align.INLINE)
d.comment(0xBAD1, "Set pointer high byte", align=Align.INLINE)
d.comment(0xBAD3, "A=0: pointer low byte and clear val", align=Align.INLINE)
d.comment(0xBAD5, "Set pointer low byte", align=Align.INLINE)
d.comment(0xBAD7, "Load negated offset (start of clear)", align=Align.INLINE)
d.label(0xBADA, "loop_clear_buffer")

d.comment(0xBADA, "Clear buffer byte", align=Align.INLINE)
d.comment(0xBADC, "Next byte", align=Align.INLINE)
d.comment(0xBADD, "Loop until page boundary", align=Align.INLINE)
d.label(0xBADF, "done_set_fcb_active")

d.comment(0xBADF, "Set bit 1 (active flag)", align=Align.INLINE)
d.comment(0xBAE1, "Add active flag to status", align=Align.INLINE)
d.comment(0xBAE4, "Update FCB status", align=Align.INLINE)
d.comment(0xBAE7, "Y=0: start restoring workspace", align=Align.INLINE)
d.label(0xBAE9, "loop_restore_workspace")

d.subroutine(
    0xBAE9,
    "loop_restore_workspace",
    title="Pop 13 saved workspace bytes back to fs_load_addr+",
    description="""Y=0..&0C loop: PLA / STA fs_load_addr,Y / INY / CPY #&0D / BNE.
Restores the 13-byte FS-options block that save_fcb_context pushed
on the stack, undoing the protection the wipe/scan path put in
place. Two callers: the JMP at &BA4B (close-and-restore exit) and
the BNE retry at &BABE.""",
)


d.comment(0xBAE9, "Restore workspace byte from stack", align=Align.INLINE)
d.comment(0xBAEA, "Store to fs_load_addr workspace", align=Align.INLINE)
d.comment(0xBAED, "Next byte", align=Align.INLINE)
d.comment(0xBAEE, "Restored all 13 bytes?", align=Align.INLINE)
d.comment(0xBAF0, "No: continue restoring", align=Align.INLINE)
d.label(0xBAF2, "restore_catalog_entry")

d.subroutine(
    0xBAF2,
    "restore_catalog_entry",
    title="Restore saved catalog entry to TX buffer",
    description="""Copies 13 bytes (Y=&0C..0) from
[`hazel_ctx_buffer`](label:hazel_ctx_buffer) back to the TX buffer
starting at [`hazel_txcb_port`](label:hazel_txcb_port). Falls through to
`find_matching_fcb`.""",
)


d.comment(0xBAF2, "Copy 13 bytes (indices 0 to &0C)", align=Align.INLINE)
d.label(0xBAF4, "loop_restore_tx_buf")

d.comment(0xBAF4, "Load saved catalog byte from &10D9", align=Align.INLINE)
d.comment(0xBAF7, "Restore to TX buffer", align=Align.INLINE)
d.comment(0xBAFA, "Next byte down", align=Align.INLINE)
d.comment(0xBAFB, "Loop for all bytes", align=Align.INLINE)
d.comment(0xBAFD, "Return", align=Align.INLINE)
d.label(0xBAFE, "loop_save_before_match")

d.subroutine(
    0xBAFE,
    "loop_save_before_match",
    title="Save FCB context, fall into find_matching_fcb",
    description="""Single-instruction wrapper at the top of the per-iteration FCB
search retry: JSR save_fcb_context to preserve the current attempt's
state (offset, station, network), then fall through into
find_matching_fcb. Single caller (the BNE retry at &BAED). Used
once the first scan past slot &0F has failed and the search needs
to restart from slot 0 with the saved context restored.""",
)


d.comment(0xBAFE, "Save current context first", align=Align.INLINE)
d.label(0xBB01, "find_matching_fcb")

d.subroutine(
    0xBB01,
    "find_matching_fcb",
    title="Find FCB slot matching channel attribute",
    description="""Scans FCB slots 0-&0F for an active entry whose
attribute reference matches hazel_chan_attr. Converts the
attribute to a channel index, then verifies the
station and network numbers. On the first scan
past slot &0F, saves context via save_fcb_context
and restarts. Returns Z=0 if the FCB has saved
offset data (bit 5 set).""",
    on_exit={"x": "matching FCB index", "z": "0=has offset data, 1=no offset"},
)


d.comment(0xBB01, "X=&FF: start scanning from -1", align=Align.INLINE)
d.label(0xBB03, "loop_reload_attr")

d.comment(0xBB03, "Load channel attribute to match", align=Align.INLINE)
d.label(0xBB06, "loop_next_fcb_slot")

d.comment(0xBB06, "Next FCB slot", align=Align.INLINE)
d.comment(0xBB07, "Past end of table (&10)?", align=Align.INLINE)
d.comment(0xBB09, "No: check this slot", align=Align.INLINE)
d.comment(0xBB0B, "Load channel attribute", align=Align.INLINE)
d.comment(0xBB0E, "Convert to channel index", align=Align.INLINE)
d.comment(0xBB11, "Load station for this channel", align=Align.INLINE)
d.comment(0xBB14, "Store as match target station high", align=Align.INLINE)
d.comment(0xBB17, "Load port for this channel", align=Align.INLINE)
d.comment(0xBB1A, "Store as match target station low", align=Align.INLINE)
d.comment(0xBB1D, "Save context and rescan from start", align=Align.INLINE)
d.label(0xBB20, "done_test_fcb_active")

d.comment(0xBB20, "Load FCB status flags", align=Align.INLINE)
d.comment(0xBB23, "Test active flag (bit 1)", align=Align.INLINE)
d.comment(0xBB25, "Not active: skip to next", align=Align.INLINE)
d.comment(0xBB27, "Get attribute to match", align=Align.INLINE)
d.comment(0xBB28, "Compare with FCB attribute ref", align=Align.INLINE)
d.comment(0xBB2B, "No attribute match: skip", align=Align.INLINE)
d.comment(0xBB2D, "Save matching FCB index", align=Align.INLINE)
d.comment(0xBB30, "Save flags from attribute compare", align=Align.INLINE)
d.comment(0xBB31, "Prepare subtraction", align=Align.INLINE)
d.comment(0xBB32, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0xBB34, "Restore flags from attribute compare", align=Align.INLINE)
d.comment(0xBB35, "Y = channel index", align=Align.INLINE)
d.comment(0xBB36, "Reload FCB index", align=Align.INLINE)
d.comment(0xBB39, "Load channel station byte", align=Align.INLINE)
d.comment(0xBB3C, "Compare with FCB station", align=Align.INLINE)
d.comment(0xBB3F, "Station mismatch: try next", align=Align.INLINE)
d.comment(0xBB41, "Load channel network byte", align=Align.INLINE)
d.comment(0xBB44, "Compare with FCB network", align=Align.INLINE)
d.comment(0xBB47, "Network mismatch: try next", align=Align.INLINE)
d.comment(0xBB49, "Load FCB flags", align=Align.INLINE)
d.comment(0xBB4C, "Bit 7 clear: no pending flush", align=Align.INLINE)
d.comment(0xBB4E, "Clear pending flag (bit 7)", align=Align.INLINE)
d.comment(0xBB50, "Update FCB status", align=Align.INLINE)
d.comment(0xBB53, "Find new open FCB slot", align=Align.INLINE)
d.comment(0xBB56, "Reload FCB flags", align=Align.INLINE)
d.label(0xBB59, "return_test_offset")

d.comment(0xBB59, "Test bit 5 (has offset data)", align=Align.INLINE)
d.comment(0xBB5B, "Return; Z=1 no offset, Z=0 has data", align=Align.INLINE)
d.label(0xBB5C, "inc_fcb_byte_count")

d.subroutine(
    0xBB5C,
    "inc_fcb_byte_count",
    title="Increment 3-byte FCB transfer count",
    description="""Increments hazel_fcb_addr_lo+X (low), cascading overflow to
hazel_fcb_addr_mid+X (mid) and hazel_fcb_addr_hi+X (high).""",
    on_entry={"x": "FCB slot index"},
)


d.comment(0xBB5C, "Increment byte count low", align=Align.INLINE)
d.comment(0xBB5F, "No overflow: done", align=Align.INLINE)
d.comment(0xBB61, "Increment byte count mid", align=Align.INLINE)
d.comment(0xBB64, "No overflow: done", align=Align.INLINE)
d.comment(0xBB66, "Increment byte count high", align=Align.INLINE)
d.label(0xBB69, "rts_inc_fcb_count")

d.comment(0xBB69, "Return", align=Align.INLINE)
d.subroutine(
    0xBB6A,
    "process_all_fcbs",
    title="Process all active FCB slots",
    description="""Saves 9 zero-page bytes (`&00B4`–`&00BC`, i.e. `fs_work_4`+0..+8)
on the stack via a `PHX`/`PHY`/loop preamble using the `&FFBD,X`
indexing-wrap trick (X = `&F7`..`&FF` wraps to `&00B4`..`&00BC`),
then scans FCB slots `&0F` down to 0.
Calls [`start_wipe_pass`](label:start_wipe_pass) for each active entry
matching the filter attribute in `Y` (`0` = match all). Restores
all saved context on completion. Also contains the OSBGET/OSBPUT
inline logic for reading and writing bytes through file
channels.""",
    on_entry={"y": "filter attribute (0=process all)"},
)


d.comment(0xBB6A, "Save X on entry", align=Align.INLINE)
d.comment(0xBB6B, "Save Y across the body", align=Align.INLINE)
d.comment(0xBB6C, "X=&F7: save 9 workspace bytes (&F7..&FF)", align=Align.INLINE)
d.label(0xBB6E, "loop_save_fcb_workspace")

d.comment(0xBB6E, "Load workspace byte", align=Align.INLINE)
d.comment(0xBB71, "Push fs_options", align=Align.INLINE)
d.comment(0xBB72, "Next byte", align=Align.INLINE)
d.comment(0xBB73, "X<0: more bytes to save", align=Align.INLINE)
d.comment(0xBB75, "Start from FCB slot &0F", align=Align.INLINE)
d.comment(0xBB77, "Store as current FCB index", align=Align.INLINE)
d.label(0xBB7A, "loop_process_fcb")

d.comment(0xBB7A, "Load current FCB index", align=Align.INLINE)
d.comment(0xBB7D, "Get filter attribute", align=Align.INLINE)
d.comment(0xBB7E, "Zero: process all FCBs", align=Align.INLINE)
d.comment(0xBB80, "Compare with FCB attribute ref", align=Align.INLINE)
d.comment(0xBB83, "No match: skip this FCB", align=Align.INLINE)
d.label(0xBB85, "done_flush_fcb")

d.comment(0xBB85, "Save filter attribute", align=Align.INLINE)
d.comment(0xBB86, "Flush pending data for this FCB", align=Align.INLINE)
d.label(0xBB8A, "done_advance_fcb")

d.comment(0xBB8A, "Previous FCB index", align=Align.INLINE)
d.comment(0xBB8D, "More slots: continue loop", align=Align.INLINE)
d.comment(0xBB8F, "X=8: restore 9 workspace bytes", align=Align.INLINE)
d.label(0xBB91, "loop_restore_fcb_ws")

d.comment(0xBB91, "Restore fs_block_offset", align=Align.INLINE)
d.comment(0xBB92, "Restore workspace byte", align=Align.INLINE)
d.comment(0xBB94, "Next byte down", align=Align.INLINE)
d.comment(0xBB95, "More bytes: continue restoring", align=Align.INLINE)
d.comment(0xBB99, "Return", align=Align.INLINE)
d.subroutine(
    0xBB9A,
    "bgetv_handler",
    title="BGETV vector handler: read byte from open file",
    description="""Reached via the BGETV vector at `&0216`, which the
[`fs_vector_table`](label:fs_vector_table) entries copy into the MOS extended
vector area. Saves caller's `Y` in `hazel_chan_attr` (channel attribute slot),
pushes `X`, calls
[`store_result_check_dir`](label:store_result_check_dir) to validate the channel,
then either reads a byte from the FCB buffer (returning it in `A`
with `C=0`) or signals end-of-file (`C=1`).""",
    on_entry={"y": "channel handle"},
    on_exit={"a": "byte read (when C=0)", "c": "0 = byte returned, 1 = EOF / error"},
)


d.entry(0xBB9A)
d.comment(0xBB9A, "Save channel attribute", align=Align.INLINE)
d.comment(0xBB9D, "Save caller's X", align=Align.INLINE)
d.comment(0xBB9E, "Push X", align=Align.INLINE)
d.comment(0xBB9F, "Store result and check not directory", align=Align.INLINE)
d.comment(0xBBA2, "Load channel flags", align=Align.INLINE)
d.comment(0xBBA5, "Test write-only flag (bit 5)", align=Align.INLINE)
d.comment(0xBBA7, "Not write-only: proceed with read", align=Align.INLINE)
d.comment(0xBBA9, "Error code &D4", align=Align.INLINE)
d.comment(0xBBAB, "Generate 'Write only' error", align=Align.INLINE)
d.label(0xBBB9, "done_read_fcb_byte")

d.comment(0xBBB9, "Clear V (first-pass matching)", align=Align.INLINE)
d.comment(0xBBBA, "Find FCB matching this channel", align=Align.INLINE)
d.comment(0xBBBD, "No offset: read byte from buffer", align=Align.INLINE)
d.comment(0xBBBF, "Load byte count for matching FCB", align=Align.INLINE)
d.comment(0xBBC2, "Compare with buffer offset limit", align=Align.INLINE)
d.comment(0xBBC5, "Below offset: data available", align=Align.INLINE)
d.comment(0xBBC7, "Load channel flags for FCB", align=Align.INLINE)
d.comment(0xBBCA, "Transfer to X for testing", align=Align.INLINE)
d.comment(0xBBCB, "Test bit 6 (EOF already signalled)", align=Align.INLINE)
d.comment(0xBBCD, "EOF already set: raise error", align=Align.INLINE)
d.comment(0xBBCF, "Restore flags", align=Align.INLINE)
d.comment(0xBBD0, "Set EOF flag (bit 6)", align=Align.INLINE)
d.comment(0xBBD2, "Update channel flags with EOF", align=Align.INLINE)
d.comment(0xBBD5, "A=0: clear receive attribute", align=Align.INLINE)
d.comment(0xBBD7, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0xBBDA, "Restore caller's X", align=Align.INLINE)
d.comment(0xBBDB, "X restored", align=Align.INLINE)
d.comment(0xBBDC, "A=&FE: EOF marker byte", align=Align.INLINE)
d.comment(0xBBDE, "Restore channel attribute", align=Align.INLINE)
d.comment(0xBBE1, "C=1: end of file", align=Align.INLINE)
d.comment(0xBBE2, "Return", align=Align.INLINE)
d.label(0xBBE3, "error_end_of_file")

d.comment(0xBBE3, "Error code &DF", align=Align.INLINE)
d.comment(0xBBE5, "Generate 'End of file' error", align=Align.INLINE)
d.label(0xBBF4, "done_load_from_buf")

d.comment(0xBBF4, "Load current byte count (= offset)", align=Align.INLINE)
d.comment(0xBBF7, "Save byte count", align=Align.INLINE)
d.comment(0xBBF8, "Get FCB slot index", align=Align.INLINE)
d.comment(0xBBF9, "X = FCB slot for byte count inc", align=Align.INLINE)
d.comment(0xBBFA, "A=0: clear receive attribute", align=Align.INLINE)
d.comment(0xBBFC, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0xBBFF, "Increment byte count for this FCB", align=Align.INLINE)
d.comment(0xBC02, "Restore byte count (= buffer offset)", align=Align.INLINE)
d.comment(0xBC03, "Y = offset into data buffer", align=Align.INLINE)
d.comment(0xBC04, "Load current FCB index", align=Align.INLINE)
d.comment(0xBC07, "Prepare addition", align=Align.INLINE)
d.comment(0xBC08, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xBC0A, "Set pointer high byte", align=Align.INLINE)
d.comment(0xBC0C, "A=0: pointer low byte", align=Align.INLINE)
d.comment(0xBC0E, "Set pointer low byte", align=Align.INLINE)
d.comment(0xBC10, "Restore caller's X", align=Align.INLINE)
d.comment(0xBC11, "X restored", align=Align.INLINE)
d.comment(0xBC12, "Read data byte from buffer", align=Align.INLINE)
d.comment(0xBC14, "Restore channel attribute", align=Align.INLINE)
d.comment(0xBC17, "C=0: byte read successfully", align=Align.INLINE)
d.comment(0xBC18, "Return; A = data byte", align=Align.INLINE)
d.subroutine(
    0xBC19,
    "bputv_handler",
    title="BPUTV vector handler: write byte to open file",
    description="""Reached via the BPUTV vector at `&0218`. Saves caller's `Y` in
`hazel_chan_attr`, pushes the data byte and `X`, then routes to the FCB
buffer-write path: stores the byte in the channel's transmit
buffer, increments the byte count via
[`inc_fcb_byte_count`](label:inc_fcb_byte_count), and exits via
[`done_inc_byte_count`](label:done_inc_byte_count).""",
    on_entry={"a": "byte to write", "y": "channel handle"},
    on_exit={"c": "0 = written, 1 = error"},
)


d.entry(0xBC19)


d.comment(0xBC19, "Save channel attribute", align=Align.INLINE)
d.comment(0xBC1C, "Save data byte", align=Align.INLINE)
d.comment(0xBC1D, "Y = data byte", align=Align.INLINE)
d.comment(0xBC1E, "Save caller's X", align=Align.INLINE)
d.comment(0xBC1F, "Push X", align=Align.INLINE)
d.comment(0xBC20, "Restore data byte to A", align=Align.INLINE)
d.comment(0xBC21, "Push data byte for later", align=Align.INLINE)
d.comment(0xBC22, "Save data byte in workspace", align=Align.INLINE)
d.comment(0xBC25, "Store result and check not directory", align=Align.INLINE)
d.comment(0xBC28, "Load channel flags", align=Align.INLINE)
d.comment(0xBC2B, "Bit 7 set: channel open, proceed", align=Align.INLINE)
d.comment(0xBC2D, "Error &C1: Not open for update", align=Align.INLINE)
d.comment(0xBC2F, "Raise error with inline string", align=Align.INLINE)
d.label(0xBC46, "done_test_write_flag")

d.comment(0xBC46, "Test write flag (bit 5)", align=Align.INLINE)
d.comment(0xBC48, "Not write-capable: use buffer path", align=Align.INLINE)
d.comment(0xBC4A, "Load reply port for this channel", align=Align.INLINE)
d.comment(0xBC4D, "Restore data byte", align=Align.INLINE)
d.comment(0xBC4E, "Send byte directly to server", align=Align.INLINE)
d.comment(0xBC51, "Update byte count and return", align=Align.INLINE)
d.label(0xBC54, "done_find_write_fcb")

d.comment(0xBC54, "Set V flag (alternate match mode)", align=Align.INLINE)
d.comment(0xBC57, "Find matching FCB for channel", align=Align.INLINE)
d.comment(0xBC5A, "Load byte count for FCB", align=Align.INLINE)
d.comment(0xBC5D, "Buffer full (&FF bytes)?", align=Align.INLINE)
d.comment(0xBC5F, "No: store byte in buffer", align=Align.INLINE)
d.comment(0xBC61, "Save X", align=Align.INLINE)
d.label(0xBC64, "done_check_buf_offset")

d.comment(0xBC64, "Push Y", align=Align.INLINE)
d.comment(0xBC67, "Below offset: skip offset update", align=Align.INLINE)
d.comment(0xBC69, "Carry set from BCS/BCC above", align=Align.INLINE)
d.comment(0xBC6B, "Update buffer offset in FCB", align=Align.INLINE)
d.comment(0xBC6E, "Non-zero: keep offset flag", align=Align.INLINE)
d.comment(0xBC70, "Mask &DF: clear bit 5", align=Align.INLINE)
d.comment(0xBC72, "Clear offset flag", align=Align.INLINE)
d.comment(0xBC75, "Update FCB status", align=Align.INLINE)
d.label(0xBC78, "done_set_dirty_flag")

d.comment(0xBC78, "Set bit 0 (dirty/active)", align=Align.INLINE)
d.comment(0xBC7A, "Add to FCB flags", align=Align.INLINE)
d.comment(0xBC7D, "Update FCB status", align=Align.INLINE)
d.comment(0xBC80, "Load byte count (= write position)", align=Align.INLINE)
d.comment(0xBC83, "Save count", align=Align.INLINE)
d.comment(0xBC84, "Get FCB slot index", align=Align.INLINE)
d.comment(0xBC85, "X = FCB slot", align=Align.INLINE)
d.comment(0xBC86, "Restore byte count", align=Align.INLINE)
d.comment(0xBC87, "Y = buffer write offset", align=Align.INLINE)
d.comment(0xBC88, "Load current FCB index", align=Align.INLINE)
d.comment(0xBC8B, "Prepare addition", align=Align.INLINE)
d.comment(0xBC8C, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xBC8E, "Set pointer high byte", align=Align.INLINE)
d.comment(0xBC90, "A=0: pointer low byte", align=Align.INLINE)
d.comment(0xBC92, "Set pointer low byte", align=Align.INLINE)
d.comment(0xBC94, "Restore data byte", align=Align.INLINE)
d.comment(0xBC95, "Write data byte to buffer", align=Align.INLINE)
d.label(0xBC97, "done_inc_byte_count")

d.subroutine(
    0xBC97,
    "done_inc_byte_count",
    title="Increment FCB byte count, clear rx attr, restore caller",
    description="""JSRs inc_fcb_byte_count for the active FCB, then A=0 / JSR
store_rx_attribute (clears the receive-attribute byte). Pulls
saved X back into X (caller's value), discards the saved data byte
on the stack and returns. Single caller (the OSBPUT/PRINT path at
&BC1F).""",
)


d.comment(0xBC97, "Increment byte count for this FCB", align=Align.INLINE)
d.comment(0xBC9A, "A=0: clear receive attribute", align=Align.INLINE)
d.comment(0xBC9C, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0xBC9F, "Restore caller's X", align=Align.INLINE)
d.comment(0xBCA0, "X restored", align=Align.INLINE)
d.comment(0xBCA1, "Discard saved data byte", align=Align.INLINE)
d.comment(0xBCA2, "Restore channel attribute", align=Align.INLINE)
d.comment(0xBCA5, "Return", align=Align.INLINE)
d.subroutine(
    0xBCA6,
    "flush_fcb_if_stn_known",
    title="Flush FCB byte count to server if station is set",
    description="""Saves all registers, checks if the FCB has a
known station. If yes, sends the accumulated byte
count as a flush request to the file server. If no
station is set, falls through to flush_fcb_with_init
which saves FCB context first.""",
    on_entry={"Y": "channel index (FCB slot)"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"},
)


d.comment(0xBCA6, "Save A", align=Align.INLINE)
d.comment(0xBCA7, "Save X", align=Align.INLINE)
d.comment(0xBCA9, "Read FCB slot attribute byte", align=Align.INLINE)
d.comment(0xBCAC, "Non-zero: station known -> store_station_and_flush", align=Align.INLINE)
d.subroutine(
    0xBCAE,
    "flush_fcb_with_init",
    title="Save FCB context and flush byte count to server",
    description="""Saves all registers and the current FCB context,
copies the FCB byte count into the TX command buffer,
and sends a flush/close request to the file server.
Restores the catalog entry and all registers on return.""",
    on_entry={"Y": "channel index (FCB slot)"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"},
)

d.comment(0xBCAE, "Save attribute byte (saved-station-test path)", align=Align.INLINE)
d.comment(0xBCAF, "Save X again", align=Align.INLINE)
d.comment(0xBCB0, "Save Y", align=Align.INLINE)
d.comment(0xBCB1, "Load station for this channel", align=Align.INLINE)
d.comment(0xBCB4, "Save station on stack", align=Align.INLINE)
d.comment(0xBCB5, "Y=0: reset index", align=Align.INLINE)
d.comment(0xBCB7, "Save current FCB context", align=Align.INLINE)
d.comment(0xBCBA, "Restore station from stack", align=Align.INLINE)
d.label(0xBCBB, "store_station_and_flush")


d.comment(0xBCBB, "Store station in command buffer", align=Align.INLINE)
d.comment(0xBCBF, "Save Y again for the next iteration", align=Align.INLINE)
d.comment(0xBCC0, "Save station for later restore", align=Align.INLINE)
d.comment(0xBCC1, "X=0", align=Align.INLINE)
d.comment(0xBCC3, "Clear function code", align=Align.INLINE)
d.comment(0xBCC6, "Load byte count lo from FCB", align=Align.INLINE)
d.comment(0xBCC9, "Store as data byte count", align=Align.INLINE)
d.comment(0xBCCC, "Load byte count mid from FCB", align=Align.INLINE)
d.comment(0xBCCF, "Store as reply command byte", align=Align.INLINE)
d.comment(0xBCD2, "Load byte count hi from FCB", align=Align.INLINE)
d.comment(0xBCD5, "Store as load vector field", align=Align.INLINE)
d.comment(0xBCD8, "Y=&0D: TX command byte offset", align=Align.INLINE)
d.comment(0xBCDA, "X=5: send 5 bytes", align=Align.INLINE)
d.comment(0xBCDC, "Send flush request to server", align=Align.INLINE)
d.comment(0xBCDF, "Restore station from stack", align=Align.INLINE)
d.comment(0xBCE0, "Y=station for wipe request", align=Align.INLINE)
d.comment(0xBCE1, "Load saved data byte", align=Align.INLINE)
d.comment(0xBCE4, "Send close/wipe request to server", align=Align.INLINE)
d.comment(0xBCE7, "Restore catalog state after flush", align=Align.INLINE)
d.comment(0xBCEC, "Restore A", align=Align.INLINE)
d.comment(0xBCED, "Return", align=Align.INLINE)
d.label(0xBCEE, "send_wipe_request")

d.subroutine(
    0xBCEE,
    "send_wipe_request",
    title="Send wipe/close request packet",
    description="""Sets up the TX control block with function code
&90, the reply port from Y, and the data byte from
A. Sends via send_disconnect_reply, then checks the
error code — raises the server error if non-zero.""",
    on_entry={"a": "data byte to send", "y": "reply port"},
)


d.comment(0xBCEE, "Store reply port", align=Align.INLINE)
d.comment(0xBCF1, "Store data byte", align=Align.INLINE)
d.comment(0xBCF4, "Save Y", align=Align.INLINE)
d.comment(0xBCF5, "Push Y to stack", align=Align.INLINE)
d.comment(0xBCF6, "Save X", align=Align.INLINE)
d.comment(0xBCF7, "Push X to stack", align=Align.INLINE)
d.comment(0xBCF8, "Function code &90", align=Align.INLINE)
d.comment(0xBCFA, "Store in send buffer", align=Align.INLINE)
d.comment(0xBCFD, "Initialise TX control block", align=Align.INLINE)
d.comment(0xBD00, "TX start address low = &DC", align=Align.INLINE)
d.comment(0xBD02, "Set TX start in control block", align=Align.INLINE)
d.comment(0xBD04, "TX end address low = &E0", align=Align.INLINE)
d.comment(0xBD06, "Set TX end in control block", align=Align.INLINE)
d.comment(0xBD08, "Expected reply port = 9", align=Align.INLINE)
d.comment(0xBD0A, "Store reply port in buffer", align=Align.INLINE)
d.comment(0xBD0D, "TX control = &C0", align=Align.INLINE)
d.comment(0xBD0F, "Y=0: no timeout", align=Align.INLINE)
d.comment(0xBD11, "Load reply port for addressing", align=Align.INLINE)
d.comment(0xBD14, "Send packet to server", align=Align.INLINE)
d.comment(0xBD17, "Load reply status", align=Align.INLINE)
d.comment(0xBD1A, "Zero: success", align=Align.INLINE)
d.comment(0xBD1C, "Store error code", align=Align.INLINE)
d.comment(0xBD1F, "X=0: copy index", align=Align.INLINE)
d.label(0xBD21, "loop_copy_wipe_err_msg")

d.comment(0xBD21, "Load error message byte", align=Align.INLINE)
d.comment(0xBD24, "Copy to error block", align=Align.INLINE)
d.comment(0xBD27, "Is it CR (end of message)?", align=Align.INLINE)
d.comment(0xBD29, "Yes: terminate string", align=Align.INLINE)
d.comment(0xBD2B, "Next byte", align=Align.INLINE)
d.comment(0xBD2C, "Continue copying error message", align=Align.INLINE)
d.label(0xBD2E, "done_terminate_wipe_err")

d.comment(0xBD2E, "NUL terminator", align=Align.INLINE)
d.comment(0xBD30, "Terminate error string in block", align=Align.INLINE)
d.comment(0xBD33, "Back up position for error check", align=Align.INLINE)
d.comment(0xBD34, "Process and raise network error", align=Align.INLINE)
d.label(0xBD37, "done_toggle_station")

d.comment(0xBD37, "Load channel attribute index", align=Align.INLINE)
d.comment(0xBD3A, "Load station number for channel", align=Align.INLINE)
d.comment(0xBD3D, "Toggle bit 0 (alternate station)", align=Align.INLINE)
d.comment(0xBD3F, "Update station number", align=Align.INLINE)
d.comment(0xBD42, "Restore X", align=Align.INLINE)
d.comment(0xBD43, "X restored", align=Align.INLINE)
d.comment(0xBD44, "Restore Y", align=Align.INLINE)
d.comment(0xBD45, "Y restored", align=Align.INLINE)
d.comment(0xBD46, "Return", align=Align.INLINE)
d.label(0xBD47, "send_and_receive")

d.subroutine(
    0xBD47,
    "send_and_receive",
    title="Set up FS options and transfer workspace",
    description="""Calls set_options_ptr to configure the FS options
pointer, then jumps to setup_transfer_workspace to
initialise the transfer and send the request.""",
    on_entry={"a": "transfer mode", "x": "workspace offset low", "y": "workspace page"},
)


d.comment(0xBD47, "Set up FS options pointer", align=Align.INLINE)
d.comment(0xBD4A, "Set up transfer workspace and return", align=Align.INLINE)
d.subroutine(
    0xBD4D,
    "read_rx_attribute",
    title="Read receive attribute byte from RX buffer",
    description="""Reads byte at offset &0A in the network receive
control block, used to track which channel owns the
current receive buffer.""",
    on_entry={},
    on_exit={"A": "receive attribute byte", "Y": "&0A"},
)


d.comment(0xBD4D, "Y=&0A: receive attribute offset", align=Align.INLINE)
d.comment(0xBD4F, "Read byte from receive buffer", align=Align.INLINE)
d.comment(0xBD51, "Return", align=Align.INLINE)
d.subroutine(
    0xBD52,
    "store_rx_attribute",
    title="Store receive attribute byte to RX buffer",
    description="""Writes A to offset &0A in the network receive
control block, marking which channel owns the
current receive buffer.""",
    on_entry={"A": "attribute byte to store"},
    on_exit={"Y": "&0A"},
)


d.comment(0xBD52, "Y=&0A: receive attribute offset", align=Align.INLINE)
d.comment(0xBD54, "Store byte to receive buffer", align=Align.INLINE)
d.comment(0xBD56, "Return", align=Align.INLINE)
d.label(0xBD57, "abort_if_escape")

d.subroutine(
    0xBD57,
    "abort_if_escape",
    title="Test escape flag and abort if pressed",
    description="""Checks the escape flag byte; returns immediately
if bit 7 is clear. If escape has been pressed,
falls through to the escape abort handler which
acknowledges the escape via OSBYTE &7E.""",
)


d.comment(0xBD57, "Test bit 7 of escape flag", align=Align.INLINE)
d.comment(0xBD59, "Escape pressed: handle abort", align=Align.INLINE)
d.comment(0xBD5B, "No escape: return", align=Align.INLINE)
d.label(0xBD5C, "error_escape_pressed")

d.comment(0xBD5C, "Close the open file", align=Align.INLINE)
d.label(0xBD5F, "escape_error_close")

d.comment(0xBD62, "Acknowledge escape condition", align=Align.INLINE)
d.comment(0xBD67, "Error number &11", align=Align.INLINE)
d.comment(0xBD69, "Generate 'Escape' BRK error", align=Align.INLINE)
d.comment(0xBD73, "Open the file (handle stored in ws_page)", align=Align.INLINE)
d.entry(0xBD73)

d.label(0xBD73, "cmd_dump")

d.subroutine(
    0xBD73,
    "cmd_dump",
    title="*Dump command handler",
    description="""Opens the file via open_file_for_read, allocates a
21-byte buffer on the stack, and parses the address
range via init_dump_buffer. Loops reading 16 bytes
per line, printing each as a 4-byte hex address,
16 hex bytes with spaces, and a 16-character ASCII
column (non-printable chars shown as '.'). Prints
a column header at every 256-byte boundary.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xBD76, "X=&14: 21-byte stack buffer for dump line state", align=Align.INLINE)
d.comment(0xBD78, "A=0: zero-fill", align=Align.INLINE)
d.label(0xBD7A, "loop_push_zero_buf")

d.comment(0xBD7A, "Push zero", align=Align.INLINE)
d.comment(0xBD7B, "Step counter", align=Align.INLINE)
d.comment(0xBD7C, "Loop while X >= 0 (21 zeros)", align=Align.INLINE)
d.comment(0xBD7E, "Capture stack pointer for later restore", align=Align.INLINE)
d.comment(0xBD7F, "Parse address range and validate against file extent", align=Align.INLINE)
d.comment(0xBD82, "Read low nibble of starting address", align=Align.INLINE)
d.comment(0xBD84, "Mask high nibble (top 4 bits)", align=Align.INLINE)
d.comment(0xBD86, "Aligned (high nibble zero): skip the header print", align=Align.INLINE)
d.comment(0xBD88, "Print 'Address: 00 01 ... 0F: ASCII data' header", align=Align.INLINE)
d.label(0xBD8B, "loop_dump_line")

d.subroutine(
    0xBD8B,
    "loop_dump_line",
    title="*DUMP per-line read loop",
    description="""Body of cmd_dump's outer line loop. Calls abort_if_escape, then
reads up to 16 bytes from the open file via OSBGET into the line
buffer at (work_ae). On EOF mid-line, breaks to clean-up; on a
full line, falls through to the formatting and print stage.
Reachable from the alignment branch at &BD54 and the per-line tail
at &BE29.""",
)


d.comment(0xBD8B, "Test escape and abort if pressed", align=Align.INLINE)
d.comment(0xBD8E, "A=&FF: count counter starts here so first INC -> 0", align=Align.INLINE)
d.comment(0xBD90, "Save counter (-1)", align=Align.INLINE)
d.label(0xBD92, "loop_read_dump_byte")

d.comment(0xBD92, "Y = file handle", align=Align.INLINE)
d.comment(0xBD94, "Read one byte via OSBGET (C set on EOF)", align=Align.INLINE)
d.comment(0xBD97, "EOF: finish off this line then exit", align=Align.INLINE)
d.comment(0xBD99, "Increment count counter", align=Align.INLINE)
d.comment(0xBD9B, "Y = current count (also buffer offset)", align=Align.INLINE)
d.comment(0xBD9D, "Store byte in 16-byte line buffer at (work_ae)+Y", align=Align.INLINE)
d.comment(0xBD9F, "Done all 16 bytes?", align=Align.INLINE)
d.comment(0xBDA1, "No: read next byte", align=Align.INLINE)
d.comment(0xBDA3, "C clear: not EOF (clean line)", align=Align.INLINE)
d.label(0xBDA4, "done_check_dump_eof")

d.comment(0xBDA4, "Save the EOF/clean flag", align=Align.INLINE)
d.comment(0xBDA5, "Reload counter byte", align=Align.INLINE)
d.comment(0xBDA7, "Bit 7 clear (counter is 0..&7F): bytes were read", align=Align.INLINE)
d.comment(0xBDA9, "EOF and no bytes: clean up and exit", align=Align.INLINE)
d.label(0xBDAB, "loop_pop_stack_buf")

d.subroutine(
    0xBDAB,
    "loop_pop_stack_buf",
    title="Drain saved bytes off stack and close",
    description="""Pulls X+1 bytes off the 6502 stack (clearing the temporary 21-byte
buffer cmd_dump uses to render each line) and tail-jumps to
close_ws_file. Reached from the in-line BPL at &BDAB and the
fall-through tail at &BE2E.""",
    on_entry={"x": "stack-byte count - 1 (caller sets it to &14 or &15)"},
)


d.comment(0xBDAB, "Restore one stack byte", align=Align.INLINE)
d.comment(0xBDAC, "Step", align=Align.INLINE)
d.comment(0xBDAD, "Loop while X >= 0 (22 pulls)", align=Align.INLINE)
d.comment(0xBDAF, "Tail-jump to close_ws_file", align=Align.INLINE)
d.label(0xBDB2, "done_check_boundary")

d.comment(0xBDB2, "Y=&10: read displayed-address byte 0", align=Align.INLINE)
d.comment(0xBDB4, "Read low byte", align=Align.INLINE)
d.comment(0xBDB6, "Top nibble", align=Align.INLINE)
d.comment(0xBDB8, "Non-zero: not a 256-byte boundary, skip header", align=Align.INLINE)
d.comment(0xBDBA, "Boundary: print column header", align=Align.INLINE)
d.label(0xBDBD, "done_start_dump_addr")

d.comment(0xBDBD, "Y=&13: highest byte of 4-byte address", align=Align.INLINE)
d.label(0xBDBF, "loop_print_addr_byte")

d.comment(0xBDBF, "Read address byte (highest first)", align=Align.INLINE)
d.comment(0xBDC1, "Save it (print_hex_byte clobbers A)", align=Align.INLINE)
d.comment(0xBDC2, "Print as 2 hex digits", align=Align.INLINE)
d.comment(0xBDC5, "Restore A", align=Align.INLINE)
d.comment(0xBDC6, "Step backwards", align=Align.INLINE)
d.comment(0xBDC7, "Reached low byte (offset &0F)?", align=Align.INLINE)
d.comment(0xBDC9, "No: continue printing", align=Align.INLINE)
d.comment(0xBDCB, "Y=&10: low byte of address", align=Align.INLINE)
d.comment(0xBDCC, "Clear C", align=Align.INLINE)
d.comment(0xBDCD, "Bump address by 16 bytes for next line", align=Align.INLINE)
d.comment(0xBDCF, "Save C from the add", align=Align.INLINE)
d.label(0xBDD0, "loop_inc_dump_addr")

d.comment(0xBDD0, "Restore C from previous step", align=Align.INLINE)
d.comment(0xBDD1, "Store updated address byte", align=Align.INLINE)
d.comment(0xBDD3, "Step Y up", align=Align.INLINE)
d.comment(0xBDD4, "Read next byte", align=Align.INLINE)
d.comment(0xBDD6, "Add carry from below", align=Align.INLINE)
d.comment(0xBDD8, "Save C", align=Align.INLINE)
d.comment(0xBDD9, "Done all 4 bytes (Y=&14)?", align=Align.INLINE)
d.comment(0xBDDB, "No: continue propagating", align=Align.INLINE)
d.comment(0xBDDD, "Restore final C", align=Align.INLINE)
d.comment(0xBDDE, "Print ' : ' separator before hex byte field", align=Align.INLINE)
d.comment(0xBDE4, "Y=0: start of buffer", align=Align.INLINE)
d.comment(0xBDE6, "X = byte counter (-1 initially, INC'd to 0..&0F)", align=Align.INLINE)
d.label(0xBDE8, "loop_print_dump_hex")

d.comment(0xBDE8, "Read byte from buffer", align=Align.INLINE)
d.comment(0xBDEA, "Print as hex + space", align=Align.INLINE)
d.label(0xBDED, "loop_next_dump_col")

d.subroutine(
    0xBDED,
    "loop_next_dump_col",
    title="*DUMP per-column advance and end-of-line check",
    description="""INY (next buffer offset), CPY #&10. End -> done_print_separator.
Otherwise DEX (decrement byte counter); BPL loop_print_dump_hex
to print the next byte. Single caller (the BPL at &BDFC after
short-line padding).""",
    on_entry={"x": "remaining bytes - 1", "y": "buffer offset"},
)


d.comment(0xBDED, "Step buffer offset", align=Align.INLINE)
d.comment(0xBDEE, "Done all 16?", align=Align.INLINE)
d.comment(0xBDF0, "Yes: print separator before ASCII field", align=Align.INLINE)
d.comment(0xBDF2, "Step counter (Y was off-by-one from line read)", align=Align.INLINE)
d.comment(0xBDF3, "Have a real byte? Print it", align=Align.INLINE)
d.comment(0xBDF5, "End of partial line: pad with 3 spaces", align=Align.INLINE)
d.comment(0xBDF6, "Print '   ' inline", align=Align.INLINE)
d.comment(0xBDFC, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0xBDFD, "Restore Y", align=Align.INLINE)
d.comment(0xBDFE, "Continue padding the rest of the hex column", align=Align.INLINE)
d.label(0xBE01, "done_print_separator")

d.comment(0xBE01, "Counter has finished -- step it once more for the ASCII test", align=Align.INLINE)
d.comment(0xBE02, "Print ': ' inline (ASCII field separator)", align=Align.INLINE)
d.comment(0xBE07, "Y=0: rewind to start of line buffer", align=Align.INLINE)
d.comment(0xBE09, "Skip 16 padding spaces if needed (inx16)", align=Align.INLINE)
d.label(0xBE0C, "loop_print_dump_ascii")

d.comment(0xBE0C, "Read line buffer byte", align=Align.INLINE)
d.comment(0xBE0E, "Mask off bit 7 (DEL/inverted)", align=Align.INLINE)
d.comment(0xBE10, "Below ' '? (control char)", align=Align.INLINE)
d.comment(0xBE12, "Yes: skip to substitution", align=Align.INLINE)
d.label(0xBE14, "skip_non_printable")

d.comment(0xBE14, "Substitute '.' for non-printables", align=Align.INLINE)
d.label(0xBE16, "done_test_del")

d.comment(0xBE16, "Compare with DEL", align=Align.INLINE)
d.comment(0xBE18, "Equal: also non-printable, substitute '.'", align=Align.INLINE)
d.comment(0xBE1A, "Print the (possibly substituted) character", align=Align.INLINE)
d.comment(0xBE1D, "Step Y", align=Align.INLINE)
d.comment(0xBE1E, "Done 16 chars?", align=Align.INLINE)
d.comment(0xBE20, "Yes: end this line", align=Align.INLINE)
d.comment(0xBE22, "Step counter back", align=Align.INLINE)
d.comment(0xBE23, "Loop while X >= 0", align=Align.INLINE)
d.label(0xBE25, "done_end_dump_line")

d.comment(0xBE25, "Print newline at end of line", align=Align.INLINE)
d.comment(0xBE28, "Restore EOF flag", align=Align.INLINE)
d.comment(0xBE29, "EOF: tidy up and exit", align=Align.INLINE)
d.comment(0xBE2B, "More to dump: jump to next line", align=Align.INLINE)
d.label(0xBE2E, "done_dump_eof")

d.comment(0xBE2E, "X=&14: balance the loop_pop_stack_buf counter", align=Align.INLINE)
d.comment(0xBE30, "Tail-jump to clean up the 21-byte stack buffer and close the file", align=Align.INLINE)
d.label(0xBE33, "print_dump_header")

d.subroutine(
    0xBE33,
    "print_dump_header",
    title="Print hex dump column header line",
    description="""Outputs the starting address followed by 16 hex
column numbers (00-0F), each separated by a space.
Provides the column alignment header for *Dump
output.""",
    on_exit={"a, x, y": "clobbered (print_hex_byte + OSASCI loop)"},
)


d.comment(0xBE33, "Read low nibble of starting address from (work_ae),Y", align=Align.INLINE)
d.comment(0xBE35, "Save it (we'll print it 16 times incrementing each iteration)", align=Align.INLINE)
d.comment(0xBE36, "Print '<CR>Address  : ' header via inline string", align=Align.INLINE)
d.comment(0xBE39, "*Dump column header", align=Align.INLINE)
d.comment(0xBE45, "X=&0F: print 16 column-number digits", align=Align.INLINE)
d.comment(0xBE47, "Pull the starting low nibble back into A", align=Align.INLINE)
d.comment(0xBE48, "Print A as two hex digits + space", align=Align.INLINE)
d.label(0xBE48, "loop_print_hex_row")

d.comment(0xBE4B, "Set C ready for the increment", align=Align.INLINE)
d.comment(0xBE4C, "A += 1 (column index increments, with C set on entry)", align=Align.INLINE)
d.comment(0xBE4E, "Wrap to nibble (0..15)", align=Align.INLINE)
d.comment(0xBE50, "Step column counter", align=Align.INLINE)
d.comment(0xBE51, "Loop while X >= 0 (16 iterations)", align=Align.INLINE)
d.comment(0xBE53, "Print ':    ASCII data<CR><CR>' trailer via inline", align=Align.INLINE)
d.comment(0xBE56, "*Dump trailer", align=Align.INLINE)
d.comment(0xBE67, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0xBE68, "Return", align=Align.INLINE)
d.label(0xBE69, "print_hex_and_space")

d.subroutine(
    0xBE69,
    "print_hex_and_space",
    title="Print hex byte followed by space",
    description="""Saves A, prints it as a 2-digit hex value via
print_hex_byte, outputs a space character, then
restores A from the stack. Used by cmd_dump and
print_dump_header for column-aligned hex output.""",
    on_entry={"a": "byte value to print"},
)


d.comment(0xBE69, "Save A so the caller can re-use the value", align=Align.INLINE)
d.comment(0xBE6A, "Print A as two hex digits", align=Align.INLINE)
d.comment(0xBE6D, "A=' ': trailing column separator", align=Align.INLINE)
d.comment(0xBE6F, "Print the space via OSASCI", align=Align.INLINE)
d.label(0xBE72, "done_print_hex_space")

d.comment(0xBE72, "Restore caller's A", align=Align.INLINE)
d.comment(0xBE73, "Return", align=Align.INLINE)
d.label(0xBE74, "parse_dump_range")

d.subroutine(
    0xBE74,
    "parse_dump_range",
    title="Parse hex address for dump range",
    description="""Reads up to 4 hex digits from the command line
into a 4-byte accumulator, stopping at CR or
space. Each digit shifts the accumulator left
by 4 bits before ORing in the new nybble.""",
    on_entry={"y": "current command-line offset"},
    on_exit={"y": "advanced past the parsed digits", "a": "first non-hex character (CR or space)"},
)


d.comment(0xBE74, "Move command-line offset Y into A for the X copy", align=Align.INLINE)
d.comment(0xBE75, "X = current command-line offset (live cursor)", align=Align.INLINE)
d.comment(0xBE76, "A=0: zero-fill value", align=Align.INLINE)
d.comment(0xBE78, "Y=0: accumulator index", align=Align.INLINE)
d.label(0xBE79, "loop_clear_hex_accum")

d.comment(0xBE79, "Zero accumulator byte at (work_ae)+Y", align=Align.INLINE)
d.comment(0xBE7B, "Step accumulator", align=Align.INLINE)
d.comment(0xBE7C, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0xBE7E, "No: continue clearing", align=Align.INLINE)
d.label(0xBE80, "loop_parse_hex_digit")

d.subroutine(
    0xBE80,
    "loop_parse_hex_digit",
    title="*DUMP / *LIST hex-address parser per-character body",
    description="""Reload command-line offset from X, INX (step cursor), TAY (use as
indirect index), read (os_text_ptr),Y. Branches: CR -> done; space
-> end of token; otherwise validate hex digit and shift it into the
4-byte accumulator. Single caller (the BNE retry at &BE95).""",
    on_entry={"x": "current command-line offset"},
)


d.comment(0xBE80, "Reload command-line offset", align=Align.INLINE)
d.comment(0xBE81, "Step cursor", align=Align.INLINE)
d.comment(0xBE82, "Y = stepped cursor (for the indirect read)", align=Align.INLINE)
d.comment(0xBE83, "Read next command-line byte", align=Align.INLINE)
d.comment(0xBE85, "CR? (end of address)", align=Align.INLINE)
d.comment(0xBE87, "Yes: range parsed -- exit via space-skip", align=Align.INLINE)
d.comment(0xBE89, "Space?", align=Align.INLINE)
d.comment(0xBE8B, "Yes: also a separator -- exit", align=Align.INLINE)
d.comment(0xBE8D, "Below '0'?", align=Align.INLINE)
d.comment(0xBE8F, "Yes: not hex -- raise 'Bad hex'", align=Align.INLINE)
d.comment(0xBE91, "Above '9'?", align=Align.INLINE)
d.comment(0xBE93, "No: it's '0'-'9' -- skip the letter handling", align=Align.INLINE)
d.comment(0xBE95, "Force uppercase via AND #&5F", align=Align.INLINE)
d.comment(
    0xBE97,
    "Add &B8: 'A' (=&41) becomes &F9 with C set; 'F' becomes &FE; this maps 'A'-'F' to &FA-&FF in C",
    align=Align.INLINE,
)
d.comment(0xBE99, "Carry out of ADC: digit was below 'A' -> bad hex", align=Align.INLINE)
d.comment(0xBE9B, "Below &FA? (i.e. before 'A' in mapped range)", align=Align.INLINE)
d.comment(0xBE9D, "Yes (out of [&FA,&FF]): bad hex", align=Align.INLINE)
d.label(0xBE9F, "done_mask_hex_digit")

d.comment(0xBE9F, "Keep low nibble (0-15)", align=Align.INLINE)
d.comment(0xBEA1, "Push the new nibble", align=Align.INLINE)
d.comment(0xBEA2, "Push X (current command-line offset)", align=Align.INLINE)
d.comment(0xBEA3, "Preserve on stack", align=Align.INLINE)
d.comment(0xBEA4, "X=4: rotate the 4-byte accumulator left 4 times", align=Align.INLINE)
d.label(0xBEA6, "loop_shift_nibble")

d.comment(0xBEA6, "Y=0: byte index for the rotate", align=Align.INLINE)
d.comment(0xBEA8, "A=0 (and C clear from TYA's flags)", align=Align.INLINE)
d.label(0xBEA9, "loop_rotate_hex_accum")

d.comment(0xBEA9, "Save A onto stack so we can use PHP/PLP to round-trip carry through the rotate", align=Align.INLINE)
d.comment(
    0xBEAA,
    "Pull flags (effectively C clear from the TYA above; on later iterations C carries the bit shifted out)",
    align=Align.INLINE,
)
d.comment(0xBEAB, "Read next accumulator byte", align=Align.INLINE)
d.comment(0xBEAD, "Shift in C from below, shift out top bit to C", align=Align.INLINE)
d.comment(0xBEAE, "Write back", align=Align.INLINE)
d.comment(0xBEB0, "Save the new C", align=Align.INLINE)
d.comment(0xBEB1, "Pull A back (PHA earlier)", align=Align.INLINE)
d.comment(0xBEB2, "Step accumulator byte", align=Align.INLINE)
d.comment(0xBEB3, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0xBEB5, "No: rotate next byte", align=Align.INLINE)
d.comment(0xBEB7, "PHA/PLP: bring saved C into flag register", align=Align.INLINE)
d.comment(0xBEB8, "C = overflow bit", align=Align.INLINE)
d.comment(0xBEB9, "C set: a bit fell off the top -- overflow", align=Align.INLINE)
d.comment(0xBEBB, "Step rotate counter", align=Align.INLINE)
d.comment(0xBEBC, "Loop while X != 0 (4 rotates total)", align=Align.INLINE)
d.comment(0xBEBE, "Pull saved X (command-line offset)", align=Align.INLINE)
d.comment(0xBEBF, "Restore X", align=Align.INLINE)
d.comment(0xBEC0, "Pull saved nibble into A", align=Align.INLINE)
d.comment(0xBEC1, "Y=0: low byte of accumulator", align=Align.INLINE)
d.comment(0xBEC3, "OR new nibble into accumulator[0]", align=Align.INLINE)
d.comment(0xBEC5, "Write back", align=Align.INLINE)
d.comment(0xBEC7, "Loop for next hex digit", align=Align.INLINE)
d.label(0xBECA, "error_hex_overflow")

d.comment(0xBECA, "Discard saved nibble", align=Align.INLINE)
d.comment(0xBECB, "Discard saved X", align=Align.INLINE)
d.comment(0xBECC, "Set C: signal overflow to caller", align=Align.INLINE)
d.comment(0xBECD, "Return with C=1", align=Align.INLINE)
d.label(0xBECE, "error_bad_hex_value")

d.comment(0xBECE, "Close the dump file before raising the error", align=Align.INLINE)
d.comment(0xBED1, "Raise 'Bad hex' error; never returns", align=Align.INLINE)
d.label(0xBED4, "loop_skip_hex_spaces")

d.comment(0xBED4, "Step past current space", align=Align.INLINE)
d.label(0xBED5, "done_test_hex_space")

d.comment(0xBED5, "Read next byte", align=Align.INLINE)
d.comment(0xBED7, "Still a space?", align=Align.INLINE)
d.comment(0xBED9, "Yes: keep skipping", align=Align.INLINE)
d.comment(0xBEDB, "Clear C: signal success", align=Align.INLINE)
d.comment(0xBEDC, "Return", align=Align.INLINE)
d.label(0xBEDD, "init_dump_buffer")

d.subroutine(
    0xBEDD,
    "init_dump_buffer",
    title="Initialise dump buffer and parse address range",
    description="""Parses the start and end addresses from the command
line via parse_dump_range. If no end address is given,
defaults to the file extent. Validates both addresses
against the file size, raising 'Outside file' if either
exceeds the extent.""",
    on_entry={"y": "command-line offset of the address arguments"},
)


d.comment(0xBEDD, "Step Y past the *Dump command name into the argument", align=Align.INLINE)
d.comment(0xBEDE, "Save the cursor offset", align=Align.INLINE)
d.comment(0xBEE0, "Set bit 0 of addr_work to 1 -- 'mode' flag for parse_dump_range below", align=Align.INLINE)
d.comment(0xBEE2, "Save mode flag", align=Align.INLINE)
d.comment(0xBEE4, "Parse the start address (max 4 hex digits)", align=Align.INLINE)
d.comment(0xBEE7, "Overflow: too many digits", align=Align.INLINE)
d.comment(0xBEE9, "Save current Y (cursor after start address)", align=Align.INLINE)
d.comment(0xBEEA, "Push it", align=Align.INLINE)
d.comment(0xBEEB, "Y = file handle saved in ws_page", align=Align.INLINE)
d.comment(0xBEED, "X=&AA: zero-page address for OSARGS result", align=Align.INLINE)
d.comment(0xBEEF, "A=2: OSARGS sub-fn 2 = read sequential file extent", align=Align.INLINE)
d.comment(0xBEF1, "Get file size into 4 bytes at &AA", align=Align.INLINE)
d.comment(0xBEF4, "Y=3: compare 4-byte values (high to low)", align=Align.INLINE)
d.label(0xBEF6, "loop_cmp_file_length")

d.comment(0xBEF6, "Read file size byte at &AA+Y", align=Align.INLINE)
d.comment(0xBEF9, "Compare with parsed start address (work_ae+Y)", align=Align.INLINE)
d.comment(0xBEFB, "Mismatch: branch decides which is bigger", align=Align.INLINE)
d.comment(0xBEFD, "Step to next byte", align=Align.INLINE)
d.comment(0xBEFE, "Loop while Y >= 0 (covers indices 3, 2, 1, 0)", align=Align.INLINE)
d.comment(0xBF00, "All bytes equal: start = extent (allowed); jump to the post-validation path", align=Align.INLINE)
d.label(0xBF02, "done_check_outside")

d.comment(0xBF02, "C clear: parsed_start > file_size -- reject", align=Align.INLINE)
d.comment(0xBF04, "Y=&FF: signal 'no copy needed' to the loop below", align=Align.INLINE)
d.comment(0xBF06, "Always taken: skip directly to advance phase", align=Align.INLINE)
d.label(0xBF08, "error_outside_file")

d.comment(0xBF08, "Close the file before raising", align=Align.INLINE)
d.comment(0xBF0B, "A=&B7: 'Outside file' error code", align=Align.INLINE)
d.comment(0xBF0D, "Raise via inline string; never returns", align=Align.INLINE)
d.comment(0xBF10, "*Dump range error", align=Align.INLINE)
d.label(0xBF1D, "loop_copy_osword_data")

d.label(0xBF1D, "loop_copy_start_addr")

d.comment(0xBF1D, "Copy file-extent byte from osword_flag to (work_ae)", align=Align.INLINE)
d.comment(0xBF1F, "Store it (used as default end address)", align=Align.INLINE)
d.label(0xBF22, "done_advance_start")

d.comment(0xBF22, "Step Y", align=Align.INLINE)
d.comment(0xBF23, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0xBF25, "No: continue copying", align=Align.INLINE)
d.comment(0xBF27, "X=&AA: zero-page source for the OSARGS write-back", align=Align.INLINE)
d.comment(0xBF29, "Y = file handle", align=Align.INLINE)
d.comment(0xBF2B, "A=1: OSARGS sub-fn 1 = write sequential file pointer", align=Align.INLINE)
d.comment(0xBF2D, "Set the file's read pointer to the parsed start", align=Align.INLINE)
d.comment(0xBF30, "Pull saved cursor offset", align=Align.INLINE)
d.comment(0xBF31, "Restore into Y", align=Align.INLINE)
d.comment(0xBF32, "Read next command-line byte", align=Align.INLINE)
d.comment(0xBF34, "CR (end of args)?", align=Align.INLINE)
d.comment(0xBF36, "No: there's a second arg -- handle below", align=Align.INLINE)
d.comment(0xBF38, "Y=1: copy os_text_ptr (2 bytes) to work_ae as a displacement-base hint", align=Align.INLINE)
d.label(0xBF3A, "loop_copy_osfile_ptr")

d.comment(0xBF3A, "Read os_text_ptr+Y", align=Align.INLINE)
d.comment(0xBF3D, "Save in work_ae+Y", align=Align.INLINE)
d.comment(0xBF3F, "Step backwards", align=Align.INLINE)
d.comment(0xBF40, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xBF42, "A=5: OSFILE sub-fn 5 = read catalogue info", align=Align.INLINE)
d.comment(0xBF44, "X = filename pointer low (work_ae)", align=Align.INLINE)
d.comment(0xBF46, "Y = filename pointer high (addr_work)", align=Align.INLINE)
d.comment(0xBF48, "Read load address into work_ae+0..3", align=Align.INLINE)
d.comment(
    0xBF4B, "Y=2: shift 3 bytes down 2 positions to drop the first 2 bytes (action code + a flag)", align=Align.INLINE
)
d.label(0xBF4D, "loop_shift_osfile_data")

d.comment(0xBF4D, "Read source byte", align=Align.INLINE)
d.comment(0xBF4F, "Y -= 2 (destination)", align=Align.INLINE)
d.comment(0xBF50, "Continue decrement", align=Align.INLINE)
d.comment(0xBF51, "Store at destination", align=Align.INLINE)
d.comment(0xBF53, "Y += 3 to advance to next source", align=Align.INLINE)
d.comment(0xBF54, "(continued)", align=Align.INLINE)
d.comment(0xBF55, "(continued)", align=Align.INLINE)
d.comment(0xBF56, "Done 6 bytes shifted?", align=Align.INLINE)
d.comment(0xBF58, "No: continue", align=Align.INLINE)
d.comment(0xBF5A, "Y -= 2: position at high byte of load address", align=Align.INLINE)
d.comment(0xBF5B, "Y=4: check from buf[4] downward", align=Align.INLINE)
d.label(0xBF5C, "loop_check_ff_addr")

d.comment(0xBF5C, "Read load-address byte at Y", align=Align.INLINE)
d.comment(0xBF5E, "Is it &FF (signals no real load address)?", align=Align.INLINE)
d.comment(0xBF60, "No: have a real load address; add it as displacement", align=Align.INLINE)
d.comment(0xBF62, "Yes: step back to next higher byte", align=Align.INLINE)
d.comment(0xBF63, "Loop until Y=0", align=Align.INLINE)
d.comment(0xBF65, "All four bytes were &FF: zero out the load address", align=Align.INLINE)
d.comment(0xBF67, "A=0", align=Align.INLINE)
d.label(0xBF69, "loop_zero_load_addr")

d.comment(0xBF69, "Zero work_ae+Y", align=Align.INLINE)
d.comment(0xBF6B, "Step backwards", align=Align.INLINE)
d.comment(0xBF6C, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xBF6E, "Always taken (after BPL drops out): skip second-arg path", align=Align.INLINE)
d.label(0xBF70, "done_parse_disp_base")

d.comment(0xBF70, "Parse end-address argument", align=Align.INLINE)
d.comment(0xBF73, "Success: continue with displacement-add", align=Align.INLINE)
d.comment(0xBF75, "Parse error: close file then raise 'Bad address'", align=Align.INLINE)
d.comment(0xBF78, "A=&FC: 'Bad address' error code", align=Align.INLINE)
d.comment(0xBF7A, "Raise; never returns", align=Align.INLINE)
d.label(0xBF85, "done_add_disp_base")

d.comment(0xBF85, "Y=0: start of work_ae", align=Align.INLINE)
d.comment(0xBF87, "X=4: 4-byte add", align=Align.INLINE)
d.comment(0xBF89, "Clear C for the add", align=Align.INLINE)
d.label(0xBF8A, "loop_add_disp_bytes")

d.comment(0xBF8A, "Read low byte of address from (work_ae)+Y", align=Align.INLINE)
d.comment(0xBF8C, "Add osword_flag+Y (low byte of length, with carry propagating)", align=Align.INLINE)
d.comment(0xBF8F, "Store sum back to osword_flag+Y", align=Align.INLINE)
d.comment(0xBF92, "Advance to next byte", align=Align.INLINE)
d.comment(0xBF93, "Decrement byte counter", align=Align.INLINE)
d.comment(0xBF94, "Loop until 4 bytes added", align=Align.INLINE)
d.comment(
    0xBF96, "Y=&14: target offset = workspace+&13 (top of end-addr field, stored hi-byte-first)", align=Align.INLINE
)
d.comment(0xBF98, "X=3: source = osword_flag+3 (top byte of sum)", align=Align.INLINE)
d.label(0xBF9A, "loop_store_disp_addr")

d.comment(0xBF9A, "Pre-decrement Y (so first store is to offset &13)", align=Align.INLINE)
d.comment(0xBF9B, "Read sum byte from osword_flag+X", align=Align.INLINE)
d.comment(0xBF9D, "Store at (work_ae)+Y", align=Align.INLINE)
d.comment(0xBF9F, "Decrement source index", align=Align.INLINE)
d.comment(0xBFA0, "Loop until X wraps below 0", align=Align.INLINE)
d.comment(0xBFA2, "Return", align=Align.INLINE)
d.label(0xBFA3, "close_ws_file")

d.subroutine(
    0xBFA3,
    "close_ws_file",
    title="Close file handle stored in workspace",
    description="""Loads the file handle from ws_page and closes it
via OSFIND with A=0.""",
    on_exit={"a, x, y": "clobbered (OSFIND)"},
)


d.comment(0xBFA3, "Y = saved file handle from ws_page", align=Align.INLINE)
d.comment(0xBFA5, "A=0: OSFIND close", align=Align.INLINE)
d.comment(0xBFA7, "Tail-call OSFIND to close the handle", align=Align.INLINE)
d.label(0xBFAA, "open_file_for_read")

d.subroutine(
    0xBFAA,
    "open_file_for_read",
    title="Open file for reading via OSFIND",
    description="""Computes the filename address from the command text
pointer plus the Y offset, calls OSFIND with A=&40
(open for input). Stores the handle in ws_page.
Raises 'Not found' if the returned handle is zero.""",
    on_entry={"y": "offset within the command line of the filename to open"},
    on_exit={"a, x, y": "clobbered"},
)

d.comment(0xBFAA, "Save flags so caller's NZC survive", align=Align.INLINE)
d.comment(0xBFAB, "Move command-line offset Y into A for the add", align=Align.INLINE)
d.comment(0xBFAC, "Clear C for the 16-bit add", align=Align.INLINE)
d.comment(0xBFAD, "A = os_text_ptr_lo + Y (filename address low byte)", align=Align.INLINE)
d.comment(0xBFAF, "Push it (we need to restore os_text_ptr after OSFIND)", align=Align.INLINE)
d.comment(0xBFB0, "Move filename low into X (OSFIND wants the address in X/Y)", align=Align.INLINE)
d.comment(0xBFB1, "A=0: zero high byte before the carry-add", align=Align.INLINE)
d.comment(0xBFB3, "Add os_text_ptr_hi with carry from the low add", align=Align.INLINE)
d.comment(0xBFB5, "Push filename high byte for the restore", align=Align.INLINE)
d.comment(0xBFB6, "Move filename high into Y", align=Align.INLINE)
d.comment(0xBFB7, "A=&40: OSFIND open-for-input mode", align=Align.INLINE)
d.comment(0xBFB9, "Open the file; returns handle in A (zero on failure)", align=Align.INLINE)
d.comment(0xBFBC, "Copy returned handle into Y (also sets Z if zero)", align=Align.INLINE)
d.comment(0xBFBD, "Stash the handle in ws_page for later close", align=Align.INLINE)
d.comment(0xBFBF, "Non-zero: open succeeded, skip error path", align=Align.INLINE)
d.comment(0xBFC1, "A=&D6: 'Not found' error code", align=Align.INLINE)
d.comment(0xBFC3, "Raise the error with the inline string below; never returns", align=Align.INLINE)
d.label(0xBFD0, "restore_text_ptr")

d.comment(
    0xBFD0,
    "Restore the saved filename high byte into os_text_ptr_hi -- but wait, this writes the FILENAME address into os_text_ptr; the caller intentionally moves os_text_ptr to scan past the filename below",
    align=Align.INLINE,
)
d.comment(0xBFD1, "Store as os_text_ptr_hi", align=Align.INLINE)
d.comment(
    0xBFD3,
    "Restore filename low byte into os_text_ptr_lo (so (os_text_ptr) now points at the filename)",
    align=Align.INLINE,
)
d.comment(0xBFD4, "Store as os_text_ptr lo", align=Align.INLINE)

d.comment(0xBFD6, "Y=0: scan from start of filename", align=Align.INLINE)
d.label(0xBFD8, "loop_skip_filename")

d.comment(0xBFD8, "Step to next byte", align=Align.INLINE)
d.comment(0xBFD9, "Read filename byte", align=Align.INLINE)
d.comment(0xBFDB, "Hit CR? End of command line", align=Align.INLINE)
d.comment(0xBFDD, "Yes: filename ended at CR (no trailing spaces)", align=Align.INLINE)
d.comment(0xBFDF, "Hit space? End of filename", align=Align.INLINE)
d.comment(0xBFE1, "No (still inside filename): keep scanning", align=Align.INLINE)
d.label(0xBFE3, "loop_skip_fn_spaces")

d.comment(0xBFE3, "Step past spaces", align=Align.INLINE)
d.comment(0xBFE4, "Read next byte", align=Align.INLINE)
d.comment(0xBFE6, "Still a space?", align=Align.INLINE)
d.comment(0xBFE8, "Yes: keep skipping", align=Align.INLINE)
d.label(0xBFEA, "done_skip_filename")


d.comment(0xBFEA, "Done: Y points just past the filename and any spaces", align=Align.INLINE)
d.comment(0xBFEB, "Restore caller's flags", align=Align.INLINE)
d.label(0xBFEC, "inx16")

d.subroutine(
    0xBFEC,
    "inx16",
    title="Increment X 16 times",
    description="""`JSR` [`inx8`](label:inx8), then fall through into `inx8` for a second pass — 16 `INX` instructions in total.""",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 16", "a, y": "preserved"},
)


d.comment(0xBFEC, "JSR inx8; on RTS, fall through into inx8 for the second 8", align=Align.INLINE)
d.label(0xBFEF, "inx8")

d.subroutine(
    0xBFEF,
    "inx8",
    title="Increment X 8 times",
    description="""`JSR` [`inx4`](label:inx4), then fall through into `inx4` for a second pass — 8 `INX` instructions in total.""",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 8", "a, y": "preserved"},
)


d.comment(0xBFEF, "JSR inx4; on RTS, fall through into inx4 for the second 4", align=Align.INLINE)
d.label(0xBFF2, "inx4")
d.subroutine(
    0xBFF2,
    "inx4",
    title="Increment X 4 times",
    description="""Four consecutive `INX` instructions then `RTS`. Building block for [`inx8`](label:inx8) and [`inx16`](label:inx16) via JSR/fall-through chaining.""",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 4", "a, y": "preserved", "n, z flags": "reflect new X"},
)
d.comment(0xBFF2, "X += 4", align=Align.INLINE)
d.comment(0xBFF3, "(continued)", align=Align.INLINE)
d.comment(0xBFF4, "(continued)", align=Align.INLINE)
d.comment(0xBFF5, "(continued)", align=Align.INLINE)
d.comment(
    0xBFF6, "Return — total X advance depends on the entry: 4 (inx4), 8 (inx8), or 16 (inx16)", align=Align.INLINE
)
# UNMAPPED: d.label(0xBFF7, "rom_tail_padding")
# UNMAPPED: d.banner(
# UNMAPPED:     0xBFF7,
# UNMAPPED:     title="ROM-tail &FF padding (33 bytes positioning the HAZEL indexing bases)",
# UNMAPPED:     description="""33 bytes of `&FF` filler between the last real instruction at
# UNMAPPED: [`inx4`](label:inx4) and the HAZEL indexing-base labels
# UNMAPPED: starting at [`hazel_minus_1a`](label:hazel_minus_1a).
# UNMAPPED: 
# UNMAPPED: These bytes exist purely to push the indexing-base labels to
# UNMAPPED: specific addresses immediately before `&C000` (the start of
# UNMAPPED: HAZEL). The labels themselves do the work -- see the
# UNMAPPED: [`hazel_idx_bases`](label:hazel_idx_bases) banner. The padding is never
# UNMAPPED: read or written; it is whatever the assembler emitted to fill
# UNMAPPED: the gap (the BeebAsm default of `&FF`).""",
# UNMAPPED: )

# UNMAPPED: d.comment(0xBFF7, "ROM-tail padding (2 bytes &FF)", align=Align.INLINE)
# UNMAPPED: d.byte(0xBFF9)

# UNMAPPED: d.comment(0xBFF9, "ROM-tail padding (1 byte &FF; on its own line for annotation)", align=Align.INLINE)
# UNMAPPED: d.comment(0xBFFA, "ROM-tail padding (30 bytes &FF)", align=Align.INLINE)
d.index_base(0xBFE6, "hazel_minus_1a")

# UNMAPPED: d.index_base(0xBFE6, "hazel_idx_bases")
# UNMAPPED: d.banner(
# UNMAPPED:     0xBFE6,
# UNMAPPED:     title="HAZEL Y-indexed access bases (3 labels at the ROM tail)",
# UNMAPPED:     description="""Three labels positioned `&1A`, `2`, and `1` bytes before `&C000`
# UNMAPPED: (the start of HAZEL), used as **indexing bases for reads and
# UNMAPPED: writes into HAZEL**.
# UNMAPPED: 
# UNMAPPED: The trick: HAZEL begins at `&C000`, so an `LDA hazel_minus_2,Y`
# UNMAPPED: / `STA hazel_minus_2,Y` instruction with Y >= 2 lands at
# UNMAPPED: `&BFFE + Y >= &C000` -- inside HAZEL. ANFS exploits this in
# UNMAPPED: several places to copy fixed-size blocks between HAZEL workspace
# UNMAPPED: and other buffers without burning a separate two-byte zero-page
# UNMAPPED: pointer:
# UNMAPPED: 
# UNMAPPED: | Site / routine                | instruction                  | base             | Y range | Effective range            |
# UNMAPPED: |-------------------------------|------------------------------|------------------|---------|----------------------------|
# UNMAPPED: | `loop_copy_fs_ctx`            | `STA hazel_minus_2,Y`        | `hazel_minus_2`  | 9..2    | `&C007..&C000`             |
# UNMAPPED: | `loop_restore_ctx`            | `LDA hazel_minus_2,Y`        | `hazel_minus_2`  | 9..2    | `&C007..&C000`             |
# UNMAPPED: | `loop_copy_ws_to_pb`          | `LDA hazel_minus_2,Y`        | `hazel_minus_2`  | 4..6    | `&C002..&C004`             |
# UNMAPPED: | `loop_copy_station`           | `LDA hazel_minus_1,Y`        | `hazel_minus_1`  | 2..1    | `&C001..&C000`             |
# UNMAPPED: | `osword_13_set_station_body`  | `STA hazel_minus_1,Y`        | `hazel_minus_1`  | 2..1    | `&C001..&C000`             |
# UNMAPPED: | `loop_copy_txcb_init`         | `LDA hazel_minus_1a,Y`       | `hazel_minus_1a` | >= &1A  | spans into HAZEL from `&C000` |
# UNMAPPED: 
# UNMAPPED: Each loop's CPY/BNE guard stops Y before it would land inside
# UNMAPPED: the ROM tail, so the actual workspace data lives entirely in
# UNMAPPED: HAZEL. The labels themselves never have their own bytes read --
# UNMAPPED: the `&FF` byte at each label address is incidental, only the
# UNMAPPED: address matters.""",
# UNMAPPED: )
# UNMAPPED: d.comment(
# UNMAPPED:     0xBFE6,
# UNMAPPED:     "Base for `hazel_minus_1a,Y` reads in loop_copy_txcb_init -- `&BFE6 + Y` reaches into HAZEL for Y >= &1A",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
d.index_base(0xBFFE, "hazel_minus_2")

# UNMAPPED: d.comment(
# UNMAPPED:     0xBFFE,
# UNMAPPED:     "Base for `hazel_minus_2,Y` reads/writes -- `&BFFE + Y` reaches into HAZEL for Y >= 2 (used by loop_copy_fs_ctx, loop_restore_ctx, loop_copy_ws_to_pb)",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
d.index_base(0xBFFF, "hazel_minus_1")

# UNMAPPED: d.comment(
# UNMAPPED:     0xBFFF,
# UNMAPPED:     "Base for `hazel_minus_1,Y` reads/writes -- `&BFFF + Y` reaches into HAZEL for Y >= 1 (used by loop_copy_station, osword_13_set_station)",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
d.label(
    0xC000,
    "hazel_fs_station",
    description="""Filing-system state block (`&C000`–`&C00A`).

Eleven bytes of currently-selected-FS context kept in HAZEL: station / network of the FS, saved prefix station, multi-purpose CSD/library/boot-type slots, FS flags, messages flag, pending-state, error code, last-error, and `*OPT` addend. The first two bytes (`hazel_fs_station`, `hazel_fs_network`) are the FS address used for every TX scout.""",
    length=11,
    group="hazel",
    access="rw",
)

d.label(
    0xC001,
    "hazel_fs_network",
    description="FS network number (sub-byte of the &C000 FS context block).",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC002, "hazel_fs_saved_station")

d.label(
    0xC003,
    "hazel_fs_context_copy",
    description="Multi-purpose sub-byte of the &C000 block: CSD handle / matched-entry index / Y-indexed base into FS context block.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC004,
    "hazel_fs_prefix_stn",
    description="Multi-purpose sub-byte of the &C000 block: saved-prefix station / library handle / boot type.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC005, "hazel_fs_flags")

d.label(0xC006, "hazel_fs_messages_flag")

d.label(0xC007, "hazel_fs_pending_state")

d.label(
    0xC008,
    "hazel_fs_error_code",
    description="FS error code (sub-byte of the &C000 block).",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC009,
    "hazel_fs_last_error",
    description="Last FS error byte (sub-byte of the &C000 block).",
    length=1,
    group="hazel",
    access="rw",
)

d.index_base(0xC00A, "hazel_fs_opts_addend", group="hazel")

d.label(
    0xC014,
    "hazel_retry_counter",
    description="Retry counter for the current Econet TX/RX cycle.",
    length=1,
    group="hazel",
    access="rw",
)

d.index_base(0xC02F, "hazel_parse_buf_m1", group="hazel")

d.label(
    0xC030,
    "hazel_parse_buf",
    description="Three-byte parse-buffer used for command-line matching (e.g. `*OPT`, `*FS`).",
    length=3,
    group="hazel",
    access="rw",
)

d.label(0xC031, "hazel_parse_buf_1")

d.label(0xC032, "hazel_parse_buf_2")

d.index_base(
    0xC038,
    "hazel_rtc_buffer",
    description="OSWORD `&0E` real-time-clock result buffer.",
    length=25,
    group="hazel",
)

d.index_base(
    0xC0F7,
    "hazel_fs_reply_byte",
    description="Latched first byte of the most recent FS reply.",
    length=1,
    group="hazel",
)

d.label(
    0xC100,
    "hazel_txcb_port",
    description="TXCB byte 0: port number for the next TX scout.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC101,
    "hazel_txcb_func_code",
    description="TXCB byte 1: function code (FS command number).",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC102, "hazel_txcb_station", description="TXCB byte 2: destination station.", length=1, group="hazel", access="rw"
)

d.label(
    0xC103,
    "hazel_txcb_network",
    description="""TXCB byte 3: multi-purpose.
TXCB destination network (TX setup) / reply function code (RX context) / `fs_cmd_csd` buffer base (other paths).""",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC104,
    "hazel_txcb_lib",
    description="TXCB byte 4: library handle terminator / transfer-length param 1.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC105,
    "hazel_txcb_data",
    description="TXCB byte 5: first reply-data byte / data start.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC106, "hazel_txcb_flag", description="TXCB byte 6: direction flag.", length=1, group="hazel", access="rw")

d.label(
    0xC107, "hazel_txcb_count", description="TXCB byte 7: data count / lock flag.", length=1, group="hazel", access="rw"
)

d.label(
    0xC108,
    "hazel_txcb_result",
    description="TXCB byte 8: result / transfer-size lo.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC109, "hazel_exec_addr")


d.label(0xC10A, "hazel_txcb_size_hi")

d.label(0xC10B, "hazel_txcb_tx_status")

d.label(0xC10C, "hazel_txcb_osword_flag")

d.index_base(0xC10D, "hazel_txcb_addr_lo", group="hazel")

d.label(0xC10E, "hazel_txcb_access")

d.label(0xC110, "hazel_txcb_addr_hi")

d.label(0xC111, "hazel_txcb_len")

d.label(0xC112, "hazel_txcb_type")

d.label(0xC113, "hazel_txcb_objtype")

d.label(0xC114, "hazel_txcb_cycle")

d.label(0xC116, "hazel_txcb_byte_16")

d.label(0xC12F, "hazel_txcb_end")

d.label(0xC130, "hazel_examine_attr")

d.index_base(0xC1C8, "hazel_chan_status", group="hazel")

d.label(0xC1DC, "hazel_net_reply_buf_0")

d.label(0xC1DD, "hazel_net_reply_buf_1")

d.label(0xC1DE, "hazel_net_reply_buf_2")

d.label(0xC1DF, "hazel_net_reply_buf_3")

d.index_base(0xC1E0, "hazel_fcb_addr_lo_minus20", group="hazel")

d.index_base(0xC1F0, "hazel_fcb_addr_mid_minus20", group="hazel")

d.index_base(0xC1FF, "hazel_display_buf_minusF4", group="hazel")

d.index_base(
    0xC200,
    "hazel_fcb_addr_lo",
    description="""FCB parallel array (16 entries): file position byte 0 (low).
Indexed by channel `0..15`; cleared by [`alloc_fcb_slot`](label:alloc_fcb_slot) on FCB allocation.""",
    length=16,
    group="hazel",
)

d.index_base(
    0xC210,
    "hazel_fcb_addr_mid",
    description="FCB parallel array (16 entries): file position byte 1 (mid).",
    length=16,
    group="hazel",
)

d.index_base(
    0xC220,
    "hazel_fcb_addr_hi",
    description="FCB parallel array (16 entries): file position byte 2 (high).",
    length=16,
    group="hazel",
)

d.index_base(
    0xC230,
    "hazel_fcb_slot_attr",
    description="""FCB parallel array (16 entries): slot occupancy + channel attribute.
Tested for zero by [`alloc_fcb_slot`](label:alloc_fcb_slot) as the slot-free check; set non-zero on allocation.""",
    length=16,
    group="hazel",
)

d.index_base(
    0xC240,
    "hazel_fcb_state_byte",
    description="""FCB parallel array (16 entries): multi-purpose state byte.
Holds station number for non-OSFIND channels, or open-mode flags for channels created by OSFIND.""",
    length=16,
    group="hazel",
)

d.index_base(
    0xC250,
    "hazel_fcb_network",
    description="FCB parallel array (16 entries): network number per channel.",
    length=16,
    group="hazel",
)

d.index_base(
    0xC260,
    "hazel_fcb_status",
    description="""FCB parallel array (16 entries): per-channel status flags.
Heavily used: bit 6 = connection active (`set_conn_active` / `clear_conn_active` toggle).""",
    length=16,
    group="hazel",
)

d.label(0xC270, "hazel_cur_dir_handle")

d.label(
    0xC271,
    "hazel_fs_lib_flags",
    description="FS library / option flags. Bit 2 = auto-boot, bit 7 = library-directory pending. Cleared / tested by *Cat / *Lcat / *Ex / *Lex paths.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC272, "hazel_fcb_slot_1")

d.label(0xC273, "hazel_fcb_slot_2")

d.label(0xC274, "hazel_fcb_slot_3")

d.index_base(0xC278, "hazel_fcb_station_lo", group="hazel")

d.index_base(0xC288, "hazel_fcb_station_hi", group="hazel")

d.index_base(0xC298, "hazel_fcb_offset_save", group="hazel")

d.index_base(0xC2A8, "hazel_fcb_attr_ref", group="hazel")

d.index_base(0xC2B8, "hazel_fcb_flags", group="hazel")

d.label(
    0xC2C8,
    "hazel_cur_fcb_index",
    description="Current FCB index used by the FCB-scan loop in [`process_all_fcbs`](label:process_all_fcbs). Followed by the channel attribute / reference, byte-counter, buffer pointer and a small block of transfer-state scratch bytes used during file I/O.",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC2C9, "hazel_chan_attr")

d.label(0xC2CA, "hazel_chan_ref")

d.label(0xC2CB, "hazel_byte_counter_lo")

d.label(0xC2CC, "hazel_buf_addr_hi")

d.label(
    0xC2CD,
    "hazel_sentinel_cd",
    description="Sentinel/scratch byte at HAZEL+&CD, used by the FCB-scan loop in [`process_all_fcbs`](label:process_all_fcbs).",
    length=1,
    group="hazel",
    access="rw",
)

d.label(
    0xC2CE,
    "hazel_sentinel_ce",
    description="Sentinel/scratch byte at HAZEL+&CE, used by the FCB-scan loop in [`process_all_fcbs`](label:process_all_fcbs).",
    length=1,
    group="hazel",
    access="rw",
)

d.label(0xC2CF, "hazel_offset_counter")

d.label(0xC2D0, "hazel_pass_counter")

d.index_base(0xC2D1, "hazel_xfer_init_zeros", group="hazel")

d.label(0xC2D4, "hazel_station_lo")

d.label(0xC2D5, "hazel_station_hi")

d.label(0xC2D6, "hazel_transfer_flag")

d.label(0xC2D7, "hazel_saved_byte")

d.label(0xC2D8, "hazel_quote_mode")

d.index_base(
    0xC2D9,
    "hazel_ctx_buffer",
    description="HAZEL context buffer (saved register / state block used during FCB processing).",
    length=1,
    group="hazel",
)

d.index_base(0xC2F3, "hazel_display_buf", group="hazel")

d.label(
    0xFE28,
    "fdc_1770_command_or_status",
    description="""Master 128 1770 floppy-disk-controller command (write) / status
(read) register, part of the `&FE24`-`&FE2F` disk interface. ANFS does not
do disk I/O; the only access is a discarded read in `set_rom_ws_page`
(its result is overwritten before use).""",
    length=1,
    group="mmio",
    access="r",
)

d.label(
    0xFE2B,
    "fdc_1770_data",
    description="""Master 128 1770 floppy-disk-controller data register, part of the
`&FE24`-`&FE2F` disk interface. ANFS does not do disk I/O; the only
access is a discarded read in `set_rom_ws_page` (its result is
overwritten before use).""",
    length=1,
    group="mmio",
    access="r",
)

d.label(
    0xFE34,
    "acccon",
    description="""Master 128 ACCCON access-control register.

Bit-by-bit (write-only):

| Bit | Name | Effect when set |
|---|---|---|
| 7 | IRR | Interrupt Request: setting it asserts the CPU IRQ line (a software-triggered IRQ) |
| 6 | TST | Test mode |
| 5 | IFJ | I/O is JIM |
| 4 | ITU | Internal Tube |
| 3 | Y   | HAZEL paged in (`&C000-&DFFF` is hidden RAM) |
| 2 | X   | LYNNE paged in (`&3000-&7FFF` is shadow RAM) |
| 1 | E   | shadow RAM owns screen |
| 0 | D   | shadow RAM for the OS display |

ANFS uses bit 7 (IRR) as a deferred-work latch via `TRB`/`TSB`.""",
    length=1,
    group="mmio",
    access="rw",
)

d.label(
    0xFE38,
    "disable_net_nmis",
    description="""Master 128 INTOFF mirror (NMI-disable side effect).
Reading any byte here disables /NMI re-entry; the byte value itself is irrelevant.""",
    length=1,
    group="mmio",
    access="r",
)

d.label(
    0xFE3C,
    "enable_net_nmis",
    description="""Master 128 INTON mirror (NMI-enable side effect).
Reading any byte here re-enables /NMI; the byte value itself is irrelevant.""",
    length=1,
    group="mmio",
    access="r",
)

d.label(
    0xFEA0,
    "econet_control1_or_status1",
    description="""ADLC control register 1 / status register 1.
Write: `CR1` (or `CR3` if `AC=1`). Read: `SR1`.

`SR1` bits: `RDA` (b0), `S2RQ` (b1), `LOOP` (b2), `FD` (b3), `CTS` (b4), `TUF` (b5), `TDRA` (b6), `IRQ` (b7).""",
    length=1,
    group="mmio",
    access="rw",
)

d.label(
    0xFEA1,
    "econet_control23_or_status2",
    description="""ADLC control register 2 / status register 2.
Write: `CR2` (or `CR4` if `AC=1`). Read: `SR2`.

`SR2` bits: `AP` (b0), `FV` (b1), `RX_IDLE` (b2), `RX_ABRT` (b3), `ERR` (b4), `DCD` (b5), `OVRN` (b6), `RDA` (b7).""",
    length=1,
    group="mmio",
    access="rw",
)

d.label(
    0xFEA2,
    "econet_data_continue_frame",
    description="""ADLC TX FIFO continue / RX FIFO read.
Write: byte to TX FIFO with `LAST_DATA = 0` (continue frame).
Read: next byte from RX FIFO.""",
    length=1,
    group="mmio",
    access="rw",
)

d.label(
    0xFEA3,
    "econet_data_terminate_frame",
    description="""ADLC TX FIFO terminate / RX FIFO read.
Write: final byte of frame (`LAST_DATA = 1`; ADLC appends CRC + closing flag).
Read: next byte from RX FIFO.""",
    length=1,
    group="mmio",
    access="rw",
)

d.label(
    0xFF1B,
    "ev_filev",
    description="FILEV extended-vector dispatcher (file operations: OSFILE, OSFIND).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.label(
    0xFF1E,
    "ev_argsv",
    description="ARGSV extended-vector dispatcher (file argument operations: OSARGS).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.label(
    0xFF21,
    "ev_bgetv",
    description="BGETV extended-vector dispatcher (single-byte read: OSBGET).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.label(
    0xFF24,
    "ev_bputv",
    description="BPUTV extended-vector dispatcher (single-byte write: OSBPUT).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.label(
    0xFF27,
    "ev_gbpbv",
    description="GBPBV extended-vector dispatcher (block transfer: OSGBPB).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.label(
    0xFF2A,
    "ev_findv",
    description="FINDV extended-vector dispatcher (open / close: OSFIND).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.label(
    0xFF2D,
    "ev_fscv",
    description="FSCV extended-vector dispatcher (filing-system control: OSFSC, *commands).",
    length=3,
    group="ext_vectors",
    access="r",
)

d.index_base(
    0xFFB0,
    "nmi_buf_idx_base",
    description="""NMI buffer indexing-base.
Used by the NMI RX setup as `STA nmi_buf_idx_base,Y` with Y values that wrap into low memory; the bytes at `&FFB0` themselves aren't read or written.""",
    length=1,
    group="idx_base",
)

d.index_base(
    0xFFBD,
    "fcb_workspace_idx_base",
    description="""FCB-workspace indexing-base (wraps into ZP).
Used by `loop_save_fcb_workspace` as the base of `LDA &FFBD,X` with X=`&F7`..`&FF`; the effective address wraps to `&00B4`..`&00BC` (= `fs_work_4`+0..+8). The byte at `&FFBD` itself is never read.""",
    length=1,
    group="idx_base",
)

d.subroutine(
    0x864C,
    "tx_setup_from_txcb",
    title="Seed TX scout from the TX control block and dispatch on type",
    description="""Copies the destination station and network from the TX
control block (`(nmi_tx_block)`) into the TX scout buffer
([`tx_dst_stn`](label:tx_dst_stn) / [`tx_dst_net`](label:tx_dst_net)), then reads
the TXCB control byte: bit 7 set selects `tx_imm_op_setup` (an immediate
operation), bit 7 clear falls to `tx_bad_ctrl_error`. Three callers in
the TX-start paths.""",
)

d.subroutine(
    0x8BFD,
    "help_table_walk_entry",
    title="*HELP / command table walker per-entry body",
    description="""Per-entry body of the command / `*HELP` table walker:
saves Y and flags, then classifies `cmd_table_fs,X` (bit 7 marks a
sub-table terminator vs. a name byte). Called from the walker loop and
from the `*HELP` command lister.""",
)

d.subroutine(
    0x9659,
    "print_space_line",
    title="Print the 'Space' status label",
    description="""Emits the inline string `"Space"` + `CR` via
[`print_inline`](label:print_inline); the `&EA` (`NOP`) terminator resumes on
the trailing `RTS`. Called from the `*STATUS` / free-space report.""",
)

d.subroutine(
    0x85AF,
    "tx_calc_transfer",
    title="Calculate transfer size; handle Tube and shadow buffers",
    description="""Prepares the buffer-transfer for a completed receive.
Clears decimal mode, then seeds [`escapable`](label:escapable) from
[`ACCCON`](address:FE34) with the transfer-mode bit set. Inspects
`RXCB[6..7]` (buffer end address byte 2 and high) to classify the buffer:

| Buffer type | Action |
|---|---|
| Tube (`RXCB[7]=&FF`, `RXCB[6]` in `[&FE, &FF]`) | if shadow RAM is enabled (`ACCCON.E`), also set the shadow bit in `escapable`; then compute the 4-byte transfer size by subtracting `RXCB[8..&B]` (start) from `RXCB[4..7]` (end) |
| Non-Tube | branch to `fallback_calc_transfer` for the 1-byte size subtraction |

Three callers: [`scout_complete`](label:scout_complete) (`&819D`),
[`rx_imm_peek`](label:rx_imm_peek) (`&84D4`),
[`tx_ctrl_proc`](label:tx_ctrl_proc) (`&87A4`).""",
    on_entry={"y": "0 -- caller convention"},
    on_exit={"a": "transfer status", "c": "set if Tube/shadow address handled, clear otherwise"},
)

# ACCCON-guarded last-data-byte store (Master 128 shadow/HAZEL aware).
# The port receive buffer may live behind shadow/HAZEL paging, so ACCCON
# is saved, switched to the caller's `escapable` paging value, used for
# the `(open_port_buf),Y` store, then restored.
d.comment(0x8287, "Save current ACCCON on stack", align=Align.INLINE)
d.comment(0x8288, "Load desired paging mode from escapable (&97)", align=Align.INLINE)
d.comment(0x828A, "Select paging so the buffer store lands correctly", align=Align.INLINE)
d.comment(0x828D, "Read last data byte from RX FIFO (FV+RDA)", align=Align.INLINE)
d.comment(0x8294, "Pull saved ACCCON", align=Align.INLINE)
d.comment(0x8295, "Restore caller's ACCCON", align=Align.INLINE)

# Defensive `CLD` guards. These sit at the head of paths reachable from
# Econet NMI/IRQ context, where the interrupted foreground could have left
# the decimal flag set; each protects a binary ADC/SBC further down the
# path (a page-pointer add, an operation-index subtract, a transfer-size
# add) from corrupting its result under decimal mode.
d.comment(0x8150, "Clear decimal mode before scanning the port slots", align=Align.INLINE)
d.comment(0x835A, "Clear decimal mode: the RXCB-pointer ADC below must be binary", align=Align.INLINE)
d.comment(0x8476, "Clear decimal mode: the operation-index SBC below must be binary", align=Align.INLINE)
d.comment(0x85AF, "Clear decimal mode before the binary transfer-size arithmetic", align=Align.INLINE)


# Structural-alignment fills
# for instructions that align 1:1 and share the same mnemonic + mode.
d.comment(0x851F, "Clear carry for offset addition", align=Align.INLINE)
d.comment(0x864C, "Save X on stack", align=Align.INLINE)
d.comment(0x86BB, "Save interrupt state", align=Align.INLINE)
d.comment(0x86BC, "Disable interrupts for ADLC access", align=Align.INLINE)
d.comment(0x86CA, "INACTIVE not set -- re-enable NMIs and loop", align=Align.INLINE)
# UNMAPPED: d.comment(0x8C0C, "Read cmd_table_fs+X (entry name byte)", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CCF, "Tail-call print_station_id to append ' Econet Station <n>' (and ' No Clock' if appropriate)", align=Align.INLINE)
# UNMAPPED: d.comment(0x90E4, "Print as decimal (no leading zeros)", align=Align.INLINE)
d.comment(0x95BB, "NOP -- bit-7 terminator + resume opcode for the preceding inline string", align=Align.INLINE)
d.comment(0xA218, "Pull operation code", align=Align.INLINE)
d.comment(0xA219, "Shift right: check bit 0 (direction)", align=Align.INLINE)
d.comment(0xA21A, "Push updated code", align=Align.INLINE)
d.comment(0xA21B, "Carry clear: OSBGET (read)", align=Align.INLINE)
d.comment(0xA5F5, "Copy parsed arg to TX buffer with X=0", align=Align.INLINE)
d.comment(0xAF96, "Pop saved TX cmd", align=Align.INLINE)
d.comment(0xAF98, "Non-zero: retry from start_spool_retry", align=Align.INLINE)
d.comment(0xAFB1, "Not 1: take printer_busy_msg path", align=Align.INLINE)
d.comment(0xAFB3, "A=&AB: 'Printer off line' error code", align=Align.INLINE)
d.comment(0xAFB5, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.comment(0xB0A3, "Store at (nfs_workspace)+Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1E4, "Look up option-string offset for index X", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1E7, "Look up option byte at the resolved offset", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1EC, "Print char (no spool)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1FE, "Print 10-char filename", align=Align.INLINE)
# UNMAPPED: d.comment(0xB201, "Print inline 'attr-bits' fragment", align=Align.INLINE)
# UNMAPPED: d.comment(0xB32C, "Print CR (no spool)", align=Align.INLINE)
d.comment(0xB406, "Load PS server address", align=Align.INLINE)
d.comment(0xB4B1, "Print station number and newline", align=Align.INLINE)
d.comment(0xB613, "Print ' \"'", align=Align.INLINE)
d.comment(0xB62C, "Bit-7 terminator from preceding stringhi", align=Align.INLINE)
d.comment(0xB62D, "Load this PS server's address for display", align=Align.INLINE)
d.comment(0xB630, "Set V (always) via always_set_v_byte", align=Align.INLINE)
d.comment(0xB639, "Pop saved slot index", align=Align.INLINE)
d.comment(0xB66B, "Ensure V clear so next BVC always taken", align=Align.INLINE)
d.comment(0xB676, "Status = 2?", align=Align.INLINE)
d.comment(0xB678, "No: check for busy", align=Align.INLINE)
d.comment(0xB67A, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB685, "Clear V", align=Align.INLINE)
d.comment(0xB688, "Status = 1?", align=Align.INLINE)
d.comment(0xB69F, "Not 1 or 2: default to jammed", align=Align.INLINE)

# --- manual coverage-gap annotations ---
d.index_base(0xA771, "boot_cmd_lo_table")
d.index_base(0xBFE6, "hazel_minus_1a")
d.index_base(0xBFE8, "hazel_idx_bases")
# UNMAPPED: d.index_base(0xBFFE, "hazel_minus_2")
# UNMAPPED: d.comment(0xBFFE, "Base for `hazel_minus_2,Y` reads/writes -- `&BFFE + Y` reaches into HAZEL for Y >= 2", align=Align.INLINE)
# UNMAPPED: d.index_base(0xBFFF, "hazel_minus_1")
d.label(0x80EA, "nmi_scout_data")
d.label(0x87FE, "nmi_tx_switch_rx")
d.label(0x8830, "nmi_reply_cont")
d.label(0x88BC, "nmi_data_tx_alt")
d.expr(0x80D6, lo(sym("nmi_scout_data")))
d.expr(0x87FA, lo(sym("nmi_tx_switch_rx")))
d.expr(0x882C, lo(sym("nmi_reply_cont")))
d.expr(0x88A7, lo(sym("nmi_data_tx_alt")))
d.expr(0x80B6, lo(sym("nmi_rx_scout_net")))
d.expr(0x81C1, lo(sym("nmi_data_rx")))
d.expr(0x81D5, lo(sym("nmi_data_rx_net")))
d.expr(0x8322, hi(sym("nmi_ack_tx_src")))
d.expr(0x8889, lo(sym("nmi_scout_ack_src")))
d.expr(0x888B, hi(sym("nmi_scout_ack_src")))
d.expr(0x88AE, lo(sym("nmi_data_tx_tube")))
d.expr(0x88B0, hi(sym("nmi_data_tx_tube")))
d.expr(0x8907, lo(sym("discard_reset_rx")))
d.expr(0x8909, hi(sym("discard_reset_rx")))
d.expr(0x895D, lo(sym("nmi_final_ack")))
d.expr(0x895F, hi(sym("nmi_final_ack")))
d.expr(0x8202, lo(sym("nmi_data_rx_bulk")))
d.expr(0x8204, hi(sym("nmi_data_rx_bulk")))
d.expr(0x820E, lo(sym("nmi_data_rx_tube")))
d.expr(0x8210, hi(sym("nmi_data_rx_tube")))
d.expr(0x8320, lo(sym("nmi_ack_tx_src")))
d.expr(0x83FE, lo(sym("nmi_rx_scout")))
d.expr(0x8400, hi(sym("nmi_rx_scout")))
d.expr(0x8565, hi(sym("tx_done_exit") - 1))
d.expr(0x8568, lo(sym("tx_done_exit") - 1))
d.expr(0x871F, lo(sym("nmi_tx_data")))
d.expr(0x883B, lo(sym("nmi_reply_validate")))
d.expr(0x8973, lo(sym("nmi_final_ack_net")))
d.expr(0x9C1A, lo(sym("hazel_parse_buf")))
d.expr(0x9C1E, hi(sym("hazel_parse_buf")))
d.expr(0xA72C, lo(sym("findlib_oscli_cmd")))
d.expr(0xA72E, hi(sym("findlib_oscli_cmd")))
d.expr(0x8816, lo(sym("nmi_reply_scout")))
d.expr(0x8818, hi(sym("nmi_reply_scout")))
d.subroutine(0x8A1F, "nmi_return_inton", title="NMI exit: re-enable NMIs and return", description="""Two-instruction NMI tail: `BIT enable_net_nmis` (INTON, guaranteeing a fresh /NMI edge if the ADLC IRQ is still asserted) then `RTI`.""")
d.label(0x84DC, "imm_reply_flag")
d.label(0x86BB, "tx_irq_off")
d.label(0x872D, "tx_enable_nmis")
d.label(0xA5F5, "run_copy_arg_to_buf")
d.label(0xAF96, "spool_pop_cmd")
d.label(0xAFAF, "check_err_code_5")
d.label(0xAFC9, "err_printer_jammed")
d.label(0xB32E, "print_col_cr")
d.label(0xB4B1, "ps_print_info_newline")
d.label(0xBFE8, "skip_fn_space_cont")
d.label(0x86DD, "set_line_jammed")
d.label(0x851D, "imm_op_build_reply")
d.label(0x9FAD, "argsv_clamp_zero")
d.label(0x9FB1, "argsv_send_request")
d.label(0x9FB8, "argsv_store_result")
d.label(0xB1E9, "loop_print_option")
d.label(0xB639, "loop_next_poll_slot")
d.label(0xB66E, "poll_test_status")
d.label(0xB67A, "poll_print_offline")
d.label(0xB688, "poll_check_busy")
d.label(0xB68C, "poll_print_jammed")
d.label(0xB696, "poll_entry_done")
d.label(0xB699, "poll_mark_slot")
d.label(0xB6A2, "poll_print_busy")
d.label(0xB62D, "poll_load_server")
d.index_base(0x8A25, "svc_dispatch_lo")
d.banner(0x8A25, title="svc_dispatch low-byte table (51 entries)",
    description="""Low-byte half of the `PHA`/`PHA`/`RTS` dispatch table read by
[`svc_dispatch`](label:svc_dispatch) as `LDA &8A23,X`. Paired with the high-byte
half at [`svc_dispatch_hi`](label:svc_dispatch_hi). Index 0 is an unused placeholder;
indices 1..50 cover service handlers, language replies, FSCV reasons, FS
replies and net-handle / OSWORD &13 trampolines. Per-entry inline comments
give each slot's dispatch.""")
d.index_base(0x8A58, "svc_dispatch_hi")
# UNMAPPED: d.banner(0x8A56, title="svc_dispatch high-byte table (51 entries + 1 padding)",
# UNMAPPED:     description="""High-byte half of the `PHA`/`PHA`/`RTS` dispatch table read as
# UNMAPPED: `LDA &8A56,X`. The dispatcher pushes the high byte first then the low, so
# UNMAPPED: `RTS` lands on target (each stored value is handler-1).""")
d.index_base(0xA9CA, "osword_13_dispatch_lo")
# UNMAPPED: d.banner(0xA9C8, title="OSWORD &13 dispatch low-byte table (18 entries)",
# UNMAPPED:     description="""Low-byte half of the OSWORD &13 sub-reason `PHA`/`PHA`/`RTS`
# UNMAPPED: dispatch, read as `LDA &A9C8,X`; paired with
# UNMAPPED: [`osword_13_dispatch_hi`](label:osword_13_dispatch_hi).""")
d.index_base(0xAD42, "netv_dispatch_lo")
# UNMAPPED: d.banner(0xAD40, title="NETV reason-code dispatch low-byte table (9 entries)",
# UNMAPPED:     description="""Low-byte half of the NETV reason-code `PHA`/`PHA`/`RTS`
# UNMAPPED: dispatch, read as `LDA &AD40,X`; paired with
# UNMAPPED: [`netv_dispatch_hi`](label:netv_dispatch_hi).""")
d.comment(0xB10E, "Index 5: threshold 39", align=Align.INLINE)
d.comment(0xB10F, "Index 6: threshold 49", align=Align.INLINE)
d.comment(0xB112, "Index 9: threshold 79", align=Align.INLINE)
d.comment(0xB116, "Index 13: threshold 118", align=Align.INLINE)
d.comment(0xB117, "Index 14: threshold 128", align=Align.INLINE)
d.comment(0xB11A, "Index 17: threshold 157", align=Align.INLINE)
d.comment(0xB11D, "Index 20: threshold 187", align=Align.INLINE)
d.comment(0xB11F, "Index 22: threshold 207", align=Align.INLINE)
d.comment(0xADE8, "OSWORD &9A", align=Align.INLINE)
d.comment(0xADEB, "OSWORD &E2", align=Align.INLINE)
d.comment(0xADEE, "OSWORD &0B", align=Align.INLINE)
d.comment(0xADF2, "OSWORD &7A", align=Align.INLINE)
d.comment(0xADF3, "OSWORD &86", align=Align.INLINE)
d.comment(0x9AA6, "BRK error code &A0 (first table entry)", align=Align.INLINE)
d.comment(0x9AC7, "BRK error code &A3", align=Align.INLINE)
d.comment(0x9AE5, "BRK error code &A5", align=Align.INLINE)
d.label(
    0x0D36,
    "mc_reply_status",
    description="MachinePeek (&88) reply staging byte ([`scout_buf`](label:scout_buf)+8); receives spool_control_flag.",
    length=1,
    group="ram_workspace",
    access="rw",
)
d.index_base(
    0x0D37,
    "mc_reply_machine_id",
    description="3-byte machine identity for the MachinePeek (&88) reply ([`scout_buf`](label:scout_buf)+9); copied from machine_id_bytes.",
    length=3,
    group="ram_workspace",
)
d.entry(0x84F2)
d.subroutine(
    0x84F2,
    "rx_imm_machine_type",
    title="RX immediate: machine-type (MachinePeek) reply",
    description="""Builds the fixed machine-identity reply for a MachinePeek
immediate operation (control byte `&88`). Copies the 3 identity
bytes at [`machine_id_bytes`](label:machine_id_bytes) into
[`mc_reply_machine_id`](label:mc_reply_machine_id), copies
[`spool_control_flag`](label:spool_control_flag) to
[`mc_reply_status`](label:mc_reply_status), points the reply buffer via
[`open_port_buf`](label:open_port_buf) and sets its length, then branches to
[`set_tx_reply_flag`](label:set_tx_reply_flag) to send it. Serviced
inline (like PEEK/POKE), not deferred.

Reached only via the immediate-op dispatch table
([`imm_op_dispatch_lo`](label:imm_op_dispatch_lo)) for control
byte `&88`.""",
)
d.comment(0x84F2, "Reply length hi = &01", align=Align.INLINE)
d.comment(0x84F4, "Set port_buf_len_hi", align=Align.INLINE)
d.comment(0x84F6, "Reply length lo = &FC", align=Align.INLINE)
d.comment(0x84F8, "Set port_buf_len", align=Align.INLINE)
d.comment(0x84FA, "Y=2: copy 3 identity bytes (2 down to 0)", align=Align.INLINE)
d.label(0x84FC, "copy_machine_id_loop")
d.comment(0x84FC, "Read machine-identity byte from ROM", align=Align.INLINE)
d.comment(0x84FF, "Store into mc_reply_machine_id", align=Align.INLINE)
d.comment(0x8502, "Next byte (descending)", align=Align.INLINE)
d.comment(0x8503, "Loop until all 3 copied", align=Align.INLINE)
d.comment(0x8505, "Load station/config byte from &0D71", align=Align.INLINE)
d.comment(0x8508, "Store into mc_reply_status", align=Align.INLINE)
d.comment(0x850B, "Reply buffer lo = &3A", align=Align.INLINE)
d.comment(0x850D, "Set open_port_buf", align=Align.INLINE)
d.comment(0x850F, "Reply buffer hi = &0C", align=Align.INLINE)
d.comment(0x8511, "Set open_port_buf_hi", align=Align.INLINE)
d.comment(0x8513, "Always taken: join common reply-send path", align=Align.INLINE)
d.index_base(0x8027, "machine_id_bytes", description="3-byte machine identity returned by the MachinePeek (&88) immediate op; copied to &0D37 by rx_imm_machine_type.")
# UNMAPPED: d.comment(0xA80E, "&80 sub-table separator; the &8E44 word is the FS-command sub-table default handler (&8E45-1); the following &4F &6E &80 &00 &00 (ASCII 'On' + markers) is a 5-byte record new in this build", align=Align.INLINE)
d.comment(0x8397, "Unreached &D8 (CLD) byte after the RTS", align=Align.INLINE)
d.comment(0x8A23, "Padding before the service-dispatch low-byte table", align=Align.INLINE)
d.comment(0xADE5, "Range 1+2: OSWORD &0A", align=Align.INLINE)
# UNMAPPED: d.comment(0xB03B, "buf start lo", align=Align.INLINE)
d.comment(0x9200, "Syntax-table offset entry (into syn_opt_dir)", align=Align.INLINE)
d.comment(0xABFD, "TX init data byte &9C", align=Align.INLINE)
# UNMAPPED: d.comment(0xA837, "NoSpace dispatch target (&9621)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA83F, "Space dispatch target (&9617)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA852, "Space dispatch target (&9640)", align=Align.INLINE)
d.comment(0x8003, "Service-call entry: jump to service_handler", align=Align.INLINE)
d.comment(0x8442, "Copy saved ACCCON to X", align=Align.INLINE)
d.comment(0x8458, "Index reached end: restore X and finish", align=Align.INLINE)
d.comment(0x852D, "Advance buffer index", align=Align.INLINE)
d.comment(0x859C, "Zero: transfer done, exit", align=Align.INLINE)
d.comment(0x85BF, "Next byte (descending)", align=Align.INLINE)
d.comment(0x8655, "Advance to destination network byte", align=Align.INLINE)
d.comment(0x86BD, "A=&40: 'line inactive' status code", align=Align.INLINE)
d.comment(0x86BF, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x86CF, "N set: line still driven, report jammed", align=Align.INLINE)
d.comment(0x86DD, "A=&2C: 'line jammed' status code", align=Align.INLINE)
d.comment(0x86DF, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x86F6, "Zero: report line jammed", align=Align.INLINE)
d.comment(0x86FA, "Branch to store TX error", align=Align.INLINE)
d.comment(0x872B, "A=&2C: 'line jammed' status code", align=Align.INLINE)
d.comment(0x872D, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x8755, "Non-zero: store control byte and add", align=Align.INLINE)
d.comment(0x8792, "C set: control byte out of range, exit", align=Align.INLINE)
d.comment(0x87E0, "Branch to store TX error", align=Align.INLINE)
d.comment(0x8817, "Install nmi_reply_scout (high)", align=Align.INLINE)
d.comment(0x89EA, "Compare to &80 (line-idle threshold)", align=Align.INLINE)
d.comment(0x89EE, "A=&40: 'line inactive' status code", align=Align.INLINE)
d.comment(0x89F0, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x89F6, "A=0", align=Align.INLINE)
d.comment(0x8A9C, "Store the spool-control flag", align=Align.INLINE)
d.comment(0x8AA1, "C set: not ours, restore ROM slot and return", align=Align.INLINE)
d.comment(0x8BEA, "Zero args: print the command table", align=Align.INLINE)
d.comment(0x8BF8, "V clear: walk the next table entry", align=Align.INLINE)
d.comment(0x8BFA, "Print newline", align=Align.INLINE)
d.comment(0x8BFD, "Save Y", align=Align.INLINE)
d.comment(0x8C11, "Print character", align=Align.INLINE)
d.comment(0x8C1D, "Print character", align=Align.INLINE)
d.comment(0x8C3D, "Print character", align=Align.INLINE)
d.comment(0x8C43, "Print newline", align=Align.INLINE)
d.comment(0x8C5A, "Print newline", align=Align.INLINE)
d.comment(0x8C61, "Print character", align=Align.INLINE)
d.comment(0x8CB8, "Loop back for the next character", align=Align.INLINE)
d.comment(0x8D07, "Print the station identity line", align=Align.INLINE)
d.comment(0x8D0A, "Print newline", align=Align.INLINE)
d.comment(0x8D15, "A=4: library-selected flag bit", align=Align.INLINE)
d.comment(0x8D17, "Set the library-selected flag", align=Align.INLINE)
d.comment(0x8D9F, "bit-7 terminator + resume opcode", align=Align.INLINE)
d.comment(0x8DA9, "Save X", align=Align.INLINE)
d.comment(0x8DAA, "Save Y", align=Align.INLINE)
d.comment(0x8E0C, "Read a character (password entry, no echo)", align=Align.INLINE)
d.comment(0x8E0F, "Ctrl-U (&15): line-delete?", align=Align.INLINE)
d.comment(0x8E39, "Branch to send the command", align=Align.INLINE)
d.comment(0x8E63, "Not matched: fall to service dispatch", align=Align.INLINE)
d.comment(0x8E73, "Not matched: fall to service dispatch", align=Align.INLINE)
d.comment(0x8EF0, "Zero: tail-call OSBYTE", align=Align.INLINE)
d.comment(0x8F64, "Test the FS flags", align=Align.INLINE)
d.comment(0x8F6F, "Y=&21: workspace flag offset", align=Align.INLINE)
d.comment(0x8F71, "Clear the workspace flag at &21", align=Align.INLINE)
d.comment(0x901D, "Merge into the FS flags", align=Align.INLINE)
d.comment(0x903E, "Toggle the workspace flag at &21", align=Align.INLINE)
d.comment(0x9094, "Positive: store the workspace byte", align=Align.INLINE)
d.comment(0x90FD, "Print newline", align=Align.INLINE)
d.comment(0x9254, "Tail-call OSASCI to print the nybble", align=Align.INLINE)
d.comment(0x9422, "Mask the FCB status flags", align=Align.INLINE)
d.comment(0x948C, "Copy A to X", align=Align.INLINE)
d.comment(0x95B6, "Print inline string", align=Align.INLINE)
d.comment(0x95BC, "Print the 'Space' free-space label", align=Align.INLINE)
d.comment(0x9657, "Branch to the shared CMOS-print return", align=Align.INLINE)
d.comment(0x9659, "Print inline string", align=Align.INLINE)
d.comment(0x9662, "bit-7 terminator + resume opcode", align=Align.INLINE)
d.comment(0x9663, "Return", align=Align.INLINE)
d.comment(0x967F, "Print newline", align=Align.INLINE)
d.comment(0x9771, "C set: copy TXCB with carry set", align=Align.INLINE)
d.comment(0x9774, "V clear: copy TXCB with carry clear", align=Align.INLINE)
d.comment(0x9864, "Advance index", align=Align.INLINE)
d.comment(0x99BE, "Branch to write the error number and string", align=Align.INLINE)
d.comment(0x9EA1, "Advance index", align=Align.INLINE)
d.comment(0xA44E, "Advance index", align=Align.INLINE)
d.comment(0xA480, "XOR against the stored command character", align=Align.INLINE)
d.comment(0xA4B2, "Rotate result bit into carry", align=Align.INLINE)
d.comment(0xA4B3, "Decrement match counter", align=Align.INLINE)
d.comment(0xA505, "Branch to load the *RUN mask", align=Align.INLINE)
d.comment(0xA561, "Rotate mask bit into carry", align=Align.INLINE)
d.comment(0xA5A3, "No match: retry via the library directory", align=Align.INLINE)
d.comment(0xA636, "Mask the OSWORD flag byte", align=Align.INLINE)
d.comment(0xA651, "Return with the last-byte flag", align=Align.INLINE)
d.comment(0xA657, "Return with the last-byte flag", align=Align.INLINE)
d.comment(0xA683, "Match: store station flags and restore", align=Align.INLINE)
d.comment(0xA6AE, "Match: store station flags and restore", align=Align.INLINE)
d.comment(0xA72B, "-NET-FindLib command pointer (low)", align=Align.INLINE)
d.comment(0xA72D, "-NET-FindLib command pointer (high)", align=Align.INLINE)
d.comment(0xA753, "Copy X to A", align=Align.INLINE)
d.comment(0xA99A, "Branch to OSWORD-11 done", align=Align.INLINE)
d.comment(0xAA3A, "Copy A to Y", align=Align.INLINE)
d.comment(0xAA51, "Copy Y to A", align=Align.INLINE)
d.comment(0xAA54, "Copy A to Y", align=Align.INLINE)
d.comment(0xAB09, "Copy A to X", align=Align.INLINE)
d.comment(0xAB9B, "Advance index", align=Align.INLINE)
d.comment(0xABD7, "Copy Y to A", align=Align.INLINE)
d.comment(0xABDA, "Advance index", align=Align.INLINE)
d.comment(0xABDB, "Branch to store the bridge station", align=Align.INLINE)
d.comment(0xACA5, "Advance index", align=Align.INLINE)
d.comment(0xACA6, "Advance index", align=Align.INLINE)
d.comment(0xACBE, "Advance index", align=Align.INLINE)
d.comment(0xACDF, "Advance index", align=Align.INLINE)
d.comment(0xAEE3, "Advance index", align=Align.INLINE)
d.comment(0xAF7C, "Copy A to X", align=Align.INLINE)
d.comment(0xAF7D, "Mask the low 3 bits", align=Align.INLINE)
d.comment(0xAF97, "Decrement", align=Align.INLINE)
d.comment(0xAF9A, "Decrement counter", align=Align.INLINE)
d.comment(0xAFAF, "Error code = 5?", align=Align.INLINE)
d.comment(0xB0A0, "Copy A to X", align=Align.INLINE)
d.comment(0xB0E4, "Branch when the *CDIR size is complete", align=Align.INLINE)
d.comment(0xB12B, "C set: set the library flag", align=Align.INLINE)
d.comment(0xB131, "C set: set the library flag", align=Align.INLINE)
d.comment(0xB14B, "Branch to set up the *EX request", align=Align.INLINE)
d.comment(0xB194, "Print a 3-digit decimal (no spool)", align=Align.INLINE)
d.comment(0xB25C, "Tail-call print_newline_no_spool", align=Align.INLINE)
d.comment(0xB334, "XOR with zp_0078", align=Align.INLINE)
d.comment(0xB336, "Add zp_0063", align=Align.INLINE)
d.comment(0xB386, "Print the digit", align=Align.INLINE)
d.comment(0xB3BE, "Loop to the next character", align=Align.INLINE)
d.comment(0xB3F2, "Y=&21: workspace flag offset", align=Align.INLINE)
d.comment(0xB3F4, "A=0", align=Align.INLINE)
d.comment(0xB3F6, "Clear the workspace flag at &21", align=Align.INLINE)
d.comment(0xB45F, "Copy A to X", align=Align.INLINE)
d.comment(0xB476, "Mask the low 3 bits", align=Align.INLINE)
d.comment(0xB48E, "Loop to pop the next PS slot", align=Align.INLINE)
d.comment(0xB4A3, "V clear: branch onward", align=Align.INLINE)
d.comment(0xB4AC, "Y=&21: workspace flag offset", align=Align.INLINE)
d.comment(0xB4AE, "Copy Y to A", align=Align.INLINE)
d.comment(0xB4AF, "Store the workspace flag at &21", align=Align.INLINE)
d.comment(0xB4BA, "Advance index", align=Align.INLINE)
d.comment(0xB6FF, "Branch to the unprotect-clear path", align=Align.INLINE)
d.comment(0xB7F4, "Branch to set the wipe CR-end", align=Align.INLINE)
d.comment(0xBD5F, "Print newline", align=Align.INLINE)
d.comment(0xB60D, "Y=&21: PS-entry flag offset in workspace", align=Align.INLINE)
d.comment(0xB60F, "Load PS-entry flag", align=Align.INLINE)
d.comment(0xB611, "Zero: slot empty, skip display", align=Align.INLINE)
d.comment(0xB61F, "Print character of PS name", align=Align.INLINE)
# UNMAPPED: d.comment(0xB62B, "Load this PS server's address for display", align=Align.INLINE)
# UNMAPPED: d.comment(0xB62E, "Set V (always) via always_set_v_byte", align=Align.INLINE)
d.comment(0xB633, "Print the server station address", align=Align.INLINE)
d.comment(0xB636, "Print newline", align=Align.INLINE)
d.comment(0xB66C, "Status ready printed: branch to end-of-entry (always)", align=Align.INLINE)
d.comment(0xB66E, "Shift status byte left to test its flag bits...", align=Align.INLINE)
d.comment(0xB66F, "...", align=Align.INLINE)
d.comment(0xB670, "...", align=Align.INLINE)
d.comment(0xB671, "...(4 shifts move bits 4-7 into C/N)", align=Align.INLINE)
d.comment(0xB672, "C set: status jammed", align=Align.INLINE)
d.comment(0xB674, "N set: status off line", align=Align.INLINE)
d.comment(0xB686, "Off-line printed: branch to end-of-entry (always)", align=Align.INLINE)
d.comment(0xB68A, "Status = 1: print at cb6a0", align=Align.INLINE)
d.comment(0xB68C, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB695, "bit-7 terminator + resume opcode", align=Align.INLINE)
d.comment(0xB696, "Print newline after the status line", align=Align.INLINE)
d.comment(0xB699, "Pull saved slot index", align=Align.INLINE)
d.comment(0xB69A, "Y = slot index", align=Align.INLINE)
d.comment(0xB69B, "&3F: 'slot processed' marker", align=Align.INLINE)
d.comment(0xB69D, "Store the &3F marker in the workspace slot", align=Align.INLINE)
d.comment(0xB6A1, "Return", align=Align.INLINE)
d.comment(0xB6CE, "Clear V for the unconditional branch", align=Align.INLINE)
d.comment(0xB6CF, "Branch to end-of-entry (always)", align=Align.INLINE)
d.comment(0x87AB, "Unwind first stacked byte", align=Align.INLINE)
d.comment(0x87AC, "Unwind second stacked byte", align=Align.INLINE)
d.comment(0x87AD, "Unwind third stacked byte", align=Align.INLINE)
d.comment(0x8B1A, "Copy A to X", align=Align.INLINE)
d.comment(0x8B1D, "Copy A to Y", align=Align.INLINE)
d.comment(0x8BF5, "Restore Y", align=Align.INLINE)
d.comment(0x8BF6, "Restore X", align=Align.INLINE)
d.comment(0x8C67, "Restore Y", align=Align.INLINE)
d.comment(0x8CF3, "Copy X to A", align=Align.INLINE)
d.comment(0x8CFE, "Copy A to Y", align=Align.INLINE)
d.comment(0x8DBD, "Restore Y", align=Align.INLINE)
d.comment(0x8DBE, "Restore X", align=Align.INLINE)
d.comment(0x8DC3, "Restore Y", align=Align.INLINE)
d.comment(0x8E35, "Restore X", align=Align.INLINE)
d.comment(0x90A9, "Save Y", align=Align.INLINE)
d.comment(0x90BA, "Restore Y", align=Align.INLINE)
d.comment(0x942F, "Save X", align=Align.INLINE)
d.comment(0x9436, "Restore X", align=Align.INLINE)
d.comment(0x9488, "Restore Y", align=Align.INLINE)
d.comment(0x94CF, "Save X", align=Align.INLINE)
d.comment(0x94D9, "Restore X", align=Align.INLINE)
d.comment(0x982E, "Unwind stacked byte", align=Align.INLINE)
d.comment(0x982F, "Unwind stacked byte", align=Align.INLINE)
d.comment(0x9A0D, "Save Y", align=Align.INLINE)
d.comment(0x9A13, "Restore Y", align=Align.INLINE)
d.comment(0xA107, "Save Y", align=Align.INLINE)
d.comment(0xA113, "Restore Y", align=Align.INLINE)
d.comment(0xA123, "Copy A to Y", align=Align.INLINE)
d.comment(0xA19B, "Restore Y", align=Align.INLINE)
d.comment(0xB3F1, "Save Y", align=Align.INLINE)
d.comment(0xB3F8, "Restore Y", align=Align.INLINE)
d.comment(0xB405, "Save Y", align=Align.INLINE)
d.comment(0xB409, "Restore Y", align=Align.INLINE)
d.comment(0xBB89, "Restore Y", align=Align.INLINE)
d.comment(0xBB97, "Restore Y", align=Align.INLINE)
d.comment(0xBB98, "Restore X", align=Align.INLINE)
d.comment(0xBCA8, "Save Y", align=Align.INLINE)
d.comment(0xBCBE, "Restore Y", align=Align.INLINE)
d.comment(0xBCEA, "Restore Y", align=Align.INLINE)
d.comment(0xBCEB, "Restore X", align=Align.INLINE)
d.comment(0x9EF1, "Save X (channel index) across the OSARGS body", align=Align.INLINE)
d.comment(0x9F01, "Restore X", align=Align.INLINE)
d.comment(0x9F87, "Load channel handle from fs_block_offset", align=Align.INLINE)
d.comment(0x9F89, "Convert handle to FCB channel index in X", align=Align.INLINE)
d.comment(0x9F8C, "Test high transfer-size byte first", align=Align.INLINE)
d.comment(0x9F8F, "Non-zero: pointer below extent, send request", align=Align.INLINE)
d.comment(0x9F91, "Compare FCB pointer high byte...", align=Align.INLINE)
d.comment(0x9F94, "...against extent high byte", align=Align.INLINE)
d.comment(0x9F97, "Pointer < extent: send request", align=Align.INLINE)
d.comment(0x9F99, "Pointer > extent: clamp path", align=Align.INLINE)
d.comment(0x9F9B, "Compare FCB pointer mid byte...", align=Align.INLINE)
d.comment(0x9F9E, "...against extent mid byte", align=Align.INLINE)
d.comment(0x9FA1, "Pointer < extent: send request", align=Align.INLINE)
d.comment(0x9FA3, "Pointer > extent: clamp path", align=Align.INLINE)
d.comment(0x9FA5, "Compare FCB pointer low byte...", align=Align.INLINE)
d.comment(0x9FA8, "...against extent low byte", align=Align.INLINE)
d.comment(0x9FAB, "Pointer < extent: send request", align=Align.INLINE)
d.comment(0x9FAD, "X=0: pointer at/beyond extent", align=Align.INLINE)
d.comment(0x9FAF, "Branch to store result (always)", align=Align.INLINE)
d.comment(0xA204, "Save X (channel index)", align=Align.INLINE)
d.comment(0xA217, "Restore Y (channel index)", align=Align.INLINE)
d.comment(0xA21D, "Copy FCB pointer low byte...", align=Align.INLINE)
d.comment(0xA220, "...into TX control block size low", align=Align.INLINE)
d.comment(0xA223, "Copy FCB pointer mid byte...", align=Align.INLINE)
d.comment(0xA226, "...into TX control block size mid", align=Align.INLINE)
d.comment(0xA229, "Copy FCB pointer high byte...", align=Align.INLINE)
d.comment(0xA22C, "...into TX control block size high", align=Align.INLINE)
import sys

# --- character-literal immediate operands ---
d.char_literal(0x8C1C)
d.char_literal(0x8C60)
d.char_literal(0x8C92)
d.char_literal(0x8DFD)
d.char_literal(0x8E4C)
d.char_literal(0x90EA)
d.char_literal(0x921C)
d.char_literal(0x9220)
d.char_literal(0x9253)
d.char_literal(0x9269)
d.char_literal(0x92C2)
d.char_literal(0x92CE)
d.char_literal(0x92D2)
d.char_literal(0x92D6)
d.char_literal(0x92DA)
d.char_literal(0x92FE)
d.char_literal(0x9302)
d.char_literal(0x9343)
d.char_literal(0x93A2)
d.char_literal(0x93A6)
d.char_literal(0x93AA)
d.char_literal(0x93AE)
d.char_literal(0x9451)
d.char_literal(0x9481)
d.char_literal(0x9493)
d.char_literal(0x949A)
d.char_literal(0x94A7)
d.char_literal(0x94B1)
d.char_literal(0x94F2)
d.char_literal(0x9501)
d.char_literal(0x951C)
d.char_literal(0x9527)
d.char_literal(0x9533)
d.char_literal(0x9542)
d.char_literal(0x9933)
d.char_literal(0x9937)
d.char_literal(0x99BB)
d.char_literal(0x9A3B)
d.char_literal(0x9A4E)
d.char_literal(0x9A60)
d.char_literal(0x9A8C)
# UNMAPPED: d.char_literal(0x9D59)
d.char_literal(0x9E8C)
d.char_literal(0x9E96)
d.char_literal(0x9EBF)
d.char_literal(0x9EC6)
d.char_literal(0xA423)
d.char_literal(0xA43E)
d.char_literal(0xA493)
d.char_literal(0xA4BB)
d.char_literal(0xA4E1)
d.char_literal(0xA4E5)
d.char_literal(0xA4EC)
d.char_literal(0xA608)
d.char_literal(0xA96C)
d.char_literal(0xA995)
d.char_literal(0xB268)
d.char_literal(0xB27B)
d.char_literal(0xB29C)
d.char_literal(0xB2AB)
d.char_literal(0xB2B9)
d.char_literal(0xB2BD)
d.char_literal(0xB2E1)
d.char_literal(0xB2E3)
d.char_literal(0xB2E7)
d.char_literal(0xB2F2)
d.char_literal(0xB381)
d.char_literal(0xB390)
d.char_literal(0xB395)
d.char_literal(0xB3B7)
d.char_literal(0xB3C4)
d.char_literal(0xB42A)
d.char_literal(0xB48B)
d.char_literal(0xB510)
d.char_literal(0xB59C)
d.char_literal(0xB5D9)
d.char_literal(0xB61C)
d.char_literal(0xB69C)
d.char_literal(0xB6ED)
d.char_literal(0xB6F1)
d.char_literal(0xB765)
d.char_literal(0xB76E)
d.char_literal(0xB794)
d.char_literal(0xB7B5)
d.char_literal(0xB7CC)
d.char_literal(0xB7CE)
d.char_literal(0xB7F1)
d.char_literal(0xB840)
d.char_literal(0xB844)
d.char_literal(0xBE11)
d.char_literal(0xBE15)
d.char_literal(0xBE6E)
d.char_literal(0xBE8A)
d.char_literal(0xBE8E)
d.char_literal(0xBE92)
d.char_literal(0xBED8)
d.char_literal(0xBFE0)
d.char_literal(0xBFE7)


# Semantic names for auto-labelled data-table indexing bases (see 4.24).
d.label(0x872F, "tx_ctrl_dispatch_lo")
d.label(0x8DC1, "ps_template_base")
d.label(0xA127, "cmos_attr_table")
d.label(0xABE7, "bridge_err_table")
d.label(0xB53A, "ps_print_template")
d.index_base(0x8A20, "os_spool_flag_table")
d.label(0x0D1C, "net_poll_status")
d.index_base(0xA88C, "osword_pb_ready")
d.label(0xA893, "osword_subcode_dispatch")
# Anchors for the two bases inside instruction operand bytes.
d.label(0x85C2, "tx_calc_tube_check")
d.label(0x8492, "tube_overflow_restore_acccon")


# --- 4.26 delta: reworked OSWORD &0E (=OSWORD 14) real-time-clock routine
# --- and the new OSARGS filing-system-check helper (&BFF7). Reached via
# --- PHA/PHA/RTS dispatch, so declared as explicit code entries. Meaning
# --- of the changes cross-checked against J.G. Harston's "ANFS 4.26 updated
# --- OSWORD 14 RTC routine".
d.entry(0xA89A)
d.subroutine(
    0xA89A,
    "osword_0e_dispatch",
    title="OSWORD &0E (14): real-time-clock request dispatch",
    description="""Entry for the OSWORD &0E clock request. First calls
[`fs_num_via_osargs`](label:fs_num_via_osargs) and only proceeds if NetFS is the
current filing system, so the request is left for other filing systems to
service otherwise. Then dispatches on the OSWORD sub-code (in X) to the
save-and-convert or write-back path.""",
)
d.comment(0xA89A, "Only act if NetFS is the current FS", align=Align.INLINE)
d.comment(0xA89D, "Not NetFS: leave for other filing systems", align=Align.INLINE)
d.comment(0xA89F, "A = OSWORD sub-code (relayed into X by fs_num_via_osargs)", align=Align.INLINE)
d.comment(0xA8A0, "Sub-code 0: write-back path", align=Align.INLINE)
d.comment(0xA8A2, "Sub-code 1?", align=Align.INLINE)
d.comment(0xA8A3, "Yes: save-and-convert path", align=Align.INLINE)
d.comment(0xA8A5, "Sub-code 3?", align=Align.INLINE)
d.comment(0xA8A7, "Yes: write-back path", align=Align.INLINE)
d.comment(0xA8A9, "Sub-code 4?", align=Align.INLINE)
d.comment(0xA8AA, "Yes: save-and-convert path", align=Align.INLINE)
d.label(0xA8AC, "osword_0e_unclaimed")
d.comment(0xA8AC, "A=8: service state = unclaimed", align=Align.INLINE)
d.comment(0xA8AE, "Store service state", align=Align.INLINE)
d.comment(0xA8B0, "Return", align=Align.INLINE)

d.entry(0xA8B1)
d.subroutine(
    0xA8B1,
    "save_txcb_and_convert",
    title="OSWORD &0E: save TXCB and format the real-time clock reply",
    description="""Saves the current TX control block, reads the clock/date fields
returned in the HAZEL TXCB workspace, converts each to packed BCD via
[`bin_to_bcd`](label:bin_to_bcd), forms the year (7-bit field plus base &51),
adjusting into the 20xx century when it reaches 100, and writes the formatted
result to the OSWORD reply buffer at (`ws_ptr_hi`),Y. Reworked in 4.26.""",
)
d.comment(0xA8B1, "Save Y (reply buffer offset)", align=Align.INLINE)
d.comment(0xA8B2, "Y=&10: length of TXCB to save", align=Align.INLINE)
d.comment(0xA8B4, "Save current TX control block", align=Align.INLINE)
d.comment(0xA8B7, "Restore Y (reply buffer offset)", align=Align.INLINE)
d.comment(0xA8B8, "X=3: convert 3 clock bytes (secs/mins/hours)", align=Align.INLINE)
d.label(0xA8BA, "loop_convert_clock")
d.comment(0xA8BA, "Save loop counter", align=Align.INLINE)
d.comment(0xA8BB, "Load clock byte X from HAZEL TXCB flags", align=Align.INLINE)
d.comment(0xA8BE, "Convert binary to BCD", align=Align.INLINE)
d.comment(0xA8C1, "Restore loop counter", align=Align.INLINE)
d.comment(0xA8C2, "Stack the BCD result", align=Align.INLINE)
d.comment(0xA8C3, "Next clock byte", align=Align.INLINE)
d.comment(0xA8C4, "Loop for all 3 clock bytes", align=Align.INLINE)
d.comment(0xA8C6, "Save X across the day/month conversion", align=Align.INLINE)
d.comment(0xA8C7, "Load day+month packed byte", align=Align.INLINE)
d.comment(0xA8CA, "Mask low 5 bits: day-of-month", align=Align.INLINE)
d.comment(0xA8CC, "Convert day to BCD", align=Align.INLINE)
d.comment(0xA8CF, "Stack BCD day", align=Align.INLINE)
d.comment(0xA8D0, "Reload the month/flags byte", align=Align.INLINE)
d.comment(0xA8D3, "Save it across the shift", align=Align.INLINE)
d.comment(0xA8D4, "Shift high nibble (month) down to low nibble", align=Align.INLINE)
d.comment(0xA8D8, "Store the shifted month back", align=Align.INLINE)
d.comment(0xA8DB, "Recover the original byte", align=Align.INLINE)
d.comment(0xA8DC, "Mask low nibble", align=Align.INLINE)
d.comment(0xA8DE, "Convert to BCD", align=Align.INLINE)
d.comment(0xA8E1, "Stack the result", align=Align.INLINE)
d.comment(0xA8E2, "Reload day+month byte", align=Align.INLINE)
d.comment(0xA8E5, "Isolate the high year bits", align=Align.INLINE)
d.comment(0xA8E7, "Shift into position", align=Align.INLINE)
d.comment(0xA8E8, "Combine with the low year bits", align=Align.INLINE)
d.comment(0xA8EB, "Add year base (&51); range 81..208", align=Align.INLINE)
d.comment(0xA8ED, "Year >= 100 (i.e. 2000+)?", align=Align.INLINE)
d.comment(0xA8EF, "No: 19xx, use the year as-is", align=Align.INLINE)
d.comment(0xA8F1, "Yes: subtract 100 for the 20xx century", align=Align.INLINE)
d.label(0xA8F3, "year_century_done")
d.comment(0xA8F3, "Save carry (century flag) across the BCD convert", align=Align.INLINE)
d.comment(0xA8F4, "Convert year to BCD", align=Align.INLINE)
d.comment(0xA8F7, "Restore carry", align=Align.INLINE)
d.comment(0xA8F8, "Stack the BCD year", align=Align.INLINE)
d.comment(0xA8F9, "X=&F9: 7 stacked bytes to unwind (wraps to 0)", align=Align.INLINE)
d.label(0xA8FB, "loop_store_reply")
d.comment(0xA8FB, "Pull next converted byte", align=Align.INLINE)
d.comment(0xA8FC, "Store into the OSWORD reply buffer", align=Align.INLINE)
d.comment(0xA8FE, "Advance reply offset", align=Align.INLINE)
d.comment(0xA8FF, "Count stacked bytes", align=Align.INLINE)
d.comment(0xA900, "Loop until all stacked bytes stored", align=Align.INLINE)
d.comment(0xA902, "Return", align=Align.INLINE)

d.entry(0xA903)
d.subroutine(
    0xA903,
    "save_txcb_done",
    title="OSWORD &0E: read the CMOS clock and finish the reply",
    description="""Builds the BCD reply via [`save_txcb_and_convert`](label:save_txcb_and_convert),
then reads the Master 128 CMOS real-time clock with OSWORD
`osword_read_cmos_clock`. On failure it writes a default century of "20" into
the reply. Note: the year conversion adjusts 20xx correctly but does not
convert 2100-2107 to 21xx.""",
)
d.comment(0xA903, "Advance reply offset", align=Align.INLINE)
d.comment(0xA904, "Build the BCD clock/date reply", align=Align.INLINE)
d.comment(0xA907, "A=2 (reply length/marker)", align=Align.INLINE)
d.comment(0xA909, "Store into the reply buffer", align=Align.INLINE)
d.comment(0xA90B, "OSWORD: read CMOS real-time clock", align=Align.INLINE)
d.comment(0xA90D, "X = reply buffer low", align=Align.INLINE)
d.comment(0xA90F, "Y = reply buffer high", align=Align.INLINE)
d.comment(0xA911, "Save flags", align=Align.INLINE)
d.comment(0xA912, "Read the CMOS clock", align=Align.INLINE)
d.comment(0xA915, "Restore flags", align=Align.INLINE)
d.comment(0xA916, "Success: return", align=Align.INLINE)
d.comment(0xA918, "Failure: write default century", align=Align.INLINE)
d.comment(0xA91A, "'0'", align=Align.INLINE)
d.comment(0xA91C, "Store century units", align=Align.INLINE)
d.comment(0xA91E, "Back up one", align=Align.INLINE)
d.comment(0xA91F, "'2'", align=Align.INLINE)
d.comment(0xA921, "Store century tens -- default \"20\"", align=Align.INLINE)

d.entry(0xA924)
d.subroutine(
    0xA924,
    "bin_to_bcd",
    title="Binary to packed BCD",
    description="""Converts the binary value in A to packed BCD using decimal-mode
addition. Preserves X/Y. Rewritten helper shared by
[`save_txcb_and_convert`](label:save_txcb_and_convert).""",
)
d.comment(0xA924, "Save flags", align=Align.INLINE)
d.comment(0xA925, "Hold binary value in X", align=Align.INLINE)
d.comment(0xA926, "A = &99 (BCD accumulator seed)", align=Align.INLINE)
d.comment(0xA928, "Enter decimal mode", align=Align.INLINE)
d.comment(0xA929, "Clear carry for the add loop", align=Align.INLINE)
d.label(0xA929, "loop_bcd_add")

d.entry(0xBFF7)
d.subroutine(
    0xBFF7,
    "fs_num_via_osargs",
    title="Read current filing-system number via OSARGS",
    description="""New in 4.26. Reads the current filing-system number with OSARGS
(reason 0) and compares it with 5 (NetFS), returning Z=1 (EQ) when NetFS is
current. [`osword_0e_dispatch`](label:osword_0e_dispatch) uses this to service the
clock OSWORD only under NetFS, leaving it for other filing systems otherwise.

The `PHA` / `PLX` pair is a deliberate register **relay**, not a save/restore.
On entry `A` holds the OSWORD sub-code; `PHA` stashes it on the stack so it
survives the `OSARGS` call (which returns the FS number in `A` and need not
preserve `X`). `PLX` then recovers the sub-code into `X` -- so the caller's
`TXA` picks it up to dispatch on. One push/pull thus both protects the sub-code
across `OSARGS` and moves it from `A` to `X`. Zeroing `A` for the call via `TYA`
(rather than `LDA #0`) likewise leans on `Y` already being 0 at entry.

Occupies ROM-tail space that was &FF padding in 4.25; its final bytes double
as the [`hazel_minus_2`](label:hazel_minus_2) / [`hazel_minus_1`](label:hazel_minus_1)
indexing-base anchors.""",
    on_entry={"a": "OSWORD sub-code (relayed out in X)", "y": "0 -- used as the OSARGS reason code"},
    on_exit={
        "a": "current filing-system number",
        "x": "OSWORD sub-code (relayed from entry A)",
        "z": "set (EQ) if NetFS (5) is the current filing system",
    },
)
d.comment(0xBFF7, "Stash the OSWORD sub-code (in A) on the stack -- survives OSARGS", align=Align.INLINE)
d.comment(0xBFF8, "A = 0 via Y (assumed 0): OSARGS reason 0 = read current FS number", align=Align.INLINE)
d.comment(0xBFF9, "OSARGS reason 0: current FS number -> A", align=Align.INLINE)
d.comment(0xBFFC, "Relay the stashed sub-code into X (not a restore) for the caller's TXA", align=Align.INLINE)
d.comment(0xBFFD, "Current FS = 5 (NetFS)? (sets Z)", align=Align.INLINE)
d.comment(0xBFFF, "Return: Z = NetFS selected, A = FS number, X = OSWORD sub-code", align=Align.INLINE)

# &94C0: 4.26 fixes the 'Bad string' error path -- 4.25 read brk_ptr (LDA &FD)
# instead of loading the error number, so the error was not set correctly.
d.comment(0x94C0, "A=&FD: 'Bad string' error number (LDA #&FD)", align=Align.INLINE)
d.comment(0xA8D5, "Shift high nibble down (2 of 4)", align=Align.INLINE)
d.comment(0xA8D6, "Shift high nibble down (3 of 4)", align=Align.INLINE)
d.comment(0xA8D7, "Shift high nibble down (4 of 4)", align=Align.INLINE)
d.comment(0xA92A, "Add 1 in decimal mode", align=Align.INLINE)
d.comment(0xA92C, "Count down the binary value", align=Align.INLINE)
d.comment(0xA92D, "Loop until the BCD total is built", align=Align.INLINE)
d.comment(0xA92F, "Restore flags", align=Align.INLINE)
d.comment(0xA930, "Return with A = packed BCD", align=Align.INLINE)
d.label(0xBFFD, "fs_num_check")

d.banner(0x863C, title="Immediate-op TX control-frame length table",
         description="Length of the TX control frame per immediate-op control byte (&81 PEEK .. &88 machine-type): PEEK/POKE &0E, JSR/UserProc/OSProc &0A, HALT/CONTINUE &06, machine-type &0A. Indexed by the immediate-op control byte.")
d.label(0x863C, "tx_length_values")
d.byte(0x863C, 8)
d.banner(0x8644, title="Immediate-op TX flags table",
         description="TX flags per immediate-op control byte. Bit 7 (&80) marks a reply-generating operation -- set for PEEK (&81) and machine-type (&88); HALT/CONTINUE &01; POKE/exec &00.")
d.label(0x8644, "tx_flags_values")
d.byte(0x8644, 8)

ir = d.disassemble()
output = str(
    ir.render(
        "beebasm",
        char_literal_style="quote",
        show_char_comment_hint=False,
        boundary_label_prefix="pydis_",
        byte_column=True,
        byte_column_format="py8dis",
        default_byte_cols=12,
        default_word_cols=6,
    )
)
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / "anfs-4.26.asm"
output_filepath.write_text(output, encoding="utf-8")
print(f"Wrote {output_filepath}", file=sys.stderr)
json_filepath = _output_dirpath / "anfs-4.26.json"
json_filepath.write_text(str(ir.render("json")), encoding="utf-8")
print(f"Wrote {json_filepath}", file=sys.stderr)
