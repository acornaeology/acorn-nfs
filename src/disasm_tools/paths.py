"""Shared path resolution for version directories."""

import sys
from pathlib import Path


def resolve_version_dirpath(versions_dirpath, version_id):
    """Map a version ID to its prefixed directory (anfs-/nfs-).

    Tries anfs-{version_id} first, then nfs-{version_id}.
    Raises SystemExit if no matching directory is found.
    """
    for prefix in ("anfs", "nfs"):
        dirpath = versions_dirpath / f"{prefix}-{version_id}"
        if dirpath.is_dir():
            return dirpath
    available = sorted(
        p.name for p in versions_dirpath.iterdir() if p.is_dir()
    )
    print(f"Error: version '{version_id}' not found.", file=sys.stderr)
    if available:
        print(f"Available: {', '.join(available)}", file=sys.stderr)
    sys.exit(1)


def rom_prefix(version_dirpath):
    """Extract ROM prefix (nfs/anfs) from a version directory name."""
    return version_dirpath.name.split("-", 1)[0]
