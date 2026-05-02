# ANFS 4.21 (variant 1) — Inline Annotation Progress

Tracking the bottom-up annotation pass that adds domain-meaning inline
comments (not mechanical descriptions) to every code item, and complete
calling-convention comments to every subroutine.

## Method

1. **Bottom-up via call graph.** Pick a leaf (depth 0) or near-leaf with
   low inline-comment density. Annotate it. Move to its callers.
2. **Domain meaning, not mnemonic.** `LDA #&0D` should be commented as
   "Load CR (newline) for OSASCI" not "Load &0D into A".
3. **Verify + lint after each routine.** Catch broken refs early.
4. **Commit per routine** (or per small cluster of related routines).
5. **Update this file** with each session's progress. Stay
   resumable.

## Tooling

- `fantasm audit summary <ver>` — global stats and per-sub flags
- `fantasm audit detail <ver> <name>` — full report on a routine
- `fantasm cfg leaves <ver>` — list leaf subroutines (no outgoing calls)
- `fantasm cfg sub <ver> <name>` — show callers/callees of a routine
- `fantasm asm extract <ver> <addr> [end]` — assembly listing for a region

## Coverage snapshots

| Date | Total code items | Inline-commented | % | Subs <50% |
|---|---|---|---|---|
| 2026-04-30 baseline | 6487 | 4770 | 73.5% | 71 |
| 2026-04-30 +leaves  | 6487 | 5014 | 77.3% | 33 |
| 2026-04-30 +depth-1 | 6487 | 5102 | 78.6% | 22 |
| 2026-04-30 +higher  | 6487 | 5420 | 83.6% | 9  |
| 2026-04-30 +large   | 6487 | 5642 | 87.0% | 6  |
| 2026-04-30 +deepest | 6487 | 5899 | 90.9% | 1  |
| 2026-05-01 Phase E+G | 6633 | 5988 | 90.3% | -  |
| 2026-05-02 Phase B   | 6633 | 5984 | 90.2% | -  |
| 2026-05-02 Phase C+G | 6657 | 6081 | 91.3% | -  |

Subroutine count: 403 (was 320 at the start of 2026-05-02). The
inline-comment percentage is broadly unchanged because Phase B
promotes existing labels rather than adding new code; the small
0.1% drift comes from a couple of stale carry-overs being trimmed
in the cross-version sweep.

## Routines fully annotated this session

Bottom-up leaves first, then their callees-already-commented neighbours.

  &8B45 svc_18_fs_select          &8CAD get_ws_page (completion)
  &8EC9 osbyte_x0                 &8ED2 osbyte_x0_y0 (already done)
  &939A is_decimal_digit          &93A2 is_dec_digit_only
  &93AB get_access_bits           &93B5 get_prot_bits + begin_prot_encode
  &93D3 set_text_and_xfer_ptr     &93D7 set_xfer_params
  &93DD set_options_ptr + clear_escapable
  &93E6 cmp_5byte_handle
  &978A save_net_tx_cb            &978B save_net_tx_cb_vset (+shared body)
  &98BE wait_net_tx_ack
  &A3E7 get_pb_ptr_as_index
  &AD15 push_osword_handler_addr
  &ADB8 match_rx_code
  &ADFE init_ws_copy_wide         &AE07 init_ws_copy_narrow
  &AE0B ws_copy_vclr_entry (shared body)
  &B21A print_10_chars + print_chars_from_buf
  &B22A parse_cmd_arg_y0          &B251 strip_token_prefix
  &B29F copy_arg_to_buf_x0        &B2A1 copy_arg_to_buf
  &B2A3 copy_arg_validated
  &B2CF mask_owner_access
  &B3D5 copy_ps_data_y1c          &B4A8 load_ps_server_addr
  &B51C write_ps_slot_byte_ff     &B523 write_two_bytes_inc_y
  &B52B reverse_ps_name_to_tx
  &B7CB prompt_yn
  &BF71 close_ws_file
  &BFBA advance_x_by_8 / _4 / inx4

