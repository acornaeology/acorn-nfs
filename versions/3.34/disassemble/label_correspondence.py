#!/usr/bin/env python3
"""Map auto-generated labels in NFS 3.34 to meaningful names from DNFS 3.60.

Parses the original Acorn assembler source, matches each reference label
independently against the NFS 3.34 ROM using opcode fingerprinting, then
identifies correspondences where our label is auto-generated.

Only auto-generated labels (c*, loop_c*, l*, sub_c*) are candidates for
replacement; hand-crafted labels are preserved.
"""

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from correlate_nfs import (
    OPCODE_LENGTHS,
    ROM_BASE,
    ROM_SIZE,
    TUBE_P4_ROM_OFFSET,
    TUBE_P4_RUNTIME,
    TUBE_P4_LENGTH,
    TUBE_P5_ROM_OFFSET,
    TUBE_P5_RUNTIME,
    TUBE_P5_LENGTH,
    TUBE_P6_ROM_OFFSET,
    TUBE_P6_RUNTIME,
    TUBE_P6_LENGTH,
    TUBE_ZP_ROM_OFFSET,
    TUBE_ZP_RUNTIME,
    TUBE_ZP_LENGTH,
    REFERENCE_DIR,
    parse_all_reference_files,
    load_rom,
)

# ============================================================
# Configuration
# ============================================================

ROM_FILEPATH = Path(__file__).parent.parent / "rom" / "nfs-3.34.rom"
JSON_FILEPATH = Path("/Users/rjs/Code/acornaeology/data/nfs/3.34.json")

# Auto-generated label patterns from py8dis
AUTO_LABEL_RE = re.compile(
    r'^(c[0-9a-f]{4,5}|loop_c[0-9a-f]+|l[0-9a-f]{4,5}|sub_c[0-9a-f]+)$'
)


# ============================================================
# Data Structures
# ============================================================

@dataclass
class LabelCorrespondence:
    """A mapping from our auto-generated label to a reference label."""
    rom_addr: int
    our_label: str
    ref_label: str
    source_file: str
    confidence: float
    matched_opcodes: int
    total_opcodes: int
    opcode_match: bool   # Whether the opcode at this exact address matches


# ============================================================
# Load disassembly labels from JSON
# ============================================================

def load_disassembly_labels(json_filepath):
    """Load labels from the structured JSON, returning {addr: [label_names]}."""
    with open(json_filepath) as f:
        data = json.load(f)

    labels_by_addr = {}
    for item in data["items"]:
        addr = item["addr"]
        item_labels = item.get("labels", [])
        if item_labels:
            labels_by_addr[addr] = item_labels

    return labels_by_addr


def is_auto_generated(label_name):
    """Check if a label name matches an auto-generated pattern."""
    return AUTO_LABEL_RE.match(label_name) is not None


# ============================================================
# Match reference labels against ROM
# ============================================================

def match_ref_labels(items, rom_data, search_start, search_length,
                     runtime_base, our_labels):
    """Match each reference label against a ROM region using opcode fingerprinting.

    Splits items at label boundaries (each label starts a new "routine").
    For each routine, builds an opcode fingerprint and slides it across
    the ROM to find the best match. Then checks if our label at that
    ROM address is auto-generated.

    Returns list of LabelCorrespondence.
    """
    # Group items into routines (split at every label)
    routines = []
    current_labels = []
    current_items = []

    for item in items:
        if item.labels:
            if current_items and current_labels:
                routines.append((current_labels, current_items))
            current_labels = list(item.labels)
            current_items = [item]
        elif item.size > 0:
            current_items.append(item)

    if current_items and current_labels:
        routines.append((current_labels, current_items))

    correspondences = []

    for labels, routine_items in routines:
        # Build opcode fingerprint
        fingerprint = []
        for item in routine_items:
            if item.opcode is not None:
                fingerprint.append(item.opcode)

        if len(fingerprint) < 2:
            continue

        # Sliding window search
        best_offset = None
        best_score = 0
        search_end = min(search_start + search_length, len(rom_data))

        for start in range(search_start, search_end):
            match_count = 0
            pos = start

            for ref_opcode in fingerprint:
                if pos >= search_end:
                    break
                rom_opcode = rom_data[pos]
                if rom_opcode == ref_opcode:
                    match_count += 1
                    inst_len = OPCODE_LENGTHS[rom_opcode]
                    if inst_len == 0:
                        break
                    pos += inst_len
                else:
                    break

            min_required = min(3, len(fingerprint))
            if match_count >= min_required and match_count > best_score:
                best_score = match_count
                best_offset = start

        if best_offset is None:
            continue

        confidence = best_score / len(fingerprint)
        if confidence < 0.5:
            continue

        rom_addr = runtime_base + (best_offset - search_start)

        # Verify opcode at the exact matched position
        opcode_match = False
        if best_offset < len(rom_data) and routine_items and routine_items[0].opcode is not None:
            opcode_match = (rom_data[best_offset] == routine_items[0].opcode)

        # Check our labels at this ROM address
        our_label_list = our_labels.get(rom_addr, [])

        for ref_label in labels:
            for our_label in our_label_list:
                if is_auto_generated(our_label):
                    correspondences.append(LabelCorrespondence(
                        rom_addr=rom_addr,
                        our_label=our_label,
                        ref_label=ref_label,
                        source_file=routine_items[0].source_file if routine_items else "",
                        confidence=confidence,
                        matched_opcodes=best_score,
                        total_opcodes=len(fingerprint),
                        opcode_match=opcode_match,
                    ))

    return correspondences


