#!/usr/bin/env python3
"""Find Markdown address links written inside backtick code spans.

Per `acornaeology.github.io/AUTHORING.md` §1.3, Markdown link syntax
inside a backtick code span is *not* interpreted -- the literal text
`[label](address:HEX)` is rendered as code, not as a hyperlink.

This tool scans the string literals of one or more driver scripts
and flags every code span that contains a `](address:` fragment
(the unmistakable middle of an `address:` link). The fix is one of:

- move the link outside the backticks
  (e.g. ```JMP` [name](address:HEX)``)
- pull the backticks inside the link label
  (e.g. ``[`name`](address:HEX)``)
- de-linkify by quoting just the name
  (e.g. ```JMP name```)

Exit status is non-zero when at least one offence is reported, so
the tool is suitable as a CI gate.
"""

import argparse
import ast
import re
import sys
from pathlib import Path

# The middle of an `address:` link. Anything else after `](` would also
# be a link, but we only care about the address: scheme here.
ADDRESS_LINK_RE = re.compile(r'\]\(address:')


def find_offences(text: str):
    """Return list of (offset_in_text, snippet) for code spans
    containing a Markdown address link.

    Algorithm: scan once, toggling an `in_span` flag at each backtick.
    When a span closes, look for an `](address:` fragment inside it;
    if found, report the full span.
    """
    offences = []
    in_span = False
    span_start = -1
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == '`':
            if not in_span:
                in_span = True
                span_start = i
            else:
                span_text = text[span_start + 1:i]
                if ADDRESS_LINK_RE.search(span_text):
                    offences.append((span_start, text[span_start:i + 1]))
                in_span = False
        i += 1
    return offences


def scan_file(path: Path):
    """Yield (line, snippet) tuples for offences in `path`."""
    src = path.read_text()
    tree = ast.parse(src, filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            for _, snippet in find_offences(node.value):
                yield node.lineno, snippet


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('paths', nargs='+', type=Path,
                   help='Driver Python files to scan')
    args = p.parse_args(argv)

    total = 0
    for path in args.paths:
        if not path.exists():
            print(f'{path}: not found', file=sys.stderr)
            return 2
        for line, snippet in scan_file(path):
            # Truncate very long snippets so the output stays readable
            display = snippet if len(snippet) <= 120 else snippet[:117] + '...'
            print(f'{path}:{line}: {display}')
            total += 1

    if total:
        print(f'\n{total} offence(s) found', file=sys.stderr)
        return 1
    print('OK -- no markdown address links inside backtick code spans')
    return 0


if __name__ == '__main__':
    sys.exit(main())
