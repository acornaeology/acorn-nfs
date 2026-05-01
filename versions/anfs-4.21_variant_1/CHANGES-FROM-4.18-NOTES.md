# ANFS 4.21 (variant 1) vs ANFS 4.18 — working notes

Note-form draft. To be reorganised into a proper `CHANGES-FROM-4.18.md`
later (see the in-tree examples under `versions/*/CHANGES-FROM-*.md`).
Capturing observations as they fall out of the disassembly work, so
the 4.21 driver itself can be cleaned of cross-version chatter.

ANFS 4.21 variant 1 is the first Master 128 ANFS. It is 65C02-aware,
drops the page 4-6 relocated workspace in favour of sideways-RAM at
&C000-&C2FF, and has a ROM-header Bad-ROM gate that rejects all
non-Master OS versions. Opcode similarity to 4.18 is 85.6%.

---

## ROM-level changes

- **CPU:** 65C02 (Master 128). Driver loads with `load(addr, file, "65c02")`;
  beebasm `CPU 1`. 65C12 instruction adoption visible in many prologues:
  PHX/PHY/PLX/PLY, BRA, STZ, TSB/TRB, BIT abs,X.
- **No relocated-block copy code.** 4.18 had the page 4-6 copy loop
  around &BE94; 4.21 has nothing in that area.
- **Master-only Bad ROM gate** at the service handler at &8A54:
  OS-version check via OSBYTE 0; rejects OS 1.00, OS 1.20, OS 2.00,
  OS 5.0 (Master Compact). Hence "variant 1" naming.
- **ACCCON save/restore** brackets the NMI data-copy paths (Master
  shadow-RAM access).
- **Service entry** is at &8A54 (was &8A15 in 4.18).
- **Workspace migration:** MOS RAM pages &0Dxx-&10xx in 4.18 become
  sideways-RAM at &C000-&C2FF. Concretely:
  - 4.18 `&0E30` parse buffer -> 4.21 `&C030` (lc030).
  - 4.18 `&0F00` TX buffer base -> 4.21 `&C100` (lc100, lc103, lc105...).
  - 4.18 `&1071` fs_lib_flags -> 4.21 `&C271` (lc271).
  - 4.18 `&10D9` saved-catalog buffer -> 4.21 `&C2D9` (lc2d9).
  - 4.18 `&10C9` FCB attribute reference -> 4.21 `&C2C9` etc.

## Behavioural changes

### OSWORD &13 auto-select FS
4.21's OSWORD &13 sub-handlers all begin with a JSR ensure_fs_selected
prologue (&8B4D). Tests bit 7 of fs_flags (&0D6C); if clear, calls
cmd_net_fs to AUTO-SELECT ANFS. On failure, raises 'net checksum'
(error &AA). 4.18 inlined `BIT &0D6C / BPL <return>` and ABORTED
(returning zero in PB[0]) when FS was inactive. This is the most
visible behaviour change for client code that uses OSWORD &13.

### svc5_irq_check rewritten (&8028)
Body differs significantly. 4.18 checked VIA IFR bit 2 for
shift-register completion. 4.21 reads the workspace byte at &0D65
(a deferred-completion flag), generates event &FE via generate_event
on hit and JMPs to &8582 (tx_done_exit) otherwise. Same address as
4.18, completely different mechanism.

### Service handler Bad-ROM gate
At &8A54, the service handler runs an OSBYTE 0 OS-version check
before any of the standard service-call dispatch. Recognised:
- OS 3.x (Master 128) -> proceed
- OS 4.0 (Master Econet Terminal) -> proceed
- everything else -> silently skip the call (return unclaimed).

4.18 had no equivalent gate — the service handler dispatched
directly.

### *RUN argument with '&' prefix is URD-relative
The cmd_run handler in 4.21 splits into two entries:
- `check_urd_prefix` at &8E2D — tests first arg char for '&'
- `cmd_run_via_urd` at &8E35 / &A4F1 — the URD-prefixed entry

If the first arg char is '&', JMPs to cmd_run_via_urd which clears
fs_lib_flags bit 1 before parsing the rest. Otherwise falls through
to pass_send_cmd for normal FS-command dispatch.

### check_escape split
4.18's check_escape (&9570) bundled the escape-flag BIT-test prologue
and the escape-acknowledge action. 4.21 splits them: each call site
performs its own BIT-test against the FS-options/escapable flag, and
JSRs `raise_escape_error` (&9895) when escape is detected. The action
half emits OSBYTE &7E and tail-jumps to classify_reply_error with A=6.

### setup_sr_tx via shadow VIA pair
4.21's shift-register prep (&8512) reads/writes the workspace shadow
pair `ws_0d68` / `ws_0d69` rather than the real VIA ACR / SR
registers. The shadow is flushed into the live VIA in the Master
IRQ path. 4.18 wrote `system_via_acr` / `system_via_sr` directly.

### read_paged_rom uses LDX &028D directly
4.21 reads &028D (current ROM number) inline rather than via OSBYTE &FD.

### svc_2_private_workspace split
4.18's `svc_2_private_workspace` (around &8EB8) bundled the
workspace-allocation logic and the ANFS bring-up sequence in a
single body. 4.21 splits them: `svc_2_private_workspace_pages`
(&8F10) handles the pages allocation; `nfs_init_body` (&8F38)
contains the bring-up. The latter is reachable only via PHA/PHA/RTS
dispatch in this build (see OPEN-ISSUES O-1).

