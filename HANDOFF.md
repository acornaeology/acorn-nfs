# Successor session handoff: ANFS 4.21 (variant 1) disassembly

This document is the prompt for a successor Claude session. It is
self-contained — read it once, then dive into the tracking files
listed below.

---

## Where to start (read these in order)

1. `versions/anfs-4.21_variant_1/ANNOTATION-PROGRESS.md` — **the live
   work plan**. Current state, coverage history, 10 phases (A..J),
   per-phase todo lists. **This is the source of truth.**
2. `versions/anfs-4.21_variant_1/OPEN-ISSUES.md` — **register of
   unresolved questions** about this ROM. Currently a cluster of
   four related puzzles (O-1..O-4) around `svc_dispatch` and its
   CMP/SBC chain that resolve together. Read before re-entering
   Phase C work.
3. `versions/anfs-4.21_variant_1/PROGRESS.md` — earlier per-routine
   review log + cross-version findings (Master OS gate, OSWORD &13
   auto-select, workspace migration, 65C12 adoption, variant naming).
4. `docs/analysis/` — published analyses linked from the website:
   - `authors-easter-egg.md` — *HELP authors trigger and the
     keyword-overlapping-message trick across 4.08.53 / 4.18 / 4.21
   - `anfs-421-variant-naming.md` — falsifiable hypothesis for why
     this ROM is "variant 1"
5. `docs/techniques/README.md` and the four numbered papers in that
   directory — describe the address-recovery techniques we built and
   when to apply each.
6. `CLAUDE.md` and `DISASSEMBLY.md` at the repo root — project-wide
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

## Heads-up: tools may be moving out of this repo

The user is currently extracting the disassembly assistance tooling
(currently under `src/disasm_tools/` — `blockmatch.py`,
`fingerprint.py`, `audit.py`, `lint.py`, `verify.py`, `cfg.py`,
`asm_extract.py`, `compare.py`, etc.) into a **dedicated package**.
By the time you start, the layout may have changed: imports may move
to a new top-level package name, the `acorn-nfs-disasm-tool` CLI
entry-point may be renamed, or the modules may be installed as a
dependency rather than living in-tree.

**Before doing anything else:**

- `git log --oneline -20` to see what landed since this handoff was
  written.
- `cat pyproject.toml` to see the current package layout / scripts.
- `uv run acorn-nfs-disasm-tool --help` to confirm the CLI still
  works under that name. If it doesn't, look for the renamed entry
  point or run the moved modules directly.
- Confirm `uv run acorn-nfs-disasm-tool verify 4.21_variant_1` and
  `lint 4.21_variant_1` still pass before changing any 4.21 driver
  content. If they don't, the tooling extraction is mid-flight and
  the user will tell you what to do — don't try to fix it yourself
  unless asked.

The 4.21 driver script itself
(`versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py`)
should be unaffected: it uses the py8dis DSL, not the disasm-tools
package.

---

## Current state (snapshot at handoff)

- `git status` clean. Working tree consistent with HEAD.
- 8 commits ahead of `origin/master` — **never push, the user does
  that themselves**.
- ROM verifies byte-identical (16384 bytes); lint clean.
- **320 subroutines, 1281 labels, 7791 comments**, 90.3% inline
  coverage (5989 of 6630 code items).
- Audit baseline: 0 NO_DESCRIPTION, 0 AUTO_NAME, 0 undeclared JSR
  targets, 1 DATA_ONLY (intentional — `fs_vector_table`).
- Calling-convention coverage (after the recent overcook trim):
  **on_entry on 192 / 320 subs (60.0%); on_exit on 165 / 320 (51.6%)**.
  This is post-trim, where every dict has been filtered down to
  registers and flags only — see "Conventions" below.
- Recently published: `docs/analysis/authors-easter-egg.md` (with
  `acornaeology.json` analyses link wired through to the website).

---

## Recent session highlights (what changed since the previous handoff)

The previous handoff was at commit `a1e82ae`. Since then:

1. **Phase A bulk pass complete.** Calling conventions were added
   across the ROM, then trimmed — see "Conventions" below.
2. **Authors easter egg analysis written** and wired into
   `acornaeology.json` so it appears on the live site.
3. **Stale `ps_template_base` label fixed** — was at &8D6E (4.18
   carry-over with no instruction reference), now at the live
   address &8DA7.
