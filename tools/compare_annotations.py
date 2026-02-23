#!/usr/bin/env python3
"""Compare subroutine descriptions and comments across NFS ROM versions.

Extracts all subroutine() and comment() calls from the three driver scripts,
matches them by name (subroutines) or by text content (comments), and reports
differences that could be backported.

Usage:
    python compare_annotations.py [--subroutines] [--comments] [--labels]
    python compare_annotations.py  # all comparisons
"""

import ast
import re
import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True).strip())

VERSIONS = {
    "3.34": REPO_ROOT / "versions/3.34/disassemble/disasm_nfs_334.py",
    "3.34B": REPO_ROOT / "versions/3.34B/disassemble/disasm_nfs_334b.py",
    "3.35D": REPO_ROOT / "versions/3.35D/disassemble/disasm_nfs_335d.py",
}


def extract_subroutines(filepath):
    """Extract subroutine name -> (address, title, description) from a driver script."""
    text = filepath.read_text()
    results = {}

    # Match subroutine() calls - they can span multiple lines
    # Pattern: subroutine(0xADDR, "name", ...) or subroutine(0xADDR, hook=..., title="name", ...)
    # We need to handle multi-line calls, so we'll use a state machine approach

    # First, join continuation lines
    lines = text.split('\n')
    joined_lines = []
    buf = ""
    paren_depth = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            if paren_depth == 0:
                joined_lines.append(line)
                continue
        buf += (" " if buf else "") + line
        paren_depth += buf.count('(') - buf.count(')')
        if paren_depth <= 0:
            joined_lines.append(buf)
            buf = ""
            paren_depth = 0

    if buf:
        joined_lines.append(buf)

    for line in joined_lines:
        line_stripped = line.strip()
        if not line_stripped.startswith('subroutine(') and 'subroutine(' not in line_stripped:
            continue
        if line_stripped.startswith('#'):
            continue

        # Extract the subroutine call
        m = re.search(r'subroutine\s*\(', line_stripped)
        if not m:
            continue

        call_text = line_stripped[m.start():]

        # Extract address
        addr_m = re.search(r'subroutine\s*\(\s*(0x[0-9a-fA-F]+)', call_text)
        if not addr_m:
            continue
        addr = int(addr_m.group(1), 16)

        # Extract name/title - could be positional or keyword
        # Positional: subroutine(0xADDR, "name", ...)
        # Keyword: subroutine(0xADDR, hook=None, title="name", ...)
        title = None
        title_m = re.search(r'title\s*=\s*"([^"]*)"', call_text)
        if title_m:
            title = title_m.group(1)
        else:
            # Try positional: second argument as string
            pos_m = re.search(r'subroutine\s*\(\s*0x[0-9a-fA-F]+\s*,\s*"([^"]*)"', call_text)
            if pos_m:
                title = pos_m.group(1)

        # Extract description
        desc = None
        # Try triple-quoted strings
        desc_m = re.search(r'description\s*=\s*"""(.*?)"""', call_text, re.DOTALL)
        if not desc_m:
            desc_m = re.search(r'description\s*=\s*"([^"]*)"', call_text)
        if desc_m:
            desc = desc_m.group(1).strip()

        # Also check for positional description (third string argument)
        if desc is None:
            # Look for pattern: subroutine(addr, "name", "desc")
            all_strings = re.findall(r'"([^"]*)"', call_text)
            if len(all_strings) >= 2 and title == all_strings[0]:
                desc = all_strings[1] if len(all_strings) > 1 else None

        if title:
            # Normalize description whitespace
            if desc:
                desc = re.sub(r'\s+', ' ', desc).strip()
            results[title] = {
                'addr': addr,
                'title': title,
                'description': desc or '',
                'raw': call_text[:200],
            }

    return results


