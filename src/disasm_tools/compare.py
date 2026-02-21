"""ROM binary comparison tool using difflib.SequenceMatcher.

Compares two BBC Micro sideways ROM images at three levels of granularity:
byte-level, opcode-only (ignoring operands), and full instruction (opcode +
operands). Produces a human-readable report showing where the ROMs differ.
"""

import hashlib
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

from disasm_tools.mos6502 import OPCODE_LENGTHS, OPCODE_MNEMONICS, ROM_BASE


# ============================================================
# Data structures
# ============================================================


@dataclass
class Instruction:
    """A single 6502 instruction from linear sweep disassembly."""

    offset: int
    opcode: int
    operand_bytes: bytes
    length: int
    is_valid: bool

    @property
    def rom_address(self) -> int:
        return ROM_BASE + self.offset

    @property
    def all_bytes(self) -> bytes:
        return bytes([self.opcode]) + self.operand_bytes

    @property
    def mnemonic(self) -> str:
        if not self.is_valid:
            return "???"
        return OPCODE_MNEMONICS[self.opcode]


@dataclass
class RomHeader:
    """Parsed BBC Micro sideways ROM header."""

    language_entry: int
    service_entry: int
    rom_type: int
    copyright_offset: int
    binary_version: int
    title: str
    version_string: str
    copyright: str


# ============================================================
# ROM header parsing
# ============================================================


def parse_rom_header(data: bytes) -> RomHeader:
    """Parse BBC Micro sideways ROM header fields.

    Header layout (offsets from start of ROM):
      +0: JMP language_entry  (3 bytes: $4C lo hi)
      +3: JMP service_entry   (3 bytes: $4C lo hi)
      +6: ROM type byte
      +7: Copyright offset    (from ROM start to NUL before "(C)")
      +8: Binary version number
      +9: Title string        (NUL-terminated)
      After title NUL: version string (up to copyright offset)
      At copyright offset: NUL, then "(C)..." NUL-terminated
    """
    language_entry = data[1] | (data[2] << 8)
    service_entry = data[4] | (data[5] << 8)
    rom_type = data[6]
    copyright_offset = data[7]
    binary_version = data[8]

    # Title: NUL-terminated string starting at offset 9
    title_end = data.index(0, 9)
    title = data[9:title_end].decode("ascii", errors="replace")

    # Version string: bytes between title NUL and copyright offset
    version_start = title_end + 1
    version_string = data[version_start:copyright_offset].rstrip(b"\x00").decode(
        "ascii", errors="replace"
    )

    # Copyright: NUL + "(C)..." NUL-terminated at copyright offset
    copyright_start = copyright_offset + 1
    copyright_end = data.index(0, copyright_start)
    copyright = data[copyright_start:copyright_end].decode("ascii", errors="replace")

    return RomHeader(
        language_entry=language_entry,
        service_entry=service_entry,
        rom_type=rom_type,
        copyright_offset=copyright_offset,
        binary_version=binary_version,
        title=title,
        version_string=version_string,
        copyright=copyright,
    )


# ============================================================
# Linear sweep disassembly
# ============================================================


def disassemble_linear(data: bytes) -> list[Instruction]:
    """Decompose ROM bytes into instructions using linear sweep.

    Invalid opcodes (length 0 in the table) are emitted as single-byte
    data items. This is a deliberate simplification: both ROMs are swept
    identically, so data tables misinterpreted as instructions will align
    correctly in the SequenceMatcher.
    """
    instructions = []
    offset = 0
    while offset < len(data):
        opcode = data[offset]
        length = OPCODE_LENGTHS[opcode]
        if length == 0:
            instructions.append(
                Instruction(offset, opcode, b"", 1, is_valid=False)
            )
            offset += 1
        elif offset + length > len(data):
            # Truncated at end of ROM
            operand = data[offset + 1 :]
            instructions.append(
                Instruction(offset, opcode, bytes(operand), len(operand) + 1,
                            is_valid=False)
            )
            break
        else:
            operand = data[offset + 1 : offset + length]
            instructions.append(
                Instruction(offset, opcode, bytes(operand), length,
                            is_valid=True)
            )
            offset += length
    return instructions


# ============================================================
# Formatting helpers
# ============================================================


def format_address(offset: int) -> str:
    """Format a ROM offset as a $hex address."""
    return f"${ROM_BASE + offset:04X}"