4. **EQUB block at &8EFE..&903B reclassified as code.** Three
   PHA/PHA/RTS-reachable routines recovered:
   - `&8EFE` (entry)
   - `&8F10` `svc_2_private_workspace_pages` (4-instruction Y-cap)
   - `&8F38` `nfs_init_body` (~92-byte ANFS bring-up sequence:
     CMOS station read, printer-server template install, NETV /
     FSCV / FILEV install, station-zero error)
5. **&8D09 reclassified as code** — the actual svc 1 dispatch
   target (a short CMOS-byte-&11 / Y-bump routine).
6. **Open issues registered.** `OPEN-ISSUES.md` records four
   related puzzles (O-1..O-4) about which dispatch path actually
   reaches `nfs_init_body`. The "companion ROM" hypothesis is
   **explicitly ruled out** — do not chase it again.
7. **Overcooked on_entry/on_exit dicts trimmed.** A one-shot AST
   script stripped narrative entries (e.g. `'workspace'`, `'ptr'`,
   `'side_effect'`) from 212 subroutine() calls, removing 368
   entries. **New rule, going forward:** on_entry / on_exit hold
   ONLY register and flag keys.

---

## Work plan (copied from ANNOTATION-PROGRESS.md, summary)

| Phase | What | Status |
|-------|------|--------|
| A | Subroutine calling conventions (`on_entry` / `on_exit`) | **Bulk pass done.** Now 60.0% / 51.6% under the registers-and-flags-only rule. Remaining gap is the legitimately-no-register-state subs and a few that still need a flag/register noted. |
| B | Identify undeclared subroutines via `audit --undeclared` | **Done** (0 undeclared remaining) |
| C | Recover remaining UNMAPPED 4.18 routines | Partial. Done: `tx_calc_transfer`, `tx_done_jsr`, `&8EFE`, `svc_2_private_workspace_pages`, `nfs_init_body`, `&8D09`. Still: `cmd_close`, `cmd_print`, `cmd_prot`, `cmd_type`, `cmd_unprot`, `read_paged_rom`, `set_jsr_protection`, `tx_ctrl_machine_type`, `check_escape`, `osword_4_handler`. **Outstanding mystery: O-1 in OPEN-ISSUES.md.** |
| D | Long EQUB runs → reclassify as EQUW/EQUS where appropriate | Pending. 11 candidates over 8 bytes (top: &AE33 39 EQUBs, &B0D5 28, &ADC1 18, &88F0 16). |
| E | Address tables → symbolic via `<()` / `>()` operators | Partial — `imm_op_dispatch_lo` done (&848B). More tables remain: `tx_done_dispatch_*`, `tx_ctrl_dispatch_*`, star-command dispatch tables, the svc_dispatch lo/hi pair at &89ED/&8A20, others. |
| F | Stale UNMAPPED comment cleanup | Pending |
| G | Last 9.7% inline-comment coverage | Pending — partly falls out of D and E. Top candidates: `ensure_fs_selected` (&8B4D, 0%), `osbyte_a2` (&9612, 33%), `issue_svc_15` (&8D02, 21%), `svc_2_private_workspace_pages` (&8F10, 12%), `print_hex_byte_no_spool` (&924C, 0%), `check_escape_and_classify` (&988F, 9%), `nfs_init_body` (&8F38, 48%), `copy_ps_data` (&B3D7, 49%). |
| H | Audit-tool flag review (BRANCH_ESCAPE 92, NO_REFS 61, FALL_THROUGH 136, FALL_THROUGH_ENTRY 27) | Pending |
| I | `rom.json` `address_links` and `glossary_links` | Pending — depends on J |
| J | `versions/anfs-4.21_variant_1/CHANGES-FROM-4.18.md` | **Final deliverable.** Don't draft until A-H are at >= 95% coverage on each dimension. |

**Recommended next phase:** continue **C** (the remaining UNMAPPED
4.18 routines) and **G** (low-coverage subs) in tandem — they
overlap, since recovered routines need fresh inline comments. Phase
**E** is also high-leverage: every dispatch table you make symbolic
removes a class of fragile `equb &XX` lines.

If you do touch Phase A again, the goal is no longer raw coverage
percentage but **correctness under the registers-only rule**: scan
for any subs whose code clearly takes/returns A/X/Y but lacks the
matching dict entry.

