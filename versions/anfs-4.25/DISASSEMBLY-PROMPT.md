# Prompt: produce the ANFS 4.25 annotated disassembly

You are creating a new, **very high quality** annotated disassembly of the
**ANFS 4.25** ROM (`versions/anfs-4.25/rom/anfs-4.25.rom`), the next Master 128
ANFS after 4.24. Only the ROM binary exists so far — no `rom.json`, no driver,
no output. 4.25 is expected to be **substantially similar to 4.24** (a 16 KB
65C02 Master 128 ROM using HAZEL hidden RAM at `&C000`–`&C2FF`, no relocated
blocks), just as 4.24 was ~94 % opcode-similar to 4.21.

Read `DISASSEMBLY.md` (full workflow), `CLAUDE.md` (conventions), and the memory
files — especially `anfs-424.md`, `dasmos-4-followups.md`, `char-literals.md`,
and `glossary-label-uri-schemes.md` — before starting. `versions/anfs-4.24/` is
your template for structure, style, and quality.

## The core idea

4.24 is already a complete, high-quality disassembly. **Do not disassemble 4.25
from scratch.** Instead: find where 4.25's code corresponds to 4.24's — much of
it will be structurally identical but at *shifted addresses* — and **transfer
4.24's annotations onto 4.25, shifting addresses as needed**, so that every
label name, subroutine description, comment, banner, on_entry/on_exit, data
table, and doc link is **identical to 4.24 wherever the code is the same**, and
**differs only where 4.25's code is genuinely new or changed**. This is the
version-graph workflow the project uses throughout (3.34→3.34B, 4.18→4.21→4.24,
etc.); 4.25's parent is **4.24**.

The end result must be indistinguishable in quality from 4.24: a reader
comparing 4.24 and 4.25 side by side should see the same annotations on the same
routines, with clean, specific new annotations only where 4.25 actually differs.

## Non-negotiable quality bar (all must hold at the end)

1. **`fantasm verify 4.25` passes byte-identically.** This is ground truth — the
   generated `.asm` must reassemble (beebasm) to a byte-exact copy of the ROM.
   Nothing else matters if this fails. Comments/labels never change emitted
   bytes, so verify must stay green through all annotation work.
2. **`fantasm lint 4.25 <driver>` clean** — every annotation address resolves,
   and all `address:` / `label:` / `glossary:` doc links resolve.
3. **`fantasm comments check 4.25`** — 0 HIGH findings (a comment must never
   state a register value / behaviour the instruction contradicts). This is the
   key guard against operand-blind annotation transfer smearing a stale 4.24
   comment onto a changed 4.25 instruction.
4. **`fantasm audit undeclared 4.25`** — 0 undeclared JSR targets (every called
   subroutine has a `subroutine()` declaration).
5. **`fantasm coverage 4.25`** — 100 % inline-comment coverage (every code item
   commented), at or above 4.24's bar.
6. All jump/dispatch tables named and **banner'd**; all legitimate data regions
   (`EQUB`/`EQUW`/`EQUS`) carry a `subroutine()`-style banner and per-byte
   `comment()`s; no bare auto-generated (`l####`, `sub_c####`) labels except the
   deliberate data-adjacent artifacts 4.24 itself leaves.

## Phase 0 — Scaffold the version

- Create `versions/anfs-4.25/{rom,disassemble,output}`; the ROM is already in
  `rom/`. Add `disassemble/__init__.py` (empty, mirror 4.24).
- Write `versions/anfs-4.25/rom/rom.json` modelled on 4.24's: title
  `"Acorn ANFS 4.25"`, `size` 16384, `md5`/`sha256` computed from the ROM,
  `cpu`/`machine`, `links`, `references`, the `memory_map_groups` legend, and a
  `docs` entry for `CHANGES-FROM-4.24.md`. Copy the group legend from 4.24.
- Register 4.25 in `fantasm.toml` (`[[versions.entry]] id = "4.25"`,
  `parents = ["4.24"]`, no `reloc_blocks` — HAZEL, like 4.24), in
  `acornaeology.json`, and in the CI matrix in `.github/workflows/verify.yml`.

## Phase 1 — Establish the 4.24 → 4.25 delta

Before touching annotations, understand exactly how 4.25 differs from 4.24:

