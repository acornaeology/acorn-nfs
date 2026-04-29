"""Fingerprint a known routine in version A and locate it in version B.

Useful when address mapping (LCS or seed-and-extend) has consumed the
routine's source bytes mapping them to unrelated bytes in version B,
leaving the routine itself UNMAPPED. This tool ignores any pre-built
address map and just slides the source-version opcode signature across
the target-version opcode stream, reporting the highest similarity.

Typical use:

    >>> fingerprint(
    ...     '4.18', '0x916E',
    ...     '4.21_variant_1',
    ...     end_addr=0x91D8,            # optional: explicit extent
    ... )

Returns the best (ratio, addr) pair plus a list of the top N candidates.
"""

import difflib
from pathlib import Path

from disasm_tools.blockmatch import disassemble_to_opcodes
from disasm_tools.mos6502 import ROM_BASE
from disasm_tools.paths import resolve_version_dirpath, rom_prefix


def _load_rom_with_cpu(versions_dirpath: Path, version_id: str):
    """Returns (data, cpu) for the named version."""
    import json
    version_dirpath = resolve_version_dirpath(versions_dirpath, version_id)
    pfx = rom_prefix(version_dirpath)
    rom_filepath = version_dirpath / "rom" / f"{pfx}-{version_id}.rom"
    rom_json_filepath = version_dirpath / "rom" / "rom.json"
    cpu = "6502"
    if rom_json_filepath.exists():
        try:
            cpu = json.loads(rom_json_filepath.read_text()).get("cpu", "6502")
        except Exception:
            pass
    return rom_filepath.read_bytes(), cpu


def opcodes_for_range(insts, start_addr, end_addr,
                      rom_base: int = ROM_BASE):
    """Return the opcode bytes from the linear sweep that fall in
    [start_addr, end_addr)."""
    return bytes(op for off, op, _ in insts
                 if start_addr <= rom_base + off < end_addr)


def fingerprint(
    versions_dirpath: Path,
    src_version: str, src_start: int, src_end: int,
    dst_version: str,
    *,
    top_n: int = 5,
    min_ratio: float = 0.5,
):
    """Locate the src_version routine [src_start, src_end) in dst_version.

    Parameters
    ----------
    versions_dirpath
        The repo's `versions/` directory.
    src_version
        Source version id (e.g. '4.18').
    src_start, src_end
        ROM-address range bounding the routine in src_version.
    dst_version
        Destination version id (e.g. '4.21_variant_1').
    top_n
        Return up to this many candidates.
    min_ratio
        Skip windows whose ratio is below this threshold.

    Returns
    -------
    list[tuple[float, int, int]]
        (ratio, dst_addr, src_opcode_count), sorted by descending ratio.
    """
    src_data, src_cpu = _load_rom_with_cpu(versions_dirpath, src_version)
    dst_data, dst_cpu = _load_rom_with_cpu(versions_dirpath, dst_version)

    src_insts = disassemble_to_opcodes(src_data, src_cpu)
    dst_insts = disassemble_to_opcodes(dst_data, dst_cpu)

    fp = opcodes_for_range(src_insts, src_start, src_end)
    if len(fp) < 4:
        return []

    dst_opcodes = bytes(op for _, op, _ in dst_insts)

    candidates = []
    for j in range(len(dst_opcodes) - len(fp)):
        window = dst_opcodes[j:j + len(fp)]
        sm = difflib.SequenceMatcher(None, fp, window, autojunk=False)
        ratio = sm.ratio()
        if ratio < min_ratio:
            continue
        candidates.append((ratio, ROM_BASE + dst_insts[j][0], len(fp)))

    candidates.sort(key=lambda t: -t[0])
    # Deduplicate near-duplicates (peak clusters)
    deduped = []
    for ratio, addr, n in candidates:
        if any(abs(addr - a2) <= 8 for _, a2, _ in deduped):
            continue
        deduped.append((ratio, addr, n))
        if len(deduped) >= top_n:
            break
    return deduped
