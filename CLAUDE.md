# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Annotated disassembly of Acorn NFS (Network Filing System) ROMs for BBC Micro. Python scripts drive py8dis (a programmable 6502 disassembler) to produce readable, verified assembly output from the original 8KB ROM binaries. Versions covered: 3.34, 3.34B, and 3.35D.

## Build commands

Requires [uv](https://docs.astral.sh/uv/) and [beebasm](https://github.com/stardot/beebasm) (v1.10+).

```sh
uv sync                            # Install dependencies
uv run acorn-nfs-disasm-tool disassemble 3.34  # Generate .asm and .json from ROM
uv run acorn-nfs-disasm-tool lint 3.34         # Validate annotation addresses
uv run acorn-nfs-disasm-tool verify 3.34       # Reassemble and byte-compare against original ROM
```

Verification is the primary correctness check: the generated assembly must reassemble to a byte-identical copy of the original ROM. Lint validates that all annotation addresses (comments, subroutines, labels) reference valid item addresses in the py8dis output — catching stale addresses carried over from other versions. CI runs `disassemble`, `lint`, then `verify` on every push.

## Architecture

### CLI entry point

`src/disasm_tools/cli.py` — subcommands: `disassemble`, `correlate`, `verify`, `lint`, `compare`. Sets env vars `ACORN_NFS_ROM` and `ACORN_NFS_OUTPUT` before invoking version-specific scripts.

### Disassembly driver

`versions/3.34/disassemble/disasm_nfs_334.py` — the main annotation file (~3,600 lines). Configures py8dis with labels, constants, subroutine descriptions, comments, and relocated code blocks using py8dis's DSL (`label()`, `constant()`, `comment()`, `subroutine()`, `move()`, `hook_subroutine()`). This is where most development work happens.

### Lint

`src/disasm_tools/lint.py` — validates that every `comment()`, `subroutine()`, and `label()` address in a driver script corresponds to a valid address in the py8dis JSON output (items, external labels, or subroutines). Catches stale addresses carried over during auto-generation of new version driver scripts. Also validates `address_links` and `glossary_links` in each version's `rom.json`.

### Verification

`src/disasm_tools/verify.py` — assembles the generated `.asm` with beebasm and does a byte-for-byte comparison against the original ROM.

### Correlation tools

`versions/3.34/disassemble/correlate_nfs.py` and `label_correspondence.py` — cross-reference auto-generated labels against DNFS 3.60 reference source using opcode fingerprinting. Used to find meaningful label names for auto-generated ones.

### Version layout

Each ROM version lives under `versions/<version>/` with subdirectories:
- `rom/` — original ROM binary and metadata (`rom.json` with hashes)
- `disassemble/` — py8dis driver script and correlation tools
- `output/` — generated assembly (`.asm`) and structured data (`.json`)

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

- ROM base address: 0x8000, size: 8192 bytes (standard BBC Micro sideways ROM)
- The ROM contains relocated code blocks (copied to pages 0x04-0x06 and zero page at runtime), handled via py8dis `move()` calls
- py8dis dependency is a custom fork at `github.com/acornaeology/py8dis`
- Assembly output targets beebasm syntax
- Assembly comments are formatted to fit within 62 characters
