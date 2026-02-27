# Changes from NFS 3.62 to NFS 3.65

NFS 3.65 is the final release of Acorn NFS. Compared to 3.62, the two ROMs
are 96.8% identical at the opcode level (34 change blocks). Most code shifts
uniformly due to the shorter ROM title, but there are two significant
functional changes to the Econet hardware handling.

## ROM header

| Field             | 3.62    | 3.65    |
|-------------------|---------|---------|
| Language entry    | &80E1   | &80DD   |
| Service entry     | &80F7   | &80F3   |
| Copyright offset  | &10     | &0C     |
| Binary version    | &83     | &03     |
| Title             | "    NET" | "NET" |

The title was shortened from 7 characters (4 leading spaces + "NET") to 3,
saving 4 bytes and shifting all subsequent header data and code addresses.

## NOP padding removed (14 bytes saved)

**Service handler entry (9 NOPs at &80F7 in 3.62).**
The 9 NOP instructions described as "bus settling time for ADLC probe" were
removed entirely. The service handler now begins immediately with PHA / CMP.

**svc_4_star_command padding (5 NOPs at &81B0 in 3.62).**
Five NOP bytes between return_2 and svc_4_star_command were removed.
The dispatch table was updated to target the handler directly.

## *EX trampoline deleted (11 bytes saved)

In 3.62, the *EX command table entry dispatched to `ex_trampoline` at &9FB5,
which disambiguated *EX from *EXEC by checking whether the next character
after "EX" was printable (>= &21). If so, the command was forwarded to the
fileserver as *EXEC; otherwise it was handled locally as *EX.

In 3.65, the trampoline is removed. Instead, the command table entry for "EX"
uses a `}` (ASCII &7D) terminator byte. Since `}` cannot appear in a valid
command, the MOS command parser itself rejects *EXEC before reaching the
handler. The dispatch address points directly to `ex_handler` at &8C4F.

## print_hex moved inline (~&9F9D to ~&8DCA)

The `print_hex` and `print_hex_nibble` subroutines were at &9F9D-&9FB4 near
the end of the ROM in 3.62. In 3.65 they are inserted inline at &8DCA,
closer to their callers.

The algorithm was also simplified: the nibble-to-hex conversion now uses
`ORA #&30` / `CMP #&3A` instead of `CMP #&0A` / `ADC #&30`, removing a
carry dependency. The `SEC` return convention was dropped.

## Self-modifying INTOFF mechanism (STA &0D1C)

This is the most significant functional change. In 3.62, NMIs were disabled
by reading the Econet station ID register (`BIT &FE18`), which has the
side-effect of clearing the NMI enable latch. In 3.65, a new RAM workspace
byte at &0D1C is used as a self-modifying opcode within the NMI dispatch
shim at &0D00. Writing different values to &0D1C switches between
NMI-enabled and NMI-disabled states:

- `LDA #&40` / `STA &0D1C` disables NMI processing
- `LDA #&2C` / `STA &0D1C` re-enables NMI processing

This pattern appears in five locations:
1. INACTIVE polling loop (`test_inactive_retry`)
2. After CTS not detected (`inactive_retry`)
3. TX prepare (after CTS detected)
4. wait_idle_and_reset

The change suggests Acorn found a timing or reliability issue with the
hardware-based NMI disable. The self-modifying code approach atomically
controls NMI processing in RAM, providing a more robust mechanism.

## ADLC CR1 reset before TX (STX &FEA0)

A new CR1 write was added to the TX prepare path:

```
LDX #&C0     ; CR1 = &C0: AC | RX_RESET
STX &FEA0    ; Write to ADLC CR1
```

This resets the ADLC receiver before beginning transmission, preventing
potential receive-during-transmit issues. In 3.62, TX prepare wrote only
to CR2 (&E7).

## NMI handler install changes

Several NMI handler install calls changed from the one-byte
`install_nmi_handler` (which only sets the JMP low byte, assuming the
high byte is already correct) to the two-byte `set_nmi_vector` (which sets
both bytes). This was required because some handlers shifted across a page
boundary (&97xx to &98xx), making the one-byte install insufficient.

## Relocated code changes

The four relocated blocks shift +3 bytes in ROM source address:

| Block     | 3.62 source | 3.65 source | Runtime  |
|-----------|-------------|-------------|----------|
| Workspace | &9321       | &9324       | &0016    |
| Page 4    | &9362       | &9365       | &0400    |
| Page 5    | &9462       | &9465       | &0500    |
| Page 6    | &9562       | &9565       | &0600    |

Workspace, page 4 and page 5 are byte-identical. Page 6 has changes
from runtime address &06CE: the trampoline JMPs shifted, and 29 bytes
of &FF padding were inserted before them, pushing the trampolines from
runtime &06CE to &06EB.

## Free space

Total free space increased from 17 bytes (3.62) to approximately 43 bytes
(3.65), distributed as 29 bytes of &FF padding at &9633-&964F and 14 bytes
at the end of the ROM.
