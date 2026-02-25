#!/usr/bin/env python3
"""Investigate restructured code regions between NFS 3.40 and 3.60.

For each UNMAPPED region, shows a side-by-side disassembly of 3.40 and 3.60
to understand how the code was reorganised.
"""

import sys
from pathlib import Path

ROM_BASE = 0x8000

OPCODE_LENGTHS = [
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 0, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    3, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    1, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    0, 2, 0, 0, 2, 2, 2, 0, 1, 0, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 3, 1, 0, 0, 3, 0, 0,
    2, 2, 2, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 3, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
    2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 1, 0, 3, 3, 3, 0,
    2, 2, 0, 0, 0, 2, 2, 0, 1, 3, 0, 0, 0, 3, 3, 0,
]

MNEMONICS = [
    "BRK","ORA","???","???","???","ORA","ASL","???","PHP","ORA","ASL","???","???","ORA","ASL","???",
    "BPL","ORA","???","???","???","ORA","ASL","???","CLC","ORA","???","???","???","ORA","ASL","???",
    "JSR","AND","???","???","BIT","AND","ROL","???","PLP","AND","ROL","???","BIT","AND","ROL","???",
    "BMI","AND","???","???","???","AND","ROL","???","SEC","AND","???","???","???","AND","ROL","???",
    "RTI","EOR","???","???","???","EOR","LSR","???","PHA","EOR","LSR","???","JMP","EOR","LSR","???",
    "BVC","EOR","???","???","???","EOR","LSR","???","CLI","EOR","???","???","???","EOR","LSR","???",
    "RTS","ADC","???","???","???","ADC","ROR","???","PLA","ADC","ROR","???","JMP","ADC","ROR","???",
    "BVS","ADC","???","???","???","ADC","ROR","???","SEI","ADC","???","???","???","ADC","ROR","???",
    "???","STA","???","???","STY","STA","STX","???","DEY","???","TXA","???","STY","STA","STX","???",
    "BCC","STA","???","???","STY","STA","STX","???","TYA","STA","TXS","???","???","STA","???","???",
    "LDY","LDA","LDX","???","LDY","LDA","LDX","???","TAY","LDA","TAX","???","LDY","LDA","LDX","???",
    "BCS","LDA","???","???","LDY","LDA","LDX","???","CLV","LDA","TSX","???","LDY","LDA","LDX","???",
    "CPY","CMP","???","???","CPY","CMP","DEC","???","INY","CMP","DEX","???","CPY","CMP","DEC","???",
    "BNE","CMP","???","???","???","CMP","DEC","???","CLD","CMP","???","???","???","CMP","DEC","???",
    "CPX","SBC","???","???","CPX","SBC","INC","???","INX","SBC","NOP","???","CPX","SBC","INC","???",
    "BEQ","SBC","???","???","???","SBC","INC","???","SED","SBC","???","???","???","SBC","INC","???",
]

ADDR_MODES = [
    "imp","x_ind","imp","imp","imp","zpg","zpg","imp","imp","imm","acc","imp","imp","abs","abs","imp",
    "rel","ind_y","imp","imp","imp","zpg_x","zpg_x","imp","imp","abs_y","imp","imp","imp","abs_x","abs_x","imp",
    "abs","x_ind","imp","imp","zpg","zpg","zpg","imp","imp","imm","acc","imp","abs","abs","abs","imp",
    "rel","ind_y","imp","imp","imp","zpg_x","zpg_x","imp","imp","abs_y","imp","imp","imp","abs_x","abs_x","imp",
    "imp","x_ind","imp","imp","imp","zpg","zpg","imp","imp","imm","acc","imp","abs","abs","abs","imp",
    "rel","ind_y","imp","imp","imp","zpg_x","zpg_x","imp","imp","abs_y","imp","imp","imp","abs_x","abs_x","imp",
    "imp","x_ind","imp","imp","imp","zpg","zpg","imp","imp","imm","acc","imp","ind","abs","abs","imp",
    "rel","ind_y","imp","imp","imp","zpg_x","zpg_x","imp","imp","abs_y","imp","imp","imp","abs_x","abs_x","imp",
    "imp","x_ind","imp","imp","zpg","zpg","zpg","imp","imp","imp","imp","imp","abs","abs","abs","imp",
    "rel","ind_y","imp","imp","zpg_x","zpg_x","zpg_y","imp","imp","abs_y","imp","imp","imp","abs_x","imp","imp",
    "imm","x_ind","imm","imp","zpg","zpg","zpg","imp","imp","imm","imp","imp","abs","abs","abs","imp",
    "rel","ind_y","imp","imp","zpg_x","zpg_x","zpg_y","imp","imp","abs_y","imp","imp","abs_x","abs_x","abs_y","imp",
    "imm","x_ind","imp","imp","zpg","zpg","zpg","imp","imp","imm","imp","imp","abs","abs","abs","imp",
    "rel","ind_y","imp","imp","imp","zpg_x","zpg_x","imp","imp","abs_y","imp","imp","imp","abs_x","abs_x","imp",
    "imm","x_ind","imp","imp","zpg","zpg","zpg","imp","imp","imm","imp","imp","abs","abs","abs","imp",
    "rel","ind_y","imp","imp","imp","zpg_x","zpg_x","imp","imp","abs_y","imp","imp","imp","abs_x","abs_x","imp",
]


