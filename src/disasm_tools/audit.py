"""Audit subroutine annotations in NFS ROM disassembly output.

Analyses the JSON output to compute subroutine extents, detect fall-throughs,
find entry references, and flag potential annotation issues. Three output modes:
  --summary:      Table of all subroutines with computed flags
  --sub <target>: Full audit report for one subroutine
  --flag <FLAG>:  Summary filtered to one flag category
"""

import json
import re
import sys
from pathlib import Path

# Mnemonics that unconditionally terminate control flow
TERMINATING_MNEMONICS = {"rts", "jmp", "brk", "rti"}

# Branch mnemonics (conditional)
BRANCH_MNEMONICS = {"bcc", "bcs", "beq", "bne", "bmi", "bpl", "bvc", "bvs"}

# Memory regions: subroutines only extend within their region
MEMORY_REGIONS = [
    (0x0016, 0x0076),   # zero page workspace
    (0x0400, 0x04FF),   # relocated page 4
    (0x0500, 0x05FF),   # relocated page 5
    (0x0600, 0x06FF),   # relocated page 6
    (0x0D00, 0x0DFF),   # NMI workspace
    (0x8000, 0x9FFF),   # ROM
]


def region_for_addr(addr):
    """Return the memory region (start, end) containing addr, or None."""
    for start, end in MEMORY_REGIONS:
        if start <= addr <= end:
            return (start, end)
    return None


def find_containing_sub(addr, rom_subs):
    """Find the subroutine containing addr (last sub with start <= addr)."""
    result = None
    for s in rom_subs:
        if s["addr"] <= addr:
            result = s
        else:
            break
    return result