def _build_routines(items):
    """Split items at label boundaries into (labels, items) pairs."""
    routines = []
    current_labels = []
    current_items = []

    for item in items:
        if item.labels:
            if current_items and current_labels:
                routines.append((current_labels, current_items))
            current_labels = list(item.labels)
            current_items = [item]
        elif item.size > 0:
            current_items.append(item)

    if current_items and current_labels:
        routines.append((current_labels, current_items))

    return routines


def _sliding_match(fingerprint, rom_data, search_start, search_length, min_opcodes):
    """Find best sliding-window opcode match. Returns (offset, score) or (None, 0)."""
    best_offset = None
    best_score = 0
    search_end = min(search_start + search_length, len(rom_data))

    for start in range(search_start, search_end):
        match_count = 0
        pos = start

        for ref_opcode in fingerprint:
            if pos >= search_end:
                break
            if rom_data[pos] == ref_opcode:
                match_count += 1
                inst_len = OPCODE_LENGTHS[rom_data[pos]]
                if inst_len == 0:
                    break
                pos += inst_len
            else:
                break

        if match_count >= min_opcodes and match_count > best_score:
            best_score = match_count
            best_offset = start

    return best_offset, best_score


def match_ref_labels_extended(items, rom_data, search_start, search_length,
                              runtime_base, our_labels, already_matched_addrs):
    """Second pass: match short routines using extended context fingerprints.

    For routines with < 3 opcodes (too short for independent matching),
    borrows opcodes from neighboring routines to build a longer fingerprint.
    The label's position is computed from the byte offset of the borrowed
    prefix within the extended match.
    """
    CONTEXT = 4  # opcodes to borrow from each neighbor

    routines = _build_routines(items)

    # Pre-compute fingerprint and byte size for each routine
    routine_info = []
    for labels, routine_items in routines:
        fp = [item.opcode for item in routine_items if item.opcode is not None]
        byte_size = sum(item.size for item in routine_items)
        routine_info.append({
            'labels': labels,
            'items': routine_items,
            'fingerprint': fp,
            'byte_size': byte_size,
        })

    correspondences = []
    search_end = min(search_start + search_length, len(rom_data))

    for i, rd in enumerate(routine_info):
        if len(rd['fingerprint']) >= 3:
            continue  # Already handled by standard matching

        # Build prefix from previous routine
        prefix_ops = []
        prefix_bytes = 0
        if i > 0:
            prev = routine_info[i - 1]
            prev_items_with_opcodes = [(item.opcode, item.size) for item in prev['items']
                                       if item.opcode is not None]
            count = min(CONTEXT, len(prev_items_with_opcodes))
            prefix_ops = [op for op, _ in prev_items_with_opcodes[-count:]]
            prefix_bytes = sum(sz for _, sz in prev_items_with_opcodes[-count:])

        # Build suffix from next routine
        suffix_ops = []
        if i + 1 < len(routine_info):
            next_rd = routine_info[i + 1]
            suffix_ops = next_rd['fingerprint'][:CONTEXT]

        extended_fp = prefix_ops + rd['fingerprint'] + suffix_ops
        if len(extended_fp) < 4:
            continue

        best_offset, best_score = _sliding_match(
            extended_fp, rom_data, search_start, search_length,
            min_opcodes=4,
        )

        if best_offset is None:
            continue

        confidence = best_score / len(extended_fp)
        if confidence < 0.6:
            continue

        # Compute ROM address of the label (skip prefix bytes)
        rom_pos = best_offset + prefix_bytes
        rom_addr = runtime_base + (rom_pos - search_start)

        if rom_addr in already_matched_addrs:
            continue

        # Verify opcode at label position
        opcode_match = False
        if rom_pos < len(rom_data):
            if rd['items'] and rd['items'][0].opcode is not None:
                opcode_match = (rom_data[rom_pos] == rd['items'][0].opcode)
            elif rd['items'] and rd['items'][0].is_data:
                if rd['items'][0].data_bytes and rd['items'][0].data_bytes[0] is not None:
                    opcode_match = (rom_data[rom_pos] == rd['items'][0].data_bytes[0])

        our_label_list = our_labels.get(rom_addr, [])

        for ref_label in rd['labels']:
            for our_label in our_label_list:
                if is_auto_generated(our_label):
                    correspondences.append(LabelCorrespondence(
                        rom_addr=rom_addr,
                        our_label=our_label,
                        ref_label=ref_label,
                        source_file=rd['items'][0].source_file if rd['items'] else "",
                        confidence=confidence,
                        matched_opcodes=best_score,
                        total_opcodes=len(extended_fp),
                        opcode_match=opcode_match,
                    ))

    return correspondences


