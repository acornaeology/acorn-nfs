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

## OSWORD &0E (14) real-time-clock routine reworked

The substantive change is a rework of the OSWORD `&0E` (14) real-time-clock
handler. The details and meaning below follow J.G. Harston's write-up (see
the reference at the foot of this page).

**It now checks the current filing system first.** The dispatcher
[`osword_0e_dispatch`](label:osword_0e_dispatch) at [`&A89A`](address:A89A) calls the
new [`fs_num_via_osargs`](label:fs_num_via_osargs) helper and only services the
clock request when [NetFS](glossary:nfs) is the current filing system — leaving the
OSWORD for other filing systems to handle otherwise.

**The clock/date formatting is restructured.**
[`save_txcb_and_convert`](label:save_txcb_and_convert) (entry moved to
[`&A8B1`](address:A8B1)) loops over the clock bytes calling a rewritten
[`bin_to_bcd`](label:bin_to_bcd) helper (decimal-mode `ADC`-in-a-loop) and forms
the year from a 7-bit field plus a base of `&51`, subtracting 100
(`CMP #&64` / `SBC #&64`) to move a year of 100 or more into the **20xx**
century. Years 2100-2107 are not converted to 21xx.
[`save_txcb_done`](label:save_txcb_done) reads the CMOS clock via OSWORD and
writes a default century of `"20"` if that read fails.

## New OSARGS filing-system helper

4.26 adds a small routine, [`fs_num_via_osargs`](label:fs_num_via_osargs), in the
ROM-tail space that was `&FF` padding in 4.25 (`&BFF7`–`&BFFF`). It reads the
current filing-system number via `OSARGS` and returns `EQ` when it is 5
([NetFS](glossary:nfs)) — the filing-system guard the reworked clock routine uses.
Its last two bytes double as the [`hazel_minus_2`](label:hazel_minus_2) /
[`hazel_minus_1`](label:hazel_minus_1) indexing-base anchors that previously sat
on the padding.

## Bug fix: `Bad string` error number

The bad-inline-argument error path at [`&94C0`](address:94C0) is corrected: 4.25
read the `brk_ptr` zero-page byte (`LDA &FD`) instead of loading the error
number, so the `Bad string` error was not set correctly. 4.26 loads it as an
immediate (`LDA #&FD`) before calling [`error_bad_inline`](label:error_bad_inline).

## Reference

The meaning of the RTC changes is documented by J.G. Harston,
[*ANFS 4.26 updated OSWORD 14 RTC routine*](https://mdfs.net/System/ROMs/Filing/Network/Acorn/ANFS426RTC).
