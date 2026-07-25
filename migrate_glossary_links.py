#!/usr/bin/env python3
"""Migrate rom.json `glossary_links` (fuzzy pattern+occurrence matcher) to
explicit inline `[text](glossary:SLUG)` links in the doc Markdown, then
drop the `glossary_links` arrays.

Each entry `{pattern, occurrence, term}` becomes a link on the FIRST safe
occurrence of `pattern` in the doc: a word-boundary match (not starting
mid-word, which is what broke `MOS` inside `CMOS`) that is not inside a
code span or an existing link. First-mention linking is the glossary
convention, and it naturally supersedes the old occurrence workarounds.

Usage: migrate_glossary_links.py <rom.json> [<rom.json> ...]
"""
import json
import re
import sys
from pathlib import Path


def slugify(term: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", term.lower().replace(" ", "-"))


def _mask(text: str) -> str:
    """Blank out code spans and existing links (same length) so pattern
    search ignores them while offsets stay aligned to the original."""
    def blank(m):
        return "\x00" * len(m.group(0))
    text = re.sub(r"`[^`]*`", blank, text)
    text = re.sub(r"\[[^\]]*\]\([^)]*\)", blank, text)
    return text


def _first_safe_pos(text: str, pattern: str):
    masked = _mask(text)
    for m in re.finditer(re.escape(pattern), masked):
        i = m.start()
        before = masked[i - 1] if i > 0 else " "
        if not (before.isalnum() or before == "_"):
            return i
    return None


# Remove a `"glossary_links": [ ... ]` block textually, preserving the
# rest of rom.json's formatting. Try leading-comma, then trailing-comma,
# then bare, so it works wherever the key sits in the doc object.
_REMOVE_PATTERNS = [
    r',\s*"glossary_links"\s*:\s*\[.*?\]',
    r'"glossary_links"\s*:\s*\[.*?\]\s*,\s*',
    r'"glossary_links"\s*:\s*\[.*?\]',
]


def _strip_glossary_links(rom_text: str) -> str:
    while '"glossary_links"' in rom_text:
        for pat in _REMOVE_PATTERNS:
            new = re.sub(pat, "", rom_text, count=1, flags=re.DOTALL)
            if new != rom_text:
                rom_text = new
                break
        else:
            break
    return rom_text


def migrate(rom_filepath: Path):
    rom_dirpath = rom_filepath.parent.parent  # versions/<v>/rom/rom.json
    data = json.loads(rom_filepath.read_text())
    changed = False
    unplaced = []
    for doc in data.get("docs", []):
        links = doc.get("glossary_links")
        if not links:
            continue
        doc_filepath = rom_dirpath / doc["path"]
        text = doc_filepath.read_text()
        # Wrap on the mutating text so already-wrapped links are excluded
        # from later patterns.
        for entry in links:
            pattern, term = entry["pattern"], entry["term"]
            pos = _first_safe_pos(text, pattern)
            if pos is None:
                unplaced.append((doc["path"], pattern, term))
                continue
            end = pos + len(pattern)
            link = f"[{text[pos:end]}](glossary:{slugify(term)})"
            text = text[:pos] + link + text[end:]
        doc_filepath.write_text(text)
        changed = True
    if changed:
        stripped = _strip_glossary_links(rom_filepath.read_text())
        # sanity: still valid JSON with no glossary_links left
        json.loads(stripped)
        rom_filepath.write_text(stripped)
    for path, pattern, term in unplaced:
        print(f"  UNPLACED {rom_filepath.parent.parent.name} :: {path} :: "
              f"{pattern!r} -> {term!r} (no safe occurrence)")
    return changed, len(unplaced)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        migrate(Path(arg))
