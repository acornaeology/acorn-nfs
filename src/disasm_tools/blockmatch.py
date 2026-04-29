"""Opcode-level address mapping between two BBC sideways ROM versions.

Provides two passes:

1. **Primary** — `difflib.SequenceMatcher` on opcode sequences (LCS).
   Order-preserving, so it cannot follow code blocks that have been
   reordered or relocated between versions.

2. **Supplementary** — seed-and-extend matching of k-grams, borrowed
   from bioinformatics (BLAST, minimap2). For each unmatched region of
   the old ROM:

     a. Look up every k-gram of opcodes in an index built over the
        unmatched regions of the new ROM, producing seed hits
        `(i_a, j_b)`.
     b. Bucket hits by alignment offset `delta = j_b - i_a`. A
        chain of seeds at a consistent delta is evidence of a moved
        block.
     c. For each chain, run `SequenceMatcher` on the windowed opcode
        sub-sequences. Compute the opcode-level similarity ratio
        `2·M / (m + n)` (Sørensen–Dice on opcode sequences, same as
        `SequenceMatcher.ratio()`). Accept the alignment if the ratio
        meets `min_ratio`.
     d. Emit per-instruction address mappings for every matching
        opcode pair in the alignment.

Conflicts inside the supplementary pass (one A or B instruction
claimed by two clusters) are resolved greedily by ratio. Conflicts
with the primary map are not allowed: the primary map is
authoritative and never overridden.

Returns address mappings as `dict[int, int]` keyed by ROM address
(e.g. `0xA000` -> `0xA1B4`), the same shape used by the existing
generate scripts.
"""

import difflib
from collections import defaultdict
from dataclasses import dataclass

from disasm_tools.mos6502 import ROM_BASE, opcode_tables


# ============================================================
# Linear sweep
# ============================================================


def disassemble_to_opcodes(data: bytes, cpu: str = "6502"):
    """Linear sweep returning a list of (offset, opcode, length) tuples.

    Invalid opcodes (length 0 in the table) advance one byte. The cpu
    argument selects between '6502' and '65c02' opcode lengths.
    """
    lengths, _ = opcode_tables(cpu)
    instructions = []
    offset = 0
    while offset < len(data):
        opcode = data[offset]
        length = lengths[opcode] or 1
        instructions.append((offset, opcode, length))
        offset += length
    return instructions


# ============================================================
# Primary map (LCS / SequenceMatcher)
# ============================================================


def build_primary_map(insts_a, insts_b, rom_base: int = ROM_BASE):
    """LCS-based opcode mapping. Order-preserving; misses reorders."""
    opcodes_a = [op for _, op, _ in insts_a]
    opcodes_b = [op for _, op, _ in insts_b]
    matcher = difflib.SequenceMatcher(None, opcodes_a, opcodes_b,
                                      autojunk=False)
    addr_map = {}
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for d in range(i2 - i1):
                addr_map[rom_base + insts_a[i1 + d][0]] = (
                    rom_base + insts_b[j1 + d][0]
                )
    return addr_map


# ============================================================
# Supplementary map (seed-and-extend)
# ============================================================


@dataclass
class RelocatedBlock:
    """A region of the old ROM that was matched to a moved region in
    the new ROM by the supplementary pass."""
    a_start_addr: int            # inclusive
    a_end_addr: int              # exclusive
    b_start_addr: int
    b_end_addr: int
    ratio: float                 # opcode-level similarity (0.0 - 1.0)
    matched_pairs: int           # address mappings produced from this block
    a_opcodes: int               # opcodes in the A window
    b_opcodes: int               # opcodes in the B window