Depth-1 routines:
  &93F7 set_conn_active           &940D clear_conn_active
  &9421 shared exit c9421
  &97B7 prep_send_tx_cb
  &B22F parse_access_prefix       &B22C parse_filename_arg
  &B2E4 ex_print_col_sep (partial)
  &B483 print_file_server_is      &B48D print_printer_server_is
  &B498 print_server_is_suffix
  &B556 print_station_addr
  &BE37 print_hex_and_space

Depth-2/3:
  &8C93 print_version_header (completion)
  &A3BB print_fs_info_newline

Higher-level routines (depth 1-7+):
  &8028 svc5_irq_check (completion)
  &92B2 parse_addr_arg (full body)
  &9776 cmd_bye             &A398 cmd_fs
  &A3C4 parse_fs_ps_args (full body, was just declaration)
  &AD40 tx_econet_abort     &AD64 netv_claim_release
  &ADD3 osword_8_handler
  &B303 print_decimal_3dig_no_spool + &B310 _digit_no_spool (NEW
        4.21 routines named & annotated)
  &BE01 print_dump_header   &BE42 parse_dump_range
  &BF78 open_file_for_read

Large/depth-3+ routines:
  &AD64 netv_claim_release  &ADD3 osword_8_handler
  &B3D7 copy_ps_data        &B6F3 cmd_wipe (body up to prompt)
  &BD41 cmd_dump            &BEAB init_dump_buffer
  &A3E9 byte_to_2bit_index (entry + handle helper alt entries)
  &A3FF net_1_read_handle / net_2_read_handle_entry
  &A415 net_3_close_handle
  &A424 mark_ws_uninit
  &B4B4 pop_requeue_ps_scan
  &9900 cond_save_error_code + error-build chain
        (build_no_reply_error / classify_reply_error /
         build_simple_error / fixup_reply_status_a)
  &AFA6 send_disconnect_reply
  &97CD recv_and_process_reply (the FS reply dispatch core)

## Outstanding

  &B3D7 copy_ps_data (49% — at threshold, not strictly below 50%
        but the surrounding routines have stale comments mixing
        printer-server and cmd_wipe carry-overs that need a careful
        cleanup pass)


# Comprehensive remaining work plan (post-audit, 2026-04-30)

The simple "add inline comments" pass is mostly done (90.9% coverage).
But the audit reveals significant remaining work across multiple
dimensions. In priority order:

