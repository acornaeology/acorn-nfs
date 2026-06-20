# Deferring the Remote Subroutine Jump

Econet lets one machine reach into another. Among its *immediate
operations* — transfers sent to port 0 that act on the remote machine
directly, without going through a filing system — is the **Remote
Subroutine Jump** (RSJ), control byte `&83`: a remote station asks the
local machine to `JSR` to an address of the caller's choosing and sends
the reply when that routine returns. Its siblings `&84` (user procedure
call) and `&85` (OS procedure call), and the flow-control pair `&86`
HALT / `&87` CONTINUE, all share the same need — they have to run code on
the receiving machine.

That creates a problem, because the frame that carries the request
arrives **inside the NMI handler**. Econet reception is NMI-driven: the
ADLC raises /NMI for every received byte, and the receive handler runs
at the highest priority in the machine, with interrupts disabled and the
single hardware NMI "in flight." You cannot `JSR` into arbitrary user
code from there. The user routine might enable interrupts, might itself
use Econet, might take milliseconds — and the whole time another network
byte could be arriving with nowhere to be serviced. The NMI handler must
get in and out in microseconds.

So NFS does not make the call from the NMI handler. It **defers** it:
the handler records *what* needs doing and arranges for an ordinary IRQ
to fire a moment later, once the NMI has returned and the machine is back
in a state where a normal interrupt — and the code it runs — is safe.
The deferred call is then made from IRQ context, through the ROM's
service-call `&05` (unrecognised interrupt) entry.

How that "fire an IRQ a moment later" is arranged is the interesting
part, and it is **not the same** on the two machines NFS/ANFS run on.
The BBC Model B has no spare timer interrupt lying idle, so NFS presses
the **system VIA shift register** into service as a one-shot delayed
interrupt. The Master 128 has a register bit whose entire job is to
assert an IRQ on demand, so ANFS on the Master simply **sets that bit**.
The Model B technique is shared by every Model B ROM in this project —
NFS 3.34 through 3.65 and ANFS 4.08.53 / 4.18 — while the Master
technique appears only in the Master ROM, ANFS 4.21. The two parts below
use the two ANFS versions as concrete examples.

The shape of the deferral is identical in both:

```
   NMI receive handler                 (later) IRQ / service call &05
   -------------------                 -----------------------------
   immediate_op:  ctrl = &83?          svc5_irq_check:
   yes, execute-class ->                 was it our deferred IRQ?
     record op type in tx_op_type        yes -> dispatch on tx_op_type
     arm a delayed IRQ  --------~~~------>  tx_done_jsr:
     return from NMI                          JMP (exec_addr)   <- the RSJ
```

`&81` PEEK, `&82` POKE and `&88` machine-type are **not** deferred. They
only read or write memory and post an immediate reply, which is safe in
the receive path, so they run there and never arm the delayed IRQ. Only
the execute-class operations `&83`–`&87` take the slow road.

A station can also *refuse* remote calls. Each holds a protection mask
(at `&0D61`) saying which immediate operations it will accept; the
`immediate_op` handler tests the incoming control byte against it and
silently discards an operation the user has disabled. This is the
"protection against Remote Subroutine Jump" a careful operator would
switch on — a remote machine can only `JSR` into yours if you have left
the door open.

## Part 1 — Model B: the VIA shift register as a one-shot timer

Concrete example: **ANFS 4.08.53**. (NFS 3.34–3.65 and ANFS 4.18 do the
same thing at their own addresses.)

The 6522 VIA's shift register, in one of its modes, will clock eight bits
in or out under control of the φ2 system clock and then raise an
interrupt — IFR bit 2, "SR complete". NFS does not care about the bits.
It cares only that **a fixed, short interval after you start it, the
shift register raises an IRQ by itself.** That is exactly a one-shot
timer, and it is free: nothing else in the machine is using the shift
register.

`setup_sr_tx` (`&8505`) arms it. The NMI handler has already decided this
is a deferred operation and reaches here with the operation type in `A`:

