#!/usr/bin/env python3
"""Find comment() calls in the 3.35D driver whose addresses don't match
any instruction boundary in the assembly output.

These are "stale" comments — annotations carried over (usually from 3.34B)
that point at addresses which no longer correspond to an instruction start.
"""

import re
import subprocess
import sys
from pathlib import Path


def get_repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip())


def extract_comments(driver_filepath: Path) -> list[dict]:
    """Extract all comment() calls from a driver script.

    Returns a list of dicts with keys:
      - address (int)
      - text (str): the full comment text
      - line_number (int): 1-based line number of the comment() call
      - inline (bool): whether inline=True is present
    """
    source = driver_filepath.read_text()
    lines = source.splitlines()
    comments = []

    # We need to handle both single-line and multi-line comment() calls.
    # Strategy: find each `comment(0xNNNN, ...)` and parse the full call.
    i = 0
    while i < len(lines):
        line = lines[i]
        # Match the start of a comment() call
        m = re.match(r'^comment\((0x[0-9A-Fa-f]+),\s*', line)
        if not m:
            i += 1
            continue

        address = int(m.group(1), 16)
        line_number = i + 1  # 1-based

        # Accumulate the full call text to extract the comment string and
        # inline flag. We need to find the matching closing paren.
        call_lines = [line]
        paren_depth = 0
        for ch in line:
            if ch == '(':
                paren_depth += 1
            elif ch == ')':
                paren_depth -= 1

        j = i + 1
        while paren_depth > 0 and j < len(lines):
            call_lines.append(lines[j])
            for ch in lines[j]:
                if ch == '(':
                    paren_depth += 1
                elif ch == ')':
                    paren_depth -= 1
            j += 1

        call_text = "\n".join(call_lines)

        # Extract inline flag
        inline = "inline=True" in call_text

        # Extract the comment text — it's the second argument.
        # It can be a simple string or a triple-quoted string.
        # Find everything after the address and comma up to the closing paren.
        after_addr = call_text[m.end():]

        # Try to extract the string content
        text = ""
        # Triple-quoted string
        triple_match = re.match(r'"""(.*?)"""', after_addr, re.DOTALL)
        if triple_match:
            text = triple_match.group(1).strip()
        else:
            # Single-line string with double quotes
            single_match = re.match(r'"(.*?)"', after_addr)
            if single_match:
                text = single_match.group(1)
            else:
                # Try single quotes
                single_match = re.match(r"'(.*?)'", after_addr)
                if single_match:
                    text = single_match.group(1)

        comments.append({
            "address": address,
            "text": text,
            "line_number": line_number,
            "inline": inline,
        })

        i = j if j > i + 1 else i + 1

    return comments


def extract_asm_addresses(asm_filepath: Path) -> set[int]:
    """Extract all instruction/data addresses from the assembly output.

    Parses two kinds of addresses:
    1. ROM addresses from '; XXXX: NN' patterns in instruction comments
    2. Runtime addresses from ':XXXX[N]' patterns (for relocated code)

    Returns a set of all addresses found.
    """
    addresses = set()
    source = asm_filepath.read_text()

    # Pattern 1: ROM addresses in the form '; XXXX: NN NN' after instruction
    # These appear as e.g. '; 8000: 4c d4 80    L..'
    for m in re.finditer(r';\s+([0-9a-f]{4}):\s+[0-9a-f]{2}\b', source):
        addresses.add(int(m.group(1), 16))

    # Pattern 2: Runtime addresses for relocated code ':XXXX[N]'
    for m in re.finditer(r':([0-9a-f]{4})\[\d+\]', source):
        addresses.add(int(m.group(1), 16))

    return addresses


def find_comment_in_334b(
    text: str, comments_334b: list[dict]
) -> int | None:
    """Find the address of a comment with the same text in the 3.34B driver.

    Matches on the first 60 characters of the comment text to handle minor
    differences in trailing content.
    """
    if not text:
        return None

    # Exact match on full text first
    for c in comments_334b:
        if c["text"] == text:
            return c["address"]

    # Fallback: match first 60 non-whitespace-normalized chars
    normalized = " ".join(text.split())[:60]
    if len(normalized) < 10:
        return None
    for c in comments_334b:
        c_normalized = " ".join(c["text"].split())[:60]
        if c_normalized == normalized:
            return c["address"]

    return None


def main():
    repo_root = get_repo_root()

    driver_335d_filepath = (
        repo_root / "versions" / "3.35D" / "disassemble" / "disasm_nfs_335d.py"
    )
    asm_335d_filepath = (
        repo_root / "versions" / "3.35D" / "output" / "nfs-3.35D.asm"
    )
    driver_334b_filepath = (
        repo_root / "versions" / "3.34B" / "disassemble" / "disasm_nfs_334b.py"
    )

    # Check files exist
    for filepath in (driver_335d_filepath, asm_335d_filepath, driver_334b_filepath):
        if not filepath.exists():
            print(f"ERROR: {filepath} not found", file=sys.stderr)
            sys.exit(1)

    # Extract data
    comments_335d = extract_comments(driver_335d_filepath)
    comments_334b = extract_comments(driver_334b_filepath)
    asm_addresses = extract_asm_addresses(asm_335d_filepath)

    print(f"Extracted {len(comments_335d)} comment() calls from 3.35D driver")
    print(f"Extracted {len(comments_334b)} comment() calls from 3.34B driver")
    print(f"Extracted {len(asm_addresses)} unique addresses from assembly output")
    print()

    # Find stale comments
    stale = []
    for c in comments_335d:
        if c["address"] not in asm_addresses:
            addr_334b = find_comment_in_334b(c["text"], comments_334b)
            stale.append({**c, "address_334b": addr_334b})

    if not stale:
        print("No stale comments found.")
        return

    print(f"Found {len(stale)} stale comment(s):\n")
    print(
        f"{'Line':>5}  {'Address':>7}  {'Inline':>6}  "
        f"{'3.34B addr':>10}  Comment text"
    )
    print("-" * 120)

    for s in stale:
        addr_str = f"${s['address']:04X}"
        inline_str = "inline" if s["inline"] else ""
        addr_334b_str = (
            f"${s['address_334b']:04X}" if s["address_334b"] is not None else ""
        )
        text_truncated = s["text"].replace("\n", " ")[:80]
        print(
            f"{s['line_number']:>5}  {addr_str:>7}  {inline_str:>6}  "
            f"{addr_334b_str:>10}  {text_truncated}"
        )


if __name__ == "__main__":
    main()
