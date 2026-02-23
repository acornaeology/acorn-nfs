#!/usr/bin/env python3
"""Find correct addresses for comment() calls carried over from another version.

Originally written to fix 17 stale 3.34B comment addresses in the 3.35D driver
script. Adaptable for future version ports by changing the stale_comments list
and the source/target ROM paths.

For each stale address, extracts the instruction at that address from the source
ROM, builds an opcode fingerprint of 4-6 surrounding instructions, and searches
the target ROM for matching byte patterns. Cross-checks proposed addresses
against instruction boundaries in the target assembly output.
"""

import re
import subprocess
import sys
from pathlib import Path


# 6502 opcode length table: maps opcode byte to instruction length (1, 2, or 3).
# Undocumented/illegal opcodes default to 1.
OPCODE_LENGTHS = {
    # BRK, ORA (indirect,X)
    0x00: 1, 0x01: 2,
    # ORA zp, ASL zp
    0x05: 2, 0x06: 2,
    # PHP, ORA #imm, ASL A
    0x08: 1, 0x09: 2, 0x0A: 1,
    # ORA abs, ASL abs
    0x0D: 3, 0x0E: 3,
    # BPL rel
    0x10: 2, 0x11: 2,
    # ORA zp,X, ASL zp,X
    0x15: 2, 0x16: 2,
    # CLC
    0x18: 1, 0x19: 3,
    # ORA abs,X, ASL abs,X
    0x1D: 3, 0x1E: 3,
    # JSR abs
    0x20: 3, 0x21: 2,
    # BIT zp, AND zp, ROL zp
    0x24: 2, 0x25: 2, 0x26: 2,
    # PLP, AND #imm, ROL A
    0x28: 1, 0x29: 2, 0x2A: 1,
    # BIT abs, AND abs, ROL abs
    0x2C: 3, 0x2D: 3, 0x2E: 3,
    # BMI rel
    0x30: 2, 0x31: 2,
    # AND zp,X, ROL zp,X
    0x35: 2, 0x36: 2,
    # SEC
    0x38: 1, 0x39: 3,
    # AND abs,X, ROL abs,X
    0x3D: 3, 0x3E: 3,
    # RTI
    0x40: 1, 0x41: 2,
    # EOR zp, LSR zp
    0x45: 2, 0x46: 2,
    # PHA, EOR #imm, LSR A
    0x48: 1, 0x49: 2, 0x4A: 1,
    # JMP abs, EOR abs, LSR abs
    0x4C: 3, 0x4D: 3, 0x4E: 3,
    # BVC rel
    0x50: 2, 0x51: 2,
    # EOR zp,X, LSR zp,X
    0x55: 2, 0x56: 2,
    # CLI
    0x58: 1, 0x59: 3,
    # EOR abs,X, LSR abs,X
    0x5D: 3, 0x5E: 3,
    # RTS
    0x60: 1, 0x61: 2,
    # ADC zp, ROR zp
    0x65: 2, 0x66: 2,
    # PLA, ADC #imm, ROR A
    0x68: 1, 0x69: 2, 0x6A: 1,
    # JMP (indirect), ADC abs, ROR abs
    0x6C: 3, 0x6D: 3, 0x6E: 3,
    # BVS rel
    0x70: 2, 0x71: 2,
    # ADC zp,X, ROR zp,X
    0x75: 2, 0x76: 2,
    # SEI
    0x78: 1, 0x79: 3,
    # ADC abs,X, ROR abs,X
    0x7D: 3, 0x7E: 3,
    # STA (indirect,X)
    0x81: 2,
    # STY zp, STA zp, STX zp
    0x84: 2, 0x85: 2, 0x86: 2,
    # DEY, TXA
    0x88: 1, 0x8A: 1,
    # STY abs, STA abs, STX abs
    0x8C: 3, 0x8D: 3, 0x8E: 3,
    # BCC rel
    0x90: 2, 0x91: 2,
    # STY zp,X, STA zp,X, STX zp,Y
    0x94: 2, 0x95: 2, 0x96: 2,
    # TYA
    0x98: 1, 0x99: 3, 0x9A: 1,
    # STA abs,X
    0x9D: 3,
    # LDY #imm, LDA (indirect,X)
    0xA0: 2, 0xA1: 2, 0xA2: 2,
    # LDY zp, LDA zp, LDX zp
    0xA4: 2, 0xA5: 2, 0xA6: 2,
    # TAY, LDA #imm, TAX
    0xA8: 1, 0xA9: 2, 0xAA: 1,
    # LDY abs, LDA abs, LDX abs
    0xAC: 3, 0xAD: 3, 0xAE: 3,
    # BCS rel
    0xB0: 2, 0xB1: 2,
    # LDY zp,X, LDA zp,X, LDX zp,Y
    0xB4: 2, 0xB5: 2, 0xB6: 2,
    # CLV
    0xB8: 1, 0xB9: 3, 0xBA: 1,
    # LDY abs,X, LDA abs,X, LDX abs,Y
    0xBC: 3, 0xBD: 3, 0xBE: 3,
    # CPY #imm, CMP (indirect,X)
    0xC0: 2, 0xC1: 2,
    # CPY zp, CMP zp, DEC zp
    0xC4: 2, 0xC5: 2, 0xC6: 2,
    # INY, CMP #imm, DEX
    0xC8: 1, 0xC9: 2, 0xCA: 1,
    # CPY abs, CMP abs, DEC abs
    0xCC: 3, 0xCD: 3, 0xCE: 3,
    # BNE rel
    0xD0: 2, 0xD1: 2,
    # CMP zp,X, DEC zp,X
    0xD5: 2, 0xD6: 2,
    # CLD
    0xD8: 1, 0xD9: 3,
    # CMP abs,X, DEC abs,X
    0xDD: 3, 0xDE: 3,
    # CPX #imm, SBC (indirect,X)
    0xE0: 2, 0xE1: 2,
    # CPX zp, SBC zp, INC zp
    0xE4: 2, 0xE5: 2, 0xE6: 2,
    # INX, SBC #imm, NOP
    0xE8: 1, 0xE9: 2, 0xEA: 1,
    # CPX abs, SBC abs, INC abs
    0xEC: 3, 0xED: 3, 0xEE: 3,
    # BEQ rel
    0xF0: 2, 0xF1: 2,
    # SBC zp,X, INC zp,X
    0xF5: 2, 0xF6: 2,
    # SED
    0xF8: 1, 0xF9: 3,
    # SBC abs,X, INC abs,X
    0xFD: 3, 0xFE: 3,
}


