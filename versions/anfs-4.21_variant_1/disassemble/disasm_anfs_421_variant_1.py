import os
from pathlib import Path
import dasmos
from dasmos import Align
from dasmos.hooks import stringhi_hook, stringz_hook
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get('FANTASM_ROM', str(_version_dirpath / 'rom' / 'anfs-4.21_variant_1.rom'))
_output_dirpath = Path(os.environ.get('FANTASM_OUTPUT_DIR', str(_version_dirpath / 'output')))
d = dasmos.Disassembler.create(cpu='65C02', auto_label_data_prefix='l', auto_label_code_prefix='c', auto_label_subroutine_prefix='sub_c', auto_label_loop_prefix='loop_c')
d.load(_rom_filepath, 0x8000)
d.byte(0xBFC7)

d.label(0xBFE6, 'hazel_minus_1a')

d.label(0xBFFE, 'hazel_minus_2')

d.label(0xBFFF, 'hazel_minus_1')

d.label(0xBFC5, 'rom_tail_padding')
d.banner(0xBFC5, title='ROM-tail &FF padding (33 bytes positioning the HAZEL indexing bases)', description="""33 bytes of `&FF` filler between the last real instruction at
[`inx4`](address:BFC0) and the HAZEL indexing-base labels
starting at [`hazel_minus_1a`](address:BFE6).

These bytes exist purely to push the indexing-base labels to
specific addresses immediately before `&C000` (the start of
HAZEL). The labels themselves do the work -- see the
[`hazel_idx_bases`](address:BFE6) banner. The padding is never
read or written; it is whatever the assembler emitted to fill
the gap (the BeebAsm default of `&FF`).""")

d.label(0xBFE6, 'hazel_idx_bases')
d.banner(0xBFE6, title='HAZEL Y-indexed access bases (3 labels at the ROM tail)', description="""Three labels positioned `&1A`, `2`, and `1` bytes before `&C000`
(the start of HAZEL), used as **indexing bases for reads and
writes into HAZEL**.

The trick: HAZEL begins at `&C000`, so an `LDA hazel_minus_2,Y`
/ `STA hazel_minus_2,Y` instruction with Y >= 2 lands at
`&BFFE + Y >= &C000` -- inside HAZEL. ANFS exploits this in
several places to copy fixed-size blocks between HAZEL workspace
and other buffers without burning a separate two-byte zero-page
pointer:

| Site / routine                | instruction                  | base             | Y range | Effective range            |
|-------------------------------|------------------------------|------------------|---------|----------------------------|
| `loop_copy_fs_ctx`            | `STA hazel_minus_2,Y`        | `hazel_minus_2`  | 9..2    | `&C007..&C000`             |
| `loop_restore_ctx`            | `LDA hazel_minus_2,Y`        | `hazel_minus_2`  | 9..2    | `&C007..&C000`             |
| `loop_copy_ws_to_pb`          | `LDA hazel_minus_2,Y`        | `hazel_minus_2`  | 4..6    | `&C002..&C004`             |
| `loop_copy_station`           | `LDA hazel_minus_1,Y`        | `hazel_minus_1`  | 2..1    | `&C001..&C000`             |
| `osword_13_set_station_body`  | `STA hazel_minus_1,Y`        | `hazel_minus_1`  | 2..1    | `&C001..&C000`             |
| `loop_copy_txcb_init`         | `LDA hazel_minus_1a,Y`       | `hazel_minus_1a` | >= &1A  | spans into HAZEL from `&C000` |

Each loop's CPY/BNE guard stops Y before it would land inside
the ROM tail, so the actual workspace data lives entirely in
HAZEL. The labels themselves never have their own bytes read --
the `&FF` byte at each label address is incidental, only the
address matters.""")
d.use_environment('acorn_mos')
d.use_environment('acorn_master_hardware')
d.use_environment('acorn_sideways_rom')
d.hook_subroutine(0x9261, 'print_inline', stringhi_hook)
d.hook_subroutine(0x928A, 'print_inline_no_spool', stringhi_hook)
d.hook_subroutine(0x99C3, 'error_inline', stringz_hook)
d.hook_subroutine(0x99C0, 'error_inline_log', stringz_hook)
d.hook_subroutine(0x99A7, 'error_bad_inline', stringz_hook)

d.label(0xFEA0, 'adlc_cr1', description="""ADLC control register 1 / status register 1.
Write: `CR1` (or `CR3` if `AC=1`). Read: `SR1`.

`SR1` bits: `RDA` (b0), `S2RQ` (b1), `LOOP` (b2), `FD` (b3), `CTS` (b4), `TUF` (b5), `TDRA` (b6), `IRQ` (b7).""", length=1, group='mmio', access='rw')

d.label(0xFEA1, 'adlc_cr2', description="""ADLC control register 2 / status register 2.
Write: `CR2` (or `CR4` if `AC=1`). Read: `SR2`.

`SR2` bits: `AP` (b0), `FV` (b1), `RX_IDLE` (b2), `RX_ABRT` (b3), `ERR` (b4), `DCD` (b5), `OVRN` (b6), `RDA` (b7).""", length=1, group='mmio', access='rw')

d.label(0xFEA2, 'adlc_tx', description="""ADLC TX FIFO continue / RX FIFO read.
Write: byte to TX FIFO with `LAST_DATA = 0` (continue frame).
Read: next byte from RX FIFO.""", length=1, group='mmio', access='rw')

d.label(0xFEA3, 'adlc_tx2', description="""ADLC TX FIFO terminate / RX FIFO read.
Write: final byte of frame (`LAST_DATA = 1`; ADLC appends CRC + closing flag).
Read: next byte from RX FIFO.""", length=1, group='mmio', access='rw')

d.label(0xFE18, 'econet_station_id', description="""Econet station ID register / INTOFF latch.
Read: station DIP-switch byte (1..254) AND INTOFF side-effect (disables NMIs from /NMI input).

ANFS reads this on every NMI entry as the first instruction of the shim, both to capture the station ID and to stop NMIs from re-firing during the body of the handler.""", length=1, group='mmio', access='r')

d.label(0xFE20, 'econet_nmi_enable', description="""Econet NMI-enable register / INTON latch.
Read: re-enables NMIs (INTON side-effect; the value read is ignored).

Used by the NMI-exit shim before `RTI` so the next /NMI edge re-triggers the handler.""", length=1, group='mmio', access='r')

d.label(0xFF1B, 'ev_filev', description='FILEV extended-vector dispatcher (file operations: OSFILE, OSFIND).', length=3, group='ext_vectors', access='r')

d.label(0xFF1E, 'ev_argsv', description='ARGSV extended-vector dispatcher (file argument operations: OSARGS).', length=3, group='ext_vectors', access='r')

d.label(0xFF21, 'ev_bgetv', description='BGETV extended-vector dispatcher (single-byte read: OSBGET).', length=3, group='ext_vectors', access='r')

d.label(0xFF24, 'ev_bputv', description='BPUTV extended-vector dispatcher (single-byte write: OSBPUT).', length=3, group='ext_vectors', access='r')

d.label(0xFF27, 'ev_gbpbv', description='GBPBV extended-vector dispatcher (block transfer: OSGBPB).', length=3, group='ext_vectors', access='r')

d.label(0xFF2A, 'ev_findv', description='FINDV extended-vector dispatcher (open / close: OSFIND).', length=3, group='ext_vectors', access='r')

d.label(0xFF2D, 'ev_fscv', description='FSCV extended-vector dispatcher (filing-system control: OSFSC, *commands).', length=3, group='ext_vectors', access='r')

d.label(0x0212, 'vec_filev', description="FILEV pointer (lo, hi, rom). Patched to ANFS's FILE handler at init.", length=2, group='ram_workspace', access='rw')

d.label(0x0214, 'vec_argsv', description="ARGSV pointer (lo, hi, rom). Patched to ANFS's ARGS handler at init.", length=2, group='ram_workspace', access='rw')

d.label(0x0216, 'vec_bgetv', description="""BGETV pointer (lo, hi, rom). Patched to ANFS's BGET handler at init.

Note: standard layout (the alternate [`vec_bgetv_alt`](address:021A) slot is also used by some routines).""", length=2, group='ram_workspace', access='rw')

d.label(0x0218, 'vec_bputv', description="BPUTV pointer (lo, hi, rom). Patched to ANFS's BPUT handler at init.", length=2, group='ram_workspace', access='rw')

d.label(0x021A, 'vec_bgetv_alt', description="""Alternate BGETV slot (lo, hi, rom).
Some ANFS routines use this in addition to the standard [`vec_bgetv`](address:0216) at &0216.""", length=2, group='ram_workspace', access='rw')

d.label(0x021C, 'vec_gbpbv', description="GBPBV pointer (lo, hi, rom). Patched to ANFS's GBPB handler at init.", length=2, group='ram_workspace', access='rw')

d.label(0x021E, 'vec_fscv', description="FSCV pointer (lo, hi, rom). Patched to ANFS's FSC handler at init.", length=2, group='ram_workspace', access='rw')
d.constant(0x99, 'port_command')
d.constant(0x90, 'port_reply')
d.constant(0x91, 'port_save_ack')
d.constant(0x92, 'port_load_data')
d.constant(0x93, 'port_remote')
d.constant(0xD1, 'port_printer')
d.constant(0xA0, 'err_line_jammed')
d.constant(0xA1, 'err_net_error')
d.constant(0xA2, 'err_not_listening')
d.constant(0xA3, 'err_no_clock')
d.constant(0xA4, 'err_tx_cb_error')
d.constant(0xA5, 'err_no_reply')
d.constant(0xA8, 'err_fs_cutoff')
d.constant(0x80, 'tx_flag')
d.constant(0x7F, 'rx_ready')
d.constant(0xFE, 'cb_stop')
d.constant(0xFD, 'cb_skip')
d.constant(0xFC, 'cb_fill')
d.constant(20, 'osbyte_explode_chars')
d.constant(120, 'osbyte_write_keys_pressed')
d.constant(143, 'osbyte_issue_service_request')
d.constant(168, 'osbyte_read_rom_ptr_table_low')

d.label(0x0097, 'escapable', description='b7=respond to Escape flag', length=1, group='zero_page', access='rw')

d.label(0x0098, 'need_release_tube', description='b7=need to release Tube', length=1, group='zero_page', access='rw')

d.label(0x0099, 'prot_flags', description='PFLAGS: printer / protocol status flags.', length=1, group='zero_page', access='rw')

d.label(0x009A, 'net_tx_ptr', description='NetTx control block pointer (low)', length=1, group='zero_page', access='rw')

d.label(0x009B, 'net_tx_ptr_hi', description='NetTx control block pointer (high)', length=1, group='zero_page', access='rw')

d.label(0x009C, 'net_rx_ptr', description='NetRx control blocks pointer (low byte). Pairs with [`net_rx_ptr_hi`](address:009D).', length=1, group='zero_page', access='rw')

d.label(0x009D, 'net_rx_ptr_hi', description='NetRx control blocks pointer (high byte). Pairs with [`net_rx_ptr`](address:009C) (low).', length=1, group='zero_page', access='rw')

d.label(0x009E, 'nfs_workspace', description='General NFS workspace pointer (low)', length=1, group='zero_page', access='rw')

d.label(0x009F, 'nfs_workspace_hi', description='General NFS workspace pointer (high)', length=1, group='zero_page', access='rw')

d.label(0x00A0, 'nmi_tx_block', description='NMI TX block pointer (low byte). Address of the TX control block currently being transmitted by the NMI handler.', length=1, group='zero_page', access='rw')

d.label(0x00A1, 'nmi_tx_block_hi', description='Block to be transmitted (high)', length=1, group='zero_page', access='rw')

d.label(0x00A2, 'port_buf_len', description='Open port buffer length (low)', length=1, group='zero_page', access='rw')

d.label(0x00A3, 'port_buf_len_hi', description='Open port buffer length (high)', length=1, group='zero_page', access='rw')

d.label(0x00A4, 'open_port_buf', description='Open port buffer address (low)', length=1, group='zero_page', access='rw')

d.label(0x00A5, 'open_port_buf_hi', description='Open port buffer address (high)', length=1, group='zero_page', access='rw')

d.label(0x00A6, 'port_ws_offset', description='Port workspace offset', length=1, group='zero_page', access='rw')

d.label(0x00A7, 'rx_buf_offset', description='Receive buffer offset', length=1, group='zero_page', access='rw')

d.label(0x00A8, 'ws_page', description='Multi-purpose workspace page', length=1, group='zero_page', access='rw')

d.label(0x00A9, 'svc_state', description='Multi-purpose service state', length=1, group='zero_page', access='rw')

d.label(0x00AA, 'osword_flag', description='OSWORD param byte', length=1, group='zero_page', access='rw')

d.label(0x00AB, 'ws_ptr_lo', description='Workspace indirect pointer (lo)', length=1, group='zero_page', access='rw')

d.label(0x00AC, 'ws_ptr_hi', description='Workspace indirect pointer (hi)', length=1, group='zero_page', access='rw')

d.label(0x00AD, 'table_idx', description='OSBYTE/palette table index counter', length=1, group='zero_page', access='rw')

d.label(0x00AE, 'work_ae', description='Indexed workspace (multi-purpose scratch)', length=1, group='zero_page', access='rw')

d.label(0x00AF, 'addr_work', description='Address work byte for comparison (indexed)', length=1, group='zero_page', access='rw')

d.label(0x00B0, 'fs_load_addr', description='WORK: load/start address (4 bytes)', length=4, group='zero_page', access='rw')

d.label(0x00B1, 'fs_load_addr_hi', length=1, group='zero_page', access='rw')

d.label(0x00B2, 'fs_load_addr_2', length=1, group='zero_page', access='rw')

d.label(0x00B3, 'fs_load_addr_3', length=1, group='zero_page', access='rw')

d.label(0x00B4, 'fs_work_4', length=1, group='zero_page', access='rw')

d.label(0x00B5, 'fs_work_5', description='FS scratch byte 5. Multi-purpose: *Wipe iteration counter, parsed FS station number, spool drive number, etc.', length=1, group='zero_page', access='rw')

d.label(0x00B6, 'fs_work_6', description='FS scratch byte 6. Multi-purpose: *Wipe end-of-buffer offset, parsed FS network number, etc.', length=1, group='zero_page', access='rw')

d.label(0x00B7, 'fs_work_7', length=1, group='zero_page', access='rw')

d.label(0x00B8, 'fs_error_ptr', length=1, group='zero_page', access='rw')

d.label(0x00B9, 'fs_crflag', length=1, group='zero_page', access='rw')

d.label(0x00BA, 'fs_spool_handle', length=1, group='zero_page', access='rw')

d.label(0x00BB, 'fs_options', length=1, group='zero_page', access='rw')

d.label(0x00BC, 'fs_block_offset', length=1, group='zero_page', access='rw')

d.label(0x00BD, 'fs_last_byte_flag', length=1, group='zero_page', access='rw')

d.label(0x00BE, 'fs_crc_lo', length=1, group='zero_page', access='rw')

d.label(0x00BF, 'fs_crc_hi', length=1, group='zero_page', access='rw')

d.label(0x00CC, 'fs_ws_ptr', description='FS workspace page pointer (lo, always 0)', length=1, group='zero_page', access='rw')

d.label(0x00C0, 'txcb_ctrl', length=1, group='zero_page', access='rw')

d.label(0x00C1, 'txcb_port', length=1, group='zero_page', access='rw')

d.label(0x00C2, 'txcb_dest', length=1, group='zero_page', access='rw')

d.label(0x00C4, 'txcb_start', length=1, group='zero_page', access='rw')

d.label(0x00C7, 'txcb_pos', length=1, group='zero_page', access='rw')

d.label(0x00C8, 'txcb_end', length=1, group='zero_page', access='rw')

d.label(0x00CD, 'nfs_temp', length=1, group='zero_page', access='rw')

d.label(0x00CE, 'rom_svc_num', length=1, group='zero_page', access='rw')

d.label(0x00CF, 'fs_spool0', length=1, group='zero_page', access='rw')

d.label(0x00D0, 'vdu_status', description='VDU status register (OSBYTE &75)', length=1, group='zero_page', access='rw')

d.label(0x0000, 'zp_ptr_lo', length=1, group='zero_page', access='rw')

d.label(0x0001, 'zp_ptr_hi', length=1, group='zero_page', access='rw')

d.label(0x0002, 'zp_work_2', length=1, group='zero_page', access='rw')

d.label(0x0003, 'zp_work_3', length=1, group='zero_page', access='rw')

d.label(0x0010, 'zp_temp_10', length=1, group='zero_page', access='rw')

d.label(0x0011, 'zp_temp_11', length=1, group='zero_page', access='rw')

d.label(0x0012, 'tube_data_ptr', length=1, group='zero_page', access='rw')

d.label(0x0013, 'tube_data_ptr_hi', length=1, group='zero_page', access='rw')

d.label(0x0014, 'tube_claim_flag', length=1, group='zero_page', access='rw')

d.label(0x0015, 'tube_claimed_id', length=1, group='zero_page', access='rw')

d.label(0x0063, 'zp_0063', description='(false ref from inline string data)', length=1, group='zero_page', access='rw')

d.label(0x0078, 'zp_0078', description='(false ref from inline string data)', length=1, group='zero_page', access='rw')

d.label(0x00EF, 'osbyte_a_copy', length=1, group='zero_page', access='rw')

d.label(0x00F0, 'osword_pb_ptr', length=1, group='zero_page', access='rw')

d.label(0x00F1, 'osword_pb_ptr_hi', length=1, group='zero_page', access='rw')

d.label(0x00F3, 'os_text_ptr_hi', length=1, group='zero_page', access='rw')

d.label(0x00F7, 'osrdsc_ptr_hi', length=1, group='zero_page', access='rw')

d.label(0x00FD, 'brk_ptr', length=1, group='zero_page', access='rw')

d.label(0x00FF, 'escape_flag', length=1, group='zero_page', access='rw')

d.label(0x0D07, 'nmi_romsel', description="""ROM-bank number patched into the NMI shim.
The NMI handler runs in the active sideways slot, so the shim begins by paging in the NFS ROM bank (this byte) before dispatching to the body.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D0C, 'nmi_jmp_lo', description="""NMI dispatch JMP-target low byte.
Patched by [`set_nmi_vector`](address:0D0E) and [`install_nmi_handler`](address:0D11). The NMI shim does `JMP (nmi_jmp_lo)` to reach the current handler.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D0D, 'nmi_jmp_hi', description="""NMI dispatch JMP-target high byte.
Paired with [`nmi_jmp_lo`](address:0D0C). Only [`set_nmi_vector`](address:0D0E) writes this; [`install_nmi_handler`](address:0D11) leaves it alone (same-page optimisation).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D0E, 'set_nmi_vector', description="""NMI vector update (both bytes).
`STY` [nmi_jmp_hi](address:0D0D) then `STA` [nmi_jmp_lo](address:0D0C), writing the full 16-bit NMI handler address into the JMP-target slot. Falls through to [`nmi_rti`](address:0D14).""", length=3, group='ram_workspace', access='r')

d.label(0x0D11, 'install_nmi_handler', description="""NMI vector update (low byte only).
`STA` [nmi_jmp_lo](address:0D0C) only, leaving the existing high byte at [`nmi_jmp_hi`](address:0D0D) in place. Same-page optimisation used when the next handler is in the same page as the current one. Falls through to [`nmi_rti`](address:0D14).""", length=3, group='ram_workspace', access='r')

d.label(0x0D14, 'nmi_rti', description="""NMI exit shim.
Restores the previous ROM bank, pulls Y and A off the stack, reads `BIT econet_nmi_enable` (INTON, re-enables /NMI), and `RTI`s. Reached either as a fall-through from [`set_nmi_vector`](address:0D0E) / [`install_nmi_handler`](address:0D11), or as a direct branch from any NMI handler that has finished early.""", length=11, group='ram_workspace', access='r')

d.label(0x0D1A, 'imm_param_base')

d.label(0x0D1E, 'tx_addr_base')

d.label(0x0D20, 'tx_dst_stn', description='Destination station for next TX scout/ACK frame.', length=1, group='ram_workspace', access='rw')

d.label(0x0D21, 'tx_dst_net', description='Destination network for next TX scout/ACK frame.', length=1, group='ram_workspace', access='rw')

d.label(0x0D22, 'tx_src_stn', description="""Source-station byte (our station ID).
Set during init from [`econet_station_id`](address:FE18).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D23, 'tx_src_net', description='Source-network byte for outgoing scout/ACK frames (typically 0 for local network).', length=1, group='ram_workspace', access='rw')

d.label(0x0D24, 'tx_ctrl_byte', description='Control byte for next TX scout frame.', length=1, group='ram_workspace', access='rw')

d.label(0x0D25, 'tx_port', description='Destination port for next TX scout frame.', length=1, group='ram_workspace', access='rw')

d.label(0x0D26, 'tx_data_start', description='Start of TX data buffer (used by scout/data frame construction).', length=1, group='ram_workspace', access='rw')

d.label(0x0D2A, 'tx_data_len', description='Length of the TX data buffer payload, used during scout/data frame construction.', length=1, group='ram_workspace', access='rw')

d.label(0x0D2E, 'scout_buf', description="""Base of the 12-byte RX scout data buffer.
Holds the most recently received scout frame during reception and ACK transmission.""", length=12, group='ram_workspace', access='rw')

d.label(0x0D2F, 'scout_src_net', description='Scout source network byte ([`scout_buf`](address:0D2E)+1).', length=1, group='ram_workspace', access='rw')

d.label(0x0D30, 'scout_ctrl', description="""Scout control byte ([`scout_buf`](address:0D2E)+2).
Carries the immediate-op code (`&81`..`&88`) for port-0 scouts; checked by [`immediate_op`](address:8454).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D31, 'scout_port', description='Scout port byte ([`scout_buf`](address:0D2E)+3).', length=1, group='ram_workspace', access='rw')

d.label(0x0D32, 'scout_data', description="""Scout data payload base ([`scout_buf`](address:0D2E)+4).
Holds the 4-byte remote address for JSR / UserProc / OSProc immediate ops.""", length=8, group='ram_workspace', access='rw')

d.label(0x0D3D, 'rx_src_stn', description="""Source station of the received scout frame.
First address byte read by [`nmi_rx_scout`](address:809B) and validated against our station ID.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D3E, 'rx_src_net', description="""Source network of the received scout frame.
Read by [`nmi_rx_scout_net`](address:80B8); used for the local-network match (0 = local, &FF = broadcast).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D3F, 'rx_ctrl', description='Control byte of the received scout frame.', length=1, group='ram_workspace', access='rw')

d.label(0x0D40, 'rx_port', description="""Port byte of the received scout frame.
Matched against the open RXCB list to find a listener (or the immediate-op port range &80..&88).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D41, 'rx_remote_addr', description='Remote address byte for received TX setup.', length=1, group='ram_workspace', access='rw')

d.label(0x0D42, 'rx_extra_byte', description='Extra trailing RX data byte.', length=1, group='ram_workspace', access='rw')

d.label(0x0D43, 'saved_nmi_lo', description="""Saved next NMI handler address (low byte).
Written by [`ack_tx_write_dest`](address:82F8) from the (A=lo, Y=hi) pair on entry, then consumed when the next NMI fires.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D44, 'saved_nmi_hi', description="""Saved next NMI handler address (high byte).
Paired with [`saved_nmi_lo`](address:0D43).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D4A, 'tx_flags', description="""TX path control flags.
Bit 7: TX path is active (used by [`nmi_error_dispatch`](address:8215) to choose between RX-error reset and TX-fail dispatch).
Bit 0: handshake-data pending.
Bit 1: data-RX into Tube buffer (selected by [`install_data_rx_handler`](address:81F7)).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D4B, 'nmi_next_lo', description="""Next NMI handler address (low byte).
Saved by the scout / data-RX handler; consumed by [`ack_tx`](address:82DF) when installing the post-ACK NMI handler.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D4C, 'nmi_next_hi', description="""Next NMI handler address (high byte).
Paired with [`nmi_next_lo`](address:0D4B).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D4F, 'tx_index', description='Index into the TX buffer (current byte position).', length=1, group='ram_workspace', access='rw')

d.label(0x0D50, 'tx_length', description='Total length of the TX data payload.', length=1, group='ram_workspace', access='rw')

d.label(0x0D60, 'tx_complete_flag', description="""TX completion semaphore.
Bit 7 set by the NMI TX-completion handler; polled by `wait_net_tx_ack` to detect frame completion.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D61, 'econet_flags', description="""Econet control flags.
Bit 7: port-list active. Bit 2: halt requested.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D62, 'econet_init_flag', description="""Econet-initialised flag.
Bit 7 set when the NMI shim has been installed; checked at every NMI to reject pre-init interrupts.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D63, 'tube_present', description="""Tube co-processor presence flag.
Probed at init via OSBYTE `&EA`; read by every TX/RX path that needs to forward data through the Tube.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D64, 'ws_0d64', description='ANFS workspace byte (role TBD).', length=1, group='ram_workspace', access='rw')

d.label(0x0D65, 'tx_op_type', description="""Deferred-work / TX-operation type flag.
Set by NMI handlers to mark pending work; polled by [`svc5_irq_check`](address:8028) as the dispatch trigger.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D66, 'exec_addr_lo', description="""Remote execution address (low byte).
Stored by remote-JSR / immediate-op paths; consumed when the queued operation runs.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D67, 'exec_addr_hi', description="""Remote execution address (high byte).
Paired with [`exec_addr_lo`](address:0D66).""", length=1, group='ram_workspace', access='rw')

d.label(0x0D68, 'ws_0d68', description='ANFS workspace byte (role TBD).', length=1, group='ram_workspace', access='rw')

d.label(0x0D69, 'ws_0d69', description='ANFS workspace byte (role TBD).', length=1, group='ram_workspace', access='rw')

d.label(0x0D6A, 'ws_0d6a', description='ANFS workspace byte (role TBD).', length=1, group='ram_workspace', access='rw')

d.label(0x0D6B, 'spool_buf_idx', description='Spool / printer buffer write index.', length=1, group='ram_workspace', access='rw')

d.label(0x0D6C, 'fs_flags', description="""Filing-system status flags.
Bit 7: NFS is currently the selected FS; cleared when another FS takes over.""", length=1, group='ram_workspace', access='rw')

d.label(0x0D6D, 'tx_retry_count', description="""Transmit retry count (default `&FF` = 255).
Settable via OSWORD `&13` PB[1].""", length=1, group='ram_workspace', access='rw')

d.label(0x0D6E, 'rx_wait_timeout', description="""Receive wait timeout (default `&28` = 40).
Settable via OSWORD `&13` PB[2].""", length=1, group='ram_workspace', access='rw')

d.label(0x0D6F, 'peek_retry_count', description="""Machine peek retry count (default `&0A` = 10).
Settable via OSWORD `&13` PB[3].""", length=1, group='ram_workspace', access='rw')

d.label(0x0D72, 'bridge_status', description="""Bridge station number (`&FF` = no bridge).
Set by the bridge-discovery scout reply; checked before any cross-network operation.""", length=1, group='ram_workspace', access='rw')

d.label(0x0DE6, 'txcb_default_base')

d.label(0x0DF0, 'rom_ws_pages', description="MOS per-ROM workspace page table (16 bytes, one per sideways-ROM slot). Each entry is the high byte of the page allocated to that ROM's absolute workspace.", length=16, group='ram_workspace', access='r')

d.label(0x0DFA, 'fs_context_save')

d.label(0x0DFE, 'osword_ws_base')

d.label(0x0DFF, 'fs_server_base')

d.label(0x0E00, 'fs_server_stn')

d.label(0x0E01, 'fs_server_net')

d.label(0x0E02, 'fs_urd_handle')

d.label(0x0E03, 'fs_csd_handle')

d.label(0x0E04, 'fs_lib_handle')

d.label(0x0E05, 'fs_boot_option')

d.label(0x0E06, 'fs_messages_flag')

d.label(0x0E07, 'fs_eof_flags')

d.label(0x0E09, 'fs_last_error')

d.label(0x0E0A, 'fs_cmd_context')

d.label(0x0E0B, 'fs_context_hi')

d.label(0x0E16, 'fs_work_16')

d.label(0x0E2F, 'fs_filename_buf_m1')

d.label(0x0E30, 'fs_filename_buf')

d.label(0x0E31, 'fs_filename_buf_1')

d.label(0x0E32, 'fs_filename_buf_2')

d.label(0x0E38, 'fs_filename_backup')

d.label(0x0EF7, 'fs_reply_data')

d.label(0x0F00, 'txcb_reply_port')

d.label(0x0F01, 'fs_cmd_y_param')

d.label(0x0F02, 'fs_cmd_urd')

d.label(0x0F03, 'fs_cmd_csd', description='TXCB port byte / CSD (current selected directory) handle. Pre-HAZEL counterpart of [`hazel_txcb_network`](address:C103).', length=1, group='ram_workspace', access='rw')

d.label(0x0F04, 'fs_cmd_lib')

d.label(0x0F05, 'fs_cmd_data', description='TX buffer data start / FS reply data. Pre-HAZEL counterpart of [`hazel_txcb_data`](address:C105).', length=1, group='ram_workspace', access='rw')

d.label(0x0F06, 'fs_func_code')

d.label(0x0F07, 'fs_data_count')

d.label(0x0F08, 'fs_reply_cmd')

d.label(0x0F09, 'fs_load_vector')

d.label(0x0F0A, 'fs_handle_check')

d.label(0x0F0B, 'fs_load_upper')

d.label(0x0F0C, 'fs_addr_check')

d.label(0x0F0D, 'fs_file_len')

d.label(0x0F0E, 'fs_file_attrs')

d.label(0x0F10, 'fs_file_len_3')

d.label(0x0F11, 'fs_obj_type')

d.label(0x0F12, 'fs_access_level')

d.label(0x0F13, 'fs_reply_stn')

d.label(0x0F14, 'fs_len_clear')

d.label(0x0F16, 'fs_boot_data')

d.label(0x0F2F, 'fs_exam_attr_char')

d.label(0x0F30, 'fs_exam_dir_flag')

d.label(0x0FDC, 'fs_putb_buf')

d.label(0x0FDD, 'fs_getb_buf')

d.label(0x0FDE, 'fs_handle_mask')

d.label(0x0FDF, 'fs_error_flags')

d.label(0x0FE0, 'fcb_xfer_count_lo')

d.label(0x0FF0, 'fcb_xfer_count_mid')

d.label(0x1000, 'fcb_count_lo')

d.label(0x1010, 'fcb_attr_or_count_mid')

d.label(0x1020, 'fcb_station_or_count_hi')

d.label(0x1030, 'fcb_net_or_port')

d.label(0x1040, 'fcb_flags')

d.label(0x1050, 'fcb_net_num')

d.label(0x1060, 'chan_status')

d.label(0x1070, 'cur_dir_handle')

d.label(0x1071, 'fs_lib_flags')

d.label(0x1072, 'handle_1_fcb')

d.label(0x1073, 'handle_2_fcb')

d.label(0x1074, 'handle_3_fcb')

d.label(0x1078, 'fcb_stn_lo')

d.label(0x1088, 'fcb_stn_hi')

d.label(0x1098, 'fcb_buf_offset')

d.label(0x10A8, 'fcb_attr_ref')

d.label(0x10B8, 'fcb_status')

d.label(0x10C8, 'cur_fcb_index')

d.label(0x10C9, 'cur_chan_attr')

d.label(0x10CA, 'cur_attr_ref')

d.label(0x10CB, 'xfer_count_lo')

d.label(0x10CC, 'fcb_buf_page')

d.label(0x10CD, 'xfer_sentinel_1')

d.label(0x10CE, 'xfer_sentinel_2')

d.label(0x10CF, 'xfer_offset')

d.label(0x10D0, 'xfer_pass_count')

d.label(0x10D1, 'xfer_counter')

d.label(0x10D4, 'work_stn_lo')

d.label(0x10D5, 'work_stn_hi')

d.label(0x10D6, 'xfer_flag')

d.label(0x10D7, 'osbput_saved_byte')

d.label(0x10D8, 'quote_mode')

d.label(0x10D9, 'fcb_ctx_save')

d.label(0x10F3, 'filename_buf', description='Filename display buffer (12 bytes). Used by directory listing and *Info to format filenames.', length=12, group='ram_workspace', access='rw')

d.label(0x959A, 'print_fs_ps_help')

d.label(0x95CD, 'print_field_tail_s')

d.label(0x95E9, 'dispatch_fs_ps_with_arg')

d.label(0x965F, 'print_ps_address')

d.label(0x9670, 'print_fs_address')

d.label(0x967F, 'print_cmos_decimal_nl')

d.label(0x9689, 'print_cmos_done')

d.label(0x8001, 'rom_header_byte1')

d.label(0x8002, 'rom_header_byte2')

d.label(0x806C, 'econet_restore')

d.label(0x809A, 'adlc_init_done')

d.label(0x83D4, 'loop_count_rxcb_slot')
d.expr_label(0x83ED, 'imm_op_dispatch_lo-&81')

d.label(0x83FF, 'return_from_discard_reset')

d.label(0x84AE, 'jmp_send_data_rx_ack')

d.label(0x84BE, 'set_rx_buf_len_hi')
d.expr_label(0x84B8, 'tx_done_dispatch_lo-&83')
d.expr_label(0x85FD, 'tx_ctrl_dispatch_lo-&81')

d.label(0x853A, 'return_from_advance_buf')

d.label(0x85F8, 'reload_inactive_mask')

d.label(0x87C4, 'tx_check_tdra_ready')

d.label(0x87EF, 'check_tdra_status')

d.label(0x8924, 'check_tx_in_progress')

d.label(0x8A85, 'clear_workspace_byte')

d.label(0x8A8A, 'restore_rom_slot')

d.label(0x8A9A, 'set_adlc_absent')

d.label(0x8AA1, 'check_adlc_flag')

d.label(0x8AA9, 'dispatch_svc_with_state')

d.label(0x8AD0, 'dispatch_svc_index')

d.label(0x8AE1, 'restore_svc_state')

d.label(0x8AE7, 'restore_romsel_rts')

d.label(0x8B04, 'loop_scan_key_range')

d.label(0x8B11, 'clear_svc_and_ws')

d.label(0x8B22, 'return_from_save_text_ptr')

d.label(0x8B2F, 'loop_sum_rom_bytes')

d.label(0x8B60, 'done_rom_checksum')

d.label(0x8B65, 'loop_copy_fs_ctx')

d.label(0x8B78, 'loop_set_vectors')

d.label(0x8BA4, 'loop_copy_ws_page')

d.label(0x8BD2, 'print_table_newline')

d.label(0x8BD8, 'loop_next_entry')

d.label(0x8BE0, 'print_indent')

d.label(0x8BF4, 'loop_pad_spaces')

d.label(0x8C06, 'loop_print_syntax')

d.label(0x8C16, 'print_syntax_char')

d.label(0x8C1C, 'done_entry_newline')

d.label(0x8C25, 'done_print_table')

d.label(0x8C3A, 'loop_indent_spaces')

d.label(0x8C41, 'return_from_help_wrap')

d.label(0x8C64, 'svc_return_unclaimed')

d.label(0x8C67, 'check_help_topic')

d.label(0x8C71, 'match_help_topic')

d.label(0x8C74, 'loop_dispatch_help')

d.label(0x8C8C, 'skip_if_no_match')

d.label(0x8C96, 'version_string_cr')

d.label(0x8CC6, 'return_from_setup_ws_ptr')

d.label(0x8CD7, 'write_key_state')

d.label(0x8CDD, 'select_net_fs')

d.label(0x8D04, 'issue_svc_osbyte')

d.label(0x8D28, 'loop_match_credits')

d.label(0x8D33, 'done_credits_check')

d.label(0x8D39, 'loop_emit_credits')

d.label(0x8D44, 'return_from_credits_check')

d.label(0x8D45, 'credits_keyword_start')

d.label(0x8DA7, 'ps_template_base')

d.label(0x8DC0, 'skip_no_fs_addr')

d.label(0x8DC7, 'loop_copy_logon_cmd')

d.label(0x8DD8, 'scan_pass_prompt')

d.label(0x8DDA, 'loop_scan_colon')

d.label(0x8DEB, 'read_pw_char')

d.label(0x8DFD, 'loop_erase_pw')

d.label(0x8E04, 'check_pw_special')

d.label(0x8E13, 'send_pass_to_fs')

d.label(0x8E70, 'dispatch_rts')

d.label(0x8ECD, 'jmp_osbyte')

d.label(0x8EEF, 'return_from_raise_y_to_c8')

d.label(0x8EF8, 'done_cap_ws_count')

d.label(0x8F56, 'loop_zero_workspace')

d.label(0x8F84, 'loop_copy_init_data')

d.label(0x8FA9, 'loop_alloc_handles')

d.label(0x9066, 'loop_restore_ctx')

d.label(0x9083, 'loop_checksum_byte')

d.label(0x908D, 'loop_copy_to_ws')

d.label(0x9090, 'store_ws_byte')

d.label(0x909D, 'return_from_fs_shutdown')

d.label(0x90A6, 'loop_sum_ws')

d.label(0x90F4, 'done_print_newline')

d.label(0x90F8, 'cmd_syntax_strings')
d.banner(0x90F8, title='*HELP / *SYNTAX argument strings (8 messages)', description="""Eight zero-terminated argument-syntax strings used by the *HELP
text builder. Each string describes the argument shape of a
particular command group; their offsets within this table are
stored in [`cmd_syntax_table`](address:91ED), keyed by command
index. Read by [`do_print_no_spool`](address:921D) when no command
argument was supplied.""")

d.label(0x90F8, 'syn_opt_dir')

d.label(0x9100, 'syn_iam')

d.label(0x912D, 'syn_object')

d.label(0x9159, 'syn_dir')

d.label(0x9170, 'syn_password')

d.label(0x91AA, 'syn_access')

d.label(0x91C6, 'syn_rename')

d.label(0x91E0, 'syn_opt_stn')

d.label(0x91ED, 'cmd_syntax_table')
d.banner(0x91ED, title='Argument-syntax offset table (12 entries)', description="""Twelve byte offsets indexing into
[`syn_opt_dir`](address:90F8). Each entry is computed as
`<syn_X> - syn_opt_dir - 1` so the print loop can `INY`
before `LDA` and still land on the first byte of the chosen
string. The byte at &91F9 immediately after the table is the
entry point of [`print_no_spool`](address:91F9).""")
for i in range(12):
    d.byte(0x91ED + i)
d.expr(0x91ED, 'syn_iam - syn_opt_dir - 2')
d.expr(0x91EF, 'syn_iam - syn_opt_dir - 1')
d.expr(0x91F0, 'syn_object - syn_opt_dir - 1')
d.expr(0x91F6, 'syn_access - syn_opt_dir - 1')
d.expr(0x91F8, 'syn_opt_stn - syn_opt_dir - 1')

d.label(0x9203, 'save_regs_for_print_no_spool')

d.label(0x921D, 'do_print_no_spool')

d.label(0x9227, 'print_via_oswrch')

d.label(0x922A, 'restore_spool_and_return')

d.label(0x9769, 'always_set_v_byte')

d.label(0x9247, 'add_ascii_base')

d.label(0x9269, 'loop_next_char')

d.label(0x926F, 'load_char')

d.label(0x9287, 'resume_caller')

d.label(0x92BF, 'next_hex_char')

d.label(0x92CA, 'check_digit_range')

d.label(0x92DA, 'skip_if_not_hex')

d.label(0x92DC, 'extract_digit_value')

d.label(0x92F0, 'next_dec_char')

d.label(0x931C, 'done_parse_num')

d.label(0x9325, 'validate_station')

d.label(0x933B, 'return_parsed')

d.label(0x933D, 'handle_dot_sep')

d.label(0x9353, 'error_overflow')

d.label(0x936B, 'error_bad_number')

d.label(0x9377, 'error_bad_param')

d.label(0x9386, 'error_bad_net_num')

d.label(0x93A8, 'return_from_digit_test')

d.label(0x93A9, 'not_a_digit')

d.label(0x93B9, 'begin_prot_encode')

d.label(0x93BD, 'loop_encode_prot')

d.label(0x93C5, 'skip_clear_prot')


d.subroutine(0x93C8, 'prot_bit_encode_table', title='Bit-permutation table for protection / access encoding', description="""11-byte lookup table used by [`get_prot_bits`](address:93B5) and
[`get_access_bits`](address:93AB) to map source bits (the raw 5-bit
or 6-bit access mask read from the directory entry) into the FS
protocol's 8-bit protection-flag layout. The encoder loop at
[`begin_prot_encode`](address:93B9) shifts each source bit out via
`LSR`; whenever the bit is 1 it ORs the corresponding entry into
the result, then advances `X`.

Two callers partition the table:

- [`get_prot_bits`](address:93B5) enters at index 0 with 5 source
  bits (raw protection mask, `AND #&1F`).
- [`get_access_bits`](address:93AB) enters at index 5 with 6 source
  bits (directory access byte, `AND #&3F`).

| idx | caller            | src bit | mask  | output bits |
| --- | ----------------- | ------- | ----- | ----------- |
|   0 | `get_prot_bits`   |       0 | `&50` | 6, 4        |
|   1 | `get_prot_bits`   |       1 | `&20` | 5           |
|   2 | `get_prot_bits`   |       2 | `&05` | 2, 0        |
|   3 | `get_prot_bits`   |       3 | `&02` | 1           |
|   4 | `get_prot_bits`   |       4 | `&88` | 7, 3        |
|   5 | `get_access_bits` |       0 | `&04` | 2           |
|   6 | `get_access_bits` |       1 | `&08` | 3           |
|   7 | `get_access_bits` |       2 | `&80` | 7           |
|   8 | `get_access_bits` |       3 | `&10` | 4           |
|   9 | `get_access_bits` |       4 | `&01` | 0           |
|  10 | `get_access_bits` |       5 | `&02` | 1           |""")
for i in range(11):
    d.byte(0x93C8 + i)
d.comment(0x93C8, 'prot src bit 0 -> out bits 6,4', align=Align.INLINE)
d.comment(0x93C9, 'prot src bit 1 -> out bit 5', align=Align.INLINE)
d.comment(0x93CA, 'prot src bit 2 -> out bits 2,0', align=Align.INLINE)
d.comment(0x93CB, 'prot src bit 3 -> out bit 1', align=Align.INLINE)
d.comment(0x93CC, 'prot src bit 4 -> out bits 7,3', align=Align.INLINE)
d.comment(0x93CD, 'access src bit 0 -> out bit 2', align=Align.INLINE)
d.comment(0x93CE, 'access src bit 1 -> out bit 3', align=Align.INLINE)
d.comment(0x93CF, 'access src bit 2 -> out bit 7', align=Align.INLINE)
d.comment(0x93D0, 'access src bit 3 -> out bit 4', align=Align.INLINE)
d.comment(0x93D1, 'access src bit 4 -> out bit 0', align=Align.INLINE)
d.comment(0x93D2, 'access src bit 5 -> out bit 1', align=Align.INLINE)

d.label(0x93E8, 'loop_cmp_handle')

d.label(0x93F1, 'return_from_cmp_handle')

d.label(0x93F2, 'fscv_7_read_handles')

d.label(0x9464, 'loop_scan_flag')

d.label(0x946D, 'loop_copy_name')

d.label(0x9479, 'append_space')

d.label(0x9482, 'return_from_copy_cmd_name')

d.label(0x9489, 'loop_skip_spaces')

d.label(0x9492, 'check_open_quote')

d.label(0x949D, 'loop_copy_arg_char')

d.label(0x94AB, 'store_arg_char')

d.label(0x94D3, 'loop_copy_rename')

d.label(0x94DA, 'error_bad_rename')

d.label(0x94E6, 'store_rename_char')

d.label(0x94F3, 'skip_rename_spaces')

d.label(0x9523, 'setup_fs_root')

d.label(0x9525, 'loop_copy_fs_num')

d.label(0x953A, 'check_fs_dot')

d.label(0x9541, 'parse_fs_dot_dir')

d.label(0x9571, 'dir_found_send')

d.label(0x9597, 'dir_pass_simple')

d.label(0x974E, 'loop_init_txcb')

d.label(0x975E, 'skip_txcb_dest')

d.label(0x9763, 'txcb_init_template')
d.banner(0x9763, title='TXCB initialisation template (12 bytes)', description="""Copied byte-for-byte by [`init_txcb`](address:974B) into the
TXCB workspace at `&00C0`. The Nth template byte (at `&9763 + N`)
ends up at TXCB offset N (`&00C0 + N`).

Bytes 2 and 3 (placeholders `&00 &00` here) are overwritten
during the copy: while writing TXCB[0] and TXCB[1] the loop also
copies `hazel_fs_station[0..1]` (HAZEL `&C000..&C001`) into
`txcb_dest` (`&00C2..&00C3`), so the runtime destination station
and network come from the live FS state rather than this
template.

The `&FF` byte at offset 6 ([`always_set_v_byte`](address:9769))
serves double duty: it is part of this template AND a `BIT $abs`
target used by 22 callers to set V and N flags without clobbering
`A`.""")
for i in range(12):
    d.byte(0x9763 + i)

d.label(0x976A, 'bit_test_ff')

d.label(0x9791, 'txcb_copy_carry_clr')

d.label(0x9792, 'txcb_copy_carry_set')

d.label(0x9798, 'loop_copy_vset_stn')

d.label(0x97B0, 'use_lib_station')

d.label(0x97B6, 'done_vset_station')

d.label(0x97D5, 'loop_next_reply')

d.label(0x97DF, 'process_reply_code')

d.label(0x97E1, 'return_from_recv_reply')

d.label(0x97E2, 'handle_disconnect')

d.label(0x97EB, 'store_reply_status')

d.label(0x97F8, 'check_data_loss')

d.label(0x9800, 'loop_scan_channels')

d.label(0x9831, 'build_error_block')

d.label(0x983B, 'setup_error_copy')

d.label(0x983D, 'loop_copy_error')

d.label(0x9850, 'lang_1_remote_boot')

d.label(0x9856, 'done_commit_state')

d.label(0x9859, 'init_remote_session')

d.label(0x987E, 'lang_3_exec_0100')

d.label(0x989F, 'lang_4_validated')

d.label(0x98AF, 'lang_0_insert_key')

d.label(0x98CF, 'init_poll_counters')

d.label(0x98D5, 'loop_poll_tx')

d.label(0x98F6, 'done_poll_tx')

d.label(0x9908, 'return_from_cond_save_err')

d.label(0x9909, 'build_no_reply_error')

d.label(0x9919, 'loop_copy_no_reply_msg')

d.label(0x9925, 'done_no_reply_msg')

d.label(0x9938, 'skip_if_not_a')

d.label(0x9940, 'mask_error_class')

d.label(0x9957, 'loop_copy_station_msg')

d.label(0x9963, 'done_station_msg')

d.label(0x9975, 'suffix_not_listening')

d.label(0x9977, 'load_suffix_offset')

d.label(0x997B, 'loop_copy_suffix')

d.label(0x9987, 'done_suffix')

d.label(0x9989, 'build_simple_error')

d.label(0x9998, 'loop_copy_error_msg')

d.label(0x999E, 'check_msg_terminator')

d.label(0x99B3, 'loop_copy_bad_prefix')

d.label(0x99CC, 'write_error_num_and_str')

d.label(0x99D6, 'loop_copy_inline_str')

d.label(0x99E9, 'trigger_brk')

d.label(0x99EC, 'handle_net_error')

d.label(0x9A10, 'close_spool_exec')

d.label(0x9A19, 'done_close_files')

d.label(0x9A21, 'loop_copy_channel_msg')

d.label(0x9A2D, 'append_error_number')

d.label(0x9A54, 'append_station_num')

d.label(0x9A81, 'loop_count_digit')

d.label(0x9A91, 'store_digit')

d.label(0x9A99, 'return_from_store_digit')

d.label(0x9A9A, 'net_error_lookup_data')
d.banner(0x9A9A, title='Net-error class -> error_msg_table offset (12 bytes)', description="""Maps Econet network-error classes to byte offsets into
[`error_msg_table`](address:9AA6).

- Indices 0-7 are keyed by error class (the reply byte AND `7`).
- Index 8 is used by `build_no_reply_error` to locate the
  '`No reply from station`' message head.
- Indices 9-11 point to the suffix strings appended after the
  station address in compound errors ('` not listening`',
  '` on channel`', '` not present`').

Each byte is computed as `<message-label> - error_msg_table` so the
table reflows automatically if a message string is edited.""")
for i in range(12):
    d.byte(0x9A9A + i)
d.expr(0x9A9B, 'msg_net_error - error_msg_table')
d.expr(0x9A9C, 'msg_station - error_msg_table')
d.expr(0x9A9D, 'msg_no_clock - error_msg_table')
d.expr(0x9A9E, 'msg_escape - error_msg_table')
d.expr(0x9A9F, 'msg_escape - error_msg_table')
d.expr(0x9AA0, 'msg_escape - error_msg_table')
d.expr(0x9AA1, 'msg_bad_option - error_msg_table')
d.expr(0x9AA2, 'msg_no_reply - error_msg_table')
d.expr(0x9AA3, 'msg_not_listening - error_msg_table')
d.expr(0x9AA4, 'msg_on_channel - error_msg_table')
d.expr(0x9AA5, 'msg_not_present - error_msg_table')

d.label(0x9AA6, 'error_msg_table')
d.banner(0x9AA6, title='Net-error message strings', description="""Body of error-text fragments referenced by
[`net_error_lookup_data`](address:9A9A). Two layouts coexist:

1. **Error entries** (offsets 0..&3F) — one byte holding the BRK
   error code, immediately followed by the null-terminated
   message string:

   ```
   <err_code> <message-bytes...> &00
   ```

2. **Suffix entries** (offsets &56, &65, &71) — bare
   null-terminated strings appended to a built-up error message;
   no leading error-code byte.

Per-byte inline comments below name each error code and message;
the bytes from this table are read by `build_simple_error` and
`build_no_reply_error` when classifying a network reply.""")

d.label(0x9B33, 'set_timeout')

d.label(0x9B3C, 'start_tx_attempt')

d.label(0x9B52, 'loop_retry_tx')

d.label(0x9B58, 'loop_tx_delay')

d.label(0x9B60, 'try_alternate_phase')

d.label(0x9B6B, 'tx_send_error')

d.label(0x9B6F, 'tx_success')

d.label(0x9B75, 'pass_txbuf_init_table')
d.banner(0x9B75, title='Pass-through TX buffer template (12 bytes)', description="""Overlaid onto the TX control block by
[`setup_pass_txbuf`](address:9B89) for pass-through operations.
The 12 bytes follow the Econet TXCB layout used elsewhere in this
ROM (compare [`bridge_rxcb_init_data`](address:ABDD)):

| Offset | Field |
|---|---|
| 0     | TX control byte (`&88` = immediate TX)        |
| 1     | TX port (`&00` = immediate op)                |
| 2-3   | dest station / network (`&FD` skip = preserve)|
| 4-5   | buffer start address (lo, hi)                  |
| 6-7   | extended-address fill (`&FF&FF`)               |
| 8-9   | buffer end address (lo, hi)                    |
| 10-11 | extended-address fill (`&FF&FF`)               |

The buffer spans [`&0D3A`..`&0D3E`](address:0D3D) -- the bytes
immediately preceding [`rx_src_stn`](address:0D3D) through
[`rx_src_net`](address:0D3E) -- so the same RX-area bytes are
echoed back as the TX payload (hence "pass-through"). The
`&FF&FF` filler bytes at offsets 6-7 and 10-11 are a software
convention left over from a 4-byte-address format the BBC
Econet driver anticipated; for main-RAM buffers they're left
as `&FF&FF`. Original TX buffer values are pushed on the stack
and restored after transmission.""")
for i in range(12):
    d.byte(0x9B75 + i)

d.label(0x9B8B, 'loop_copy_template')

d.label(0x9B98, 'skip_template_byte')

d.label(0x9BA5, 'start_pass_tx')

d.label(0x9BB1, 'done_pass_retries')

d.label(0x9BC6, 'loop_poll_pass_tx')

d.label(0x9BCB, 'restore_retry_state')

d.label(0x9BD8, 'loop_pass_tx_delay')

d.label(0x9BE0, 'pass_tx_success')

d.label(0x9BE5, 'loop_restore_txbuf')

d.label(0x9BEF, 'skip_restore_byte')

d.label(0x9BF7, 'loop_copy_text_ptr')

d.label(0x9C08, 'loop_gsread_char')

d.label(0x9C13, 'terminate_buf')

d.label(0x9C39, 'copy_arg_and_enum')

d.label(0x9C56, 'copy_ws_then_fsopts')

d.label(0x9C5C, 'setup_txcb_addrs')

d.label(0x9C5E, 'loop_copy_addrs')

d.label(0x9C79, 'loop_copy_offsets')

d.label(0x9C8E, 'loop_swap_and_send')

d.label(0x9C90, 'loop_copy_start_end')

d.label(0x9CA4, 'loop_verify_addrs')

d.label(0x9CAF, 'return_from_txcb_swap')

d.label(0x9CB0, 'check_display_type')

d.label(0x9CB5, 'setup_dir_display')

d.label(0x9CBA, 'loop_compute_diffs')

d.label(0x9CD8, 'loop_copy_fs_options')

d.label(0x9CF9, 'send_info_request')

d.label(0x9D06, 'setup_txcb_transfer')

d.label(0x9D0C, 'recv_reply')

d.label(0x9D0F, 'store_result')

d.label(0x9D1C, 'loop_copy_file_info')

d.label(0x9D1F, 'store_prot_byte')

d.label(0x9D2D, 'loop_print_filename')

d.label(0x9D51, 'loop_print_hex_byte')

d.label(0x9D61, 'loop_copy_fsopts_byte')

d.label(0x9D70, 'return_from_advance_y')

d.label(0x9D74, 'loop_copy_ws_byte')

d.label(0x9D83, 'discard_handle_match')

d.label(0x9D8D, 'init_transfer_addrs')

d.label(0x9D98, 'loop_copy_addr_offset')

d.label(0x9DAA, 'loop_check_vs_limit')

d.label(0x9DB6, 'clamp_end_to_limit')

d.label(0x9DB8, 'loop_copy_limit')

d.label(0x9DBF, 'set_port_and_ctrl')

d.label(0x9DDC, 'dispatch_osword_op')

d.label(0x9DE8, 'dispatch_ops_1_to_6')

d.label(0x9E00, 'loop_copy_fsopts_4')

d.label(0x9E0D, 'setup_save_access')

d.label(0x9E17, 'loop_copy_fsopts_8')

d.label(0x9E22, 'send_save_or_access')

d.label(0x9E29, 'send_delete_request')

d.label(0x9E2E, 'send_request_vset')

d.label(0x9E34, 'skip_if_error')

d.label(0x9E39, 'setup_write_access')

d.label(0x9E43, 'read_cat_info')

d.label(0x9E65, 'loop_copy_cat_info')

d.label(0x9E72, 'loop_copy_ext_info')

d.label(0x9E7E, 'return_with_handle')

d.label(0x9E7F, 'done_osword_op')

d.label(0x9E89, 'loop_copy_cmdline_char')

d.label(0x9E95, 'pad_with_spaces')

d.label(0x9EA0, 'loop_copy_buf_char')

d.label(0x9EA2, 'copy_from_buf_entry')

d.label(0x9EBD, 'validate_chan_close')

d.label(0x9EC2, 'error_invalid_chan')

d.label(0x9EC5, 'check_chan_range')

d.label(0x9ED5, 'loop_copy_fcb_fields')

d.label(0x9EE5, 'dispatch_osfind_op')

d.label(0x9EF0, 'osfind_with_channel')

d.label(0x9F22, 'loop_copy_zp_to_buf')

d.label(0x9F38, 'done_return_flag')

d.label(0x9F3B, 'osargs_read_op')

d.label(0x9F4A, 'loop_copy_reply_to_zp')

d.label(0x9F57, 'osargs_ptr_dispatch')

d.label(0x9F79, 'osargs_write_ptr')

d.label(0x9F80, 'loop_copy_ptr_to_buf')

d.label(0x9FB1, 'close_all_fcbs')

d.label(0x9FC2, 'osfind_close_or_open')

d.label(0x9FCD, 'done_file_open')

d.label(0x9FCF, 'clear_result')

d.label(0x9FD1, 'shift_and_finalise')

d.label(0x9FD4, 'alloc_fcb_for_open')

d.label(0xA00B, 'loop_shift_filename')

d.label(0xA04C, 'check_open_mode')

d.label(0xA05E, 'alloc_fcb_with_flags')

d.label(0xA062, 'store_fcb_flags')

d.label(0xA068, 'done_osfind')

d.label(0xA06B, 'close_all_channels')

d.label(0xA084, 'close_specific_chan')

d.label(0xA08A, 'send_close_request')

d.label(0xA09C, 'done_close')

d.label(0xA09F, 'clear_single_fcb')

d.label(0xA0A9, 'fscv_0_opt_entry')

d.label(0xA0B3, 'osargs_dispatch')

d.label(0xA0B6, 'store_display_flag')

d.label(0xA0BB, 'error_osargs')

d.label(0xA0C0, 'send_osargs_request')

d.label(0xA10B, 'fscv_1_eof')

d.label(0xA126, 'mark_not_found')

d.label(0xA128, 'restore_and_return')

d.label(0xA136, 'loop_adjust_byte')

d.label(0xA142, 'subtract_ws_byte')

d.label(0xA145, 'store_adjusted_byte')

d.label(0xA15F, 'skip_if_out_of_range')

d.label(0xA162, 'valid_osgbpb_op')

d.label(0xA16D, 'load_chan_handle')

d.label(0xA1AC, 'set_write_active')

d.label(0xA1AF, 'setup_gbpb_request')

d.label(0xA205, 'loop_copy_opts_to_buf')

d.label(0xA210, 'skip_struct_hole')

d.label(0xA219, 'store_direction_flag')

d.label(0xA227, 'store_port_and_send')

d.label(0xA244, 'loop_setup_addr_bytes')

d.label(0xA25B, 'loop_copy_offset')

d.label(0xA26F, 'send_with_swap')

d.label(0xA272, 'recv_and_update')

d.label(0xA28A, 'send_osbput_data')

d.label(0xA29F, 'write_block_entry')

d.label(0xA2AD, 'store_station_result')

d.label(0xA2AF, 'loop_copy_opts_to_ws')

d.label(0xA2C1, 'handle_cat_update')

d.label(0xA2F5, 'loop_copy_to_host')

d.label(0xA302, 'tube_write_setup')

d.label(0xA30F, 'set_tube_addr')

d.label(0xA314, 'loop_write_to_tube')

d.label(0xA31D, 'loop_tube_delay')

d.label(0xA32C, 'update_cat_position')

d.label(0xA368, 'clear_buf_after_write')

d.label(0xA36A, 'loop_clear_buf')

d.label(0xA384, 'loop_check_remaining')

d.label(0xA38D, 'done_write_block')

d.label(0xA3B8, 'print_current_fs')

d.label(0xA3DA, 'store_station_lo')

d.label(0xA3E1, 'skip_if_no_station')

d.label(0xA3FF, 'net_1_read_handle')

d.label(0xA405, 'net_2_read_entry')

d.label(0xA410, 'return_zero_uninit')

d.label(0xA412, 'store_pb_result')

d.label(0xA415, 'net_3_close_handle')

d.label(0xA424, 'mark_ws_uninit')

d.label(0xA44E, 'dispatch_fs_cmd')

d.label(0xA45D, 'restart_table_scan')

d.label(0xA465, 'loop_match_char')

d.label(0xA474, 'skip_entry_chars')

d.label(0xA480, 'loop_skip_to_next')

d.label(0xA485, 'check_separator')

d.label(0xA48B, 'loop_check_sep_table')

d.label(0xA497, 'sep_table_data')

d.label(0xA4A2, 'loop_skip_trail_spaces')

d.label(0xA4A8, 'skip_dot_and_spaces')

d.label(0xA4AC, 'check_cmd_flags')

d.label(0xA4BD, 'clear_v_flag')

d.label(0xA4BE, 'clear_c_flag')

d.label(0xA4BF, 'return_with_result')

d.label(0xA4C3, 'loop_scan_past_word')

d.label(0xA4C4, 'check_char_type')

d.label(0xA4D2, 'skip_sep_spaces')

d.label(0xA4D9, 'set_c_and_return')

d.label(0xA4E4, 'fscv_2_star_run')

d.label(0xA4FF, 'open_file_for_run')

d.label(0xA517, 'loop_check_handles')

d.label(0xA51F, 'alloc_run_fcb')

d.label(0xA53B, 'done_run_dispatch')

d.label(0xA53E, 'try_library_path')

d.label(0xA552, 'loop_find_name_end')

d.label(0xA55A, 'loop_shift_name_right')

d.label(0xA565, 'loop_copy_lib_prefix')

d.label(0xA576, 'retry_with_library')

d.label(0xA578, 'restore_filename')

d.label(0xA57A, 'loop_restore_name')

d.label(0xA58F, 'library_tried')

d.label(0xA5AE, 'check_exec_addr')

d.label(0xA5B0, 'loop_check_exec_bytes')

d.label(0xA5C3, 'alloc_run_channel')

d.label(0xA5D7, 'library_dir_prefix')

d.label(0xA5E8, 'loop_read_gs_string')

d.label(0xA5EE, 'loop_skip_trailing')

d.label(0xA633, 'dispatch_via_vector')

d.label(0xA63E, 'fsreply_5_set_lib')

d.label(0xA647, 'loop_search_stn_bit2')

d.label(0xA65D, 'done_search_bit2')

d.label(0xA66B, 'set_flags_bit2')

d.label(0xA672, 'loop_search_stn_bit3')

d.label(0xA688, 'done_search_bit3')

d.label(0xA696, 'set_flags_bit3')

d.label(0xA6A9, 'loop_search_stn_boot')

d.label(0xA6BF, 'done_search_boot')

d.label(0xA6CD, 'set_flags_boot')

d.label(0xA6CF, 'store_stn_flags_restore')

d.label(0xA6D2, 'jmp_restore_fs_ctx')

d.label(0xA6D5, 'fsreply_1_boot')

d.label(0xA6E5, 'fsreply_2_copy_handles')

d.label(0xA726, 'check_auto_boot_flag')

d.label(0xA7C9, 'cmd_table_nfs_iam')

d.label(0xBEEB, 'loop_copy_osword_data')

d.label(0xA870, 'return_from_osword_setup')

d.label(0xA874, 'osword_0e_handler')

d.label(0xA890, 'return_from_osword_0e')

d.label(0xA891, 'save_txcb_and_convert')

d.label(0xA8DE, 'loop_copy_bcd_to_pb')

d.label(0xA908, 'loop_bcd_add')

d.label(0xA90E, 'done_bcd_convert')

d.label(0xA910, 'osword_10_handler')

d.label(0xA919, 'setup_ws_rx_ptrs')

d.label(0xA93D, 'loop_find_rx_slot')

d.label(0xA951, 'store_rx_slot_found')

d.label(0xA956, 'use_specified_slot')

d.label(0xA96C, 'loop_copy_slot_data')

d.label(0xA96D, 'copy_pb_and_mark')

d.label(0xA97A, 'increment_and_retry')

d.label(0xA97F, 'store_rx_result')

d.label(0xA981, 'osword_11_done')

d.label(0xA985, 'osword_12_handler')

d.label(0xA99A, 'osword_13_dispatch')

d.label(0xA9A7, 'return_from_osword_13')
d.entry(0xAA72)
d.entry(0xAA75)

d.label(0xA9A8, 'osword_13_dispatch_lo')
d.banner(0xA9A8, title='OSWORD &13 dispatch low-byte table (18 entries)', description="""Read by [`osword_13_dispatch`](address:A99A) as `LDA &A9A8,X`. Paired
with the high-byte half at [`osword_13_dispatch_hi`](address:A9BA).
Sub-codes 0..&11 cover read/set station, read/write workspace pair,
read/write protection, read/set handles, read RX flag/port/error,
read context, read/write CSD, read free buffers, read/write context
3, and bridge query.""")
for addr in range(0xA9A8, 0xA9BA):
    d.byte(addr)

d.label(0xA9BA, 'osword_13_dispatch_hi')
d.banner(0xA9BA, title='OSWORD &13 dispatch high-byte table (18 entries)', description="""Read by [`osword_13_dispatch`](address:A99A) as `LDA &A9BA,X`. The
dispatcher pushes the hi byte first then the lo, so RTS lands on
`target` (the table stores `target-1`).""")
for addr in range(0xA9BA, 0xA9CC):
    d.byte(addr)
_netv_dispatch_entries = [(0x00, 'dispatch_rts', 'no-op (RTS only)'), (0x01, 'netv_print_data', 'NETV reason 1: print data'), (0x02, 'netv_print_data', 'NETV reason 2: print data (alias)'), (0x03, 'netv_print_data', 'NETV reason 3: print data (alias)'), (0x04, 'osword_4_handler', 'NETV reason 4: OSWORD &04'), (0x05, 'netv_spool_check', 'NETV reason 5: spool check'), (0x06, 'dispatch_rts', 'no-op (RTS only)'), (0x07, 'netv_claim_release', 'NETV reason 7: claim/release'), (0x08, 'osword_8_handler', 'NETV reason 8: OSWORD &08')]

d.label(0xAD20, 'netv_dispatch_lo')
d.banner(0xAD20, title='NETV reason-code dispatch low-byte table (9 entries)', description="""Read by [`push_osword_handler_addr`](address:AD15) as
`LDA &AD20,X`. Paired with the high-byte half at
[`netv_dispatch_hi`](address:AD29). The wrapper at
[`netv_handler`](address:ACFC) reads the original A from the MOS
stack frame (`&0103,X` after TSX) and gates 9..&FF away to
[`return_6`](address:AD0E) before dispatching reasons 0..8.""")
for addr in range(0xAD20, 0xAD29):
    d.byte(addr)

d.label(0xAD29, 'netv_dispatch_hi')
d.banner(0xAD29, title='NETV reason-code dispatch high-byte table (9 entries)', description="""Read by [`push_osword_handler_addr`](address:AD15) as
`LDA &AD29,X`. The dispatcher pushes the hi byte first then the
lo, so RTS lands on `target` (the table stores `target-1`).""")
for addr in range(0xAD29, 0xAD32):
    d.byte(addr)
for idx, name, role in _netv_dispatch_entries:
    d.expr(0xAD20 + idx, '<(%s-1)' % name)
    d.expr(0xAD29 + idx, '>(%s-1)' % name)
    d.comment(0xAD20 + idx, 'reason &%02X: %s (%s)' % (idx, name, role), align=Align.INLINE)
    d.comment(0xAD29 + idx, 'reason &%02X: %s' % (idx, name), align=Align.INLINE)
_osword_13_entries = [(0x00, 'osword_13_read_station', 'read FS station'), (0x01, 'osword_13_set_station', 'set FS station'), (0x02, 'osword_13_read_ws_pair', 'read workspace pair'), (0x03, 'osword_13_write_ws_pair', 'write workspace pair'), (0x04, 'osword_13_read_prot', 'read protection mask'), (0x05, 'osword_13_write_prot', 'write protection mask'), (0x06, 'osword_13_read_handles', 'read transfer handles'), (0x07, 'osword_13_set_handles', 'set transfer handles'), (0x08, 'osword_13_read_rx_flag', 'read RX flag'), (0x09, 'osword_13_read_rx_port', 'read RX port'), (0x0A, 'osword_13_read_error', 'read last error'), (0x0B, 'osword_13_read_context', 'read context'), (0x0C, 'osword_13_read_csd', 'read CSD'), (0x0D, 'osword_13_write_csd', 'write CSD'), (0x0E, 'osword_13_read_free_bufs', 'read free buffers'), (0x0F, 'osword_13_read_ctx_3', 'read context byte 3'), (0x10, 'osword_13_write_ctx_3', 'write context byte 3'), (0x11, 'osword_13_bridge_query', 'bridge query')]
for idx, name, role in _osword_13_entries:
    d.expr(0xA9A8 + idx, '<(%s-1)' % name)
    d.expr(0xA9BA + idx, '>(%s-1)' % name)
    d.comment(0xA9A8 + idx, 'sub &%02X: %s (%s)' % (idx, name, role), align=Align.INLINE)
    d.comment(0xA9BA + idx, 'sub &%02X: %s' % (idx, name), align=Align.INLINE)

d.label(0xA9CF, 'read_station_bytes')

d.label(0xA9D1, 'loop_copy_station')

d.label(0xA9E4, 'loop_store_station')

d.label(0xA9FB, 'scan_fcb_entry')

d.label(0xAA2A, 'check_handle_2')

d.label(0xAA44, 'check_handle_3')

d.label(0xAA5E, 'store_updated_status')

d.label(0xAA62, 'next_fcb_entry')

d.label(0xAA76, 'setup_csd_copy')

d.label(0xAA88, 'copy_ws_byte_to_pb')

d.label(0xAAB1, 'return_from_write_ws_pair')

d.label(0xAAC7, 'loop_copy_handles')

d.label(0xAAD3, 'start_set_handles')

d.label(0xAAD5, 'validate_handle')

d.label(0xAAE5, 'handle_invalid')

d.label(0xAAEC, 'check_handle_alloc')

d.label(0xAB12, 'next_handle_slot')

d.label(0xAB19, 'assign_handle_2')

d.label(0xAB30, 'assign_handle_3')

d.label(0xAB47, 'loop_scan_fcb_flags')

d.label(0xAB59, 'no_flag_match')

d.label(0xAB5A, 'clear_flag_bits')

d.label(0xAB62, 'next_flag_entry')

d.label(0xAB82, 'store_a_to_pb_1')

d.label(0xABBB, 'bridge_found')

d.label(0xABC4, 'compare_bridge_status')

d.label(0xABCB, 'use_default_station')

d.label(0xABCE, 'store_bridge_station')

d.label(0xABD0, 'return_from_bridge_query')

d.label(0xABD1, 'bridge_txcb_init_table')

d.label(0xABDD, 'bridge_rxcb_init_data')
for i in range(4):
    d.byte(0xABD1 + i)

d.label(0xABF9, 'loop_copy_bridge_init')

d.label(0xAC0D, 'loop_wait_ws_status')

d.label(0xAC21, 'loop_wait_tx_done')

d.label(0xAC37, 'bridge_responded')

d.label(0xAC46, 'return_from_bridge_poll')

d.label(0xAC47, 'osword_14_handler')

d.label(0xAC55, 'loop_copy_txcb_init')

d.label(0xAC5D, 'store_txcb_init_byte')

d.label(0xAC85, 'loop_copy_ws_to_pb')

d.label(0xACB7, 'handle_tx_request')

d.label(0xACCE, 'loop_send_pb_chars')

d.label(0xACE4, 'loop_bridge_tx_delay')

d.label(0xACED, 'handle_burst_xfer')

d.label(0xAD0E, 'restore_regs_return')

d.label(0xAD64, 'netv_claim_release')

d.label(0xAD7D, 'process_match_result')

d.label(0xAD86, 'save_tube_state')

d.label(0xAD88, 'loop_save_tube_bytes')

d.label(0xAD9F, 'loop_poll_ws_status')

d.label(0xADAC, 'loop_restore_stack')

d.label(0xADB0, 'store_stack_byte')

d.label(0xADB7, 'return_from_claim_release')

d.label(0xADC0, 'return_from_match_rx_code')

d.label(0xADC1, 'osword_claim_codes')
d.banner(0xADC1, title='OSWORD per-claim-code lookup table (18 bytes)', description="""Looked up by [`match_rx_code`](address:ADB8) when an Econet RX
event triggers an OSWORD-related claim. The X register selects an
18-byte slice; bytes encode the claim type (immediate-op,
broadcast, port-specific) used by the dispatcher to decide which
handler chain to install. Per-byte inline comments document each
entry.""")
for i in range(18):
    d.byte(0xADC1 + i)

d.label(0xADDD, 'copy_pb_to_ws')

d.label(0xADE1, 'loop_copy_pb_to_ws')

d.label(0xAE0C, 'loop_copy_ws_template')

d.label(0xAE21, 'store_tx_ptr_hi')

d.label(0xAE23, 'select_store_target')

d.label(0xAE29, 'store_via_rx_ptr')

d.label(0xAE2B, 'advance_template_idx')

d.label(0xAE2F, 'done_ws_template_copy')

d.label(0xAE33, 'ws_txcb_template_data')
d.banner(0xAE33, title='Workspace TXCB template (39 bytes, three overlapping regions)', description="""Three overlapping copy regions indexed by different callers:

| Caller | X / Y / V | Range | Destination |
|---|---|---|---|
| Wide   | `X=&0D`, `Y=&7C`, `V=1` | bytes 0..13  | `ws+&6F..&7C` via `net_rx_ptr` |
| Narrow | `X=&1A`, `Y=&17`, `V=0` | bytes 14..26 | `ws+&0C..&17` via `nfs_workspace` |
| Vclr   | `X=&26`, `Y=&20`, `V=0` | bytes 27..38 | `ws+&15..&20` via `nfs_workspace` |

Per-byte inline comments below describe each entry's role in the
TXCB it ends up in.""")
for i in range(39):
    d.byte(0xAE33 + i)

d.label(0xAE5A, 'netv_spool_check')

d.label(0xAE6E, 'return_from_spool_reset')

d.label(0xAE6F, 'netv_print_data')

d.label(0xAE7E, 'loop_drain_printer_buf')

d.label(0xAEB5, 'done_spool_ctrl')

d.label(0xAEF7, 'check_spool_state')

d.label(0xAF06, 'start_spool_retry')

d.label(0xAF0B, 'loop_copy_spool_tx')

d.label(0xAF2A, 'loop_copy_spool_rx')

d.label(0xAF37, 'store_spool_rx_byte')

d.label(0xAF39, 'advance_spool_rx_idx')

d.label(0xAF60, 'spool_tx_succeeded')

d.label(0xAF75, 'spool_tx_retry')

d.label(0xAFB2, 'loop_scan_disconnect')

d.label(0xAFC1, 'verify_stn_match')

d.label(0xAFCC, 'send_disconnect_status')

d.label(0xAFE9, 'store_tx_ctrl_byte')

d.label(0xAFF1, 'loop_wait_disc_tx_ack')

d.label(0xB002, 'tx_econet_txcb_template')
d.banner(0xB002, title='Spool / disconnect TX control-block template (12 bytes)', description="""12-byte Econet TXCB initialisation template used by the spool /
disconnect TX paths. Copied into the workspace TXCB at offsets
`&21..&2C` via `(net_rx_ptr),Y`. Destination station and network
are filled in afterwards by the caller. Per-byte inline comments
identify each TXCB field.""")
for i in range(12):
    d.byte(0xB002 + i)

d.label(0xB00E, 'rx_palette_txcb_template')
d.banner(0xB00E, title='Palette-RX control-block template (12 bytes)', description="""12-byte template used by the *PS / palette-RX paths. Copied with
marker processing: `&FD` skips the destination byte (preserving
the existing field), `&FC` substitutes `net_rx_ptr_hi` (the
caller's RX-buffer page). Filled in over the workspace TXCB by
the broadcast-RX setup before the request is dispatched.""")
for i in range(12):
    d.byte(0xB00E + i)

d.label(0xB01A, 'lang_2_save_palette_vdu')

d.label(0xB031, 'loop_read_palette')

d.label(0xB0B1, 'parse_cdir_size')

d.label(0xB0BA, 'loop_find_alloc_size')

d.label(0xB0C0, 'done_cdir_size')
d.entry(0xB0A3)
for i in range(27):
    d.byte(0xB0D5 + i)

d.label(0xB107, 'ex_set_lib_flag')

d.label(0xB118, 'fscv_5_cat')

d.label(0xB121, 'cat_set_lib_flag')

d.label(0xB12E, 'setup_ex_request')

d.label(0xB14A, 'store_owner_flags')

d.label(0xB17B, 'print_public_label')

d.label(0xB1BF, 'print_dir_header')

d.label(0xB1E7, 'setup_ex_pagination')

d.label(0xB207, 'loop_scan_entry_data')

d.label(0xB227, 'jmp_osnewl')

d.label(0xB255, 'loop_shift_str_left')

d.label(0xB263, 'loop_trim_trailing')

d.label(0xB272, 'done_strip_prefix')

d.label(0xB274, 'return_from_strip_prefix')

d.label(0xB275, 'check_hash_prefix')

d.label(0xB279, 'error_bad_prefix')

d.label(0xB27C, 'check_colon_prefix')

d.label(0xB28B, 'set_fs_select_flag')

d.label(0xB298, 'option_str_offset_data')

d.label(0xB2A4, 'loop_copy_char')

d.label(0xB2B1, 'restore_after_check')

d.label(0xB2B3, 'advance_positions')

d.label(0xB2DD, 'loop_scan_entries')

d.label(0xB33F, 'loop_divide_digit')

d.label(0xB34F, 'print_nonzero_digit')

d.label(0xB37E, 'loop_advance_char')

d.label(0xB38B, 'loop_skip_space_chars')

d.label(0xB3B6, 'done_ps_available')

d.label(0xB3D9, 'loop_copy_ps_tmpl')

d.label(0xB3E3, 'no_ps_name_given')

d.label(0xB3E6, 'save_ps_cmd_ptr')

d.label(0xB3F0, 'loop_pad_ps_name')

d.label(0xB408, 'loop_read_ps_char')

d.label(0xB416, 'done_ps_name_parse')

d.label(0xB429, 'loop_pop_ps_slot')

d.label(0xB44F, 'done_ps_slot_mark')

d.label(0xB457, 'done_ps_scan')

d.label(0xB46C, 'print_ps_now')

d.label(0xB477, 'store_ps_station')

d.label(0xB498, 'print_server_is_suffix')

d.label(0xB4C6, 'loop_scan_ps_slots')

d.label(0xB4D6, 'skip_next_ps_slot')

d.label(0xB4DA, 'reinit_ps_slot')

d.label(0xB502, 'done_ps_slot_scan')

d.label(0xB511, 'loop_ps_delay')

d.label(0xB52D, 'loop_push_ps_name')

d.label(0xB537, 'loop_pop_ps_name')

d.label(0xB549, 'loop_copy_tx_hdr')

d.label(0xB552, 'ps_tx_header_template')
d.banner(0xB552, title='Printer-server TX header template (4 bytes)', description="""Four bytes copied to the head of the printer-server transmit
buffer by [`reverse_ps_name_to_tx`](address:B52B): control byte
`&80` (immediate-TX request), port `&D1` (printer block port),
function-code stub, and reply-port byte. Filled-in destination
fields follow from the caller's PS slot.""")
for i in range(4):
    d.byte(0xB552 + i)

d.label(0xB566, 'skip_if_local_net')

d.label(0xB575, 'ps_slot_txcb_template')
d.banner(0xB575, title='Printer-server slot TXCB template (12 bytes)', description="""12-byte Econet TXCB template for printer-server slot buffers.
Copied by [`init_ps_slot_from_rx`](address:B6A6) into workspace
offsets `&78`-`&83` via indexed addressing from
`write_ps_slot_link_addr` (`write_ps_slot_hi_link+1`). Substitutes
`net_rx_ptr_hi` at offsets `&7D` and `&81` (the hi bytes of the
two buffer pointers) so they point into the current RX buffer
page.

Structure: 4-byte header (control, port, station, network)
followed by two 4-byte buffer descriptors (lo address, hi page,
end lo, end hi). End bytes `&FF` are placeholders filled in later
by the caller.""")
for i in range(12):
    d.byte(0xB575 + i)

d.label(0xB5C3, 'no_poll_name_given')

d.label(0xB5C6, 'skip_if_no_poll_arg')

d.label(0xB5CE, 'loop_pad_poll_name')

d.label(0xB5E6, 'loop_read_poll_char')

d.label(0xB5F4, 'done_poll_name_parse')

d.label(0xB611, 'loop_print_poll_name')

d.label(0xB61F, 'done_poll_name_print')

d.label(0xB65A, 'check_poll_jammed')

d.label(0xB65E, 'print_poll_jammed')

d.label(0xB66A, 'check_poll_busy')

d.label(0xB69A, 'done_poll_status_line')

d.label(0xB69D, 'done_poll_slot_mark')

d.label(0xB6A8, 'loop_copy_slot_tmpl')

d.label(0xB6B3, 'subst_rx_page_byte')

d.label(0xB6B5, 'store_slot_tmpl_byte')

d.label(0xB6CB, 'done_uppercase_store')

d.label(0xB6EE, 'loop_match_prot_attr')

d.label(0xB703, 'request_next_wipe')

d.label(0xB736, 'check_wipe_attr')

d.label(0xB739, 'loop_check_if_locked')

d.label(0xB73D, 'skip_wipe_locked')

d.label(0xB742, 'check_wipe_dir')

d.label(0xB74B, 'show_wipe_prompt')

d.label(0xB74F, 'loop_copy_wipe_name')

d.label(0xB773, 'loop_print_wipe_info')

d.label(0xB787, 'check_wipe_response')

d.label(0xB799, 'loop_build_wipe_cmd')

d.label(0xB7A2, 'skip_if_not_space')

d.label(0xB7A6, 'set_wipe_cr_end')

d.label(0xB7A8, 'store_wipe_tx_char')

d.label(0xB7B7, 'skip_wipe_to_next')

d.label(0xB7BD, 'use_wipe_leaf_name')

d.label(0xB7BE, 'loop_copy_wipe_leaf')

d.label(0xB7E6, 'loop_clear_chan_table')

d.label(0xB7F6, 'loop_mark_chan_avail')

d.label(0xB80F, 'error_chan_out_of_range')

d.label(0xB811, 'return_chan_index')

d.label(0xB81D, 'error_chan_not_found')

d.label(0xB85B, 'error_chan_not_here')

d.label(0xB866, 'loop_copy_chan_err_str')

d.label(0xB879, 'loop_append_err_suffix')

d.label(0xB8AB, 'loop_scan_fcb_slots')

d.label(0xB8B9, 'done_found_free_slot')

d.label(0xB8F6, 'return_alloc_success')

d.label(0xB8F9, 'skip_set_carry')

d.label(0xB8FE, 'loop_scan_fcb_down')

d.label(0xB902, 'skip_if_slots_done')

d.label(0xB916, 'done_check_station')

d.label(0xB93A, 'loop_find_fcb')

d.label(0xB941, 'skip_if_no_wrap')

d.label(0xB94B, 'done_check_fcb_status')

d.label(0xB955, 'done_select_fcb')

d.label(0xB956, 'loop_scan_empty_fcb')

d.label(0xB95D, 'done_test_empty_slot')

d.label(0xB96C, 'skip_if_modified_fcb')

d.label(0xB989, 'loop_clear_counters')

d.label(0xB9DA, 'done_restore_offset')

d.label(0xBA00, 'done_clear_fcb_active')

d.label(0xBA0B, 'loop_save_tx_context')

d.label(0xBA1E, 'done_save_context')

d.label(0xBA21, 'loop_find_pending_fcb')

d.label(0xBA65, 'done_init_wipe')

d.label(0xBA89, 'done_calc_offset')

d.label(0xBAA8, 'loop_clear_buffer')

d.label(0xBAAD, 'done_set_fcb_active')

d.label(0xBAB7, 'loop_restore_workspace')

d.label(0xBAC2, 'loop_restore_tx_buf')

d.label(0xBACC, 'loop_save_before_match')

d.label(0xBAD1, 'loop_reload_attr')

d.label(0xBAD4, 'loop_next_fcb_slot')

d.label(0xBAEE, 'done_test_fcb_active')

d.label(0xBB27, 'return_test_offset')

d.label(0xBB48, 'loop_process_fcb')

d.label(0xBB53, 'done_flush_fcb')

d.label(0xBB58, 'done_advance_fcb')

d.label(0xBB87, 'done_read_fcb_byte')

d.label(0xBBB1, 'error_end_of_file')

d.label(0xBBC2, 'done_load_from_buf')

d.label(0xBC14, 'done_test_write_flag')

d.label(0xBC22, 'done_find_write_fcb')

d.label(0xBC32, 'done_check_buf_offset')

d.label(0xBC46, 'done_set_dirty_flag')

d.label(0xBC65, 'done_inc_byte_count')

d.label(0xBCEF, 'loop_copy_wipe_err_msg')

d.label(0xBCFC, 'done_terminate_wipe_err')

d.label(0xBD05, 'done_toggle_station')

d.label(0x83E5, 'discard_reset_rx')

d.label(0x83E8, 'reset_adlc_rx_listen')

d.label(0x83EB, 'set_nmi_rx_scout')

d.label(0x8512, 'setup_sr_tx')

d.label(0x8549, 'tx_done_econet_event')

d.label(0x8551, 'tx_done_fire_event')

d.label(0x8B00, 'scan_remote_keys')

d.label(0x8B18, 'save_text_ptr')

d.label(0x8BBB, 'help_print_nfs_cmds')

d.label(0x8BC6, 'print_cmd_table')

d.label(0x8BD5, 'print_cmd_table_loop')

d.label(0x8C29, 'help_wrap_if_serial')

d.label(0x8C93, 'print_version_header')

d.label(0x8CBD, 'setup_ws_ptr')

d.label(0x8CFD, 'notify_new_fs')

d.label(0x8CFF, 'call_fscv')

d.label(0x8D02, 'issue_svc_15')

d.label(0x8E21, 'clear_if_station_match')

d.label(0x8E2C, 'return_from_station_match')

d.label(0x8E38, 'pass_send_cmd')

d.label(0x8E3C, 'send_cmd_and_dispatch')

d.label(0x8E5B, 'dir_op_dispatch')

d.label(0x8E6A, 'push_dispatch_lo')

d.label(0x8EF0, 'store_ws_page_count')

d.label(0x903C, 'init_adlc_and_vectors')

d.label(0x904F, 'write_vector_entry')

d.label(0x9064, 'restore_fs_context')

d.label(0x9071, 'fscv_6_shutdown')

d.label(0x909E, 'verify_ws_checksum')

d.label(0x90B5, 'error_net_checksum')

d.label(0x9236, 'print_hex_byte')

d.label(0x923F, 'print_hex_nybble')

d.label(0x934A, 'err_bad_hex')

d.label(0x9357, 'err_bad_station_num')

d.label(0x939A, 'is_decimal_digit')

d.label(0x93A2, 'is_dec_digit_only')

d.label(0x93AB, 'get_access_bits')

d.label(0x93B5, 'get_prot_bits')

d.label(0x93D3, 'set_text_and_xfer_ptr')

d.label(0x93D7, 'set_xfer_params')

d.label(0x93DD, 'set_options_ptr')

d.label(0x93E1, 'clear_escapable')

d.label(0x93E6, 'cmp_5byte_handle')

d.label(0x93F7, 'set_conn_active')

d.label(0x940D, 'clear_conn_active')

d.label(0x9437, 'error_bad_filename')

d.label(0x9446, 'check_not_ampersand')

d.label(0x944E, 'read_filename_char')

d.label(0x945E, 'send_fs_request')

d.label(0x9483, 'parse_quoted_arg')

d.label(0x973D, 'init_txcb_bye')

d.label(0x973F, 'init_txcb_port')

d.label(0x974B, 'init_txcb')

d.label(0x976F, 'send_request_nowrite')

d.label(0x9773, 'send_request_write')

d.label(0x978A, 'save_net_tx_cb')

d.label(0x978B, 'save_net_tx_cb_vset')

d.label(0x97B7, 'prep_send_tx_cb')

d.label(0x97CD, 'recv_and_process_reply')

d.label(0x98BE, 'wait_net_tx_ack')

d.label(0x9900, 'cond_save_error_code')

d.label(0x9930, 'fixup_reply_status_a')

d.label(0x993B, 'load_reply_and_classify')

d.label(0x993D, 'classify_reply_error')

d.label(0x99A2, 'bad_str_anchor')

d.label(0x99DF, 'check_net_error_code')

d.label(0x9A3A, 'append_drv_dot_num')

d.label(0x9A5E, 'append_space_and_num')

d.label(0x9A69, 'append_decimal_num')

d.label(0x9A7A, 'append_decimal_digit')

d.label(0x9B24, 'init_tx_ptr_and_send')

d.label(0x9B2C, 'send_net_packet')

d.label(0x9B81, 'init_tx_ptr_for_pass')

d.label(0x9B89, 'setup_pass_txbuf')

d.label(0x9BF5, 'load_text_ptr_and_parse')

d.label(0x9C00, 'gsread_to_buf')

d.label(0x9C3E, 'do_fs_cmd_iteration')

d.label(0x9C85, 'send_txcb_swap_addrs')

d.label(0x9D44, 'print_load_exec_addrs')

d.label(0x9D4F, 'print_5_hex_bytes')

d.label(0x9D5F, 'copy_fsopts_to_zp')

d.label(0x9D6B, 'skip_one_and_advance5')

d.label(0x9D6C, 'advance_y_by_4')

d.label(0x9D71, 'copy_workspace_to_fsopts')

d.label(0x9D7E, 'retreat_y_by_4')

d.label(0x9D7F, 'retreat_y_by_3')

d.label(0x9D87, 'check_and_setup_txcb')

d.label(0x9E82, 'format_filename_field')

d.label(0x9FB4, 'return_with_last_flag')

d.label(0x9FB6, 'finalise_and_return')

d.label(0xA12C, 'update_addr_from_offset9')

d.label(0xA131, 'update_addr_from_offset1')

d.label(0xA133, 'add_workspace_to_fsopts')

d.label(0xA134, 'adjust_fsopts_4bytes')

d.label(0xA1EF, 'lookup_cat_entry_0')

d.label(0xA1F3, 'lookup_cat_slot_data')

d.label(0xA1FA, 'setup_transfer_workspace')

d.label(0xA2ED, 'write_data_block')

d.label(0xA329, 'tail_update_catalogue')

d.label(0xA390, 'tube_claim_c3')

d.label(0xA3BB, 'print_fs_info_newline')

d.label(0xA3E7, 'get_pb_ptr_as_index')

d.label(0xA3E9, 'byte_to_2bit_index')

d.label(0xA3FE, 'return_from_2bit_index')

d.label(0xA42F, 'fscv_3_star_cmd')

d.label(0xA440, 'cmd_fs_reentry')

d.label(0xA442, 'error_syntax')

d.label(0xA45B, 'match_fs_cmd')

d.label(0xA638, 'fsreply_3_set_csd')

d.label(0xA644, 'find_station_bit2')

d.label(0xA66F, 'find_station_bit3')

d.label(0xA6A6, 'flip_set_station_boot')

d.label(0xA764, 'boot_cmd_oscli')

d.label(0xA864, 'osword_setup_handler')

d.label(0xA901, 'bin_to_bcd')

d.label(0xAC67, 'store_osword_pb_ptr')

d.label(0xACAD, 'store_ptr_at_ws_y')

d.label(0xABE9, 'init_bridge_poll')

d.label(0xACF8, 'enable_irq_and_poll')

d.label(0xAD15, 'push_osword_handler_addr')

d.label(0xAD40, 'tx_econet_abort')

d.label(0xADFE, 'init_ws_copy_wide')

d.label(0xAE07, 'init_ws_copy_narrow')

d.label(0xAE0B, 'ws_copy_vclr_entry')

d.label(0xAE64, 'reset_spool_buf_state')

d.label(0xAE94, 'append_byte_to_rxbuf')

d.label(0xAE9D, 'handle_spool_ctrl_byte')

d.label(0xAF80, 'err_printer_busy')

d.label(0xAFA6, 'send_disconnect_reply')

d.label(0xB05F, 'commit_state_byte')

d.label(0xB066, 'serialise_palette_entry')

d.label(0xB081, 'read_osbyte_to_ws_x0')

d.label(0xB083, 'read_osbyte_to_ws')

d.label(0xB0D2, 'cdir_dispatch_col')

d.label(0xB21A, 'print_10_chars')

d.label(0xB22A, 'parse_cmd_arg_y0')

d.label(0xB22C, 'parse_filename_arg')

d.label(0xB22F, 'parse_access_prefix')

d.label(0xB251, 'strip_token_prefix')

d.label(0xB29F, 'copy_arg_to_buf_x0')

d.label(0xB2A1, 'copy_arg_to_buf')

d.label(0xB2A3, 'copy_arg_validated')

d.label(0xB2CA, 'return_from_copy_arg')

d.label(0xB2E4, 'ex_print_col_sep')

d.label(0xB327, 'print_num_no_leading')

d.label(0xB32A, 'print_decimal_3dig')

d.label(0xB338, 'print_decimal_digit')

d.label(0xB356, 'return_from_print_digit')

d.label(0xB373, 'save_ptr_to_os_text')

d.label(0xB37F, 'skip_to_next_arg')

d.label(0xB392, 'return_from_skip_arg')

d.label(0xB393, 'save_ptr_to_spool_buf')

d.label(0xB39E, 'init_spool_drive')

d.label(0xB3D5, 'copy_ps_data_y1c')

d.label(0xB3D7, 'copy_ps_data')

d.label(0xB483, 'print_file_server_is')

d.label(0xB48D, 'print_printer_server_is')

d.label(0xB4A8, 'load_ps_server_addr')

d.label(0xB4B4, 'pop_requeue_ps_scan')

d.label(0xB4FC, 'write_ps_slot_hi_link')

d.label(0xB51C, 'write_ps_slot_byte_ff')

d.label(0xB523, 'write_two_bytes_inc_y')

d.label(0xB52B, 'reverse_ps_name_to_tx')

d.label(0xB556, 'print_station_addr')

d.label(0xB6A5, 'return_from_poll_slots')

d.label(0xB6A6, 'init_ps_slot_from_rx')

d.label(0xB6BD, 'store_char_uppercase')

d.label(0xB7D3, 'flush_and_read_char')

d.label(0xB7E3, 'init_channel_table')

d.label(0xB805, 'attr_to_chan_index')

d.label(0xB814, 'check_chan_char')

d.label(0xB81C, 'err_net_chan_invalid')

d.label(0xB81F, 'err_net_chan_not_found')

d.label(0xB847, 'lookup_chan_by_char')

d.label(0xB886, 'store_result_check_dir')

d.label(0xB88C, 'check_not_dir')

d.label(0xB8A8, 'alloc_fcb_slot')

d.label(0xB8DC, 'alloc_fcb_or_error')

d.label(0xB8F8, 'close_all_net_chans')

d.label(0xB8FC, 'scan_fcb_flags')

d.label(0xB925, 'match_station_net')

d.label(0xB933, 'return_from_match_stn')

d.label(0xB934, 'find_open_fcb')

d.label(0xB977, 'init_wipe_counters')

d.label(0xB99A, 'start_wipe_pass')

d.label(0xBA09, 'save_fcb_context')

d.label(0xBAC0, 'restore_catalog_entry')

d.label(0xBACF, 'find_matching_fcb')

d.label(0xBB2A, 'inc_fcb_byte_count')

d.label(0xBB37, 'return_from_inc_fcb_count')

d.label(0xBCBC, 'send_wipe_request')

d.label(0xBD15, 'send_and_receive')

d.label(0xBD25, 'abort_if_escape')

d.label(0xBD2A, 'error_escape_pressed')

d.label(0xBD48, 'loop_push_zero_buf')

d.label(0xBD59, 'loop_dump_line')

d.label(0xBD60, 'loop_read_dump_byte')

d.label(0xBD72, 'done_check_dump_eof')

d.label(0xBD79, 'loop_pop_stack_buf')

d.label(0xBD80, 'done_check_boundary')

d.label(0xBD8B, 'done_start_dump_addr')

d.label(0xBD8D, 'loop_print_addr_byte')

d.label(0xBD9E, 'loop_inc_dump_addr')

d.label(0xBDB6, 'loop_print_dump_hex')

d.label(0xBDBB, 'loop_next_dump_col')

d.label(0xBDCF, 'done_print_separator')

d.label(0xBDDA, 'loop_print_dump_ascii')

d.label(0xBDE2, 'skip_non_printable')

d.label(0xBDE4, 'done_test_del')

d.label(0xBDF3, 'done_end_dump_line')

d.label(0xBDFC, 'done_dump_eof')

d.label(0xBE01, 'print_dump_header')

d.label(0xBE37, 'print_hex_and_space')

d.label(0xBF71, 'close_ws_file')

d.label(0xBF78, 'open_file_for_read')

d.label(0xBE40, 'done_print_hex_space')

d.label(0xBFA6, 'loop_skip_filename')

d.label(0xBFB1, 'loop_skip_fn_spaces')

d.label(0xBE42, 'parse_dump_range')

d.label(0xBE47, 'loop_clear_hex_accum')

d.label(0xBE4E, 'loop_parse_hex_digit')

d.label(0xBE6D, 'done_mask_hex_digit')

d.label(0xBE74, 'loop_shift_nibble')

d.label(0xBE77, 'loop_rotate_hex_accum')

d.label(0xBE98, 'error_hex_overflow')

d.label(0xBE9C, 'error_bad_hex_value')

d.label(0xBEA2, 'loop_skip_hex_spaces')

d.label(0xBEA3, 'done_test_hex_space')

d.label(0xBEAB, 'init_dump_buffer')

d.label(0xBEC4, 'loop_cmp_file_length')

d.label(0xBED0, 'done_check_outside')

d.label(0xBED6, 'error_outside_file')

d.label(0xBEEB, 'loop_copy_start_addr')

d.label(0xBEF0, 'done_advance_start')

d.label(0xBF08, 'loop_copy_osfile_ptr')

d.label(0xBF1B, 'loop_shift_osfile_data')

d.label(0xBF2A, 'loop_check_ff_addr')

d.label(0xBF37, 'loop_zero_load_addr')

d.label(0xBF3E, 'done_parse_disp_base')

d.label(0xBF53, 'done_add_disp_base')

d.label(0xBF58, 'loop_add_disp_bytes')

d.label(0xBF68, 'loop_store_disp_addr')

d.label(0xBFBA, 'advance_x_by_8')

d.label(0xBFBD, 'advance_x_by_4')

d.label(0xBFC0, 'inx4')
d.entry(0x8028)


d.subroutine(0x8028, 'svc5_irq_check', title='Service 5: unrecognised interrupt (Master 128 dispatch)', description="""Reads the deferred-work flag at `&0D65`; if zero, returns early via
`PLX`/`PLY`/`RTS`. Otherwise clears bit 7 of the Master 128 `ACCCON`
register at `&FE34` (`TRB`), zeros `&0D65`, then dispatches one of
two ways depending on bit 7 of the saved `Y`:

| Caller `Y` bit 7 | Action |
|---|---|
| Set | Dispatch via the `PHA`/`PHA`/`RTS` table at [`dispatch_svc5`](address:8048) |
| Clear | Fire Econet RX event `&FE` via [`generate_event`](address:8045), then `JMP` to [`tx_done_exit`](address:8582) |""", on_entry={'a': '5 (service call number)', 'x': 'ROM slot', 'y': 'parameter (high bit selects dispatch path)'})


d.subroutine(0x8045, 'generate_event', title='Generate event via EVNTV', description="""Single-instruction `JMP (evntv)` that hands control to whatever
handler is hooked into the MOS event vector. Called via service
call &05 (`svc5_irq_check`) on a 'transmit complete' or 'receive
complete' edge so user/MOS code can react to network events.""", on_entry={'A': 'event number'}, on_exit={'A': 'preserved', 'X': 'preserved', 'Y': 'preserved'})


d.subroutine(0x8048, 'dispatch_svc5', title='Service-5 PHA/PHA/RTS dispatch tail', description="""Builds an `RTS`-target on the stack from the
[`tx_done_dispatch_lo`](address:84B8) low-byte table and a hard-
coded high byte of `&85`, then falls through into the shared
[`svc_5_unknown_irq`](address:804F) `RTS` to land on the matching
[`tx_done_dispatch_lo`](address:84B8)+`Y` page-`&85` handler.""", on_entry={'y': 'tx_done_dispatch_lo offset (post-&83 base bias)'})


d.subroutine(0x804F, 'svc_5_unknown_irq', title='Service-5 unknown-IRQ tail (PHA/PHA/RTS landing)', description="""Bare `RTS` reused as the final step of every
[`dispatch_svc5`](address:8048) entry. With the target's
high/low bytes already pushed by the caller, `RTS` jumps to the
selected handler. Also reached as the unclaimed-IRQ tail of the
service-5 prologue when no ANFS handler matches.""")


d.subroutine(0x8A54, 'service_handler', title='Service call dispatch (Master 128)', description="""Handles service calls 1, 4, 8, 9, 13, 14, and 15.

| Call | Meaning                          |
|-----:|----------------------------------|
|    1 | Absolute workspace claim         |
|    4 | Unrecognised `*` command         |
|    8 | Unrecognised OSWORD              |
|    9 | `*HELP`                          |
|   13 | ROM initialisation               |
|   14 | ROM initialisation complete      |
|   15 | Vectors claimed                  |

On service 15 the ROM verifies the host OS via OSBYTE 0 with the
input `X=1`, which returns the OS version code:

| OSBYTE 1 value | Host                                |
|---------------:|-------------------------------------|
|              0 | OS 1.00 (early BBC B or Electron)   |
|              1 | OS 1.20 or American OS              |
|              2 | OS 2.00 (BBC B+)                    |
|              3 | OS 3.2 / 3.5 (Master 128)           |
|              4 | OS 4.0 (Master Econet Terminal)     |
|              5 | OS 5.0 (Master Compact)             |

Only Master 128 and Master Econet Terminal are supported. Any
other version gets a `Bad ROM <slot>` message printed and its
workspace byte cleared at `&02A0 + adjusted-slot`, effectively
rejecting the ROM.""", on_entry={'a': 'service call number', 'x': 'ROM slot', 'y': 'parameter'})

d.label(0x801A, 'copyright_string')

d.label(0x8070, 'init_nmi_workspace')

d.label(0x8072, 'copy_nmi_shim')

d.label(0x80B3, 'accept_frame')

d.label(0x80C6, 'scout_reject')

d.label(0x80CE, 'accept_local_net')

d.label(0x80D1, 'accept_scout_net')

d.label(0x80E5, 'scout_discard')

d.label(0x80ED, 'scout_loop_rda')

d.label(0x80FD, 'scout_loop_second')

d.label(0x8138, 'scout_no_match')

d.label(0x813B, 'scout_match_port')

d.label(0x8145, 'scan_port_list')

d.label(0x814E, 'scan_nfs_port_list')

d.label(0x8152, 'check_port_slot')

d.label(0x8154, 'scout_ctrl_check')

d.label(0x8166, 'check_station_filter')

d.label(0x8170, 'scout_port_match')

d.label(0x817A, 'next_port_slot')

d.label(0x8187, 'discard_no_match')

d.label(0x818A, 'try_nfs_port_list')

d.label(0x8195, 'port_match_found')

d.label(0x81A7, 'send_data_rx_ack')

d.label(0x81B8, 'data_rx_setup')

d.label(0x81D6, 'nmi_data_rx_net')

d.label(0x81EC, 'nmi_data_rx_skip')

d.label(0x81F7, 'install_data_rx_handler')

d.label(0x820A, 'install_tube_rx')

d.label(0x8215, 'nmi_error_dispatch')

d.label(0x821D, 'rx_error_reset')

d.label(0x8228, 'data_rx_loop')

d.label(0x8241, 'read_sr2_between_pairs')

d.label(0x8248, 'read_second_rx_byte')

d.label(0x825C, 'check_sr2_loop_again')

d.label(0x827F, 'read_last_rx_byte')

d.label(0x828E, 'send_ack')

d.label(0x8291, 'nmi_data_rx_tube')

d.label(0x8294, 'rx_tube_data')

d.label(0x82B1, 'data_rx_tube_error')

d.label(0x82B4, 'data_rx_tube_complete')

d.label(0x82EA, 'ack_tx_configure')

d.label(0x82F8, 'ack_tx_write_dest')

d.label(0x8339, 'start_data_tx')

d.label(0x833C, 'dispatch_nmi_error')

d.label(0x833F, 'advance_rx_buffer_ptr')

d.label(0x834A, 'add_rxcb_ptr')

d.label(0x8378, 'inc_rxcb_ptr')

d.label(0x8383, 'skip_tube_update')

d.label(0x8385, 'return_rx_complete')

d.label(0x8395, 'rx_complete_update_rxcb')

d.label(0x839A, 'add_buf_to_base')

d.label(0x83A1, 'inc_rxcb_buf_hi')

d.label(0x83A3, 'store_buf_ptr_lo')

d.label(0x83A5, 'store_rxcb_buf_ptr')

d.label(0x83AA, 'store_rxcb_buf_hi')

d.label(0x83AC, 'skip_buf_ptr_update')

d.label(0x8400, 'copy_scout_to_buffer')

d.label(0x8406, 'copy_scout_select')

d.label(0x8416, 'copy_scout_bytes')

d.label(0x8424, 'next_scout_byte')

d.label(0x842B, 'scout_copy_done')

d.label(0x8436, 'copy_scout_via_tube')

d.label(0x8448, 'release_tube')

d.label(0x8451, 'clear_release_flag')

d.label(0x846B, 'rotate_prot_mask')

d.label(0x8471, 'dispatch_imm_op')

d.label(0x847C, 'scout_page_overflow')

d.label(0x8482, 'check_scout_done')

d.label(0x8488, 'imm_op_out_of_range')

d.label(0x84A5, 'copy_addr_loop')

d.label(0x84B1, 'svc5_dispatch_lo')

d.label(0x84E0, 'set_tx_reply_flag')

d.label(0x84E8, 'rx_imm_halt_cont')

d.label(0x84ED, 'tx_cr2_setup')

d.label(0x84F2, 'tx_nmi_setup')

d.label(0x84F9, 'imm_op_build_reply')

d.label(0x8529, 'imm_op_discard')

d.label(0x8573, 'halt_spin_loop')

d.label(0x8582, 'tx_done_exit')

d.label(0x8589, 'tx_begin')

d.label(0x85A1, 'tx_imm_op_setup')

d.label(0x85B5, 'calc_peek_poke_size')

d.label(0x85CC, 'tx_ctrl_range_check')

d.label(0x85D0, 'check_imm_range')

d.label(0x85D6, 'copy_imm_params')

d.label(0x85E0, 'tx_line_idle_check')

d.label(0x85FA, 'test_inactive_retry')

d.label(0x85FC, 'intoff_test_inactive')

d.label(0x8602, 'test_line_idle')

d.label(0x8616, 'inactive_retry')

d.label(0x862C, 'tx_bad_ctrl_error')

d.label(0x863C, 'tx_no_clock_error')

d.label(0x863E, 'store_tx_error')

d.label(0x8697, 'add_bytes_loop')

d.label(0x8686, 'tx_ctrl_machine_type')

d.label(0x86A9, 'setup_data_xfer')

d.label(0x86BF, 'copy_bcast_addr')

d.label(0x86CB, 'setup_unicast_xfer')

d.label(0x86D0, 'proc_op_status2')

d.label(0x86D2, 'store_status_copy_ptr')

d.label(0x86D5, 'skip_buf_setup')

d.label(0x86E0, 'tx_ctrl_exit')

d.label(0x86ED, 'tx_fifo_write')

d.label(0x870D, 'tx_error')

d.label(0x8711, 'tx_fifo_not_ready')

d.label(0x8718, 'tx_store_error')

d.label(0x871B, 'delay_nmi_disable')

d.label(0x873C, 'check_handshake_bit')

d.label(0x8746, 'install_reply_scout')

d.label(0x8773, 'reject_reply')

d.label(0x87CE, 'data_tx_begin')

d.label(0x87DC, 'install_imm_data_nmi')

d.label(0x87F2, 'data_tx_check_fifo')

d.label(0x880B, 'write_second_tx_byte')

d.label(0x881F, 'check_irq_loop')

d.label(0x882B, 'data_tx_last')

d.label(0x883C, 'install_saved_handler')

d.label(0x8845, 'nmi_data_tx_tube')

d.label(0x8848, 'tube_tx_fifo_write')

d.label(0x8860, 'write_second_tube_byte')

d.label(0x886A, 'tube_tx_inc_byte2')

d.label(0x886E, 'tube_tx_inc_byte3')

d.label(0x8872, 'tube_tx_inc_byte4')

d.label(0x8876, 'check_tube_irq_loop')

d.label(0x887E, 'tx_tdra_error')

d.label(0x88A6, 'nmi_final_ack_net')

d.label(0x88D7, 'check_fv_final_ack')

d.label(0x88E2, 'tx_result_fail')

d.label(0x8935, 'calc_transfer_size')

d.label(0x8965, 'restore_x_and_return')

d.label(0x8968, 'fallback_calc_transfer')

d.label(0x898B, 'nmi_shim_rom_src')

d.label(0x89A6, 'wait_idle_and_reset')

d.label(0x89AB, 'poll_nmi_idle')

d.label(0x89C7, 'reset_enter_listen')
d.entry(0x804F)
d.entry(0x809B)
d.entry(0x80B8)
d.entry(0x80E8)
d.entry(0x81B8)
d.entry(0x81C2)
d.entry(0x81D6)
d.entry(0x81EC)
d.entry(0x8223)
d.entry(0x8291)
d.entry(0x8316)
d.entry(0x8360)
d.entry(0x8386)
d.entry(0x84F9)
d.entry(0x85F1)
d.entry(0x86E7)
d.entry(0x870D)
d.entry(0x8723)
d.entry(0x872F)
d.entry(0x874B)
d.entry(0x875F)
d.entry(0x8776)
d.entry(0x87BE)
d.entry(0x87E3)
d.entry(0x8845)
d.entry(0x8886)
d.entry(0x8892)
d.entry(0x88A6)
d.entry(0x88BA)
d.entry(0x88DE)
d.entry(0x88E4)
d.entry(0x8968)
d.entry(0x89CA)
d.entry(0x89D8)
d.comment(0x8000, """ANFS ROM 4.21 (variant 1) disassembly (Acorn Advanced Network Filing System)
============================================================================""")


d.subroutine(0x8050, 'adlc_init', title='ADLC initialisation', description="""Initialise ADLC hardware and Econet workspace. Disables NMIs via
`BIT master_intoff` (the Master 128 INTOFF register at &FE38;
the Model-B equivalent reads econet_station_id at &FE18 for the
same side effect). Performs a full ADLC reset via
[`adlc_full_reset`](address:898C), then probes for a Tube
co-processor via OSBYTE `&EA` and stores the result in
[`tube_present`](address:0D63). Issues an NMI-claim service
request (OSBYTE `&8F`, `X=&0C`). Falls through to
[`init_nmi_workspace`](address:8070) to copy the NMI shim to
RAM.""")


d.subroutine(0x8070, 'init_nmi_workspace', title='Initialise NMI workspace (skip service request)', description="""Copies 32 bytes of NMI shim code from ROM (`listen_jmp_hi`) to the
start of the NFS workspace RAM block, then patches the current ROM
bank number into the self-modifying code at `nmi_romsel` (`&0D07`).

The shim includes the INTOFF/INTON pair (`BIT
econet_station_id` at entry, `BIT econet_nmi_enable` before
`RTI`) that toggles the IC97 NMI-enable flip-flop, guaranteeing
edge re-triggering on /NMI.

Workspace fields written:

| Address / label | Value | Role |
|---|---|---|
| `tx_src_net`         | `0`    | clear |
| `need_release_tube`  | `0`    | clear |
| `tx_op_type`         | `0`    | clear |
| `tx_src_stn` (`&0D22`) | station ID | from `econet_station_id` |
| `tx_complete_flag`   | `&80`  | mark idle |
| `econet_init_flag`   | `&80`  | mark initialised |

Finally re-enables NMIs via INTON (`econet_nmi_enable` read).""")


d.subroutine(0x809B, 'nmi_rx_scout', title='NMI RX scout handler (initial byte)', description="""Default NMI handler for incoming scout frames. Checks whether the
frame is addressed to us or is a broadcast. Installed as the NMI
target during idle RX listen mode.

Tests `SR2` bit 0 (`AP` = Address Present) to detect incoming
data. Reads the first byte (destination station) from the RX FIFO
and compares against our station ID. Reading `econet_station_id`
(`&FE18`) also disables NMIs (INTOFF side effect).""")


d.subroutine(0x80B8, 'nmi_rx_scout_net', title='RX scout second byte handler', description="""Reads the second byte of an incoming scout (destination network).

| Value | Meaning | Action |
|---|---|---|
| `0`   | local network | accept |
| `&FF` | broadcast | accept and flag |
| other | foreign network | reject |

Installs [`copy_scout_to_buffer`](address:8400) as the
scout-data reading loop handler.""")


d.subroutine(0x80D8, 'scout_error', title='Scout error/discard handler', description="""Handles scout reception errors and end-of-frame conditions. Reads
`SR2` and tests `AP|RDA` (bits 0 and 7):

- **Neither set** – the frame ended cleanly; simply discard.
- **Either set** – unexpected data is present; perform a full ADLC
  reset.

Also serves as the common discard path for address/network
mismatches from [`nmi_rx_scout`](address:809B) and
[`scout_complete`](address:8112) – reached by 5 branch sites
across the scout reception chain.""")


d.subroutine(0x8112, 'scout_complete', title='Scout completion handler', description="""Processes a completed scout frame. Writes `CR1=&00` and `CR2=&84`
to disable `PSE` and suppress `FV`, then tests `SR2` for `FV`
(frame valid). If `FV` is set with `RDA`, reads the remaining
scout data bytes in pairs into the buffer at `&0D3D`.

Matches the port byte (`&0D40`) against open receive control
blocks to find a listener:

- **On match** – calculates the transfer size via
  [`tx_calc_transfer`](address:8900), sets up the data RX
  handler chain, and sends a scout ACK.
- **On no match or error** – discards the frame via
  [`scout_error`](address:80D8).""")


d.subroutine(0x8195, 'port_match_found', title='Scout matched: arm data RX, ACK or discard', description="""Sets `scout_status=3` (match found) at `rx_port`, calls
[`tx_calc_transfer`](address:8900) to compute the transfer
parameters from the RXCB, then triages:

| Carry | `rx_src_net` (V) | Action |
|---|---|---|
| `C=0` | – | no Tube claimed → [`nmi_error_dispatch`](address:8215) (discard) |
| `C=1` | broadcast | discard (broadcasts get no ACK) |
| `C=1` | unicast   | [`send_data_rx_ack`](address:81A7) |

Four inbound refs (one `JSR` from `&84B9` and three branches from
the [`scout_complete`](address:8112) dispatch).""", on_exit={'a': '3 (scout_status)'})


d.subroutine(0x81A7, 'send_data_rx_ack', title='Send scout ACK and arm data-RX continuation', description="""Switches the ADLC to TX mode for the scout ACK frame: writes
`CR1=&44` (`RX_RESET | TIE`), `CR2=&A7` (`RTS | CLR_TX_ST |
FC_TDRA | PSE`), then loads `(A,Y) = (&B8, &81)` – the address
of [`data_rx_setup`](address:81B8) – and `JMP`s to
[`ack_tx_write_dest`](address:82F8) which saves the pair into
`saved_nmi_lo`/`saved_nmi_hi` (so the NMI handler will install it
later) and writes the ACK destination address bytes to the TX
FIFO.

Two callers: the dispatch in [`scout_complete`](address:8112)
at `&81A2` and the immediate-op POKE path at `&84AE`
(`jmp_send_data_rx_ack`).""", on_exit={'a': '&B8 (low byte of data_rx_setup)', 'y': '&81 (high byte of data_rx_setup)'})


d.subroutine(0x81B8, 'data_rx_setup', title='NMI handler: switch ADLC to RX for the data frame', description="""NMI continuation entry installed by
[`send_data_rx_ack`](address:81A7) (which pushes
`(&81B8 - 1)` on the stack and routes it through
[`ack_tx_write_dest`](address:82F8)). When the next NMI fires,
this body writes `CR1 = &82` (`TX_RESET | RIE`) to switch the
ADLC from scout-ACK TX mode to data-frame RX mode, then `JMP`s to
`install_nmi_handler` to install
[`nmi_data_rx`](address:81C2) as the next NMI handler.""")


d.subroutine(0x81C2, 'nmi_data_rx', title='Data frame RX handler (four-way handshake)', description="""Receives the data frame after the scout ACK has been sent. First
checks AP (Address Present) for the start of the data frame. Reads
and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: this routine (AP + dest-stn check) →
[`nmi_data_rx_net`](address:81D6) (dest-net check) →
[`nmi_data_rx_skip`](address:81EC) (skip ctrl + port) →
[`nmi_data_rx_bulk`](address:8223) (bulk data read) →
[`data_rx_complete`](address:8268) (completion).""")


d.subroutine(0x81D6, 'nmi_data_rx_net', title='NMI handler: validate dest-net byte of data frame', description="""NMI continuation entry installed by [`nmi_data_rx`](address:81C2)
once the AP and dest-station bytes have validated. Polls SR2
(`BIT econet_control23_or_status2`); on no RDA, branches to
[`nmi_error_dispatch`](address:8215). Otherwise reads the dest-
network byte from the ADLC FIFO and falls through to the
control/port skip step.""", on_exit={'a': 'dest-network byte (validated against local)'})


d.subroutine(0x81EC, 'nmi_data_rx_skip', title='NMI handler: skip control + port bytes', description="""NMI continuation entry that consumes the control and port bytes of
the data frame (already known from the scout) and proceeds to the
bulk-data-read continuation. Polls SR2 for RDA on entry; on no
RDA, branches to [`nmi_error_dispatch`](address:8215).""")


d.subroutine(0x81F7, 'install_data_rx_handler', title='Install data RX bulk or Tube handler', description="""Selects between the normal bulk-RX handler at
[`nmi_data_rx_bulk`](address:8223) and the Tube RX handler at
[`nmi_data_rx_tube`](address:8291) based on bit 1 of
`rx_src_net` (`tx_flags`).

| `rx_src_net` bit 1 | Handler |
|---|---|
| clear | [`nmi_data_rx_bulk`](address:8223) (`A=&23`, `Y=&82`) |
| set   | [`nmi_data_rx_tube`](address:8291) (`A=&91`, `Y=&82`) |

In the bulk path, after loading the handler address, checks `SR1`
bit 7. If `IRQ` is already asserted (more data waiting), jumps
directly to [`nmi_data_rx_bulk`](address:8223) to avoid NMI
re-entry overhead. Otherwise installs the handler via
[`set_nmi_vector`](address:0D0E) (the `(A,Y)` pair becomes the
NMI dispatch target) and returns via `RTI`.""")


d.subroutine(0x8215, 'nmi_error_dispatch', title='NMI error handler dispatch', description="""Common error/abort entry used by 11 call sites. The dispatch byte
at [`rx_src_net`](address:0D3E) doubles as a TX-state flag here:
bit 7 distinguishes whether the NMI handler reached this point on
an RX-error path or a TX not-listening path.

| `rx_src_net` bit 7 | Path |
|---|---|
| clear | RX error – full ADLC reset; return to idle listen |
| set   | TX not-listening – `JMP` [`tx_result_fail`](address:88E2) |""")


d.subroutine(0x8223, 'nmi_data_rx_bulk', title='Data frame bulk read loop', description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at `(open_port_buf),Y`. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.

- SR2 non-zero (FV or other) → completion via
  [`data_rx_complete`](address:8268).
- SR2 = 0 → RTI, wait for next NMI to continue.""")


d.subroutine(0x8268, 'data_rx_complete', title='Data frame completion', description="""Reached when `SR2` non-zero during data RX (`FV` detected). Same
pattern as scout completion: disables `PSE` (`CR2=&84`, `CR1=&00`),
then tests `FV` and `RDA`. If `FV+RDA`, reads the last byte; if
extra data is available and buffer space remains, stores it.
Proceeds to send the final ACK via [`ack_tx`](address:82DF).""")


d.subroutine(0x8291, 'nmi_data_rx_tube', title='NMI handler: data-frame RX into Tube buffer', description="""NMI continuation entry for the Tube data-RX path. Polls SR2 for
RDA, reads the next data byte from the ADLC RX FIFO, and writes it
to the Tube data register, advancing the Tube transfer pointer
each iteration. Tests for end-of-frame via FV and either continues
the tight inner loop or returns via `RTI`. Reached only via the
NMI vector after `install_tube_rx` configures the handler.""")


d.subroutine(0x82DF, 'ack_tx', title='ACK transmission', description="""Sends a scout ACK or final ACK frame as part of the four-way
handshake. Tests bit 7 of [`rx_src_net`](address:0D3E) (used as
TX-flags here): if set this is a final ACK and completion runs
through [`tx_result_ok`](address:88DE). Otherwise configures
for TX (`CR1=&44`, `CR2=&A7`) and writes the ACK address frame:
destination station from [`scout_buf`](address:0D2E), destination
network from [`scout_src_net`](address:0D2F), source station
from the workspace copy [`tx_src_stn`](address:0D22), and
`src_net=0`. The ACK frame has no data payload -- just address
bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from `saved_nmi_lo`/`saved_nmi_hi` (saved by the
scout/data RX handler via [`ack_tx_write_dest`](address:82F8))
and sends `TX_LAST_DATA` (`CR2=&3F`) to close the frame.""")


d.subroutine(0x82F8, 'ack_tx_write_dest', title='Begin ACK transmit: write destination address to ADLC', description="""First step of the four-byte ACK frame transmission. Saves the
caller-supplied `(A=lo, Y=hi)` next-NMI handler address into
`saved_nmi_lo` / `saved_nmi_hi`, loads the destination station
from [`scout_buf`](address:0D2E) and tests `SR1` bit 6 (`TDRA`,
TX Data Register Available) via `BIT adlc_cr1`. If `TDRA` is
clear the TX FIFO isn't ready and control branches to
[`dispatch_nmi_error`](address:833C) to abort.

When `TDRA` is set, writes the destination station and network
bytes (from [`scout_src_net`](address:0D2F)) into `adlc_tx`, then
installs [`nmi_ack_tx_src`](address:8316) as the next NMI handler
via [`set_nmi_vector`](address:0D0E) -- that handler will write
the source-address pair on the next NMI.

Two callers: [`send_data_rx_ack`](address:81A7)'s tail `JMP` and
[`imm_op_build_reply`](address:84F9).""", on_entry={'a': 'low byte of next NMI handler', 'y': 'high byte of next NMI handler'})


d.subroutine(0x8316, 'nmi_ack_tx_src', title='ACK TX continuation', description="""Continuation of ACK frame transmission, reached via NMI after
[`ack_tx_write_dest`](address:82F8) installed it as the next
handler. Reads our station ID from the workspace copy
[`tx_src_stn`](address:0D22), tests `TDRA` via `SR1`, and writes
`(station, network=0)` to the TX FIFO -- completing the 4-byte
ACK address header.

Then dispatches on [`rx_src_net`](address:0D3E) bit 7 (which the
caller uses as a TX-flags byte):

| Bit 7 | Action |
|---|---|
| set   | branch to `start_data_tx` to begin the data phase |
| clear | write `CR2=&3F` (TX_LAST_DATA) and fall through to [`post_ack_scout`](address:832D) |""")


d.subroutine(0x832D, 'post_ack_scout', title='Post-ACK scout processing', description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer starting at
[`rx_src_stn`](address:0D3D) (scout-ACK destination
addresses). Checks the port byte at
[`rx_port`](address:0D40) against open receive blocks to find
a matching listener.

- **Match** – sets up the data-RX handler chain for the four-way-
  handshake data phase.
- **No match** – discards the frame.""")


d.subroutine(0x833F, 'advance_rx_buffer_ptr', title='Advance RX buffer pointer after transfer', description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.

Reads:

- [`tx_flags`](address:0D4A) bit 1 – data transfer in progress
- [`tx_flags`](address:0D4A) bit 5 – Tube transfer
- 4-byte transfer count from `net_tx_ptr,Y` (`Y=8..&0B`)
- RXCB pointer at `(port_ws_offset),Y`

Updates the RXCB in place. Clobbers `A` and `Y`; preserves `X`
across the Tube branch (saved/restored via stack).""", on_exit={'a': '&FF when transfer was active, else preserved entry value'})


d.subroutine(0x8386, 'nmi_post_ack_dispatch', title='Post-ACK frame-complete NMI handler', description="""Installed by `ack_tx_configure` via
[`saved_nmi_lo`](address:0D43) / [`saved_nmi_hi`](address:0D44).
Fires as an NMI after the ACK frame (CRC + closing flag) has been
fully transmitted by the ADLC. Dispatches on `scout_port`:

| `scout_port` | Control | Target |
|---|---|---|
| `≠ 0` | – | [`rx_complete_update_rxcb`](address:8395) (finalise data transfer, mark RXCB complete) |
| `0`   | `&82` (POKE) | [`rx_complete_update_rxcb`](address:8395) (same path) |
| `0`   | other | `imm_op_build_reply` |""")


d.subroutine(0x8395, 'rx_complete_update_rxcb', title='Complete RX and update RXCB', description="""Called from [`nmi_post_ack_dispatch`](address:8386) after the
final ACK has been transmitted. Finalises the received data
transfer:

1. Calls [`advance_rx_buffer_ptr`](address:833F) to update the
   4-byte buffer pointer with the transfer count (and handle Tube
   re-claim if needed).
2. Stores the source station, network, and port into the RXCB.
3. ORs `&80` into the RXCB control byte (bit 7 = complete).

This is the **NMI-to-foreground synchronisation point**:
`wait_net_tx_ack` polls bit 7 of the RXCB control byte to detect
that the reply has arrived.

Falls through to [`discard_reset_rx`](address:83E5) to reset
the ADLC to idle RX-listen mode.""")


d.subroutine(0x83E5, 'discard_reset_rx', title='Discard scout, reset ADLC, install RX-scout NMI', description="""Three-stage idle-restore chain:

1. [`discard_reset_listen`](address:83F2) – abandon any
   in-flight scout and release a held Tube claim.
2. [`reset_adlc_rx_listen`](address:83E8) – call
   `adlc_rx_listen` (reset `CR1`/`CR2` and re-arm RX).
3. [`set_nmi_rx_scout`](address:83EB) – install
   [`nmi_rx_scout`](address:809B) as the active NMI handler
   and `JMP` out via [`set_nmi_vector`](address:0D0E).

Used as the standard "something went wrong, get back to listening"
exit.""")


d.subroutine(0x83E8, 'reset_adlc_rx_listen', title='Reset ADLC and install RX-scout NMI', description="""Tail of the [`discard_reset_rx`](address:83E5) chain entered
directly when no scout needs discarding. Calls `adlc_rx_listen`
to reset `CR1`/`CR2` to RX-only mode, then falls through to
[`set_nmi_rx_scout`](address:83EB).

Two inbound `JSR`s plus one fall-through (from
[`discard_reset_rx`](address:83E5)).""")


d.subroutine(0x83EB, 'set_nmi_rx_scout', title='Install nmi_rx_scout as NMI handler', description="""Loads `(A=&9B, Y=&80)` -- the address of
[`nmi_rx_scout`](address:809B) -- and `JMP`s to
[`set_nmi_vector`](address:0D0E), which writes both bytes into
the NMI JMP-target slot at `nmi_jmp_lo`/`nmi_jmp_hi`. Tail of
the [`discard_reset_rx`](address:83E5) /
[`reset_adlc_rx_listen`](address:83E8) chain, used to put the
NMI vector back to scout-handling after a discard or reset.

Two callers: `&80CB` (after init) and `&80E2` (after error).""")


d.subroutine(0x83F2, 'discard_reset_listen', title='Discard with Tube release', description="""Checks whether a Tube transfer is active by ANDing bit 1 of
[`tube_present`](address:0D63) with
[`rx_src_net`](address:0D3E) (`tx_flags`). If a Tube claim is
held, calls [`release_tube`](address:8448) to free it before
returning.

Used as the clean-up path after RXCB completion and after ADLC
reset to ensure no stale Tube claims persist.""")


d.subroutine(0x8400, 'copy_scout_to_buffer', title='Copy scout data to port buffer (entry point)', description="""Five-instruction prologue that prepares to copy scout-payload
bytes (offsets `4..&0B`) from [`scout_buf`](address:0D2E) into the
open port buffer. Saves `X` on the stack, loads `X=4` (the first
scout-data offset) and `A=&02` (Tube-flag mask), then `BIT`s
[`rx_src_net`](address:0D3E) (`tx_flags`) so the immediately
following `BNE` in
[`save_acccon_for_shadow_ram`](address:8409) can dispatch:

| Bit 1 | Path |
|---|---|
| clear | fall through into `save_acccon_for_shadow_ram` (direct memory store via `(open_port_buf),Y`, with ACCCON saved/restored on Master 128) |
| set   | branch to [`copy_scout_via_tube`](address:8436) (Tube R3 write) |

Both paths walk the four-byte buffer pointer and end via
[`scout_copy_done`](address:842B) which restores `X` and returns.
Single caller: [`port_match_found`](address:8195) at `&81A4`.""")


d.subroutine(0x8448, 'release_tube', title='Release Tube co-processor claim', description="""Tests bit 7 of [`prot_flags`](address:0099) -- the bit ANFS uses
to track whether the Tube is currently still claimed:

| Bit 7 | State | Action |
|---|---|---|
| set | already released | branch to `clear_release_flag` (skips the release call) |
| clear | claim held | `JSR tube_addr_data_dispatch` with `A=&82` to release the claim, then fall through |

Both paths end at `clear_release_flag` which `LSR`s `prot_flags`
(shifting bit 7 to 0) before returning.

Called after completed RX transfers and during discard paths to
ensure no stale Tube claims persist.

**Idempotent:** safe to call when the Tube has already been
released. Clobbers `A`; preserves `X` and `Y`.""", on_exit={'a': 'clobbered'})


d.subroutine(0x8454, 'immediate_op', title='Immediate operation handler (port = 0)', description="""Checks the control byte at [`scout_ctrl`](address:0D30) for
immediate-operation codes:

| Range | Op | Treatment |
|---|---|---|
| `< &81` or `> &88` | – | out of range; discarded |
| `&81`..`&86` | PEEK / POKE / JSR / UserProc / OSProc / HALT | gated by [`econet_flags`](address:0D61) immediate-op mask |
| `&87`..`&88` | CONTINUE / machine-type | bypass the mask check |

For `&81`..`&86`, converts the code to a 0-based index and tests
against the immediate-op mask at
[`econet_flags`](address:0D61) to determine whether this
station accepts the operation. If accepted, dispatches via
[`imm_op_dispatch_lo`](address:848B) (PHA/PHA/RTS).

Builds the reply by storing data length, station / network, and
control byte into the RX buffer header.""")


d.subroutine(0x848B, 'imm_op_dispatch_lo', title='Immediate-op dispatch lo-byte table (8 entries)', description="""Eight low-byte entries at `&848B`-`&8492` indexed by the
immediate-op control byte (`&81`-`&88`) via
`LDA imm_op_dispatch_lo-&81,Y` at the dispatch site. Each entry is
the low byte of `(handler-1)` so PHA/PHA/RTS dispatch lands on the
handler. The high byte pushed by the dispatcher is constant
(`&84`), so all targets sit in `&84xx`. Per-entry inline comments
identify each control byte's handler.""")
for addr in range(0x848B, 0x8493):
    d.byte(addr)
d.expr(0x848B, '<(rx_imm_peek-1)')
d.expr(0x848C, '<(rx_imm_poke-1)')
d.expr(0x848D, '<(rx_imm_exec-1)')
d.expr(0x848E, '<(rx_imm_exec-1)')
d.expr(0x848F, '<(rx_imm_exec-1)')
d.expr(0x8490, '<(rx_imm_halt_cont-1)')
d.expr(0x8491, '<(rx_imm_halt_cont-1)')
d.expr(0x8492, '<(rx_imm_machine_type-1)')
d.comment(0x848B, 'ctrl &81: PEEK', align=Align.INLINE)
d.comment(0x848C, 'ctrl &82: POKE', align=Align.INLINE)
d.comment(0x848D, 'ctrl &83: JSR', align=Align.INLINE)
d.comment(0x848E, 'ctrl &84: UserProc', align=Align.INLINE)
d.comment(0x848F, 'ctrl &85: OSProc', align=Align.INLINE)
d.comment(0x8490, 'ctrl &86: HALT', align=Align.INLINE)
d.comment(0x8491, 'ctrl &87: CONTINUE', align=Align.INLINE)
d.comment(0x8492, 'ctrl &88: machine-type', align=Align.INLINE)


d.subroutine(0x8493, 'rx_imm_exec', title='RX immediate: JSR / UserProc / OSProc setup', description="""Sets up the port buffer to receive remote-procedure data. Copies
the 2-byte remote address from [`scout_data`](address:0D32)
into the execution-address workspace at
[`exec_addr_lo`](address:0D66) / [`exec_addr_hi`](address:0D67),
then jumps to the common data-receive path at `&81C1`.

Used for operation types `&83` (JSR), `&84` (UserProc), and
`&85` (OSProc).""")


d.subroutine(0x84B1, 'rx_imm_poke', title='RX immediate: POKE setup', description="""Sets up workspace offsets for receiving POKE data:
`port_ws_offset = &2E`, `rx_buf_offset = &0D`. Jumps to the
common data-receive path at `&81AF`.""")


d.subroutine(0x84BC, 'rx_imm_machine_type', title='RX immediate: machine-type query', description="""Sets up the response buffer for a machine-type query immediate
operation (4-byte response: machine code + version digits). Falls
through to [`set_rx_buf_len_hi`](address:84BE) to configure
the buffer dimensions, then branches to `set_tx_reply_flag`.""")


d.subroutine(0x84CE, 'rx_imm_peek', title='RX immediate: PEEK setup', description="""Writes `&0D2E` to `port_ws_offset` / `rx_buf_offset`, sets
`scout_status = 2`, then calls
[`tx_calc_transfer`](address:8900) to send the PEEK response
data back to the requesting station.""")


d.subroutine(0x8512, 'setup_sr_tx', title='Save TX op type and update workspace ACR-format byte', description="""Stores the TX operation type in [`tx_op_type`](address:0D65).

| Op code | Path |
|---|---|
| `≥ &86` (HALT / CONTINUE / machine-type) | branch forward to the ACCCON IRR set; the workspace byte is left untouched |
| `< &86` | load [`ws_0d68`](address:0D68), copy it to [`ws_0d69`](address:0D69) (preserved for later restore), `ORA` in bits 2-4 (the SR-mode-2 mask in System-VIA ACR layout), write the modified value back to `ws_0d68` |

The byte at `ws_0d68` carries an ACR-format flag layout left over
from 4.18, which used the same op-code dispatch to update the
*live* System VIA ACR. In 4.21 the byte stays in workspace --
nothing in this ROM flushes it to the live VIA. Single caller
(`&83E2` in [`scout_complete`](address:8112)).""", on_entry={'a': 'TX operation type'})


d.subroutine(0x852C, 'advance_buffer_ptr', title='Increment 4-byte receive-buffer pointer', description="""Adds 1 to the 4-byte counter at `&A2..&A5` (`port_buf_len` lo/hi,
`open_port_buf` lo/hi), cascading overflow through all four
bytes. Called after each byte is stored during scout-data copy
and data-frame reception to track the current write position in
the receive buffer.

Preserves `A`, `X`, `Y` (uses `INC zp` throughout).""", on_exit={'a, x, y': 'preserved (INC zp only)'})


d.subroutine(0x84F9, 'imm_op_build_reply', title='Build immediate-operation reply header', description="""Writes the reply-frame header for a port-0 immediate operation
into the RX buffer at offsets `&7F..&81`:

| RX offset | Source | Meaning |
|---|---|---|
| `&7F` | `port_buf_len + &80` | reply data length (raw count + header offset) |
| `&80` | [`scout_buf`](address:0D2E) | requesting station |
| `&81` | [`scout_src_net`](address:0D2F) | requesting network |

Then loads the control byte from
[`scout_ctrl`](address:0D30) into `A` and falls through into
[`setup_sr_tx`](address:8512), which stores `A` as
[`tx_op_type`](address:0D65) and configures the ADLC for the SR
phase of the reply. Reached via the immediate-op dispatch path.""")
d.entry(0x8540)


d.subroutine(0x8540, 'tx_done_jsr', title='TX done: remote JSR execution', description="""Pushes ([`tx_done_exit`](address:8582) ` - 1`) on the stack so
`RTS` returns to [`tx_done_exit`](address:8582) when the remote
routine completes, then does `JMP` indirect through
[`exec_addr_lo`](address:0D66) to call the remote-supplied JSR
target. When that routine returns via `RTS`, control resumes at
[`tx_done_exit`](address:8582) which tidies up TX state.""")


d.subroutine(0x8549, 'tx_done_econet_event', title='TX done: fire Econet event', description="""Handler for TX operation type `&84`. Loads the remote address
from [`exec_addr_lo`](address:0D66) /
[`exec_addr_hi`](address:0D67) into `X` / `A` and sets `Y=8`
(Econet event number), then falls through to `tx_done_fire_event`
to call OSEVEN.

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi. The dispatcher
pushed the caller's `X` and `Y` onto the stack before
transferring control, and the shared
[`tx_done_exit`](address:8582) restores them via
`PLA`/`TAY`/`PLA`/`TAX` before returning `A=0`.""", on_exit={'a': '0 (success status)', 'x, y': 'restored from stack via tx_done_exit'})


d.subroutine(0x8557, 'tx_done_os_proc', title='TX done: OSProc call', description="""Calls the ROM service entry point with
`X = `[`exec_addr_lo`](address:0D66)`, Y = `[`exec_addr_hi`](address:0D67).
This invokes an OS-level procedure on behalf of the remote
station, then exits via [`tx_done_exit`](address:8582).

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi.""", on_exit={'a': '0 (success status)', 'x, y': 'restored from stack via tx_done_exit'})


d.subroutine(0x8563, 'tx_done_halt', title='TX done: HALT', description="""Sets bit 2 of [`econet_flags`](address:0D61), enables
interrupts, and spin-waits until bit 2 is cleared (by a CONTINUE
from the remote station). If bit 2 is already set, skips to exit.

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi. Falls through to
[`tx_done_continue`](address:857A) after the spin completes;
on the already-halted path it branches directly to
[`tx_done_exit`](address:8582).""", on_exit={'a': '0 (success status, set by tx_done_exit)', 'i flag': 'interrupts enabled (CLI inside the spin)', 'x, y': 'restored from stack via tx_done_exit'})


d.subroutine(0x857A, 'tx_done_continue', title='TX done: CONTINUE', description="""Clears bit 2 of [`econet_flags`](address:0D61), releasing any
station that is halted and spinning in
[`tx_done_halt`](address:8563).

Reached either as a fall-through from
[`tx_done_halt`](address:8563) or directly via
`PHA`/`PHA`/`RTS` dispatch from
[`tx_done_dispatch_lo`](address:853B) / hi. Falls through to
[`tx_done_exit`](address:8582) which restores `X` and `Y`
from the stack and returns `A=0`.""", on_exit={'a': '0 (success status)', 'x, y': 'restored from stack via tx_done_exit'})


d.subroutine(0x8582, 'tx_done_exit', title='Shared TX-done exit: restore X/Y, return A=0', description="""Common cleanup tail used by every entry in the
[`tx_done_dispatch_lo`](address:853B) table. Pulls the saved
`Y` and `X` off the stack (the dispatcher pushed them before the
`PHA`/`PHA`/`RTS` jump), loads `A=0` (success status), and `RTS`
to the caller.

Five inbound refs: a tail-jump from `&8042` (the SVC 5 IRQ-check
path in [`svc5_irq_check`](address:8028)), plus the JMPs at
`&8554`, `&8560`, `&8568`, and the fall-through at `&8578`.""", on_exit={'a': '0 (success status)', 'x, y': 'restored from stack'})


d.subroutine(0x8589, 'tx_begin', title='Begin TX operation', description="""Main TX initiation entry point (called via the NETV trampoline).

1. Copies destination station / network from the TXCB to the
   scout buffer.
2. Dispatches: control byte `≥ &81` → immediate-op setup; else
   normal data transfer.
3. Calculates transfer sizes via
   [`tx_calc_transfer`](address:8900); copies extra
   parameters into the workspace.
4. Enters the INACTIVE polling loop at
   [`inactive_poll`](address:85F1).""")


d.subroutine(0x85F1, 'inactive_poll', title='INACTIVE polling loop', description="""Entry point for the Econet line-idle detection loop.

1. Saves the TX index in [`rx_remote_addr`](address:0D41).
2. Pushes two timeout-counter bytes onto the stack.
3. Loads `Y = &E7` (CR2 value for TX preparation).
4. Loads the INACTIVE bit mask (`&04`) into `A`.
5. Falls through to [`intoff_test_inactive`](address:85FC)
   to begin polling `SR2` with interrupts disabled.""", on_exit={'y': '&E7 (CR2 value for tx_prepare)'})


d.subroutine(0x85FC, 'intoff_test_inactive', title='Disable NMIs and test INACTIVE', description="""Disables NMIs via two `BIT` reads of
[`master_intoff`](address:FE38) (the Master 128 INTOFF register;
the Model-B equivalent reads `econet_station_id` at &FE18 for the
same side-effect), then polls `SR2` for the INACTIVE bit (bit 2):

| `SR2` INACTIVE | Action |
|---|---|
| set   | read `SR1`, write `CR2=&67` to clear status, then test `CTS` (`SR1` bit 4); if `CTS` present, branch to [`tx_prepare`](address:864A) |
| clear | re-enable NMIs via [`master_inton`](address:FE3C) (INTON) and decrement the 3-byte timeout counter on the stack |

On timeout, falls through to
[`tx_line_jammed`](address:8630).""", on_entry={'a': '&04 (INACTIVE bit mask)', 'y': '&E7 (CR2 value for tx_prepare)'})


d.subroutine(0x862C, 'tx_bad_ctrl_error', title="Raise TX 'Bad control byte' (&44) error", description="""Loads error code `&44` ("Bad control") and ALWAYS-branches to
`store_tx_error`, which records it in the TX control block and
finishes the TX attempt.

Reached from three early-validation sites in
[`tx_begin`](address:8589) (`&859E`, `&85CE`, `&85D2`) when the
operation type is out of range.""", on_exit={'a': "&44 (TX 'Bad control' error code)"})


d.subroutine(0x8630, 'tx_line_jammed', title='TX timeout error handler (Line Jammed)', description="""Reached when the [`inactive_poll`](address:85F1) /
[`intoff_test_inactive`](address:85FC) loop times out without
detecting a quiet line.

1. Writes `CR2=&07` (`FC_TDRA | 2_1_BYTE | PSE`) to abort the TX
   attempt.
2. Pulls the 3-byte timeout state from the stack.
3. Stores error code `&40` ("Line Jammed") in the TX control
   block via `store_tx_error`.""")


d.subroutine(0x864A, 'tx_prepare', title='TX preparation', description="""Configures the ADLC for frame transmission and dispatches to the
control-byte handler.

1. Writes `CR2 = Y` (`&E7`) and `CR1 = &44` to enable TX with
   interrupts (`RX_RESET` + transmit-IRQ enable).
2. Installs [`nmi_tx_data`](address:86E7) as the next NMI handler
   by writing `&E7,&86` directly into `nmi_jmp_lo` / `nmi_jmp_hi`.
3. Sets bit 7 of [`prot_flags`](address:0099) (Tube-claimed
   marker, paired with [`release_tube`](address:8448)) via
   `SEC` / `ROR prot_flags`.
4. `BIT master_inton` re-enables NMIs so `TDRA` can fire.

Then dispatches on [`tx_port`](address:0D25):

| `tx_port` | Path |
|---|---|
| non-zero | branch to `setup_data_xfer` (standard data transfer) |
| zero (immediate op) | look up `tx_flags` / `tx_length` from `tx_flags_table` / `tx_length_table` indexed by [`tx_ctrl_byte`](address:0D24), push `&86` (high byte) and `tx_ctrl_dispatch_lo[Y-&81]` (low byte) and `RTS` to the control-byte handler |

The 4-byte destination-address write to the TX FIFO happens in
the dispatched-to handler (e.g. `setup_data_xfer`,
[`tx_ctrl_machine_type`](address:8686), etc.), not here.""", on_entry={'y': '&E7 (CR2 prep value)'})


d.subroutine(0x8686, 'tx_ctrl_machine_type', title='TX ctrl: machine-type query setup', description="""Handler for control byte `&88`. Sets `scout_status = 3` and
branches to `store_status_copy_ptr`, skipping the 4-byte address
addition (no address parameters needed for a machine-type query).

Reached only via `PHA`/`PHA`/`RTS` dispatch from
[`tx_ctrl_dispatch_lo`](address:867E) entry `&88`.""", on_exit={'a': '3 (scout_status for machine type query)'})


d.subroutine(0x868A, 'tx_ctrl_peek', title='TX ctrl: PEEK transfer setup', description="""Sets `A=3` (scout_status for PEEK) and branches to
[`tx_ctrl_store_and_add`](address:8690) to store the status
and perform the 4-byte transfer-address addition.""", on_exit={'a': '3 (scout_status for PEEK)'})


d.subroutine(0x868E, 'tx_ctrl_poke', title='TX ctrl: POKE transfer setup', description="""Sets `A=2` (scout_status for POKE) and falls through to
[`tx_ctrl_store_and_add`](address:8690) to store the status
and perform the 4-byte transfer-address addition.""", on_exit={'a': '2 (scout_status for POKE)'})


d.subroutine(0x8690, 'tx_ctrl_store_and_add', title='TX ctrl: store status and add transfer address', description="""Shared path for PEEK (`A=3`) and POKE (`A=2`):

1. Stores `A` as the scout status byte at
   [`rx_port`](address:0D40).
2. Performs a 4-byte addition with carry propagation. For
   `Y=&0C..&0F` it adds `(nmi_tx_block),Y` (i.e. TXCB bytes
   12..15 from the block pointed to by
   [`nmi_tx_block`](address:00A0)) into `tx_addr_base,Y` --
   `tx_addr_base+&0C..&0F` is the 4-byte transfer-length
   workspace at [`tx_data_len`](address:0D2A)..&0D2D.
3. Falls through to [`tx_ctrl_proc`](address:86A2) which
   checks the loop boundary, then continues to
   [`tx_calc_transfer`](address:8900) and `tx_ctrl_exit`.""", on_entry={'a': 'scout status (3=PEEK, 2=POKE)'})


d.subroutine(0x86A2, 'tx_ctrl_proc', title='TX ctrl: tail of address-add loop + setup_data_xfer entry', description="""Tail of the 4-byte transfer-address addition loop that started in
[`tx_ctrl_store_and_add`](address:8690): `CPY #&10` ends the
loop when Y reaches `&10`, `PLP` restores the saved carry, and
`BNE` skips the buffer-setup code if the transfer size is zero.

Falls through (or is reached via the dispatch from
[`tx_prepare`](address:864A) when port != 0) to
`setup_data_xfer` at `&86A9`, which dispatches between broadcast
and unicast based on whether `tx_dst_stn` and `tx_dst_net` are
both `&FF`.""")


d.subroutine(0x86E7, 'nmi_tx_data', title='NMI TX data handler', description="""Writes 2 bytes per NMI invocation to the TX FIFO at
[`adlc_tx`](address:FEA2). Uses `BIT`
[`adlc_cr1`](address:FEA0)
on `SR1` to test `TDRA` (`V` flag = bit 6) and `IRQ` (`N` flag =
bit 7).

After writing 2 bytes, checks if the frame is complete:

| `SR1` bit 7 (`IRQ`) | Action |
|---|---|
| set   | tight loop: write 2 more bytes without returning from NMI |
| clear | return via `RTI` and wait for the next NMI |""")


d.subroutine(0x8723, 'tx_last_data', title='TX_LAST_DATA and frame completion', description="""Signals end of TX frame by writing `CR2=&3F` (TX_LAST_DATA), then
installs [`nmi_tx_complete`](address:872F) as the next NMI
handler.

`CR2=&3F` = `%0011_1111`, with each bit selecting an ADLC
control function:

| Bit | Mnemonic | Effect |
|-----|----------|--------|
| 7   | (RTS)    | **0** – drops RTS after frame |
| 6   | (CLR_TX_ST) | **0** – do *not* clear TX status |
| 5   | CLR_RX_ST | clears `fv_stored_` (prepares for RX of reply) |
| 4   | TX_LAST_DATA | tells the ADLC this is the final data byte |
| 3   | FLAG_IDLE | send flags / idle after the frame |
| 2   | FC_TDRA  | force clear TDRA |
| 1   | 2_1_BYTE | two-byte transfer mode |
| 0   | PSE      | prioritised status enable |

The routine exits via `JMP` to
[`set_nmi_vector`](address:0D0E), which installs
[`nmi_tx_complete`](address:872F) and falls through to
[`nmi_rti`](address:0D14). The `BIT` of
[`econet_nmi_enable`](address:FE20) (INTON) inside
[`nmi_rti`](address:0D14) creates the /NMI edge for the
frame-complete interrupt – essential because the ADLC IRQ may
transition atomically from TDRA to frame-complete without
de-asserting in between.""")


d.subroutine(0x872F, 'nmi_tx_complete', title='TX completion: switch to RX mode', description="""Called via NMI after the frame (including CRC and closing flag)
has been fully transmitted. Writes `CR1=&82` (`TX_RESET | RIE`)
to clear `RX_RESET` and enable RX interrupts – the **TX-to-RX
pivot** in the four-way handshake. The scout ACK can only be
received after this point.

Full `CR1` sequence through a handshake:

| Step | `CR1` | Meaning |
|---|---|---|
| 1 | `&44` | scout TX |
| 2 | `&82` | await scout ACK |
| 3 | `&44` | data TX |
| 4 | `&82` | await data ACK |

Dispatches on [`rx_src_net`](address:0D3E) flags:

| Flag | Action |
|---|---|
| bit 6 set (broadcast) | jump to [`tx_result_ok`](address:88DE) |
| bit 0 set (handshake data pending) | jump to [`handshake_await_ack`](address:8886) |
| both clear | install [`nmi_reply_scout`](address:874B) for scout ACK reception |""")


d.subroutine(0x874B, 'nmi_reply_scout', title='RX reply-scout handler', description="""NMI handler installed before the reply-scout reception phase.
Tests `SR2` bit 0 (`AP`) for an incoming address; on `AP` clear
falls through to `tx_error`. Otherwise reads the first RX byte
(destination station) and compares it against the workspace copy
[`tx_src_stn`](address:0D22). On mismatch branches to
[`reject_reply`](address:8773); on match installs
[`nmi_reply_cont`](address:875F) as the next NMI handler via
[`install_nmi_handler`](address:0D11) (low-byte only -- the high
byte stays at `&87`).""")


d.subroutine(0x875F, 'nmi_reply_cont', title='RX reply continuation handler', description="""Reads the second byte of the reply scout (destination network)
and validates it is zero (local network). Loads `A=&76`, the low
byte of [`nmi_reply_validate`](address:8776), to install it as
the next NMI handler.

**Optimisation:** before installing, checks `SR1` bit 7 (`IRQ`
still asserted) via `BIT adlc_cr1` / `BMI`. When `IRQ` is still
set the next byte is already in the FIFO, so the routine falls
through directly to [`nmi_reply_validate`](address:8776) without
an intermediate `RTI`, avoiding NMI re-entry overhead for short
frames where all bytes arrive in quick succession.""")


d.subroutine(0x8773, 'reject_reply', title='Abandon reply scout (1-instruction trampoline)', description="""Single `JMP` to [`tx_result_fail`](address:88E2). Acts as a
near-target for the `BPL`/`BNE` exits scattered through
[`nmi_reply_scout`](address:874B),
[`nmi_reply_validate`](address:8776), and
[`nmi_scout_ack_src`](address:87BE) that need to abort the
reply path – the unconditional `JMP` at `&8773` takes them to
[`tx_result_fail`](address:88E2) (which stores the error and
returns to idle).

Seven inbound refs in total (one `JSR` plus six branches).""")


d.subroutine(0x8776, 'nmi_reply_validate', title='RX reply validation (Path 2 for FV/PSE interaction)', description="""Reads the source station and source network from the reply scout
and validates them against the original TX destination
([`tx_dst_stn`](address:0D20) /
[`tx_dst_net`](address:0D21)).

1. Check SR2 bit 7 (RDA) -- must see data available.
2. Read source station, compare to `tx_dst_stn`.
3. Read source network, compare to `tx_dst_net`.
4. Check SR2 bit 1 (FV) -- must see frame complete.

If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (`CR2=&A7` for RTS, `CR1=&44` for TX mode).""")


d.subroutine(0x87BE, 'nmi_scout_ack_src', title='TX scout ACK: write source address', description="""Continuation of the TX-side scout ACK. Reads our station ID from
the workspace copy [`tx_src_stn`](address:0D22), tests `TDRA`
via `SR1`, and writes `(station, network=0)` to the TX FIFO.

Then dispatches on bit 1 of [`rx_src_net`](address:0D3E) to
select the next NMI handler:

| Bit 1 | Handler |
|---|---|
| set   | immediate-op data NMI handler |
| clear | normal [`nmi_tx_data`](address:86E7) |

Installs the chosen handler via
[`set_nmi_vector`](address:0D0E). Shares the
[`tx_check_tdra_ready`](address:87C4) entry with
[`ack_tx`](address:82DF).""")


d.subroutine(0x87CE, 'data_tx_begin', title='Begin data-frame TX: install nmi_data_tx or alt', description="""Tests bit 1 of [`rx_src_net`](address:0D3E)
([`tx_flags`](address:0D4A)):

| Bit 1 | Path |
|---|---|
| set (immediate-op) | branch to `install_imm_data_nmi` to use the alternative handler |
| clear | install the [`nmi_data_tx`](address:87E3) alt-entry at `&87EB` (lo=`&EB`, hi=`&87`) into the NMI vector. The alt-entry skips the page-counter check and goes straight to the byte-count load |

Single caller (`&8339` inside [`ack_tx`](address:82DF)).""")


d.subroutine(0x87E3, 'nmi_data_tx', title='TX data phase: send payload', description="""NMI handler that transmits the data payload of a four-way
handshake. Loads bytes from `(open_port_buf),Y` (or from Tube
R3 in the immediate-op variant), writing pairs to the TX FIFO.
After each pair, decrements the byte counters
(`port_buf_len`/`port_buf_len_hi`):

| Condition | Action |
|---|---|
| `port_buf_len_hi = 0` (final partial page) | branch to `data_tx_last` (internal label) to send the remaining bytes and tail-call [`tx_last_data`](address:8723) |
| count > 0, `SR1` IRQ still set | tight loop: write another pair without returning from NMI |
| count > 0, `SR1` IRQ clear | return via `RTI` and wait for next NMI |

The alt-entry at `&87EB` (used by
[`data_tx_begin`](address:87CE)) skips the page-counter check
and starts at the byte-count load.""")


d.subroutine(0x8845, 'nmi_data_tx_tube', title='NMI handler: TX FIFO write from Tube buffer', description="""NMI continuation handler used during TX of a Tube-sourced data
frame. Tests SR1 TDRA via `BIT
econet_control1_or_status1`, writes the next pair of bytes from
the Tube buffer to the ADLC TX FIFO (the `tube_tx_fifo_write`
shared body at `&8848`), and either continues the tight inner loop
on a continuing IRQ or returns via `RTI`. Reached only via the NMI
vector after [`tx_prepare`](address:864A) installs it.""")


d.subroutine(0x8886, 'handshake_await_ack', title='Four-way handshake: switch to RX for final ACK', description="""Called via JMP from [`nmi_tx_complete`](address:872F) when bit 0
of [`tx_flags`](address:0D4A) is set (four-way handshake in
progress). Writes `CR1=&82` (`TX_RESET|RIE`) to switch the ADLC
from TX mode to RX mode, listening for the final ACK from the
remote station. Installs [`nmi_final_ack`](address:8892) as the
next NMI handler via [`set_nmi_vector`](address:0D0E).""")


d.subroutine(0x8892, 'nmi_final_ack', title='RX final ACK handler', description="""Receives the final ACK in a four-way handshake. Same validation
pattern as [`nmi_reply_validate`](address:8776):

1. Check AP, read dest_stn, compare to our station.
2. Check RDA, read dest_net, validate = 0.
3. Check RDA, read src_stn / src_net, compare to TX dest.
4. Check FV for frame completion.

On success, stores result=0 via
[`tx_result_ok`](address:88DE). On failure, error &41.""")


d.subroutine(0x88A6, 'nmi_final_ack_net', title='NMI handler: final-ACK source-net validation', description="""NMI continuation entry installed by `nmi_final_ack`. Polls SR2 for
RDA, reads the source-network byte from the ADLC RX FIFO, and
compares with the original TX destination network (`tx_dst_net`,
`&0D21`). On mismatch, branches to
[`tx_result_fail`](address:88E2). On match, falls through into
[`nmi_final_ack_validate`](address:88BA) for the source-station
check. Reached only via the NMI vector (no static caller).""", on_exit={'a': 'source-network byte read from FIFO'})


d.subroutine(0x88BA, 'nmi_final_ack_validate', title='Final ACK validation', description="""Continuation of [`nmi_final_ack`](address:8892). Tests `SR2`
for `RDA`, then reads the source station and source network
bytes from the RX FIFO, comparing each against the original TX
destination at [`tx_dst_stn`](address:0D20) and
[`tx_dst_net`](address:0D21). Finally tests `SR2` bit 1
(`FV`) for frame completion.

Any mismatch or missing `FV` branches to
[`tx_result_fail`](address:88E2). On success, falls through
to [`tx_result_ok`](address:88DE).""")


d.subroutine(0x88DE, 'tx_result_ok', title='TX completion handler', description="""Loads `A=0` (success) and branches unconditionally to
[`tx_store_result`](address:88E4) (`BEQ` is always taken since
A=0, skipping the `tx_result_fail` body at &88E2). This two-
instruction entry point exists so that `JMP` sites can target
the success path without needing to set `A`. Called from
[`ack_tx`](address:82DF) for final-ACK completion and from
[`nmi_tx_complete`](address:872F) for immediate-op completion
where no ACK is expected.""", on_exit={'a': '0 (TX success)'})


d.subroutine(0x88E2, 'tx_result_fail', title='TX failure: not listening', description="""Loads error code `&41` ("not listening") and falls through to
[`tx_store_result`](address:88E4). The most common TX-error
path – reached from 11 sites across the final-ACK validation
chain when the remote station doesn't respond or the frame is
malformed.""", on_exit={'a': "&41 ('not listening' TX error)"})


d.subroutine(0x88E4, 'tx_store_result', title='TX result store and completion', description="""Stores the TX result code (in `A`) at offset 0 of the TX control
block via `(nmi_tx_block),Y=0`. Sets
[`tx_complete_flag`](address:0D60) to `&80` to signal TX
completion to the foreground polling loop. Then jumps to
[`discard_reset_rx`](address:83E5) for a full ADLC reset and
return to idle RX-listen mode.""", on_entry={'a': 'result code (0=success, &40=jammed, &41=not listening)'})


d.subroutine(0x8900, 'tx_calc_transfer', title='Calculate transfer size and reclaim Tube buffer', description="""Inspects `RXCB[6..7]` (buffer end address byte 2 and high) to
detect a Tube buffer (high=`&FF`, byte 2 in `[&FE, &FF]`).

| Buffer type | Action |
|---|---|
| Tube | compute 4-byte transfer size by subtracting `RXCB[8..&B]` (start) from `RXCB[4..7]` (end); store via `(port_ws_offset),Y`; re-claim Tube via `JSR &0406` with claim type `&C2` |
| Non-Tube | fall through to `fallback_calc_transfer` for a 1-byte size subtraction without the Tube reclaim |

Three callers: [`scout_complete`](address:8112) (`&819A`),
[`rx_imm_peek`](address:84CE) (`&84DB`),
[`tx_ctrl_proc`](address:86A2) (`&86DD`).""", on_entry={'y': '0 -- caller convention'}, on_exit={'a': 'transfer status', 'c': 'set if Tube address claimed, clear otherwise'})


d.subroutine(0x898C, 'adlc_full_reset', title='ADLC full reset', description="""Performs a full ADLC hardware reset:

1. Writes `CR1=&C1` (`TX_RESET | RX_RESET | AC`) to put both TX
   and RX sections in reset with address-control enabled.
2. Configures `CR4=&1E` (8-bit RX word, abort extend, NRZ
   encoding).
3. Configures `CR3=&00` (no loopback, no AEX, NRZ, no DTR).
4. Falls through to [`adlc_rx_listen`](address:899B) to
   re-enter RX-listen mode.""", on_entry={}, on_exit={'a, x, y': 'clobbered'})


d.subroutine(0x899B, 'adlc_rx_listen', title='Enter RX-listen mode', description="""Configures the ADLC for passive RX-listen mode:

| Register | Value | Meaning |
|---|---|---|
| `CR1` | `&82` | `TX_RESET \\| RIE` – TX section held in reset, RX interrupts enabled |
| `CR2` | `&67` | `CLR_TX_ST \\| CLR_RX_ST \\| FC_TDRA \\| 2_1_BYTE \\| PSE` – clear all pending status, enable prioritised status |

This is the idle state where the ADLC listens for incoming scout
frames via NMI.""", on_entry={}, on_exit={'a, x': 'clobbered (control byte writes)', 'y': 'preserved'})


d.subroutine(0x89A6, 'wait_idle_and_reset', title='Wait for idle NMI state and reset Econet', description="""Service-13 (`&0D`) handler -- the post-hard-reset Econet
shutdown path. Reached via
[`svc_dispatch`](address:8E61) slot &0D. Checks
[`econet_init_flag`](address:0D62) to see if Econet has been
initialised; if not, skips straight to
[`adlc_rx_listen`](address:899B). Otherwise spins in a tight
loop comparing the NMI handler vector at
[`nmi_jmp_lo`](address:0D0C) /
[`nmi_jmp_hi`](address:0D0D) against the address of
[`nmi_rx_scout`](address:809B) to wait until the in-flight
NMI handler chain has unwound back to scout-listening.

When the NMI vector matches `nmi_rx_scout` again, falls through
to [`save_econet_state`](address:89B9) to clear the initialised
flags and re-enter RX-listen mode. (Service &0B 'NMI release'
is handled by the separate [`econet_restore`](address:806C).)""", on_entry={'a': '13 (service call number, &0D)'}, on_exit={'a, x, y': 'clobbered'})


d.subroutine(0x89B9, 'save_econet_state', title='Reset Econet flags and enter RX-listen', description="""Disables NMIs via `BIT master_intoff` (the Master 128 dedicated
INTOFF at &FE38), then clears
[`tx_complete_flag`](address:0D60) and
[`econet_init_flag`](address:0D62) by storing the current `A`
value. Sets `Y=5` (service-call workspace page) and jumps to
[`adlc_rx_listen`](address:899B) to configure the ADLC for
passive listening.

Used during the wait-idle-and-reset path (svc &0D) to safely
tear down the Econet state before another ROM can claim the
NMI workspace.""", on_entry={'a': 'value to store into tx_complete_flag / econet_init_flag (typically 0 to clear)'}, on_exit={'y': '5 (service-call workspace page)'})


d.subroutine(0x89CA, 'nmi_bootstrap_entry', title='Bootstrap NMI entry point (in ROM)', description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM shim at the start of the NFS workspace block. Unlike
the RAM shim (which uses a self-modifying `JMP` to dispatch to
different handlers), this one hardcodes
`JMP `[`nmi_rx_scout`](address:809B). Used as the initial
NMI handler before the workspace has been properly set up during
initialisation.

Same sequence as the RAM shim:

```6502
BIT master_intoff      ; INTOFF (Master 128 dedicated register)
PHA
TYA
PHA
LDA #romsel-bank
STA romsel
JMP nmi_rx_scout
```

The `BIT` of [`econet_station_id`](address:FE18) (INTOFF) at
entry and `BIT` of [`econet_nmi_enable`](address:FE20) (INTON)
before `RTI` in [`nmi_rti`](address:0D14) are essential for
edge-triggered NMI re-delivery.

The 6502 /NMI is falling-edge triggered; the Econet NMI-enable
flip-flop (IC97) gates the ADLC IRQ onto /NMI. INTOFF clears the
flip-flop, forcing /NMI high; INTON sets it, allowing the ADLC
IRQ through. This creates a guaranteed high-to-low edge on /NMI
even when the ADLC IRQ is continuously asserted (e.g. when it
transitions atomically from TDRA to frame-complete without
de-asserting). Without this mechanism,
[`nmi_tx_complete`](address:872F) would never fire after
[`tx_last_data`](address:8723).""")


d.subroutine(0x89D8, 'rom_set_nmi_vector', title='ROM copy of set_nmi_vector + nmi_rti', description="""ROM-resident version of the NMI-exit sequence; also the source
for the initial copy to RAM at
[`set_nmi_vector`](address:0D0E).

| RAM target | Function |
|---|---|
| [`set_nmi_vector`](address:0D0E) | writes both hi and lo bytes of the `JMP` target at [`nmi_jmp_lo`](address:0D0C) / [`nmi_jmp_hi`](address:0D0D) |
| [`nmi_rti`](address:0D14) | restores the original ROM bank, pulls `Y` and `A` from the stack, then `BIT` of [`econet_nmi_enable`](address:FE20) (INTON) to re-enable the NMI flip-flop before `RTI` |

The INTON creates a guaranteed falling edge on /NMI if the ADLC
IRQ is already asserted, ensuring the next handler fires
immediately.""")


d.subroutine(0x8B00, 'scan_remote_keys', title='Scan keyboard for remote-operation keys', description="""Uses OSBYTE `&7A` with `Y=&7F` to check whether remote-operation
keys (`&CE`..`&CF`) are currently pressed. If neither key is
detected, clears `svc_state` and `nfs_workspace` to zero via the
`clear_svc_and_ws` entry point (also used directly by
[`cmd_roff`](address:8AEA)). Called by `check_escape`.

`X` is saved into `nfs_workspace` across the OSBYTE call and
restored each iteration – the loop reuses `A` as the key-code
counter without needing `X`. `clear_svc_and_ws` is also entered
directly (label) by [`cmd_roff`](address:8AEA) with no
register pre-conditions.""", on_entry={'x': 'preserved by being saved to nfs_workspace and reloaded each iteration (no other preconditions)'}, on_exit={'a': '0 (when no key pressed -- the cleared path)', 'x': 'may be modified by OSBYTE', 'y': '&7F (left over from OSBYTE call setup)'})


d.subroutine(0x8B18, 'save_text_ptr', title='Save OS text pointer for later retrieval', description="""Copies `&F2`/`&F3` (`os_text_ptr`) into `fs_crc_lo` /
`fs_crc_hi`. Called by [`svc_4_star_command`](address:8C42)
and [`svc_9_help`](address:8C51) before attempting command
matches, and by `match_fs_cmd` during iterative help-topic
matching. Preserves `A` via `PHA`/`PLA`.""", on_exit={'a': 'preserved'})


d.subroutine(0x8BBB, 'help_print_nfs_cmds', title='*HELP NFS topic: print NFS-specific commands', description="""Loads `X=&35` (the offset of the first NFS-specific command in
`cmd_table_fs`) and tail-falls into
[`print_cmd_table`](address:8BC6) to emit the listing. Single
caller (the `*HELP` topic dispatch at `&8C6E`).""", on_exit={'x': '&35 + advance through the table'})


d.subroutine(0x8BC6, 'print_cmd_table', title='Print *HELP command listing with optional header', description="""| `V` flag | Action |
|---|---|
| set   | save `X`/`Y`, call [`print_version_header`](address:8C93) to show the ROM version string and station number, restore `X`/`Y` |
| clear | output a newline only |

Either path then falls through to
[`print_cmd_table_loop`](address:8BD5) to enumerate
commands.""", on_entry={'x': 'offset into cmd_table_fs', 'v': 'set=print version header, clear=newline only'})


d.subroutine(0x8BD5, 'print_cmd_table_loop', title='Enumerate and print command table entries', description="""Walks the ANFS command table from offset `X`, printing each
command name padded to 9 characters followed by its syntax
description.

| Entry byte bit 7 | Treatment |
|---|---|
| clear | print this entry |
| set   | mark end-of-table |

The syntax descriptor byte's low 5 bits index into
`cmd_syntax_table`; index `&0E` triggers special handling that
lists shared command names in parentheses. Calls
[`help_wrap_if_serial`](address:8C29) to handle line
continuation on serial output streams. Preserves `Y`.""", on_entry={'x': 'offset into cmd_table_fs'})


d.subroutine(0x8BD8, 'loop_next_entry', title='*HELP table walker per-entry body', description="""Loads `cmd_table_fs,X` (entry byte at offset `X`):

| Bit 7 | Target |
|---|---|
| clear | `print_indent` (continue with this entry) |
| set   | `JMP done_print_table` (end of table reached) |

Single caller (the `BNE` retry at `&8C22` in
[`print_cmd_table`](address:8BC6)'s outer loop).""", on_entry={'x': 'current cmd_table_fs offset'})


d.subroutine(0x8C06, 'loop_print_syntax', title='Per-character body of *HELP syntax string emit', description="""`INY` / load `syn_opt_dir,Y` / detect terminator or
line-break:

| Byte | Action |
|---|---|
| `0`  | terminator – stop |
| `CR` (`&0D`) | line-break – wrap |
| other | print the character |

Two callers: the `BNE` at `&8C13` (continue with current char)
and the `BEQ` at `&8C19` (fall-through from the line-wrap
path).""", on_entry={'y': 'current index into syn_opt_dir'})


d.subroutine(0x8C25, 'done_print_table', title='Cleanup epilogue for print_cmd_table', description="""Pops the saved `P` and `Y` registers off the stack and `RTS`.
Used as the shared exit for [`print_cmd_table`](address:8BC6)
after it has emitted a help listing or detected end-of-table.
Single caller (the `BEQ` at `&8BDD` in
[`print_cmd_table`](address:8BC6) when `V` was set on entry,
indicating the saved state needs restoring).""", on_exit={'y': 'restored from stack', 'p (flags)': 'restored from stack'})


d.subroutine(0x8C29, 'help_wrap_if_serial', title='Wrap *HELP syntax lines for serial output', description="""Checks the output destination via [`vdu_mode`](address:0355):

| Stream | Action |
|---|---|
| 0 (VDU) | return immediately |
| 3 (printer) | return immediately |
| serial | output newline + 12 spaces of indentation to align continuation lines with the syntax-description column |""", on_exit={'y': 'preserved (saved/restored via PHY/PLY)', 'a': 'clobbered (last char written via OSWRCH)'})


d.subroutine(0x8C64, 'svc_return_unclaimed', title='Restore Y and return service-call unclaimed', description="""Reloads `Y` from `ws_page` (the saved command-line offset) and
`RTS` to the caller without clearing `A` – preserving the
original service number so the next ROM in the chain sees the
unclaimed call.

Reached from the four service-handler escape paths at `&8C4C`,
`&8C91`, `&8CD5`, and `&95BE` that hand a request back to MOS
without acting on it.""", on_exit={'y': 'ws_page (restored command-line offset)'})


d.subroutine(0x8C93, 'print_version_header', title='Print ANFS version string and station number', description="""Uses an inline string after `JSR` to
[`print_inline`](address:9261): `CR + "Advanced NFS 4.21" +
CR`. After the inline string, `JMP`s to
[`print_station_id`](address:90C7) to append the local Econet
station number.""", on_entry={}, on_exit={'a, x, y': 'clobbered (print_inline + print_station_id)'})


d.subroutine(0x8CAD, 'get_ws_page', title='Read workspace page number for current ROM slot', description="""Indexes into the MOS per-ROM workspace table
[`rom_ws_pages`](address:0DF0) using `romsel_copy` (`&F4`) as
the ROM slot. Holds a copy of the slot byte in `Y`, then runs a
`ROL` / `PHP` / `ROR` / `PLP` sequence at `&8CB3`–`&8CB6` that
restores `A` to the original byte while leaving the saved-flags
register reflecting bit 6 of the original byte (the ADLC-absent
flag). Falls through to whichever caller-specific tail follows.""", on_exit={'a': 'workspace page byte (preserved through ROL/ROR)', 'y': 'same byte (set by `TAY` before the rotate trick)', 'n': 'set to bit 6 of the original byte (ADLC-absent flag)'})


d.subroutine(0x8CBD, 'setup_ws_ptr', title='Set up zero-page pointer to workspace page', description="""Calls [`get_ws_page`](address:8CAD) to read the page number,
stores it as the high byte in `nfs_temp` (`&CD`), and clears the
low byte at `&CC` to zero. This gives a page-aligned pointer used
by FS initialisation and [`cmd_net_fs`](address:8B23) to
access the private workspace.""", on_exit={'a': '0', 'y': 'workspace page number'})


d.subroutine(0x8CFD, 'notify_new_fs', title='Notify OS of filing-system selection', description="""Loads `A=6` (FSCV reason: filing system change) and falls
through to [`call_fscv`](address:8CFF), which `JMP`-indirects
through `vec_fscv` to invoke the FSCV vector. The FSCV handler
returns to whatever invoked `notify_new_fs` -- this is a
fire-and-forget notification, not a return-to-caller call.

Single caller (&8b60 inside the FS-selection sequence).""", on_entry={}, on_exit={'a': '6 (clobbered by FSCV handler)'})


d.subroutine(0x8CFF, 'call_fscv', title='Dispatch to filing-system control vector (FSCV)', description="""Indirect `JMP` through `FSCV` at [`vec_fscv`](address:021E),
providing OS-level filing-system services such as FS-selection
notification (`A=6`) and `*RUN` handling.

Also contains [`issue_svc_15`](address:8D02) and
`issue_svc_osbyte` entry points that issue paged-ROM service
requests via OSBYTE `&8F`.""", on_entry={'a': 'FSCV reason code'})


d.subroutine(0x8D09, 'svc_dispatch_idx_2', title='svc_dispatch table[2] handler', description="""Reached only via PHA/PHA/RTS dispatch from the
[`svc_dispatch`](address:89ED) table at index 2. Pushes `Y`
onto the stack via `PHY`, sets `X=&11` (CMOS RAM offset for the
Econet station-flags byte), calls [`osbyte_a1`](address:8E9A) to
read it, then ANDs the result with `&01` (bit 0 = "use page &0B
fallback") and pulls `Y` back. Used by the workspace-allocation
path to discover whether the user has overridden the default
private workspace base.""", on_exit={'a': '0 or 1 (CMOS bit 0 of station-flags byte)'})


d.subroutine(0x8D24, 'check_credits_easter_egg', title='Easter egg: match *HELP keyword to author credits', description="""Matches the `*HELP` argument against a keyword embedded in the
credits data at `credits_keyword_start`. Starts matching from
offset 5 in the data (`X=5`) and checks each byte against the
command-line text until a mismatch or `X` reaches `&0D`.

On a full match, prints the ANFS author credits:

- B Cockburn
- J Dunn
- B Robertson
- J Wills

Each name is terminated by `CR`.""")


d.subroutine(0x8E21, 'clear_if_station_match', title='Clear hazel_fs_network if it matches the bridge status byte', description="""Calls [`init_bridge_poll`](address:ABE9) (returning the
[`spool_control_flag`](address:0D71) bridge status byte in `A`,
either freshly populated or already cached from a previous
invocation) and EORs it with
[`hazel_fs_network`](address:C001). When the two match (`EOR`
result is zero), zeroes `hazel_fs_network` so subsequent FS
operations fall back to the local network.

Called by [`cmd_iam`](address:8D91) and
[`osword_13_set_station`](address:A9EC) when reconciling a
parsed file-server station address against the bridge state.""", on_exit={'a': '0 if cleared (match), bridge-XOR-network otherwise'})


d.subroutine(0x8E2D, 'check_urd_prefix', title="Branch to *RUN handler if first arg char is '&'", description="""Reads the first character of the parsed command text via
`(fs_crc_lo),Y`:

| First char | Path |
|---|---|
| `'&'` (URD prefix marker) | `JMP cmd_run_via_urd` |
| any other | fall through to `pass_send_cmd` (send as normal FS request) |

Single caller (the FS command-name post-match path at
`&9597`).""")


d.subroutine(0x8E3C, 'send_cmd_and_dispatch', title='Send FS command and dispatch the reply', description="""1. `JSR save_net_tx_cb` to set up and transmit the command.
2. Read the reply function code from
   [`hazel_txcb_network`](address:C103).

| Reply code | Action |
|---|---|
| `0`     | branch to the no-reply path (`dispatch_rts`) |
| non-zero | load [`hazel_txcb_data`](address:C105) (first reply byte), `Y=&25` (dispatch offset for the standard reply table), continue into the reply-dispatch chain |

Two callers: the fall-through from
[`check_urd_prefix`](address:8E2D) (`&8E1F` via
`pass_send_cmd`) and the `JMP` from `send_fs_request` (`&9460`).""", on_entry={'y': 'extra dispatch offset (0 from send_fs_request, non-zero for some specialised paths)'})


d.subroutine(0x8E5B, 'dir_op_dispatch', title='Dispatch directory operation via PHA/PHA/RTS', description="""Validates `X < 5` and sets `Y = &18` as the dispatch offset,
then falls through into [`svc_dispatch`](address:8E61). The
`INX`/`DEY`/`BPL` loop in
[`svc_dispatch`](address:8E61) then settles `X_final =
X_caller + Y + 1`, landing on indices `&19..&1D` of the
[`svc_dispatch_lo`](address:89ED) /
[`svc_dispatch_hi`](address:8A20) tables. Those slots map to
the language-reply handlers `lang_0_insert_key`
(idx `&19`) through `lang_4_validated` (idx `&1D`).

(In 4.18 the offset was `&0E`, reaching indices 15..19. The 4.21
shift to `&18` puts the targets ten slots higher in the rebuilt
dispatch table.)""", on_entry={'x': 'directory operation code (0-4)'})


d.subroutine(0x8E98, 'read_cmos_byte_0', title='Read CMOS RAM byte 0 (Master 128)', description="""Sets `X=0` and falls through to [`osbyte_a1`](address:8E9A),
which issues OSBYTE `&A1` to read CMOS RAM byte 0 – the
file-system / language byte holding the default boot mode and FS
selection.

Single caller (`&8FBB`, inside
[`nfs_init_body`](address:8F38)'s CMOS-read sequence).""", on_exit={'y': 'CMOS byte 0 (returned by OSBYTE &A1)'})


d.subroutine(0x8ED2, 'osbyte_x0_y0', title='OSBYTE wrapper with X=0, Y=0', description="""Sets `X=0` and `Y=0` then branches to `jmp_osbyte`. Called from
the Econet OSBYTE dispatch chain to handle OSBYTEs that require
both `X` and `Y` cleared. The unconditional `BEQ` (after `LDY
#0` sets `Z`) reaches the `JMP osbyte` instruction.""", on_entry={'a': 'OSBYTE number'}, on_exit={'x': '0', 'y': '0'})


d.subroutine(0x8EF0, 'store_ws_page_count', title='Record workspace page count (capped at &D3)', description="""Stores the workspace allocation from service 1 into offset `&0B` of
the receive control block, capping the value at `&D3` to prevent
overflow into adjacent workspace areas. Called by
[`svc_2_priv_ws`](address:8F10) after issuing the
absolute workspace claim service call.""", on_entry={'y': 'workspace page count from service 1'})
d.entry(0x8EFE)
d.entry(0x8F10)
d.entry(0x8F38)


d.subroutine(0x8F10, 'svc_2_priv_ws', title='Service-2 page-allocation prologue', description="""Reads CMOS byte `&11` to test bit 2 of the saved Econet status;
either advances the caller's first-available-page (`Y`) by 2 and
uses it, or forces page `&0B` as a fallback. Sets `net_rx_ptr_hi` /
`nfs_workspace_hi` to the chosen page pair, clears the corresponding
lo bytes, and calls [`get_ws_page`](address:8CAD). If the resulting
page is `>= &DC`, branches to the helper at
[`&8EFE`](address:8EFE) which publishes the page into
`rom_ws_pages[romsel_copy]` with bit 7 masked off.

This routine handles only the workspace-page allocation half of
service 2. The bring-up remainder (station ID, FS workspace zero,
`cmd_net_fs`, [`init_adlc_and_vectors`](address:903C)) lives at
[`nfs_init_body`](address:8F38) and is dispatched separately – see
the comment block above.""", on_entry={'y': 'first available private workspace page'})


d.subroutine(0x8F38, 'nfs_init_body', title='ANFS initialisation body', description="""Reached only via PHA/PHA/RTS dispatch (table index 22 in the
svc_dispatch table at `&89ED` / `&8A20`). Carries out the bring-up
sequence after page allocation:

- Clears `ws_page` / `tx_complete_flag` and the receive-block
  remote-op flag.
- On warm reset (`last_break_type` non-zero) and `fs_flags` bit 4
  set, calls [`setup_ws_ptr`](address:8CBD) and zeroes the FS
  workspace page in a 256-byte loop.
- Calls [`copy_ps_data_y1c`](address:B3D5) to install the printer-
  server template.
- Reads CMOS bytes `&01..&04` via `osbyte_a1`, storing each into
  the workspace identity block at `nfs_workspace+{0..3}`.
- Reads CMOS byte `&11` (Econet station): if zero, prints
  `Station number in CMOS RAM invalid. Using 1 instead!` and
  defaults to station 1.
- Stores station ID into the receive block.
- Calls `cmd_net_fs` to select ANFS as the active filing system,
  then [`init_adlc_and_vectors`](address:903C) to install NETV /
  FSCV / etc., `handle_spool_ctrl_byte` and `init_bridge_poll`
  for protection setup.

Returns via `RTS` at `&903B`.

Reached via Master 128 service call `&27` (= 39 decimal),
documented in the *Advanced Reference Manual for the BBC Master*:

> Reset has occurred. Call made after hard reset. Mainly for
> Econet Filing system so that it can claim NMIs. This call is
> now required since the MOS no longer offers workspace on a
> soft BREAK. A Sideways ROM should therefore re-initialise
> itself.

The full set of Master 128 service calls ANFS handles, dispatched
via the CMP/SBC normalisation chain in
[`service_handler`](address:8A54):

| svc        | idx   | handler                   | purpose                |
| ---------- | ----- | ------------------------- | ---------------------- |
| `&00..&0C` | 1..13 | (svc-1..12 handlers)      | service-1 .. service-12 |
| `&12`      | 14    | `svc_18_fs_select`        | FS select              |
| `&18`      | 15    | `match_on_suffix`         | Interactive HELP       |
| `&21`      | 16    | `raise_y_to_c8`           | static ws claim        |
| `&22`      | 17    | `set_rom_ws_page`         | dynamic ws offer       |
| `&23`      | 18    | `store_ws_page_count`     | top-of-static-ws       |
| `&24`      | 19    | `noop_dey_rts`            | dynamic ws claim (1 pg) |
| `&25`      | 20    | `copy_template_to_zp`     | FS name + info reply   |
| `&26`      | 21    | `svc_26_close_all_files`  | close all files        |
| `&27`      | 22    | `nfs_init_body` (this)    | reset re-init          |
| `&28`      | 23    | `print_fs_ps_help` | *CONFIGURE option      |
| `&29`      | 24    | `svc_29_status`   | *STATUS option         |

Everything else (svc `&0D..&11`, `&13..&17`, `&19..&20`, `&2A+`)
falls through to
[`dispatch_svc_state_check`](address:8ACE) with `A := 0` and
dispatches to idx 1 = `dispatch_rts` (no-op) – deliberately
ignoring svc `&15` (100 Hz poll), svc `&2A` (language ROM
startup), etc.""")

d.label(0x8FB8, 'done_alloc_handles')


d.subroutine(0x903C, 'init_adlc_and_vectors', title='Initialise ADLC and install extended vectors', description="""Reads the ROM pointer table via OSBYTE `&A8`, writes vector
addresses and ROM ID into the extended vector table for `NETV`
and one additional vector, then restores any previous FS context
via [`restore_fs_context`](address:9064). Falls through into
[`write_vector_entry`](address:904F).""", on_exit={'a, x, y': 'clobbered (falls through into write_vector_entry)'})


d.subroutine(0x904F, 'write_vector_entry', title='Install extended-vector table entries', description="""Copies vector addresses from the dispatch table at
`svc_dispatch_lo_offset+Y` into the MOS extended-vector table
pointed to by `fs_error_ptr`. For each entry, writes address low,
high, then the current ROM ID from `romsel_copy` (`&F4`). Loops
`X` times.

After the loop, stores `&FF` at
[`bridge_status`](address:0D72) as an installed flag, calls
`deselect_fs_if_active` and [`get_ws_page`](address:8CAD) to
restore FS state.""", on_entry={'x': 'number of vectors to install', 'y': 'starting offset in extended vector table'}, on_exit={'y': 'workspace page number + 1'})


d.subroutine(0x9064, 'restore_fs_context', title='Restore FS context from HAZEL into RX block', description="""Copies 8 bytes (offsets 2..9) from the HAZEL FS state block into
the receive control block at `(net_rx_ptr)+Y`. The source uses
the [`hazel_minus_2`](address:BFFE) indexing-base trick:
`LDA hazel_minus_2,Y` with `Y` running 9 down to 2 lands at
`&C007..&C000` (the [`hazel_fs_station`](address:C000) block --
station, network, saved station, CSD/lib slots, FS flags, etc.).
Restores those bytes into the RX control block when the caller
needs to re-publish the FS context (e.g. after a flip-set boot).

Called by [`svc_2_priv_ws`](address:8F10) during init,
`deselect_fs_if_active` during FS teardown, and
`flip_set_station_boot`.""", on_exit={'a, y': 'clobbered (loop counter / data byte)'})


d.subroutine(0x9071, 'fscv_6_shutdown', title='Deselect filing system and save workspace', description="""If the filing system is currently selected (bit 7 of
[`fs_flags`](address:0D6C) set):

1. Closes all open FCBs.
2. Closes `*SPOOL`/`*EXEC` files via OSBYTE `&77`.
3. Saves the FS workspace to page `&10` shadow with checksum.
4. Clears the selected flag.""")


d.subroutine(0x909E, 'verify_ws_checksum', title='Verify workspace checksum integrity', description="""Sums bytes 0..`&76` of the workspace page via the zero-page
pointer at `&CC`/`&CD` and compares with the stored value at
offset `&77`. On mismatch, raises a 'net sum' error (`&AA`) via
[`error_net_checksum`](address:90B5).

The checksummed page holds open-file information (preserved when
ANFS is not the current filing system) and the current printer
type. Can only be reset by a control-BREAK.

Preserves `A`, `Y`, and processor flags using `PHP`/`PHA`. Called
by 5 sites across `format_filename_field`, `adjust_fsopts_4bytes`,
and `start_wipe_pass` before workspace access.""", on_exit={'a': 'preserved (PHA/PLA)', 'y': 'preserved', 'p (flags)': 'preserved (PHP/PLP)'})


d.subroutine(0x90B5, 'error_net_checksum', title="Raise 'net checksum' BRK error", description="""Loads error code `&AA` and tail-calls `error_bad_inline` with the
inline string 'net checksum'. Reached when
[`ensure_fs_selected`](address:8B4D) (auto-select path)
cannot bring ANFS up, or when
[`verify_ws_checksum`](address:909E) detects that the saved
workspace checksum at offset `&77` doesn't match the live sum –
only resettable by a control-BREAK. Never returns.""")


d.subroutine(0x90C7, 'print_station_id', title='Print Econet station number and clock status', description="""Uses [`print_inline`](address:9261) to output `'Econet
Station '`, then reads the station ID from offset 1 of the
receive control block and prints it as a decimal number via
`print_num_no_leading`. Tests ADLC status register 2
([`adlc_cr2`](address:FEA1)) to detect the Econet clock; if
absent, appends `' No Clock'` via a second inline string.
Finishes with `OSNEWL`.

Called by [`print_version_header`](address:8C93) and
[`svc_3_autoboot`](address:8CC7).""", on_exit={'a, x, y': 'clobbered (print_inline + print_num_no_leading + OSNEWL)'})


d.subroutine(0x91F9, 'print_newline_no_spool', title='Print CR via OSASCI, bypassing any open *SPOOL file', description="""Loads `A=&0D` and falls into
[`print_char_no_spool`](address:91FB). The underlying
mechanism temporarily writes `0` to the `*SPOOL` file handle
(OSBYTE `&C7` with `X=0`, `Y=0`) so the printed `CR` is not
captured by spool, then restores the previous handle on exit.

Called from [`service_handler`](address:8A54) (`&8A7C`) after
the `'Bad ROM <slot>'` message, and from two other diagnostic
sites (`&8E10`, `&9D3E`).""", on_entry={}, on_exit={'a, x, y, p': 'preserved (print_char_no_spool brackets the call with full register save/restore via PHA/PHP/PLP/PLA)'})


d.subroutine(0x91FB, 'print_char_no_spool', title='Print A via OSASCI, bypassing any open *SPOOL file', description="""Pushes the caller's flags, then forces `V=1` via the `BIT &9769`
/ `BVS` trick (`&9769` is a constant `&FF` byte in ROM). Saves
`X`, `Y`, `A` and a copy of the (now `V=1`) flags.

1. Calls OSBYTE `&C7` with `X=0`, `Y=0` to write `0` to the
   `*SPOOL` file handle, returning the previous handle in `X`.
2. If the previous handle was in the NFS-issued range
   `&21..&2F`, calls OSBYTE `&C7` again with `X=OLD`, `Y=0` to
   **restore** the spool *before* the print (so the print is
   captured); otherwise leaves spool closed for the duration of
   the print.
3. `PLP`s the inner `P`, then routes to OSASCI (the `BIT` trick
   set `V=1`, so the `BVC` at `&9220` is not taken).
4. Final OSBYTE `&C7` with `Y=&FF` either no-ops (if spool
   already restored) or writes `OLD` back (if it was deferred).
5. Pulls `A`, `Y`, `X`, `P` and returns.

Eight inner-ROM callers: `&925F`, `&92A4`, `&9D30`, `&9D5C`,
`&B21F`, `&B2F9`, `&B321`, `&B752`.""", on_entry={'a': 'byte to print as ASCII char (CR is translated by OSASCI)'})


d.subroutine(0x9201, 'print_byte_no_spool', title='Print A via OSWRCH (raw, no CR translation), bypass *SPOOL', description="""As [`print_char_no_spool`](address:91FB) but the inner
`PHP`/`CLV` at `&9201` forces `V=0` in the saved flags, so the
`BVC` at `&9220` takes the `OSWRCH` branch instead of `OSASCI`.

Used when the caller wants to emit a raw byte (e.g. a VDU
control code) without `CR` translation. Sole caller in this ROM
is at `&8DE6`.""", on_entry={'a': 'raw byte to print via OSWRCH'})


d.subroutine(0x9236, 'print_hex_byte', title='Print A as two hexadecimal digits', description="""Saves `A` on the stack, shifts right four times to isolate the
high nybble, calls [`print_hex_nybble`](address:923F) to
print it, then restores the full byte and falls through to
[`print_hex_nybble`](address:923F) for the low nybble.

Callers: `print_5_hex_bytes`, [`cmd_ex`](address:B103),
[`cmd_dump`](address:BD41), and `print_dump_header`.""", on_entry={'a': 'byte to print'}, on_exit={'a': 'original byte value'})


d.subroutine(0x923F, 'print_hex_nybble', title='Print low nybble of A as hex digit', description="""Masks `A` to the low 4 bits, then converts to ASCII:

1. Adds 7 for letters `A`..`F` (via `ADC #6` with carry set from
   the `CMP`).
2. `ADC #&30` for the final `'0'`..`'F'` character.
3. Outputs via `JMP OSASCI`.""", on_entry={'a': 'value (low nybble used)'})


d.subroutine(0x9269, 'loop_next_char', title='print_inline pointer-advance step', description="""`INC fs_error_ptr` (lo); on overflow `INC fs_crflag` (hi). Single
caller (the loop tail at `&9284` inside
[`print_inline`](address:9261)). Falls through to `load_char`
which reads the next inline-string byte.""")


d.subroutine(0x92B2, 'parse_addr_arg', title='Parse decimal or hex station address argument', description="""Reads characters from the command argument at `(fs_crc_lo),Y`.
Supports `&` prefix for hex, `.` separator for net.station
addresses, and plain decimal. Returns the result in `fs_load_addr_2`
(and `A`). Raises [`Bad hex`](address:934A), `Bad number`,
[`Bad station number`](address:9357), and overflow errors as
appropriate. The body uses the standard 6502 idioms: `ASL ASL ASL
ASL` + `ADC` for hex-digit accumulation, and `result*2 + result*8`
for decimal `*10`. Two named callers: from `&A3C9` and `&A3DE`.""", on_entry={'y': 'index into command-string buffer at (fs_crc_lo),Y', 'a': 'ignored'}, on_exit={'c': 'set if a number was parsed'})


d.subroutine(0x934A, 'err_bad_hex', title="Raise 'Bad hex' BRK error", description="""Loads error code `&F1` and tail-calls `error_bad_inline` with
the inline string `'hex'` – `error_bad_inline` prepends `'Bad '`
to produce the final `'Bad hex'` message. Called from
[`parse_addr_arg`](address:92B2) and the `*DUMP` / `*LIST`
hex parsers when a digit is out of range. Never returns.""")


d.subroutine(0x939A, 'is_decimal_digit', title="Test for digit, '&', or '.' separator", description="""Compares `A` against `'&'` and `'.'` first; if either matches,
returns with carry set via the shared `return_from_digit_test` exit.
Otherwise falls through to
[`is_dec_digit_only`](address:93A2) for the `'0'`..`'9'`
range test.

Called by [`cmd_iam`](address:8D91),
[`cmd_ps`](address:B3AC), and
[`cmd_pollps`](address:B581) when parsing station
addresses.""", on_entry={'a': 'character to test'}, on_exit={'c': 'set if digit/&/., clear otherwise'})


d.subroutine(0x93A2, 'is_dec_digit_only', title="Test for decimal digit '0'..'9'", description="""Uses two `CMP`s to bracket-test `A` against the range
`&30..&39`:

1. `CMP #&3A` sets carry if `A >= ':'` (above digits).
2. `CMP #&30` sets carry if `A >= '0'`.

The net effect: carry set only for `'0'..'9'`. Called by
[`parse_addr_arg`](address:92B2).""", on_entry={'a': 'character to test'}, on_exit={'c': "set if '0'-'9', clear otherwise"})


d.subroutine(0x93AB, 'get_access_bits', title='Read and encode directory entry access byte', description="""Loads the access byte from offset &0E of the directory entry via
`(fs_options),Y`, masks to 6 bits (`AND #&3F`), then sets `X=4`
and branches to [`begin_prot_encode`](address:93B9) to map through
[`prot_bit_encode_table`](address:93C8). Called by
[`check_and_setup_txcb`](address:9D87) for owner and public
access.""", on_exit={'a': 'encoded access flags', 'x': '&FF + bits-set (left in this state by get_prot_bits fall-through)'})


d.subroutine(0x93B5, 'get_prot_bits', title='Encode protection bits via lookup table', description="""Masks `A` to 5 bits (`AND #&1F`), sets `X=&FF` to start at table
index 0, then enters the shared encoding loop at
[`begin_prot_encode`](address:93B9). Shifts out each source bit
and ORs in the corresponding value from
[`prot_bit_encode_table`](address:93C8). Called by
[`send_txcb_swap_addrs`](address:9C85) and
[`check_and_setup_txcb`](address:9D87).""", on_entry={'a': 'raw protection bits (low 5 used)'}, on_exit={'a': 'encoded protection flags'})


d.subroutine(0x93D3, 'set_text_and_xfer_ptr', title='Set OS text pointer then transfer parameters', description="""Stores `X`/`Y` into the MOS text pointer at `os_text_ptr` /
`os_text_ptr_hi` (`&F2`/`&F3`), then falls through to
[`set_xfer_params`](address:93D7) and
[`set_options_ptr`](address:93DD) to configure the full FS
transfer context. Two callers:
[`fscv_3_star_cmd`](address:A42F) (FSCV reason 3) and
[`ps_scan_resume`](address:B0FE) (PS scan tail).""", on_entry={'x': 'text pointer low byte', 'y': 'text pointer high byte'})


d.subroutine(0x93D7, 'set_xfer_params', title='Set FS transfer byte count and source pointer', description="""Stores `A` into `fs_last_byte_flag` (`&BD`) as the transfer byte
count, and `X`/`Y` into `fs_crc_lo`/`hi` (`&BE`/`&BF`) as the
source-data pointer. Falls through to
[`set_options_ptr`](address:93DD) to complete the
transfer-context setup.

Called by 5 sites across [`cmd_ex`](address:B103),
`format_filename_field`, and `gsread_to_buf`.""", on_entry={'a': 'transfer byte count', 'x': 'source pointer low', 'y': 'source pointer high'})


d.subroutine(0x93DD, 'set_options_ptr', title='Set FS options pointer and clear escape flag', description="""Stores `X`/`Y` into `fs_options`/`fs_block_offset` (`&BB`/`&BC`)
as the options-block pointer. Then enters
[`clear_escapable`](address:93E1) which uses
`PHP`/`LSR`/`PLP` to clear bit 0 of the escape flag at `&97`
without disturbing processor flags.

Called by `format_filename_field` and `send_and_receive`.""", on_entry={'x': 'options pointer low', 'y': 'options pointer high'})


d.subroutine(0x93E1, 'clear_escapable', title='Clear bit 0 of need_release_tube preserving flags', description="""PHP / LSR need_release_tube / PLP / RTS. Shifts bit 0 of
need_release_tube into carry while clearing it, then restores the
caller's flags so the operation is invisible to NZC-sensitive
code. Single caller (&9B72 in the recv-and-classify reply path).""")


d.subroutine(0x93E6, 'cmp_5byte_handle', title='Compare 5-byte handle buffers for equality', description="""Loops `X` from 4 down to 1, comparing each byte of
`addr_work+X` with `fs_load_addr_3+X` using `EOR`. Returns on
the first mismatch (`Z=0`) or after all 5 bytes match (`Z=1`).

Called by `send_txcb_swap_addrs` and `check_and_setup_txcb` to
verify station/handle identity.""", on_exit={'z': 'set if bytes 1..4 match (byte 0 is not compared)', 'a': 'EOR of last compared bytes', 'x': '0 if all matched, else mismatch index'})


d.subroutine(0x93F2, 'fscv_7_read_handles', title='FSCV reason 7: report FCB handle range', description="""Returns the FCB handle range to the caller: `X=&20` (lowest valid
handle) and `Y=&2F` (highest valid handle), then `RTS`. Reached
via the FSCV vector with reason code 7. Used by the OS to discover
which handle values this filing system claims.""", on_exit={'x': '&20 (first valid FCB handle)', 'y': '&2F (last valid FCB handle)'})


d.subroutine(0x93F7, 'set_conn_active', title='Set connection-active flag in channel table', description="""Saves registers on the stack, recovers the original `A` from the
stack via `TSX`/`LDA &0102,X`, then calls `attr_to_chan_index` to
find the channel slot. `ORA`s bit 6 (`&40`) into the channel
status byte at [`hazel_fcb_status`](address:C260)`+X`.
Preserves `A`, `X`, and processor flags via
`PHP`/`PHA`/`PLA`/`PLP`.

Called by `format_filename_field` and `adjust_fsopts_4bytes`.""", on_entry={'a': 'channel attribute byte'})


d.subroutine(0x940D, 'clear_conn_active', title='Clear connection-active flag in channel table', description="""Mirror of [`set_conn_active`](address:93F7) but `AND`s the
channel status byte with `&BF` (bit-6 clear mask) instead of
`ORA`ing. Uses the same register-preservation pattern:
`PHP`/`PHA`/`TSX` to recover `A`, then `attr_to_chan_index` to
find the slot. Shares the `done_conn_flag` exit with
[`set_conn_active`](address:93F7).""", on_entry={'a': 'channel attribute byte'})


d.subroutine(0x9437, 'error_bad_filename', title="Raise 'Bad file name' BRK error", description="""Loads error code `&CC` and tail-calls `error_bad_inline` with
the inline string `'file name'` – `error_bad_inline` prepends
`'Bad '` to produce the final `'Bad file name'` message. Used
by [`check_not_ampersand`](address:9446) and other filename
validators. Never returns.""")


d.subroutine(0x9446, 'check_not_ampersand', title="Reject '&' as filename character", description="""Loads the first character from the parse buffer at `&0E30` and
compares with `'&'` (`&26`). Branches to
[`error_bad_filename`](address:9437) if matched, otherwise
returns.

Also contains [`read_filename_char`](address:944E) which
loops reading characters from the command line into the TX
buffer at `hazel_txcb_data` (`&C105`), calling
`strip_token_prefix` on each byte and terminating on `CR`. Used
by [`cmd_fs_operation`](address:9425) and
[`cmd_rename`](address:94C5).""", on_exit={'a': 'first byte of parse buffer (preserved unchanged on the non-error path)'})


d.subroutine(0x944E, 'read_filename_char', title='Loop reading filename chars into TX buffer', description="""Per-character loop body of the filename-copy logic in
[`check_not_ampersand`](address:9446):

1. `JSR` to [`check_not_ampersand`](address:9446) to reject `'&'`.
2. Store the byte at [`hazel_txcb_data`](address:C105)`+X`
   (TX buffer area).
3. Increment `X`.
4. Branch to [`send_fs_request`](address:945E) on `CR`, or
   strip a BASIC token prefix via `strip_token_prefix` and
   re-enter the loop.

Three callers: the loop's own `BRA` at `&945C`, plus `&9435`
([`cmd_rename`](address:94C5)'s first-arg copy) and `&950F`
([`cmd_fs_operation`](address:9425)'s filename pickup).""", on_entry={'a': 'current character to copy', 'x': 'TX-buffer write index'}, on_exit={'x': 'advanced past the CR terminator'})


d.subroutine(0x945E, 'send_fs_request', title='Send FS command with no extra dispatch offset', description="""Loads `Y=0` (so dispatch lookups don't add an offset) and
tail-jumps to [`send_cmd_and_dispatch`](address:8E3C). Two
callers: [`read_filename_char`](address:944E)'s `BEQ` on
`CR` (`&9457`) and the `*RUN` argument-handling tail at
`&9537`.""")


d.subroutine(0x9463, 'copy_fs_cmd_name', title='Copy matched command name to TX buffer', description="""Scans backwards in `cmd_table_fs` from the current position to find
the bit-7 flag byte marking the start of the command name. Copies
each character forward into the TX buffer at `&C105` until the next
bit-7 byte (end of name), then appends a space separator.""", on_entry={'x': "byte offset within cmd_table_fs (just past the matched command's last name char)", 'y': 'current command-line offset (saved/restored)'}, on_exit={'x': 'TX buffer offset past name+space', 'y': 'command line offset (restored)', 'a': 'clobbered'})


d.subroutine(0x9483, 'parse_quoted_arg', title='Parse possibly-quoted filename argument', description="""Reads from the command line at `(fs_crc_lo),Y` (`&BE`). Handles
double-quote delimiters and stores the result in the parse
buffer at `&0E30`. Raises `'Bad string'` on unbalanced quotes.""", on_entry={'y': 'current offset within the command line'}, on_exit={'y': 'advanced past the parsed argument', 'a': 'clobbered (last byte read)'})


d.subroutine(0x973D, 'init_txcb_bye', title='Set up open receive for FS reply on port &90', description="""Loads `A=&90` (the FS command/reply port) and falls through to
[`init_txcb_port`](address:973F), which creates an open
receive control block: the template sets `txcb_ctrl` to `&80`,
then `DEC` makes it `&7F` (bit 7 clear = awaiting reply). The
NMI RX handler sets bit 7 when a reply arrives on this port,
which [`wait_net_tx_ack`](address:98BE) polls for.""", on_entry={})


d.subroutine(0x973F, 'init_txcb_port', title='Create open receive control block on specified port', description="""Calls [`init_txcb`](address:974B) to copy the 12-byte
template into the TXCB workspace at `&00C0`, then stores `A` as
the port (`txcb_port` at `&C1`) and sets `txcb_start` to 3. The
`DEC txcb_ctrl` changes the control byte from `&80` to `&7F`
(bit 7 clear), creating an open receive: the NMI RX handler
will set bit 7 when a reply frame arrives on this port, which
[`wait_net_tx_ack`](address:98BE) polls for.""", on_entry={'a': 'port number'})


d.subroutine(0x974B, 'init_txcb', title='Initialise TX control block from ROM template', description="""Copies 12 bytes from [`txcb_init_template`](address:9763) into the
TXCB workspace at `&00C0`. For the first two bytes (`Y=0,1`),
also copies the destination station/network from `&0E00` into
`txcb_dest` (`&C2`). Preserves `A` via `PHA`/`PLA`.

Called by 4 sites including [`cmd_pass`](address:8DD5),
[`init_txcb_port`](address:973F),
[`prep_send_tx_cb`](address:97B7), and `send_wipe_request`.""", on_exit={'a': 'preserved', 'x, y': 'clobbered (Y left at &FF on loop exit)'})


d.subroutine(0x976F, 'send_request_nowrite', title='Send read-only FS request (carry set)', description="""Pushes `A` and sets carry to indicate no-write mode, then
branches to `txcb_copy_carry_set` to enter the common TXCB copy,
send, and reply-processing path. The carry flag controls whether
a disconnect is sent on certain reply codes. Called by
`setup_transfer_workspace`.""", on_entry={'y': 'FS function code (stored as TX[1] = txcb_func by txcb_copy_carry_set)', 'a': 'saved on stack at entry (consumed by the txcb send/receive path)'})


d.subroutine(0x9773, 'send_request_write', title='Send read-write FS request (V clear)', description="""Clears `V` flag and branches unconditionally to
`txcb_copy_carry_clr` (via `BVC`, always taken after `CLV`) to
enter the common TXCB copy, send, and reply-processing path with
carry clear (write mode). Called by `do_fs_cmd_iteration` and
`send_txcb_swap_addrs`.""", on_entry={'y': 'FS function code (stored as TX[1] = txcb_func by txcb_copy_carry_clr)', 'a': 'request payload byte (used by the txcb send path)'})


d.subroutine(0x978A, 'save_net_tx_cb', title='Save FS state and send command to file server', description="""Copies station address and function code (`Y`) to the TX buffer,
builds the TXCB via [`init_txcb`](address:974B), sends the
packet through [`prep_send_tx_cb`](address:97B7), and waits
for the reply via [`recv_and_process_reply`](address:97CD).
`V` is clear for standard mode.""", on_entry={'y': 'FS function code (becomes TX[1] = txcb_func)', 'x': 'TX buffer payload length (prep_send_tx_cb uses X+5 as txcb_end)'}, on_exit={'a': 'FS reply status'})


d.subroutine(0x978B, 'save_net_tx_cb_vset', title='Save and send TXCB with V flag set', description="""Variant of [`save_net_tx_cb`](address:978A) for callers that
have already set `V`. Copies the FS station address from `&0E02`
to `&0F02`, then falls through to `txcb_copy_carry_clr` which
clears carry and enters the common TXCB copy, send, and reply
path.

Called by `check_and_setup_txcb`, `format_filename_field`, and
`cmd_remove`.""", on_entry={'y': 'FS function code', 'x': 'TX buffer payload length', 'v flag': "set by caller (selects this variant via the 'no CLV' fall-through from save_net_tx_cb)"}, on_exit={'a': 'FS reply status'})


d.subroutine(0x97B7, 'prep_send_tx_cb', title='Build TXCB from scratch, send, and receive reply', description="""Full send/receive cycle comprising two separate Econet
transactions:

1. Save flags, set reply port `&90`.
2. Call [`init_txcb`](address:974B), compute `txcb_end =
   X + 5`.
3. Dispatch on carry:

   | `C` | Path |
   |---|---|
   | set   | `handle_disconnect` |
   | clear | `init_tx_ptr_and_send` for a client-initiated four-way handshake (scout, ACK, data, ACK) to deliver the command |

4. After TX completes, the ADLC returns to idle RX-listen.
5. Falls through to [`recv_and_process_reply`](address:97CD)
   which waits for the server to independently initiate a new
   four-way handshake with the reply on port `&90`. There is no
   reply data in the original ACK payload.""", on_entry={'x': 'TX buffer payload length (txcb_end = X + 5)', 'y': 'FS function code (already stashed by the txcb-copy entry path)', 'c flag': 'set = disconnect path (handle_disconnect); clear = normal four-way handshake send'}, on_exit={'a': "FS reply status (or doesn't return on error)"})


d.subroutine(0x97CD, 'recv_and_process_reply', title='Receive FS reply and dispatch on status codes', description="""Waits for a server-initiated reply transaction. After the
command TX completes (a separate client-initiated four-way
handshake), calls [`init_txcb_bye`](address:973D) to set up
an open receive on port `&90` (`txcb_ctrl = &7F`). The server
independently initiates a new four-way handshake to deliver the
reply; the NMI RX handler matches the incoming scout against
this RXCB and sets bit 7 on completion.
[`wait_net_tx_ack`](address:98BE) polls for this.

Iterates over reply bytes:

| Byte / state | Action |
|---|---|
| `0` | terminates |
| `V` set | adjust by `+&2B` |
| non-zero, `V` clear | dispatch to `store_reply_status` |

Handles disconnect requests (`C` set from
[`prep_send_tx_cb`](address:97B7)) and `'Data Lost'`
warnings when channel status bits indicate pending writes were
interrupted.""", on_entry={'c flag': "set = disconnect mode (caller sent a disconnect scout; handle the server's matching reply)"}, on_exit={'a': 'FS reply status byte'})


d.subroutine(0x9850, 'lang_1_remote_boot', title='Language reply 1: remote-boot init / continue', description="""Reads the reply byte at `(net_rx_ptr),0`. If zero, branches to
[`init_remote_session`](address:9859) to (re)initialise the
remote session. Otherwise falls through to `done_commit_state`
which finalises the boot state byte for the active session.""")


d.subroutine(0x987E, 'lang_3_exec_0100', title="Language reply 3: raise 'Remoted' error at &0100", description="""Calls [`commit_state_byte`](address:B05F) to record the new state,
loads `A=0` and tail-calls [`error_inline_log`](address:99C0) with
the inline string `Remoted` followed by `&07` (BEL). Used by
remote-language replies that need to abort the current operation
with a terminal beep + error. Never returns.""")


d.subroutine(0x9895, 'raise_escape_error', title='Acknowledge escape and raise classified error', description="""Issues OSBYTE &7E (acknowledge_escape -- clears the escape condition
and runs any registered escape effects), loads A=6, and tail-jumps to
classify_reply_error which builds the Escape error. Reached from
&98EF (after recv_and_process_reply detects escape) and &B7DF
(cmd_wipe's per-iteration escape check). Never returns -- the
classify_reply_error path triggers BRK.""", on_exit={'a': '6 (Escape error code passed to classify_reply_error)'})


d.subroutine(0x989F, 'lang_4_validated', title='Language reply 4: validate remote session and apply', description="""Reads the first reply byte at `(net_rx_ptr),0`. If zero, branches
to [`init_remote_session`](address:9859) to set up a fresh remote
session. Otherwise reads the validation byte at offset `&80` and
the local stored value at workspace offset `&0E`; on mismatch,
the remote session is rejected.""")


d.subroutine(0x98AF, 'lang_0_insert_key', title='Language reply 0: insert remote keypress', description="""Reads the keycode from the reply at `(net_rx_ptr),&82` into `Y`,
sets `X=0`, calls [`commit_state_byte`](address:B05F) to record
the state change, and issues `OSBYTE &99` (insert into keyboard
buffer) to deliver the keypress to the local machine.""", on_entry={'a': 'ignored (entry from reply dispatch)'})


d.subroutine(0x98BE, 'wait_net_tx_ack', title='Wait for reply on open receive with timeout', description="""Despite the name, this does **not** wait for a TX acknowledgment.
It polls an open receive control block (bit 7 of `txcb_ctrl`,
set to `&7F` by [`init_txcb_port`](address:973F)) until the
NMI RX handler delivers a reply frame and sets bit 7.

Uses a three-level nested polling loop:

| Loop | Source | Default | Iterations |
|---|---|---|---|
| inner  | wraps from 0 | – | 256 |
| middle | wraps from 0 | – | 256 |
| outer  | [`rx_wait_timeout`](address:0D6E) | `&28` (40) | 40 |

Total: `256 × 256 × 40 = 2,621,440` poll iterations. At ~17
cycles per poll on a 2 MHz 6502, the default gives ~22 seconds.

On timeout, branches to `build_no_reply_error` to raise
`'No reply'`. Called by 6 sites across the protocol stack.""")


d.subroutine(0x9900, 'cond_save_error_code', title='Conditionally store error code to workspace', description="""Tests bit 7 of [`fs_flags`](address:0D6C) (FS-selected
flag):

| Bit 7 | Action |
|---|---|
| clear | return immediately |
| set   | store `A` into `hazel_fs_last_error` (`&0E09`) |

This guards against writing error state when no filing system
is active. Called internally by the error-classification chain
and by `error_inline_log`.""", on_entry={'a': 'error code to store'})


d.subroutine(0x9930, 'fixup_reply_status_a', title="Substitute 'B' for 'A' in reply status byte", description="""Reads the FS reply status byte at (net_tx_ptr,X). If it is 'A'
(Acknowledge with no error), substitutes 'B' so downstream code
treats it as a soft error. CLV before falling through into
mask_error_class to ensure the no-extended-error path is taken.""", on_entry={'x': 'indirect index into net_tx_ptr'}, on_exit={'a': 'reply status byte (with A->B substitution)', 'v': '0 (clear)'})


d.subroutine(0x993B, 'load_reply_and_classify', title='Load reply byte and classify error', description="""Single-byte prologue to
[`classify_reply_error`](address:993D): `LDA (net_tx_ptr,X)`
reads the FS reply status byte, then falls through. Single
caller (`&9B6C`, after a recv-and-classify path that already
has `X` set).""", on_entry={'x': 'indirect index into net_tx_ptr'})


d.subroutine(0x993D, 'classify_reply_error', title='Classify FS reply error code', description="""Forces `V=1` via `BIT always_set_v_byte` (signals the
extended-error path), masks the error code in `A` to 3 bits (the
error class 0..7), saves the class on the stack, and dispatches:

| Class | Path |
|---|---|
| 2 (station-related) | multi-line `build_no_reply_error` |
| other | `build_simple_error` |

Two callers: [`raise_escape_error`](address:9895) (with
`A=6`) and the FS reply dispatch at `&A0BD`.""", on_entry={'a': 'error code byte'})


d.subroutine(0x99DF, 'check_net_error_code', title="Translate net error: 'OK' → return, 'FS error' → append", description="""Reads the receive-attribute byte:

| Receive attribute | Action |
|---|---|
| non-zero | network error – branch to `handle_net_error` |
| zero, saved error = `&DE` (FS error code) | branch to `append_error_number` to add the FS-specific code to the error text |
| zero, saved error other | tail-jump to `&0100` (BRK error block) to trigger BRK and let MOS dispatch |""")


d.subroutine(0x9A3A, 'append_drv_dot_num', title="Append 'net.station' decimal string to error text", description="""Reads network and station numbers from the TX control block at
offsets 3 and 2. Writes:

1. A space separator.
2. The network number as decimal (if non-zero).
3. A dot (`'.'`).
4. The station number as decimal digits.

into the error-text buffer at the current position.""", on_entry={'x': 'error text buffer index'}, on_exit={'x': 'updated buffer index past appended text'})


d.subroutine(0x9A5E, 'append_space_and_num', title='Append space and decimal number to error text', description="""Writes a space character to the error text buffer
at the current position (fs_load_addr_2), then falls
through to append_decimal_num to convert the value
in A to decimal digits with leading zero suppression.""", on_entry={'a': 'number to append (0-255)'})


d.subroutine(0x9A69, 'append_decimal_num', title='Convert byte to decimal and append to error text', description="""Extracts hundreds, tens and units digits by three
successive calls to append_decimal_digit. Uses the
V flag to suppress leading zeros — hundreds and tens
are skipped when zero, but the units digit is always
emitted.""", on_entry={'a': 'number to convert (0-255)'})


d.subroutine(0x9A7A, 'append_decimal_digit', title='Extract and append one decimal digit', description="""Divides Y by A using repeated subtraction to extract
a single decimal digit. Stores the ASCII digit in the
error text buffer at fs_load_addr_2 unless V is set
and the quotient is zero (leading zero suppression).
Returns the remainder in Y for subsequent digit
extraction.""", on_entry={'a': 'divisor (100, 10, or 1)', 'y': 'number to divide', 'v': 'set to suppress leading zero'}, on_exit={'y': 'remainder after division', 'v': 'clear once a non-zero digit is emitted'})


d.subroutine(0x9B24, 'init_tx_ptr_and_send', title='Point TX at zero-page TXCB and send', description="""Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the
standard TXCB location in zero page), then falls
through to send_net_packet for transmission with
retry logic.""", on_exit={'a': 'TX result code (0 = success; &40 jammed; &41 not listening; etc.) -- see send_net_packet'})


d.subroutine(0x9B2C, 'send_net_packet', title='Transmit Econet packet with retry', description="""Two-phase transmit with retry. Loads retry count from
[`tx_retry_count`](address:0D6D) (default `&FF` = 255; 0
means retry forever). Each failed attempt waits in a nested
delay loop: `X` = TXCB control byte (typically `&80`), `Y` =
`&60`; total ~61 ms at 2 MHz (ROM-only fetches, unaffected by
video mode).

| Phase | Activation | Behaviour |
|---|---|---|
| 1 | always | runs the full count with escape disabled |
| 2 | only when `tx_retry_count = 0` | sets `need_release_tube` to enable escape checking, retries indefinitely |

With default `&FF`, phase 2 is never entered. Failures go to
[`load_reply_and_classify`](address:993B) (`'Line jammed'`,
`'Net error'`, etc.), distinct from the `'No reply'` timeout in
[`wait_net_tx_ack`](address:98BE).""", on_exit={'a': 'TX result (0 = success; non-zero = error class consumed by the BRK path)'})


d.subroutine(0x9B81, 'init_tx_ptr_for_pass', title='Set up TX pointer and send pass-through packet', description="""Copies the template into the TX buffer (skipping
&FD markers), saves original values on stack,
then polls the ADLC and retries until complete.""", on_exit={'a': 'TX result (from poll_adlc_tx_status)'})


d.subroutine(0x9B89, 'setup_pass_txbuf', title='Initialise TX buffer from pass-through template', description="""Copies 12 bytes from pass_txbuf_init_table into the
TX control block, pushing the original values on the
stack for later restoration. Skips offsets marked &FD
in the template. Starts transmission via
poll_adlc_tx_status and retries on failure, restoring
the original TX buffer contents when done.""", on_exit={'a': 'TX result (from poll_adlc_tx_status)'})


d.subroutine(0x9BB6, 'poll_adlc_tx_status', title='Wait for TX ready, then start new transmission', description="""1. Polls [`tx_complete_flag`](address:0D60) via `ASL`
   (testing bit 7) until set, indicating any previous TX
   operation has completed and the ADLC is back in idle
   RX-listen mode.
2. Copies the TX control-block pointer from `net_tx_ptr` to
   `nmi_tx_block`.
3. Calls [`tx_begin`](address:8589), which performs a
   complete transmission from scratch (copies destination from
   TXCB to scout buffer, polls for INACTIVE, configures ADLC
   `CR1=&44 RX_RESET|TIE`, `CR2=&E7 RTS|CLR`, runs the full
   four-way handshake via NMI).
4. After [`tx_begin`](address:8589) returns, polls the TXCB
   first byte until bit 7 clears (NMI handler stores result
   there).

Result in `A`:

| Code | Meaning |
|---|---|
| `&00` | success |
| `&40` | jammed |
| `&41` | not listening |
| `&43` | no clock |
| `&44` | bad control byte |""", on_exit={'a': 'TX result (&00 success / &40 jammed / &41 not listening / &43 no clock / &44 bad control byte)'})


d.subroutine(0x9BF5, 'load_text_ptr_and_parse', title='Copy text pointer from FS options and parse string', description="""Reads a 2-byte address from (fs_options)+0/1 into
os_text_ptr (&00F2), resets Y to zero, then falls
through to gsread_to_buf to parse the string at that
address into the &0E30 buffer.""", on_exit={'y': '0 (reset before GSINIT)'})


d.subroutine(0x9C00, 'gsread_to_buf', title='Parse command line via GSINIT/GSREAD into hazel_parse_buf', description="""Calls GSINIT to initialise string reading, then loops calling
GSREAD to copy characters into [`hazel_parse_buf`](address:C030)
until end-of-string. Appends a CR terminator and sets
`fs_crc_lo`/`hi` to point at the buffer for subsequent parsing
routines. (Pre-HAZEL ROMs used `fs_filename_buf` at &0E30; the
4.21 build uses HAZEL.)""", on_entry={'y': 'current command-line offset (consumed by GSINIT)'}, on_exit={'y': 'advanced past the parsed source'})


d.subroutine(0x9C22, 'filev_handler', title='FILEV vector handler: OSFILE', description="""Reached via the FILEV vector at `&0212`. Sets up transfer
parameters via [`set_xfer_params`](address:93D7), loads the OS text
pointer and parses the filename via
[`load_text_ptr_and_parse`](address:9BF5),
[`mask_owner_access`](address:B2CF) clears the FS-selection bits,
and [`parse_access_prefix`](address:B22F) records any access-byte
prefix. Routes by `fs_last_byte_flag` bit: positive (read /
display) goes to `check_display_type`; negative (write / save)
falls into the create-new-file path.""", on_entry={'a': 'OSFILE function code', 'x, y': 'control-block pointer (low, high)'})


d.subroutine(0x9C3E, 'do_fs_cmd_iteration', title='Execute one iteration of a multi-step FS command', description="""Called by match_fs_cmd for commands that enumerate
directory entries. Sets port &92, sends the initial
request via send_request_write, then synchronises the
FS options and workspace state (order depends on the
cycle flag at offset 6). Copies 4 address bytes,
formats the filename field, sends via
send_txcb_swap_addrs, and receives the reply.""", on_entry={'y': 'FS function code (matches send_request_write contract)'}, on_exit={'a': 'FS reply status'})


d.subroutine(0x9C85, 'send_txcb_swap_addrs', title='Send TXCB and swap start/end addresses', description="""If the 5-byte handle matches, returns
immediately. Otherwise sets port &92, copies
addresses, sends, waits for acknowledgment,
and retries on address mismatch.""", on_exit={'a': 'FS reply status (or unchanged if handles matched -- the routine returns early when no work is needed)'})


d.subroutine(0x9CB5, 'setup_dir_display', title='Compute display deltas and prep FS info request', description="""Iterates 4 times over paired (lo, hi) address words in the FS options
block at offsets &0E and &0A (loop body advances Y by 5 each pass).
For each pair, computes (high - low), saves both originals to
workspace at &00A6+Y (port_ws_offset region), and overwrites the
options entry with the difference so the caller can render 'load
addr', 'exec addr', 'length', etc. without redoing the subtraction.
Then copies 9 bytes of FS-options metadata into the TX buffer at
&C103, sets need_release_tube as the escapable flag, and stores FS
port &91 (info request) at &C102. Final tail-call dispatches the
request via send_request_write.""", on_exit={'a': '&91 (FS port for info request)', 'x, y': 'clobbered'})


d.subroutine(0x9D44, 'print_load_exec_addrs', title='Print exec address and file length in hex', description="""Prints the exec address as 5 hex bytes from
(fs_options) offset 9 downwards, then the file
length as 3 hex bytes from offset &0C. Each group
is followed by a space separator via OSASCI.""", on_exit={'a, x, y': 'clobbered (print_hex_byte + OSASCI)'})


d.subroutine(0x9D4F, 'print_5_hex_bytes', title='Print hex byte sequence from FS options', description="""Outputs `X+1` bytes from `(fs_options)` starting at offset `Y`,
decrementing `Y` for each byte (big-endian display order). Each
byte is printed as two hex digits via
[`print_hex_byte`](address:9236). Finishes with a trailing
space via OSASCI.

The default entry with `X=4` prints 5 bytes (a full 32-bit
address plus extent).""", on_entry={'x': 'byte count minus 1 (default 4 for 5 bytes)', 'y': 'starting offset in (fs_options)'})


d.subroutine(0x9D5F, 'copy_fsopts_to_zp', title='Copy FS options address bytes to zero page', description="""Copies 4 bytes from (fs_options) at offsets 2-5
into zero page at &00AE+Y. Used by
do_fs_cmd_iteration to preserve the current address
state. Falls through to skip_one_and_advance5 to
advance Y past the copied region.""", on_entry={'y': 'destination offset within the &00AE.. zero-page region (also indexes the source via (fs_options),Y)'}, on_exit={'y': 'advanced by 5 (via skip_one_and_advance5 fall-through)', 'a': 'clobbered'})


d.subroutine(0x9D6B, 'skip_one_and_advance5', title='Advance Y by 5', description="""Entry point one INY before advance_y_by_4, giving
a total Y increment of 5. Used to skip past a
5-byte address/length structure in the FS options
block.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset + 5', 'a, x': 'preserved'})


d.subroutine(0x9D6C, 'advance_y_by_4', title='Advance Y by 4', description="""Four consecutive INY instructions. Used as a
subroutine to step Y past a 4-byte address field
in the FS options or workspace structure.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset + 4'})


d.subroutine(0x9D71, 'copy_workspace_to_fsopts', title='Copy workspace reply data to FS options', description="""Copies bytes from the reply buffer at &0F02+Y
into (fs_options) at offsets &0D down to 2. Used
to update the FS options block with data returned
from the file server. Falls through to
retreat_y_by_4.""", on_entry={'y': 'current offset (controls how many bytes are copied before the loop terminates)'}, on_exit={'y': 'decremented by 4 (via retreat_y_by_4 fall-through)', 'a': 'clobbered'})


d.subroutine(0x9D7E, 'retreat_y_by_4', title='Retreat Y by 4', description="""Four consecutive DEY instructions. Companion to
advance_y_by_4 for reverse traversal of address
structures.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset - 4'})


d.subroutine(0x9D7F, 'retreat_y_by_3', title='Retreat Y by 3', description="""Three consecutive DEY instructions. Used by
setup_transfer_workspace to step back through
interleaved address pairs in the FS options block.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset - 3'})


d.subroutine(0x9D87, 'check_and_setup_txcb', title='Set up data-transfer TXCB and dispatch reply', description="""Compares the 5-byte handle via
[`cmp_5byte_handle`](address:93E6); if unchanged, returns.
Otherwise:

1. Computes start / end addresses with overflow clamping.
2. Sets the port and control byte.
3. Sends the packet.
4. Dispatches on the reply sub-operation code.""", on_exit={'a': 'FS reply sub-operation code (drives downstream dispatch)'})


d.subroutine(0x9DDC, 'dispatch_osword_op', title='OSWORD &13 sub-operation triage (1-7)', description="""Stores the sub-operation code in
[`hazel_txcb_data`](address:C105) and triages by value:

| Value | Target |
|---|---|
| `0..6` | `dispatch_ops_1_to_6` |
| `7`    | [`setup_dir_display`](address:9CB5) (`*INFO` expansion) |
| `> 7`  | `skip_if_error` (routes through [`finalise_and_return`](address:9FB6)) |

Single caller (`&9CB2` in the OSWORD `&13` handler entry).""", on_entry={'a': 'OSWORD sub-op code'})


d.subroutine(0x9E82, 'format_filename_field', title='Format filename into fixed-width display field', description="""Builds a 12-character space-padded filename at
[`filename_buf`](address:10F3) for directory listing
output. Sources the name from either the command line
or the [`fs_cmd_data`](address:0F05) reply buffer
depending on the value in [`fs_cmd_csd`](address:0F03).
Truncates or pads to exactly 12 characters.""", on_exit={'a, x, y': 'clobbered'})


d.subroutine(0x9FB1, 'close_all_fcbs', title='Close all FCBs (process_all_fcbs + finalise)', description="""Single-instruction wrapper: JSR process_all_fcbs to walk every FCB
slot and close each open file in turn, then fall through to
return_with_last_flag (which loads fs_last_byte_flag and finalises
caller state). Single caller (the OSFIND close-all path at &9EBA).""", on_exit={'a': 'fs_last_byte_flag (loaded by return_with_last_flag)'})


d.subroutine(0x9FB4, 'return_with_last_flag', title='Load last-byte flag and finalise', description="""Loads fs_last_byte_flag (&BD) into A and falls through to
finalise_and_return, which clears the receive-attribute byte and
restores caller's X/Y. The 12 inbound refs are mostly fall-through
exits from FS reply handlers that need to return the last-byte
status to their caller; only one site (&9FAE) reaches it via JSR.""", on_exit={'a': 'fs_last_byte_flag', 'x': 'fs_options (restored by finalise_and_return)', 'y': 'fs_block_offset (restored by finalise_and_return)'})


d.subroutine(0x9FB6, 'finalise_and_return', title="Clear receive-attribute and restore caller's X/Y", description="""Common 7-byte exit sequence used at the end of format_filename_field, several FS reply handlers, and match_fs_cmd. Saves A across a call to store_rx_attribute(0) (which clears the receive-attribute byte), then restores X from fs_options and Y from fs_block_offset before returning. Effectively: 'finish processing, clear network state, restore caller's pointers'.

One JSR caller (match_fs_cmd at &A599) plus 6 branch entries from format_filename_field's various exit paths.""", on_entry={'a': 'result code to return'}, on_exit={'a': 'preserved', 'x': 'fs_options low byte', 'y': 'fs_block_offset low byte'})


d.subroutine(0x9EAB, 'argsv_handler', title='ARGSV vector handler: OSARGS', description="""Reached via the ARGSV vector at `&0214`. Verifies the FS workspace
checksum, stores the result as the last-byte flag, and sets the FS
options pointer. Routes by `A`: positive (`bit 7 clear`) dispatches
to a sub-operation table; bit 6 vs bit 5 of `A` then selects
between read-and-write paths via further branching.""", on_entry={'a': 'OSARGS function code', 'x': 'control-block low byte', 'y': 'channel handle'})


d.subroutine(0x9FC2, 'osfind_close_or_open', title='OSFIND dispatch: close-all, close-one, or open', description="""Triages the OSFIND function code in `A`:

| `A` | Meaning | Path |
|---|---|---|
| `≥ 2` | open for input / output / update | branch to `done_file_open` |
| `1`   | close one channel | go to `done_file_open` |
| `0`   | close all channels | load `A=5` (close-all return code) and fall through |

Single caller (the OSFIND vector table at `&9EED`).""", on_entry={'a': 'OSFIND function code (0=close-all, 1=close-one, >=2 = open variants)'})


d.subroutine(0x9FCF, 'clear_result', title='Set A=0 and finalise', description="""Loads A=0 and falls through to shift_and_finalise (LSR A / BPL
finalise_and_return). The LSR-then-BPL is the standard FS-handler
'success exit with carry clear' idiom. Two callers: the post-
return path at &9FD6 and the catalogue tail at tail_update_
catalogue (&A329).""", on_exit={'a': '0', 'c': '0 (LSR of 0)'})


d.subroutine(0x9D0C, 'recv_reply', title='Receive FS reply and stash result byte', description="""JSRs recv_and_process_reply, then falls through to store_result
(STX hazel_txcb_result; LDY #&0E to point at the protection-bits offset).
Single caller (the dispatch at &9C82).""", on_exit={'x': 'FS result byte (also written to hazel_txcb_result)', 'y': '&0E (FS options offset for protection)'})


d.subroutine(0xA0A9, 'fscv_0_opt_entry', title='FSCV reason 0: read OSARGS', description="""Handles OSARGS via the FSCV vector. If `A=0` (initialise dot-seen
flag) clears the flag and proceeds. Compares `X` against 4 (number
of args): out-of-range exits via the OSARGS dispatch chain to a
shared error path; otherwise dispatches to the per-argument
handler. Reached via the FSCV vector with reason code 0.""", on_entry={'a': 'OSARGS sub-function (0 = initialise)', 'x': 'argument index (0-3)'})


d.subroutine(0xA10B, 'fscv_1_eof', title='FSCV reason 1: EOF check', description="""Verifies the FS workspace checksum, then loads the channel's
block-offset byte (`fs_block_offset`, `&BC`), pushes it on the
stack and stores the per-channel attribute reference in `hazel_chan_attr`.
The body proceeds to compare the buffer byte count with the file
length to decide whether the channel is at EOF. Reached via the
FSCV vector with reason code 1.""", on_entry={'y': 'channel handle'}, on_exit={'a': '0 = not at EOF, non-zero = EOF'})


d.subroutine(0xA12C, 'update_addr_from_offset9', title='Update both address fields in FS options', description="""Calls [`add_workspace_to_fsopts`](address:A133) for offset
9 (the high address / exec address field), then falls through to
[`update_addr_from_offset1`](address:A131) to process offset
1 (the low address / load address field).""", on_exit={'a, x, y, c flag': 'clobbered (4-byte arithmetic loop)'})


d.subroutine(0xA131, 'update_addr_from_offset1', title='Update low address field in FS options', description="""Sets Y=1 and falls through to
add_workspace_to_fsopts to add the workspace
adjustment bytes to the load address field at
offset 1 in the FS options block.""", on_entry={'c': 'carry state passed to add_workspace_to_fsopts'})


d.subroutine(0xA133, 'add_workspace_to_fsopts', title='Add workspace bytes to FS options with clear carry', description="""Clears carry and falls through to
adjust_fsopts_4bytes. Provides a convenient entry
point when the caller needs addition without a
preset carry.""", on_entry={'y': 'FS options offset for first byte'})


d.subroutine(0xA134, 'adjust_fsopts_4bytes', title='Add or subtract 4 workspace bytes from FS options', description="""Processes 4 consecutive bytes at `(fs_options)+Y`, adding or
subtracting the corresponding 4-byte transfer-address record
from ANFS workspace.

The direction is controlled by bit 7 of `fs_load_addr_2`:

| Bit 7 | Operation |
|---|---|
| set   | subtract |
| clear | add |

Carry propagates across all 4 bytes for correct multi-byte
arithmetic.""", on_entry={'y': 'FS options offset for first byte', 'c': 'carry input for first byte'})

d.label(0xA1EA, 'return_success')


d.subroutine(0xA145, 'store_adjusted_byte', title='Store adjusted byte and step the loop', description="""Tail of the address-adjustment 4-byte loop: STA (fs_options),Y /
INY / INX / BNE loop_adjust_byte / RTS. The BNE retries until X
has cycled through all 4 bytes; once X overflows back to 0 the
loop exits and the RTS returns. Single caller (the loop-body fall-
through at &A13F).""", on_entry={'a': 'byte to store', 'y': 'current FS-options index', 'x': 'remaining-byte counter'})


d.subroutine(0xA14C, 'gbpbv_handler', title='GBPBV vector handler: OSGBPB', description="""Reached via the GBPBV vector at
[`vec_gbpbv`](address:021C) after the
[`fs_vector_table`](address:8EA7) has copied the entry.
Verifies the FS workspace checksum, sets up transfer parameters,
masks the access prefix, and dispatches the OSGBPB sub-operation
in `A`:

| `A` | Operation |
|---|---|
| `1` | PUT bytes with pointer |
| `2` | PUT bytes |
| `3` | GET bytes with pointer |
| `4` | GET bytes |
| `5` | read disc title |
| `6` | read CSD |
| `7` | read library |
| `8` | read files in CSD |""", on_entry={'a': 'OSGBPB function code (1-8)', 'x, y': 'control-block pointer (low, high)'})


d.subroutine(0xA1EF, 'lookup_cat_entry_0', title='Look up channel from FS options offset 0', description="""Loads the channel handle from (fs_options) at
offset 0, then falls through to lookup_cat_slot_data
to find the corresponding FCB entry.""", on_exit={'a': 'FCB flag byte from &1030+X', 'x': 'channel slot index'})


d.subroutine(0xA1F3, 'lookup_cat_slot_data', title='Look up channel and return FCB flag byte', description="""Calls [`lookup_chan_by_char`](address:B847) to find the channel
slot for handle `A` in the channel table, then loads the FCB
slot-attribute byte from
[`hazel_fcb_slot_attr`](address:C230)+`X`. (Pre-HAZEL ROMs read
from &1030+X.)""", on_entry={'a': 'channel handle'}, on_exit={'a': 'FCB slot-attribute byte', 'x': 'channel slot index'})


d.subroutine(0xA1FA, 'setup_transfer_workspace', title='Prepare workspace for OSGBPB data transfer', description="""Orchestrates the setup for OSGBPB (get/put multiple bytes)
operations:

1. Look up the channel.
2. Copy the 6-byte address structure from FS options (skipping
   the hole at offset 8).
3. Determine transfer direction from the operation code:

   | Operation code parity | Direction | FS port |
   |---|---|---|
   | even | read  | `&91` |
   | odd  | write | `&92` |

4. Send the FS request.
5. Configure the TXCB address pairs for the actual
   data-transfer phase.
6. Dispatch to the appropriate handler.""", on_exit={'a': 'FS reply status from the data-transfer phase'})


d.subroutine(0xA284, 'recv_reply_preserve_flags', title='Receive and process reply, preserving flags', description="""Wrapper around recv_and_process_reply that
saves and restores the processor status register,
so the caller's flag state is not affected by
the reply processing.""", on_exit={'a': 'FS reply status', 'p (flags)': 'preserved across the call (PHP/PLP)'})


d.subroutine(0xA28A, 'send_osbput_data', title='Send OSBPUT data block to file server', description="""Sets `Y=&15` (TX buffer size for OSBPUT data) and calls
[`save_net_tx_cb`](address:978A) to dispatch the TX. Then copies
the display flag from `hazel_fs_flags` to `hazel_txcb_byte_16` (TX header continuation).
Single caller in the OSBPUT-buffered-write path.""")


d.subroutine(0xA29F, 'write_block_entry', title='Pre-write Tube-station check, fall into write_data_block', description="""Y=4 (FS-options offset for station). If tube_present is zero
(no Tube co-pro), branch forward to store_station_result and skip
the next compare; otherwise CMP (fs_options),Y to validate the
caller's station matches the saved Tube station. Falls through to
write_data_block. Single caller (&A16A in the OSWORD write path).""", on_entry={'y': 'ignored (forced to 4)'})


d.subroutine(0xA2ED, 'write_data_block', title='Write data block to destination or Tube', description="""| `tube_present` | Action |
|---|---|
| zero (no Tube) | copy directly from the `fs_cmd_data` buffer via `(fs_crc_lo)` |
| non-zero       | claim the Tube, set up the transfer address, write via R3 |""", on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xA329, 'tail_update_catalogue', title='Catalogue-update exit (JMP clear_result)', description="""Single-instruction tail: JMP clear_result -- shared exit for the
catalogue-update paths after they have finished writing the new
entry. Two callers: &A300 (the success path) and &A38D (the
no-change path). Never returns directly (clear_result loads A=0
and tail-falls into finalise_and_return).""")


d.subroutine(0xA390, 'tube_claim_c3', title='Claim the Tube via protocol &C3', description="""Loops calling tube_addr_data_dispatch with
protocol byte &C3 until the claim succeeds
(carry set on return). Used before Tube data
transfers to ensure exclusive access to the
Tube co-processor interface.""", on_entry={}, on_exit={'a': '&C3 (the claim protocol byte left in A)', 'c flag': 'set (the claim succeeded -- this is the loop termination condition)'})


d.subroutine(0xA3BB, 'print_fs_info_newline', title='Print station address and newline', description="""Sets V (suppressing leading-zero padding on
the network number) then prints the station
address followed by a newline via OSNEWL.
Used by *FS and *PS output formatting.""", on_exit={'a, x, y': 'clobbered (print_station_addr + OSNEWL)'})


d.subroutine(0xA3C4, 'parse_fs_ps_args', title='Parse station address from *FS/*PS arguments', description="""Reads a station address in `net.station` format from the command
line, with the network number optional (defaults to local network).
Calls [`init_bridge_poll`](address:ABE9) to ensure the bridge
routing table is populated, then validates the parsed address
against known stations. The parsed-station value is stored in
`fs_work_7` (`&B7`).""", on_entry={'y': 'current command-line offset'}, on_exit={'x, y': 'preserved (saved/restored via PHX/PHY)'})


d.subroutine(0xA3E7, 'get_pb_ptr_as_index', title='Convert parameter block pointer to table index', description="""Reads the first byte from the OSWORD parameter
block pointer and falls through to
byte_to_2bit_index to produce a 12-byte-aligned
table index in Y.""", on_exit={'a': 'PB[0] (preserved through byte_to_2bit_index)', 'y': 'byte offset (0, 6, 12, ... up to &42)'})


d.subroutine(0xA3E9, 'byte_to_2bit_index', title='Convert byte to 12-byte-aligned table index', description="""Computes Y = A * 6 (via A*12/2) for indexing
into the OSWORD handler workspace tables.
Clamps Y to zero if the result exceeds &48,
preventing out-of-bounds access.""", on_entry={'a': 'table entry number'}, on_exit={'y': 'byte offset (0, 6, 12, ... up to &42)'})


d.subroutine(0xA3FF, 'net_1_read_handle', title='FS reply: read handle byte (no workspace lookup)', description="""Reads the inline handle byte directly from the RX buffer at
`(net_rx_ptr),Y` with `Y=&6F`, then branches into the shared
PB-store path. Used when the caller wants the raw handle byte from
the FS reply rather than the workspace-tracked value.""", on_exit={'a': 'handle byte from RX buffer'})


d.subroutine(0xA405, 'net_2_read_entry', title='FS reply: read handle byte from workspace table', description="""Calls [`get_pb_ptr_as_index`](address:A3E7) to convert the OSWORD
parameter-block pointer to a workspace-table index. On out-of-range
(`C=1`), returns zero. Otherwise reads the handle byte from
`nfs_workspace,Y`; if the slot is `?` (uninitialised marker), falls
through to the zero-return path; otherwise stores the real handle
into PB[0].""")


d.subroutine(0xA415, 'net_3_close_handle', title='FS reply: close handle entry', description="""Calls [`get_pb_ptr_as_index`](address:A3E7) to look up the
workspace slot. On out-of-range, marks the workspace as
uninitialised. Otherwise rotates `fs_flags` bit 0 into carry (state
save), reads PB[0] (the handle to close), and proceeds with the
close path.""")


d.subroutine(0xA42F, 'fscv_3_star_cmd', title='FSCV reason 3: process *<command> via FS', description="""Sets up text and transfer pointers via set_text_and_xfer_ptr, marks
spool / Tube state as inactive (fs_spool_handle = need_release_tube
= &FF), then calls match_fs_cmd with X=&35, Y=0 to look up the user's
text in the FS command table. The match-or-error result feeds into
the FS dispatch chain that follows. Single caller (the FSCV vector
table at &8CFA).""")


d.subroutine(0xA440, 'cmd_fs_reentry', title='FS-command re-entry guard (BVC dispatch_fs_cmd)', description="""Single-instruction prologue: BVC dispatch_fs_cmd. Reached as the
fall-through target after a *RUN failure -- if V is clear (the
re-entry path is permitted) it branches into dispatch_fs_cmd to
re-attempt the command; otherwise falls through to error_syntax to
raise 'Syntax'. Single caller (the FS dispatch table at &8C4E).""")


d.subroutine(0xA45B, 'match_fs_cmd', title='Match command name against FS command table', description="""Case-insensitive compare of the command line against
`cmd_table_fs` entries with bit-7-terminated names. Returns with
the matched entry address on success.""", on_entry={'x': 'starting offset within cmd_table_fs (selects which sub-table is searched: NFS commands, FS commands, etc.)'}, on_exit={'x': 'byte offset just past the matched command name in cmd_table_fs (or end-of-table if no match)', 'y': 'command-line offset of the first non-name character (typically the argument start)', 'z flag': 'set on match, clear on no-match'})


d.subroutine(0xA4A2, 'loop_skip_trail_spaces', title='Skip trailing spaces from FS command-line args', description="""Reads (fs_crc_lo),Y; on space, falls through to the per-char
advance; non-space exits to check_cmd_flags. Shared body with
skip_dot_and_spaces at &A4A8 (alt-entry that also accepts dots).
Single caller (the BNE retry at &A4A9).""", on_entry={'y': 'current command-line offset'})


d.subroutine(0xA4E4, 'fscv_2_star_run', title='FSCV reason 2: handle *RUN', description="""Saves the OS text pointer via
[`save_ptr_to_os_text`](address:B373), calls
[`mask_owner_access`](address:B2CF) to clear the FS-selection bit,
ORs in bit 1 (the *RUN-in-progress flag), and stores back to
[`hazel_fs_lib_flags`](address:C271). Falls through to the run-handling chain
that opens the file and starts execution. Reached via the FSCV
vector dispatch with reason code 2.""")


d.subroutine(0xA4F1, 'cmd_run_via_urd', title='*RUN entry for URD-prefixed argument', description="""Reached from cmd_fs_operation at &8E35 when the first character of
the *RUN argument is '&' (the URD = User Root Directory prefix).
Saves the OS text pointer via save_ptr_to_os_text, masks the access
bits via mask_owner_access, clears bit 1 of the result, and stores
into hazel_fs_lib_flags. Falls through to cmd_run_load_mask which calls
parse_cmd_arg_y0 to begin parsing the rest of the *RUN argument.
Single caller; never returns directly (continues into the run
flow).""")


d.subroutine(0xA5A1, 'error_bad_command', title="Raise 'Bad command' BRK error", description="""Loads error code &FE and tail-calls error_bad_inline with the inline
string 'command' -- error_bad_inline prepends 'Bad ' to produce the
final 'Bad command' message. Used by the FS command parser when no
table entry matches the user's input. Never returns.""")


d.subroutine(0xA5AE, 'check_exec_addr', title='Validate exec address is non-zero', description="""Iterates X = 3..0 over the 4-byte exec-address copy at hazel_txcb_flag..hazel_exec_addr,
incrementing each byte. If any byte becomes non-zero (BNE),
branches forward to library_path_string (the OSCLI dispatch path). When all four
INC operations leave a zero result the address was &FFFFFFFF + 1 =
0 -- not a valid exec address -- and the routine falls through to
the no-exec-address handler. Single caller (&A51C in the *RUN
handler).""", on_entry={'a': 'exec address bytes already in hazel_txcb_flag..hazel_exec_addr'}, on_exit={'x': '0 if no valid exec; non-zero branch otherwise'})


d.subroutine(0xA5C3, 'alloc_run_channel', title='Allocate FCB slot for *RUN target file', description="""Loads the saved OSWORD parameter byte at hazel_txcb_data, calls alloc_fcb_slot
to obtain a free channel index in A, transfers it into Y, then
clears the per-channel attribute byte at hazel_fcb_status,X. Used by the
*RUN argument-handling path at &A538 once the file is opened, to
reserve a channel for the running program.""", on_exit={'a': 'channel attribute byte (cleared to 0)', 'x': 'FCB slot index', 'y': 'FCB slot index (copy of X)'})


d.subroutine(0xA638, 'fsreply_3_set_csd', title='FS reply handler: select CSD station', description="""Single-instruction wrapper: JSR find_station_bit3 to record the
new current-selected-directory (CSD) station in the table, then
JMP return_with_last_flag to clean up and return. Single caller
(the FS reply dispatch at &9594).""", on_exit={'a': 'fs_last_byte_flag (loaded by return_with_last_flag)'})


d.subroutine(0xA63E, 'fsreply_5_set_lib', title='FS reply handler: set library station', description="""Two-instruction wrapper: `JSR
`[`flip_set_station_boot`](address:A6A6) to record the new library
station, then `JMP`
[`return_with_last_flag`](address:9FB4). Reached only via the FS
reply dispatch table.""")


d.subroutine(0xA644, 'find_station_bit2', title='Find printer server station in table (bit 2)', description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 2 set (printer server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""", on_exit={'v flag': 'set if matching slot already had bit 2; clear if newly allocated', 'x': 'table slot index of the matched/allocated entry'})


d.subroutine(0xA66F, 'find_station_bit3', title='Find file server station in table (bit 3)', description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 3 set (file server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""", on_exit={'v flag': 'set if matching slot already had bit 3; clear if newly allocated', 'x': 'table slot index of the matched/allocated entry'})


d.subroutine(0xA6A6, 'flip_set_station_boot', title='Set boot option for a station in the table', description="""Scans up to 16 station table entries for one
matching the current address with bit 4 set
(boot-eligible). Stores the requested boot type
in the matching entry and calls
restore_fs_context to re-establish the filing
system state.""", on_entry={'a': 'boot type code to store'}, on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xA6D5, 'fsreply_1_boot', title='FS reply 1: copy boot handles + flag boot pending', description="""Closes all network channels via
[`close_all_net_chans`](address:B8F8), sets bit 6 of `fs_flags`
(`TSB &0D6C`, marking the boot-pending state), then loads the
boot type from the FS reply at `hazel_txcb_result` and stores it into both the
current-boot-type slot (`hazel_fs_flags`) and the FCB-flags table. Pushes
the boot type for the fall-through into `fsreply_2_copy_handles`
which copies the per-handle table.""")


d.subroutine(0xA6E5, 'fsreply_2_copy_handles', title='FS reply 2: install handles and (optionally) boot', description="""Records the file-server / printer-server / library handles from
the I-AM reply into the station table by calling
[`find_station_bit2`](address:A644),
[`find_station_bit3`](address:A66F), and
[`flip_set_station_boot`](address:A6A6) in turn with the three
handle bytes loaded from the TXCB reply
([`hazel_txcb_data`](address:C105),
[`hazel_txcb_flag`](address:C106),
[`hazel_txcb_count`](address:C107)). PHP/PLP carry a flag across
the calls: when Carry is clear on entry the routine returns via
[`return_with_last_flag`](address:9FB4); when Carry is set it
continues into the boot path at
[`fsreply_2_handle_loop`](address:A70B), which OSCLIs
`-NET-FindLib`, optionally calls OSBYTE `&6D` to make the filing
system permanent, clears the auto-boot flag in
[`hazel_fs_lib_flags`](address:C271), and (unless CTRL is held)
falls through to [`boot_suffix_string`](address:A75F) to execute
the !Boot command. Reached only via the FS reply dispatch
table.""", on_entry={'a': 'boot-type byte (saved on stack at entry)', 'carry': 'set when boot processing should follow'})


d.subroutine(0xA764, 'boot_cmd_oscli', title='Look up boot command in boot_prefix_string table and OSCLI it', description="""Loads X = boot_prefix_string,Y (the low byte of the boot-command address),
sets Y=&A7 (high byte = &A7xx area where the boot strings live),
then JMPs to oscli with (X,Y) pointing at a CR-terminated command
string. Single caller (&A5D4 in the *RUN-then-* boot dispatch).""", on_entry={'y': 'boot-command index'})


d.subroutine(0xA864, 'osword_setup_handler', title='Push OSWORD handler address for RTS dispatch', description="""Indexes the OSWORD dispatch table by X to
push a handler address (hi then lo) onto the
stack. Copies 3 bytes from the osword_flag
workspace into the RX buffer, loads PB byte 0
(the OSWORD sub-code), and clears svc_state.
The subsequent RTS dispatches to the pushed
handler address.""", on_entry={'x': 'OSWORD handler index (0-6)'})


d.subroutine(0xA901, 'bin_to_bcd', title='Convert binary byte to BCD', description="""Uses decimal mode (SED) with a count-up loop:
starts at BCD 0 and adds 1 in decimal mode for
each decrement of the binary input. Saves and
restores the processor flags to avoid leaving
decimal mode active. Called 6 times by
save_txcb_and_convert for clock date/time
conversion.""", on_entry={'a': 'binary value (0-99)'}, on_exit={'a': 'BCD equivalent'})


d.subroutine(0xAC47, 'osword_14_handler', title='OSWORD &14 handler: bridge poll / station status', description="""Triages by `A`: `A >= 1` branches via `BCS` to
[`handle_tx_request`](address:ACB7) which reads the station and
network from `PB[1]`/`PB[2]` into the RX-block destination slots
and falls through to the burst-transfer body. `A = 0` (the
bridge-poll sub-code) falls through here: pushes `A`, calls
[`ensure_fs_selected`](address:8B4D) to bring ANFS up if needed,
pulls `A` back, sets `Y=&23` and calls
[`mask_owner_access`](address:B2CF) to clear FS-selection bits,
then runs the bridge-poll body.""", on_entry={'a': 'OSWORD &14 sub-function code', 'x, y': 'OSWORD parameter block pointer (low, high)'})


d.subroutine(0xACED, 'handle_burst_xfer', title='OSWORD &14 burst-transfer path: extend buffer end and TX', description="""Reached from [`handle_tx_request`](address:ACB7)'s `BNE` at
`&ACCC`. Calls [`init_ws_copy_wide`](address:ADFE) to copy the
workspace TXCB template into the wide-mode workspace slot, then
extends the buffer end-byte at `(net_rx_ptr)+&7B` by `3` to
account for the 3-byte burst header before falling through into
[`enable_irq_and_poll`](address:ACF8), which re-enables IRQs and
tail-jumps to [`send_net_packet`](address:9B2C).""", on_entry={'net_rx_ptr': 'set up by handle_tx_request (dest station/network already stored at +&71/&72)'})


d.subroutine(0xACB7, 'handle_tx_request', title='Sub-code 0: copy PB station/network into RX block, dispatch burst', description="""Sub-code-0 path of [`osword_14_handler`](address:AC47), reached
via the `BCC handle_tx_request` at `&AC49` when the caller's `A`
is 0. Reads two bytes from the OSWORD parameter block:

| Reg setup | Source     | Stored at        |
| --------- | ---------- | ---------------- |
| `Y=1`     | `PB[1]`    | (parked in `X`)  |
| `Y=2`     | `PB[2]`    | `(net_rx_ptr)+&72` (dest network) |
| `Y=3`     | (saved as `osword_flag` for the next byte read) | |
| `Y=&71`   | `X` (PB[1])| `(net_rx_ptr)+&71` (dest station) |

Wraps the body in `PHP`/`PLP` so the entry flags (carry clear from
the `BCC`) survive the workspace stores; the `BNE` after `PLP`
then dispatches to [`handle_burst_xfer`](address:ACED) when the
caller's `A` was non-zero (a defensive branch -- the `BCC` entry
guarantees `A=0` in 4.21, but the same body is the entry point
the burst path piggy-backs on).""", on_entry={'a': "OSWORD &14 sub-function code (caller's A; 0 via the BCC entry from osword_14_handler)", 'ws_ptr_hi': 'OSWORD parameter-block high byte'})


d.subroutine(0xAC67, 'store_osword_pb_ptr', title='Store workspace pointer+1 to NFS workspace', description="""Computes ws_ptr_hi + 1 and stores the resulting
16-bit address at workspace offset &1C via
store_ptr_at_ws_y. Then reads PB byte 1 (the
transfer length) and adds ws_ptr_hi to compute
the buffer end pointer, stored at workspace
offset &20.""")


d.subroutine(0xACAD, 'store_ptr_at_ws_y', title='Store 16-bit pointer at workspace offset Y', description="""Writes a 16-bit address to (nfs_workspace)+Y.
The low byte comes from A; the high byte is
computed from table_idx plus carry,
supporting pointer arithmetic across page
boundaries.""", on_entry={'a': 'pointer low byte', 'y': 'workspace offset', 'c': 'carry for high byte addition'})


d.subroutine(0xAA82, 'copy_pb_byte_to_ws', title='Conditionally copy parameter block byte to workspace', description="""If carry is set, loads a byte from the OSWORD
parameter block at offset Y; if clear, uses
the value already in A. Stores the result to
workspace at the current offset. Decrements X
and loops until the requested byte count is
transferred.""", on_entry={'c': 'set to load from PB, clear to use A', 'x': 'byte count', 'y': 'PB source offset'})


d.subroutine(0xA910, 'osword_10_handler', title='OSWORD &10 handler: send network packet', description="""ASL on [`tx_complete_flag`](address:0D60) shifts the old bit 7
into Carry. When that bit was clear (`C=0`, TX in progress) the
handler stores Y back through the parameter-block pointer at
`(ws_ptr_hi),Y` and RTS, leaving the caller a status byte. When
it was set (`C=1`, TX idle) execution falls through to the start
path at [`setup_ws_rx_ptrs`](address:A919), which seeds the
workspace pointers from [`net_rx_ptr_hi`](address:009D)/`#&6F`,
copies 16 bytes of the parameter block into the workspace via
[`copy_pb_byte_to_ws`](address:AA82) and JMPs to
[`tx_begin`](address:8589) to launch the transmission.""", on_entry={'x, y': 'OSWORD parameter block pointer (low, high)'})


d.subroutine(0xA92D, 'osword_11_handler', title='OSWORD &11 handler: receive network packet', description="""Reached via the OSWORD dispatch as well as via fall-through from
[`osword_10_handler`](address:A910). Configures the workspace
pointer from `nfs_workspace_hi`, saves the Econet interrupt state
via `ROR econet_flags`, and either uses the slot specified by the
caller (Y non-zero) or scans from slot 3 onwards via
[`byte_to_2bit_index`](address:A3E9) to find a free slot. Stores
the resulting status byte and the copied PB bytes back into the
caller's parameter block.""", on_entry={'x, y': 'OSWORD parameter block pointer (low, high)'})


d.subroutine(0xA985, 'osword_12_handler', title='OSWORD &12 handler: receive packet from workspace', description="""Reads `net_rx_ptr_hi` into `ws_ptr_lo`, sets `Y=&7F` and reads the
status byte from the RX block, then `Y=&80` to flag the packet as
processed. The body proceeds to copy the packet payload from the
RX buffer into the OSWORD parameter block via
[`copy_pb_byte_to_ws`](address:AA82).""", on_entry={'x, y': 'OSWORD parameter block pointer (low, high)'})
d.entry(0xA9CC)


d.subroutine(0xA9CC, 'osword_13_read_station', title='OSWORD &13 sub 0: read file server station', description="""Returns the current file server station and network numbers in
`PB[1..2]`. If ANFS is not active,
[`ensure_fs_selected`](address:8B4D) auto-selects it (raising `net
checksum` on failure) before the body runs.""")
d.entry(0xA9DA)


d.subroutine(0xA9DA, 'osword_13_set_station', title='OSWORD &13 sub 1: set file server station', description="""Sets the file server station and network numbers from `PB[1..2]`.
The prologue at `&A9DA` calls
[`ensure_fs_selected`](address:8B4D) to verify ANFS is active
(auto-selecting it if not), then the body at
[`osword_13_set_station_body`](address:A9DD) processes all FCBs
and scans the 16-entry FCB table to reassign handles matching the
new station.""")

d.label(0xA9DD, 'osword_13_set_station_body')


d.subroutine(0x8B4D, 'ensure_fs_selected', title='Ensure ANFS is the active filing system', description="""If bit 7 of `fs_flags` is set (ANFS already active), `RTS` via
`return_from_save_text_ptr`. Otherwise calls `cmd_net_fs` to select
ANFS now; on failure, `JMP`s to
[`error_net_checksum`](address:90B5) to raise the `net checksum`
error. After successful selection, falls through to the body at
`&8B5A` which sets up the OSWORD parameter block pointer and
continues the caller's work.""", on_entry={'x, y': 'OSWORD parameter block pointer (preserved across the cmd_net_fs call when selection happens)'})


d.subroutine(0xAA72, 'osword_13_read_csd', title='OSWORD &13 sub 12: read CSD path', description="""Reads 5 current selected directory path bytes
from the RX workspace at offset &17 into
PB[1..5]. Sets carry clear to select the
workspace-to-PB copy direction.""")


d.subroutine(0xAA75, 'osword_13_write_csd', title='OSWORD &13 sub 13: write CSD path', description="""Writes 5 current selected directory path bytes
from PB[1..5] into the RX workspace at offset
&17. Sets carry to select the PB-to-workspace
copy direction.""")


d.subroutine(0xAA91, 'osword_13_read_ws_pair', title='OSWORD &13 sub 2: read workspace byte pair', description="""Reads 2 bytes from the NFS workspace page
starting at offset 1 into PB[1..2]. Uses
nfs_workspace_hi as the page and
copy_pb_byte_to_ws with carry clear for the
workspace-to-PB direction.""")


d.subroutine(0xAA9D, 'osword_13_write_ws_pair', title='OSWORD &13 sub 3: write workspace byte pair', description="""Writes 2 bytes from PB[1..2] into the NFS
workspace at offsets 2 and 3. Then calls
init_bridge_poll and conditionally clears
the workspace byte if the bridge status
changed.""")


d.subroutine(0xAAB2, 'osword_13_read_prot', title='OSWORD &13 sub 4: read protection mask', description="""Returns the current protection mask (ws_0d68)
in PB[1].""")


d.subroutine(0xAAB8, 'osword_13_write_prot', title='OSWORD &13 sub 5: write protection mask', description="""Loads the new protection mask from `PB[1]` and falls through into
[`set_ws_pair_0d68_0d69`](address:AABB) which mirrors it into the
ACR/SR-format byte pair at `&0D68` / `&0D69` that ANFS uses for its
own state tracking.""")


d.subroutine(0xAABB, 'set_ws_pair_0d68_0d69', title='Store A in both ws_0d68 and ws_0d69', description="""Copies `A` to both [`ws_0d68`](address:0D68) and
[`ws_0d69`](address:0D69), then `RTS`. The bytes carry ACR/SR-style
flag layouts that ANFS uses internally; nothing in this ROM flushes
them to the live System VIA. Two callers:
[`nfs_init_body`](address:8F38) at `&8FA6` (where A is `0` or
`&FF` based on FS-options bit 6) and
[`cmd_prot`](address:B6D2) at `&B6D9` (the *Prot path).
A 2-store-and-return convenience to keep both call sites flat.""", on_entry={'a': 'value to mirror into both workspace bytes'})
d.entry(0xAAC2)


d.subroutine(0xAAC2, 'osword_13_read_handles', title='OSWORD &13 sub 6: read FCB handle info', description="""Returns the 3-byte FCB handle/port data from the workspace at
`C271[1..3]` into `PB[1..3]`. If ANFS is not active,
[`ensure_fs_selected`](address:8B4D) auto-selects it before the
body runs.""")
d.entry(0xAAD0)


d.subroutine(0xAAD0, 'osword_13_set_handles', title='OSWORD &13 sub 7: set FCB handles', description="""Validates and assigns up to 3 FCB handles
from PB[1..3]. Each handle value (&20-&2F)
indexes the channel tables. For valid handles
with the appropriate flag bit, stores the
station and FCB index, then updates flag bits
across all FCB entries via update_fcb_flag_bits.""")


d.subroutine(0xAB43, 'update_fcb_flag_bits', title='Update FCB flag bits across all entries', description="""Scans all 16 FCB entries in hazel_fcb_status. For each
entry with bit 6 set, tests the Y-specified
bit mask: if matching, ORs bit 5 into the
flags; if not, leaves bit 5 clear. In both
cases, inverts and clears the tested bits.
Preserves X.""", on_entry={'y': 'flag bit mask to test', 'x': 'current FCB index (preserved)'})


d.subroutine(0xAB68, 'osword_13_read_rx_flag', title='OSWORD &13 sub 8: read RX control block flag', description="""Returns byte 1 of the current RX control
block in PB[1].""")


d.subroutine(0xAB71, 'osword_13_read_rx_port', title='OSWORD &13 sub 9: read RX port byte', description="""Returns byte &7F of the current RX control
block in PB[1], and stores &80 in PB[2].""")


d.subroutine(0xAB7F, 'osword_13_read_error', title='OSWORD &13 sub 10: read error flag', description="""Returns the latched FS last-error byte
([`hazel_fs_last_error`](address:C009)) in `PB[1]`. Falls through
into [`store_a_to_pb_1`](address:AB82).""")


d.subroutine(0xAB82, 'store_a_to_pb_1', title='Store A to OSWORD parameter block at offset 1', description="""Increments Y to 1 and stores A into the
OSWORD parameter block via (ws_ptr_hi),Y.
Used by OSWORD 13 sub-handlers to return a
single result byte.""", on_entry={'A': 'value to store'}, on_exit={'Y': '1'})


d.subroutine(0xAB86, 'osword_13_read_context', title='OSWORD &13 sub 11: read context byte', description="""Returns the FS context/error code
([`hazel_fs_error_code`](address:C008)) in `PB[1]` when bit 7 is
clear; if bit 7 is set the value is left alone (the BPL skips the
store). Tail-merges into [`store_a_to_pb_1`](address:AB82).""")


d.subroutine(0xAB8B, 'osword_13_read_free_bufs', title='OSWORD &13 sub 14: read printer buffer free space', description="""Returns the number of free bytes remaining in
the printer spool buffer (&6F minus spool_buf_idx)
in PB[1]. The buffer starts at offset &25 and can
hold up to &4A bytes of spool data.""")


d.subroutine(0xAB93, 'osword_13_read_ctx_3', title='OSWORD &13 sub 15: read retry counts', description="""Returns the three retry count values in
PB[1..3]: PB[1] = transmit retry count
(default &FF = 255), PB[2] = receive poll
count (default &28 = 40), PB[3] = machine
peek retry count (default &0A = 10). Setting
transmit retries to 0 means retry forever.""")


d.subroutine(0xAB9E, 'osword_13_write_ctx_3', title='OSWORD &13 sub 16: write retry counts', description="""Sets the three retry count values from
PB[1..3]: PB[1] = transmit retry count,
PB[2] = receive poll count, PB[3] = machine
peek retry count.""")


d.subroutine(0xABA9, 'osword_13_bridge_query', title='OSWORD &13 sub 17: query bridge status', description="""Calls init_bridge_poll, then returns the
bridge status. If bridge_status is &FF (no bridge),
stores 0 in PB[0]. Otherwise stores bridge_status
in PB[1] and conditionally updates PB[3]
based on station comparison.""")


d.subroutine(0xABE9, 'init_bridge_poll', title='Initialise Econet bridge routing table', description="""Checks the bridge status byte: if &FF
(uninitialised), broadcasts a bridge query
packet and polls for replies. Each reply
adds a network routing entry to the bridge
table. Skips the broadcast if the table has
already been populated from a previous call.""", on_exit={'a, x, y': 'clobbered when the broadcast path runs'})


d.subroutine(0xACF8, 'enable_irq_and_poll', title='Enable interrupts and send Econet packet', description="""Executes CLI to re-enable interrupts, then
falls through to send_net_packet. Used after
a sequence that ran with interrupts disabled
to ensure the packet is sent with normal
interrupt handling active.""", on_entry={'i flag': 'may be set (caller had IRQs off); CLI clears it'}, on_exit={'i flag': 'clear (interrupts enabled)'})


d.subroutine(0xACFC, 'netv_handler', title='NETV handler: OSWORD dispatch', description="""Installed as the NETV handler via `write_vector_entry`. Saves all
registers, reads the OSWORD number from the stack, and dispatches
OSWORDs 0-8 via [`push_osword_handler_addr`](address:AD15).
OSWORDs `>= 9` are ignored (registers restored, RTS returns to
MOS). The handler's address lives in the extended vector data
area together with the other [`fs_vector_table`](address:8EA7)
entries.""", on_entry={'a': 'OSWORD number (read from stacked A on entry)', 'x, y': 'PB pointer low/high (per OSWORD calling convention)'}, on_exit={'a, x, y, p': 'restored from stack'})


d.subroutine(0xAD15, 'push_osword_handler_addr', title='Push OSWORD handler address for RTS dispatch', description="""Indexes the OSWORD handler dispatch table
using the current OSWORD number to push the
handler's address (hi/lo) onto the stack.
Reloads the OSWORD number from osbyte_a_copy
so the dispatched handler can identify the
specific call.""", on_entry={'a': 'OSWORD number (0-8) -- table index'}, on_exit={'a': "OSWORD number (re-loaded for the handler's use)"})
d.entry(0xAD32)


d.subroutine(0xAD32, 'osword_4_handler', title='OSWORD &04 handler: clear C, send abort', description="""Reaches the stack via `TSX`, clears bit 0 of the stacked processor
status (`ROR stack_page_6,X` then `ASL stack_page_6,X` -- a
read-modify cycle that lands the carry-out where bit 0 of the
saved P was), so the caller resumes with `C=0`. Stores the
caller's `Y` into NFS workspace at offset `&DA`, then falls
through to [`tx_econet_abort`](address:AD40) with `A=0` to
transmit a clean disconnect packet.""", on_entry={'y': 'OSWORD parameter byte (saved into nfs_workspace+&DA)'})


d.subroutine(0xAD40, 'tx_econet_abort', title='Send Econet abort/disconnect packet', description="""Stores the abort code in workspace, configures
the TX control block with control byte &80
(immediate operation flag), and transmits the
abort packet. Used to cleanly disconnect from
a remote station during error recovery.""", on_entry={'a': 'abort code (stored in workspace before TX)'})


d.subroutine(0xAD64, 'netv_claim_release', title='OSWORD 7 handler: claim/release network resources', description="""Handles OSWORD 7 (SOUND) intercepted via NETV.
Searches the claim code table in two passes:
first 11 entries (state 2), then all 18 (state
3). On match, saves 3 tube state bytes to
workspace and sends an abort with the state
code. For state 3 matches, also polls workspace
for a response and restores the caller's stack
frame from the saved bytes.""", on_entry={'a': 'OSWORD 7 number (validated by caller)'})


d.subroutine(0xADB8, 'match_rx_code', title='Search receive code table for match', description="""Scans a table of receive operation codes
starting at index X, comparing each against A.
Returns with Z set if a match is found, Z clear
if the end-of-table marker is reached.""", on_entry={'a': 'receive code to match', 'x': 'starting table index'}, on_exit={'z': 'set if match found'})


d.subroutine(0xADD3, 'osword_8_handler', title='OSWORD 7/8 handler: copy PB to workspace and abort', description="""Handles OSWORD 7 or 8 by copying 15 bytes from
the parameter block to workspace at offset &DB,
storing the OSWORD number at offset &DA, setting
control value &E9, and sending an abort packet.
Returns via tx_econet_abort. Rejects other
OSWORD numbers by returning immediately.""", on_entry={'a': 'OSWORD number (must be 7 or 8 to be processed)'})


d.subroutine(0xADFE, 'init_ws_copy_wide', title='Initialise workspace copy in wide mode (14 bytes)', description="""Copies 14 bytes to workspace offset &7C.
Falls through to the template-driven copy
loop which handles &FD (skip), &FE (end),
and &FC (page pointer) markers.""", on_entry={'x': 'template source offset (within ws_txcb_template_data)'})


d.subroutine(0xAE07, 'init_ws_copy_narrow', title='Initialise workspace copy in narrow mode (27 bytes)', description="""Sets up a 27-byte copy to workspace offset &17,
then falls through to ws_copy_vclr_entry for
the template-driven copy loop. Used for the
compact workspace initialisation variant.""", on_entry={'x': 'template source offset'})


d.subroutine(0xAE0B, 'ws_copy_vclr_entry', title='Template-driven workspace copy with V clear', description="""Processes a template byte array to initialise
workspace. Special marker bytes: &FE terminates
the copy, &FD skips the current offset, and &FC
substitutes the workspace page pointer. All
other values are stored directly to the
workspace at the current offset.""", on_entry={'x': 'template source offset', 'y': 'destination offset within NFS workspace', 'v flag': 'clear (controls a downstream branch in the shared body; init_ws_copy_wide / _narrow enter with V=0)'}, on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xAE5A, 'netv_spool_check', title='OSWORD 5 handler: check spool PB and reset buffer', description="""Handles OSWORD 5 intercepted via NETV. Checks
if X-1 matches osword_pb_ptr and bit 0 of
&00D0 is clear. If both conditions are met,
falls through to reset_spool_buf_state to
reinitialise the spool buffer for new data.""", on_entry={'x': 'OSWORD parameter block low byte (X-1 compared against osword_pb_ptr)'})


d.subroutine(0xAE6F, 'netv_print_data', title='OSWORD 1-3 handler: drain printer buffer', description="""Handles OSWORDs 1-3 intercepted via NETV.
When X=1, drains the printer buffer (OSBYTE
&91, buffer 3) into the receive buffer, sending
packets via process_spool_data when the buffer
exceeds &6E bytes. When X>1, routes to
handle_spool_ctrl_byte for spool state control.""", on_entry={'x': '1 = drain printer buffer; >1 = control byte path'})


d.subroutine(0xAE64, 'reset_spool_buf_state', title='Reset spool buffer to initial state', description="""Sets the spool buffer pointer (`spool_buf_idx`)
to `&21` and the control byte (`ws_0d6a`) to `&41`
(ready for new data). Called after processing a
complete spool data block.""", on_entry={}, on_exit={'a, y': 'clobbered'})


d.subroutine(0xAE94, 'append_byte_to_rxbuf', title='Append byte to receive buffer', description="""Stores A in the receive buffer at the current
buffer index (ws_ptr_lo), then increments the
index. Used to accumulate incoming spool data
bytes before processing.""", on_entry={'a': 'byte to append'})


d.subroutine(0xAE9D, 'handle_spool_ctrl_byte', title='Handle spool control byte and flush buffer', description="""Rotates bit 0 of the control byte into carry
for mode selection (print vs spool), appends
the byte to the buffer, calls process_spool_data
to transmit the accumulated data, and resets
the buffer state ready for the next block.""", on_entry={'a': 'control byte (bit 0 selects mode: 0 = print, 1 = spool)'}, on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xAEB8, 'process_spool_data', title='Transmit accumulated spool buffer data', description="""Copies the workspace state to the TX control
block, sends a disconnect reply if the previous
transfer requires acknowledgment, then handles
the spool output sequence by setting up and
sending the pass-through TX buffer.""", on_exit={'a': 'TX result (from setup_pass_txbuf)'})


d.subroutine(0xAF80, 'err_printer_busy', title="Raise 'Printer busy' error", description="""Loads error code &A6 and tail-calls error_inline_log with the inline
string 'Printer busy'. Called when an attempt is made to enable a
printer server while one is already active. Never returns.""")


d.subroutine(0xAFA6, 'send_disconnect_reply', title='Send Econet disconnect reply packet', description="""Sets up the TX pointer, copies station
addresses, matches the station in the table,
and sends the response. Waits for
acknowledgment before returning.""", on_exit={'a': 'TX result code'})


d.subroutine(0xB01A, 'lang_2_save_palette_vdu', title='Language reply 2: save palette / VDU state', description="""Reached via the language-reply dispatch table when a remote sends
reply code 2 ('save palette and VDU state'). Saves the current
template byte from `osword_flag` on the stack, sets up the
workspace pointer (`nfs_workspace`) to the appropriate offset, and
copies the palette / VDU state from MOS workspace at `&0350` into
the workspace transmit buffer for forwarding back to the
station.""")


d.subroutine(0xB05F, 'commit_state_byte', title='Copy current state byte to committed state', description="""Reads the working state byte from workspace and
stores it to the committed state location. Used
to finalise a state transition after all related
workspace fields have been updated.""", on_exit={'a': '= the committed value'})


d.subroutine(0xB066, 'serialise_palette_entry', title='Serialise palette register to workspace', description="""Reads the current logical colour for a palette
register via OSBYTE &0B and stores both the
palette value and the display mode information
in the workspace block. Used during remote
screen state capture.""", on_entry={'x': 'palette register index (0-15)', 'y': 'destination workspace offset (palette + mode pair)'}, on_exit={'y': 'advanced past the 2-byte pair', 'a, x': 'clobbered (OSBYTE)'})


d.subroutine(0xB081, 'read_osbyte_to_ws_x0', title='Read OSBYTE with X=0 and store to workspace', description="""Sets X=0 then falls through to read_osbyte_to_ws
to issue the OSBYTE call and store the result.
Used when the OSBYTE parameter X must be zero.""", on_entry={'y': 'destination workspace offset'}, on_exit={'y': 'incremented past the stored byte', 'a, x': 'clobbered (OSBYTE)'})


d.subroutine(0xB083, 'read_osbyte_to_ws', title='Issue OSBYTE from table and store result', description="""Loads the OSBYTE function code from the next
entry in the OSBYTE table, issues the call, and
stores the Y result in workspace at the current
offset. Advances the table pointer for the next
call.""", on_entry={'x': 'OSBYTE X parameter', 'y': 'destination workspace offset'}, on_exit={'y': 'incremented past the stored byte', 'a, x': 'clobbered'})


d.subroutine(0xB118, 'fscv_5_cat', title='FSCV reason 5: catalogue (*CAT)', description="""Sets up transfer parameters via [`set_xfer_params`](address:93D7),
clears the library bit in `hazel_fs_lib_flags` via the
`ROR`/`CLC`/`ROL` idiom that uses carry to preserve other flags,
and falls through to `cat_set_lib_flag` to issue the FS examine
request. Reached via the FSCV vector with reason code 5.""")


d.subroutine(0xB21A, 'print_10_chars', title='Print 10 characters from reply buffer', description="""Sets Y=10 and falls through to
print_chars_from_buf. Used by cmd_ex to print
fixed-width directory title, directory name, and
library name fields.""", on_entry={'x': 'buffer offset to start printing from'})


d.subroutine(0xB21C, 'print_chars_from_buf', title='Print Y characters from buffer via OSASCI', description="""Loops Y times, loading each byte from fs_cmd_data+X
and printing it via OSASCI. Advances X after
each character, leaving X pointing past the
last printed byte.""", on_entry={'x': 'buffer offset', 'y': 'character count'})


d.subroutine(0xB22A, 'parse_cmd_arg_y0', title='Parse command argument from offset zero', description="""Sets Y=0 and falls through to parse_filename_arg
for GSREAD-based filename parsing with prefix
character handling.""", on_exit={'y': 'advanced past the parsed argument'})


d.subroutine(0xB22C, 'parse_filename_arg', title='Parse filename via GSREAD with prefix handling', description="""Calls [`gsread_to_buf`](address:9C00) to read the command-line
string into [`hazel_parse_buf`](address:C030) (the 4.21 HAZEL
parse buffer at &C030), then falls through to
[`parse_access_prefix`](address:B22F) to process `'&'`, `':'`,
`'.'` and `'#'` prefix characters.""", on_entry={'y': 'current command-line offset (consumed by gsread_to_buf)'}, on_exit={'y': 'advanced past the parsed argument'})


d.subroutine(0xB22F, 'parse_access_prefix', title='Parse access and FS selection prefix characters', description="""Examines the first character(s) of the parsed
buffer at &C030 for prefix characters: '&' sets
the FS selection flag (bit 6 of hazel_fs_lib_flags) and
strips the prefix, ':' with '.' also triggers FS
selection, '#' is accepted as a channel prefix.
Raises 'Bad file name' for invalid combinations
like '&.' followed by CR.""")


d.subroutine(0xB251, 'strip_token_prefix', title='Strip first character from parsed token buffer', description="""Shifts all bytes in the &C030 buffer left by
one position (removing the first character),
then trims any trailing spaces by replacing
them with CR terminators. Used after consuming
a prefix character like '&' or ':'.""", on_exit={'x': 'preserved (saved/restored via PHA/PLA)', 'a': 'clobbered'})


d.subroutine(0xB29F, 'copy_arg_to_buf_x0', title='Copy argument to TX buffer from offset zero', description="""Sets X=0 and falls through to copy_arg_to_buf
then copy_arg_validated. Provides the simplest
entry point for copying a single parsed argument
into the TX buffer at position zero.""", on_exit={'x': 'TX buffer offset just past the copied argument', 'y': 'advanced past the source argument'})


d.subroutine(0xB2A1, 'copy_arg_to_buf', title='Copy argument to TX buffer with Y=0', description="""Sets Y=0 and falls through to copy_arg_validated
with carry set, enabling '&' character validation.
X must already contain the destination offset
within the TX buffer.""", on_entry={'x': 'destination offset within the TX buffer'}, on_exit={'x': 'TX buffer offset just past the copied argument', 'y': 'advanced past the source argument'})


d.subroutine(0xB2A3, 'copy_arg_validated', title='Copy command line characters to TX buffer', description="""Copies characters from (fs_crc_lo)+Y to fs_cmd_data+X
until a CR terminator is reached. With carry set,
validates each character against '&' — raising
'Bad file name' if found — to prevent FS selector
characters from being embedded in filenames.""", on_entry={'x': 'TX buffer destination offset', 'y': 'command line source offset', 'c': "set to enable '&' validation"})

d.label(0xB2C8, 'done_trim_spaces')


d.subroutine(0xB2CF, 'mask_owner_access', title='Clear FS selection flags from options word', description="""`AND`s the `&C271` (`hazel_fs_lib_flags`) byte with `&1F`, clearing the
FS selection flag (bit 6) and other high bits to retain only the
5-bit owner-access mask. Called before parsing to reset the prefix
state from a previous command. 12 callers.""", on_exit={'a': 'masked value'})


d.subroutine(0xB2E4, 'ex_print_col_sep', title='Print column separator or newline for *Ex/*Cat', description="""In *Cat mode, increments a column counter modulo 4
and prints a two-space separator between entries,
with a newline at the end of each row. In *Ex
mode (fs_spool_handle negative), prints a newline
after every entry. Scans the entry data and loops
back to print the next entry's characters.""")


d.subroutine(0xB327, 'print_num_no_leading', title='Print decimal number with leading zero suppression', description="""Sets `V=1` via `BIT always_set_v_byte` (the `&FF` constant at
&9769, whose bit 6 sets V) to enable leading-zero suppression
in [`print_decimal_3dig`](address:B32A), then falls through to
that routine. Used by [`print_station_id`](address:90C7) for
compact station number display.""", on_entry={'a': 'number to print (0-255)'})


d.subroutine(0xB32A, 'print_decimal_3dig', title='Print byte as 3-digit decimal via OSASCI', description="""Extracts hundreds, tens and units digits by
successive calls to print_decimal_digit. The V
flag controls leading zero suppression: if set,
zero digits are skipped until a non-zero digit
appears. V is always cleared before the units
digit to ensure at least one digit is printed.""", on_entry={'a': 'number to print (0-255)', 'v': 'set to suppress leading zeros'})


d.subroutine(0xB338, 'print_decimal_digit', title='Print one decimal digit by repeated subtraction', description="""Initialises X to '0'-1 and loops, incrementing X
while subtracting the divisor from Y. On underflow,
adds back the divisor to get the remainder in Y.
If V is set, suppresses leading zeros by skipping
the OSASCI call when the digit is '0'.""", on_entry={'a': 'divisor', 'y': 'value to divide'}, on_exit={'y': 'remainder after division'})


d.subroutine(0xB357, 'cmd_info_dispatch', title='*Info command handler', description="""Dispatched from the star-command table at index &28. Clears the
owner-only access bits via [`mask_owner_access`](address:B2CF),
then writes the two-byte FS command prefix `'i' '.'` into
[`hazel_txcb_data`](address:C105)/[`hazel_txcb_flag`](address:C106),
saves the command-line pointer with
[`save_ptr_to_os_text`](address:B373), parses the *Info argument
via [`parse_cmd_arg_y0`](address:B22A), copies it into the TX
buffer at offset 2 with [`copy_arg_to_buf`](address:B2A1), and
JMPs to [`send_cmd_and_dispatch`](address:8E3C) to send the
request to the file server.""", on_entry={'y': 'command-line offset in text pointer'})


d.subroutine(0xB373, 'save_ptr_to_os_text', title='Copy text pointer to OS text pointer workspace', description="""Saves fs_crc_lo/hi into the MOS text pointer
locations at &00F2/&00F3. Preserves A on the
stack. Called before GSINIT/GSREAD sequences
that need to parse from the current command
line position.""", on_exit={'a': 'preserved (PHA/PLA)'})


d.subroutine(0xB37F, 'skip_to_next_arg', title='Advance past spaces to the next command argument', description="""Scans (fs_crc_lo)+Y for space characters,
advancing Y past each one. Returns with A
holding the first non-space character, or CR
if the end of line is reached. Used by *CDir
and *Remove to detect extra arguments.""", on_entry={'y': 'starting offset (where to begin scanning)'}, on_exit={'a': 'first non-space character or CR', 'y': 'offset of that character'})


d.subroutine(0xB393, 'save_ptr_to_spool_buf', title='Copy text pointer to spool buffer pointer', description="""Saves fs_crc_lo/hi into fs_options/fs_block_offset
for use as the spool buffer pointer. Preserves A
on the stack. Called by *PS and *PollPS before
parsing their arguments.""", on_exit={'a': 'preserved (PHA/PLA)'})


d.subroutine(0xB39E, 'init_spool_drive', title='Initialise spool drive page pointers', description="""Calls get_ws_page to read the workspace page
number for the current ROM slot, stores it as
the spool drive page high byte (addr_work), and
clears the low byte (work_ae) to zero. Preserves
Y on the stack.""", on_exit={'a': '0', 'y': 'preserved (PHY/PLY)'})


d.subroutine(0xB3D5, 'copy_ps_data_y1c', title='Copy printer server template at offset &18', description="""Sets Y=&18 and falls through to copy_ps_data.
Called during workspace initialisation
(svc_2_private_workspace) to set up the printer
server template at the standard offset.""", on_exit={'y': '&20 (advanced past the copied 8 bytes)'})


d.subroutine(0xB3D7, 'copy_ps_data', title='Copy 8-byte printer server template to RX buffer', description="""Copies 8 bytes of default printer server data into the RX buffer
at the current `Y` offset. Uses indexed addressing: `LDA
ps_template_base,X` with `X` starting at `&F8`, so the effective
read address is `ps_template_base+&F8 = ps_template_data`
([`&8E9F`](address:8E9F)). The 6502 trick reaches data 248
bytes past the base label in a single instruction; the base
address (`ps_template_base`) deliberately falls inside the operand
byte of a JSR instruction at `&8DA6` -- see
docs/analysis/authors-easter-egg.md.""", on_entry={'y': 'destination offset within the RX buffer'}, on_exit={'y': 'advanced by 8', 'x': '0 (loop terminator)', 'a': 'last template byte'})

d.label(0xB441, 'read_ps_station_addr')


d.subroutine(0xB477, 'store_ps_station', title='Write printer-server station number into NFS workspace', description="""Stores fs_work_5/fs_work_6 (the parsed station/network bytes) into
nfs_workspace offsets 2 and 3 (the printer-server slot's station/
net pair). Single caller (cmd_ps's parse-success path at &B3D2).""")


d.subroutine(0xB483, 'print_file_server_is', title="Print 'File server ' prefix", description="""Uses print_inline to output 'File' then falls through
to the shared ' server is ' suffix at
print_printer_server_is.""", on_entry={}, on_exit={'a, x, y': 'clobbered (OSASCI via print_inline)'})


d.subroutine(0xB48D, 'print_printer_server_is', title="Print 'Printer server is ' prefix", description="""Uses print_inline to output the full label
'Printer server is ' with trailing space.""", on_entry={}, on_exit={'a, x, y': 'clobbered (OSASCI via print_inline)'})


d.subroutine(0xB4A8, 'load_ps_server_addr', title='Load printer server address from workspace', description="""Reads the station and network bytes from workspace
offsets 2 and 3 into the station/network variables.""", on_exit={'a, y': 'clobbered'})


d.subroutine(0xB4B4, 'pop_requeue_ps_scan', title='Pop return address and requeue PS slot scan', description="""Converts the PS slot flags to a workspace index,
writes slot data, and jumps back into the PS scan
loop to continue processing.""", on_entry={'a': 'PS slot flags byte to convert into a workspace index'})


d.subroutine(0xB4D6, 'skip_next_ps_slot', title='Advance to next PS slot, wrap if all 256 done', description="""INX / TXA / BNE loop_scan_ps_slots. Slot index in X advances; the
BNE re-enters the scan unless X has wrapped to zero (all 256
slots scanned). Single caller (the no-match path at &B4FF in the
PS slot scanner).""", on_entry={'x': 'current slot index'})


d.subroutine(0xB51C, 'write_ps_slot_byte_ff', title='Write buffer page byte and two &FF markers', description="""Stores the buffer page byte at the current Y offset
in workspace, followed by two &FF sentinel bytes.
Advances Y after each write.""", on_entry={'a': 'buffer page byte to store at workspace+Y', 'y': 'starting workspace offset'}, on_exit={'a': '&FF (the sentinel value left in A)', 'y': 'workspace offset advanced by 3 (one byte + two markers)'})


d.subroutine(0xB523, 'write_two_bytes_inc_y', title='Write A to two consecutive workspace bytes', description="""Stores A at the current Y offset via (nfs_workspace),Y
then again at Y+1, advancing Y after each write.""", on_entry={'a': 'byte to store', 'y': 'workspace offset'})


d.subroutine(0xB52B, 'reverse_ps_name_to_tx', title='Reverse-copy printer server name to TX buffer', description="""Copies 8 bytes from the RX buffer at offsets `&18..&1F`
(`(net_rx_ptr)+&18..+&1F`) to the TX buffer at offsets
`&10..&17` (`(net_rx_ptr)+&10..+&17`) in reversed byte order.
Implementation: pushes the 8 RX bytes onto the stack, then pops
them back to the TX area; the LIFO order achieves the reversal.""", on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xB556, 'print_station_addr', title='Print station address as decimal net.station', description="""If the network number is zero, prints only the
station number. Otherwise prints network.station
separated by a dot. V flag controls padding with
leading spaces for column alignment.""", on_entry={'v flag': 'set = no leading-space padding; clear = pad to align in a column'}, on_exit={'a, x, y': 'clobbered (print_decimal_3dig and OSASCI)'})


d.subroutine(0xB6A6, 'init_ps_slot_from_rx', title='Initialise PS slot buffer from template data', description="""Copies the 12-byte
[`ps_slot_txcb_template`](address:B575) into workspace at
offsets &78-&83 via indexed addressing from
`write_ps_slot_link_addr` (`write_ps_slot_hi_link+1`).
Substitutes `net_rx_ptr_hi` at offsets &7D and &81 (the hi bytes
of the two buffer pointers) so they point into the current RX
buffer page.""", on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xB6BD, 'store_char_uppercase', title='Convert to uppercase and store in RX buffer', description="""If the character in A is lowercase (&61-&7A), converts
to uppercase by clearing bit 5. Stores the result in
the RX buffer at the current position, advances the
buffer pointer, and decrements the character count.""", on_entry={'a': 'character to store'})


d.subroutine(0xB703, 'request_next_wipe', title="Build 'examine directory' TXCB for next wipe iteration", description="""Issues FS function-code 1 ('examine directory entry') for the
current iteration in fs_work_5. Writes the function code into
TXCB[5] and TXCB[7], copies the iteration index to TXCB[6], and
falls through to the TXCB-build / send sequence. Single caller
(the BNE retry at &B73F that loops cmd_wipe over each match).""")


d.subroutine(0xB7D3, 'flush_and_read_char', title='Flush keyboard buffer and read one character', description="""Calls OSBYTE &0F to flush the input buffer, then
OSRDCH to read a single character. Raises an escape
error if escape was pressed (carry set on return).""", on_entry={}, on_exit={'a': 'character read from keyboard', 'x, y': 'clobbered (OSBYTE/OSRDCH)'})


d.subroutine(0xB7E3, 'init_channel_table', title='Initialise channel allocation table', description="""Clears all 256 bytes of the table, then marks
available channel slots based on the count from
the receive buffer. Sets the first slot to &C0
(active channel marker).""", on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xB805, 'attr_to_chan_index', title='Convert channel attribute to table index', description="""Subtracts &20 from the attribute byte and clamps
to the range 0-&0F. Returns &FF if out of range.
Preserves processor flags via PHP/PLP.""", on_entry={'a': 'channel attribute byte'}, on_exit={'a': 'table index (0-&0F) or &FF if invalid'})


d.subroutine(0xB814, 'check_chan_char', title='Validate channel character and look up entry', description="""Characters below '0' are looked up directly in
the channel table. Characters '0' and above are
converted to a table index via attr_to_chan_index.
Raises 'Net channel' error if invalid.""", on_entry={'a': 'channel character'})


d.subroutine(0xB81C, 'err_net_chan_invalid', title="Raise 'Net channel' error (saving channel char on stack)", description="""Pushes the bad channel character on the stack, then falls through to
error_chan_not_found which loads error code &DE and tail-calls
error_inline_log with the inline string 'Net channel'. The PHA at
entry differs from the &B81D error_chan_not_found alt-entry: this
form is reached when the caller has the channel character in A and
wants it preserved on the stack for the error handler to inspect.
Never returns -- error_inline_log triggers a BRK.""", on_entry={'a': 'channel character (saved on stack)'})


d.subroutine(0xB847, 'lookup_chan_by_char', title='Look up channel by character code', description="""Subtracts `&20` from the character to produce a table index
(inlining the same arithmetic as
[`attr_to_chan_index`](address:B805) without the bounds check),
loads the channel slot's `hazel_fcb_slot_attr` byte; on zero
raises `error_chan_not_found`. Otherwise verifies station/network
via [`match_station_net`](address:B925) and returns the slot's
flags in `A`.""", on_entry={'a': 'channel character'}, on_exit={'a': 'channel flags'})


d.subroutine(0xB886, 'store_result_check_dir', title='Store channel attribute and check not directory', description="""Writes the current channel attribute to the receive
buffer, then tests the directory flag (bit 1). Raises
'Is a dir.' error if the attribute refers to a
directory rather than a file.""", on_entry={'a': 'channel attribute byte to store and check'})


d.subroutine(0xB88C, 'check_not_dir', title='Validate channel is not a directory', description="""Calls check_chan_char to validate the channel, then
tests the directory flag (bit 1). Raises 'Is a dir.'
error if the channel refers to a directory.""", on_entry={'a': 'channel character (validated by check_chan_char)'})


d.subroutine(0xB8A8, 'alloc_fcb_slot', title='Allocate a free file control block slot', description="""Scans FCB slots &20-&2F for an empty entry.
Returns Z=0 with X=slot index on success, or
Z=1 with A=0 if all slots are occupied.""", on_exit={'x': 'slot index (if Z=0)', 'z': '0=success, 1=no free slot'})


d.subroutine(0xB8DC, 'alloc_fcb_or_error', title='Allocate FCB slot or raise error', description="""Calls alloc_fcb_slot and raises 'No more FCBs'
if no free slot is available. Preserves the
caller's argument on the stack.""", on_entry={'a': "caller's argument byte (saved/restored via PHA/PLA across the alloc call)"}, on_exit={'x': 'newly allocated FCB slot index (&20-&2F)', 'a': 'preserved'})


d.subroutine(0xB8F8, 'close_all_net_chans', title='Close all network channels for current station', description="""Scans FCB slots &0F down to 0, closing those
matching the current station. C=0 closes all
matching entries; C=1 closes with write-flush.""", on_entry={'c': '0=close all, 1=close with write-flush'})


d.subroutine(0xB8FC, 'scan_fcb_flags', title='Scan FCB slot flags from &10 downward', description="""Iterates through FCB slots starting at &10,
checking each slot's flags byte. Returns when
all slots have been processed.""", on_exit={'x': 'last scanned FCB index', 'z flag': 'set if a matching slot was found (via fall-through into match_station_net)'})


d.subroutine(0xB925, 'match_station_net', title='Check FCB slot matches current station/network', description="""Compares the station and network numbers in the
FCB at slot X against the current values using
EOR. Returns Z=1 if both match, Z=0 if either
differs.""", on_entry={'x': 'FCB slot index'}, on_exit={'z': '1=match, 0=no match'})


d.subroutine(0xB934, 'find_open_fcb', title='Find next open FCB slot for current connection', description="""Scans from the current index, wrapping around at
the end. On the first pass finds active entries
matching the station; on the second pass finds
empty slots for new allocations.""", on_entry={'x': 'starting FCB index (search wraps)'}, on_exit={'x': 'FCB slot index of the matched (active) or first empty slot', 'z flag': 'match status (set when an entry was found)'})


d.subroutine(0xB977, 'init_wipe_counters', title='Initialise byte counters for wipe/transfer', description="""Sets `hazel_pass_counter` to 1 and clears
`hazel_byte_counter_lo`, `hazel_offset_counter` and
`hazel_transfer_flag`. Then stores `&FF` sentinels in
[`hazel_sentinel_cd`](address:C2CD) /
[`hazel_sentinel_ce`](address:C2CE). The HAZEL FS-state region
is at &C2xx in the 4.21 build.""", on_entry={}, on_exit={'x': 'small loop counter (last DEX value)', 'y': '0 (cleared by the TYA path)'})


d.subroutine(0xB99A, 'start_wipe_pass', title='Start wipe pass for current FCB', description="""Verifies the workspace checksum, saves the station
context (pushing station low/high), initialises
transfer counters via init_wipe_counters, and sends
the initial request via send_and_receive. Clears the
active and offset flags on completion.""", on_entry={'x': 'FCB slot index'})


d.subroutine(0xBA09, 'save_fcb_context', title='Save FCB context and process pending slots', description="""Copies 13 bytes from the TX buffer (&0F00) and
fs_load_addr workspace to temporary storage at
&10D9. If Y=0, skips to the restore loop. Otherwise
scans for pending FCB slots (bits 7+6 set), flushes
each via start_wipe_pass, allocates new slots via
find_open_fcb, and sends directory requests. Falls
through to restore_catalog_entry.""", on_entry={'y': 'filter attribute (0=process all)'})


d.subroutine(0xBAB7, 'loop_restore_workspace', title='Pop 13 saved workspace bytes back to fs_load_addr+', description="""Y=0..&0C loop: PLA / STA fs_load_addr,Y / INY / CPY #&0D / BNE.
Restores the 13-byte FS-options block that save_fcb_context pushed
on the stack, undoing the protection the wipe/scan path put in
place. Two callers: the JMP at &BA1B (close-and-restore exit) and
the BNE retry at &BABE.""")


d.subroutine(0xBAC0, 'restore_catalog_entry', title='Restore saved catalog entry to TX buffer', description="""Copies 13 bytes (Y=&0C..0) from
[`hazel_ctx_buffer`](address:C2D9) back to the TX buffer
starting at [`hazel_txcb_port`](address:C100). Falls through to
`find_matching_fcb`. (Pre-HAZEL ROMs read from `&10D9` and wrote
to `&0F00`; the 4.21 build relocates both to HAZEL.)""")


d.subroutine(0xBACC, 'loop_save_before_match', title='Save FCB context, fall into find_matching_fcb', description="""Single-instruction wrapper at the top of the per-iteration FCB
search retry: JSR save_fcb_context to preserve the current attempt's
state (offset, station, network), then fall through into
find_matching_fcb. Single caller (the BNE retry at &BAEB). Used
once the first scan past slot &0F has failed and the search needs
to restart from slot 0 with the saved context restored.""")


d.subroutine(0xBACF, 'find_matching_fcb', title='Find FCB slot matching channel attribute', description="""Scans FCB slots 0-&0F for an active entry whose
attribute reference matches hazel_chan_attr. Converts the
attribute to a channel index, then verifies the
station and network numbers. On the first scan
past slot &0F, saves context via save_fcb_context
and restarts. Returns Z=0 if the FCB has saved
offset data (bit 5 set).""", on_exit={'x': 'matching FCB index', 'z': '0=has offset data, 1=no offset'})


d.subroutine(0xBB2A, 'inc_fcb_byte_count', title='Increment 3-byte FCB transfer count', description="""Increments hazel_fcb_addr_lo+X (low), cascading overflow to
hazel_fcb_addr_mid+X (mid) and hazel_fcb_addr_hi+X (high).""", on_entry={'x': 'FCB slot index'})


d.subroutine(0xBB38, 'process_all_fcbs', title='Process all active FCB slots', description="""Saves 9 zero-page bytes (`&00B4`–`&00BC`, i.e. `fs_work_4`+0..+8)
on the stack via a `PHX`/`PHY`/loop preamble using the `&FFBD,X`
indexing-wrap trick (X = `&F7`..`&FF` wraps to `&00B4`..`&00BC`),
then scans FCB slots `&0F` down to 0.
Calls [`start_wipe_pass`](address:B99A) for each active entry
matching the filter attribute in `Y` (`0` = match all). Restores
all saved context on completion. Also contains the OSBGET/OSBPUT
inline logic for reading and writing bytes through file
channels.""", on_entry={'y': 'filter attribute (0=process all)'})


d.subroutine(0xBB68, 'bgetv_handler', title='BGETV vector handler: read byte from open file', description="""Reached via the BGETV vector at `&021A`, which the
[`fs_vector_table`](address:8EA7) entries copy into the MOS extended
vector area. Saves caller's `Y` in `hazel_chan_attr` (channel attribute slot),
pushes `X`, calls
[`store_result_check_dir`](address:B886) to validate the channel,
then either reads a byte from the FCB buffer (returning it in `A`
with `C=0`) or signals end-of-file (`C=1`).""", on_entry={'y': 'channel handle'}, on_exit={'a': 'byte read (when C=0)', 'c': '0 = byte returned, 1 = EOF / error'})


d.subroutine(0xBBE7, 'bputv_handler', title='BPUTV vector handler: write byte to open file', description="""Reached via the BPUTV vector at `&0218`. Saves caller's `Y` in
`hazel_chan_attr`, pushes the data byte and `X`, then routes to the FCB
buffer-write path: stores the byte in the channel's transmit
buffer, increments the byte count via
[`inc_fcb_byte_count`](address:BB2A), and exits via
[`done_inc_byte_count`](address:BC65).""", on_entry={'a': 'byte to write', 'y': 'channel handle'}, on_exit={'c': '0 = written, 1 = error'})


d.subroutine(0xBC65, 'done_inc_byte_count', title='Increment FCB byte count, clear rx attr, restore caller', description="""JSRs inc_fcb_byte_count for the active FCB, then A=0 / JSR
store_rx_attribute (clears the receive-attribute byte). Pulls
saved X back into X (caller's value), discards the saved data byte
on the stack and returns. Single caller (the OSBPUT/PRINT path at
&BC1F).""")


d.subroutine(0xBC74, 'flush_fcb_if_station_known', title='Flush FCB byte count to server if station is set', description="""Saves all registers, checks if the FCB has a
known station. If yes, sends the accumulated byte
count as a flush request to the file server. If no
station is set, falls through to flush_fcb_with_init
which saves FCB context first.""", on_entry={'Y': 'channel index (FCB slot)'}, on_exit={'A': 'preserved', 'X': 'preserved', 'Y': 'preserved'})


d.subroutine(0xBC7C, 'flush_fcb_with_init', title='Save FCB context and flush byte count to server', description="""Saves all registers and the current FCB context,
copies the FCB byte count into the TX command buffer,
and sends a flush/close request to the file server.
Restores the catalog entry and all registers on return.""", on_entry={'Y': 'channel index (FCB slot)'}, on_exit={'A': 'preserved', 'X': 'preserved', 'Y': 'preserved'})

d.label(0xBC89, 'store_station_and_flush')


d.subroutine(0xBCBC, 'send_wipe_request', title='Send wipe/close request packet', description="""Sets up the TX control block with function code
&90, the reply port from Y, and the data byte from
A. Sends via send_disconnect_reply, then checks the
error code — raises the server error if non-zero.""", on_entry={'a': 'data byte to send', 'y': 'reply port'})


d.subroutine(0xBD15, 'send_and_receive', title='Set up FS options and transfer workspace', description="""Calls set_options_ptr to configure the FS options
pointer, then jumps to setup_transfer_workspace to
initialise the transfer and send the request.""", on_entry={'a': 'transfer mode', 'x': 'workspace offset low', 'y': 'workspace page'})


d.subroutine(0xBD1B, 'read_rx_attribute', title='Read receive attribute byte from RX buffer', description="""Reads byte at offset &0A in the network receive
control block, used to track which channel owns the
current receive buffer.""", on_entry={}, on_exit={'A': 'receive attribute byte', 'Y': '&0A'})


d.subroutine(0xBD20, 'store_rx_attribute', title='Store receive attribute byte to RX buffer', description="""Writes A to offset &0A in the network receive
control block, marking which channel owns the
current receive buffer.""", on_entry={'A': 'attribute byte to store'}, on_exit={'Y': '&0A'})


d.subroutine(0xBD25, 'abort_if_escape', title='Test escape flag and abort if pressed', description="""Checks the escape flag byte; returns immediately
if bit 7 is clear. If escape has been pressed,
falls through to the escape abort handler which
acknowledges the escape via OSBYTE &7E.""")


d.subroutine(0xBD59, 'loop_dump_line', title='*DUMP per-line read loop', description="""Body of cmd_dump's outer line loop. Calls abort_if_escape, then
reads up to 16 bytes from the open file via OSBGET into the line
buffer at (work_ae). On EOF mid-line, breaks to clean-up; on a
full line, falls through to the formatting and print stage.
Reachable from the alignment branch at &BD54 and the per-line tail
at &BDF9.""")


d.subroutine(0xBD79, 'loop_pop_stack_buf', title='Drain saved bytes off stack and close', description="""Pulls X+1 bytes off the 6502 stack (clearing the temporary 21-byte
buffer cmd_dump uses to render each line) and tail-jumps to
close_ws_file. Reached from the in-line BPL at &BD7B and the
fall-through tail at &BDFE.""", on_entry={'x': 'stack-byte count - 1 (caller sets it to &14 or &15)'})


d.subroutine(0xBDBB, 'loop_next_dump_col', title='*DUMP per-column advance and end-of-line check', description="""INY (next buffer offset), CPY #&10. End -> done_print_separator.
Otherwise DEX (decrement byte counter); BPL loop_print_dump_hex
to print the next byte. Single caller (the BPL at &BDCC after
short-line padding).""", on_entry={'x': 'remaining bytes - 1', 'y': 'buffer offset'})


d.subroutine(0xBE01, 'print_dump_header', title='Print hex dump column header line', description="""Outputs the starting address followed by 16 hex
column numbers (00-0F), each separated by a space.
Provides the column alignment header for *Dump
output.""", on_exit={'a, x, y': 'clobbered (print_hex_byte + OSASCI loop)'})


d.subroutine(0xBE37, 'print_hex_and_space', title='Print hex byte followed by space', description="""Saves A, prints it as a 2-digit hex value via
print_hex_byte, outputs a space character, then
restores A from the stack. Used by cmd_dump and
print_dump_header for column-aligned hex output.""", on_entry={'a': 'byte value to print'})


d.subroutine(0xBF71, 'close_ws_file', title='Close file handle stored in workspace', description="""Loads the file handle from ws_page and closes it
via OSFIND with A=0.""", on_exit={'a, x, y': 'clobbered (OSFIND)'})


d.subroutine(0xBF78, 'open_file_for_read', title='Open file for reading via OSFIND', description="""Computes the filename address from the command text
pointer plus the Y offset, calls OSFIND with A=&40
(open for input). Stores the handle in ws_page.
Raises 'Not found' if the returned handle is zero.""", on_entry={'y': 'offset within the command line of the filename to open'}, on_exit={'a, x, y': 'clobbered'})

d.label(0xBF9E, 'restore_text_ptr')

d.label(0xBFB8, 'done_skip_filename')


d.subroutine(0xBE42, 'parse_dump_range', title='Parse hex address for dump range', description="""Reads up to 4 hex digits from the command line
into a 4-byte accumulator, stopping at CR or
space. Each digit shifts the accumulator left
by 4 bits before ORing in the new nybble.""", on_entry={'y': 'current command-line offset'}, on_exit={'y': 'advanced past the parsed digits', 'a': 'first non-hex character (CR or space)'})


d.subroutine(0xBE4E, 'loop_parse_hex_digit', title='*DUMP / *LIST hex-address parser per-character body', description="""Reload command-line offset from X, INX (step cursor), TAY (use as
indirect index), read (os_text_ptr),Y. Branches: CR -> done; space
-> end of token; otherwise validate hex digit and shift it into the
4-byte accumulator. Single caller (the BNE retry at &BE95).""", on_entry={'x': 'current command-line offset'})


d.subroutine(0xBEAB, 'init_dump_buffer', title='Initialise dump buffer and parse address range', description="""Parses the start and end addresses from the command
line via parse_dump_range. If no end address is given,
defaults to the file extent. Validates both addresses
against the file size, raising 'Outside file' if either
exceeds the extent.""", on_entry={'y': 'command-line offset of the address arguments'})


d.subroutine(0xBFBA, 'advance_x_by_8', title='Advance X by 16 via nested JSR + fall-through', description="""**Note:** the name is historical and misleading -- this routine
actually advances `X` by 16, not 8.

`JSR advance_x_by_4` followed by no `RTS`, so control falls
through into [`advance_x_by_4`](address:BFBD) itself for a
second pass. Each pass through `advance_x_by_4` runs `inx4`
twice (8 INXs), so two passes give 16 INXs in total.""", on_entry={'x': 'value to advance'}, on_exit={'x': 'input + 16', 'a, y': 'preserved'})


d.subroutine(0xBFBD, 'advance_x_by_4', title='Advance X by 8 via JSR and fall-through', description="""**Note:** the name is historical and misleading -- this routine
actually advances `X` by 8, not 4.

`JSR inx4` (4 INXs); the JSR's RTS lands at &BFC0 which is
[`inx4`](address:BFC0)'s entry, so a second pass runs by fall-
through (4 more INXs). Total: 8 INXs.""", on_entry={'x': 'value to advance'}, on_exit={'x': 'input + 8', 'a, y': 'preserved'})


d.subroutine(0xBFC0, 'inx4', title='Increment X four times', description="""Four consecutive INX instructions. Used as a
building block by advance_x_by_4 and
advance_x_by_8 via JSR/fall-through chaining.""", on_entry={'x': 'value to advance'}, on_exit={'x': 'input + 4', 'a, y': 'preserved', 'n, z flags': 'reflect new X'})
d.comment(0x8006, 'ROM type: service + language', align=Align.INLINE)
d.comment(0x8019, 'Null terminator before copyright', align=Align.INLINE)
d.comment(0x803A, 'Copy to A for sign test', align=Align.INLINE)
d.comment(0x803B, 'Bit 7 set: dispatch via table', align=Align.INLINE)
d.comment(0x803D, 'A=&FE: Econet receive event', align=Align.INLINE)
d.comment(0x8042, 'Fire event (enable: *FX52,150)', align=Align.INLINE)
d.comment(0x8045, 'Dispatch through event vector', align=Align.INLINE)
d.comment(0x803F, 'Call event vector handler', align=Align.INLINE)
d.comment(0x8048, 'Push return addr high (&85)', align=Align.INLINE)
d.comment(0x804A, 'High byte on stack for RTS', align=Align.INLINE)
d.comment(0x804B, 'Load dispatch target low byte', align=Align.INLINE)
d.comment(0x804E, 'Low byte on stack for RTS', align=Align.INLINE)
d.comment(0x804F, "RTS = dispatch to PHA'd address", align=Align.INLINE)
d.comment(0x8050, 'INTOFF: read station ID, disable NMIs', align=Align.INLINE)
d.comment(0x8053, 'Full ADLC hardware reset', align=Align.INLINE)
d.comment(0x8056, 'OSBYTE &EA: check Tube co-processor', align=Align.INLINE)
d.comment(0x8058, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x805A, 'Clear Econet init flag before setup', align=Align.INLINE)
d.comment(0x8063, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x8065, 'X=&0C: NMI claim service', align=Align.INLINE)
d.comment(0x805D, 'Check Tube presence via OSBYTE &EA', align=Align.INLINE)
d.comment(0x8060, 'Store Tube presence flag from OSBYTE &EA', align=Align.INLINE)
d.comment(0x8067, 'Issue NMI claim service request', align=Align.INLINE)
d.comment(0x806A, 'Y=5: NMI claim service number', align=Align.INLINE)
d.comment(0x806C, 'Check if NMI service was claimed (Y changed)', align=Align.INLINE)
d.comment(0x806E, 'Service claimed by other ROM: skip init', align=Align.INLINE)
d.comment(0x8070, 'Copy NMI shim from ROM to &0D0C area', align=Align.INLINE)
d.comment(0x8072, 'Read byte from NMI shim ROM source', align=Align.INLINE)
d.comment(0x8075, 'Write to NMI shim RAM (start of NFS workspace)', align=Align.INLINE)
d.comment(0x8078, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8079, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x807B, 'Patch current ROM bank into NMI shim', align=Align.INLINE)
d.comment(0x807D, 'Self-modifying code: ROM bank at &0D07', align=Align.INLINE)
d.comment(0x8080, 'Clear source network (Y=0 from copy loop)', align=Align.INLINE)
d.comment(0x8083, 'Clear Tube release flag', align=Align.INLINE)
d.comment(0x8085, 'Clear TX operation type', align=Align.INLINE)
d.comment(0x808F, '&80 = Econet initialised', align=Align.INLINE)
d.comment(0x8091, 'Mark TX as complete (ready)', align=Align.INLINE)
d.comment(0x8094, 'Mark Econet as initialised', align=Align.INLINE)
d.comment(0x8097, 'INTON: re-enable NMIs (&FE20 read side effect)', align=Align.INLINE)
d.comment(0x809A, 'Return', align=Align.INLINE)
d.comment(0x809B, 'A=&01: mask for SR2 bit0 (AP = Address Present)', align=Align.INLINE)
d.comment(0x809D, 'Z = A AND SR2 -- tests if AP is set', align=Align.INLINE)
d.comment(0x80A0, 'AP not set, no incoming data -- check for errors', align=Align.INLINE)
d.comment(0x80A2, 'Read first RX byte (destination station address)', align=Align.INLINE)
d.comment(0x80A5, 'Compare to our station ID (&FE18 read = INTOFF, disables NMIs)', align=Align.INLINE)
d.comment(0x80A8, 'Match -- accept frame', align=Align.INLINE)
d.comment(0x80AA, 'Check for broadcast address (&FF)', align=Align.INLINE)
d.comment(0x80AC, 'Neither our address nor broadcast -- reject frame', align=Align.INLINE)
d.comment(0x80AE, 'Flag &40 = broadcast frame', align=Align.INLINE)
d.comment(0x80B0, 'Store broadcast flag in rx_src_net', align=Align.INLINE)
d.comment(0x80B3, 'Install nmi_rx_scout_net NMI handler', align=Align.INLINE)
d.comment(0x80B5, 'Install next handler', align=Align.INLINE)
d.comment(0x80B8, 'Test SR2 for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x80BB, 'No RDA -- check errors', align=Align.INLINE)
d.comment(0x80BD, 'Read destination network byte', align=Align.INLINE)
d.comment(0x80C0, 'Network = 0 -- local network, accept', align=Align.INLINE)
d.comment(0x80C2, 'Test if network = &FF (broadcast)', align=Align.INLINE)
d.comment(0x80C4, 'Broadcast network -- accept', align=Align.INLINE)
d.comment(0x80C6, 'Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x80C8, 'Write CR1 to discontinue RX', align=Align.INLINE)
d.comment(0x80CB, 'Return to idle scout listening', align=Align.INLINE)
d.comment(0x80CE, 'Network = 0 (local): clear tx_flags', align=Align.INLINE)
d.comment(0x80D1, 'Store Y offset for scout data buffer', align=Align.INLINE)
d.comment(0x80D3, 'Install scout data handler', align=Align.INLINE)
d.comment(0x80D5, 'Install scout data loop', align=Align.INLINE)
d.comment(0x80D8, 'Read SR2', align=Align.INLINE)
d.comment(0x80DB, 'Test AP (b0) | RDA (b7)', align=Align.INLINE)
d.comment(0x80DD, 'Neither set -- clean end, discard frame', align=Align.INLINE)
d.comment(0x80DF, 'Unexpected data/status: full ADLC reset', align=Align.INLINE)
d.comment(0x80E2, 'Discard and return to idle', align=Align.INLINE)
d.comment(0x80E5, 'Gentle discard: RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x80E8, 'Y = buffer offset', align=Align.INLINE)
d.comment(0x80EA, 'Read SR2', align=Align.INLINE)
d.comment(0x80ED, 'No RDA -- error handler', align=Align.INLINE)
d.comment(0x80EF, 'Read data byte from RX FIFO', align=Align.INLINE)
d.comment(0x80F2, 'Store at &0D3D+Y (scout buffer)', align=Align.INLINE)
d.comment(0x80F5, 'Advance buffer index', align=Align.INLINE)
d.comment(0x80F6, 'Read SR2 again (FV detection point)', align=Align.INLINE)
d.comment(0x80F9, 'RDA set -- more data, read second byte', align=Align.INLINE)
d.comment(0x80FB, 'SR2 non-zero (FV or other) -- scout completion', align=Align.INLINE)
d.comment(0x80FD, 'Read second byte of pair', align=Align.INLINE)
d.comment(0x8100, 'Store at &0D3D+Y', align=Align.INLINE)
d.comment(0x8103, 'Advance and check buffer limit', align=Align.INLINE)
d.comment(0x8104, 'Copied all 12 scout bytes?', align=Align.INLINE)
d.comment(0x8106, 'Buffer full (Y=12) -- force completion', align=Align.INLINE)
d.comment(0x8108, 'Save final buffer offset', align=Align.INLINE)
d.comment(0x810A, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x810D, 'SR2 non-zero -- loop back for more bytes', align=Align.INLINE)
d.comment(0x810F, 'SR2 = 0 -- wait for next NMI', align=Align.INLINE)
d.comment(0x8112, 'Save Y for next iteration', align=Align.INLINE)
d.comment(0x8114, 'Write CR1', align=Align.INLINE)
d.comment(0x8117, 'CR2=&84: disable PSE, enable RDA_SUPPRESS_FV', align=Align.INLINE)
d.comment(0x8119, 'Write CR2', align=Align.INLINE)
d.comment(0x811C, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x811E, 'Test SR2 FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x8121, 'No FV -- not a valid frame end, error', align=Align.INLINE)
d.comment(0x8123, 'FV set but no RDA -- missing last byte, error', align=Align.INLINE)
d.comment(0x8125, 'Read last byte from RX FIFO', align=Align.INLINE)
d.comment(0x8128, 'Store last byte at &0D3D+Y', align=Align.INLINE)
d.comment(0x812B, 'CR1=&44: RX_RESET | TIE (switch to TX for ACK)', align=Align.INLINE)
d.comment(0x812D, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x8130, 'Set bit7 of need_release_tube flag', align=Align.INLINE)
d.comment(0x8131, 'Rotate C=1 into bit7: mark Tube release needed', align=Align.INLINE)
d.comment(0x8133, 'Check port byte: 0 = immediate op, non-zero = data transfer', align=Align.INLINE)
d.comment(0x8136, 'Port non-zero -- look for matching receive block', align=Align.INLINE)
d.comment(0x8138, 'Port = 0 -- immediate operation handler', align=Align.INLINE)
d.comment(0x813B, 'Check if broadcast (bit6 of tx_flags)', align=Align.INLINE)
d.comment(0x813E, 'Not broadcast -- skip CR2 setup', align=Align.INLINE)
d.comment(0x8140, 'CR2=&07: broadcast prep', align=Align.INLINE)
d.comment(0x8142, 'Write CR2: broadcast frame prep', align=Align.INLINE)
d.comment(0x8145, 'Check if RX port list active (bit7)', align=Align.INLINE)
d.comment(0x8148, 'No active ports -- try NFS workspace', align=Align.INLINE)
d.comment(0x814A, 'Start scanning port list at page &C0', align=Align.INLINE)
d.comment(0x814C, 'Y=0: start offset within each port slot', align=Align.INLINE)
d.comment(0x814E, 'Store page to workspace pointer low', align=Align.INLINE)
d.comment(0x8150, 'Store page high byte for slot scanning', align=Align.INLINE)
d.comment(0x8152, 'Y=0: read control byte from start of slot', align=Align.INLINE)
d.comment(0x8154, 'Read port control byte from slot', align=Align.INLINE)
d.comment(0x8156, 'Zero = end of port list, no match', align=Align.INLINE)
d.comment(0x8158, '&7F = any-port wildcard', align=Align.INLINE)
d.comment(0x815A, 'Not wildcard -- check specific port match', align=Align.INLINE)
d.comment(0x815C, 'Y=1: advance to port byte in slot', align=Align.INLINE)
d.comment(0x815D, 'Read port number from slot (offset 1)', align=Align.INLINE)
d.comment(0x815F, 'Zero port in slot = match any port', align=Align.INLINE)
d.comment(0x8161, 'Check if port matches this slot', align=Align.INLINE)
d.comment(0x8164, 'Port mismatch -- try next slot', align=Align.INLINE)
d.comment(0x8166, 'Y=2: advance to station byte', align=Align.INLINE)
d.comment(0x8167, 'Read station filter from slot (offset 2)', align=Align.INLINE)
d.comment(0x8169, 'Zero station = match any station, accept', align=Align.INLINE)
d.comment(0x816B, 'Check if source station matches', align=Align.INLINE)
d.comment(0x816E, 'Station mismatch -- try next slot', align=Align.INLINE)
d.comment(0x8170, 'Y=3: advance to network byte', align=Align.INLINE)
d.comment(0x8171, 'Read network filter from slot (offset 3)', align=Align.INLINE)
d.comment(0x8173, 'Zero = accept any network', align=Align.INLINE)
d.comment(0x8175, 'Check if source network matches', align=Align.INLINE)
d.comment(0x8178, 'Network matches or zero = accept', align=Align.INLINE)
d.comment(0x817A, 'Check if NFS workspace search pending', align=Align.INLINE)
d.comment(0x817C, 'No NFS workspace -- try fallback path', align=Align.INLINE)
d.comment(0x817E, 'Load current slot base address', align=Align.INLINE)
d.comment(0x8180, 'For 12-byte slot advance', align=Align.INLINE)
d.comment(0x8181, 'Advance to next 12-byte port slot', align=Align.INLINE)
d.comment(0x8183, 'Update workspace pointer to next slot', align=Align.INLINE)
d.comment(0x8185, "Always branches (page &C0 won't overflow)", align=Align.INLINE)
d.comment(0x8187, 'No match found -- discard frame', align=Align.INLINE)
d.comment(0x818A, 'Try NFS workspace if paged list exhausted', align=Align.INLINE)
d.comment(0x818D, 'No NFS workspace RX (bit6 clear) -- discard', align=Align.INLINE)
d.comment(0x818F, 'NFS workspace starts at offset 0 in page', align=Align.INLINE)
d.comment(0x8191, 'NFS workspace high byte for port list', align=Align.INLINE)
d.comment(0x8193, 'Scan NFS workspace port list', align=Align.INLINE)
d.comment(0x8195, 'Match found: set scout_status = 3', align=Align.INLINE)
d.comment(0x8197, 'Record match for completion handler', align=Align.INLINE)
d.comment(0x819A, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x819D, 'C=0: no Tube claimed -- discard', align=Align.INLINE)
d.comment(0x819F, 'Check broadcast flag for ACK path', align=Align.INLINE)
d.comment(0x81A2, 'Not broadcast -- normal ACK path', align=Align.INLINE)
d.comment(0x81A4, 'Broadcast: different completion path', align=Align.INLINE)
d.comment(0x81A7, 'CR1=&44: RX_RESET | TIE', align=Align.INLINE)
d.comment(0x81A9, 'Write CR1: TX mode for ACK', align=Align.INLINE)
d.comment(0x81AC, 'CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE', align=Align.INLINE)
d.comment(0x81AE, 'Write CR2: enable TX with PSE', align=Align.INLINE)
d.comment(0x81B1, 'Install data_rx_setup at &81B8', align=Align.INLINE)
d.comment(0x81B3, 'High byte of data_rx_setup handler', align=Align.INLINE)
d.comment(0x81B5, 'Send ACK with data_rx_setup as next NMI', align=Align.INLINE)
d.comment(0x81B8, 'CR1=&82: TX_RESET | RIE (switch to RX for data frame)', align=Align.INLINE)
d.comment(0x81BA, 'Write CR1: switch to RX for data frame', align=Align.INLINE)
d.comment(0x81BD, 'Install nmi_data_rx at &81E7', align=Align.INLINE)
d.comment(0x81BF, 'Install nmi_data_rx and return from NMI', align=Align.INLINE)
d.comment(0x81C2, 'A=1: AP mask for SR2 bit test', align=Align.INLINE)
d.comment(0x81C4, 'Test SR2 AP bit', align=Align.INLINE)
d.comment(0x81C7, 'No AP: wrong frame or error', align=Align.INLINE)
d.comment(0x81C9, 'Read first byte (dest station)', align=Align.INLINE)
d.comment(0x81CC, 'Compare to our station ID (INTOFF)', align=Align.INLINE)
d.comment(0x81CF, 'Not for us: error path', align=Align.INLINE)
d.comment(0x81D1, 'Install nmi_data_rx_net check handler', align=Align.INLINE)
d.comment(0x81D3, 'Set NMI vector via RAM shim', align=Align.INLINE)
d.comment(0x81D6, 'Validate source network = 0', align=Align.INLINE)
d.comment(0x81D9, 'SR2 bit7 clear: no data ready -- error', align=Align.INLINE)
d.comment(0x81DB, 'Read dest network byte', align=Align.INLINE)
d.comment(0x81DE, 'Network != 0: wrong network -- error', align=Align.INLINE)
d.comment(0x81E0, 'Install skip handler at &8211', align=Align.INLINE)
d.comment(0x81E2, 'High byte of &8211 handler', align=Align.INLINE)
d.comment(0x81E4, 'SR1 bit7: IRQ, data already waiting', align=Align.INLINE)
d.comment(0x81E7, 'Data ready: skip directly, no return', align=Align.INLINE)
d.comment(0x81E9, 'Install handler and return', align=Align.INLINE)
d.comment(0x81EC, 'Test SR2 RDA (RX data byte ready)', align=Align.INLINE)
d.comment(0x81EF, 'SR2 bit7 clear: error', align=Align.INLINE)
d.comment(0x81F1, 'Discard control byte', align=Align.INLINE)
d.comment(0x81F4, 'Discard port byte', align=Align.INLINE)
d.comment(0x81F7, 'A=2: Tube transfer flag mask', align=Align.INLINE)
d.comment(0x81F9, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x81FC, 'Tube active: use Tube RX path', align=Align.INLINE)
d.comment(0x81FE, 'A=&23: low byte of nmi_data_rx_bulk (&8223)', align=Align.INLINE)
d.comment(0x8200, 'Y=&82: high byte of nmi_data_rx_bulk', align=Align.INLINE)
d.comment(0x8202, 'SR1 bit7: more data already waiting?', align=Align.INLINE)
d.comment(0x8205, 'Yes: enter bulk read directly', align=Align.INLINE)
d.comment(0x8207, 'No: install handler', align=Align.INLINE)
d.comment(0x820A, 'A=&91: low byte of nmi_data_rx_tube (&8291)', align=Align.INLINE)
d.comment(0x820C, 'Y=&82: high byte of nmi_data_rx_tube', align=Align.INLINE)
d.comment(0x820E, 'Install Tube handler', align=Align.INLINE)
d.comment(0x8211, """Page-overflow exit from nmi_data_rx_bulk: restores the Master 128 ACCCON
that was saved at &822A before falling through to the RXCB-update path.""")
d.comment(0x8211, 'Pull saved ACCCON from stack', align=Align.INLINE)
d.comment(0x8212, "Restore caller's ACCCON on page-overflow exit", align=Align.INLINE)
d.comment(0x8215, 'Check tx_flags for error path', align=Align.INLINE)
d.comment(0x8218, 'Bit7 clear: RX error path', align=Align.INLINE)
d.comment(0x821A, 'Bit7 set: TX result = not listening', align=Align.INLINE)
d.comment(0x821D, 'Full ADLC reset on RX error', align=Align.INLINE)
d.comment(0x8220, 'Discard and return to idle listen', align=Align.INLINE)
d.comment(0x8223, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x8225, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x8228, 'SR2 bit7 clear: frame complete (FV)', align=Align.INLINE)
d.comment(0x822A, """4.21 Master 128: save/restore ACCCON across the (open_port_buf),Y stores
in this bulk-read loop. Same idiom as in copy_scout_to_buffer; workspace
&97 holds the desired ACCCON value pre-loaded by the caller.""")
d.comment(0x822A, 'Save current ACCCON on stack (Master 128)', align=Align.INLINE)
d.comment(0x822D, 'Push ACCCON snapshot', align=Align.INLINE)
d.comment(0x822E, 'Load desired ACCCON from workspace &97', align=Align.INLINE)
d.comment(0x8230, 'Set ACCCON for the upcoming buffer stores', align=Align.INLINE)
d.comment(0x8233, 'Read first byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x8236, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x8238, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8239, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x823B, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x823D, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x823F, 'No pages left: handle as complete', align=Align.INLINE)
d.comment(0x8241, 'Read SR2 between byte pairs', align=Align.INLINE)
d.comment(0x8244, 'SR2 bit7 set: more data available', align=Align.INLINE)
d.comment(0x8246, 'SR2 non-zero, bit7 clear: frame done', align=Align.INLINE)
d.comment(0x8248, 'Read second byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x824B, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x824D, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x824E, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x8250, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x8252, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x8254, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x8256, 'No pages left: frame complete', align=Align.INLINE)
d.comment(0x825C, 'Re-poll ADLC SR2 for next byte pair', align=Align.INLINE)
d.comment(0x825F, 'More data: loop back to data_rx_loop', align=Align.INLINE)
d.comment(0x8261, 'No more data: return from NMI', align=Align.INLINE)
d.comment(0x8258, 'Pull saved ACCCON from stack', align=Align.INLINE)
d.comment(0x8259, "Restore caller's ACCCON between byte pairs", align=Align.INLINE)
d.comment(0x8264, 'Pull saved ACCCON (frame-complete path)', align=Align.INLINE)
d.comment(0x8265, "Restore caller's ACCCON before completion", align=Align.INLINE)
d.comment(0x8268, 'A=&84: CR2 value (disable PSE)', align=Align.INLINE)
d.comment(0x826A, 'Write CR2 = &84 to disable PSE for bit testing', align=Align.INLINE)
d.comment(0x826D, 'A=0: CR1 value (disable all interrupts)', align=Align.INLINE)
d.comment(0x826F, 'Write CR1 = 0 to disable all interrupts', align=Align.INLINE)
d.comment(0x8272, 'Save Y (byte count from data RX loop)', align=Align.INLINE)
d.comment(0x8274, 'A=&02: FV mask', align=Align.INLINE)
d.comment(0x8276, 'Test SR2 FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x8279, 'No FV -- error', align=Align.INLINE)
d.comment(0x827B, 'FV set, no RDA -- proceed to ACK', align=Align.INLINE)
d.comment(0x827D, 'Check if buffer space remains', align=Align.INLINE)
d.comment(0x827F, 'No buffer space: error/discard frame', align=Align.INLINE)
d.comment(0x8281, 'FV+RDA: read and store last data byte', align=Align.INLINE)
d.comment(0x8284, 'Y = current buffer write offset', align=Align.INLINE)
d.comment(0x8286, 'Store last byte in port receive buffer', align=Align.INLINE)
d.comment(0x8288, 'Advance buffer write offset', align=Align.INLINE)
d.comment(0x828A, 'No page wrap: proceed to send ACK', align=Align.INLINE)
d.comment(0x828C, 'Page boundary: advance buffer page', align=Align.INLINE)
d.comment(0x828E, 'Send ACK frame to complete handshake', align=Align.INLINE)
d.comment(0x8291, 'Read SR2 for Tube data receive path', align=Align.INLINE)
d.comment(0x8294, 'RDA clear: no more data, frame complete', align=Align.INLINE)
d.comment(0x8296, 'Read data byte from ADLC RX FIFO', align=Align.INLINE)
d.comment(0x8299, 'Check buffer limits and transfer size', align=Align.INLINE)
d.comment(0x829C, 'Zero: buffer full, handle as error', align=Align.INLINE)
d.comment(0x829E, 'Send byte to Tube data register 3', align=Align.INLINE)
d.comment(0x82A1, 'Read second data byte (paired transfer)', align=Align.INLINE)
d.comment(0x82A4, 'Send second byte to Tube', align=Align.INLINE)
d.comment(0x82A7, 'Check limits after byte pair', align=Align.INLINE)
d.comment(0x82AA, 'Zero: Tube transfer complete', align=Align.INLINE)
d.comment(0x82AC, 'Re-read SR2 for next byte pair', align=Align.INLINE)
d.comment(0x82AF, 'More data available: continue loop', align=Align.INLINE)
d.comment(0x82B1, 'Unexpected end: return from NMI', align=Align.INLINE)
d.comment(0x82B4, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x82B6, 'Write CR1 for individual bit testing', align=Align.INLINE)
d.comment(0x82B9, 'CR2=&84: disable PSE', align=Align.INLINE)
d.comment(0x82BB, 'Write CR2: same pattern as main path', align=Align.INLINE)
d.comment(0x82BE, 'A=&02: FV mask for Tube completion', align=Align.INLINE)
d.comment(0x82C0, 'Test SR2 FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x82C3, 'No FV: incomplete frame, error', align=Align.INLINE)
d.comment(0x82C5, 'FV set, no RDA: proceed to ACK', align=Align.INLINE)
d.comment(0x82C7, 'Check if any buffer was allocated', align=Align.INLINE)
d.comment(0x82C9, 'OR all 4 buffer pointer bytes together', align=Align.INLINE)
d.comment(0x82CB, 'Check buffer low byte', align=Align.INLINE)
d.comment(0x82CD, 'Check buffer high byte', align=Align.INLINE)
d.comment(0x82CF, 'All zero (null buffer): error', align=Align.INLINE)
d.comment(0x82D1, 'Read extra trailing byte from FIFO', align=Align.INLINE)
d.comment(0x82D4, 'Save extra byte in workspace for later use', align=Align.INLINE)
d.comment(0x82D7, 'Bit5 = extra data byte available flag', align=Align.INLINE)
d.comment(0x82D9, 'Set extra byte flag in tx_flags', align=Align.INLINE)
d.comment(0x82DC, 'Store updated flags', align=Align.INLINE)
d.comment(0x82DF, 'Load TX flags to check ACK type', align=Align.INLINE)
d.comment(0x82E2, 'Bit7 clear: normal scout ACK', align=Align.INLINE)
d.comment(0x82E4, 'Final ACK: call completion handler', align=Align.INLINE)
d.comment(0x82E7, 'Jump to TX success result', align=Align.INLINE)
d.comment(0x82EA, 'CR1=&44: RX_RESET | TIE (switch to TX mode)', align=Align.INLINE)
d.comment(0x82EC, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x82EF, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x82F1, 'Write CR2: enable TX with status clear', align=Align.INLINE)
d.comment(0x82F4, 'Install saved next handler (scout ACK path)', align=Align.INLINE)
d.comment(0x82F6, 'High byte of post-ACK handler', align=Align.INLINE)
d.comment(0x82F8, 'Store next handler low byte', align=Align.INLINE)
d.comment(0x82FB, 'Store next handler high byte', align=Align.INLINE)
d.comment(0x82FE, 'Load dest station from RX scout buffer', align=Align.INLINE)
d.comment(0x8301, 'Test SR1 TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x8304, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x8306, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x8309, 'Load dest network from RX scout buffer', align=Align.INLINE)
d.comment(0x830C, 'Write dest net byte to FIFO', align=Align.INLINE)
d.comment(0x830F, 'A=&16: low byte of nmi_ack_tx_src (&8316)', align=Align.INLINE)
d.comment(0x8311, 'High byte of nmi_ack_tx_src', align=Align.INLINE)
d.comment(0x8313, 'Set NMI vector to ack_tx_src handler', align=Align.INLINE)
d.comment(0x8316, 'Load our station ID from workspace copy', align=Align.INLINE)
d.comment(0x8319, 'Test SR1 TDRA', align=Align.INLINE)
d.comment(0x831C, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x831E, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x8321, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x8323, 'Write network=0 (local) to TX FIFO', align=Align.INLINE)
d.comment(0x8326, 'Check tx_flags for data phase', align=Align.INLINE)
d.comment(0x8329, 'bit7 set: start data TX phase', align=Align.INLINE)
d.comment(0x832B, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x832D, 'Write CR2 to clear status after ACK TX', align=Align.INLINE)
d.comment(0x8330, 'Install saved handler from &0D4B/&0D4C', align=Align.INLINE)
d.comment(0x8333, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x8336, 'Install next NMI handler', align=Align.INLINE)
d.comment(0x8339, 'Jump to start data TX phase', align=Align.INLINE)
d.comment(0x833C, 'Jump to error handler', align=Align.INLINE)
d.comment(0x833F, 'A=2: test bit1 of tx_flags', align=Align.INLINE)
d.comment(0x8341, 'Check tx_flags data-transfer bit', align=Align.INLINE)
d.comment(0x8344, 'Bit1 clear: no transfer -- return', align=Align.INLINE)
d.comment(0x8346, 'Init carry for 4-byte add', align=Align.INLINE)
d.comment(0x8347, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x8348, 'Y=8: start at byte 0 of the 4-byte RXCB pointer', align=Align.INLINE)
d.comment(0x834A, 'Load RXCB[Y] (buffer pointer byte)', align=Align.INLINE)
d.comment(0x834C, 'Restore carry from stack', align=Align.INLINE)
d.comment(0x834D, 'Add transfer count byte', align=Align.INLINE)
d.comment(0x8350, 'Store updated pointer back to RXCB', align=Align.INLINE)
d.comment(0x8352, 'Next byte', align=Align.INLINE)
d.comment(0x8353, 'Save carry for next iteration', align=Align.INLINE)
d.comment(0x8354, 'Done 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x8356, 'No: continue adding', align=Align.INLINE)
d.comment(0x8358, 'Discard final carry', align=Align.INLINE)
d.comment(0x8359, 'A=&20: test bit5 of tx_flags', align=Align.INLINE)
d.comment(0x835B, 'Check tx_flags Tube bit', align=Align.INLINE)
d.comment(0x835E, 'No Tube: skip Tube update', align=Align.INLINE)
d.comment(0x8360, 'Save X on stack', align=Align.INLINE)
d.comment(0x8361, 'Push X', align=Align.INLINE)
d.comment(0x8362, 'A=8: offset for Tube address', align=Align.INLINE)
d.comment(0x8364, 'For address calculation', align=Align.INLINE)
d.comment(0x8365, 'Add workspace base offset', align=Align.INLINE)
d.comment(0x8367, 'X = address low for Tube claim', align=Align.INLINE)
d.comment(0x8368, 'Y = address high for Tube claim', align=Align.INLINE)
d.comment(0x836A, 'A=1: Tube claim type (read)', align=Align.INLINE)
d.comment(0x836C, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x836F, 'Load extra RX data byte', align=Align.INLINE)
d.comment(0x8372, 'Send to Tube via R3', align=Align.INLINE)
d.comment(0x8375, 'Init carry for increment', align=Align.INLINE)
d.comment(0x8376, 'Y=8: start at byte 0 of the 4-byte RXCB pointer', align=Align.INLINE)
d.comment(0x8378, 'A=0: add carry only (increment)', align=Align.INLINE)
d.comment(0x837A, 'Add carry to pointer byte', align=Align.INLINE)
d.comment(0x837C, 'Store back to RXCB', align=Align.INLINE)
d.comment(0x837E, 'Next byte', align=Align.INLINE)
d.comment(0x837F, 'Keep going while carry propagates', align=Align.INLINE)
d.comment(0x8381, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8382, 'Transfer to X register', align=Align.INLINE)
d.comment(0x8383, 'A=&FF: return value (transfer done)', align=Align.INLINE)
d.comment(0x8385, 'Return', align=Align.INLINE)
d.comment(0x8386, 'Load received port byte', align=Align.INLINE)
d.comment(0x8389, 'Port != 0: data transfer frame', align=Align.INLINE)
d.comment(0x838B, 'Port=0: load control byte', align=Align.INLINE)
d.comment(0x838E, 'Ctrl = &82 (POKE)?', align=Align.INLINE)
d.comment(0x8390, 'Yes: POKE also needs data transfer', align=Align.INLINE)
d.comment(0x8392, 'Other port-0 ops: immediate dispatch', align=Align.INLINE)
d.comment(0x8395, 'Update buffer pointer and check for Tube', align=Align.INLINE)
d.comment(0x8398, 'Transfer not done: skip buffer update', align=Align.INLINE)
d.comment(0x839A, 'Load buffer bytes remaining', align=Align.INLINE)
d.comment(0x839C, 'For address add', align=Align.INLINE)
d.comment(0x839D, 'Add to buffer base address', align=Align.INLINE)
d.comment(0x839F, 'No carry: skip high byte increment', align=Align.INLINE)
d.comment(0x83A1, 'Carry: increment buffer high byte', align=Align.INLINE)
d.comment(0x83A3, 'Y=8: store updated buffer position', align=Align.INLINE)
d.comment(0x83A5, 'Store updated low byte to RXCB', align=Align.INLINE)
d.comment(0x83A7, 'Y=9: buffer high byte offset', align=Align.INLINE)
d.comment(0x83A8, 'Load updated buffer high byte', align=Align.INLINE)
d.comment(0x83AA, 'Store high byte to RXCB', align=Align.INLINE)
d.comment(0x83AC, 'Check port byte again', align=Align.INLINE)
d.comment(0x83AF, 'Port=0: immediate op, discard+listen', align=Align.INLINE)
d.comment(0x83B1, 'Load source network from scout buffer', align=Align.INLINE)
d.comment(0x83B4, 'Y=3: RXCB source network offset', align=Align.INLINE)
d.comment(0x83B6, 'Store source network to RXCB', align=Align.INLINE)
d.comment(0x83B8, 'Y=2: source station offset', align=Align.INLINE)
d.comment(0x83B9, 'Load source station from scout buffer', align=Align.INLINE)
d.comment(0x83BC, 'Store source station to RXCB', align=Align.INLINE)
d.comment(0x83BE, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x83BF, 'Load port byte', align=Align.INLINE)
d.comment(0x83C2, 'Store port to RXCB', align=Align.INLINE)
d.comment(0x83C4, 'Y=0: control/flag byte offset', align=Align.INLINE)
d.comment(0x83C5, 'Load control byte from scout', align=Align.INLINE)
d.comment(0x83C8, 'Set bit7: signals wait_net_tx_ack that reply arrived', align=Align.INLINE)
d.comment(0x83CA, 'Store to RXCB byte 0 (bit 7 set = complete)', align=Align.INLINE)
d.comment(0x83CC, 'Load callback event flags', align=Align.INLINE)
d.comment(0x83CF, 'Shift bit 0 into carry', align=Align.INLINE)
d.comment(0x83D0, 'Bit 0 clear: no callback, skip to reset', align=Align.INLINE)
d.comment(0x83D2, 'Load RXCB workspace pointer low byte (carry set on entry)', align=Align.INLINE)
d.comment(0x83D4, 'Count slots', align=Align.INLINE)
d.comment(0x83D5, 'Subtract 12 bytes per RXCB slot', align=Align.INLINE)
d.comment(0x83D7, 'Loop until pointer exhausted', align=Align.INLINE)
d.comment(0x83D9, 'Adjust for off-by-one', align=Align.INLINE)
d.comment(0x83DA, 'Check slot index >= 3', align=Align.INLINE)
d.comment(0x83DC, 'Slot < 3: no callback, skip to reset', align=Align.INLINE)
d.comment(0x83DE, 'Discard scout and reset listen state', align=Align.INLINE)
d.comment(0x83E1, 'Pass slot index as callback parameter', align=Align.INLINE)
d.comment(0x83E2, 'Jump to TX completion with slot index', align=Align.INLINE)
d.comment(0x83E5, 'Discard scout and reset RX listen', align=Align.INLINE)
d.comment(0x83E8, 'Reset ADLC and return to RX listen', align=Align.INLINE)
d.comment(0x83EB, 'A=&9B: low byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x83ED, 'Y=&80: high byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x83EF, 'Install nmi_rx_scout as NMI handler', align=Align.INLINE)
d.comment(0x83F2, 'Tube flag bit 1 AND tx_flags bit 1', align=Align.INLINE)
d.comment(0x83F4, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x83F7, 'Test tx_flags for Tube transfer', align=Align.INLINE)
d.comment(0x83FA, 'No Tube transfer active -- skip release', align=Align.INLINE)
d.comment(0x83FC, 'Release Tube claim before discarding', align=Align.INLINE)
d.comment(0x83FF, 'Return', align=Align.INLINE)
d.comment(0x8400, 'Save X on stack', align=Align.INLINE)
d.comment(0x8401, 'Push X', align=Align.INLINE)
d.comment(0x8402, 'X=4: start at scout byte offset 4', align=Align.INLINE)
d.comment(0x8404, 'A=2: Tube transfer check mask', align=Align.INLINE)
d.comment(0x8406, 'Check tx_flags Tube bit', align=Align.INLINE)
d.comment(0x8409, 'Tube active: use R3 write path', align=Align.INLINE)
d.comment(0x840B, """4.21 Master 128: save/restore ACCCON across the (open_port_buf),Y stores.
The destination port buffer may live in shadow RAM; bit 0 of ACCCON (D)
controls whether (zp),Y addressing hits shadow vs main RAM. Workspace &97
holds the desired ACCCON value pre-loaded by the caller.""")
d.comment(0x840B, 'Save current ACCCON on stack (4.21 Master 128)', align=Align.INLINE)
d.comment(0x840E, 'Push ACCCON snapshot', align=Align.INLINE)
d.comment(0x840F, 'Load desired ACCCON from workspace &97', align=Align.INLINE)
d.comment(0x8411, 'Set ACCCON for the upcoming (open_port_buf),Y stores', align=Align.INLINE)
d.comment(0x8414, 'Y = current buffer position', align=Align.INLINE)
d.comment(0x8416, 'Load scout data byte', align=Align.INLINE)
d.comment(0x8419, 'Store to port buffer', align=Align.INLINE)
d.comment(0x841B, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x841C, 'No page crossing', align=Align.INLINE)
d.comment(0x841E, 'Page crossing: inc buffer high byte', align=Align.INLINE)
d.comment(0x8420, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x8422, 'No pages left: overflow', align=Align.INLINE)
d.comment(0x8424, 'Next scout data byte', align=Align.INLINE)
d.comment(0x8425, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x8427, 'Done all scout data? (X reaches &0C)', align=Align.INLINE)
d.comment(0x8429, 'No: continue copying', align=Align.INLINE)
d.comment(0x842B, 'Pull saved ACCCON from stack', align=Align.INLINE)
d.comment(0x842C, "Restore caller's ACCCON before continuing", align=Align.INLINE)
d.comment(0x842F, 'Pull saved X from stack', align=Align.INLINE)
d.comment(0x8431, 'Tail-jump to rx_complete_update_rxcb', align=Align.INLINE)
d.comment(0x8434, 'Reset ADLC if carry set', align=Align.INLINE)
d.comment(0x8436, 'Tube path: load scout data byte', align=Align.INLINE)
d.comment(0x8439, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x843C, 'Increment buffer position counters', align=Align.INLINE)
d.comment(0x843F, 'Counter overflow: handle end of buffer', align=Align.INLINE)
d.comment(0x8441, 'Next scout data byte', align=Align.INLINE)
d.comment(0x8442, 'Done all scout data?', align=Align.INLINE)
d.comment(0x8444, 'No: continue Tube writes', align=Align.INLINE)
d.comment(0x8448, 'Check if Tube needs releasing', align=Align.INLINE)
d.comment(0x844A, 'Bit7 set: already released', align=Align.INLINE)
d.comment(0x844C, 'A=&82: Tube release claim type', align=Align.INLINE)
d.comment(0x844E, 'Release Tube address claim', align=Align.INLINE)
d.comment(0x8451, 'Clear release flag (LSR clears bit7)', align=Align.INLINE)
d.comment(0x8453, 'Return', align=Align.INLINE)
d.comment(0x8454, 'Control byte &81-&88 range check', align=Align.INLINE)
d.comment(0x8457, 'Below &81: not an immediate op', align=Align.INLINE)
d.comment(0x8459, 'Out of range low: jump to discard', align=Align.INLINE)
d.comment(0x845B, 'Above &88: not an immediate op', align=Align.INLINE)
d.comment(0x845D, 'Out of range high: jump to discard', align=Align.INLINE)
d.comment(0x845F, 'HALT(&87)/CONTINUE(&88) skip protection', align=Align.INLINE)
d.comment(0x8461, 'Ctrl >= &87: dispatch without mask check', align=Align.INLINE)
d.comment(0x8463, 'Convert ctrl byte to 0-based index for mask', align=Align.INLINE)
d.comment(0x8464, 'For subtract', align=Align.INLINE)
d.comment(0x8465, 'A = ctrl - &81 (0-based operation index)', align=Align.INLINE)
d.comment(0x8467, 'Y = index for mask rotation count', align=Align.INLINE)
d.comment(0x8468, 'Load protection mask from LSTAT', align=Align.INLINE)
d.comment(0x846B, 'Rotate mask right by control byte index', align=Align.INLINE)
d.comment(0x846C, 'Decrement rotation counter', align=Align.INLINE)
d.comment(0x846D, 'Loop until bit aligned', align=Align.INLINE)
d.comment(0x846F, 'Bit set = operation disabled, discard', align=Align.INLINE)
d.comment(0x8471, 'Reload ctrl byte for dispatch table', align=Align.INLINE)
d.comment(0x8474, 'Hi byte: all handlers are in page &84', align=Align.INLINE)
d.comment(0x8476, 'Push hi byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x8477, 'Load handler low byte from jump table', align=Align.INLINE)
d.comment(0x847A, 'Push handler low byte', align=Align.INLINE)
d.comment(0x847B, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0x847C, 'Increment port buffer length', align=Align.INLINE)
d.comment(0x847E, """Tube-path overflow exit from copy_scout_to_buffer: restores the Master 128
ACCCON that was saved at &840B before re-joining the scout-done path.""")
d.comment(0x847E, 'Pull saved ACCCON from stack', align=Align.INLINE)
d.comment(0x847F, "Restore caller's ACCCON on Tube-overflow exit", align=Align.INLINE)
d.comment(0x8482, 'Check if scout data index reached 11', align=Align.INLINE)
d.comment(0x8484, 'Yes: loop back to continue reading', align=Align.INLINE)
d.comment(0x8486, 'Restore A from stack', align=Align.INLINE)
d.comment(0x8487, 'Transfer to X', align=Align.INLINE)
d.comment(0x8488, 'Jump to discard handler', align=Align.INLINE)
d.comment(0x8493, 'A=0: port buffer lo at page boundary', align=Align.INLINE)
d.comment(0x8495, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x8497, 'Buffer length lo = &82', align=Align.INLINE)
d.comment(0x8499, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x849B, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x849D, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x849F, 'Load RX page hi for buffer', align=Align.INLINE)
d.comment(0x84A1, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x84A3, 'Y=1: copy 2 bytes (1 down to 0)', align=Align.INLINE)
d.comment(0x84A5, 'Load remote address byte', align=Align.INLINE)
d.comment(0x84A8, 'Store to exec address workspace', align=Align.INLINE)
d.comment(0x84AB, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x84AC, 'Loop until all 4 bytes copied', align=Align.INLINE)
d.comment(0x84AE, 'Enter common data-receive path', align=Align.INLINE)
d.comment(0x84B1, 'Port workspace offset = &2E', align=Align.INLINE)
d.comment(0x84B3, 'Store as port_ws_offset', align=Align.INLINE)
d.comment(0x84B5, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x84B7, 'Store as rx_buf_offset', align=Align.INLINE)
d.comment(0x84B9, 'Enter POKE data-receive path', align=Align.INLINE)
d.comment(0x84BC, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x84BE, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x84C0, 'Buffer length lo = &FC', align=Align.INLINE)
d.comment(0x84C2, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x84C4, 'Buffer start lo = &EE', align=Align.INLINE)
d.comment(0x84C6, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x84C8, 'Buffer hi = &88 (response goes to &88EE area)', align=Align.INLINE)
d.comment(0x84CA, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x84CE, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x84D0, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x84D2, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x84D4, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x84D6, 'Scout status = 2 (PEEK response)', align=Align.INLINE)
d.comment(0x84D8, 'Store scout status', align=Align.INLINE)
d.comment(0x84DB, 'Calculate transfer size for response', align=Align.INLINE)
d.comment(0x84DE, 'C=0: transfer not set up, discard', align=Align.INLINE)
d.comment(0x84E0, 'Mark TX flags bit 7 (reply pending)', align=Align.INLINE)
d.comment(0x84E3, 'Set reply pending flag', align=Align.INLINE)
d.comment(0x84E5, 'Store updated TX flags', align=Align.INLINE)
d.comment(0x84E8, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x84EA, 'Write CR1: enable TX interrupts', align=Align.INLINE)
d.comment(0x84ED, 'CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE', align=Align.INLINE)
d.comment(0x84EF, 'Write CR2 for TX setup', align=Align.INLINE)
d.comment(0x84F2, 'NMI handler lo byte (self-modifying)', align=Align.INLINE)
d.comment(0x84F4, 'Y=&85: NMI handler high byte', align=Align.INLINE)
d.comment(0x84F6, 'Acknowledge and write TX dest', align=Align.INLINE)
d.comment(0x84F9, 'Get buffer position for reply header', align=Align.INLINE)
d.comment(0x84FB, 'Clear carry for offset addition', align=Align.INLINE)
d.comment(0x84FC, 'Data offset = buf_len + &80 (past header)', align=Align.INLINE)
d.comment(0x84FE, 'Y=&7F: reply data length slot', align=Align.INLINE)
d.comment(0x8500, 'Store reply data length in RX buffer', align=Align.INLINE)
d.comment(0x8502, 'Y=&80: source station slot', align=Align.INLINE)
d.comment(0x8504, 'Load requesting station number', align=Align.INLINE)
d.comment(0x8507, 'Store source station in reply header', align=Align.INLINE)
d.comment(0x850A, 'Load requesting network number', align=Align.INLINE)
d.comment(0x850D, 'Store source network in reply header', align=Align.INLINE)
d.comment(0x850F, 'Load control byte from received frame', align=Align.INLINE)
d.comment(0x8512, 'Save TX operation type for SR dispatch', align=Align.INLINE)
d.comment(0x8515, 'Op codes >= &86 (HALT/CONTINUE/machine-type) skip the SR setup', align=Align.INLINE)
d.comment(0x8517, 'Skip ahead to the ACCCON IRR set', align=Align.INLINE)
d.comment(0x8519, 'Load workspace ACR-format byte', align=Align.INLINE)
d.comment(0x851C, 'Stash a copy in ws_0d69 for later restore', align=Align.INLINE)
d.comment(0x851F, 'In shift-register mode-2 control bits', align=Align.INLINE)
d.comment(0x8521, 'Write updated workspace byte back to ws_0d68', align=Align.INLINE)
d.comment(0x8524, 'A=&80: ACCCON bit 7 (IRR -- raise interrupt)', align=Align.INLINE)
d.comment(0x8526, 'Set ACCCON IRR to flag a pending interrupt to MOS', align=Align.INLINE)
d.comment(0x8529, 'Return to idle listen mode', align=Align.INLINE)
d.comment(0x852C, 'Increment buffer length low byte', align=Align.INLINE)
d.comment(0x852E, 'No overflow: done', align=Align.INLINE)
d.comment(0x8530, 'Increment buffer length high byte', align=Align.INLINE)
d.comment(0x8532, 'No overflow: done', align=Align.INLINE)
d.comment(0x8534, 'Increment buffer pointer low byte', align=Align.INLINE)
d.comment(0x8536, 'No overflow: done', align=Align.INLINE)
d.comment(0x8538, 'Increment buffer pointer high byte', align=Align.INLINE)
d.comment(0x853A, 'Return', align=Align.INLINE)
d.comment(0x8542, 'Push hi byte on stack', align=Align.INLINE)
d.comment(0x8543, 'A=&81: low byte of tx_done_exit-1 (&8581)', align=Align.INLINE)
d.comment(0x8545, 'Push lo byte on stack', align=Align.INLINE)
d.comment(0x8546, 'Call remote JSR; RTS to tx_done_exit', align=Align.INLINE)


d.subroutine(0x853B, 'tx_done_dispatch_lo', title='TX done dispatch lo-byte table (5 entries)', description="""Low bytes of PHA/PHA/RTS dispatch targets for TX operation types
`&83`-`&87`. Read by the dispatch at
[`dispatch_svc5`](address:8048) via
`LDA tx_done_dispatch_lo-&83,Y` (the operand lands mid-instruction
inside [`set_rx_buf_len_hi`](address:84BE)). The dispatch
trampoline pushes `&85` as the high byte, so targets are
`&85xx+1`. Entries for `Y < &83` read from preceding code bytes
and are not valid operation types. Per-entry inline comments
identify each TX operation type's handler.""")
d.comment(0x8549, 'X = remote address lo from exec_addr_lo', align=Align.INLINE)
d.comment(0x854C, 'A = remote address hi from exec_addr_hi', align=Align.INLINE)
d.comment(0x854F, 'Y = 8: Econet event number', align=Align.INLINE)
d.comment(0x8554, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x8557, 'X = remote address lo', align=Align.INLINE)
d.comment(0x855A, 'Y = remote address hi', align=Align.INLINE)
d.comment(0x855D, 'Call ROM entry point at &8000', align=Align.INLINE)
d.comment(0x8560, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x8563, 'A=&04: bit 2 mask (halt flag in econet_flags)', align=Align.INLINE)
d.comment(0x8565, 'Test if already halted', align=Align.INLINE)
d.comment(0x8568, 'Already halted: skip to exit', align=Align.INLINE)
d.comment(0x856A, 'Set bit 2 in econet_flags (halt)', align=Align.INLINE)
d.comment(0x856D, 'Store halt flag', align=Align.INLINE)
d.comment(0x8570, 'A=4: re-load halt bit mask', align=Align.INLINE)
d.comment(0x8572, 'Enable interrupts during halt wait', align=Align.INLINE)
d.comment(0x8573, 'Test halt flag', align=Align.INLINE)
d.comment(0x8576, 'Still halted: keep spinning', align=Align.INLINE)
d.comment(0x857A, 'Load current econet_flags', align=Align.INLINE)
d.comment(0x857D, 'Clear bit 2: release halted station', align=Align.INLINE)
d.comment(0x857F, 'Store updated flags', align=Align.INLINE)
d.comment(0x8582, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x8583, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x8584, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8585, 'Transfer to X register', align=Align.INLINE)
d.comment(0x8586, 'A=0: success status', align=Align.INLINE)
d.comment(0x8588, 'Return with A=0 (success)', align=Align.INLINE)
d.comment(0x8589, 'Save X on stack', align=Align.INLINE)
d.comment(0x858A, 'Push X', align=Align.INLINE)
d.comment(0x858B, 'Y=2: TXCB offset for dest station', align=Align.INLINE)
d.comment(0x858D, 'Load dest station from TX control block', align=Align.INLINE)
d.comment(0x858F, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x8593, 'Load dest network from TX control block', align=Align.INLINE)
d.comment(0x8595, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x8598, 'Y=0: first byte of TX control block', align=Align.INLINE)
d.comment(0x859A, 'Load control/flag byte', align=Align.INLINE)
d.comment(0x859C, 'Bit7 set: immediate operation ctrl byte', align=Align.INLINE)
d.comment(0x859E, 'Bit7 clear: normal data transfer', align=Align.INLINE)
d.comment(0x85A1, 'Store control byte to TX scout buffer', align=Align.INLINE)
d.comment(0x85A4, 'X = control byte for range checks', align=Align.INLINE)
d.comment(0x85A5, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x85A6, 'Load port byte from TX control block', align=Align.INLINE)
d.comment(0x85A8, 'Store port byte to TX scout buffer', align=Align.INLINE)
d.comment(0x85AB, 'Port != 0: skip immediate op setup', align=Align.INLINE)
d.comment(0x85AD, 'Ctrl < &83: PEEK/POKE need address calc', align=Align.INLINE)
d.comment(0x85AF, 'Ctrl >= &83: skip to range check', align=Align.INLINE)
d.comment(0x85B1, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x85B2, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x85B3, 'Y=8: high pointer offset in TXCB', align=Align.INLINE)
d.comment(0x85B5, 'Load TXCB[Y] (end addr byte)', align=Align.INLINE)
d.comment(0x85B7, 'Y -= 4: back to start addr offset', align=Align.INLINE)
d.comment(0x85B8, '(continued)', align=Align.INLINE)
d.comment(0x85B9, '(continued)', align=Align.INLINE)
d.comment(0x85BA, '(continued)', align=Align.INLINE)
d.comment(0x85BB, 'Restore borrow from stack', align=Align.INLINE)
d.comment(0x85BC, 'end - start = transfer size byte', align=Align.INLINE)
d.comment(0x85BE, 'Store result to tx_data_start', align=Align.INLINE)
d.comment(0x85C1, 'Y += 5: advance to next end byte', align=Align.INLINE)
d.comment(0x85C2, '(continued)', align=Align.INLINE)
d.comment(0x85C3, '(continued)', align=Align.INLINE)
d.comment(0x85C4, '(continued)', align=Align.INLINE)
d.comment(0x85C5, '(continued)', align=Align.INLINE)
d.comment(0x85C6, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x85C7, 'Done all 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x85C9, 'No: next byte pair', align=Align.INLINE)
d.comment(0x85CB, 'Discard final borrow', align=Align.INLINE)
d.comment(0x85CC, 'Ctrl < &81: not an immediate op', align=Align.INLINE)
d.comment(0x85CE, 'Below range: normal data transfer', align=Align.INLINE)
d.comment(0x85D0, 'Ctrl >= &89: out of immediate range', align=Align.INLINE)
d.comment(0x85D2, 'Above range: normal data transfer', align=Align.INLINE)
d.comment(0x85D4, 'Y=&0C: start of extra data in TXCB', align=Align.INLINE)
d.comment(0x85D6, 'Load extra parameter byte from TXCB', align=Align.INLINE)
d.comment(0x85D8, 'Copy to NMI shim workspace at &0D1A+Y', align=Align.INLINE)
d.comment(0x85DB, 'Next byte', align=Align.INLINE)
d.comment(0x85DC, 'Done 4 bytes? (Y reaches &10)', align=Align.INLINE)
d.comment(0x85DE, 'No: continue copying', align=Align.INLINE)
d.comment(0x85E0, 'A=&20: mask for SR2 INACTIVE bit', align=Align.INLINE)
d.comment(0x85E2, 'Test SR2 if line is idle', align=Align.INLINE)
d.comment(0x85E5, 'Line not idle: handle as line jammed', align=Align.INLINE)
d.comment(0x85E7, 'A=&FD: high byte of timeout counter', align=Align.INLINE)
d.comment(0x85E9, 'Push timeout high byte to stack', align=Align.INLINE)
d.comment(0x85EA, 'Scout frame = 6 address+ctrl bytes', align=Align.INLINE)
d.comment(0x85EC, 'Store scout frame length', align=Align.INLINE)
d.comment(0x85EF, 'A=0: init low byte of timeout counter', align=Align.INLINE)
d.comment(0x85F1, 'Save TX index', align=Align.INLINE)
d.comment(0x85F4, 'Push timeout byte 1 on stack', align=Align.INLINE)
d.comment(0x85F5, 'Push timeout byte 2 on stack', align=Align.INLINE)
d.comment(0x85F6, 'Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x85F8, 'A=&04: INACTIVE bit mask for SR2 test', align=Align.INLINE)
d.comment(0x85FA, 'Save interrupt state', align=Align.INLINE)
d.comment(0x85FB, 'Disable interrupts for ADLC access', align=Align.INLINE)
d.comment(0x85FC, 'INTOFF -- disable NMIs', align=Align.INLINE)
d.comment(0x85FF, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x8602, 'Z = &04 AND SR2 -- tests INACTIVE', align=Align.INLINE)
d.comment(0x8605, 'INACTIVE not set -- re-enable NMIs and loop', align=Align.INLINE)
d.comment(0x8607, 'Read SR1 (acknowledge pending interrupt)', align=Align.INLINE)
d.comment(0x860A, 'CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x860C, 'Write CR2: clear status, prepare TX', align=Align.INLINE)
d.comment(0x860F, 'A=&10: CTS mask for SR1 bit4', align=Align.INLINE)
d.comment(0x8611, 'Test SR1 CTS present', align=Align.INLINE)
d.comment(0x8614, 'CTS set -- clock hardware detected, start TX', align=Align.INLINE)
d.comment(0x8616, 'INTON -- re-enable NMIs (&FE20 read)', align=Align.INLINE)
d.comment(0x8619, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x861A, '3-byte timeout counter on stack', align=Align.INLINE)
d.comment(0x861B, 'Increment timeout counter byte 1', align=Align.INLINE)
d.comment(0x861E, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x8620, 'Increment timeout counter byte 2', align=Align.INLINE)
d.comment(0x8623, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x8625, 'Increment timeout counter byte 3', align=Align.INLINE)
d.comment(0x8628, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x862C, 'Error &44: control byte out of valid range', align=Align.INLINE)
d.comment(0x8630, 'CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)', align=Align.INLINE)
d.comment(0x8632, 'Write CR2 to abort TX', align=Align.INLINE)
d.comment(0x8635, 'Clean 3 bytes of timeout loop state', align=Align.INLINE)
d.comment(0x8636, 'Pop saved register', align=Align.INLINE)
d.comment(0x8637, 'Pop saved register', align=Align.INLINE)
d.comment(0x8638, "Error &40 = 'Line Jammed'", align=Align.INLINE)
d.comment(0x863A, 'ALWAYS branch to shared error handler', align=Align.INLINE)
d.comment(0x863C, "Error &43 = 'No Clock'", align=Align.INLINE)
d.comment(0x863E, 'Offset 0 = error byte in TX control block', align=Align.INLINE)
d.comment(0x8640, 'Store error code in TX CB byte 0', align=Align.INLINE)
d.comment(0x8642, '&80 = TX complete flag', align=Align.INLINE)
d.comment(0x8644, 'Signal TX operation complete', align=Align.INLINE)
d.comment(0x8647, 'Restore X saved by caller', align=Align.INLINE)
d.comment(0x8648, 'Move to X register', align=Align.INLINE)
d.comment(0x8649, 'Return to TX caller', align=Align.INLINE)
d.comment(0x864A, 'Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x864D, 'CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)', align=Align.INLINE)
d.comment(0x864F, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x8652, 'X=&E7: low byte of nmi_tx_data (&86E7)', align=Align.INLINE)
d.comment(0x8654, 'High byte of NMI handler address', align=Align.INLINE)
d.comment(0x8656, 'Write NMI vector low byte directly', align=Align.INLINE)
d.comment(0x8659, 'Write NMI vector high byte directly', align=Align.INLINE)
d.comment(0x865C, 'SEC: prepare carry for ROR into bit 7', align=Align.INLINE)
d.comment(0x865D, 'Rotate carry into bit 7 of prot_flags (Tube-claimed)', align=Align.INLINE)
d.comment(0x865F, 'INTON -- NMIs now fire for TDRA (&FE20 read)', align=Align.INLINE)
d.comment(0x8662, 'Load destination port number', align=Align.INLINE)
d.comment(0x8665, 'Port != 0: standard data transfer', align=Align.INLINE)
d.comment(0x8667, 'Port 0: load control byte for table lookup', align=Align.INLINE)
d.comment(0x866A, 'Look up tx_flags from table', align=Align.INLINE)
d.comment(0x866D, 'Store operation flags', align=Align.INLINE)
d.comment(0x8670, 'Look up tx_length from table', align=Align.INLINE)
d.comment(0x8673, 'Store expected transfer length', align=Align.INLINE)
d.comment(0x8676, 'A=&86: high byte of tx_ctrl_* dispatch target', align=Align.INLINE)
d.comment(0x8678, 'Push high byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x8679, 'Look up handler address low from table', align=Align.INLINE)
d.comment(0x867C, 'Push low byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x867D, 'RTS dispatches to control-byte handler', align=Align.INLINE)


d.subroutine(0x867E, 'tx_ctrl_dispatch_lo', title='TX ctrl dispatch lo-byte table (8 entries)', description="""Low bytes of PHA/PHA/RTS dispatch targets for TX control byte
types `&81`-`&88`. Read by the dispatch at `&8679` via
`LDA tx_ctrl_dispatch_lo-&81,Y` (the operand lands mid-
instruction inside
[`intoff_test_inactive`](address:85FC)). High byte pushed by
the dispatcher is always `&86`, so targets are `&86xx+1`. Last
entry (`&88`) dispatches to
[`tx_ctrl_machine_type`](address:8686), the 4 bytes immediately
after the table.""")
d.comment(0x8686, 'A=3: scout_status for machine type query', align=Align.INLINE)
d.comment(0x8688, 'Skip address addition, store status', align=Align.INLINE)
d.comment(0x868A, 'A=3: scout_status for PEEK op', align=Align.INLINE)
d.comment(0x868E, 'Scout status = 2 (POKE transfer)', align=Align.INLINE)
d.comment(0x8690, 'Store scout status', align=Align.INLINE)
d.comment(0x8693, 'Clear carry for 4-byte addition', align=Align.INLINE)
d.comment(0x8694, 'Save carry on stack', align=Align.INLINE)
d.comment(0x8695, 'Y=&0C: start at offset 12', align=Align.INLINE)
d.comment(0x8697, 'Load workspace address byte', align=Align.INLINE)
d.comment(0x869A, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0x869B, 'Add TXCB address byte', align=Align.INLINE)
d.comment(0x869D, 'Store updated address byte', align=Align.INLINE)
d.comment(0x86A0, 'Next byte', align=Align.INLINE)
d.comment(0x86A1, 'Save carry for next addition', align=Align.INLINE)
d.comment(0x86A2, 'Compare Y with 16-byte boundary', align=Align.INLINE)
d.comment(0x86A4, 'Below boundary: continue addition', align=Align.INLINE)
d.comment(0x86A6, 'Restore processor flags', align=Align.INLINE)
d.comment(0x86A7, 'Skip buffer setup if transfer size is zero', align=Align.INLINE)
d.comment(0x86A9, 'Load dest station for broadcast check', align=Align.INLINE)
d.comment(0x86AC, 'AND with dest network', align=Align.INLINE)
d.comment(0x86AF, 'Both &FF = broadcast address?', align=Align.INLINE)
d.comment(0x86B1, 'Not broadcast: unicast path', align=Align.INLINE)
d.comment(0x86B3, 'Broadcast scout: 14 bytes total', align=Align.INLINE)
d.comment(0x86B5, 'Store broadcast scout length', align=Align.INLINE)
d.comment(0x86B8, 'A=&40: broadcast flag', align=Align.INLINE)
d.comment(0x86BA, 'Set broadcast flag in tx_flags', align=Align.INLINE)
d.comment(0x86BD, 'Y=4: start of address data in TXCB', align=Align.INLINE)
d.comment(0x86BF, 'Copy TXCB address bytes to scout buffer', align=Align.INLINE)
d.comment(0x86C1, 'Store to TX source/data area', align=Align.INLINE)
d.comment(0x86C4, 'Next byte', align=Align.INLINE)
d.comment(0x86C5, 'Done 8 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x86C7, 'No: continue copying', align=Align.INLINE)
d.comment(0x86CB, 'A=0: clear flags for unicast', align=Align.INLINE)
d.comment(0x86CD, 'Clear tx_flags', align=Align.INLINE)
d.comment(0x86D0, 'scout_status=2: data transfer pending', align=Align.INLINE)
d.comment(0x86D2, 'Store scout status', align=Align.INLINE)
d.comment(0x86D5, 'Copy TX block pointer to workspace ptr', align=Align.INLINE)
d.comment(0x86D7, 'Store low byte', align=Align.INLINE)
d.comment(0x86D9, 'Copy TX block pointer high byte', align=Align.INLINE)
d.comment(0x86DB, 'Store high byte', align=Align.INLINE)
d.comment(0x86DD, 'Calculate transfer size from RXCB', align=Align.INLINE)
d.comment(0x86E0, 'Restore processor status from stack', align=Align.INLINE)
d.comment(0x86E1, 'Restore stacked registers (4 PLAs)', align=Align.INLINE)
d.comment(0x86E5, 'Restore X from A', align=Align.INLINE)
d.comment(0x86E6, 'Return to caller', align=Align.INLINE)
d.comment(0x86E7, 'Load TX buffer index', align=Align.INLINE)
d.comment(0x86EA, 'SR1: V=bit6(TDRA), N=bit7(IRQ)', align=Align.INLINE)
d.comment(0x86ED, 'TDRA not set -- TX error', align=Align.INLINE)
d.comment(0x86EF, 'Load byte from TX buffer', align=Align.INLINE)
d.comment(0x86F2, 'Write to TX_DATA (continue frame)', align=Align.INLINE)
d.comment(0x86F5, 'Next TX buffer byte', align=Align.INLINE)
d.comment(0x86F6, 'Load second byte from TX buffer', align=Align.INLINE)
d.comment(0x86F9, 'Advance TX index past second byte', align=Align.INLINE)
d.comment(0x86FA, 'Save updated TX buffer index', align=Align.INLINE)
d.comment(0x86FD, 'Write second byte to TX_DATA', align=Align.INLINE)
d.comment(0x8700, 'Compare index to TX length', align=Align.INLINE)
d.comment(0x8703, 'Frame complete -- go to TX_LAST_DATA', align=Align.INLINE)
d.comment(0x8705, 'Check if we can send another pair', align=Align.INLINE)
d.comment(0x8708, 'IRQ set -- send 2 more bytes (tight loop)', align=Align.INLINE)
d.comment(0x870A, 'Wait for next NMI', align=Align.INLINE)
d.comment(0x870D, 'Error &42', align=Align.INLINE)
d.comment(0x8711, 'CR2=&67: clear status, return to listen', align=Align.INLINE)
d.comment(0x8713, 'Write CR2: clear status, idle listen', align=Align.INLINE)
d.comment(0x8716, 'Error &41 (TDRA not ready)', align=Align.INLINE)
d.comment(0x8718, 'INTOFF (also loads station ID)', align=Align.INLINE)
d.comment(0x871B, 'PHA/PLA delay loop (256 iterations for NMI disable)', align=Align.INLINE)
d.comment(0x871C, 'PHA/PLA delay (~7 cycles each)', align=Align.INLINE)
d.comment(0x871D, 'Increment delay counter', align=Align.INLINE)
d.comment(0x871E, 'Loop 256 times for NMI disable', align=Align.INLINE)
d.comment(0x8720, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x8723, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x8725, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x8728, 'Install NMI handler at &8728 (TX completion)', align=Align.INLINE)
d.comment(0x872A, 'High byte of handler address', align=Align.INLINE)
d.comment(0x872C, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x872F, 'Jump to error handler', align=Align.INLINE)
d.comment(0x8731, 'Write CR1 to switch from TX to RX', align=Align.INLINE)
d.comment(0x8734, 'Test workspace flags', align=Align.INLINE)
d.comment(0x8737, 'bit6 not set -- check bit0', align=Align.INLINE)
d.comment(0x8739, 'bit6 set -- TX completion', align=Align.INLINE)
d.comment(0x873C, 'A=1: mask for bit0 test', align=Align.INLINE)
d.comment(0x873E, 'Test tx_flags bit0 (handshake)', align=Align.INLINE)
d.comment(0x8741, 'bit0 clear: install reply handler', align=Align.INLINE)
d.comment(0x8743, 'bit0 set -- four-way handshake data phase', align=Align.INLINE)
d.comment(0x8746, 'Install nmi_reply_validate at &874B', align=Align.INLINE)
d.comment(0x8748, 'Install handler', align=Align.INLINE)
d.comment(0x874B, 'A=&01: AP mask for SR2', align=Align.INLINE)
d.comment(0x874D, 'Test SR2 AP (Address Present)', align=Align.INLINE)
d.comment(0x8750, 'No AP -- error', align=Align.INLINE)
d.comment(0x8752, 'Read first RX byte (destination station)', align=Align.INLINE)
d.comment(0x8755, 'Compare to our station ID (workspace copy)', align=Align.INLINE)
d.comment(0x8758, 'Not our station -- error/reject', align=Align.INLINE)
d.comment(0x875A, 'Install next handler at &8758 (reply continuation)', align=Align.INLINE)
d.comment(0x875C, 'Install continuation handler', align=Align.INLINE)
d.comment(0x875F, 'Read RX byte (destination station)', align=Align.INLINE)
d.comment(0x8762, 'No RDA -- error', align=Align.INLINE)
d.comment(0x8764, 'Read destination network byte', align=Align.INLINE)
d.comment(0x8767, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x8769, 'A=&76: low byte of nmi_reply_validate (&8776)', align=Align.INLINE)
d.comment(0x876B, 'Test SR1 IRQ (N=bit7) -- more data ready?', align=Align.INLINE)
d.comment(0x876E, 'IRQ set -- fall through to &8779', align=Align.INLINE)
d.comment(0x8770, 'IRQ not set -- install handler', align=Align.INLINE)
d.comment(0x8773, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x8776, 'Test SR2 RDA (bit7). Must be set for valid reply.', align=Align.INLINE)
d.comment(0x8779, 'No RDA -- error (FV masking RDA via PSE would cause this)', align=Align.INLINE)
d.comment(0x877B, 'Read source station', align=Align.INLINE)
d.comment(0x877E, 'Compare to original TX destination station (&0D20)', align=Align.INLINE)
d.comment(0x8781, 'Mismatch -- not the expected reply, error', align=Align.INLINE)
d.comment(0x8783, 'Read source network', align=Align.INLINE)
d.comment(0x8786, 'Compare to original TX destination network (&0D21)', align=Align.INLINE)
d.comment(0x8789, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x878B, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x878D, 'Test SR2 FV -- frame must be complete', align=Align.INLINE)
d.comment(0x8790, 'No FV -- incomplete frame, error', align=Align.INLINE)
d.comment(0x8792, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)', align=Align.INLINE)
d.comment(0x8794, 'Write CR2: enable RTS for TX handshake', align=Align.INLINE)
d.comment(0x8797, 'CR1=&44: RX_RESET | TIE (TX active for scout ACK)', align=Align.INLINE)
d.comment(0x8799, 'Write CR1: reset RX, enable TX interrupt', align=Align.INLINE)
d.comment(0x879C, 'Install handshake_await_ack into &0D43/&0D44 (four-way data phase)', align=Align.INLINE)
d.comment(0x879E, 'High byte &88 of next handler address', align=Align.INLINE)
d.comment(0x87A0, 'Store low byte to nmi_next_lo', align=Align.INLINE)
d.comment(0x87A3, 'Store high byte to nmi_next_hi', align=Align.INLINE)
d.comment(0x87A6, 'Load dest station for scout ACK TX', align=Align.INLINE)
d.comment(0x87A9, 'Test SR1 TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x87AC, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87AE, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x87B1, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x87B4, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x87B7, 'Install handler at &87B7 (write src addr for scout ACK)', align=Align.INLINE)
d.comment(0x87B9, 'High byte &87 of handler address', align=Align.INLINE)
d.comment(0x87BB, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x87BE, 'Load our station ID from workspace copy', align=Align.INLINE)
d.comment(0x87C1, 'Test SR1 TDRA', align=Align.INLINE)
d.comment(0x87C4, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87C6, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x87C9, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x87CB, 'Write network byte to TX FIFO', align=Align.INLINE)
d.comment(0x87CE, 'Test bit 1 of tx_flags', align=Align.INLINE)
d.comment(0x87D0, 'Check if immediate-op or data-transfer', align=Align.INLINE)
d.comment(0x87D3, 'Bit 1 set: immediate op, use alt handler', align=Align.INLINE)
d.comment(0x87D5, 'A=&EB: low byte of nmi_data_tx alt-entry (&87EB)', align=Align.INLINE)
d.comment(0x87D7, 'Y=&87: high byte of nmi_data_tx', align=Align.INLINE)
d.comment(0x87D9, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x87DC, 'Install nmi_imm_data at &8837', align=Align.INLINE)
d.comment(0x87DE, 'High byte of handler address', align=Align.INLINE)
d.comment(0x87E0, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x87E3, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x87E5, 'No pages left: send final partial page', align=Align.INLINE)
d.comment(0x87E7, 'Load remaining byte count', align=Align.INLINE)
d.comment(0x87E9, 'Zero bytes left: skip to TDRA check', align=Align.INLINE)
d.comment(0x87EB, 'Load remaining byte count (alt entry)', align=Align.INLINE)
d.comment(0x87ED, 'Zero: loop back to top of handler', align=Align.INLINE)
d.comment(0x87EF, 'Test SR1 TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x87F2, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87F4, """4.21 Master 128: save/restore ACCCON across the (open_port_buf),Y reads
in this TX FIFO loop. Same idiom as copy_scout_to_buffer / nmi_data_rx_bulk;
workspace &97 holds the desired ACCCON value pre-loaded by the caller.""")
d.comment(0x87F4, 'Save current ACCCON on stack (Master 128)', align=Align.INLINE)
d.comment(0x87F7, 'Push ACCCON snapshot', align=Align.INLINE)
d.comment(0x87F8, 'Load desired ACCCON from workspace &97', align=Align.INLINE)
d.comment(0x87FA, 'Set ACCCON for the upcoming buffer reads', align=Align.INLINE)
d.comment(0x87FD, 'Write data byte to TX FIFO', align=Align.INLINE)
d.comment(0x87FF, 'Write first byte of pair to FIFO', align=Align.INLINE)
d.comment(0x8802, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8803, 'No page crossing', align=Align.INLINE)
d.comment(0x8805, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x8807, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x8809, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x880B, 'Load second byte of pair', align=Align.INLINE)
d.comment(0x880D, 'Write second byte to FIFO', align=Align.INLINE)
d.comment(0x8810, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8811, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x8813, 'No page crossing', align=Align.INLINE)
d.comment(0x8815, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x8817, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x881F, 'Test ADLC SR1 IRQ flag for next byte pair', align=Align.INLINE)
d.comment(0x8822, 'IRQ still set: more bytes to send', align=Align.INLINE)
d.comment(0x8824, 'IRQ cleared: return from NMI', align=Align.INLINE)
d.comment(0x8819, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x881B, 'Pull saved ACCCON from stack', align=Align.INLINE)
d.comment(0x881C, "Restore caller's ACCCON between byte pairs", align=Align.INLINE)
d.comment(0x8827, 'Pull saved ACCCON (frame-end path)', align=Align.INLINE)
d.comment(0x8828, "Restore caller's ACCCON before TX_LAST_DATA", align=Align.INLINE)
d.comment(0x882B, 'CR2=&3F: TX_LAST_DATA (close data frame)', align=Align.INLINE)
d.comment(0x882D, 'Write CR2 to close frame', align=Align.INLINE)
d.comment(0x8830, 'Check tx_flags for next action', align=Align.INLINE)
d.comment(0x8833, 'Bit7 clear: error, install saved handler', align=Align.INLINE)
d.comment(0x8835, 'Install discard_reset_listen at &83F2', align=Align.INLINE)
d.comment(0x8837, 'High byte of &83F2 handler', align=Align.INLINE)
d.comment(0x8839, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x883C, 'Load saved next handler low byte', align=Align.INLINE)
d.comment(0x883F, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x8842, 'Install saved handler and return', align=Align.INLINE)
d.comment(0x8845, 'Tube TX: test SR1 TDRA', align=Align.INLINE)
d.comment(0x8848, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x884A, 'Read byte from Tube R3', align=Align.INLINE)
d.comment(0x884D, 'Write to TX FIFO', align=Align.INLINE)
d.comment(0x8850, 'Increment 4-byte buffer counter', align=Align.INLINE)
d.comment(0x8852, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x8854, 'Carry into second byte', align=Align.INLINE)
d.comment(0x8856, 'No further carry', align=Align.INLINE)
d.comment(0x8858, 'Carry into third byte', align=Align.INLINE)
d.comment(0x885A, 'No further carry', align=Align.INLINE)
d.comment(0x885C, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x885E, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x8860, 'Read second Tube byte from R3', align=Align.INLINE)
d.comment(0x8863, 'Write second byte to TX FIFO', align=Align.INLINE)
d.comment(0x8866, 'Increment 4-byte counter (second byte)', align=Align.INLINE)
d.comment(0x8868, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x886A, 'Carry into second byte', align=Align.INLINE)
d.comment(0x886C, 'No further carry', align=Align.INLINE)
d.comment(0x886E, 'Carry into third byte', align=Align.INLINE)
d.comment(0x8870, 'No further carry', align=Align.INLINE)
d.comment(0x8872, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x8874, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x8876, 'Test SR1 IRQ for tight loop', align=Align.INLINE)
d.comment(0x8879, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x887B, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x887E, 'TX error: check flags for path', align=Align.INLINE)
d.comment(0x8881, 'Bit7 clear: TX result = not listening', align=Align.INLINE)
d.comment(0x8883, 'Bit7 set: discard and return to listen', align=Align.INLINE)
d.comment(0x8886, 'CR1=&82: TX_RESET | RIE (switch to RX for final ACK)', align=Align.INLINE)
d.comment(0x8888, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x888B, 'Install nmi_final_ack handler', align=Align.INLINE)
d.comment(0x888D, 'High byte of handler address', align=Align.INLINE)
d.comment(0x888F, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x8892, 'A=&01: AP mask', align=Align.INLINE)
d.comment(0x8894, 'Test SR2 AP', align=Align.INLINE)
d.comment(0x8897, 'No AP -- error', align=Align.INLINE)
d.comment(0x8899, 'Read dest station', align=Align.INLINE)
d.comment(0x889C, 'Compare to our station (workspace copy)', align=Align.INLINE)
d.comment(0x889F, 'Not our station -- error', align=Align.INLINE)
d.comment(0x88A1, 'A=&A6: low byte of nmi_final_ack_net (&88A6)', align=Align.INLINE)
d.comment(0x88A3, 'Install continuation handler', align=Align.INLINE)
d.comment(0x88A6, 'Test SR2 RDA', align=Align.INLINE)
d.comment(0x88A9, 'No RDA -- error', align=Align.INLINE)
d.comment(0x88AB, 'Read dest network', align=Align.INLINE)
d.comment(0x88AE, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x88B0, 'Install nmi_final_ack_validate handler', align=Align.INLINE)
d.comment(0x88B2, 'Test SR1 IRQ -- more data ready?', align=Align.INLINE)
d.comment(0x88B5, 'IRQ set -- fall through to validate', align=Align.INLINE)
d.comment(0x88B7, 'Install handler', align=Align.INLINE)
d.comment(0x88BA, 'Test SR2 RDA', align=Align.INLINE)
d.comment(0x88BD, 'No RDA -- error', align=Align.INLINE)
d.comment(0x88BF, 'Read source station', align=Align.INLINE)
d.comment(0x88C2, 'Compare to TX dest station (&0D20)', align=Align.INLINE)
d.comment(0x88C5, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x88C7, 'Read source network', align=Align.INLINE)
d.comment(0x88CA, 'Compare to TX dest network (&0D21)', align=Align.INLINE)
d.comment(0x88CD, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x88CF, 'Load TX flags for next action', align=Align.INLINE)
d.comment(0x88D2, 'bit7 clear: no data phase', align=Align.INLINE)
d.comment(0x88D4, 'Install data RX handler', align=Align.INLINE)
d.comment(0x88D7, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x88D9, 'Test SR2 FV -- frame must be complete', align=Align.INLINE)
d.comment(0x88DC, 'No FV -- error', align=Align.INLINE)
d.comment(0x88DE, 'A=0: success result code', align=Align.INLINE)
d.comment(0x88E0, 'Always taken (A=0)', align=Align.INLINE)
d.comment(0x88E2, 'A=&41: not listening error code', align=Align.INLINE)
d.comment(0x88E4, 'Y=0: index into TX control block', align=Align.INLINE)
d.comment(0x88E6, 'Store result/error code at (nmi_tx_block),0', align=Align.INLINE)
d.comment(0x88E8, 'A=&80: TX-complete signal for tx_complete_flag', align=Align.INLINE)
d.comment(0x88EA, 'Signal TX complete', align=Align.INLINE)
d.comment(0x88ED, 'Full ADLC reset and return to idle listen', align=Align.INLINE)

d.label(0x88F0, 'rom_gap_88f0')

d.label(0x88F0, 'rom_gap_88f0')
d.banner(0x88F0, title='Purpose unknown. Unreferenced, unreachable.')
d.comment(0x8909, 'Read RXCB[7] (buffer addr high byte)', align=Align.INLINE)
d.comment(0x890B, 'Compare to &FF', align=Align.INLINE)
d.comment(0x890D, 'Not &FF: normal buffer, skip Tube check', align=Align.INLINE)
d.comment(0x8910, 'Read RXCB[6] (buffer addr byte 2)', align=Align.INLINE)
d.comment(0x8912, 'Check if addr byte 2 >= &FE (Tube range)', align=Align.INLINE)
d.comment(0x8924, 'Transmit in progress?', align=Align.INLINE)
d.comment(0x8927, 'No: fallback path', align=Align.INLINE)
d.comment(0x8929, 'Load TX flags for transfer setup', align=Align.INLINE)
d.comment(0x892C, 'Set bit 1 (transfer complete)', align=Align.INLINE)
d.comment(0x892E, 'Store with bit 1 set (Tube xfer)', align=Align.INLINE)
d.comment(0x8931, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x8932, 'Save carry on stack', align=Align.INLINE)
d.comment(0x8933, 'Y=4: start at RXCB offset 4', align=Align.INLINE)
d.comment(0x8935, 'Load RXCB[Y] (current ptr byte)', align=Align.INLINE)
d.comment(0x8937, 'Y += 4: advance to RXCB[Y+4]', align=Align.INLINE)
d.comment(0x8938, '(continued)', align=Align.INLINE)
d.comment(0x8939, '(continued)', align=Align.INLINE)
d.comment(0x893A, '(continued)', align=Align.INLINE)
d.comment(0x893B, 'Restore borrow from previous byte', align=Align.INLINE)
d.comment(0x893C, 'Subtract RXCB[Y+4] (start ptr byte)', align=Align.INLINE)
d.comment(0x893E, 'Store result byte', align=Align.INLINE)
d.comment(0x8941, 'Y -= 3: next source byte', align=Align.INLINE)
d.comment(0x8942, '(continued)', align=Align.INLINE)
d.comment(0x8943, '(continued)', align=Align.INLINE)
d.comment(0x8944, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x8945, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0x8947, 'No: next byte pair', align=Align.INLINE)
d.comment(0x8949, 'Discard final borrow', align=Align.INLINE)
d.comment(0x894A, 'Save X', align=Align.INLINE)
d.comment(0x894B, 'Save X', align=Align.INLINE)
d.comment(0x894C, 'Compute address of RXCB+4', align=Align.INLINE)
d.comment(0x894E, 'For base pointer addition', align=Align.INLINE)
d.comment(0x894F, 'Add RXCB base to get RXCB+4 addr', align=Align.INLINE)
d.comment(0x8951, 'X = low byte of RXCB+4', align=Align.INLINE)
d.comment(0x8952, 'Y = high byte of RXCB ptr', align=Align.INLINE)
d.comment(0x8954, 'Tube claim type &C2', align=Align.INLINE)
d.comment(0x8956, 'Claim Tube transfer address', align=Align.INLINE)
d.comment(0x8959, 'No Tube: skip reclaim', align=Align.INLINE)
d.comment(0x895B, 'Tube: reclaim with scout status', align=Align.INLINE)
d.comment(0x895E, 'Reclaim with scout status type', align=Align.INLINE)
d.comment(0x8961, 'Release Tube claim after reclaim', align=Align.INLINE)
d.comment(0x8964, 'C=1: Tube address claimed', align=Align.INLINE)
d.comment(0x8965, 'Restore X', align=Align.INLINE)
d.comment(0x8966, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8967, 'Return with C = transfer status', align=Align.INLINE)
d.comment(0x8968, 'Y=4: RXCB current pointer offset', align=Align.INLINE)
d.comment(0x896A, 'Load RXCB[4] (current ptr lo)', align=Align.INLINE)
d.comment(0x896C, 'Y=8: RXCB start address offset', align=Align.INLINE)
d.comment(0x896E, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x896F, 'Subtract RXCB[8] (start ptr lo)', align=Align.INLINE)
d.comment(0x8971, 'Store transfer size lo', align=Align.INLINE)
d.comment(0x8973, 'Y=5: current ptr hi offset', align=Align.INLINE)
d.comment(0x8975, 'Load RXCB[5] (current ptr hi)', align=Align.INLINE)
d.comment(0x8977, 'Propagate borrow only', align=Align.INLINE)
d.comment(0x8979, 'Temp store of adjusted hi byte', align=Align.INLINE)
d.comment(0x897B, 'Y=8: start address lo offset', align=Align.INLINE)
d.comment(0x897D, 'Copy RXCB[8] to open port buffer lo', align=Align.INLINE)
d.comment(0x897F, 'Store to scratch (side effect)', align=Align.INLINE)
d.comment(0x8981, 'Y=9: start address hi offset', align=Align.INLINE)
d.comment(0x8983, 'Load RXCB[9]', align=Align.INLINE)
d.comment(0x8985, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x8986, 'Subtract adjusted hi byte', align=Align.INLINE)
d.comment(0x8988, 'Store transfer size hi', align=Align.INLINE)
d.comment(0x898A, 'Return with C=1', align=Align.INLINE)
d.comment(0x898B, 'Return with C=1 (success)', align=Align.INLINE)
d.comment(0x898C, 'CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)', align=Align.INLINE)
d.comment(0x898E, 'Write CR1 to ADLC register 0', align=Align.INLINE)
d.comment(0x8991, 'CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding', align=Align.INLINE)
d.comment(0x8993, 'Write CR4 to ADLC register 3', align=Align.INLINE)
d.comment(0x8996, 'CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR', align=Align.INLINE)
d.comment(0x8998, 'Write CR3 to ADLC register 1', align=Align.INLINE)
d.comment(0x899B, 'CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)', align=Align.INLINE)
d.comment(0x899D, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x89A0, 'CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x89A2, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x89A5, 'Return; ADLC now in RX listen mode', align=Align.INLINE)
d.comment(0x89A6, 'Check if Econet has been initialised', align=Align.INLINE)
d.comment(0x89A9, 'Not initialised: skip to RX listen', align=Align.INLINE)
d.comment(0x89AB, 'Read current NMI handler low byte', align=Align.INLINE)
d.comment(0x89AE, 'Expected: &B3 (nmi_rx_scout low)', align=Align.INLINE)
d.comment(0x89B0, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x89B2, 'Read current NMI handler high byte', align=Align.INLINE)
d.comment(0x89B5, 'Test if high byte = &80 (page of nmi_rx_scout)', align=Align.INLINE)
d.comment(0x89B7, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x89B9, 'INTOFF: disable NMIs', align=Align.INLINE)
d.comment(0x89BC, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x89BF, 'TX not in progress', align=Align.INLINE)
d.comment(0x89C2, 'Econet not initialised', align=Align.INLINE)
d.comment(0x89C5, 'Y=5: service call workspace page', align=Align.INLINE)
d.comment(0x89C7, 'Set ADLC to RX listen mode', align=Align.INLINE)
d.comment(0x89CA, 'INTOFF: force /NMI high (IC97 flip-flop clear)', align=Align.INLINE)
d.comment(0x89CD, 'Save A', align=Align.INLINE)
d.comment(0x89CE, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x89CF, 'Save Y (via A)', align=Align.INLINE)
d.comment(0x89D0, 'ROM bank 0 (patched during init for actual bank)', align=Align.INLINE)
d.comment(0x89D2, 'Select Econet ROM bank via ROMSEL', align=Align.INLINE)
d.comment(0x89D5, 'Jump to scout handler in ROM', align=Align.INLINE)
d.comment(0x89D8, 'Store handler high byte at &0D0D', align=Align.INLINE)
d.comment(0x89DB, 'Store handler low byte at &0D0C', align=Align.INLINE)
d.comment(0x89DE, 'Restore NFS ROM bank', align=Align.INLINE)
d.comment(0x89E0, 'Page in via hardware latch', align=Align.INLINE)
d.comment(0x89E3, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x89E4, 'Transfer ROM bank to Y', align=Align.INLINE)
d.comment(0x89E5, 'Restore A from stack', align=Align.INLINE)
d.comment(0x89E6, 'INTON: guaranteed /NMI edge if ADLC IRQ asserted', align=Align.INLINE)
d.comment(0x89E9, 'Return from interrupt', align=Align.INLINE)
d.comment(0x8A5A, 'OSBYTE 0: read OS version', align=Align.INLINE)
d.comment(0x8A5C, 'X=1 to request version number', align=Align.INLINE)
d.comment(0x8A61, 'OS 3.2/3.5 (Master 128)?', align=Align.INLINE)
d.comment(0x8A63, 'Yes: target OS, skip Bad ROM message', align=Align.INLINE)
d.comment(0x8A65, 'OS 4.0 (Master Econet Terminal)?', align=Align.INLINE)
d.comment(0x8A67, 'Yes: target OS, skip Bad ROM message', align=Align.INLINE)
d.comment(0x8A69, 'Transfer OS version to A', align=Align.INLINE)
d.comment(0x8A6A, 'Save flags (Z set if OS 1.00) across print', align=Align.INLINE)
d.comment(0x8A6B, "Print '<CR>Bad ROM ' to mark non-Master OS", align=Align.INLINE)
d.comment(0x8A77, "Load this ROM's slot number", align=Align.INLINE)
d.comment(0x8A79, 'Print slot number as decimal', align=Align.INLINE)
d.comment(0x8A7C, 'Print trailing newline, bypassing *SPOOL', align=Align.INLINE)
d.comment(0x8A7F, 'Reload ROM slot for workspace clearing', align=Align.INLINE)
d.comment(0x8A81, 'Restore flags', align=Align.INLINE)
d.comment(0x8A82, 'OS 1.00: skip INX (table starts at slot 0)', align=Align.INLINE)
d.comment(0x8A84, 'Adjust index for OS 1.20/2.00/5.00 layout', align=Align.INLINE)
d.comment(0x8A85, 'A=0', align=Align.INLINE)
d.comment(0x8A87, 'Clear workspace byte for this ROM', align=Align.INLINE)
d.comment(0x8A54, 'Save service call number', align=Align.INLINE)
d.comment(0x8A55, 'Service call &0F (vectors claimed)?', align=Align.INLINE)
d.comment(0x8A57, 'No: skip vectors-claimed handling', align=Align.INLINE)
d.comment(0x8A8A, 'Restore ROM slot to X', align=Align.INLINE)
d.comment(0x8A8D, 'Pop service call number into A', align=Align.INLINE)
d.comment(0x8A8E, 'Re-save service call number', align=Align.INLINE)
d.comment(0x8B45, 'Service 18 carries FS number in Y; Econet is FS 5', align=Align.INLINE)
d.comment(0x8B47, 'Not us: pass the call on (RTS via shared return)', align=Align.INLINE)
d.comment(0x8B49, 'A=0 to claim the service', align=Align.INLINE)
d.comment(0x8B4B, 'Clear svc_state and fall into ensure_fs_selected', align=Align.INLINE)
d.comment(0x8ECB, "Y=&FF: 'read' parameter for OSBYTE", align=Align.INLINE)
d.comment(0x8ECD, 'Tail-call OSBYTE', align=Align.INLINE)
d.comment(0x8EC9, 'X=0 then fall through into osbyte_yff', align=Align.INLINE)
d.comment(0x939A, "Hex prefix '&'?", align=Align.INLINE)
d.comment(0x939C, 'Yes: treat as digit-like (carry set on exit)', align=Align.INLINE)
d.comment(0x939E, "Network/station separator '.'?", align=Align.INLINE)
d.comment(0x93A0, 'Yes: also digit-like; else fall through to decimal test', align=Align.INLINE)
d.comment(0x93A2, "Above '9'? (CMP #':')", align=Align.INLINE)
d.comment(0x93A4, 'Yes: not a digit -- jump to clear-carry exit', align=Align.INLINE)
d.comment(0x93A6, "Below '0'? (CMP sets carry if A >= '0')", align=Align.INLINE)
d.comment(0x93A8, "Carry now reflects '0'-'9' membership; return", align=Align.INLINE)
d.comment(0x93A9, 'Out-of-range exit: clear carry to signal not-a-digit', align=Align.INLINE)
d.comment(0x93AA, 'Return', align=Align.INLINE)
d.comment(0x93AB, 'Y=&0E: directory entry access byte offset', align=Align.INLINE)
d.comment(0x93AD, 'Read access byte through fs_options pointer', align=Align.INLINE)
d.comment(0x93AF, 'Mask to 6 protection bits (clears the unused top two)', align=Align.INLINE)
d.comment(0x93B1, 'X=4: encode-table column index for owner-access bits', align=Align.INLINE)
d.comment(0x93B3, 'Always taken: LDX #4 cleared Z, so BNE is unconditional', align=Align.INLINE)
d.comment(0x93B5, 'Mask to 5 protection bits (low 5)', align=Align.INLINE)
d.comment(0x93B7, 'X=&FF; INX inside the loop bumps to 0 for column 0', align=Align.INLINE)
d.comment(0x93B9, 'Park source bits in fs_error_ptr -- the LSR target', align=Align.INLINE)
d.comment(0x93BB, 'A=0: accumulator for encoded result', align=Align.INLINE)
d.comment(0x93BD, 'Advance table column index', align=Align.INLINE)
d.comment(0x93BE, 'Shift next source bit into carry', align=Align.INLINE)
d.comment(0x93C0, 'Source bit was 0: skip the OR for this column', align=Align.INLINE)
d.comment(0x93C2, "Source bit was 1: OR in this column's encoded mask", align=Align.INLINE)
d.comment(0x93C5, 'Continue while either fs_error_ptr or A is non-zero (loop ends when source exhausted and result still 0)', align=Align.INLINE)
d.comment(0x93C7, 'Return with encoded value in A', align=Align.INLINE)
d.comment(0x93D3, 'Save text pointer low byte (where caller wants OS to scan from)', align=Align.INLINE)
d.comment(0x93D5, 'Save text pointer high byte; fall through to set_xfer_params', align=Align.INLINE)
d.comment(0x93D7, 'Stash transfer byte count (in A)', align=Align.INLINE)
d.comment(0x93D9, 'Source pointer low byte', align=Align.INLINE)
d.comment(0x93DB, 'Source pointer high byte; fall through to set_options_ptr', align=Align.INLINE)
d.comment(0x93DD, 'Options pointer low byte (parameter block base)', align=Align.INLINE)
d.comment(0x93DF, 'Options pointer high byte; fall through to clear_escapable', align=Align.INLINE)
d.comment(0x93E1, "Save flags so the LSR doesn't disturb caller's NZC", align=Align.INLINE)
d.comment(0x93E2, 'Shift bit 0 of need_release_tube into carry, clearing the bit', align=Align.INLINE)
d.comment(0x93E4, "Restore caller's flags", align=Align.INLINE)
d.comment(0x93E5, 'Return', align=Align.INLINE)
d.comment(0x93E6, 'X=4: loop from offset 4 down to 1 (skips offset 0)', align=Align.INLINE)
d.comment(0x93E8, 'Load saved-handle byte from addr_work[X]', align=Align.INLINE)
d.comment(0x93EA, 'EOR with parsed handle byte; Z set iff bytes match', align=Align.INLINE)
d.comment(0x93EC, 'Mismatch: bail out with Z clear', align=Align.INLINE)
d.comment(0x93EE, 'Decrement to next byte', align=Align.INLINE)
d.comment(0x93EF, 'Loop while X != 0 (offset 0 is intentionally not compared)', align=Align.INLINE)
d.comment(0x93F1, 'Return; Z reflects last EOR (set = match, clear = mismatch)', align=Align.INLINE)
d.comment(0xA3E7, 'Read PB[0] (the OSWORD sub-function code in most calls); fall into byte_to_2bit_index', align=Align.INLINE)
d.comment(0xAD15, 'Load handler high byte from hi-table column X', align=Align.INLINE)
d.comment(0xAD18, 'Push for the eventual RTS dispatch', align=Align.INLINE)
d.comment(0xAD19, 'Load handler low byte from lo-table column X', align=Align.INLINE)
d.comment(0xAD1C, 'Push lo so RTS pulls (lo, hi)+1 -> handler entry', align=Align.INLINE)
d.comment(0xAD1D, 'Reload original OSWORD number into A for the handler', align=Align.INLINE)
d.comment(0xAD1F, 'RTS jumps to handler with A=OSWORD number', align=Align.INLINE)
d.comment(0xADB8, 'Compare A with table entry at index X', align=Align.INLINE)
d.comment(0xADBB, 'Match: return with Z set', align=Align.INLINE)
d.comment(0xADBD, 'Step to next earlier table entry', align=Align.INLINE)
d.comment(0xADBE, 'Loop while X >= 0 (table walked top-down)', align=Align.INLINE)
d.comment(0xADC0, 'Return; Z reflects last CMP', align=Align.INLINE)
d.comment(0xADFE, 'X=&0D: 14 template bytes to process', align=Align.INLINE)
d.comment(0xAE00, 'Y=&7C: workspace destination offset for wide variant', align=Align.INLINE)
d.comment(0xAE02, 'BIT &FF unconditionally sets V (the always_set_v_byte trick)', align=Align.INLINE)
d.comment(0xAE05, 'V=1 always: skip the narrow-mode prologue and CLV', align=Align.INLINE)
d.comment(0xAE07, 'Y=&17: workspace destination offset for narrow variant', align=Align.INLINE)
d.comment(0xAE09, 'X=&1A: 27 template bytes to process; fall into ws_copy_vclr_entry which CLVs', align=Align.INLINE)
d.comment(0xAE0B, 'Clear V: narrow mode (writes via nfs_workspace pointer)', align=Align.INLINE)
d.comment(0xAE0C, 'Read next template byte', align=Align.INLINE)
d.comment(0xAE0F, '&FE: end-of-template marker?', align=Align.INLINE)
d.comment(0xAE11, 'Yes: finalise and return', align=Align.INLINE)
d.comment(0xAE13, '&FD: skip-this-offset marker?', align=Align.INLINE)
d.comment(0xAE15, 'Yes: advance index without storing', align=Align.INLINE)
d.comment(0xAE17, '&FC: substitute-workspace-page-pointer marker?', align=Align.INLINE)
d.comment(0xAE19, 'No special marker: store this byte verbatim', align=Align.INLINE)
d.comment(0xAE1B, "Wide path: page pointer is net_rx_ptr's high byte", align=Align.INLINE)
d.comment(0xAE1D, 'V=1 (wide): keep the rx_ptr high byte', align=Align.INLINE)
d.comment(0xAE1F, 'V=0 (narrow): use nfs_workspace high byte instead', align=Align.INLINE)
d.comment(0xAE21, 'Stash whichever page byte we picked into net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xAE23, 'V=1 (wide): store via net_rx_ptr,Y', align=Align.INLINE)
d.comment(0xAE25, 'V=0 (narrow): store via nfs_workspace,Y', align=Align.INLINE)
d.comment(0xAE27, 'Always branch: V is still clear here', align=Align.INLINE)
d.comment(0xAE29, 'Wide-mode store via net_rx_ptr', align=Align.INLINE)
d.comment(0xAE2B, 'Step Y down (workspace offset)', align=Align.INLINE)
d.comment(0xAE2C, 'Step X down (template index)', align=Align.INLINE)
d.comment(0xAE2D, 'Loop while X >= 0', align=Align.INLINE)
d.comment(0xAE2F, 'Bump Y back to first written offset', align=Align.INLINE)
d.comment(0xAE30, 'Save it as net_tx_ptr low for the caller', align=Align.INLINE)
d.comment(0xAE32, 'Return', align=Align.INLINE)
d.comment(0xB21A, 'Y=10: ten characters to print (fixed-width field)', align=Align.INLINE)
d.comment(0xB21C, 'Read next character from reply buffer at offset X', align=Align.INLINE)
d.comment(0xB21F, 'Print via OSASCI, bypassing the *SPOOL file', align=Align.INLINE)
d.comment(0xB222, 'Step buffer offset', align=Align.INLINE)
d.comment(0xB223, 'Step character counter', align=Align.INLINE)
d.comment(0xB224, 'Loop until Y=0', align=Align.INLINE)
d.comment(0xB226, 'Return; X points just past the last printed byte', align=Align.INLINE)
d.comment(0xB22A, 'Y=0: scan from start of command line', align=Align.INLINE)
d.comment(0xB251, "Save caller's X (TX buffer offset)", align=Align.INLINE)
d.comment(0xB252, 'Push it', align=Align.INLINE)
d.comment(0xB253, 'X=&FF: INX in loop bumps to 0 for first byte', align=Align.INLINE)
d.comment(0xB255, 'Step to next byte position', align=Align.INLINE)
d.comment(0xB256, 'Read byte X+1 (the next character)', align=Align.INLINE)
d.comment(0xB259, 'Store it back at byte X (shifting left by one)', align=Align.INLINE)
d.comment(0xB25C, 'EOR with CR; Z set if we just shifted the terminator', align=Align.INLINE)
d.comment(0xB25E, 'More to shift: continue', align=Align.INLINE)
d.comment(0xB260, 'X is now the buffer length (excluding CR)', align=Align.INLINE)
d.comment(0xB261, 'Empty after shift: skip trim, restore X, return', align=Align.INLINE)
d.comment(0xB263, 'Read last buffer byte (X-1 because we count from 0)', align=Align.INLINE)
d.comment(0xB266, "EOR with space; Z set iff it's a trailing space", align=Align.INLINE)
d.comment(0xB268, 'Not a space: trim done, restore X, return', align=Align.INLINE)
d.comment(0xB26A, 'It is a space: replace with CR (truncate the string)', align=Align.INLINE)
d.comment(0xB26C, 'Store CR at the now-trimmed position', align=Align.INLINE)
d.comment(0xB26F, 'Step backwards', align=Align.INLINE)
d.comment(0xB270, 'Loop while X > 0', align=Align.INLINE)
d.comment(0xB272, "Restore caller's TX buffer offset", align=Align.INLINE)
d.comment(0xB273, 'Transfer back to X', align=Align.INLINE)
d.comment(0xB274, 'Return', align=Align.INLINE)
d.comment(0xB29F, 'X=0: place the argument at the start of the TX buffer; fall into copy_arg_to_buf', align=Align.INLINE)
d.comment(0x8CAF, 'Load workspace page byte for this ROM slot', align=Align.INLINE)
d.comment(0x8CAD, 'Y = current ROM slot number from MOS copy at &F4', align=Align.INLINE)
d.comment(0x8CB2, 'Hold a copy of the slot byte in Y while we test bit 6', align=Align.INLINE)
d.comment(0x8CB3, 'ROL puts pre-ROL bit 6 into the post-ROL N flag (and pre-ROL bit 7 into C)', align=Align.INLINE)
d.comment(0x8CB4, "Save those flags so the upcoming ROR doesn't lose N", align=Align.INLINE)
d.comment(0x8CB5, 'ROR restores A to its original value (using the saved C)', align=Align.INLINE)
d.comment(0x8CB6, 'Restore the ROL flags: N is now pre-ROL bit 6', align=Align.INLINE)
d.comment(0x8CB7, 'Bit 6 clear: skip the OR (no ADLC-absent flag)', align=Align.INLINE)
d.comment(0x8CB9, 'Bit 6 set: re-set bit 7 in the returned page byte (the ADLC-absent flag uses bit 7 in callers)', align=Align.INLINE)
d.comment(0xB2CF, 'Read fs_lib_flags (now at &C271 in 4.21)', align=Align.INLINE)
d.comment(0xB2D2, 'Keep only the 5-bit owner access mask', align=Align.INLINE)
d.comment(0xB2D4, 'Store back, clearing FS-selection and other high bits', align=Align.INLINE)
d.comment(0xB2D7, 'Return', align=Align.INLINE)
d.comment(0xB7CB, "Print 'Y/N) ' via the inline-string helper", align=Align.INLINE)
d.comment(0xB7CE, 'Inline string body — bytes consumed by print_inline_no_spool (above)', align=Align.INLINE)
d.comment(0xBF71, 'Y = saved file handle from ws_page', align=Align.INLINE)
d.comment(0xBF73, 'A=0: OSFIND close', align=Align.INLINE)
d.comment(0xBF75, 'Tail-call OSFIND to close the handle', align=Align.INLINE)
d.comment(0xBFBA, 'First INX-by-4 via JSR; falls into advance_x_by_4 for the second four', align=Align.INLINE)
d.comment(0xBFBD, 'JSR inx4 (4 INX); RTS returns here, then falls into inx4 again for the implicit second four', align=Align.INLINE)
d.comment(0xBFC1, '(continued)', align=Align.INLINE)
d.comment(0xBFC2, '(continued)', align=Align.INLINE)
d.comment(0xBFC3, '(continued)', align=Align.INLINE)
d.comment(0xBFC4, "Return; caller is either an explicit JSR (so X has advanced by 4) or advance_x_by_8's fall-through (so X has advanced by 8 total)", align=Align.INLINE)
d.comment(0xB2A1, "Y=0: scan from start of command line (CLC entry skips '&' validation)", align=Align.INLINE)
d.comment(0xB2A3, "Set C: this entry validates against '&'", align=Align.INLINE)
d.comment(0xB2A4, 'Read next source byte through fs_crc_lo pointer', align=Align.INLINE)
d.comment(0xB2A6, 'Store into TX buffer at offset X', align=Align.INLINE)
d.comment(0xB2A9, 'Validation off (C clear): just advance positions', align=Align.INLINE)
d.comment(0xB2AB, "Test against '!' to bias the EOR comparison", align=Align.INLINE)
d.comment(0xB2AD, "EOR with '&'; Z set iff source byte was '&'", align=Align.INLINE)
d.comment(0xB2AF, "'&' inside the argument is illegal: raise 'Bad filename'", align=Align.INLINE)
d.comment(0xB2B1, 'Restore A by undoing the EOR (so the loop terminator test below sees the original byte)', align=Align.INLINE)
d.comment(0xB2B3, 'Advance TX buffer offset', align=Align.INLINE)
d.comment(0xB2B4, 'Advance command-line offset', align=Align.INLINE)
d.comment(0xB2B5, 'EOR with CR; Z set iff we just stored the terminator', align=Align.INLINE)
d.comment(0xB2B7, 'More to copy: continue', align=Align.INLINE)
d.comment(0xB2B9, 'Look at the byte just before the CR we stopped on', align=Align.INLINE)
d.comment(0xB2BC, 'EOR with space; Z set iff that byte was a trailing space', align=Align.INLINE)
d.comment(0xB2BE, 'Not a space: trim done', align=Align.INLINE)
d.comment(0xB2C0, 'Step back over the space', align=Align.INLINE)
d.comment(0xB2C1, 'A=&0D: replace the trailing space with CR', align=Align.INLINE)
d.comment(0xB2C3, 'Store CR at the now-truncated end', align=Align.INLINE)
d.comment(0xB2C6, 'Always taken (A=&0D from LDA #&0D so Z is clear); look at the next byte back', align=Align.INLINE)
d.comment(0xB2C8, 'All trailing spaces consumed (or none present)', align=Align.INLINE)
d.comment(0xB2CA, 'Return', align=Align.INLINE)
d.comment(0xB3D5, 'Y=&18: standard offset for the PS template; fall into copy_ps_data', align=Align.INLINE)
d.comment(0xB4A8, 'Y=2: workspace offset of PS station byte', align=Align.INLINE)
d.comment(0xB4AA, 'Read station byte', align=Align.INLINE)
d.comment(0xB4AC, 'Stash in fs_work_5 (PS station)', align=Align.INLINE)
d.comment(0xB4AE, 'Y=3: workspace offset of PS network byte', align=Align.INLINE)
d.comment(0xB4AF, 'Read network byte', align=Align.INLINE)
d.comment(0xB4B1, 'Stash in fs_work_6 (PS network)', align=Align.INLINE)
d.comment(0xB51C, 'Step Y to next workspace slot byte', align=Align.INLINE)
d.comment(0xB51D, 'Load buffer page byte from addr_work', align=Align.INLINE)
d.comment(0xB51F, 'Write at offset Y', align=Align.INLINE)
d.comment(0xB521, 'A=&FF: sentinel; fall into write_two_bytes_inc_y to store two of them', align=Align.INLINE)
d.comment(0xB523, 'Step Y to next destination', align=Align.INLINE)
d.comment(0xB524, 'Write A at workspace offset Y', align=Align.INLINE)
d.comment(0xB526, 'Step Y again', align=Align.INLINE)
d.comment(0xB527, 'Write A at the next offset (two consecutive copies)', align=Align.INLINE)
d.comment(0xB529, 'Final INY leaves Y pointing past the second write', align=Align.INLINE)
d.comment(0xB52B, 'Y=&18: source offset (start of PS name in RX buffer)', align=Align.INLINE)
d.comment(0xB52D, 'Read RX byte at offset Y', align=Align.INLINE)
d.comment(0xB52F, 'Push it (the stack reverses the order)', align=Align.INLINE)
d.comment(0xB530, 'Step source', align=Align.INLINE)
d.comment(0xB531, 'Reached &20 (one past the 8-byte name)?', align=Align.INLINE)
d.comment(0xB533, 'No: continue pushing', align=Align.INLINE)
d.comment(0xB535, 'Y=&17: destination offset for the reversed name', align=Align.INLINE)
d.comment(0xB537, 'Pull next pushed byte (LIFO -> reversed order)', align=Align.INLINE)
d.comment(0xB538, 'Store at destination offset Y', align=Align.INLINE)
d.comment(0xB53A, 'Step destination back', align=Align.INLINE)
d.comment(0xB53B, 'Reached &0F (one before the destination range)?', align=Align.INLINE)
d.comment(0xB53D, 'No: continue popping', align=Align.INLINE)
d.comment(0xB53F, 'Copy net_rx_ptr_hi as the TX page (TX shares the same page as RX for this packet)', align=Align.INLINE)
d.comment(0xB541, 'Set net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xB543, 'TX low byte = &0C: skip past the TX header to where the reversed name lives', align=Align.INLINE)
d.comment(0xB545, 'Set net_tx_ptr lo', align=Align.INLINE)
d.comment(0xB547, 'Y=3: copy 4-byte TX header (offsets 3..0)', align=Align.INLINE)
d.comment(0xB549, 'Read template byte', align=Align.INLINE)
d.comment(0xB54C, 'Write to TX buffer at offset Y', align=Align.INLINE)
d.comment(0xB54E, 'Step backwards', align=Align.INLINE)
d.comment(0xB54F, 'Loop while Y >= 0', align=Align.INLINE)
d.comment(0xB551, 'Return', align=Align.INLINE)
d.comment(0x978A, 'Clear V: standard send mode (callers set V via save_net_tx_cb_vset for the lib-flag variant)', align=Align.INLINE)
d.comment(0x978B, 'Read FS station from &C002 (saved from selection time)', align=Align.INLINE)
d.comment(0x978E, 'Copy into TX buffer at &C102 (dest station for header)', align=Align.INLINE)
d.comment(0x9791, 'Clear C: caller wants four-way handshake (not disconnect)', align=Align.INLINE)
d.comment(0x9792, 'Save flags so we can keep V across the loop', align=Align.INLINE)
d.comment(0x9793, 'Save Y -- the entry function code -- into TX[1]', align=Align.INLINE)
d.comment(0x9796, 'Y=1: copy 2 bytes (network/control) starting at index 1', align=Align.INLINE)
d.comment(0x9798, 'Read source byte at &C003+Y', align=Align.INLINE)
d.comment(0x979B, 'Write to TX buffer at &C103+Y', align=Align.INLINE)
d.comment(0x979E, 'Step backwards', align=Align.INLINE)
d.comment(0x979F, 'Loop while Y >= 0 (covers indices 1, 0)', align=Align.INLINE)
d.comment(0x97A1, 'Test fs_lib_flags: bit 6 = use library, bit 7 = *-prefix-stripped', align=Align.INLINE)
d.comment(0x97A4, 'V (bit 6) set: use the library station instead', align=Align.INLINE)
d.comment(0x97A6, 'Neither bit set: leave the FS station copy intact', align=Align.INLINE)
d.comment(0x97A8, 'Bit 7 (FS-prefix) set: substitute the saved-prefix station from &C004', align=Align.INLINE)
d.comment(0x97AB, "Override TX[3]'s station byte", align=Align.INLINE)
d.comment(0x97AE, "Always taken: V was clear when we entered (BVS at &97A4 didn't fire)", align=Align.INLINE)
d.comment(0x97B0, 'use_lib_station: substitute the library station from &C002 (the original FS station, but bit 6 of fs_lib_flags redirects via lib path)', align=Align.INLINE)
d.comment(0x97B3, 'Override TX[3] with the library station byte', align=Align.INLINE)
d.comment(0x97B6, 'Restore the saved flags (V/C control downstream init_txcb behaviour)', align=Align.INLINE)
d.comment(0x98BE, 'Read the configurable rx-wait timeout (&0D6E, default &28 = ~22s on 2 MHz)', align=Align.INLINE)
d.comment(0x98C1, 'Push it as the outermost counter (read back via stack-X indexing later)', align=Align.INLINE)
d.comment(0x98C2, 'Read econet_flags so we can preserve it across the wait', align=Align.INLINE)
d.comment(0x98C5, "Push it (we'll temporarily set bit 7 to mark waiting)", align=Align.INLINE)
d.comment(0x98C6, 'Check whether net_tx_ptr_hi is non-zero (TX in flight?)', align=Align.INLINE)
d.comment(0x98C8, 'Yes: skip the flag-set; counters initialise either way', align=Align.INLINE)
d.comment(0x98CA, 'TX idle: set bit 7 of econet_flags (signal RX-only wait)', align=Align.INLINE)
d.comment(0x98CC, 'Write the modified flags back', align=Align.INLINE)
d.comment(0x98CF, 'A=0: initial value for inner+middle counters', align=Align.INLINE)
d.comment(0x98D1, 'Push it -- middle counter at stack[X+2]', align=Align.INLINE)
d.comment(0x98D2, 'Push it again -- inner counter at stack[X+1]', align=Align.INLINE)
d.comment(0x98D3, 'Y=0: indirect index for net_tx_ptr poll', align=Align.INLINE)
d.comment(0x98D4, 'Capture S into X so we can address the stack counters', align=Align.INLINE)
d.comment(0x98D5, 'Read RX/TX flags through net_tx_ptr -- bit 7 set means complete', align=Align.INLINE)
d.comment(0x98D7, 'Bit 7 set: reply received, exit poll', align=Align.INLINE)
d.comment(0x98D9, 'Decrement inner counter at stack[X+1]', align=Align.INLINE)
d.comment(0x98DC, 'Inner not zero yet: poll again', align=Align.INLINE)
d.comment(0x98DE, 'Inner wrapped: decrement middle at stack[X+2]', align=Align.INLINE)
d.comment(0x98E1, 'Middle not zero: poll again', align=Align.INLINE)
d.comment(0x98E3, 'Middle wrapped: decrement outer at stack[X+4] (the saved timeout value)', align=Align.INLINE)
d.comment(0x98E6, 'Outer not zero: poll again', align=Align.INLINE)
d.comment(0x98E8, 'Reload the original timeout to test for timeout=0 mode', align=Align.INLINE)
d.comment(0x98EB, 'Configured timeout was non-zero: declare timeout', align=Align.INLINE)
d.comment(0x98ED, 'Timeout=0 (poll forever): check escape flag', align=Align.INLINE)
d.comment(0x98EF, 'Escape pressed: jump to escape handler at &9895', align=Align.INLINE)
d.comment(0x98F1, 'Reset outer counter so we keep polling', align=Align.INLINE)
d.comment(0x98F4, "Always taken (INC's result is always non-zero here): back to inner", align=Align.INLINE)
d.comment(0x98F6, 'done_poll_tx: discard inner counter', align=Align.INLINE)
d.comment(0x98F7, 'Discard middle counter', align=Align.INLINE)
d.comment(0x98F8, 'Pull saved econet_flags', align=Align.INLINE)
d.comment(0x98F9, 'Restore them (clearing bit 7 if we set it)', align=Align.INLINE)
d.comment(0x98FC, 'Pull saved rx_wait_timeout into A', align=Align.INLINE)
d.comment(0x98FD, "If timeout reached zero, raise 'No reply'", align=Align.INLINE)
d.comment(0x98FF, 'Reply received normally: return', align=Align.INLINE)
d.comment(0x93F7, 'Save flags so the rest of the routine is transparent', align=Align.INLINE)
d.comment(0x93F8, 'Save A (the attribute byte we need to recover via stack)', align=Align.INLINE)
d.comment(0x93F9, 'Save X', align=Align.INLINE)
d.comment(0x93FA, 'Capture S into X to address stack from below', align=Align.INLINE)
d.comment(0x93FB, 'Re-read the original A from stack[X+2] (above PHX/PHA)', align=Align.INLINE)
d.comment(0x93FE, 'Convert attribute byte to channel-table index', align=Align.INLINE)
d.comment(0x9401, 'No matching channel: skip the flag set, just restore', align=Align.INLINE)
d.comment(0x9403, 'A=&40: bit 6 = connection-active mask', align=Align.INLINE)
d.comment(0x9405, 'OR with current status byte for this channel', align=Align.INLINE)
d.comment(0x9408, 'Write back the updated status', align=Align.INLINE)
d.comment(0x940B, 'Always taken (A is non-zero after the OR with &40); join shared exit', align=Align.INLINE)
d.comment(0x940D, 'Save flags', align=Align.INLINE)
d.comment(0x940E, 'Save A', align=Align.INLINE)
d.comment(0x940F, 'Save X', align=Align.INLINE)
d.comment(0x9410, 'Capture S into X for stack-relative reads', align=Align.INLINE)
d.comment(0x9411, 'Re-read the attribute byte from stack[X+2]', align=Align.INLINE)
d.comment(0x9414, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9417, 'No matching channel: just restore', align=Align.INLINE)
d.comment(0x9419, 'A=&BF: bit 6 clear mask', align=Align.INLINE)
d.comment(0x941E, 'Write back the updated status', align=Align.INLINE)
d.comment(0x9421, 'Restore X (saved at PHX)', align=Align.INLINE)
d.comment(0x9422, 'Restore A', align=Align.INLINE)
d.comment(0x9423, 'Restore flags', align=Align.INLINE)
d.comment(0x9424, 'Return; A and X preserved across the call', align=Align.INLINE)
d.comment(0x97B7, 'Save flags so C survives the init_txcb call', align=Align.INLINE)
d.comment(0x97B8, 'Reply port = &90 (FS reply port)', align=Align.INLINE)
d.comment(0x97BA, 'Stash port in TXCB[0]', align=Align.INLINE)
d.comment(0x97BD, 'Build the rest of the TXCB (control, dest stn/net, etc.)', align=Align.INLINE)
d.comment(0x97C0, 'Move TX-buffer end pointer (returned in X) into A', align=Align.INLINE)
d.comment(0x97C1, 'Add 5 bytes of slack for trailing reply data', align=Align.INLINE)
d.comment(0x97C3, 'Stash the resulting end-of-buffer offset', align=Align.INLINE)
d.comment(0x97C5, 'Restore the original C flag from caller', align=Align.INLINE)
d.comment(0x97C6, 'C set: this is a disconnect; jump to handle_disconnect', align=Align.INLINE)
d.comment(0x97C8, 'Save flags again across the actual TX (TX clobbers them)', align=Align.INLINE)
d.comment(0x97C9, 'Send the four-way-handshake-initiated command packet', align=Align.INLINE)
d.comment(0x97CC, "Restore caller's flags before falling into recv_and_process_reply", align=Align.INLINE)
d.comment(0xB22F, 'Read first parsed-buffer character (the candidate prefix)', align=Align.INLINE)
d.comment(0xB232, "EOR with '&'; Z set iff the byte was '&'", align=Align.INLINE)
d.comment(0xB234, "Not '&': try ':' (and '#') instead", align=Align.INLINE)
d.comment(0xB236, 'Read fs_lib_flags', align=Align.INLINE)
d.comment(0xB239, 'Set bit 6 (URD-relative resolution flag)', align=Align.INLINE)
d.comment(0xB23B, 'Write back updated flags', align=Align.INLINE)
d.comment(0xB23E, "Strip the '&' from the buffer (shift left + trim)", align=Align.INLINE)
d.comment(0xB241, "Step caller's X back to account for the consumed character", align=Align.INLINE)
d.comment(0xB242, 'Re-read the (now first) buffer byte after the strip', align=Align.INLINE)
d.comment(0xB245, "EOR with '.'; Z set iff '&.' pair (URD root)", align=Align.INLINE)
d.comment(0xB247, "Not '&.': just '&' alone -- check for trailing '#'", align=Align.INLINE)
d.comment(0xB249, "It was '&.': peek the byte after the dot", align=Align.INLINE)
d.comment(0xB24C, "EOR with CR; Z set iff '&.<CR>' (illegal: dot needs a name to follow)", align=Align.INLINE)
d.comment(0xB24E, "'&.<CR>' is invalid: raise 'Bad filename'", align=Align.INLINE)
d.comment(0xB250, "Valid '&.<name>': step X back for the dot too", align=Align.INLINE)
d.comment(0xB483, "Print 'File' via inline string", align=Align.INLINE)
d.comment(0xB48A, 'Clear V so the BVC below is taken', align=Align.INLINE)
d.comment(0xB48B, "Always taken (V was just cleared); skip the 'Printer' prologue and reach the shared ' server is ' suffix", align=Align.INLINE)
d.comment(0xB48D, "Print 'Printer' via inline string", align=Align.INLINE)
d.comment(0xB497, 'NOP -- bit-7 terminator + harmless resume opcode', align=Align.INLINE)
d.comment(0xB498, "Print ' server is ' via inline string", align=Align.INLINE)
d.comment(0xB4A6, 'NOP -- bit-7 terminator + harmless resume opcode', align=Align.INLINE)
d.comment(0xB4A7, 'Return; caller now prints the actual server (file or printer) address', align=Align.INLINE)
d.comment(0xBE37, 'Save A so the caller can re-use the value', align=Align.INLINE)
d.comment(0xBE38, 'Print A as two hex digits', align=Align.INLINE)
d.comment(0xBE3B, "A=' ': trailing column separator", align=Align.INLINE)
d.comment(0xBE3D, 'Print the space via OSASCI', align=Align.INLINE)
d.comment(0xBE40, "Restore caller's A", align=Align.INLINE)
d.comment(0xBE41, 'Return', align=Align.INLINE)
d.comment(0xA3BB, "Set V so print_station_addr suppresses the leading '0.' when the network number is zero", align=Align.INLINE)
d.comment(0xA3BE, 'Print the station/network address', align=Align.INLINE)
d.comment(0xA3C1, 'Tail-call OSNEWL for the trailing CR/LF', align=Align.INLINE)
d.comment(0xB22C, 'Read the GSREAD-style filename argument into the &C030 buffer, then fall into parse_access_prefix', align=Align.INLINE)
d.comment(0xB556, "Save caller's V (controls leading-zero padding via the BVS at &B566)", align=Align.INLINE)
d.comment(0xB557, 'Read network number (fs_work_6)', align=Align.INLINE)
d.comment(0xB559, "Network 0 means local: skip the 'NN.' prefix", align=Align.INLINE)
d.comment(0xB55B, 'Network non-zero: print as 3-digit decimal', align=Align.INLINE)
d.comment(0xB55E, "A='.': separator between network and station", align=Align.INLINE)
d.comment(0xB560, 'Print the dot', align=Align.INLINE)
d.comment(0xB563, 'Set V so the next BVS branches over the padding (we just printed digits, no padding needed)', align=Align.INLINE)
d.comment(0xB566, 'V set: skip leading-space padding', align=Align.INLINE)
d.comment(0xB568, 'V clear (caller wanted padding): print 4 leading spaces via inline string', align=Align.INLINE)
d.comment(0xB56F, 'Read station number (fs_work_5)', align=Align.INLINE)
d.comment(0xB571, "Restore caller's V (so print_decimal_3dig honours its own leading-zero suppression)", align=Align.INLINE)
d.comment(0xB572, 'Tail-call print_decimal_3dig for the station number', align=Align.INLINE)
d.comment(0x8CA9, 'NOP -- bit-7 terminator + harmless resume opcode', align=Align.INLINE)
d.comment(0x8CAA, "Tail-call print_station_id to append ' Econet Station <n>' (and ' No Clock' if appropriate)", align=Align.INLINE)
d.comment(0xB2E4, 'Read fs_spool_handle (also column counter in *Cat mode)', align=Align.INLINE)
d.comment(0xB2E6, 'Negative: *Ex mode (one-per-line) -- skip column logic, just print newline', align=Align.INLINE)
d.comment(0xB2E8, 'Bump column counter', align=Align.INLINE)
d.comment(0xB2E9, 'Get the new value into A', align=Align.INLINE)
d.comment(0xB2EA, 'Wrap to 0..3 (4 columns per row)', align=Align.INLINE)
d.comment(0xB2EC, 'Save the new column index', align=Align.INLINE)
d.comment(0xB2EE, 'Wrapped to 0: end of row, print newline', align=Align.INLINE)
d.comment(0xB2F0, 'Mid-row: print 2-space column separator via inline', align=Align.INLINE)
d.comment(0xB303, 'Y = value to convert (digits read off via successive divisions)', align=Align.INLINE)
d.comment(0xB304, 'Divisor for hundreds digit', align=Align.INLINE)
d.comment(0xB306, 'Print hundreds digit', align=Align.INLINE)
d.comment(0xB309, 'Divisor for tens digit', align=Align.INLINE)
d.comment(0xB30B, 'Print tens digit', align=Align.INLINE)
d.comment(0xB30E, 'Divisor for units digit (always print at least the units to avoid the empty 0 case)', align=Align.INLINE)
d.comment(0xB310, 'Stash divisor in fs_error_ptr (the SBC target below)', align=Align.INLINE)
d.comment(0xB313, "X = '0'-1: digit counter, INX in the loop steps to '0' first", align=Align.INLINE)
d.comment(0xB315, 'Set carry', align=Align.INLINE)
d.comment(0xB316, 'Step quotient digit', align=Align.INLINE)
d.comment(0xB317, 'Subtract divisor', align=Align.INLINE)
d.comment(0xB319, 'No underflow: keep dividing', align=Align.INLINE)
d.comment(0xB31B, 'Underflow: add divisor back to recover the remainder', align=Align.INLINE)
d.comment(0xB31D, 'Remainder -> Y, ready for the next digit', align=Align.INLINE)
d.comment(0xB31E, "Move digit ('0'-'9') from X into A for printing", align=Align.INLINE)
d.comment(0xB31F, 'Save divisor in X across the print (print_char_no_spool preserves X is not guaranteed)', align=Align.INLINE)
d.comment(0xB321, 'Print the digit, bypassing *SPOOL', align=Align.INLINE)
d.comment(0xB324, 'Restore divisor from X', align=Align.INLINE)
d.comment(0xB326, 'Return', align=Align.INLINE)
d.comment(0xBF78, "Save flags so caller's NZC survive", align=Align.INLINE)
d.comment(0xBF79, 'Move command-line offset Y into A for the add', align=Align.INLINE)
d.comment(0xBF7A, 'Clear C for the 16-bit add', align=Align.INLINE)
d.comment(0xBF7B, 'A = os_text_ptr_lo + Y (filename address low byte)', align=Align.INLINE)
d.comment(0xBF7D, 'Push it (we need to restore os_text_ptr after OSFIND)', align=Align.INLINE)
d.comment(0xBF7E, 'Move filename low into X (OSFIND wants the address in X/Y)', align=Align.INLINE)
d.comment(0xBF7F, 'A=0: zero high byte before the carry-add', align=Align.INLINE)
d.comment(0xBF81, 'Add os_text_ptr_hi with carry from the low add', align=Align.INLINE)
d.comment(0xBF83, 'Push filename high byte for the restore', align=Align.INLINE)
d.comment(0xBF84, 'Move filename high into Y', align=Align.INLINE)
d.comment(0xBF85, 'A=&40: OSFIND open-for-input mode', align=Align.INLINE)
d.comment(0xBF87, 'Open the file; returns handle in A (zero on failure)', align=Align.INLINE)
d.comment(0xBF8A, 'Copy returned handle into Y (also sets Z if zero)', align=Align.INLINE)
d.comment(0xBF8B, 'Stash the handle in ws_page for later close', align=Align.INLINE)
d.comment(0xBF8D, 'Non-zero: open succeeded, skip error path', align=Align.INLINE)
d.comment(0xBF8F, "A=&D6: 'Not found' error code", align=Align.INLINE)
d.comment(0xBF91, 'Raise the error with the inline string below; never returns', align=Align.INLINE)
d.comment(0xBF9E, 'Restore the saved filename high byte into os_text_ptr_hi -- but wait, this writes the FILENAME address into os_text_ptr; the caller intentionally moves os_text_ptr to scan past the filename below', align=Align.INLINE)
d.comment(0xBFA1, 'Restore filename low byte into os_text_ptr_lo (so (os_text_ptr) now points at the filename)', align=Align.INLINE)
d.comment(0xBFA4, 'Y=0: scan from start of filename', align=Align.INLINE)
d.comment(0xBFA6, 'Step to next byte', align=Align.INLINE)
d.comment(0xBFA7, 'Read filename byte', align=Align.INLINE)
d.comment(0xBFA9, 'Hit CR? End of command line', align=Align.INLINE)
d.comment(0xBFAB, 'Yes: filename ended at CR (no trailing spaces)', align=Align.INLINE)
d.comment(0xBFAD, 'Hit space? End of filename', align=Align.INLINE)
d.comment(0xBFAF, 'No (still inside filename): keep scanning', align=Align.INLINE)
d.comment(0xBFB1, 'Step past spaces', align=Align.INLINE)
d.comment(0xBFB2, 'Read next byte', align=Align.INLINE)
d.comment(0xBFB4, 'Still a space?', align=Align.INLINE)
d.comment(0xBFB6, 'Yes: keep skipping', align=Align.INLINE)
d.comment(0xBFB8, 'Done: Y points just past the filename and any spaces', align=Align.INLINE)
d.comment(0xBFB9, "Restore caller's flags", align=Align.INLINE)
d.comment(0xAD40, 'Y=&D9: workspace offset for the abort code byte', align=Align.INLINE)
d.comment(0xAD42, 'Store the abort code (passed in A) at workspace[&D9]', align=Align.INLINE)
d.comment(0xAD44, 'A=&80: control = immediate-operation flag', align=Align.INLINE)
d.comment(0xAD46, 'Y=&0C: TXCB control-byte offset', align=Align.INLINE)
d.comment(0xAD48, 'Set TXCB[&0C] = &80 (immediate / abort)', align=Align.INLINE)
d.comment(0xAD4A, "Save current net_tx_ptr low (we'll repoint TX at the abort packet)", align=Align.INLINE)
d.comment(0xAD4C, 'Push it for restore on exit', align=Align.INLINE)
d.comment(0xAD4D, 'Save net_tx_ptr high too', align=Align.INLINE)
d.comment(0xAD4F, 'Push it', align=Align.INLINE)
d.comment(0xAD50, 'TX low = &0C (abort packet starts at workspace[&0C])', align=Align.INLINE)
d.comment(0xAD52, 'Get nfs_workspace high byte', align=Align.INLINE)
d.comment(0xAD54, 'TX high = workspace page (so net_tx_ptr now points at the abort packet in workspace)', align=Align.INLINE)
d.comment(0xAD56, 'Send the abort packet via the standard TX path', align=Align.INLINE)
d.comment(0xAD59, 'A=&3F: TXCB status = abort-complete sentinel', align=Align.INLINE)
d.comment(0xAD5B, 'Write status via (net_tx_ptr,X) -- mark TX done', align=Align.INLINE)
d.comment(0xAD5D, 'Pull saved net_tx_ptr high', align=Align.INLINE)
d.comment(0xAD5E, 'Restore', align=Align.INLINE)
d.comment(0xAD60, 'Pull saved net_tx_ptr low', align=Align.INLINE)
d.comment(0xAD61, "Restore -- caller's TX state intact", align=Align.INLINE)
d.comment(0xAD63, 'Return', align=Align.INLINE)
d.comment(0xBE01, 'Read low nibble of starting address from (work_ae),Y', align=Align.INLINE)
d.comment(0xBE03, "Save it (we'll print it 16 times incrementing each iteration)", align=Align.INLINE)
d.comment(0xBE04, "Print '<CR>Address  : ' header via inline string", align=Align.INLINE)
d.comment(0xBE13, 'X=&0F: print 16 column-number digits', align=Align.INLINE)
d.comment(0xBE15, 'Pull the starting low nibble back into A', align=Align.INLINE)
d.comment(0xBE16, 'Print A as two hex digits + space', align=Align.INLINE)
d.comment(0xBE19, 'Set C ready for the increment', align=Align.INLINE)
d.comment(0xBE1A, 'A += 1 (column index increments, with C set on entry)', align=Align.INLINE)
d.comment(0xBE1C, 'Wrap to nibble (0..15)', align=Align.INLINE)
d.comment(0xBE1E, 'Step column counter', align=Align.INLINE)
d.comment(0xBE1F, 'Loop while X >= 0 (16 iterations)', align=Align.INLINE)
d.comment(0xBE21, "Print ':    ASCII data<CR><CR>' trailer via inline", align=Align.INLINE)
d.comment(0xBE35, 'NOP -- bit-7 terminator + harmless resume opcode', align=Align.INLINE)
d.comment(0xBE36, 'Return', align=Align.INLINE)
d.comment(0xBE42, 'Move command-line offset Y into A for the X copy', align=Align.INLINE)
d.comment(0xBE43, 'X = current command-line offset (live cursor)', align=Align.INLINE)
d.comment(0xBE44, 'A=0: zero-fill value', align=Align.INLINE)
d.comment(0xBE46, 'Y=0: accumulator index', align=Align.INLINE)
d.comment(0xBE47, 'Zero accumulator byte at (work_ae)+Y', align=Align.INLINE)
d.comment(0xBE49, 'Step accumulator', align=Align.INLINE)
d.comment(0xBE4A, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0xBE4C, 'No: continue clearing', align=Align.INLINE)
d.comment(0xBE4E, 'Reload command-line offset', align=Align.INLINE)
d.comment(0xBE4F, 'Step cursor', align=Align.INLINE)
d.comment(0xBE50, 'Y = stepped cursor (for the indirect read)', align=Align.INLINE)
d.comment(0xBE51, 'Read next command-line byte', align=Align.INLINE)
d.comment(0xBE53, 'CR? (end of address)', align=Align.INLINE)
d.comment(0xBE55, 'Yes: range parsed -- exit via space-skip', align=Align.INLINE)
d.comment(0xBE57, 'Space?', align=Align.INLINE)
d.comment(0xBE59, 'Yes: also a separator -- exit', align=Align.INLINE)
d.comment(0xBE5B, "Below '0'?", align=Align.INLINE)
d.comment(0xBE5D, "Yes: not hex -- raise 'Bad hex'", align=Align.INLINE)
d.comment(0xBE5F, "Above '9'?", align=Align.INLINE)
d.comment(0xBE61, "No: it's '0'-'9' -- skip the letter handling", align=Align.INLINE)
d.comment(0xBE63, 'Force uppercase via AND #&5F', align=Align.INLINE)
d.comment(0xBE65, "Add &B8: 'A' (=&41) becomes &F9 with C set; 'F' becomes &FE; this maps 'A'-'F' to &FA-&FF in C", align=Align.INLINE)
d.comment(0xBE67, "Carry out of ADC: digit was below 'A' -> bad hex", align=Align.INLINE)
d.comment(0xBE69, "Below &FA? (i.e. before 'A' in mapped range)", align=Align.INLINE)
d.comment(0xBE6B, 'Yes (out of [&FA,&FF]): bad hex', align=Align.INLINE)
d.comment(0xBE6D, 'Keep low nibble (0-15)', align=Align.INLINE)
d.comment(0xBE6F, 'Push the new nibble', align=Align.INLINE)
d.comment(0xBE70, 'Push X (current command-line offset)', align=Align.INLINE)
d.comment(0xBE72, 'X=4: rotate the 4-byte accumulator left 4 times', align=Align.INLINE)
d.comment(0xBE74, 'Y=0: byte index for the rotate', align=Align.INLINE)
d.comment(0xBE76, "A=0 (and C clear from TYA's flags)", align=Align.INLINE)
d.comment(0xBE77, 'Save A onto stack so we can use PHP/PLP to round-trip carry through the rotate', align=Align.INLINE)
d.comment(0xBE78, 'Pull flags (effectively C clear from the TYA above; on later iterations C carries the bit shifted out)', align=Align.INLINE)
d.comment(0xBE79, 'Read next accumulator byte', align=Align.INLINE)
d.comment(0xBE7B, 'Shift in C from below, shift out top bit to C', align=Align.INLINE)
d.comment(0xBE7C, 'Write back', align=Align.INLINE)
d.comment(0xBE7E, 'Save the new C', align=Align.INLINE)
d.comment(0xBE7F, 'Pull A back (PHA earlier)', align=Align.INLINE)
d.comment(0xBE80, 'Step accumulator byte', align=Align.INLINE)
d.comment(0xBE81, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0xBE83, 'No: rotate next byte', align=Align.INLINE)
d.comment(0xBE85, 'PHA/PLP: bring saved C into flag register', align=Align.INLINE)
d.comment(0xBE87, 'C set: a bit fell off the top -- overflow', align=Align.INLINE)
d.comment(0xBE89, 'Step rotate counter', align=Align.INLINE)
d.comment(0xBE8A, 'Loop while X != 0 (4 rotates total)', align=Align.INLINE)
d.comment(0xBE8C, 'Pull saved X (command-line offset)', align=Align.INLINE)
d.comment(0xBE8D, 'Restore X', align=Align.INLINE)
d.comment(0xBE8E, 'Pull saved nibble into A', align=Align.INLINE)
d.comment(0xBE8F, 'Y=0: low byte of accumulator', align=Align.INLINE)
d.comment(0xBE91, 'OR new nibble into accumulator[0]', align=Align.INLINE)
d.comment(0xBE93, 'Write back', align=Align.INLINE)
d.comment(0xBE95, 'Loop for next hex digit', align=Align.INLINE)
d.comment(0xBE98, 'Discard saved nibble', align=Align.INLINE)
d.comment(0xBE99, 'Discard saved X', align=Align.INLINE)
d.comment(0xBE9A, 'Set C: signal overflow to caller', align=Align.INLINE)
d.comment(0xBE9B, 'Return with C=1', align=Align.INLINE)
d.comment(0xBE9C, 'Close the dump file before raising the error', align=Align.INLINE)
d.comment(0xBE9F, "Raise 'Bad hex' error; never returns", align=Align.INLINE)
d.comment(0xBEA2, 'Step past current space', align=Align.INLINE)
d.comment(0xBEA3, 'Read next byte', align=Align.INLINE)
d.comment(0xBEA5, 'Still a space?', align=Align.INLINE)
d.comment(0xBEA7, 'Yes: keep skipping', align=Align.INLINE)
d.comment(0xBEA9, 'Clear C: signal success', align=Align.INLINE)
d.comment(0xBEAA, 'Return', align=Align.INLINE)
d.comment(0x8028, "Save X (the ROM slot we're being called on behalf of)", align=Align.INLINE)
d.comment(0x8029, 'Save Y (the dispatch-path selector via its high bit)', align=Align.INLINE)
d.comment(0x802A, 'Read deferred-work flag at &0D65 (set by NMI when work queued)', align=Align.INLINE)
d.comment(0x802D, "Non-zero: there's work to dispatch", align=Align.INLINE)
d.comment(0x802F, 'Zero: no work; restore Y', align=Align.INLINE)
d.comment(0x8030, 'Restore X', align=Align.INLINE)
d.comment(0x8031, 'Return to MOS (service unclaimed)', align=Align.INLINE)
d.comment(0x8032, 'A=&80: bit 7 -- the bit to clear in ACCCON', align=Align.INLINE)
d.comment(0x8034, 'Clear ACCCON bit 7 (release IRR mask)', align=Align.INLINE)
d.comment(0x8037, "Zero the deferred-work flag (we're handling it now)", align=Align.INLINE)
d.comment(0x803A, 'Bring saved Y back into A so BMI can test bit 7', align=Align.INLINE)
d.comment(0x803B, "Bit 7 of caller's Y set: dispatch via PHA/PHA/RTS table", align=Align.INLINE)
d.comment(0x8042, 'Tail-jump to tx_done_exit which restores X/Y and claims the service', align=Align.INLINE)
d.comment(0xADD3, 'Y=&0E: scan 15 bytes (offsets 14..0) of the PB', align=Align.INLINE)
d.comment(0xADD5, 'Is the OSWORD number 7?', align=Align.INLINE)
d.comment(0xADD7, 'Yes: handle as either 7 or 8 -- both copy PB to ws', align=Align.INLINE)
d.comment(0xADD9, 'Is the OSWORD number 8?', align=Align.INLINE)
d.comment(0xADDB, 'Neither 7 nor 8: return early (other OSWORDs handled elsewhere)', align=Align.INLINE)
d.comment(0xADDD, 'X=&DB: workspace offset for the PB copy', align=Align.INLINE)
d.comment(0xADDF, 'Temporarily reuse nfs_workspace as the destination low byte (high byte already points at the workspace page)', align=Align.INLINE)
d.comment(0xADE1, 'Read PB[Y]', align=Align.INLINE)
d.comment(0xADE3, 'Write to (nfs_workspace),Y -- effectively writes to workspace[&DB+Y]', align=Align.INLINE)
d.comment(0xADE5, 'Step backwards through the 15 bytes', align=Align.INLINE)
d.comment(0xADE6, 'Loop while Y >= 0', align=Align.INLINE)
d.comment(0xADE8, 'Bring Y back to 0 for the next single-byte write', align=Align.INLINE)
d.comment(0xADE9, 'Decrement nfs_workspace low byte: now points at workspace[&DA] (one before the copied region)', align=Align.INLINE)
d.comment(0xADEB, 'Read original OSWORD number from osbyte_a_copy', align=Align.INLINE)
d.comment(0xADED, 'Store at workspace[&DA] -- so the abort packet header carries the OSWORD number', align=Align.INLINE)
d.comment(0xADEF, 'Restore nfs_workspace to its proper low byte (Y=0)', align=Align.INLINE)
d.comment(0xADF1, 'Y=&14: TXCB control offset', align=Align.INLINE)
d.comment(0xADF3, 'A=&E9: status code for OSWORD-passthrough abort', align=Align.INLINE)
d.comment(0xADF5, 'Store status at TXCB[&14]', align=Align.INLINE)
d.comment(0xADF7, 'A=1: abort code for tx_econet_abort', align=Align.INLINE)
d.comment(0xADF9, 'Send the abort packet', align=Align.INLINE)
d.comment(0xADFC, 'Restore nfs_workspace from X (X is unchanged across tx_econet_abort)', align=Align.INLINE)
d.comment(0xA3C4, "Save caller's X (command-line offset cursor)", align=Align.INLINE)
d.comment(0xA3C5, 'A=0: clear the dot-seen flag for parse_addr_arg', align=Align.INLINE)
d.comment(0xA3C7, 'Store cleared dot-seen flag', align=Align.INLINE)
d.comment(0xA3C9, 'Parse first number (network or standalone station)', align=Align.INLINE)
d.comment(0xA3CC, 'C set: parse_addr_arg saw an empty argument -- skip station storage', align=Align.INLINE)
d.comment(0xA3CE, 'Save the network number in fs_work_7', align=Align.INLINE)
d.comment(0xA3D0, 'Save Y (current command-line cursor) for after the bridge poll', align=Align.INLINE)
d.comment(0xA3D1, 'Populate the bridge routing table -- returns local network number in A', align=Align.INLINE)
d.comment(0xA3D4, 'EOR with parsed network: Z set iff parse matched local', align=Align.INLINE)
d.comment(0xA3D6, 'Match: keep A=0 to mark local network', align=Align.INLINE)
d.comment(0xA3D8, 'Mismatch: A = parsed network number', align=Align.INLINE)
d.comment(0xA3DA, 'Store network number into fs_work_6 (the canonical form: 0=local, non-zero=remote)', align=Align.INLINE)
d.comment(0xA3DC, 'Restore Y', align=Align.INLINE)
d.comment(0xA3DD, 'Step Y past the dot separator', align=Align.INLINE)
d.comment(0xA3DE, 'Parse station number after the dot', align=Align.INLINE)
d.comment(0xA3E1, 'C set: no station after dot -- leave fs_work_5 alone', align=Align.INLINE)
d.comment(0xA3E3, 'Store parsed station in fs_work_5', align=Align.INLINE)
d.comment(0xA3E5, "Restore caller's X", align=Align.INLINE)
d.comment(0xA3E6, 'Return', align=Align.INLINE)
d.comment(0x9776, 'Y=0: process_all_fcbs filter (0 = all FCBs)', align=Align.INLINE)
d.comment(0x9778, 'Walk all 16 FCB slots, calling start_wipe_pass on each', align=Align.INLINE)
d.comment(0x977B, 'OSBYTE &77 = close *SPOOL and *EXEC files', align=Align.INLINE)
d.comment(0x977D, 'Close any open *SPOOL/*EXEC handles', align=Align.INLINE)
d.comment(0x9780, "A=&40: bit 6 of fs_flags = 'FS in active session'", align=Align.INLINE)
d.comment(0x9782, 'Clear bit 6: mark FS session inactive', align=Align.INLINE)
d.comment(0x9785, 'Close every Econet client channel', align=Align.INLINE)
d.comment(0x9788, "Y=&17: FS function code 'Bye' (logoff request)", align=Align.INLINE)
d.comment(0xA398, 'Read current FS station from workspace', align=Align.INLINE)
d.comment(0xA39B, "Save in fs_work_5 (so 'no-arg' path can print it)", align=Align.INLINE)
d.comment(0xA39D, 'Read current FS network', align=Align.INLINE)
d.comment(0xA3A0, 'Save in fs_work_6', align=Align.INLINE)
d.comment(0xA3A2, 'Look at the first command-line byte', align=Align.INLINE)
d.comment(0xA3A4, 'Is it CR (no argument)?', align=Align.INLINE)
d.comment(0xA3A6, 'Yes: print the current FS address', align=Align.INLINE)
d.comment(0xA3A8, "Parse 'net.station' arg into fs_work_5/6", align=Align.INLINE)
d.comment(0xA3AB, 'A=1: OSWORD &13 sub-function 1 = set file server station', align=Align.INLINE)
d.comment(0xA3AD, 'Store sub-function in PB[0]', align=Align.INLINE)
d.comment(0xA3AF, 'A=&13: OSWORD &13', align=Align.INLINE)
d.comment(0xA3B1, 'X = lo of PB pointer (fs_work_4 = &B4)', align=Align.INLINE)
d.comment(0xA3B3, 'Y = hi of PB pointer (=0, since fs_work_4 is in zero page)', align=Align.INLINE)
d.comment(0xA3B5, 'Tail-jump into OSWORD; the OS routes us back through osword_13_set_station', align=Align.INLINE)
d.comment(0x92B2, 'Zero the accumulator (fs_load_addr_2)', align=Align.INLINE)
d.comment(0x92B4, 'Read first command-line byte', align=Align.INLINE)
d.comment(0x92B6, "Hex prefix '&'?", align=Align.INLINE)
d.comment(0x92B8, 'No: try decimal path', align=Align.INLINE)
d.comment(0x92BA, "Yes: skip the '&'", align=Align.INLINE)
d.comment(0x92BB, 'Read first hex digit', align=Align.INLINE)
d.comment(0x92BD, "Always taken (CMP #'&' set C if A>='&'); jump into the hex digit-range check", align=Align.INLINE)
d.comment(0x92BF, 'Step to next character', align=Align.INLINE)
d.comment(0x92C0, 'Read next hex digit candidate', align=Align.INLINE)
d.comment(0x92C2, 'Dot? Net.station separator', align=Align.INLINE)
d.comment(0x92C4, 'Yes: switch to station-parsing mode', align=Align.INLINE)
d.comment(0x92C6, "Below '!' (CR/space)? End of argument", align=Align.INLINE)
d.comment(0x92C8, 'Yes: number complete', align=Align.INLINE)
d.comment(0x92CA, "Below '0'?", align=Align.INLINE)
d.comment(0x92CC, 'Yes: not a hex digit', align=Align.INLINE)
d.comment(0x92CE, "Above '9'? (CMP #':')", align=Align.INLINE)
d.comment(0x92D0, "No (it's '0'-'9'): straight to digit extraction", align=Align.INLINE)
d.comment(0x92D2, 'Force uppercase via AND #&5F', align=Align.INLINE)
d.comment(0x92D4, "Map 'A'-'F' to &FA-&FF (ADC #&B8 with C from earlier CMP #':' which set C)", align=Align.INLINE)
d.comment(0x92D6, "Carry out of ADC: was below 'A' -- bad hex", align=Align.INLINE)
d.comment(0x92D8, "Below &FA? (digit > 'F' overflowed past)", align=Align.INLINE)
d.comment(0x92DA, 'Yes: bad hex (out of [&FA,&FF])', align=Align.INLINE)
d.comment(0x92DC, 'Mask to nibble', align=Align.INLINE)
d.comment(0x92DE, 'Stash digit value in fs_load_addr_3', align=Align.INLINE)
d.comment(0x92E0, 'Load accumulator', align=Align.INLINE)
d.comment(0x92E2, 'Above 16? (would overflow when shifted left 4)', align=Align.INLINE)
d.comment(0x92E4, 'Yes: overflow', align=Align.INLINE)
d.comment(0x92E6, 'Shift accumulator left 4 (multiply by 16)', align=Align.INLINE)
d.comment(0x92E7, '(shift 2)', align=Align.INLINE)
d.comment(0x92E8, '(shift 3)', align=Align.INLINE)
d.comment(0x92E9, '(shift 4)', align=Align.INLINE)
d.comment(0x92EA, 'Add new nibble', align=Align.INLINE)
d.comment(0x92EC, 'Save updated accumulator', align=Align.INLINE)
d.comment(0x92EE, 'No carry: continue (always taken since accumulator was checked < 16 above)', align=Align.INLINE)
d.comment(0x92F0, 'Read next decimal-digit candidate', align=Align.INLINE)
d.comment(0x92F2, 'Dot? Net.station separator', align=Align.INLINE)
d.comment(0x92F4, 'Yes: switch to station-parsing mode', align=Align.INLINE)
d.comment(0x92F6, "Below '!' (CR/space)?", align=Align.INLINE)
d.comment(0x92F8, 'Yes: number complete', align=Align.INLINE)
d.comment(0x92FA, "Test for '0'-'9' and reject '&'/'.'", align=Align.INLINE)
d.comment(0x92FD, 'Not a decimal digit: bad number', align=Align.INLINE)
d.comment(0x92FF, 'Mask to nibble', align=Align.INLINE)
d.comment(0x9301, 'Stash digit', align=Align.INLINE)
d.comment(0x9303, 'Accumulator * 2', align=Align.INLINE)
d.comment(0x9305, 'Overflowed: too big for byte', align=Align.INLINE)
d.comment(0x9307, 'Reload doubled value', align=Align.INLINE)
d.comment(0x9309, '* 2 again (now * 4)', align=Align.INLINE)
d.comment(0x930A, 'Overflow check', align=Align.INLINE)
d.comment(0x930C, '* 2 again (now * 8)', align=Align.INLINE)
d.comment(0x930D, 'Overflow check', align=Align.INLINE)
d.comment(0x930F, '+ accumulator (now * 8 + * 2 = * 10)', align=Align.INLINE)
d.comment(0x9311, 'Overflow check', align=Align.INLINE)
d.comment(0x9313, '+ new digit', align=Align.INLINE)
d.comment(0x9315, 'Overflow check', align=Align.INLINE)
d.comment(0x9317, 'Save * 10 + digit', align=Align.INLINE)
d.comment(0x9319, 'Step input cursor', align=Align.INLINE)
d.comment(0x931A, 'Always taken (Y wraps at 256, never zero in practice)', align=Align.INLINE)
d.comment(0x931C, 'Read mode flag', align=Align.INLINE)
d.comment(0x931E, 'Bit 7 clear: in net.station mode -- validate result', align=Align.INLINE)
d.comment(0x9320, 'Decimal-only mode: get result', align=Align.INLINE)
d.comment(0x9322, 'Result is zero: bad parameter', align=Align.INLINE)
d.comment(0x9324, 'Return with parsed result in A (decimal-only path)', align=Align.INLINE)
d.comment(0x9325, 'Reload result', align=Align.INLINE)
d.comment(0x9327, 'Station 255 is reserved (broadcast)', align=Align.INLINE)
d.comment(0x9329, 'Yes: bad station number', align=Align.INLINE)
d.comment(0x932B, 'Reload result for the next test', align=Align.INLINE)
d.comment(0x932D, 'Non-zero: valid station, return', align=Align.INLINE)
d.comment(0x932F, 'Zero result: must have followed a dot to be valid', align=Align.INLINE)
d.comment(0x9331, 'No dot was seen: bad station number', align=Align.INLINE)
d.comment(0x9333, 'Dot seen: peek the byte before current cursor', align=Align.INLINE)
d.comment(0x9334, 'Read previous byte', align=Align.INLINE)
d.comment(0x9336, 'Restore Y', align=Align.INLINE)
d.comment(0x9337, "Was previous char '.'?", align=Align.INLINE)
d.comment(0x9339, 'No: bad station number', align=Align.INLINE)
d.comment(0x933B, "All checks passed: C=1 marks 'parsed successfully'", align=Align.INLINE)
d.comment(0x933C, 'Return', align=Align.INLINE)
d.comment(0x933D, 'Dot already seen?', align=Align.INLINE)
d.comment(0x933F, "Yes: 'Bad number' (multiple dots)", align=Align.INLINE)
d.comment(0x9341, 'Set dot-seen flag', align=Align.INLINE)
d.comment(0x9343, 'Get parsed network number (before dot)', align=Align.INLINE)
d.comment(0x9345, 'Network 255 is reserved', align=Align.INLINE)
d.comment(0x9347, "Yes: 'Bad network number'", align=Align.INLINE)
d.comment(0x9349, 'Return; caller continues parsing the station', align=Align.INLINE)
d.comment(0xAD64, "Y = OSWORD parameter-block pointer high byte (used as an 'unrecognised' sentinel below)", align=Align.INLINE)
d.comment(0xAD66, 'Code &81? (compatibility shortcut for one specific claim type)', align=Align.INLINE)
d.comment(0xAD68, 'Yes: skip table scan, use match-result with Y already set non-zero', align=Align.INLINE)
d.comment(0xAD6A, 'Y=1: state 2 marker', align=Align.INLINE)
d.comment(0xAD6C, 'X=&0A: scan first 11 entries (table indices 0..&0A)', align=Align.INLINE)
d.comment(0xAD6E, 'Look up A in the claim code table', align=Align.INLINE)
d.comment(0xAD71, 'Match: handle as state 2', align=Align.INLINE)
d.comment(0xAD73, 'DEY: Y=0 (state 3 marker, two DEYs from 1)', align=Align.INLINE)
d.comment(0xAD75, 'X=&11: scan all 18 entries (state 3 also accepts the extended range)', align=Align.INLINE)
d.comment(0xAD77, 'Look up A again with extended range', align=Align.INLINE)
d.comment(0xAD7A, 'Match: handle as state 3', align=Align.INLINE)
d.comment(0xAD7C, 'Y=1 again (no match found, will return below)', align=Align.INLINE)
d.comment(0xAD7D, 'X=2: default state code passed to tx_econet_abort', align=Align.INLINE)
d.comment(0xAD7F, 'Move match marker (Y) into A for the BEQ test', align=Align.INLINE)
d.comment(0xAD80, 'Y=0 (no match): return without action', align=Align.INLINE)
d.comment(0xAD82, "Save flags so we can branch later on Y's sign", align=Align.INLINE)
d.comment(0xAD83, 'Y > 0 (state 2): skip the X bump', align=Align.INLINE)
d.comment(0xAD85, 'State 3: X=3 (different abort code)', align=Align.INLINE)
d.comment(0xAD86, 'Y=&DC: workspace offset for tube state bytes', align=Align.INLINE)
d.comment(0xAD88, 'Read tube_claimed_id,Y', align=Align.INLINE)
d.comment(0xAD8B, 'Save in workspace[&DC..]', align=Align.INLINE)
d.comment(0xAD8D, 'Step backwards', align=Align.INLINE)
d.comment(0xAD8E, 'Done at &DA?', align=Align.INLINE)
d.comment(0xAD90, 'Loop while Y > &DA (saves &DA, &DB, &DC -- 3 bytes)', align=Align.INLINE)
d.comment(0xAD92, 'Move state code (2 or 3) into A for the abort', align=Align.INLINE)
d.comment(0xAD93, 'Send abort with the state code', align=Align.INLINE)
d.comment(0xAD96, "Restore the saved flags (Y's sign)", align=Align.INLINE)
d.comment(0xAD97, 'Y was positive (state 2): just return', align=Align.INLINE)
d.comment(0xAD99, "A=&7F: 'pending response' control value", align=Align.INLINE)
d.comment(0xAD9B, 'Y=&0C: TXCB control offset', align=Align.INLINE)
d.comment(0xAD9D, 'Mark TXCB as pending', align=Align.INLINE)
d.comment(0xAD9F, 'Read TXCB status byte', align=Align.INLINE)
d.comment(0xADA1, 'Bit 7 still clear: keep polling for response', align=Align.INLINE)
d.comment(0xADA3, "Capture S so we can patch the caller's stack frame", align=Align.INLINE)
d.comment(0xADA4, 'Y=&DD: highest workspace offset for the response copy', align=Align.INLINE)
d.comment(0xADA6, 'Read first response byte (workspace[&DD])', align=Align.INLINE)
d.comment(0xADAA, 'Always taken (after ORA result is non-zero); store into stack[&106+X] then walk down', align=Align.INLINE)
d.comment(0xADAC, 'Step Y down', align=Align.INLINE)
d.comment(0xADAD, 'Step X down (stack offset)', align=Align.INLINE)
d.comment(0xADAE, 'Read next workspace byte', align=Align.INLINE)
d.comment(0xADB0, "Patch caller's stack frame at &106+X", align=Align.INLINE)
d.comment(0xADB3, 'Reached &DA (lower workspace bound)?', align=Align.INLINE)
d.comment(0xADB5, 'No: keep restoring', align=Align.INLINE)
d.comment(0xADB7, 'Return', align=Align.INLINE)
d.comment(0xB6F3, 'Reset access flags before parsing the new argument', align=Align.INLINE)
d.comment(0xB6F6, 'A=0: clear the file-iteration counter', align=Align.INLINE)
d.comment(0xB6F8, 'Store iteration counter (steps to next file each loop)', align=Align.INLINE)
d.comment(0xB6FA, 'Save text pointer for re-reading the wildcard each iteration', align=Align.INLINE)
d.comment(0xB6FD, 'Parse the wildcard filename into the &C030 buffer', align=Align.INLINE)
d.comment(0xB700, 'Step X past the CR terminator (so X = filename length+1)', align=Align.INLINE)
d.comment(0xB701, 'Save end-of-buffer offset', align=Align.INLINE)
d.comment(0xB703, 'FS function code byte 0 = 1 (examine)', align=Align.INLINE)
d.comment(0xB705, "TXCB[5] = 1: 'examine directory entry'", align=Align.INLINE)
d.comment(0xB708, 'TXCB[7] = 1: ditto for the second buffer slot', align=Align.INLINE)
d.comment(0xB70B, 'Load current iteration index', align=Align.INLINE)
d.comment(0xB70D, 'TXCB[6] = iteration index (which directory entry)', align=Align.INLINE)
d.comment(0xB710, 'X=3: copy starting at TX[3] (after the FS header bytes)', align=Align.INLINE)
d.comment(0xB712, 'Copy the parsed filename into the TX buffer', align=Align.INLINE)
d.comment(0xB715, "Y=3: FS function code 'Examine'", align=Align.INLINE)
d.comment(0xB717, 'A=&80: set bit 7 of need_release_tube to flag long-lived TX', align=Align.INLINE)
d.comment(0xB719, 'Store flag', align=Align.INLINE)
d.comment(0xB71B, 'Send the examine request and wait for reply', align=Align.INLINE)
d.comment(0xB71E, 'Read FS reply byte 0 (status code)', align=Align.INLINE)
d.comment(0xB721, 'Non-zero status: process the response', align=Align.INLINE)
d.comment(0xB723, 'OSBYTE &0F: flush input buffer class', align=Align.INLINE)
d.comment(0xB725, 'X=1: flush keyboard buffer', align=Align.INLINE)
d.comment(0xB727, 'Flush keyboard buffer (clear pending Y/N keypress)', align=Align.INLINE)
d.comment(0xB72A, 'OSBYTE &7A: scan keyboard from key 16 (clear keypress queue)', align=Align.INLINE)
d.comment(0xB72C, 'Run the scan', align=Align.INLINE)
d.comment(0xB72F, 'Y=0: no key', align=Align.INLINE)
d.comment(0xB731, 'OSBYTE &78: write keys-pressed state', align=Align.INLINE)
d.comment(0xB733, 'Tail-call OSBYTE: clean up and return', align=Align.INLINE)
d.comment(0xB736, 'Read attribute byte from FS reply (TXCB[&2F])', align=Align.INLINE)
d.comment(0xB739, "Is it 'L' (locked)?", align=Align.INLINE)
d.comment(0xB73B, 'Not locked: check for directory', align=Align.INLINE)
d.comment(0xB73D, 'Locked: skip this file, advance to next', align=Align.INLINE)
d.comment(0xB73F, 'Loop back to request the next directory entry', align=Align.INLINE)
d.comment(0xB742, "Is it 'D' (directory)?", align=Align.INLINE)
d.comment(0xB744, 'Not a directory: prompt the user', align=Align.INLINE)
d.comment(0xB746, 'Directory: check second attribute byte (size)', align=Align.INLINE)
d.comment(0xB749, 'Loop back to attribute test (re-checks if non-empty)', align=Align.INLINE)
d.comment(0xB74B, 'X=1: scan name starting at TX[1]', align=Align.INLINE)
d.comment(0xB74D, 'Y = end-of-buffer offset (saved earlier in fs_work_6)', align=Align.INLINE)
d.comment(0xB74F, 'Read filename byte from TX[6+X]', align=Align.INLINE)
d.comment(0xB752, 'Print via *SPOOL-bypassing OSASCI', align=Align.INLINE)
d.comment(0xB755, 'Also store into the parse buffer for later use', align=Align.INLINE)
d.comment(0xB758, 'Step parse-buffer offset', align=Align.INLINE)
d.comment(0xB759, 'Step TX-buffer offset', align=Align.INLINE)
d.comment(0xB75A, 'Reached &0C (12 chars)?', align=Align.INLINE)
d.comment(0xB75C, 'No: continue copying', align=Align.INLINE)
d.comment(0xB75E, "Print '(?/' prompt prefix and read response", align=Align.INLINE)
d.comment(0xB761, "Inline string '(?/' is read by the hook above", align=Align.INLINE)
d.comment(0xB764, "NOP -- bit-7 terminator + resume opcode for the '(?/' stringhi", align=Align.INLINE)
d.comment(0xB765, "Print 'Y/N) ' via prompt_yn (reads keypress)", align=Align.INLINE)
d.comment(0xB768, "Was the keypress '?' (help)?", align=Align.INLINE)
d.comment(0xB76A, "Not '?': process Y/N response", align=Align.INLINE)
d.comment(0xB76C, "'?': print CR before help text", align=Align.INLINE)
d.comment(0xB76E, 'Print CR character', align=Align.INLINE)
d.comment(0xB771, 'X=2: start of name in TX[2]', align=Align.INLINE)
d.comment(0xB773, 'Read name byte from TX[5+X] (FS reply)', align=Align.INLINE)
d.comment(0xB776, 'Print name char (no spool)', align=Align.INLINE)
d.comment(0xB779, 'Advance index', align=Align.INLINE)
d.comment(0xB77A, 'End of TX[5+X] name field at offset &3E?', align=Align.INLINE)
d.comment(0xB77C, 'No: continue printing', align=Align.INLINE)
d.comment(0xB77E, "Print 'Wipe? ' help suffix via inline string", align=Align.INLINE)
d.comment(0xB783, 'Bit-7 terminator + resume', align=Align.INLINE)
d.comment(0xB784, 'Re-prompt user with prompt_yn', align=Align.INLINE)
d.comment(0xB787, "Mask to upper-case ('A'..'Z' map to themselves)", align=Align.INLINE)
d.comment(0xB789, "Was the response 'Y'?", align=Align.INLINE)
d.comment(0xB78B, 'No: skip this entry, advance to next', align=Align.INLINE)
d.comment(0xB78D, 'Yes: echo the keypress', align=Align.INLINE)
d.comment(0xB790, 'X=0: start scanning the parse-buffer name', align=Align.INLINE)
d.comment(0xB792, 'Read first parse-buffer byte at hazel_parse_buf', align=Align.INLINE)
d.comment(0xB795, 'Is it CR (no path component)?', align=Align.INLINE)
d.comment(0xB797, 'Yes: use leaf-name only path at &B7BD', align=Align.INLINE)
d.comment(0xB799, 'Read parse-buffer byte at hazel_parse_buf+X', align=Align.INLINE)
d.comment(0xB79C, 'Is it CR (end of name)?', align=Align.INLINE)
d.comment(0xB79E, 'No: check for space separator', align=Align.INLINE)
d.comment(0xB7A0, "CR: substitute '.' so the dir prefix terminates with a separator", align=Align.INLINE)
d.comment(0xB7A2, 'Is it space?', align=Align.INLINE)
d.comment(0xB7A4, 'No: store byte as-is', align=Align.INLINE)
d.comment(0xB7A6, 'Yes: substitute CR (end-of-cmd)', align=Align.INLINE)
d.comment(0xB7A8, 'Store byte into TX[5+X] (delete-command buffer)', align=Align.INLINE)
d.comment(0xB7AB, 'Advance index', align=Align.INLINE)
d.comment(0xB7AC, 'Was that byte CR (just stored)?', align=Align.INLINE)
d.comment(0xB7AE, 'No: continue copying', align=Align.INLINE)
d.comment(0xB7B0, 'Y=&14: FS function code &14 = delete', align=Align.INLINE)
d.comment(0xB7B2, 'Send the delete request and wait for reply', align=Align.INLINE)
d.comment(0xB7B5, 'Decrement iteration counter so we re-examine the now-shifted-up slot', align=Align.INLINE)
d.comment(0xB7B7, 'Print newline before next entry', align=Align.INLINE)
d.comment(0xB7BA, 'Loop back to skip_wipe_locked (= request next entry)', align=Align.INLINE)
d.comment(0xB7BD, 'DEX: pre-decrement before the INX in the loop', align=Align.INLINE)
d.comment(0xB7BE, 'Advance index', align=Align.INLINE)
d.comment(0xB7BF, 'Read parse-buffer byte at hazel_parse_buf_1+X (skip CR at hazel_parse_buf)', align=Align.INLINE)
d.comment(0xB7C2, 'Store into TX[5+X] (delete-command buffer)', align=Align.INLINE)
d.comment(0xB7C5, 'Reached space (end-of-leaf)?', align=Align.INLINE)
d.comment(0xB7C7, 'No: continue copying', align=Align.INLINE)
d.comment(0x959A, 'Read first command-line char at (os_text_ptr),Y', align=Align.INLINE)
d.comment(0x959C, 'Is it CR (no argument supplied)?', align=Align.INLINE)
d.comment(0x959E, 'Non-CR: argument present -- exit via dispatch_fs_ps_with_arg (X=&A0)', align=Align.INLINE)
d.comment(0x95A0, "CR: print 'FS       ' header", align=Align.INLINE)
d.comment(0x95A3, "Print '[<D>.]<D>\\r'", align=Align.INLINE)
d.comment(0x95A6, "Print 'PS       ' header", align=Align.INLINE)
d.comment(0x95A9, "Print '[<D>.]<D>\\r' again", align=Align.INLINE)
d.comment(0x95AC, "Print final 'Space\\rNoSpace\\r' lines", align=Align.INLINE)
d.comment(0x95BD, 'NOP -- bit-7 terminator + resume opcode for the preceding inline string', align=Align.INLINE)
d.comment(0x95C1, "Print 'P' prefix", align=Align.INLINE)
d.comment(0x95C5, 'CLV -- bit-7 terminator + resume (V flag is irrelevant here, used as 1-byte resume opcode)', align=Align.INLINE)
d.comment(0x95C6, "BVC: V was just cleared -> always taken; falls into the shared 'S       ' tail at &95CD", align=Align.INLINE)
d.comment(0x95C8, "Print 'F' prefix", align=Align.INLINE)
d.comment(0x95CC, "NOP -- bit-7 terminator; falls through into the shared 'S       ' tail at &95CD", align=Align.INLINE)
d.comment(0x95CD, "Print 'S       ' (S + 7 spaces) -- the shared 8-char field used by both 'FS' and 'PS' callers", align=Align.INLINE)
d.comment(0x95D8, 'Bit-7 terminator', align=Align.INLINE)
d.comment(0x95D9, 'Return', align=Align.INLINE)
d.comment(0x95DA, "Print '[<D>.]<D>\\r' (file-name syntax fragment, shared between *FS/*PS no-arg help and *Dir)", align=Align.INLINE)
d.comment(0x95E7, 'Bit-7 terminator', align=Align.INLINE)
d.comment(0x95E8, 'Return', align=Align.INLINE)
d.comment(0x95E9, 'X=&A0: index into svc4 dispatch table (no-arg path)', align=Align.INLINE)
d.comment(0x95EB, 'Tail-jump to svc4_dispatch_lookup with X=&A0', align=Align.INLINE)
d.comment(0xA5FB, 'Store low byte of (os_text_ptr + Y) -> fs_crc_lo (repurposed as a generic pointer)', align=Align.INLINE)
d.comment(0xA5FD, 'Load os_text_ptr_hi for the high-byte add', align=Align.INLINE)
d.comment(0xA5FF, 'Add carry from low add (no extra increment)', align=Align.INLINE)
d.comment(0xA601, 'Store result high byte -> fs_crc_hi', align=Align.INLINE)
d.comment(0xA9EF, 'A=&0E: bits 1..3 (FS-state mask)', align=Align.INLINE)
d.comment(0xA9F1, 'Set fs_flags bits 1..3', align=Align.INLINE)
d.comment(0xA9F4, 'A=&40: FS-active flag bit', align=Align.INLINE)
d.comment(0xA9F6, 'Clear FS-active flag (bit 6)', align=Align.INLINE)
d.comment(0xA9F9, 'X=&0F: scan all 16 FCB slots (X = 15 down to 0)', align=Align.INLINE)
d.comment(0xAABB, 'Mirror A into ws_0d68 (ACR-format byte)', align=Align.INLINE)
d.comment(0xAABE, 'Mirror A into ws_0d69 (IER-format byte)', align=Align.INLINE)
d.comment(0xAAC1, 'Return', align=Align.INLINE)
d.comment(0xB60F, 'Y=&18: name field offset in RX buffer', align=Align.INLINE)
d.comment(0xB624, 'Bit-7 terminator from preceding stringhi', align=Align.INLINE)
d.comment(0xB625, 'Pop saved slot index', align=Align.INLINE)
d.comment(0xB649, 'X=0: indexed-indirect access mode', align=Align.INLINE)
d.comment(0xB657, 'Ensure V clear so next BVC always taken', align=Align.INLINE)
d.comment(0xB675, 'Advance work_ae to next status byte (lo)', align=Align.INLINE)
d.comment(0xB68E, 'Advance work_ae to next status byte (lo)', align=Align.INLINE)
d.comment(0xB690, 'Read network number byte via (work_ae,X)', align=Align.INLINE)
d.comment(0xBF58, 'Read low byte of address from (work_ae)+Y', align=Align.INLINE)
d.comment(0xBF5A, 'Add osword_flag+Y (low byte of length, with carry propagating)', align=Align.INLINE)
d.comment(0xBF5D, 'Store sum back to osword_flag+Y', align=Align.INLINE)
d.comment(0xBF60, 'Advance to next byte', align=Align.INLINE)
d.comment(0xBF61, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xBF62, 'Loop until 4 bytes added', align=Align.INLINE)
d.comment(0xBF64, 'Y=&14: target offset = workspace+&13 (top of end-addr field, stored hi-byte-first)', align=Align.INLINE)
d.comment(0xBF66, 'X=3: source = osword_flag+3 (top byte of sum)', align=Align.INLINE)
d.comment(0xBF68, 'Pre-decrement Y (so first store is to offset &13)', align=Align.INLINE)
d.comment(0xBF69, 'Read sum byte from osword_flag+X', align=Align.INLINE)
d.comment(0xBF6B, 'Store at (work_ae)+Y', align=Align.INLINE)
d.comment(0xBF6D, 'Decrement source index', align=Align.INLINE)
d.comment(0xBF6E, 'Loop until X wraps below 0', align=Align.INLINE)
d.comment(0xBF70, 'Return', align=Align.INLINE)
d.comment(0x8900, 'Read ACCCON (Master 128 access-control register)', align=Align.INLINE)
d.comment(0x8903, 'Set bit 3 of A (transfer-mode flag)', align=Align.INLINE)
d.comment(0x8905, 'Store as escapable mode', align=Align.INLINE)
d.comment(0x8907, 'Y=7: scout-bytes counter', align=Align.INLINE)
d.comment(0x8914, 'C clear: no Tube, plain transfer path', align=Align.INLINE)
d.comment(0x8916, 'Z clear (other state set): use fallback path', align=Align.INLINE)
d.comment(0x8918, 'Z set: re-read ACCCON for second decision', align=Align.INLINE)
d.comment(0x891B, 'Rotate bit 0 (E flag) into C', align=Align.INLINE)
d.comment(0x891C, 'C clear: shadow not enabled, fallback path', align=Align.INLINE)
d.comment(0x891E, 'Shadow enabled: set bit 2 of escapable', align=Align.INLINE)
d.comment(0x8920, 'Atomic bit-set on escapable', align=Align.INLINE)
d.comment(0x8922, 'Branch to fallback_calc_transfer (always)', align=Align.INLINE)
d.comment(0x8A59, 'Save Y on stack across the version-check', align=Align.INLINE)
d.comment(0x8A8C, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x8ABA, 'C clear: service number was below the prior CMP threshold, take dispatch fall-through', align=Align.INLINE)
d.comment(0x8ABC, 'Subtract 5 to remap service range', align=Align.INLINE)
d.comment(0x8ABE, 'Compare with &0E', align=Align.INLINE)
d.comment(0x8AC0, 'Equal: dispatch directly', align=Align.INLINE)
d.comment(0x8AC2, 'Below: take dispatch fall-through', align=Align.INLINE)
d.comment(0x8AC4, 'Subtract 8 to remap further', align=Align.INLINE)
d.comment(0x8AC6, 'Compare with &0F', align=Align.INLINE)
d.comment(0x8AC8, 'Below: dispatch fall-through', align=Align.INLINE)
d.comment(0x8ACA, 'Compare with &18', align=Align.INLINE)
d.comment(0x8ACC, 'Below: dispatch index now in A', align=Align.INLINE)
d.comment(0x989F, 'Y=0: status byte offset', align=Align.INLINE)
d.comment(0x98A1, 'Read RX status byte', align=Align.INLINE)
d.comment(0x98A3, 'Zero status: re-init the session', align=Align.INLINE)
d.comment(0x98A5, 'Y=&80: session-ID byte offset in RX', align=Align.INLINE)
d.comment(0x98A7, 'Read remote session-ID', align=Align.INLINE)
d.comment(0x98A9, 'Y=&0E: stored session-ID offset in workspace', align=Align.INLINE)
d.comment(0x98AB, 'Compare with stored ID', align=Align.INLINE)
d.comment(0x98AD, 'Mismatch: skip the commit (treat as foreign)', align=Align.INLINE)
d.comment(0xAD32, 'Read the MOS stack frame holding caller flags', align=Align.INLINE)
d.comment(0xAD33, 'Shift carry out of caller P (stack[&106+X])', align=Align.INLINE)
d.comment(0xAD36, 'Carry is now cleared in caller P', align=Align.INLINE)
d.comment(0xAD3A, 'Y=&DA: workspace osword-4 result offset', align=Align.INLINE)
d.comment(0xAD3C, 'Store Y at (nfs_workspace)+&DA', align=Align.INLINE)
d.comment(0xAD3E, 'A=0: clear A for the abort path', align=Align.INLINE)
d.comment(0xA644, 'X=&10: scan 16 entries', align=Align.INLINE)
d.comment(0xA646, 'Clear V (no-match marker)', align=Align.INLINE)
d.comment(0xA647, 'Step to previous entry', align=Align.INLINE)
d.comment(0xA648, 'Below 0: scan complete', align=Align.INLINE)
d.comment(0xA64A, "Compare entry X's stn/net with caller's", align=Align.INLINE)
d.comment(0xA64D, 'No match: continue', align=Align.INLINE)
d.comment(0xA64F, "Match: read entry's flag byte at hazel_fcb_status+X", align=Align.INLINE)
d.comment(0xA652, 'Mask bit 2', align=Align.INLINE)
d.comment(0xA654, 'Bit 2 clear: keep scanning', align=Align.INLINE)
d.comment(0xA656, 'Bit 2 set: A = matched entry index (Y)', align=Align.INLINE)
d.comment(0xA657, 'Store Y at hazel_fcb_slot_attr+X (link entry to slot)', align=Align.INLINE)
d.comment(0xA65A, 'BIT always_set_v_byte: V <- 1 (match found)', align=Align.INLINE)
d.comment(0xA65D, 'Save Y at hazel_fs_saved_station (matched entry index)', align=Align.INLINE)
d.comment(0xA660, 'V set: skip new-slot alloc', align=Align.INLINE)
d.comment(0xA662, "A = caller's index", align=Align.INLINE)
d.comment(0xA663, 'Allocate a fresh FCB slot', align=Align.INLINE)
d.comment(0xA666, 'Save FCB slot index at hazel_fcb_slot_1', align=Align.INLINE)
d.comment(0xA669, 'Z set: alloc failed -> restore FS context', align=Align.INLINE)
d.comment(0xA66B, 'A=&26: workspace flag for bit 2 search', align=Align.INLINE)
d.comment(0xA66F, 'X=&10: scan 16 entries', align=Align.INLINE)
d.comment(0xA671, 'Clear V (no-match marker)', align=Align.INLINE)
d.comment(0xA672, 'Step to previous entry', align=Align.INLINE)
d.comment(0xA673, 'Below 0: scan complete', align=Align.INLINE)
d.comment(0xA675, "Compare entry's stn/net with caller's", align=Align.INLINE)
d.comment(0xA678, 'No match: continue', align=Align.INLINE)
d.comment(0xA67A, "Match: read entry's flag byte at hazel_fcb_status+X", align=Align.INLINE)
d.comment(0xA67D, 'Mask bit 3', align=Align.INLINE)
d.comment(0xA67F, 'Bit 3 clear: keep scanning', align=Align.INLINE)
d.comment(0xA681, 'Bit 3 set: A = matched entry index (Y)', align=Align.INLINE)
d.comment(0xA682, 'Store Y at hazel_fcb_slot_attr+X (link entry to slot)', align=Align.INLINE)
d.comment(0xA685, 'BIT always_set_v_byte: V <- 1 (match found)', align=Align.INLINE)
d.comment(0xA688, 'Save Y at hazel_fs_context_copy (matched entry index)', align=Align.INLINE)
d.comment(0xA68B, 'V set: skip new-slot alloc', align=Align.INLINE)
d.comment(0xA68D, "A = caller's index", align=Align.INLINE)
d.comment(0xA68E, 'Allocate a fresh FCB slot', align=Align.INLINE)
d.comment(0xA691, 'Save FCB slot index at hazel_fcb_slot_2', align=Align.INLINE)
d.comment(0xA694, 'Z set: alloc failed -> restore FS context', align=Align.INLINE)
d.comment(0xA696, 'A=&2A: workspace flag for bit 3 search', align=Align.INLINE)
d.comment(0xA42F, 'Set text/transfer pointers from FS context', align=Align.INLINE)
d.comment(0xA432, 'Y=&FF -- mark spool/Tube state inactive', align=Align.INLINE)
d.comment(0xA434, 'Store fs_spool_handle = &FF', align=Align.INLINE)
d.comment(0xA436, 'Store need_release_tube = &FF', align=Align.INLINE)
d.comment(0xA439, 'X=&35: NFS-commands sub-table offset', align=Align.INLINE)
d.comment(0xA43B, 'Match against the NFS sub-table', align=Align.INLINE)
d.comment(0xA43E, 'C set: no match -> dispatch via fall-through', align=Align.INLINE)
d.comment(0x98AF, 'Y=&82: keypress byte offset in RX', align=Align.INLINE)
d.comment(0x98B1, 'Read remote keypress code', align=Align.INLINE)
d.comment(0x98B3, 'Y = key code', align=Align.INLINE)
d.comment(0x98B4, 'X=0: keyboard buffer ID', align=Align.INLINE)
d.comment(0x98B6, 'Commit the language-reply state', align=Align.INLINE)
d.comment(0x98B9, 'OSBYTE &99: insert byte into input buffer', align=Align.INLINE)
d.comment(0xB477, 'Y=2: workspace offset for stored station', align=Align.INLINE)
d.comment(0xB479, 'Load station number', align=Align.INLINE)
d.comment(0xB47B, 'Store at (nfs_workspace)+2', align=Align.INLINE)
d.comment(0xB47E, 'Load network number', align=Align.INLINE)
d.comment(0xB480, 'Store at (nfs_workspace)+3', align=Align.INLINE)
d.comment(0xB482, 'Return', align=Align.INLINE)
d.comment(0x9353, 'Test fs_work_4 bit 7', align=Align.INLINE)
d.comment(0x9355, 'Bit 7 set: redirect to error_bad_param', align=Align.INLINE)
d.comment(0x9357, "A=&D0: 'Bad station' error code", align=Align.INLINE)
d.comment(0x9359, 'Raise via error_bad_inline (never returns)', align=Align.INLINE)
d.comment(0x936B, "A=&F0: 'Bad number' error code", align=Align.INLINE)
d.comment(0x936D, 'Raise via error_bad_inline (never returns)', align=Align.INLINE)
d.comment(0x9377, "A=&94: 'Bad parameter' error code", align=Align.INLINE)
d.comment(0x9379, 'Raise via error_bad_inline (never returns)', align=Align.INLINE)
d.comment(0x9386, "A=&D1: 'Bad net number' error code", align=Align.INLINE)
d.comment(0x9388, 'Raise via error_bad_inline (never returns)', align=Align.INLINE)
d.comment(0xA4E4, 'Save text pointer (for GSREAD-driven parsing)', align=Align.INLINE)
d.comment(0xA4E7, 'Reset fs_lib_flags low bits to 5-bit access mask', align=Align.INLINE)
d.comment(0xA4EA, 'Set bit 1 of A (mark *RUN-style invocation)', align=Align.INLINE)
d.comment(0xA44E, 'A=0: clear svc_state', align=Align.INLINE)
d.comment(0xA450, 'Store -> svc_state', align=Align.INLINE)
d.comment(0xA452, 'Load dispatch hi byte from cmd_dispatch_hi_table+X', align=Align.INLINE)
d.comment(0xA455, 'Push hi for RTS dispatch', align=Align.INLINE)
d.comment(0xA456, 'Load dispatch lo byte from cmd_dispatch_lo_table+X', align=Align.INLINE)
d.comment(0xA459, 'Push lo for RTS dispatch', align=Align.INLINE)
d.comment(0xA45A, 'RTS -> dispatched command handler', align=Align.INLINE)
d.comment(0x8F10, "Save Y on stack (caller's claim)", align=Align.INLINE)
d.comment(0x8F11, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0x8F13, 'Read CMOS &11 via osbyte_a1', align=Align.INLINE)
d.comment(0x8F16, 'A = CMOS &11 value', align=Align.INLINE)
d.comment(0x8F17, 'Mask bit 2 (workspace-size flag)', align=Align.INLINE)
d.comment(0x8F19, "Bit 2 set: keep caller's Y, advance by 2", align=Align.INLINE)
d.comment(0x8F1B, 'Bit 2 clear: A=&0B (use 11-page minimum)', align=Align.INLINE)
d.comment(0x8F1D, 'BRA to common tail', align=Align.INLINE)
d.comment(0x8F1F, 'Bit-2-set path: restore Y', align=Align.INLINE)
d.comment(0x8F20, 'TYA / INY / INY -- raise Y by 2 pages', align=Align.INLINE)
d.comment(0x8F21, 'Y += 1', align=Align.INLINE)
d.comment(0x8F22, 'Y += 1 again (total +2)', align=Align.INLINE)
d.comment(0x8F23, 'Push raised Y', align=Align.INLINE)
d.comment(0x8F24, 'Store final page count high to net_rx_ptr_hi', align=Align.INLINE)
d.comment(0x8F26, 'Increment for nfs_workspace_hi', align=Align.INLINE)
d.comment(0x8F27, 'Store workspace high page', align=Align.INLINE)
d.comment(0x8F29, 'A=0: clear-byte for the lo halves below', align=Align.INLINE)
d.comment(0x8F2B, 'Clear net_rx_ptr_lo (page-aligned)', align=Align.INLINE)
d.comment(0x8F2D, 'Clear nfs_workspace_lo (page-aligned)', align=Align.INLINE)
d.comment(0x8F2F, 'Compute workspace start page via get_ws_page', align=Align.INLINE)
d.comment(0x8F32, 'Y >= &DC?', align=Align.INLINE)
d.comment(0x8F34, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x8F35, 'Yes: jump to set_rom_ws_page (error path)', align=Align.INLINE)
d.comment(0x8F37, 'Return', align=Align.INLINE)
d.comment(0x9850, 'Y=0: status byte offset', align=Align.INLINE)
d.comment(0x9852, 'Read RX status byte', align=Align.INLINE)
d.comment(0x9854, 'Zero: re-init the session', align=Align.INLINE)
d.comment(0x9856, 'Non-zero: commit state and continue', align=Align.INLINE)
d.comment(0x9859, "Mark session as 'remote boot'", align=Align.INLINE)
d.comment(0x985B, 'Store updated status byte back to RX[0]', align=Align.INLINE)
d.comment(0x985D, 'X=&80: caller machine-id byte offset', align=Align.INLINE)
d.comment(0x985F, 'Y=&80: same offset', align=Align.INLINE)
d.comment(0x9861, 'Read remote machine ID', align=Align.INLINE)
d.comment(0x9863, 'Push -- save across the workspace store', align=Align.INLINE)
d.comment(0x9865, 'Re-read for the second store target', align=Align.INLINE)
d.comment(0x9867, 'Y=&0F: workspace machine-ID lo offset', align=Align.INLINE)
d.comment(0x9869, 'Store at (nfs_workspace)+&0F', align=Align.INLINE)
d.comment(0x986C, 'Pop saved machine ID', align=Align.INLINE)
d.comment(0x986D, 'Store at (nfs_workspace)+&0F (reuse)', align=Align.INLINE)
d.comment(0x986F, 'Scan remote-key flags', align=Align.INLINE)
d.comment(0x9872, 'Initialise narrow workspace template', align=Align.INLINE)
d.comment(0x9875, 'X=1: enable Econet keyboard', align=Align.INLINE)
d.comment(0x9877, 'Y=0', align=Align.INLINE)
d.comment(0x9879, 'OSBYTE &C9: read/write Econet keyboard disable', align=Align.INLINE)
d.comment(0xB275, "Test for '#' prefix (3 ^ &23 = 0)", align=Align.INLINE)
d.comment(0xB277, "Equal: '#' was the prefix, return", align=Align.INLINE)
d.comment(0xB279, 'Other: not a recognised prefix -> error', align=Align.INLINE)
d.comment(0xB27C, "Test for ':' (&3F ^ &1C)", align=Align.INLINE)
d.comment(0xB27E, 'Different: caller had no prefix, return', align=Align.INLINE)
d.comment(0xB280, "':' confirmed -- read next char from parse buffer", align=Align.INLINE)
d.comment(0xB283, "Test for '.' (path separator)", align=Align.INLINE)
d.comment(0xB285, "Equal: ':.' qualified prefix", align=Align.INLINE)
d.comment(0xB287, "Test for '#'", align=Align.INLINE)
d.comment(0xB289, 'Other: no recognised tail prefix, return', align=Align.INLINE)
d.comment(0xB28B, 'Recognised: load fs_lib_flags', align=Align.INLINE)
d.comment(0xB28E, 'Set bit 6 (FS-select pending)', align=Align.INLINE)
d.comment(0xB290, 'Store updated fs_lib_flags', align=Align.INLINE)
d.comment(0xB293, 'Recurse to strip the trailing component', align=Align.INLINE)
d.comment(0xB296, 'Decrement X (consume processed char)', align=Align.INLINE)
d.comment(0xB297, 'Return', align=Align.INLINE)
d.comment(0xA5C9, 'A = parsed character', align=Align.INLINE)
d.comment(0xA5D2, 'Y=3: skip past 3-byte FS header', align=Align.INLINE)
d.comment(0xA5E4, 'For the loop entry', align=Align.INLINE)
d.comment(0xA5EB, 'Always (BCC after CLC) loop back', align=Align.INLINE)
d.comment(0xA5EE, 'Advance Y past trailing space', align=Align.INLINE)
d.comment(0xA5F5, 'Test for CR (terminator)', align=Align.INLINE)
d.comment(0xA5F7, 'Clear C for arithmetic', align=Align.INLINE)
d.comment(0xA606, 'X=&C0: pointer-to-options high byte', align=Align.INLINE)
d.comment(0xA60C, 'Store as fs_options', align=Align.INLINE)
d.comment(0xA62C, 'Y=&C1: high byte of TX buffer pointer', align=Align.INLINE)
d.comment(0xA62E, 'A=4: option byte for *RUN', align=Align.INLINE)
d.comment(0xA630, 'Relocated execute path', align=Align.INLINE)
d.comment(0xA633, 'A=1: dispatch flag', align=Align.INLINE)
d.comment(0xA635, 'Indirect jump via workspace vector', align=Align.INLINE)
d.comment(0xA867, 'Push for stack frame manipulation', align=Align.INLINE)
d.comment(0xA86B, 'Push again', align=Align.INLINE)
d.comment(0xA879, 'A = sub-code', align=Align.INLINE)
d.comment(0xA884, 'Compare with &04', align=Align.INLINE)
d.comment(0xA871, 'PB-ready / parameter table (3 bytes) read by osword_setup_handler at &A868 via LDA osword_pb_ready,X', align=Align.INLINE)
d.comment(0xA874, 'BIT $abs -- 3-byte skip-trick that jumps over the extract_osword_subcode prologue when called via &A874', align=Align.INLINE)
d.comment(0xA877, 'Shift ws_page right -- splits parameter byte into upper / lower nibbles', align=Align.INLINE)
d.comment(0xA87A, 'LDA #&A9 -- 2-byte BIT-trick filler (skipped when entered at &A87E)', align=Align.INLINE)
d.comment(0xA87C, 'LDA #&A9 -- 2-byte BIT-trick filler', align=Align.INLINE)
d.comment(0xA87E, 'Load template source pointer', align=Align.INLINE)
d.comment(0xA886, 'Equal: take save_txcb_and_convert path', align=Align.INLINE)
d.comment(0xA88A, 'Equal: take save_txcb_done path', align=Align.INLINE)
d.comment(0xA8C6, 'Push current A', align=Align.INLINE)
d.comment(0xA8CF, 'Pop saved value', align=Align.INLINE)
d.comment(0xA8D1, 'Divide by 4', align=Align.INLINE)
d.comment(0xA8D2, '(continued)', align=Align.INLINE)
d.comment(0xA8D4, 'Add &51 (offset base)', align=Align.INLINE)
d.comment(0xA8E6, 'Return', align=Align.INLINE)
d.comment(0xA8E7, 'Convert TXCB date/time bytes to BCD', align=Align.INLINE)
d.comment(0xA8EA, 'Y=7: copy 8 bytes (Y=7 down to 0)', align=Align.INLINE)
d.comment(0xA8EC, 'Load BCD byte from TXCB area (hazel_txcb_lib + Y)', align=Align.INLINE)
d.comment(0xA8EF, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA8F1, 'Decrement Y (advance backwards)', align=Align.INLINE)
d.comment(0xA8F2, 'Loop until Y wraps', align=Align.INLINE)
d.comment(0xA8F4, 'A=2: PB[0] parameter for OSWORD &0E (seconds-since-midnight format)', align=Align.INLINE)
d.comment(0xA8F6, 'Store parameter at PB[0]', align=Align.INLINE)
d.comment(0xA8F8, 'A=&0E: OSWORD &0E (read CMOS RTC)', align=Align.INLINE)
d.comment(0xA8FA, 'X = PB pointer low', align=Align.INLINE)
d.comment(0xA8FC, 'Y = PB pointer high (via table_idx scratch)', align=Align.INLINE)
d.comment(0xAAE5, 'A=0: invalid-handle marker', align=Align.INLINE)
d.comment(0xAB01, 'Save Y for processing', align=Align.INLINE)
d.comment(0xAB02, 'Push Y', align=Align.INLINE)
d.comment(0xAB08, 'Pop saved Y', align=Align.INLINE)
d.comment(0xAB13, 'Compare with 4', align=Align.INLINE)
d.comment(0xAB18, 'Return', align=Align.INLINE)
d.comment(0xAB1D, 'Save current Y', align=Align.INLINE)
d.comment(0xAB1F, 'Y=8 (handle-bit shift index)', align=Align.INLINE)
d.comment(0xAB29, 'Set bits 3 and 5', align=Align.INLINE)
d.comment(0xAB31, 'Push for save/restore', align=Align.INLINE)
d.comment(0xAB37, 'Pop saved value', align=Align.INLINE)
d.comment(0xACB6, 'Return', align=Align.INLINE)
d.comment(0xACB8, 'Y=1: workspace offset', align=Align.INLINE)
d.comment(0xACD6, 'Y=&7D: workspace pointer offset', align=Align.INLINE)
d.comment(0xACDE, 'Set carry', align=Align.INLINE)
d.comment(0xACE5, 'Loop while X != 0', align=Align.INLINE)
d.comment(0xACEA, 'Loop while not CR', align=Align.INLINE)
d.comment(0xACF0, 'Y=&7B: end-byte offset', align=Align.INLINE)
d.comment(0xACF4, 'Add 3 (end-of-buffer adjust)', align=Align.INLINE)
d.comment(0xA504, 'A=2: open-input mode for OSFIND', align=Align.INLINE)
d.comment(0xA509, 'Y=&12: cmd code for *RUN', align=Align.INLINE)
d.comment(0xA50B, 'Send the request and wait for reply', align=Align.INLINE)
d.comment(0xA50E, 'Read reply status from TX[5]', align=Align.INLINE)
d.comment(0xA511, 'Compare with 1 (not-found)', align=Align.INLINE)
d.comment(0xA51F, 'Decrement X (post-find adjustment)', align=Align.INLINE)
d.comment(0xA525, 'X=1: target offset for the *RUN-channel command', align=Align.INLINE)
d.comment(0xA527, 'Store X to hazel_txcb_data (cmd byte)', align=Align.INLINE)
d.comment(0xA52A, 'Store X to hazel_txcb_flag (cmd flag)', align=Align.INLINE)
d.comment(0xA52E, 'Copy filename arg into TX buffer', align=Align.INLINE)
d.comment(0xA54A, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0xA550, 'X=&FF -- start scan from end', align=Align.INLINE)
d.comment(0xA556, 'Compare with CR (terminator)', align=Align.INLINE)
d.comment(0xA560, 'Decrement scan index', align=Align.INLINE)
d.comment(0xA56B, 'Decrement scan index', align=Align.INLINE)
d.comment(0xA571, "Mark byte as 'argument'", align=Align.INLINE)
d.comment(0xA578, 'X=&FF -- restart scan from end', align=Align.INLINE)
d.comment(0xA588, "Mark caller's flags", align=Align.INLINE)
d.comment(0xAC25, 'Push X (saved across delay)', align=Align.INLINE)
d.comment(0xAC2C, 'Y=&18: status-byte offset', align=Align.INLINE)
d.comment(0xAC3C, 'Result byte to Y', align=Align.INLINE)
d.comment(0xAC41, 'Invert (presence -> absence)', align=Align.INLINE)
d.comment(0xAC46, 'Return', align=Align.INLINE)
d.comment(0xB3E6, 'Save Y at ws_ptr_hi', align=Align.INLINE)
d.comment(0xB3F2, 'Advance Y past padding', align=Align.INLINE)
d.comment(0xB3F4, 'Loop while Y wraps', align=Align.INLINE)
d.comment(0xB3F9, 'Restore Y from ws_ptr_hi', align=Align.INLINE)
d.comment(0xB400, 'X=6: scan up to 6 PS slots', align=Align.INLINE)
d.comment(0xB40F, 'C set: end of slots', align=Align.INLINE)
d.comment(0xB429, 'Pop saved slot index', align=Align.INLINE)
d.comment(0xB42C, 'Push it back (for retry)', align=Align.INLINE)
d.comment(0xB432, 'Advance Y by 4 (next slot)', align=Align.INLINE)
d.comment(0xB435, 'Read ws byte at (nfs_workspace)+Y', align=Align.INLINE)
d.comment(0xB437, 'Save as work_ae lo', align=Align.INLINE)
d.comment(0xB439, 'Read indirect via (work_ae,X)', align=Align.INLINE)
d.comment(0xB43B, 'Z set: zero -> read station addr', align=Align.INLINE)
d.comment(0xB43D, 'Compare with 3', align=Align.INLINE)
d.comment(0xB43F, 'Other than 3: skip slot mark', align=Align.INLINE)
d.comment(0xB441, 'Back up to network byte', align=Align.INLINE)
d.comment(0xB442, 'Read network byte', align=Align.INLINE)
d.comment(0xB444, 'Save as fs_work_6', align=Align.INLINE)
d.comment(0xB446, 'Back up to station byte', align=Align.INLINE)
d.comment(0xB447, 'Read station byte', align=Align.INLINE)
d.comment(0xB449, 'Save as fs_work_5', align=Align.INLINE)
d.comment(0xB44B, 'Y=&20: PS marker offset', align=Align.INLINE)
d.comment(0xB44D, 'Store station to (net_rx_ptr)+&20', align=Align.INLINE)
d.comment(0xB44F, 'Pop saved slot index', align=Align.INLINE)
d.comment(0xB451, "A=&3F: 'processed' marker", align=Align.INLINE)
d.comment(0xB453, 'Mark slot as processed', align=Align.INLINE)
d.comment(0xB457, "Print 'Printer server is ' fragment", align=Align.INLINE)
d.comment(0xB45A, 'Y=&20: marker offset', align=Align.INLINE)
d.comment(0xB45C, 'Read marker byte', align=Align.INLINE)
d.comment(0xB45E, "Non-zero: print 'now <stn>'", align=Align.INLINE)
d.comment(0xB460, "Print 'still ' fragment", align=Align.INLINE)
d.comment(0xB469, 'Bit-7 terminator (next opcode)', align=Align.INLINE)
d.comment(0xB46C, "Print 'now ' fragment", align=Align.INLINE)
d.comment(0xB473, 'Bit-7 terminator', align=Align.INLINE)
d.comment(0xB474, 'Print station number and newline', align=Align.INLINE)
d.comment(0xB188, 'Push for stack-based saves', align=Align.INLINE)
d.comment(0xB1B7, 'Bit 7 of A set (negative): print directory header', align=Align.INLINE)
d.comment(0xB1B9, 'Print char (no spool)', align=Align.INLINE)
d.comment(0xB1BC, 'Advance Y', align=Align.INLINE)
d.comment(0xB1BD, 'Loop until Y wraps', align=Align.INLINE)
d.comment(0xB1BF, "Print ')\\rDir. ' header for the directory listing", align=Align.INLINE)
d.comment(0xB1C9, 'X=&11: filename offset in TX buffer', align=Align.INLINE)
d.comment(0xB1CB, 'Print 10-char filename', align=Align.INLINE)
d.comment(0xB1CE, "Print inline 'attr-bits' fragment", align=Align.INLINE)
d.comment(0xB1DB, 'X=&1B: extension offset in TX buffer', align=Align.INLINE)
d.comment(0xB1DD, 'Print 10-char extension', align=Align.INLINE)
d.comment(0xB1E0, 'Print newline', align=Align.INLINE)
d.comment(0xB1E3, 'Pop saved counter', align=Align.INLINE)
d.comment(0xB1E4, 'Store as fs_lib_flags', align=Align.INLINE)
d.comment(0xB1E7, 'Save Y as hazel_txcb_flag (next-entry index)', align=Align.INLINE)
d.comment(0xB1EA, 'Save Y as fs_work_4', align=Align.INLINE)
d.comment(0xB1EC, 'Load fs_work_5 (page count)', align=Align.INLINE)
d.comment(0xB1EE, 'Store at hazel_txcb_count', align=Align.INLINE)
d.comment(0xB1F1, 'Load fs_work_7', align=Align.INLINE)
d.comment(0xB1F3, 'Store at hazel_txcb_data', align=Align.INLINE)
d.comment(0xB1F6, 'X=3: TX[3] is start of arg buffer', align=Align.INLINE)
d.comment(0xB1F8, 'Copy filename arg', align=Align.INLINE)
d.comment(0xB1FB, 'Y=3: cmd code 3 (catalog)', align=Align.INLINE)
d.comment(0xB1FD, 'Send TX request', align=Align.INLINE)
d.comment(0xB200, 'X advances entry counter', align=Align.INLINE)
d.comment(0xB201, 'Read reply status', align=Align.INLINE)
d.comment(0xB204, 'Z: empty reply -> exit cat', align=Align.INLINE)
d.comment(0xB206, 'Push reply status', align=Align.INLINE)
d.comment(0xB207, 'Advance Y', align=Align.INLINE)
d.comment(0xB208, 'Read entry byte from hazel_txcb_data+Y', align=Align.INLINE)
d.comment(0xB20B, 'Bit 7 clear: keep scanning', align=Align.INLINE)
d.comment(0xB20D, 'Store with high-bit clear at hazel_txcb_lib+Y', align=Align.INLINE)
d.comment(0xB210, 'Print column separator', align=Align.INLINE)
d.comment(0xB213, 'Pop saved status', align=Align.INLINE)
d.comment(0xB214, 'Clear carry for the ADC below', align=Align.INLINE)
d.comment(0xB215, 'Add fs_work_4 (page accumulator)', align=Align.INLINE)
d.comment(0xB217, 'New index', align=Align.INLINE)
d.comment(0xB218, 'Non-zero: continue paging', align=Align.INLINE)
d.comment(0xA70B, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0xA70D, 'Read CMOS &11 via osbyte_a1', align=Align.INLINE)
d.comment(0xA710, 'Result to A', align=Align.INLINE)
d.comment(0xA711, 'Mask bit 1 (auto-CLI flag)', align=Align.INLINE)
d.comment(0xA713, 'Bit clear: skip auto-CLI', align=Align.INLINE)
d.comment(0xA715, 'X = lo of fsreply_2_skip_handles (boot-cmd string ptr)', align=Align.INLINE)
d.comment(0xA717, 'Y = hi of fsreply_2_skip_handles', align=Align.INLINE)
d.comment(0xA719, 'OSCLI to execute boot command', align=Align.INLINE)
d.comment(0xA71C, 'Pop saved A', align=Align.INLINE)
d.comment(0xA71D, 'Compare with 2', align=Align.INLINE)
d.comment(0xA71F, 'Below: skip making FS permanent', align=Align.INLINE)
d.comment(0xA721, 'OSBYTE &6D: make filing system permanent', align=Align.INLINE)
d.comment(0xA75F, 'Read hazel_fs_flags (boot-state flag)', align=Align.INLINE)
d.comment(0xA762, 'Z: take boot_load_cmd path', align=Align.INLINE)
d.comment(0x8B5A, 'Read osword_pb_ptr_hi', align=Align.INLINE)
d.comment(0x8B5C, 'Push it', align=Align.INLINE)
d.comment(0x8B5D, 'Read osword_pb_ptr lo', align=Align.INLINE)
d.comment(0x8B5F, 'Push it', align=Align.INLINE)
d.comment(0x8BAE, 'Set bit 0 of fs_flags (= NFS active)', align=Align.INLINE)
d.comment(0x8BB1, 'Issue Master service call &0F (vector update)', align=Align.INLINE)
d.comment(0x8BB4, 'Pop saved osword_pb_ptr lo', align=Align.INLINE)
d.comment(0x8BB5, 'Restore osword_pb_ptr lo', align=Align.INLINE)
d.comment(0x8BB7, 'Pop saved osword_pb_ptr hi', align=Align.INLINE)
d.comment(0x8BB8, 'Restore osword_pb_ptr hi', align=Align.INLINE)
d.comment(0x8BBA, 'Return', align=Align.INLINE)
d.comment(0x926B, 'Z clear: continue with this char', align=Align.INLINE)
d.comment(0x926D, 'Z set (CR): increment fs_crflag', align=Align.INLINE)
d.comment(0x9273, 'Read fs_error_ptr (saved across OSASCI)', align=Align.INLINE)
d.comment(0x9275, 'Push it', align=Align.INLINE)
d.comment(0x9276, 'Read fs_crflag', align=Align.INLINE)
d.comment(0x9278, 'Push it', align=Align.INLINE)
d.comment(0x927E, 'Pop saved fs_crflag', align=Align.INLINE)
d.comment(0x927F, 'Restore fs_crflag', align=Align.INLINE)
d.comment(0x9281, 'Pop saved fs_error_ptr', align=Align.INLINE)
d.comment(0x9282, 'Restore fs_error_ptr', align=Align.INLINE)
d.comment(0x9284, 'Loop back', align=Align.INLINE)
d.comment(0xA9E9, 'Step back to previous byte', align=Align.INLINE)
d.comment(0xAA03, 'Entry index to A', align=Align.INLINE)
d.comment(0xAA04, 'Mask bit 5', align=Align.INLINE)
d.comment(0xAA0F, 'Clear carry', align=Align.INLINE)
d.comment(0xAA5E, 'A = Y for store', align=Align.INLINE)
d.comment(0xAA62, 'Decrement entry counter', align=Align.INLINE)
d.comment(0xAA59, 'A=8: fs_flags bit 3 (FS-error pending)', align=Align.INLINE)
d.comment(0xAA5B, 'Clear FS-error-pending flag', align=Align.INLINE)
d.comment(0xAA5F, 'Store updated status into hazel_fcb_status[X]', align=Align.INLINE)
d.comment(0xAA63, 'Loop while X >= 0 (scan all FCBs)', align=Align.INLINE)
d.comment(0xAA65, 'A=&0E: status flag value', align=Align.INLINE)
d.comment(0xAA67, 'Test fs_flags bits 1..3', align=Align.INLINE)
d.comment(0xAA6A, 'Non-zero: skip the FS-active set', align=Align.INLINE)
d.comment(0xAA6C, 'A=&40: FS-active flag bit', align=Align.INLINE)
d.comment(0xAA71, 'Return -- FCB-status update complete', align=Align.INLINE)
d.comment(0xAA6E, 'Set FS-active flag (bit 6 of fs_flags)', align=Align.INLINE)
d.comment(0xA45C, 'Push for save/restore', align=Align.INLINE)
d.comment(0xA481, '(continued)', align=Align.INLINE)
d.comment(0xA482, '(continued)', align=Align.INLINE)
d.comment(0xA486, 'Push for stack-based comparison', align=Align.INLINE)
d.comment(0xA494, 'A = matched offset, save in Y', align=Align.INLINE)
d.comment(0xA497, 'Dispatch helper (sep_table_data path)', align=Align.INLINE)
d.comment(0xA49A, 'Check separator flag (zp_0026)', align=Align.INLINE)
d.comment(0xA49E, 'Effective unconditional jump', align=Align.INLINE)
d.comment(0xA0E1, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0xA0E7, 'Read CMOS &11 result to A', align=Align.INLINE)
d.comment(0xA0EC, 'Push CMOS value', align=Align.INLINE)
d.comment(0xA0F0, 'Value to X', align=Align.INLINE)
d.comment(0xA0F2, 'Shift CMOS bits', align=Align.INLINE)
d.comment(0xA0F8, 'Pop saved value', align=Align.INLINE)
d.comment(0xA919, 'Read net_rx_ptr_hi', align=Align.INLINE)
d.comment(0xA942, 'Divide by 2', align=Align.INLINE)
d.comment(0xA944, 'Index to X', align=Align.INLINE)
d.comment(0xA94D, 'Step to next slot', align=Align.INLINE)
d.comment(0xA951, 'Found slot index', align=Align.INLINE)
d.comment(0xA95B, 'Back up scan', align=Align.INLINE)
d.comment(0xA960, 'Y=1: result-byte offset', align=Align.INLINE)
d.comment(0xA96C, 'For the ADC chain', align=Align.INLINE)
d.comment(0xAD13, 'Restore flags', align=Align.INLINE)
d.comment(0xAD14, 'Return', align=Align.INLINE)
d.comment(0x8EF1, 'Push for save', align=Align.INLINE)
d.comment(0x8EFC, 'Pop -- save Y temporarily', align=Align.INLINE)
d.comment(0x8F01, 'Push restored value', align=Align.INLINE)
d.comment(0x8F02, 'Mask bit 7 (workspace flag)', align=Align.INLINE)
d.comment(0x8F0A, 'Read &FE28 (Master ROMSEL shadow)', align=Align.INLINE)
d.comment(0x8F0D, 'Pop saved Y', align=Align.INLINE)
d.comment(0x8F0E, 'Increment for next page', align=Align.INLINE)
d.comment(0x8F0F, 'Return', align=Align.INLINE)
d.comment(0xB2F5, 'Non-zero: take col_sep_print_char tail', align=Align.INLINE)
d.comment(0xB2F7, 'A=&0D: CR character', align=Align.INLINE)
d.comment(0xB2F9, 'Print CR (no spool)', align=Align.INLINE)
d.comment(0xB2FC, 'Next entry', align=Align.INLINE)
d.comment(0xB2FD, 'Loop until X wraps', align=Align.INLINE)
d.comment(0x8D24, 'Y = ws_page (workspace high page)', align=Align.INLINE)
d.comment(0x8D87, 'Save caller Y', align=Align.INLINE)
d.comment(0x8D88, 'Read fs_last_byte_flag (work_bd)', align=Align.INLINE)
d.comment(0x8D8A, 'Read fs_options (work_bb)', align=Align.INLINE)
d.comment(0x8D8C, 'Read fs_block_offset (work_bc)', align=Align.INLINE)
d.comment(0x8D8E, 'Push fs_last_byte_flag for restore on return', align=Align.INLINE)
d.comment(0xAB43, 'A = caller X', align=Align.INLINE)
d.comment(0xAB45, 'X=&0F: scan all 16 FCB slots', align=Align.INLINE)
d.comment(0xAB4B, 'Shift bit into carry for test', align=Align.INLINE)
d.comment(0xAB62, 'Decrement FCB index', align=Align.INLINE)
d.comment(0xAB67, 'Return', align=Align.INLINE)
d.comment(0x8B38, 'Return -- last instruction of cmd_net_fs body', align=Align.INLINE)
d.comment(0x8B39, 'A=&20: ADLC IRQ-status mask (CR2 bit 5)', align=Align.INLINE)
d.comment(0x8B3B, 'Read ADLC CR2/SR2 (&FEA1)', align=Align.INLINE)
d.comment(0x8B3E, 'Z set (no carrier): proceed to FS-select', align=Align.INLINE)
d.comment(0x8B40, "A=3: 'ROM has no NFS' error code", align=Align.INLINE)
d.comment(0x8B42, 'Raise via build_simple_error (never returns)', align=Align.INLINE)
d.comment(0x9612, 'A=&A2: write CMOS RAM byte via OSBYTE', align=Align.INLINE)
d.comment(0x9617, 'BRA -91 -> bra_target_svc_return', align=Align.INLINE)
d.comment(0x9619, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0x961B, 'Read CMOS &11 via osbyte_a1', align=Align.INLINE)
d.comment(0x961E, 'A = current CMOS &11 value', align=Align.INLINE)
d.comment(0x961F, 'Set bit 0 in A', align=Align.INLINE)
d.comment(0x9621, 'BRA osbyte_a2_value_tya: shared write-back tail', align=Align.INLINE)
d.comment(0x9623, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0x9625, 'Read CMOS &11 via osbyte_a1', align=Align.INLINE)
d.comment(0x9628, 'A = current CMOS &11 value', align=Align.INLINE)
d.comment(0x9629, 'Clear bit 0 in A', align=Align.INLINE)
d.comment(0x962B, 'New CMOS value to Y', align=Align.INLINE)
d.comment(0x962C, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0x962E, 'BRA osbyte_a2: write CMOS &11 = Y', align=Align.INLINE)
d.comment(0x9630, 'Read first command-line char', align=Align.INLINE)
d.comment(0x9632, 'Is it CR (no argument)?', align=Align.INLINE)
d.comment(0x9634, 'Non-CR: parse the argument at help_dispatch_setup', align=Align.INLINE)
d.comment(0x9636, "Print 'FS       ' header", align=Align.INLINE)
d.comment(0x9639, 'Print FS network.station from CMOS &02/&01', align=Align.INLINE)
d.comment(0x963C, "Print 'PS       ' header", align=Align.INLINE)
d.comment(0x963F, 'Print PS network.station from CMOS &04/&03', align=Align.INLINE)
d.comment(0x9642, 'X=&11: CMOS RAM byte index', align=Align.INLINE)
d.comment(0x9644, 'Read CMOS &11 (FS state)', align=Align.INLINE)
d.comment(0x9647, 'A = CMOS &11', align=Align.INLINE)
d.comment(0x9648, 'Mask bit 0 (FS-active flag)', align=Align.INLINE)
d.comment(0x964A, "Bit set: skip 'No ' prefix", align=Align.INLINE)
d.comment(0x964C, "Print 'No ' prefix via inline", align=Align.INLINE)
d.comment(0x9652, 'Bit-7 terminator + resume', align=Align.INLINE)
d.comment(0x9653, "Print 'Space        ' or similar via inline", align=Align.INLINE)
d.comment(0x965C, 'Bit-7 terminator + resume opcode', align=Align.INLINE)
d.comment(0x965F, 'X=4: CMOS RAM byte 4 (network number)', align=Align.INLINE)
d.comment(0x9661, 'Read CMOS &04 via osbyte_a1', align=Align.INLINE)
d.comment(0x9664, 'A = CMOS &04 value', align=Align.INLINE)
d.comment(0x9665, 'Print as decimal (no leading zeros)', align=Align.INLINE)
d.comment(0x9668, "Print '.' separator via inline", align=Align.INLINE)
d.comment(0x966C, 'X=3: CMOS &03 (PS station)', align=Align.INLINE)
d.comment(0x966E, 'BRA print_cmos_decimal_nl: shared print-and-trail', align=Align.INLINE)
d.comment(0x9670, 'X=2: CMOS &02 (FS network)', align=Align.INLINE)
d.comment(0x9672, 'Read CMOS &02 via osbyte_a1', align=Align.INLINE)
d.comment(0x9675, 'A = CMOS &02', align=Align.INLINE)
d.comment(0x9676, 'Print as decimal', align=Align.INLINE)
d.comment(0x9679, "Print '.' separator via inline", align=Align.INLINE)
d.comment(0x967D, 'X=1: CMOS &01 (port)', align=Align.INLINE)
d.comment(0x967F, 'Read CMOS X via osbyte_a1', align=Align.INLINE)
d.comment(0x9682, 'A = CMOS value', align=Align.INLINE)
d.comment(0x9683, 'Print as decimal', align=Align.INLINE)
d.comment(0x9689, 'JMP svc_return_unclaimed (release service call)', align=Align.INLINE)
d.comment(0x968C, 'X=&BD: setup index for the dispatch chain', align=Align.INLINE)
d.comment(0x968E, 'JMP svc4_dispatch_lookup -- shared parser dispatch', align=Align.INLINE)
d.comment(0x969B, 'Copy os_text_ptr lo to work_ae', align=Align.INLINE)
d.comment(0x969D, 'Store -> work_ae', align=Align.INLINE)
d.comment(0x969F, 'Copy os_text_ptr hi', align=Align.INLINE)
d.comment(0x96A1, 'Store -> addr_work', align=Align.INLINE)
d.comment(0x96A3, 'Restore caller Y', align=Align.INLINE)
d.comment(0x96A4, 'Save Y again (preserve across loop)', align=Align.INLINE)
d.comment(0x96A5, 'X=0: pattern offset starts at 0', align=Align.INLINE)
d.comment(0x96A7, 'Read text byte at (work_ae)+Y', align=Align.INLINE)
d.comment(0x96AC, 'Mask bit 5 -- case-insensitive comparison', align=Align.INLINE)
d.comment(0x96AE, 'Equal: continue checking pattern', align=Align.INLINE)
d.comment(0x96B1, 'Return (no match)', align=Align.INLINE)
d.comment(0x96B2, 'Advance text index', align=Align.INLINE)
d.comment(0x96B3, 'Advance pattern index', align=Align.INLINE)
d.comment(0x96B4, 'Done all 3 chars?', align=Align.INLINE)
d.comment(0x96B6, 'No: continue', align=Align.INLINE)
d.comment(0x96B8, 'Match: save Y', align=Align.INLINE)
d.comment(0x96B9, 'Ensure NFS is selected (auto-select if needed)', align=Align.INLINE)
d.comment(0x96BD, 'Advance Y to next char', align=Align.INLINE)
d.comment(0x96BE, 'Read text byte at (work_ae)+Y', align=Align.INLINE)
d.comment(0x96C0, 'Is it CR (end-of-line)?', align=Align.INLINE)
d.comment(0x96C2, 'Yes: nothing to load -> return', align=Align.INLINE)
d.comment(0x96C4, 'Is it space?', align=Align.INLINE)
d.comment(0x96C6, 'No: continue scanning past non-space', align=Align.INLINE)
d.comment(0x96C8, 'Skip space char', align=Align.INLINE)
d.comment(0x96C9, 'Read next byte', align=Align.INLINE)
d.comment(0x96CB, 'Is it space?', align=Align.INLINE)
d.comment(0x96CD, 'Yes: keep skipping spaces', align=Align.INLINE)
d.comment(0x96CF, 'Is it CR?', align=Align.INLINE)
d.comment(0x96D1, 'Yes: nothing past spaces -> return', align=Align.INLINE)
d.comment(0x96D3, 'Save Y as hazel_txcb_data (cmd buffer ptr)', align=Align.INLINE)
d.comment(0x96D6, 'Save Y as hazel_txcb_flag (cmd flag)', align=Align.INLINE)
d.comment(0x96D9, 'X=1: index for template walk', align=Align.INLINE)
d.comment(0x96DB, 'Advance template index', align=Align.INLINE)
d.comment(0x96DC, 'Read template byte from help_topic_template+X', align=Align.INLINE)
d.comment(0x96DF, 'Store at hazel_txcb_data+X', align=Align.INLINE)
d.comment(0x96E2, "Compare with '.' (template terminator)", align=Align.INLINE)
d.comment(0x96E4, "Not '.': continue copying template", align=Align.INLINE)
d.comment(0x96E6, 'Save text-buffer index', align=Align.INLINE)
d.comment(0x96E7, 'Advance dest index', align=Align.INLINE)
d.comment(0x96E8, 'Read topic char at (work_ae),Y', align=Align.INLINE)
d.comment(0x96EA, 'Advance source', align=Align.INLINE)
d.comment(0x96EB, 'Store at hazel_txcb_data+X', align=Align.INLINE)
d.comment(0x96EE, 'CR? (end of name)', align=Align.INLINE)
d.comment(0x96F0, 'Yes: take start_help_file_load path (open file)', align=Align.INLINE)
d.comment(0x96F2, 'Space? (terminator)', align=Align.INLINE)
d.comment(0x96F4, 'No: continue copying', align=Align.INLINE)
d.comment(0x96F6, 'A=&0D: replace space with CR', align=Align.INLINE)
d.comment(0x96F8, 'BRA back to store the CR', align=Align.INLINE)
d.comment(0x96FA, 'Account for last char', align=Align.INLINE)
d.comment(0x96FB, 'Read fs_lib_flags (hazel_fs_lib_flags)', align=Align.INLINE)
d.comment(0x96FE, 'Preserve low bits, clear high bits', align=Align.INLINE)
d.comment(0x9700, 'Set bit 7 (load-pending flag)', align=Align.INLINE)
d.comment(0x9702, 'Store back to fs_lib_flags', align=Align.INLINE)
d.comment(0x9705, 'A=&40: load mode flag', align=Align.INLINE)
d.comment(0x9707, 'Store as fs_last_byte_flag', align=Align.INLINE)
d.comment(0x9709, 'Open the help-topic file', align=Align.INLINE)
d.comment(0x970D, 'Y=0: open failed -> return', align=Align.INLINE)
d.comment(0x9712, 'C clear: byte read OK -> print it', align=Align.INLINE)
d.comment(0x9714, 'A=0: OSFIND close mode', align=Align.INLINE)
d.comment(0x971C, 'BRA back to match_char_process (return)', align=Align.INLINE)
d.comment(0x9720, 'Bit 7 clear: not escaping, continue', align=Align.INLINE)
d.comment(0x9722, 'Escape: jump to error path escape_error_close', align=Align.INLINE)
d.comment(0x9725, 'Compare with CR', align=Align.INLINE)
d.comment(0x9727, 'Z: CR -- handle line-end (newline)', align=Align.INLINE)
d.comment(0x972C, 'BRA back to read next byte', align=Align.INLINE)
d.comment(0x972E, 'Save file handle', align=Align.INLINE)
d.comment(0x972F, 'A=&DA: OSBYTE &DA = read paged-mode flag', align=Align.INLINE)
d.comment(0x9731, 'Issue OSBYTE &DA (X=0)', align=Align.INLINE)
d.comment(0x9734, 'Restore handle', align=Align.INLINE)
d.comment(0x9735, 'Result to A', align=Align.INLINE)
d.comment(0x9736, 'Non-zero: paged mode pending -> handle Escape', align=Align.INLINE)
d.comment(0x973B, 'BRA back to read next byte', align=Align.INLINE)
d.comment(0xA99F, 'Read dispatch hi from osword_13_dispatch_hi+X', align=Align.INLINE)
d.comment(0xA9A2, 'Push hi for RTS dispatch', align=Align.INLINE)
d.comment(0xA9A3, 'Read dispatch lo from osword_13_dispatch_lo+X', align=Align.INLINE)
d.comment(0xA9A6, 'Push lo for RTS dispatch', align=Align.INLINE)
d.comment(0xA9A7, 'RTS -> dispatched OSWORD &13 sub-handler', align=Align.INLINE)
d.comment(0xAE71, 'Non-zero: nothing to print, return', align=Align.INLINE)
d.comment(0xAE74, 'Step counter back', align=Align.INLINE)
d.comment(0xAE77, 'Read MOS stack frame', align=Align.INLINE)
d.comment(0xAE85, 'C set: return path', align=Align.INLINE)
d.comment(0xAE8F, 'Print accumulated spool data', align=Align.INLINE)
d.comment(0xB01C, 'Save state byte', align=Align.INLINE)
d.comment(0xB02F, 'Save another byte', align=Align.INLINE)
d.comment(0xB03C, 'Restore inner saved', align=Align.INLINE)
d.comment(0xB052, 'Restore outer saved', align=Align.INLINE)
d.comment(0xB05C, 'Restore final saved', align=Align.INLINE)
d.comment(0xB3BC, 'Read fs_options[Y]', align=Align.INLINE)
d.comment(0xB3C6, 'C clear: save ptr and continue', align=Align.INLINE)
d.comment(0xB3C8, 'A = current Y', align=Align.INLINE)
d.comment(0x8DA0, 'Clear hazel_fs_pending_state (connection-attempt flag)', align=Align.INLINE)
d.comment(0x8DA5, 'Pop and discard saved fs_last_byte_flag', align=Align.INLINE)
d.comment(0x8DA6, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0xAEB8, 'Y=8: buf_start_lo TXCB offset', align=Align.INLINE)
d.comment(0xAEBA, 'Load current spool-buffer index', align=Align.INLINE)
d.comment(0xAEBD, 'Store at workspace+8 (buf_start_lo)', align=Align.INLINE)
d.comment(0xAEBF, 'Load RX page (= net_rx_ptr_hi)', align=Align.INLINE)
d.comment(0xAEC2, 'Store at workspace+9 (buf_start_hi)', align=Align.INLINE)
d.comment(0xAEC4, 'Y=5: alt buf_start_hi offset', align=Align.INLINE)
d.comment(0xAEC6, 'Store at workspace+5 (also buf-start hi)', align=Align.INLINE)
d.comment(0xAEC8, 'Y=&0B: TXCB offset for following copy', align=Align.INLINE)
d.comment(0xAECA, 'X=&26: template offset for vclr region', align=Align.INLINE)
d.comment(0xAECC, 'Copy 12-byte ws-template region (V-clear)', align=Align.INLINE)
d.comment(0xAECF, 'Step back to offset &0A', align=Align.INLINE)
d.comment(0xAED0, 'Read shadow ACR (ws_0d6a)', align=Align.INLINE)
d.comment(0xAED4, 'Shift bit 7 into C', align=Align.INLINE)
d.comment(0xAED6, 'Toggle bit 7', align=Align.INLINE)
d.comment(0xAED8, 'Store updated shadow back to ws_0d6a', align=Align.INLINE)
d.comment(0xAEDB, 'Shift bit 0 into bit 1', align=Align.INLINE)
d.comment(0xAEDC, 'Store at workspace+&0A', align=Align.INLINE)
d.comment(0xAEDE, 'Read vdu_status', align=Align.INLINE)
d.comment(0xAEE1, 'Clear bit 0 of vdu_status', align=Align.INLINE)
d.comment(0xAEE3, 'Store updated', align=Align.INLINE)
d.comment(0xAEE5, 'Y=&21: spool_buf_idx reset value', align=Align.INLINE)
d.comment(0xAEE7, 'Reset spool_buf_idx', align=Align.INLINE)
d.comment(0xAEEA, 'A=0', align=Align.INLINE)
d.comment(0xAEED, 'Y = workspace high page', align=Align.INLINE)
d.comment(0xAEEF, 'Re-enable IRQs (NMI window over)', align=Align.INLINE)
d.comment(0xAEF0, 'Send disconnect reply', align=Align.INLINE)
d.comment(0xAEF3, 'Restore vdu_status', align=Align.INLINE)
d.comment(0xAEF4, 'Restore vdu_status', align=Align.INLINE)
d.comment(0xAEF6, 'Return', align=Align.INLINE)
d.comment(0xAEF7, 'Read shadow ACR', align=Align.INLINE)
d.comment(0xAEFA, 'Shift bit 0 into C', align=Align.INLINE)
d.comment(0xAEFB, 'C clear: re-process spool data', align=Align.INLINE)
d.comment(0xAEFD, 'Read vdu_status', align=Align.INLINE)
d.comment(0xAF00, 'Clear bit 0 of vdu_status', align=Align.INLINE)
d.comment(0xAF02, 'Store updated', align=Align.INLINE)
d.comment(0xAF04, 'A=&14: TX command byte', align=Align.INLINE)
d.comment(0xAF06, 'Save TX command', align=Align.INLINE)
d.comment(0xAF07, 'X=&0B: tx_econet_txcb_template offset', align=Align.INLINE)
d.comment(0xAF09, 'Y=&2C: dest TXCB offset', align=Align.INLINE)
d.comment(0xAF0B, 'Read template byte at tx_econet_txcb_template+X', align=Align.INLINE)
d.comment(0xAF0E, 'Store at (net_rx_ptr)+Y', align=Align.INLINE)
d.comment(0xAF10, 'Decrement Y', align=Align.INLINE)
d.comment(0xAF11, 'Decrement X', align=Align.INLINE)
d.comment(0xAF12, 'Loop until X wraps below 0', align=Align.INLINE)
d.comment(0xAF14, 'Store X (= &FF) as need_release_tube', align=Align.INLINE)
d.comment(0xAF16, 'Y=2: workspace offset for source', align=Align.INLINE)
d.comment(0xAF18, 'Read (nfs_workspace)+2', align=Align.INLINE)
d.comment(0xAF1B, 'Y=3', align=Align.INLINE)
d.comment(0xAF1C, 'Read (nfs_workspace)+3', align=Align.INLINE)
d.comment(0xAF1E, 'Y=&24: dest offset in TXCB', align=Align.INLINE)
d.comment(0xAF20, 'Store at (net_rx_ptr)+Y', align=Align.INLINE)
d.comment(0xAF22, 'Y=&23', align=Align.INLINE)
d.comment(0xAF24, 'Store at (net_rx_ptr)+Y', align=Align.INLINE)
d.comment(0xAF26, 'X=&0B: rx_palette_txcb_template offset', align=Align.INLINE)
d.comment(0xAF28, 'Y=&0B: dest offset in workspace', align=Align.INLINE)
d.comment(0xAF2A, 'Read template byte at rx_palette_txcb_template+X', align=Align.INLINE)
d.comment(0xAF2D, 'Compare with &FD (skip-byte marker)', align=Align.INLINE)
d.comment(0xAF2F, 'Equal: skip this byte', align=Align.INLINE)
d.comment(0xAF31, 'Compare with &FC (page-ptr marker)', align=Align.INLINE)
d.comment(0xAF33, 'Not &FC: store as-is', align=Align.INLINE)
d.comment(0xAF35, '&FC: substitute net_rx_ptr_hi', align=Align.INLINE)
d.comment(0xAF37, 'Store at (nfs_workspace)+Y', align=Align.INLINE)
d.comment(0xAF39, 'Next dest', align=Align.INLINE)
d.comment(0xAF3A, 'Next source', align=Align.INLINE)
d.comment(0xAF3B, 'Loop until X wraps', align=Align.INLINE)
d.comment(0xAF3D, 'A=&21: TXCB control byte', align=Align.INLINE)
d.comment(0xAF3F, 'Store at net_tx_ptr lo', align=Align.INLINE)
d.comment(0xAF41, 'Read net_rx_ptr_hi', align=Align.INLINE)
d.comment(0xAF43, 'Store as net_tx_ptr hi', align=Align.INLINE)
d.comment(0xAF45, 'Set up the pass-through TX buffer', align=Align.INLINE)
d.comment(0xAF48, 'Send the TX packet', align=Align.INLINE)
d.comment(0xAF4B, 'A=0: clear net_tx_ptr lo', align=Align.INLINE)
d.comment(0xAF4D, 'Store -> net_tx_ptr lo', align=Align.INLINE)
d.comment(0xAF4F, 'Read nfs_workspace_hi', align=Align.INLINE)
d.comment(0xAF51, 'Store -> net_tx_ptr hi', align=Align.INLINE)
d.comment(0xAF53, 'Wait for TX ack', align=Align.INLINE)
d.comment(0xAF56, 'Y=&2D: spool result-byte offset', align=Align.INLINE)
d.comment(0xAF58, 'Read result via (net_rx_ptr)+Y', align=Align.INLINE)
d.comment(0xAF5A, 'Z: success path', align=Align.INLINE)
d.comment(0xAF5C, 'Compare with 3 (retry threshold)', align=Align.INLINE)
d.comment(0xAF5E, 'Other: take retry path', align=Align.INLINE)
d.comment(0xAF60, 'Discard saved TX cmd', align=Align.INLINE)
d.comment(0xAF61, 'Restore vdu_status', align=Align.INLINE)
d.comment(0xAF62, 'Restore vdu_status', align=Align.INLINE)
d.comment(0xAF64, 'A=0: success-return code', align=Align.INLINE)
d.comment(0xAF66, 'Append byte to RX buffer', align=Align.INLINE)
d.comment(0xAF69, 'Recurse: process_spool_data', align=Align.INLINE)
d.comment(0xAF6C, 'Read shadow ACR', align=Align.INLINE)
d.comment(0xAF6F, 'Mask high nibble', align=Align.INLINE)
d.comment(0xAF71, 'Store updated shadow', align=Align.INLINE)
d.comment(0xAF74, 'Return', align=Align.INLINE)
d.comment(0xAF75, 'Save retry counter', align=Align.INLINE)
d.comment(0xAF76, 'Pop saved TX cmd', align=Align.INLINE)
d.comment(0xAF77, 'Set carry', align=Align.INLINE)
d.comment(0xAF78, 'Decrement retry', align=Align.INLINE)
d.comment(0xAF7A, 'Non-zero: retry from start_spool_retry', align=Align.INLINE)
d.comment(0xAF7C, 'Check the saved retry counter', align=Align.INLINE)
d.comment(0xAF7E, 'Not 1: take printer_busy_msg path', align=Align.INLINE)
d.comment(0xAEA2, 'Equal: take fill path', align=Align.INLINE)
d.comment(0xAEAC, 'Stop: process_spool_data and return', align=Align.INLINE)
d.comment(0xAE9E, 'C clear: take check_spool_state path', align=Align.INLINE)
d.comment(0xAEA3, 'Save state byte', align=Align.INLINE)
d.comment(0xAEAD, 'A=3: spool-data result code', align=Align.INLINE)
d.comment(0xAEAF, 'Append result to RX buffer', align=Align.INLINE)
d.comment(0xAEB2, 'Process the accumulated spool data', align=Align.INLINE)
d.comment(0xAEB5, 'Reset spool buffer state', align=Align.INLINE)
d.comment(0xB01A, 'Read osword_flag (preserved across the dispatch)', align=Align.INLINE)
d.comment(0xB01D, 'A=&E9: workspace start lo for palette save', align=Align.INLINE)
d.comment(0xB01F, 'Store as nfs_workspace lo', align=Align.INLINE)
d.comment(0xB021, 'Y=0', align=Align.INLINE)
d.comment(0xB023, 'Reset osword_flag = 0', align=Align.INLINE)
d.comment(0xB025, 'Read vdu_screen_mode (MOS state byte)', align=Align.INLINE)
d.comment(0xB028, 'Store at (nfs_workspace)+0', align=Align.INLINE)
d.comment(0xB02A, 'Advance nfs_workspace lo', align=Align.INLINE)
d.comment(0xB02C, 'Read vdu_display_start_hi (next MOS byte)', align=Align.INLINE)
d.comment(0xB031, 'Store at (nfs_workspace)', align=Align.INLINE)
d.comment(0xB033, 'Read updated nfs_workspace lo', align=Align.INLINE)
d.comment(0xB035, 'Read nfs_workspace hi', align=Align.INLINE)
d.comment(0xB037, 'A=&0B: OSWORD &0B = read palette entry', align=Align.INLINE)
d.comment(0xB03D, 'Y=0', align=Align.INLINE)
d.comment(0xB03F, 'Store palette result at workspace', align=Align.INLINE)
d.comment(0xB042, 'Re-read palette result', align=Align.INLINE)
d.comment(0xB045, 'Read updated workspace lo', align=Align.INLINE)
d.comment(0xB047, 'Advance workspace', align=Align.INLINE)
d.comment(0xB049, 'Increment osword_flag (palette index)', align=Align.INLINE)
d.comment(0xB04C, 'Read updated osword_flag', align=Align.INLINE)
d.comment(0xB04E, 'Compare with &F9 (last palette entry)', align=Align.INLINE)
d.comment(0xB050, 'Not done: loop', align=Align.INLINE)
d.comment(0xB053, 'Reset osword_flag = 0 after palette loop', align=Align.INLINE)
d.comment(0xB055, 'Advance workspace', align=Align.INLINE)
d.comment(0xB057, 'Serialise the next palette entry', align=Align.INLINE)
d.comment(0xB05A, 'Advance workspace', align=Align.INLINE)
d.comment(0xB05D, 'Save osword_flag', align=Align.INLINE)
d.comment(0xB066, 'Read vdu_mode (current palette index)', align=Align.INLINE)
d.comment(0xB069, 'Mark as palette entry', align=Align.INLINE)
d.comment(0xB06B, 'Store at (nfs_workspace)+Y', align=Align.INLINE)
d.comment(0xB06D, 'Read vdu_mode', align=Align.INLINE)
d.comment(0xB070, 'Advance workspace', align=Align.INLINE)
d.comment(0xB072, 'A = current Y (= 0)', align=Align.INLINE)
d.comment(0xB073, 'Store 0 at (nfs_workspace)+Y', align=Align.INLINE)
d.comment(0xB075, 'Read lookup byte from read_osbyte_table+X', align=Align.INLINE)
d.comment(0xB078, 'X=0: indexed-indirect mode', align=Align.INLINE)
d.comment(0xB07A, 'Advance workspace', align=Align.INLINE)
d.comment(0xB07C, 'Store at (nfs_workspace,X)', align=Align.INLINE)
d.comment(0xB07E, 'Read OSBYTE result via x=0 helper', align=Align.INLINE)
d.comment(0xB083, 'Y = osword_flag (OSBYTE-table index)', align=Align.INLINE)
d.comment(0xB085, 'Increment osword_flag for next call', align=Align.INLINE)
d.comment(0xB087, 'Advance nfs_workspace', align=Align.INLINE)
d.comment(0xB089, 'Load OSBYTE number from read_osbyte_return+Y', align=Align.INLINE)
d.comment(0xB08C, 'Y=&FF -- OSBYTE arg (read mode)', align=Align.INLINE)
d.comment(0xB08E, 'Issue OSBYTE', align=Align.INLINE)
d.comment(0xB091, 'Result to A', align=Align.INLINE)
d.comment(0xB092, 'X=0: indexed-indirect mode', align=Align.INLINE)
d.comment(0xB094, 'Store at (nfs_workspace,X)', align=Align.INLINE)
d.comment(0xB096, 'Return', align=Align.INLINE)
d.comment(0xB0A0, 'JMP (cdir_unused_dispatch_table,X) -- never executed; see cmd_cdir', align=Align.INLINE)
d.comment(0xA83B, 'BRA osword_store_svc_state -- skip past 22-byte caller-cleanup frame', align=Align.INLINE)
d.comment(0xA84A, 'Read svc_state[Y] (frame slot)', align=Align.INLINE)
d.comment(0xA854, 'Next slot', align=Align.INLINE)
d.comment(0xA855, 'Loop until Y wraps', align=Align.INLINE)
d.comment(0x90C7, "Print 'Station ' inline string", align=Align.INLINE)
d.comment(0x90D9, 'Y=1: PB station-byte offset', align=Align.INLINE)
d.comment(0x90DB, 'Read RX[1] = station number', align=Align.INLINE)
d.comment(0x90DD, 'Print as decimal (no leading zeros)', align=Align.INLINE)
d.comment(0x8BC8, 'Save X (cmd-table offset)', align=Align.INLINE)
d.comment(0x8BCA, 'Print the version-banner header', align=Align.INLINE)
d.comment(0x8BC9, 'Save Y (text-pointer offset)', align=Align.INLINE)
d.comment(0xB2DB, 'X=0: scan from start of TX entry', align=Align.INLINE)
d.comment(0xB2DD, 'Read entry byte at hazel_txcb_data+X', align=Align.INLINE)
d.comment(0xB2E0, 'Bit 7 set: end-of-entries -> return', align=Align.INLINE)
d.comment(0xB2E2, 'Non-printable: take CR-newline path at col_sep_print_cr', align=Align.INLINE)
d.comment(0xAF80, "A=&A6: 'Printer busy' error code", align=Align.INLINE)
d.comment(0xAF82, 'Raise via error_inline_log (never returns)', align=Align.INLINE)
d.comment(0xAF92, "A=&A7: 'Printer jammed' error code", align=Align.INLINE)
d.comment(0xAF94, 'Raise via error_inline_log (never returns)', align=Align.INLINE)
d.comment(0xA901, 'Save caller flags (D may be in any state)', align=Align.INLINE)
d.comment(0xA902, 'Save A across decimal-mode arithmetic', align=Align.INLINE)
d.comment(0xA905, 'Enter decimal mode', align=Align.INLINE)
d.comment(0xA90E, 'Restore caller flags (incl. D)', align=Align.INLINE)
d.comment(0xAE94, 'Y = spool_buf_idx', align=Align.INLINE)
d.comment(0xAE97, 'Store A at (net_rx_ptr)+Y', align=Align.INLINE)
d.comment(0xAE99, 'Advance spool_buf_idx', align=Align.INLINE)
d.comment(0xAE9C, 'Return', align=Align.INLINE)
d.comment(0x9895, 'A=&7E: OSBYTE &7E = acknowledge Escape', align=Align.INLINE)
d.comment(0x989A, "A=6: error class for 'Escape'", align=Align.INLINE)
d.comment(0x989C, 'JMP classify_reply_error (never returns)', align=Align.INLINE)
d.comment(0x9262, 'Store as fs_error_ptr (return-addr saved)', align=Align.INLINE)
d.comment(0x9265, 'Store as fs_crflag (entry flag)', align=Align.INLINE)
d.comment(0x9267, 'Y=0: start scanning at offset 0', align=Align.INLINE)
d.comment(0x924E, 'LSR / LSR / LSR -- shift hi nibble down to lo', align=Align.INLINE)
d.comment(0x924F, '(continued)', align=Align.INLINE)
d.comment(0x9250, '(continued)', align=Align.INLINE)
d.comment(0xABBE, 'Advance Y', align=Align.INLINE)
d.comment(0xABC7, 'Non-zero: take return path', align=Align.INLINE)
d.comment(0xABD0, 'Return', align=Align.INLINE)
d.comment(0xA4DC, 'Test fs_flags bit 6', align=Align.INLINE)
d.comment(0xA4DF, 'Bit 6 set: take fscv_2_star_run', align=Align.INLINE)
d.comment(0xA4E1, "Bit 6 clear: raise 'Bad command'", align=Align.INLINE)
d.comment(0x987E, 'Commit the language-reply state byte', align=Align.INLINE)
d.comment(0x9881, "A=0: 'Bad' error code", align=Align.INLINE)
d.comment(0x9883, 'Raise via error_inline_log (never returns)', align=Align.INLINE)
d.comment(0x8088, 'Y=1: tx_src_stn offset in NMI block', align=Align.INLINE)
d.comment(0x808A, 'Read TX source station from (net_rx_ptr)+1', align=Align.INLINE)
d.comment(0x808C, 'Store as tx_src_stn', align=Align.INLINE)
d.comment(0x8F38, 'A=0: clear-byte for the next four stores', align=Align.INLINE)
d.comment(0x8F3A, 'Clear ws_page (workspace page count)', align=Align.INLINE)
d.comment(0x8F3C, 'Clear tx_complete_flag', align=Align.INLINE)
d.comment(0x8F3F, 'Y=0: receive-block offset 0 (remote-op flag)', align=Align.INLINE)
d.comment(0x8F41, 'Clear remote-op flag at (net_rx_ptr)+0', align=Align.INLINE)
d.comment(0x8F48, "A=&10: fs_flags bit 4 mask (checks 'workspace already set up')", align=Align.INLINE)
d.comment(0x8F43, 'Read l028D (current ROM number)', align=Align.INLINE)
d.comment(0x8F46, 'Non-zero (re-init): take nfs_init_check_fs_flags path', align=Align.INLINE)
d.comment(0x8F5B, 'Copy initial PS template (1C bytes) into ws', align=Align.INLINE)
d.comment(0x8F5E, 'X=1: CMOS &01 = port number', align=Align.INLINE)
d.comment(0x8F60, 'Read CMOS &01', align=Align.INLINE)
d.comment(0x8F63, 'Store at hazel_fs_station (workspace+0)', align=Align.INLINE)
d.comment(0x8F66, 'X=2: CMOS &02 = network number', align=Align.INLINE)
d.comment(0x8F68, 'Read CMOS &02', align=Align.INLINE)
d.comment(0x8F6B, 'Store at hazel_fs_network', align=Align.INLINE)
d.comment(0x8F6E, 'X=3: CMOS &03 = FS station', align=Align.INLINE)
d.comment(0x8F70, 'Read CMOS &03', align=Align.INLINE)
d.comment(0x8F73, 'A = FS station', align=Align.INLINE)
d.comment(0x8F78, 'X=4: CMOS &04 = FS network', align=Align.INLINE)
d.comment(0x8F7D, 'A = FS network', align=Align.INLINE)
d.comment(0x8F9A, 'X=&11: CMOS &11 (ANFS settings)', align=Align.INLINE)
d.comment(0x8F9C, 'Read CMOS &11', align=Align.INLINE)
d.comment(0x8F9F, 'A = settings byte', align=Align.INLINE)
d.comment(0x8FA0, 'Mask bit 6 (CMOS protection-state flag)', align=Align.INLINE)
d.comment(0x8FA2, 'Bit clear: skip the &FF substitution', align=Align.INLINE)
d.comment(0x8FA4, 'A=&FF -- enable protection', align=Align.INLINE)
d.comment(0x8FA6, 'Set ws_0d68/ws_0d69 pair', align=Align.INLINE)
d.comment(0x8FBB, 'Read CMOS &00 (= station ID byte)', align=Align.INLINE)
d.comment(0x8FBE, 'Y (CMOS value) into A', align=Align.INLINE)
d.comment(0x8FBF, 'Non-zero: station ID valid -> alloc_common_entry', align=Align.INLINE)
d.comment(0x9000, "INY wrapped past 0 (station=&FF then INY=&00): report 'CMOS RAM invalid' and default to 1", align=Align.INLINE)
d.comment(0x9004, 'Y=1: net_rx_ptr offset for station-ID byte', align=Align.INLINE)
d.comment(0x9006, 'Store station ID into (net_rx_ptr)+1', align=Align.INLINE)
d.comment(0x9008, 'X=&40: econet_flags init value', align=Align.INLINE)
d.comment(0x900A, 'Initialise econet_flags', align=Align.INLINE)
d.comment(0x901D, "A=3: spool-ctrl byte 'init'", align=Align.INLINE)
d.comment(0x901F, 'Initialise *SPOOL handle in workspace', align=Align.INLINE)
d.comment(0x8FC1, "Print 'Station number in CMOS RAM invalid...' warning", align=Align.INLINE)
d.comment(0x8FFB, 'A=1: default station ID', align=Align.INLINE)
d.comment(0x8FFD, 'BRA to alloc_store_station_id with default', align=Align.INLINE)
d.comment(0x8FFF, 'Check next byte (CMOS station ID hi?)', align=Align.INLINE)
d.comment(0x9002, 'BRA to alloc_store_station_id (always)', align=Align.INLINE)
d.comment(0x900D, 'Call cmd_net_fs to select NFS', align=Align.INLINE)
d.comment(0x9010, 'Z: selection succeeded', align=Align.INLINE)
d.comment(0x9012, 'A=&10: bit 4 marker for fs_flags', align=Align.INLINE)
d.comment(0x9017, 'Store updated fs_flags', align=Align.INLINE)
d.comment(0x901A, 'Initialise ADLC and FILEV/ARGSV/...vectors', align=Align.INLINE)
d.comment(0x9022, 'Send a bridge-discovery packet and poll', align=Align.INLINE)
d.comment(0x9025, 'Save current bridge byte', align=Align.INLINE)
d.comment(0x9026, 'With stored hazel_fs_network (network number)', align=Align.INLINE)
d.comment(0x9029, 'Different: take verify_copy_station_id path', align=Align.INLINE)
d.comment(0x902B, 'Same: store as new hazel_fs_network', align=Align.INLINE)
d.comment(0x902E, 'Y=3: net_rx_ptr offset 3', align=Align.INLINE)
d.comment(0x9030, 'Store at (net_rx_ptr)+3', align=Align.INLINE)
d.comment(0x9032, 'Restore saved byte', align=Align.INLINE)
d.comment(0x9033, 'Y=3: workspace offset', align=Align.INLINE)
d.comment(0x9037, 'Mismatch: skip store', align=Align.INLINE)
d.comment(0x9039, 'Match: store at (nfs_workspace)+3', align=Align.INLINE)
d.comment(0x903B, 'Return', align=Align.INLINE)
d.comment(0x8540, 'A=&85: high byte of tx_done_exit-1 (&8581)', align=Align.INLINE)
d.comment(0x8BE5, 'Y=9: cmd_table_fs sub-table 1 offset', align=Align.INLINE)
d.comment(0x8BE7, 'Read cmd_table_fs+X (entry name byte)', align=Align.INLINE)
d.comment(0x8C32, 'Save Y across OS call', align=Align.INLINE)
d.comment(0x8CE0, 'A=0: clear svc_state marker', align=Align.INLINE)
d.comment(0x8CE2, 'Store -> svc_state', align=Align.INLINE)
d.comment(0x8DE6, 'Print byte no-spool', align=Align.INLINE)
d.comment(0x8E10, 'Print newline no-spool', align=Align.INLINE)
d.comment(0x8E98, 'X=0: CMOS RAM index 0 (station ID)', align=Align.INLINE)
d.comment(0x8E9A, 'A=&A1: OSBYTE &A1 = read CMOS RAM', align=Align.INLINE)
d.comment(0x8ED2, 'X=0: clear OSBYTE X arg', align=Align.INLINE)
d.comment(0x8EE1, 'Clear svc_state', align=Align.INLINE)
d.comment(0x9078, 'Close all FCBs (process_all_fcbs)', align=Align.INLINE)
d.comment(0x93F2, 'X=&20: handle-table base offset', align=Align.INLINE)
d.comment(0x93F4, 'Y=&2F: handle count + flag', align=Align.INLINE)
d.comment(0x93F6, 'Return', align=Align.INLINE)
d.comment(0x945C, 'BRA back to read_filename_char', align=Align.INLINE)
d.comment(0x9463, 'Save Y on entry', align=Align.INLINE)
d.comment(0x988F, 'Read escape_flag', align=Align.INLINE)
d.comment(0x9891, 'Mask with need_release_tube (escape-disable)', align=Align.INLINE)
d.comment(0x9893, 'Bit 7 clear: not escaping, return', align=Align.INLINE)
d.comment(0x995F, 'Advance Y', align=Align.INLINE)
d.comment(0x9960, 'Advance X', align=Align.INLINE)
d.comment(0x9961, 'Loop until X wraps', align=Align.INLINE)
d.comment(0xA3B8, "Print 'File server is ' fragment", align=Align.INLINE)
d.comment(0xA5B8, "A=&93: error code 'Bad command'", align=Align.INLINE)
d.comment(0xA638, 'Find station-bit-3 entry', align=Align.INLINE)
d.comment(0xA63E, 'Record library station in station table', align=Align.INLINE)
d.comment(0xA6D8, 'A=&40: protection-level marker', align=Align.INLINE)
d.comment(0xA6E4, 'Save state', align=Align.INLINE)
d.comment(0xA9D6, 'Step back', align=Align.INLINE)
d.comment(0xAA72, 'WS-to-PB direction (read)', align=Align.INLINE)
d.comment(0xAA78, 'Save A as osword_flag (counter)', align=Align.INLINE)
d.comment(0xAA8C, 'Next byte', align=Align.INLINE)
d.comment(0xAA90, 'Return', align=Align.INLINE)
d.comment(0xAA96, 'A = current byte index', align=Align.INLINE)
d.comment(0xAA9A, 'WS-to-PB direction', align=Align.INLINE)
d.comment(0xAAA0, 'Next byte', align=Align.INLINE)
d.comment(0xAB68, 'Y=1: PB[1] = RX flag location', align=Align.INLINE)
d.comment(0xAB8D, 'PB-to-WS direction (write)', align=Align.INLINE)
d.comment(0xAB93, 'Next ctx byte', align=Align.INLINE)
d.comment(0xAB9D, 'Return', align=Align.INLINE)
d.comment(0xAC4B, 'Save state', align=Align.INLINE)
d.comment(0xAC64, 'Next byte', align=Align.INLINE)
d.comment(0xAC74, 'Y=&20: TXCB offset', align=Align.INLINE)
d.comment(0xAC8F, 'Read nfs_workspace_hi', align=Align.INLINE)
d.comment(0xACF8, 'Re-enable IRQs', align=Align.INLINE)
d.comment(0xAE5A, 'Step counter', align=Align.INLINE)
d.comment(0xAE61, 'Shift bit 0 into C', align=Align.INLINE)
d.comment(0xB05F, 'Read saved copy of ws_0d68 from ws_0d69', align=Align.INLINE)
d.comment(0xB062, 'Store back to ws_0d68', align=Align.INLINE)
d.comment(0xB065, 'Return', align=Align.INLINE)
d.comment(0xB081, 'X=0: zero-arg helper entry', align=Align.INLINE)
d.comment(0xB357, 'Clear owner-only access bits before checking the URD', align=Align.INLINE)
d.comment(0xB35A, "A=&69: 'i' character (info prefix)", align=Align.INLINE)
d.comment(0xB35C, "Store 'i' as start of FS command name in the TX buffer", align=Align.INLINE)
d.comment(0xB35F, "A='.': abbreviation terminator", align=Align.INLINE)
d.comment(0xB361, "Store '.' as command-name terminator", align=Align.INLINE)
d.comment(0xB364, 'Save the command-line pointer for the dispatcher', align=Align.INLINE)
d.comment(0xB367, 'Parse the *Info argument from the command line', align=Align.INLINE)
d.comment(0xB36A, "X=2: TX-buffer offset to copy the arg into (after 'i.')", align=Align.INLINE)
d.comment(0xB36C, 'Append parsed argument to the TX command buffer', align=Align.INLINE)
d.comment(0xB370, 'Send the FS command and dispatch the reply', align=Align.INLINE)
d.comment(0xB36F, 'A = next index', align=Align.INLINE)
d.comment(0xB4B3, 'Return', align=Align.INLINE)
d.comment(0xB52A, 'Return', align=Align.INLINE)
d.comment(0xB831, 'Clear tx_buffer_scratch+X scratch', align=Align.INLINE)
d.comment(0xB8A7, 'Return', align=Align.INLINE)
d.comment(0xBB38, 'Save X on entry', align=Align.INLINE)
d.comment(0xBF9F, 'Store as os_text_ptr_hi', align=Align.INLINE)
d.comment(0xBFA2, 'Store as os_text_ptr lo', align=Align.INLINE)

d.label(0x8EFE, 'set_rom_ws_page')

d.label(0x8F24, 'commit_workspace_pages')

d.label(0x901A, 'complete_nfs_init')

d.label(0x96FA, 'start_help_file_load')

d.label(0x970F, 'loop_print_help_byte')

d.label(0x972E, 'handle_help_paged_mode')

d.label(0xA0DF, 'osopt_check_cmos_protect')

d.label(0xB625, 'loop_pollps_next_slot')

d.label(0x8032, 'irq_check_dispatch')

d.label(0x8211, 'page_boundary_restore')

d.label(0x8258, 'byte_pair_restore')

d.label(0x8264, 'frame_complete_restore')

d.label(0x842F, 'scout_done_restore_x')

d.label(0x8434, 'dispatch_imm_op_fail')

d.label(0x847E, 'tube_overflow_restore')

d.label(0x8524, 'enable_irq_pending')

d.label(0x881B, 'check_fifo_loop')

d.label(0x8827, 'frame_end_restore')

d.label(0x8922, 'shadow_enable_flag')

d.label(0x8A8D, 'restore_rom_slot_entry')

d.label(0x8ACE, 'dispatch_svc_state_check')

d.label(0x8B5A, 'select_fs_cmd_net_fs')

d.label(0x8C46, 'svc4_dispatch_lookup')

d.label(0x8CBB, 'get_ws_page_loop')

d.label(0x8E7E, 'fs_template_done')

d.label(0x8E7F, 'fs_info_template')
d.banner(0x8E7F, title='FS-name reply template (11 bytes, byte-reversed)', description="""Source data for the byte-reverse copy in
[`copy_template_to_zp`](address:8E73). When stored at
`(os_text_ptr),Y` in reverse order the destination reads
`"NET" + 6 spaces + "/" + length-byte 5`, which is the FS name
the ROM reports for service &25 (FS name + info reply).""")

d.label(0x8F1F, 'private_ws_set_bit')

d.label(0x8F4F, 'nfs_init_check_fs_flags')

d.label(0x8FA6, 'init_copy_skip_cmos')

d.label(0x8FBB, 'alloc_post_restore_check')

d.label(0x8FC1, 'alloc_error_overflow')

d.label(0x8FFF, 'alloc_common_entry')

d.label(0x9004, 'alloc_store_station_id')

d.label(0x9032, 'verify_copy_station_id')

d.label(0x925D, 'print_nybble_leading_zero')

d.label(0x9298, 'print_next_string_char')

d.label(0x92AF, 'print_char_terminator')

d.label(0x9421, 'clear_channel_flag')

d.label(0x95BE, 'bra_target_svc_return')

d.label(0x9653, 'parse_object_space_print')

d.label(0x968C, 'help_dispatch_setup')

d.label(0x9697, 'on_suffix_pattern')

d.label(0x96B0, 'match_char_loop_cmp')

d.label(0x96B2, 'match_char_found')

d.label(0x96BC, 'match_char_process')

d.label(0x971E, 'help_print_start')

d.label(0x9725, 'help_print_char_check')

d.label(0x9827, 'scan_channel_store_reply')

d.label(0x9984, 'suffix_copy_loop')

d.label(0x9A0D, 'net_error_close_spool')

d.label(0xA0CF, 'osargs_store_ptr_lo')

d.label(0xA0DB, 'osargs_check_length')

d.label(0xA103, 'cmos_opt_mask_table')
d.banner(0xA103, title='CMOS &11 bit-field masks for OSARGS / *OPT 4 (8 bytes)', description="""Used by the OSARGS-via-FSCV / *OPT 4 path
([`osopt_check_cmos_protect`](address:A0DF)) to read or update bit
fields inside CMOS RAM byte `&11` (the Econet status byte holding
the auto-boot type and printer/messages flags).

- **Indices 0-3** are extraction masks: `AND CMOS_&11` with
  `&01`, `&02`, `&04`, `&06` returns bit 0, bit 1, bit 2 or
  bits 1+2 respectively.
- **Indices 4-7** are clear masks: `AND CMOS_&11` with `&FD`,
  `&F3`, `&CF`, `&3F` zeroes bits 1, 2-3, 4-5 or 6-7 in turn,
  before OR-ing the new value back in.

A second indexed-base trick reads the same eight bytes through
[`cmos_attr_table`](address:A0FF) (this label - 4): for write
sub-codes 4-7 the read-masks at indices 0-3 (1, 2, 4, 6) double
as the bit-shift counts that left-align the new value into its
target field.""")
for _i in range(8):
    d.byte(0xA103 + _i)
del _i
d.comment(0xA103, 'Idx 0: AND mask = &01 (extract CMOS &11 bit 0)', align=Align.INLINE)
d.comment(0xA104, 'Idx 1: AND mask = &02 (extract CMOS &11 bit 1)', align=Align.INLINE)
d.comment(0xA105, 'Idx 2: AND mask = &04 (extract CMOS &11 bit 2)', align=Align.INLINE)
d.comment(0xA106, 'Idx 3: AND mask = &06 (extract CMOS &11 bits 1,2)', align=Align.INLINE)
d.comment(0xA107, 'Idx 4: AND mask = &FD (clear CMOS &11 bit 1)', align=Align.INLINE)
d.comment(0xA108, 'Idx 5: AND mask = &F3 (clear CMOS &11 bits 2,3)', align=Align.INLINE)
d.comment(0xA109, 'Idx 6: AND mask = &CF (clear CMOS &11 bits 4,5)', align=Align.INLINE)
d.comment(0xA10A, 'Idx 7: AND mask = &3F (clear CMOS &11 bits 6,7)', align=Align.INLINE)

d.label(0xA3E5, 'no_station_loop')

d.label(0xA4A0, 'separator_char_table')

d.label(0xA4FC, 'cmd_run_load_mask')

d.label(0xA5DF, 'library_path_string')

d.label(0xA6FE, 'fsreply_2_skip_handles')

d.label(0xA70B, 'fsreply_2_handle_loop')

d.label(0xA71C, 'fsreply_2_store_handle')

d.label(0xA75B, 'boot_prefix_string')

d.label(0xA75F, 'boot_suffix_string')

d.label(0xA855, 'osword_store_svc_state')

d.label(0xA871, 'osword_pb_ready')

d.label(0xA8E7, 'save_txcb_done')

d.label(0xAF92, 'printer_busy_msg')

d.label(0xB097, 'read_osbyte_return')

d.label(0xB099, 'read_osbyte_table')

d.label(0xB0EE, 'cdir_size_done')
d.byte(0xB0F0)
d.byte(0xB0F1)
d.comment(0xB0EE, 'Index 26: threshold &F6 (246) -- last cdir-size threshold; doubles as cdir_size_done[0] (unread by init loop)', align=Align.INLINE)
d.comment(0xB0EF, 'cdir_size_done[1] = &FF -> tx_retry_count (retry counter init)', align=Align.INLINE)
d.comment(0xB0F0, 'cdir_size_done[2] = &28 -> rx_wait_timeout (40 retries)', align=Align.INLINE)
d.comment(0xB0F1, 'cdir_size_done[3] = &0A -> peek_retry_count (10 retries)', align=Align.INLINE)

d.label(0xB185, 'cat_after_label_print')

d.label(0xB29C, 'option_offset_table')

d.label(0xB2F7, 'col_sep_eol_check')

d.label(0xB2F9, 'col_sep_print_cr')

d.label(0xB2FC, 'col_sep_print_char')

d.label(0xB474, 'print_ps_padding')

d.label(0xB56F, 'local_net_prefix')

d.label(0xB6D8, 'unprot_clear')

d.label(0xB6E9, 'unprot_check')

d.label(0xB6EB, 'unprot_apply')

d.label(0xBD2D, 'escape_error_close')

d.label(0xC109, 'hazel_exec_addr')


d.subroutine(0x8409, 'save_acccon_for_shadow_ram', title='Save ACCCON across scout-buffer access', description="""Saves the current [`acccon`](address:FE34) value, sets ACCCON
for the upcoming `(open_port_buf),Y` stores (so writes go to the
right shadow / main RAM bank on the Master 128), performs the
copy, then restores the saved ACCCON before returning. Wraps the
inner copy loop with shadow-RAM gating so scout-buffer writes
land in the caller's address space rather than the FS-private
HAZEL window.""")

d.label(0x8BEA, 'loop_print_cmd_name')


d.subroutine(0x8DA6, 'load_transfer_params', title='Set FS transfer parameters via set_xfer_params', description="""3-byte trampoline that calls
[`set_xfer_params`](address:93D7) and falls through into
[`cmd_pass`](address:8DD5)'s argument-parse prologue. Reached
from `init_txcb_and_load_xfer` at `&B3D9` to install the FS
transfer context (byte count + source pointer in `fs_last_byte_flag`
/ `fs_crc_lo`/`hi`) before continuing into the *I am / *Pass
station-and-credential parser.""")

d.label(0x8E75, 'loop_copy_return_template')

d.label(0x9292, 'loop_print_inline_string')


d.subroutine(0x95C1, 'print_station_low', title="Print 'PS       ' 9-column header", description="""Calls [`print_inline`](address:9261) with `'P'` then falls
through (via the 1-byte CLV terminator and BVC) into
[`print_field_tail_s`](address:95CD), so the combined output is
`'PS       '` -- the 9-column 'PS' field used in the `*FS`/`*PS`
no-arg help and `*STATUS` displays.""")


d.subroutine(0x95C8, 'print_fs_station', title="Print 'FS       ' 9-column header", description="""Calls [`print_inline`](address:9261) with `'F'` then falls
through (via the 1-byte NOP terminator) into
[`print_field_tail_s`](address:95CD), so the combined output is
`'FS       '` -- the 9-column 'FS' field used in the `*FS`/`*PS`
no-arg help and `*STATUS` displays.""")


d.subroutine(0x95DA, 'print_dir_syntax', title="Print '[<D>.]<D>\\\\r' directory-name syntax fragment", description="""3-byte JSR + inline `'[<D>.]<D>'` + CR + NOP terminator. Used as
a shared fragment by both `*Dir`'s syntax help and the `*FS`/`*PS`
no-argument help via [`print_fs_ps_help`](address:959A).""")


d.subroutine(0x965F, 'print_ps_address', title='Print printer-server address from CMOS', description="""Reads the printer-server's saved network number from CMOS byte
&04, prints it as decimal (no leading zeros), prints a `.`
separator, then sets `X=3` and falls into
[`print_cmos_decimal_nl`](address:967F) to read CMOS &03 and
print the printer-server station with a trailing newline.
Returns via the [`print_cmos_done`](address:9689) trampoline.""")


d.subroutine(0x9670, 'print_fs_address', title='Print file-server address from CMOS', description="""Reads the file-server's saved network number from CMOS byte
&02, prints it as decimal (no leading zeros), prints a `.`
separator, then sets `X=1` and falls into
[`print_cmos_decimal_nl`](address:967F) to read CMOS &01 and
print the file-server station with a trailing newline. Returns
via the [`print_cmos_done`](address:9689) trampoline.""")


d.subroutine(0x968E, 'dispatch_help_command', title='Dispatch *HELP-style argument via svc4_dispatch_lookup', description="""3-byte trampoline: `JMP svc4_dispatch_lookup` with `X = &BD` from
the caller. Used by [`svc_29_status`](address:9630)'s
non-CR path so an argument after `*STATUS` (or similar *HELP-like
cmd) gets parsed and dispatched through the same shared parser as
the regular cmd-table dispatch. Note the `'!Help.'` bytes
immediately following are an unrelated inline string used by the
filename walker, not part of this routine's body.""")

d.label(0x96A7, 'loop_match_on_suffix')

d.label(0x96BD, 'loop_skip_non_spaces')

d.label(0x96C8, 'loop_help_skip_spaces')

d.label(0x96DB, 'loop_copy_command_suffix')

d.label(0x96E7, 'loop_copy_topic_name')

d.label(0x96EB, 'loop_store_topic_char')


d.subroutine(0x9FEE, 'send_open_file_request', description='Send file open request with V flag set for directory check.')

d.label(0xA0F2, 'loop_extract_attribute_bits')

d.label(0xA84A, 'loop_save_osword_workspace')

d.label(0xA85C, 'loop_restore_osword_workspace')


d.subroutine(0xA877, 'extract_osword_subcode', title='Decode OSWORD &0E parameter byte and branch to handler', description="""Right-shifts `ws_page` (PB[0]) into `A`, transfers it to `Y` for
the dispatcher, then runs an EOR/CMP chain against
`ws_precomputed_value` to classify the requested sub-code:

| Test          | Path                              |
| ------------- | --------------------------------- |
| `CMP #4` =    | `save_txcb_and_convert` (clock)   |
| `CMP #3` =    | `save_txcb_done` (write back)     |
| anything else | set `svc_state = 8` and `RTS`     |

The two `LDA #&A9` filler bytes preceding the EOR are a 4-byte
BIT-trick skip used when the alternate entry [`osword_0e_handler`
](address:A874) is taken via the `BIT $abs` at `&A874`. Reached
only via the OSWORD `&0E` (CMOS clock read) handler chain.""")

d.label(0xA8EC, 'loop_copy_pbytes_to_workspace')

d.label(0xB0A0, 'cmd_cdir_indirect_dispatch')

d.label(0xB1B4, 'loop_print_dir_format')

d.label(0xB2B9, 'loop_trim_trailing_spaces')

d.label(0xB316, 'loop_divide_decimal_digit')

d.label(0xBB3C, 'loop_save_fcb_workspace')

d.label(0xBB5F, 'loop_restore_fcb_workspace')

d.label(0xBE16, 'loop_print_hex_row')

d.label(0x0020, 'tx_buffer_scratch', length=1, group='zero_page', access='rw')

d.label(0x0026, 'parse_separator_flag', length=1, group='zero_page', access='rw')

d.label(0x00ED, 'tx_imm_idx_base', length=1, group='zero_page', access='rw')

d.label(0x0100, 'error_block')

d.label(0x0101, 'error_text')

d.label(0x0102, 'stack_page_2')

d.label(0x0103, 'stack_page_3')

d.label(0x0104, 'stack_page_4')

d.label(0x0106, 'stack_page_6')

d.label(0x028D, 'last_break_type')

d.label(0x02A0, 'rom_type_table')

d.label(0x0350, 'vdu_screen_mode', description='VDU screen mode set by the OS.', length=1, group='ram_workspace', access='r')

d.label(0x0351, 'vdu_display_start_hi', description='VDU display start address (high byte).', length=1, group='ram_workspace', access='r')

d.label(0x0355, 'vdu_mode', description="""VDU current output stream selector.
Determines whether `OSWRCH` writes to the screen, printer, serial port, etc. ANFS reads this to decide whether to wrap *HELP syntax lines for serial output.""", length=1, group='ram_workspace', access='r')

d.label(0x0406, 'tube_addr_data_dispatch')

d.label(0x0CFF, 'nmi_code_base')

d.label(0x0D71, 'spool_control_flag', description='Multi-purpose: spool-buffer control flag (printer spooling); also doubles as the bridge-routing-table status byte read by [`init_bridge_poll`](address:ABE9) (`&FF` = uninitialised, anything else = bridge already polled).', length=1, group='ram_workspace', access='rw')

d.label(0x2048, 'ws_template_source')

d.label(0x2322, 'separator_parse_dispatch')

d.label(0x4898, 'cdir_unused_dispatch_table')

d.label(0x688B, 'ws_precomputed_value')

d.label(0x6F6E, 'false_ref_6f6e')

d.label(0xC000, 'hazel_fs_station', description="""Filing-system state block (`&C000`–`&C00A`).

Eleven bytes of currently-selected-FS context kept in HAZEL: station / network of the FS, saved prefix station, multi-purpose CSD/library/boot-type slots, FS flags, messages flag, pending-state, error code, last-error, and `*OPT` addend. The first two bytes (`hazel_fs_station`, `hazel_fs_network`) are the FS address used for every TX scout.""", length=11, group='hazel', access='rw')

d.label(0xC001, 'hazel_fs_network', description='FS network number (sub-byte of the &C000 FS context block).', length=1, group='hazel', access='rw')

d.label(0xC002, 'hazel_fs_saved_station')

d.label(0xC003, 'hazel_fs_context_copy', description='Multi-purpose sub-byte of the &C000 block: CSD handle / matched-entry index / Y-indexed base into FS context block.', length=1, group='hazel', access='rw')

d.label(0xC004, 'hazel_fs_prefix_stn', description='Multi-purpose sub-byte of the &C000 block: saved-prefix station / library handle / boot type.', length=1, group='hazel', access='rw')

d.label(0xC005, 'hazel_fs_flags')

d.label(0xC006, 'hazel_fs_messages_flag')

d.label(0xC007, 'hazel_fs_pending_state')

d.label(0xC008, 'hazel_fs_error_code', description='FS error code (sub-byte of the &C000 block).', length=1, group='hazel', access='rw')

d.label(0xC009, 'hazel_fs_last_error', description='Last FS error byte (sub-byte of the &C000 block).', length=1, group='hazel', access='rw')

d.label(0xC00A, 'hazel_fs_opts_addend')

d.label(0xC014, 'hazel_retry_counter', description='Retry counter for the current Econet TX/RX cycle.', length=1, group='hazel', access='rw')

d.label(0xC02F, 'hazel_parse_buf_m1')

d.label(0xC030, 'hazel_parse_buf', description='Three-byte parse-buffer used for command-line matching (e.g. `*OPT`, `*FS`).', length=3, group='hazel', access='rw')

d.label(0xC031, 'hazel_parse_buf_1')

d.label(0xC032, 'hazel_parse_buf_2')

d.label(0xC038, 'hazel_rtc_buffer', description='OSWORD `&0E` real-time-clock result buffer.', length=25, group='hazel', access='rw')

d.label(0xC0F7, 'hazel_fs_reply_byte', description='Latched first byte of the most recent FS reply.', length=1, group='hazel', access='rw')

d.label(0xC100, 'hazel_txcb_port', description='TXCB byte 0: port number for the next TX scout.', length=1, group='hazel', access='rw')

d.label(0xC101, 'hazel_txcb_func_code', description='TXCB byte 1: function code (FS command number).', length=1, group='hazel', access='rw')

d.label(0xC102, 'hazel_txcb_station', description='TXCB byte 2: destination station.', length=1, group='hazel', access='rw')

d.label(0xC103, 'hazel_txcb_network', description="""TXCB byte 3: multi-purpose.
TXCB destination network (TX setup) / reply function code (RX context) / `fs_cmd_csd` buffer base (other paths).""", length=1, group='hazel', access='rw')

d.label(0xC104, 'hazel_txcb_lib', description='TXCB byte 4: library handle terminator / transfer-length param 1.', length=1, group='hazel', access='rw')

d.label(0xC105, 'hazel_txcb_data', description='TXCB byte 5: first reply-data byte / data start.', length=1, group='hazel', access='rw')

d.label(0xC106, 'hazel_txcb_flag', description='TXCB byte 6: direction flag.', length=1, group='hazel', access='rw')

d.label(0xC107, 'hazel_txcb_count', description='TXCB byte 7: data count / lock flag.', length=1, group='hazel', access='rw')

d.label(0xC108, 'hazel_txcb_result', description='TXCB byte 8: result / transfer-size lo.', length=1, group='hazel', access='rw')

d.label(0xC10A, 'hazel_txcb_size_hi')

d.label(0xC10B, 'hazel_txcb_tx_status')

d.label(0xC10C, 'hazel_txcb_osword_flag')

d.label(0xC10D, 'hazel_txcb_addr_lo')

d.label(0xC10E, 'hazel_txcb_access')

d.label(0xC110, 'hazel_txcb_addr_hi')

d.label(0xC111, 'hazel_txcb_len')

d.label(0xC112, 'hazel_txcb_type')

d.label(0xC113, 'hazel_txcb_objtype')

d.label(0xC114, 'hazel_txcb_cycle')

d.label(0xC116, 'hazel_txcb_byte_16')

d.label(0xC12F, 'hazel_txcb_end')

d.label(0xC130, 'hazel_examine_attr')

d.label(0xC1C8, 'hazel_chan_status')

d.label(0xC1DC, 'hazel_net_reply_buf_0')

d.label(0xC1DD, 'hazel_net_reply_buf_1')

d.label(0xC1DE, 'hazel_net_reply_buf_2')

d.label(0xC1DF, 'hazel_net_reply_buf_3')

d.label(0xC1E0, 'hazel_fcb_addr_lo_minus20')

d.label(0xC1F0, 'hazel_fcb_addr_mid_minus20')

d.label(0xC1FF, 'hazel_display_buf_minusF4')

d.label(0xC200, 'hazel_fcb_addr_lo', description="""FCB parallel array (16 entries): file position byte 0 (low).
Indexed by channel `0..15`; cleared by [`alloc_fcb_slot`](address:B8A8) on FCB allocation.""", length=16, group='hazel', access='rw')

d.label(0xC210, 'hazel_fcb_addr_mid', description='FCB parallel array (16 entries): file position byte 1 (mid).', length=16, group='hazel', access='rw')

d.label(0xC220, 'hazel_fcb_addr_hi', description='FCB parallel array (16 entries): file position byte 2 (high).', length=16, group='hazel', access='rw')

d.label(0xC230, 'hazel_fcb_slot_attr', description="""FCB parallel array (16 entries): slot occupancy + channel attribute.
Tested for zero by [`alloc_fcb_slot`](address:B8A8) as the slot-free check; set non-zero on allocation.""", length=16, group='hazel', access='rw')

d.label(0xC240, 'hazel_fcb_state_byte', description="""FCB parallel array (16 entries): multi-purpose state byte.
Holds station number for non-OSFIND channels, or open-mode flags for channels created by OSFIND.""", length=16, group='hazel', access='rw')

d.label(0xC250, 'hazel_fcb_network', description='FCB parallel array (16 entries): network number per channel.', length=16, group='hazel', access='rw')

d.label(0xC260, 'hazel_fcb_status', description="""FCB parallel array (16 entries): per-channel status flags.
Heavily used: bit 6 = connection active (`set_conn_active` / `clear_conn_active` toggle).""", length=16, group='hazel', access='rw')

d.label(0xC270, 'hazel_cur_dir_handle')

d.label(0xC271, 'hazel_fs_lib_flags', description='FS library / option flags. Bit 2 = auto-boot, bit 7 = library-directory pending. Cleared / tested by *Cat / *Lcat / *Ex / *Lex paths.', length=1, group='hazel', access='rw')

d.label(0xC272, 'hazel_fcb_slot_1')

d.label(0xC273, 'hazel_fcb_slot_2')

d.label(0xC274, 'hazel_fcb_slot_3')

d.label(0xC278, 'hazel_fcb_station_lo')

d.label(0xC288, 'hazel_fcb_station_hi')

d.label(0xC298, 'hazel_fcb_offset_save')

d.label(0xC2A8, 'hazel_fcb_attr_ref')

d.label(0xC2B8, 'hazel_fcb_flags')

d.label(0xC2C8, 'hazel_cur_fcb_index', description='Current FCB index used by the FCB-scan loop in [`process_all_fcbs`](address:BB38). Followed by the channel attribute / reference, byte-counter, buffer pointer and a small block of transfer-state scratch bytes used during file I/O.', length=1, group='hazel', access='rw')

d.label(0xC2C9, 'hazel_chan_attr')

d.label(0xC2CA, 'hazel_chan_ref')

d.label(0xC2CB, 'hazel_byte_counter_lo')

d.label(0xC2CC, 'hazel_buf_addr_hi')

d.label(0xC2CD, 'hazel_sentinel_cd', description='Sentinel/scratch byte at HAZEL+&CD, used by the FCB-scan loop in [`process_all_fcbs`](address:BB38).', length=1, group='hazel', access='rw')

d.label(0xC2CE, 'hazel_sentinel_ce', description='Sentinel/scratch byte at HAZEL+&CE, used by the FCB-scan loop in [`process_all_fcbs`](address:BB38).', length=1, group='hazel', access='rw')

d.label(0xC2CF, 'hazel_offset_counter')

d.label(0xC2D0, 'hazel_pass_counter')

d.label(0xC2D1, 'hazel_xfer_init_zeros')

d.label(0xC2D4, 'hazel_station_lo')

d.label(0xC2D5, 'hazel_station_hi')

d.label(0xC2D6, 'hazel_transfer_flag')

d.label(0xC2D7, 'hazel_saved_byte')

d.label(0xC2D8, 'hazel_quote_mode')

d.label(0xC2D9, 'hazel_ctx_buffer', description='HAZEL context buffer (saved register / state block used during FCB processing).', length=1, group='hazel', access='rw')

d.label(0xC2F3, 'hazel_display_buf')

d.label(0xFE28, 'master_romsel_shadow', description="""Master 128 ROMSEL shadow register.
Read-only mirror of the current sideways-ROM selection (the actual ROMSEL is at `&FE30`).""", length=1, group='mmio', access='r')

d.label(0xFE2B, 'master_break_type_shadow', description="""Master 128 last-break-type hardware shadow.
Reflects the value left by the last reset (cold / warm / power-on).""", length=1, group='mmio', access='r')

d.label(0xFE34, 'acccon', description="""Master 128 ACCCON access-control register.

Bit-by-bit (write-only):

| Bit | Name | Effect when set |
|---|---|---|
| 7 | IRR | IRQ-on-VSYNC mask |
| 6 | TST | Test mode |
| 5 | IFJ | I/O is JIM |
| 4 | ITU | Internal Tube |
| 3 | Y   | HAZEL paged in (`&C000-&DFFF` is hidden RAM) |
| 2 | X   | LYNNE paged in (`&3000-&7FFF` is shadow RAM) |
| 1 | E   | shadow RAM owns screen |
| 0 | D   | shadow RAM for the OS display |

ANFS uses bit 7 (IRR) as a deferred-work latch via `TRB`/`TSB`.""", length=1, group='mmio', access='rw')

d.label(0xFE38, 'master_intoff', description="""Master 128 INTOFF mirror (NMI-disable side effect).
Reading any byte here disables /NMI re-entry; the byte value itself is irrelevant.""", length=1, group='mmio', access='r')

d.label(0xFE3C, 'master_inton', description="""Master 128 INTON mirror (NMI-enable side effect).
Reading any byte here re-enables /NMI; the byte value itself is irrelevant.""", length=1, group='mmio', access='r')

d.label(0xFFB0, 'nmi_buf_idx_base', description="""NMI buffer indexing-base.
Used by the NMI RX setup as `STA nmi_buf_idx_base,Y` with Y values that wrap into low memory; the bytes at `&FFB0` themselves aren't read or written.""", length=1, group='idx_base', access='r')

d.label(0xFFBD, 'fcb_workspace_idx_base', description="""FCB-workspace indexing-base (wraps into ZP).
Used by `loop_save_fcb_workspace` as the base of `LDA &FFBD,X` with X=`&F7`..`&FF`; the effective address wraps to `&00B4`..`&00BC` (= `fs_work_4`+0..+8). The byte at `&FFBD` itself is never read.""", length=1, group='idx_base', access='r')

d.label(0x840A, 'imm_op_handler_lo_table')

d.label(0x886F, 'tx_length_table')

d.label(0x8877, 'tx_flags_table')

d.label(0x89C9, 'nmi_shim_source')

d.label(0x968F, 'help_topic_template')

d.label(0x99A3, 'bad_prefix_table')

d.label(0xA0FE, 'osopt_cmos_writeback_jsr')

d.label(0xA0FF, 'cmos_attr_table', description="""Indexing-base alias of [`cmos_opt_mask_table`](address:A103) - 4.
`LDA cmos_attr_table,X` at &A0ED with X=4..7 reads the read-masks 1, 2, 4, 6 from the underlying table; those values double as bit-shift counts that left-align the new field into CMOS &11. The byte at &A0FF is inside the operand of the JSR at &A0FE and is never read directly.""", length=1, group='idx_base', access='r')

d.label(0xA76D, 'cmd_dispatch_lo_table')

d.label(0xA76E, 'cmd_dispatch_hi_table')

d.label(0xA878, 'osword_subcode_dispatch')

d.label(0xABC5, 'bridge_err_table')

d.label(0xB0D4, 'cdir_size_thresholds')

d.label(0xB4FD, 'ps_print_template')

d.label(0xB821, 'net_chan_err_strings')
d.comment(0xA741, "Boot command 'L.-NET-!Boot' (Load !Boot)", align=Align.INLINE)
d.comment(0xA74D, 'CR terminator', align=Align.INLINE)
d.comment(0xA74E, "Boot command 'E.-NET-!Boot' (Exec !Boot)", align=Align.INLINE)
d.comment(0xA75A, 'CR terminator', align=Align.INLINE)
d.comment(0xA75B, "Boot command low-byte index table -- 4 bytes spelling 'ZAHN', each the low byte of a boot-command address in the &A7xx page (Z=&5A, A=&41, H=&48, N=&4E)", align=Align.INLINE)
d.comment(0xA764, 'Load boot-command low byte from boot_prefix_string[Y]', align=Align.INLINE)
d.comment(0xA767, 'Y=&A7: high byte (boot strings live in &A7xx)', align=Align.INLINE)
d.comment(0xA769, 'Tail-jump to OSCLI to execute the boot command', align=Align.INLINE)
d.comment(0xA83D, 'OSWORD setup state (13 bytes -- constants and offsets used by svc_8_osword)', align=Align.INLINE)
d.comment(0xA3E9, 'Multiply A by 2', align=Align.INLINE)
d.comment(0xA3EA, 'Multiply A by 2 again -- A is now A_orig * 4', align=Align.INLINE)
d.comment(0xA3EB, 'Stash A_orig * 4 on the stack', align=Align.INLINE)
d.comment(0xA3EC, 'Multiply A by 2 -- A is now A_orig * 8 (C = bit 7 of A_orig*4)', align=Align.INLINE)
d.comment(0xA3ED, 'Capture S so we can read the just-pushed value', align=Align.INLINE)
d.comment(0xA3EE, 'Save the C flag from the third ASL', align=Align.INLINE)
d.comment(0xA3EF, 'ADC stack[X+1] = A_orig*4 (with C from the ASL): A = A_orig*8 + A_orig*4 + C = A_orig*12 + C', align=Align.INLINE)
d.comment(0xA3F2, 'Halve the result, putting the new C as bit 7', align=Align.INLINE)
d.comment(0xA3F3, 'Restore the saved C (from the third ASL)', align=Align.INLINE)
d.comment(0xA3F4, "ASL doubles the halved value (effectively undoes the ROR's divide while reusing C)", align=Align.INLINE)
d.comment(0xA3F5, 'Y = A_orig * 12 (the 12-byte-aligned index)', align=Align.INLINE)
d.comment(0xA3F6, 'Recover A_orig * 4 (left on the stack at &A3EB)', align=Align.INLINE)
d.comment(0xA3F7, 'Above &48 (i.e. A_orig * 4 >= 72, A_orig >= 18)?', align=Align.INLINE)
d.comment(0xA3F9, 'No: keep computed Y', align=Align.INLINE)
d.comment(0xA3FB, 'Yes: clamp Y to 0 (out of range)', align=Align.INLINE)
d.comment(0xA3FD, 'Mirror Y -> A so callers can test Z', align=Align.INLINE)
d.comment(0xA3FE, 'Return; Y holds 12-byte-aligned offset, A is non-zero on success', align=Align.INLINE)
d.comment(0xB3D7, 'X=&F8: walks 0..7 via wraparound (loads from ps_template_base+&F8 = ps_template_data &8E9F)', align=Align.INLINE)
d.comment(0xB3D9, 'Read template byte from ps_template_data + (X-&F8)', align=Align.INLINE)
d.comment(0xB3DC, 'Store into RX buffer at offset Y', align=Align.INLINE)
d.comment(0xB3DE, 'Step destination', align=Align.INLINE)
d.comment(0xB3DF, 'Step source -- wraps from &FF to &00 to terminate', align=Align.INLINE)
d.comment(0xB3E0, 'Loop while X != 0 (8 iterations: &F8..&FF)', align=Align.INLINE)
d.comment(0xB3E2, 'Return', align=Align.INLINE)
d.comment(0xBEAB, 'Step Y past the *Dump command name into the argument', align=Align.INLINE)
d.comment(0xBEAC, 'Save the cursor offset', align=Align.INLINE)
d.comment(0xBEAE, "Set bit 0 of addr_work to 1 -- 'mode' flag for parse_dump_range below", align=Align.INLINE)
d.comment(0xBEB0, 'Save mode flag', align=Align.INLINE)
d.comment(0xBEB2, 'Parse the start address (max 4 hex digits)', align=Align.INLINE)
d.comment(0xBEB5, 'Overflow: too many digits', align=Align.INLINE)
d.comment(0xBEB7, 'Save current Y (cursor after start address)', align=Align.INLINE)
d.comment(0xBEB8, 'Push it', align=Align.INLINE)
d.comment(0xBEB9, 'Y = file handle saved in ws_page', align=Align.INLINE)
d.comment(0xBEBB, 'X=&AA: zero-page address for OSARGS result', align=Align.INLINE)
d.comment(0xBEBD, 'A=2: OSARGS sub-fn 2 = read sequential file extent', align=Align.INLINE)
d.comment(0xBEBF, 'Get file size into 4 bytes at &AA', align=Align.INLINE)
d.comment(0xBEC2, 'Y=3: compare 4-byte values (high to low)', align=Align.INLINE)
d.comment(0xBEC4, 'Read file size byte at &AA+Y', align=Align.INLINE)
d.comment(0xBEC7, 'Compare with parsed start address (work_ae+Y)', align=Align.INLINE)
d.comment(0xBEC9, 'Mismatch: branch decides which is bigger', align=Align.INLINE)
d.comment(0xBECB, 'Step to next byte', align=Align.INLINE)
d.comment(0xBECC, 'Loop while Y >= 0 (covers indices 3, 2, 1, 0)', align=Align.INLINE)
d.comment(0xBECE, 'All bytes equal: start = extent (allowed); jump to the post-validation path', align=Align.INLINE)
d.comment(0xBED0, 'C clear: parsed_start > file_size -- reject', align=Align.INLINE)
d.comment(0xBED2, "Y=&FF: signal 'no copy needed' to the loop below", align=Align.INLINE)
d.comment(0xBED4, 'Always taken: skip directly to advance phase', align=Align.INLINE)
d.comment(0xBED6, 'Close the file before raising', align=Align.INLINE)
d.comment(0xBED9, "A=&B7: 'Outside file' error code", align=Align.INLINE)
d.comment(0xBEDB, 'Raise via inline string; never returns', align=Align.INLINE)
d.comment(0xBEEB, 'Copy file-extent byte from osword_flag to (work_ae)', align=Align.INLINE)
d.comment(0xBEED, 'Store it (used as default end address)', align=Align.INLINE)
d.comment(0xBEF0, 'Step Y', align=Align.INLINE)
d.comment(0xBEF1, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0xBEF3, 'No: continue copying', align=Align.INLINE)
d.comment(0xBEF5, 'X=&AA: zero-page source for the OSARGS write-back', align=Align.INLINE)
d.comment(0xBEF7, 'Y = file handle', align=Align.INLINE)
d.comment(0xBEF9, 'A=1: OSARGS sub-fn 1 = write sequential file pointer', align=Align.INLINE)
d.comment(0xBEFB, "Set the file's read pointer to the parsed start", align=Align.INLINE)
d.comment(0xBEFE, 'Pull saved cursor offset', align=Align.INLINE)
d.comment(0xBEFF, 'Restore into Y', align=Align.INLINE)
d.comment(0xBF00, 'Read next command-line byte', align=Align.INLINE)
d.comment(0xBF02, 'CR (end of args)?', align=Align.INLINE)
d.comment(0xBF04, "No: there's a second arg -- handle below", align=Align.INLINE)
d.comment(0xBF06, 'Y=1: copy os_text_ptr (2 bytes) to work_ae as a displacement-base hint', align=Align.INLINE)
d.comment(0xBF08, 'Read os_text_ptr+Y', align=Align.INLINE)
d.comment(0xBF0B, 'Save in work_ae+Y', align=Align.INLINE)
d.comment(0xBF0D, 'Step backwards', align=Align.INLINE)
d.comment(0xBF0E, 'Loop while Y >= 0', align=Align.INLINE)
d.comment(0xBF10, 'A=5: OSFILE sub-fn 5 = read catalogue info', align=Align.INLINE)
d.comment(0xBF12, 'X = filename pointer low (work_ae)', align=Align.INLINE)
d.comment(0xBF14, 'Y = filename pointer high (addr_work)', align=Align.INLINE)
d.comment(0xBF16, 'Read load address into work_ae+0..3', align=Align.INLINE)
d.comment(0xBF19, 'Y=2: shift 3 bytes down 2 positions to drop the first 2 bytes (action code + a flag)', align=Align.INLINE)
d.comment(0xBF1B, 'Read source byte', align=Align.INLINE)
d.comment(0xBF1D, 'Y -= 2 (destination)', align=Align.INLINE)
d.comment(0xBF1F, 'Store at destination', align=Align.INLINE)
d.comment(0xBF21, 'Y += 3 to advance to next source', align=Align.INLINE)
d.comment(0xBF22, '(continued)', align=Align.INLINE)
d.comment(0xBF23, '(continued)', align=Align.INLINE)
d.comment(0xBF24, 'Done 6 bytes shifted?', align=Align.INLINE)
d.comment(0xBF26, 'No: continue', align=Align.INLINE)
d.comment(0xBF28, 'Y -= 2: position at high byte of load address', align=Align.INLINE)
d.comment(0xBF2A, 'Read load-address byte at Y', align=Align.INLINE)
d.comment(0xBF2C, 'Is it &FF (signals no real load address)?', align=Align.INLINE)
d.comment(0xBF2E, 'No: have a real load address; add it as displacement', align=Align.INLINE)
d.comment(0xBF30, 'Yes: step back to next higher byte', align=Align.INLINE)
d.comment(0xBF31, 'Loop until Y=0', align=Align.INLINE)
d.comment(0xBF33, 'All four bytes were &FF: zero out the load address', align=Align.INLINE)
d.comment(0xBF35, 'A=0', align=Align.INLINE)
d.comment(0xBF37, 'Zero work_ae+Y', align=Align.INLINE)
d.comment(0xBF39, 'Step backwards', align=Align.INLINE)
d.comment(0xBF3A, 'Loop while Y >= 0', align=Align.INLINE)
d.comment(0xBF3C, 'Always taken (after BPL drops out): skip second-arg path', align=Align.INLINE)
d.comment(0xBF3E, 'Parse end-address argument', align=Align.INLINE)
d.comment(0xBF41, 'Success: continue with displacement-add', align=Align.INLINE)
d.comment(0xBF43, "Parse error: close file then raise 'Bad address'", align=Align.INLINE)
d.comment(0xBF46, "A=&FC: 'Bad address' error code", align=Align.INLINE)
d.comment(0xBF48, 'Raise; never returns', align=Align.INLINE)
d.comment(0xBF53, 'Y=0: start of work_ae', align=Align.INLINE)
d.comment(0xBF55, 'X=4: 4-byte add', align=Align.INLINE)
d.comment(0xBF57, 'Clear C for the add', align=Align.INLINE)
d.comment(0xBD41, 'Open the file (handle stored in ws_page)', align=Align.INLINE)
d.comment(0xBD44, 'X=&14: 21-byte stack buffer for dump line state', align=Align.INLINE)
d.comment(0xBD46, 'A=0: zero-fill', align=Align.INLINE)
d.comment(0xBD48, 'Push zero', align=Align.INLINE)
d.comment(0xBD49, 'Step counter', align=Align.INLINE)
d.comment(0xBD4A, 'Loop while X >= 0 (21 zeros)', align=Align.INLINE)
d.comment(0xBD4C, 'Capture stack pointer for later restore', align=Align.INLINE)
d.comment(0xBD4D, 'Parse address range and validate against file extent', align=Align.INLINE)
d.comment(0xBD50, 'Read low nibble of starting address', align=Align.INLINE)
d.comment(0xBD52, 'Mask high nibble (top 4 bits)', align=Align.INLINE)
d.comment(0xBD54, 'Aligned (high nibble zero): skip the header print', align=Align.INLINE)
d.comment(0xBD56, "Print 'Address: 00 01 ... 0F: ASCII data' header", align=Align.INLINE)
d.comment(0xBD59, 'Test escape and abort if pressed', align=Align.INLINE)
d.comment(0xBD5C, 'A=&FF: count counter starts here so first INC -> 0', align=Align.INLINE)
d.comment(0xBD5E, 'Save counter (-1)', align=Align.INLINE)
d.comment(0xBD60, 'Y = file handle', align=Align.INLINE)
d.comment(0xBD62, 'Read one byte via OSBGET (C set on EOF)', align=Align.INLINE)
d.comment(0xBD65, 'EOF: finish off this line then exit', align=Align.INLINE)
d.comment(0xBD67, 'Increment count counter', align=Align.INLINE)
d.comment(0xBD69, 'Y = current count (also buffer offset)', align=Align.INLINE)
d.comment(0xBD6B, 'Store byte in 16-byte line buffer at (work_ae)+Y', align=Align.INLINE)
d.comment(0xBD6D, 'Done all 16 bytes?', align=Align.INLINE)
d.comment(0xBD6F, 'No: read next byte', align=Align.INLINE)
d.comment(0xBD71, 'C clear: not EOF (clean line)', align=Align.INLINE)
d.comment(0xBD72, 'Save the EOF/clean flag', align=Align.INLINE)
d.comment(0xBD73, 'Reload counter byte', align=Align.INLINE)
d.comment(0xBD75, 'Bit 7 clear (counter is 0..&7F): bytes were read', align=Align.INLINE)
d.comment(0xBD77, 'EOF and no bytes: clean up and exit', align=Align.INLINE)
d.comment(0xBD79, 'Restore one stack byte', align=Align.INLINE)
d.comment(0xBD7A, 'Step', align=Align.INLINE)
d.comment(0xBD7B, 'Loop while X >= 0 (22 pulls)', align=Align.INLINE)
d.comment(0xBD7D, 'Tail-jump to close_ws_file', align=Align.INLINE)
d.comment(0xBD80, 'Y=&10: read displayed-address byte 0', align=Align.INLINE)
d.comment(0xBD82, 'Read low byte', align=Align.INLINE)
d.comment(0xBD84, 'Top nibble', align=Align.INLINE)
d.comment(0xBD86, 'Non-zero: not a 256-byte boundary, skip header', align=Align.INLINE)
d.comment(0xBD88, 'Boundary: print column header', align=Align.INLINE)
d.comment(0xBD8B, 'Y=&13: highest byte of 4-byte address', align=Align.INLINE)
d.comment(0xBD8D, 'Read address byte (highest first)', align=Align.INLINE)
d.comment(0xBD8F, 'Save it (print_hex_byte clobbers A)', align=Align.INLINE)
d.comment(0xBD90, 'Print as 2 hex digits', align=Align.INLINE)
d.comment(0xBD93, 'Restore A', align=Align.INLINE)
d.comment(0xBD94, 'Step backwards', align=Align.INLINE)
d.comment(0xBD95, 'Reached low byte (offset &0F)?', align=Align.INLINE)
d.comment(0xBD97, 'No: continue printing', align=Align.INLINE)
d.comment(0xBD99, 'Y=&10: low byte of address', align=Align.INLINE)
d.comment(0xBD9A, 'Clear C', align=Align.INLINE)
d.comment(0xBD9B, 'Bump address by 16 bytes for next line', align=Align.INLINE)
d.comment(0xBD9D, 'Save C from the add', align=Align.INLINE)
d.comment(0xBD9E, 'Restore C from previous step', align=Align.INLINE)
d.comment(0xBD9F, 'Store updated address byte', align=Align.INLINE)
d.comment(0xBDA1, 'Step Y up', align=Align.INLINE)
d.comment(0xBDA2, 'Read next byte', align=Align.INLINE)
d.comment(0xBDA4, 'Add carry from below', align=Align.INLINE)
d.comment(0xBDA6, 'Save C', align=Align.INLINE)
d.comment(0xBDA7, 'Done all 4 bytes (Y=&14)?', align=Align.INLINE)
d.comment(0xBDA9, 'No: continue propagating', align=Align.INLINE)
d.comment(0xBDAB, 'Restore final C', align=Align.INLINE)
d.comment(0xBDAC, "Print ' : ' separator before hex byte field", align=Align.INLINE)
d.comment(0xBDB2, 'Y=0: start of buffer', align=Align.INLINE)
d.comment(0xBDB4, "X = byte counter (-1 initially, INC'd to 0..&0F)", align=Align.INLINE)
d.comment(0xBDB6, 'Read byte from buffer', align=Align.INLINE)
d.comment(0xBDB8, 'Print as hex + space', align=Align.INLINE)
d.comment(0xBDBB, 'Step buffer offset', align=Align.INLINE)
d.comment(0xBDBC, 'Done all 16?', align=Align.INLINE)
d.comment(0xBDBE, 'Yes: print separator before ASCII field', align=Align.INLINE)
d.comment(0xBDC0, 'Step counter (Y was off-by-one from line read)', align=Align.INLINE)
d.comment(0xBDC1, 'Have a real byte? Print it', align=Align.INLINE)
d.comment(0xBDC3, 'End of partial line: pad with 3 spaces', align=Align.INLINE)
d.comment(0xBDC4, "Print '   ' inline", align=Align.INLINE)
d.comment(0xBDCA, 'NOP -- bit-7 terminator + harmless resume opcode', align=Align.INLINE)
d.comment(0xBDCB, 'Restore Y', align=Align.INLINE)
d.comment(0xBDCC, 'Continue padding the rest of the hex column', align=Align.INLINE)
d.comment(0xBDCF, 'Counter has finished -- step it once more for the ASCII test', align=Align.INLINE)
d.comment(0xBDD0, "Print ': ' inline (ASCII field separator)", align=Align.INLINE)
d.comment(0xBDD5, 'Y=0: rewind to start of line buffer', align=Align.INLINE)
d.comment(0xBDD7, 'Skip 8 padding spaces if needed (advance_x_by_8)', align=Align.INLINE)
d.comment(0xBDDA, 'Read line buffer byte', align=Align.INLINE)
d.comment(0xBDDC, 'Mask off bit 7 (DEL/inverted)', align=Align.INLINE)
d.comment(0xBDDE, "Below ' '? (control char)", align=Align.INLINE)
d.comment(0xBDE0, 'Yes: skip to substitution', align=Align.INLINE)
d.comment(0xBDE2, "Substitute '.' for non-printables", align=Align.INLINE)
d.comment(0xBDE4, 'Compare with DEL', align=Align.INLINE)
d.comment(0xBDE6, "Equal: also non-printable, substitute '.'", align=Align.INLINE)
d.comment(0xBDE8, 'Print the (possibly substituted) character', align=Align.INLINE)
d.comment(0xBDEB, 'Step Y', align=Align.INLINE)
d.comment(0xBDEC, 'Done 16 chars?', align=Align.INLINE)
d.comment(0xBDEE, 'Yes: end this line', align=Align.INLINE)
d.comment(0xBDF0, 'Step counter back', align=Align.INLINE)
d.comment(0xBDF1, 'Loop while X >= 0', align=Align.INLINE)
d.comment(0xBDF3, 'Print newline at end of line', align=Align.INLINE)
d.comment(0xBDF6, 'Restore EOF flag', align=Align.INLINE)
d.comment(0xBDF7, 'EOF: tidy up and exit', align=Align.INLINE)
d.comment(0xBDF9, 'More to dump: jump to next line', align=Align.INLINE)
d.comment(0xBDFC, 'X=&14: balance the loop_pop_stack_buf counter', align=Align.INLINE)
d.comment(0xBDFE, 'Tail-jump to clean up the 21-byte stack buffer and close the file', align=Align.INLINE)
d.comment(0xB4B4, 'Pull saved upper byte of ws_ptr_lo+osword_flag pair', align=Align.INLINE)
d.comment(0xB4B5, 'Save into osword_flag', align=Align.INLINE)
d.comment(0xB4B7, 'Pull lower byte', align=Align.INLINE)
d.comment(0xB4B8, 'Save into ws_ptr_lo', align=Align.INLINE)
d.comment(0xB4BA, 'Push 0 -- placeholder, will be the stacked return marker', align=Align.INLINE)
d.comment(0xB4BC, 'Push it', align=Align.INLINE)
d.comment(0xB4BD, 'ws_ptr_hi base = &84 (start of PS slot table area)', align=Align.INLINE)
d.comment(0xB4BF, 'Save base', align=Align.INLINE)
d.comment(0xB4C1, 'Shift bit 0 of econet_flags into C (saved scan state)', align=Align.INLINE)
d.comment(0xB4C4, 'A=3: PS slot index counter', align=Align.INLINE)
d.comment(0xB4C6, 'Convert slot index to 12-byte-aligned table offset', align=Align.INLINE)
d.comment(0xB4C9, 'Out of range (clamped to 0): all slots scanned', align=Align.INLINE)
d.comment(0xB4CB, 'A /= 2 (shift down)', align=Align.INLINE)
d.comment(0xB4CC, 'A /= 2 again (now slot index * 4 / 4 = slot index)', align=Align.INLINE)
d.comment(0xB4CD, 'X = slot index', align=Align.INLINE)
d.comment(0xB4CE, "Read slot's status byte at workspace[Y]", align=Align.INLINE)
d.comment(0xB4D0, 'Slot empty (0): scan done', align=Align.INLINE)
d.comment(0xB4D2, "Slot is '?' (uninitialised marker)?", align=Align.INLINE)
d.comment(0xB4D4, "Yes: re-init this slot's data", align=Align.INLINE)
d.comment(0xB4D6, 'Step slot index', align=Align.INLINE)
d.comment(0xB4D7, 'Move to A for next iteration', align=Align.INLINE)
d.comment(0xB4D8, 'Loop while X != 0 (wraps when all slots done)', align=Align.INLINE)
d.comment(0xB4DA, 'Save Y (slot table offset)', align=Align.INLINE)
d.comment(0xB4DB, 'Push it', align=Align.INLINE)
d.comment(0xB4DC, "A=&7F: slot status 'busy/active'", align=Align.INLINE)
d.comment(0xB4DE, 'Mark slot active', align=Align.INLINE)
d.comment(0xB4E0, 'Step Y to control byte', align=Align.INLINE)
d.comment(0xB4E1, 'A=&9E: control byte (Master 128 PS-init pattern)', align=Align.INLINE)
d.comment(0xB4E3, 'Store control byte', align=Align.INLINE)
d.comment(0xB4E5, 'A=0: zero-fill the next two bytes', align=Align.INLINE)
d.comment(0xB4E7, 'Write two zeros, advance Y', align=Align.INLINE)
d.comment(0xB4EA, 'Read current ws_ptr_hi', align=Align.INLINE)
d.comment(0xB4EC, 'Store as buffer-link low byte', align=Align.INLINE)
d.comment(0xB4EE, 'Clear C ready for the +3', align=Align.INLINE)
d.comment(0xB4EF, "Save flags so the ADC's C doesn't leak", align=Align.INLINE)
d.comment(0xB4F0, "Bump ws_ptr_hi by 3 (next slot's base)", align=Align.INLINE)
d.comment(0xB4F2, 'Restore flags', align=Align.INLINE)
d.comment(0xB4F3, 'Save updated ws_ptr_hi', align=Align.INLINE)
d.comment(0xB4F5, 'Write buffer page + two &FF sentinels', align=Align.INLINE)
d.comment(0xB4F8, 'Read ws_ptr_hi (now updated)', align=Align.INLINE)
d.comment(0xB4FA, 'Store as second-link byte', align=Align.INLINE)
d.comment(0xB4FC, 'Write another buffer page + two &FF sentinels', align=Align.INLINE)
d.comment(0xB4FF, 'Continue scanning slots', align=Align.INLINE)
d.comment(0xB502, 'Restore bit 0 of econet_flags via ASL (recovers from the LSR at &B4C1)', align=Align.INLINE)
d.comment(0xB505, 'Pull saved ws_ptr_lo', align=Align.INLINE)
d.comment(0xB507, "Push it back (the caller's return-resume sequence)", align=Align.INLINE)
d.comment(0xB508, 'Pull saved osword_flag', align=Align.INLINE)
d.comment(0xB50A, 'Push it back', align=Align.INLINE)
d.comment(0xB50B, 'A=&0A: outer counter', align=Align.INLINE)
d.comment(0xB50D, 'Y=&0A: inner counter', align=Align.INLINE)
d.comment(0xB50E, 'X=&0A: middle counter', align=Align.INLINE)
d.comment(0xB50F, 'Save outer in fs_work_4', align=Align.INLINE)
d.comment(0xB511, 'Decrement inner counter', align=Align.INLINE)
d.comment(0xB512, 'Inner not zero: keep delaying', align=Align.INLINE)
d.comment(0xB514, 'Decrement middle', align=Align.INLINE)
d.comment(0xB515, 'Middle not zero: refresh inner and continue', align=Align.INLINE)
d.comment(0xB517, 'Decrement outer in fs_work_4', align=Align.INLINE)
d.comment(0xB519, 'Outer not zero: another full sweep (~1000 cycles)', align=Align.INLINE)
d.comment(0xB51B, 'Return', align=Align.INLINE)
d.comment(0x9900, 'Test bit 7 of fs_flags (FS-active flag)', align=Align.INLINE)
d.comment(0x9903, 'FS not active: skip the save', align=Align.INLINE)
d.comment(0x9905, 'FS active: store error code at &C009 (last-error byte)', align=Align.INLINE)
d.comment(0x9908, 'Return', align=Align.INLINE)
d.comment(0x9909, "X=8: net_error_lookup_data offset for 'No reply' message", align=Align.INLINE)
d.comment(0x990B, 'Y = message offset within the string table (&9AA6 base)', align=Align.INLINE)
d.comment(0x990E, 'X=0: error-text buffer index', align=Align.INLINE)
d.comment(0x9910, 'Zero the &0100 length byte (length will be filled in later)', align=Align.INLINE)
d.comment(0x9913, 'Read first message byte (the error code)', align=Align.INLINE)
d.comment(0x9916, 'Conditionally save it as last-error', align=Align.INLINE)
d.comment(0x9919, 'Read next message byte', align=Align.INLINE)
d.comment(0x991C, 'Append to error-text buffer at &0101+X', align=Align.INLINE)
d.comment(0x991F, 'Null terminator: message done', align=Align.INLINE)
d.comment(0x9921, 'Step buffer index', align=Align.INLINE)
d.comment(0x9922, 'Step source offset', align=Align.INLINE)
d.comment(0x9923, 'Loop while Y != 0 (Y wraps at 256, not expected)', align=Align.INLINE)
d.comment(0x9925, "Append ' on drive <num>' or similar context", align=Align.INLINE)
d.comment(0x9928, 'A=0: null terminator', align=Align.INLINE)
d.comment(0x992A, 'Store at end of message', align=Align.INLINE)
d.comment(0x992D, 'Tail-jump to dispatch the BRK error', align=Align.INLINE)
d.comment(0x9930, 'Read FS reply status byte at (net_tx_ptr,X)', align=Align.INLINE)
d.comment(0x9932, "Status 'A'? (Acknowledge with no error)", align=Align.INLINE)
d.comment(0x9934, "Not 'A': pass through unchanged", align=Align.INLINE)
d.comment(0x9936, "Substitute 'B' for 'A' (handle ACK as a soft error)", align=Align.INLINE)
d.comment(0x9938, 'Clear V to take the standard mask path', align=Align.INLINE)
d.comment(0x9939, 'Always taken: use the standard masked-error path', align=Align.INLINE)
d.comment(0x993B, 'Read FS reply status byte', align=Align.INLINE)
d.comment(0x993D, 'BIT $always_set_v_byte: force V=1 (extended-error path)', align=Align.INLINE)
d.comment(0x9940, 'Mask to 3 bits (error class 0..7)', align=Align.INLINE)
d.comment(0x9942, 'Save error class on stack', align=Align.INLINE)
d.comment(0x9943, "Class 2 = 'station-related' family?", align=Align.INLINE)
d.comment(0x9945, 'No: build a simple one-line error', align=Align.INLINE)
d.comment(0x9947, 'Class 2 yes: save flags so we can branch on V later', align=Align.INLINE)
d.comment(0x9948, 'X = error class (=2)', align=Align.INLINE)
d.comment(0x9949, 'Y = lookup-table offset', align=Align.INLINE)
d.comment(0x994C, 'Read first message byte (error code)', align=Align.INLINE)
d.comment(0x994F, 'Conditionally save it', align=Align.INLINE)
d.comment(0x9952, 'X=0: text-buffer index', align=Align.INLINE)
d.comment(0x9954, 'Zero length byte', align=Align.INLINE)
d.comment(0x9957, 'Read message byte', align=Align.INLINE)
d.comment(0x995A, 'Append to buffer', align=Align.INLINE)
d.comment(0x995D, 'Null terminator -- station message done', align=Align.INLINE)
d.comment(0x9963, "Append ' on drive <num>' suffix", align=Align.INLINE)
d.comment(0x9966, 'Restore the saved class flags', align=Align.INLINE)
d.comment(0x9967, "V was set: use 'not listening' suffix", align=Align.INLINE)
d.comment(0x9969, "A=&A4: 'station <n> not available' error code", align=Align.INLINE)
d.comment(0x996B, 'Save the alternative error code', align=Align.INLINE)
d.comment(0x996E, 'Patch error-text buffer length byte', align=Align.INLINE)
d.comment(0x9971, 'Y=&0B: lookup index for the listening-station suffix', align=Align.INLINE)
d.comment(0x9973, 'Always taken (Y is non-zero); jump to load_suffix_offset', align=Align.INLINE)
d.comment(0x9975, "V was clear: 'not listening' suffix variant", align=Align.INLINE)
d.comment(0x9977, 'Read suffix offset from lookup', align=Align.INLINE)
d.comment(0x997A, 'Y = suffix offset', align=Align.INLINE)
d.comment(0x997B, 'Read suffix byte', align=Align.INLINE)
d.comment(0x997E, 'Append', align=Align.INLINE)
d.comment(0x9981, 'Null: suffix done', align=Align.INLINE)
d.comment(0x9983, 'Step Y', align=Align.INLINE)
d.comment(0x9984, 'Step X', align=Align.INLINE)
d.comment(0x9985, 'Loop while X != 0 (max 255 chars)', align=Align.INLINE)
d.comment(0x9987, 'Always taken (Z still set from BEQ): final terminator check', align=Align.INLINE)
d.comment(0x9989, 'X = error class', align=Align.INLINE)
d.comment(0x998A, 'Y = lookup-table offset', align=Align.INLINE)
d.comment(0x998D, 'X=0: buffer index', align=Align.INLINE)
d.comment(0x998F, 'Zero length', align=Align.INLINE)
d.comment(0x9992, 'Read first message byte (error code)', align=Align.INLINE)
d.comment(0x9995, 'Conditionally save it', align=Align.INLINE)
d.comment(0x9998, 'Read next message byte', align=Align.INLINE)
d.comment(0x999B, 'Append to buffer', align=Align.INLINE)
d.comment(0x999E, 'Null terminator -> dispatch', align=Align.INLINE)
d.comment(0x99A0, 'Step Y', align=Align.INLINE)
d.comment(0x99A1, 'Step X', align=Align.INLINE)
d.comment(0x99A2, 'Loop while X != 0', align=Align.INLINE)
d.comment(0xAFA6, "X = caller's TX-ptr low byte", align=Align.INLINE)
d.comment(0xAFA8, "Y = caller's TX-ptr high byte", align=Align.INLINE)
d.comment(0xAFAA, 'Save A (the disconnect status to send)', align=Align.INLINE)
d.comment(0xAFAB, 'Test if A=0 (broadcast disconnect)', align=Align.INLINE)
d.comment(0xAFAD, 'Yes: skip the per-station scan', align=Align.INLINE)
d.comment(0xAFAF, 'X=&FF: scan counter -- INX in loop bumps to 0', align=Align.INLINE)
d.comment(0xAFB1, 'Y=A: status code (also used as station-table key)', align=Align.INLINE)
d.comment(0xAFB2, 'Restore status into A for the compare', align=Align.INLINE)
d.comment(0xAFB3, 'Step station-table index', align=Align.INLINE)
d.comment(0xAFB4, 'Compare with table[X] at &C230 (per-station status)', align=Align.INLINE)
d.comment(0xAFB7, 'Match: verify station address still matches', align=Align.INLINE)
d.comment(0xAFB9, 'Reached end of 16-slot table?', align=Align.INLINE)
d.comment(0xAFBB, 'No: keep scanning', align=Align.INLINE)
d.comment(0xAFBD, 'All slots tested, no match: A=0', align=Align.INLINE)
d.comment(0xAFBF, 'Always taken: jump to send-status', align=Align.INLINE)
d.comment(0xAFC1, 'Y = matching index', align=Align.INLINE)
d.comment(0xAFC2, 'Verify station/network at this slot still matches caller', align=Align.INLINE)
d.comment(0xAFC5, 'Mismatch: station moved, keep scanning', align=Align.INLINE)
d.comment(0xAFC7, 'Read connection-active flag at &C260+X', align=Align.INLINE)
d.comment(0xAFCA, 'Mask to bit 0 (active flag)', align=Align.INLINE)
d.comment(0xAFCC, 'Y=0: TX[0] = control byte', align=Align.INLINE)
d.comment(0xAFCE, 'OR active-flag bit into the status', align=Align.INLINE)
d.comment(0xAFD0, 'Save the combined status', align=Align.INLINE)
d.comment(0xAFD1, 'Write it to TX[0]', align=Align.INLINE)
d.comment(0xAFD3, 'Send the disconnect packet via four-way handshake', align=Align.INLINE)
d.comment(0xAFD6, 'A=&FF: sentinel', align=Align.INLINE)
d.comment(0xAFD8, 'Y=8: TX[8] / TX[9] = packet trailer markers', align=Align.INLINE)
d.comment(0xAFDA, 'Write &FF at TX[8]', align=Align.INLINE)
d.comment(0xAFDC, 'Step Y', align=Align.INLINE)
d.comment(0xAFDD, 'Write &FF at TX[9]', align=Align.INLINE)
d.comment(0xAFDF, 'Pull the saved status', align=Align.INLINE)
d.comment(0xAFE0, 'Move into X for the test', align=Align.INLINE)
d.comment(0xAFE1, 'Y=&D1: control byte for ack-mode TXCB[1]', align=Align.INLINE)
d.comment(0xAFE3, "Pull caller's original A again (was double-saved)", align=Align.INLINE)
d.comment(0xAFE4, 'Push it back', align=Align.INLINE)
d.comment(0xAFE5, 'A=0: skip the override', align=Align.INLINE)
d.comment(0xAFE7, 'Non-zero: use Y=&90 (FS reply port instead)', align=Align.INLINE)
d.comment(0xAFE9, 'Move chosen control/port into A', align=Align.INLINE)
d.comment(0xAFEA, 'Y=1: TX[1] is the port byte', align=Align.INLINE)
d.comment(0xAFEC, 'Write to TX[1]', align=Align.INLINE)
d.comment(0xAFEE, 'Move saved status into A', align=Align.INLINE)
d.comment(0xAFEF, 'Y=0: TX[0] for ack poll', align=Align.INLINE)
d.comment(0xAFF0, "Push the status (we'll EOR with reply below)", align=Align.INLINE)
d.comment(0xAFF1, 'A=&7F: marker pattern', align=Align.INLINE)
d.comment(0xAFF3, 'Write to TX[0]', align=Align.INLINE)
d.comment(0xAFF5, 'Wait for the TX/RX flip', align=Align.INLINE)
d.comment(0xAFF8, 'Pull saved status (peek without consuming)', align=Align.INLINE)
d.comment(0xAFF9, 'Push it back', align=Align.INLINE)
d.comment(0xAFFA, 'EOR with TX[0]: zero iff reply matches saved', align=Align.INLINE)
d.comment(0xAFFC, 'Rotate result; C set if bit 0 differs', align=Align.INLINE)
d.comment(0xAFFD, 'C set: keep waiting', align=Align.INLINE)
d.comment(0xAFFF, 'Discard saved status', align=Align.INLINE)
d.comment(0xB000, "Discard caller's saved A", align=Align.INLINE)
d.comment(0xB001, 'Return', align=Align.INLINE)
d.comment(0xA3FF, "Y=&6F: net_rx_ptr offset for the 'inline' handle byte", align=Align.INLINE)
d.comment(0xA401, 'Read handle byte directly from RX buffer', align=Align.INLINE)
d.comment(0xA403, 'C clear: read-handle path -- store directly to PB', align=Align.INLINE)
d.comment(0xA405, 'Convert PB pointer to workspace table offset', align=Align.INLINE)
d.comment(0xA408, 'Out of range: return zero (uninitialised)', align=Align.INLINE)
d.comment(0xA40A, 'Read workspace handle byte', align=Align.INLINE)
d.comment(0xA40C, "Slot marked '?' (uninitialised)?", align=Align.INLINE)
d.comment(0xA40E, 'Has a real handle: keep it and store', align=Align.INLINE)
d.comment(0xA410, 'Force result to zero (uninitialised marker)', align=Align.INLINE)
d.comment(0xA412, 'Write into PB[0] (handle return slot)', align=Align.INLINE)
d.comment(0xA414, 'Return', align=Align.INLINE)
d.comment(0xA415, 'Convert PB pointer to workspace table offset', align=Align.INLINE)
d.comment(0xA418, 'Out of range: mark as uninitialised', align=Align.INLINE)
d.comment(0xA41A, 'Shift bit 0 of fs_flags into C (save state)', align=Align.INLINE)
d.comment(0xA41D, 'Read PB[0] (the handle to close)', align=Align.INLINE)
d.comment(0xA41F, 'Shift bit 7 of A into C', align=Align.INLINE)
d.comment(0xA420, 'Restore C into bit 0 of fs_flags', align=Align.INLINE)
d.comment(0xA423, 'Return; the close action is dispatched elsewhere based on the saved C state', align=Align.INLINE)
d.comment(0xA424, 'Save bit 0 of econet_flags', align=Align.INLINE)
d.comment(0xA427, "A='?': uninitialised marker", align=Align.INLINE)
d.comment(0xA429, "Write '?' to workspace[Y] (the slot is now free)", align=Align.INLINE)
d.comment(0xA42B, 'Restore bit 0 of econet_flags', align=Align.INLINE)
d.comment(0xA42E, 'Return', align=Align.INLINE)
d.comment(0x97CD, "Save flags so caller's V/C survive the receive", align=Align.INLINE)
d.comment(0x97CE, 'Set up open RX on port &90 for the FS reply (TXCB[0] = &90, ctrl = &7F)', align=Align.INLINE)
d.comment(0x97D1, 'Wait for the reply via the 3-level stack timer', align=Align.INLINE)
d.comment(0x97D4, "Restore caller's flags", align=Align.INLINE)
d.comment(0x97D5, 'Step Y to next reply byte', align=Align.INLINE)
d.comment(0x97D6, 'Read reply byte at txcb_start+Y', align=Align.INLINE)
d.comment(0x97D8, 'Stash for the dispatch tests below', align=Align.INLINE)
d.comment(0x97D9, 'Zero terminates: return', align=Align.INLINE)
d.comment(0x97DB, "V clear (caller's V): use code as-is", align=Align.INLINE)
d.comment(0x97DD, 'V set: shift the code by +&2A (extended-error mapping)', align=Align.INLINE)
d.comment(0x97DF, 'Non-zero: dispatch as an error', align=Align.INLINE)
d.comment(0x97E1, 'Return', align=Align.INLINE)
d.comment(0x97E2, "Pull caller's pushed return state", align=Align.INLINE)
d.comment(0x97E3, "X=&C0: 'remote disconnect' status", align=Align.INLINE)
d.comment(0x97E5, 'Step Y past the disconnect byte', align=Align.INLINE)
d.comment(0x97E6, 'Send disconnect notification to remote', align=Align.INLINE)
d.comment(0x97E9, 'C clear (success): continue scanning replies', align=Align.INLINE)
d.comment(0x97EB, 'Save the error code into &C009', align=Align.INLINE)
d.comment(0x97EE, 'Read FS state byte at &C007', align=Align.INLINE)
d.comment(0x97F1, 'Save flags so we can branch later', align=Align.INLINE)
d.comment(0x97F2, 'FS state non-zero: data-loss check needed', align=Align.INLINE)
d.comment(0x97F4, 'Reply was &BF (special: not a real error)?', align=Align.INLINE)
d.comment(0x97F6, 'No: build error block', align=Align.INLINE)
d.comment(0x97F8, "A=&40: 'channel-active' bitmask", align=Align.INLINE)
d.comment(0x97FA, 'Push it onto the OR-accumulator', align=Align.INLINE)
d.comment(0x97FB, "Clear the FS-active bit (we're losing the connection)", align=Align.INLINE)
d.comment(0x97FE, 'X=&F0: scan from channel offset &F0 upwards', align=Align.INLINE)
d.comment(0x9800, 'Pull current OR accumulator', align=Align.INLINE)
d.comment(0x9801, 'OR with channel status byte at &C1C8+X', align=Align.INLINE)
d.comment(0x9804, 'Push back updated accumulator', align=Align.INLINE)
d.comment(0x9805, 'Reload channel byte', align=Align.INLINE)
d.comment(0x9808, 'Mask to top 2 bits (preserve TX/RX state)', align=Align.INLINE)
d.comment(0x980A, 'Write back trimmed status', align=Align.INLINE)
d.comment(0x980D, 'Step channel index', align=Align.INLINE)
d.comment(0x980E, 'Loop while X bit 7 set (covers &F0..&FF)', align=Align.INLINE)
d.comment(0x9810, 'Clear the FS state byte (no longer active)', align=Align.INLINE)
d.comment(0x9813, 'Force-close all client channels', align=Align.INLINE)
d.comment(0x9816, 'Pull final OR accumulator', align=Align.INLINE)
d.comment(0x9817, 'Bit 0 (was bit 6 of any &40 byte) -> C', align=Align.INLINE)
d.comment(0x9818, 'Any channel was active: skip the warning', align=Align.INLINE)
d.comment(0x981A, "No active channels were lost: print 'Data Lost' warning via inline string", align=Align.INLINE)
d.comment(0x9827, 'Reload error code from &C009', align=Align.INLINE)
d.comment(0x982A, 'Restore saved flags (was bit 7 of fs_flags)', align=Align.INLINE)
d.comment(0x982B, 'Z set (no error): build the error block anyway', align=Align.INLINE)
d.comment(0x982D, "Pull caller's saved return state (3 bytes from PHP earlier)", align=Align.INLINE)
d.comment(0x9830, 'Return -- caller dispatched on a non-error reply', align=Align.INLINE)
d.comment(0x9831, 'Y=1: skip past the leading TXCB control byte', align=Align.INLINE)
d.comment(0x9833, 'Error code below &A8 (extended)?', align=Align.INLINE)
d.comment(0x9835, 'No (>= &A8): proceed to copy', align=Align.INLINE)
d.comment(0x9837, 'Yes: clamp to &A8 (truncate range)', align=Align.INLINE)
d.comment(0x9839, 'Write clamped code back into TXCB', align=Align.INLINE)
d.comment(0x983B, 'Y=&FF: INY in loop bumps to 0', align=Align.INLINE)
d.comment(0x983D, 'Step Y', align=Align.INLINE)
d.comment(0x983E, 'Read TXCB byte (error block content)', align=Align.INLINE)
d.comment(0x9840, 'Copy to BRK error block at &0100+Y', align=Align.INLINE)
d.comment(0x9843, 'EOR with CR; Z set when we just copied the terminator', align=Align.INLINE)
d.comment(0x9845, 'Not yet at CR: continue copying', align=Align.INLINE)
d.comment(0x9847, 'Write the CR terminator (Z still set so A=0; ensures cleanly terminated)', align=Align.INLINE)
d.comment(0x984A, 'Step Y back so it points at the CR position', align=Align.INLINE)
d.comment(0x984B, 'Move Y into A for the BRK', align=Align.INLINE)
d.comment(0x984C, 'Move Y into X (caller convention)', align=Align.INLINE)
d.comment(0x984D, 'Tail-jump into the BRK-dispatch error path', align=Align.INLINE)
d.comment(0x8A8F, 'Service call &24 (Dynamic Workspace requirements)?', align=Align.INLINE)
d.comment(0x8A91, 'No: skip ADLC check', align=Align.INLINE)
d.comment(0x8A93, 'Read ADLC status register 1', align=Align.INLINE)
d.comment(0x8A96, 'Mask relevant status bits', align=Align.INLINE)
d.comment(0x8A98, 'Non-zero: ADLC absent, set flag', align=Align.INLINE)
d.comment(0x8A9A, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0x8A9D, 'Set carry to mark ADLC absent', align=Align.INLINE)
d.comment(0x8A9E, 'Rotate carry into bit 7 of slot flag', align=Align.INLINE)
d.comment(0x8AA1, 'Load ROM slot flag byte', align=Align.INLINE)
d.comment(0x8AA4, 'Shift bit 7 (ADLC absent) into carry', align=Align.INLINE)
d.comment(0x8AA5, 'Restore service call number', align=Align.INLINE)
d.comment(0x8AA6, 'ADLC present: continue dispatch', align=Align.INLINE)
d.comment(0x8AA8, 'ADLC absent: decline service, return', align=Align.INLINE)
d.comment(0x8AA9, 'Transfer service number to X', align=Align.INLINE)
d.comment(0x8AAA, 'Save current service state', align=Align.INLINE)
d.comment(0x8AAC, 'Push old state', align=Align.INLINE)
d.comment(0x8AAD, 'Restore service number to A', align=Align.INLINE)
d.comment(0x8AAE, 'Store as current service state', align=Align.INLINE)
d.comment(0x8AB0, 'Service < 13?', align=Align.INLINE)
d.comment(0x8AB2, 'Yes: use as dispatch index directly', align=Align.INLINE)
d.comment(0x8AB4, 'Subtract 5 (map 13-17 to 8-12)', align=Align.INLINE)
d.comment(0x8AB6, 'Mapped value = 13? (original was 18)', align=Align.INLINE)
d.comment(0x8AB8, 'Yes: valid service 18 (FS select)', align=Align.INLINE)
d.comment(0x8ACE, 'Unknown service: set index to 0', align=Align.INLINE)
d.comment(0x8AD0, 'Transfer dispatch index to X', align=Align.INLINE)
d.comment(0x8AD1, 'Index 0: unhandled service, skip', align=Align.INLINE)
d.comment(0x8AD3, 'Save current workspace page', align=Align.INLINE)
d.comment(0x8AD5, 'Push old page', align=Align.INLINE)
d.comment(0x8AD6, 'Set workspace page from Y parameter', align=Align.INLINE)
d.comment(0x8AD8, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8AD9, 'Y=0 for dispatch offset', align=Align.INLINE)
d.comment(0x8ADB, 'Dispatch to service handler via table', align=Align.INLINE)
d.comment(0x8ADE, 'Restore old workspace page', align=Align.INLINE)
d.comment(0x8ADF, 'Store it back', align=Align.INLINE)
d.comment(0x8AE1, 'Get service state (return code)', align=Align.INLINE)
d.comment(0x8AE3, 'Restore old service state', align=Align.INLINE)
d.comment(0x8AE4, 'Store it back', align=Align.INLINE)
d.comment(0x8AE6, 'Transfer return code to A', align=Align.INLINE)
d.comment(0x8AE7, 'Restore ROM slot to X', align=Align.INLINE)
d.comment(0x8AE9, 'Return to MOS', align=Align.INLINE)
d.comment(0x8AEA, 'Offset 0 in receive block', align=Align.INLINE)
d.comment(0x8AEC, 'Load remote operation flag', align=Align.INLINE)
d.comment(0x8AEE, 'Zero: already off, skip to cleanup', align=Align.INLINE)
d.comment(0x8AF0, 'A=0', align=Align.INLINE)
d.comment(0x8AF3, 'Clear remote operation flag', align=Align.INLINE)
d.comment(0x8AF6, 'OSBYTE &C9: keyboard disable', align=Align.INLINE)
d.comment(0x8AFB, 'A=&0A: workspace init parameter', align=Align.INLINE)
d.comment(0x8AFD, 'Initialise workspace area', align=Align.INLINE)
d.comment(0x8B00, 'Save X in workspace', align=Align.INLINE)
d.comment(0x8B02, 'A=&CE: start of key range', align=Align.INLINE)
d.comment(0x8B04, 'Restore X from workspace', align=Align.INLINE)
d.comment(0x8B06, 'Y=&7F: OSBYTE scan parameter', align=Align.INLINE)
d.comment(0x8B08, 'OSBYTE: scan keyboard', align=Align.INLINE)
d.comment(0x8B0B, 'Advance to next key code', align=Align.INLINE)
d.comment(0x8B0D, 'Reached &D0?', align=Align.INLINE)
d.comment(0x8B0F, 'No: loop back (scan &CE and &CF)', align=Align.INLINE)
d.comment(0x8B11, 'A=0', align=Align.INLINE)
d.comment(0x8B13, 'Clear service state', align=Align.INLINE)
d.comment(0x8B15, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B17, 'Return', align=Align.INLINE)
d.comment(0x8B18, 'Save A', align=Align.INLINE)
d.comment(0x8B19, 'Copy OS text pointer low', align=Align.INLINE)
d.comment(0x8B1B, 'to fs_crc_lo', align=Align.INLINE)
d.comment(0x8B1D, 'Copy OS text pointer high', align=Align.INLINE)
d.comment(0x8B1F, 'to fs_crc_hi', align=Align.INLINE)
d.comment(0x8B21, 'Restore A', align=Align.INLINE)
d.comment(0x8B22, 'Return', align=Align.INLINE)
d.comment(0x8B23, 'Get workspace page for this ROM slot', align=Align.INLINE)
d.comment(0x8B26, 'Store as high byte of load address', align=Align.INLINE)
d.comment(0x8B28, 'A=0', align=Align.INLINE)
d.comment(0x8B2A, 'Clear low byte of load address', align=Align.INLINE)
d.comment(0x8B2C, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8B2D, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8B2F, 'Add byte to running checksum', align=Align.INLINE)
d.comment(0x8B31, 'Decrement index', align=Align.INLINE)
d.comment(0x8B32, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8B34, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8B36, 'Compare with stored checksum', align=Align.INLINE)
d.comment(0x8B4D, 'Test fs_flags bit 7 (ANFS active)', align=Align.INLINE)
d.comment(0x8B50, 'Already active: tail-RTS via shared exit', align=Align.INLINE)
d.comment(0x8B52, 'Auto-select ANFS via the *NFS handler', align=Align.INLINE)
d.comment(0x8B55, 'Z=1 (A=0): selection succeeded', align=Align.INLINE)
d.comment(0x8B57, "Otherwise raise 'net checksum' error", align=Align.INLINE)
d.comment(0x8B60, 'Call FSCV with A=6 (new FS)', align=Align.INLINE)
d.comment(0x8B63, 'Y=9: end of FS context block', align=Align.INLINE)
d.comment(0x8B65, 'Load byte from receive block', align=Align.INLINE)
d.comment(0x8B67, 'Store into FS workspace', align=Align.INLINE)
d.comment(0x8B6A, 'Decrement index', align=Align.INLINE)
d.comment(0x8B6B, 'Reached offset 1?', align=Align.INLINE)
d.comment(0x8B6D, 'No: continue copying', align=Align.INLINE)
d.comment(0x8B6F, 'Shift bit 7 of FS flags into carry', align=Align.INLINE)
d.comment(0x8B72, 'Clear carry', align=Align.INLINE)
d.comment(0x8B73, 'Clear bit 7 of FS flags', align=Align.INLINE)
d.comment(0x8B76, 'Y=&0D: vector table size - 1', align=Align.INLINE)
d.comment(0x8B78, 'Load FS vector address', align=Align.INLINE)
d.comment(0x8B7B, 'Store into FILEV vector table', align=Align.INLINE)
d.comment(0x8B7E, 'Decrement index', align=Align.INLINE)
d.comment(0x8B7F, 'Loop until all vectors installed', align=Align.INLINE)
d.comment(0x8B81, 'Initialise ADLC and NMI workspace', align=Align.INLINE)
d.comment(0x8B84, 'Y=&1B: extended vector offset', align=Align.INLINE)
d.comment(0x8B86, 'X=7: two more vectors to set up', align=Align.INLINE)
d.comment(0x8B88, 'Set up extended vectors', align=Align.INLINE)
d.comment(0x8B8B, 'A=0', align=Align.INLINE)
d.comment(0x8B8D, 'Clear FS state byte', align=Align.INLINE)
d.comment(0x8B90, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B93, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B96, 'Clear receive attribute byte', align=Align.INLINE)
d.comment(0x8B99, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B9C, 'Set up workspace pointers', align=Align.INLINE)
d.comment(0x8B9F, 'Initialise FS state', align=Align.INLINE)
d.comment(0x8BA2, 'Y=&77: workspace block size - 1', align=Align.INLINE)
d.comment(0x8BA4, 'Load byte from source workspace', align=Align.INLINE)
d.comment(0x8BA6, 'Store to page &10 shadow copy', align=Align.INLINE)
d.comment(0x8BA9, 'Decrement index', align=Align.INLINE)
d.comment(0x8BAA, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8BAC, 'A=&80: FS selected flag', align=Align.INLINE)
d.comment(0x8BBB, 'X=&35: NFS command table offset', align=Align.INLINE)
d.comment(0x8BBD, 'Print help for NFS commands', align=Align.INLINE)
d.comment(0x8BC0, 'X=0: utility command table offset', align=Align.INLINE)
d.comment(0x8BC4, 'X=&35: NFS command table offset', align=Align.INLINE)
d.comment(0x8BC6, 'V clear: take newline-only path (skip version header)', align=Align.INLINE)
d.comment(0x8BCF, 'Clear overflow flag', align=Align.INLINE)
d.comment(0x8BD5, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0x8BD6, 'Push it', align=Align.INLINE)
d.comment(0x8BD7, 'Save processor status', align=Align.INLINE)
d.comment(0x8BD8, 'Load byte from command table', align=Align.INLINE)
d.comment(0x8BDB, 'Bit 7 clear: valid entry, continue', align=Align.INLINE)
d.comment(0x8BDD, 'End of table: finish up', align=Align.INLINE)
d.comment(0x8BE0, 'Print two-space indent', align=Align.INLINE)
d.comment(0x8BED, 'Advance table pointer', align=Align.INLINE)
d.comment(0x8BEE, 'Decrement padding counter', align=Align.INLINE)
d.comment(0x8BEF, 'Load next character', align=Align.INLINE)
d.comment(0x8BF2, 'Bit 7 clear: more chars, continue', align=Align.INLINE)
d.comment(0x8BF4, 'Pad with spaces', align=Align.INLINE)
d.comment(0x8BF9, 'Decrement remaining pad count', align=Align.INLINE)
d.comment(0x8BFA, 'More padding needed: loop', align=Align.INLINE)
d.comment(0x8BFC, 'Load syntax descriptor byte', align=Align.INLINE)
d.comment(0x8BFF, 'Mask to get syntax string index', align=Align.INLINE)
d.comment(0x8C01, 'Use index as Y', align=Align.INLINE)
d.comment(0x8C02, 'Look up syntax string offset', align=Align.INLINE)
d.comment(0x8C05, 'Transfer offset to Y', align=Align.INLINE)
d.comment(0x8C06, 'Advance to next character', align=Align.INLINE)
d.comment(0x8C07, 'Load syntax string character', align=Align.INLINE)
d.comment(0x8C0A, 'Zero terminator: end of syntax', align=Align.INLINE)
d.comment(0x8C0C, 'Carriage return: line continuation', align=Align.INLINE)
d.comment(0x8C0E, 'No: print the character', align=Align.INLINE)
d.comment(0x8C10, 'Handle line wrap in syntax output', align=Align.INLINE)
d.comment(0x8C13, 'Continue with next character', align=Align.INLINE)
d.comment(0x8C19, 'Continue with next character', align=Align.INLINE)
d.comment(0x8C1F, 'X += 3: skip syntax descriptor and address', align=Align.INLINE)
d.comment(0x8C20, '(continued)', align=Align.INLINE)
d.comment(0x8C21, '(continued)', align=Align.INLINE)
d.comment(0x8C22, 'Loop for next command', align=Align.INLINE)
d.comment(0x8C25, 'Restore processor status', align=Align.INLINE)
d.comment(0x8C26, 'Restore Y', align=Align.INLINE)
d.comment(0x8C27, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8C28, 'Return', align=Align.INLINE)
d.comment(0x8C29, 'Read output stream type', align=Align.INLINE)
d.comment(0x8C2C, 'Stream 0 (VDU): no wrapping', align=Align.INLINE)
d.comment(0x8C2E, 'Stream 3 (printer)?', align=Align.INLINE)
d.comment(0x8C30, 'Yes: no wrapping', align=Align.INLINE)
d.comment(0x8C36, 'Y=&0B: indent width - 1', align=Align.INLINE)
d.comment(0x8C38, 'Space character', align=Align.INLINE)
d.comment(0x8C3D, 'Decrement indent counter', align=Align.INLINE)
d.comment(0x8C3E, 'More spaces needed: loop', align=Align.INLINE)
d.comment(0x8C41, 'Return', align=Align.INLINE)
d.comment(0x8C42, 'X=0: start of utility command table', align=Align.INLINE)
d.comment(0x8C44, 'Get command line offset', align=Align.INLINE)
d.comment(0x8C46, 'Save text pointer to fs_crc', align=Align.INLINE)
d.comment(0x8C49, 'Try to match command in table', align=Align.INLINE)
d.comment(0x8C4C, 'No match: return to caller', align=Align.INLINE)
d.comment(0x8C4E, 'Match found: execute command', align=Align.INLINE)
d.comment(0x8C51, 'Check for credits Easter egg', align=Align.INLINE)
d.comment(0x8C54, 'Get command line offset', align=Align.INLINE)
d.comment(0x8C56, 'Load character at offset', align=Align.INLINE)
d.comment(0x8C58, 'Is it CR (bare *HELP)?', align=Align.INLINE)
d.comment(0x8C5A, 'No: check for specific topic', align=Align.INLINE)
d.comment(0x8C5C, 'Print version string', align=Align.INLINE)
d.comment(0x8C5F, 'X=&91: start of help command list', align=Align.INLINE)
d.comment(0x8C61, 'Print command list from table', align=Align.INLINE)
d.comment(0x8C64, 'Restore Y (command line offset)', align=Align.INLINE)
d.comment(0x8C66, 'Return unclaimed', align=Align.INLINE)
d.comment(0x8C67, 'Test for topic match (sets flags)', align=Align.INLINE)
d.comment(0x8C6A, "Is first char '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8C6C, 'No: try topic-specific help', align=Align.INLINE)
d.comment(0x8C6E, "'.' found: show full command list", align=Align.INLINE)
d.comment(0x8C71, 'Save text pointer to fs_crc', align=Align.INLINE)
d.comment(0x8C74, 'Save flags', align=Align.INLINE)
d.comment(0x8C75, 'X=&91: help command table start', align=Align.INLINE)
d.comment(0x8C77, 'Try to match help topic in table', align=Align.INLINE)
d.comment(0x8C7A, 'No match: try next topic', align=Align.INLINE)
d.comment(0x8C7C, 'Restore flags', align=Align.INLINE)
d.comment(0x8C7D, 'Push return address high (&8C)', align=Align.INLINE)
d.comment(0x8C7F, 'Push it for RTS dispatch', align=Align.INLINE)
d.comment(0x8C80, 'Push return address low (&74)', align=Align.INLINE)
d.comment(0x8C82, 'Push it for RTS dispatch', align=Align.INLINE)
d.comment(0x8C83, 'Load dispatch address high', align=Align.INLINE)
d.comment(0x8C86, 'Push dispatch high for RTS', align=Align.INLINE)
d.comment(0x8C87, 'Load dispatch address low', align=Align.INLINE)
d.comment(0x8C8A, 'Push dispatch low for RTS', align=Align.INLINE)
d.comment(0x8C8B, 'Dispatch via RTS (returns to &8C80)', align=Align.INLINE)
d.comment(0x8C8C, 'Restore flags from before match', align=Align.INLINE)
d.comment(0x8C8D, 'End of command line?', align=Align.INLINE)
d.comment(0x8C8F, 'No: try matching next topic', align=Align.INLINE)
d.comment(0x8C93, 'Print version string via inline', align=Align.INLINE)
d.comment(0x8CBB, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8CBC, 'Return with page in A and Y', align=Align.INLINE)
d.comment(0x8CBD, 'Get workspace page for ROM slot', align=Align.INLINE)
d.comment(0x8CC0, 'Store page in nfs_temp', align=Align.INLINE)
d.comment(0x8CC2, 'A=0', align=Align.INLINE)
d.comment(0x8CC4, 'Clear low byte of pointer', align=Align.INLINE)
d.comment(0x8CC6, 'Return', align=Align.INLINE)
d.comment(0x8CC7, 'OSBYTE &7A: scan keyboard from key 16', align=Align.INLINE)
d.comment(0x8CCD, 'No key pressed: select Net FS', align=Align.INLINE)
d.comment(0x8CCF, 'Key &19 (N)?', align=Align.INLINE)
d.comment(0x8CD1, 'Yes: write key state and boot', align=Align.INLINE)
d.comment(0x8CD3, "EOR with &55: maps to zero if 'N'", align=Align.INLINE)
d.comment(0x8CD5, 'Not N key: return unclaimed', align=Align.INLINE)
d.comment(0x8CD8, 'OSBYTE &78: write keys pressed', align=Align.INLINE)
d.comment(0x8CDD, 'Select NFS as current filing system', align=Align.INLINE)
d.comment(0x8CE4, 'Print station number', align=Align.INLINE)
d.comment(0x8CEA, 'Get workspace page', align=Align.INLINE)
d.comment(0x8CEC, 'Non-zero: already initialised, return', align=Align.INLINE)
d.comment(0x8CEE, 'Load boot flags', align=Align.INLINE)
d.comment(0x8CF1, 'Set bit 2 (auto-boot in progress)', align=Align.INLINE)
d.comment(0x8CF3, 'Store updated boot flags', align=Align.INLINE)
d.comment(0x8CF6, 'X=&1C: boot filename address low', align=Align.INLINE)
d.comment(0x8CF8, 'Y=&8D: boot filename address high', align=Align.INLINE)
d.comment(0x8CFA, 'Execute boot file', align=Align.INLINE)
d.comment(0x8CFF, 'Tail-jump via FSCV vector (filing-system change service)', align=Align.INLINE)
d.comment(0x8D02, 'X=&0F: service 15 (vectors claimed)', align=Align.INLINE)
d.comment(0x8D04, "A=&8F: OSBYTE 'Issue paged-ROM service request'", align=Align.INLINE)
d.comment(0x8CFD, 'A=6: notify new filing system', align=Align.INLINE)
d.comment(0x8D26, 'X=5: start of credits keyword', align=Align.INLINE)
d.comment(0x8D28, 'Load character from command line', align=Align.INLINE)
d.comment(0x8D2A, 'Compare with credits keyword', align=Align.INLINE)
d.comment(0x8D2D, 'Mismatch: check if keyword complete', align=Align.INLINE)
d.comment(0x8D2F, 'Advance command line pointer', align=Align.INLINE)
d.comment(0x8D30, 'Advance keyword pointer', align=Align.INLINE)
d.comment(0x8D31, 'Continue matching', align=Align.INLINE)
d.comment(0x8D33, 'Reached end of keyword (X=&0D)?', align=Align.INLINE)
d.comment(0x8D35, 'No: keyword not fully matched, return', align=Align.INLINE)
d.comment(0x8D37, 'X=0: start of credits text', align=Align.INLINE)
d.comment(0x8D39, 'Load character from credits string', align=Align.INLINE)
d.comment(0x8D3C, 'Zero terminator: done printing', align=Align.INLINE)
d.comment(0x8D41, 'Advance string pointer', align=Align.INLINE)
d.comment(0x8D42, 'Continue printing', align=Align.INLINE)
d.comment(0x8D44, 'Return', align=Align.INLINE)
d.comment(0x8D91, 'OSBYTE &77: close SPOOL/EXEC', align=Align.INLINE)
d.comment(0x8D93, 'Store as pending operation marker', align=Align.INLINE)
d.comment(0x8D99, 'Y=0', align=Align.INLINE)
d.comment(0x8D9B, 'Clear password entry flag', align=Align.INLINE)
d.comment(0x8D9D, 'Reset FS connection state', align=Align.INLINE)
d.comment(0x8DAA, 'Load first option byte', align=Align.INLINE)
d.comment(0x8DAC, 'Parse station number if present', align=Align.INLINE)
d.comment(0x8DAF, 'Not a digit: skip to password entry', align=Align.INLINE)
d.comment(0x8DB1, 'Parse user ID string', align=Align.INLINE)
d.comment(0x8DB4, 'No user ID: go to password', align=Align.INLINE)
d.comment(0x8DC0, 'No FS address: skip to password', align=Align.INLINE)
d.comment(0x8DB6, 'Store file server station low', align=Align.INLINE)
d.comment(0x8DB9, 'Check and store FS network', align=Align.INLINE)
d.comment(0x8DBC, 'Skip separator', align=Align.INLINE)
d.comment(0x8DBD, 'Parse next argument', align=Align.INLINE)
d.comment(0x8DC2, 'Store file server station high', align=Align.INLINE)
d.comment(0x8DC5, 'X=&FF: pre-decrement for loop', align=Align.INLINE)
d.comment(0x8DC7, 'Advance index', align=Align.INLINE)
d.comment(0x8DC8, 'Load logon command template byte', align=Align.INLINE)
d.comment(0x8DCB, 'Store into transmit buffer', align=Align.INLINE)
d.comment(0x8DCE, 'Bit 7 clear: more bytes, loop', align=Align.INLINE)
d.comment(0x8DD0, 'Send logon with file server lookup', align=Align.INLINE)
d.comment(0x8DD3, 'Success: skip to password entry', align=Align.INLINE)
d.comment(0x8DD5, 'Build FS command packet', align=Align.INLINE)
d.comment(0x8DD8, 'Y=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0x8DDA, 'Advance to next byte', align=Align.INLINE)
d.comment(0x8DDB, 'Load byte from reply buffer', align=Align.INLINE)
d.comment(0x8DDE, 'Is it CR (end of prompt)?', align=Align.INLINE)
d.comment(0x8DE0, 'Yes: no colon found, skip to send', align=Align.INLINE)
d.comment(0x8DE2, "Is it ':' (password prompt)?", align=Align.INLINE)
d.comment(0x8DE4, 'No: keep scanning', align=Align.INLINE)
d.comment(0x8DE9, 'Save position of colon', align=Align.INLINE)
d.comment(0x8DEB, 'A=&FF: mark as escapable', align=Align.INLINE)
d.comment(0x8DED, 'Set escape flag', align=Align.INLINE)
d.comment(0x8DEF, 'Check for escape condition', align=Align.INLINE)
d.comment(0x8DF7, 'Not NAK (&15): check other chars', align=Align.INLINE)
d.comment(0x8DF9, 'Restore colon position', align=Align.INLINE)
d.comment(0x8DFB, 'Non-zero: restart from colon', align=Align.INLINE)
d.comment(0x8DFD, 'At colon position?', align=Align.INLINE)
d.comment(0x8DFF, 'Yes: restart password input', align=Align.INLINE)
d.comment(0x8E01, 'Backspace: move back one character', align=Align.INLINE)
d.comment(0x8E02, 'If not at start: restart input', align=Align.INLINE)
d.comment(0x8E04, 'Delete key (&7F)?', align=Align.INLINE)
d.comment(0x8E06, 'Yes: handle backspace', align=Align.INLINE)
d.comment(0x8E08, 'Store character in password buffer', align=Align.INLINE)
d.comment(0x8E0B, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x8E0C, 'Is it CR (end of password)?', align=Align.INLINE)
d.comment(0x8E0E, 'No: read another character', align=Align.INLINE)
d.comment(0x8E13, 'Transfer string length to A', align=Align.INLINE)
d.comment(0x8E14, 'Save string length', align=Align.INLINE)
d.comment(0x8E15, 'Set up transmit control block', align=Align.INLINE)
d.comment(0x8E18, 'Send to file server and get reply', align=Align.INLINE)
d.comment(0x8E1C, 'Include terminator', align=Align.INLINE)
d.comment(0x8E1D, 'Y=0', align=Align.INLINE)
d.comment(0x8E21, 'Ensure bridge initialised; A=spool_control_flag (bridge status)', align=Align.INLINE)
d.comment(0x8E24, 'EOR with hazel_fs_network: zero result if equal', align=Align.INLINE)
d.comment(0x8E27, 'Different: return without clearing', align=Align.INLINE)
d.comment(0x8E29, 'Same: clear station byte', align=Align.INLINE)
d.comment(0x8E2C, 'Return', align=Align.INLINE)
d.comment(0x8E2D, 'Y=0: first character offset', align=Align.INLINE)
d.comment(0x8E38, 'Build FS command packet', align=Align.INLINE)
d.comment(0x8E2F, 'Load first character of command text', align=Align.INLINE)
d.comment(0x8E3B, 'Transfer result to Y', align=Align.INLINE)
d.comment(0x8E31, "Is it '&' (URD prefix)?", align=Align.INLINE)
d.comment(0x8E3C, 'Set up command and send to FS', align=Align.INLINE)
d.comment(0x8E33, 'No: send as normal FS command', align=Align.INLINE)
d.comment(0x8E3F, 'Load reply function code', align=Align.INLINE)
d.comment(0x8E35, 'Yes: route via *RUN for URD prefix handling', align=Align.INLINE)
d.comment(0x8E42, 'Zero: no reply, return', align=Align.INLINE)
d.comment(0x8E44, 'Load first reply byte', align=Align.INLINE)
d.comment(0x8E47, 'Y=&25: logon dispatch offset', align=Align.INLINE)
d.comment(0x8E4B, 'Parse reply as decimal number', align=Align.INLINE)
d.comment(0x8E4E, 'Result >= 8?', align=Align.INLINE)
d.comment(0x8E50, 'Yes: out of range, return', align=Align.INLINE)
d.comment(0x8E52, 'Transfer handle to X', align=Align.INLINE)
d.comment(0x8E53, 'Look up in open files table', align=Align.INLINE)
d.comment(0x8E56, 'Transfer result to A', align=Align.INLINE)
d.comment(0x8E57, 'Y=&1D: handle dispatch offset', align=Align.INLINE)
d.comment(0x8E5B, 'Handle >= 5?', align=Align.INLINE)
d.comment(0x8E5D, 'Yes: out of range, return', align=Align.INLINE)
d.comment(0x8E5F, 'Y=&18: settles X_final to &19..&1D (lang reply 0..4)', align=Align.INLINE)
d.comment(0x8E61, 'Advance X to target index', align=Align.INLINE)
d.comment(0x8E63, 'Y still positive: continue counting', align=Align.INLINE)
d.comment(0x8E62, 'Decrement Y offset counter', align=Align.INLINE)
d.comment(0x8E65, 'Y=&FF: will be ignored by caller', align=Align.INLINE)
d.comment(0x8E66, 'Load dispatch address high byte', align=Align.INLINE)
d.comment(0x8E69, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E6A, 'Load dispatch address low byte', align=Align.INLINE)
d.comment(0x8E6D, 'Push low byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E6E, 'Load FS options pointer', align=Align.INLINE)
d.comment(0x8E70, 'Dispatch via RTS', align=Align.INLINE)
d.comment(0x8E71, 'Claim 1 page (DEY = decrement Y by 1)', align=Align.INLINE)
d.comment(0x8E72, 'Return', align=Align.INLINE)
d.comment(0x8E73, 'X = 10 (top of 11-byte template)', align=Align.INLINE)
d.comment(0x8E75, 'Load template byte X from &8E7F+X', align=Align.INLINE)
d.comment(0x8E78, 'Store at (&F2),Y', align=Align.INLINE)
d.comment(0x8E7A, 'Advance destination cursor', align=Align.INLINE)
d.comment(0x8E7B, 'Step to previous template byte', align=Align.INLINE)
d.comment(0x8E7C, 'Loop until X has wrapped past 0', align=Align.INLINE)
d.comment(0x8E7E, 'Return', align=Align.INLINE)
d.comment(0x8E80, "11-byte template (length 5 in [0], then '       TEN'); copied to (&F2),Y by copy_template_to_zp", align=Align.INLINE)
d.comment(0x8E8A, 'Test bit 6 of fs_flags (NFS currently selected?)', align=Align.INLINE)
d.comment(0x8E8D, 'Clear: return without acting', align=Align.INLINE)
d.comment(0x8E8F, 'Ensure NFS is the selected FS', align=Align.INLINE)
d.comment(0x8E92, 'A=0', align=Align.INLINE)
d.comment(0x8E94, "Y=0 -- FILEV 'close all files' sub-call", align=Align.INLINE)
d.comment(0x8E95, 'Tail-call findv_handler (= FILEV)', align=Align.INLINE)
d.comment(0x8E9F, """Printer server template (8 bytes)

Default printer server configuration data, read
indirectly by copy_ps_data via LDA ps_template_base,X
with X=&F8..&FF (reaching ps_template_base+&F8 =
&8E9F). Contains "PRINT " (6 bytes) as the default
printer server name, followed by &01 and &00 as
default status bytes. Absent from NFS versions;
unique to ANFS.""")
d.comment(0x8E9F, 'PS template: default name "PRINT "', align=Align.INLINE)
d.comment(0x8ED4, 'Y=0', align=Align.INLINE)
d.comment(0x8ED8, 'Get original OSBYTE A parameter', align=Align.INLINE)
d.comment(0x8EDA, 'Subtract &31 (map &32-&35 to 1-4)', align=Align.INLINE)
d.comment(0x8EDC, 'In range 0-3?', align=Align.INLINE)
d.comment(0x8EDE, 'No: not ours, return unclaimed', align=Align.INLINE)
d.comment(0x8EE0, 'Transfer to X as dispatch index', align=Align.INLINE)
d.comment(0x8EE3, 'Transfer Y to A (OSBYTE Y param)', align=Align.INLINE)
d.comment(0x8EE4, 'Y=&2F: OSBYTE dispatch offset', align=Align.INLINE)
d.comment(0x8EE6, 'Dispatch to OSBYTE handler via table', align=Align.INLINE)
d.comment(0x8EE9, 'Y already >= &C8?', align=Align.INLINE)
d.comment(0x8EEB, 'Yes: return Y unchanged', align=Align.INLINE)
d.comment(0x8EED, 'No: raise Y to &C8', align=Align.INLINE)
d.comment(0x8EEF, 'Return', align=Align.INLINE)
d.comment(0x8EF0, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8EF2, 'Y >= &D3?', align=Align.INLINE)
d.comment(0x8EF4, 'No: use Y as-is', align=Align.INLINE)
d.comment(0x8EF6, 'Cap at &D3', align=Align.INLINE)
d.comment(0x8EF8, 'Offset &0B in receive block', align=Align.INLINE)
d.comment(0x8EFA, 'Store workspace page count', align=Align.INLINE)
d.comment(0x8EFD, 'Return -- ws_page count saved', align=Align.INLINE)
d.comment(0x8EFE, "Caller's page (in Y) into A", align=Align.INLINE)
d.comment(0x8EFF, 'Y = current ROM slot from romsel_copy', align=Align.INLINE)
d.comment(0x8F04, 'Publish page into rom_ws_pages[slot] (bit 7 cleared = workspace claimed)', align=Align.INLINE)
d.comment(0x8F07, 'Read Master break-type shadow (&FE2B)', align=Align.INLINE)
d.comment(0x8F4D, 'Zero: first ROM init, skip FS setup', align=Align.INLINE)
d.comment(0x8F4F, 'Set up workspace pointers', align=Align.INLINE)
d.comment(0x8F52, 'Clear FS flags', align=Align.INLINE)
d.comment(0x8F55, 'A=0, transfer to Y', align=Align.INLINE)
d.comment(0x8F56, 'Clear byte in FS workspace', align=Align.INLINE)
d.comment(0x8F58, 'Next workspace byte', align=Align.INLINE)
d.comment(0x8F59, 'Loop until full page (256 bytes) cleared', align=Align.INLINE)
d.comment(0x8F74, 'Y=2: nfs_workspace offset for FS station', align=Align.INLINE)
d.comment(0x8F76, 'Store FS station at (nfs_workspace)+2', align=Align.INLINE)
d.comment(0x8F7A, 'Read CMOS &04 (FS network)', align=Align.INLINE)
d.comment(0x8F7E, 'Y=3: nfs_workspace offset for FS network', align=Align.INLINE)
d.comment(0x8F80, 'Store at NFS workspace offset 2', align=Align.INLINE)
d.comment(0x8F82, 'X=3: init data byte count', align=Align.INLINE)
d.comment(0x8F84, 'Load initialisation data byte', align=Align.INLINE)
d.comment(0x8F87, 'Store in workspace', align=Align.INLINE)
d.comment(0x8F8A, 'Decrement counter', align=Align.INLINE)
d.comment(0x8F8B, 'More bytes: loop', align=Align.INLINE)
d.comment(0x8F8D, 'Clear workspace flag', align=Align.INLINE)
d.comment(0x8F90, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8F93, 'Initialise ADLC protection table', align=Align.INLINE)
d.comment(0x8F96, 'X=&FF (underflow from X=0)', align=Align.INLINE)
d.comment(0x8FA9, 'Get current workspace page', align=Align.INLINE)
d.comment(0x8F97, 'Initialise workspace flag to &FF', align=Align.INLINE)
d.comment(0x8FAB, 'Allocate FS handle page', align=Align.INLINE)
d.comment(0x8FAE, 'Allocation failed: finish init', align=Align.INLINE)
d.comment(0x8FB0, 'A=&3F: default handle permissions', align=Align.INLINE)
d.comment(0x8FB2, 'Store handle permissions', align=Align.INLINE)
d.comment(0x8FB4, 'Advance to next page', align=Align.INLINE)
d.comment(0x8FB6, 'Continue allocating: loop', align=Align.INLINE)
d.comment(0x8FB8, 'Restore FS context from saved state', align=Align.INLINE)
d.comment(0x903C, 'Initialise ADLC hardware', align=Align.INLINE)
d.comment(0x903F, 'OSBYTE &A8: read ROM pointer table', align=Align.INLINE)
d.comment(0x9041, 'Read ROM pointer table address', align=Align.INLINE)
d.comment(0x9044, 'Store table pointer low', align=Align.INLINE)
d.comment(0x9046, 'Store table pointer high', align=Align.INLINE)
d.comment(0x9048, 'Y=&36: NETV vector offset', align=Align.INLINE)
d.comment(0x904A, 'Set NETV address', align=Align.INLINE)
d.comment(0x904D, 'X=1: one more vector pair to set', align=Align.INLINE)
d.comment(0x904F, 'Load vector address low byte', align=Align.INLINE)
d.comment(0x9052, 'Store into extended vector table', align=Align.INLINE)
d.comment(0x9054, 'Advance to high byte', align=Align.INLINE)
d.comment(0x9055, 'Load vector address high byte', align=Align.INLINE)
d.comment(0x9058, 'Store into extended vector table', align=Align.INLINE)
d.comment(0x905A, 'Advance to ROM ID byte', align=Align.INLINE)
d.comment(0x905B, 'Load current ROM slot number', align=Align.INLINE)
d.comment(0x905D, 'Store ROM ID in extended vector', align=Align.INLINE)
d.comment(0x905F, 'Advance to next vector entry', align=Align.INLINE)
d.comment(0x9060, 'Decrement vector counter', align=Align.INLINE)
d.comment(0x9061, 'More vectors to set: loop', align=Align.INLINE)
d.comment(0x9063, 'Return', align=Align.INLINE)
d.comment(0x9064, 'Y=9: end of FS context block', align=Align.INLINE)
d.comment(0x9066, 'Load FS context byte', align=Align.INLINE)
d.comment(0x9069, 'Store into receive block', align=Align.INLINE)
d.comment(0x906B, 'Decrement index', align=Align.INLINE)
d.comment(0x906C, 'Reached offset 1?', align=Align.INLINE)
d.comment(0x906E, 'No: continue copying', align=Align.INLINE)
d.comment(0x9070, 'Return', align=Align.INLINE)
d.comment(0x9071, 'FS currently selected?', align=Align.INLINE)
d.comment(0x9074, 'No (bit 7 clear): return', align=Align.INLINE)
d.comment(0x9076, 'Y=0', align=Align.INLINE)
d.comment(0x907B, 'Restore FS context to receive block', align=Align.INLINE)
d.comment(0x907E, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x9080, 'A=0: checksum accumulator', align=Align.INLINE)
d.comment(0x9082, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9083, 'Add byte from page &10 shadow', align=Align.INLINE)
d.comment(0x9086, 'Decrement index', align=Align.INLINE)
d.comment(0x9087, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x9089, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x908D, 'Load byte from page &10 shadow', align=Align.INLINE)
d.comment(0x9090, 'Copy to FS workspace', align=Align.INLINE)
d.comment(0x9092, 'Decrement index', align=Align.INLINE)
d.comment(0x9093, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9095, 'Load FS flags', align=Align.INLINE)
d.comment(0x9098, 'Clear bit 7 (FS no longer selected)', align=Align.INLINE)
d.comment(0x909A, 'Store updated flags', align=Align.INLINE)
d.comment(0x909D, 'Return', align=Align.INLINE)
d.comment(0x909E, 'Save processor status', align=Align.INLINE)
d.comment(0x909F, 'Save A', align=Align.INLINE)
d.comment(0x90A1, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x90A3, 'A=0: checksum accumulator', align=Align.INLINE)
d.comment(0x90A5, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x90A6, 'Add byte from FS workspace', align=Align.INLINE)
d.comment(0x90A8, 'Decrement index', align=Align.INLINE)
d.comment(0x90A9, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x90AB, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x90AD, 'Compare with stored checksum', align=Align.INLINE)
d.comment(0x90AF, 'Mismatch: raise checksum error', align=Align.INLINE)
d.comment(0x90B2, 'Restore A', align=Align.INLINE)
d.comment(0x90B3, 'Restore processor status', align=Align.INLINE)
d.comment(0x90B4, 'Return (checksum valid)', align=Align.INLINE)
d.comment(0x90B5, 'Error number &AA', align=Align.INLINE)
d.comment(0x90B7, "Raise 'net checksum' error", align=Align.INLINE)
d.comment(0x90CC, "Print 'Econet Station ' via inline", align=Align.INLINE)
d.comment(0x90E0, 'Space character', align=Align.INLINE)
d.comment(0x90E2, 'Check ADLC status register 2', align=Align.INLINE)
d.comment(0x90E5, 'Clock present: skip warning', align=Align.INLINE)
d.comment(0x90E7, "Print ' No Clock' via inline", align=Align.INLINE)
d.comment(0x90F3, 'String terminator', align=Align.INLINE)
d.comment(0x90F7, 'Return', align=Align.INLINE)
d.comment(0x90F8, """*HELP command syntax strings

13 null-terminated syntax help strings displayed
by *HELP after each command name. Multi-line
entries use &0D as a line break. Indexed by
cmd_syntax_table via the low 5 bits of each
command's syntax descriptor byte.""")
d.comment(0x90F8, 'Syn 1: *Dir, *LCat, *LEx, *Wipe', align=Align.INLINE)
d.comment(0x9118, 'Line break', align=Align.INLINE)
d.comment(0x914C, 'Syn 4 continued: address clause', align=Align.INLINE)
d.comment(0x9158, 'Null terminator', align=Align.INLINE)
d.comment(0x9159, 'Syn 5: *Lib', align=Align.INLINE)
d.comment(0x9170, 'Syn 7: *Pass', align=Align.INLINE)
d.comment(0x91DF, 'Null terminator', align=Align.INLINE)
d.comment(0x91E0, 'Syn 11: (station id. argument)', align=Align.INLINE)
d.comment(0x91ED, """Command syntax string offset table

13 offsets into syn_opt_dir (&9022).
Indexed by the low 5 bits of each command table
syntax descriptor byte. Index &0E is handled
separately as a shared-commands list. The print
loop at &8BD5 does INY before LDA, so each offset
points to the byte before the first character.""")
d.comment(0x9236, 'Save full byte', align=Align.INLINE)
d.comment(0x9237, 'Shift high nybble to low', align=Align.INLINE)
d.comment(0x9238, 'Continue shifting', align=Align.INLINE)
d.comment(0x9239, 'Continue shifting', align=Align.INLINE)
d.comment(0x923A, 'High nybble now in bits 0-3', align=Align.INLINE)
d.comment(0x923B, 'Print high nybble as hex digit', align=Align.INLINE)
d.comment(0x923E, 'Restore full byte', align=Align.INLINE)
d.comment(0x923F, 'Mask to low nybble', align=Align.INLINE)
d.comment(0x9241, 'Digit >= &0A?', align=Align.INLINE)
d.comment(0x9243, 'No: skip letter adjustment', align=Align.INLINE)
d.comment(0x9245, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.comment(0x9247, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.comment(0x9763, 'Offset 0: txcb_ctrl = &80 (TX command)', align=Align.INLINE)
d.comment(0x9764, 'Offset 1: txcb_port = &99 (FS command port)', align=Align.INLINE)
d.comment(0x9765, 'Offset 2: txcb_dest lo placeholder (overwritten with hazel_fs_station[0])', align=Align.INLINE)
d.comment(0x9766, 'Offset 3: txcb_dest hi placeholder (overwritten with hazel_fs_station[1])', align=Align.INLINE)
d.comment(0x9767, 'Offset 4: txcb_start lo = 0', align=Align.INLINE)
d.comment(0x9768, 'Offset 5: txcb_start hi = &C1 (data buffer starts at &C100 in HAZEL)', align=Align.INLINE)
d.comment(0x9769, 'Offset 6: padding &FF; doubles as the always_set_v_byte BIT $abs target', align=Align.INLINE)
d.comment(0x976A, 'Offset 7: txcb_pos = &FF (also labelled bit_test_ff)', align=Align.INLINE)
d.comment(0x976B, 'Offset 8: txcb_end lo = &FF', align=Align.INLINE)
d.comment(0x976C, 'Offset 9: txcb_end hi = &C1 (buffer end &C1FF)', align=Align.INLINE)
d.comment(0x976D, 'Offset 10: extended-addr fill (&FF)', align=Align.INLINE)
d.comment(0x976E, 'Offset 11: extended-addr fill (&FF)', align=Align.INLINE)
d.entry(0x8D09)
d.entry(0x8CC7)
d.entry(0x8C42)
d.entry(0x8ED8)
d.entry(0x8C51)
d.entry(0x8EE9)

d.label(0x8EE9, 'raise_y_to_c8')

d.label(0x8CC7, 'svc_3_autoboot')

d.label(0x8C42, 'svc_4_star_command')

d.label(0x8ED8, 'svc_7_osbyte')

d.label(0x8C51, 'svc_9_help')

d.label(0xA83C, 'svc_8_osword_disp')

d.label(0x969A, 'match_on_suffix')

d.label(0xB0FE, 'ps_scan_resume')

d.label(0xB357, 'cmd_info_dispatch')

d.label(0xA4DC, 'check_urd_present')

d.label(0xB2DB, 'ex_init_scan_x0')

d.label(0x89ED, 'svc_dispatch_lo')
d.banner(0x89ED, title='svc_dispatch low-byte table (51 entries)', description="""Low-byte half of the `PHA`/`PHA`/`RTS` dispatch table read by
[`svc_dispatch`](address:8E61) as `LDA &89ED,X`. Paired with
the high-byte half at [`svc_dispatch_hi`](address:8A20).

Index 0 is a placeholder (target value unused – never reached);
indices 1..50 cover:

- service handlers
- language reply handlers
- FSCV reasons
- FS reply handlers
- net-handle / OSWORD `&13` trampolines

Per-entry inline comments give the index and the call/reply each
slot dispatches.""")
for addr in range(0x89ED, 0x8A20):
    d.byte(addr)

d.label(0x8A20, 'svc_dispatch_hi')
d.banner(0x8A20, title='svc_dispatch high-byte table (51 entries + 1 padding)', description="""High-byte half of the `PHA`/`PHA`/`RTS` dispatch table read by
[`svc_dispatch`](address:8E61) as `LDA &8A20,X`. The
dispatcher pushes the hi byte first then the lo, so `RTS` lands
on `target` (the table stores `target-1`). The trailing byte at
`&8A53` is 1-byte padding – there are only 51 valid entries
(0..50).""")
for addr in range(0x8A20, 0x8A54):
    d.byte(addr)
_svc_dispatch_entries = [(0x00, 0xE905, None, 'placeholder (never reached)'), (0x01, 0x8E70, 'dispatch_rts', 'no-op (RTS only)'), (0x02, 0x8D09, 'svc_dispatch_idx_2', 'workspace claim helper (CMOS bit 0)'), (0x03, 0x8F10, 'svc_2_priv_ws', 'svc &02: private workspace pages'), (0x04, 0x8CC7, 'svc_3_autoboot', 'svc &03: auto-boot'), (0x05, 0x8C42, 'svc_4_star_command', 'svc &04: unrecognised *command'), (0x06, 0x8028, 'svc5_irq_check', 'svc &05: IRQ check'), (0x07, 0x8E70, 'dispatch_rts', 'no-op (RTS only)'), (0x08, 0x8ED8, 'svc_7_osbyte', 'svc &07: unrecognised OSBYTE'), (0x09, 0xA83C, 'svc_8_osword_disp', 'svc &08: OSWORD dispatch'), (0x0A, 0x8C51, 'svc_9_help', 'svc &09: *HELP'), (0x0B, 0x8E70, 'dispatch_rts', 'no-op (RTS only)'), (0x0C, 0x806C, 'econet_restore', 'svc &0B: NMI release'), (0x0D, 0x89A6, 'wait_idle_and_reset', 'svc &0D: wait idle and reset'), (0x0E, 0x8B45, 'svc_18_fs_select', 'svc &12: FS select'), (0x0F, 0x969A, 'match_on_suffix', "svc &18: interactive HELP 'ON ' matcher"), (0x10, 0x8EE9, 'raise_y_to_c8', 'svc &21: static workspace claim'), (0x11, 0x8EFE, 'set_rom_ws_page', 'svc &22: dynamic workspace offer'), (0x12, 0x8EF0, 'store_ws_page_count', 'svc &23: top-of-static-workspace'), (0x13, 0x8E71, 'noop_dey_rts', 'svc &24: dynamic workspace claim'), (0x14, 0x8E73, 'copy_template_to_zp', 'svc &25: FS name + info reply'), (0x15, 0x8E8A, 'svc_26_close_all_files', 'svc &26: close all files'), (0x16, 0x8F38, 'nfs_init_body', 'svc &27: post-hard-reset re-init'), (0x17, 0x959A, 'print_fs_ps_help', 'svc &28: print *FS/*PS no-arg syntax help'), (0x18, 0x9630, 'svc_29_status', 'svc &29: *STATUS handler'), (0x19, 0x98AF, 'lang_0_insert_key', 'language reply 0: insert remote key'), (0x1A, 0x9850, 'lang_1_remote_boot', 'language reply 1: remote boot'), (0x1B, 0xB01A, 'lang_2_save_palette_vdu', 'language reply 2: save palette/VDU'), (0x1C, 0x987E, 'lang_3_exec_0100', 'language reply 3: execute at &0100'), (0x1D, 0x989F, 'lang_4_validated', 'language reply 4: remote validated'), (0x1E, 0xA0A9, 'fscv_0_opt_entry', 'FSCV 0: *OPT'), (0x1F, 0xA10B, 'fscv_1_eof', 'FSCV 1: EOF'), (0x20, 0xA4F1, 'cmd_run_via_urd', 'FSCV 2: *RUN'), (0x21, 0xA42F, 'fscv_3_star_cmd', 'FSCV 3: *command'), (0x22, 0xA4F1, 'cmd_run_via_urd', 'FSCV 4: *RUN (alias)'), (0x23, 0xB118, 'fscv_5_cat', 'FSCV 5: *CAT'), (0x24, 0x9071, 'fscv_6_shutdown', 'FSCV 6: shutdown'), (0x25, 0x93F2, 'fscv_7_read_handles', 'FSCV 7: read handles'), (0x26, 0x8E70, 'dispatch_rts', 'no-op (RTS only)'), (0x27, 0xB0FE, 'ps_scan_resume', 'PS scan tail (after pop_requeue)'), (0x28, 0xB357, 'cmd_info_dispatch', '*Info dispatch'), (0x29, 0xA4DC, 'check_urd_present', 'URD-present check'), (0x2A, 0xB2DB, 'ex_init_scan_x0', '*Ex scan init'), (0x2B, 0xA6D5, 'fsreply_1_boot', 'FS reply 1: copy handles + boot'), (0x2C, 0xA6E5, 'fsreply_2_copy_handles', 'FS reply 2: copy handles'), (0x2D, 0xA638, 'fsreply_3_set_csd', 'FS reply 3: set CSD'), (0x2E, 0xA4F1, 'cmd_run_via_urd', 'FS reply 4: *RUN (alias)'), (0x2F, 0xA63E, 'fsreply_5_set_lib', 'FS reply 5: set library'), (0x30, 0xA3FF, 'net_1_read_handle', 'net handle 1: read handle'), (0x31, 0xA405, 'net_2_read_entry', 'net handle 2: read handle entry'), (0x32, 0xA415, 'net_3_close_handle', 'net handle 3: close handle')]
for idx, target, name, desc in _svc_dispatch_entries:
    if name is not None:
        d.expr(0x89ED + idx, '<(%s-1)' % name)
        d.expr(0x8A20 + idx, '>(%s-1)' % name)
    d.comment(0x89ED + idx, '&%02X: %s' % (idx, desc), align=Align.INLINE)
    d.comment(0x8A20 + idx, '&%02X: %s' % (idx, desc), align=Align.INLINE)
d.comment(0x8A53, 'padding (table has only 51 entries)', align=Align.INLINE)


d.subroutine(0x8EE9, 'raise_y_to_c8', title='Master 128 service &21 handler: claim static hidden-RAM workspace', description="""Four-instruction stub: `CPY #&C8 / BCS return / LDY #&C8 / RTS`.
Reached when MOS issues service call `&21` ("Offer Static Workspace
in Hidden RAM") to all sideways ROMs at reset. Per the *Advanced
Reference Manual for the BBC Master*, hidden-RAM static workspace
runs from page `&C0` up to page `&DB`; each filing-system ROM that
wants a slice raises Y to its required base page. ANFS demands its
static workspace base at page `&C8`, so it raises Y to `&C8` if a
previous ROM hasn't already.""", on_entry={'y': 'current bottom of static workspace claim (some page in &C0..&DB)'}, on_exit={'y': '>= &C8 (ANFS static workspace base)'})


d.subroutine(0x8CC7, 'svc_3_autoboot', title='Service 3: auto-boot on reset', description="""Scans the keyboard via OSBYTE &7A for the 'N' key
(&19 or &55 EOR'd with &55). If pressed, records
the key state via OSBYTE &78. Selects the network
filing system by calling cmd_net_fs, prints the
station ID, then checks if this is the first boot
(ws_page = 0). If so, sets the auto-boot flag in
&1071 and JMPs to cmd_fs_entry to execute the boot
file.""", on_entry={'a': '3 (service call number)', 'x': 'ROM slot', 'y': 'parameter (Master 128 service-call dispatch)'})


d.subroutine(0x8C42, 'svc_4_star_command', title='Service 4: unrecognised star command', description="""Saves the OS text pointer, then calls match_fs_cmd
to search the command table starting at offset 0
(all command sub-tables). If no match is found (carry
set), returns with the service call unclaimed. On
a match, JMPs to cmd_fs_reentry to execute the
matched command handler via the PHA/PHA/RTS
dispatch mechanism.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8ED8, 'svc_7_osbyte', title='Service 7: unrecognised OSBYTE', description="""Maps Econet OSBYTE codes &32-&35 to dispatch
indices 0-3 by subtracting &31 (with carry from
a preceding SBC). Returns unclaimed if the OSBYTE
number is outside this range. For valid codes,
claims the service (sets svc_state to 0) and
JMPs to svc_dispatch with Y=&21 to reach the
Econet OSBYTE handler table.""", on_entry={'a': 'OSBYTE number (from osbyte_a_copy at &EF)'})
d.entry(0xA83B)


d.subroutine(0xA83B, 'svc_8_osword', title='Service 8: unrecognised OSWORD', description="""Handles MOS service call 8 (unrecognised OSWORD).
Filters OSWORD codes &0E-&14 by subtracting &0E (via
CLC/SBC &0D) and rejecting values outside 0-6. For
valid codes, calls osword_setup_handler to push the
dispatch address, then copies 3 bytes from the RX
buffer to osword_flag workspace.""", on_entry={'a': 'OSWORD number (from osbyte_a_copy)', 'y': 'parameter passed by service-call dispatch'})


d.subroutine(0x8C51, 'svc_9_help', title='Service 9: *HELP', description="""Handles MOS service call 9 (*HELP). First checks
for the credits Easter egg. For bare *HELP (CR
at text pointer), prints the version header and
full command list starting at table offset &91.
For *HELP with an argument, handles '.' as a
shortcut to list all NFS commands, otherwise
iterates through help topics using PHA/PHA/RTS
dispatch to print matching command groups.
Returns with Y = ws_page (unclaimed).""", on_entry={'a': '9 (service call number)', 'y': 'command-line offset of *HELP argument'}, on_exit={'y': 'ws_page (workspace page) -- the service call is left UNCLAIMED so MOS continues to the next ROM'})
d.entry(0x8B45)


d.subroutine(0x8B52, 'select_fs_via_cmd_net_fs', title='Force ANFS selection (raise net checksum on failure)', description="""Tail-fragment of [`ensure_fs_selected`](address:8B4D) used directly
by `svc_3_autoboot` when an autoboot needs to force-select ANFS as
the active filing system. Calls `cmd_net_fs` to perform the actual
selection; on failure (`BEQ` not taken), `JMP`s to
[`error_net_checksum`](address:90B5) to raise the `net checksum`
error. Used when there is no clean `BIT fs_flags` / `BMI` shortcut
for early-return.""", on_entry={'x, y': 'preserved across cmd_net_fs (as per the ensure_fs_selected calling contract)'}, on_exit={'a': 'current FS state byte if selection succeeded'})


d.subroutine(0x924C, 'print_hex_byte_no_spool', title='Print A as two hex digits, *SPOOL-bypassing', description="""As [`print_hex_byte`](address:9236) but emits each digit via
[`print_char_no_spool`](address:91FB) (the *SPOOL-bypassing OSASCI
wrapper), so the digits don't appear in any active spool capture.
Saves `A`, extracts the high nibble (`LSR` x4), prints it via
[`print_hex_nybble_no_spool`](address:9255), then restores `A` and
falls through for the low nibble. Sole caller:
[`print_5_hex_bytes`](address:9D4F) at `&9D53`.""", on_entry={'a': 'byte to print'}, on_exit={'a': 'preserved'})


d.subroutine(0x9255, 'print_hex_nybble_no_spool', title='Print low nybble of A as one hex digit, *SPOOL-bypassing', description='As print_hex_nybble (&923F) but emits via the print_char_no_spool tail-call instead of OSASCI directly, so the digit is not captured by any active *SPOOL file. Standard AND #&0F / CMP #&0A / +6-or-not / + #&30 mapping for hex digits 0-9 / A-F. Tail-jumps to print_char_no_spool via BRA.', on_entry={'a': 'value (low nybble used)'})


d.subroutine(0x95EE, 'set_fs_or_ps_cmos_station', title='Write FS/PS station+network to Master 128 CMOS RAM', description="""Reached via PHA/PHA/RTS dispatch from cmd_table_fs sub-table 4
(`*FS` at [`&A80F`](address:A80F), `*PS` at
[`&A814`](address:A814)) when the caller supplies a `<net>.<stn>`
argument or wants to inspect/update the saved address.

The flag byte's low 6 bits (`AND #&3F`) double as the CMOS byte
index for the relevant station:

| command | flag | idx | CMOS bytes      |
| ------- | ---- | --- | --------------- |
| `*FS`   | `&C1` | 1   | 1 = FS station, 2 = FS network |
| `*PS`   | `&C3` | 3   | 3 = PS station, 4 = PS network |

Pre-reads existing CMOS[idx] and CMOS[idx+1] into `fs_work_5` /
`fs_work_6` so that the no-argument path leaves the saved values
unchanged. Calls
[`parse_fs_ps_args`](address:A3C4) which conditionally overwrites
`fs_work_5` (station), `fs_work_6` (canonical network: 0=local,
non-zero=remote) and `fs_work_7` (raw parsed network).

Writes the station via [`osbyte_a2`](address:9612), then falls
through into `osbyte_a2` itself to write the raw network at
CMOS[idx+1]. Final `BRA` inside `osbyte_a2` returns via
[`svc_return_unclaimed`](address:8C64).""", on_entry={'x': "offset in cmd_table_fs of the matched entry's flag byte"})


d.subroutine(0x9612, 'osbyte_a2', title='OSBYTE &A2 (write Master CMOS RAM byte)', description="""Three instructions: `LDA #&A2 / JSR OSBYTE / BRA &95BE`. Writes
the Master 128 CMOS RAM byte indexed by `X` with the value in `Y`.
The trailing `BRA` lands on
[`bra_target_svc_return`](address:95BE) (a 3-byte `JMP` trampoline
to [`svc_return_unclaimed`](address:8C64), reached this way
because `BRA`'s 8-bit displacement can't span &9617 → &8C64).

`osbyte_a2` ends at &9618 (3 instructions, 8 bytes); the next
labelled routine is [`cmd_space`](address:9619). Counterpart of
[`osbyte_a1`](address:8E9A) (read).

Callers: [`set_fs_or_ps_cmos_station`](address:95EE) (once via
`JSR`, once via fall-through), the `BRA` shortcut at
[`&962E`](address:962E) inside [`cmd_nospace`](address:9623), and
an `OSARGS`-related read-modify-write of CMOS byte &11 ending at
[`osopt_cmos_writeback_jsr`](address:A0FE).""", on_entry={'x': 'CMOS RAM byte index', 'y': 'value to write'})


d.subroutine(0x9619, 'cmd_space', title='*Space command: enable space-remaining display', description="""Reached via the [`cmd_table_fs`](address:A4D6) dispatch entry for
`*Space`. Reads CMOS byte &11 with [`osbyte_a1`](address:8E9A),
sets bit 0 of the value, then `BRA`s to the shared write-back tail
at [`osbyte_a2_value_tya`](address:962B).""")


d.subroutine(0x9623, 'cmd_nospace', title='*NoSpace command: disable space-remaining display', description="""Reached via the [`cmd_table_fs`](address:A4D6) dispatch entry for
`*NoSpace`. Reads CMOS byte &11 with [`osbyte_a1`](address:8E9A),
clears bit 0 of the value, falls through to
[`osbyte_a2_value_tya`](address:962B), and `BRA`s back into
[`osbyte_a2`](address:9612) to write CMOS &11 = `Y`.""")


d.subroutine(0x962B, 'osbyte_a2_value_tya', title='Shared CMOS write-back tail', description="""Common tail used by [`cmd_space`](address:9619) (via `BRA` from
&9621 with the new value already in `A`) and
[`cmd_nospace`](address:9623) (fall-through with the new value in
`A`). `TAY` moves the byte to `Y`, then `LDX #&11` reloads the
CMOS index and `BRA osbyte_a2` performs the write.""")


d.subroutine(0x9630, 'svc_29_status', title='Service &29: *STATUS handler', description="""Reached via `svc_dispatch` slot &18. With no argument on the
command line (first byte = `CR`) prints the FS and PS station
addresses from CMOS &01-&04, then a single FS-active flag drawn
from bit 0 of CMOS &11 (the same bit that
[`cmd_space`](address:9619) / [`cmd_nospace`](address:9623) set
and clear). With an argument, branches to
[`help_dispatch_setup`](address:968C) to parse it.""")


d.subroutine(0x8B45, 'svc_18_fs_select', title='Service 18: filing-system selection request', description="""Service-18 entry point.

| Condition | Action |
|---|---|
| `Y ≠ 5`   | return unclaimed (not the Econet FS) |
| Bit 7 of [`fs_flags`](address:0D6C) set | return (FS already selected) |
| else | fall through to [`cmd_net_fs`](address:8B23) for the full network-FS selection sequence |""", on_entry={'y': 'filing system number requested'})
d.entry(0x98AF)
d.entry(0x9850)
d.entry(0xB01A)
d.entry(0x987E)
d.entry(0x989F)
d.entry(0xA0A9)
d.entry(0x9E7F)
d.entry(0xA10B)
d.entry(0xA4E4)
d.entry(0xA42F)
d.entry(0xB118)
d.entry(0x9071)
d.entry(0x93F2)
d.entry(0xA6D5)
d.entry(0xA6E5)
d.entry(0xA638)
d.entry(0xA63E)
d.entry(0xA3FF)
d.entry(0xA405)
d.entry(0xA415)

d.label(0xA7A1, 'cmd_table_nfs')

d.label(0xA7FD, 'cmd_table_help_topics')

d.label(0xA80C, 'cmd_table_syntax_help')
d.entry(0x8B39)

d.label(0x8B39, 'cmd_net_check_hw')
d.entry(0x8D87)

d.label(0x8D87, 'cmd_iam_save_ctx')
d.entry(0xB581)
d.entry(0xB6D2)
d.entry(0xB3AC)
d.entry(0x8AEA)
d.entry(0xB6D6)
d.entry(0xBD41)

d.label(0xA76C, 'cmd_table_fs')
d.banner(0xA76C, title='ANFS *command dispatch tables (5 concatenated sub-tables)', description="""See the comment block immediately above the
[`cmd_table_fs`](address:A76C) declaration in the driver for the
sub-table layout, walker contract, and flag-byte encoding. Each
entry's two-byte dispatch word stores `target-1`; PHA/PHA/RTS
arrives at `target`. Per-entry inline comments below name the
command, syntax-template index, and dispatch target.""")
_cmd_table_fs_entries = [(0xA76C, 'Net', 0xA76F, 0x80, 0xA770, 'cmd_net_check_hw', 'Econet HW check + select NFS'), (0xA772, 'Pollps', 0xA778, 0x88, 0xA779, 'cmd_pollps', 'syn 8: (<stn. id.>|<ps type>)'), (0xA77B, 'Prot', 0xA77F, 0x80, 0xA780, 'cmd_prot', 'toggle CMOS protection bit'), (0xA782, 'PS', 0xA784, 0x88, 0xA785, 'cmd_ps', 'syn 8: (<stn. id.>|<ps type>)'), (0xA787, 'Roff', 0xA78B, 0x80, 0xA78C, 'cmd_roff', 'printer offline'), (0xA78E, 'Unprot', 0xA794, 0x80, 0xA795, 'cmd_unprot', 'toggle CMOS protection bit'), (0xA797, 'Wdump', 0xA79C, 0xC4, 0xA79D, 'cmd_dump', 'syn 4 -- *DUMP alias'), (0xA7A1, 'Access', 0xA7A7, 0xC9, 0xA7A8, 'cmd_fs_operation', 'syn 9: <obj> (L)(W)(R)...'), (0xA7AA, 'Bye', 0xA7AD, 0x80, 0xA7AE, 'cmd_bye', 'log off FS'), (0xA7B0, 'Cdir', 0xA7B4, 0xC6, 0xA7B5, 'cmd_cdir', 'syn 6 -- create directory'), (0xA7B7, 'Dir', 0xA7BA, 0x81, 0xA7BB, 'cmd_dir', 'syn 1: (<dir>)'), (0xA7BD, 'Flip', 0xA7C1, 0x80, 0xA7C2, 'cmd_flip', 'swap fs/private workspace'), (0xA7C4, 'FS', 0xA7C6, 0x8B, 0xA7C7, 'cmd_fs', 'syn &B -- file-server selection'), (0xA7C9, 'I am', 0xA7CD, 0xC2, 0xA7CE, 'cmd_iam_save_ctx', 'syn 2: (<stn>) <user>...'), (0xA7D0, 'Lcat', 0xA7D4, 0x81, 0xA7D5, 'cmd_lcat', 'syn 1: (<dir>) -- *CAT of library'), (0xA7D7, 'Lex', 0xA7DA, 0x81, 0xA7DB, 'cmd_lex', 'syn 1: (<dir>) -- *EX of library'), (0xA7DD, 'Lib', 0xA7E0, 0xC5, 0xA7E1, 'cmd_fs_operation', 'syn 5: <dir> -- set library'), (0xA7E3, 'Pass', 0xA7E7, 0xC7, 0xA7E8, 'cmd_pass', 'syn 7: <pass> ...'), (0xA7EA, 'Rename', 0xA7F0, 0xCA, 0xA7F1, 'cmd_rename', 'syn &A: <old> <new>'), (0xA7F3, 'Wipe', 0xA7F7, 0x81, 0xA7F8, 'cmd_wipe', 'syn 1: (<dir>) -- delete with confirm'), (0xA7FD, 'Net', 0xA800, 0x80, 0xA801, 'help_net', '*HELP NET'), (0xA803, 'Utils', 0xA808, 0x80, 0xA809, 'help_utils', '*HELP UTILS'), (0xA80C, 'FS', 0xA80E, 0xC1, 0xA80F, 'set_fs_or_ps_cmos_station', 'FS not selected'), (0xA811, 'PS', 0xA813, 0xC3, 0xA814, 'set_fs_or_ps_cmos_station', 'PS not selected'), (0xA816, 'NoSpace', 0xA81D, 0x80, 0xA81E, None, 'caller &9623'), (0xA820, 'Space', 0xA825, 0x80, 0xA826, None, 'caller &9619'), (0xA829, 'FS', 0xA82B, 0x81, 0xA82C, 'print_fs_address', 'caller &9670'), (0xA82E, 'PS', 0xA830, 0x83, 0xA831, 'print_ps_address', 'caller &965F'), (0xA833, 'Space', 0xA838, 0x80, 0xA839, None, 'caller &9641')]
for name_addr, name, flag_addr, flag_byte, lo_addr, target_label, role in _cmd_table_fs_entries:
    name_len = flag_addr - name_addr
    if name_len > 1:
        d.string(name_addr, name_len)
    else:
        d.byte(name_addr)
    d.byte(flag_addr)
    d.word(lo_addr)
    if target_label is not None:
        d.expr(lo_addr, '%s-1' % target_label)
    d.comment(name_addr, role, align=Align.INLINE)
    syn_idx = flag_byte & 0x1F
    flag_parts = ['no syn'] if syn_idx == 0 else ['syn &%X' % syn_idx]
    if flag_byte & 0x40:
        flag_parts.append('V if no arg')
    d.comment(flag_addr, ', '.join(flag_parts), align=Align.INLINE)
d.byte(0xA79F)
d.byte(0xA7A0)
d.byte(0xA7FA)
d.byte(0xA7FB)
d.byte(0xA7FC)
d.byte(0xA80B)
d.byte(0xA828)
d.comment(0xA79F, 'Sub-table 1 end (walker reads &80 -> stop)', align=Align.INLINE)
d.comment(0xA7A0, 'Padding (alignment before sub-table 2)', align=Align.INLINE)
d.comment(0xA7FA, 'Sub-table 2 end (walker reads &80 -> stop)', align=Align.INLINE)
d.comment(0xA7FB, 'Padding -- &2C 8E happens to spell &8E2D = check_urd_prefix but is never read', align=Align.INLINE)
d.comment(0xA7FC, 'Padding (continued)', align=Align.INLINE)
d.comment(0xA80B, 'Sub-table 3 end (walker reads &80 -> stop)', align=Align.INLINE)
d.comment(0xA828, 'Sub-tables 4/5 separator', align=Align.INLINE)

d.label(0xBD41, 'cmd_dump')

d.label(0x8B23, 'cmd_net_fs')

d.label(0xB581, 'cmd_pollps')

d.label(0xB3AC, 'cmd_ps')

d.label(0x8AEA, 'cmd_roff')


d.subroutine(0xBD41, 'cmd_dump', title='*Dump command handler', description="""Opens the file via open_file_for_read, allocates a
21-byte buffer on the stack, and parses the address
range via init_dump_buffer. Loops reading 16 bytes
per line, printing each as a 4-byte hex address,
16 hex bytes with spaces, and a 16-character ASCII
column (non-printable chars shown as '.'). Prints
a column header at every 256-byte boundary.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8B23, 'cmd_net_fs', title='Select Econet network filing system', description="""Computes a checksum over the first `&77` bytes of the workspace
page and verifies against the stored value; raises an error on
mismatch. On success:

1. Notifies the OS via FSCV reason 6
   ([`notify_new_fs`](address:8CFD)).
2. Copies the FS context block from the receive block to the
   HAZEL FS state at [`hazel_fs_station`](address:C000)
   (offsets 0..9), via the `hazel_minus_2,Y` indexing-base
   trick.
3. Installs 7 filing-system vectors (FILEV etc.) from
   [`fs_vector_table`](address:8EA7).
4. Initialises the ADLC and extended vectors.
5. Sets up the channel table.
6. Sets bit 7 of [`fs_flags`](address:0D6C) to mark the FS as
   selected.
7. Issues service call 15 (vectors claimed) via
   [`issue_svc_15`](address:8D02).""", on_entry={'y': 'command line offset in text pointer (unused for *NET FS but supplied by star-cmd dispatch)'}, on_exit={'a, x, y': 'clobbered'})


d.subroutine(0xB581, 'cmd_pollps', title='*Pollps command handler', description="""Initialises the spool drive, copies the PS name to
the TX buffer, and parses an optional station number
or PS name argument. Sends a poll request, then
prints the server address and name. Iterates through
PS slots, displaying each station's status as
'ready', 'busy' (with client station), or 'jammed'.
Marks processed slots with &3F.""", on_entry={'y': 'command line offset in text pointer'})
d.entry(0xB6D2)
d.entry(0xB6D6)


d.subroutine(0xB6D2, 'cmd_prot', title='*Prot command handler', description="""Loads `A=&FF` (full protection mask) and falls through (via an
always-taken `BNE`) to the shared protection-update body at
`&B6D8`, which:

1. Saves the new flag (`Z=0` for *Prot, `Z=1` for *Unprot) on the
   stack via `PHP`.
2. Calls [`set_via_shadow_pair`](address:AABB) to mirror `A` into
   the workspace shadow ACR (`ws_0d68`) and shadow IER
   (`ws_0d69`).
3. Reads CMOS RAM byte `&11` (Econet station/protection flags)
   via [`osbyte_a1`](address:8E9A) into `Y`, copies to `A`.
4. Restores the saved flag and selects:
   - *Prot path: `ORA #&40` (set bit 6 = protection on).
   - *Unprot path: `AND #&BF` (clear bit 6).
5. Writes the updated byte back to CMOS via OSBYTE `&A2`
   (write CMOS RAM).

The ANFS protection state lives in CMOS bit 6 of byte `&11`, so it
survives BREAK and power-cycle until explicitly toggled.""", on_entry={'y': 'command line offset (unused; *Prot takes no args)'})


d.subroutine(0xB6D6, 'cmd_unprot', title='*Unprot command handler', description="""Loads `A=&00` (no protection) and falls through to the shared
protection-update body at `&B6D8`, which clears bit 6 of CMOS RAM
byte `&11` (the Econet protection flag). See
[`cmd_prot`](address:B6D2) for the full body description.""", on_entry={'y': 'command line offset (unused; *Unprot takes no args)'})


d.subroutine(0xB3AC, 'cmd_ps', title='*PS command handler', description="""Checks the printer server availability flag; raises
'Printer busy' if unavailable. Initialises the spool
drive and buffer pointer, then dispatches on argument
type: no argument branches to no_ps_name_given, a
leading digit branches to save_ps_cmd_ptr as a station
number, otherwise parses a named PS address via
load_ps_server_addr and parse_fs_ps_args.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8AEA, 'cmd_roff', title='*ROFF command handler', description="""Disables remote operation by clearing the flag at offset 0 in the
receive block. If remote operation was active, re-enables the
keyboard via OSBYTE `&C9` (with `X=0`, `Y=0`) and calls
`tx_econet_abort` with `A=&0A` to reinitialise the workspace
area. Falls through to [`scan_remote_keys`](address:8B00)
which clears `svc_state` and `nfs_workspace`.""", on_entry={'y': 'command line offset (unused -- *ROFF takes no args)'}, on_exit={'a, x, y': 'clobbered'})
d.entry(0x9425)
d.entry(0x9776)
d.entry(0x9512)
d.entry(0xB103)
d.entry(0xA69A)
d.entry(0xA398)
d.entry(0xB0F2)
d.entry(0xB0F8)
d.entry(0x8DD5)
d.entry(0xB312)
d.entry(0x94C5)
d.entry(0xB6F3)

d.label(0x9425, 'cmd_fs_operation')

d.label(0x9776, 'cmd_bye')

d.label(0x9512, 'cmd_dir')

d.label(0xB103, 'cmd_ex')

d.label(0xA69A, 'cmd_flip')

d.label(0xA398, 'cmd_fs')

d.label(0xB0F2, 'cmd_lcat')

d.label(0xB0F8, 'cmd_lex')

d.label(0x8DD5, 'cmd_pass')

d.label(0x94C5, 'cmd_rename')

d.label(0xB6F3, 'cmd_wipe')


d.subroutine(0x9425, 'cmd_fs_operation', title='Shared *Access / *Delete / *Info / *Lib command handler', description="""Copies the command name to the TX buffer, parses a quoted
filename argument via [`parse_quoted_arg`](address:9483), and
checks the access prefix. Validates the filename does not start
with `'&'`, then falls through to
[`read_filename_char`](address:944E) to copy remaining
characters and send the request. Raises
[`Bad file name`](address:9437) if a bare `CR` is found where
a filename was expected.""", on_entry={'y': 'command line offset in text pointer', 'x': 'byte offset within cmd_table_fs identifying which of the four shared commands was matched (Access, Delete, Info, or Lib)'})


d.subroutine(0x9776, 'cmd_bye', title='*Bye command handler', description="""Closes all open file control blocks via
process_all_fcbs, shuts down any *SPOOL/*EXEC files
with OSBYTE &77, and closes all network channels.
Falls through to save_net_tx_cb with function code
&17 to send the bye request to the file server.""")
d.entry(0xB0A0)
d.entry(0xB0A1)


d.subroutine(0xB0A1, 'cmd_cdir', title='*CDir command handler', description="""Parses an optional allocation size argument: if absent, defaults to
index 2 (standard 19-entry directory, `&200` bytes); if present,
parses the decimal value and searches a 26-entry threshold table to
find the matching allocation size index. Parses the directory name
via `parse_filename_arg`, copies it to the TX buffer, and sends FS
command code `&1B` to create the directory.

Reached via PHA/PHA/RTS dispatch from `cmd_table_fs` entry
[`*Cdir`](address:A7B0); the byte at the entry-1 address `&B0A0`
happens to decode as `JMP (cdir_unused_dispatch_table,X)` but is never executed.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x9512, 'cmd_dir', title='*Dir command handler', description="""Handles three argument syntaxes:

| Argument | Action |
|---|---|
| plain path        | delegates to `pass_send_cmd` |
| `'&'` alone       | root directory |
| `'&N.dir'`        | cross-filesystem directory change |

The cross-FS form sends a file-server selection command (code
`&12`) to locate the target server, raising `'Not found'` on
failure, then sends the directory change (code 6) and calls
`find_fs_and_exit` to update the active FS context.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB103, 'cmd_ex', title='*Ex command handler', description="""Unified handler for *Ex, *LCat, and *LEx. Sets the
library flag from carry (CLC for current, SEC for library).
Configures column format: 1 entry per line for Ex
(command 3), 3 per column for Cat (command &0B). Sends the
examine request (code &12), then prints the directory
header: title, cycle number, Owner/Public label, option
name, Dir. and Lib. paths. Paginates through entries,
printing each via ex_print_col_sep until the server
returns zero entries.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xA69A, 'cmd_flip', title='*Flip command handler', description="""Exchanges the CSD and CSL (library) handles. Saves the current
CSD handle from [`hazel_fs_context_copy`](address:C003), loads
the library handle from [`hazel_fs_prefix_stn`](address:C004)
into Y, and calls [`find_station_bit3`](address:A66F) to install
it as the new CSD. Restores the original CSD handle and falls
through to [`flip_set_station_boot`](address:A6A6) to install
it as the new library. Useful when files to be LOADed are in
the library and *DIR/*LIB would be inconvenient.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xA398, 'cmd_fs', title='*FS command handler', description="""Saves the current file server station address, then
checks for a command-line argument. With no argument,
falls through to print_current_fs to display the active
server. With an argument, parses the station number via
parse_fs_ps_args and issues OSWORD &13 (sub-function 1)
to select the new file server.""", on_entry={'y': 'command line offset in text pointer'})
d.entry(0x8D91)


d.subroutine(0x8D91, 'cmd_iam', title='*I AM command handler (file server logon)', description="""Closes any *SPOOL/*EXEC files via OSBYTE &77,
resets all file control blocks via
process_all_fcbs, then parses the command line
for an optional station number and file server
address. If a station number is present, stores
it and calls clear_if_station_match to validate.
Copies the logon command template from
cmd_table_nfs_iam into the transmit buffer and
sends via copy_arg_validated. Falls through to
cmd_pass for password entry.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB0F2, 'cmd_lcat', title='*LCat command handler', description="""Rotates the caller's carry into bit 7 of
[`hazel_fs_lib_flags`](address:C271) (the dispatch path enters
with C=1 so this sets the 'library' flag), then `SEC` / `BCS`
unconditionally jumps to `cat_set_lib_flag` inside
[`cmd_ex`](address:B103) to catalogue the library directory
with three entries per column.""", on_entry={'y': 'command line offset in text pointer', 'c': '1 (set by the cmd_table_fs dispatch path)'})


d.subroutine(0xB0F8, 'cmd_lex', title='*LEx command handler', description="""Rotates the caller's carry into bit 7 of
[`hazel_fs_lib_flags`](address:C271) (the dispatch path enters
with C=1 so this sets the 'library' flag), then jumps to
`ex_set_lib_flag` inside [`cmd_ex`](address:B103) to examine
the library directory with one entry per line.""", on_entry={'y': 'command line offset in text pointer', 'c': '1 (set by the cmd_table_fs dispatch path)'})


d.subroutine(0x8D02, 'issue_svc_15', title='Issue OSBYTE 143 service 15 (vectors-claimed) request', description='Tail-call wrapper that loads X=&0F (service number 15) and tail-jumps to OSBYTE 143 (issue paged ROM service request), which broadcasts service 15 to all sideways ROMs. ANFS calls this from svc_2_private_workspace after claiming its workspace, to give other ROMs a chance to react.', on_entry={'a': 'OSBYTE result is irrelevant -- this is fire-and-forget'})


d.subroutine(0x8E9A, 'osbyte_a1', title='OSBYTE &A1 (read Master CMOS RAM byte)', description="""Loads `A=&A1` and tail-jumps to `OSBYTE` – reads the Master 128
CMOS RAM byte indexed by `X`. Two callers:
[`format_filename_field`](address:A0E3) and
[`flip_set_station_boot`](address:A70D).

**Dual-use trick:** the 5 bytes `A9 A1 4C F4 FF` also serve as
the leading slot of the vector-dispatch table that
[`write_vector_entry`](address:904F) reads via
`LDA osbyte_a1,Y` – a deliberate overlap so the routine's body
doubles as table data.""", on_entry={'x': 'CMOS RAM byte index'}, on_exit={'y': 'CMOS byte read', 'x': 'preserved'})


d.subroutine(0x988F, 'check_escape_and_classify', title='Acknowledge escape (if pressed) and classify reply', description="""If escape_flag bit 7 is clear OR need_release_tube bit 7 is clear (so AND result has bit 7 clear), returns immediately via return_1. Otherwise acknowledges escape via OSBYTE &7E (clears the escape condition and runs escape effects), loads A=6 (a synthesized 'Escape' error class), and tail-jumps to classify_reply_error to build the 'Escape' BRK error block.

Two callers: cmd_pass (&8DEF) for password-entry escape, and send_net_packet (&9B48) for in-flight TX escape.""", on_entry={}, on_exit={'a': 'preserved (return) or never returns (escape path)'})


d.subroutine(0x8DD5, 'cmd_pass', title='*PASS command handler (change password)', description="""Builds the FS command packet via copy_arg_to_buf_x0,
then scans the reply buffer for a ':' separator
indicating a password prompt. If found, reads
characters from the keyboard without echo, handling
Delete (&7F) for backspace and NAK (&15) to restart
from the colon position. Sends the completed
password to the file server via save_net_tx_cb and
branches to send_cmd_and_dispatch for the reply.""", on_entry={'y': 'command line offset in text pointer (also the entry point for cmd_iam fall-through)'})


d.subroutine(0xB303, 'print_decimal_3dig_no_spool', title='Print 3-digit decimal via *SPOOL-bypassing print', description="As print_decimal_3dig (&B32A) but each digit is emitted via print_char_no_spool, which closes the *SPOOL handle around OSASCI so the digit doesn't appear in any active capture. Always prints all three digits (no leading-zero suppression).", on_entry={'a': 'value 0-255'})


d.subroutine(0xB310, 'print_decimal_digit_no_spool', title='Print one decimal digit, *SPOOL-bypassing', description='As print_decimal_digit (&B338) but emits via print_char_no_spool. fs_error_ptr is used as scratch storage for the divisor and is preserved across the print.', on_entry={'a': 'divisor (100, 10, or 1)', 'y': 'value to divide'}, on_exit={'y': 'remainder after division'})


d.subroutine(0x94C5, 'cmd_rename', title='*Rename command handler', description="""Parses two space-separated filenames from the command line, each
with its own access prefix. Sets the owner-only access mask
before parsing each name. Validates that both names resolve to
the same file server by comparing the FS-options word – raises
`'Bad rename'` if they differ. Falls through to
[`read_filename_char`](address:944E) to copy the second
filename into the TX buffer and send the request.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB6F3, 'cmd_wipe', title='*Wipe command handler', description="""Setup half of *Wipe. Masks owner access via
[`mask_owner_access`](address:B2CF), zeroes the file-iteration
counter [`fs_work_5`](address:00B5), preserves the command-line
pointer with [`save_ptr_to_os_text`](address:B373), parses the
wildcard filename via [`parse_filename_arg`](address:B22C), and
records the end-of-argument offset (X+1) in
[`fs_work_6`](address:00B6). Falls through to
[`request_next_wipe`](address:B703), which drives the per-file
examine/prompt/delete loop until the wildcard is exhausted.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB7CB, 'prompt_yn', title='Print Y/N prompt and read user response', description="""Prints 'Y/N) ' via inline string, flushes
the input buffer, and reads a single character
from the keyboard.""", on_entry={}, on_exit={'A': "character read from keyboard (after the 'Y/N) ' prompt)"})
d.entry(0x8BC4)
d.entry(0x8BC0)

d.label(0x8BC4, 'help_net')

d.label(0x8BC0, 'help_utils')


d.subroutine(0x8BC4, 'help_net', title='*HELP NET topic handler', description="""Sets `X = &35` (the NFS command sub-table offset) and falls
through to [`print_cmd_table`](address:8BC6) to display the
NFS command list with version header.""", on_entry={'y': 'command-line offset (PHA/PHA/RTS dispatch contract)'}, on_exit={'a, x, y': 'clobbered (print_cmd_table)'})


d.subroutine(0x8BC0, 'help_utils', title='*HELP UTILS topic handler', description="""Sets `X = 0` to select the utility command sub-table and branches
to [`print_cmd_table`](address:8BC6) to display the command
list. Prints the version header followed by all utility
commands.""", on_entry={'y': 'command-line offset (PHA/PHA/RTS dispatch contract)'}, on_exit={'a, x, y': 'clobbered'})
d.entry(0x8C29)
d.entry(0x93F7)
d.entry(0x9C22)
d.entry(0x9EAB)
d.entry(0x9FC2)
d.entry(0xA14C)
d.entry(0xA28A)
d.entry(0xAC47)
d.entry(0xAD64)
d.entry(0xAE6F)
d.entry(0xBB68)
d.entry(0x8549)
for i in range(5):
    d.byte(0x853B + i)
d.expr(0x853B, '<(tx_done_jsr-1)')
d.expr(0x853C, '<(tx_done_econet_event-1)')
d.expr(0x853D, '<(tx_done_os_proc-1)')
d.expr(0x853E, '<(tx_done_halt-1)')
d.expr(0x853F, '<(tx_done_continue-1)')
d.comment(0x853B, 'op &83: remote JSR', align=Align.INLINE)
d.comment(0x853C, 'op &84: fire Econet event', align=Align.INLINE)
d.comment(0x853D, 'op &85: OSProc call', align=Align.INLINE)
d.comment(0x853E, 'op &86: HALT', align=Align.INLINE)
d.comment(0x853F, 'op &87: CONTINUE', align=Align.INLINE)
d.entry(0x8686)
for i in range(8):
    d.byte(0x867E + i)
d.expr(0x867E, '<(tx_ctrl_peek-1)')
d.expr(0x867F, '<(tx_ctrl_poke-1)')
d.expr(0x8680, '<(proc_op_status2-1)')
d.expr(0x8681, '<(proc_op_status2-1)')
d.expr(0x8682, '<(proc_op_status2-1)')
d.expr(0x8683, '<(tx_ctrl_exit-1)')
d.expr(0x8684, '<(tx_ctrl_exit-1)')
d.expr(0x8685, '<(tx_ctrl_machine_type-1)')
d.comment(0x867E, 'ctrl &81: PEEK', align=Align.INLINE)
d.comment(0x867F, 'ctrl &82: POKE', align=Align.INLINE)
d.comment(0x8680, 'ctrl &83: JSR', align=Align.INLINE)
d.comment(0x8681, 'ctrl &84: UserProc', align=Align.INLINE)
d.comment(0x8682, 'ctrl &85: OSProc', align=Align.INLINE)
d.comment(0x8683, 'ctrl &86: HALT', align=Align.INLINE)
d.comment(0x8684, 'ctrl &87: CONTINUE', align=Align.INLINE)
d.comment(0x8685, 'ctrl &88: machine type', align=Align.INLINE)
d.byte(0x88F0, 16, cols=16)
d.entry(0x84BE)
d.entry(0x84CE)
d.entry(0x88F0)
d.entry(0xA874)
d.entry(0xA910)
d.entry(0xA92D)
d.entry(0xA985)
d.entry(0xA99A)
d.entry(0xB357)
d.entry(0x9619)
d.entry(0x9623)
d.entry(0x9630)
d.entry(0x959A)
d.entry(0x95EE)
d.entry(0x8E71)
d.entry(0x8E73)
d.entry(0x8E8A)
d.entry(0xB2DB)
d.entry(0x969A)
d.entry(0xACFC)
d.entry(0xBBE7)


d.subroutine(0x8EA7, 'fs_vector_table', title='FS vector dispatch and handler addresses (34 bytes)', description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by loop_set_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the extended vector table.

Bytes 14-33: handler address pairs read by write_vector_entry.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (write_vector_entry writes the current ROM
bank number instead). The last entry (FSCV) has no padding
byte.""")

d.label(0xA02F, 'findv_handler')

d.label(0x8E4B, 'fscv_handler')
_ev_dispatch = ['ev_filev', 'ev_argsv', 'ev_bgetv', 'ev_bputv', 'ev_gbpbv', 'ev_findv', 'ev_fscv']
for i, ev in enumerate(_ev_dispatch):
    addr = 0x8EA7 + i * 2
    d.word(addr)
    d.expr(addr, ev)
    d.comment(addr, '%s dispatch' % ev[3:].upper(), align=Align.INLINE)
handler_names = [('FILEV', 'filev_handler'), ('ARGSV', 'argsv_handler'), ('BGETV', 'bgetv_handler'), ('BPUTV', 'bputv_handler'), ('GBPBV', 'gbpbv_handler'), ('FINDV', 'findv_handler'), ('FSCV', 'fscv_handler')]
for i, (name, handler_label) in enumerate(handler_names):
    base_addr = 0x8EB5 + i * 3
    d.word(base_addr)
    d.expr(base_addr, handler_label)
    d.comment(base_addr, '%s handler' % name, align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, '(ROM bank — not read)', align=Align.INLINE)

d.label(0x8E9F, 'ps_template_data')
d.banner(0x8E9F, title='Printer-server name template (8 bytes)', description="""Eight bytes (`"PRINT "` then `&01 &00`) read by
[`copy_ps_data`](address:B3D5) via the indexed-base trick
`LDA ps_template_base+X` with `X=&F8..&FF`. The base label
`ps_template_base` resolves to `ps_template_data - &F8` so the
indexed access lands on the bytes here. Default contents installed
into the Printer-Server name slot during ANFS initialisation.""")

d.label(0xACFC, 'netv_handler')

d.label(0x9AB3, 'msg_net_error')

d.label(0x9ABE, 'msg_station')

d.label(0x9AC7, 'msg_no_clock')

d.label(0x9AD1, 'msg_escape')

d.label(0x9AD9, 'msg_bad_option')

d.label(0x9AE5, 'msg_no_reply')

d.label(0x9AFC, 'msg_not_listening')

d.label(0x9B0B, 'msg_on_channel')

d.label(0x9B17, 'msg_not_present')
d.comment(0x8A6E, 'svc 13 fail path', align=Align.INLINE)
d.comment(0x9119, 'syntax help for *Pass / *I am', align=Align.INLINE)
d.comment(0x9193, 'syntax help for *PS / *Pollps', align=Align.INLINE)
d.comment(0x9AA7, 'err_line_jammed = &A0', align=Align.INLINE)
d.comment(0x9AB4, 'err_net_error = &A1', align=Align.INLINE)
d.comment(0xB1D1, 'label for *Ex output', align=Align.INLINE)
d.comment(0xB49B, "fragment for 'File/Printer server is ...' messages", align=Align.INLINE)
d.comment(0xBE07, '*Dump column header', align=Align.INLINE)
d.comment(0xBE24, '*Dump trailer', align=Align.INLINE)
d.comment(0xBEDE, '*Dump range error', align=Align.INLINE)
d.comment(0x9691, "'!Help.' prefix bytes (not used by the matcher; may be visible as a fallback help-message head)", align=Align.INLINE)
d.comment(0x9697, "'ON ' -- 3-char pattern read by match_on_suffix at &969A via EOR &9697,X with X=0..2 to detect '... ON ' help-line suffix", align=Align.INLINE)
d.comment(0xB575, 'Offset 0: txcb_ctrl = &80 (standard)', align=Align.INLINE)
d.comment(0xB576, 'Offset 1: txcb_port = &9F (PS port)', align=Align.INLINE)
d.comment(0xB577, 'Offset 2: dest station (placeholder, &00)', align=Align.INLINE)
d.comment(0xB578, 'Offset 3: dest network (placeholder, &00)', align=Align.INLINE)
d.comment(0xB579, 'Offset 4: buf1 start lo = &10', align=Align.INLINE)
d.comment(0xB57A, 'Offset 5: buf1 start hi (page from net_rx_ptr)', align=Align.INLINE)
d.comment(0xB57B, 'Offset 6: buf1 end lo placeholder = &FF', align=Align.INLINE)
d.comment(0xB57C, 'Offset 7: buf1 end hi placeholder = &FF', align=Align.INLINE)
d.comment(0xB57D, 'Offset 8: buf2 start lo = &18', align=Align.INLINE)
d.comment(0xB57E, 'Offset 9: buf2 start hi (page from net_rx_ptr)', align=Align.INLINE)
d.comment(0xB57F, 'Offset 10: buf2 end lo placeholder = &FF', align=Align.INLINE)
d.comment(0xB580, 'Offset 11: buf2 end hi placeholder = &FF', align=Align.INLINE)
d.comment(0xBFC5, 'ROM-tail padding (2 bytes &FF)', align=Align.INLINE)
d.comment(0xBFC7, 'ROM-tail padding (1 byte &FF; on its own line for annotation)', align=Align.INLINE)
d.comment(0xBFC8, 'ROM-tail padding (30 bytes &FF)', align=Align.INLINE)
d.comment(0xBFE6, 'Base for `hazel_minus_1a,Y` reads in loop_copy_txcb_init -- `&BFE6 + Y` reaches into HAZEL for Y >= &1A', align=Align.INLINE)
d.comment(0xBFFE, 'Base for `hazel_minus_2,Y` reads/writes -- `&BFFE + Y` reaches into HAZEL for Y >= 2 (used by loop_copy_fs_ctx, loop_restore_ctx, loop_copy_ws_to_pb)', align=Align.INLINE)
d.comment(0xBFFF, 'Base for `hazel_minus_1,Y` reads/writes -- `&BFFF + Y` reaches into HAZEL for Y >= 1 (used by loop_copy_station, osword_13_set_station)', align=Align.INLINE)
d.byte(0x9AD0)
d.byte(0x9AD1)
d.byte(0x9AD9)
d.byte(0x9B0A)
d.byte(0x9B16)
d.byte(0x8D45)
d.comment(0x8D45, 'CR', align=Align.INLINE)
d.byte(0x8D5E)
d.comment(0x8D5E, 'CR', align=Align.INLINE)
d.string(0x8D6E, 2)
d.byte(0x8D84)
d.comment(0x8D84, 'CR', align=Align.INLINE)

d.label(0xA740, 'boot_load_cmd')


d.subroutine(0x8E61, 'svc_dispatch', title='PHA/PHA/RTS table dispatch', description="""Computes a target index by incrementing `X` and decrementing `Y`
until `Y` goes negative, effectively calculating `X+Y+1`. Pushes
the target address (high then low byte) from
[`svc_dispatch_lo`](address:89ED) /
[`svc_dispatch_hi`](address:8A20) onto the stack, loads
`fs_options` into `X`, then `RTS` jumps to the target
subroutine. Used for all service dispatch, FS command execution,
and OSBYTE handler routing.

Routine extent is &8E61-&8E70 (the `RTS` is the dispatch). The
short Master service handlers at
[`noop_dey_rts`](address:8E71) (svc &24),
[`copy_template_to_zp`](address:8E73) (svc &25) and
[`svc_26_close_all_files`](address:8E8A) sit immediately after.""", on_entry={'x': 'base dispatch index', 'y': 'additional offset'}, on_exit={'x': 'fs_options value'})


d.subroutine(0x8E71, 'noop_dey_rts', title='Service &24: dynamic workspace claim (1 page)', description="""Two-byte handler reached via [`svc_dispatch`](address:8E61) slot
&13. `DEY` decrements the caller's first-available-page count by 1
to claim a single workspace page; `RTS` returns to the dispatcher.""")


d.subroutine(0x8E73, 'copy_template_to_zp', title='Service &25: FS name + info reply', description="""Reached via [`svc_dispatch`](address:8E61) slot &14. Copies the
11-byte template at [`fs_info_template`](address:8E7F) into the
caller's workspace at `(os_text_ptr),Y`. The loop counts `X`
down from 10 to 0 reading from `template[X]`, while `Y`
increments from the caller's value, so the destination ends up
holding the template byte-reversed (`'NET      /' + length-byte`).
Returns via the shared `RTS` at
[`fs_template_done`](address:8E7E).""")


d.subroutine(0x8E8A, 'svc_26_close_all_files', title='Service &26: close all files (FILEV via Y=0)', description="""Reached via [`svc_dispatch`](address:8E61) slot &15. Tests bit 6
of [`fs_flags`](address:0D6C) (NFS-active flag). If clear, branches
back to the shared `RTS` at [`fs_template_done`](address:8E7E)
without acting. Otherwise calls
[`ensure_fs_selected`](address:8B4D) to make NFS the current
filing system, sets `A=Y=0` and tail-calls
[`findv_handler`](address:A02F) — the FILEV `Y=0` path closes all
open NFS channels.""")


d.subroutine(0x8EC9, 'osbyte_x0', title='OSBYTE wrapper with X=0, Y=&FF', description="""Sets X=0 and falls through to osbyte_yff to also
set Y=&FF. Provides a single call to execute
OSBYTE with A as the function code. Used by
adlc_init, init_adlc_and_vectors, and Econet
OSBYTE handling.""", on_entry={'a': 'OSBYTE function code'}, on_exit={'x': '0', 'y': '&FF'})


d.subroutine(0x8ECB, 'osbyte_yff', title='OSBYTE wrapper with Y=&FF', description="""Sets Y=&FF and JMPs to the MOS OSBYTE entry
point. X must already be set by the caller. The
osbyte_x0 entry point falls through to here after
setting X=0.""", on_entry={'a': 'OSBYTE function code', 'x': 'OSBYTE X parameter'}, on_exit={'y': '&FF'})

d.label(0x8EC9, 'osbyte_x0')

d.label(0x8ECB, 'osbyte_yff')


d.subroutine(0x9261, 'print_inline', title='Print inline string, high-bit terminated', description="""Pops the return address from the stack, prints each byte via
`OSASCI` until a byte with bit 7 set is found, then jumps to that
address. The high-bit byte serves as both the string terminator
and the opcode of the first instruction after the string.

Common terminators:

| Byte | Opcode | Effect |
|---|---|---|
| `&EA` | `NOP`  | fall-through |
| `&B8` | `CLV`  | followed by `BVC` for an unconditional forward branch |""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by OSASCI)', 'y': '0'})


d.subroutine(0x928A, 'print_inline_no_spool', title='Print inline string, high-bit terminated, *SPOOL-bypassing', description="""As [`print_inline`](address:9261), but each character is
emitted via [`print_char_no_spool`](address:91FB) instead of
`OSASCI` directly, so the printed text does not appear in any
active `*SPOOL` capture.

Used by status output that should not be saved to a spool file
(e.g. `*Wipe` `'(Y/N) '` prompts, `*Ex` column separators, the
`'Bad ROM'` service-handler message via the
`recv_and_process_reply` `'Data Lost'` warning, and inline-string
arguments inside [`cmd_ex`](address:B103)'s directory
listing).

Six callers: `&981A` (`recv_and_process_reply`), `&B158`/`&B162`
([`cmd_ex`](address:B103)), `&B2F0` (`ex_print_col_sep`),
`&B75E` ([`cmd_wipe`](address:B6F3)), `&B7CB`
(`prompt_yn`).""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by print_char_no_spool)', 'y': '0'})
d.comment(0x9261, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x9264, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x9269, 'Advance pointer to next character', align=Align.INLINE)
d.comment(0x926F, 'Load next byte from inline string', align=Align.INLINE)
d.comment(0x9271, 'Bit 7 set? Done — this byte is the next opcode', align=Align.INLINE)
d.comment(0x9279, 'Reload character (pointer may have been clobbered)', align=Align.INLINE)
d.comment(0x927B, 'Print character via OSASCI', align=Align.INLINE)
d.comment(0x9287, 'Jump to address of high-bit byte (resumes code)', align=Align.INLINE)


d.subroutine(0x99C3, 'error_inline', title='Generate BRK error from inline string', description="""Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""", on_entry={'a': 'error number (stored in error block at &0101)'})
d.comment(0x99C3, 'Save error number in Y', align=Align.INLINE)
d.comment(0x99C4, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x99C7, 'Pop return address (high)', align=Align.INLINE)


d.subroutine(0x99C0, 'error_inline_log', title='Generate BRK error from inline string (with logging)', description="""Like error_inline, but first conditionally logs the error code to
workspace via cond_save_error_code before building the error block.""", on_entry={'a': 'error number'})
d.comment(0x99C0, 'Conditionally log error code to workspace', align=Align.INLINE)


d.subroutine(0x99A7, 'error_bad_inline', title="Generate 'Bad ...' BRK error from inline string", description="""Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""", on_entry={'a': 'error number'})
d.comment(0x99A7, 'Conditionally log error code to workspace', align=Align.INLINE)
d.comment(0x99AA, 'Save error number in Y', align=Align.INLINE)
d.comment(0x99AB, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x99AC, 'Store return address low', align=Align.INLINE)
d.comment(0x99AE, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x99AF, 'Store return address high', align=Align.INLINE)
d.comment(0x99B1, 'X=0: start of prefix string', align=Align.INLINE)
d.comment(0x99B3, "Copy 'Bad ' prefix from lookup table", align=Align.INLINE)
d.comment(0x99B4, 'Get next prefix character', align=Align.INLINE)
d.comment(0x99B7, 'Store in error text buffer', align=Align.INLINE)
d.comment(0x99BA, "Is it space (end of 'Bad ')?", align=Align.INLINE)
d.comment(0x99BC, 'No: copy next prefix character', align=Align.INLINE)
d.comment(0x99CC, 'Store error number in error block', align=Align.INLINE)
d.comment(0x99D3, 'Zero the BRK byte at &0100', align=Align.INLINE)
d.comment(0x99D6, 'Copy inline string into error block', align=Align.INLINE)
d.comment(0x99D8, 'Read next byte from inline string', align=Align.INLINE)
d.comment(0x99DD, 'Loop until null terminator', align=Align.INLINE)
d.comment(0x99DF, 'Read receive attribute byte', align=Align.INLINE)
d.comment(0xB0A3, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xB0A6, 'Skip to optional size argument', align=Align.INLINE)
d.comment(0xB0A9, 'End of line?', align=Align.INLINE)
d.comment(0xB0AB, 'No: parse size argument', align=Align.INLINE)
d.comment(0xB0AD, 'Default allocation size index = 2', align=Align.INLINE)
d.comment(0xB0B1, 'A=&FF: mark as decimal parse', align=Align.INLINE)
d.comment(0xB0B3, 'Store decimal parse flag', align=Align.INLINE)
d.comment(0xB0B5, 'Parse numeric size argument', align=Align.INLINE)
d.comment(0xB0B8, 'X=&1B: top of 26-entry size table', align=Align.INLINE)
d.comment(0xB0BA, 'Try next lower index', align=Align.INLINE)
d.comment(0xB0BB, 'Compare size with threshold', align=Align.INLINE)
d.comment(0xB0BE, 'A < threshold: keep searching', align=Align.INLINE)
d.comment(0xB0C0, 'Store allocation size index', align=Align.INLINE)
d.comment(0xB0C3, 'Restore command line offset', align=Align.INLINE)
d.comment(0xB0C4, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB0C5, 'Save text pointer for filename parse', align=Align.INLINE)
d.comment(0xB0C8, 'Parse directory name argument', align=Align.INLINE)
d.comment(0xB0CB, 'X=1: one argument to copy', align=Align.INLINE)
d.comment(0xB0CD, 'Copy directory name to TX buffer', align=Align.INLINE)
d.comment(0xB0D0, 'Y=&1B: *CDir FS command code', align=Align.INLINE)
d.comment(0xB0D2, 'Send command to file server', align=Align.INLINE)

d.label(0xB0D5, 'cdir_alloc_size_table')
d.banner(0xB0D5, title='*CDir allocation size threshold table (26 entries)', description="""26 thresholds dividing 0-255 into size classes for the *CDir
directory-size argument. Table base is at `cdir_dispatch_col+2`
(overlapping the JMP operand high byte just before the table); the search
loop (`LDX #&1B` / `DEX` / `CMP table,X` / `BCC`) scans indices
26 down to 0. Index 0 reads `&94` from the JMP and is unreachable
because index 1 (threshold `&00`) always matches first. The
resulting `X` (1-26) is the allocation size class sent to the
file server. Default when no size argument is given: index 2.""")
d.comment(0xB0D5, 'Index 1: threshold 0 (catch-all)', align=Align.INLINE)
d.comment(0xB0D6, 'Index 2: threshold 10 (default)', align=Align.INLINE)
d.comment(0xB0D7, 'Index 3: threshold 20', align=Align.INLINE)
d.comment(0xB0DC, 'Index 8: threshold 69', align=Align.INLINE)
d.comment(0xB0DE, 'Index 10: threshold 88', align=Align.INLINE)
d.comment(0xB0DF, 'Index 11: threshold 98', align=Align.INLINE)
d.comment(0xB0E0, 'Index 12: threshold 108', align=Align.INLINE)
d.comment(0xB0E3, 'Index 15: threshold 138', align=Align.INLINE)
d.comment(0xB0E4, 'Index 16: threshold 148', align=Align.INLINE)
d.comment(0xB0E6, 'Index 18: threshold 167', align=Align.INLINE)
d.comment(0xB0E7, 'Index 19: threshold 177', align=Align.INLINE)
d.comment(0xB0E9, 'Index 21: threshold 197', align=Align.INLINE)
d.comment(0xB0EB, 'Index 23: threshold 216', align=Align.INLINE)
d.comment(0xB0EC, 'Index 24: threshold 226', align=Align.INLINE)
d.comment(0xB0ED, 'Index 25: threshold 236', align=Align.INLINE)
d.comment(0xB0F2, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xB0F5, 'Set carry (= library directory)', align=Align.INLINE)
d.comment(0xB0F8, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xB0FB, 'Set carry (= library directory)', align=Align.INLINE)
d.comment(0xB6D2, 'Load &FF (protect)', align=Align.INLINE)
d.comment(0xB6D6, 'Load &00 (unprotect)', align=Align.INLINE)
d.comment(0xB6D8, 'Save Z flag (1 = unprot, 0 = prot) for later', align=Align.INLINE)
d.comment(0xB6D9, 'Mirror A into ws_0d68 / ws_0d69 pair', align=Align.INLINE)
d.comment(0xB6DC, 'X=&11: CMOS offset for Econet flags', align=Align.INLINE)
d.comment(0xB6DE, 'OSBYTE &A1 reads CMOS byte &11 -> Y', align=Align.INLINE)
d.comment(0xB6E1, 'A = current CMOS byte', align=Align.INLINE)
d.comment(0xB6E2, 'Restore the saved Z flag', align=Align.INLINE)
d.comment(0xB6E3, 'Z=1: unprot path', align=Align.INLINE)
d.comment(0xB6E5, 'Set bit 6 (protection on)', align=Align.INLINE)
d.comment(0xB6E7, 'ALWAYS branch to write-back', align=Align.INLINE)
d.comment(0xB6E9, 'Clear bit 6 (protection off)', align=Align.INLINE)
d.comment(0xB6EB, 'Y = new flag byte', align=Align.INLINE)
d.comment(0xB6EC, 'OSBYTE &A2: write CMOS byte', align=Align.INLINE)
d.comment(0xB6EE, 'X=&11: CMOS offset for Econet flags', align=Align.INLINE)
d.comment(0xB6F0, 'Tail-call OSBYTE', align=Align.INLINE)
d.comment(0x9425, "Copy command name 'Access'/'Delete'/'Info'/'Lib' to TX buffer", align=Align.INLINE)
d.comment(0x9429, 'Parse quoted filename argument from command line', align=Align.INLINE)
d.comment(0x942C, 'Parse the access prefix (e.g. L,W,R) into a bitmask', align=Align.INLINE)
d.comment(0x9430, "Reject '&' character in filename", align=Align.INLINE)
d.comment(0x9433, 'End of line?', align=Align.INLINE)
d.comment(0x9435, 'No: copy filename chars to buffer', align=Align.INLINE)
d.comment(0x9437, 'Error number &CC', align=Align.INLINE)
d.comment(0x9439, "Raise 'Bad file name' error", align=Align.INLINE)
d.comment(0x9446, 'Load first parsed character', align=Align.INLINE)
d.comment(0x9449, "Is it '&'?", align=Align.INLINE)
d.comment(0x944B, 'Yes: invalid filename', align=Align.INLINE)
d.comment(0x944D, 'Return', align=Align.INLINE)
d.comment(0x944E, "Reject '&' in current char", align=Align.INLINE)
d.comment(0x9451, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x9454, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9455, 'End of line?', align=Align.INLINE)
d.comment(0x9457, 'Yes: send request to file server', align=Align.INLINE)
d.comment(0x9459, 'Strip BASIC token prefix byte', align=Align.INLINE)
d.comment(0x9464, 'Scan backwards in command table', align=Align.INLINE)
d.comment(0x9465, 'Load table byte', align=Align.INLINE)
d.comment(0x9468, 'Bit 7 clear: keep scanning', align=Align.INLINE)
d.comment(0x946A, 'Point past flag byte to name start', align=Align.INLINE)
d.comment(0x946B, 'Y=0: TX buffer offset', align=Align.INLINE)
d.comment(0x946D, 'Load command name character', align=Align.INLINE)
d.comment(0x9470, 'Bit 7 set: end of name', align=Align.INLINE)
d.comment(0x9472, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x9475, 'Advance table pointer', align=Align.INLINE)
d.comment(0x9476, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9477, 'Continue copying name', align=Align.INLINE)
d.comment(0x9479, 'Space separator', align=Align.INLINE)
d.comment(0x947B, 'Append space after command name', align=Align.INLINE)
d.comment(0x947E, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x947F, 'Transfer length to A', align=Align.INLINE)
d.comment(0x9480, 'And to X (buffer position)', align=Align.INLINE)
d.comment(0x9482, 'Return', align=Align.INLINE)
d.comment(0x9483, 'A=0: no quote mode', align=Align.INLINE)
d.comment(0x9486, 'Clear quote tracking flag', align=Align.INLINE)
d.comment(0x9489, 'Load char from command line', align=Align.INLINE)
d.comment(0x948B, 'Space?', align=Align.INLINE)
d.comment(0x948D, 'No: check for opening quote', align=Align.INLINE)
d.comment(0x948F, 'Skip leading space', align=Align.INLINE)
d.comment(0x9490, 'Continue skipping spaces', align=Align.INLINE)
d.comment(0x9492, 'Double-quote character?', align=Align.INLINE)
d.comment(0x9494, 'No: start reading filename', align=Align.INLINE)
d.comment(0x9496, 'Skip opening quote', align=Align.INLINE)
d.comment(0x9497, 'Toggle quote mode flag', align=Align.INLINE)
d.comment(0x949A, 'Store updated quote mode', align=Align.INLINE)
d.comment(0x949D, 'Load char from command line', align=Align.INLINE)
d.comment(0x949F, 'Double-quote?', align=Align.INLINE)
d.comment(0x94A1, 'No: store character as-is', align=Align.INLINE)
d.comment(0x94A3, 'Toggle quote mode', align=Align.INLINE)
d.comment(0x94A6, 'Store updated quote mode', align=Align.INLINE)
d.comment(0x94A9, 'Replace closing quote with space', align=Align.INLINE)
d.comment(0x94AB, 'Store character in parse buffer', align=Align.INLINE)
d.comment(0x94AE, 'Advance command line pointer', align=Align.INLINE)
d.comment(0x94AF, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x94B0, 'End of line?', align=Align.INLINE)
d.comment(0x94B2, 'No: continue parsing', align=Align.INLINE)
d.comment(0x94B4, 'Check quote balance flag', align=Align.INLINE)
d.comment(0x94B7, 'Balanced: return OK', align=Align.INLINE)
d.comment(0x94B9, 'Unbalanced: use BRK ptr for error', align=Align.INLINE)
d.comment(0x94BB, "Raise 'Bad string' error", align=Align.INLINE)
d.comment(0x94D3, 'Load next parsed character', align=Align.INLINE)
d.comment(0x94D6, 'End of line?', align=Align.INLINE)
d.comment(0x94D8, 'No: store character', align=Align.INLINE)
d.comment(0x94DA, 'Error number &B0', align=Align.INLINE)
d.comment(0x94DC, "Raise 'Bad rename' error", align=Align.INLINE)
d.comment(0x94E6, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x94E9, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x94EA, 'Space (name separator)?', align=Align.INLINE)
d.comment(0x94EC, 'Yes: first name complete', align=Align.INLINE)
d.comment(0x94EE, 'Strip BASIC token prefix byte', align=Align.INLINE)
d.comment(0x94F3, 'Strip token from next char', align=Align.INLINE)
d.comment(0x94F6, 'Load next parsed character', align=Align.INLINE)
d.comment(0x94F9, 'Still a space?', align=Align.INLINE)
d.comment(0x94FB, 'Yes: skip multiple spaces', align=Align.INLINE)
d.comment(0x94FD, 'Save current FS options', align=Align.INLINE)
d.comment(0x9500, 'Push them', align=Align.INLINE)
d.comment(0x9501, 'Reset access mask for second name', align=Align.INLINE)
d.comment(0x9509, 'Restore original FS options', align=Align.INLINE)
d.comment(0x950A, 'Options changed (cross-FS)?', align=Align.INLINE)
d.comment(0x950D, "Yes: error (can't rename across FS)", align=Align.INLINE)
d.comment(0x950F, 'Copy second filename and send', align=Align.INLINE)
d.comment(0x9512, 'Get first char of argument', align=Align.INLINE)
d.comment(0x9514, "Is it '&' (FS selector prefix)?", align=Align.INLINE)
d.comment(0x9516, 'No: simple dir change', align=Align.INLINE)
d.comment(0x9518, "Skip '&'", align=Align.INLINE)
d.comment(0x9519, "Get char after '&'", align=Align.INLINE)
d.comment(0x951B, 'End of line?', align=Align.INLINE)
d.comment(0x951D, "Yes: '&' alone (root directory)", align=Align.INLINE)
d.comment(0x951F, 'Space?', align=Align.INLINE)
d.comment(0x9521, "No: check for '.' separator", align=Align.INLINE)
d.comment(0x9523, 'Y=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0x9525, 'Advance index', align=Align.INLINE)
d.comment(0x9526, 'Load char from command line', align=Align.INLINE)
d.comment(0x9528, 'Copy to TX buffer', align=Align.INLINE)
d.comment(0x952B, "Is it '&' (end of FS path)?", align=Align.INLINE)
d.comment(0x952D, 'No: keep copying', align=Align.INLINE)
d.comment(0x952F, "Replace '&' with CR terminator", align=Align.INLINE)
d.comment(0x9531, 'Store CR in buffer', align=Align.INLINE)
d.comment(0x9534, 'Point past CR', align=Align.INLINE)
d.comment(0x9535, 'Transfer length to A', align=Align.INLINE)
d.comment(0x9536, 'And to X (byte count)', align=Align.INLINE)
d.comment(0x9537, 'Send directory request to server', align=Align.INLINE)
d.comment(0x953A, "Is char after '&' a dot?", align=Align.INLINE)
d.comment(0x953C, 'Yes: &FS.dir format', align=Align.INLINE)
d.comment(0x953E, 'No: invalid syntax', align=Align.INLINE)
d.comment(0x9541, "Skip '.'", align=Align.INLINE)
d.comment(0x9542, 'Save dir path start position', align=Align.INLINE)
d.comment(0x9544, 'FS command 4: examine directory', align=Align.INLINE)
d.comment(0x9546, 'Store in TX buffer', align=Align.INLINE)
d.comment(0x9549, 'Load FS flags', align=Align.INLINE)
d.comment(0x954C, 'Set bit 6 (FS selection active)', align=Align.INLINE)
d.comment(0x954E, 'Store updated flags', align=Align.INLINE)
d.comment(0x9551, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9553, 'Copy FS number to buffer', align=Align.INLINE)
d.comment(0x9556, 'Y=&12: select FS command code', align=Align.INLINE)
d.comment(0x9558, 'Send FS selection command', align=Align.INLINE)
d.comment(0x955B, 'Load reply status', align=Align.INLINE)
d.comment(0x955E, 'Status 2 (found)?', align=Align.INLINE)
d.comment(0x9560, 'Yes: proceed to dir change', align=Align.INLINE)
d.comment(0x9562, 'Error number &D6', align=Align.INLINE)
d.comment(0x9564, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0x9571, 'Load current FS station byte', align=Align.INLINE)
d.comment(0x9574, 'Store in TX buffer', align=Align.INLINE)
d.comment(0x9577, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9579, 'Y=7: change directory command code', align=Align.INLINE)
d.comment(0x957B, 'Send directory change request', align=Align.INLINE)
d.comment(0x957E, 'X=1', align=Align.INLINE)
d.comment(0x9580, 'Store start marker in buffer', align=Align.INLINE)
d.comment(0x9583, 'Store start marker in buffer+1', align=Align.INLINE)
d.comment(0x9587, 'Restore dir path start position', align=Align.INLINE)
d.comment(0x9589, 'Copy directory path to buffer', align=Align.INLINE)
d.comment(0x958C, 'Y=6: set directory command code', align=Align.INLINE)
d.comment(0x958E, 'Send set directory command', align=Align.INLINE)
d.comment(0x9591, 'Load reply handle', align=Align.INLINE)
d.comment(0x9594, 'Select FS and return', align=Align.INLINE)
d.comment(0x9597, 'Simple: pass command to FS', align=Align.INLINE)
d.comment(0x973D, 'A=&90: bye command port', align=Align.INLINE)
d.comment(0x973F, 'Initialise TXCB from template', align=Align.INLINE)
d.comment(0x9742, 'Set transmit port', align=Align.INLINE)
d.comment(0x9744, 'A=3: data start offset', align=Align.INLINE)
d.comment(0x9746, 'Set TXCB start offset', align=Align.INLINE)
d.comment(0x9748, 'Open receive: &80->&7F (bit 7 clear = awaiting reply)', align=Align.INLINE)
d.comment(0x974A, 'Return', align=Align.INLINE)
d.comment(0x974B, 'Save A', align=Align.INLINE)
d.comment(0x974C, 'Y=&0B: template size - 1', align=Align.INLINE)
d.comment(0x974E, 'Load byte from TXCB template', align=Align.INLINE)
d.comment(0x9751, 'Store to TXCB workspace', align=Align.INLINE)
d.comment(0x9754, 'Index >= 2?', align=Align.INLINE)
d.comment(0x9756, 'Yes: skip dest station copy', align=Align.INLINE)
d.comment(0x9758, 'Load dest station byte', align=Align.INLINE)
d.comment(0x975B, 'Store to TXCB destination', align=Align.INLINE)
d.comment(0x975E, 'Decrement index', align=Align.INLINE)
d.comment(0x975F, 'More bytes: continue', align=Align.INLINE)
d.comment(0x9761, 'Restore A', align=Align.INLINE)
d.comment(0x9762, 'Return', align=Align.INLINE)
d.comment(0x976F, 'Save A', align=Align.INLINE)
d.comment(0x9770, 'Set carry (read-only mode)', align=Align.INLINE)
d.comment(0x9773, 'Clear V', align=Align.INLINE)
d.comment(0xA69A, 'Load current CSD handle', align=Align.INLINE)
d.comment(0xA69D, 'Save CSD handle', align=Align.INLINE)
d.comment(0xA69E, 'Load library handle into Y', align=Align.INLINE)
d.comment(0xA6A1, 'Install library as new CSD', align=Align.INLINE)
d.comment(0xA6A4, 'Restore original CSD handle', align=Align.INLINE)
d.comment(0xA6A5, 'Y = original CSD (becomes library)', align=Align.INLINE)
d.comment(0xA6A6, 'X=&10: max 16 station entries', align=Align.INLINE)
d.comment(0xA6A8, 'Clear V (no match found yet)', align=Align.INLINE)
d.comment(0xA6A9, 'Decrement station index', align=Align.INLINE)
d.comment(0xA6AA, 'All searched: exit loop', align=Align.INLINE)
d.comment(0xA6AC, 'Check if station[X] matches', align=Align.INLINE)
d.comment(0xA6AF, 'No match: try next station', align=Align.INLINE)
d.comment(0xA6B1, 'Load station flags byte', align=Align.INLINE)
d.comment(0xA6B4, 'Test bit 4 (active flag)', align=Align.INLINE)
d.comment(0xA6B6, 'Not active: try next station', align=Align.INLINE)
d.comment(0xA6B8, 'Transfer boot type to A', align=Align.INLINE)
d.comment(0xA6B9, 'Store boot setting for station', align=Align.INLINE)
d.comment(0xA6BC, 'Set V flag (station match found)', align=Align.INLINE)
d.comment(0xA6BF, 'Store boot type', align=Align.INLINE)
d.comment(0xA6C2, 'V set (matched): skip allocation', align=Align.INLINE)
d.comment(0xA6C4, 'Boot type to A', align=Align.INLINE)
d.comment(0xA6C5, 'Allocate FCB slot for new entry', align=Align.INLINE)
d.comment(0xA6C8, 'Store allocation result', align=Align.INLINE)
d.comment(0xA6CB, 'Zero: allocation failed, exit', align=Align.INLINE)
d.comment(0xA6CD, 'A=&32: station flags (active+boot)', align=Align.INLINE)
d.comment(0xA6CF, 'Store station flags', align=Align.INLINE)
d.comment(0xA6D2, 'Restore FS context and return', align=Align.INLINE)
d.comment(0xA6D5, 'Close all network channels', align=Align.INLINE)
d.comment(0xA6E5, 'Save processor status', align=Align.INLINE)
d.comment(0xA6E6, 'Load station number from reply', align=Align.INLINE)
d.comment(0xA6E9, 'Find station entry with bit 2', align=Align.INLINE)
d.comment(0xA6EC, 'Load network number from reply', align=Align.INLINE)
d.comment(0xA6EF, 'Find station entry with bit 3', align=Align.INLINE)
d.comment(0xA6F2, 'Load boot type from reply', align=Align.INLINE)
d.comment(0xA6F5, 'Set boot config for station', align=Align.INLINE)
d.comment(0xA6F8, 'Restore processor status', align=Align.INLINE)
d.comment(0xA6F9, 'Carry set: proceed with boot', align=Align.INLINE)
d.comment(0xA6FB, 'Return with last flag', align=Align.INLINE)
d.comment(0xA726, 'Load config flags', align=Align.INLINE)
d.comment(0xA729, 'Save copy in X', align=Align.INLINE)
d.comment(0xA72A, 'Test bit 2 (auto-boot flag)', align=Align.INLINE)
d.comment(0xA72C, 'Save bit 2 test result', align=Align.INLINE)
d.comment(0xA72D, 'Restore full flags', align=Align.INLINE)
d.comment(0xA72E, 'Clear bit 2 (consume flag)', align=Align.INLINE)
d.comment(0xA730, 'Store cleared flags', align=Align.INLINE)
d.comment(0xA733, 'Restore bit 2 test result', align=Align.INLINE)
d.comment(0xA734, 'Bit 2 was set: skip to boot cmd', align=Align.INLINE)
d.comment(0xA736, 'OSBYTE &79: scan keyboard', align=Align.INLINE)
d.comment(0xA73E, 'CTRL not pressed: proceed to boot', align=Align.INLINE)
d.comment(0xA740, 'CTRL pressed: cancel boot, return', align=Align.INLINE)
d.comment(0xB312, 'Convert remaining value to A', align=Align.INLINE)
d.comment(0xB327, 'Set V (suppress leading zeros)', align=Align.INLINE)
d.comment(0xB32A, 'Transfer value to Y (remainder)', align=Align.INLINE)
d.comment(0xB32B, 'A=100: hundreds divisor', align=Align.INLINE)
d.comment(0xB32D, 'Print hundreds digit', align=Align.INLINE)
d.comment(0xB330, 'A=10: tens divisor', align=Align.INLINE)
d.comment(0xB332, 'Print tens digit', align=Align.INLINE)
d.comment(0xB335, 'Clear V (always print units)', align=Align.INLINE)
d.comment(0xB336, 'A=1: units divisor', align=Align.INLINE)
d.comment(0xB338, 'Store divisor', align=Align.INLINE)
d.comment(0xB33A, 'Get remaining value', align=Align.INLINE)
d.comment(0xB33B, "X='0'-1: digit counter", align=Align.INLINE)
d.comment(0xB33D, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xB33E, 'Save V flag for leading zero check', align=Align.INLINE)
d.comment(0xB33F, 'Count quotient digit', align=Align.INLINE)
d.comment(0xB340, 'Subtract divisor', align=Align.INLINE)
d.comment(0xB342, 'No underflow: continue dividing', align=Align.INLINE)
d.comment(0xB344, 'Add back divisor (get remainder)', align=Align.INLINE)
d.comment(0xB346, 'Remainder to Y for next digit', align=Align.INLINE)
d.comment(0xB347, 'Digit character to A', align=Align.INLINE)
d.comment(0xB348, 'Restore V flag', align=Align.INLINE)
d.comment(0xB349, 'V clear: always print digit', align=Align.INLINE)
d.comment(0xB34B, "V set: is digit '0'?", align=Align.INLINE)
d.comment(0xB34D, 'Yes: suppress leading zero', align=Align.INLINE)
d.comment(0xB34F, 'Save divisor across OSASCI call', align=Align.INLINE)
d.comment(0xB354, 'Restore divisor', align=Align.INLINE)
d.comment(0xB356, 'Return', align=Align.INLINE)
d.comment(0xB373, 'Save A', align=Align.INLINE)
d.comment(0xB374, 'Copy text pointer low byte', align=Align.INLINE)
d.comment(0xB376, 'To OS text pointer low', align=Align.INLINE)
d.comment(0xB378, 'Copy text pointer high byte', align=Align.INLINE)
d.comment(0xB37A, 'To OS text pointer high', align=Align.INLINE)
d.comment(0xB37C, 'Restore A', align=Align.INLINE)
d.comment(0xB37D, 'Return', align=Align.INLINE)
d.comment(0xB37E, 'Advance past current character', align=Align.INLINE)
d.comment(0xB37F, 'Load char from command line', align=Align.INLINE)
d.comment(0xB381, 'Space?', align=Align.INLINE)
d.comment(0xB383, 'Yes: skip trailing spaces', align=Align.INLINE)
d.comment(0xB385, 'CR (end of line)?', align=Align.INLINE)
d.comment(0xB387, 'Yes: return (at end)', align=Align.INLINE)
d.comment(0xB38B, 'Advance past space', align=Align.INLINE)
d.comment(0xB38C, 'Load next character', align=Align.INLINE)
d.comment(0xB38E, 'Still a space?', align=Align.INLINE)
d.comment(0xB390, 'Yes: skip multiple spaces', align=Align.INLINE)
d.comment(0xB392, 'Return (at next argument)', align=Align.INLINE)
d.comment(0xB393, 'Save A', align=Align.INLINE)
d.comment(0xB394, 'Copy text pointer low byte', align=Align.INLINE)
d.comment(0xB396, 'To spool buffer pointer low', align=Align.INLINE)
d.comment(0xB398, 'Copy text pointer high byte', align=Align.INLINE)
d.comment(0xB39A, 'To spool buffer pointer high', align=Align.INLINE)
d.comment(0xB39C, 'Restore A', align=Align.INLINE)
d.comment(0xB39D, 'Return', align=Align.INLINE)
d.comment(0xB39E, 'Save Y', align=Align.INLINE)
d.comment(0xB39F, 'Push it', align=Align.INLINE)
d.comment(0xB3A0, 'Get workspace page number', align=Align.INLINE)
d.comment(0xB3A3, 'Store as spool drive page high', align=Align.INLINE)
d.comment(0xB3A5, 'Restore Y', align=Align.INLINE)
d.comment(0xB3A6, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB3A7, 'A=0', align=Align.INLINE)
d.comment(0xB3A9, 'Clear spool drive page low', align=Align.INLINE)
d.comment(0xB3AB, 'Return', align=Align.INLINE)
d.comment(0xBD25, 'Test bit 7 of escape flag', align=Align.INLINE)
d.comment(0xBD27, 'Escape pressed: handle abort', align=Align.INLINE)
d.comment(0xBD29, 'No escape: return', align=Align.INLINE)
d.comment(0xBD2A, 'Close the open file', align=Align.INLINE)
d.comment(0xBD30, 'Acknowledge escape condition', align=Align.INLINE)
d.comment(0xBD35, 'Error number &11', align=Align.INLINE)
d.comment(0xBD37, "Generate 'Escape' BRK error", align=Align.INLINE)
d.comment(0xB581, 'Save command line pointer high', align=Align.INLINE)
d.comment(0xB583, 'Initialise spool/print drive', align=Align.INLINE)
d.comment(0xB586, 'Save spool drive number', align=Align.INLINE)
d.comment(0xB588, 'Copy PS name to TX buffer', align=Align.INLINE)
d.comment(0xB58B, 'Init PS slot from RX data', align=Align.INLINE)
d.comment(0xB58E, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB590, 'Save pointer to spool buffer', align=Align.INLINE)
d.comment(0xB593, 'Get first argument character', align=Align.INLINE)
d.comment(0xB595, 'End of command line?', align=Align.INLINE)
d.comment(0xB597, 'Yes: no argument given', align=Align.INLINE)
d.comment(0xB599, 'Clear V (= explicit PS name given)', align=Align.INLINE)
d.comment(0xB59A, 'Is first char a decimal digit?', align=Align.INLINE)
d.comment(0xB59D, 'Yes: station number, skip PS name', align=Align.INLINE)
d.comment(0xB59F, 'PS name follows', align=Align.INLINE)
d.comment(0xB5A0, 'Save Y', align=Align.INLINE)
d.comment(0xB5A1, 'Load PS server address', align=Align.INLINE)
d.comment(0xB5A4, 'Restore Y', align=Align.INLINE)
d.comment(0xB5A5, 'Back to Y register', align=Align.INLINE)
d.comment(0xB5A6, 'Parse FS/PS arguments', align=Align.INLINE)
d.comment(0xB5A9, 'Offset &7A in slot buffer', align=Align.INLINE)
d.comment(0xB5AB, 'Get parsed station low', align=Align.INLINE)
d.comment(0xB5AD, 'Store station number low', align=Align.INLINE)
d.comment(0xB5B0, 'Get parsed network number', align=Align.INLINE)
d.comment(0xB5B2, 'Store station number high', align=Align.INLINE)
d.comment(0xB5B4, 'Offset &14 in TX buffer', align=Align.INLINE)
d.comment(0xB5B6, 'Copy PS data to TX buffer', align=Align.INLINE)
d.comment(0xB5B9, 'Get buffer page high', align=Align.INLINE)
d.comment(0xB5BB, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0xB5BD, 'Offset &78 in buffer', align=Align.INLINE)
d.comment(0xB5BF, 'Set TX pointer low byte', align=Align.INLINE)
d.comment(0xB5C3, 'Set V (= no explicit PS name)', align=Align.INLINE)
d.comment(0xB5C6, 'V set (no arg): skip to send', align=Align.INLINE)
d.comment(0xB5C8, 'Max 6 characters for PS name', align=Align.INLINE)
d.comment(0xB5CA, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB5CC, 'Space character', align=Align.INLINE)
d.comment(0xB5CE, 'Fill buffer position with space', align=Align.INLINE)
d.comment(0xB5D0, 'Next position', align=Align.INLINE)
d.comment(0xB5D1, 'Count down', align=Align.INLINE)
d.comment(0xB5D2, 'Loop until 6 spaces filled', align=Align.INLINE)
d.comment(0xB5D4, 'Save pointer to OS text', align=Align.INLINE)
d.comment(0xB5D7, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB5D9, 'Initialise string reading', align=Align.INLINE)
d.comment(0xB5DC, 'Empty string: skip to send', align=Align.INLINE)
d.comment(0xB5DE, 'Max 6 characters', align=Align.INLINE)
d.comment(0xB5E0, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB5E2, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB5E4, 'Save buffer position', align=Align.INLINE)
d.comment(0xB5E6, 'Restore string pointer', align=Align.INLINE)
d.comment(0xB5E8, 'Read next char from string', align=Align.INLINE)
d.comment(0xB5EB, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB5ED, 'End of string: go to send', align=Align.INLINE)
d.comment(0xB5EF, 'Store char uppercased in buffer', align=Align.INLINE)
d.comment(0xB5F2, 'Loop if more chars to copy', align=Align.INLINE)
d.comment(0xB5F4, 'Enable escape checking', align=Align.INLINE)
d.comment(0xB5F6, 'Set escapable flag', align=Align.INLINE)
d.comment(0xB5F8, 'Send the poll request packet', align=Align.INLINE)
d.comment(0xB5FB, 'Pop and requeue PS scan', align=Align.INLINE)
d.comment(0xB5FE, "Print 'Printer server '", align=Align.INLINE)
d.comment(0xB601, 'Load PS server address', align=Align.INLINE)
d.comment(0xB604, 'Set V and N flags', align=Align.INLINE)
d.comment(0xB607, 'Print station address', align=Align.INLINE)
d.comment(0xB60A, 'Print \' "\'', align=Align.INLINE)
d.comment(0xB611, 'Get character from name field', align=Align.INLINE)
d.comment(0xB613, 'Is it a space?', align=Align.INLINE)
d.comment(0xB615, 'Yes: end of name', align=Align.INLINE)
d.comment(0xB61A, 'Next character', align=Align.INLINE)
d.comment(0xB61B, 'Past end of name field?', align=Align.INLINE)
d.comment(0xB61D, 'No: continue printing name', align=Align.INLINE)
d.comment(0xB61F, 'Print \'"\' + CR', align=Align.INLINE)
d.comment(0xB626, 'Zero: all slots done, return', align=Align.INLINE)
d.comment(0xB628, 'Save slot offset', align=Align.INLINE)
d.comment(0xB629, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB62A, 'Read slot status byte', align=Align.INLINE)
d.comment(0xB62C, 'Bit 7 clear: slot inactive', align=Align.INLINE)
d.comment(0xB62E, 'Advance to station number', align=Align.INLINE)
d.comment(0xB62F, 'Offset+2 in slot', align=Align.INLINE)
d.comment(0xB630, 'Read station number low', align=Align.INLINE)
d.comment(0xB632, 'Store station low', align=Align.INLINE)
d.comment(0xB634, 'Next byte (offset+3)', align=Align.INLINE)
d.comment(0xB635, 'Read network number', align=Align.INLINE)
d.comment(0xB637, 'Store network number', align=Align.INLINE)
d.comment(0xB639, 'Next byte (offset+4)', align=Align.INLINE)
d.comment(0xB63A, 'Read status page pointer', align=Align.INLINE)
d.comment(0xB63C, 'Store pointer low', align=Align.INLINE)
d.comment(0xB63E, 'Clear V flag', align=Align.INLINE)
d.comment(0xB63F, 'Print station address (V=0)', align=Align.INLINE)
d.comment(0xB642, "Print ' is '", align=Align.INLINE)
d.comment(0xB64B, 'Read printer status byte', align=Align.INLINE)
d.comment(0xB64D, 'Non-zero: not ready', align=Align.INLINE)
d.comment(0xB64F, "Print 'ready'", align=Align.INLINE)
d.comment(0xB65A, 'Status = 2?', align=Align.INLINE)
d.comment(0xB65C, 'No: check for busy', align=Align.INLINE)
d.comment(0xB65E, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB667, 'Clear V', align=Align.INLINE)
d.comment(0xB66A, 'Status = 1?', align=Align.INLINE)
d.comment(0xB66C, 'Not 1 or 2: default to jammed', align=Align.INLINE)
d.comment(0xB66E, "Print 'busy'", align=Align.INLINE)
d.comment(0xB677, 'Read client station number', align=Align.INLINE)
d.comment(0xB679, 'Store station low', align=Align.INLINE)
d.comment(0xB67B, 'Zero: no client info, skip', align=Align.INLINE)
d.comment(0xB67D, "Print ' with station '", align=Align.INLINE)
d.comment(0xB692, 'Store network number', align=Align.INLINE)
d.comment(0xB694, 'Set V flag', align=Align.INLINE)
d.comment(0xB697, 'Print client station address', align=Align.INLINE)
d.comment(0xB69D, 'Retrieve slot offset', align=Align.INLINE)
d.comment(0xB69E, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB69F, 'Mark slot as processed (&3F)', align=Align.INLINE)
d.comment(0xB6A1, 'Write marker to workspace', align=Align.INLINE)
d.comment(0xB6A5, 'Return', align=Align.INLINE)
d.comment(0xB6A6, 'Start at offset &78', align=Align.INLINE)
d.comment(0xB6A8, 'Load template byte', align=Align.INLINE)
d.comment(0xB6AB, 'At offset &7D?', align=Align.INLINE)
d.comment(0xB6AD, 'Yes: substitute RX page', align=Align.INLINE)
d.comment(0xB6AF, 'At offset &81?', align=Align.INLINE)
d.comment(0xB6B1, 'No: use template byte', align=Align.INLINE)
d.comment(0xB6B3, 'Use RX buffer page instead', align=Align.INLINE)
d.comment(0xB6B5, 'Store byte in slot buffer', align=Align.INLINE)
d.comment(0xB6B7, 'Next offset', align=Align.INLINE)
d.comment(0xB6B8, 'Past end of slot (&84)?', align=Align.INLINE)
d.comment(0xB6BA, 'No: continue copying', align=Align.INLINE)
d.comment(0xB6BC, 'Return', align=Align.INLINE)
d.comment(0xB6BD, 'Y = current buffer position', align=Align.INLINE)
d.comment(0xB6BF, 'Strip high bit', align=Align.INLINE)
d.comment(0xB6C1, "Is it lowercase 'a' or above?", align=Align.INLINE)
d.comment(0xB6C3, "Below 'a': not lowercase", align=Align.INLINE)
d.comment(0xB6C5, "Above 'z'?", align=Align.INLINE)
d.comment(0xB6C7, 'Yes: not lowercase', align=Align.INLINE)
d.comment(0xB6C9, 'Convert to uppercase', align=Align.INLINE)
d.comment(0xB6CB, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB6CD, 'Next buffer position', align=Align.INLINE)
d.comment(0xB6CE, 'Update buffer position', align=Align.INLINE)
d.comment(0xB6D0, 'Decrement character count', align=Align.INLINE)
d.comment(0xB6D1, 'Return (Z set if count=0)', align=Align.INLINE)
d.comment(0xB103, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xB106, 'Clear carry (= current directory)', align=Align.INLINE)
d.comment(0xB107, 'Rotate carry back, clearing bit 7', align=Align.INLINE)
d.comment(0xB10A, 'A=&FF: initial column counter', align=Align.INLINE)
d.comment(0xB10C, 'Store column counter', align=Align.INLINE)
d.comment(0xB10E, 'One entry per line (Ex format)', align=Align.INLINE)
d.comment(0xB110, 'Store entries per page', align=Align.INLINE)
d.comment(0xB112, 'FS command code 3: Examine', align=Align.INLINE)
d.comment(0xB114, 'Store command code', align=Align.INLINE)
d.comment(0xB118, 'Set transfer parameters', align=Align.INLINE)
d.comment(0xB11B, 'Y=0: start from entry 0', align=Align.INLINE)
d.comment(0xB11D, 'Rotate carry into lib flag', align=Align.INLINE)
d.comment(0xB120, 'Clear carry (= current directory)', align=Align.INLINE)
d.comment(0xB121, 'Rotate carry back, clearing bit 7', align=Align.INLINE)
d.comment(0xB124, 'Three entries per column (Cat)', align=Align.INLINE)
d.comment(0xB126, 'Store column counter', align=Align.INLINE)
d.comment(0xB128, 'Store entries per page', align=Align.INLINE)
d.comment(0xB12A, 'FS command code &0B: Catalogue', align=Align.INLINE)
d.comment(0xB12C, 'Store command code', align=Align.INLINE)
d.comment(0xB12E, 'Save text pointer', align=Align.INLINE)
d.comment(0xB131, 'A=&FF: enable escape checking', align=Align.INLINE)
d.comment(0xB133, 'Set escapable flag', align=Align.INLINE)
d.comment(0xB135, 'Command code 6', align=Align.INLINE)
d.comment(0xB137, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB13A, 'Parse directory argument', align=Align.INLINE)
d.comment(0xB13D, 'X=1: offset in buffer', align=Align.INLINE)
d.comment(0xB13F, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0xB142, 'Get library/FS flags', align=Align.INLINE)
d.comment(0xB145, 'Shift bit 0 to carry', align=Align.INLINE)
d.comment(0xB146, 'Bit 0 clear: skip', align=Align.INLINE)
d.comment(0xB148, 'Set bit 6 (owner access flag)', align=Align.INLINE)
d.comment(0xB14A, 'Rotate back', align=Align.INLINE)
d.comment(0xB14B, 'Store modified flags', align=Align.INLINE)
d.comment(0xB14E, 'Y=&12: FS command for examine', align=Align.INLINE)
d.comment(0xB150, 'Send request to file server', align=Align.INLINE)
d.comment(0xB153, 'X=3: offset to directory title', align=Align.INLINE)
d.comment(0xB155, 'Print directory title (10 chars)', align=Align.INLINE)
d.comment(0xB158, "Print '('", align=Align.INLINE)
d.comment(0xB15C, 'Load FS object-type code from hazel_txcb_objtype (file/dir/etc)', align=Align.INLINE)
d.comment(0xB162, "Print ')     ' to close the type-code field", align=Align.INLINE)
d.comment(0xB170, "Print 'Owner' + CR", align=Align.INLINE)
d.comment(0xB17B, "Print 'Public' + CR", align=Align.INLINE)
d.comment(0xB189, 'Mask owner access bits', align=Align.INLINE)
d.comment(0xB18C, 'Y=&15: FS command for dir info', align=Align.INLINE)
d.comment(0xB18E, 'Send request to file server', align=Align.INLINE)
d.comment(0xB191, 'Advance X past header', align=Align.INLINE)
d.comment(0xB192, 'Y=&10: print 16 chars', align=Align.INLINE)
d.comment(0xB194, 'Print file entry', align=Align.INLINE)
d.comment(0xB197, "Print '    Option '", align=Align.INLINE)
d.comment(0xB1A8, 'Transfer to X for table lookup', align=Align.INLINE)
d.comment(0xB1A9, 'Print option as hex', align=Align.INLINE)
d.comment(0xB1AC, "Print ' ('", align=Align.INLINE)
d.comment(0x94BE, 'Store to TXCB', align=Align.INLINE)
d.comment(0x94E4, 'Add 5 for header size', align=Align.INLINE)
d.comment(0x9567, 'Store null terminator (A=0 from EOR)', align=Align.INLINE)
d.comment(0x956A, 'Get message length', align=Align.INLINE)
d.comment(0x956D, 'Go to error dispatch', align=Align.INLINE)
d.comment(0x9586, 'Non-zero: commit state and return', align=Align.INLINE)
d.comment(0x95EE, 'Read flag byte for matched cmd entry (syntax idx in bits 0..4)', align=Align.INLINE)
d.comment(0x95F1, 'Mask off end-marker (bit 7) and V-if-no-arg flag (bit 6)', align=Align.INLINE)
d.comment(0x95F3, 'X = CMOS byte index (1=FS stn, 3=PS stn)', align=Align.INLINE)
d.comment(0x95F4, 'Save CMOS index', align=Align.INLINE)
d.comment(0x95F5, "Save caller's command-line cursor", align=Align.INLINE)
d.comment(0x95F6, 'Save CMOS index again (consumed by first PLX below)', align=Align.INLINE)
d.comment(0x95F7, 'Read existing CMOS[idx] (current station)', align=Align.INLINE)
d.comment(0x95FA, 'Default station if user gives no args', align=Align.INLINE)
d.comment(0x95FC, 'Recover CMOS index from stack', align=Align.INLINE)
d.comment(0x95FD, 'X+=1: advance to network byte', align=Align.INLINE)
d.comment(0x95FE, 'Read existing CMOS[idx+1] (current network)', align=Align.INLINE)
d.comment(0x9601, 'Default network if user gives no args', align=Align.INLINE)
d.comment(0x9603, 'Restore command-line cursor', align=Align.INLINE)
d.comment(0x9604, "Parse '<net>.<stn>'; updates fs_work_5/6/7 if args present", align=Align.INLINE)
d.comment(0x9607, 'Recover CMOS index from stack', align=Align.INLINE)
d.comment(0x9608, 'Re-save CMOS index for second write', align=Align.INLINE)
d.comment(0x9609, 'Y = station (parsed or pre-read default)', align=Align.INLINE)
d.comment(0x960B, 'Write CMOS[idx] = station', align=Align.INLINE)
d.comment(0x960E, 'Recover CMOS index from stack', align=Align.INLINE)
d.comment(0x960F, 'X+=1: advance to network byte', align=Align.INLINE)
d.comment(0x9610, 'Y = raw parsed network (NOT canonical fs_work_6); fall through into osbyte_a2 to write CMOS[idx+1]', align=Align.INLINE)
d.comment(0xA07E, 'Save to fs_work_5', align=Align.INLINE)
d.comment(0xA080, 'Load current FS station low', align=Align.INLINE)
d.comment(0xA083, 'Save to fs_work_6', align=Align.INLINE)
d.comment(0xA087, 'Is it CR (no argument)?', align=Align.INLINE)
d.comment(0xA094, 'Parameter block low', align=Align.INLINE)
d.comment(0xA096, 'Parameter block high', align=Align.INLINE)
d.comment(0xA0A1, 'Clear hazel_fcb_addr_mid for slot Y', align=Align.INLINE)
d.comment(0xA0A7, 'Z still set from LDA #0: always branch to done_close', align=Align.INLINE)
d.comment(0xA0A9, 'A=0 (init sub-code): jump to store_display_flag', align=Align.INLINE)
d.comment(0xA0AB, 'Non-zero A: X==4? (read OSARGS args)', align=Align.INLINE)
d.comment(0xA0AD, 'X != 4: take normal OSARGS dispatch', align=Align.INLINE)
d.comment(0xA0B3, 'X-- (osargs_dispatch entry): step sub-code down', align=Align.INLINE)
d.comment(0xA0B4, 'X != 1: take store-ptr-lo path', align=Align.INLINE)
d.comment(0xA0B9, 'Tail-branch to done_close', align=Align.INLINE)
d.comment(0xA0BB, 'A=7: error code (out-of-range OSARGS sub-code)', align=Align.INLINE)
d.comment(0xA0BD, 'Raise BRK error', align=Align.INLINE)
d.comment(0xA0C0, 'Store Y as TXCB data byte (OSARGS payload)', align=Align.INLINE)
d.comment(0xA0C5, 'Send OSARGS request via TX control block', align=Align.INLINE)
d.comment(0xA0CA, 'Update hazel_fs_flags from OSARGS reply', align=Align.INLINE)
d.comment(0xA0CF, 'X >= 8?', align=Align.INLINE)
d.comment(0xA0D1, 'Yes: out-of-range OSARGS sub-code', align=Align.INLINE)
d.comment(0xA0D3, 'X == 4?', align=Align.INLINE)
d.comment(0xA0D5, 'Yes: take fast read path (osargs_check_length)', align=Align.INLINE)
d.comment(0xA0D7, 'Y < 4?', align=Align.INLINE)
d.comment(0xA0D9, 'Yes: take CMOS-protect path', align=Align.INLINE)
d.comment(0xA0DB, 'Y >= 2?', align=Align.INLINE)
d.comment(0xA0DD, 'Yes: argument out of range', align=Align.INLINE)
d.comment(0xA0E0, 'Save sub-code across the CMOS read', align=Align.INLINE)
d.comment(0xA0E3, 'Read CMOS &11 (Econet status) -> Y', align=Align.INLINE)
d.comment(0xA0E6, 'Restore sub-code', align=Align.INLINE)
d.comment(0xA0E8, 'Mask CMOS &11 with cmos_opt_mask_table[X]', align=Align.INLINE)
d.comment(0xA0ED, 'Load shift count from cmos_attr_table[X]', align=Align.INLINE)
d.comment(0xA0F1, "Caller's Y back to A as the value to shift", align=Align.INLINE)
d.comment(0xA0F3, 'Count down shift iterations', align=Align.INLINE)
d.comment(0xA0F4, 'Loop until X reaches 0', align=Align.INLINE)
d.comment(0xA0F6, 'Stash shifted value in fs_load_addr scratch', align=Align.INLINE)
d.comment(0xA0F9, 'OR with the CMOS-masked value', align=Align.INLINE)
d.comment(0xA0FC, 'X=&11: target CMOS byte for write-back', align=Align.INLINE)
d.comment(0xA101, 'Tail-branch into the OSARGS done path', align=Align.INLINE)
d.comment(0xA129, "Generate 'Syntax' error", align=Align.INLINE)
d.comment(0xA133, 'Clear carry for the upcoming 4-byte add', align=Align.INLINE)
d.comment(0xA13A, 'Push high byte', align=Align.INLINE)
d.comment(0xA13F, 'RTS dispatches to command handler', align=Align.INLINE)
d.comment(0xA45B, 'Save command-line offset Y on stack', align=Align.INLINE)
d.comment(0xA45D, 'Reload saved Y (peek without popping)', align=Align.INLINE)
d.comment(0xA45E, 'Push it back to keep on stack', align=Align.INLINE)
d.comment(0xA45F, 'Y = saved command-line offset', align=Align.INLINE)
d.comment(0xA460, 'First char of current entry name', align=Align.INLINE)
d.comment(0xA463, 'Bit 7 set already: end of table', align=Align.INLINE)
d.comment(0xA465, 'Next char from table', align=Align.INLINE)
d.comment(0xA468, 'Bit 7 set: name fully matched', align=Align.INLINE)
d.comment(0xA46C, 'Mask off case bit (5)', align=Align.INLINE)
d.comment(0xA46E, 'Mismatch (after case mask): skip entry', align=Align.INLINE)
d.comment(0xA470, 'Advance command-line offset', align=Align.INLINE)
d.comment(0xA471, 'Advance table offset', align=Align.INLINE)
d.comment(0xA472, 'ALWAYS branch: continue matching', align=Align.INLINE)
d.comment(0xA474, 'Skip remaining name chars', align=Align.INLINE)
d.comment(0xA475, 'Load next table byte', align=Align.INLINE)
d.comment(0xA478, 'Bit 7 clear: continue skipping', align=Align.INLINE)
d.comment(0xA47A, 'Char on command line at current Y', align=Align.INLINE)
d.comment(0xA47C, 'Is it `.` (abbreviation)?', align=Align.INLINE)
d.comment(0xA47E, 'Yes: accept abbreviated match', align=Align.INLINE)
d.comment(0xA480, 'Skip 3-byte handler trailer (flag, lo, hi)', align=Align.INLINE)
d.comment(0xA483, 'ALWAYS branch: try next entry', align=Align.INLINE)
d.comment(0xA485, 'Save matched-name length on stack', align=Align.INLINE)
d.comment(0xA487, 'Char on command line just past name', align=Align.INLINE)
d.comment(0xA489, 'Y=9: separator-table size - 1', align=Align.INLINE)
d.comment(0xA48B, 'Compare with separator', align=Align.INLINE)
d.comment(0xA48E, 'Match: valid command boundary', align=Align.INLINE)
d.comment(0xA490, 'Try next separator', align=Align.INLINE)
d.comment(0xA491, 'Loop through 10 separators', align=Align.INLINE)
d.comment(0xA493, 'Restore matched-name length', align=Align.INLINE)
d.comment(0xA495, 'ALWAYS branch: try next entry', align=Align.INLINE)
d.comment(0xA4A0, 'Restore matched-name length', align=Align.INLINE)
d.comment(0xA4A1, 'Y = matched-name length', align=Align.INLINE)
d.comment(0xA4A2, 'Char on command line at current Y', align=Align.INLINE)
d.comment(0xA4A4, 'Is it space?', align=Align.INLINE)
d.comment(0xA4A6, "No: check the entry's no-arg flag", align=Align.INLINE)
d.comment(0xA4A8, 'Advance past the space (or `.`)', align=Align.INLINE)
d.comment(0xA4A9, 'Loop: keep skipping', align=Align.INLINE)
d.comment(0xA4AC, "Load entry's flag byte (post-name)", align=Align.INLINE)
d.comment(0xA4AF, 'Shift bit 7 into C: the no-arg bit', align=Align.INLINE)
d.comment(0xA4B0, 'C=0: entry allows arguments', align=Align.INLINE)
d.comment(0xA4B2, 'Char on command line', align=Align.INLINE)
d.comment(0xA4B4, 'Is it CR (no argument)?', align=Align.INLINE)
d.comment(0xA4B6, 'Argument present, V clear', align=Align.INLINE)
d.comment(0xA4B8, 'Force V=1: entry validated as match', align=Align.INLINE)
d.comment(0xA4BB, 'V set: skip the CLV', align=Align.INLINE)
d.comment(0xA4BD, 'Clear V (no-arg flag not asserted)', align=Align.INLINE)
d.comment(0xA4BE, 'Clear C (no error / no-arg path)', align=Align.INLINE)
d.comment(0xA4BF, 'Discard saved Y on stack', align=Align.INLINE)
d.comment(0xA4C0, 'A = current command-line char', align=Align.INLINE)
d.comment(0xA4C2, 'Return (Z=1 on match, C and V set per result)', align=Align.INLINE)
d.comment(0xA4C3, 'Advance command-line offset', align=Align.INLINE)
d.comment(0xA4C4, 'Char on command line', align=Align.INLINE)
d.comment(0xA4C6, 'Is it CR (end of input)?', align=Align.INLINE)
d.comment(0xA4C8, 'Yes: set C and return (no match)', align=Align.INLINE)
d.comment(0xA4CA, 'Is it `.`?', align=Align.INLINE)
d.comment(0xA4CC, 'Yes: skip separator spaces', align=Align.INLINE)
d.comment(0xA4CE, 'Is it space?', align=Align.INLINE)
d.comment(0xA4D0, 'No: keep scanning past word', align=Align.INLINE)
d.comment(0xA4D2, 'Advance past space', align=Align.INLINE)
d.comment(0xA4D3, 'Load next char', align=Align.INLINE)
d.comment(0xA4D5, 'Still space?', align=Align.INLINE)
d.comment(0xA4D7, 'Yes: keep skipping', align=Align.INLINE)
d.comment(0xA4D9, 'Set C: signal no-match return path', align=Align.INLINE)
d.comment(0xA4DA, 'ALWAYS branch to common return', align=Align.INLINE)
d.comment(0x8D09, 'Save Y on stack', align=Align.INLINE)
d.comment(0x8D0A, 'X=&11: CMOS offset for Econet station-flags', align=Align.INLINE)
d.comment(0x8D0C, 'Read CMOS byte: result in Y', align=Align.INLINE)
d.comment(0x8D0F, 'A = CMOS byte', align=Align.INLINE)
d.comment(0x8D10, "Restore caller's Y", align=Align.INLINE)
d.comment(0x8D11, 'Isolate bit 0 (page-&0B fallback flag)', align=Align.INLINE)
d.comment(0x8D13, "Bit clear: keep caller's Y", align=Align.INLINE)
d.comment(0x8D15, "Caller's Y already >= &10?", align=Align.INLINE)
d.comment(0x8D17, 'Yes: keep it', align=Align.INLINE)
d.comment(0x8D19, 'Y < &10 with bit set: clamp to &10', align=Align.INLINE)
d.comment(0x8D1B, 'Return', align=Align.INLINE)
d.comment(0x934A, 'Error code &F1', align=Align.INLINE)
d.comment(0x934C, "Raise 'Bad hex' error", align=Align.INLINE)
d.comment(0xA440, 'V clear: re-enter dispatch_fs_cmd', align=Align.INLINE)
d.comment(0xA442, 'Error code &DC', align=Align.INLINE)
d.comment(0xA444, "Raise 'Syntax' error", align=Align.INLINE)
d.comment(0xA300, 'X=&10: scan 16 slots (15 to 0)', align=Align.INLINE)
d.comment(0xA302, 'Clear V', align=Align.INLINE)
d.comment(0xA309, 'No match: try next', align=Align.INLINE)
d.comment(0xA30B, 'Load slot status byte', align=Align.INLINE)
d.comment(0xA30E, 'Test bit 2 (PS active flag)?', align=Align.INLINE)
d.comment(0xA312, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA319, 'Store Y to fs_urd_handle', align=Align.INLINE)
d.comment(0xA31E, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA322, 'Store allocation result', align=Align.INLINE)
d.comment(0xA32E, 'Try next slot', align=Align.INLINE)
d.comment(0xA341, 'Set V (found match)', align=Align.INLINE)
d.comment(0xA344, 'Store Y to fs_csd_handle', align=Align.INLINE)
d.comment(0xA347, 'V set: found, skip allocation', align=Align.INLINE)
d.comment(0xA34A, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0x9146, 'Store as string pointer low', align=Align.INLINE)
d.comment(0x9149, 'Store as string pointer high', align=Align.INLINE)
d.comment(0x91F9, 'A=&0D (CR) for OSASCI translation; fall through', align=Align.INLINE)
d.comment(0x91FB, "Save caller's flags (V from caller is irrelevant — see &91FC)", align=Align.INLINE)
d.comment(0x91FC, 'Unconditionally sets V=1 (bit 6 of operand &FF)', align=Align.INLINE)
d.comment(0x91FF, 'V=1 always, branch always taken (skips the CLV path)', align=Align.INLINE)
d.comment(0x9201, "Alt entry: save caller's flags BEFORE forcing V=0", align=Align.INLINE)
d.comment(0x9202, 'Force V=0 -> OSWRCH path at &9220 (raw byte)', align=Align.INLINE)
d.comment(0x9203, 'Save X', align=Align.INLINE)
d.comment(0x9204, 'Save Y', align=Align.INLINE)
d.comment(0x9205, 'Save A (the byte to print)', align=Align.INLINE)
d.comment(0x9206, 'Save inner P — V here picks OSASCI vs OSWRCH later', align=Align.INLINE)
d.comment(0x9207, 'OSBYTE 199 (read/write *SPOOL file handle)', align=Align.INLINE)
d.comment(0x9209, 'X=0: handle value to write', align=Align.INLINE)
d.comment(0x920B, 'Y=0: write mode (NEW = (OLD AND 0) EOR X = X = 0)', align=Align.INLINE)
d.comment(0x920D, 'Closes spool; X returns OLD handle', align=Align.INLINE)
d.comment(0x9210, "OLD < ' '? (likely 0 = was already closed)", align=Align.INLINE)
d.comment(0x9212, 'Yes: leave spool closed for the print', align=Align.INLINE)
d.comment(0x9214, "OLD >= '0'?", align=Align.INLINE)
d.comment(0x9216, 'Yes (>= &30): leave spool closed', align=Align.INLINE)
d.comment(0x9218, 'OLD in [&20,&2F] (NFS handle range): re-open spool with X=OLD', align=Align.INLINE)
d.comment(0x921B, 'Clear X for the post-print restore', align=Align.INLINE)
d.comment(0x921D, 'Restore inner P (V=1 OSASCI / V=0 OSWRCH)', align=Align.INLINE)
d.comment(0x921E, 'Pull A (the byte)', align=Align.INLINE)
d.comment(0x921F, 'Push it back so the final epilogue PLA still works', align=Align.INLINE)
d.comment(0x9220, 'V=0 -> OSWRCH (raw); V=1 -> OSASCI (CR translation)', align=Align.INLINE)
d.comment(0x9222, 'OSASCI: writes A, translating CR to CR/LF', align=Align.INLINE)
d.comment(0x9225, 'Skip OSWRCH branch', align=Align.INLINE)
d.comment(0x9227, 'OSWRCH: writes A as a raw byte', align=Align.INLINE)
d.comment(0x922A, 'OSBYTE 199 again to restore spool state', align=Align.INLINE)
d.comment(0x922C, 'Y=&FF (read mode): NEW = OLD EOR X', align=Align.INLINE)
d.comment(0x922E, 'X=0 -> no change; X=OLD -> writes OLD back', align=Align.INLINE)
d.comment(0x9231, 'Pull A (preserved across the call)', align=Align.INLINE)
d.comment(0x9232, 'Pull Y', align=Align.INLINE)
d.comment(0x9233, 'Pull X', align=Align.INLINE)
d.comment(0x9234, "Pull caller's original flags", align=Align.INLINE)
d.comment(0x9235, 'Return', align=Align.INLINE)
d.comment(0x924C, 'Save full byte', align=Align.INLINE)
d.comment(0x924D, 'Shift high nybble to low (LSR x4)', align=Align.INLINE)
d.comment(0x9251, 'Print high nybble as hex digit', align=Align.INLINE)
d.comment(0x9254, 'Restore full byte; fall through for low nybble', align=Align.INLINE)
d.comment(0x9255, 'Mask to low nybble', align=Align.INLINE)
d.comment(0x9257, 'Digit >= &0A?', align=Align.INLINE)
d.comment(0x9259, 'No: skip letter adjustment', align=Align.INLINE)
d.comment(0x925B, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.comment(0x925D, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.comment(0x925F, 'Tail-jump to *SPOOL-bypassing print', align=Align.INLINE)
d.comment(0x928A, 'Pop return-addr low byte (-> string pointer low)', align=Align.INLINE)
d.comment(0x928B, "Save in fs_error_ptr (the loop's pointer low)", align=Align.INLINE)
d.comment(0x928D, 'Pop return-addr high byte', align=Align.INLINE)
d.comment(0x928E, "Save in fs_crflag (the loop's pointer high)", align=Align.INLINE)
d.comment(0x9290, 'Y=0: indirect index for (fs_error_ptr),Y', align=Align.INLINE)
d.comment(0x9292, 'Step pointer low byte to next char', align=Align.INLINE)
d.comment(0x9294, 'No carry: skip high-byte INC', align=Align.INLINE)
d.comment(0x9296, 'Page wrap: bump pointer high', align=Align.INLINE)
d.comment(0x9298, 'Read next character from inline string', align=Align.INLINE)
d.comment(0x929A, 'Bit 7 set: terminator -- this byte is the next opcode', align=Align.INLINE)
d.comment(0x929C, 'Save pointer low (print_char_no_spool may clobber)', align=Align.INLINE)
d.comment(0x929E, 'Push it', align=Align.INLINE)
d.comment(0x929F, 'Save pointer high', align=Align.INLINE)
d.comment(0x92A1, 'Push it', align=Align.INLINE)
d.comment(0x92A2, "Reload the character we're about to print", align=Align.INLINE)
d.comment(0x92A4, 'Print it via the *SPOOL-bypassing OSASCI wrapper', align=Align.INLINE)
d.comment(0x92A7, 'Pop pointer high back', align=Align.INLINE)
d.comment(0x92A8, 'Restore', align=Align.INLINE)
d.comment(0x92AA, 'Pop pointer low back', align=Align.INLINE)
d.comment(0x92AB, 'Restore', align=Align.INLINE)
d.comment(0x92AD, 'Always taken (BRA-style; A is non-zero from print)', align=Align.INLINE)
d.comment(0x92AF, "Resume execution at the terminator byte's address (JMP indirect via fs_error_ptr)", align=Align.INLINE)
d.comment(0x92BD, 'Convert to channel index', align=Align.INLINE)
d.comment(0x92D0, 'Get stack pointer', align=Align.INLINE)
d.comment(0x92D4, 'Convert to channel index', align=Align.INLINE)
d.comment(0x92E2, 'Transfer back to X', align=Align.INLINE)
d.comment(0xA4F1, 'Save current OS text pointer', align=Align.INLINE)
d.comment(0xA4F4, 'Mask access bits', align=Align.INLINE)
d.comment(0xA4F7, 'Clear bit 1 of mask', align=Align.INLINE)
d.comment(0xA4F9, 'Save into fs_lib_flags', align=Align.INLINE)
d.comment(0xA4FC, 'Begin parsing the *RUN argument', align=Align.INLINE)
d.comment(0xA4FF, 'X=1: TX-buffer write index for argument', align=Align.INLINE)
d.comment(0xA501, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0xA515, 'Return from svc_8_osword', align=Align.INLINE)
d.comment(0xA513, 'Loop until all 6 restored', align=Align.INLINE)
d.comment(0xA506, 'Next byte down', align=Align.INLINE)
d.comment(0xA51A, 'Load handler address low byte', align=Align.INLINE)
d.comment(0xA520, 'Loop while X >= 0 (scan all 4 handle slots)', align=Align.INLINE)
d.comment(0xA522, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0xA531, 'Test station active flag', align=Align.INLINE)
d.comment(0xA536, 'C set: error from save_net_tx_cb -- abort *RUN', align=Align.INLINE)
d.comment(0xA538, 'Yes: handle clock read', align=Align.INLINE)
d.comment(0xA53E, 'Return', align=Align.INLINE)
d.comment(0xA541, 'Y=&10: length of TXCB to save', align=Align.INLINE)
d.comment(0xA543, 'Save current TX control block', align=Align.INLINE)
d.comment(0xA54C, 'Store BCD seconds', align=Align.INLINE)
d.comment(0xA552, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA558, 'Load hours from clock workspace', align=Align.INLINE)
d.comment(0xA561, 'Clear hours high position', align=Align.INLINE)
d.comment(0xA563, 'Store zero', align=Align.INLINE)
d.comment(0xA573, 'Restore day+month byte', align=Align.INLINE)
d.comment(0xA57A, 'Store BCD month', align=Align.INLINE)
d.comment(0xA57E, 'Shift high nibble down', align=Align.INLINE)
d.comment(0xA581, '4th shift: isolate high nibble', align=Align.INLINE)
d.comment(0xA58A, 'Copy 7 bytes (Y=6 down to 0)', align=Align.INLINE)
d.comment(0xA58F, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA592, 'Loop for all 7 bytes', align=Align.INLINE)
d.comment(0xA5A1, 'Error code &FE', align=Align.INLINE)
d.comment(0xA5A3, "Raise 'Bad command' error", align=Align.INLINE)
d.comment(0xA5B3, 'Low byte = &6F', align=Align.INLINE)
d.comment(0xA5B5, 'Set osword_flag', align=Align.INLINE)
d.comment(0xA5C3, 'Set workspace pointer high', align=Align.INLINE)
d.comment(0xA5CA, 'Y=OSWORD flag (slot specifier)', align=Align.INLINE)
d.comment(0xA5CF, 'A=3: start searching from slot 3', align=Align.INLINE)
d.comment(0xA5D4, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA5D7, 'Continue shift', align=Align.INLINE)
d.comment(0xA5E5, 'Transfer found slot to A', align=Align.INLINE)
d.comment(0xA5E8, 'Store slot number to PB byte 0', align=Align.INLINE)
d.comment(0xA5ED, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA5EF, 'Y=Y-1: adjust workspace offset', align=Align.INLINE)
d.comment(0xA5F8, 'Compare Y with OSWORD flag', align=Align.INLINE)
d.comment(0xA608, 'Y=1: workspace flag offset', align=Align.INLINE)
d.comment(0xA60A, 'Store pending marker to workspace', align=Align.INLINE)
d.comment(0xA60E, 'Increment retry counter', align=Align.INLINE)
d.comment(0xA613, 'Store result A to PB via Y', align=Align.INLINE)
d.comment(0xA615, 'Rotate Econet flags back (restore state)', align=Align.INLINE)
d.comment(0xA618, 'Return from OSWORD 11 handler', align=Align.INLINE)
d.comment(0xA61B, 'Store to ws_ptr_lo', align=Align.INLINE)
d.comment(0xA61D, 'Y=&7F: last byte of RX buffer', align=Align.INLINE)
d.comment(0xA625, 'X-1: adjust count', align=Align.INLINE)
d.comment(0xA903, 'Zero: result is 0, skip loop', align=Align.INLINE)
d.comment(0xA906, 'Start BCD result at 0', align=Align.INLINE)
d.comment(0xA908, 'Clear carry for BCD add', align=Align.INLINE)
d.comment(0xA909, 'Add 1 in decimal mode', align=Align.INLINE)
d.comment(0xA90B, 'Count down binary value', align=Align.INLINE)
d.comment(0xA90C, 'Loop until zero', align=Align.INLINE)
d.comment(0xA90F, 'Return with BCD result in A', align=Align.INLINE)
d.comment(0xA910, 'ASL tx_complete_flag: old bit 7 -> C', align=Align.INLINE)
d.comment(0xA913, 'A = Y (saved index)', align=Align.INLINE)
d.comment(0xA914, 'C=1 (TX idle): start new transmission', align=Align.INLINE)
d.comment(0xA916, 'C=0 (TX busy): write status byte back to PB', align=Align.INLINE)
d.comment(0xA918, 'Return (TX still in progress)', align=Align.INLINE)
d.comment(0xA91B, 'Copy to ws_ptr_lo', align=Align.INLINE)
d.comment(0xA91D, 'Also set as NMI TX block high', align=Align.INLINE)
d.comment(0xA91F, 'Low byte = &6F', align=Align.INLINE)
d.comment(0xA921, 'Set osword_flag', align=Align.INLINE)
d.comment(0xA923, 'Set NMI TX block low', align=Align.INLINE)
d.comment(0xA925, 'X=&0F: byte count for copy', align=Align.INLINE)
d.comment(0xA927, 'Copy data and begin transmission', align=Align.INLINE)
d.comment(0xA92A, 'Jump to begin Econet transmission', align=Align.INLINE)
d.comment(0xA92D, 'Load NFS workspace page high byte', align=Align.INLINE)
d.comment(0xA92F, 'Set workspace pointer high', align=Align.INLINE)
d.comment(0xA931, 'Set workspace pointer low from Y', align=Align.INLINE)
d.comment(0xA933, 'Rotate Econet flags (save interrupt state)', align=Align.INLINE)
d.comment(0xA936, 'Y=OSWORD flag (slot specifier)', align=Align.INLINE)
d.comment(0xA937, 'Store OSWORD flag', align=Align.INLINE)
d.comment(0xA939, 'Non-zero: use specified slot', align=Align.INLINE)
d.comment(0xA93B, 'A=3: start searching from slot 3', align=Align.INLINE)
d.comment(0xA93D, 'Convert slot to 2-bit workspace index', align=Align.INLINE)
d.comment(0xA940, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA943, 'Continue shift', align=Align.INLINE)
d.comment(0xA945, 'Load workspace byte at offset', align=Align.INLINE)
d.comment(0xA947, 'Zero: slot empty, store result', align=Align.INLINE)
d.comment(0xA949, "Compare with &3F ('?' marker)", align=Align.INLINE)
d.comment(0xA94B, 'Match: slot found for receive', align=Align.INLINE)
d.comment(0xA94E, 'Transfer back to A', align=Align.INLINE)
d.comment(0xA94F, 'Loop back (A != 0)', align=Align.INLINE)
d.comment(0xA952, 'X=0: index for indirect store', align=Align.INLINE)
d.comment(0xA954, 'Store slot number to PB byte 0', align=Align.INLINE)
d.comment(0xA956, 'Convert specified slot to workspace index', align=Align.INLINE)
d.comment(0xA959, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA95C, 'Update workspace pointer low', align=Align.INLINE)
d.comment(0xA95E, 'A=&C0: slot active marker', align=Align.INLINE)
d.comment(0xA962, 'X=&0B: byte count for PB copy', align=Align.INLINE)
d.comment(0xA964, 'Compare Y with OSWORD flag', align=Align.INLINE)
d.comment(0xA966, 'Add workspace byte (check slot state)', align=Align.INLINE)
d.comment(0xA968, 'Zero: slot ready, copy PB and mark', align=Align.INLINE)
d.comment(0xA96A, 'Negative: slot busy, increment and retry', align=Align.INLINE)
d.comment(0xA96D, 'Copy PB byte to workspace slot', align=Align.INLINE)
d.comment(0xA970, 'C set: copy done, finish', align=Align.INLINE)
d.comment(0xA972, "A=&3F: mark slot as pending ('?')", align=Align.INLINE)
d.comment(0xA974, 'Y=1: workspace flag offset', align=Align.INLINE)
d.comment(0xA976, 'Store pending marker to workspace', align=Align.INLINE)
d.comment(0xA97A, 'Increment retry counter', align=Align.INLINE)
d.comment(0xA97C, 'Non-zero: retry copy loop', align=Align.INLINE)
d.comment(0xA97E, 'Decrement Y (adjust offset)', align=Align.INLINE)
d.comment(0xA97F, 'Store result A to PB via Y', align=Align.INLINE)
d.comment(0xA981, 'Rotate Econet flags back (restore state)', align=Align.INLINE)
d.comment(0xA984, 'Return from OSWORD 11 handler', align=Align.INLINE)
d.comment(0xA985, 'Set workspace from RX ptr high', align=Align.INLINE)
d.comment(0xA987, 'Store to ws_ptr_lo', align=Align.INLINE)
d.comment(0xA989, 'Y=&7F: last byte of RX buffer', align=Align.INLINE)
d.comment(0xA98B, 'Load port/count from RX buffer', align=Align.INLINE)
d.comment(0xA98D, 'Y=&80: set workspace pointer', align=Align.INLINE)
d.comment(0xA98E, 'Store as osword_flag', align=Align.INLINE)
d.comment(0xA990, 'X = port/count value', align=Align.INLINE)
d.comment(0xA991, 'X-1: adjust count', align=Align.INLINE)
d.comment(0xA992, 'Y=0 for copy', align=Align.INLINE)
d.comment(0xA994, 'Copy workspace data', align=Align.INLINE)
d.comment(0xA997, 'Update state and return', align=Align.INLINE)
d.comment(0xA99A, 'X = sub-code', align=Align.INLINE)
d.comment(0xA99B, 'Sub-code < &13?', align=Align.INLINE)
d.comment(0xA99D, 'Out of range: return', align=Align.INLINE)
d.comment(0xAAD3, 'Y=1: first handle in PB', align=Align.INLINE)
d.comment(0xAAD5, 'Load handle value from PB[Y]', align=Align.INLINE)
d.comment(0xAAD7, 'Must be >= &20', align=Align.INLINE)
d.comment(0xAAD9, 'Below range: invalid', align=Align.INLINE)
d.comment(0xAADB, 'Must be < &30', align=Align.INLINE)
d.comment(0xAADD, 'Above range: invalid', align=Align.INLINE)
d.comment(0xAADF, 'X = handle value', align=Align.INLINE)
d.comment(0xAAE0, 'Load fcb_attr_or_count_mid[handle]', align=Align.INLINE)
d.comment(0xAAE3, 'Non-zero: FCB exists', align=Align.INLINE)
d.comment(0xAAE8, 'Clear PB[0] status', align=Align.INLINE)
d.comment(0xAAEA, 'Skip to next handle', align=Align.INLINE)
d.comment(0xAAEC, 'Load fcb_flags[handle] flags', align=Align.INLINE)
d.comment(0xAAEF, 'Test bit 1 (allocated?)', align=Align.INLINE)
d.comment(0xAAF1, 'Not allocated: invalid', align=Align.INLINE)
d.comment(0xAAF3, 'X = handle value', align=Align.INLINE)
d.comment(0xAAF4, 'Store handle to fs_lib_flags+Y', align=Align.INLINE)
d.comment(0xAAF7, 'Load station from fcb_attr_or_count_mid', align=Align.INLINE)
d.comment(0xAAFA, 'Store station to fs_server_net+Y', align=Align.INLINE)
d.comment(0xAAFD, 'Is this handle 1 (Y=1)?', align=Align.INLINE)
d.comment(0xAAFF, 'No: check handle 2', align=Align.INLINE)
d.comment(0xAB03, 'Bit mask &04 for handle 1', align=Align.INLINE)
d.comment(0xAB05, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xAB09, 'Back to Y', align=Align.INLINE)
d.comment(0xAB0A, 'Reload fcb_flags flags', align=Align.INLINE)
d.comment(0xAB0D, 'Set bits 2+5 (active+updated)', align=Align.INLINE)
d.comment(0xAB0F, 'Store updated flags', align=Align.INLINE)
d.comment(0xAB12, 'Next handle slot', align=Align.INLINE)
d.comment(0xAB15, 'No: process next handle', align=Align.INLINE)
d.comment(0xAB17, 'Y=3 for return', align=Align.INLINE)
d.comment(0xAB19, 'Is this handle 2 (Y=2)?', align=Align.INLINE)
d.comment(0xAB1B, 'No: must be handle 3', align=Align.INLINE)
d.comment(0xAB1E, 'Push Y', align=Align.INLINE)
d.comment(0xAB21, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xAB24, 'Restore Y', align=Align.INLINE)
d.comment(0xAB25, 'Back to Y', align=Align.INLINE)
d.comment(0xAB26, 'Reload fcb_flags flags', align=Align.INLINE)
d.comment(0xAB2B, 'Store updated flags', align=Align.INLINE)
d.comment(0xAB2E, 'Next handle slot', align=Align.INLINE)
d.comment(0xAB30, 'Handle 3: save Y', align=Align.INLINE)
d.comment(0xAB32, 'Bit mask &10 for handle 3', align=Align.INLINE)
d.comment(0xAB34, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xAB38, 'Back to Y', align=Align.INLINE)
d.comment(0xAB39, 'Reload fcb_flags flags', align=Align.INLINE)
d.comment(0xAB3C, 'Set bits 4+5 (active+updated)', align=Align.INLINE)
d.comment(0xAB3E, 'Store updated flags', align=Align.INLINE)
d.comment(0xAB41, 'Next handle slot', align=Align.INLINE)
d.comment(0xAB44, 'Push X', align=Align.INLINE)
d.comment(0xAB47, 'Load FCB flags', align=Align.INLINE)
d.comment(0xAB4A, 'Shift bits 6-7 into bits 7-0', align=Align.INLINE)
d.comment(0xAB4C, 'Bit 6 clear: skip entry', align=Align.INLINE)
d.comment(0xAB4E, 'Restore Y (bit mask)', align=Align.INLINE)
d.comment(0xAB4F, 'Test mask bits against flags', align=Align.INLINE)
d.comment(0xAB52, 'Zero: no matching bits', align=Align.INLINE)
d.comment(0xAB54, 'Matching: restore Y', align=Align.INLINE)
d.comment(0xAB55, 'Set bit 5 (updated)', align=Align.INLINE)
d.comment(0xAB57, 'Skip clear path', align=Align.INLINE)
d.comment(0xAB59, 'No match: restore Y', align=Align.INLINE)
d.comment(0xAB5A, 'Invert all bits', align=Align.INLINE)
d.comment(0xAB5C, 'Clear tested bits in flags', align=Align.INLINE)
d.comment(0xAB5F, 'Store updated flags', align=Align.INLINE)
d.comment(0xAB63, 'Loop for all 16 entries', align=Align.INLINE)
d.comment(0xAB65, 'Restore original X', align=Align.INLINE)
d.comment(0xAB66, 'Back to X', align=Align.INLINE)
d.comment(0xAB6A, 'Load (net_rx_ptr)+1', align=Align.INLINE)
d.comment(0xAB6C, 'Y=0', align=Align.INLINE)
d.comment(0xAB6E, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xAB71, 'Y=&7F: port byte offset', align=Align.INLINE)
d.comment(0xAB73, 'Load (net_rx_ptr)+&7F', align=Align.INLINE)
d.comment(0xAB75, 'Y=1', align=Align.INLINE)
d.comment(0xAB77, 'Store to PB[1]', align=Align.INLINE)
d.comment(0xAB7A, 'A=&80', align=Align.INLINE)
d.comment(0xAB7C, 'Store &80 to PB[2]', align=Align.INLINE)
d.comment(0xAB7E, 'Return', align=Align.INLINE)
d.comment(0xAB7F, 'Load error flag', align=Align.INLINE)
d.comment(0xAB82, 'Y=1: parameter block offset 1', align=Align.INLINE)
d.comment(0xAB83, 'Store result to PB[1]', align=Align.INLINE)
d.comment(0xAB85, 'Return', align=Align.INLINE)
d.comment(0xAB86, 'Load context byte', align=Align.INLINE)
d.comment(0xAB89, 'Bit 7 clear: store context to PB', align=Align.INLINE)
d.comment(0xAB8B, 'Total buffers = &6F', align=Align.INLINE)
d.comment(0xAB8E, 'Free = &6F - spool_buf_idx', align=Align.INLINE)
d.comment(0xAB91, 'Non-negative: store free count to PB', align=Align.INLINE)
d.comment(0xAB94, 'Return', align=Align.INLINE)
d.comment(0xAB97, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xAB99, 'Done 3 bytes?', align=Align.INLINE)
d.comment(0xAB9B, 'No: loop', align=Align.INLINE)
d.comment(0xAB9E, 'Next byte offset', align=Align.INLINE)
d.comment(0xAB9F, 'Load PB[Y]', align=Align.INLINE)
d.comment(0xABA1, 'Store to tx_retry_count[Y]', align=Align.INLINE)
d.comment(0xABA4, 'Done 3 bytes?', align=Align.INLINE)
d.comment(0xABA6, 'No: loop', align=Align.INLINE)
d.comment(0xABA8, 'Return', align=Align.INLINE)
d.comment(0xABA9, 'Poll for bridge', align=Align.INLINE)
d.comment(0xABAC, 'Y=0', align=Align.INLINE)
d.comment(0xABAE, 'Load bridge status', align=Align.INLINE)
d.comment(0xABB1, 'Is it &FF (no bridge)?', align=Align.INLINE)
d.comment(0xABB3, 'No: bridge found', align=Align.INLINE)
d.comment(0xABB6, 'PB[0] = 0 (no bridge)', align=Align.INLINE)
d.comment(0xABBB, 'Y=1', align=Align.INLINE)
d.comment(0xABBC, 'PB[1] = bridge status', align=Align.INLINE)
d.comment(0xABBF, 'Y=3', align=Align.INLINE)
d.comment(0xABC0, 'Load PB[3] (caller value)', align=Align.INLINE)
d.comment(0xABC2, 'Zero: use default station', align=Align.INLINE)
d.comment(0xABC4, 'Compare with bridge status', align=Align.INLINE)
d.comment(0xABC9, 'Same: confirm station', align=Align.INLINE)
d.comment(0xABCB, 'Load default from fs_server_net', align=Align.INLINE)
d.comment(0xABCE, 'Store to PB[3]', align=Align.INLINE)
d.comment(0xABD1, 'TX 0: ctrl = &82 (immediate mode)', align=Align.INLINE)
d.comment(0xABD2, 'TX 1: port = &9C (bridge discovery)', align=Align.INLINE)
d.comment(0xABD3, 'TX 2: dest station = &FF (broadcast)', align=Align.INLINE)
d.comment(0xABD4, 'TX 3: dest network = &FF (all nets)', align=Align.INLINE)
d.comment(0xABD5, 'TX 4-9: immediate data payload', align=Align.INLINE)
d.comment(0xABDC, 'TX 11: &00 (terminator)', align=Align.INLINE)
d.comment(0xABDD, 'RX 0: ctrl = &7F (receive)', align=Align.INLINE)
d.comment(0xABDE, 'RX 1: port = &9C (bridge discovery)', align=Align.INLINE)
d.comment(0xABDF, 'RX 2: station = &00 (any)', align=Align.INLINE)
d.comment(0xABE0, 'RX 3: network = &00 (any)', align=Align.INLINE)
d.comment(0xABE3, 'RX 6: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xABE4, 'RX 7: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xABE6, 'RX 9: buf end hi (&0D) -> &0D74', align=Align.INLINE)
d.comment(0xABE9, 'Check bridge status', align=Align.INLINE)
d.comment(0xABEC, 'Is it &FF (uninitialised)?', align=Align.INLINE)
d.comment(0xABEE, 'No: bridge already active, return', align=Align.INLINE)
d.comment(0xABF0, 'Save Y', align=Align.INLINE)
d.comment(0xABF1, 'Preserve Y on stack', align=Align.INLINE)
d.comment(0xABF2, 'Y=&18: workspace offset for init', align=Align.INLINE)
d.comment(0xABF4, 'X=&0B: 12 bytes to copy', align=Align.INLINE)
d.comment(0xABF6, 'Rotate econet_flags right (save flag)', align=Align.INLINE)
d.comment(0xABF9, 'Load init data byte', align=Align.INLINE)
d.comment(0xABFC, 'Store to workspace', align=Align.INLINE)
d.comment(0xABFE, 'Load TXCB template byte', align=Align.INLINE)
d.comment(0xAC01, 'Store to TX control block', align=Align.INLINE)
d.comment(0xAC03, 'Next workspace byte', align=Align.INLINE)
d.comment(0xAC04, 'Next template byte', align=Align.INLINE)
d.comment(0xAC05, 'Loop for all 12 bytes', align=Align.INLINE)
d.comment(0xAC07, 'Store X (-1) as bridge counter', align=Align.INLINE)
d.comment(0xAC0A, 'Restore econet_flags flag', align=Align.INLINE)
d.comment(0xAC0D, 'Shift ws_0d60 left (check status)', align=Align.INLINE)
d.comment(0xAC10, 'C=0: status clear, retry', align=Align.INLINE)
d.comment(0xAC12, 'Control byte &82 for TX', align=Align.INLINE)
d.comment(0xAC14, 'Set in TX control block', align=Align.INLINE)
d.comment(0xAC16, 'Data block at &00C0', align=Align.INLINE)
d.comment(0xAC18, 'Set NMI TX block low', align=Align.INLINE)
d.comment(0xAC1A, 'High byte = 0 (page 0)', align=Align.INLINE)
d.comment(0xAC1C, 'Set NMI TX block high', align=Align.INLINE)
d.comment(0xAC1E, 'Begin Econet transmission', align=Align.INLINE)
d.comment(0xAC21, 'Test TX control block bit 7', align=Align.INLINE)
d.comment(0xAC23, 'Negative: TX still in progress', align=Align.INLINE)
d.comment(0xAC50, 'Y=&23: workspace offset for params', align=Align.INLINE)
d.comment(0xAC52, 'Set owner access mask', align=Align.INLINE)
d.comment(0xAC55, 'Load TXCB init byte', align=Align.INLINE)
d.comment(0xAC58, 'Non-zero: use template value', align=Align.INLINE)
d.comment(0xAC5A, 'Zero: use workspace default value', align=Align.INLINE)
d.comment(0xAC5D, 'Store to workspace', align=Align.INLINE)
d.comment(0xAC5F, 'Next byte down', align=Align.INLINE)
d.comment(0xAC60, 'Until Y reaches &17', align=Align.INLINE)
d.comment(0xAC62, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xAC65, 'Set net_tx_ptr low byte', align=Align.INLINE)
d.comment(0xAC67, 'Y=&1C: workspace offset for PB pointer', align=Align.INLINE)
d.comment(0xAC69, 'Load PB page number', align=Align.INLINE)
d.comment(0xAC6B, 'PB starts at next page boundary (+1)', align=Align.INLINE)
d.comment(0xAC6D, 'Store PB start pointer at ws[&1C]', align=Align.INLINE)
d.comment(0xAC70, 'Y=1: PB byte 1 (transfer length)', align=Align.INLINE)
d.comment(0xAC72, 'Load transfer length from PB', align=Align.INLINE)
d.comment(0xAC76, 'Add PB base for buffer end address', align=Align.INLINE)
d.comment(0xAC78, 'Store PB pointer to workspace', align=Align.INLINE)
d.comment(0xAC7B, 'Y=2: parameter offset', align=Align.INLINE)
d.comment(0xAC7D, 'Control byte &90', align=Align.INLINE)
d.comment(0xAC7F, 'Set escapable flag', align=Align.INLINE)
d.comment(0xAC81, 'Store control byte to PB', align=Align.INLINE)
d.comment(0xAC85, 'Load workspace data', align=Align.INLINE)
d.comment(0xAC88, 'Store to parameter block', align=Align.INLINE)
d.comment(0xAC8A, 'Next byte', align=Align.INLINE)
d.comment(0xAC8B, 'Until Y reaches 7', align=Align.INLINE)
d.comment(0xAC8D, 'Loop for 3 bytes (Y=4,5,6)', align=Align.INLINE)
d.comment(0xAC91, 'Store to net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xAC93, 'Enable interrupts', align=Align.INLINE)
d.comment(0xAC96, 'Y=&20: workspace offset', align=Align.INLINE)
d.comment(0xAC98, 'Set to &FF (pending)', align=Align.INLINE)
d.comment(0xAC9A, 'Mark send pending in workspace', align=Align.INLINE)
d.comment(0xAC9D, 'Also mark offset &21', align=Align.INLINE)
d.comment(0xAC9F, 'Y=&19: control offset', align=Align.INLINE)
d.comment(0xACA1, 'Control byte &90', align=Align.INLINE)
d.comment(0xACA3, 'Store to workspace', align=Align.INLINE)
d.comment(0xACA5, 'Y=&18: RX control offset', align=Align.INLINE)
d.comment(0xACA6, 'Control byte &7F', align=Align.INLINE)
d.comment(0xACA8, 'Store RX control', align=Align.INLINE)
d.comment(0xACAA, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xACAD, 'Store address low byte at ws[Y]', align=Align.INLINE)
d.comment(0xACAF, 'Advance to high byte offset', align=Align.INLINE)
d.comment(0xACB0, 'Load high byte base (table_idx)', align=Align.INLINE)
d.comment(0xACB2, 'Add carry for page crossing', align=Align.INLINE)
d.comment(0xACB4, 'Store address high byte at ws[Y+1]', align=Align.INLINE)
d.comment(0xACB7, 'Save processor flags', align=Align.INLINE)
d.comment(0xACBA, 'Load station number from PB', align=Align.INLINE)
d.comment(0xACBC, 'X = station number', align=Align.INLINE)
d.comment(0xACBE, 'Load network number from PB', align=Align.INLINE)
d.comment(0xACC0, 'Y=3: workspace start offset', align=Align.INLINE)
d.comment(0xACC1, 'Store Y as ws_ptr_lo', align=Align.INLINE)
d.comment(0xACC3, 'Y=&72: workspace offset for dest', align=Align.INLINE)
d.comment(0xACC5, 'Store network to workspace', align=Align.INLINE)
d.comment(0xACC7, 'Y=&71', align=Align.INLINE)
d.comment(0xACC8, 'A = station (from X)', align=Align.INLINE)
d.comment(0xACC9, 'Store station to workspace', align=Align.INLINE)
d.comment(0xACCB, 'Restore flags from PHP', align=Align.INLINE)
d.comment(0xACCC, 'Non-zero sub-code: handle burst', align=Align.INLINE)
d.comment(0xACCE, 'Load current offset', align=Align.INLINE)
d.comment(0xACD0, 'Advance offset for next byte', align=Align.INLINE)
d.comment(0xACD2, 'Load next char from PB', align=Align.INLINE)
d.comment(0xACD4, 'Zero: end of data, return', align=Align.INLINE)
d.comment(0xACD8, 'Store char to RX buffer', align=Align.INLINE)
d.comment(0xACDA, 'Save char for later test', align=Align.INLINE)
d.comment(0xACDB, 'Init workspace copy for wide xfer', align=Align.INLINE)
d.comment(0xACDF, 'Set bit 7: Tube needs release', align=Align.INLINE)
d.comment(0xACE1, 'Enable IRQ and send packet', align=Align.INLINE)
d.comment(0xACE4, 'Delay countdown', align=Align.INLINE)
d.comment(0xACE7, 'Restore char', align=Align.INLINE)
d.comment(0xACE8, 'Test if char was CR (&0D)', align=Align.INLINE)
d.comment(0xACEC, 'CR sent: return', align=Align.INLINE)
d.comment(0xACED, 'Init workspace for wide copy', align=Align.INLINE)
d.comment(0xACF2, 'Load buffer size', align=Align.INLINE)
d.comment(0xACF6, 'Store adjusted size', align=Align.INLINE)
d.comment(0xACF9, 'Send packet and return', align=Align.INLINE)
d.comment(0xACFC, 'Save processor flags', align=Align.INLINE)
d.comment(0xACFD, 'Save A', align=Align.INLINE)
d.comment(0xACFE, 'Save X', align=Align.INLINE)
d.comment(0xACFF, 'Push X', align=Align.INLINE)
d.comment(0xAD00, 'Save Y', align=Align.INLINE)
d.comment(0xAD01, 'Push Y', align=Align.INLINE)
d.comment(0xAD02, 'Get stack pointer', align=Align.INLINE)
d.comment(0xAD03, 'Read OSWORD number from stack', align=Align.INLINE)
d.comment(0xAD06, 'OSWORD >= 9?', align=Align.INLINE)
d.comment(0xAD08, 'Yes: out of range, restore + return', align=Align.INLINE)
d.comment(0xAD0A, 'X = OSWORD number', align=Align.INLINE)
d.comment(0xAD0B, 'Push handler address for dispatch', align=Align.INLINE)
d.comment(0xAD0E, 'Restore Y', align=Align.INLINE)
d.comment(0xAD0F, 'Back to Y', align=Align.INLINE)
d.comment(0xAD10, 'Restore X', align=Align.INLINE)
d.comment(0xAD11, 'Back to X', align=Align.INLINE)
d.comment(0xAD12, 'Restore A', align=Align.INLINE)
d.comment(0xAD1D, 'Reload OSWORD number for handler', align=Align.INLINE)
d.comment(0xAD2F, 'hi OSWORD 6: no-op (RTS)', align=Align.INLINE)
d.comment(0xAD39, 'A = original Y', align=Align.INLINE)
d.comment(0xAD40, 'Y=&D9: workspace abort offset', align=Align.INLINE)
d.comment(0xAD42, 'Store abort code to workspace', align=Align.INLINE)
d.comment(0xAD4A, 'Save current TX ptr low', align=Align.INLINE)
d.comment(0xAD50, 'Set TX ptr to workspace offset', align=Align.INLINE)
d.comment(0xAD54, 'Set TX ptr high', align=Align.INLINE)
d.comment(0xAD56, 'Send the abort packet', align=Align.INLINE)
d.comment(0xAD59, 'Set status to &3F (complete)', align=Align.INLINE)
d.comment(0xAD5B, 'Store at TX ptr offset 0', align=Align.INLINE)
d.comment(0xAD64, 'Load PB pointer high', align=Align.INLINE)
d.comment(0xAD66, 'Compare with &81 (special case)', align=Align.INLINE)
d.comment(0xAD68, 'Match: skip to processing', align=Align.INLINE)
d.comment(0xAD6C, 'X=&0A: 11 codes to check', align=Align.INLINE)
d.comment(0xAD74, 'Y=-1: flag second range', align=Align.INLINE)
d.comment(0xAD75, 'X=&11: 18 codes to check', align=Align.INLINE)
d.comment(0xAD7C, 'Not found: increment Y', align=Align.INLINE)
d.comment(0xAD7D, 'X=2: default state', align=Align.INLINE)
d.comment(0xAD7F, 'A = Y (search result)', align=Align.INLINE)
d.comment(0xAD82, 'Save result flags', align=Align.INLINE)
d.comment(0xAD86, 'Y=&DC: workspace offset for save', align=Align.INLINE)
d.comment(0xAD90, 'Loop for 3 bytes', align=Align.INLINE)
d.comment(0xAD92, 'A = state (2 or 3)', align=Align.INLINE)
d.comment(0xADA1, 'Positive: keep waiting', align=Align.INLINE)
d.comment(0xADA3, 'Get stack pointer', align=Align.INLINE)
d.comment(0xADA4, 'Y=&DD: workspace result offset', align=Align.INLINE)
d.comment(0xADA8, 'Set bit 6 and bit 2', align=Align.INLINE)
d.comment(0xADAA, 'Always branch (NZ from ORA)', align=Align.INLINE)
d.comment(0xADC1, 'Range 1+2: OSWORD &04', align=Align.INLINE)
d.comment(0xADC2, 'Range 1+2: OSWORD &09', align=Align.INLINE)
d.comment(0xADC4, 'Range 1+2: OSWORD &14', align=Align.INLINE)
d.comment(0xADC5, 'Range 1+2: OSWORD &15', align=Align.INLINE)
d.comment(0xADC7, 'Range 1+2: OSWORD &9B', align=Align.INLINE)
d.comment(0xADC8, 'Range 1+2: OSWORD &E1', align=Align.INLINE)
d.comment(0xADCA, 'Range 1+2: OSWORD &E3', align=Align.INLINE)
d.comment(0xADCB, 'Range 1+2: OSWORD &E4', align=Align.INLINE)
d.comment(0xADCD, 'Range 2 only: OSWORD &0C', align=Align.INLINE)
d.comment(0xADCE, 'Range 2 only: OSWORD &0F', align=Align.INLINE)
d.comment(0xADCF, 'Range 2 only: OSWORD &79', align=Align.INLINE)
d.comment(0xADD2, 'Range 2 only: OSWORD &87', align=Align.INLINE)
d.comment(0xADD3, 'Y=&0E: copy 15 bytes (0-14)', align=Align.INLINE)
d.comment(0xADD7, 'Yes: handle', align=Align.INLINE)
d.comment(0xADDB, 'No: return', align=Align.INLINE)
d.comment(0xADDD, 'Workspace low = &DB', align=Align.INLINE)
d.comment(0xADDF, 'Set nfs_workspace low byte', align=Align.INLINE)
d.comment(0xADE3, 'Store to workspace[Y]', align=Align.INLINE)
d.comment(0xADE8, 'Y=0', align=Align.INLINE)
d.comment(0xADE9, 'Workspace low = &DA', align=Align.INLINE)
d.comment(0xADEB, 'Load OSWORD number', align=Align.INLINE)
d.comment(0xADED, 'Store at workspace+0 (= &DA)', align=Align.INLINE)
d.comment(0xADEF, 'Workspace low = 0 (restore)', align=Align.INLINE)
d.comment(0xADF3, 'Control value &E9', align=Align.INLINE)
d.comment(0xADFC, 'Restore nfs_workspace low', align=Align.INLINE)
d.comment(0xAE00, 'Y=&7C: workspace destination offset', align=Align.INLINE)
d.comment(0xAE02, 'Test bit 6 (V flag check)', align=Align.INLINE)
d.comment(0xAE05, 'V=1: skip to wide mode copy', align=Align.INLINE)
d.comment(0xAE07, 'Y=&17: narrow mode dest offset', align=Align.INLINE)
d.comment(0xAE09, 'X=&1A: 27 bytes to copy', align=Align.INLINE)
d.comment(0xAE0B, 'Clear V flag for narrow mode', align=Align.INLINE)
d.comment(0xAE17, 'Is it &FC? (page ptr marker)', align=Align.INLINE)
d.comment(0xAE1B, '&FC: load RX buffer page', align=Align.INLINE)
d.comment(0xAE1F, 'V=0: use nfs_workspace_hi', align=Align.INLINE)
d.comment(0xAE21, 'Store as TX ptr high', align=Align.INLINE)
d.comment(0xAE33, 'Wide &6F: ctrl=&85', align=Align.INLINE)
d.comment(0xAE35, 'Wide &71: skip (dest station)', align=Align.INLINE)
d.comment(0xAE38, 'Wide &74: buf start hi=page ptr', align=Align.INLINE)
d.comment(0xAE39, 'Wide &75: buf start ext lo', align=Align.INLINE)
d.comment(0xAE3A, 'Wide &76: buf start ext hi', align=Align.INLINE)
d.comment(0xAE3B, 'Wide &77: buf end lo=&7E', align=Align.INLINE)
d.comment(0xAE3E, 'Wide &7A: buf end ext hi', align=Align.INLINE)
d.comment(0xAE3F, 'Wide &7B: zero', align=Align.INLINE)
d.comment(0xAE40, 'Wide &7C: zero', align=Align.INLINE)
d.comment(0xAE41, 'Narrow stop (&FE terminator)', align=Align.INLINE)
d.comment(0xAE44, 'Narrow &0E: skip (dest station)', align=Align.INLINE)
d.comment(0xAE47, 'Narrow &11: buf start hi=page ptr', align=Align.INLINE)
d.comment(0xAE48, 'Narrow &12: buf start ext lo', align=Align.INLINE)
d.comment(0xAE49, 'Narrow &13: buf start ext hi', align=Align.INLINE)
d.comment(0xAE4A, 'Narrow &14: buf end lo=&DE', align=Align.INLINE)
d.comment(0xAE4D, 'Narrow &17: buf end ext hi', align=Align.INLINE)
d.comment(0xAE4E, 'Spool stop (&FE terminator)', align=Align.INLINE)
d.comment(0xAE51, 'Spool &03: skip (dest network)', align=Align.INLINE)
d.comment(0xAE54, 'Spool &06: buf start ext lo', align=Align.INLINE)
d.comment(0xAE55, 'Spool &07: buf start ext hi', align=Align.INLINE)
d.comment(0xAE56, 'Spool &08: skip (buf end lo)', align=Align.INLINE)
d.comment(0xAE59, 'Spool &0B: buf end ext hi', align=Align.INLINE)
d.comment(0xAE5B, 'Match osword_pb_ptr?', align=Align.INLINE)
d.comment(0xAE5D, 'No: return (not our PB)', align=Align.INLINE)
d.comment(0xAE5F, 'Load spool state byte', align=Align.INLINE)
d.comment(0xAE62, 'C=1: already active, return', align=Align.INLINE)
d.comment(0xAE64, 'Buffer start offset = &21', align=Align.INLINE)
d.comment(0xAE66, 'Store as buffer pointer', align=Align.INLINE)
d.comment(0xAE69, 'Control state &41', align=Align.INLINE)
d.comment(0xAE6B, 'Store as spool control state', align=Align.INLINE)
d.comment(0xAE6E, 'Return', align=Align.INLINE)
d.comment(0xAE6F, 'Check Y == 4', align=Align.INLINE)
d.comment(0xAE73, 'A = X (control byte)', align=Align.INLINE)
d.comment(0xAE75, 'Non-zero: handle spool ctrl byte', align=Align.INLINE)
d.comment(0xAE78, 'OR with stack value', align=Align.INLINE)
d.comment(0xAE7B, 'Store back to stack', align=Align.INLINE)
d.comment(0xAE7E, 'OSBYTE &91: read buffer', align=Align.INLINE)
d.comment(0xAE80, 'X=3: printer buffer', align=Align.INLINE)
d.comment(0xAE82, 'Read character from buffer', align=Align.INLINE)
d.comment(0xAE87, 'A = extracted character', align=Align.INLINE)
d.comment(0xAE88, 'Add byte to RX buffer', align=Align.INLINE)
d.comment(0xAE8B, 'Buffer past &6E limit?', align=Align.INLINE)
d.comment(0xAE8D, 'No: read more from buffer', align=Align.INLINE)
d.comment(0xAE92, 'More room: continue reading', align=Align.INLINE)
d.comment(0xAE9D, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAEA0, 'Load spool control state', align=Align.INLINE)
d.comment(0xAEA4, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAEA5, 'Restore state', align=Align.INLINE)
d.comment(0xAEA6, 'C=1: already started, reset', align=Align.INLINE)
d.comment(0xAEA8, 'Set bits 0-1 (active + pending)', align=Align.INLINE)
d.comment(0xAEAA, 'Store updated state', align=Align.INLINE)
d.comment(0xAED3, 'Save state', align=Align.INLINE)
d.comment(0xAED5, 'Restore state', align=Align.INLINE)
d.comment(0xAEE0, 'Push for later restore', align=Align.INLINE)
d.comment(0xAEEC, 'X=0', align=Align.INLINE)
d.comment(0xAEFF, 'Push for restore', align=Align.INLINE)
d.comment(0xAF1A, 'Save station', align=Align.INLINE)
d.comment(0xAF23, 'Restore station', align=Align.INLINE)
d.comment(0xAFAF, 'X=&FF: start search from -1', align=Align.INLINE)
d.comment(0xAFB1, 'Y = disconnect code', align=Align.INLINE)
d.comment(0xAFB4, 'Compare with station table entry', align=Align.INLINE)
d.comment(0xAFC2, 'Check station and network match', align=Align.INLINE)
d.comment(0xAFD3, 'Send the packet', align=Align.INLINE)
d.comment(0xAFE3, 'Check original disconnect code', align=Align.INLINE)
d.comment(0xAFE7, 'Non-zero: use &90 control', align=Align.INLINE)
d.comment(0xAFF0, 'Save status on stack', align=Align.INLINE)
d.comment(0xAFF8, 'Restore status', align=Align.INLINE)
d.comment(0xAFFA, 'Compare with current TX buffer', align=Align.INLINE)
d.comment(0xAFFC, 'Rotate result bit 0 to carry', align=Align.INLINE)
d.comment(0xB002, 'ctrl=&80 (standard TX)', align=Align.INLINE)
d.comment(0xB003, 'port=&9F', align=Align.INLINE)
d.comment(0xB004, 'dest station=&00 (filled later)', align=Align.INLINE)
d.comment(0xB005, 'dest network=&00 (filled later)', align=Align.INLINE)
d.comment(0xB006, 'buf start lo (&9F)', align=Align.INLINE)
d.comment(0xB007, 'buf start hi (&8E); start = &8E9F', align=Align.INLINE)
d.comment(0xB008, 'buf start ext lo=&FF', align=Align.INLINE)
d.comment(0xB009, 'buf start ext hi=&FF', align=Align.INLINE)
d.comment(0xB00A, 'buf end lo (&A7)', align=Align.INLINE)
d.comment(0xB00B, 'buf end hi (&8E); end = &8EA7', align=Align.INLINE)
d.comment(0xB00C, 'buf end ext lo=&FF', align=Align.INLINE)
d.comment(0xB00D, 'buf end ext hi=&FF', align=Align.INLINE)
d.comment(0xB00E, 'ctrl=&7F (RX listen)', align=Align.INLINE)
d.comment(0xB00F, 'port=&9E', align=Align.INLINE)
d.comment(0xB010, 'skip: preserve dest station', align=Align.INLINE)
d.comment(0xB013, 'buf start hi=page ptr (&FC)', align=Align.INLINE)
d.comment(0xB014, 'buf start ext lo=&FF', align=Align.INLINE)
d.comment(0xB015, 'buf start ext hi=&FF', align=Align.INLINE)
d.comment(0xB018, 'buf end ext lo=&FF', align=Align.INLINE)
d.comment(0xB019, 'buf end ext hi=&FF', align=Align.INLINE)
d.comment(0xB030, 'A=0 for first palette entry', align=Align.INLINE)
d.comment(0xB039, 'Read palette entry', align=Align.INLINE)
d.comment(0xB041, 'Y=1: physical colour offset', align=Align.INLINE)
d.comment(0xB044, 'Save for next iteration', align=Align.INLINE)
d.comment(0xB04B, 'Y=0', align=Align.INLINE)
d.comment(0xB298, 'Data: option string offset table', align=Align.INLINE)
d.comment(0xB29F, 'X=0: start of buffer', align=Align.INLINE)
d.comment(0xB2A1, 'Y=0: start of argument', align=Align.INLINE)
d.comment(0xB2A4, 'Get character from command line', align=Align.INLINE)
d.comment(0xB2A9, 'Carry clear: skip validation', align=Align.INLINE)
d.comment(0xB2AF, "Yes: '&' not allowed in filenames", align=Align.INLINE)
d.comment(0xB2B1, "'&' in filename: bad filename", align=Align.INLINE)
d.comment(0xB2B5, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xB2B9, 'Load character from end of buffer', align=Align.INLINE)
d.comment(0xB2BC, 'Test for space (&20)', align=Align.INLINE)
d.comment(0xB2C6, 'ALWAYS: trim next character back', align=Align.INLINE)
d.comment(0xB2C8, 'A=0: success return code', align=Align.INLINE)
d.comment(0xB2D4, 'Store masked flags', align=Align.INLINE)
d.comment(0xB3AC, 'A=1: check printer ready', align=Align.INLINE)
d.comment(0xB3AE, 'Test printer server workspace flag', align=Align.INLINE)
d.comment(0xB3B1, 'Non-zero: printer available', align=Align.INLINE)
d.comment(0xB3B3, 'Printer not available: error', align=Align.INLINE)
d.comment(0xB3B6, 'Initialise spool drive', align=Align.INLINE)
d.comment(0xB3B9, 'Save pointer to spool buffer', align=Align.INLINE)
d.comment(0xB3BE, 'End of command line?', align=Align.INLINE)
d.comment(0xB3C0, 'Yes: no argument given', align=Align.INLINE)
d.comment(0xB3C2, 'Clear V (= explicit PS name given)', align=Align.INLINE)
d.comment(0xB3C3, 'Is first char a decimal digit?', align=Align.INLINE)
d.comment(0xB3C9, 'Save Y', align=Align.INLINE)
d.comment(0xB3CA, 'Load PS server address', align=Align.INLINE)
d.comment(0xB3CD, 'Restore Y', align=Align.INLINE)
d.comment(0xB3CE, 'Back to Y register', align=Align.INLINE)
d.comment(0xB3CF, 'Parse FS/PS arguments', align=Align.INLINE)
d.comment(0xB3D2, 'Jump to store station address', align=Align.INLINE)
d.comment(0xB3D5, 'Start at offset &18', align=Align.INLINE)
d.comment(0xB3D7, 'X=&F8: offset into template', align=Align.INLINE)
d.comment(0xB3D9, 'Get template byte', align=Align.INLINE)
d.comment(0xB3DF, 'Next source offset', align=Align.INLINE)
d.comment(0xB3E3, 'Set V (= no explicit PS name)', align=Align.INLINE)
d.comment(0xB3E8, 'V set: skip PS name parsing', align=Align.INLINE)
d.comment(0xB3EA, 'Max 6 characters for PS name', align=Align.INLINE)
d.comment(0xB3EC, 'Buffer offset &1C for PS name', align=Align.INLINE)
d.comment(0xB3EE, 'Space character', align=Align.INLINE)
d.comment(0xB3F0, 'Fill buffer with space', align=Align.INLINE)
d.comment(0xB3F3, 'Count down', align=Align.INLINE)
d.comment(0xB3F6, 'Save text pointer', align=Align.INLINE)
d.comment(0xB3FB, 'Initialise string reading', align=Align.INLINE)
d.comment(0xB3FE, 'Empty string: skip to send', align=Align.INLINE)
d.comment(0xB402, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB404, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB406, 'Save buffer position', align=Align.INLINE)
d.comment(0xB408, 'Restore string pointer', align=Align.INLINE)
d.comment(0xB40A, 'Read next character', align=Align.INLINE)
d.comment(0xB40D, 'Save updated pointer', align=Align.INLINE)
d.comment(0xB411, 'Store char uppercased in buffer', align=Align.INLINE)
d.comment(0xB414, 'Loop for more characters', align=Align.INLINE)
d.comment(0xB416, 'Copy reversed PS name to TX', align=Align.INLINE)
d.comment(0xB419, 'Send PS status request', align=Align.INLINE)
d.comment(0xB41C, 'Pop and requeue PS scan', align=Align.INLINE)
d.comment(0xB41F, 'Load PS server address', align=Align.INLINE)
d.comment(0xB422, 'A=0', align=Align.INLINE)
d.comment(0xB425, 'Offset &24 in buffer', align=Align.INLINE)
d.comment(0xB427, 'Clear PS status byte', align=Align.INLINE)
d.comment(0xB42A, 'Zero: all slots done', align=Align.INLINE)
d.comment(0xB42D, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB42E, 'Read slot status', align=Align.INLINE)
d.comment(0xB430, 'Bit 7 clear: slot inactive', align=Align.INLINE)
d.comment(0xB450, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB4B4, 'Pop return address low', align=Align.INLINE)
d.comment(0xB4BA, 'Push 0 as end-of-list marker', align=Align.INLINE)
d.comment(0xB4BD, 'Start scanning from offset &84', align=Align.INLINE)
d.comment(0xB4C1, 'Shift PS slot flags right', align=Align.INLINE)
d.comment(0xB4C6, 'Convert to 2-bit workspace index', align=Align.INLINE)
d.comment(0xB4C9, 'Carry set: no more slots', align=Align.INLINE)
d.comment(0xB4CC, 'To get slot offset', align=Align.INLINE)
d.comment(0xB4D8, 'Loop for more slots', align=Align.INLINE)
d.comment(0xB4E1, 'Low byte: workspace page', align=Align.INLINE)
d.comment(0xB4FC, 'Write another page + &FF bytes', align=Align.INLINE)
d.comment(0xB502, 'Shift PS slot flags back', align=Align.INLINE)
d.comment(0xB507, 'Push onto stack', align=Align.INLINE)
d.comment(0xB515, 'Middle loop: 10 iterations', align=Align.INLINE)
d.comment(0xB519, 'Outer loop: ~1000 delay cycles', align=Align.INLINE)
d.comment(0xB521, 'A=&FF', align=Align.INLINE)
d.comment(0xB527, 'Write byte to workspace', align=Align.INLINE)
d.comment(0xB529, 'Advance Y', align=Align.INLINE)
d.comment(0xB52B, 'Start of PS name at offset &1C', align=Align.INLINE)
d.comment(0xB535, 'End of TX name field at &1B', align=Align.INLINE)
d.comment(0xB537, 'Pop byte (reversed order)', align=Align.INLINE)
d.comment(0xB53B, 'Start of TX field (&0F)?', align=Align.INLINE)
d.comment(0xB53F, 'Copy RX page to TX', align=Align.INLINE)
d.comment(0xB543, 'TX offset &10', align=Align.INLINE)
d.comment(0xB552, 'Control byte &80 (immediate TX)', align=Align.INLINE)
d.comment(0xB553, 'Port &9F (printer server)', align=Align.INLINE)
d.comment(0xB554, 'Station &FF (any)', align=Align.INLINE)
d.comment(0xB555, 'Network &FF (any)', align=Align.INLINE)
d.comment(0xB556, 'Save V flag (controls padding)', align=Align.INLINE)
d.comment(0xB55E, "'.' separator", align=Align.INLINE)
d.comment(0xB563, 'Set V (suppress station padding)', align=Align.INLINE)
d.comment(0xB568, 'Print 4 spaces (padding)', align=Align.INLINE)
d.comment(0xB571, 'Restore flags', align=Align.INLINE)
d.comment(0xB572, 'Print station as 3 digits', align=Align.INLINE)
d.comment(0xB7D3, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0xB7D5, 'X=1: flush input buffers', align=Align.INLINE)
d.comment(0xB7D7, 'Flush keyboard buffer before read', align=Align.INLINE)
d.comment(0xB7DA, 'Read character from input stream', align=Align.INLINE)
d.comment(0xB7DD, 'C clear: character read OK', align=Align.INLINE)
d.comment(0xB7DF, 'Escape pressed: raise error', align=Align.INLINE)
d.comment(0xB7E2, 'Return with character in A', align=Align.INLINE)
d.comment(0xB7E3, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB7E5, 'Y=0: start index', align=Align.INLINE)
d.comment(0xB7E6, 'Clear channel table entry', align=Align.INLINE)
d.comment(0xB7E9, 'Next entry', align=Align.INLINE)
d.comment(0xB7EA, 'Loop until all 256 bytes cleared', align=Align.INLINE)
d.comment(0xB7EC, 'Offset &0F in receive buffer', align=Align.INLINE)
d.comment(0xB7EE, 'Get number of available channels', align=Align.INLINE)
d.comment(0xB7F0, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB7F1, "Subtract 'Z' to get negative count", align=Align.INLINE)
d.comment(0xB7F3, 'Y = negative channel count (index)', align=Align.INLINE)
d.comment(0xB7F4, 'Channel marker &40 (available)', align=Align.INLINE)
d.comment(0xB7F6, 'Mark channel slot as available', align=Align.INLINE)
d.comment(0xB7F9, 'Previous channel slot', align=Align.INLINE)
d.comment(0xB7FA, 'Reached start of channel range?', align=Align.INLINE)
d.comment(0xB7FC, 'No: continue marking channels', align=Align.INLINE)
d.comment(0xB7FE, 'Point to first channel slot', align=Align.INLINE)
d.comment(0xB7FF, 'Active channel marker &C0', align=Align.INLINE)
d.comment(0xB801, 'Mark first channel as active', align=Align.INLINE)
d.comment(0xB804, 'Return', align=Align.INLINE)
d.comment(0xB805, 'Save flags', align=Align.INLINE)
d.comment(0xB806, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB807, 'Subtract &20 to get table index', align=Align.INLINE)
d.comment(0xB809, 'Negative: out of valid range', align=Align.INLINE)
d.comment(0xB80B, 'Above maximum channel index &0F?', align=Align.INLINE)
d.comment(0xB80D, 'In range: valid index', align=Align.INLINE)
d.comment(0xB80F, 'Out of range: return &FF (invalid)', align=Align.INLINE)
d.comment(0xB811, 'Restore flags', align=Align.INLINE)
d.comment(0xB812, 'X = channel index (or &FF)', align=Align.INLINE)
d.comment(0xB813, 'Return', align=Align.INLINE)
d.comment(0xB814, 'Below space?', align=Align.INLINE)
d.comment(0xB816, 'Yes: invalid channel character', align=Align.INLINE)
d.comment(0xB818, "Below '0'?", align=Align.INLINE)
d.comment(0xB81A, 'In range &20-&2F: look up channel', align=Align.INLINE)
d.comment(0xB81C, 'Save channel character', align=Align.INLINE)
d.comment(0xB81D, 'Error code &DE', align=Align.INLINE)
d.comment(0xB81F, "Generate 'Net channel' error", align=Align.INLINE)
d.comment(0xB82E, 'Error string continuation (unreachable)', align=Align.INLINE)
d.comment(0xB847, 'Save channel character', align=Align.INLINE)
d.comment(0xB848, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB849, 'Convert char to table index', align=Align.INLINE)
d.comment(0xB84B, 'X = channel table index', align=Align.INLINE)
d.comment(0xB84C, 'Look up network number for channel', align=Align.INLINE)
d.comment(0xB84F, 'Zero: channel not found, raise error', align=Align.INLINE)
d.comment(0xB851, 'Check station/network matches current', align=Align.INLINE)
d.comment(0xB854, 'No match: build detailed error msg', align=Align.INLINE)
d.comment(0xB856, 'Discard saved channel character', align=Align.INLINE)
d.comment(0xB857, 'Load channel status flags', align=Align.INLINE)
d.comment(0xB85A, 'Return; A = channel flags', align=Align.INLINE)
d.comment(0xB85B, 'Error code &DE', align=Align.INLINE)
d.comment(0xB85D, 'Store error code in error block', align=Align.INLINE)
d.comment(0xB860, 'BRK opcode', align=Align.INLINE)
d.comment(0xB862, 'Store BRK at start of error block', align=Align.INLINE)
d.comment(0xB865, 'X=0: copy index', align=Align.INLINE)
d.comment(0xB866, 'Advance copy position', align=Align.INLINE)
d.comment(0xB867, "Load 'Net channel' string byte", align=Align.INLINE)
d.comment(0xB86A, 'Copy to error text', align=Align.INLINE)
d.comment(0xB86D, 'Continue until NUL terminator', align=Align.INLINE)
d.comment(0xB86F, 'Save end-of-string position', align=Align.INLINE)
d.comment(0xB871, 'Save for suffix append', align=Align.INLINE)
d.comment(0xB873, 'Retrieve channel character', align=Align.INLINE)
d.comment(0xB874, "Append ' N' (channel number)", align=Align.INLINE)
d.comment(0xB877, "Load 'Net channel' end position", align=Align.INLINE)
d.comment(0xB879, 'Skip past NUL to suffix string', align=Align.INLINE)
d.comment(0xB87A, 'Advance destination position', align=Align.INLINE)
d.comment(0xB87B, "Load ' not on this...' suffix byte", align=Align.INLINE)
d.comment(0xB87E, 'Append to error message', align=Align.INLINE)
d.comment(0xB881, 'Continue until NUL', align=Align.INLINE)
d.comment(0xB883, 'Raise the constructed error', align=Align.INLINE)
d.comment(0xB886, 'Load current channel attribute', align=Align.INLINE)
d.comment(0xB889, 'Store channel attribute to RX buffer', align=Align.INLINE)
d.comment(0xB88C, 'Validate and look up channel', align=Align.INLINE)
d.comment(0xB88F, 'Test directory flag (bit 1)', align=Align.INLINE)
d.comment(0xB891, 'Not a directory: return OK', align=Align.INLINE)
d.comment(0xB893, 'Error code &A8', align=Align.INLINE)
d.comment(0xB895, "Generate 'Is a dir.' error", align=Align.INLINE)
d.comment(0xB8A8, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB8A9, 'Start scanning from FCB slot &20', align=Align.INLINE)
d.comment(0xB8AB, 'Load FCB station byte', align=Align.INLINE)
d.comment(0xB8AE, 'Zero: slot is free, use it', align=Align.INLINE)
d.comment(0xB8B0, 'Try next slot', align=Align.INLINE)
d.comment(0xB8B1, 'Past last FCB slot &2F?', align=Align.INLINE)
d.comment(0xB8B3, 'No: check next slot', align=Align.INLINE)
d.comment(0xB8B5, 'No free slot: discard saved attribute', align=Align.INLINE)
d.comment(0xB8B6, 'A=0: return failure (Z set)', align=Align.INLINE)
d.comment(0xB8B8, 'Return', align=Align.INLINE)
d.comment(0xB8B9, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB8BA, 'Store attribute in FCB slot', align=Align.INLINE)
d.comment(0xB8BD, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB8BF, 'Clear FCB transfer count low', align=Align.INLINE)
d.comment(0xB8C2, 'Clear FCB transfer count mid', align=Align.INLINE)
d.comment(0xB8C5, 'Clear FCB transfer count high', align=Align.INLINE)
d.comment(0xB8C8, 'Load current station number', align=Align.INLINE)
d.comment(0xB8CB, 'Store station in FCB', align=Align.INLINE)
d.comment(0xB8CE, 'Load current network number', align=Align.INLINE)
d.comment(0xB8D1, 'Store network in FCB', align=Align.INLINE)
d.comment(0xB8D4, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB8D5, 'Save slot index', align=Align.INLINE)
d.comment(0xB8D6, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB8D7, 'Convert slot to channel index (0-&0F)', align=Align.INLINE)
d.comment(0xB8D9, 'X = channel index', align=Align.INLINE)
d.comment(0xB8DA, 'Restore A = FCB slot index', align=Align.INLINE)
d.comment(0xB8DB, 'Return; A=slot, X=channel, Z clear', align=Align.INLINE)
d.comment(0xB8DC, 'Save argument', align=Align.INLINE)
d.comment(0xB8DD, 'A=0: allocate any available slot', align=Align.INLINE)
d.comment(0xB8DF, 'Try to allocate an FCB slot', align=Align.INLINE)
d.comment(0xB8E2, 'Success: slot allocated', align=Align.INLINE)
d.comment(0xB8E4, 'Error code &C0', align=Align.INLINE)
d.comment(0xB8E6, "Generate 'No more FCBs' error", align=Align.INLINE)
d.comment(0xB8F6, 'Restore argument', align=Align.INLINE)
d.comment(0xB8F7, 'Return', align=Align.INLINE)
d.comment(0xB8F8, 'C=0: close all matching channels', align=Align.INLINE)
d.comment(0xB8F9, 'Branch always to scan entry', align=Align.INLINE)
d.comment(0xB8FC, 'Start from FCB slot &10', align=Align.INLINE)
d.comment(0xB8FE, 'Previous FCB slot', align=Align.INLINE)
d.comment(0xB8FF, 'More slots to check', align=Align.INLINE)
d.comment(0xB901, 'All FCB slots processed, return', align=Align.INLINE)
d.comment(0xB902, 'Load channel flags for this slot', align=Align.INLINE)
d.comment(0xB905, 'Save flags in Y', align=Align.INLINE)
d.comment(0xB906, 'Test active flag (bit 1)', align=Align.INLINE)
d.comment(0xB908, 'Not active: check station match', align=Align.INLINE)
d.comment(0xB90A, 'V clear (close all): next slot', align=Align.INLINE)
d.comment(0xB90C, 'C clear: check station match', align=Align.INLINE)
d.comment(0xB90E, 'Restore original flags', align=Align.INLINE)
d.comment(0xB90F, 'Clear write-pending flag (bit 5)', align=Align.INLINE)
d.comment(0xB911, 'Update channel flags', align=Align.INLINE)
d.comment(0xB914, 'Next slot (V always set here)', align=Align.INLINE)
d.comment(0xB916, 'Check if channel belongs to station', align=Align.INLINE)
d.comment(0xB919, 'No match: skip to next slot', align=Align.INLINE)
d.comment(0xB91B, 'A=0: clear channel', align=Align.INLINE)
d.comment(0xB91D, 'Clear channel flags (close it)', align=Align.INLINE)
d.comment(0xB920, 'Clear network number', align=Align.INLINE)
d.comment(0xB923, 'Continue to next slot', align=Align.INLINE)
d.comment(0xB925, 'Load FCB station number', align=Align.INLINE)
d.comment(0xB928, 'Compare with current station', align=Align.INLINE)
d.comment(0xB92B, 'Different: Z=0, no match', align=Align.INLINE)
d.comment(0xB92D, 'Load FCB network number', align=Align.INLINE)
d.comment(0xB930, 'Compare with current network', align=Align.INLINE)
d.comment(0xB933, 'Return; Z=1 if match, Z=0 if not', align=Align.INLINE)
d.comment(0xB934, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB937, 'Set V flag (first pass marker)', align=Align.INLINE)
d.comment(0xB93A, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB93B, 'Past end of table (&10)?', align=Align.INLINE)
d.comment(0xB93D, 'No: continue checking', align=Align.INLINE)
d.comment(0xB93F, 'Wrap around to slot 0', align=Align.INLINE)
d.comment(0xB941, 'Back to starting slot?', align=Align.INLINE)
d.comment(0xB944, 'No: check this slot', align=Align.INLINE)
d.comment(0xB946, 'V clear (second pass): scan empties', align=Align.INLINE)
d.comment(0xB948, 'Clear V for second pass', align=Align.INLINE)
d.comment(0xB949, 'Continue scanning', align=Align.INLINE)
d.comment(0xB94B, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB94E, 'Shift bit 7 (in-use) into carry', align=Align.INLINE)
d.comment(0xB94F, 'Not in use: skip', align=Align.INLINE)
d.comment(0xB951, 'Test bit 2 (modified flag)', align=Align.INLINE)
d.comment(0xB953, 'Modified: check further conditions', align=Align.INLINE)
d.comment(0xB955, 'Adjust for following INX', align=Align.INLINE)
d.comment(0xB956, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB957, 'Past end of table?', align=Align.INLINE)
d.comment(0xB959, 'No: continue', align=Align.INLINE)
d.comment(0xB95B, 'Wrap around to slot 0', align=Align.INLINE)
d.comment(0xB95D, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB960, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0xB961, 'Not in use: continue scanning', align=Align.INLINE)
d.comment(0xB963, 'Set carry', align=Align.INLINE)
d.comment(0xB964, 'Restore original flags', align=Align.INLINE)
d.comment(0xB965, 'Save flags back (mark as found)', align=Align.INLINE)
d.comment(0xB968, 'Restore original FCB index', align=Align.INLINE)
d.comment(0xB96B, 'Return with found slot in X', align=Align.INLINE)
d.comment(0xB96C, 'V set (first pass): skip modified', align=Align.INLINE)
d.comment(0xB96E, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB971, 'Test bit 5 (offset pending)', align=Align.INLINE)
d.comment(0xB973, 'Bit 5 set: skip this slot', align=Align.INLINE)
d.comment(0xB975, 'Use this slot', align=Align.INLINE)
d.comment(0xB977, 'Initial pass count = 1', align=Align.INLINE)
d.comment(0xB979, 'Store pass counter', align=Align.INLINE)
d.comment(0xB97C, 'Y=0', align=Align.INLINE)
d.comment(0xB97D, 'Clear byte counter low', align=Align.INLINE)
d.comment(0xB980, 'Clear offset counter', align=Align.INLINE)
d.comment(0xB983, 'Clear transfer flag', align=Align.INLINE)
d.comment(0xB986, 'A=0', align=Align.INLINE)
d.comment(0xB987, 'Clear 3 counter bytes', align=Align.INLINE)
d.comment(0xB989, 'Clear counter byte', align=Align.INLINE)
d.comment(0xB98C, 'Next byte', align=Align.INLINE)
d.comment(0xB98D, 'Loop for indices 2, 1, 0', align=Align.INLINE)
d.comment(0xB98F, 'Store &FF as sentinel in xfer_sentinel_1', align=Align.INLINE)
d.comment(0xB992, 'Store &FF as sentinel in xfer_sentinel_2', align=Align.INLINE)
d.comment(0xB995, 'X=&CA: workspace offset', align=Align.INLINE)
d.comment(0xB997, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB999, 'Return; X/Y point to &10CA', align=Align.INLINE)
d.comment(0xB99A, 'Verify workspace checksum integrity', align=Align.INLINE)
d.comment(0xB99D, 'Save current FCB index', align=Align.INLINE)
d.comment(0xB9A0, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB9A3, 'Shift bit 0 (active) into carry', align=Align.INLINE)
d.comment(0xB9A4, 'Not active: clear status and return', align=Align.INLINE)
d.comment(0xB9A6, 'Save current station low to stack', align=Align.INLINE)
d.comment(0xB9A9, 'Push station low', align=Align.INLINE)
d.comment(0xB9AA, 'Save current station high', align=Align.INLINE)
d.comment(0xB9AD, 'Push station high', align=Align.INLINE)
d.comment(0xB9AE, 'Load FCB station low', align=Align.INLINE)
d.comment(0xB9B1, 'Set as working station low', align=Align.INLINE)
d.comment(0xB9B4, 'Load FCB station high', align=Align.INLINE)
d.comment(0xB9B7, 'Set as working station high', align=Align.INLINE)
d.comment(0xB9BA, 'Reset transfer counters', align=Align.INLINE)
d.comment(0xB9BD, 'Set offset to &FF (no data yet)', align=Align.INLINE)
d.comment(0xB9C0, 'Set pass counter to 0 (flush mode)', align=Align.INLINE)
d.comment(0xB9C3, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB9C6, 'Transfer to A', align=Align.INLINE)
d.comment(0xB9C7, 'Prepare addition', align=Align.INLINE)
d.comment(0xB9C8, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB9CA, 'Store buffer address high byte', align=Align.INLINE)
d.comment(0xB9CD, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB9D0, 'Test bit 5 (has saved offset)', align=Align.INLINE)
d.comment(0xB9D2, 'No offset: skip restore', align=Align.INLINE)
d.comment(0xB9D4, 'Load saved byte offset', align=Align.INLINE)
d.comment(0xB9D7, 'Restore offset counter', align=Align.INLINE)
d.comment(0xB9DA, 'Load FCB attribute reference', align=Align.INLINE)
d.comment(0xB9DD, 'Store as current reference', align=Align.INLINE)
d.comment(0xB9E0, 'Transfer to X', align=Align.INLINE)
d.comment(0xB9E1, 'Read saved receive attribute', align=Align.INLINE)
d.comment(0xB9E4, 'Push to stack', align=Align.INLINE)
d.comment(0xB9E5, 'Restore attribute to A', align=Align.INLINE)
d.comment(0xB9E6, 'Set attribute in receive buffer', align=Align.INLINE)
d.comment(0xB9E8, 'X=&CA: workspace offset', align=Align.INLINE)
d.comment(0xB9EA, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB9EC, 'A=0: standard transfer mode', align=Align.INLINE)
d.comment(0xB9EE, 'Send data and receive response', align=Align.INLINE)
d.comment(0xB9F1, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB9F4, 'Restore saved receive attribute', align=Align.INLINE)
d.comment(0xB9F5, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB9F8, 'Restore station high', align=Align.INLINE)
d.comment(0xB9F9, 'Store station high', align=Align.INLINE)
d.comment(0xB9FC, 'Restore station low', align=Align.INLINE)
d.comment(0xB9FD, 'Store station low', align=Align.INLINE)
d.comment(0xBA00, 'Mask &DC: clear bits 0, 1, 5', align=Align.INLINE)
d.comment(0xBA02, 'Clear active and offset flags', align=Align.INLINE)
d.comment(0xBA05, 'Update FCB status', align=Align.INLINE)
d.comment(0xBA08, 'Return', align=Align.INLINE)
d.comment(0xBA09, 'Copy 13 bytes (indices 0 to &0C)', align=Align.INLINE)
d.comment(0xBA0B, 'Load TX buffer byte', align=Align.INLINE)
d.comment(0xBA0E, 'Save to context buffer at &10D9', align=Align.INLINE)
d.comment(0xBA11, 'Load workspace byte from fs_load_addr', align=Align.INLINE)
d.comment(0xBA13, 'Save to stack', align=Align.INLINE)
d.comment(0xBA14, 'Next byte down', align=Align.INLINE)
d.comment(0xBA15, 'Loop for all 13 bytes', align=Align.INLINE)
d.comment(0xBA17, 'Y=0? (no FCB to process)', align=Align.INLINE)
d.comment(0xBA19, 'Non-zero: scan and process FCBs', align=Align.INLINE)
d.comment(0xBA1B, 'Y=0: skip to restore workspace', align=Align.INLINE)
d.comment(0xBA1E, 'Save flags', align=Align.INLINE)
d.comment(0xBA1F, 'X=&FF: start scanning from -1', align=Align.INLINE)
d.comment(0xBA21, 'Next FCB slot', align=Align.INLINE)
d.comment(0xBA22, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xBA25, 'Bit 7 clear: not pending, skip', align=Align.INLINE)
d.comment(0xBA27, 'Shift bit 6 to bit 7', align=Align.INLINE)
d.comment(0xBA28, 'Bit 6 clear: skip', align=Align.INLINE)
d.comment(0xBA2A, "Flush this FCB's pending data", align=Align.INLINE)
d.comment(0xBA2D, 'Pending marker &40', align=Align.INLINE)
d.comment(0xBA2F, 'Mark FCB as pending-only', align=Align.INLINE)
d.comment(0xBA32, 'Save flags', align=Align.INLINE)
d.comment(0xBA33, 'Find next available FCB slot', align=Align.INLINE)
d.comment(0xBA36, 'Restore flags', align=Align.INLINE)
d.comment(0xBA37, 'Load current channel attribute', align=Align.INLINE)
d.comment(0xBA3A, 'Store as current reference', align=Align.INLINE)
d.comment(0xBA3D, 'Save attribute', align=Align.INLINE)
d.comment(0xBA3E, 'Prepare attribute-to-channel conversion', align=Align.INLINE)
d.comment(0xBA3F, 'Convert attribute (&20+) to channel index', align=Align.INLINE)
d.comment(0xBA41, 'Y = attribute index', align=Align.INLINE)
d.comment(0xBA42, 'Load station for this attribute', align=Align.INLINE)
d.comment(0xBA45, 'Store station in TX buffer', align=Align.INLINE)
d.comment(0xBA48, 'Restore attribute', align=Align.INLINE)
d.comment(0xBA49, 'Store attribute in FCB slot', align=Align.INLINE)
d.comment(0xBA4C, 'Load working station low', align=Align.INLINE)
d.comment(0xBA4F, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xBA52, 'Load working station high', align=Align.INLINE)
d.comment(0xBA55, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xBA58, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xBA59, 'Prepare addition', align=Align.INLINE)
d.comment(0xBA5A, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xBA5C, 'Store buffer address high byte', align=Align.INLINE)
d.comment(0xBA5F, 'Restore flags', align=Align.INLINE)
d.comment(0xBA60, 'V clear: skip directory request', align=Align.INLINE)
d.comment(0xBA62, 'Command byte = 0', align=Align.INLINE)
d.comment(0xBA65, 'Reset transfer counters', align=Align.INLINE)
d.comment(0xBA68, 'Read saved receive attribute', align=Align.INLINE)
d.comment(0xBA6B, 'Function code &0D', align=Align.INLINE)
d.comment(0xBA6C, 'Load current reference', align=Align.INLINE)
d.comment(0xBA6F, 'Set in receive buffer', align=Align.INLINE)
d.comment(0xBA71, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xBA73, 'A=2: transfer mode 2', align=Align.INLINE)
d.comment(0xBA75, 'Send and receive data', align=Align.INLINE)
d.comment(0xBA78, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xBA79, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xBA7C, 'Reload FCB index', align=Align.INLINE)
d.comment(0xBA7F, 'Load pass counter', align=Align.INLINE)
d.comment(0xBA82, 'Non-zero: data received, calc offset', align=Align.INLINE)
d.comment(0xBA84, 'Load offset counter', align=Align.INLINE)
d.comment(0xBA87, 'Zero: no data received at all', align=Align.INLINE)
d.comment(0xBA89, 'Load offset counter', align=Align.INLINE)
d.comment(0xBA8C, 'Negate (ones complement)', align=Align.INLINE)
d.comment(0xBA8E, 'Clear carry for add', align=Align.INLINE)
d.comment(0xBA8F, 'Complete twos complement negation', align=Align.INLINE)
d.comment(0xBA91, 'Store negated offset in FCB', align=Align.INLINE)
d.comment(0xBA94, 'Set bit 5 (has saved offset)', align=Align.INLINE)
d.comment(0xBA96, 'Add to FCB flags', align=Align.INLINE)
d.comment(0xBA99, 'Update FCB status', align=Align.INLINE)
d.comment(0xBA9C, 'Load buffer address high byte', align=Align.INLINE)
d.comment(0xBA9F, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xBAA1, 'A=0: pointer low byte and clear val', align=Align.INLINE)
d.comment(0xBAA3, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xBAA5, 'Load negated offset (start of clear)', align=Align.INLINE)
d.comment(0xBAA8, 'Clear buffer byte', align=Align.INLINE)
d.comment(0xBAAA, 'Next byte', align=Align.INLINE)
d.comment(0xBAAB, 'Loop until page boundary', align=Align.INLINE)
d.comment(0xBAAD, 'Set bit 1 (active flag)', align=Align.INLINE)
d.comment(0xBAAF, 'Add active flag to status', align=Align.INLINE)
d.comment(0xBAB2, 'Update FCB status', align=Align.INLINE)
d.comment(0xBAB5, 'Y=0: start restoring workspace', align=Align.INLINE)
d.comment(0xBAB7, 'Restore workspace byte from stack', align=Align.INLINE)
d.comment(0xBAB8, 'Store to fs_load_addr workspace', align=Align.INLINE)
d.comment(0xBABB, 'Next byte', align=Align.INLINE)
d.comment(0xBABC, 'Restored all 13 bytes?', align=Align.INLINE)
d.comment(0xBABE, 'No: continue restoring', align=Align.INLINE)
d.comment(0xBAC0, 'Copy 13 bytes (indices 0 to &0C)', align=Align.INLINE)
d.comment(0xBAC2, 'Load saved catalog byte from &10D9', align=Align.INLINE)
d.comment(0xBAC5, 'Restore to TX buffer', align=Align.INLINE)
d.comment(0xBAC8, 'Next byte down', align=Align.INLINE)
d.comment(0xBAC9, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xBACB, 'Return', align=Align.INLINE)
d.comment(0xBACC, 'Save current context first', align=Align.INLINE)
d.comment(0xBACF, 'X=&FF: start scanning from -1', align=Align.INLINE)
d.comment(0xBAD1, 'Load channel attribute to match', align=Align.INLINE)
d.comment(0xBAD4, 'Next FCB slot', align=Align.INLINE)
d.comment(0xBAD5, 'Past end of table (&10)?', align=Align.INLINE)
d.comment(0xBAD7, 'No: check this slot', align=Align.INLINE)
d.comment(0xBAD9, 'Load channel attribute', align=Align.INLINE)
d.comment(0xBADC, 'Convert to channel index', align=Align.INLINE)
d.comment(0xBADF, 'Load station for this channel', align=Align.INLINE)
d.comment(0xBAE2, 'Store as match target station high', align=Align.INLINE)
d.comment(0xBAE5, 'Load port for this channel', align=Align.INLINE)
d.comment(0xBAE8, 'Store as match target station low', align=Align.INLINE)
d.comment(0xBAEB, 'Save context and rescan from start', align=Align.INLINE)
d.comment(0xBAEE, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xBAF1, 'Test active flag (bit 1)', align=Align.INLINE)
d.comment(0xBAF3, 'Not active: skip to next', align=Align.INLINE)
d.comment(0xBAF5, 'Get attribute to match', align=Align.INLINE)
d.comment(0xBAF6, 'Compare with FCB attribute ref', align=Align.INLINE)
d.comment(0xBAF9, 'No attribute match: skip', align=Align.INLINE)
d.comment(0xBAFB, 'Save matching FCB index', align=Align.INLINE)
d.comment(0xBAFE, 'Save flags from attribute compare', align=Align.INLINE)
d.comment(0xBAFF, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xBB00, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0xBB02, 'Restore flags from attribute compare', align=Align.INLINE)
d.comment(0xBB03, 'Y = channel index', align=Align.INLINE)
d.comment(0xBB04, 'Reload FCB index', align=Align.INLINE)
d.comment(0xBB07, 'Load channel station byte', align=Align.INLINE)
d.comment(0xBB0A, 'Compare with FCB station', align=Align.INLINE)
d.comment(0xBB0D, 'Station mismatch: try next', align=Align.INLINE)
d.comment(0xBB0F, 'Load channel network byte', align=Align.INLINE)
d.comment(0xBB12, 'Compare with FCB network', align=Align.INLINE)
d.comment(0xBB15, 'Network mismatch: try next', align=Align.INLINE)
d.comment(0xBB17, 'Load FCB flags', align=Align.INLINE)
d.comment(0xBB1A, 'Bit 7 clear: no pending flush', align=Align.INLINE)
d.comment(0xBB1C, 'Clear pending flag (bit 7)', align=Align.INLINE)
d.comment(0xBB1E, 'Update FCB status', align=Align.INLINE)
d.comment(0xBB21, 'Find new open FCB slot', align=Align.INLINE)
d.comment(0xBB24, 'Reload FCB flags', align=Align.INLINE)
d.comment(0xBB27, 'Test bit 5 (has offset data)', align=Align.INLINE)
d.comment(0xBB29, 'Return; Z=1 no offset, Z=0 has data', align=Align.INLINE)
d.comment(0xBB2A, 'Increment byte count low', align=Align.INLINE)
d.comment(0xBB2D, 'No overflow: done', align=Align.INLINE)
d.comment(0xBB2F, 'Increment byte count mid', align=Align.INLINE)
d.comment(0xBB32, 'No overflow: done', align=Align.INLINE)
d.comment(0xBB34, 'Increment byte count high', align=Align.INLINE)
d.comment(0xBB37, 'Return', align=Align.INLINE)
d.comment(0xBB67, 'Return', align=Align.INLINE)
d.comment(0xBB68, 'Save channel attribute', align=Align.INLINE)
d.comment(0xBB6B, "Save caller's X", align=Align.INLINE)
d.comment(0xBB6C, 'Push X', align=Align.INLINE)
d.comment(0xBB6D, 'Store result and check not directory', align=Align.INLINE)
d.comment(0xBB70, 'Load channel flags', align=Align.INLINE)
d.comment(0xBB73, 'Test write-only flag (bit 5)', align=Align.INLINE)
d.comment(0xBB75, 'Not write-only: proceed with read', align=Align.INLINE)
d.comment(0xBB77, 'Error code &D4', align=Align.INLINE)
d.comment(0xBB79, "Generate 'Write only' error", align=Align.INLINE)
d.comment(0xBB87, 'Clear V (first-pass matching)', align=Align.INLINE)
d.comment(0xBB88, 'Find FCB matching this channel', align=Align.INLINE)
d.comment(0xBB8B, 'No offset: read byte from buffer', align=Align.INLINE)
d.comment(0xBB8D, 'Load byte count for matching FCB', align=Align.INLINE)
d.comment(0xBB90, 'Compare with buffer offset limit', align=Align.INLINE)
d.comment(0xBB93, 'Below offset: data available', align=Align.INLINE)
d.comment(0xBB95, 'Load channel flags for FCB', align=Align.INLINE)
d.comment(0xBB98, 'Transfer to X for testing', align=Align.INLINE)
d.comment(0xBB99, 'Test bit 6 (EOF already signalled)', align=Align.INLINE)
d.comment(0xBB9B, 'EOF already set: raise error', align=Align.INLINE)
d.comment(0xBB9D, 'Restore flags', align=Align.INLINE)
d.comment(0xBB9E, 'Set EOF flag (bit 6)', align=Align.INLINE)
d.comment(0xBBA0, 'Update channel flags with EOF', align=Align.INLINE)
d.comment(0xBBA3, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xBBA5, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0xBBA8, "Restore caller's X", align=Align.INLINE)
d.comment(0xBBA9, 'X restored', align=Align.INLINE)
d.comment(0xBBAA, 'A=&FE: EOF marker byte', align=Align.INLINE)
d.comment(0xBBAC, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xBBAF, 'C=1: end of file', align=Align.INLINE)
d.comment(0xBBB0, 'Return', align=Align.INLINE)
d.comment(0xBBB1, 'Error code &DF', align=Align.INLINE)
d.comment(0xBBB3, "Generate 'End of file' error", align=Align.INLINE)
d.comment(0xBBC2, 'Load current byte count (= offset)', align=Align.INLINE)
d.comment(0xBBC5, 'Save byte count', align=Align.INLINE)
d.comment(0xBBC6, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xBBC7, 'X = FCB slot for byte count inc', align=Align.INLINE)
d.comment(0xBBC8, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xBBCA, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0xBBCD, 'Increment byte count for this FCB', align=Align.INLINE)
d.comment(0xBBD0, 'Restore byte count (= buffer offset)', align=Align.INLINE)
d.comment(0xBBD1, 'Y = offset into data buffer', align=Align.INLINE)
d.comment(0xBBD2, 'Load current FCB index', align=Align.INLINE)
d.comment(0xBBD5, 'Prepare addition', align=Align.INLINE)
d.comment(0xBBD6, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xBBD8, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xBBDA, 'A=0: pointer low byte', align=Align.INLINE)
d.comment(0xBBDC, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xBBDE, "Restore caller's X", align=Align.INLINE)
d.comment(0xBBDF, 'X restored', align=Align.INLINE)
d.comment(0xBBE0, 'Read data byte from buffer', align=Align.INLINE)
d.comment(0xBBE2, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xBBE5, 'C=0: byte read successfully', align=Align.INLINE)
d.comment(0xBBE6, 'Return; A = data byte', align=Align.INLINE)
d.comment(0xBBE7, 'Save channel attribute', align=Align.INLINE)
d.comment(0xBBEA, 'Save data byte', align=Align.INLINE)
d.comment(0xBBEB, 'Y = data byte', align=Align.INLINE)
d.comment(0xBBEC, "Save caller's X", align=Align.INLINE)
d.comment(0xBBED, 'Push X', align=Align.INLINE)
d.comment(0xBBEE, 'Restore data byte to A', align=Align.INLINE)
d.comment(0xBBEF, 'Push data byte for later', align=Align.INLINE)
d.comment(0xBBF0, 'Save data byte in workspace', align=Align.INLINE)
d.comment(0xBBF3, 'Store result and check not directory', align=Align.INLINE)
d.comment(0xBBF6, 'Load channel flags', align=Align.INLINE)
d.comment(0xBBF9, 'Bit 7 set: channel open, proceed', align=Align.INLINE)
d.comment(0xBBFB, 'Error &C1: Not open for update', align=Align.INLINE)
d.comment(0xBBFD, 'Raise error with inline string', align=Align.INLINE)
d.comment(0xBC14, 'Test write flag (bit 5)', align=Align.INLINE)
d.comment(0xBC16, 'Not write-capable: use buffer path', align=Align.INLINE)
d.comment(0xBC18, 'Load reply port for this channel', align=Align.INLINE)
d.comment(0xBC1B, 'Restore data byte', align=Align.INLINE)
d.comment(0xBC1C, 'Send byte directly to server', align=Align.INLINE)
d.comment(0xBC1F, 'Update byte count and return', align=Align.INLINE)
d.comment(0xBC22, 'Set V flag (alternate match mode)', align=Align.INLINE)
d.comment(0xBC25, 'Find matching FCB for channel', align=Align.INLINE)
d.comment(0xBC28, 'Load byte count for FCB', align=Align.INLINE)
d.comment(0xBC2B, 'Buffer full (&FF bytes)?', align=Align.INLINE)
d.comment(0xBC2D, 'No: store byte in buffer', align=Align.INLINE)
d.comment(0xBC2F, 'Save X', align=Align.INLINE)
d.comment(0xBC32, 'Push Y', align=Align.INLINE)
d.comment(0xBC35, 'Below offset: skip offset update', align=Align.INLINE)
d.comment(0xBC37, 'Carry set from BCS/BCC above', align=Align.INLINE)
d.comment(0xBC39, 'Update buffer offset in FCB', align=Align.INLINE)
d.comment(0xBC3C, 'Non-zero: keep offset flag', align=Align.INLINE)
d.comment(0xBC3E, 'Mask &DF: clear bit 5', align=Align.INLINE)
d.comment(0xBC40, 'Clear offset flag', align=Align.INLINE)
d.comment(0xBC43, 'Update FCB status', align=Align.INLINE)
d.comment(0xBC46, 'Set bit 0 (dirty/active)', align=Align.INLINE)
d.comment(0xBC48, 'Add to FCB flags', align=Align.INLINE)
d.comment(0xBC4B, 'Update FCB status', align=Align.INLINE)
d.comment(0xBC4E, 'Load byte count (= write position)', align=Align.INLINE)
d.comment(0xBC51, 'Save count', align=Align.INLINE)
d.comment(0xBC52, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xBC53, 'X = FCB slot', align=Align.INLINE)
d.comment(0xBC54, 'Restore byte count', align=Align.INLINE)
d.comment(0xBC55, 'Y = buffer write offset', align=Align.INLINE)
d.comment(0xBC56, 'Load current FCB index', align=Align.INLINE)
d.comment(0xBC59, 'Prepare addition', align=Align.INLINE)
d.comment(0xBC5A, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xBC5C, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xBC5E, 'A=0: pointer low byte', align=Align.INLINE)
d.comment(0xBC60, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xBC62, 'Restore data byte', align=Align.INLINE)
d.comment(0xBC63, 'Write data byte to buffer', align=Align.INLINE)
d.comment(0xBC65, 'Increment byte count for this FCB', align=Align.INLINE)
d.comment(0xBC68, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xBC6A, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0xBC6D, "Restore caller's X", align=Align.INLINE)
d.comment(0xBC6E, 'X restored', align=Align.INLINE)
d.comment(0xBC6F, 'Discard saved data byte', align=Align.INLINE)
d.comment(0xBC70, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xBC73, 'Return', align=Align.INLINE)
d.comment(0xBC74, 'Save A', align=Align.INLINE)
d.comment(0xBC75, 'Save X', align=Align.INLINE)
d.comment(0xBC77, 'Read FCB slot attribute byte', align=Align.INLINE)
d.comment(0xBC7A, 'Non-zero: station known -> store_station_and_flush', align=Align.INLINE)
d.comment(0xBC7C, 'Save attribute byte (saved-station-test path)', align=Align.INLINE)
d.comment(0xBC7D, 'Save X again', align=Align.INLINE)
d.comment(0xBC7E, 'Save Y', align=Align.INLINE)
d.comment(0xBCBA, 'Restore A', align=Align.INLINE)
d.comment(0xBCBB, 'Return', align=Align.INLINE)
d.comment(0xBCBC, 'Store reply port', align=Align.INLINE)
d.comment(0xBCBF, 'Store data byte', align=Align.INLINE)
d.comment(0xBCC2, 'Save Y', align=Align.INLINE)
d.comment(0xBCC3, 'Push Y to stack', align=Align.INLINE)
d.comment(0xBCC4, 'Save X', align=Align.INLINE)
d.comment(0xBCC5, 'Push X to stack', align=Align.INLINE)
d.comment(0xBCC6, 'Function code &90', align=Align.INLINE)
d.comment(0xBCC8, 'Store in send buffer', align=Align.INLINE)
d.comment(0xBCCB, 'Initialise TX control block', align=Align.INLINE)
d.comment(0xBCCE, 'TX start address low = &DC', align=Align.INLINE)
d.comment(0xBCD0, 'Set TX start in control block', align=Align.INLINE)
d.comment(0xBCD2, 'TX end address low = &E0', align=Align.INLINE)
d.comment(0xBCD4, 'Set TX end in control block', align=Align.INLINE)
d.comment(0xBCD6, 'Expected reply port = 9', align=Align.INLINE)
d.comment(0xBCD8, 'Store reply port in buffer', align=Align.INLINE)
d.comment(0xBCDB, 'TX control = &C0', align=Align.INLINE)
d.comment(0xBCDD, 'Y=0: no timeout', align=Align.INLINE)
d.comment(0xBCDF, 'Load reply port for addressing', align=Align.INLINE)
d.comment(0xBCE2, 'Send packet to server', align=Align.INLINE)
d.comment(0xBCE5, 'Load reply status', align=Align.INLINE)
d.comment(0xBCE8, 'Zero: success', align=Align.INLINE)
d.comment(0xBCEA, 'Store error code', align=Align.INLINE)
d.comment(0xBCED, 'X=0: copy index', align=Align.INLINE)
d.comment(0xBCEF, 'Load error message byte', align=Align.INLINE)
d.comment(0xBCF2, 'Copy to error block', align=Align.INLINE)
d.comment(0xBCF5, 'Is it CR (end of message)?', align=Align.INLINE)
d.comment(0xBCF7, 'Yes: terminate string', align=Align.INLINE)
d.comment(0xBCF9, 'Next byte', align=Align.INLINE)
d.comment(0xBCFA, 'Continue copying error message', align=Align.INLINE)
d.comment(0xBCFC, 'NUL terminator', align=Align.INLINE)
d.comment(0xBCFE, 'Terminate error string in block', align=Align.INLINE)
d.comment(0xBD01, 'Back up position for error check', align=Align.INLINE)
d.comment(0xBD02, 'Process and raise network error', align=Align.INLINE)
d.comment(0xBD05, 'Load channel attribute index', align=Align.INLINE)
d.comment(0xBD08, 'Load station number for channel', align=Align.INLINE)
d.comment(0xBD0B, 'Toggle bit 0 (alternate station)', align=Align.INLINE)
d.comment(0xBD0D, 'Update station number', align=Align.INLINE)
d.comment(0xBD10, 'Restore X', align=Align.INLINE)
d.comment(0xBD11, 'X restored', align=Align.INLINE)
d.comment(0xBD12, 'Restore Y', align=Align.INLINE)
d.comment(0xBD13, 'Y restored', align=Align.INLINE)
d.comment(0xBD14, 'Return', align=Align.INLINE)
d.comment(0xBD15, 'Set up FS options pointer', align=Align.INLINE)
d.comment(0xBD18, 'Set up transfer workspace and return', align=Align.INLINE)
d.comment(0xBD1B, 'Y=&0A: receive attribute offset', align=Align.INLINE)
d.comment(0xBD1D, 'Read byte from receive buffer', align=Align.INLINE)
d.comment(0xBD1F, 'Return', align=Align.INLINE)
d.comment(0xBD20, 'Y=&0A: receive attribute offset', align=Align.INLINE)
d.comment(0xBD22, 'Store byte to receive buffer', align=Align.INLINE)
d.comment(0xBD24, 'Return', align=Align.INLINE)
d.comment(0xBD44, '21 bytes to push (0-&14)', align=Align.INLINE)
d.comment(0xBD4D, 'Set up buffer pointer and parse args', align=Align.INLINE)
d.comment(0xBD54, 'Skip header if 16-byte aligned', align=Align.INLINE)
d.comment(0xBD56, 'Print column header for offset start', align=Align.INLINE)
d.comment(0xBD86, 'Non-zero: header already current', align=Align.INLINE)
d.comment(0xBD9B, 'Add 16 to lowest address byte', align=Align.INLINE)
d.comment(0xBDAC, 'Print address/data separator', align=Align.INLINE)
d.comment(0xBDB4, 'X = bytes read (counter for display)', align=Align.INLINE)
d.comment(0xBDC0, 'Decrement remaining data bytes', align=Align.INLINE)
d.comment(0xBE42, 'Save command line offset to X', align=Align.INLINE)
d.comment(0xBE43, 'X tracks current position', align=Align.INLINE)
d.comment(0xBE61, 'Yes: is a decimal digit', align=Align.INLINE)
d.comment(0xBE65, "Map 'A'-'F' → &FA-&FF (C=0 here)", align=Align.INLINE)
d.comment(0xBE67, "Carry set: char > 'F', error", align=Align.INLINE)
d.comment(0xBE69, "Below &FA? (i.e. was < 'A')", align=Align.INLINE)
d.comment(0xBE71, 'Preserve on stack', align=Align.INLINE)
d.comment(0xBE72, '4 bits to shift in', align=Align.INLINE)
d.comment(0xBE77, 'Transfer carry bit to flags via stack', align=Align.INLINE)
d.comment(0xBE78, 'C = bit shifted out of prev iter', align=Align.INLINE)
d.comment(0xBE7B, 'Rotate left through carry', align=Align.INLINE)
d.comment(0xBE86, 'C = overflow bit', align=Align.INLINE)
d.comment(0xBE87, 'Overflow: address too large', align=Align.INLINE)
d.comment(0xBE9C, 'Close open file before error', align=Align.INLINE)
d.comment(0xBEAB, 'X+1: first byte of buffer', align=Align.INLINE)
d.comment(0xBEAE, 'Buffer is on stack in page 1', align=Align.INLINE)
d.comment(0xBEB2, 'Parse start offset from command line', align=Align.INLINE)
d.comment(0xBEB7, 'A = command line offset after parse', align=Align.INLINE)
d.comment(0xBEBD, 'A=2: read file extent (length)', align=Align.INLINE)
d.comment(0xBEC7, 'Compare with start offset byte', align=Align.INLINE)
d.comment(0xBECC, 'More bytes to compare', align=Align.INLINE)
d.comment(0xBECE, 'All equal: start = length, within file', align=Align.INLINE)
d.comment(0xBED0, 'Length < start: outside file', align=Align.INLINE)
d.comment(0xBED2, 'Y=&FF: length > start, flag for later', align=Align.INLINE)
d.comment(0xBED4, 'Continue to copy start address', align=Align.INLINE)
d.comment(0xBEEB, 'Load start address byte from buffer', align=Align.INLINE)
d.comment(0xBEF9, 'A=1: write file pointer', align=Align.INLINE)
d.comment(0xBEFB, 'OSARGS: set file pointer', align=Align.INLINE)
d.comment(0xBF06, 'Copy 2 bytes: os_text_ptr to buffer', align=Align.INLINE)
d.comment(0xBF19, 'Start at OSFILE +2 (load addr byte 0)', align=Align.INLINE)
d.comment(0xBF1E, 'Continue decrement', align=Align.INLINE)
d.comment(0xBF28, 'Y=6 after loop exit', align=Align.INLINE)
d.comment(0xBF29, 'Y=4: check from buf[4] downward', align=Align.INLINE)
d.comment(0xBF2E, 'No: valid load address, use it', align=Align.INLINE)
d.comment(0xBF33, 'Clear all 4 bytes', align=Align.INLINE)
d.comment(0xBF3C, 'Continue to compute display address', align=Align.INLINE)
d.comment(0xBF43, 'Invalid: close file before error', align=Align.INLINE)
d.comment(0xBF5A, 'Add start offset byte', align=Align.INLINE)
d.comment(0xBF64, 'Point past end of address area', align=Align.INLINE)
d.comment(0xBF79, 'A=filename offset from Y', align=Align.INLINE)
d.comment(0xBF7B, 'Add text pointer low byte', align=Align.INLINE)
d.comment(0xBF7D, 'Save filename address low', align=Align.INLINE)
d.comment(0xBF7E, 'X=filename address low (for OSFIND)', align=Align.INLINE)
d.comment(0xBF81, 'Add text pointer high byte + carry', align=Align.INLINE)
d.comment(0xBF91, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0xBF9E, 'Restore text pointer high from stack', align=Align.INLINE)
d.comment(0xBFA1, 'Restore text pointer low from stack', align=Align.INLINE)
d.comment(0xBFAB, 'Yes: finished parsing filename', align=Align.INLINE)
d.comment(0xBFB8, 'Restore caller flags', align=Align.INLINE)
d.comment(0xBFBA, 'JSR+fall-through: 8+8=16 INXs total', align=Align.INLINE)
d.comment(0xBFBD, 'JSR+fall-through: 4+4=8 INXs', align=Align.INLINE)
d.comment(0xBFC0, 'X += 4', align=Align.INLINE)
d.comment(0xBFC4, 'Return', align=Align.INLINE)
d.comment(0xBFC7, 'Padding; next byte is reloc_p5_src', align=Align.INLINE)
d.comment(0x9100, 'Syn 2: *I Am (login)', align=Align.INLINE)
d.comment(0x912D, 'Syn 3: *Delete, *FS, *Remove', align=Align.INLINE)
d.comment(0x9184, 'Syn 7 continued: new password', align=Align.INLINE)
d.comment(0x91AA, 'Syn 9: *Access', align=Align.INLINE)
d.comment(0x91C5, 'Null terminator', align=Align.INLINE)
d.comment(0x91C6, 'Syn 10: *Rename', align=Align.INLINE)
d.comment(0x91EC, 'Null terminator', align=Align.INLINE)
d.comment(0x91ED, "Idx 0: 'opt_dir' (offset -2 variant for *Dir's INY-twice walker)", align=Align.INLINE)
d.comment(0x91EE, 'Idx 1: &FF = no syntax string for this index', align=Align.INLINE)
d.comment(0x91EF, 'Idx 2: \\"(<stn.id.>) <user id.>...\\"', align=Align.INLINE)
d.comment(0x91F0, 'Idx 3: \\"<object>\\"', align=Align.INLINE)
d.comment(0x91F1, 'Idx 4: \\"<filename> (<offset>...)\\"', align=Align.INLINE)
d.comment(0x91F2, "Idx 5: '<dir>' (offset 0x60 = syn_dir)", align=Align.INLINE)
d.comment(0x91F3, 'Idx 6: continued <dir> string region', align=Align.INLINE)
d.comment(0x91F4, 'Idx 7: \\"(:<CR>) <password>...\\"', align=Align.INLINE)
d.comment(0x91F5, 'Idx 8: \\"(<stn.id.>|<ps type>)\\"', align=Align.INLINE)
d.comment(0x91F6, 'Idx 9: \\"<object> (L)(W)(R)...\\"', align=Align.INLINE)
d.comment(0x91F7, "Idx 10: '<filename> <new filename>' (syn_rename)", align=Align.INLINE)
d.comment(0x91F8, 'Idx 11: \\"(<stn. id.>)\\"', align=Align.INLINE)
d.comment(0x94C5, "Copy 'Rename ' to TX buffer", align=Align.INLINE)
d.comment(0x986B, 'Y=&0E', align=Align.INLINE)
d.comment(0x99C5, 'Store return address low', align=Align.INLINE)
d.comment(0x99C8, 'Store return address high', align=Align.INLINE)
d.comment(0x99CA, 'X=0: error text index', align=Align.INLINE)
d.comment(0x99CF, 'Copy error number to A', align=Align.INLINE)
d.comment(0x99D0, 'Push error number on stack', align=Align.INLINE)
d.comment(0x99D1, 'Y=0: inline string index', align=Align.INLINE)
d.comment(0x99D7, 'Advance string index', align=Align.INLINE)
d.comment(0x99DA, 'Store byte in error block', align=Align.INLINE)
d.comment(0x99E2, 'Non-zero: network returned an error', align=Align.INLINE)
d.comment(0x99E4, 'Pop saved error number', align=Align.INLINE)
d.comment(0x99E5, 'Was it &DE (file server error)?', align=Align.INLINE)
d.comment(0x99E7, 'Yes: append error number and trigger BRK', align=Align.INLINE)
d.comment(0x99E9, 'Jump to BRK via error block', align=Align.INLINE)
d.comment(0x99EC, 'Store error code in workspace', align=Align.INLINE)
d.comment(0x99EF, 'Push error code', align=Align.INLINE)
d.comment(0x99F0, 'Save X (error text index)', align=Align.INLINE)
d.comment(0x99F1, 'Push X', align=Align.INLINE)
d.comment(0x99F2, 'Read receive attribute byte', align=Align.INLINE)
d.comment(0x99F5, 'Save to fs_load_addr as spool handle', align=Align.INLINE)
d.comment(0x99F7, 'A=0: clear error code in RX buffer', align=Align.INLINE)
d.comment(0x99F9, 'Zero the error code byte in buffer', align=Align.INLINE)
d.comment(0x99FB, 'A=&C6: OSBYTE read spool handle', align=Align.INLINE)
d.comment(0x99FD, 'Read current spool file handle', align=Align.INLINE)
d.comment(0x9A00, 'Compare Y result with saved handle', align=Align.INLINE)
d.comment(0x9A02, 'Match: close the spool file', align=Align.INLINE)
d.comment(0x9A04, 'Compare X result with saved handle', align=Align.INLINE)
d.comment(0x9A06, 'No match: skip spool close', align=Align.INLINE)
d.comment(0x9A08, 'Push A (preserved)', align=Align.INLINE)
d.comment(0x9A09, 'A=&C6: disable spool with OSBYTE', align=Align.INLINE)
d.comment(0x9A0B, 'ALWAYS branch to close spool', align=Align.INLINE)
d.comment(0x9A14, 'A=0: close file', align=Align.INLINE)
d.comment(0x9A16, 'Close the spool/exec file', align=Align.INLINE)
d.comment(0x9A19, 'Pull saved X (error text index)', align=Align.INLINE)
d.comment(0x9A1A, 'Restore X', align=Align.INLINE)
d.comment(0x9A1B, "Y=&0A: lookup index for 'on channel'", align=Align.INLINE)
d.comment(0x9A1D, 'Load message offset from lookup table', align=Align.INLINE)
d.comment(0x9A20, 'Transfer offset to Y', align=Align.INLINE)
d.comment(0x9A21, 'Load error message byte', align=Align.INLINE)
d.comment(0x9A24, 'Append to error text buffer', align=Align.INLINE)
d.comment(0x9A27, 'Null terminator: done copying', align=Align.INLINE)
d.comment(0x9A29, 'Advance error text index', align=Align.INLINE)
d.comment(0x9A2A, 'Advance message index', align=Align.INLINE)
d.comment(0x9A2B, 'Loop until full message copied', align=Align.INLINE)
d.comment(0x9A2D, 'Save error text end position', align=Align.INLINE)
d.comment(0x9A2F, 'Pull saved error number', align=Align.INLINE)
d.comment(0x9A30, "Append ' nnn' error number suffix", align=Align.INLINE)
d.comment(0x9A33, 'A=0: null terminator', align=Align.INLINE)
d.comment(0x9A35, 'Terminate error text string', align=Align.INLINE)
d.comment(0x9A38, 'ALWAYS branch to trigger BRK error', align=Align.INLINE)
d.comment(0x9A3A, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9A3C, 'Append space to error text', align=Align.INLINE)
d.comment(0x9A3F, 'Advance error text index', align=Align.INLINE)
d.comment(0x9A40, 'Save position for number formatting', align=Align.INLINE)
d.comment(0x9A42, 'Y=3: offset to network number in TX CB', align=Align.INLINE)
d.comment(0x9A44, 'Load network number', align=Align.INLINE)
d.comment(0x9A46, 'Zero: skip network part (local)', align=Align.INLINE)
d.comment(0x9A48, 'Append network number as decimal', align=Align.INLINE)
d.comment(0x9A4B, 'Reload error text position', align=Align.INLINE)
d.comment(0x9A4D, "A='.': dot separator", align=Align.INLINE)
d.comment(0x9A4F, 'Append dot to error text', align=Align.INLINE)
d.comment(0x9A52, 'Advance past dot', align=Align.INLINE)
d.comment(0x9A54, 'Y=2: offset to station number in TX CB', align=Align.INLINE)
d.comment(0x9A56, 'Load station number', align=Align.INLINE)
d.comment(0x9A58, 'Append station number as decimal', align=Align.INLINE)
d.comment(0x9A5B, 'Reload error text position', align=Align.INLINE)
d.comment(0x9A5D, 'Return', align=Align.INLINE)
d.comment(0x9A5E, 'Save number in Y', align=Align.INLINE)
d.comment(0x9A5F, "A=' ': space prefix", align=Align.INLINE)
d.comment(0x9A61, 'Load current error text position', align=Align.INLINE)
d.comment(0x9A63, 'Append space to error text', align=Align.INLINE)
d.comment(0x9A66, 'Advance position past space', align=Align.INLINE)
d.comment(0x9A68, 'Restore number to A', align=Align.INLINE)
d.comment(0x9A69, 'Save number in Y for division', align=Align.INLINE)
d.comment(0x9A6A, 'Set V: suppress leading zeros', align=Align.INLINE)
d.comment(0x9A6D, 'A=100: hundreds digit divisor', align=Align.INLINE)
d.comment(0x9A6F, 'Extract and append hundreds digit', align=Align.INLINE)
d.comment(0x9A72, 'A=10: tens digit divisor', align=Align.INLINE)
d.comment(0x9A74, 'Extract and append tens digit', align=Align.INLINE)
d.comment(0x9A77, 'A=1: units digit (remainder)', align=Align.INLINE)
d.comment(0x9A79, 'Clear V: always print units digit', align=Align.INLINE)
d.comment(0x9A7A, 'Store divisor', align=Align.INLINE)
d.comment(0x9A7C, 'Copy number to A for division', align=Align.INLINE)
d.comment(0x9A7D, "X='0'-1: digit counter (ASCII offset)", align=Align.INLINE)
d.comment(0x9A7F, 'Save V flag (leading zero suppression)', align=Align.INLINE)
d.comment(0x9A80, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9A81, 'Increment digit counter', align=Align.INLINE)
d.comment(0x9A82, 'Subtract divisor', align=Align.INLINE)
d.comment(0x9A84, 'Not negative yet: continue counting', align=Align.INLINE)
d.comment(0x9A86, 'Add back divisor (restore remainder)', align=Align.INLINE)
d.comment(0x9A88, 'Restore V flag', align=Align.INLINE)
d.comment(0x9A89, 'Save remainder back to Y', align=Align.INLINE)
d.comment(0x9A8A, 'Digit counter to A (ASCII digit)', align=Align.INLINE)
d.comment(0x9A8B, "Is digit '0'?", align=Align.INLINE)
d.comment(0x9A8D, 'Non-zero: always print', align=Align.INLINE)
d.comment(0x9A8F, 'V set (suppress leading zeros): skip', align=Align.INLINE)
d.comment(0x9A91, 'Clear V: first non-zero digit seen', align=Align.INLINE)
d.comment(0x9A92, 'Load current text position', align=Align.INLINE)
d.comment(0x9A94, 'Store ASCII digit in error text', align=Align.INLINE)
d.comment(0x9A97, 'Advance text position', align=Align.INLINE)
d.comment(0x9A99, 'Return', align=Align.INLINE)
d.comment(0x9AB2, 'Null terminator', align=Align.INLINE)
d.comment(0x9AB3, 'Error &A1: Net error', align=Align.INLINE)
d.comment(0x9ABD, 'Null terminator', align=Align.INLINE)
d.comment(0x9ABE, 'Error &A2: Station', align=Align.INLINE)
d.comment(0x9AD0, 'Null terminator', align=Align.INLINE)
d.comment(0x9AD1, 'Error &11: Escape', align=Align.INLINE)
d.comment(0x9AD9, 'Error &CB: Bad option', align=Align.INLINE)
d.comment(0x9AE4, 'Null terminator + Error &A5: No reply from station', align=Align.INLINE)
d.comment(0x9AE6, 'err_no_reply = &A5 message body', align=Align.INLINE)
d.comment(0x9AFB, 'Null terminator', align=Align.INLINE)
d.comment(0x9AFC, 'Suffix string (offset &56 in lookup)', align=Align.INLINE)
d.comment(0x9B0A, 'Null terminator', align=Align.INLINE)
d.comment(0x9B0B, 'Suffix: \\" on channel\\"', align=Align.INLINE)
d.comment(0x9B16, 'Null terminator', align=Align.INLINE)
d.comment(0x9B17, 'Suffix: \\" not present\\"', align=Align.INLINE)
d.comment(0x9B23, 'Null terminator', align=Align.INLINE)
d.comment(0x9B24, 'X=&C0: TX control block base (low)', align=Align.INLINE)
d.comment(0x9B26, 'Set TX pointer low', align=Align.INLINE)
d.comment(0x9B28, 'X=0: TX control block base (high)', align=Align.INLINE)
d.comment(0x9B2A, 'Set TX pointer high (page 0)', align=Align.INLINE)
d.comment(0x9B2C, 'Load retry count from workspace', align=Align.INLINE)
d.comment(0x9B2F, 'Non-zero: use configured retry count', align=Align.INLINE)
d.comment(0x9B31, 'A=&FF: default retry count (255)', align=Align.INLINE)
d.comment(0x9B33, 'Y=&60: timeout value', align=Align.INLINE)
d.comment(0x9B35, 'Push retry count', align=Align.INLINE)
d.comment(0x9B36, 'A=&60: copy timeout to A', align=Align.INLINE)
d.comment(0x9B37, 'Push timeout', align=Align.INLINE)
d.comment(0x9B38, 'X=0: TX pointer index', align=Align.INLINE)
d.comment(0x9B3A, 'Load first byte of TX control block', align=Align.INLINE)
d.comment(0x9B3C, 'Restore control byte (overwritten by result code on retry)', align=Align.INLINE)
d.comment(0x9B3E, 'Push control byte', align=Align.INLINE)
d.comment(0x9B3F, 'Poll ADLC until line idle', align=Align.INLINE)
d.comment(0x9B42, 'Bit 6 (error flag) into N', align=Align.INLINE)
d.comment(0x9B43, 'N=0 (bit 6 clear): success', align=Align.INLINE)
d.comment(0x9B45, 'Shift away error flag, keep error type', align=Align.INLINE)
d.comment(0x9B46, 'Z=1 (no type bits): fatal; Z=0: retryable', align=Align.INLINE)
d.comment(0x9B48, 'Check for escape condition', align=Align.INLINE)
d.comment(0x9B4B, 'Pull control byte', align=Align.INLINE)
d.comment(0x9B4C, 'Restore to X', align=Align.INLINE)
d.comment(0x9B4D, 'Pull timeout', align=Align.INLINE)
d.comment(0x9B4E, 'Restore to Y', align=Align.INLINE)
d.comment(0x9B4F, 'Pull retry count', align=Align.INLINE)
d.comment(0x9B50, 'Zero retries remaining: try alternate', align=Align.INLINE)
d.comment(0x9B52, 'Decrement retry counter', align=Align.INLINE)
d.comment(0x9B54, 'Push updated retry count', align=Align.INLINE)
d.comment(0x9B55, 'Copy timeout to A', align=Align.INLINE)
d.comment(0x9B56, 'Push timeout for delay loop', align=Align.INLINE)
d.comment(0x9B57, 'Copy control byte to A', align=Align.INLINE)
d.comment(0x9B58, 'Inner delay: decrement X', align=Align.INLINE)
d.comment(0x9B59, 'Loop until X=0', align=Align.INLINE)
d.comment(0x9B5B, 'Decrement outer counter Y', align=Align.INLINE)
d.comment(0x9B5C, 'Loop until Y=0', align=Align.INLINE)
d.comment(0x9B5E, 'ALWAYS branch: retry transmission', align=Align.INLINE)
d.comment(0x9B60, 'Compare retry count with alternate', align=Align.INLINE)
d.comment(0x9B63, 'Different: go to error handling', align=Align.INLINE)
d.comment(0x9B65, 'A=&80: set escapable flag', align=Align.INLINE)
d.comment(0x9B67, 'Mark as escapable for second phase', align=Align.INLINE)
d.comment(0x9B69, 'ALWAYS branch: retry with escapable', align=Align.INLINE)
d.comment(0x9B6B, 'Result code to X', align=Align.INLINE)
d.comment(0x9B6C, 'Jump to classify reply and return', align=Align.INLINE)
d.comment(0x9B6F, 'Pull control byte', align=Align.INLINE)
d.comment(0x9B70, 'Pull timeout', align=Align.INLINE)
d.comment(0x9B71, 'Pull retry count', align=Align.INLINE)
d.comment(0x9B72, 'Clear escapable flag and return', align=Align.INLINE)
d.comment(0x9B75, 'Offset 0: ctrl = &88 (immediate TX)', align=Align.INLINE)
d.comment(0x9B76, 'Offset 1: port = &00 (immediate op)', align=Align.INLINE)
d.comment(0x9B77, 'Offset 2: &FD skip (preserve dest stn)', align=Align.INLINE)
d.comment(0x9B78, 'Offset 3: &FD skip (preserve dest net)', align=Align.INLINE)
d.comment(0x9B79, 'Offset 4: buf start lo (&3A) -> &0D3A', align=Align.INLINE)
d.comment(0x9B7A, 'Offset 5: buf start hi (&0D) -> &0D3A', align=Align.INLINE)
d.comment(0x9B7B, 'Offset 6: extended-addr fill (&FF)', align=Align.INLINE)
d.comment(0x9B7C, 'Offset 7: extended-addr fill (&FF)', align=Align.INLINE)
d.comment(0x9B7D, 'Offset 8: buf end lo (&3E) -> &0D3E', align=Align.INLINE)
d.comment(0x9B7E, 'Offset 9: buf end hi (&0D) -> &0D3E', align=Align.INLINE)
d.comment(0x9B7F, 'Offset 10: extended-addr fill (&FF)', align=Align.INLINE)
d.comment(0x9B80, 'Offset 11: extended-addr fill (&FF)', align=Align.INLINE)
d.comment(0x9B81, 'Y=&C0: TX control block base (low)', align=Align.INLINE)
d.comment(0x9B83, 'Set TX pointer low byte', align=Align.INLINE)
d.comment(0x9B85, 'Y=0: TX control block base (high)', align=Align.INLINE)
d.comment(0x9B87, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0x9B89, 'Y=&0B: 12 bytes to process (0-11)', align=Align.INLINE)
d.comment(0x9B8B, 'Load template byte for this offset', align=Align.INLINE)
d.comment(0x9B8E, 'Is it &FD (skip marker)?', align=Align.INLINE)
d.comment(0x9B90, "Yes: skip this offset, don't modify", align=Align.INLINE)
d.comment(0x9B92, 'Load existing TX buffer byte', align=Align.INLINE)
d.comment(0x9B94, 'Save original value on stack', align=Align.INLINE)
d.comment(0x9B95, 'Copy template value to A', align=Align.INLINE)
d.comment(0x9B96, 'Store template value to TX buffer', align=Align.INLINE)
d.comment(0x9B98, 'Next offset (descending)', align=Align.INLINE)
d.comment(0x9B99, 'Loop until all 12 bytes processed', align=Align.INLINE)
d.comment(0x9B9B, 'Load pass-through control value', align=Align.INLINE)
d.comment(0x9B9E, 'Push control value', align=Align.INLINE)
d.comment(0x9B9F, 'A=&FF (Y is &FF after loop)', align=Align.INLINE)
d.comment(0x9BA0, 'Push &FF as timeout', align=Align.INLINE)
d.comment(0x9BA1, 'X=0: TX pointer index', align=Align.INLINE)
d.comment(0x9BA3, 'Load control byte from TX CB', align=Align.INLINE)
d.comment(0x9BA5, 'Write control byte to start TX', align=Align.INLINE)
d.comment(0x9BA7, 'Save control byte on stack', align=Align.INLINE)
d.comment(0x9BA8, 'Poll ADLC until line idle', align=Align.INLINE)
d.comment(0x9BAB, 'Shift result: check bit 6 (success)', align=Align.INLINE)
d.comment(0x9BAC, 'Bit 6 clear: transmission complete', align=Align.INLINE)
d.comment(0x9BAE, 'Shift result: check bit 5 (fatal)', align=Align.INLINE)
d.comment(0x9BAF, 'Non-zero (not fatal): retry', align=Align.INLINE)
d.comment(0x9BB1, 'X=0: clear error status', align=Align.INLINE)
d.comment(0x9BB3, 'Jump to fix up reply status', align=Align.INLINE)
d.comment(0x9BB6, 'Shift ws_0d60 left to poll ADLC', align=Align.INLINE)
d.comment(0x9BB9, 'Bit not set: keep polling', align=Align.INLINE)
d.comment(0x9BBB, 'Copy TX pointer low to NMI TX block', align=Align.INLINE)
d.comment(0x9BBD, 'Store in NMI TX block low', align=Align.INLINE)
d.comment(0x9BBF, 'Copy TX pointer high', align=Align.INLINE)
d.comment(0x9BC1, 'Store in NMI TX block high', align=Align.INLINE)
d.comment(0x9BC3, 'Begin Econet frame transmission', align=Align.INLINE)
d.comment(0x9BC6, 'Read TX status byte', align=Align.INLINE)
d.comment(0x9BC8, 'Bit 7 set: still transmitting', align=Align.INLINE)
d.comment(0x9BCA, 'Return with result in A', align=Align.INLINE)
d.comment(0x9BCB, 'Pull control byte', align=Align.INLINE)
d.comment(0x9BCC, 'Restore to X', align=Align.INLINE)
d.comment(0x9BCD, 'Pull timeout', align=Align.INLINE)
d.comment(0x9BCE, 'Restore to Y', align=Align.INLINE)
d.comment(0x9BCF, 'Pull retry count', align=Align.INLINE)
d.comment(0x9BD0, 'Zero retries: go to error handling', align=Align.INLINE)
d.comment(0x9BD2, 'Decrement retry counter', align=Align.INLINE)
d.comment(0x9BD4, 'Push updated retry count', align=Align.INLINE)
d.comment(0x9BD5, 'Copy timeout to A', align=Align.INLINE)
d.comment(0x9BD6, 'Push timeout', align=Align.INLINE)
d.comment(0x9BD7, 'Copy control byte to A', align=Align.INLINE)
d.comment(0x9BD8, 'Inner delay loop: decrement X', align=Align.INLINE)
d.comment(0x9BD9, 'Loop until X=0', align=Align.INLINE)
d.comment(0x9BDB, 'Decrement outer counter Y', align=Align.INLINE)
d.comment(0x9BDC, 'Loop until Y=0', align=Align.INLINE)
d.comment(0x9BDE, 'ALWAYS branch: retry transmission', align=Align.INLINE)
d.comment(0x9BE0, 'Pull control byte (discard)', align=Align.INLINE)
d.comment(0x9BE1, 'Pull timeout (discard)', align=Align.INLINE)
d.comment(0x9BE2, 'Pull retry count (discard)', align=Align.INLINE)
d.comment(0x9BE3, 'Y=0: start restoring from offset 0', align=Align.INLINE)
d.comment(0x9BE5, 'Load template byte for this offset', align=Align.INLINE)
d.comment(0x9BE8, 'Is it &FD (skip marker)?', align=Align.INLINE)
d.comment(0x9BEA, "Yes: don't restore this offset", align=Align.INLINE)
d.comment(0x9BEC, 'Pull original value from stack', align=Align.INLINE)
d.comment(0x9BED, 'Restore original TX buffer byte', align=Align.INLINE)
d.comment(0x9BEF, 'Next offset (ascending)', align=Align.INLINE)
d.comment(0x9BF0, 'Processed all 12 bytes?', align=Align.INLINE)
d.comment(0x9BF2, 'No: continue restoring', align=Align.INLINE)
d.comment(0x9BF4, 'Return with TX buffer restored', align=Align.INLINE)
d.comment(0x9BF5, 'Y=1: start at second byte of pointer', align=Align.INLINE)
d.comment(0x9BF7, 'Load pointer byte from FS options', align=Align.INLINE)
d.comment(0x9BF9, 'Store in OS text pointer', align=Align.INLINE)
d.comment(0x9BFC, 'Decrement index', align=Align.INLINE)
d.comment(0x9BFD, 'Loop until both bytes copied', align=Align.INLINE)
d.comment(0x9BFF, 'Y=0: reset index for string reading', align=Align.INLINE)
d.comment(0x9C00, 'X=&FF: pre-increment for buffer index', align=Align.INLINE)
d.comment(0x9C02, 'C=0: initialise for string input', align=Align.INLINE)
d.comment(0x9C03, 'GSINIT: initialise string reading', align=Align.INLINE)
d.comment(0x9C06, 'Z set (empty string): store terminator', align=Align.INLINE)
d.comment(0x9C08, 'GSREAD: read next character', align=Align.INLINE)
d.comment(0x9C0B, 'C set: end of string reached', align=Align.INLINE)
d.comment(0x9C0D, 'Advance buffer index', align=Align.INLINE)
d.comment(0x9C0E, 'Store character in fs_filename_buf buffer', align=Align.INLINE)
d.comment(0x9C11, 'ALWAYS branch: read next character', align=Align.INLINE)
d.comment(0x9C13, 'Advance past last character', align=Align.INLINE)
d.comment(0x9C14, 'A=CR: terminate filename', align=Align.INLINE)
d.comment(0x9C16, 'Store CR terminator in buffer', align=Align.INLINE)
d.comment(0x9C19, 'A=&30: low byte of fs_filename_buf buffer', align=Align.INLINE)
d.comment(0x9C1B, 'Set command text pointer low', align=Align.INLINE)
d.comment(0x9C1D, 'A=&0E: high byte of fs_filename_buf buffer', align=Align.INLINE)
d.comment(0x9C1F, 'Set command text pointer high', align=Align.INLINE)
d.comment(0x9C21, 'Return with buffer filled', align=Align.INLINE)
d.comment(0x9C22, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9C25, 'Load text pointer and parse filename', align=Align.INLINE)
d.comment(0x9C28, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x9C2B, 'Parse access prefix from filename', align=Align.INLINE)
d.comment(0x9C2E, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9C30, 'Positive (not last): display file info', align=Align.INLINE)
d.comment(0x9C32, 'Is it &FF (last entry)?', align=Align.INLINE)
d.comment(0x9C34, 'Yes: copy arg and iterate', align=Align.INLINE)
d.comment(0x9C36, 'Other value: return with flag', align=Align.INLINE)
d.comment(0x9C39, 'Copy argument to buffer at X=0', align=Align.INLINE)
d.comment(0x9C3C, 'Y=2: enumerate directory command', align=Align.INLINE)
d.comment(0x9C3E, 'A=&92: FS port number', align=Align.INLINE)
d.comment(0x9C40, 'Set escapable flag to &92', align=Align.INLINE)
d.comment(0x9C42, 'Store port number in TX buffer', align=Align.INLINE)
d.comment(0x9C45, 'Send request to file server', align=Align.INLINE)
d.comment(0x9C48, 'Y=6: offset to response cycle flag', align=Align.INLINE)
d.comment(0x9C4A, 'Load cycle flag from FS options', align=Align.INLINE)
d.comment(0x9C4C, 'Non-zero: already initialised', align=Align.INLINE)
d.comment(0x9C4E, 'Copy FS options to zero page first', align=Align.INLINE)
d.comment(0x9C51, 'Then copy workspace to FS options', align=Align.INLINE)
d.comment(0x9C54, 'Branch to continue (C clear from JSR)', align=Align.INLINE)
d.comment(0x9C56, 'Copy workspace to FS options first', align=Align.INLINE)
d.comment(0x9C59, 'Then copy FS options to zero page', align=Align.INLINE)
d.comment(0x9C5C, 'Y=4: loop counter', align=Align.INLINE)
d.comment(0x9C5E, 'Load address byte from zero page', align=Align.INLINE)
d.comment(0x9C60, 'Save to TXCB end pointer', align=Align.INLINE)
d.comment(0x9C62, 'Add offset from buffer', align=Align.INLINE)
d.comment(0x9C65, 'Store sum in fs_work area', align=Align.INLINE)
d.comment(0x9C67, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9C68, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C69, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9C6B, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9C6C, 'Subtract high offset', align=Align.INLINE)
d.comment(0x9C6F, 'Store result in fs_work_7', align=Align.INLINE)
d.comment(0x9C71, 'Format filename for display', align=Align.INLINE)
d.comment(0x9C74, 'Send TXCB and swap addresses', align=Align.INLINE)
d.comment(0x9C77, 'X=2: copy 3 offset bytes', align=Align.INLINE)
d.comment(0x9C79, 'Load offset byte from fs_file_len_3', align=Align.INLINE)
d.comment(0x9C7C, 'Store in fs_cmd_data for next iteration', align=Align.INLINE)
d.comment(0x9C7F, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C80, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9C82, 'Jump to receive and process reply', align=Align.INLINE)
d.comment(0x9C85, 'Compare 5-byte handle with current', align=Align.INLINE)
d.comment(0x9C88, 'Match: no need to send, return', align=Align.INLINE)
d.comment(0x9C8A, 'A=&92: FS reply port number', align=Align.INLINE)
d.comment(0x9C8C, 'Set TXCB port', align=Align.INLINE)
d.comment(0x9C8E, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9C90, 'Load TXCB end pointer byte', align=Align.INLINE)
d.comment(0x9C92, 'Store in TXCB start pointer', align=Align.INLINE)
d.comment(0x9C94, 'Load new end address from fs_work', align=Align.INLINE)
d.comment(0x9C96, 'Store in TXCB end pointer', align=Align.INLINE)
d.comment(0x9C98, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C99, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9C9B, 'A=&7F: control byte for data transfer', align=Align.INLINE)
d.comment(0x9C9D, 'Set TXCB control byte', align=Align.INLINE)
d.comment(0x9C9F, 'Wait for network TX acknowledgement', align=Align.INLINE)
d.comment(0x9CA2, 'Y=3: compare 4 bytes', align=Align.INLINE)
d.comment(0x9CA4, 'Load TXCB end byte', align=Align.INLINE)
d.comment(0x9CA7, 'Compare with expected end address', align=Align.INLINE)
d.comment(0x9CAA, 'Mismatch: resend from start', align=Align.INLINE)
d.comment(0x9CAC, 'Decrement counter', align=Align.INLINE)
d.comment(0x9CAD, 'Loop until all 4 bytes match', align=Align.INLINE)
d.comment(0x9CAF, 'Return (all bytes match)', align=Align.INLINE)
d.comment(0x9CB0, 'Z set: directory entry display', align=Align.INLINE)
d.comment(0x9CB2, 'Non-zero: jump to OSWORD dispatch', align=Align.INLINE)
d.comment(0x9CB5, 'X=4: loop counter for 4 iterations', align=Align.INLINE)
d.comment(0x9CB7, 'Y=&0E: FS options offset for addresses', align=Align.INLINE)
d.comment(0x9CB9, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9CBA, 'Load address byte from FS options', align=Align.INLINE)
d.comment(0x9CBC, 'Save to workspace (port_ws_offset)', align=Align.INLINE)
d.comment(0x9CBF, 'Y -= 4 to point to paired offset', align=Align.INLINE)
d.comment(0x9CC2, 'Subtract paired value', align=Align.INLINE)
d.comment(0x9CC4, 'Store difference in fs_cmd_csd buffer', align=Align.INLINE)
d.comment(0x9CC7, 'Push difference', align=Align.INLINE)
d.comment(0x9CC8, 'Load paired value from FS options', align=Align.INLINE)
d.comment(0x9CCA, 'Save to workspace', align=Align.INLINE)
d.comment(0x9CCD, 'Pull difference back', align=Align.INLINE)
d.comment(0x9CCE, 'Store in FS options for display', align=Align.INLINE)
d.comment(0x9CD0, 'Advance Y by 5 for next field', align=Align.INLINE)
d.comment(0x9CD3, 'Decrement loop counter', align=Align.INLINE)
d.comment(0x9CD4, 'Loop for all 4 address pairs', align=Align.INLINE)
d.comment(0x9CD6, 'Y=9: copy 9 bytes of options data', align=Align.INLINE)
d.comment(0x9CD8, 'Load FS options byte', align=Align.INLINE)
d.comment(0x9CDA, 'Store in fs_cmd_csd buffer', align=Align.INLINE)
d.comment(0x9CDD, 'Decrement index', align=Align.INLINE)
d.comment(0x9CDE, 'Loop until all 9 bytes copied', align=Align.INLINE)
d.comment(0x9CE0, 'A=&91: FS port for info request', align=Align.INLINE)
d.comment(0x9CE2, 'Set escapable flag', align=Align.INLINE)
d.comment(0x9CE4, 'Store port in TX buffer', align=Align.INLINE)
d.comment(0x9CE7, 'Store in fs_error_ptr', align=Align.INLINE)
d.comment(0x9CE9, 'X=&0B: copy argument at offset 11', align=Align.INLINE)
d.comment(0x9CEB, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0x9CEE, 'Y=1: info sub-command', align=Align.INLINE)
d.comment(0x9CF0, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9CF2, 'Is it 7 (catalogue info)?', align=Align.INLINE)
d.comment(0x9CF4, 'Save comparison result', align=Align.INLINE)
d.comment(0x9CF5, 'Not 7: keep Y=1', align=Align.INLINE)
d.comment(0x9CF7, 'Y=&1D: extended info command', align=Align.INLINE)
d.comment(0x9CF9, 'Send request to file server', align=Align.INLINE)
d.comment(0x9CFC, 'Format filename for display', align=Align.INLINE)
d.comment(0x9CFF, 'Restore comparison flags', align=Align.INLINE)
d.comment(0x9D00, 'Not catalogue info: show short format', align=Align.INLINE)
d.comment(0x9D02, 'X=0: start at first byte', align=Align.INLINE)
d.comment(0x9D04, 'ALWAYS branch to store and display', align=Align.INLINE)
d.comment(0x9D06, 'Load file handle from fs_cmd_data', align=Align.INLINE)
d.comment(0x9D09, 'Check and set up TXCB for transfer', align=Align.INLINE)
d.comment(0x9D0C, 'Receive and process reply', align=Align.INLINE)
d.comment(0x9D0F, 'Store result byte in fs_reply_cmd', align=Align.INLINE)
d.comment(0x9D12, 'Y=&0E: protection bits offset', align=Align.INLINE)
d.comment(0x9D14, 'Load access byte from fs_cmd_data', align=Align.INLINE)
d.comment(0x9D17, 'Extract protection bit flags', align=Align.INLINE)
d.comment(0x9D1A, 'Zero: use reply buffer data', align=Align.INLINE)
d.comment(0x9D1C, 'Load file info byte from fs_reply_data', align=Align.INLINE)
d.comment(0x9D1F, 'Store in FS options at offset Y', align=Align.INLINE)
d.comment(0x9D21, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9D22, 'Y=&12: end of protection fields?', align=Align.INLINE)
d.comment(0x9D24, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9D26, 'Load display flag from fs_messages_flag', align=Align.INLINE)
d.comment(0x9D29, 'Zero: skip display, return', align=Align.INLINE)
d.comment(0x9D2B, 'Y=&F4: index into hazel_display_buf for filename', align=Align.INLINE)
d.comment(0x9D2D, 'Load filename character from filename_buf', align=Align.INLINE)
d.comment(0x9D30, 'Print character via OSASCI', align=Align.INLINE)
d.comment(0x9D33, 'Advance to next character', align=Align.INLINE)
d.comment(0x9D34, 'Printed all 12 characters?', align=Align.INLINE)
d.comment(0x9D36, 'Y=5: offset for access string', align=Align.INLINE)
d.comment(0x9D38, 'Print 5 hex bytes (access info)', align=Align.INLINE)
d.comment(0x9D3B, 'Print load and exec addresses', align=Align.INLINE)
d.comment(0x9D3E, 'Print newline', align=Align.INLINE)
d.comment(0x9D41, 'Jump to return with last flag', align=Align.INLINE)
d.comment(0x9D44, 'Y=9: offset for exec address', align=Align.INLINE)
d.comment(0x9D46, 'Print 5 hex bytes (exec address)', align=Align.INLINE)
d.comment(0x9D49, 'Y=&0C: offset for length (3 bytes)', align=Align.INLINE)
d.comment(0x9D4B, 'X=3: print 3 bytes only', align=Align.INLINE)
d.comment(0x9D4D, 'ALWAYS branch to print routine', align=Align.INLINE)
d.comment(0x9D4F, 'X=4: print 5 bytes (4 to 0)', align=Align.INLINE)
d.comment(0x9D51, 'Load byte from FS options at offset Y', align=Align.INLINE)
d.comment(0x9D53, 'Print as 2-digit hex', align=Align.INLINE)
d.comment(0x9D56, 'Decrement byte offset', align=Align.INLINE)
d.comment(0x9D57, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9D58, 'Loop until all bytes printed', align=Align.INLINE)
d.comment(0x9D5A, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9D5C, 'Print space via OSASCI and return', align=Align.INLINE)
d.comment(0x9D5F, 'Y=5: copy 4 bytes (offsets 2-5)', align=Align.INLINE)
d.comment(0x9D61, 'Load byte from FS options', align=Align.INLINE)
d.comment(0x9D63, 'Store in zero page at work_ae+Y', align=Align.INLINE)
d.comment(0x9D66, 'Decrement index', align=Align.INLINE)
d.comment(0x9D67, 'Below offset 2?', align=Align.INLINE)
d.comment(0x9D69, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9D6B, 'Y += 5', align=Align.INLINE)
d.comment(0x9D6C, 'Y += 4', align=Align.INLINE)
d.comment(0x9D6D, '(continued)', align=Align.INLINE)
d.comment(0x9D6E, '(continued)', align=Align.INLINE)
d.comment(0x9D6F, '(continued)', align=Align.INLINE)
d.comment(0x9D70, 'Return', align=Align.INLINE)
d.comment(0x9D71, 'Y=&0D: copy bytes from offset &0D down', align=Align.INLINE)
d.comment(0x9D73, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9D74, 'Store byte in FS options at offset Y', align=Align.INLINE)
d.comment(0x9D76, 'Load next workspace byte from fs_cmd_urd+Y', align=Align.INLINE)
d.comment(0x9D79, 'Decrement index', align=Align.INLINE)
d.comment(0x9D7A, 'Below offset 2?', align=Align.INLINE)
d.comment(0x9D7C, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9D7E, 'Y -= 4', align=Align.INLINE)
d.comment(0x9D7F, 'Y -= 3', align=Align.INLINE)
d.comment(0x9D80, '(continued)', align=Align.INLINE)
d.comment(0x9D81, '(continued)', align=Align.INLINE)
d.comment(0x9D82, 'Return', align=Align.INLINE)
d.comment(0x9D83, 'Discard stacked value', align=Align.INLINE)
d.comment(0x9D84, 'Restore Y from fs_block_offset', align=Align.INLINE)
d.comment(0x9D86, 'Return (handle already matches)', align=Align.INLINE)
d.comment(0x9D87, 'Save port/sub-function on stack', align=Align.INLINE)
d.comment(0x9D88, 'Compare 5-byte handle with current', align=Align.INLINE)
d.comment(0x9D8B, 'Match: discard port and return', align=Align.INLINE)
d.comment(0x9D8D, 'X=0: loop start', align=Align.INLINE)
d.comment(0x9D8F, 'Y=4: copy 4 bytes', align=Align.INLINE)
d.comment(0x9D91, 'Clear fs_reply_cmd (transfer size low)', align=Align.INLINE)
d.comment(0x9D94, 'Clear fs_load_vector (transfer size high)', align=Align.INLINE)
d.comment(0x9D97, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9D98, 'Load address byte from zero page', align=Align.INLINE)
d.comment(0x9D9A, 'Store in TXCB start pointer', align=Align.INLINE)
d.comment(0x9D9C, 'Add offset from fs_func_code', align=Align.INLINE)
d.comment(0x9D9F, 'Store sum in TXCB end pointer', align=Align.INLINE)
d.comment(0x9DA1, 'Also update load address', align=Align.INLINE)
d.comment(0x9DA3, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9DA4, 'Decrement counter', align=Align.INLINE)
d.comment(0x9DA5, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9DA7, 'Carry set: overflow, use limit', align=Align.INLINE)
d.comment(0x9DA9, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9DAA, 'Load computed end address', align=Align.INLINE)
d.comment(0x9DAD, 'Subtract maximum from fs_work_4', align=Align.INLINE)
d.comment(0x9DB0, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9DB1, 'Decrement counter', align=Align.INLINE)
d.comment(0x9DB2, 'Loop for all bytes', align=Align.INLINE)
d.comment(0x9DB4, 'Below limit: keep computed end', align=Align.INLINE)
d.comment(0x9DB6, 'X=3: copy 4 bytes of limit', align=Align.INLINE)
d.comment(0x9DB8, 'Load limit from fs_work_4', align=Align.INLINE)
d.comment(0x9DBA, 'Store as TXCB end', align=Align.INLINE)
d.comment(0x9DBC, 'Decrement counter', align=Align.INLINE)
d.comment(0x9DBD, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9DBF, 'Pull port from stack', align=Align.INLINE)
d.comment(0x9DC0, 'Push back (keep for later)', align=Align.INLINE)
d.comment(0x9DC1, 'Save flags (carry = overflow state)', align=Align.INLINE)
d.comment(0x9DC2, 'Set TXCB port number', align=Align.INLINE)
d.comment(0x9DC4, 'A=&80: control byte for data request', align=Align.INLINE)
d.comment(0x9DC6, 'Set TXCB control byte', align=Align.INLINE)
d.comment(0x9DC8, 'Init TX pointer and send packet', align=Align.INLINE)
d.comment(0x9DCB, 'Load error pointer', align=Align.INLINE)
d.comment(0x9DCD, 'Init TXCB port from error pointer', align=Align.INLINE)
d.comment(0x9DD0, 'Restore overflow flags', align=Align.INLINE)
d.comment(0x9DD1, 'Carry set: discard and return', align=Align.INLINE)
d.comment(0x9DD3, 'A=&91: FS reply port', align=Align.INLINE)
d.comment(0x9DD5, 'Set TXCB port for reply', align=Align.INLINE)
d.comment(0x9DD7, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0x9DDA, 'Non-zero (not done): retry send', align=Align.INLINE)
d.comment(0x9DDC, 'Store sub-operation code', align=Align.INLINE)
d.comment(0x9DDF, 'Compare with 7', align=Align.INLINE)
d.comment(0x9DE1, 'Below 7: handle operations 1-6', align=Align.INLINE)
d.comment(0x9DE3, 'Above 7: jump to handle via finalise', align=Align.INLINE)
d.comment(0x9DE5, 'Equal to 7: jump to directory display', align=Align.INLINE)
d.comment(0x9DE8, 'Compare with 6', align=Align.INLINE)
d.comment(0x9DEA, '6: delete file operation', align=Align.INLINE)
d.comment(0x9DEC, 'Compare with 5', align=Align.INLINE)
d.comment(0x9DEE, '5: read catalogue info', align=Align.INLINE)
d.comment(0x9DF0, 'Compare with 4', align=Align.INLINE)
d.comment(0x9DF2, '4: write file attributes', align=Align.INLINE)
d.comment(0x9DF4, 'Compare with 1', align=Align.INLINE)
d.comment(0x9DF6, '1: read file info', align=Align.INLINE)
d.comment(0x9DF8, 'Shift left twice: A*4', align=Align.INLINE)
d.comment(0x9DF9, 'A*4', align=Align.INLINE)
d.comment(0x9DFA, 'Copy to Y as index', align=Align.INLINE)
d.comment(0x9DFB, 'Y -= 3 to get FS options offset', align=Align.INLINE)
d.comment(0x9DFE, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9E00, 'Load byte from FS options at offset Y', align=Align.INLINE)
d.comment(0x9E02, 'Store in fs_func_code buffer', align=Align.INLINE)
d.comment(0x9E05, 'Decrement source offset', align=Align.INLINE)
d.comment(0x9E06, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9E07, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9E09, 'X=5: copy arg to buffer at offset 5', align=Align.INLINE)
d.comment(0x9E0B, 'ALWAYS branch to copy and send', align=Align.INLINE)
d.comment(0x9E0D, 'Get access bits for file', align=Align.INLINE)
d.comment(0x9E10, 'Store access byte in fs_file_attrs', align=Align.INLINE)
d.comment(0x9E13, 'Y=9: source offset in FS options', align=Align.INLINE)
d.comment(0x9E15, 'X=8: copy 8 bytes to buffer', align=Align.INLINE)
d.comment(0x9E17, 'Load FS options byte', align=Align.INLINE)
d.comment(0x9E19, 'Store in fs_cmd_data buffer', align=Align.INLINE)
d.comment(0x9E1C, 'Decrement source offset', align=Align.INLINE)
d.comment(0x9E1D, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9E1E, 'Loop for all 8 bytes', align=Align.INLINE)
d.comment(0x9E20, 'X=&0A: buffer offset for argument', align=Align.INLINE)
d.comment(0x9E22, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0x9E25, 'Y=&13: OSWORD &13 (NFS operation)', align=Align.INLINE)
d.comment(0x9E27, 'ALWAYS branch to send request', align=Align.INLINE)
d.comment(0x9E29, 'Copy argument to buffer at X=0', align=Align.INLINE)
d.comment(0x9E2C, 'Y=&14: delete file command', align=Align.INLINE)
d.comment(0x9E2E, 'Set V flag (no directory check)', align=Align.INLINE)
d.comment(0x9E31, 'Send request with V set', align=Align.INLINE)
d.comment(0x9E34, 'Carry set: error, jump to finalise', align=Align.INLINE)
d.comment(0x9E36, 'No error: return with last flag', align=Align.INLINE)
d.comment(0x9E39, 'Get access bits for file', align=Align.INLINE)
d.comment(0x9E3C, 'Store in fs_func_code', align=Align.INLINE)
d.comment(0x9E3F, 'X=2: buffer offset', align=Align.INLINE)
d.comment(0x9E41, 'ALWAYS branch to copy and send', align=Align.INLINE)
d.comment(0x9E43, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9E45, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0x9E48, 'Y=&12: open file command', align=Align.INLINE)
d.comment(0x9E4A, 'Send open file request', align=Align.INLINE)
d.comment(0x9E4D, 'Load reply handle from fs_obj_type', align=Align.INLINE)
d.comment(0x9E50, 'Clear fs_obj_type', align=Align.INLINE)
d.comment(0x9E53, 'Clear fs_len_clear', align=Align.INLINE)
d.comment(0x9E56, 'Get protection bits', align=Align.INLINE)
d.comment(0x9E59, 'Load file handle from fs_cmd_data', align=Align.INLINE)
d.comment(0x9E5C, 'Zero: file not found, return', align=Align.INLINE)
d.comment(0x9E5E, 'Y=&0E: store access bits', align=Align.INLINE)
d.comment(0x9E60, 'Store access byte in FS options', align=Align.INLINE)
d.comment(0x9E62, 'Y=&0D', align=Align.INLINE)
d.comment(0x9E63, 'X=&0C: copy 12 bytes of file info', align=Align.INLINE)
d.comment(0x9E65, 'Load reply byte from fs_cmd_data+X', align=Align.INLINE)
d.comment(0x9E68, 'Store in FS options at offset Y', align=Align.INLINE)
d.comment(0x9E6A, 'Decrement destination offset', align=Align.INLINE)
d.comment(0x9E6B, 'Decrement source counter', align=Align.INLINE)
d.comment(0x9E6C, 'Loop for all 12 bytes', align=Align.INLINE)
d.comment(0x9E6E, 'X=1 (INX from 0)', align=Align.INLINE)
d.comment(0x9E6F, 'X=2', align=Align.INLINE)
d.comment(0x9E70, 'Y=&11: FS options offset', align=Align.INLINE)
d.comment(0x9E72, 'Load extended info byte from fs_access_level', align=Align.INLINE)
d.comment(0x9E75, 'Store in FS options', align=Align.INLINE)
d.comment(0x9E77, 'Decrement destination offset', align=Align.INLINE)
d.comment(0x9E78, 'Decrement source counter', align=Align.INLINE)
d.comment(0x9E79, 'Loop until all copied', align=Align.INLINE)
d.comment(0x9E7B, 'Reload file handle', align=Align.INLINE)
d.comment(0x9E7E, 'Transfer to A', align=Align.INLINE)
d.comment(0x9E7F, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9E82, 'Y=0: start writing at filename_buf[0]', align=Align.INLINE)
d.comment(0x9E84, 'Load source offset from fs_cmd_csd', align=Align.INLINE)
d.comment(0x9E87, 'Non-zero: copy from fs_cmd_data buffer', align=Align.INLINE)
d.comment(0x9E89, 'Load character from command line', align=Align.INLINE)
d.comment(0x9E8B, "Below '!' (control/space)?", align=Align.INLINE)
d.comment(0x9E8D, 'Yes: pad with spaces', align=Align.INLINE)
d.comment(0x9E8F, 'Store printable character in filename_buf', align=Align.INLINE)
d.comment(0x9E92, 'Advance to next character', align=Align.INLINE)
d.comment(0x9E93, 'Loop for more characters', align=Align.INLINE)
d.comment(0x9E95, "A=' ': space for padding", align=Align.INLINE)
d.comment(0x9E97, 'Store space in display buffer', align=Align.INLINE)
d.comment(0x9E9A, 'Advance index', align=Align.INLINE)
d.comment(0x9E9B, 'Filled all 12 characters?', align=Align.INLINE)
d.comment(0x9E9D, 'No: pad more spaces', align=Align.INLINE)
d.comment(0x9E9F, 'Return with field formatted', align=Align.INLINE)
d.comment(0x9EA0, 'Advance source and destination', align=Align.INLINE)
d.comment(0x9EA2, 'Load byte from fs_cmd_data buffer', align=Align.INLINE)
d.comment(0x9EA5, 'Store in filename_buf', align=Align.INLINE)
d.comment(0x9EA8, 'Bit 7 clear: more characters', align=Align.INLINE)
d.comment(0x9EAA, 'Return (bit 7 set = terminator)', align=Align.INLINE)
d.comment(0x9EAB, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9EAE, 'Store result as last byte flag', align=Align.INLINE)
d.comment(0x9EB0, 'Set FS options pointer', align=Align.INLINE)
d.comment(0x9EB3, 'OR with 0 to set flags', align=Align.INLINE)
d.comment(0x9EB5, 'Positive: handle sub-operations', align=Align.INLINE)
d.comment(0x9EB7, 'Shift left to check bit 6', align=Align.INLINE)
d.comment(0x9EB8, 'Zero (was &80): close channel', align=Align.INLINE)
d.comment(0x9EBA, 'Other: process all FCBs first', align=Align.INLINE)
d.comment(0x9EBD, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9EBE, 'Compare with &20 (space)', align=Align.INLINE)
d.comment(0x9EC0, 'Above &20: check further', align=Align.INLINE)
d.comment(0x9EC2, 'Below &20: invalid channel char', align=Align.INLINE)
d.comment(0x9EC5, "Compare with '0'", align=Align.INLINE)
d.comment(0x9EC7, "Above '0': invalid channel char", align=Align.INLINE)
d.comment(0x9EC9, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9ECC, 'Transfer Y to A (FCB index)', align=Align.INLINE)
d.comment(0x9ECD, 'Push FCB index', align=Align.INLINE)
d.comment(0x9ECE, 'Copy to X', align=Align.INLINE)
d.comment(0x9ECF, 'Y=0: clear counter', align=Align.INLINE)
d.comment(0x9ED1, 'Clear last byte flag', align=Align.INLINE)
d.comment(0x9ED3, 'Clear block offset', align=Align.INLINE)
d.comment(0x9ED5, 'Load channel data from fcb_attr_or_count_mid+X', align=Align.INLINE)
d.comment(0x9ED8, 'Store in FS options at Y', align=Align.INLINE)
d.comment(0x9EDA, 'Advance X by 8 (next FCB field)', align=Align.INLINE)
d.comment(0x9EDD, 'Advance destination index', align=Align.INLINE)
d.comment(0x9EDE, 'Copied all 4 channel fields?', align=Align.INLINE)
d.comment(0x9EE0, 'No: copy next field', align=Align.INLINE)
d.comment(0x9EE2, 'Pull saved FCB index', align=Align.INLINE)
d.comment(0x9EE3, 'Restore to fs_block_offset', align=Align.INLINE)
d.comment(0x9EE5, 'Compare with 5', align=Align.INLINE)
d.comment(0x9EE7, '5 or above: return with last flag', align=Align.INLINE)
d.comment(0x9EE9, 'Compare Y with 0', align=Align.INLINE)
d.comment(0x9EEB, 'Non-zero: handle OSFIND with channel', align=Align.INLINE)
d.comment(0x9EED, 'Y=0 (close): jump to OSFIND open', align=Align.INLINE)
d.comment(0x9EF0, 'Push sub-function', align=Align.INLINE)
d.comment(0x9EF1, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9EF2, 'Push X (FCB slot)', align=Align.INLINE)
d.comment(0x9EF3, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9EF4, 'Push Y (channel char)', align=Align.INLINE)
d.comment(0x9EF5, 'Check file is not a directory', align=Align.INLINE)
d.comment(0x9EF8, 'Pull channel char', align=Align.INLINE)
d.comment(0x9EF9, 'Store channel char as receive attribute', align=Align.INLINE)
d.comment(0x9EFC, 'Load FCB flag byte from fcb_net_or_port', align=Align.INLINE)
d.comment(0x9EFF, 'Store in fs_cmd_data', align=Align.INLINE)
d.comment(0x9F02, 'Pull X (FCB slot)', align=Align.INLINE)
d.comment(0x9F03, 'Restore X', align=Align.INLINE)
d.comment(0x9F04, 'Pull sub-function', align=Align.INLINE)
d.comment(0x9F05, 'Shift right: check bit 0', align=Align.INLINE)
d.comment(0x9F06, 'Zero (OSFIND close): handle close', align=Align.INLINE)
d.comment(0x9F08, 'Save flags (carry from LSR)', align=Align.INLINE)
d.comment(0x9F09, 'Push sub-function', align=Align.INLINE)
d.comment(0x9F0A, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9F0C, 'Load block offset', align=Align.INLINE)
d.comment(0x9F0E, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9F11, 'Load updated data from fcb_attr_or_count_mid', align=Align.INLINE)
d.comment(0x9F14, 'Store in fs_cmd_data', align=Align.INLINE)
d.comment(0x9F17, 'Pull sub-function', align=Align.INLINE)
d.comment(0x9F18, 'Store in fs_func_code', align=Align.INLINE)
d.comment(0x9F1B, 'Restore flags', align=Align.INLINE)
d.comment(0x9F1C, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9F1D, 'Push Y (offset)', align=Align.INLINE)
d.comment(0x9F1E, 'Carry clear: read operation', align=Align.INLINE)
d.comment(0x9F20, 'Y=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9F22, 'Load zero page data', align=Align.INLINE)
d.comment(0x9F24, 'Store in fs_data_count buffer', align=Align.INLINE)
d.comment(0x9F27, 'Decrement source', align=Align.INLINE)
d.comment(0x9F28, 'Decrement counter', align=Align.INLINE)
d.comment(0x9F29, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9F2B, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9F2D, 'X=5: argument offset', align=Align.INLINE)
d.comment(0x9F2F, 'Send TX control block to server', align=Align.INLINE)
d.comment(0x9F32, 'Store X in last byte flag', align=Align.INLINE)
d.comment(0x9F34, 'Pull saved offset', align=Align.INLINE)
d.comment(0x9F35, 'Set connection active flag', align=Align.INLINE)
d.comment(0x9F38, 'Return with last flag', align=Align.INLINE)
d.comment(0x9F3B, 'Y=&0C: TX buffer size (smaller)', align=Align.INLINE)
d.comment(0x9F3D, 'X=2: argument offset', align=Align.INLINE)
d.comment(0x9F3F, 'Send TX control block', align=Align.INLINE)
d.comment(0x9F42, 'Store A in last byte flag', align=Align.INLINE)
d.comment(0x9F44, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9F46, 'Y=2: zero page offset', align=Align.INLINE)
d.comment(0x9F48, 'Store A in zero page', align=Align.INLINE)
d.comment(0x9F4A, 'Load buffer byte from fs_cmd_data+Y', align=Align.INLINE)
d.comment(0x9F4D, 'Store in zero page at offset', align=Align.INLINE)
d.comment(0x9F4F, 'Decrement source X', align=Align.INLINE)
d.comment(0x9F50, 'Decrement counter Y', align=Align.INLINE)
d.comment(0x9F51, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9F53, 'Pull saved offset', align=Align.INLINE)
d.comment(0x9F54, 'Return with last flag', align=Align.INLINE)
d.comment(0x9F57, 'Carry set: write file pointer', align=Align.INLINE)
d.comment(0x9F59, 'Load block offset', align=Align.INLINE)
d.comment(0x9F5B, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9F5E, 'Load FS options pointer', align=Align.INLINE)
d.comment(0x9F60, 'Load FCB low byte from fcb_count_lo', align=Align.INLINE)
d.comment(0x9F63, 'Store in zero page pointer low', align=Align.INLINE)
d.comment(0x9F66, 'Load FCB high byte from fcb_attr_or_count_mid', align=Align.INLINE)
d.comment(0x9F69, 'Store in zero page pointer high', align=Align.INLINE)
d.comment(0x9F6C, 'Load FCB extent from fcb_station_or_count_hi', align=Align.INLINE)
d.comment(0x9F6F, 'Store in zero page work area', align=Align.INLINE)
d.comment(0x9F72, 'A=0: clear high byte', align=Align.INLINE)
d.comment(0x9F74, 'Store zero in work area high', align=Align.INLINE)
d.comment(0x9F77, 'ALWAYS branch to return with flag', align=Align.INLINE)
d.comment(0x9F79, 'Store write value in fs_func_code', align=Align.INLINE)
d.comment(0x9F7C, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9F7D, 'Push X (zero page offset)', align=Align.INLINE)
d.comment(0x9F7E, 'Y=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9F80, 'Load zero page data at offset', align=Align.INLINE)
d.comment(0x9F82, 'Store in fs_data_count buffer', align=Align.INLINE)
d.comment(0x9F85, 'Decrement source', align=Align.INLINE)
d.comment(0x9F86, 'Decrement counter', align=Align.INLINE)
d.comment(0x9F87, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9F89, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9F8B, 'X=5: argument offset', align=Align.INLINE)
d.comment(0x9F8D, 'Send TX control block', align=Align.INLINE)
d.comment(0x9F90, 'Store X in last byte flag', align=Align.INLINE)
d.comment(0x9F92, 'Pull saved zero page offset', align=Align.INLINE)
d.comment(0x9F93, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9F94, 'Load block offset (attribute)', align=Align.INLINE)
d.comment(0x9F96, 'Clear connection active flag', align=Align.INLINE)
d.comment(0x9F99, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9F9C, 'Load zero page pointer low', align=Align.INLINE)
d.comment(0x9F9F, 'Store back to FCB fcb_count_lo', align=Align.INLINE)
d.comment(0x9FA2, 'Load zero page pointer high', align=Align.INLINE)
d.comment(0x9FA5, 'Store back to FCB fcb_attr_or_count_mid', align=Align.INLINE)
d.comment(0x9FA8, 'Load zero page work byte', align=Align.INLINE)
d.comment(0x9FAB, 'Store back to FCB fcb_station_or_count_hi', align=Align.INLINE)
d.comment(0x9FAE, 'Return with last flag', align=Align.INLINE)
d.comment(0x9FB1, 'Process all matching FCBs first', align=Align.INLINE)
d.comment(0x9FB4, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9FB6, 'Push result on stack', align=Align.INLINE)
d.comment(0x9FB7, 'A=0: clear error flag', align=Align.INLINE)
d.comment(0x9FB9, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0x9FBC, 'Pull result back', align=Align.INLINE)
d.comment(0x9FBD, 'Restore X from FS options pointer', align=Align.INLINE)
d.comment(0x9FBF, 'Restore Y from block offset', align=Align.INLINE)
d.comment(0x9FC1, 'Return to caller', align=Align.INLINE)
d.comment(0x9FC2, 'Compare with 2 (open for output)', align=Align.INLINE)
d.comment(0x9FC4, '2 or above: handle file open', align=Align.INLINE)
d.comment(0x9FC6, 'Transfer to Y (Y=0 or 1)', align=Align.INLINE)
d.comment(0x9FC7, 'Non-zero (1 = read pointer): copy data', align=Align.INLINE)
d.comment(0x9FC9, 'A=5: return code for close-all', align=Align.INLINE)
d.comment(0x9FCB, 'ALWAYS branch to finalise', align=Align.INLINE)
d.comment(0x9FCD, 'Z set: jump to clear A and return', align=Align.INLINE)
d.comment(0x9FCF, 'A=0: clear result', align=Align.INLINE)
d.comment(0x9FD1, 'Shift right (always positive)', align=Align.INLINE)
d.comment(0x9FD2, 'Positive: jump to finalise', align=Align.INLINE)
d.comment(0x9FD4, 'Mask to 6-bit access value', align=Align.INLINE)
d.comment(0x9FD6, 'Non-zero: clear A and finalise', align=Align.INLINE)
d.comment(0x9FD8, 'Transfer X to A (options pointer)', align=Align.INLINE)
d.comment(0x9FD9, 'Allocate FCB slot or raise error', align=Align.INLINE)
d.comment(0x9FDC, 'Toggle bit 7', align=Align.INLINE)
d.comment(0x9FDE, 'Shift left: build open mode', align=Align.INLINE)
d.comment(0x9FDF, 'Store open mode in fs_cmd_data', align=Align.INLINE)
d.comment(0x9FE2, 'Rotate to complete mode byte', align=Align.INLINE)
d.comment(0x9FE3, 'Store in fs_func_code', align=Align.INLINE)
d.comment(0x9FE6, 'Parse command argument (Y=0)', align=Align.INLINE)
d.comment(0x9FE9, 'X=2: buffer offset', align=Align.INLINE)
d.comment(0x9FEB, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0x9FEE, 'Y=6: open file command', align=Align.INLINE)
d.comment(0x9FF0, 'Set V flag (skip directory check)', align=Align.INLINE)
d.comment(0x9FF3, 'Set carry', align=Align.INLINE)
d.comment(0x9FF4, 'Rotate carry into escapable flag bit 7', align=Align.INLINE)
d.comment(0x9FF6, 'Send open request with V set', align=Align.INLINE)
d.comment(0x9FF9, 'Carry set (error): jump to finalise', align=Align.INLINE)
d.comment(0x9FFB, 'A=&FF: mark as newly opened', align=Align.INLINE)
d.comment(0x9FFD, 'Store &FF as receive attribute', align=Align.INLINE)
d.comment(0xA000, 'Load handle from fs_cmd_data', align=Align.INLINE)
d.comment(0xA003, 'Push handle', align=Align.INLINE)
d.comment(0xA004, 'A=4: file info sub-command', align=Align.INLINE)
d.comment(0xA006, 'Store sub-command', align=Align.INLINE)
d.comment(0xA009, 'X=1: shift filename', align=Align.INLINE)
d.comment(0xA00B, 'Load filename byte from fs_func_code+X', align=Align.INLINE)
d.comment(0xA00E, 'Shift down to fs_cmd_data+X', align=Align.INLINE)
d.comment(0xA011, 'Advance source index', align=Align.INLINE)
d.comment(0xA012, 'Is it CR (end of filename)?', align=Align.INLINE)
d.comment(0xA014, 'No: continue shifting', align=Align.INLINE)
d.comment(0xA016, 'Y=&12: file info request', align=Align.INLINE)
d.comment(0xA018, 'Send file info request', align=Align.INLINE)
d.comment(0xA01B, 'Load last byte flag', align=Align.INLINE)
d.comment(0xA01D, 'Clear bit 6 (read/write bits)', align=Align.INLINE)
d.comment(0xA01F, 'OR with reply access byte', align=Align.INLINE)
d.comment(0xA022, 'Set bit 0 (file is open)', align=Align.INLINE)
d.comment(0xA024, 'Transfer to Y (access flags)', align=Align.INLINE)
d.comment(0xA025, 'Check bit 1 (write access)', align=Align.INLINE)
d.comment(0xA027, 'No write access: check read-only', align=Align.INLINE)
d.comment(0xA029, 'Pull handle from stack', align=Align.INLINE)
d.comment(0xA02A, 'Allocate FCB slot for channel', align=Align.INLINE)
d.comment(0xA02D, 'Non-zero: FCB allocated, store flags', align=Align.INLINE)
d.comment(0xA02F, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0xA032, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0xA035, 'Transfer A to X', align=Align.INLINE)
d.comment(0xA036, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA039, 'Transfer X back to A', align=Align.INLINE)
d.comment(0xA03A, 'Zero: close file, process FCBs', align=Align.INLINE)
d.comment(0xA03C, 'Save text pointer for OS', align=Align.INLINE)
d.comment(0xA03F, 'Load current directory handle', align=Align.INLINE)
d.comment(0xA042, 'Zero: allocate new FCB', align=Align.INLINE)
d.comment(0xA044, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA045, 'X=0: clear directory handle', align=Align.INLINE)
d.comment(0xA047, 'Store zero (clear handle)', align=Align.INLINE)
d.comment(0xA04A, 'ALWAYS branch to finalise', align=Align.INLINE)
d.comment(0xA04C, 'Load access/open mode byte', align=Align.INLINE)
d.comment(0xA04F, 'Rotate right: check bit 0', align=Align.INLINE)
d.comment(0xA050, 'Carry set (bit 0): check read permission', align=Align.INLINE)
d.comment(0xA052, 'Rotate right: check bit 1', align=Align.INLINE)
d.comment(0xA053, 'Carry clear (no write): skip', align=Align.INLINE)
d.comment(0xA055, 'Test bit 7 of fs_data_count (lock flag)', align=Align.INLINE)
d.comment(0xA058, 'Not locked: skip', align=Align.INLINE)
d.comment(0xA05A, 'Transfer Y to A (flags)', align=Align.INLINE)
d.comment(0xA05B, 'Set bit 5 (locked file flag)', align=Align.INLINE)
d.comment(0xA05D, 'Transfer back to Y', align=Align.INLINE)
d.comment(0xA05E, 'Pull handle from stack', align=Align.INLINE)
d.comment(0xA05F, 'Allocate FCB slot for channel', align=Align.INLINE)
d.comment(0xA062, 'Transfer to X', align=Align.INLINE)
d.comment(0xA063, 'Transfer Y to A (flags)', align=Align.INLINE)
d.comment(0xA064, 'Store flags in FCB table fcb_flags', align=Align.INLINE)
d.comment(0xA067, 'Transfer X back to A (handle)', align=Align.INLINE)
d.comment(0xA068, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0xA06B, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0xA06E, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA06F, 'Non-zero channel: close specific', align=Align.INLINE)
d.comment(0xA071, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0xA073, 'Push (save for restore)', align=Align.INLINE)
d.comment(0xA074, 'A=&77: OSBYTE close spool/exec files', align=Align.INLINE)
d.comment(0xA076, 'Close any *SPOOL and *EXEC files', align=Align.INLINE)
d.comment(0xA079, 'Pull saved options pointer', align=Align.INLINE)
d.comment(0xA07A, 'Restore FS options pointer', align=Align.INLINE)
d.comment(0xA07C, 'A=0: clear flags', align=Align.INLINE)
d.comment(0xA082, 'ALWAYS branch to send close request', align=Align.INLINE)
d.comment(0xA084, 'Validate channel character', align=Align.INLINE)
d.comment(0xA08A, 'Store as fs_cmd_data (file handle)', align=Align.INLINE)
d.comment(0xA08D, 'X=1: argument size', align=Align.INLINE)
d.comment(0xA08F, 'Y=7: close file command', align=Align.INLINE)
d.comment(0xA091, 'Send close file request', align=Align.INLINE)
d.comment(0xA098, 'Clear V flag', align=Align.INLINE)
d.comment(0xA099, 'Scan and clear all FCB flags', align=Align.INLINE)
d.comment(0xA09C, 'Return with last flag', align=Align.INLINE)
d.comment(0xA09F, 'A=0: clear FCB entry', align=Align.INLINE)
d.comment(0xA0A4, 'Clear hazel_fcb_state_byte for slot Y', align=Align.INLINE)
d.comment(0xA0AF, 'X==4 path: Y < 4?', align=Align.INLINE)
d.comment(0xA0B1, 'Yes: send OSARGS request via TXCB', align=Align.INLINE)
d.comment(0xA0B6, 'Store Y as hazel_fs_messages_flag (display control)', align=Align.INLINE)
d.comment(0xA0C3, 'Y=&16: TXCB function code (OSARGS request)', align=Align.INLINE)
d.comment(0xA0C8, 'Reload Y from fs_block_offset', align=Align.INLINE)
d.comment(0xA0CD, 'No error (positive): tail to done_close', align=Align.INLINE)
d.comment(0xA10B, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0xA10E, 'Push checksum-verify result -- preserve it across the FCB lookups below', align=Align.INLINE)
d.comment(0xA10F, 'Load block offset', align=Align.INLINE)
d.comment(0xA111, 'Push block offset', align=Align.INLINE)
d.comment(0xA112, 'Store X in cur_chan_attr', align=Align.INLINE)
d.comment(0xA115, 'Find matching FCB entry', align=Align.INLINE)
d.comment(0xA118, 'Zero: no match found', align=Align.INLINE)
d.comment(0xA11A, 'Load FCB low byte from fcb_count_lo', align=Align.INLINE)
d.comment(0xA11D, 'Compare with stored offset fcb_buf_offset', align=Align.INLINE)
d.comment(0xA120, 'FCB lo-byte below stored offset -> not the matching FCB; mark_not_found', align=Align.INLINE)
d.comment(0xA122, 'X=&FF: mark as found (all bits set)', align=Align.INLINE)
d.comment(0xA124, 'ALWAYS branch (negative)', align=Align.INLINE)
d.comment(0xA126, 'X=0: mark as not found', align=Align.INLINE)
d.comment(0xA128, 'Restore block offset from stack', align=Align.INLINE)
d.comment(0xA12A, 'Restore result from stack', align=Align.INLINE)
d.comment(0xA12B, 'Return', align=Align.INLINE)
d.comment(0xA12C, 'Y=9: FS options offset for high address', align=Align.INLINE)
d.comment(0xA12E, 'Add workspace values to FS options', align=Align.INLINE)
d.comment(0xA131, 'Y=1: FS options offset for low address', align=Align.INLINE)
d.comment(0xA134, 'X=&FC: loop counter (-4 to -1)', align=Align.INLINE)
d.comment(0xA136, 'Load FS options byte at offset Y', align=Align.INLINE)
d.comment(0xA138, 'Test fs_load_addr_2 bit 7 (add/subtract)', align=Align.INLINE)
d.comment(0xA13C, 'Add workspace byte to FS options', align=Align.INLINE)
d.comment(0xA142, 'Subtract workspace byte from FS options', align=Align.INLINE)
d.comment(0xA145, 'Store result back to FS options', align=Align.INLINE)
d.comment(0xA147, 'Advance to next byte', align=Align.INLINE)
d.comment(0xA148, 'Advance counter', align=Align.INLINE)
d.comment(0xA149, 'Loop until 4 bytes processed', align=Align.INLINE)
d.comment(0xA14B, 'Return', align=Align.INLINE)
d.comment(0xA14C, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0xA14F, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0xA152, 'Push transfer type on stack', align=Align.INLINE)
d.comment(0xA153, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA156, 'Pull transfer type', align=Align.INLINE)
d.comment(0xA157, 'Transfer to X', align=Align.INLINE)
d.comment(0xA158, 'Zero: no valid operation, return', align=Align.INLINE)
d.comment(0xA15A, 'Decrement (convert 1-based to 0-based)', align=Align.INLINE)
d.comment(0xA15B, 'Compare with 8 (max operation)', align=Align.INLINE)
d.comment(0xA15D, 'Below 8: valid operation', align=Align.INLINE)
d.comment(0xA15F, 'Out of range: return with flag', align=Align.INLINE)
d.comment(0xA162, 'Transfer operation code to A', align=Align.INLINE)
d.comment(0xA163, 'Y=0: buffer offset', align=Align.INLINE)
d.comment(0xA165, 'Push operation code', align=Align.INLINE)
d.comment(0xA166, 'Compare with 4 (write operations)', align=Align.INLINE)
d.comment(0xA168, 'Below 4: read operation', align=Align.INLINE)
d.comment(0xA16A, '4 or above: write data block', align=Align.INLINE)
d.comment(0xA16D, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0xA16F, 'Push handle', align=Align.INLINE)
d.comment(0xA170, 'Check file is not a directory', align=Align.INLINE)
d.comment(0xA173, 'Pull handle', align=Align.INLINE)
d.comment(0xA174, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA175, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0xA178, 'Load FCB flag byte from fcb_net_or_port', align=Align.INLINE)
d.comment(0xA17B, 'Store file handle in fs_cmd_data', align=Align.INLINE)
d.comment(0xA17E, 'A=0: clear direction flag', align=Align.INLINE)
d.comment(0xA180, 'Store in fs_func_code', align=Align.INLINE)
d.comment(0xA183, 'Load FCB low byte (position)', align=Align.INLINE)
d.comment(0xA186, 'Store in fs_data_count', align=Align.INLINE)
d.comment(0xA189, 'Load FCB high byte', align=Align.INLINE)
d.comment(0xA18C, 'Store in fs_reply_cmd', align=Align.INLINE)
d.comment(0xA18F, 'Load FCB extent byte', align=Align.INLINE)
d.comment(0xA192, 'Store in fs_load_vector', align=Align.INLINE)
d.comment(0xA195, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0xA197, 'X=5: argument count', align=Align.INLINE)
d.comment(0xA199, 'Send TX control block to server', align=Align.INLINE)
d.comment(0xA19C, 'Pull operation code', align=Align.INLINE)
d.comment(0xA19D, 'Set up transfer workspace', align=Align.INLINE)
d.comment(0xA1A0, 'Save flags (carry from setup)', align=Align.INLINE)
d.comment(0xA1A1, 'Y=0: index for channel handle', align=Align.INLINE)
d.comment(0xA1A3, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0xA1A5, 'Carry set (write): set active', align=Align.INLINE)
d.comment(0xA1A7, 'Read: clear connection active', align=Align.INLINE)
d.comment(0xA1AA, 'Branch to continue (always positive)', align=Align.INLINE)
d.comment(0xA1AC, 'Write: set connection active', align=Align.INLINE)
d.comment(0xA1AF, 'Clear fs_func_code (Y=0)', align=Align.INLINE)
d.comment(0xA1B2, 'Look up channel slot data', align=Align.INLINE)
d.comment(0xA1B5, 'Store flag byte in fs_cmd_data', align=Align.INLINE)
d.comment(0xA1B8, 'Y=&0C: TX buffer size (short)', align=Align.INLINE)
d.comment(0xA1BA, 'X=2: argument count', align=Align.INLINE)
d.comment(0xA1BC, 'Send TX control block', align=Align.INLINE)
d.comment(0xA1BF, 'Look up channel entry at Y=0', align=Align.INLINE)
d.comment(0xA1C2, 'Y=9: FS options offset for position', align=Align.INLINE)
d.comment(0xA1C4, 'Load new position low from fs_cmd_data', align=Align.INLINE)
d.comment(0xA1C7, 'Update FCB low byte in fcb_count_lo', align=Align.INLINE)
d.comment(0xA1CA, 'Store in FS options at Y=9', align=Align.INLINE)
d.comment(0xA1CC, 'Y=&0A', align=Align.INLINE)
d.comment(0xA1CD, 'Load new position high from fs_func_code', align=Align.INLINE)
d.comment(0xA1D0, 'Update FCB high byte in fcb_attr_or_count_mid', align=Align.INLINE)
d.comment(0xA1D3, 'Store in FS options at Y=&0A', align=Align.INLINE)
d.comment(0xA1D5, 'Y=&0B', align=Align.INLINE)
d.comment(0xA1D6, 'Load new extent from fs_data_count', align=Align.INLINE)
d.comment(0xA1D9, 'Update FCB extent in fcb_station_or_count_hi', align=Align.INLINE)
d.comment(0xA1DC, 'Store in FS options at Y=&0B', align=Align.INLINE)
d.comment(0xA1DE, 'A=0: clear high byte of extent', align=Align.INLINE)
d.comment(0xA1E0, 'Y=&0C', align=Align.INLINE)
d.comment(0xA1E1, 'Store zero in FS options at Y=&0C', align=Align.INLINE)
d.comment(0xA1E3, 'Restore flags', align=Align.INLINE)
d.comment(0xA1E4, 'Carry clear: skip last-byte check', align=Align.INLINE)
d.comment(0xA1E6, 'Load last-byte-of-transfer flag', align=Align.INLINE)
d.comment(0xA1E8, 'Is transfer still pending (flag=3)?', align=Align.INLINE)
d.comment(0xA1EA, 'A=0: success', align=Align.INLINE)
d.comment(0xA1EC, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0xA1EF, 'Y=0: offset for channel handle', align=Align.INLINE)
d.comment(0xA1F1, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0xA1F3, 'Look up channel by character', align=Align.INLINE)
d.comment(0xA1F6, 'Load slot-attribute byte from hazel_fcb_slot_attr,X', align=Align.INLINE)
d.comment(0xA1F9, 'Return with flag in A', align=Align.INLINE)
d.comment(0xA1FA, 'Push operation code on stack', align=Align.INLINE)
d.comment(0xA1FB, 'Look up channel entry at Y=0', align=Align.INLINE)
d.comment(0xA1FE, 'Store flag byte in fs_cmd_data', align=Align.INLINE)
d.comment(0xA201, 'Y=&0B: source offset in FS options', align=Align.INLINE)
d.comment(0xA203, 'X=6: copy 6 bytes', align=Align.INLINE)
d.comment(0xA205, 'Load FS options byte', align=Align.INLINE)
d.comment(0xA207, 'Store in fs_func_code buffer', align=Align.INLINE)
d.comment(0xA20A, 'Decrement source index', align=Align.INLINE)
d.comment(0xA20B, 'Skip offset 8?', align=Align.INLINE)
d.comment(0xA20D, 'No: continue copy', align=Align.INLINE)
d.comment(0xA20F, 'Skip offset 8 (hole in structure)', align=Align.INLINE)
d.comment(0xA210, 'Decrement destination counter', align=Align.INLINE)
d.comment(0xA211, 'Loop until all 6 bytes copied', align=Align.INLINE)
d.comment(0xA213, 'Pull operation code', align=Align.INLINE)
d.comment(0xA214, 'Shift right: check bit 0 (direction)', align=Align.INLINE)
d.comment(0xA215, 'Push updated code', align=Align.INLINE)
d.comment(0xA216, 'Carry clear: OSBGET (read)', align=Align.INLINE)
d.comment(0xA218, 'Carry set: OSBPUT (write), X=1', align=Align.INLINE)
d.comment(0xA219, 'Store direction flag in fs_func_code', align=Align.INLINE)
d.comment(0xA21C, 'Y=&0B: TX buffer size', align=Align.INLINE)
d.comment(0xA21E, 'X=&91: port for OSBGET', align=Align.INLINE)
d.comment(0xA220, 'Pull operation code', align=Align.INLINE)
d.comment(0xA221, 'Push back (keep on stack)', align=Align.INLINE)
d.comment(0xA222, 'Zero (OSBGET): keep port &91', align=Align.INLINE)
d.comment(0xA224, 'X=&92: port for OSBPUT', align=Align.INLINE)
d.comment(0xA226, 'Y=&0A: adjusted buffer size', align=Align.INLINE)
d.comment(0xA227, 'Store port in fs_cmd_urd', align=Align.INLINE)
d.comment(0xA22A, 'Store port in fs_error_ptr', align=Align.INLINE)
d.comment(0xA22C, 'X=8: argument count', align=Align.INLINE)
d.comment(0xA22E, 'Load file handle from fs_cmd_data', align=Align.INLINE)
d.comment(0xA231, 'Send request (no write data)', align=Align.INLINE)
d.comment(0xA234, 'X=0: index', align=Align.INLINE)
d.comment(0xA236, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0xA238, 'Transfer to X as index', align=Align.INLINE)
d.comment(0xA239, 'Load FCB flags from fcb_flags', align=Align.INLINE)
d.comment(0xA23C, 'Toggle bit 0 (transfer direction)', align=Align.INLINE)
d.comment(0xA23E, 'Store updated flags', align=Align.INLINE)
d.comment(0xA241, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xA242, 'X=4: process 4 address bytes', align=Align.INLINE)
d.comment(0xA244, 'Load FS options address byte', align=Align.INLINE)
d.comment(0xA246, 'Store in zero page address area', align=Align.INLINE)
d.comment(0xA249, 'Store in TXCB position', align=Align.INLINE)
d.comment(0xA24C, 'Advance Y by 4', align=Align.INLINE)
d.comment(0xA24F, 'Add offset from FS options', align=Align.INLINE)
d.comment(0xA251, 'Store computed end address', align=Align.INLINE)
d.comment(0xA254, 'Retreat Y by 3 for next pair', align=Align.INLINE)
d.comment(0xA257, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xA258, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0xA25A, 'X=1 (INX from 0)', align=Align.INLINE)
d.comment(0xA25B, 'Load offset from fs_cmd_csd', align=Align.INLINE)
d.comment(0xA25E, 'Copy to fs_func_code', align=Align.INLINE)
d.comment(0xA261, 'Decrement counter', align=Align.INLINE)
d.comment(0xA262, 'Loop until both bytes copied', align=Align.INLINE)
d.comment(0xA264, 'Pull operation code', align=Align.INLINE)
d.comment(0xA265, 'Non-zero (OSBPUT): swap addresses', align=Align.INLINE)
d.comment(0xA267, 'Load port from fs_cmd_urd', align=Align.INLINE)
d.comment(0xA26A, 'Check and set up TXCB', align=Align.INLINE)
d.comment(0xA26D, 'Carry set: skip swap', align=Align.INLINE)
d.comment(0xA26F, 'Send TXCB and swap start/end addresses', align=Align.INLINE)
d.comment(0xA272, 'Receive and process reply', align=Align.INLINE)
d.comment(0xA275, 'Store result in fs_load_addr_2', align=Align.INLINE)
d.comment(0xA277, 'Update addresses from offset 9', align=Align.INLINE)
d.comment(0xA27A, 'Decrement fs_load_addr_2', align=Align.INLINE)
d.comment(0xA27C, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xA27D, 'Adjust FS options by 4 bytes', align=Align.INLINE)
d.comment(0xA280, 'Shift fs_cmd_data left (update status)', align=Align.INLINE)
d.comment(0xA283, 'Return', align=Align.INLINE)
d.comment(0xA284, 'Save flags before reply processing', align=Align.INLINE)
d.comment(0xA285, 'Process server reply', align=Align.INLINE)
d.comment(0xA288, 'Restore flags after reply processing', align=Align.INLINE)
d.comment(0xA289, 'Return', align=Align.INLINE)
d.comment(0xA28A, 'Y=&15: TX buffer size for OSBPUT data', align=Align.INLINE)
d.comment(0xA28C, 'Send TX control block', align=Align.INLINE)
d.comment(0xA28F, 'Load display flag from hazel_fs_flags', align=Align.INLINE)
d.comment(0xA292, 'Store in hazel_txcb_byte_16', align=Align.INLINE)
d.comment(0xA295, 'Clear fs_load_addr (X=0)', align=Align.INLINE)
d.comment(0xA297, 'Clear fs_load_addr_hi', align=Align.INLINE)
d.comment(0xA299, 'A=&12: byte count for data block', align=Align.INLINE)
d.comment(0xA29B, 'Store in fs_load_addr_2', align=Align.INLINE)
d.comment(0xA29D, 'ALWAYS branch to write data block', align=Align.INLINE)
d.comment(0xA29F, 'Y=4: offset for station comparison', align=Align.INLINE)
d.comment(0xA2A1, 'Load stored station from tube_present', align=Align.INLINE)
d.comment(0xA2A4, 'Zero: skip station check', align=Align.INLINE)
d.comment(0xA2A6, 'Compare with FS options station', align=Align.INLINE)
d.comment(0xA2A8, 'Mismatch: skip subtraction', align=Align.INLINE)
d.comment(0xA2AA, 'Y=3', align=Align.INLINE)
d.comment(0xA2AB, 'Subtract FS options value', align=Align.INLINE)
d.comment(0xA2AD, 'Store result in svc_state', align=Align.INLINE)
d.comment(0xA2AF, 'Load FS options byte at Y', align=Align.INLINE)
d.comment(0xA2B1, 'Store in workspace at fs_last_byte_flag+Y', align=Align.INLINE)
d.comment(0xA2B4, 'Decrement index', align=Align.INLINE)
d.comment(0xA2B5, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0xA2B7, 'Pull operation code', align=Align.INLINE)
d.comment(0xA2B8, 'Mask to 2-bit sub-operation', align=Align.INLINE)
d.comment(0xA2BA, 'Zero: send OSBPUT data', align=Align.INLINE)
d.comment(0xA2BC, 'Shift right: check bit 0', align=Align.INLINE)
d.comment(0xA2BD, 'Zero (bit 0 clear): handle read', align=Align.INLINE)
d.comment(0xA2BF, 'Carry set: handle catalogue update', align=Align.INLINE)
d.comment(0xA2C1, 'Transfer to Y (Y=0)', align=Align.INLINE)
d.comment(0xA2C2, 'Load data byte from fs_csd_handle', align=Align.INLINE)
d.comment(0xA2C5, 'Store in fs_cmd_csd', align=Align.INLINE)
d.comment(0xA2C8, 'Load high data byte from fs_lib_handle', align=Align.INLINE)
d.comment(0xA2CB, 'Store in fs_cmd_lib', align=Align.INLINE)
d.comment(0xA2CE, 'Load port from fs_urd_handle', align=Align.INLINE)
d.comment(0xA2D1, 'Store in fs_cmd_urd', align=Align.INLINE)
d.comment(0xA2D4, 'X=&12: buffer size marker', align=Align.INLINE)
d.comment(0xA2D6, 'Store in fs_cmd_y_param', align=Align.INLINE)
d.comment(0xA2D9, 'A=&0D: count value', align=Align.INLINE)
d.comment(0xA2DB, 'Store in fs_func_code', align=Align.INLINE)
d.comment(0xA2DE, 'Store in fs_load_addr_2', align=Align.INLINE)
d.comment(0xA2E0, 'Shift right (A=6)', align=Align.INLINE)
d.comment(0xA2E1, 'Store in fs_cmd_data', align=Align.INLINE)
d.comment(0xA2E4, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xA2E5, 'Prepare and send TX control block', align=Align.INLINE)
d.comment(0xA2E8, 'Store X in fs_load_addr_hi (X=0)', align=Align.INLINE)
d.comment(0xA2EA, 'X=1 (after INX)', align=Align.INLINE)
d.comment(0xA2EB, 'Store X in fs_load_addr', align=Align.INLINE)
d.comment(0xA2ED, 'Load svc_state (tube flag)', align=Align.INLINE)
d.comment(0xA2EF, 'Non-zero: write via tube', align=Align.INLINE)
d.comment(0xA2F1, 'Load source index from fs_load_addr', align=Align.INLINE)
d.comment(0xA2F3, 'Load destination index from fs_load_addr_hi', align=Align.INLINE)
d.comment(0xA2F5, 'Load data byte from fs_cmd_data buffer', align=Align.INLINE)
d.comment(0xA2F8, 'Store to destination via fs_crc pointer', align=Align.INLINE)
d.comment(0xA2FA, 'Advance source index', align=Align.INLINE)
d.comment(0xA2FB, 'Advance destination index', align=Align.INLINE)
d.comment(0xA2FC, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xA2FE, 'Loop until all bytes transferred', align=Align.INLINE)
d.comment(0xA305, 'A=1: tube transfer type (write)', align=Align.INLINE)
d.comment(0xA307, 'Load destination low from fs_options', align=Align.INLINE)
d.comment(0xA30C, 'No wrap: skip high increment', align=Align.INLINE)
d.comment(0xA30F, 'Set up tube transfer address', align=Align.INLINE)
d.comment(0xA314, 'Load data byte from buffer', align=Align.INLINE)
d.comment(0xA317, 'Write to tube data register 3', align=Align.INLINE)
d.comment(0xA31A, 'Advance source index', align=Align.INLINE)
d.comment(0xA31B, 'Y=6: tube write delay', align=Align.INLINE)
d.comment(0xA31D, 'Delay loop: decrement Y', align=Align.INLINE)
d.comment(0xA320, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xA324, 'A=&83: release tube claim', align=Align.INLINE)
d.comment(0xA326, 'Release tube', align=Align.INLINE)
d.comment(0xA329, 'Jump to clear A and finalise return', align=Align.INLINE)
d.comment(0xA32C, 'Y=9: offset for position byte', align=Align.INLINE)
d.comment(0xA330, 'Store in fs_func_code', align=Align.INLINE)
d.comment(0xA333, 'Y=5: offset for extent byte', align=Align.INLINE)
d.comment(0xA335, 'Load extent byte from FS options', align=Align.INLINE)
d.comment(0xA337, 'Store in fs_data_count', align=Align.INLINE)
d.comment(0xA33A, 'X=&0D: byte count', align=Align.INLINE)
d.comment(0xA33C, 'Store in fs_reply_cmd', align=Align.INLINE)
d.comment(0xA33F, 'Y=2: command sub-type', align=Align.INLINE)
d.comment(0xA343, 'Store in fs_cmd_data', align=Align.INLINE)
d.comment(0xA346, 'Y=3: TX buffer command byte', align=Align.INLINE)
d.comment(0xA34C, 'Load data offset from fs_func_code', align=Align.INLINE)
d.comment(0xA34F, 'Store as first byte of FS options', align=Align.INLINE)
d.comment(0xA351, 'Load data count from fs_cmd_data', align=Align.INLINE)
d.comment(0xA354, 'Y=9: position offset in FS options', align=Align.INLINE)
d.comment(0xA356, 'Add to current position', align=Align.INLINE)
d.comment(0xA358, 'Store updated position', align=Align.INLINE)
d.comment(0xA35A, 'Load TXCB end byte', align=Align.INLINE)
d.comment(0xA35C, 'Subtract 7 (header overhead)', align=Align.INLINE)
d.comment(0xA35E, 'Store remaining data size', align=Align.INLINE)
d.comment(0xA361, 'Store in fs_load_addr_2 (byte count)', align=Align.INLINE)
d.comment(0xA363, 'Zero bytes: skip write', align=Align.INLINE)
d.comment(0xA365, 'Write data block to host/tube', align=Align.INLINE)
d.comment(0xA368, 'X=2: clear 3 bytes (indices 0-2)', align=Align.INLINE)
d.comment(0xA36A, 'Clear fs_data_count+X', align=Align.INLINE)
d.comment(0xA36D, 'Decrement index', align=Align.INLINE)
d.comment(0xA36E, 'Loop until all cleared', align=Align.INLINE)
d.comment(0xA370, 'Update addresses from offset 1', align=Align.INLINE)
d.comment(0xA373, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xA374, 'Decrement fs_load_addr_2', align=Align.INLINE)
d.comment(0xA376, 'Load data count from fs_cmd_data', align=Align.INLINE)
d.comment(0xA379, 'Copy to fs_func_code', align=Align.INLINE)
d.comment(0xA37C, 'Adjust FS options by 4 bytes (subtract)', align=Align.INLINE)
d.comment(0xA37F, 'X=3: check 4 bytes', align=Align.INLINE)
d.comment(0xA381, 'Y=5: starting offset', align=Align.INLINE)
d.comment(0xA383, 'Set carry for comparison', align=Align.INLINE)
d.comment(0xA384, 'Load FS options byte', align=Align.INLINE)
d.comment(0xA386, 'Non-zero: more data remaining', align=Align.INLINE)
d.comment(0xA388, 'Advance to next byte', align=Align.INLINE)
d.comment(0xA389, 'Decrement counter', align=Align.INLINE)
d.comment(0xA38A, 'Loop until all bytes checked', align=Align.INLINE)
d.comment(0xA38C, 'All zero: clear carry (transfer complete)', align=Align.INLINE)
d.comment(0xA38D, 'Jump to update catalogue and return', align=Align.INLINE)
d.comment(0xA390, 'A=&C3: tube claim protocol', align=Align.INLINE)
d.comment(0xA392, 'Dispatch tube address/data claim', align=Align.INLINE)
d.comment(0xA395, 'Carry clear: claim failed, retry', align=Align.INLINE)
d.comment(0xA397, 'Return (tube claimed)', align=Align.INLINE)
d.comment(0xA49F, 'CR (carriage return)', align=Align.INLINE)
d.comment(0xA517, 'Increment handle byte', align=Align.INLINE)
d.comment(0xA51C, 'Non-zero: handle valid, execute', align=Align.INLINE)
d.comment(0xA52D, 'X=2', align=Align.INLINE)
d.comment(0xA533, 'Send re-open request', align=Align.INLINE)
d.comment(0xA53B, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0xA545, 'Load library flag byte', align=Align.INLINE)
d.comment(0xA548, 'Bit 7 set: library already tried', align=Align.INLINE)
d.comment(0xA54E, 'Carry set: bad command', align=Align.INLINE)
d.comment(0xA553, 'Load filename byte', align=Align.INLINE)
d.comment(0xA55A, 'Shift filename right by 8 bytes', align=Align.INLINE)
d.comment(0xA55D, 'Store shifted byte', align=Align.INLINE)
d.comment(0xA565, "Copy 'Library.' prefix", align=Align.INLINE)
d.comment(0xA568, 'Store prefix byte', align=Align.INLINE)
d.comment(0xA56C, 'Loop until prefix copied', align=Align.INLINE)
d.comment(0xA56E, 'Load library flag', align=Align.INLINE)
d.comment(0xA576, 'Retry file open with library path', align=Align.INLINE)
d.comment(0xA57B, 'Load backup byte', align=Align.INLINE)
d.comment(0xA583, 'No: continue restoring', align=Align.INLINE)
d.comment(0xA585, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA5AE, 'X=3: check 4 execution bytes', align=Align.INLINE)
d.comment(0xA5B0, 'Increment execution address byte', align=Align.INLINE)
d.comment(0xA5B6, 'Loop until all checked', align=Align.INLINE)
d.comment(0xA5BA, "Generate 'No!' error", align=Align.INLINE)
d.comment(0xA5C6, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA5CC, 'Clear status in channel table', align=Align.INLINE)
d.comment(0xA5E2, 'Y=0', align=Align.INLINE)
d.comment(0xA5F1, 'Is it space?', align=Align.INLINE)
d.comment(0xA5F3, 'Yes: skip it', align=Align.INLINE)
d.comment(0xA5F9, 'Add to text pointer low', align=Align.INLINE)
d.comment(0xA603, 'Save text pointer for later', align=Align.INLINE)
d.comment(0xA611, 'X=&4A: FS command table offset', align=Align.INLINE)
d.comment(0xA623, 'All &FF?', align=Align.INLINE)
d.comment(0xA627, 'Claim tube for data transfer', align=Align.INLINE)
d.comment(0xA62A, 'X=9: parameter count', align=Align.INLINE)
d.comment(0xA7A1, '*Access', align=Align.INLINE)
d.comment(0xA7A7, 'V no arg; syn 9: <obj> (L)(W)(R)...', align=Align.INLINE)
d.comment(0xA83C, 'CLC so SBC subtracts value+1', align=Align.INLINE)
d.comment(0xA83F, 'A = OSWORD - &0E (CLC+SBC = -&0E)', align=Align.INLINE)
d.comment(0xA841, 'Below &0E: not ours, return', align=Align.INLINE)
d.comment(0xA843, 'Index >= 7? (OSWORD > &14)', align=Align.INLINE)
d.comment(0xA845, 'Above &14: not ours, return', align=Align.INLINE)
d.comment(0xA847, 'X=OSWORD handler index (0-6)', align=Align.INLINE)
d.comment(0xA848, 'Y=6: save 6 workspace bytes', align=Align.INLINE)
d.comment(0xA84D, 'Save on stack', align=Align.INLINE)
d.comment(0xA84E, 'Load OSWORD parameter byte', align=Align.INLINE)
d.comment(0xA851, 'Copy parameter to workspace', align=Align.INLINE)
d.comment(0xA857, 'Set up dispatch and save state', align=Align.INLINE)
d.comment(0xA85A, 'Y=&FA: restore 6 workspace bytes', align=Align.INLINE)
d.comment(0xA85C, 'Restore saved workspace byte', align=Align.INLINE)
d.comment(0xA85D, 'Store to osword_flag workspace', align=Align.INLINE)
d.comment(0xA860, 'Next byte', align=Align.INLINE)
d.comment(0xA861, 'Loop until all 6 restored', align=Align.INLINE)
d.comment(0xA863, 'Return from svc_8_osword', align=Align.INLINE)
d.comment(0xA864, 'X = OSWORD index (0-6)', align=Align.INLINE)
d.comment(0xA868, 'Load handler address low byte', align=Align.INLINE)
d.comment(0xA86C, 'Copy 3 bytes (Y=2,1,0)', align=Align.INLINE)
d.comment(0xA86E, 'Load from osword_flag workspace', align=Align.INLINE)
d.comment(0xA870, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0xA888, 'Restore A (OSWORD sub-code)', align=Align.INLINE)
d.comment(0xA88C, 'Other sub-codes: set state = 8', align=Align.INLINE)
d.comment(0xA88E, 'Store service state', align=Align.INLINE)
d.comment(0xA890, 'Return', align=Align.INLINE)
d.comment(0xA891, 'X=0: start of TX control block', align=Align.INLINE)
d.comment(0xA893, 'Y=&10: length of TXCB to save', align=Align.INLINE)
d.comment(0xA895, 'Save current TX control block', align=Align.INLINE)
d.comment(0xA898, 'Load seconds from clock workspace', align=Align.INLINE)
d.comment(0xA89B, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA89E, 'Store BCD seconds', align=Align.INLINE)
d.comment(0xA8A1, 'Load minutes from clock workspace', align=Align.INLINE)
d.comment(0xA8A4, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA8A7, 'Store BCD minutes', align=Align.INLINE)
d.comment(0xA8AA, 'Load hours from clock workspace', align=Align.INLINE)
d.comment(0xA8AD, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA8B0, 'Store BCD hours', align=Align.INLINE)
d.comment(0xA8B3, 'Clear hours high position', align=Align.INLINE)
d.comment(0xA8B5, 'Store zero', align=Align.INLINE)
d.comment(0xA8B8, 'Load day+month byte', align=Align.INLINE)
d.comment(0xA8BB, 'Save for later high nibble extract', align=Align.INLINE)
d.comment(0xA8BC, 'Load day value', align=Align.INLINE)
d.comment(0xA8BF, 'Convert day to BCD', align=Align.INLINE)
d.comment(0xA8C2, 'Store BCD day', align=Align.INLINE)
d.comment(0xA8C5, 'Restore day+month byte', align=Align.INLINE)
d.comment(0xA8C7, 'Mask low nibble (month low bits)', align=Align.INLINE)
d.comment(0xA8C9, 'Convert to BCD', align=Align.INLINE)
d.comment(0xA8CC, 'Store BCD month', align=Align.INLINE)
d.comment(0xA8D0, 'Shift high nibble down', align=Align.INLINE)
d.comment(0xA8D3, '4th shift: isolate high nibble', align=Align.INLINE)
d.comment(0xA8D6, 'Convert year to BCD', align=Align.INLINE)
d.comment(0xA8D9, 'Store BCD year', align=Align.INLINE)
d.comment(0xA8DC, 'Copy 7 bytes (Y=6 down to 0)', align=Align.INLINE)
d.comment(0xA8DE, 'Load BCD byte from workspace', align=Align.INLINE)
d.comment(0xA8E1, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA8E3, 'Next byte down', align=Align.INLINE)
d.comment(0xA8E4, 'Loop for all 7 bytes', align=Align.INLINE)
d.comment(0xA9CF, 'Y=2: copy 2 bytes', align=Align.INLINE)
d.comment(0xA9D1, 'Load station byte', align=Align.INLINE)
d.comment(0xA9D4, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA9D7, 'Loop for bytes 2..1', align=Align.INLINE)
d.comment(0xA9D9, 'Return', align=Align.INLINE)
d.comment(0xA9DD, 'Y=0 for process_all_fcbs', align=Align.INLINE)
d.comment(0xA9DF, 'Close all open FCBs', align=Align.INLINE)
d.comment(0xA9E2, 'Y=2: copy 2 bytes', align=Align.INLINE)
d.comment(0xA9E4, 'Load new station byte from PB', align=Align.INLINE)
d.comment(0xA9E6, 'Store to fs_server_base', align=Align.INLINE)
d.comment(0xA9EA, 'Loop for bytes 2..1', align=Align.INLINE)
d.comment(0xA9EC, 'Clear handles if station matches', align=Align.INLINE)
d.comment(0xA9FB, 'Load FCB flags', align=Align.INLINE)
d.comment(0xA9FE, 'Save flags in Y', align=Align.INLINE)
d.comment(0xA9FF, 'Test bit 1 (FCB allocated?)', align=Align.INLINE)
d.comment(0xAA01, 'No: skip to next entry', align=Align.INLINE)
d.comment(0xAA06, 'Store updated flags', align=Align.INLINE)
d.comment(0xAA09, 'Save in Y', align=Align.INLINE)
d.comment(0xAA0A, 'Does FCB match new station?', align=Align.INLINE)
d.comment(0xAA0D, 'No match: skip to next', align=Align.INLINE)
d.comment(0xAA10, 'Restore flags', align=Align.INLINE)
d.comment(0xAA11, 'Test bit 2 (handle 1 active?)', align=Align.INLINE)
d.comment(0xAA13, 'No: check handle 2', align=Align.INLINE)
d.comment(0xAA15, 'Restore flags', align=Align.INLINE)
d.comment(0xAA16, 'Set bit 5 (handle reassigned)', align=Align.INLINE)
d.comment(0xAA19, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xAA1C, 'Store as handle 1 station', align=Align.INLINE)
d.comment(0xAA1F, 'FCB index', align=Align.INLINE)
d.comment(0xAA20, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xAA22, 'Store as handle 1 FCB index', align=Align.INLINE)
d.comment(0xAA2A, 'Y still holds the saved FCB status -- TYA so we can re-test bit 3 (handle-2 active flag)', align=Align.INLINE)
d.comment(0xAA2B, 'Test bit 3 (handle 2 active?)', align=Align.INLINE)
d.comment(0xAA2D, 'No: check handle 3', align=Align.INLINE)
d.comment(0xAA30, 'Set bit 5', align=Align.INLINE)
d.comment(0xAA33, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xAA36, 'Store as handle 2 station', align=Align.INLINE)
d.comment(0xAA39, 'FCB index', align=Align.INLINE)
d.comment(0xAA3A, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xAA3C, 'Store as handle 2 FCB index', align=Align.INLINE)
d.comment(0xAA45, 'Test bit 4 (handle 3 active?)', align=Align.INLINE)
d.comment(0xAA47, 'No: store final flags', align=Align.INLINE)
d.comment(0xAA49, 'Restore flags', align=Align.INLINE)
d.comment(0xAA4A, 'Set bit 5', align=Align.INLINE)
d.comment(0xAA4C, 'Save updated flags', align=Align.INLINE)
d.comment(0xAA4D, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xAA50, 'Store as handle 3 station', align=Align.INLINE)
d.comment(0xAA53, 'FCB index', align=Align.INLINE)
d.comment(0xAA54, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xAA56, 'Store as handle 3 FCB index', align=Align.INLINE)
d.comment(0xAA73, 'Skip SEC', align=Align.INLINE)
d.comment(0xAA75, 'C=1: PB-to-workspace direction', align=Align.INLINE)
d.comment(0xAA76, 'Workspace offset &17', align=Align.INLINE)
d.comment(0xAA7A, 'Page from RX pointer high byte', align=Align.INLINE)
d.comment(0xAA7C, 'Set ws_ptr_hi', align=Align.INLINE)
d.comment(0xAA7E, 'Y=1: first PB data byte', align=Align.INLINE)
d.comment(0xAA80, 'X=5: copy 5 bytes', align=Align.INLINE)
d.comment(0xAA82, 'C=0: skip PB-to-WS copy', align=Align.INLINE)
d.comment(0xAA84, 'C=1: load from parameter block', align=Align.INLINE)
d.comment(0xAA86, 'Store to workspace', align=Align.INLINE)
d.comment(0xAA88, 'Load from workspace', align=Align.INLINE)
d.comment(0xAA8A, 'Store to parameter block', align=Align.INLINE)
d.comment(0xAA8D, 'Count down', align=Align.INLINE)
d.comment(0xAA8E, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xAA91, 'Load workspace page high byte', align=Align.INLINE)
d.comment(0xAA93, 'Set ws_ptr_hi', align=Align.INLINE)
d.comment(0xAA95, 'Y=1', align=Align.INLINE)
d.comment(0xAA97, 'Set ws_ptr_lo = 1', align=Align.INLINE)
d.comment(0xAA99, 'X=1: copy 2 bytes', align=Align.INLINE)
d.comment(0xAA9B, 'Copy via copy_pb_byte_to_ws', align=Align.INLINE)
d.comment(0xAA9D, 'Y=1: first PB data byte', align=Align.INLINE)
d.comment(0xAA9E, 'Load PB[1]', align=Align.INLINE)
d.comment(0xAAA1, 'Store to (nfs_workspace)+2', align=Align.INLINE)
d.comment(0xAAA3, 'Load PB[2]', align=Align.INLINE)
d.comment(0xAAA5, 'Y=3', align=Align.INLINE)
d.comment(0xAAA6, 'Store to (nfs_workspace)+3', align=Align.INLINE)
d.comment(0xAAA8, 'Reinitialise bridge routing', align=Align.INLINE)
d.comment(0xAAAB, 'Compare result with workspace', align=Align.INLINE)
d.comment(0xAAAD, 'Different: leave unchanged', align=Align.INLINE)
d.comment(0xAAAF, 'Same: clear workspace byte', align=Align.INLINE)
d.comment(0xAAB1, 'Return', align=Align.INLINE)
d.comment(0xAAB2, 'Load protection mask', align=Align.INLINE)
d.comment(0xAAB5, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xAAB8, 'Y=1: PB data offset', align=Align.INLINE)
d.comment(0xAAB9, 'Load new mask from PB[1]', align=Align.INLINE)
d.comment(0xAAC5, 'Y=3: copy 3 bytes', align=Align.INLINE)
d.comment(0xAAC7, 'Load handle byte', align=Align.INLINE)
d.comment(0xAACA, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xAACC, 'Previous byte', align=Align.INLINE)
d.comment(0xAACD, 'Loop for bytes 3..1', align=Align.INLINE)
d.comment(0xAACF, 'Return', align=Align.INLINE)
d.comment(0xAC2E, 'Load bridge response', align=Align.INLINE)
d.comment(0xAC30, 'Negative: bridge responded', align=Align.INLINE)
d.comment(0xAC32, 'Advance retry counter by 8', align=Align.INLINE)
d.comment(0xAC35, 'Positive: retry poll loop', align=Align.INLINE)
d.comment(0xAC37, 'Set response to &3F (OK)', align=Align.INLINE)
d.comment(0xAC39, 'Store to workspace', align=Align.INLINE)
d.comment(0xAC3B, 'Restore saved Y', align=Align.INLINE)
d.comment(0xAC3D, 'Load bridge status', align=Align.INLINE)
d.comment(0xAC40, 'X = bridge status', align=Align.INLINE)
d.comment(0xAC43, 'Status was &FF: return (no bridge)', align=Align.INLINE)
d.comment(0xAC45, 'Return bridge station in A', align=Align.INLINE)
d.comment(0xAC47, 'Compare sub-code with 1', align=Align.INLINE)
d.comment(0xAC49, 'Sub-code >= 1: handle TX request', align=Align.INLINE)
d.comment(0xB0A1, 'Save command line offset', align=Align.INLINE)
d.comment(0xB0A2, 'Push onto stack', align=Align.INLINE)
d.comment(0xB0D8, 'Index 4: threshold 29', align=Align.INLINE)
d.comment(0xB0DB, 'Index 7: threshold 59', align=Align.INLINE)
d.comment(0xBB3A, 'X=&F7: save 9 workspace bytes (&F7..&FF)', align=Align.INLINE)
d.comment(0xBB3C, 'Load workspace byte', align=Align.INLINE)
d.comment(0xBB3F, 'Push fs_options', align=Align.INLINE)
d.comment(0xBB40, 'Next byte', align=Align.INLINE)
d.comment(0xBB41, 'X<0: more bytes to save', align=Align.INLINE)
d.comment(0xBB43, 'Start from FCB slot &0F', align=Align.INLINE)
d.comment(0xBB45, 'Store as current FCB index', align=Align.INLINE)
d.comment(0xBB48, 'Load current FCB index', align=Align.INLINE)
d.comment(0xBB4B, 'Get filter attribute', align=Align.INLINE)
d.comment(0xBB4C, 'Zero: process all FCBs', align=Align.INLINE)
d.comment(0xBB4E, 'Compare with FCB attribute ref', align=Align.INLINE)
d.comment(0xBB51, 'No match: skip this FCB', align=Align.INLINE)
d.comment(0xBB53, 'Save filter attribute', align=Align.INLINE)
d.comment(0xBB54, 'Flush pending data for this FCB', align=Align.INLINE)
d.comment(0xBB58, 'Previous FCB index', align=Align.INLINE)
d.comment(0xBB5B, 'More slots: continue loop', align=Align.INLINE)
d.comment(0xBB5D, 'X=8: restore 9 workspace bytes', align=Align.INLINE)
d.comment(0xBB5F, 'Restore fs_block_offset', align=Align.INLINE)
d.comment(0xBB60, 'Restore workspace byte', align=Align.INLINE)
d.comment(0xBB62, 'Next byte down', align=Align.INLINE)
d.comment(0xBB63, 'More bytes: continue restoring', align=Align.INLINE)
d.comment(0xBC7F, 'Load station for this channel', align=Align.INLINE)
d.comment(0xBC82, 'Save station on stack', align=Align.INLINE)
d.comment(0xBC83, 'Y=0: reset index', align=Align.INLINE)
d.comment(0xBC85, 'Save current FCB context', align=Align.INLINE)
d.comment(0xBC88, 'Restore station from stack', align=Align.INLINE)
d.comment(0xBC89, 'Store station in command buffer', align=Align.INLINE)
d.comment(0xBC8E, 'Save station for later restore', align=Align.INLINE)
d.comment(0xBC8F, 'X=0', align=Align.INLINE)
d.comment(0xBC91, 'Clear function code', align=Align.INLINE)
d.comment(0xBC94, 'Load byte count lo from FCB', align=Align.INLINE)
d.comment(0xBC97, 'Store as data byte count', align=Align.INLINE)
d.comment(0xBC9A, 'Load byte count mid from FCB', align=Align.INLINE)
d.comment(0xBC9D, 'Store as reply command byte', align=Align.INLINE)
d.comment(0xBCA0, 'Load byte count hi from FCB', align=Align.INLINE)
d.comment(0xBCA3, 'Store as load vector field', align=Align.INLINE)
d.comment(0xBCA6, 'Y=&0D: TX command byte offset', align=Align.INLINE)
d.comment(0xBCA8, 'X=5: send 5 bytes', align=Align.INLINE)
d.comment(0xBCAA, 'Send flush request to server', align=Align.INLINE)
d.comment(0xBCAD, 'Restore station from stack', align=Align.INLINE)
d.comment(0xBCAE, 'Y=station for wipe request', align=Align.INLINE)
d.comment(0xBCAF, 'Load saved data byte', align=Align.INLINE)
d.comment(0xBCB2, 'Send close/wipe request to server', align=Align.INLINE)
d.comment(0xBCB5, 'Restore catalog state after flush', align=Align.INLINE)
d.comment(0x945E, 'Y=0: ensure offset starts from beginning of TX command buffer', align=Align.INLINE)
d.comment(0x9460, 'Send the FS command and dispatch the reply', align=Align.INLINE)
d.comment(0x94C9, 'Clear owner-only access bits before parsing', align=Align.INLINE)
d.comment(0x94CC, 'Parse the quoted source filename', align=Align.INLINE)
d.comment(0x94CF, 'Parse access prefix on the source filename', align=Align.INLINE)
d.comment(0x94F1, 'BRA back to loop_copy_rename', align=Align.INLINE)
d.comment(0x9504, 'Save loop index across the access parse', align=Align.INLINE)
d.comment(0x9505, 'Parse access prefix on the second filename', align=Align.INLINE)
d.comment(0x9508, 'Restore loop index', align=Align.INLINE)
d.comment(0x95BE, 'JMP to svc_return_unclaimed (long-distance via this 3-byte trampoline)', align=Align.INLINE)
d.comment(0x9A0E, "A=&C7: OSBYTE 'flush input buffer'", align=Align.INLINE)
d.comment(0x9A10, 'Tail-call OSBYTE with X=0/Y=0', align=Align.INLINE)
d.comment(0xA0FE, 'Write CMOS RAM byte (Y) to byte index (X)', align=Align.INLINE)
d.comment(0xA4EC, 'Update hazel_fs_lib_flags with the result', align=Align.INLINE)
d.comment(0xA594, 'Test hazel_fs_lib_flags bits 6 / 7', align=Align.INLINE)
d.comment(0xA597, 'Either bit set: this is an invalid command path', align=Align.INLINE)
d.comment(0xA599, 'Otherwise finalise and return', align=Align.INLINE)
d.comment(0xA59C, 'A=&0B: FSCV reason 11 (filing-system change)', align=Align.INLINE)
d.comment(0xA59E, 'Tail-call FSCV', align=Align.INLINE)
d.comment(0xA5DF, 'Copy parsed arg to TX buffer with X=0', align=Align.INLINE)
d.comment(0xA6DD, "Mark this path as 'success' for the caller", align=Align.INLINE)
d.comment(0xA6DE, 'Load TX result code from hazel_txcb_result', align=Align.INLINE)
d.comment(0xA6E1, 'Store as hazel_fs_flags', align=Align.INLINE)
d.comment(0xA9CC, 'Ensure NFS is currently the selected FS', align=Align.INLINE)
d.comment(0xA9DA, 'Ensure NFS is currently the selected FS', align=Align.INLINE)
d.comment(0xAA25, 'A=2: fs_flags bit 1 mask', align=Align.INLINE)
d.comment(0xAA27, 'Clear fs_flags bit 1', align=Align.INLINE)
d.comment(0xAA3F, 'A=4: fs_flags bit 2 mask', align=Align.INLINE)
d.comment(0xAA44, 'Y still holds the saved FCB status -- TYA so we can re-test bit 4 (handle-3 active flag)', align=Align.INLINE)
d.comment(0xAA41, 'Clear fs_flags bit 2', align=Align.INLINE)
d.comment(0xAAC2, 'Ensure NFS is currently the selected FS', align=Align.INLINE)
d.comment(0xAAD0, 'Ensure NFS is currently the selected FS', align=Align.INLINE)
d.comment(0xAC26, "A=&13: OSBYTE 'wait for VSYNC'", align=Align.INLINE)
d.comment(0xAC2B, "Restore caller's X", align=Align.INLINE)
d.comment(0xAC4C, 'Ensure NFS is currently the selected FS', align=Align.INLINE)
d.comment(0xAC4F, 'Pop saved A from the stack frame', align=Align.INLINE)
d.comment(0xB0FE, 'Set OS text pointer and FS-options transfer ptr', align=Align.INLINE)
d.comment(0xB101, 'Y=0: TX-buffer offset for the first byte', align=Align.INLINE)
d.comment(0xB16B, 'Read hazel_txcb_type (FS reply opcode)', align=Align.INLINE)
d.comment(0xB16E, 'Non-zero (private library): take the public-label branch', align=Align.INLINE)
d.comment(0xB179, 'Non-zero: branch to cat_after_label_print', align=Align.INLINE)
d.comment(0xB185, 'Read hazel_fs_lib_flags', align=Align.INLINE)
d.comment(0xB1A5, 'Read hazel_fs_flags', align=Align.INLINE)
d.comment(0xB1B1, 'Look up option-string offset for index X', align=Align.INLINE)
d.comment(0xB1B4, 'Look up option byte at the resolved offset', align=Align.INLINE)
d.comment(0xBB39, 'Save Y across the body', align=Align.INLINE)
d.comment(0xBC8D, 'Save Y again for the next iteration', align=Align.INLINE)
import sys
ir = d.disassemble()
output = str(ir.render('beebasm', boundary_label_prefix='pydis_', byte_column=True, byte_column_format='py8dis', default_byte_cols=12, default_word_cols=6))
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / 'anfs-4.21_variant_1.asm'
output_filepath.write_text(output, encoding='utf-8')
print(f'Wrote {output_filepath}', file=sys.stderr)
json_filepath = _output_dirpath / 'anfs-4.21_variant_1.json'
json_filepath.write_text(str(ir.render('json')), encoding='utf-8')
print(f'Wrote {json_filepath}', file=sys.stderr)
