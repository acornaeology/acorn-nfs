# Changes from ANFS 4.18 to ANFS 4.21 (variant 1)

ANFS 4.18 was the last ANFS to run on a Model B. ANFS 4.21
(variant 1) is the first to run on a Master 128 – and the first to
*refuse* to run on anything else. Between the two ROMs sits Acorn's
biggest 8-bit hardware reshuffle, and ANFS's rewrite is shaped by it
through and through.

The two 16 KB sideways ROMs share 86.7 % of their opcode structure
but only 1.7 % of their bytes match at the same offset. Almost every operand
has shifted, because the workspace has moved off-page and the ROM
title gained a few bytes. The interesting changes lie underneath
that arithmetic: the Model B's constraints – no hidden RAM, plain
6502 instruction set, direct VIA access – pushed 4.18 into
workarounds the Master makes unnecessary, and 4.21 takes them all
apart.

## The host-OS gate

The first thing the 4.21 service handler does, before dispatching
anything, is ask the OS what it's running on. Pre-Master OSes, and
the Master Compact, are sent away unclaimed:

| OS version | Hardware | Action |
|---|---|---|
| 1.x | BBC Model B | reject |
| 2.x | BBC Model B+ | reject |
| 3.x | Master 128 (MOS 3.20 / 3.50) | proceed |
| 4.0 | Master Econet Terminal | proceed |
| 5.0 | Master Compact | reject |

A reject silently returns service unclaimed, so MOS keeps looking
for a filing system without ANFS interfering with anything it
shouldn't. There was no equivalent gate in 4.18 –
[`service_handler`](address:8A15@4.18) dispatched directly. The
service entry-point itself shifts from `&8A15` (4.18) to
[`&8A54`](address:8A54), most of which is the gate code.

"Variant 1" isn't part of the official name – the ROM image itself
just calls itself "Acorn ANFS 4.21". Several distinct ROM images
claiming to be ANFS 4.21 have turned up over the years; this
project labels its first specimen "variant 1" to keep them apart.
The relationship between the variants – their relative ordering,
if any – is not known.

## HAZEL: hidden RAM under the OS

The structural change with the broadest consequences is the move
from MOS workspace in main RAM to **HAZEL**, the Master 128's 8 KB
of hidden RAM at `&C000`–`&DFFF`. HAZEL sits underneath the MOS VDU drivers in the
address map and is reached by setting bit Y (bit 3) of the ACCCON
register at [`&FE34`](address:FE34) – when ACCCON.Y is set, reads
and writes to `&C000`–`&DFFF` go to HAZEL instead of the OS ROM.
Filing systems are HAZEL's intended client; ANFS occupies the
first 768 bytes (`&C000`–`&C2FF`).

The 4.18 → 4.21 workspace mapping is uniform: every byte that lived
in the page-`&0E`–`&10` main-RAM area shifts by `+&B200`.

| Workspace data         | 4.18    | 4.21                        |
|------------------------|---------|-----------------------------|
| Parse buffer           | `&0E30` | `&C030`                     |
| TX buffer base         | `&0F00` | `&C100`                     |
| FS lib flags           | `&1071` | [`&C271`](address:C271)     |
| FCB attributes         | `&10C9` | `&C2C9`                     |
| Saved catalogue buffer | `&10D9` | [`&C2D9`](address:C2D9)     |

In 4.18 the Model B had no spare RAM for a 768-byte filing-system
workspace. The ROM coped by stealing pages 4–6 of main RAM and
populating them on first selection from a copy loop in the main-ROM
tail – about 130 bytes of code around
[`&BE94`](address:BE94@4.18). In 4.21 that whole apparatus is gone:
the workspace is just *there* whenever ACCCON.Y is set, no copy
required.

## The `hazel_minus_2` trick

The 6502's indexed addressing modes are cheap, but there is no
`STA (zp),Y` – you need a zero-page pointer pair to do indirect-
indexed writes. ANFS routines that copy small blocks through HAZEL
frequently want to start at `&C000`, but a typical zero-page layout
already has every byte spoken for, and burning two more for "the
HAZEL base" is wasteful when only `Y` ever varies.

The 4.21 ROM solves this by putting the labels *just below* HAZEL.
The ROM's last 64 bytes are `&FF` padding (read-only and otherwise
unused), but two of those bytes are deliberately labelled:

```python
hazel_minus_2 = &BFFE
hazel_minus_1 = &BFFF
```