# ============================================================
# Output
# ============================================================

def _is_strong(c):
    """A correspondence is strong if it matched well with good confidence."""
    return c.matched_opcodes >= 3 and c.confidence >= 0.6 and c.opcode_match


def generate_report(correspondences):
    """Generate a table report and pasteable label() calls."""
    # Deduplicate: if same rom_addr appears multiple times, keep best confidence
    best = {}
    for c in correspondences:
        key = c.rom_addr
        if key not in best or c.confidence > best[key].confidence:
            best[key] = c

    sorted_corr = sorted(best.values(), key=lambda c: c.rom_addr)
    strong = [c for c in sorted_corr if _is_strong(c)]
    weak = [c for c in sorted_corr if not _is_strong(c)]

    header = (f"{'ROM Addr':<10s} {'Our Label':<20s} {'Ref Label':<20s} "
              f"{'Source':<8s} {'Conf':>5s} {'Match':>7s} {'Opcode':>6s}")
    divider = (f"{'─'*9:<10s} {'─'*19:<20s} {'─'*19:<20s} "
               f"{'─'*7:<8s} {'─'*5:>5s} {'─'*7:>7s} {'─'*6:>6s}")

    def format_row(c):
        conf_str = f"{c.confidence*100:.0f}%"
        match_str = f"{c.matched_opcodes}/{c.total_opcodes}"
        opcode_str = "yes" if c.opcode_match else "NO"
        return (f"&{c.rom_addr:04X}      {c.our_label:<20s} {c.ref_label:<20s} "
                f"{c.source_file:<8s} {conf_str:>5s} {match_str:>7s} {opcode_str:>6s}")

    lines = []
    lines.append("=" * 95)
    lines.append("Label Correspondence Report: NFS 3.34 / DNFS 3.60")
    lines.append("=" * 95)

    # Strong matches
    lines.append("")
    lines.append(f"STRONG MATCHES ({len(strong)} labels, >= 3 consecutive opcode matches)")
    lines.append("")
    lines.append(header)
    lines.append(divider)
    for c in strong:
        lines.append(format_row(c))

    # Weak matches
    if weak:
        lines.append("")
        lines.append(f"WEAK MATCHES ({len(weak)} labels, < 3 opcodes or opcode mismatch — review needed)")
        lines.append("")
        lines.append(header)
        lines.append(divider)
        for c in weak:
            lines.append(format_row(c))

    lines.append("")
    lines.append(f"Total: {len(strong)} strong + {len(weak)} weak = {len(sorted_corr)}")
    lines.append("")

    # Pasteable label() calls (strong matches only)
    lines.append("=" * 95)
    lines.append("Pasteable label() calls for nfs_334_v2.py")
    lines.append("(Strong matches only — review weak matches manually)")
    lines.append("=" * 95)
    lines.append("")

    for c in strong:
        ref_lower = c.ref_label.lower()
        comment = f"# was {c.our_label}, from {c.source_file}"
        lines.append(f'label(0x{c.rom_addr:04X}, "{ref_lower}")    {comment}')

    if weak:
        lines.append("")
        lines.append("# Weak matches (review before using):")
        for c in weak:
            ref_lower = c.ref_label.lower()
            comment = f"# was {c.our_label}, from {c.source_file}"
            reason = "opcode mismatch" if not c.opcode_match else f"only {c.matched_opcodes} opcode(s)"
            lines.append(f'# label(0x{c.rom_addr:04X}, "{ref_lower}")    '
                         f'{comment} [{reason}]')

    lines.append("")
    return "\n".join(lines)


