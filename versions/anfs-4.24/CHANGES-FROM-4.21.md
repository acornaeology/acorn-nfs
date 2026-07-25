# Changes from [ANFS](glossary:nfs) 4.21 (variant 1) to ANFS 4.24

ANFS 4.24 is the next [Master 128](glossary:master-128) ANFS after 4.21 (variant 1). Both are
[65C02](glossary:65c02) [ROM](glossary:rom)s that keep their filing-system workspace in [HAZEL](glossary:hazel) hidden RAM
at `&C000`–`&C2FF`, so 4.24 inherits the whole Master-128 architecture
4.21 introduced. The two 16 KB ROMs share **93.9 %** of their opcode
structure; the byte-level similarity is 85.1 %, and only 2.3 % of bytes
match at the same offset because almost every operand shifted as code
grew and moved.

The differences are refinements rather than a redesign: a scattering of
defensive fixes and a handful of routines compacted or reshaped. None
changes externally-visible behaviour.

## ROM header

| Field | 4.21 (variant 1) | 4.24 |
|---|---|---|
| Title | `Acorn ANFS 4.21` | `Acorn ANFS 4.24` |
| Copyright | `(C)1986 Acorn` | `(C)1986 Acorn` |
| ROM type | `&82` | `&82` |
| Service entry | [`&8A54`](address:8A54@4.21_variant_1) | [`&8A8A`](address:8A8A) |
| Language entry | none (`&4342`) | none (`&4342`) |

The service entry moves down by `&36` bytes, tracking the code inserted
ahead of it.

## Defensive `CLD` guards in the interrupt paths

4.24 adds four `CLD` instructions at the head of paths reachable from
[Econet](glossary:econet) [NMI](glossary:nmi) / [IRQ](glossary:irq) context:

| Address | Path | Protects |
|---|---|---|
| [`&8150`](address:8150) | port-slot scan | scan arithmetic |
| [`&835A`](address:835A) | `add_rxcb_ptr` | the RXCB-pointer `ADC` |
| [`&8476`](address:8476) | `immediate_op` | the operation-index `SBC` |
| [`&85AD`](address:85AD) | transfer setup | the transfer-size `ADC` |

An interrupt can arrive while the foreground has the decimal flag set;
each guard clears `D` so the binary `ADC` / `SBC` further down its path
computes correctly. 4.21 relied on callers never leaving `D` set. A fifth
`CLD` byte sits at [`&8397`](address:8397) but is unreached (it follows an
`RTS`), so it is inert.

## [ACCCON](glossary:acccon)-guarded buffer stores

The Master 128 reaches the Econet receive buffer through shadow / HAZEL
paging, controlled by [`ACCCON`](address:FE34). 4.24 widens the
save-restore of `ACCCON` around the buffer writes. The clearest new
instance is the last-data-byte store at [`&8284`](address:8284): it
saves `ACCCON`, switches to the caller's paging value in
[`escapable`](label:escapable), performs the `(open_port_buf),Y` store, then
restores `ACCCON` — so the write lands in the correct RAM regardless of
what the interrupted foreground had paged in.

## Credits easter egg rewritten

The `*` credits keyword handler drops its hand-written character-emit
loop. Where 4.21 walked `credits_keyword_start` byte by byte through
`OSASCI`, 4.24 emits the same text with a single `jsr`
[`print_inline`](label:print_inline) (at [`&8D59`](address:8D59)) over the
inline, high-bit-terminated string at [`&8D5C`](address:8D5C). The `&EA`
(`NOP`) terminator doubles as the resume opcode and falls through to the
`RTS`. The string still lists the four authors (B Cockburn, J Dunn,
B Robertson, J Wills).

## `print_fs_address` / `print_ps_address` share one tail

4.21 had two near-identical routines that each read a `network.station`
pair from [CMOS](glossary:cmos) and printed it. 4.24 folds them into one body:
[`print_ps_address`](label:print_ps_address) loads `X=4` and branches into the
shared tail; [`print_fs_address`](label:print_fs_address) loads `X=2` and falls
straight in. The shared tail [`print_cmos_pair`](label:print_cmos_pair) prints
`CMOS[X]`, a `.`, then `CMOS[X-1]`, deriving the station index with
`PHX` / `PLX` / `DEX` instead of a second literal `LDX`.

## Immediate-operation handlers compacted

The port-0 immediate-operation setup block (`&848B`–`&84F9` in 4.21) is
reshaped: the dispatch low-byte table moves, and the machine-type handler
at [`&84C7`](address:84C7) now uses the same workspace-offset setup as the
PEEK path (`port_ws_offset = &2E`, `rx_buf_offset = &0D`, then
`jsr tx_calc_transfer`) rather than writing its own buffer dimensions.

The transfer-size routine `tx_calc_transfer` is relocated from
[`&8900`](address:8900@4.21_variant_1) to [`&85AD`](address:85AD) (its
three call sites move with it) and gains a `CLD` guard and a new
shadow-RAM branch: when the buffer is a Tube address and `ACCCON.E` marks
shadow RAM enabled, it now sets the shadow bit in `escapable` before the
4-byte size subtraction.

## New command sub-table record

4.24 inserts a five-byte record — `4F 6E 80 00 00`, ASCII `"On"` followed
by table markers — into the FS-command sub-table at
[`&A80E`](address:A80E), immediately after that sub-table's shifted
default-handler word (`&8E44`, i.e. [`&8E45`](address:8E45)-1, the
`*command` / `*RUN`-`&` classifier). This is the one net-new record in
the command tables; it is why command-table addresses shift by `+&14`
before it and `+&19` after. (The preceding word `&8E2C`→`&8E44` is not
new — it is the same default-handler slot, shifted with the extended-
vector region.)

## TX control block grows a byte

Several TXCB field offsets shift by `+1` (e.g. the destination-offset
load `LDY #&2C`→`LDY #&2D` and the control-byte `LDA #&21`→`LDA #&22`),
reflecting a one-byte growth in the transmit control block layout.

## Dispatch-table bases

Every PHA/PHA/RTS dispatch table shifts with the code around it:

| Table | 4.21 (lo / hi) | 4.24 (lo / hi) |
|---|---|---|
| Service call | `&89ED` / `&8A20` | `&8A23` / `&8A56` |
| [OSWORD](glossary:osword) `&13` | `&A9A8` / `&A9BA` | `&A9C8` / `&A9DA` |
| NETV | `&AD20` / `&AD29` | `&AD40` / `&AD49` |
| Extended vectors | `&8EB5` | `&8ECD` |
