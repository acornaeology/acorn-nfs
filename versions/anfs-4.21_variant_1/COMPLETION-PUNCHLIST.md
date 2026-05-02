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
| 1 - O-2/3/4 quick wins        | #17 | DONE |
| 2 - cmd_table_fs symbolic     | #18 | DONE |
| 3 - top-20 routine walk       | #19 | DONE |
| 4 - per-string banners        | #20 | DONE |
| 5 - O-1 dispatch trace        | #21 | DONE (arithmetic resolved; MOS trigger open) |
| 6 - osbyte_a2 dead-code fate  | #22 | DONE (it's not dead -- annotated as dispatch targets) |
| 7 - selective auto-rename     | #23 | DONE |

## Final state (2026-05-02 evening, end of long-haul push)

| Metric              | Value           |
|---------------------|-----------------|
| Verify              | byte-identical  |
| Lint                | clean           |
| `comments check`    | zero findings   |
| `data runs --unannotated` | empty     |
| Inline density      | 100.0 % (7087 / 7087) |
| Subroutines         | 459             |
| Open issues         | 1 (O-1's MOS trigger; arithmetic resolved) |

## Session log

### 2026-05-02 (set-up)

- Created this punchlist.
- Created TaskCreate entries #16-#23 for the seven buckets.
- Confirmed start-of-push state: 88.2 % density / 458 subs / verify
  byte-identical / lint and comments-check both clean.

### 2026-05-02 (Buckets 1, 4, 2 landed)

- **Bucket 1 (O-2/3/4):** &8EE9 svc_1_abs_workspace renamed to
  raise_y_to_c8 (matches the &C8 threshold the body actually uses);
  &8A8F inline corrected to "Service call &24 (Econet-present
  query)"; dir_op_dispatch description rewritten for Y=&18 / dispatch
  indices &19..&1D. OPEN-ISSUES updated.
- **Bucket 4 (per-string banners):** ~40 inline strings now have
  `comment(addr, "Inline: '...' role", inline=True)`. ps_slot_txcb_
  template (&B575) and rom_tail_padding (&BFC5) got per-byte / per-
  region inline comments. `data runs --unannotated` now empty.
- **Bucket 2 (cmd_table_fs symbolic):** all 25 *command entries now
  emit `equb <(label-1)` / `equb >(label-1)` with per-entry inline
  role comments. Three structural fixes uncovered: *Cdir target moved
  from &B0A0 to &B0A1 (PHA/PHA/RTS lands one byte past the opcode);
  *I am gets cmd_iam_save_ctx prologue label at &8D87; *Net gets
  cmd_net_check_hw label at &8B39. Cleared a 327-line stale block of
  4.18 OSWORD-13 / handle-mgmt / bridge-query comments at &A60E..&A84C
  that were duplicating real 4.21 annotations.

State after Buckets 1/2/4: density 87.4 % / 459 subs / verify
byte-identical / lint and comments-check clean / `data runs
--unannotated` empty.

### 2026-05-02 (Buckets 3, 5, 6, 7 -- the long haul)

Walked every remaining partial-coverage routine in nine commit
batches (3a..3i), plus tackled the recovered code in the
osbyte_a2 grouping (Bucket 6), the nfs_init_body dispatch trace
(Bucket 5), and the strategic auto-label renames (Bucket 7).

- **Bucket 3 (top-20 walk):** 9 commits adding ~480 inline
  comments across roughly 60 routines, in roughly impact order:
  request_next_wipe response tail (45 items); the small wins
  cluster (cmd_dir / cmd_pollps / init_dump_buffer /
  tx_calc_transfer / service_handler -- 60 items); a 10-routine
  dispatch-target batch (lang/osword_4/find_station/fscv/
  err_bad/cmd_fs_reentry -- ~70 items); a 7-routine svc_2 /
  lang_1 / strip_token_prefix tail / alloc_run_channel /
  osword_setup / osword_13_set_handles / store_ptr_at_ws_y batch
  (~65 items); cmd_run_via_urd / init_bridge_poll / copy_ps_data
  / fscv_5_cat / fsreply_2 (~125 items); 12 mid-tier helpers
  (select_fs / loop_next_char / osword / netv / cmd_net_check_hw
  etc -- ~75 items); the lang_2 / serialise_palette / read_osbyte
  / handle_spool_ctrl_byte tails (~40 items); a final 14-routine
  small-routine sweep (~50 items).
- **Bucket 6 (osbyte_a2 dead-code fate):** decided it's *not*
  dead -- the 126 items at &9612..&973C include the recovered
  CMOS-bit helpers (&9619 / &9623, no static callers but
  dispatch-table reachable), parse_object_argument (&9630, idx
  &18), match_on_suffix (&969A, idx &0F), and the *HELP <topic>
  ON file-load loop. Walked all of it (~125 items).
- **Bucket 5 (O-1):** traced the dispatch arithmetic. The only
  way to reach idx 22 = nfs_init_body in svc_dispatch is via
  service_handler's CMP/SBC chain with input `&27` (= 39
  decimal), producing X = 21, then svc_dispatch's `INX/DEY/BPL`
  loop adds 1. The MOS-side trigger that issues service `&27`
  remains unidentified, but the dispatch math is solid and the
  body is real code. Updated nfs_init_body's description and
  marked O-1 as PARTIALLY RESOLVED in OPEN-ISSUES.md.
- **Bucket 5 also:** walked nfs_init_body itself (48 items).
- **Bucket 7 (selective auto-rename):** renamed 8 cXXXX labels at
  routine junction points where a semantic name aids
  understanding. The other ~80 auto-labels stay as cXXXX (1-3
  instruction continuation pads).
- **Two stale-block cleanups along the way:** ~210 lines of 4.18
  process_spool_data / parse_access_prefix / cmd_ps / copy_ps_data
  comments (lines 11930..12135) and a separate ~80-line
  cmd_table_fs / handle-mgmt block (in Bucket 2). All 4.18
  carry-overs at addresses now occupied by different 4.21 code,
  detectable as duplicates of real annotations.

Final state: 100.0 % inline density, all checks clean.
