# The "authors" easter egg

ANFS hides a credit roll behind an undocumented `*HELP` topic. Type

```
*HELP authors
```

at any prompt with ANFS as the active filing system, and the ROM
prints

```
The authors of ANFS are;
B Cockburn
J Dunn
B Robertson
J Wills
```

This note records two clever bytes-saving tricks that fall out of how
the easter egg is implemented.

## How the matcher works

The handler is `check_credits_easter_egg` at `&8D24` in 4.21 (and at
the corresponding offset in 4.18 / 4.08.53). It is the first thing
`svc_9_help` does on every `*HELP` service-9 dispatch, before any of
the normal help-table lookups:

```
.svc_9_help
    jsr check_credits_easter_egg
    ldy ws_page
    lda (os_text_ptr),y
    cmp #&0d                    ; bare *HELP -> version header
    ...
```

The matcher itself is just sixteen bytes:

```
.check_credits_easter_egg
    ldy ws_page                 ; Y = command-line offset of the *HELP arg
    ldx #5
.loop_match_credits
    lda (os_text_ptr),y         ; char from the command line
    cmp credits_keyword_start,x ; vs keyword byte
    bne done_credits_check      ; mismatch -> see if we got far enough
    iny
    inx
    bne loop_match_credits      ; (always: X is in 6..&FF here)
.done_credits_check
    cpx #&0c                    ; success iff X reached &0C on mismatch
    bne return_from_credits_check
    ldx #0                      ; print credits from offset 0
    ...
```

Starting from `X = 5` and looping while characters match, the
**success condition is a mismatch at exactly the moment `X = &0C`**.
That means the matched range is offsets 5..11 inclusive — seven bytes.

## Trick 1: the keyword lives inside the message

`credits_keyword_start` at `&8D45` is laid out like this:

```
offset  byte(s)
------  -------
   0    CR
   1-3  T h e
   4    ' '
   5-11 a u t h o r s     <-- the seven bytes the matcher walks
  12    ' '
  13-24 of ANFS are;
  25    CR
  26-35 B Cockburn
  36    CR
  37-39 J D u
  40-41 n n             <-- still part of the printed message
  42    CR
  43-53 B Robertson
  54    CR
  55-61 J Wills
  62    CR
  63    CR
  64    00              <-- null terminator for the print loop
```

The print loop emits everything from offset 0 up to the first zero
byte. So the same physical bytes do two jobs:

- **As a keyword**: bytes 5..11 form the literal string `authors` that
  the matcher compares against the command-line argument.
- **As a message**: bytes 5..11 are also the word `authors` in
  `"The authors of ANFS are;"`, which is what the routine prints when
  the match succeeds.

A naive implementation would have stored a separate keyword table
("authors\0") plus the credits banner. The ANFS authors realised the
two strings overlap perfectly and dropped the keyword table entirely
— saving eight bytes for zero functional cost.

It is the only easter-egg trigger word that was naturally going to
appear in the credit roll anyway.

## Trick 2: indexed addressing through a "convenient" base

`copy_ps_data` is the printer-server template loader. It needs to
copy eight bytes — the default printer-server name `"PRINT "`
followed by two status bytes — into the open RX buffer. The 6502
trick it uses to do this in five instructions is:

```
.copy_ps_data
    ldx #&f8
.loop_copy_ps_tmpl
    lda <some_base>,x       ; read template byte
    sta (net_rx_ptr),y      ; into RX buffer
    iny
    inx                     ; X wraps from &FF -> &00 to terminate
    bne loop_copy_ps_tmpl
    rts
```

`X` walks `&F8..&FF` (eight values) before wrapping to zero and
ending the loop. So the routine reads from `<some_base> + &F8`
through `<some_base> + &FF` — and the ROM author can pick *any*
`<some_base>` whose `+&F8` lands on the actual template data.

Where this base lands shifts every time the ROM is rebuilt: the
template data and the credits data move around as code changes, so
the offset that satisfies `base + &F8 = template_data` lands somewhere
new each time.

