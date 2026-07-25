#!/usr/bin/env python3
"""Add `group=` to memory-map entries that dasmos flags as ungrouped
(dasmos#43): a mapped label / index-base with no group can't be placed
within the surrounding memory layout.

Driven by the exact address list from the `fantasm disassemble` warning
(passed on the command line), so it only touches entries already on the
map — it never adds group= to a bare label (which would wrongly pull it
onto the map). AST-based: the kwarg is spliced in after the call's last
existing argument, never by blind text edit.

Group is chosen by address band, matching the vocabulary already used in
the 4.21/4.24 drivers:
    < &0100          zero_page
    &0100..&01FF     stack
    &0200..&BFFF     ram_workspace
    &C000..&C2FF     hazel

Usage: group_memory_map.py <driver.py> <hexaddr> [<hexaddr> ...]
Prints the set of groups it assigned (one per line) for the caller to
fold into rom.json's memory_map_groups legend.
"""
import ast
import sys
from pathlib import Path


def group_for(addr: int) -> str:
    if addr < 0x0100:
        return "zero_page"
    if addr < 0x0200:
        return "stack"
    if addr < 0xC000:
        return "ram_workspace"
    if addr < 0xC300:
        return "hazel"
    raise ValueError(f"no band for &{addr:04X}")


def add_groups(path: Path, addrs: set[int]):
    src = path.read_text()
    tree = ast.parse(src)
    lines = src.splitlines(keepends=True)
    line_start = [0]
    for ln in lines:
        line_start.append(line_start[-1] + len(ln))

    def off(lineno, col):
        return line_start[lineno - 1] + col

    edits = []  # (insert_offset, text)
    assigned = set()
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr in ("label", "index_base", "index_region")
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "d"
                and node.args
                and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, int)):
            continue
        addr = node.args[0].value
        if addr not in addrs:
            continue
        if any(kw.arg == "group" for kw in node.keywords):
            continue  # already grouped
        g = group_for(addr)
        last = max((*node.args, *node.keywords),
                   key=lambda n: (n.end_lineno, n.end_col_offset))
        pos = off(last.end_lineno, last.end_col_offset)
        edits.append((pos, f', group="{g}"'))
        assigned.add(g)

    if edits:
        edits.sort(reverse=True)
        for pos, text in edits:
            src = src[:pos] + text + src[pos:]
        path.write_text(src)
    return len(edits), assigned


if __name__ == "__main__":
    driver_filepath = Path(sys.argv[1])
    toks = " ".join(sys.argv[2:]).split()
    addrs = {int(a.lstrip("&"), 16) for a in toks}
    n, assigned = add_groups(driver_filepath, addrs)
    sys.stderr.write(f"{driver_filepath.name}: grouped {n} entries\n")
    for g in sorted(assigned):
        print(g)
