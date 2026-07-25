#!/usr/bin/env python3
"""Resolve auto-labels (lXXXX / cXXXX / sub_cXXXX / loop_cXXXX) in a target
version to semantic names taken from a cleaner reference version.

Most auto-labels are data tables read as indexing bases (`lda LABEL,y`).
The reference version (e.g. 4.21_variant_1, which has zero auto-labels)
names the same table, and the *comment* on the reference instruction is
carried verbatim into the target. So: for each auto-label in the target,
find the instruction(s) that reference it, take their inline comment, find
the reference-version instruction with the same comment, and read the
semantic label name off that instruction's operand.

Prints a proposed mapping: target-auto-label @ target-addr -> ref-name.
This is a suggestion aid; the driver edits are applied separately after
review. Nothing here changes emitted bytes.
"""

import re
import sys
from pathlib import Path

BASE = Path('/Users/rjs/Code/acornaeology/acorn-nfs')


def asm_path(v):
    return BASE / 'versions' / f'anfs-{v}' / 'output' / f'anfs-{v}.asm'


AUTO_RE = re.compile(r'\b(l[0-9a-f]{4}|c[0-9a-f]{4}|sub_c[0-9a-f]{4}|loop_c[0-9a-f]{4})\b')
# an asm instruction line: "    mnemonic operand   ; addr: bytes  echo   ; comment"
LINE_RE = re.compile(r'^\s+(\S.*?)\s+; ([0-9a-f]{4}): ([0-9a-f ]+?)\s{2,}\S*\s*(?:; (.*))?$')


def parse_asm(path):
    """Return list of dicts: {mnemonic_operand, addr, comment} for code lines."""
    rows = []
    for ln in path.read_text().split('\n'):
        m = LINE_RE.match(ln)
        if m:
            rows.append({
                'text': m.group(1).strip(),
                'addr': int(m.group(2), 16),
                'comment': (m.group(4) or '').strip(),
            })
    return rows


def operand_label(text):
    """Extract the symbolic operand label from e.g. 'lda tx_flags_table,y'."""
    m = re.search(r'\b(?:lda|ldx|ldy|sta|stx|sty|adc|sbc|and|ora|eor|cmp|cpx|cpy|bit|inc|dec|asl|lsr|rol|ror|jmp|jsr)\s+\(?([a-zA-Z_][a-zA-Z0-9_]*)', text)
    return m.group(1) if m else None


def main():
    target, ref = sys.argv[1], sys.argv[2]
    trows = parse_asm(asm_path(target))
    rrows = parse_asm(asm_path(ref))

    # index reference rows by comment
    ref_by_comment = {}
    for r in rrows:
        if r['comment']:
            ref_by_comment.setdefault(r['comment'], []).append(r)

    # find every auto-label and the rows that reference it
    autos = {}
    for r in trows:
        lbl = operand_label(r['text'])
        if lbl and AUTO_RE.fullmatch(lbl):
            autos.setdefault(lbl, []).append(r)

    print(f"# {len(autos)} auto-labels referenced in {target}")
    for lbl in sorted(autos):
        refs = autos[lbl]
        proposals = set()
        addr = None
        for r in refs:
            addr = addr or None
            for rr in ref_by_comment.get(r['comment'], []):
                nm = operand_label(rr['text'])
                if nm and not AUTO_RE.fullmatch(nm):
                    proposals.add(nm)
        # operand address in target
        op_addrs = set()
        for r in refs:
            mm = re.search(r'\b([0-9a-f]{2,4})\b', '')  # placeholder
        print(f"{lbl:14s} refs={len(refs):2d}  comment={refs[0]['comment']!r:60s} -> {sorted(proposals) or '???'}")


if __name__ == '__main__':
    main()
