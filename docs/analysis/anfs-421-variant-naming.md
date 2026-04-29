# Why is ANFS 4.21 named "variant 1"?

The ROM is shipped under the name "anfs-4.21_variant_1.rom" but its
internal title is just "Acorn ANFS 4.21". The variant suffix is not in
the ROM header. This note records what the disassembly tells us about
*why* multiple 4.21 builds appear to have existed.

## Evidence: the host-OS gate

In `service_handler` at &8A54, on a Service 15 ("vectors claimed") call
the ROM reads the host OS version via OSBYTE 0 and tests:

```
&8A61  CPX #3            ; OS 3.2/3.5 — Master 128
&8A63  BEQ restore_rom_slot
&8A65  CPX #4            ; OS 4.0   — Master Econet Terminal
&8A67  BEQ restore_rom_slot
&8A69  TXA               ; otherwise: print "Bad ROM <slot>" and
&8A6A  PHP               ; clear the slot's workspace byte at &02A0
       ...
```

The OSBYTE 0 result conventions are:

| X | Host OS                      | Outcome |
|---|------------------------------|---------|
| 0 | OS 1.00 (early BBC B / Electron) | rejected |
| 1 | OS 1.20 / American OS         | rejected |
| 2 | OS 2.00 (BBC B+)              | rejected |
| 3 | OS 3.2 / 3.5 (Master 128)     | accepted |
| 4 | OS 4.0 (Master Econet Terminal) | accepted |
| 5 | OS 5.0 (Master Compact)       | rejected |

So this ROM was built for the original Master 128 and the rack-mounted
Master Econet Terminal but explicitly rejects every other model in the
range, including the Master Compact.

The 4.18 equivalent at &8A23 only tested `CPX #1` and `CPX #2`, gating
*workspace skip* (not a hard rejection) for the BBC B+ and OS 1.20. The
4.21 code is a stronger gate and a different acceptance set.

## Hypothesis

"variant 1" is most likely the original Master 128 / Master ET build of
ANFS 4.21. The natural counterpart "variant 2" would be the Master
Compact build that accepts X=5 (and would presumably reject X=3/4 in
the same manner). The version *number* (4.21) probably stays the same
across variants because the source release is shared; what differs is
the per-machine compile-time gate.

This is an observation derived from one ROM only. Confirming it
requires comparing against another 4.21 ROM with a different MD5 and
matching internal title.

## What would falsify this

* A second ANFS 4.21 ROM with a different MD5 that targets OS 5.0
  (X=5) at the same code site would confirm the variant-per-machine
  hypothesis.
* A second ROM that targets the *same* OS set as this one would mean
  the variants differ on something other than the host-OS gate (e.g.
  bug fixes, language differences, Tube-protocol changes).
* If no other 4.21 ROM ever turns up, the "_variant_1" suffix may
  simply be a curatorial tag from the BBC Micro ROM Library that
  doesn't correspond to a sibling release at all.

## References

* Disassembly: `versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py`,
  `service_handler` at &8A54.
* OSBYTE 0 documentation: see e.g. the Master 128 Reference Manual,
  Part 2 (the OSBYTE call table), or the in-repo
  `docs/Acorn_EconetL23UG.pdf` which uses the same convention.
* The 4.18 baseline that this routine evolved from is in
  `versions/anfs-4.18/disassemble/disasm_anfs_418.py`,
  `service_handler` at &8A15.