# ============================================================
# Main
# ============================================================

def main():
    print("Label Correspondence Tool: NFS 3.34 / DNFS 3.60")
    print()

    # Parse reference source
    print("Phase 1: Parsing reference source files...")
    symbols, all_items, items_by_file = parse_all_reference_files(REFERENCE_DIR)
    print(f"  {len(symbols)} symbols, {len(all_items)} items from {len(items_by_file)} files")

    # Load ROM
    print("\nPhase 2: Loading ROM...")
    rom_data = load_rom(ROM_FILEPATH)
    print(f"  {len(rom_data)} bytes")

    # Load our labels from JSON
    print("\nPhase 3: Loading disassembly labels from JSON...")
    our_labels = load_disassembly_labels(JSON_FILEPATH)
    auto_count = sum(
        1 for labels in our_labels.values()
        for label in labels
        if is_auto_generated(label)
    )
    named_count = sum(
        1 for labels in our_labels.values()
        for label in labels
        if not is_auto_generated(label)
    )
    print(f"  {auto_count} auto-generated labels, {named_count} named labels")

    # Match reference labels against ROM
    print("\nPhase 4: Matching reference labels against ROM...")

    all_correspondences = []

    # Main ROM (NFS01-NFS10)
    main_items = []
    for fname in [f"NFS{i:02d}" for i in range(1, 11)]:
        if fname in items_by_file:
            main_items.extend(items_by_file[fname])

    print(f"  Main ROM: {len(main_items)} reference items")
    main_corr = match_ref_labels(
        main_items, rom_data, 0, ROM_SIZE, ROM_BASE, our_labels
    )
    all_correspondences.extend(main_corr)
    print(f"  Main ROM: {len(main_corr)} correspondences")

    # Tube code regions
    tube_regions = []
    if "NFS11" in items_by_file:
        tube_regions.append(("NFS11", items_by_file["NFS11"],
                             TUBE_ZP_ROM_OFFSET, TUBE_ZP_RUNTIME, TUBE_ZP_LENGTH))
    if "NFS12" in items_by_file:
        tube_regions.append(("NFS12", items_by_file["NFS12"],
                             TUBE_P4_ROM_OFFSET, TUBE_P4_RUNTIME, TUBE_P4_LENGTH))
    if "NFS13" in items_by_file:
        tube_regions.append(("NFS13", items_by_file["NFS13"],
                             TUBE_P5_ROM_OFFSET, TUBE_P5_RUNTIME,
                             TUBE_P5_LENGTH + TUBE_P6_LENGTH))

    for region_name, region_items, rom_offset, runtime_base, length in tube_regions:
        corr = match_ref_labels(
            region_items, rom_data, rom_offset, length,
            runtime_base, our_labels
        )
        all_correspondences.extend(corr)
        print(f"  {region_name}: {len(corr)} correspondences")

    print(f"  Pass 1 total: {len(all_correspondences)}")

    # Pass 2: Extended context matching for short routines
    print("\nPhase 5: Extended context matching (short routines)...")
    already_matched = {c.rom_addr for c in all_correspondences}

    ext_corr = match_ref_labels_extended(
        main_items, rom_data, 0, ROM_SIZE, ROM_BASE,
        our_labels, already_matched
    )
    all_correspondences.extend(ext_corr)
    print(f"  Main ROM: {len(ext_corr)} new correspondences from context")

    for region_name, region_items, rom_offset, runtime_base, length in tube_regions:
        ext = match_ref_labels_extended(
            region_items, rom_data, rom_offset, length,
            runtime_base, our_labels, already_matched
        )
        all_correspondences.extend(ext)
        if ext:
            print(f"  {region_name}: {len(ext)} new correspondences from context")

    print(f"\n  Grand total: {len(all_correspondences)} correspondences")

    # Generate report
    print("\nPhase 6: Generating report...\n")
    report = generate_report(all_correspondences)
    print(report)

    # Write to file
    report_filepath = Path(__file__).parent / "label_correspondence_report.txt"
    with open(report_filepath, 'w') as f:
        f.write(report)
    print(f"Report written to {report_filepath}")


if __name__ == "__main__":
    main()
