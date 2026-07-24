#!/usr/bin/env python3
"""Recover UNMAPPED annotations in the 4.24 driver whose 4.21 address
merely *shifted* (unchanged code/data relocated by inserted bytes).

The blockmatch address map only covers CODE addresses (they appear in the
opcode stream); annotations that point at DATA (dispatch tables, the
command table, string tables) were left UNMAPPED because their base
addresses never entered the opcode LCS. But most of those data regions
are unchanged between 4.21 and 4.24 — they just moved.

For each UNMAPPED single-address `d.*` line we compute the local shift
from the nearest mapped code address below and above the target. If both
agree (the target sits inside a uniformly-shifted run), the relocation is
provably content-preserving and we re-map the address and un-comment the
line. Lines in genuinely-changed regions (inconsistent local shift, or
multi-address / for-loop statements) are left UNMAPPED for manual review.

Idempotent: re-running only acts on lines still marked UNMAPPED.
"""
import re
import bisect
from pathlib import Path
from fantasm.api.blockmatch import build_full_address_map

BASE = Path('/Users/rjs/Code/acornaeology/acorn-nfs')
DRIVER = BASE / 'versions/anfs-4.24/disassemble/disasm_anfs_424.py'
ROM_A = BASE / 'versions/anfs-4.21_variant_1/rom/anfs-4.21_variant_1.rom'
ROM_B = BASE / 'versions/anfs-4.24/rom/anfs-4.24.rom'

# Only single-line, single-address annotation calls are auto-recovered.
# (for-loops over dispatch tables and multi-address statements are handled
# by hand.)
RECOVER_FUNCS = ('comment', 'label', 'entry', 'subroutine', 'byte',
                 'index_base', 'index_region', 'word', 'string',
                 'char_literal', 'inkey_code', 'format_hint', 'rts_code_ptr')

WINDOW = 96  # bytes; both neighbours must sit within this of the target


def main():
    a = ROM_A.read_bytes()
    b = ROM_B.read_bytes()
    amap, _, _, _ = build_full_address_map(a, b, "65c02", "65c02")
    for x in range(0x10000):
        if 0x8000 <= x <= 0xBFFF:
            continue
        amap.setdefault(x, x)
    romkeys = sorted(k for k in amap if 0x8000 <= k <= 0xBFFF)

    def interp(addr):
        if addr in amap:
            return amap[addr]
        i = bisect.bisect_left(romkeys, addr)
        below = romkeys[i - 1] if i > 0 else None
        above = romkeys[i] if i < len(romkeys) else None
        if below is None or above is None:
            return None
        if addr - below > WINDOW or above - addr > WINDOW:
            return None
        d1 = amap[below] - below
        d2 = amap[above] - above
        if d1 == d2:
            return addr + d1
        return None

    lines = DRIVER.read_text().split('\n')
    out = []
    recovered = 0
    addr_re = re.compile(r'0x([0-9A-Fa-f]{2,4})')
    # Only TOP-LEVEL calls (exactly one space after the marker — not the
    # 5-space-indented for-loop bodies) whose leading argument is a literal
    # address immediately followed by `,` or `)`. This excludes computed
    # bases like `d.expr(0xAD20 + idx, ...)` that reference loop variables.
    func_re = re.compile(
        r'^# UNMAPPED: (d\.(?:%s))\(0x[0-9A-Fa-f]{2,4}\s*[,)]' %
        '|'.join(RECOVER_FUNCS))

    for ln in lines:
        m = func_re.match(ln)
        if not m:
            out.append(ln)
            continue
        inner = ln[len('# UNMAPPED:'):].lstrip()
        # collect ROM addresses in the code portion (strip trailing comment)
        code = inner.partition('#')[0]
        # reject any statement that references a loop/computed variable
        if re.search(r'[A-Za-z_]\w*\s*[-+]\s*\w|%\s*\(|\bidx\b|enumerate',
                     code):
            out.append(ln)
            continue
        addrs = [int(x, 16) for x in addr_re.findall(code)]
        rom_addrs = [x for x in addrs if 0x8000 <= x <= 0xBFFF]
        if not rom_addrs:
            out.append(ln)
            continue
        mapping = {x: interp(x) for x in set(rom_addrs)}
        if any(v is None for v in mapping.values()):
            out.append(ln)
            continue
        # remap each ROM address in the code portion; keep comment verbatim
        c_part, sep, cmt = inner.partition('#')

        def repl(mo):
            v = int(mo.group(1), 16)
            if 0x8000 <= v <= 0xBFFF and v in mapping:
                return '0x%04X' % mapping[v]
            return mo.group(0)
        c_new = addr_re.sub(repl, c_part)
        out.append(c_new + sep + cmt)
        recovered += 1

    DRIVER.write_text('\n'.join(out))
    print(f"recovered {recovered} UNMAPPED annotation lines")


if __name__ == '__main__':
    main()
