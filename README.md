# Acorn NFS

[![Verify disassembly](https://github.com/acornaeology/acorn-nfs/actions/workflows/verify.yml/badge.svg)](https://github.com/acornaeology/acorn-nfs/actions/workflows/verify.yml)

Network Filing System for the BBC Micro Econet interface.

This repository contains annotated disassemblies of the Acorn NFS ROM, produced by reverse-engineering the original 6502 machine code. Each disassembly includes named labels, comments explaining the logic, and cross-references between subroutines.

## Versions

### Acorn NFS 3.34

- [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.34.html)
- [Raw assembly source](versions/3.34/output/nfs-3.34.asm)
- [Acorn NFS 3.34 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=d6761cb566cd87b0c1117b5b600cff16)

## How it works

The disassembly is produced by a Python script that drives a custom version of [py8dis](https://github.com/acornaeology/py8dis), a programmable disassembler for 6502 binaries. The script feeds the original ROM image to py8dis along with annotations — entry points, labels, constants, and comments — to produce readable assembly output.

The output is verified by reassembling with [beebasm](https://github.com/stardot/beebasm) and comparing the result byte-for-byte against the original ROM. This round-trip verification runs automatically in CI on every push.

## Building locally

Requires [uv](https://docs.astral.sh/uv/) and [beebasm](https://github.com/stardot/beebasm).

```sh
uv sync
uv run acorn-nfs disassemble 3.34
uv run acorn-nfs verify 3.34
```

## References

- [Acorn DNFS 3.00 source code](https://github.com/stardot/AcornDNFSv300)
  This is a different version of NFS, but its comments and labels provided important guidance in the disassembly and annotation process.

## Credits

- [py8dis](https://github.com/acornaeology/py8dis) by [SteveF](https://github.com/ZornsLemma), forked for use with acornaeology
- [beebasm](https://github.com/stardot/beebasm) by Rich Mayfield and contributors
- [The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/) by tobylobster

## License

The annotations and disassembly scripts in this repository are released under the [MIT License](LICENSE). The original ROM images remain the property of their respective copyright holders.
