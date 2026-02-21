# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Annotated disassembly of Acorn NFS (Network Filing System) ROM v3.34 for BBC Micro. A Python script drives py8dis (a programmable 6502 disassembler) to produce readable, verified assembly output from the original 8KB ROM binary.

## Build commands

Requires [uv](https://docs.astral.sh/uv/) and [beebasm](https://github.com/stardot/beebasm) (v1.10+).

```sh
uv sync                            # Install dependencies
uv run acorn-nfs disassemble 3.34  # Generate .asm and .json from ROM
uv run acorn-nfs verify 3.34       # Reassemble and byte-compare against original ROM
```

Verification is the primary correctness check: the generated assembly must reassemble to a byte-identical copy of the original ROM. CI runs both `disassemble` then `verify` on every push.

## Architecture

### CLI entry point

`src/acorn_nfs/cli.py` — three subcommands: `disassemble`, `correlate`, `verify`. Sets env vars `ACORN_NFS_ROM` and `ACORN_NFS_OUTPUT` before invoking version-specific scripts.

### Disassembly driver

`versions/3.34/disassemble/nfs_334_v2.py` — the main annotation file (~3,600 lines). Configures py8dis with labels, constants, subroutine descriptions, comments, and relocated code blocks using py8dis's DSL (`label()`, `constant()`, `comment()`, `subroutine()`, `move()`, `hook_subroutine()`). This is where most development work happens.

### Verification

`src/acorn_nfs/verify.py` — assembles the generated `.asm` with beebasm and does a byte-for-byte comparison against the original ROM.

### Correlation tools

`versions/3.34/disassemble/correlate_nfs.py` and `label_correspondence.py` — cross-reference auto-generated labels against DNFS 3.60 reference source using opcode fingerprinting. Used to find meaningful label names for auto-generated ones.

### Version layout

Each ROM version lives under `versions/<version>/` with subdirectories:
- `rom/` — original ROM binary and metadata (`rom.json` with hashes)
- `disassemble/` — py8dis driver script and correlation tools
- `output/` — generated assembly (`.asm`) and structured data (`.json`)

## Key technical context

- ROM base address: 0x8000, size: 8192 bytes (standard BBC Micro sideways ROM)
- The ROM contains relocated code blocks (copied to pages 0x04-0x06 and zero page at runtime), handled via py8dis `move()` calls
- py8dis dependency is a custom fork at `github.com/acornaeology/py8dis`
- Assembly output targets beebasm syntax
- Assembly comments are formatted to fit within 62 characters
