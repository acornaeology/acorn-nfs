#!/usr/bin/env python3
"""Convert `[`name`](address:HEX[@version][?flag])` links inside driver
comment / description strings to the symbolic `label:name` form — but
only when it is provably safe (verified same-name): the link text,
stripped of backticks, must be a label whose address in the target
version equals HEX exactly. Anything else (raw &XXXX / prose text, or a
name that doesn't resolve to that exact address) is left on `address:`.

Symbolic links don't go stale when code shifts between versions, so a
carried-over comment keeps pointing at the right routine. Annotation-only:
comments never affect emitted bytes, so `verify` must still pass.

Usage: convert_comment_address_to_label.py  (walks versions/*/disassemble/)
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


def version_of_driver(driver_filepath):
    # versions/<prefix>-<ver>/disassemble/<driver>.py
    name = driver_filepath.relative_to(VERSIONS_DIRPATH).parts[0]
    return name.split("-", 1)[1]


def main():
    total_conv = total_skip = 0
    for driver_filepath in VERSIONS_DIRPATH.glob("*/disassemble/disasm_*.py"):
        own_version = version_of_driver(driver_filepath)
        text = driver_filepath.read_text()
        conv = skip = 0

        def repl(m):
            nonlocal conv, skip
            name = m.group("name")
            addr = int(m.group("hex"), 16)
            at = m.group("at") or ""
            flag = m.group("flag") or ""
            version = at[1:] if at else own_version
            if labels_for_version(version).get(name) == addr:
                conv += 1
                vis = m.group(0)[1:m.group(0).index("]")]
                return f"[{vis}](label:{name}{at}{flag})"
            skip += 1
            return m.group(0)

        new = LINK_RE.sub(repl, text)
        if new != text:
            driver_filepath.write_text(new)
        total_conv += conv
        total_skip += skip
        if conv or skip:
            print(f"  {driver_filepath.parts[1]}: converted {conv}, left {skip}")
    print(f"TOTAL: converted {total_conv} address:->label:, left {total_skip}")


if __name__ == "__main__":
    main()