## Phase A: Subroutine calling conventions (highest impact)

  Coverage history (318 subroutines):

    | Date              | on_entry | on_exit | Both |
    |-------------------|----------|---------|------|
    | baseline          |   31.4%  |  16.4%  |  ?   |
    | 2026-04-30 (mid)  |   54.1%  |  41.8%  | 33.0%|
    | 2026-04-30 (late) |   84.0%  |  63.2%  | 62.9%|
    | 2026-04-30 (end)  |   98.1%* |  77.0%  | 76.7%|

  *True on_entry coverage is 100% modulo the intentional
  fs_vector_table DATA_ONLY entry. The Python scan reports six
  routines as missing on_entry (print_inline, print_inline_no_spool,
  error_inline, error_inline_log, error_bad_inline, plus
  fs_vector_table) but the five inline-string utilities all DO
  have on_entry -- the scan cannot read past triple-quoted (`"""\\`)
  description bodies, so it generates a false negative for them.
  Phase A is effectively complete.

  Every subroutine should document:

    - Registers it expects on entry (A, X, Y)
    - Flags it expects on entry (C, V mostly)
    - Registers it returns on exit
    - Flags it returns
    - Any side effects (workspace bytes touched, stack consumed, etc.)

  Approach: walk the subroutine list ordered by call-graph depth (so
  that callers' conventions follow from callees'). For each, read the
  body, identify the calling conventions, fill in `on_entry` and
  `on_exit`. **Phase A is complete** (modulo `fs_vector_table` which
  is intentionally DATA_ONLY).

  Same body cross-version note: a spot-check of nmi_rx_scout in 4.18
  vs 4.21 shows the bodies are byte-for-byte equivalent except where
  4.21 reads the saved `tx_src_stn` copy at &0D22 instead of &FE18
  directly (a Master 128 specific change). 4.18 doesn't yet have
  on_entry/on_exit on its NMI handlers; the calling-convention text
  written for 4.21 should port over with minimal edits if a future
  pass back-fills 4.18.

  Done so far this session (17 Phase-A commits + 2 progress
  checkpoints):

    - tx_done dispatch family (5 subs): tx_done_jsr, _econet_event,
      _os_proc, _halt, _continue plus advance_rx_buffer_ptr,
      release_tube, advance_buffer_ptr.
    - print/text-pointer/spool helpers (10 subs): save_text_ptr,
      get_ws_page, print_newline_no_spool, get_access_bits,
      cmp_5byte_handle, init_txcb_bye, init_txcb,
      send_request_nowrite, send_request_write, save_ptr_to_os_text,
      skip_to_next_arg, save_ptr_to_spool_buf, init_spool_drive,
      load_ps_server_addr, write_ps_slot_byte_ff,
      reverse_ps_name_to_tx, flush_and_read_char, abort_if_escape,
      prompt_yn.
    - Service / FS-init helpers (10 subs): scan_remote_keys,
      help_wrap_if_serial, setup_ws_ptr, notify_new_fs,
      clear_if_station_match, init_adlc_and_vectors,
      restore_fs_context, check_not_ampersand, copy_fs_cmd_name,
      parse_quoted_arg.
    - FS messaging core (6 subs): cmd_bye, save_net_tx_cb,
      save_net_tx_cb_vset, prep_send_tx_cb, recv_and_process_reply,
      wait_net_tx_ack.
    - Parse/copy/print/inx helpers (11 subs): parse_cmd_arg_y0,
      parse_filename_arg, strip_token_prefix, copy_arg_to_buf_x0,
      copy_arg_to_buf, print_file_server_is, print_printer_server_is,
      print_station_addr, advance_x_by_8, advance_x_by_4, inx4.
    - cmd_* handlers (10 subs): cmd_net_fs, cmd_roff,
      cmd_fs_operation, cmd_dir, cmd_iam, cmd_pass, cmd_rename,
      parse_fs_ps_args, print_fs_info_newline.
    - OSWORD &13 sub-handlers (19 subs): read/set_station, read/
      write_csd, read/write_ws_pair, read/write_prot, read/set_handles,
      read_rx_flag, read_rx_port, read_error, read_context,
      read_free_bufs, read/write_ctx_3, bridge_query, plus
      store_osword_pb_ptr.
    - NETV / Tube / station-table (13 subs): recv_reply_preserve_flags,
      tube_claim_c3, find_station_bit2, find_station_bit3,
      flip_set_station_boot, enable_irq_and_poll, netv_handler,
      push_osword_handler_addr, tx_econet_abort, osword_8_handler,
      init_ws_copy_wide, init_ws_copy_narrow, ws_copy_vclr_entry.

  Side fixes found and committed:

  - strip_token_prefix's description said "&0E30 buffer" (4.18
    location); body actually operates on lc030 = &C030. Updated.
  - parse_access_prefix's description referenced &0E30 / l1071;
    body operates on &C030 / fs_lib_flags (&C271). Updated.

  There are likely more such carry-over comments to clean up in
  Phase F (general stale-comment cleanup).

  Continued in this session (8 more commits, ~120 more subs):

    - TX retry path / gsread / FS-options helpers (11 subs):
      init_tx_ptr_and_send, send_net_packet, poll_adlc_tx_status,
      load_text_ptr_and_parse, gsread_to_buf, print_load_exec_addrs,
      copy_fsopts_to_zp, skip_one_and_advance5,
      copy_workspace_to_fsopts, ensure_fs_selected, match_fs_cmd.
    - FCB allocation / channel-and-dir checks / *Dump (12 subs):
      init_channel_table, store_result_check_dir, check_not_dir,
      alloc_fcb_or_error, scan_fcb_flags, find_open_fcb,
      restore_catalog_entry, print_dump_header, close_ws_file,
      open_file_for_read, parse_dump_range, init_dump_buffer.
    - parse helpers / PS templates / service handlers / *HELP
      (15 subs): commit_state_byte, serialise_palette_entry,
      read_osbyte_to_ws_x0, read_osbyte_to_ws, parse_access_prefix,
      mask_owner_access, ex_print_col_sep, copy_ps_data_y1c,
      copy_ps_data, init_ps_slot_from_rx, pop_requeue_ps_scan,
      help_net, help_utils, svc_3_autoboot, svc_8_osword,
      svc_9_help, select_fs_via_cmd_net_fs.
    - FS multi-step / OSGBPB / NETV-spool / bridge (19 subs):
      init_tx_ptr_for_pass, setup_pass_txbuf, do_fs_cmd_iteration,
      send_txcb_swap_addrs, check_and_setup_txcb,
      format_filename_field, update_addr_from_offset9,
      lookup_cat_entry_0, setup_transfer_workspace, write_data_block,
      get_pb_ptr_as_index, init_bridge_poll, netv_claim_release,
      netv_spool_check, netv_print_data, reset_spool_buf_state,
      handle_spool_ctrl_byte, process_spool_data,
      send_disconnect_reply.
    - gap-fill on previously-on_exit-only subs + OSWORD &13 reads
      (22 subs): scan_remote_keys, notify_new_fs,
      print_newline_no_spool, init_txcb_bye, tube_claim_c3,
      parse_cmd_arg_y0, print_file_server_is,
      print_printer_server_is, prompt_yn, flush_and_read_char,
      alloc_fcb_slot, init_wipe_counters, find_matching_fcb,
      reset_spool_buf_state, copy_ps_data_y1c, plus OSWORD &13
      read_csd, read_ws_pair, read_prot, read_handles, read_rx_flag,
      read_rx_port, read_error, read_context, read_free_bufs,
      read_ctx_3, bridge_query.
    - misc service-tier (5 subs): print_version_header,
      check_credits_easter_egg, fscv_6_shutdown, verify_ws_checksum,
      print_station_id.
    - ADLC init / reset / RX-listen + rom_set_nmi_vector (7 subs):
      adlc_init, init_nmi_workspace, adlc_full_reset, adlc_rx_listen,
      wait_idle_and_reset, save_econet_state, rom_set_nmi_vector.
    - NMI dispatch RX-scout / data-RX chain (16 subs): nmi_rx_scout,
      nmi_rx_scout_net, scout_error, scout_complete, nmi_data_rx,
      install_data_rx_handler, nmi_error_dispatch, nmi_data_rx_bulk,
      data_rx_complete, ack_tx, nmi_ack_tx_src, post_ack_scout,
      nmi_post_ack_dispatch, rx_complete_update_rxcb,
      discard_reset_listen, copy_scout_to_buffer.
    - NMI dispatch TX path + immediate-op chain (29 subs):
      immediate_op, rx_imm_exec, rx_imm_poke, rx_imm_machine_type,
      rx_imm_peek, advance_buffer_ptr, imm_op_build_reply, tx_begin,
      inactive_poll, intoff_test_inactive, tx_line_jammed, tx_prepare,
      tx_ctrl_peek, tx_ctrl_poke, tx_ctrl_proc, nmi_tx_data,
      tx_last_data, nmi_tx_complete, nmi_reply_scout, nmi_reply_cont,
      nmi_reply_validate, nmi_scout_ack_src, nmi_data_tx,
      handshake_await_ack, nmi_final_ack, nmi_final_ack_validate,
      tx_result_ok, tx_result_fail, nmi_bootstrap_entry.

  All NMI dispatch entries document the shared shim contract:
  BIT &FE18 (INTOFF) / PHA / TYA / PHA / ROMSEL switched to NFS
  bank, A and Y already saved on stack on entry, X is NOT saved
  by the shim, NMI flip-flop disabled. Exit paths are documented
  as "next NMI handler installed at &0D0C/&0D0D, control returns
  via nmi_rti" rather than the RTS/RTI confusion that calling-
  conventions tooling tends to assume.

