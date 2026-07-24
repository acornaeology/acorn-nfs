#!/usr/bin/env python3
"""Generate the initial disasm_anfs_424.py by mapping addresses from
ANFS 4.21 (variant 1).

ANFS 4.24 is the next Master 128 ANFS after 4.21 (variant 1). Both are
65C02 builds with no relocated blocks (filing-system workspace lives in
HAZEL hidden RAM at &C000-&C2FF), so the transformation is a pure
opcode-level address remap of the closest sibling driver — no CPU change,
no dead runtime ranges, no move() calls to strip.

Compared with 4.21 (variant 1):
- The ROM title grew from "Acorn ANFS 4.21" to "Acorn ANFS 4.24"; the
  copyright ("(C)1986 Acorn") is unchanged.
- The service entry moved from &8A54 to &8A8A.
- 93.9% opcode-similar; scattered CLD insertions, new ACCCON save/restore
  sequences, and one small relocated routine (&88F0-&898C -> &863A-&863A).

This script applies SequenceMatcher + seed-and-extend to the 65C02 opcode
sequences of both ROMs to build a main-ROM address map, identity-maps zero
page and the &0D00-&10FF workspace, and rewrites the 4.21_variant_1 driver
script with the translated addresses. Lines whose addresses do not map are
prefixed `# UNMAPPED:` for manual review.
"""

import re
import sys
from pathlib import Path

from fantasm.api.blockmatch import build_full_address_map

# ============================================================
# Configuration
# ============================================================

ROM_BASE = 0x8000
ROM_SIZE = 16384

# Both 4.21_variant_1 and 4.24 are 65C02 (Master 128).
CPU_A = "65c02"
CPU_B = "65c02"

# 4.24 has the same runtime-address model as 4.21_variant_1: no relocated
# blocks, workspace in HAZEL. There are no dead ranges to strip.
DEAD_RANGES = []


def in_dead_range(addr):
    return any(lo <= addr <= hi for lo, hi in DEAD_RANGES)


# ============================================================
# Script transformation
# ============================================================


def group_logical_statements(lines):
    """Group lines into logical statements, tracking open parentheses.

    Returns list of (start_line_idx, end_line_idx_exclusive, lines_list).
    Multi-line function calls (where parens aren't balanced) are grouped
    together.
    """
    groups = []
    current_start = 0
    current_lines = []
    paren_depth = 0
    # String state is carried ACROSS lines so triple-quoted descriptions
    # (whose body lines may contain unbalanced parens) don't desync the
    # paren depth. `in_s` is the active string delimiter or None.
    in_s = None
    escaped = False

    for i, line in enumerate(lines):
        current_lines.append(line)

        j = 0
        n = len(line)
        while j < n:
            ch = line[j]
            if in_s is None:
                if ch == '#':
                    break  # rest of line is a comment
                if ch in ('"', "'"):
                    if line[j:j+3] in ('"""', "'''"):
                        in_s = line[j:j+3]
                        j += 3
                        continue
                    in_s = ch
                elif ch == '(':
                    paren_depth += 1
                elif ch == ')':
                    paren_depth -= 1
                j += 1
            else:
                # Inside a string: only look for the closing delimiter.
                # Parens here are never counted.
                if escaped:
                    escaped = False
                    j += 1
                    continue
                if ch == '\\' and len(in_s) == 1:
                    escaped = True
                    j += 1
                    continue
                if len(in_s) == 3 and line[j:j+3] == in_s:
                    in_s = None
                    j += 3
                    continue
                if len(in_s) == 1 and ch == in_s:
                    in_s = None
                j += 1

        # A statement ends only when parens are balanced AND we are not in
        # the middle of a multi-line (triple-quoted) string.
        if paren_depth <= 0 and in_s is None:
            paren_depth = 0
            groups.append((current_start, i + 1, current_lines))
            current_start = i + 1
            current_lines = []

    if current_lines:
        groups.append((current_start, current_start + len(current_lines),
                       current_lines))

    return groups


