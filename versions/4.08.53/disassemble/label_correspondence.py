#!/usr/bin/env python3
"""Build an opcode-level address map from NFS 3.65 to ANFS 4.08.53.

Uses difflib.SequenceMatcher on opcode sequences extracted from both ROMs
to identify matching code regions. Reads all label(), subroutine(),
comment(), and constant() annotations from the NFS 3.65 driver script
and maps them to ANFS addresses. Handles both the main ROM body and
the relocated code blocks (pages 4-6 and zero page) separately.

Output:
  - Comprehensive report to stdout
  - JSON address map to versions/4.08.53/disassemble/label_map.json
"""

import difflib
import json
import re
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

_script_dirpath = Path(__file__).resolve().parent
_project_dirpath = _script_dirpath.parent.parent.parent

NFS_ROM_FILEPATH = _project_dirpath / "versions" / "3.65" / "rom" / "nfs-3.65.rom"
ANFS_ROM_FILEPATH = _project_dirpath / "versions" / "4.08.53" / "rom" / "anfs-4.08.53.rom"

NFS_DRIVER_FILEPATH = _project_dirpath / "versions" / "3.65" / "disassemble" / "disasm_nfs_365.py"

JSON_OUTPUT_FILEPATH = _script_dirpath / "label_map.json"

ROM_BASE = 0x8000

NFS_ROM_SIZE = 8192     # 8K: &8000-&9FFF
ANFS_ROM_SIZE = 16384   # 16K: &8000-&BFFF

# NFS 3.65 relocated block sources (ROM offsets = address - &8000)
NFS_RELOC = {
    "zp": {"rom_offset": 0x1324, "runtime": 0x0016, "length": 0x61},    # 97 bytes
    "p4": {"rom_offset": 0x1365, "runtime": 0x0400, "length": 0x100},   # 256 bytes
    "p5": {"rom_offset": 0x1465, "runtime": 0x0500, "length": 0x100},   # 256 bytes
    "p6": {"rom_offset": 0x1565, "runtime": 0x0600, "length": 0x100},   # 256 bytes
}

# ANFS 4.08.53 relocated block sources (ROM offsets = address - &8000)
ANFS_RELOC = {
    "p4": {"rom_offset": 0x3F00, "runtime": 0x0400, "length": 0x100},   # 256 bytes
    "p5": {"rom_offset": 0x3C90, "runtime": 0x0500, "length": 0x100},   # 256 bytes
    "p6": {"rom_offset": 0x3D90, "runtime": 0x0600, "length": 0x100},   # 256 bytes
    "zp": {"rom_offset": 0x3EBF, "runtime": 0x0016, "length": 0x42},    # 66 bytes
}

# ============================================================
# 6502 Opcode Length Table (256 entries)
# ============================================================
# 0 = invalid/undefined, 1 = implied/accumulator, 2 = immediate/zp/rel, 3 = absolute
OPCODE_LENGTHS = [
    # $00-$0F
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 0, 3, 3, 0,
    # $10-$1F
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    # $20-$2F
    3, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    # $30-$3F
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    # $40-$4F
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    # $50-$5F
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    # $60-$6F
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    # $70-$7F
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    # $80-$8F
    0, 2, 0, 0, 2, 2, 2, 0, 1, 0, 1, 0, 3, 3, 3, 0,
    # $90-$9F
    2, 2, 0, 0, 2, 2, 2, 0, 1, 3, 1, 0, 0, 3, 0, 0,
    # $A0-$AF
    2, 2, 2, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    # $B0-$BF
    2, 2, 0, 0, 2, 2, 2, 0, 1, 3, 1, 0, 3, 3, 3, 0,
    # $C0-$CF
    2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    # $D0-$DF
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    # $E0-$EF
    2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    # $F0-$FF
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
]


# ============================================================
# ROM loading
# ============================================================

def load_rom(filepath):
    """Load a ROM binary file."""
    with open(filepath, "rb") as f:
        return f.read()


# ============================================================
# Opcode extraction
# ============================================================