## Phase B: Unidentified subroutine boundaries

  **Done (2026-05-02).** Sweep completed using `fantasm promote`,
  which scores labelled code items by inbound-ref count, JSR-call
  count, and AfterTerm flag. Outcome:

  - **62 JSR-targeted candidates** (any label with at least one
    `JSR site`) all promoted. Includes error helpers, exit
    epilogues, dispatch trampolines, parser loop bodies, and *DUMP /
    *Wipe tails. See commits `8833173` … `0d644d2`.

  - **32 entry()-only candidates** (declared as code but reached
    only via vectors / NMI vector indirection / PHA/PHA/RTS) all
    promoted. Includes the FILEV / ARGSV / GBPBV / BGETV / BPUTV
    handlers, FSCV reasons 0/1/2/5/7, FS reply handlers, language-
    reply handlers, OSWORD &10/&12/&14 handlers, NMI-vector
    continuations (data_rx_setup, nmi_data_rx_net, nmi_data_rx_skip,
    nmi_data_rx_tube, nmi_data_tx_tube, nmi_final_ack_net), the svc
    table[2] target at &8D09, and the small send_osbput_data
    helper. See commits `d10a4dd` and `a8dd8e9`.

  - **803 JSR=0 promote candidates** assessed and ruled out:
    - 0 are reached via JMP.
    - 9 are reached via BRA (all are within the same enclosing
      routine — internal continuation labels).
    - The rest only by conditional branches.
    None are subroutines.

  - **9 entry()-only addresses left as labels** (not subroutines):
    `&804F`, `&80E8`, `&8360`, `&84BE` (`set_rx_buf_len_hi`),
    `&870D` (`tx_error`), `&88F0` (dead data block), `&8968`
    (`fallback_calc_transfer`), `&8EFE`, `&9E7F`
    (`done_osword_op`). Each is a branch landing pad / fall-through
    entry / single-RTS sentinel / dead data; none are callable
    subroutines.

  Subroutine count: 403 (up from 320 at session start).