ROM_BASE = 0x8000
ROM_SIZE = 8192


def get_opcode_length(opcode: int) -> int:
    """Return the byte length of a 6502 instruction given its opcode."""
    return OPCODE_LENGTHS.get(opcode, 1)


def get_instruction_bytes(rom: bytes, addr: int) -> bytes:
    """Extract the full instruction (opcode + operands) at a ROM address."""
    offset = addr - ROM_BASE
    if offset < 0 or offset >= len(rom):
        return b""
    opcode = rom[offset]
    length = get_opcode_length(opcode)
    end = min(offset + length, len(rom))
    return rom[offset:end]


def get_opcode_fingerprint(rom: bytes, addr: int, count: int = 5) -> list[int]:
    """Extract a sequence of opcodes (ignoring operands) starting at addr.

    Returns a list of `count` opcodes. Stops early if we run past ROM end.
    """
    opcodes = []
    offset = addr - ROM_BASE
    for _ in range(count):
        if offset < 0 or offset >= len(rom):
            break
        opcode = rom[offset]
        opcodes.append(opcode)
        length = get_opcode_length(opcode)
        offset += length
    return opcodes


def get_instruction_sequence(rom: bytes, addr: int, count: int = 5) -> list[bytes]:
    """Extract a sequence of full instructions (opcode + operands) starting at addr."""
    instructions = []
    offset = addr - ROM_BASE
    for _ in range(count):
        if offset < 0 or offset >= len(rom):
            break
        opcode = rom[offset]
        length = get_opcode_length(opcode)
        end = min(offset + length, len(rom))
        instructions.append(rom[offset:end])
        offset += length
    return instructions


