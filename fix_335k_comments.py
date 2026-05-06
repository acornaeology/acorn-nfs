#!/usr/bin/env python3
"""Fix stale hex addresses in 3.35K disassembly driver comments.

Builds label-name-based address maps from 3.34, 3.34B, and 3.35D JSON
outputs to 3.35K, then replaces &XXXX addresses in comments and
triple-quoted description strings (but not in Python code).
"""

import json
import re
import sys
from pathlib import Path

VERSIONS_DIRPATH = Path(__file__).resolve().parent / "versions"
TARGET_FILEPATH = VERSIONS_DIRPATH / "3.35K" / "disassemble" / "disasm_nfs_335K.py"

# Source version JSONs (oldest first — later versions override earlier ones
# for duplicate label names, which is correct since more recent source
# addresses are more likely to appear in the 3.35D-derived driver).
SOURCE_VERSIONS = [
    ("3.34", VERSIONS_DIRPATH / "3.34" / "output" / "nfs-3.34.json"),
    ("3.34B", VERSIONS_DIRPATH / "3.34B" / "output" / "nfs-3.34B.json"),
    ("3.35D", VERSIONS_DIRPATH / "3.35D" / "output" / "nfs-3.35D.json"),
]
TARGET_JSON_FILEPATH = VERSIONS_DIRPATH / "3.35K" / "output" / "nfs-3.35K.json"

# Matches &XXXX (4 hex digits, upper or lower case, Acorn notation)
ADDR_RE = re.compile(r"&([0-9A-Fa-f]{4})")


def build_label_to_addr(json_filepath: Path) -> dict[str, int]:
    """Build a mapping from label name to address from a py8dis JSON output."""
    with open(json_filepath) as f:
        data = json.load(f)

    label_map: dict[str, int] = {}

    # From items: each item has 'addr' and 'labels' (list of label names)
    for item in data.get("items", []):
        addr = item["addr"]
        for lbl in item.get("labels", []):
            label_map[lbl] = addr
        # Also sub_labels: dict of addr_str -> [label_names]
        for sub_addr_str, sub_labels in item.get("sub_labels", {}).items():
            sub_addr = int(sub_addr_str)
            for lbl in sub_labels:
                label_map[lbl] = sub_addr

    # From external_labels: dict of label_name -> addr
    for lbl, addr in data.get("external_labels", {}).items():
        label_map[lbl] = addr

    # From subroutines: list of {addr, name, ...}
    # Some subroutines have title/description but no name.
    for sub in data.get("subroutines", []):
        if "name" in sub:
            label_map[sub["name"]] = sub["addr"]

    # From constants: list of {name, value}
    for const in data.get("constants", []):
        label_map[const["name"]] = const["value"]

    return label_map


def build_address_map() -> dict[int, int]:
    """Build a mapping from source version addresses to 3.35K addresses.

    For each label name that exists in both a source version and 3.35K,
    maps the source address to the 3.35K address (only when they differ).
    """
    target_labels = build_label_to_addr(TARGET_JSON_FILEPATH)

    # Invert: target addr -> set of label names
    # (we don't actually need this, we just need source_addr -> target_addr)

    addr_map: dict[int, int] = {}
    conflicts: dict[int, set[int]] = {}  # source_addr -> set of target_addrs

    for version_name, json_filepath in SOURCE_VERSIONS:
        if not json_filepath.exists():
            print(f"  Skipping {version_name}: {json_filepath} not found")
            continue

        source_labels = build_label_to_addr(json_filepath)
        version_mappings = 0

        for label_name, source_addr in source_labels.items():
            if label_name in target_labels:
                target_addr = target_labels[label_name]
                if source_addr != target_addr:
                    if source_addr in addr_map and addr_map[source_addr] != target_addr:
                        # Conflict: same source address maps to different targets
                        # via different label names. Track for reporting.
                        if source_addr not in conflicts:
                            conflicts[source_addr] = {addr_map[source_addr]}
                        conflicts[source_addr].add(target_addr)
                    addr_map[source_addr] = target_addr
                    version_mappings += 1

        print(f"  {version_name}: {len(source_labels)} labels, "
              f"{version_mappings} address changes vs 3.35K")

    if conflicts:
        print(f"\n  WARNING: {len(conflicts)} source addresses map to "
              f"multiple targets (last version wins):")
        for src, targets in sorted(conflicts.items()):
            print(f"    &{src:04X} -> {', '.join(f'&{t:04X}' for t in sorted(targets))}")

    return addr_map


def replace_addresses_in_text(text: str, addr_map: dict[int, int]) -> tuple[str, int]:
    """Replace &XXXX addresses in text using the address map.

    Returns (new_text, replacement_count).
    """
    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        addr = int(m.group(1), 16)
        if addr in addr_map:
            new_addr = addr_map[addr]
            count += 1
            # Preserve original case style
            orig = m.group(1)
            if orig == orig.upper():
                return f"&{new_addr:04X}"
            else:
                return f"&{new_addr:04x}"
        return m.group(0)

    new_text = ADDR_RE.sub(replacer, text)
    return new_text, count


