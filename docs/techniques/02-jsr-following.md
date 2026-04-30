# JSR-following: triangulating routine addresses through known callers

## Problem

Routine `R` at address `addr_A` in version A is unmapped. Some of `R`'s
callers, however, *did* map cleanly. We can use the surviving caller
mappings to read the actual JSR target byte at the corresponding
location in version B and recover `R`'s new address directly — without
any fuzzy matching.

This is the most reliable single-routine technique we have. It produces
no false positives when the prerequisites are met.

## Algorithm

1. Build a 4.18 → 4.21 address map from every routine that *is* named in
   both drivers. With ~300 named routines this gives several hundred
   anchor points spread across the ROM.

   ```python
   addr_map = {}  # 4.18 addr -> 4.21 addr
   for name, old_addr in old_subs.items():
       if name in new_subs:
           addr_map[old_addr] = new_subs[name]
   ```

2. For each unmapped routine `R` at `addr_A`, find the addresses in
   version A that contain `JSR addr_A` (or `JMP addr_A`):

   ```python
   def find_callers(data, target):
       lo = target & 0xFF
       hi = (target >> 8) & 0xFF
       return [ROM_BASE + i
               for i in range(len(data) - 2)
               if data[i] == 0x20 and data[i+1] == lo and data[i+2] == hi]
   ```

3. For each caller `caller_old`, look up the corresponding
   `caller_new = addr_map[caller_old]` (or extrapolate from a nearby
   anchor: if `caller_old` falls in a contiguous run between known
   anchors, add the offset).

4. At `caller_new` in version B, expect to find the byte `0x20` (JSR)
   followed by a 16-bit address. That address is `R`'s location in
   version B.

5. If multiple callers agree on the same target, you're done. If they
   disagree, the routine probably split into two and the callers have
   diverged.

## Worked example

```
4.18 caller of get_ws_page lives at &8B1A.
&8B1A is between known mapping anchors so it's mappable to 4.21 &8B23.
At 4.21 &8B23: bytes 20 AD 8C  =>  JSR &8CAD.
Therefore get_ws_page in 4.21_v1 is at &8CAD.
```

Confirmed by spot-checking the prologue against 4.18:

| 4.18 &8CB9 | 4.21 &8CAD |
|---|---|
| LDY romsel_copy | LDY romsel_copy |
| LDA rom_ws_pages,Y | LDA rom_ws_pages,Y |
| TAY / RTS | TAY / ROL A / PHP / ROR A / PLP / BPL +2 / ORA #&80 / TAY / RTS |

The prologues match (with the 4.21 version's extra ADLC-flag-extraction
suffix), confirming the JSR-followed address.

## Prerequisites

This technique needs all of:

* **A direct JSR or JMP caller** (not a PHA/PHA/RTS dispatched call).
  About 80% of ANFS routines are PHA/PHA/RTS dispatched, so this
  technique is a poor fit for them. Use [dispatch-table
  decoding](04-dispatch-table-decoding.md) instead in that case.
* **A mappable caller**. If every caller of `R` is itself in unmapped
  territory, JSR-following can't get a foothold.

## Strengths

* **Zero false positives**. If the JSR opcode and target bytes are
  there, the routine is at exactly that address — no interpretation
  needed.
* **Cheap**. One byte-pattern scan in version A plus a small number of
  byte reads in version B per candidate routine.
* **Self-validating**. Multiple callers confirm or invalidate the
  result.

## Pseudocode for the full pass

```python
unmapped = list_of_unmapped_4_18_subs()
for old_addr, name in unmapped:
    callers = find_callers(old_data, old_addr)
    for caller_old in callers:
        if caller_old in addr_map:
            caller_new = addr_map[caller_old]
        else:
            # nearby anchor extrapolation
            nearest = find_nearest_anchor(addr_map, caller_old, max_dist=4)
            if not nearest:
                continue
            caller_new = nearest[1] + (caller_old - nearest[0])
        if new_data[caller_new - ROM_BASE] != 0x20:
            continue  # not a JSR — caller's bytes diverged
        target = (new_data[caller_new - ROM_BASE + 1]
                  | (new_data[caller_new - ROM_BASE + 2] << 8))
        if 0x8000 <= target <= 0xBFFF:
            print(f"{name}: 4.18 &{old_addr:04X} -> 4.21 &{target:04X}")
            break
```

The `find_nearest_anchor` extrapolation is necessary because not every
single byte address has an anchor — only the entry points of named
subroutines. For an internal address inside a mapped routine the
extrapolation is `caller_new = nearest_anchor_new + (caller_old -
nearest_anchor_old)`. This is safe within ~16 bytes of an anchor; beyond
that, intervening insertions or deletions can throw off the offset.

## Limitations

* **Cannot find PHA/PHA/RTS dispatched routines** by itself, since
  there's no direct JSR site for those. Combine with dispatch-table
  decoding.
* **Caller's prologue may have shifted**. If the 4.18 caller has had
  instructions inserted before the JSR, the offset extrapolation puts
  the candidate `caller_new` somewhere other than at the JSR opcode.
  Mitigated by skipping candidates where the byte at `caller_new` is
  not `0x20`.
* **Only finds routines that are still being called**. If the new
  version dropped all calls to `R`, JSR-following silently misses it
  even when the body still exists.

## When to use

First choice for any UNMAPPED routine that has at least one direct JSR
caller. Combine with [opcode fingerprinting](01-opcode-fingerprinting.md)
to verify the result is the right routine (not something else placed at
the same address by coincidence).