def load_subroutines(json_filepath):
    """Load JSON output, compute subroutine extents and flags.

    Returns a list of subroutine dicts augmented with:
      items, code_count, data_count, last_mnemonic, terminates,
      next_sub, entry_refs, escaping_branches, flags
    """
    data = json.loads(Path(json_filepath).read_text())
    items = data["items"]
    raw_subs = data.get("subroutines", [])

    # Filter out OS entry points (addr >= 0xFF00) — these are stubs
    rom_subs = [s for s in raw_subs if s["addr"] < 0xFF00]
    rom_subs.sort(key=lambda s: s["addr"])

    # Build addr→item index
    items_by_addr = {item["addr"]: item for item in items}
    sorted_items = sorted(items, key=lambda i: i["addr"])

    # Build target→referencing-items index for entry ref lookups
    target_refs = {}
    for item in items:
        t = item.get("target")
        if t is not None:
            target_refs.setdefault(t, []).append(item)

    # First pass: compute extents and basic properties for all subs,
    # so the second pass can look up predecessor termination status.
    sub_data = []

    for idx, sub in enumerate(rom_subs):
        sub_addr = sub["addr"]
        sub_region = region_for_addr(sub_addr)

        # Find extent end: next sub in same region, or region end
        extent_end = None
        next_sub_info = None
        for j in range(idx + 1, len(rom_subs)):
            candidate = rom_subs[j]
            if region_for_addr(candidate["addr"]) == sub_region:
                extent_end = candidate["addr"]
                next_sub_info = {
                    "addr": candidate["addr"],
                    "name": candidate.get("name", "?"),
                }
                break

        # Collect items in this sub's extent
        sub_items = []
        for item in sorted_items:
            if item["addr"] < sub_addr:
                continue
            if extent_end is not None and item["addr"] >= extent_end:
                break
            # Must be in same region
            if sub_region and region_for_addr(item["addr"]) == sub_region:
                sub_items.append(item)
            elif sub_region is None:
                if extent_end is None or item["addr"] < extent_end:
                    sub_items.append(item)

        code_count = sum(1 for i in sub_items if i.get("type") == "code")
        data_count = len(sub_items) - code_count

        # Find last code item for termination check
        code_items = [i for i in sub_items if i.get("type") == "code"]
        last_mnemonic = code_items[-1].get("mnemonic") if code_items else None
        terminates = last_mnemonic in TERMINATING_MNEMONICS if last_mnemonic else False

        # py8dis reference tracking: the 'references' field on the item at
        # sub_addr lists all addresses that reference this location, including
        # operand targets, data table entries, and relocated code pointers.
        item_at_addr = items_by_addr.get(sub_addr)
        has_any_refs = bool(item_at_addr and item_at_addr.get("references"))

        # Entry references: JSR/JMP from elsewhere targeting this sub's addr
        entry_refs = []
        for ref_item in target_refs.get(sub_addr, []):
            if ref_item.get("mnemonic") in ("jsr", "jmp"):
                containing = find_containing_sub(ref_item["addr"], rom_subs)
                ref_sub_name = containing.get("name", f"&{containing['addr']:04X}") if containing else "?"
                entry_refs.append({
                    "addr": ref_item["addr"],
                    "mnemonic": ref_item["mnemonic"],
                    "in_sub": ref_sub_name,
                })

        # Branch references (conditional branches targeting this sub's addr)
        branch_entry_refs = []
        for ref_item in target_refs.get(sub_addr, []):
            if ref_item.get("mnemonic") in BRANCH_MNEMONICS:
                containing = find_containing_sub(ref_item["addr"], rom_subs)
                ref_sub_name = containing.get("name", f"&{containing['addr']:04X}") if containing else "?"
                branch_entry_refs.append({
                    "addr": ref_item["addr"],
                    "mnemonic": ref_item["mnemonic"],
                    "in_sub": ref_sub_name,
                })

        # Escaping branches: branch items within extent whose target is outside
        escaping_branches = []
        for item in sub_items:
            if item.get("mnemonic") in BRANCH_MNEMONICS:
                target = item.get("target")
                if target is not None:
                    in_extent = (sub_addr <= target < extent_end) if extent_end else (target >= sub_addr)
                    if not in_extent:
                        escaping_branches.append({
                            "addr": item["addr"],
                            "mnemonic": item["mnemonic"],
                            "target": target,
                            "target_label": item.get("target_label", f"&{target:04X}"),
                        })

        sub_data.append({
            "sub": sub,
            "idx": idx,
            "sub_addr": sub_addr,
            "sub_region": sub_region,
            "sub_items": sub_items,
            "code_count": code_count,
            "data_count": data_count,
            "last_mnemonic": last_mnemonic,
            "terminates": terminates,
            "next_sub_info": next_sub_info,
            "has_any_refs": has_any_refs,
            "entry_refs": entry_refs,
            "branch_entry_refs": branch_entry_refs,
            "escaping_branches": escaping_branches,
        })

    # Second pass: compute flags using predecessor termination info
    results = []
    for i, sd in enumerate(sub_data):
        sub = sd["sub"]
        flags = set()

        if not sd["terminates"] and sd["next_sub_info"]:
            flags.add("FALL_THROUGH")

        # Determine predecessor in same region
        prev_terminates = True  # default for first sub in region
        if i > 0 and sub_data[i - 1]["sub_region"] == sd["sub_region"]:
            prev_terminates = sub_data[i - 1]["terminates"]

        has_direct_refs = bool(sd["entry_refs"]) or bool(sd["branch_entry_refs"])

        if not has_direct_refs and not sd["has_any_refs"]:
            if not prev_terminates:
                # Predecessor falls through AND no references anywhere —
                # genuinely reached only via fall-through
                flags.add("FALL_THROUGH_ENTRY")
            else:
                # Predecessor terminates but no references found —
                # likely called indirectly (dispatch table, vector, NMI install)
                flags.add("NO_REFS")
        elif not has_direct_refs and sd["has_any_refs"]:
            # Referenced somewhere (e.g. address taken for a table or vector)
            # but not via direct JSR/JMP/branch
            if not prev_terminates:
                flags.add("FALL_THROUGH_ENTRY")

        if sd["escaping_branches"]:
            flags.add("BRANCH_ESCAPE")

        if sd["code_count"] == 0 and sd["data_count"] > 0:
            flags.add("DATA_ONLY")

        name = sub.get("name", "")
        if re.match(r"sub_c[0-9a-f]+$", name):
            flags.add("AUTO_NAME")

        title = sub.get("title", "")
        description = sub.get("description", "")
        if not title and not description:
            flags.add("NO_DESCRIPTION")
        elif len(title) + len(description) < 40 and not description:
            flags.add("NO_DESCRIPTION")

        results.append({
            "addr": sd["sub_addr"],
            "name": name or f"&{sd['sub_addr']:04X}",
            "title": title,
            "description": description,
            "on_entry": sub.get("on_entry", ""),
            "on_exit": sub.get("on_exit", ""),
            "items": sd["sub_items"],
            "code_count": sd["code_count"],
            "data_count": sd["data_count"],
            "last_mnemonic": sd["last_mnemonic"],
            "terminates": sd["terminates"],
            "next_sub": sd["next_sub_info"],
            "entry_refs": sd["entry_refs"],
            "branch_entry_refs": sd["branch_entry_refs"],
            "escaping_branches": sd["escaping_branches"],
            "flags": flags,
        })

    return results


