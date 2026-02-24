#!/usr/bin/env python3
"""Generate the initial disasm_nfs_335k.py by mapping addresses from 3.35D.

Uses opcode-level sequence matching to build an address map between
the 3.35D and 3.35K ROMs, then transforms the 3.35D disassembly
driver script by translating all address references.
"""

import difflib
import re
import sys
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

ROM_BASE = 0x8000
ROM_SIZE = 8192

OPCODE_LENGTHS = [
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 0, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    3, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    0, 2, 0, 0, 2, 2, 2, 0, 1, 0, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 3, 1, 0, 0, 3, 0, 0,
    2, 2, 2, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 3, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
]


def disassemble_to_opcodes(data):
    """Linear sweep, returning list of (offset, opcode, length)."""
    instructions = []
    offset = 0
    while offset < len(data):
        opcode = data[offset]
        length = OPCODE_LENGTHS[opcode]
        if length == 0:
            length = 1
        instructions.append((offset, opcode, length))
        offset += length
    return instructions


def build_address_map(data_a, data_b):
    """Build a mapping from ROM-A addresses to ROM-B addresses."""
    insts_a = disassemble_to_opcodes(data_a)
    insts_b = disassemble_to_opcodes(data_b)

    opcodes_a = [op for _, op, _ in insts_a]
    opcodes_b = [op for _, op, _ in insts_b]

    matcher = difflib.SequenceMatcher(None, opcodes_a, opcodes_b, autojunk=False)

    addr_map = {}
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                off_a = insts_a[i1 + k][0]
                off_b = insts_b[j1 + k][0]
                addr_map[ROM_BASE + off_a] = ROM_BASE + off_b

    return addr_map


def build_relocated_address_map(data_a, data_b, src_a, src_b, dest, length):
    """Build address map for a relocated code block."""
    block_a = data_a[src_a - ROM_BASE:src_a - ROM_BASE + length]
    block_b = data_b[src_b - ROM_BASE:src_b - ROM_BASE + length]

    insts_a = disassemble_to_opcodes(block_a)
    insts_b = disassemble_to_opcodes(block_b)

    opcodes_a = [op for _, op, _ in insts_a]
    opcodes_b = [op for _, op, _ in insts_b]

    matcher = difflib.SequenceMatcher(None, opcodes_a, opcodes_b, autojunk=False)

    addr_map = {}
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                off_a = insts_a[i1 + k][0]
                off_b = insts_b[j1 + k][0]
                addr_map[dest + off_a] = dest + off_b

    return addr_map


def group_logical_statements(lines):
    """Group lines into logical statements, tracking open parentheses.

    Returns list of (start_line_idx, end_line_idx_exclusive, lines_list).
    Multi-line function calls (where parens aren't balanced) are grouped together.
    """
    groups = []
    current_start = 0
    current_lines = []
    paren_depth = 0

    for i, line in enumerate(lines):
        current_lines.append(line)

        # Count parens, ignoring those in strings and comments
        in_string = None
        escaped = False
        code = line
        # Strip Python comments (# outside strings)
        comment_stripped = []
        in_s = None
        for j, ch in enumerate(code):
            if in_s is None:
                if ch == '#':
                    break
                if ch in ('"', "'"):
                    # Check for triple quotes
                    if code[j:j+3] in ('"""', "'''"):
                        in_s = code[j:j+3]
                    else:
                        in_s = ch
                comment_stripped.append(ch)
            else:
                comment_stripped.append(ch)
                if not escaped:
                    if len(in_s) == 3 and code[j:j+3] == in_s:
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

        # Also track triple-quoted strings that span lines
        triple_count = code.count('"""') + code.count("'''")

        if paren_depth <= 0:
            paren_depth = 0
            groups.append((current_start, i + 1, current_lines))
            current_start = i + 1
            current_lines = []

    if current_lines:
        groups.append((current_start, current_start + len(current_lines), current_lines))

    return groups


