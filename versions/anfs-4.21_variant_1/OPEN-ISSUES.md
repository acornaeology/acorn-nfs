# ANFS 4.21 (variant 1) — open issues

A register of unresolved questions and known stale annotations
specific to the ANFS 4.21 variant 1 disassembly. The recovery work
on this ROM has surfaced a cluster of related puzzles around the
`svc_dispatch` table and its CMP/SBC chain that are best resolved
together, since they share the same misinterpretation upstream.

Each entry records:

- **What's known** (verified facts, byte-level evidence)
- **What's not known** (the actual open question)
- **What's been ruled out** (avenues already explored that didn't pan
  out, so we don't repeat the dead end)
- **Suggested next steps** when picking it back up

If a future session resolves an issue, move the resolution into
either `docs/analysis/` (project-level analyses) or
`PROGRESS.md`/`ANNOTATION-PROGRESS.md` (version-internal notes),
and remove the entry from here.

---

### O-1: What dispatch path reaches `nfs_init_body` at &8F38?

**Status:** unresolved (Phase C continuation).

**What's known:**

- The body at `&8F38..&903B` is decoded code (no longer EQUBs) that
  performs the full ANFS bring-up sequence: clear workspace, read CMOS
  station ID, install printer-server template, call `cmd_net_fs` to
  select ANFS, call `init_adlc_and_vectors` to install NETV / FSCV /
  FILEV / etc., call `handle_spool_ctrl_byte` and `init_bridge_poll`
  for protection setup, raise the `Station number in CMOS RAM
  invalid. Using 1 instead!` error if the CMOS station is zero.
  Returns via `RTS` at `&903B`.
- The body has *no* incoming `JSR` / `JMP` / branch from anywhere in
  the ROM. It is reachable only via PHA/PHA/RTS dispatch.
- The svc_dispatch table at `&89ED` (lo) / `&8A20` (hi) has an entry
  at index 22 whose target-1 is `&8F37` (lo=&37, hi=&8F), so RTS
  lands at `&8F38`.
- The byte sequence `38 8F` (little-endian &8F38) does not appear
  anywhere in the ROM, and `&37 / &8F` only appear adjacent in the
  expected dispatch-table positions. So the only mechanism that
  forms the address `&8F38` for execution is the table read.
- `svc_dispatch` is called from five sites (&8ADB, &8E49, &8E59,
  &8E63, &8EE6) and once via fall-through from `dir_op_dispatch` at
  `&8E5F`. Tracing each caller's `(X, Y)` pair should determine
  exactly which call site can reach index 22 -- but that trace has
  not yet produced a clean answer that doesn't lead to wrong
  conclusions (see "What's been ruled out" below).
- `svc_dispatch` computes `X_final = X_caller + Y_caller + 1`, and
  the table is indexed by `X_final`.

**What's not known:**

- Which call site of `svc_dispatch` legitimately invokes index 22 in
  the live ROM, and from what real-world trigger.
- Whether the body at `&8F38` is dead in this build or has a live
  trigger that just isn't visible in this single-ROM analysis.

**What's been ruled out:**

- *No companion ROM hypothesis.* An earlier hypothesis was that
  service 39 (= `&27`) is issued by a sibling Master 128 ANFS
  variant, dovetailing with the `_variant_1` naming. The user
  confirmed this is wrong: there is no companion ROM in the
  intended deployment, so chasing inter-ROM service issuance is a
  dead end.
- *Self-issuance via OSBYTE &8F.* Searched the entire ROM for
  `LDX #&21..&29` (load X with service 33-41), and for any
  `LDA #&8F` (issue service request) preceded by an indirect X
  load. Only two `OSBYTE &8F` issuance sites exist in this ROM:
  `&8063` issues service 12 (NMI claim), and `&8D04` issues
  service 15 (vectors claimed). Neither targets the 33-41 range.
- *Direct branch into &8F38.* No `JSR &8F38`, `JMP &8F38`,
  conditional branch with target `&8F38`, or self-modifying-code
  preparation of the address `&8F38` exists in the ROM.

**Confidence note on the trace:**

The reading that "index 22 corresponds to MOS service 39" comes from
the CMP/SBC chain at `&8AB0..&8ACE`:

```
&8AB0  CMP #&0D       ; svc < 13?
&8AB2  BCC dispatch_svc_index
&8AB4  SBC #5
&8AB6  CMP #&0D
&8AB8  BEQ dispatch_svc_index   ; svc 18 -> X=13
&8ABA  BCC unhandled
&8ABC  SBC #5
&8ABE  CMP #&0E
&8AC0  BEQ dispatch_svc_index   ; svc 24 -> X=14
&8AC2  BCC unhandled
&8AC4  SBC #8
&8AC6  CMP #&0F
&8AC8  BCC unhandled
&8ACA  CMP #&18
&8ACC  BCC dispatch_svc_index   ; svc 33-41 -> X=15-23
```