### dir_op_dispatch Y value
`dir_op_dispatch` at &8E5B sets Y=&18 (was &0E in 4.18). The
reachable indices via this path shift from 15..19 to 25..29.

## Annotation / structural notes

### 65C12 prologue adoption
Many routines that pushed/popped X and Y via TXA/PHA / TYA/PHA
in 4.18 use direct PHX / PHY in 4.21. Examples:
- copy_fs_cmd_name (&9463)
- parse_fs_ps_args (&A3C4)
- help_wrap_if_serial (around &8C29)

### Removed code (vs 4.08.53 carry forward)
4.18 already had these removed; 4.21 inherits the absence:
- loop_copy_osword_flag (the OSWORD copy-back loop)
- return_from_flush_read
- unused_clear_ws_78
- The dead code at 4.18 &B42F is gone in 4.21 too.

### svc_dispatch lo/hi shifts
The PHA/PHA/RTS svc dispatch table moved:
- 4.18 lo half at &89CA -> 4.21 lo half at &89ED
- 4.18 hi half at &89EF -> 4.21 hi half at &8A20

The fs_vector_table moved similarly: 4.18 had it at &8E6F; 4.21 has
it at &8EB5 (= &8E9A + &1B). The +&46 shift comes from the longer
ROM title and the inserted Bad-ROM gate.

### Address-mapping table (recovered routines)

| Routine                       | 4.18      | 4.21      | Notes |
|-------------------------------|-----------|-----------|-------|
| svc5_irq_check                | &8028     | &8028     | rewritten body (see above) |
| tx_done_jsr                   | &8543     | &8540     | -3 byte shift |
| tx_calc_transfer              | &88F2     | &8900     | |
| get_ws_page                   | &8CB9     | &8CAD     | body extends with ROL/PHP/ROR/PLP |
| issue_svc_15                  | &8D17     | &8D24     | |
| osbyte_x0_y0                  | &8E8C     | &8ED2     | same body |
| osbyte_x0                     | &8E83     | &8EC9     | same body |
| osbyte_a2 caller (8D91)       | &8D79     | &8D91     | prologue differs |
| svc_2_private_workspace_pages | &8EB8 (part) | &8F10  | split (see above) |
| nfs_init_body                 | &8EB8 (part) | &8F38  | split (see above) |
| print_station_id              | &8FF1     | &90C7     | |
| copy_fs_cmd_name              | &9327     | &9463     | 65C12 PHY |
| read_filename_char (TX buf)   | &0F05     | &C105     | workspace migrated |
| parse_fs_ps_args              | &A0A7     | &A3C4     | 65C12 PHX/PHY |
| osword_13_read_station        | &A660     | &A9CC     | |
| osword_13_set_station         | &A673     | &A9DA     | FS-active gate factored out |
| osword_13_read_handles        | &A734     | &AAC2     | |
| osword_13_set_handles         | &A744     | &AAD0     | |
| svc_8_osword                  | &A4EE     | &A83B     | |
| ensure_fs_selected            | &8B0D     | &8B45     | |
| mask_owner_access             | &AF32     | &B2CF     | fs_lib_flags moved &1071 -> &C271 |
| process_all_fcbs              | &B799     | &BB38     | rewritten — uses fs_options + fs_block_offset (PROGRESS §5) |
| svc_18_fs_select related path | &AD10     | &B0A0     | |

### Stale 4.18 carry-overs found and fixed during 4.21 work
- `error_bad_command` was labelled at the wrong address (&A592)
  carried over from 4.18; the real body is at &A5A1.
- `svc_1_abs_workspace` 4.18 label at &8EE9 doesn't match the live
  4.21 dispatch; OPEN-ISSUES O-2.
- `dir_op_dispatch` description still said `Y=&0E` (4.18 value)
  while the byte is `&18`; OPEN-ISSUES O-4.
- `osbyte_a1` at &8E9A is dual-use: the 5 bytes `A9 A1 4C F4 FF`
  are the routine's code AND the leading slot of a vector-dispatch
  table read via `LDA c8e9a,Y`. Handled in 4.21 via expr_label.

### Dispatch-table layout shifts
- `tx_done_dispatch_lo` moved from &853E (4.18) to &853B (4.21);
  same 5-entry semantics for op types &83-&87.
- `tx_ctrl_dispatch_lo` moved from &8681 (4.18) to &867E (4.21);
  same 8-entry semantics for ctrl bytes &81-&88.
- `tx_ctrl_machine_type` moved from &8689 (4.18) to &8686 (4.21);
  -3 byte shift matches the dispatch-table move.
- `imm_op_dispatch_lo` moved from &8488 (4.18) to &848B (4.21).
- For each, the dispatcher operand uses an `expr_label` of the form
  `<table_label>-<base_offset>` so renames flow through.

## Open-issue cross-references

- **O-1** (OPEN-ISSUES.md): the dispatch path that reaches
  `nfs_init_body` &8F38 isn't yet pinned down. The table[22] entry
  is real but no JSR/JMP/branch exists for the address.
- **O-2..O-4**: stale 4.18 labels surviving in the dispatch area
  (svc_1_abs_workspace, the 'Service 1' inline comment at &8A8F,
  dir_op_dispatch's Y=&0E description).
