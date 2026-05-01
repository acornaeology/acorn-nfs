# Disassembly Guide

How to produce annotated, verified disassemblies of new Acorn NFS ROM versions and maintain annotation quality. Based on experience with NFS 3.34, 3.34B, 3.35D, and 3.35K.

For project overview and build instructions, see [README.md](README.md). For architecture details, see [CLAUDE.md](CLAUDE.md). For Acorn-specific terminology, see [GLOSSARY.md](GLOSSARY.md).


## Prerequisites

- [uv](https://docs.astral.sh/uv/) for Python dependency management
- [beebasm](https://github.com/stardot/beebasm) (v1.10+) for assembly verification
- The ROM binary (8192 bytes) for the version being disassembled
- MD5 and SHA-256 hashes of the ROM (`md5 <rom>`, `shasum -a 256 <rom>`)
- An existing disassembly of the nearest version to use as a base


## Quick reference: CLI tools

The general-purpose disassembly tooling is provided by [fantasm](https://acornaeology.github.io/fantasm/), invoked via `uv run fantasm <command>`. The command-by-command reference is at <https://acornaeology.github.io/fantasm/cli.html>; the workflow guide at <https://acornaeology.github.io/fantasm/workflows.html> covers cross-version patterns NFS uses heavily (`backfill`, `annotations diff`, `addresses map`).

| Command | Description | Example |
|---------|-------------|---------|
| `fantasm disassemble` | Run py8dis driver to generate `.asm` and `.json` | `uv run fantasm disassemble 3.34` |
| `fantasm verify` | Reassemble and byte-compare against original ROM | `uv run fantasm verify 3.34` |
| `fantasm lint` | Validate annotation addresses in driver script | `uv run fantasm lint 3.34 versions/nfs-3.34/disassemble/disasm_nfs_334.py` |
| `fantasm compare` | Compare two ROM versions (byte and opcode level) | `uv run fantasm compare 3.34 3.34B` |
| `fantasm asm extract` | Extract assembly section by address range or label | `uv run fantasm asm extract 3.34 &8069 &809E` |
| `fantasm audit summary` | Subroutine annotation summary | `uv run fantasm audit summary 3.34` |
| `fantasm audit detail` | Detail report for a single subroutine | `uv run fantasm audit detail 3.34 prepare_fs_cmd` |
| `fantasm audit undeclared` | List JSR targets without `subroutine()` declarations | `uv run fantasm audit undeclared 3.34` |

The `asm extract` command accepts hex addresses in multiple formats (`&80EA`, `$80EA`, `0x80EA`) as well as label names. Cross-referencing labels against DNFS 3.60 source is handled by the per-version correlation scripts under `versions/nfs-3.34/disassemble/`.


## Producing a new version disassembly

### Step 1: Directory structure

Create the version directory tree:

```
versions/<VER>/
  rom/
    nfs-<VER>.rom          # The ROM binary
    rom.json               # Metadata: title, size, md5, sha256, docs
  disassemble/
    __init__.py            # Empty
    disasm_nfs_<ver>.py    # Driver script (lowercase, dots removed)
  output/                  # Generated .asm and .json go here
```

Update `acornaeology.json` to add the new version to the versions array.

Naming convention: version "3.35D" becomes script `disasm_nfs_335d.py` and ROM `nfs-3.35D.rom`.

### Step 2: Run initial comparison

```sh
uv run fantasm compare <BASE> <NEW>
```

This gives similarity statistics. Key thresholds:

- **>95% opcode similarity**: Simple offset-based transformation works (e.g. 3.34 to 3.34B: 98.7%, uniform +1 shift)
- **80-95% opcode similarity**: Need SequenceMatcher-based address mapping (e.g. 3.34B to 3.35D: 87.4%, non-uniform shifts)
- **<80% opcode similarity**: May need a more manual approach

### Step 3: Build address map and generate driver script

Use `generate_335d.py` in the project root as a template. The key functions:

**`disassemble_to_opcodes(data)`** — Linear sweep of the ROM, extracting (offset, opcode, instruction_length) tuples using the 6502 opcode length table.

**`build_address_map(data_a, data_b)`** — Uses `difflib.SequenceMatcher` on the opcode sequences (ignoring operands) to find matching regions. For each matched instruction pair, maps `ROM_BASE + offset_a` to `ROM_BASE + offset_b`.

**`build_relocated_address_map(data_a, data_b, src_a, src_b, dest, length)`** — Same approach for relocated code blocks. The ROM source addresses differ between versions but the runtime destination is the same.

**`transform_script(script_text, addr_map)`** — Parses the base driver script and transforms all address-bearing calls:

- `label(0xADDR, ...)`, `subroutine(0xADDR, ...)`, `comment(0xADDR, ...)`, `entry(0xADDR)`, `hook_subroutine(0xADDR, ...)`, `rts_code_ptr(0xADDR, ...)` — address is mapped
- `move(dest, src, length)` — source address needs manual updating
- `constant(...)` — NOT mapped (these are symbolic values, not ROM addresses)
- `for addr in [...]` loops — all hex values in the list are mapped

Unmapped addresses get an `# UNMAPPED:` prefix. The `group_logical_statements()` function handles multi-line calls (open parentheses).

#### Identity mappings

Add identity mappings for addresses that exist in both versions unchanged:

- RAM workspace: &0000-&00FF, &0D00-&0FFF
- Dispatch tables that are data: &8015-&806A (check this per version)

#### Relocated block sources

The `move()` calls need manual updating. Find new source addresses by examining the ROM init code:

- Find `init_vectors_and_copy` in the new ROM
- The page copy loop shows LDA with the high byte of the ROM source
- Alternatively, compute from the offset: if main ROM code grew by N bytes, relocated block sources shift by the same N bytes

### Step 4: Fix errors iteratively

Run:

```sh
uv run fantasm disassemble <VER>
uv run fantasm verify <VER>
```

#### py8dis AssertionError: "Nothing loaded at address 0xNNNN"

An `entry()` points to an address at the ROM boundary where the instruction would extend past the end. Comment out the entry and its label.

Example: `entry(0x9FFA)` where the 3-byte instruction at &9FFF would need bytes at &A000+.

#### beebasm "Duplicate label" errors

py8dis auto-generates `return_1`, `return_2`, etc. for RTS instructions. If the same auto-label appears in both main ROM and relocated code, beebasm reports a duplicate. Fix by adding explicit labels at one of the conflicting addresses:

```python
label(0x8555, "return_4")
label(0x8D5A, "return_5")
```

Check for this pattern by searching the generated `.asm` for the duplicate label.

#### Misaddressed annotations

The SequenceMatcher address map is approximately as accurate as the opcode similarity percentage. Many `subroutine()`, `comment()`, and `label()` calls will have stale base-version addresses. Two approaches:

1. **Bulk fix using address map** (preferred for many errors): Reuse `build_address_map()` to programmatically scan the driver script for addresses in the base version's address space but not in the new version's.

2. **Opcode fingerprinting** (for individual routines): Extract 4-8 bytes of the base version's code at the old address and search for that byte pattern in the new ROM. Short opcode sequences are usually unique enough to identify the correct new address.

#### UNMAPPED lines

Lines marked `# UNMAPPED:` are from the base version where the code was deleted or reorganised beyond SequenceMatcher's ability to match. For each:

- Check if the code exists elsewhere in the new ROM (relocated, not deleted)
- If deleted, remove the annotation
- If it's a subroutine description, check if the routine still exists at a different address using opcode fingerprinting

### Step 5: Annotate new code

Use the comparison output to identify inserted code blocks. For each, use `asm extract` to examine the assembly:

```sh
uv run fantasm asm extract <VER> &80EA &8120
```

What to annotate:

- **Labels** for new entry points, subroutines, and data tables
- **`subroutine()`** descriptions: what it does, calling convention (registers in/out), side effects
- **`comment()`** for non-obvious instructions or algorithm explanations
- **`constant()`** for magic numbers (Tube registers, OSBYTE numbers, etc.)

Focus on subroutine descriptions that explain:
1. Purpose: what the routine does
2. Entry conditions: register values, memory state
3. Exit conditions: what's returned, what's preserved
4. Side effects


## py8dis driver script reference

The driver script configures py8dis using a Python DSL. Each call annotates the disassembly output.

### Core DSL calls

**`label(address, name)`** — Assign a symbolic name to a ROM or RAM address. The name appears in the assembly output wherever that address is referenced.

**`constant(name, value)`** — Define a named constant for a numeric value. Used for OSBYTE numbers, hardware register addresses, and other magic numbers. The value is symbolic, not a ROM address — do not transform it during address mapping.

**`comment(address, text)`** — Attach a comment to a specific instruction address. Appears as a `; comment` in the assembly output. Multiple `comment()` calls at the same address are concatenated.

**`subroutine(address, title, description)`** — Mark the start of a subroutine with a title and description. The title is a short summary (one line). The description is a longer explanation of behaviour, calling convention, and side effects.

**`entry(address)`** — Mark an address as a code entry point. Ensures py8dis disassembles from this address rather than treating it as data.

**`move(dest, source, length)`** — Declare a relocated code block. The ROM contains code at `source` that is copied to `dest` at runtime. py8dis disassembles it using `dest` addresses.

**`hook_subroutine(address, hook_function)`** — Register a custom Python function that py8dis calls when it encounters this subroutine during disassembly. Used for special handling of dispatch tables, inline data, etc.

**`rts_code_ptr(lo_address, hi_address, count)`** — Declare a split lo/hi byte address table used for PHA/PHA/RTS dispatch. Addresses in the table are stored minus 1 (the 6502 RTS convention).

### Calling convention format

Subroutine descriptions use a structured format for entry and exit conditions:

```python
subroutine(0x8350, "Prepare FS command",
    """Parse and validate a filing system command string.

    On entry:
      (text_ptr),Y points to the command string
    On exit:
      A = command number
      C clear if valid, set if error
    """)
```

### Relocated code handling

The ROM contains blocks that are copied to lower RAM at runtime (pages &04-&06 and zero page workspace). These are declared with `move()`:

```python
move(0x0400, 0x9D4A, 0x0300)  # Copy &0300 bytes from ROM &9D4A to RAM &0400
```

Annotations for relocated code reference the runtime address (the `dest`), not the ROM source address.


## Annotation guidelines

### Subroutine descriptions

A good subroutine description:

- **Title**: A standalone phrase or short sentence summarising the routine's purpose. Not a sentence fragment that runs into the description.
- **Description**: Explains behaviour, entry/exit conditions, and side effects. Written as complete sentences.
- **Calling convention**: Uses `On entry:` and `On exit:` blocks with indented register/flag details.

### Comment length

Assembly comments are formatted to fit within 62 characters. This is a py8dis formatting constraint. For longer explanations, use multiple `comment()` calls at the same address (they are concatenated with line breaks) or put the detail in the `subroutine()` description.

### Hex notation

- Use **Acorn notation** (`&XXXX`) in documentation, Markdown files, and human-readable output
- Use **Python notation** (`0xXXXX`) in Python scripts (driver scripts, tools)

### Tips for annotating new code

- Don't try to annotate the entire assembly in one pass — focus on new and changed code
- For complex new code, write the `subroutine()` description as a block comment and add per-instruction `comment()` calls for the tricky parts
- Cross-reference with the base version's annotations — if a routine moved but didn't change, the base version's annotations are still correct
- Build ad-hoc tools for repetitive work: scripts that search for patterns, extract byte sequences, compare specific regions


## Auditing annotations

The audit tool systematically verifies subroutine boundaries, descriptions, and control flow. It analyses the JSON output (not the driver script) so it reflects the actual disassembler output.

### Summary mode

```sh
uv run fantasm audit summary <VER>
```

Shows all subroutines with computed flags:

```
ADDR    NAME                             END       ITEMS  FLAGS
&8069   dispatch_net_cmd                 FALL→       9/0  BRANCH_ESCAPE,FALL_THROUGH,NO_REFS
&809F   dispatch                         RTS        10/0
...
176 subroutines: 53 RTS, 47 JMP, 75 fall-through
Flags: 69 BRANCH_ESCAPE, 6 DATA_ONLY, 73 FALL_THROUGH, 28 FALL_THROUGH_ENTRY, 47 NO_REFS
```

### Detail mode

Full report for a single subroutine, including description, extent, caller references, escaping branches, and the assembly listing:

```sh
uv run fantasm audit detail <VER> prepare_fs_cmd
uv run fantasm audit detail <VER> 0x8350
uv run fantasm audit detail <VER> '&8350'
```

The detail view shows everything needed to verify a description: the code itself, who calls it, what it falls through to, and which branches escape.

### Flag filter mode

Filter the summary to show only subroutines with a specific flag:

```sh
uv run fantasm audit summary <VER> --flag FALL_THROUGH_ENTRY
```

### Audit flags

| Flag | Meaning | What to check |
|------|---------|---------------|
| `FALL_THROUGH` | Last item before next sub isn't RTS/JMP/BRK/RTI | Is the fall-through intentional and documented? |
| `FALL_THROUGH_ENTRY` | Predecessor falls through AND no JSR/JMP/branch refs | Is this genuinely only reachable via fall-through? |
| `NO_REFS` | Predecessor terminates but no refs found anywhere | Likely called indirectly (dispatch table, vector, NMI). Verify the description explains how it's reached. |
| `BRANCH_ESCAPE` | A conditional branch targets outside the sub's extent | Is the branch target correct? Is it documented? |
| `DATA_ONLY` | All items are byte/string, zero code | Is this correctly marked as data, not a mis-disassembly? |
| `AUTO_NAME` | Name matches `sub_c*` pattern | Needs a meaningful name. |
| `NO_DESCRIPTION` | Missing or very short title and description | Needs annotation work. |

### Recommended audit workflow

1. Run `audit summary` to see flag counts and plan the work
2. Pick the smallest unreviewed flag category
3. For each subroutine in the category, run `audit detail` to read the description and code
4. Fix any issues in the driver script, then re-run the driver and verify
5. Track progress so you can interrupt and resume across sessions
6. After all flagged subroutines, check unflagged ones (those with no flags at all)

Start with the smallest categories first. Many subroutines have multiple flags, so categories overlap — check for already-reviewed subroutines before re-auditing.

### Common issues found by auditing

- **Title/description split**: Title is a sentence fragment that continues into the description rather than being a standalone summary
- **Label mismatches**: Label name describes one thing, code does another
- **Undocumented fall-throughs**: Subroutine falls into the next one but the description doesn't mention it
- **Stale descriptions**: Description carried over from another version without updating for code changes


## Writing version comparison documents

Create `versions/<VER>/CHANGES-FROM-<BASE>.md` following the established format. See existing files for templates:

- `versions/3.34B/CHANGES-FROM-3.34.md`
- `versions/3.35D/CHANGES-FROM-3.34B.md`
- `versions/3.35K/CHANGES-FROM-3.35D.md`

### Document structure

1. **Summary statistics** from the comparison tool output
2. **ROM header** table comparing all header fields
3. **Numbered changes** — each functional difference with:
   - What changed (before/after table where appropriate)
   - Runtime addresses affected
   - Why it matters (functional significance)
4. **Address map** — key entry point mappings and offsets
5. **Relocated blocks table** — ROM sources and runtime addresses

Use Acorn hex notation (`&XXXX`) for all addresses in the document.

### Address links in rom.json

Update `versions/<VER>/rom/rom.json` with a `docs` section containing `address_links` for every `&XXXX` pattern in the CHANGES document. Each entry maps a specific occurrence (0-indexed) of a pattern to a version and address:

```json
{"pattern": "&80EA", "occurrence": 0, "version": "3.35D", "address": "0x80EA"}
```

Addresses that refer to the base version should use that version's identifier. Hardware registers (&FEE0-&FEE7) and MOS vectors (&FFC2, &FFC5) are skipped.

### Glossary links in rom.json

Similarly, `glossary_links` map term patterns to glossary entries:

```json
{"pattern": "Econet", "occurrence": 0, "term": "Econet"}
```

Both link types are validated by the lint tool in CI.


## Key gotchas

1. **Dispatch tables are data, not code.** The split lo/hi byte tables at &8020/&8044 contain addresses minus 1 (for PHA/PHA/RTS dispatch). Don't let the disassembler trace through them as code.

2. **Relocated code has two address spaces.** The ROM source address and the runtime address are different. py8dis `move()` handles this, but annotations need to reference the runtime address when discussing what the code does.

3. **The ROM is exactly 8192 bytes.** Code insertions must be balanced by deletions or compressions elsewhere. Check if the version string length changed, if any trailing data was trimmed, or if routines were compacted.

4. **py8dis auto-labels can collide.** Any `return_N`, `loop_cXXXX`, etc. that appears in both main ROM and relocated code will cause beebasm duplicate label errors. Fix by adding explicit labels.

5. **Context window management.** The full assembly output is 7000-8000 lines. Use `extract` to examine specific sections. Use search tools to find patterns. Work on one subroutine at a time rather than loading the full output.

6. **SequenceMatcher only matches opcodes, not operands.** Two instructions with the same opcode but different operands (e.g. LDA &1234 vs LDA &5678) will be marked as "equal" in the opcode sequence. This is correct for address mapping but means the map can produce false matches when code is reorganised at a fine grain.

7. **`constant()` doesn't take ROM addresses.** Constants are symbolic values (OSBYTE numbers, hardware register addresses, etc.) and should NOT have their values transformed by the address map.


## Tools reference

| Tool | Provided by | Purpose |
|------|-------------|---------|
| `fantasm verify` | fantasm | beebasm reassembly and byte comparison |
| `fantasm lint` | fantasm | Validate annotation addresses and doc links |
| `fantasm compare` | fantasm | Binary comparison with SequenceMatcher |
| `fantasm asm extract` | fantasm | Extract assembly sections by address or label |
| `fantasm audit` | fantasm | Subroutine annotation audit (flags, extents, refs) |
| `fantasm cfg` | fantasm | Call-graph queries (depth/leaves/roots/sub) |
| `fantasm.api.mos6502` | fantasm | 6502 / 65C02 instruction lengths and mnemonics |
| Generate script | `generate_335d.py` (project root) | Template for address mapping and script generation |
