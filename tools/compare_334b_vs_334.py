"""Compare annotations between NFS 3.34B and 3.34 disassembly driver scripts.

Extracts subroutine(), label(), constant(), and comment() calls from both
scripts and reports differences in names, descriptions, and text.
"""

import ast
import re
import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True).strip())

SCRIPT_334B = REPO_ROOT / "versions/3.34B/disassemble/disasm_nfs_334b.py"
SCRIPT_334 = REPO_ROOT / "versions/3.34/disassemble/disasm_nfs_334.py"


def read_file(filepath):
    return filepath.read_text(encoding="utf-8")


def find_balanced_call(text, start_pos):
    """Given text and the position of the opening '(' of a function call,
    return the full string up to and including the matching ')'.
    Handles nested parens, strings (single/double/triple-quoted)."""
    depth = 0
    i = start_pos
    in_string = None  # None, or the quote character(s)
    while i < len(text):
        c = text[i]
        # Handle escape sequences inside strings
        if in_string and c == '\\':
            i += 2
            continue
        # Check for triple-quoted strings
        if not in_string and text[i:i+3] in ('"""', "'''"):
            in_string = text[i:i+3]
            i += 3
            continue
        if in_string and len(in_string) == 3 and text[i:i+3] == in_string:
            in_string = None
            i += 3
            continue
        # Check for single-quoted strings
        if not in_string and c in ('"', "'"):
            in_string = c
            i += 1
            continue
        if in_string and len(in_string) == 1 and c == in_string:
            in_string = None
            i += 1
            continue
        # Track parens only outside strings
        if not in_string:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    return text[start_pos:i+1]
        i += 1
    return None


def extract_all_calls(text, func_name):
    """Find all top-level calls to func_name(...) in text.
    Returns list of (match_start, full_call_string) tuples."""
    results = []
    # Match both 'func_name(' and 'hook_func_name(' patterns
    pattern = re.compile(r'(?:^|\n)\s*(?:hook_)?' + re.escape(func_name) + r'\s*\(', re.MULTILINE)
    for m in pattern.finditer(text):
        # Find the position of the opening paren
        paren_pos = text.index('(', m.start() + 1)
        full_call = find_balanced_call(text, paren_pos)
        if full_call:
            # Reconstruct the full statement
            prefix = text[m.start():paren_pos].lstrip('\n')
            results.append((m.start(), prefix + full_call))
    return results


def parse_subroutine_call(call_text):
    """Parse a subroutine() call string to extract addr, name, title, description.
    Returns dict with keys: addr, name, title, description (any may be None)."""
    result = {"addr": None, "name": None, "title": None, "description": None}

    # Extract the arguments part (between outermost parens)
    paren_start = call_text.index('(')
    inner = call_text[paren_start:]  # includes parens

    # Try to parse as a Python expression by wrapping in a dummy function call
    # We'll use ast to parse a fake module: _f(args)
    try:
        fake_code = f"_f{inner}"
        tree = ast.parse(fake_code, mode='eval')
        call_node = tree.body
        # Positional args
        for i, arg in enumerate(call_node.args):
            if i == 0:
                # First arg is the address
                if isinstance(arg, ast.Constant):
                    result["addr"] = arg.value
                elif isinstance(arg, ast.Num):  # older Python
                    result["addr"] = arg.n
            elif i == 1:
                # Second positional arg could be the name (string) or a variable
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    result["name"] = arg.value
        # Keyword args
        for kw in call_node.keywords:
            if kw.arg == "title" and isinstance(kw.value, ast.Constant):
                result["title"] = kw.value.value
            elif kw.arg == "description" and isinstance(kw.value, ast.Constant):
                result["description"] = kw.value.value
    except (SyntaxError, ValueError):
        # Fallback: regex extraction
        addr_m = re.match(r'\(\s*(0x[0-9A-Fa-f]+)', inner)
        if addr_m:
            result["addr"] = int(addr_m.group(1), 16)
        name_m = re.search(r'^\(\s*0x[0-9A-Fa-f]+\s*,\s*"([^"]+)"', inner)
        if name_m:
            result["name"] = name_m.group(1)
        title_m = re.search(r'title\s*=\s*"([^"]*)"', call_text)
        if title_m:
            result["title"] = title_m.group(1)
        desc_m = re.search(r'description\s*=\s*"""\\?\s*(.*?)"""', call_text, re.DOTALL)
        if desc_m:
            result["description"] = desc_m.group(1).strip()

    return result


