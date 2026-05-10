"""AST-based scan of a dasmos driver script for bare hex / linkification opportunities.

For each comment(), subroutine(), label() call, extract the comment / title /
description string literals (incl. concatenated triple-quoted strings) and
report every bare `&XXXX` reference, whether the address has a known label,
and a snippet of context. Cross-references the JSON output for label resolution.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path


HEX_RE = re.compile(r"&([0-9A-Fa-f]{2,4})")
# Look for an existing address: link in the immediate vicinity
LINK_NEAR_RE = re.compile(r"\]\(address:[0-9A-Fa-f]+(?:\?hex)?\)")


def build_label_map(json_path):
    j = json.load(open(json_path))
    labels = {}
    for it in j["items"]:
        if it.get("labels"):
            labels[it["addr"]] = it["labels"][0]
        for off, lst in (it.get("sub_labels") or {}).items():
            if lst:
                labels[int(off)] = lst[0]
    for s in j["subroutines"]:
        labels.setdefault(s["addr"], s["name"])
    ext = j.get("external_labels") or {}
    if isinstance(ext, dict):
        for name, addr in ext.items():
            labels.setdefault(addr, name)
    return labels


def addr_arg(node):
    """Return int address from first positional arg if it's a numeric literal."""
    if not node.args:
        return None
    a = node.args[0]
    if isinstance(a, ast.Constant) and isinstance(a.value, int):
        return a.value
    return None


def collect_strings(node):
    """Extract (kind, raw_text, lineno) tuples for the call's text-bearing args."""
    out = []
    fn = ""
    if isinstance(node.func, ast.Attribute):
        fn = node.func.attr
    elif isinstance(node.func, ast.Name):
        fn = node.func.id

    if fn == "comment":
        # comment(addr, text, ...)
        if len(node.args) >= 2:
            t = const_str(node.args[1])
            if t is not None:
                out.append(("comment", t, node.args[1].lineno))
    elif fn in ("subroutine", "label"):
        # subroutine(addr, name, *, title=..., description=...)
        # also handle positional-only forms: subroutine(addr, name, title)
        for kw in node.keywords:
            if kw.arg in ("title", "description"):
                t = const_str(kw.value)
                if t is not None:
                    out.append((kw.arg, t, kw.value.lineno))
    return out


def const_str(node):
    """Return string value if node is a single string constant or a JoinedStr/concat we can resolve."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    # Adjacent string literals get folded to a single Constant by the parser.
    return None


def scan(driver_path, label_map, *, start=0x0000, end=0xFFFF):
    src = Path(driver_path).read_text()
    tree = ast.parse(src)
    findings = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        addr = addr_arg(node)
        if addr is None:
            continue
        if not (start <= addr <= end):
            continue
        for kind, text, lineno in collect_strings(node):
            for m in HEX_RE.finditer(text):
                hexstr = m.group(1).upper()
                if len(hexstr) < 3:
                    continue
                # Skip if inside an existing markdown link target like (address:XXXX)
                # by checking the preceding ~3 chars
                pre = text[max(0, m.start() - 9) : m.start()]
                if "address:" in pre:
                    continue
                val = int(hexstr, 16)
                label = label_map.get(val, "")
                snippet = text[max(0, m.start() - 35) : min(len(text), m.end() + 35)].replace("\n", " ⏎ ")
                findings.append({
                    "addr": addr,
                    "lineno": lineno,
                    "kind": kind,
                    "hex": hexstr,
                    "label": label,
                    "snippet": snippet,
                })
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("driver_path")
    ap.add_argument("json_path")
    ap.add_argument("--start", type=lambda s: int(s, 16), default=0x0000)
    ap.add_argument("--end", type=lambda s: int(s, 16), default=0xFFFF)
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--with-label-only", action="store_true")
    ap.add_argument("--kind", help="comment|title|description (filter)")
    args = ap.parse_args()

    labels = build_label_map(args.json_path)
    findings = scan(args.driver_path, labels, start=args.start, end=args.end)
    if args.with_label_only:
        findings = [f for f in findings if f["label"]]
    if args.kind:
        findings = [f for f in findings if f["kind"] == args.kind]

    if args.summary:
        total = len(findings)
        with_label = sum(1 for f in findings if f["label"])
        by_kind = {}
        for f in findings:
            by_kind[f["kind"]] = by_kind.get(f["kind"], 0) + 1
        print(f"driver={args.driver_path}")
        print(f"range=&{args.start:04X}..&{args.end:04X}")
        print(f"total bare-hex occurrences: {total}")
        print(f"  linkifiable (label known):  {with_label}")
        print(f"  unknown / external:         {total - with_label}")
        print(f"  by kind: {by_kind}")
        return

    print("# kind\tline\taddr\thex\tlabel\tsnippet")
    for f in findings:
        print(f"{f['kind']}\t{f['lineno']}\t&{f['addr']:04X}\t&{f['hex']}\t{f['label']}\t{f['snippet']}")


if __name__ == "__main__":
    main()