## Phase C: Recover remaining UNMAPPED 4.18 routines

  From `git log` and grep of UNMAPPED subroutine() blocks: the
  carry-over still has unrecovered routines whose 4.18 names are
  known. Use `fantasm.api.fingerprint` and the JSR-following
  technique.

  Done:

    - svc_2_private_workspace -- split into
      svc_2_private_workspace_pages (&8F10) +
      nfs_init_body (&8F38).
    - tx_done_jsr (&8540).
    - tx_ctrl_machine_type (&8686).
    - tx_calc_transfer (&8900).
    - check_escape -- split into check_urd_prefix (&8E2D) +
      raise_escape_error (&9895). The 4.18 single-routine version
      bundled the BIT-test prologue with the action; 4.21
      separates them.
    - osword_13_set_handles (&AAD0).
    - osword_13_read_handles (&AAC2).

  Done (2026-05-02):

    - cmd_prot at &B6D2 (with cmd_unprot at &B6D6 sharing body):
      Master 128 stores protection in CMOS bit 6 of byte &11; no
      keyword arguments any more, the wrapper just toggles the bit.
    - osword_4_handler at &AD32: reached via OSWORD dispatch
      table; clears caller's C, stores Y to nfs_workspace+&DA,
      falls into tx_econet_abort.

  Confirmed REMOVED in 4.21 (no equivalent code exists):

    - cmd_close, cmd_print, cmd_type -- Master MOS provides these
      as built-ins, so the NFS ROM no longer wraps them.
    - read_paged_rom -- no JMP osrdsc (`4C B9 FF`) anywhere.
    - set_jsr_protection -- svc5_irq_check rewritten around the
      Master deferred-work flag at &0D65; the JSR-protection
      mechanism is gone. The shared SR-shadow-update body lives
      at setup_sr_tx (&8512) for unrelated TX-prep work.

  Removals captured in CHANGES-FROM-4.18-NOTES.md.

  **Phase C complete.**

