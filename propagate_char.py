#!/usr/bin/env python3
"""Propagate character-literal decisions from a reference version (whose
d.char_literal set is already curated) to a target version, keyed on
(operand value, normalised inline comment) rather than address — because
the shared comments carry across the version graph even though addresses
shift.

For each printable-range immediate in the target:
  - (value, norm-comment) matches a CONVERTED ref candidate  -> convert
  - matches a NON-converted ref candidate                    -> leave
  - key is ambiguous in the ref (both) or unseen             -> REVIEW

Prints the convert addresses (for apply_char_literals) and lists the
REVIEW rows so a human decides the genuinely new sites.

Usage: propagate_char.py <ref.asm> <ref_driver.py> <target.asm>
"""
import re
import sys
from pathlib import Path

# immediate line, either "#&2e" or "#'.'"; value read from byte column
IMM = re.compile(r'^\s*(?P<mnem>[a-z]{3})\s+#')
BYTES = re.compile(r';\s*(?P<addr>[0-9a-f]{4}):\s*(?P<b0>[0-9a-f]{2})\s+(?P<b1>[0-9a-f]{2})\b')


def norm(comment: str) -> str:
    c = comment.lower().strip()
    c = re.sub(r'&[0-9a-f]+', '&', c)       # addresses/hex values drift
    c = re.sub(r'\s+', ' ', c)
    return c


def candidates(asm_filepath):
    rows = []
    for line in Path(asm_filepath).read_text().splitlines():
        h = IMM.match(line)
        if not h:
            continue
        b = BYTES.search(line)
        if not b:
            continue
        val = int(b.group("b1"), 16)
        if not (0x20 <= val <= 0x7E):
            continue
        operand_addr = int(b.group("addr"), 16) + 1
        comment = line.rsplit(";", 1)[-1].strip() if ";" in line else ""
        rows.append((operand_addr, h.group("mnem"), val, comment))
    return rows


def main(ref_asm, ref_driver, tgt_asm):
    converted = {int(a, 16) for a in
                 re.findall(r'd\.char_literal\(0x([0-9A-Fa-f]+)\)',
                            Path(ref_driver).read_text())}
    decision = {}  # (val, norm) -> set of bools
    for addr, mnem, val, comment in candidates(ref_asm):
        decision.setdefault((val, norm(comment)), set()).add(addr in converted)

    convert, review = [], []
    for addr, mnem, val, comment in candidates(tgt_asm):
        key = (val, norm(comment))
        d = decision.get(key)
        if d == {True}:
            convert.append(addr)
        elif d == {False}:
            pass
        else:  # ambiguous or unseen
            review.append((addr, mnem, val, comment, "ambiguous" if d else "unseen"))

    print("CONVERT " + " ".join(f"{a:04X}" for a in sorted(convert)))
    print(f"# {len(convert)} convert, {len(review)} to review")
    for addr, mnem, val, comment, why in review:
        print(f"  REVIEW 0x{addr:04X} {mnem} #&{val:02x} '{chr(val)}' [{why}] | {comment}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
