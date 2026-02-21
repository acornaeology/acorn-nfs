"""CLI entry point for acorn-nfs."""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def find_repo_root():
    """Find the repository root by looking for pyproject.toml."""
    dirpath = Path(__file__).resolve().parent
    while dirpath != dirpath.parent:
        if (dirpath / "pyproject.toml").exists():
            return dirpath
        dirpath = dirpath.parent
    raise RuntimeError("Could not find repository root")


def get_version_dirpath(version):
    """Return the path to a version directory, raising if it doesn't exist."""
    repo_root = find_repo_root()
    version_dirpath = repo_root / "versions" / version
    if not version_dirpath.is_dir():
        available = sorted(
            p.name for p in (repo_root / "versions").iterdir() if p.is_dir()
        )
        print(f"Error: version '{version}' not found.", file=sys.stderr)
        if available:
            print(f"Available versions: {', '.join(available)}", file=sys.stderr)
        sys.exit(1)
    return version_dirpath


def cmd_disassemble(args):
    """Run the disassembly for a given NFS version."""
    version_dirpath = get_version_dirpath(args.version)
    script_filepath = version_dirpath / "disassemble" / "nfs_334_v2.py"

    if not script_filepath.exists():
        print(f"Error: {script_filepath} not found", file=sys.stderr)
        sys.exit(1)

    env = os.environ.copy()
    env["ACORN_NFS_ROM"] = str(version_dirpath / "rom" / f"nfs-{args.version}.rom")
    env["ACORN_NFS_OUTPUT"] = str(version_dirpath / "output")

    result = subprocess.run(
        [sys.executable, str(script_filepath)],
        env=env,
    )
    sys.exit(result.returncode)


def cmd_correlate(args):
    """Run the correlation tool for a given NFS version."""
    version_dirpath = get_version_dirpath(args.version)
    script_filepath = version_dirpath / "disassemble" / "correlate_nfs.py"

    if not script_filepath.exists():
        print(f"Error: {script_filepath} not found", file=sys.stderr)
        sys.exit(1)

    result = subprocess.run(
        [sys.executable, str(script_filepath)],
        env=os.environ.copy(),
    )
    sys.exit(result.returncode)


def cmd_verify(args):
    """Assemble the disassembly and verify it matches the original ROM."""
    from acorn_nfs.verify import verify

    version_dirpath = get_version_dirpath(args.version)
    sys.exit(verify(version_dirpath, args.version))


def main():
    parser = argparse.ArgumentParser(
        prog="acorn-nfs",
        description="Acorn NFS ROM disassembly tools",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    dis_parser = subparsers.add_parser(
        "disassemble", help="Run disassembly for an NFS version"
    )
    dis_parser.add_argument("version", help="NFS version (e.g. 3.34)")
    dis_parser.set_defaults(func=cmd_disassemble)

    cor_parser = subparsers.add_parser(
        "correlate", help="Run correlation tool for an NFS version"
    )
    cor_parser.add_argument("version", help="NFS version (e.g. 3.34)")
    cor_parser.set_defaults(func=cmd_correlate)

    verify_parser = subparsers.add_parser(
        "verify", help="Verify disassembly round-trips to original ROM"
    )
    verify_parser.add_argument("version", help="NFS version (e.g. 3.34)")
    verify_parser.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    args.func(args)
