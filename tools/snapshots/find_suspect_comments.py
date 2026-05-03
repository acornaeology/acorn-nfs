#!/usr/bin/env python3
"""Identify inline comments at addresses whose 4.18→4.21_variant_1 mapping was
removed when fantasm issue #10 (remove interpolated mappings) lands.

Workflow:

1. Pre-fix snapshot is stored alongside this script as
   `addr_map_4.18_to_4.21_variant_1_pre_issue10.tsv`. It was captured
   before issue #10 was merged.

2. After the fix is released, re-run the same command to capture a
   post-fix snapshot:

       uv run fantasm addresses map 4.18 4.21_variant_1 --threshold 1 \
           | tail -n +2 | sort > tools/snapshots/addr_map_4.18_to_4.21_variant_1_post_issue10.tsv

3. Run this script:

       uv run python tools/snapshots/find_suspect_comments.py

   It diffs the two snapshots, finds 4.21 target addresses that were in
   the OLD map but NOT in the NEW map (the interpolated mappings), and
   reports any inline comments in the 4.21_variant_1 driver targeting
   those addresses. Those are the prime candidates for stale carry-over
   from the original baseline generation.

Per-address output: <target_addr> <source_addr> <comment_count>.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRE = HERE / "addr_map_4.18_to_4.21_variant_1_pre_issue10.tsv"
POST = HERE / "addr_map_4.18_to_4.21_variant_1_post_issue10.tsv"
DRIVER = HERE.parent.parent / "versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py"

COMMENT_RE = re.compile(r"^\s*comment\(0x([0-9A-Fa-f]+)\s*,")


def load_map(path):
    """Returns a dict {source_addr: target_addr} keyed on integers."""
    out = {}
    for line in path.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        src, tgt = parts[0].lstrip("&"), parts[1].lstrip("&")
        if tgt == "-":
            continue  # explicit "no mapping"
        try:
            out[int(src, 16)] = int(tgt, 16)
        except ValueError:
            pass
    return out


def main():
    if not POST.exists():
        sys.exit(f"Post-fix snapshot not yet captured. See header docstring "
                 f"for capture command. Expected: {POST}")
    pre = load_map(PRE)
    post = load_map(POST)

    # 4.21 target addresses that used to have a mapping but now don't:
    pre_targets = set(pre.values())
    post_targets = set(post.values())
    suspect_targets = pre_targets - post_targets
    print(f"# Pre-fix map entries:  {len(pre)}")
    print(f"# Post-fix map entries: {len(post)}")
    print(f"# 4.21 target addresses lost (interpolated): {len(suspect_targets)}")

    # Count inline comments in the driver per address.
    counts = {}
    for line in DRIVER.read_text().splitlines():
        m = COMMENT_RE.match(line)
        if not m:
            continue
        addr = int(m.group(1), 16)
        counts[addr] = counts.get(addr, 0) + 1

    # Reverse-lookup: which source addr(s) in pre mapped to each target?
    pre_inv = {}
    for s, t in pre.items():
        pre_inv.setdefault(t, []).append(s)

    suspect_with_comments = sorted(a for a in suspect_targets if a in counts)
    total_comments = sum(counts.get(a, 0) for a in suspect_with_comments)
    print(f"# Suspect targets with inline comment(s): {len(suspect_with_comments)}")
    print(f"# Total comments at suspect targets: {total_comments}")
    print()
    print("# 4.21 target\t4.18 source(s)\t#comments")
    for tgt in suspect_with_comments:
        srcs = ",".join(f"&{s:04X}" for s in sorted(pre_inv.get(tgt, [])))
        print(f"&{tgt:04X}\t{srcs}\t{counts[tgt]}")


if __name__ == "__main__":
    main()