def disasm_region(data, start_addr, end_addr, labels=None):
    """Disassemble a region of ROM data, returning formatted lines."""
    if labels is None:
        labels = {}
    lines = []
    off = start_addr - ROM_BASE
    end_off = end_addr - ROM_BASE
    while off < end_off and off < len(data):
        addr = ROM_BASE + off
        opcode = data[off]
        length = OPCODE_LENGTHS[opcode]
        if length == 0:
            length = 1

        # Get bytes
        raw = data[off:off+length]
        hex_bytes = ' '.join(f'{b:02X}' for b in raw)

        # Format instruction
        mnem = MNEMONICS[opcode]
        mode = ADDR_MODES[opcode]

        if length == 1:
            if mode == 'acc':
                operand = 'A'
            else:
                operand = ''
        elif length == 2:
            val = data[off+1]
            if mode == 'imm':
                operand = f'#${val:02X}'
            elif mode == 'zpg':
                operand = f'${val:02X}'
            elif mode == 'zpg_x':
                operand = f'${val:02X},X'
            elif mode == 'zpg_y':
                operand = f'${val:02X},Y'
            elif mode == 'x_ind':
                operand = f'(${val:02X},X)'
            elif mode == 'ind_y':
                operand = f'(${val:02X}),Y'
            elif mode == 'rel':
                target = addr + 2 + (val if val < 128 else val - 256)
                operand = f'${target:04X}'
            else:
                operand = f'${val:02X}'
        elif length == 3:
            val = data[off+1] | (data[off+2] << 8)
            if mode == 'abs':
                operand = f'${val:04X}'
            elif mode == 'abs_x':
                operand = f'${val:04X},X'
            elif mode == 'abs_y':
                operand = f'${val:04X},Y'
            elif mode == 'ind':
                operand = f'(${val:04X})'
            else:
                operand = f'${val:04X}'
        else:
            operand = ''

        label_str = ''
        if addr in labels:
            label_str = f'  ; {labels[addr]}'

        instr = f'{mnem} {operand}'.strip()
        lines.append(f'  ${addr:04X}: {hex_bytes:<9s} {instr:<16s}{label_str}')
        off += length
    return lines


def show_region(title, data40, data60, addr40_start, addr40_end, addr60_start, addr60_end,
                labels40=None, labels60=None):
    """Show side-by-side comparison of a code region."""
    print(f'\n{"=" * 72}')
    print(f'{title}')
    print(f'{"=" * 72}')
    print(f'\n--- 3.40: ${addr40_start:04X}-${addr40_end:04X} ({addr40_end - addr40_start} bytes) ---')
    for line in disasm_region(data40, addr40_start, addr40_end, labels40):
        print(line)
    print(f'\n--- 3.60: ${addr60_start:04X}-${addr60_end:04X} ({addr60_end - addr60_start} bytes) ---')
    for line in disasm_region(data60, addr60_start, addr60_end, labels60):
        print(line)