def transform_script(script_text, addr_map):
    """Transform the 4.21_variant_1 script to 4.24 by mapping addresses."""
    lines = script_text.split('\n')
    hex_addr_pattern = re.compile(r'0x([0-9A-Fa-f]{2,5})')

    # The driver calls these as methods on the disassembler instance, e.g.
    # `d.comment(0x8123, ...)`. Match an optional `d.` prefix.
    addr_first_funcs = ['label', 'entry', 'subroutine', 'comment',
                        'hook_subroutine', 'rts_code_ptr', 'index_base',
                        'index_region', 'format_hint', 'char_literal',
                        'inkey_code', 'banner']
    pfx = r'(?:d\.)?'

    groups = group_logical_statements(lines)
    output_lines = []

    text_replacements = [
        ('anfs-4.21_variant_1', 'anfs-4.24'),
        ('ANFS 4.21 (variant 1)', 'ANFS 4.24'),
        ('ANFS 4.21', 'ANFS 4.24'),
    ]

    def apply_text_replacements(s):
        for old, new in text_replacements:
            s = s.replace(old, new)
        return s

    for start_idx, end_idx, group_lines in groups:
        first_line = group_lines[0]
        stripped = first_line.strip()

        if stripped.startswith('#') or stripped == '':
            for gl in group_lines:
                output_lines.append(apply_text_replacements(gl))
            continue

        group_lines = [apply_text_replacements(gl) for gl in group_lines]
        first_line = group_lines[0]
        stripped = first_line.strip()

        # move() calls: 4.24 has no relocated blocks (none expected in the
        # 4.21_variant_1 base, but keep the guard for safety).
        if re.match(rf'{pfx}(?:move|add_move)\(', stripped):
            for gl in group_lines:
                output_lines.append('# UNMAPPED (no relocated blocks): ' + gl)
            continue

        # Constants are symbolic; never map.
        if re.match(rf'{pfx}constant\(', stripped):
            output_lines.extend(group_lines)
            continue

        # byte()/word() calls: map address
        if re.match(rf'{pfx}(?:byte|word)\(', stripped):
            m = re.match(rf'^(\s*{pfx}(?:byte|word)\()0x([0-9A-Fa-f]+)(.*)',
                         first_line)
            if m:
                prefix, addr_hex, rest = m.groups()
                addr = int(addr_hex, 16)
                if addr in addr_map:
                    group_lines[0] = f'{prefix}0x{addr_map[addr]:04X}{rest}'
                    output_lines.extend(group_lines)
                else:
                    for gl in group_lines:
                        output_lines.append('# UNMAPPED: ' + gl)
            else:
                output_lines.extend(group_lines)
            continue

        # Address-bearing function calls
        is_addr_func = False
        for func_name in addr_first_funcs:
            if re.match(rf'{pfx}{func_name}\(', stripped):
                is_addr_func = True
                # The leading address may be on the first line (single-line
                # call) or on a following line (multi-line call where the
                # `(` opens on line 0 and `0xADDR,` is on line 1). Find the
                # first hex literal in the code portion of the group and map
                # only that one — the subject address. Any further hex
                # literals belong to description/comment text and stay put.
                target_line_idx = None
                for li, gl in enumerate(group_lines):
                    code_part = gl.partition('#')[0]
                    if re.search(r'0x[0-9A-Fa-f]+', code_part):
                        target_line_idx = li
                        break
                if target_line_idx is None:
                    output_lines.extend(group_lines)
                    break
                m = re.search(r'0x([0-9A-Fa-f]+)',
                              group_lines[target_line_idx].partition('#')[0])
                addr = int(m.group(1), 16)
                if addr in addr_map:
                    new_addr = addr_map[addr]
                    code_part, sep, comment_part = \
                        group_lines[target_line_idx].partition('#')
                    code_part = re.sub(r'0x[0-9A-Fa-f]+',
                                       f'0x{new_addr:04X}', code_part, count=1)
                    group_lines[target_line_idx] = code_part + sep + comment_part
                    output_lines.extend(group_lines)
                else:
                    for gl in group_lines:
                        output_lines.append('# UNMAPPED: ' + gl)
                break

        if is_addr_func:
            continue

        # Catch-all: any other statement that contains hex addresses (e.g.
        # `_cmd_entries = [(0xA3F6, "cmd_close"), ...]`, for-loop iterables,
        # range() limits) — map every hex literal. If any address can't be
        # mapped, mark the whole statement UNMAPPED.
        joined = '\n'.join(group_lines)
        joined_no_comments = re.sub(r'#.*', '', joined)
        addrs_in_statement = []
        for m in hex_addr_pattern.finditer(joined_no_comments):
            try:
                addrs_in_statement.append(int(m.group(1), 16))
            except ValueError:
                pass

        if addrs_in_statement:
            unmappable = [a for a in addrs_in_statement
                          if a not in addr_map]
            if unmappable:
                for gl in group_lines:
                    output_lines.append('# UNMAPPED: ' + gl)
                continue

            def map_hex_literal(match):
                addr = int(match.group(1), 16)
                if addr in addr_map:
                    return f'0x{addr_map[addr]:04X}'
                return f'0x{addr:04X}'

            # Map only the code part of each line (preserve comments verbatim).
            mapped_lines = []
            for gl in group_lines:
                code_part, sep, comment_part = gl.partition('#')
                code_mapped = hex_addr_pattern.sub(map_hex_literal, code_part)
                mapped_lines.append(code_mapped + sep + comment_part)
            output_lines.extend(mapped_lines)
            continue

        output_lines.extend(group_lines)

    # Post-process for-loops: if any body line is UNMAPPED, UNMAP the whole
    # loop; if the for-header is UNMAPPED, UNMAP the body.
    def is_for_header(line):
        s = line.strip()
        return s.startswith('for ') and s.endswith(':')

    def is_unmapped(line):
        return line.lstrip().startswith('# UNMAPPED')

    # Pass (a): UNMAPPED for-line -> UNMAP body
    pass_a = []
    i = 0
    while i < len(output_lines):
        line = output_lines[i]
        if is_unmapped(line):
            inner = re.sub(r'^# UNMAPPED[^:]*:\s', '', line)
            if is_for_header(inner):
                pass_a.append(line)
                i += 1
                while i < len(output_lines):
                    body_line = output_lines[i]
                    if body_line == '' or body_line.lstrip() != body_line:
                        if not is_unmapped(body_line):
                            pass_a.append('# UNMAPPED (orphan body): '
                                          + body_line)
                        else:
                            pass_a.append(body_line)
                        i += 1
                    else:
                        break
                continue
        pass_a.append(line)
        i += 1

    # Pass (b): for-loop where ANY body line is UNMAPPED -> UNMAP the
    # whole loop (header + every body line).
    def looks_indented(line):
        return line[0:1] in (' ', '\t')

    pass_b = []
    i = 0
    while i < len(pass_a):
        line = pass_a[i]
        if is_for_header(line):
            j = i + 1
            body_lines = []
            any_unmapped = False
            while j < len(pass_a):
                next_line = pass_a[j]
                next_stripped = next_line.strip()
                if next_stripped == '':
                    body_lines.append(next_line)
                    j += 1
                    continue
                if is_unmapped(next_line):
                    body_lines.append(next_line)
                    any_unmapped = True
                    j += 1
                    continue
                if looks_indented(next_line):
                    body_lines.append(next_line)
                    j += 1
                    continue
                break
            while body_lines and body_lines[-1].strip() == '':
                j -= 1
                body_lines.pop()
            if any_unmapped:
                pass_b.append('# UNMAPPED: ' + line)
                for body_line in body_lines:
                    if is_unmapped(body_line) or body_line.strip() == '':
                        pass_b.append(body_line)
                    else:
                        pass_b.append('# UNMAPPED (orphan body): '
                                      + body_line)
            else:
                pass_b.append(line)
                pass_b.extend(body_lines)
            i = j
            continue
        pass_b.append(line)
        i += 1

    # Pass (d): collect every label/subroutine name that ended up UNMAPPED,
    # then UNMAP every expr() call that references one of those missing names.
    name_call_re = re.compile(
        r'(?:d\.)?(?:label|subroutine|hook_subroutine|index_base)\s*\(\s*'
        r'0x[0-9A-Fa-f]+\s*,\s*"([A-Za-z_][A-Za-z_0-9]*)"'
    )
    expr_call_re = re.compile(
        r'^\s*(?:d\.)?expr\s*\(\s*0x[0-9A-Fa-f]+\s*,\s*"([^"]*)"\s*\)'
    )
    identifier_re = re.compile(r'\b([A-Za-z_][A-Za-z_0-9]*)\b')

    while True:
        unmapped_names = set()
        defined_names = set()
        for line in pass_b:
            stripped = line.lstrip()
            if is_unmapped(line):
                inner = re.sub(r'^# UNMAPPED[^:]*:\s*', '', stripped)
                for m in name_call_re.finditer(inner):
                    unmapped_names.add(m.group(1))
            else:
                for m in name_call_re.finditer(stripped):
                    defined_names.add(m.group(1))
        truly_missing = unmapped_names - defined_names
        if not truly_missing:
            break

        changed = False
        new_pass = []
        for line in pass_b:
            if is_unmapped(line):
                new_pass.append(line)
                continue
            m = expr_call_re.match(line)
            if m:
                referenced = {nm.group(1)
                              for nm in identifier_re.finditer(m.group(1))}
                if referenced & truly_missing:
                    new_pass.append('# UNMAPPED (broken ref): ' + line)
                    changed = True
                    continue
            new_pass.append(line)
        pass_b = new_pass
        if not changed:
            break

    return '\n'.join(pass_b)


