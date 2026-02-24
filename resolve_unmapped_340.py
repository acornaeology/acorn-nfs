#!/usr/bin/env python3
"""Resolve UNMAPPED annotations in the NFS 3.40 driver script.

Uses the opcode-level address map from generate_340.py enhanced with:
1. Interpolation from nearest mapped neighbours for addresses in change blocks
2. Local opcode fingerprinting to confirm interpolated mappings
3. Validation against the py8dis JSON output (valid item addresses)

Outputs a report of each UNMAPPED annotation with its resolved 3.40 address
(or an explanation of why it can't be resolved).
"""

import difflib
import json
import re
import sys
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

ROM_BASE = 0x8000
ROM_SIZE = 8192

BASE = Path('/Users/rjs/Code/acornaeology/acorn-nfs')

ROM_A_FILEPATH = BASE / 'versions' / '3.35K' / 'rom' / 'nfs-3.35K.rom'
ROM_B_FILEPATH = BASE / 'versions' / '3.40' / 'rom' / 'nfs-3.40.rom'
DRIVER_FILEPATH = BASE / 'versions' / '3.40' / 'disassemble' / 'disasm_nfs_340.py'
JSON_FILEPATH = BASE / 'versions' / '3.40' / 'output' / 'nfs-3.40.json'

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


def build_full_address_map(data_a, data_b):
    """Build address map including both 'equal' and 'replace' blocks.

    Returns:
        addr_map: dict mapping ROM-A addresses to ROM-B addresses (equal blocks)
        change_blocks: list of (tag, a_start, a_end, b_start, b_end) for non-equal blocks
        insts_a, insts_b: instruction lists for local fingerprinting
    """
    insts_a = disassemble_to_opcodes(data_a)
    insts_b = disassemble_to_opcodes(data_b)

    opcodes_a = [op for _, op, _ in insts_a]
    opcodes_b = [op for _, op, _ in insts_b]

    matcher = difflib.SequenceMatcher(None, opcodes_a, opcodes_b, autojunk=False)

    addr_map = {}
    change_blocks = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                off_a = insts_a[i1 + k][0]
                off_b = insts_b[j1 + k][0]
                addr_map[ROM_BASE + off_a] = ROM_BASE + off_b
        else:
            a_start = ROM_BASE + insts_a[i1][0] if i1 < len(insts_a) else None
            a_end = ROM_BASE + insts_a[i2 - 1][0] if i2 > i1 else a_start
            b_start = ROM_BASE + insts_b[j1][0] if j1 < len(insts_b) else None
            b_end = ROM_BASE + insts_b[j2 - 1][0] if j2 > j1 else b_start
            change_blocks.append((tag, a_start, a_end, b_start, b_end, i1, i2, j1, j2))

    return addr_map, change_blocks, insts_a, insts_b


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
    change_blocks = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                off_a = insts_a[i1 + k][0]
                off_b = insts_b[j1 + k][0]
                addr_map[dest + off_a] = dest + off_b
        else:
            a_start = dest + insts_a[i1][0] if i1 < len(insts_a) else None
            a_end = dest + insts_a[i2 - 1][0] if i2 > i1 else a_start
            b_start = dest + insts_b[j1][0] if j1 < len(insts_b) else None
            b_end = dest + insts_b[j2 - 1][0] if j2 > j1 else b_start
            change_blocks.append((tag, a_start, a_end, b_start, b_end, i1, i2, j1, j2))

    return addr_map, change_blocks, insts_a, insts_b


def interpolate_address(addr, addr_map, sorted_mapped_addrs):
    """Find the likely 3.40 address by interpolating from nearest mapped neighbours."""
    # Binary search for nearest mapped addresses before and after
    import bisect
    idx = bisect.bisect_left(sorted_mapped_addrs, addr)

    before_addr = sorted_mapped_addrs[idx - 1] if idx > 0 else None
    after_addr = sorted_mapped_addrs[idx] if idx < len(sorted_mapped_addrs) else None

    if before_addr is not None:
        before_mapped = addr_map[before_addr]
        before_delta = addr - before_addr
        interp_from_before = before_mapped + before_delta
    else:
        interp_from_before = None

    if after_addr is not None:
        after_mapped = addr_map[after_addr]
        after_delta = addr - after_addr
        interp_from_after = after_mapped + after_delta
    else:
        interp_from_after = None

    return before_addr, before_mapped if before_addr else None, \
           after_addr, after_mapped if after_addr else None, \
           interp_from_before, interp_from_after


def fingerprint_at(data, addr, base, n_opcodes=6):
    """Get the first N opcodes starting at addr in data."""
    offset = addr - base
    if offset < 0 or offset >= len(data):
        return []
    opcodes = []
    pos = offset
    while len(opcodes) < n_opcodes and pos < len(data):
        op = data[pos]
        length = OPCODE_LENGTHS[op]
        if length == 0:
            length = 1
        opcodes.append(op)
        pos += length
    return opcodes


