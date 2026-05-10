# Comment-format sweep — progress tracker

Branch: `comment-format`. Goal: upgrade `comment()` / `subroutine()` / `label()`
strings in NFS driver scripts to use the inline-Markdown features described in
`/Users/rjs/Code/acornaeology/acornaeology.github.io/AUTHORING.md`.

## Methodology

1. **Section by section.** Pick an address range (e.g. ZP Tube glue at &0016–&006F)
   and sweep it across all 8 NFS drivers in lockstep. Smaller sections commit cleanly.
2. **Linkify.** Convert `` `label_name` at `&XXXX` `` → `[label_name](address:XXXX?hex)`,
   plain `&XXXX` → `[label](address:XXXX)` when a name is available, etc. Drop the
   `?hex` suffix unless the hex *itself* is load-bearing (typical guidance from user).
3. **Restructure.** Promote prose lists / dispatch tables in `description=`
   blocks to GFM bullets / tables. Use the en-dash (` – `) and arrow (`→`)
   typography from §1.4 of the authoring guide. Apply the tooltip-boundary
   `\n` convention to memory-map labels (§3.2).
4. **Cross-version propagation.** A description in 3.34 is usually shared with
   3.34B / 3.35D / 3.35K / 3.40 / 3.60 / 3.62 / 3.65 (sometimes with an address
   shift). After upgrading one version, propagate the same edit to the others —
   adapting addresses where needed. **Don't paste uncritically:** verify the
   address resolves to a label with the same role in each target version.
5. **Verify after every section.** `uv run fantasm verify <ver>` for each
   touched version, then `uv run fantasm lint <ver>` and `uv run fantasm
   comments check <ver>` (HIGH-strict before commit).
6. **Commit per section.** Single bundled commit covering all 8 versions.

## Tooling

- `/tmp/scan_driver.py <driver> <json> --start &XXXX --end &YYYY` — AST-based
  scan of a single driver: lists every bare `&XXXX` occurrence in `comment()` /
  `subroutine()` / `label()` strings, with the resolved label (if any) and a
  context snippet.
- `uv run fantasm comments check <ver>` — vendor consistency checker
  (HIGH = blocking; MEDIUM = stale-addr report, useful while sweeping).
- `uv run fantasm asm extract <ver> &START &END` — render a numbered slice
  of the rendered .asm so we can read the listing without opening the file.
- `uv run fantasm annotations diff <src> <tgt>` — confirm a comment really is
  shared across versions (or has drifted).

## Section status

| Section | Range | 3.34 | 3.34B | 3.35D | 3.35K | 3.40 | 3.60 | 3.62 | 3.65 |
|---------|-------|------|-------|-------|-------|------|------|------|------|
| Tube glue (ZP)        | &0016–&006F | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Reloc p4              | &0400–&04FF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Reloc p5/p6           | &0500–&06FF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ROM header / service  | &8000–&80CF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| FSCV                  | &80D0–&82FF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| File handle ops       | &8300–&8AFF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Star commands         | &8B00–&92FF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Net protocol          | &9300–&9FFF | . | . | . | . | . | . | . | . |

Legend: `.` = pending, `~` = in-progress, `✓` = swept + verified.

## Notes

- ANFS (4.08.53 / 4.18 / 4.21_variant_1) deferred. 4.21 already follows the
  conventions; 4.18 + 4.08.53 would be a follow-up sweep.
- The tooltip-boundary `\n` convention applies to **memory-map** labels
  (§3.2) not to inline comments. Don't add `\n` markers where they don't belong.
- Driver-internal `# comments` (Python source comments) are out of scope —
  only the strings passed to dasmos calls render to HTML.
- **Don't `address:` link external/MOS environment labels.** They aren't
  memory-map entries (no `description=` metadata) and aren't in ROM range,
  so the resolver emits a build warning. Use plain inline-code (`` `nvwrch` ``)
  with the bare hex if needed (`` `&FFCB` ``). Confirmed via site rebuild —
  `address:FFCB` produced "no memory-map entry and not in ROM range".

## Known pre-existing issues (out of scope)

- 3.34B's inline comments at &003A/&003D/&003F say "R1" but the code reads
  Tube R4 (this variant wired WRCH to R4). The subroutine description at
  &0016 is correct ("polls R4"). Logged as task #11.
- 3.34 / 3.34B `comments check --strict` HIGH finding: `Y=&85 but LDY #&84`
  at &83F6 / &83F7. Pre-existing on master.