def extract_opcodes(rom_data, start_offset, length):
    """Extract an opcode sequence from ROM data, walking instruction boundaries.

    Returns a list of (offset_within_region, opcode_byte) tuples.
    """
    opcodes = []
    pos = 0
    while pos < length:
        abs_pos = start_offset + pos
        if abs_pos >= len(rom_data):
            break
        opcode = rom_data[abs_pos]
        opcodes.append((pos, opcode))
        inst_len = OPCODE_LENGTHS[opcode]
        if inst_len == 0:
            # Invalid opcode, treat as 1-byte data
            pos += 1
        else:
            pos += inst_len
    return opcodes


def extract_opcode_sequence(rom_data, start_offset, length):
    """Extract just the opcode bytes (no position info) for SequenceMatcher."""
    return [op for _, op in extract_opcodes(rom_data, start_offset, length)]


# ============================================================
# Address mapping via SequenceMatcher
# ============================================================

def build_address_map_for_region(nfs_data, nfs_start, nfs_length,
                                 anfs_data, anfs_start, anfs_length,
                                 nfs_runtime_base, anfs_runtime_base):
    """Build a runtime-address to runtime-address map for one region.

    Uses difflib.SequenceMatcher on opcode sequences to find matching
    blocks, then expands each matched opcode into a full instruction-level
    address mapping.

    Returns:
        address_map: dict mapping NFS runtime addr -> ANFS runtime addr
        stats: dict with match statistics
    """
    nfs_opcodes = extract_opcodes(nfs_data, nfs_start, nfs_length)
    anfs_opcodes = extract_opcodes(anfs_data, anfs_start, anfs_length)

    nfs_seq = [op for _, op in nfs_opcodes]
    anfs_seq = [op for _, op in anfs_opcodes]

    matcher = difflib.SequenceMatcher(None, nfs_seq, anfs_seq, autojunk=False)
    matching_blocks = matcher.get_matching_blocks()

    address_map = {}
    total_matched_opcodes = 0

    for nfs_idx, anfs_idx, size in matching_blocks:
        if size == 0:
            continue
        total_matched_opcodes += size

        for k in range(size):
            nfs_region_offset, nfs_opcode = nfs_opcodes[nfs_idx + k]
            anfs_region_offset, anfs_opcode = anfs_opcodes[anfs_idx + k]

            nfs_runtime = nfs_runtime_base + nfs_region_offset
            anfs_runtime = anfs_runtime_base + anfs_region_offset

            # Map the opcode address
            address_map[nfs_runtime] = anfs_runtime

            # Also map operand bytes within this instruction
            inst_len = OPCODE_LENGTHS[nfs_opcode]
            if inst_len == 0:
                inst_len = 1
            anfs_inst_len = OPCODE_LENGTHS[anfs_opcode]
            if anfs_inst_len == 0:
                anfs_inst_len = 1

            # Only map operand bytes if instruction lengths agree
            if inst_len == anfs_inst_len:
                for b in range(1, inst_len):
                    nfs_byte_addr = nfs_runtime + b
                    anfs_byte_addr = anfs_runtime + b
                    address_map[nfs_byte_addr] = anfs_byte_addr

    stats = {
        "nfs_opcodes": len(nfs_opcodes),
        "anfs_opcodes": len(anfs_opcodes),
        "matched_opcodes": total_matched_opcodes,
        "match_pct": (total_matched_opcodes / len(nfs_opcodes) * 100)
            if nfs_opcodes else 0.0,
        "matching_blocks": len([b for b in matching_blocks if b[2] > 0]),
    }

    return address_map, stats


# ============================================================
# Parse NFS 3.65 driver script annotations
# ============================================================