def format_bytes(data: bytes) -> str:
    """Format bytes as hex string like '20 D4 80'."""
    return " ".join(f"{b:02X}" for b in data)


def disassemble_instruction(rom: bytes, addr: int) -> str:
    """Return a basic disassembly of the instruction at addr."""
    offset = addr - ROM_BASE
    if offset < 0 or offset >= len(rom):
        return "???"
    opcode = rom[offset]
    length = get_opcode_length(opcode)

    # Simple mnemonic table for common opcodes (just enough for display)
    MNEMONICS = {
        0x00: "BRK", 0x01: "ORA", 0x05: "ORA", 0x06: "ASL", 0x08: "PHP",
        0x09: "ORA", 0x0A: "ASL", 0x0D: "ORA", 0x0E: "ASL", 0x10: "BPL",
        0x11: "ORA", 0x15: "ORA", 0x16: "ASL", 0x18: "CLC", 0x19: "ORA",
        0x1D: "ORA", 0x1E: "ASL", 0x20: "JSR", 0x21: "AND", 0x24: "BIT",
        0x25: "AND", 0x26: "ROL", 0x28: "PLP", 0x29: "AND", 0x2A: "ROL",
        0x2C: "BIT", 0x2D: "AND", 0x2E: "ROL", 0x30: "BMI", 0x31: "AND",
        0x35: "AND", 0x36: "ROL", 0x38: "SEC", 0x39: "AND", 0x3D: "AND",
        0x3E: "ROL", 0x40: "RTI", 0x41: "EOR", 0x45: "EOR", 0x46: "LSR",
        0x48: "PHA", 0x49: "EOR", 0x4A: "LSR", 0x4C: "JMP", 0x4D: "EOR",
        0x4E: "LSR", 0x50: "BVC", 0x51: "EOR", 0x55: "EOR", 0x56: "LSR",
        0x58: "CLI", 0x59: "EOR", 0x5D: "EOR", 0x5E: "LSR", 0x60: "RTS",
        0x61: "ADC", 0x65: "ADC", 0x66: "ROR", 0x68: "PLA", 0x69: "ADC",
        0x6A: "ROR", 0x6C: "JMP", 0x6D: "ADC", 0x6E: "ROR", 0x70: "BVS",
        0x71: "ADC", 0x75: "ADC", 0x76: "ROR", 0x78: "SEI", 0x79: "ADC",
        0x7D: "ADC", 0x7E: "ROR", 0x81: "STA", 0x84: "STY", 0x85: "STA",
        0x86: "STX", 0x88: "DEY", 0x8A: "TXA", 0x8C: "STY", 0x8D: "STA",
        0x8E: "STX", 0x90: "BCC", 0x91: "STA", 0x94: "STY", 0x95: "STA",
        0x96: "STX", 0x98: "TYA", 0x99: "STA", 0x9A: "TXS", 0x9D: "STA",
        0xA0: "LDY", 0xA1: "LDA", 0xA2: "LDX", 0xA4: "LDY", 0xA5: "LDA",
        0xA6: "LDX", 0xA8: "TAY", 0xA9: "LDA", 0xAA: "TAX", 0xAC: "LDY",
        0xAD: "LDA", 0xAE: "LDX", 0xB0: "BCS", 0xB1: "LDA", 0xB4: "LDY",
        0xB5: "LDA", 0xB6: "LDX", 0xB8: "CLV", 0xB9: "LDA", 0xBA: "TSX",
        0xBC: "LDY", 0xBD: "LDA", 0xBE: "LDX", 0xC0: "CPY", 0xC1: "CMP",
        0xC4: "CPY", 0xC5: "CMP", 0xC6: "DEC", 0xC8: "INY", 0xC9: "CMP",
        0xCA: "DEX", 0xCC: "CPY", 0xCD: "CMP", 0xCE: "DEC", 0xD0: "BNE",
        0xD1: "CMP", 0xD5: "CMP", 0xD6: "DEC", 0xD8: "CLD", 0xD9: "CMP",
        0xDD: "CMP", 0xDE: "DEC", 0xE0: "CPX", 0xE1: "SBC", 0xE4: "CPX",
        0xE5: "SBC", 0xE6: "INC", 0xE8: "INX", 0xE9: "SBC", 0xEA: "NOP",
        0xEC: "CPX", 0xED: "SBC", 0xEE: "INC", 0xF0: "BEQ", 0xF1: "SBC",
        0xF5: "SBC", 0xF6: "INC", 0xF8: "SED", 0xF9: "SBC", 0xFD: "SBC",
        0xFE: "INC",
    }
    mnemonic = MNEMONICS.get(opcode, f"???({opcode:02X})")

    if length == 1:
        return mnemonic
    elif length == 2:
        operand = rom[offset + 1] if offset + 1 < len(rom) else 0
        return f"{mnemonic} ${operand:02X}"
    else:
        lo = rom[offset + 1] if offset + 1 < len(rom) else 0
        hi = rom[offset + 2] if offset + 2 < len(rom) else 0
        return f"{mnemonic} ${hi:02X}{lo:02X}"