def extract_comments(filepath):
    """Extract address -> comment text from a driver script."""
    text = filepath.read_text()
    results = {}

    lines = text.split('\n')
    joined_lines = []
    buf = ""
    paren_depth = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            if paren_depth == 0:
                joined_lines.append(line)
                continue
        buf += (" " if buf else "") + line
        paren_depth += buf.count('(') - buf.count(')')
        if paren_depth <= 0:
            joined_lines.append(buf)
            buf = ""
            paren_depth = 0
    if buf:
        joined_lines.append(buf)

    for line in joined_lines:
        line_stripped = line.strip()
        if line_stripped.startswith('#'):
            continue

        m = re.search(r'(?<!\w)comment\s*\(', line_stripped)
        if not m:
            continue

        call_text = line_stripped[m.start():]

        addr_m = re.search(r'comment\s*\(\s*(0x[0-9a-fA-F]+)', call_text)
        if not addr_m:
            continue
        addr = int(addr_m.group(1), 16)

        # Extract comment text - try triple-quoted first, then single-quoted
        text_m = re.search(r'comment\s*\(\s*0x[0-9a-fA-F]+\s*,\s*"""(.*?)"""', call_text, re.DOTALL)
        if not text_m:
            text_m = re.search(r'comment\s*\(\s*0x[0-9a-fA-F]+\s*,\s*"(.*?)"', call_text)
        if text_m:
            comment_text = text_m.group(1).strip()
            comment_text = re.sub(r'\s+', ' ', comment_text)
            results[addr] = comment_text

    return results


def extract_labels(filepath):
    """Extract address -> label name from a driver script."""
    text = filepath.read_text()
    results = {}

    for m in re.finditer(r'label\s*\(\s*(0x[0-9a-fA-F]+)\s*,\s*"([^"]*)"', text):
        addr = int(m.group(1), 16)
        name = m.group(2)
        results[addr] = name

    return results


def build_address_map_between_versions(v1_labels, v2_labels):
    """Build a mapping from v1 addresses to v2 addresses using shared label names."""
    v1_by_name = {name: addr for addr, name in v1_labels.items()}
    v2_by_name = {name: addr for addr, name in v2_labels.items()}

    addr_map = {}  # v1_addr -> v2_addr
    for name in v1_by_name:
        if name in v2_by_name:
            addr_map[v1_by_name[name]] = v2_by_name[name]

    return addr_map


def compare_subroutines():
    """Compare subroutine descriptions across versions."""
    subs = {}
    for ver, path in VERSIONS.items():
        subs[ver] = extract_subroutines(path)

    print("=" * 72)
    print("SUBROUTINE DESCRIPTION COMPARISON")
    print("=" * 72)

    # Get all unique subroutine names
    all_names = set()
    for ver in subs:
        all_names.update(subs[ver].keys())

    differences = []
    missing = []

    for name in sorted(all_names):
        versions_with = {v: subs[v][name] for v in subs if name in subs[v]}

        if len(versions_with) < 2:
            # Only in one version
            ver = list(versions_with.keys())[0]
            missing.append((name, ver, versions_with[ver]))
            continue

        # Compare descriptions
        descs = {v: versions_with[v]['description'] for v in versions_with}
        unique_descs = set(descs.values())

        if len(unique_descs) > 1:
            differences.append((name, descs, versions_with))

    # Report differences
    if differences:
        print(f"\n### {len(differences)} subroutines with DIFFERENT descriptions:\n")
        for name, descs, info in differences:
            print(f"--- {name} ---")
            for ver in ["3.34", "3.34B", "3.35D"]:
                if ver in descs:
                    addr = info[ver]['addr']
                    print(f"  [{ver}] (0x{addr:04X}): {descs[ver][:200]}")
                    if len(descs[ver]) > 200:
                        print(f"    ...({len(descs[ver])} chars total)")
            print()
    else:
        print("\nNo subroutine description differences found.")

    # Report version-exclusive subroutines
    if missing:
        print(f"\n### {len(missing)} subroutines only in ONE version:\n")
        for name, ver, info in missing:
            print(f"  [{ver}] {name} (0x{info['addr']:04X}): {info['description'][:120]}")