def extract_subroutines(text):
    """Extract all subroutine() calls, returning dict of {name: {title, description, addr}}.

    For subroutines without an explicit name argument, looks up the label()
    call at the same address to find the name.
    """
    # First, build an address-to-name map from label() calls
    labels_by_addr = {}
    label_pattern = re.compile(r'label\(\s*0x([0-9A-Fa-f]+)\s*,\s*"([^"]+)"\s*\)')
    for m in label_pattern.finditer(text):
        addr = int(m.group(1), 16)
        name = m.group(2)
        labels_by_addr[addr] = name

    # Also get names from hook_subroutine() calls
    hook_pattern = re.compile(r'hook_subroutine\(\s*0x([0-9A-Fa-f]+)\s*,\s*"([^"]+)"')
    for m in hook_pattern.finditer(text):
        addr = int(m.group(1), 16)
        name = m.group(2)
        labels_by_addr[addr] = name

    results = {}
    calls = extract_all_calls(text, "subroutine")

    for _, call_text in calls:
        # Skip hook_subroutine calls (we only want subroutine() calls)
        stripped = call_text.lstrip()
        if stripped.startswith("hook_subroutine"):
            continue

        parsed = parse_subroutine_call(call_text)
        addr = parsed["addr"]
        name = parsed["name"]
        title = parsed["title"]
        description = parsed["description"]

        # If no name in the call, look up by address
        if name is None and addr is not None:
            name = labels_by_addr.get(addr)

        # Use name if available, otherwise fall back to title as key
        # (anonymous subroutines are matched by title between versions)
        key = name
        if key is None and title:
            key = f"[anon: {title}]"
        elif key is None:
            key = f"[anon@&{addr:04X}]"

        if key is not None:
            results[key] = {
                "addr": addr,
                "name": name,
                "title": title or "",
                "description": (description or "").strip(),
            }

    return results


def extract_labels(text):
    """Extract all label() calls, returning dict of {name: addr}."""
    results = {}
    pattern = re.compile(r'label\(\s*0x([0-9A-Fa-f]+)\s*,\s*"([^"]+)"\s*\)')
    for m in pattern.finditer(text):
        addr = int(m.group(1), 16)
        name = m.group(2)
        results[name] = addr
    return results


def extract_constants(text):
    """Extract all constant() calls, returning dict of {name: value_str}."""
    results = {}
    # Match both hex (0x...) and decimal numeric values
    pattern = re.compile(r'constant\(\s*(0x[0-9A-Fa-f]+|\d+)\s*,\s*"([^"]+)"\s*\)')
    for m in pattern.finditer(text):
        value = m.group(1)
        name = m.group(2)
        results[name] = value
    return results


