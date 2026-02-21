# Changes from NFS 3.34 to NFS 3.34B

NFS 3.34B is a minor revision of Acorn NFS 3.34 for the BBC Micro. The two
8 KB ROMs are 98.7% identical at the opcode level.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 8192 bytes   |
| Identical bytes at same offset  | 2963 (36.2%) |
| Byte-level similarity           | 96.5%        |
| Opcode-level similarity         | 98.7%        |
| Full instruction similarity     | 93.0%        |
| Instructions (3.34 / 3.34B)     | 4037 / 4045  |
| Structural change blocks        | 22           |

The low identical-byte count (36.2%) is misleading: most of the byte
differences are address operands shifted by the 1-byte version string
insertion. The opcode-level similarity (98.7%) reflects the true structural
similarity.

## ROM header

The ROM headers are identical:

| Field             | Value  |
|-------------------|--------|
| Title             | "NET"  |
| ROM type          | $82    |
| Language entry    | $8099  |
| Service entry     | $80AF  |
| Binary version    | $03    |
| Copyright         | "(C)ROFF" |

There is no version string field in the header. The version number appears
as an inline string printed by the `*HELP` handler.

## Changes

### 1. Version string: "3.34" to "3.34B"

The ROM identification string printed by `*HELP` (at $81C4 in 3.34) changed
from "3.34" to "3.34B". This inserts one byte ("B") into the ROM image,
shifting all subsequent addresses by +1.

### 2. Deleted RTS at end of page 6 relocated block

An RTS instruction at $964B (the final byte of the page 6 Tube host code
block, runtime address $06FF) was removed. This 1-byte deletion compensates
for the 1-byte version string insertion, keeping the ROM at exactly 8192
bytes and leaving all addresses from $964C onwards unchanged.

### 3. Tube WRCH register: R1 to R4

The most significant functional change. Five instructions in the Tube host
code were modified to use Tube register R4 ($FEE6/$FEE7) instead of R1
($FEE0/$FEE1) for WRCH character I/O:

| Runtime addr | 3.34            | 3.34B           | Routine              |
|--------------|-----------------|-----------------|----------------------|
| $003A        | BIT $FEE0       | BIT $FEE6       | tube_main_loop       |
| $003F        | LDA $FEE1       | LDA $FEE7       | tube_handle_wrch     |
| $004A        | BIT $FEE0       | BIT $FEE6       | tube_poll_r2         |
| $0527        | BIT $FEE0       | BIT $FEE6       | tube_poll_r4_wrch    |
| $052C        | LDA $FEE1       | LDA $FEE7       | tube_poll_r4_wrch    |

These are all in the relocated Tube host code (BRK handler block and page 5
block), which is copied from ROM to RAM during initialisation.

**Why this matters:** The BBC Micro Tube ULA has four register pairs:

- R1 ($FEE0/$FEE1): events and escape signalling
- R2 ($FEE2/$FEE3): command bytes and general data transfer
- R4 ($FEE6/$FEE7): one-byte transfers

In NFS 3.34, R1 was overloaded: it handled both WRCH character data and
escape/event signalling. NFS 3.34B moves WRCH polling and data reads to R4
(the one-byte transfer register), which is a better semantic fit for
single-character transfers. The escape check routine ($06E2), event handler
($06E8), and the R1 send routine ($06F7) remain on R1, preserving R1's
role as the escape/event channel.

This is a protocol refinement that separates character I/O from
escape/event signalling, reducing the potential for contention on R1.

### 4. Shifted address operands

All code from $81C8 to $964A in 3.34 appears at $81C9 to $964B in 3.34B,
with absolute address operands adjusted accordingly. This accounts for the
bulk of the byte-level differences but represents no functional change.

## Address map

```
3.34 Range       3.34B Range      Offset
$8000-$81C7  ->  $8000-$81C7      +0       Identical
  (n/a)      ->  $81C8            n/a      Inserted "B" byte
$81C8-$964A  ->  $81C9-$964B      +1       Shifted
$964B        ->  (deleted)        n/a      RTS removed
$964C-$9FFF  ->  $964C-$9FFF      +0       Identical
```

Relocated code block ROM sources (all +1):

| Block        | 3.34   | 3.34B  | Runtime       | Size      |
|--------------|--------|--------|---------------|-----------|
| BRK handler  | $9307  | $9308  | $0016-$0076   | 97 bytes  |
| Page 4       | $934C  | $934D  | $0400-$04FF   | 256 bytes |
| Page 5       | $944C  | $944D  | $0500-$05FF   | 256 bytes |
| Page 6       | $954C  | $954D  | $0600-$06FF   | 256 bytes |
