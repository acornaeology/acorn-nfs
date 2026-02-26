"""CLI entry point for acorn-nfs-disasm-tool."""

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
    script_filename = f"disasm_nfs_{args.version.replace('.', '').lower()}.py"
    script_filepath = version_dirpath / "disassemble" / script_filename

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
    from disasm_tools.verify import verify

    version_dirpath = get_version_dirpath(args.version)
    sys.exit(verify(version_dirpath, args.version))


def cmd_lint(args):
    """Validate annotation addresses against the disassembly output."""
    from disasm_tools.lint import lint

    version_dirpath = get_version_dirpath(args.version)
    sys.exit(lint(version_dirpath, args.version))


def cmd_compare(args):
    """Compare two ROM versions byte-by-byte and instruction-by-instruction."""
    from disasm_tools.compare import compare

    version_dirpath_a = get_version_dirpath(args.version_a)
    version_dirpath_b = get_version_dirpath(args.version_b)
    sys.exit(compare(version_dirpath_a, args.version_a,
                     version_dirpath_b, args.version_b))


def cmd_extract(args):
    """Extract a section of disassembly output by address range or label."""
    from disasm_tools.asm_extract import extract

    version_dirpath = get_version_dirpath(args.version)
    asm_filepath = version_dirpath / "output" / f"nfs-{args.version}.asm"

    if not asm_filepath.exists():
        print(f"Error: {asm_filepath} not found (run disassemble first)", file=sys.stderr)
        sys.exit(1)

    sys.exit(extract(str(asm_filepath), args.start, args.end))


def cmd_audit(args):
    """Audit subroutine annotations."""
    from disasm_tools.audit import audit

    version_dirpath = get_version_dirpath(args.version)
    sys.exit(audit(version_dirpath, args.version,
                   sub_target=args.sub, summary=args.summary,
                   flag_filter=args.flag))


def cmd_cfg(args):
    """Build and query the inter-procedural call graph."""
    from disasm_tools.cfg import cfg

    version_dirpath = get_version_dirpath(args.version)
    sys.exit(cfg(version_dirpath, args.version,
                 fmt=args.format, leaves=args.leaves, roots=args.roots,
                 sub=args.sub, depth=args.depth))


def cmd_context(args):
    """Generate per-subroutine context files for inline commenting."""
    from disasm_tools.context import generate_context

    version_dirpath = get_version_dirpath(args.version)
    output_dirpath = Path(args.output) if args.output else None
    sys.exit(generate_context(version_dirpath, args.version,
                              threshold=args.threshold,
                              output_dirpath=output_dirpath,
                              single_sub=args.sub,
                              summary_only=args.summary))


def cmd_backfill(args):
    """Propagate annotations from a richly-annotated version to an earlier one."""
    from disasm_tools.backfill import backfill

    repo_root = find_repo_root()
    # Validate both versions exist
    get_version_dirpath(args.version)
    get_version_dirpath(args.source)
    sys.exit(backfill(repo_root, args.source, args.version,
                      threshold=args.threshold, dry_run=args.dry_run))


def cmd_labels(args):
    """Generate per-label context files for label renaming."""
    from disasm_tools.labels import generate_labels

    version_dirpath = get_version_dirpath(args.version)
    output_dirpath = Path(args.output) if args.output else None
    sys.exit(generate_labels(version_dirpath, args.version,
                             output_dirpath=output_dirpath,
                             category_filter=args.category,
                             single_label=args.label,
                             summary_only=args.summary))