def format_instruction(inst: Instruction) -> str:
    """Format a single instruction for display.

    Returns e.g. "LDA #$42 (A9 42)" or ".byte $FF (FF)"
    """
    hex_bytes = " ".join(f"{b:02X}" for b in inst.all_bytes)
    if not inst.is_valid:
        return f".byte ${inst.opcode:02X}  ({hex_bytes})"

    mnemonic = inst.mnemonic
    if inst.length == 1:
        return f"{mnemonic}  ({hex_bytes})"
    elif inst.length == 2:
        operand = inst.operand_bytes[0]
        # Branch instructions use relative addressing
        if inst.opcode in (
            0x10, 0x30, 0x50, 0x70, 0x90, 0xB0, 0xD0, 0xF0,
        ):
            # Compute branch target
            signed = operand if operand < 128 else operand - 256
            target = inst.rom_address + 2 + signed
            return f"{mnemonic} ${target:04X}  ({hex_bytes})"
        else:
            return f"{mnemonic} ${operand:02X}  ({hex_bytes})"
    else:
        addr = inst.operand_bytes[0] | (inst.operand_bytes[1] << 8)
        return f"{mnemonic} ${addr:04X}  ({hex_bytes})"


# ============================================================
# Comparison engine
# ============================================================


def compare_headers(
    header_a: RomHeader, header_b: RomHeader, label_a: str, label_b: str
) -> list[str]:
    """Compare two ROM headers, returning report lines."""
    lines = []
    col_a = max(len(label_a), 14)
    col_b = max(len(label_b), 14)

    lines.append(f"  {'Field':<22s} {label_a:<{col_a}s}  {label_b:<{col_b}s}")
    lines.append(f"  {'-' * 22} {'-' * col_a}  {'-' * col_b}")

    fields = [
        ("Language entry", f"${header_a.language_entry:04X}",
         f"${header_b.language_entry:04X}"),
        ("Service entry", f"${header_a.service_entry:04X}",
         f"${header_b.service_entry:04X}"),
        ("ROM type", f"${header_a.rom_type:02X}",
         f"${header_b.rom_type:02X}"),
        ("Copyright offset", f"${header_a.copyright_offset:02X}",
         f"${header_b.copyright_offset:02X}"),
        ("Binary version", f"${header_a.binary_version:02X}",
         f"${header_b.binary_version:02X}"),
        ("Title", f'"{header_a.title}"', f'"{header_b.title}"'),
        ("Version string", f'"{header_a.version_string}"',
         f'"{header_b.version_string}"'),
        ("Copyright", f'"{header_a.copyright}"', f'"{header_b.copyright}"'),
    ]

    for name, val_a, val_b in fields:
        marker = " " if val_a == val_b else "*"
        lines.append(f"{marker} {name:<22s} {val_a:<{col_a}s}  {val_b}")

    return lines


