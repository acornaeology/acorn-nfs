#!/usr/bin/env python3
"""Generate the initial disasm_anfs_421_variant_1.py by mapping addresses
from ANFS 4.18.

ANFS 4.21 (variant 1) is the first Master 128 ANFS. Compared with 4.18:

- The page 4/5/6 ROM-to-RAM copy loop has been removed entirely. The
  Master uses scattered private-workspace inits at &C000-&C2FF instead
  of compact relocated blocks. So no move() calls in the new driver.
- The CPU is 65C02 (CMOS), so the linear sweep needs the 65C02 opcode
  length table. The driver loads with cpu='65c02'.
- The ROM title grew from "Acorn ANFS 4.18" to "Acorn ANFS 4.21" and the
  copyright year changed from 1985 to 1986.
- The service entry moved from &8A15 to &8A54.

This script applies SequenceMatcher to the opcode sequences (using 65C02
lengths) of both ROMs to build a main-ROM address map, identity-maps zero
page and filing-system workspace, and rewrites the 4.18 driver script
with the translated addresses. Lines whose addresses do not map (e.g.
references to the gone &04xx-&06xx and &0016-&0057 runtime ranges) are
prefixed `# UNMAPPED:` for manual review.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))
from disasm_tools.blockmatch import build_full_address_map  # noqa: E402

# ============================================================
# Configuration
# ============================================================

ROM_BASE = 0x8000
ROM_SIZE = 16384

# 4.18 is NMOS 6502, 4.21_variant_1 is 65C02 (Master 128)
CPU_A = "6502"
CPU_B = "65c02"

# Address ranges from 4.18 that have NO counterpart in 4.21_variant_1.
# Annotations in these ranges should be left UNMAPPED for manual review.
#  - &0016-&0057: NMI workspace + zero-page relocated code (no longer copied)
#  - &0400-&06FF: pages 4-6 relocated code (no longer copied)
DEAD_RANGES = [
    (0x0016, 0x0057),
    (0x0400, 0x06FF),
]


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

    for i, line in enumerate(lines):
        current_lines.append(line)

        in_s = None
        escaped = False
        comment_stripped = []
        for j, ch in enumerate(line):
            if in_s is None:
                if ch == '#':
                    break
                if ch in ('"', "'"):
                    if line[j:j+3] in ('"""', "'''"):
                        in_s = line[j:j+3]
                    else:
                        in_s = ch
                comment_stripped.append(ch)
            else:
                comment_stripped.append(ch)
                if not escaped:
                    if len(in_s) == 3 and line[j:j+3] == in_s:
                        in_s = None
                    elif len(in_s) == 1 and ch == in_s:
                        in_s = None
                    elif ch == '\\':
                        escaped = True
                        continue
                escaped = False

        for ch in comment_stripped:
            if ch == '(':
                paren_depth += 1
            elif ch == ')':
                paren_depth -= 1

        if paren_depth <= 0:
            paren_depth = 0
            groups.append((current_start, i + 1, current_lines))
            current_start = i + 1
            current_lines = []

    if current_lines:
        groups.append((current_start, current_start + len(current_lines),
                       current_lines))

    return groups