def parse_driver_annotations(filepath):
    """Parse label(), subroutine(), comment(), and constant() calls.

    Returns a dict with keys "label", "subroutine", "comment", "constant",
    each mapping to a list of dicts with at least an "address" field.
    """
    with open(filepath, "r") as f:
        source = f.read()
    lines = source.split("\n")

    annotations = {
        "label": [],
        "subroutine": [],
        "comment": [],
        "constant": [],
    }

    # label(0xADDR, "name")
    label_re = re.compile(
        r'^label\(\s*(0x[0-9A-Fa-f]+)\s*,\s*"([^"]+)"\s*\)')
    # subroutine(0xADDR, ...) — may span multiple lines
    sub_re = re.compile(
        r'^subroutine\(\s*(0x[0-9A-Fa-f]+)\s*,')
    # comment(0xADDR, "text", ...)
    comment_re = re.compile(
        r'^comment\(\s*(0x[0-9A-Fa-f]+)\s*,\s*"')
    # constant(0xADDR, "name") or constant(VALUE, "name")
    constant_re = re.compile(
        r'^constant\(\s*(0x[0-9A-Fa-f]+|[0-9]+)\s*,\s*"([^"]+)"\s*\)')
    # hook_subroutine(0xADDR, "name", hook)
    hook_sub_re = re.compile(
        r'^hook_subroutine\(\s*(0x[0-9A-Fa-f]+)\s*,\s*"([^"]+)"\s*,')
    # entry(0xADDR)
    entry_re = re.compile(
        r'^entry\(\s*(0x[0-9A-Fa-f]+)\s*\)')

    # Extract subroutine title from multi-line call
    sub_title_re = re.compile(r'title\s*=\s*"([^"]*)"')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        m = label_re.match(line)
        if m:
            addr = int(m.group(1), 16)
            name = m.group(2)
            annotations["label"].append({
                "address": addr, "name": name,
            })
            i += 1
            continue

        m = sub_re.match(line)
        if m:
            addr = int(m.group(1), 16)
            # Collect full subroutine call (may span lines)
            full_call = line
            paren_depth = line.count("(") - line.count(")")
            j = i + 1
            while paren_depth > 0 and j < len(lines):
                full_call += "\n" + lines[j]
                paren_depth += lines[j].count("(") - lines[j].count(")")
                j += 1
            title_m = sub_title_re.search(full_call)
            title = title_m.group(1) if title_m else ""
            annotations["subroutine"].append({
                "address": addr, "title": title,
            })
            i = j
            continue

        m = comment_re.match(line)
        if m:
            addr = int(m.group(1), 16)
            annotations["comment"].append({"address": addr})
            i += 1
            continue

        m = constant_re.match(line)
        if m:
            val_str = m.group(1)
            if val_str.startswith("0x"):
                addr = int(val_str, 16)
            else:
                addr = int(val_str)
            name = m.group(2)
            annotations["constant"].append({
                "address": addr, "name": name,
            })
            i += 1
            continue

        m = hook_sub_re.match(line)
        if m:
            addr = int(m.group(1), 16)
            name = m.group(2)
            annotations["label"].append({
                "address": addr, "name": name,
                "source": "hook_subroutine",
            })
            i += 1
            continue

        m = entry_re.match(line)
        if m:
            addr = int(m.group(1), 16)
            annotations["label"].append({
                "address": addr, "name": None,
                "source": "entry",
            })
            i += 1
            continue

        i += 1

    return annotations


# ============================================================
# Classify address into region
# ============================================================

def classify_nfs_address(addr):
    """Determine which region an NFS 3.65 address belongs to.

    Returns one of: "main_rom", "zp", "p4", "p5", "p6", or None.
    """
    # Relocated block runtime ranges
    for block_name, block in NFS_RELOC.items():
        runtime = block["runtime"]
        length = block["length"]
        if runtime <= addr < runtime + length:
            return block_name

    # Main ROM: &8000-&9FFF, excluding relocated block source areas
    if ROM_BASE <= addr < ROM_BASE + NFS_ROM_SIZE:
        return "main_rom"

    return None


# ============================================================
# Report generation
# ============================================================

