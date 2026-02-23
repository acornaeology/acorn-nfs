#!/usr/bin/env python3
"""Extract sections of a disassembly .asm file by address range or label.

Usage:
    python asm_extract.py <asm_file> <start> [end]

    start/end can be:
      - Hex address: 80EA or $80EA or &80EA or 0x80EA
      - Label name: service_handler

    If end is omitted, extracts ~40 lines from start.

Examples:
    python asm_extract.py nfs-3.35D.asm 80EA 80F4
    python asm_extract.py nfs-3.35D.asm service_handler
    python asm_extract.py nfs-3.35D.asm &807D &80B4
"""

import re
import sys


def parse_address(s):
    """Parse a hex address from various notations."""
    s = s.strip().lstrip("$&").removeprefix("0x")
    try:
        return int(s, 16)
    except ValueError:
        return None


def build_index(lines):
    """Build address-to-line and label-to-line indices."""
    addr_to_line = {}
    label_to_line = {}
    addr_re = re.compile(r";\s*([0-9a-f]{4}):")
    label_re = re.compile(r"^\.(\w+)")

    for i, line in enumerate(lines):
        m = addr_re.search(line)
        if m:
            addr = int(m.group(1), 16)
            if addr not in addr_to_line:
                addr_to_line[addr] = i

        m = label_re.match(line)
        if m:
            label_to_line[m.group(1)] = i

    return addr_to_line, label_to_line


def find_line_for_target(target, lines, addr_to_line, label_to_line):
    """Resolve a target (address or label) to a line number."""
    addr = parse_address(target)
    if addr is not None:
        if addr in addr_to_line:
            return addr_to_line[addr]
        # Find nearest address <= target
        candidates = [a for a in addr_to_line if a <= addr]
        if candidates:
            nearest = max(candidates)
            return addr_to_line[nearest]
        return None

    # Try as label name
    if target in label_to_line:
        return label_to_line[target]

    # Partial match
    matches = [k for k in label_to_line if target in k]
    if len(matches) == 1:
        return label_to_line[matches[0]]
    elif matches:
        print(f"Ambiguous label '{target}', matches: {', '.join(sorted(matches))}", file=sys.stderr)
        return label_to_line[matches[0]]

    return None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    asm_filepath = sys.argv[1]
    start_target = sys.argv[2]
    end_target = sys.argv[3] if len(sys.argv) > 3 else None

    with open(asm_filepath) as f:
        lines = f.readlines()

    addr_to_line, label_to_line = build_index(lines)

    start_line = find_line_for_target(start_target, lines, addr_to_line, label_to_line)
    if start_line is None:
        print(f"Could not find '{start_target}'", file=sys.stderr)
        sys.exit(1)

    # Back up to include preceding comment/label lines
    while start_line > 0 and not re.search(r";\s*[0-9a-f]{4}:", lines[start_line - 1]):
        if lines[start_line - 1].strip() == "" or lines[start_line - 1].startswith(";") or lines[start_line - 1].startswith("."):
            start_line -= 1
        else:
            break

    if end_target:
        end_line = find_line_for_target(end_target, lines, addr_to_line, label_to_line)
        if end_line is None:
            print(f"Could not find '{end_target}'", file=sys.stderr)
            sys.exit(1)
        end_line += 1  # Include the end line
    else:
        end_line = min(start_line + 40, len(lines))

    for i in range(start_line, end_line):
        print(f"{i+1:5d}  {lines[i]}", end="")


if __name__ == "__main__":
    main()