def find_exact_instruction_match(rom: bytes, instruction: bytes) -> list[int]:
    """Find all offsets in the ROM where the exact instruction bytes appear
    at a valid instruction boundary (scanning from the start)."""
    matches = []
    # Scan entire ROM to find the byte pattern
    target = instruction
    offset = 0
    while offset < len(rom):
        idx = rom.find(target, offset)
        if idx == -1:
            break
        matches.append(ROM_BASE + idx)
        offset = idx + 1
    return matches


def find_fingerprint_matches(
    rom: bytes,
    fingerprint: list[int],
    instruction_bytes: bytes,
) -> list[int]:
    """Find addresses in the ROM where the opcode fingerprint matches.

    Walks the ROM from the beginning to find instruction boundaries,
    then checks each for a matching opcode sequence.
    """
    matches = []
    # Walk through the ROM instruction by instruction from the start
    offset = 0
    while offset < len(rom):
        opcode = rom[offset]
        length = get_opcode_length(opcode)

        # Check if fingerprint matches starting here
        if opcode == fingerprint[0]:
            fp = get_opcode_fingerprint(rom, ROM_BASE + offset, len(fingerprint))
            if fp == fingerprint:
                matches.append(ROM_BASE + offset)

        offset += length

    return matches


def extract_asm_addresses(asm_filepath: Path) -> set[int]:
    """Extract all instruction boundary addresses from the assembly output.

    Parses '; XXXX: NN' patterns and ':XXXX[N]' patterns.
    """
    addresses = set()
    source = asm_filepath.read_text()

    # ROM addresses: '; 8000: 4c d4 80    L..'
    for m in re.finditer(r";\s+([0-9a-f]{4}):\s+[0-9a-f]{2}\b", source):
        addresses.add(int(m.group(1), 16))

    # Runtime addresses for relocated code: ':XXXX[N]'
    for m in re.finditer(r":([0-9a-f]{4})\[\d+\]", source):
        addresses.add(int(m.group(1), 16))

    return addresses


