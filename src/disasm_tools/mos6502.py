"""MOS 6502 processor constants for disassembly tools."""

# Standard BBC Micro sideways ROM base address and size.
ROM_BASE = 0x8000
ROM_SIZE = 8192

# Instruction lengths indexed by opcode byte (0-255).
# 0 = invalid/undefined, 1 = implied/accumulator,
# 2 = immediate/zp/rel, 3 = absolute
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

# Mnemonics indexed by opcode byte (0-255).
# "???" for invalid/undefined opcodes.
OPCODE_MNEMONICS = [
    # $00-$0F
    "BRK", "ORA", "???", "???", "???", "ORA", "ASL", "???",
    "PHP", "ORA", "ASL", "???", "???", "ORA", "ASL", "???",
    # $10-$1F
    "BPL", "ORA", "???", "???", "???", "ORA", "ASL", "???",
    "CLC", "ORA", "???", "???", "???", "ORA", "ASL", "???",
    # $20-$2F
    "JSR", "AND", "???", "???", "BIT", "AND", "ROL", "???",
    "PLP", "AND", "ROL", "???", "BIT", "AND", "ROL", "???",
    # $30-$3F
    "BMI", "AND", "???", "???", "???", "AND", "ROL", "???",
    "SEC", "AND", "???", "???", "???", "AND", "ROL", "???",
    # $40-$4F
    "RTI", "EOR", "???", "???", "???", "EOR", "LSR", "???",
    "PHA", "EOR", "LSR", "???", "JMP", "EOR", "LSR", "???",
    # $50-$5F
    "BVC", "EOR", "???", "???", "???", "EOR", "LSR", "???",
    "CLI", "EOR", "???", "???", "???", "EOR", "LSR", "???",
    # $60-$6F
    "RTS", "ADC", "???", "???", "???", "ADC", "ROR", "???",
    "PLA", "ADC", "ROR", "???", "JMP", "ADC", "ROR", "???",
    # $70-$7F
    "BVS", "ADC", "???", "???", "???", "ADC", "ROR", "???",
    "SEI", "ADC", "???", "???", "???", "ADC", "ROR", "???",
    # $80-$8F
    "???", "STA", "???", "???", "STY", "STA", "STX", "???",
    "DEY", "???", "TXA", "???", "STY", "STA", "STX", "???",
    # $90-$9F
    "BCC", "STA", "???", "???", "STY", "STA", "STX", "???",
    "TYA", "STA", "TXS", "???", "???", "STA", "???", "???",
    # $A0-$AF
    "LDY", "LDA", "LDX", "???", "LDY", "LDA", "LDX", "???",
    "TAY", "LDA", "TAX", "???", "LDY", "LDA", "LDX", "???",
    # $B0-$BF
    "BCS", "LDA", "???", "???", "LDY", "LDA", "LDX", "???",
    "CLV", "LDA", "TSX", "???", "LDY", "LDA", "LDX", "???",
    # $C0-$CF
    "CPY", "CMP", "???", "???", "CPY", "CMP", "DEC", "???",
    "INY", "CMP", "DEX", "???", "CPY", "CMP", "DEC", "???",
    # $D0-$DF
    "BNE", "CMP", "???", "???", "???", "CMP", "DEC", "???",
    "CLD", "CMP", "???", "???", "???", "CMP", "DEC", "???",
    # $E0-$EF
    "CPX", "SBC", "???", "???", "CPX", "SBC", "INC", "???",
    "INX", "SBC", "NOP", "???", "CPX", "SBC", "INC", "???",
    # $F0-$FF
    "BEQ", "SBC", "???", "???", "???", "SBC", "INC", "???",
    "SED", "SBC", "???", "???", "???", "SBC", "INC", "???",
]


# 65C02 / 65SC12 (CMOS 6502, used in BBC Master 128) extends the 6502
# instruction set. The lengths and mnemonics below differ from the NMOS
# 6502 only at the opcodes the CMOS variant defines.
#
# Source: py8dis/cpu65C02.py.
_CMOS_OVERRIDES = {
    0x04: (2, "TSB"),  # TSB zp
    0x0C: (3, "TSB"),  # TSB addr
    0x12: (2, "ORA"),  # ORA (zp)
    0x14: (2, "TRB"),  # TRB zp
    0x1A: (1, "INC"),  # INC A
    0x1C: (3, "TRB"),  # TRB addr
    0x32: (2, "AND"),  # AND (zp)
    0x34: (2, "BIT"),  # BIT zp,X
    0x3A: (1, "DEC"),  # DEC A
    0x3C: (3, "BIT"),  # BIT addr,X
    0x52: (2, "EOR"),  # EOR (zp)
    0x5A: (1, "PHY"),  # PHY
    0x64: (2, "STZ"),  # STZ zp
    0x72: (2, "ADC"),  # ADC (zp)
    0x74: (2, "STZ"),  # STZ zp,X
    0x7A: (1, "PLY"),  # PLY
    0x7C: (3, "JMP"),  # JMP (addr,X)
    0x80: (2, "BRA"),  # BRA offset
    0x89: (2, "BIT"),  # BIT #imm
    0x92: (2, "STA"),  # STA (zp)
    0x9C: (3, "STZ"),  # STZ addr
    0x9E: (3, "STZ"),  # STZ addr,X
    0xB2: (2, "LDA"),  # LDA (zp)
    0xD2: (2, "CMP"),  # CMP (zp)
    0xDA: (1, "PHX"),  # PHX
    0xF2: (2, "SBC"),  # SBC (zp)
    0xFA: (1, "PLX"),  # PLX
}

OPCODE_LENGTHS_65C02 = list(OPCODE_LENGTHS)
OPCODE_MNEMONICS_65C02 = list(OPCODE_MNEMONICS)
for _op, (_len, _mne) in _CMOS_OVERRIDES.items():
    OPCODE_LENGTHS_65C02[_op] = _len
    OPCODE_MNEMONICS_65C02[_op] = _mne


def opcode_tables(cpu):
    """Return (lengths, mnemonics) for the named CPU.

    Recognised values: '6502' (default), '65c02' (CMOS, Master 128).
    """
    cpu = (cpu or "6502").lower()
    if cpu in ("6502", ""):
        return OPCODE_LENGTHS, OPCODE_MNEMONICS
    if cpu in ("65c02", "65sc12", "65c12", "cmos"):
        return OPCODE_LENGTHS_65C02, OPCODE_MNEMONICS_65C02
    raise ValueError(f"Unknown CPU: {cpu!r}")