---

## Key tools (CLI under `uv run acorn-nfs-disasm-tool`)

> The CLI name may change once the tool extraction lands — see
> "Heads-up" above.

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
- `fingerprint` module — locate a routine in version B by
  sliding-window opcode similarity (ignores the existing address
  map; useful when LCS consumed source bytes for unrelated mappings).
- `blockmatch` module — primary LCS + supplementary
  seed-and-extend (BLAST/minimap2-style) opcode-level address mapping.

---

## Conventions you must follow

These are non-negotiable per the user's standing instructions:

1. **Inline comments express domain meaning, not mnemonic.** `LDA #&0D`
   should be commented as "Load CR (newline) for OSASCI", never
   "Load &0D into A".
2. **Every subroutine needs a description.** Use:
   `subroutine(addr, name, title=..., description="...", on_entry={...},
   on_exit={...})`.
3. **on_entry / on_exit hold ONLY register and flag keys.** Allowed
   keys: `'a'`, `'x'`, `'y'`, `'p'`, `'s'`, `'c'`, `'n'`, `'v'`,
   `'z'`, `'d'`, `'i'`, `'b'`. Parenthesised qualifiers like
   `'c (set)'` are fine. **Do NOT** add narrative keys (`'workspace'`,
   `'ptr'`, `'service'`, `'side_effect'`, etc.) — those belong in
   the description. The good examples are &8028 and &8045; the
   anti-pattern was the pre-trim &8070. If a sub's calling
   convention is genuinely "no register state", omit on_entry /
   on_exit entirely.
4. **Side effects (workspace bytes, stack consumption, V/C semantics
   beyond a simple flag, vectors touched) belong in the description**,
   not in on_entry / on_exit.
5. **Address tables should be symbolic.** Replace `equb &XX` with
   `equb <(label-1)` / `equb >(label-1)` for PHA/PHA/RTS dispatch
   tables, or `equw label` for absolute pointers. The
   `imm_op_dispatch_lo` table at &848B is the canonical example.
6. **Naming: use `_filepath`, `_dirpath`, `_dirname`, `_filename`
   suffixes** (not `_dir`, `_file`).
7. **Acorn `&XXXX` notation in docs and Markdown; Python `0xXXXX` in
   scripts.**
8. **No emojis** in commit messages, code comments, or any committed
   file. Avoid using them anywhere unless explicitly requested.
9. **Don't reference yourself, "Claude", Anthropic, or the LLM model**
   in commit messages or comments.
10. **Never push.** Leave `git push` to the user.
11. **Verify + lint after every chunk.** Both must pass before
    committing.
12. **Small commits, frequent commits.** One routine or one small
    cluster per commit. Match the cadence in the recent git log.
13. **Don't draft `CHANGES-FROM-4.18.md` (Phase J) until phases A-H
    are substantially complete.** The user explicitly does not want a
    premature CHANGES doc.
14. **No commenting noise.** Don't write `; load A` or `; jump`. Don't
    add comments where the well-named identifier already says it. Only
    comment the *why* and the *domain meaning*.
15. **Annotations live in `comment(addr, "...")` calls, not Python
    `#` comments** in the driver. Python comments don't appear in
    the generated `.asm`. Use block triple-quoted strings for
    multi-line `comment()` calls.

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
- **ACCCON save/restore** brackets the NMI data-copy paths (see the
  Phase G commit, `eb32468`).
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
7. **Dispatch-table reshape**: 4.18's svc dispatch table layout
   shifted in 4.21; `dir_op_dispatch` now sets `Y=&18` (not `&0E`),
   moving its reachable indices from 15..19 to 25..29. Some 4.18
   labels (e.g. `svc_1_abs_workspace`, `ps_template_base` at the
   wrong address) survived as carry-overs and have been moved or
   demoted — see commits `915eaf5`, `569bf49`. **Outstanding:** the
   real path that reaches `nfs_init_body` at &8F38 is the subject
   of OPEN-ISSUES O-1.
8. **ANFS bring-up code path moved**: the body that did "first-time
   ANFS init" inline at the end of 4.18's `svc_2_private_workspace`
   (&8EB8) has been split out / re-routed in 4.21 — `nfs_init_body`
   at &8F38 now contains the equivalent work, reachable only via
   PHA/PHA/RTS dispatch.

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
   or decode the dispatch table directly. The recent &8EFE / &8F10 /
   &8F38 / &8D09 recoveries are examples.