def main():
    parser = argparse.ArgumentParser(
        prog="acorn-nfs-disasm-tool",
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

    lint_parser = subparsers.add_parser(
        "lint", help="Validate annotation addresses in driver script"
    )
    lint_parser.add_argument("version", help="NFS version (e.g. 3.34)")
    lint_parser.set_defaults(func=cmd_lint)

    compare_parser = subparsers.add_parser(
        "compare", help="Compare two ROM versions"
    )
    compare_parser.add_argument("version_a", help="First NFS version (e.g. 3.34)")
    compare_parser.add_argument("version_b", help="Second NFS version (e.g. 3.34B)")
    compare_parser.set_defaults(func=cmd_compare)

    extract_parser = subparsers.add_parser(
        "extract", help="Extract assembly section by address or label"
    )
    extract_parser.add_argument("version", help="NFS version (e.g. 3.35K)")
    extract_parser.add_argument("start", help="Start address (hex) or label name")
    extract_parser.add_argument("end", nargs="?", default=None,
                                help="End address (hex) or label name (optional)")
    extract_parser.set_defaults(func=cmd_extract)

    audit_parser = subparsers.add_parser(
        "audit", help="Audit subroutine annotations"
    )
    audit_parser.add_argument("version", help="NFS version (e.g. 3.34)")
    audit_parser.add_argument("--sub", help="Detail for one subroutine (addr or name)")
    audit_parser.add_argument("--summary", action="store_true",
                              help="Show summary table (default if no --sub)")
    audit_parser.add_argument("--flag", help="Filter summary by flag")
    audit_parser.set_defaults(func=cmd_audit)

    cfg_parser = subparsers.add_parser(
        "cfg", help="Build and query inter-procedural call graph"
    )
    cfg_parser.add_argument("version", help="NFS version (e.g. 3.34)")
    cfg_parser.add_argument("--format", default="json",
                            choices=["json", "dot"],
                            help="Output format (default: json)")
    cfg_parser.add_argument("--leaves", action="store_true",
                            help="List leaf subroutines (no outgoing calls)")
    cfg_parser.add_argument("--roots", action="store_true",
                            help="List root subroutines (no incoming calls)")
    cfg_parser.add_argument("--sub", help="Show callers/callees of a subroutine")
    cfg_parser.add_argument("--depth", action="store_true",
                            help="Show call depth from leaves")
    cfg_parser.set_defaults(func=cmd_cfg)

    context_parser = subparsers.add_parser(
        "context", help="Generate per-subroutine context files for commenting"
    )
    context_parser.add_argument("version", help="NFS version (e.g. 3.60)")
    context_parser.add_argument("--threshold", type=float, default=50,
                                help="Max comment density %% to include "
                                     "(default: 50)")
    context_parser.add_argument("--output", help="Output directory "
                                "(default: versions/<ver>/context/)")
    context_parser.add_argument("--sub",
                                help="Generate for one subroutine only "
                                     "(addr or name)")
    context_parser.add_argument("--summary", action="store_true",
                                help="Print summary stats only, no files")
    context_parser.set_defaults(func=cmd_context)

    backfill_parser = subparsers.add_parser(
        "backfill", help="Propagate annotations from one version to another"
    )
    backfill_parser.add_argument("version",
                                 help="Target NFS version (e.g. 3.40)")
    backfill_parser.add_argument("--from", dest="source", default="3.60",
                                 help="Source version (default: 3.60)")
    backfill_parser.add_argument("--threshold", type=int, default=5,
                                 help="Min matching opcode block length "
                                      "(default: 5)")
    backfill_parser.add_argument("--dry-run", action="store_true",
                                 help="Show what would be added without "
                                      "modifying files")
    backfill_parser.set_defaults(func=cmd_backfill)

    labels_parser = subparsers.add_parser(
        "labels", help="Generate per-label context files for renaming"
    )
    labels_parser.add_argument("version", help="NFS version (e.g. 3.60)")
    labels_parser.add_argument("--output", help="Output directory "
                               "(default: versions/<ver>/labels/)")
    labels_parser.add_argument("--category",
                               choices=["subroutine", "shared_tail", "data",
                                        "internal_loop",
                                        "internal_conditional"],
                               help="Filter to one category")
    labels_parser.add_argument("--label",
                               help="Generate for one label only "
                                    "(addr or name)")
    labels_parser.add_argument("--summary", action="store_true",
                               help="Print summary stats only, no files")
    labels_parser.set_defaults(func=cmd_labels)

    args = parser.parse_args()
    args.func(args)