def compare_roms(
    data_a: bytes, data_b: bytes, label_a: str, label_b: str
) -> str:
    """Generate the full comparison report."""
    lines = []

    # ---- Basic stats ----
    sha256_a = hashlib.sha256(data_a).hexdigest()
    sha256_b = hashlib.sha256(data_b).hexdigest()

    byte_matcher = SequenceMatcher(None, data_a, data_b, autojunk=False)
    byte_ratio = byte_matcher.ratio()
    identical_bytes = sum(
        1 for a, b in zip(data_a, data_b) if a == b
    )

    # ---- Instruction decomposition ----
    insts_a = disassemble_linear(data_a)
    insts_b = disassemble_linear(data_b)

    # Opcode-only sequences (structural comparison)
    opcodes_a = [inst.opcode for inst in insts_a]
    opcodes_b = [inst.opcode for inst in insts_b]
    opcode_matcher = SequenceMatcher(None, opcodes_a, opcodes_b, autojunk=False)
    opcode_ratio = opcode_matcher.ratio()

    # Full instruction sequences (opcode + operands)
    inst_bytes_a = [inst.all_bytes for inst in insts_a]
    inst_bytes_b = [inst.all_bytes for inst in insts_b]
    inst_matcher = SequenceMatcher(None, inst_bytes_a, inst_bytes_b, autojunk=False)
    inst_ratio = inst_matcher.ratio()

    # ---- Report header ----
    lines.append("=" * 64)
    lines.append(f"ROM Comparison: NFS {label_a} vs NFS {label_b}")
    lines.append("=" * 64)
    lines.append("")

    # ---- 1. Summary ----
    lines.append("1. SUMMARY")
    lines.append("")
    lines.append(f"  {label_a}: {len(data_a)} bytes  SHA-256: {sha256_a[:16]}...")
    lines.append(f"  {label_b}: {len(data_b)} bytes  SHA-256: {sha256_b[:16]}...")
    lines.append("")
    min_len = min(len(data_a), len(data_b))
    lines.append(
        f"  Identical bytes at same offset: {identical_bytes}/{min_len} "
        f"({100 * identical_bytes / min_len:.1f}%)"
    )
    lines.append(f"  Byte-level similarity:         {byte_ratio:.1%} (SequenceMatcher)")
    lines.append(f"  Opcode-level similarity:       {opcode_ratio:.1%} (structure only)")
    lines.append(
        f"  Full instruction similarity:   {inst_ratio:.1%} (opcode + operands)"
    )
    lines.append(f"  Instructions: {len(insts_a)} ({label_a}) / {len(insts_b)} ({label_b})")
    lines.append("")

    # ---- 2. ROM header ----
    lines.append("2. ROM HEADER")
    lines.append("")
    try:
        header_a = parse_rom_header(data_a)
        header_b = parse_rom_header(data_b)
        lines.extend(compare_headers(header_a, header_b, label_a, label_b))
    except Exception as e:
        lines.append(f"  Error parsing headers: {e}")
    lines.append("")

    # ---- 3. Structural changes (opcode-only) ----
    lines.append("3. STRUCTURAL CHANGES (opcode-level)")
    lines.append("")

    opcode_ops = opcode_matcher.get_opcodes()
    n_equal = sum(1 for tag, *_ in opcode_ops if tag == "equal")
    n_replace = sum(1 for tag, *_ in opcode_ops if tag == "replace")
    n_delete = sum(1 for tag, *_ in opcode_ops if tag == "delete")
    n_insert = sum(1 for tag, *_ in opcode_ops if tag == "insert")
    n_changes = n_replace + n_delete + n_insert

    lines.append(
        f"  {n_changes} change blocks "
        f"({n_replace} replaced, {n_delete} deleted, {n_insert} inserted), "
        f"{n_equal} equal regions"
    )
    lines.append("")

    for tag, i1, i2, j1, j2 in opcode_ops:
        if tag == "equal":
            a_start = format_address(insts_a[i1].offset)
            a_end = format_address(insts_a[i2 - 1].offset)
            b_start = format_address(insts_b[j1].offset)
            b_end = format_address(insts_b[j2 - 1].offset)
            count = i2 - i1
            lines.append(
                f"  == {a_start}-{a_end} / {b_start}-{b_end}: "
                f"{count} instructions match"
            )
        elif tag == "replace":
            lines.append(
                f"  ~~ REPLACE {i2 - i1} -> {j2 - j1} instructions:"
            )
            for k in range(i1, i2):
                inst = insts_a[k]
                lines.append(
                    f"     {label_a} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )
            for k in range(j1, j2):
                inst = insts_b[k]
                lines.append(
                    f"     {label_b} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )
        elif tag == "delete":
            lines.append(f"  -- DELETE {i2 - i1} instructions from {label_a}:")
            for k in range(i1, i2):
                inst = insts_a[k]
                lines.append(
                    f"     {label_a} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )
        elif tag == "insert":
            lines.append(f"  ++ INSERT {j2 - j1} instructions in {label_b}:")
            for k in range(j1, j2):
                inst = insts_b[k]
                lines.append(
                    f"     {label_b} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )

    lines.append("")

    # ---- 4. Full instruction diff map ----
    lines.append("4. INSTRUCTION DIFF MAP (opcode + operands)")
    lines.append("")

    inst_ops = inst_matcher.get_opcodes()
    for tag, i1, i2, j1, j2 in inst_ops:
        if tag == "equal":
            a_start = format_address(insts_a[i1].offset)
            a_end = format_address(insts_a[i2 - 1].offset)
            b_start = format_address(insts_b[j1].offset)
            b_end = format_address(insts_b[j2 - 1].offset)
            count = i2 - i1
            byte_count_a = sum(insts_a[k].length for k in range(i1, i2))
            lines.append(
                f"  == {a_start}-{a_end} / {b_start}-{b_end}: "
                f"{count} instructions ({byte_count_a} bytes)"
            )
        elif tag == "replace":
            lines.append(
                f"  ~~ REPLACE {i2 - i1} -> {j2 - j1} instructions:"
            )
            for k in range(i1, i2):
                inst = insts_a[k]
                lines.append(
                    f"     {label_a} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )
            for k in range(j1, j2):
                inst = insts_b[k]
                lines.append(
                    f"     {label_b} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )
        elif tag == "delete":
            lines.append(f"  -- DELETE {i2 - i1} instructions from {label_a}:")
            for k in range(i1, i2):
                inst = insts_a[k]
                lines.append(
                    f"     {label_a} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )
        elif tag == "insert":
            lines.append(f"  ++ INSERT {j2 - j1} instructions in {label_b}:")
            for k in range(j1, j2):
                inst = insts_b[k]
                lines.append(
                    f"     {label_b} {format_address(inst.offset)}: "
                    f"{format_instruction(inst)}"
                )

    return "\n".join(lines)


# ============================================================
# Entry point
# ============================================================


def compare(version_dirpath_a, version_a, version_dirpath_b, version_b):
    """Compare two ROM versions and print the report.

    Returns 0 on success, 1 on error.
    """
    rom_filepath_a = version_dirpath_a / "rom" / f"nfs-{version_a}.rom"
    rom_filepath_b = version_dirpath_b / "rom" / f"nfs-{version_b}.rom"

    for filepath in (rom_filepath_a, rom_filepath_b):
        if not filepath.exists():
            print(f"Error: ROM file not found: {filepath}", file=sys.stderr)
            return 1

    data_a = rom_filepath_a.read_bytes()
    data_b = rom_filepath_b.read_bytes()

    report = compare_roms(data_a, data_b, version_a, version_b)
    print(report)
    return 0