def find_relocated_blocks(
    insts_a, insts_b, primary_addr_map,
    *,
    rom_base: int = ROM_BASE,
    k: int = 6,
    min_seeds: int = 2,
    max_seed_gap: int = 8,
    min_block_opcodes: int = 8,
    min_ratio: float = 0.85,
):
    """Find supplementary opcode-level address mappings via
    k-mer seed-and-extend.

    insts_a, insts_b
        Linear-sweep output for each ROM.
    primary_addr_map
        Authoritative mappings from the primary pass; never overridden.
    k
        Seed length in opcodes. 6 is a good default for 6502/65C02:
        long enough that random matches are rare, short enough that
        small routines still seed.
    min_seeds
        Minimum number of seeds in a chain before extension. 2 keeps
        false positives down without rejecting small relocated blocks.
    max_seed_gap
        Maximum opcode gap between consecutive seeds in the same
        chain (lets a chain absorb a small mismatch).
    min_block_opcodes
        Minimum number of opcodes in the windowed alignment.
    min_ratio
        Minimum opcode-level similarity (Sørensen–Dice / SequenceMatcher
        ratio) required to accept the alignment.

    Returns
    -------
    (supplementary_map, blocks)
        - supplementary_map: dict[int, int] of new address mappings
          (no overlap with primary_addr_map).
        - blocks: list[RelocatedBlock] describing each accepted alignment.
    """
    if len(insts_a) < k or len(insts_b) < k:
        return {}, []

    # Pre-compute pinned-instruction masks
    primary_b_addrs = set(primary_addr_map.values())
    a_pinned = [
        (rom_base + off) in primary_addr_map for off, _, _ in insts_a
    ]
    b_pinned = [
        (rom_base + off) in primary_b_addrs for off, _, _ in insts_b
    ]

    opcodes_a = bytes(op for _, op, _ in insts_a)
    opcodes_b = bytes(op for _, op, _ in insts_b)

    # ---- Index k-mers over unmatched B ----
    b_index: dict[bytes, list[int]] = defaultdict(list)
    for j in range(len(opcodes_b) - k + 1):
        # Skip k-grams that touch any pinned instruction
        if any(b_pinned[j + d] for d in range(k)):
            continue
        b_index[opcodes_b[j:j + k]].append(j)

    # ---- Collect seeds, bucket by delta ----
    seeds_by_delta: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i in range(len(opcodes_a) - k + 1):
        if any(a_pinned[i + d] for d in range(k)):
            continue
        kmer = opcodes_a[i:i + k]
        if kmer in b_index:
            for j in b_index[kmer]:
                seeds_by_delta[j - i].append((i, j))

    # ---- Chain seeds with bounded gaps within each delta bucket ----
    candidates = []  # (i_lo, i_hi_excl, j_lo, j_hi_excl)
    for delta, seeds in seeds_by_delta.items():
        if len(seeds) < min_seeds:
            continue
        seeds.sort()
        chain = [seeds[0]]
        for s in seeds[1:]:
            if s[0] - chain[-1][0] <= max_seed_gap:
                chain.append(s)
            else:
                if len(chain) >= min_seeds:
                    i_lo = chain[0][0]
                    i_hi = chain[-1][0] + k
                    j_lo = chain[0][1]
                    j_hi = chain[-1][1] + k
                    candidates.append((i_lo, i_hi, j_lo, j_hi))
                chain = [s]
        if len(chain) >= min_seeds:
            i_lo = chain[0][0]
            i_hi = chain[-1][0] + k
            j_lo = chain[0][1]
            j_hi = chain[-1][1] + k
            candidates.append((i_lo, i_hi, j_lo, j_hi))

    # ---- Score each candidate via SequenceMatcher on the window ----
    aligned = []  # (ratio, i_lo, j_lo, blocks, a_len, b_len)
    for i_lo, i_hi, j_lo, j_hi in candidates:
        a_len = i_hi - i_lo
        b_len = j_hi - j_lo
        if a_len < min_block_opcodes or b_len < min_block_opcodes:
            continue
        a_win = opcodes_a[i_lo:i_hi]
        b_win = opcodes_b[j_lo:j_hi]
        sm = difflib.SequenceMatcher(None, a_win, b_win, autojunk=False)
        ratio = sm.ratio()
        if ratio < min_ratio:
            continue
        aligned.append(
            (ratio, i_lo, j_lo, sm.get_matching_blocks(), a_len, b_len)
        )

    # ---- Greedy assignment by descending ratio ----
    aligned.sort(key=lambda t: -t[0])
    used_a, used_b = set(), set()
    supplementary: dict[int, int] = {}
    blocks: list[RelocatedBlock] = []

    for ratio, i_lo, j_lo, mblocks, a_len, b_len in aligned:
        added_pairs = 0
        first_a = first_b = None
        last_a_end = last_b_end = None
        for b in mblocks:
            for d in range(b.size):
                a_idx = i_lo + b.a + d
                b_idx = j_lo + b.b + d
                if a_idx in used_a or b_idx in used_b:
                    continue
                if a_pinned[a_idx] or b_pinned[b_idx]:
                    continue
                addr_a = rom_base + insts_a[a_idx][0]
                addr_b = rom_base + insts_b[b_idx][0]
                if addr_a in primary_addr_map:
                    continue
                if addr_a in supplementary:
                    continue
                supplementary[addr_a] = addr_b
                used_a.add(a_idx)
                used_b.add(b_idx)
                added_pairs += 1
                if first_a is None:
                    first_a = addr_a
                    first_b = addr_b
                last_a_end = addr_a + insts_a[a_idx][2]
                last_b_end = addr_b + insts_b[b_idx][2]
        if added_pairs > 0 and first_a is not None:
            blocks.append(RelocatedBlock(
                a_start_addr=first_a,
                a_end_addr=last_a_end,
                b_start_addr=first_b,
                b_end_addr=last_b_end,
                ratio=ratio,
                matched_pairs=added_pairs,
                a_opcodes=a_len,
                b_opcodes=b_len,
            ))

    return supplementary, blocks


# ============================================================
# Convenience: primary + supplementary in one call
# ============================================================


def build_full_address_map(
    data_a: bytes, data_b: bytes,
    cpu_a: str = "6502", cpu_b: str = "6502",
    *,
    rom_base: int = ROM_BASE,
    **kwargs,
):
    """Build a primary + supplementary opcode-level address map.

    Returns
    -------
    (full_map, primary_map, supplementary_map, blocks)
        full_map        merged dict (primary takes precedence)
        primary_map     LCS-based mappings
        supplementary_map  seed-and-extend mappings (disjoint from primary)
        blocks          list[RelocatedBlock] describing supplementary alignments
    """
    insts_a = disassemble_to_opcodes(data_a, cpu_a)
    insts_b = disassemble_to_opcodes(data_b, cpu_b)
    primary = build_primary_map(insts_a, insts_b, rom_base=rom_base)
    supplementary, blocks = find_relocated_blocks(
        insts_a, insts_b, primary, rom_base=rom_base, **kwargs
    )
    full = dict(primary)
    full.update(supplementary)
    return full, primary, supplementary, blocks
