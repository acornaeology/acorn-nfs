#!/usr/bin/env python3
"""Remap stale &XXXX prose addresses in the 4.25 driver.

The 4.24 driver's comment/description prose carries 4.24 addresses
verbatim; the +2 shift above &85AC left many of them pointing at the wrong
byte in 4.25. This rebuilds the same 4.24->4.25 address map generate_425.py
used and, for each stale &XXXX flagged by `fantasm comments check`, does a
global word-boundary replacement of `&XXXX` with its mapped value.

A stale address is one comments-check reports as "not a known address in
this version", so every occurrence of that exact token is wrong and a
global replace is safe. Dry-run by default; pass --apply to write.
"""

import bisect
import re
import sys
from pathlib import Path

from fantasm.api.blockmatch import build_full_address_map
from fantasm.api.mos6502 import opcode_tables

BASE = Path('/Users/rjs/Code/acornaeology/acorn-nfs')
ROM_A = BASE / 'versions' / 'anfs-4.24' / 'rom' / 'anfs-4.24.rom'
ROM_B = BASE / 'versions' / 'anfs-4.25' / 'rom' / 'anfs-4.25.rom'
DRIVER = BASE / 'versions' / 'anfs-4.25' / 'disassemble' / 'disasm_anfs_425.py'
CPU = '65c02'


def build_map():
    data_a = ROM_A.read_bytes()
    data_b = ROM_B.read_bytes()
    addr_map, *_ = build_full_address_map(data_a, data_b, CPU, CPU)
    for addr in range(0x0000, 0x10000):
        if 0x8000 <= addr <= 0xBFFF:
            continue
        addr_map.setdefault(addr, addr)
    lengths, _ = opcode_tables(CPU)
    romkeys = sorted(k for k in addr_map if 0x8000 <= k <= 0xBFFF)
    romvals = {k: addr_map[k] for k in romkeys}

    def bytes_match(src, dst):
        oa, ob = src - 0x8000, dst - 0x8000
        L = max(1, lengths[data_a[oa]])
        if ob + L > len(data_b) or oa + L > len(data_a):
            return False
        return data_a[oa:oa + L] == data_b[ob:ob + L]

    WINDOW = 120
    interp = {}
    for addr in range(0x8000, 0xC000):
        if addr in addr_map:
            continue
        i = bisect.bisect_left(romkeys, addr)
        if i == 0 or i >= len(romkeys):
            continue
        below, above = romkeys[i - 1], romkeys[i]
        if addr - below > WINDOW or above - addr > WINDOW:
            continue
        d1, d2 = romvals[below] - below, romvals[above] - above
        if d1 == d2 and bytes_match(addr, addr + d1):
            interp[addr] = addr + d1
    addr_map.update(interp)
    return addr_map


def valid_4_25_addrs(addr_map):
    return set(addr_map.values())


def main():
    apply = '--apply' in sys.argv
    # Read stale &XXXX tokens from stdin (pipe the comments-check output);
    # extract the "&XXXX which is not a known address" values.
    stdin_text = '' if sys.stdin.isatty() else sys.stdin.read()
    stale = sorted({
        int(m, 16)
        for m in re.findall(r'&([0-9A-Fa-f]{4}) which is not', stdin_text)
    })
    if not stale:
        print("Pipe `fantasm comments check` output into stdin.",
              file=sys.stderr)
        return

    addr_map = build_map()
    valid = valid_4_25_addrs(addr_map)
    text = DRIVER.read_text()

    changes = []
    for a in stale:
        token = f'&{a:04X}'
        mapped = addr_map.get(a)
        if mapped is None or mapped == a:
            # Only ROM addresses (&8000-&BFFF) shift between versions;
            # workspace / ZP / MMIO are fixed, so never remap them (e.g.
            # &0D2D is a benign unlabelled workspace range endpoint,
            # flagged in 4.24 too). Try a +2 fallback for the dominant
            # post-&85AC displacement, ROM-only.
            if not (0x8000 <= a <= 0xBFFF):
                changes.append((token, None, "SKIP (non-ROM, fixed)"))
                continue
            cand = a + 2
            if cand in valid:
                mapped = cand
            else:
                changes.append((token, None, "NO MAPPING"))
                continue
        new_token = f'&{mapped:04X}'
        # Count case-insensitive occurrences of the token as a whole word.
        pat = re.compile(re.escape(token), re.IGNORECASE)
        n = len(pat.findall(text))
        changes.append((token, new_token, f"{n} occ"))
        if apply and n:
            text = pat.sub(new_token, text)

    for old, new, note in changes:
        print(f"  {old} -> {new}   ({note})")

    if apply:
        DRIVER.write_text(text)
        print(f"\nApplied to {DRIVER}", file=sys.stderr)
    else:
        print("\n(dry-run; pass --apply to write)", file=sys.stderr)


if __name__ == '__main__':
    main()
