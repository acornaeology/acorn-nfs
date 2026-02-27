#!/usr/bin/env python3
"""Map auto-generated labels in NFS 3.40 to meaningful names from DNFS 3.60.

Adapts the 3.34 label_correspondence tool for 3.40's relocated block offsets.
"""

import sys
from pathlib import Path

# Add 3.34's disassemble directory to import path
_334_dir = Path(__file__).resolve().parent.parent.parent / "3.34" / "disassemble"
sys.path.insert(0, str(_334_dir))

from correlate_nfs import (
    OPCODE_LENGTHS,
    ROM_BASE,
    ROM_SIZE,
    REFERENCE_DIR,
    parse_all_reference_files,
    load_rom,
)
from label_correspondence import (
    load_disassembly_labels,
    is_auto_generated,
    match_ref_labels,
    match_ref_labels_extended,
    generate_report,
)

# 3.40 relocated block offsets
TUBE_ZP_ROM_OFFSET = 0x131C   # &931C in ROM → runtime &0016
TUBE_ZP_RUNTIME    = 0x0016
TUBE_ZP_LENGTH     = 0x61

TUBE_P4_ROM_OFFSET = 0x135D   # &935D in ROM → runtime &0400
TUBE_P4_RUNTIME    = 0x0400
TUBE_P4_LENGTH     = 0x100

TUBE_P5_ROM_OFFSET = 0x1456   # &9456 in ROM → runtime &0500
TUBE_P5_RUNTIME    = 0x0500
TUBE_P5_LENGTH     = 0x100

TUBE_P6_ROM_OFFSET = 0x1556   # &9556 in ROM → runtime &0600
TUBE_P6_RUNTIME    = 0x0600
TUBE_P6_LENGTH     = 0x100

ROM_FILEPATH = Path(__file__).parent.parent / "rom" / "nfs-3.40.rom"
JSON_FILEPATH = Path(__file__).parent.parent / "output" / "nfs-3.40.json"


def main():
    print("Label Correspondence Tool: NFS 3.40 / DNFS 3.60")
    print()

    print("Phase 1: Parsing reference source files...")
    symbols, all_items, items_by_file = parse_all_reference_files(REFERENCE_DIR)
    print(f"  {len(symbols)} symbols, {len(all_items)} items from {len(items_by_file)} files")

    print("\nPhase 2: Loading ROM...")
    rom_data = load_rom(ROM_FILEPATH)
    print(f"  {len(rom_data)} bytes")

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

    # Pass 2: Extended context matching
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

    print("\nPhase 6: Generating report...\n")
    report = generate_report(all_correspondences)
    # Fix report title
    report = report.replace("NFS 3.34", "NFS 3.40")
    report = report.replace("disasm_nfs_334.py", "disasm_nfs_340.py")
    print(report)

    report_filepath = Path(__file__).parent / "label_correspondence_report.txt"
    with open(report_filepath, 'w') as f:
        f.write(report)
    print(f"Report written to {report_filepath}")


if __name__ == "__main__":
    main()