def end_type(sub):
    """Short string describing how a subroutine ends."""
    if sub["terminates"]:
        m = sub["last_mnemonic"].upper()
        return m
    if sub["next_sub"]:
        return "FALL\u2192"
    return "END"


def format_summary(subs, flag_filter=None):
    """Print summary table to stdout."""
    if flag_filter:
        flag_upper = flag_filter.upper()
        subs = [s for s in subs if flag_upper in s["flags"]]

    if not subs:
        print("No subroutines match the filter.")
        return

    # Header
    print(f"{'ADDR':<7s} {'NAME':<32s} {'END':<7s} {'ITEMS':>7s}  FLAGS")
    print(f"{'----':<7s} {'----':<32s} {'---':<7s} {'-----':>7s}  -----")

    for sub in subs:
        addr_str = f"&{sub['addr']:04X}"
        name = sub["name"][:31]
        end = end_type(sub)
        items_str = f"{sub['code_count']}/{sub['data_count']}"
        flags_str = ",".join(sorted(sub["flags"])) if sub["flags"] else ""
        print(f"{addr_str:<7s} {name:<32s} {end:<7s} {items_str:>7s}  {flags_str}")

    # Summary counts
    total = len(subs)
    rts_count = sum(1 for s in subs if s["last_mnemonic"] == "rts")
    jmp_count = sum(1 for s in subs if s["last_mnemonic"] == "jmp")
    fall_count = sum(1 for s in subs if not s["terminates"])
    print(f"\n{total} subroutines: {rts_count} RTS, {jmp_count} JMP, {fall_count} fall-through")

    # Flag totals
    all_flags = set()
    for s in subs:
        all_flags.update(s["flags"])
    if all_flags:
        flag_counts = []
        for flag in sorted(all_flags):
            count = sum(1 for s in subs if flag in s["flags"])
            flag_counts.append(f"{count} {flag}")
        print(f"Flags: {', '.join(flag_counts)}")