def transform_script(script_text, addr_map):
    """Transform the 3.35D script to 3.35K by mapping addresses."""
    lines = script_text.split('\n')
    hex_addr_pattern = re.compile(r'0x([0-9A-Fa-f]{2,5})')

    # Functions that take a ROM/runtime address as first argument
    addr_first_funcs = ['label', 'entry', 'subroutine', 'comment',
                        'hook_subroutine', 'rts_code_ptr']

    groups = group_logical_statements(lines)
    output_lines = []

    for start_idx, end_idx, group_lines in groups:
        first_line = group_lines[0]
        stripped = first_line.strip()
        full_text = '\n'.join(group_lines)

        # --- Skip pure comments and blank lines ---
        if stripped.startswith('#') or stripped == '':
            for gl in group_lines:
                # Apply text replacements to comments
                gl = gl.replace('nfs-3.35D', 'nfs-3.35K')
                if 'Address map: NFS 3.34B \u2192 NFS 3.35D' in gl:
                    gl = gl.replace('Address map: NFS 3.34B \u2192 NFS 3.35D',
                                    'Address map: NFS 3.35D \u2192 NFS 3.35K')
                if 'derived from the NFS 3.34B disassembly driver' in gl:
                    gl = gl.replace('derived from the NFS 3.34B disassembly driver',
                                    'derived from the NFS 3.35D disassembly driver')
                if 'two ROMs are 87.4% identical' in gl:
                    gl = '# The two ROMs are 97.8% identical at the opcode level.'
                output_lines.append(gl)
            continue

        # --- File path replacements ---
        group_lines = [gl.replace('nfs-3.35D', 'nfs-3.35K') for gl in group_lines]
        first_line = group_lines[0]
        stripped = first_line.strip()

        # --- move() calls ---
        if stripped.startswith('move('):
            for gl in group_lines:
                if '0x931A' in gl:
                    gl = gl.replace('0x931A', '0x9315')
                    gl = re.sub(r'#.*', '# &9315 (-5 from 3.35D)', gl)
                elif '0x935F' in gl:
                    gl = gl.replace('0x935F', '0x935A')
                    gl = re.sub(r'#.*', '# &935A (-5 from 3.35D)', gl)
                elif '0x945F' in gl:
                    gl = gl.replace('0x945F', '0x945A')
                    gl = re.sub(r'#.*', '# &945A (-5 from 3.35D)', gl)
                elif '0x955F' in gl:
                    gl = gl.replace('0x955F', '0x955A')
                    gl = re.sub(r'#.*', '# &955A (-5 from 3.35D)', gl)
                output_lines.append(gl)
            continue

        # --- Constant definitions (don't map) ---
        if stripped.startswith('constant('):
            output_lines.extend(group_lines)
            continue

        # --- Address-bearing function calls ---
        is_addr_func = False
        for func_name in addr_first_funcs:
            if stripped.startswith(func_name + '('):
                is_addr_func = True
                # Extract the first hex address
                match = re.match(
                    rf'^(\s*{func_name}\()0x([0-9A-Fa-f]+)(.*)',
                    first_line
                )
                if match:
                    prefix, addr_hex, rest = match.groups()
                    addr = int(addr_hex, 16)
                    if addr in addr_map:
                        new_addr = addr_map[addr]
                        group_lines[0] = f'{prefix}0x{new_addr:04X}{rest}'
                        output_lines.extend(group_lines)
                    else:
                        # Comment out entire multi-line statement
                        for gl in group_lines:
                            output_lines.append('# UNMAPPED: ' + gl)
                else:
                    output_lines.extend(group_lines)
                break

        if is_addr_func:
            continue

        # --- for addr in [...] loops ---
        if 'for addr in [' in stripped or 'for i in range(' in stripped:
            def map_hex_in_list(match):
                addr = int(match.group(1), 16)
                if addr in addr_map:
                    return f'0x{addr_map[addr]:04X}'
                return f'0x{addr:04X}'
            group_lines = [hex_addr_pattern.sub(map_hex_in_list, gl)
                          for gl in group_lines]

        output_lines.extend(group_lines)

    # Post-process: fix for-loops whose body is entirely UNMAPPED
    final_lines = []
    i = 0
    result_lines = output_lines
    while i < len(result_lines):
        line = result_lines[i]
        stripped = line.strip()
        if stripped.startswith('for ') and stripped.endswith(':'):
            # Check if ALL following indented lines are UNMAPPED or blank
            j = i + 1
            all_unmapped = True
            while j < len(result_lines):
                next_stripped = result_lines[j].strip()
                if next_stripped == '' or next_stripped.startswith('#'):
                    if next_stripped.startswith('# UNMAPPED:'):
                        j += 1
                        continue
                    break  # blank line or non-UNMAPPED comment ends the block
                elif result_lines[j][0:1] in (' ', '\t'):
                    # Indented line that's not a comment
                    all_unmapped = False
                    break
                else:
                    break  # non-indented line
            if all_unmapped and j > i + 1:
                final_lines.append('# UNMAPPED: ' + line)
                i += 1
                continue
        final_lines.append(line)
        i += 1

    return '\n'.join(final_lines)


