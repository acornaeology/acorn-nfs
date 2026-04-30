# Successor session handoff: ANFS 4.21 (variant 1) disassembly

This document is the prompt for a successor Claude session. It is
self-contained — read it once, then dive into the tracking files
listed below.

---

## Where to start (read these in order)

1. `versions/anfs-4.21_variant_1/ANNOTATION-PROGRESS.md` — **the live
   work plan**. Current state, coverage history, 10 phases (A..J),
   per-phase todo lists. **This is the source of truth.**
2. `versions/anfs-4.21_variant_1/PROGRESS.md` — earlier per-routine
   review log + cross-version findings (Master OS gate, OSWORD &13
   auto-select, workspace migration, 65C12 adoption, variant naming).
3. `docs/techniques/README.md` and the four numbered papers in that
   directory — describe the address-recovery techniques we built and
   when to apply each.
4. `CLAUDE.md` and `DISASSEMBLY.md` at the repo root — project-wide
   conventions and tool reference.

The `memory/` system (auto-loaded into context) already carries the
key facts; you don't need to read it explicitly but
`memory/anfs-421-variant-1.md` mirrors much of this.

---

## Project context (one paragraph)

This is the `acorn-nfs` repo: an annotated disassembly project for
Acorn NFS (BBC Micro Network Filing System) and ANFS (Advanced NFS)
ROMs. Multiple versions are already complete (3.34 through 3.65,
4.08.53, 4.18). The current focus is **ANFS 4.21 variant 1**, the
first Master 128 ANFS, which uses the 65C02 (CMOS 6502) instruction
set, has no relocated-block copy code (uses sideways-RAM filing-system
workspace at &C000-&C2FF instead), and was generated initially by
applying a 4.18 → 4.21 address map via `generate_421_variant_1.py`
(which uses `src/disasm_tools/blockmatch.py`).

---

## Current state (snapshot at handoff)

- `git status` clean. Working tree consistent with HEAD.
- 67 commits ahead of `origin/master` — **never push, the user does
  that themselves**. (The user has just rewritten history with
  `git filter-repo` to drop a 113 MB PDF and re-set the upstream;
  it's a fast-forward from the remote's POV.)
- ROM verifies byte-identical (16384 bytes); lint clean.
- 318 subroutines, 1281 labels, 7753 comments, 90.9% inline coverage
  (5899 of 6487 code items).
- Audit baseline: 0 NO_DESCRIPTION, 0 AUTO_NAME, 0 undeclared JSR
  targets, 1 DATA_ONLY (intentional — `fs_vector_table`).

---

## Work plan (copied from ANNOTATION-PROGRESS.md, summary)

| Phase | What | Status |
|-------|------|--------|
| A | Subroutine calling conventions (`on_entry` / `on_exit`) | **Biggest gap** — only 32% have on_entry, 17% have on_exit. ~198 subs need work. |
| B | Identify undeclared subroutines via `audit --undeclared` | **Done** (10 recovered) |
| C | Recover remaining UNMAPPED 4.18 routines | Partial — `tx_calc_transfer`, `tx_done_jsr` done. Still: `svc_2_private_workspace`, `cmd_close`, `cmd_print`, `cmd_prot`, `cmd_type`, `cmd_unprot`, `read_paged_rom`, `set_jsr_protection`, `tx_ctrl_machine_type`, `check_escape`, `osword_4_handler` |
| D | Long EQUB runs → reclassify as EQUW/EQUS where appropriate | Pending. 11 candidates over 8 bytes (top: &AE33 39 EQUBs, &B0D5 28, &ADC1 18, &88F0 16). |
| E | Address tables → symbolic via `<()` / `>()` operators | Partial — `imm_op_dispatch_lo` done (&848B). More tables: `tx_done_dispatch_*` (&853E in 4.18, moved in 4.21), `tx_ctrl_dispatch_*` (&8681), star-command dispatch tables, others. |
| F | Stale UNMAPPED comment cleanup (~1900 lines) | Pending |
| G | Last 9.1% inline-comment coverage | Pending — partly falls out of D and E |
| H | Audit-tool flag review (BRANCH_ESCAPE 91, NO_REFS 59, FALL_THROUGH 131, FALL_THROUGH_ENTRY 27) | Pending |
| I | `rom.json` `address_links` and `glossary_links` | Pending — depends on J |
| J | `versions/anfs-4.21_variant_1/CHANGES-FROM-4.18.md` | **Final deliverable.** Don't draft until A-H are at >= 95% coverage on each dimension. |

**Recommended next phase: A** (calling conventions). It's the largest
remaining dimension and high leverage — every subroutine should
document on_entry / on_exit / side effects. Best worked
bottom-up (leaves first); see ANNOTATION-PROGRESS.md for the audit
listing of leaves still missing this.

