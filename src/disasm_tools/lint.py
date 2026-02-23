"""Lint annotation addresses in NFS ROM disassembly driver scripts.

Validates that every comment(), subroutine(), and label() address in the
driver script corresponds to an actual item (instruction or data) address
in the py8dis JSON output. Catches stale addresses carried over from a
source version during auto-generation of a new driver script.
"""

import json
import re
import sys
from pathlib import Path


def extract_annotations(driver_filepath):
    """Extract all annotation addresses from a driver script.

    Parses comment(), subroutine(), and label() calls.
    Returns a list of dicts with keys: kind, address, line_number, detail.
    """
    source = driver_filepath.read_text()
    lines = source.splitlines()
    annotations = []

    for line_number, line in enumerate(lines, 1):
        stripped = line.lstrip()

        # comment(0xADDR, ...)
        m = re.match(r'comment\(\s*(0x[0-9A-Fa-f]+)', stripped)
        if m:
            annotations.append({
                "kind": "comment",
                "address": int(m.group(1), 16),
                "line_number": line_number,
                "detail": None,
            })
            continue

        # subroutine(0xADDR, ...) — also detect is_entry_point=False
        m = re.match(r'subroutine\(\s*(0x[0-9A-Fa-f]+)', stripped)
        if m:
            # Accumulate the full call to check for is_entry_point=False
            call_text = line
            paren_depth = line.count('(') - line.count(')')
            j = line_number  # 0-based: line_number is 1-based, so j indexes next line
            while paren_depth > 0 and j < len(lines):
                call_text += lines[j]
                paren_depth += lines[j].count('(') - lines[j].count(')')
                j += 1

            is_entry_point = "is_entry_point=False" not in call_text
            annotations.append({
                "kind": "subroutine",
                "address": int(m.group(1), 16),
                "line_number": line_number,
                "detail": "entry_point" if is_entry_point else "metadata_only",
            })
            continue

        # label(0xADDR, ...)
        m = re.match(r'label\(\s*(0x[0-9A-Fa-f]+)', stripped)
        if m:
            annotations.append({
                "kind": "label",
                "address": int(m.group(1), 16),
                "line_number": line_number,
                "detail": None,
            })
            continue

    return annotations


def load_valid_addresses(json_filepath):
    """Load valid addresses from the py8dis JSON output.

    Includes item addresses (instructions and data), external label
    addresses (workspace RAM locations named for operand references),
    and subroutine addresses (which may be in overlapping code regions
    where the same bytes decode as different instructions depending on
    the entry point).
    """
    data = json.loads(json_filepath.read_text())
    addresses = {item['addr'] for item in data['items']}
    for addr in data.get('external_labels', {}).values():
        addresses.add(addr)
    for sub in data.get('subroutines', []):
        addresses.add(sub['addr'])
    return addresses


def lint(version_dirpath, version):
    """Validate annotation addresses against the JSON output.

    Returns 0 on success, 1 on failure.
    """
    script_filename = f"disasm_nfs_{version.replace('.', '').lower()}.py"
    driver_filepath = version_dirpath / "disassemble" / script_filename
    json_filepath = version_dirpath / "output" / f"nfs-{version}.json"

    if not driver_filepath.exists():
        print(f"Error: driver script not found: {driver_filepath}", file=sys.stderr)
        return 1

    if not json_filepath.exists():
        print(f"Error: JSON output not found: {json_filepath}", file=sys.stderr)
        print("Run 'acorn-nfs-disasm-tool disassemble' first.", file=sys.stderr)
        return 1

    annotations = extract_annotations(driver_filepath)
    valid_addresses = load_valid_addresses(json_filepath)

    counts = {"comment": 0, "subroutine": 0, "label": 0}
    errors = []
    warnings = []

    for ann in annotations:
        counts[ann["kind"]] += 1

        if ann["address"] not in valid_addresses:
            msg = (
                f"  line {ann['line_number']}: "
                f"{ann['kind']}(0x{ann['address']:04X}) "
                f"— not a valid item address"
            )

            if ann["kind"] == "subroutine" and ann["detail"] == "metadata_only":
                warnings.append(msg)
            else:
                errors.append(msg)

    if errors:
        print(
            f"Lint FAILED: {len(errors)} annotation(s) at invalid addresses ({version})",
            file=sys.stderr,
        )
        for msg in errors:
            print(msg, file=sys.stderr)
        if warnings:
            print(
                f"\n  Plus {len(warnings)} warning(s) "
                f"(is_entry_point=False subroutines):",
                file=sys.stderr,
            )
            for msg in warnings:
                print(msg, file=sys.stderr)
        return 1

    summary = (
        f"{counts['comment']} comments, "
        f"{counts['subroutine']} subroutines, "
        f"{counts['label']} labels checked"
    )
    print(f"Lint passed: {summary} ({version})")

    if warnings:
        print(f"  {len(warnings)} warning(s) (is_entry_point=False subroutines):")
        for msg in warnings:
            print(msg)

    return 0