def main():
    base = Path('/Users/rjs/Code/acornaeology/acorn-nfs')
    rom_a_filepath = base / 'versions' / '3.35D' / 'rom' / 'nfs-3.35D.rom'
    rom_b_filepath = base / 'versions' / '3.35K' / 'rom' / 'nfs-3.35K.rom'
    script_filepath = base / 'versions' / '3.35D' / 'disassemble' / 'disasm_nfs_335d.py'
    output_filepath = base / 'versions' / '3.35K' / 'disassemble' / 'disasm_nfs_335k.py'

    print("Loading ROMs...", file=sys.stderr)
    data_a = rom_a_filepath.read_bytes()
    data_b = rom_b_filepath.read_bytes()

    print("Building main ROM address map...", file=sys.stderr)
    addr_map = build_address_map(data_a, data_b)
    print(f"  Mapped {len(addr_map)} main ROM addresses", file=sys.stderr)

    print("Building relocated block address maps...", file=sys.stderr)
    reloc_blocks = [
        (0x931A, 0x9315, 0x0016, 0x61),
        (0x935F, 0x935A, 0x0400, 0x100),
        (0x945F, 0x945A, 0x0500, 0x100),
        (0x955F, 0x955A, 0x0600, 0x100),
    ]

    for src_a, src_b, dest, length in reloc_blocks:
        reloc_map = build_relocated_address_map(data_a, data_b, src_a, src_b, dest, length)
        addr_map.update(reloc_map)
        print(f"  Block ${src_a:04X}\u2192${src_b:04X} (runtime ${dest:04X}): {len(reloc_map)} addresses",
              file=sys.stderr)

    # Identity mappings for RAM workspace
    for addr in range(0x0000, 0x0100):
        if addr not in addr_map:
            addr_map[addr] = addr
    for addr in range(0x0D00, 0x1000):
        if addr not in addr_map:
            addr_map[addr] = addr

    # The dispatch tables at $8020 (lo) and $8044 (hi) are data, not code,
    # and exist at the same ROM offsets in both versions
    for addr in range(0x8015, 0x806B):
        if addr not in addr_map:
            addr_map[addr] = addr

    print(f"  Total mapped addresses: {len(addr_map)}", file=sys.stderr)

    key_addrs = [0x80D4, 0x80EA, 0x810D, 0x81FA, 0x8486, 0x853C, 0x9660]
    print("\nKey address mappings:", file=sys.stderr)
    for addr in key_addrs:
        if addr in addr_map:
            print(f"  ${addr:04X} \u2192 ${addr_map[addr]:04X}", file=sys.stderr)
        else:
            print(f"  ${addr:04X} \u2192 UNMAPPED", file=sys.stderr)

    print("\nTransforming script...", file=sys.stderr)
    script_text = script_filepath.read_text()
    result = transform_script(script_text, addr_map)

    output_filepath.write_text(result)
    print(f"\nWrote {output_filepath}", file=sys.stderr)

    unmapped = sum(1 for line in result.split('\n') if line.strip().startswith('# UNMAPPED:'))
    print(f"  {unmapped} lines marked as UNMAPPED", file=sys.stderr)


if __name__ == '__main__':
    main()
