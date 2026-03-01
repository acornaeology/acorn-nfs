# Changes from NFS 3.60 to NFS 3.62

NFS 3.62 is a minimal bug-fix release of Acorn NFS 3.60 for the BBC Micro.
The two 8 KB ROMs are 99.7% identical at the opcode level, with only 16 bytes
differing. The single functional change fixes a command-matching bug where
`*EXEC` was incorrectly caught by the `*EX` entry in the command table.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 8192 bytes   |
| Identical bytes at same offset  | 8176 (99.8%) |
| Byte-level similarity           | 99.8%        |
| Opcode-level similarity         | 99.7%        |
| Full instruction similarity     | 99.7%        |
| Instructions (3.60 / 3.62)     | 4073 / 4067  |
| Structural change blocks        | 4            |

## ROM header

| Field             | 3.60      | 3.62      |
|-------------------|-----------|-----------|
| Title             | "    NET" | "    NET" |
| ROM type          | &82       | &82       |
| Binary version    | &83       | &83       |
| Copyright         | "(C)ROFF" | "(C)ROFF" |
| Language entry    | &80E1     | &80E1     |
| Service entry     | &80F7     | &80F7     |

All header fields are functionally unchanged. The language and service entry
points remain at &80E1 and &80F7.

## Changes

### 1. Version identification

The ROM header version byte at &8023 changes from &60 to &62, and the version
string at &820B changes from `"NFS 3.60"` to `"NFS 3.62"`.

### 2. *EX vs *EXEC disambiguation (bug fix)

In NFS 3.60, the `*EX` entry in the FS command match table at &8C4B dispatches
directly to `ex_handler` at &8C61. This means any command beginning with "EX"
— including `*EXEC` — is matched as `*EX` and handled locally as a directory
listing rather than being forwarded to the fileserver.

NFS 3.62 fixes this by changing the `*EX` dispatch address in the command table
from &8C61 to &9FB5, where a new 12-byte trampoline routine checks whether the
command continues past "EX":

| Address | Instruction         | Purpose                              |
|---------|---------------------|--------------------------------------|
| &9FB5   | `LDA (fs_crc_lo),Y` | Load next character from command     |
| &9FB7   | `CMP #&21`          | Printable non-space character?       |
| &9FB9   | `BCS &9FBE`         | Yes: command continues, forward to FS|
| &9FBB   | `JMP ex_handler`    | No: terminated, handle *EX locally   |
| &9FBE   | `JMP forward_star_cmd` | Forward *EXEC etc. to fileserver  |

If the character after "EX" is below &21 (space, CR, or control character),
the command is `*EX` and control passes to `ex_handler` at &8C61 as before.
If the character is &21 or above (a printable character), the command is
something like `*EXEC` and is forwarded to the fileserver via
`forward_star_cmd` at &80C1.

The trampoline occupies 12 bytes of the &FF padding at the end of the ROM
(&9FB5-&9FC0), reducing the unused space from 75 bytes to 63 bytes.

The two byte changes in the command table data are:

| Address | 3.60 | 3.62 | Meaning                              |
|---------|------|------|--------------------------------------|
| &8C57   | &8C  | &9F  | Dispatch address high byte           |
| &8C58   | &60  | &B4  | Dispatch address low byte            |

These encode the PHA/PHA/RTS dispatch target as (address-1): &8C60 → &8C61
in 3.60, &9FB4 → &9FB5 in 3.62.

## Relocated code blocks

All four relocated code blocks are byte-identical between 3.60 and 3.62,
at the same ROM source addresses:

| Block     | ROM source | Runtime dest | Length  |
|-----------|------------|--------------|---------|
| Workspace | &9321      | &0016        | &61     |
| Page 4    | &9362      | &0400        | &100    |
| Page 5    | &9462      | &0500        | &100    |
| Page 6    | &9562      | &0600        | &100    |
