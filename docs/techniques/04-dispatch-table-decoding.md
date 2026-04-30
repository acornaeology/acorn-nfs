# Dispatch-table decoding: recovering all PHA/PHA/RTS handlers at once

## Problem

The 6502 has no `JSR (indirect)` and no `JMP (indirect,X)` — only
`JMP (indirect)` and the 65C12's `JMP (indirect,X)`. To dispatch
through a function-pointer table on the NMOS 6502, the standard
idiom is **PHA/PHA/RTS**: push the high byte of the target, push the
low byte, then `RTS`, which pops both bytes into the program counter
and adds 1 to land at the desired address.

ANFS uses this idiom heavily — for service-call dispatch, OSWORD &13
sub-functions, OSBYTE handlers, star-command handlers, and several
internal sub-tables. None of these dispatched routines have direct
JSR callers, so [JSR-following](02-jsr-following.md) doesn't find
them. They're reached only through bytes inside data tables.

The good news: each table is a **batch source of truth** for a whole
family of routines. Decode the table once and you get every
handler's address simultaneously.

## The PHA/PHA/RTS dispatch pattern

```
.dispatch
    tax                      ; index = sub-function number
    cmp #N                   ; reject out-of-range
    bcs reject
    lda hi_table,x           ; load high byte
    pha
    lda lo_table,x           ; load low byte
    pha
    rts                      ; jumps to (hi << 8 | lo) + 1
```

The `+1` matters. `RTS` pulls PCL, then PCH, then increments PC. So
the byte stored is **target − 1**. Equivalently, target = stored + 1.

The two halves of the dispatch table — `lo_table` and `hi_table` —
may be split (low bytes contiguous in one region, high bytes
contiguous in another), interleaved, or stored as one packed run.

## Algorithm

1. **Find the dispatcher.** Look for the
   `LDA hi,x / PHA / LDA lo,x / PHA / RTS` pattern. The two `LDA abs,X`
   operands give the table base addresses directly. In 4.21_v1
   the OSWORD &13 dispatcher at &A99A is:

   ```
   AA       TAX
   C9 13    CMP #&13
   B0 08    BCS +8         (reject)
   BD BA A9 LDA &A9BA,X    (hi table)
   48       PHA
   BD A8 A9 LDA &A9A8,X    (lo table)
   48       PHA
   60       RTS
   ```

2. **Decode the table.** Walk both halves in parallel for `N` entries
   (up to the `CMP #N` bound), computing
   `target = ((hi << 8) | lo) + 1`:

   ```python
   for x in range(N):
       lo = data[lo_base - ROM_BASE + x]
       hi = data[hi_base - ROM_BASE + x]
       target = ((hi << 8) | lo) + 1
       print(f"sub {x}: &{target:04X}")
   ```

3. **Cross-reference with known names.** If the source version had
   names for these sub-functions (and they kept the same numbering
   convention), assign them to the new addresses verbatim.

4. **Spot-check the prologues.** PHA/PHA/RTS dispatched routines
   often share a setup prologue across all entries. If many entries
   start with the same opcode sequence, you've decoded correctly.

## Worked example: OSWORD &13 in 4.21_v1

The OSWORD &13 sub-handler dispatch table at &A9A8/&A9BA decoded:

| Sub | Target | 4.18 name |
|---|---|---|
| 0 | &A9CC | osword_13_read_station |
| 1 | &A9DA | osword_13_set_station |
| 2 | &AA91 | osword_13_read_ws_pair |
| 3 | &AA9D | osword_13_write_ws_pair |
| 4 | &AAB2 | osword_13_read_prot |
| 5 | &AAB8 | osword_13_write_prot |
| 6 | &AAC2 | osword_13_read_handles |
| 7 | &AAD0 | osword_13_set_handles |
| 8 | &AB68 | osword_13_read_rx_flag |
| 9 | &AB71 | osword_13_read_rx_port |
| 10 | &AB7F | osword_13_read_error |
| 11 | &AB86 | osword_13_read_context |
| 12 | &AA72 | osword_13_read_csd |
| 13 | &AA75 | osword_13_write_csd |
| 14 | &AB8B | osword_13_read_free_bufs |
| 15 | &AB93 | osword_13_read_ctx_3 |
| 16 | &AB9E | osword_13_write_ctx_3 |

Eighteen handlers, all named in one pass. The LCS-based mapper
recovered most of these for free (because the relative ordering of
the table entries was unchanged) but four (read_station,
set_station, read_handles, set_handles) had a 1-byte prologue
shift that left them mis-aligned by exactly one address — easily
corrected once the dispatch table reveals the canonical entry
points.

## Variations

### Split-byte tables vs interleaved

Some dispatchers store `lo, hi, lo, hi, ...` interleaved instead of
`lo, lo, ..., hi, hi, ...` in two halves. The decoder generalises:

```python
if interleaved:
    for x in range(N):
        lo = data[base + x*2]
        hi = data[base + x*2 + 1]
        target = ((hi << 8) | lo) + 1
```

ANFS's star-command table at &A3D8 uses *triplet* entries
`(name_first_char, lo_offset, hi_offset)` where the offsets are
*relative* to a per-sub-table base — yet another variation requiring
its own decoder.

### Hidden trampolines

Some dispatched routines start with shared boilerplate
(register-save, FS-active check) before reaching their specific
body. If your `target` byte points at a `JSR shared_prologue` rather
than at the routine's distinctive body, the *real* entry is still
`target` (that's what RTS lands on); the body label is at
`target + 3`. Annotate the entry, then add a body-start label.

In 4.21 ANFS the OSWORD &13 read_station / set_station / read_handles
/ set_handles handlers all begin with `JSR ensure_fs_selected`
(&8B4D). Their body labels are 3 bytes after their dispatch entries
— a useful pattern to capture as a body-start label adjacent to the
entry-point declaration.

### Dispatch through DEX/RTS or RTS-only stubs

Some routines are dispatched to addresses that contain only a `RTS`
or short stub (e.g. an RTS that's there for a "no-op sub-function"
slot). The table entry is still valid; the routine simply does
nothing.

## Strengths

* **Batch recovery** — one decoder pass yields all handlers in the
  family.
* **No fuzzy matching** — the addresses come straight from the
  dispatch table bytes.
* **Reveals semantics** — the table's structure tells you which
  sub-function index each handler is, useful when naming the
  recovered routines.
* **Survives any internal reorganisation**. As long as the
  dispatcher knows where its tables are, the dispatched routines
  can move freely across the ROM and the dispatch table tracks
  them.

## Limitations

* **Need to find the dispatcher first.** If the dispatcher itself is
  unmapped, you have to fingerprint it (it's distinctive — the
  PHA/PHA/RTS pattern with two `LDA abs,X` is a recognisable
  16-byte prologue).
* **Need to know the dispatch encoding.** Most ANFS tables use the
  standard PHA/PHA/RTS. A few use `JMP (vector,X)` (65C12 only) or
  computed-goto via JMP table; those need their own decoders.
* **Need to know how many entries.** Look at the `CMP #N / BCS` or
  equivalent range check that precedes the dispatch — N is the
  table length.

## When to use

First choice for any UNMAPPED routine that is reached only via
dispatch. Decode the table once; recover the entire family of
handlers in a single commit. Combine with [string
anchoring](03-string-anchoring.md) for star-command tables (the name
strings sit adjacent to the dispatch addresses) and with
[opcode fingerprinting](01-opcode-fingerprinting.md) to verify each
recovered handler is the right routine.
