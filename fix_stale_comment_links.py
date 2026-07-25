#!/usr/bin/env python3
"""Fix stale in-comment address: links: a `[`name`](address:HEX)` whose
text IS a real label but whose HEX is a few bytes off the label's actual
address (so it only resolved by nearest-preceding, sometimes to the wrong
routine). Convert each to `[`name`](label:name)`, which resolves to the
label's correct current address.

Only touches non-`?flag` links where `name` resolves to a label at an
address *different* from HEX — the exact-match ones are already converted
and the `?hex` ones are left on address: on purpose. Logs every fix.

Usage: fix_stale_comment_links.py  (walks versions/*/disassemble/)
"""
import json
import re
from functools import lru_cache
from pathlib import Path

VERSIONS_DIRPATH = Path("versions")

LINK_RE = re.compile(
    r"\[`?(?P<name>[A-Za-z_][A-Za-z0-9_]*)`?\]"
    r"\(address:(?P<hex>[0-9A-Fa-f]+)"
    r"(?P<at>@[0-9A-Za-z._]+)?"
    r"(?P<flag>\?[^)]*)?\)"
)


def build_label_addrs(data):
    m = {}
    for e in data.get("memory_map", []):
        if e.get("name"):
            m.setdefault(e["name"], e["addr"])
    for e in data.get("index_bases", []):
        if e.get("name"):
            m.setdefault(e["name"], e["addr"])
    for s in data.get("subroutines", []):
        if s.get("name"):
            m.setdefault(s["name"], s["addr"])
    ext = data.get("external_labels") or {}
    if isinstance(ext, dict):
        for n, a in ext.items():
            m.setdefault(n, a)
    for it in data.get("items", []):
        for n in it.get("labels", []):
            m[n] = it["addr"]
        for addr_str, names in it.get("sub_labels", {}).items():
            for n in names:
                m[n] = int(addr_str)
    return m


@lru_cache(maxsize=None)
def labels_for_version(version_id):
    for prefix in ("anfs", "nfs"):
        json_files = list(
            (VERSIONS_DIRPATH / f"{prefix}-{version_id}" / "output").glob("*.json"))
        if json_files:
            return build_label_addrs(json.loads(json_files[0].read_text()))
    return {}


def main():
    fixed = 0
    for driver_filepath in VERSIONS_DIRPATH.glob("*/disassemble/disasm_*.py"):
        own_version = driver_filepath.relative_to(
            VERSIONS_DIRPATH).parts[0].split("-", 1)[1]
        text = driver_filepath.read_text()

        def repl(m):
            nonlocal fixed
            name = m.group("name")
            addr = int(m.group("hex"), 16)
            at = m.group("at") or ""
            if m.group("flag"):
                return m.group(0)
            version = at[1:] if at else own_version
            actual = labels_for_version(version).get(name)
            if actual is not None and actual != addr:
                fixed += 1
                print(f"  {driver_filepath.parts[1]}: {name} "
                      f"&{addr:04X} -> &{actual:04X}")
                vis = m.group(0)[1:m.group(0).index("]")]
                return f"[{vis}](label:{name}{at})"
            return m.group(0)

        new = LINK_RE.sub(repl, text)
        if new != text:
            driver_filepath.write_text(new)
    print(f"TOTAL: fixed {fixed} stale links")


if __name__ == "__main__":
    main()
