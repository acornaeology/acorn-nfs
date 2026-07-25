# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Annotated disassembly of Acorn NFS and ANFS (Network Filing System / Advanced Network Filing System) ROMs for BBC Micro. Python scripts drive [dasmos](https://acornaeology.github.io/dasmos/) (a programmable 6502 disassembler with a stable 1.0 API and byte-faithful round-trip oracle) to produce readable, verified assembly output from the original ROM binaries. Versions covered: NFS 3.34, 3.34B, 3.35D, 3.35K, 3.40, 3.60, 3.62, 3.65; ANFS 4.08.53, 4.18, 4.21 (variant 1).

## Build commands

Requires [uv](https://docs.astral.sh/uv/) and [beebasm](https://github.com/stardot/beebasm) (v1.10+).

```sh
uv sync                                                                       # Install dependencies (incl. fantasm)
uv run fantasm disassemble 3.34                                               # Run dasmos driver via fantasm (sets FANTASM_ROM / FANTASM_OUTPUT_DIR)
uv run fantasm lint 3.34 versions/nfs-3.34/disassemble/disasm_nfs_334.py     # Validate annotation addresses
uv run fantasm verify 3.34                                                    # Reassemble and byte-compare against original ROM
```

Verification is the primary correctness check: the generated assembly must reassemble to a byte-identical copy of the original ROM. Lint validates that all annotation addresses (comments, subroutines, labels) reference valid item addresses in the dasmos JSON output — catching stale addresses carried over from other versions. CI runs `fantasm disassemble`, then `fantasm lint`, then `fantasm verify` on every push.

## Architecture

### CLI: fantasm

The general-purpose 6502 disassembly tooling lives in the [fantasm](https://pypi.org/project/fantasm/) package, declared as a regular project dependency in `pyproject.toml`. Subcommands include `disassemble`, `verify`, `lint`, `compare`, `asm extract`, `audit summary|detail|undeclared`, `cfg depth|leaves|roots|sub`, `sub insert`, `comments check`, `backfill`, and `promote`. Run `uv run fantasm --help` for the full surface.

**Full fantasm reference: <https://acornaeology.github.io/fantasm/>** — the user guide covers every subcommand, the `fantasm.toml` schema, the version-graph workflows (the bit NFS uses heavily), and the importable `fantasm.api`. Reach for it before guessing.

### Disassembly driver

`versions/nfs-3.34/disassemble/disasm_nfs_334.py` — the main annotation file. Constructs a `dasmos.Disassembler` with `Disassembler.create(cpu='6502', ...)` and configures it with environments (`d.use_environment('acorn_mos')`), labels, constants, subroutine descriptions, comments, and relocated code blocks via the dasmos driver API (`d.label()`, `d.constant()`, `d.comment()`, `d.subroutine()`, `d.add_move()`, `d.hook_subroutine()`, `d.entry()`, `d.rts_code_ptr()`, `d.format_hint()`). Disassembly is finalised with `ir = d.disassemble()` and rendered via `ir.render('beebasm')` / `ir.render('json')`. This is where most development work happens. Run the driver directly with `uv run python <driver-path>` to regenerate `.asm` and `.json` outputs. Full driver-API guide: <https://acornaeology.github.io/dasmos/driver_api.html>.

**`index_base` / `index_region` vs `label` (dasmos 2.0+).** dasmos classifies each cross-reference as a *direct* access (`lda addr`) or an *indexing base* (`lda addr,X`, where the byte touched is `addr+X` and the base byte itself is never read/written). For a **data** address touched *only* as an indexing base (its xref reads "used as index base N times" with no "referenced" — a 256-byte table, a channel-indexed parallel array, a copy-loop source/dest base), use `d.index_base(addr, name, description=…, group=…, length=…)` instead of `d.label(…)`: it keeps the name/description/group/length so the `,X` operand still resolves and stays documented, sets `access='indexed_base'` itself (drop any `access='rw'/'r'/'w'`), keeps the base off the fixed-location memory map, and lists it under the JSON `index_bases` section. When several bases cluster just below a named anchor, `d.index_region(anchor, name, window=(lo, hi), …)` renders in-window neighbours as `anchor±k,X` instead of a hand-written label per slot (windows must be disjoint; an explicit `label()` inside a window wins).

**Finding candidates.** `fantasm labels list <VER> --index-base-only` (fantasm 0.17.2+) lists every label whose references are *exclusively* indexing bases — the exact `d.index_base()` candidate set — with `Direct`/`Idx` counts and a `Code` column flagging code items. This covers ROM data tables (dispatch address-table halves, `error_msg_table`, templates, lookup tables — the memo's headline case) as well as RAM/ZP scratch. Two blind spots to compensate for by hand: (1) it *under*-reports low-page (zero-page / page 0–2) bases because dasmos's schema-v2 `references[]` doesn't carry their kind — dasmos's own `.asm` xref ("used as index base") is authoritative there, so grep the `.asm` for those; (2) the `Code` flag *misses relocated-code entries* — a moved block's code item lives at its move *source* address, so a `d.entry()`/`add_move` destination shows `Code` blank even though it is a live entry point (e.g. `tube_page6_start` at `&0600`, written by the copy loop as `sta …,Y`). Always also exclude `d.entry()` targets.

**What to convert / leave.** Convert genuine `d.label()` **data** index-bases — RAM/ZP scratch *and* ROM data tables. **Leave:** any `type='code'` item and any `d.entry()` target (the code-label caveat — converting one moves a live entry point off the map); `d.subroutine()` data-*banner* regions (the banner's title/structure is deliberate — index_base would strip it); and auto-generated (`l####`) / environment labels (no `d.label()` to convert). There is no substitute for reading the label and its usage before converting — the name and inline comments usually state whether it is a table/template (data) or an entry/handler (code). `index_base`/`index_region` are annotation-only and never change emitted bytes — verify must still pass byte-identically.

### Lint

`uv run fantasm lint <VER> <DRIVER_PATH>` — validates that every `comment()`, `subroutine()`, and `label()` address in a driver script corresponds to a valid address in the dasmos JSON output (items, external labels, or subroutines). Catches stale addresses carried over during auto-generation of new version driver scripts. Also validates `address_links` and `glossary_links` in each version's `rom.json`.

### Verification

`uv run fantasm verify <VER>` — assembles the generated `.asm` with beebasm and does a byte-for-byte comparison against the original ROM.

### Correlation tools

`versions/nfs-3.34/disassemble/correlate_nfs.py` and `label_correspondence.py` — cross-reference auto-generated labels against DNFS 3.60 reference source using opcode fingerprinting. Used to find meaningful label names for auto-generated ones.

### Version layout

Each ROM version lives under `versions/<prefix>-<version>/` where prefix is `nfs` or `anfs` (e.g. `versions/nfs-3.34/`, `versions/anfs-4.08.53/`). Subdirectories:
- `rom/` — original ROM binary and metadata (`rom.json` with hashes)
- `disassemble/` — dasmos driver script and correlation tools
- `output/` — generated assembly (`.asm`) and structured data (`.json`)

Version IDs in `acornaeology.json` and CLI arguments are bare numbers (`3.34`, `4.08.53`). fantasm and the project's own scripts resolve a version ID to its prefixed directory by probing for `anfs-{id}` then `nfs-{id}`.

### Glossary

`GLOSSARY.md` — project-level glossary of Acorn-specific terms, registered in `acornaeology.json` as `"glossary": "GLOSSARY.md"`. Uses Markdown definition-list syntax with a brief/extended split:

```markdown
**TERM** (Expansion)
: Brief definition — one or two sentences. What the term IS.

  Extended detail — how NFS uses it, implementation specifics,
  or additional context. Shown only on the glossary page.
```

First paragraph = brief (tooltip text). Subsequent indented paragraphs after a blank line = extended (glossary page only). Entries without extended detail keep a single paragraph.

### Documentation links in `rom.json`

Each version's `rom/rom.json` has a `docs` array. Each doc entry can have:

- `address_links` — maps hex address patterns in Markdown to disassembly addresses (validated by lint against the JSON output)
- `glossary_links` — maps term patterns in Markdown to glossary entries (validated by lint against `GLOSSARY.md`)

Both use the same shape: `{"pattern": "...", "occurrence": 0, "term"|"address": "..."}`. The `occurrence` field is a 0-based index among all substring matches of the pattern.

### Disassembly guide

`DISASSEMBLY.md` — comprehensive development guide covering the full workflow for producing a new version disassembly, CLI tool reference, dasmos driver-API conventions, annotation guidelines, audit methodology, and common gotchas.

## Key technical context

- NFS ROM base address: 0x8000, size: 8192 bytes (standard BBC Micro sideways ROM)
- ANFS ROM base address: 0x8000, size: 16384 bytes (16KB sideways ROM)
- The ROM contains relocated code blocks (copied to pages 0x04-0x06 and zero page at runtime), handled via dasmos `d.add_move(dest, src, length)` calls
- Disassembler is [dasmos](https://acornaeology.github.io/dasmos/) (PyPI `dasmos>=4.0.0`; needs `fantasm>=0.18.0` to parse its schema-versioned JSON — `meta.schema_version` 4 — and surface index-base candidates); local source-of-truth checkout at `/Users/rjs/Code/acornaeology/dasmos/`. dasmos 4 renders string exprs like `<(label-1)` through its expression AST as `<(label - 1)` (spaced operators, byte-identical); `d.expr()` still accepts the legacy string form, and `access="rw"` still maps onto the new orthogonal R/W/B access flags. **Operand-override convention:** write `d.expr()` operands with the validated DSL — `from dasmos.expr import sym, lo, hi`, e.g. `d.expr(addr, lo(sym("label") - 1))`, `d.expr(addr, sym("a") - sym("b"))` — so a stale symbol errors at build time (`d.expr_label()` stays a string; a `(...) AND &FF` mask stays a string). **Memory-map convention:** every mapped `d.label()`/`d.index_base()` (any carrying `description`/`length`/`access`) needs a `group=` — `zero_page`, `stack`, `ram_workspace`, `hazel`, `mmio`, `ext_vectors`, `idx_base` — and each group needs a one-line entry in the version's rom.json `memory_map_groups` legend, or dasmos warns it can't place the row (dasmos#43)
- Assembly output targets beebasm syntax (renderer keyword: `'beebasm'`). Every driver renders with `char_literal_style="quote"` and `show_char_comment_hint=False`. **Character-literal convention:** where an immediate operand byte genuinely holds an ASCII character (a compare/load/test against a real character in command / filename / number / argument parsing), mark it with `d.char_literal(<operand-byte addr>)` so it renders `#'x'` instead of a bare hex byte. Judge each site from its inline comment — *leave* control-register values (CR1/CR2), bit masks and flags, workspace/table offsets, error/status codes, install-address bytes, and self-modifying opcode bytes as hex even when their value falls in the printable range. `char_literal` is annotation-only (verify stays byte-identical). Propagate across the version graph with `propagate_char.py` (keys on value+comment) and hand-review the residue
- Assembly comments are formatted to fit within 62 characters