---

## Key tools (CLI under `uv run acorn-nfs-disasm-tool`)

| Subcommand | What |
|---|---|
| `disassemble <ver>` | Generate `.asm` and `.json` from the driver script |
| `verify <ver>` | Reassemble via beebasm, byte-compare against ROM (THE correctness check) |
| `lint <ver>` | Validate annotation addresses, doc links |
| `audit <ver> --summary` | Subroutine summary with audit flags |
| `audit <ver> --sub <addr/name>` | Full per-sub report (extent, callers, callees, comments, listing) |
| `audit <ver> --undeclared` | JSR targets without subroutine() declarations |
| `audit <ver> --flag <FLAG>` | Filter summary by flag (NO_DESCRIPTION, AUTO_NAME, NO_REFS, ...) |
| `cfg <ver> --leaves` / `--roots` / `--sub <name>` | Call-graph queries |
| `context <ver> --summary` | Global inline-coverage stats + candidate list |
| `extract <ver> <start> [end]` | Assembly listing for a region |
| `compare <ver1> <ver2>` | Cross-version comparison (uses 65C02 sweep when rom.json says cpu='65c02') |

Python modules (for ad-hoc work):
- `src/disasm_tools/fingerprint.py` — locate a routine in version B
  by sliding-window opcode similarity (ignores the existing address
  map; useful when LCS consumed source bytes for unrelated mappings).
- `src/disasm_tools/blockmatch.py` — primary LCS + supplementary
  seed-and-extend (BLAST/minimap2-style) opcode-level address mapping.

---

## Conventions you must follow

These are non-negotiable per the user's standing instructions:

1. **Inline comments express domain meaning, not mnemonic.** `LDA #&0D`
   should be commented as "Load CR (newline) for OSASCI", never
   "Load &0D into A".
2. **Every subroutine needs a description AND calling convention**:
   `subroutine(addr, name, title=..., description="...", on_entry={...},
   on_exit={...})`. Use lowercase register names ('a', 'x', 'y').
   Document side effects in the description (workspace bytes touched,
   stack consumed, V/C semantics, etc.).
3. **Address tables should be symbolic.** Replace `equb &XX` with
   `equb <(label-1)` / `equb >(label-1)` for PHA/PHA/RTS dispatch
   tables, or `equw label` for absolute pointers. The
   `imm_op_dispatch_lo` table at &848B is the canonical example
   (committed earlier in this session).
4. **Naming: use `_filepath`, `_dirpath`, `_dirname`, `_filename`
   suffixes** (not `_dir`, `_file`).
5. **Acorn `&XXXX` notation in docs and Markdown; Python `0xXXXX` in
   scripts.**
6. **No emojis** in commit messages, code comments, or any committed
   file. Avoid using them anywhere unless explicitly requested.
7. **Don't reference yourself, "Claude", Anthropic, or the LLM model**
   in commit messages or comments.
8. **Never push.** Leave `git push` to the user.
9. **Verify + lint after every chunk.** Both must pass before
   committing.
10. **Small commits, frequent commits.** One routine or one small
    cluster per commit. Match the cadence in the recent git log.
11. **Don't draft `CHANGES-FROM-4.18.md` (Phase J) until phases A-H
    are substantially complete.** The user explicitly does not want a
    premature CHANGES doc.
12. **No commenting noise.** Don't write `; load A` or `; jump`. Don't
    add comments where the well-named identifier already says it. Only
    comment the *why* and the *domain meaning*.

---

## Master 128 specifics worth knowing

- **CPU is 65C02.** The driver script loads with `load(addr, file,
  "65c02")`. beebasm needs `CPU 1` (emitted automatically).
- **No page 4/5/6 relocated code.** The Master uses sideways-RAM
  filing-system workspace at &C000-&C2FF. There are no `move()` calls
  in the driver.
- **&0016-&0057 and &0400-&06FF are dead ranges** — addresses there in
  4.18 carry-over comments have no counterpart in 4.21.
- **Service entry at &8A54** (was &8A15 in 4.18).
- **Master-only Bad ROM check**: rejects OS 1.00, OS 1.20, OS 2.00,
  OS 5.0 (Master Compact). Hence the "variant 1" naming — likely a
  separate Compact build exists.
- **OSWORD &13 auto-selects FS** (behavior change from 4.18 which
  aborted with zero-status when FS was inactive).
- **65C12 adoption** in many routines: PHX/PHY/PLX/PLY, BRA, STZ,
  TSB/TRB, BIT abs,X.
- **Two parallel print families**: standard via OSASCI, and
  `print_*_no_spool` via `print_char_no_spool` which brackets OSBYTE
  199 (read/write *SPOOL handle) around the print to bypass any active
  spool capture. The full set: `print_newline_no_spool` (&91F9),
  `print_char_no_spool` (&91FB), `print_byte_no_spool` (&9201),
  `print_hex_byte_no_spool` (&924C), `print_hex_nybble_no_spool`
  (&9255), `print_inline_no_spool` (&928A).