This trace gives `svc 39 -> X=21 -> table[22]`. But since service 39
isn't issued by anyone we can find, the more likely conclusion is
that **this trace is interpreting the chain incorrectly** -- the user
has signalled that one of my assumptions upstream is wrong, and
chasing "who issues service 39" is the wrong direction.

**Suggested next steps:**

1. Re-examine the CMP/SBC chain assuming the input value at `&8AB0`
   is *not* a raw MOS service number. What else could `A` represent
   at that point? Is there a path from `service_handler` to `&8AB0`
   that transforms `A` in a way I missed?
2. Look at the `cmp #&24` at `&8A8F`. The driver inline comment says
   "Service 1 (workspace claim)?" but the byte clearly compares
   against `&24` (= 36). If the comment were correct, that would
   imply `A` at that point is *not* the raw service number -- which
   would also reframe the SBC chain's input.
3. Cross-reference the DNFS 3.00 source code (linked from
   `acornaeology.json` references) to see how the equivalent chain
   was structured there, and what `A` actually represents at the
   point of comparison.
4. Check whether the LDY operand bytes in the various `svc_dispatch`
   callers (&8E48 = `&25`, &8E58 = `&1D`, &8E60 = `&18`, &8EE5 =
   `&2F`) match other versions or expected sub-table boundaries. A
   mismatch in any of these would change which indices each path
   can reach.
5. Set a watch on this routine in an emulated boot trace and observe
   what stack state precedes the RTS that lands on `&8F38`. That
   would directly reveal the trigger without depending on static
   analysis.

**Cross-references:**

- Source: `versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py`,
  the entry block at the `entry(0x8EFE)` / `entry(0x8F10)` /
  `entry(0x8F38)` declarations and the dispatch-table comment block.
- Comparison ROM: `versions/anfs-4.18/disassemble/disasm_anfs_418.py`,
  `svc_2_private_workspace` at `&8EB8`. The same logical work as
  4.21's `&8F38` body lives inline at the end of 4.18's svc_2 — so
  4.21 has split or re-routed it.

---

### O-2: `label(0x8EE9, "svc_1_abs_workspace")` is a stale 4.18 carry-over

**Status:** noted; depends on resolving O-1.

**What's known:**

- 4.18's svc_1 handler is at `&8EE9` and the label was carried over
  to the 4.21 driver verbatim.
- In 4.21 the actual svc 1 dispatch (`table[2]` of the dispatch
  table) targets `&8D09`, not `&8EE9`. `&8D09` is a short routine
  that reads CMOS byte `&11`, tests bit 0, and conditionally bumps
  Y to `&10`.
- `&8EE9` is reachable via PHA/PHA/RTS dispatch but the exact
  trigger for it depends on the resolution of O-1. The body is a
  small 4-instruction routine that ensures `Y >= &C8` -- a much
  larger workspace size than 4.18's `&16` minimum. The cap value
  `&C8` was the original signal that 4.21's workspace layout had
  changed substantially.

**What's not known:**

- The correct semantic name for `&8EE9` in 4.21.

**Suggested next steps:**

- Resolve O-1 first; the dispatch path that reaches `&8EE9` will
  reveal what kind of workspace it is being asked to grow to `&C8`
  pages for, which should indicate the routine's real role.
- Once the role is clear, rename the label and remove the stale
  4.18 description.

---

### O-3: Inline comment at `&8A8F` claims "Service 1" but the byte is `CMP #&24`

**Status:** noted; relates to O-1.

**What's known:**

- `&8A8F` byte = `C9 24` = `CMP #&24`. The driver inline comment
  reads "Service 1 (workspace claim)?" -- a plain carry-over from a
  4.18 version where the byte was probably different.
- The branch on this CMP only special-cases an ADLC-presence refresh
  for whatever `A == &24` represents at that point.

**What's not known:**

- What `&24` (= 36) means in this context. If `A` at this point is a
  raw service number, then 4.21 special-cases service 36 for an
  ADLC-presence check. If `A` is something else (the lurking
  possibility flagged in O-1), the meaning differs.

**Suggested next steps:**

- Cleanup is contingent on resolving O-1.

---

### O-4: `dir_op_dispatch` description says `Y=&0E` but byte is `&18`

**Status:** known stale comment.

**What's known:**

- `&8E5F` bytes = `A0 18` = `LDY #&18` (= 24 decimal).
- The subroutine description for `dir_op_dispatch` at `&8E5B` says
  "sets Y=&0E" -- a 4.18 carry-over. 4.21 has changed this to
  `&18`, which shifts the dispatch-table indices reached by
  directory operations from `15..19` (in 4.18) to `25..29` (in
  4.21).
- The shift means the entries at indices 15..19 in 4.21 are *not*
  used by `dir_op_dispatch` and must be reached by some other
  mechanism (linked to O-1).

**Suggested next steps:**

- Update the description to say `Y=&18` and `indices 25..29` once
  the broader picture in O-1 is settled.