def extract_comments(text):
    """Extract all comment() calls, returning list of (addr, comment_text, inline_flag).

    Uses balanced-paren extraction and ast parsing for robustness.
    """
    results = []
    calls = extract_all_calls(text, "comment")

    for _, call_text in calls:
        # Parse using ast
        paren_start = call_text.index('(')
        inner = call_text[paren_start:]
        try:
            fake_code = f"_f{inner}"
            tree = ast.parse(fake_code, mode='eval')
            call_node = tree.body

            addr = None
            comment_text = None
            inline = False

            for i, arg in enumerate(call_node.args):
                if i == 0:
                    if isinstance(arg, ast.Constant):
                        addr = arg.value
                elif i == 1:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        comment_text = arg.value

            for kw in call_node.keywords:
                if kw.arg == "inline" and isinstance(kw.value, ast.Constant):
                    inline = kw.value.value

            if addr is not None and comment_text is not None:
                results.append((addr, comment_text.strip(), inline))
        except (SyntaxError, ValueError):
            # Fallback: regex
            addr_m = re.match(r'comment\(\s*0x([0-9A-Fa-f]+)', call_text)
            if not addr_m:
                continue
            addr = int(addr_m.group(1), 16)
            # Try triple-quoted
            desc_m = re.search(r'"""\\?\s*(.*?)"""', call_text, re.DOTALL)
            if desc_m:
                comment_text = desc_m.group(1).strip()
            else:
                # Single-quoted
                sq_m = re.search(r'(?:,\s*)"((?:[^"\\]|\\.)*)"', call_text)
                if sq_m:
                    comment_text = sq_m.group(1).strip()
            inline = bool(re.search(r'inline\s*=\s*True', call_text))
            if comment_text is not None:
                results.append((addr, comment_text, inline))

    return results


def normalize_description(desc):
    """Normalize a description for comparison by removing address-specific references."""
    # Replace hex addresses like &XXXX or $XXXX or 0xXXXX with a placeholder
    normalized = re.sub(r'[&$]([0-9A-Fa-f]{4})\b', '&ADDR', desc)
    normalized = re.sub(r'0x([0-9A-Fa-f]{4})\b', '0xADDR', normalized)
    # Normalize whitespace
    normalized = ' '.join(normalized.split())
    return normalized


def normalize_comment(text):
    """Normalize comment text for comparison."""
    normalized = re.sub(r'[&$]([0-9A-Fa-f]{4})\b', '&ADDR', text)
    normalized = re.sub(r'0x([0-9A-Fa-f]{4})\b', '0xADDR', normalized)
    # Also normalize "3.34B" vs "3.34" version strings
    normalized = re.sub(r'3\.34B?', '3.34x', normalized)
    # Normalize whitespace
    normalized = ' '.join(normalized.split())
    return normalized