### 4.08.53: the base lands inside "Cockburn"

In 4.08.53 the template data is at `&8E43`, so the base needs to be
`&8D4B`. That falls inside `B Cockburn` — the assembler labels it
`ps_template_base` and the layout reads:

```
&8D47  equs "B Co"
.ps_template_base
&8D4B  equs "ckburn"     <-- &8D4B + &F8 = &8E43
```

The bytes `c k b u r n` are read by the credit-print loop on the
match path, and the address `&8D4B` is the base for `copy_ps_data`'s
indexed read.

### 4.18: the base lands inside "Dunn"

In 4.18 the template data is at `&8E59`, so the base needs to be
`&8D61`. That address falls inside `J Dunn` — specifically on the
first `n` of `"nn"`:

```
&8D5D  equs "J Du"
.ps_template_base
&8D61  equs "nn"          <-- &8D61 + &F8 = &8E59
&8D63  equb &0D
&8D64  equs "B Robertson"
...
```

Two roles in one address: it is both a label that anchors the
indexed-addressing arithmetic in `copy_ps_data` (read by no other
code; the bytes themselves are never accessed via this label), and
the `nn` letters of `J Dunn` in the printed credit roll (read only
by the credit-print loop). The label costs zero ROM bytes — it
just names a convenient point inside an existing string.

The disassembly's `LDA ps_template_base,X` at `&B01B` is, at the
opcode level, identical to writing `LDA &8D61,X` directly. The
symbolic name is purely an annotation aid; the *cleverness* is the
choice of `&8D61` as the address the assembler computed to.

### 4.21: the trick moved into a JSR operand

In 4.21 the template data has moved to `&8E9F`. The base now needs
to be `&8E9F - &F8 = &8DA7`. That address is inside the operand of
an instruction:

```
&8DA6  20 D7 93   jsr set_xfer_params
                  ^  ^^
                  |  &8DA7 -- the low byte of the &93D7 operand
                  &8DA6
```

`&8DA7` is the second byte of the three-byte `JSR &93D7` encoding —
the low byte of its target operand. py8dis labels it `l8da7` (an
auto-generated mid-instruction label) and `copy_ps_data`'s LDA reads
through it as `LDA l8da7,X`.

So the dual-use trick survives across 4.21 but in a different
location: instead of the base label landing inside a credits string,
it lands inside an instruction's operand. Same idea, different
host.

## Loose end in the 4.21 driver

The 4.21 disassembly defines a `ps_template_base` label at `&8D6E`
(inside "J Dunn", mirroring 4.18's positioning). That address is
**not** what 4.21's `copy_ps_data` actually reads from — the code
goes through `&8DA7` as shown above. The `&8D6E` label is a stale
carry-over from when the disassembly was generated by mapping 4.18's
labels onto 4.21 addresses, and no instruction in 4.21 references it.
The label could be removed without affecting the assembled ROM.

## Why this is worth recording

These tricks are individually tiny — eight bytes here, three bytes
there — but they're the kind of detail you only see in a hand-tuned
8-bit ROM and that is invisible in any binary diff. The credit-roll
keyword and the data-template arithmetic both hide behind ordinary-
looking strings, so they're easy to miss on a first pass. Documenting
them here means the next reader (or the next ROM variant we look at)
can spot the pattern faster.

## References

- Disassembly: `versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py`,
  `check_credits_easter_egg` at `&8D24`, `copy_ps_data` at `&B3D7`.
- 4.18 baseline: `versions/anfs-4.18/disassemble/disasm_anfs_418.py`,
  the same routines at slightly different addresses (the
  `ps_template_base = &8D61` placement is in 4.18 and earlier).
- The credit roll itself originates much earlier than 4.18 — the
  same authors are listed in ANFS 4.08.53 with the same trigger
  word, suggesting this easter egg has been part of ANFS since its
  initial release.
