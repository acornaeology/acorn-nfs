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

- `context <ver> --summary` — global coverage stats and candidate list
- `context <ver> --sub <name>` — write per-routine context file
- `cfg <ver> --leaves` — list leaf subroutines (no outgoing calls)
- `cfg <ver> --sub <name>` — show callers/callees of a routine
- `extract <ver> <addr> [end]` — assembly listing for a region
- `audit <ver> --sub <name>` — full report including refs and extent

## Coverage snapshots

| Date | Total code items | Inline-commented | % | Subs <50% |
|---|---|---|---|---|
| 2026-04-30 baseline | 6487 | 4770 | 73.5% | 71 |
| 2026-04-30 +leaves  | 6487 | 5014 | 77.3% | 33 |
| 2026-04-30 +depth-1 | 6487 | 5102 | 78.6% | 22 |
| 2026-04-30 +higher  | 6487 | 5420 | 83.6% | 9  |

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

## Working queue

Sorted by `context --summary` output (lowest-density leaves first).
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