```
.setup_sr_tx
    sta tx_op_type        ; &8505  remember WHAT to do, for the IRQ side
    lda #&84              ; &8508  IER: clear bit 2 ...
    sta system_via_ier    ; &850A  ... disable the SR interrupt while we set up
    lda system_via_acr    ; &850D  read the auxiliary control register
    and #&1c              ; &8510  isolate the current shift-register mode bits
    sta ws_0d64           ; &8512  save them, to restore on the IRQ side
    lda system_via_acr    ; &8515  read ACR again
    and #&e3              ; &8518  clear the SR mode bits
    ora #8                ; &851A  set SR mode 2: shift IN under φ2
    sta system_via_acr    ; &851C  apply -> the shift register starts free-running
    bit system_via_sr     ; &851F  touch SR to clear any stale flag and start it
```

From the `STA system_via_acr` at `&851C`, the shift register is
free-running under φ2. Eight shifts later it sets IFR bit 2, and because
that is a system-VIA interrupt source it pulls the CPU's IRQ line. By
then the NMI handler has long since returned and the machine is taking
ordinary interrupts again, so the IRQ is delivered through the normal
path. The MOS offers it round the sideways ROMs as **service call `&05`,
"unrecognised interrupt,"** and NFS catches it:

```
.svc5_irq_check
    lda #4                ; &8023  mask for IFR bit 2 (SR complete)
    bit system_via_ifr    ; &8025  is the SR-complete flag set?
    bne save_registers    ; &8028  yes -> this IRQ is ours, handle it
    lda #5                ; &802A  no -> not ours
    rts                   ; &802C  return A=5 so MOS keeps offering it round
.save_registers
    ...                   ; restore the saved SR mode from ws_0d64,
    ...                   ; clear IFR bit 2 and re-disable the SR interrupt
    ldy tx_op_type        ; &8047  recover WHAT we deferred
    ...                   ; dispatch through tx_done_dispatch_lo
```

The dispatch lands on a small handler per operation type. For the RSJ
(`&83`) it is `tx_done_jsr`, and this is where, at last, the remote
caller's subroutine is entered — safely, in IRQ context:

```
.tx_done_jsr
    lda #&85              ; &8539  push the high byte of (tx_done_exit - 1)
    pha                   ; &853B
    lda #&7a              ; &853C  push the low byte
    pha                   ; &853E
    jmp (exec_addr_lo)    ; &853F  JMP (&0D66) -- THE Remote Subroutine Jump
```

The two `PHA`s plant a return address on the stack so that when the
remote routine finishes with `RTS`, control falls into `tx_done_exit` and
NFS can post the reply. The `JMP (&0D66)` is the call itself: `&0D66`
holds the address the remote station asked for, copied out of the request
frame.

That is the whole trick on the Model B. An interrupt source no one needs
for its nominal purpose is repurposed as an egg-timer: start it in the
NMI handler, ignore the data it shifts, and collect the interrupt it
raises a few microseconds later in a context where running code is safe.

## Part 2 — Master 128: a register bit that *is* a software IRQ

Concrete example: **ANFS 4.21** (variant 1), the first Master 128 ANFS.

The Master does not need the egg-timer, because it has something better:
ACCCON bit 7. ACCCON (`&FE34`) is the Master's access-control register —
mostly it pages the shadow and HAZEL RAM in and out — but its top bit,
**IRR (Interrupt Request)**, is a software interrupt line. Setting it
pulls the CPU's /IRQ pin low directly; the interrupt is held off only by
the 6502's I flag. (See the references: this is not, as one might guess
from the name, a VSYNC-related mask — writing 1 simply asserts IRQ.)

So the deferral collapses to two instructions in the arming routine and
one in the handler. `setup_sr_tx` (`&8512`) — the routine keeps the Model
B name — reaches here from the NMI handler with the operation type in
`A`:

```
.setup_sr_tx
    sta tx_op_type        ; &8512  remember WHAT to do
    cmp #&86              ; &8515  HALT/CONTINUE/machine-type (>= &86)?
    bcs enable_irq_pending; &8517  ... if so, skip the ACR fiddling
    lda ws_0d68           ; &8519  (execute-class only) read workspace ACR byte
    sta ws_0d69           ; &851C  save a copy
    ora #&1c              ; &851F  set shift-register mode-2 bits ...
    sta ws_0d68           ; &8521  ... back into WORKSPACE (see below)
.enable_irq_pending
    lda #&80              ; &8524  ACCCON bit 7 (IRR)
    tsb acccon            ; &8526  set it -> assert a software IRQ
```