def main():
    base = Path('/Users/rjs/Code/acornaeology/acorn-nfs')
    data40 = (base / 'versions/3.40/rom/nfs-3.40.rom').read_bytes()
    data60 = (base / 'versions/3.60/rom/nfs-3.60.rom').read_bytes()

    region = sys.argv[1] if len(sys.argv) > 1 else 'all'

    if region in ('all', 'tx_poll'):
        # TX poll routines: 3.40 &8687-&86D7, 3.60 equivalent area
        show_region(
            'TX POLL ROUTINES (setup_tx_ptr_c0 / tx_poll_ff / tx_poll_core)',
            data40, data60,
            0x8687, 0x86D7,  # 3.40
            0x86DD, 0x8720,  # 3.60 (shifted, based on mapped neighbours)
            labels40={0x8687: 'setup_tx_ptr_c0', 0x868F: 'tx_poll_ff',
                      0x8691: 'tx_poll_timeout', 0x8693: 'tx_poll_core',
                      0x86AD: 'l4'},
        )

    if region in ('all', 'catalogue'):
        # Catalogue display: 3.40 &8D22-&8D70, 3.60 equivalent
        show_region(
            'CATALOGUE DISPLAY (print_file_info / pad_filename_spaces / print_exec_and_len)',
            data40, data60,
            0x8D22, 0x8D70,  # 3.40
            0x8D6E, 0x8DC0,  # 3.60
            labels40={0x8D24: 'print_file_info', 0x8D45: 'pad_filename_spaces',
                      0x8D58: 'print_exec_and_len'},
        )

    if region in ('all', 'copyl3'):
        # OSWORD area: 3.40 &8EAF-&8EC0, 3.60 equivalent
        show_region(
            'OSWORD AREA (copyl3)',
            data40, data60,
            0x8EAF, 0x8EC0,  # 3.40
            0x8EB7, 0x8EC8,  # 3.60
            labels40={0x8EB3: 'copyl3'},
        )

    if region in ('all', 'fscv_args'):
        # FSCV args: 3.40 &85C5-&85E0, 3.60 equivalent
        show_region(
            'FSCV ARGS (save_fscv_args_with_ptrs)',
            data40, data60,
            0x85C5, 0x85E0,  # 3.40
            0x85CC, 0x85E5,  # 3.60
            labels40={0x85C8: 'save_fscv_args_with_ptrs', 0x85D2: 'save_fscv_args'},
        )

    if region in ('all', 'irq_service'):
        # IRQ service: 3.40 &9B30-&9B80, 3.60 equivalent
        show_region(
            'IRQ SERVICE (entry at 0x9B35)',
            data40, data60,
            0x9B30, 0x9B80,  # 3.40
            0x9B1B, 0x9B30,  # 3.60
            labels40={0x9B35: 'irq_service_entry'},
        )

    if region in ('all', 'ex_handler'):
        # EX handler: 3.40 &8C18-&8C30, 3.60 equivalent
        show_region(
            'EX HANDLER (ex_handler at 0x8C1B)',
            data40, data60,
            0x8C18, 0x8C35,  # 3.40
            0x8C5E, 0x8C80,  # 3.60
            labels40={0x8C1B: 'ex_handler'},
        )

    if region in ('all', 'save_econet'):
        # Save econet state: 3.40 &96C5-&96F5, 3.60 equivalent
        show_region(
            'SAVE ECONET STATE (save_econet_state at 0x96C8)',
            data40, data60,
            0x96C5, 0x96F5,  # 3.40
            0x96B5, 0x96F5,  # 3.60
            labels40={0x96C8: 'save_econet_state', 0x96D8: 'adlc_full_reset',
                      0x96E7: 'adlc_rx_listen', 0x96EC: 'adlc_init_cr2'},
        )

    if region in ('all', 'dispatch'):
        # Y-indexed dispatch tables: search 3.60 for replacements
        print(f'\n{"=" * 72}')
        print('Y-INDEXED DISPATCH TABLES')
        print(f'{"=" * 72}')
        print('\n3.40 had 3 Y-indexed dispatch tables (LDA tbl,Y / PHA / LDA tbl,Y / PHA):')
        print('  $9A79: LDA $9A0C,Y PHA LDA $9A04,Y PHA  (immediate op)')
        print('  $9B6B: LDA $9AF6,Y PHA LDA $9AF1,Y PHA  (TX completion)')
        print('  $9CB2: LDA $9C42,Y PHA LDA $9C3A,Y PHA  (TX ctrl byte)')
        print('\n3.60 has 0 Y-indexed dispatch tables — all removed.')
        print('\nSearching for alternative dispatch patterns in 3.60...')

        # Check for JSR-based or JMP-based dispatch alternatives
        # Look for TYA / ASL / TAY / LDA tbl,Y patterns (table jump via doubling)
        for off in range(len(data60) - 6):
            # TAX/TAY followed by LDA abs,X/Y then JMP (indirect)
            pass

        # Show the 3.40 dispatch areas to understand what they dispatched
        show_region(
            'IMMEDIATE OP DISPATCH (3.40 $9A79, UNMAPPED in 3.60)',
            data40, data60,
            0x9A70, 0x9A90,
            0x9A50, 0x9A70,  # approximate 3.60 area
            labels40={0x9A79: 'dispatch_imm_op'},
        )


if __name__ == '__main__':
    main()