---

## Cross-version findings to fold into Phase J (CHANGES doc)

These are documented in `PROGRESS.md` under "Findings" — don't lose
them. Summary:

1. **Service handler Master-only Bad ROM check** (&8A54): OS-version
   gate via OSBYTE 0; rejects everything except Master 128 (OS 3.x)
   and Master Econet Terminal (OS 4.0).
2. **OSWORD &13 auto-select**: 4.18 aborted when FS not active; 4.21
   factors the check into `ensure_fs_selected` (&8B4D) which calls
   `cmd_net_fs` to AUTO-SELECT instead, raising 'net checksum' on
   failure.
3. **Master 128 workspace migration**: 4.18's MOS RAM pages
   &0Dxx-&10xx replaced with sideways-RAM &C000-&C2FF.
4. **65C12 instruction adoption** for tighter prologues.
5. **No page-relocation copy loop** (the 4.18 &BE94 area).
6. **Variant naming**: see `docs/analysis/anfs-421-variant-naming.md`
   for the falsifiable hypothesis.

---

## Things that have bitten us — watch out for these

1. **Carry-over labels at the wrong address.** The address mapper
   sometimes lands a 4.18 label at a 4.21 address whose code has
   completely different meaning. Symptom: a `subroutine()` description
   that says one thing but the actual code does another. Always
   spot-check the prologue against the description.
2. **PHA/PHA/RTS dispatch routines have no JSR caller** — won't be
   found by `--undeclared` (which scans JSR sites). Use
   `audit --sub <addr>` once you suspect an address is a sub entry,
   or decode the dispatch table directly.
3. **Address shifts can be small but consequential**: e.g.
   `tx_done_jsr` moved from 4.18 &8543 to 4.21 &8540 (-3 bytes), and
   `osword_13_set_station`'s body landing was off by 3 bytes from the
   dispatch entry (the FS-active-check JSR was extracted into its own
   routine).
4. **EQUB classification can be wrong.** `byte()` directives carried
   over from 4.18 may force 4.21 code-bearing bytes to data
   classification. The `imm_op_dispatch_lo` table at &848B was an
   example — fix is `for addr in range(...): byte(addr)` followed by
   `expr(addr, "<(label-1)")`.
5. **Dual-use bytes**: e.g. `osbyte_a1` at &8E9A — its 5 bytes (`A9 A1
   4C F4 FF`) are both the routine's code AND the leading entries of
   a vector-dispatch data table read by `write_vector_entry` via
   `LDA c8e9a,Y`. Spot the dual-purpose by checking what reads the
   address as data while a JSR also targets it.
6. **Stale carry-over comments at unrelated addresses.** When you
   spot wildly inappropriate inline comments (e.g. `Bit 4: &88 =
   %10001000` on a routine that prints text), strip them — they're
   from 4.18 mappings that landed on different code.

---

## Resuming workflow

When you start a session:

1. `git log --oneline -5` to see the last few commits.
2. `cat versions/anfs-4.21_variant_1/ANNOTATION-PROGRESS.md` to read
   the plan.
3. `uv run acorn-nfs-disasm-tool context 4.21_variant_1 --summary` to
   see current coverage stats and candidates.
4. Pick a phase from the plan; do small batches; commit per batch
   after `verify` + `lint` pass.
5. End the session with a coverage snapshot row in
   `ANNOTATION-PROGRESS.md` and an updated todo list.

If you find new structural patterns worth recording (new dispatch
table style, new behaviour change between versions, new annotation
gotcha), add a note to `PROGRESS.md` under "Findings" or open an
analysis doc in `docs/analysis/`.

If you build a new generic tool (something that benefits future
versions, not just this one), put it under `src/disasm_tools/` and
write a short paper for `docs/techniques/`.

---

## What NOT to do

- Don't start writing `CHANGES-FROM-4.18.md` (Phase J) until phases
  A-H are substantially done. The user has been clear about this.
- Don't push to the remote.
- Don't delete `docs/Econet Level 3 File Server Manager's Guide.pdf`
  if you find it on disk — it was history-stripped via filter-repo
  for being too large. The `.gitignore` already keeps it untracked.
- Don't add emojis or self-references to anything you commit.
- Don't try to do all 198 calling conventions in one massive commit.
  Small batches (10-20 subs each) with verify + lint between is the
  established cadence.
- Don't change tool behaviour without checking that other versions
  still verify (the `mos6502.py` / `compare.py` / `blockmatch.py`
  changes from this session are designed to be additive — preserve
  that property).

Good luck.
