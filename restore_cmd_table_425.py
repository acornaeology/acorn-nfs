#!/usr/bin/env python3
"""Restore the UNMAPPED _cmd_table_fs_entries tuples and handler_names loop
in the 4.25 driver.

generate_425.py UNMAPPED these because the command/vector tables hold
shifted handler addresses whose bytes changed with the +2 insertion at
&85AC, so the byte-verified interpolation (rightly conservative for
comments) also refused these structural definitions. The whole &A780-&A852
command-table region and the &8ECD extended-vector table shift by a uniform
+2, so restoring is a field-aware +2 remap. Verify is the safety net: the
d.expr(handler - 1) / d.word overrides reassemble to the original bytes only
if the addresses are right.
"""

import ast
import re
from pathlib import Path

D = Path('/Users/rjs/Code/acornaeology/acorn-nfs/versions/anfs-4.25'
         '/disassemble/disasm_anfs_425.py')
SHIFT = 2
ADDR_LOOP = 0x85AC


def shift_addr(a):
    return a + SHIFT if 0x8000 <= a <= 0xBFFF and a >= ADDR_LOOP else a


def shift_prose_addrs(s):
    def repl(m):
        a = int(m.group(1), 16)
        return '&%04X' % shift_addr(a) if 0x8000 <= a <= 0xBFFF else m.group(0)
    return re.sub(r'&([0-9A-Fa-f]{4})', repl, s)


text = D.read_text()

# --- 1. cmd-table tuples ---------------------------------------------------
n_tuples = 0


def restore_tuple(m):
    global n_tuples
    tup = ast.literal_eval(m.group(1))
    name_addr, name, flag_addr, flag_byte, lo_addr, target, role = tup
    role = shift_prose_addrs(role)
    target_repr = 'None' if target is None else repr(target)
    n_tuples += 1
    return ('(0x%04X, %r, 0x%04X, 0x%02X, 0x%04X, %s, %r),'
            % (shift_addr(name_addr), name, shift_addr(flag_addr), flag_byte,
               shift_addr(lo_addr), target_repr, role))


text = re.sub(r'# UNMAPPED: (\(0x[0-9A-Fa-f]+,.*\)),\s*$',
              restore_tuple, text, flags=re.MULTILINE)

# --- 2. handler_names loop (exact block replacement) -----------------------
old_block = '''# UNMAPPED: for i, (name, handler_label) in enumerate(handler_names):
# UNMAPPED:     base_addr = 0x8ECD + i * 3
# UNMAPPED (orphan body):     d.word(base_addr)
# UNMAPPED (orphan body):     d.expr(base_addr, sym(handler_label))
# UNMAPPED (orphan body):     d.comment(base_addr, "%s handler" % name, align=Align.INLINE)
# UNMAPPED (orphan body):     if i < 6:
# UNMAPPED (orphan body):         d.byte(base_addr + 2, 1)
# UNMAPPED (orphan body):         d.comment(base_addr + 2, "(ROM bank — not read)", align=Align.INLINE)'''

new_block = '''for i, (name, handler_label) in enumerate(handler_names):
    base_addr = 0x%04X + i * 3
    d.word(base_addr)
    d.expr(base_addr, sym(handler_label))
    d.comment(base_addr, "%%s handler" %% name, align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, "(ROM bank — not read)", align=Align.INLINE)''' % shift_addr(0x8ECD)

assert text.count(old_block) == 1, "handler_names block not found uniquely"
text = text.replace(old_block, new_block)

D.write_text(text)
print(f"Restored {n_tuples} cmd-table tuples + handler_names loop "
      f"(ext-vector base 0x{shift_addr(0x8ECD):04X})")