# ============================================================
# Entry point
# ============================================================


def main():
    base = Path('/Users/rjs/Code/acornaeology/acorn-nfs')
    rom_a_filepath = (
        base / 'versions' / 'anfs-4.21_variant_1' / 'rom'
        / 'anfs-4.21_variant_1.rom'
    )
    rom_b_filepath = base / 'versions' / 'anfs-4.24' / 'rom' / 'anfs-4.24.rom'
    script_filepath = (
        base / 'versions' / 'anfs-4.21_variant_1' / 'disassemble'
        / 'disasm_anfs_421_variant_1.py'
    )
    output_filepath = (
        base / 'versions' / 'anfs-4.24' / 'disassemble' / 'disasm_anfs_424.py'
    )

    print("Loading ROMs...", file=sys.stderr)
    data_a = rom_a_filepath.read_bytes()
    data_b = rom_b_filepath.read_bytes()

    print("Building address map (LCS + seed-and-extend, 65C02-aware)...",
          file=sys.stderr)
    addr_map, primary, supplementary, blocks = build_full_address_map(
        data_a, data_b, CPU_A, CPU_B,
    )
    print(f"  Primary (LCS):       {len(primary)} addresses",
          file=sys.stderr)
    print(f"  Supplementary (k=6): {len(supplementary)} addresses "
          f"in {len(blocks)} relocated blocks",
          file=sys.stderr)
    for blk in sorted(blocks, key=lambda b: -b.matched_pairs)[:10]:
        print(
            f"    A &{blk.a_start_addr:04X}-&{blk.a_end_addr:04X} "
            f"-> B &{blk.b_start_addr:04X}-&{blk.b_end_addr:04X}  "
            f"ratio={blk.ratio:.2f}  pairs={blk.matched_pairs}",
            file=sys.stderr,
        )
    print(f"  Total mapped (primary+supp): {len(addr_map)}",
          file=sys.stderr)

    # Identity mappings for every fixed (non-ROM) address. Only ROM code /
    # data in &8000-&BFFF shifts between versions; ZP, RAM workspace,
    # page-2 vectors, HAZEL (&C000-&DFFF), MMIO (&FExx) and the MOS vectors
    # (&FFxx) sit at fixed hardware/OS locations common to both Master 128
    # builds, so map them through unchanged. (Semantic correctness of any
    # HAZEL label is a triage concern; identity keeps the address valid so
    # verify round-trips byte-identically.)
    print("Adding identity mappings for fixed (non-ROM) addresses...",
          file=sys.stderr)
    identity_count = 0
    for addr in range(0x0000, 0x10000):
        if 0x8000 <= addr <= 0xBFFF:
            continue
        if addr not in addr_map:
            addr_map[addr] = addr
            identity_count += 1
    print(f"  Added {identity_count} identity mappings", file=sys.stderr)
    print(f"  Total mapped addresses: {len(addr_map)}", file=sys.stderr)

    print("\nTransforming script...", file=sys.stderr)
    script_text = script_filepath.read_text()
    result = transform_script(script_text, addr_map)

    output_filepath.write_text(result)
    print(f"\nWrote {output_filepath}", file=sys.stderr)

    unmapped = sum(1 for line in result.split('\n')
                   if line.strip().startswith('# UNMAPPED'))
    print(f"  {unmapped} lines marked as UNMAPPED", file=sys.stderr)


if __name__ == '__main__':
    main()