The `TSB acccon` at `&8526` is the entire mechanism: it sets IRR, the
/IRQ line goes low, and as soon as the NMI handler returns and interrupts
are enabled the IRQ is taken. As before it arrives as service call `&05`:

```
.svc5_irq_check
    phx                   ; &8028
    phy                   ; &8029
    ldy tx_op_type        ; &802A  anything deferred?
    bne irq_check_dispatch; &802D  yes -> handle it
    ply
    plx
    rts                   ; &8031  no -> not ours, pass the service call on
.irq_check_dispatch
    lda #&80              ; &8032  ACCCON bit 7 (IRR)
    trb acccon            ; &8034  CLEAR it -> drop the software IRQ
    stz tx_op_type        ; &8037  we are handling it now
    ...                   ; dispatch exactly as on the Model B
```

The two halves mirror each other through one bit: the NMI side `TSB`s
IRR to raise the interrupt, the IRQ side `TRB`s it to lower it again,
and the work in between — recover `tx_op_type`, dispatch to
`tx_done_jsr`, `JMP (exec_addr)` — is the same on both machines. Note the
trigger is no longer self-timing: on the Master the IRQ is *pending the
instant* `TSB` runs and fires the moment the I flag allows, rather than
after a fixed shift interval.

### A fossil of the Model B mechanism

Look again at `&8519`–`&8521` above. For an execute-class operation the
Master code still computes a **shift-register mode-2 control byte** —
`ORA #&1C` is the same bit pattern the Model B writes to the VIA's
ACR — and stores it. But it stores it into a *workspace* byte (`&0D68`),
and **nothing in the 4.21 ROM ever flushes that byte to the live VIA.**
The shift register is never armed; the computed value is dead.

It is a fossil. ANFS for the Master was derived from the Model B code
base, and when the deferral was rewritten to use ACCCON IRR, the old
shift-register-mode bookkeeping was left in place — harmlessly writing a
value that is now never used. It is a small, concrete sign of the
lineage between the two implementations, visible only in the
disassembly: the Master ROM still remembers how the BBC did it.

## Why this is worth recording

The deferral is easy to miss because nothing in the code announces it.
On the Model B you see the shift register being configured and assume it
is shifting data; on the Master you see a bit being set in the
memory-paging register and assume it is paging memory. In both cases the
real purpose is the same and is invisible without knowing the intent:
move a piece of work from the forbidden NMI context into a safe IRQ a
few microseconds later. It is a neat illustration of a recurring 8-bit
idiom — *if you cannot do the work here, arrange for an interrupt to ask
you again somewhere safer* — and of how the same idea is expressed
through whatever hardware the target machine happens to offer.

## References

- Model B path (ANFS 4.08.53):
  `versions/anfs-4.08.53/disassemble/disasm_anfs_40853.py` —
  `immediate_op` (`&844B`), `imm_op_build_reply` / `setup_sr_tx`
  (`&84EC` / `&8505`), `svc5_irq_check` (`&8023`), `tx_done_jsr`
  (`&8539`). NFS 3.34–3.65 and ANFS 4.18 use the same mechanism at their
  own addresses.
- Master path (ANFS 4.21 variant 1):
  `versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py`
  — `setup_sr_tx` (`&8512`), `svc5_irq_check` (`&8028`), and the `acccon`
  register definition at `&FE34`.
- Econet immediate operations and the RSJ are defined in the *Econet
  Advanced User Guide* (`docs/Acorn_EconetL23UG.pdf`); see also the
  GLOSSARY entries for *immediate operation* and *RSJ*.
- ACCCON bit 7 (IRR): *Master Series Hardware Specification* and the
  *Advanced Reference Manual for the BBC Master* describe IRR as an
  interrupt-request bit that, when set, asserts the CPU /IRQ line via an
  open-drain output.