3. **Address shifts can be small but consequential**: e.g.
   `tx_done_jsr` moved from 4.18 &8543 to 4.21 &8540 (-3 bytes), and
   `osword_13_set_station`'s body landing was off by 3 bytes from the
   dispatch entry (the FS-active-check JSR was extracted into its own
   routine).
4. **EQUB classification can be wrong.** `byte()` directives carried
   over from 4.18 may force 4.21 code-bearing bytes to data
   classification. `imm_op_dispatch_lo` at &848B and the
   &8EFE..&903B block are both examples — fix is to remove the
   `byte()` carryovers and add `entry(addr)` markers so py8dis
   walks the bytes as code.
5. **Dual-use bytes**: e.g. `osbyte_a1` at &8E9A — its 5 bytes (`A9 A1
   4C F4 FF`) are both the routine's code AND the leading entries of
   a vector-dispatch data table read by `write_vector_entry` via
   `LDA c8e9a,Y`. Spot the dual-purpose by checking what reads the
   address as data while a JSR also targets it.
6. **Stale carry-over comments at unrelated addresses.** When you
   spot wildly inappropriate inline comments (e.g. `Bit 4: &88 =
   %10001000` on a routine that prints text), strip them — they're
   from 4.18 mappings that landed on different code.
7. **Don't speculate about "companion ROMs" issuing services to this
   one.** The user has explicitly ruled this out as the explanation
   for unreachable dispatch entries. If a dispatch index has no
   apparent caller, record it in OPEN-ISSUES.md and move on — don't
   invent inter-ROM service flows. See O-1 for the full list of
   ruled-out hypotheses.
8. **Python `col_offset` is byte-based, not char-based.** If you
   write an AST-driven cleanup script over the driver, encode the
   source to UTF-8 bytes and index by byte offset. The em-dash `—`
   (3 bytes UTF-8) in some descriptions will silently corrupt
   char-indexed edits.

---

## Resuming workflow

When you start a session:

1. `git log --oneline -10` to see the last few commits.
2. Verify the toolchain still works (see "Heads-up" above) — the
   user may have moved tools out into a dedicated package.
3. `cat versions/anfs-4.21_variant_1/ANNOTATION-PROGRESS.md` to read
   the plan.
4. `cat versions/anfs-4.21_variant_1/OPEN-ISSUES.md` if you're going
   to be doing dispatch-table work or recovering anything around the
   svc_dispatch chain.
5. `uv run acorn-nfs-disasm-tool context 4.21_variant_1 --summary`
   to see current coverage stats and candidates.
6. Pick a phase from the plan; do small batches; commit per batch
   after `verify` + `lint` pass.
7. End the session with a coverage snapshot row in
   `ANNOTATION-PROGRESS.md` and an updated todo list.

If you find new structural patterns worth recording (new dispatch
table style, new behaviour change between versions, new annotation
gotcha), add a note to `PROGRESS.md` under "Findings" or open an
analysis doc in `docs/analysis/` (and link it from
`acornaeology.json` so it appears on the website).

If you build a new generic tool (something that benefits future
versions, not just this one), put it under `src/disasm_tools/` and
write a short paper for `docs/techniques/`. **But check first**
whether the tool extraction has happened — if the package has moved,
contributions go to the new package, not back here.

---

## What NOT to do

- Don't start writing `CHANGES-FROM-4.18.md` (Phase J) until phases
  A-H are substantially done. The user has been clear about this.
- Don't push to the remote.
- Don't add narrative keys to on_entry / on_exit dicts. Registers
  and flags only.
- Don't speculate about companion ROMs to explain unreachable
  dispatch entries — record the puzzle in OPEN-ISSUES.md instead.
- Don't delete `docs/Econet Level 3 File Server Manager's Guide.pdf`
  if you find it on disk — it was history-stripped via filter-repo
  for being too large. The `.gitignore` already keeps it untracked.
- Don't add emojis or self-references to anything you commit.
- Don't try to do all remaining work in one massive commit. Small
  batches with verify + lint between is the established cadence.
- Don't change tool behaviour without checking that other versions
  still verify — and bear in mind the tool extraction may be in
  flight.

Good luck.