- `fantasm compare 4.24 4.25` at byte / opcode / full-instruction granularity to
  measure similarity and locate the change blocks. Expect a high match with a
  scattering of inserts/edits (as 4.24-vs-4.21 was 93.9 % opcode-similar).
- Note where code **shifts** (uniform address deltas across runs) versus where it
  is **genuinely edited/inserted/removed**. The dispatch-table bases, service
  entry, and any grown control blocks will move; read each change block to
  classify it as *shift* (transfer annotation, adjust address) vs *new* (write
  fresh annotation).

## Phase 2 — Bootstrap the 4.25 driver from 4.24

Write **`generate_425.py`** at the repo root, modelled closely on
`generate_424.py`. It must:

1. Build a **4.24 → 4.25 opcode-level address map** with
   `fantasm.api.blockmatch.build_full_address_map` (SequenceMatcher +
   seed-and-extend over the 65C02 opcode streams of both ROMs). Identity-map the
   fixed non-ROM addresses (zero page, stack, HAZEL `&C0xx`, MMIO `&FExx`,
   extended vectors `&FFxx`).
2. **Opcode-map the 4.24 driver** (`disasm_anfs_424.py`) onto 4.25: rewrite every
   `d.`-prefixed address argument (`label`, `subroutine`, `comment`,
   `index_base`, `entry`, `expr`, `add_move`, …) through the address map. Reuse
   4.24's fixes to the generator's statement-grouping (parens inside strings,
   triple-quote state across lines, `d.`-prefix matching, multi-line address
   args) — see `anfs-424.md`.
3. **Byte-verified interpolation** for data/label addresses the opcode stream
   didn't cover: only relocate an annotation onto a 4.25 byte when the
   instruction bytes match, so a stale comment can never smear onto an
   operand-changed instruction. Fill uniform-shift runs.
4. Mark everything it could **not** confidently map with `# UNMAPPED:` so the
   changed/new regions are obvious to annotate by hand next.

`generate_425.py` is a **one-shot bootstrap**. After it runs, the driver
`disasm_anfs_425.py` is the source of truth — never regenerate it (that would
drop hand corrections).

## Phase 3 — Drive to the quality gates

Iterate driver → `fantasm disassemble 4.25` → gates, fixing until green:

- Get **`verify` byte-identical** first. Then use the propagation/QA tools:
  - `fantasm backfill 4.24 4.25` and `fantasm annotations diff 4.24 4.25` to
    surface 4.24 annotations that map cleanly to 4.25 addresses and aren't yet
    present — copy the safe ones in. For a well-bootstrapped driver these return
    near-empty; a non-empty result flags a genuine gap.
  - `fantasm comments check 4.25` — resolve **every HIGH**. HIGH `reg_value` =
    the transfer carried a stale 4.24 comment onto a 4.25 instruction with a
    different operand/register; rewrite from the 4.25 code. MEDIUM
    `desc_stale_addr` = a 4.24 address left in prose — remap it (prefer making it
    a `label:`/`glossary:` link so it can't go stale again; see Phase 5).
  - Recover annotations the byte-verified interpolation skipped near change
    boundaries via unique ≥2-byte instruction-fingerprint matching.
- Then close coverage to **100 %** (`fantasm coverage 4.25`): annotate the
  changed-region gaps by **reading the 4.25 code**, and carry verbatim only the
  comments on structurally identical (mnemonic+mode-aligned) instructions.
- `fantasm audit undeclared 4.25` → declare every JSR target with
  `d.subroutine(...)`, including `on_entry`/`on_exit` where the calling
  convention is clear (`fantasm audit --sub &XXXX`, `fantasm sub insert`).

## Phase 4 — Annotate the genuine 4.25 deltas

For each change block Phase 1 flagged as *new/changed*, write fresh,
**specific** annotations from the 4.25 code — the same standard as 4.24's
delta annotations (defensive `CLD` guards, ACCCON save/restore, relocated
routines, grown control blocks, credits, etc.). Re-base every PHA/PHA/RTS
dispatch table from its dispatcher's operand and re-map the command tables
across any insert/shift split. Name and banner every table; document new data
bytes from value + position.

## Phase 5 — Adopt every modern convention (this is where "high quality" lives)

Use **all** the tooling. The disassembly must meet the current bar, not just
4.24's historical one:

- **`index_base` / `index_region`** for data addresses touched only as an
  indexing base (`lda base,X`). `fantasm labels list 4.25 --index-base-only`
  gives the candidate set; convert genuine data tables/scratch, leave code
  items, `d.entry()` targets, and banner regions. (See `dasmos-2-index-base.md`.)
- **Operand-override DSL**: write `d.expr()` operands with the validated
  `dasmos.expr` DSL — `from dasmos.expr import sym, lo, hi`, e.g.
  `d.expr(addr, lo(sym("label") - 1))` — never raw immediates + a comment, and
  never opaque strings. For `LDX #<lo : LDY #<hi` pointer loads use
  `lo(sym(...))` / `hi(sym(...))`.
- **Memory map**: every mapped `d.label()` / `d.index_base()` needs a `group=`
  (`zero_page` / `stack` / `ram_workspace` / `hazel` / `mmio` / `ext_vectors` /
  `idx_base`) and the `memory_map_groups` legend in `rom.json` — or dasmos warns
  (dasmos#43).
- **Character literals**: render character-valued immediates as `#'x'` via
  `d.char_literal(<operand-byte addr>)`; the driver renders with
  `char_literal_style="quote"` and `show_char_comment_hint=False`. Judge each
  site from its comment — convert genuine character compares/loads/tests; leave
  control-register values, masks, offsets, error codes, and opcode bytes as hex.
  (See `char-literals.md`; `convert_comment_address_to_label.py` /
  `propagate_char.py` show the propagation pattern.)
- **Doc / comment links**: use the explicit schemes, never the retired fuzzy
  matcher or stale numeric addresses. `[text](label:NAME)` for a labelled target
  (version-stable — resolves to the label's current address, and with `?hex`
  renders `text (&ADDR)` in the `.asm` via dasmos 4.1.0); `[text](glossary:SLUG)`
  for glossary terms; keep numeric `address:HEX` only for genuine raw-address /
  `&XXXX`-prose refs. (See `glossary-label-uri-schemes.md`.)
- Follow the authoring conventions: Markdown link syntax for addresses,
  en-dash typography, tooltip-boundary `\n`, legitimate data regions get a
  `subroutine()` banner, and **no cross-version references inside the driver** —
  comparisons live in `CHANGES-FROM-4.24.md`, not in `disasm_anfs_425.py`.

Toolchain: **dasmos 4.1.0**, **fantasm 0.18.0**. `uv add 'dasmos>=4.1.0'` if the
new version's env needs it.

## Phase 6 — Finalise

- Write `versions/anfs-4.25/CHANGES-FROM-4.24.md` documenting the **ANFS history**
  (what changed in 4.25 and why), not the disassembly process — with
  `label:`/`glossary:` links. Mirror the tone and structure of
  `CHANGES-FROM-4.21.md`; validate its links with `lint`.
- Write `versions/anfs-4.25/ANNOTATION-PROGRESS.md` (mirror 4.24's): the gate
  table, what's done, and any residual data-adjacent artifacts.
- Confirm the full gate suite green (verify, lint, comments check, audit
  undeclared, coverage 100 %) and that the site still builds
  (`acornaeology-build` in the generator repo) with 4.25's outputs.
- Do the work on a branch, in small ratcheting commits (no emojis / no
  self-reference in messages; end with the project's Co-Authored-By line). Leave
  pushing to the user. Record the outcome in a memory file and add 4.25 to the
  Completed Versions list.

## Pitfalls learned (don't relearn them)

- The opcode map covers **code** only; **data and label addresses** need the
  byte-verified interpolation pass — otherwise data tables land at 4.24
  addresses. Always `# UNMAPPED:`-mark what isn't confidently mapped.
- `SequenceMatcher`/opcode-map is **operand-blind**: two instructions with the
  same opcode but different operands look "identical", so a transferred comment
  can be stale. `fantasm comments check` is the safety net — treat every HIGH as
  a real bug.
- Re-base dispatch tables from the **dispatcher's operand**, not by assuming the
  4.24 offset. A single new command-table record shifts everything after it.
- Keep the driver free of cross-version prose; put all "vs 4.24" narrative in
  `CHANGES-FROM-4.24.md`.