def generate_report(address_maps, region_stats, annotations, all_mapped,
                    all_unmapped):
    """Generate a comprehensive text report."""
    lines = []

    lines.append("=" * 90)
    lines.append("Label Correspondence Report: NFS 3.65 (8K) -> ANFS 4.08.53 (16K)")
    lines.append("=" * 90)

    # Overall match statistics
    lines.append("")
    lines.append("OPCODE MATCH STATISTICS BY REGION")
    lines.append("-" * 60)

    total_nfs = 0
    total_matched = 0

    for region_name, stats in region_stats.items():
        nfs_count = stats["nfs_opcodes"]
        anfs_count = stats["anfs_opcodes"]
        matched = stats["matched_opcodes"]
        pct = stats["match_pct"]
        blocks = stats["matching_blocks"]
        total_nfs += nfs_count
        total_matched += matched
        lines.append(
            f"  {region_name:12s}: {matched:4d}/{nfs_count:4d} NFS opcodes matched "
            f"({pct:5.1f}%), {blocks} contiguous blocks"
        )
        lines.append(
            f"  {'':12s}  ANFS region has {anfs_count} opcodes"
        )

    overall_pct = (total_matched / total_nfs * 100) if total_nfs else 0.0
    lines.append(f"  {'TOTAL':12s}: {total_matched:4d}/{total_nfs:4d} "
                 f"({overall_pct:5.1f}%)")

    # Annotation mapping summary
    lines.append("")
    lines.append("ANNOTATION MAPPING SUMMARY")
    lines.append("-" * 60)
    for ann_type in ("label", "subroutine", "comment", "constant"):
        mapped_count = sum(
            1 for item in all_mapped if item["type"] == ann_type
        )
        unmapped_count = sum(
            1 for item in all_unmapped if item["type"] == ann_type
        )
        total = mapped_count + unmapped_count
        pct = (mapped_count / total * 100) if total else 0.0
        lines.append(
            f"  {ann_type:14s}: {mapped_count:4d} mapped, "
            f"{unmapped_count:4d} unmapped, {total:4d} total ({pct:5.1f}%)"
        )

    total_mapped_count = len(all_mapped)
    total_unmapped_count = len(all_unmapped)
    total_all = total_mapped_count + total_unmapped_count
    total_pct = (total_mapped_count / total_all * 100) if total_all else 0.0
    lines.append(
        f"  {'ALL':14s}: {total_mapped_count:4d} mapped, "
        f"{total_unmapped_count:4d} unmapped, {total_all:4d} total ({total_pct:5.1f}%)"
    )

    # Mapped labels and subroutines
    lines.append("")
    lines.append("=" * 90)
    lines.append("MAPPED LABELS (label + hook_subroutine)")
    lines.append("=" * 90)
    lines.append(f"{'NFS Addr':>10s}  {'ANFS Addr':>10s}  {'Shift':>7s}  {'Region':8s}  Name")
    lines.append(f"{'--------':>10s}  {'---------':>10s}  {'-----':>7s}  {'------':8s}  ----")

    mapped_labels = sorted(
        [item for item in all_mapped if item["type"] == "label"],
        key=lambda x: x["nfs_address"],
    )
    for item in mapped_labels:
        nfs_addr = item["nfs_address"]
        anfs_addr = item["anfs_address"]
        shift = anfs_addr - nfs_addr
        region = item.get("region") or "?"
        name = item.get("name", "")
        if name is None:
            name = "(entry)"
        lines.append(
            f"  &{nfs_addr:04X}       &{anfs_addr:04X}      {shift:+5d}   "
            f"{region:8s}  {name}"
        )

    lines.append("")
    lines.append("=" * 90)
    lines.append("MAPPED SUBROUTINES")
    lines.append("=" * 90)
    lines.append(f"{'NFS Addr':>10s}  {'ANFS Addr':>10s}  {'Shift':>7s}  Title")
    lines.append(f"{'--------':>10s}  {'---------':>10s}  {'-----':>7s}  -----")

    mapped_subs = sorted(
        [item for item in all_mapped if item["type"] == "subroutine"],
        key=lambda x: x["nfs_address"],
    )
    for item in mapped_subs:
        nfs_addr = item["nfs_address"]
        anfs_addr = item["anfs_address"]
        shift = anfs_addr - nfs_addr
        title = item.get("title", "")
        lines.append(
            f"  &{nfs_addr:04X}       &{anfs_addr:04X}      {shift:+5d}   {title}"
        )

    # Unmapped items
    lines.append("")
    lines.append("=" * 90)
    lines.append("UNMAPPED LABELS")
    lines.append("=" * 90)

    unmapped_labels = sorted(
        [item for item in all_unmapped if item["type"] == "label"],
        key=lambda x: x["nfs_address"],
    )
    for item in unmapped_labels:
        nfs_addr = item["nfs_address"]
        region = item.get("region") or "?"
        name = item.get("name", "")
        if name is None:
            name = "(entry)"
        lines.append(f"  &{nfs_addr:04X}  {region:8s}  {name}")

    lines.append("")
    lines.append("=" * 90)
    lines.append("UNMAPPED SUBROUTINES")
    lines.append("=" * 90)

    unmapped_subs = sorted(
        [item for item in all_unmapped if item["type"] == "subroutine"],
        key=lambda x: x["nfs_address"],
    )
    for item in unmapped_subs:
        nfs_addr = item["nfs_address"]
        title = item.get("title", "")
        lines.append(f"  &{nfs_addr:04X}  {title}")

    # Comment mapping summary (don't list all 3800+ individually)
    lines.append("")
    lines.append("=" * 90)
    lines.append("COMMENT MAPPING (summary only — see JSON for full data)")
    lines.append("=" * 90)

    mapped_comments = sorted(
        [item for item in all_mapped if item["type"] == "comment"],
        key=lambda x: x["nfs_address"],
    )
    unmapped_comments = sorted(
        [item for item in all_unmapped if item["type"] == "comment"],
        key=lambda x: x["nfs_address"],
    )

    if mapped_comments:
        lines.append(f"  Mapped: {len(mapped_comments)} comments "
                     f"(&{mapped_comments[0]['nfs_address']:04X} - "
                     f"&{mapped_comments[-1]['nfs_address']:04X})")
    if unmapped_comments:
        lines.append(f"  Unmapped: {len(unmapped_comments)} comments "
                     f"(&{unmapped_comments[0]['nfs_address']:04X} - "
                     f"&{unmapped_comments[-1]['nfs_address']:04X})")

    lines.append("")
    lines.append("=" * 90)
    lines.append("END OF REPORT")
    lines.append("=" * 90)

    return "\n".join(lines)