def format_detail(sub, asm_filepath):
    """Print full audit report for one subroutine."""
    print(f"## {sub['name']} (&{sub['addr']:04X})")

    if sub["title"]:
        print(f"Title: {sub['title']}")

    flags_str = ", ".join(sorted(sub["flags"])) if sub["flags"] else "none"
    print(f"Flags: {flags_str}")

    # Description
    print(f"\n### Description")
    if sub["description"]:
        print(sub["description"])
    elif sub["title"]:
        print(f"(title only: {sub['title']})")
    else:
        print("(no description)")

    if sub["on_entry"]:
        print(f"\nOn entry: {sub['on_entry']}")
    if sub["on_exit"]:
        print(f"On exit: {sub['on_exit']}")

    # Extent
    print(f"\n### Extent")
    if sub["items"]:
        first_addr = sub["items"][0]["addr"]
        last_addr = sub["items"][-1]["addr"]
        print(f"Address range: &{first_addr:04X}-&{last_addr:04X} "
              f"({sub['code_count']} code, {sub['data_count']} data items)")
    else:
        print("(no items)")

    end = end_type(sub)
    if sub["terminates"]:
        last_code = None
        for item in reversed(sub["items"]):
            if item.get("type") == "code":
                last_code = item
                break
        if last_code:
            operand = last_code.get("operand", "")
            print(f"Ends: {last_code['mnemonic'].upper()} {operand} (&{last_code['addr']:04X})")
    elif sub["next_sub"]:
        ns = sub["next_sub"]
        print(f"Ends: FALLS THROUGH to {ns['name']} (&{ns['addr']:04X})")

    # Called by
    all_refs = sub["entry_refs"]
    if all_refs:
        print(f"\n### Called by ({len(all_refs)} references)")
        for ref in sorted(all_refs, key=lambda r: r["addr"]):
            print(f"  &{ref['addr']:04X} {ref['mnemonic'].upper():<4s} "
                  f"(in {ref['in_sub']})")
    else:
        print(f"\n### Called by (0 references)")

    # Branch entry refs
    if sub["branch_entry_refs"]:
        print(f"\n### Branch entries ({len(sub['branch_entry_refs'])} references)")
        for ref in sorted(sub["branch_entry_refs"], key=lambda r: r["addr"]):
            print(f"  &{ref['addr']:04X} {ref['mnemonic'].upper():<4s} "
                  f"(in {ref['in_sub']})")

    # Escaping branches
    if sub["escaping_branches"]:
        print(f"\n### Escaping branches")
        for br in sorted(sub["escaping_branches"], key=lambda b: b["addr"]):
            print(f"  &{br['addr']:04X} {br['mnemonic'].upper()} "
                  f"\u2192 &{br['target']:04X} {br['target_label']}")

    # Assembly listing
    if asm_filepath and Path(asm_filepath).exists():
        from disasm_tools.asm_extract import build_index, find_line_for_target

        lines = Path(asm_filepath).read_text().splitlines(keepends=True)
        addr_to_line, label_to_line = build_index(lines)

        start_target = f"0x{sub['addr']:04X}"
        start_line = find_line_for_target(start_target, lines, addr_to_line, label_to_line)

        if start_line is not None:
            # Back up to include preceding comment/label lines
            while start_line > 0 and not re.search(r";\s*[0-9a-f]{4}:", lines[start_line - 1]):
                stripped = lines[start_line - 1].strip()
                if stripped == "" or stripped.startswith(";") or stripped.startswith("."):
                    start_line -= 1
                else:
                    break

            # Find end: use next_sub addr or fixed window
            if sub["next_sub"]:
                end_target = f"0x{sub['next_sub']['addr']:04X}"
                end_line = find_line_for_target(end_target, lines, addr_to_line, label_to_line)
                if end_line is not None:
                    # Back up over blank lines between subs
                    while end_line > start_line and lines[end_line - 1].strip() == "":
                        end_line -= 1
                else:
                    end_line = min(start_line + 60, len(lines))
            else:
                # Last sub in region — use last item addr
                if sub["items"]:
                    last_target = f"0x{sub['items'][-1]['addr']:04X}"
                    end_line = find_line_for_target(last_target, lines, addr_to_line, label_to_line)
                    if end_line is not None:
                        end_line += 1
                    else:
                        end_line = min(start_line + 60, len(lines))
                else:
                    end_line = min(start_line + 20, len(lines))

            print(f"\n### Assembly")
            for i in range(start_line, end_line):
                print(f"{i+1:5d}  {lines[i]}", end="")
            if not lines[end_line - 1].endswith("\n"):
                print()


def find_sub(subs, target):
    """Find a subroutine by address (hex) or name."""
    # Try as hex address
    addr_str = target.strip().lstrip("$&").removeprefix("0x")
    try:
        addr = int(addr_str, 16)
        for s in subs:
            if s["addr"] == addr:
                return s
    except ValueError:
        pass

    # Try as exact name
    for s in subs:
        if s["name"] == target:
            return s

    # Try partial name match
    matches = [s for s in subs if target in s["name"]]
    if len(matches) == 1:
        return matches[0]
    if matches:
        print(f"Ambiguous name '{target}', matches:", file=sys.stderr)
        for m in matches:
            print(f"  &{m['addr']:04X} {m['name']}", file=sys.stderr)
        return None

    print(f"Subroutine '{target}' not found", file=sys.stderr)
    return None


ALL_FLAGS = [
    "FALL_THROUGH", "FALL_THROUGH_ENTRY", "NO_REFS", "BRANCH_ESCAPE",
    "DATA_ONLY", "AUTO_NAME", "NO_DESCRIPTION",
]


def audit(version_dirpath, version, sub_target=None, summary=False, flag_filter=None):
    """Main entry point. Returns exit code 0 on success, 1 on error."""
    json_filepath = version_dirpath / "output" / f"nfs-{version}.json"
    asm_filepath = version_dirpath / "output" / f"nfs-{version}.asm"

    if not json_filepath.exists():
        print(f"Error: {json_filepath} not found (run disassemble first)",
              file=sys.stderr)
        return 1

    subs = load_subroutines(json_filepath)

    if sub_target:
        sub = find_sub(subs, sub_target)
        if sub is None:
            return 1
        format_detail(sub, asm_filepath)
    elif flag_filter:
        if flag_filter.upper() not in ALL_FLAGS:
            print(f"Unknown flag '{flag_filter}'. Available: {', '.join(ALL_FLAGS)}",
                  file=sys.stderr)
            return 1
        format_summary(subs, flag_filter=flag_filter)
    else:
        # Default to summary
        format_summary(subs)

    return 0
