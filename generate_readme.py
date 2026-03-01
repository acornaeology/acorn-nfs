#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["jinja2>=3.1"]
# ///
"""Generate README.md from project metadata and a Jinja2 template."""

import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

REPO_ROOT = Path(__file__).resolve().parent
REPO_URL = "https://github.com/acornaeology/acorn-nfs"
SITE_URL = "https://acornaeology.uk"


def resolve_version_dirpath(versions_dirpath, version_id):
    """Map a version ID to its prefixed directory (anfs-/nfs-)."""
    for prefix in ("anfs", "nfs"):
        dirpath = versions_dirpath / f"{prefix}-{version_id}"
        if dirpath.is_dir():
            return dirpath
    print(f"Error: version directory not found for '{version_id}'", file=sys.stderr)
    sys.exit(1)


def main():
    manifest = json.loads((REPO_ROOT / "acornaeology.json").read_text())
    slug = manifest["slug"]

    versions = []
    for version_id in manifest["versions"]:
        version_dirpath = resolve_version_dirpath(REPO_ROOT / "versions", version_id)
        version_dirname = version_dirpath.name
        prefix = version_dirname.split("-", 1)[0]
        rom_meta = json.loads(
            (version_dirpath / "rom" / "rom.json").read_text()
        )

        docs = []
        for doc in rom_meta.get("docs", []):
            docs.append({
                "label": doc["label"],
                "path": f"versions/{version_dirname}/{doc['path']}",
            })

        versions.append({
            "id": version_id,
            "title": rom_meta.get("title", f"{manifest['name']} {version_id}"),
            "site_url": f"{SITE_URL}/{slug}/{version_id}.html",
            "asm_path": f"versions/{version_dirname}/output/{prefix}-{version_id}.asm",
            "links": rom_meta.get("links", []),
            "docs": docs,
        })

    env = Environment(
        loader=FileSystemLoader(REPO_ROOT),
        keep_trailing_newline=True,
    )
    template = env.get_template("README.md.j2")

    readme_text = template.render(
        name=manifest["name"],
        description=manifest["description"],
        repo_url=REPO_URL,
        versions=versions,
        references=manifest.get("references", []),
    )

    readme_filepath = REPO_ROOT / "README.md"
    readme_filepath.write_text(readme_text)
    print(f"Generated {readme_filepath.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
