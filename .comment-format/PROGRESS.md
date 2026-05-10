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
| Net protocol          | &9300–&9FFF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

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

## MEDIUM-finding pass

`fantasm comments check` (without `--strict`) reports MEDIUM-confidence
findings whenever a comment / description text contains a bare `&XXXX`
that doesn't resolve to a labeled item. Reviewed each one across all 8
versions and split into:

**Genuine bugs uncovered + fixed:**

- `tube_osword` buffer address: 3.35D / 3.35K page-6 banner table said
  *buffer at `&0130`* but those versions actually use `&0128` (the
  3.34/B versions use `&0130`). My own page-5/6 sweep had copied the
  wrong value across.
- `tube_osword` inline at &0692 in 3.34 / 3.34B: said *Send result
  block bytes from `&0128`* but the instruction is `LDY l0130,X`.
  Should be `&0130`.
- `econet_tx_rx` description: 3.34 / 3.34B / 3.35K / 3.40 said *NMI
  workspace `&0DDA`* — but `nmi_sub_table` is at `&0DE6` in every
  version (the actual `LDA nmi_sub_table,Y` source confirms this).
  3.35D had previously been corrected; 3.60 / 3.62 / 3.65 had the
  right address. Fixed all four to `nmi_sub_table` link.
- `svc_4_star_command` description in 3.40 referenced `&8014` and
  `&800D` for the `*ROFF` and `*NET` matchers. Both are real labels
  (`cmd_roff_str`, `cmd_net_str`) — linkified. Also linkified the
  fall-through targets (`net_4_resume_remote`, `svc_13_select_nfs`).
- `boot_cmd_strings` description in 3.40 became a 4-row table with
  one row per boot option (Off / Load / Run / Exec).

**Cosmetic linkifications (silence false positives, improve readability):**

- `init_tx_ctrl_block` description: linkified `&0E00`/`&0E01`
  (`fs_server_stn` / `fs_server_net`) and the `&00C2/&00C3`
  destination (`txcb_dest`).
- `save_fscv_args_with_ptrs` description: replaced
  `os_text_ptr/&F3` and `fs_cmd_ptr/&0E11` with single-label links
  to the 16-bit pointers.
- `tx_ctrl_template` description: linkified `&0F00` (`fs_cmd_type`)
  in the `&0F00`–`&0FFF` buffer-page reference.
- `rx_imm_machine_type` (3.40): rephrased the buffer setup so the
  `&7F25` literal becomes `&25` + `&7F` (offset and page) rather
  than a stale "address" reference.

**Genuine false positives left alone:**

- MOS extended-vector dispatch addresses `&FF1B`–`&FF2D` (mentioned
  by `init_fs_vectors` and `fs_vector_addrs`) — these are MOS-side
  and have no labels in our project.
- High-byte halves of split-byte writes (`&0221` = `EVNTV+1`,
  `&0203` = `BRKV+1`) — the inline comments correctly say which byte
  is being written; no separate label exists.
- Sentinel values like `&FFFF` (used for "any station", "unlimited
  length") — these are byte-pair values, not addresses.
- `&0D00` (NMI shim runtime base) — `nmi_code_base` label is at
  `&0CFF` for unrelated reasons; the shim genuinely starts at `&0D00`
  with no separate label there. Refactoring the label was out of
  scope.
- `&01FC` (length value passed as immediate operand). `&XXXX` is the
  project's chosen hex notation per `CLAUDE.md`.

Final tally: MEDIUM findings reduced from
17/18/19/20/24/22/22/22 → 15/16/17/17/19/20/20/20 across the 8 NFS
versions (down ~25 findings total, ~12% reduction). The remaining
~150 findings are accepted false positives (legitimate references
to non-labeled addresses or non-address values in `&XXXX` notation).

## Drive-by correctness fixes (now resolved)

- **3.34B Tube WRCH register comments** — inline comments at &003D
  (`R1 not ready: check R2 instead`), &0048 (`loop back to R1 check`)
  and &004D (`R1 ready: handle WRCH first`) all said "R1" but 3.34B
  wires WRCH to R4 (the BIT at &003A and LDA at &003F target
  `tube_status_register_4_and_cpu_control` and `tube_data_register_4`).
  The subroutine description at &0016 was already correct ("polls R4").
  Fixed: replaced "R1" → "R4" in those three inline comments.
- **3.34 / 3.34B SPOOL-close comments** — inline comments at &83F6
  (3.34) / &83F7 (3.34B) said `Y=&85` but the instruction is
  `LDY #&84`. The string lives at &8444 / &8445 (`sp_dot_string`),
  not &85xx. Comment value was carried from the modern 3.65 version
  where the string IS at &85xx. Also: the next-instruction comment
  said `Close SPOOL/EXEC via "*SP." or "*E."` but 3.34 / 3.34B only
  have a SPOOL-close path (no EXEC handle is read or compared);
  the dual-path code only appears from 3.35D onwards. Fixed: comment
  now says `Y=&84: high byte of sp_dot_string` and
  `Close SPOOL via *SP.`. The 3.65 / 3.62 / 3.60 / 3.40 / 3.35K /
  3.35D versions are unchanged — their `Y=&85` comments correctly
  describe their `LDY #&85` instructions.

## Final state (all 8 sections complete)

| Check                          | Result |
|--------------------------------|--------|
| `fantasm verify` × 8 versions  | all PASSED (8192-byte byte-identical match) |
| `fantasm lint` × 8 versions    | all clean (no broken refs) |
| `fantasm comments check --strict` | only the 2 pre-existing HIGH findings on 3.34/3.34B remain |
| Site rebuild                   | zero warnings |

`address:HEX` link counts per driver (started at 1–3 per version):

| Version | Links | Inline-comment density |
|---------|-------|------------------------|
| 3.34    | 60    | 97.2% |
| 3.34B   | 58    | 97.1% |
| 3.35D   | 60    | 97.4% |
| 3.35K   | 60    | 97.4% |
| 3.40    | 65    | 97.6% |
| 3.60    | 72    | 97.6% |
| 3.62    | 72    | 97.6% |
| 3.65    | 95    | 97.6% |

## What was deliberately NOT done

- Full linkification of every bare `&XXXX` in inline comments. The sweep
  prioritised descriptions (`title=`, `description=` kwargs of
  `subroutine()`/`label()`) and the most impactful inline references.
  Around 330–380 bare-hex occurrences remain per driver — most are
  immediate values, byte literals (`&80`, `&FF`), or addresses for
  which adding a link would be lower-value churn.
- Per-handler `tube_X` polish in 3.34 / 3.34B / 3.35D / 3.35K. Those
  versions don't carry separate `subroutine()` declarations for handlers
  like `tube_osbput`, only labels. The page-5 / page-6 banners were
  upgraded; per-handler descriptions only exist (and were upgraded)
  from 3.40 onwards.
- `econet_tx_rx` rewrite for older versions (description references
  &8383 which is 3.65-specific).
- Older-version (3.34/B/D/K) `argsv_handler` and `findv_handler`
  rewrites — those versions used different FS commands (&0A/&14 vs
  &0C/&0D) so the per-row content needs different protocol details
  rather than just an address-shift sed.