## Phase D: Data classification review

  481 EQUB / 14 EQUW / 147 EQUS / 0 EQUD lines emitted. Audit:

  Long EQUB runs (top candidates for re-classification):
    &AE33: 39 EQUBs   ws_txcb_template_data (template byte stream)
    &B0D5: 28 EQUBs   CDir allocation size threshold table
    &ADC1: 18 EQUBs   osword_claim_codes (one byte per claim type)
    &88F0: 16 EQUBs   dead data after rom_set_nmi_vector
    &91ED: 12 EQUBs   cmd_syntax_table (12-entry index table)
    &9A9A: 12 EQUBs   net_error_lookup_data
    &9B75: 12 EQUBs   ?
    &B002: 12 EQUBs   tx_econet_txcb_template
    &B00E: 12 EQUBs   rx_palette_txcb_template
    &B575: 12 EQUBs   ps_slot_txcb_template
    &93C8: 11 EQUBs   prot_bit_encode_table

  For each: confirm the byte-vs-word-vs-string classification matches
  the actual access pattern. Tables of addresses should be EQUW.
  Tables that hold paired (lo, hi) bytes for PHA/PHA/RTS dispatch
  should ideally be split as `equb <(target_label)` / `equb >(target_
  label)` so renames flow through.

  Also: every EQUB / EQUW / EQUS line should have a comment explaining
  its role in domain terms, not just `; data byte`.

## Phase E: Address tables -> symbolic via <() / >()

  Where a 2-byte address appears as raw `equw &XXXX` or as paired
  `equb &lo / equb &hi`, replace with `equw label` or
  `equb <(label) / equb >(label)`. Beebasm's `<()` and `>()` operators
  extract low / high bytes symbolically, so renames or relocations
  flow through cleanly.

  Audit: search for every `equw &[0-9A-F]{4}` and every adjacent
  pair of `equb` whose values match a known label.

  Done: imm_op_dispatch_lo at &848B (PEEK/POKE/JSR/HALT/CONT/MachineType
  for ctrl bytes &81-&88); tx_done_dispatch_lo at &853B (5 entries for
  TX op types &83-&87, dispatcher reads via expr_label `tx_done_
  dispatch_lo-&83` at &84B8); tx_ctrl_dispatch_lo at &867E (8 entries
  for TX ctrl bytes &81-&88, operand &85FD lands mid-instruction
  inside intoff_test_inactive). The latter required moving
  tx_ctrl_machine_type from the 4.18 carry-over &8689 to the 4.21
  &8686 (-3 byte shift). Remaining: svc_dispatch lo/hi pair at
  &89ED/&8A20 (blocked by O-1), star-command dispatch tables, plus
  smaller `equw` candidates.

## Phase F: Stale UNMAPPED comment cleanup

  **Substantially done (2026-05-02).** Four passes:

  - **Pass 1 (-733 lines):** wholesale `sed '/# UNMAPPED (dead range/d'`
    -- the 733 stubs at &0016-&0057 / &0400-&06FF, all from 4.18's
    relocated workspace which 4.21 doesn't have.
  - **Pass 2 (-854 lines):** wholesale `sed '/^# UNMAPPED:/d' +
    '/^# UNMAPPED (broken ref):/d'` -- the active-range carry-over
    stubs at 4.21 addresses where the 4.18 annotation no longer
    fits (477 stale comment(), 142 label(), 6 subroutine(), 13
    byte(), 11 expr(), 10 entry(), 4 string(), 1 word(), 10 broken-
    ref expr(), plus 6 orphan-body lines).
  - **Pass 3 (43 reg_value findings -> 0):** `fantasm comments
    check` flagged 43 inline comments whose register-value text no
    longer matched the 4.21 instruction at the same address (this
    was the main "impeding progress" issue -- stale comments at
    duplicate-comment addresses concatenating with new ones in
    the asm output). Most were deleted; a few were value-updated
    (e.g. `X=&4A` -> `X=&35` for the moved cmd-table offset,
    `Y=&10: page &10` -> `Y=&C2: high byte of lc2c2 (FCB context
    buffer)` for the sideways-RAM workspace migration).
  - **Pass 4 (chain + most stale_addr):** trivial chain_comment
    findings ("Second INX" -> "(continued)") and 10 of the 15
    stale_addr findings (NMI-handler install sites referencing
    moved addresses, e.g. `&87EE` -> `&86E7`).

  **State at end:** `fantasm comments check` reports 49 MEDIUM-
  confidence findings remaining: 38 desc_stale_addr, 6
  block_stale_addr, 5 stale_addr. These are mostly false-positives:
  workspace bytes that aren't declared as items (&0D5D, &0D3A,
  &0D48, &0D4A, &0D74), the mid-instruction operands of the
  expr_label dispatchers I introduced (&84B8, &85FD), and label-
  only addresses (ps_template_base &8DA7) that are valid but don't
  appear in the JSON item map. Genuine remaining staleness is in
  ~15 subroutine() descriptions that reference 4.18 addresses --
  worth fixing piecemeal but no longer impeding progress.

  Driver shrank from ~17085 to ~15500 lines (~10% smaller). HIGH-
  confidence comment-vs-code findings: 0.

