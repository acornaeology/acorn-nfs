import os
from pathlib import Path
import dasmos
from dasmos.expr import sym, lo, hi
from dasmos import Align
from dasmos.hooks import stringhi_hook, stringz_hook

_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get("FANTASM_ROM", str(_version_dirpath / "rom" / "anfs-4.24.rom"))
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
    (0x0001, 0x8E88, "dispatch_rts", "no-op (RTS only)"),
    (0x0002, 0x8D2B, "svc_dispatch_idx_2", "workspace claim helper (CMOS bit 0)"),
    (0x0003, 0x8F28, "svc_2_priv_ws", "svc &02: private workspace pages"),
    (0x0004, 0x8CEC, "svc_3_autoboot", "svc &03: auto-boot"),
    (0x0005, 0x8C67, "svc_4_star_command", "svc &04: unrecognised *command"),
    (0x0006, 0x802A, "svc5_irq_check", "svc &05: IRQ check"),
    (0x0007, 0x8E88, "dispatch_rts", "no-op (RTS only)"),
    (0x0008, 0x8EF0, "svc_7_osbyte", "svc &07: unrecognised OSBYTE"),
    (0x0009, 0xA855, "svc_8_osword_disp", "svc &08: OSWORD dispatch"),
    (0x000A, 0x8C76, "svc_9_help", "svc &09: *HELP"),
    (0x000B, 0x8E88, "dispatch_rts", "no-op (RTS only)"),
    (0x000C, 0x806E, "econet_restore", "svc &0B: NMI release"),
    (0x000D, 0x89D9, "wait_idle_and_reset", "svc &0D: wait idle and reset"),
    (0x000E, 0x8B6B, "svc_18_fs_select", "svc &12: FS select"),
    (0x0F, 0x9690, "match_on_suffix", "svc &18: interactive HELP 'ON ' matcher"),
    (0x0010, 0x8F01, "raise_y_to_c8", "svc &21: static workspace claim"),
    (0x0011, 0x8F16, "set_rom_ws_page", "svc &22: dynamic workspace offer"),
    (0x0012, 0x8F08, "store_ws_page_count", "svc &23: top-of-static-workspace"),
    (0x0013, 0x8E89, "noop_dey_rts", "svc &24: dynamic workspace claim"),
    (0x0014, 0x8E8B, "copy_template_to_zp", "svc &25: FS name + info reply"),
    (0x0015, 0x8EA2, "svc_26_close_all_files", "svc &26: close all files"),
    (0x0016, 0x8F50, "nfs_init_body", "svc &27: post-hard-reset re-init"),
    (0x0017, 0x959F, "print_fs_ps_help", "svc &28: print *FS/*PS no-arg syntax help"),
    (0x0018, 0x962F, "svc_29_status", "svc &29: *STATUS handler"),
    (0x0019, 0x98AD, "lang_0_insert_key", "language reply 0: insert remote key"),
    (0x001A, 0x984E, "lang_1_remote_boot", "language reply 1: remote boot"),
    (0x001B, 0xB04F, "lang_2_save_palette_vdu", "language reply 2: save palette/VDU"),
    (0x001C, 0x987C, "lang_3_exec_0100", "language reply 3: execute at &0100"),
    (0x001D, 0x989D, "lang_4_validated", "language reply 4: remote validated"),
    (0x001E, 0xA0CF, "fscv_0_opt_entry", "FSCV 0: *OPT"),
    (0x001F, 0xA131, "fscv_1_eof", "FSCV 1: EOF"),
    (0x0020, 0xA505, "cmd_run_via_urd", "FSCV 2: *RUN"),
    (0x0021, 0xA443, "fscv_3_star_cmd", "FSCV 3: *command"),
    (0x0022, 0xA505, "cmd_run_via_urd", "FSCV 4: *RUN (alias)"),
    (0x0023, 0xB14B, "fscv_5_cat", "FSCV 5: *CAT"),
    (0x0024, 0x9078, "fscv_6_shutdown", "FSCV 6: shutdown"),
    (0x0025, 0x93F7, "fscv_7_read_handles", "FSCV 7: read handles"),
    (0x0026, 0x8E88, "dispatch_rts", "no-op (RTS only)"),
    (0x0027, 0xB131, "ps_scan_resume", "PS scan tail (after pop_requeue)"),
    (0x0028, 0xB38A, "cmd_info_dispatch", "*Info dispatch"),
    (0x0029, 0xA4F0, "check_urd_present", "URD-present check"),
    (0x002A, 0xB30E, "ex_init_scan_x0", "*Ex scan init"),
    (0x002B, 0xA6E9, "fsreply_1_boot", "FS reply 1: copy handles + boot"),
    (0x002C, 0xA6F9, "fsreply_2_copy_handles", "FS reply 2: copy handles"),
    (0x002D, 0xA64C, "fsreply_3_set_csd", "FS reply 3: set CSD"),
    (0x002E, 0xA505, "cmd_run_via_urd", "FS reply 4: *RUN (alias)"),
    (0x002F, 0xA652, "fsreply_5_set_lib", "FS reply 5: set library"),
    (0x0030, 0xA413, "net_1_read_handle", "net handle 1: read handle"),
    (0x0031, 0xA419, "net_2_read_entry", "net handle 2: read handle entry"),
    (0x0032, 0xA429, "net_3_close_handle", "net handle 3: close handle"),
]
_cmd_table_fs_entries = [
(0xA780, "Net", 0xA783, 0x80, 0xA784, "cmd_net_check_hw", "Econet HW check + select NFS"),
(0xA786, "Pollps", 0xA78C, 0x88, 0xA78D, "cmd_pollps", "syn 8: (<stn. id.>|<ps type>)"),
(0xA78F, "Prot", 0xA793, 0x80, 0xA794, "cmd_prot", "toggle CMOS protection bit"),
(0xA796, "PS", 0xA798, 0x88, 0xA799, "cmd_ps", "syn 8: (<stn. id.>|<ps type>)"),
(0xA79B, "Roff", 0xA79F, 0x80, 0xA7A0, "cmd_roff", "printer offline"),
(0xA7A2, "Unprot", 0xA7A8, 0x80, 0xA7A9, "cmd_unprot", "toggle CMOS protection bit"),
(0xA7AB, "Wdump", 0xA7B0, 0xC4, 0xA7B1, "cmd_dump", "syn 4 -- *DUMP alias"),
(0xA7B5, "Access", 0xA7BB, 0xC9, 0xA7BC, "cmd_fs_operation", "syn 9: <obj> (L)(W)(R)..."),
(0xA7BE, "Bye", 0xA7C1, 0x80, 0xA7C2, "cmd_bye", "log off FS"),
(0xA7C4, "Cdir", 0xA7C8, 0xC6, 0xA7C9, "cmd_cdir", "syn 6 -- create directory"),
(0xA7CB, "Dir", 0xA7CE, 0x81, 0xA7CF, "cmd_dir", "syn 1: (<dir>)"),
(0xA7D1, "Flip", 0xA7D5, 0x80, 0xA7D6, "cmd_flip", "swap fs/private workspace"),
(0xA7D8, "FS", 0xA7DA, 0x8B, 0xA7DB, "cmd_fs", "syn &B -- file-server selection"),
(0xA7DD, "I am", 0xA7E1, 0xC2, 0xA7E2, "cmd_iam_save_ctx", "syn 2: (<stn>) <user>..."),
(0xA7E4, "Lcat", 0xA7E8, 0x81, 0xA7E9, "cmd_lcat", "syn 1: (<dir>) -- *CAT of library"),
(0xA7EB, "Lex", 0xA7EE, 0x81, 0xA7EF, "cmd_lex", "syn 1: (<dir>) -- *EX of library"),
(0xA7F1, "Lib", 0xA7F4, 0xC5, 0xA7F5, "cmd_fs_operation", "syn 5: <dir> -- set library"),
(0xA7F7, "Pass", 0xA7FB, 0xC7, 0xA7FC, "cmd_pass", "syn 7: <pass> ..."),
(0xA7FE, "Rename", 0xA804, 0xCA, 0xA805, "cmd_rename", "syn &A: <old> <new>"),
(0xA807, "Wipe", 0xA80B, 0x81, 0xA80C, "cmd_wipe", "syn 1: (<dir>) -- delete with confirm"),
(0xA816, "Net", 0xA819, 0x80, 0xA81A, "help_net", "*HELP NET"),
(0xA81C, "Utils", 0xA821, 0x80, 0xA822, "help_utils", "*HELP UTILS"),
(0xA825, "FS", 0xA827, 0xC1, 0xA828, "set_fs_or_ps_cmos_station", "FS not selected"),
(0xA82A, "PS", 0xA82C, 0xC3, 0xA82D, "set_fs_or_ps_cmos_station", "PS not selected"),
(0xA82F, "NoSpace", 0xA836, 0x80, 0xA837, None, "caller &9623"),
(0xA839, "Space", 0xA83E, 0x80, 0xA83F, None, "caller &9619"),
(0xA842, "FS", 0xA844, 0x81, 0xA845, "print_fs_address", "caller &9670"),
(0xA847, "PS", 0xA849, 0x83, 0xA84A, "print_ps_address", "caller &965F"),
(0xA84C, "Space", 0xA851, 0x80, 0xA852, None, "caller &9641"),
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
    "acorn_sideways_rom", rom_title="ANFS ROM 4.24 disassembly (Acorn Advanced Network Filing System)"
)
d.index_base(0x0000, "zp_ptr_lo", length=1, group="zero_page")

# 4.24 dispatch-table bases (read from each dispatcher's operand; the
# tables hold shifted handler addresses so they don't opcode-map).
for idx, name, role in _netv_dispatch_entries:
    d.expr(0xAD40 + idx, lo(sym(name) - 1))
    d.expr(0xAD49 + idx, hi(sym(name) - 1))
    d.comment(0xAD40 + idx, "reason &%02X: %s (%s)" % (idx, name, role), align=Align.INLINE)
    d.comment(0xAD49 + idx, "reason &%02X: %s" % (idx, name), align=Align.INLINE)
for idx, name, role in _osword_13_entries:
    d.expr(0xA9C8 + idx, lo(sym(name) - 1))
    d.expr(0xA9DA + idx, hi(sym(name) - 1))
    d.comment(0xA9C8 + idx, "sub &%02X: %s (%s)" % (idx, name, role), align=Align.INLINE)
    d.comment(0xA9DA + idx, "sub &%02X: %s" % (idx, name), align=Align.INLINE)

for idx, target, name, desc in _svc_dispatch_entries:
    if name is not None:
        d.expr(0x8A23 + idx, lo(sym(name) - 1))
        d.expr(0x8A56 + idx, hi(sym(name) - 1))
    d.comment(0x8A23 + idx, "&%02X: %s" % (idx, desc), align=Align.INLINE)
    d.comment(0x8A56 + idx, "&%02X: %s" % (idx, desc), align=Align.INLINE)
d.index_base(0x0001, "zp_ptr_hi", length=1, group="zero_page")

d.index_base(0x0002, "zp_work_2", length=1, group="zero_page")

for i, (name, handler_label) in enumerate(handler_names):
    base_addr = 0x8ECD + i * 3
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
| set   | TX not-listening – `JMP` [`tx_result_fail`](label:tx_result_fail) |""",
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
the ADLC to idle RX-listen mode.""",
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
d.comment(0x85AC, "Return with A=0 (success)", align=Align.INLINE)
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
# UNMAPPED: 4. Enters the INACTIVE polling loop at
# UNMAPPED:    [`inactive_poll`](label:inactive_poll).""",
# UNMAPPED: )


# UNMAPPED: d.comment(0x8589, "Save X on stack", align=Align.INLINE)
d.comment(0x864B, "Push X", align=Align.INLINE)
d.comment(0x864C, "Y=2: TXCB offset for dest station", align=Align.INLINE)
d.comment(0x864E, "Load dest station from TX control block", align=Align.INLINE)
d.comment(0x8650, "Store to TX scout buffer", align=Align.INLINE)
d.comment(0x8654, "Load dest network from TX control block", align=Align.INLINE)
d.comment(0x8656, "Store to TX scout buffer", align=Align.INLINE)
d.comment(0x8659, "Y=0: first byte of TX control block", align=Align.INLINE)
d.comment(0x865B, "Load control/flag byte", align=Align.INLINE)
d.comment(0x865D, "Bit7 set: immediate operation ctrl byte", align=Align.INLINE)
d.comment(0x865F, "Bit7 clear: normal data transfer", align=Align.INLINE)
d.label(0x8662, "tx_imm_op_setup")

d.comment(0x8662, "Store control byte to TX scout buffer", align=Align.INLINE)
d.comment(0x8665, "X = control byte for range checks", align=Align.INLINE)
d.comment(0x8666, "Y=1: port byte offset", align=Align.INLINE)
d.comment(0x8667, "Load port byte from TX control block", align=Align.INLINE)
d.comment(0x8669, "Store port byte to TX scout buffer", align=Align.INLINE)
d.comment(0x866C, "Port != 0: skip immediate op setup", align=Align.INLINE)
d.comment(0x866E, "Ctrl < &83: PEEK/POKE need address calc", align=Align.INLINE)
d.comment(0x8670, "Ctrl >= &83: skip to range check", align=Align.INLINE)
d.comment(0x8672, "Init borrow for 4-byte subtract", align=Align.INLINE)
d.comment(0x8673, "Save carry on stack for loop", align=Align.INLINE)
d.comment(0x8674, "Y=8: high pointer offset in TXCB", align=Align.INLINE)
d.label(0x8676, "calc_peek_poke_size")

d.comment(0x8676, "Load TXCB[Y] (end addr byte)", align=Align.INLINE)
d.comment(0x8678, "Y -= 4: back to start addr offset", align=Align.INLINE)
d.comment(0x8679, "(continued)", align=Align.INLINE)
d.comment(0x867A, "(continued)", align=Align.INLINE)
d.comment(0x867B, "(continued)", align=Align.INLINE)
d.comment(0x867C, "Restore borrow from stack", align=Align.INLINE)
d.comment(0x867D, "end - start = transfer size byte", align=Align.INLINE)
d.comment(0x867F, "Store result to tx_data_start", align=Align.INLINE)
d.comment(0x8682, "Y += 5: advance to next end byte", align=Align.INLINE)
d.comment(0x8683, "(continued)", align=Align.INLINE)
d.comment(0x8684, "(continued)", align=Align.INLINE)
d.comment(0x8685, "(continued)", align=Align.INLINE)
d.comment(0x8686, "(continued)", align=Align.INLINE)
d.comment(0x8687, "Save borrow for next byte", align=Align.INLINE)
d.comment(0x8688, "Done all 4 bytes? (Y reaches &0C)", align=Align.INLINE)
d.comment(0x868A, "No: next byte pair", align=Align.INLINE)
d.comment(0x868C, "Discard final borrow", align=Align.INLINE)
d.label(0x868D, "tx_ctrl_range_check")

d.comment(0x868D, "Ctrl < &81: not an immediate op", align=Align.INLINE)
d.comment(0x868F, "Below range: normal data transfer", align=Align.INLINE)
d.label(0x8691, "check_imm_range")

d.comment(0x8691, "Ctrl >= &89: out of immediate range", align=Align.INLINE)
d.comment(0x8693, "Above range: normal data transfer", align=Align.INLINE)
d.comment(0x8695, "Y=&0C: start of extra data in TXCB", align=Align.INLINE)
d.label(0x8697, "copy_imm_params")

d.comment(0x8697, "Load extra parameter byte from TXCB", align=Align.INLINE)
d.comment(0x8699, "Copy to NMI shim workspace at &0D1A+Y", align=Align.INLINE)
d.comment(0x869C, "Next byte", align=Align.INLINE)
d.comment(0x869D, "Done 4 bytes? (Y reaches &10)", align=Align.INLINE)
d.comment(0x869F, "No: continue copying", align=Align.INLINE)
d.label(0x86A1, "tx_line_idle_check")

d.comment(0x86A1, "A=&20: mask for SR2 INACTIVE bit", align=Align.INLINE)
d.comment(0x86A3, "Test SR2 if line is idle", align=Align.INLINE)
d.comment(0x86A6, "Line not idle: handle as line jammed", align=Align.INLINE)
d.comment(0x86A8, "A=&FD: high byte of timeout counter", align=Align.INLINE)
d.comment(0x86AA, "Push timeout high byte to stack", align=Align.INLINE)
d.comment(0x86AB, "Scout frame = 6 address+ctrl bytes", align=Align.INLINE)
d.comment(0x86AD, "Store scout frame length", align=Align.INLINE)
d.comment(0x86B0, "A=0: init low byte of timeout counter", align=Align.INLINE)
d.entry(0x86B2)
d.subroutine(
    0x86B2,
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


d.comment(0x86B2, "Save TX index", align=Align.INLINE)
d.comment(0x86B5, "Push timeout byte 1 on stack", align=Align.INLINE)
d.comment(0x86B6, "Push timeout byte 2 on stack", align=Align.INLINE)
d.comment(0x86B7, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", align=Align.INLINE)
# UNMAPPED: d.label(0x85F8, "reload_inactive_mask")

d.comment(0x86C3, "A=&04: INACTIVE bit mask for SR2 test", align=Align.INLINE)
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


d.comment(0x86C0, "INTOFF -- disable NMIs", align=Align.INLINE)
# UNMAPPED: d.expr_label(0x85FD, "tx_ctrl_dispatch_lo-&81")

# UNMAPPED: d.comment(0x85FF, "INTOFF again (belt-and-braces)", align=Align.INLINE)
# UNMAPPED: d.label(0x8602, "test_line_idle")

d.comment(0x86C5, "Z = &04 AND SR2 -- tests INACTIVE", align=Align.INLINE)
# UNMAPPED: d.comment(0x8605, "INACTIVE not set -- re-enable NMIs and loop", align=Align.INLINE)
d.comment(0x86CA, "Read SR1 (acknowledge pending interrupt)", align=Align.INLINE)
d.comment(0x86CF, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", align=Align.INLINE)
d.comment(0x86D1, "Write CR2: clear status, prepare TX", align=Align.INLINE)
d.comment(0x86D4, "A=&10: CTS mask for SR1 bit4", align=Align.INLINE)
d.comment(0x86D6, "Test SR1 CTS present", align=Align.INLINE)
d.comment(0x86D9, "CTS set -- clock hardware detected, start TX", align=Align.INLINE)
d.label(0x86E0, "inactive_retry")

d.comment(0x86E0, "INTON -- re-enable NMIs (Master &FE3C)", align=Align.INLINE)
d.comment(0x86E3, "Restore interrupt state", align=Align.INLINE)
d.comment(0x86E4, "3-byte timeout counter on stack", align=Align.INLINE)
d.comment(0x86E5, "Increment timeout counter byte 1", align=Align.INLINE)
d.comment(0x86E8, "Not overflowed: retry INACTIVE test", align=Align.INLINE)
d.comment(0x86EA, "Increment timeout counter byte 2", align=Align.INLINE)
d.comment(0x86ED, "Not overflowed: retry INACTIVE test", align=Align.INLINE)
d.comment(0x86EF, "Increment timeout counter byte 3", align=Align.INLINE)
d.comment(0x86F2, "Not overflowed: retry INACTIVE test", align=Align.INLINE)
d.label(0x86F6, "tx_bad_ctrl_error")

d.subroutine(
    0x86F6,
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


d.comment(0x86F6, "Error &44: control byte out of valid range", align=Align.INLINE)
d.subroutine(
    0x86FA,
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


d.comment(0x86FA, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", align=Align.INLINE)
d.comment(0x86FC, "Write CR2 to abort TX", align=Align.INLINE)
d.comment(0x86FF, "Clean 3 bytes of timeout loop state", align=Align.INLINE)
d.comment(0x8700, "Pop saved register", align=Align.INLINE)
d.comment(0x8701, "Pop saved register", align=Align.INLINE)
d.comment(0x8702, "Error &40 = 'Line Jammed'", align=Align.INLINE)
d.comment(0x8704, "ALWAYS branch to shared error handler", align=Align.INLINE)
d.label(0x8706, "tx_no_clock_error")

d.comment(0x8706, "Error &43 = 'No Clock'", align=Align.INLINE)
d.label(0x8708, "store_tx_error")

d.comment(0x8708, "Offset 0 = error byte in TX control block", align=Align.INLINE)
d.comment(0x870A, "Store error code in TX CB byte 0", align=Align.INLINE)
d.comment(0x870C, "&80 = TX complete flag", align=Align.INLINE)
d.comment(0x870E, "Signal TX operation complete", align=Align.INLINE)
d.comment(0x8711, "Restore X saved by caller", align=Align.INLINE)
d.comment(0x8712, "Move to X register", align=Align.INLINE)
d.comment(0x8713, "Return to TX caller", align=Align.INLINE)
d.subroutine(
    0x8714,
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


d.comment(0x8714, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", align=Align.INLINE)
d.comment(0x8717, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", align=Align.INLINE)
d.comment(0x8719, "Write to ADLC CR1", align=Align.INLINE)
d.comment(0x871C, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x871E, "High byte of NMI handler address", align=Align.INLINE)
d.comment(0x8720, "Write NMI vector low byte directly", align=Align.INLINE)
d.comment(0x8723, "Write NMI vector high byte directly", align=Align.INLINE)
d.comment(0x8726, "SEC: prepare carry for ROR into bit 7", align=Align.INLINE)
d.comment(0x8727, "Rotate carry into bit 7 of prot_flags (Tube-claimed)", align=Align.INLINE)
d.comment(0x872E, "INTON -- NMIs now fire for TDRA (Master &FE3C)", align=Align.INLINE)
d.comment(0x8731, "Load destination port number", align=Align.INLINE)
d.comment(0x8734, "Port != 0: standard data transfer", align=Align.INLINE)
d.comment(0x8736, "Port 0: load control byte for table lookup", align=Align.INLINE)
d.comment(0x8739, "Look up tx_flags from table", align=Align.INLINE)
d.comment(0x873C, "Store operation flags", align=Align.INLINE)
d.comment(0x873F, "Look up tx_length from table", align=Align.INLINE)
d.comment(0x8742, "Store expected transfer length", align=Align.INLINE)
d.comment(0x8745, "A=&87: high byte of tx_ctrl_* dispatch target", align=Align.INLINE)
d.comment(0x8747, "Push high byte for PHA/PHA/RTS dispatch", align=Align.INLINE)
d.comment(0x8748, "Look up handler address low from table", align=Align.INLINE)
d.comment(0x874B, "Push low byte for PHA/PHA/RTS dispatch", align=Align.INLINE)
d.comment(0x874C, "RTS dispatches to control-byte handler", align=Align.INLINE)


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
d.comment(0x874F, "Skip address addition, store status", align=Align.INLINE)
d.subroutine(
    0x8751,
    "tx_ctrl_peek",
    title="TX ctrl: PEEK transfer setup",
    description="""Sets `A=3` (scout_status for PEEK) and branches to
[`tx_ctrl_store_and_add`](label:tx_ctrl_store_and_add) to store the status
and perform the 4-byte transfer-address addition.""",
    on_exit={"a": "3 (scout_status for PEEK)"},
)


d.comment(0x8751, "A=3: scout_status for PEEK op", align=Align.INLINE)
d.subroutine(
    0x8755,
    "tx_ctrl_poke",
    title="TX ctrl: POKE transfer setup",
    description="""Sets `A=2` (scout_status for POKE) and falls through to
[`tx_ctrl_store_and_add`](label:tx_ctrl_store_and_add) to store the status
and perform the 4-byte transfer-address addition.""",
    on_exit={"a": "2 (scout_status for POKE)"},
)


d.comment(0x8755, "Scout status = 2 (POKE transfer)", align=Align.INLINE)
d.subroutine(
    0x8757,
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


d.comment(0x8757, "Store scout status", align=Align.INLINE)
d.comment(0x875A, "Clear carry for 4-byte addition", align=Align.INLINE)
d.comment(0x875B, "Save carry on stack", align=Align.INLINE)
d.comment(0x875C, "Y=&0C: start at offset 12", align=Align.INLINE)
d.label(0x875E, "add_bytes_loop")

d.comment(0x875E, "Load workspace address byte", align=Align.INLINE)
d.comment(0x8761, "Restore carry from previous byte", align=Align.INLINE)
d.comment(0x8762, "Add TXCB address byte", align=Align.INLINE)
d.comment(0x8764, "Store updated address byte", align=Align.INLINE)
d.comment(0x8767, "Next byte", align=Align.INLINE)
d.comment(0x8768, "Save carry for next addition", align=Align.INLINE)
d.subroutine(
    0x8769,
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


d.comment(0x8769, "Compare Y with 16-byte boundary", align=Align.INLINE)
d.comment(0x876B, "Below boundary: continue addition", align=Align.INLINE)
d.comment(0x876D, "Restore processor flags", align=Align.INLINE)
d.comment(0x876E, "Skip buffer setup if transfer size is zero", align=Align.INLINE)
d.label(0x8770, "setup_data_xfer")

d.comment(0x8770, "Load dest station for broadcast check", align=Align.INLINE)
d.comment(0x8773, "AND with dest network", align=Align.INLINE)
d.comment(0x8776, "Both &FF = broadcast address?", align=Align.INLINE)
d.comment(0x8778, "Not broadcast: unicast path", align=Align.INLINE)
d.comment(0x877A, "Broadcast scout: 14 bytes total", align=Align.INLINE)
d.comment(0x877C, "Store broadcast scout length", align=Align.INLINE)
d.comment(0x877F, "A=&40: broadcast flag", align=Align.INLINE)
d.comment(0x8781, "Set broadcast flag in tx_flags", align=Align.INLINE)
d.comment(0x8784, "Y=4: start of address data in TXCB", align=Align.INLINE)
d.label(0x8786, "copy_bcast_addr")

d.comment(0x8786, "Copy TXCB address bytes to scout buffer", align=Align.INLINE)
d.comment(0x8788, "Store to TX source/data area", align=Align.INLINE)
d.comment(0x878B, "Next byte", align=Align.INLINE)
d.comment(0x878C, "Done 8 bytes? (Y reaches &0C)", align=Align.INLINE)
d.comment(0x878E, "No: continue copying", align=Align.INLINE)
d.label(0x8792, "setup_unicast_xfer")

d.comment(0x8792, "A=0: clear flags for unicast", align=Align.INLINE)
d.comment(0x8794, "Clear tx_flags", align=Align.INLINE)
d.label(0x8797, "proc_op_status2")

d.comment(0x8797, "scout_status=2: data transfer pending", align=Align.INLINE)
d.label(0x8799, "store_status_copy_ptr")

d.comment(0x8799, "Store scout status", align=Align.INLINE)
d.label(0x879C, "skip_buf_setup")

d.comment(0x879C, "Copy TX block pointer to workspace ptr", align=Align.INLINE)
d.comment(0x879E, "Store low byte", align=Align.INLINE)
d.comment(0x87A0, "Copy TX block pointer high byte", align=Align.INLINE)
d.comment(0x87A2, "Store high byte", align=Align.INLINE)
d.comment(0x87A4, "Calculate transfer size from RXCB", align=Align.INLINE)
d.label(0x87A7, "tx_ctrl_exit")

d.comment(0x87A7, "Restore processor status from stack", align=Align.INLINE)
d.comment(0x87A8, "Restore stacked registers (4 PLAs)", align=Align.INLINE)
d.comment(0x87AC, "Restore X from A", align=Align.INLINE)
d.comment(0x87AD, "Return to caller", align=Align.INLINE)
d.entry(0x87B6)
d.subroutine(
    0x87B6,
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


d.comment(0x87B6, "Load TX buffer index", align=Align.INLINE)
d.comment(0x87B9, "SR1: V=bit6(TDRA), N=bit7(IRQ)", align=Align.INLINE)
d.label(0x87BC, "tx_fifo_write")

d.comment(0x87BC, "TDRA not set -- TX error", align=Align.INLINE)
d.comment(0x87BE, "Load byte from TX buffer", align=Align.INLINE)
d.comment(0x87C1, "Write to TX_DATA (continue frame)", align=Align.INLINE)
d.comment(0x87C4, "Next TX buffer byte", align=Align.INLINE)
d.comment(0x87C5, "Load second byte from TX buffer", align=Align.INLINE)
d.comment(0x87C8, "Advance TX index past second byte", align=Align.INLINE)
d.comment(0x87C9, "Save updated TX buffer index", align=Align.INLINE)
d.comment(0x87CC, "Write second byte to TX_DATA", align=Align.INLINE)
d.comment(0x87CF, "Compare index to TX length", align=Align.INLINE)
d.comment(0x87D2, "Frame complete -- go to TX_LAST_DATA", align=Align.INLINE)
d.comment(0x87D4, "Check if we can send another pair", align=Align.INLINE)
d.comment(0x87D7, "IRQ set -- send 2 more bytes (tight loop)", align=Align.INLINE)
d.comment(0x87D9, "Wait for next NMI", align=Align.INLINE)
d.label(0x87DC, "tx_error")

d.entry(0x87DC)
d.comment(0x87DC, "Error &42", align=Align.INLINE)
d.label(0x87E0, "tx_fifo_not_ready")

d.comment(0x87E0, "CR2=&67: clear status, return to listen", align=Align.INLINE)
d.comment(0x87E2, "Write CR2: clear status, idle listen", align=Align.INLINE)
d.comment(0x87E5, "Error &41 (TDRA not ready)", align=Align.INLINE)
d.label(0x87E7, "tx_store_error")

d.comment(0x87E7, "INTOFF: disable NMIs (Master &FE38)", align=Align.INLINE)
d.label(0x87EA, "delay_nmi_disable")

d.comment(0x87EA, "PHA/PLA delay loop (256 iterations for NMI disable)", align=Align.INLINE)
d.comment(0x87EB, "PHA/PLA delay (~7 cycles each)", align=Align.INLINE)
d.comment(0x87EC, "Increment delay counter", align=Align.INLINE)
d.comment(0x87ED, "Loop 256 times for NMI disable", align=Align.INLINE)
d.comment(0x87EF, "Store error and return to idle", align=Align.INLINE)
d.entry(0x87F2)
d.subroutine(
    0x87F2,
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


d.comment(0x87F2, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", align=Align.INLINE)
d.comment(0x87F4, "Write to ADLC CR2", align=Align.INLINE)
d.comment(0x87F7, "Install TX->RX switch handler (low)", align=Align.INLINE)
# UNMAPPED: d.comment(0x872A, "High byte of handler address", align=Align.INLINE)
d.comment(0x87F9, "Install and return via set_nmi_vector", align=Align.INLINE)
d.entry(0x87FC)
d.subroutine(
    0x87FC,
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


d.comment(0x87FC, "Jump to error handler", align=Align.INLINE)
d.comment(0x87FE, "Write CR1 to switch from TX to RX", align=Align.INLINE)
d.comment(0x8801, "Test workspace flags", align=Align.INLINE)
d.comment(0x8804, "bit6 not set -- check bit0", align=Align.INLINE)
d.comment(0x8806, "bit6 set -- TX completion", align=Align.INLINE)
d.label(0x8809, "check_handshake_bit")

d.comment(0x8809, "A=1: mask for bit0 test", align=Align.INLINE)
d.comment(0x880B, "Test tx_flags bit0 (handshake)", align=Align.INLINE)
d.comment(0x880E, "bit0 clear: install reply handler", align=Align.INLINE)
d.comment(0x8810, "bit0 set -- four-way handshake data phase", align=Align.INLINE)
d.label(0x8813, "install_reply_scout")

d.comment(0x8813, "Install nmi_reply_scout (low)", align=Align.INLINE)
d.comment(0x8817, "Install handler", align=Align.INLINE)
d.entry(0x881A)
d.subroutine(
    0x881A,
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


d.comment(0x881A, "A=&01: AP mask for SR2", align=Align.INLINE)
d.comment(0x881C, "Test SR2 AP (Address Present)", align=Align.INLINE)
d.comment(0x881F, "No AP -- error", align=Align.INLINE)
d.comment(0x8821, "Read first RX byte (destination station)", align=Align.INLINE)
d.comment(0x8824, "Compare to our station ID (workspace copy)", align=Align.INLINE)
d.comment(0x8827, "Not our station -- error/reject", align=Align.INLINE)
d.comment(0x8829, "Install reply-continuation handler (low)", align=Align.INLINE)
d.comment(0x882B, "Install continuation handler", align=Align.INLINE)
d.entry(0x882E)
d.subroutine(
    0x882E,
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


d.comment(0x882E, "Read RX byte (destination station)", align=Align.INLINE)
d.comment(0x8831, "No RDA -- error", align=Align.INLINE)
d.comment(0x8833, "Read destination network byte", align=Align.INLINE)
d.comment(0x8836, "Non-zero -- network mismatch, error", align=Align.INLINE)
d.comment(0x8838, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x883A, "Test SR1 IRQ (N=bit7) -- more data ready?", align=Align.INLINE)
d.comment(0x883D, "IRQ set -- fall through to &8848", align=Align.INLINE)
d.comment(0x883F, "IRQ not set -- install handler", align=Align.INLINE)
d.label(0x8842, "reject_reply")

d.subroutine(
    0x8842,
    "reject_reply",
    title="Abandon reply scout (1-instruction trampoline)",
    description="""Single `JMP` to [`tx_result_fail`](label:tx_result_fail). Acts as a
near-target for the `BPL`/`BNE` exits scattered through
[`nmi_reply_scout`](label:nmi_reply_scout),
[`nmi_reply_validate`](label:nmi_reply_validate), and
[`nmi_scout_ack_src`](label:nmi_scout_ack_src) that need to abort the
reply path – the unconditional `JMP` at `&8773` takes them to
[`tx_result_fail`](label:tx_result_fail) (which stores the error and
returns to idle).

Seven inbound refs in total (one `JSR` plus six branches).""",
)


d.comment(0x8842, "Store error and return to idle", align=Align.INLINE)
d.entry(0x8845)
d.subroutine(
    0x8845,
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


d.comment(0x8845, "Test SR2 RDA (bit7). Must be set for valid reply.", align=Align.INLINE)
d.comment(0x8848, "No RDA -- error (FV masking RDA via PSE would cause this)", align=Align.INLINE)
d.comment(0x884A, "Read source station", align=Align.INLINE)
d.comment(0x884D, "Compare to original TX destination station (&0D20)", align=Align.INLINE)
d.comment(0x8850, "Mismatch -- not the expected reply, error", align=Align.INLINE)
d.comment(0x8852, "Read source network", align=Align.INLINE)
d.comment(0x8855, "Compare to original TX destination network (&0D21)", align=Align.INLINE)
d.comment(0x8858, "Mismatch -- error", align=Align.INLINE)
d.comment(0x885A, "A=&02: FV mask for SR2 bit1", align=Align.INLINE)
d.comment(0x885C, "Test SR2 FV -- frame must be complete", align=Align.INLINE)
d.comment(0x885F, "No FV -- incomplete frame, error", align=Align.INLINE)
d.comment(0x8861, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", align=Align.INLINE)
d.comment(0x8863, "Write CR2: enable RTS for TX handshake", align=Align.INLINE)
d.comment(0x8866, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", align=Align.INLINE)
d.comment(0x8868, "Write CR1: reset RX, enable TX interrupt", align=Align.INLINE)
d.comment(0x886B, "Install handshake_await_ack into &0D43/&0D44 (four-way data phase)", align=Align.INLINE)
d.comment(0x886D, "High byte &88 of next handler address", align=Align.INLINE)
d.comment(0x886F, "Store low byte to nmi_next_lo", align=Align.INLINE)
d.comment(0x8872, "Store high byte to nmi_next_hi", align=Align.INLINE)
d.comment(0x8875, "Load dest station for scout ACK TX", align=Align.INLINE)
d.comment(0x8878, "Test SR1 TDRA (V=bit6)", align=Align.INLINE)
d.comment(0x887B, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x887D, "Write dest station to TX FIFO", align=Align.INLINE)
d.comment(0x8880, "Write dest network to TX FIFO", align=Align.INLINE)
d.comment(0x8883, "Write dest network to TX FIFO", align=Align.INLINE)
d.comment(0x8886, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8888, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x888A, "Set NMI vector and return", align=Align.INLINE)
d.entry(0x888D)
d.subroutine(
    0x888D,
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


d.comment(0x888D, "Load our station ID from workspace copy", align=Align.INLINE)
d.comment(0x8890, "Test SR1 TDRA", align=Align.INLINE)
d.label(0x8893, "tx_check_tdra_ready")

d.comment(0x8893, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x8895, "Write our station to TX FIFO", align=Align.INLINE)
d.comment(0x8898, "Write network=0 to TX FIFO", align=Align.INLINE)
d.comment(0x889A, "Write network byte to TX FIFO", align=Align.INLINE)
d.label(0x889D, "data_tx_begin")

d.subroutine(
    0x889D,
    "data_tx_begin",
    title="Begin data-frame TX: install nmi_data_tx or alt",
    description="""Tests bit 1 of [`net_frame_flags`](label:net_frame_flags)
([`tx_flags`](label:tx_flags)):

| Bit 1 | Path |
|---|---|
| set (immediate-op) | branch to `install_imm_data_nmi` to use the alternative handler |
| clear | install the [`nmi_data_tx`](label:nmi_data_tx) alt-entry at `&87EB` (lo=`&EB`, hi=`&87`) into the NMI vector. The alt-entry skips the page-counter check and goes straight to the byte-count load |

Single caller (`&8339` inside [`ack_tx`](label:ack_tx)).""",
)


d.comment(0x889D, "Test bit 1 of tx_flags", align=Align.INLINE)
d.comment(0x889F, "Check if immediate-op or data-transfer", align=Align.INLINE)
d.comment(0x88A2, "Bit 1 set: immediate op, use alt handler", align=Align.INLINE)
d.comment(0x88A4, "Install nmi_data_tx alt-entry (low)", align=Align.INLINE)
d.comment(0x88A6, "Y=&88: high byte of nmi_data_tx", align=Align.INLINE)
d.comment(0x88A8, "Install and return via set_nmi_vector", align=Align.INLINE)
d.label(0x88AB, "install_imm_data_nmi")

d.comment(0x88AB, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x88AD, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x88AF, "Install and return via set_nmi_vector", align=Align.INLINE)
d.entry(0x88B2)
d.subroutine(
    0x88B2,
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

The alt-entry at `&87EB` (used by
[`data_tx_begin`](label:data_tx_begin)) skips the page-counter check
and starts at the byte-count load.""",
)


d.comment(0x88B2, "Y = buffer offset, resume from last position", align=Align.INLINE)
d.comment(0x88B4, "No pages left: send final partial page", align=Align.INLINE)
d.comment(0x88B6, "Load remaining byte count", align=Align.INLINE)
d.comment(0x88B8, "Zero bytes left: skip to TDRA check", align=Align.INLINE)
d.comment(0x88BA, "Load remaining byte count (alt entry)", align=Align.INLINE)
d.comment(0x88BC, "Zero: loop back to top of handler", align=Align.INLINE)
d.label(0x88BE, "check_tdra_status")

d.comment(0x88BE, "Test SR1 TDRA (V=bit6)", align=Align.INLINE)
d.label(0x88C1, "data_tx_check_fifo")

d.comment(0x88C1, "TDRA not ready -- error", align=Align.INLINE)
d.comment(
    0x88C3,
    """Save/restore ACCCON across the (open_port_buf),Y reads
in this TX FIFO loop. Same idiom as copy_scout_to_buffer / nmi_data_rx_bulk;
workspace &97 holds the desired ACCCON value pre-loaded by the caller.""",
)
d.comment(0x88C3, "Save current ACCCON on stack", align=Align.INLINE)
d.comment(0x88C6, "Push ACCCON snapshot", align=Align.INLINE)
d.comment(0x88C7, "Load desired ACCCON from workspace &97", align=Align.INLINE)
d.comment(0x88C9, "Set ACCCON for the upcoming buffer reads", align=Align.INLINE)
d.comment(0x88CC, "Write data byte to TX FIFO", align=Align.INLINE)
d.comment(0x88CE, "Write first byte of pair to FIFO", align=Align.INLINE)
d.comment(0x88D1, "Advance buffer offset", align=Align.INLINE)
d.comment(0x88D2, "No page crossing", align=Align.INLINE)
d.comment(0x88D4, "Page crossing: decrement page count", align=Align.INLINE)
d.comment(0x88D6, "No pages left: send last data", align=Align.INLINE)
d.comment(0x88D8, "Increment buffer high byte", align=Align.INLINE)
d.label(0x88DA, "write_second_tx_byte")

d.comment(0x88DA, "Load second byte of pair", align=Align.INLINE)
d.comment(0x88DC, "Write second byte to FIFO", align=Align.INLINE)
d.comment(0x88DF, "Advance buffer offset", align=Align.INLINE)
d.comment(0x88E0, "Save updated buffer position", align=Align.INLINE)
d.comment(0x88E2, "No page crossing", align=Align.INLINE)
d.comment(0x88E4, "Page crossing: decrement page count", align=Align.INLINE)
d.comment(0x88E6, "No pages left: send last data", align=Align.INLINE)
d.comment(0x88E8, "Increment buffer high byte", align=Align.INLINE)
d.comment(0x88EA, "Pull saved ACCCON from stack", align=Align.INLINE)
d.label(0x88EA, "check_fifo_loop")

d.comment(0x88EB, "Restore caller's ACCCON between byte pairs", align=Align.INLINE)
d.label(0x88EE, "check_irq_loop")

d.comment(0x88EE, "Test ADLC SR1 IRQ flag for next byte pair", align=Align.INLINE)
d.comment(0x88F1, "IRQ still set: more bytes to send", align=Align.INLINE)
d.comment(0x88F3, "IRQ cleared: return from NMI", align=Align.INLINE)
d.comment(0x88F6, "Pull saved ACCCON (frame-end path)", align=Align.INLINE)
d.label(0x88F6, "frame_end_restore")

d.comment(0x88F7, "Restore caller's ACCCON before TX_LAST_DATA", align=Align.INLINE)
d.label(0x88FA, "data_tx_last")

d.comment(0x88FA, "CR2=&3F: TX_LAST_DATA (close data frame)", align=Align.INLINE)
d.comment(0x88FC, "Write CR2 to close frame", align=Align.INLINE)
d.comment(0x88FF, "Check tx_flags for next action", align=Align.INLINE)
d.comment(0x8902, "Bit7 clear: error, install saved handler", align=Align.INLINE)
d.comment(0x8904, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8906, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x8908, "Set NMI vector and return", align=Align.INLINE)
d.label(0x890B, "install_saved_handler")

d.comment(0x890B, "Load saved next handler low byte", align=Align.INLINE)
d.comment(0x890E, "Load saved next handler high byte", align=Align.INLINE)
d.comment(0x8911, "Install saved handler and return", align=Align.INLINE)
d.label(0x8914, "nmi_data_tx_tube")

d.entry(0x8914)
d.subroutine(
    0x8914,
    "nmi_data_tx_tube",
    title="NMI handler: TX FIFO write from Tube buffer",
    description="""NMI continuation handler used during TX of a Tube-sourced data
frame. Tests SR1 TDRA via `BIT
econet_control1_or_status1`, writes the next pair of bytes from
the Tube buffer to the ADLC TX FIFO (the `tube_tx_fifo_write`
shared body at `&8848`), and either continues the tight inner loop
on a continuing IRQ or returns via `RTI`. Reached only via the NMI
vector after [`tx_prepare`](label:tx_prepare) installs it.""",
)


d.comment(0x8914, "Tube TX: test SR1 TDRA", align=Align.INLINE)
d.label(0x8917, "tube_tx_fifo_write")

d.comment(0x8917, "TDRA not ready -- error", align=Align.INLINE)
d.comment(0x8919, "Read byte from Tube R3", align=Align.INLINE)
d.comment(0x891C, "Write to TX FIFO", align=Align.INLINE)
d.comment(0x891F, "Increment 4-byte buffer counter", align=Align.INLINE)
d.comment(0x8921, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x8923, "Carry into second byte", align=Align.INLINE)
d.comment(0x8925, "No further carry", align=Align.INLINE)
d.comment(0x8927, "Carry into third byte", align=Align.INLINE)
d.comment(0x8929, "No further carry", align=Align.INLINE)
d.comment(0x892B, "Carry into fourth byte", align=Align.INLINE)
d.comment(0x892D, "Counter wrapped to zero: last data", align=Align.INLINE)
d.label(0x892F, "write_second_tube_byte")

d.comment(0x892F, "Read second Tube byte from R3", align=Align.INLINE)
d.comment(0x8932, "Write second byte to TX FIFO", align=Align.INLINE)
d.comment(0x8935, "Increment 4-byte counter (second byte)", align=Align.INLINE)
d.comment(0x8937, "Low byte didn't wrap", align=Align.INLINE)
d.label(0x8939, "tube_tx_inc_byte2")

d.comment(0x8939, "Carry into second byte", align=Align.INLINE)
d.comment(0x893B, "No further carry", align=Align.INLINE)
d.label(0x893D, "tube_tx_inc_byte3")

d.comment(0x893D, "Carry into third byte", align=Align.INLINE)
d.label(0x85B9, "tx_length_table")

d.comment(0x893F, "No further carry", align=Align.INLINE)
d.label(0x8941, "tube_tx_inc_byte4")

d.comment(0x8941, "Carry into fourth byte", align=Align.INLINE)
d.comment(0x8943, "Counter wrapped to zero: last data", align=Align.INLINE)
d.label(0x8945, "check_tube_irq_loop")

d.comment(0x8945, "Test SR1 IRQ for tight loop", align=Align.INLINE)
d.label(0x85C1, "tx_flags_table")

d.comment(0x8948, "IRQ still set: write 2 more bytes", align=Align.INLINE)
d.comment(0x894A, "No IRQ: return, wait for next NMI", align=Align.INLINE)
d.label(0x894D, "tx_tdra_error")

d.comment(0x894D, "TX error: check flags for path", align=Align.INLINE)
d.comment(0x8950, "Bit7 clear: TX result = not listening", align=Align.INLINE)
d.comment(0x8952, "Bit7 set: discard and return to listen", align=Align.INLINE)
d.entry(0x8955)
d.subroutine(
    0x8955,
    "handshake_await_ack",
    title="Four-way handshake: switch to RX for final ACK",
    description="""Called via JMP from [`nmi_tx_complete`](label:nmi_tx_complete) when bit 0
of [`tx_flags`](label:tx_flags) is set (four-way handshake in
progress). Writes `CR1=&82` (`TX_RESET|RIE`) to switch the ADLC
from TX mode to RX mode, listening for the final ACK from the
remote station. Installs [`nmi_final_ack`](label:nmi_final_ack) as the
next NMI handler via [`set_nmi_vector`](label:set_nmi_vector).""",
)


d.comment(0x8955, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", align=Align.INLINE)
d.comment(0x8957, "Write to ADLC CR1", align=Align.INLINE)
d.comment(0x895A, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x895C, "Next NMI handler address (high)", align=Align.INLINE)
d.comment(0x895E, "Install and return via set_nmi_vector", align=Align.INLINE)
d.entry(0x8961)
d.subroutine(
    0x8961,
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


d.comment(0x8961, "A=&01: AP mask", align=Align.INLINE)
d.comment(0x8963, "Test SR2 AP", align=Align.INLINE)
d.comment(0x8966, "No AP -- error", align=Align.INLINE)
d.comment(0x8968, "Read dest station", align=Align.INLINE)
d.comment(0x896B, "Compare to our station (workspace copy)", align=Align.INLINE)
d.comment(0x896E, "Not our station -- error", align=Align.INLINE)
d.comment(0x8970, "Next NMI handler address (low)", align=Align.INLINE)
d.comment(0x8972, "Install continuation handler", align=Align.INLINE)
d.label(0x8975, "nmi_final_ack_net")

d.entry(0x8975)
d.subroutine(
    0x8975,
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


d.comment(0x8975, "Test SR2 RDA", align=Align.INLINE)
d.comment(0x8978, "No RDA -- error", align=Align.INLINE)
d.comment(0x897A, "Read dest network", align=Align.INLINE)
d.comment(0x897D, "Non-zero -- network mismatch, error", align=Align.INLINE)
d.comment(0x897F, "Install nmi_final_ack_validate handler", align=Align.INLINE)
d.comment(0x8981, "Test SR1 IRQ -- more data ready?", align=Align.INLINE)
d.comment(0x8984, "IRQ set -- fall through to validate", align=Align.INLINE)
d.comment(0x8986, "Install handler", align=Align.INLINE)
d.entry(0x8989)
d.subroutine(
    0x8989,
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


d.comment(0x8989, "Test SR2 RDA", align=Align.INLINE)
d.comment(0x898C, "No RDA -- error", align=Align.INLINE)
d.comment(0x898E, "Read source station", align=Align.INLINE)
d.comment(0x8991, "Compare to TX dest station (&0D20)", align=Align.INLINE)
d.comment(0x8994, "Mismatch -- error", align=Align.INLINE)
d.comment(0x8996, "Read source network", align=Align.INLINE)
d.comment(0x8999, "Compare to TX dest network (&0D21)", align=Align.INLINE)
d.comment(0x899C, "Mismatch -- error", align=Align.INLINE)
d.comment(0x899E, "Load TX flags for next action", align=Align.INLINE)
d.comment(0x89A1, "bit7 clear: no data phase", align=Align.INLINE)
d.comment(0x89A3, "Install data RX handler", align=Align.INLINE)
d.label(0x89A6, "check_fv_final_ack")

d.comment(0x89A6, "A=&02: FV mask for SR2 bit1", align=Align.INLINE)
d.comment(0x89A8, "Test SR2 FV -- frame must be complete", align=Align.INLINE)
d.comment(0x89AB, "No FV -- error", align=Align.INLINE)
d.entry(0x89AD)
d.subroutine(
    0x89AD,
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


d.comment(0x89AD, "A=0: success result code", align=Align.INLINE)
d.comment(0x89AF, "Always taken (A=0)", align=Align.INLINE)
d.label(0x89B1, "tx_result_fail")

d.subroutine(
    0x89B1,
    "tx_result_fail",
    title="TX failure: not listening",
    description="""Loads error code `&41` ("not listening") and falls through to
[`tx_store_result`](label:tx_store_result). The most common TX-error
path – reached from 11 sites across the final-ACK validation
chain when the remote station doesn't respond or the frame is
malformed.""",
    on_exit={"a": "&41 ('not listening' TX error)"},
)


d.comment(0x89B1, "A=&41: not listening error code", align=Align.INLINE)
d.entry(0x89B3)
d.subroutine(
    0x89B3,
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


d.comment(0x89B3, "Y=0: index into TX control block", align=Align.INLINE)
d.comment(0x89B5, "Store result/error code at (nmi_tx_block),0", align=Align.INLINE)
d.comment(0x89B7, "A=&80: TX-complete signal for tx_complete_flag", align=Align.INLINE)
d.comment(0x89B9, "Signal TX complete", align=Align.INLINE)
d.comment(0x89BC, "Full ADLC reset and return to idle listen", align=Align.INLINE)


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


d.comment(0x85AE, "Read ACCCON (access-control register)", align=Align.INLINE)
d.comment(0x85B1, "Set bit 3 of A (transfer-mode flag)", align=Align.INLINE)
d.comment(0x85B3, "Store as escapable mode", align=Align.INLINE)
d.comment(0x85B5, "Y=7: scout-bytes counter", align=Align.INLINE)
d.comment(0x85B7, "Read RXCB[7] (buffer addr high byte)", align=Align.INLINE)
d.comment(0x85B9, "Compare to &FF", align=Align.INLINE)
d.comment(0x85BB, "Not &FF: normal buffer, skip Tube check", align=Align.INLINE)
d.comment(0x85BE, "Read RXCB[6] (buffer addr byte 2)", align=Align.INLINE)
d.comment(0x85C0, "Check if addr byte 2 >= &FE (Tube range)", align=Align.INLINE)
d.comment(0x85C2, "C clear: no Tube, plain transfer path", align=Align.INLINE)
d.comment(0x85C4, "Z clear (other state set): use fallback path", align=Align.INLINE)
d.comment(0x85C6, "Z set: re-read ACCCON for second decision", align=Align.INLINE)
d.comment(0x85C9, "Rotate bit 0 (E flag) into C", align=Align.INLINE)
d.comment(0x85CA, "C clear: shadow not enabled, fallback path", align=Align.INLINE)
d.comment(0x85CC, "Shadow enabled: set bit 2 of escapable", align=Align.INLINE)
d.comment(0x85CE, "Atomic bit-set on escapable", align=Align.INLINE)
d.comment(0x85D0, "Branch to fallback_calc_transfer (always)", align=Align.INLINE)
d.label(0x85D0, "shadow_enable_flag")

d.label(0x85D2, "check_tx_in_progress")

d.comment(0x85D2, "Transmit in progress?", align=Align.INLINE)
d.comment(0x85D5, "No: fallback path", align=Align.INLINE)
d.comment(0x85D7, "Load TX flags for transfer setup", align=Align.INLINE)
d.comment(0x85DA, "Set bit 1 (transfer complete)", align=Align.INLINE)
d.comment(0x85DC, "Store with bit 1 set (Tube xfer)", align=Align.INLINE)
d.comment(0x85DF, "Init borrow for 4-byte subtract", align=Align.INLINE)
d.comment(0x85E0, "Save carry on stack", align=Align.INLINE)
d.comment(0x85E1, "Y=4: start at RXCB offset 4", align=Align.INLINE)
d.label(0x85E3, "calc_transfer_size")

d.comment(0x85E3, "Load RXCB[Y] (current ptr byte)", align=Align.INLINE)
d.comment(0x85E5, "Y += 4: advance to RXCB[Y+4]", align=Align.INLINE)
d.comment(0x85E6, "(continued)", align=Align.INLINE)
d.comment(0x85E7, "(continued)", align=Align.INLINE)
d.comment(0x85E8, "(continued)", align=Align.INLINE)
d.comment(0x85E9, "Restore borrow from previous byte", align=Align.INLINE)
d.comment(0x85EA, "Subtract RXCB[Y+4] (start ptr byte)", align=Align.INLINE)
d.comment(0x85EC, "Store result byte", align=Align.INLINE)
d.comment(0x85EF, "Y -= 3: next source byte", align=Align.INLINE)
d.comment(0x85F0, "(continued)", align=Align.INLINE)
d.comment(0x85F1, "(continued)", align=Align.INLINE)
d.comment(0x85F2, "Save borrow for next byte", align=Align.INLINE)
d.comment(0x85F3, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0x85F5, "No: next byte pair", align=Align.INLINE)
d.comment(0x85F7, "Discard final borrow", align=Align.INLINE)
d.comment(0x85F8, "Save X", align=Align.INLINE)
d.comment(0x85F9, "Save X", align=Align.INLINE)
d.comment(0x85FA, "Compute address of RXCB+4", align=Align.INLINE)
d.comment(0x85FC, "For base pointer addition", align=Align.INLINE)
d.comment(0x85FD, "Add RXCB base to get RXCB+4 addr", align=Align.INLINE)
d.comment(0x85FF, "X = low byte of RXCB+4", align=Align.INLINE)
d.comment(0x8600, "Y = high byte of RXCB ptr", align=Align.INLINE)
d.comment(0x8602, "Tube claim type &C2", align=Align.INLINE)
d.comment(0x8604, "Claim Tube transfer address", align=Align.INLINE)
d.comment(0x8607, "No Tube: skip reclaim", align=Align.INLINE)
d.comment(0x8609, "Tube: reclaim with scout status", align=Align.INLINE)
d.comment(0x860C, "Reclaim with scout status type", align=Align.INLINE)
d.comment(0x860F, "Release Tube claim after reclaim", align=Align.INLINE)
d.comment(0x8612, "C=1: Tube address claimed", align=Align.INLINE)
d.label(0x8613, "restore_x_and_return")

d.comment(0x8613, "Restore X", align=Align.INLINE)
d.comment(0x8614, "Restore X from stack", align=Align.INLINE)
d.comment(0x8615, "Return with C = transfer status", align=Align.INLINE)
d.label(0x8616, "fallback_calc_transfer")

d.entry(0x8616)
d.comment(0x8616, "Y=4: RXCB current pointer offset", align=Align.INLINE)
d.comment(0x8618, "Load RXCB[4] (current ptr lo)", align=Align.INLINE)
d.comment(0x861A, "Y=8: RXCB start address offset", align=Align.INLINE)
d.comment(0x861C, "Set carry for subtraction", align=Align.INLINE)
d.comment(0x861D, "Subtract RXCB[8] (start ptr lo)", align=Align.INLINE)
d.comment(0x861F, "Store transfer size lo", align=Align.INLINE)
d.comment(0x8621, "Y=5: current ptr hi offset", align=Align.INLINE)
d.comment(0x8623, "Load RXCB[5] (current ptr hi)", align=Align.INLINE)
d.comment(0x8625, "Propagate borrow only", align=Align.INLINE)
d.comment(0x8627, "Temp store of adjusted hi byte", align=Align.INLINE)
d.comment(0x8629, "Y=8: start address lo offset", align=Align.INLINE)
d.comment(0x862B, "Copy RXCB[8] to open port buffer lo", align=Align.INLINE)
d.comment(0x862D, "Store to scratch (side effect)", align=Align.INLINE)
d.comment(0x862F, "Y=9: start address hi offset", align=Align.INLINE)
d.comment(0x8631, "Load RXCB[9]", align=Align.INLINE)
d.comment(0x8633, "Set carry for subtraction", align=Align.INLINE)
d.comment(0x8634, "Subtract adjusted hi byte", align=Align.INLINE)
d.comment(0x8636, "Store transfer size hi", align=Align.INLINE)
d.comment(0x8638, "Return with C=1", align=Align.INLINE)
d.label(0x8639, "nmi_shim_rom_src")

d.comment(0x8639, "Return with C=1 (success)", align=Align.INLINE)
d.subroutine(
    0x89BF,
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


d.comment(0x89BF, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", align=Align.INLINE)
d.comment(0x89C1, "Write CR1 to ADLC register 0", align=Align.INLINE)
d.comment(0x89C4, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", align=Align.INLINE)
d.comment(0x89C6, "Write CR4 to ADLC register 3", align=Align.INLINE)
d.comment(0x89C9, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", align=Align.INLINE)
d.comment(0x89CB, "Write CR3 to ADLC register 1", align=Align.INLINE)
d.subroutine(
    0x89CE,
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


d.comment(0x89CE, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", align=Align.INLINE)
d.comment(0x89D0, "Write to ADLC CR1", align=Align.INLINE)
d.comment(0x89D3, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", align=Align.INLINE)
d.comment(0x89D5, "Write to ADLC CR2", align=Align.INLINE)
d.comment(0x89D8, "Return; ADLC now in RX listen mode", align=Align.INLINE)
d.label(0x89D9, "wait_idle_and_reset")

d.subroutine(
    0x89D9,
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


d.comment(0x89D9, "Check if Econet has been initialised", align=Align.INLINE)
d.comment(0x89DC, "Not initialised: skip to RX listen", align=Align.INLINE)
d.label(0x89DE, "poll_nmi_idle")

d.comment(0x89DE, "Read current NMI handler low byte", align=Align.INLINE)
d.comment(0x89E1, "Expected: &B3 (nmi_rx_scout low)", align=Align.INLINE)
d.comment(0x89E3, "Not idle: spin and wait", align=Align.INLINE)
d.comment(0x89E5, "Read current NMI handler high byte", align=Align.INLINE)
# UNMAPPED: d.comment(0x89B5, "Test if high byte = &80 (page of nmi_rx_scout)", align=Align.INLINE)
d.comment(0x89EA, "Not idle: spin and wait", align=Align.INLINE)
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


d.comment(0x89F1, "INTOFF: disable NMIs", align=Align.INLINE)
# UNMAPPED: d.comment(0x89BC, "INTOFF again (belt-and-braces)", align=Align.INLINE)
d.comment(0x89F6, "TX not in progress", align=Align.INLINE)
d.comment(0x89F9, "Econet not initialised", align=Align.INLINE)
d.comment(0x89FC, "Y=5: service call workspace page", align=Align.INLINE)
d.label(0x89FE, "reset_enter_listen")
d.comment(0x89FE, "Set ADLC to RX listen mode", align=Align.INLINE)
d.label(0x8A00, "nmi_shim_source")

d.entry(0x8A01)
d.subroutine(
    0x8A01,
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


d.comment(0x8A01, "INTOFF: force /NMI high (clear NMI flip-flop)", align=Align.INLINE)
d.comment(0x8A04, "Save A", align=Align.INLINE)
d.comment(0x8A05, "Transfer Y to A", align=Align.INLINE)
d.comment(0x8A06, "Save Y (via A)", align=Align.INLINE)
d.comment(0x8A07, "ROM bank 0 (patched during init for actual bank)", align=Align.INLINE)
d.comment(0x8A09, "Select Econet ROM bank via ROMSEL", align=Align.INLINE)
d.comment(0x8A0C, "Jump to scout handler in ROM", align=Align.INLINE)
d.entry(0x8A0F)


d.subroutine(
    0x8A0F,
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


d.comment(0x8A0F, "Store handler high byte at &0D0D", align=Align.INLINE)
d.comment(0x8A12, "Store handler low byte at &0D0C", align=Align.INLINE)
d.comment(0x8A15, "Restore NFS ROM bank", align=Align.INLINE)
d.comment(0x8A17, "Page in via hardware latch", align=Align.INLINE)
d.comment(0x8A1A, "Restore Y from stack", align=Align.INLINE)
d.comment(0x8A1B, "Transfer ROM bank to Y", align=Align.INLINE)
d.comment(0x8A1C, "Restore A from stack", align=Align.INLINE)
d.comment(0x8A1D, "INTON: guaranteed /NMI edge if ADLC IRQ asserted", align=Align.INLINE)
d.comment(0x8A20, "Return from interrupt", align=Align.INLINE)
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
# UNMAPPED: [`svc_dispatch`](label:svc_dispatch) as `LDA &8A20,X`. The
# UNMAPPED: dispatcher pushes the hi byte first then the lo, so `RTS` lands
# UNMAPPED: on `target` (the table stores `target-1`). The trailing byte at
# UNMAPPED: `&8A53` is 1-byte padding – there are only 51 valid entries
# UNMAPPED: (0..50).""",
# UNMAPPED: )
# UNMAPPED: for addr in range(0x8A20, 0x8A54):
# UNMAPPED (orphan body):     d.byte(addr)
# UNMAPPED: d.comment(0x8A53, "padding (table has only 51 entries)", align=Align.INLINE)


d.subroutine(
    0x8A8A,
    "service_handler",
    title="Service call dispatch",
    description="""Handles service calls 1, 4, 8, 9, 13, 14, and 15.

| Call | Meaning                          |
|-----:|----------------------------------|
|    1 | Absolute workspace claim         |
|    4 | Unrecognised `*` command         |
|    8 | Unrecognised OSWORD              |
|    9 | `*HELP`                          |
|   13 | ROM initialisation               |
|   14 | ROM initialisation complete      |
|   15 | Vectors claimed                  |

On service 15 the ROM verifies the host OS via OSBYTE 0 with the
input `X=1`, which returns the OS version code:

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

d.comment(0x8A8A, "Save service call number", align=Align.INLINE)
d.comment(0x8A8B, "Service call &0F (vectors claimed)?", align=Align.INLINE)
d.comment(0x8A8D, "No: skip vectors-claimed handling", align=Align.INLINE)
d.comment(0x8A8F, "Save Y on stack across the version-check", align=Align.INLINE)
d.comment(0x8A90, "OSBYTE 0: read OS version", align=Align.INLINE)
d.comment(0x8A92, "X=1 to request version number", align=Align.INLINE)
d.comment(0x8A9D, "OS 3.2/3.5 (Master 128)?", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A63, "Yes: target OS, skip Bad ROM message", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A65, "OS 4.0 (Master Econet Terminal)?", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A67, "Yes: target OS, skip Bad ROM message", align=Align.INLINE)
d.comment(0x8AA1, "Transfer OS version to A", align=Align.INLINE)
d.comment(0x8AA2, "Save flags (Z set if OS 1.00) across print", align=Align.INLINE)
d.comment(0x8AA3, "Print '<CR>Bad ROM ' to mark non-Master OS", align=Align.INLINE)
d.comment(0x8AA6, "svc 13 fail path", align=Align.INLINE)
d.comment(0x8AAF, "Load this ROM's slot number", align=Align.INLINE)
d.comment(0x8AB1, "Print slot number as decimal", align=Align.INLINE)
d.comment(0x8AB4, "Print trailing newline, bypassing *SPOOL", align=Align.INLINE)
d.comment(0x8AB7, "Reload ROM slot for workspace clearing", align=Align.INLINE)
d.comment(0x8AB9, "Restore flags", align=Align.INLINE)
d.comment(0x8ABA, "OS 1.00: skip INX (table starts at slot 0)", align=Align.INLINE)
d.comment(0x8ABC, "Adjust index for OS 1.20/2.00/5.00 layout", align=Align.INLINE)
d.label(0x8ABD, "clear_workspace_byte")

d.comment(0x8ABD, "A=0", align=Align.INLINE)
d.comment(0x8ABF, "Clear workspace byte for this ROM", align=Align.INLINE)
d.label(0x8AC2, "restore_rom_slot")

d.comment(0x8AC2, "Restore ROM slot to X", align=Align.INLINE)
d.comment(0x8AC4, "Restore Y from stack", align=Align.INLINE)
d.comment(0x8AC5, "Pop service call number into A", align=Align.INLINE)
d.label(0x8AC5, "restore_rom_slot_entry")

d.comment(0x8AC6, "Re-save service call number", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A8F, "Service call &24 (Dynamic Workspace requirements)?", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A91, "No: skip ADLC check", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A93, "Read ADLC status register 1", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A96, "Mask relevant status bits", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A98, "Non-zero: ADLC absent, set flag", align=Align.INLINE)
# UNMAPPED: d.label(0x8A9A, "set_adlc_absent")

# UNMAPPED: d.comment(0x8A9A, "Shift bit 7 into carry", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A9D, "Set carry to mark ADLC absent", align=Align.INLINE)
# UNMAPPED: d.comment(0x8A9E, "Rotate carry into bit 7 of slot flag", align=Align.INLINE)
d.label(0x8AC7, "check_adlc_flag")

d.comment(0x8AC7, "Load ROM slot flag byte", align=Align.INLINE)
d.comment(0x8ACA, "Shift bit 7 (ADLC absent) into carry", align=Align.INLINE)
d.comment(0x8ACB, "Restore service call number", align=Align.INLINE)
d.comment(0x8ACC, "ADLC present: continue dispatch", align=Align.INLINE)
d.comment(0x8ACE, "ADLC absent: decline service, return", align=Align.INLINE)
d.label(0x8ACF, "dispatch_svc_with_state")

d.comment(0x8ACF, "Transfer service number to X", align=Align.INLINE)
d.comment(0x8AD0, "Save current service state", align=Align.INLINE)
d.comment(0x8AD2, "Push old state", align=Align.INLINE)
d.comment(0x8AD3, "Restore service number to A", align=Align.INLINE)
d.comment(0x8AD4, "Store as current service state", align=Align.INLINE)
d.comment(0x8AD6, "Service < 13?", align=Align.INLINE)
d.comment(0x8AD8, "Yes: use as dispatch index directly", align=Align.INLINE)
d.comment(0x8ADA, "Subtract 5 (map 13-17 to 8-12)", align=Align.INLINE)
d.comment(0x8ADC, "Mapped value = 13? (original was 18)", align=Align.INLINE)
d.comment(0x8ADE, "Yes: valid service 18 (FS select)", align=Align.INLINE)
d.comment(
    0x8AE0, "C clear: service number was below the prior CMP threshold, take dispatch fall-through", align=Align.INLINE
)
d.comment(0x8AE2, "Subtract 5 to remap service range", align=Align.INLINE)
d.comment(0x8AE4, "Compare with &0E", align=Align.INLINE)
d.comment(0x8AE6, "Equal: dispatch directly", align=Align.INLINE)
d.comment(0x8AE8, "Below: take dispatch fall-through", align=Align.INLINE)
d.comment(0x8AEA, "Subtract 8 to remap further", align=Align.INLINE)
d.comment(0x8AEC, "Compare with &0F", align=Align.INLINE)
d.comment(0x8AEE, "Below: dispatch fall-through", align=Align.INLINE)
d.comment(0x8AF0, "Compare with &18", align=Align.INLINE)
d.comment(0x8AF2, "Below: dispatch index now in A", align=Align.INLINE)
d.label(0x8AF4, "dispatch_svc_state_check")

d.comment(0x8AF4, "Unknown service: set index to 0", align=Align.INLINE)
d.label(0x8AF6, "dispatch_svc_index")

d.comment(0x8AF6, "Transfer dispatch index to X", align=Align.INLINE)
d.comment(0x8AF7, "Index 0: unhandled service, skip", align=Align.INLINE)
d.comment(0x8AF9, "Save current workspace page", align=Align.INLINE)
d.comment(0x8AFB, "Push old page", align=Align.INLINE)
d.comment(0x8AFC, "Set workspace page from Y parameter", align=Align.INLINE)
d.comment(0x8AFE, "Transfer Y to A", align=Align.INLINE)
d.comment(0x8AFF, "Y=0 for dispatch offset", align=Align.INLINE)
d.comment(0x8B01, "Dispatch to service handler via table", align=Align.INLINE)
d.comment(0x8B04, "Restore old workspace page", align=Align.INLINE)
d.comment(0x8B05, "Store it back", align=Align.INLINE)
d.label(0x8B07, "restore_svc_state")

d.comment(0x8B07, "Get service state (return code)", align=Align.INLINE)
d.comment(0x8B09, "Restore old service state", align=Align.INLINE)
d.comment(0x8B0A, "Store it back", align=Align.INLINE)
d.comment(0x8B0C, "Transfer return code to A", align=Align.INLINE)
d.label(0x8B0D, "restore_romsel_rts")

d.comment(0x8B0D, "Restore ROM slot to X", align=Align.INLINE)
d.comment(0x8B0F, "Return to MOS", align=Align.INLINE)
d.comment(0x8B10, "Offset 0 in receive block", align=Align.INLINE)
d.entry(0x8B10)
d.label(0x8B10, "cmd_roff")


d.subroutine(
    0x8B10,
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
d.comment(0x8B12, "Load remote operation flag", align=Align.INLINE)
d.comment(0x8B14, "Zero: already off, skip to cleanup", align=Align.INLINE)
d.comment(0x8B16, "A=0", align=Align.INLINE)
d.comment(0x8B19, "Clear remote operation flag", align=Align.INLINE)
d.comment(0x8B1C, "OSBYTE &C9: keyboard disable", align=Align.INLINE)
d.comment(0x8B21, "A=&0A: workspace init parameter", align=Align.INLINE)
d.comment(0x8B23, "Initialise workspace area", align=Align.INLINE)
d.label(0x8B26, "scan_remote_keys")

d.subroutine(
    0x8B26,
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


d.comment(0x8B26, "Save X in workspace", align=Align.INLINE)
d.comment(0x8B28, "A=&CE: start of key range", align=Align.INLINE)
d.label(0x8B2A, "loop_scan_key_range")

d.comment(0x8B2A, "Restore X from workspace", align=Align.INLINE)
d.comment(0x8B2C, "Y=&7F: OSBYTE scan parameter", align=Align.INLINE)
d.comment(0x8B2E, "OSBYTE: scan keyboard", align=Align.INLINE)
d.comment(0x8B31, "Advance to next key code", align=Align.INLINE)
d.comment(0x8B33, "Reached &D0?", align=Align.INLINE)
d.comment(0x8B35, "No: loop back (scan &CE and &CF)", align=Align.INLINE)
d.label(0x8B37, "clear_svc_and_ws")

d.comment(0x8B37, "A=0", align=Align.INLINE)
d.comment(0x8B39, "Clear service state", align=Align.INLINE)
d.comment(0x8B3B, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8B3D, "Return", align=Align.INLINE)
d.label(0x8B3E, "save_text_ptr")

d.subroutine(
    0x8B3E,
    "save_text_ptr",
    title="Save OS text pointer for later retrieval",
    description="""Copies `&F2`/`&F3` (`os_text_ptr`) into `fs_crc_lo` /
`fs_crc_hi`. Called by [`svc_4_star_command`](label:svc_4_star_command)
and [`svc_9_help`](label:svc_9_help) before attempting command
matches, and by `match_fs_cmd` during iterative help-topic
matching. Preserves `A` via `PHA`/`PLA`.""",
    on_exit={"a": "preserved"},
)


d.comment(0x8B3E, "Save A", align=Align.INLINE)
d.comment(0x8B3F, "Copy OS text pointer low", align=Align.INLINE)
d.comment(0x8B41, "to fs_crc_lo", align=Align.INLINE)
d.comment(0x8B43, "Copy OS text pointer high", align=Align.INLINE)
d.comment(0x8B45, "to fs_crc_hi", align=Align.INLINE)
d.comment(0x8B47, "Restore A", align=Align.INLINE)
d.label(0x8B48, "rts_save_text_ptr")

d.comment(0x8B48, "Return", align=Align.INLINE)
d.comment(0x8B49, "Get workspace page for this ROM slot", align=Align.INLINE)
d.label(0x8B49, "cmd_net_fs")

d.subroutine(
    0x8B49,
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


d.comment(0x8B4C, "Store as high byte of load address", align=Align.INLINE)
d.comment(0x8B4E, "A=0", align=Align.INLINE)
d.comment(0x8B50, "Clear low byte of load address", align=Align.INLINE)
d.comment(0x8B52, "Clear carry for addition", align=Align.INLINE)
d.comment(0x8B53, "Y=&76: checksum range end", align=Align.INLINE)
d.label(0x8B55, "loop_sum_rom_bytes")

d.comment(0x8B55, "Add byte to running checksum", align=Align.INLINE)
d.comment(0x8B57, "Decrement index", align=Align.INLINE)
d.comment(0x8B58, "Loop until all bytes summed", align=Align.INLINE)
d.comment(0x8B5A, "Y=&77: checksum storage offset", align=Align.INLINE)
d.comment(0x8B5C, "Compare with stored checksum", align=Align.INLINE)
d.comment(0x8B5E, "Return -- last instruction of cmd_net_fs body", align=Align.INLINE)
d.comment(0x8B5F, "A=&20: ADLC IRQ-status mask (CR2 bit 5)", align=Align.INLINE)
d.entry(0x8B5F)

d.label(0x8B5F, "cmd_net_check_hw")
d.comment(0x8B61, "Read ADLC CR2/SR2 (&FEA1)", align=Align.INLINE)
d.comment(0x8B64, "Z set (no carrier): proceed to FS-select", align=Align.INLINE)
d.comment(0x8B66, "A=3: 'ROM has no NFS' error code", align=Align.INLINE)
d.comment(0x8B68, "Raise via build_simple_error (never returns)", align=Align.INLINE)
d.comment(0x8B6B, "Service 18 carries FS number in Y; Econet is FS 5", align=Align.INLINE)
d.entry(0x8B6B)


d.subroutine(
    0x8B6B,
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
d.comment(0x8B6D, "Not us: pass the call on (RTS via shared return)", align=Align.INLINE)
d.comment(0x8B6F, "A=0 to claim the service", align=Align.INLINE)
d.comment(0x8B71, "Clear svc_state and fall into ensure_fs_selected", align=Align.INLINE)
d.subroutine(
    0x8B73,
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


d.comment(0x8B73, "Test fs_flags bit 7 (ANFS active)", align=Align.INLINE)
d.comment(0x8B76, "Already active: tail-RTS via shared exit", align=Align.INLINE)
d.comment(0x8B78, "Auto-select ANFS via the *NFS handler", align=Align.INLINE)
d.subroutine(
    0x8B78,
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


d.comment(0x8B7B, "Z=1 (A=0): selection succeeded", align=Align.INLINE)
d.comment(0x8B7D, "Otherwise raise 'net checksum' error", align=Align.INLINE)
d.comment(0x8B80, "Read osword_pb_ptr_hi", align=Align.INLINE)
d.label(0x8B80, "select_fs_cmd_net_fs")

d.comment(0x8B82, "Push it", align=Align.INLINE)
d.comment(0x8B83, "Read osword_pb_ptr lo", align=Align.INLINE)
d.comment(0x8B85, "Push it", align=Align.INLINE)
d.label(0x8B86, "done_rom_checksum")

d.comment(0x8B86, "Call FSCV with A=6 (new FS)", align=Align.INLINE)
d.comment(0x8B89, "Y=9: end of FS context block", align=Align.INLINE)
d.label(0x8B8B, "loop_copy_fs_ctx")

d.comment(0x8B8B, "Load byte from receive block", align=Align.INLINE)
d.comment(0x8B8D, "Store into FS workspace", align=Align.INLINE)
d.comment(0x8B90, "Decrement index", align=Align.INLINE)
d.comment(0x8B91, "Reached offset 1?", align=Align.INLINE)
d.comment(0x8B93, "No: continue copying", align=Align.INLINE)
d.comment(0x8B95, "Shift bit 7 of FS flags into carry", align=Align.INLINE)
d.comment(0x8B98, "Clear carry", align=Align.INLINE)
d.comment(0x8B99, "Clear bit 7 of FS flags", align=Align.INLINE)
d.comment(0x8B9C, "Y=&0D: vector table size - 1", align=Align.INLINE)
d.label(0x8B9E, "loop_set_vectors")

d.comment(0x8B9E, "Load FS vector address", align=Align.INLINE)
d.comment(0x8BA1, "Store into FILEV vector table", align=Align.INLINE)
d.comment(0x8BA4, "Decrement index", align=Align.INLINE)
d.comment(0x8BA5, "Loop until all vectors installed", align=Align.INLINE)
d.comment(0x8BA7, "Initialise ADLC and NMI workspace", align=Align.INLINE)
d.comment(0x8BAA, "Y=&1B: extended vector offset", align=Align.INLINE)
d.comment(0x8BAC, "X=7: two more vectors to set up", align=Align.INLINE)
d.comment(0x8BAE, "Set up extended vectors", align=Align.INLINE)
d.comment(0x8BB1, "A=0", align=Align.INLINE)
d.comment(0x8BB3, "Clear FS state byte", align=Align.INLINE)
d.comment(0x8BB6, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8BB9, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8BBC, "Clear receive attribute byte", align=Align.INLINE)
d.comment(0x8BBF, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8BC2, "Set up workspace pointers", align=Align.INLINE)
d.comment(0x8BC5, "Initialise FS state", align=Align.INLINE)
d.comment(0x8BC8, "Y=&77: workspace block size - 1", align=Align.INLINE)
d.label(0x8BCA, "loop_copy_ws_page")

d.comment(0x8BCA, "Load byte from source workspace", align=Align.INLINE)
d.comment(0x8BCC, "Store to the HAZEL &C2 FCB shadow copy", align=Align.INLINE)
d.comment(0x8BCF, "Decrement index", align=Align.INLINE)
d.comment(0x8BD0, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x8BD2, "A=&80: FS selected flag", align=Align.INLINE)
d.comment(0x8BD4, "Set bit 0 of fs_flags (= NFS active)", align=Align.INLINE)
d.comment(0x8BD7, "Issue Master service call &0F (vector update)", align=Align.INLINE)
d.comment(0x8BDA, "Pop saved osword_pb_ptr lo", align=Align.INLINE)
d.comment(0x8BDB, "Restore osword_pb_ptr lo", align=Align.INLINE)
d.comment(0x8BDD, "Pop saved osword_pb_ptr hi", align=Align.INLINE)
d.comment(0x8BDE, "Restore osword_pb_ptr hi", align=Align.INLINE)
d.comment(0x8BE0, "Return", align=Align.INLINE)
d.label(0x8BE1, "help_print_nfs_cmds")

d.subroutine(
    0x8BE1,
    "help_print_nfs_cmds",
    title="*HELP NFS topic: print NFS-specific commands",
    description="""Loads `X=&35` (the offset of the first NFS-specific command in
`cmd_table_fs`) and tail-falls into
[`print_cmd_table`](label:print_cmd_table) to emit the listing. Single
caller (the `*HELP` topic dispatch at `&8C6E`).""",
    on_exit={"x": "&35 + advance through the table"},
)


d.comment(0x8BE1, "X=&35: NFS command table offset", align=Align.INLINE)
d.comment(0x8BE3, "Print help for NFS commands", align=Align.INLINE)
d.comment(0x8BE6, "X=0: utility command table offset", align=Align.INLINE)
d.entry(0x8BE6)

d.label(0x8BE6, "help_utils")


d.subroutine(
    0x8BE6,
    "help_utils",
    title="*HELP UTILS topic handler",
    description="""Sets `X = 0` to select the utility command sub-table and branches
to [`print_cmd_table`](label:print_cmd_table) to display the command
list. Prints the version header followed by all utility
commands.""",
    on_entry={"y": "command-line offset (PHA/PHA/RTS dispatch contract)"},
    on_exit={"a, x, y": "clobbered"},
)
d.comment(0x8BEA, "X=&35: NFS command table offset", align=Align.INLINE)
d.entry(0x8BEA)
d.label(0x8BEA, "help_net")

d.subroutine(
    0x8BEA,
    "help_net",
    title="*HELP NET topic handler",
    description="""Sets `X = &35` (the NFS command sub-table offset) and falls
through to [`print_cmd_table`](label:print_cmd_table) to display the
NFS command list with version header.""",
    on_entry={"y": "command-line offset (PHA/PHA/RTS dispatch contract)"},
    on_exit={"a, x, y": "clobbered (print_cmd_table)"},
)


d.label(0x8BEC, "print_cmd_table")

d.subroutine(
    0x8BEC,
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


d.comment(0x8BEC, "V clear: take newline-only path (skip version header)", align=Align.INLINE)
d.comment(0x8BEE, "Save X (cmd-table offset)", align=Align.INLINE)
d.comment(0x8BEF, "Save Y (text-pointer offset)", align=Align.INLINE)
d.comment(0x8BF0, "Print the version-banner header", align=Align.INLINE)
d.comment(0x8BF5, "Clear overflow flag", align=Align.INLINE)
d.label(0x8BF8, "print_table_newline")

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
d.comment(0x8BFC, "Save processor status", align=Align.INLINE)
d.label(0x8BFD, "loop_next_entry")

d.subroutine(
    0x8BFD,
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


d.comment(0x8BFD, "Load byte from command table", align=Align.INLINE)
d.comment(0x8C00, "Bit 7 clear: valid entry, continue", align=Align.INLINE)
d.comment(0x8C02, "End of table: finish up", align=Align.INLINE)
d.label(0x8C05, "print_indent")

d.comment(0x8C05, "Print two-space indent", align=Align.INLINE)
d.comment(0x8C0A, "Y=9: cmd_table_fs sub-table 1 offset", align=Align.INLINE)
# UNMAPPED: d.comment(0x8BE7, "Read cmd_table_fs+X (entry name byte)", align=Align.INLINE)
d.label(0x8C0F, "loop_print_cmd_name")


d.comment(0x8C12, "Advance table pointer", align=Align.INLINE)
d.comment(0x8C13, "Decrement padding counter", align=Align.INLINE)
d.comment(0x8C14, "Load next character", align=Align.INLINE)
d.comment(0x8C17, "Bit 7 clear: more chars, continue", align=Align.INLINE)
d.label(0x8C19, "loop_pad_spaces")

d.comment(0x8C19, "Pad with spaces", align=Align.INLINE)
d.comment(0x8C1E, "Decrement remaining pad count", align=Align.INLINE)
d.comment(0x8C1F, "More padding needed: loop", align=Align.INLINE)
d.comment(0x8C21, "Load syntax descriptor byte", align=Align.INLINE)
d.comment(0x8C24, "Mask to get syntax string index", align=Align.INLINE)
d.comment(0x8C26, "Use index as Y", align=Align.INLINE)
d.comment(0x8C27, "Look up syntax string offset", align=Align.INLINE)
d.comment(0x8C2A, "Transfer offset to Y", align=Align.INLINE)
d.label(0x8C2B, "loop_print_syntax")

d.subroutine(
    0x8C2B,
    "loop_print_syntax",
    title="Per-character body of *HELP syntax string emit",
    description="""`INY` / load `syn_opt_dir,Y` / detect terminator or
line-break:

| Byte | Action |
|---|---|
| `0`  | terminator – stop |
| `CR` (`&0D`) | line-break – wrap |
| other | print the character |

Two callers: the `BNE` at `&8C13` (continue with current char)
and the `BEQ` at `&8C19` (fall-through from the line-wrap
path).""",
    on_entry={"y": "current index into syn_opt_dir"},
)


d.comment(0x8C2B, "Advance to next character", align=Align.INLINE)
d.comment(0x8C2C, "Load syntax string character", align=Align.INLINE)
d.comment(0x8C2F, "Zero terminator: end of syntax", align=Align.INLINE)
d.comment(0x8C31, "Carriage return: line continuation", align=Align.INLINE)
d.comment(0x8C33, "No: print the character", align=Align.INLINE)
d.comment(0x8C35, "Handle line wrap in syntax output", align=Align.INLINE)
d.comment(0x8C38, "Continue with next character", align=Align.INLINE)
d.label(0x8C3B, "print_syntax_char")

d.comment(0x8C3E, "Continue with next character", align=Align.INLINE)
d.label(0x8C41, "done_entry_newline")

d.comment(0x8C44, "X += 3: skip syntax descriptor and address", align=Align.INLINE)
d.comment(0x8C45, "(continued)", align=Align.INLINE)
d.comment(0x8C46, "(continued)", align=Align.INLINE)
d.comment(0x8C47, "Loop for next command", align=Align.INLINE)
d.label(0x8C4A, "done_print_table")

d.subroutine(
    0x8C4A,
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


d.comment(0x8C4A, "Restore processor status", align=Align.INLINE)
d.comment(0x8C4B, "Restore Y", align=Align.INLINE)
d.comment(0x8C4C, "Transfer to Y", align=Align.INLINE)
d.comment(0x8C4D, "Return", align=Align.INLINE)
d.label(0x8C4E, "help_wrap_if_serial")

d.subroutine(
    0x8C4E,
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


d.comment(0x8C4E, "Read output stream type", align=Align.INLINE)
d.entry(0x8C4E)
d.comment(0x8C51, "Stream 0 (VDU): no wrapping", align=Align.INLINE)
d.comment(0x8C53, "Stream 3 (printer)?", align=Align.INLINE)
d.comment(0x8C55, "Yes: no wrapping", align=Align.INLINE)
d.comment(0x8C57, "Save Y across OS call", align=Align.INLINE)
d.comment(0x8C5B, "Y=&0B: indent width - 1", align=Align.INLINE)
d.comment(0x8C5D, "Space character", align=Align.INLINE)
d.label(0x8C5F, "loop_indent_spaces")

d.comment(0x8C62, "Decrement indent counter", align=Align.INLINE)
d.comment(0x8C63, "More spaces needed: loop", align=Align.INLINE)
d.label(0x8C66, "rts_help_wrap")

d.comment(0x8C66, "Return", align=Align.INLINE)
d.comment(0x8C67, "X=0: start of utility command table", align=Align.INLINE)
d.entry(0x8C67)
d.label(0x8C67, "svc_4_star_command")

d.subroutine(
    0x8C67,
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


d.comment(0x8C69, "Get command line offset", align=Align.INLINE)
d.label(0x8C6B, "svc4_dispatch_lookup")

d.comment(0x8C6B, "Save text pointer to fs_crc", align=Align.INLINE)
d.comment(0x8C6E, "Try to match command in table", align=Align.INLINE)
d.comment(0x8C71, "No match: return to caller", align=Align.INLINE)
d.comment(0x8C73, "Match found: execute command", align=Align.INLINE)
d.comment(0x8C76, "Check for credits Easter egg", align=Align.INLINE)
d.entry(0x8C76)
d.label(0x8C76, "svc_9_help")

d.subroutine(
    0x8C76,
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
d.comment(0x8C79, "Get command line offset", align=Align.INLINE)
d.comment(0x8C7B, "Load character at offset", align=Align.INLINE)
d.comment(0x8C7D, "Is it CR (bare *HELP)?", align=Align.INLINE)
d.comment(0x8C7F, "No: check for specific topic", align=Align.INLINE)
d.comment(0x8C81, "Print version string", align=Align.INLINE)
d.comment(0x8C84, "X=&91: start of help command list", align=Align.INLINE)
d.comment(0x8C86, "Print command list from table", align=Align.INLINE)
d.label(0x8C89, "svc_return_unclaimed")

d.subroutine(
    0x8C89,
    "svc_return_unclaimed",
    title="Restore Y and return service-call unclaimed",
    description="""Reloads `Y` from `ws_page` (the saved command-line offset) and
`RTS` to the caller without clearing `A` – preserving the
original service number so the next ROM in the chain sees the
unclaimed call.

Reached from the four service-handler escape paths at `&8C4C`,
`&8C91`, `&8CFA`, and `&95BD` that hand a request back to MOS
without acting on it.""",
    on_exit={"y": "ws_page (restored command-line offset)"},
)


d.comment(0x8C89, "Restore Y (command line offset)", align=Align.INLINE)
d.comment(0x8C8B, "Return unclaimed", align=Align.INLINE)
d.label(0x8C8C, "check_help_topic")

d.comment(0x8C8C, "Test for topic match (sets flags)", align=Align.INLINE)
d.comment(0x8C8F, "Is first char '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8C91, "No: try topic-specific help", align=Align.INLINE)
d.comment(0x8C93, "'.' found: show full command list", align=Align.INLINE)
d.label(0x8C96, "match_help_topic")

d.comment(0x8C96, "Save text pointer to fs_crc", align=Align.INLINE)
d.label(0x8C99, "loop_dispatch_help")

d.comment(0x8C99, "Save flags", align=Align.INLINE)
d.comment(0x8C9A, "X=&96: help command table start", align=Align.INLINE)
d.comment(0x8C9C, "Try to match help topic in table", align=Align.INLINE)
d.comment(0x8C9F, "No match: try next topic", align=Align.INLINE)
d.comment(0x8CA1, "Restore flags", align=Align.INLINE)
d.comment(0x8CA2, "Push return address high (&8C)", align=Align.INLINE)
d.comment(0x8CA4, "Push it for RTS dispatch", align=Align.INLINE)
d.comment(0x8CA5, "Push return address low (&74)", align=Align.INLINE)
d.comment(0x8CA7, "Push it for RTS dispatch", align=Align.INLINE)
d.comment(0x8CA8, "Load dispatch address high", align=Align.INLINE)
d.comment(0x8CAB, "Push dispatch high for RTS", align=Align.INLINE)
d.comment(0x8CAC, "Load dispatch address low", align=Align.INLINE)
d.comment(0x8CAF, "Push dispatch low for RTS", align=Align.INLINE)
d.comment(0x8CB0, "Dispatch via RTS (returns to &8CA5)", align=Align.INLINE)
d.label(0x8CB1, "skip_if_no_match")

d.comment(0x8CB1, "Restore flags from before match", align=Align.INLINE)
d.comment(0x8CB2, "End of command line?", align=Align.INLINE)
d.comment(0x8CB4, "No: try matching next topic", align=Align.INLINE)
d.label(0x8CB8, "print_version_header")

d.subroutine(
    0x8CB8,
    "print_version_header",
    title="Print ANFS version string and station number",
    description="""Uses an inline string after `JSR` to
[`print_inline`](label:print_inline): `CR + "Advanced NFS 4.24" +
CR`. After the inline string, `JMP`s to
[`print_station_id`](label:print_station_id) to append the local Econet
station number.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered (print_inline + print_station_id)"},
)


d.comment(0x8CB8, "Print version string via inline", align=Align.INLINE)
d.label(0x8CBB, "version_string_cr")

d.comment(0x8CCE, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
# UNMAPPED: d.comment(
# UNMAPPED:     0x8CAA,
# UNMAPPED:     "Tail-call print_station_id to append ' Econet Station <n>' (and ' No Clock' if appropriate)",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
d.subroutine(
    0x8CD2,
    "get_ws_page",
    title="Read workspace page number for current ROM slot",
    description="""Indexes into the MOS per-ROM workspace table
[`rom_ws_pages`](label:rom_ws_pages) using `romsel_copy` (`&F4`) as
the ROM slot. Holds a copy of the slot byte in `Y`, then runs a
`ROL` / `PHP` / `ROR` / `PLP` sequence at `&8CD8`–`&8CB6` that
restores `A` to the original byte while leaving the saved-flags
register reflecting bit 6 of the original byte (the ADLC-absent
flag). Falls through to whichever caller-specific tail follows.""",
    on_exit={
        "a": "workspace page byte (preserved through ROL/ROR)",
        "y": "same byte (set by `TAY` before the rotate trick)",
        "n": "set to bit 6 of the original byte (ADLC-absent flag)",
    },
)


d.comment(0x8CD2, "Y = current ROM slot number from MOS copy at &F4", align=Align.INLINE)
d.comment(0x8CD4, "Load workspace page byte for this ROM slot", align=Align.INLINE)
d.comment(0x8CD7, "Hold a copy of the slot byte in Y while we test bit 6", align=Align.INLINE)
d.comment(0x8CD8, "ROL puts pre-ROL bit 6 into the post-ROL N flag (and pre-ROL bit 7 into C)", align=Align.INLINE)
d.comment(0x8CD9, "Save those flags so the upcoming ROR doesn't lose N", align=Align.INLINE)
d.comment(0x8CDA, "ROR restores A to its original value (using the saved C)", align=Align.INLINE)
d.comment(0x8CDB, "Restore the ROL flags: N is now pre-ROL bit 6", align=Align.INLINE)
d.comment(0x8CDC, "Bit 6 clear: skip the OR (no ADLC-absent flag)", align=Align.INLINE)
d.comment(
    0x8CDE,
    "Bit 6 set: re-set bit 7 in the returned page byte (the ADLC-absent flag uses bit 7 in callers)",
    align=Align.INLINE,
)
d.label(0x8CE0, "get_ws_page_loop")

d.comment(0x8CE0, "Transfer to Y", align=Align.INLINE)
d.comment(0x8CE1, "Return with page in A and Y", align=Align.INLINE)
d.label(0x8CE2, "setup_ws_ptr")

d.subroutine(
    0x8CE2,
    "setup_ws_ptr",
    title="Set up zero-page pointer to workspace page",
    description="""Calls [`get_ws_page`](label:get_ws_page) to read the page number,
stores it as the high byte in `nfs_temp` (`&CD`), and clears the
low byte at `&CC` to zero. This gives a page-aligned pointer used
by FS initialisation and [`cmd_net_fs`](label:cmd_net_fs) to
access the private workspace.""",
    on_exit={"a": "0", "y": "workspace page number"},
)


d.comment(0x8CE2, "Get workspace page for ROM slot", align=Align.INLINE)
d.comment(0x8CE5, "Store page in nfs_temp", align=Align.INLINE)
d.comment(0x8CE7, "A=0", align=Align.INLINE)
d.comment(0x8CE9, "Clear low byte of pointer", align=Align.INLINE)
d.label(0x8CEB, "rts_setup_ws_ptr")

d.comment(0x8CEB, "Return", align=Align.INLINE)
d.comment(0x8CEC, "OSBYTE &7A: scan keyboard from key 16", align=Align.INLINE)
d.entry(0x8CEC)
d.label(0x8CEC, "svc_3_autoboot")

d.subroutine(
    0x8CEC,
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


d.comment(0x8CF2, "No key pressed: select Net FS", align=Align.INLINE)
d.comment(0x8CF4, "Key &19 (N)?", align=Align.INLINE)
d.comment(0x8CF6, "Yes: write key state and boot", align=Align.INLINE)
d.comment(0x8CF8, "EOR with &55: maps to zero if 'N'", align=Align.INLINE)
d.comment(0x8CFA, "Not N key: return unclaimed", align=Align.INLINE)
d.label(0x8CFC, "write_key_state")

d.comment(0x8CFD, "OSBYTE &78: write keys pressed", align=Align.INLINE)
d.label(0x8D02, "select_net_fs")

d.comment(0x8D02, "Select NFS as current filing system", align=Align.INLINE)
d.comment(0x8D0B, "A=0: clear svc_state marker", align=Align.INLINE)
d.comment(0x8D0D, "Store -> svc_state", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CE4, "Print station number", align=Align.INLINE)
d.comment(0x8D0F, "Get workspace page", align=Align.INLINE)
d.comment(0x8D11, "Non-zero: already initialised, return", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CEE, "Load boot flags", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CF1, "Set bit 2 (auto-boot in progress)", align=Align.INLINE)
# UNMAPPED: d.comment(0x8CF3, "Store updated boot flags", align=Align.INLINE)
d.comment(0x8D18, "X=&3E: boot filename address low", align=Align.INLINE)
d.comment(0x8D1A, "Y=&8D: boot filename address high", align=Align.INLINE)
d.comment(0x8D1C, "Execute boot file", align=Align.INLINE)
d.label(0x8D1F, "notify_new_fs")

d.subroutine(
    0x8D1F,
    "notify_new_fs",
    title="Notify OS of filing-system selection",
    description="""Loads `A=6` (FSCV reason: filing system change) and falls
through to [`call_fscv`](label:call_fscv), which `JMP`-indirects
through `vec_fscv` to invoke the FSCV vector. The FSCV handler
returns to whatever invoked `notify_new_fs` -- this is a
fire-and-forget notification, not a return-to-caller call.

Single caller (&8b86 inside the FS-selection sequence).""",
    on_entry={},
    on_exit={"a": "6 (clobbered by FSCV handler)"},
)


d.comment(0x8D1F, "A=6: notify new filing system", align=Align.INLINE)
d.label(0x8D21, "call_fscv")

d.subroutine(
    0x8D21,
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


d.comment(0x8D21, "Tail-jump via FSCV vector (filing-system change service)", align=Align.INLINE)
d.label(0x8D24, "issue_svc_15")

d.comment(0x8D24, "X=&0F: service 15 (vectors claimed)", align=Align.INLINE)
d.subroutine(
    0x8D24,
    "issue_svc_15",
    title="Issue OSBYTE 143 service 15 (vectors-claimed) request",
    description="Tail-call wrapper that loads X=&0F (service number 15) and tail-jumps to OSBYTE 143 (issue paged ROM service request), which broadcasts service 15 to all sideways ROMs. ANFS calls this from svc_2_private_workspace after claiming its workspace, to give other ROMs a chance to react.",
    on_entry={"a": "OSBYTE result is irrelevant -- this is fire-and-forget"},
)


d.label(0x8D26, "issue_svc_osbyte")

d.comment(0x8D26, "A=&8F: OSBYTE 'Issue paged-ROM service request'", align=Align.INLINE)
d.subroutine(
    0x8D2B,
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


d.entry(0x8D2B)
d.comment(0x8D2B, "Save Y on stack", align=Align.INLINE)
d.comment(0x8D2C, "X=&11: CMOS offset for Econet station-flags", align=Align.INLINE)
d.comment(0x8D2E, "Read CMOS byte: result in Y", align=Align.INLINE)
d.comment(0x8D31, "A = CMOS byte", align=Align.INLINE)
d.comment(0x8D32, "Restore caller's Y", align=Align.INLINE)
d.comment(0x8D33, "Isolate bit 0 (page-&0B fallback flag)", align=Align.INLINE)
d.comment(0x8D35, "Bit clear: keep caller's Y", align=Align.INLINE)
d.comment(0x8D37, "Caller's Y already >= &10?", align=Align.INLINE)
d.comment(0x8D39, "Yes: keep it", align=Align.INLINE)
d.comment(0x8D3B, "Y < &10 with bit set: clamp to &10", align=Align.INLINE)
d.comment(0x8D3D, "Return", align=Align.INLINE)
d.subroutine(
    0x8D46,
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


d.comment(0x8D46, "Y = ws_page (workspace high page)", align=Align.INLINE)
d.comment(0x8D48, "X=5: start of credits keyword", align=Align.INLINE)
d.label(0x8D4A, "loop_match_credits")

d.comment(0x8D4A, "Load character from command line", align=Align.INLINE)
d.comment(0x8D4C, "Compare with credits keyword", align=Align.INLINE)
d.comment(0x8D4F, "Mismatch: check if keyword complete", align=Align.INLINE)
d.comment(0x8D51, "Advance command line pointer", align=Align.INLINE)
d.comment(0x8D52, "Advance keyword pointer", align=Align.INLINE)
d.comment(0x8D53, "Continue matching", align=Align.INLINE)
d.label(0x8D55, "done_credits_check")

d.comment(0x8D55, "Reached end of keyword (X=&0C)?", align=Align.INLINE)
d.comment(0x8D57, "No: keyword not fully matched, return", align=Align.INLINE)
d.comment(0x8D59, "Print the credits string inline (high-bit terminated)", align=Align.INLINE)

# The credits string is emitted by print_inline (high-bit terminated),
# not by the manual emit loop the earlier ANFS versions used. The bytes
# at &8D5C..&8D9C are the inline string, consumed by the print_inline
# hook; the &EA (NOP) terminator at &8D9D doubles as the resume opcode
# and falls through to the RTS at &8D9E. The same string doubles as the
# keyword matched by the CMP loop above (credits_keyword_start).
d.index_base(0x8D5C, "credits_keyword_start")

d.label(0x8D9E, "rts_credits_check")
d.comment(0x8D9E, "Return", align=Align.INLINE)

d.comment(0x8D9F, "Save caller Y", align=Align.INLINE)
d.entry(0x8D9F)

d.label(0x8D9F, "cmd_iam_save_ctx")
d.comment(0x8DA0, "Read fs_last_byte_flag (work_bd)", align=Align.INLINE)
d.comment(0x8DA2, "Read fs_options (work_bb)", align=Align.INLINE)
d.comment(0x8DA4, "Read fs_block_offset (work_bc)", align=Align.INLINE)
d.comment(0x8DA6, "Push fs_last_byte_flag for restore on return", align=Align.INLINE)
d.comment(0x8DA9, "OSBYTE &77: close SPOOL/EXEC", align=Align.INLINE)
d.entry(0x8DA9)


d.subroutine(
    0x8DA9,
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


d.comment(0x8DAB, "Store as pending operation marker", align=Align.INLINE)
d.comment(0x8DB1, "Y=0", align=Align.INLINE)
d.comment(0x8DB3, "Clear password entry flag", align=Align.INLINE)
d.comment(0x8DB5, "Reset FS connection state", align=Align.INLINE)
d.comment(0x8DB8, "Clear hazel_fs_pending_state (connection-attempt flag)", align=Align.INLINE)
d.comment(0x8DBD, "Pop and discard saved fs_last_byte_flag", align=Align.INLINE)
d.comment(0x8DBE, "Set up transfer parameters", align=Align.INLINE)
d.subroutine(
    0x8DBE,
    "load_transfer_params",
    title="Set FS transfer parameters via set_xfer_params",
    description="""3-byte trampoline that calls
[`set_xfer_params`](label:set_xfer_params) and falls through into
[`cmd_pass`](label:cmd_pass)'s argument-parse prologue. Reached
from `init_txcb_and_load_xfer` at `&B3D9` to install the FS
transfer context (byte count + source pointer in `fs_last_byte_flag`
/ `fs_crc_lo`/`hi`) before continuing into the *I am / *Pass
station-and-credential parser.""",
)

# UNMAPPED: d.label(0x8DA7, "ps_template_base")

d.comment(0x8DC2, "Load first option byte", align=Align.INLINE)
d.comment(0x8DC4, "Parse station number if present", align=Align.INLINE)
d.comment(0x8DC7, "Not a digit: skip to password entry", align=Align.INLINE)
d.comment(0x8DC9, "Parse user ID string", align=Align.INLINE)
d.comment(0x8DCC, "No user ID: go to password", align=Align.INLINE)
d.comment(0x8DCE, "Store file server station low", align=Align.INLINE)
d.comment(0x8DD1, "Check and store FS network", align=Align.INLINE)
d.comment(0x8DD4, "Skip separator", align=Align.INLINE)
d.comment(0x8DD5, "Parse next argument", align=Align.INLINE)
d.label(0x8DD8, "skip_no_fs_addr")

d.comment(0x8DD8, "No FS address: skip to password", align=Align.INLINE)
d.comment(0x8DDA, "Store file server station high", align=Align.INLINE)
d.comment(0x8DDD, "X=&FF: pre-decrement for loop", align=Align.INLINE)
d.label(0x8DDF, "loop_copy_logon_cmd")

d.comment(0x8DDF, "Advance index", align=Align.INLINE)
d.comment(0x8DE0, "Load logon command template byte", align=Align.INLINE)
d.comment(0x8DE3, "Store into transmit buffer", align=Align.INLINE)
d.comment(0x8DE6, "Bit 7 clear: more bytes, loop", align=Align.INLINE)
d.comment(0x8DE8, "Send logon with file server lookup", align=Align.INLINE)
d.comment(0x8DEB, "Success: skip to password entry", align=Align.INLINE)
d.comment(0x8DED, "Build FS command packet", align=Align.INLINE)
d.entry(0x8DED)
d.label(0x8DED, "cmd_pass")

d.subroutine(
    0x8DED,
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


d.label(0x8DF0, "scan_pass_prompt")

d.comment(0x8DF0, "Y=&FF: pre-increment for loop", align=Align.INLINE)
d.label(0x8DF2, "loop_scan_colon")

d.comment(0x8DF2, "Advance to next byte", align=Align.INLINE)
d.comment(0x8DF3, "Load byte from reply buffer", align=Align.INLINE)
d.comment(0x8DF6, "Is it CR (end of prompt)?", align=Align.INLINE)
d.comment(0x8DF8, "Yes: no colon found, skip to send", align=Align.INLINE)
d.comment(0x8DFA, "Is it ':' (password prompt)?", align=Align.INLINE)
d.comment(0x8DFC, "No: keep scanning", align=Align.INLINE)
d.comment(0x8DFE, "Print byte no-spool", align=Align.INLINE)
d.comment(0x8E01, "Save position of colon", align=Align.INLINE)
d.label(0x8E03, "read_pw_char")

d.comment(0x8E03, "A=&FF: mark as escapable", align=Align.INLINE)
d.comment(0x8E05, "Set escape flag", align=Align.INLINE)
d.comment(0x8E07, "Check for escape condition", align=Align.INLINE)
d.comment(0x8E0F, "Not NAK (&15): check other chars", align=Align.INLINE)
d.comment(0x8E11, "Restore colon position", align=Align.INLINE)
d.comment(0x8E13, "Non-zero: restart from colon", align=Align.INLINE)
d.label(0x8E15, "loop_erase_pw")

d.comment(0x8E15, "At colon position?", align=Align.INLINE)
d.comment(0x8E17, "Yes: restart password input", align=Align.INLINE)
d.comment(0x8E19, "Backspace: move back one character", align=Align.INLINE)
d.comment(0x8E1A, "If not at start: restart input", align=Align.INLINE)
d.label(0x8E1C, "check_pw_special")

d.comment(0x8E1C, "Delete key (&7F)?", align=Align.INLINE)
d.comment(0x8E1E, "Yes: handle backspace", align=Align.INLINE)
d.comment(0x8E20, "Store character in password buffer", align=Align.INLINE)
d.comment(0x8E23, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x8E24, "Is it CR (end of password)?", align=Align.INLINE)
d.comment(0x8E26, "No: read another character", align=Align.INLINE)
d.comment(0x8E28, "Print newline no-spool", align=Align.INLINE)
d.label(0x8E2B, "send_pass_to_fs")

d.comment(0x8E2B, "Transfer string length to A", align=Align.INLINE)
d.comment(0x8E2C, "Save string length", align=Align.INLINE)
d.comment(0x8E2D, "Set up transmit control block", align=Align.INLINE)
d.comment(0x8E30, "Send to file server and get reply", align=Align.INLINE)
d.comment(0x8E34, "Include terminator", align=Align.INLINE)
d.comment(0x8E35, "Y=0", align=Align.INLINE)
d.label(0x8E39, "clear_if_station_match")

d.subroutine(
    0x8E39,
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


d.comment(0x8E39, "Ensure bridge initialised; A=spool_control_flag (bridge status)", align=Align.INLINE)
d.comment(0x8E3C, "EOR with hazel_fs_network: zero result if equal", align=Align.INLINE)
d.comment(0x8E3F, "Different: return without clearing", align=Align.INLINE)
d.comment(0x8E41, "Same: clear station byte", align=Align.INLINE)
d.label(0x8E44, "rts_station_match")

d.comment(0x8E44, "Return", align=Align.INLINE)
d.subroutine(
    0x8E45,
    "check_urd_prefix",
    title="Branch to *RUN handler if first arg char is '&'",
    description="""Reads the first character of the parsed command text via
`(fs_crc_lo),Y`:

| First char | Path |
|---|---|
| `'&'` (URD prefix marker) | `JMP cmd_run_via_urd` |
| any other | fall through to `pass_send_cmd` (send as normal FS request) |

Single caller (the FS command-name post-match path at
`&959C`).""",
)


d.comment(0x8E45, "Y=0: first character offset", align=Align.INLINE)
d.comment(0x8E47, "Load first character of command text", align=Align.INLINE)
d.comment(0x8E49, "Is it '&' (URD prefix)?", align=Align.INLINE)
d.comment(0x8E4B, "No: send as normal FS command", align=Align.INLINE)
d.comment(0x8E4D, "Yes: route via *RUN for URD prefix handling", align=Align.INLINE)
d.label(0x8E50, "pass_send_cmd")

d.comment(0x8E50, "Build FS command packet", align=Align.INLINE)
d.comment(0x8E53, "Transfer result to Y", align=Align.INLINE)
d.label(0x8E54, "send_cmd_and_dispatch")

d.subroutine(
    0x8E54,
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


d.comment(0x8E54, "Set up command and send to FS", align=Align.INLINE)
d.comment(0x8E57, "Load reply function code", align=Align.INLINE)
d.comment(0x8E5A, "Zero: no reply, return", align=Align.INLINE)
d.comment(0x8E5C, "Load first reply byte", align=Align.INLINE)
d.comment(0x8E5F, "Y=&25: logon dispatch offset", align=Align.INLINE)
d.comment(0x8E63, "Parse reply as decimal number", align=Align.INLINE)
d.label(0x8E63, "fscv_handler")
for i, ev in enumerate(_ev_dispatch):
    addr = 0x8EBF + i * 2
    d.word(addr)
    d.expr(addr, sym(ev))
    d.comment(addr, "%s dispatch" % ev[3:].upper(), align=Align.INLINE)
d.comment(0x8E66, "Result >= 8?", align=Align.INLINE)
d.comment(0x8E68, "Yes: out of range, return", align=Align.INLINE)
d.comment(0x8E6A, "Transfer handle to X", align=Align.INLINE)
d.comment(0x8E6B, "Look up in open files table", align=Align.INLINE)
d.comment(0x8E6E, "Transfer result to A", align=Align.INLINE)
d.comment(0x8E6F, "Y=&1D: handle dispatch offset", align=Align.INLINE)
d.label(0x8E73, "dir_op_dispatch")

d.subroutine(
    0x8E73,
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


d.comment(0x8E73, "Handle >= 5?", align=Align.INLINE)
d.comment(0x8E75, "Yes: out of range, return", align=Align.INLINE)
d.comment(0x8E77, "Y=&18: settles X_final to &19..&1D (lang reply 0..4)", align=Align.INLINE)
d.comment(0x8E79, "Advance X to target index", align=Align.INLINE)
d.subroutine(
    0x8E79,
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


d.comment(0x8E7A, "Decrement Y offset counter", align=Align.INLINE)
d.comment(0x8E7B, "Y still positive: continue counting", align=Align.INLINE)
d.comment(0x8E7D, "Y=&FF: will be ignored by caller", align=Align.INLINE)
d.comment(0x8E7E, "Load dispatch address high byte", align=Align.INLINE)
d.comment(0x8E81, "Push high byte for RTS dispatch", align=Align.INLINE)
d.label(0x8E82, "push_dispatch_lo")

d.comment(0x8E82, "Load dispatch address low byte", align=Align.INLINE)
d.comment(0x8E85, "Push low byte for RTS dispatch", align=Align.INLINE)
d.comment(0x8E86, "Load FS options pointer", align=Align.INLINE)
d.label(0x8E88, "dispatch_rts")

d.comment(0x8E88, "Dispatch via RTS", align=Align.INLINE)
d.comment(0x8E89, "Claim 1 page (DEY = decrement Y by 1)", align=Align.INLINE)
d.entry(0x8E89)
d.subroutine(
    0x8E89,
    "noop_dey_rts",
    title="Service &24: dynamic workspace claim (1 page)",
    description="""Two-byte handler reached via [`svc_dispatch`](label:svc_dispatch) slot
&13. `DEY` decrements the caller's first-available-page count by 1
to claim a single workspace page; `RTS` returns to the dispatcher.""",
)


d.comment(0x8E8A, "Return", align=Align.INLINE)
d.comment(0x8E8B, "X = 10 (top of 11-byte template)", align=Align.INLINE)
d.entry(0x8E8B)
d.subroutine(
    0x8E8B,
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


d.label(0x8E8D, "loop_copy_return_template")

d.comment(0x8E8D, "Load template byte X from &8E97+X", align=Align.INLINE)
d.comment(0x8E90, "Store at (&F2),Y", align=Align.INLINE)
d.comment(0x8E92, "Advance destination cursor", align=Align.INLINE)
d.comment(0x8E93, "Step to previous template byte", align=Align.INLINE)
d.comment(0x8E94, "Loop until X has wrapped past 0", align=Align.INLINE)
d.label(0x8E96, "fs_template_done")

d.comment(0x8E96, "Return", align=Align.INLINE)
d.index_base(0x8E97, "fs_info_template")
d.banner(
    0x8E97,
    title="FS-name reply template (11 bytes, byte-reversed)",
    description="""Source data for the byte-reverse copy in
[`copy_template_to_zp`](label:copy_template_to_zp). When stored at
`(os_text_ptr),Y` in reverse order the destination reads
`"NET" + 6 spaces + "/" + length-byte 5`, which is the FS name
the ROM reports for service &25 (FS name + info reply).""",
)

d.comment(
    0x8E98,
    "11-byte template (length 5 in [0], then '       TEN'); copied to (&F2),Y by copy_template_to_zp",
    align=Align.INLINE,
)
d.comment(0x8EA2, "Test bit 6 of fs_flags (NFS currently selected?)", align=Align.INLINE)
d.entry(0x8EA2)
d.subroutine(
    0x8EA2,
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


d.comment(0x8EA5, "Clear: return without acting", align=Align.INLINE)
d.comment(0x8EA7, "Ensure NFS is the selected FS", align=Align.INLINE)
d.comment(0x8EAA, "A=0", align=Align.INLINE)
d.comment(0x8EAC, "Y=0 -- FILEV 'close all files' sub-call", align=Align.INLINE)
d.comment(0x8EAD, "Tail-call findv_handler (= FILEV)", align=Align.INLINE)
d.subroutine(
    0x8EB0,
    "read_cmos_byte_0",
    title="Read CMOS RAM byte 0",
    description="""Sets `X=0` and falls through to [`osbyte_a1`](label:osbyte_a1),
which issues OSBYTE `&A1` to read CMOS RAM byte 0 – the
file-system / language byte holding the default boot mode and FS
selection.

Single caller (`&8FBB`, inside
[`nfs_init_body`](label:nfs_init_body)'s CMOS-read sequence).""",
    on_exit={"y": "CMOS byte 0 (returned by OSBYTE &A1)"},
)


d.comment(0x8EB0, "X=0: CMOS RAM index 0 (station ID)", align=Align.INLINE)
d.comment(0x8EB2, "A=&A1: OSBYTE &A1 = read CMOS RAM", align=Align.INLINE)
d.subroutine(
    0x8EB2,
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
    0x8EB7,
    """Printer server template (8 bytes)

Default printer server configuration data, read
indirectly by copy_ps_data via LDA ps_template_base,X
with X=&F8..&FF (reaching ps_template_base+&F8 =
&8EB7). Contains "PRINT " (6 bytes) as the default
printer server name, followed by &01 and &00 as
default status bytes. Absent from NFS versions;
unique to ANFS.""",
)
d.comment(0x8EB7, 'PS template: default name "PRINT "', align=Align.INLINE)
d.label(0x8EB7, "ps_template_data")
d.banner(
    0x8EB7,
    title="Printer-server name template (8 bytes)",
    description="""Eight bytes (`"PRINT "` then `&01 &00`) read by
[`copy_ps_data`](label:copy_ps_data) via the indexed-base trick
`LDA ps_template_base+X` with `X=&F8..&FF`. The base label
`ps_template_base` resolves to `ps_template_data - &F8` so the
indexed access lands on the bytes here. Default contents installed
into the Printer-Server name slot during ANFS initialisation.""",
)

d.subroutine(
    0x8EBF,
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

d.comment(0x8EE1, "X=0 then fall through into osbyte_yff", align=Align.INLINE)
d.subroutine(
    0x8EE1,
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


d.label(0x8EE1, "osbyte_x0")

d.comment(0x8EE3, "Y=&FF: 'read' parameter for OSBYTE", align=Align.INLINE)
d.subroutine(
    0x8EE3,
    "osbyte_yff",
    title="OSBYTE wrapper with Y=&FF",
    description="""Sets Y=&FF and JMPs to the MOS OSBYTE entry
point. X must already be set by the caller. The
osbyte_x0 entry point falls through to here after
setting X=0.""",
    on_entry={"a": "OSBYTE function code", "x": "OSBYTE X parameter"},
    on_exit={"y": "&FF"},
)

d.label(0x8EE3, "osbyte_yff")


d.label(0x8EE5, "jmp_osbyte")

d.comment(0x8EE5, "Tail-call OSBYTE", align=Align.INLINE)
d.subroutine(
    0x8EEA,
    "osbyte_x0_y0",
    title="OSBYTE wrapper with X=0, Y=0",
    description="""Sets `X=0` and `Y=0` then branches to `jmp_osbyte`. Called from
the Econet OSBYTE dispatch chain to handle OSBYTEs that require
both `X` and `Y` cleared. The unconditional `BEQ` (after `LDY
#0` sets `Z`) reaches the `JMP osbyte` instruction.""",
    on_entry={"a": "OSBYTE number"},
    on_exit={"x": "0", "y": "0"},
)


d.comment(0x8EEA, "X=0: clear OSBYTE X arg", align=Align.INLINE)
d.comment(0x8EEC, "Y=0", align=Align.INLINE)
d.comment(0x8EF0, "Get original OSBYTE A parameter", align=Align.INLINE)
d.entry(0x8EF0)
d.label(0x8EF0, "svc_7_osbyte")

d.subroutine(
    0x8EF0,
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
d.comment(0x8EF2, "Subtract &31 (map &32-&35 to 1-4)", align=Align.INLINE)
d.comment(0x8EF4, "In range 0-3?", align=Align.INLINE)
d.comment(0x8EF6, "No: not ours, return unclaimed", align=Align.INLINE)
d.comment(0x8EF8, "Transfer to X as dispatch index", align=Align.INLINE)
d.comment(0x8EF9, "Clear svc_state", align=Align.INLINE)
d.comment(0x8EFB, "Transfer Y to A (OSBYTE Y param)", align=Align.INLINE)
d.comment(0x8EFC, "Y=&2F: OSBYTE dispatch offset", align=Align.INLINE)
d.comment(0x8EFE, "Dispatch to OSBYTE handler via table", align=Align.INLINE)
d.comment(0x8F01, "Y already >= &C8?", align=Align.INLINE)
d.entry(0x8F01)

d.label(0x8F01, "raise_y_to_c8")

d.subroutine(
    0x8F01,
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


d.comment(0x8F03, "Yes: return Y unchanged", align=Align.INLINE)
d.comment(0x8F05, "No: raise Y to &C8", align=Align.INLINE)
d.label(0x8F07, "rts_raise_y_to_c8")

d.comment(0x8F07, "Return", align=Align.INLINE)
d.label(0x8F08, "store_ws_page_count")

d.subroutine(
    0x8F08,
    "store_ws_page_count",
    title="Record workspace page count (capped at &D3)",
    description="""Stores the workspace allocation from service 1 into offset `&0B` of
the receive control block, capping the value at `&D3` to prevent
overflow into adjacent workspace areas. Called by
[`svc_2_priv_ws`](label:svc_2_priv_ws) after issuing the
absolute workspace claim service call.""",
    on_entry={"y": "workspace page count from service 1"},
)
d.comment(0x8F08, "Transfer Y to A", align=Align.INLINE)
d.comment(0x8F09, "Push for save", align=Align.INLINE)
d.comment(0x8F0A, "Y >= &D3?", align=Align.INLINE)
d.comment(0x8F0C, "No: use Y as-is", align=Align.INLINE)
d.comment(0x8F0E, "Cap at &D3", align=Align.INLINE)
d.label(0x8F10, "done_cap_ws_count")

d.comment(0x8F10, "Offset &0B in receive block", align=Align.INLINE)
d.comment(0x8F12, "Store workspace page count", align=Align.INLINE)
d.comment(0x8F14, "Pop -- save Y temporarily", align=Align.INLINE)
d.comment(0x8F15, "Return -- ws_page count saved", align=Align.INLINE)
d.entry(0x8F16)
d.label(0x8F16, "set_rom_ws_page")

d.comment(0x8F16, "Caller's page (in Y) into A", align=Align.INLINE)
d.comment(0x8F17, "Y = current ROM slot from romsel_copy", align=Align.INLINE)
d.comment(0x8F19, "Push restored value", align=Align.INLINE)
d.comment(0x8F1A, "Mask bit 7 (workspace flag)", align=Align.INLINE)
d.comment(0x8F1C, "Publish page into rom_ws_pages[slot] (bit 7 cleared = workspace claimed)", align=Align.INLINE)
d.comment(0x8F1F, "Discarded read of 1770 data reg (&FE2B)", align=Align.INLINE)
d.comment(0x8F22, "Discarded read of 1770 status reg (&FE28)", align=Align.INLINE)
d.comment(0x8F25, "Pop saved Y", align=Align.INLINE)
d.comment(0x8F26, "Increment for next page", align=Align.INLINE)
d.comment(0x8F27, "Return", align=Align.INLINE)
d.entry(0x8F28)
d.subroutine(
    0x8F28,
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


d.comment(0x8F28, "Save Y on stack (caller's claim)", align=Align.INLINE)
d.comment(0x8F29, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0x8F2B, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0x8F2E, "A = CMOS &11 value", align=Align.INLINE)
d.comment(0x8F2F, "Mask bit 2 (workspace-size flag)", align=Align.INLINE)
d.comment(0x8F31, "Bit 2 set: keep caller's Y, advance by 2", align=Align.INLINE)
d.comment(0x8F33, "Bit 2 clear: A=&0B (use 11-page minimum)", align=Align.INLINE)
d.comment(0x8F35, "BRA to common tail", align=Align.INLINE)
d.comment(0x8F37, "Bit-2-set path: restore Y", align=Align.INLINE)
d.label(0x8F37, "private_ws_set_bit")

d.comment(0x8F38, "TYA / INY / INY -- raise Y by 2 pages", align=Align.INLINE)
d.comment(0x8F39, "Y += 1", align=Align.INLINE)
d.comment(0x8F3A, "Y += 1 again (total +2)", align=Align.INLINE)
d.comment(0x8F3B, "Push raised Y", align=Align.INLINE)
d.comment(0x8F3C, "Store final page count high to net_rx_ptr_hi", align=Align.INLINE)
d.label(0x8F3C, "commit_workspace_pages")

d.comment(0x8F3E, "Increment for nfs_workspace_hi", align=Align.INLINE)
d.comment(0x8F3F, "Store workspace high page", align=Align.INLINE)
d.comment(0x8F41, "A=0: clear-byte for the lo halves below", align=Align.INLINE)
d.comment(0x8F43, "Clear net_rx_ptr_lo (page-aligned)", align=Align.INLINE)
d.comment(0x8F45, "Clear nfs_workspace_lo (page-aligned)", align=Align.INLINE)
d.comment(0x8F47, "Compute workspace start page via get_ws_page", align=Align.INLINE)
d.comment(0x8F4A, "Y >= &DC?", align=Align.INLINE)
d.comment(0x8F4C, "Restore Y from stack", align=Align.INLINE)
d.comment(0x8F4D, "Yes: jump to set_rom_ws_page (error path)", align=Align.INLINE)
d.comment(0x8F4F, "Return", align=Align.INLINE)
d.entry(0x8F50)


d.subroutine(
    0x8F50,
    "nfs_init_body",
    title="ANFS initialisation body",
    description="""Reached only via PHA/PHA/RTS dispatch (table index 22 in the
svc_dispatch table at `&8A23` / `&8A20`). Carries out the bring-up
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

| svc        | idx   | handler                   | purpose                |
| ---------- | ----- | ------------------------- | ---------------------- |
| `&00..&0C` | 1..13 | (svc-1..12 handlers)      | service-1 .. service-12 |
| `&12`      | 14    | `svc_18_fs_select`        | FS select              |
| `&18`      | 15    | `match_on_suffix`         | Interactive HELP       |
| `&21`      | 16    | `raise_y_to_c8`           | static ws claim        |
| `&22`      | 17    | `set_rom_ws_page`         | dynamic ws offer       |
| `&23`      | 18    | `store_ws_page_count`     | top-of-static-ws       |
| `&24`      | 19    | `noop_dey_rts`            | dynamic ws claim (1 pg) |
| `&25`      | 20    | `copy_template_to_zp`     | FS name + info reply   |
| `&26`      | 21    | `svc_26_close_all_files`  | close all files        |
| `&27`      | 22    | `nfs_init_body` (this)    | reset re-init          |
| `&28`      | 23    | `print_fs_ps_help` | *CONFIGURE option      |
| `&29`      | 24    | `svc_29_status`   | *STATUS option         |

Everything else (svc `&0D..&11`, `&13..&17`, `&19..&20`, `&2A+`)
falls through to
[`dispatch_svc_state_check`](label:dispatch_svc_state_check) with `A := 0` and
dispatches to idx 1 = `dispatch_rts` (no-op) – deliberately
ignoring svc `&15` (100 Hz poll), svc `&2A` (language ROM
startup), etc.""",
)

d.comment(0x8F50, "A=0: clear-byte for the next four stores", align=Align.INLINE)
d.comment(0x8F52, "Clear ws_page (workspace page count)", align=Align.INLINE)
d.comment(0x8F54, "Clear tx_complete_flag", align=Align.INLINE)
d.comment(0x8F57, "Y=0: receive-block offset 0 (remote-op flag)", align=Align.INLINE)
d.comment(0x8F59, "Clear remote-op flag at (net_rx_ptr)+0", align=Align.INLINE)
d.comment(0x8F5B, "Read l028D (current ROM number)", align=Align.INLINE)
d.comment(0x8F5E, "Non-zero (re-init): take nfs_init_check_fs_flags path", align=Align.INLINE)
d.comment(0x8F60, "A=&10: fs_flags bit 4 mask (checks 'workspace already set up')", align=Align.INLINE)
d.comment(0x8F65, "Zero: first ROM init, skip FS setup", align=Align.INLINE)
d.label(0x8F67, "nfs_init_check_fs_flags")

d.comment(0x8F67, "Set up workspace pointers", align=Align.INLINE)
d.comment(0x8F6A, "Clear FS flags", align=Align.INLINE)
d.comment(0x8F71, "A=0, transfer to Y", align=Align.INLINE)
d.label(0x8F72, "loop_zero_workspace")

d.comment(0x8F72, "Clear byte in FS workspace", align=Align.INLINE)
d.comment(0x8F74, "Next workspace byte", align=Align.INLINE)
d.comment(0x8F75, "Loop until full page (256 bytes) cleared", align=Align.INLINE)
d.comment(0x8F77, "Copy initial PS template (1C bytes) into ws", align=Align.INLINE)
d.comment(0x8F7A, "X=1: CMOS &01 = port number", align=Align.INLINE)
d.comment(0x8F7C, "Read CMOS &01", align=Align.INLINE)
d.comment(0x8F7F, "Store at hazel_fs_station (workspace+0)", align=Align.INLINE)
d.comment(0x8F82, "X=2: CMOS &02 = network number", align=Align.INLINE)
d.comment(0x8F84, "Read CMOS &02", align=Align.INLINE)
d.comment(0x8F87, "Store at hazel_fs_network", align=Align.INLINE)
d.comment(0x8F8A, "X=3: CMOS &03 = FS station", align=Align.INLINE)
d.comment(0x8F8C, "Read CMOS &03", align=Align.INLINE)
d.comment(0x8F8F, "A = FS station", align=Align.INLINE)
d.comment(0x8F90, "Y=2: nfs_workspace offset for FS station", align=Align.INLINE)
d.comment(0x8F92, "Store FS station at (nfs_workspace)+2", align=Align.INLINE)
d.comment(0x8F94, "X=4: CMOS &04 = FS network", align=Align.INLINE)
d.comment(0x8F96, "Read CMOS &04 (FS network)", align=Align.INLINE)
d.comment(0x8F99, "A = FS network", align=Align.INLINE)
d.comment(0x8F9A, "Y=3: nfs_workspace offset for FS network", align=Align.INLINE)
d.comment(0x8F9C, "Store at NFS workspace offset 2", align=Align.INLINE)
d.comment(0x8F9E, "X=3: init data byte count", align=Align.INLINE)
d.label(0x8FA0, "loop_copy_init_data")

d.comment(0x8FA0, "Load initialisation data byte", align=Align.INLINE)
d.comment(0x8FA3, "Store in workspace", align=Align.INLINE)
d.comment(0x8FA6, "Decrement counter", align=Align.INLINE)
d.comment(0x8FA7, "More bytes: loop", align=Align.INLINE)
d.comment(0x8FA9, "Clear workspace flag", align=Align.INLINE)
d.comment(0x8FAC, "Clear workspace byte", align=Align.INLINE)
d.comment(0x8FAF, "Initialise ADLC protection table", align=Align.INLINE)
d.comment(0x8FB2, "X=&FF (underflow from X=0)", align=Align.INLINE)
d.comment(0x8FB3, "Initialise workspace flag to &FF", align=Align.INLINE)
d.comment(0x8FB6, "X=&11: CMOS &11 (ANFS settings)", align=Align.INLINE)
d.comment(0x8FB8, "Read CMOS &11", align=Align.INLINE)
d.comment(0x8FBB, "A = settings byte", align=Align.INLINE)
d.comment(0x8FBC, "Mask bit 6 (CMOS protection-state flag)", align=Align.INLINE)
d.comment(0x8FBE, "Bit clear: skip the &FF substitution", align=Align.INLINE)
d.comment(0x8FC0, "A=&FF -- enable protection", align=Align.INLINE)
d.comment(0x8FC2, "Set prot_status/prot_status_save pair", align=Align.INLINE)
d.label(0x8FC2, "init_copy_skip_cmos")

d.label(0x8FC5, "loop_alloc_handles")

d.comment(0x8FC5, "Get current workspace page", align=Align.INLINE)
d.comment(0x8FC7, "Allocate FS handle page", align=Align.INLINE)
d.comment(0x8FCA, "Allocation failed: finish init", align=Align.INLINE)
d.comment(0x8FCC, "A=&3F: default handle permissions", align=Align.INLINE)
d.comment(0x8FCE, "Store handle permissions", align=Align.INLINE)
d.comment(0x8FD0, "Advance to next page", align=Align.INLINE)
d.comment(0x8FD2, "Continue allocating: loop", align=Align.INLINE)
d.label(0x8FD4, "done_alloc_handles")


d.comment(0x8FD4, "Restore FS context from saved state", align=Align.INLINE)
d.comment(0x8FD7, "Read CMOS &00 (= station ID byte)", align=Align.INLINE)
d.label(0x8FD7, "alloc_post_restore_check")

d.comment(0x8FDA, "Y (CMOS value) into A", align=Align.INLINE)
d.comment(0x8FDB, "Non-zero: station ID valid -> alloc_common_entry", align=Align.INLINE)
d.comment(0x8FDD, "Print 'Station number in CMOS RAM invalid...' warning", align=Align.INLINE)
d.label(0x8FDD, "alloc_error_overflow")

d.comment(0x9002, "A=1: default station ID", align=Align.INLINE)
d.comment(0x9004, "BRA to alloc_store_station_id with default", align=Align.INLINE)
d.comment(0x9006, "Check next byte (CMOS station ID hi?)", align=Align.INLINE)
d.label(0x9006, "alloc_common_entry")

d.comment(
    0x9007,
    "INY wrapped past 0 (station=&FF then INY=&00): report 'CMOS RAM invalid' and default to 1",
    align=Align.INLINE,
)
d.comment(0x9009, "BRA to alloc_store_station_id (always)", align=Align.INLINE)
d.comment(0x900B, "Y=1: net_rx_ptr offset for station-ID byte", align=Align.INLINE)
d.label(0x900B, "alloc_store_station_id")

d.comment(0x900D, "Store station ID into (net_rx_ptr)+1", align=Align.INLINE)
d.comment(0x900F, "X=&40: econet_flags init value", align=Align.INLINE)
d.comment(0x9011, "Initialise econet_flags", align=Align.INLINE)
d.comment(0x9014, "Call cmd_net_fs to select NFS", align=Align.INLINE)
d.comment(0x9017, "Z: selection succeeded", align=Align.INLINE)
d.comment(0x9019, "A=&10: bit 4 marker for fs_flags", align=Align.INLINE)
d.comment(0x901E, "Store updated fs_flags", align=Align.INLINE)
d.comment(0x9021, "Initialise ADLC and FILEV/ARGSV/...vectors", align=Align.INLINE)
d.label(0x9021, "complete_nfs_init")

d.comment(0x9024, "A=3: spool-ctrl byte 'init'", align=Align.INLINE)
d.comment(0x9026, "Initialise *SPOOL handle in workspace", align=Align.INLINE)
d.comment(0x9029, "Send a bridge-discovery packet and poll", align=Align.INLINE)
d.comment(0x902C, "Save current bridge byte", align=Align.INLINE)
d.comment(0x902D, "With stored hazel_fs_network (network number)", align=Align.INLINE)
d.comment(0x9030, "Different: take verify_copy_station_id path", align=Align.INLINE)
d.comment(0x9032, "Same: store as new hazel_fs_network", align=Align.INLINE)
d.comment(0x9035, "Y=3: net_rx_ptr offset 3", align=Align.INLINE)
d.comment(0x9037, "Store at (net_rx_ptr)+3", align=Align.INLINE)
d.comment(0x9039, "Restore saved byte", align=Align.INLINE)
d.label(0x9039, "verify_copy_station_id")

d.comment(0x903A, "Y=3: workspace offset", align=Align.INLINE)
d.comment(0x903E, "Mismatch: skip store", align=Align.INLINE)
d.comment(0x9040, "Match: store at (nfs_workspace)+3", align=Align.INLINE)
d.comment(0x9042, "Return", align=Align.INLINE)
d.label(0x9043, "init_adlc_and_vectors")

d.subroutine(
    0x9043,
    "init_adlc_and_vectors",
    title="Initialise ADLC and install extended vectors",
    description="""Reads the ROM pointer table via OSBYTE `&A8`, writes vector
addresses and ROM ID into the extended vector table for `NETV`
and one additional vector, then restores any previous FS context
via [`restore_fs_context`](label:restore_fs_context). Falls through into
[`write_vector_entry`](label:write_vector_entry).""",
    on_exit={"a, x, y": "clobbered (falls through into write_vector_entry)"},
)


d.comment(0x9043, "Initialise ADLC hardware", align=Align.INLINE)
d.comment(0x9046, "OSBYTE &A8: read ROM pointer table", align=Align.INLINE)
d.comment(0x9048, "Read ROM pointer table address", align=Align.INLINE)
d.comment(0x904B, "Store table pointer low", align=Align.INLINE)
d.comment(0x904D, "Store table pointer high", align=Align.INLINE)
d.comment(0x904F, "Y=&36: NETV vector offset", align=Align.INLINE)
d.comment(0x9051, "Set NETV address", align=Align.INLINE)
d.comment(0x9054, "X=1: one more vector pair to set", align=Align.INLINE)
d.label(0x9056, "write_vector_entry")

d.subroutine(
    0x9056,
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


d.comment(0x9056, "Load vector address low byte", align=Align.INLINE)
d.comment(0x9059, "Store into extended vector table", align=Align.INLINE)
d.comment(0x905B, "Advance to high byte", align=Align.INLINE)
d.comment(0x905C, "Load vector address high byte", align=Align.INLINE)
d.comment(0x905F, "Store into extended vector table", align=Align.INLINE)
d.comment(0x9061, "Advance to ROM ID byte", align=Align.INLINE)
d.comment(0x9062, "Load current ROM slot number", align=Align.INLINE)
d.comment(0x9064, "Store ROM ID in extended vector", align=Align.INLINE)
d.comment(0x9066, "Advance to next vector entry", align=Align.INLINE)
d.comment(0x9067, "Decrement vector counter", align=Align.INLINE)
d.comment(0x9068, "More vectors to set: loop", align=Align.INLINE)
d.comment(0x906A, "Return", align=Align.INLINE)
d.label(0x906B, "restore_fs_context")

d.subroutine(
    0x906B,
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


d.comment(0x906B, "Y=9: end of FS context block", align=Align.INLINE)
d.label(0x906D, "loop_restore_ctx")

d.comment(0x906D, "Load FS context byte", align=Align.INLINE)
d.comment(0x9070, "Store into receive block", align=Align.INLINE)
d.comment(0x9072, "Decrement index", align=Align.INLINE)
d.comment(0x9073, "Reached offset 1?", align=Align.INLINE)
d.comment(0x9075, "No: continue copying", align=Align.INLINE)
d.comment(0x9077, "Return", align=Align.INLINE)
d.label(0x9078, "fscv_6_shutdown")

d.subroutine(
    0x9078,
    "fscv_6_shutdown",
    title="Deselect filing system and save workspace",
    description="""If the filing system is currently selected (bit 7 of
[`fs_flags`](label:fs_flags) set):

1. Closes all open FCBs.
2. Closes `*SPOOL`/`*EXEC` files via OSBYTE `&77`.
3. Saves the FS workspace to page `&10` shadow with checksum.
4. Clears the selected flag.""",
)


d.comment(0x9078, "FS currently selected?", align=Align.INLINE)
d.entry(0x9078)
d.comment(0x907B, "No (bit 7 clear): return", align=Align.INLINE)
d.comment(0x907D, "Y=0", align=Align.INLINE)
d.comment(0x907F, "Close all FCBs (process_all_fcbs)", align=Align.INLINE)
d.comment(0x9082, "Restore FS context to receive block", align=Align.INLINE)
d.comment(0x9085, "Y=&76: checksum range end", align=Align.INLINE)
d.comment(0x9087, "A=0: checksum accumulator", align=Align.INLINE)
d.comment(0x9089, "Clear carry for addition", align=Align.INLINE)
d.label(0x908A, "loop_checksum_byte")

d.comment(0x908A, "Add byte from the HAZEL &C2 FCB shadow", align=Align.INLINE)
d.comment(0x908D, "Decrement index", align=Align.INLINE)
d.comment(0x908E, "Loop until all bytes summed", align=Align.INLINE)
d.comment(0x9090, "Y=&77: checksum storage offset", align=Align.INLINE)
d.label(0x9094, "loop_copy_to_ws")

d.comment(0x9094, "Load byte from the HAZEL &C2 FCB shadow", align=Align.INLINE)
d.label(0x9097, "store_ws_byte")

d.comment(0x9097, "Copy to FS workspace", align=Align.INLINE)
d.comment(0x9099, "Decrement index", align=Align.INLINE)
d.comment(0x909A, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x909C, "Load FS flags", align=Align.INLINE)
d.comment(0x909F, "Clear bit 7 (FS no longer selected)", align=Align.INLINE)
d.comment(0x90A1, "Store updated flags", align=Align.INLINE)
d.label(0x90A4, "rts_fs_shutdown")

d.comment(0x90A4, "Return", align=Align.INLINE)
d.label(0x90A5, "verify_ws_checksum")

d.subroutine(
    0x90A5,
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


d.comment(0x90A5, "Save processor status", align=Align.INLINE)
d.comment(0x90A6, "Save A", align=Align.INLINE)
d.comment(0x90A8, "Y=&76: checksum range end", align=Align.INLINE)
d.comment(0x90AA, "A=0: checksum accumulator", align=Align.INLINE)
d.comment(0x90AC, "Clear carry for addition", align=Align.INLINE)
d.label(0x90AD, "loop_sum_ws")

d.comment(0x90AD, "Add byte from FS workspace", align=Align.INLINE)
d.comment(0x90AF, "Decrement index", align=Align.INLINE)
d.comment(0x90B0, "Loop until all bytes summed", align=Align.INLINE)
d.comment(0x90B2, "Y=&77: checksum storage offset", align=Align.INLINE)
d.comment(0x90B4, "Compare with stored checksum", align=Align.INLINE)
d.comment(0x90B6, "Mismatch: raise checksum error", align=Align.INLINE)
d.comment(0x90B9, "Restore A", align=Align.INLINE)
d.comment(0x90BA, "Restore processor status", align=Align.INLINE)
d.comment(0x90BB, "Return (checksum valid)", align=Align.INLINE)
d.label(0x90BC, "error_net_checksum")

d.subroutine(
    0x90BC,
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


d.comment(0x90BC, "Error number &AA", align=Align.INLINE)
d.comment(0x90BE, "Raise 'net checksum' error", align=Align.INLINE)
d.subroutine(
    0x90CE,
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


d.comment(0x90CE, "Print 'Station ' inline string", align=Align.INLINE)
d.comment(0x90D3, "Print 'Econet Station ' via inline", align=Align.INLINE)
d.comment(0x90E0, "Y=1: PB station-byte offset", align=Align.INLINE)
d.comment(0x90E2, "Read RX[1] = station number", align=Align.INLINE)
# UNMAPPED: d.comment(0x90DD, "Print as decimal (no leading zeros)", align=Align.INLINE)
d.comment(0x90E7, "Space character", align=Align.INLINE)
d.comment(0x90E9, "Check ADLC status register 2", align=Align.INLINE)
d.comment(0x90EC, "Clock present: skip warning", align=Align.INLINE)
d.comment(0x90EE, "Print ' No Clock' via inline", align=Align.INLINE)
d.comment(0x90FA, "String terminator", align=Align.INLINE)
d.label(0x90FB, "done_print_newline")

d.comment(0x90FE, "Return", align=Align.INLINE)
d.index_base(0x90FF, "cmd_syntax_strings")
d.banner(
    0x90FF,
    title="*HELP / *SYNTAX argument strings (8 messages)",
    description="""Eight zero-terminated argument-syntax strings used by the *HELP
text builder. Each string describes the argument shape of a
particular command group; their offsets within this table are
stored in [`cmd_syntax_table`](label:cmd_syntax_table), keyed by command
index. Read by [`do_print_no_spool`](label:do_print_no_spool) when no command
argument was supplied.""",
)

d.index_base(0x90FF, "syn_opt_dir")

d.comment(
    0x90FF,
    """*HELP command syntax strings

13 null-terminated syntax help strings displayed
by *HELP after each command name. Multi-line
entries use &0D as a line break. Indexed by
cmd_syntax_table via the low 5 bits of each
command's syntax descriptor byte.""",
)
d.comment(0x90FF, "Syn 1: *Dir, *LCat, *LEx, *Wipe", align=Align.INLINE)
d.label(0x9107, "syn_iam")

d.comment(0x9107, "Syn 2: *I Am (login)", align=Align.INLINE)
d.comment(0x911F, "Line break", align=Align.INLINE)
d.comment(0x9120, "syntax help for *Pass / *I am", align=Align.INLINE)
d.label(0x9134, "syn_object")

d.comment(0x9134, "Syn 3: *Delete, *FS, *Remove", align=Align.INLINE)
d.comment(0x914D, "Store as string pointer low", align=Align.INLINE)
d.comment(0x9150, "Store as string pointer high", align=Align.INLINE)
d.comment(0x9153, "Syn 4 continued: address clause", align=Align.INLINE)
d.comment(0x915F, "Null terminator", align=Align.INLINE)
d.label(0x9160, "syn_dir")

d.comment(0x9160, "Syn 5: *Lib", align=Align.INLINE)
d.label(0x9177, "syn_password")

d.comment(0x9177, "Syn 7: *Pass", align=Align.INLINE)
d.comment(0x918B, "Syn 7 continued: new password", align=Align.INLINE)
d.comment(0x919A, "syntax help for *PS / *Pollps", align=Align.INLINE)
d.label(0x91B3, "syn_access")

d.comment(0x91B3, "Syn 9: *Access", align=Align.INLINE)
d.comment(0x91CE, "Null terminator", align=Align.INLINE)
d.label(0x91CF, "syn_rename")

d.comment(0x91CF, "Syn 10: *Rename", align=Align.INLINE)
d.comment(0x91E8, "Null terminator", align=Align.INLINE)
d.label(0x91E9, "syn_opt_stn")

d.comment(0x91E9, "Syn 11: (station id. argument)", align=Align.INLINE)
# UNMAPPED: d.comment(0x91EC, "Null terminator", align=Align.INLINE)
d.index_base(0x91F5, "cmd_syntax_table")
d.banner(
    0x91F5,
    title="Argument-syntax offset table (12 entries)",
    description="""Twelve byte offsets indexing into
[`syn_opt_dir`](label:syn_opt_dir). Each entry is computed as
`<syn_X> - syn_opt_dir - 1` so the print loop can `INY`
before `LDA` and still land on the first byte of the chosen
string. The byte at &91F9 immediately after the table is the
entry point of [`print_no_spool`](address:91F9).""",
)
for i in range(12):
    d.byte(0x91F5 + i)
d.expr(0x91F5, sym("syn_iam") - sym("syn_opt_dir") - 2)
d.comment(
    0x91F5,
    """Command syntax string offset table

13 offsets into syn_opt_dir (&9022).
Indexed by the low 5 bits of each command table
syntax descriptor byte. Index &0E is handled
separately as a shared-commands list. The print
loop at &8BD5 does INY before LDA, so each offset
points to the byte before the first character.""",
)
d.comment(0x91F5, "Idx 0: 'opt_dir' (offset -2 variant for *Dir's INY-twice walker)", align=Align.INLINE)
d.comment(0x91F6, "Idx 1: &FF = no syntax string for this index", align=Align.INLINE)
d.expr(0x91F7, sym("syn_iam") - sym("syn_opt_dir") - 1)
d.comment(0x91F7, 'Idx 2: \\"(<stn.id.>) <user id.>...\\"', align=Align.INLINE)
d.expr(0x91F8, sym("syn_object") - sym("syn_opt_dir") - 1)
d.comment(0x91F8, 'Idx 3: \\"<object>\\"', align=Align.INLINE)
d.comment(0x91F9, 'Idx 4: \\"<filename> (<offset>...)\\"', align=Align.INLINE)
d.comment(0x91FA, "Idx 5: '<dir>' (offset 0x60 = syn_dir)", align=Align.INLINE)
d.comment(0x91FB, "Idx 6: continued <dir> string region", align=Align.INLINE)
d.comment(0x91FC, 'Idx 7: \\"(:<CR>) <password>...\\"', align=Align.INLINE)
d.comment(0x91FD, 'Idx 8: \\"(<stn.id.>|<ps type>)\\"', align=Align.INLINE)
# UNMAPPED: d.expr(0x91F6, "syn_access - syn_opt_dir - 1")
# UNMAPPED: d.comment(0x91F6, 'Idx 9: \\"<object> (L)(W)(R)...\\"', align=Align.INLINE)
# UNMAPPED: d.comment(0x91F7, "Idx 10: '<filename> <new filename>' (syn_rename)", align=Align.INLINE)
# UNMAPPED: d.expr(0x91F8, "syn_opt_stn - syn_opt_dir - 1")

# UNMAPPED: d.comment(0x91F8, 'Idx 11: \\"(<stn. id.>)\\"', align=Align.INLINE)
d.subroutine(
    0x9202,
    "print_newline_no_spool",
    title="Print CR via OSASCI, bypassing any open *SPOOL file",
    description="""Loads `A=&0D` and falls into
[`print_char_no_spool`](label:print_char_no_spool). The underlying
mechanism temporarily writes `0` to the `*SPOOL` file handle
(OSBYTE `&C7` with `X=0`, `Y=0`) so the printed `CR` is not
captured by spool, then restores the previous handle on exit.

Called from [`service_handler`](label:service_handler) (`&8AB4`) after
the `'Bad ROM <slot>'` message, and from two other diagnostic
sites (`&8E28`, `&9D3C`).""",
    on_entry={},
    on_exit={
        "a, x, y, p": "preserved (print_char_no_spool brackets the call with full register save/restore via PHA/PHP/PLP/PLA)"
    },
)


d.comment(0x9202, "A=&0D (CR) for OSASCI translation; fall through", align=Align.INLINE)
d.subroutine(
    0x9204,
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

Eight inner-ROM callers: `&9268`, `&92AD`, `&9D2E`, `&9D5A`,
`&B21F`, `&B2F9`, `&B321`, `&B77B`.""",
    on_entry={"a": "byte to print as ASCII char (CR is translated by OSASCI)"},
)


d.comment(0x9204, "Save caller's flags (V from caller is irrelevant — see &91FC)", align=Align.INLINE)
d.comment(0x9205, "Unconditionally sets V=1 (bit 6 of operand &FF)", align=Align.INLINE)
d.comment(0x9208, "V=1 always, branch always taken (skips the CLV path)", align=Align.INLINE)
d.subroutine(
    0x920A,
    "print_byte_no_spool",
    title="Print A via OSWRCH (raw, no CR translation), bypass *SPOOL",
    description="""As [`print_char_no_spool`](label:print_char_no_spool) but the inner
`PHP`/`CLV` at `&9201` forces `V=0` in the saved flags, so the
`BVC` at `&9229` takes the `OSWRCH` branch instead of `OSASCI`.

Used when the caller wants to emit a raw byte (e.g. a VDU
control code) without `CR` translation. Sole caller in this ROM
is at `&8DE6`.""",
    on_entry={"a": "raw byte to print via OSWRCH"},
)


d.comment(0x920A, "Alt entry: save caller's flags BEFORE forcing V=0", align=Align.INLINE)
d.comment(0x920B, "Force V=0 -> OSWRCH path at &9229 (raw byte)", align=Align.INLINE)
d.label(0x920C, "save_regs_print_no_spool")

d.comment(0x920C, "Save X", align=Align.INLINE)
d.comment(0x920D, "Save Y", align=Align.INLINE)
d.comment(0x920E, "Save A (the byte to print)", align=Align.INLINE)
d.comment(0x920F, "Save inner P — V here picks OSASCI vs OSWRCH later", align=Align.INLINE)
d.comment(0x9210, "OSBYTE 199 (read/write *SPOOL file handle)", align=Align.INLINE)
d.comment(0x9212, "X=0: handle value to write", align=Align.INLINE)
d.comment(0x9214, "Y=0: write mode (NEW = (OLD AND 0) EOR X = X = 0)", align=Align.INLINE)
d.comment(0x9216, "Closes spool; X returns OLD handle", align=Align.INLINE)
d.comment(0x9219, "OLD < ' '? (likely 0 = was already closed)", align=Align.INLINE)
d.comment(0x921B, "Yes: leave spool closed for the print", align=Align.INLINE)
d.comment(0x921D, "OLD >= '0'?", align=Align.INLINE)
d.comment(0x921F, "Yes (>= &30): leave spool closed", align=Align.INLINE)
d.comment(0x9221, "OLD in [&20,&2F] (NFS handle range): re-open spool with X=OLD", align=Align.INLINE)
d.comment(0x9224, "Clear X for the post-print restore", align=Align.INLINE)
d.label(0x9226, "do_print_no_spool")

d.comment(0x9226, "Restore inner P (V=1 OSASCI / V=0 OSWRCH)", align=Align.INLINE)
d.comment(0x9227, "Pull A (the byte)", align=Align.INLINE)
d.comment(0x9228, "Push it back so the final epilogue PLA still works", align=Align.INLINE)
d.comment(0x9229, "V=0 -> OSWRCH (raw); V=1 -> OSASCI (CR translation)", align=Align.INLINE)
d.comment(0x922B, "OSASCI: writes A, translating CR to CR/LF", align=Align.INLINE)
d.comment(0x922E, "Skip OSWRCH branch", align=Align.INLINE)
d.label(0x9230, "print_via_oswrch")

d.comment(0x9230, "OSWRCH: writes A as a raw byte", align=Align.INLINE)
d.label(0x9233, "restore_spool_and_return")

d.comment(0x9233, "OSBYTE 199 again to restore spool state", align=Align.INLINE)
d.comment(0x9235, "Y=&FF (read mode): NEW = OLD EOR X", align=Align.INLINE)
d.comment(0x9237, "X=0 -> no change; X=OLD -> writes OLD back", align=Align.INLINE)
d.comment(0x923A, "Pull A (preserved across the call)", align=Align.INLINE)
d.comment(0x923B, "Pull Y", align=Align.INLINE)
d.comment(0x923C, "Pull X", align=Align.INLINE)
d.comment(0x923D, "Pull caller's original flags", align=Align.INLINE)
d.comment(0x923E, "Return", align=Align.INLINE)
d.label(0x923F, "print_hex_byte")

d.subroutine(
    0x923F,
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


d.comment(0x923F, "Save full byte", align=Align.INLINE)
d.comment(0x9240, "Shift high nybble to low", align=Align.INLINE)
d.comment(0x9241, "Continue shifting", align=Align.INLINE)
d.comment(0x9242, "Continue shifting", align=Align.INLINE)
d.comment(0x9243, "High nybble now in bits 0-3", align=Align.INLINE)
d.comment(0x9244, "Print high nybble as hex digit", align=Align.INLINE)
d.comment(0x9247, "Restore full byte", align=Align.INLINE)
d.label(0x9248, "print_hex_nybble")

d.subroutine(
    0x9248,
    "print_hex_nybble",
    title="Print low nybble of A as hex digit",
    description="""Masks `A` to the low 4 bits, then converts to ASCII:

1. Adds 7 for letters `A`..`F` (via `ADC #6` with carry set from
   the `CMP`).
2. `ADC #&30` for the final `'0'`..`'F'` character.
3. Outputs via `JMP OSASCI`.""",
    on_entry={"a": "value (low nybble used)"},
)


d.comment(0x9248, "Mask to low nybble", align=Align.INLINE)
d.comment(0x924A, "Digit >= &0A?", align=Align.INLINE)
d.comment(0x924C, "No: skip letter adjustment", align=Align.INLINE)
d.comment(0x924E, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.label(0x9250, "add_ascii_base")

d.comment(0x9250, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.subroutine(
    0x9255,
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


d.comment(0x9255, "Save full byte", align=Align.INLINE)
d.comment(0x9256, "Shift high nybble to low (LSR x4)", align=Align.INLINE)
d.comment(0x9257, "LSR / LSR / LSR -- shift hi nibble down to lo", align=Align.INLINE)
d.comment(0x9258, "(continued)", align=Align.INLINE)
d.comment(0x9259, "(continued)", align=Align.INLINE)
d.comment(0x925A, "Print high nybble as hex digit", align=Align.INLINE)
d.comment(0x925D, "Restore full byte; fall through for low nybble", align=Align.INLINE)
d.subroutine(
    0x925E,
    "print_hex_nybble_no_spool",
    title="Print low nybble of A as one hex digit, *SPOOL-bypassing",
    description="As print_hex_nybble (&923F) but emits via the print_char_no_spool tail-call instead of OSASCI directly, so the digit is not captured by any active *SPOOL file. Standard AND #&0F / CMP #&0A / +6-or-not / + #&30 mapping for hex digits 0-9 / A-F. Tail-jumps to print_char_no_spool via BRA.",
    on_entry={"a": "value (low nybble used)"},
)


d.comment(0x925E, "Mask to low nybble", align=Align.INLINE)
d.comment(0x9260, "Digit >= &0A?", align=Align.INLINE)
d.comment(0x9262, "No: skip letter adjustment", align=Align.INLINE)
d.comment(0x9264, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.label(0x9266, "print_nybble_leading_zero")

d.comment(0x9266, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.comment(0x9268, "Tail-jump to *SPOOL-bypassing print", align=Align.INLINE)
d.hook_subroutine(0x926A, "print_inline", stringhi_hook)
d.subroutine(
    0x926A,
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


d.comment(0x926A, "Pop return address (low) — points to last byte of JSR", align=Align.INLINE)
d.comment(0x926B, "Store as fs_error_ptr (return-addr saved)", align=Align.INLINE)
d.comment(0x926D, "Pop return address (high)", align=Align.INLINE)
d.comment(0x926E, "Store as fs_crflag (entry flag)", align=Align.INLINE)
d.comment(0x9270, "Y=0: start scanning at offset 0", align=Align.INLINE)
d.label(0x9272, "loop_next_char")

d.subroutine(
    0x9272,
    "loop_next_char",
    title="print_inline pointer-advance step",
    description="""`INC fs_error_ptr` (lo); on overflow `INC fs_crflag` (hi). Single
caller (the loop tail at `&9284` inside
[`print_inline`](label:print_inline)). Falls through to `load_char`
which reads the next inline-string byte.""",
)


d.comment(0x9272, "Advance pointer to next character", align=Align.INLINE)
d.comment(0x9274, "Z clear: continue with this char", align=Align.INLINE)
d.comment(0x9276, "Z set (CR): increment fs_crflag", align=Align.INLINE)
d.label(0x9278, "load_char")

d.comment(0x9278, "Load next byte from inline string", align=Align.INLINE)
d.comment(0x927A, "Bit 7 set? Done — this byte is the next opcode", align=Align.INLINE)
d.comment(0x927C, "Read fs_error_ptr (saved across OSASCI)", align=Align.INLINE)
d.comment(0x927E, "Push it", align=Align.INLINE)
d.comment(0x927F, "Read fs_crflag", align=Align.INLINE)
d.comment(0x9281, "Push it", align=Align.INLINE)
d.comment(0x9282, "Reload character (pointer may have been clobbered)", align=Align.INLINE)
d.comment(0x9284, "Print character via OSASCI", align=Align.INLINE)
d.comment(0x9287, "Pop saved fs_crflag", align=Align.INLINE)
d.comment(0x9288, "Restore fs_crflag", align=Align.INLINE)
d.comment(0x928A, "Pop saved fs_error_ptr", align=Align.INLINE)
d.comment(0x928B, "Restore fs_error_ptr", align=Align.INLINE)
d.comment(0x928D, "Loop back", align=Align.INLINE)
d.label(0x9290, "resume_caller")

d.comment(0x9290, "Jump to address of high-bit byte (resumes code)", align=Align.INLINE)


d.hook_subroutine(0x9293, "print_inline_no_spool", stringhi_hook)
d.subroutine(
    0x9293,
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

Six callers: `&9818` (`recv_and_process_reply`), `&B18B`/`&B195`
([`cmd_ex`](label:cmd_ex)), `&B323` (`ex_print_col_sep`),
`&B787` ([`cmd_wipe`](label:cmd_wipe)), `&B7CB`
(`prompt_yn`).""",
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)", "x": "corrupted (by print_char_no_spool)", "y": "0"},
)
d.comment(0x9293, "Pop return-addr low byte (-> string pointer low)", align=Align.INLINE)
d.comment(0x9294, "Save in fs_error_ptr (the loop's pointer low)", align=Align.INLINE)
d.comment(0x9296, "Pop return-addr high byte", align=Align.INLINE)
d.comment(0x9297, "Save in fs_crflag (the loop's pointer high)", align=Align.INLINE)
d.comment(0x9299, "Y=0: indirect index for (fs_error_ptr),Y", align=Align.INLINE)
d.label(0x929B, "loop_print_inline_string")


d.comment(0x929B, "Step pointer low byte to next char", align=Align.INLINE)
d.comment(0x929D, "No carry: skip high-byte INC", align=Align.INLINE)
d.comment(0x929F, "Page wrap: bump pointer high", align=Align.INLINE)
d.label(0x92A1, "print_next_string_char")

d.comment(0x92A1, "Read next character from inline string", align=Align.INLINE)
d.comment(0x92A3, "Bit 7 set: terminator -- this byte is the next opcode", align=Align.INLINE)
d.comment(0x92A5, "Save pointer low (print_char_no_spool may clobber)", align=Align.INLINE)
d.comment(0x92A7, "Push it", align=Align.INLINE)
d.comment(0x92A8, "Save pointer high", align=Align.INLINE)
d.comment(0x92AA, "Push it", align=Align.INLINE)
d.comment(0x92AB, "Reload the character we're about to print", align=Align.INLINE)
d.comment(0x92AD, "Print it via the *SPOOL-bypassing OSASCI wrapper", align=Align.INLINE)
d.comment(0x92B0, "Pop pointer high back", align=Align.INLINE)
d.comment(0x92B1, "Restore", align=Align.INLINE)
d.comment(0x92B3, "Pop pointer low back", align=Align.INLINE)
d.comment(0x92B4, "Restore", align=Align.INLINE)
d.comment(0x92B6, "Always taken (BRA-style; A is non-zero from print)", align=Align.INLINE)
d.label(0x92B8, "print_char_terminator")

d.comment(
    0x92B8, "Resume execution at the terminator byte's address (JMP indirect via fs_error_ptr)", align=Align.INLINE
)
d.subroutine(
    0x92BB,
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


d.comment(0x92BB, "Zero the accumulator (fs_load_addr_2)", align=Align.INLINE)
d.comment(0x92BD, "Read first command-line byte", align=Align.INLINE)
d.comment(0x92BF, "Hex prefix '&'?", align=Align.INLINE)
d.comment(0x92C1, "No: try decimal path", align=Align.INLINE)
d.comment(0x92C3, "Yes: skip the '&'", align=Align.INLINE)
d.comment(0x92C4, "Read first hex digit", align=Align.INLINE)
d.comment(0x92C6, "Always taken (CMP #'&' set C if A>='&'); jump into the hex digit-range check", align=Align.INLINE)
d.label(0x92C8, "next_hex_char")

d.comment(0x92C8, "Step to next character", align=Align.INLINE)
d.comment(0x92C9, "Read next hex digit candidate", align=Align.INLINE)
d.comment(0x92CB, "Dot? Net.station separator", align=Align.INLINE)
d.comment(0x92CD, "Yes: switch to station-parsing mode", align=Align.INLINE)
d.comment(0x92CF, "Below '!' (CR/space)? End of argument", align=Align.INLINE)
d.comment(0x92D1, "Yes: number complete", align=Align.INLINE)
d.label(0x92D3, "check_digit_range")

d.comment(0x92D3, "Below '0'?", align=Align.INLINE)
d.comment(0x92D5, "Yes: not a hex digit", align=Align.INLINE)
d.comment(0x92D7, "Above '9'? (CMP #':')", align=Align.INLINE)
d.comment(0x92D9, "No (it's '0'-'9'): straight to digit extraction", align=Align.INLINE)
d.comment(0x92DB, "Force uppercase via AND #&5F", align=Align.INLINE)
d.comment(0x92DD, "Map 'A'-'F' to &FA-&FF (ADC #&B8 with C from earlier CMP #':' which set C)", align=Align.INLINE)
d.comment(0x92DF, "Carry out of ADC: was below 'A' -- bad hex", align=Align.INLINE)
d.comment(0x92E1, "Below &FA? (digit > 'F' overflowed past)", align=Align.INLINE)
d.label(0x92E3, "skip_if_not_hex")

d.comment(0x92E3, "Yes: bad hex (out of [&FA,&FF])", align=Align.INLINE)
d.label(0x92E5, "extract_digit_value")

d.comment(0x92E5, "Mask to nibble", align=Align.INLINE)
d.comment(0x92E7, "Stash digit value in fs_load_addr_3", align=Align.INLINE)
d.comment(0x92E9, "Load accumulator", align=Align.INLINE)
d.comment(0x92EB, "Above 16? (would overflow when shifted left 4)", align=Align.INLINE)
d.comment(0x92ED, "Yes: overflow", align=Align.INLINE)
d.comment(0x92EF, "Shift accumulator left 4 (multiply by 16)", align=Align.INLINE)
d.comment(0x92F0, "(shift 2)", align=Align.INLINE)
d.comment(0x92F1, "(shift 3)", align=Align.INLINE)
d.comment(0x92F2, "(shift 4)", align=Align.INLINE)
d.comment(0x92F3, "Add new nibble", align=Align.INLINE)
d.comment(0x92F5, "Save updated accumulator", align=Align.INLINE)
d.comment(0x92F7, "No carry: continue (always taken since accumulator was checked < 16 above)", align=Align.INLINE)
d.label(0x92F9, "next_dec_char")

d.comment(0x92F9, "Read next decimal-digit candidate", align=Align.INLINE)
d.comment(0x92FB, "Dot? Net.station separator", align=Align.INLINE)
d.comment(0x92FD, "Yes: switch to station-parsing mode", align=Align.INLINE)
d.comment(0x92FF, "Below '!' (CR/space)?", align=Align.INLINE)
d.comment(0x9301, "Yes: number complete", align=Align.INLINE)
d.comment(0x9303, "Test for '0'-'9' and reject '&'/'.'", align=Align.INLINE)
d.comment(0x9306, "Not a decimal digit: bad number", align=Align.INLINE)
d.comment(0x9308, "Mask to nibble", align=Align.INLINE)
d.comment(0x930A, "Stash digit", align=Align.INLINE)
d.comment(0x930C, "Accumulator * 2", align=Align.INLINE)
d.comment(0x930E, "Overflowed: too big for byte", align=Align.INLINE)
d.comment(0x9310, "Reload doubled value", align=Align.INLINE)
d.comment(0x9312, "* 2 again (now * 4)", align=Align.INLINE)
d.comment(0x9313, "Overflow check", align=Align.INLINE)
d.comment(0x9315, "* 2 again (now * 8)", align=Align.INLINE)
d.comment(0x9316, "Overflow check", align=Align.INLINE)
d.comment(0x9318, "+ accumulator (now * 8 + * 2 = * 10)", align=Align.INLINE)
d.comment(0x931A, "Overflow check", align=Align.INLINE)
d.comment(0x931C, "+ new digit", align=Align.INLINE)
d.comment(0x931E, "Overflow check", align=Align.INLINE)
d.comment(0x9320, "Save * 10 + digit", align=Align.INLINE)
d.comment(0x9322, "Step input cursor", align=Align.INLINE)
d.comment(0x9323, "Always taken (Y wraps at 256, never zero in practice)", align=Align.INLINE)
d.label(0x9325, "done_parse_num")

d.comment(0x9325, "Read mode flag", align=Align.INLINE)
d.comment(0x9327, "Bit 7 clear: in net.station mode -- validate result", align=Align.INLINE)
d.comment(0x9329, "Decimal-only mode: get result", align=Align.INLINE)
d.comment(0x932B, "Result is zero: bad parameter", align=Align.INLINE)
d.comment(0x932D, "Return with parsed result in A (decimal-only path)", align=Align.INLINE)
d.label(0x932E, "validate_station")

d.comment(0x932E, "Reload result", align=Align.INLINE)
d.comment(0x9330, "Station 255 is reserved (broadcast)", align=Align.INLINE)
d.comment(0x9332, "Yes: bad station number", align=Align.INLINE)
d.comment(0x9334, "Reload result for the next test", align=Align.INLINE)
d.comment(0x9336, "Non-zero: valid station, return", align=Align.INLINE)
d.comment(0x9338, "Zero result: must have followed a dot to be valid", align=Align.INLINE)
d.comment(0x933A, "No dot was seen: bad station number", align=Align.INLINE)
d.comment(0x933C, "Dot seen: peek the byte before current cursor", align=Align.INLINE)
d.comment(0x933D, "Read previous byte", align=Align.INLINE)
d.comment(0x933F, "Restore Y", align=Align.INLINE)
d.comment(0x9340, "Was previous char '.'?", align=Align.INLINE)
d.comment(0x9342, "No: bad station number", align=Align.INLINE)
d.label(0x9344, "return_parsed")

d.comment(0x9344, "All checks passed: C=1 marks 'parsed successfully'", align=Align.INLINE)
d.comment(0x9345, "Return", align=Align.INLINE)
d.label(0x9346, "handle_dot_sep")

d.comment(0x9346, "Dot already seen?", align=Align.INLINE)
d.comment(0x9348, "Yes: 'Bad number' (multiple dots)", align=Align.INLINE)
d.comment(0x934A, "Set dot-seen flag", align=Align.INLINE)
d.comment(0x934C, "Get parsed network number (before dot)", align=Align.INLINE)
d.comment(0x934E, "Network 255 is reserved", align=Align.INLINE)
d.comment(0x9350, "Yes: 'Bad network number'", align=Align.INLINE)
d.comment(0x9352, "Return; caller continues parsing the station", align=Align.INLINE)
d.label(0x9353, "err_bad_hex")

d.subroutine(
    0x9353,
    "err_bad_hex",
    title="Raise 'Bad hex' BRK error",
    description="""Loads error code `&F1` and tail-calls `error_bad_inline` with
the inline string `'hex'` – `error_bad_inline` prepends `'Bad '`
to produce the final `'Bad hex'` message. Called from
[`parse_addr_arg`](label:parse_addr_arg) and the `*DUMP` / `*LIST`
hex parsers when a digit is out of range. Never returns.""",
)


d.comment(0x9353, "Error code &F1", align=Align.INLINE)
d.comment(0x9355, "Raise 'Bad hex' error", align=Align.INLINE)
d.label(0x935C, "error_overflow")

d.comment(0x935C, "Test fs_work_4 bit 7", align=Align.INLINE)
d.comment(0x935E, "Bit 7 set: redirect to error_bad_param", align=Align.INLINE)
d.label(0x9360, "err_bad_station_num")

d.comment(0x9360, "A=&D0: 'Bad station' error code", align=Align.INLINE)
d.comment(0x9362, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x9374, "error_bad_number")

d.comment(0x9374, "A=&F0: 'Bad number' error code", align=Align.INLINE)
d.comment(0x9376, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x9380, "error_bad_param")

d.comment(0x9380, "A=&94: 'Bad parameter' error code", align=Align.INLINE)
d.comment(0x9382, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x938F, "error_bad_net_num")

d.comment(0x938F, "A=&D1: 'Bad net number' error code", align=Align.INLINE)
d.comment(0x9391, "Raise via error_bad_inline (never returns)", align=Align.INLINE)
d.label(0x939F, "is_decimal_digit")

d.subroutine(
    0x939F,
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


d.comment(0x939F, "Hex prefix '&'?", align=Align.INLINE)
d.comment(0x93A1, "Yes: treat as digit-like (carry set on exit)", align=Align.INLINE)
d.comment(0x93A3, "Network/station separator '.'?", align=Align.INLINE)
d.comment(0x93A5, "Yes: also digit-like; else fall through to decimal test", align=Align.INLINE)
d.label(0x93A7, "is_dec_digit_only")

d.subroutine(
    0x93A7,
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


d.comment(0x93A7, "Above '9'? (CMP #':')", align=Align.INLINE)
d.comment(0x93A9, "Yes: not a digit -- jump to clear-carry exit", align=Align.INLINE)
d.comment(0x93AB, "Below '0'? (CMP sets carry if A >= '0')", align=Align.INLINE)
d.label(0x93AD, "rts_digit_test")

d.comment(0x93AD, "Carry now reflects '0'-'9' membership; return", align=Align.INLINE)
d.label(0x93AE, "not_a_digit")

d.comment(0x93AE, "Out-of-range exit: clear carry to signal not-a-digit", align=Align.INLINE)
d.comment(0x93AF, "Return", align=Align.INLINE)
d.label(0x93B0, "get_access_bits")

d.subroutine(
    0x93B0,
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


d.comment(0x93B0, "Y=&0E: directory entry access byte offset", align=Align.INLINE)
d.comment(0x93B2, "Read access byte through fs_options pointer", align=Align.INLINE)
d.comment(0x93B4, "Mask to 6 protection bits (clears the unused top two)", align=Align.INLINE)
d.comment(0x93B6, "X=4: encode-table column index for owner-access bits", align=Align.INLINE)
d.comment(0x93B8, "Always taken: LDX #4 cleared Z, so BNE is unconditional", align=Align.INLINE)
d.label(0x93BA, "get_prot_bits")

d.subroutine(
    0x93BA,
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


d.comment(0x93BA, "Mask to 5 protection bits (low 5)", align=Align.INLINE)
d.comment(0x93BC, "X=&FF; INX inside the loop bumps to 0 for column 0", align=Align.INLINE)
d.label(0x93BE, "begin_prot_encode")

d.comment(0x93BE, "Park source bits in fs_error_ptr -- the LSR target", align=Align.INLINE)
d.comment(0x93C0, "A=0: accumulator for encoded result", align=Align.INLINE)
d.label(0x93C2, "loop_encode_prot")

d.comment(0x93C2, "Advance table column index", align=Align.INLINE)
d.comment(0x93C3, "Shift next source bit into carry", align=Align.INLINE)
d.comment(0x93C5, "Source bit was 0: skip the OR for this column", align=Align.INLINE)
d.comment(0x93C7, "Source bit was 1: OR in this column's encoded mask", align=Align.INLINE)
d.label(0x93CA, "skip_clear_prot")


d.comment(
    0x93CA,
    "Continue while either fs_error_ptr or A is non-zero (loop ends when source exhausted and result still 0)",
    align=Align.INLINE,
)
d.comment(0x93CC, "Return with encoded value in A", align=Align.INLINE)
d.subroutine(
    0x93CD,
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
    d.byte(0x93CD + i)
d.comment(0x93CD, "prot src bit 0 -> out bits 6,4", align=Align.INLINE)
d.comment(0x93CE, "prot src bit 1 -> out bit 5", align=Align.INLINE)
d.comment(0x93CF, "prot src bit 2 -> out bits 2,0", align=Align.INLINE)
d.comment(0x93D0, "prot src bit 3 -> out bit 1", align=Align.INLINE)
d.comment(0x93D1, "prot src bit 4 -> out bits 7,3", align=Align.INLINE)
d.comment(0x93D2, "access src bit 0 -> out bit 2", align=Align.INLINE)
d.comment(0x93D3, "access src bit 1 -> out bit 3", align=Align.INLINE)
d.comment(0x93D4, "access src bit 2 -> out bit 7", align=Align.INLINE)
d.comment(0x93D5, "access src bit 3 -> out bit 4", align=Align.INLINE)
d.comment(0x93D6, "access src bit 4 -> out bit 0", align=Align.INLINE)
d.comment(0x93D7, "access src bit 5 -> out bit 1", align=Align.INLINE)

d.label(0x93D8, "set_text_and_xfer_ptr")

d.subroutine(
    0x93D8,
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


d.comment(0x93D8, "Save text pointer low byte (where caller wants OS to scan from)", align=Align.INLINE)
d.comment(0x93DA, "Save text pointer high byte; fall through to set_xfer_params", align=Align.INLINE)
d.label(0x93DC, "set_xfer_params")

d.subroutine(
    0x93DC,
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


d.comment(0x93DC, "Stash transfer byte count (in A)", align=Align.INLINE)
d.comment(0x93DE, "Source pointer low byte", align=Align.INLINE)
d.comment(0x93E0, "Source pointer high byte; fall through to set_options_ptr", align=Align.INLINE)
d.label(0x93E2, "set_options_ptr")

d.subroutine(
    0x93E2,
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


d.comment(0x93E2, "Options pointer low byte (parameter block base)", align=Align.INLINE)
d.comment(0x93E4, "Options pointer high byte; fall through to clear_escapable", align=Align.INLINE)
d.label(0x93E6, "clear_escapable")

d.subroutine(
    0x93E6,
    "clear_escapable",
    title="Clear bit 0 of need_release_tube preserving flags",
    description="""PHP / LSR need_release_tube / PLP / RTS. Shifts bit 0 of
need_release_tube into carry while clearing it, then restores the
caller's flags so the operation is invisible to NZC-sensitive
code. Single caller (&9B70 in the recv-and-classify reply path).""",
)


d.comment(0x93E6, "Save flags so the LSR doesn't disturb caller's NZC", align=Align.INLINE)
d.comment(0x93E7, "Shift bit 0 of need_release_tube into carry, clearing the bit", align=Align.INLINE)
d.comment(0x93E9, "Restore caller's flags", align=Align.INLINE)
d.comment(0x93EA, "Return", align=Align.INLINE)
d.label(0x93EB, "cmp_5byte_handle")

d.subroutine(
    0x93EB,
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


d.comment(0x93EB, "X=4: loop from offset 4 down to 1 (skips offset 0)", align=Align.INLINE)
d.label(0x93ED, "loop_cmp_handle")

d.comment(0x93ED, "Load saved-handle byte from addr_work[X]", align=Align.INLINE)
d.comment(0x93EF, "EOR with parsed handle byte; Z set iff bytes match", align=Align.INLINE)
d.comment(0x93F1, "Mismatch: bail out with Z clear", align=Align.INLINE)
d.comment(0x93F3, "Decrement to next byte", align=Align.INLINE)
d.comment(0x93F4, "Loop while X != 0 (offset 0 is intentionally not compared)", align=Align.INLINE)
d.label(0x93F6, "rts_cmp_handle")

d.comment(0x93F6, "Return; Z reflects last EOR (set = match, clear = mismatch)", align=Align.INLINE)
d.label(0x93F7, "fscv_7_read_handles")

d.subroutine(
    0x93F7,
    "fscv_7_read_handles",
    title="FSCV reason 7: report FCB handle range",
    description="""Returns the FCB handle range to the caller: `X=&20` (lowest valid
handle) and `Y=&2F` (highest valid handle), then `RTS`. Reached
via the FSCV vector with reason code 7. Used by the OS to discover
which handle values this filing system claims.""",
    on_exit={"x": "&20 (first valid FCB handle)", "y": "&2F (last valid FCB handle)"},
)


d.comment(0x93F7, "X=&20: handle-table base offset", align=Align.INLINE)
d.entry(0x93F7)
d.comment(0x93F9, "Y=&2F: handle count + flag", align=Align.INLINE)
d.comment(0x93FB, "Return", align=Align.INLINE)
d.label(0x93FC, "set_conn_active")

d.subroutine(
    0x93FC,
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


d.comment(0x93FC, "Save flags so the rest of the routine is transparent", align=Align.INLINE)
d.entry(0x93FC)
d.comment(0x93FD, "Save A (the attribute byte we need to recover via stack)", align=Align.INLINE)
d.comment(0x93FE, "Save X", align=Align.INLINE)
d.comment(0x93FF, "Capture S into X to address stack from below", align=Align.INLINE)
d.comment(0x9400, "Re-read the original A from stack[X+2] (above PHX/PHA)", align=Align.INLINE)
d.comment(0x9403, "Convert attribute byte to channel-table index", align=Align.INLINE)
d.comment(0x9406, "No matching channel: skip the flag set, just restore", align=Align.INLINE)
d.comment(0x9408, "A=&40: bit 6 = connection-active mask", align=Align.INLINE)
d.comment(0x940A, "OR with current status byte for this channel", align=Align.INLINE)
d.comment(0x940D, "Write back the updated status", align=Align.INLINE)
d.comment(0x9410, "Always taken (A is non-zero after the OR with &40); join shared exit", align=Align.INLINE)
d.label(0x9412, "clear_conn_active")

d.subroutine(
    0x9412,
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


d.comment(0x9412, "Save flags", align=Align.INLINE)
d.comment(0x9413, "Save A", align=Align.INLINE)
d.comment(0x9414, "Save X", align=Align.INLINE)
d.comment(0x9415, "Capture S into X for stack-relative reads", align=Align.INLINE)
d.comment(0x9416, "Re-read the attribute byte from stack[X+2]", align=Align.INLINE)
d.comment(0x9419, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0x941C, "No matching channel: just restore", align=Align.INLINE)
d.comment(0x941E, "A=&BF: bit 6 clear mask", align=Align.INLINE)
d.comment(0x9423, "Write back the updated status", align=Align.INLINE)
d.comment(0x9426, "Restore X (saved at PHX)", align=Align.INLINE)
d.label(0x9426, "clear_channel_flag")

d.comment(0x9427, "Restore A", align=Align.INLINE)
d.comment(0x9428, "Restore flags", align=Align.INLINE)
d.comment(0x9429, "Return; A and X preserved across the call", align=Align.INLINE)
d.entry(0x942A)
d.label(0x942A, "cmd_fs_operation")

d.subroutine(
    0x942A,
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


d.comment(0x942A, "Copy command name 'Access'/'Delete'/'Info'/'Lib' to TX buffer", align=Align.INLINE)
d.comment(0x942E, "Parse quoted filename argument from command line", align=Align.INLINE)
d.comment(0x9431, "Parse the access prefix (e.g. L,W,R) into a bitmask", align=Align.INLINE)
d.comment(0x9435, "Reject '&' character in filename", align=Align.INLINE)
d.comment(0x9438, "End of line?", align=Align.INLINE)
d.comment(0x943A, "No: copy filename chars to buffer", align=Align.INLINE)
d.label(0x943C, "error_bad_filename")

d.subroutine(
    0x943C,
    "error_bad_filename",
    title="Raise 'Bad file name' BRK error",
    description="""Loads error code `&CC` and tail-calls `error_bad_inline` with
the inline string `'file name'` – `error_bad_inline` prepends
`'Bad '` to produce the final `'Bad file name'` message. Used
by [`check_not_ampersand`](label:check_not_ampersand) and other filename
validators. Never returns.""",
)


d.comment(0x943C, "Error number &CC", align=Align.INLINE)
d.comment(0x943E, "Raise 'Bad file name' error", align=Align.INLINE)
d.label(0x944B, "check_not_ampersand")

d.subroutine(
    0x944B,
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


d.comment(0x944B, "Load first parsed character", align=Align.INLINE)
d.comment(0x944E, "Is it '&'?", align=Align.INLINE)
d.comment(0x9450, "Yes: invalid filename", align=Align.INLINE)
d.comment(0x9452, "Return", align=Align.INLINE)
d.label(0x9453, "read_filename_char")

d.subroutine(
    0x9453,
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

Three callers: the loop's own `BRA` at `&945C`, plus `&9435`
([`cmd_rename`](label:cmd_rename)'s first-arg copy) and `&950F`
([`cmd_fs_operation`](label:cmd_fs_operation)'s filename pickup).""",
    on_entry={"a": "current character to copy", "x": "TX-buffer write index"},
    on_exit={"x": "advanced past the CR terminator"},
)


d.comment(0x9453, "Reject '&' in current char", align=Align.INLINE)
d.comment(0x9456, "Store character in TX buffer", align=Align.INLINE)
d.comment(0x9459, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x945A, "End of line?", align=Align.INLINE)
d.comment(0x945C, "Yes: send request to file server", align=Align.INLINE)
d.comment(0x945E, "Strip BASIC token prefix byte", align=Align.INLINE)
d.comment(0x9461, "BRA back to read_filename_char", align=Align.INLINE)
d.label(0x9463, "send_fs_request")

d.subroutine(
    0x9463,
    "send_fs_request",
    title="Send FS command with no extra dispatch offset",
    description="""Loads `Y=0` (so dispatch lookups don't add an offset) and
tail-jumps to [`send_cmd_and_dispatch`](label:send_cmd_and_dispatch). Two
callers: [`read_filename_char`](label:read_filename_char)'s `BEQ` on
`CR` (`&945C`) and the `*RUN` argument-handling tail at
`&953C`.""",
)


d.comment(0x9463, "Y=0: ensure offset starts from beginning of TX command buffer", align=Align.INLINE)
d.comment(0x9465, "Send the FS command and dispatch the reply", align=Align.INLINE)
d.subroutine(
    0x9468,
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


d.comment(0x9468, "Save Y on entry", align=Align.INLINE)
d.label(0x9469, "loop_scan_flag")

d.comment(0x9469, "Scan backwards in command table", align=Align.INLINE)
d.comment(0x946A, "Load table byte", align=Align.INLINE)
d.comment(0x946D, "Bit 7 clear: keep scanning", align=Align.INLINE)
d.comment(0x946F, "Point past flag byte to name start", align=Align.INLINE)
d.comment(0x9470, "Y=0: TX buffer offset", align=Align.INLINE)
d.label(0x9472, "loop_copy_name")

d.comment(0x9472, "Load command name character", align=Align.INLINE)
d.comment(0x9475, "Bit 7 set: end of name", align=Align.INLINE)
d.comment(0x9477, "Store character in TX buffer", align=Align.INLINE)
d.comment(0x947A, "Advance table pointer", align=Align.INLINE)
d.comment(0x947B, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x947C, "Continue copying name", align=Align.INLINE)
d.label(0x947E, "append_space")

d.comment(0x947E, "Space separator", align=Align.INLINE)
d.comment(0x9480, "Append space after command name", align=Align.INLINE)
d.comment(0x9483, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x9484, "Transfer length to A", align=Align.INLINE)
d.comment(0x9485, "And to X (buffer position)", align=Align.INLINE)
d.label(0x9487, "rts_copy_cmd_name")

d.comment(0x9487, "Return", align=Align.INLINE)
d.label(0x9488, "parse_quoted_arg")

d.subroutine(
    0x9488,
    "parse_quoted_arg",
    title="Parse possibly-quoted filename argument",
    description="""Reads from the command line at `(fs_crc_lo),Y` (`&BE`). Handles
double-quote delimiters and stores the result in the parse
buffer at `&0E30`. Raises `'Bad string'` on unbalanced quotes.""",
    on_entry={"y": "current offset within the command line"},
    on_exit={"y": "advanced past the parsed argument", "a": "clobbered (last byte read)"},
)


d.comment(0x9488, "A=0: no quote mode", align=Align.INLINE)
d.comment(0x948B, "Clear quote tracking flag", align=Align.INLINE)
d.label(0x948E, "loop_skip_spaces")

d.comment(0x948E, "Load char from command line", align=Align.INLINE)
d.comment(0x9490, "Space?", align=Align.INLINE)
d.comment(0x9492, "No: check for opening quote", align=Align.INLINE)
d.comment(0x9494, "Skip leading space", align=Align.INLINE)
d.comment(0x9495, "Continue skipping spaces", align=Align.INLINE)
d.label(0x9497, "check_open_quote")

d.comment(0x9497, "Double-quote character?", align=Align.INLINE)
d.comment(0x9499, "No: start reading filename", align=Align.INLINE)
d.comment(0x949B, "Skip opening quote", align=Align.INLINE)
d.comment(0x949C, "Toggle quote mode flag", align=Align.INLINE)
d.comment(0x949F, "Store updated quote mode", align=Align.INLINE)
d.label(0x94A2, "loop_copy_arg_char")

d.comment(0x94A2, "Load char from command line", align=Align.INLINE)
d.comment(0x94A4, "Double-quote?", align=Align.INLINE)
d.comment(0x94A6, "No: store character as-is", align=Align.INLINE)
d.comment(0x94A8, "Toggle quote mode", align=Align.INLINE)
d.comment(0x94AB, "Store updated quote mode", align=Align.INLINE)
d.comment(0x94AE, "Replace closing quote with space", align=Align.INLINE)
d.label(0x94B0, "store_arg_char")

d.comment(0x94B0, "Store character in parse buffer", align=Align.INLINE)
d.comment(0x94B3, "Advance command line pointer", align=Align.INLINE)
d.comment(0x94B4, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x94B5, "End of line?", align=Align.INLINE)
d.comment(0x94B7, "No: continue parsing", align=Align.INLINE)
d.comment(0x94B9, "Check quote balance flag", align=Align.INLINE)
d.comment(0x94BC, "Balanced: return OK", align=Align.INLINE)
d.comment(0x94BE, "Unbalanced: use BRK ptr for error", align=Align.INLINE)
d.comment(0x94C0, "Raise 'Bad string' error", align=Align.INLINE)
d.comment(0x94C3, "Store to TXCB", align=Align.INLINE)
d.entry(0x94CA)
d.label(0x94CA, "cmd_rename")

d.subroutine(
    0x94CA,
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


d.comment(0x94CA, "Copy 'Rename ' to TX buffer", align=Align.INLINE)
d.comment(0x94CE, "Clear owner-only access bits before parsing", align=Align.INLINE)
d.comment(0x94D1, "Parse the quoted source filename", align=Align.INLINE)
d.comment(0x94D4, "Parse access prefix on the source filename", align=Align.INLINE)
d.label(0x94D8, "loop_copy_rename")

d.comment(0x94D8, "Load next parsed character", align=Align.INLINE)
d.comment(0x94DB, "End of line?", align=Align.INLINE)
d.comment(0x94DD, "No: store character", align=Align.INLINE)
d.label(0x94DF, "error_bad_rename")

d.comment(0x94DF, "Error number &B0", align=Align.INLINE)
d.comment(0x94E1, "Raise 'Bad rename' error", align=Align.INLINE)
d.comment(0x94E9, "Add 5 for header size", align=Align.INLINE)
d.label(0x94EB, "store_rename_char")

d.comment(0x94EB, "Store character in TX buffer", align=Align.INLINE)
d.comment(0x94EE, "Advance buffer pointer", align=Align.INLINE)
d.comment(0x94EF, "Space (name separator)?", align=Align.INLINE)
d.comment(0x94F1, "Yes: first name complete", align=Align.INLINE)
d.comment(0x94F3, "Strip BASIC token prefix byte", align=Align.INLINE)
d.comment(0x94F6, "BRA back to loop_copy_rename", align=Align.INLINE)
d.label(0x94F8, "skip_rename_spaces")

d.comment(0x94F8, "Strip token from next char", align=Align.INLINE)
d.comment(0x94FB, "Load next parsed character", align=Align.INLINE)
d.comment(0x94FE, "Still a space?", align=Align.INLINE)
d.comment(0x9500, "Yes: skip multiple spaces", align=Align.INLINE)
d.comment(0x9502, "Save current FS options", align=Align.INLINE)
d.comment(0x9505, "Push them", align=Align.INLINE)
d.comment(0x9506, "Reset access mask for second name", align=Align.INLINE)
d.comment(0x9509, "Save loop index across the access parse", align=Align.INLINE)
d.comment(0x950A, "Parse access prefix on the second filename", align=Align.INLINE)
d.comment(0x950D, "Restore loop index", align=Align.INLINE)
d.comment(0x950E, "Restore original FS options", align=Align.INLINE)
d.comment(0x950F, "Options changed (cross-FS)?", align=Align.INLINE)
d.comment(0x9512, "Yes: error (can't rename across FS)", align=Align.INLINE)
d.comment(0x9514, "Copy second filename and send", align=Align.INLINE)
d.entry(0x9517)
d.label(0x9517, "cmd_dir")

d.subroutine(
    0x9517,
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


d.comment(0x9517, "Get first char of argument", align=Align.INLINE)
d.comment(0x9519, "Is it '&' (FS selector prefix)?", align=Align.INLINE)
d.comment(0x951B, "No: simple dir change", align=Align.INLINE)
d.comment(0x951D, "Skip '&'", align=Align.INLINE)
d.comment(0x951E, "Get char after '&'", align=Align.INLINE)
d.comment(0x9520, "End of line?", align=Align.INLINE)
d.comment(0x9522, "Yes: '&' alone (root directory)", align=Align.INLINE)
d.comment(0x9524, "Space?", align=Align.INLINE)
d.comment(0x9526, "No: check for '.' separator", align=Align.INLINE)
d.label(0x9528, "setup_fs_root")

d.comment(0x9528, "Y=&FF: pre-increment for loop", align=Align.INLINE)
d.label(0x952A, "loop_copy_fs_num")

d.comment(0x952A, "Advance index", align=Align.INLINE)
d.comment(0x952B, "Load char from command line", align=Align.INLINE)
d.comment(0x952D, "Copy to TX buffer", align=Align.INLINE)
d.comment(0x9530, "Is it '&' (end of FS path)?", align=Align.INLINE)
d.comment(0x9532, "No: keep copying", align=Align.INLINE)
d.comment(0x9534, "Replace '&' with CR terminator", align=Align.INLINE)
d.comment(0x9536, "Store CR in buffer", align=Align.INLINE)
d.comment(0x9539, "Point past CR", align=Align.INLINE)
d.comment(0x953A, "Transfer length to A", align=Align.INLINE)
d.comment(0x953B, "And to X (byte count)", align=Align.INLINE)
d.comment(0x953C, "Send directory request to server", align=Align.INLINE)
d.label(0x953F, "check_fs_dot")

d.comment(0x953F, "Is char after '&' a dot?", align=Align.INLINE)
d.comment(0x9541, "Yes: &FS.dir format", align=Align.INLINE)
d.comment(0x9543, "No: invalid syntax", align=Align.INLINE)
d.label(0x9546, "parse_fs_dot_dir")

d.comment(0x9546, "Skip '.'", align=Align.INLINE)
d.comment(0x9547, "Save dir path start position", align=Align.INLINE)
d.comment(0x9549, "FS command 4: examine directory", align=Align.INLINE)
d.comment(0x954B, "Store in TX buffer", align=Align.INLINE)
d.comment(0x954E, "Load FS flags", align=Align.INLINE)
d.comment(0x9551, "Set bit 6 (FS selection active)", align=Align.INLINE)
d.comment(0x9553, "Store updated flags", align=Align.INLINE)
d.comment(0x9556, "X=1: buffer offset", align=Align.INLINE)
d.comment(0x9558, "Copy FS number to buffer", align=Align.INLINE)
d.comment(0x955B, "Y=&12: select FS command code", align=Align.INLINE)
d.comment(0x955D, "Send FS selection command", align=Align.INLINE)
d.comment(0x9560, "Load reply status", align=Align.INLINE)
d.comment(0x9563, "Status 2 (found)?", align=Align.INLINE)
d.comment(0x9565, "Yes: proceed to dir change", align=Align.INLINE)
d.comment(0x9567, "Error number &D6", align=Align.INLINE)
d.comment(0x9569, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0x956C, "Store null terminator (A=0 from EOR)", align=Align.INLINE)
d.comment(0x956F, "Get message length", align=Align.INLINE)
d.comment(0x9572, "Go to error dispatch", align=Align.INLINE)
d.label(0x9576, "dir_found_send")

d.comment(0x9576, "Load current FS station byte", align=Align.INLINE)
d.comment(0x9579, "Store in TX buffer", align=Align.INLINE)
d.comment(0x957C, "X=1: buffer offset", align=Align.INLINE)
d.comment(0x957E, "Y=7: change directory command code", align=Align.INLINE)
d.comment(0x9580, "Send directory change request", align=Align.INLINE)
d.comment(0x9583, "X=1", align=Align.INLINE)
d.comment(0x9585, "Store start marker in buffer", align=Align.INLINE)
d.comment(0x9588, "Store start marker in buffer+1", align=Align.INLINE)
d.comment(0x958B, "Non-zero: commit state and return", align=Align.INLINE)
d.comment(0x958C, "Restore dir path start position", align=Align.INLINE)
d.comment(0x958E, "Copy directory path to buffer", align=Align.INLINE)
d.comment(0x9591, "Y=6: set directory command code", align=Align.INLINE)
d.comment(0x9593, "Send set directory command", align=Align.INLINE)
d.comment(0x9596, "Load reply handle", align=Align.INLINE)
d.comment(0x9599, "Select FS and return", align=Align.INLINE)
d.label(0x959C, "dir_pass_simple")

d.comment(0x959C, "Simple: pass command to FS", align=Align.INLINE)
d.label(0x959F, "print_fs_ps_help")

d.comment(0x959F, "Read first command-line char at (os_text_ptr),Y", align=Align.INLINE)
d.entry(0x959F)
d.comment(0x95A1, "Is it CR (no argument supplied)?", align=Align.INLINE)
d.comment(0x95A3, "Non-CR: argument present -- exit via dispatch_fs_ps_with_arg (X=&A0)", align=Align.INLINE)
d.comment(0x95A5, "CR: print 'FS       ' header", align=Align.INLINE)
d.comment(0x95A8, "Print '[<D>.]<D>\\r'", align=Align.INLINE)
d.comment(0x95AB, "Print 'PS       ' header", align=Align.INLINE)
d.comment(0x95AE, "Print '[<D>.]<D>\\r' again", align=Align.INLINE)
d.comment(0x95B1, "Print final 'Space\\rNoSpace\\r' lines", align=Align.INLINE)
# UNMAPPED: d.comment(0x95BD, "NOP -- bit-7 terminator + resume opcode for the preceding inline string", align=Align.INLINE)
d.label(0x95BD, "bra_target_svc_return")

d.comment(0x95BD, "JMP to svc_return_unclaimed (long-distance via this 3-byte trampoline)", align=Align.INLINE)
d.comment(0x95C0, "Print 'P' prefix", align=Align.INLINE)
d.subroutine(
    0x95C0,
    "print_station_low",
    title="Print 'PS       ' 9-column header",
    description="""Calls [`print_inline`](label:print_inline) with `'P'` then falls
through (via the 1-byte CLV terminator and BVC) into
[`print_field_tail_s`](label:print_field_tail_s), so the combined output is
`'PS       '` -- the 9-column 'PS' field used in the `*FS`/`*PS`
no-arg help and `*STATUS` displays.""",
)


d.comment(
    0x95C4,
    "CLV -- bit-7 terminator + resume (V flag is irrelevant here, used as 1-byte resume opcode)",
    align=Align.INLINE,
)
d.comment(
    0x95C5,
    "BVC: V was just cleared -> always taken; falls into the shared 'S       ' tail at &95CC",
    align=Align.INLINE,
)
d.comment(0x95C7, "Print 'F' prefix", align=Align.INLINE)
d.subroutine(
    0x95C7,
    "print_fs_station",
    title="Print 'FS       ' 9-column header",
    description="""Calls [`print_inline`](label:print_inline) with `'F'` then falls
through (via the 1-byte NOP terminator) into
[`print_field_tail_s`](label:print_field_tail_s), so the combined output is
`'FS       '` -- the 9-column 'FS' field used in the `*FS`/`*PS`
no-arg help and `*STATUS` displays.""",
)


d.comment(0x95CB, "NOP -- bit-7 terminator; falls through into the shared 'S       ' tail at &95CC", align=Align.INLINE)
d.label(0x95CC, "print_field_tail_s")

d.comment(
    0x95CC,
    "Print 'S       ' (S + 7 spaces) -- the shared 8-char field used by both 'FS' and 'PS' callers",
    align=Align.INLINE,
)
d.comment(0x95D7, "Bit-7 terminator", align=Align.INLINE)
d.comment(0x95D8, "Return", align=Align.INLINE)
d.comment(
    0x95D9,
    "Print '[<D>.]<D>\\r' (file-name syntax fragment, shared between *FS/*PS no-arg help and *Dir)",
    align=Align.INLINE,
)
d.subroutine(
    0x95D9,
    "print_dir_syntax",
    title="Print '[<D>.]<D>\\\\r' directory-name syntax fragment",
    description="""3-byte JSR + inline `'[<D>.]<D>'` + CR + NOP terminator. Used as
a shared fragment by both `*Dir`'s syntax help and the `*FS`/`*PS`
no-argument help via [`print_fs_ps_help`](label:print_fs_ps_help).""",
)


d.comment(0x95E6, "Bit-7 terminator", align=Align.INLINE)
d.comment(0x95E7, "Return", align=Align.INLINE)
d.label(0x95E8, "dispatch_fs_ps_with_arg")

d.comment(0x95E8, "X=&A5: index into svc4 dispatch table (no-arg path)", align=Align.INLINE)
d.comment(0x95EA, "Tail-jump to svc4_dispatch_lookup with X=&A0", align=Align.INLINE)
d.subroutine(
    0x95ED,
    "set_fs_or_ps_cmos_station",
    title="Write FS/PS station+network to CMOS RAM",
    description="""Reached via PHA/PHA/RTS dispatch from cmd_table_fs sub-table 4
(`*FS` at [`&A828`](address:A828), `*PS` at
[`&A82D`](address:A82D)) when the caller supplies a `<net>.<stn>`
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


d.entry(0x95ED)
d.comment(0x95ED, "Read flag byte for matched cmd entry (syntax idx in bits 0..4)", align=Align.INLINE)
d.comment(0x95F0, "Mask off end-marker (bit 7) and V-if-no-arg flag (bit 6)", align=Align.INLINE)
d.comment(0x95F2, "X = CMOS byte index (1=FS stn, 3=PS stn)", align=Align.INLINE)
d.comment(0x95F3, "Save CMOS index", align=Align.INLINE)
d.comment(0x95F4, "Save caller's command-line cursor", align=Align.INLINE)
d.comment(0x95F5, "Save CMOS index again (consumed by first PLX below)", align=Align.INLINE)
d.comment(0x95F6, "Read existing CMOS[idx] (current station)", align=Align.INLINE)
d.comment(0x95F9, "Default station if user gives no args", align=Align.INLINE)
d.comment(0x95FB, "Recover CMOS index from stack", align=Align.INLINE)
d.comment(0x95FC, "X+=1: advance to network byte", align=Align.INLINE)
d.comment(0x95FD, "Read existing CMOS[idx+1] (current network)", align=Align.INLINE)
d.comment(0x9600, "Default network if user gives no args", align=Align.INLINE)
d.comment(0x9602, "Restore command-line cursor", align=Align.INLINE)
d.comment(0x9603, "Parse '<net>.<stn>'; updates fs_work_5/6/7 if args present", align=Align.INLINE)
d.comment(0x9606, "Recover CMOS index from stack", align=Align.INLINE)
d.comment(0x9607, "Re-save CMOS index for second write", align=Align.INLINE)
d.comment(0x9608, "Y = station (parsed or pre-read default)", align=Align.INLINE)
d.comment(0x960A, "Write CMOS[idx] = station", align=Align.INLINE)
d.comment(0x960D, "Recover CMOS index from stack", align=Align.INLINE)
d.comment(0x960E, "X+=1: advance to network byte", align=Align.INLINE)
d.comment(
    0x960F,
    "Y = raw parsed network (NOT canonical fs_work_6); fall through into osbyte_a2 to write CMOS[idx+1]",
    align=Align.INLINE,
)
d.comment(0x9611, "A=&A2: write CMOS RAM byte via OSBYTE", align=Align.INLINE)
d.subroutine(
    0x9611,
    "osbyte_a2",
    title="OSBYTE &A2 (write Master CMOS RAM byte)",
    description="""Three instructions: `LDA #&A2 / JSR OSBYTE / BRA &95BD`. Writes
the Master 128 CMOS RAM byte indexed by `X` with the value in `Y`.
The trailing `BRA` lands on
[`bra_target_svc_return`](label:bra_target_svc_return) (a 3-byte `JMP` trampoline
to [`svc_return_unclaimed`](label:svc_return_unclaimed), reached this way
because `BRA`'s 8-bit displacement can't span &9616 → &8C89).

`osbyte_a2` ends at [`&9618`](address:9618) (3 instructions, 7 bytes);
the next labelled routine is [`cmd_space`](label:cmd_space). Counterpart of
[`osbyte_a1`](label:osbyte_a1) (read).

Callers: [`set_fs_or_ps_cmos_station`](label:set_fs_or_ps_cmos_station) (once via
`JSR`, once via fall-through), the `BRA` shortcut at
`&962D` inside [`cmd_nospace`](label:cmd_nospace), and
an `OSARGS`-related read-modify-write of CMOS byte &11 ending at
[`osopt_cmos_writeback_jsr`](label:osopt_cmos_writeback_jsr).""",
    on_entry={"x": "CMOS RAM byte index", "y": "value to write"},
)


d.comment(0x9616, "BRA -91 -> bra_target_svc_return", align=Align.INLINE)
d.comment(0x9618, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.subroutine(
    0x9618,
    "cmd_space",
    title="*Space command: enable space-remaining display",
    description="""Reached via the [`cmd_table_fs`](label:cmd_table_fs) dispatch entry for
`*Space`. Reads CMOS byte &11 with [`osbyte_a1`](label:osbyte_a1),
sets bit 0 of the value, then `BRA`s to the shared write-back tail
at [`osbyte_a2_value_tya`](label:osbyte_a2_value_tya).""",
)


d.entry(0x9618)
d.comment(0x961A, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0x961D, "A = current CMOS &11 value", align=Align.INLINE)
d.comment(0x961E, "Set bit 0 in A", align=Align.INLINE)
d.comment(0x9620, "BRA osbyte_a2_value_tya: shared write-back tail", align=Align.INLINE)
d.comment(0x9622, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.subroutine(
    0x9622,
    "cmd_nospace",
    title="*NoSpace command: disable space-remaining display",
    description="""Reached via the [`cmd_table_fs`](label:cmd_table_fs) dispatch entry for
`*NoSpace`. Reads CMOS byte &11 with [`osbyte_a1`](label:osbyte_a1),
clears bit 0 of the value, falls through to
[`osbyte_a2_value_tya`](label:osbyte_a2_value_tya), and `BRA`s back into
[`osbyte_a2`](label:osbyte_a2) to write CMOS &11 = `Y`.""",
)


d.entry(0x9622)
d.comment(0x9624, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0x9627, "A = current CMOS &11 value", align=Align.INLINE)
d.comment(0x9628, "Clear bit 0 in A", align=Align.INLINE)
d.comment(0x962A, "New CMOS value to Y", align=Align.INLINE)
d.subroutine(
    0x962A,
    "osbyte_a2_value_tya",
    title="Shared CMOS write-back tail",
    description="""Common tail used by [`cmd_space`](label:cmd_space) (via `BRA` from
&9620 with the new value already in `A`) and
[`cmd_nospace`](label:cmd_nospace) (fall-through with the new value in
`A`). `TAY` moves the byte to `Y`, then `LDX #&11` reloads the
CMOS index and `BRA osbyte_a2` performs the write.""",
)


d.comment(0x962B, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0x962D, "BRA osbyte_a2: write CMOS &11 = Y", align=Align.INLINE)
d.comment(0x962F, "Read first command-line char", align=Align.INLINE)
d.subroutine(
    0x962F,
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


d.entry(0x962F)
d.comment(0x9631, "Is it CR (no argument)?", align=Align.INLINE)
d.comment(0x9633, "Non-CR: parse the argument at help_dispatch_setup", align=Align.INLINE)
d.comment(0x9635, "Print 'FS       ' header", align=Align.INLINE)
d.comment(0x9638, "Print FS network.station from CMOS &02/&01", align=Align.INLINE)
d.comment(0x963B, "Print 'PS       ' header", align=Align.INLINE)
d.comment(0x963E, "Print PS network.station from CMOS &04/&03", align=Align.INLINE)
d.comment(0x9641, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0x9643, "Read CMOS &11 (FS state)", align=Align.INLINE)
d.comment(0x9646, "A = CMOS &11", align=Align.INLINE)
d.comment(0x9647, "Mask bit 0 (FS-active flag)", align=Align.INLINE)
d.comment(0x9649, "Bit set: skip 'No ' prefix", align=Align.INLINE)
d.comment(0x964B, "Print 'No ' prefix via inline", align=Align.INLINE)
d.comment(0x9651, "Bit-7 terminator + resume", align=Align.INLINE)
d.comment(0x9652, "Print 'Space        ' or similar via inline", align=Align.INLINE)
d.label(0x9652, "parse_object_space_print")

d.comment(0x965C, "Bit-7 terminator + resume opcode", align=Align.INLINE)
d.subroutine(
    0x9662,
    "print_ps_address",
    title="Print printer-server address from CMOS",
    description="""Prints the printer server's saved `network.station` from
CMOS RAM. Sets `X=4` (the PS network byte) and branches into the shared
tail at [`print_cmos_pair`](label:print_cmos_pair), which prints CMOS[X] then
CMOS[X-1] separated by a `.`.

In 4.24 the two entry points share one body: `print_fs_address` (`X=2`)
falls straight in, while `print_ps_address` (`X=4`) reaches it by `BRA`,
skipping the `LDX #2`.""",
)

d.comment(0x9662, "X=4: CMOS RAM byte 4 (PS network number)", align=Align.INLINE)
d.comment(0x9664, "Branch into shared tail (X already set)", align=Align.INLINE)
d.subroutine(
    0x9666,
    "print_fs_address",
    title="Print file-server address from CMOS",
    description="""Prints the file server's saved `network.station` from
CMOS RAM. Sets `X=2` (the FS network byte) and falls into the shared tail
[`print_cmos_pair`](label:print_cmos_pair). See [`print_ps_address`](label:print_ps_address)
for the shared-body structure.""",
)

d.comment(0x9666, "X=2: CMOS RAM byte 2 (FS network number)", align=Align.INLINE)
d.label(0x9668, "print_cmos_pair")
d.comment(0x9668, "Save network-byte index across the first print", align=Align.INLINE)
d.comment(0x9669, "Read CMOS[X] (network number) via osbyte_a1", align=Align.INLINE)
d.comment(0x966C, "A = CMOS network byte", align=Align.INLINE)
d.comment(0x966D, "Print as decimal (no leading zeros)", align=Align.INLINE)
d.comment(0x9670, "Print '.' separator via inline", align=Align.INLINE)
d.comment(0x9674, "PLX terminator: restore X (network index)", align=Align.INLINE)
d.comment(0x9675, "X-1: the station byte sits just below the network byte", align=Align.INLINE)
d.label(0x9676, "print_cmos_decimal_nl")

d.comment(0x9676, "Read CMOS X via osbyte_a1", align=Align.INLINE)
d.comment(0x9679, "A = CMOS value", align=Align.INLINE)
d.comment(0x967A, "Print as decimal", align=Align.INLINE)
d.label(0x9680, "print_cmos_done")

d.comment(0x9680, "JMP svc_return_unclaimed (release service call)", align=Align.INLINE)
d.comment(0x9683, "X=&C2: setup index for the dispatch chain", align=Align.INLINE)
d.label(0x9683, "help_dispatch_setup")

d.comment(0x9685, "JMP svc4_dispatch_lookup -- shared parser dispatch", align=Align.INLINE)
d.subroutine(
    0x9685,
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

d.label(0x9686, "help_topic_template")

d.comment(
    0x9688,
    "'!Help.' filename template copied into the TXCB command buffer to open the help file",
    align=Align.INLINE,
)

d.subroutine(
    0x9690,
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

d.label(0x96AF, "help_return")
d.label(0x96B1, "help_on_matched")
d.label(0x96B6, "loop_skip_help_spaces")
d.label(0x96C2, "help_have_topic_char")
d.label(0x96C3, "help_build_cmd")
d.label(0x96CB, "loop_copy_command_suffix")
d.label(0x96DB, "check_template_dot")
d.label(0x96DF, "loop_copy_topic_name")
d.label(0x96E3, "store_topic_char")
d.label(0x96F2, "start_help_file_load")
d.label(0x9708, "loop_print_help_byte")
d.label(0x9715, "help_next_topic")
d.label(0x9718, "loop_help_next_topic")
d.label(0x9723, "help_print_start")
d.label(0x972A, "help_emit_char")

d.comment(0x9690, "Save caller's command-line index Y", align=Align.INLINE)
d.comment(0x9691, "Test fs_flags: bit 6 = interactive HELP armed", align=Align.INLINE)
d.comment(0x9694, "Bit 6 clear: not our HELP call -> return", align=Align.INLINE)
d.comment(0x9696, "Point work_ae at the command line (lo)", align=Align.INLINE)
d.comment(0x9698, "Store command-line pointer lo", align=Align.INLINE)
d.comment(0x969A, "Command-line pointer hi", align=Align.INLINE)
d.comment(0x969C, "Store pointer hi (addr_work)", align=Align.INLINE)
d.comment(0x969E, "Read first keyword character", align=Align.INLINE)
d.comment(0x96A0, "Compare with 'O' ...", align=Align.INLINE)
d.comment(0x96A2, "... case-insensitively (mask bit 5)", align=Align.INLINE)
d.comment(0x96A4, "Not 'O': return (line is not '...ON ')", align=Align.INLINE)
d.comment(0x96A6, "Advance to second character", align=Align.INLINE)
d.comment(0x96A7, "Read second keyword character", align=Align.INLINE)
d.comment(0x96A9, "Compare with 'N' ...", align=Align.INLINE)
d.comment(0x96AB, "... case-insensitively", align=Align.INLINE)
d.comment(0x96AD, "'ON' matched: handle the topic", align=Align.INLINE)
d.comment(0x96AF, "Restore caller's Y", align=Align.INLINE)
d.comment(0x96B0, "Return to service dispatcher", align=Align.INLINE)
d.comment(0x96B1, "Save Y across FS-select", align=Align.INLINE)
d.comment(0x96B2, "Ensure NFS is the current filing system", align=Align.INLINE)
d.comment(0x96B5, "Restore Y", align=Align.INLINE)
d.comment(0x96B6, "Advance to next command-line character", align=Align.INLINE)
d.comment(0x96B7, "Read it", align=Align.INLINE)
d.comment(0x96B9, "Set V (topic-char marker) from &9767 bit 6", align=Align.INLINE)
d.comment(0x96BC, "Space?", align=Align.INLINE)
d.comment(0x96BE, "Control char (<space): stop scanning", align=Align.INLINE)
d.comment(0x96C0, "Space: keep skipping leading spaces", align=Align.INLINE)
d.comment(0x96C2, "Real char: clear V (topic present)", align=Align.INLINE)
d.comment(0x96C3, "Save command-buffer index", align=Align.INLINE)
d.comment(0x96C6, "Save it as the command flag too", align=Align.INLINE)
d.comment(0x96C9, "X=1: template-walk index", align=Align.INLINE)
d.comment(0x96CB, "Advance template index", align=Align.INLINE)
d.comment(0x96CC, "Read '!Help.' template byte", align=Align.INLINE)
d.comment(0x96CF, "Store into the command buffer", align=Align.INLINE)
d.comment(0x96D2, "V clear (real topic char): check '.' terminator", align=Align.INLINE)
d.comment(0x96D4, "V set (line ended): CR?", align=Align.INLINE)
d.comment(0x96D6, "Not CR: keep copying template", align=Align.INLINE)
d.comment(0x96D8, "Skip the CR", align=Align.INLINE)
d.comment(0x96D9, "Open the help file", align=Align.INLINE)
d.comment(0x96DB, "Template terminator '.'?", align=Align.INLINE)
d.comment(0x96DD, "No: keep copying template", align=Align.INLINE)
d.comment(0x96DF, "Advance destination index", align=Align.INLINE)
d.comment(0x96E0, "Read topic-name character", align=Align.INLINE)
d.comment(0x96E2, "Advance source index", align=Align.INLINE)
d.comment(0x96E3, "Store topic character", align=Align.INLINE)
d.comment(0x96E6, "CR (end of name)?", align=Align.INLINE)
d.comment(0x96E8, "Yes: open the help file", align=Align.INLINE)
d.comment(0x96EA, "Space (terminator)?", align=Align.INLINE)
d.comment(0x96EC, "No: keep copying the name", align=Align.INLINE)
d.comment(0x96EE, "Replace trailing space with CR", align=Align.INLINE)
d.comment(0x96F0, "Store the CR terminator", align=Align.INLINE)
d.comment(0x96F2, "Save command-buffer index", align=Align.INLINE)
d.comment(0x96F3, "Account for the last character", align=Align.INLINE)
d.comment(0x96F4, "Read fs_lib_flags", align=Align.INLINE)
d.comment(0x96F7, "Clear the top two bits", align=Align.INLINE)
d.comment(0x96F9, "Set bit 7 (load pending)", align=Align.INLINE)
d.comment(0x96FB, "Store fs_lib_flags back", align=Align.INLINE)
d.comment(0x96FE, "A=&40: load-mode flag", align=Align.INLINE)
d.comment(0x9700, "Set last-byte flag", align=Align.INLINE)
d.comment(0x9702, "Open the help-topic file", align=Align.INLINE)
d.comment(0x9705, "File handle -> Y (0 = open failed)", align=Align.INLINE)
d.comment(0x9706, "Open failed: skip to next topic", align=Align.INLINE)
d.comment(0x9708, "Read next byte from the help file", align=Align.INLINE)
d.comment(0x970B, "C clear: byte read OK -> print it", align=Align.INLINE)
d.comment(0x970D, "A=0: OSFIND close mode", align=Align.INLINE)
d.comment(0x9712, "Print a newline after the file", align=Align.INLINE)
d.comment(0x9715, "Restore command-line index", align=Align.INLINE)
d.comment(0x9716, "Back up over the first consumed char", align=Align.INLINE)
d.comment(0x9717, "Back up over the second consumed char", align=Align.INLINE)
d.comment(0x9718, "Advance to next character", align=Align.INLINE)
d.comment(0x9719, "Read it", align=Align.INLINE)
d.comment(0x971B, "Space?", align=Align.INLINE)
d.comment(0x971D, "Control char: no more topics -> return", align=Align.INLINE)
d.comment(0x971F, "Space: keep scanning", align=Align.INLINE)
d.comment(0x9721, "Real char: process the next topic", align=Align.INLINE)
d.comment(0x9723, "Check the Escape flag", align=Align.INLINE)
d.comment(0x9725, "Bit 7 clear: not escaping -> print", align=Align.INLINE)
d.comment(0x9727, "Escape pressed: abort with error", align=Align.INLINE)
d.comment(0x972A, "Print the byte", align=Align.INLINE)
d.comment(0x972D, "Was it a CR?", align=Align.INLINE)
d.comment(0x972F, "No: read the next byte", align=Align.INLINE)
d.comment(0x9731, "CR: read paged-mode line count", align=Align.INLINE)
d.comment(0x9734, "Non-zero: no pause, continue", align=Align.INLINE)
d.comment(0x9736, "Emit newline", align=Align.INLINE)
d.comment(0x9739, "Loop for the next byte", align=Align.INLINE)


# svc &18 help handler: genuine ASCII-character operands
d.char_literal(0x96A1)
d.char_literal(0x96AA)
d.char_literal(0x96BD)
d.char_literal(0x96DC)
d.char_literal(0x96EB)
d.char_literal(0x971C)

d.label(0x973B, "init_txcb_bye")

d.subroutine(
    0x973B,
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


d.comment(0x973B, "A=&90: bye command port", align=Align.INLINE)
d.label(0x973D, "init_txcb_port")

d.subroutine(
    0x973D,
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


d.comment(0x973D, "Initialise TXCB from template", align=Align.INLINE)
d.comment(0x9740, "Set transmit port", align=Align.INLINE)
d.comment(0x9742, "A=3: data start offset", align=Align.INLINE)
d.comment(0x9744, "Set TXCB start offset", align=Align.INLINE)
d.comment(0x9746, "Open receive: &80->&7F (bit 7 clear = awaiting reply)", align=Align.INLINE)
d.comment(0x9748, "Return", align=Align.INLINE)
d.label(0x9749, "init_txcb")

d.subroutine(
    0x9749,
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


d.comment(0x9749, "Save A", align=Align.INLINE)
d.comment(0x974A, "Y=&0B: template size - 1", align=Align.INLINE)
d.label(0x974C, "loop_init_txcb")

d.comment(0x974C, "Load byte from TXCB template", align=Align.INLINE)
d.comment(0x974F, "Store to TXCB workspace", align=Align.INLINE)
d.comment(0x9752, "Index >= 2?", align=Align.INLINE)
d.comment(0x9754, "Yes: skip dest station copy", align=Align.INLINE)
d.comment(0x9756, "Load dest station byte", align=Align.INLINE)
d.comment(0x9759, "Store to TXCB destination", align=Align.INLINE)
d.label(0x975C, "skip_txcb_dest")

d.comment(0x975C, "Decrement index", align=Align.INLINE)
d.comment(0x975D, "More bytes: continue", align=Align.INLINE)
d.comment(0x975F, "Restore A", align=Align.INLINE)
d.comment(0x9760, "Return", align=Align.INLINE)
d.index_base(0x9761, "txcb_init_template")
d.banner(
    0x9761,
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
    d.byte(0x9761 + i)

d.comment(0x9761, "Offset 0: txcb_ctrl = &80 (TX command)", align=Align.INLINE)
d.comment(0x9762, "Offset 1: txcb_port = &99 (FS command port)", align=Align.INLINE)
d.comment(0x9763, "Offset 2: txcb_dest lo placeholder (overwritten with hazel_fs_station[0])", align=Align.INLINE)
d.comment(0x9764, "Offset 3: txcb_dest hi placeholder (overwritten with hazel_fs_station[1])", align=Align.INLINE)
d.comment(0x9765, "Offset 4: txcb_start lo = 0", align=Align.INLINE)
d.comment(0x9766, "Offset 5: txcb_start hi = &C1 (data buffer starts at &C100 in HAZEL)", align=Align.INLINE)
d.label(0x9767, "always_set_v_byte")

d.comment(0x9767, "Offset 6: padding &FF; doubles as the always_set_v_byte BIT $abs target", align=Align.INLINE)
d.label(0x9768, "bit_test_ff")

d.comment(0x9768, "Offset 7: txcb_pos = &FF (also labelled bit_test_ff)", align=Align.INLINE)
d.comment(0x9769, "Offset 8: txcb_end lo = &FF", align=Align.INLINE)
d.comment(0x976A, "Offset 9: txcb_end hi = &C1 (buffer end &C1FF)", align=Align.INLINE)
d.comment(0x976B, "Offset 10: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x976C, "Offset 11: extended-addr fill (&FF)", align=Align.INLINE)
d.label(0x976D, "send_request_nowrite")

d.subroutine(
    0x976D,
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


d.comment(0x976D, "Save A", align=Align.INLINE)
d.comment(0x976E, "Set carry (read-only mode)", align=Align.INLINE)
d.label(0x9771, "send_request_write")

d.subroutine(
    0x9771,
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


d.comment(0x9771, "Clear V", align=Align.INLINE)
d.comment(0x9774, "Y=0: process_all_fcbs filter (0 = all FCBs)", align=Align.INLINE)
d.entry(0x9774)
d.label(0x9774, "cmd_bye")

d.subroutine(
    0x9774,
    "cmd_bye",
    title="*Bye command handler",
    description="""Closes all open file control blocks via
process_all_fcbs, shuts down any *SPOOL/*EXEC files
with OSBYTE &77, and closes all network channels.
Falls through to save_net_tx_cb with function code
&17 to send the bye request to the file server.""",
)
d.comment(0x9776, "Walk all 16 FCB slots, calling start_wipe_pass on each", align=Align.INLINE)
d.comment(0x9779, "OSBYTE &77 = close *SPOOL and *EXEC files", align=Align.INLINE)
d.comment(0x977B, "Close any open *SPOOL/*EXEC handles", align=Align.INLINE)
d.comment(0x977E, "A=&40: bit 6 of fs_flags = 'FS in active session'", align=Align.INLINE)
d.comment(0x9780, "Clear bit 6: mark FS session inactive", align=Align.INLINE)
d.comment(0x9783, "Close every Econet client channel", align=Align.INLINE)
d.comment(0x9786, "Y=&17: FS function code 'Bye' (logoff request)", align=Align.INLINE)
d.label(0x9788, "save_net_tx_cb")

d.subroutine(
    0x9788,
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
    0x9788,
    "Clear V: standard send mode (callers set V via save_net_tx_cb_vset for the lib-flag variant)",
    align=Align.INLINE,
)
d.label(0x9789, "save_net_tx_cb_vset")

d.subroutine(
    0x9789,
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


d.comment(0x9789, "Read FS station from &C002 (saved from selection time)", align=Align.INLINE)
d.comment(0x978C, "Copy into TX buffer at &C102 (dest station for header)", align=Align.INLINE)
d.label(0x978F, "txcb_copy_carry_clr")

d.comment(0x978F, "Clear C: caller wants four-way handshake (not disconnect)", align=Align.INLINE)
d.label(0x9790, "txcb_copy_carry_set")

d.comment(0x9790, "Save flags so we can keep V across the loop", align=Align.INLINE)
d.comment(0x9791, "Save Y -- the entry function code -- into TX[1]", align=Align.INLINE)
d.comment(0x9794, "Y=1: copy 2 bytes (network/control) starting at index 1", align=Align.INLINE)
d.label(0x9796, "loop_copy_vset_stn")

d.comment(0x9796, "Read source byte at &C003+Y", align=Align.INLINE)
d.comment(0x9799, "Write to TX buffer at &C103+Y", align=Align.INLINE)
d.comment(0x979C, "Step backwards", align=Align.INLINE)
d.comment(0x979D, "Loop while Y >= 0 (covers indices 1, 0)", align=Align.INLINE)
d.comment(0x979F, "Test fs_lib_flags: bit 6 = use library, bit 7 = *-prefix-stripped", align=Align.INLINE)
d.comment(0x97A2, "V (bit 6) set: use the library station instead", align=Align.INLINE)
d.comment(0x97A4, "Neither bit set: leave the FS station copy intact", align=Align.INLINE)
d.comment(0x97A6, "Bit 7 (FS-prefix) set: substitute the saved-prefix station from &C004", align=Align.INLINE)
d.comment(0x97A9, "Override TX[3]'s station byte", align=Align.INLINE)
d.comment(0x97AC, "Always taken: V was clear when we entered (BVS at &97A4 didn't fire)", align=Align.INLINE)
d.label(0x97AE, "use_lib_station")

d.comment(
    0x97AE,
    "use_lib_station: substitute the library station from &C002 (the original FS station, but bit 6 of fs_lib_flags redirects via lib path)",
    align=Align.INLINE,
)
d.comment(0x97B1, "Override TX[3] with the library station byte", align=Align.INLINE)
d.label(0x97B4, "done_vset_station")

d.comment(0x97B4, "Restore the saved flags (V/C control downstream init_txcb behaviour)", align=Align.INLINE)
d.label(0x97B5, "prep_send_tx_cb")

d.subroutine(
    0x97B5,
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


d.comment(0x97B5, "Save flags so C survives the init_txcb call", align=Align.INLINE)
d.comment(0x97B6, "Reply port = &90 (FS reply port)", align=Align.INLINE)
d.comment(0x97B8, "Stash port in TXCB[0]", align=Align.INLINE)
d.comment(0x97BB, "Build the rest of the TXCB (control, dest stn/net, etc.)", align=Align.INLINE)
d.comment(0x97BE, "Move TX-buffer end pointer (returned in X) into A", align=Align.INLINE)
d.comment(0x97BF, "Add 5 bytes of slack for trailing reply data", align=Align.INLINE)
d.comment(0x97C1, "Stash the resulting end-of-buffer offset", align=Align.INLINE)
d.comment(0x97C3, "Restore the original C flag from caller", align=Align.INLINE)
d.comment(0x97C4, "C set: this is a disconnect; jump to handle_disconnect", align=Align.INLINE)
d.comment(0x97C6, "Save flags again across the actual TX (TX clobbers them)", align=Align.INLINE)
d.comment(0x97C7, "Send the four-way-handshake-initiated command packet", align=Align.INLINE)
d.comment(0x97CA, "Restore caller's flags before falling into recv_and_process_reply", align=Align.INLINE)
d.label(0x97CB, "recv_and_process_reply")

d.subroutine(
    0x97CB,
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


d.comment(0x97CB, "Save flags so caller's V/C survive the receive", align=Align.INLINE)
d.comment(0x97CC, "Set up open RX on port &90 for the FS reply (TXCB[0] = &90, ctrl = &7F)", align=Align.INLINE)
d.comment(0x97CF, "Wait for the reply via the 3-level stack timer", align=Align.INLINE)
d.comment(0x97D2, "Restore caller's flags", align=Align.INLINE)
d.label(0x97D3, "loop_next_reply")

d.comment(0x97D3, "Step Y to next reply byte", align=Align.INLINE)
d.comment(0x97D4, "Read reply byte at txcb_start+Y", align=Align.INLINE)
d.comment(0x97D6, "Stash for the dispatch tests below", align=Align.INLINE)
d.comment(0x97D7, "Zero terminates: return", align=Align.INLINE)
d.comment(0x97D9, "V clear (caller's V): use code as-is", align=Align.INLINE)
d.comment(0x97DB, "V set: shift the code by +&2A (extended-error mapping)", align=Align.INLINE)
d.label(0x97DD, "process_reply_code")

d.comment(0x97DD, "Non-zero: dispatch as an error", align=Align.INLINE)
d.label(0x97DF, "rts_recv_reply")

d.comment(0x97DF, "Return", align=Align.INLINE)
d.label(0x97E0, "handle_disconnect")

d.comment(0x97E0, "Pull caller's pushed return state", align=Align.INLINE)
d.comment(0x97E1, "X=&C0: 'remote disconnect' status", align=Align.INLINE)
d.comment(0x97E3, "Step Y past the disconnect byte", align=Align.INLINE)
d.comment(0x97E4, "Send disconnect notification to remote", align=Align.INLINE)
d.comment(0x97E7, "C clear (success): continue scanning replies", align=Align.INLINE)
d.label(0x97E9, "store_reply_status")

d.comment(0x97E9, "Save the error code into &C009", align=Align.INLINE)
d.comment(0x97EC, "Read FS state byte at &C007", align=Align.INLINE)
d.comment(0x97EF, "Save flags so we can branch later", align=Align.INLINE)
d.comment(0x97F0, "FS state non-zero: data-loss check needed", align=Align.INLINE)
d.comment(0x97F2, "Reply was &BF (special: not a real error)?", align=Align.INLINE)
d.comment(0x97F4, "No: build error block", align=Align.INLINE)
d.label(0x97F6, "check_data_loss")

d.comment(0x97F6, "A=&40: 'channel-active' bitmask", align=Align.INLINE)
d.comment(0x97F8, "Push it onto the OR-accumulator", align=Align.INLINE)
d.comment(0x97F9, "Clear the FS-active bit (we're losing the connection)", align=Align.INLINE)
d.comment(0x97FC, "X=&F0: scan from channel offset &F0 upwards", align=Align.INLINE)
d.label(0x97FE, "loop_scan_channels")

d.comment(0x97FE, "Pull current OR accumulator", align=Align.INLINE)
d.comment(0x97FF, "OR with channel status byte at &C1C8+X", align=Align.INLINE)
d.comment(0x9802, "Push back updated accumulator", align=Align.INLINE)
d.comment(0x9803, "Reload channel byte", align=Align.INLINE)
d.comment(0x9806, "Mask to top 2 bits (preserve TX/RX state)", align=Align.INLINE)
d.comment(0x9808, "Write back trimmed status", align=Align.INLINE)
d.comment(0x980B, "Step channel index", align=Align.INLINE)
d.comment(0x980C, "Loop while X bit 7 set (covers &F0..&FF)", align=Align.INLINE)
d.comment(0x980E, "Clear the FS state byte (no longer active)", align=Align.INLINE)
d.comment(0x9811, "Force-close all client channels", align=Align.INLINE)
d.comment(0x9814, "Pull final OR accumulator", align=Align.INLINE)
d.comment(0x9815, "Bit 0 (was bit 6 of any &40 byte) -> C", align=Align.INLINE)
d.comment(0x9816, "Any channel was active: skip the warning", align=Align.INLINE)
d.comment(0x9818, "No active channels were lost: print 'Data Lost' warning via inline string", align=Align.INLINE)
d.label(0x9825, "scan_channel_store_reply")

d.comment(0x9825, "Reload error code from &C009", align=Align.INLINE)
d.comment(0x9828, "Restore saved flags (was bit 7 of fs_flags)", align=Align.INLINE)
d.comment(0x9829, "Z set (no error): build the error block anyway", align=Align.INLINE)
d.comment(0x982B, "Pull caller's saved return state (3 bytes from PHP earlier)", align=Align.INLINE)
d.comment(0x982E, "Return -- caller dispatched on a non-error reply", align=Align.INLINE)
d.label(0x982F, "build_error_block")

d.comment(0x982F, "Y=1: skip past the leading TXCB control byte", align=Align.INLINE)
d.comment(0x9831, "Error code below &A8 (extended)?", align=Align.INLINE)
d.comment(0x9833, "No (>= &A8): proceed to copy", align=Align.INLINE)
d.comment(0x9835, "Yes: clamp to &A8 (truncate range)", align=Align.INLINE)
d.comment(0x9837, "Write clamped code back into TXCB", align=Align.INLINE)
d.label(0x9839, "setup_error_copy")

d.comment(0x9839, "Y=&FF: INY in loop bumps to 0", align=Align.INLINE)
d.label(0x983B, "loop_copy_error")

d.comment(0x983B, "Step Y", align=Align.INLINE)
d.comment(0x983C, "Read TXCB byte (error block content)", align=Align.INLINE)
d.comment(0x983E, "Copy to BRK error block at &0100+Y", align=Align.INLINE)
d.comment(0x9841, "EOR with CR; Z set when we just copied the terminator", align=Align.INLINE)
d.comment(0x9843, "Not yet at CR: continue copying", align=Align.INLINE)
d.comment(0x9845, "Write the CR terminator (Z still set so A=0; ensures cleanly terminated)", align=Align.INLINE)
d.comment(0x9848, "Step Y back so it points at the CR position", align=Align.INLINE)
d.comment(0x9849, "Move Y into A for the BRK", align=Align.INLINE)
d.comment(0x984A, "Move Y into X (caller convention)", align=Align.INLINE)
d.comment(0x984B, "Tail-jump into the BRK-dispatch error path", align=Align.INLINE)
d.label(0x984E, "lang_1_remote_boot")

d.subroutine(
    0x984E,
    "lang_1_remote_boot",
    title="Language reply 1: remote-boot init / continue",
    description="""Reads the reply byte at `(net_rx_ptr),0`. If zero, branches to
[`init_remote_session`](label:init_remote_session) to (re)initialise the
remote session. Otherwise falls through to `done_commit_state`
which finalises the boot state byte for the active session.""",
)


d.comment(0x984E, "Y=0: status byte offset", align=Align.INLINE)
d.entry(0x984E)
d.comment(0x9850, "Read RX status byte", align=Align.INLINE)
d.comment(0x9852, "Zero: re-init the session", align=Align.INLINE)
d.label(0x9854, "done_commit_state")

d.comment(0x9854, "Non-zero: commit state and continue", align=Align.INLINE)
d.label(0x9857, "init_remote_session")

d.comment(0x9857, "Mark session as 'remote boot'", align=Align.INLINE)
d.comment(0x9859, "Store updated status byte back to RX[0]", align=Align.INLINE)
d.comment(0x985B, "X=&80: caller machine-id byte offset", align=Align.INLINE)
d.comment(0x985D, "Y=&80: same offset", align=Align.INLINE)
d.comment(0x985F, "Read remote machine ID", align=Align.INLINE)
d.comment(0x9861, "Push -- save across the workspace store", align=Align.INLINE)
d.comment(0x9863, "Re-read for the second store target", align=Align.INLINE)
d.comment(0x9865, "Y=&0F: workspace machine-ID lo offset", align=Align.INLINE)
d.comment(0x9867, "Store at (nfs_workspace)+&0F", align=Align.INLINE)
d.comment(0x9869, "Y=&0E", align=Align.INLINE)
d.comment(0x986A, "Pop saved machine ID", align=Align.INLINE)
d.comment(0x986B, "Store at (nfs_workspace)+&0F (reuse)", align=Align.INLINE)
d.comment(0x986D, "Scan remote-key flags", align=Align.INLINE)
d.comment(0x9870, "Initialise narrow workspace template", align=Align.INLINE)
d.comment(0x9873, "X=1: enable Econet keyboard", align=Align.INLINE)
d.comment(0x9875, "Y=0", align=Align.INLINE)
d.comment(0x9877, "OSBYTE &C9: read/write Econet keyboard disable", align=Align.INLINE)
d.label(0x987C, "lang_3_exec_0100")

d.subroutine(
    0x987C,
    "lang_3_exec_0100",
    title="Language reply 3: raise 'Remoted' error at &0100",
    description="""Calls [`commit_state_byte`](label:commit_state_byte) to record the new state,
loads `A=0` and tail-calls [`error_inline_log`](label:error_inline_log) with
the inline string `Remoted` followed by `&07` (BEL). Used by
remote-language replies that need to abort the current operation
with a terminal beep + error. Never returns.""",
)


d.comment(0x987C, "Commit the language-reply state byte", align=Align.INLINE)
d.entry(0x987C)
d.comment(0x987F, "A=0: 'Bad' error code", align=Align.INLINE)
d.comment(0x9881, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.comment(0x988D, "Read escape_flag", align=Align.INLINE)
d.subroutine(
    0x988D,
    "check_escape_and_classify",
    title="Acknowledge escape (if pressed) and classify reply",
    description="""If escape_flag bit 7 is clear OR need_release_tube bit 7 is clear (so AND result has bit 7 clear), returns immediately via return_1. Otherwise acknowledges escape via OSBYTE &7E (clears the escape condition and runs escape effects), loads A=6 (a synthesized 'Escape' error class), and tail-jumps to classify_reply_error to build the 'Escape' BRK error block.

Two callers: cmd_pass (&8E07) for password-entry escape, and send_net_packet (&9B46) for in-flight TX escape.""",
    on_entry={},
    on_exit={"a": "preserved (return) or never returns (escape path)"},
)


d.comment(0x988F, "Mask with need_release_tube (escape-disable)", align=Align.INLINE)
d.comment(0x9891, "Bit 7 clear: not escaping, return", align=Align.INLINE)
d.subroutine(
    0x9893,
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


d.comment(0x9893, "A=&7E: OSBYTE &7E = acknowledge Escape", align=Align.INLINE)
d.comment(0x9898, "A=6: error class for 'Escape'", align=Align.INLINE)
d.comment(0x989A, "JMP classify_reply_error (never returns)", align=Align.INLINE)
d.label(0x989D, "lang_4_validated")

d.subroutine(
    0x989D,
    "lang_4_validated",
    title="Language reply 4: validate remote session and apply",
    description="""Reads the first reply byte at `(net_rx_ptr),0`. If zero, branches
to [`init_remote_session`](label:init_remote_session) to set up a fresh remote
session. Otherwise reads the validation byte at offset `&80` and
the local stored value at workspace offset `&0E`; on mismatch,
the remote session is rejected.""",
)


d.comment(0x989D, "Y=0: status byte offset", align=Align.INLINE)
d.entry(0x989D)
d.comment(0x989F, "Read RX status byte", align=Align.INLINE)
d.comment(0x98A1, "Zero status: re-init the session", align=Align.INLINE)
d.comment(0x98A3, "Y=&80: session-ID byte offset in RX", align=Align.INLINE)
d.comment(0x98A5, "Read remote session-ID", align=Align.INLINE)
d.comment(0x98A7, "Y=&0E: stored session-ID offset in workspace", align=Align.INLINE)
d.comment(0x98A9, "Compare with stored ID", align=Align.INLINE)
d.comment(0x98AB, "Mismatch: skip the commit (treat as foreign)", align=Align.INLINE)
d.label(0x98AD, "lang_0_insert_key")

d.subroutine(
    0x98AD,
    "lang_0_insert_key",
    title="Language reply 0: insert remote keypress",
    description="""Reads the keycode from the reply at `(net_rx_ptr),&82` into `Y`,
sets `X=0`, calls [`commit_state_byte`](label:commit_state_byte) to record
the state change, and issues `OSBYTE &99` (insert into keyboard
buffer) to deliver the keypress to the local machine.""",
    on_entry={"a": "ignored (entry from reply dispatch)"},
)


d.comment(0x98AD, "Y=&82: keypress byte offset in RX", align=Align.INLINE)
d.entry(0x98AD)
d.comment(0x98AF, "Read remote keypress code", align=Align.INLINE)
d.comment(0x98B1, "Y = key code", align=Align.INLINE)
d.comment(0x98B2, "X=0: keyboard buffer ID", align=Align.INLINE)
d.comment(0x98B4, "Commit the language-reply state", align=Align.INLINE)
d.comment(0x98B7, "OSBYTE &99: insert byte into input buffer", align=Align.INLINE)
d.label(0x98BC, "wait_net_tx_ack")

d.subroutine(
    0x98BC,
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


d.comment(0x98BC, "Read the configurable rx-wait timeout (&0D6E, default &28 = ~22s on 2 MHz)", align=Align.INLINE)
d.comment(0x98BF, "Push it as the outermost counter (read back via stack-X indexing later)", align=Align.INLINE)
d.comment(0x98C0, "Read econet_flags so we can preserve it across the wait", align=Align.INLINE)
d.comment(0x98C3, "Push it (we'll temporarily set bit 7 to mark waiting)", align=Align.INLINE)
d.comment(0x98C4, "Check whether net_tx_ptr_hi is non-zero (TX in flight?)", align=Align.INLINE)
d.comment(0x98C6, "Yes: skip the flag-set; counters initialise either way", align=Align.INLINE)
d.comment(0x98C8, "TX idle: set bit 7 of econet_flags (signal RX-only wait)", align=Align.INLINE)
d.comment(0x98CA, "Write the modified flags back", align=Align.INLINE)
d.label(0x98CD, "init_poll_counters")

d.comment(0x98CD, "A=0: initial value for inner+middle counters", align=Align.INLINE)
d.comment(0x98CF, "Push it -- middle counter at stack[X+2]", align=Align.INLINE)
d.comment(0x98D0, "Push it again -- inner counter at stack[X+1]", align=Align.INLINE)
d.comment(0x98D1, "Y=0: indirect index for net_tx_ptr poll", align=Align.INLINE)
d.comment(0x98D2, "Capture S into X so we can address the stack counters", align=Align.INLINE)
d.label(0x98D3, "loop_poll_tx")

d.comment(0x98D3, "Read RX/TX flags through net_tx_ptr -- bit 7 set means complete", align=Align.INLINE)
d.comment(0x98D5, "Bit 7 set: reply received, exit poll", align=Align.INLINE)
d.comment(0x98D7, "Decrement inner counter at stack[X+1]", align=Align.INLINE)
d.comment(0x98DA, "Inner not zero yet: poll again", align=Align.INLINE)
d.comment(0x98DC, "Inner wrapped: decrement middle at stack[X+2]", align=Align.INLINE)
d.comment(0x98DF, "Middle not zero: poll again", align=Align.INLINE)
d.comment(0x98E1, "Middle wrapped: decrement outer at stack[X+4] (the saved timeout value)", align=Align.INLINE)
d.comment(0x98E4, "Outer not zero: poll again", align=Align.INLINE)
d.comment(0x98E6, "Reload the original timeout to test for timeout=0 mode", align=Align.INLINE)
d.comment(0x98E9, "Configured timeout was non-zero: declare timeout", align=Align.INLINE)
d.comment(0x98EB, "Timeout=0 (poll forever): check escape flag", align=Align.INLINE)
d.comment(0x98ED, "Escape pressed: jump to escape handler at &9895", align=Align.INLINE)
d.comment(0x98EF, "Reset outer counter so we keep polling", align=Align.INLINE)
d.comment(0x98F2, "Always taken (INC's result is always non-zero here): back to inner", align=Align.INLINE)
d.label(0x98F4, "done_poll_tx")

d.comment(0x98F4, "done_poll_tx: discard inner counter", align=Align.INLINE)
d.comment(0x98F5, "Discard middle counter", align=Align.INLINE)
d.comment(0x98F6, "Pull saved econet_flags", align=Align.INLINE)
d.comment(0x98F7, "Restore them (clearing bit 7 if we set it)", align=Align.INLINE)
d.comment(0x98FA, "Pull saved rx_wait_timeout into A", align=Align.INLINE)
d.comment(0x98FB, "If timeout reached zero, raise 'No reply'", align=Align.INLINE)
d.comment(0x98FD, "Reply received normally: return", align=Align.INLINE)
d.label(0x98FE, "cond_save_error_code")

d.subroutine(
    0x98FE,
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


d.comment(0x98FE, "Test bit 7 of fs_flags (FS-active flag)", align=Align.INLINE)
d.comment(0x9901, "FS not active: skip the save", align=Align.INLINE)
d.comment(0x9903, "FS active: store error code at &C009 (last-error byte)", align=Align.INLINE)
d.label(0x9906, "rts_cond_save_err")

d.comment(0x9906, "Return", align=Align.INLINE)
d.label(0x9907, "build_no_reply_error")

d.comment(0x9907, "X=8: net_error_lookup_data offset for 'No reply' message", align=Align.INLINE)
d.comment(0x9909, "Y = message offset within the string table (&9AA4 base)", align=Align.INLINE)
d.comment(0x990C, "X=0: error-text buffer index", align=Align.INLINE)
d.comment(0x990E, "Zero the &0100 length byte (length will be filled in later)", align=Align.INLINE)
d.comment(0x9911, "Read first message byte (the error code)", align=Align.INLINE)
d.comment(0x9914, "Conditionally save it as last-error", align=Align.INLINE)
d.label(0x9917, "loop_copy_no_reply_msg")

d.comment(0x9917, "Read next message byte", align=Align.INLINE)
d.comment(0x991A, "Append to error-text buffer at &0101+X", align=Align.INLINE)
d.comment(0x991D, "Null terminator: message done", align=Align.INLINE)
d.comment(0x991F, "Step buffer index", align=Align.INLINE)
d.comment(0x9920, "Step source offset", align=Align.INLINE)
d.comment(0x9921, "Loop while Y != 0 (Y wraps at 256, not expected)", align=Align.INLINE)
d.label(0x9923, "done_no_reply_msg")

d.comment(0x9923, "Append ' on drive <num>' or similar context", align=Align.INLINE)
d.comment(0x9926, "A=0: null terminator", align=Align.INLINE)
d.comment(0x9928, "Store at end of message", align=Align.INLINE)
d.comment(0x992B, "Tail-jump to dispatch the BRK error", align=Align.INLINE)
d.label(0x992E, "fixup_reply_status_a")

d.subroutine(
    0x992E,
    "fixup_reply_status_a",
    title="Substitute 'B' for 'A' in reply status byte",
    description="""Reads the FS reply status byte at (net_tx_ptr,X). If it is 'A'
(Acknowledge with no error), substitutes 'B' so downstream code
treats it as a soft error. CLV before falling through into
mask_error_class to ensure the no-extended-error path is taken.""",
    on_entry={"x": "indirect index into net_tx_ptr"},
    on_exit={"a": "reply status byte (with A->B substitution)", "v": "0 (clear)"},
)


d.comment(0x992E, "Read FS reply status byte at (net_tx_ptr,X)", align=Align.INLINE)
d.comment(0x9930, "Status 'A'? (Acknowledge with no error)", align=Align.INLINE)
d.comment(0x9932, "Not 'A': pass through unchanged", align=Align.INLINE)
d.comment(0x9934, "Substitute 'B' for 'A' (handle ACK as a soft error)", align=Align.INLINE)
d.label(0x9936, "skip_if_not_a")

d.comment(0x9936, "Clear V to take the standard mask path", align=Align.INLINE)
d.comment(0x9937, "Always taken: use the standard masked-error path", align=Align.INLINE)
d.label(0x9939, "load_reply_and_classify")

d.subroutine(
    0x9939,
    "load_reply_and_classify",
    title="Load reply byte and classify error",
    description="""Single-byte prologue to
[`classify_reply_error`](label:classify_reply_error): `LDA (net_tx_ptr,X)`
reads the FS reply status byte, then falls through. Single
caller (`&9B6A`, after a recv-and-classify path that already
has `X` set).""",
    on_entry={"x": "indirect index into net_tx_ptr"},
)


d.comment(0x9939, "Read FS reply status byte", align=Align.INLINE)
d.label(0x993B, "classify_reply_error")

d.subroutine(
    0x993B,
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


d.comment(0x993B, "BIT $always_set_v_byte: force V=1 (extended-error path)", align=Align.INLINE)
d.label(0x993E, "mask_error_class")

d.comment(0x993E, "Mask to 3 bits (error class 0..7)", align=Align.INLINE)
d.comment(0x9940, "Save error class on stack", align=Align.INLINE)
d.comment(0x9941, "Class 2 = 'station-related' family?", align=Align.INLINE)
d.comment(0x9943, "No: build a simple one-line error", align=Align.INLINE)
d.comment(0x9945, "Class 2 yes: save flags so we can branch on V later", align=Align.INLINE)
d.comment(0x9946, "X = error class (=2)", align=Align.INLINE)
d.comment(0x9947, "Y = lookup-table offset", align=Align.INLINE)
d.comment(0x994A, "Read first message byte (error code)", align=Align.INLINE)
d.comment(0x994D, "Conditionally save it", align=Align.INLINE)
d.comment(0x9950, "X=0: text-buffer index", align=Align.INLINE)
d.comment(0x9952, "Zero length byte", align=Align.INLINE)
d.label(0x9955, "loop_copy_station_msg")

d.comment(0x9955, "Read message byte", align=Align.INLINE)
d.comment(0x9958, "Append to buffer", align=Align.INLINE)
d.comment(0x995B, "Null terminator -- station message done", align=Align.INLINE)
d.comment(0x995D, "Advance Y", align=Align.INLINE)
d.comment(0x995E, "Advance X", align=Align.INLINE)
d.comment(0x995F, "Loop until X wraps", align=Align.INLINE)
d.label(0x9961, "done_station_msg")

d.comment(0x9961, "Append ' on drive <num>' suffix", align=Align.INLINE)
d.comment(0x9964, "Restore the saved class flags", align=Align.INLINE)
d.comment(0x9965, "V was set: use 'not listening' suffix", align=Align.INLINE)
d.comment(0x9967, "A=&A4: 'station <n> not available' error code", align=Align.INLINE)
d.comment(0x9969, "Save the alternative error code", align=Align.INLINE)
d.comment(0x996C, "Patch error-text buffer length byte", align=Align.INLINE)
d.comment(0x996F, "Y=&0B: lookup index for the listening-station suffix", align=Align.INLINE)
d.comment(0x9971, "Always taken (Y is non-zero); jump to load_suffix_offset", align=Align.INLINE)
d.label(0x9973, "suffix_not_listening")

d.comment(0x9973, "V was clear: 'not listening' suffix variant", align=Align.INLINE)
d.label(0x9975, "load_suffix_offset")

d.comment(0x9975, "Read suffix offset from lookup", align=Align.INLINE)
d.comment(0x9978, "Y = suffix offset", align=Align.INLINE)
d.label(0x9979, "loop_copy_suffix")

d.comment(0x9979, "Read suffix byte", align=Align.INLINE)
d.comment(0x997C, "Append", align=Align.INLINE)
d.comment(0x997F, "Null: suffix done", align=Align.INLINE)
d.comment(0x9981, "Step Y", align=Align.INLINE)
d.label(0x9982, "suffix_copy_loop")

d.comment(0x9982, "Step X", align=Align.INLINE)
d.comment(0x9983, "Loop while X != 0 (max 255 chars)", align=Align.INLINE)
d.label(0x9985, "done_suffix")

d.comment(0x9985, "Always taken (Z still set from BEQ): final terminator check", align=Align.INLINE)
d.label(0x9987, "build_simple_error")

d.comment(0x9987, "X = error class", align=Align.INLINE)
d.comment(0x9988, "Y = lookup-table offset", align=Align.INLINE)
d.comment(0x998B, "X=0: buffer index", align=Align.INLINE)
d.comment(0x998D, "Zero length", align=Align.INLINE)
d.comment(0x9990, "Read first message byte (error code)", align=Align.INLINE)
d.comment(0x9993, "Conditionally save it", align=Align.INLINE)
d.label(0x9996, "loop_copy_error_msg")

d.comment(0x9996, "Read next message byte", align=Align.INLINE)
d.comment(0x9999, "Append to buffer", align=Align.INLINE)
d.label(0x999C, "check_msg_terminator")

d.comment(0x999C, "Null terminator -> dispatch", align=Align.INLINE)
d.comment(0x999E, "Step Y", align=Align.INLINE)
d.comment(0x999F, "Step X", align=Align.INLINE)
d.label(0x99A0, "bad_str_anchor")

d.comment(0x99A0, "Loop while X != 0", align=Align.INLINE)
d.label(0x99A1, "bad_prefix_table")

d.hook_subroutine(0x99A5, "error_bad_inline", stringz_hook)

d.subroutine(
    0x99A5,
    "error_bad_inline",
    title="Generate 'Bad ...' BRK error from inline string",
    description="""Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""",
    on_entry={"a": "error number"},
)
d.comment(0x99A5, "Conditionally log error code to workspace", align=Align.INLINE)
d.comment(0x99A8, "Save error number in Y", align=Align.INLINE)
d.comment(0x99A9, "Pop return address (low) — points to last byte of JSR", align=Align.INLINE)
d.comment(0x99AA, "Store return address low", align=Align.INLINE)
d.comment(0x99AC, "Pop return address (high)", align=Align.INLINE)
d.comment(0x99AD, "Store return address high", align=Align.INLINE)
d.comment(0x99AF, "X=0: start of prefix string", align=Align.INLINE)
d.label(0x99B1, "loop_copy_bad_prefix")

d.comment(0x99B1, "Copy 'Bad ' prefix from lookup table", align=Align.INLINE)
d.comment(0x99B2, "Get next prefix character", align=Align.INLINE)
d.comment(0x99B5, "Store in error text buffer", align=Align.INLINE)
d.comment(0x99B8, "Is it space (end of 'Bad ')?", align=Align.INLINE)
d.comment(0x99BA, "No: copy next prefix character", align=Align.INLINE)
d.hook_subroutine(0x99BE, "error_inline_log", stringz_hook)
d.subroutine(
    0x99BE,
    "error_inline_log",
    title="Generate BRK error from inline string (with logging)",
    description="""Like error_inline, but first conditionally logs the error code to
workspace via cond_save_error_code before building the error block.""",
    on_entry={"a": "error number"},
)
d.comment(0x99BE, "Conditionally log error code to workspace", align=Align.INLINE)


d.hook_subroutine(0x99C1, "error_inline", stringz_hook)
d.subroutine(
    0x99C1,
    "error_inline",
    title="Generate BRK error from inline string",
    description="""Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""",
    on_entry={"a": "error number (stored in error block at &0101)"},
)
d.comment(0x99C1, "Save error number in Y", align=Align.INLINE)
d.comment(0x99C2, "Pop return address (low) — points to last byte of JSR", align=Align.INLINE)
d.comment(0x99C3, "Store return address low", align=Align.INLINE)
d.comment(0x99C5, "Pop return address (high)", align=Align.INLINE)


d.comment(0x99C6, "Store return address high", align=Align.INLINE)
d.comment(0x99C8, "X=0: error text index", align=Align.INLINE)
d.label(0x99CA, "write_error_num_and_str")

d.comment(0x99CA, "Store error number in error block", align=Align.INLINE)
d.comment(0x99CD, "Copy error number to A", align=Align.INLINE)
d.comment(0x99CE, "Push error number on stack", align=Align.INLINE)
d.comment(0x99CF, "Y=0: inline string index", align=Align.INLINE)
d.comment(0x99D1, "Zero the BRK byte at &0100", align=Align.INLINE)
d.label(0x99D4, "loop_copy_inline_str")

d.comment(0x99D4, "Copy inline string into error block", align=Align.INLINE)
d.comment(0x99D5, "Advance string index", align=Align.INLINE)
d.comment(0x99D6, "Read next byte from inline string", align=Align.INLINE)
d.comment(0x99D8, "Store byte in error block", align=Align.INLINE)
d.comment(0x99DB, "Loop until null terminator", align=Align.INLINE)
d.label(0x99DD, "check_net_error_code")

d.subroutine(
    0x99DD,
    "check_net_error_code",
    title="Translate net error: 'OK' → return, 'FS error' → append",
    description="""Reads the receive-attribute byte:

| Receive attribute | Action |
|---|---|
| non-zero | network error – branch to `handle_net_error` |
| zero, saved error = `&DE` (FS error code) | branch to `append_error_number` to add the FS-specific code to the error text |
| zero, saved error other | tail-jump to `&0100` (BRK error block) to trigger BRK and let MOS dispatch |""",
)


d.comment(0x99DD, "Read receive attribute byte", align=Align.INLINE)
d.comment(0x99E0, "Non-zero: network returned an error", align=Align.INLINE)
d.comment(0x99E2, "Pop saved error number", align=Align.INLINE)
d.comment(0x99E3, "Was it &DE (file server error)?", align=Align.INLINE)
d.comment(0x99E5, "Yes: append error number and trigger BRK", align=Align.INLINE)
d.label(0x99E7, "trigger_brk")

d.comment(0x99E7, "Jump to BRK via error block", align=Align.INLINE)
d.label(0x99EA, "handle_net_error")

d.comment(0x99EA, "Store error code in workspace", align=Align.INLINE)
d.comment(0x99ED, "Push error code", align=Align.INLINE)
d.comment(0x99EE, "Save X (error text index)", align=Align.INLINE)
d.comment(0x99EF, "Push X", align=Align.INLINE)
d.comment(0x99F0, "Read receive attribute byte", align=Align.INLINE)
d.comment(0x99F3, "Save to fs_load_addr as spool handle", align=Align.INLINE)
d.comment(0x99F5, "A=0: clear error code in RX buffer", align=Align.INLINE)
d.comment(0x99F7, "Zero the error code byte in buffer", align=Align.INLINE)
d.comment(0x99F9, "A=&C6: OSBYTE read spool handle", align=Align.INLINE)
d.comment(0x99FB, "Read current spool file handle", align=Align.INLINE)
d.comment(0x99FE, "Compare Y result with saved handle", align=Align.INLINE)
d.comment(0x9A00, "Match: close the spool file", align=Align.INLINE)
d.comment(0x9A02, "Compare X result with saved handle", align=Align.INLINE)
d.comment(0x9A04, "No match: skip spool close", align=Align.INLINE)
d.comment(0x9A06, "Push A (preserved)", align=Align.INLINE)
d.comment(0x9A07, "A=&C6: disable spool with OSBYTE", align=Align.INLINE)
d.comment(0x9A09, "ALWAYS branch to close spool", align=Align.INLINE)
d.label(0x9A0B, "net_error_close_spool")

d.comment(0x9A0C, "A=&C7: OSBYTE 'flush input buffer'", align=Align.INLINE)
d.label(0x9A0E, "close_spool_exec")

d.comment(0x9A0E, "Tail-call OSBYTE with X=0/Y=0", align=Align.INLINE)
d.comment(0x9A12, "A=0: close file", align=Align.INLINE)
d.comment(0x9A14, "Close the spool/exec file", align=Align.INLINE)
d.label(0x9A17, "done_close_files")

d.comment(0x9A17, "Pull saved X (error text index)", align=Align.INLINE)
d.comment(0x9A18, "Restore X", align=Align.INLINE)
d.comment(0x9A19, "Y=&0A: lookup index for 'on channel'", align=Align.INLINE)
d.comment(0x9A1B, "Load message offset from lookup table", align=Align.INLINE)
d.comment(0x9A1E, "Transfer offset to Y", align=Align.INLINE)
d.label(0x9A1F, "loop_copy_channel_msg")

d.comment(0x9A1F, "Load error message byte", align=Align.INLINE)
d.comment(0x9A22, "Append to error text buffer", align=Align.INLINE)
d.comment(0x9A25, "Null terminator: done copying", align=Align.INLINE)
d.comment(0x9A27, "Advance error text index", align=Align.INLINE)
d.comment(0x9A28, "Advance message index", align=Align.INLINE)
d.comment(0x9A29, "Loop until full message copied", align=Align.INLINE)
d.label(0x9A2B, "append_error_number")

d.comment(0x9A2B, "Save error text end position", align=Align.INLINE)
d.comment(0x9A2D, "Pull saved error number", align=Align.INLINE)
d.comment(0x9A2E, "Append ' nnn' error number suffix", align=Align.INLINE)
d.comment(0x9A31, "A=0: null terminator", align=Align.INLINE)
d.comment(0x9A33, "Terminate error text string", align=Align.INLINE)
d.comment(0x9A36, "ALWAYS branch to trigger BRK error", align=Align.INLINE)
d.label(0x9A38, "append_drv_dot_num")

d.subroutine(
    0x9A38,
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


d.comment(0x9A38, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9A3A, "Append space to error text", align=Align.INLINE)
d.comment(0x9A3D, "Advance error text index", align=Align.INLINE)
d.comment(0x9A3E, "Save position for number formatting", align=Align.INLINE)
d.comment(0x9A40, "Y=3: offset to network number in TX CB", align=Align.INLINE)
d.comment(0x9A42, "Load network number", align=Align.INLINE)
d.comment(0x9A44, "Zero: skip network part (local)", align=Align.INLINE)
d.comment(0x9A46, "Append network number as decimal", align=Align.INLINE)
d.comment(0x9A49, "Reload error text position", align=Align.INLINE)
d.comment(0x9A4B, "A='.': dot separator", align=Align.INLINE)
d.comment(0x9A4D, "Append dot to error text", align=Align.INLINE)
d.comment(0x9A50, "Advance past dot", align=Align.INLINE)
d.label(0x9A52, "append_station_num")

d.comment(0x9A52, "Y=2: offset to station number in TX CB", align=Align.INLINE)
d.comment(0x9A54, "Load station number", align=Align.INLINE)
d.comment(0x9A56, "Append station number as decimal", align=Align.INLINE)
d.comment(0x9A59, "Reload error text position", align=Align.INLINE)
d.comment(0x9A5B, "Return", align=Align.INLINE)
d.label(0x9A5C, "append_space_and_num")

d.subroutine(
    0x9A5C,
    "append_space_and_num",
    title="Append space and decimal number to error text",
    description="""Writes a space character to the error text buffer
at the current position (fs_load_addr_2), then falls
through to append_decimal_num to convert the value
in A to decimal digits with leading zero suppression.""",
    on_entry={"a": "number to append (0-255)"},
)


d.comment(0x9A5C, "Save number in Y", align=Align.INLINE)
d.comment(0x9A5D, "A=' ': space prefix", align=Align.INLINE)
d.comment(0x9A5F, "Load current error text position", align=Align.INLINE)
d.comment(0x9A61, "Append space to error text", align=Align.INLINE)
d.comment(0x9A64, "Advance position past space", align=Align.INLINE)
d.comment(0x9A66, "Restore number to A", align=Align.INLINE)
d.label(0x9A67, "append_decimal_num")

d.subroutine(
    0x9A67,
    "append_decimal_num",
    title="Convert byte to decimal and append to error text",
    description="""Extracts hundreds, tens and units digits by three
successive calls to append_decimal_digit. Uses the
V flag to suppress leading zeros — hundreds and tens
are skipped when zero, but the units digit is always
emitted.""",
    on_entry={"a": "number to convert (0-255)"},
)


d.comment(0x9A67, "Save number in Y for division", align=Align.INLINE)
d.comment(0x9A68, "Set V: suppress leading zeros", align=Align.INLINE)
d.comment(0x9A6B, "A=100: hundreds digit divisor", align=Align.INLINE)
d.comment(0x9A6D, "Extract and append hundreds digit", align=Align.INLINE)
d.comment(0x9A70, "A=10: tens digit divisor", align=Align.INLINE)
d.comment(0x9A72, "Extract and append tens digit", align=Align.INLINE)
d.comment(0x9A75, "A=1: units digit (remainder)", align=Align.INLINE)
d.comment(0x9A77, "Clear V: always print units digit", align=Align.INLINE)
d.label(0x9A78, "append_decimal_digit")

d.subroutine(
    0x9A78,
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


d.comment(0x9A78, "Store divisor", align=Align.INLINE)
d.comment(0x9A7A, "Copy number to A for division", align=Align.INLINE)
d.comment(0x9A7B, "X='0'-1: digit counter (ASCII offset)", align=Align.INLINE)
d.comment(0x9A7D, "Save V flag (leading zero suppression)", align=Align.INLINE)
d.comment(0x9A7E, "Set carry for subtraction", align=Align.INLINE)
d.label(0x9A7F, "loop_count_digit")

d.comment(0x9A7F, "Increment digit counter", align=Align.INLINE)
d.comment(0x9A80, "Subtract divisor", align=Align.INLINE)
d.comment(0x9A82, "Not negative yet: continue counting", align=Align.INLINE)
d.comment(0x9A84, "Add back divisor (restore remainder)", align=Align.INLINE)
d.comment(0x9A86, "Restore V flag", align=Align.INLINE)
d.comment(0x9A87, "Save remainder back to Y", align=Align.INLINE)
d.comment(0x9A88, "Digit counter to A (ASCII digit)", align=Align.INLINE)
d.comment(0x9A89, "Is digit '0'?", align=Align.INLINE)
d.comment(0x9A8B, "Non-zero: always print", align=Align.INLINE)
d.comment(0x9A8D, "V set (suppress leading zeros): skip", align=Align.INLINE)
d.label(0x9A8F, "store_digit")

d.comment(0x9A8F, "Clear V: first non-zero digit seen", align=Align.INLINE)
d.comment(0x9A90, "Load current text position", align=Align.INLINE)
d.comment(0x9A92, "Store ASCII digit in error text", align=Align.INLINE)
d.comment(0x9A95, "Advance text position", align=Align.INLINE)
d.label(0x9A97, "rts_store_digit")

d.comment(0x9A97, "Return", align=Align.INLINE)
d.index_base(0x9A98, "net_error_lookup_data")
d.banner(
    0x9A98,
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
    d.byte(0x9A98 + i)
d.expr(0x9A99, sym("msg_net_error") - sym("error_msg_table"))
d.expr(0x9A9A, sym("msg_station") - sym("error_msg_table"))
d.expr(0x9A9B, sym("msg_no_clock") - sym("error_msg_table"))
d.expr(0x9A9C, sym("msg_escape") - sym("error_msg_table"))
d.expr(0x9A9D, sym("msg_escape") - sym("error_msg_table"))
d.expr(0x9A9E, sym("msg_escape") - sym("error_msg_table"))
d.expr(0x9A9F, sym("msg_bad_option") - sym("error_msg_table"))
d.expr(0x9AA0, sym("msg_no_reply") - sym("error_msg_table"))
d.expr(0x9AA1, sym("msg_not_listening") - sym("error_msg_table"))
d.expr(0x9AA2, sym("msg_on_channel") - sym("error_msg_table"))
d.expr(0x9AA3, sym("msg_not_present") - sym("error_msg_table"))

d.index_base(0x9AA4, "error_msg_table")
d.banner(
    0x9AA4,
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

d.comment(0x9AA5, "err_line_jammed = &A0", align=Align.INLINE)
d.comment(0x9AB0, "Null terminator", align=Align.INLINE)
d.label(0x9AB1, "msg_net_error")

d.comment(0x9AB1, "Error &A1: Net error", align=Align.INLINE)
d.comment(0x9AB2, "err_net_error = &A1", align=Align.INLINE)
d.comment(0x9ABB, "Null terminator", align=Align.INLINE)
d.label(0x9ABC, "msg_station")

d.comment(0x9ABC, "Error &A2: Station", align=Align.INLINE)
d.label(0x9AC5, "msg_no_clock")

d.byte(0x9ACE)
d.comment(0x9ACE, "Null terminator", align=Align.INLINE)
d.label(0x9ACF, "msg_escape")

d.byte(0x9ACF)
d.comment(0x9ACF, "Error &11: Escape", align=Align.INLINE)
d.label(0x9AD7, "msg_bad_option")

d.byte(0x9AD7)
d.comment(0x9AD7, "Error &CB: Bad option", align=Align.INLINE)
d.comment(0x9AE2, "Null terminator + Error &A5: No reply from station", align=Align.INLINE)
d.label(0x9AE3, "msg_no_reply")

d.comment(0x9AE4, "err_no_reply = &A5 message body", align=Align.INLINE)
d.comment(0x9AF9, "Null terminator", align=Align.INLINE)
d.label(0x9AFA, "msg_not_listening")

d.comment(0x9AFA, "Suffix string (offset &56 in lookup)", align=Align.INLINE)
d.byte(0x9B08)
d.comment(0x9B08, "Null terminator", align=Align.INLINE)
d.label(0x9B09, "msg_on_channel")

d.comment(0x9B09, 'Suffix: \\" on channel\\"', align=Align.INLINE)
d.byte(0x9B14)
d.comment(0x9B14, "Null terminator", align=Align.INLINE)
d.label(0x9B15, "msg_not_present")
d.comment(0x9B15, 'Suffix: \\" not present\\"', align=Align.INLINE)
d.comment(0x9B21, "Null terminator", align=Align.INLINE)
d.label(0x9B22, "init_tx_ptr_and_send")

d.subroutine(
    0x9B22,
    "init_tx_ptr_and_send",
    title="Point TX at zero-page TXCB and send",
    description="""Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the
standard TXCB location in zero page), then falls
through to send_net_packet for transmission with
retry logic.""",
    on_exit={"a": "TX result code (0 = success; &40 jammed; &41 not listening; etc.) -- see send_net_packet"},
)


d.comment(0x9B22, "X=&C0: TX control block base (low)", align=Align.INLINE)
d.comment(0x9B24, "Set TX pointer low", align=Align.INLINE)
d.comment(0x9B26, "X=0: TX control block base (high)", align=Align.INLINE)
d.comment(0x9B28, "Set TX pointer high (page 0)", align=Align.INLINE)
d.label(0x9B2A, "send_net_packet")

d.subroutine(
    0x9B2A,
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


d.comment(0x9B2A, "Load retry count from workspace", align=Align.INLINE)
d.comment(0x9B2D, "Non-zero: use configured retry count", align=Align.INLINE)
d.comment(0x9B2F, "A=&FF: default retry count (255)", align=Align.INLINE)
d.label(0x9B31, "set_timeout")

d.comment(0x9B31, "Y=&60: timeout value", align=Align.INLINE)
d.comment(0x9B33, "Push retry count", align=Align.INLINE)
d.comment(0x9B34, "A=&60: copy timeout to A", align=Align.INLINE)
d.comment(0x9B35, "Push timeout", align=Align.INLINE)
d.comment(0x9B36, "X=0: TX pointer index", align=Align.INLINE)
d.comment(0x9B38, "Load first byte of TX control block", align=Align.INLINE)
d.label(0x9B3A, "start_tx_attempt")

d.comment(0x9B3A, "Restore control byte (overwritten by result code on retry)", align=Align.INLINE)
d.comment(0x9B3C, "Push control byte", align=Align.INLINE)
d.comment(0x9B3D, "Poll ADLC until line idle", align=Align.INLINE)
d.comment(0x9B40, "Bit 6 (error flag) into N", align=Align.INLINE)
d.comment(0x9B41, "N=0 (bit 6 clear): success", align=Align.INLINE)
d.comment(0x9B43, "Shift away error flag, keep error type", align=Align.INLINE)
d.comment(0x9B44, "Z=1 (no type bits): fatal; Z=0: retryable", align=Align.INLINE)
d.comment(0x9B46, "Check for escape condition", align=Align.INLINE)
d.comment(0x9B49, "Pull control byte", align=Align.INLINE)
d.comment(0x9B4A, "Restore to X", align=Align.INLINE)
d.comment(0x9B4B, "Pull timeout", align=Align.INLINE)
d.comment(0x9B4C, "Restore to Y", align=Align.INLINE)
d.comment(0x9B4D, "Pull retry count", align=Align.INLINE)
d.comment(0x9B4E, "Zero retries remaining: try alternate", align=Align.INLINE)
d.label(0x9B50, "loop_retry_tx")

d.comment(0x9B50, "Decrement retry counter", align=Align.INLINE)
d.comment(0x9B52, "Push updated retry count", align=Align.INLINE)
d.comment(0x9B53, "Copy timeout to A", align=Align.INLINE)
d.comment(0x9B54, "Push timeout for delay loop", align=Align.INLINE)
d.comment(0x9B55, "Copy control byte to A", align=Align.INLINE)
d.label(0x9B56, "loop_tx_delay")

d.comment(0x9B56, "Inner delay: decrement X", align=Align.INLINE)
d.comment(0x9B57, "Loop until X=0", align=Align.INLINE)
d.comment(0x9B59, "Decrement outer counter Y", align=Align.INLINE)
d.comment(0x9B5A, "Loop until Y=0", align=Align.INLINE)
d.comment(0x9B5C, "ALWAYS branch: retry transmission", align=Align.INLINE)
d.label(0x9B5E, "try_alternate_phase")

d.comment(0x9B5E, "Compare retry count with alternate", align=Align.INLINE)
d.comment(0x9B61, "Different: go to error handling", align=Align.INLINE)
d.comment(0x9B63, "A=&80: set escapable flag", align=Align.INLINE)
d.comment(0x9B65, "Mark as escapable for second phase", align=Align.INLINE)
d.comment(0x9B67, "ALWAYS branch: retry with escapable", align=Align.INLINE)
d.label(0x9B69, "tx_send_error")

d.comment(0x9B69, "Result code to X", align=Align.INLINE)
d.comment(0x9B6A, "Jump to classify reply and return", align=Align.INLINE)
d.label(0x9B6D, "tx_success")

d.comment(0x9B6D, "Pull control byte", align=Align.INLINE)
d.comment(0x9B6E, "Pull timeout", align=Align.INLINE)
d.comment(0x9B6F, "Pull retry count", align=Align.INLINE)
d.comment(0x9B70, "Clear escapable flag and return", align=Align.INLINE)
d.index_base(0x9B73, "pass_txbuf_init_table")
d.banner(
    0x9B73,
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
and restored after transmission.""",
)
for i in range(12):
    d.byte(0x9B73 + i)

d.comment(0x9B73, "Offset 0: ctrl = &88 (immediate TX)", align=Align.INLINE)
d.comment(0x9B74, "Offset 1: port = &00 (immediate op)", align=Align.INLINE)
d.comment(0x9B75, "Offset 2: &FD skip (preserve dest stn)", align=Align.INLINE)
d.comment(0x9B76, "Offset 3: &FD skip (preserve dest net)", align=Align.INLINE)
d.comment(0x9B77, "Offset 4: buf start lo (&3A) -> &0D3A", align=Align.INLINE)
d.comment(0x9B78, "Offset 5: buf start hi (&0D) -> &0D3A", align=Align.INLINE)
d.comment(0x9B79, "Offset 6: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x9B7A, "Offset 7: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x9B7B, "Offset 8: buf end lo (&3E) -> &0D3E", align=Align.INLINE)
d.comment(0x9B7C, "Offset 9: buf end hi (&0D) -> &0D3E", align=Align.INLINE)
d.comment(0x9B7D, "Offset 10: extended-addr fill (&FF)", align=Align.INLINE)
d.comment(0x9B7E, "Offset 11: extended-addr fill (&FF)", align=Align.INLINE)
d.label(0x9B7F, "init_tx_ptr_for_pass")

d.subroutine(
    0x9B7F,
    "init_tx_ptr_for_pass",
    title="Set up TX pointer and send pass-through packet",
    description="""Copies the template into the TX buffer (skipping
&FD markers), saves original values on stack,
then polls the ADLC and retries until complete.""",
    on_exit={"a": "TX result (from poll_econet_data_continue_frame_status)"},
)


d.comment(0x9B7F, "Y=&C0: TX control block base (low)", align=Align.INLINE)
d.comment(0x9B81, "Set TX pointer low byte", align=Align.INLINE)
d.comment(0x9B83, "Y=0: TX control block base (high)", align=Align.INLINE)
d.comment(0x9B85, "Set TX pointer high byte", align=Align.INLINE)
d.label(0x9B87, "setup_pass_txbuf")

d.subroutine(
    0x9B87,
    "setup_pass_txbuf",
    title="Initialise TX buffer from pass-through template",
    description="""Copies 12 bytes from pass_txbuf_init_table into the
TX control block, pushing the original values on the
stack for later restoration. Skips offsets marked &FD
in the template. Starts transmission via
poll_econet_data_continue_frame_status and retries on failure, restoring
the original TX buffer contents when done.""",
    on_exit={"a": "TX result (from poll_econet_data_continue_frame_status)"},
)


d.comment(0x9B87, "Y=&0B: 12 bytes to process (0-11)", align=Align.INLINE)
d.label(0x9B89, "loop_copy_template")

d.comment(0x9B89, "Load template byte for this offset", align=Align.INLINE)
d.comment(0x9B8C, "Is it &FD (skip marker)?", align=Align.INLINE)
d.comment(0x9B8E, "Yes: skip this offset, don't modify", align=Align.INLINE)
d.comment(0x9B90, "Load existing TX buffer byte", align=Align.INLINE)
d.comment(0x9B92, "Save original value on stack", align=Align.INLINE)
d.comment(0x9B93, "Copy template value to A", align=Align.INLINE)
d.comment(0x9B94, "Store template value to TX buffer", align=Align.INLINE)
d.label(0x9B96, "skip_template_byte")

d.comment(0x9B96, "Next offset (descending)", align=Align.INLINE)
d.comment(0x9B97, "Loop until all 12 bytes processed", align=Align.INLINE)
d.comment(0x9B99, "Load pass-through control value", align=Align.INLINE)
d.comment(0x9B9C, "Push control value", align=Align.INLINE)
d.comment(0x9B9D, "A=&FF (Y is &FF after loop)", align=Align.INLINE)
d.comment(0x9B9E, "Push &FF as timeout", align=Align.INLINE)
d.comment(0x9B9F, "X=0: TX pointer index", align=Align.INLINE)
d.comment(0x9BA1, "Load control byte from TX CB", align=Align.INLINE)
d.label(0x9BA3, "start_pass_tx")

d.comment(0x9BA3, "Write control byte to start TX", align=Align.INLINE)
d.comment(0x9BA5, "Save control byte on stack", align=Align.INLINE)
d.comment(0x9BA6, "Poll ADLC until line idle", align=Align.INLINE)
d.comment(0x9BA9, "Shift result: check bit 6 (success)", align=Align.INLINE)
d.comment(0x9BAA, "Bit 6 clear: transmission complete", align=Align.INLINE)
d.comment(0x9BAC, "Shift result: check bit 5 (fatal)", align=Align.INLINE)
d.comment(0x9BAD, "Non-zero (not fatal): retry", align=Align.INLINE)
d.label(0x9BAF, "done_pass_retries")

d.comment(0x9BAF, "X=0: clear error status", align=Align.INLINE)
d.comment(0x9BB1, "Jump to fix up reply status", align=Align.INLINE)
d.subroutine(
    0x9BB4,
    "poll_econet_data_continue_frame_status",
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
| `&44` | bad control byte |""",
    on_exit={"a": "TX result (&00 success / &40 jammed / &41 not listening / &43 no clock / &44 bad control byte)"},
)


d.comment(0x9BB4, "Shift ws_0d60 left to poll ADLC", align=Align.INLINE)
d.comment(0x9BB7, "Bit not set: keep polling", align=Align.INLINE)
d.comment(0x9BB9, "Copy TX pointer low to NMI TX block", align=Align.INLINE)
d.comment(0x9BBB, "Store in NMI TX block low", align=Align.INLINE)
d.comment(0x9BBD, "Copy TX pointer high", align=Align.INLINE)
d.comment(0x9BBF, "Store in NMI TX block high", align=Align.INLINE)
d.comment(0x9BC1, "Begin Econet frame transmission", align=Align.INLINE)
d.label(0x9BC4, "loop_poll_pass_tx")

d.comment(0x9BC4, "Read TX status byte", align=Align.INLINE)
d.comment(0x9BC6, "Bit 7 set: still transmitting", align=Align.INLINE)
d.comment(0x9BC8, "Return with result in A", align=Align.INLINE)
d.label(0x9BC9, "restore_retry_state")

d.comment(0x9BC9, "Pull control byte", align=Align.INLINE)
d.comment(0x9BCA, "Restore to X", align=Align.INLINE)
d.comment(0x9BCB, "Pull timeout", align=Align.INLINE)
d.comment(0x9BCC, "Restore to Y", align=Align.INLINE)
d.comment(0x9BCD, "Pull retry count", align=Align.INLINE)
d.comment(0x9BCE, "Zero retries: go to error handling", align=Align.INLINE)
d.comment(0x9BD0, "Decrement retry counter", align=Align.INLINE)
d.comment(0x9BD2, "Push updated retry count", align=Align.INLINE)
d.comment(0x9BD3, "Copy timeout to A", align=Align.INLINE)
d.comment(0x9BD4, "Push timeout", align=Align.INLINE)
d.comment(0x9BD5, "Copy control byte to A", align=Align.INLINE)
d.label(0x9BD6, "loop_pass_tx_delay")

d.comment(0x9BD6, "Inner delay loop: decrement X", align=Align.INLINE)
d.comment(0x9BD7, "Loop until X=0", align=Align.INLINE)
d.comment(0x9BD9, "Decrement outer counter Y", align=Align.INLINE)
d.comment(0x9BDA, "Loop until Y=0", align=Align.INLINE)
d.comment(0x9BDC, "ALWAYS branch: retry transmission", align=Align.INLINE)
d.label(0x9BDE, "pass_tx_success")

d.comment(0x9BDE, "Pull control byte (discard)", align=Align.INLINE)
d.comment(0x9BDF, "Pull timeout (discard)", align=Align.INLINE)
d.comment(0x9BE0, "Pull retry count (discard)", align=Align.INLINE)
d.comment(0x9BE1, "Y=0: start restoring from offset 0", align=Align.INLINE)
d.label(0x9BE3, "loop_restore_txbuf")

d.comment(0x9BE3, "Load template byte for this offset", align=Align.INLINE)
d.comment(0x9BE6, "Is it &FD (skip marker)?", align=Align.INLINE)
d.comment(0x9BE8, "Yes: don't restore this offset", align=Align.INLINE)
d.comment(0x9BEA, "Pull original value from stack", align=Align.INLINE)
d.comment(0x9BEB, "Restore original TX buffer byte", align=Align.INLINE)
d.label(0x9BED, "skip_restore_byte")

d.comment(0x9BED, "Next offset (ascending)", align=Align.INLINE)
d.comment(0x9BEE, "Processed all 12 bytes?", align=Align.INLINE)
d.comment(0x9BF0, "No: continue restoring", align=Align.INLINE)
d.comment(0x9BF2, "Return with TX buffer restored", align=Align.INLINE)
d.label(0x9BF3, "load_text_ptr_and_parse")

d.subroutine(
    0x9BF3,
    "load_text_ptr_and_parse",
    title="Copy text pointer from FS options and parse string",
    description="""Reads a 2-byte address from (fs_options)+0/1 into
os_text_ptr (&00F2), resets Y to zero, then falls
through to gsread_to_buf to parse the string at that
address into the &0E30 buffer.""",
    on_exit={"y": "0 (reset before GSINIT)"},
)


d.comment(0x9BF3, "Y=1: start at second byte of pointer", align=Align.INLINE)
d.label(0x9BF5, "loop_copy_text_ptr")

d.comment(0x9BF5, "Load pointer byte from FS options", align=Align.INLINE)
d.comment(0x9BF7, "Store in OS text pointer", align=Align.INLINE)
d.comment(0x9BFA, "Decrement index", align=Align.INLINE)
d.comment(0x9BFB, "Loop until both bytes copied", align=Align.INLINE)
d.comment(0x9BFD, "Y=0: reset index for string reading", align=Align.INLINE)
d.label(0x9BFE, "gsread_to_buf")

d.subroutine(
    0x9BFE,
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


d.comment(0x9BFE, "X=&FF: pre-increment for buffer index", align=Align.INLINE)
d.comment(0x9C00, "C=0: initialise for string input", align=Align.INLINE)
d.comment(0x9C01, "GSINIT: initialise string reading", align=Align.INLINE)
d.comment(0x9C04, "Z set (empty string): store terminator", align=Align.INLINE)
d.label(0x9C06, "loop_gsread_char")

d.comment(0x9C06, "GSREAD: read next character", align=Align.INLINE)
d.comment(0x9C09, "C set: end of string reached", align=Align.INLINE)
d.comment(0x9C0B, "Advance buffer index", align=Align.INLINE)
d.comment(0x9C0C, "Store character in fs_filename_buf buffer", align=Align.INLINE)
d.comment(0x9C0F, "ALWAYS branch: read next character", align=Align.INLINE)
d.label(0x9C11, "terminate_buf")

d.comment(0x9C11, "Advance past last character", align=Align.INLINE)
d.comment(0x9C12, "A=CR: terminate filename", align=Align.INLINE)
d.comment(0x9C14, "Store CR terminator in buffer", align=Align.INLINE)
d.comment(0x9C17, "Parse-buffer pointer (low)", align=Align.INLINE)
d.comment(0x9C19, "Set command text pointer low", align=Align.INLINE)
d.comment(0x9C1B, "Parse-buffer pointer (high)", align=Align.INLINE)
d.comment(0x9C1D, "Set command text pointer high", align=Align.INLINE)
d.comment(0x9C1F, "Return with buffer filled", align=Align.INLINE)
d.subroutine(
    0x9C20,
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


d.entry(0x9C20)
d.comment(0x9C20, "Set up transfer parameters", align=Align.INLINE)
d.comment(0x9C23, "Load text pointer and parse filename", align=Align.INLINE)
d.comment(0x9C26, "Set owner-only access mask", align=Align.INLINE)
d.comment(0x9C29, "Parse access prefix from filename", align=Align.INLINE)
d.comment(0x9C2C, "Load last byte flag", align=Align.INLINE)
d.comment(0x9C2E, "Positive (not last): display file info", align=Align.INLINE)
d.comment(0x9C30, "Is it &FF (last entry)?", align=Align.INLINE)
d.comment(0x9C32, "Yes: copy arg and iterate", align=Align.INLINE)
d.comment(0x9C34, "Other value: return with flag", align=Align.INLINE)
d.label(0x9C37, "copy_arg_and_enum")

d.comment(0x9C37, "Copy argument to buffer at X=0", align=Align.INLINE)
d.comment(0x9C3A, "Y=2: enumerate directory command", align=Align.INLINE)
d.label(0x9C3C, "do_fs_cmd_iteration")

d.subroutine(
    0x9C3C,
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


d.comment(0x9C3C, "A=&92: FS port number", align=Align.INLINE)
d.comment(0x9C3E, "Set escapable flag to &92", align=Align.INLINE)
d.comment(0x9C40, "Store port number in TX buffer", align=Align.INLINE)
d.comment(0x9C43, "Send request to file server", align=Align.INLINE)
d.comment(0x9C46, "Y=6: offset to response cycle flag", align=Align.INLINE)
d.comment(0x9C48, "Load cycle flag from FS options", align=Align.INLINE)
d.comment(0x9C4A, "Non-zero: already initialised", align=Align.INLINE)
d.comment(0x9C4C, "Copy FS options to zero page first", align=Align.INLINE)
d.comment(0x9C4F, "Then copy workspace to FS options", align=Align.INLINE)
d.comment(0x9C52, "Branch to continue (C clear from JSR)", align=Align.INLINE)
d.label(0x9C54, "copy_ws_then_fsopts")

d.comment(0x9C54, "Copy workspace to FS options first", align=Align.INLINE)
d.comment(0x9C57, "Then copy FS options to zero page", align=Align.INLINE)
d.label(0x9C5A, "setup_txcb_addrs")

d.comment(0x9C5A, "Y=4: loop counter", align=Align.INLINE)
d.label(0x9C5C, "loop_copy_addrs")

d.comment(0x9C5C, "Load address byte from zero page", align=Align.INLINE)
d.comment(0x9C5E, "Save to TXCB end pointer", align=Align.INLINE)
d.comment(0x9C60, "Add offset from buffer", align=Align.INLINE)
d.comment(0x9C63, "Store sum in fs_work area", align=Align.INLINE)
d.comment(0x9C65, "Advance to next byte", align=Align.INLINE)
d.comment(0x9C66, "Decrement counter", align=Align.INLINE)
d.comment(0x9C67, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9C69, "Set carry for subtraction", align=Align.INLINE)
d.comment(0x9C6A, "Subtract high offset", align=Align.INLINE)
d.comment(0x9C6D, "Store result in fs_work_7", align=Align.INLINE)
d.comment(0x9C6F, "Format filename for display", align=Align.INLINE)
d.comment(0x9C72, "Send TXCB and swap addresses", align=Align.INLINE)
d.comment(0x9C75, "X=2: copy 3 offset bytes", align=Align.INLINE)
d.label(0x9C77, "loop_copy_offsets")

d.comment(0x9C77, "Load offset byte from fs_file_len_3", align=Align.INLINE)
d.comment(0x9C7A, "Store in fs_cmd_data for next iteration", align=Align.INLINE)
d.comment(0x9C7D, "Decrement counter", align=Align.INLINE)
d.comment(0x9C7E, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x9C80, "Jump to receive and process reply", align=Align.INLINE)
d.label(0x9C83, "send_txcb_swap_addrs")

d.subroutine(
    0x9C83,
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


d.comment(0x9C83, "Compare 5-byte handle with current", align=Align.INLINE)
d.comment(0x9C86, "Match: no need to send, return", align=Align.INLINE)
d.comment(0x9C88, "A=&92: FS reply port number", align=Align.INLINE)
d.comment(0x9C8A, "Set TXCB port", align=Align.INLINE)
d.label(0x9C8C, "loop_swap_and_send")

d.comment(0x9C8C, "X=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9C8E, "loop_copy_start_end")

d.comment(0x9C8E, "Load TXCB end pointer byte", align=Align.INLINE)
d.comment(0x9C90, "Store in TXCB start pointer", align=Align.INLINE)
d.comment(0x9C92, "Load new end address from fs_work", align=Align.INLINE)
d.comment(0x9C94, "Store in TXCB end pointer", align=Align.INLINE)
d.comment(0x9C96, "Decrement counter", align=Align.INLINE)
d.comment(0x9C97, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9C99, "A=&7F: control byte for data transfer", align=Align.INLINE)
d.comment(0x9C9B, "Set TXCB control byte", align=Align.INLINE)
d.comment(0x9C9D, "Wait for network TX acknowledgement", align=Align.INLINE)
d.comment(0x9CA0, "Y=3: compare 4 bytes", align=Align.INLINE)
d.label(0x9CA2, "loop_verify_addrs")

d.comment(0x9CA2, "Load TXCB end byte", align=Align.INLINE)
d.comment(0x9CA5, "Compare with expected end address", align=Align.INLINE)
d.comment(0x9CA8, "Mismatch: resend from start", align=Align.INLINE)
d.comment(0x9CAA, "Decrement counter", align=Align.INLINE)
d.comment(0x9CAB, "Loop until all 4 bytes match", align=Align.INLINE)
d.label(0x9CAD, "rts_txcb_swap")

d.comment(0x9CAD, "Return (all bytes match)", align=Align.INLINE)
d.label(0x9CAE, "check_display_type")

d.comment(0x9CAE, "Z set: directory entry display", align=Align.INLINE)
d.comment(0x9CB0, "Non-zero: jump to OSWORD dispatch", align=Align.INLINE)
d.label(0x9CB3, "setup_dir_display")

d.subroutine(
    0x9CB3,
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


d.comment(0x9CB3, "X=4: loop counter for 4 iterations", align=Align.INLINE)
d.comment(0x9CB5, "Y=&0E: FS options offset for addresses", align=Align.INLINE)
d.comment(0x9CB7, "Set carry for subtraction", align=Align.INLINE)
d.label(0x9CB8, "loop_compute_diffs")

d.comment(0x9CB8, "Load address byte from FS options", align=Align.INLINE)
d.comment(0x9CBA, "Save to workspace (port_ws_offset)", align=Align.INLINE)
d.comment(0x9CBD, "Y -= 4 to point to paired offset", align=Align.INLINE)
d.comment(0x9CC0, "Subtract paired value", align=Align.INLINE)
d.comment(0x9CC2, "Store difference in fs_cmd_csd buffer", align=Align.INLINE)
d.comment(0x9CC5, "Push difference", align=Align.INLINE)
d.comment(0x9CC6, "Load paired value from FS options", align=Align.INLINE)
d.comment(0x9CC8, "Save to workspace", align=Align.INLINE)
d.comment(0x9CCB, "Pull difference back", align=Align.INLINE)
d.comment(0x9CCC, "Store in FS options for display", align=Align.INLINE)
d.comment(0x9CCE, "Advance Y by 5 for next field", align=Align.INLINE)
d.comment(0x9CD1, "Decrement loop counter", align=Align.INLINE)
d.comment(0x9CD2, "Loop for all 4 address pairs", align=Align.INLINE)
d.comment(0x9CD4, "Y=9: copy 9 bytes of options data", align=Align.INLINE)
d.label(0x9CD6, "loop_copy_fs_options")

d.comment(0x9CD6, "Load FS options byte", align=Align.INLINE)
d.comment(0x9CD8, "Store in fs_cmd_csd buffer", align=Align.INLINE)
d.comment(0x9CDB, "Decrement index", align=Align.INLINE)
d.comment(0x9CDC, "Loop until all 9 bytes copied", align=Align.INLINE)
d.comment(0x9CDE, "A=&91: FS port for info request", align=Align.INLINE)
d.comment(0x9CE0, "Set escapable flag", align=Align.INLINE)
d.comment(0x9CE2, "Store port in TX buffer", align=Align.INLINE)
d.comment(0x9CE5, "Store in fs_error_ptr", align=Align.INLINE)
d.comment(0x9CE7, "X=&0B: copy argument at offset 11", align=Align.INLINE)
d.comment(0x9CE9, "Copy argument to TX buffer", align=Align.INLINE)
d.comment(0x9CEC, "Y=1: info sub-command", align=Align.INLINE)
d.comment(0x9CEE, "Load last byte flag", align=Align.INLINE)
d.comment(0x9CF0, "Is it 7 (catalogue info)?", align=Align.INLINE)
d.comment(0x9CF2, "Save comparison result", align=Align.INLINE)
d.comment(0x9CF3, "Not 7: keep Y=1", align=Align.INLINE)
d.comment(0x9CF5, "Y=&1D: extended info command", align=Align.INLINE)
d.label(0x9CF7, "send_info_request")

d.comment(0x9CF7, "Send request to file server", align=Align.INLINE)
d.comment(0x9CFA, "Format filename for display", align=Align.INLINE)
d.comment(0x9CFD, "Restore comparison flags", align=Align.INLINE)
d.comment(0x9CFE, "Not catalogue info: show short format", align=Align.INLINE)
d.comment(0x9D00, "X=0: start at first byte", align=Align.INLINE)
d.comment(0x9D02, "ALWAYS branch to store and display", align=Align.INLINE)
d.label(0x9D04, "setup_txcb_transfer")

d.comment(0x9D04, "Load file handle from fs_cmd_data", align=Align.INLINE)
d.comment(0x9D07, "Check and set up TXCB for transfer", align=Align.INLINE)
d.label(0x9D0A, "recv_reply")

d.subroutine(
    0x9D0A,
    "recv_reply",
    title="Receive FS reply and stash result byte",
    description="""JSRs recv_and_process_reply, then falls through to store_result
(STX hazel_txcb_result; LDY #&0E to point at the protection-bits offset).
Single caller (the dispatch at &9C80).""",
    on_exit={"x": "FS result byte (also written to hazel_txcb_result)", "y": "&0E (FS options offset for protection)"},
)


d.comment(0x9D0A, "Receive and process reply", align=Align.INLINE)
d.label(0x9D0D, "store_result")

d.comment(0x9D0D, "Store result byte in fs_reply_cmd", align=Align.INLINE)
d.comment(0x9D10, "Y=&0E: protection bits offset", align=Align.INLINE)
d.comment(0x9D12, "Load access byte from fs_cmd_data", align=Align.INLINE)
d.comment(0x9D15, "Extract protection bit flags", align=Align.INLINE)
d.comment(0x9D18, "Zero: use reply buffer data", align=Align.INLINE)
d.label(0x9D1A, "loop_copy_file_info")

d.comment(0x9D1A, "Load file info byte from fs_reply_data", align=Align.INLINE)
d.label(0x9D1D, "store_prot_byte")

d.comment(0x9D1D, "Store in FS options at offset Y", align=Align.INLINE)
d.comment(0x9D1F, "Advance to next byte", align=Align.INLINE)
d.comment(0x9D20, "Y=&12: end of protection fields?", align=Align.INLINE)
d.comment(0x9D22, "No: copy next byte", align=Align.INLINE)
d.comment(0x9D24, "Load display flag from fs_messages_flag", align=Align.INLINE)
d.comment(0x9D27, "Zero: skip display, return", align=Align.INLINE)
d.comment(0x9D29, "Y=&F4: index into hazel_display_buf for filename", align=Align.INLINE)
d.label(0x9D2B, "loop_print_filename")

d.comment(0x9D2B, "Load filename character from filename_buf", align=Align.INLINE)
d.comment(0x9D2E, "Print character via OSASCI", align=Align.INLINE)
d.comment(0x9D31, "Advance to next character", align=Align.INLINE)
d.comment(0x9D32, "Printed all 12 characters?", align=Align.INLINE)
d.comment(0x9D34, "Y=5: offset for access string", align=Align.INLINE)
d.comment(0x9D36, "Print 5 hex bytes (access info)", align=Align.INLINE)
d.comment(0x9D39, "Print load and exec addresses", align=Align.INLINE)
d.comment(0x9D3C, "Print newline", align=Align.INLINE)
d.comment(0x9D3F, "Jump to return with last flag", align=Align.INLINE)
d.label(0x9D42, "print_load_exec_addrs")

d.subroutine(
    0x9D42,
    "print_load_exec_addrs",
    title="Print exec address and file length in hex",
    description="""Prints the exec address as 5 hex bytes from
(fs_options) offset 9 downwards, then the file
length as 3 hex bytes from offset &0C. Each group
is followed by a space separator via OSASCI.""",
    on_exit={"a, x, y": "clobbered (print_hex_byte + OSASCI)"},
)


d.comment(0x9D42, "Y=9: offset for exec address", align=Align.INLINE)
d.comment(0x9D44, "Print 5 hex bytes (exec address)", align=Align.INLINE)
d.comment(0x9D47, "Y=&0C: offset for length (3 bytes)", align=Align.INLINE)
d.comment(0x9D49, "X=3: print 3 bytes only", align=Align.INLINE)
d.comment(0x9D4B, "ALWAYS branch to print routine", align=Align.INLINE)
d.label(0x9D4D, "print_5_hex_bytes")

d.subroutine(
    0x9D4D,
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


d.comment(0x9D4D, "X=4: print 5 bytes (4 to 0)", align=Align.INLINE)
d.label(0x9D4F, "loop_print_hex_byte")

d.comment(0x9D4F, "Load byte from FS options at offset Y", align=Align.INLINE)
d.comment(0x9D51, "Print as 2-digit hex", align=Align.INLINE)
d.comment(0x9D54, "Decrement byte offset", align=Align.INLINE)
d.comment(0x9D55, "Decrement byte count", align=Align.INLINE)
d.comment(0x9D56, "Loop until all bytes printed", align=Align.INLINE)
d.comment(0x9D58, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9D5A, "Print space via OSASCI and return", align=Align.INLINE)
d.label(0x9D5D, "copy_fsopts_to_zp")

d.subroutine(
    0x9D5D,
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


d.comment(0x9D5D, "Y=5: copy 4 bytes (offsets 2-5)", align=Align.INLINE)
d.label(0x9D5F, "loop_copy_fsopts_byte")

d.comment(0x9D5F, "Load byte from FS options", align=Align.INLINE)
d.comment(0x9D61, "Store in zero page at work_ae+Y", align=Align.INLINE)
d.comment(0x9D64, "Decrement index", align=Align.INLINE)
d.comment(0x9D65, "Below offset 2?", align=Align.INLINE)
d.comment(0x9D67, "No: copy next byte", align=Align.INLINE)
d.label(0x9D69, "skip_one_and_advance5")

d.subroutine(
    0x9D69,
    "skip_one_and_advance5",
    title="Advance Y by 5",
    description="""Entry point one INY before advance_y_by_4, giving
a total Y increment of 5. Used to skip past a
5-byte address/length structure in the FS options
block.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset + 5", "a, x": "preserved"},
)


d.comment(0x9D69, "Y += 5", align=Align.INLINE)
d.label(0x9D6A, "advance_y_by_4")

d.subroutine(
    0x9D6A,
    "advance_y_by_4",
    title="Advance Y by 4",
    description="""Four consecutive INY instructions. Used as a
subroutine to step Y past a 4-byte address field
in the FS options or workspace structure.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset + 4"},
)


d.comment(0x9D6A, "Y += 4", align=Align.INLINE)
d.comment(0x9D6B, "(continued)", align=Align.INLINE)
d.comment(0x9D6C, "(continued)", align=Align.INLINE)
d.comment(0x9D6D, "(continued)", align=Align.INLINE)
d.label(0x9D6E, "rts_advance_y")

d.comment(0x9D6E, "Return", align=Align.INLINE)
d.label(0x9D6F, "copy_workspace_to_fsopts")

d.subroutine(
    0x9D6F,
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


d.comment(0x9D6F, "Y=&0D: copy bytes from offset &0D down", align=Align.INLINE)
d.comment(0x9D71, "Transfer X to A", align=Align.INLINE)
d.label(0x9D72, "loop_copy_ws_byte")

d.comment(0x9D72, "Store byte in FS options at offset Y", align=Align.INLINE)
d.comment(0x9D74, "Load next workspace byte from fs_cmd_urd+Y", align=Align.INLINE)
d.comment(0x9D77, "Decrement index", align=Align.INLINE)
d.comment(0x9D78, "Below offset 2?", align=Align.INLINE)
d.comment(0x9D7A, "No: copy next byte", align=Align.INLINE)
d.label(0x9D7C, "retreat_y_by_4")

d.subroutine(
    0x9D7C,
    "retreat_y_by_4",
    title="Retreat Y by 4",
    description="""Four consecutive DEY instructions. Companion to
advance_y_by_4 for reverse traversal of address
structures.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 4"},
)


d.comment(0x9D7C, "Y -= 4", align=Align.INLINE)
d.label(0x9D7D, "retreat_y_by_3")

d.subroutine(
    0x9D7D,
    "retreat_y_by_3",
    title="Retreat Y by 3",
    description="""Three consecutive DEY instructions. Used by
setup_transfer_workspace to step back through
interleaved address pairs in the FS options block.""",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 3"},
)


d.comment(0x9D7D, "Y -= 3", align=Align.INLINE)
d.comment(0x9D7E, "(continued)", align=Align.INLINE)
d.comment(0x9D7F, "(continued)", align=Align.INLINE)
d.comment(0x9D80, "Return", align=Align.INLINE)
d.label(0x9D81, "discard_handle_match")

d.comment(0x9D81, "Discard stacked value", align=Align.INLINE)
d.comment(0x9D82, "Restore Y from fs_block_offset", align=Align.INLINE)
d.comment(0x9D84, "Return (handle already matches)", align=Align.INLINE)
d.label(0x9D85, "check_and_setup_txcb")

d.subroutine(
    0x9D85,
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


d.comment(0x9D85, "Save port/sub-function on stack", align=Align.INLINE)
d.comment(0x9D86, "Compare 5-byte handle with current", align=Align.INLINE)
d.comment(0x9D89, "Match: discard port and return", align=Align.INLINE)
d.label(0x9D8B, "init_transfer_addrs")

d.comment(0x9D8B, "X=0: loop start", align=Align.INLINE)
d.comment(0x9D8D, "Y=4: copy 4 bytes", align=Align.INLINE)
d.comment(0x9D8F, "Clear fs_reply_cmd (transfer size low)", align=Align.INLINE)
d.comment(0x9D92, "Clear fs_load_vector (transfer size high)", align=Align.INLINE)
d.comment(0x9D95, "Clear carry for addition", align=Align.INLINE)
d.label(0x9D96, "loop_copy_addr_offset")

d.comment(0x9D96, "Load address byte from zero page", align=Align.INLINE)
d.comment(0x9D98, "Store in TXCB start pointer", align=Align.INLINE)
d.comment(0x9D9A, "Add offset from fs_func_code", align=Align.INLINE)
d.comment(0x9D9D, "Store sum in TXCB end pointer", align=Align.INLINE)
d.comment(0x9D9F, "Also update load address", align=Align.INLINE)
d.comment(0x9DA1, "Advance to next byte", align=Align.INLINE)
d.comment(0x9DA2, "Decrement counter", align=Align.INLINE)
d.comment(0x9DA3, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9DA5, "Carry set: overflow, use limit", align=Align.INLINE)
d.comment(0x9DA7, "Set carry for subtraction", align=Align.INLINE)
d.label(0x9DA8, "loop_check_vs_limit")

d.comment(0x9DA8, "Load computed end address", align=Align.INLINE)
d.comment(0x9DAB, "Subtract maximum from fs_work_4", align=Align.INLINE)
d.comment(0x9DAE, "Advance to next byte", align=Align.INLINE)
d.comment(0x9DAF, "Decrement counter", align=Align.INLINE)
d.comment(0x9DB0, "Loop for all bytes", align=Align.INLINE)
d.comment(0x9DB2, "Below limit: keep computed end", align=Align.INLINE)
d.label(0x9DB4, "clamp_end_to_limit")

d.comment(0x9DB4, "X=3: copy 4 bytes of limit", align=Align.INLINE)
d.label(0x9DB6, "loop_copy_limit")

d.comment(0x9DB6, "Load limit from fs_work_4", align=Align.INLINE)
d.comment(0x9DB8, "Store as TXCB end", align=Align.INLINE)
d.comment(0x9DBA, "Decrement counter", align=Align.INLINE)
d.comment(0x9DBB, "Loop for all 4 bytes", align=Align.INLINE)
d.label(0x9DBD, "set_port_and_ctrl")

d.comment(0x9DBD, "Pull port from stack", align=Align.INLINE)
d.comment(0x9DBE, "Push back (keep for later)", align=Align.INLINE)
d.comment(0x9DBF, "Save flags (carry = overflow state)", align=Align.INLINE)
d.comment(0x9DC0, "Set TXCB port number", align=Align.INLINE)
d.comment(0x9DC2, "A=&80: control byte for data request", align=Align.INLINE)
d.comment(0x9DC4, "Set TXCB control byte", align=Align.INLINE)
d.comment(0x9DC6, "Init TX pointer and send packet", align=Align.INLINE)
d.comment(0x9DC9, "Load error pointer", align=Align.INLINE)
d.comment(0x9DCB, "Init TXCB port from error pointer", align=Align.INLINE)
d.comment(0x9DCE, "Restore overflow flags", align=Align.INLINE)
d.comment(0x9DCF, "Carry set: discard and return", align=Align.INLINE)
d.comment(0x9DD1, "A=&91: FS reply port", align=Align.INLINE)
d.comment(0x9DD3, "Set TXCB port for reply", align=Align.INLINE)
d.comment(0x9DD5, "Wait for TX acknowledgement", align=Align.INLINE)
d.comment(0x9DD8, "Non-zero (not done): retry send", align=Align.INLINE)
d.label(0x9DDA, "dispatch_osword_op")

d.subroutine(
    0x9DDA,
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


d.comment(0x9DDA, "Store sub-operation code", align=Align.INLINE)
d.comment(0x9DDD, "Compare with 7", align=Align.INLINE)
d.comment(0x9DDF, "Below 7: handle operations 1-6", align=Align.INLINE)
d.comment(0x9DE1, "Above 7: jump to handle via finalise", align=Align.INLINE)
d.comment(0x9DE3, "Equal to 7: jump to directory display", align=Align.INLINE)
d.label(0x9DE6, "dispatch_ops_1_to_6")

d.comment(0x9DE6, "Compare with 6", align=Align.INLINE)
d.comment(0x9DE8, "6: delete file operation", align=Align.INLINE)
d.comment(0x9DEA, "Compare with 5", align=Align.INLINE)
d.comment(0x9DEC, "5: read catalogue info", align=Align.INLINE)
d.comment(0x9DEE, "Compare with 4", align=Align.INLINE)
d.comment(0x9DF0, "4: write file attributes", align=Align.INLINE)
d.comment(0x9DF2, "Compare with 1", align=Align.INLINE)
d.comment(0x9DF4, "1: read file info", align=Align.INLINE)
d.comment(0x9DF6, "Shift left twice: A*4", align=Align.INLINE)
d.comment(0x9DF7, "A*4", align=Align.INLINE)
d.comment(0x9DF8, "Copy to Y as index", align=Align.INLINE)
d.comment(0x9DF9, "Y -= 3 to get FS options offset", align=Align.INLINE)
d.comment(0x9DFC, "X=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9DFE, "loop_copy_fsopts_4")

d.comment(0x9DFE, "Load byte from FS options at offset Y", align=Align.INLINE)
d.comment(0x9E00, "Store in fs_func_code buffer", align=Align.INLINE)
d.comment(0x9E03, "Decrement source offset", align=Align.INLINE)
d.comment(0x9E04, "Decrement byte count", align=Align.INLINE)
d.comment(0x9E05, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9E07, "X=5: copy arg to buffer at offset 5", align=Align.INLINE)
d.comment(0x9E09, "ALWAYS branch to copy and send", align=Align.INLINE)
d.label(0x9E0B, "setup_save_access")

d.comment(0x9E0B, "Get access bits for file", align=Align.INLINE)
d.comment(0x9E0E, "Store access byte in fs_file_attrs", align=Align.INLINE)
d.comment(0x9E11, "Y=9: source offset in FS options", align=Align.INLINE)
d.comment(0x9E13, "X=8: copy 8 bytes to buffer", align=Align.INLINE)
d.label(0x9E15, "loop_copy_fsopts_8")

d.comment(0x9E15, "Load FS options byte", align=Align.INLINE)
d.comment(0x9E17, "Store in fs_cmd_data buffer", align=Align.INLINE)
d.comment(0x9E1A, "Decrement source offset", align=Align.INLINE)
d.comment(0x9E1B, "Decrement byte count", align=Align.INLINE)
d.comment(0x9E1C, "Loop for all 8 bytes", align=Align.INLINE)
d.comment(0x9E1E, "X=&0A: buffer offset for argument", align=Align.INLINE)
d.label(0x9E20, "send_save_or_access")

d.comment(0x9E20, "Copy argument to buffer", align=Align.INLINE)
d.comment(0x9E23, "Y=&13: OSWORD &13 (NFS operation)", align=Align.INLINE)
d.comment(0x9E25, "ALWAYS branch to send request", align=Align.INLINE)
d.label(0x9E27, "send_delete_request")

d.comment(0x9E27, "Copy argument to buffer at X=0", align=Align.INLINE)
d.comment(0x9E2A, "Y=&14: delete file command", align=Align.INLINE)
d.label(0x9E2C, "send_request_vset")

d.comment(0x9E2C, "Set V flag (no directory check)", align=Align.INLINE)
d.comment(0x9E2F, "Send request with V set", align=Align.INLINE)
d.label(0x9E32, "skip_if_error")

d.comment(0x9E32, "Carry set: error, jump to finalise", align=Align.INLINE)
d.comment(0x9E34, "No error: return with last flag", align=Align.INLINE)
d.label(0x9E37, "setup_write_access")

d.comment(0x9E37, "Get access bits for file", align=Align.INLINE)
d.comment(0x9E3A, "Store in fs_func_code", align=Align.INLINE)
d.comment(0x9E3D, "X=2: buffer offset", align=Align.INLINE)
d.comment(0x9E3F, "ALWAYS branch to copy and send", align=Align.INLINE)
d.label(0x9E41, "read_cat_info")

d.comment(0x9E41, "X=1: buffer offset", align=Align.INLINE)
d.comment(0x9E43, "Copy argument to buffer", align=Align.INLINE)
d.comment(0x9E46, "Y=&12: open file command", align=Align.INLINE)
d.comment(0x9E48, "Send open file request", align=Align.INLINE)
d.comment(0x9E4B, "Load reply handle from fs_obj_type", align=Align.INLINE)
d.comment(0x9E4E, "Clear fs_obj_type", align=Align.INLINE)
d.comment(0x9E51, "Clear fs_len_clear", align=Align.INLINE)
d.comment(0x9E54, "Get protection bits", align=Align.INLINE)
d.comment(0x9E57, "Load file handle from fs_cmd_data", align=Align.INLINE)
d.comment(0x9E5A, "Zero: file not found, return", align=Align.INLINE)
d.comment(0x9E5C, "Y=&0E: store access bits", align=Align.INLINE)
d.comment(0x9E5E, "Store access byte in FS options", align=Align.INLINE)
d.comment(0x9E60, "Y=&0D", align=Align.INLINE)
d.comment(0x9E61, "X=&0C: copy 12 bytes of file info", align=Align.INLINE)
d.label(0x9E63, "loop_copy_cat_info")

d.comment(0x9E63, "Load reply byte from fs_cmd_data+X", align=Align.INLINE)
d.comment(0x9E66, "Store in FS options at offset Y", align=Align.INLINE)
d.comment(0x9E68, "Decrement destination offset", align=Align.INLINE)
d.comment(0x9E69, "Decrement source counter", align=Align.INLINE)
d.comment(0x9E6A, "Loop for all 12 bytes", align=Align.INLINE)
d.comment(0x9E6C, "X=1 (INX from 0)", align=Align.INLINE)
d.comment(0x9E6D, "X=2", align=Align.INLINE)
d.comment(0x9E6E, "Y=&11: FS options offset", align=Align.INLINE)
d.label(0x9E70, "loop_copy_ext_info")

d.comment(0x9E70, "Load extended info byte from fs_access_level", align=Align.INLINE)
d.comment(0x9E73, "Store in FS options", align=Align.INLINE)
d.comment(0x9E75, "Decrement destination offset", align=Align.INLINE)
d.comment(0x9E76, "Decrement source counter", align=Align.INLINE)
d.comment(0x9E77, "Loop until all copied", align=Align.INLINE)
d.comment(0x9E79, "Reload file handle", align=Align.INLINE)
d.label(0x9E7C, "return_with_handle")

d.comment(0x9E7C, "Transfer to A", align=Align.INLINE)
d.label(0x9E7D, "done_osword_op")

d.entry(0x9E7D)
d.comment(0x9E7D, "Jump to finalise and return", align=Align.INLINE)
d.label(0x9E80, "format_filename_field")

d.subroutine(
    0x9E80,
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


d.comment(0x9E80, "Y=0: start writing at filename_buf[0]", align=Align.INLINE)
d.comment(0x9E82, "Load source offset from fs_cmd_csd", align=Align.INLINE)
d.comment(0x9E85, "Non-zero: copy from fs_cmd_data buffer", align=Align.INLINE)
d.label(0x9E87, "loop_copy_cmdline_char")

d.comment(0x9E87, "Load character from command line", align=Align.INLINE)
d.comment(0x9E89, "Below '!' (control/space)?", align=Align.INLINE)
d.comment(0x9E8B, "Yes: pad with spaces", align=Align.INLINE)
d.comment(0x9E8D, "Store printable character in filename_buf", align=Align.INLINE)
d.comment(0x9E90, "Advance to next character", align=Align.INLINE)
d.comment(0x9E91, "Loop for more characters", align=Align.INLINE)
d.label(0x9E93, "pad_with_spaces")

d.comment(0x9E93, "A=' ': space for padding", align=Align.INLINE)
d.comment(0x9E95, "Store space in display buffer", align=Align.INLINE)
d.comment(0x9E98, "Advance index", align=Align.INLINE)
d.comment(0x9E99, "Filled all 12 characters?", align=Align.INLINE)
d.comment(0x9E9B, "No: pad more spaces", align=Align.INLINE)
d.comment(0x9E9D, "Return with field formatted", align=Align.INLINE)
d.label(0x9E9E, "loop_copy_buf_char")

d.comment(0x9E9E, "Advance source and destination", align=Align.INLINE)
d.label(0x9EA0, "copy_from_buf_entry")

d.comment(0x9EA0, "Load byte from fs_cmd_data buffer", align=Align.INLINE)
d.comment(0x9EA3, "Store in filename_buf", align=Align.INLINE)
d.comment(0x9EA6, "Bit 7 clear: more characters", align=Align.INLINE)
d.comment(0x9EA8, "Return (bit 7 set = terminator)", align=Align.INLINE)
d.subroutine(
    0x9EA9,
    "argsv_handler",
    title="ARGSV vector handler: OSARGS",
    description="""Reached via the ARGSV vector at `&0214`. Verifies the FS workspace
checksum, stores the result as the last-byte flag, and sets the FS
options pointer. Routes by `A`: positive (`bit 7 clear`) dispatches
to a sub-operation table; bit 6 vs bit 5 of `A` then selects
between read-and-write paths via further branching.""",
    on_entry={"a": "OSARGS function code", "x": "control-block low byte", "y": "channel handle"},
)


d.entry(0x9EA9)
d.comment(0x9EA9, "Verify workspace checksum", align=Align.INLINE)
d.comment(0x9EAC, "Store result as last byte flag", align=Align.INLINE)
d.comment(0x9EAE, "Set FS options pointer", align=Align.INLINE)
d.comment(0x9EB1, "OR with 0 to set flags", align=Align.INLINE)
d.comment(0x9EB3, "Positive: handle sub-operations", align=Align.INLINE)
d.comment(0x9EB5, "Shift left to check bit 6", align=Align.INLINE)
d.comment(0x9EB6, "Zero (was &80): close channel", align=Align.INLINE)
d.comment(0x9EB8, "Other: process all FCBs first", align=Align.INLINE)
d.label(0x9EBB, "validate_chan_close")

d.comment(0x9EBB, "Transfer Y to A", align=Align.INLINE)
d.comment(0x9EBC, "Compare with &20 (space)", align=Align.INLINE)
d.comment(0x9EBE, "Above &20: check further", align=Align.INLINE)
d.label(0x9EC0, "error_invalid_chan")

d.comment(0x9EC0, "Below &20: invalid channel char", align=Align.INLINE)
d.label(0x9EC3, "check_chan_range")

d.comment(0x9EC3, "Compare with '0'", align=Align.INLINE)
d.comment(0x9EC5, "Above '0': invalid channel char", align=Align.INLINE)
d.comment(0x9EC7, "Process all matching FCBs", align=Align.INLINE)
d.comment(0x9ECA, "Transfer Y to A (FCB index)", align=Align.INLINE)
d.comment(0x9ECB, "Push FCB index", align=Align.INLINE)
d.comment(0x9ECC, "Copy to X", align=Align.INLINE)
d.comment(0x9ECD, "Y=0: clear counter", align=Align.INLINE)
d.comment(0x9ECF, "Clear last byte flag", align=Align.INLINE)
d.comment(0x9ED1, "Clear block offset", align=Align.INLINE)
d.label(0x9ED3, "loop_copy_fcb_fields")

d.comment(0x9ED3, "Load channel data from fcb_attr_or_count_mid+X", align=Align.INLINE)
d.comment(0x9ED6, "Store in FS options at Y", align=Align.INLINE)
d.comment(0x9ED8, "Advance X by 8 (next FCB field)", align=Align.INLINE)
d.comment(0x9EDB, "Advance destination index", align=Align.INLINE)
d.comment(0x9EDC, "Copied all 4 channel fields?", align=Align.INLINE)
d.comment(0x9EDE, "No: copy next field", align=Align.INLINE)
d.comment(0x9EE0, "Pull saved FCB index", align=Align.INLINE)
d.comment(0x9EE1, "Restore to fs_block_offset", align=Align.INLINE)
d.label(0x9EE3, "dispatch_osfind_op")

d.comment(0x9EE3, "Compare with 5", align=Align.INLINE)
d.comment(0x9EE5, "5 or above: return with last flag", align=Align.INLINE)
d.comment(0x9EE7, "Compare Y with 0", align=Align.INLINE)
d.comment(0x9EE9, "Non-zero: handle OSFIND with channel", align=Align.INLINE)
d.comment(0x9EEB, "Y=0 (close): jump to OSFIND open", align=Align.INLINE)
d.label(0x9EEE, "osfind_with_channel")

d.comment(0x9EEE, "Push sub-function", align=Align.INLINE)
# UNMAPPED: d.comment(0x9EF1, "Transfer X to A", align=Align.INLINE)
# UNMAPPED: d.comment(0x9EF2, "Push X (FCB slot)", align=Align.INLINE)
d.comment(0x9EF0, "Transfer Y to A", align=Align.INLINE)
d.comment(0x9EF1, "Push Y (channel char)", align=Align.INLINE)
d.comment(0x9EF2, "Check file is not a directory", align=Align.INLINE)
d.comment(0x9EF5, "Pull channel char", align=Align.INLINE)
d.comment(0x9EF6, "Store channel char as receive attribute", align=Align.INLINE)
d.comment(0x9EF9, "Load FCB flag byte from fcb_net_or_port", align=Align.INLINE)
d.comment(0x9EFC, "Store in fs_cmd_data", align=Align.INLINE)
# UNMAPPED: d.comment(0x9F02, "Pull X (FCB slot)", align=Align.INLINE)
# UNMAPPED: d.comment(0x9F03, "Restore X", align=Align.INLINE)
d.comment(0x9F00, "Pull sub-function", align=Align.INLINE)
d.comment(0x9F01, "Shift right: check bit 0", align=Align.INLINE)
d.comment(0x9F02, "Zero (OSFIND close): handle close", align=Align.INLINE)
d.comment(0x9F04, "Save flags (carry from LSR)", align=Align.INLINE)
d.comment(0x9F05, "Push sub-function", align=Align.INLINE)
d.comment(0x9F06, "Load FS options pointer low", align=Align.INLINE)
d.comment(0x9F08, "Load block offset", align=Align.INLINE)
d.comment(0x9F0A, "Process all matching FCBs", align=Align.INLINE)
d.comment(0x9F0D, "Load updated data from fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0x9F10, "Store in fs_cmd_data", align=Align.INLINE)
d.comment(0x9F13, "Pull sub-function", align=Align.INLINE)
d.comment(0x9F14, "Store in fs_func_code", align=Align.INLINE)
d.comment(0x9F17, "Restore flags", align=Align.INLINE)
d.comment(0x9F18, "Transfer Y to A", align=Align.INLINE)
d.comment(0x9F19, "Push Y (offset)", align=Align.INLINE)
d.comment(0x9F1A, "Carry clear: read operation", align=Align.INLINE)
d.comment(0x9F1C, "Y=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9F1E, "loop_copy_zp_to_buf")

d.comment(0x9F1E, "Load zero page data", align=Align.INLINE)
d.comment(0x9F20, "Store in fs_data_count buffer", align=Align.INLINE)
d.comment(0x9F23, "Decrement source", align=Align.INLINE)
d.comment(0x9F24, "Decrement counter", align=Align.INLINE)
d.comment(0x9F25, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9F27, "Y=&0D: TX buffer size", align=Align.INLINE)
d.comment(0x9F29, "X=5: argument offset", align=Align.INLINE)
d.comment(0x9F2B, "Send TX control block to server", align=Align.INLINE)
d.comment(0x9F2E, "Store X in last byte flag", align=Align.INLINE)
d.comment(0x9F30, "Pull saved offset", align=Align.INLINE)
d.comment(0x9F31, "Set connection active flag", align=Align.INLINE)
d.label(0x9F34, "done_return_flag")

d.comment(0x9F34, "Return with last flag", align=Align.INLINE)
d.label(0x9F37, "osargs_read_op")

d.comment(0x9F37, "Y=&0C: TX buffer size (smaller)", align=Align.INLINE)
d.comment(0x9F39, "X=2: argument offset", align=Align.INLINE)
d.comment(0x9F3B, "Send TX control block", align=Align.INLINE)
d.comment(0x9F3E, "Store A in last byte flag", align=Align.INLINE)
d.comment(0x9F40, "Load FS options pointer low", align=Align.INLINE)
d.comment(0x9F42, "Y=2: zero page offset", align=Align.INLINE)
d.comment(0x9F44, "Store A in zero page", align=Align.INLINE)
d.label(0x9F46, "loop_copy_reply_to_zp")

d.comment(0x9F46, "Load buffer byte from fs_cmd_data+Y", align=Align.INLINE)
d.comment(0x9F49, "Store in zero page at offset", align=Align.INLINE)
d.comment(0x9F4B, "Decrement source X", align=Align.INLINE)
d.comment(0x9F4C, "Decrement counter Y", align=Align.INLINE)
d.comment(0x9F4D, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0x9F4F, "Pull saved offset", align=Align.INLINE)
d.comment(0x9F50, "Return with last flag", align=Align.INLINE)
d.label(0x9F53, "osargs_ptr_dispatch")

d.comment(0x9F53, "Carry set: write file pointer", align=Align.INLINE)
d.comment(0x9F55, "Load block offset", align=Align.INLINE)
d.comment(0x9F57, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0x9F5A, "Load FS options pointer", align=Align.INLINE)
d.comment(0x9F5C, "Load FCB low byte from fcb_count_lo", align=Align.INLINE)
d.comment(0x9F5F, "Store in zero page pointer low", align=Align.INLINE)
d.comment(0x9F62, "Load FCB high byte from fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0x9F65, "Store in zero page pointer high", align=Align.INLINE)
d.comment(0x9F68, "Load FCB extent from fcb_station_or_count_hi", align=Align.INLINE)
d.comment(0x9F6B, "Store in zero page work area", align=Align.INLINE)
d.comment(0x9F6E, "A=0: clear high byte", align=Align.INLINE)
d.comment(0x9F70, "Store zero in work area high", align=Align.INLINE)
d.comment(0x9F73, "ALWAYS branch to return with flag", align=Align.INLINE)
d.label(0x9F75, "osargs_write_ptr")

d.comment(0x9F75, "Store write value in fs_func_code", align=Align.INLINE)
d.comment(0x9F78, "Transfer X to A", align=Align.INLINE)
d.comment(0x9F79, "Push X (zero page offset)", align=Align.INLINE)
d.comment(0x9F7A, "Y=3: copy 4 bytes", align=Align.INLINE)
d.label(0x9F7C, "loop_copy_ptr_to_buf")

d.comment(0x9F7C, "Load zero page data at offset", align=Align.INLINE)
d.comment(0x9F7E, "Store in fs_data_count buffer", align=Align.INLINE)
d.comment(0x9F81, "Decrement source", align=Align.INLINE)
d.comment(0x9F82, "Decrement counter", align=Align.INLINE)
d.comment(0x9F83, "Loop for all 4 bytes", align=Align.INLINE)
d.comment(0x9FAF, "Y=&0D: TX buffer size", align=Align.INLINE)
d.comment(0x9FB1, "X=5: argument offset", align=Align.INLINE)
d.comment(0x9FB3, "Send TX control block", align=Align.INLINE)
d.comment(0x9FB6, "Store X in last byte flag", align=Align.INLINE)
d.comment(0x9FB8, "Pull saved zero page offset", align=Align.INLINE)
d.comment(0x9FB9, "Transfer to Y", align=Align.INLINE)
d.comment(0x9FBA, "Load block offset (attribute)", align=Align.INLINE)
d.comment(0x9FBC, "Clear connection active flag", align=Align.INLINE)
d.comment(0x9FBF, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0x9FC2, "Load zero page pointer low", align=Align.INLINE)
d.comment(0x9FC5, "Store back to FCB fcb_count_lo", align=Align.INLINE)
d.comment(0x9FC8, "Load zero page pointer high", align=Align.INLINE)
d.comment(0x9FCB, "Store back to FCB fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0x9FCE, "Load zero page work byte", align=Align.INLINE)
d.comment(0x9FD1, "Store back to FCB fcb_station_or_count_hi", align=Align.INLINE)
d.comment(0x9FD4, "Return with last flag", align=Align.INLINE)
d.label(0x9FD7, "close_all_fcbs")

d.subroutine(
    0x9FD7,
    "close_all_fcbs",
    title="Close all FCBs (process_all_fcbs + finalise)",
    description="""Single-instruction wrapper: JSR process_all_fcbs to walk every FCB
slot and close each open file in turn, then fall through to
return_with_last_flag (which loads fs_last_byte_flag and finalises
caller state). Single caller (the OSFIND close-all path at &9EB8).""",
    on_exit={"a": "fs_last_byte_flag (loaded by return_with_last_flag)"},
)


d.comment(0x9FD7, "Process all matching FCBs first", align=Align.INLINE)
d.label(0x9FDA, "return_with_last_flag")

d.subroutine(
    0x9FDA,
    "return_with_last_flag",
    title="Load last-byte flag and finalise",
    description="""Loads fs_last_byte_flag (&BD) into A and falls through to
finalise_and_return, which clears the receive-attribute byte and
restores caller's X/Y. The 12 inbound refs are mostly fall-through
exits from FS reply handlers that need to return the last-byte
status to their caller; only one site (&9FD4) reaches it via JSR.""",
    on_exit={
        "a": "fs_last_byte_flag",
        "x": "fs_options (restored by finalise_and_return)",
        "y": "fs_block_offset (restored by finalise_and_return)",
    },
)


d.comment(0x9FDA, "Load last byte flag", align=Align.INLINE)
d.label(0x9FDC, "finalise_and_return")

d.subroutine(
    0x9FDC,
    "finalise_and_return",
    title="Clear receive-attribute and restore caller's X/Y",
    description="""Common 7-byte exit sequence used at the end of format_filename_field, several FS reply handlers, and match_fs_cmd. Saves A across a call to store_rx_attribute(0) (which clears the receive-attribute byte), then restores X from fs_options and Y from fs_block_offset before returning. Effectively: 'finish processing, clear network state, restore caller's pointers'.

One JSR caller (match_fs_cmd at &A599) plus 6 branch entries from format_filename_field's various exit paths.""",
    on_entry={"a": "result code to return"},
    on_exit={"a": "preserved", "x": "fs_options low byte", "y": "fs_block_offset low byte"},
)


d.comment(0x9FDC, "Push result on stack", align=Align.INLINE)
d.comment(0x9FDD, "A=0: clear error flag", align=Align.INLINE)
d.comment(0x9FDF, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0x9FE2, "Pull result back", align=Align.INLINE)
d.comment(0x9FE3, "Restore X from FS options pointer", align=Align.INLINE)
d.comment(0x9FE5, "Restore Y from block offset", align=Align.INLINE)
d.comment(0x9FE7, "Return to caller", align=Align.INLINE)
d.label(0x9FE8, "osfind_close_or_open")

d.subroutine(
    0x9FE8,
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


d.entry(0x9FE8)
d.comment(0x9FE8, "Compare with 2 (open for output)", align=Align.INLINE)
d.comment(0x9FEA, "2 or above: handle file open", align=Align.INLINE)
d.comment(0x9FEC, "Transfer to Y (Y=0 or 1)", align=Align.INLINE)
d.comment(0x9FED, "Non-zero (1 = read pointer): copy data", align=Align.INLINE)
d.comment(0x9FEF, "A=5: return code for close-all", align=Align.INLINE)
d.comment(0x9FF1, "ALWAYS branch to finalise", align=Align.INLINE)
d.label(0x9FF3, "done_file_open")

d.comment(0x9FF3, "Z set: jump to clear A and return", align=Align.INLINE)
d.label(0x9FF5, "clear_result")

d.subroutine(
    0x9FF5,
    "clear_result",
    title="Set A=0 and finalise",
    description="""Loads A=0 and falls through to shift_and_finalise (LSR A / BPL
finalise_and_return). The LSR-then-BPL is the standard FS-handler
'success exit with carry clear' idiom. Two callers: the post-
return path at &9FFC and the catalogue tail at tail_update_
catalogue (&A33D).""",
    on_exit={"a": "0", "c": "0 (LSR of 0)"},
)


d.comment(0x9FF5, "A=0: clear result", align=Align.INLINE)
d.label(0x9FF7, "shift_and_finalise")

d.comment(0x9FF7, "Shift right (always positive)", align=Align.INLINE)
d.comment(0x9FF8, "Positive: jump to finalise", align=Align.INLINE)
d.label(0x9FFA, "alloc_fcb_for_open")

d.comment(0x9FFA, "Mask to 6-bit access value", align=Align.INLINE)
d.comment(0x9FFC, "Non-zero: clear A and finalise", align=Align.INLINE)
d.comment(0x9FFE, "Transfer X to A (options pointer)", align=Align.INLINE)
d.comment(0x9FFF, "Allocate FCB slot or raise error", align=Align.INLINE)
d.comment(0xA002, "Toggle bit 7", align=Align.INLINE)
d.comment(0xA004, "Shift left: build open mode", align=Align.INLINE)
d.comment(0xA005, "Store open mode in fs_cmd_data", align=Align.INLINE)
d.comment(0xA008, "Rotate to complete mode byte", align=Align.INLINE)
d.comment(0xA009, "Store in fs_func_code", align=Align.INLINE)
d.comment(0xA00C, "Parse command argument (Y=0)", align=Align.INLINE)
d.comment(0xA00F, "X=2: buffer offset", align=Align.INLINE)
d.comment(0xA011, "Copy argument to TX buffer", align=Align.INLINE)
d.subroutine(
    0xA014, "send_open_file_request", description="Send file open request with V flag set for directory check."
)

d.comment(0xA014, "Y=6: open file command", align=Align.INLINE)
d.comment(0xA016, "Set V flag (skip directory check)", align=Align.INLINE)
d.comment(0xA019, "Set carry", align=Align.INLINE)
d.comment(0xA01A, "Rotate carry into escapable flag bit 7", align=Align.INLINE)
d.comment(0xA01C, "Send open request with V set", align=Align.INLINE)
d.comment(0xA01F, "Carry set (error): jump to finalise", align=Align.INLINE)
d.comment(0xA021, "A=&FF: mark as newly opened", align=Align.INLINE)
d.comment(0xA023, "Store &FF as receive attribute", align=Align.INLINE)
d.comment(0xA026, "Load handle from fs_cmd_data", align=Align.INLINE)
d.comment(0xA029, "Push handle", align=Align.INLINE)
d.comment(0xA02A, "A=4: file info sub-command", align=Align.INLINE)
d.comment(0xA02C, "Store sub-command", align=Align.INLINE)
d.comment(0xA02F, "X=1: shift filename", align=Align.INLINE)
d.label(0xA031, "loop_shift_filename")

d.comment(0xA031, "Load filename byte from fs_func_code+X", align=Align.INLINE)
d.comment(0xA034, "Shift down to fs_cmd_data+X", align=Align.INLINE)
d.comment(0xA037, "Advance source index", align=Align.INLINE)
d.comment(0xA038, "Is it CR (end of filename)?", align=Align.INLINE)
d.comment(0xA03A, "No: continue shifting", align=Align.INLINE)
d.comment(0xA03C, "Y=&12: file info request", align=Align.INLINE)
d.comment(0xA03E, "Send file info request", align=Align.INLINE)
d.comment(0xA041, "Load last byte flag", align=Align.INLINE)
d.comment(0xA043, "Clear bit 6 (read/write bits)", align=Align.INLINE)
d.comment(0xA045, "OR with reply access byte", align=Align.INLINE)
d.comment(0xA048, "Set bit 0 (file is open)", align=Align.INLINE)
d.comment(0xA04A, "Transfer to Y (access flags)", align=Align.INLINE)
d.comment(0xA04B, "Check bit 1 (write access)", align=Align.INLINE)
d.comment(0xA04D, "No write access: check read-only", align=Align.INLINE)
d.comment(0xA04F, "Pull handle from stack", align=Align.INLINE)
d.comment(0xA050, "Allocate FCB slot for channel", align=Align.INLINE)
d.comment(0xA053, "Non-zero: FCB allocated, store flags", align=Align.INLINE)
d.label(0xA055, "findv_handler")

d.comment(0xA055, "Verify workspace checksum", align=Align.INLINE)
d.comment(0xA058, "Set up transfer parameters", align=Align.INLINE)
d.comment(0xA05B, "Transfer A to X", align=Align.INLINE)
d.comment(0xA05C, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xA05F, "Transfer X back to A", align=Align.INLINE)
d.comment(0xA060, "Zero: close file, process FCBs", align=Align.INLINE)
d.comment(0xA062, "Save text pointer for OS", align=Align.INLINE)
d.comment(0xA065, "Load current directory handle", align=Align.INLINE)
d.comment(0xA068, "Zero: allocate new FCB", align=Align.INLINE)
d.comment(0xA06A, "Transfer Y to A", align=Align.INLINE)
d.comment(0xA06B, "X=0: clear directory handle", align=Align.INLINE)
d.comment(0xA06D, "Store zero (clear handle)", align=Align.INLINE)
d.comment(0xA070, "ALWAYS branch to finalise", align=Align.INLINE)
d.label(0xA072, "check_open_mode")

d.comment(0xA072, "Load access/open mode byte", align=Align.INLINE)
d.comment(0xA075, "Rotate right: check bit 0", align=Align.INLINE)
d.comment(0xA076, "Carry set (bit 0): check read permission", align=Align.INLINE)
d.comment(0xA078, "Rotate right: check bit 1", align=Align.INLINE)
d.comment(0xA079, "Carry clear (no write): skip", align=Align.INLINE)
d.comment(0xA07B, "Test bit 7 of fs_data_count (lock flag)", align=Align.INLINE)
d.comment(0xA07E, "Not locked: skip", align=Align.INLINE)
d.comment(0xA080, "Transfer Y to A (flags)", align=Align.INLINE)
d.comment(0xA081, "Set bit 5 (locked file flag)", align=Align.INLINE)
d.comment(0xA083, "Transfer back to Y", align=Align.INLINE)
d.label(0xA084, "alloc_fcb_with_flags")

d.comment(0xA084, "Pull handle from stack", align=Align.INLINE)
d.comment(0xA085, "Allocate FCB slot for channel", align=Align.INLINE)
d.label(0xA088, "store_fcb_flags")

d.comment(0xA088, "Transfer to X", align=Align.INLINE)
d.comment(0xA089, "Transfer Y to A (flags)", align=Align.INLINE)
d.comment(0xA08A, "Store flags in FCB table fcb_flags", align=Align.INLINE)
d.comment(0xA08D, "Transfer X back to A (handle)", align=Align.INLINE)
d.label(0xA08E, "done_osfind")

d.comment(0xA08E, "Jump to finalise and return", align=Align.INLINE)
d.label(0xA091, "close_all_channels")

d.comment(0xA091, "Process all matching FCBs", align=Align.INLINE)
d.comment(0xA094, "Transfer Y to A", align=Align.INLINE)
d.comment(0xA095, "Non-zero channel: close specific", align=Align.INLINE)
d.comment(0xA097, "Load FS options pointer low", align=Align.INLINE)
d.comment(0xA099, "Push (save for restore)", align=Align.INLINE)
d.comment(0xA09A, "A=&77: OSBYTE close spool/exec files", align=Align.INLINE)
d.comment(0xA09C, "Close any *SPOOL and *EXEC files", align=Align.INLINE)
d.comment(0xA09F, "Pull saved options pointer", align=Align.INLINE)
d.comment(0xA0A0, "Restore FS options pointer", align=Align.INLINE)
d.comment(0xA0A2, "A=0: clear flags", align=Align.INLINE)
d.comment(0xA0A4, "Save to fs_work_5", align=Align.INLINE)
d.comment(0xA0A6, "Load current FS station low", align=Align.INLINE)
d.comment(0xA0A8, "ALWAYS branch to send close request", align=Align.INLINE)
d.comment(0xA0A9, "Save to fs_work_6", align=Align.INLINE)
d.label(0xA0AA, "close_specific_chan")

d.comment(0xA0AA, "Validate channel character", align=Align.INLINE)
d.comment(0xA0AD, "Is it CR (no argument)?", align=Align.INLINE)
d.label(0xA0B0, "send_close_request")

d.comment(0xA0B0, "Store as fs_cmd_data (file handle)", align=Align.INLINE)
d.comment(0xA0B3, "X=1: argument size", align=Align.INLINE)
d.comment(0xA0B5, "Y=7: close file command", align=Align.INLINE)
d.comment(0xA0B7, "Send close file request", align=Align.INLINE)
d.comment(0xA0BA, "Parameter block low", align=Align.INLINE)
d.comment(0xA0BC, "Parameter block high", align=Align.INLINE)
d.comment(0xA0BE, "Clear V flag", align=Align.INLINE)
d.comment(0xA0BF, "Scan and clear all FCB flags", align=Align.INLINE)
d.label(0xA0C2, "done_close")

d.comment(0xA0C2, "Return with last flag", align=Align.INLINE)
d.label(0xA0C5, "clear_single_fcb")

d.comment(0xA0C5, "A=0: clear FCB entry", align=Align.INLINE)
d.comment(0xA0C7, "Clear hazel_fcb_addr_mid for slot Y", align=Align.INLINE)
d.comment(0xA0CA, "Clear hazel_fcb_state_byte for slot Y", align=Align.INLINE)
d.comment(0xA0CD, "Z still set from LDA #0: always branch to done_close", align=Align.INLINE)
d.label(0xA0CF, "fscv_0_opt_entry")

d.subroutine(
    0xA0CF,
    "fscv_0_opt_entry",
    title="FSCV reason 0: read OSARGS",
    description="""Handles OSARGS via the FSCV vector. If `A=0` (initialise dot-seen
flag) clears the flag and proceeds. Compares `X` against 4 (number
of args): out-of-range exits via the OSARGS dispatch chain to a
shared error path; otherwise dispatches to the per-argument
handler. Reached via the FSCV vector with reason code 0.""",
    on_entry={"a": "OSARGS sub-function (0 = initialise)", "x": "argument index (0-3)"},
)


d.entry(0xA0CF)
d.comment(0xA0CF, "A=0 (init sub-code): jump to store_display_flag", align=Align.INLINE)
d.comment(0xA0D1, "Non-zero A: X==4? (read OSARGS args)", align=Align.INLINE)
d.comment(0xA0D3, "X != 4: take normal OSARGS dispatch", align=Align.INLINE)
d.comment(0xA0D5, "X==4 path: Y < 4?", align=Align.INLINE)
d.comment(0xA0D7, "Yes: send OSARGS request via TXCB", align=Align.INLINE)
d.label(0xA0D9, "osargs_dispatch")

d.comment(0xA0D9, "X-- (osargs_dispatch entry): step sub-code down", align=Align.INLINE)
d.comment(0xA0DA, "X != 1: take store-ptr-lo path", align=Align.INLINE)
d.label(0xA0DC, "store_display_flag")

d.comment(0xA0DC, "Store Y as hazel_fs_messages_flag (display control)", align=Align.INLINE)
d.comment(0xA0DF, "Tail-branch to done_close", align=Align.INLINE)
d.label(0xA0E1, "error_osargs")

d.comment(0xA0E1, "A=7: error code (out-of-range OSARGS sub-code)", align=Align.INLINE)
d.comment(0xA0E3, "Raise BRK error", align=Align.INLINE)
d.label(0xA0E6, "send_osargs_request")

d.comment(0xA0E6, "Store Y as TXCB data byte (OSARGS payload)", align=Align.INLINE)
d.comment(0xA0E9, "Y=&16: TXCB function code (OSARGS request)", align=Align.INLINE)
d.comment(0xA0EB, "Send OSARGS request via TX control block", align=Align.INLINE)
d.comment(0xA0EE, "Reload Y from fs_block_offset", align=Align.INLINE)
d.comment(0xA0F0, "Update hazel_fs_flags from OSARGS reply", align=Align.INLINE)
d.comment(0xA0F3, "No error (positive): tail to done_close", align=Align.INLINE)
d.label(0xA0F5, "osargs_store_ptr_lo")

d.comment(0xA0F5, "X >= 8?", align=Align.INLINE)
d.comment(0xA0F7, "Yes: out-of-range OSARGS sub-code", align=Align.INLINE)
d.comment(0xA0F9, "X == 4?", align=Align.INLINE)
d.comment(0xA0FB, "Yes: take fast read path (osargs_check_length)", align=Align.INLINE)
d.comment(0xA0FD, "Y < 4?", align=Align.INLINE)
d.comment(0xA0FF, "Yes: take CMOS-protect path", align=Align.INLINE)
d.label(0xA101, "osargs_check_length")

d.comment(0xA101, "Y >= 2?", align=Align.INLINE)
d.comment(0xA103, "Yes: argument out of range", align=Align.INLINE)
d.label(0xA105, "osopt_check_cmos_protect")

d.comment(0xA106, "Save sub-code across the CMOS read", align=Align.INLINE)
d.comment(0xA107, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0xA109, "Read CMOS &11 (Econet status) -> Y", align=Align.INLINE)
d.comment(0xA10C, "Restore sub-code", align=Align.INLINE)
d.comment(0xA10D, "Read CMOS &11 result to A", align=Align.INLINE)
d.comment(0xA10E, "Mask CMOS &11 with cmos_opt_mask_table[X]", align=Align.INLINE)
d.comment(0xA112, "Push CMOS value", align=Align.INLINE)
d.comment(0xA113, "Load shift count from cmos_attr_table[X]", align=Align.INLINE)
d.comment(0xA116, "Value to X", align=Align.INLINE)
d.comment(0xA117, "Caller's Y back to A as the value to shift", align=Align.INLINE)
d.comment(0xA118, "Shift CMOS bits", align=Align.INLINE)
d.label(0xA118, "loop_extract_attr_bits")

d.comment(0xA119, "Count down shift iterations", align=Align.INLINE)
d.comment(0xA11A, "Loop until X reaches 0", align=Align.INLINE)
d.comment(0xA11C, "Stash shifted value in fs_load_addr scratch", align=Align.INLINE)
d.comment(0xA11E, "Pop saved value", align=Align.INLINE)
d.comment(0xA11F, "OR with the CMOS-masked value", align=Align.INLINE)
d.comment(0xA122, "X=&11: target CMOS byte for write-back", align=Align.INLINE)
d.label(0xA124, "osopt_cmos_writeback_jsr")

d.comment(0xA124, "Write CMOS RAM byte (Y) to byte index (X)", align=Align.INLINE)
# UNMAPPED: d.label(
# UNMAPPED:     0xA0FF,
# UNMAPPED:     "cmos_attr_table",
# UNMAPPED:     description="""Indexing-base alias of [`cmos_opt_mask_table`](label:cmos_opt_mask_table) - 4.
# UNMAPPED: `LDA cmos_attr_table,X` at &A0ED with X=4..7 reads the read-masks 1, 2, 4, 6 from the underlying table; those values double as bit-shift counts that left-align the new field into CMOS &11. The byte at &A0FF is inside the operand of the JSR at &A0FE and is never read directly.""",
# UNMAPPED:     length=1,
# UNMAPPED:     group="idx_base",
# UNMAPPED:     access="r",
# UNMAPPED: )

d.comment(0xA127, "Tail-branch into the OSARGS done path", align=Align.INLINE)
d.index_base(0xA129, "cmos_opt_mask_table")
d.banner(
    0xA129,
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
    d.byte(0xA129 + _i)
del _i
d.comment(0xA129, "Idx 0: AND mask = &01 (extract CMOS &11 bit 0)", align=Align.INLINE)
d.comment(0xA12A, "Idx 1: AND mask = &02 (extract CMOS &11 bit 1)", align=Align.INLINE)
d.comment(0xA12B, "Idx 2: AND mask = &04 (extract CMOS &11 bit 2)", align=Align.INLINE)
d.comment(0xA12C, "Idx 3: AND mask = &06 (extract CMOS &11 bits 1,2)", align=Align.INLINE)
d.comment(0xA12D, "Idx 4: AND mask = &FD (clear CMOS &11 bit 1)", align=Align.INLINE)
d.comment(0xA12E, "Idx 5: AND mask = &F3 (clear CMOS &11 bits 2,3)", align=Align.INLINE)
d.comment(0xA12F, "Idx 6: AND mask = &CF (clear CMOS &11 bits 4,5)", align=Align.INLINE)
d.comment(0xA130, "Idx 7: AND mask = &3F (clear CMOS &11 bits 6,7)", align=Align.INLINE)

d.label(0xA131, "fscv_1_eof")

d.subroutine(
    0xA131,
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


d.entry(0xA131)
d.comment(0xA131, "Verify workspace checksum", align=Align.INLINE)
d.comment(0xA134, "Push checksum-verify result -- preserve it across the FCB lookups below", align=Align.INLINE)
d.comment(0xA135, "Load block offset", align=Align.INLINE)
d.comment(0xA137, "Push block offset", align=Align.INLINE)
d.comment(0xA138, "Store X in cur_chan_attr", align=Align.INLINE)
d.comment(0xA13B, "Find matching FCB entry", align=Align.INLINE)
d.comment(0xA13E, "Zero: no match found", align=Align.INLINE)
d.comment(0xA140, "Load FCB low byte from fcb_count_lo", align=Align.INLINE)
d.comment(0xA143, "Compare with stored offset fcb_buf_offset", align=Align.INLINE)
d.comment(0xA146, "FCB lo-byte below stored offset -> not the matching FCB; mark_not_found", align=Align.INLINE)
d.comment(0xA148, "X=&FF: mark as found (all bits set)", align=Align.INLINE)
d.comment(0xA14A, "ALWAYS branch (negative)", align=Align.INLINE)
d.label(0xA14C, "mark_not_found")

d.comment(0xA14C, "X=0: mark as not found", align=Align.INLINE)
d.label(0xA14E, "restore_and_return")

d.comment(0xA14E, "Restore block offset from stack", align=Align.INLINE)
d.comment(0xA14F, "Generate 'Syntax' error", align=Align.INLINE)
d.comment(0xA150, "Restore result from stack", align=Align.INLINE)
d.comment(0xA151, "Return", align=Align.INLINE)
d.label(0xA152, "update_addr_from_offset9")

d.subroutine(
    0xA152,
    "update_addr_from_offset9",
    title="Update both address fields in FS options",
    description="""Calls [`add_workspace_to_fsopts`](label:add_workspace_to_fsopts) for offset
9 (the high address / exec address field), then falls through to
[`update_addr_from_offset1`](label:update_addr_from_offset1) to process offset
1 (the low address / load address field).""",
    on_exit={"a, x, y, c flag": "clobbered (4-byte arithmetic loop)"},
)


d.comment(0xA152, "Y=9: FS options offset for high address", align=Align.INLINE)
d.comment(0xA154, "Add workspace values to FS options", align=Align.INLINE)
d.label(0xA157, "update_addr_from_offset1")

d.subroutine(
    0xA157,
    "update_addr_from_offset1",
    title="Update low address field in FS options",
    description="""Sets Y=1 and falls through to
add_workspace_to_fsopts to add the workspace
adjustment bytes to the load address field at
offset 1 in the FS options block.""",
    on_entry={"c": "carry state passed to add_workspace_to_fsopts"},
)


d.comment(0xA157, "Y=1: FS options offset for low address", align=Align.INLINE)
d.label(0xA159, "add_workspace_to_fsopts")

d.subroutine(
    0xA159,
    "add_workspace_to_fsopts",
    title="Add workspace bytes to FS options with clear carry",
    description="""Clears carry and falls through to
adjust_fsopts_4bytes. Provides a convenient entry
point when the caller needs addition without a
preset carry.""",
    on_entry={"y": "FS options offset for first byte"},
)


d.comment(0xA159, "Clear carry for the upcoming 4-byte add", align=Align.INLINE)
d.label(0xA15A, "adjust_fsopts_4bytes")

d.subroutine(
    0xA15A,
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

d.comment(0xA15A, "X=&FC: loop counter (-4 to -1)", align=Align.INLINE)
d.label(0xA15C, "loop_adjust_byte")

d.comment(0xA15C, "Load FS options byte at offset Y", align=Align.INLINE)
d.comment(0xA15E, "Test fs_load_addr_2 bit 7 (add/subtract)", align=Align.INLINE)
d.comment(0xA160, "Push high byte", align=Align.INLINE)
d.comment(0xA162, "Add workspace byte to FS options", align=Align.INLINE)
d.comment(0xA165, "RTS dispatches to command handler", align=Align.INLINE)
d.label(0xA168, "subtract_ws_byte")

d.comment(0xA168, "Subtract workspace byte from FS options", align=Align.INLINE)
d.label(0xA16B, "store_adjusted_byte")

d.subroutine(
    0xA16B,
    "store_adjusted_byte",
    title="Store adjusted byte and step the loop",
    description="""Tail of the address-adjustment 4-byte loop: STA (fs_options),Y /
INY / INX / BNE loop_adjust_byte / RTS. The BNE retries until X
has cycled through all 4 bytes; once X overflows back to 0 the
loop exits and the RTS returns. Single caller (the loop-body fall-
through at &A165).""",
    on_entry={"a": "byte to store", "y": "current FS-options index", "x": "remaining-byte counter"},
)


d.comment(0xA16B, "Store result back to FS options", align=Align.INLINE)
d.comment(0xA16D, "Advance to next byte", align=Align.INLINE)
d.comment(0xA16E, "Advance counter", align=Align.INLINE)
d.comment(0xA16F, "Loop until 4 bytes processed", align=Align.INLINE)
d.comment(0xA171, "Return", align=Align.INLINE)
d.subroutine(
    0xA172,
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


d.entry(0xA172)
d.comment(0xA172, "Verify workspace checksum", align=Align.INLINE)
d.comment(0xA175, "Set up transfer parameters", align=Align.INLINE)
d.comment(0xA178, "Push transfer type on stack", align=Align.INLINE)
d.comment(0xA179, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xA17C, "Pull transfer type", align=Align.INLINE)
d.comment(0xA17D, "Transfer to X", align=Align.INLINE)
d.comment(0xA17E, "Zero: no valid operation, return", align=Align.INLINE)
d.comment(0xA180, "Decrement (convert 1-based to 0-based)", align=Align.INLINE)
d.comment(0xA181, "Compare with 8 (max operation)", align=Align.INLINE)
d.comment(0xA183, "Below 8: valid operation", align=Align.INLINE)
d.label(0xA185, "skip_if_out_of_range")

d.comment(0xA185, "Out of range: return with flag", align=Align.INLINE)
d.label(0xA188, "valid_osgbpb_op")

d.comment(0xA188, "Transfer operation code to A", align=Align.INLINE)
d.comment(0xA189, "Y=0: buffer offset", align=Align.INLINE)
d.comment(0xA18B, "Push operation code", align=Align.INLINE)
d.comment(0xA18C, "Compare with 4 (write operations)", align=Align.INLINE)
d.comment(0xA18E, "Below 4: read operation", align=Align.INLINE)
d.comment(0xA190, "4 or above: write data block", align=Align.INLINE)
d.label(0xA193, "load_chan_handle")

d.comment(0xA193, "Load channel handle from FS options", align=Align.INLINE)
d.comment(0xA195, "Push handle", align=Align.INLINE)
d.comment(0xA196, "Check file is not a directory", align=Align.INLINE)
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
d.comment(0xA19A, "Send TX control block to server", align=Align.INLINE)
d.comment(0xA19D, "Pull operation code", align=Align.INLINE)
d.comment(0xA19E, "Set up transfer workspace", align=Align.INLINE)
d.comment(0xA1A1, "Save flags (carry from setup)", align=Align.INLINE)
d.comment(0xA1A2, "Y=0: index for channel handle", align=Align.INLINE)
d.comment(0xA1A4, "Load channel handle from FS options", align=Align.INLINE)
d.comment(0xA1A6, "Carry set (write): set active", align=Align.INLINE)
d.comment(0xA1A8, "Read: clear connection active", align=Align.INLINE)
d.comment(0xA1AB, "Branch to continue (always positive)", align=Align.INLINE)
d.label(0xA1AD, "set_write_active")

d.comment(0xA1AD, "Write: set connection active", align=Align.INLINE)
d.label(0xA1B0, "setup_gbpb_request")

d.comment(0xA1B0, "Clear fs_func_code (Y=0)", align=Align.INLINE)
d.comment(0xA1B3, "Look up channel slot data", align=Align.INLINE)
d.comment(0xA1B6, "Store flag byte in fs_cmd_data", align=Align.INLINE)
d.comment(0xA1B9, "Y=&0C: TX buffer size (short)", align=Align.INLINE)
d.comment(0xA1BB, "X=2: argument count", align=Align.INLINE)
d.comment(0xA1BD, "Send TX control block", align=Align.INLINE)
d.comment(0xA1C0, "Look up channel entry at Y=0", align=Align.INLINE)
d.comment(0xA1C3, "Y=9: FS options offset for position", align=Align.INLINE)
d.comment(0xA1C5, "Load new position low from fs_cmd_data", align=Align.INLINE)
d.comment(0xA1C8, "Update FCB low byte in fcb_count_lo", align=Align.INLINE)
d.comment(0xA1CB, "Store in FS options at Y=9", align=Align.INLINE)
d.comment(0xA1CD, "Y=&0A", align=Align.INLINE)
d.comment(0xA1CE, "Load new position high from fs_func_code", align=Align.INLINE)
d.comment(0xA1D1, "Update FCB high byte in fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0xA1D4, "Store in FS options at Y=&0A", align=Align.INLINE)
d.comment(0xA1D6, "Y=&0B", align=Align.INLINE)
d.comment(0xA1D7, "Load new extent from fs_data_count", align=Align.INLINE)
d.comment(0xA1DA, "Update FCB extent in fcb_station_or_count_hi", align=Align.INLINE)
d.comment(0xA1DD, "Store in FS options at Y=&0B", align=Align.INLINE)
d.comment(0xA1DF, "A=0: clear high byte of extent", align=Align.INLINE)
d.comment(0xA1E1, "Y=&0C", align=Align.INLINE)
d.comment(0xA1E2, "Store zero in FS options at Y=&0C", align=Align.INLINE)
d.comment(0xA1E4, "Restore flags", align=Align.INLINE)
d.comment(0xA1E5, "Carry clear: skip last-byte check", align=Align.INLINE)
d.comment(0xA1E7, "Load last-byte-of-transfer flag", align=Align.INLINE)
d.comment(0xA1E9, "Is transfer still pending (flag=3)?", align=Align.INLINE)
d.label(0xA1EB, "return_success")


d.comment(0xA1EB, "A=0: success", align=Align.INLINE)
d.comment(0xA1ED, "Jump to finalise and return", align=Align.INLINE)
d.label(0xA1F0, "lookup_cat_entry_0")

d.subroutine(
    0xA1F0,
    "lookup_cat_entry_0",
    title="Look up channel from FS options offset 0",
    description="""Loads the channel handle from (fs_options) at
offset 0, then falls through to lookup_cat_slot_data
to find the corresponding FCB entry.""",
    on_exit={"a": "FCB flag byte from hazel_fcb_slot_attr,X", "x": "channel slot index"},
)


d.comment(0xA1F0, "Y=0: offset for channel handle", align=Align.INLINE)
d.comment(0xA1F2, "Load channel handle from FS options", align=Align.INLINE)
d.label(0xA1F4, "lookup_cat_slot_data")

d.subroutine(
    0xA1F4,
    "lookup_cat_slot_data",
    title="Look up channel and return FCB flag byte",
    description="""Calls [`lookup_chan_by_char`](label:lookup_chan_by_char) to find the channel
slot for handle `A` in the channel table, then loads the FCB
slot-attribute byte from
[`hazel_fcb_slot_attr`](label:hazel_fcb_slot_attr)+`X`.""",
    on_entry={"a": "channel handle"},
    on_exit={"a": "FCB slot-attribute byte", "x": "channel slot index"},
)


d.comment(0xA1F4, "Look up channel by character", align=Align.INLINE)
d.comment(0xA1F7, "Load slot-attribute byte from hazel_fcb_slot_attr,X", align=Align.INLINE)
d.comment(0xA1FA, "Return with flag in A", align=Align.INLINE)
d.label(0xA1FB, "setup_transfer_workspace")

d.subroutine(
    0xA1FB,
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


d.comment(0xA1FB, "Push operation code on stack", align=Align.INLINE)
d.comment(0xA1FC, "Look up channel entry at Y=0", align=Align.INLINE)
d.comment(0xA1FF, "Store flag byte in fs_cmd_data", align=Align.INLINE)
d.comment(0xA203, "Y=&0B: source offset in FS options", align=Align.INLINE)
d.comment(0xA205, "X=6: copy 6 bytes", align=Align.INLINE)
d.label(0xA207, "loop_copy_opts_to_buf")

d.comment(0xA207, "Load FS options byte", align=Align.INLINE)
d.comment(0xA209, "Store in fs_func_code buffer", align=Align.INLINE)
d.comment(0xA20C, "Decrement source index", align=Align.INLINE)
d.comment(0xA20D, "Skip offset 8?", align=Align.INLINE)
d.comment(0xA20F, "No: continue copy", align=Align.INLINE)
d.comment(0xA211, "Skip offset 8 (hole in structure)", align=Align.INLINE)
d.label(0xA212, "skip_struct_hole")

d.comment(0xA212, "Decrement destination counter", align=Align.INLINE)
d.comment(0xA213, "Loop until all 6 bytes copied", align=Align.INLINE)
# UNMAPPED: d.comment(0xA213, "Pull operation code", align=Align.INLINE)
# UNMAPPED: d.comment(0xA214, "Shift right: check bit 0 (direction)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA215, "Push updated code", align=Align.INLINE)
# UNMAPPED: d.comment(0xA216, "Carry clear: OSBGET (read)", align=Align.INLINE)
# UNMAPPED: d.comment(0xA218, "Carry set: OSBPUT (write), X=1", align=Align.INLINE)
d.label(0xA22D, "store_direction_flag")

d.comment(0xA22D, "Store direction flag in fs_func_code", align=Align.INLINE)
d.comment(0xA230, "Y=&0B: TX buffer size", align=Align.INLINE)
d.comment(0xA232, "X=&91: port for OSBGET", align=Align.INLINE)
d.comment(0xA234, "Pull operation code", align=Align.INLINE)
d.comment(0xA235, "Push back (keep on stack)", align=Align.INLINE)
d.comment(0xA236, "Zero (OSBGET): keep port &91", align=Align.INLINE)
d.comment(0xA238, "X=&92: port for OSBPUT", align=Align.INLINE)
d.comment(0xA23A, "Y=&0A: adjusted buffer size", align=Align.INLINE)
d.label(0xA23B, "store_port_and_send")

d.comment(0xA23B, "Store port in fs_cmd_urd", align=Align.INLINE)
d.comment(0xA23E, "Store port in fs_error_ptr", align=Align.INLINE)
d.comment(0xA240, "X=8: argument count", align=Align.INLINE)
d.comment(0xA242, "Load file handle from fs_cmd_data", align=Align.INLINE)
d.comment(0xA245, "Send request (no write data)", align=Align.INLINE)
d.comment(0xA248, "X=0: index", align=Align.INLINE)
d.comment(0xA24A, "Load channel handle from FS options", align=Align.INLINE)
d.comment(0xA24C, "Transfer to X as index", align=Align.INLINE)
d.comment(0xA24D, "Load FCB flags from fcb_flags", align=Align.INLINE)
d.comment(0xA250, "Toggle bit 0 (transfer direction)", align=Align.INLINE)
d.comment(0xA252, "Store updated flags", align=Align.INLINE)
d.comment(0xA255, "Clear carry for addition", align=Align.INLINE)
d.comment(0xA256, "X=4: process 4 address bytes", align=Align.INLINE)
d.label(0xA258, "loop_setup_addr_bytes")

d.comment(0xA258, "Load FS options address byte", align=Align.INLINE)
d.comment(0xA25A, "Store in zero page address area", align=Align.INLINE)
d.comment(0xA25D, "Store in TXCB position", align=Align.INLINE)
d.comment(0xA260, "Advance Y by 4", align=Align.INLINE)
d.comment(0xA263, "Add offset from FS options", align=Align.INLINE)
d.comment(0xA265, "Store computed end address", align=Align.INLINE)
d.comment(0xA268, "Retreat Y by 3 for next pair", align=Align.INLINE)
d.comment(0xA26B, "Decrement byte counter", align=Align.INLINE)
d.comment(0xA26C, "Loop for all 4 address bytes", align=Align.INLINE)
d.comment(0xA26E, "X=1 (INX from 0)", align=Align.INLINE)
d.label(0xA26F, "loop_copy_offset")

d.comment(0xA26F, "Load offset from fs_cmd_csd", align=Align.INLINE)
d.comment(0xA272, "Copy to fs_func_code", align=Align.INLINE)
d.comment(0xA275, "Decrement counter", align=Align.INLINE)
d.comment(0xA276, "Loop until both bytes copied", align=Align.INLINE)
d.comment(0xA278, "Pull operation code", align=Align.INLINE)
d.comment(0xA279, "Non-zero (OSBPUT): swap addresses", align=Align.INLINE)
d.comment(0xA27B, "Load port from fs_cmd_urd", align=Align.INLINE)
d.comment(0xA27E, "Check and set up TXCB", align=Align.INLINE)
d.comment(0xA281, "Carry set: skip swap", align=Align.INLINE)
d.label(0xA283, "send_with_swap")

d.comment(0xA283, "Send TXCB and swap start/end addresses", align=Align.INLINE)
d.label(0xA286, "recv_and_update")

d.comment(0xA286, "Receive and process reply", align=Align.INLINE)
d.comment(0xA289, "Store result in fs_load_addr_2", align=Align.INLINE)
d.comment(0xA28B, "Update addresses from offset 9", align=Align.INLINE)
d.comment(0xA28E, "Decrement fs_load_addr_2", align=Align.INLINE)
d.comment(0xA290, "Set carry for subtraction", align=Align.INLINE)
d.comment(0xA291, "Adjust FS options by 4 bytes", align=Align.INLINE)
d.comment(0xA294, "Shift fs_cmd_data left (update status)", align=Align.INLINE)
d.comment(0xA297, "Return", align=Align.INLINE)
d.subroutine(
    0xA298,
    "recv_reply_preserve_flags",
    title="Receive and process reply, preserving flags",
    description="""Wrapper around recv_and_process_reply that
saves and restores the processor status register,
so the caller's flag state is not affected by
the reply processing.""",
    on_exit={"a": "FS reply status", "p (flags)": "preserved across the call (PHP/PLP)"},
)


d.comment(0xA298, "Save flags before reply processing", align=Align.INLINE)
d.comment(0xA299, "Process server reply", align=Align.INLINE)
d.comment(0xA29C, "Restore flags after reply processing", align=Align.INLINE)
d.comment(0xA29D, "Return", align=Align.INLINE)
d.label(0xA29E, "send_osbput_data")

d.subroutine(
    0xA29E,
    "send_osbput_data",
    title="Send OSBPUT data block to file server",
    description="""Sets `Y=&15` (TX buffer size for OSBPUT data) and calls
[`save_net_tx_cb`](label:save_net_tx_cb) to dispatch the TX. Then copies
the display flag from `hazel_fs_flags` to `hazel_txcb_byte_16` (TX header continuation).
Single caller in the OSBPUT-buffered-write path.""",
)


d.entry(0xA29E)
d.comment(0xA29E, "Y=&15: TX buffer size for OSBPUT data", align=Align.INLINE)
d.comment(0xA2A0, "Send TX control block", align=Align.INLINE)
d.comment(0xA2A3, "Load display flag from hazel_fs_flags", align=Align.INLINE)
d.comment(0xA2A6, "Store in hazel_txcb_byte_16", align=Align.INLINE)
d.comment(0xA2A9, "Clear fs_load_addr (X=0)", align=Align.INLINE)
d.comment(0xA2AB, "Clear fs_load_addr_hi", align=Align.INLINE)
d.comment(0xA2AD, "A=&12: byte count for data block", align=Align.INLINE)
d.comment(0xA2AF, "Store in fs_load_addr_2", align=Align.INLINE)
d.comment(0xA2B1, "ALWAYS branch to write data block", align=Align.INLINE)
d.label(0xA2B3, "write_block_entry")

d.subroutine(
    0xA2B3,
    "write_block_entry",
    title="Pre-write Tube-station check, fall into write_data_block",
    description="""Y=4 (FS-options offset for station). If tube_present is zero
(no Tube co-pro), branch forward to store_station_result and skip
the next compare; otherwise CMP (fs_options),Y to validate the
caller's station matches the saved Tube station. Falls through to
write_data_block. Single caller (&A190 in the OSWORD write path).""",
    on_entry={"y": "ignored (forced to 4)"},
)


d.comment(0xA2B3, "Y=4: offset for station comparison", align=Align.INLINE)
d.comment(0xA2B5, "Load stored station from tube_present", align=Align.INLINE)
d.comment(0xA2B8, "Zero: skip station check", align=Align.INLINE)
d.comment(0xA2BA, "Compare with FS options station", align=Align.INLINE)
d.comment(0xA2BC, "Mismatch: skip subtraction", align=Align.INLINE)
d.comment(0xA2BE, "Y=3", align=Align.INLINE)
d.comment(0xA2BF, "Subtract FS options value", align=Align.INLINE)
d.label(0xA2C1, "store_station_result")

d.comment(0xA2C1, "Store result in svc_state", align=Align.INLINE)
d.label(0xA2C3, "loop_copy_opts_to_ws")

d.comment(0xA2C3, "Load FS options byte at Y", align=Align.INLINE)
d.comment(0xA2C5, "Store in workspace at fs_last_byte_flag+Y", align=Align.INLINE)
d.comment(0xA2C8, "Decrement index", align=Align.INLINE)
d.comment(0xA2C9, "Loop until all bytes copied", align=Align.INLINE)
d.comment(0xA2CB, "Pull operation code", align=Align.INLINE)
d.comment(0xA2CC, "Mask to 2-bit sub-operation", align=Align.INLINE)
d.comment(0xA2CE, "Zero: send OSBPUT data", align=Align.INLINE)
d.comment(0xA2D0, "Shift right: check bit 0", align=Align.INLINE)
d.comment(0xA2D1, "Zero (bit 0 clear): handle read", align=Align.INLINE)
d.comment(0xA2D3, "Carry set: handle catalogue update", align=Align.INLINE)
d.label(0xA2D5, "handle_cat_update")

d.comment(0xA2D5, "Transfer to Y (Y=0)", align=Align.INLINE)
d.comment(0xA2D6, "Load data byte from fs_csd_handle", align=Align.INLINE)
d.comment(0xA2D9, "Store in fs_cmd_csd", align=Align.INLINE)
d.comment(0xA2DC, "Load high data byte from fs_lib_handle", align=Align.INLINE)
d.comment(0xA2DF, "Store in fs_cmd_lib", align=Align.INLINE)
d.comment(0xA2E2, "Load port from fs_urd_handle", align=Align.INLINE)
d.comment(0xA2E5, "Store in fs_cmd_urd", align=Align.INLINE)
d.comment(0xA2E8, "X=&12: buffer size marker", align=Align.INLINE)
d.comment(0xA2EA, "Store in fs_cmd_y_param", align=Align.INLINE)
d.comment(0xA2ED, "A=&0D: count value", align=Align.INLINE)
d.comment(0xA2EF, "Store in fs_func_code", align=Align.INLINE)
d.comment(0xA2F2, "Store in fs_load_addr_2", align=Align.INLINE)
d.comment(0xA2F4, "Shift right (A=6)", align=Align.INLINE)
d.comment(0xA2F5, "Store in fs_cmd_data", align=Align.INLINE)
d.comment(0xA2F8, "Clear carry for addition", align=Align.INLINE)
d.comment(0xA2F9, "Prepare and send TX control block", align=Align.INLINE)
d.comment(0xA2FC, "Store X in fs_load_addr_hi (X=0)", align=Align.INLINE)
d.comment(0xA2FE, "X=1 (after INX)", align=Align.INLINE)
d.comment(0xA2FF, "Store X in fs_load_addr", align=Align.INLINE)
d.label(0xA301, "write_data_block")

d.subroutine(
    0xA301,
    "write_data_block",
    title="Write data block to destination or Tube",
    description="""| `tube_present` | Action |
|---|---|
| zero (no Tube) | copy directly from the `fs_cmd_data` buffer via `(fs_crc_lo)` |
| non-zero       | claim the Tube, set up the transfer address, write via R3 |""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xA301, "Load svc_state (tube flag)", align=Align.INLINE)
d.comment(0xA303, "Non-zero: write via tube", align=Align.INLINE)
d.comment(0xA305, "Load source index from fs_load_addr", align=Align.INLINE)
d.comment(0xA307, "Load destination index from fs_load_addr_hi", align=Align.INLINE)
d.label(0xA309, "loop_copy_to_host")

d.comment(0xA309, "Load data byte from fs_cmd_data buffer", align=Align.INLINE)
d.comment(0xA30C, "Store to destination via fs_crc pointer", align=Align.INLINE)
d.comment(0xA30E, "Advance source index", align=Align.INLINE)
d.comment(0xA30F, "Advance destination index", align=Align.INLINE)
d.comment(0xA310, "Decrement byte counter", align=Align.INLINE)
d.comment(0xA312, "Loop until all bytes transferred", align=Align.INLINE)
d.comment(0xA314, "X=&10: scan 16 slots (15 to 0)", align=Align.INLINE)
d.label(0xA316, "tube_write_setup")

d.comment(0xA316, "Clear V", align=Align.INLINE)
d.comment(0xA319, "A=1: tube transfer type (write)", align=Align.INLINE)
d.comment(0xA31B, "Load destination low from fs_options", align=Align.INLINE)
d.comment(0xA31D, "No match: try next", align=Align.INLINE)
d.comment(0xA31F, "Load slot status byte", align=Align.INLINE)
d.comment(0xA320, "No wrap: skip high increment", align=Align.INLINE)
d.comment(0xA322, "Test bit 2 (PS active flag)?", align=Align.INLINE)
d.label(0xA323, "set_tube_addr")

d.comment(0xA323, "Set up tube transfer address", align=Align.INLINE)
d.comment(0xA326, "Transfer Y to A", align=Align.INLINE)
d.label(0xA328, "loop_write_to_tube")

d.comment(0xA328, "Load data byte from buffer", align=Align.INLINE)
d.comment(0xA32B, "Write to tube data register 3", align=Align.INLINE)
d.comment(0xA32D, "Store Y to fs_urd_handle", align=Align.INLINE)
d.comment(0xA32E, "Advance source index", align=Align.INLINE)
d.comment(0xA32F, "Y=6: tube write delay", align=Align.INLINE)
d.label(0xA331, "loop_tube_delay")

d.comment(0xA331, "Delay loop: decrement Y", align=Align.INLINE)
d.comment(0xA332, "Transfer Y to A", align=Align.INLINE)
d.comment(0xA334, "Decrement byte counter", align=Align.INLINE)
d.comment(0xA336, "Store allocation result", align=Align.INLINE)
d.comment(0xA338, "A=&83: release tube claim", align=Align.INLINE)
d.comment(0xA33A, "Release tube", align=Align.INLINE)
d.label(0xA33D, "tail_update_catalogue")

d.subroutine(
    0xA33D,
    "tail_update_catalogue",
    title="Catalogue-update exit (JMP clear_result)",
    description="""Single-instruction tail: JMP clear_result -- shared exit for the
catalogue-update paths after they have finished writing the new
entry. Two callers: &A314 (the success path) and &A38D (the
no-change path). Never returns directly (clear_result loads A=0
and tail-falls into finalise_and_return).""",
)


d.comment(0xA33D, "Jump to clear A and finalise return", align=Align.INLINE)
d.label(0xA340, "update_cat_position")

d.comment(0xA340, "Y=9: offset for position byte", align=Align.INLINE)
d.comment(0xA342, "Try next slot", align=Align.INLINE)
d.comment(0xA344, "Store in fs_func_code", align=Align.INLINE)
d.comment(0xA347, "Y=5: offset for extent byte", align=Align.INLINE)
d.comment(0xA349, "Load extent byte from FS options", align=Align.INLINE)
d.comment(0xA34B, "Store in fs_data_count", align=Align.INLINE)
d.comment(0xA34E, "X=&0D: byte count", align=Align.INLINE)
d.comment(0xA350, "Store in fs_reply_cmd", align=Align.INLINE)
d.comment(0xA353, "Y=2: command sub-type", align=Align.INLINE)
d.comment(0xA355, "Set V (found match)", align=Align.INLINE)
d.comment(0xA357, "Store in fs_cmd_data", align=Align.INLINE)
d.comment(0xA358, "Store Y to fs_csd_handle", align=Align.INLINE)
d.comment(0xA35A, "Y=3: TX buffer command byte", align=Align.INLINE)
d.comment(0xA35B, "V set: found, skip allocation", align=Align.INLINE)
d.comment(0xA35E, "Allocate FCB slot", align=Align.INLINE)
d.comment(0xA360, "Load data offset from fs_func_code", align=Align.INLINE)
d.comment(0xA363, "Store as first byte of FS options", align=Align.INLINE)
d.comment(0xA365, "Load data count from fs_cmd_data", align=Align.INLINE)
d.comment(0xA368, "Y=9: position offset in FS options", align=Align.INLINE)
d.comment(0xA36A, "Add to current position", align=Align.INLINE)
d.comment(0xA36C, "Store updated position", align=Align.INLINE)
d.comment(0xA36E, "Load TXCB end byte", align=Align.INLINE)
d.comment(0xA370, "Subtract 7 (header overhead)", align=Align.INLINE)
d.comment(0xA372, "Store remaining data size", align=Align.INLINE)
d.comment(0xA375, "Store in fs_load_addr_2 (byte count)", align=Align.INLINE)
d.comment(0xA377, "Zero bytes: skip write", align=Align.INLINE)
d.comment(0xA379, "Write data block to host/tube", align=Align.INLINE)
d.label(0xA37C, "clear_buf_after_write")

d.comment(0xA37C, "X=2: clear 3 bytes (indices 0-2)", align=Align.INLINE)
d.label(0xA37E, "loop_clear_buf")

d.comment(0xA37E, "Clear fs_data_count+X", align=Align.INLINE)
d.comment(0xA381, "Decrement index", align=Align.INLINE)
d.comment(0xA382, "Loop until all cleared", align=Align.INLINE)
d.comment(0xA384, "Update addresses from offset 1", align=Align.INLINE)
d.comment(0xA387, "Set carry for subtraction", align=Align.INLINE)
d.comment(0xA388, "Decrement fs_load_addr_2", align=Align.INLINE)
d.comment(0xA38A, "Load data count from fs_cmd_data", align=Align.INLINE)
d.comment(0xA38D, "Copy to fs_func_code", align=Align.INLINE)
d.comment(0xA390, "Adjust FS options by 4 bytes (subtract)", align=Align.INLINE)
d.comment(0xA393, "X=3: check 4 bytes", align=Align.INLINE)
d.comment(0xA395, "Y=5: starting offset", align=Align.INLINE)
d.comment(0xA397, "Set carry for comparison", align=Align.INLINE)
d.label(0xA398, "loop_check_remaining")

d.comment(0xA398, "Load FS options byte", align=Align.INLINE)
d.comment(0xA39A, "Non-zero: more data remaining", align=Align.INLINE)
d.comment(0xA39C, "Advance to next byte", align=Align.INLINE)
d.comment(0xA39D, "Decrement counter", align=Align.INLINE)
d.comment(0xA39E, "Loop until all bytes checked", align=Align.INLINE)
d.comment(0xA3A0, "All zero: clear carry (transfer complete)", align=Align.INLINE)
d.label(0xA3A1, "done_write_block")

d.comment(0xA3A1, "Jump to update catalogue and return", align=Align.INLINE)
d.label(0xA3A4, "tube_claim_c3")

d.subroutine(
    0xA3A4,
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


d.comment(0xA3A4, "A=&C3: tube claim protocol", align=Align.INLINE)
d.comment(0xA3A6, "Dispatch tube address/data claim", align=Align.INLINE)
d.comment(0xA3A9, "Carry clear: claim failed, retry", align=Align.INLINE)
d.comment(0xA3AB, "Return (tube claimed)", align=Align.INLINE)
d.comment(0xA3AC, "Read current FS station from workspace", align=Align.INLINE)
d.entry(0xA3AC)
d.label(0xA3AC, "cmd_fs")

d.subroutine(
    0xA3AC,
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
d.comment(0xA3AF, "Save in fs_work_5 (so 'no-arg' path can print it)", align=Align.INLINE)
d.comment(0xA3B1, "Read current FS network", align=Align.INLINE)
d.comment(0xA3B4, "Save in fs_work_6", align=Align.INLINE)
d.comment(0xA3B6, "Look at the first command-line byte", align=Align.INLINE)
d.comment(0xA3B8, "Is it CR (no argument)?", align=Align.INLINE)
d.comment(0xA3BA, "Yes: print the current FS address", align=Align.INLINE)
d.comment(0xA3BC, "Parse 'net.station' arg into fs_work_5/6", align=Align.INLINE)
d.comment(0xA3BF, "A=1: OSWORD &13 sub-function 1 = set file server station", align=Align.INLINE)
d.comment(0xA3C1, "Store sub-function in PB[0]", align=Align.INLINE)
d.comment(0xA3C3, "A=&13: OSWORD &13", align=Align.INLINE)
d.comment(0xA3C5, "X = lo of PB pointer (fs_work_4 = &B4)", align=Align.INLINE)
d.comment(0xA3C7, "Y = hi of PB pointer (=0, since fs_work_4 is in zero page)", align=Align.INLINE)
d.comment(0xA3C9, "Tail-jump into OSWORD; the OS routes us back through osword_13_set_station", align=Align.INLINE)
d.label(0xA3CC, "print_current_fs")

d.comment(0xA3CC, "Print 'File server is ' fragment", align=Align.INLINE)
d.label(0xA3CF, "print_fs_info_newline")

d.subroutine(
    0xA3CF,
    "print_fs_info_newline",
    title="Print station address and newline",
    description="""Sets V (suppressing leading-zero padding on
the network number) then prints the station
address followed by a newline via OSNEWL.
Used by *FS and *PS output formatting.""",
    on_exit={"a, x, y": "clobbered (print_station_addr + OSNEWL)"},
)


d.comment(
    0xA3CF,
    "Set V so print_station_addr suppresses the leading '0.' when the network number is zero",
    align=Align.INLINE,
)
d.comment(0xA3D2, "Print the station/network address", align=Align.INLINE)
d.comment(0xA3D5, "Tail-call OSNEWL for the trailing CR/LF", align=Align.INLINE)
d.subroutine(
    0xA3D8,
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


d.comment(0xA3D8, "Save caller's X (command-line offset cursor)", align=Align.INLINE)
d.comment(0xA3D9, "A=0: clear the dot-seen flag for parse_addr_arg", align=Align.INLINE)
d.comment(0xA3DB, "Store cleared dot-seen flag", align=Align.INLINE)
d.comment(0xA3DD, "Parse first number (network or standalone station)", align=Align.INLINE)
d.comment(0xA3E0, "C set: parse_addr_arg saw an empty argument -- skip station storage", align=Align.INLINE)
d.comment(0xA3E2, "Save the network number in fs_work_7", align=Align.INLINE)
d.comment(0xA3E4, "Save Y (current command-line cursor) for after the bridge poll", align=Align.INLINE)
d.comment(0xA3E5, "Populate the bridge routing table -- returns local network number in A", align=Align.INLINE)
d.comment(0xA3E8, "EOR with parsed network: Z set iff parse matched local", align=Align.INLINE)
d.comment(0xA3EA, "Match: keep A=0 to mark local network", align=Align.INLINE)
d.comment(0xA3EC, "Mismatch: A = parsed network number", align=Align.INLINE)
d.label(0xA3EE, "store_station_lo")

d.comment(
    0xA3EE, "Store network number into fs_work_6 (the canonical form: 0=local, non-zero=remote)", align=Align.INLINE
)
d.comment(0xA3F0, "Restore Y", align=Align.INLINE)
d.comment(0xA3F1, "Step Y past the dot separator", align=Align.INLINE)
d.comment(0xA3F2, "Parse station number after the dot", align=Align.INLINE)
d.label(0xA3F5, "skip_if_no_station")

d.comment(0xA3F5, "C set: no station after dot -- leave fs_work_5 alone", align=Align.INLINE)
d.comment(0xA3F7, "Store parsed station in fs_work_5", align=Align.INLINE)
d.comment(0xA3F9, "Restore caller's X", align=Align.INLINE)
d.label(0xA3F9, "no_station_loop")

d.comment(0xA3FA, "Return", align=Align.INLINE)
d.label(0xA3FB, "get_pb_ptr_as_index")

d.subroutine(
    0xA3FB,
    "get_pb_ptr_as_index",
    title="Convert parameter block pointer to table index",
    description="""Reads the first byte from the OSWORD parameter
block pointer and falls through to
byte_to_2bit_index to produce a 12-byte-aligned
table index in Y.""",
    on_exit={"a": "PB[0] (preserved through byte_to_2bit_index)", "y": "byte offset (0, 6, 12, ... up to &42)"},
)


d.comment(
    0xA3FB, "Read PB[0] (the OSWORD sub-function code in most calls); fall into byte_to_2bit_index", align=Align.INLINE
)
d.label(0xA3FD, "byte_to_2bit_index")

d.subroutine(
    0xA3FD,
    "byte_to_2bit_index",
    title="Convert byte to 12-byte-aligned table index",
    description="""Computes Y = A * 6 (via A*12/2) for indexing
into the OSWORD handler workspace tables.
Clamps Y to zero if the result exceeds &48,
preventing out-of-bounds access.""",
    on_entry={"a": "table entry number"},
    on_exit={"y": "byte offset (0, 6, 12, ... up to &42)"},
)


d.comment(0xA3FD, "Multiply A by 2", align=Align.INLINE)
d.comment(0xA3FE, "Multiply A by 2 again -- A is now A_orig * 4", align=Align.INLINE)
d.comment(0xA3FF, "Stash A_orig * 4 on the stack", align=Align.INLINE)
d.comment(0xA400, "Multiply A by 2 -- A is now A_orig * 8 (C = bit 7 of A_orig*4)", align=Align.INLINE)
d.comment(0xA401, "Capture S so we can read the just-pushed value", align=Align.INLINE)
d.comment(0xA402, "Save the C flag from the third ASL", align=Align.INLINE)
d.comment(
    0xA403,
    "ADC stack[X+1] = A_orig*4 (with C from the ASL): A = A_orig*8 + A_orig*4 + C = A_orig*12 + C",
    align=Align.INLINE,
)
d.comment(0xA406, "Halve the result, putting the new C as bit 7", align=Align.INLINE)
d.comment(0xA407, "Restore the saved C (from the third ASL)", align=Align.INLINE)
d.comment(
    0xA408, "ASL doubles the halved value (effectively undoes the ROR's divide while reusing C)", align=Align.INLINE
)
d.comment(0xA409, "Y = A_orig * 12 (the 12-byte-aligned index)", align=Align.INLINE)
d.comment(0xA40A, "Recover A_orig * 4 (left on the stack at &A3FF)", align=Align.INLINE)
d.comment(0xA40B, "Above &48 (i.e. A_orig * 4 >= 72, A_orig >= 18)?", align=Align.INLINE)
d.comment(0xA40D, "No: keep computed Y", align=Align.INLINE)
d.comment(0xA40F, "Yes: clamp Y to 0 (out of range)", align=Align.INLINE)
d.comment(0xA411, "Mirror Y -> A so callers can test Z", align=Align.INLINE)
d.label(0xA412, "rts_2bit_index")

d.comment(0xA412, "Return; Y holds 12-byte-aligned offset, A is non-zero on success", align=Align.INLINE)
d.label(0xA413, "net_1_read_handle")

d.subroutine(
    0xA413,
    "net_1_read_handle",
    title="FS reply: read handle byte (no workspace lookup)",
    description="""Reads the inline handle byte directly from the RX buffer at
`(net_rx_ptr),Y` with `Y=&6F`, then branches into the shared
PB-store path. Used when the caller wants the raw handle byte from
the FS reply rather than the workspace-tracked value.""",
    on_exit={"a": "handle byte from RX buffer"},
)


d.comment(0xA413, "Y=&6F: net_rx_ptr offset for the 'inline' handle byte", align=Align.INLINE)
d.entry(0xA413)
d.comment(0xA415, "Read handle byte directly from RX buffer", align=Align.INLINE)
d.comment(0xA417, "C clear: read-handle path -- store directly to PB", align=Align.INLINE)
d.label(0xA419, "net_2_read_entry")

d.subroutine(
    0xA419,
    "net_2_read_entry",
    title="FS reply: read handle byte from workspace table",
    description="""Calls [`get_pb_ptr_as_index`](label:get_pb_ptr_as_index) to convert the OSWORD
parameter-block pointer to a workspace-table index. On out-of-range
(`C=1`), returns zero. Otherwise reads the handle byte from
`nfs_workspace,Y`; if the slot is `?` (uninitialised marker), falls
through to the zero-return path; otherwise stores the real handle
into PB[0].""",
)


d.comment(0xA419, "Convert PB pointer to workspace table offset", align=Align.INLINE)
d.entry(0xA419)
d.comment(0xA41C, "Out of range: return zero (uninitialised)", align=Align.INLINE)
d.comment(0xA41E, "Read workspace handle byte", align=Align.INLINE)
d.comment(0xA420, "Slot marked '?' (uninitialised)?", align=Align.INLINE)
d.comment(0xA422, "Has a real handle: keep it and store", align=Align.INLINE)
d.label(0xA424, "return_zero_uninit")

d.comment(0xA424, "Force result to zero (uninitialised marker)", align=Align.INLINE)
d.label(0xA426, "store_pb_result")

d.comment(0xA426, "Write into PB[0] (handle return slot)", align=Align.INLINE)
d.comment(0xA428, "Return", align=Align.INLINE)
d.label(0xA429, "net_3_close_handle")

d.subroutine(
    0xA429,
    "net_3_close_handle",
    title="FS reply: close handle entry",
    description="""Calls [`get_pb_ptr_as_index`](label:get_pb_ptr_as_index) to look up the
workspace slot. On out-of-range, marks the workspace as
uninitialised. Otherwise rotates `fs_flags` bit 0 into carry (state
save), reads PB[0] (the handle to close), and proceeds with the
close path.""",
)


d.comment(0xA429, "Convert PB pointer to workspace table offset", align=Align.INLINE)
d.entry(0xA429)

d.comment(0xA42C, "Out of range: mark as uninitialised", align=Align.INLINE)
d.comment(0xA42E, "Shift bit 0 of fs_flags into C (save state)", align=Align.INLINE)
d.comment(0xA431, "Read PB[0] (the handle to close)", align=Align.INLINE)
d.comment(0xA433, "Shift bit 7 of A into C", align=Align.INLINE)
d.comment(0xA434, "Restore C into bit 0 of fs_flags", align=Align.INLINE)
d.comment(0xA437, "Return; the close action is dispatched elsewhere based on the saved C state", align=Align.INLINE)
d.label(0xA438, "mark_ws_uninit")

d.comment(0xA438, "Save bit 0 of econet_flags", align=Align.INLINE)
d.comment(0xA43B, "A='?': uninitialised marker", align=Align.INLINE)
d.comment(0xA43D, "Write '?' to workspace[Y] (the slot is now free)", align=Align.INLINE)
d.comment(0xA43F, "Restore bit 0 of econet_flags", align=Align.INLINE)
d.comment(0xA442, "Return", align=Align.INLINE)
d.label(0xA443, "fscv_3_star_cmd")

d.subroutine(
    0xA443,
    "fscv_3_star_cmd",
    title="FSCV reason 3: process *<command> via FS",
    description="""Sets up text and transfer pointers via set_text_and_xfer_ptr, marks
spool / Tube state as inactive (fs_spool_handle = need_release_tube
= &FF), then calls match_fs_cmd with X=&35, Y=0 to look up the user's
text in the FS command table. The match-or-error result feeds into
the FS dispatch chain that follows. Single caller (the FSCV vector
table at &8CFA).""",
)


d.comment(0xA443, "Set text/transfer pointers from FS context", align=Align.INLINE)
d.entry(0xA443)
d.comment(0xA446, "Y=&FF -- mark spool/Tube state inactive", align=Align.INLINE)
d.comment(0xA448, "Store fs_spool_handle = &FF", align=Align.INLINE)
d.comment(0xA44A, "Store need_release_tube = &FF", align=Align.INLINE)
d.comment(0xA44D, "X=&35: NFS-commands sub-table offset", align=Align.INLINE)
d.comment(0xA44F, "Match against the NFS sub-table", align=Align.INLINE)
d.comment(0xA452, "C set: no match -> dispatch via fall-through", align=Align.INLINE)
d.label(0xA454, "cmd_fs_reentry")

d.subroutine(
    0xA454,
    "cmd_fs_reentry",
    title="FS-command re-entry guard (BVC dispatch_fs_cmd)",
    description="""Single-instruction prologue: BVC dispatch_fs_cmd. Reached as the
fall-through target after a *RUN failure -- if V is clear (the
re-entry path is permitted) it branches into dispatch_fs_cmd to
re-attempt the command; otherwise falls through to error_syntax to
raise 'Syntax'. Single caller (the FS dispatch table at &8C4E).""",
)


d.comment(0xA454, "V clear: re-enter dispatch_fs_cmd", align=Align.INLINE)
d.label(0xA456, "error_syntax")

d.comment(0xA456, "Error code &DC", align=Align.INLINE)
d.comment(0xA458, "Raise 'Syntax' error", align=Align.INLINE)
d.label(0xA462, "dispatch_fs_cmd")

d.comment(0xA462, "A=0: clear svc_state", align=Align.INLINE)
d.comment(0xA464, "Store -> svc_state", align=Align.INLINE)
d.comment(0xA466, "Load dispatch hi byte from cmd_dispatch_hi_table+X", align=Align.INLINE)
d.comment(0xA469, "Push hi for RTS dispatch", align=Align.INLINE)
d.comment(0xA46A, "Load dispatch lo byte from cmd_dispatch_lo_table+X", align=Align.INLINE)
d.comment(0xA46D, "Push lo for RTS dispatch", align=Align.INLINE)
d.comment(0xA46E, "RTS -> dispatched command handler", align=Align.INLINE)
d.label(0xA46F, "match_fs_cmd")

d.subroutine(
    0xA46F,
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


d.comment(0xA46F, "Save command-line offset Y on stack", align=Align.INLINE)
d.comment(0xA470, "Push for save/restore", align=Align.INLINE)
d.label(0xA471, "restart_table_scan")

d.comment(0xA471, "Reload saved Y (peek without popping)", align=Align.INLINE)
d.comment(0xA472, "Push it back to keep on stack", align=Align.INLINE)
d.comment(0xA473, "Y = saved command-line offset", align=Align.INLINE)
d.comment(0xA474, "First char of current entry name", align=Align.INLINE)
d.comment(0xA477, "Bit 7 set already: end of table", align=Align.INLINE)
d.label(0xA479, "loop_match_char")

d.comment(0xA479, "Next char from table", align=Align.INLINE)
d.comment(0xA47C, "Bit 7 set: name fully matched", align=Align.INLINE)
d.comment(0xA480, "Mask off case bit (5)", align=Align.INLINE)
d.comment(0xA482, "Mismatch (after case mask): skip entry", align=Align.INLINE)
d.comment(0xA484, "Advance command-line offset", align=Align.INLINE)
d.comment(0xA485, "Advance table offset", align=Align.INLINE)
d.comment(0xA486, "ALWAYS branch: continue matching", align=Align.INLINE)
d.label(0xA488, "skip_entry_chars")

d.comment(0xA488, "Skip remaining name chars", align=Align.INLINE)
d.comment(0xA489, "Load next table byte", align=Align.INLINE)
d.comment(0xA48C, "Bit 7 clear: continue skipping", align=Align.INLINE)
d.comment(0xA48E, "Char on command line at current Y", align=Align.INLINE)
d.comment(0xA490, "Is it `.` (abbreviation)?", align=Align.INLINE)
d.comment(0xA492, "Yes: accept abbreviated match", align=Align.INLINE)
d.label(0xA494, "loop_skip_to_next")

d.comment(0xA494, "Skip 3-byte handler trailer (flag, lo, hi)", align=Align.INLINE)
d.comment(0xA495, "(continued)", align=Align.INLINE)
d.comment(0xA496, "(continued)", align=Align.INLINE)
d.comment(0xA497, "ALWAYS branch: try next entry", align=Align.INLINE)
d.label(0xA499, "check_separator")

d.comment(0xA499, "Save matched-name length on stack", align=Align.INLINE)
d.comment(0xA49A, "Push for stack-based comparison", align=Align.INLINE)
d.comment(0xA49B, "Char on command line just past name", align=Align.INLINE)
d.comment(0xA49D, "Y=9: separator-table size - 1", align=Align.INLINE)
d.label(0xA49F, "loop_check_sep_table")

d.comment(0xA49F, "Compare with separator", align=Align.INLINE)
d.comment(0xA4A2, "Match: valid command boundary", align=Align.INLINE)
d.comment(0xA4A4, "Try next separator", align=Align.INLINE)
d.comment(0xA4A5, "Loop through 10 separators", align=Align.INLINE)
d.comment(0xA4A7, "Restore matched-name length", align=Align.INLINE)
d.comment(0xA4A8, "A = matched offset, save in Y", align=Align.INLINE)
d.comment(0xA4A9, "ALWAYS branch: try next entry", align=Align.INLINE)
d.label(0xA4AB, "sep_table_data")

d.comment(0xA4AB, "Dispatch helper (sep_table_data path)", align=Align.INLINE)
d.comment(0xA4AE, "Check separator flag (zp_0026)", align=Align.INLINE)
d.comment(0xA4B2, "Effective unconditional jump", align=Align.INLINE)
d.comment(0xA4B3, "CR (carriage return)", align=Align.INLINE)
d.label(0xA4B4, "separator_char_table")

d.comment(0xA4B4, "Restore matched-name length", align=Align.INLINE)
d.comment(0xA4B5, "Y = matched-name length", align=Align.INLINE)
d.label(0xA4B6, "loop_skip_trail_spaces")

d.subroutine(
    0xA4B6,
    "loop_skip_trail_spaces",
    title="Skip trailing spaces from FS command-line args",
    description="""Reads (fs_crc_lo),Y; on space, falls through to the per-char
advance; non-space exits to check_cmd_flags. Shared body with
skip_dot_and_spaces at &A4A8 (alt-entry that also accepts dots).
Single caller (the BNE retry at &A4A9).""",
    on_entry={"y": "current command-line offset"},
)


d.comment(0xA4B6, "Char on command line at current Y", align=Align.INLINE)
d.comment(0xA4B8, "Is it space?", align=Align.INLINE)
d.comment(0xA4BA, "No: check the entry's no-arg flag", align=Align.INLINE)
d.label(0xA4BC, "skip_dot_and_spaces")

d.comment(0xA4BC, "Advance past the space (or `.`)", align=Align.INLINE)
d.comment(0xA4BD, "Loop: keep skipping", align=Align.INLINE)
d.label(0xA4C0, "check_cmd_flags")

d.comment(0xA4C0, "Load entry's flag byte (post-name)", align=Align.INLINE)
d.comment(0xA4C3, "Shift bit 7 into C: the no-arg bit", align=Align.INLINE)
d.comment(0xA4C4, "C=0: entry allows arguments", align=Align.INLINE)
d.comment(0xA4C6, "Char on command line", align=Align.INLINE)
d.comment(0xA4C8, "Is it CR (no argument)?", align=Align.INLINE)
d.comment(0xA4CA, "Argument present, V clear", align=Align.INLINE)
d.comment(0xA4CC, "Force V=1: entry validated as match", align=Align.INLINE)
d.comment(0xA4CF, "V set: skip the CLV", align=Align.INLINE)
d.label(0xA4D1, "clear_v_flag")

d.comment(0xA4D1, "Clear V (no-arg flag not asserted)", align=Align.INLINE)
d.label(0xA4D2, "clear_c_flag")

d.comment(0xA4D2, "Clear C (no error / no-arg path)", align=Align.INLINE)
d.label(0xA4D3, "return_with_result")

d.comment(0xA4D3, "Discard saved Y on stack", align=Align.INLINE)
d.comment(0xA4D4, "A = current command-line char", align=Align.INLINE)
d.comment(0xA4D6, "Return (Z=1 on match, C and V set per result)", align=Align.INLINE)
d.label(0xA4D7, "loop_scan_past_word")

d.comment(0xA4D7, "Advance command-line offset", align=Align.INLINE)
d.label(0xA4D8, "check_char_type")

d.comment(0xA4D8, "Char on command line", align=Align.INLINE)
d.comment(0xA4DA, "Is it CR (end of input)?", align=Align.INLINE)
d.comment(0xA4DC, "Yes: set C and return (no match)", align=Align.INLINE)
d.comment(0xA4DE, "Is it `.`?", align=Align.INLINE)
d.comment(0xA4E0, "Yes: skip separator spaces", align=Align.INLINE)
d.comment(0xA4E2, "Is it space?", align=Align.INLINE)
d.comment(0xA4E4, "No: keep scanning past word", align=Align.INLINE)
d.label(0xA4E6, "skip_sep_spaces")

d.comment(0xA4E6, "Advance past space", align=Align.INLINE)
d.comment(0xA4E7, "Load next char", align=Align.INLINE)
d.comment(0xA4E9, "Still space?", align=Align.INLINE)
d.comment(0xA4EB, "Yes: keep skipping", align=Align.INLINE)
d.label(0xA4ED, "set_c_and_return")

d.comment(0xA4ED, "Set C: signal no-match return path", align=Align.INLINE)
d.comment(0xA4EE, "ALWAYS branch to common return", align=Align.INLINE)
d.comment(0xA4F0, "Test fs_flags bit 6", align=Align.INLINE)
d.label(0xA4F0, "check_urd_present")

d.comment(0xA4F3, "Bit 6 set: take fscv_2_star_run", align=Align.INLINE)
d.comment(0xA4F5, "Bit 6 clear: raise 'Bad command'", align=Align.INLINE)
d.label(0xA4F8, "fscv_2_star_run")

d.subroutine(
    0xA4F8,
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


d.comment(0xA4F8, "Save text pointer (for GSREAD-driven parsing)", align=Align.INLINE)
d.entry(0xA4F8)
d.comment(0xA4FB, "Reset fs_lib_flags low bits to 5-bit access mask", align=Align.INLINE)
d.comment(0xA4FE, "Set bit 1 of A (mark *RUN-style invocation)", align=Align.INLINE)
d.comment(0xA500, "Update hazel_fs_lib_flags with the result", align=Align.INLINE)
d.subroutine(
    0xA505,
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


d.comment(0xA505, "Save current OS text pointer", align=Align.INLINE)
d.comment(0xA508, "Mask access bits", align=Align.INLINE)
d.comment(0xA50B, "Clear bit 1 of mask", align=Align.INLINE)
d.comment(0xA50D, "Save into fs_lib_flags", align=Align.INLINE)
d.label(0xA510, "cmd_run_load_mask")

d.comment(0xA510, "Begin parsing the *RUN argument", align=Align.INLINE)
d.label(0xA513, "open_file_for_run")

d.comment(0xA513, "X=1: TX-buffer write index for argument", align=Align.INLINE)
d.comment(0xA515, "Copy argument to TX buffer", align=Align.INLINE)
d.comment(0xA518, "A=2: open-input mode for OSFIND", align=Align.INLINE)
d.comment(0xA51A, "Next byte down", align=Align.INLINE)
d.comment(0xA51D, "Y=&12: cmd code for *RUN", align=Align.INLINE)
d.comment(0xA51F, "Send the request and wait for reply", align=Align.INLINE)
d.comment(0xA522, "Read reply status from TX[5]", align=Align.INLINE)
d.comment(0xA525, "Compare with 1 (not-found)", align=Align.INLINE)
d.comment(0xA527, "Loop until all 6 restored", align=Align.INLINE)
d.comment(0xA529, "Return from svc_8_osword", align=Align.INLINE)
d.label(0xA52B, "loop_check_handles")

d.comment(0xA52B, "Increment handle byte", align=Align.INLINE)
d.comment(0xA52E, "Load handler address low byte", align=Align.INLINE)
d.comment(0xA530, "Non-zero: handle valid, execute", align=Align.INLINE)
d.label(0xA533, "alloc_run_fcb")

d.comment(0xA533, "Decrement X (post-find adjustment)", align=Align.INLINE)
d.comment(0xA534, "Loop while X >= 0 (scan all 4 handle slots)", align=Align.INLINE)
d.comment(0xA536, "RTS dispatches to pushed handler", align=Align.INLINE)
d.comment(0xA539, "X=1: target offset for the *RUN-channel command", align=Align.INLINE)
d.comment(0xA53B, "Store X to hazel_txcb_data (cmd byte)", align=Align.INLINE)
d.comment(0xA53E, "Store X to hazel_txcb_flag (cmd flag)", align=Align.INLINE)
d.comment(0xA541, "X=2", align=Align.INLINE)
d.comment(0xA542, "Copy filename arg into TX buffer", align=Align.INLINE)
d.comment(0xA545, "Test station active flag", align=Align.INLINE)
d.comment(0xA547, "Send re-open request", align=Align.INLINE)
d.comment(0xA54A, "C set: error from save_net_tx_cb -- abort *RUN", align=Align.INLINE)
d.comment(0xA54C, "Yes: handle clock read", align=Align.INLINE)
d.label(0xA54F, "done_run_dispatch")

d.comment(0xA54F, "Jump to finalise and return", align=Align.INLINE)
d.label(0xA552, "try_library_path")

d.comment(0xA552, "Return", align=Align.INLINE)
d.comment(0xA555, "Y=&10: length of TXCB to save", align=Align.INLINE)
d.comment(0xA557, "Save current TX control block", align=Align.INLINE)
d.comment(0xA559, "Load library flag byte", align=Align.INLINE)
d.comment(0xA55C, "Bit 7 set: library already tried", align=Align.INLINE)
d.comment(0xA55E, "Shift bit 7 into carry", align=Align.INLINE)
d.comment(0xA560, "Store BCD seconds", align=Align.INLINE)
d.comment(0xA562, "Carry set: bad command", align=Align.INLINE)
d.comment(0xA564, "X=&FF -- start scan from end", align=Align.INLINE)
d.label(0xA566, "loop_find_name_end")

d.comment(0xA566, "Convert binary to BCD", align=Align.INLINE)
d.comment(0xA567, "Load filename byte", align=Align.INLINE)
d.comment(0xA56A, "Compare with CR (terminator)", align=Align.INLINE)
d.comment(0xA56C, "Load hours from clock workspace", align=Align.INLINE)
d.label(0xA56E, "loop_shift_name_right")

d.comment(0xA56E, "Shift filename right by 8 bytes", align=Align.INLINE)
d.comment(0xA571, "Store shifted byte", align=Align.INLINE)
d.comment(0xA574, "Decrement scan index", align=Align.INLINE)
d.comment(0xA575, "Clear hours high position", align=Align.INLINE)
d.comment(0xA577, "Store zero", align=Align.INLINE)
d.label(0xA579, "loop_copy_lib_prefix")

d.comment(0xA579, "Copy 'Library.' prefix", align=Align.INLINE)
d.comment(0xA57C, "Store prefix byte", align=Align.INLINE)
d.comment(0xA57F, "Decrement scan index", align=Align.INLINE)
d.comment(0xA580, "Loop until prefix copied", align=Align.INLINE)
d.comment(0xA582, "Load library flag", align=Align.INLINE)
d.comment(0xA585, "Mark byte as 'argument'", align=Align.INLINE)
d.comment(0xA587, "Restore day+month byte", align=Align.INLINE)
d.label(0xA58A, "retry_with_library")

d.comment(0xA58A, "Retry file open with library path", align=Align.INLINE)
d.label(0xA58C, "restore_filename")

d.comment(0xA58C, "X=&FF -- restart scan from end", align=Align.INLINE)
d.label(0xA58E, "loop_restore_name")

d.comment(0xA58E, "Store BCD month", align=Align.INLINE)
d.comment(0xA58F, "Load backup byte", align=Align.INLINE)
d.comment(0xA592, "Shift high nibble down", align=Align.INLINE)
d.comment(0xA595, "4th shift: isolate high nibble", align=Align.INLINE)
d.comment(0xA597, "No: continue restoring", align=Align.INLINE)
d.comment(0xA599, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xA59C, "Mark caller's flags", align=Align.INLINE)
d.comment(0xA59E, "Copy 7 bytes (Y=6 down to 0)", align=Align.INLINE)
d.label(0xA5A3, "library_tried")

d.comment(0xA5A3, "Store to parameter block", align=Align.INLINE)
d.comment(0xA5A6, "Loop for all 7 bytes", align=Align.INLINE)
d.comment(0xA5A8, "Test hazel_fs_lib_flags bits 6 / 7", align=Align.INLINE)
d.comment(0xA5AB, "Either bit set: this is an invalid command path", align=Align.INLINE)
d.comment(0xA5AD, "Otherwise finalise and return", align=Align.INLINE)
d.comment(0xA5B0, "A=&0B: FSCV reason 11 (filing-system change)", align=Align.INLINE)
d.comment(0xA5B2, "Tail-call FSCV", align=Align.INLINE)
d.subroutine(
    0xA5B5,
    "error_bad_command",
    title="Raise 'Bad command' BRK error",
    description="""Loads error code &FE and tail-calls error_bad_inline with the inline
string 'command' -- error_bad_inline prepends 'Bad ' to produce the
final 'Bad command' message. Used by the FS command parser when no
table entry matches the user's input. Never returns.""",
)


d.comment(0xA5B5, "Error code &FE", align=Align.INLINE)
d.comment(0xA5B7, "Raise 'Bad command' error", align=Align.INLINE)
d.label(0xA5C2, "check_exec_addr")

d.subroutine(
    0xA5C2,
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


d.comment(0xA5C2, "X=3: check 4 execution bytes", align=Align.INLINE)
d.label(0xA5C4, "loop_check_exec_bytes")

d.comment(0xA5C4, "Increment execution address byte", align=Align.INLINE)
d.comment(0xA5C7, "Low byte = &6F", align=Align.INLINE)
d.comment(0xA5C9, "Set osword_flag", align=Align.INLINE)
d.comment(0xA5CA, "Loop until all checked", align=Align.INLINE)
d.comment(0xA5CC, "A=&93: error code 'Bad command'", align=Align.INLINE)
d.comment(0xA5CE, "Generate 'No!' error", align=Align.INLINE)
d.label(0xA5D7, "alloc_run_channel")

d.subroutine(
    0xA5D7,
    "alloc_run_channel",
    title="Allocate FCB slot for *RUN target file",
    description="""Loads the saved OSWORD parameter byte at hazel_txcb_data, calls alloc_fcb_slot
to obtain a free channel index in A, transfers it into Y, then
clears the per-channel attribute byte at hazel_fcb_status,X. Used by the
*RUN argument-handling path at &A54C once the file is opened, to
reserve a channel for the running program.""",
    on_exit={"a": "channel attribute byte (cleared to 0)", "x": "FCB slot index", "y": "FCB slot index (copy of X)"},
)


d.comment(0xA5D7, "Set workspace pointer high", align=Align.INLINE)
d.comment(0xA5DA, "Allocate FCB slot", align=Align.INLINE)
d.comment(0xA5DD, "A = parsed character", align=Align.INLINE)
d.comment(0xA5DE, "Y=OSWORD flag (slot specifier)", align=Align.INLINE)
d.comment(0xA5E0, "Clear status in channel table", align=Align.INLINE)
d.comment(0xA5E3, "A=3: start searching from slot 3", align=Align.INLINE)
d.comment(0xA5E6, "Y=3: skip past 3-byte FS header", align=Align.INLINE)
d.comment(0xA5E8, "C set: slot invalid, store result", align=Align.INLINE)
d.index_base(0xA5EB, "library_dir_prefix")

d.comment(0xA5EB, "Continue shift", align=Align.INLINE)
# UNMAPPED: d.label(0xA5DF, "library_path_string")

# UNMAPPED: d.comment(0xA5DF, "Copy parsed arg to TX buffer with X=0", align=Align.INLINE)
d.comment(0xA5F6, "Y=0", align=Align.INLINE)
d.comment(0xA5F8, "For the loop entry", align=Align.INLINE)
d.comment(0xA5F9, "Transfer found slot to A", align=Align.INLINE)
d.label(0xA5FC, "loop_read_gs_string")

d.comment(0xA5FC, "Store slot number to PB byte 0", align=Align.INLINE)
d.comment(0xA5FF, "Always (BCC after CLC) loop back", align=Align.INLINE)
d.comment(0xA601, "C set: slot invalid, store result", align=Align.INLINE)
d.label(0xA602, "loop_skip_trailing")

d.comment(0xA602, "Advance Y past trailing space", align=Align.INLINE)
d.comment(0xA603, "Y=Y-1: adjust workspace offset", align=Align.INLINE)
d.comment(0xA605, "Is it space?", align=Align.INLINE)
d.comment(0xA607, "Yes: skip it", align=Align.INLINE)
d.comment(0xA609, "Test for CR (terminator)", align=Align.INLINE)
d.comment(0xA60B, "Clear C for arithmetic", align=Align.INLINE)
d.comment(0xA60C, "Compare Y with OSWORD flag", align=Align.INLINE)
d.comment(0xA60D, "Add to text pointer low", align=Align.INLINE)
d.comment(
    0xA60F, "Store low byte of (os_text_ptr + Y) -> fs_crc_lo (repurposed as a generic pointer)", align=Align.INLINE
)
d.comment(0xA611, "Load os_text_ptr_hi for the high-byte add", align=Align.INLINE)
d.comment(0xA613, "Add carry from low add (no extra increment)", align=Align.INLINE)
d.comment(0xA615, "Store result high byte -> fs_crc_hi", align=Align.INLINE)
d.comment(0xA617, "Save text pointer for later", align=Align.INLINE)
d.comment(0xA61A, "X=&C0: pointer-to-options high byte", align=Align.INLINE)
d.comment(0xA61C, "Y=1: workspace flag offset", align=Align.INLINE)
d.comment(0xA61E, "Store pending marker to workspace", align=Align.INLINE)
d.comment(0xA620, "Store as fs_options", align=Align.INLINE)
d.comment(0xA622, "Increment retry counter", align=Align.INLINE)
d.comment(0xA625, "X=&4A: FS command table offset", align=Align.INLINE)
d.comment(0xA627, "Store result A to PB via Y", align=Align.INLINE)
d.comment(0xA629, "Rotate Econet flags back (restore state)", align=Align.INLINE)
d.comment(0xA62C, "Return from OSWORD 11 handler", align=Align.INLINE)
d.comment(0xA62F, "Store to ws_ptr_lo", align=Align.INLINE)
d.comment(0xA631, "Y=&7F: last byte of RX buffer", align=Align.INLINE)
d.comment(0xA637, "All &FF?", align=Align.INLINE)
d.comment(0xA639, "X-1: adjust count", align=Align.INLINE)
d.comment(0xA63B, "Claim tube for data transfer", align=Align.INLINE)
d.comment(0xA63E, "X=9: parameter count", align=Align.INLINE)
d.comment(0xA640, "Y=&C1: high byte of TX buffer pointer", align=Align.INLINE)
d.comment(0xA642, "A=4: option byte for *RUN", align=Align.INLINE)
d.comment(0xA644, "Relocated execute path", align=Align.INLINE)
d.label(0xA647, "dispatch_via_vector")

d.comment(0xA647, "A=1: dispatch flag", align=Align.INLINE)
d.comment(0xA649, "Indirect jump via workspace vector", align=Align.INLINE)
d.label(0xA64C, "fsreply_3_set_csd")

d.subroutine(
    0xA64C,
    "fsreply_3_set_csd",
    title="FS reply handler: select CSD station",
    description="""Single-instruction wrapper: JSR find_station_bit3 to record the
new current-selected-directory (CSD) station in the table, then
JMP return_with_last_flag to clean up and return. Single caller
(the FS reply dispatch at &9599).""",
    on_exit={"a": "fs_last_byte_flag (loaded by return_with_last_flag)"},
)


d.comment(0xA64C, "Find station-bit-3 entry", align=Align.INLINE)
d.entry(0xA64C)
d.label(0xA652, "fsreply_5_set_lib")

d.subroutine(
    0xA652,
    "fsreply_5_set_lib",
    title="FS reply handler: set library station",
    description="""Two-instruction wrapper: `JSR
`[`flip_set_station_boot`](label:flip_set_station_boot) to record the new library
station, then `JMP`
[`return_with_last_flag`](label:return_with_last_flag). Reached only via the FS
reply dispatch table.""",
)


d.comment(0xA652, "Record library station in station table", align=Align.INLINE)
d.entry(0xA652)
d.label(0xA658, "find_station_bit2")

d.subroutine(
    0xA658,
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


d.comment(0xA658, "X=&10: scan 16 entries", align=Align.INLINE)
d.comment(0xA65A, "Clear V (no-match marker)", align=Align.INLINE)
d.label(0xA65B, "loop_search_stn_bit2")

d.comment(0xA65B, "Step to previous entry", align=Align.INLINE)
d.comment(0xA65C, "Below 0: scan complete", align=Align.INLINE)
d.comment(0xA65E, "Compare entry X's stn/net with caller's", align=Align.INLINE)
d.comment(0xA661, "No match: continue", align=Align.INLINE)
d.comment(0xA663, "Match: read entry's flag byte at hazel_fcb_status+X", align=Align.INLINE)
d.comment(0xA666, "Mask bit 2", align=Align.INLINE)
d.comment(0xA668, "Bit 2 clear: keep scanning", align=Align.INLINE)
d.comment(0xA66A, "Bit 2 set: A = matched entry index (Y)", align=Align.INLINE)
d.comment(0xA66B, "Store Y at hazel_fcb_slot_attr+X (link entry to slot)", align=Align.INLINE)
d.comment(0xA66E, "BIT always_set_v_byte: V <- 1 (match found)", align=Align.INLINE)
d.label(0xA671, "done_search_bit2")

d.comment(0xA671, "Save Y at hazel_fs_saved_station (matched entry index)", align=Align.INLINE)
d.comment(0xA674, "V set: skip new-slot alloc", align=Align.INLINE)
d.comment(0xA676, "A = caller's index", align=Align.INLINE)
d.comment(0xA677, "Allocate a fresh FCB slot", align=Align.INLINE)
d.comment(0xA67A, "Save FCB slot index at hazel_fcb_slot_1", align=Align.INLINE)
d.comment(0xA67D, "Z set: alloc failed -> restore FS context", align=Align.INLINE)
d.label(0xA67F, "set_flags_bit2")

d.comment(0xA67F, "A=&26: workspace flag for bit 2 search", align=Align.INLINE)
d.label(0xA683, "find_station_bit3")

d.subroutine(
    0xA683,
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


d.comment(0xA683, "X=&10: scan 16 entries", align=Align.INLINE)
d.comment(0xA685, "Clear V (no-match marker)", align=Align.INLINE)
d.label(0xA686, "loop_search_stn_bit3")

d.comment(0xA686, "Step to previous entry", align=Align.INLINE)
d.comment(0xA687, "Below 0: scan complete", align=Align.INLINE)
d.comment(0xA689, "Compare entry's stn/net with caller's", align=Align.INLINE)
d.comment(0xA68C, "No match: continue", align=Align.INLINE)
d.comment(0xA68E, "Match: read entry's flag byte at hazel_fcb_status+X", align=Align.INLINE)
d.comment(0xA691, "Mask bit 3", align=Align.INLINE)
d.comment(0xA693, "Bit 3 clear: keep scanning", align=Align.INLINE)
d.comment(0xA695, "Bit 3 set: A = matched entry index (Y)", align=Align.INLINE)
d.comment(0xA696, "Store Y at hazel_fcb_slot_attr+X (link entry to slot)", align=Align.INLINE)
d.comment(0xA699, "BIT always_set_v_byte: V <- 1 (match found)", align=Align.INLINE)
d.label(0xA69C, "done_search_bit3")

d.comment(0xA69C, "Save Y at hazel_fs_context_copy (matched entry index)", align=Align.INLINE)
d.comment(0xA69F, "V set: skip new-slot alloc", align=Align.INLINE)
d.comment(0xA6A1, "A = caller's index", align=Align.INLINE)
d.comment(0xA6A2, "Allocate a fresh FCB slot", align=Align.INLINE)
d.comment(0xA6A5, "Save FCB slot index at hazel_fcb_slot_2", align=Align.INLINE)
d.comment(0xA6A8, "Z set: alloc failed -> restore FS context", align=Align.INLINE)
d.label(0xA6AA, "set_flags_bit3")

d.comment(0xA6AA, "A=&2A: workspace flag for bit 3 search", align=Align.INLINE)
d.entry(0xA6AE)
d.label(0xA6AE, "cmd_flip")

d.subroutine(
    0xA6AE,
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


d.comment(0xA6AE, "Load current CSD handle", align=Align.INLINE)
d.comment(0xA6B1, "Save CSD handle", align=Align.INLINE)
d.comment(0xA6B2, "Load library handle into Y", align=Align.INLINE)
d.comment(0xA6B5, "Install library as new CSD", align=Align.INLINE)
d.comment(0xA6B8, "Restore original CSD handle", align=Align.INLINE)
d.comment(0xA6B9, "Y = original CSD (becomes library)", align=Align.INLINE)
d.label(0xA6BA, "flip_set_station_boot")

d.subroutine(
    0xA6BA,
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


d.comment(0xA6BA, "X=&10: max 16 station entries", align=Align.INLINE)
d.comment(0xA6BC, "Clear V (no match found yet)", align=Align.INLINE)
d.label(0xA6BD, "loop_search_stn_boot")

d.comment(0xA6BD, "Decrement station index", align=Align.INLINE)
d.comment(0xA6BE, "All searched: exit loop", align=Align.INLINE)
d.comment(0xA6C0, "Check if station[X] matches", align=Align.INLINE)
d.comment(0xA6C3, "No match: try next station", align=Align.INLINE)
d.comment(0xA6C5, "Load station flags byte", align=Align.INLINE)
d.comment(0xA6C8, "Test bit 4 (active flag)", align=Align.INLINE)
d.comment(0xA6CA, "Not active: try next station", align=Align.INLINE)
d.comment(0xA6CC, "Transfer boot type to A", align=Align.INLINE)
d.comment(0xA6CD, "Store boot setting for station", align=Align.INLINE)
d.comment(0xA6D0, "Set V flag (station match found)", align=Align.INLINE)
d.label(0xA6D3, "done_search_boot")

d.comment(0xA6D3, "Store boot type", align=Align.INLINE)
d.comment(0xA6D6, "V set (matched): skip allocation", align=Align.INLINE)
d.comment(0xA6D8, "Boot type to A", align=Align.INLINE)
d.comment(0xA6D9, "Allocate FCB slot for new entry", align=Align.INLINE)
d.comment(0xA6DC, "Store allocation result", align=Align.INLINE)
d.comment(0xA6DF, "Zero: allocation failed, exit", align=Align.INLINE)
d.label(0xA6E1, "set_flags_boot")

d.comment(0xA6E1, "A=&32: station flags (active+boot)", align=Align.INLINE)
d.label(0xA6E3, "store_stn_flags_restore")

d.comment(0xA6E3, "Store station flags", align=Align.INLINE)
d.label(0xA6E6, "jmp_restore_fs_ctx")

d.comment(0xA6E6, "Restore FS context and return", align=Align.INLINE)
d.label(0xA6E9, "fsreply_1_boot")

d.subroutine(
    0xA6E9,
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
[`boot_persist_fs_maybe`](label:boot_persist_fs_maybe) at `&A730`, which
tests the recovered boot-type byte against `2` to decide whether
to call OSBYTE `&6D`. Anyone following the stack across this
fall-through should look past `fsreply_2_copy_handles` and
`boot_try_findlib` to find the pop.""",
)


d.entry(0xA6E9)
d.comment(0xA6E9, "Close all network channels", align=Align.INLINE)
d.comment(0xA6EC, "A=&40: bit-6 mask for fs_flags (boot-pending flag)", align=Align.INLINE)
d.comment(0xA6EE, "Set boot-pending bit on fs_flags (TSB = test-and-set)", align=Align.INLINE)
d.comment(0xA6F1, "C=1: signal boot-pending to fsreply_2_copy_handles (its BCS at &A6F9 takes the boot path)", align=Align.INLINE)
d.comment(0xA6F2, "Load boot-type byte from FS reply (hazel_txcb_result)", align=Align.INLINE)
d.comment(0xA6F5, "Store boot type as hazel_fs_flags (consumed later by boot_select_cmd)", align=Align.INLINE)
d.comment(0xA6F8, "Push boot-type byte (popped later by boot_persist_fs_maybe at &A730)", align=Align.INLINE)
d.label(0xA6F9, "fsreply_2_copy_handles")

d.subroutine(
    0xA6F9,
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
  the dispatcher arrives with Carry clear, so `BCS` at `&A6F9`
  is not taken and the routine exits via
  `JMP return_with_last_flag` without ever reaching the `PLA`
  at `&A730`. The stack contract is satisfied trivially.
- **Fall-through from [`fsreply_1_boot`](label:fsreply_1_boot)** —
  fsreply_1_boot pushes A (the boot-type byte) and `SEC`s
  before falling in, so `BCS` is taken and the boot path runs;
  the `PLA` at `&A730` then pops the boot-type byte cleanly.

Direct dispatch with Carry set is not part of the contract;
the boot path requires the pre-pushed A from fsreply_1_boot.""",
    on_entry={
        "a": "boot-type byte (pushed by fsreply_1_boot when arriving via fall-through; ignored on direct-dispatch C-clear path)",
        "carry": "set when boot processing should follow (only legal via fsreply_1_boot fall-through)",
    },
)


d.entry(0xA6F9)
d.comment(0xA6F9, "Save processor status", align=Align.INLINE)
d.comment(0xA6FA, "Load station number from reply", align=Align.INLINE)
d.comment(0xA6FD, "Find station entry with bit 2", align=Align.INLINE)
d.comment(0xA700, "Load network number from reply", align=Align.INLINE)
d.comment(0xA703, "Find station entry with bit 3", align=Align.INLINE)
d.comment(0xA706, "Load boot type from reply", align=Align.INLINE)
d.comment(0xA709, "Set boot config for station", align=Align.INLINE)
d.comment(0xA70C, "Restore processor status", align=Align.INLINE)
d.comment(0xA70D, "Carry set: proceed with boot", align=Align.INLINE)
d.comment(0xA70F, "Return with last flag", align=Align.INLINE)
d.label(0xA712, "findlib_oscli_cmd")
d.banner(
    0xA712,
    title="OSCLI command string '-NET-FindLib'<CR>",
    description="""Passed to OSCLI by [`boot_try_findlib`](label:boot_try_findlib). The
`-NET-` prefix is the MOS hyphen-bracketed FS-selector form —
see that subroutine's description for the convention and why
it's used here rather than a plain `*FindLib`.""",
)


d.subroutine(
    0xA71F,
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


d.comment(0xA71F, "X=&11: CMOS RAM byte index", align=Align.INLINE)
d.comment(0xA721, "Read CMOS &11 via osbyte_a1", align=Align.INLINE)
d.comment(0xA724, "Result to A", align=Align.INLINE)
d.comment(0xA725, "Mask bit 1 (auto-CLI flag)", align=Align.INLINE)
d.comment(0xA727, "Bit clear: skip auto-CLI", align=Align.INLINE)
# UNMAPPED: d.expr(0xA716, "<findlib_oscli_cmd")
# UNMAPPED: d.expr(0xA718, ">findlib_oscli_cmd")
d.comment(0xA72D, "OSCLI '-NET-FindLib': dispatch to NFS via FSCV,3 (bypass service-4 broadcast)", align=Align.INLINE)
d.comment(0xA730, "Pop saved A", align=Align.INLINE)
d.label(0xA730, "boot_persist_fs_maybe")

d.comment(0xA731, "Compare with 2", align=Align.INLINE)
d.comment(0xA733, "Below: skip making FS permanent", align=Align.INLINE)
d.comment(0xA735, "Boot type >= 2 (NFS-resident !Boot): A=&6D to commit NFS as default FS", align=Align.INLINE)
d.label(0xA73A, "check_auto_boot_flag")

d.subroutine(
    0xA73A,
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


d.comment(0xA73A, "Load config flags", align=Align.INLINE)
d.comment(0xA73D, "Save copy in X", align=Align.INLINE)
d.comment(0xA73E, "Test bit 2 (auto-boot flag)", align=Align.INLINE)
d.comment(0xA740, "Save bit 2 test result", align=Align.INLINE)
d.comment(0xA741, "Restore full flags", align=Align.INLINE)
d.comment(0xA742, "Clear bit 2 (consume flag)", align=Align.INLINE)
d.comment(0xA744, "Store cleared flags", align=Align.INLINE)
d.comment(0xA747, "Restore bit 2 test result", align=Align.INLINE)
d.comment(0xA748, "Auto-boot flag was set: skip CTRL check, dispatch boot via boot_select_cmd", align=Align.INLINE)
d.comment(0xA74A, "OSBYTE &79: scan keyboard", align=Align.INLINE)
d.comment(0xA74C, "X = CTRL key scan code (negative-X INKEY form for OSBYTE &79)", align=Align.INLINE)
d.comment(0xA752, "CTRL not pressed: proceed to boot", align=Align.INLINE)
d.label(0xA754, "boot_cancel_rts")
d.label(0xA755, "boot_cmd_load_str")
d.label(0xA762, "boot_cmd_exec_str")


d.comment(0xA754, "Cancel boot, return (CTRL held, or boot type 0 via BEQ at &A762)", align=Align.INLINE)
d.comment(0xA755, "Boot cmd '*LOAD -NET-!Boot' (load !Boot via NFS, bypassing service-4 broadcast — see boot_try_findlib)", align=Align.INLINE)
d.comment(0xA761, "CR terminator", align=Align.INLINE)
d.comment(0xA762, "Boot cmd '*EXEC -NET-!Boot' (exec !Boot via NFS, bypassing service-4 broadcast — see boot_try_findlib)", align=Align.INLINE)
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
# UNMAPPED: d.comment(0xA75D, "Y=2: lo byte of &A748 (offset 7 into boot_cmd_load_str, on '!') — '!Boot' on current FS", align=Align.INLINE)
# UNMAPPED: d.expr(0xA75E, "<boot_cmd_exec_str")
# UNMAPPED: d.comment(0xA75E, "Y=3: lo byte of boot_cmd_exec_str (&A74E) — 'E.-NET-!Boot'", align=Align.INLINE)
d.label(0xA773, "boot_select_cmd")

d.subroutine(
    0xA773,
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
the `BNE` at `&A748` (auto-boot flag was set, skip CTRL check)
and the `BPL` at `&A73E` (CTRL not pressed, proceed to boot).""",
)


d.comment(0xA773, "Y = boot-type byte from FS reply (0..3)", align=Align.INLINE)
d.comment(0xA776, "Z (boot type 0): cancel boot via boot_cancel_rts", align=Align.INLINE)
d.label(0xA778, "boot_cmd_oscli")

d.subroutine(
    0xA778,
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


d.comment(0xA778, "Load boot-command low byte from boot_cmd_lo_table[Y]", align=Align.INLINE)
d.comment(0xA77B, "Y=&A7: high byte (boot strings live in &A7xx)", align=Align.INLINE)
d.comment(0xA77D, "Tail-jump to OSCLI to execute the boot command", align=Align.INLINE)
d.index_base(0xA780, "cmd_table_fs")
d.banner(
    0xA780,
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
d.label(0xA781, "cmd_dispatch_lo_table")

d.label(0xA782, "cmd_dispatch_hi_table")

d.byte(0xA7B3)
d.comment(0xA7B3, "Sub-table 1 end (walker reads &80 -> stop)", align=Align.INLINE)
d.byte(0xA7B4)
d.comment(0xA7B4, "Padding (alignment before sub-table 2)", align=Align.INLINE)
d.label(0xA7B5, "cmd_table_nfs")

d.index_base(0xA7DD, "cmd_table_nfs_iam")

# UNMAPPED: d.byte(0xA7FA)
# UNMAPPED: d.comment(0xA7FA, "Sub-table 2 end (walker reads &80 -> stop)", align=Align.INLINE)
# UNMAPPED: d.byte(0xA7FB)
# UNMAPPED: d.comment(0xA7FB, "Padding -- &2C 8E happens to spell &8E2D = check_urd_prefix but is never read", align=Align.INLINE)
# UNMAPPED: d.byte(0xA7FC)
# UNMAPPED: d.comment(0xA7FC, "Padding (continued)", align=Align.INLINE)
# UNMAPPED: d.label(0xA7FD, "cmd_table_help_topics")

d.byte(0xA824)
d.comment(0xA824, "Sub-table 3 end (walker reads &80 -> stop)", align=Align.INLINE)
d.label(0xA825, "cmd_table_syntax_help")
d.byte(0xA841)
d.comment(0xA841, "Sub-tables 4/5 separator", align=Align.INLINE)

d.comment(0xA854, "BRA osword_store_svc_state -- skip past 22-byte caller-cleanup frame", align=Align.INLINE)
d.entry(0xA854)


d.subroutine(
    0xA854,
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


d.label(0xA855, "svc_8_osword_disp")

d.comment(0xA855, "CLC so SBC subtracts value+1", align=Align.INLINE)
d.comment(0xA856, "OSWORD setup state (13 bytes -- constants and offsets used by svc_8_osword)", align=Align.INLINE)
d.comment(0xA858, "A = OSWORD - &0E (CLC+SBC = -&0E)", align=Align.INLINE)
d.comment(0xA85A, "Below &0E: not ours, return", align=Align.INLINE)
d.comment(0xA85C, "Index >= 7? (OSWORD > &14)", align=Align.INLINE)
d.comment(0xA85E, "Above &14: not ours, return", align=Align.INLINE)
d.comment(0xA860, "X=OSWORD handler index (0-6)", align=Align.INLINE)
d.comment(0xA861, "Y=6: save 6 workspace bytes", align=Align.INLINE)
d.comment(0xA863, "Read svc_state[Y] (frame slot)", align=Align.INLINE)
d.label(0xA863, "loop_save_osword_ws")

d.comment(0xA866, "Save on stack", align=Align.INLINE)
d.comment(0xA867, "Load OSWORD parameter byte", align=Align.INLINE)
d.comment(0xA86A, "Copy parameter to workspace", align=Align.INLINE)
d.comment(0xA86D, "Next slot", align=Align.INLINE)
d.comment(0xA86E, "Loop until Y wraps", align=Align.INLINE)
d.label(0xA86E, "osword_store_svc_state")

d.comment(0xA870, "Set up dispatch and save state", align=Align.INLINE)
d.comment(0xA873, "Y=&FA: restore 6 workspace bytes", align=Align.INLINE)
d.label(0xA875, "loop_restore_osword_ws")


d.comment(0xA875, "Restore saved workspace byte", align=Align.INLINE)
d.comment(0xA876, "Store to osword_flag workspace", align=Align.INLINE)
d.comment(0xA879, "Next byte", align=Align.INLINE)
d.comment(0xA87A, "Loop until all 6 restored", align=Align.INLINE)
d.comment(0xA87C, "Return from svc_8_osword", align=Align.INLINE)
d.label(0xA87D, "osword_setup_handler")

d.subroutine(
    0xA87D,
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


d.comment(0xA87D, "X = OSWORD index (0-6)", align=Align.INLINE)
d.comment(0xA880, "Push for stack frame manipulation", align=Align.INLINE)
d.comment(0xA881, "Load handler address low byte", align=Align.INLINE)
d.comment(0xA884, "Push again", align=Align.INLINE)
d.comment(0xA885, "Copy 3 bytes (Y=2,1,0)", align=Align.INLINE)
d.comment(0xA887, "Load from osword_flag workspace", align=Align.INLINE)
d.label(0xA889, "rts_osword_setup")

d.comment(0xA889, "RTS dispatches to pushed handler", align=Align.INLINE)
# UNMAPPED: d.comment(
# UNMAPPED:     0xA871,
# UNMAPPED:     "PB-ready / parameter table (3 bytes) read by osword_setup_handler at &A868 via LDA osword_pb_ready,X",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
# UNMAPPED: d.index_base(0xA871, "osword_pb_ready")

d.label(0xA874, "osword_0e_handler")

# UNMAPPED: d.comment(
# UNMAPPED:     0xA874,
# UNMAPPED:     "BIT $abs -- 3-byte skip-trick that jumps over the extract_osword_subcode prologue when called via &A874",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
d.entry(0xA874)
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
d.comment(0xA897, "Load template source pointer", align=Align.INLINE)
# UNMAPPED: d.comment(0xA884, "Compare with &04", align=Align.INLINE)
d.comment(0xA8A5, "Equal: take save_txcb_and_convert path", align=Align.INLINE)
d.comment(0xA8A7, "Restore A (OSWORD sub-code)", align=Align.INLINE)
d.comment(0xA8A9, "Equal: take save_txcb_done path", align=Align.INLINE)
d.comment(0xA8AB, "Other sub-codes: set state = 8", align=Align.INLINE)
d.comment(0xA8AD, "Store service state", align=Align.INLINE)
d.label(0xA8AF, "rts_osword_0e")

d.comment(0xA8AF, "Return", align=Align.INLINE)
d.subroutine(
    0xA8B0,
    "save_txcb_and_convert",
    title="OSWORD &0E: convert the clock/date fields to BCD",
    description="""Saves the TX control block, then reads the clock and date fields from the
HAZEL TXCB workspace and converts each to packed BCD via
[`bin_to_bcd`](label:bin_to_bcd) for the OSWORD &0E real-time-clock reply.""",
)

d.comment(0xA8B0, "X=0: start of TX control block", align=Align.INLINE)
d.comment(0xA8B2, "Y=&10: length of TXCB to save", align=Align.INLINE)
d.comment(0xA8B4, "Save current TX control block", align=Align.INLINE)
d.comment(0xA8B7, "Load seconds from clock workspace", align=Align.INLINE)
d.comment(0xA8BA, "Convert binary to BCD", align=Align.INLINE)
d.comment(0xA8BD, "Store BCD seconds", align=Align.INLINE)
d.comment(0xA8C0, "Load minutes from clock workspace", align=Align.INLINE)
d.comment(0xA8C3, "Convert binary to BCD", align=Align.INLINE)
d.comment(0xA8C6, "Store BCD minutes", align=Align.INLINE)
d.comment(0xA8C9, "Load hours from clock workspace", align=Align.INLINE)
d.comment(0xA8CC, "Convert binary to BCD", align=Align.INLINE)
d.comment(0xA8CF, "Store BCD hours", align=Align.INLINE)
d.comment(0xA8D2, "Clear hours high position", align=Align.INLINE)
d.comment(0xA8D4, "Store zero", align=Align.INLINE)
d.comment(0xA8D7, "Load day+month byte", align=Align.INLINE)
d.comment(0xA8DA, "Save for later high nibble extract", align=Align.INLINE)
d.comment(0xA8DB, "Load day value", align=Align.INLINE)
d.comment(0xA8DE, "Convert day to BCD", align=Align.INLINE)
d.comment(0xA8E1, "Store BCD day", align=Align.INLINE)
d.comment(0xA8E4, "Restore day+month byte", align=Align.INLINE)
d.comment(0xA8E5, "Push current A", align=Align.INLINE)
d.comment(0xA8E6, "Mask low nibble (month low bits)", align=Align.INLINE)
d.comment(0xA8E8, "Convert to BCD", align=Align.INLINE)
d.comment(0xA8EB, "Store BCD month", align=Align.INLINE)
d.comment(0xA8EE, "Pop saved value", align=Align.INLINE)
d.comment(0xA8EF, "Shift high nibble down", align=Align.INLINE)
d.comment(0xA8F0, "Divide by 4", align=Align.INLINE)
d.comment(0xA8F1, "(continued)", align=Align.INLINE)
d.comment(0xA8F2, "4th shift: isolate high nibble", align=Align.INLINE)
d.comment(0xA8F4, "Add &51 (offset base)", align=Align.INLINE)
d.comment(0xA8F6, "Convert year to BCD", align=Align.INLINE)
d.comment(0xA8F9, "Store BCD year", align=Align.INLINE)
d.comment(0xA8FC, "Copy 7 bytes (Y=6 down to 0)", align=Align.INLINE)
d.label(0xA8FE, "loop_copy_bcd_to_pb")

d.comment(0xA8FE, "Load BCD byte from workspace", align=Align.INLINE)
d.comment(0xA901, "Store to parameter block", align=Align.INLINE)
d.comment(0xA903, "Next byte down", align=Align.INLINE)
d.comment(0xA904, "Loop for all 7 bytes", align=Align.INLINE)
d.comment(0xA906, "Return", align=Align.INLINE)
d.comment(0xA907, "Convert TXCB date/time bytes to BCD", align=Align.INLINE)
d.subroutine(
    0xA907,
    "save_txcb_done",
    title="OSWORD &0E: build the reply and read the CMOS clock",
    description="""Builds the BCD reply via [`save_txcb_and_convert`](label:save_txcb_and_convert),
copies it into the OSWORD parameter block, and reads the CMOS real-time clock
via OSWORD &0E.""",
)

d.comment(0xA90A, "Y=7: copy 8 bytes (Y=7 down to 0)", align=Align.INLINE)
d.comment(0xA90C, "Load BCD byte from TXCB area (hazel_txcb_lib + Y)", align=Align.INLINE)
d.label(0xA90C, "loop_copy_pbytes_to_ws")

d.comment(0xA90F, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xA911, "Decrement Y (advance backwards)", align=Align.INLINE)
d.comment(0xA912, "Loop until Y wraps", align=Align.INLINE)
d.comment(0xA914, "A=2: PB[0] parameter for OSWORD &0E (seconds-since-midnight format)", align=Align.INLINE)
d.comment(0xA916, "Store parameter at PB[0]", align=Align.INLINE)
d.comment(0xA918, "A=&0E: OSWORD &0E (read CMOS RTC)", align=Align.INLINE)
d.comment(0xA91A, "X = PB pointer low", align=Align.INLINE)
d.comment(0xA91C, "Y = PB pointer high (via table_idx scratch)", align=Align.INLINE)
d.subroutine(
    0xA921,
    "bin_to_bcd",
    title="Convert binary byte to BCD",
    description="""Uses decimal mode (SED) with a count-up loop:
starts at BCD 0 and adds 1 in decimal mode for
each decrement of the binary input. Saves and
restores the processor flags to avoid leaving
decimal mode active. Called 6 times by
save_txcb_and_convert for clock date/time
conversion.""",
    on_entry={"a": "binary value (0-99)"},
    on_exit={"a": "BCD equivalent"},
)


d.comment(0xA921, "Save caller flags (D may be in any state)", align=Align.INLINE)
d.comment(0xA922, "Save A across decimal-mode arithmetic", align=Align.INLINE)
d.comment(0xA923, "Zero: result is 0, skip loop", align=Align.INLINE)
d.comment(0xA925, "Enter decimal mode", align=Align.INLINE)
d.comment(0xA926, "Start BCD result at 0", align=Align.INLINE)
d.label(0xA928, "loop_bcd_add")

d.comment(0xA928, "Clear carry for BCD add", align=Align.INLINE)
d.comment(0xA929, "Add 1 in decimal mode", align=Align.INLINE)
d.comment(0xA92B, "Count down binary value", align=Align.INLINE)
d.comment(0xA92C, "Loop until zero", align=Align.INLINE)
d.label(0xA92E, "done_bcd_convert")

d.comment(0xA92E, "Restore caller flags (incl. D)", align=Align.INLINE)
d.comment(0xA92F, "Return with BCD result in A", align=Align.INLINE)
d.label(0xA930, "osword_10_handler")

d.subroutine(
    0xA930,
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


d.entry(0xA930)
d.comment(0xA930, "ASL tx_complete_flag: old bit 7 -> C", align=Align.INLINE)
d.comment(0xA933, "A = Y (saved index)", align=Align.INLINE)
d.comment(0xA934, "C=1 (TX idle): start new transmission", align=Align.INLINE)
d.comment(0xA936, "C=0 (TX busy): write status byte back to PB", align=Align.INLINE)
d.comment(0xA938, "Return (TX still in progress)", align=Align.INLINE)
d.label(0xA939, "setup_ws_rx_ptrs")

d.comment(0xA939, "Read net_rx_ptr_hi", align=Align.INLINE)
d.comment(0xA93B, "Copy to ws_ptr_lo", align=Align.INLINE)
d.comment(0xA93D, "Also set as NMI TX block high", align=Align.INLINE)
d.comment(0xA93F, "Low byte = &6F", align=Align.INLINE)
d.comment(0xA941, "Set osword_flag", align=Align.INLINE)
d.comment(0xA943, "Set NMI TX block low", align=Align.INLINE)
d.comment(0xA945, "X=&0F: byte count for copy", align=Align.INLINE)
d.comment(0xA947, "Copy data and begin transmission", align=Align.INLINE)
d.comment(0xA94A, "Jump to begin Econet transmission", align=Align.INLINE)
d.subroutine(
    0xA94D,
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


d.entry(0xA94D)
d.comment(0xA94D, "Load NFS workspace page high byte", align=Align.INLINE)
d.comment(0xA94F, "Set workspace pointer high", align=Align.INLINE)
d.comment(0xA951, "Set workspace pointer low from Y", align=Align.INLINE)
d.comment(0xA953, "Rotate Econet flags (save interrupt state)", align=Align.INLINE)
d.comment(0xA956, "Y=OSWORD flag (slot specifier)", align=Align.INLINE)
d.comment(0xA957, "Store OSWORD flag", align=Align.INLINE)
d.comment(0xA959, "Non-zero: use specified slot", align=Align.INLINE)
d.comment(0xA95B, "A=3: start searching from slot 3", align=Align.INLINE)
d.label(0xA95D, "loop_find_rx_slot")

d.comment(0xA95D, "Convert slot to 2-bit workspace index", align=Align.INLINE)
d.comment(0xA960, "C set: slot invalid, store result", align=Align.INLINE)
d.comment(0xA962, "Divide by 2", align=Align.INLINE)
d.comment(0xA963, "Continue shift", align=Align.INLINE)
d.comment(0xA964, "Index to X", align=Align.INLINE)
d.comment(0xA965, "Load workspace byte at offset", align=Align.INLINE)
d.comment(0xA967, "Zero: slot empty, store result", align=Align.INLINE)
d.comment(0xA969, "Compare with &3F ('?' marker)", align=Align.INLINE)
d.comment(0xA96B, "Match: slot found for receive", align=Align.INLINE)
d.comment(0xA96D, "Step to next slot", align=Align.INLINE)
d.comment(0xA96E, "Transfer back to A", align=Align.INLINE)
d.comment(0xA96F, "Loop back (A != 0)", align=Align.INLINE)
d.label(0xA971, "store_rx_slot_found")

d.comment(0xA971, "Found slot index", align=Align.INLINE)
d.comment(0xA972, "X=0: index for indirect store", align=Align.INLINE)
d.comment(0xA974, "Store slot number to PB byte 0", align=Align.INLINE)
d.label(0xA976, "use_specified_slot")

d.comment(0xA976, "Convert specified slot to workspace index", align=Align.INLINE)
d.comment(0xA979, "C set: slot invalid, store result", align=Align.INLINE)
d.comment(0xA97B, "Back up scan", align=Align.INLINE)
d.comment(0xA97C, "Update workspace pointer low", align=Align.INLINE)
d.comment(0xA97E, "A=&C0: slot active marker", align=Align.INLINE)
d.comment(0xA980, "Y=1: result-byte offset", align=Align.INLINE)
d.comment(0xA982, "X=&0B: byte count for PB copy", align=Align.INLINE)
d.comment(0xA984, "Compare Y with OSWORD flag", align=Align.INLINE)
d.comment(0xA986, "Add workspace byte (check slot state)", align=Align.INLINE)
d.comment(0xA988, "Zero: slot ready, copy PB and mark", align=Align.INLINE)
d.comment(0xA98A, "Negative: slot busy, increment and retry", align=Align.INLINE)
d.label(0xA98C, "loop_copy_slot_data")

d.comment(0xA98C, "For the ADC chain", align=Align.INLINE)
d.label(0xA98D, "copy_pb_and_mark")

d.comment(0xA98D, "Copy PB byte to workspace slot", align=Align.INLINE)
d.comment(0xA990, "C set: copy done, finish", align=Align.INLINE)
d.comment(0xA992, "A=&3F: mark slot as pending ('?')", align=Align.INLINE)
d.comment(0xA994, "Y=1: workspace flag offset", align=Align.INLINE)
d.comment(0xA996, "Store pending marker to workspace", align=Align.INLINE)
d.label(0xA99A, "increment_and_retry")

d.comment(0xA99A, "Increment retry counter", align=Align.INLINE)
d.comment(0xA99C, "Non-zero: retry copy loop", align=Align.INLINE)
d.comment(0xA99E, "Decrement Y (adjust offset)", align=Align.INLINE)
d.label(0xA99F, "store_rx_result")

d.comment(0xA99F, "Store result A to PB via Y", align=Align.INLINE)
d.label(0xA9A1, "osword_11_done")

d.comment(0xA9A1, "Rotate Econet flags back (restore state)", align=Align.INLINE)
d.comment(0xA9A4, "Return from OSWORD 11 handler", align=Align.INLINE)
d.label(0xA9A5, "osword_12_handler")

d.subroutine(
    0xA9A5,
    "osword_12_handler",
    title="OSWORD &12 handler: receive packet from workspace",
    description="""Reads `net_rx_ptr_hi` into `ws_ptr_lo`, sets `Y=&7F` and reads the
status byte from the RX block, then `Y=&80` to flag the packet as
processed. The body proceeds to copy the packet payload from the
RX buffer into the OSWORD parameter block via
[`copy_pb_byte_to_ws`](label:copy_pb_byte_to_ws).""",
    on_entry={"x, y": "OSWORD parameter block pointer (low, high)"},
)
d.entry(0xA9A5)
d.comment(0xA9A5, "Set workspace from RX ptr high", align=Align.INLINE)
d.comment(0xA9A7, "Store to ws_ptr_lo", align=Align.INLINE)
d.comment(0xA9A9, "Y=&7F: last byte of RX buffer", align=Align.INLINE)
d.comment(0xA9AB, "Load port/count from RX buffer", align=Align.INLINE)
d.comment(0xA9AD, "Y=&80: set workspace pointer", align=Align.INLINE)
d.comment(0xA9AE, "Store as osword_flag", align=Align.INLINE)
d.comment(0xA9B0, "X = port/count value", align=Align.INLINE)
d.comment(0xA9B1, "X-1: adjust count", align=Align.INLINE)
d.comment(0xA9B2, "Y=0 for copy", align=Align.INLINE)
d.comment(0xA9B4, "Copy workspace data", align=Align.INLINE)
d.comment(0xA9B7, "Update state and return", align=Align.INLINE)
d.label(0xA9BA, "osword_13_dispatch")

d.entry(0xA9BA)
d.comment(0xA9BA, "X = sub-code", align=Align.INLINE)
d.comment(0xA9BB, "Sub-code < &13?", align=Align.INLINE)
d.comment(0xA9BD, "Out of range: return", align=Align.INLINE)
d.comment(0xA9BF, "Read dispatch hi from osword_13_dispatch_hi+X", align=Align.INLINE)
d.comment(0xA9C2, "Push hi for RTS dispatch", align=Align.INLINE)
d.comment(0xA9C3, "Read dispatch lo from osword_13_dispatch_lo+X", align=Align.INLINE)
d.comment(0xA9C6, "Push lo for RTS dispatch", align=Align.INLINE)
d.label(0xA9C7, "rts_osword_13")
d.comment(0xA9C7, "RTS -> dispatched OSWORD &13 sub-handler", align=Align.INLINE)
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
d.index_base(0xA9DA, "osword_13_dispatch_hi")
d.banner(
    0xA9DA,
    title="OSWORD &13 dispatch high-byte table (18 entries)",
    description="""Read by [`osword_13_dispatch`](label:osword_13_dispatch) as `LDA &A9BA,X`. The
dispatcher pushes the hi byte first then the lo, so RTS lands on
`target` (the table stores `target-1`).""",
)
for addr in range(0xA9DA, 0xA9EC):
    d.byte(addr)
d.entry(0xA9EC)


d.subroutine(
    0xA9EC,
    "osword_13_read_station",
    title="OSWORD &13 sub 0: read file server station",
    description="""Returns the current file server station and network numbers in
`PB[1..2]`. If ANFS is not active,
[`ensure_fs_selected`](label:ensure_fs_selected) auto-selects it (raising `net
checksum` on failure) before the body runs.""",
)
d.comment(0xA9EC, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.label(0xA9EF, "read_station_bytes")

d.comment(0xA9EF, "Y=2: copy 2 bytes", align=Align.INLINE)
d.label(0xA9F1, "loop_copy_station")

d.comment(0xA9F1, "Load station byte", align=Align.INLINE)
d.comment(0xA9F4, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xA9F6, "Step back", align=Align.INLINE)
d.comment(0xA9F7, "Loop for bytes 2..1", align=Align.INLINE)
d.comment(0xA9F9, "Return", align=Align.INLINE)
d.entry(0xA9FA)


d.subroutine(
    0xA9FA,
    "osword_13_set_station",
    title="OSWORD &13 sub 1: set file server station",
    description="""Sets the file server station and network numbers from `PB[1..2]`.
The prologue at `&A9DA` calls
[`ensure_fs_selected`](label:ensure_fs_selected) to verify ANFS is active
(auto-selecting it if not), then the body at
[`osword_13_set_station_body`](label:osword_13_set_station_body) processes all FCBs
and scans the 16-entry FCB table to reassign handles matching the
new station.""",
)

d.comment(0xA9FA, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.label(0xA9FD, "osword_13_set_station_body")


d.comment(0xA9FD, "Y=0 for process_all_fcbs", align=Align.INLINE)
d.comment(0xA9FF, "Close all open FCBs", align=Align.INLINE)
d.comment(0xAA02, "Y=2: copy 2 bytes", align=Align.INLINE)
d.label(0xAA04, "loop_store_station")

d.comment(0xAA04, "Load new station byte from PB", align=Align.INLINE)
d.comment(0xAA06, "Store to fs_server_base", align=Align.INLINE)
d.comment(0xAA09, "Step back to previous byte", align=Align.INLINE)
d.comment(0xAA0A, "Loop for bytes 2..1", align=Align.INLINE)
d.comment(0xAA0C, "Clear handles if station matches", align=Align.INLINE)
d.comment(0xAA0F, "A=&0E: bits 1..3 (FS-state mask)", align=Align.INLINE)
d.comment(0xAA11, "Set fs_flags bits 1..3", align=Align.INLINE)
d.comment(0xAA14, "A=&40: FS-active flag bit", align=Align.INLINE)
d.comment(0xAA16, "Clear FS-active flag (bit 6)", align=Align.INLINE)
d.comment(0xAA19, "X=&0F: scan all 16 FCB slots (X = 15 down to 0)", align=Align.INLINE)
d.label(0xAA1B, "scan_fcb_entry")

d.comment(0xAA1B, "Load FCB flags", align=Align.INLINE)
d.comment(0xAA1E, "Save flags in Y", align=Align.INLINE)
d.comment(0xAA1F, "Test bit 1 (FCB allocated?)", align=Align.INLINE)
d.comment(0xAA21, "No: skip to next entry", align=Align.INLINE)
d.comment(0xAA23, "Entry index to A", align=Align.INLINE)
d.comment(0xAA24, "Mask bit 5", align=Align.INLINE)
d.comment(0xAA26, "Store updated flags", align=Align.INLINE)
d.comment(0xAA29, "Save in Y", align=Align.INLINE)
d.comment(0xAA2A, "Does FCB match new station?", align=Align.INLINE)
d.comment(0xAA2D, "No match: skip to next", align=Align.INLINE)
d.comment(0xAA2F, "Clear carry", align=Align.INLINE)
d.comment(0xAA30, "Restore flags", align=Align.INLINE)
d.comment(0xAA31, "Test bit 2 (handle 1 active?)", align=Align.INLINE)
d.comment(0xAA33, "No: check handle 2", align=Align.INLINE)
d.comment(0xAA35, "Restore flags", align=Align.INLINE)
d.comment(0xAA36, "Set bit 5 (handle reassigned)", align=Align.INLINE)
d.comment(0xAA39, "Get FCB high byte", align=Align.INLINE)
d.comment(0xAA3C, "Store as handle 1 station", align=Align.INLINE)
d.comment(0xAA3F, "FCB index", align=Align.INLINE)
d.comment(0xAA40, "Add &20 for FCB table offset", align=Align.INLINE)
d.comment(0xAA42, "Store as handle 1 FCB index", align=Align.INLINE)
d.comment(0xAA45, "A=2: fs_flags bit 1 mask", align=Align.INLINE)
d.comment(0xAA47, "Clear fs_flags bit 1", align=Align.INLINE)
d.label(0xAA4A, "check_handle_2")

d.comment(
    0xAA4A,
    "Y still holds the saved FCB status -- TYA so we can re-test bit 3 (handle-2 active flag)",
    align=Align.INLINE,
)
d.comment(0xAA4B, "Test bit 3 (handle 2 active?)", align=Align.INLINE)
d.comment(0xAA4D, "No: check handle 3", align=Align.INLINE)
d.comment(0xAA50, "Set bit 5", align=Align.INLINE)
d.comment(0xAA53, "Get FCB high byte", align=Align.INLINE)
d.comment(0xAA56, "Store as handle 2 station", align=Align.INLINE)
d.comment(0xAA59, "FCB index", align=Align.INLINE)
d.comment(0xAA5A, "Add &20 for FCB table offset", align=Align.INLINE)
d.comment(0xAA5C, "Store as handle 2 FCB index", align=Align.INLINE)
d.comment(0xAA5F, "A=4: fs_flags bit 2 mask", align=Align.INLINE)
d.comment(0xAA61, "Clear fs_flags bit 2", align=Align.INLINE)
d.label(0xAA64, "check_handle_3")

d.comment(
    0xAA64,
    "Y still holds the saved FCB status -- TYA so we can re-test bit 4 (handle-3 active flag)",
    align=Align.INLINE,
)
d.comment(0xAA65, "Test bit 4 (handle 3 active?)", align=Align.INLINE)
d.comment(0xAA67, "No: store final flags", align=Align.INLINE)
d.comment(0xAA69, "Restore flags", align=Align.INLINE)
d.comment(0xAA6A, "Set bit 5", align=Align.INLINE)
d.comment(0xAA6C, "Save updated flags", align=Align.INLINE)
d.comment(0xAA6D, "Get FCB high byte", align=Align.INLINE)
d.comment(0xAA70, "Store as handle 3 station", align=Align.INLINE)
d.comment(0xAA73, "FCB index", align=Align.INLINE)
d.comment(0xAA74, "Add &20 for FCB table offset", align=Align.INLINE)
d.comment(0xAA76, "Store as handle 3 FCB index", align=Align.INLINE)
d.comment(0xAA79, "A=8: fs_flags bit 3 (FS-error pending)", align=Align.INLINE)
d.comment(0xAA7B, "Clear FS-error-pending flag", align=Align.INLINE)
d.label(0xAA7E, "store_updated_status")

d.comment(0xAA7E, "A = Y for store", align=Align.INLINE)
d.comment(0xAA7F, "Store updated status into hazel_fcb_status[X]", align=Align.INLINE)
d.label(0xAA82, "next_fcb_entry")

d.comment(0xAA82, "Decrement entry counter", align=Align.INLINE)
d.comment(0xAA83, "Loop while X >= 0 (scan all FCBs)", align=Align.INLINE)
d.comment(0xAA85, "A=&0E: status flag value", align=Align.INLINE)
d.comment(0xAA87, "Test fs_flags bits 1..3", align=Align.INLINE)
d.comment(0xAA8A, "Non-zero: skip the FS-active set", align=Align.INLINE)
d.comment(0xAA8C, "A=&40: FS-active flag bit", align=Align.INLINE)
d.comment(0xAA8E, "Set FS-active flag (bit 6 of fs_flags)", align=Align.INLINE)
d.comment(0xAA91, "Return -- FCB-status update complete", align=Align.INLINE)
d.entry(0xAA92)
d.subroutine(
    0xAA92,
    "osword_13_read_csd",
    title="OSWORD &13 sub 12: read CSD path",
    description="""Reads 5 current selected directory path bytes
from the RX workspace at offset &17 into
PB[1..5]. Sets carry clear to select the
workspace-to-PB copy direction.""",
)


d.comment(0xAA92, "WS-to-PB direction (read)", align=Align.INLINE)
d.comment(0xAA93, "Skip SEC", align=Align.INLINE)
d.entry(0xAA95)

d.subroutine(
    0xAA95,
    "osword_13_write_csd",
    title="OSWORD &13 sub 13: write CSD path",
    description="""Writes 5 current selected directory path bytes
from PB[1..5] into the RX workspace at offset
&17. Sets carry to select the PB-to-workspace
copy direction.""",
)


d.comment(0xAA95, "C=1: PB-to-workspace direction", align=Align.INLINE)
d.label(0xAA96, "setup_csd_copy")

d.comment(0xAA96, "Workspace offset &17", align=Align.INLINE)
d.comment(0xAA98, "Save A as osword_flag (counter)", align=Align.INLINE)
d.comment(0xAA9A, "Page from RX pointer high byte", align=Align.INLINE)
d.comment(0xAA9C, "Set ws_ptr_hi", align=Align.INLINE)
d.comment(0xAA9E, "Y=1: first PB data byte", align=Align.INLINE)
d.comment(0xAAA0, "X=5: copy 5 bytes", align=Align.INLINE)
d.subroutine(
    0xAAA2,
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


d.comment(0xAAA2, "C=0: skip PB-to-WS copy", align=Align.INLINE)
d.comment(0xAAA4, "C=1: load from parameter block", align=Align.INLINE)
d.comment(0xAAA6, "Store to workspace", align=Align.INLINE)
d.label(0xAAA8, "copy_ws_byte_to_pb")

d.comment(0xAAA8, "Load from workspace", align=Align.INLINE)
d.comment(0xAAAA, "Store to parameter block", align=Align.INLINE)
d.comment(0xAAAC, "Next byte", align=Align.INLINE)
d.comment(0xAAAD, "Count down", align=Align.INLINE)
d.comment(0xAAAE, "Loop for all bytes", align=Align.INLINE)
d.comment(0xAAB0, "Return", align=Align.INLINE)
d.subroutine(
    0xAAB1,
    "osword_13_read_ws_pair",
    title="OSWORD &13 sub 2: read workspace byte pair",
    description="""Reads 2 bytes from the NFS workspace page
starting at offset 1 into PB[1..2]. Uses
nfs_workspace_hi as the page and
copy_pb_byte_to_ws with carry clear for the
workspace-to-PB direction.""",
)


d.comment(0xAAB1, "Load workspace page high byte", align=Align.INLINE)
d.comment(0xAAB3, "Set ws_ptr_hi", align=Align.INLINE)
d.comment(0xAAB5, "Y=1", align=Align.INLINE)
d.comment(0xAAB6, "A = current byte index", align=Align.INLINE)
d.comment(0xAAB7, "Set ws_ptr_lo = 1", align=Align.INLINE)
d.comment(0xAAB9, "X=1: copy 2 bytes", align=Align.INLINE)
d.comment(0xAABA, "WS-to-PB direction", align=Align.INLINE)
d.comment(0xAABB, "Copy via copy_pb_byte_to_ws", align=Align.INLINE)
d.subroutine(
    0xAABD,
    "osword_13_write_ws_pair",
    title="OSWORD &13 sub 3: write workspace byte pair",
    description="""Writes 2 bytes from PB[1..2] into the NFS
workspace at offsets 2 and 3. Then calls
init_bridge_poll and conditionally clears
the workspace byte if the bridge status
changed.""",
)


d.comment(0xAABD, "Y=1: first PB data byte", align=Align.INLINE)
d.comment(0xAABE, "Load PB[1]", align=Align.INLINE)
d.comment(0xAAC0, "Next byte", align=Align.INLINE)
d.comment(0xAAC1, "Store to (nfs_workspace)+2", align=Align.INLINE)
d.comment(0xAAC3, "Load PB[2]", align=Align.INLINE)
d.comment(0xAAC5, "Y=3", align=Align.INLINE)
d.comment(0xAAC6, "Store to (nfs_workspace)+3", align=Align.INLINE)
d.comment(0xAAC8, "Reinitialise bridge routing", align=Align.INLINE)
d.comment(0xAACB, "Compare result with workspace", align=Align.INLINE)
d.comment(0xAACD, "Different: leave unchanged", align=Align.INLINE)
d.comment(0xAACF, "Same: clear workspace byte", align=Align.INLINE)
d.label(0xAAD1, "rts_write_ws_pair")

d.comment(0xAAD1, "Return", align=Align.INLINE)
d.subroutine(
    0xAAD2,
    "osword_13_read_prot",
    title="OSWORD &13 sub 4: read protection mask",
    description="""Returns the current protection mask (prot_status)
in PB[1].""",
)


d.comment(0xAAD2, "Load protection mask", align=Align.INLINE)
d.comment(0xAAD5, "Store to PB[1] and return", align=Align.INLINE)
d.subroutine(
    0xAAD8,
    "osword_13_write_prot",
    title="OSWORD &13 sub 5: write protection mask",
    description="""Loads the new protection mask from `PB[1]` and falls through into
[`set_ws_pair_0d68_0d69`](label:set_ws_pair_0d68_0d69) which mirrors it into the
ACR/SR-format byte pair at `&0D68` / `&0D69` that ANFS uses for its
own state tracking.""",
)


d.comment(0xAAD8, "Y=1: PB data offset", align=Align.INLINE)
d.comment(0xAAD9, "Load new mask from PB[1]", align=Align.INLINE)
d.subroutine(
    0xAADB,
    "set_ws_pair_0d68_0d69",
    title="Store A in both prot_status and prot_status_save",
    description="""Copies `A` to both [`prot_status`](label:prot_status) and
[`prot_status_save`](label:prot_status_save), then `RTS`. The bytes carry ACR/SR-style
flag layouts that ANFS uses internally; nothing in this ROM flushes
them to the live System VIA. Two callers:
[`nfs_init_body`](label:nfs_init_body) at `&8FA6` (where A is `0` or
`&FF` based on FS-options bit 6) and
[`cmd_prot`](label:cmd_prot) at `&B702` (the *Prot path).
A 2-store-and-return convenience to keep both call sites flat.""",
    on_entry={"a": "value to mirror into both workspace bytes"},
)
d.comment(0xAADB, "Mirror A into prot_status (ACR-format byte)", align=Align.INLINE)
d.comment(0xAADE, "Mirror A into prot_status_save (IER-format byte)", align=Align.INLINE)
d.comment(0xAAE1, "Return", align=Align.INLINE)
d.entry(0xAAE2)


d.subroutine(
    0xAAE2,
    "osword_13_read_handles",
    title="OSWORD &13 sub 6: read FCB handle info",
    description="""Returns the 3-byte FCB handle/port data from the workspace at
`C271[1..3]` into `PB[1..3]`. If ANFS is not active,
[`ensure_fs_selected`](label:ensure_fs_selected) auto-selects it before the
body runs.""",
)
d.comment(0xAAE2, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.comment(0xAAE5, "Y=3: copy 3 bytes", align=Align.INLINE)
d.label(0xAAE7, "loop_copy_handles")

d.comment(0xAAE7, "Load handle byte", align=Align.INLINE)
d.comment(0xAAEA, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xAAEC, "Previous byte", align=Align.INLINE)
d.comment(0xAAED, "Loop for bytes 3..1", align=Align.INLINE)
d.comment(0xAAEF, "Return", align=Align.INLINE)
d.entry(0xAAF0)


d.subroutine(
    0xAAF0,
    "osword_13_set_handles",
    title="OSWORD &13 sub 7: set FCB handles",
    description="""Validates and assigns up to 3 FCB handles
from PB[1..3]. Each handle value (&20-&2F)
indexes the channel tables. For valid handles
with the appropriate flag bit, stores the
station and FCB index, then updates flag bits
across all FCB entries via update_fcb_flag_bits.""",
)


d.comment(0xAAF0, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.label(0xAAF3, "start_set_handles")

d.comment(0xAAF3, "Y=1: first handle in PB", align=Align.INLINE)
d.label(0xAAF5, "validate_handle")

d.comment(0xAAF5, "Load handle value from PB[Y]", align=Align.INLINE)
d.comment(0xAAF7, "Must be >= &20", align=Align.INLINE)
d.comment(0xAAF9, "Below range: invalid", align=Align.INLINE)
d.comment(0xAAFB, "Must be < &30", align=Align.INLINE)
d.comment(0xAAFD, "Above range: invalid", align=Align.INLINE)
d.comment(0xAAFF, "X = handle value", align=Align.INLINE)
d.comment(0xAB00, "Load fcb_attr_or_count_mid[handle]", align=Align.INLINE)
d.comment(0xAB03, "Non-zero: FCB exists", align=Align.INLINE)
d.label(0xAB05, "handle_invalid")

d.comment(0xAB05, "A=0: invalid-handle marker", align=Align.INLINE)
d.comment(0xAB08, "Clear PB[0] status", align=Align.INLINE)
d.comment(0xAB0A, "Skip to next handle", align=Align.INLINE)
d.label(0xAB0C, "check_handle_alloc")

d.comment(0xAB0C, "Load fcb_flags[handle] flags", align=Align.INLINE)
d.comment(0xAB0F, "Test bit 1 (allocated?)", align=Align.INLINE)
d.comment(0xAB11, "Not allocated: invalid", align=Align.INLINE)
d.comment(0xAB13, "X = handle value", align=Align.INLINE)
d.comment(0xAB14, "Store handle to fs_lib_flags+Y", align=Align.INLINE)
d.comment(0xAB17, "Load station from fcb_attr_or_count_mid", align=Align.INLINE)
d.comment(0xAB1A, "Store station to fs_server_net+Y", align=Align.INLINE)
d.comment(0xAB1D, "Is this handle 1 (Y=1)?", align=Align.INLINE)
d.comment(0xAB1F, "No: check handle 2", align=Align.INLINE)
d.comment(0xAB21, "Save Y for processing", align=Align.INLINE)
d.comment(0xAB22, "Push Y", align=Align.INLINE)
d.comment(0xAB23, "Bit mask &04 for handle 1", align=Align.INLINE)
d.comment(0xAB25, "Update flags across all FCBs", align=Align.INLINE)
d.comment(0xAB28, "Pop saved Y", align=Align.INLINE)
d.comment(0xAB29, "Back to Y", align=Align.INLINE)
d.comment(0xAB2A, "Reload fcb_flags flags", align=Align.INLINE)
d.comment(0xAB2D, "Set bits 2+5 (active+updated)", align=Align.INLINE)
d.comment(0xAB2F, "Store updated flags", align=Align.INLINE)
d.label(0xAB32, "next_handle_slot")

d.comment(0xAB32, "Next handle slot", align=Align.INLINE)
d.comment(0xAB33, "Compare with 4", align=Align.INLINE)
d.comment(0xAB35, "No: process next handle", align=Align.INLINE)
d.comment(0xAB37, "Y=3 for return", align=Align.INLINE)
d.comment(0xAB38, "Return", align=Align.INLINE)
d.label(0xAB39, "assign_handle_2")

d.comment(0xAB39, "Is this handle 2 (Y=2)?", align=Align.INLINE)
d.comment(0xAB3B, "No: must be handle 3", align=Align.INLINE)
d.comment(0xAB3D, "Save current Y", align=Align.INLINE)
d.comment(0xAB3E, "Push Y", align=Align.INLINE)
d.comment(0xAB3F, "Y=8 (handle-bit shift index)", align=Align.INLINE)
d.comment(0xAB41, "Update flags across all FCBs", align=Align.INLINE)
d.comment(0xAB44, "Restore Y", align=Align.INLINE)
d.comment(0xAB45, "Back to Y", align=Align.INLINE)
d.comment(0xAB46, "Reload fcb_flags flags", align=Align.INLINE)
d.comment(0xAB49, "Set bits 3 and 5", align=Align.INLINE)
d.comment(0xAB4B, "Store updated flags", align=Align.INLINE)
d.comment(0xAB4E, "Next handle slot", align=Align.INLINE)
d.label(0xAB50, "assign_handle_3")

d.comment(0xAB50, "Handle 3: save Y", align=Align.INLINE)
d.comment(0xAB51, "Push for save/restore", align=Align.INLINE)
d.comment(0xAB52, "Bit mask &10 for handle 3", align=Align.INLINE)
d.comment(0xAB54, "Update flags across all FCBs", align=Align.INLINE)
d.comment(0xAB57, "Pop saved value", align=Align.INLINE)
d.comment(0xAB58, "Back to Y", align=Align.INLINE)
d.comment(0xAB59, "Reload fcb_flags flags", align=Align.INLINE)
d.comment(0xAB5C, "Set bits 4+5 (active+updated)", align=Align.INLINE)
d.comment(0xAB5E, "Store updated flags", align=Align.INLINE)
d.comment(0xAB61, "Next handle slot", align=Align.INLINE)
d.subroutine(
    0xAB63,
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


d.comment(0xAB63, "A = caller X", align=Align.INLINE)
d.comment(0xAB64, "Push X", align=Align.INLINE)
d.comment(0xAB65, "X=&0F: scan all 16 FCB slots", align=Align.INLINE)
d.label(0xAB67, "loop_scan_fcb_flags")

d.comment(0xAB67, "Load FCB flags", align=Align.INLINE)
d.comment(0xAB6A, "Shift bits 6-7 into bits 7-0", align=Align.INLINE)
d.comment(0xAB6B, "Shift bit into carry for test", align=Align.INLINE)
d.comment(0xAB6C, "Bit 6 clear: skip entry", align=Align.INLINE)
d.comment(0xAB6E, "Restore Y (bit mask)", align=Align.INLINE)
d.comment(0xAB6F, "Test mask bits against flags", align=Align.INLINE)
d.comment(0xAB72, "Zero: no matching bits", align=Align.INLINE)
d.comment(0xAB74, "Matching: restore Y", align=Align.INLINE)
d.comment(0xAB75, "Set bit 5 (updated)", align=Align.INLINE)
d.comment(0xAB77, "Skip clear path", align=Align.INLINE)
d.label(0xAB79, "no_flag_match")

d.comment(0xAB79, "No match: restore Y", align=Align.INLINE)
d.label(0xAB7A, "clear_flag_bits")

d.comment(0xAB7A, "Invert all bits", align=Align.INLINE)
d.comment(0xAB7C, "Clear tested bits in flags", align=Align.INLINE)
d.comment(0xAB7F, "Store updated flags", align=Align.INLINE)
d.label(0xAB82, "next_flag_entry")

d.comment(0xAB82, "Decrement FCB index", align=Align.INLINE)
d.comment(0xAB83, "Loop for all 16 entries", align=Align.INLINE)
d.comment(0xAB85, "Restore original X", align=Align.INLINE)
d.comment(0xAB86, "Back to X", align=Align.INLINE)
d.comment(0xAB87, "Return", align=Align.INLINE)
d.subroutine(
    0xAB88,
    "osword_13_read_rx_flag",
    title="OSWORD &13 sub 8: read RX control block flag",
    description="""Returns byte 1 of the current RX control
block in PB[1].""",
)


d.comment(0xAB88, "Y=1: PB[1] = RX flag location", align=Align.INLINE)
d.comment(0xAB8A, "Load (net_rx_ptr)+1", align=Align.INLINE)
d.comment(0xAB8C, "Y=0", align=Align.INLINE)
d.comment(0xAB8E, "Store to PB[1] and return", align=Align.INLINE)
d.subroutine(
    0xAB91,
    "osword_13_read_rx_port",
    title="OSWORD &13 sub 9: read RX port byte",
    description="""Returns byte &7F of the current RX control
block in PB[1], and stores &80 in PB[2].""",
)


d.comment(0xAB91, "Y=&7F: port byte offset", align=Align.INLINE)
d.comment(0xAB93, "Load (net_rx_ptr)+&7F", align=Align.INLINE)
d.comment(0xAB95, "Y=1", align=Align.INLINE)
d.comment(0xAB97, "Store to PB[1]", align=Align.INLINE)
d.comment(0xAB9A, "A=&80", align=Align.INLINE)
d.comment(0xAB9C, "Store &80 to PB[2]", align=Align.INLINE)
d.comment(0xAB9E, "Return", align=Align.INLINE)
d.subroutine(
    0xAB9F,
    "osword_13_read_error",
    title="OSWORD &13 sub 10: read error flag",
    description="""Returns the latched FS last-error byte
([`hazel_fs_last_error`](label:hazel_fs_last_error)) in `PB[1]`. Falls through
into [`store_a_to_pb_1`](label:store_a_to_pb_1).""",
)


d.comment(0xAB9F, "Load error flag", align=Align.INLINE)
d.label(0xABA2, "store_a_to_pb_1")

d.subroutine(
    0xABA2,
    "store_a_to_pb_1",
    title="Store A to OSWORD parameter block at offset 1",
    description="""Increments Y to 1 and stores A into the
OSWORD parameter block via (ws_ptr_hi),Y.
Used by OSWORD 13 sub-handlers to return a
single result byte.""",
    on_entry={"A": "value to store"},
    on_exit={"Y": "1"},
)


d.comment(0xABA2, "Y=1: parameter block offset 1", align=Align.INLINE)
d.comment(0xABA3, "Store result to PB[1]", align=Align.INLINE)
d.comment(0xABA5, "Return", align=Align.INLINE)
d.subroutine(
    0xABA6,
    "osword_13_read_context",
    title="OSWORD &13 sub 11: read context byte",
    description="""Returns the FS context/error code
([`hazel_fs_error_code`](label:hazel_fs_error_code)) in `PB[1]` when bit 7 is
clear; if bit 7 is set the value is left alone (the BPL skips the
store). Tail-merges into [`store_a_to_pb_1`](label:store_a_to_pb_1).""",
)


d.comment(0xABA6, "Load context byte", align=Align.INLINE)
d.comment(0xABA9, "Bit 7 clear: store context to PB", align=Align.INLINE)
d.subroutine(
    0xABAB,
    "osword_13_read_free_bufs",
    title="OSWORD &13 sub 14: read printer buffer free space",
    description="""Returns the number of free bytes remaining in
the printer spool buffer (&6F minus spool_buf_idx)
in PB[1]. The buffer starts at offset &25 and can
hold up to &4A bytes of spool data.""",
)


d.comment(0xABAB, "Total buffers = &6F", align=Align.INLINE)
d.comment(0xABAD, "PB-to-WS direction (write)", align=Align.INLINE)
d.comment(0xABAE, "Free = &6F - spool_buf_idx", align=Align.INLINE)
d.comment(0xABB1, "Non-negative: store free count to PB", align=Align.INLINE)
d.subroutine(
    0xABB3,
    "osword_13_read_ctx_3",
    title="OSWORD &13 sub 15: read retry counts",
    description="""Returns the three retry count values in
PB[1..3]: PB[1] = transmit retry count
(default &FF = 255), PB[2] = receive poll
count (default &28 = 40), PB[3] = machine
peek retry count (default &0A = 10). Setting
transmit retries to 0 means retry forever.""",
)


d.comment(0xABB3, "Next ctx byte", align=Align.INLINE)
d.comment(0xABB4, "Return", align=Align.INLINE)
d.comment(0xABB7, "Store to PB[Y]", align=Align.INLINE)
d.comment(0xABB9, "Done 3 bytes?", align=Align.INLINE)
d.comment(0xABBB, "No: loop", align=Align.INLINE)
d.comment(0xABBD, "Return", align=Align.INLINE)
d.subroutine(
    0xABBE,
    "osword_13_write_ctx_3",
    title="OSWORD &13 sub 16: write retry counts",
    description="""Sets the three retry count values from
PB[1..3]: PB[1] = transmit retry count,
PB[2] = receive poll count, PB[3] = machine
peek retry count.""",
)


d.comment(0xABBE, "Next byte offset", align=Align.INLINE)
d.comment(0xABBF, "Load PB[Y]", align=Align.INLINE)
d.comment(0xABC1, "Store to tx_retry_count[Y]", align=Align.INLINE)
d.comment(0xABC4, "Done 3 bytes?", align=Align.INLINE)
d.comment(0xABC6, "No: loop", align=Align.INLINE)
d.comment(0xABC8, "Return", align=Align.INLINE)
d.subroutine(
    0xABC9,
    "osword_13_bridge_query",
    title="OSWORD &13 sub 17: query bridge status",
    description="""Calls init_bridge_poll, then returns the
bridge status. If bridge_status is &FF (no bridge),
stores 0 in PB[0]. Otherwise stores bridge_status
in PB[1] and conditionally updates PB[3]
based on station comparison.""",
)


d.comment(0xABC9, "Poll for bridge", align=Align.INLINE)
d.comment(0xABCC, "Y=0", align=Align.INLINE)
d.comment(0xABCE, "Load bridge status", align=Align.INLINE)
d.comment(0xABD1, "Is it &FF (no bridge)?", align=Align.INLINE)
d.comment(0xABD3, "No: bridge found", align=Align.INLINE)
d.comment(0xABD6, "PB[0] = 0 (no bridge)", align=Align.INLINE)
d.label(0xABDB, "bridge_found")

d.comment(0xABDB, "Y=1", align=Align.INLINE)
d.comment(0xABDC, "PB[1] = bridge status", align=Align.INLINE)
d.comment(0xABDE, "Advance Y", align=Align.INLINE)
d.comment(0xABDF, "Y=3", align=Align.INLINE)
d.comment(0xABE0, "Load PB[3] (caller value)", align=Align.INLINE)
d.comment(0xABE2, "Zero: use default station", align=Align.INLINE)
d.label(0xABE4, "compare_bridge_status")

d.comment(0xABE4, "Compare with bridge status", align=Align.INLINE)
# UNMAPPED: d.label(0xABC5, "bridge_err_table")

d.comment(0xABE7, "Non-zero: take return path", align=Align.INLINE)
d.comment(0xABE9, "Same: confirm station", align=Align.INLINE)
d.label(0xABEB, "use_default_station")

d.comment(0xABEB, "Load default from fs_server_net", align=Align.INLINE)
d.label(0xABEE, "store_bridge_station")

d.comment(0xABEE, "Store to PB[3]", align=Align.INLINE)
d.label(0xABF0, "rts_bridge_query")

d.comment(0xABF0, "Return", align=Align.INLINE)
d.index_base(0xABF1, "bridge_txcb_init_table")

for i in range(4):
    d.byte(0xABF1 + i)

d.comment(0xABF1, "TX 0: ctrl = &82 (immediate mode)", align=Align.INLINE)
d.comment(0xABF2, "TX 1: port = &9C (bridge discovery)", align=Align.INLINE)
d.comment(0xABF3, "TX 2: dest station = &FF (broadcast)", align=Align.INLINE)
d.comment(0xABF4, "TX 3: dest network = &FF (all nets)", align=Align.INLINE)
d.comment(0xABF5, "TX 4-9: immediate data payload", align=Align.INLINE)
d.comment(0xABFC, "TX 11: &00 (terminator)", align=Align.INLINE)
d.label(0xABFD, "bridge_rxcb_init_data")
d.comment(0xABFD, "RX 0: ctrl = &7F (receive)", align=Align.INLINE)
d.comment(0xABFE, "RX 1: port = &9C (bridge discovery)", align=Align.INLINE)
d.comment(0xABFF, "RX 2: station = &00 (any)", align=Align.INLINE)
d.comment(0xAC00, "RX 3: network = &00 (any)", align=Align.INLINE)
d.comment(0xAC03, "RX 6: extended addr fill (&FF)", align=Align.INLINE)
d.comment(0xAC04, "RX 7: extended addr fill (&FF)", align=Align.INLINE)
d.comment(0xAC06, "RX 9: buf end hi (&0D) -> &0D74", align=Align.INLINE)
d.label(0xAC09, "init_bridge_poll")

d.subroutine(
    0xAC09,
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


d.comment(0xAC09, "Check bridge status", align=Align.INLINE)
d.comment(0xAC0C, "Is it &FF (uninitialised)?", align=Align.INLINE)
d.comment(0xAC0E, "No: bridge already active, return", align=Align.INLINE)
d.comment(0xAC10, "Save Y", align=Align.INLINE)
d.comment(0xAC11, "Preserve Y on stack", align=Align.INLINE)
d.comment(0xAC12, "Y=&18: workspace offset for init", align=Align.INLINE)
d.comment(0xAC14, "X=&0B: 12 bytes to copy", align=Align.INLINE)
d.comment(0xAC16, "Rotate econet_flags right (save flag)", align=Align.INLINE)
d.label(0xAC19, "loop_copy_bridge_init")

d.comment(0xAC19, "Load init data byte", align=Align.INLINE)
d.comment(0xAC1C, "Store to workspace", align=Align.INLINE)
d.comment(0xAC1E, "Load TXCB template byte", align=Align.INLINE)
d.comment(0xAC21, "Store to TX control block", align=Align.INLINE)
d.comment(0xAC23, "Next workspace byte", align=Align.INLINE)
d.comment(0xAC24, "Next template byte", align=Align.INLINE)
d.comment(0xAC25, "Loop for all 12 bytes", align=Align.INLINE)
d.comment(0xAC27, "Store X (-1) as bridge counter", align=Align.INLINE)
d.comment(0xAC2A, "Restore econet_flags flag", align=Align.INLINE)
d.label(0xAC2D, "loop_wait_ws_status")

d.comment(0xAC2D, "Shift ws_0d60 left (check status)", align=Align.INLINE)
d.comment(0xAC30, "C=0: status clear, retry", align=Align.INLINE)
d.comment(0xAC32, "Control byte &82 for TX", align=Align.INLINE)
d.comment(0xAC34, "Set in TX control block", align=Align.INLINE)
d.comment(0xAC36, "Data block at &00C0", align=Align.INLINE)
d.comment(0xAC38, "Set NMI TX block low", align=Align.INLINE)
d.comment(0xAC3A, "High byte = 0 (page 0)", align=Align.INLINE)
d.comment(0xAC3C, "Set NMI TX block high", align=Align.INLINE)
d.comment(0xAC3E, "Begin Econet transmission", align=Align.INLINE)
d.label(0xAC41, "loop_wait_tx_done")

d.comment(0xAC41, "Test TX control block bit 7", align=Align.INLINE)
d.comment(0xAC43, "Negative: TX still in progress", align=Align.INLINE)
d.comment(0xAC45, "Push X (saved across delay)", align=Align.INLINE)
d.comment(0xAC46, "A=&13: OSBYTE 'wait for VSYNC'", align=Align.INLINE)
d.comment(0xAC4B, "Restore caller's X", align=Align.INLINE)
d.comment(0xAC4C, "Y=&18: status-byte offset", align=Align.INLINE)
d.comment(0xAC4E, "Load bridge response", align=Align.INLINE)
d.comment(0xAC50, "Negative: bridge responded", align=Align.INLINE)
d.comment(0xAC52, "Advance retry counter by 8", align=Align.INLINE)
d.comment(0xAC55, "Positive: retry poll loop", align=Align.INLINE)
d.label(0xAC57, "bridge_responded")

d.comment(0xAC57, "Set response to &3F (OK)", align=Align.INLINE)
d.comment(0xAC59, "Store to workspace", align=Align.INLINE)
d.comment(0xAC5B, "Restore saved Y", align=Align.INLINE)
d.comment(0xAC5C, "Result byte to Y", align=Align.INLINE)
d.comment(0xAC5D, "Load bridge status", align=Align.INLINE)
d.comment(0xAC60, "X = bridge status", align=Align.INLINE)
d.comment(0xAC61, "Invert (presence -> absence)", align=Align.INLINE)
d.comment(0xAC63, "Status was &FF: return (no bridge)", align=Align.INLINE)
d.comment(0xAC65, "Return bridge station in A", align=Align.INLINE)
d.label(0xAC66, "rts_bridge_poll")

d.comment(0xAC66, "Return", align=Align.INLINE)
d.label(0xAC67, "osword_14_handler")

d.subroutine(
    0xAC67,
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


d.entry(0xAC67)
d.comment(0xAC67, "Compare sub-code with 1", align=Align.INLINE)
d.comment(0xAC69, "Sub-code >= 1: handle TX request", align=Align.INLINE)
d.comment(0xAC6B, "Save state", align=Align.INLINE)
d.comment(0xAC6C, "Ensure NFS is currently the selected FS", align=Align.INLINE)
d.comment(0xAC6F, "Pop saved A from the stack frame", align=Align.INLINE)
d.comment(0xAC70, "Y=&23: workspace offset for params", align=Align.INLINE)
d.comment(0xAC72, "Set owner access mask", align=Align.INLINE)
d.label(0xAC75, "loop_copy_txcb_init")

d.comment(0xAC75, "Load TXCB init byte", align=Align.INLINE)
d.comment(0xAC78, "Non-zero: use template value", align=Align.INLINE)
d.comment(0xAC7A, "Zero: use workspace default value", align=Align.INLINE)
d.label(0xAC7D, "store_txcb_init_byte")

d.comment(0xAC7D, "Store to workspace", align=Align.INLINE)
d.comment(0xAC7F, "Next byte down", align=Align.INLINE)
d.comment(0xAC80, "Until Y reaches &17", align=Align.INLINE)
d.comment(0xAC82, "Loop for all bytes", align=Align.INLINE)
d.comment(0xAC84, "Next byte", align=Align.INLINE)
d.comment(0xAC85, "Set net_tx_ptr low byte", align=Align.INLINE)
d.label(0xAC87, "store_osword_pb_ptr")

d.subroutine(
    0xAC87,
    "store_osword_pb_ptr",
    title="Store workspace pointer+1 to NFS workspace",
    description="""Computes ws_ptr_hi + 1 and stores the resulting
16-bit address at workspace offset &1C via
store_ptr_at_ws_y. Then reads PB byte 1 (the
transfer length) and adds ws_ptr_hi to compute
the buffer end pointer, stored at workspace
offset &20.""",
)


d.comment(0xAC87, "Y=&1C: workspace offset for PB pointer", align=Align.INLINE)
d.comment(0xAC89, "Load PB page number", align=Align.INLINE)
d.comment(0xAC8B, "PB starts at next page boundary (+1)", align=Align.INLINE)
d.comment(0xAC8D, "Store PB start pointer at ws[&1C]", align=Align.INLINE)
d.comment(0xAC90, "Y=1: PB byte 1 (transfer length)", align=Align.INLINE)
d.comment(0xAC92, "Load transfer length from PB", align=Align.INLINE)
d.comment(0xAC94, "Y=&20: TXCB offset", align=Align.INLINE)
d.comment(0xAC96, "Add PB base for buffer end address", align=Align.INLINE)
d.comment(0xAC98, "Store PB pointer to workspace", align=Align.INLINE)
d.comment(0xAC9B, "Y=2: parameter offset", align=Align.INLINE)
d.comment(0xAC9D, "Control byte &90", align=Align.INLINE)
d.comment(0xAC9F, "Set escapable flag", align=Align.INLINE)
d.comment(0xACA1, "Store control byte to PB", align=Align.INLINE)
d.label(0xACA5, "loop_copy_ws_to_pb")

d.comment(0xACA5, "Load workspace data", align=Align.INLINE)
d.comment(0xACA8, "Store to parameter block", align=Align.INLINE)
d.comment(0xACAA, "Next byte", align=Align.INLINE)
d.comment(0xACAB, "Until Y reaches 7", align=Align.INLINE)
d.comment(0xACAD, "Loop for 3 bytes (Y=4,5,6)", align=Align.INLINE)
d.comment(0xACAF, "Read nfs_workspace_hi", align=Align.INLINE)
d.comment(0xACB1, "Store to net_tx_ptr_hi", align=Align.INLINE)
d.comment(0xACB3, "Enable interrupts", align=Align.INLINE)
d.comment(0xACB6, "Y=&20: workspace offset", align=Align.INLINE)
d.comment(0xACB8, "Set to &FF (pending)", align=Align.INLINE)
d.comment(0xACBA, "Mark send pending in workspace", align=Align.INLINE)
d.comment(0xACBD, "Also mark offset &21", align=Align.INLINE)
d.comment(0xACBF, "Y=&19: control offset", align=Align.INLINE)
d.comment(0xACC1, "Control byte &90", align=Align.INLINE)
d.comment(0xACC3, "Store to workspace", align=Align.INLINE)
d.comment(0xACC5, "Y=&18: RX control offset", align=Align.INLINE)
d.comment(0xACC6, "Control byte &7F", align=Align.INLINE)
d.comment(0xACC8, "Store RX control", align=Align.INLINE)
d.comment(0xACCA, "Wait for TX acknowledgement", align=Align.INLINE)
d.label(0xACCD, "store_ptr_at_ws_y")

d.subroutine(
    0xACCD,
    "store_ptr_at_ws_y",
    title="Store 16-bit pointer at workspace offset Y",
    description="""Writes a 16-bit address to (nfs_workspace)+Y.
The low byte comes from A; the high byte is
computed from table_idx plus carry,
supporting pointer arithmetic across page
boundaries.""",
    on_entry={"a": "pointer low byte", "y": "workspace offset", "c": "carry for high byte addition"},
)


d.comment(0xACCD, "Store address low byte at ws[Y]", align=Align.INLINE)
d.comment(0xACCF, "Advance to high byte offset", align=Align.INLINE)
d.comment(0xACD0, "Load high byte base (table_idx)", align=Align.INLINE)
d.comment(0xACD2, "Add carry for page crossing", align=Align.INLINE)
d.comment(0xACD4, "Store address high byte at ws[Y+1]", align=Align.INLINE)
d.comment(0xACD6, "Return", align=Align.INLINE)
d.label(0xACD7, "handle_tx_request")

d.subroutine(
    0xACD7,
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


d.comment(0xACD7, "Save processor flags", align=Align.INLINE)
d.comment(0xACD8, "Y=1: workspace offset", align=Align.INLINE)
d.comment(0xACDA, "Load station number from PB", align=Align.INLINE)
d.comment(0xACDC, "X = station number", align=Align.INLINE)
d.comment(0xACDE, "Load network number from PB", align=Align.INLINE)
d.comment(0xACE0, "Y=3: workspace start offset", align=Align.INLINE)
d.comment(0xACE1, "Store Y as ws_ptr_lo", align=Align.INLINE)
d.comment(0xACE3, "Y=&72: workspace offset for dest", align=Align.INLINE)
d.comment(0xACE5, "Store network to workspace", align=Align.INLINE)
d.comment(0xACE7, "Y=&71", align=Align.INLINE)
d.comment(0xACE8, "A = station (from X)", align=Align.INLINE)
d.comment(0xACE9, "Store station to workspace", align=Align.INLINE)
d.comment(0xACEB, "Restore flags from PHP", align=Align.INLINE)
d.comment(0xACEC, "Non-zero sub-code: handle burst", align=Align.INLINE)
d.label(0xACEE, "loop_send_pb_chars")

d.comment(0xACEE, "Load current offset", align=Align.INLINE)
d.comment(0xACF0, "Advance offset for next byte", align=Align.INLINE)
d.comment(0xACF2, "Load next char from PB", align=Align.INLINE)
d.comment(0xACF4, "Zero: end of data, return", align=Align.INLINE)
d.comment(0xACF6, "Y=&7D: workspace pointer offset", align=Align.INLINE)
d.comment(0xACF8, "Store char to RX buffer", align=Align.INLINE)
d.comment(0xACFA, "Save char for later test", align=Align.INLINE)
d.comment(0xACFB, "Init workspace copy for wide xfer", align=Align.INLINE)
d.comment(0xACFE, "Set carry", align=Align.INLINE)
d.comment(0xACFF, "Set bit 7: Tube needs release", align=Align.INLINE)
d.comment(0xAD01, "Enable IRQ and send packet", align=Align.INLINE)
d.label(0xAD04, "loop_bridge_tx_delay")

d.comment(0xAD04, "Delay countdown", align=Align.INLINE)
d.comment(0xAD05, "Loop while X != 0", align=Align.INLINE)
d.comment(0xAD07, "Restore char", align=Align.INLINE)
d.comment(0xAD08, "Test if char was CR (&0D)", align=Align.INLINE)
d.comment(0xAD0A, "Loop while not CR", align=Align.INLINE)
d.comment(0xAD0C, "CR sent: return", align=Align.INLINE)
d.label(0xAD0D, "handle_burst_xfer")

d.subroutine(
    0xAD0D,
    "handle_burst_xfer",
    title="OSWORD &14 burst-transfer path: extend buffer end and TX",
    description="""Reached from [`handle_tx_request`](label:handle_tx_request)'s `BNE` at
`&ACEC`. Calls [`init_ws_copy_wide`](label:init_ws_copy_wide) to copy the
workspace TXCB template into the wide-mode workspace slot, then
extends the buffer end-byte at `(net_rx_ptr)+&7B` by `3` to
account for the 3-byte burst header before falling through into
[`enable_irq_and_poll`](label:enable_irq_and_poll), which re-enables IRQs and
tail-jumps to [`send_net_packet`](label:send_net_packet).""",
    on_entry={"net_rx_ptr": "set up by handle_tx_request (dest station/network already stored at +&71/&72)"},
)


d.comment(0xAD0D, "Init workspace for wide copy", align=Align.INLINE)
d.comment(0xAD10, "Y=&7B: end-byte offset", align=Align.INLINE)
d.comment(0xAD12, "Load buffer size", align=Align.INLINE)
d.comment(0xAD14, "Add 3 (end-of-buffer adjust)", align=Align.INLINE)
d.comment(0xAD16, "Store adjusted size", align=Align.INLINE)
d.label(0xAD18, "enable_irq_and_poll")

d.subroutine(
    0xAD18,
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


d.comment(0xAD18, "Re-enable IRQs", align=Align.INLINE)
d.comment(0xAD19, "Send packet and return", align=Align.INLINE)
d.subroutine(
    0xAD1C,
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


d.entry(0xAD1C)
d.label(0xAD1C, "netv_handler")

d.comment(0xAD1C, "Save processor flags", align=Align.INLINE)
d.comment(0xAD1D, "Save A", align=Align.INLINE)
d.comment(0xAD1E, "Save X", align=Align.INLINE)
d.comment(0xAD1F, "Push X", align=Align.INLINE)
d.comment(0xAD20, "Save Y", align=Align.INLINE)
d.comment(0xAD21, "Push Y", align=Align.INLINE)
d.comment(0xAD22, "Get stack pointer", align=Align.INLINE)
d.comment(0xAD23, "Read OSWORD number from stack", align=Align.INLINE)
d.comment(0xAD26, "OSWORD >= 9?", align=Align.INLINE)
d.comment(0xAD28, "Yes: out of range, restore + return", align=Align.INLINE)
d.comment(0xAD2A, "X = OSWORD number", align=Align.INLINE)
d.comment(0xAD2B, "Push handler address for dispatch", align=Align.INLINE)
d.label(0xAD2E, "restore_regs_return")

d.comment(0xAD2E, "Restore Y", align=Align.INLINE)
d.comment(0xAD2F, "Back to Y", align=Align.INLINE)
d.comment(0xAD30, "Restore X", align=Align.INLINE)
d.comment(0xAD31, "Back to X", align=Align.INLINE)
d.comment(0xAD32, "Restore A", align=Align.INLINE)
d.comment(0xAD33, "Restore flags", align=Align.INLINE)
d.comment(0xAD34, "Return", align=Align.INLINE)
d.label(0xAD35, "push_osword_handler_addr")

d.subroutine(
    0xAD35,
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
d.comment(0xAD35, "Load handler high byte from hi-table column X", align=Align.INLINE)
d.comment(0xAD38, "Push for the eventual RTS dispatch", align=Align.INLINE)
d.comment(0xAD39, "Load handler low byte from lo-table column X", align=Align.INLINE)
d.comment(0xAD3C, "Push lo so RTS pulls (lo, hi)+1 -> handler entry", align=Align.INLINE)
d.comment(0xAD3D, "Reload original OSWORD number into A for the handler", align=Align.INLINE)
d.comment(0xAD3F, "RTS jumps to handler with A=OSWORD number", align=Align.INLINE)
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
d.index_base(0xAD49, "netv_dispatch_hi")
d.banner(
    0xAD49,
    title="NETV reason-code dispatch high-byte table (9 entries)",
    description="""Read by [`push_osword_handler_addr`](label:push_osword_handler_addr) as
`LDA &AD29,X`. The dispatcher pushes the hi byte first then the
lo, so RTS lands on `target` (the table stores `target-1`).""",
)
for addr in range(0xAD49, 0xAD52):
    d.byte(addr)
d.entry(0xAD52)


d.subroutine(
    0xAD52,
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


d.comment(0xAD52, "Read the MOS stack frame holding caller flags", align=Align.INLINE)
d.comment(0xAD53, "Shift carry out of caller P (stack[&106+X])", align=Align.INLINE)
d.comment(0xAD56, "Carry is now cleared in caller P", align=Align.INLINE)
d.comment(0xAD59, "A = original Y", align=Align.INLINE)
d.comment(0xAD5A, "Y=&DA: workspace osword-4 result offset", align=Align.INLINE)
d.comment(0xAD5C, "Store Y at (nfs_workspace)+&DA", align=Align.INLINE)
d.comment(0xAD5E, "A=0: clear A for the abort path", align=Align.INLINE)
d.label(0xAD60, "tx_econet_abort")

d.subroutine(
    0xAD60,
    "tx_econet_abort",
    title="Send Econet abort/disconnect packet",
    description="""Stores the abort code in workspace, configures
the TX control block with control byte &80
(immediate operation flag), and transmits the
abort packet. Used to cleanly disconnect from
a remote station during error recovery.""",
    on_entry={"a": "abort code (stored in workspace before TX)"},
)


d.comment(0xAD60, "Y=&D9: workspace offset for the abort code byte", align=Align.INLINE)
d.comment(0xAD62, "Store the abort code (passed in A) at workspace[&D9]", align=Align.INLINE)
d.comment(0xAD64, "A=&80: control = immediate-operation flag", align=Align.INLINE)
d.comment(0xAD66, "Y=&0C: TXCB control-byte offset", align=Align.INLINE)
d.comment(0xAD68, "Set TXCB[&0C] = &80 (immediate / abort)", align=Align.INLINE)
d.comment(0xAD6A, "Save current net_tx_ptr low (we'll repoint TX at the abort packet)", align=Align.INLINE)
d.comment(0xAD6C, "Push it for restore on exit", align=Align.INLINE)
d.comment(0xAD6D, "Save net_tx_ptr high too", align=Align.INLINE)
d.comment(0xAD6F, "Push it", align=Align.INLINE)
d.comment(0xAD70, "TX low = &0C (abort packet starts at workspace[&0C])", align=Align.INLINE)
d.comment(0xAD72, "Get nfs_workspace high byte", align=Align.INLINE)
d.comment(
    0xAD74, "TX high = workspace page (so net_tx_ptr now points at the abort packet in workspace)", align=Align.INLINE
)
d.comment(0xAD76, "Send the abort packet via the standard TX path", align=Align.INLINE)
d.comment(0xAD79, "A=&3F: TXCB status = abort-complete sentinel", align=Align.INLINE)
d.comment(0xAD7B, "Write status via (net_tx_ptr,X) -- mark TX done", align=Align.INLINE)
d.comment(0xAD7D, "Pull saved net_tx_ptr high", align=Align.INLINE)
d.comment(0xAD7E, "Restore", align=Align.INLINE)
d.comment(0xAD80, "Pull saved net_tx_ptr low", align=Align.INLINE)
d.comment(0xAD81, "Restore -- caller's TX state intact", align=Align.INLINE)
d.comment(0xAD83, "Return", align=Align.INLINE)
d.label(0xAD84, "netv_claim_release")

d.subroutine(
    0xAD84,
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
    0xAD84,
    "Y = OSWORD parameter-block pointer high byte (used as an 'unrecognised' sentinel below)",
    align=Align.INLINE,
)
d.entry(0xAD84)
d.comment(0xAD86, "Code &81? (compatibility shortcut for one specific claim type)", align=Align.INLINE)
d.comment(0xAD88, "Yes: skip table scan, use match-result with Y already set non-zero", align=Align.INLINE)
d.comment(0xAD8A, "Y=1: state 2 marker", align=Align.INLINE)
d.comment(0xAD8C, "X=&0A: scan first 11 entries (table indices 0..&0A)", align=Align.INLINE)
d.comment(0xAD8E, "Look up A in the claim code table", align=Align.INLINE)
d.comment(0xAD91, "Match: handle as state 2", align=Align.INLINE)
d.comment(0xAD93, "DEY: Y=0 (state 3 marker, two DEYs from 1)", align=Align.INLINE)
d.comment(0xAD94, "Y=-1: flag second range", align=Align.INLINE)
d.comment(0xAD95, "X=&11: scan all 18 entries (state 3 also accepts the extended range)", align=Align.INLINE)
d.comment(0xAD97, "Look up A again with extended range", align=Align.INLINE)
d.comment(0xAD9A, "Match: handle as state 3", align=Align.INLINE)
d.comment(0xAD9C, "Y=1 again (no match found, will return below)", align=Align.INLINE)
d.label(0xAD9D, "process_match_result")

d.comment(0xAD9D, "X=2: default state code passed to tx_econet_abort", align=Align.INLINE)
d.comment(0xAD9F, "Move match marker (Y) into A for the BEQ test", align=Align.INLINE)
d.comment(0xADA0, "Y=0 (no match): return without action", align=Align.INLINE)
d.comment(0xADA2, "Save flags so we can branch later on Y's sign", align=Align.INLINE)
d.comment(0xADA3, "Y > 0 (state 2): skip the X bump", align=Align.INLINE)
d.comment(0xADA5, "State 3: X=3 (different abort code)", align=Align.INLINE)
d.label(0xADA6, "save_tube_state")

d.comment(0xADA6, "Y=&DC: workspace offset for tube state bytes", align=Align.INLINE)
d.label(0xADA8, "loop_save_tube_bytes")

d.comment(0xADA8, "Read tube_claimed_id,Y", align=Align.INLINE)
d.comment(0xADAB, "Save in workspace[&DC..]", align=Align.INLINE)
d.comment(0xADAD, "Step backwards", align=Align.INLINE)
d.comment(0xADAE, "Done at &DA?", align=Align.INLINE)
d.comment(0xADB0, "Loop while Y > &DA (saves &DA, &DB, &DC -- 3 bytes)", align=Align.INLINE)
d.comment(0xADB2, "Move state code (2 or 3) into A for the abort", align=Align.INLINE)
d.comment(0xADB3, "Send abort with the state code", align=Align.INLINE)
d.comment(0xADB6, "Restore the saved flags (Y's sign)", align=Align.INLINE)
d.comment(0xADB7, "Y was positive (state 2): just return", align=Align.INLINE)
d.comment(0xADB9, "A=&7F: 'pending response' control value", align=Align.INLINE)
d.comment(0xADBB, "Y=&0C: TXCB control offset", align=Align.INLINE)
d.comment(0xADBD, "Mark TXCB as pending", align=Align.INLINE)
d.label(0xADBF, "loop_poll_ws_status")

d.comment(0xADBF, "Read TXCB status byte", align=Align.INLINE)
d.comment(0xADC1, "Bit 7 still clear: keep polling for response", align=Align.INLINE)
d.comment(0xADC3, "Capture S so we can patch the caller's stack frame", align=Align.INLINE)
d.comment(0xADC4, "Y=&DD: highest workspace offset for the response copy", align=Align.INLINE)
d.comment(0xADC6, "Read first response byte (workspace[&DD])", align=Align.INLINE)
d.comment(0xADC8, "Set bit 6 and bit 2", align=Align.INLINE)
d.comment(
    0xADCA, "Always taken (after ORA result is non-zero); store into stack[&106+X] then walk down", align=Align.INLINE
)
d.label(0xADCC, "loop_restore_stack")

d.comment(0xADCC, "Step Y down", align=Align.INLINE)
d.comment(0xADCD, "Step X down (stack offset)", align=Align.INLINE)
d.comment(0xADCE, "Read next workspace byte", align=Align.INLINE)
d.label(0xADD0, "store_stack_byte")

d.comment(0xADD0, "Patch caller's stack frame at &106+X", align=Align.INLINE)
d.comment(0xADD3, "Reached &DA (lower workspace bound)?", align=Align.INLINE)
d.comment(0xADD5, "No: keep restoring", align=Align.INLINE)
d.label(0xADD7, "rts_claim_release")

d.comment(0xADD7, "Return", align=Align.INLINE)
d.subroutine(
    0xADD8,
    "match_rx_code",
    title="Search receive code table for match",
    description="""Scans a table of receive operation codes
starting at index X, comparing each against A.
Returns with Z set if a match is found, Z clear
if the end-of-table marker is reached.""",
    on_entry={"a": "receive code to match", "x": "starting table index"},
    on_exit={"z": "set if match found"},
)


d.comment(0xADD8, "Compare A with table entry at index X", align=Align.INLINE)
d.comment(0xADDB, "Match: return with Z set", align=Align.INLINE)
d.comment(0xADDD, "Step to next earlier table entry", align=Align.INLINE)
d.comment(0xADDE, "Loop while X >= 0 (table walked top-down)", align=Align.INLINE)
d.label(0xADE0, "rts_match_rx_code")

d.comment(0xADE0, "Return; Z reflects last CMP", align=Align.INLINE)
d.index_base(0xADE1, "osword_claim_codes")
d.banner(
    0xADE1,
    title="OSWORD per-claim-code lookup table (18 bytes)",
    description="""Looked up by [`match_rx_code`](label:match_rx_code) when an Econet RX
event triggers an OSWORD-related claim. The X register selects an
18-byte slice; bytes encode the claim type (immediate-op,
broadcast, port-specific) used by the dispatcher to decide which
handler chain to install. Per-byte inline comments document each
entry.""",
)
for i in range(18):
    d.byte(0xADE1 + i)

d.comment(0xADE1, "Range 1+2: OSWORD &04", align=Align.INLINE)
d.comment(0xADE2, "Range 1+2: OSWORD &09", align=Align.INLINE)
d.comment(0xADE4, "Range 1+2: OSWORD &14", align=Align.INLINE)
d.comment(0xADE5, "Range 1+2: OSWORD &15", align=Align.INLINE)
d.comment(0xADE7, "Range 1+2: OSWORD &9B", align=Align.INLINE)
d.comment(0xADE8, "Range 1+2: OSWORD &E1", align=Align.INLINE)
d.comment(0xADEA, "Range 1+2: OSWORD &E3", align=Align.INLINE)
d.comment(0xADEB, "Range 1+2: OSWORD &E4", align=Align.INLINE)
d.comment(0xADED, "Range 2 only: OSWORD &0C", align=Align.INLINE)
d.comment(0xADEE, "Range 2 only: OSWORD &0F", align=Align.INLINE)
d.comment(0xADEF, "Range 2 only: OSWORD &79", align=Align.INLINE)
d.comment(0xADF2, "Range 2 only: OSWORD &87", align=Align.INLINE)
d.subroutine(
    0xADF3,
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


d.comment(0xADF3, "Y=&0E: scan 15 bytes (offsets 14..0) of the PB", align=Align.INLINE)
d.comment(0xADF5, "Is the OSWORD number 7?", align=Align.INLINE)
d.comment(0xADF7, "Yes: handle as either 7 or 8 -- both copy PB to ws", align=Align.INLINE)
d.comment(0xADF9, "Is the OSWORD number 8?", align=Align.INLINE)
d.comment(0xADFB, "Neither 7 nor 8: return early (other OSWORDs handled elsewhere)", align=Align.INLINE)
d.label(0xADFD, "copy_pb_to_ws")

d.comment(0xADFD, "X=&DB: workspace offset for the PB copy", align=Align.INLINE)
d.comment(
    0xADFF,
    "Temporarily reuse nfs_workspace as the destination low byte (high byte already points at the workspace page)",
    align=Align.INLINE,
)
d.label(0xAE01, "loop_copy_pb_to_ws")

d.comment(0xAE01, "Read PB[Y]", align=Align.INLINE)
d.comment(0xAE03, "Write to (nfs_workspace),Y -- effectively writes to workspace[&DB+Y]", align=Align.INLINE)
d.comment(0xAE05, "Step backwards through the 15 bytes", align=Align.INLINE)
d.comment(0xAE06, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xAE08, "Bring Y back to 0 for the next single-byte write", align=Align.INLINE)
d.comment(
    0xAE09,
    "Decrement nfs_workspace low byte: now points at workspace[&DA] (one before the copied region)",
    align=Align.INLINE,
)
d.comment(0xAE0B, "Read original OSWORD number from osbyte_a_copy", align=Align.INLINE)
d.comment(0xAE0D, "Store at workspace[&DA] -- so the abort packet header carries the OSWORD number", align=Align.INLINE)
d.comment(0xAE0F, "Restore nfs_workspace to its proper low byte (Y=0)", align=Align.INLINE)
d.comment(0xAE11, "Y=&14: TXCB control offset", align=Align.INLINE)
d.comment(0xAE13, "A=&E9: status code for OSWORD-passthrough abort", align=Align.INLINE)
d.comment(0xAE15, "Store status at TXCB[&14]", align=Align.INLINE)
d.comment(0xAE17, "A=1: abort code for tx_econet_abort", align=Align.INLINE)
d.comment(0xAE19, "Send the abort packet", align=Align.INLINE)
d.comment(0xAE1C, "Restore nfs_workspace from X (X is unchanged across tx_econet_abort)", align=Align.INLINE)
d.label(0xAE1E, "init_ws_copy_wide")

d.subroutine(
    0xAE1E,
    "init_ws_copy_wide",
    title="Initialise workspace copy in wide mode (14 bytes)",
    description="""Copies 14 bytes to workspace offset &7C.
Falls through to the template-driven copy
loop which handles &FD (skip), &FE (end),
and &FC (page pointer) markers.""",
    on_entry={"x": "template source offset (within ws_txcb_template_data)"},
)


d.comment(0xAE1E, "X=&0D: 14 template bytes to process", align=Align.INLINE)
d.comment(0xAE20, "Y=&7C: workspace destination offset for wide variant", align=Align.INLINE)
d.comment(0xAE22, "BIT &FF unconditionally sets V (the always_set_v_byte trick)", align=Align.INLINE)
d.comment(0xAE25, "V=1 always: skip the narrow-mode prologue and CLV", align=Align.INLINE)
d.label(0xAE27, "init_ws_copy_narrow")

d.subroutine(
    0xAE27,
    "init_ws_copy_narrow",
    title="Initialise workspace copy in narrow mode (27 bytes)",
    description="""Sets up a 27-byte copy to workspace offset &17,
then falls through to ws_copy_vclr_entry for
the template-driven copy loop. Used for the
compact workspace initialisation variant.""",
    on_entry={"x": "template source offset"},
)


d.comment(0xAE27, "Y=&17: workspace destination offset for narrow variant", align=Align.INLINE)
d.comment(0xAE29, "X=&1A: 27 template bytes to process; fall into ws_copy_vclr_entry which CLVs", align=Align.INLINE)
d.label(0xAE2B, "ws_copy_vclr_entry")

d.subroutine(
    0xAE2B,
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


d.comment(0xAE2B, "Clear V: narrow mode (writes via nfs_workspace pointer)", align=Align.INLINE)
d.label(0xAE2C, "loop_copy_ws_template")

d.comment(0xAE2C, "Read next template byte", align=Align.INLINE)
d.comment(0xAE2F, "&FE: end-of-template marker?", align=Align.INLINE)
d.comment(0xAE31, "Yes: finalise and return", align=Align.INLINE)
d.comment(0xAE33, "&FD: skip-this-offset marker?", align=Align.INLINE)
d.comment(0xAE35, "Yes: advance index without storing", align=Align.INLINE)
d.comment(0xAE37, "&FC: substitute-workspace-page-pointer marker?", align=Align.INLINE)
d.comment(0xAE39, "No special marker: store this byte verbatim", align=Align.INLINE)
d.comment(0xAE3B, "Wide path: page pointer is net_rx_ptr's high byte", align=Align.INLINE)
d.comment(0xAE3D, "V=1 (wide): keep the rx_ptr high byte", align=Align.INLINE)
d.comment(0xAE3F, "V=0 (narrow): use nfs_workspace high byte instead", align=Align.INLINE)
d.label(0xAE41, "store_tx_ptr_hi")

d.comment(0xAE41, "Stash whichever page byte we picked into net_tx_ptr_hi", align=Align.INLINE)
d.label(0xAE43, "select_store_target")

d.comment(0xAE43, "V=1 (wide): store via net_rx_ptr,Y", align=Align.INLINE)
d.comment(0xAE45, "V=0 (narrow): store via nfs_workspace,Y", align=Align.INLINE)
d.comment(0xAE47, "Always branch: V is still clear here", align=Align.INLINE)
d.label(0xAE49, "store_via_rx_ptr")

d.comment(0xAE49, "Wide-mode store via net_rx_ptr", align=Align.INLINE)
d.label(0xAE4B, "advance_template_idx")

d.comment(0xAE4B, "Step Y down (workspace offset)", align=Align.INLINE)
d.comment(0xAE4C, "Step X down (template index)", align=Align.INLINE)
d.comment(0xAE4D, "Loop while X >= 0", align=Align.INLINE)
d.label(0xAE4F, "done_ws_template_copy")

d.comment(0xAE4F, "Bump Y back to first written offset", align=Align.INLINE)
d.comment(0xAE50, "Save it as net_tx_ptr low for the caller", align=Align.INLINE)
d.comment(0xAE52, "Return", align=Align.INLINE)
d.index_base(0xAE53, "ws_txcb_template_data")
d.banner(
    0xAE53,
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
    d.byte(0xAE53 + i)

d.comment(0xAE53, "Wide &6F: ctrl=&85", align=Align.INLINE)
d.comment(0xAE55, "Wide &71: skip (dest station)", align=Align.INLINE)
d.comment(0xAE58, "Wide &74: buf start hi=page ptr", align=Align.INLINE)
d.comment(0xAE59, "Wide &75: buf start ext lo", align=Align.INLINE)
d.comment(0xAE5A, "Wide &76: buf start ext hi", align=Align.INLINE)
d.comment(0xAE5B, "Wide &77: buf end lo=&7E", align=Align.INLINE)
d.comment(0xAE5E, "Wide &7A: buf end ext hi", align=Align.INLINE)
d.comment(0xAE5F, "Wide &7B: zero", align=Align.INLINE)
d.comment(0xAE60, "Wide &7C: zero", align=Align.INLINE)
d.comment(0xAE61, "Narrow stop (&FE terminator)", align=Align.INLINE)
d.comment(0xAE64, "Narrow &0E: skip (dest station)", align=Align.INLINE)
d.comment(0xAE67, "Narrow &11: buf start hi=page ptr", align=Align.INLINE)
d.comment(0xAE68, "Narrow &12: buf start ext lo", align=Align.INLINE)
d.comment(0xAE69, "Narrow &13: buf start ext hi", align=Align.INLINE)
d.comment(0xAE6A, "Narrow &14: buf end lo=&DE", align=Align.INLINE)
d.comment(0xAE6D, "Narrow &17: buf end ext hi", align=Align.INLINE)
d.comment(0xAE6E, "Spool stop (&FE terminator)", align=Align.INLINE)
d.comment(0xAE71, "Spool &03: skip (dest network)", align=Align.INLINE)
d.comment(0xAE74, "Spool &06: buf start ext lo", align=Align.INLINE)
d.comment(0xAE75, "Spool &07: buf start ext hi", align=Align.INLINE)
d.comment(0xAE76, "Spool &08: skip (buf end lo)", align=Align.INLINE)
d.comment(0xAE79, "Spool &0B: buf end ext hi", align=Align.INLINE)
d.label(0xAE7A, "netv_spool_check")

d.subroutine(
    0xAE7A,
    "netv_spool_check",
    title="OSWORD 5 handler: check spool PB and reset buffer",
    description="""Handles OSWORD 5 intercepted via NETV. Checks
if X-1 matches osword_pb_ptr and bit 0 of
&00D0 is clear. If both conditions are met,
falls through to reset_spool_buf_state to
reinitialise the spool buffer for new data.""",
    on_entry={"x": "OSWORD parameter block low byte (X-1 compared against osword_pb_ptr)"},
)


d.comment(0xAE7A, "Step counter", align=Align.INLINE)
d.comment(0xAE7B, "Match osword_pb_ptr?", align=Align.INLINE)
d.comment(0xAE7D, "No: return (not our PB)", align=Align.INLINE)
d.comment(0xAE7F, "Load spool state byte", align=Align.INLINE)
d.comment(0xAE81, "Shift bit 0 into C", align=Align.INLINE)
d.comment(0xAE82, "C=1: already active, return", align=Align.INLINE)
d.label(0xAE84, "reset_spool_buf_state")

d.subroutine(
    0xAE84,
    "reset_spool_buf_state",
    title="Reset spool buffer to initial state",
    description="""Sets the spool buffer pointer (`spool_buf_idx`)
to `&21` and the control byte (`ws_0d6a`) to `&41`
(ready for new data). Called after processing a
complete spool data block.""",
    on_entry={},
    on_exit={"a, y": "clobbered"},
)


d.comment(0xAE84, "Buffer start offset = &21", align=Align.INLINE)
d.comment(0xAE86, "Store as buffer pointer", align=Align.INLINE)
d.comment(0xAE89, "Control state &41", align=Align.INLINE)
d.comment(0xAE8B, "Store as spool control state", align=Align.INLINE)
d.label(0xAE8E, "rts_spool_reset")

d.comment(0xAE8E, "Return", align=Align.INLINE)
d.label(0xAE8F, "netv_print_data")

d.subroutine(
    0xAE8F,
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


d.entry(0xAE8F)
d.comment(0xAE8F, "Check Y == 4", align=Align.INLINE)
d.comment(0xAE91, "Non-zero: nothing to print, return", align=Align.INLINE)
d.comment(0xAE93, "A = X (control byte)", align=Align.INLINE)
d.comment(0xAE94, "Step counter back", align=Align.INLINE)
d.comment(0xAE95, "Non-zero: handle spool ctrl byte", align=Align.INLINE)
d.comment(0xAE97, "Read MOS stack frame", align=Align.INLINE)
d.comment(0xAE98, "OR with stack value", align=Align.INLINE)
d.comment(0xAE9B, "Store back to stack", align=Align.INLINE)
d.label(0xAE9E, "loop_drain_printer_buf")

d.comment(0xAE9E, "OSBYTE &91: read buffer", align=Align.INLINE)
d.comment(0xAEA0, "X=3: printer buffer", align=Align.INLINE)
d.comment(0xAEA2, "Read character from buffer", align=Align.INLINE)
d.comment(0xAEA5, "C set: return path", align=Align.INLINE)
d.comment(0xAEA7, "A = extracted character", align=Align.INLINE)
d.comment(0xAEA8, "Add byte to RX buffer", align=Align.INLINE)
d.comment(0xAEAB, "Buffer past &6E limit?", align=Align.INLINE)
d.comment(0xAEAD, "No: read more from buffer", align=Align.INLINE)
d.comment(0xAEAF, "Print accumulated spool data", align=Align.INLINE)
d.comment(0xAEB2, "More room: continue reading", align=Align.INLINE)
d.label(0xAEB4, "append_byte_to_rxbuf")

d.subroutine(
    0xAEB4,
    "append_byte_to_rxbuf",
    title="Append byte to receive buffer",
    description="""Stores A in the receive buffer at the current
buffer index (ws_ptr_lo), then increments the
index. Used to accumulate incoming spool data
bytes before processing.""",
    on_entry={"a": "byte to append"},
)


d.comment(0xAEB4, "Y = spool_buf_idx", align=Align.INLINE)
d.comment(0xAEB7, "Store A at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAEB9, "Advance spool_buf_idx", align=Align.INLINE)
d.comment(0xAEBC, "Return", align=Align.INLINE)
d.label(0xAEBD, "handle_spool_ctrl_byte")

d.subroutine(
    0xAEBD,
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


d.comment(0xAEBD, "Rotate bit 0 into carry", align=Align.INLINE)
d.comment(0xAEBE, "C clear: take check_spool_state path", align=Align.INLINE)
d.comment(0xAEC0, "Load spool control state", align=Align.INLINE)
d.comment(0xAEC2, "Equal: take fill path", align=Align.INLINE)
d.comment(0xAEC3, "Save state byte", align=Align.INLINE)
d.comment(0xAEC4, "Rotate bit 0 into carry", align=Align.INLINE)
d.comment(0xAEC5, "Restore state", align=Align.INLINE)
d.comment(0xAEC6, "C=1: already started, reset", align=Align.INLINE)
d.comment(0xAEC8, "Set bits 0-1 (active + pending)", align=Align.INLINE)
d.comment(0xAECA, "Store updated state", align=Align.INLINE)
d.comment(0xAECC, "Stop: process_spool_data and return", align=Align.INLINE)
d.comment(0xAECD, "A=3: spool-data result code", align=Align.INLINE)
d.comment(0xAECF, "Append result to RX buffer", align=Align.INLINE)
d.comment(0xAED2, "Process the accumulated spool data", align=Align.INLINE)
d.label(0xAED5, "done_spool_ctrl")

d.comment(0xAED5, "Reset spool buffer state", align=Align.INLINE)
d.subroutine(
    0xAED8,
    "process_spool_data",
    title="Transmit accumulated spool buffer data",
    description="""Copies the workspace state to the TX control
block, sends a disconnect reply if the previous
transfer requires acknowledgment, then handles
the spool output sequence by setting up and
sending the pass-through TX buffer.""",
    on_exit={"a": "TX result (from setup_pass_txbuf)"},
)


d.comment(0xAED8, "Y=8: buf_start_lo TXCB offset", align=Align.INLINE)
d.comment(0xAEDA, "Load current spool-buffer index", align=Align.INLINE)
d.comment(0xAEDD, "Store at workspace+8 (buf_start_lo)", align=Align.INLINE)
d.comment(0xAEDF, "Load RX page (= net_rx_ptr_hi)", align=Align.INLINE)
d.comment(0xAEE2, "Store at workspace+9 (buf_start_hi)", align=Align.INLINE)
d.comment(0xAEE4, "Y=5: alt buf_start_hi offset", align=Align.INLINE)
d.comment(0xAEE6, "Store at workspace+5 (also buf-start hi)", align=Align.INLINE)
d.comment(0xAEE8, "Y=&0B: TXCB offset for following copy", align=Align.INLINE)
d.comment(0xAEEA, "X=&26: template offset for vclr region", align=Align.INLINE)
d.comment(0xAEEC, "Copy 12-byte ws-template region (V-clear)", align=Align.INLINE)
d.comment(0xAEEF, "Step back to offset &0A", align=Align.INLINE)
d.comment(0xAEF0, "Read shadow ACR (ws_0d6a)", align=Align.INLINE)
d.comment(0xAEF3, "Save state", align=Align.INLINE)
d.comment(0xAEF4, "Shift bit 7 into C", align=Align.INLINE)
d.comment(0xAEF5, "Restore state", align=Align.INLINE)
d.comment(0xAEF6, "Toggle bit 7", align=Align.INLINE)
d.comment(0xAEF8, "Store updated shadow back to ws_0d6a", align=Align.INLINE)
d.comment(0xAEFB, "Shift bit 0 into bit 1", align=Align.INLINE)
d.comment(0xAEFC, "Store at workspace+&0A", align=Align.INLINE)
d.comment(0xAEFE, "Read vdu_status", align=Align.INLINE)
d.comment(0xAF00, "Push for later restore", align=Align.INLINE)
d.comment(0xAF01, "Clear bit 0 of vdu_status", align=Align.INLINE)
d.comment(0xAF03, "Store updated", align=Align.INLINE)
d.comment(0xAF05, "Y=&22: spool_buf_idx reset value", align=Align.INLINE)
d.comment(0xAF07, "Reset spool_buf_idx", align=Align.INLINE)
d.comment(0xAF0A, "A=0", align=Align.INLINE)
d.comment(0xAF0C, "X=0", align=Align.INLINE)
d.comment(0xAF0D, "Y = workspace high page", align=Align.INLINE)
d.comment(0xAF0F, "Re-enable IRQs (NMI window over)", align=Align.INLINE)
d.comment(0xAF10, "Send disconnect reply", align=Align.INLINE)
d.comment(0xAF13, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF14, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF16, "Return", align=Align.INLINE)
d.label(0xAF17, "check_spool_state")

d.comment(0xAF17, "Read shadow ACR", align=Align.INLINE)
d.comment(0xAF1A, "Shift bit 0 into C", align=Align.INLINE)
d.comment(0xAF1B, "C clear: re-process spool data", align=Align.INLINE)
d.comment(0xAF1D, "Read vdu_status", align=Align.INLINE)
d.comment(0xAF1F, "Push for restore", align=Align.INLINE)
d.comment(0xAF20, "Clear bit 0 of vdu_status", align=Align.INLINE)
d.comment(0xAF22, "Store updated", align=Align.INLINE)
d.comment(0xAF24, "A=&14: TX command byte", align=Align.INLINE)
d.label(0xAF26, "start_spool_retry")

d.comment(0xAF26, "Save TX command", align=Align.INLINE)
d.comment(0xAF27, "X=&0B: tx_econet_txcb_template offset", align=Align.INLINE)
d.comment(0xAF29, "Y=&2D: dest TXCB offset", align=Align.INLINE)
d.label(0xAF2B, "loop_copy_spool_tx")

d.comment(0xAF2B, "Read template byte at tx_econet_txcb_template+X", align=Align.INLINE)
d.comment(0xAF2E, "Store at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAF30, "Decrement Y", align=Align.INLINE)
d.comment(0xAF31, "Decrement X", align=Align.INLINE)
d.comment(0xAF32, "Loop until X wraps below 0", align=Align.INLINE)
d.comment(0xAF34, "Store X (= &FF) as need_release_tube", align=Align.INLINE)
d.comment(0xAF36, "Y=2: workspace offset for source", align=Align.INLINE)
d.comment(0xAF38, "Read (nfs_workspace)+2", align=Align.INLINE)
d.comment(0xAF3A, "Save station", align=Align.INLINE)
d.comment(0xAF3B, "Y=3", align=Align.INLINE)
d.comment(0xAF3C, "Read (nfs_workspace)+3", align=Align.INLINE)
d.comment(0xAF3E, "Y=&25: dest offset in TXCB", align=Align.INLINE)
d.comment(0xAF40, "Store at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAF42, "Y=&23", align=Align.INLINE)
d.comment(0xAF43, "Restore station", align=Align.INLINE)
d.comment(0xAF44, "Store at (net_rx_ptr)+Y", align=Align.INLINE)
d.comment(0xAF46, "X=&0B: rx_palette_txcb_template offset", align=Align.INLINE)
d.comment(0xAF48, "Y=&0B: dest offset in workspace", align=Align.INLINE)
d.label(0xAF4A, "loop_copy_spool_rx")

d.comment(0xAF4A, "Read template byte at rx_palette_txcb_template+X", align=Align.INLINE)
d.comment(0xAF4D, "Compare with &FD (skip-byte marker)", align=Align.INLINE)
d.comment(0xAF4F, "Equal: skip this byte", align=Align.INLINE)
d.comment(0xAF51, "Compare with &FC (page-ptr marker)", align=Align.INLINE)
d.comment(0xAF53, "Not &FC: store as-is", align=Align.INLINE)
d.comment(0xAF55, "&FC: substitute net_rx_ptr_hi", align=Align.INLINE)
d.label(0xAF57, "store_spool_rx_byte")

d.comment(0xAF57, "Store at (nfs_workspace)+Y", align=Align.INLINE)
d.label(0xAF59, "advance_spool_rx_idx")

d.comment(0xAF59, "Next dest", align=Align.INLINE)
d.comment(0xAF5A, "Next source", align=Align.INLINE)
d.comment(0xAF5B, "Loop until X wraps", align=Align.INLINE)
d.comment(0xAF5D, "A=&22: TXCB control byte", align=Align.INLINE)
d.comment(0xAF5F, "Store at net_tx_ptr lo", align=Align.INLINE)
d.comment(0xAF61, "Read net_rx_ptr_hi", align=Align.INLINE)
d.comment(0xAF63, "Store as net_tx_ptr hi", align=Align.INLINE)
d.comment(0xAF65, "Set up the pass-through TX buffer", align=Align.INLINE)
d.comment(0xAF68, "Send the TX packet", align=Align.INLINE)
d.comment(0xAF6B, "A=0: clear net_tx_ptr lo", align=Align.INLINE)
d.comment(0xAF6D, "Store -> net_tx_ptr lo", align=Align.INLINE)
d.comment(0xAF6F, "Read nfs_workspace_hi", align=Align.INLINE)
d.comment(0xAF71, "Store -> net_tx_ptr hi", align=Align.INLINE)
d.comment(0xAF73, "Wait for TX ack", align=Align.INLINE)
d.comment(0xAF76, "Y=&2E: spool result-byte offset", align=Align.INLINE)
d.comment(0xAF78, "Read result via (net_rx_ptr)+Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF5A, "Z: success path", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF5C, "Compare with 3 (retry threshold)", align=Align.INLINE)
d.comment(0xAF7D, "Other: take retry path", align=Align.INLINE)
d.label(0xAF7F, "spool_tx_succeeded")

d.comment(0xAF7F, "Discard saved TX cmd", align=Align.INLINE)
d.comment(0xAF80, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF81, "Restore vdu_status", align=Align.INLINE)
d.comment(0xAF83, "A=0: success-return code", align=Align.INLINE)
d.comment(0xAF85, "Append byte to RX buffer", align=Align.INLINE)
d.comment(0xAF88, "Recurse: process_spool_data", align=Align.INLINE)
d.comment(0xAF8B, "Read shadow ACR", align=Align.INLINE)
d.comment(0xAF8E, "Mask high nibble", align=Align.INLINE)
d.comment(0xAF90, "Store updated shadow", align=Align.INLINE)
d.comment(0xAF93, "Return", align=Align.INLINE)
# UNMAPPED: d.label(0xAF75, "spool_tx_retry")

# UNMAPPED: d.comment(0xAF75, "Save retry counter", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF76, "Pop saved TX cmd", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF77, "Set carry", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF78, "Decrement retry", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF7A, "Non-zero: retry from start_spool_retry", align=Align.INLINE)
# UNMAPPED: d.comment(0xAF7C, "Check the saved retry counter", align=Align.INLINE)
d.comment(0xAF99, "Not 1: take printer_busy_msg path", align=Align.INLINE)
d.label(0xAF9B, "err_printer_busy")

d.subroutine(
    0xAF9B,
    "err_printer_busy",
    title="Raise 'Printer busy' error",
    description="""Loads error code &A6 and tail-calls error_inline_log with the inline
string 'Printer busy'. Called when an attempt is made to enable a
printer server while one is already active. Never returns.""",
)


d.comment(0xAF9B, "A=&A6: 'Printer busy' error code", align=Align.INLINE)
d.comment(0xAF9D, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.comment(0xAFC7, "A=&A7: 'Printer jammed' error code", align=Align.INLINE)
# UNMAPPED: d.label(0xAF92, "printer_busy_msg")

d.comment(0xAFC9, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.label(0xAFDB, "send_disconnect_reply")

d.subroutine(
    0xAFDB,
    "send_disconnect_reply",
    title="Send Econet disconnect reply packet",
    description="""Sets up the TX pointer, copies station
addresses, matches the station in the table,
and sends the response. Waits for
acknowledgment before returning.""",
    on_exit={"a": "TX result code"},
)


d.comment(0xAFDB, "X = caller's TX-ptr low byte", align=Align.INLINE)
d.comment(0xAFDD, "Y = caller's TX-ptr high byte", align=Align.INLINE)
d.comment(0xAFDF, "Save A (the disconnect status to send)", align=Align.INLINE)
d.comment(0xAFE0, "Test if A=0 (broadcast disconnect)", align=Align.INLINE)
d.comment(0xAFE2, "Yes: skip the per-station scan", align=Align.INLINE)
d.comment(0xAFE4, "X=&FF: scan counter -- INX in loop bumps to 0", align=Align.INLINE)
d.comment(0xAFE6, "Y=A: status code (also used as station-table key)", align=Align.INLINE)
d.label(0xAFE7, "loop_scan_disconnect")

d.comment(0xAFE7, "Restore status into A for the compare", align=Align.INLINE)
d.comment(0xAFE8, "Step station-table index", align=Align.INLINE)
d.comment(0xAFE9, "Compare with table[X] at &C230 (per-station status)", align=Align.INLINE)
d.comment(0xAFEC, "Match: verify station address still matches", align=Align.INLINE)
d.comment(0xAFEE, "Reached end of 16-slot table?", align=Align.INLINE)
d.comment(0xAFF0, "No: keep scanning", align=Align.INLINE)
d.comment(0xAFF2, "All slots tested, no match: A=0", align=Align.INLINE)
d.comment(0xAFF4, "Always taken: jump to send-status", align=Align.INLINE)
d.label(0xAFF6, "verify_stn_match")

d.comment(0xAFF6, "Y = matching index", align=Align.INLINE)
d.comment(0xAFF7, "Verify station/network at this slot still matches caller", align=Align.INLINE)
d.comment(0xAFFA, "Mismatch: station moved, keep scanning", align=Align.INLINE)
d.comment(0xAFFC, "Read connection-active flag at &C260+X", align=Align.INLINE)
d.comment(0xAFFF, "Mask to bit 0 (active flag)", align=Align.INLINE)
d.label(0xB001, "send_disconnect_status")

d.comment(0xB001, "Y=0: TX[0] = control byte", align=Align.INLINE)
d.comment(0xB003, "OR active-flag bit into the status", align=Align.INLINE)
d.comment(0xB005, "Save the combined status", align=Align.INLINE)
d.comment(0xB006, "Write it to TX[0]", align=Align.INLINE)
d.comment(0xB008, "Send the disconnect packet via four-way handshake", align=Align.INLINE)
d.comment(0xB00B, "A=&FF: sentinel", align=Align.INLINE)
d.comment(0xB00D, "Y=8: TX[8] / TX[9] = packet trailer markers", align=Align.INLINE)
d.comment(0xB00F, "Write &FF at TX[8]", align=Align.INLINE)
d.comment(0xB011, "Step Y", align=Align.INLINE)
d.comment(0xB012, "Write &FF at TX[9]", align=Align.INLINE)
d.comment(0xB014, "Pull the saved status", align=Align.INLINE)
d.comment(0xB015, "Move into X for the test", align=Align.INLINE)
d.comment(0xB016, "Y=&D1: control byte for ack-mode TXCB[1]", align=Align.INLINE)
d.comment(0xB018, "Pull caller's original A again (was double-saved)", align=Align.INLINE)
d.comment(0xB019, "Push it back", align=Align.INLINE)
d.comment(0xB01A, "A=0: skip the override", align=Align.INLINE)
d.comment(0xB01C, "Non-zero: use Y=&90 (FS reply port instead)", align=Align.INLINE)
d.label(0xB01E, "store_tx_ctrl_byte")

d.comment(0xB01E, "Move chosen control/port into A", align=Align.INLINE)
d.comment(0xB01F, "Y=1: TX[1] is the port byte", align=Align.INLINE)
d.comment(0xB021, "Write to TX[1]", align=Align.INLINE)
d.comment(0xB023, "Move saved status into A", align=Align.INLINE)
d.comment(0xB024, "Y=0: TX[0] for ack poll", align=Align.INLINE)
d.comment(0xB025, "Push the status (we'll EOR with reply below)", align=Align.INLINE)
d.label(0xB026, "loop_wait_disc_tx_ack")

d.comment(0xB026, "A=&7F: marker pattern", align=Align.INLINE)
d.comment(0xB028, "Write to TX[0]", align=Align.INLINE)
d.comment(0xB02A, "Wait for the TX/RX flip", align=Align.INLINE)
d.comment(0xB02D, "Pull saved status (peek without consuming)", align=Align.INLINE)
d.comment(0xB02E, "Push it back", align=Align.INLINE)
d.comment(0xB02F, "EOR with TX[0]: zero iff reply matches saved", align=Align.INLINE)
d.comment(0xB031, "Rotate result; C set if bit 0 differs", align=Align.INLINE)
d.comment(0xB032, "C set: keep waiting", align=Align.INLINE)
d.comment(0xB034, "Discard saved status", align=Align.INLINE)
d.comment(0xB035, "Discard caller's saved A", align=Align.INLINE)
d.comment(0xB036, "Return", align=Align.INLINE)
d.index_base(0xB037, "tx_econet_txcb_template")
d.banner(
    0xB037,
    title="Spool / disconnect TX control-block template (12 bytes)",
    description="""12-byte Econet TXCB initialisation template used by the spool /
disconnect TX paths. Copied into the workspace TXCB at offsets
`&21..&2C` via `(net_rx_ptr),Y`. Destination station and network
are filled in afterwards by the caller. Per-byte inline comments
identify each TXCB field.""",
)
for i in range(12):
    d.byte(0xB037 + i)

d.comment(0xB037, "ctrl=&80 (standard TX)", align=Align.INLINE)
d.comment(0xB038, "port=&9F", align=Align.INLINE)
d.comment(0xB039, "dest station=&00 (filled later)", align=Align.INLINE)
d.comment(0xB03A, "dest network=&00 (filled later)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB006, "buf start lo (&9F)", align=Align.INLINE)
d.comment(0xB03C, "buf start hi (&8E); start = &8EB7", align=Align.INLINE)
d.comment(0xB03D, "buf start ext lo=&FF", align=Align.INLINE)
d.comment(0xB03E, "buf start ext hi=&FF", align=Align.INLINE)
# UNMAPPED: d.comment(0xB00A, "buf end lo (&A7)", align=Align.INLINE)
d.comment(0xB040, "buf end hi (&8E); end = &8EA7", align=Align.INLINE)
d.comment(0xB041, "buf end ext lo=&FF", align=Align.INLINE)
d.comment(0xB042, "buf end ext hi=&FF", align=Align.INLINE)
d.index_base(0xB043, "rx_palette_txcb_template")
d.banner(
    0xB043,
    title="Palette-RX control-block template (12 bytes)",
    description="""12-byte template used by the *PS / palette-RX paths. Copied with
marker processing: `&FD` skips the destination byte (preserving
the existing field), `&FC` substitutes `net_rx_ptr_hi` (the
caller's RX-buffer page). Filled in over the workspace TXCB by
the broadcast-RX setup before the request is dispatched.""",
)
for i in range(12):
    d.byte(0xB043 + i)

d.comment(0xB043, "ctrl=&7F (RX listen)", align=Align.INLINE)
d.comment(0xB044, "port=&9E", align=Align.INLINE)
# UNMAPPED: d.comment(0xB010, "skip: preserve dest station", align=Align.INLINE)
d.comment(0xB048, "buf start hi=page ptr (&FC)", align=Align.INLINE)
d.comment(0xB049, "buf start ext lo=&FF", align=Align.INLINE)
d.comment(0xB04A, "buf start ext hi=&FF", align=Align.INLINE)
d.comment(0xB04D, "buf end ext lo=&FF", align=Align.INLINE)
d.comment(0xB04E, "buf end ext hi=&FF", align=Align.INLINE)
d.label(0xB04F, "lang_2_save_palette_vdu")

d.subroutine(
    0xB04F,
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


d.comment(0xB04F, "Read osword_flag (preserved across the dispatch)", align=Align.INLINE)
d.entry(0xB04F)
d.comment(0xB051, "Save state byte", align=Align.INLINE)
d.comment(0xB052, "A=&E9: workspace start lo for palette save", align=Align.INLINE)
d.comment(0xB054, "Store as nfs_workspace lo", align=Align.INLINE)
d.comment(0xB056, "Y=0", align=Align.INLINE)
d.comment(0xB058, "Reset osword_flag = 0", align=Align.INLINE)
d.comment(0xB05A, "Read vdu_screen_mode (MOS state byte)", align=Align.INLINE)
d.comment(0xB05D, "Store at (nfs_workspace)+0", align=Align.INLINE)
d.comment(0xB05F, "Advance nfs_workspace lo", align=Align.INLINE)
d.comment(0xB061, "Read vdu_display_start_hi (next MOS byte)", align=Align.INLINE)
d.comment(0xB064, "Save another byte", align=Align.INLINE)
d.comment(0xB065, "A=0 for first palette entry", align=Align.INLINE)
d.label(0xB066, "loop_read_palette")

d.comment(0xB066, "Store at (nfs_workspace)", align=Align.INLINE)
d.comment(0xB068, "Read updated nfs_workspace lo", align=Align.INLINE)
d.comment(0xB06A, "Read nfs_workspace hi", align=Align.INLINE)
d.comment(0xB06C, "A=&0B: OSWORD &0B = read palette entry", align=Align.INLINE)
d.comment(0xB06E, "Read palette entry", align=Align.INLINE)
d.comment(0xB071, "Restore inner saved", align=Align.INLINE)
d.comment(0xB072, "Y=0", align=Align.INLINE)
d.comment(0xB074, "Store palette result at workspace", align=Align.INLINE)
d.comment(0xB076, "Y=1: physical colour offset", align=Align.INLINE)
d.comment(0xB077, "Re-read palette result", align=Align.INLINE)
d.comment(0xB079, "Save for next iteration", align=Align.INLINE)
d.comment(0xB07A, "Read updated workspace lo", align=Align.INLINE)
d.comment(0xB07C, "Advance workspace", align=Align.INLINE)
d.comment(0xB07E, "Increment osword_flag (palette index)", align=Align.INLINE)
d.comment(0xB080, "Y=0", align=Align.INLINE)
d.comment(0xB081, "Read updated osword_flag", align=Align.INLINE)
d.comment(0xB083, "Compare with &F9 (last palette entry)", align=Align.INLINE)
d.comment(0xB085, "Not done: loop", align=Align.INLINE)
d.comment(0xB087, "Restore outer saved", align=Align.INLINE)
d.comment(0xB088, "Reset osword_flag = 0 after palette loop", align=Align.INLINE)
d.comment(0xB08A, "Advance workspace", align=Align.INLINE)
d.comment(0xB08C, "Serialise the next palette entry", align=Align.INLINE)
d.comment(0xB08F, "Advance workspace", align=Align.INLINE)
d.comment(0xB091, "Restore final saved", align=Align.INLINE)
d.comment(0xB092, "Save osword_flag", align=Align.INLINE)
d.label(0xB094, "commit_state_byte")

d.subroutine(
    0xB094,
    "commit_state_byte",
    title="Copy current state byte to committed state",
    description="""Reads the working state byte from workspace and
stores it to the committed state location. Used
to finalise a state transition after all related
workspace fields have been updated.""",
    on_exit={"a": "= the committed value"},
)


d.comment(0xB094, "Read saved copy of prot_status from prot_status_save", align=Align.INLINE)
d.comment(0xB097, "Store back to prot_status", align=Align.INLINE)
d.comment(0xB09A, "Return", align=Align.INLINE)
d.label(0xB09B, "serialise_palette_entry")

d.subroutine(
    0xB09B,
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


d.comment(0xB09B, "Read vdu_mode (current palette index)", align=Align.INLINE)
d.comment(0xB09F, "Mark as palette entry", align=Align.INLINE)
# UNMAPPED: d.comment(0xB06B, "Store at (nfs_workspace)+Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB06D, "Read vdu_mode", align=Align.INLINE)
d.comment(0xB0A3, "Advance workspace", align=Align.INLINE)
d.comment(0xB0A5, "A = current Y (= 0)", align=Align.INLINE)
d.comment(0xB0A6, "Store 0 at (nfs_workspace)+Y", align=Align.INLINE)
d.comment(0xB0A8, "Read lookup byte from read_osbyte_table+X", align=Align.INLINE)
d.comment(0xB0AB, "X=0: indexed-indirect mode", align=Align.INLINE)
d.comment(0xB0AD, "Advance workspace", align=Align.INLINE)
d.comment(0xB0AF, "Store at (nfs_workspace,X)", align=Align.INLINE)
d.comment(0xB0B1, "Read OSBYTE result via x=0 helper", align=Align.INLINE)
d.label(0xB0B4, "read_osbyte_to_ws_x0")

d.subroutine(
    0xB0B4,
    "read_osbyte_to_ws_x0",
    title="Read OSBYTE with X=0 and store to workspace",
    description="""Sets X=0 then falls through to read_osbyte_to_ws
to issue the OSBYTE call and store the result.
Used when the OSBYTE parameter X must be zero.""",
    on_entry={"y": "destination workspace offset"},
    on_exit={"y": "incremented past the stored byte", "a, x": "clobbered (OSBYTE)"},
)


d.comment(0xB0B4, "X=0: zero-arg helper entry", align=Align.INLINE)
d.label(0xB0B6, "read_osbyte_to_ws")

d.subroutine(
    0xB0B6,
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


d.comment(0xB0B6, "Y = osword_flag (OSBYTE-table index)", align=Align.INLINE)
d.comment(0xB0B8, "Increment osword_flag for next call", align=Align.INLINE)
d.comment(0xB0BA, "Advance nfs_workspace", align=Align.INLINE)
d.comment(0xB0BC, "Load OSBYTE number from read_osbyte_return+Y", align=Align.INLINE)
d.comment(0xB0BF, "Y=&FF -- OSBYTE arg (read mode)", align=Align.INLINE)
d.comment(0xB0C1, "Issue OSBYTE", align=Align.INLINE)
d.comment(0xB0C4, "Result to A", align=Align.INLINE)
d.comment(0xB0C5, "X=0: indexed-indirect mode", align=Align.INLINE)
d.comment(0xB0C7, "Store at (nfs_workspace,X)", align=Align.INLINE)
d.comment(0xB0C9, "Return", align=Align.INLINE)
d.index_base(0xB0CA, "read_osbyte_return")

d.index_base(0xB0CC, "read_osbyte_table")

d.comment(0xB0D3, "JMP (cdir_unused_dispatch_table,X) -- never executed; see cmd_cdir", align=Align.INLINE)
d.label(0xB0D3, "cmd_cdir_indirect_dispatch")

d.entry(0xB0D3)
d.entry(0xB0D4)


d.subroutine(
    0xB0D4,
    "cmd_cdir",
    title="*CDir command handler",
    description="""Parses an optional allocation size argument: if absent, defaults to
index 2 (standard 19-entry directory, `&200` bytes); if present,
parses the decimal value and searches a 26-entry threshold table to
find the matching allocation size index. Parses the directory name
via `parse_filename_arg`, copies it to the TX buffer, and sends FS
command code `&1B` to create the directory.

Reached via PHA/PHA/RTS dispatch from `cmd_table_fs` entry
[`*Cdir`](address:A7B0); the byte at the entry-1 address `&B0D3`
happens to decode as `JMP (cdir_unused_dispatch_table,X)` but is never executed.""",
    on_entry={"y": "command line offset in text pointer"},
)


d.comment(0xB0D4, "Save command line offset", align=Align.INLINE)
d.comment(0xB0D5, "Push onto stack", align=Align.INLINE)
d.entry(0xB0D6)
d.comment(0xB0D6, "Set owner-only access mask", align=Align.INLINE)
d.comment(0xB0D9, "Skip to optional size argument", align=Align.INLINE)
d.comment(0xB0DC, "End of line?", align=Align.INLINE)
d.comment(0xB0DE, "No: parse size argument", align=Align.INLINE)
d.comment(0xB0E0, "Default allocation size index = 2", align=Align.INLINE)
d.label(0xB0E4, "parse_cdir_size")

d.comment(0xB0E4, "A=&FF: mark as decimal parse", align=Align.INLINE)
d.comment(0xB0E6, "Store decimal parse flag", align=Align.INLINE)
d.comment(0xB0E8, "Parse numeric size argument", align=Align.INLINE)
d.comment(0xB0EB, "X=&1B: top of 26-entry size table", align=Align.INLINE)
d.label(0xB0ED, "loop_find_alloc_size")

d.comment(0xB0ED, "Try next lower index", align=Align.INLINE)
d.comment(0xB0EE, "Compare size with threshold", align=Align.INLINE)
d.comment(0xB0F1, "A < threshold: keep searching", align=Align.INLINE)
d.label(0xB0F3, "done_cdir_size")
d.comment(0xB0F3, "Store allocation size index", align=Align.INLINE)
d.comment(0xB0F6, "Restore command line offset", align=Align.INLINE)
d.comment(0xB0F7, "Transfer to Y", align=Align.INLINE)
d.comment(0xB0F8, "Save text pointer for filename parse", align=Align.INLINE)
d.comment(0xB0FB, "Parse directory name argument", align=Align.INLINE)
d.comment(0xB0FE, "X=1: one argument to copy", align=Align.INLINE)
d.comment(0xB100, "Copy directory name to TX buffer", align=Align.INLINE)
d.comment(0xB103, "Y=&1B: *CDir FS command code", align=Align.INLINE)
d.label(0xB105, "cdir_dispatch_col")

d.comment(0xB105, "Send command to file server", align=Align.INLINE)

d.label(0xB107, "cdir_size_thresholds")

for i in range(27):
    d.byte(0xB108 + i)

d.label(0xB108, "cdir_alloc_size_table")
d.banner(
    0xB108,
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
d.comment(0xB108, "Index 1: threshold 0 (catch-all)", align=Align.INLINE)
d.comment(0xB109, "Index 2: threshold 10 (default)", align=Align.INLINE)
d.comment(0xB10A, "Index 3: threshold 20", align=Align.INLINE)
d.comment(0xB10B, "Index 4: threshold 29", align=Align.INLINE)
d.comment(0xB10E, "Index 7: threshold 59", align=Align.INLINE)
d.comment(0xB10F, "Index 8: threshold 69", align=Align.INLINE)
d.comment(0xB111, "Index 10: threshold 88", align=Align.INLINE)
d.comment(0xB112, "Index 11: threshold 98", align=Align.INLINE)
d.comment(0xB113, "Index 12: threshold 108", align=Align.INLINE)
d.comment(0xB116, "Index 15: threshold 138", align=Align.INLINE)
d.comment(0xB117, "Index 16: threshold 148", align=Align.INLINE)
d.comment(0xB119, "Index 18: threshold 167", align=Align.INLINE)
d.comment(0xB11A, "Index 19: threshold 177", align=Align.INLINE)
d.comment(0xB11C, "Index 21: threshold 197", align=Align.INLINE)
d.comment(0xB11E, "Index 23: threshold 216", align=Align.INLINE)
d.comment(0xB11F, "Index 24: threshold 226", align=Align.INLINE)
d.comment(0xB120, "Index 25: threshold 236", align=Align.INLINE)
d.index_base(0xB121, "cdir_size_done")
d.comment(
    0xB121,
    "Index 26: threshold &F6 (246) -- last cdir-size threshold; doubles as cdir_size_done[0] (unread by init loop)",
    align=Align.INLINE,
)
d.comment(0xB122, "cdir_size_done[1] = &FF -> tx_retry_count (retry counter init)", align=Align.INLINE)
d.byte(0xB123)
d.comment(0xB123, "cdir_size_done[2] = &28 -> rx_wait_timeout (40 retries)", align=Align.INLINE)
d.byte(0xB124)
d.comment(0xB124, "cdir_size_done[3] = &0A -> peek_retry_count (10 retries)", align=Align.INLINE)

d.entry(0xB125)
d.label(0xB125, "cmd_lcat")

d.subroutine(
    0xB125,
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


d.comment(0xB125, "Rotate carry into lib flag bit 7", align=Align.INLINE)
d.comment(0xB128, "Set carry (= library directory)", align=Align.INLINE)
d.entry(0xB12B)
d.label(0xB12B, "cmd_lex")

d.subroutine(
    0xB12B,
    "cmd_lex",
    title="*LEx command handler",
    description="""Rotates the caller's carry into bit 7 of
[`hazel_fs_lib_flags`](label:hazel_fs_lib_flags) (the dispatch path enters
with C=1 so this sets the 'library' flag), then jumps to
`ex_set_lib_flag` inside [`cmd_ex`](label:cmd_ex) to examine
the library directory with one entry per line.""",
    on_entry={"y": "command line offset in text pointer", "c": "1 (set by the cmd_table_fs dispatch path)"},
)


d.comment(0xB12B, "Rotate carry into lib flag bit 7", align=Align.INLINE)
d.comment(0xB12E, "Set carry (= library directory)", align=Align.INLINE)
d.label(0xB131, "ps_scan_resume")

d.comment(0xB131, "Set OS text pointer and FS-options transfer ptr", align=Align.INLINE)
d.comment(0xB134, "Y=0: TX-buffer offset for the first byte", align=Align.INLINE)
d.entry(0xB136)
d.label(0xB136, "cmd_ex")

d.subroutine(
    0xB136,
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


d.comment(0xB136, "Rotate carry into lib flag bit 7", align=Align.INLINE)
d.comment(0xB139, "Clear carry (= current directory)", align=Align.INLINE)
d.label(0xB13A, "ex_set_lib_flag")

d.comment(0xB13A, "Rotate carry back, clearing bit 7", align=Align.INLINE)
d.comment(0xB13D, "A=&FF: initial column counter", align=Align.INLINE)
d.comment(0xB13F, "Store column counter", align=Align.INLINE)
d.comment(0xB141, "One entry per line (Ex format)", align=Align.INLINE)
d.comment(0xB143, "Store entries per page", align=Align.INLINE)
d.comment(0xB145, "FS command code 3: Examine", align=Align.INLINE)
d.comment(0xB147, "Store command code", align=Align.INLINE)
d.label(0xB14B, "fscv_5_cat")

d.subroutine(
    0xB14B,
    "fscv_5_cat",
    title="FSCV reason 5: catalogue (*CAT)",
    description="""Sets up transfer parameters via [`set_xfer_params`](label:set_xfer_params),
clears the library bit in `hazel_fs_lib_flags` via the
`ROR`/`CLC`/`ROL` idiom that uses carry to preserve other flags,
and falls through to `cat_set_lib_flag` to issue the FS examine
request. Reached via the FSCV vector with reason code 5.""",
)


d.entry(0xB14B)
d.comment(0xB14B, "Set transfer parameters", align=Align.INLINE)
d.comment(0xB14E, "Y=0: start from entry 0", align=Align.INLINE)
d.comment(0xB150, "Rotate carry into lib flag", align=Align.INLINE)
d.comment(0xB153, "Clear carry (= current directory)", align=Align.INLINE)
d.label(0xB154, "cat_set_lib_flag")

d.comment(0xB154, "Rotate carry back, clearing bit 7", align=Align.INLINE)
d.comment(0xB157, "Three entries per column (Cat)", align=Align.INLINE)
d.comment(0xB159, "Store column counter", align=Align.INLINE)
d.comment(0xB15B, "Store entries per page", align=Align.INLINE)
d.comment(0xB15D, "FS command code &0B: Catalogue", align=Align.INLINE)
d.comment(0xB15F, "Store command code", align=Align.INLINE)
d.label(0xB161, "setup_ex_request")

d.comment(0xB161, "Save text pointer", align=Align.INLINE)
d.comment(0xB164, "A=&FF: enable escape checking", align=Align.INLINE)
d.comment(0xB166, "Set escapable flag", align=Align.INLINE)
d.comment(0xB168, "Command code 6", align=Align.INLINE)
d.comment(0xB16A, "Store in TX buffer", align=Align.INLINE)
d.comment(0xB16D, "Parse directory argument", align=Align.INLINE)
d.comment(0xB170, "X=1: offset in buffer", align=Align.INLINE)
d.comment(0xB172, "Copy argument to TX buffer", align=Align.INLINE)
d.comment(0xB175, "Get library/FS flags", align=Align.INLINE)
d.comment(0xB178, "Shift bit 0 to carry", align=Align.INLINE)
d.comment(0xB179, "Bit 0 clear: skip", align=Align.INLINE)
d.comment(0xB17B, "Set bit 6 (owner access flag)", align=Align.INLINE)
d.label(0xB17D, "store_owner_flags")

d.comment(0xB17D, "Rotate back", align=Align.INLINE)
d.comment(0xB17E, "Store modified flags", align=Align.INLINE)
d.comment(0xB181, "Y=&12: FS command for examine", align=Align.INLINE)
d.comment(0xB183, "Send request to file server", align=Align.INLINE)
d.comment(0xB186, "X=3: offset to directory title", align=Align.INLINE)
d.comment(0xB188, "Print directory title (10 chars)", align=Align.INLINE)
d.comment(0xB18B, "Print '('", align=Align.INLINE)
d.comment(0xB18F, "Load FS object-type code from hazel_txcb_objtype (file/dir/etc)", align=Align.INLINE)
d.comment(0xB195, "Print ')     ' to close the type-code field", align=Align.INLINE)
d.comment(0xB19E, "Read hazel_txcb_type (FS reply opcode)", align=Align.INLINE)
d.comment(0xB1A1, "Non-zero (private library): take the public-label branch", align=Align.INLINE)
d.comment(0xB1A3, "Print 'Owner' + CR", align=Align.INLINE)
d.comment(0xB1AC, "Non-zero: branch to cat_after_label_print", align=Align.INLINE)
d.label(0xB1AE, "print_public_label")

d.comment(0xB1AE, "Print 'Public' + CR", align=Align.INLINE)
d.label(0xB1B8, "cat_after_label_print")

d.comment(0xB1B8, "Read hazel_fs_lib_flags", align=Align.INLINE)
d.comment(0xB1BB, "Push for stack-based saves", align=Align.INLINE)
d.comment(0xB1BC, "Mask owner access bits", align=Align.INLINE)
d.comment(0xB1BF, "Y=&15: FS command for dir info", align=Align.INLINE)
d.comment(0xB1C1, "Send request to file server", align=Align.INLINE)
d.comment(0xB1C4, "Advance X past header", align=Align.INLINE)
d.comment(0xB1C5, "Y=&10: print 16 chars", align=Align.INLINE)
d.comment(0xB1C7, "Print file entry", align=Align.INLINE)
d.comment(0xB1CA, "Print '    Option '", align=Align.INLINE)
d.comment(0xB1D8, "Read hazel_fs_flags", align=Align.INLINE)
d.comment(0xB1DB, "Transfer to X for table lookup", align=Align.INLINE)
d.comment(0xB1DC, "Print option as hex", align=Align.INLINE)
d.comment(0xB1DF, "Print ' ('", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1B1, "Look up option-string offset for index X", align=Align.INLINE)
# UNMAPPED: d.label(0xB1B4, "loop_print_dir_format")

# UNMAPPED: d.comment(0xB1B4, "Look up option byte at the resolved offset", align=Align.INLINE)
d.comment(0xB1EA, "Bit 7 of A set (negative): print directory header", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1B9, "Print char (no spool)", align=Align.INLINE)
d.comment(0xB1EF, "Advance Y", align=Align.INLINE)
d.comment(0xB1F0, "Loop until Y wraps", align=Align.INLINE)
d.label(0xB1F2, "print_dir_header")

d.comment(0xB1F2, "Print ')\\rDir. ' header for the directory listing", align=Align.INLINE)
d.comment(0xB1FC, "X=&11: filename offset in TX buffer", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1CB, "Print 10-char filename", align=Align.INLINE)
# UNMAPPED: d.comment(0xB1CE, "Print inline 'attr-bits' fragment", align=Align.INLINE)
d.comment(0xB204, "label for *Ex output", align=Align.INLINE)
d.comment(0xB20E, "X=&1B: extension offset in TX buffer", align=Align.INLINE)
d.comment(0xB210, "Print 10-char extension", align=Align.INLINE)
d.comment(0xB213, "Print newline", align=Align.INLINE)
d.comment(0xB216, "Pop saved counter", align=Align.INLINE)
d.comment(0xB217, "Store as fs_lib_flags", align=Align.INLINE)
d.label(0xB21A, "setup_ex_pagination")

d.comment(0xB21A, "Save Y as hazel_txcb_flag (next-entry index)", align=Align.INLINE)
d.comment(0xB21D, "Save Y as fs_work_4", align=Align.INLINE)
d.comment(0xB21F, "Load fs_work_5 (page count)", align=Align.INLINE)
d.comment(0xB221, "Store at hazel_txcb_count", align=Align.INLINE)
d.comment(0xB224, "Load fs_work_7", align=Align.INLINE)
d.comment(0xB226, "Store at hazel_txcb_data", align=Align.INLINE)
d.comment(0xB229, "X=3: TX[3] is start of arg buffer", align=Align.INLINE)
d.comment(0xB22B, "Copy filename arg", align=Align.INLINE)
d.comment(0xB22E, "Y=3: cmd code 3 (catalog)", align=Align.INLINE)
d.comment(0xB230, "Send TX request", align=Align.INLINE)
d.comment(0xB233, "X advances entry counter", align=Align.INLINE)
d.comment(0xB234, "Read reply status", align=Align.INLINE)
d.comment(0xB237, "Z: empty reply -> exit cat", align=Align.INLINE)
d.comment(0xB239, "Push reply status", align=Align.INLINE)
d.label(0xB23A, "loop_scan_entry_data")

d.comment(0xB23A, "Advance Y", align=Align.INLINE)
d.comment(0xB23B, "Read entry byte from hazel_txcb_data+Y", align=Align.INLINE)
d.comment(0xB23E, "Bit 7 clear: keep scanning", align=Align.INLINE)
d.comment(0xB240, "Store with high-bit clear at hazel_txcb_lib+Y", align=Align.INLINE)
d.comment(0xB243, "Print column separator", align=Align.INLINE)
d.comment(0xB246, "Pop saved status", align=Align.INLINE)
d.comment(0xB247, "Clear carry for the ADC below", align=Align.INLINE)
d.comment(0xB248, "Add fs_work_4 (page accumulator)", align=Align.INLINE)
d.comment(0xB24A, "New index", align=Align.INLINE)
d.comment(0xB24B, "Non-zero: continue paging", align=Align.INLINE)
d.label(0xB24D, "print_10_chars")

d.subroutine(
    0xB24D,
    "print_10_chars",
    title="Print 10 characters from reply buffer",
    description="""Sets Y=10 and falls through to
print_chars_from_buf. Used by cmd_ex to print
fixed-width directory title, directory name, and
library name fields.""",
    on_entry={"x": "buffer offset to start printing from"},
)


d.comment(0xB24D, "Y=10: ten characters to print (fixed-width field)", align=Align.INLINE)
d.subroutine(
    0xB24F,
    "print_chars_from_buf",
    title="Print Y characters from buffer via OSASCI",
    description="""Loops Y times, loading each byte from fs_cmd_data+X
and printing it via OSASCI. Advances X after
each character, leaving X pointing past the
last printed byte.""",
    on_entry={"x": "buffer offset", "y": "character count"},
)


d.comment(0xB24F, "Read next character from reply buffer at offset X", align=Align.INLINE)
d.comment(0xB252, "Print via OSASCI, bypassing the *SPOOL file", align=Align.INLINE)
d.comment(0xB255, "Step buffer offset", align=Align.INLINE)
d.comment(0xB256, "Step character counter", align=Align.INLINE)
d.comment(0xB257, "Loop until Y=0", align=Align.INLINE)
d.comment(0xB259, "Return; X points just past the last printed byte", align=Align.INLINE)
d.label(0xB25A, "jmp_osnewl")

d.label(0xB25D, "parse_cmd_arg_y0")

d.subroutine(
    0xB25D,
    "parse_cmd_arg_y0",
    title="Parse command argument from offset zero",
    description="""Sets Y=0 and falls through to parse_filename_arg
for GSREAD-based filename parsing with prefix
character handling.""",
    on_exit={"y": "advanced past the parsed argument"},
)


d.comment(0xB25D, "Y=0: scan from start of command line", align=Align.INLINE)
d.label(0xB25F, "parse_filename_arg")

d.subroutine(
    0xB25F,
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
    0xB25F,
    "Read the GSREAD-style filename argument into the &C030 buffer, then fall into parse_access_prefix",
    align=Align.INLINE,
)
d.label(0xB262, "parse_access_prefix")

d.subroutine(
    0xB262,
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


d.comment(0xB262, "Read first parsed-buffer character (the candidate prefix)", align=Align.INLINE)
d.comment(0xB265, "EOR with '&'; Z set iff the byte was '&'", align=Align.INLINE)
d.comment(0xB267, "Not '&': try ':' (and '#') instead", align=Align.INLINE)
d.comment(0xB269, "Read fs_lib_flags", align=Align.INLINE)
d.comment(0xB26C, "Set bit 6 (URD-relative resolution flag)", align=Align.INLINE)
d.comment(0xB26E, "Write back updated flags", align=Align.INLINE)
d.comment(0xB271, "Strip the '&' from the buffer (shift left + trim)", align=Align.INLINE)
d.comment(0xB274, "Step caller's X back to account for the consumed character", align=Align.INLINE)
d.comment(0xB275, "Re-read the (now first) buffer byte after the strip", align=Align.INLINE)
d.comment(0xB278, "EOR with '.'; Z set iff '&.' pair (URD root)", align=Align.INLINE)
d.comment(0xB27A, "Not '&.': just '&' alone -- check for trailing '#'", align=Align.INLINE)
d.comment(0xB27C, "It was '&.': peek the byte after the dot", align=Align.INLINE)
d.comment(0xB27F, "EOR with CR; Z set iff '&.<CR>' (illegal: dot needs a name to follow)", align=Align.INLINE)
d.comment(0xB281, "'&.<CR>' is invalid: raise 'Bad filename'", align=Align.INLINE)
d.comment(0xB283, "Valid '&.<name>': step X back for the dot too", align=Align.INLINE)
d.label(0xB284, "strip_token_prefix")

d.subroutine(
    0xB284,
    "strip_token_prefix",
    title="Strip first character from parsed token buffer",
    description="""Shifts all bytes in the &C030 buffer left by
one position (removing the first character),
then trims any trailing spaces by replacing
them with CR terminators. Used after consuming
a prefix character like '&' or ':'.""",
    on_exit={"x": "preserved (saved/restored via PHA/PLA)", "a": "clobbered"},
)


d.comment(0xB284, "Save caller's X (TX buffer offset)", align=Align.INLINE)
d.comment(0xB285, "Push it", align=Align.INLINE)
d.comment(0xB286, "X=&FF: INX in loop bumps to 0 for first byte", align=Align.INLINE)
d.label(0xB288, "loop_shift_str_left")

d.comment(0xB288, "Step to next byte position", align=Align.INLINE)
d.comment(0xB289, "Read byte X+1 (the next character)", align=Align.INLINE)
d.comment(0xB28C, "Store it back at byte X (shifting left by one)", align=Align.INLINE)
d.comment(0xB28F, "EOR with CR; Z set if we just shifted the terminator", align=Align.INLINE)
d.comment(0xB291, "More to shift: continue", align=Align.INLINE)
d.comment(0xB293, "X is now the buffer length (excluding CR)", align=Align.INLINE)
d.comment(0xB294, "Empty after shift: skip trim, restore X, return", align=Align.INLINE)
d.label(0xB296, "loop_trim_trailing")

d.comment(0xB296, "Read last buffer byte (X-1 because we count from 0)", align=Align.INLINE)
d.comment(0xB299, "EOR with space; Z set iff it's a trailing space", align=Align.INLINE)
d.comment(0xB29B, "Not a space: trim done, restore X, return", align=Align.INLINE)
d.comment(0xB29D, "It is a space: replace with CR (truncate the string)", align=Align.INLINE)
d.comment(0xB29F, "Store CR at the now-trimmed position", align=Align.INLINE)
d.comment(0xB2A2, "Step backwards", align=Align.INLINE)
d.comment(0xB2A3, "Loop while X > 0", align=Align.INLINE)
d.label(0xB2A5, "done_strip_prefix")

d.comment(0xB2A5, "Restore caller's TX buffer offset", align=Align.INLINE)
d.comment(0xB2A6, "Transfer back to X", align=Align.INLINE)
d.label(0xB2A7, "rts_strip_prefix")

d.comment(0xB2A7, "Return", align=Align.INLINE)
d.label(0xB2A8, "check_hash_prefix")

d.comment(0xB2A8, "Test for '#' prefix (3 ^ &23 = 0)", align=Align.INLINE)
d.comment(0xB2AA, "Equal: '#' was the prefix, return", align=Align.INLINE)
d.label(0xB2AC, "error_bad_prefix")

d.comment(0xB2AC, "Other: not a recognised prefix -> error", align=Align.INLINE)
d.label(0xB2AF, "check_colon_prefix")

d.comment(0xB2AF, "Test for ':' (&3F ^ &1C)", align=Align.INLINE)
d.comment(0xB2B1, "Different: caller had no prefix, return", align=Align.INLINE)
d.comment(0xB2B3, "':' confirmed -- read next char from parse buffer", align=Align.INLINE)
d.comment(0xB2B6, "Test for '.' (path separator)", align=Align.INLINE)
d.comment(0xB2B8, "Equal: ':.' qualified prefix", align=Align.INLINE)
d.comment(0xB2BA, "Test for '#'", align=Align.INLINE)
d.comment(0xB2BC, "Other: no recognised tail prefix, return", align=Align.INLINE)
d.label(0xB2BE, "set_fs_select_flag")

d.comment(0xB2BE, "Recognised: load fs_lib_flags", align=Align.INLINE)
d.comment(0xB2C1, "Set bit 6 (FS-select pending)", align=Align.INLINE)
d.comment(0xB2C3, "Store updated fs_lib_flags", align=Align.INLINE)
d.comment(0xB2C6, "Recurse to strip the trailing component", align=Align.INLINE)
d.comment(0xB2C9, "Decrement X (consume processed char)", align=Align.INLINE)
d.comment(0xB2CA, "Return", align=Align.INLINE)
d.index_base(0xB2CB, "option_str_offset_data")

d.comment(0xB2CB, "Data: option string offset table", align=Align.INLINE)
d.index_base(0xB2CF, "option_offset_table")

d.label(0xB2D2, "copy_arg_to_buf_x0")

d.subroutine(
    0xB2D2,
    "copy_arg_to_buf_x0",
    title="Copy argument to TX buffer from offset zero",
    description="""Sets X=0 and falls through to copy_arg_to_buf
then copy_arg_validated. Provides the simplest
entry point for copying a single parsed argument
into the TX buffer at position zero.""",
    on_exit={"x": "TX buffer offset just past the copied argument", "y": "advanced past the source argument"},
)


d.comment(
    0xB2D2, "X=0: place the argument at the start of the TX buffer; fall into copy_arg_to_buf", align=Align.INLINE
)
d.label(0xB2D4, "copy_arg_to_buf")

d.subroutine(
    0xB2D4,
    "copy_arg_to_buf",
    title="Copy argument to TX buffer with Y=0",
    description="""Sets Y=0 and falls through to copy_arg_validated
with carry set, enabling '&' character validation.
X must already contain the destination offset
within the TX buffer.""",
    on_entry={"x": "destination offset within the TX buffer"},
    on_exit={"x": "TX buffer offset just past the copied argument", "y": "advanced past the source argument"},
)


d.comment(0xB2D4, "Y=0: scan from start of command line (CLC entry skips '&' validation)", align=Align.INLINE)
d.label(0xB2D6, "copy_arg_validated")

d.subroutine(
    0xB2D6,
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

d.comment(0xB2D6, "Set C: this entry validates against '&'", align=Align.INLINE)
d.label(0xB2D7, "loop_copy_char")

d.comment(0xB2D7, "Read next source byte through fs_crc_lo pointer", align=Align.INLINE)
d.comment(0xB2D9, "Store into TX buffer at offset X", align=Align.INLINE)
d.comment(0xB2DC, "Validation off (C clear): just advance positions", align=Align.INLINE)
d.comment(0xB2DE, "Test against '!' to bias the EOR comparison", align=Align.INLINE)
d.comment(0xB2E0, "EOR with '&'; Z set iff source byte was '&'", align=Align.INLINE)
d.comment(0xB2E2, "'&' inside the argument is illegal: raise 'Bad filename'", align=Align.INLINE)
d.label(0xB2E4, "restore_after_check")

d.comment(
    0xB2E4,
    "Restore A by undoing the EOR (so the loop terminator test below sees the original byte)",
    align=Align.INLINE,
)
d.label(0xB2E6, "advance_positions")

d.comment(0xB2E6, "Advance TX buffer offset", align=Align.INLINE)
d.comment(0xB2E7, "Advance command-line offset", align=Align.INLINE)
d.comment(0xB2E8, "EOR with CR; Z set iff we just stored the terminator", align=Align.INLINE)
d.comment(0xB2EA, "More to copy: continue", align=Align.INLINE)
d.comment(0xB2EC, "Look at the byte just before the CR we stopped on", align=Align.INLINE)
d.label(0xB2EC, "loop_trim_trailing_spaces")

d.comment(0xB2EF, "EOR with space; Z set iff that byte was a trailing space", align=Align.INLINE)
d.comment(0xB2F1, "Not a space: trim done", align=Align.INLINE)
d.comment(0xB2F3, "Step back over the space", align=Align.INLINE)
d.comment(0xB2F4, "A=&0D: replace the trailing space with CR", align=Align.INLINE)
d.comment(0xB2F6, "Store CR at the now-truncated end", align=Align.INLINE)
d.comment(0xB2F9, "Always taken (A=&0D from LDA #&0D so Z is clear); look at the next byte back", align=Align.INLINE)
d.label(0xB2FB, "done_trim_spaces")


d.comment(0xB2FB, "All trailing spaces consumed (or none present)", align=Align.INLINE)
d.label(0xB2FD, "rts_copy_arg")

d.comment(0xB2FD, "Return", align=Align.INLINE)
d.subroutine(
    0xB302,
    "mask_owner_access",
    title="Clear FS selection flags from options word",
    description="""`AND`s the `&C271` (`hazel_fs_lib_flags`) byte with `&1F`, clearing the
FS selection flag (bit 6) and other high bits to retain only the
5-bit owner-access mask. Called before parsing to reset the prefix
state from a previous command. 12 callers.""",
    on_exit={"a": "masked value"},
)


d.comment(0xB302, "Read fs_lib_flags (&C271)", align=Align.INLINE)
d.comment(0xB305, "Keep only the 5-bit owner access mask", align=Align.INLINE)
d.comment(0xB307, "Store back, clearing FS-selection and other high bits", align=Align.INLINE)
d.comment(0xB30A, "Return", align=Align.INLINE)
d.comment(0xB30E, "X=0: scan from start of TX entry", align=Align.INLINE)
d.label(0xB30E, "ex_init_scan_x0")

d.entry(0xB30E)
d.label(0xB310, "loop_scan_entries")

d.comment(0xB310, "Read entry byte at hazel_txcb_data+X", align=Align.INLINE)
d.comment(0xB313, "Bit 7 set: end-of-entries -> return", align=Align.INLINE)
d.comment(0xB315, "Non-printable: take CR-newline path at col_sep_print_cr", align=Align.INLINE)
d.label(0xB317, "ex_print_col_sep")

d.subroutine(
    0xB317,
    "ex_print_col_sep",
    title="Print column separator or newline for *Ex/*Cat",
    description="""In *Cat mode, increments a column counter modulo 4
and prints a two-space separator between entries,
with a newline at the end of each row. In *Ex
mode (fs_spool_handle negative), prints a newline
after every entry. Scans the entry data and loops
back to print the next entry's characters.""",
)


d.comment(0xB317, "Read fs_spool_handle (also column counter in *Cat mode)", align=Align.INLINE)
d.comment(0xB319, "Negative: *Ex mode (one-per-line) -- skip column logic, just print newline", align=Align.INLINE)
d.comment(0xB31B, "Bump column counter", align=Align.INLINE)
d.comment(0xB31C, "Get the new value into A", align=Align.INLINE)
d.comment(0xB31D, "Wrap to 0..3 (4 columns per row)", align=Align.INLINE)
d.comment(0xB31F, "Save the new column index", align=Align.INLINE)
d.comment(0xB321, "Wrapped to 0: end of row, print newline", align=Align.INLINE)
d.comment(0xB323, "Mid-row: print 2-space column separator via inline", align=Align.INLINE)
d.comment(0xB328, "Non-zero: take col_sep_print_char tail", align=Align.INLINE)
d.comment(0xB32A, "A=&0D: CR character", align=Align.INLINE)
d.label(0xB32A, "col_sep_eol_check")

# UNMAPPED: d.comment(0xB2F9, "Print CR (no spool)", align=Align.INLINE)
# UNMAPPED: d.label(0xB2F9, "col_sep_print_cr")

d.comment(0xB32F, "Next entry", align=Align.INLINE)
d.label(0xB32F, "col_sep_print_char")

d.comment(0xB330, "Loop until X wraps", align=Align.INLINE)
d.comment(0xB336, "Y = value to convert (digits read off via successive divisions)", align=Align.INLINE)
d.subroutine(
    0xB336,
    "print_dec_3dig_no_spool",
    title="Print 3-digit decimal via *SPOOL-bypassing print",
    description="As print_decimal_3dig (&B32A) but each digit is emitted via print_char_no_spool, which closes the *SPOOL handle around OSASCI so the digit doesn't appear in any active capture. Always prints all three digits (no leading-zero suppression).",
    on_entry={"a": "value 0-255"},
)


d.comment(0xB337, "Divisor for hundreds digit", align=Align.INLINE)
d.comment(0xB339, "Print hundreds digit", align=Align.INLINE)
d.comment(0xB33C, "Divisor for tens digit", align=Align.INLINE)
d.comment(0xB33E, "Print tens digit", align=Align.INLINE)
d.comment(
    0xB341, "Divisor for units digit (always print at least the units to avoid the empty 0 case)", align=Align.INLINE
)
d.comment(0xB343, "Stash divisor in fs_error_ptr (the SBC target below)", align=Align.INLINE)
d.subroutine(
    0xB343,
    "print_dec_digit_no_spool",
    title="Print one decimal digit, *SPOOL-bypassing",
    description="As print_decimal_digit (&B36B) but emits via print_char_no_spool. fs_error_ptr is used as scratch storage for the divisor and is preserved across the print.",
    on_entry={"a": "divisor (100, 10, or 1)", "y": "value to divide"},
    on_exit={"y": "remainder after division"},
)


d.entry(0xB345)
d.comment(0xB345, "Convert remaining value to A", align=Align.INLINE)
d.comment(0xB346, "X = '0'-1: digit counter, INX in the loop steps to '0' first", align=Align.INLINE)
d.comment(0xB348, "Set carry", align=Align.INLINE)
d.comment(0xB349, "Step quotient digit", align=Align.INLINE)
d.label(0xB349, "loop_divide_decimal_digit")

d.comment(0xB34A, "Subtract divisor", align=Align.INLINE)
d.comment(0xB34C, "No underflow: keep dividing", align=Align.INLINE)
d.comment(0xB34E, "Underflow: add divisor back to recover the remainder", align=Align.INLINE)
d.comment(0xB350, "Remainder -> Y, ready for the next digit", align=Align.INLINE)
d.comment(0xB351, "Move digit ('0'-'9') from X into A for printing", align=Align.INLINE)
d.comment(
    0xB352, "Save divisor in X across the print (print_char_no_spool preserves X is not guaranteed)", align=Align.INLINE
)
d.comment(0xB354, "Print the digit, bypassing *SPOOL", align=Align.INLINE)
d.comment(0xB357, "Restore divisor from X", align=Align.INLINE)
d.comment(0xB359, "Return", align=Align.INLINE)
d.label(0xB35A, "print_num_no_leading")

d.subroutine(
    0xB35A,
    "print_num_no_leading",
    title="Print decimal number with leading zero suppression",
    description="""Sets `V=1` via `BIT always_set_v_byte` (the `&FF` constant at
&9769, whose bit 6 sets V) to enable leading-zero suppression
in [`print_decimal_3dig`](label:print_decimal_3dig), then falls through to
that routine. Used by [`print_station_id`](label:print_station_id) for
compact station number display.""",
    on_entry={"a": "number to print (0-255)"},
)


d.comment(0xB35A, "Set V (suppress leading zeros)", align=Align.INLINE)
d.label(0xB35D, "print_decimal_3dig")

d.subroutine(
    0xB35D,
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


d.comment(0xB35D, "Transfer value to Y (remainder)", align=Align.INLINE)
d.comment(0xB35E, "A=100: hundreds divisor", align=Align.INLINE)
d.comment(0xB360, "Print hundreds digit", align=Align.INLINE)
d.comment(0xB363, "A=10: tens divisor", align=Align.INLINE)
d.comment(0xB365, "Print tens digit", align=Align.INLINE)
d.comment(0xB368, "Clear V (always print units)", align=Align.INLINE)
d.comment(0xB369, "A=1: units divisor", align=Align.INLINE)
d.label(0xB36B, "print_decimal_digit")

d.subroutine(
    0xB36B,
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


d.comment(0xB36B, "Store divisor", align=Align.INLINE)
d.comment(0xB36D, "Get remaining value", align=Align.INLINE)
d.comment(0xB36E, "X='0'-1: digit counter", align=Align.INLINE)
d.comment(0xB370, "Set carry for subtraction", align=Align.INLINE)
d.comment(0xB371, "Save V flag for leading zero check", align=Align.INLINE)
d.label(0xB372, "loop_divide_digit")

d.comment(0xB372, "Count quotient digit", align=Align.INLINE)
d.comment(0xB373, "Subtract divisor", align=Align.INLINE)
d.comment(0xB375, "No underflow: continue dividing", align=Align.INLINE)
d.comment(0xB377, "Add back divisor (get remainder)", align=Align.INLINE)
d.comment(0xB379, "Remainder to Y for next digit", align=Align.INLINE)
d.comment(0xB37A, "Digit character to A", align=Align.INLINE)
d.comment(0xB37B, "Restore V flag", align=Align.INLINE)
d.comment(0xB37C, "V clear: always print digit", align=Align.INLINE)
d.comment(0xB37E, "V set: is digit '0'?", align=Align.INLINE)
d.comment(0xB380, "Yes: suppress leading zero", align=Align.INLINE)
d.label(0xB382, "print_nonzero_digit")

d.comment(0xB382, "Save divisor across OSASCI call", align=Align.INLINE)
d.comment(0xB387, "Restore divisor", align=Align.INLINE)
d.label(0xB389, "rts_print_digit")

d.comment(0xB389, "Return", align=Align.INLINE)
d.subroutine(
    0xB38A,
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


d.comment(0xB38A, "Clear owner-only access bits before checking the URD", align=Align.INLINE)
d.label(0xB38A, "cmd_info_dispatch")

d.entry(0xB38A)
d.comment(0xB38D, "A=&69: 'i' character (info prefix)", align=Align.INLINE)
d.comment(0xB38F, "Store 'i' as start of FS command name in the TX buffer", align=Align.INLINE)
d.comment(0xB392, "A='.': abbreviation terminator", align=Align.INLINE)
d.comment(0xB394, "Store '.' as command-name terminator", align=Align.INLINE)
d.comment(0xB397, "Save the command-line pointer for the dispatcher", align=Align.INLINE)
d.comment(0xB39A, "Parse the *Info argument from the command line", align=Align.INLINE)
d.comment(0xB39D, "X=2: TX-buffer offset to copy the arg into (after 'i.')", align=Align.INLINE)
d.comment(0xB39F, "Append parsed argument to the TX command buffer", align=Align.INLINE)
d.comment(0xB3A2, "A = next index", align=Align.INLINE)
d.comment(0xB3A3, "Send the FS command and dispatch the reply", align=Align.INLINE)
d.label(0xB3A6, "save_ptr_to_os_text")

d.subroutine(
    0xB3A6,
    "save_ptr_to_os_text",
    title="Copy text pointer to OS text pointer workspace",
    description="""Saves fs_crc_lo/hi into the MOS text pointer
locations at &00F2/&00F3. Preserves A on the
stack. Called before GSINIT/GSREAD sequences
that need to parse from the current command
line position.""",
    on_exit={"a": "preserved (PHA/PLA)"},
)


d.comment(0xB3A6, "Save A", align=Align.INLINE)
d.comment(0xB3A7, "Copy text pointer low byte", align=Align.INLINE)
d.comment(0xB3A9, "To OS text pointer low", align=Align.INLINE)
d.comment(0xB3AB, "Copy text pointer high byte", align=Align.INLINE)
d.comment(0xB3AD, "To OS text pointer high", align=Align.INLINE)
d.comment(0xB3AF, "Restore A", align=Align.INLINE)
d.comment(0xB3B0, "Return", align=Align.INLINE)
d.label(0xB3B1, "loop_advance_char")

d.comment(0xB3B1, "Advance past current character", align=Align.INLINE)
d.label(0xB3B2, "skip_to_next_arg")

d.subroutine(
    0xB3B2,
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


d.comment(0xB3B2, "Load char from command line", align=Align.INLINE)
d.comment(0xB3B4, "Space?", align=Align.INLINE)
d.comment(0xB3B6, "Yes: skip trailing spaces", align=Align.INLINE)
d.comment(0xB3B8, "CR (end of line)?", align=Align.INLINE)
d.comment(0xB3BA, "Yes: return (at end)", align=Align.INLINE)
d.label(0xB3BE, "loop_skip_space_chars")

d.comment(0xB3BE, "Advance past space", align=Align.INLINE)
d.comment(0xB3BF, "Load next character", align=Align.INLINE)
d.comment(0xB3C1, "Still a space?", align=Align.INLINE)
d.comment(0xB3C3, "Yes: skip multiple spaces", align=Align.INLINE)
d.label(0xB3C5, "rts_skip_arg")

d.comment(0xB3C5, "Return (at next argument)", align=Align.INLINE)
d.label(0xB3C6, "save_ptr_to_spool_buf")

d.subroutine(
    0xB3C6,
    "save_ptr_to_spool_buf",
    title="Copy text pointer to spool buffer pointer",
    description="""Saves fs_crc_lo/hi into fs_options/fs_block_offset
for use as the spool buffer pointer. Preserves A
on the stack. Called by *PS and *PollPS before
parsing their arguments.""",
    on_exit={"a": "preserved (PHA/PLA)"},
)


d.comment(0xB3C6, "Save A", align=Align.INLINE)
d.comment(0xB3C7, "Copy text pointer low byte", align=Align.INLINE)
d.comment(0xB3C9, "To spool buffer pointer low", align=Align.INLINE)
d.comment(0xB3CB, "Copy text pointer high byte", align=Align.INLINE)
d.comment(0xB3CD, "To spool buffer pointer high", align=Align.INLINE)
d.comment(0xB3CF, "Restore A", align=Align.INLINE)
d.comment(0xB3D0, "Return", align=Align.INLINE)
d.label(0xB3D1, "init_spool_drive")

d.subroutine(
    0xB3D1,
    "init_spool_drive",
    title="Initialise spool drive page pointers",
    description="""Calls get_ws_page to read the workspace page
number for the current ROM slot, stores it as
the spool drive page high byte (addr_work), and
clears the low byte (work_ae) to zero. Preserves
Y on the stack.""",
    on_exit={"a": "0", "y": "preserved (PHY/PLY)"},
)


d.comment(0xB3D1, "Save Y", align=Align.INLINE)
d.comment(0xB3D2, "Push it", align=Align.INLINE)
d.comment(0xB3D3, "Get workspace page number", align=Align.INLINE)
d.comment(0xB3D6, "Store as spool drive page high", align=Align.INLINE)
d.comment(0xB3D8, "Restore Y", align=Align.INLINE)
d.comment(0xB3D9, "Transfer to Y", align=Align.INLINE)
d.comment(0xB3DA, "A=0", align=Align.INLINE)
d.comment(0xB3DC, "Clear spool drive page low", align=Align.INLINE)
d.comment(0xB3DE, "Return", align=Align.INLINE)
d.entry(0xB3DF)
d.label(0xB3DF, "cmd_ps")

d.subroutine(
    0xB3DF,
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


d.comment(0xB3DF, "A=1: check printer ready", align=Align.INLINE)
d.comment(0xB3E1, "Test printer server workspace flag", align=Align.INLINE)
d.comment(0xB3E4, "Non-zero: printer available", align=Align.INLINE)
d.comment(0xB3E6, "Printer not available: error", align=Align.INLINE)
d.label(0xB3E9, "done_ps_available")

d.comment(0xB3E9, "Initialise spool drive", align=Align.INLINE)
d.comment(0xB3EC, "Save pointer to spool buffer", align=Align.INLINE)
d.comment(0xB3F7, "Read fs_options[Y]", align=Align.INLINE)
d.comment(0xB3F9, "End of command line?", align=Align.INLINE)
d.comment(0xB3FB, "Yes: no argument given", align=Align.INLINE)
d.comment(0xB3FD, "Clear V (= explicit PS name given)", align=Align.INLINE)
d.comment(0xB3FE, "Is first char a decimal digit?", align=Align.INLINE)
d.comment(0xB401, "C clear: save ptr and continue", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3C8, "A = current Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3C9, "Save Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3CA, "Load PS server address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3CD, "Restore Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB3CE, "Back to Y register", align=Align.INLINE)
d.comment(0xB408, "Parse FS/PS arguments", align=Align.INLINE)
d.comment(0xB40B, "Jump to store station address", align=Align.INLINE)
d.label(0xB40E, "copy_ps_data_y1c")

d.subroutine(
    0xB40E,
    "copy_ps_data_y1c",
    title="Copy printer server template at offset &18",
    description="""Sets Y=&18 and falls through to copy_ps_data.
Called during workspace initialisation
(svc_2_private_workspace) to set up the printer
server template at the standard offset.""",
    on_exit={"y": "&20 (advanced past the copied 8 bytes)"},
)


d.comment(0xB40E, "Y=&18: standard offset for the PS template; fall into copy_ps_data", align=Align.INLINE)
d.label(0xB410, "copy_ps_data")

d.subroutine(
    0xB410,
    "copy_ps_data",
    title="Copy 8-byte printer server template to RX buffer",
    description="""Copies 8 bytes of default printer server data into the RX buffer
at the current `Y` offset. Uses indexed addressing: `LDA
ps_template_base,X` with `X` starting at `&F8`, so the effective
read address is `ps_template_base+&F8 = ps_template_data`
(`&8EB7`). The 6502 trick reaches data 248
bytes past the base label in a single instruction; the base
address (`ps_template_base`) deliberately falls inside the operand
byte of a JSR instruction at `&8DA6` -- see
docs/analysis/authors-easter-egg.md.""",
    on_entry={"y": "destination offset within the RX buffer"},
    on_exit={"y": "advanced by 8", "x": "0 (loop terminator)", "a": "last template byte"},
)

d.comment(
    0xB410,
    "X=&F8: walks 0..7 via wraparound (loads from ps_template_base+&F8 = ps_template_data &8EB7)",
    align=Align.INLINE,
)
d.label(0xB412, "loop_copy_ps_tmpl")

d.comment(0xB412, "Read template byte from ps_template_data + (X-&F8)", align=Align.INLINE)
d.comment(0xB415, "Store into RX buffer at offset Y", align=Align.INLINE)
d.comment(0xB417, "Step destination", align=Align.INLINE)
d.comment(0xB418, "Step source -- wraps from &FF to &00 to terminate", align=Align.INLINE)
d.comment(0xB419, "Loop while X != 0 (8 iterations: &F8..&FF)", align=Align.INLINE)
d.comment(0xB41B, "Return", align=Align.INLINE)
d.label(0xB41C, "no_ps_name_given")

d.comment(0xB41C, "Set V (= no explicit PS name)", align=Align.INLINE)
d.label(0xB41F, "save_ps_cmd_ptr")

d.comment(0xB41F, "Save Y at ws_ptr_hi", align=Align.INLINE)
d.comment(0xB421, "V set: skip PS name parsing", align=Align.INLINE)
d.comment(0xB423, "Max 6 characters for PS name", align=Align.INLINE)
d.comment(0xB425, "Buffer offset &1C for PS name", align=Align.INLINE)
d.comment(0xB427, "Space character", align=Align.INLINE)
d.label(0xB429, "loop_pad_ps_name")

d.comment(0xB429, "Fill buffer with space", align=Align.INLINE)
d.comment(0xB42B, "Advance Y past padding", align=Align.INLINE)
d.comment(0xB42C, "Count down", align=Align.INLINE)
d.comment(0xB42D, "Loop while Y wraps", align=Align.INLINE)
d.comment(0xB42F, "Save text pointer", align=Align.INLINE)
d.comment(0xB432, "Restore Y from ws_ptr_hi", align=Align.INLINE)
d.comment(0xB434, "Initialise string reading", align=Align.INLINE)
d.comment(0xB437, "Empty string: skip to send", align=Align.INLINE)
d.comment(0xB439, "X=6: scan up to 6 PS slots", align=Align.INLINE)
d.comment(0xB43B, "Save updated string pointer", align=Align.INLINE)
d.comment(0xB43D, "Buffer offset for PS name", align=Align.INLINE)
d.comment(0xB43F, "Save buffer position", align=Align.INLINE)
d.label(0xB441, "loop_read_ps_char")

d.comment(0xB441, "Restore string pointer", align=Align.INLINE)
d.comment(0xB443, "Read next character", align=Align.INLINE)
d.comment(0xB446, "Save updated pointer", align=Align.INLINE)
d.comment(0xB448, "C set: end of slots", align=Align.INLINE)
d.comment(0xB44A, "Store char uppercased in buffer", align=Align.INLINE)
d.comment(0xB44D, "Loop for more characters", align=Align.INLINE)
d.label(0xB44F, "done_ps_name_parse")

d.comment(0xB44F, "Copy reversed PS name to TX", align=Align.INLINE)
d.comment(0xB452, "Send PS status request", align=Align.INLINE)
d.comment(0xB455, "Pop and requeue PS scan", align=Align.INLINE)
d.comment(0xB458, "Load PS server address", align=Align.INLINE)
d.comment(0xB45B, "A=0", align=Align.INLINE)
d.comment(0xB45E, "Offset &24 in buffer", align=Align.INLINE)
d.comment(0xB460, "Clear PS status byte", align=Align.INLINE)
d.label(0xB462, "loop_pop_ps_slot")

d.comment(0xB462, "Pop saved slot index", align=Align.INLINE)
d.comment(0xB463, "Zero: all slots done", align=Align.INLINE)
d.comment(0xB465, "Push it back (for retry)", align=Align.INLINE)
d.comment(0xB466, "Transfer to Y", align=Align.INLINE)
d.comment(0xB467, "Read slot status", align=Align.INLINE)
d.comment(0xB469, "Bit 7 clear: slot inactive", align=Align.INLINE)
d.comment(0xB46B, "Advance Y by 4 (next slot)", align=Align.INLINE)
d.comment(0xB46E, "Read ws byte at (nfs_workspace)+Y", align=Align.INLINE)
d.comment(0xB470, "Save as work_ae lo", align=Align.INLINE)
d.comment(0xB472, "Read indirect via (work_ae,X)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB43B, "Z set: zero -> read station addr", align=Align.INLINE)
# UNMAPPED: d.comment(0xB43D, "Compare with 3", align=Align.INLINE)
d.comment(0xB476, "Other than 3: skip slot mark", align=Align.INLINE)
d.label(0xB478, "read_ps_station_addr")


d.comment(0xB478, "Back up to network byte", align=Align.INLINE)
d.comment(0xB479, "Read network byte", align=Align.INLINE)
d.comment(0xB47B, "Save as fs_work_6", align=Align.INLINE)
d.comment(0xB47D, "Back up to station byte", align=Align.INLINE)
d.comment(0xB47E, "Read station byte", align=Align.INLINE)
d.comment(0xB480, "Save as fs_work_5", align=Align.INLINE)
d.comment(0xB482, "Y=&20: PS marker offset", align=Align.INLINE)
d.comment(0xB484, "Store station to (net_rx_ptr)+&20", align=Align.INLINE)
d.label(0xB486, "done_ps_slot_mark")

d.comment(0xB486, "Pop saved slot index", align=Align.INLINE)
d.comment(0xB487, "Transfer to Y", align=Align.INLINE)
d.comment(0xB488, "A=&3F: 'processed' marker", align=Align.INLINE)
d.comment(0xB48A, "Mark slot as processed", align=Align.INLINE)
d.label(0xB48E, "done_ps_scan")

d.comment(0xB48E, "Print 'Printer server is ' fragment", align=Align.INLINE)
d.comment(0xB491, "Y=&20: marker offset", align=Align.INLINE)
d.comment(0xB493, "Read marker byte", align=Align.INLINE)
d.comment(0xB495, "Non-zero: print 'now <stn>'", align=Align.INLINE)
d.comment(0xB497, "Print 'still ' fragment", align=Align.INLINE)
d.comment(0xB4A0, "Bit-7 terminator (next opcode)", align=Align.INLINE)
d.label(0xB4A3, "print_ps_now")

d.comment(0xB4A3, "Print 'now ' fragment", align=Align.INLINE)
# UNMAPPED: d.comment(0xB473, "Bit-7 terminator", align=Align.INLINE)
# UNMAPPED: d.comment(0xB474, "Print station number and newline", align=Align.INLINE)
# UNMAPPED: d.label(0xB474, "print_ps_padding")

d.label(0xB4B2, "store_ps_station")

d.subroutine(
    0xB4B2,
    "store_ps_station",
    title="Write printer-server station number into NFS workspace",
    description="""Stores fs_work_5/fs_work_6 (the parsed station/network bytes) into
nfs_workspace offsets 2 and 3 (the printer-server slot's station/
net pair). Single caller (cmd_ps's parse-success path at &B3D2).""",
)


d.comment(0xB4B2, "Y=2: workspace offset for stored station", align=Align.INLINE)
d.comment(0xB4B4, "Load station number", align=Align.INLINE)
d.comment(0xB4B6, "Store at (nfs_workspace)+2", align=Align.INLINE)
d.comment(0xB4B9, "Load network number", align=Align.INLINE)
d.comment(0xB4BB, "Store at (nfs_workspace)+3", align=Align.INLINE)
d.comment(0xB4BD, "Return", align=Align.INLINE)
d.label(0xB4BE, "print_file_server_is")

d.subroutine(
    0xB4BE,
    "print_file_server_is",
    title="Print 'File server ' prefix",
    description="""Uses print_inline to output 'File' then falls through
to the shared ' server is ' suffix at
print_printer_server_is.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered (OSASCI via print_inline)"},
)


d.comment(0xB4BE, "Print 'File' via inline string", align=Align.INLINE)
d.comment(0xB4C5, "Clear V so the BVC below is taken", align=Align.INLINE)
d.comment(
    0xB4C6,
    "Always taken (V was just cleared); skip the 'Printer' prologue and reach the shared ' server is ' suffix",
    align=Align.INLINE,
)
d.label(0xB4C8, "print_printer_server_is")

d.subroutine(
    0xB4C8,
    "print_printer_server_is",
    title="Print 'Printer server is ' prefix",
    description="""Uses print_inline to output the full label
'Printer server is ' with trailing space.""",
    on_entry={},
    on_exit={"a, x, y": "clobbered (OSASCI via print_inline)"},
)


d.comment(0xB4C8, "Print 'Printer' via inline string", align=Align.INLINE)
d.comment(0xB4D2, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.label(0xB4D3, "print_server_is_suffix")

d.comment(0xB4D3, "Print ' server is ' via inline string", align=Align.INLINE)
d.comment(0xB4D6, "fragment for 'File/Printer server is ...' messages", align=Align.INLINE)
d.comment(0xB4E1, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0xB4E2, "Return; caller now prints the actual server (file or printer) address", align=Align.INLINE)
d.label(0xB4E3, "load_ps_server_addr")

d.subroutine(
    0xB4E3,
    "load_ps_server_addr",
    title="Load printer server address from workspace",
    description="""Reads the station and network bytes from workspace
offsets 2 and 3 into the station/network variables.""",
    on_exit={"a, y": "clobbered"},
)


d.comment(0xB4E3, "Y=2: workspace offset of PS station byte", align=Align.INLINE)
d.comment(0xB4E5, "Read station byte", align=Align.INLINE)
d.comment(0xB4E7, "Stash in fs_work_5 (PS station)", align=Align.INLINE)
d.comment(0xB4E9, "Y=3: workspace offset of PS network byte", align=Align.INLINE)
d.comment(0xB4EA, "Read network byte", align=Align.INLINE)
d.comment(0xB4EC, "Stash in fs_work_6 (PS network)", align=Align.INLINE)
d.comment(0xB4EE, "Return", align=Align.INLINE)
d.label(0xB4EF, "pop_requeue_ps_scan")

d.subroutine(
    0xB4EF,
    "pop_requeue_ps_scan",
    title="Pop return address and requeue PS slot scan",
    description="""Converts the PS slot flags to a workspace index,
writes slot data, and jumps back into the PS scan
loop to continue processing.""",
    on_entry={"a": "PS slot flags byte to convert into a workspace index"},
)


d.comment(0xB4EF, "Pull saved upper byte of ws_ptr_lo+osword_flag pair", align=Align.INLINE)
d.comment(0xB4F0, "Save into osword_flag", align=Align.INLINE)
d.comment(0xB4F2, "Pull lower byte", align=Align.INLINE)
d.comment(0xB4F3, "Save into ws_ptr_lo", align=Align.INLINE)
d.comment(0xB4F5, "Push 0 -- placeholder, will be the stacked return marker", align=Align.INLINE)
d.comment(0xB4F7, "Push it", align=Align.INLINE)
d.comment(0xB4F8, "ws_ptr_hi base = &84 (start of PS slot table area)", align=Align.INLINE)
d.comment(0xB4FA, "Save base", align=Align.INLINE)
d.comment(0xB4FC, "Shift bit 0 of econet_flags into C (saved scan state)", align=Align.INLINE)
d.comment(0xB4FF, "A=3: PS slot index counter", align=Align.INLINE)
d.label(0xB501, "loop_scan_ps_slots")

d.comment(0xB501, "Convert slot index to 12-byte-aligned table offset", align=Align.INLINE)
d.comment(0xB504, "Out of range (clamped to 0): all slots scanned", align=Align.INLINE)
d.comment(0xB506, "A /= 2 (shift down)", align=Align.INLINE)
d.comment(0xB507, "A /= 2 again (now slot index * 4 / 4 = slot index)", align=Align.INLINE)
d.comment(0xB508, "X = slot index", align=Align.INLINE)
d.comment(0xB509, "Read slot's status byte at workspace[Y]", align=Align.INLINE)
d.comment(0xB50B, "Slot empty (0): scan done", align=Align.INLINE)
d.comment(0xB50D, "Slot is '?' (uninitialised marker)?", align=Align.INLINE)
d.comment(0xB50F, "Yes: re-init this slot's data", align=Align.INLINE)
d.label(0xB511, "skip_next_ps_slot")

d.subroutine(
    0xB511,
    "skip_next_ps_slot",
    title="Advance to next PS slot, wrap if all 256 done",
    description="""INX / TXA / BNE loop_scan_ps_slots. Slot index in X advances; the
BNE re-enters the scan unless X has wrapped to zero (all 256
slots scanned). Single caller (the no-match path at &B4FF in the
PS slot scanner).""",
    on_entry={"x": "current slot index"},
)


d.comment(0xB511, "Step slot index", align=Align.INLINE)
d.comment(0xB512, "Move to A for next iteration", align=Align.INLINE)
d.comment(0xB513, "Loop while X != 0 (wraps when all slots done)", align=Align.INLINE)
d.label(0xB515, "reinit_ps_slot")

d.comment(0xB515, "Save Y (slot table offset)", align=Align.INLINE)
d.comment(0xB516, "Push it", align=Align.INLINE)
d.comment(0xB517, "A=&7F: slot status 'busy/active'", align=Align.INLINE)
d.comment(0xB519, "Mark slot active", align=Align.INLINE)
d.comment(0xB51B, "Step Y to control byte", align=Align.INLINE)
d.comment(0xB51C, "A=&9E: control byte (PS-init pattern)", align=Align.INLINE)
d.comment(0xB51E, "Store control byte", align=Align.INLINE)
d.comment(0xB520, "A=0: zero-fill the next two bytes", align=Align.INLINE)
d.comment(0xB522, "Write two zeros, advance Y", align=Align.INLINE)
d.comment(0xB525, "Read current ws_ptr_hi", align=Align.INLINE)
d.comment(0xB527, "Store as buffer-link low byte", align=Align.INLINE)
d.comment(0xB529, "Clear C ready for the +3", align=Align.INLINE)
d.comment(0xB52A, "Save flags so the ADC's C doesn't leak", align=Align.INLINE)
d.comment(0xB52B, "Bump ws_ptr_hi by 3 (next slot's base)", align=Align.INLINE)
d.comment(0xB52D, "Restore flags", align=Align.INLINE)
d.comment(0xB52E, "Save updated ws_ptr_hi", align=Align.INLINE)
d.comment(0xB530, "Write buffer page + two &FF sentinels", align=Align.INLINE)
d.comment(0xB533, "Read ws_ptr_hi (now updated)", align=Align.INLINE)
d.comment(0xB535, "Store as second-link byte", align=Align.INLINE)
d.label(0xB537, "write_ps_slot_hi_link")

d.comment(0xB537, "Write another buffer page + two &FF sentinels", align=Align.INLINE)
# UNMAPPED: d.label(0xB4FD, "ps_print_template")

d.comment(0xB53A, "Continue scanning slots", align=Align.INLINE)
d.label(0xB53D, "done_ps_slot_scan")

d.comment(0xB53D, "Restore bit 0 of econet_flags via ASL (recovers from the LSR at &B4C1)", align=Align.INLINE)
d.comment(0xB540, "Pull saved ws_ptr_lo", align=Align.INLINE)
d.comment(0xB542, "Push it back (the caller's return-resume sequence)", align=Align.INLINE)
d.comment(0xB543, "Pull saved osword_flag", align=Align.INLINE)
d.comment(0xB545, "Push it back", align=Align.INLINE)
d.comment(0xB546, "A=&0A: outer counter", align=Align.INLINE)
d.comment(0xB548, "Y=&0A: inner counter", align=Align.INLINE)
d.comment(0xB549, "X=&0A: middle counter", align=Align.INLINE)
d.comment(0xB54A, "Save outer in fs_work_4", align=Align.INLINE)
d.label(0xB54C, "loop_ps_delay")

d.comment(0xB54C, "Decrement inner counter", align=Align.INLINE)
d.comment(0xB54D, "Inner not zero: keep delaying", align=Align.INLINE)
d.comment(0xB54F, "Decrement middle", align=Align.INLINE)
d.comment(0xB550, "Middle not zero: refresh inner and continue", align=Align.INLINE)
d.comment(0xB552, "Decrement outer in fs_work_4", align=Align.INLINE)
d.comment(0xB554, "Outer not zero: another full sweep (~1000 cycles)", align=Align.INLINE)
d.comment(0xB556, "Return", align=Align.INLINE)
d.label(0xB557, "write_ps_slot_byte_ff")

d.subroutine(
    0xB557,
    "write_ps_slot_byte_ff",
    title="Write buffer page byte and two &FF markers",
    description="""Stores the buffer page byte at the current Y offset
in workspace, followed by two &FF sentinel bytes.
Advances Y after each write.""",
    on_entry={"a": "buffer page byte to store at workspace+Y", "y": "starting workspace offset"},
    on_exit={"a": "&FF (the sentinel value left in A)", "y": "workspace offset advanced by 3 (one byte + two markers)"},
)


d.comment(0xB557, "Step Y to next workspace slot byte", align=Align.INLINE)
d.comment(0xB558, "Load buffer page byte from addr_work", align=Align.INLINE)
d.comment(0xB55A, "Write at offset Y", align=Align.INLINE)
d.comment(0xB55C, "A=&FF: sentinel; fall into write_two_bytes_inc_y to store two of them", align=Align.INLINE)
d.label(0xB55E, "write_two_bytes_inc_y")

d.subroutine(
    0xB55E,
    "write_two_bytes_inc_y",
    title="Write A to two consecutive workspace bytes",
    description="""Stores A at the current Y offset via (nfs_workspace),Y
then again at Y+1, advancing Y after each write.""",
    on_entry={"a": "byte to store", "y": "workspace offset"},
)


d.comment(0xB55E, "Step Y to next destination", align=Align.INLINE)
d.comment(0xB55F, "Write A at workspace offset Y", align=Align.INLINE)
d.comment(0xB561, "Step Y again", align=Align.INLINE)
d.comment(0xB562, "Write A at the next offset (two consecutive copies)", align=Align.INLINE)
d.comment(0xB564, "Final INY leaves Y pointing past the second write", align=Align.INLINE)
d.comment(0xB565, "Return", align=Align.INLINE)
d.label(0xB566, "reverse_ps_name_to_tx")

d.subroutine(
    0xB566,
    "reverse_ps_name_to_tx",
    title="Reverse-copy printer server name to TX buffer",
    description="""Copies 8 bytes from the RX buffer at offsets `&18..&1F`
(`(net_rx_ptr)+&18..+&1F`) to the TX buffer at offsets
`&10..&17` (`(net_rx_ptr)+&10..+&17`) in reversed byte order.
Implementation: pushes the 8 RX bytes onto the stack, then pops
them back to the TX area; the LIFO order achieves the reversal.""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xB566, "Y=&18: source offset (start of PS name in RX buffer)", align=Align.INLINE)
d.label(0xB568, "loop_push_ps_name")

d.comment(0xB568, "Read RX byte at offset Y", align=Align.INLINE)
d.comment(0xB56A, "Push it (the stack reverses the order)", align=Align.INLINE)
d.comment(0xB56B, "Step source", align=Align.INLINE)
d.comment(0xB56C, "Reached &20 (one past the 8-byte name)?", align=Align.INLINE)
d.comment(0xB56E, "No: continue pushing", align=Align.INLINE)
d.comment(0xB570, "Y=&17: destination offset for the reversed name", align=Align.INLINE)
d.label(0xB572, "loop_pop_ps_name")

d.comment(0xB572, "Pull next pushed byte (LIFO -> reversed order)", align=Align.INLINE)
d.comment(0xB573, "Store at destination offset Y", align=Align.INLINE)
d.comment(0xB575, "Step destination back", align=Align.INLINE)
d.comment(0xB576, "Reached &0F (one before the destination range)?", align=Align.INLINE)
d.comment(0xB578, "No: continue popping", align=Align.INLINE)
d.comment(
    0xB57A, "Copy net_rx_ptr_hi as the TX page (TX shares the same page as RX for this packet)", align=Align.INLINE
)
d.comment(0xB57C, "Set net_tx_ptr_hi", align=Align.INLINE)
d.comment(0xB57E, "TX low byte = &0C: skip past the TX header to where the reversed name lives", align=Align.INLINE)
d.comment(0xB580, "Set net_tx_ptr lo", align=Align.INLINE)
d.comment(0xB582, "Y=3: copy 4-byte TX header (offsets 3..0)", align=Align.INLINE)
d.label(0xB584, "loop_copy_tx_hdr")

d.comment(0xB584, "Read template byte", align=Align.INLINE)
d.comment(0xB587, "Write to TX buffer at offset Y", align=Align.INLINE)
d.comment(0xB589, "Step backwards", align=Align.INLINE)
d.comment(0xB58A, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xB58C, "Return", align=Align.INLINE)
d.index_base(0xB58D, "ps_tx_header_template")
d.banner(
    0xB58D,
    title="Printer-server TX header template (4 bytes)",
    description="""Four bytes copied to the head of the printer-server transmit
buffer by [`reverse_ps_name_to_tx`](label:reverse_ps_name_to_tx): control byte
`&80` (immediate-TX request), port `&D1` (printer block port),
function-code stub, and reply-port byte. Filled-in destination
fields follow from the caller's PS slot.""",
)
for i in range(4):
    d.byte(0xB58D + i)

d.comment(0xB58D, "Control byte &80 (immediate TX)", align=Align.INLINE)
d.comment(0xB58E, "Port &9F (printer server)", align=Align.INLINE)
d.comment(0xB58F, "Station &FF (any)", align=Align.INLINE)
d.comment(0xB590, "Network &FF (any)", align=Align.INLINE)
d.label(0xB591, "print_station_addr")

d.subroutine(
    0xB591,
    "print_station_addr",
    title="Print station address as decimal net.station",
    description="""If the network number is zero, prints only the
station number. Otherwise prints network.station
separated by a dot. V flag controls padding with
leading spaces for column alignment.""",
    on_entry={"v flag": "set = no leading-space padding; clear = pad to align in a column"},
    on_exit={"a, x, y": "clobbered (print_decimal_3dig and OSASCI)"},
)


d.comment(0xB591, "Save caller's V (controls leading-zero padding via the BVS at &B566)", align=Align.INLINE)
d.comment(0xB592, "Read network number (fs_work_6)", align=Align.INLINE)
d.comment(0xB594, "Network 0 means local: skip the 'NN.' prefix", align=Align.INLINE)
d.comment(0xB596, "Network non-zero: print as 3-digit decimal", align=Align.INLINE)
d.comment(0xB599, "A='.': separator between network and station", align=Align.INLINE)
d.comment(0xB59B, "Print the dot", align=Align.INLINE)
d.comment(
    0xB59E,
    "Set V so the next BVS branches over the padding (we just printed digits, no padding needed)",
    align=Align.INLINE,
)
d.label(0xB5A1, "skip_if_local_net")

d.comment(0xB5A1, "V set: skip leading-space padding", align=Align.INLINE)
d.comment(0xB5A3, "V clear (caller wanted padding): print 4 leading spaces via inline string", align=Align.INLINE)
d.comment(0xB5AA, "Read station number (fs_work_5)", align=Align.INLINE)
d.label(0xB5AA, "local_net_prefix")

d.comment(
    0xB5AC, "Restore caller's V (so print_decimal_3dig honours its own leading-zero suppression)", align=Align.INLINE
)
d.comment(0xB5AD, "Tail-call print_decimal_3dig for the station number", align=Align.INLINE)
d.label(0xB5B0, "ps_slot_txcb_template")
d.banner(
    0xB5B0,
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
    d.byte(0xB5B0 + i)

d.comment(0xB5B0, "Offset 0: txcb_ctrl = &80 (standard)", align=Align.INLINE)
d.comment(0xB5B1, "Offset 1: txcb_port = &9F (PS port)", align=Align.INLINE)
d.comment(0xB5B2, "Offset 2: dest station (placeholder, &00)", align=Align.INLINE)
d.comment(0xB5B3, "Offset 3: dest network (placeholder, &00)", align=Align.INLINE)
d.comment(0xB5B4, "Offset 4: buf1 start lo = &10", align=Align.INLINE)
d.comment(0xB5B5, "Offset 5: buf1 start hi (page from net_rx_ptr)", align=Align.INLINE)
d.comment(0xB5B6, "Offset 6: buf1 end lo placeholder = &FF", align=Align.INLINE)
d.comment(0xB5B7, "Offset 7: buf1 end hi placeholder = &FF", align=Align.INLINE)
d.comment(0xB5B8, "Offset 8: buf2 start lo = &18", align=Align.INLINE)
d.comment(0xB5B9, "Offset 9: buf2 start hi (page from net_rx_ptr)", align=Align.INLINE)
d.comment(0xB5BA, "Offset 10: buf2 end lo placeholder = &FF", align=Align.INLINE)
d.comment(0xB5BB, "Offset 11: buf2 end hi placeholder = &FF", align=Align.INLINE)
d.entry(0xB5BC)
d.label(0xB5BC, "cmd_pollps")

d.subroutine(
    0xB5BC,
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
d.comment(0xB5BC, "Save command line pointer high", align=Align.INLINE)
d.comment(0xB5BE, "Initialise spool/print drive", align=Align.INLINE)
# UNMAPPED: d.comment(0xB586, "Save spool drive number", align=Align.INLINE)
d.comment(0xB5C1, "Copy PS name to TX buffer", align=Align.INLINE)
d.comment(0xB5C4, "Init PS slot from RX data", align=Align.INLINE)
d.comment(0xB5C7, "Restore command line pointer", align=Align.INLINE)
d.comment(0xB5C9, "Save pointer to spool buffer", align=Align.INLINE)
d.comment(0xB5CC, "Get first argument character", align=Align.INLINE)
d.comment(0xB5CE, "End of command line?", align=Align.INLINE)
d.comment(0xB5D0, "Yes: no argument given", align=Align.INLINE)
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
d.comment(0xB5D2, "Max 6 characters for PS name", align=Align.INLINE)
d.comment(0xB5D4, "Buffer offset for PS name", align=Align.INLINE)
d.comment(0xB5D6, "Space character", align=Align.INLINE)
d.label(0xB5D8, "loop_pad_poll_name")

d.comment(0xB5D8, "Fill buffer position with space", align=Align.INLINE)
d.comment(0xB5DA, "Next position", align=Align.INLINE)
d.comment(0xB5DB, "Count down", align=Align.INLINE)
d.comment(0xB5DC, "Loop until 6 spaces filled", align=Align.INLINE)
d.comment(0xB5DE, "Save pointer to OS text", align=Align.INLINE)
d.comment(0xB5E1, "Restore command line pointer", align=Align.INLINE)
d.comment(0xB5E3, "Initialise string reading", align=Align.INLINE)
d.comment(0xB5E6, "Empty string: skip to send", align=Align.INLINE)
d.comment(0xB5E8, "Max 6 characters", align=Align.INLINE)
d.comment(0xB5EA, "Save updated string pointer", align=Align.INLINE)
d.comment(0xB5EC, "Buffer offset for PS name", align=Align.INLINE)
d.comment(0xB5EE, "Save buffer position", align=Align.INLINE)
d.label(0xB5F0, "loop_read_poll_char")

d.comment(0xB5F0, "Restore string pointer", align=Align.INLINE)
d.comment(0xB5F2, "Read next char from string", align=Align.INLINE)
d.comment(0xB5F5, "Save updated string pointer", align=Align.INLINE)
d.comment(0xB5F7, "End of string: go to send", align=Align.INLINE)
d.comment(0xB5F9, "Store char uppercased in buffer", align=Align.INLINE)
d.comment(0xB5FC, "Loop if more chars to copy", align=Align.INLINE)
d.label(0xB5FE, "done_poll_name_parse")

d.comment(0xB5FE, "Enable escape checking", align=Align.INLINE)
d.comment(0xB600, "Set escapable flag", align=Align.INLINE)
d.comment(0xB602, "Send the poll request packet", align=Align.INLINE)
d.comment(0xB605, "Pop and requeue PS scan", align=Align.INLINE)
d.comment(0xB608, "Print 'Printer server '", align=Align.INLINE)
# UNMAPPED: d.comment(0xB601, "Load PS server address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB604, "Set V and N flags", align=Align.INLINE)
# UNMAPPED: d.comment(0xB607, "Print station address", align=Align.INLINE)
# UNMAPPED: d.comment(0xB60A, "Print ' \"'", align=Align.INLINE)
d.comment(0xB615, "Y=&18: name field offset in RX buffer", align=Align.INLINE)
d.label(0xB617, "loop_print_poll_name")

d.comment(0xB617, "Get character from name field", align=Align.INLINE)
d.comment(0xB619, "Is it a space?", align=Align.INLINE)
d.comment(0xB61B, "Yes: end of name", align=Align.INLINE)
d.comment(0xB620, "Next character", align=Align.INLINE)
d.comment(0xB621, "Past end of name field?", align=Align.INLINE)
d.comment(0xB623, "No: continue printing name", align=Align.INLINE)
d.label(0xB625, "done_poll_name_print")

d.comment(0xB625, "Print '\"' + CR", align=Align.INLINE)
# UNMAPPED: d.comment(0xB624, "Bit-7 terminator from preceding stringhi", align=Align.INLINE)
# UNMAPPED: d.comment(0xB625, "Pop saved slot index", align=Align.INLINE)
# UNMAPPED: d.label(0xB625, "loop_pollps_next_slot")

d.comment(0xB638, "Zero: all slots done, return", align=Align.INLINE)
d.comment(0xB63A, "Save slot offset", align=Align.INLINE)
d.comment(0xB63B, "Transfer to Y", align=Align.INLINE)
d.comment(0xB63C, "Read slot status byte", align=Align.INLINE)
d.comment(0xB63E, "Bit 7 clear: slot inactive", align=Align.INLINE)
d.comment(0xB640, "Advance to station number", align=Align.INLINE)
d.comment(0xB641, "Offset+2 in slot", align=Align.INLINE)
d.comment(0xB642, "Read station number low", align=Align.INLINE)
d.comment(0xB644, "Store station low", align=Align.INLINE)
d.comment(0xB646, "Next byte (offset+3)", align=Align.INLINE)
d.comment(0xB647, "Read network number", align=Align.INLINE)
d.comment(0xB649, "Store network number", align=Align.INLINE)
d.comment(0xB64B, "Next byte (offset+4)", align=Align.INLINE)
d.comment(0xB64C, "Read status page pointer", align=Align.INLINE)
d.comment(0xB64E, "Store pointer low", align=Align.INLINE)
d.comment(0xB650, "Clear V flag", align=Align.INLINE)
d.comment(0xB651, "Print station address (V=0)", align=Align.INLINE)
d.comment(0xB654, "Print ' is '", align=Align.INLINE)
d.comment(0xB65B, "X=0: indexed-indirect access mode", align=Align.INLINE)
d.comment(0xB65D, "Read printer status byte", align=Align.INLINE)
d.comment(0xB65F, "Non-zero: not ready", align=Align.INLINE)
d.comment(0xB661, "Print 'ready'", align=Align.INLINE)
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
d.comment(0xB6A0, "Print 'busy'", align=Align.INLINE)
d.comment(0xB6A7, "Advance work_ae to next status byte (lo)", align=Align.INLINE)
d.comment(0xB6A9, "Read client station number", align=Align.INLINE)
d.comment(0xB6AB, "Store station low", align=Align.INLINE)
d.comment(0xB6AD, "Zero: no client info, skip", align=Align.INLINE)
d.comment(0xB6AF, "Print ' with station '", align=Align.INLINE)
d.comment(0xB6C0, "Advance work_ae to next status byte (lo)", align=Align.INLINE)
d.comment(0xB6C2, "Read network number byte via (work_ae,X)", align=Align.INLINE)
d.comment(0xB6C4, "Store network number", align=Align.INLINE)
d.comment(0xB6C6, "Set V flag", align=Align.INLINE)
d.comment(0xB6C9, "Print client station address", align=Align.INLINE)
# UNMAPPED: d.label(0xB69A, "done_poll_status_line")

# UNMAPPED: d.label(0xB69D, "done_poll_slot_mark")

# UNMAPPED: d.comment(0xB69D, "Retrieve slot offset", align=Align.INLINE)
# UNMAPPED: d.comment(0xB69E, "Transfer to Y", align=Align.INLINE)
# UNMAPPED: d.comment(0xB69F, "Mark slot as processed (&3F)", align=Align.INLINE)
# UNMAPPED: d.comment(0xB6A1, "Write marker to workspace", align=Align.INLINE)
# UNMAPPED: d.label(0xB6A5, "rts_poll_slots")

# UNMAPPED: d.comment(0xB6A5, "Return", align=Align.INLINE)
d.label(0xB6CF, "init_ps_slot_from_rx")

d.subroutine(
    0xB6CF,
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


d.comment(0xB6CF, "Start at offset &78", align=Align.INLINE)
d.label(0xB6D1, "loop_copy_slot_tmpl")

d.comment(0xB6D1, "Load template byte", align=Align.INLINE)
d.comment(0xB6D4, "At offset &7D?", align=Align.INLINE)
d.comment(0xB6D6, "Yes: substitute RX page", align=Align.INLINE)
d.comment(0xB6D8, "At offset &81?", align=Align.INLINE)
d.comment(0xB6DA, "No: use template byte", align=Align.INLINE)
d.label(0xB6DC, "subst_rx_page_byte")

d.comment(0xB6DC, "Use RX buffer page instead", align=Align.INLINE)
d.label(0xB6DE, "store_slot_tmpl_byte")

d.comment(0xB6DE, "Store byte in slot buffer", align=Align.INLINE)
d.comment(0xB6E0, "Next offset", align=Align.INLINE)
d.comment(0xB6E1, "Past end of slot (&84)?", align=Align.INLINE)
d.comment(0xB6E3, "No: continue copying", align=Align.INLINE)
d.comment(0xB6E5, "Return", align=Align.INLINE)
d.label(0xB6E6, "store_char_uppercase")

d.subroutine(
    0xB6E6,
    "store_char_uppercase",
    title="Convert to uppercase and store in RX buffer",
    description="""If the character in A is lowercase (&61-&7A), converts
to uppercase by clearing bit 5. Stores the result in
the RX buffer at the current position, advances the
buffer pointer, and decrements the character count.""",
    on_entry={"a": "character to store"},
)


d.comment(0xB6E6, "Y = current buffer position", align=Align.INLINE)
d.comment(0xB6E8, "Strip high bit", align=Align.INLINE)
d.comment(0xB6EA, "Is it lowercase 'a' or above?", align=Align.INLINE)
d.comment(0xB6EC, "Below 'a': not lowercase", align=Align.INLINE)
d.comment(0xB6EE, "Above 'z'?", align=Align.INLINE)
d.comment(0xB6F0, "Yes: not lowercase", align=Align.INLINE)
d.comment(0xB6F2, "Convert to uppercase", align=Align.INLINE)
d.label(0xB6F4, "done_uppercase_store")

d.comment(0xB6F4, "Store in RX buffer", align=Align.INLINE)
d.comment(0xB6F6, "Next buffer position", align=Align.INLINE)
d.comment(0xB6F7, "Update buffer position", align=Align.INLINE)
d.comment(0xB6F9, "Decrement character count", align=Align.INLINE)
d.comment(0xB6FA, "Return (Z set if count=0)", align=Align.INLINE)
d.entry(0xB6FB)
d.entry(0xB6FB)
d.subroutine(
    0xB6FB,
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


d.comment(0xB6FB, "Load &FF (protect)", align=Align.INLINE)
d.entry(0xB6FF)
d.entry(0xB6FF)


d.subroutine(
    0xB6FF,
    "cmd_unprot",
    title="*Unprot command handler",
    description="""Loads `A=&00` (no protection) and falls through to the shared
protection-update body at `&B6D8`, which clears bit 6 of CMOS RAM
byte `&11` (the Econet protection flag). See
[`cmd_prot`](label:cmd_prot) for the full body description.""",
    on_entry={"y": "command line offset (unused; *Unprot takes no args)"},
)


d.comment(0xB6FF, "Load &00 (unprotect)", align=Align.INLINE)
d.label(0xB701, "unprot_clear")

d.comment(0xB701, "Save Z flag (1 = unprot, 0 = prot) for later", align=Align.INLINE)
d.comment(0xB702, "Mirror A into prot_status / prot_status_save pair", align=Align.INLINE)
d.comment(0xB705, "X=&11: CMOS offset for Econet flags", align=Align.INLINE)
d.comment(0xB707, "OSBYTE &A1 reads CMOS byte &11 -> Y", align=Align.INLINE)
d.comment(0xB70A, "A = current CMOS byte", align=Align.INLINE)
d.comment(0xB70B, "Restore the saved Z flag", align=Align.INLINE)
d.comment(0xB70C, "Z=1: unprot path", align=Align.INLINE)
d.comment(0xB70E, "Set bit 6 (protection on)", align=Align.INLINE)
d.comment(0xB710, "ALWAYS branch to write-back", align=Align.INLINE)
d.label(0xB712, "unprot_check")

d.comment(0xB712, "Clear bit 6 (protection off)", align=Align.INLINE)
d.label(0xB714, "unprot_apply")

d.comment(0xB714, "Y = new flag byte", align=Align.INLINE)
d.comment(0xB715, "OSBYTE &A2: write CMOS byte", align=Align.INLINE)
d.label(0xB717, "loop_match_prot_attr")

d.comment(0xB717, "X=&11: CMOS offset for Econet flags", align=Align.INLINE)
d.comment(0xB719, "Tail-call OSBYTE", align=Align.INLINE)
d.comment(0xB71C, "Reset access flags before parsing the new argument", align=Align.INLINE)
d.entry(0xB71C)

d.label(0xB71C, "cmd_wipe")


d.subroutine(
    0xB71C,
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


d.comment(0xB71F, "A=0: clear the file-iteration counter", align=Align.INLINE)
d.comment(0xB721, "Store iteration counter (steps to next file each loop)", align=Align.INLINE)
d.comment(0xB723, "Save text pointer for re-reading the wildcard each iteration", align=Align.INLINE)
d.comment(0xB726, "Parse the wildcard filename into the &C030 buffer", align=Align.INLINE)
d.comment(0xB729, "Step X past the CR terminator (so X = filename length+1)", align=Align.INLINE)
d.comment(0xB72A, "Save end-of-buffer offset", align=Align.INLINE)
d.label(0xB72C, "request_next_wipe")

d.subroutine(
    0xB72C,
    "request_next_wipe",
    title="Build 'examine directory' TXCB for next wipe iteration",
    description="""Issues FS function-code 1 ('examine directory entry') for the
current iteration in fs_work_5. Writes the function code into
TXCB[5] and TXCB[7], copies the iteration index to TXCB[6], and
falls through to the TXCB-build / send sequence. Single caller
(the BNE retry at &B768 that loops cmd_wipe over each match).""",
)


d.comment(0xB72C, "FS function code byte 0 = 1 (examine)", align=Align.INLINE)
d.comment(0xB72E, "TXCB[5] = 1: 'examine directory entry'", align=Align.INLINE)
d.comment(0xB731, "TXCB[7] = 1: ditto for the second buffer slot", align=Align.INLINE)
d.comment(0xB734, "Load current iteration index", align=Align.INLINE)
d.comment(0xB736, "TXCB[6] = iteration index (which directory entry)", align=Align.INLINE)
d.comment(0xB739, "X=3: copy starting at TX[3] (after the FS header bytes)", align=Align.INLINE)
d.comment(0xB73B, "Copy the parsed filename into the TX buffer", align=Align.INLINE)
d.comment(0xB73E, "Y=3: FS function code 'Examine'", align=Align.INLINE)
d.comment(0xB740, "A=&80: set bit 7 of need_release_tube to flag long-lived TX", align=Align.INLINE)
d.comment(0xB742, "Store flag", align=Align.INLINE)
d.comment(0xB744, "Send the examine request and wait for reply", align=Align.INLINE)
d.comment(0xB747, "Read FS reply byte 0 (status code)", align=Align.INLINE)
d.comment(0xB74A, "Non-zero status: process the response", align=Align.INLINE)
d.comment(0xB74C, "OSBYTE &0F: flush input buffer class", align=Align.INLINE)
d.comment(0xB74E, "X=1: flush keyboard buffer", align=Align.INLINE)
d.comment(0xB750, "Flush keyboard buffer (clear pending Y/N keypress)", align=Align.INLINE)
d.comment(0xB753, "OSBYTE &7A: scan keyboard from key 16 (clear keypress queue)", align=Align.INLINE)
d.comment(0xB755, "Run the scan", align=Align.INLINE)
d.comment(0xB758, "Y=0: no key", align=Align.INLINE)
d.comment(0xB75A, "OSBYTE &78: write keys-pressed state", align=Align.INLINE)
d.comment(0xB75C, "Tail-call OSBYTE: clean up and return", align=Align.INLINE)
d.label(0xB75F, "check_wipe_attr")

d.comment(0xB75F, "Read attribute byte from FS reply (TXCB[&2F])", align=Align.INLINE)
d.label(0xB762, "loop_check_if_locked")

d.comment(0xB762, "Is it 'L' (locked)?", align=Align.INLINE)
d.comment(0xB764, "Not locked: check for directory", align=Align.INLINE)
d.label(0xB766, "skip_wipe_locked")

d.comment(0xB766, "Locked: skip this file, advance to next", align=Align.INLINE)
d.comment(0xB768, "Loop back to request the next directory entry", align=Align.INLINE)
d.label(0xB76B, "check_wipe_dir")

d.comment(0xB76B, "Is it 'D' (directory)?", align=Align.INLINE)
d.comment(0xB76D, "Not a directory: prompt the user", align=Align.INLINE)
d.comment(0xB76F, "Directory: check second attribute byte (size)", align=Align.INLINE)
d.comment(0xB772, "Loop back to attribute test (re-checks if non-empty)", align=Align.INLINE)
d.label(0xB774, "show_wipe_prompt")

d.comment(0xB774, "X=1: scan name starting at TX[1]", align=Align.INLINE)
d.comment(0xB776, "Y = end-of-buffer offset (saved earlier in fs_work_6)", align=Align.INLINE)
d.label(0xB778, "loop_copy_wipe_name")

d.comment(0xB778, "Read filename byte from TX[6+X]", align=Align.INLINE)
d.comment(0xB77B, "Print via *SPOOL-bypassing OSASCI", align=Align.INLINE)
d.comment(0xB77E, "Also store into the parse buffer for later use", align=Align.INLINE)
d.comment(0xB781, "Step parse-buffer offset", align=Align.INLINE)
d.comment(0xB782, "Step TX-buffer offset", align=Align.INLINE)
d.comment(0xB783, "Reached &0C (12 chars)?", align=Align.INLINE)
d.comment(0xB785, "No: continue copying", align=Align.INLINE)
d.comment(0xB787, "Print '(?/' prompt prefix and read response", align=Align.INLINE)
d.comment(0xB78A, "Inline string '(?/' is read by the hook above", align=Align.INLINE)
d.comment(0xB78D, "NOP -- bit-7 terminator + resume opcode for the '(?/' stringhi", align=Align.INLINE)
d.comment(0xB78E, "Print 'Y/N) ' via prompt_yn (reads keypress)", align=Align.INLINE)
d.comment(0xB791, "Was the keypress '?' (help)?", align=Align.INLINE)
d.comment(0xB793, "Not '?': process Y/N response", align=Align.INLINE)
d.comment(0xB795, "'?': print CR before help text", align=Align.INLINE)
d.comment(0xB797, "Print CR character", align=Align.INLINE)
d.comment(0xB79A, "X=2: start of name in TX[2]", align=Align.INLINE)
d.label(0xB79C, "loop_print_wipe_info")

d.comment(0xB79C, "Read name byte from TX[5+X] (FS reply)", align=Align.INLINE)
d.comment(0xB79F, "Print name char (no spool)", align=Align.INLINE)
d.comment(0xB7A2, "Advance index", align=Align.INLINE)
d.comment(0xB7A3, "End of TX[5+X] name field at offset &3E?", align=Align.INLINE)
d.comment(0xB7A5, "No: continue printing", align=Align.INLINE)
d.comment(0xB7A7, "Print 'Wipe? ' help suffix via inline string", align=Align.INLINE)
d.comment(0xB7AC, "Bit-7 terminator + resume", align=Align.INLINE)
d.comment(0xB7AD, "Re-prompt user with prompt_yn", align=Align.INLINE)
d.label(0xB7B0, "check_wipe_response")

d.comment(0xB7B0, "Mask to upper-case ('A'..'Z' map to themselves)", align=Align.INLINE)
d.comment(0xB7B2, "Was the response 'Y'?", align=Align.INLINE)
d.comment(0xB7B4, "No: skip this entry, advance to next", align=Align.INLINE)
d.comment(0xB7B6, "Yes: echo the keypress", align=Align.INLINE)
d.comment(0xB7B9, "X=0: start scanning the parse-buffer name", align=Align.INLINE)
d.comment(0xB7BB, "Read first parse-buffer byte at hazel_parse_buf", align=Align.INLINE)
d.comment(0xB7BE, "Is it CR (no path component)?", align=Align.INLINE)
d.comment(0xB7C0, "Yes: use leaf-name only path at &B7E6", align=Align.INLINE)
d.label(0xB7C2, "loop_build_wipe_cmd")

d.comment(0xB7C2, "Read parse-buffer byte at hazel_parse_buf+X", align=Align.INLINE)
d.comment(0xB7C5, "Is it CR (end of name)?", align=Align.INLINE)
d.comment(0xB7C7, "No: check for space separator", align=Align.INLINE)
d.comment(0xB7C9, "CR: substitute '.' so the dir prefix terminates with a separator", align=Align.INLINE)
d.label(0xB7CB, "skip_if_not_space")

d.comment(0xB7CB, "Is it space?", align=Align.INLINE)
d.comment(0xB7CD, "No: store byte as-is", align=Align.INLINE)
d.label(0xB7CF, "set_wipe_cr_end")

d.comment(0xB7CF, "Yes: substitute CR (end-of-cmd)", align=Align.INLINE)
d.label(0xB7D1, "store_wipe_tx_char")

d.comment(0xB7D1, "Store byte into TX[5+X] (delete-command buffer)", align=Align.INLINE)
d.comment(0xB7D4, "Advance index", align=Align.INLINE)
d.comment(0xB7D5, "Was that byte CR (just stored)?", align=Align.INLINE)
d.comment(0xB7D7, "No: continue copying", align=Align.INLINE)
d.comment(0xB7D9, "Y=&14: FS function code &14 = delete", align=Align.INLINE)
d.comment(0xB7DB, "Send the delete request and wait for reply", align=Align.INLINE)
d.comment(0xB7DE, "Decrement iteration counter so we re-examine the now-shifted-up slot", align=Align.INLINE)
d.label(0xB7E0, "skip_wipe_to_next")

d.comment(0xB7E0, "Print newline before next entry", align=Align.INLINE)
d.comment(0xB7E3, "Loop back to skip_wipe_locked (= request next entry)", align=Align.INLINE)
d.label(0xB7E6, "use_wipe_leaf_name")

d.comment(0xB7E6, "DEX: pre-decrement before the INX in the loop", align=Align.INLINE)
d.label(0xB7E7, "loop_copy_wipe_leaf")

d.comment(0xB7E7, "Advance index", align=Align.INLINE)
d.comment(0xB7E8, "Read parse-buffer byte at hazel_parse_buf_1+X (skip CR at hazel_parse_buf)", align=Align.INLINE)
d.comment(0xB7EB, "Store into TX[5+X] (delete-command buffer)", align=Align.INLINE)
d.comment(0xB7EE, "Reached space (end-of-leaf)?", align=Align.INLINE)
d.comment(0xB7F0, "No: continue copying", align=Align.INLINE)
d.comment(0xB7F4, "Print 'Y/N) ' via the inline-string helper", align=Align.INLINE)
d.subroutine(
    0xB7F4,
    "prompt_yn",
    title="Print Y/N prompt and read user response",
    description="""Prints 'Y/N) ' via inline string, flushes
the input buffer, and reads a single character
from the keyboard.""",
    on_entry={},
    on_exit={"A": "character read from keyboard (after the 'Y/N) ' prompt)"},
)
d.comment(0xB7F7, "Inline string body — bytes consumed by print_inline_no_spool (above)", align=Align.INLINE)
d.label(0xB7FC, "flush_and_read_char")

d.subroutine(
    0xB7FC,
    "flush_and_read_char",
    title="Flush keyboard buffer and read one character",
    description="""Calls OSBYTE &0F to flush the input buffer, then
OSRDCH to read a single character. Raises an escape
error if escape was pressed (carry set on return).""",
    on_entry={},
    on_exit={"a": "character read from keyboard", "x, y": "clobbered (OSBYTE/OSRDCH)"},
)


d.comment(0xB7FC, "OSBYTE &0F: flush buffer class", align=Align.INLINE)
d.comment(0xB7FE, "X=1: flush input buffers", align=Align.INLINE)
d.comment(0xB800, "Flush keyboard buffer before read", align=Align.INLINE)
d.comment(0xB803, "Read character from input stream", align=Align.INLINE)
d.comment(0xB806, "C clear: character read OK", align=Align.INLINE)
d.comment(0xB808, "Escape pressed: raise error", align=Align.INLINE)
d.comment(0xB80B, "Return with character in A", align=Align.INLINE)
d.label(0xB80C, "init_channel_table")

d.subroutine(
    0xB80C,
    "init_channel_table",
    title="Initialise channel allocation table",
    description="""Clears all 256 bytes of the table, then marks
available channel slots based on the count from
the receive buffer. Sets the first slot to &C0
(active channel marker).""",
    on_exit={"a, x, y": "clobbered"},
)


d.comment(0xB80C, "A=0: clear value", align=Align.INLINE)
d.comment(0xB80E, "Y=0: start index", align=Align.INLINE)
d.label(0xB80F, "loop_clear_chan_table")

d.comment(0xB80F, "Clear channel table entry", align=Align.INLINE)
d.comment(0xB812, "Next entry", align=Align.INLINE)
d.comment(0xB813, "Loop until all 256 bytes cleared", align=Align.INLINE)
d.comment(0xB815, "Offset &0F in receive buffer", align=Align.INLINE)
d.comment(0xB817, "Get number of available channels", align=Align.INLINE)
d.comment(0xB819, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB81A, "Subtract 'Z' to get negative count", align=Align.INLINE)
d.comment(0xB81C, "Y = negative channel count (index)", align=Align.INLINE)
d.comment(0xB81D, "Channel marker &40 (available)", align=Align.INLINE)
d.label(0xB81F, "loop_mark_chan_avail")

d.comment(0xB81F, "Mark channel slot as available", align=Align.INLINE)
d.comment(0xB822, "Previous channel slot", align=Align.INLINE)
d.comment(0xB823, "Reached start of channel range?", align=Align.INLINE)
d.comment(0xB825, "No: continue marking channels", align=Align.INLINE)
d.comment(0xB827, "Point to first channel slot", align=Align.INLINE)
d.comment(0xB828, "Active channel marker &C0", align=Align.INLINE)
d.comment(0xB82A, "Mark first channel as active", align=Align.INLINE)
d.comment(0xB82D, "Return", align=Align.INLINE)
d.label(0xB82E, "attr_to_chan_index")

d.subroutine(
    0xB82E,
    "attr_to_chan_index",
    title="Convert channel attribute to table index",
    description="""Subtracts &20 from the attribute byte and clamps
to the range 0-&0F. Returns &FF if out of range.
Preserves processor flags via PHP/PLP.""",
    on_entry={"a": "channel attribute byte"},
    on_exit={"a": "table index (0-&0F) or &FF if invalid"},
)


d.comment(0xB82E, "Save flags", align=Align.INLINE)
d.comment(0xB82F, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB830, "Subtract &20 to get table index", align=Align.INLINE)
d.comment(0xB832, "Negative: out of valid range", align=Align.INLINE)
d.comment(0xB834, "Above maximum channel index &0F?", align=Align.INLINE)
d.comment(0xB836, "In range: valid index", align=Align.INLINE)
d.label(0xB838, "error_chan_out_of_range")

d.comment(0xB838, "Out of range: return &FF (invalid)", align=Align.INLINE)
d.label(0xB83A, "return_chan_index")

d.comment(0xB83A, "Restore flags", align=Align.INLINE)
d.comment(0xB83B, "X = channel index (or &FF)", align=Align.INLINE)
d.comment(0xB83C, "Return", align=Align.INLINE)
d.label(0xB83D, "check_chan_char")

d.subroutine(
    0xB83D,
    "check_chan_char",
    title="Validate channel character and look up entry",
    description="""Characters below '0' are looked up directly in
the channel table. Characters '0' and above are
converted to a table index via attr_to_chan_index.
Raises 'Net channel' error if invalid.""",
    on_entry={"a": "channel character"},
)


d.comment(0xB83D, "Below space?", align=Align.INLINE)
d.comment(0xB83F, "Yes: invalid channel character", align=Align.INLINE)
d.comment(0xB841, "Below '0'?", align=Align.INLINE)
d.comment(0xB843, "In range &20-&2F: look up channel", align=Align.INLINE)
d.label(0xB845, "err_net_chan_invalid")

d.subroutine(
    0xB845,
    "err_net_chan_invalid",
    title="Raise 'Net channel' error (saving channel char on stack)",
    description="""Pushes the bad channel character on the stack, then falls through to
error_chan_not_found which loads error code &DE and tail-calls
error_inline_log with the inline string 'Net channel'. The PHA at
entry differs from the &B81D error_chan_not_found alt-entry: this
form is reached when the caller has the channel character in A and
wants it preserved on the stack for the error handler to inspect.
Never returns -- error_inline_log triggers a BRK.""",
    on_entry={"a": "channel character (saved on stack)"},
)


d.comment(0xB845, "Save channel character", align=Align.INLINE)
d.label(0xB846, "error_chan_not_found")

d.comment(0xB846, "Error code &DE", align=Align.INLINE)
d.label(0xB848, "err_net_chan_not_found")

d.comment(0xB848, "Generate 'Net channel' error", align=Align.INLINE)
d.label(0xB84A, "net_chan_err_strings")
d.comment(0xB857, "Error string continuation (unreachable)", align=Align.INLINE)
d.comment(0xB85A, "Clear tx_buffer_scratch+X scratch", align=Align.INLINE)
d.label(0xB870, "lookup_chan_by_char")

d.subroutine(
    0xB870,
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


d.comment(0xB870, "Save channel character", align=Align.INLINE)
d.comment(0xB871, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB872, "Convert char to table index", align=Align.INLINE)
d.comment(0xB874, "X = channel table index", align=Align.INLINE)
d.comment(0xB875, "Look up network number for channel", align=Align.INLINE)
d.comment(0xB878, "Zero: channel not found, raise error", align=Align.INLINE)
d.comment(0xB87A, "Check station/network matches current", align=Align.INLINE)
d.comment(0xB87D, "No match: build detailed error msg", align=Align.INLINE)
d.comment(0xB87F, "Discard saved channel character", align=Align.INLINE)
d.comment(0xB880, "Load channel status flags", align=Align.INLINE)
d.comment(0xB883, "Return; A = channel flags", align=Align.INLINE)
d.label(0xB884, "error_chan_not_here")

d.comment(0xB884, "Error code &DE", align=Align.INLINE)
d.comment(0xB886, "Store error code in error block", align=Align.INLINE)
d.comment(0xB889, "BRK opcode", align=Align.INLINE)
d.comment(0xB88B, "Store BRK at start of error block", align=Align.INLINE)
d.comment(0xB88E, "X=0: copy index", align=Align.INLINE)
d.label(0xB88F, "loop_copy_chan_err_str")

d.comment(0xB88F, "Advance copy position", align=Align.INLINE)
d.comment(0xB890, "Load 'Net channel' string byte", align=Align.INLINE)
d.comment(0xB893, "Copy to error text", align=Align.INLINE)
d.comment(0xB896, "Continue until NUL terminator", align=Align.INLINE)
d.comment(0xB898, "Save end-of-string position", align=Align.INLINE)
d.comment(0xB89A, "Save for suffix append", align=Align.INLINE)
d.comment(0xB89C, "Retrieve channel character", align=Align.INLINE)
d.comment(0xB89D, "Append ' N' (channel number)", align=Align.INLINE)
d.comment(0xB8A0, "Load 'Net channel' end position", align=Align.INLINE)
d.label(0xB8A2, "loop_append_err_suffix")

d.comment(0xB8A2, "Skip past NUL to suffix string", align=Align.INLINE)
d.comment(0xB8A3, "Advance destination position", align=Align.INLINE)
d.comment(0xB8A4, "Load ' not on this...' suffix byte", align=Align.INLINE)
d.comment(0xB8A7, "Append to error message", align=Align.INLINE)
d.comment(0xB8AA, "Continue until NUL", align=Align.INLINE)
d.comment(0xB8AC, "Raise the constructed error", align=Align.INLINE)
d.label(0xB8AF, "store_result_check_dir")

d.subroutine(
    0xB8AF,
    "store_result_check_dir",
    title="Store channel attribute and check not directory",
    description="""Writes the current channel attribute to the receive
buffer, then tests the directory flag (bit 1). Raises
'Is a dir.' error if the attribute refers to a
directory rather than a file.""",
    on_entry={"a": "channel attribute byte to store and check"},
)


d.comment(0xB8AF, "Load current channel attribute", align=Align.INLINE)
d.comment(0xB8B2, "Store channel attribute to RX buffer", align=Align.INLINE)
d.label(0xB8B5, "check_not_dir")

d.subroutine(
    0xB8B5,
    "check_not_dir",
    title="Validate channel is not a directory",
    description="""Calls check_chan_char to validate the channel, then
tests the directory flag (bit 1). Raises 'Is a dir.'
error if the channel refers to a directory.""",
    on_entry={"a": "channel character (validated by check_chan_char)"},
)


d.comment(0xB8B5, "Validate and look up channel", align=Align.INLINE)
d.comment(0xB8B8, "Test directory flag (bit 1)", align=Align.INLINE)
d.comment(0xB8BA, "Not a directory: return OK", align=Align.INLINE)
d.comment(0xB8BC, "Error code &A8", align=Align.INLINE)
d.comment(0xB8BE, "Generate 'Is a dir.' error", align=Align.INLINE)
d.comment(0xB8D0, "Return", align=Align.INLINE)
d.label(0xB8D1, "alloc_fcb_slot")

d.subroutine(
    0xB8D1,
    "alloc_fcb_slot",
    title="Allocate a free file control block slot",
    description="""Scans FCB slots &20-&2F for an empty entry.
Returns Z=0 with X=slot index on success, or
Z=1 with A=0 if all slots are occupied.""",
    on_exit={"x": "slot index (if Z=0)", "z": "0=success, 1=no free slot"},
)


d.comment(0xB8D1, "Save channel attribute", align=Align.INLINE)
d.comment(0xB8D2, "Start scanning from FCB slot &20", align=Align.INLINE)
d.label(0xB8D4, "loop_scan_fcb_slots")

d.comment(0xB8D4, "Load FCB station byte", align=Align.INLINE)
d.comment(0xB8D7, "Zero: slot is free, use it", align=Align.INLINE)
d.comment(0xB8D9, "Try next slot", align=Align.INLINE)
d.comment(0xB8DA, "Past last FCB slot &2F?", align=Align.INLINE)
d.comment(0xB8DC, "No: check next slot", align=Align.INLINE)
d.comment(0xB8DE, "No free slot: discard saved attribute", align=Align.INLINE)
d.comment(0xB8DF, "A=0: return failure (Z set)", align=Align.INLINE)
d.comment(0xB8E1, "Return", align=Align.INLINE)
d.label(0xB8E2, "done_found_free_slot")

d.comment(0xB8E2, "Restore channel attribute", align=Align.INLINE)
d.comment(0xB8E3, "Store attribute in FCB slot", align=Align.INLINE)
d.comment(0xB8E6, "A=0: clear value", align=Align.INLINE)
d.comment(0xB8E8, "Clear FCB transfer count low", align=Align.INLINE)
d.comment(0xB8EB, "Clear FCB transfer count mid", align=Align.INLINE)
d.comment(0xB8EE, "Clear FCB transfer count high", align=Align.INLINE)
d.comment(0xB8F1, "Load current station number", align=Align.INLINE)
d.comment(0xB8F4, "Store station in FCB", align=Align.INLINE)
d.comment(0xB8F7, "Load current network number", align=Align.INLINE)
d.comment(0xB8FA, "Store network in FCB", align=Align.INLINE)
d.comment(0xB8FD, "Get FCB slot index", align=Align.INLINE)
d.comment(0xB8FE, "Save slot index", align=Align.INLINE)
d.comment(0xB8FF, "Prepare subtraction", align=Align.INLINE)
d.comment(0xB900, "Convert slot to channel index (0-&0F)", align=Align.INLINE)
d.comment(0xB902, "X = channel index", align=Align.INLINE)
d.comment(0xB903, "Restore A = FCB slot index", align=Align.INLINE)
d.comment(0xB904, "Return; A=slot, X=channel, Z clear", align=Align.INLINE)
d.label(0xB905, "alloc_fcb_or_error")

d.subroutine(
    0xB905,
    "alloc_fcb_or_error",
    title="Allocate FCB slot or raise error",
    description="""Calls alloc_fcb_slot and raises 'No more FCBs'
if no free slot is available. Preserves the
caller's argument on the stack.""",
    on_entry={"a": "caller's argument byte (saved/restored via PHA/PLA across the alloc call)"},
    on_exit={"x": "newly allocated FCB slot index (&20-&2F)", "a": "preserved"},
)


d.comment(0xB905, "Save argument", align=Align.INLINE)
d.comment(0xB906, "A=0: allocate any available slot", align=Align.INLINE)
d.comment(0xB908, "Try to allocate an FCB slot", align=Align.INLINE)
d.comment(0xB90B, "Success: slot allocated", align=Align.INLINE)
d.comment(0xB90D, "Error code &C0", align=Align.INLINE)
d.comment(0xB90F, "Generate 'No more FCBs' error", align=Align.INLINE)
d.label(0xB926, "return_alloc_success")

d.comment(0xB926, "Restore argument", align=Align.INLINE)
d.comment(0xB927, "Return", align=Align.INLINE)
d.label(0xB928, "close_all_net_chans")

d.subroutine(
    0xB928,
    "close_all_net_chans",
    title="Close all network channels for current station",
    description="""Scans FCB slots &0F down to 0, closing those
matching the current station. C=0 closes all
matching entries; C=1 closes with write-flush.""",
    on_entry={"c": "0=close all, 1=close with write-flush"},
)


d.comment(0xB928, "C=0: close all matching channels", align=Align.INLINE)
d.label(0xB929, "skip_set_carry")

d.comment(0xB929, "Branch always to scan entry", align=Align.INLINE)
d.label(0xB92C, "scan_fcb_flags")

d.subroutine(
    0xB92C,
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


d.comment(0xB92C, "Start from FCB slot &10", align=Align.INLINE)
d.label(0xB92E, "loop_scan_fcb_down")

d.comment(0xB92E, "Previous FCB slot", align=Align.INLINE)
d.comment(0xB92F, "More slots to check", align=Align.INLINE)
d.comment(0xB931, "All FCB slots processed, return", align=Align.INLINE)
d.label(0xB932, "skip_if_slots_done")

d.comment(0xB932, "Load channel flags for this slot", align=Align.INLINE)
d.comment(0xB935, "Save flags in Y", align=Align.INLINE)
d.comment(0xB936, "Test active flag (bit 1)", align=Align.INLINE)
d.comment(0xB938, "Not active: check station match", align=Align.INLINE)
d.comment(0xB93A, "V clear (close all): next slot", align=Align.INLINE)
d.comment(0xB93C, "C clear: check station match", align=Align.INLINE)
d.comment(0xB93E, "Restore original flags", align=Align.INLINE)
d.comment(0xB93F, "Clear write-pending flag (bit 5)", align=Align.INLINE)
d.comment(0xB941, "Update channel flags", align=Align.INLINE)
d.comment(0xB944, "Next slot (V always set here)", align=Align.INLINE)
d.label(0xB946, "done_check_station")

d.comment(0xB946, "Check if channel belongs to station", align=Align.INLINE)
d.comment(0xB949, "No match: skip to next slot", align=Align.INLINE)
d.comment(0xB94B, "A=0: clear channel", align=Align.INLINE)
d.comment(0xB94D, "Clear channel flags (close it)", align=Align.INLINE)
d.comment(0xB950, "Clear network number", align=Align.INLINE)
d.comment(0xB953, "Continue to next slot", align=Align.INLINE)
d.label(0xB955, "match_station_net")

d.subroutine(
    0xB955,
    "match_station_net",
    title="Check FCB slot matches current station/network",
    description="""Compares the station and network numbers in the
FCB at slot X against the current values using
EOR. Returns Z=1 if both match, Z=0 if either
differs.""",
    on_entry={"x": "FCB slot index"},
    on_exit={"z": "1=match, 0=no match"},
)


d.comment(0xB955, "Load FCB station number", align=Align.INLINE)
d.comment(0xB958, "Compare with current station", align=Align.INLINE)
d.comment(0xB95B, "Different: Z=0, no match", align=Align.INLINE)
d.comment(0xB95D, "Load FCB network number", align=Align.INLINE)
d.comment(0xB960, "Compare with current network", align=Align.INLINE)
d.label(0xB963, "rts_match_stn")

d.comment(0xB963, "Return; Z=1 if match, Z=0 if not", align=Align.INLINE)
d.label(0xB964, "find_open_fcb")

d.subroutine(
    0xB964,
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


d.comment(0xB964, "Load current FCB index", align=Align.INLINE)
d.comment(0xB967, "Set V flag (first pass marker)", align=Align.INLINE)
d.label(0xB96A, "loop_find_fcb")

d.comment(0xB96A, "Next FCB slot", align=Align.INLINE)
d.comment(0xB96B, "Past end of table (&10)?", align=Align.INLINE)
d.comment(0xB96D, "No: continue checking", align=Align.INLINE)
d.comment(0xB96F, "Wrap around to slot 0", align=Align.INLINE)
d.label(0xB971, "skip_if_no_wrap")

d.comment(0xB971, "Back to starting slot?", align=Align.INLINE)
d.comment(0xB974, "No: check this slot", align=Align.INLINE)
d.comment(0xB976, "V clear (second pass): scan empties", align=Align.INLINE)
d.comment(0xB978, "Clear V for second pass", align=Align.INLINE)
d.comment(0xB979, "Continue scanning", align=Align.INLINE)
d.label(0xB97B, "done_check_fcb_status")

d.comment(0xB97B, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB97E, "Shift bit 7 (in-use) into carry", align=Align.INLINE)
d.comment(0xB97F, "Not in use: skip", align=Align.INLINE)
d.comment(0xB981, "Test bit 2 (modified flag)", align=Align.INLINE)
d.comment(0xB983, "Modified: check further conditions", align=Align.INLINE)
d.label(0xB985, "done_select_fcb")

d.comment(0xB985, "Adjust for following INX", align=Align.INLINE)
d.label(0xB986, "loop_scan_empty_fcb")

d.comment(0xB986, "Next FCB slot", align=Align.INLINE)
d.comment(0xB987, "Past end of table?", align=Align.INLINE)
d.comment(0xB989, "No: continue", align=Align.INLINE)
d.comment(0xB98B, "Wrap around to slot 0", align=Align.INLINE)
d.label(0xB98D, "done_test_empty_slot")

d.comment(0xB98D, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB990, "Shift bit 7 into carry", align=Align.INLINE)
d.comment(0xB991, "Not in use: continue scanning", align=Align.INLINE)
d.comment(0xB993, "Set carry", align=Align.INLINE)
d.comment(0xB994, "Restore original flags", align=Align.INLINE)
d.comment(0xB995, "Save flags back (mark as found)", align=Align.INLINE)
d.comment(0xB998, "Restore original FCB index", align=Align.INLINE)
d.comment(0xB99B, "Return with found slot in X", align=Align.INLINE)
d.label(0xB99C, "skip_if_modified_fcb")

d.comment(0xB99C, "V set (first pass): skip modified", align=Align.INLINE)
d.comment(0xB99E, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB9A1, "Test bit 5 (offset pending)", align=Align.INLINE)
d.comment(0xB9A3, "Bit 5 set: skip this slot", align=Align.INLINE)
d.comment(0xB9A5, "Use this slot", align=Align.INLINE)
d.label(0xB9A7, "init_wipe_counters")

d.subroutine(
    0xB9A7,
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


d.comment(0xB9A7, "Initial pass count = 1", align=Align.INLINE)
d.comment(0xB9A9, "Store pass counter", align=Align.INLINE)
d.comment(0xB9AC, "Y=0", align=Align.INLINE)
d.comment(0xB9AD, "Clear byte counter low", align=Align.INLINE)
d.comment(0xB9B0, "Clear offset counter", align=Align.INLINE)
d.comment(0xB9B3, "Clear transfer flag", align=Align.INLINE)
d.comment(0xB9B6, "A=0", align=Align.INLINE)
d.comment(0xB9B7, "Clear 3 counter bytes", align=Align.INLINE)
d.label(0xB9B9, "loop_clear_counters")

d.comment(0xB9B9, "Clear counter byte", align=Align.INLINE)
d.comment(0xB9BC, "Next byte", align=Align.INLINE)
d.comment(0xB9BD, "Loop for indices 2, 1, 0", align=Align.INLINE)
d.comment(0xB9BF, "Store &FF as sentinel in xfer_sentinel_1", align=Align.INLINE)
d.comment(0xB9C2, "Store &FF as sentinel in xfer_sentinel_2", align=Align.INLINE)
d.comment(0xB9C5, "X=&CA: workspace offset", align=Align.INLINE)
d.comment(0xB9C7, "Y=&C2: HAZEL workspace page &C2", align=Align.INLINE)
d.comment(0xB9C9, "Return; X/Y point to &C2CA", align=Align.INLINE)
d.label(0xB9CA, "start_wipe_pass")

d.subroutine(
    0xB9CA,
    "start_wipe_pass",
    title="Start wipe pass for current FCB",
    description="""Verifies the workspace checksum, saves the station
context (pushing station low/high), initialises
transfer counters via init_wipe_counters, and sends
the initial request via send_and_receive. Clears the
active and offset flags on completion.""",
    on_entry={"x": "FCB slot index"},
)


d.comment(0xB9CA, "Verify workspace checksum integrity", align=Align.INLINE)
d.comment(0xB9CD, "Save current FCB index", align=Align.INLINE)
d.comment(0xB9D0, "Load FCB status flags", align=Align.INLINE)
d.comment(0xB9D3, "Shift bit 0 (active) into carry", align=Align.INLINE)
d.comment(0xB9D4, "Not active: clear status and return", align=Align.INLINE)
d.comment(0xB9D6, "Save current station low to stack", align=Align.INLINE)
d.comment(0xB9D9, "Push station low", align=Align.INLINE)
d.comment(0xB9DA, "Save current station high", align=Align.INLINE)
d.comment(0xB9DD, "Push station high", align=Align.INLINE)
d.comment(0xB9DE, "Load FCB station low", align=Align.INLINE)
d.comment(0xB9E1, "Set as working station low", align=Align.INLINE)
d.comment(0xB9E4, "Load FCB station high", align=Align.INLINE)
d.comment(0xB9E7, "Set as working station high", align=Align.INLINE)
d.comment(0xB9EA, "Reset transfer counters", align=Align.INLINE)
d.comment(0xB9ED, "Set offset to &FF (no data yet)", align=Align.INLINE)
d.comment(0xB9F0, "Set pass counter to 0 (flush mode)", align=Align.INLINE)
d.comment(0xB9F3, "Reload FCB index", align=Align.INLINE)
d.comment(0xB9F6, "Transfer to A", align=Align.INLINE)
d.comment(0xB9F7, "Prepare addition", align=Align.INLINE)
d.comment(0xB9F8, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xB9FA, "Store buffer address high byte", align=Align.INLINE)
d.comment(0xB9FD, "Load FCB status flags", align=Align.INLINE)
d.comment(0xBA00, "Test bit 5 (has saved offset)", align=Align.INLINE)
d.comment(0xBA02, "No offset: skip restore", align=Align.INLINE)
d.comment(0xBA04, "Load saved byte offset", align=Align.INLINE)
d.comment(0xBA07, "Restore offset counter", align=Align.INLINE)
d.label(0xBA0A, "done_restore_offset")

d.comment(0xBA0A, "Load FCB attribute reference", align=Align.INLINE)
d.comment(0xBA0D, "Store as current reference", align=Align.INLINE)
d.comment(0xBA10, "Transfer to X", align=Align.INLINE)
d.comment(0xBA11, "Read saved receive attribute", align=Align.INLINE)
d.comment(0xBA14, "Push to stack", align=Align.INLINE)
d.comment(0xBA15, "Restore attribute to A", align=Align.INLINE)
d.comment(0xBA16, "Set attribute in receive buffer", align=Align.INLINE)
d.comment(0xBA18, "X=&CA: workspace offset", align=Align.INLINE)
d.comment(0xBA1A, "Y=&C2: HAZEL workspace page &C2", align=Align.INLINE)
d.comment(0xBA1C, "A=0: standard transfer mode", align=Align.INLINE)
d.comment(0xBA1E, "Send data and receive response", align=Align.INLINE)
d.comment(0xBA21, "Reload FCB index", align=Align.INLINE)
d.comment(0xBA24, "Restore saved receive attribute", align=Align.INLINE)
d.comment(0xBA25, "Restore receive attribute", align=Align.INLINE)
d.comment(0xBA28, "Restore station high", align=Align.INLINE)
d.comment(0xBA29, "Store station high", align=Align.INLINE)
d.comment(0xBA2C, "Restore station low", align=Align.INLINE)
d.comment(0xBA2D, "Store station low", align=Align.INLINE)
d.label(0xBA30, "done_clear_fcb_active")

d.comment(0xBA30, "Mask &DC: clear bits 0, 1, 5", align=Align.INLINE)
d.comment(0xBA32, "Clear active and offset flags", align=Align.INLINE)
d.comment(0xBA35, "Update FCB status", align=Align.INLINE)
d.comment(0xBA38, "Return", align=Align.INLINE)
d.label(0xBA39, "save_fcb_context")

d.subroutine(
    0xBA39,
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


d.comment(0xBA39, "Copy 13 bytes (indices 0 to &0C)", align=Align.INLINE)
d.label(0xBA3B, "loop_save_tx_context")

d.comment(0xBA3B, "Load TX buffer byte", align=Align.INLINE)
d.comment(0xBA3E, "Save to context buffer at &10D9", align=Align.INLINE)
d.comment(0xBA41, "Load workspace byte from fs_load_addr", align=Align.INLINE)
d.comment(0xBA43, "Save to stack", align=Align.INLINE)
d.comment(0xBA44, "Next byte down", align=Align.INLINE)
d.comment(0xBA45, "Loop for all 13 bytes", align=Align.INLINE)
d.comment(0xBA47, "Y=0? (no FCB to process)", align=Align.INLINE)
d.comment(0xBA49, "Non-zero: scan and process FCBs", align=Align.INLINE)
d.comment(0xBA4B, "Y=0: skip to restore workspace", align=Align.INLINE)
d.label(0xBA4E, "done_save_context")

d.comment(0xBA4E, "Save flags", align=Align.INLINE)
d.comment(0xBA4F, "X=&FF: start scanning from -1", align=Align.INLINE)
d.label(0xBA51, "loop_find_pending_fcb")

d.comment(0xBA51, "Next FCB slot", align=Align.INLINE)
d.comment(0xBA52, "Load FCB status flags", align=Align.INLINE)
d.comment(0xBA55, "Bit 7 clear: not pending, skip", align=Align.INLINE)
d.comment(0xBA57, "Shift bit 6 to bit 7", align=Align.INLINE)
d.comment(0xBA58, "Bit 6 clear: skip", align=Align.INLINE)
d.comment(0xBA5A, "Flush this FCB's pending data", align=Align.INLINE)
d.comment(0xBA5D, "Pending marker &40", align=Align.INLINE)
d.comment(0xBA5F, "Mark FCB as pending-only", align=Align.INLINE)
d.comment(0xBA62, "Save flags", align=Align.INLINE)
d.comment(0xBA63, "Find next available FCB slot", align=Align.INLINE)
d.comment(0xBA66, "Restore flags", align=Align.INLINE)
d.comment(0xBA67, "Load current channel attribute", align=Align.INLINE)
d.comment(0xBA6A, "Store as current reference", align=Align.INLINE)
d.comment(0xBA6D, "Save attribute", align=Align.INLINE)
d.comment(0xBA6E, "Prepare attribute-to-channel conversion", align=Align.INLINE)
d.comment(0xBA6F, "Convert attribute (&20+) to channel index", align=Align.INLINE)
d.comment(0xBA71, "Y = attribute index", align=Align.INLINE)
d.comment(0xBA72, "Load station for this attribute", align=Align.INLINE)
d.comment(0xBA75, "Store station in TX buffer", align=Align.INLINE)
d.comment(0xBA78, "Restore attribute", align=Align.INLINE)
d.comment(0xBA79, "Store attribute in FCB slot", align=Align.INLINE)
d.comment(0xBA7C, "Load working station low", align=Align.INLINE)
d.comment(0xBA7F, "Store in TX buffer", align=Align.INLINE)
d.comment(0xBA82, "Load working station high", align=Align.INLINE)
d.comment(0xBA85, "Store in TX buffer", align=Align.INLINE)
d.comment(0xBA88, "Get FCB slot index", align=Align.INLINE)
d.comment(0xBA89, "Prepare addition", align=Align.INLINE)
d.comment(0xBA8A, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xBA8C, "Store buffer address high byte", align=Align.INLINE)
d.comment(0xBA8F, "Restore flags", align=Align.INLINE)
d.comment(0xBA90, "V clear: skip directory request", align=Align.INLINE)
d.comment(0xBA92, "Command byte = 0", align=Align.INLINE)
d.label(0xBA95, "done_init_wipe")

d.comment(0xBA95, "Reset transfer counters", align=Align.INLINE)
d.comment(0xBA98, "Read saved receive attribute", align=Align.INLINE)
d.comment(0xBA9B, "Function code &0D", align=Align.INLINE)
d.comment(0xBA9C, "Load current reference", align=Align.INLINE)
d.comment(0xBA9F, "Set in receive buffer", align=Align.INLINE)
d.comment(0xBAA1, "Y=&C2: HAZEL workspace page &C2", align=Align.INLINE)
d.comment(0xBAA3, "A=2: transfer mode 2", align=Align.INLINE)
d.comment(0xBAA5, "Send and receive data", align=Align.INLINE)
d.comment(0xBAA8, "Restore receive attribute", align=Align.INLINE)
d.comment(0xBAA9, "Restore receive attribute", align=Align.INLINE)
d.comment(0xBAAC, "Reload FCB index", align=Align.INLINE)
d.comment(0xBAAF, "Load pass counter", align=Align.INLINE)
d.comment(0xBAB2, "Non-zero: data received, calc offset", align=Align.INLINE)
d.comment(0xBAB4, "Load offset counter", align=Align.INLINE)
d.comment(0xBAB7, "Zero: no data received at all", align=Align.INLINE)
d.label(0xBAB9, "done_calc_offset")

d.comment(0xBAB9, "Load offset counter", align=Align.INLINE)
d.comment(0xBABC, "Negate (ones complement)", align=Align.INLINE)
d.comment(0xBABE, "Clear carry for add", align=Align.INLINE)
d.comment(0xBABF, "Complete twos complement negation", align=Align.INLINE)
d.comment(0xBAC1, "Store negated offset in FCB", align=Align.INLINE)
d.comment(0xBAC4, "Set bit 5 (has saved offset)", align=Align.INLINE)
d.comment(0xBAC6, "Add to FCB flags", align=Align.INLINE)
d.comment(0xBAC9, "Update FCB status", align=Align.INLINE)
d.comment(0xBACC, "Load buffer address high byte", align=Align.INLINE)
d.comment(0xBACF, "Set pointer high byte", align=Align.INLINE)
d.comment(0xBAD1, "A=0: pointer low byte and clear val", align=Align.INLINE)
d.comment(0xBAD3, "Set pointer low byte", align=Align.INLINE)
d.comment(0xBAD5, "Load negated offset (start of clear)", align=Align.INLINE)
d.label(0xBAD8, "loop_clear_buffer")

d.comment(0xBAD8, "Clear buffer byte", align=Align.INLINE)
d.comment(0xBADA, "Next byte", align=Align.INLINE)
d.comment(0xBADB, "Loop until page boundary", align=Align.INLINE)
d.label(0xBADD, "done_set_fcb_active")

d.comment(0xBADD, "Set bit 1 (active flag)", align=Align.INLINE)
d.comment(0xBADF, "Add active flag to status", align=Align.INLINE)
d.comment(0xBAE2, "Update FCB status", align=Align.INLINE)
d.comment(0xBAE5, "Y=0: start restoring workspace", align=Align.INLINE)
d.label(0xBAE7, "loop_restore_workspace")

d.subroutine(
    0xBAE7,
    "loop_restore_workspace",
    title="Pop 13 saved workspace bytes back to fs_load_addr+",
    description="""Y=0..&0C loop: PLA / STA fs_load_addr,Y / INY / CPY #&0D / BNE.
Restores the 13-byte FS-options block that save_fcb_context pushed
on the stack, undoing the protection the wipe/scan path put in
place. Two callers: the JMP at &BA4B (close-and-restore exit) and
the BNE retry at &BABE.""",
)


d.comment(0xBAE7, "Restore workspace byte from stack", align=Align.INLINE)
d.comment(0xBAE8, "Store to fs_load_addr workspace", align=Align.INLINE)
d.comment(0xBAEB, "Next byte", align=Align.INLINE)
d.comment(0xBAEC, "Restored all 13 bytes?", align=Align.INLINE)
d.comment(0xBAEE, "No: continue restoring", align=Align.INLINE)
d.label(0xBAF0, "restore_catalog_entry")

d.subroutine(
    0xBAF0,
    "restore_catalog_entry",
    title="Restore saved catalog entry to TX buffer",
    description="""Copies 13 bytes (Y=&0C..0) from
[`hazel_ctx_buffer`](label:hazel_ctx_buffer) back to the TX buffer
starting at [`hazel_txcb_port`](label:hazel_txcb_port). Falls through to
`find_matching_fcb`.""",
)


d.comment(0xBAF0, "Copy 13 bytes (indices 0 to &0C)", align=Align.INLINE)
d.label(0xBAF2, "loop_restore_tx_buf")

d.comment(0xBAF2, "Load saved catalog byte from &10D9", align=Align.INLINE)
d.comment(0xBAF5, "Restore to TX buffer", align=Align.INLINE)
d.comment(0xBAF8, "Next byte down", align=Align.INLINE)
d.comment(0xBAF9, "Loop for all bytes", align=Align.INLINE)
d.comment(0xBAFB, "Return", align=Align.INLINE)
d.label(0xBAFC, "loop_save_before_match")

d.subroutine(
    0xBAFC,
    "loop_save_before_match",
    title="Save FCB context, fall into find_matching_fcb",
    description="""Single-instruction wrapper at the top of the per-iteration FCB
search retry: JSR save_fcb_context to preserve the current attempt's
state (offset, station, network), then fall through into
find_matching_fcb. Single caller (the BNE retry at &BAEB). Used
once the first scan past slot &0F has failed and the search needs
to restart from slot 0 with the saved context restored.""",
)


d.comment(0xBAFC, "Save current context first", align=Align.INLINE)
d.label(0xBAFF, "find_matching_fcb")

d.subroutine(
    0xBAFF,
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


d.comment(0xBAFF, "X=&FF: start scanning from -1", align=Align.INLINE)
d.label(0xBB01, "loop_reload_attr")

d.comment(0xBB01, "Load channel attribute to match", align=Align.INLINE)
d.label(0xBB04, "loop_next_fcb_slot")

d.comment(0xBB04, "Next FCB slot", align=Align.INLINE)
d.comment(0xBB05, "Past end of table (&10)?", align=Align.INLINE)
d.comment(0xBB07, "No: check this slot", align=Align.INLINE)
d.comment(0xBB09, "Load channel attribute", align=Align.INLINE)
d.comment(0xBB0C, "Convert to channel index", align=Align.INLINE)
d.comment(0xBB0F, "Load station for this channel", align=Align.INLINE)
d.comment(0xBB12, "Store as match target station high", align=Align.INLINE)
d.comment(0xBB15, "Load port for this channel", align=Align.INLINE)
d.comment(0xBB18, "Store as match target station low", align=Align.INLINE)
d.comment(0xBB1B, "Save context and rescan from start", align=Align.INLINE)
d.label(0xBB1E, "done_test_fcb_active")

d.comment(0xBB1E, "Load FCB status flags", align=Align.INLINE)
d.comment(0xBB21, "Test active flag (bit 1)", align=Align.INLINE)
d.comment(0xBB23, "Not active: skip to next", align=Align.INLINE)
d.comment(0xBB25, "Get attribute to match", align=Align.INLINE)
d.comment(0xBB26, "Compare with FCB attribute ref", align=Align.INLINE)
d.comment(0xBB29, "No attribute match: skip", align=Align.INLINE)
d.comment(0xBB2B, "Save matching FCB index", align=Align.INLINE)
d.comment(0xBB2E, "Save flags from attribute compare", align=Align.INLINE)
d.comment(0xBB2F, "Prepare subtraction", align=Align.INLINE)
d.comment(0xBB30, "Convert attribute to channel index", align=Align.INLINE)
d.comment(0xBB32, "Restore flags from attribute compare", align=Align.INLINE)
d.comment(0xBB33, "Y = channel index", align=Align.INLINE)
d.comment(0xBB34, "Reload FCB index", align=Align.INLINE)
d.comment(0xBB37, "Load channel station byte", align=Align.INLINE)
d.comment(0xBB3A, "Compare with FCB station", align=Align.INLINE)
d.comment(0xBB3D, "Station mismatch: try next", align=Align.INLINE)
d.comment(0xBB3F, "Load channel network byte", align=Align.INLINE)
d.comment(0xBB42, "Compare with FCB network", align=Align.INLINE)
d.comment(0xBB45, "Network mismatch: try next", align=Align.INLINE)
d.comment(0xBB47, "Load FCB flags", align=Align.INLINE)
d.comment(0xBB4A, "Bit 7 clear: no pending flush", align=Align.INLINE)
d.comment(0xBB4C, "Clear pending flag (bit 7)", align=Align.INLINE)
d.comment(0xBB4E, "Update FCB status", align=Align.INLINE)
d.comment(0xBB51, "Find new open FCB slot", align=Align.INLINE)
d.comment(0xBB54, "Reload FCB flags", align=Align.INLINE)
d.label(0xBB57, "return_test_offset")

d.comment(0xBB57, "Test bit 5 (has offset data)", align=Align.INLINE)
d.comment(0xBB59, "Return; Z=1 no offset, Z=0 has data", align=Align.INLINE)
d.label(0xBB5A, "inc_fcb_byte_count")

d.subroutine(
    0xBB5A,
    "inc_fcb_byte_count",
    title="Increment 3-byte FCB transfer count",
    description="""Increments hazel_fcb_addr_lo+X (low), cascading overflow to
hazel_fcb_addr_mid+X (mid) and hazel_fcb_addr_hi+X (high).""",
    on_entry={"x": "FCB slot index"},
)


d.comment(0xBB5A, "Increment byte count low", align=Align.INLINE)
d.comment(0xBB5D, "No overflow: done", align=Align.INLINE)
d.comment(0xBB5F, "Increment byte count mid", align=Align.INLINE)
d.comment(0xBB62, "No overflow: done", align=Align.INLINE)
d.comment(0xBB64, "Increment byte count high", align=Align.INLINE)
d.label(0xBB67, "rts_inc_fcb_count")

d.comment(0xBB67, "Return", align=Align.INLINE)
d.subroutine(
    0xBB68,
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


d.comment(0xBB68, "Save X on entry", align=Align.INLINE)
d.comment(0xBB69, "Save Y across the body", align=Align.INLINE)
d.comment(0xBB6A, "X=&F7: save 9 workspace bytes (&F7..&FF)", align=Align.INLINE)
d.label(0xBB6C, "loop_save_fcb_workspace")

d.comment(0xBB6C, "Load workspace byte", align=Align.INLINE)
d.comment(0xBB6F, "Push fs_options", align=Align.INLINE)
d.comment(0xBB70, "Next byte", align=Align.INLINE)
d.comment(0xBB71, "X<0: more bytes to save", align=Align.INLINE)
d.comment(0xBB73, "Start from FCB slot &0F", align=Align.INLINE)
d.comment(0xBB75, "Store as current FCB index", align=Align.INLINE)
d.label(0xBB78, "loop_process_fcb")

d.comment(0xBB78, "Load current FCB index", align=Align.INLINE)
d.comment(0xBB7B, "Get filter attribute", align=Align.INLINE)
d.comment(0xBB7C, "Zero: process all FCBs", align=Align.INLINE)
d.comment(0xBB7E, "Compare with FCB attribute ref", align=Align.INLINE)
d.comment(0xBB81, "No match: skip this FCB", align=Align.INLINE)
d.label(0xBB83, "done_flush_fcb")

d.comment(0xBB83, "Save filter attribute", align=Align.INLINE)
d.comment(0xBB84, "Flush pending data for this FCB", align=Align.INLINE)
d.label(0xBB88, "done_advance_fcb")

d.comment(0xBB88, "Previous FCB index", align=Align.INLINE)
d.comment(0xBB8B, "More slots: continue loop", align=Align.INLINE)
d.comment(0xBB8D, "X=8: restore 9 workspace bytes", align=Align.INLINE)
d.label(0xBB8F, "loop_restore_fcb_ws")

d.comment(0xBB8F, "Restore fs_block_offset", align=Align.INLINE)
d.comment(0xBB90, "Restore workspace byte", align=Align.INLINE)
d.comment(0xBB92, "Next byte down", align=Align.INLINE)
d.comment(0xBB93, "More bytes: continue restoring", align=Align.INLINE)
d.comment(0xBB97, "Return", align=Align.INLINE)
d.subroutine(
    0xBB98,
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


d.entry(0xBB98)
d.comment(0xBB98, "Save channel attribute", align=Align.INLINE)
d.comment(0xBB9B, "Save caller's X", align=Align.INLINE)
d.comment(0xBB9C, "Push X", align=Align.INLINE)
d.comment(0xBB9D, "Store result and check not directory", align=Align.INLINE)
d.comment(0xBBA0, "Load channel flags", align=Align.INLINE)
d.comment(0xBBA3, "Test write-only flag (bit 5)", align=Align.INLINE)
d.comment(0xBBA5, "Not write-only: proceed with read", align=Align.INLINE)
d.comment(0xBBA7, "Error code &D4", align=Align.INLINE)
d.comment(0xBBA9, "Generate 'Write only' error", align=Align.INLINE)
d.label(0xBBB7, "done_read_fcb_byte")

d.comment(0xBBB7, "Clear V (first-pass matching)", align=Align.INLINE)
d.comment(0xBBB8, "Find FCB matching this channel", align=Align.INLINE)
d.comment(0xBBBB, "No offset: read byte from buffer", align=Align.INLINE)
d.comment(0xBBBD, "Load byte count for matching FCB", align=Align.INLINE)
d.comment(0xBBC0, "Compare with buffer offset limit", align=Align.INLINE)
d.comment(0xBBC3, "Below offset: data available", align=Align.INLINE)
d.comment(0xBBC5, "Load channel flags for FCB", align=Align.INLINE)
d.comment(0xBBC8, "Transfer to X for testing", align=Align.INLINE)
d.comment(0xBBC9, "Test bit 6 (EOF already signalled)", align=Align.INLINE)
d.comment(0xBBCB, "EOF already set: raise error", align=Align.INLINE)
d.comment(0xBBCD, "Restore flags", align=Align.INLINE)
d.comment(0xBBCE, "Set EOF flag (bit 6)", align=Align.INLINE)
d.comment(0xBBD0, "Update channel flags with EOF", align=Align.INLINE)
d.comment(0xBBD3, "A=0: clear receive attribute", align=Align.INLINE)
d.comment(0xBBD5, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0xBBD8, "Restore caller's X", align=Align.INLINE)
d.comment(0xBBD9, "X restored", align=Align.INLINE)
d.comment(0xBBDA, "A=&FE: EOF marker byte", align=Align.INLINE)
d.comment(0xBBDC, "Restore channel attribute", align=Align.INLINE)
d.comment(0xBBDF, "C=1: end of file", align=Align.INLINE)
d.comment(0xBBE0, "Return", align=Align.INLINE)
d.label(0xBBE1, "error_end_of_file")

d.comment(0xBBE1, "Error code &DF", align=Align.INLINE)
d.comment(0xBBE3, "Generate 'End of file' error", align=Align.INLINE)
d.label(0xBBF2, "done_load_from_buf")

d.comment(0xBBF2, "Load current byte count (= offset)", align=Align.INLINE)
d.comment(0xBBF5, "Save byte count", align=Align.INLINE)
d.comment(0xBBF6, "Get FCB slot index", align=Align.INLINE)
d.comment(0xBBF7, "X = FCB slot for byte count inc", align=Align.INLINE)
d.comment(0xBBF8, "A=0: clear receive attribute", align=Align.INLINE)
d.comment(0xBBFA, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0xBBFD, "Increment byte count for this FCB", align=Align.INLINE)
d.comment(0xBC00, "Restore byte count (= buffer offset)", align=Align.INLINE)
d.comment(0xBC01, "Y = offset into data buffer", align=Align.INLINE)
d.comment(0xBC02, "Load current FCB index", align=Align.INLINE)
d.comment(0xBC05, "Prepare addition", align=Align.INLINE)
d.comment(0xBC06, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xBC08, "Set pointer high byte", align=Align.INLINE)
d.comment(0xBC0A, "A=0: pointer low byte", align=Align.INLINE)
d.comment(0xBC0C, "Set pointer low byte", align=Align.INLINE)
d.comment(0xBC0E, "Restore caller's X", align=Align.INLINE)
d.comment(0xBC0F, "X restored", align=Align.INLINE)
d.comment(0xBC10, "Read data byte from buffer", align=Align.INLINE)
d.comment(0xBC12, "Restore channel attribute", align=Align.INLINE)
d.comment(0xBC15, "C=0: byte read successfully", align=Align.INLINE)
d.comment(0xBC16, "Return; A = data byte", align=Align.INLINE)
d.subroutine(
    0xBC17,
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


d.entry(0xBC17)


d.comment(0xBC17, "Save channel attribute", align=Align.INLINE)
d.comment(0xBC1A, "Save data byte", align=Align.INLINE)
d.comment(0xBC1B, "Y = data byte", align=Align.INLINE)
d.comment(0xBC1C, "Save caller's X", align=Align.INLINE)
d.comment(0xBC1D, "Push X", align=Align.INLINE)
d.comment(0xBC1E, "Restore data byte to A", align=Align.INLINE)
d.comment(0xBC1F, "Push data byte for later", align=Align.INLINE)
d.comment(0xBC20, "Save data byte in workspace", align=Align.INLINE)
d.comment(0xBC23, "Store result and check not directory", align=Align.INLINE)
d.comment(0xBC26, "Load channel flags", align=Align.INLINE)
d.comment(0xBC29, "Bit 7 set: channel open, proceed", align=Align.INLINE)
d.comment(0xBC2B, "Error &C1: Not open for update", align=Align.INLINE)
d.comment(0xBC2D, "Raise error with inline string", align=Align.INLINE)
d.label(0xBC44, "done_test_write_flag")

d.comment(0xBC44, "Test write flag (bit 5)", align=Align.INLINE)
d.comment(0xBC46, "Not write-capable: use buffer path", align=Align.INLINE)
d.comment(0xBC48, "Load reply port for this channel", align=Align.INLINE)
d.comment(0xBC4B, "Restore data byte", align=Align.INLINE)
d.comment(0xBC4C, "Send byte directly to server", align=Align.INLINE)
d.comment(0xBC4F, "Update byte count and return", align=Align.INLINE)
d.label(0xBC52, "done_find_write_fcb")

d.comment(0xBC52, "Set V flag (alternate match mode)", align=Align.INLINE)
d.comment(0xBC55, "Find matching FCB for channel", align=Align.INLINE)
d.comment(0xBC58, "Load byte count for FCB", align=Align.INLINE)
d.comment(0xBC5B, "Buffer full (&FF bytes)?", align=Align.INLINE)
d.comment(0xBC5D, "No: store byte in buffer", align=Align.INLINE)
d.comment(0xBC5F, "Save X", align=Align.INLINE)
d.label(0xBC62, "done_check_buf_offset")

d.comment(0xBC62, "Push Y", align=Align.INLINE)
d.comment(0xBC65, "Below offset: skip offset update", align=Align.INLINE)
d.comment(0xBC67, "Carry set from BCS/BCC above", align=Align.INLINE)
d.comment(0xBC69, "Update buffer offset in FCB", align=Align.INLINE)
d.comment(0xBC6C, "Non-zero: keep offset flag", align=Align.INLINE)
d.comment(0xBC6E, "Mask &DF: clear bit 5", align=Align.INLINE)
d.comment(0xBC70, "Clear offset flag", align=Align.INLINE)
d.comment(0xBC73, "Update FCB status", align=Align.INLINE)
d.label(0xBC76, "done_set_dirty_flag")

d.comment(0xBC76, "Set bit 0 (dirty/active)", align=Align.INLINE)
d.comment(0xBC78, "Add to FCB flags", align=Align.INLINE)
d.comment(0xBC7B, "Update FCB status", align=Align.INLINE)
d.comment(0xBC7E, "Load byte count (= write position)", align=Align.INLINE)
d.comment(0xBC81, "Save count", align=Align.INLINE)
d.comment(0xBC82, "Get FCB slot index", align=Align.INLINE)
d.comment(0xBC83, "X = FCB slot", align=Align.INLINE)
d.comment(0xBC84, "Restore byte count", align=Align.INLINE)
d.comment(0xBC85, "Y = buffer write offset", align=Align.INLINE)
d.comment(0xBC86, "Load current FCB index", align=Align.INLINE)
d.comment(0xBC89, "Prepare addition", align=Align.INLINE)
d.comment(0xBC8A, "Add &11 for buffer page offset", align=Align.INLINE)
d.comment(0xBC8C, "Set pointer high byte", align=Align.INLINE)
d.comment(0xBC8E, "A=0: pointer low byte", align=Align.INLINE)
d.comment(0xBC90, "Set pointer low byte", align=Align.INLINE)
d.comment(0xBC92, "Restore data byte", align=Align.INLINE)
d.comment(0xBC93, "Write data byte to buffer", align=Align.INLINE)
d.label(0xBC95, "done_inc_byte_count")

d.subroutine(
    0xBC95,
    "done_inc_byte_count",
    title="Increment FCB byte count, clear rx attr, restore caller",
    description="""JSRs inc_fcb_byte_count for the active FCB, then A=0 / JSR
store_rx_attribute (clears the receive-attribute byte). Pulls
saved X back into X (caller's value), discards the saved data byte
on the stack and returns. Single caller (the OSBPUT/PRINT path at
&BC1F).""",
)


d.comment(0xBC95, "Increment byte count for this FCB", align=Align.INLINE)
d.comment(0xBC98, "A=0: clear receive attribute", align=Align.INLINE)
d.comment(0xBC9A, "Clear receive attribute (A=0)", align=Align.INLINE)
d.comment(0xBC9D, "Restore caller's X", align=Align.INLINE)
d.comment(0xBC9E, "X restored", align=Align.INLINE)
d.comment(0xBC9F, "Discard saved data byte", align=Align.INLINE)
d.comment(0xBCA0, "Restore channel attribute", align=Align.INLINE)
d.comment(0xBCA3, "Return", align=Align.INLINE)
d.subroutine(
    0xBCA4,
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


d.comment(0xBCA4, "Save A", align=Align.INLINE)
d.comment(0xBCA5, "Save X", align=Align.INLINE)
d.comment(0xBCA7, "Read FCB slot attribute byte", align=Align.INLINE)
d.comment(0xBCAA, "Non-zero: station known -> store_station_and_flush", align=Align.INLINE)
d.subroutine(
    0xBCAC,
    "flush_fcb_with_init",
    title="Save FCB context and flush byte count to server",
    description="""Saves all registers and the current FCB context,
copies the FCB byte count into the TX command buffer,
and sends a flush/close request to the file server.
Restores the catalog entry and all registers on return.""",
    on_entry={"Y": "channel index (FCB slot)"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"},
)

d.comment(0xBCAC, "Save attribute byte (saved-station-test path)", align=Align.INLINE)
d.comment(0xBCAD, "Save X again", align=Align.INLINE)
d.comment(0xBCAE, "Save Y", align=Align.INLINE)
d.comment(0xBCAF, "Load station for this channel", align=Align.INLINE)
d.comment(0xBCB2, "Save station on stack", align=Align.INLINE)
d.comment(0xBCB3, "Y=0: reset index", align=Align.INLINE)
d.comment(0xBCB5, "Save current FCB context", align=Align.INLINE)
d.comment(0xBCB8, "Restore station from stack", align=Align.INLINE)
d.label(0xBCB9, "store_station_and_flush")


d.comment(0xBCB9, "Store station in command buffer", align=Align.INLINE)
d.comment(0xBCBD, "Save Y again for the next iteration", align=Align.INLINE)
d.comment(0xBCBE, "Save station for later restore", align=Align.INLINE)
d.comment(0xBCBF, "X=0", align=Align.INLINE)
d.comment(0xBCC1, "Clear function code", align=Align.INLINE)
d.comment(0xBCC4, "Load byte count lo from FCB", align=Align.INLINE)
d.comment(0xBCC7, "Store as data byte count", align=Align.INLINE)
d.comment(0xBCCA, "Load byte count mid from FCB", align=Align.INLINE)
d.comment(0xBCCD, "Store as reply command byte", align=Align.INLINE)
d.comment(0xBCD0, "Load byte count hi from FCB", align=Align.INLINE)
d.comment(0xBCD3, "Store as load vector field", align=Align.INLINE)
d.comment(0xBCD6, "Y=&0D: TX command byte offset", align=Align.INLINE)
d.comment(0xBCD8, "X=5: send 5 bytes", align=Align.INLINE)
d.comment(0xBCDA, "Send flush request to server", align=Align.INLINE)
d.comment(0xBCDD, "Restore station from stack", align=Align.INLINE)
d.comment(0xBCDE, "Y=station for wipe request", align=Align.INLINE)
d.comment(0xBCDF, "Load saved data byte", align=Align.INLINE)
d.comment(0xBCE2, "Send close/wipe request to server", align=Align.INLINE)
d.comment(0xBCE5, "Restore catalog state after flush", align=Align.INLINE)
d.comment(0xBCEA, "Restore A", align=Align.INLINE)
d.comment(0xBCEB, "Return", align=Align.INLINE)
d.label(0xBCEC, "send_wipe_request")

d.subroutine(
    0xBCEC,
    "send_wipe_request",
    title="Send wipe/close request packet",
    description="""Sets up the TX control block with function code
&90, the reply port from Y, and the data byte from
A. Sends via send_disconnect_reply, then checks the
error code — raises the server error if non-zero.""",
    on_entry={"a": "data byte to send", "y": "reply port"},
)


d.comment(0xBCEC, "Store reply port", align=Align.INLINE)
d.comment(0xBCEF, "Store data byte", align=Align.INLINE)
d.comment(0xBCF2, "Save Y", align=Align.INLINE)
d.comment(0xBCF3, "Push Y to stack", align=Align.INLINE)
d.comment(0xBCF4, "Save X", align=Align.INLINE)
d.comment(0xBCF5, "Push X to stack", align=Align.INLINE)
d.comment(0xBCF6, "Function code &90", align=Align.INLINE)
d.comment(0xBCF8, "Store in send buffer", align=Align.INLINE)
d.comment(0xBCFB, "Initialise TX control block", align=Align.INLINE)
d.comment(0xBCFE, "TX start address low = &DC", align=Align.INLINE)
d.comment(0xBD00, "Set TX start in control block", align=Align.INLINE)
d.comment(0xBD02, "TX end address low = &E0", align=Align.INLINE)
d.comment(0xBD04, "Set TX end in control block", align=Align.INLINE)
d.comment(0xBD06, "Expected reply port = 9", align=Align.INLINE)
d.comment(0xBD08, "Store reply port in buffer", align=Align.INLINE)
d.comment(0xBD0B, "TX control = &C0", align=Align.INLINE)
d.comment(0xBD0D, "Y=0: no timeout", align=Align.INLINE)
d.comment(0xBD0F, "Load reply port for addressing", align=Align.INLINE)
d.comment(0xBD12, "Send packet to server", align=Align.INLINE)
d.comment(0xBD15, "Load reply status", align=Align.INLINE)
d.comment(0xBD18, "Zero: success", align=Align.INLINE)
d.comment(0xBD1A, "Store error code", align=Align.INLINE)
d.comment(0xBD1D, "X=0: copy index", align=Align.INLINE)
d.label(0xBD1F, "loop_copy_wipe_err_msg")

d.comment(0xBD1F, "Load error message byte", align=Align.INLINE)
d.comment(0xBD22, "Copy to error block", align=Align.INLINE)
d.comment(0xBD25, "Is it CR (end of message)?", align=Align.INLINE)
d.comment(0xBD27, "Yes: terminate string", align=Align.INLINE)
d.comment(0xBD29, "Next byte", align=Align.INLINE)
d.comment(0xBD2A, "Continue copying error message", align=Align.INLINE)
d.label(0xBD2C, "done_terminate_wipe_err")

d.comment(0xBD2C, "NUL terminator", align=Align.INLINE)
d.comment(0xBD2E, "Terminate error string in block", align=Align.INLINE)
d.comment(0xBD31, "Back up position for error check", align=Align.INLINE)
d.comment(0xBD32, "Process and raise network error", align=Align.INLINE)
d.label(0xBD35, "done_toggle_station")

d.comment(0xBD35, "Load channel attribute index", align=Align.INLINE)
d.comment(0xBD38, "Load station number for channel", align=Align.INLINE)
d.comment(0xBD3B, "Toggle bit 0 (alternate station)", align=Align.INLINE)
d.comment(0xBD3D, "Update station number", align=Align.INLINE)
d.comment(0xBD40, "Restore X", align=Align.INLINE)
d.comment(0xBD41, "X restored", align=Align.INLINE)
d.comment(0xBD42, "Restore Y", align=Align.INLINE)
d.comment(0xBD43, "Y restored", align=Align.INLINE)
d.comment(0xBD44, "Return", align=Align.INLINE)
d.label(0xBD45, "send_and_receive")

d.subroutine(
    0xBD45,
    "send_and_receive",
    title="Set up FS options and transfer workspace",
    description="""Calls set_options_ptr to configure the FS options
pointer, then jumps to setup_transfer_workspace to
initialise the transfer and send the request.""",
    on_entry={"a": "transfer mode", "x": "workspace offset low", "y": "workspace page"},
)


d.comment(0xBD45, "Set up FS options pointer", align=Align.INLINE)
d.comment(0xBD48, "Set up transfer workspace and return", align=Align.INLINE)
d.subroutine(
    0xBD4B,
    "read_rx_attribute",
    title="Read receive attribute byte from RX buffer",
    description="""Reads byte at offset &0A in the network receive
control block, used to track which channel owns the
current receive buffer.""",
    on_entry={},
    on_exit={"A": "receive attribute byte", "Y": "&0A"},
)


d.comment(0xBD4B, "Y=&0A: receive attribute offset", align=Align.INLINE)
d.comment(0xBD4D, "Read byte from receive buffer", align=Align.INLINE)
d.comment(0xBD4F, "Return", align=Align.INLINE)
d.subroutine(
    0xBD50,
    "store_rx_attribute",
    title="Store receive attribute byte to RX buffer",
    description="""Writes A to offset &0A in the network receive
control block, marking which channel owns the
current receive buffer.""",
    on_entry={"A": "attribute byte to store"},
    on_exit={"Y": "&0A"},
)


d.comment(0xBD50, "Y=&0A: receive attribute offset", align=Align.INLINE)
d.comment(0xBD52, "Store byte to receive buffer", align=Align.INLINE)
d.comment(0xBD54, "Return", align=Align.INLINE)
d.label(0xBD55, "abort_if_escape")

d.subroutine(
    0xBD55,
    "abort_if_escape",
    title="Test escape flag and abort if pressed",
    description="""Checks the escape flag byte; returns immediately
if bit 7 is clear. If escape has been pressed,
falls through to the escape abort handler which
acknowledges the escape via OSBYTE &7E.""",
)


d.comment(0xBD55, "Test bit 7 of escape flag", align=Align.INLINE)
d.comment(0xBD57, "Escape pressed: handle abort", align=Align.INLINE)
d.comment(0xBD59, "No escape: return", align=Align.INLINE)
d.label(0xBD5A, "error_escape_pressed")

d.comment(0xBD5A, "Close the open file", align=Align.INLINE)
d.label(0xBD5D, "escape_error_close")

d.comment(0xBD60, "Acknowledge escape condition", align=Align.INLINE)
d.comment(0xBD65, "Error number &11", align=Align.INLINE)
d.comment(0xBD67, "Generate 'Escape' BRK error", align=Align.INLINE)
d.comment(0xBD71, "Open the file (handle stored in ws_page)", align=Align.INLINE)
d.entry(0xBD71)

d.label(0xBD71, "cmd_dump")

d.subroutine(
    0xBD71,
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


d.comment(0xBD74, "X=&14: 21-byte stack buffer for dump line state", align=Align.INLINE)
d.comment(0xBD76, "A=0: zero-fill", align=Align.INLINE)
d.label(0xBD78, "loop_push_zero_buf")

d.comment(0xBD78, "Push zero", align=Align.INLINE)
d.comment(0xBD79, "Step counter", align=Align.INLINE)
d.comment(0xBD7A, "Loop while X >= 0 (21 zeros)", align=Align.INLINE)
d.comment(0xBD7C, "Capture stack pointer for later restore", align=Align.INLINE)
d.comment(0xBD7D, "Parse address range and validate against file extent", align=Align.INLINE)
d.comment(0xBD80, "Read low nibble of starting address", align=Align.INLINE)
d.comment(0xBD82, "Mask high nibble (top 4 bits)", align=Align.INLINE)
d.comment(0xBD84, "Aligned (high nibble zero): skip the header print", align=Align.INLINE)
d.comment(0xBD86, "Print 'Address: 00 01 ... 0F: ASCII data' header", align=Align.INLINE)
d.label(0xBD89, "loop_dump_line")

d.subroutine(
    0xBD89,
    "loop_dump_line",
    title="*DUMP per-line read loop",
    description="""Body of cmd_dump's outer line loop. Calls abort_if_escape, then
reads up to 16 bytes from the open file via OSBGET into the line
buffer at (work_ae). On EOF mid-line, breaks to clean-up; on a
full line, falls through to the formatting and print stage.
Reachable from the alignment branch at &BD54 and the per-line tail
at &BE29.""",
)


d.comment(0xBD89, "Test escape and abort if pressed", align=Align.INLINE)
d.comment(0xBD8C, "A=&FF: count counter starts here so first INC -> 0", align=Align.INLINE)
d.comment(0xBD8E, "Save counter (-1)", align=Align.INLINE)
d.label(0xBD90, "loop_read_dump_byte")

d.comment(0xBD90, "Y = file handle", align=Align.INLINE)
d.comment(0xBD92, "Read one byte via OSBGET (C set on EOF)", align=Align.INLINE)
d.comment(0xBD95, "EOF: finish off this line then exit", align=Align.INLINE)
d.comment(0xBD97, "Increment count counter", align=Align.INLINE)
d.comment(0xBD99, "Y = current count (also buffer offset)", align=Align.INLINE)
d.comment(0xBD9B, "Store byte in 16-byte line buffer at (work_ae)+Y", align=Align.INLINE)
d.comment(0xBD9D, "Done all 16 bytes?", align=Align.INLINE)
d.comment(0xBD9F, "No: read next byte", align=Align.INLINE)
d.comment(0xBDA1, "C clear: not EOF (clean line)", align=Align.INLINE)
d.label(0xBDA2, "done_check_dump_eof")

d.comment(0xBDA2, "Save the EOF/clean flag", align=Align.INLINE)
d.comment(0xBDA3, "Reload counter byte", align=Align.INLINE)
d.comment(0xBDA5, "Bit 7 clear (counter is 0..&7F): bytes were read", align=Align.INLINE)
d.comment(0xBDA7, "EOF and no bytes: clean up and exit", align=Align.INLINE)
d.label(0xBDA9, "loop_pop_stack_buf")

d.subroutine(
    0xBDA9,
    "loop_pop_stack_buf",
    title="Drain saved bytes off stack and close",
    description="""Pulls X+1 bytes off the 6502 stack (clearing the temporary 21-byte
buffer cmd_dump uses to render each line) and tail-jumps to
close_ws_file. Reached from the in-line BPL at &BDAB and the
fall-through tail at &BE2E.""",
    on_entry={"x": "stack-byte count - 1 (caller sets it to &14 or &15)"},
)


d.comment(0xBDA9, "Restore one stack byte", align=Align.INLINE)
d.comment(0xBDAA, "Step", align=Align.INLINE)
d.comment(0xBDAB, "Loop while X >= 0 (22 pulls)", align=Align.INLINE)
d.comment(0xBDAD, "Tail-jump to close_ws_file", align=Align.INLINE)
d.label(0xBDB0, "done_check_boundary")

d.comment(0xBDB0, "Y=&10: read displayed-address byte 0", align=Align.INLINE)
d.comment(0xBDB2, "Read low byte", align=Align.INLINE)
d.comment(0xBDB4, "Top nibble", align=Align.INLINE)
d.comment(0xBDB6, "Non-zero: not a 256-byte boundary, skip header", align=Align.INLINE)
d.comment(0xBDB8, "Boundary: print column header", align=Align.INLINE)
d.label(0xBDBB, "done_start_dump_addr")

d.comment(0xBDBB, "Y=&13: highest byte of 4-byte address", align=Align.INLINE)
d.label(0xBDBD, "loop_print_addr_byte")

d.comment(0xBDBD, "Read address byte (highest first)", align=Align.INLINE)
d.comment(0xBDBF, "Save it (print_hex_byte clobbers A)", align=Align.INLINE)
d.comment(0xBDC0, "Print as 2 hex digits", align=Align.INLINE)
d.comment(0xBDC3, "Restore A", align=Align.INLINE)
d.comment(0xBDC4, "Step backwards", align=Align.INLINE)
d.comment(0xBDC5, "Reached low byte (offset &0F)?", align=Align.INLINE)
d.comment(0xBDC7, "No: continue printing", align=Align.INLINE)
d.comment(0xBDC9, "Y=&10: low byte of address", align=Align.INLINE)
d.comment(0xBDCA, "Clear C", align=Align.INLINE)
d.comment(0xBDCB, "Bump address by 16 bytes for next line", align=Align.INLINE)
d.comment(0xBDCD, "Save C from the add", align=Align.INLINE)
d.label(0xBDCE, "loop_inc_dump_addr")

d.comment(0xBDCE, "Restore C from previous step", align=Align.INLINE)
d.comment(0xBDCF, "Store updated address byte", align=Align.INLINE)
d.comment(0xBDD1, "Step Y up", align=Align.INLINE)
d.comment(0xBDD2, "Read next byte", align=Align.INLINE)
d.comment(0xBDD4, "Add carry from below", align=Align.INLINE)
d.comment(0xBDD6, "Save C", align=Align.INLINE)
d.comment(0xBDD7, "Done all 4 bytes (Y=&14)?", align=Align.INLINE)
d.comment(0xBDD9, "No: continue propagating", align=Align.INLINE)
d.comment(0xBDDB, "Restore final C", align=Align.INLINE)
d.comment(0xBDDC, "Print ' : ' separator before hex byte field", align=Align.INLINE)
d.comment(0xBDE2, "Y=0: start of buffer", align=Align.INLINE)
d.comment(0xBDE4, "X = byte counter (-1 initially, INC'd to 0..&0F)", align=Align.INLINE)
d.label(0xBDE6, "loop_print_dump_hex")

d.comment(0xBDE6, "Read byte from buffer", align=Align.INLINE)
d.comment(0xBDE8, "Print as hex + space", align=Align.INLINE)
d.label(0xBDEB, "loop_next_dump_col")

d.subroutine(
    0xBDEB,
    "loop_next_dump_col",
    title="*DUMP per-column advance and end-of-line check",
    description="""INY (next buffer offset), CPY #&10. End -> done_print_separator.
Otherwise DEX (decrement byte counter); BPL loop_print_dump_hex
to print the next byte. Single caller (the BPL at &BDFC after
short-line padding).""",
    on_entry={"x": "remaining bytes - 1", "y": "buffer offset"},
)


d.comment(0xBDEB, "Step buffer offset", align=Align.INLINE)
d.comment(0xBDEC, "Done all 16?", align=Align.INLINE)
d.comment(0xBDEE, "Yes: print separator before ASCII field", align=Align.INLINE)
d.comment(0xBDF0, "Step counter (Y was off-by-one from line read)", align=Align.INLINE)
d.comment(0xBDF1, "Have a real byte? Print it", align=Align.INLINE)
d.comment(0xBDF3, "End of partial line: pad with 3 spaces", align=Align.INLINE)
d.comment(0xBDF4, "Print '   ' inline", align=Align.INLINE)
d.comment(0xBDFA, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0xBDFB, "Restore Y", align=Align.INLINE)
d.comment(0xBDFC, "Continue padding the rest of the hex column", align=Align.INLINE)
d.label(0xBDFF, "done_print_separator")

d.comment(0xBDFF, "Counter has finished -- step it once more for the ASCII test", align=Align.INLINE)
d.comment(0xBE00, "Print ': ' inline (ASCII field separator)", align=Align.INLINE)
d.comment(0xBE05, "Y=0: rewind to start of line buffer", align=Align.INLINE)
d.comment(0xBE07, "Skip 16 padding spaces if needed (inx16)", align=Align.INLINE)
d.label(0xBE0A, "loop_print_dump_ascii")

d.comment(0xBE0A, "Read line buffer byte", align=Align.INLINE)
d.comment(0xBE0C, "Mask off bit 7 (DEL/inverted)", align=Align.INLINE)
d.comment(0xBE0E, "Below ' '? (control char)", align=Align.INLINE)
d.comment(0xBE10, "Yes: skip to substitution", align=Align.INLINE)
d.label(0xBE12, "skip_non_printable")

d.comment(0xBE12, "Substitute '.' for non-printables", align=Align.INLINE)
d.label(0xBE14, "done_test_del")

d.comment(0xBE14, "Compare with DEL", align=Align.INLINE)
d.comment(0xBE16, "Equal: also non-printable, substitute '.'", align=Align.INLINE)
d.comment(0xBE18, "Print the (possibly substituted) character", align=Align.INLINE)
d.comment(0xBE1B, "Step Y", align=Align.INLINE)
d.comment(0xBE1C, "Done 16 chars?", align=Align.INLINE)
d.comment(0xBE1E, "Yes: end this line", align=Align.INLINE)
d.comment(0xBE20, "Step counter back", align=Align.INLINE)
d.comment(0xBE21, "Loop while X >= 0", align=Align.INLINE)
d.label(0xBE23, "done_end_dump_line")

d.comment(0xBE23, "Print newline at end of line", align=Align.INLINE)
d.comment(0xBE26, "Restore EOF flag", align=Align.INLINE)
d.comment(0xBE27, "EOF: tidy up and exit", align=Align.INLINE)
d.comment(0xBE29, "More to dump: jump to next line", align=Align.INLINE)
d.label(0xBE2C, "done_dump_eof")

d.comment(0xBE2C, "X=&14: balance the loop_pop_stack_buf counter", align=Align.INLINE)
d.comment(0xBE2E, "Tail-jump to clean up the 21-byte stack buffer and close the file", align=Align.INLINE)
d.label(0xBE31, "print_dump_header")

d.subroutine(
    0xBE31,
    "print_dump_header",
    title="Print hex dump column header line",
    description="""Outputs the starting address followed by 16 hex
column numbers (00-0F), each separated by a space.
Provides the column alignment header for *Dump
output.""",
    on_exit={"a, x, y": "clobbered (print_hex_byte + OSASCI loop)"},
)


d.comment(0xBE31, "Read low nibble of starting address from (work_ae),Y", align=Align.INLINE)
d.comment(0xBE33, "Save it (we'll print it 16 times incrementing each iteration)", align=Align.INLINE)
d.comment(0xBE34, "Print '<CR>Address  : ' header via inline string", align=Align.INLINE)
d.comment(0xBE37, "*Dump column header", align=Align.INLINE)
d.comment(0xBE43, "X=&0F: print 16 column-number digits", align=Align.INLINE)
d.comment(0xBE45, "Pull the starting low nibble back into A", align=Align.INLINE)
d.comment(0xBE46, "Print A as two hex digits + space", align=Align.INLINE)
d.label(0xBE46, "loop_print_hex_row")

d.comment(0xBE49, "Set C ready for the increment", align=Align.INLINE)
d.comment(0xBE4A, "A += 1 (column index increments, with C set on entry)", align=Align.INLINE)
d.comment(0xBE4C, "Wrap to nibble (0..15)", align=Align.INLINE)
d.comment(0xBE4E, "Step column counter", align=Align.INLINE)
d.comment(0xBE4F, "Loop while X >= 0 (16 iterations)", align=Align.INLINE)
d.comment(0xBE51, "Print ':    ASCII data<CR><CR>' trailer via inline", align=Align.INLINE)
d.comment(0xBE54, "*Dump trailer", align=Align.INLINE)
d.comment(0xBE65, "NOP -- bit-7 terminator + harmless resume opcode", align=Align.INLINE)
d.comment(0xBE66, "Return", align=Align.INLINE)
d.label(0xBE67, "print_hex_and_space")

d.subroutine(
    0xBE67,
    "print_hex_and_space",
    title="Print hex byte followed by space",
    description="""Saves A, prints it as a 2-digit hex value via
print_hex_byte, outputs a space character, then
restores A from the stack. Used by cmd_dump and
print_dump_header for column-aligned hex output.""",
    on_entry={"a": "byte value to print"},
)


d.comment(0xBE67, "Save A so the caller can re-use the value", align=Align.INLINE)
d.comment(0xBE68, "Print A as two hex digits", align=Align.INLINE)
d.comment(0xBE6B, "A=' ': trailing column separator", align=Align.INLINE)
d.comment(0xBE6D, "Print the space via OSASCI", align=Align.INLINE)
d.label(0xBE70, "done_print_hex_space")

d.comment(0xBE70, "Restore caller's A", align=Align.INLINE)
d.comment(0xBE71, "Return", align=Align.INLINE)
d.label(0xBE72, "parse_dump_range")

d.subroutine(
    0xBE72,
    "parse_dump_range",
    title="Parse hex address for dump range",
    description="""Reads up to 4 hex digits from the command line
into a 4-byte accumulator, stopping at CR or
space. Each digit shifts the accumulator left
by 4 bits before ORing in the new nybble.""",
    on_entry={"y": "current command-line offset"},
    on_exit={"y": "advanced past the parsed digits", "a": "first non-hex character (CR or space)"},
)


d.comment(0xBE72, "Move command-line offset Y into A for the X copy", align=Align.INLINE)
d.comment(0xBE73, "X = current command-line offset (live cursor)", align=Align.INLINE)
d.comment(0xBE74, "A=0: zero-fill value", align=Align.INLINE)
d.comment(0xBE76, "Y=0: accumulator index", align=Align.INLINE)
d.label(0xBE77, "loop_clear_hex_accum")

d.comment(0xBE77, "Zero accumulator byte at (work_ae)+Y", align=Align.INLINE)
d.comment(0xBE79, "Step accumulator", align=Align.INLINE)
d.comment(0xBE7A, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0xBE7C, "No: continue clearing", align=Align.INLINE)
d.label(0xBE7E, "loop_parse_hex_digit")

d.subroutine(
    0xBE7E,
    "loop_parse_hex_digit",
    title="*DUMP / *LIST hex-address parser per-character body",
    description="""Reload command-line offset from X, INX (step cursor), TAY (use as
indirect index), read (os_text_ptr),Y. Branches: CR -> done; space
-> end of token; otherwise validate hex digit and shift it into the
4-byte accumulator. Single caller (the BNE retry at &BE95).""",
    on_entry={"x": "current command-line offset"},
)


d.comment(0xBE7E, "Reload command-line offset", align=Align.INLINE)
d.comment(0xBE7F, "Step cursor", align=Align.INLINE)
d.comment(0xBE80, "Y = stepped cursor (for the indirect read)", align=Align.INLINE)
d.comment(0xBE81, "Read next command-line byte", align=Align.INLINE)
d.comment(0xBE83, "CR? (end of address)", align=Align.INLINE)
d.comment(0xBE85, "Yes: range parsed -- exit via space-skip", align=Align.INLINE)
d.comment(0xBE87, "Space?", align=Align.INLINE)
d.comment(0xBE89, "Yes: also a separator -- exit", align=Align.INLINE)
d.comment(0xBE8B, "Below '0'?", align=Align.INLINE)
d.comment(0xBE8D, "Yes: not hex -- raise 'Bad hex'", align=Align.INLINE)
d.comment(0xBE8F, "Above '9'?", align=Align.INLINE)
d.comment(0xBE91, "No: it's '0'-'9' -- skip the letter handling", align=Align.INLINE)
d.comment(0xBE93, "Force uppercase via AND #&5F", align=Align.INLINE)
d.comment(
    0xBE95,
    "Add &B8: 'A' (=&41) becomes &F9 with C set; 'F' becomes &FE; this maps 'A'-'F' to &FA-&FF in C",
    align=Align.INLINE,
)
d.comment(0xBE97, "Carry out of ADC: digit was below 'A' -> bad hex", align=Align.INLINE)
d.comment(0xBE99, "Below &FA? (i.e. before 'A' in mapped range)", align=Align.INLINE)
d.comment(0xBE9B, "Yes (out of [&FA,&FF]): bad hex", align=Align.INLINE)
d.label(0xBE9D, "done_mask_hex_digit")

d.comment(0xBE9D, "Keep low nibble (0-15)", align=Align.INLINE)
d.comment(0xBE9F, "Push the new nibble", align=Align.INLINE)
d.comment(0xBEA0, "Push X (current command-line offset)", align=Align.INLINE)
d.comment(0xBEA1, "Preserve on stack", align=Align.INLINE)
d.comment(0xBEA2, "X=4: rotate the 4-byte accumulator left 4 times", align=Align.INLINE)
d.label(0xBEA4, "loop_shift_nibble")

d.comment(0xBEA4, "Y=0: byte index for the rotate", align=Align.INLINE)
d.comment(0xBEA6, "A=0 (and C clear from TYA's flags)", align=Align.INLINE)
d.label(0xBEA7, "loop_rotate_hex_accum")

d.comment(0xBEA7, "Save A onto stack so we can use PHP/PLP to round-trip carry through the rotate", align=Align.INLINE)
d.comment(
    0xBEA8,
    "Pull flags (effectively C clear from the TYA above; on later iterations C carries the bit shifted out)",
    align=Align.INLINE,
)
d.comment(0xBEA9, "Read next accumulator byte", align=Align.INLINE)
d.comment(0xBEAB, "Shift in C from below, shift out top bit to C", align=Align.INLINE)
d.comment(0xBEAC, "Write back", align=Align.INLINE)
d.comment(0xBEAE, "Save the new C", align=Align.INLINE)
d.comment(0xBEAF, "Pull A back (PHA earlier)", align=Align.INLINE)
d.comment(0xBEB0, "Step accumulator byte", align=Align.INLINE)
d.comment(0xBEB1, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0xBEB3, "No: rotate next byte", align=Align.INLINE)
d.comment(0xBEB5, "PHA/PLP: bring saved C into flag register", align=Align.INLINE)
d.comment(0xBEB6, "C = overflow bit", align=Align.INLINE)
d.comment(0xBEB7, "C set: a bit fell off the top -- overflow", align=Align.INLINE)
d.comment(0xBEB9, "Step rotate counter", align=Align.INLINE)
d.comment(0xBEBA, "Loop while X != 0 (4 rotates total)", align=Align.INLINE)
d.comment(0xBEBC, "Pull saved X (command-line offset)", align=Align.INLINE)
d.comment(0xBEBD, "Restore X", align=Align.INLINE)
d.comment(0xBEBE, "Pull saved nibble into A", align=Align.INLINE)
d.comment(0xBEBF, "Y=0: low byte of accumulator", align=Align.INLINE)
d.comment(0xBEC1, "OR new nibble into accumulator[0]", align=Align.INLINE)
d.comment(0xBEC3, "Write back", align=Align.INLINE)
d.comment(0xBEC5, "Loop for next hex digit", align=Align.INLINE)
d.label(0xBEC8, "error_hex_overflow")

d.comment(0xBEC8, "Discard saved nibble", align=Align.INLINE)
d.comment(0xBEC9, "Discard saved X", align=Align.INLINE)
d.comment(0xBECA, "Set C: signal overflow to caller", align=Align.INLINE)
d.comment(0xBECB, "Return with C=1", align=Align.INLINE)
d.label(0xBECC, "error_bad_hex_value")

d.comment(0xBECC, "Close the dump file before raising the error", align=Align.INLINE)
d.comment(0xBECF, "Raise 'Bad hex' error; never returns", align=Align.INLINE)
d.label(0xBED2, "loop_skip_hex_spaces")

d.comment(0xBED2, "Step past current space", align=Align.INLINE)
d.label(0xBED3, "done_test_hex_space")

d.comment(0xBED3, "Read next byte", align=Align.INLINE)
d.comment(0xBED5, "Still a space?", align=Align.INLINE)
d.comment(0xBED7, "Yes: keep skipping", align=Align.INLINE)
d.comment(0xBED9, "Clear C: signal success", align=Align.INLINE)
d.comment(0xBEDA, "Return", align=Align.INLINE)
d.label(0xBEDB, "init_dump_buffer")

d.subroutine(
    0xBEDB,
    "init_dump_buffer",
    title="Initialise dump buffer and parse address range",
    description="""Parses the start and end addresses from the command
line via parse_dump_range. If no end address is given,
defaults to the file extent. Validates both addresses
against the file size, raising 'Outside file' if either
exceeds the extent.""",
    on_entry={"y": "command-line offset of the address arguments"},
)


d.comment(0xBEDB, "Step Y past the *Dump command name into the argument", align=Align.INLINE)
d.comment(0xBEDC, "Save the cursor offset", align=Align.INLINE)
d.comment(0xBEDE, "Set bit 0 of addr_work to 1 -- 'mode' flag for parse_dump_range below", align=Align.INLINE)
d.comment(0xBEE0, "Save mode flag", align=Align.INLINE)
d.comment(0xBEE2, "Parse the start address (max 4 hex digits)", align=Align.INLINE)
d.comment(0xBEE5, "Overflow: too many digits", align=Align.INLINE)
d.comment(0xBEE7, "Save current Y (cursor after start address)", align=Align.INLINE)
d.comment(0xBEE8, "Push it", align=Align.INLINE)
d.comment(0xBEE9, "Y = file handle saved in ws_page", align=Align.INLINE)
d.comment(0xBEEB, "X=&AA: zero-page address for OSARGS result", align=Align.INLINE)
d.comment(0xBEED, "A=2: OSARGS sub-fn 2 = read sequential file extent", align=Align.INLINE)
d.comment(0xBEEF, "Get file size into 4 bytes at &AA", align=Align.INLINE)
d.comment(0xBEF2, "Y=3: compare 4-byte values (high to low)", align=Align.INLINE)
d.label(0xBEF4, "loop_cmp_file_length")

d.comment(0xBEF4, "Read file size byte at &AA+Y", align=Align.INLINE)
d.comment(0xBEF7, "Compare with parsed start address (work_ae+Y)", align=Align.INLINE)
d.comment(0xBEF9, "Mismatch: branch decides which is bigger", align=Align.INLINE)
d.comment(0xBEFB, "Step to next byte", align=Align.INLINE)
d.comment(0xBEFC, "Loop while Y >= 0 (covers indices 3, 2, 1, 0)", align=Align.INLINE)
d.comment(0xBEFE, "All bytes equal: start = extent (allowed); jump to the post-validation path", align=Align.INLINE)
d.label(0xBF00, "done_check_outside")

d.comment(0xBF00, "C clear: parsed_start > file_size -- reject", align=Align.INLINE)
d.comment(0xBF02, "Y=&FF: signal 'no copy needed' to the loop below", align=Align.INLINE)
d.comment(0xBF04, "Always taken: skip directly to advance phase", align=Align.INLINE)
d.label(0xBF06, "error_outside_file")

d.comment(0xBF06, "Close the file before raising", align=Align.INLINE)
d.comment(0xBF09, "A=&B7: 'Outside file' error code", align=Align.INLINE)
d.comment(0xBF0B, "Raise via inline string; never returns", align=Align.INLINE)
d.comment(0xBF0E, "*Dump range error", align=Align.INLINE)
d.label(0xBF1B, "loop_copy_osword_data")

d.label(0xBF1B, "loop_copy_start_addr")

d.comment(0xBF1B, "Copy file-extent byte from osword_flag to (work_ae)", align=Align.INLINE)
d.comment(0xBF1D, "Store it (used as default end address)", align=Align.INLINE)
d.label(0xBF20, "done_advance_start")

d.comment(0xBF20, "Step Y", align=Align.INLINE)
d.comment(0xBF21, "Done all 4 bytes?", align=Align.INLINE)
d.comment(0xBF23, "No: continue copying", align=Align.INLINE)
d.comment(0xBF25, "X=&AA: zero-page source for the OSARGS write-back", align=Align.INLINE)
d.comment(0xBF27, "Y = file handle", align=Align.INLINE)
d.comment(0xBF29, "A=1: OSARGS sub-fn 1 = write sequential file pointer", align=Align.INLINE)
d.comment(0xBF2B, "Set the file's read pointer to the parsed start", align=Align.INLINE)
d.comment(0xBF2E, "Pull saved cursor offset", align=Align.INLINE)
d.comment(0xBF2F, "Restore into Y", align=Align.INLINE)
d.comment(0xBF30, "Read next command-line byte", align=Align.INLINE)
d.comment(0xBF32, "CR (end of args)?", align=Align.INLINE)
d.comment(0xBF34, "No: there's a second arg -- handle below", align=Align.INLINE)
d.comment(0xBF36, "Y=1: copy os_text_ptr (2 bytes) to work_ae as a displacement-base hint", align=Align.INLINE)
d.label(0xBF38, "loop_copy_osfile_ptr")

d.comment(0xBF38, "Read os_text_ptr+Y", align=Align.INLINE)
d.comment(0xBF3B, "Save in work_ae+Y", align=Align.INLINE)
d.comment(0xBF3D, "Step backwards", align=Align.INLINE)
d.comment(0xBF3E, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xBF40, "A=5: OSFILE sub-fn 5 = read catalogue info", align=Align.INLINE)
d.comment(0xBF42, "X = filename pointer low (work_ae)", align=Align.INLINE)
d.comment(0xBF44, "Y = filename pointer high (addr_work)", align=Align.INLINE)
d.comment(0xBF46, "Read load address into work_ae+0..3", align=Align.INLINE)
d.comment(
    0xBF49, "Y=2: shift 3 bytes down 2 positions to drop the first 2 bytes (action code + a flag)", align=Align.INLINE
)
d.label(0xBF4B, "loop_shift_osfile_data")

d.comment(0xBF4B, "Read source byte", align=Align.INLINE)
d.comment(0xBF4D, "Y -= 2 (destination)", align=Align.INLINE)
d.comment(0xBF4E, "Continue decrement", align=Align.INLINE)
d.comment(0xBF4F, "Store at destination", align=Align.INLINE)
d.comment(0xBF51, "Y += 3 to advance to next source", align=Align.INLINE)
d.comment(0xBF52, "(continued)", align=Align.INLINE)
d.comment(0xBF53, "(continued)", align=Align.INLINE)
d.comment(0xBF54, "Done 6 bytes shifted?", align=Align.INLINE)
d.comment(0xBF56, "No: continue", align=Align.INLINE)
d.comment(0xBF58, "Y -= 2: position at high byte of load address", align=Align.INLINE)
d.comment(0xBF59, "Y=4: check from buf[4] downward", align=Align.INLINE)
d.label(0xBF5A, "loop_check_ff_addr")

d.comment(0xBF5A, "Read load-address byte at Y", align=Align.INLINE)
d.comment(0xBF5C, "Is it &FF (signals no real load address)?", align=Align.INLINE)
d.comment(0xBF5E, "No: have a real load address; add it as displacement", align=Align.INLINE)
d.comment(0xBF60, "Yes: step back to next higher byte", align=Align.INLINE)
d.comment(0xBF61, "Loop until Y=0", align=Align.INLINE)
d.comment(0xBF63, "All four bytes were &FF: zero out the load address", align=Align.INLINE)
d.comment(0xBF65, "A=0", align=Align.INLINE)
d.label(0xBF67, "loop_zero_load_addr")

d.comment(0xBF67, "Zero work_ae+Y", align=Align.INLINE)
d.comment(0xBF69, "Step backwards", align=Align.INLINE)
d.comment(0xBF6A, "Loop while Y >= 0", align=Align.INLINE)
d.comment(0xBF6C, "Always taken (after BPL drops out): skip second-arg path", align=Align.INLINE)
d.label(0xBF6E, "done_parse_disp_base")

d.comment(0xBF6E, "Parse end-address argument", align=Align.INLINE)
d.comment(0xBF71, "Success: continue with displacement-add", align=Align.INLINE)
d.comment(0xBF73, "Parse error: close file then raise 'Bad address'", align=Align.INLINE)
d.comment(0xBF76, "A=&FC: 'Bad address' error code", align=Align.INLINE)
d.comment(0xBF78, "Raise; never returns", align=Align.INLINE)
d.label(0xBF83, "done_add_disp_base")

d.comment(0xBF83, "Y=0: start of work_ae", align=Align.INLINE)
d.comment(0xBF85, "X=4: 4-byte add", align=Align.INLINE)
d.comment(0xBF87, "Clear C for the add", align=Align.INLINE)
d.label(0xBF88, "loop_add_disp_bytes")

d.comment(0xBF88, "Read low byte of address from (work_ae)+Y", align=Align.INLINE)
d.comment(0xBF8A, "Add osword_flag+Y (low byte of length, with carry propagating)", align=Align.INLINE)
d.comment(0xBF8D, "Store sum back to osword_flag+Y", align=Align.INLINE)
d.comment(0xBF90, "Advance to next byte", align=Align.INLINE)
d.comment(0xBF91, "Decrement byte counter", align=Align.INLINE)
d.comment(0xBF92, "Loop until 4 bytes added", align=Align.INLINE)
d.comment(
    0xBF94, "Y=&14: target offset = workspace+&13 (top of end-addr field, stored hi-byte-first)", align=Align.INLINE
)
d.comment(0xBF96, "X=3: source = osword_flag+3 (top byte of sum)", align=Align.INLINE)
d.label(0xBF98, "loop_store_disp_addr")

d.comment(0xBF98, "Pre-decrement Y (so first store is to offset &13)", align=Align.INLINE)
d.comment(0xBF99, "Read sum byte from osword_flag+X", align=Align.INLINE)
d.comment(0xBF9B, "Store at (work_ae)+Y", align=Align.INLINE)
d.comment(0xBF9D, "Decrement source index", align=Align.INLINE)
d.comment(0xBF9E, "Loop until X wraps below 0", align=Align.INLINE)
d.comment(0xBFA0, "Return", align=Align.INLINE)
d.label(0xBFA1, "close_ws_file")

d.subroutine(
    0xBFA1,
    "close_ws_file",
    title="Close file handle stored in workspace",
    description="""Loads the file handle from ws_page and closes it
via OSFIND with A=0.""",
    on_exit={"a, x, y": "clobbered (OSFIND)"},
)


d.comment(0xBFA1, "Y = saved file handle from ws_page", align=Align.INLINE)
d.comment(0xBFA3, "A=0: OSFIND close", align=Align.INLINE)
d.comment(0xBFA5, "Tail-call OSFIND to close the handle", align=Align.INLINE)
d.label(0xBFA8, "open_file_for_read")

d.subroutine(
    0xBFA8,
    "open_file_for_read",
    title="Open file for reading via OSFIND",
    description="""Computes the filename address from the command text
pointer plus the Y offset, calls OSFIND with A=&40
(open for input). Stores the handle in ws_page.
Raises 'Not found' if the returned handle is zero.""",
    on_entry={"y": "offset within the command line of the filename to open"},
    on_exit={"a, x, y": "clobbered"},
)

d.comment(0xBFA8, "Save flags so caller's NZC survive", align=Align.INLINE)
d.comment(0xBFA9, "Move command-line offset Y into A for the add", align=Align.INLINE)
d.comment(0xBFAA, "Clear C for the 16-bit add", align=Align.INLINE)
d.comment(0xBFAB, "A = os_text_ptr_lo + Y (filename address low byte)", align=Align.INLINE)
d.comment(0xBFAD, "Push it (we need to restore os_text_ptr after OSFIND)", align=Align.INLINE)
d.comment(0xBFAE, "Move filename low into X (OSFIND wants the address in X/Y)", align=Align.INLINE)
d.comment(0xBFAF, "A=0: zero high byte before the carry-add", align=Align.INLINE)
d.comment(0xBFB1, "Add os_text_ptr_hi with carry from the low add", align=Align.INLINE)
d.comment(0xBFB3, "Push filename high byte for the restore", align=Align.INLINE)
d.comment(0xBFB4, "Move filename high into Y", align=Align.INLINE)
d.comment(0xBFB5, "A=&40: OSFIND open-for-input mode", align=Align.INLINE)
d.comment(0xBFB7, "Open the file; returns handle in A (zero on failure)", align=Align.INLINE)
d.comment(0xBFBA, "Copy returned handle into Y (also sets Z if zero)", align=Align.INLINE)
d.comment(0xBFBB, "Stash the handle in ws_page for later close", align=Align.INLINE)
d.comment(0xBFBD, "Non-zero: open succeeded, skip error path", align=Align.INLINE)
d.comment(0xBFBF, "A=&D6: 'Not found' error code", align=Align.INLINE)
d.comment(0xBFC1, "Raise the error with the inline string below; never returns", align=Align.INLINE)
d.label(0xBFCE, "restore_text_ptr")

d.comment(
    0xBFCE,
    "Restore the saved filename high byte into os_text_ptr_hi -- but wait, this writes the FILENAME address into os_text_ptr; the caller intentionally moves os_text_ptr to scan past the filename below",
    align=Align.INLINE,
)
d.comment(0xBFCF, "Store as os_text_ptr_hi", align=Align.INLINE)
d.comment(
    0xBFD1,
    "Restore filename low byte into os_text_ptr_lo (so (os_text_ptr) now points at the filename)",
    align=Align.INLINE,
)
d.comment(0xBFD2, "Store as os_text_ptr lo", align=Align.INLINE)

d.comment(0xBFD4, "Y=0: scan from start of filename", align=Align.INLINE)
d.label(0xBFD6, "loop_skip_filename")

d.comment(0xBFD6, "Step to next byte", align=Align.INLINE)
d.comment(0xBFD7, "Read filename byte", align=Align.INLINE)
d.comment(0xBFD9, "Hit CR? End of command line", align=Align.INLINE)
d.comment(0xBFDB, "Yes: filename ended at CR (no trailing spaces)", align=Align.INLINE)
d.comment(0xBFDD, "Hit space? End of filename", align=Align.INLINE)
d.comment(0xBFDF, "No (still inside filename): keep scanning", align=Align.INLINE)
d.label(0xBFE1, "loop_skip_fn_spaces")

d.comment(0xBFE1, "Step past spaces", align=Align.INLINE)
d.comment(0xBFE2, "Read next byte", align=Align.INLINE)
d.comment(0xBFE4, "Still a space?", align=Align.INLINE)
d.comment(0xBFE6, "Yes: keep skipping", align=Align.INLINE)
d.label(0xBFE8, "done_skip_filename")


d.comment(0xBFE8, "Done: Y points just past the filename and any spaces", align=Align.INLINE)
d.comment(0xBFE9, "Restore caller's flags", align=Align.INLINE)
d.label(0xBFEA, "inx16")

d.subroutine(
    0xBFEA,
    "inx16",
    title="Increment X 16 times",
    description="""`JSR` [`inx8`](label:inx8), then fall through into `inx8` for a second pass — 16 `INX` instructions in total.""",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 16", "a, y": "preserved"},
)


d.comment(0xBFEA, "JSR inx8; on RTS, fall through into inx8 for the second 8", align=Align.INLINE)
d.label(0xBFED, "inx8")

d.subroutine(
    0xBFED,
    "inx8",
    title="Increment X 8 times",
    description="""`JSR` [`inx4`](label:inx4), then fall through into `inx4` for a second pass — 8 `INX` instructions in total.""",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 8", "a, y": "preserved"},
)


d.comment(0xBFED, "JSR inx4; on RTS, fall through into inx4 for the second 4", align=Align.INLINE)
d.label(0xBFF0, "inx4")
d.subroutine(
    0xBFF0,
    "inx4",
    title="Increment X 4 times",
    description="""Four consecutive `INX` instructions then `RTS`. Building block for [`inx8`](label:inx8) and [`inx16`](label:inx16) via JSR/fall-through chaining.""",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 4", "a, y": "preserved", "n, z flags": "reflect new X"},
)
d.comment(0xBFF0, "X += 4", align=Align.INLINE)
d.comment(0xBFF1, "(continued)", align=Align.INLINE)
d.comment(0xBFF2, "(continued)", align=Align.INLINE)
d.comment(0xBFF3, "(continued)", align=Align.INLINE)
d.comment(
    0xBFF4, "Return — total X advance depends on the entry: 4 (inx4), 8 (inx8), or 16 (inx16)", align=Align.INLINE
)
d.label(0xBFF5, "rom_tail_padding")
d.banner(
    0xBFF5,
    title="ROM-tail &FF padding (33 bytes positioning the HAZEL indexing bases)",
    description="""33 bytes of `&FF` filler between the last real instruction at
[`inx4`](label:inx4) and the HAZEL indexing-base labels
starting at [`hazel_minus_1a`](label:hazel_minus_1a).

These bytes exist purely to push the indexing-base labels to
specific addresses immediately before `&C000` (the start of
HAZEL). The labels themselves do the work -- see the
[`hazel_idx_bases`](label:hazel_idx_bases) banner. The padding is never
read or written; it is whatever the assembler emitted to fill
the gap (the BeebAsm default of `&FF`).""",
)

d.comment(0xBFF5, "ROM-tail padding (2 bytes &FF)", align=Align.INLINE)
d.byte(0xBFF7)

d.comment(0xBFF7, "ROM-tail padding (1 byte &FF; on its own line for annotation)", align=Align.INLINE)
d.comment(0xBFF8, "ROM-tail padding (30 bytes &FF)", align=Align.INLINE)
# UNMAPPED: d.index_base(0xBFE6, "hazel_minus_1a")

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
# UNMAPPED: d.index_base(0xBFFE, "hazel_minus_2")

# UNMAPPED: d.comment(
# UNMAPPED:     0xBFFE,
# UNMAPPED:     "Base for `hazel_minus_2,Y` reads/writes -- `&BFFE + Y` reaches into HAZEL for Y >= 2 (used by loop_copy_fs_ctx, loop_restore_ctx, loop_copy_ws_to_pb)",
# UNMAPPED:     align=Align.INLINE,
# UNMAPPED: )
# UNMAPPED: d.index_base(0xBFFF, "hazel_minus_1")

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
    0x864A,
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
    0x8BFB,
    "help_table_walk_entry",
    title="*HELP / command table walker per-entry body",
    description="""Per-entry body of the command / `*HELP` table walker:
saves Y and flags, then classifies `cmd_table_fs,X` (bit 7 marks a
sub-table terminator vs. a name byte). Called from the walker loop and
from the `*HELP` command lister.""",
)

d.subroutine(
    0x9657,
    "print_space_line",
    title="Print the 'Space' status label",
    description="""Emits the inline string `"Space"` + `CR` via
[`print_inline`](label:print_inline); the `&EA` (`NOP`) terminator resumes on
the trailing `RTS`. Called from the `*STATUS` / free-space report.""",
)

d.subroutine(
    0x85AD,
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
d.comment(0x85AD, "Clear decimal mode before the binary transfer-size arithmetic", align=Align.INLINE)


# Structural-alignment fills
# for instructions that align 1:1 and share the same mnemonic + mode.
d.comment(0x851F, "Clear carry for offset addition", align=Align.INLINE)
d.comment(0x864A, "Save X on stack", align=Align.INLINE)
d.comment(0x86B9, "Save interrupt state", align=Align.INLINE)
d.comment(0x86BA, "Disable interrupts for ADLC access", align=Align.INLINE)
d.comment(0x86C8, "INACTIVE not set -- re-enable NMIs and loop", align=Align.INLINE)
d.comment(0x8C0C, "Read cmd_table_fs+X (entry name byte)", align=Align.INLINE)
d.comment(0x8CCF, "Tail-call print_station_id to append ' Econet Station <n>' (and ' No Clock' if appropriate)", align=Align.INLINE)
d.comment(0x90E4, "Print as decimal (no leading zeros)", align=Align.INLINE)
d.comment(0x95B9, "NOP -- bit-7 terminator + resume opcode for the preceding inline string", align=Align.INLINE)
d.comment(0xA216, "Pull operation code", align=Align.INLINE)
d.comment(0xA217, "Shift right: check bit 0 (direction)", align=Align.INLINE)
d.comment(0xA218, "Push updated code", align=Align.INLINE)
d.comment(0xA219, "Carry clear: OSBGET (read)", align=Align.INLINE)
d.comment(0xA5F3, "Copy parsed arg to TX buffer with X=0", align=Align.INLINE)
d.comment(0xAF94, "Pop saved TX cmd", align=Align.INLINE)
d.comment(0xAF96, "Non-zero: retry from start_spool_retry", align=Align.INLINE)
d.comment(0xAFAF, "Not 1: take printer_busy_msg path", align=Align.INLINE)
d.comment(0xAFB1, "A=&AB: 'Printer off line' error code", align=Align.INLINE)
d.comment(0xAFB3, "Raise via error_inline_log (never returns)", align=Align.INLINE)
d.comment(0xB0A1, "Store at (nfs_workspace)+Y", align=Align.INLINE)
d.comment(0xB1E4, "Look up option-string offset for index X", align=Align.INLINE)
d.comment(0xB1E7, "Look up option byte at the resolved offset", align=Align.INLINE)
d.comment(0xB1EC, "Print char (no spool)", align=Align.INLINE)
d.comment(0xB1FE, "Print 10-char filename", align=Align.INLINE)
d.comment(0xB201, "Print inline 'attr-bits' fragment", align=Align.INLINE)
d.comment(0xB32C, "Print CR (no spool)", align=Align.INLINE)
d.comment(0xB404, "Load PS server address", align=Align.INLINE)
d.comment(0xB4AF, "Print station number and newline", align=Align.INLINE)
d.comment(0xB611, "Print ' \"'", align=Align.INLINE)
d.comment(0xB62A, "Bit-7 terminator from preceding stringhi", align=Align.INLINE)
d.comment(0xB637, "Pop saved slot index", align=Align.INLINE)
d.comment(0xB669, "Ensure V clear so next BVC always taken", align=Align.INLINE)
d.comment(0xB674, "Status = 2?", align=Align.INLINE)
d.comment(0xB676, "No: check for busy", align=Align.INLINE)
d.comment(0xB678, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB683, "Clear V", align=Align.INLINE)
d.comment(0xB686, "Status = 1?", align=Align.INLINE)
d.comment(0xB69D, "Not 1 or 2: default to jammed", align=Align.INLINE)

# --- manual coverage-gap annotations ---
d.index_base(0xA76F, "boot_cmd_lo_table")
d.index_base(0xBFE6, "hazel_minus_1a")
d.index_base(0xBFE6, "hazel_idx_bases")
d.index_base(0xBFFE, "hazel_minus_2")
d.comment(0xBFFE, "Base for `hazel_minus_2,Y` reads/writes -- `&BFFE + Y` reaches into HAZEL for Y >= 2", align=Align.INLINE)
d.index_base(0xBFFF, "hazel_minus_1")
d.label(0x80EA, "nmi_scout_data")
d.label(0x87FC, "nmi_tx_switch_rx")
d.label(0x882E, "nmi_reply_cont")
d.label(0x88BA, "nmi_data_tx_alt")
d.expr(0x80D6, lo(sym("nmi_scout_data")))
d.expr(0x87F8, lo(sym("nmi_tx_switch_rx")))
d.expr(0x882A, lo(sym("nmi_reply_cont")))
d.expr(0x88A5, lo(sym("nmi_data_tx_alt")))
d.expr(0x80B6, lo(sym("nmi_rx_scout_net")))
d.expr(0x81C1, lo(sym("nmi_data_rx")))
d.expr(0x81D5, lo(sym("nmi_data_rx_net")))
d.expr(0x8322, hi(sym("nmi_ack_tx_src")))
d.expr(0x8887, lo(sym("nmi_scout_ack_src")))
d.expr(0x8889, hi(sym("nmi_scout_ack_src")))
d.expr(0x88AC, lo(sym("nmi_data_tx_tube")))
d.expr(0x88AE, hi(sym("nmi_data_tx_tube")))
d.expr(0x8905, lo(sym("discard_reset_rx")))
d.expr(0x8907, hi(sym("discard_reset_rx")))
d.expr(0x895B, lo(sym("nmi_final_ack")))
d.expr(0x895D, hi(sym("nmi_final_ack")))
d.expr(0x8202, lo(sym("nmi_data_rx_bulk")))
d.expr(0x8204, hi(sym("nmi_data_rx_bulk")))
d.expr(0x820E, lo(sym("nmi_data_rx_tube")))
d.expr(0x8210, hi(sym("nmi_data_rx_tube")))
d.expr(0x8320, lo(sym("nmi_ack_tx_src")))
d.expr(0x83FE, lo(sym("nmi_rx_scout")))
d.expr(0x8400, hi(sym("nmi_rx_scout")))
d.expr(0x8565, hi(sym("tx_done_exit") - 1))
d.expr(0x8568, lo(sym("tx_done_exit") - 1))
d.expr(0x871D, lo(sym("nmi_tx_data")))
d.expr(0x8839, lo(sym("nmi_reply_validate")))
d.expr(0x8971, lo(sym("nmi_final_ack_net")))
d.expr(0x9C18, lo(sym("hazel_parse_buf")))
d.expr(0x9C1C, hi(sym("hazel_parse_buf")))
d.expr(0xA72A, lo(sym("findlib_oscli_cmd")))
d.expr(0xA72C, hi(sym("findlib_oscli_cmd")))
d.expr(0x8814, lo(sym("nmi_reply_scout")))
d.expr(0x8816, hi(sym("nmi_reply_scout")))
d.subroutine(0x8A1D, "nmi_return_inton", title="NMI exit: re-enable NMIs and return", description="""Two-instruction NMI tail: `BIT enable_net_nmis` (INTON, guaranteeing a fresh /NMI edge if the ADLC IRQ is still asserted) then `RTI`.""")
d.label(0x84DC, "imm_reply_flag")
d.label(0x86B9, "tx_irq_off")
d.label(0x872B, "tx_enable_nmis")
d.label(0xA5F3, "run_copy_arg_to_buf")
d.label(0xAF94, "spool_pop_cmd")
d.label(0xAFAD, "check_err_code_5")
d.label(0xAFC7, "err_printer_jammed")
d.label(0xB32C, "print_col_cr")
d.label(0xB4AF, "ps_print_info_newline")
d.label(0xBFE6, "skip_fn_space_cont")
d.label(0x86DB, "set_line_jammed")
d.label(0x851D, "imm_op_build_reply")
d.label(0x9FAB, "argsv_clamp_zero")
d.label(0x9FAF, "argsv_send_request")
d.label(0x9FB6, "argsv_store_result")
d.label(0xB1E7, "loop_print_option")
d.label(0xB637, "loop_next_poll_slot")
d.label(0xB66C, "poll_test_status")
d.label(0xB678, "poll_print_offline")
d.label(0xB686, "poll_check_busy")
d.label(0xB68A, "poll_print_jammed")
d.label(0xB694, "poll_entry_done")
d.label(0xB697, "poll_mark_slot")
d.label(0xB6A0, "poll_print_busy")
d.label(0xB62B, "poll_load_server")
d.index_base(0x8A23, "svc_dispatch_lo")
d.banner(0x8A23, title="svc_dispatch low-byte table (51 entries)",
    description="""Low-byte half of the `PHA`/`PHA`/`RTS` dispatch table read by
[`svc_dispatch`](label:svc_dispatch) as `LDA &8A23,X`. Paired with the high-byte
half at [`svc_dispatch_hi`](label:svc_dispatch_hi). Index 0 is an unused placeholder;
indices 1..50 cover service handlers, language replies, FSCV reasons, FS
replies and net-handle / OSWORD &13 trampolines. Per-entry inline comments
give each slot's dispatch.""")
d.index_base(0x8A56, "svc_dispatch_hi")
d.banner(0x8A56, title="svc_dispatch high-byte table (51 entries + 1 padding)",
    description="""High-byte half of the `PHA`/`PHA`/`RTS` dispatch table read as
`LDA &8A56,X`. The dispatcher pushes the high byte first then the low, so
`RTS` lands on target (each stored value is handler-1).""")
d.index_base(0xA9C8, "osword_13_dispatch_lo")
d.banner(0xA9C8, title="OSWORD &13 dispatch low-byte table (18 entries)",
    description="""Low-byte half of the OSWORD &13 sub-reason `PHA`/`PHA`/`RTS`
dispatch, read as `LDA &A9C8,X`; paired with
[`osword_13_dispatch_hi`](label:osword_13_dispatch_hi).""")
d.index_base(0xAD40, "netv_dispatch_lo")
d.banner(0xAD40, title="NETV reason-code dispatch low-byte table (9 entries)",
    description="""Low-byte half of the NETV reason-code `PHA`/`PHA`/`RTS`
dispatch, read as `LDA &AD40,X`; paired with
[`netv_dispatch_hi`](label:netv_dispatch_hi).""")
d.comment(0xB10C, "Index 5: threshold 39", align=Align.INLINE)
d.comment(0xB10D, "Index 6: threshold 49", align=Align.INLINE)
d.comment(0xB110, "Index 9: threshold 79", align=Align.INLINE)
d.comment(0xB114, "Index 13: threshold 118", align=Align.INLINE)
d.comment(0xB115, "Index 14: threshold 128", align=Align.INLINE)
d.comment(0xB118, "Index 17: threshold 157", align=Align.INLINE)
d.comment(0xB11B, "Index 20: threshold 187", align=Align.INLINE)
d.comment(0xB11D, "Index 22: threshold 207", align=Align.INLINE)
d.comment(0xADE6, "OSWORD &9A", align=Align.INLINE)
d.comment(0xADE9, "OSWORD &E2", align=Align.INLINE)
d.comment(0xADEC, "OSWORD &0B", align=Align.INLINE)
d.comment(0xADF0, "OSWORD &7A", align=Align.INLINE)
d.comment(0xADF1, "OSWORD &86", align=Align.INLINE)
d.comment(0x9AA4, "BRK error code &A0 (first table entry)", align=Align.INLINE)
d.comment(0x9AC5, "BRK error code &A3", align=Align.INLINE)
d.comment(0x9AE3, "BRK error code &A5", align=Align.INLINE)
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
d.comment(0xA80E, "&80 sub-table separator; the &8E44 word is the FS-command sub-table default handler (&8E45-1); the following &4F &6E &80 &00 &00 (ASCII 'On' + markers) is a 5-byte record new in this build", align=Align.INLINE)
d.comment(0x8397, "Unreached &D8 (CLD) byte after the RTS", align=Align.INLINE)
d.comment(0x8A21, "Padding before the service-dispatch low-byte table", align=Align.INLINE)
d.comment(0xADE3, "Range 1+2: OSWORD &0A", align=Align.INLINE)
d.comment(0xB03B, "buf start lo", align=Align.INLINE)
d.comment(0x91FE, "Syntax-table offset entry (into syn_opt_dir)", align=Align.INLINE)
d.comment(0xABFB, "TX init data byte &9C", align=Align.INLINE)
d.comment(0xA837, "NoSpace dispatch target (&9621)", align=Align.INLINE)
d.comment(0xA83F, "Space dispatch target (&9617)", align=Align.INLINE)
d.comment(0xA852, "Space dispatch target (&9640)", align=Align.INLINE)
d.comment(0x8003, "Service-call entry: jump to service_handler", align=Align.INLINE)
d.comment(0x8442, "Copy saved ACCCON to X", align=Align.INLINE)
d.comment(0x8458, "Index reached end: restore X and finish", align=Align.INLINE)
d.comment(0x852D, "Advance buffer index", align=Align.INLINE)
d.comment(0x859C, "Zero: transfer done, exit", align=Align.INLINE)
d.comment(0x85BD, "Next byte (descending)", align=Align.INLINE)
d.comment(0x8653, "Advance to destination network byte", align=Align.INLINE)
d.comment(0x86BB, "A=&40: 'line inactive' status code", align=Align.INLINE)
d.comment(0x86BD, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x86CD, "N set: line still driven, report jammed", align=Align.INLINE)
d.comment(0x86DB, "A=&2C: 'line jammed' status code", align=Align.INLINE)
d.comment(0x86DD, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x86F4, "Zero: report line jammed", align=Align.INLINE)
d.comment(0x86F8, "Branch to store TX error", align=Align.INLINE)
d.comment(0x8729, "A=&2C: 'line jammed' status code", align=Align.INLINE)
d.comment(0x872B, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x8753, "Non-zero: store control byte and add", align=Align.INLINE)
d.comment(0x8790, "C set: control byte out of range, exit", align=Align.INLINE)
d.comment(0x87DE, "Branch to store TX error", align=Align.INLINE)
d.comment(0x8815, "Install nmi_reply_scout (high)", align=Align.INLINE)
d.comment(0x89E8, "Compare to &80 (line-idle threshold)", align=Align.INLINE)
d.comment(0x89EC, "A=&40: 'line inactive' status code", align=Align.INLINE)
d.comment(0x89EE, "Store net poll-status byte", align=Align.INLINE)
d.comment(0x89F4, "A=0", align=Align.INLINE)
d.comment(0x8A9A, "Store the spool-control flag", align=Align.INLINE)
d.comment(0x8A9F, "C set: not ours, restore ROM slot and return", align=Align.INLINE)
d.comment(0x8BE8, "Zero args: print the command table", align=Align.INLINE)
d.comment(0x8BF6, "V clear: walk the next table entry", align=Align.INLINE)
d.comment(0x8BF8, "Print newline", align=Align.INLINE)
d.comment(0x8BFB, "Save Y", align=Align.INLINE)
d.comment(0x8C0F, "Print character", align=Align.INLINE)
d.comment(0x8C1B, "Print character", align=Align.INLINE)
d.comment(0x8C3B, "Print character", align=Align.INLINE)
d.comment(0x8C41, "Print newline", align=Align.INLINE)
d.comment(0x8C58, "Print newline", align=Align.INLINE)
d.comment(0x8C5F, "Print character", align=Align.INLINE)
d.comment(0x8CB6, "Loop back for the next character", align=Align.INLINE)
d.comment(0x8D05, "Print the station identity line", align=Align.INLINE)
d.comment(0x8D08, "Print newline", align=Align.INLINE)
d.comment(0x8D13, "A=4: library-selected flag bit", align=Align.INLINE)
d.comment(0x8D15, "Set the library-selected flag", align=Align.INLINE)
d.comment(0x8D9D, "bit-7 terminator + resume opcode", align=Align.INLINE)
d.comment(0x8DA7, "Save X", align=Align.INLINE)
d.comment(0x8DA8, "Save Y", align=Align.INLINE)
d.comment(0x8E0A, "Read a character (password entry, no echo)", align=Align.INLINE)
d.comment(0x8E0D, "Ctrl-U (&15): line-delete?", align=Align.INLINE)
d.comment(0x8E37, "Branch to send the command", align=Align.INLINE)
d.comment(0x8E61, "Not matched: fall to service dispatch", align=Align.INLINE)
d.comment(0x8E71, "Not matched: fall to service dispatch", align=Align.INLINE)
d.comment(0x8EEE, "Zero: tail-call OSBYTE", align=Align.INLINE)
d.comment(0x8F62, "Test the FS flags", align=Align.INLINE)
d.comment(0x8F6D, "Y=&21: workspace flag offset", align=Align.INLINE)
d.comment(0x8F6F, "Clear the workspace flag at &21", align=Align.INLINE)
d.comment(0x901B, "Merge into the FS flags", align=Align.INLINE)
d.comment(0x903C, "Toggle the workspace flag at &21", align=Align.INLINE)
d.comment(0x9092, "Positive: store the workspace byte", align=Align.INLINE)
d.comment(0x90FB, "Print newline", align=Align.INLINE)
d.comment(0x9252, "Tail-call OSASCI to print the nybble", align=Align.INLINE)
d.comment(0x9420, "Mask the FCB status flags", align=Align.INLINE)
d.comment(0x948A, "Copy A to X", align=Align.INLINE)
d.comment(0x95B4, "Print inline string", align=Align.INLINE)
d.comment(0x95BA, "Print the 'Space' free-space label", align=Align.INLINE)
d.comment(0x9655, "Branch to the shared CMOS-print return", align=Align.INLINE)
d.comment(0x9657, "Print inline string", align=Align.INLINE)
d.comment(0x9660, "bit-7 terminator + resume opcode", align=Align.INLINE)
d.comment(0x9661, "Return", align=Align.INLINE)
d.comment(0x967D, "Print newline", align=Align.INLINE)
d.comment(0x976F, "C set: copy TXCB with carry set", align=Align.INLINE)
d.comment(0x9772, "V clear: copy TXCB with carry clear", align=Align.INLINE)
d.comment(0x9862, "Advance index", align=Align.INLINE)
d.comment(0x99BC, "Branch to write the error number and string", align=Align.INLINE)
d.comment(0x9E9F, "Advance index", align=Align.INLINE)
d.comment(0xA44C, "Advance index", align=Align.INLINE)
d.comment(0xA47E, "XOR against the stored command character", align=Align.INLINE)
d.comment(0xA4B0, "Rotate result bit into carry", align=Align.INLINE)
d.comment(0xA4B1, "Decrement match counter", align=Align.INLINE)
d.comment(0xA503, "Branch to load the *RUN mask", align=Align.INLINE)
d.comment(0xA55F, "Rotate mask bit into carry", align=Align.INLINE)
d.comment(0xA5A1, "No match: retry via the library directory", align=Align.INLINE)
d.comment(0xA634, "Mask the OSWORD flag byte", align=Align.INLINE)
d.comment(0xA64F, "Return with the last-byte flag", align=Align.INLINE)
d.comment(0xA655, "Return with the last-byte flag", align=Align.INLINE)
d.comment(0xA681, "Match: store station flags and restore", align=Align.INLINE)
d.comment(0xA6AC, "Match: store station flags and restore", align=Align.INLINE)
d.comment(0xA729, "-NET-FindLib command pointer (low)", align=Align.INLINE)
d.comment(0xA72B, "-NET-FindLib command pointer (high)", align=Align.INLINE)
d.comment(0xA751, "Copy X to A", align=Align.INLINE)
d.comment(0xA998, "Branch to OSWORD-11 done", align=Align.INLINE)
d.comment(0xAA38, "Copy A to Y", align=Align.INLINE)
d.comment(0xAA4F, "Copy Y to A", align=Align.INLINE)
d.comment(0xAA52, "Copy A to Y", align=Align.INLINE)
d.comment(0xAB07, "Copy A to X", align=Align.INLINE)
d.comment(0xAB99, "Advance index", align=Align.INLINE)
d.comment(0xABD5, "Copy Y to A", align=Align.INLINE)
d.comment(0xABD8, "Advance index", align=Align.INLINE)
d.comment(0xABD9, "Branch to store the bridge station", align=Align.INLINE)
d.comment(0xACA3, "Advance index", align=Align.INLINE)
d.comment(0xACA4, "Advance index", align=Align.INLINE)
d.comment(0xACBC, "Advance index", align=Align.INLINE)
d.comment(0xACDD, "Advance index", align=Align.INLINE)
d.comment(0xAEE1, "Advance index", align=Align.INLINE)
d.comment(0xAF7A, "Copy A to X", align=Align.INLINE)
d.comment(0xAF7B, "Mask the low 3 bits", align=Align.INLINE)
d.comment(0xAF95, "Decrement", align=Align.INLINE)
d.comment(0xAF98, "Decrement counter", align=Align.INLINE)
d.comment(0xAFAD, "Error code = 5?", align=Align.INLINE)
d.comment(0xB09E, "Copy A to X", align=Align.INLINE)
d.comment(0xB0E2, "Branch when the *CDIR size is complete", align=Align.INLINE)
d.comment(0xB129, "C set: set the library flag", align=Align.INLINE)
d.comment(0xB12F, "C set: set the library flag", align=Align.INLINE)
d.comment(0xB149, "Branch to set up the *EX request", align=Align.INLINE)
d.comment(0xB192, "Print a 3-digit decimal (no spool)", align=Align.INLINE)
d.comment(0xB25A, "Tail-call print_newline_no_spool", align=Align.INLINE)
d.comment(0xB332, "XOR with zp_0078", align=Align.INLINE)
d.comment(0xB334, "Add zp_0063", align=Align.INLINE)
d.comment(0xB384, "Print the digit", align=Align.INLINE)
d.comment(0xB3BC, "Loop to the next character", align=Align.INLINE)
d.comment(0xB3F0, "Y=&21: workspace flag offset", align=Align.INLINE)
d.comment(0xB3F2, "A=0", align=Align.INLINE)
d.comment(0xB3F4, "Clear the workspace flag at &21", align=Align.INLINE)
d.comment(0xB45D, "Copy A to X", align=Align.INLINE)
d.comment(0xB474, "Mask the low 3 bits", align=Align.INLINE)
d.comment(0xB48C, "Loop to pop the next PS slot", align=Align.INLINE)
d.comment(0xB4A1, "V clear: branch onward", align=Align.INLINE)
d.comment(0xB4AA, "Y=&21: workspace flag offset", align=Align.INLINE)
d.comment(0xB4AC, "Copy Y to A", align=Align.INLINE)
d.comment(0xB4AD, "Store the workspace flag at &21", align=Align.INLINE)
d.comment(0xB4B8, "Advance index", align=Align.INLINE)
d.comment(0xB6FD, "Branch to the unprotect-clear path", align=Align.INLINE)
d.comment(0xB7F2, "Branch to set the wipe CR-end", align=Align.INLINE)
d.comment(0xBD5D, "Print newline", align=Align.INLINE)
d.comment(0xB60B, "Y=&21: PS-entry flag offset in workspace", align=Align.INLINE)
d.comment(0xB60D, "Load PS-entry flag", align=Align.INLINE)
d.comment(0xB60F, "Zero: slot empty, skip display", align=Align.INLINE)
d.comment(0xB61D, "Print character of PS name", align=Align.INLINE)
d.comment(0xB62B, "Load this PS server's address for display", align=Align.INLINE)
d.comment(0xB62E, "Set V (always) via always_set_v_byte", align=Align.INLINE)
d.comment(0xB631, "Print the server station address", align=Align.INLINE)
d.comment(0xB634, "Print newline", align=Align.INLINE)
d.comment(0xB66A, "Status ready printed: branch to end-of-entry (always)", align=Align.INLINE)
d.comment(0xB66C, "Shift status byte left to test its flag bits...", align=Align.INLINE)
d.comment(0xB66D, "...", align=Align.INLINE)
d.comment(0xB66E, "...", align=Align.INLINE)
d.comment(0xB66F, "...(4 shifts move bits 4-7 into C/N)", align=Align.INLINE)
d.comment(0xB670, "C set: status jammed", align=Align.INLINE)
d.comment(0xB672, "N set: status off line", align=Align.INLINE)
d.comment(0xB684, "Off-line printed: branch to end-of-entry (always)", align=Align.INLINE)
d.comment(0xB688, "Status = 1: print at cb6a0", align=Align.INLINE)
d.comment(0xB68A, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB693, "bit-7 terminator + resume opcode", align=Align.INLINE)
d.comment(0xB694, "Print newline after the status line", align=Align.INLINE)
d.comment(0xB697, "Pull saved slot index", align=Align.INLINE)
d.comment(0xB698, "Y = slot index", align=Align.INLINE)
d.comment(0xB699, "&3F: 'slot processed' marker", align=Align.INLINE)
d.comment(0xB69B, "Store the &3F marker in the workspace slot", align=Align.INLINE)
d.comment(0xB69F, "Return", align=Align.INLINE)
d.comment(0xB6CC, "Clear V for the unconditional branch", align=Align.INLINE)
d.comment(0xB6CD, "Branch to end-of-entry (always)", align=Align.INLINE)
d.comment(0x87A9, "Unwind first stacked byte", align=Align.INLINE)
d.comment(0x87AA, "Unwind second stacked byte", align=Align.INLINE)
d.comment(0x87AB, "Unwind third stacked byte", align=Align.INLINE)
d.comment(0x8B18, "Copy A to X", align=Align.INLINE)
d.comment(0x8B1B, "Copy A to Y", align=Align.INLINE)
d.comment(0x8BF3, "Restore Y", align=Align.INLINE)
d.comment(0x8BF4, "Restore X", align=Align.INLINE)
d.comment(0x8C65, "Restore Y", align=Align.INLINE)
d.comment(0x8CF1, "Copy X to A", align=Align.INLINE)
d.comment(0x8CFC, "Copy A to Y", align=Align.INLINE)
d.comment(0x8DBB, "Restore Y", align=Align.INLINE)
d.comment(0x8DBC, "Restore X", align=Align.INLINE)
d.comment(0x8DC1, "Restore Y", align=Align.INLINE)
d.comment(0x8E33, "Restore X", align=Align.INLINE)
d.comment(0x90A7, "Save Y", align=Align.INLINE)
d.comment(0x90B8, "Restore Y", align=Align.INLINE)
d.comment(0x942D, "Save X", align=Align.INLINE)
d.comment(0x9434, "Restore X", align=Align.INLINE)
d.comment(0x9486, "Restore Y", align=Align.INLINE)
d.comment(0x94CD, "Save X", align=Align.INLINE)
d.comment(0x94D7, "Restore X", align=Align.INLINE)
d.comment(0x982C, "Unwind stacked byte", align=Align.INLINE)
d.comment(0x982D, "Unwind stacked byte", align=Align.INLINE)
d.comment(0x9A0B, "Save Y", align=Align.INLINE)
d.comment(0x9A11, "Restore Y", align=Align.INLINE)
d.comment(0xA105, "Save Y", align=Align.INLINE)
d.comment(0xA111, "Restore Y", align=Align.INLINE)
d.comment(0xA121, "Copy A to Y", align=Align.INLINE)
d.comment(0xA199, "Restore Y", align=Align.INLINE)
d.comment(0xB3EF, "Save Y", align=Align.INLINE)
d.comment(0xB3F6, "Restore Y", align=Align.INLINE)
d.comment(0xB403, "Save Y", align=Align.INLINE)
d.comment(0xB407, "Restore Y", align=Align.INLINE)
d.comment(0xBB87, "Restore Y", align=Align.INLINE)
d.comment(0xBB95, "Restore Y", align=Align.INLINE)
d.comment(0xBB96, "Restore X", align=Align.INLINE)
d.comment(0xBCA6, "Save Y", align=Align.INLINE)
d.comment(0xBCBC, "Restore Y", align=Align.INLINE)
d.comment(0xBCE8, "Restore Y", align=Align.INLINE)
d.comment(0xBCE9, "Restore X", align=Align.INLINE)
d.comment(0x9EEF, "Save X (channel index) across the OSARGS body", align=Align.INLINE)
d.comment(0x9EFF, "Restore X", align=Align.INLINE)
d.comment(0x9F85, "Load channel handle from fs_block_offset", align=Align.INLINE)
d.comment(0x9F87, "Convert handle to FCB channel index in X", align=Align.INLINE)
d.comment(0x9F8A, "Test high transfer-size byte first", align=Align.INLINE)
d.comment(0x9F8D, "Non-zero: pointer below extent, send request", align=Align.INLINE)
d.comment(0x9F8F, "Compare FCB pointer high byte...", align=Align.INLINE)
d.comment(0x9F92, "...against extent high byte", align=Align.INLINE)
d.comment(0x9F95, "Pointer < extent: send request", align=Align.INLINE)
d.comment(0x9F97, "Pointer > extent: clamp path", align=Align.INLINE)
d.comment(0x9F99, "Compare FCB pointer mid byte...", align=Align.INLINE)
d.comment(0x9F9C, "...against extent mid byte", align=Align.INLINE)
d.comment(0x9F9F, "Pointer < extent: send request", align=Align.INLINE)
d.comment(0x9FA1, "Pointer > extent: clamp path", align=Align.INLINE)
d.comment(0x9FA3, "Compare FCB pointer low byte...", align=Align.INLINE)
d.comment(0x9FA6, "...against extent low byte", align=Align.INLINE)
d.comment(0x9FA9, "Pointer < extent: send request", align=Align.INLINE)
d.comment(0x9FAB, "X=0: pointer at/beyond extent", align=Align.INLINE)
d.comment(0x9FAD, "Branch to store result (always)", align=Align.INLINE)
d.comment(0xA202, "Save X (channel index)", align=Align.INLINE)
d.comment(0xA215, "Restore Y (channel index)", align=Align.INLINE)
d.comment(0xA21B, "Copy FCB pointer low byte...", align=Align.INLINE)
d.comment(0xA21E, "...into TX control block size low", align=Align.INLINE)
d.comment(0xA221, "Copy FCB pointer mid byte...", align=Align.INLINE)
d.comment(0xA224, "...into TX control block size mid", align=Align.INLINE)
d.comment(0xA227, "Copy FCB pointer high byte...", align=Align.INLINE)
d.comment(0xA22A, "...into TX control block size high", align=Align.INLINE)
import sys

# --- character-literal immediate operands ---
d.char_literal(0x8C1A)
d.char_literal(0x8C5E)
d.char_literal(0x8C90)
d.char_literal(0x8DFB)
d.char_literal(0x8E4A)
d.char_literal(0x90E8)
d.char_literal(0x921A)
d.char_literal(0x921E)
d.char_literal(0x9251)
d.char_literal(0x9267)
d.char_literal(0x92C0)
d.char_literal(0x92CC)
d.char_literal(0x92D0)
d.char_literal(0x92D4)
d.char_literal(0x92D8)
d.char_literal(0x92FC)
d.char_literal(0x9300)
d.char_literal(0x9341)
d.char_literal(0x93A0)
d.char_literal(0x93A4)
d.char_literal(0x93A8)
d.char_literal(0x93AC)
d.char_literal(0x944F)
d.char_literal(0x947F)
d.char_literal(0x9491)
d.char_literal(0x9498)
d.char_literal(0x94A5)
d.char_literal(0x94AF)
d.char_literal(0x94F0)
d.char_literal(0x94FF)
d.char_literal(0x951A)
d.char_literal(0x9525)
d.char_literal(0x9531)
d.char_literal(0x9540)
d.char_literal(0x9931)
d.char_literal(0x9935)
d.char_literal(0x99B9)
d.char_literal(0x9A39)
d.char_literal(0x9A4C)
d.char_literal(0x9A5E)
d.char_literal(0x9A8A)
d.char_literal(0x9D59)
d.char_literal(0x9E8A)
d.char_literal(0x9E94)
d.char_literal(0x9EBD)
d.char_literal(0x9EC4)
d.char_literal(0xA421)
d.char_literal(0xA43C)
d.char_literal(0xA491)
d.char_literal(0xA4B9)
d.char_literal(0xA4DF)
d.char_literal(0xA4E3)
d.char_literal(0xA4EA)
d.char_literal(0xA606)
d.char_literal(0xA96A)
d.char_literal(0xA993)
d.char_literal(0xB266)
d.char_literal(0xB279)
d.char_literal(0xB29A)
d.char_literal(0xB2A9)
d.char_literal(0xB2B7)
d.char_literal(0xB2BB)
d.char_literal(0xB2DF)
d.char_literal(0xB2E1)
d.char_literal(0xB2E5)
d.char_literal(0xB2F0)
d.char_literal(0xB37F)
d.char_literal(0xB38E)
d.char_literal(0xB393)
d.char_literal(0xB3B5)
d.char_literal(0xB3C2)
d.char_literal(0xB428)
d.char_literal(0xB489)
d.char_literal(0xB50E)
d.char_literal(0xB59A)
d.char_literal(0xB5D7)
d.char_literal(0xB61A)
d.char_literal(0xB69A)
d.char_literal(0xB6EB)
d.char_literal(0xB6EF)
d.char_literal(0xB763)
d.char_literal(0xB76C)
d.char_literal(0xB792)
d.char_literal(0xB7B3)
d.char_literal(0xB7CA)
d.char_literal(0xB7CC)
d.char_literal(0xB7EF)
d.char_literal(0xB83E)
d.char_literal(0xB842)
d.char_literal(0xBE0F)
d.char_literal(0xBE13)
d.char_literal(0xBE6C)
d.char_literal(0xBE88)
d.char_literal(0xBE8C)
d.char_literal(0xBE90)
d.char_literal(0xBED6)
d.char_literal(0xBFDE)
d.char_literal(0xBFE5)


# Semantic names for data-table indexing bases the bootstrap left auto-
# labelled (their bytes shift/overlap code, so interpolation could not carry
# the 4.21 names). Anchors (tx_enable_nmis, load_transfer_params, ...) are
# already named, so these render as semantic aliases.
d.label(0x872D, "tx_ctrl_dispatch_lo")
d.label(0x8DBF, "ps_template_base")
d.label(0xA125, "cmos_attr_table")
d.label(0xABE5, "bridge_err_table")
d.label(0xB538, "ps_print_template")
d.index_base(0x8A1E, "os_spool_flag_table")
d.label(0x0D1C, "net_poll_status")
d.index_base(0xA88A, "osword_pb_ready")
d.label(0xA891, "osword_subcode_dispatch")


# Anchor names for the two indexing bases inside instruction operand bytes.
d.label(0x85C0, "tx_calc_tube_check")
d.label(0x8492, "tube_overflow_restore_acccon")

d.banner(0x863A, title="Immediate-op TX control-frame length table",
         description="Length of the TX control frame per immediate-op control byte (&81 PEEK .. &88 machine-type): PEEK/POKE &0E, JSR/UserProc/OSProc &0A, HALT/CONTINUE &06, machine-type &0A. Indexed by the immediate-op control byte.")
d.label(0x863A, "tx_length_values")
d.byte(0x863A, 8)
d.banner(0x8642, title="Immediate-op TX flags table",
         description="TX flags per immediate-op control byte. Bit 7 (&80) marks a reply-generating operation -- set for PEEK (&81) and machine-type (&88); HALT/CONTINUE &01; POKE/exec &00.")
d.label(0x8642, "tx_flags_values")
d.byte(0x8642, 8)

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
output_filepath = _output_dirpath / "anfs-4.24.asm"
output_filepath.write_text(output, encoding="utf-8")
print(f"Wrote {output_filepath}", file=sys.stderr)
json_filepath = _output_dirpath / "anfs-4.24.json"
json_filepath.write_text(str(ir.render("json")), encoding="utf-8")
print(f"Wrote {json_filepath}", file=sys.stderr)