def main():
    text_334b = read_file(SCRIPT_334B)
    text_334 = read_file(SCRIPT_334)

    print("=" * 72)
    print("Comparison: NFS 3.34B vs 3.34 disassembly driver scripts")
    print("=" * 72)

    # --- Subroutines ---
    subs_334b = extract_subroutines(text_334b)
    subs_334 = extract_subroutines(text_334)

    print(f"\n{'=' * 72}")
    print("SUBROUTINES")
    print(f"{'=' * 72}")
    print(f"  3.34B: {len(subs_334b)} subroutines extracted")
    print(f"  3.34:  {len(subs_334)} subroutines extracted")

    names_334b = set(subs_334b.keys())
    names_334 = set(subs_334.keys())

    only_in_334b = sorted(names_334b - names_334)
    only_in_334 = sorted(names_334 - names_334b)
    common = sorted(names_334b & names_334)

    if only_in_334b:
        print(f"\n  --- Subroutines in 3.34B but NOT in 3.34 ({len(only_in_334b)}) ---")
        for name in only_in_334b:
            info = subs_334b[name]
            print(f"    {name} (at &{info['addr']:04X})")
            print(f"      Title: {info['title']}")
            desc_lines = info['description'].split('\n')
            for line in desc_lines[:3]:
                print(f"      {line}")
            if len(desc_lines) > 3:
                print("      ...")
    else:
        print("\n  --- No subroutines unique to 3.34B ---")

    if only_in_334:
        print(f"\n  --- Subroutines in 3.34 but NOT in 3.34B ({len(only_in_334)}) ---")
        for name in only_in_334:
            info = subs_334[name]
            print(f"    {name} (at &{info['addr']:04X})")
            print(f"      Title: {info['title']}")
            desc_lines = info['description'].split('\n')
            for line in desc_lines[:3]:
                print(f"      {line}")
            if len(desc_lines) > 3:
                print("      ...")
    else:
        print("\n  --- No subroutines unique to 3.34 ---")

    # Compare descriptions of common subroutines
    diff_descs = []
    for name in common:
        desc_b = normalize_description(subs_334b[name]["description"])
        desc_a = normalize_description(subs_334[name]["description"])
        title_b = subs_334b[name]["title"]
        title_a = subs_334[name]["title"]
        if desc_b != desc_a or title_b != title_a:
            diff_descs.append(name)

    if diff_descs:
        print(f"\n  --- Subroutines with DIFFERENT descriptions ({len(diff_descs)}) ---")
        for name in diff_descs:
            print(f"\n    {name}:")
            if subs_334b[name]["title"] != subs_334[name]["title"]:
                print(f"      3.34B title: {subs_334b[name]['title']}")
                print(f"      3.34  title: {subs_334[name]['title']}")
            norm_b = normalize_description(subs_334b[name]["description"])
            norm_a = normalize_description(subs_334[name]["description"])
            if norm_b != norm_a:
                # Show only the differing lines
                lines_b = subs_334b[name]["description"].split("\n")
                lines_a = subs_334[name]["description"].split("\n")
                shown = False
                for i, (lb, la) in enumerate(zip(lines_b, lines_a)):
                    if lb != la:
                        if not shown:
                            print("      Description differences (line-by-line):")
                            shown = True
                        print(f"        Line {i+1}:")
                        print(f"          3.34B: {lb}")
                        print(f"          3.34:  {la}")
                if len(lines_b) != len(lines_a):
                    print(f"      (3.34B has {len(lines_b)} lines, 3.34 has {len(lines_a)} lines)")
    else:
        print("\n  --- All common subroutine descriptions match (after address normalization) ---")

    # --- Labels ---
    labels_334b = extract_labels(text_334b)
    labels_334 = extract_labels(text_334)

    print(f"\n{'=' * 72}")
    print("LABELS")
    print(f"{'=' * 72}")
    print(f"  3.34B: {len(labels_334b)} labels extracted")
    print(f"  3.34:  {len(labels_334)} labels extracted")

    lnames_334b = set(labels_334b.keys())
    lnames_334 = set(labels_334.keys())

    labels_only_334b = sorted(lnames_334b - lnames_334)
    labels_only_334 = sorted(lnames_334 - lnames_334b)

    if labels_only_334b:
        print(f"\n  --- Labels in 3.34B but NOT in 3.34 ({len(labels_only_334b)}) ---")
        for name in labels_only_334b:
            print(f"    {name} (at &{labels_334b[name]:04X})")
    else:
        print("\n  --- No labels unique to 3.34B ---")

    if labels_only_334:
        print(f"\n  --- Labels in 3.34 but NOT in 3.34B ({len(labels_only_334)}) ---")
        for name in labels_only_334:
            print(f"    {name} (at &{labels_334[name]:04X})")
    else:
        print("\n  --- No labels unique to 3.34 ---")

    # --- Constants ---
    consts_334b = extract_constants(text_334b)
    consts_334 = extract_constants(text_334)

    print(f"\n{'=' * 72}")
    print("CONSTANTS")
    print(f"{'=' * 72}")
    print(f"  3.34B: {len(consts_334b)} constants extracted")
    print(f"  3.34:  {len(consts_334)} constants extracted")

    cnames_334b = set(consts_334b.keys())
    cnames_334 = set(consts_334.keys())

    consts_only_334b = sorted(cnames_334b - cnames_334)
    consts_only_334 = sorted(cnames_334 - cnames_334b)

    if consts_only_334b:
        print(f"\n  --- Constants in 3.34B but NOT in 3.34 ({len(consts_only_334b)}) ---")
        for name in consts_only_334b:
            print(f"    {name} = {consts_334b[name]}")
    else:
        print("\n  --- No constants unique to 3.34B ---")

    if consts_only_334:
        print(f"\n  --- Constants in 3.34 but NOT in 3.34B ({len(consts_only_334)}) ---")
        for name in consts_only_334:
            print(f"    {name} = {consts_334[name]}")
    else:
        print("\n  --- No constants unique to 3.34 ---")

    common_consts = sorted(cnames_334b & cnames_334)
    diff_consts = []
    for name in common_consts:
        if consts_334b[name] != consts_334[name]:
            diff_consts.append(name)
    if diff_consts:
        print(f"\n  --- Constants with different values ({len(diff_consts)}) ---")
        for name in diff_consts:
            print(f"    {name}: 3.34B={consts_334b[name]}  3.34={consts_334[name]}")
    else:
        print("\n  --- All common constants have matching values ---")

    # --- Comments ---
    comments_334b = extract_comments(text_334b)
    comments_334 = extract_comments(text_334)

    print(f"\n{'=' * 72}")
    print("COMMENTS")
    print(f"{'=' * 72}")
    print(f"  3.34B: {len(comments_334b)} comments extracted")
    print(f"  3.34:  {len(comments_334)} comments extracted")

    # Build normalized text sets for comparison
    norm_comments_334b = {}
    for addr, ctext, inline in comments_334b:
        norm = normalize_comment(ctext)
        norm_comments_334b[norm] = (addr, ctext, inline)

    norm_comments_334 = {}
    for addr, ctext, inline in comments_334:
        norm = normalize_comment(ctext)
        norm_comments_334[norm] = (addr, ctext, inline)

    norm_set_b = set(norm_comments_334b.keys())
    norm_set_a = set(norm_comments_334.keys())

    comments_only_334b = sorted(norm_set_b - norm_set_a)
    comments_only_334 = sorted(norm_set_a - norm_set_b)

    if comments_only_334b:
        print(f"\n  --- Comments in 3.34B but NOT in 3.34 ({len(comments_only_334b)}) ---")
        for norm in comments_only_334b:
            addr, ctext, inline = norm_comments_334b[norm]
            preview = ctext[:120].replace("\n", " // ")
            print(f"    &{addr:04X}: {preview}{'...' if len(ctext) > 120 else ''}")
            if inline:
                print("           (inline)")
    else:
        print("\n  --- No comments unique to 3.34B ---")

    if comments_only_334:
        print(f"\n  --- Comments in 3.34 but NOT in 3.34B ({len(comments_only_334)}) ---")
        for norm in comments_only_334:
            addr, ctext, inline = norm_comments_334[norm]
            preview = ctext[:120].replace("\n", " // ")
            print(f"    &{addr:04X}: {preview}{'...' if len(ctext) > 120 else ''}")
            if inline:
                print("           (inline)")
    else:
        print("\n  --- No comments unique to 3.34 ---")

    # --- Summary ---
    print(f"\n{'=' * 72}")
    print("SUMMARY")
    print(f"{'=' * 72}")
    total_diffs = (
        len(only_in_334b) + len(only_in_334)
        + len(diff_descs)
        + len(labels_only_334b) + len(labels_only_334)
        + len(consts_only_334b) + len(consts_only_334) + len(diff_consts)
        + len(comments_only_334b) + len(comments_only_334)
    )
    print(f"  Subroutines only in 3.34B: {len(only_in_334b)}")
    print(f"  Subroutines only in 3.34:  {len(only_in_334)}")
    print(f"  Subroutines with different descriptions: {len(diff_descs)}")
    print(f"  Labels only in 3.34B: {len(labels_only_334b)}")
    print(f"  Labels only in 3.34:  {len(labels_only_334)}")
    print(f"  Constants only in 3.34B: {len(consts_only_334b)}")
    print(f"  Constants only in 3.34:  {len(consts_only_334)}")
    print(f"  Constants with different values: {len(diff_consts)}")
    print(f"  Comments only in 3.34B: {len(comments_only_334b)}")
    print(f"  Comments only in 3.34:  {len(comments_only_334)}")
    print(f"  TOTAL DIFFERENCES: {total_diffs}")


if __name__ == "__main__":
    main()
