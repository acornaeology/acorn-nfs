#!/usr/bin/env python3
"""Insert `d.char_literal(0xADDR)` calls into a driver for the operand
bytes that genuinely hold an ASCII character (comparisons / loads / tests
against a real character), so the operand renders as `#'x'` instead of a
bare hex byte. Addresses are the operand-byte address (opcode addr + 1).

Idempotent: skips any address already carrying a char_literal call. The
block is inserted just before `ir = d.disassemble()`, under a marker.

Usage: apply_char_literals.py <driver.py> <hexaddr> [<hexaddr> ...]
       apply_char_literals.py <driver.py> --file <addr-list-file>
"""
import re
import sys
from pathlib import Path

MARKER = "# --- character-literal immediate operands ---"


def main(driver_filepath: Path, addrs):
    src = driver_filepath.read_text()
    existing = {int(a, 16) for a in re.findall(r'd\.char_literal\(0x([0-9A-Fa-f]+)\)', src)}
    addrs = sorted(set(addrs) - existing)
    if not addrs:
        print(f"{driver_filepath.name}: nothing to add")
        return
    block = [MARKER] + [f"d.char_literal(0x{a:04X})" for a in addrs] + [""]
    text = "\n".join(block)
    # append to an existing block if present, else insert before disassemble()
    if MARKER in src:
        src = src.replace(MARKER + "\n",
                          "\n".join(f"d.char_literal(0x{a:04X})" for a in addrs)
                          + "\n" + MARKER + "\n", 1)
    else:
        m = re.search(r'^ir = d\.disassemble\(\)', src, re.M)
        if not m:
            raise SystemExit(f"{driver_filepath}: no disassemble() call")
        src = src[:m.start()] + text + "\n" + src[m.start():]
    driver_filepath.write_text(src)
    print(f"{driver_filepath.name}: added {len(addrs)} char_literal calls")


if __name__ == "__main__":
    driver_filepath = Path(sys.argv[1])
    rest = sys.argv[2:]
    if rest and rest[0] == "--file":
        toks = Path(rest[1]).read_text().split()
    else:
        toks = " ".join(rest).split()
    main(driver_filepath, [int(t.lstrip("&"), 16) for t in toks])