def compare_comments():
    """Compare comments across versions, using label-based address mapping."""
    comments = {}
    labels = {}
    for ver, path in VERSIONS.items():
        comments[ver] = extract_comments(path)
        labels[ver] = extract_labels(path)

    print("\n" + "=" * 72)
    print("COMMENT COMPARISON")
    print("=" * 72)

    # Build address maps using shared labels
    addr_maps = {
        ("3.34", "3.34B"): build_address_map_between_versions(labels["3.34"], labels["3.34B"]),
        ("3.34B", "3.35D"): build_address_map_between_versions(labels["3.34B"], labels["3.35D"]),
        ("3.34", "3.35D"): build_address_map_between_versions(labels["3.34"], labels["3.35D"]),
    }

    # For each comment in 3.35D, find corresponding address in 3.34B and 3.34
    # and check if the comment exists/differs
    print(f"\nComment counts: 3.34={len(comments['3.34'])}, 3.34B={len(comments['3.34B'])}, 3.35D={len(comments['3.35D'])}")

    # Find comments in 3.35D that differ from or are missing in 3.34B
    map_35d_to_34b = {v: k for k, v in addr_maps[("3.34B", "3.35D")].items()}

    new_in_35d = []
    different = []
    for addr_35d, text_35d in sorted(comments["3.35D"].items()):
        addr_34b = map_35d_to_34b.get(addr_35d)
        if addr_34b is None:
            new_in_35d.append((addr_35d, text_35d, "no address mapping"))
            continue

        if addr_34b not in comments["3.34B"]:
            new_in_35d.append((addr_35d, text_35d, f"mapped to 0x{addr_34b:04X} but no comment there"))
            continue

        text_34b = comments["3.34B"][addr_34b]
        if text_35d != text_34b:
            different.append((addr_35d, addr_34b, text_35d, text_34b))

    # Also find comments in 3.34B not in 3.35D
    map_34b_to_35d = addr_maps[("3.34B", "3.35D")]
    only_in_34b = []
    for addr_34b, text_34b in sorted(comments["3.34B"].items()):
        addr_35d = map_34b_to_35d.get(addr_34b)
        if addr_35d is None:
            only_in_34b.append((addr_34b, text_34b, "no address mapping"))
            continue
        if addr_35d not in comments["3.35D"]:
            only_in_34b.append((addr_34b, text_34b, f"mapped to 0x{addr_35d:04X} but no comment there"))

    if different:
        print(f"\n### {len(different)} comments that DIFFER between 3.35D and 3.34B:\n")
        for addr_35d, addr_34b, text_35d, text_34b in different:
            print(f"  [3.35D 0x{addr_35d:04X} / 3.34B 0x{addr_34b:04X}]")
            print(f"    3.35D: {text_35d[:150]}")
            print(f"    3.34B: {text_34b[:150]}")
            print()
    else:
        print("\nNo comment text differences found between 3.35D and 3.34B.")

    if new_in_35d:
        print(f"\n### {len(new_in_35d)} comments in 3.35D with no equivalent in 3.34B:\n")
        for addr, text, reason in new_in_35d:
            print(f"  0x{addr:04X}: {text[:120]} ({reason})")

    if only_in_34b:
        print(f"\n### {len(only_in_34b)} comments in 3.34B with no equivalent in 3.35D:\n")
        for addr, text, reason in only_in_34b:
            print(f"  0x{addr:04X}: {text[:120]} ({reason})")

    # Now compare 3.34 vs 3.34B
    map_34b_to_34 = {v: k for k, v in addr_maps[("3.34", "3.34B")].items()}
    new_in_34b = []
    diff_34_34b = []
    for addr_34b, text_34b in sorted(comments["3.34B"].items()):
        addr_34 = map_34b_to_34.get(addr_34b)
        if addr_34 is None:
            new_in_34b.append((addr_34b, text_34b, "no address mapping"))
            continue
        if addr_34 not in comments["3.34"]:
            new_in_34b.append((addr_34b, text_34b, f"mapped to 0x{addr_34:04X} but no comment there"))
            continue
        text_34 = comments["3.34"][addr_34]
        if text_34b != text_34:
            diff_34_34b.append((addr_34b, addr_34, text_34b, text_34))

    if diff_34_34b:
        print(f"\n### {len(diff_34_34b)} comments that DIFFER between 3.34B and 3.34:\n")
        for addr_34b, addr_34, text_34b, text_34 in diff_34_34b:
            print(f"  [3.34B 0x{addr_34b:04X} / 3.34 0x{addr_34:04X}]")
            print(f"    3.34B: {text_34b[:150]}")
            print(f"    3.34:  {text_34[:150]}")
            print()
    else:
        print("\nNo comment text differences found between 3.34B and 3.34.")

    if new_in_34b:
        print(f"\n### {len(new_in_34b)} comments in 3.34B with no equivalent in 3.34:\n")
        for addr, text, reason in new_in_34b:
            print(f"  0x{addr:04X}: {text[:120]} ({reason})")


