# Changes from [ANFS](glossary:nfs) 4.24 to ANFS 4.25

ANFS 4.25 is the next [Master 128](glossary:master-128) ANFS after 4.24. Both are
[65C02](glossary:65c02) [ROM](glossary:rom)s that keep their filing-system workspace in [HAZEL](glossary:hazel) hidden RAM
at `&C000`–`&C2FF`, so 4.25 inherits the whole Master-128 architecture
unchanged. The two 16 KB ROMs share **98.2 %** of their opcode structure —
closer than any adjacent pair earlier in the ANFS chain. Only 10.3 % of
bytes match at the same offset, because a single two-byte instruction
inserted early in the ROM shifts almost every later address by `+2`.

The change is a one-instruction refinement, not a redesign, and does not
alter externally-visible behaviour.

## ROM header

| Field | 4.24 | 4.25 |
|---|---|---|
| Title | `Acorn ANFS 4.24` | `Acorn ANFS 4.25` |
| Copyright | `(C)1986 Acorn` | `(C)1986 Acorn` |
| ROM type | `&82` | `&82` |
| Service entry | [`&8A8A`](address:8A8A@4.24) | [`&8A8C`](address:8A8C) |
| Language entry | none (`&4342`) | none (`&4342`) |

The service entry moves up by two bytes, tracking the inserted instruction
ahead of it.

## The one functional change: `svc_state` cleared on the transmit-done path

The transmit-done exit [`tx_done_exit`](label:tx_done_exit) restores `X` and `Y`
from the stack and loads `A = 0` (success) before returning. 4.25 inserts a
single `STA` [`svc_state`](label:svc_state) at [`&85AC`](address:85AC) between the
`LDA #0` and the `RTS`, so the path now also writes the success code to the
service-state byte instead of leaving whatever an earlier stage of the
service call had put there:

```
        lda #0            ; A = 0 (success)
        sta svc_state     ; 4.25: also clear svc_state to success   <- new
        rts               ; return with A = 0
```

Those two bytes (`85 A9`) are the whole delta. Everything else below is a
mechanical consequence of them.

## Consequences of the `+2` shift

- **Every ROM address at or after [`&85AC`](address:85AC) moves up by two.** All
  `JSR` / `JMP` targets, dispatch-table entries, command-table records and
  self-modifying-code operand bytes follow the shift; none is a genuine
  edit. The two trailing `&FF` padding bytes at the very top of the 4.24
  ROM are dropped so the image stays exactly 16 KB.
- **Boot-filename pointer.** The auto-boot path loads the boot-filename
  address with `LDX #&3E : LDY #&8D` in 4.24; because the filename string
  moved with the shift, 4.25 loads `LDX #&40 : LDY #&8D` — the same pointer
  to the same (shifted) string.
- **Credits string.** The easter-egg text printed by
  [`print_inline`](label:print_inline) reads `Advanced NFS 4.25` (was
  `Advanced NFS 4.24`); the four authors (B Cockburn, J Dunn, B Robertson,
  J Wills) are unchanged.

## Dispatch-table bases

Every PHA/PHA/RTS dispatch table and the extended-vector table shift with
the code around them:

| Table | 4.24 (lo / hi) | 4.25 (lo / hi) |
|---|---|---|
| Service call | `&8A23` / `&8A56` | [`&8A25`](address:8A25) / [`&8A58`](address:8A58) |
| [OSWORD](glossary:osword) `&13` | `&A9C8` / `&A9DA` | [`&A9CA`](address:A9CA) / [`&A9DC`](address:A9DC) |
| NETV | `&AD40` / `&AD49` | [`&AD42`](address:AD42) / [`&AD4B`](address:AD4B) |
| Extended vectors | `&8ECD` | [`&8ECF`](address:8ECF) |
