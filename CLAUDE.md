# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Annotated disassembly of Acorn NFS and ANFS (Network Filing System / Advanced Network Filing System) ROMs for BBC Micro. Python scripts drive py8dis (a programmable 6502 disassembler) to produce readable, verified assembly output from the original ROM binaries. Versions covered: NFS 3.34, 3.34B, 3.35D, 3.35K, 3.40, 3.60, 3.62, 3.65; ANFS 4.08.53.

## Build commands

Requires [uv](https://docs.astral.sh/uv/) and [beebasm](https://github.com/stardot/beebasm) (v1.10+).

```sh
uv sync                                                                       # Install dependencies (incl. fantasm)
uv run fantasm disassemble 3.34                                               # Run py8dis driver via fantasm (sets FANTASM_ROM / FANTASM_OUTPUT_DIR)
uv run fantasm lint 3.34 versions/nfs-3.34/disassemble/disasm_nfs_334.py     # Validate annotation addresses
uv run fantasm verify 3.34                                                    # Reassemble and byte-compare against original ROM
```

Verification is the primary correctness check: the generated assembly must reassemble to a byte-identical copy of the original ROM. Lint validates that all annotation addresses (comments, subroutines, labels) reference valid item addresses in the py8dis output — catching stale addresses carried over from other versions. CI runs `fantasm disassemble`, then `fantasm lint`, then `fantasm verify` on every push.

## Architecture

### CLI: fantasm

The general-purpose 6502 disassembly tooling lives in the [fantasm](https://pypi.org/project/fantasm/) package, declared as a regular project dependency in `pyproject.toml`. Subcommands include `verify`, `lint`, `compare`, `asm extract`, `audit summary|detail|undeclared`, `cfg depth|leaves|roots|sub`, `sub insert`, `comments check`, `backfill`, and `promote`. Run `uv run fantasm --help` for the full surface.

### Disassembly driver

`versions/nfs-3.34/disassemble/disasm_nfs_334.py` — the main annotation file (~3,600 lines). Configures py8dis with labels, constants, subroutine descriptions, comments, and relocated code blocks using py8dis's DSL (`label()`, `constant()`, `comment()`, `subroutine()`, `move()`, `hook_subroutine()`). This is where most development work happens. Run the driver directly with `uv run python <driver-path>` to regenerate `.asm` and `.json` outputs.

### Lint

`uv run fantasm lint <VER> <DRIVER_PATH>` — validates that every `comment()`, `subroutine()`, and `label()` address in a driver script corresponds to a valid address in the py8dis JSON output (items, external labels, or subroutines). Catches stale addresses carried over during auto-generation of new version driver scripts. Also validates `address_links` and `glossary_links` in each version's `rom.json`.

### Verification

`uv run fantasm verify <VER>` — assembles the generated `.asm` with beebasm and does a byte-for-byte comparison against the original ROM.

### Correlation tools

`versions/nfs-3.34/disassemble/correlate_nfs.py` and `label_correspondence.py` — cross-reference auto-generated labels against DNFS 3.60 reference source using opcode fingerprinting. Used to find meaningful label names for auto-generated ones.

### Version layout

Each ROM version lives under `versions/<prefix>-<version>/` where prefix is `nfs` or `anfs` (e.g. `versions/nfs-3.34/`, `versions/anfs-4.08.53/`). Subdirectories:
- `rom/` — original ROM binary and metadata (`rom.json` with hashes)
- `disassemble/` — py8dis driver script and correlation tools
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

`DISASSEMBLY.md` — comprehensive development guide covering the full workflow for producing a new version disassembly, CLI tool reference, py8dis DSL conventions, annotation guidelines, audit methodology, and common gotchas.

## Key technical context

- NFS ROM base address: 0x8000, size: 8192 bytes (standard BBC Micro sideways ROM)
- ANFS ROM base address: 0x8000, size: 16384 bytes (16KB sideways ROM)
- The ROM contains relocated code blocks (copied to pages 0x04-0x06 and zero page at runtime), handled via py8dis `move()` calls
- py8dis dependency is a custom fork at `github.com/acornaeology/py8dis`
- Assembly output targets beebasm syntax
- Assembly comments are formatted to fit within 62 characters