def compare_labels():
    """Compare label names across versions."""
    labels = {}
    for ver, path in VERSIONS.items():
        labels[ver] = extract_labels(path)

    print("\n" + "=" * 72)
    print("LABEL COMPARISON")
    print("=" * 72)

    # Build address maps
    addr_maps = {
        ("3.34", "3.34B"): build_address_map_between_versions(labels["3.34"], labels["3.34B"]),
        ("3.34B", "3.35D"): build_address_map_between_versions(labels["3.34B"], labels["3.35D"]),
    }

    # Find labels that exist in 3.35D but not in 3.34B (by mapped address)
    map_35d_to_34b = {v: k for k, v in addr_maps[("3.34B", "3.35D")].items()}

    # Labels in 3.35D where the mapped 3.34B address has no label or different label
    new_labels_35d = []
    renamed_labels = []
    for addr_35d, name_35d in sorted(labels["3.35D"].items()):
        addr_34b = map_35d_to_34b.get(addr_35d)
        if addr_34b is None:
            # Check if this label name exists in 3.34B at any address
            if name_35d not in {n for n in labels["3.34B"].values()}:
                new_labels_35d.append((addr_35d, name_35d))
            continue
        if addr_34b in labels["3.34B"]:
            name_34b = labels["3.34B"][addr_34b]
            if name_35d != name_34b:
                renamed_labels.append((addr_35d, addr_34b, name_35d, name_34b))
        else:
            new_labels_35d.append((addr_35d, name_35d))

    # Labels in 3.34B not in 3.35D
    map_34b_to_35d = addr_maps[("3.34B", "3.35D")]
    missing_in_35d = []
    for addr_34b, name_34b in sorted(labels["3.34B"].items()):
        addr_35d = map_34b_to_35d.get(addr_34b)
        if addr_35d is None:
            if name_34b not in {n for n in labels["3.35D"].values()}:
                missing_in_35d.append((addr_34b, name_34b))
            continue
        if addr_35d not in labels["3.35D"]:
            missing_in_35d.append((addr_34b, name_34b))

    print(f"\nLabel counts: 3.34={len(labels['3.34'])}, 3.34B={len(labels['3.34B'])}, 3.35D={len(labels['3.35D'])}")

    if renamed_labels:
        print(f"\n### {len(renamed_labels)} labels RENAMED between 3.34B and 3.35D:\n")
        for addr_35d, addr_34b, name_35d, name_34b in renamed_labels:
            print(f"  0x{addr_34b:04X}/0x{addr_35d:04X}: {name_34b} -> {name_35d}")

    if new_labels_35d:
        print(f"\n### {len(new_labels_35d)} labels in 3.35D not in 3.34B:\n")
        for addr, name in new_labels_35d:
            print(f"  0x{addr:04X}: {name}")

    if missing_in_35d:
        print(f"\n### {len(missing_in_35d)} labels in 3.34B not in 3.35D:\n")
        for addr, name in missing_in_35d:
            print(f"  0x{addr:04X}: {name}")

    # Now compare 3.34 vs 3.34B
    map_34b_to_34 = {v: k for k, v in addr_maps[("3.34", "3.34B")].items()}
    renamed_34 = []
    new_in_34b = []
    missing_in_34b = []

    for addr_34b, name_34b in sorted(labels["3.34B"].items()):
        addr_34 = map_34b_to_34.get(addr_34b)
        if addr_34 is None:
            if name_34b not in {n for n in labels["3.34"].values()}:
                new_in_34b.append((addr_34b, name_34b))
            continue
        if addr_34 in labels["3.34"]:
            name_34 = labels["3.34"][addr_34]
            if name_34b != name_34:
                renamed_34.append((addr_34b, addr_34, name_34b, name_34))
        else:
            new_in_34b.append((addr_34b, name_34b))

    for addr_34, name_34 in sorted(labels["3.34"].items()):
        addr_34b = addr_maps[("3.34", "3.34B")].get(addr_34)
        if addr_34b is None:
            if name_34 not in {n for n in labels["3.34B"].values()}:
                missing_in_34b.append((addr_34, name_34))
            continue
        if addr_34b not in labels["3.34B"]:
            missing_in_34b.append((addr_34, name_34))

    if renamed_34:
        print(f"\n### {len(renamed_34)} labels RENAMED between 3.34 and 3.34B:\n")
        for addr_34b, addr_34, name_34b, name_34 in renamed_34:
            print(f"  0x{addr_34:04X}/0x{addr_34b:04X}: {name_34} -> {name_34b}")

    if new_in_34b:
        print(f"\n### {len(new_in_34b)} labels in 3.34B not in 3.34:\n")
        for addr, name in new_in_34b:
            print(f"  0x{addr:04X}: {name}")

    if missing_in_34b:
        print(f"\n### {len(missing_in_34b)} labels in 3.34 not in 3.34B:\n")
        for addr, name in missing_in_34b:
            print(f"  0x{addr:04X}: {name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    do_all = not args

    if do_all or "--subroutines" in args:
        compare_subroutines()
    if do_all or "--comments" in args:
        compare_comments()
    if do_all or "--labels" in args:
        compare_labels()