Now `STA hazel_minus_2,Y` with `Y ≥ 2` lands at `&BFFE + Y ≥
&C000` – inside HAZEL. The instruction is three bytes, no zero-page
pointer needed, no setup. Routines like `loop_copy_fs_ctx` use the
pattern with just `LDA src,X / STA hazel_minus_2,Y`; the loop's
`CPY` guard simply stops `Y` before it could underflow back into
the ROM tail.

It's a piece of code economy that becomes possible only because the
ROM author controls both endpoints – the data layout in the tail
*and* the access patterns in the routines. A few bytes of `&FF`
padding are invisible to the user; what matters is that the labels
at the right offsets exist so the assembler can resolve
`hazel_minus_2,Y` to `&BFFE,Y`.

## 65C02 instructions

Because the host-OS gate guarantees a Master, the assembler runs in
65C02 mode. About a dozen new instructions show up across the ROM:

- **`PHX` / `PHY` / `PLX` / `PLY`** push and pull X and Y directly.
  4.18 prologues that needed to save both registers wrote
  `TXA / PHA / TYA / PHA`, costing 8 bytes and 14 cycles for the
  round-trip; the 65C02 form does the same in 4 bytes and 6 cycles.
  See [`copy_fs_cmd_name`](address:9463) or
  [`parse_fs_ps_args`](address:A3C4) for typical examples.
- **`BRA`** is an unconditional branch that costs 1 byte and 1 cycle
  less than `JMP abs` (within ±127 bytes).
- **`STZ`** stores zero without needing a register; it replaces
  `LDA #0 / STA zp` with a single 2-byte instruction. The
  disassembly has more than thirty STZ sites, and the
  `LDA #0`-then-store sequence is nearly extinct.
- **`TSB`** and **`TRB`** test-and-set / test-and-reset bits in
  memory atomically. Used in the shadow-VIA path described below,
  where read-modify-write needs to be a single instruction so an
  interrupt can't see a half-updated flag.
- **`BIT abs,X`** is indexed BIT, used in the dispatch tails.

The savings aren't dramatic per call site, but they accumulate. The
4.21 ROM has 81 more instructions than 4.18 (8270 vs 8189) while
implementing strictly more functionality – because the new
instructions paid for the new code.

## Interrupts, deferred work, and the shadow VIA

Master MOS owns the System VIA. Its auxiliary control register
(ACR) and shift register (SR) are touched by the OS during VDU
work, sound, and keyboard polling. A filing system that needed
shift-register-driven I/O on the Model B could write the VIA
directly; on the Master it can't, because MOS will overwrite its
settings.

ANFS 4.21 introduces a **shadow VIA pair**: two workspace bytes
that ANFS treats as the canonical state of ACR (mirrored at
`&0D68`) and SR (`&0D69`). [`setup_sr_tx`](address:8512) updates
the shadow; the live VIA gets reconciled inside the Master's IRQ
dispatch path. 4.18 wrote ACR and SR directly; in 4.21 those
direct writes are simply gone.

The IRQ entry [`svc5_irq_check`](address:8028) lives at the same
address `&8028` in both ROMs, but the body is unrecognisable:

```
4.18:                         4.21:
    LDA &FE4D    ; VIA IFR        LDY &0D65    ; deferred-work flag
    AND #&02     ; SR IRQ?        BEQ no_deferred
    BEQ no_sr_irq                 TRB ACCCON   ; release shadow-RAM
    ...                           STZ &0D65    ; consume the flag
                                  BMI dispatch_svc5
                                  LDA #&FE     ; fire RX event
                                  ...
```

The deferred-work flag at `&0D65` is set by IRQ and NMI paths when
they spot work that can't be done in the interrupt context –
because MOS may be holding the VIA, or shadow RAM is paged the
wrong way for the address the handler wanted to touch. The next
service-handler entry, which runs with the interrupt cleared and
the OS in a known state, consumes the flag, restores ACCCON, and
dispatches the deferred work. It's the standard *raise a flag in
the ISR, drain it in non-IRQ code* pattern, but the architectural
reason for it is explicit: the Master's memory paging makes some
operations unsafe inside the ISR.

The Master's `&27` service call ("Reset has occurred") follows the
same discipline. ANFS uses it specifically to claim NMIs for
Econet receive – because the Master MOS no longer offers workspace
on a soft `BREAK`, a 4.18 lifecycle assumption that 4.21 has to
abandon.

