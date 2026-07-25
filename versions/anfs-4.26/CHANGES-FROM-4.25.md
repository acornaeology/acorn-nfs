# Changes from [ANFS](glossary:nfs) 4.25 to ANFS 4.26

ANFS 4.26 is the next [Master 128](glossary:master-128) ANFS after 4.25. Both are
[65C02](glossary:65c02) [ROM](glossary:rom)s that keep their filing-system workspace in [HAZEL](glossary:hazel) hidden RAM
at `&C000`–`&C2FF`, so 4.26 inherits the whole Master-128 architecture
unchanged. The two 16 KB ROMs are **99.0 %** identical at the same byte offset —
almost nothing moves. The service entry, ROM type and copyright are unchanged.

The differences are a single reworked routine plus a small new helper; nothing
about the filing-system interface changes.

## ROM header and credits

| Field | 4.25 | 4.26 |
|---|---|---|
| Title | `Acorn ANFS 4.25` | `Acorn ANFS 4.26` |
| Copyright | `(C)1986 Acorn` | `(C)1986 Acorn` |
| ROM type | `&82` | `&82` |
| Service entry | [`&8A8C`](address:8A8C@4.25) | [`&8A8C`](address:8A8C) |

The credits easter-egg header punctuation changes from `The authors of ANFS
are;` to `The authors of ANFS are:` — a one-byte cosmetic tweak in the inline
string.

## OSWORD &0E clock reply routine reworked

The largest change is a rewrite of the routine that formats the real-time-clock
reply for OSWORD `&0E`, [`save_txcb_and_convert`](label:save_txcb_and_convert) at
[`&A8B2`](address:A8B2). 4.26 restructures the binary-to-BCD conversion: it now
loops over the three clock bytes calling a rewritten
[`bin_to_bcd`](label:bin_to_bcd) helper (decimal-mode `ADC`-in-a-loop), splits
the packed day/month byte into nibbles, and derives the year modulo 100
(`ADC #&51` / `CMP #&64` / `SBC #&64`) before storing the formatted result to
the reply buffer. The routine occupies the same address span; the reply it
produces is unchanged.

## New OSARGS filing-system helper

4.26 adds a small routine, [`fs_num_via_osargs`](label:fs_num_via_osargs), in the
ROM-tail space that was `&FF` padding in 4.25 (`&BFF7`–`&BFFF`). It reads the
current filing-system number via `OSARGS` and compares it with 5 ([NFS](glossary:nfs)).
Its last two bytes double as the [`hazel_minus_2`](label:hazel_minus_2) /
[`hazel_minus_1`](label:hazel_minus_1) indexing-base anchors that previously sat
on the padding.

## Minor edits

- The bad-inline-argument error path at [`&94C0`](address:94C0) loads the error
  number as an immediate (`LDA #&FD`) rather than reading the `brk_ptr`
  zero-page byte, and calls [`error_bad_inline`](label:error_bad_inline).