def transform_script(script_text, addr_map):
    """Transform the 4.18 script to 4.21_variant_1 by mapping addresses."""
    lines = script_text.split('\n')
    hex_addr_pattern = re.compile(r'0x([0-9A-Fa-f]{2,5})')

    addr_first_funcs = ['label', 'entry', 'subroutine', 'comment',
                        'hook_subroutine', 'rts_code_ptr']

    groups = group_logical_statements(lines)
    output_lines = []

    text_replacements = [
        ('anfs-4.18', 'anfs-4.21_variant_1'),
        ('ANFS 4.18', 'ANFS 4.21 (variant 1)'),
        ('"6502"', '"65c02"'),
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

        # If any address in this whole logical statement falls in a dead
        # range, mark the whole thing UNMAPPED. This catches list/tuple
        # literals (e.g. _tube_r2_entries = [(0x0506, ...), ...]) and
        # other patterns that aren't simple address-first calls.
        all_text = '\n'.join(group_lines)
        # Strip line comments before scanning for hex literals (a string
        # like &0500 in a doc-comment shouldn't trigger UNMAPPED).
        all_addrs = []
        for hex_match in hex_addr_pattern.finditer(
            re.sub(r'#.*', '', all_text)
        ):
            try:
                all_addrs.append(int(hex_match.group(1), 16))
            except ValueError:
                pass
        if all_addrs and any(in_dead_range(a) for a in all_addrs):
            for gl in group_lines:
                output_lines.append(
                    '# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): '
                    + gl
                )
            continue

        # move() calls: 4.21_variant_1 has no relocated blocks
        if stripped.startswith('move('):
            for gl in group_lines:
                output_lines.append('# UNMAPPED (no relocated blocks): ' + gl)
            continue

        # Constants are symbolic; never map.
        if stripped.startswith('constant('):
            output_lines.extend(group_lines)
            continue

        # byte() calls: map address
        if stripped.startswith('byte('):
            match = re.match(r'^(\s*byte\()0x([0-9A-Fa-f]+)(.*)', first_line)
            if match:
                prefix, addr_hex, rest = match.groups()
                addr = int(addr_hex, 16)
                if addr in addr_map:
                    new_addr = addr_map[addr]
                    group_lines[0] = f'{prefix}0x{new_addr:04X}{rest}'
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
            if stripped.startswith(func_name + '('):
                is_addr_func = True
                match = re.match(
                    rf'^(\s*{func_name}\()0x([0-9A-Fa-f]+)(.*)',
                    first_line
                )
                if match:
                    prefix, addr_hex, rest = match.groups()
                    addr = int(addr_hex, 16)
                    if in_dead_range(addr):
                        for gl in group_lines:
                            output_lines.append(
                                '# UNMAPPED (dead range &0016-&0057 / '
                                '&0400-&06FF): ' + gl
                            )
                    elif addr in addr_map:
                        new_addr = addr_map[addr]
                        group_lines[0] = f'{prefix}0x{new_addr:04X}{rest}'
                        output_lines.extend(group_lines)
                    else:
                        for gl in group_lines:
                            output_lines.append('# UNMAPPED: ' + gl)
                else:
                    output_lines.extend(group_lines)
                break

        if is_addr_func:
            continue

        # Catch-all: any other statement that contains hex addresses (e.g.
        # `_cmd_entries = [(0xA3F6, "cmd_close"), ...]`, for-loop iterables,
        # range() limits) — map every hex literal. If any address can't be
        # mapped, mark the whole statement UNMAPPED so we don't crash py8dis
        # with stale addresses.
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

            def map_hex_literal(match, _line_idx=[0]):
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

    # Post-process for-loops in two passes:
    # (a) If the for-line is UNMAPPED, also UNMAP every indented body line
    #     (orphan body would be an IndentationError).
    # (b) If every body line is already UNMAPPED, also UNMAP the for-line
    #     (we don't want a `for: (only comments)` block).
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
            # Strip the prefix to inspect the original text.
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
    # whole loop (header + every body line). A partial body would leak
    # NameErrors when intermediate assignments are commented out.
    #
    # Body detection: an UNMAPPED comment is treated as part of the body
    # (it stands in for the original indented statement). Empty lines
    # are absorbed too. The body ends at the first non-indented,
    # non-empty, non-UNMAPPED line.
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
            any_real_body = False
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
                    any_real_body = True
                    j += 1
                    continue
                break
            # Trim trailing blank lines back out of the body
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

    # Pass (c): for-loop whose body is entirely UNMAPPED -> UNMAP for-line
    pass_c = []
    i = 0
    while i < len(pass_b):
        line = pass_b[i]
        if is_for_header(line):
            j = i + 1
            all_unmapped = True
            while j < len(pass_b):
                next_line = pass_b[j]
                next_stripped = next_line.strip()
                if next_stripped == '' or next_stripped.startswith('#'):
                    if is_unmapped(next_line):
                        j += 1
                        continue
                    break
                elif next_line[0:1] in (' ', '\t'):
                    all_unmapped = False
                    break
                else:
                    break
            if all_unmapped and j > i + 1:
                pass_c.append('# UNMAPPED: ' + line)
                i += 1
                continue
        pass_c.append(line)
        i += 1

    # Pass (d): collect every label/subroutine name that ended up
    # UNMAPPED, then UNMAP every expr() / rts_code_ptr() call that
    # references one of those missing names. To avoid false positives
    # from descriptive strings, only inspect calls that *do* reference
    # labels symbolically — namely expr() (second arg is a symbolic
    # expression string) and rts_code_ptr() (uses label names).
    name_call_re = re.compile(
        r'(?:label|subroutine|hook_subroutine)\s*\(\s*0x[0-9A-Fa-f]+\s*,\s*'
        r'"([A-Za-z_][A-Za-z_0-9]*)"'
    )
    expr_call_re = re.compile(
        r'^\s*expr\s*\(\s*0x[0-9A-Fa-f]+\s*,\s*"([^"]*)"\s*\)'
    )
    identifier_re = re.compile(r'\b([A-Za-z_][A-Za-z_0-9]*)\b')

    while True:
        unmapped_names = set()
        defined_names = set()
        for line in pass_c:
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
        for line in pass_c:
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
        pass_c = new_pass
        if not changed:
            break

    return '\n'.join(pass_c)


# ============================================================
# Entry point
# ============================================================


def main():
    base = Path('/Users/rjs/Code/acornaeology/acorn-nfs')
    rom_a_filepath = base / 'versions' / 'anfs-4.18' / 'rom' / 'anfs-4.18.rom'
    rom_b_filepath = (
        base / 'versions' / 'anfs-4.21_variant_1' / 'rom'
        / 'anfs-4.21_variant_1.rom'
    )
    script_filepath = (
        base / 'versions' / 'anfs-4.18' / 'disassemble' / 'disasm_anfs_418.py'
    )
    output_filepath = (
        base / 'versions' / 'anfs-4.21_variant_1' / 'disassemble'
        / 'disasm_anfs_421_variant_1.py'
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
    if blocks:
        # Most informative: largest blocks first
        for blk in sorted(blocks, key=lambda b: -b.matched_pairs)[:10]:
            print(
                f"    A &{blk.a_start_addr:04X}-&{blk.a_end_addr:04X} "
                f"-> B &{blk.b_start_addr:04X}-&{blk.b_end_addr:04X}  "
                f"ratio={blk.ratio:.2f}  pairs={blk.matched_pairs}",
                file=sys.stderr,
            )
        if len(blocks) > 10:
            print(f"    ... and {len(blocks) - 10} more.",
                  file=sys.stderr)
    print(f"  Total mapped (primary+supp): {len(addr_map)}",
          file=sys.stderr)

    # Identity mappings for RAM workspace pages still common to both.
    # Skip the 4.18 dead ranges (no counterpart in 4.21_variant_1).
    print("Adding identity mappings for RAM workspace...", file=sys.stderr)
    identity_count = 0
    for addr in range(0x0000, 0x0100):
        if in_dead_range(addr):
            continue
        if addr not in addr_map:
            addr_map[addr] = addr
            identity_count += 1
    for addr in range(0x0D00, 0x1100):
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