## OSWORD &13: clean errors instead of quiet zeroes

OSWORD `&13` is ANFS's API surface – clients use it to read and
write the saved file-server station, the receive-channel handles,
the bridge state, and so on. In 4.18 each sub-handler began with a
`BIT &0D6C / BPL <return>` that quietly bailed if ANFS wasn't the
active filing system, returning a zeroed parameter block. A client
that expected a station back and got `0.0` had no way to tell
whether the FS was inactive or whether the FS was *on* station
`0.0`.

4.21 wraps every OSWORD `&13` sub-handler in an
[`ensure_fs_selected`](address:8B4D) prologue. It tests bit 7 of
`fs_flags` and, if clear, calls [`cmd_net_fs`](address:9776) to
make ANFS the active filing system. On selection failure it raises
a `'net checksum'` error (`&AA`).

The new behaviour is more aggressive than the old quiet-zero, but
it's more honest: the client either gets real data or a real
error, never a confusable success with a misleading payload.

## Protection moves into CMOS

`*PROT` and `*UNPROT` in 4.18 took attribute keywords (`L`, `W`,
`R`, `WR`, …) and accumulated the parsed bits into a workspace
mask. The keyword-parser table and the per-keyword bit-encoding
ran fifty-odd bytes; the parser body itself was more. The mask was
lost on `BREAK`.

[`cmd_prot`](address:B6D2) and [`cmd_unprot`](address:B6D6) in
4.21 take **no arguments**. They're each a four-instruction toggle
of bit 6 of CMOS RAM byte `&11` (the Master's Econet station-flags
byte) via OSBYTE `&A1` (read CMOS) and OSBYTE `&A2` (write CMOS),
with the new value mirrored into the shadow ACR/SR pair through
`set_via_shadow_pair`:

```6502
cmd_prot:
    LDA #&11                ; CMOS byte: station flags
    JSR osbyte_a1           ; read into Y
    TYA
    ORA #&40                ; set bit 6
    JSR osbyte_a2           ; write back
    JMP set_via_shadow_pair
```

Storing the state in CMOS rather than volatile RAM means it
survives `BREAK`, soft reset, and power-cycle – ANFS doesn't have
to manage persistence at all. The keyword parser and its encoding
table are gone. What's left is a routine the user could read and
understand in thirty seconds.

## What 4.21 sheds

Some 4.18 features simply don't appear in 4.21, because the Master
MOS already provides them or because the wrapper was vestigial:

- **`*CLOSE`, `*PRINT`, `*TYPE`** are handled natively by Master
  MOS, so the ANFS wrappers (4.18's `cmd_close`, `cmd_print`,
  `cmd_type`) are gone. The strings *Close*, *Print*, *Type* don't
  appear anywhere in the 4.21 ROM.
- **`read_paged_rom`** at [`&8AA0`](address:8AA0@4.18) used OSBYTE
  `&FD` to fetch the current ROM number; 4.21 reads `&028D`
  directly, and the `JSR &FFB9` that drove the 4.18 helper is gone
  too.
- **The relocation copy loop** at
  [`&BE94`](address:BE94@4.18) – the 130-byte routine that
  populated the 4.18 pages 4–6 workspace on first selection – has
  no counterpart, because HAZEL needs no initialisation of that
  kind.
- **The `*PROT` / `*UNPROT` keyword parser** described above.
- **The per-handler `BIT abs / BPL` early-returns** in OSWORD `&13`
  sub-handlers, replaced by the unified `ensure_fs_selected`
  prologue.

Together these account for several hundred bytes – roughly the
budget that the host-OS gate, the 65C02-prologue rewrites, the
shadow-VIA path, the deferred-work IRQ machinery, and
`ensure_fs_selected` reclaim.

## In sum

4.21 v1 is a leaner client running on a richer host. The Model B's
constraints pushed 4.18 into workarounds: relocated workspace
pages, hand-rolled push/pop sequences, direct VIA writes, persistent
state held in volatile RAM. The Master 128 dissolves all of those
constraints, and 4.21 takes them apart in favour of HAZEL workspace,
65C02 push/pull, shadow-VIA reconciliation through the IRQ path,
and CMOS-backed configuration. What's left is a ROM that's tightly
bound to its host – which is exactly why it gates so aggressively
against being run anywhere else.