## Phase G: Last 9.1% inline-comment coverage

  Currently 5899 / 6487. The remainder lives in routines that
  haven't been walked end-to-end (typically partial-coverage subs)
  or in data tables that need EQUB-by-EQUB comments (Phase D).

  Mostly falls out of phases D and E above; final sweep at the end
  to mop up isolated gaps.

## Phase H: Audit pass against the audit-tool flag categories

  Walk each flag category from `fantasm audit summary`, validating
  that the flag is correct (or fixing the routine if not):

    BRANCH_ESCAPE (91): a branch targets outside the routine extent.
      Often correct (shared exits, fall-through targets) but worth
      verifying each.
    NO_REFS (59): no incoming refs found. Likely PHA/PHA/RTS
      dispatch or dead code. Each should have a description that
      explains how it's reached.
    FALL_THROUGH (131): last item isn't a clean exit. Fine if the
      next subroutine is the documented fall-through target.
    FALL_THROUGH_ENTRY (27): only reachable via fall-through.
      Check description explicitly mentions this.
    DATA_ONLY (1): fs_vector_table -- intentional, leave alone.

## Phase I: rom.json links

  Once the CHANGES doc is drafted (Phase J), populate
  `address_links` and `glossary_links` in `rom/rom.json` so the
  website can render cross-references. Lint validates these.

## Phase J: CHANGES-FROM-4.18.md

  The publishable deliverable. Only after phases A through H above
  are at >= 95% coverage on the relevant dimension and the audit is
  clean. Synthesises everything from `PROGRESS.md`,
  `docs/analysis/anfs-421-variant-naming.md`, the per-routine commit
  messages, and the audit findings into a structured changes
  document following the established 4.18 example.

## Working queue

Sorted by `fantasm audit summary` output (lowest-density leaves first).
Strike through as completed.

### Leaves (no outgoing calls)

| Addr | Name | Items | %inline | Status |
|---|---|---|---|---|
| &8B45 | svc_18_fs_select | 4 | 0% | |
| &8CAD | get_ws_page | 11 | 27% | |
| &8EC9 | osbyte_x0 | 1 | 0% | |
| &939A | is_decimal_digit | 4 | 0% | |
| &93A2 | is_dec_digit_only | 6 | 0% | |
| &93AB | get_access_bits | 5 | 20% | |
| &93B5 | get_prot_bits | 10 | 0% | |
| &93D3 | set_text_and_xfer_ptr | 2 | 0% | |
| &93D7 | set_xfer_params | 3 | 0% | |
| &93DD | set_options_ptr | 6 | 0% | |
| &93E6 | cmp_5byte_handle | 10 | 0% | |
| &978A | save_net_tx_cb | 1 | 0% | |
| &978B | save_net_tx_cb_vset | 19 | 5% | |
| &98BE | wait_net_tx_ack | 34 | 3% | |
| &A3E7 | get_pb_ptr_as_index | 1 | 0% | |
| &AD15 | push_osword_handler_addr | 6 | 0% | |
| &ADB8 | match_rx_code | 5 | 20% | |
| &ADFE | init_ws_copy_wide | 4 | 0% | |
| &AE07 | init_ws_copy_narrow | 2 | 0% | |
| &AE0B | ws_copy_vclr_entry | 22 | 23% | |
| &B21A | print_10_chars | 1 | 0% | |
| &B22A | parse_cmd_arg_y0 | 1 | 0% | |
| &B251 | strip_token_prefix | 36 | 0% | |
| &B29F | copy_arg_to_buf_x0 | 1 | 0% | |
| ... | (more from context output) | | | |

### Higher-order routines

To populate as we finish leaves and walk callers.

## Findings

(Notable observations to fold into the eventual CHANGES doc; see also
`PROGRESS.md` for cross-version findings.)
