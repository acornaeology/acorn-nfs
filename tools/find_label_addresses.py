#!/usr/bin/env python3
"""Find the corresponding addresses for labels across ROM versions.

Uses opcode fingerprinting: extracts a few bytes from the source ROM at the
label address, then searches the target ROM for that byte pattern.

Usage:
    python find_label_addresses.py
"""

import subprocess
from pathlib import Path

ROM_BASE = 0x8000

REPO_ROOT = Path(subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True).strip())

ROMS = {
    "3.34": REPO_ROOT / "versions/3.34/rom/nfs-3.34.rom",
    "3.34B": REPO_ROOT / "versions/3.34B/rom/nfs-3.34B.rom",
    "3.35D": REPO_ROOT / "versions/3.35D/rom/nfs-3.35D.rom",
}

# 6502 instruction lengths by opcode
OPCODE_LENGTHS = [
    2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 3, 3, 1,  # 00-0F
    2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 3, 3, 1,  # 10-1F
    3, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3, 1,  # 20-2F
    2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 3, 3, 1,  # 30-3F
    1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3, 1,  # 40-4F
    2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 3, 3, 1,  # 50-5F
    1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3, 1,  # 60-6F
    2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 3, 3, 1,  # 70-7F
    1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 1,  # 80-8F
    2, 2, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 3, 1, 1,  # 90-9F
    2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3, 1,  # A0-AF
    2, 2, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 3, 3, 3, 1,  # B0-BF
    2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3, 1,  # C0-CF
    2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 3, 3, 1,  # D0-DF
    2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3, 1,  # E0-EF
    2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 1, 1, 1, 3, 3, 1,  # F0-FF
]


def extract_opcode_fingerprint(data, offset, count=6):
    """Extract a sequence of opcodes (without operands) starting at offset."""
    opcodes = []
    pos = offset
    for _ in range(count):
        if pos >= len(data):
            break
        opcode = data[pos]
        length = OPCODE_LENGTHS[opcode]
        opcodes.append(opcode)
        pos += length
    return bytes(opcodes)


def find_fingerprint_in_rom(data, fingerprint):
    """Search for an opcode fingerprint in a ROM, returning all matching offsets."""
    matches = []
    for start in range(len(data)):
        fp = extract_opcode_fingerprint(data, start, len(fingerprint))
        if fp == fingerprint:
            matches.append(start)
    return matches


def main():
    roms = {ver: Path(p).read_bytes() for ver, p in ROMS.items()}

    # Labels to find: exist in 3.34B, need 3.35D address
    labels_34b = {
        "return_bget": 0x84A4,
        "pad_filename_spaces": 0x8618,
        "print_exec_and_len": 0x862B,
        "return_copy_string": 0x8D73,
        "print_dir_from_offset": 0x8D76,
        "rchex": 0x9103,
    }

    # Labels to find: exist in 3.35D, need 3.34B/3.34 address
    labels_35d = {
        "print_hex_byte": 0x8DA5,
    }

    print("=== Finding 3.34B labels in 3.35D ===\n")
    for name, addr in sorted(labels_34b.items()):
        offset = addr - ROM_BASE
        fp = extract_opcode_fingerprint(roms["3.34B"], offset, 6)
        print(f"{name} (3.34B: &{addr:04X})")
        print(f"  Fingerprint: {' '.join(f'{b:02X}' for b in fp)}")

        # Show actual bytes at that location for context
        raw = roms["3.34B"][offset:offset+12]
        print(f"  Raw bytes:   {' '.join(f'{b:02X}' for b in raw)}")

        matches = find_fingerprint_in_rom(roms["3.35D"], fp)
        if matches:
            for m in matches:
                addr_35d = m + ROM_BASE
                raw_35d = roms["3.35D"][m:m+12]
                print(f"  -> 3.35D: &{addr_35d:04X} (raw: {' '.join(f'{b:02X}' for b in raw_35d)})")
        else:
            # Try shorter fingerprint
            fp4 = extract_opcode_fingerprint(roms["3.34B"], offset, 4)
            matches4 = find_fingerprint_in_rom(roms["3.35D"], fp4)
            if matches4:
                print(f"  No 6-opcode match; 4-opcode matches at: {', '.join(f'&{m+ROM_BASE:04X}' for m in matches4)}")
            else:
                print(f"  NO MATCH in 3.35D (code may have been removed/restructured)")
        print()

    print("=== Finding 3.35D labels in 3.34B and 3.34 ===\n")
    for name, addr in sorted(labels_35d.items()):
        offset = addr - ROM_BASE
        fp = extract_opcode_fingerprint(roms["3.35D"], offset, 6)
        print(f"{name} (3.35D: &{addr:04X})")
        print(f"  Fingerprint: {' '.join(f'{b:02X}' for b in fp)}")

        raw = roms["3.35D"][offset:offset+12]
        print(f"  Raw bytes:   {' '.join(f'{b:02X}' for b in raw)}")

        for ver in ["3.34B", "3.34"]:
            matches = find_fingerprint_in_rom(roms[ver], fp)
            if matches:
                for m in matches:
                    addr_v = m + ROM_BASE
                    raw_v = roms[ver][m:m+12]
                    print(f"  -> {ver}: &{addr_v:04X} (raw: {' '.join(f'{b:02X}' for b in raw_v)})")
            else:
                fp4 = extract_opcode_fingerprint(roms["3.35D"], offset, 4)
                matches4 = find_fingerprint_in_rom(roms[ver], fp4)
                if matches4:
                    print(f"  No 6-opcode match in {ver}; 4-opcode matches: {', '.join(f'&{m+ROM_BASE:04X}' for m in matches4)}")
                else:
                    print(f"  NO MATCH in {ver}")
        print()


if __name__ == "__main__":
    main()