def process_file(filepath: Path, addr_map: dict[int, int]) -> int:
    """Process the driver file, replacing addresses in comments and descriptions.

    Strategy:
    - Track whether we're inside a triple-quoted string (description= argument).
    - For lines inside triple-quoted strings: replace all &XXXX addresses.
    - For lines outside triple-quoted strings: only replace in the comment
      portion (after #), leaving Python code untouched.

    Returns total number of replacements made.
    """
    with open(filepath) as f:
        lines = f.readlines()

    total_replacements = 0
    in_triple_quote = False
    # Track what kind of triple quote we're in
    triple_quote_char = None
    output_lines = []

    for line_num, line in enumerate(lines, 1):
        if in_triple_quote:
            # We're inside a triple-quoted string. Check if it ends on this line.
            # Find the closing triple quote
            assert triple_quote_char is not None
            end_idx = line.find(triple_quote_char)
            if end_idx != -1:
                # Triple-quoted string ends on this line.
                # Replace addresses in the part before the closing quotes.
                before_close = line[:end_idx]
                after_close = line[end_idx:]  # includes the closing """ and rest
                new_before, count = replace_addresses_in_text(before_close, addr_map)
                total_replacements += count
                output_lines.append(new_before + after_close)
                in_triple_quote = False
                triple_quote_char = None
            else:
                # Entire line is inside triple-quoted string.
                new_line, count = replace_addresses_in_text(line, addr_map)
                total_replacements += count
                output_lines.append(new_line)
        else:
            # Not inside a triple-quoted string.
            # Check if a triple-quoted string starts on this line.
            # We look for description=""" or description='''
            # but also just any triple quote that's part of a subroutine() call.

            # First, handle lines that are pure comments (start with # possibly indented)
            stripped = line.lstrip()
            if stripped.startswith("#"):
                # Entire line is a comment. Replace addresses in the whole line.
                new_line, count = replace_addresses_in_text(line, addr_map)
                total_replacements += count
                output_lines.append(new_line)
                continue

            # Check for triple-quoted strings opening on this line.
            # Look for """ or ''' that opens a multi-line string.
            # Common patterns:
            #   description="""\     (opens, content starts next line)
            #   description="""...""")  (single-line triple-quoted)
            #   title="...",         (single-line, not triple-quoted)

            new_line = line
            line_replacements = 0

            # Handle inline comments: find # that's not inside a string
            # and replace addresses only in the comment portion.
            # This is tricky because # can appear in strings.
            # Simpler approach: find the comment portion carefully.
            comment_start = find_comment_start(line)
            if comment_start is not None:
                code_part = line[:comment_start]
                comment_part = line[comment_start:]
                new_comment, count = replace_addresses_in_text(comment_part, addr_map)
                line_replacements += count
                new_line = code_part + new_comment

            # Now check if a triple-quoted string opens on this line.
            # We need to check the code part (before any comment) for triple quotes.
            code_to_check = new_line if comment_start is None else new_line[:comment_start]

            for tq in ['"""', "'''"]:
                tq_start = code_to_check.find(tq)
                if tq_start != -1:
                    # Found opening triple quote. Check if it closes on the same line.
                    after_open = code_to_check[tq_start + 3:]
                    tq_close = after_open.find(tq)
                    if tq_close != -1:
                        # Single-line triple-quoted string. Replace addresses
                        # inside the string content only.
                        string_start = tq_start + 3
                        string_end = tq_start + 3 + tq_close
                        before_str = new_line[:string_start]
                        string_content = new_line[string_start:string_end]
                        after_str = new_line[string_end:]
                        new_content, count = replace_addresses_in_text(
                            string_content, addr_map
                        )
                        line_replacements += count
                        new_line = before_str + new_content + after_str
                    else:
                        # Multi-line triple-quoted string opens here.
                        # Replace addresses in the portion after the opening quotes
                        # (if any content on this line after the quotes).
                        string_start = tq_start + 3
                        before_str = new_line[:string_start]
                        after_open_content = new_line[string_start:]
                        new_content, count = replace_addresses_in_text(
                            after_open_content, addr_map
                        )
                        line_replacements += count
                        new_line = before_str + new_content
                        in_triple_quote = True
                        triple_quote_char = tq
                    break  # Only process first triple quote on the line

            total_replacements += line_replacements
            output_lines.append(new_line)

    with open(filepath, "w") as f:
        f.writelines(output_lines)

    return total_replacements


def find_comment_start(line: str) -> int | None:
    """Find the index of a # comment character that's not inside a string.

    Returns None if no comment is found.
    """
    in_string = False
    string_char = None
    i = 0
    while i < len(line):
        ch = line[i]
        if in_string:
            if ch == "\\" and i + 1 < len(line):
                i += 2  # Skip escaped character
                continue
            if ch == string_char:
                # Check for triple quote ending
                if line[i:i+3] in ['"""', "'''"]:
                    i += 3
                else:
                    i += 1
                in_string = False
                string_char = None
                continue
        else:
            if ch == "#":
                return i
            if ch in ('"', "'"):
                # Check for triple quote
                if line[i:i+3] in ['"""', "'''"]:
                    string_char = line[i:i+3]
                    in_string = True
                    i += 3
                    # Check if triple quote closes on same line
                    close_idx = line.find(string_char, i)
                    if close_idx != -1:
                        i = close_idx + 3
                        in_string = False
                        string_char = None
                    continue
                else:
                    string_char = ch
                    in_string = True
        i += 1
    return None


def main():
    print("Building address maps from source versions to 3.35K...")
    print()
    addr_map = build_address_map()
    print(f"\nTotal address map: {len(addr_map)} entries "
          f"(source addresses that differ in 3.35K)")

    # Show some examples
    print("\nSample mappings (first 20):")
    for src, tgt in sorted(addr_map.items())[:20]:
        print(f"  &{src:04X} -> &{tgt:04X}")

    print(f"\nProcessing {TARGET_FILEPATH}...")
    replacements = process_file(TARGET_FILEPATH, addr_map)
    print(f"\nDone: {replacements} address replacements made.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
