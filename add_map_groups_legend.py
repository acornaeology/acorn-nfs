#!/usr/bin/env python3
"""Write the `memory_map_groups` legend (group -> human description) into
a version's rom.json, listing exactly the groups that version's driver
uses. Complements group_memory_map.py (which tags each entry); this is
the legend dasmos#43 groups render against.

Textual, order-preserving: the block is inserted right after the
`"title"` line (or the existing block replaced in place), so the rest of
rom.json is left byte-for-byte unchanged.

Usage: add_map_groups_legend.py <rom.json> <group1> <group2> ...
"""
import re
import sys
from pathlib import Path

ORDER = ["zero_page", "stack", "ram_workspace",
         "hazel", "mmio", "ext_vectors", "idx_base"]
DESC = {
    "zero_page": "Zero page",
    "stack": "6502 stack page",
    "ram_workspace": "RAM workspace",
    "hazel": "Filing system workspace (HAZEL)",
    "mmio": "Memory-mapped I/O",
    "ext_vectors": "MOS extended-vector trampolines",
    "idx_base": "Indexing-base addresses (wrap into ZP)",
}


def block(groups):
    want = [g for g in ORDER if g in groups]
    lines = ['    "memory_map_groups": {']
    for i, g in enumerate(want):
        comma = "," if i < len(want) - 1 else ""
        lines.append(f'        "{g}": "{DESC[g]}"{comma}')
    lines.append("    },")
    return "\n".join(lines)


def main(rom_filepath: Path, groups):
    src = rom_filepath.read_text()
    new = block(groups)
    # replace an existing block in place, else insert after the title line
    existing = re.search(r'^ {4}"memory_map_groups": \{.*?^ {4}\},',
                         src, re.S | re.M)
    if existing:
        src = src[:existing.start()] + new + src[existing.end():]
    else:
        m = re.search(r'^ {4}"title": .*?,\n', src, re.M)
        if not m:
            raise SystemExit(f"{rom_filepath}: no title line to anchor to")
        src = src[:m.end()] + new + "\n" + src[m.end():]
    rom_filepath.write_text(src)


if __name__ == "__main__":
    main(Path(sys.argv[1]), set(" ".join(sys.argv[2:]).split()))
