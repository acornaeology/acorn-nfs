#!/usr/bin/env python3
"""Convert `[`name`](address:HEX[@version][?flag])` doc links to the
symbolic `label:name` form — but only when it's provably safe: the link
text (stripped of backticks) must be a label whose address in the target
version equals HEX. Non-label link text (raw hex, prose) is left on
`address:`.

Symbolic links don't go stale when code shifts between versions, which is
the whole point of `label:`.

Usage: convert_docs_address_to_label.py  (walks versions/*/)
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


def version_of_doc(doc_filepath):
    # versions/<prefix>-<ver>/<doc>
    name = doc_filepath.relative_to(VERSIONS_DIRPATH).parts[0]
    return name.split("-", 1)[1]


def main():
    converted = skipped = 0
    for doc_filepath in VERSIONS_DIRPATH.glob("*/*.md"):
        own_version = version_of_doc(doc_filepath)
        text = doc_filepath.read_text()

        def repl(m):
            nonlocal converted, skipped
            name = m.group("name")
            addr = int(m.group("hex"), 16)
            at = m.group("at") or ""
            flag = m.group("flag") or ""
            version = at[1:] if at else own_version
            if labels_for_version(version).get(name) == addr:
                converted += 1
                # keep the author's backtick styling on the visible text
                vis = m.group(0)[1:m.group(0).index("]")]
                return f"[{vis}](label:{name}{at}{flag})"
            skipped += 1
            return m.group(0)

        new = LINK_RE.sub(repl, text)
        if new != text:
            doc_filepath.write_text(new)
    print(f"converted {converted} address:->label:, left {skipped} as address:")


if __name__ == "__main__":
    main()
