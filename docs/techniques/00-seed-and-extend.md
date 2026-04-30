# Seed-and-extend block matching for ROM version address mapping

## Problem

We have ROM version A, fully annotated, and ROM version B which we are about
to disassemble. We want to translate every address-bearing annotation from A
to B: `subroutine(addr_A, ...)` becomes `subroutine(addr_B, ...)`. To do that
we need a function `m: addr_A → addr_B`.

The natural approach is to align the two opcode sequences and propagate the
mapping for every aligned instruction. `difflib.SequenceMatcher` does this
via the longest common subsequence (LCS) algorithm. It works well — for
ANFS 4.08.53 → 4.18 it produces ~7000 mappings out of ~8000 instructions.

But LCS is **order-preserving**. If routine X moved from address A1 to a
higher address A2', and routine Y moved in the opposite direction, LCS can
match at most one of them: it will pick the longer and emit the other as
"deleted" in A and "inserted" in B. The annotations for the lost routine
become unmapped.

For ANFS 4.18 → 4.21 (variant 1) the loss rate is small in practice — the
Master 128 mostly *rewrote* code rather than reordering it — but moves
across the larger ANFS family (4.08.53 → 4.18) are common, with around 117
addresses in 8 distinct relocated blocks recovered by the technique below.

## Algorithm: seed-and-extend with k-mer indexing

Borrowed from BLAST and minimap2, the bioinformatics tools that solve the
same problem at a much larger scale (aligning DNA reads against reference
genomes). Three stages:

### 1. Index

Build a hash table of every k-gram of opcodes in the unmatched regions of
B, keyed by the k-tuple of opcode bytes, valued as the offsets where it
occurs:

```python
b_index: dict[bytes, list[int]] = defaultdict(list)
for j in range(len(opcodes_b) - k + 1):
    if any(b_pinned[j + d] for d in range(k)):
        continue
    b_index[opcodes_b[j:j + k]].append(j)
```

`b_pinned` records which positions are already mapped by the primary LCS
pass; we only consider positions outside that pre-existing alignment.

### 2. Seed

For every k-gram in the unmatched regions of A, look it up in the index.
Each hit `(i, j)` is a candidate seed alignment with offset `delta = j - i`.
Bucket all seeds by their delta:

```python
seeds_by_delta: dict[int, list[(int, int)]] = defaultdict(list)
for i in range(len(opcodes_a) - k + 1):
    if any(a_pinned[i + d] for d in range(k)):
        continue
    if (kmer := opcodes_a[i:i + k]) in b_index:
        for j in b_index[kmer]:
            seeds_by_delta[j - i].append((i, j))
```

Then chain seeds at the same delta whose A-positions are within a small
gap (`max_seed_gap = 8` opcodes by default). A chain with at least
`min_seeds = 2` hits is a candidate alignment region.

### 3. Extend

For each candidate region, run a constrained `SequenceMatcher` on the two
windowed opcode sub-sequences and check the similarity ratio:

```python
sm = difflib.SequenceMatcher(None, a_window, b_window, autojunk=False)
ratio = sm.ratio()
```

Accept the alignment if `ratio >= min_ratio` (default 0.85). The ratio is
mathematically equivalent to the Sørensen–Dice coefficient on opcode
sequences — symmetric, normalised to [0, 1], and tolerant of small length
differences.

### 4. Greedy assignment

Sort accepted alignments by descending ratio. For each, copy its matching
opcode pairs into the supplementary map, skipping any pair that conflicts
with the primary map or with a previously-accepted higher-ratio alignment.

## Choosing k

For 6502/65C02 ROMs the opcode alphabet has 256 letters, so the
expected number of random k-gram hits in a 16 KB ROM is about
`16384 / 256^k`. With `k = 6` that is `16384 / 256^6 ≈ 4 × 10⁻¹¹` —
random hits are negligible, but small routines still seed comfortably
because their first 6 opcodes are usually distinctive.

`k = 4` is more permissive: more candidate seeds per chain, more false
seeds to filter through extension. Useful when the source routine is
short or has been edited.

`k = 8` is more selective: fewer seeds, fewer false positives, but small
relocated blocks won't seed.

Default in `disasm_tools/blockmatch.py` is `k = 6`.

## What this misses

* **Sub-fragment moves** — if only part of a routine moved, the seed
  chain may cover the moved fragment but the prologue is in a different
  place. The supplementary mapping is still correct for the moved
  fragment, but the *entry point* needs another technique
  (string anchoring or dispatch-table decoding usually).
* **Routines rewritten in place** — opcode similarity drops below the
  threshold even though the routine is at the *same* address with the
  *same* purpose. The primary LCS pass handles same-position rewrites
  well; only reorders + rewrites are problematic.
* **Repetitive patterns** — dispatch tables, string-copy loops, and
  small idioms can collide. The minimum chain length and ratio
  threshold filter most of these but tuning may be needed.

## Validation

The implementation in `src/disasm_tools/blockmatch.py` ships with a
synthetic test: given `A = X || Y` and `B = Y || X` (a true block
swap), the primary pass picks one half and the supplementary pass
recovers the other at ratio 1.0.

On real ROM pairs:

| Pair | Supplementary mappings | Largest block |
|---|---|---|
| 4.18 vs 4.08.53 (sibling release) | (not measured here) | — |
| NFS 3.34B vs 3.35D | 117 mappings in 8 blocks | 28 instructions, ratio 1.00 |
| ANFS 4.18 vs 4.21 variant 1 | 0 | — |

The 4.18 vs 4.21 zero result is a property of the version pair — the
unmatched regions in 4.21 have at most 31% pairwise opcode similarity to
the unmatched regions in 4.18 (Master 128 *rewrote* the code rather than
relocating it). Fingerprinting individual known routines from 4.18 still
finds them in 4.21, but the supplementary block-match doesn't catch them
because LCS already consumed their source bytes mapping them to
unrelated targets in 4.21.

## References

* `src/disasm_tools/blockmatch.py` — implementation
* Altschul et al., *Basic local alignment search tool*, J. Mol. Biol., 1990
  — original BLAST paper, the inspiration for this seed-and-extend pattern
* Li, *Minimap2: pairwise alignment for nucleotide sequences*, Bioinformatics,
  2018 — the modern descendant that uses a similar k-mer index plus
  chaining
