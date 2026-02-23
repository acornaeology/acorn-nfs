# Changes from NFS 3.34B to NFS 3.35D

NFS 3.35D is a substantial revision of Acorn NFS 3.34B for the BBC Micro. The
two 8 KB ROMs are 87.4% identical at the opcode level, with 161 structural
change blocks reflecting significant new functionality and protocol changes.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 8192 bytes   |
| Identical bytes at same offset  | 272 (3.3%)   |
| Byte-level similarity           | 83.0%        |
| Opcode-level similarity         | 87.4%        |
| Full instruction similarity     | 75.8%        |
| Instructions (3.34B / 3.35D)    | 4045 / 4019  |
| Structural change blocks        | 161          |

The very low identical-byte count (3.3%) reflects the extensive address
shifting caused by multiple code insertions and deletions throughout the ROM.
The opcode-level similarity (87.4%) is a better measure of structural
similarity but still shows considerably more change than the 3.34 to 3.34B
transition (98.7%).

## ROM header

| Field             | 3.34B  | 3.35D  |
|-------------------|--------|--------|
| Title             | "NET"  | "NET"  |
| ROM type          | &82    | &82    |
| Binary version    | &03    | &03    |
| Copyright         | "(C)ROFF" | "(C)ROFF" |
| Language entry    | &8099  | &80D4  |
| Service entry     | &80AF  | &80EA  |

The language and service entry points have moved due to new code inserted
before them (the station number parser at &807D-&80B3 and the per-ROM disable
check at &80EA-&80F3). All other header fields are unchanged.

## Changes

### 1. Version string: "3.34B" to "3.35d"

The ROM identification string printed by `*HELP` (at &81BF in 3.34B, &81FA in
3.35D) changed from `"NFS 3.34B"` to `"NFS 3.35d"`. The revision letter is
now lowercase, an unusual convention for Acorn ROMs.

### 2. Command-line station number parsing

Entirely new code at &807D-&80B3 adds two capabilities to the `*NET` command:

**Station number syntax:** `*NET 123` or `*NET 123.45` directly sets the
fileserver station and network numbers (stored at &0E00 and &0E01). In 3.34B,
changing the fileserver required the `*I AM` command; `*NET` only dispatched
numbered sub-commands (`*NET1` through `*NET4`).

The parser at &8088 calls the existing `parse_decimal` routine (at &85FD)
twice: once for the station number and, if a separator is found, again for
the network number. It handles both `station` and `station.network` forms.

**Colon command continuation:** If a colon (`:`) is found in the command text,
the code echoes the colon and reads interactive input character by character
via OSRDCH (&80A7), appending it to the command buffer. After CR is received,
the combined text is forwarded to the fileserver. This enables constructs like
`*NET 123:command` where the text after the colon is typed interactively.

### 3. Per-ROM disable flag

The service handler at &80EA gains a new guard. Before dispatching any service
call, 3.35D reads the byte at `&0DF0+X` (where X is the ROM bank number,
within the NFS workspace page at &0D00-&0DFF). If bit 7 of that byte is set,
the ROM returns immediately without processing the service call:

| Runtime addr | Instruction            | Purpose                           |
|--------------|------------------------|-----------------------------------|
| &80EA        | PHA                    | Save service number               |
| &80EB        | LDA &0DF0,X           | Read per-ROM disable flag         |
| &80EE        | ASL A                  | Shift bit 7 into carry            |
| &80EF        | PLA                    | Restore service number            |
| &80F0        | BMI c80f4              | If &FE/&FF, skip disable check    |
| &80F2        | BCS return_1           | If carry set, ROM is disabled     |

Service calls &FE (Tube init) and &FF (full reset) bypass this check, since
they are needed regardless of the disable state. This provides a mechanism
for the MOS or another ROM to selectively disable NFS without removing the
ROM physically.

### 4. Table-driven vector initialisation

The hardcoded LDA/STA pairs in 3.34B's `init_vectors_and_copy` (at &80C8)
have been replaced by a data-driven loop at &810D-&8123. The loop reads four
triplets from a table at &8177, each containing (low byte, high byte, vector
offset), and stores the 16-bit values at &0200+offset:

| Vector | Address | 3.34B value | 3.35D value |
|--------|---------|-------------|-------------|
| BRKV   | &0202   | &0016       | &0016       |
| WRCHV  | &020E   | &051C       | &051C       |
| RDCHV  | &0210   | &04E7       | &04E7       |
| EVNTV  | &0220   | &06E8       | &06E5       |

The EVNTV target changed from &06E8 to &06E5, reflecting a 3-byte shift in
the page 6 event handler code. All other vector targets are unchanged.

### 5. Tube WRCH register: R4 back to R1

The most significant Tube protocol change, and a reversal of the 3.34 to
3.34B change. Five instructions in the Tube host code were modified to use
Tube register R1 (&FEE0/&FEE1) instead of R4 (&FEE6/&FEE7) for WRCH
character I/O:

| Runtime addr | 3.34B           | 3.35D           | Routine                |
|--------------|-----------------|-----------------|------------------------|
| &003A        | BIT &FEE6       | BIT &FEE0       | tube_main_loop         |
| &003F        | LDA &FEE7       | LDA &FEE1       | tube_handle_wrch       |
| &004A        | BIT &FEE6       | BIT &FEE0       | tube_poll_r2           |
| &0527        | BIT &FEE6       | BIT &FEE0       | tube_poll_r4/r1_wrch   |
| &052C        | LDA &FEE7       | LDA &FEE1       | tube_poll_r4/r1_wrch   |

