# Opcode fingerprinting: locating a single routine in a new ROM version

## Problem

We know that routine `R` lives at address `addr_A` in version A and we have
its full byte extent (or at least the next subroutine's start address). The
LCS-based address mapper either failed to map `addr_A` at all, or mapped it
to an obviously wrong location in version B — perhaps because LCS chose to
align A's bytes with B's similar-but-unrelated bytes elsewhere. We want to
find `R` in version B without trusting the existing map.

## Algorithm

A sliding-window opcode-similarity search:

1. Extract the **opcode-only** signature of `R` from version A. Strip
   operand bytes — they hold ROM addresses that almost certainly differ in
   version B even when the routine is otherwise identical.
2. Build the opcode stream for the entire version B ROM via the same
   linear-sweep procedure, ignoring the existing address map.
3. For every position `j` in B's opcode stream, compute
   `SequenceMatcher.ratio()` between `R`'s signature and the
   length-matched window starting at `j`.
4. Sort by descending ratio. Cluster near-duplicates (peak smearing on a
   single match) and keep the top N.

## Pseudocode

```python
def fingerprint(insts_a, src_start, src_end, insts_b, *,
                min_ratio=0.5, top_n=5):
    fp = bytes(op for off, op, _ in insts_a
               if src_start <= ROM_BASE + off < src_end)
    dst_opcodes = bytes(op for _, op, _ in insts_b)
    candidates = []
    for j in range(len(dst_opcodes) - len(fp)):
        sm = SequenceMatcher(None, fp, dst_opcodes[j:j + len(fp)],
                             autojunk=False)
        if sm.ratio() >= min_ratio:
            candidates.append((sm.ratio(),
                               ROM_BASE + insts_b[j][0],
                               len(fp)))
    candidates.sort(key=lambda t: -t[0])
    deduped = []
    for ratio, addr, n in candidates:
        if any(abs(addr - a2) <= 8 for _, a2, _ in deduped):
            continue
        deduped.append((ratio, addr, n))
        if len(deduped) >= top_n:
            break
    return deduped
```

The implementation lives in `src/disasm_tools/fingerprint.py` and reads ROM
bytes plus the per-version `cpu` field from each `rom.json`.

## Choosing the signature length

Longer is better when the routine survived in one piece. In ANFS 4.18 →
4.21 the median signature length for successful matches was around 40
opcodes; the largest was 164 (process_all_fcbs).

Short signatures (under 16 opcodes) are unreliable because:

* Many short opcode sequences appear coincidentally elsewhere in the ROM
  (`LDA / STA / RTS` is common).
* Two-opcode prologues like `TYA / PHA` happen everywhere.

If the routine is short, prefer one of the more anchored techniques —
[JSR-following](02-jsr-following.md), [string anchoring](03-string-anchoring.md)
or [dispatch-table decoding](04-dispatch-table-decoding.md).

## Failure modes

### Prologue divergence

The most common false positive. If the new version replaced a
`TYA / PHA / TXA / PHA / LDA fs_options / PHA / LDA fs_block_offset / PHA /
LDX #&0F` 5-byte register-and-state save with a tighter
`PHX / PHY / LDX #&F7 / loop` 4-byte version (as ANFS 4.18 → 4.21 did
for `process_all_fcbs`), the body still matches strongly but its first
hit lies several opcodes deep into the routine — the entry point gets
reported at an address *inside* the routine.

**Symptom**: The fingerprint reports a candidate at an address whose
first 1–4 opcodes don't match the source's first 1–4 opcodes, but
opcodes 5–N do.

**Mitigation**: Spot-check the prologue by extracting both versions
side by side. If the body match starts at `candidate + N`, walk back N
bytes (or look at what calls the candidate; if a JSR target is
`candidate + N`, that's the real entry).

### Sub-fragment matches

A long routine that has been split into two parts — entry-point logic
moved one place, body moved another — produces a peak match on the body
fragment, not the entry point.

**Symptom**: The fingerprint hits a body label rather than the routine
name, with the surrounding context obviously belonging to a different
routine.

**Mitigation**: Cross-check the candidate with the dispatch table for
PHA/PHA/RTS-dispatched routines, or look for a JSR site that lands on
the prologue.

### Same-address rewrites

If the new version rewrote the routine in place, the body opcodes
diverge enough that the *highest-ratio* match might be on a different
unrelated routine that happens to be more opcode-similar than the
in-place rewrite.

**Symptom**: Top candidate is in the wrong place; the actual rewrite
shows up further down with low ratio.

**Mitigation**: This case is unusual when the LCS pass has already
accepted the same-address mapping. If LCS has thrown out the address
entirely (the relevant byte runs are too dissimilar), the routine has
been substantially rewritten and you may have to annotate from scratch.

## When to use this vs other techniques

* **First choice for unanchored routines**. If the routine has no
  inline string, no dispatch-table entry, and no direct JSR caller
  that you can map, fingerprinting is the only option.
* **Cheap to try first**. The implementation is one slide over the
  ROM; even on a 16 KB ROM with a 40-opcode signature it's
  millisecond-fast.
* **Cross-check with at least one other signal** before declaring a
  match. The next three papers all give complementary signals.

## Worked examples

| 4.18 routine | 4.21 candidate | Ratio | Outcome |
|---|---|---|---|
| `parse_addr_arg` &916E | &92AF | 0.965 | true match (corrected to &92B2 entry) |
| `svc_18_fs_select` &8B0D | &8B45 | 1.000 | true match |
| `cmd_cdir` &AD10 | &B09F | 0.902 | off-by-1 (real entry &B0A0; &B09F = previous routine's RTS) |
| `process_all_fcbs` &B799 | &BB2A | 0.878 | false positive — real entry &BB38 (prologue diverged) |
| `osword_4_handler` &A9B0 | &AD30 | 0.857 | suspect — first opcode differs (TSX vs LDA abs) |
| `tx_calc_transfer` &88F2 | &8910 | 0.897 | false positive — body opcodes differ |

The mixed accuracy in the table is the lived-experience caveat:
fingerprinting is fast and useful but never authoritative on its own.
Always pair it with a verifying technique for confirmation before
committing the annotation.