def find_fingerprint_in_range(fingerprint, data, base, search_start, search_end, min_match=4):
    """Search for an opcode fingerprint in a range of the ROM.

    Returns list of (addr, match_count) sorted by match_count descending.
    """
    matches = []
    offset = search_start - base
    end_offset = search_end - base

    while offset < end_offset and offset < len(data):
        candidate = fingerprint_at(data, base + offset, base, len(fingerprint))
        match_count = sum(1 for a, b in zip(fingerprint, candidate) if a == b)
        if match_count >= min_match:
            matches.append((base + offset, match_count))
        # Advance by instruction length
        op = data[offset]
        length = OPCODE_LENGTHS[op]
        if length == 0:
            length = 1
        offset += length

    matches.sort(key=lambda x: -x[1])
    return matches


def extract_unmapped_annotations(driver_filepath):
    """Extract all UNMAPPED annotations from the driver script.

    Returns list of dicts with: kind, address, line_number, name, detail.
    """
    source = driver_filepath.read_text()
    lines = source.splitlines()
    annotations = []

    hex_pattern = re.compile(r'0x([0-9A-Fa-f]+)')

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped.startswith('# UNMAPPED:'):
            i += 1
            continue

        content = stripped[len('# UNMAPPED:'):].strip()

        # Determine kind
        kind = None
        addr = None
        name = None

        for func_name in ['subroutine', 'comment', 'label', 'entry', 'rts_code_ptr', 'for ']:
            if content.startswith(func_name):
                kind = func_name.strip()
                break

        if kind is None:
            # Continuation of a multi-line UNMAPPED block
            i += 1
            continue

        # Extract address
        m = hex_pattern.search(content)
        if m:
            addr = int(m.group(1), 16)

        # Extract name for subroutine/label
        if kind in ('subroutine', 'label'):
            name_match = re.search(r'"([^"]+)"', content)
            if name_match:
                name = name_match.group(1)

        # Collect multi-line continuation
        detail_lines = [content]
        if kind == 'subroutine':
            # Subroutines are multi-line — collect until we find a non-UNMAPPED line
            j = i + 1
            while j < len(lines):
                next_stripped = lines[j].strip()
                if next_stripped.startswith('# UNMAPPED:'):
                    detail_lines.append(next_stripped[len('# UNMAPPED:'):].strip())
                    j += 1
                else:
                    break
            i = j
        else:
            i += 1

        annotations.append({
            'kind': kind,
            'address': addr,
            'name': name,
            'line_number': i,  # approximate
            'detail': '\n'.join(detail_lines),
        })

    return annotations


def load_valid_addresses(json_filepath):
    """Load the set of valid item addresses from the py8dis JSON output."""
    data = json.loads(json_filepath.read_text())
    valid = set()
    for item in data.get('items', []):
        addr = item.get('addr')
        if addr is not None:
            valid.add(addr)
    for sub in data.get('subroutines', []):
        addr = sub.get('addr')
        if addr is not None:
            valid.add(addr)
    # external_labels is a dict of name -> addr
    for name, addr in data.get('external_labels', {}).items():
        if isinstance(addr, int):
            valid.add(addr)
    return valid


