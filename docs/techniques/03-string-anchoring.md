# String anchoring: locating routines by their inline strings

## Problem

Routine `R` prints a known message — say, "Econet Station " — using
the inline-string idiom: a `JSR print_inline` whose return address
points to the string bytes, followed by code that resumes after the
string. Both `R`'s entry and the JSR site are unmapped in version B.
But the string itself is searchable: a 15-byte ASCII pattern is
extraordinarily unlikely to collide.

## The inline string idiom

ANFS prints status text via this pattern:

```
.print_inline
    pla / sta ptr_lo  ; pull return address into a zero-page pointer
    pla / sta ptr_hi
.loop
    inc ptr_lo / bne / inc ptr_hi
    lda (ptr_lo),y
    bmi .end           ; high-bit byte: terminator AND first opcode
    jsr osasci
    bra .loop
.end
    jmp (ptr_lo)       ; resume after string
```

A caller looks like:

```
.print_station_id
    jsr print_inline
    equs "Econet Station "    ; data bytes
    ldy #1                    ; resumes here; LDY's opcode (&A0) has bit 7 clear
    ...
```

The clever bit: the next instruction's opcode after the string
*acts as the terminator* because `print_inline` checks the high bit.
Most opcodes have bit 7 clear (0x00–0x7F), so the natural terminator
falls between the string and the next instruction.

This idiom means that **finding the string** locates both the JSR
site (3 bytes earlier) and the routine entry that contains it.

## Algorithm

1. Pick a string fragment that's likely to be unique. Whole human-
   readable phrases like `"Econet Station "` or `"Bad ROM "` work well;
   single English words are too common.

2. Scan the new ROM's bytes for the literal:

   ```python
   pos = 0
   while True:
       i = new_data.find(b"Econet Station", pos)
       if i < 0: break
       print(f"&{ROM_BASE + i:04X}")
       pos = i + 1
   ```

3. The 3 bytes immediately before each hit should be `20 LL HH` — a
   `JSR &HHLL` to `print_inline`. Verify and identify the routine that
   owns this code.

4. The routine entry usually starts a few opcodes upstream of the
   `JSR print_inline`, often at the nearest `LDA` / `LDX` / `LDY` /
   register save / RTS. If the routine has its own subroutine
   declaration in 4.18 with the inline string in its body, walk back
   through the 4.18 driver to find the entry-point address relative
   to the inline string and apply the same offset in 4.21.

## Worked example

Searching 4.21_v1 for `"Econet Station "`:

```
&90CA: b"Econet Station ..."
```

Reading 3 bytes back: `&90C7: 20 61 92` → `JSR &9261` → `JSR print_inline`.

In 4.18 the same string is at &8FF4, the JSR at &8FF1. The 4.18 routine
entry is `print_station_id` at &8FF1 (the JSR is the first instruction
of the routine).

Therefore `print_station_id` in 4.21_v1 is at **&90C7** — exactly the
3-byte distance from the string, matching 4.18's structure.

Verified by extracting the surrounding context: 2 callers at &8CAA and
&8CE4 in 4.21_v1, matching the 4.18 callers `print_version_header` and
`svc_3_auto_boot`.

## Strengths

* **Authoritative**. A unique 12+ byte ASCII string anchors the
  surrounding code with zero ambiguity.
* **Bridges code and data**. The string is data; the surrounding
  code is otherwise invisible to opcode-only fingerprinting.
* **Survives reorderings**. The string moves with its routine no
  matter how the ROM is laid out.
* **Survives prologue rewrites**. Even if the routine's prologue is
  totally rewritten, the inline string is the load-bearing part of
  the routine and it's preserved.

## Limitations

* **Only works for routines that print constants**. Many helper
  routines (workspace inits, dispatch glue) print nothing.
* **Strings may be deleted or changed**. Master 128 ports often
  shorten messages or move them into a shared lookup table —
  the literal `"Econet Station "` may not exist verbatim in the new
  ROM. Search for shorter, more invariant fragments first.
* **Multiple callers print the same string**. The error-printing
  family, for example, all use `error_inline` with similar
  preamble — a single shared message could anchor several routines
  at once (a feature, not a bug).

## Variations

### Error-message anchoring

Errors are printed via `error_inline`, which builds a BRK error block
from the inline string. Searching for short error strings like `"Bad "`
or `"Not found"` finds the *callers* of `error_inline`, which are the
sites where specific errors are raised — useful for naming error-paths.

### Command-name anchoring

Star-command names appear in the cmd_table_fs as bit-7-terminated ASCII.
Searching for `"PROT"` or `"CDIR"` locates the table entries whose
adjacent dispatch words point to the command handlers. This is more
reliably done via [dispatch-table
decoding](04-dispatch-table-decoding.md) which handles the table
structure directly.

### Help-topic anchoring

`*HELP` topic names like `"NET"` or `"UTILS"` appear in dedicated
help-string tables. Same pattern: a string anchors the table, the
table indexes the topic handlers.

## When to use

First choice for any user-visible printing routine. The string anchor
is so distinctive that this technique gives near-certainty without
needing to spot-check the prologue. Pair with a quick verification of
the surrounding context (number of callers, presence of expected
helper JSRs) and you're done.
