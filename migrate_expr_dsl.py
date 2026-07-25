#!/usr/bin/env python3
"""Migrate `d.expr(addr, <string>)` operand overrides to the dasmos 4
expression DSL (`dasmos.expr.sym/lo/hi`), so operand references are
validated symbols rather than opaque strings.

Renders identically (verified) but a stale/typo'd `sym("name")` now
errors at build time. AST-based: finds each `d.expr(...)` call and
replaces exactly the operand-argument source span — no text search and
replace. `d.expr_label(...)` is left alone (string-only dasmos API).

Handled operand forms:
  "<(NAME)"            -> lo(sym("NAME"))
  "<(NAME-1)"          -> lo(sym("NAME") - 1)
  ">(NAME)"            -> hi(sym("NAME"))
  "A - B"              -> sym("A") - sym("B")     (label/const difference)
  "A - 1"              -> sym("A") - 1
  "<(%s-1)" % var      -> lo(sym(var) - 1)        (loop-built)
  target_label         -> sym(target_label)        (bare variable)
  target_label + "-1"  -> sym(target_label) - 1
"""
import ast
import re
import sys
from pathlib import Path


def num_or_name(tok, quote):
    """Render a single term of the inner arithmetic as DSL source."""
    tok = tok.strip()
    if tok == "%s":
        return None  # sentinel: substitute the template variable
    m = re.fullmatch(r"&([0-9A-Fa-f]+)", tok)
    if m:
        return f"0x{m.group(1)}"
    if re.fullmatch(r"0x[0-9A-Fa-f]+|\d+", tok):
        return tok
    if re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]*", tok):
        return f'sym("{tok}")' if quote else f"sym({tok})"
    raise ValueError(f"unparseable term {tok!r}")


def inner_to_dsl(inner, var=None):
    """Parse `NAME`, `NAME-1`, `A - B`, `%s-1` into DSL source. `var` is
    the template variable name substituted for `%s` (unquoted sym)."""
    parts = re.split(r"\s*([+-])\s*", inner.strip())
    terms = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            terms.append(p)  # operator
            continue
        t = num_or_name(p, quote=(var is None))
        if t is None:  # %s placeholder
            t = f"sym({var})"
        terms.append(t)
    return " ".join(terms)


def string_to_dsl(s, var=None):
    """Convert an operand string (or template body) to DSL source.

    Raises ValueError on forms we deliberately do not touch (e.g. a
    `(...) AND &FF` mask, which renders differently from `lo(...)`); the
    caller treats that as "leave as a string".
    """
    s = s.strip()
    if "AND" in s or " OR " in s or " EOR " in s:
        raise ValueError(f"bitwise expr left as string: {s!r}")
    m = re.fullmatch(r"([<>])\((.*)\)", s)          # <(inner)
    if not m:
        m = re.fullmatch(r"([<>])\s*([A-Za-z_].*)", s)  # <label (no parens)
    if m:
        wrap = "lo" if m.group(1) == "<" else "hi"
        return f"{wrap}({inner_to_dsl(m.group(2), var)})"
    return inner_to_dsl(s, var)


def arg_to_dsl(node):
    """Given the operand-argument AST node, return DSL source or None to
    skip (already DSL / unrecognised)."""
    # bare string literal
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return string_to_dsl(node.value)
    # "template" % var
    if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod)
            and isinstance(node.left, ast.Constant)
            and isinstance(node.left.value, str)
            and isinstance(node.right, ast.Name)):
        return string_to_dsl(node.left.value, var=node.right.id)
    # bare variable holding a label name
    if isinstance(node, ast.Name):
        return f"sym({node.id})"
    # var + "-1"  /  var + "+8"
    if (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)
            and isinstance(node.left, ast.Name)
            and isinstance(node.right, ast.Constant)
            and isinstance(node.right.value, str)):
        tail = node.right.value.strip()
        m = re.fullmatch(r"([+-])\s*(&?[0-9A-Fa-fx]+)", tail)
        if m:
            op = m.group(1)
            n = m.group(2).replace("&", "0x")
            return f"sym({node.left.id}) {op} {n}"
    return None  # already a Call (lo/hi/sym) or unknown -> leave


def migrate(path: Path):
    src = path.read_text()
    tree = ast.parse(src)
    edits = []  # (start_offset, end_offset, replacement)
    skipped = []
    lines = src.splitlines(keepends=True)
    line_start = [0]
    for ln in lines:
        line_start.append(line_start[-1] + len(ln))

    def off(lineno, col):
        return line_start[lineno - 1] + col

    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "expr"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "d"):
            continue
        if len(node.args) < 2:
            continue
        arg = node.args[1]
        try:
            dsl = arg_to_dsl(arg)
        except ValueError as exc:
            skipped.append(str(exc))
            continue
        if dsl is None:
            continue
        s = off(arg.lineno, arg.col_offset)
        e = off(arg.end_lineno, arg.end_col_offset)
        edits.append((s, e, dsl))

    if not edits:
        return 0, skipped
    edits.sort(reverse=True)
    for s, e, dsl in edits:
        src = src[:s] + dsl + src[e:]

    # ensure the DSL import is present
    if "from dasmos.expr import" not in src:
        src = re.sub(r"(^import dasmos\b.*?$)",
                     r"\1\nfrom dasmos.expr import sym, lo, hi",
                     src, count=1, flags=re.M)
    path.write_text(src)
    return len(edits), skipped


if __name__ == "__main__":
    for p in sys.argv[1:]:
        n, skipped = migrate(Path(p))
        print(f"{p}: migrated {n} d.expr operands"
              + (f" (skipped {len(skipped)}: {skipped})" if skipped else ""))
