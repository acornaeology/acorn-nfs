#!/usr/bin/env python3
"""Generate README.md from project metadata."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
REPO_URL = "https://github.com/acornaeology/acorn-nfs"


def main():
    manifest = json.loads((REPO_ROOT / "acornaeology.json").read_text())
    name = manifest["name"]
    description = manifest["description"]
    versions = manifest["versions"]

    lines = []

    lines.append(f"# {name}")
    lines.append("")
    lines.append(
        "[![Verify disassembly]"
        f"({REPO_URL}/actions/workflows/verify.yml/badge.svg)]"
        f"({REPO_URL}/actions/workflows/verify.yml)"
    )
    lines.append("")
    lines.append(description)
    lines.append("")
    lines.append(
        "This repository contains annotated disassemblies of the Acorn NFS ROM, "
        "produced by reverse-engineering the original 6502 machine code. Each "
        "disassembly includes named labels, comments explaining the logic, and "
        "cross-references between subroutines."
    )
    lines.append("")

    lines.append("## Versions")
    lines.append("")
    for version_id in versions:
        version_dirpath = REPO_ROOT / "versions" / version_id
        rom_json_filepath = version_dirpath / "rom" / "rom.json"
        rom_meta = json.loads(rom_json_filepath.read_text())
        title = rom_meta.get("title", f"{name} {version_id}")

        site_url = f"https://acornaeology.uk/{manifest['slug']}/{version_id}.html"
        asm_path = f"versions/{version_id}/output/nfs-{version_id}.asm"

        lines.append(f"### {title}")
        lines.append("")
        lines.append(
            f"- [Formatted disassembly on acornaeology.uk]({site_url})"
        )
        lines.append(f"- [Raw assembly source]({asm_path})")

        for link in rom_meta.get("links", []):
            lines.append(f"- [{link['label']}]({link['url']})")

        lines.append("")

    lines.append("## How it works")
    lines.append("")
    lines.append(
        "The disassembly is produced by a Python script that drives "
        "a custom version of [py8dis](https://github.com/acornaeology/py8dis), a programmable "
        "disassembler for 6502 binaries. The script feeds the original ROM "
        "image to py8dis along with annotations — entry points, labels, "
        "constants, and comments — to produce readable assembly output."
    )
    lines.append("")
    lines.append(
        "The output is verified by reassembling with "
        "[beebasm](https://github.com/stardot/beebasm) and comparing the "
        "result byte-for-byte against the original ROM. This round-trip "
        "verification runs automatically in CI on every push."
    )
    lines.append("")

    lines.append("## Building locally")
    lines.append("")
    lines.append("Requires [uv](https://docs.astral.sh/uv/) and "
                 "[beebasm](https://github.com/stardot/beebasm).")
    lines.append("")
    lines.append("```sh")
    lines.append("uv sync")
    for version_id in versions:
        lines.append(f"uv run acorn-nfs disassemble {version_id}")
        lines.append(f"uv run acorn-nfs verify {version_id}")
    lines.append("```")
    lines.append("")

    references = manifest.get("references", [])
    if references:
        lines.append("## References")
        lines.append("")
        for ref in references:
            lines.append(f"- [{ref['label']}]({ref['url']})")
            if "note" in ref:
                lines.append(f"  {ref['note']}")
        lines.append("")

    lines.append("## Credits")
    lines.append("")
    lines.append(
        "- [py8dis](https://github.com/acornaeology/py8dis) by "
        "[SteveF](https://github.com/ZornsLemma), forked for use with "
        "acornaeology"
    )
    lines.append(
        "- [beebasm](https://github.com/stardot/beebasm) by Rich Mayfield "
        "and contributors"
    )
    lines.append(
        "- [The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/) "
        "by tobylobster"
    )
    lines.append("")

    lines.append("## License")
    lines.append("")
    lines.append(
        "The annotations and disassembly scripts in this repository are "
        "released under the [MIT License](LICENSE). The original ROM images "
        "remain the property of their respective copyright holders."
    )
    lines.append("")

    readme_filepath = REPO_ROOT / "README.md"
    readme_filepath.write_text("\n".join(lines))
    print(f"Generated {readme_filepath.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