def main():
    repo_root = Path(
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    )

    rom_334b_filepath = repo_root / "versions" / "3.34B" / "rom" / "nfs-3.34B.rom"
    rom_335d_filepath = repo_root / "versions" / "3.35D" / "rom" / "nfs-3.35D.rom"
    asm_335d_filepath = repo_root / "versions" / "3.35D" / "output" / "nfs-3.35D.asm"

    for filepath in (rom_334b_filepath, rom_335d_filepath, asm_335d_filepath):
        if not filepath.exists():
            print(f"ERROR: {filepath} not found", file=sys.stderr)
            sys.exit(1)

    rom_334b = rom_334b_filepath.read_bytes()
    rom_335d = rom_335d_filepath.read_bytes()
    asm_addresses = extract_asm_addresses(asm_335d_filepath)

    print(f"Loaded 3.34B ROM: {len(rom_334b)} bytes")
    print(f"Loaded 3.35D ROM: {len(rom_335d)} bytes")
    print(f"Loaded {len(asm_addresses)} instruction boundaries from 3.35D assembly")
    print()

    # Stale comment addresses (3.34B addresses)
    stale_comments = [
        (0x8075, "inline", "Y=&20: base offset for *NET commands (index 33+)"),
        (0x80A8, "inline", "Load low byte of (handler - 1) from table"),
        (0x80AB, "inline", "Push low byte onto stack"),
        (0x80AE, "inline", "RTS pops address, adds 1, jumps to handler"),
        (0x809D, "inline", "Y=&0D: base offset for language handlers (index 14+)"),
        (0x8290, "inline", "OSBYTE &FD: read type of last reset"),
        (0x829C, "inline", "Station &FE = no server selected"),
        (0x82CA, "inline", "Initialise ADLC hardware"),
        (0x8095, "inline", "Y=&12: base offset for FSCV dispatch (indices 19+)"),
        (0x8DFA, "inline", "Subtract &0F: OSWORD &0F-&13 become indices 0-4"),
        (0x8E19, "inline", "Dispatch table: low bytes for OSWORD &0F-&13 handlers"),
        (0x8E1E, "inline", "Dispatch table: high bytes for OSWORD &0F-&13 handlers"),
        (0x80F9, "block", "Copy NMI handler code from ROM to RAM pages &04-&06"),
        (0x8113, "block", "Copy NMI workspace initialiser from ROM to &0016-&0076"),
        (0x8FBF, "inline", "Non-zero = error/timeout: jump to cleanup"),
        (0x8FF0, "inline", "Test for end-of-data marker (&0D)"),
        (0x9021, "inline", "PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it"),
    ]

    print("=" * 120)
    print("STALE COMMENT ADDRESS MAPPING: 3.34B -> 3.35D")
    print("=" * 120)
    print()

    for addr_334b, comment_type, comment_text in stale_comments:
        print("-" * 120)
        print(f"Comment: \"{comment_text}\" ({comment_type})")
        print(f"3.34B address: ${addr_334b:04X}")

        # Extract instruction at 3.34B address
        instr_334b = get_instruction_bytes(rom_334b, addr_334b)
        disasm_334b = disassemble_instruction(rom_334b, addr_334b)
        print(f"3.34B instruction: [{format_bytes(instr_334b)}] {disasm_334b}")

        # Get opcode fingerprint (sequence of opcodes, 5 instructions)
        fingerprint = get_opcode_fingerprint(rom_334b, addr_334b, 5)
        print(
            f"Opcode fingerprint (5 instr): "
            f"[{' '.join(f'{op:02X}' for op in fingerprint)}]"
        )

        # Show the full instruction sequence for context
        seq_334b = get_instruction_sequence(rom_334b, addr_334b, 5)
        print(f"Full instruction sequence:")
        seq_addr = addr_334b
        for instr in seq_334b:
            print(
                f"  ${seq_addr:04X}: [{format_bytes(instr)}] "
                f"{disassemble_instruction(rom_334b, seq_addr)}"
            )
            seq_addr += len(instr)

        # Strategy 1: Find exact full-instruction-sequence match in 3.35D
        # Try matching progressively shorter sequences
        best_match = None
        best_confidence = None

        # Try matching 5, 4, 3 instruction sequences (full bytes)
        for seq_len in (5, 4, 3):
            seq = get_instruction_sequence(rom_334b, addr_334b, seq_len)
            pattern = b"".join(seq)
            candidates = find_exact_instruction_match(rom_335d, pattern)
            # Filter to instruction boundaries
            boundary_candidates = [a for a in candidates if a in asm_addresses]

            if len(boundary_candidates) == 1:
                best_match = boundary_candidates[0]
                best_confidence = f"exact match ({seq_len}-instr sequence, {len(pattern)} bytes)"
                break
            elif len(boundary_candidates) > 1:
                # Try longer sequence to disambiguate
                continue
            elif len(candidates) == 1:
                best_match = candidates[0]
                best_confidence = (
                    f"exact match ({seq_len}-instr sequence, {len(pattern)} bytes)"
                    " [NOT on boundary]"
                )
                break

        # Strategy 2: If no exact match, try opcode fingerprint
        if best_match is None:
            for fp_len in (6, 5, 4):
                fp = get_opcode_fingerprint(rom_334b, addr_334b, fp_len)
                candidates = find_fingerprint_matches(rom_335d, fp, instr_334b)
                boundary_candidates = [a for a in candidates if a in asm_addresses]

                if len(boundary_candidates) == 1:
                    best_match = boundary_candidates[0]
                    best_confidence = f"unique fingerprint ({fp_len} opcodes)"
                    break
                elif len(boundary_candidates) > 1:
                    # Use surrounding context to disambiguate: check if exact
                    # first instruction also matches
                    refined = [
                        a
                        for a in boundary_candidates
                        if get_instruction_bytes(rom_335d, a) == instr_334b
                    ]
                    if len(refined) == 1:
                        best_match = refined[0]
                        best_confidence = (
                            f"fingerprint ({fp_len} opcodes) + exact first instr"
                        )
                        break
                    elif len(refined) > 1:
                        # Still multiple -- try using the 2-instruction prefix
                        seq2 = b"".join(
                            get_instruction_sequence(rom_334b, addr_334b, 2)
                        )
                        refined2 = [
                            a
                            for a in refined
                            if rom_335d[a - ROM_BASE : a - ROM_BASE + len(seq2)]
                            == seq2
                        ]
                        if len(refined2) == 1:
                            best_match = refined2[0]
                            best_confidence = (
                                f"fingerprint ({fp_len} opcodes) "
                                "+ exact 2-instr prefix"
                            )
                            break
                        # Report multiple candidates
                        print(f"\n  MULTIPLE CANDIDATES ({len(refined)} matches):")
                        for c in refined:
                            on_boundary = c in asm_addresses
                            disasm = disassemble_instruction(rom_335d, c)
                            instr = get_instruction_bytes(rom_335d, c)
                            print(
                                f"    ${c:04X}: [{format_bytes(instr)}] {disasm}"
                                f"  boundary={on_boundary}"
                            )
                        continue

        # Strategy 3: For data tables (like dispatch tables), try matching
        # a shorter run of exact bytes (3-5 bytes)
        if best_match is None:
            for byte_len in (5, 4, 3, 2):
                offset_334b = addr_334b - ROM_BASE
                if offset_334b + byte_len > len(rom_334b):
                    continue
                pattern = rom_334b[offset_334b : offset_334b + byte_len]
                matches = []
                idx = 0
                while idx < len(rom_335d):
                    found = rom_335d.find(pattern, idx)
                    if found == -1:
                        break
                    candidate_addr = ROM_BASE + found
                    if candidate_addr in asm_addresses:
                        matches.append(candidate_addr)
                    idx = found + 1

                if len(matches) == 1:
                    best_match = matches[0]
                    best_confidence = f"exact byte match ({byte_len} bytes)"
                    break
                elif len(matches) > 1 and byte_len >= 4:
                    # Show candidates
                    print(
                        f"\n  MULTIPLE BYTE MATCHES ({len(matches)} for "
                        f"{byte_len} bytes):"
                    )
                    for c in matches[:10]:
                        on_boundary = c in asm_addresses
                        instr = rom_335d[
                            c - ROM_BASE : c - ROM_BASE + byte_len
                        ]
                        print(
                            f"    ${c:04X}: [{format_bytes(instr)}]"
                            f"  boundary={on_boundary}"
                        )

        # Report result
        print()
        if best_match is not None:
            instr_335d = get_instruction_bytes(rom_335d, best_match)
            disasm_335d = disassemble_instruction(rom_335d, best_match)
            on_boundary = best_match in asm_addresses

            print(f"  PROPOSED 3.35D address: ${best_match:04X}")
            print(f"  3.35D instruction: [{format_bytes(instr_335d)}] {disasm_335d}")
            print(f"  Instruction boundary: {'YES' if on_boundary else 'NO'}")
            print(f"  Confidence: {best_confidence}")
            print(f"  Offset delta: {best_match - addr_334b:+d} bytes")

            # Show surrounding context in 3.35D
            print(f"  3.35D context:")
            ctx_addr = best_match
            for instr in get_instruction_sequence(rom_335d, best_match, 5):
                print(
                    f"    ${ctx_addr:04X}: [{format_bytes(instr)}] "
                    f"{disassemble_instruction(rom_335d, ctx_addr)}"
                )
                ctx_addr += len(instr)
        else:
            print(f"  PROPOSED 3.35D address: NOT FOUND")
            print(f"  Confidence: no match found")

        print()

    # Summary table
    print()
    print("=" * 120)
    print("SUMMARY TABLE")
    print("=" * 120)
    print(
        f"{'3.34B':>7}  {'3.35D':>7}  {'Delta':>6}  {'Boundary':>8}  "
        f"{'Confidence':<50}  Comment"
    )
    print("-" * 120)

    for addr_334b, comment_type, comment_text in stale_comments:
        instr_334b = get_instruction_bytes(rom_334b, addr_334b)
        fingerprint = get_opcode_fingerprint(rom_334b, addr_334b, 5)

        best_match = None
        best_confidence = None

        # Repeat the same search logic for summary
        for seq_len in (5, 4, 3):
            seq = get_instruction_sequence(rom_334b, addr_334b, seq_len)
            pattern = b"".join(seq)
            candidates = find_exact_instruction_match(rom_335d, pattern)
            boundary_candidates = [a for a in candidates if a in asm_addresses]
            if len(boundary_candidates) == 1:
                best_match = boundary_candidates[0]
                best_confidence = f"exact ({seq_len}-instr)"
                break
            elif len(candidates) == 1:
                best_match = candidates[0]
                best_confidence = f"exact ({seq_len}-instr) [no boundary]"
                break

        if best_match is None:
            for fp_len in (6, 5, 4):
                fp = get_opcode_fingerprint(rom_334b, addr_334b, fp_len)
                candidates = find_fingerprint_matches(rom_335d, fp, instr_334b)
                boundary_candidates = [a for a in candidates if a in asm_addresses]
                if len(boundary_candidates) == 1:
                    best_match = boundary_candidates[0]
                    best_confidence = f"fingerprint ({fp_len} opcodes)"
                    break
                elif len(boundary_candidates) > 1:
                    refined = [
                        a
                        for a in boundary_candidates
                        if get_instruction_bytes(rom_335d, a) == instr_334b
                    ]
                    if len(refined) == 1:
                        best_match = refined[0]
                        best_confidence = f"fp({fp_len}) + exact instr"
                        break
                    elif len(refined) > 1:
                        seq2 = b"".join(
                            get_instruction_sequence(rom_334b, addr_334b, 2)
                        )
                        refined2 = [
                            a
                            for a in refined
                            if rom_335d[a - ROM_BASE : a - ROM_BASE + len(seq2)]
                            == seq2
                        ]
                        if len(refined2) == 1:
                            best_match = refined2[0]
                            best_confidence = f"fp({fp_len}) + 2-instr prefix"
                            break

        if best_match is None:
            for byte_len in (5, 4, 3, 2):
                offset_334b = addr_334b - ROM_BASE
                if offset_334b + byte_len > len(rom_334b):
                    continue
                pattern = rom_334b[offset_334b : offset_334b + byte_len]
                matches = []
                idx = 0
                while idx < len(rom_335d):
                    found = rom_335d.find(pattern, idx)
                    if found == -1:
                        break
                    candidate_addr = ROM_BASE + found
                    if candidate_addr in asm_addresses:
                        matches.append(candidate_addr)
                    idx = found + 1
                if len(matches) == 1:
                    best_match = matches[0]
                    best_confidence = f"byte match ({byte_len}B)"
                    break

        if best_match is not None:
            on_boundary = best_match in asm_addresses
            delta = best_match - addr_334b
            addr_str = f"${best_match:04X}"
            boundary_str = "YES" if on_boundary else "NO"
            delta_str = f"{delta:+d}"
        else:
            addr_str = "NOT FOUND"
            boundary_str = "-"
            delta_str = "-"
            best_confidence = "no match"

        text_short = comment_text[:45]
        print(
            f"${addr_334b:04X}  {addr_str:>7}  {delta_str:>6}  "
            f"{boundary_str:>8}  {best_confidence:<50}  {text_short}"
        )


if __name__ == "__main__":
    main()