# ============================================================
# Main
# ============================================================

def main():
    print("Label Correspondence: NFS 3.65 (8K) -> ANFS 4.08.53 (16K)")
    print()

    # Phase 1: Load ROMs
    print("Phase 1: Loading ROMs...")
    nfs_data = load_rom(NFS_ROM_FILEPATH)
    anfs_data = load_rom(ANFS_ROM_FILEPATH)
    print(f"  NFS 3.65:     {len(nfs_data)} bytes")
    print(f"  ANFS 4.08.53: {len(anfs_data)} bytes")

    # Phase 2: Build address maps for each region
    print("\nPhase 2: Building opcode-level address maps...")

    address_maps = {}
    region_stats = {}

    # Main ROM body
    # NFS main ROM: &8000-&9FFF (full 8K, SequenceMatcher will handle
    # the relocated block source regions as part of the ROM image)
    # ANFS: &8000-&BFFF (full 16K)
    main_map, main_stats = build_address_map_for_region(
        nfs_data, 0, NFS_ROM_SIZE,
        anfs_data, 0, ANFS_ROM_SIZE,
        ROM_BASE, ROM_BASE,
    )
    address_maps["main_rom"] = main_map
    region_stats["main_rom"] = main_stats
    print(f"  Main ROM: {main_stats['matched_opcodes']}/{main_stats['nfs_opcodes']} "
          f"NFS opcodes matched ({main_stats['match_pct']:.1f}%), "
          f"{main_stats['matching_blocks']} contiguous blocks")

    # Relocated blocks: match NFS relocated source against ANFS relocated source
    # using their runtime addresses, since the code runs at the same runtime
    # addresses in both ROMs.
    for block_name in ("zp", "p4", "p5", "p6"):
        nfs_block = NFS_RELOC[block_name]
        anfs_block = ANFS_RELOC[block_name]

        block_map, block_stats = build_address_map_for_region(
            nfs_data, nfs_block["rom_offset"], nfs_block["length"],
            anfs_data, anfs_block["rom_offset"], anfs_block["length"],
            nfs_block["runtime"], anfs_block["runtime"],
        )
        address_maps[block_name] = block_map
        region_stats[block_name] = block_stats
        print(f"  {block_name:3s} block: {block_stats['matched_opcodes']}/{block_stats['nfs_opcodes']} "
              f"NFS opcodes matched ({block_stats['match_pct']:.1f}%), "
              f"{block_stats['matching_blocks']} contiguous blocks")

    # Build combined address map (all regions)
    combined_map = {}
    for region_map in address_maps.values():
        combined_map.update(region_map)

    print(f"\n  Combined: {len(combined_map)} addresses mapped")

    # Phase 3: Parse NFS 3.65 driver annotations
    print("\nPhase 3: Parsing NFS 3.65 driver annotations...")
    annotations = parse_driver_annotations(NFS_DRIVER_FILEPATH)
    for ann_type, items in annotations.items():
        print(f"  {ann_type}: {len(items)} entries")

    # Phase 4: Map annotations through address map
    print("\nPhase 4: Mapping annotations to ANFS addresses...")

    all_mapped = []
    all_unmapped = []

    for ann_type, items in annotations.items():
        for item in items:
            addr = item["address"]
            region = classify_nfs_address(addr)

            entry = {
                "type": ann_type,
                "nfs_address": addr,
                "region": region,
            }

            # Copy annotation-specific fields
            if "name" in item:
                entry["name"] = item["name"]
            if "title" in item:
                entry["title"] = item["title"]
            if "source" in item:
                entry["source"] = item["source"]

            if addr in combined_map:
                entry["anfs_address"] = combined_map[addr]
                all_mapped.append(entry)
            else:
                all_unmapped.append(entry)

    mapped_count = len(all_mapped)
    unmapped_count = len(all_unmapped)
    total = mapped_count + unmapped_count
    pct = (mapped_count / total * 100) if total else 0.0
    print(f"  {mapped_count} mapped, {unmapped_count} unmapped "
          f"({pct:.1f}% mapped)")

    # Phase 5: Generate report
    print("\nPhase 5: Generating report...")
    report = generate_report(
        address_maps, region_stats, annotations, all_mapped, all_unmapped,
    )
    print()
    print(report)

    # Phase 6: Write JSON output
    print(f"\nPhase 6: Writing JSON to {JSON_OUTPUT_FILEPATH}...")

    json_output = {
        "source_rom": "NFS 3.65",
        "target_rom": "ANFS 4.08.53",
        "source_rom_filepath": str(NFS_ROM_FILEPATH),
        "target_rom_filepath": str(ANFS_ROM_FILEPATH),
        "region_stats": region_stats,
        "address_map": {
            f"0x{k:04X}": f"0x{v:04X}"
            for k, v in sorted(combined_map.items())
        },
        "mapped_annotations": sorted(all_mapped, key=lambda x: x["nfs_address"]),
        "unmapped_annotations": sorted(all_unmapped, key=lambda x: x["nfs_address"]),
    }

    with open(JSON_OUTPUT_FILEPATH, "w") as f:
        json.dump(json_output, f, indent=2)

    print(f"  Written {len(combined_map)} address mappings")
    print(f"  Written {len(all_mapped)} mapped annotations")
    print(f"  Written {len(all_unmapped)} unmapped annotations")
    print("\nDone.")


if __name__ == "__main__":
    main()