def main():
    print("Loading ROMs...", file=sys.stderr)
    data_a = ROM_A_FILEPATH.read_bytes()
    data_b = ROM_B_FILEPATH.read_bytes()

    print("Building main ROM address map...", file=sys.stderr)
    addr_map, change_blocks, insts_a, insts_b = build_full_address_map(data_a, data_b)
    print(f"  Mapped {len(addr_map)} main ROM addresses", file=sys.stderr)
    print(f"  {len(change_blocks)} change blocks", file=sys.stderr)

    print("Building relocated block address maps...", file=sys.stderr)
    reloc_blocks = [
        (0x9315, 0x931C, 0x0016, 0x61),
        (0x935A, 0x935D, 0x0400, 0x100),
        (0x945A, 0x9456, 0x0500, 0x100),
        (0x955A, 0x9556, 0x0600, 0x100),
    ]

    all_change_blocks = list(change_blocks)
    for src_a, src_b, dest, length in reloc_blocks:
        reloc_map, reloc_changes, _, _ = build_relocated_address_map(
            data_a, data_b, src_a, src_b, dest, length)
        addr_map.update(reloc_map)
        all_change_blocks.extend(reloc_changes)

    # Identity mappings for RAM workspace
    for addr in range(0x0000, 0x0100):
        if addr not in addr_map:
            addr_map[addr] = addr
    for addr in range(0x0D00, 0x1000):
        if addr not in addr_map:
            addr_map[addr] = addr

    sorted_mapped = sorted(addr_map.keys())
    print(f"  Total mapped: {len(addr_map)}", file=sys.stderr)

    print("Loading valid addresses from JSON output...", file=sys.stderr)
    valid_addrs = load_valid_addresses(JSON_FILEPATH)
    print(f"  {len(valid_addrs)} valid item addresses", file=sys.stderr)

    print("Extracting UNMAPPED annotations...", file=sys.stderr)
    annotations = extract_unmapped_annotations(DRIVER_FILEPATH)
    print(f"  {len(annotations)} UNMAPPED annotations", file=sys.stderr)

    # Determine which ROM to fingerprint for each address range
    def get_fingerprint_data(addr):
        """Get the ROM data and base address for fingerprinting."""
        if 0x8000 <= addr < 0xA000:
            return data_a, data_b, ROM_BASE
        # For relocated addresses, we need to use the block data
        for src_a, src_b, dest, length in reloc_blocks:
            if dest <= addr < dest + length:
                block_a = data_a[src_a - ROM_BASE:src_a - ROM_BASE + length]
                block_b = data_b[src_b - ROM_BASE:src_b - ROM_BASE + length]
                return block_a, block_b, dest
        return None, None, None

    print("\n" + "=" * 72)
    print("UNMAPPED ANNOTATION RESOLUTION REPORT")
    print("=" * 72)

    resolved = 0
    unresolved = 0

    for ann in annotations:
        addr = ann['address']
        if addr is None:
            continue

        kind = ann['kind']
        name = ann['name'] or '(unnamed)'

        # Skip non-address annotations (for loops, etc.)
        if kind in ('for', 'rts_code_ptr'):
            continue

        # Check if directly mapped
        if addr in addr_map:
            new_addr = addr_map[addr]
            is_valid = new_addr in valid_addrs
            status = "VALID" if is_valid else "NOT_VALID_ITEM"
            print(f"\n{kind}(0x{addr:04X}) -> 0x{new_addr:04X}  [{status}]  {name}")
            if is_valid:
                resolved += 1
            else:
                unresolved += 1
            continue

        # Interpolate from neighbours
        before_a, before_b, after_a, after_b, interp_before, interp_after = \
            interpolate_address(addr, addr_map, sorted_mapped)

        # Get fingerprint from ROM A
        src_data_a, src_data_b, base = get_fingerprint_data(addr)
        if src_data_a is None:
            print(f"\n{kind}(0x{addr:04X}) -> ???  [NO_ROM_DATA]  {name}")
            unresolved += 1
            continue

        fp = fingerprint_at(src_data_a, addr, base, n_opcodes=8)

        # Determine search range in ROM B
        if interp_before is not None and interp_after is not None:
            search_lo = min(interp_before, interp_after) - 32
            search_hi = max(interp_before, interp_after) + 32
        elif interp_before is not None:
            search_lo = interp_before - 32
            search_hi = interp_before + 64
        elif interp_after is not None:
            search_lo = interp_after - 64
            search_hi = interp_after + 32
        else:
            search_lo = base
            search_hi = base + len(src_data_b)

        # Clamp to ROM range
        search_lo = max(search_lo, base)
        search_hi = min(search_hi, base + len(src_data_b))

        matches = find_fingerprint_in_range(fp, src_data_b, base, search_lo, search_hi, min_match=4)

        print(f"\n{kind}(0x{addr:04X})  {name}")
        print(f"  Neighbours: before 0x{before_a:04X}->0x{before_b:04X}, "
              f"after 0x{after_a:04X}->0x{after_b:04X}"
              if before_a and after_a else "  Neighbours: partial")
        if interp_before is not None:
            print(f"  Interpolated from before: 0x{interp_before:04X}")
        if interp_after is not None:
            print(f"  Interpolated from after:  0x{interp_after:04X}")
        print(f"  Fingerprint ({len(fp)} opcodes): {' '.join(f'{op:02X}' for op in fp)}")
        print(f"  Search range: 0x{search_lo:04X}-0x{search_hi:04X}")

        if matches:
            best_addr, best_count = matches[0]
            is_valid = best_addr in valid_addrs
            status = "VALID" if is_valid else "NOT_VALID_ITEM"
            print(f"  Best match: 0x{best_addr:04X} ({best_count}/{len(fp)} opcodes)  [{status}]")
            if len(matches) > 1:
                print(f"  Other matches: {', '.join(f'0x{a:04X}({c})' for a, c in matches[1:5])}")
            if is_valid:
                resolved += 1
            else:
                # Try nearby valid addresses
                for delta in range(-3, 4):
                    if best_addr + delta in valid_addrs:
                        print(f"  Nearby valid: 0x{best_addr + delta:04X}")
                unresolved += 1
        else:
            print(f"  No fingerprint match found")
            unresolved += 1

    print(f"\n{'=' * 72}")
    print(f"Resolved: {resolved}  Unresolved: {unresolved}")


if __name__ == '__main__':
    main()
