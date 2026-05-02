# ANFS 4.21 (variant 1) — completion punchlist

Tracking the residual work to take the disassembly from "publishable
draft" (where Phase J landed it) to "fully annotated canonical
artefact". Each session updates this file as items move from
**[pending]** to **[in-progress]** to **[done]**, so the work is
interruptible and resumable.

State at the start of this push (2026-05-02 evening, after Phases
A-J, fantasm 0.7.1 bump, and the OSWORD &13 / NETV symbolic table
conversions):

| Metric              | Value           |
|---------------------|-----------------|
| Verify              | byte-identical  |
| Lint                | clean           |
| `comments check`    | zero findings   |
| Inline density      | 88.2 % (6245 / 7080) |
| Subroutines         | 458             |
| Open issues         | 4 (O-1..O-4)    |

## Buckets and priorities

Listed in the order I plan to work them. Each links to a TaskCreate
entry that holds the operational details.

### Bucket 1 — quick wins (Task #17)

Three short stale-annotation issues, each 5-15 minutes.

- [ ] **O-2** -- `svc_1_abs_workspace` at `&8EE9`: verify against live
  dispatch (svc_dispatch idx 16 → &8EE9, decoded earlier in Phase E).
  Either confirm and close, or rename if mis-labelled.
- [ ] **O-3** -- inline comment at `&8A8F` saying "Service 1" while
  byte is `CMP #&24`. Replace or delete.
- [ ] **O-4** -- `dir_op_dispatch` description says `Y=&0E` but byte
  is `&18`. Update description.

### Bucket 2 — `cmd_table_fs` symbolic conversion (Task #18)

The biggest remaining "raw bytes" data table. Four sub-tables of
variable-length entries (name + 1-byte flag + 2-byte address-1).
Lo halves still auto-split as printable-ASCII strings.

- [ ] Parse the four sub-tables into a Python data list with
  (name, flag, target_label) per entry.
- [ ] Replace auto-classified strings/bytes with explicit `byte()`
  declarations covering each entry's flag + address bytes.
- [ ] `expr()` per address pair: `<(target-1)` / `>(target-1)`.
- [ ] Inline comment per entry naming the star command and its
  syntax-template index.
- [ ] Add `entry()` for any dispatch target not yet declared.
- [ ] Audit existing `entry()`s for correctness (Phase E found
  one wrong: `*Net` was at `&8B23` but should have been `&8B39`;
  others may have similar issues).

### Bucket 3 — top-20 routine walk (Task #19)

Add inline annotation to the most-uncommented routines. Goal:
density 88.2 % → ~93 %.

| Sub                           | Uncommented | Status |
|-------------------------------|------------:|--------|
| request_next_wipe             | 45          | [ ]    |
| process_spool_data            | 37          | [ ]    |
| fscv_5_cat                    | 37          | [ ]    |
| copy_ps_data                  | 36          | [ ]    |
| init_bridge_poll              | 21          | [ ]    |
| lang_1_remote_boot            | 20          | [ ]    |
| cmd_run_via_urd               | 19          | [ ]    |
| strip_token_prefix            | 16          | [ ]    |
| init_dump_buffer              | 14          | [ ]    |
| tx_calc_transfer              | 12          | [ ]    |
| service_handler               | 12          | [ ]    |
| osword_setup_handler          | 12          | [ ]    |
| osword_13_set_handles         | 12          | [ ]    |
| select_fs_via_cmd_net_fs      | 11          | [ ]    |
| loop_next_char                | 11          | [ ]    |
| store_ptr_at_ws_y             | 11          | [ ]    |
| err_bad_hex                   | 10          | [ ]    |
| fscv_0_opt_entry              | 10          | [ ]    |
| match_fs_cmd                  | 10          | [ ]    |
| alloc_run_channel             | 10          | [ ]    |

Order: by uncommented count (largest first) within each commit
session. Commit per routine or small cluster. After each, run
verify + lint + `comments check` to make sure no stale comments
were re-introduced.

### Bucket 4 — per-string banners (Task #20)

`fantasm data runs --unannotated` shows ~30 short strings (mostly
13-55 char error / info messages used inline after JSR &9261 /
&928A). They're correctly classified, just lack a `comment()` line
explaining their role.

- [ ] Walk the list, add a one-line `comment(addr, "...")` per
  string, one commit for the batch.

### Bucket 5 — O-1 dispatch trace for `nfs_init_body` (Task #21)

Identify which `svc_dispatch` call site produces `X_final = 22`.
Five callers:

- `&8ADB` (service_handler) — X depends on service-call number
- `&8E49`, `&8E59` — dir_op_dispatch chains
- `&8E63` — fall-through from dir_op_dispatch
- `&8EE6` — OSBYTE chain

For each, work out the (X_caller, Y_caller) ranges that can reach
`X_final = X_caller + Y_caller + 1 = 22`.

- [ ] Tabulate per-caller (X, Y) ranges.
- [ ] Identify which caller can legitimately reach `idx 22`.
- [ ] Document on the `nfs_init_body` description.
- [ ] Remove O-1 from OPEN-ISSUES.md.

If the dispatch trace concludes the body is genuinely dead in
this build (no valid trigger), document that finding instead.

### Bucket 6 — fate of 126-item osbyte_a2 dead-code range (Task #22)

The recovered &9619-&973C region traces as code but has no JSR/JMP
callers anywhere. Three options:

- (a) Annotate per-item with calling conventions guessed from
  context. High effort, low value if dead.
- (b) Revert the `entry()` declarations and re-classify as `byte()`
  with an explanatory `data_banner`. Removes 126 items from the
  uncommented count and accurately reflects the unreached state.
- (c) Hybrid: keep the trace but add a routine-level banner
  marking the region as "reachable only via paths not yet found",
  add brief routine-level descriptions, skip per-item.

Decision pending the O-1 trace outcome — if the dispatch table
genuinely targets these addresses, they're not really dead and
(a) or (c) wins; if O-1 concludes that part of the table is
relics, (b) is the honest call.

### Bucket 7 — selective auto-label rename (Task #23)

91 `cXXXX` / `lXXXX` labels remain. Most are 1-3 instruction
continuation pads — naming them adds noise. A handful sit at
routine-internal junction points (e.g. `c8efe`, `c8a8d`, `c8b5a`,
`c8c46` with multi-instruction tails) where a semantic name would
help. Address opportunistically as adjacent routines are walked
in Bucket 3.

## Heuristic for "done"

I'll call this disassembly *complete* when:

1. Inline density ≥ 95 % (or the residual is documented dead code).
2. All four open issues resolved or marked as accepted unknowns.
3. `cmd_table_fs` symbolic conversion landed.
4. `comments check` clean.
5. Verify + lint clean.

Stop-light dashboard at the bottom of each session update.

## Status summary

| Bucket | Task | State |
|--------|------|-------|
| 1 - O-2/3/4 quick wins        | #17 | pending |
| 2 - cmd_table_fs symbolic     | #18 | pending |
| 3 - top-20 routine walk       | #19 | pending |
| 4 - per-string banners        | #20 | pending |
| 5 - O-1 dispatch trace        | #21 | pending |
| 6 - osbyte_a2 dead-code fate  | #22 | pending |
| 7 - selective auto-rename     | #23 | pending |

## Session log

### 2026-05-02 (set-up)

- Created this punchlist.
- Created TaskCreate entries #16-#23 for the seven buckets.
- Confirmed start-of-push state: 88.2 % density / 458 subs / verify
  byte-identical / lint and comments-check both clean.
