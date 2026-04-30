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