The routine at &0527 is labeled `tube_poll_r4_wrch` in 3.34B (polling R4) and
`tube_poll_r1_wrch` in 3.35D (polling R1), reflecting the register reversion.

These are all in the relocated Tube host code (BRK handler block and page 5
block), which is copied from ROM to RAM during initialisation.

**History:** In NFS 3.34, WRCH polling used R1. NFS 3.34B moved it to R4
(the one-byte transfer register). NFS 3.35D reverses this, returning WRCH
to R1. The `tube_send_r4` routine continues to use R4 for outbound data in
all three versions.

The BBC Micro Tube ULA register pairs:

- R1 (&FEE0/&FEE1): events, escape signalling, and (in 3.34/3.35D) WRCH
- R2 (&FEE2/&FEE3): command bytes and general data transfer
- R4 (&FEE6/&FEE7): one-byte transfers

### 6. GSINIT/GSREAD filename parsing for FSCV

In 3.34B, FSCV codes 2 (`*/`), 3 (unrecognised `*` command), and 4 (`*RUN`)
all dispatch to the same handler (`fscv_star_handler`). In 3.35D, codes 2 and
4 now dispatch through a new wrapper at &8DC7 (`sub_c8dc7`) which calls
`parse_filename_gs` first, using the MOS GSINIT/GSREAD API (&FFC2/&FFC5) to
parse the filename into the command buffer at &0E30 before forwarding it to
the fileserver. A second GSINIT/GSREAD call at &8DE2 consumes the parsed
filename and advances past trailing spaces.

This adds support for quoted filenames and `|`-escaped special characters in
`*/` and `*RUN` commands. The `*` (unrecognised command) path via FSCV code 3
still bypasses this parsing, passing the raw command text to the fileserver.

3.34B contains one GSINIT/GSREAD call site (at &86A6); 3.35D contains two
(at &86C8 and &8DE2).

### 7. Table-driven Tube address claim

The `tube_addr_claim` routine in the page 4 relocated code was restructured.
In 3.34B, a series of compare-and-branch instructions selects the appropriate
Tube control register value based on the claim type. In 3.35D, this is
replaced by a lookup table containing the 8 possible control register values,
indexed by the claim type in X. The lookup table approach is more compact and
easier to extend.

### 8. OSBYTE &C6 replaces &C7 in error handler

In the error handling path (3.34B: &83E8, 3.35D: &8432), the OSBYTE call
changed from &C7 (read/write `*SPOOL` file handle) to &C6 (read/write `*EXEC`
file handle). The purpose is to check whether the currently open EXEC or SPOOL
file is using the same handle as the one that just errored, and if so, to
close it. 3.35D checks the EXEC handle instead of the SPOOL handle, which may
fix a bug where errors during an `*EXEC` file were not properly detected.

### 9. Catalogue formatting

Several small changes to the `*CAT` display formatting:

- Padding spaces after the station number display are now embedded directly in
  the inline print string rather than using a separate `print_spaces` call,
  saving 3 bytes per occurrence.
- The "Option" label gains 4 leading spaces (`"    Option "` vs `"Option "`),
  improving column alignment.
- Directory and library name printing uses a different subroutine path.
- The entries-per-line calculation uses a pre-set value rather than a runtime
  division loop.

### 10. Workspace variable relocation

Several workspace variables moved to different addresses:

| Label              | 3.34B address | 3.35D address |
|--------------------|---------------|---------------|
| `nfs_temp`         | &CD           | &A8           |
| `rom_svc_num`      | &CE           | &A9           |
| `tx_clear_flag`    | &0D3A         | &0D62         |
| Per-ROM disable flag | (none)        | &0DF0+X       |

### 11. Shifted address operands

All code throughout the ROM has shifted addresses due to the cumulative effect
of insertions and deletions. Unlike the 3.34 to 3.34B transition (a uniform
+1 shift from &81C8 onwards), the shifts in 3.35D are non-uniform, varying by
region as multiple code blocks were inserted, deleted, and reorganised.

## Address map

The address mapping between 3.34B and 3.35D is non-linear, with 161 change
blocks. Key entry point mappings:

| Function              | 3.34B   | 3.35D   | Offset  |
|-----------------------|---------|---------|---------|
| Language entry        | &8099   | &80D4   | +&3B    |
| Service entry         | &80AF   | &80EA   | +&3B    |
| Init vectors          | &80C8   | &810D   | +&45    |
| Version string        | &81BF   | &81FA   | +&3B    |
| Service dispatch      | &80B7   | &8150   | +&99    |

Relocated code block ROM sources (all +&12):

| Block        | 3.34B  | 3.35D  | Runtime       | Size      |
|--------------|--------|--------|---------------|-----------|
| BRK handler  | &9308  | &931A  | &0016-&0076   | 97 bytes  |
| Page 4       | &934D  | &935F  | &0400-&04FF   | 256 bytes |
| Page 5       | &944D  | &945F  | &0500-&05FF   | 256 bytes |
| Page 6       | &954D  | &955F  | &0600-&06FF   | 256 bytes |
