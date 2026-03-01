# Acorn NFS and Acorn ANFS

[![Verify disassembly](https://github.com/acornaeology/acorn-nfs/actions/workflows/verify.yml/badge.svg)](https://github.com/acornaeology/acorn-nfs/actions/workflows/verify.yml)

Network Filing System and Advanced Network Filing System for the BBC Micro Econet interface.

This repository contains annotated disassemblies of the Acorn NFS ROM, produced by reverse-engineering the original 6502 machine code. Each disassembly includes named labels, comments explaining the logic, and cross-references between subroutines.

## Versions

- **Acorn NFS 3.34**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.34.html)
  - [Raw assembly source](versions/nfs-3.34/output/nfs-3.34.asm)
  - [Acorn NFS 3.34 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=d6761cb566cd87b0c1117b5b600cff16)
- **Acorn NFS 3.34B**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.34B.html)
  - [Raw assembly source](versions/nfs-3.34B/output/nfs-3.34B.asm)
  - [Acorn NFS 3.34B in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=f1ce449900053d6d28c743904fc0efb1)
  - [Changes from NFS 3.34](versions/nfs-3.34B/CHANGES-FROM-3.34.md)
- **Acorn NFS 3.35D**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.35D.html)
  - [Raw assembly source](versions/nfs-3.35D/output/nfs-3.35D.asm)
  - [Acorn NFS 3.35D in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=3a25c88f6cc81052a4593ca7636105d1)
  - [Changes from NFS 3.34B](versions/nfs-3.35D/CHANGES-FROM-3.34B.md)
- **Acorn NFS 3.35K**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.35K.html)
  - [Raw assembly source](versions/nfs-3.35K/output/nfs-3.35K.asm)
  - [Acorn NFS 3.35K in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=03b6f0a92809fc0f30854a667cdfc2b0)
  - [Changes from NFS 3.35D](versions/nfs-3.35K/CHANGES-FROM-3.35D.md)
- **Acorn NFS 3.40**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.40.html)
  - [Raw assembly source](versions/nfs-3.40/output/nfs-3.40.asm)
  - [Acorn NFS 3.40 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=e08a5f08c5b3cd910d57581c81cb6c34)
  - [Changes from NFS 3.35K](versions/nfs-3.40/CHANGES-FROM-3.35K.md)
- **Acorn NFS 3.60**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.60.html)
  - [Raw assembly source](versions/nfs-3.60/output/nfs-3.60.asm)
  - [Acorn NFS 3.60 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=e345ac2f6f2130ad7683413071069609)
  - [Changes from NFS 3.40](versions/nfs-3.60/CHANGES-FROM-3.40.md)
- **Acorn NFS 3.62**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.62.html)
  - [Raw assembly source](versions/nfs-3.62/output/nfs-3.62.asm)
  - [Acorn NFS 3.62 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=2753db3479e60e64b8c2eb80a48392f5)
  - [Changes from NFS 3.60](versions/nfs-3.62/CHANGES-FROM-3.60.md)
- **Acorn NFS 3.65**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/3.65.html)
  - [Raw assembly source](versions/nfs-3.65/output/nfs-3.65.asm)
  - [Acorn NFS 3.65 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=1e150e6bd53d22c15eb05302b6e5f167)
  - [Changes from NFS 3.62](versions/nfs-3.65/CHANGES-FROM-3.62.md)
- **Acorn ANFS 4.08.53**
  - [Formatted disassembly on acornaeology.uk](https://acornaeology.uk/acorn-nfs/4.08.53.html)
  - [Raw assembly source](versions/anfs-4.08.53/output/anfs-4.08.53.asm)
  - [Acorn ANFS 4.08.53 in The BBC Micro ROM Library](https://tobylobster.github.io/rom_library/?md5=eadb37a9abbdbb70543efc2bede440bd)

## How it works

The disassembly is produced by a Python script that drives a custom version of [py8dis](https://github.com/acornaeology/py8dis), a programmable disassembler for 6502 binaries. The script feeds the original ROM image to py8dis along with annotations — entry points, labels, constants, and comments — to produce readable assembly output.

The output is verified by reassembling with [beebasm](https://github.com/stardot/beebasm) and comparing the result byte-for-byte against the original ROM. This round-trip verification runs automatically in CI on every push.

## Building locally

Requires [uv](https://docs.astral.sh/uv/) and [beebasm](https://github.com/stardot/beebasm).

```sh
uv sync
uv run acorn-nfs-disasm-tool disassemble 3.34
uv run acorn-nfs-disasm-tool verify 3.34
uv run acorn-nfs-disasm-tool disassemble 3.34B
uv run acorn-nfs-disasm-tool verify 3.34B
uv run acorn-nfs-disasm-tool disassemble 3.35D
uv run acorn-nfs-disasm-tool verify 3.35D
uv run acorn-nfs-disasm-tool disassemble 3.35K
uv run acorn-nfs-disasm-tool verify 3.35K
uv run acorn-nfs-disasm-tool disassemble 3.40
uv run acorn-nfs-disasm-tool verify 3.40
uv run acorn-nfs-disasm-tool disassemble 3.60
uv run acorn-nfs-disasm-tool verify 3.60
uv run acorn-nfs-disasm-tool disassemble 3.62
uv run acorn-nfs-disasm-tool verify 3.62
uv run acorn-nfs-disasm-tool disassemble 3.65
uv run acorn-nfs-disasm-tool verify 3.65
uv run acorn-nfs-disasm-tool disassemble 4.08.53
uv run acorn-nfs-disasm-tool verify 4.08.53
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
