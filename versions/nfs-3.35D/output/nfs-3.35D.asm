; Constants
adlc_cr1                                    = 65184
adlc_cr2                                    = 65185
adlc_tx                                     = 65186
adlc_tx2                                    = 65187
buffer_printer                              = 3
cb_fill                                     = 252
cb_skip                                     = 253
cb_stop                                     = 254
econet_nmi_enable                           = 65056
econet_station_id                           = 65048
err_fs_cutoff                               = 168
err_line_jammed                             = 160
err_net_error                               = 161
err_no_clock                                = 163
err_no_reply                                = 165
err_not_listening                           = 162
err_tx_cb_error                             = 164
event_network_error                         = 8
handle_base                                 = 32
osbyte_close_spool_exec                     = 119
osbyte_explode_chars                        = 20
osbyte_insert_input_buffer                  = 153
osbyte_issue_service_request                = 143
osbyte_printer_driver_going_dormant         = 123
osbyte_read_buffer                          = 145
osbyte_read_rom_ptr_table_low               = 168
osbyte_read_tube_presence                   = 234
osbyte_read_write_econet_keyboard_disable   = 201
osbyte_read_write_exec_file_handle          = 198
osbyte_read_write_last_break_type           = 253
osbyte_scan_keyboard_from_16                = 122
osbyte_write_keys_pressed                   = 120
osfind_close                                = 0
osword_read_palette                         = 11
port_command                                = 153
port_load_data                              = 146
port_printer                                = 209
port_remote                                 = 147
port_reply                                  = 144
port_save_ack                               = 145
rx_ready                                    = 127
tx_flag                                     = 128

; Memory locations
zp_ptr_lo                               = &0000
zp_ptr_hi                               = &0001
zp_work_2                               = &0002
zp_work_3                               = &0003
zp_temp_10                              = &0010
zp_temp_11                              = &0011
tube_data_ptr                           = &0012
tube_data_ptr_hi                        = &0013
tube_claim_flag                         = &0014
tube_claimed_id                         = &0015
zp_63                                   = &0063
escapable                               = &0097
need_release_tube                       = &0098
prot_flags                              = &0099
net_tx_ptr                              = &009a
net_tx_ptr_hi                           = &009b
net_rx_ptr                              = &009c
net_rx_ptr_hi                           = &009d
nfs_workspace                           = &009e
nfs_workspace_hi                        = &009f
nmi_tx_block                            = &00a0
nmi_tx_block_hi                         = &00a1
port_buf_len                            = &00a2
port_buf_len_hi                         = &00a3
open_port_buf                           = &00a4
open_port_buf_hi                        = &00a5
port_ws_offset                          = &00a6
rx_buf_offset                           = &00a7
nfs_temp                                = &00a8
rom_svc_num                             = &00a9
osword_flag                             = &00aa
ws_ptr_lo                               = &00ab
ws_ptr_hi                               = &00ac
table_idx                               = &00ad
work_ae                                 = &00ae
addr_work                               = &00af
fs_load_addr                            = &00b0
fs_load_addr_hi                         = &00b1
fs_load_addr_2                          = &00b2
fs_load_addr_3                          = &00b3
fs_work_4                               = &00b4
fs_work_5                               = &00b5
fs_work_7                               = &00b7
fs_error_ptr                            = &00b8
fs_crflag                               = &00b9
fs_spool_handle                         = &00ba
fs_options                              = &00bb
fs_block_offset                         = &00bc
fs_last_byte_flag                       = &00bd
fs_crc_lo                               = &00be
fs_crc_hi                               = &00bf
txcb_ctrl                               = &00c0
txcb_port                               = &00c1
txcb_dest                               = &00c2
txcb_start                              = &00c4
txcb_pos                                = &00c7
txcb_end                                = &00c8
fs_temp_cd                              = &00cd
fs_temp_ce                              = &00ce
fs_spool0                               = &00cf
osbyte_a_copy                           = &00ef
osword_pb_ptr                           = &00f0
osword_pb_ptr_hi                        = &00f1
os_text_ptr                             = &00f2
os_text_ptr_hi                          = &00f3
romsel_copy                             = &00f4
osrdsc_ptr                              = &00f6
osrdsc_ptr_hi                           = &00f7
brk_ptr                                 = &00fd
escape_flag                             = &00ff
l0100                                   = &0100
l0101                                   = &0101
l0102                                   = &0102
l0103                                   = &0103
l0104                                   = &0104
l0106                                   = &0106
l0128                                   = &0128
userv                                   = &0200
filev                                   = &0212
fscv                                    = &021e
netv                                    = &0224
l0350                                   = &0350
l0351                                   = &0351
l0355                                   = &0355
l0700                                   = &0700
l0cff                                   = &0cff
nmi_shim_07                             = &0d07
nmi_jmp_lo                              = &0d0c
nmi_jmp_hi                              = &0d0d
set_nmi_vector                          = &0d0e
install_nmi_handler                     = &0d11
nmi_rti                                 = &0d14
nmi_shim_1a                             = &0d1a
l0d1e                                   = &0d1e
tx_dst_stn                              = &0d20
tx_dst_net                              = &0d21
tx_src_stn                              = &0d22
tx_src_net                              = &0d23
tx_ctrl_byte                            = &0d24
tx_port                                 = &0d25
tx_data_start                           = &0d26
tx_data_len                             = &0d2a
rx_status_flags                         = &0d38
tx_ctrl_status                          = &0d3a
rx_ctrl_copy                            = &0d3b
rx_src_stn                              = &0d3d
rx_src_net                              = &0d3e
rx_ctrl                                 = &0d3f
rx_port                                 = &0d40
rx_remote_addr                          = &0d41
tx_flags                                = &0d4a
nmi_next_lo                             = &0d4b
nmi_next_hi                             = &0d4c
tx_index                                = &0d4f
tx_length                               = &0d50
tx_work_51                              = &0d51
tx_in_progress                          = &0d52
tx_work_57                              = &0d57
l0d58                                   = &0d58
l0d59                                   = &0d59
scout_status                            = &0d5c
rx_extra_byte                           = &0d5d
l0d60                                   = &0d60
printer_buf_ptr                         = &0d61
tx_clear_flag                           = &0d62
prot_status                             = &0d63
rx_flags                                = &0d64
saved_jsr_mask                          = &0d65
econet_init_flag                        = &0d66
tube_flag                               = &0d67
nmi_sub_table                           = &0de6
fs_state_deb                            = &0deb
rom_ws_table                            = &0df0
fs_context_base                         = &0dfe
fs_server_stn                           = &0e00
fs_server_net                           = &0e01
fs_urd_handle                           = &0e02
fs_csd_handle                           = &0e03
fs_lib_handle                           = &0e04
fs_boot_option                          = &0e05
fs_messages_flag                        = &0e06
fs_eof_flags                            = &0e07
fs_sequence_nos                         = &0e08
fs_last_error                           = &0e09
fs_cmd_context                          = &0e0a
fs_context_hi                           = &0e0b
fs_reply_status                         = &0e0d
fs_target_stn                           = &0e0e
fs_cmd_ptr                              = &0e10
l0e11                                   = &0e11
fs_work_16                              = &0e16
fs_filename_buf                         = &0e30
fs_reply_data                           = &0ef7
fs_cmd_type                             = &0f00
fs_cmd_y_param                          = &0f01
fs_cmd_urd                              = &0f02
fs_cmd_csd                              = &0f03
fs_cmd_lib                              = &0f04
fs_cmd_data                             = &0f05
fs_func_code                            = &0f06
fs_data_count                           = &0f07
fs_reply_cmd                            = &0f08
fs_load_vector                          = &0f09
fs_load_upper                           = &0f0b
fs_addr_check                           = &0f0c
fs_file_len                             = &0f0d
fs_file_attrs                           = &0f0e
fs_file_len_3                           = &0f10
fs_obj_type                             = &0f11
fs_access_level                         = &0f12
fs_reply_stn                            = &0f13
fs_len_clear                            = &0f14
fs_boot_data                            = &0f16
fs_putb_buf                             = &0fdc
fs_getb_buf                             = &0fdd
fs_handle_mask                          = &0fde
fs_error_flags                          = &0fdf
fs_error_buf                            = &0fe0
l18a5                                   = &18a5
l212e                                   = &212e
station_id_disable_net_nmis             = &fe18
video_ula_control                       = &fe20
romsel                                  = &fe30
system_via_sr                           = &fe4a
system_via_acr                          = &fe4b
system_via_ifr                          = &fe4d
system_via_ier                          = &fe4e
econet_control1_or_status1              = &fea0
econet_control23_or_status2             = &fea1
econet_data_continue_frame              = &fea2
econet_data_terminate_frame             = &fea3
tube_status_1_and_tube_control          = &fee0
tube_data_register_1                    = &fee1
tube_status_register_2                  = &fee2
tube_data_register_2                    = &fee3
tube_status_register_3                  = &fee4
tube_data_register_3                    = &fee5
tube_status_register_4_and_cpu_control  = &fee6
tube_data_register_4                    = &fee7
oseven                                  = &ffbf
gsinit                                  = &ffc2
gsread                                  = &ffc5
nvrdch                                  = &ffc8
nvwrch                                  = &ffcb
osfind                                  = &ffce
osgbpb                                  = &ffd1
osbput                                  = &ffd4
osbget                                  = &ffd7
osargs                                  = &ffda
osfile                                  = &ffdd
osrdch                                  = &ffe0
osasci                                  = &ffe3
osnewl                                  = &ffe7
oswrch                                  = &ffee
osword                                  = &fff1
osbyte                                  = &fff4
oscli                                   = &fff7

    org &931a

.reloc_zp_src

; Move 1: &931a to &16 for length 69
    org &16
; ***************************************************************************************
; Tube BRK handler (BRKV target) — reference: NFS11 NEWBR
; 
; Sends error information to the Tube co-processor via R2 and R4:
;   1. Sends &FF to R4 (WRIFOR) to signal error
;   2. Reads R2 data (flush any pending byte)
;   3. Sends &00 via R2, then error number from (&FD),0
;   4. Loops sending error string bytes via R2 until zero terminator
;   5. Falls through to tube_reset_stack → tube_main_loop
; The main loop continuously polls R1 for WRCH requests (forwarded
; to OSWRITCH &FFCB) and R2 for command bytes (dispatched via the
; 14-entry table at &0500). The R2 command byte is stored at &55
; before dispatch via JMP (&0500).
; ***************************************************************************************
; &931a referenced 1 time by &8147
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 931a: a9 ff       ..  :0016[1]   ; A=&FF: signal error to co-processor via R4
    jsr tube_send_r4                                                  ; 931c: 20 d6 06     .. :0018[1]   ; Send &FF error signal to Tube R4
    lda tube_data_register_2                                          ; 931f: ad e3 fe    ... :001b[1]   ; Flush any pending R2 byte
    lda #0                                                            ; 9322: a9 00       ..  :001e[1]   ; A=0: send zero prefix to R2
.tube_send_zero_r2
    jsr tube_send_r2                                                  ; 9324: 20 cd 06     .. :0020[1]   ; Send zero prefix byte via R2
    tay                                                               ; 9327: a8          .   :0023[1]   ; Y=0: start of error block at (&FD)
    lda (brk_ptr),y                                                   ; 9328: b1 fd       ..  :0024[1]   ; Load error number from (&FD),0
    jsr tube_send_r2                                                  ; 932a: 20 cd 06     .. :0026[1]   ; Send error number via R2
; &932d referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 932d: c8          .   :0029[1]   ; Advance to next error string byte
.tube_send_error_byte
    lda (brk_ptr),y                                                   ; 932e: b1 fd       ..  :002a[1]   ; Load next error string byte
    jsr tube_send_r2                                                  ; 9330: 20 cd 06     .. :002c[1]   ; Send error string byte via R2
    tax                                                               ; 9333: aa          .   :002f[1]   ; Zero byte = end of error string
    bne tube_brk_send_loop                                            ; 9334: d0 f7       ..  :0030[1]   ; Loop until zero terminator sent
.tube_reset_stack
    ldx #&ff                                                          ; 9336: a2 ff       ..  :0032[1]   ; Reset stack pointer to top
    txs                                                               ; 9338: 9a          .   :0034[1]   ; TXS: set stack pointer from X
    cli                                                               ; 9339: 58          X   :0035[1]   ; Enable interrupts for main loop
; ***************************************************************************************
; Save registers and enter Tube polling loop
; 
; Saves X and Y to zp_temp_11/zp_temp_10, then falls through
; to tube_main_loop which polls Tube R1 (WRCH) and R2 (command)
; registers in an infinite loop. Called from tube_init_reloc
; after ROM relocation and from tube_dispatch_table handlers
; that need to restart the main loop.
; ***************************************************************************************
; &933a referenced 2 times by &04ec[2], &053a[3]
.tube_enter_main_loop
    stx zp_temp_11                                                    ; 933a: 86 11       ..  :0036[1]   ; Save X to temporary
    sty zp_temp_10                                                    ; 933c: 84 10       ..  :0038[1]   ; Save Y to temporary
; &933e referenced 6 times by &0048[1], &05ae[3], &05d5[3], &0635[4], &069d[4], &06ca[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 933e: 2c e0 fe    ,.. :003a[1]   ; BIT R1 status: check WRCH request
    bpl tube_poll_r2                                                  ; 9341: 10 06       ..  :003d[1]   ; R1 not ready: check R2 instead
; &9343 referenced 1 time by &004d[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 9343: ad e1 fe    ... :003f[1]   ; Read character from Tube R1 data
    jsr nvwrch                                                        ; 9346: 20 cb ff     .. :0042[1]   ; Write character
; &9349 referenced 1 time by &003d[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9349: 2c e2 fe    ,.. :0045[1]   ; BIT R2 status: check command byte
    bpl tube_main_loop                                                ; 934c: 10 f0       ..  :0048[1]   ; R2 not ready: loop back to R1 check
    bit tube_status_1_and_tube_control                                ; 934e: 2c e0 fe    ,.. :004a[1]   ; Re-check R1: WRCH has priority over R2
    bmi tube_handle_wrch                                              ; 9351: 30 f0       0.  :004d[1]   ; R1 ready: handle WRCH first
    ldx tube_data_register_2                                          ; 9353: ae e3 fe    ... :004f[1]   ; Read command byte from Tube R2 data
    stx tube_dispatch_ptr_lo                                          ; 9356: 86 55       .U  :0052[1]   ; Self-modify JMP low byte for dispatch
.tube_dispatch_cmd
tube_dispatch_ptr_lo = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 9358: 6c 00 05    l.. :0054[1]   ; Dispatch to handler via indirect JMP

; &9359 referenced 1 time by &0052[1]
; &935b referenced 2 times by &0478[2], &0493[2]
.tube_transfer_addr
    equb 0                                                            ; 935b: 00          .   :0057[1]
; &935c referenced 2 times by &047c[2], &0498[2]
.tube_xfer_page
    equb &80                                                          ; 935c: 80          .   :0058[1]
; &935d referenced 1 time by &04a2[2]
.tube_xfer_addr_2
    equb 0                                                            ; 935d: 00          .   :0059[1]
; &935e referenced 1 time by &04a0[2]
.tube_xfer_addr_3
    equb 0                                                            ; 935e: 00          .   :005a[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, reloc_zp_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &005b

    ; Set the program counter to the next position in the binary file.
    org reloc_zp_src + (* - nmi_workspace_start)

.reloc_p4_src

; Move 2: &935f to &0400 for length 256
    org &0400
; ***************************************************************************************
; Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)
; 
; Copied from ROM at &934D during init. The first 28 bytes (&0400-&041B)
; overlap with the end of the ZP block (the same ROM bytes serve both
; the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
;   &0400: JMP &0473 (BEGIN — CLI parser / startup entry)
;   &0403: JMP &06E2 (tube_escape_check)
;   &0406: tube_addr_claim — Tube address claim protocol (ADRR)
;   &0414: tube_post_init — called after ROM→RAM copy
;   &0473: BEGIN — startup/CLI entry, break type check
;   &04E7: tube_rdch_handler — RDCHV target
;   &04EF: tube_restore_regs — restore X,Y, dispatch entry 6
;   &04F7: tube_read_r2 — poll R2 status, read data byte to A
; ***************************************************************************************
; &935f referenced 1 time by &812d
.tube_code_page4
    jmp tube_begin                                                    ; 935f: 4c 73 04    Ls. :0400[2]   ; JMP to BEGIN startup entry

.tube_escape_entry
    jmp tube_escape_check                                             ; 9362: 4c df 06    L.. :0403[2]   ; JMP to tube_escape_check (&06A7)

; &9365 referenced 10 times by &04bc[2], &04e4[2], &8b3f, &8b51, &8bae, &8e17, &9a01, &9a53, &9fa7, &9faf
.tube_addr_claim
    cmp #&80                                                          ; 9365: c9 80       ..  :0406[2]   ; A>=&80: address claim; A<&80: data transfer
    bcc setup_data_transfer                                           ; 9367: 90 1c       ..  :0408[2]   ; A<&80: data transfer setup (SENDW)
    cmp #&c0                                                          ; 9369: c9 c0       ..  :040a[2]   ; A>=&C0: new address claim from another host
    bcs addr_claim_external                                           ; 936b: b0 0b       ..  :040c[2]   ; C=1: external claim, check ownership
    ora #&40 ; '@'                                                    ; 936d: 09 40       .@  :040e[2]   ; Map &80-&BF range to &C0-&FF for comparison
    cmp tube_claimed_id                                               ; 936f: c5 15       ..  :0410[2]   ; Is this for our currently-claimed address?
    bne return_tube_init                                              ; 9371: d0 11       ..  :0412[2]   ; Not our address: return
; &9373 referenced 1 time by &813f
.tube_post_init
    lda #&80                                                          ; 9373: a9 80       ..  :0414[2]   ; &80 sentinel: clear address claim
    sta tube_claim_flag                                               ; 9375: 85 14       ..  :0416[2]   ; Store to claim-in-progress flag
    rts                                                               ; 9377: 60          `   :0418[2]   ; Return from tube_post_init

; &9378 referenced 1 time by &040c[2]
.addr_claim_external
    asl tube_claim_flag                                               ; 9378: 06 14       ..  :0419[2]   ; Another host claiming; check if we're owner
    bcs accept_new_claim                                              ; 937a: b0 06       ..  :041b[2]   ; C=1: we have an active claim
    cmp tube_claimed_id                                               ; 937c: c5 15       ..  :041d[2]   ; Compare with our claimed address
    beq return_tube_init                                              ; 937e: f0 04       ..  :041f[2]   ; Match: return (we already have it)
    clc                                                               ; 9380: 18          .   :0421[2]   ; Not ours: CLC = we don't own this address
    rts                                                               ; 9381: 60          `   :0422[2]   ; Return with C=0 (claim denied)

; &9382 referenced 1 time by &041b[2]
.accept_new_claim
    sta tube_claimed_id                                               ; 9382: 85 15       ..  :0423[2]   ; Accept new claim: update our address
; &9384 referenced 2 times by &0412[2], &041f[2]
.return_tube_init
    rts                                                               ; 9384: 60          `   :0425[2]   ; Return with address updated

; &9385 referenced 1 time by &0408[2]
.setup_data_transfer
    sty tube_data_ptr_hi                                              ; 9385: 84 13       ..  :0426[2]   ; Save 16-bit transfer address from (X,Y)
    stx tube_data_ptr                                                 ; 9387: 86 12       ..  :0428[2]   ; Store address pointer low byte
    jsr tube_send_r4                                                  ; 9389: 20 d6 06     .. :042a[2]   ; Send transfer type byte to co-processor
    tax                                                               ; 938c: aa          .   :042d[2]   ; X = transfer type for table lookup
    ldy #3                                                            ; 938d: a0 03       ..  :042e[2]   ; Y=3: send 4 bytes (address + claimed addr)
; &938f referenced 1 time by &0436[2]
.send_xfer_addr_bytes
    lda (tube_data_ptr),y                                             ; 938f: b1 12       ..  :0430[2]   ; Load transfer address byte from (X,Y)
    jsr tube_send_r4                                                  ; 9391: 20 d6 06     .. :0432[2]   ; Send address byte to co-processor via R4
    dey                                                               ; 9394: 88          .   :0435[2]   ; Previous byte (big-endian: 3,2,1,0)
    bpl send_xfer_addr_bytes                                          ; 9395: 10 f8       ..  :0436[2]   ; Loop for all 4 address bytes
    jsr tube_send_r4                                                  ; 9397: 20 d6 06     .. :0438[2]   ; Send claimed address via R4
    ldy #&18                                                          ; 939a: a0 18       ..  :043b[2]   ; Y=&18: enable Tube control register
    sty tube_status_1_and_tube_control                                ; 939c: 8c e0 fe    ... :043d[2]   ; Enable Tube interrupt generation
    lda tube_xfer_ctrl_bits,x                                         ; 939f: bd 6b 04    .k. :0440[2]   ; Look up Tube control bits for this xfer type
    sta tube_status_1_and_tube_control                                ; 93a2: 8d e0 fe    ... :0443[2]   ; Apply transfer-specific control bits
    lsr a                                                             ; 93a5: 4a          J   :0446[2]   ; LSR: check bit 2 (2-byte flush needed?)
    lsr a                                                             ; 93a6: 4a          J   :0447[2]   ; LSR: shift bit 2 to carry
; &93a7 referenced 1 time by &044b[2]
.poll_r4_copro_ack
    bit tube_status_register_4_and_cpu_control                        ; 93a7: 2c e6 fe    ,.. :0448[2]   ; Poll R4 status for co-processor response
    bvc poll_r4_copro_ack                                             ; 93aa: 50 fb       P.  :044b[2]   ; Bit 6 clear: not ready, keep polling
    bcs flush_r3_nmi_check                                            ; 93ac: b0 0d       ..  :044d[2]   ; R4 bit 7: co-processor acknowledged transfer
    cpx #4                                                            ; 93ae: e0 04       ..  :044f[2]   ; Type 4 = SENDW (host-to-parasite word xfer)
    bne return_tube_xfer                                              ; 93b0: d0 17       ..  :0451[2]   ; Not SENDW type: skip release path
    pla                                                               ; 93b2: 68          h   :0453[2]   ; Discard return address (low byte)
    pla                                                               ; 93b3: 68          h   :0454[2]   ; Discard return address (high byte)
; &93b4 referenced 1 time by &04b8[2]
.release_claim_restart
    lda #&80                                                          ; 93b4: a9 80       ..  :0455[2]   ; A=&80: reset claim flag sentinel
    sta tube_claim_flag                                               ; 93b6: 85 14       ..  :0457[2]   ; Clear claim-in-progress flag
    jmp tube_reply_byte                                               ; 93b8: 4c cd 05    L.. :0459[2]   ; Restart Tube main loop

; &93bb referenced 1 time by &044d[2]
.flush_r3_nmi_check
    bit tube_data_register_3                                          ; 93bb: 2c e5 fe    ,.. :045c[2]   ; Flush R3 data (first byte)
    bit tube_data_register_3                                          ; 93be: 2c e5 fe    ,.. :045f[2]   ; Flush R3 data (second byte)
.copro_ack_nmi_check
    lsr a                                                             ; 93c1: 4a          J   :0462[2]   ; LSR: check bit 0 (NMI used?)
    bcc return_tube_xfer                                              ; 93c2: 90 05       ..  :0463[2]   ; C=0: NMI not used, skip NMI release
    ldy #&88                                                          ; 93c4: a0 88       ..  :0465[2]   ; Release Tube NMI (transfer used interrupts)
    sty tube_status_1_and_tube_control                                ; 93c6: 8c e0 fe    ... :0467[2]   ; Write &88 to Tube control to release NMI
; &93c9 referenced 2 times by &0451[2], &0463[2]
.return_tube_xfer
    rts                                                               ; 93c9: 60          `   :046a[2]   ; Return from transfer setup

; &93ca referenced 1 time by &0440[2]
.tube_xfer_ctrl_bits
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; 93ca: 86 88 96... ... :046b[2]

; &93d2 referenced 1 time by &0400[2]
.tube_begin
    cli                                                               ; 93d2: 58          X   :0473[2]   ; BEGIN: enable interrupts for Tube host code
    php                                                               ; 93d3: 08          .   :0474[2]   ; Save processor status
    pha                                                               ; 93d4: 48          H   :0475[2]   ; Save A on stack
    ldy #0                                                            ; 93d5: a0 00       ..  :0476[2]   ; Y=0: start at beginning of page
    sty tube_transfer_addr                                            ; 93d7: 84 57       .W  :0478[2]   ; Store to zero page pointer low byte
; ***************************************************************************************
; Initialise relocation address for ROM transfer
; 
; Sets source page to &8000 and page counter to &80. Checks
; ROM type bit 5 for a relocation address in the ROM header;
; if present, extracts the 4-byte address from after the
; copyright string. Otherwise uses default &8000 start.
; ***************************************************************************************
.tube_init_reloc
    lda #&80                                                          ; 93d9: a9 80       ..  :047a[2]   ; Init: start sending from &8000
    sta tube_xfer_page                                                ; 93db: 85 58       .X  :047c[2]   ; Store &80 as source page high byte
    sta zp_ptr_hi                                                     ; 93dd: 85 01       ..  :047e[2]   ; Store &80 as page counter initial value
    lda #&20 ; ' '                                                    ; 93df: a9 20       .   :0480[2]   ; A=&20: bit 5 mask for ROM type check
    and rom_type                                                      ; 93e1: 2d 06 80    -.. :0482[2]   ; ROM type bit 5: reloc address in header?
    beq store_xfer_end_addr                                           ; 93e4: f0 19       ..  :0485[2]   ; No reloc addr: use defaults
    ldx copyright_offset                                              ; 93e6: ae 07 80    ... :0487[2]   ; Skip past copyright string to find reloc addr
; &93e9 referenced 1 time by &048e[2]
.scan_copyright_end
    inx                                                               ; 93e9: e8          .   :048a[2]   ; Skip past null-terminated copyright string
    lda rom_header,x                                                  ; 93ea: bd 00 80    ... :048b[2]   ; Load next byte from ROM header
    bne scan_copyright_end                                            ; 93ed: d0 fa       ..  :048e[2]   ; Loop until null terminator found
    lda lang_entry_lo,x                                               ; 93ef: bd 01 80    ... :0490[2]   ; Read 4-byte reloc address from ROM header
    sta tube_transfer_addr                                            ; 93f2: 85 57       .W  :0493[2]   ; Store reloc addr byte 1 as transfer addr
    lda lang_entry_hi,x                                               ; 93f4: bd 02 80    ... :0495[2]   ; Load reloc addr byte 2
    sta tube_xfer_page                                                ; 93f7: 85 58       .X  :0498[2]   ; Store as source page start
    ldy service_entry,x                                               ; 93f9: bc 03 80    ... :049a[2]   ; Load reloc addr byte 3
    lda svc_entry_lo,x                                                ; 93fc: bd 04 80    ... :049d[2]   ; Load reloc addr byte 4 (highest)
; &93ff referenced 1 time by &0485[2]
.store_xfer_end_addr
    sta tube_xfer_addr_3                                              ; 93ff: 85 5a       .Z  :04a0[2]   ; Store high byte of end address
    sty tube_xfer_addr_2                                              ; 9401: 84 59       .Y  :04a2[2]   ; Store byte 3 of end address
    pla                                                               ; 9403: 68          h   :04a4[2]   ; Restore A from stack
    plp                                                               ; 9404: 28          (   :04a5[2]   ; Restore processor status
    bcs beginr                                                        ; 9405: b0 12       ..  :04a6[2]   ; Carry set: language entry (claim Tube)
    tax                                                               ; 9407: aa          .   :04a8[2]   ; X = A (preserved from entry)
    bne begink                                                        ; 9408: d0 03       ..  :04a9[2]   ; Non-zero: check break type
    jmp tube_reply_ack                                                ; 940a: 4c cb 05    L.. :04ab[2]   ; A=0: acknowledge and return

; &940d referenced 1 time by &04a9[2]
.begink
    ldx #0                                                            ; 940d: a2 00       ..  :04ae[2]   ; X=0 for OSBYTE read
    ldy #&ff                                                          ; 940f: a0 ff       ..  :04b0[2]   ; Y=&FF for OSBYTE read
    lda #osbyte_read_write_last_break_type                            ; 9411: a9 fd       ..  :04b2[2]   ; OSBYTE &FD: read last break type
    jsr osbyte                                                        ; 9413: 20 f4 ff     .. :04b4[2]   ; Read type of last reset
    txa                                                               ; 9416: 8a          .   :04b7[2]   ; X=value of type of last reset
    beq release_claim_restart                                         ; 9417: f0 9b       ..  :04b8[2]   ; Soft break (0): skip ROM transfer
; &9419 referenced 2 times by &04a6[2], &04bf[2]
.beginr
    lda #&ff                                                          ; 9419: a9 ff       ..  :04ba[2]   ; A=&FF: claim Tube for all operations
    jsr tube_addr_claim                                               ; 941b: 20 06 04     .. :04bc[2]   ; Claim Tube address via R4
    bcc beginr                                                        ; 941e: 90 f9       ..  :04bf[2]   ; Not claimed: retry until claimed
    lda #1                                                            ; 9420: a9 01       ..  :04c1[2]   ; Transfer type 1 (parasite to host)
    jsr tube_setup_transfer                                           ; 9422: 20 e0 04     .. :04c3[2]   ; Set up Tube transfer parameters
    ldy #0                                                            ; 9425: a0 00       ..  :04c6[2]   ; Y=0: start at page boundary
    sty zp_ptr_lo                                                     ; 9427: 84 00       ..  :04c8[2]   ; Source ptr low = 0
    ldx #&40 ; '@'                                                    ; 9429: a2 40       .@  :04ca[2]   ; X=&40: 64 pages (16KB) to transfer
; &942b referenced 2 times by &04d7[2], &04dc[2]
.send_rom_byte
    lda (zp_ptr_lo),y                                                 ; 942b: b1 00       ..  :04cc[2]   ; Read byte from source address
    sta tube_data_register_3                                          ; 942d: 8d e5 fe    ... :04ce[2]   ; Send byte to Tube via R3
; &9430 referenced 1 time by &04d4[2]
.poll_r3_ready
    bit tube_status_register_3                                        ; 9430: 2c e4 fe    ,.. :04d1[2]   ; Check R3 status
    bvc poll_r3_ready                                                 ; 9433: 50 fb       P.  :04d4[2]   ; Not ready: wait for Tube
    iny                                                               ; 9435: c8          .   :04d6[2]   ; Next byte in page
    bne send_rom_byte                                                 ; 9436: d0 f3       ..  :04d7[2]   ; More bytes in page: continue
    inc zp_ptr_hi                                                     ; 9438: e6 01       ..  :04d9[2]   ; Next source page
    dex                                                               ; 943a: ca          .   :04db[2]   ; Decrement page counter
    bne send_rom_byte                                                 ; 943b: d0 ee       ..  :04dc[2]   ; More pages: continue transfer
    lda #4                                                            ; 943d: a9 04       ..  :04de[2]   ; Transfer type 4 (host to parasite burst)
; &943f referenced 1 time by &04c3[2]
.tube_setup_transfer
    ldy #0                                                            ; 943f: a0 00       ..  :04e0[2]   ; Y=0: low byte of param block ptr
    ldx #&57 ; 'W'                                                    ; 9441: a2 57       .W  :04e2[2]   ; X=&57: param block at &0057
    jmp tube_addr_claim                                               ; 9443: 4c 06 04    L.. :04e4[2]   ; Claim Tube and start transfer

.tube_rdch_handler
    lda #1                                                            ; 9446: a9 01       ..  :04e7[2]   ; R2 command: OSRDCH request
    jsr tube_send_r2                                                  ; 9448: 20 cd 06     .. :04e9[2]   ; Send OSRDCH request to host
    jmp tube_enter_main_loop                                          ; 944b: 4c 36 00    L6. :04ec[2]   ; Jump to RDCH completion handler

.tube_restore_regs
    ldy zp_temp_10                                                    ; 944e: a4 10       ..  :04ef[2]   ; Restore saved Y register
    ldx zp_temp_11                                                    ; 9450: a6 11       ..  :04f1[2]   ; Restore X from saved value
    jsr tube_read_r2                                                  ; 9452: 20 f7 04     .. :04f3[2]   ; Read result byte from R2
    asl a                                                             ; 9455: 0a          .   :04f6[2]   ; Shift carry into C flag
; &9456 referenced 22 times by &04f3[2], &04fa[2], &0543[3], &0547[3], &0550[3], &0569[3], &0580[3], &058c[3], &0592[3], &059b[3], &05b5[3], &05da[3], &05eb[3], &0604[4], &060c[4], &0623[4], &0627[4], &0638[4], &063c[4], &0640[4], &065a[4], &06a2[4]
.tube_read_r2
    bit tube_status_register_2                                        ; 9456: 2c e2 fe    ,.. :04f7[2]   ; Poll R2 status register
    bpl tube_read_r2                                                  ; 9459: 10 fb       ..  :04fa[2]   ; Bit 7 clear: R2 not ready, wait
    lda tube_data_register_2                                          ; 945b: ad e3 fe    ... :04fc[2]   ; Read byte from R2 data register
    rts                                                               ; 945e: 60          `   :04ff[2]   ; Return with pointers initialised


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, reloc_p4_src

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &0500

    ; Set the program counter to the next position in the binary file.
    org reloc_p4_src + (* - tube_code_page4)

.l945f

; Move 3: &945f to &0500 for length 256
    org &0500
; ***************************************************************************************
; Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)
; 
; Copied from ROM at &944D during init. Contains:
;   &0500: tube_dispatch_table — 14-entry handler address table
;   &051C: tube_wrch_handler — WRCHV target
;   &051F: tube_send_and_poll — send byte via R2, poll for reply
;   &0527: tube_poll_r1_wrch — service R1 WRCH while waiting for R2
;   &053D: tube_release_return — restore regs and RTS
;   &0543: tube_osbput — write byte to file
;   &0550: tube_osbget — read byte from file
;   &055B: tube_osrdch — read character
;   &0569: tube_osfind — open file
;   &0580: tube_osfind_close — close file (A=0)
;   &058C: tube_osargs — file argument read/write
;   &05B1: tube_read_string — read CR-terminated string into &0700
;   &05C5: tube_oscli — execute * command
;   &05CB: tube_reply_ack — send &7F acknowledge
;   &05CD: tube_reply_byte — send byte and return to main loop
;   &05D8: tube_osfile — whole file operation
; ***************************************************************************************
; &945f referenced 2 times by &0054[1], &8133
.tube_dispatch_table
    equw tube_osrdch                                                  ; 945f: 5b 05       [.  :0500[3]   ; cmd 0: OSRDCH
    equw tube_oscli                                                   ; 9461: c5 05       ..  :0502[3]   ; cmd 1: OSCLI
    equw tube_osbyte_short                                            ; 9463: 23 06       #.  :0504[3]   ; cmd 2: OSBYTE (2-param)
    equw tube_osbyte_long                                             ; 9465: 38 06       8.  :0506[3]   ; cmd 3: OSBYTE (3-param)
    equw tube_osword                                                  ; 9467: 5a 06       Z.  :0508[3]   ; cmd 4: OSWORD
    equw tube_osword_rdln                                             ; 9469: a0 06       ..  :050a[3]   ; cmd 5: OSWORD 0 (read line)
    equw tube_restore_regs                                            ; 946b: ef 04       ..  :050c[3]   ; cmd 6: release/restore regs
    equw tube_release_return                                          ; 946d: 3d 05       =.  :050e[3]   ; cmd 7: restore regs, RTS
    equw tube_osargs                                                  ; 946f: 8c 05       ..  :0510[3]   ; cmd 8: OSARGS
    equw tube_osbget                                                  ; 9471: 50 05       P.  :0512[3]   ; cmd 9: OSBGET
    equw tube_osbput                                                  ; 9473: 43 05       C.  :0514[3]   ; cmd 10: OSBPUT
    equw tube_osfind                                                  ; 9475: 69 05       i.  :0516[3]   ; cmd 11: OSFIND
    equw tube_osfile                                                  ; 9477: d8 05       ..  :0518[3]   ; cmd 12: OSFILE
    equw tube_osgbpb                                                  ; 9479: 02 06       ..  :051a[3]   ; cmd 13: OSGBPB

.tube_wrch_handler
    pha                                                               ; 947b: 48          H   :051c[3]   ; Save A for WRCHV echo
    lda #0                                                            ; 947c: a9 00       ..  :051d[3]   ; A=0: send null prefix via R2
.tube_send_and_poll
    jsr tube_send_r2                                                  ; 947e: 20 cd 06     .. :051f[3]   ; Send prefix byte to co-processor
; &9481 referenced 2 times by &052a[3], &0532[3]
.poll_r2_reply
    bit tube_status_register_2                                        ; 9481: 2c e2 fe    ,.. :0522[3]   ; Poll R2 for co-processor reply
    bvs wrch_echo_reply                                               ; 9484: 70 0e       p.  :0525[3]   ; R2 ready: go process reply
.tube_poll_r1_wrch
    bit tube_status_1_and_tube_control                                ; 9486: 2c e0 fe    ,.. :0527[3]   ; Check R1 for pending WRCH request
    bpl poll_r2_reply                                                 ; 9489: 10 f6       ..  :052a[3]   ; No R1 data: back to polling R2
    lda tube_data_register_1                                          ; 948b: ad e1 fe    ... :052c[3]   ; Read WRCH character from R1
    jsr nvwrch                                                        ; 948e: 20 cb ff     .. :052f[3]   ; Write character
.tube_resume_poll
    jmp poll_r2_reply                                                 ; 9491: 4c 22 05    L". :0532[3]   ; Resume R2 polling after servicing

; &9494 referenced 1 time by &0525[3]
.wrch_echo_reply
    pla                                                               ; 9494: 68          h   :0535[3]   ; Recover original character
    sta tube_data_register_2                                          ; 9495: 8d e3 fe    ... :0536[3]   ; Echo character back via R2
    pha                                                               ; 9498: 48          H   :0539[3]   ; Push for dispatch loop re-entry
    jmp tube_enter_main_loop                                          ; 9499: 4c 36 00    L6. :053a[3]   ; Enter main dispatch loop

.tube_release_return
    ldx zp_temp_11                                                    ; 949c: a6 11       ..  :053d[3]   ; Restore saved X from temporary
    ldy zp_temp_10                                                    ; 949e: a4 10       ..  :053f[3]   ; Restore saved Y from temporary
    pla                                                               ; 94a0: 68          h   :0541[3]   ; Restore saved A
    rts                                                               ; 94a1: 60          `   :0542[3]   ; Return to caller

.tube_osbput
    jsr tube_read_r2                                                  ; 94a2: 20 f7 04     .. :0543[3]   ; Read channel handle from R2
    tay                                                               ; 94a5: a8          .   :0546[3]   ; Y=channel handle from R2
    jsr tube_read_r2                                                  ; 94a6: 20 f7 04     .. :0547[3]   ; Read data byte from R2 for BPUT
    jsr osbput                                                        ; 94a9: 20 d4 ff     .. :054a[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 94ac: 4c cb 05    L.. :054d[3]   ; BPUT done: send acknowledge, return

.tube_osbget
    jsr tube_read_r2                                                  ; 94af: 20 f7 04     .. :0550[3]   ; Read channel handle from R2
    tay                                                               ; 94b2: a8          .   :0553[3]   ; Y=channel handle for OSBGET; Y=file handle
    jsr osbget                                                        ; 94b3: 20 d7 ff     .. :0554[3]   ; Read a single byte from an open file Y
    pha                                                               ; 94b6: 48          H   :0557[3]   ; Save byte read from file
    jmp send_reply_ok                                                 ; 94b7: 4c 5f 05    L_. :0558[3]   ; Send carry+byte reply (BGET result)

.tube_osrdch
    jsr nvrdch                                                        ; 94ba: 20 c8 ff     .. :055b[3]   ; Read a character from the current input stream
    pha                                                               ; 94bd: 48          H   :055e[3]   ; A=character read
; &94be referenced 2 times by &0558[3], &0620[4]
.send_reply_ok
    ora #&80                                                          ; 94be: 09 80       ..  :055f[3]   ; Set bit 7 (no-error flag)
.tube_rdch_reply
    ror a                                                             ; 94c0: 6a          j   :0561[3]   ; ROR A: encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; 94c1: 20 cd 06     .. :0562[3]   ; = JSR tube_send_r2 (overlaps &053D entry)
    pla                                                               ; 94c4: 68          h   :0565[3]   ; Restore read character/byte
    jmp tube_reply_byte                                               ; 94c5: 4c cd 05    L.. :0566[3]   ; Return to Tube main loop

.tube_osfind
    jsr tube_read_r2                                                  ; 94c8: 20 f7 04     .. :0569[3]   ; Read open mode from R2
    beq tube_osfind_close                                             ; 94cb: f0 12       ..  :056c[3]   ; A=0: close file, else open with filename
    pha                                                               ; 94cd: 48          H   :056e[3]   ; Save open mode while reading filename
    jsr tube_read_string                                              ; 94ce: 20 b1 05     .. :056f[3]   ; Read filename string from R2 into &0700
    pla                                                               ; 94d1: 68          h   :0572[3]   ; Recover open mode from stack
    jsr osfind                                                        ; 94d2: 20 ce ff     .. :0573[3]   ; Open or close file(s)
    pha                                                               ; 94d5: 48          H   :0576[3]   ; Save file handle result
    lda #&ff                                                          ; 94d6: a9 ff       ..  :0577[3]   ; A=&FF: success marker
    jsr tube_send_r2                                                  ; 94d8: 20 cd 06     .. :0579[3]   ; Send success marker via R2
    pla                                                               ; 94db: 68          h   :057c[3]   ; Restore file handle
    jmp tube_reply_byte                                               ; 94dc: 4c cd 05    L.. :057d[3]   ; Send file handle result to co-processor

; &94df referenced 1 time by &056c[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; 94df: 20 f7 04     .. :0580[3]   ; OSFIND close: read handle from R2
    tay                                                               ; 94e2: a8          .   :0583[3]   ; Y=handle to close
    lda #osfind_close                                                 ; 94e3: a9 00       ..  :0584[3]   ; A=0: close command for OSFIND
    jsr osfind                                                        ; 94e5: 20 ce ff     .. :0586[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94e8: 4c cb 05    L.. :0589[3]   ; Close done: send acknowledge, return

.tube_osargs
    jsr tube_read_r2                                                  ; 94eb: 20 f7 04     .. :058c[3]   ; Read file handle from R2
    tay                                                               ; 94ee: a8          .   :058f[3]   ; Y=file handle for OSARGS
.tube_read_params
    ldx #3                                                            ; 94ef: a2 03       ..  :0590[3]   ; Read 4-byte arg + reason from R2 into ZP
; &94f1 referenced 1 time by &0598[3]
.read_osargs_params
    jsr tube_read_r2                                                  ; 94f1: 20 f7 04     .. :0592[3]   ; Read next param byte from R2
    sta zp_ptr_lo,x                                                   ; 94f4: 95 00       ..  :0595[3]   ; Params stored at &00-&03 (little-endian)
    dex                                                               ; 94f6: ca          .   :0597[3]   ; Decrement byte counter
    bpl read_osargs_params                                            ; 94f7: 10 f8       ..  :0598[3]   ; Loop until all 4 bytes read
    inx                                                               ; 94f9: e8          .   :059a[3]   ; X=0: reset index after loop
    jsr tube_read_r2                                                  ; 94fa: 20 f7 04     .. :059b[3]   ; Read OSARGS reason code from R2
    jsr osargs                                                        ; 94fd: 20 da ff     .. :059e[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 9500: 20 cd 06     .. :05a1[3]   ; Send result A back to co-processor
    ldx #3                                                            ; 9503: a2 03       ..  :05a4[3]   ; Return 4-byte result from ZP &00-&03
; &9505 referenced 1 time by &05ac[3]
.send_osargs_result
    lda zp_ptr_lo,x                                                   ; 9505: b5 00       ..  :05a6[3]   ; Load result byte from zero page
    jsr tube_send_r2                                                  ; 9507: 20 cd 06     .. :05a8[3]   ; Send byte to co-processor via R2
    dex                                                               ; 950a: ca          .   :05ab[3]   ; Previous byte (count down)
    bpl send_osargs_result                                            ; 950b: 10 f8       ..  :05ac[3]   ; Loop for all 4 bytes
    jmp tube_main_loop                                                ; 950d: 4c 3a 00    L:. :05ae[3]   ; Return to Tube main loop

; &9510 referenced 3 times by &056f[3], &05c5[3], &05e2[3]
.tube_read_string
    ldx #0                                                            ; 9510: a2 00       ..  :05b1[3]   ; X=0: initialise string buffer index
    ldy #0                                                            ; 9512: a0 00       ..  :05b3[3]   ; Y=0: string buffer offset 0
; &9514 referenced 1 time by &05c0[3]
.strnh
    jsr tube_read_r2                                                  ; 9514: 20 f7 04     .. :05b5[3]   ; Read next string byte from R2
    sta l0700,y                                                       ; 9517: 99 00 07    ... :05b8[3]   ; Store byte in string buffer at &0700+Y
    iny                                                               ; 951a: c8          .   :05bb[3]   ; Next buffer position
    beq string_buf_done                                               ; 951b: f0 04       ..  :05bc[3]   ; Y overflow: string too long, truncate
    cmp #&0d                                                          ; 951d: c9 0d       ..  :05be[3]   ; Check for CR terminator
    bne strnh                                                         ; 951f: d0 f3       ..  :05c0[3]   ; Not CR: continue reading string
; &9521 referenced 1 time by &05bc[3]
.string_buf_done
    ldy #7                                                            ; 9521: a0 07       ..  :05c2[3]   ; Y=7: set XY=&0700 for OSCLI/OSFIND
    rts                                                               ; 9523: 60          `   :05c4[3]   ; Return with XY pointing to &0700

.tube_oscli
    jsr tube_read_string                                              ; 9524: 20 b1 05     .. :05c5[3]   ; Read command string from R2
    jsr oscli                                                         ; 9527: 20 f7 ff     .. :05c8[3]   ; Execute * command via OSCLI
; &952a referenced 3 times by &04ab[2], &054d[3], &0589[3]
.tube_reply_ack
    lda #&7f                                                          ; 952a: a9 7f       ..  :05cb[3]   ; &7F = success acknowledgement
; &952c referenced 5 times by &0459[2], &0566[3], &057d[3], &05d0[3], &06b5[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 952c: 2c e2 fe    ,.. :05cd[3]   ; Poll R2 status until ready
    bvc tube_reply_byte                                               ; 952f: 50 fb       P.  :05d0[3]   ; Bit 6 clear: not ready, loop
    sta tube_data_register_2                                          ; 9531: 8d e3 fe    ... :05d2[3]   ; Write byte to R2 data register
; &9534 referenced 1 time by &0600[4]
.mj
    jmp tube_main_loop                                                ; 9534: 4c 3a 00    L:. :05d5[3]   ; Return to Tube main loop

.tube_osfile
    ldx #&10                                                          ; 9537: a2 10       ..  :05d8[3]   ; X=&10: 16 bytes for OSFILE CB
; &9539 referenced 1 time by &05e0[3]
.argsw
    jsr tube_read_r2                                                  ; 9539: 20 f7 04     .. :05da[3]   ; Read next control block byte from R2
    sta zp_ptr_hi,x                                                   ; 953c: 95 01       ..  :05dd[3]   ; Store at &01+X (descending)
    dex                                                               ; 953e: ca          .   :05df[3]   ; Decrement byte counter
    bne argsw                                                         ; 953f: d0 f8       ..  :05e0[3]   ; Loop for all 16 bytes
    jsr tube_read_string                                              ; 9541: 20 b1 05     .. :05e2[3]   ; Read filename string from R2 into &0700
    stx zp_ptr_lo                                                     ; 9544: 86 00       ..  :05e5[3]   ; XY=&0700: filename pointer for OSFILE
    sty zp_ptr_hi                                                     ; 9546: 84 01       ..  :05e7[3]   ; Store Y=7 as pointer high byte
    ldy #0                                                            ; 9548: a0 00       ..  :05e9[3]   ; Y=0 for OSFILE control block offset
    jsr tube_read_r2                                                  ; 954a: 20 f7 04     .. :05eb[3]   ; Read OSFILE reason code from R2
    jsr osfile                                                        ; 954d: 20 dd ff     .. :05ee[3]   ; Execute OSFILE operation
    ora #&80                                                          ; 9550: 09 80       ..  :05f1[3]   ; Set bit 7: mark result as present
    jsr tube_send_r2                                                  ; 9552: 20 cd 06     .. :05f3[3]   ; Send result A (object type) to co-processor
    ldx #&10                                                          ; 9555: a2 10       ..  :05f6[3]   ; Return 16-byte control block to co-processor
; &9557 referenced 1 time by &05fe[3]
.send_osfile_ctrl_blk
    lda zp_ptr_hi,x                                                   ; 9557: b5 01       ..  :05f8[3]   ; Load control block byte
    jsr tube_send_r2                                                  ; 9559: 20 cd 06     .. :05fa[3]   ; Send byte to co-processor via R2
    dex                                                               ; 955c: ca          .   :05fd[3]   ; Decrement byte counter
    bne send_osfile_ctrl_blk                                          ; 955d: d0 f8       ..  :05fe[3]   ; Loop for all 16 bytes

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_dispatch_table, *, l945f

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org l945f + (* - tube_dispatch_table)

.c955f

; Move 4: &955f to &0600 for length 256
    org &0600
; ***************************************************************************************
; Tube host code page 6 — reference: NFS13 (GBPB-ESCA)
; 
; Copied from ROM at &954D during init. &0600-&0601 is the tail
; of tube_osfile (BEQ to tube_reply_byte when done). Contains:
;   &0602: tube_osgbpb — multi-byte file I/O
;   &0626: tube_osbyte_short — 2-param OSBYTE (returns X)
;   &063B: tube_osbyte_long — 3-param OSBYTE (returns carry+Y+X)
;   &065D: tube_osword — variable-length OSWORD (buffer at &0130)
;   &06A3: tube_osword_rdln — OSWORD 0 (read line, 5-byte params)
;   &06BB: tube_rdln_send_line — send input line from &0700
;   &06D0: tube_send_r2 — poll R2 status, write A to R2 data
;   &06D9: tube_send_r4 — poll R4 status, write A to R4 data
;   &06E2: tube_escape_check — check &FF, forward escape to R1
;   &06E8: tube_event_handler — EVNTV: forward event (A,X,Y) via R1
;   &06F7: tube_send_r1 — poll R1 status, write A to R1 data
; ***************************************************************************************
; &955f referenced 1 time by &8139
.tube_code_page6
    beq mj                                                            ; 955f: f0 d3       ..  :0600[4]   ; OSGBPB done: return to main loop
.tube_osgbpb
    ldx #&0c                                                          ; 9561: a2 0c       ..  :0602[4]   ; X=&0C: 13 bytes for OSGBPB CB
; &9563 referenced 1 time by &060a[4]
.read_gbpb_params
    jsr tube_read_r2                                                  ; 9563: 20 f7 04     .. :0604[4]   ; Read param byte from Tube R2
    sta zp_ptr_lo,x                                                   ; 9566: 95 00       ..  :0607[4]   ; Store in zero page param block
    dex                                                               ; 9568: ca          .   :0609[4]   ; Next byte (descending)
    bpl read_gbpb_params                                              ; 9569: 10 f8       ..  :060a[4]   ; Loop until all 13 bytes read
    jsr tube_read_r2                                                  ; 956b: 20 f7 04     .. :060c[4]   ; Read A (OSGBPB function code)
    inx                                                               ; 956e: e8          .   :060f[4]   ; X=0 after loop
    ldy #0                                                            ; 956f: a0 00       ..  :0610[4]   ; Y=0 for OSGBPB call
    jsr osgbpb                                                        ; 9571: 20 d1 ff     .. :0612[4]   ; Read or write multiple bytes to an open file
    pha                                                               ; 9574: 48          H   :0615[4]   ; Save OSGBPB result on stack
    ldx #&0c                                                          ; 9575: a2 0c       ..  :0616[4]   ; X=12: send 13 updated param bytes
; &9577 referenced 1 time by &061e[4]
.send_gbpb_params
    lda zp_ptr_lo,x                                                   ; 9577: b5 00       ..  :0618[4]   ; Load updated param byte
    jsr tube_send_r2                                                  ; 9579: 20 cd 06     .. :061a[4]   ; Send param byte via R2
    dex                                                               ; 957c: ca          .   :061d[4]   ; Next byte (descending)
    bpl send_gbpb_params                                              ; 957d: 10 f8       ..  :061e[4]   ; Loop until all 13 bytes sent
    jmp send_reply_ok                                                 ; 957f: 4c 5f 05    L_. :0620[4]   ; Return to main event loop

.tube_osbyte_short
    jsr tube_read_r2                                                  ; 9582: 20 f7 04     .. :0623[4]   ; Read X parameter from R2
    tax                                                               ; 9585: aa          .   :0626[4]   ; Save in X
    jsr tube_read_r2                                                  ; 9586: 20 f7 04     .. :0627[4]   ; Read A (OSBYTE function code)
    jsr osbyte                                                        ; 9589: 20 f4 ff     .. :062a[4]   ; Execute OSBYTE A,X
; &958c referenced 2 times by &0630[4], &0658[4]
.tube_osbyte_send_x
    bit tube_status_register_2                                        ; 958c: 2c e2 fe    ,.. :062d[4]   ; Poll R2 status (bit 6 = ready)
    bvc tube_osbyte_send_x                                            ; 958f: 50 fb       P.  :0630[4]   ; Not ready: keep polling
    stx tube_data_register_2                                          ; 9591: 8e e3 fe    ... :0632[4]   ; Send X result for 2-param OSBYTE
; &9594 referenced 1 time by &0648[4]
.bytex
    jmp tube_main_loop                                                ; 9594: 4c 3a 00    L:. :0635[4]   ; Return to main event loop

.tube_osbyte_long
    jsr tube_read_r2                                                  ; 9597: 20 f7 04     .. :0638[4]   ; Read X parameter from R2
    tax                                                               ; 959a: aa          .   :063b[4]   ; Save in X
    jsr tube_read_r2                                                  ; 959b: 20 f7 04     .. :063c[4]   ; Read Y parameter from co-processor
    tay                                                               ; 959e: a8          .   :063f[4]   ; Save in Y
    jsr tube_read_r2                                                  ; 959f: 20 f7 04     .. :0640[4]   ; Read A (OSBYTE function code)
    jsr osbyte                                                        ; 95a2: 20 f4 ff     .. :0643[4]   ; Execute OSBYTE A,X,Y
    eor #&9d                                                          ; 95a5: 49 9d       I.  :0646[4]   ; Test for OSBYTE &9D (fast Tube BPUT)
    beq bytex                                                         ; 95a7: f0 eb       ..  :0648[4]   ; OSBYTE &9D (fast Tube BPUT): no result needed
    lda #&40 ; '@'                                                    ; 95a9: a9 40       .@  :064a[4]   ; A=&40: high bit will hold carry
    ror a                                                             ; 95ab: 6a          j   :064c[4]   ; Encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; 95ac: 20 cd 06     .. :064d[4]   ; Send carry+status byte via R2
; &95af referenced 1 time by &0653[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 95af: 2c e2 fe    ,.. :0650[4]   ; Poll R2 status for ready
    bvc tube_osbyte_send_y                                            ; 95b2: 50 fb       P.  :0653[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; 95b4: 8c e3 fe    ... :0655[4]   ; Send Y result, then fall through to send X
    bvs tube_osbyte_send_x                                            ; 95b7: 70 d3       p.  :0658[4]   ; ALWAYS branch

.tube_osword
    jsr tube_read_r2                                                  ; 95b9: 20 f7 04     .. :065a[4]   ; Read OSWORD number from R2
    tay                                                               ; 95bc: a8          .   :065d[4]   ; Save OSWORD number in Y
; &95bd referenced 1 time by &0661[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 95bd: 2c e2 fe    ,.. :065e[4]   ; Poll R2 status for data ready
    bpl tube_osword_read                                              ; 95c0: 10 fb       ..  :0661[4]   ; Not ready: keep polling
    ldx tube_data_register_2                                          ; 95c2: ae e3 fe    ... :0663[4]   ; Read param block length from R2
    dex                                                               ; 95c5: ca          .   :0666[4]   ; DEX: length 0 means no params to read
    bmi skip_param_read                                               ; 95c6: 30 0f       0.  :0667[4]   ; No params (length=0): skip read loop
; &95c8 referenced 2 times by &066c[4], &0675[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 95c8: 2c e2 fe    ,.. :0669[4]   ; Poll R2 status for data ready
    bpl tube_osword_read_lp                                           ; 95cb: 10 fb       ..  :066c[4]   ; Not ready: keep polling
    lda tube_data_register_2                                          ; 95cd: ad e3 fe    ... :066e[4]   ; Read param byte from R2
    sta l0128,x                                                       ; 95d0: 9d 28 01    .(. :0671[4]   ; Store param bytes into block at &0128
    dex                                                               ; 95d3: ca          .   :0674[4]   ; Next param byte (descending)
    bpl tube_osword_read_lp                                           ; 95d4: 10 f2       ..  :0675[4]   ; Loop until all params read
    tya                                                               ; 95d6: 98          .   :0677[4]   ; Restore OSWORD number from Y
; &95d7 referenced 1 time by &0667[4]
.skip_param_read
    ldx #<(l0128)                                                     ; 95d7: a2 28       .(  :0678[4]   ; XY=&0128: param block address for OSWORD
    ldy #>(l0128)                                                     ; 95d9: a0 01       ..  :067a[4]   ; Y=&01: param block at &0128
    jsr osword                                                        ; 95db: 20 f1 ff     .. :067c[4]   ; Execute OSWORD with XY=&0128
    lda #&ff                                                          ; 95de: a9 ff       ..  :067f[4]   ; A=&FF: result marker for co-processor
    jsr tube_send_r2                                                  ; 95e0: 20 cd 06     .. :0681[4]   ; Send result marker via R2
; &95e3 referenced 1 time by &0687[4]
.poll_r2_osword_result
    bit tube_status_register_2                                        ; 95e3: 2c e2 fe    ,.. :0684[4]   ; Poll R2 status for ready
    bpl poll_r2_osword_result                                         ; 95e6: 10 fb       ..  :0687[4]   ; Not ready: keep polling
    ldx tube_data_register_2                                          ; 95e8: ae e3 fe    ... :0689[4]   ; Read result block length from R2
    dex                                                               ; 95eb: ca          .   :068c[4]   ; Decrement result byte counter
    bmi tube_return_main                                              ; 95ec: 30 0e       0.  :068d[4]   ; No results to send: return to main loop
; &95ee referenced 1 time by &069b[4]
.tube_osword_write
    ldy l0128,x                                                       ; 95ee: bc 28 01    .(. :068f[4]   ; Send result block bytes from &0128 via R2
; &95f1 referenced 1 time by &0695[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95f1: 2c e2 fe    ,.. :0692[4]   ; Poll R2 status for ready
    bvc tube_osword_write_lp                                          ; 95f4: 50 fb       P.  :0695[4]   ; Not ready: keep polling
    sty tube_data_register_2                                          ; 95f6: 8c e3 fe    ... :0697[4]   ; Send result byte via R2
    dex                                                               ; 95f9: ca          .   :069a[4]   ; Next result byte (descending)
    bpl tube_osword_write                                             ; 95fa: 10 f2       ..  :069b[4]   ; Loop until all results sent
; &95fc referenced 1 time by &068d[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95fc: 4c 3a 00    L:. :069d[4]   ; Return to main event loop

.tube_osword_rdln
    ldx #4                                                            ; 95ff: a2 04       ..  :06a0[4]   ; X=4: read 5-byte RDLN ctrl block
; &9601 referenced 1 time by &06a8[4]
.read_rdln_ctrl_block
    jsr tube_read_r2                                                  ; 9601: 20 f7 04     .. :06a2[4]   ; Read control block byte from R2
    sta zp_ptr_lo,x                                                   ; 9604: 95 00       ..  :06a5[4]   ; Store in zero page params
    dex                                                               ; 9606: ca          .   :06a7[4]   ; Next byte (descending)
    bpl read_rdln_ctrl_block                                          ; 9607: 10 f8       ..  :06a8[4]   ; Loop until all 5 bytes read
    inx                                                               ; 9609: e8          .   :06aa[4]   ; X=0 after loop, A=0 for OSWORD 0 (read line)
    ldy #0                                                            ; 960a: a0 00       ..  :06ab[4]   ; Y=0 for OSWORD 0
    txa                                                               ; 960c: 8a          .   :06ad[4]   ; A=0: OSWORD 0 (read line)
    jsr osword                                                        ; 960d: 20 f1 ff     .. :06ae[4]   ; Read input line from keyboard
    bcc tube_rdln_send_line                                           ; 9610: 90 05       ..  :06b1[4]   ; C=0: line read OK; C=1: escape pressed
    lda #&ff                                                          ; 9612: a9 ff       ..  :06b3[4]   ; &FF = escape/error signal to co-processor
    jmp tube_reply_byte                                               ; 9614: 4c cd 05    L.. :06b5[4]   ; Escape: send &FF error to co-processor

; &9617 referenced 1 time by &06b1[4]
.tube_rdln_send_line
    ldx #0                                                            ; 9617: a2 00       ..  :06b8[4]   ; X=0: start of input buffer at &0700
    lda #&7f                                                          ; 9619: a9 7f       ..  :06ba[4]   ; &7F = line read successfully
    jsr tube_send_r2                                                  ; 961b: 20 cd 06     .. :06bc[4]   ; Send &7F (success) to co-processor
; &961e referenced 1 time by &06c8[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 961e: bd 00 07    ... :06bf[4]   ; Load char from input buffer
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 9621: 20 cd 06     .. :06c2[4]   ; Send char to co-processor
    inx                                                               ; 9624: e8          .   :06c5[4]   ; Next character
    cmp #&0d                                                          ; 9625: c9 0d       ..  :06c6[4]   ; Check for CR terminator
    bne tube_rdln_send_loop                                           ; 9627: d0 f5       ..  :06c8[4]   ; Loop until CR terminator sent
    jmp tube_main_loop                                                ; 9629: 4c 3a 00    L:. :06ca[4]   ; Return to main event loop

; &962c referenced 17 times by &0020[1], &0026[1], &002c[1], &04e9[2], &051f[3], &0562[3], &0579[3], &05a1[3], &05a8[3], &05f3[3], &05fa[3], &061a[4], &064d[4], &0681[4], &06bc[4], &06c2[4], &06d0[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 962c: 2c e2 fe    ,.. :06cd[4]   ; Poll R2 status (bit 6 = ready)
    bvc tube_send_r2                                                  ; 962f: 50 fb       P.  :06d0[4]   ; Not ready: keep polling
    sta tube_data_register_2                                          ; 9631: 8d e3 fe    ... :06d2[4]   ; Write A to Tube R2 data register
    rts                                                               ; 9634: 60          `   :06d5[4]   ; Return to caller

; &9635 referenced 5 times by &0018[1], &042a[2], &0432[2], &0438[2], &06d9[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 9635: 2c e6 fe    ,.. :06d6[4]   ; Poll R4 status (bit 6 = ready)
    bvc tube_send_r4                                                  ; 9638: 50 fb       P.  :06d9[4]   ; Not ready: keep polling
    sta tube_data_register_4                                          ; 963a: 8d e7 fe    ... :06db[4]   ; Write A to Tube R4 data register
    rts                                                               ; 963d: 60          `   :06de[4]   ; Return to caller

; &963e referenced 1 time by &0403[2]
.tube_escape_check
    lda escape_flag                                                   ; 963e: a5 ff       ..  :06df[4]   ; Check OS escape flag at &FF
    sec                                                               ; 9640: 38          8   :06e1[4]   ; SEC+ROR: put bit 7 of &FF into carry+bit 7
    ror a                                                             ; 9641: 6a          j   :06e2[4]   ; ROR: shift escape bit 7 to carry
    bmi tube_send_r1                                                  ; 9642: 30 0f       0.  :06e3[4]   ; Escape set: forward to co-processor via R1
.tube_event_handler
    pha                                                               ; 9644: 48          H   :06e5[4]   ; EVNTV: forward event A, Y, X to co-processor
    lda #0                                                            ; 9645: a9 00       ..  :06e6[4]   ; Send &00 prefix (event notification)
    jsr tube_send_r1                                                  ; 9647: 20 f4 06     .. :06e8[4]   ; Send zero prefix via R1
    tya                                                               ; 964a: 98          .   :06eb[4]   ; Y value for event
    jsr tube_send_r1                                                  ; 964b: 20 f4 06     .. :06ec[4]   ; Send Y via R1
    txa                                                               ; 964e: 8a          .   :06ef[4]   ; X value for event
    jsr tube_send_r1                                                  ; 964f: 20 f4 06     .. :06f0[4]   ; Send X via R1
    pla                                                               ; 9652: 68          h   :06f3[4]   ; Restore A (event type)
; &9653 referenced 5 times by &06e3[4], &06e8[4], &06ec[4], &06f0[4], &06f7[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9653: 2c e0 fe    ,.. :06f4[4]   ; Poll R1 status (bit 6 = ready)
    bvc tube_send_r1                                                  ; 9656: 50 fb       P.  :06f7[4]   ; Not ready: keep polling
    sta tube_data_register_1                                          ; 9658: 8d e1 fe    ... :06f9[4]   ; Write A to Tube R1 data register
    rts                                                               ; 965b: 60          `   :06fc[4]   ; Return to caller

    equs " NE"                                                        ; 965c: 20 4e 45     NE :06fd[4]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page6, *, c955f

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page6, &0700

    ; Set the program counter to the next position in the binary file.
    org c955f + (* - tube_code_page6)


    org &8000

; Sideways ROM header
; NFS ROM 3.35D disassembly (Acorn Econet filing system)
; =====================================================
; &8000 referenced 2 times by &048b[2], &9bc7
.pydis_start
.rom_header
.language_entry
lang_entry_lo = rom_header+1
lang_entry_hi = rom_header+2
    jmp language_handler                                              ; 8000: 4c d4 80    L..            ; JMP language_handler

; &8001 referenced 1 time by &0490[2]
; &8002 referenced 1 time by &0495[2]
; &8003 referenced 1 time by &049a[2]
.service_entry
svc_entry_lo = service_entry+1
    jmp service_handler                                               ; 8003: 4c ea 80    L..            ; JMP service_handler

; &8004 referenced 1 time by &049d[2]
; &8006 referenced 1 time by &0482[2]
.rom_type
    equb &82                                                          ; 8006: 82          .
; &8007 referenced 1 time by &0487[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 0c          .
; &8008 referenced 2 times by &81de, &81e7
.binary_version
    equb 3                                                            ; 8008: 03          .
.title
    equs "NET"                                                        ; 8009: 4e 45 54    NET
.copyright
    equb 0                                                            ; 800c: 00          .
; The 'ROFF' suffix at &8010 is reused by the *ROFF
; command matcher (svc_star_command) — a space-saving
; trick that shares ROM bytes between the copyright
; string and the star command table.
.copyright_string
    equs "(C)ROFF"                                                    ; 800d: 28 43 29... (C)
; Error message offset table (9 entries).
; Each byte is a Y offset into error_msg_table.
; Entry 0 (Y=0, "Line Jammed") doubles as the
; copyright string null terminator.
; Indexed by TXCB status (AND #7), or hardcoded 8.
; &8014 referenced 1 time by &84dd
.error_offsets
    equb 0                                                            ; 8014: 00          .              ; "Line Jammed"
    equb &0d                                                          ; 8015: 0d          .              ; "Net Error"
    equb &18                                                          ; 8016: 18          .              ; "Not listening"
    equb &27                                                          ; 8017: 27          '              ; "No Clock"
    equb &31                                                          ; 8018: 31          1              ; "Escape"
    equb &31                                                          ; 8019: 31          1              ; "Escape"
    equb &31                                                          ; 801a: 31          1              ; "Escape"
    equb &39                                                          ; 801b: 39          9              ; "Bad Option"
    equb &45                                                          ; 801c: 45          E              ; "No reply"
; Four bytes with unknown purpose.
    equb 1                                                            ; 801d: 01          .              ; Purpose unknown
    equb 0                                                            ; 801e: 00          .              ; Purpose unknown
    equb &35                                                          ; 801f: 35          5              ; Purpose unknown
; &8020 referenced 1 time by &80e3
    equb 3                                                            ; 8020: 03          .              ; Purpose unknown
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at &80DA.
; See dispatch_0_hi (&8045) for the corresponding high bytes.
; 
; Five callers share this table via different Y base offsets:
;   Y=&00  Service calls 0-12       (indices 1-13)
;   Y=&0D  Language entry reasons    (indices 14-18)
;   Y=&12  FSCV codes 0-7           (indices 19-26)
;   Y=&16  FS reply handlers        (indices 27-32)
;   Y=&20  *NET1-4 sub-commands     (indices 33-36)
.dispatch_0_lo
    equb <(return_2-1)                                                ; 8021: 75          u              ; lo - Svc 0: already claimed (no-op)
    equb <(svc_1_abs_workspace-1)                                     ; 8022: ab          .              ; lo - Svc 1: absolute workspace
    equb <(svc_2_private_workspace-1)                                 ; 8023: b4          .              ; lo - Svc 2: private workspace
    equb <(svc_3_autoboot-1)                                          ; 8024: 0c          .              ; lo - Svc 3: auto-boot
    equb <(svc_4_star_command-1)                                      ; 8025: 82          .              ; lo - Svc 4: unrecognised star command
    equb <(svc_5_unknown_irq-1)                                       ; 8026: 6b          k              ; lo - Svc 5: unrecognised interrupt
    equb <(return_2-1)                                                ; 8027: 75          u              ; lo - Svc 6: BRK (no-op)
    equb <(dispatch_net_cmd-1)                                        ; 8028: 68          h              ; lo - Svc 7: unrecognised OSBYTE
    equb <(svc_8_osword-1)                                            ; 8029: 7d          }              ; lo - Svc 8: unrecognised OSWORD
    equb <(svc_9_help-1)                                              ; 802a: f6          .              ; lo - Svc 9: *HELP
    equb <(return_2-1)                                                ; 802b: 75          u              ; lo - Svc 10: static workspace (no-op)
    equb <(svc_11_nmi_claim-1)                                        ; 802c: 68          h              ; lo - Svc 11: NMI release (reclaim NMIs)
    equb <(svc_12_nmi_release-1)                                      ; 802d: 65          e              ; lo - Svc 12: NMI claim (save NMI state)
    equb <(lang_0_insert_remote_key-1)                                ; 802e: c4          .              ; lo - Lang 0: no language / Tube
    equb <(lang_1_remote_boot-1)                                      ; 802f: 76          v              ; lo - Lang 1: normal startup
    equb <(lang_2_save_palette_vdu-1)                                 ; 8030: a3          .              ; lo - Lang 2: softkey byte (Electron)
    equb <(lang_3_execute_at_0100-1)                                  ; 8031: a4          .              ; lo - Lang 3: softkey length (Electron)
    equb <(lang_4_remote_validated-1)                                 ; 8032: b4          .              ; lo - Lang 4: remote validated
    equb <(fscv_0_opt-1)                                              ; 8033: cb          .              ; lo - FSCV 0: *OPT
    equb <(fscv_1_eof-1)                                              ; 8034: 50          P              ; lo - FSCV 1: EOF check
    equb <(fscv_2_star_run-1)                                         ; 8035: c6          .              ; lo - FSCV 2: */ (run)
    equb <(fscv_3_star_cmd-1)                                         ; 8036: b3          .              ; lo - FSCV 3: unrecognised star command
    equb <(fscv_2_star_run-1)                                         ; 8037: c6          .              ; lo - FSCV 4: *RUN
    equb <(fscv_5_cat-1)                                              ; 8038: ff          .              ; lo - FSCV 5: *CAT
    equb <(fscv_6_shutdown-1)                                         ; 8039: 40          @              ; lo - FSCV 6: shutdown
    equb <(fscv_7_read_handles-1)                                     ; 803a: 55          U              ; lo - FSCV 7: read handle range
    equb <(fsreply_0_print_dir-1)                                     ; 803b: 5e          ^              ; lo - FS reply: print directory name
    equb <(fsreply_1_copy_handles_boot-1)                             ; 803c: 27          '              ; lo - FS reply: copy handles + boot
    equb <(fsreply_2_copy_handles-1)                                  ; 803d: 28          (              ; lo - FS reply: copy handles
    equb <(fsreply_3_set_csd-1)                                       ; 803e: 21          !              ; lo - FS reply: set CSD handle
    equb <(fsreply_4_notify_exec-1)                                   ; 803f: cc          .              ; lo - FS reply: notify + execute
    equb <(fsreply_5_set_lib-1)                                       ; 8040: 1c          .              ; lo - FS reply: set library handle
    equb <(net_1_read_handle-1)                                       ; 8041: 42          B              ; lo - *NET1: read handle from packet
    equb <(net_2_read_handle_entry-1)                                 ; 8042: 5d          ]              ; lo - *NET2: read handle from workspace
    equb <(net_3_close_handle-1)                                      ; 8043: 6d          m              ; lo - *NET3: close handle
; &8044 referenced 1 time by &80df
    equb <(net_4_resume_remote-1)                                     ; 8044: 89          .              ; lo - *NET4: resume remote
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_0_lo (&8021). Together they form a table
; of 37 handler addresses, used via the PHA/PHA/RTS trick at
; &80DA.
.dispatch_0_hi
    equb >(return_2-1)                                                ; 8045: 81          .              ; hi - Svc 0: already claimed (no-op)
    equb >(svc_1_abs_workspace-1)                                     ; 8046: 82          .              ; hi - Svc 1: absolute workspace
    equb >(svc_2_private_workspace-1)                                 ; 8047: 82          .              ; hi - Svc 2: private workspace
    equb >(svc_3_autoboot-1)                                          ; 8048: 82          .              ; hi - Svc 3: auto-boot
    equb >(svc_4_star_command-1)                                      ; 8049: 81          .              ; hi - Svc 4: unrecognised star command
    equb >(svc_5_unknown_irq-1)                                       ; 804a: 96          .              ; hi - Svc 5: unrecognised interrupt
    equb >(return_2-1)                                                ; 804b: 81          .              ; hi - Svc 6: BRK (no-op)
    equb >(dispatch_net_cmd-1)                                        ; 804c: 80          .              ; hi - Svc 7: unrecognised OSBYTE
    equb >(svc_8_osword-1)                                            ; 804d: 8e          .              ; hi - Svc 8: unrecognised OSWORD
    equb >(svc_9_help-1)                                              ; 804e: 81          .              ; hi - Svc 9: *HELP
    equb >(return_2-1)                                                ; 804f: 81          .              ; hi - Svc 10: static workspace (no-op)
    equb >(svc_11_nmi_claim-1)                                        ; 8050: 96          .              ; hi - Svc 11: NMI release (reclaim NMIs)
    equb >(svc_12_nmi_release-1)                                      ; 8051: 96          .              ; hi - Svc 12: NMI claim (save NMI state)
    equb >(lang_0_insert_remote_key-1)                                ; 8052: 84          .              ; hi - Lang 0: no language / Tube
    equb >(lang_1_remote_boot-1)                                      ; 8053: 84          .              ; hi - Lang 1: normal startup
    equb >(lang_2_save_palette_vdu-1)                                 ; 8054: 92          .              ; hi - Lang 2: softkey byte (Electron)
    equb >(lang_3_execute_at_0100-1)                                  ; 8055: 84          .              ; hi - Lang 3: softkey length (Electron)
    equb >(lang_4_remote_validated-1)                                 ; 8056: 84          .              ; hi - Lang 4: remote validated
    equb >(fscv_0_opt-1)                                              ; 8057: 89          .              ; hi - FSCV 0: *OPT
    equb >(fscv_1_eof-1)                                              ; 8058: 88          .              ; hi - FSCV 1: EOF check
    equb >(fscv_2_star_run-1)                                         ; 8059: 8d          .              ; hi - FSCV 2: */ (run)
    equb >(fscv_3_star_cmd-1)                                         ; 805a: 8b          .              ; hi - FSCV 3: unrecognised star command
    equb >(fscv_2_star_run-1)                                         ; 805b: 8d          .              ; hi - FSCV 4: *RUN
    equb >(fscv_5_cat-1)                                              ; 805c: 8b          .              ; hi - FSCV 5: *CAT
    equb >(fscv_6_shutdown-1)                                         ; 805d: 83          .              ; hi - FSCV 6: shutdown
    equb >(fscv_7_read_handles-1)                                     ; 805e: 86          .              ; hi - FSCV 7: read handle range
    equb >(fsreply_0_print_dir-1)                                     ; 805f: 8d          .              ; hi - FS reply: print directory name
    equb >(fsreply_1_copy_handles_boot-1)                             ; 8060: 8e          .              ; hi - FS reply: copy handles + boot
    equb >(fsreply_2_copy_handles-1)                                  ; 8061: 8e          .              ; hi - FS reply: copy handles
    equb >(fsreply_3_set_csd-1)                                       ; 8062: 8e          .              ; hi - FS reply: set CSD handle
    equb >(fsreply_4_notify_exec-1)                                   ; 8063: 8d          .              ; hi - FS reply: notify + execute
    equb >(fsreply_5_set_lib-1)                                       ; 8064: 8e          .              ; hi - FS reply: set library handle
    equb >(net_1_read_handle-1)                                       ; 8065: 8e          .              ; hi - *NET1: read handle from packet
    equb >(net_2_read_handle_entry-1)                                 ; 8066: 8e          .              ; hi - *NET2: read handle from workspace
    equb >(net_3_close_handle-1)                                      ; 8067: 8e          .              ; hi - *NET3: close handle
    equb >(net_4_resume_remote-1)                                     ; 8068: 81          .              ; hi - *NET4: resume remote

; ***************************************************************************************
; *NET command dispatcher
; 
; Parses the character after *NET as '1'-'4', maps to table
; indices 33-36 via base offset Y=&20, and dispatches via &80DA.
; Characters outside '1'-'4' fall through to return_1 (RTS).
; 
; These are internal sub-commands used only by the ROM itself,
; not user-accessible star commands. The MOS command parser
; requires a space or terminator after 'NET', so *NET1 typed
; at the command line does not match; these are reached only
; via OSCLI calls within the ROM.
; 
; *NET1 (&8E43): read file handle from received
; packet (net_1_read_handle)
; 
; *NET2 (&8E5E): read handle entry from workspace
; (net_2_read_handle_entry)
; 
; *NET3 (&8E6E): close handle / mark as unused
; (net_3_close_handle)
; 
; *NET4 (&818A): resume after remote operation
; (net_4_resume_remote)
; ***************************************************************************************
.dispatch_net_cmd
    lda osbyte_a_copy                                                 ; 8069: a5 ef       ..             ; Read command character following *NET
    sbc #&31 ; '1'                                                    ; 806b: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    bmi return_1                                                      ; 806d: 30 7a       0z             ; Negative: not a net command, exit
    cmp #4                                                            ; 806f: c9 04       ..             ; Command index >= 4: invalid *NET sub-command
    bcs return_1                                                      ; 8071: b0 76       .v             ; Out of range: return via c80e3/RTS
    tax                                                               ; 8073: aa          .              ; X = command index (0-3)
    lda #0                                                            ; 8074: a9 00       ..             ; Clear &A9 (used by dispatch)
    sta rom_svc_num                                                   ; 8076: 85 a9       ..             ; Store zero to &A9
    tya                                                               ; 8078: 98          .              ; Preserve A before dispatch
    ldy #&20 ; ' '                                                    ; 8079: a0 20       .              ; Y=&20: base offset for *NET commands (index 33+)
    bne dispatch                                                      ; 807b: d0 5d       .]             ; ALWAYS branch to dispatch; ALWAYS branch

; &807d referenced 1 time by &8082
.skip_iam_spaces
    iny                                                               ; 807d: c8          .              ; Advance past matched command text
; ***************************************************************************************
; "I AM" command handler
; 
; Dispatched from the command match table when the user types
; "*I AM <station>" or "*I AM <network>.<station>". Also used as
; the station number parser for "*NET <network>.<station>".
; Skips leading spaces, then calls parse_decimal twice if a dot
; separator is present. The first number becomes the network
; (&0E01, via TAX pass-through in parse_decimal) and the second
; becomes the station (&0E00). With a single number, it is stored
; as the station and the network defaults to 0 (local). If a colon
; follows, reads interactive input via OSRDCH and appends it to
; the command buffer. Finally jumps to forward_star_cmd.
; ***************************************************************************************
.i_am_handler
    lda (fs_options),y                                                ; 807e: b1 bb       ..             ; Load next char from command line
    cmp #&20 ; ' '                                                    ; 8080: c9 20       .              ; Skip spaces
    beq skip_iam_spaces                                               ; 8082: f0 f9       ..             ; Loop back to skip leading spaces
    cmp #&41 ; 'A'                                                    ; 8084: c9 41       .A             ; Colon = interactive remote command prefix
    bcs scan_for_colon                                                ; 8086: b0 11       ..             ; Char >= ':': skip number parsing
    lda #0                                                            ; 8088: a9 00       ..             ; A=0: default network number
    jsr parse_decimal                                                 ; 808a: 20 fd 85     ..            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc store_station_net                                             ; 808d: 90 04       ..             ; C=1: dot found, first number was network
    iny                                                               ; 808f: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8090: 20 fd 85     ..            ; Parse decimal number from (fs_options),Y (DECIN)
; &8093 referenced 1 time by &808d
.store_station_net
    sta fs_server_stn                                                 ; 8093: 8d 00 0e    ...            ; A=parsed value (accumulated in &B2)
    stx fs_server_net                                                 ; 8096: 8e 01 0e    ...            ; X=initial A value (saved by TAX)
; &8099 referenced 2 times by &8086, &80a2
.scan_for_colon
    iny                                                               ; 8099: c8          .              ; Skip past current character
    lda (fs_options),y                                                ; 809a: b1 bb       ..             ; Load next character from cmd line
    cmp #&0d                                                          ; 809c: c9 0d       ..             ; CR: end of command string?
    beq forward_star_cmd                                              ; 809e: f0 14       ..             ; Y=0: no colon found, send command
    cmp #&3a ; ':'                                                    ; 80a0: c9 3a       .:             ; Test for colon separator
    bne scan_for_colon                                                ; 80a2: d0 f5       ..             ; Not colon: keep scanning backward
    jsr oswrch                                                        ; 80a4: 20 ee ff     ..            ; Echo colon, then read user input from keyboard; Write character
; &80a7 referenced 1 time by &80af
.read_remote_cmd_line
    jsr osrdch                                                        ; 80a7: 20 e0 ff     ..            ; Check for escape condition; Read a character from the current input stream
    sta (fs_options),y                                                ; 80aa: 91 bb       ..             ; A=character read
    iny                                                               ; 80ac: c8          .              ; Advance write pointer
    cmp #&0d                                                          ; 80ad: c9 0d       ..             ; Test for CR (end of line)
    bne read_remote_cmd_line                                          ; 80af: d0 f6       ..             ; Not CR: continue reading input
    jsr osnewl                                                        ; 80b1: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
; ***************************************************************************************
; Forward unrecognised * command to fileserver (COMERR)
; 
; Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
; prepares an FS command with function code 0, and sends it to the
; fileserver to request decoding. The server returns a command code
; indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
; 5=load-as-command). This mechanism allows the fileserver to extend
; the client's command set without ROM updates. Called from the "I."
; and catch-all entries in the command match table at &8BE2, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; ***************************************************************************************
; &80b4 referenced 1 time by &809e
.forward_star_cmd
    jsr copy_filename                                                 ; 80b4: 20 4b 8d     K.            ; Copy command text to FS buffer
    tay                                                               ; 80b7: a8          .              ; Y=function code for HDRFN
.prepare_cmd_dispatch
    jsr prepare_fs_cmd                                                ; 80b8: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    ldx fs_cmd_csd                                                    ; 80bb: ae 03 0f    ...            ; X=depends on function
    beq return_1                                                      ; 80be: f0 29       .)             ; CSD handle zero: not logged in
    lda fs_cmd_data                                                   ; 80c0: ad 05 0f    ...            ; A=function code (0-7)
    ldy #&16                                                          ; 80c3: a0 16       ..             ; Y=depends on function
    bne dispatch                                                      ; 80c5: d0 13       ..             ; ALWAYS branch

; ***************************************************************************************
; FSCV dispatch entry
; 
; Entered via the extended vector table when the MOS calls FSCV.
; Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
; and dispatches codes 0-7 via the shared dispatch table at &8020
; with base offset Y=&12 (table indices 19-26).
; Function codes: 0=*OPT, 1=EOF, 2=*/, 3=unrecognised *,
; 4=*RUN, 5=*CAT, 6=shutdown, 7=read handles.
; 
; On Entry:
;     A: function code (0-7)
;     X: depends on function
;     Y: depends on function
; 
; On Exit:
;     A: depends on handler (preserved if A >= 8)
;     X: depends on handler (preserved if A >= 8)
;     Y: depends on handler (preserved if A >= 8)
; ***************************************************************************************
.fscv_handler
    jsr save_fscv_args_with_ptrs                                      ; 80c7: 20 a5 85     ..            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 80ca: c9 08       ..             ; Function code >= 8? Return (unsupported)
    bcs return_1                                                      ; 80cc: b0 1b       ..             ; Function code >= 8? Return (unsupported)
    tax                                                               ; 80ce: aa          .              ; X = function code for dispatch
    tya                                                               ; 80cf: 98          .              ; Save Y (command text ptr hi)
    ldy #&12                                                          ; 80d0: a0 12       ..             ; Y=&12: base offset for FSCV dispatch (indices 19+)
    bne dispatch                                                      ; 80d2: d0 06       ..             ; ALWAYS branch

; ***************************************************************************************
; Language entry dispatcher
; 
; Called when the NFS ROM is entered as a language. Although rom_type
; (&82) does not set the language bit, the MOS enters this point
; after NFS claims service &FE (Tube post-init). X = reason code
; (0-4). Dispatches via table indices 14-18 (base offset Y=&0D).
; ***************************************************************************************
; &80d4 referenced 1 time by &8000
.language_handler
.lang_entry_dispatch
    cpx #5                                                            ; 80d4: e0 05       ..             ; X >= 5: invalid reason code, return
.svc_dispatch_range
    bcs return_1                                                      ; 80d6: b0 11       ..             ; Out of range: return via RTS
    ldy #&0d                                                          ; 80d8: a0 0d       ..             ; Y=&0D: base offset for language handlers (index 14+)
; ***************************************************************************************
; PHA/PHA/RTS computed dispatch
; 
; X = command index within caller's group (e.g. service number)
; Y = base offset into dispatch table (0, &0D, &20, etc.)
; The loop adds Y+1 to X, so final X = command index + base + 1.
; Then high and low bytes of (handler-1) are pushed onto the stack,
; and RTS pops them and jumps to handler_address.
; 
; This is a standard 6502 trick: RTS increments the popped address
; by 1 before jumping, so the table stores (address - 1) to
; compensate. Multiple callers share one table via different Y
; base offsets.
; ***************************************************************************************
; &80da referenced 5 times by &807b, &80c5, &80d2, &80dc, &816a
.dispatch
    inx                                                               ; 80da: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80db: 88          .              ; Decrement base offset counter
    bpl dispatch                                                      ; 80dc: 10 fc       ..             ; Loop until Y exhausted
    tay                                                               ; 80de: a8          .              ; Y=&FF (no further use)
    lda dispatch_0_hi-1,x                                             ; 80df: bd 44 80    .D.            ; Load high byte of (handler - 1) from table
    pha                                                               ; 80e2: 48          H              ; Push high byte onto stack
    lda dispatch_0_lo-1,x                                             ; 80e3: bd 20 80    . .            ; Load low byte of (handler - 1) from table
    pha                                                               ; 80e6: 48          H              ; Push low byte onto stack
    ldx fs_options                                                    ; 80e7: a6 bb       ..             ; Restore X (fileserver options) for use by handler
; &80e9 referenced 7 times by &806d, &8071, &80be, &80cc, &80d6, &80f2, &80fc
.return_1
    rts                                                               ; 80e9: 60          `              ; RTS pops address, adds 1, jumps to handler

; ***************************************************************************************
; Service handler entry
; 
; Checks per-ROM disable flag at &0DF0+X (new in 3.35D). If
; bit 7 is set, returns immediately; service calls &FE/&FF
; bypass this check. Intercepts three service calls:
;   &FE: Tube init -- explode character definitions
;   &FF: Full init -- vector setup, copy code to RAM, select NFS
;   &12 (Y=5): Select NFS as active filing system
; All other service calls < &0D dispatch via c8150.
; ***************************************************************************************
; &80ea referenced 1 time by &8003
.service_handler
.service_handler_entry
    pha                                                               ; 80ea: 48          H              ; Save A (service number) on stack
    lda rom_ws_table,x                                                ; 80eb: bd f0 0d    ...            ; Load per-ROM workspace flag
    asl a                                                             ; 80ee: 0a          .              ; Test bit 7 (ROM disabled flag)
    pla                                                               ; 80ef: 68          h              ; Restore A (service number)
    bmi check_svc_high                                                ; 80f0: 30 02       0.             ; Service >= &80: always handle
    bcs return_1                                                      ; 80f2: b0 f5       ..             ; C=1 (disabled): skip this ROM
; ***************************************************************************************
; Service handler: high service dispatch
; 
; Handles service calls >= &80. Compares A against &FE:
;   &FF: Full init — jump to init_vectors_and_copy
;   &FE: Tube init — explode character definitions (if Y != 0)
;   < &FE: Fall through to check for service &12 and dispatch.
; ***************************************************************************************
; &80f4 referenced 1 time by &80f0
.check_svc_high
    cmp #&fe                                                          ; 80f4: c9 fe       ..             ; Service >= &FE?
    bcc check_svc_12                                                  ; 80f6: 90 58       .X             ; Service < &FE: skip to &12/dispatch check
    bne init_vectors_and_copy                                         ; 80f8: d0 13       ..             ; Service &FF: full init (vectors + RAM copy)
    cpy #0                                                            ; 80fa: c0 00       ..             ; Service &FE: Y=0?
    beq return_1                                                      ; 80fc: f0 eb       ..             ; Y=0: no Tube data, skip to &12 check
    stx zp_temp_11                                                    ; 80fe: 86 11       ..             ; Save ROM number across OSBYTE
    sty zp_temp_10                                                    ; 8100: 84 10       ..             ; Save Tube address across OSBYTE
    ldx #6                                                            ; 8102: a2 06       ..             ; X=6 extra pages for char definitions
    lda #osbyte_explode_chars                                         ; 8104: a9 14       ..             ; OSBYTE &14: explode character RAM
    jsr osbyte                                                        ; 8106: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
    ldx zp_temp_11                                                    ; 8109: a6 11       ..             ; Restore ROM number
    bne restore_y_check_svc                                           ; 810b: d0 3f       .?             ; Continue to vector setup
; ***************************************************************************************
; NFS initialisation (service &FF: full reset)
; 
; New in 3.35D: table-driven vector initialisation replaces
; the hardcoded LDA/STA pairs of 3.34B. Reads 4 triplets from
; the data table at &8177 (low byte, high byte, vector offset)
; and stores each 16-bit value at &0200+offset:
;   EVNTV (&0220) = &06E5   BRKV  (&0202) = &0016
;   RDCHV (&0210) = &04E7   WRCHV (&020E) = &051C
; Then writes &8E to Tube control register (&FEE0) and copies
; 3 pages of Tube host code from ROM (&935F/&945F/&955F)
; to RAM (&0400/&0500/&0600), calls tube_post_init (&0414),
; and copies 97 bytes of workspace init from ROM (&931A) to
; &0016-&0076.
; ***************************************************************************************
; &810d referenced 1 time by &80f8
.init_vectors_and_copy
    sty zp_temp_10                                                    ; 810d: 84 10       ..             ; Save Y (ROM number) for later
    ldy #&0c                                                          ; 810f: a0 0c       ..             ; Y=12: 4 triplets x 3 bytes each
; &8111 referenced 1 time by &8123
.init_vector_loop
    ldx return_2,y                                                    ; 8111: be 76 81    .v.            ; Load vector offset from table
    dey                                                               ; 8114: 88          .              ; Previous table byte
    lda return_2,y                                                    ; 8115: b9 76 81    .v.            ; Load vector high byte from table
    sta userv+1,x                                                     ; 8118: 9d 01 02    ...            ; Store high byte at &0201+X
    dey                                                               ; 811b: 88          .              ; Previous table byte
    lda return_2,y                                                    ; 811c: b9 76 81    .v.            ; Load vector low byte from table
    sta userv,x                                                       ; 811f: 9d 00 02    ...            ; Store low byte at &0200+X
    dey                                                               ; 8122: 88          .              ; Previous table byte
    bne init_vector_loop                                              ; 8123: d0 ec       ..             ; Loop for all 4 vector pairs
.init_tube_and_workspace
    lda #&8e                                                          ; 8125: a9 8e       ..             ; A=&8E: Tube control register init value
    sta tube_status_1_and_tube_control                                ; 8127: 8d e0 fe    ...            ; Write to Tube control register
; Copy NMI handler code from ROM to RAM pages &04-&06
; &812a referenced 1 time by &813d
.cloop
    lda reloc_p4_src,y                                                ; 812a: b9 5f 93    ._.            ; Load ROM byte from page &93
    sta tube_code_page4,y                                             ; 812d: 99 00 04    ...            ; Store to page &04 (Tube code)
    lda l945f,y                                                       ; 8130: b9 5f 94    ._.            ; Load ROM byte from page &94
    sta tube_dispatch_table,y                                         ; 8133: 99 00 05    ...            ; Store to page &05 (dispatch table)
    lda c955f,y                                                       ; 8136: b9 5f 95    ._.            ; Load ROM byte from page &95
    sta tube_code_page6,y                                             ; 8139: 99 00 06    ...            ; Store to page &06
    dey                                                               ; 813c: 88          .              ; DEY wraps 0 -> &FF on first iteration
    bne cloop                                                         ; 813d: d0 eb       ..             ; Loop until 256 bytes copied per page
    jsr tube_post_init                                                ; 813f: 20 14 04     ..            ; Run post-init routine in copied code
    ldx #&60 ; '`'                                                    ; 8142: a2 60       .`             ; X=&60: copy 97 bytes (&60..&00)
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &8144 referenced 1 time by &814a
.copy_nmi_workspace
    lda reloc_zp_src,x                                                ; 8144: bd 1a 93    ...            ; Load NMI workspace init byte from ROM
    sta nmi_workspace_start,x                                         ; 8147: 95 16       ..             ; Store to zero page &16+X
    dex                                                               ; 8149: ca          .              ; Next byte
    bpl copy_nmi_workspace                                            ; 814a: 10 f8       ..             ; Loop until all workspace bytes copied
; &814c referenced 1 time by &810b
.restore_y_check_svc
    ldy zp_temp_10                                                    ; 814c: a4 10       ..             ; Restore Y (ROM number)
.tube_chars_done
    lda #0                                                            ; 814e: a9 00       ..             ; A=0: fall through to service &12 check
; &8150 referenced 1 time by &80f6
.check_svc_12
    cmp #&12                                                          ; 8150: c9 12       ..             ; Is this service &12 (select FS)?
    bne not_svc_12_nfs                                                ; 8152: d0 04       ..             ; No: check if service < &0D
    cpy #5                                                            ; 8154: c0 05       ..             ; Service &12: Y=5 (NFS)?
    beq select_nfs                                                    ; 8156: f0 67       .g             ; Y=5: select NFS
; ***************************************************************************************
; Service call dispatcher
; 
; Dispatches MOS service calls 0-12 via the shared dispatch table.
; Uses base offset Y=0, so table index = service number + 1.
; Service numbers >= 13 are ignored (branch to return).
; ***************************************************************************************
; &8158 referenced 1 time by &8152
.not_svc_12_nfs
.dispatch_service
    cmp #&0d                                                          ; 8158: c9 0d       ..             ; Service >= &0D?
.svc_unhandled_return
    bcs return_2                                                      ; 815a: b0 1a       ..             ; Service >= &0D: not handled, return
.do_svc_dispatch
    tax                                                               ; 815c: aa          .              ; X = service number (dispatch index)
    lda rom_svc_num                                                   ; 815d: a5 a9       ..             ; Save &A9 (current service state)
    pha                                                               ; 815f: 48          H              ; Push saved &A9
    lda nfs_temp                                                      ; 8160: a5 a8       ..             ; Save &A8 (workspace page number)
    pha                                                               ; 8162: 48          H              ; Push saved &A8
    stx rom_svc_num                                                   ; 8163: 86 a9       ..             ; Store service number to &A9
    sty nfs_temp                                                      ; 8165: 84 a8       ..             ; Store Y (page number) to &A8
    tya                                                               ; 8167: 98          .              ; A = Y for dispatch table offset
    ldy #0                                                            ; 8168: a0 00       ..             ; Y=0: base offset for service dispatch
    jsr dispatch                                                      ; 816a: 20 da 80     ..            ; JSR to dispatcher (returns here after handler completes)
    ldx rom_svc_num                                                   ; 816d: a6 a9       ..             ; Recover service claim status from &A9
    pla                                                               ; 816f: 68          h              ; Restore saved &A8 from stack
    sta nfs_temp                                                      ; 8170: 85 a8       ..             ; Write back &A8
; ***************************************************************************************
; Service dispatch epilogue
; 
; Common return path for all dispatched service handlers.
; Restores rom_svc_num from the stack (pushed by dispatch_service),
; transfers X (ROM number) to A, then returns via RTS.
; ***************************************************************************************
.svc_dispatch_epilogue
    pla                                                               ; 8172: 68          h              ; Restore saved A from service dispatch
    sta rom_svc_num                                                   ; 8173: 85 a9       ..             ; Save to workspace &A9
    txa                                                               ; 8175: 8a          .              ; Return ROM number in A
; &8176 referenced 4 times by &8111, &8115, &811c, &815a
.return_2
    rts                                                               ; 8176: 60          `              ; Return (not our command)

    equb &1c, 5, &0e, &e7, 4, &10, &16, 0, 2, &e5, 6, &20             ; 8177: 1c 05 0e... ...

.svc_4_star_command
    ldx #8                                                            ; 8183: a2 08       ..             ; X=8: compare 8 chars for *ROFF
    jsr match_rom_string                                              ; 8185: 20 d6 81     ..            ; Try matching *ROFF command
    bne match_net_cmd                                                 ; 8188: d0 2e       ..             ; No match: try *NET
; ***************************************************************************************
; Resume after remote operation / *ROFF handler (NROFF)
; 
; Checks byte 4 of (net_rx_ptr): if non-zero, the keyboard was
; disabled during a remote operation (peek/poke/boot). Clears
; the flag, re-enables the keyboard via OSBYTE &C9, and sends
; function &0A to notify completion. Also handles *ROFF and the
; triple-plus escape sequence (+++), which resets system masks
; via OSBYTE &CE and returns control to the MOS, providing an
; escape route when a remote session becomes unresponsive.
; ***************************************************************************************
.net_4_resume_remote
    ldy #4                                                            ; 818a: a0 04       ..             ; Y=4: offset of keyboard disable flag
    lda (net_rx_ptr),y                                                ; 818c: b1 9c       ..             ; Read flag from RX buffer
    beq skip_kbd_reenable                                             ; 818e: f0 21       .!             ; Zero: keyboard not disabled, skip
    lda #0                                                            ; 8190: a9 00       ..             ; A=0: value to clear flag and re-enable
    tax                                                               ; 8192: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 8193: 91 9c       ..             ; Clear keyboard disable flag in buffer
    tay                                                               ; 8195: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 8196: a9 c9       ..             ; OSBYTE &C9: Econet keyboard disable
    jsr osbyte                                                        ; 8198: 20 f4 ff     ..            ; Re-enable keyboard (X=0, Y=0); Enable keyboard (for Econet)
    lda #&0a                                                          ; 819b: a9 0a       ..             ; Function &0A: remote operation complete
    jsr setup_tx_and_send                                             ; 819d: 20 c0 90     ..            ; Send notification to controlling station
; &81a0 referenced 1 time by &8496
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 81a0: 86 9e       ..             ; Save X (return value from TX)
    lda #&ce                                                          ; 81a2: a9 ce       ..             ; OSBYTE &CE: first system mask to reset
; &81a4 referenced 1 time by &81af
.clear_osbyte_masks
    ldx nfs_workspace                                                 ; 81a4: a6 9e       ..             ; Restore X for OSBYTE call
    ldy #&7f                                                          ; 81a6: a0 7f       ..             ; Y=&7F: AND mask (clear bit 7)
    jsr osbyte                                                        ; 81a8: 20 f4 ff     ..            ; Reset system mask byte
    adc #1                                                            ; 81ab: 69 01       i.             ; Advance to next OSBYTE (&CE -> &CF)
    cmp #&d0                                                          ; 81ad: c9 d0       ..             ; Reached &D0? (past &CF)
    beq clear_osbyte_masks                                            ; 81af: f0 f3       ..             ; No: reset &CF too
; &81b1 referenced 1 time by &818e
.skip_kbd_reenable
    lda #0                                                            ; 81b1: a9 00       ..             ; A=0: clear remote state
    sta rom_svc_num                                                   ; 81b3: 85 a9       ..             ; Clear &A9 (service dispatch state)
    sta nfs_workspace                                                 ; 81b5: 85 9e       ..             ; Clear workspace byte
    rts                                                               ; 81b7: 60          `              ; Return

; &81b8 referenced 1 time by &8188
.match_net_cmd
    ldx #1                                                            ; 81b8: a2 01       ..             ; X=1: ROM offset for "NET" match
    jsr match_rom_string                                              ; 81ba: 20 d6 81     ..            ; Try matching *NET command
    bne restore_y_return                                              ; 81bd: d0 46       .F             ; No match: return unclaimed
; ***************************************************************************************
; Select NFS as active filing system (INIT)
; 
; Reached from service &12 (select FS) with Y=5, or when *NET command
; selects NFS. Notifies the current FS of shutdown via FSCV A=6 —
; this triggers the outgoing FS to save its context back to its
; workspace page, allowing restoration if re-selected later (the
; FSDIE handoff mechanism). Then sets up the standard OS vector
; indirections (FILEV through FSCV) to NFS entry points, claims the
; extended vector table entries, and issues service &0F (vectors
; claimed) to notify other ROMs. If fs_temp_cd is zero (auto-boot
; not inhibited), injects the synthetic command "I .BOOT" through
; the command decoder to trigger auto-boot login.
; ***************************************************************************************
; &81bf referenced 1 time by &8156
.select_nfs
    jsr call_fscv_shutdown                                            ; 81bf: 20 08 82     ..            ; Notify current FS of shutdown (FSCV A=6)
    sec                                                               ; 81c2: 38          8              ; C=1 for ROR
    ror nfs_temp                                                      ; 81c3: 66 a8       f.             ; Set bit 7 of l00a8 (inhibit auto-boot)
    jsr issue_vectors_claimed                                         ; 81c5: 20 6b 82     k.            ; Claim OS vectors, issue service &0F
    ldy #&1d                                                          ; 81c8: a0 1d       ..             ; Y=&1D: top of FS state range
; &81ca referenced 1 time by &81d2
.initl
    lda (net_rx_ptr),y                                                ; 81ca: b1 9c       ..             ; Copy FS state from RX buffer...
    sta fs_state_deb,y                                                ; 81cc: 99 eb 0d    ...            ; ...to workspace (offsets &15-&1D)
    dey                                                               ; 81cf: 88          .              ; Next byte (descending)
    cpy #&14                                                          ; 81d0: c0 14       ..             ; Loop until offset &14 done
    bne initl                                                         ; 81d2: d0 f6       ..             ; Continue loop
    beq init_fs_vectors                                               ; 81d4: f0 7e       .~             ; ALWAYS branch to init_fs_vectors; ALWAYS branch

; ***************************************************************************************
; Match command text against ROM string table
; 
; Compares characters from (os_text_ptr)+Y against bytes starting
; at binary_version+X (&8008+X). Input is uppercased via AND &DF.
; Returns with Z=1 if the ROM string's NUL terminator was reached
; (match), or Z=0 if a mismatch was found. On match, Y points
; past the matched text; on return, skips trailing spaces.
; ***************************************************************************************
; &81d6 referenced 2 times by &8185, &81ba
.match_rom_string
    ldy nfs_temp                                                      ; 81d6: a4 a8       ..             ; Y = saved text pointer offset
; &81d8 referenced 1 time by &81e5
.match_next_char
    lda (os_text_ptr),y                                               ; 81d8: b1 f2       ..             ; Load next input character
    and #&df                                                          ; 81da: 29 df       ).             ; Force uppercase (clear bit 5)
    beq cmd_name_matched                                              ; 81dc: f0 09       ..             ; Input char is NUL/space: check ROM byte
    cmp binary_version,x                                              ; 81de: dd 08 80    ...            ; Compare with ROM string byte
    bne cmd_name_matched                                              ; 81e1: d0 04       ..             ; Mismatch: check if ROM string ended
    iny                                                               ; 81e3: c8          .              ; Advance input pointer
    inx                                                               ; 81e4: e8          .              ; Advance ROM string pointer
    bne match_next_char                                               ; 81e5: d0 f1       ..             ; Continue matching (always taken)
; &81e7 referenced 2 times by &81dc, &81e1
.cmd_name_matched
    lda binary_version,x                                              ; 81e7: bd 08 80    ...            ; Load ROM string byte at match point
    beq skip_cmd_spaces                                               ; 81ea: f0 02       ..             ; Zero = end of ROM string = full match
    rts                                                               ; 81ec: 60          `              ; Non-zero = partial/no match; Z=0

; &81ed referenced 1 time by &81f2
.skpspi
    iny                                                               ; 81ed: c8          .              ; Skip this space
; &81ee referenced 1 time by &81ea
.skip_cmd_spaces
    lda (os_text_ptr),y                                               ; 81ee: b1 f2       ..             ; Load next input character
    cmp #&20 ; ' '                                                    ; 81f0: c9 20       .              ; Is it a space?
    beq skpspi                                                        ; 81f2: f0 f9       ..             ; Yes: keep skipping
    eor #&0d                                                          ; 81f4: 49 0d       I.             ; XOR with CR: Z=1 if end of line
    rts                                                               ; 81f6: 60          `              ; Return (not our service call)

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_9_help
    jsr print_inline                                                  ; 81f7: 20 e2 85     ..            ; Print inline ROM identification string
    equs &0d, "NFS 3.35d", &0d                                        ; 81fa: 0d 4e 46... .NF

; &8205 referenced 2 times by &81bd, &821a
.restore_y_return
    ldy nfs_temp                                                      ; 8205: a4 a8       ..             ; Reload saved character counter
    rts                                                               ; 8207: 60          `              ; Return (service not claimed)

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &8208 referenced 2 times by &81bf, &820d
.call_fscv_shutdown
    lda #6                                                            ; 8208: a9 06       ..             ; FSCV reason 6 = FS shutdown
    jmp (fscv)                                                        ; 820a: 6c 1e 02    l..            ; Tail-call via filing system control vector

; ***************************************************************************************
; Service 3: auto-boot
; 
; Notifies current FS of shutdown via FSCV A=6. Scans keyboard
; (OSBYTE &7A): if no key is pressed, auto-boot proceeds directly
; via print_station_info. If a key is pressed, falls through to
; check_boot_key: the 'N' key (matrix address &55) proceeds with
; auto-boot, any other key causes the auto-boot to be declined.
; ***************************************************************************************
.svc_3_autoboot
    jsr call_fscv_shutdown                                            ; 820d: 20 08 82     ..            ; Notify current FS of shutdown
    lda #osbyte_scan_keyboard_from_16                                 ; 8210: a9 7a       .z             ; OSBYTE &7A: scan keyboard
    jsr osbyte                                                        ; 8212: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 8215: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi print_station_info                                            ; 8216: 30 0a       0.             ; No key pressed: proceed with auto-boot
; ***************************************************************************************
; Check boot key
; 
; Checks if the pressed key (in A) is 'N' (matrix address &55). If
; not 'N', returns to the MOS without claiming the service call
; (another ROM may boot instead). If 'N', forgets the keypress via
; OSBYTE &78 and falls through to print_station_info.
; ***************************************************************************************
.check_boot_key
    eor #&55 ; 'U'                                                    ; 8218: 49 55       IU             ; XOR with &55: result=0 if key is 'N'
    bne restore_y_return                                              ; 821a: d0 e9       ..             ; Not 'N': return without claiming
    tay                                                               ; 821c: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 821d: a9 78       .x             ; OSBYTE &78: clear key-pressed state
    jsr osbyte                                                        ; 821f: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; ***************************************************************************************
; Print station identification
; 
; Prints "Econet Station <n>" using the station number from the net
; receive buffer, then tests ADLC SR2 for the network clock signal —
; prints " No Clock" if absent. Falls through to init_fs_vectors.
; ***************************************************************************************
; &8222 referenced 1 time by &8216
.print_station_info
    jsr print_inline                                                  ; 8222: 20 e2 85     ..            ; Print 'Econet Station ' banner
    equs "Econet Station "                                            ; 8225: 45 63 6f... Eco

    ldy #&14                                                          ; 8234: a0 14       ..             ; Y=&14: offset for station number
    lda (net_rx_ptr),y                                                ; 8236: b1 9c       ..             ; Load station number
    jsr print_decimal                                                 ; 8238: 20 86 8d     ..            ; Print as 3-digit decimal
    lda #&20 ; ' '                                                    ; 823b: a9 20       .              ; BIT trick: bit 5 of SR2 = clock present
    bit econet_control23_or_status2                                   ; 823d: 2c a1 fe    ,..            ; Test DCD: clock present if bit 5 clear
.dofsl1
    beq skip_no_clock_msg                                             ; 8240: f0 0d       ..             ; Clock present: skip warning
    jsr print_inline                                                  ; 8242: 20 e2 85     ..            ; Print ' No Clock' warning
    equs " No Clock"                                                  ; 8245: 20 4e 6f...  No

    nop                                                               ; 824e: ea          .              ; NOP (padding after inline string)
; &824f referenced 1 time by &8240
.skip_no_clock_msg
    jsr print_inline                                                  ; 824f: 20 e2 85     ..            ; Print two CRs (blank line)
    equs &0d, &0d                                                     ; 8252: 0d 0d       ..

; ***************************************************************************************
; Initialise filing system vectors
; 
; Copies 14 bytes from fs_vector_addrs (&828A) into FILEV-FSCV (&0212),
; setting all 7 filing system vectors to the extended vector dispatch
; addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
; ROM pointer table entries with the actual NFS handler addresses. Also
; reached directly from select_nfs, bypassing the station display.
; Falls through to issue_vectors_claimed.
; ***************************************************************************************
; &8254 referenced 1 time by &81d4
.init_fs_vectors
    ldy #&0d                                                          ; 8254: a0 0d       ..             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
; &8256 referenced 1 time by &825d
.init_vector_copy_loop
    lda fs_vector_addrs,y                                             ; 8256: b9 8a 82    ...            ; Load vector address from table
    sta filev,y                                                       ; 8259: 99 12 02    ...            ; Write to FILEV-FSCV vector table
    dey                                                               ; 825c: 88          .              ; Next byte (descending)
    bpl init_vector_copy_loop                                         ; 825d: 10 f7       ..             ; Loop until all 14 bytes copied
    jsr setup_rom_ptrs_netv                                           ; 825f: 20 15 83     ..            ; Read ROM ptr table addr, install NETV
    ldy #&1b                                                          ; 8262: a0 1b       ..             ; Install 7 handler entries in ROM ptr table
    ldx #7                                                            ; 8264: a2 07       ..             ; 7 FS vectors to install
    jsr store_rom_ptr_pair                                            ; 8266: 20 29 83     ).            ; Install each 3-byte vector entry
    stx rom_svc_num                                                   ; 8269: 86 a9       ..             ; X=0 after loop; store as workspace offset
; ***************************************************************************************
; Issue 'vectors claimed' service and optionally auto-boot
; 
; Issues service &0F (vectors claimed) via OSBYTE &8F, then
; service &0A. If fs_temp_cd is zero (auto-boot not inhibited),
; sets up the command string "I .BOOT" at &8282 and jumps to
; the FSCV 3 unrecognised-command handler (which matches against
; the command table at &8BE2). The "I." prefix triggers the
; catch-all entry which forwards the command to the fileserver.
; Falls through to run_fscv_cmd.
; ***************************************************************************************
; &826b referenced 1 time by &81c5
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 826b: a9 8f       ..             ; A=&8F: issue service request
    ldx #&0f                                                          ; 826d: a2 0f       ..             ; X=&0F: 'vectors claimed' service
    jsr osbyte                                                        ; 826f: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 8272: a2 0a       ..             ; X=&0A: service &0A
    jsr osbyte                                                        ; 8274: 20 f4 ff     ..            ; Issue service &0A
    ldx nfs_temp                                                      ; 8277: a6 a8       ..             ; Non-zero after hard reset: skip auto-boot
    bne return_3                                                      ; 8279: d0 37       .7             ; Non-zero: skip auto-boot
    ldx #&82                                                          ; 827b: a2 82       ..             ; X = lo byte of auto-boot string at &8292
; ***************************************************************************************
; Run FSCV command from ROM
; 
; Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
; to execute the command string at (X, Y). X is pre-loaded by the
; caller with the low byte of the string address. Also used as a
; data base address by store_rom_ptr_pair for Y-indexed access to
; the handler address table.
; ***************************************************************************************
; &827d referenced 2 times by &8329, &832f
.run_fscv_cmd
    ldy #&82                                                          ; 827d: a0 82       ..             ; Y=&82: ROM page high byte
    jmp fscv_3_star_cmd                                               ; 827f: 4c b4 8b    L..            ; Execute command string at (X, Y)

; Synthetic auto-boot command string. "I " does not match any
; entry in NFS's local command table — "I." requires a dot, and
; "I AM" requires 'A' after the space — so fscv_3_star_cmd
; forwards the entire string to the fileserver, which executes
; the .BOOT file.
    equs "I .BOOT", &0d                                               ; 8282: 49 20 2e... I .            ; Auto-boot string tail / NETV handler data
; ***************************************************************************************
; FS vector dispatch and handler addresses (34 bytes)
; 
; Bytes 0-13: extended vector dispatch addresses, copied to
; FILEV-FSCV (&0212) by init_fs_vectors. Each 2-byte pair is
; a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
; the handler in the ROM pointer table.
; 
; Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
; Each entry has addr_lo, addr_hi, then a padding byte that is
; not read at runtime (store_rom_ptr_pair writes the current ROM
; bank number without reading). The last entry (FSCV) has no
; padding byte.
; ***************************************************************************************
; &828a referenced 1 time by &8256
.fs_vector_addrs
    equb &1b                                                          ; 828a: 1b          .              ; FILEV dispatch lo
    equb &ff                                                          ; 828b: ff          .              ; FILEV dispatch hi
    equb &1e                                                          ; 828c: 1e          .              ; ARGSV dispatch lo
    equb &ff                                                          ; 828d: ff          .              ; ARGSV dispatch hi
    equb &21                                                          ; 828e: 21          !              ; BGETV dispatch lo
    equb &ff                                                          ; 828f: ff          .              ; BGETV dispatch hi
    equb &24                                                          ; 8290: 24          $              ; BPUTV dispatch lo
    equb &ff                                                          ; 8291: ff          .              ; BPUTV dispatch hi
    equb &27                                                          ; 8292: 27          '              ; GBPBV dispatch lo
    equb &ff                                                          ; 8293: ff          .              ; GBPBV dispatch hi
    equb &2a                                                          ; 8294: 2a          *              ; FINDV dispatch lo
    equb &ff                                                          ; 8295: ff          .              ; FINDV dispatch hi
    equb &2d                                                          ; 8296: 2d          -              ; FSCV dispatch lo
    equb &ff                                                          ; 8297: ff          .              ; FSCV dispatch hi
    equb &e7                                                          ; 8298: e7          .              ; FILEV handler lo (&86E7)
    equb &86                                                          ; 8299: 86          .              ; FILEV handler hi
    equb &4a                                                          ; 829a: 4a          J              ; (ROM bank — not read)
    equb &0c                                                          ; 829b: 0c          .              ; ARGSV handler lo (&890C)
    equb &89                                                          ; 829c: 89          .              ; ARGSV handler hi
    equb &44                                                          ; 829d: 44          D              ; (ROM bank — not read)
    equb &39                                                          ; 829e: 39          9              ; BGETV handler lo (&8539)
    equb &85                                                          ; 829f: 85          .              ; BGETV handler hi
    equb &57                                                          ; 82a0: 57          W              ; (ROM bank — not read)
    equb &ec                                                          ; 82a1: ec          .              ; BPUTV handler lo (&83EC)
    equb &83                                                          ; 82a2: 83          .              ; BPUTV handler hi
    equb &42                                                          ; 82a3: 42          B              ; (ROM bank — not read)
    equb &10                                                          ; 82a4: 10          .              ; GBPBV handler lo (&8A10)
    equb &8a                                                          ; 82a5: 8a          .              ; GBPBV handler hi
    equb &41                                                          ; 82a6: 41          A              ; (ROM bank — not read)
    equb &78                                                          ; 82a7: 78          x              ; FINDV handler lo (&8978)
    equb &89                                                          ; 82a8: 89          .              ; FINDV handler hi
    equb &52                                                          ; 82a9: 52          R              ; (ROM bank — not read)
    equb &c7                                                          ; 82aa: c7          .              ; FSCV handler lo (&80C7)
    equb &80                                                          ; 82ab: 80          .              ; FSCV handler hi

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; ***************************************************************************************
.svc_1_abs_workspace
    cpy #&10                                                          ; 82ac: c0 10       ..             ; Already at page &10 or above?
    bcs return_3                                                      ; 82ae: b0 02       ..             ; Yes: nothing to claim
    ldy #&10                                                          ; 82b0: a0 10       ..             ; Claim pages &0D-&0F (3 pages)
; &82b2 referenced 2 times by &8279, &82ae
.return_3
    rts                                                               ; 82b2: 60          `              ; Return (workspace claim done)

    equb &7c, &90                                                     ; 82b3: 7c 90       |.

; ***************************************************************************************
; Service 2: claim private workspace and initialise NFS
; 
; Y = next available workspace page on entry.
; Sets up net_rx_ptr (Y) and nfs_workspace (Y+1) page pointers.
; On soft break (OSBYTE &FD returns 0): skips FS state init,
; preserving existing login state, file server selection, and
; control block configuration — this is why pressing BREAK
; keeps the user logged in.
; On power-up/CTRL-BREAK (result non-zero):
;   - Sets FS server station to &FE (FS, the default; no server)
;   - Sets printer server to &EB (PS, the default)
;   - Clears FS handles, OPT byte, message flag, SEQNOS
;   - Initialises all RXCBs with &3F flag (available)
; In both cases: reads station ID from &FE18 (only valid during
; reset), calls adlc_init, enables user-level RX (LFLAG=&40).
; ***************************************************************************************
.svc_2_private_workspace
    sty net_rx_ptr_hi                                                 ; 82b5: 84 9d       ..             ; Store page as RX buffer high byte
    iny                                                               ; 82b7: c8          .              ; Next page for NFS workspace
    sty nfs_workspace_hi                                              ; 82b8: 84 9f       ..             ; Store page as NFS workspace high
    lda #0                                                            ; 82ba: a9 00       ..             ; A=0 for clearing workspace
    ldy #4                                                            ; 82bc: a0 04       ..             ; Y=4: remote status offset
    sta (net_rx_ptr),y                                                ; 82be: 91 9c       ..             ; Clear status byte in net receive buffer
    ldy #&ff                                                          ; 82c0: a0 ff       ..             ; Y=&FF: used for later iteration
    sta net_rx_ptr                                                    ; 82c2: 85 9c       ..             ; Clear RX ptr low byte
    sta nfs_workspace                                                 ; 82c4: 85 9e       ..             ; Clear workspace ptr low byte
    sta nfs_temp                                                      ; 82c6: 85 a8       ..             ; Clear RXCB iteration counter
    sta tx_clear_flag                                                 ; 82c8: 8d 62 0d    .b.            ; Clear TX semaphore (no TX in progress)
    tax                                                               ; 82cb: aa          .              ; X=0 for OSBYTE; X=&00
    lda #osbyte_read_write_last_break_type                            ; 82cc: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 82ce: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 82d1: 8a          .              ; X = break type from OSBYTE result; X=value of type of last reset
    beq read_station_id                                               ; 82d2: f0 32       .2             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 82d4: a0 15       ..             ; Y=&15: printer station offset in RX buffer
    lda #&fe                                                          ; 82d6: a9 fe       ..             ; &FE = no server selected
    sta fs_server_stn                                                 ; 82d8: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 82db: 91 9c       ..             ; Store &FE at printer station offset
    lda #0                                                            ; 82dd: a9 00       ..             ; A=0 for clearing workspace fields
    sta fs_server_net                                                 ; 82df: 8d 01 0e    ...            ; Clear network number
    sta prot_status                                                   ; 82e2: 8d 63 0d    .c.            ; Clear protection status
    sta fs_messages_flag                                              ; 82e5: 8d 06 0e    ...            ; Clear message flag
    sta fs_boot_option                                                ; 82e8: 8d 05 0e    ...            ; Clear boot option
    iny                                                               ; 82eb: c8          .              ; Y=&16
    sta (net_rx_ptr),y                                                ; 82ec: 91 9c       ..             ; Clear net number at RX buffer offset &16
    ldy #3                                                            ; 82ee: a0 03       ..             ; Init printer server: station &FE, net 0
    sta (nfs_workspace),y                                             ; 82f0: 91 9e       ..             ; Store net 0 at workspace offset 3
    dey                                                               ; 82f2: 88          .              ; Y=2: printer station offset; Y=&02
    lda #&eb                                                          ; 82f3: a9 eb       ..             ; &FE = no printer server
    sta (nfs_workspace),y                                             ; 82f5: 91 9e       ..             ; Store &FE at printer station in workspace
; &82f7 referenced 1 time by &8304
.init_rxcb_entries
    lda nfs_temp                                                      ; 82f7: a5 a8       ..             ; Load RXCB counter
    jsr calc_handle_offset                                            ; 82f9: 20 4c 8e     L.            ; Convert to workspace byte offset
    bcs read_station_id                                               ; 82fc: b0 08       ..             ; C=1: past max handles, done
    lda #&3f ; '?'                                                    ; 82fe: a9 3f       .?             ; Mark RXCB as available
    sta (nfs_workspace),y                                             ; 8300: 91 9e       ..             ; Write &3F flag to workspace
    inc nfs_temp                                                      ; 8302: e6 a8       ..             ; Next RXCB number
    bne init_rxcb_entries                                             ; 8304: d0 f1       ..             ; Loop for all RXCBs
; &8306 referenced 2 times by &82d2, &82fc
.read_station_id
    lda station_id_disable_net_nmis                                   ; 8306: ad 18 fe    ...            ; Read station ID (also INTOFF)
    ldy #&14                                                          ; 8309: a0 14       ..             ; Y=&14: station ID offset in RX buffer
    sta (net_rx_ptr),y                                                ; 830b: 91 9c       ..             ; Store our station number
    jsr trampoline_adlc_init                                          ; 830d: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 8310: a9 40       .@             ; Enable user-level RX (LFLAG=&40)
    sta rx_flags                                                      ; 8312: 8d 64 0d    .d.            ; Store to rx_flags
; ***************************************************************************************
; Set up ROM pointer table and NETV
; 
; Reads the ROM pointer table base address via OSBYTE &A8, stores
; it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
; one 3-byte extended vector entry (addr=&9008, rom=current) into
; the ROM pointer table at offset &36, installing osword_dispatch
; as the NETV handler.
; ***************************************************************************************
; &8315 referenced 1 time by &825f
.setup_rom_ptrs_netv
    lda #osbyte_read_rom_ptr_table_low                                ; 8315: a9 a8       ..             ; OSBYTE &A8: read ROM pointer table address
    ldx #0                                                            ; 8317: a2 00       ..             ; X=0: read low byte
    ldy #&ff                                                          ; 8319: a0 ff       ..             ; Y=&FF: read high byte
    jsr osbyte                                                        ; 831b: 20 f4 ff     ..            ; Returns table address in X (lo) Y (hi); Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 831e: 86 f6       ..             ; Store table base address low byte; X=value of address of ROM pointer table (low byte)
    sty osrdsc_ptr_hi                                                 ; 8320: 84 f7       ..             ; Store table base address high byte; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 8322: a0 36       .6             ; NETV extended vector offset in ROM ptr table
    sty netv                                                          ; 8324: 8c 24 02    .$.            ; Set NETV low byte = &36 (vector dispatch)
    ldx #1                                                            ; 8327: a2 01       ..             ; Install 1 entry (NETV) in ROM ptr table
; &8329 referenced 2 times by &8266, &833b
.store_rom_ptr_pair
    lda run_fscv_cmd,y                                                ; 8329: b9 7d 82    .}.            ; Load handler address low byte from table
    sta (osrdsc_ptr),y                                                ; 832c: 91 f6       ..             ; Store to ROM pointer table
    iny                                                               ; 832e: c8          .              ; Next byte
    lda run_fscv_cmd,y                                                ; 832f: b9 7d 82    .}.            ; Load handler address high byte from table
    sta (osrdsc_ptr),y                                                ; 8332: 91 f6       ..             ; Store to ROM pointer table
    iny                                                               ; 8334: c8          .              ; Next byte
    lda romsel_copy                                                   ; 8335: a5 f4       ..             ; Write current ROM bank number
    sta (osrdsc_ptr),y                                                ; 8337: 91 f6       ..             ; Store ROM number to ROM pointer table
    iny                                                               ; 8339: c8          .              ; Advance to next entry position
    dex                                                               ; 833a: ca          .              ; Count down entries
    bne store_rom_ptr_pair                                            ; 833b: d0 ec       ..             ; Loop until all entries installed
    ldy nfs_workspace_hi                                              ; 833d: a4 9f       ..             ; Y = workspace high byte + 1 = next free page
    iny                                                               ; 833f: c8          .              ; Advance past workspace page
    rts                                                               ; 8340: 60          `              ; Return; Y = page after NFS workspace

; ***************************************************************************************
; FSCV 6: Filing system shutdown / save state (FSDIE)
; 
; Called when another filing system (e.g. DFS) is selected. Saves
; the current NFS context (FSLOCN station number, URD/CSD/LIB
; handles, OPT byte, etc.) from page &0E into the dynamic workspace
; backup area. This allows the state to be restored when *NET is
; re-issued later, without losing the login session. Finally calls
; OSBYTE &7B (printer driver going dormant) to release the
; Econet network printer on FS switch.
; ***************************************************************************************
.fscv_6_shutdown
    ldy #&1d                                                          ; 8341: a0 1d       ..             ; Copy 10 bytes: FS state to workspace backup
; &8343 referenced 1 time by &834b
.fsdiel
    lda fs_state_deb,y                                                ; 8343: b9 eb 0d    ...            ; Load FS state byte at offset Y
    sta (net_rx_ptr),y                                                ; 8346: 91 9c       ..             ; Store to workspace backup area
    dey                                                               ; 8348: 88          .              ; Next byte down
    cpy #&14                                                          ; 8349: c0 14       ..             ; Offsets &15-&1D: server, handles, OPT, etc.
    bne fsdiel                                                        ; 834b: d0 f6       ..             ; Loop for offsets &1D..&15
    lda #osbyte_printer_driver_going_dormant                          ; 834d: a9 7b       .{             ; A=&7B: printer driver going dormant
    jmp osbyte                                                        ; 834f: 4c f4 ff    L..            ; Printer driver going dormant

; ***************************************************************************************
; Initialise TX control block for FS reply on port &90
; 
; Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
; up the TX control block, stores the port and control bytes, then
; decrements the control flag. Used by send_fs_reply_cmd to prepare
; for receiving the fileserver's reply.
; ***************************************************************************************
; &8352 referenced 1 time by &83cb
.init_tx_reply_port
    lda #&90                                                          ; 8352: a9 90       ..             ; A=&90: FS reply port (PREPLY)
; &8354 referenced 1 time by &8840
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8354: 20 60 83     `.            ; Init TXCB from template
    sta txcb_port                                                     ; 8357: 85 c1       ..             ; Store port number in TXCB
    lda #3                                                            ; 8359: a9 03       ..             ; Control byte: 3 = transmit
    sta txcb_start                                                    ; 835b: 85 c4       ..             ; Store control byte in TXCB
    dec txcb_ctrl                                                     ; 835d: c6 c0       ..             ; Decrement TXCB flag to arm TX
    rts                                                               ; 835f: 60          `              ; Return after port setup

; ***************************************************************************************
; Initialise TX control block at &00C0 from template
; 
; Copies 12 bytes from tx_ctrl_template (&8335) to &00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from &0E00/&0E01 to &00C2/&00C3.
; The template sets up: control=&80, port=&99 (FS command port),
; command data length=&0F, plus padding bytes.
; ***************************************************************************************
; &8360 referenced 4 times by &8354, &83b4, &8405, &8ff3
.init_tx_ctrl_block
    pha                                                               ; 8360: 48          H              ; Preserve A across call
    ldy #&0b                                                          ; 8361: a0 0b       ..             ; Copy 12 bytes (Y=11..0)
; &8363 referenced 1 time by &8374
.fstxl1
    lda tx_ctrl_template,y                                            ; 8363: b9 78 83    .x.            ; Load template byte
    sta txcb_ctrl,y                                                   ; 8366: 99 c0 00    ...            ; Store to TX control block at &00C0
    cpy #2                                                            ; 8369: c0 02       ..             ; Y < 2: also copy FS server station/network
    bpl fstxl2                                                        ; 836b: 10 06       ..             ; Skip station/network copy for Y >= 2
    lda fs_server_stn,y                                               ; 836d: b9 00 0e    ...            ; Load FS server station (Y=0) or network (Y=1)
    sta txcb_dest,y                                                   ; 8370: 99 c2 00    ...            ; Store to dest station/network at &00C2
; &8373 referenced 1 time by &836b
.fstxl2
    dey                                                               ; 8373: 88          .              ; Next byte (descending)
    bpl fstxl1                                                        ; 8374: 10 ed       ..             ; Loop until all 12 bytes copied
    pla                                                               ; 8376: 68          h              ; Restore A
    rts                                                               ; 8377: 60          `              ; Return

; ***************************************************************************************
; TX control block template (TXTAB, 12 bytes)
; 
; 12-byte template copied to &00C0 by init_tx_ctrl. Defines the
; TX control block for FS commands: control flag, port, station/
; network, and data buffer pointers (&0F00-&0FFF). The 4-byte
; Econet addresses use only the low 2 bytes; upper bytes are &FF.
; ***************************************************************************************
; &8378 referenced 1 time by &8363
.tx_ctrl_template
    equb &80                                                          ; 8378: 80          .              ; Control flag
    equb &99                                                          ; 8379: 99          .              ; Port (FS command = &99)
    equb 0                                                            ; 837a: 00          .              ; Station (filled at runtime)
    equb 0                                                            ; 837b: 00          .              ; Network (filled at runtime)
    equb 0                                                            ; 837c: 00          .              ; Buffer start low
    equb &0f                                                          ; 837d: 0f          .              ; Buffer start high (page &0F)
; &837e referenced 3 times by &88c0, &899b, &9171
.tx_ctrl_upper
    equb &ff                                                          ; 837e: ff          .              ; Buffer start pad (4-byte Econet addr)
    equb &ff                                                          ; 837f: ff          .              ; Buffer start pad
    equb &ff                                                          ; 8380: ff          .              ; Buffer end low
    equb &0f                                                          ; 8381: 0f          .              ; Buffer end high (page &0F)
    equb &ff                                                          ; 8382: ff          .              ; Buffer end pad
    equb &ff                                                          ; 8383: ff          .              ; Buffer end pad

; ***************************************************************************************
; Prepare FS command with carry set
; 
; Alternate entry to prepare_fs_cmd that pushes A, loads &2A
; into fs_error_ptr, and enters with carry set (SEC). The carry
; flag is later tested by build_send_fs_cmd to select the
; byte-stream (BSXMIT) transmission path.
; ***************************************************************************************
; &8384 referenced 1 time by &8a61
.prepare_cmd_with_flag
    pha                                                               ; 8384: 48          H              ; Save flag byte for command
    lda #&2a ; '*'                                                    ; 8385: a9 2a       .*             ; A=&2A: error ptr for retry
    sec                                                               ; 8387: 38          8              ; C=1: include flag in FS command
    bcs store_fs_hdr_fn                                               ; 8388: b0 14       ..             ; ALWAYS branch to prepare_fs_cmd; ALWAYS branch

; &838a referenced 2 times by &8704, &87ad
.prepare_cmd_clv
    clv                                                               ; 838a: b8          .              ; V=0: command has no flag byte
    bvc store_fs_hdr_clc                                              ; 838b: 50 10       P.             ; ALWAYS branch to prepare_fs_cmd; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8BE2 for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 838d: a9 77       .w             ; A=&77: OSBYTE close spool/exec
    jsr osbyte                                                        ; 838f: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #&17                                                          ; 8392: a0 17       ..             ; Y=function code for HDRFN
; ***************************************************************************************
; Prepare FS command buffer (12 references)
; 
; Builds the 5-byte FS protocol header at &0F00:
;   &0F00 HDRREP = reply port (set downstream, typically &90/PREPLY)
;   &0F01 HDRFN  = Y parameter (function code)
;   &0F02 HDRURD = URD handle (from &0E02)
;   &0F03 HDRCSD = CSD handle (from &0E03)
;   &0F04 HDRLIB = LIB handle (from &0E04)
; Command-specific data follows at &0F05 (TXBUF). Also clears V flag.
; Called before building specific FS commands for transmission.
; 
; On Entry:
;     Y: function code for HDRFN
;     X: preserved through header build
; 
; On Exit:
;     A: 0 on success (from build_send_fs_cmd)
;     X: 0 on success, &D6 on not-found
;     Y: 1 (offset past command code in reply)
; ***************************************************************************************
; &8394 referenced 12 times by &80b8, &8865, &88db, &8927, &894e, &89c1, &89e6, &8abc, &8b72, &8c1b, &8c52, &8cbf
.prepare_fs_cmd
    clv                                                               ; 8394: b8          .              ; V=0: standard FS command path
; &8395 referenced 2 times by &88c3, &899e
.init_tx_ctrl_data
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 8395: ad 02 0e    ...            ; Copy URD handle from workspace to buffer
    sta fs_cmd_urd                                                    ; 8398: 8d 02 0f    ...            ; Store URD at &0F02
    lda #&2a ; '*'                                                    ; 839b: a9 2a       .*             ; A=&2A: error ptr for retry
; &839d referenced 1 time by &838b
.store_fs_hdr_clc
    clc                                                               ; 839d: 18          .              ; CLC: no byte-stream path
; &839e referenced 1 time by &8388
.store_fs_hdr_fn
    sty fs_cmd_y_param                                                ; 839e: 8c 01 0f    ...            ; Store function code at &0F01
    sta fs_error_ptr                                                  ; 83a1: 85 b8       ..             ; Store error ptr for TX poll
    ldy #1                                                            ; 83a3: a0 01       ..             ; Y=1: copy CSD (offset 1) then LIB (offset 0)
; &83a5 referenced 1 time by &83ac
.copy_dir_handles
    lda fs_csd_handle,y                                               ; 83a5: b9 03 0e    ...            ; Copy CSD and LIB handles to command buffer; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 83a8: 99 03 0f    ...            ; Store at &0F03 (CSD) and &0F04 (LIB)
    dey                                                               ; 83ab: 88          .              ; Y=function code
    bpl copy_dir_handles                                              ; 83ac: 10 f7       ..             ; Loop for both handles
; ***************************************************************************************
; Build and send FS command (DOFSOP)
; 
; Sets reply port to &90 (PREPLY) at &0F00, initialises the TX
; control block, then adjusts TXCB's high pointer (HPTR) to X+5
; -- the 5-byte FS header (reply port, function code, URD, CSD,
; LIB) plus the command data -- so only meaningful bytes are
; transmitted, conserving Econet bandwidth. If carry is set on
; entry (DOFSBX byte-stream path), takes the alternate path
; through econet_tx_retry for direct BSXMIT transmission.
; Otherwise sets up the TX pointer via setup_tx_ptr_c0 and falls
; through to send_fs_reply_cmd for reply handling. The carry flag
; is the sole discriminator between byte-stream and standard FS
; protocol paths -- set by SEC at the BPUTV/BGETV entry points.
; On return from WAITFS/BSXMIT, Y=0; INY advances past the
; command code to read the return code. Error &D6 ("not found")
; is detected via ADC #(&100-&D6) with C=0 -- if the return code
; was exactly &D6, the result wraps to zero (Z=1). This is a
; branchless comparison returning C=1, A=0 as a soft error that
; callers can handle, vs hard errors which go through FSERR.
; 
; On Entry:
;     X: buffer extent (command-specific data bytes)
;     Y: function code
;     A: timeout period for FS reply
;     C: 0 for standard FS path, 1 for byte-stream (BSXMIT)
; 
; On Exit:
;     A: 0 on success
;     X: 0 on success, &D6 on not-found
;     Y: 1 (offset past command code in reply)
; ***************************************************************************************
; &83ae referenced 1 time by &8b15
.build_send_fs_cmd
    php                                                               ; 83ae: 08          .              ; Save carry (FS path vs byte-stream)
    lda #&90                                                          ; 83af: a9 90       ..             ; Reply port &90 (PREPLY)
    sta fs_cmd_type                                                   ; 83b1: 8d 00 0f    ...            ; Store at &0F00 (HDRREP)
    jsr init_tx_ctrl_block                                            ; 83b4: 20 60 83     `.            ; Copy TX template to &00C0
    txa                                                               ; 83b7: 8a          .              ; A = X (buffer extent)
    adc #5                                                            ; 83b8: 69 05       i.             ; HPTR = header (5) + data (X) bytes to send
    sta txcb_end                                                      ; 83ba: 85 c8       ..             ; Store to TXCB end-pointer low
    plp                                                               ; 83bc: 28          (              ; Restore carry flag
    bcs dofsl5                                                        ; 83bd: b0 22       ."             ; C=1: byte-stream path (BSXMIT)
    php                                                               ; 83bf: 08          .              ; Save flags for send_fs_reply_cmd
    jsr setup_tx_ptr_c0                                               ; 83c0: 20 69 86     i.            ; Point net_tx_ptr to &00C0; transmit
    plp                                                               ; 83c3: 28          (              ; Restore flags
    bcc send_fs_reply_cmd                                             ; 83c4: 90 04       ..             ; C=0: standard FS command path
; ***************************************************************************************
; Send FS command with standard timeout
; 
; Wrapper for send_fs_reply_cmd that sets the timeout counter
; (fs_error_ptr at &B8) to &2A before falling through. The &2A
; value becomes the outer loop count in send_to_fs's 3-level
; polling loop (~42 x 65536 iterations). Called after file
; transfer operations to send the completion command to the
; fileserver. Eliminated in 3.35K where call sites inline the
; LDA #&2A / STA fs_error_ptr sequence directly.
; ***************************************************************************************
; &83c6 referenced 2 times by &87b9, &8a99
.send_fs_reply_timed
    lda #&2a ; '*'                                                    ; 83c6: a9 2a       .*             ; A=&2A: error ptr for retry
    sta fs_error_ptr                                                  ; 83c8: 85 b8       ..             ; Store error ptr for TX poll
; &83ca referenced 1 time by &83c4
.send_fs_reply_cmd
    php                                                               ; 83ca: 08          .              ; Save flags (V flag state)
    jsr init_tx_reply_port                                            ; 83cb: 20 52 83     R.            ; Set up RX wait for FS reply
    lda fs_error_ptr                                                  ; 83ce: a5 b8       ..             ; Load error ptr for TX retry
    jsr send_to_fs                                                    ; 83d0: 20 fa 84     ..            ; Transmit and wait (BRIANX)
    plp                                                               ; 83d3: 28          (              ; Restore flags
; &83d4 referenced 1 time by &83ea
.dofsl7
    iny                                                               ; 83d4: c8          .              ; Y=1: skip past command code byte
    lda (txcb_start),y                                                ; 83d5: b1 c4       ..             ; Load return code from FS reply
    tax                                                               ; 83d7: aa          .              ; X = return code
    beq return_dofsl7                                                 ; 83d8: f0 06       ..             ; Zero: success, return
    bvc check_fs_error                                                ; 83da: 50 02       P.             ; V=0: standard path, error is fatal
    adc #&2a ; '*'                                                    ; 83dc: 69 2a       i*             ; ADC #&2A: test for &D6 (not found)
; &83de referenced 1 time by &83da
.check_fs_error
    bne store_fs_error                                                ; 83de: d0 70       .p             ; Non-zero: hard error, go to FSERR
; &83e0 referenced 1 time by &83d8
.return_dofsl7
    rts                                                               ; 83e0: 60          `              ; Return (success or soft &D6 error)

; &83e1 referenced 1 time by &83bd
.dofsl5
    pla                                                               ; 83e1: 68          h              ; Discard saved flags from stack
    ldx #&c0                                                          ; 83e2: a2 c0       ..             ; X=&C0: TXCB address for byte-stream TX
    iny                                                               ; 83e4: c8          .              ; Y++ past command code
    jsr econet_tx_retry                                               ; 83e5: 20 5b 92     [.            ; Byte-stream transmit with retry
    sta fs_load_addr_3                                                ; 83e8: 85 b3       ..             ; Store result to &B3
    bcc dofsl7                                                        ; 83ea: 90 e8       ..             ; C=0: success, check reply code
.bputv_handler
    clc                                                               ; 83ec: 18          .              ; CLC for address addition
; ***************************************************************************************
; Handle BPUT/BGET file byte I/O
; 
; BPUTV enters at &83A3 (CLC; fall through) and BGETV enters
; at &8486 (SEC; JSR here). The carry flag is preserved via
; PHP/PLP through the call chain and tested later (BCS) to
; select byte-stream transmission (BSXMIT) vs normal FS
; transmission (FSXMIT) -- a control-flow encoding using
; processor flags to avoid an extra flag variable.
; 
; BSXMIT uses handle=0 for print stream transactions (which
; sidestep the SEQNOS sequence number manipulation) and non-zero
; handles for file operations. After transmission, the high
; pointer bytes of the CB are reset to &FF -- "The BGET/PUT byte
; fix" which prevents stale buffer pointers corrupting subsequent
; byte-level operations.
; 
; On Entry:
;     C: 0 for BPUT (write byte), 1 for BGET (read byte)
;     A: byte to write (BPUT only)
;     Y: file handle
; 
; On Exit:
;     A: preserved
;     X: preserved
;     Y: preserved
; ***************************************************************************************
; &83ed referenced 1 time by &853a
.handle_bput_bget
    pha                                                               ; 83ed: 48          H              ; Save A (BPUT byte) on stack
    sta fs_error_flags                                                ; 83ee: 8d df 0f    ...            ; Also save byte at &0FDF for BSXMIT
    txa                                                               ; 83f1: 8a          .              ; Transfer X for stack save
    pha                                                               ; 83f2: 48          H              ; Save X on stack
    tya                                                               ; 83f3: 98          .              ; Transfer Y (handle) for stack save
    pha                                                               ; 83f4: 48          H              ; Save Y (handle) on stack
    php                                                               ; 83f5: 08          .              ; Save P (C = BPUT/BGET selector) on stack
    sty fs_spool_handle                                               ; 83f6: 84 ba       ..             ; Save handle for SPOOL/EXEC comparison later
    jsr handle_to_mask_clc                                            ; 83f8: 20 26 86     &.            ; Convert handle Y to single-bit mask
    sty fs_handle_mask                                                ; 83fb: 8c de 0f    ...            ; Store handle bitmask at &0FDE
    sty fs_spool0                                                     ; 83fe: 84 cf       ..             ; Store handle bitmask for sequence tracking
    ldy #&90                                                          ; 8400: a0 90       ..             ; &90 = data port (PREPLY)
    sty fs_putb_buf                                                   ; 8402: 8c dc 0f    ...            ; Store reply port in command buffer
    jsr init_tx_ctrl_block                                            ; 8405: 20 60 83     `.            ; Set up 12-byte TXCB from template
    lda #&dc                                                          ; 8408: a9 dc       ..             ; CB reply buffer at &0FDC
    sta txcb_start                                                    ; 840a: 85 c4       ..             ; Store reply buffer ptr low in TXCB
    lda #&e0                                                          ; 840c: a9 e0       ..             ; Error buffer at &0FE0
    sta txcb_end                                                      ; 840e: 85 c8       ..             ; Store error buffer ptr low in TXCB
    iny                                                               ; 8410: c8          .              ; Y=1 (from init_tx_ctrl_block exit)
    ldx #9                                                            ; 8411: a2 09       ..             ; X=9: BPUT function code
    plp                                                               ; 8413: 28          (              ; Restore C: selects BPUT (0) vs BGET (1)
    bcc store_retry_count                                             ; 8414: 90 01       ..             ; C=0 (BPUT): keep X=9
    dex                                                               ; 8416: ca          .              ; X=&08
; &8417 referenced 1 time by &8414
.store_retry_count
    stx fs_getb_buf                                                   ; 8417: 8e dd 0f    ...            ; Store function code at &0FDD
    lda fs_spool0                                                     ; 841a: a5 cf       ..             ; Load handle bitmask for BSXMIT
    ldx #&c0                                                          ; 841c: a2 c0       ..             ; X=&C0: TXCB address for econet_tx_retry
    jsr econet_tx_retry                                               ; 841e: 20 5b 92     [.            ; Transmit via byte-stream protocol
    ldx fs_getb_buf                                                   ; 8421: ae dd 0f    ...            ; Load reply byte from buffer
    beq update_sequence_return                                        ; 8424: f0 48       .H             ; Zero reply = success, skip error handling
    ldy #&1f                                                          ; 8426: a0 1f       ..             ; Copy 32-byte reply to error buffer at &0FE0
; &8428 referenced 1 time by &842f
.error1
    lda fs_putb_buf,y                                                 ; 8428: b9 dc 0f    ...            ; Load reply byte at offset Y
    sta fs_error_buf,y                                                ; 842b: 99 e0 0f    ...            ; Store to error buffer at &0FE0+Y
    dey                                                               ; 842e: 88          .              ; Next byte (descending)
    bpl error1                                                        ; 842f: 10 f7       ..             ; Loop until all 32 bytes copied
    tax                                                               ; 8431: aa          .              ; X=File handle
    lda #osbyte_read_write_exec_file_handle                           ; 8432: a9 c6       ..             ; A=&C6: read *EXEC file handle
    jsr osbyte                                                        ; 8434: 20 f4 ff     ..            ; Read/Write *EXEC file handle
    lda #&f1                                                          ; 8437: a9 f1       ..             ; A=&F1: OSCLI "SP." string at &84F1
    cpy fs_spool_handle                                               ; 8439: c4 ba       ..             ; Y=value of *SPOOL file handle
    beq close_spool_exec                                              ; 843b: f0 06       ..             ; Match: close SPOOL file
    lda #&f5                                                          ; 843d: a9 f5       ..             ; A=&F5: offset for 'E.' string
    cpx fs_spool_handle                                               ; 843f: e4 ba       ..             ; X=value of *EXEC file handle
    bne dispatch_fs_error                                             ; 8441: d0 06       ..             ; No match: dispatch FS error
; &8443 referenced 1 time by &843b
.close_spool_exec
    tax                                                               ; 8443: aa          .              ; X = string offset for OSCLI close
    ldy #&84                                                          ; 8444: a0 84       ..             ; Y=&84: high byte of OSCLI string in ROM
    jsr oscli                                                         ; 8446: 20 f7 ff     ..            ; Close SPOOL/EXEC via "*SP." or "*E."
; &8449 referenced 1 time by &8441
.dispatch_fs_error
    lda #&e0                                                          ; 8449: a9 e0       ..             ; Reset CB pointer to error buffer at &0FE0
    sta txcb_start                                                    ; 844b: 85 c4       ..             ; Reset reply ptr to error buffer
    ldx fs_getb_buf                                                   ; 844d: ae dd 0f    ...            ; Reload reply byte for error dispatch
; ***************************************************************************************
; Handle fileserver error replies (FSERR)
; 
; The fileserver returns errors as: zero command code + error number +
; CR-terminated message string. This routine converts the reply buffer
; in-place to a standard MOS BRK error packet by:
;   1. Storing the error code at fs_last_error (&0E09)
;   2. Normalizing error codes below &A8 to &A8 (the standard FS error
;      number), since the MOS error space below &A8 has other meanings
;   3. Scanning for the CR terminator and replacing it with &00
;   4. JMPing indirect through (l00c4) to execute the buffer as a BRK
;      instruction — the zero command code serves as the BRK opcode
; N.B. This relies on the fileserver always returning a zero command
; code in position 0 of the reply buffer.
; ***************************************************************************************
; &8450 referenced 1 time by &83de
.store_fs_error
    stx fs_last_error                                                 ; 8450: 8e 09 0e    ...            ; Remember raw FS error code
    ldy #1                                                            ; 8453: a0 01       ..             ; Y=1: point to error number byte in reply
    cpx #&a8                                                          ; 8455: e0 a8       ..             ; Clamp FS errors below &A8 to standard &A8
    bcs error_code_clamped                                            ; 8457: b0 04       ..             ; Error >= &A8: keep original value
    lda #&a8                                                          ; 8459: a9 a8       ..             ; Error < &A8: override with standard &A8
    sta (txcb_start),y                                                ; 845b: 91 c4       ..             ; Write clamped error number to reply buffer
; &845d referenced 1 time by &8457
.error_code_clamped
    ldy #&ff                                                          ; 845d: a0 ff       ..             ; Start scanning from offset &FF (will INY to 0)
; &845f referenced 1 time by &8467
.copy_error_to_brk
    iny                                                               ; 845f: c8          .              ; Next byte in reply buffer
    lda (txcb_start),y                                                ; 8460: b1 c4       ..             ; Copy reply buffer to &0100 for BRK execution
    sta l0100,y                                                       ; 8462: 99 00 01    ...            ; Build BRK error block at &0100
    eor #&0d                                                          ; 8465: 49 0d       I.             ; Scan for CR terminator (&0D)
    bne copy_error_to_brk                                             ; 8467: d0 f6       ..             ; Continue until CR found
    sta l0100,y                                                       ; 8469: 99 00 01    ...            ; Replace CR with zero = BRK error block end
    beq execute_downloaded                                            ; 846c: f0 44       .D             ; Execute as BRK error block at &0100; ALWAYS; ALWAYS branch

; &846e referenced 1 time by &8424
.update_sequence_return
    sta fs_sequence_nos                                               ; 846e: 8d 08 0e    ...            ; Save updated sequence number
    pla                                                               ; 8471: 68          h              ; Restore Y from stack
    tay                                                               ; 8472: a8          .              ; Transfer A to Y for indexing
    pla                                                               ; 8473: 68          h              ; Restore X from stack
    tax                                                               ; 8474: aa          .              ; Transfer to X for return
    pla                                                               ; 8475: 68          h              ; Restore A from stack
.return_remote_cmd
    rts                                                               ; 8476: 60          `              ; Return to caller

; ***************************************************************************************
; Remote boot/execute handler
; 
; Checks byte 4 of the RX control block (remote status flag).
; If zero (not currently remoted), falls through to remot1 to
; set up a new remote session. If non-zero (already remoted),
; jumps to clear_jsr_protection and returns.
; ***************************************************************************************
.lang_1_remote_boot
    ldy #4                                                            ; 8477: a0 04       ..             ; Y=4: remote status flag offset
    lda (net_rx_ptr),y                                                ; 8479: b1 9c       ..             ; Read remote status from RX CB
    beq remot1                                                        ; 847b: f0 03       ..             ; Zero: not remoted, set up session
; &847d referenced 1 time by &84c3
.rchex
    jmp clear_jsr_protection                                          ; 847d: 4c e9 92    L..            ; Already remoted: clear and return

; &8480 referenced 2 times by &847b, &84b9
.remot1
    ora #9                                                            ; 8480: 09 09       ..             ; Set remote status: bits 0+3 (ORA #9)
    sta (net_rx_ptr),y                                                ; 8482: 91 9c       ..             ; Store updated remote status
    ldx #&80                                                          ; 8484: a2 80       ..             ; X=&80: RX data area offset
    ldy #&80                                                          ; 8486: a0 80       ..             ; Y=&80: read source station low
    lda (net_rx_ptr),y                                                ; 8488: b1 9c       ..             ; Read source station lo from RX data at &80
    pha                                                               ; 848a: 48          H              ; Save source station low byte
    iny                                                               ; 848b: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 848c: b1 9c       ..             ; Read source station hi from RX data at &81
    ldy #&0f                                                          ; 848e: a0 0f       ..             ; Save controlling station to workspace &0E/&0F
    sta (nfs_workspace),y                                             ; 8490: 91 9e       ..             ; Store station high to ws+&0F
    dey                                                               ; 8492: 88          .              ; Y=&0E; Y=&0e
    pla                                                               ; 8493: 68          h              ; Restore source station low
    sta (nfs_workspace),y                                             ; 8494: 91 9e       ..             ; Store station low to ws+&0E
    jsr clear_osbyte_ce_cf                                            ; 8496: 20 a0 81     ..            ; Clear OSBYTE &CE/&CF flags
    jsr ctrl_block_setup                                              ; 8499: 20 76 91     v.            ; Set up TX control block
    ldx #1                                                            ; 849c: a2 01       ..             ; X=1: disable keyboard
    ldy #0                                                            ; 849e: a0 00       ..             ; Y=0 for OSBYTE
    lda #osbyte_read_write_econet_keyboard_disable                    ; 84a0: a9 c9       ..             ; Disable keyboard for remote session
    jsr osbyte                                                        ; 84a2: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute code at &0100
; 
; Clears JSR protection, zeroes &0100-&0102 (creating a BRK
; instruction at &0100 as a safe default), then JMP &0100 to
; execute code received over the network. If no code was loaded,
; the BRK triggers an error handler.
; ***************************************************************************************
.lang_3_execute_at_0100
    jsr clear_jsr_protection                                          ; 84a5: 20 e9 92     ..            ; Allow JSR to page 1 (stack page)
    ldx #2                                                            ; 84a8: a2 02       ..             ; Zero bytes &0100-&0102
    lda #0                                                            ; 84aa: a9 00       ..             ; A=0: zero execution header bytes
; &84ac referenced 1 time by &84b0
.zero_exec_header
    sta l0100,x                                                       ; 84ac: 9d 00 01    ...            ; BRK at &0100 as safe default
    dex                                                               ; 84af: ca          .              ; Next byte
    bpl zero_exec_header                                              ; 84b0: 10 fa       ..             ; Loop until all zeroed
; &84b2 referenced 2 times by &846c, &84eb
.execute_downloaded
    jmp l0100                                                         ; 84b2: 4c 00 01    L..            ; Execute downloaded code

; ***************************************************************************************
; Remote operation with source validation
; 
; Validates that the source station in the received packet matches
; the controlling station stored in the NFS workspace. If byte 4 of
; the RX control block is zero (not currently remoted), allows the
; new remote session via remot1. If non-zero, compares the source
; station at RX offset &80 against workspace offset &0E -- rejects
; mismatched stations via clear_jsr_protection, accepts matching
; stations by falling through to lang_0_insert_remote_key.
; ***************************************************************************************
.lang_4_remote_validated
    ldy #4                                                            ; 84b5: a0 04       ..             ; Y=4: RX control block byte 4 (remote status)
    lda (net_rx_ptr),y                                                ; 84b7: b1 9c       ..             ; Read remote status flag
    beq remot1                                                        ; 84b9: f0 c5       ..             ; Zero = not remoted; allow new session
    ldy #&80                                                          ; 84bb: a0 80       ..             ; Read source station from RX data at &80
    lda (net_rx_ptr),y                                                ; 84bd: b1 9c       ..             ; A = source station number
    ldy #&0e                                                          ; 84bf: a0 0e       ..             ; Compare against controlling station at &0E
    cmp (nfs_workspace),y                                             ; 84c1: d1 9e       ..             ; Check if source matches controller
    bne rchex                                                         ; 84c3: d0 b8       ..             ; Reject: source != controlling station
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.lang_0_insert_remote_key
    ldy #&82                                                          ; 84c5: a0 82       ..             ; Read keypress from RX data at &82
    lda (net_rx_ptr),y                                                ; 84c7: b1 9c       ..             ; Load character byte
    tay                                                               ; 84c9: a8          .              ; Y = character to insert
    ldx #0                                                            ; 84ca: a2 00       ..             ; X = buffer 0 (keyboard input)
    jsr clear_jsr_protection                                          ; 84cc: 20 e9 92     ..            ; Release JSR protection before inserting key
    lda #osbyte_insert_input_buffer                                   ; 84cf: a9 99       ..             ; OSBYTE &99: insert char into input buffer
    jmp osbyte                                                        ; 84d1: 4c f4 ff    L..            ; Tail call: insert character Y into buffer X; Insert character Y into input buffer X

; &84d4 referenced 1 time by &8527
.error_not_listening
    lda #8                                                            ; 84d4: a9 08       ..             ; Error code 8: "Not listening" error
    bne set_listen_offset                                             ; 84d6: d0 04       ..             ; ALWAYS branch to set_listen_offset; ALWAYS branch

; &84d8 referenced 1 time by &86b2
.nlistn
    lda (net_tx_ptr,x)                                                ; 84d8: a1 9a       ..             ; Load TX status byte for error lookup
; &84da referenced 2 times by &8537, &89de
.nlisne
    and #7                                                            ; 84da: 29 07       ).             ; Mask to 3-bit error code (0-7)
; &84dc referenced 1 time by &84d6
.set_listen_offset
    tax                                                               ; 84dc: aa          .              ; X = error code index
    ldy error_offsets,x                                               ; 84dd: bc 14 80    ...            ; Look up error message offset from table
    ldx #0                                                            ; 84e0: a2 00       ..             ; X=0: start writing at &0101
    stx l0100                                                         ; 84e2: 8e 00 01    ...            ; Store BRK opcode at &0100
; &84e5 referenced 1 time by &84ef
.copy_error_message
    lda error_msg_table,y                                             ; 84e5: b9 56 85    .V.            ; Load error message byte
    sta l0101,x                                                       ; 84e8: 9d 01 01    ...            ; Build error message at &0101+
    beq execute_downloaded                                            ; 84eb: f0 c5       ..             ; Zero byte = end of message; go execute BRK
    iny                                                               ; 84ed: c8          .              ; Next error message source byte
    inx                                                               ; 84ee: e8          .              ; Next error buffer position
    bne copy_error_message                                            ; 84ef: d0 f4       ..             ; Continue copying message
    equs "SP."                                                        ; 84f1: 53 50 2e    SP.
    equb &0d, &45, &2e, &0d                                           ; 84f4: 0d 45 2e... .E.

; &84f8 referenced 3 times by &875d, &9036, &9290
.send_to_fs_star
    lda #&2a ; '*'                                                    ; 84f8: a9 2a       .*             ; A=&2A: error ptr for FS send
; ***************************************************************************************
; Send command to fileserver and handle reply (WAITFS)
; 
; Performs a complete FS transaction: transmit then wait for reply.
; Sets bit 7 of rx_status_flags (mark FS transaction in progress),
; builds a TX frame from the data at (net_tx_ptr), and transmits
; it. The system RX flag (LFLAG bit 7) is only set when receiving
; into the page-zero control block — if RXCBP's high byte is
; non-zero, setting the system flag would interfere with other RX
; operations. The timeout counter uses the stack (indexed via TSX)
; rather than memory to avoid bus conflicts with Econet hardware
; during the tight polling loop. Handles multi-block replies and
; checks for escape conditions between blocks.
; ***************************************************************************************
; &84fa referenced 2 times by &83d0, &884c
.send_to_fs
    pha                                                               ; 84fa: 48          H              ; Save function code on stack
    lda rx_flags                                                      ; 84fb: ad 64 0d    .d.            ; Load current rx_flags
    pha                                                               ; 84fe: 48          H              ; Save rx_flags on stack for restore
    ora #&80                                                          ; 84ff: 09 80       ..             ; Set bit7: FS transaction in progress
    sta rx_flags                                                      ; 8501: 8d 64 0d    .d.            ; Write back updated rx_flags
.skip_rx_flag_set
    lda #0                                                            ; 8504: a9 00       ..             ; Push two zero bytes as timeout counters
    pha                                                               ; 8506: 48          H              ; First zero for timeout
    pha                                                               ; 8507: 48          H              ; Second zero for timeout
    tay                                                               ; 8508: a8          .              ; Y=0: index for flag byte check; Y=&00
    tsx                                                               ; 8509: ba          .              ; TSX: index stack-based timeout via X
; &850a referenced 3 times by &8514, &8519, &851e
.fs_reply_poll
    jsr check_escape                                                  ; 850a: 20 2a 85     *.            ; Check for user escape condition
.incpx
    lda (net_tx_ptr),y                                                ; 850d: b1 9a       ..             ; Read flag byte from TX control block
    bmi fs_wait_cleanup                                               ; 850f: 30 0f       0.             ; Bit 7 set = reply received
    dec l0101,x                                                       ; 8511: de 01 01    ...            ; Three-stage nested timeout: inner loop
    bne fs_reply_poll                                                 ; 8514: d0 f4       ..             ; Inner not expired: keep polling
    dec l0102,x                                                       ; 8516: de 02 01    ...            ; Middle timeout loop
    bne fs_reply_poll                                                 ; 8519: d0 ef       ..             ; Middle not expired: keep polling
    dec l0104,x                                                       ; 851b: de 04 01    ...            ; Outer timeout loop (slowest)
    bne fs_reply_poll                                                 ; 851e: d0 ea       ..             ; Outer not expired: keep polling
; &8520 referenced 1 time by &850f
.fs_wait_cleanup
    pla                                                               ; 8520: 68          h              ; Pop first timeout byte
    pla                                                               ; 8521: 68          h              ; Pop second timeout byte
    pla                                                               ; 8522: 68          h              ; Pop saved rx_flags into A
    sta rx_flags                                                      ; 8523: 8d 64 0d    .d.            ; Restore saved rx_flags from stack
    pla                                                               ; 8526: 68          h              ; Pop saved function code
    beq error_not_listening                                           ; 8527: f0 ab       ..             ; A=saved func code; zero would mean no reply
    rts                                                               ; 8529: 60          `              ; Return to caller

; ***************************************************************************************
; Check and handle escape condition (ESC)
; 
; Two-level escape gating: the MOS escape flag (&FF bit 7) is ANDed
; with the software enable flag ESCAP. Both must have bit 7 set for
; escape to fire. ESCAP is set non-zero during data port operations
; (LOADOP stores the data port &90, serving double duty as both the
; port number and the escape-enable flag). ESCAP is disabled via LSR
; in the ENTER routine, which clears bit 7 — PHP/PLP around the LSR
; preserves the carry flag since ENTER is called from contexts where
; carry has semantic meaning (e.g., PUTBYT vs BGET distinction).
; This architecture allows escape between retransmission attempts
; but prevents interruption during critical FS transactions. If
; escape fires: acknowledges via OSBYTE &7E, then checks whether
; the failing handle is the current SPOOL or EXEC handle (OSBYTE
; &C6/&C7); if so, issues "*SP." or "*E." via OSCLI to gracefully
; close the channel before raising the error — preventing the system
; from continuing to spool output to a broken file handle.
; ***************************************************************************************
; &852a referenced 2 times by &850a, &8699
.check_escape
    lda #&7e ; '~'                                                    ; 852a: a9 7e       .~             ; A=&7E: OSBYTE acknowledge escape
; ***************************************************************************************
; Test MOS escape flag and abort if pending
; 
; Tests MOS escape flag (&FF bit 7). If escape is pending:
; acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
; the control block via (net_tx_ptr),Y, and branches to the
; NLISTN error path. If no escape, returns immediately.
; ***************************************************************************************
.check_escape_handler
    bit escape_flag                                                   ; 852c: 24 ff       $.             ; Test escape flag (bit 7)
    bpl return_4                                                      ; 852e: 10 25       .%             ; Bit 7 clear: no escape, return
    jsr osbyte                                                        ; 8530: 20 f4 ff     ..            ; Acknowledge escape via OSBYTE &7E
    lsr a                                                             ; 8533: 4a          J              ; LSR: get escape result bit
    sta (net_tx_ptr),y                                                ; 8534: 91 9a       ..             ; Store escape result to TXCB
    asl a                                                             ; 8536: 0a          .              ; Restore A
    bne nlisne                                                        ; 8537: d0 a1       ..             ; Non-zero: report 'Not listening'
.bgetv_handler
    sec                                                               ; 8539: 38          8              ; C=1: flag for BGET mode
    jsr handle_bput_bget                                              ; 853a: 20 ed 83     ..            ; Handle BGET via FS command; Handle BPUT/BGET file byte I/O
    sec                                                               ; 853d: 38          8              ; SEC: set carry for error check
    lda #&fe                                                          ; 853e: a9 fe       ..             ; A=&FE: mask for EOF check
    bit fs_error_flags                                                ; 8540: 2c df 0f    ,..            ; BIT l0fdf: test error flags
    bvs return_4                                                      ; 8543: 70 10       p.             ; V=1: error, return early
    clc                                                               ; 8545: 18          .              ; CLC: no error
    php                                                               ; 8546: 08          .              ; Save P (C=0 from CLC above)
    lda fs_spool0                                                     ; 8547: a5 cf       ..             ; Load handle bitmask
    plp                                                               ; 8549: 28          (              ; Restore C flag for branch test
    bmi bgetv_shared_jsr                                              ; 854a: 30 03       0.             ; Bit 7 set: skip clear, just set
    jsr clear_fs_flag                                                 ; 854c: 20 60 86     `.            ; Clear EOF hint for this handle
; &854f referenced 1 time by &854a
.bgetv_shared_jsr
    jsr set_fs_flag                                                   ; 854f: 20 5b 86     [.            ; Set EOF flag for this handle
.load_handle_mask
    lda fs_handle_mask                                                ; 8552: ad de 0f    ...            ; Load handle bitmask for caller
; &8555 referenced 2 times by &852e, &8543
.return_4
    rts                                                               ; 8555: 60          `              ; Return with handle mask in A

; Econet error message table (ERRTAB, 7 entries).
; Each entry: error number byte followed by NUL-terminated string.
;   &A0: "Line Jammed"     &A1: "Net Error"
;   &A2: "Not listening"   &A3: "No Clock"
;   &11: "Escape"           &CB: "Bad Option"
;   &A5: "No reply"
; Indexed by the low 3 bits of the TXCB flag byte (AND #&07),
; which encode the specific Econet failure reason. The NREPLY
; and NLISTN routines build a MOS BRK error block at &100 on the
; stack page: NREPLY fires when the fileserver does not respond
; within the timeout period; NLISTN fires when the destination
; station actively refused the connection.
; Indexed via the error dispatch at c8424/c842c.
; &8556 referenced 1 time by &84e5
.error_msg_table
    equb &a0                                                          ; 8556: a0          .
    equs "Line Jammed", 0                                             ; 8557: 4c 69 6e... Lin
    equb &a1                                                          ; 8563: a1          .
    equs "Net Error", 0                                               ; 8564: 4e 65 74... Net
    equb &a2                                                          ; 856e: a2          .
    equs "Not listening", 0                                           ; 856f: 4e 6f 74... Not
    equb &a3                                                          ; 857d: a3          .
    equs "No Clock", 0                                                ; 857e: 4e 6f 20... No
    equb &11                                                          ; 8587: 11          .
    equs "Escape", 0                                                  ; 8588: 45 73 63... Esc
    equb &cb                                                          ; 858f: cb          .
    equs "Bad Option", 0                                              ; 8590: 42 61 64... Bad
    equb &a5                                                          ; 859b: a5          .
    equs "No reply", 0                                                ; 859c: 4e 6f 20... No

; ***************************************************************************************
; Save FSCV arguments with text pointers
; 
; Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
; Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
; falls through to save_fscv_args to store A/X/Y in the FS
; workspace.
; ***************************************************************************************
; &85a5 referenced 3 times by &80c7, &8978, &8bb4
.save_fscv_args_with_ptrs
    stx os_text_ptr                                                   ; 85a5: 86 f2       ..             ; X to os_text_ptr (text ptr lo)
    sty os_text_ptr_hi                                                ; 85a7: 84 f3       ..             ; Y to os_text_ptr hi
    stx fs_cmd_ptr                                                    ; 85a9: 8e 10 0e    ...            ; X to FS command ptr lo
    sty l0e11                                                         ; 85ac: 8c 11 0e    ...            ; Y to FS command ptr hi
; ***************************************************************************************
; Save FSCV/vector arguments
; 
; Stores A, X, Y into the filing system workspace. Called at the
; start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
; GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
;   &BD (fs_last_byte_flag) = A (function code / command)
;   &BB (fs_options)        = X (control block ptr low)
;   &BC (fs_block_offset)   = Y (control block ptr high)
;   &BE/&BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)
; ***************************************************************************************
; &85af referenced 3 times by &86e7, &890c, &8a10
.save_fscv_args
    sta fs_last_byte_flag                                             ; 85af: 85 bd       ..             ; A = function code / command
    stx fs_options                                                    ; 85b1: 86 bb       ..             ; X = control block ptr lo
    sty fs_block_offset                                               ; 85b3: 84 bc       ..             ; Y = control block ptr hi
    stx fs_crc_lo                                                     ; 85b5: 86 be       ..             ; X dup for indexed access via (fs_crc)
    sty fs_crc_hi                                                     ; 85b7: 84 bf       ..             ; Y dup for indexed access
    rts                                                               ; 85b9: 60          `              ; Return

; ***************************************************************************************
; Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)
; 
; Reads attribute byte at offset &0E from the parameter block,
; masks to 6 bits, then falls through to the shared bitmask
; builder. Converts fileserver protection format (5-6 bits) to
; BBC OSFILE attribute format (8 bits) via the lookup table at
; &85D7. The two formats use different bit layouts for file
; protection attributes.
; ***************************************************************************************
; &85ba referenced 2 times by &889f, &88ca
.decode_attribs_6bit
    ldy #&0e                                                          ; 85ba: a0 0e       ..             ; Y=&0E: attribute byte offset in param block
    lda (fs_options),y                                                ; 85bc: b1 bb       ..             ; Load FS attribute byte
    and #&3f ; '?'                                                    ; 85be: 29 3f       )?             ; Mask to 6 bits (FS → BBC direction)
    ldx #4                                                            ; 85c0: a2 04       ..             ; X=4: skip first 4 table entries (BBC→FS half)
    bne attrib_shift_bits                                             ; 85c2: d0 04       ..             ; ALWAYS branch to shared bitmask builder; ALWAYS branch

; ***************************************************************************************
; Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)
; 
; Masks A to 5 bits and builds an access bitmask via the
; lookup table at &85D7. Each input bit position maps to a
; different output bit via the table. The conversion is done
; by iterating through the source bits and OR-ing in the
; corresponding destination bits from the table, translating
; between BBC (8-bit) and fileserver (5-bit) protection formats.
; ***************************************************************************************
; &85c4 referenced 2 times by &87c4, &88e7
.decode_attribs_5bit
    and #&1f                                                          ; 85c4: 29 1f       ).             ; Mask to 5 bits (BBC → FS direction)
    ldx #&ff                                                          ; 85c6: a2 ff       ..             ; X=&FF: INX makes 0; start from table index 0
; &85c8 referenced 1 time by &85c2
.attrib_shift_bits
    sta fs_error_ptr                                                  ; 85c8: 85 b8       ..             ; Temp storage for source bitmask to shift out
    lda #0                                                            ; 85ca: a9 00       ..             ; A=0: accumulate destination bits here
; &85cc referenced 1 time by &85d4
.map_attrib_bits
    inx                                                               ; 85cc: e8          .              ; Next table entry
    lsr fs_error_ptr                                                  ; 85cd: 46 b8       F.             ; Shift out source bits one at a time
    bcc skip_set_attrib_bit                                           ; 85cf: 90 03       ..             ; Bit was 0: skip this destination bit
    ora access_bit_table,x                                            ; 85d1: 1d d7 85    ...            ; OR in destination bit from lookup table
; &85d4 referenced 1 time by &85cf
.skip_set_attrib_bit
    bne map_attrib_bits                                               ; 85d4: d0 f6       ..             ; Loop while source bits remain (A != 0)
    rts                                                               ; 85d6: 60          `              ; Return; A = converted attribute bitmask

; &85d7 referenced 1 time by &85d1
.access_bit_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 85d7: 50 20 05... P .

; ***************************************************************************************
; Print inline string, high-bit terminated (VSTRNG)
; 
; Pops the return address from the stack, prints each byte via OSASCI
; until a byte with bit 7 set is found, then jumps to that address.
; The high-bit byte serves as both the string terminator and the opcode
; of the first instruction after the string. N.B. Cannot be used for
; BRK error messages -- the stack manipulation means a BRK in the
; inline data would corrupt the stack rather than invoke the error
; handler.
; 
; On Exit:
;     A: terminator byte (bit 7 set, also next opcode)
;     X: corrupted (by OSASCI)
;     Y: 0
; ***************************************************************************************
; &85e2 referenced 14 times by &81f7, &8222, &8242, &824f, &8c23, &8c2d, &8c3b, &8c46, &8c5b, &8c70, &8c83, &8c92, &8ca4, &8d74
.print_inline
    pla                                                               ; 85e2: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 85e3: 85 b0       ..             ; Store return addr low as string ptr
    pla                                                               ; 85e5: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 85e6: 85 b1       ..             ; Store return addr high as string ptr
    ldy #0                                                            ; 85e8: a0 00       ..             ; Y=0: offset for indirect load
; &85ea referenced 1 time by &85f7
.print_inline_char
    inc fs_load_addr                                                  ; 85ea: e6 b0       ..             ; Advance pointer past return address / to next char
    bne print_next_char                                               ; 85ec: d0 02       ..             ; No page wrap: skip high byte inc
    inc fs_load_addr_hi                                               ; 85ee: e6 b1       ..             ; Handle page crossing in pointer
; &85f0 referenced 1 time by &85ec
.print_next_char
    lda (fs_load_addr),y                                              ; 85f0: b1 b0       ..             ; Load next byte from inline string
    bmi jump_via_addr                                                 ; 85f2: 30 06       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 85f4: 20 e3 ff     ..            ; Write character
    jmp print_inline_char                                             ; 85f7: 4c ea 85    L..            ; Continue printing next character

; &85fa referenced 1 time by &85f2
.jump_via_addr
    jmp (fs_load_addr)                                                ; 85fa: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

; ***************************************************************************************
; Parse decimal number from (fs_options),Y (DECIN)
; 
; Reads ASCII digits and accumulates in &B2 (fs_load_addr_2).
; Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
; computed as ASL &B2 (x2), then A = &B2*4 via two ASLs,
; then ADC &B2 gives x10.
; Terminates on "." (pathname separator), control chars, or space.
; The delimiter handling was revised to support dot-separated path
; components (e.g. "1.$.PROG") -- originally stopped on any char
; >= &40 (any letter), but the revision allows numbers followed
; by dots.
; 
; On Entry:
;     Y: offset into (fs_options) buffer
; 
; On Exit:
;     A: parsed value (accumulated in &B2)
;     X: initial A value (saved by TAX)
;     Y: offset past last digit parsed
; ***************************************************************************************
; &85fd referenced 2 times by &808a, &8090
.parse_decimal
    tax                                                               ; 85fd: aa          .              ; Save A in X for caller
    lda #0                                                            ; 85fe: a9 00       ..             ; Zero accumulator
    sta fs_load_addr_2                                                ; 8600: 85 b2       ..             ; Clear accumulator workspace
; &8602 referenced 1 time by &861f
.scan_decimal_digit
    lda (fs_options),y                                                ; 8602: b1 bb       ..             ; Load next char from buffer
    cmp #&40 ; '@'                                                    ; 8604: c9 40       .@             ; Letter or above?
    bcs no_dot_exit                                                   ; 8606: b0 19       ..             ; Yes: not a digit, done
    cmp #&2e ; '.'                                                    ; 8608: c9 2e       ..             ; Dot separator?
    beq parse_decimal_rts                                             ; 860a: f0 16       ..             ; Yes: exit with C=1 (dot found)
    bmi no_dot_exit                                                   ; 860c: 30 13       0.             ; Control char or space: done
    and #&0f                                                          ; 860e: 29 0f       ).             ; Mask ASCII digit to 0-9
    sta fs_load_addr_3                                                ; 8610: 85 b3       ..             ; Save new digit
    asl fs_load_addr_2                                                ; 8612: 06 b2       ..             ; Running total * 2
    lda fs_load_addr_2                                                ; 8614: a5 b2       ..             ; A = running total * 2
    asl a                                                             ; 8616: 0a          .              ; A = running total * 4
    asl a                                                             ; 8617: 0a          .              ; A = running total * 8
    adc fs_load_addr_2                                                ; 8618: 65 b2       e.             ; + total*2 = total * 10
    adc fs_load_addr_3                                                ; 861a: 65 b3       e.             ; + digit = total*10 + digit
    sta fs_load_addr_2                                                ; 861c: 85 b2       ..             ; Store new running total
    iny                                                               ; 861e: c8          .              ; Advance to next char
    bne scan_decimal_digit                                            ; 861f: d0 e1       ..             ; Loop (always: Y won't wrap to 0)
; &8621 referenced 2 times by &8606, &860c
.no_dot_exit
    clc                                                               ; 8621: 18          .              ; No dot found: C=0
; &8622 referenced 1 time by &860a
.parse_decimal_rts
    lda fs_load_addr_2                                                ; 8622: a5 b2       ..             ; Return result in A
    rts                                                               ; 8624: 60          `              ; Return with result in A

; ***************************************************************************************
; Convert handle in A to bitmask
; 
; Transfers A to Y via TAY, then falls through to
; handle_to_mask_clc to clear carry and convert.
; ***************************************************************************************
; &8625 referenced 3 times by &8853, &8a2b, &8f4d
.handle_to_mask_a
    tay                                                               ; 8625: a8          .              ; Handle number to Y for conversion
; ***************************************************************************************
; Convert handle to bitmask (carry cleared)
; 
; Clears carry to ensure handle_to_mask converts
; unconditionally. Falls through to handle_to_mask.
; ***************************************************************************************
; &8626 referenced 2 times by &83f8, &8917
.handle_to_mask_clc
    clc                                                               ; 8626: 18          .              ; Force unconditional conversion
; ***************************************************************************************
; Convert file handle to bitmask (Y2FS)
; 
; Converts fileserver handles to single-bit masks segregated inside
; the BBC. NFS handles occupy the &20-&27 range (base HAND=&20),
; which cannot collide with local filing system or cassette handles
; -- the MOS routes OSFIND/OSBGET/OSBPUT to the correct filing
; system based on the handle value alone. The power-of-two encoding
; allows the EOF hint byte to track up to 8 files simultaneously
; with one bit per file, and enables fast set operations (ORA to
; add, EOR to toggle, AND to test) without loops. Handle 0 passes
; through unchanged (means "no file"). The bit-shift conversion loop
; has a built-in validity check: if the handle is out of range, the
; repeated ASL shifts all bits out, leaving A=0, which is converted
; to Y=&FF as a sentinel -- bad handles fail gracefully rather than
; indexing into garbage.
; Callers needing to move the handle from A use handle_to_mask_a;
; callers needing carry cleared use handle_to_mask_clc.
; 
; On Entry:
;     Y: handle number
;     C: 0: convert, 1 with Y=0: skip, 1 with Y!=0: convert
; 
; On Exit:
;     A: preserved
;     X: preserved
;     Y: bitmask (single bit set) or &FF if handle invalid
; ***************************************************************************************
; &8627 referenced 1 time by &897c
.handle_to_mask
    pha                                                               ; 8627: 48          H              ; Save A (will be restored on exit)
    txa                                                               ; 8628: 8a          .              ; Save X (will be restored on exit)
    pha                                                               ; 8629: 48          H              ;   (second half of X save)
    tya                                                               ; 862a: 98          .              ; A = handle from Y
    bcc y2fsl5                                                        ; 862b: 90 02       ..             ; C=0: always convert
    beq handle_mask_exit                                              ; 862d: f0 0f       ..             ; C=1 and Y=0: skip (handle 0 = none)
; &862f referenced 1 time by &862b
.y2fsl5
    sec                                                               ; 862f: 38          8              ; C=1 and Y!=0: convert
    sbc #&1f                                                          ; 8630: e9 1f       ..             ; A = handle - &1F (1-based bit position)
    tax                                                               ; 8632: aa          .              ; X = shift count
    lda #1                                                            ; 8633: a9 01       ..             ; Start with bit 0 set
; &8635 referenced 1 time by &8637
.y2fsl2
    asl a                                                             ; 8635: 0a          .              ; Shift bit left
    dex                                                               ; 8636: ca          .              ; Count down
    bne y2fsl2                                                        ; 8637: d0 fc       ..             ; Loop until correct position
    ror a                                                             ; 8639: 6a          j              ; Undo final extra shift
    tay                                                               ; 863a: a8          .              ; Y = resulting bitmask
    bne handle_mask_exit                                              ; 863b: d0 01       ..             ; Non-zero: valid mask, skip to exit
    dey                                                               ; 863d: 88          .              ; Zero: invalid handle, set Y=&FF
; &863e referenced 2 times by &862d, &863b
.handle_mask_exit
    pla                                                               ; 863e: 68          h              ; Restore X
    tax                                                               ; 863f: aa          .              ; Restore X from stack
    pla                                                               ; 8640: 68          h              ; Restore A
    rts                                                               ; 8641: 60          `              ; Return with mask in X

; ***************************************************************************************
; Convert bitmask to handle number (FS2A)
; 
; Inverse of Y2FS. Converts from the power-of-two FS format
; back to a sequential handle number by counting right shifts
; until A=0. Adds &1E to convert the 1-based bit position to
; a handle number (handles start at &1F+1 = &20). Used when
; receiving handle values from the fileserver in reply packets.
; 
; On Entry:
;     A: single-bit bitmask
; 
; On Exit:
;     A: handle number (&20-&27)
;     X: corrupted
;     Y: preserved
; ***************************************************************************************
; &8642 referenced 2 times by &89ab, &8f65
.mask_to_handle
    ldx #&1f                                                          ; 8642: a2 1f       ..             ; X = &1F (handle base - 1)
; &8644 referenced 1 time by &8646
.fs2al1
    inx                                                               ; 8644: e8          .              ; Count this bit position
    lsr a                                                             ; 8645: 4a          J              ; Shift mask right; C=0 when done
    bne fs2al1                                                        ; 8646: d0 fc       ..             ; Loop until all bits shifted out
    txa                                                               ; 8648: 8a          .              ; A = X = &1F + bit position = handle
    rts                                                               ; 8649: 60          `              ; Return with handle in A

; ***************************************************************************************
; Compare two 4-byte addresses
; 
; Compares bytes at &B0-&B3 against &B4-&B7 using EOR.
; Used by the OSFILE save handler to compare the current
; transfer address (&C8-&CB, copied to &B0) against the end
; address (&B4-&B7) during multi-block file data transfers.
; 
; On Exit:
;     A: corrupted (EOR result)
;     X: corrupted
;     Y: preserved
; ***************************************************************************************
; &864a referenced 2 times by &8743, &87fb
.compare_addresses
    ldx #4                                                            ; 864a: a2 04       ..             ; Compare 4 bytes (index 4,3,2,1)
; &864c referenced 1 time by &8653
.compare_addr_byte
    lda addr_work,x                                                   ; 864c: b5 af       ..             ; Load byte from first address
    eor fs_load_addr_3,x                                              ; 864e: 55 b3       U.             ; XOR with corresponding byte
    bne return_compare                                                ; 8650: d0 03       ..             ; Mismatch: Z=0, return unequal
    dex                                                               ; 8652: ca          .              ; Next byte
    bne compare_addr_byte                                             ; 8653: d0 f7       ..             ; Continue comparing
; &8655 referenced 1 time by &8650
.return_compare
    rts                                                               ; 8655: 60          `              ; Return with Z flag result

.fscv_7_read_handles
    ldx #&20 ; ' '                                                    ; 8656: a2 20       .              ; X=first handle (&20)
    ldy #&27 ; '''                                                    ; 8658: a0 27       .'             ; Y=last handle (&27)
.return_fscv_handles
    rts                                                               ; 865a: 60          `              ; Return (FSCV 7 read handles)

; ***************************************************************************************
; Set bit(s) in FS flags (&0E07)
; 
; ORs A into fs_work_0e07 (EOF hint byte). Each bit represents
; one of up to 8 open file handles. When clear, the file is
; definitely NOT at EOF. When set, the fileserver must be queried
; to confirm EOF status. This negative-cache optimisation avoids
; expensive network round-trips for the common case. The hint is
; cleared when the file pointer is updated (since seeking away
; from EOF invalidates the hint) and set after BGET/OPEN/EOF
; operations that might have reached the end.
; ***************************************************************************************
; &865b referenced 5 times by &854f, &8954, &89a7, &89c7, &8aa6
.set_fs_flag
    ora fs_eof_flags                                                  ; 865b: 0d 07 0e    ...            ; Set EOF hint bit(s) for handle mask
    bne store_fs_flag                                                 ; 865e: d0 05       ..             ; ALWAYS branch to store updated flags
; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
; the specified bits. Falls through to store the result.
; ***************************************************************************************
; &8660 referenced 3 times by &854c, &886e, &8aa3
.clear_fs_flag
    eor #&ff                                                          ; 8660: 49 ff       I.             ; Invert mask for AND clear
    and fs_eof_flags                                                  ; 8662: 2d 07 0e    -..            ; Clear specified bits in flags
; &8665 referenced 1 time by &865e
.store_fs_flag
    sta fs_eof_flags                                                  ; 8665: 8d 07 0e    ...            ; Write back updated flags
    rts                                                               ; 8668: 60          `              ; Return

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &8669 referenced 2 times by &83c0, &883b
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8669: a2 c0       ..             ; X=&C0: TX control block at &00C0
    stx net_tx_ptr                                                    ; 866b: 86 9a       ..             ; Set TX pointer lo
    ldx #0                                                            ; 866d: a2 00       ..             ; X=0: page zero
    stx net_tx_ptr_hi                                                 ; 866f: 86 9b       ..             ; Set TX pointer high = 0 (page zero)
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &8671 referenced 4 times by &901f, &9079, &90d0, &926e
.tx_poll_ff
    lda #&ff                                                          ; 8671: a9 ff       ..             ; A=&FF: full retry count
.tx_poll_timeout
    ldy #&60 ; '`'                                                    ; 8673: a0 60       .`             ; Y=timeout parameter (&60 = standard)
; ***************************************************************************************
; Core transmit and poll routine (XMIT)
; 
; Claims the TX semaphore (tx_ctrl_status) via ASL -- a busy-wait
; spinlock where carry=0 means the semaphore is held by another
; operation. Only after claiming the semaphore is the TX pointer
; copied to nmi_tx_block, ensuring the low-level transmit code
; sees a consistent pointer. Then calls the ADLC TX setup routine
; and polls the control byte for completion:
;   bit 7 set = still busy (loop)
;   bit 6 set = error (check escape or report)
;   bit 6 clear = success (clean return)
; On error, checks for escape condition and handles retries.
; Two entry points: setup_tx_ptr_c0 (&8669) always uses the
; standard TXCB; tx_poll_core (&8675) is general-purpose.
; 
; On Entry:
;     A: retry count (&FF = full retry)
;     Y: timeout parameter (&60 = standard)
; 
; On Exit:
;     A: entry A (retry count, restored from stack)
;     X: 0
;     Y: 0
; ***************************************************************************************
; &8675 referenced 1 time by &905f
.tx_poll_core
    pha                                                               ; 8675: 48          H              ; Save retry count on stack
    tya                                                               ; 8676: 98          .              ; Transfer timeout to A
    pha                                                               ; 8677: 48          H              ; Save timeout on stack
    ldx #0                                                            ; 8678: a2 00       ..             ; X=0 for (net_tx_ptr,X) indirect
    lda (net_tx_ptr,x)                                                ; 867a: a1 9a       ..             ; Load TXCB byte 0 (control/status)
; &867c referenced 1 time by &86af
.tx_retry
    sta (net_tx_ptr,x)                                                ; 867c: 81 9a       ..             ; Write control byte to start TX
    pha                                                               ; 867e: 48          H              ; Save control byte for retry
; &867f referenced 1 time by &8682
.tx_semaphore_spin
    asl tx_clear_flag                                                 ; 867f: 0e 62 0d    .b.            ; Test TX semaphore (C=1 when free)
    bcc tx_semaphore_spin                                             ; 8682: 90 fb       ..             ; Spin until semaphore released
    lda net_tx_ptr                                                    ; 8684: a5 9a       ..             ; Copy TX ptr lo to NMI block
    sta nmi_tx_block                                                  ; 8686: 85 a0       ..             ; Store for NMI handler access
    lda net_tx_ptr_hi                                                 ; 8688: a5 9b       ..             ; Copy TX ptr hi to NMI block
    sta nmi_tx_block_hi                                               ; 868a: 85 a1       ..             ; Store for NMI handler access
    jsr trampoline_tx_setup                                           ; 868c: 20 60 96     `.            ; Initiate ADLC TX via trampoline
; &868f referenced 1 time by &8691
.poll_txcb_status
    lda (net_tx_ptr,x)                                                ; 868f: a1 9a       ..             ; Poll TXCB byte 0 for completion
    bmi poll_txcb_status                                              ; 8691: 30 fc       0.             ; Bit 7 set: still busy, keep polling
    asl a                                                             ; 8693: 0a          .              ; Shift bit 6 into bit 7 (error flag)
    bpl tx_success                                                    ; 8694: 10 1f       ..             ; Bit 6 clear: success, clean return
    asl a                                                             ; 8696: 0a          .              ; Shift bit 5 into carry
    beq tx_not_listening                                              ; 8697: f0 18       ..             ; Zero: fatal error, no escape
    jsr check_escape                                                  ; 8699: 20 2a 85     *.            ; Check for user escape condition
    pla                                                               ; 869c: 68          h              ; Discard saved control byte
    tax                                                               ; 869d: aa          .              ; Save to X for retry delay
    pla                                                               ; 869e: 68          h              ; Restore timeout parameter
    tay                                                               ; 869f: a8          .              ; Back to Y
    pla                                                               ; 86a0: 68          h              ; Restore retry count
    beq tx_not_listening                                              ; 86a1: f0 0e       ..             ; No retries left: report error
    sbc #1                                                            ; 86a3: e9 01       ..             ; Decrement retry count
    pha                                                               ; 86a5: 48          H              ; Save updated retry count
    tya                                                               ; 86a6: 98          .              ; Timeout to A for delay
    pha                                                               ; 86a7: 48          H              ; Save timeout parameter
    txa                                                               ; 86a8: 8a          .              ; Control byte for delay duration
; &86a9 referenced 2 times by &86aa, &86ad
.msdely
    dex                                                               ; 86a9: ca          .              ; Inner delay loop
    bne msdely                                                        ; 86aa: d0 fd       ..             ; Spin until X=0
    dey                                                               ; 86ac: 88          .              ; Outer delay loop
    bne msdely                                                        ; 86ad: d0 fa       ..             ; Continue delay
    beq tx_retry                                                      ; 86af: f0 cb       ..             ; ALWAYS branch

; &86b1 referenced 2 times by &8697, &86a1
.tx_not_listening
    tax                                                               ; 86b1: aa          .              ; Save error code in X
    jmp nlistn                                                        ; 86b2: 4c d8 84    L..            ; Report 'Not listening' error

; &86b5 referenced 1 time by &8694
.tx_success
    pla                                                               ; 86b5: 68          h              ; Discard saved control byte
    pla                                                               ; 86b6: 68          h              ; Discard timeout parameter
    pla                                                               ; 86b7: 68          h              ; Discard retry count
    rts                                                               ; 86b8: 60          `              ; Return (success)

; ***************************************************************************************
; Copy filename pointer to os_text_ptr and parse
; 
; Copies the 2-byte filename pointer from (fs_options),Y into
; os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
; to parse the filename via GSINIT/GSREAD into the &0E30 buffer.
; ***************************************************************************************
; &86b9 referenced 1 time by &86ea
.copy_filename_ptr
    ldy #1                                                            ; 86b9: a0 01       ..             ; Y=1: copy 2 bytes (high then low)
; &86bb referenced 1 time by &86c1
.file1
    lda (fs_options),y                                                ; 86bb: b1 bb       ..             ; Load filename ptr from control block
    sta os_text_ptr,y                                                 ; 86bd: 99 f2 00    ...            ; Store to MOS text pointer (&F2/&F3)
    dey                                                               ; 86c0: 88          .              ; Next byte (descending)
    bpl file1                                                         ; 86c1: 10 f8       ..             ; Loop for both bytes
; ***************************************************************************************
; Parse filename using GSINIT/GSREAD into &0E30
; 
; Uses the MOS GSINIT/GSREAD API to parse a filename string from
; (os_text_ptr),Y, handling quoted strings and |-escaped characters.
; Stores the parsed result CR-terminated at &0E30 and sets up
; fs_crc_lo/hi to point to that buffer. Sub-entry at &86C5 allows
; a non-zero starting Y offset.
; 
; 
; On Entry:
;     Y: offset into (os_text_ptr) buffer (0 at &86C3)
; 
; On Exit:
;     X: length of parsed string
;     Y: preserved
; ***************************************************************************************
; &86c3 referenced 2 times by &8991, &8dc7
.parse_filename_gs
    ldy #0                                                            ; 86c3: a0 00       ..             ; Start from beginning of string
; ***************************************************************************************
; Parse filename via GSINIT/GSREAD from offset Y
; 
; Sub-entry of parse_filename_gs that accepts a non-zero Y offset
; into the (os_text_ptr) string. Initialises GSINIT, reads chars
; via GSREAD into &0E30, CR-terminates the result, and sets up
; fs_crc_lo/hi to point at the buffer.
; ***************************************************************************************
; &86c5 referenced 1 time by &8c11
.parse_filename_gs_y
    ldx #&ff                                                          ; 86c5: a2 ff       ..             ; X=&FF: next INX wraps to first char index
    clc                                                               ; 86c7: 18          .              ; C=0 for GSINIT: parse from current position
    jsr gsinit                                                        ; 86c8: 20 c2 ff     ..            ; Initialise GS string parser
    beq terminate_filename                                            ; 86cb: f0 0b       ..             ; Empty string: skip to CR terminator
; &86cd referenced 1 time by &86d6
.quote1
    jsr gsread                                                        ; 86cd: 20 c5 ff     ..            ; Read next character via GSREAD
    bcs terminate_filename                                            ; 86d0: b0 06       ..             ; C=1 from GSREAD: end of string reached
    inx                                                               ; 86d2: e8          .              ; Advance buffer index
    sta fs_filename_buf,x                                             ; 86d3: 9d 30 0e    .0.            ; Store parsed character to &0E30+X
    bcc quote1                                                        ; 86d6: 90 f5       ..             ; ALWAYS loop (GSREAD clears C on success); ALWAYS branch

; &86d8 referenced 2 times by &86cb, &86d0
.terminate_filename
    inx                                                               ; 86d8: e8          .              ; Terminate parsed string with CR
.tx_result_check
    lda #&0d                                                          ; 86d9: a9 0d       ..             ; CR = &0D
    sta fs_filename_buf,x                                             ; 86db: 9d 30 0e    .0.            ; Store CR terminator at end of string
    lda #&30 ; '0'                                                    ; 86de: a9 30       .0             ; Point fs_crc_lo/hi at &0E30 parse buffer
    sta fs_crc_lo                                                     ; 86e0: 85 be       ..             ; fs_crc_lo = &30
    lda #&0e                                                          ; 86e2: a9 0e       ..             ; fs_crc_hi = &0E → buffer at &0E30
    sta fs_crc_hi                                                     ; 86e4: 85 bf       ..             ; Store high byte
    rts                                                               ; 86e6: 60          `              ; Return; X = string length

; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Calls save_fscv_args (&85AF) to preserve A/X/Y, then JSR &86B9
; to copy the 2-byte filename pointer from the parameter block to
; os_text_ptr and fall through to parse_filename_gs (&86C3) which
; parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
; the parsed filename buffer.
; Dispatches by function code A:
;   A=&FF: load file (send_fs_examine at &86FD)
;   A=&00: save file (filev_save at &8773)
;   A=&01-&06: attribute operations (filev_attrib_dispatch at &8875)
;   Other: restore_args_return (unsupported, no-op)
; 
; On Entry:
;     A: function code (&FF=load, &00=save, &01-&06=attrs)
;     X: parameter block address low byte
;     Y: parameter block address high byte
; 
; On Exit:
;     A: restored
;     X: restored
;     Y: restored
; ***************************************************************************************
.filev_handler
    jsr save_fscv_args                                                ; 86e7: 20 af 85     ..            ; Save A/X/Y in FS workspace
    jsr copy_filename_ptr                                             ; 86ea: 20 b9 86     ..            ; Copy filename ptr from param block to os_text_ptr
    lda fs_last_byte_flag                                             ; 86ed: a5 bd       ..             ; Recover function code from saved A
    bpl saveop                                                        ; 86ef: 10 7d       .}             ; A >= 0: save (&00) or attribs (&01-&06)
    cmp #&ff                                                          ; 86f1: c9 ff       ..             ; A=&FF? Only &FF is valid for load
    beq loadop                                                        ; 86f3: f0 03       ..             ; A=&FF: branch to load path
    jmp restore_args_return                                           ; 86f5: 4c 57 89    LW.            ; Unknown negative code: no-op return

; &86f8 referenced 1 time by &86f3
.loadop
    jsr copy_filename                                                 ; 86f8: 20 4b 8d     K.            ; Copy parsed filename to cmd buffer
    ldy #2                                                            ; 86fb: a0 02       ..             ; Y=2: FS function code offset
; ***************************************************************************************
; Send FS examine command
; 
; Sends FS command &03 (FCEXAM: examine file) to the fileserver.
; Sets &0F02=&03 and error pointer to '*'. Called for OSFILE &FF
; (load file) with the filename already in the command buffer.
; The FS reply contains load/exec addresses and file length which
; are used to set up the data transfer. The header URD field
; is repurposed to carry the Econet data port number (PLDATA=&92)
; for the subsequent block data transfer.
; ***************************************************************************************
; &86fd referenced 1 time by &8ddc
.send_fs_examine
    lda #&92                                                          ; 86fd: a9 92       ..             ; Port &92 = PLDATA (data transfer port)
    sta fs_cmd_urd                                                    ; 86ff: 8d 02 0f    ...            ; Overwrite URD field with data port number
    lda #&2a ; '*'                                                    ; 8702: a9 2a       .*             ; A=&2A: error ptr for retry
    jsr prepare_cmd_clv                                               ; 8704: 20 8a 83     ..            ; Build FS header (V=1: CLV path)
    ldy #6                                                            ; 8707: a0 06       ..             ; Y=6: param block byte 6
    lda (fs_options),y                                                ; 8709: b1 bb       ..             ; Byte 6: use file's own load address?
    bne lodfil                                                        ; 870b: d0 08       ..             ; Non-zero: use FS reply address (lodfil)
    jsr copy_load_addr_from_params                                    ; 870d: 20 d6 87     ..            ; Zero: copy caller's load addr first
    jsr copy_reply_to_params                                          ; 8710: 20 e8 87     ..            ; Then copy FS reply to param block
    bcc skip_lodfil                                                   ; 8713: 90 06       ..             ; Carry clear from prepare_cmd_clv: skip lodfil
; &8715 referenced 1 time by &870b
.lodfil
    jsr copy_reply_to_params                                          ; 8715: 20 e8 87     ..            ; Copy FS reply addresses to param block
    jsr copy_load_addr_from_params                                    ; 8718: 20 d6 87     ..            ; Then copy load addr from param block
; &871b referenced 1 time by &8713
.skip_lodfil
    ldy #4                                                            ; 871b: a0 04       ..             ; Compute end address = load + file length
; &871d referenced 1 time by &8728
.copy_load_end_addr
    lda fs_load_addr,x                                                ; 871d: b5 b0       ..             ; Load address byte
    sta txcb_end,x                                                    ; 871f: 95 c8       ..             ; Store as current transfer position
    adc fs_file_len,x                                                 ; 8721: 7d 0d 0f    }..            ; Add file length byte
    sta fs_work_4,x                                                   ; 8724: 95 b4       ..             ; Store as end position
    inx                                                               ; 8726: e8          .              ; Next address byte
    dey                                                               ; 8727: 88          .              ; Decrement byte counter
    bne copy_load_end_addr                                            ; 8728: d0 f3       ..             ; Loop for all 4 address bytes
    sec                                                               ; 872a: 38          8              ; Adjust high byte for 3-byte length overflow
    sbc fs_file_len_3                                                 ; 872b: ed 10 0f    ...            ; Subtract 4th length byte from end addr
    sta fs_work_7                                                     ; 872e: 85 b7       ..             ; Store adjusted end address high byte
    jsr print_file_info                                               ; 8730: 20 fa 8c     ..            ; Display file info after FS reply
    jsr send_data_blocks                                              ; 8733: 20 43 87     C.            ; Transfer file data in &80-byte blocks
    ldx #2                                                            ; 8736: a2 02       ..             ; Copy 3-byte file length to FS reply cmd buffer
; &8738 referenced 1 time by &873f
.floop
    lda fs_file_len_3,x                                               ; 8738: bd 10 0f    ...            ; Load file length byte
    sta fs_cmd_data,x                                                 ; 873b: 9d 05 0f    ...            ; Store in FS command data buffer
    dex                                                               ; 873e: ca          .              ; Next byte (count down)
    bpl floop                                                         ; 873f: 10 f7       ..             ; Loop for 3 bytes (X=2,1,0)
    bmi send_fs_reply                                                 ; 8741: 30 76       0v             ; ALWAYS branch

; ***************************************************************************************
; Send file data in multi-block chunks
; 
; Repeatedly sends &80-byte (128-byte) blocks of file data to the
; fileserver using command &7F. Compares current address (&C8-&CB)
; against end address (&B4-&B7) via compare_addresses, and loops
; until the entire file has been transferred. Each block is sent
; via send_to_fs_star.
; ***************************************************************************************
; &8743 referenced 2 times by &8733, &8a96
.send_data_blocks
    jsr compare_addresses                                             ; 8743: 20 4a 86     J.            ; Compare two 4-byte addresses
    beq return_lodchk                                                 ; 8746: f0 25       .%             ; Addresses match: transfer complete
    lda #&92                                                          ; 8748: a9 92       ..             ; Port &92 for data block transfer
    sta txcb_port                                                     ; 874a: 85 c1       ..             ; Store port to TXCB command byte
; &874c referenced 1 time by &8768
.send_block_loop
    ldx #3                                                            ; 874c: a2 03       ..             ; Set up next &80-byte block for transfer
; &874e referenced 1 time by &8757
.copy_block_addrs
    lda txcb_end,x                                                    ; 874e: b5 c8       ..             ; Swap: current addr -> source, end -> current
    sta txcb_start,x                                                  ; 8750: 95 c4       ..             ; Source addr = current position
    lda fs_work_4,x                                                   ; 8752: b5 b4       ..             ; Load end address byte
    sta txcb_end,x                                                    ; 8754: 95 c8       ..             ; Dest = end address (will be clamped)
    dex                                                               ; 8756: ca          .              ; Next address byte
    bpl copy_block_addrs                                              ; 8757: 10 f5       ..             ; Loop for all 4 bytes
    lda #&7f                                                          ; 8759: a9 7f       ..             ; Command &7F = data block transfer
    sta txcb_ctrl                                                     ; 875b: 85 c0       ..             ; Store to TXCB control byte
    jsr send_to_fs_star                                               ; 875d: 20 f8 84     ..            ; Send this block to the fileserver
    ldy #3                                                            ; 8760: a0 03       ..             ; Y=3: compare 4 bytes (3..0)
; &8762 referenced 1 time by &876b
.lodchk
    lda txcb_end,y                                                    ; 8762: b9 c8 00    ...            ; Compare current vs end address (4 bytes)
    eor fs_work_4,y                                                   ; 8765: 59 b4 00    Y..            ; XOR with end address byte
    bne send_block_loop                                               ; 8768: d0 e2       ..             ; Not equal: more blocks to send
    dey                                                               ; 876a: 88          .              ; Next byte
    bpl lodchk                                                        ; 876b: 10 f5       ..             ; Loop for all 4 address bytes
; &876d referenced 1 time by &8746
.return_lodchk
    rts                                                               ; 876d: 60          `              ; All equal: transfer complete

; &876e referenced 1 time by &86ef
.saveop
    beq filev_save                                                    ; 876e: f0 03       ..             ; A=0: SAVE handler
    jmp filev_attrib_dispatch                                         ; 8770: 4c 75 88    Lu.            ; A!=0: attribute dispatch (A=1-6)

; ***************************************************************************************
; OSFILE save handler (A=&00)
; 
; Copies 4-byte load/exec/length addresses from the parameter block
; to the FS command buffer, along with the filename. Sends FS
; command &91 with function &14 to initiate the save, then
; calls print_file_info to display the filename being saved.
; Handles both host and Tube-based data sources.
; When receiving the save acknowledgement, the RX low pointer is
; incremented by 1 to skip the command code (CC) byte, which
; indicates the FS type and must be preserved. N.B. this assumes
; the RX buffer does not cross a page boundary.
; ***************************************************************************************
; &8773 referenced 1 time by &876e
.filev_save
    ldx #4                                                            ; 8773: a2 04       ..             ; Process 4 address bytes (load/exec/start/end)
    ldy #&0e                                                          ; 8775: a0 0e       ..             ; Y=&0E: start from end-address in param block
; &8777 referenced 1 time by &8791
.savsiz
    lda (fs_options),y                                                ; 8777: b1 bb       ..             ; Read end-address byte from param block
    sta port_ws_offset,y                                              ; 8779: 99 a6 00    ...            ; Save to port workspace for transfer setup
    jsr sub_4_from_y                                                  ; 877c: 20 f5 87     ..            ; Y = Y-4: point to start-address byte
    sbc (fs_options),y                                                ; 877f: f1 bb       ..             ; end - start = transfer length byte
    sta fs_cmd_csd,y                                                  ; 8781: 99 03 0f    ...            ; Store length byte in FS command buffer
    pha                                                               ; 8784: 48          H              ; Save length byte for param block restore
    lda (fs_options),y                                                ; 8785: b1 bb       ..             ; Read corresponding start-address byte
    sta port_ws_offset,y                                              ; 8787: 99 a6 00    ...            ; Save to port workspace
    pla                                                               ; 878a: 68          h              ; Restore length byte from stack
    sta (fs_options),y                                                ; 878b: 91 bb       ..             ; Replace param block entry with length
    jsr add_5_to_y                                                    ; 878d: 20 e2 87     ..            ; Y = Y+5: advance to next address group
    dex                                                               ; 8790: ca          .              ; Decrement address byte counter
    bne savsiz                                                        ; 8791: d0 e4       ..             ; Loop for all 4 address bytes
    ldy #9                                                            ; 8793: a0 09       ..             ; Copy load/exec addresses to FS command buffer
; &8795 referenced 1 time by &879b
.copy_save_params
    lda (fs_options),y                                                ; 8795: b1 bb       ..             ; Read load/exec address byte from params
    sta fs_cmd_csd,y                                                  ; 8797: 99 03 0f    ...            ; Copy to FS command buffer
    dey                                                               ; 879a: 88          .              ; Next byte (descending)
    bne copy_save_params                                              ; 879b: d0 f8       ..             ; Loop for bytes 9..1
    lda #&91                                                          ; 879d: a9 91       ..             ; Port &91 for save command
    sta fs_cmd_urd                                                    ; 879f: 8d 02 0f    ...            ; Overwrite URD field with port number
    sta fs_error_ptr                                                  ; 87a2: 85 b8       ..             ; Save port &91 for flow control ACK
    ldx #&0b                                                          ; 87a4: a2 0b       ..             ; Append filename at offset &0B in cmd buffer
    jsr copy_string_to_cmd                                            ; 87a6: 20 4d 8d     M.            ; Append filename to cmd buffer at offset X
    ldy #1                                                            ; 87a9: a0 01       ..             ; Y=1: function code for save
    lda #&14                                                          ; 87ab: a9 14       ..             ; A=&14: FS function code for SAVE
    jsr prepare_cmd_clv                                               ; 87ad: 20 8a 83     ..            ; Build header and send FS save command
    jsr print_file_info                                               ; 87b0: 20 fa 8c     ..            ; Display filename being saved
.save_csd_display
    lda fs_cmd_data                                                   ; 87b3: ad 05 0f    ...            ; Load CSD from FS reply
    jsr transfer_file_blocks                                          ; 87b6: 20 fa 87     ..            ; Transfer file data blocks to server
; &87b9 referenced 1 time by &8741
.send_fs_reply
    jsr send_fs_reply_timed                                           ; 87b9: 20 c6 83     ..            ; Send FS reply acknowledgement
.skip_catalogue_msg
    stx fs_reply_cmd                                                  ; 87bc: 8e 08 0f    ...            ; Store reply command for attr decode
    ldy #&0e                                                          ; 87bf: a0 0e       ..             ; Y=&0E: access byte offset in param block
    lda fs_cmd_data                                                   ; 87c1: ad 05 0f    ...            ; Load access byte from FS reply
    jsr decode_attribs_5bit                                           ; 87c4: 20 c4 85     ..            ; Convert FS access to BBC attribute format
    beq direct_attr_copy                                              ; 87c7: f0 03       ..             ; Z=1: first byte, use A directly
; &87c9 referenced 1 time by &87d1
.copy_attr_loop
    lda fs_reply_data,y                                               ; 87c9: b9 f7 0e    ...            ; Load attribute byte from FS reply
; &87cc referenced 1 time by &87c7
.direct_attr_copy
    sta (fs_options),y                                                ; 87cc: 91 bb       ..             ; Store decoded access in param block
    iny                                                               ; 87ce: c8          .              ; Next attribute byte
    cpy #&12                                                          ; 87cf: c0 12       ..             ; Copied all 4 bytes? (Y=&0E..&11)
    bne copy_attr_loop                                                ; 87d1: d0 f6       ..             ; Loop for 4 attribute bytes
    jmp restore_args_return                                           ; 87d3: 4c 57 89    LW.            ; Restore A/X/Y and return to caller

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &87d6 referenced 2 times by &870d, &8718
.copy_load_addr_from_params
    ldy #5                                                            ; 87d6: a0 05       ..             ; Start at offset 5 (top of 4-byte addr)
; &87d8 referenced 1 time by &87e0
.lodrl1
    lda (fs_options),y                                                ; 87d8: b1 bb       ..             ; Read from parameter block
    sta work_ae,y                                                     ; 87da: 99 ae 00    ...            ; Store to local workspace
    dey                                                               ; 87dd: 88          .              ; Next byte (descending)
    cpy #2                                                            ; 87de: c0 02       ..             ; Copy offsets 5,4,3,2 (4 bytes)
    bcs lodrl1                                                        ; 87e0: b0 f6       ..             ; Loop while Y >= 2
; &87e2 referenced 1 time by &878d
.add_5_to_y
    iny                                                               ; 87e2: c8          .              ; Y=3 after loop; add 5 to get Y=8
; &87e3 referenced 1 time by &8a73
.add_4_to_y
    iny                                                               ; 87e3: c8          .              ; INY * 4 = add 4 to Y
    iny                                                               ; 87e4: c8          .              ; Add 1 (of 5) to Y
    iny                                                               ; 87e5: c8          .              ; Add 2 (of 5) to Y
    iny                                                               ; 87e6: c8          .              ; Add 3 (of 5) to Y
    rts                                                               ; 87e7: 60          `              ; Return

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; ***************************************************************************************
; &87e8 referenced 2 times by &8710, &8715
.copy_reply_to_params
    ldy #&0d                                                          ; 87e8: a0 0d       ..             ; Start at offset &0D (top of range)
    txa                                                               ; 87ea: 8a          .              ; First store uses X (attrib byte)
; &87eb referenced 1 time by &87f3
.lodrl2
    sta (fs_options),y                                                ; 87eb: 91 bb       ..             ; Write to parameter block
    lda fs_cmd_urd,y                                                  ; 87ed: b9 02 0f    ...            ; Read next byte from reply buffer
    dey                                                               ; 87f0: 88          .              ; Next byte (descending)
    cpy #2                                                            ; 87f1: c0 02       ..             ; Copy offsets &0D down to 2
    bcs lodrl2                                                        ; 87f3: b0 f6       ..             ; Loop until offset 2 reached
; &87f5 referenced 1 time by &877c
.sub_4_from_y
    dey                                                               ; 87f5: 88          .              ; Y=1 after loop; sub 4 to get Y=&FD
; &87f6 referenced 2 times by &888d, &8a7b
.sub_3_from_y
    dey                                                               ; 87f6: 88          .              ; Subtract 1 (of 3) from Y
    dey                                                               ; 87f7: 88          .              ; Subtract 2 (of 3) from Y
    dey                                                               ; 87f8: 88          .              ; Subtract 3 (of 3) from Y
    rts                                                               ; 87f9: 60          `              ; Return to caller

; ***************************************************************************************
; Multi-block file data transfer
; 
; Manages the transfer of file data in chunks between the local
; machine and the fileserver. Entry conditions: WORK (&B0-&B3) and
; WORK+4 (&B4-&B7) hold the low and high addresses of the data
; being sent/received. Sets up source (&C4-&C7) and destination
; (&C8-&CB) from the FS reply, sends &80-byte (128-byte) blocks
; with command &91, and continues until all data has been
; transferred. Handles address overflow and Tube co-processor
; transfers. For SAVE, WORK+8 holds the port on which to receive
; byte-level ACKs for each data block (flow control).
; ***************************************************************************************
; &87fa referenced 2 times by &87b6, &8a91
.transfer_file_blocks
    pha                                                               ; 87fa: 48          H              ; Save FS command byte on stack
    jsr compare_addresses                                             ; 87fb: 20 4a 86     J.            ; Compare two 4-byte addresses
    beq restore_ay_return                                             ; 87fe: f0 71       .q             ; Addresses equal: nothing to transfer
; &8800 referenced 1 time by &884f
.next_block
    ldx #0                                                            ; 8800: a2 00       ..             ; X=0: clear hi bytes of block size
    ldy #4                                                            ; 8802: a0 04       ..             ; Y=4: process 4 address bytes
    stx fs_reply_cmd                                                  ; 8804: 8e 08 0f    ...            ; Clear block size hi byte 1
    stx fs_load_vector                                                ; 8807: 8e 09 0f    ...            ; Clear block size hi byte 2
    clc                                                               ; 880a: 18          .              ; CLC for ADC in loop
; &880b referenced 1 time by &8818
.block_addr_loop
    lda fs_load_addr,x                                                ; 880b: b5 b0       ..             ; Source = current position
    sta txcb_start,x                                                  ; 880d: 95 c4       ..             ; Store source address byte
    adc fs_func_code,x                                                ; 880f: 7d 06 0f    }..            ; Add block size to current position
    sta txcb_end,x                                                    ; 8812: 95 c8       ..             ; Store dest address byte
    sta fs_load_addr,x                                                ; 8814: 95 b0       ..             ; Advance current position
    inx                                                               ; 8816: e8          .              ; Next address byte
    dey                                                               ; 8817: 88          .              ; Decrement byte counter
    bne block_addr_loop                                               ; 8818: d0 f1       ..             ; Loop for all 4 bytes
    bcs clamp_dest_setup                                              ; 881a: b0 0d       ..             ; Carry: address overflowed, clamp
    sec                                                               ; 881c: 38          8              ; SEC for SBC in overshoot check
; &881d referenced 1 time by &8825
.savchk
    lda fs_load_addr,y                                                ; 881d: b9 b0 00    ...            ; Check if new pos overshot end addr
    sbc fs_work_4,y                                                   ; 8820: f9 b4 00    ...            ; Subtract end address byte
    iny                                                               ; 8823: c8          .              ; Next byte
    dex                                                               ; 8824: ca          .              ; Decrement counter
    bne savchk                                                        ; 8825: d0 f6       ..             ; Loop for 4-byte comparison
    bcc send_block                                                    ; 8827: 90 09       ..             ; C=0: no overshoot, proceed
; &8829 referenced 1 time by &881a
.clamp_dest_setup
    ldx #3                                                            ; 8829: a2 03       ..             ; Overshot: clamp dest to end address
; &882b referenced 1 time by &8830
.clamp_dest_addr
    lda fs_work_4,x                                                   ; 882b: b5 b4       ..             ; Load end address byte
    sta txcb_end,x                                                    ; 882d: 95 c8       ..             ; Replace dest with end address
    dex                                                               ; 882f: ca          .              ; Next byte
    bpl clamp_dest_addr                                               ; 8830: 10 f9       ..             ; Loop for all 4 bytes
; &8832 referenced 1 time by &8827
.send_block
    pla                                                               ; 8832: 68          h              ; Recover original FS command byte
    pha                                                               ; 8833: 48          H              ; Re-push for next iteration
    php                                                               ; 8834: 08          .              ; Save processor flags (C from cmp)
    sta txcb_port                                                     ; 8835: 85 c1       ..             ; Store command byte in TXCB
    lda #&80                                                          ; 8837: a9 80       ..             ; 128-byte block size for data transfer
    sta txcb_ctrl                                                     ; 8839: 85 c0       ..             ; Store size in TXCB control byte
    jsr setup_tx_ptr_c0                                               ; 883b: 20 69 86     i.            ; Point TX ptr to &00C0; transmit
    lda fs_error_ptr                                                  ; 883e: a5 b8       ..             ; ACK port for flow control
    jsr init_tx_ctrl_port                                             ; 8840: 20 54 83     T.            ; Set reply port for ACK receive
    plp                                                               ; 8843: 28          (              ; Restore flags (C=overshoot status)
    bcs restore_ay_return                                             ; 8844: b0 2b       .+             ; C=1: all data sent (overshot), done
    lda #&91                                                          ; 8846: a9 91       ..             ; Command &91 = data block transfer
    sta txcb_port                                                     ; 8848: 85 c1       ..             ; Store command &91 in TXCB
    lda #&2a ; '*'                                                    ; 884a: a9 2a       .*             ; A=&2A: error ptr for retry
    jsr send_to_fs                                                    ; 884c: 20 fa 84     ..            ; Transmit block and wait (BRIANX)
    bne next_block                                                    ; 884f: d0 af       ..             ; More blocks? Loop back
; ***************************************************************************************
; FSCV 1: EOF handler
; 
; Checks whether a file handle has reached end-of-file. Converts
; the handle via handle_to_mask_clc, tests the result against the
; EOF hint byte (&0E07). If the hint bit is clear, returns X=0
; immediately (definitely not at EOF — no network call needed).
; If the hint bit is set, sends FS command &11 (FCEOF) to query
; the fileserver for definitive EOF status. Returns X=&FF if at
; EOF, X=&00 if not. This two-level check avoids an expensive
; network round-trip when the file is known to not be at EOF.
; ***************************************************************************************
.fscv_1_eof
    pha                                                               ; 8851: 48          H              ; Save A (function code)
    txa                                                               ; 8852: 8a          .              ; X = file handle to check
    jsr handle_to_mask_a                                              ; 8853: 20 25 86     %.            ; Convert handle to bitmask in A
    tya                                                               ; 8856: 98          .              ; Y = handle bitmask from conversion
    and fs_eof_flags                                                  ; 8857: 2d 07 0e    -..            ; Local hint: is EOF possible for this handle?
    tax                                                               ; 885a: aa          .              ; X = result of AND (0 = not at EOF)
    beq restore_ay_return                                             ; 885b: f0 14       ..             ; Hint clear: definitely not at EOF
    pha                                                               ; 885d: 48          H              ; Save bitmask for clear_fs_flag
    sty fs_cmd_data                                                   ; 885e: 8c 05 0f    ...            ; Handle byte in FS command buffer
    ldy #&11                                                          ; 8861: a0 11       ..             ; Y=&11: FS function code FCEOF; Y=function code for HDRFN
    ldx #1                                                            ; 8863: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8865: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8868: 68          h              ; Restore bitmask
    ldx fs_cmd_data                                                   ; 8869: ae 05 0f    ...            ; FS reply: non-zero = at EOF
    bne restore_ay_return                                             ; 886c: d0 03       ..             ; At EOF: skip flag clear
    jsr clear_fs_flag                                                 ; 886e: 20 60 86     `.            ; Not at EOF: clear the hint bit
; &8871 referenced 4 times by &87fe, &8844, &885b, &886c
.restore_ay_return
    pla                                                               ; 8871: 68          h              ; Restore A
    ldy fs_block_offset                                               ; 8872: a4 bc       ..             ; Restore Y
    rts                                                               ; 8874: 60          `              ; Return; X=0 (not EOF) or X=&FF (EOF)

; ***************************************************************************************
; FILEV attribute dispatch (A=1-6)
; 
; Dispatches OSFILE operations by function code:
;   A=1: write catalogue info (load/exec/length/attrs) — FS &14
;   A=2: write load address only
;   A=3: write exec address only
;   A=4: write file attributes
;   A=5: read catalogue info, returns type in A — FS &12
;   A=6: delete named object — FS &14 (FCDEL)
;   A>=7: falls through to restore_args_return (no-op)
; Each handler builds the appropriate FS command, sends it to
; the fileserver, and copies the reply into the parameter block.
; The control block layout uses dual-purpose fields: the 'data
; start' field doubles as 'length' and 'data end' doubles as
; 'protection' depending on whether reading or writing attrs.
; ***************************************************************************************
; &8875 referenced 1 time by &8770
.filev_attrib_dispatch
    sta fs_cmd_data                                                   ; 8875: 8d 05 0f    ...            ; Store function code in FS cmd buffer
    cmp #6                                                            ; 8878: c9 06       ..             ; A=6? (delete)
    beq cha6                                                          ; 887a: f0 3f       .?             ; Yes: jump to delete handler
    bcs check_attrib_result                                           ; 887c: b0 48       .H             ; A>=7: unsupported, fall through to return
    cmp #5                                                            ; 887e: c9 05       ..             ; A=5? (read catalogue info)
    beq cha5                                                          ; 8880: f0 52       .R             ; Yes: jump to read info handler
    cmp #4                                                            ; 8882: c9 04       ..             ; A=4? (write attributes only)
    beq cha4                                                          ; 8884: f0 44       .D             ; Yes: jump to write attrs handler
    cmp #1                                                            ; 8886: c9 01       ..             ; A=1? (write all catalogue info)
    beq get_file_protection                                           ; 8888: f0 15       ..             ; Yes: jump to write-all handler
    asl a                                                             ; 888a: 0a          .              ; A=2 or 3: convert to param block offset
    asl a                                                             ; 888b: 0a          .              ; A*4: 2->8, 3->12
    tay                                                               ; 888c: a8          .              ; Y = A*4
    jsr sub_3_from_y                                                  ; 888d: 20 f6 87     ..            ; Y = A*4 - 3 (load addr offset for A=2)
    ldx #3                                                            ; 8890: a2 03       ..             ; X=3: copy 4 bytes
; &8892 referenced 1 time by &8899
.chalp1
    lda (fs_options),y                                                ; 8892: b1 bb       ..             ; Load address byte from param block
    sta fs_func_code,x                                                ; 8894: 9d 06 0f    ...            ; Store to FS cmd data area
    dey                                                               ; 8897: 88          .              ; Next source byte (descending)
    dex                                                               ; 8898: ca          .              ; Next dest byte
    bpl chalp1                                                        ; 8899: 10 f7       ..             ; Loop for 4 bytes
    ldx #5                                                            ; 889b: a2 05       ..             ; X=5: data extent for filename copy
    bne copy_filename_to_cmd                                          ; 889d: d0 15       ..             ; ALWAYS branch

; &889f referenced 1 time by &8888
.get_file_protection
    jsr decode_attribs_6bit                                           ; 889f: 20 ba 85     ..            ; A=1: encode protection from param block
    sta fs_file_attrs                                                 ; 88a2: 8d 0e 0f    ...            ; Store encoded attrs at &0F0E
    ldy #9                                                            ; 88a5: a0 09       ..             ; Y=9: source offset in param block
    ldx #8                                                            ; 88a7: a2 08       ..             ; X=8: dest offset in cmd buffer
; &88a9 referenced 1 time by &88b0
.chalp2
    lda (fs_options),y                                                ; 88a9: b1 bb       ..             ; Load byte from param block
    sta fs_cmd_data,x                                                 ; 88ab: 9d 05 0f    ...            ; Store to FS cmd buffer
    dey                                                               ; 88ae: 88          .              ; Next source byte (descending)
    dex                                                               ; 88af: ca          .              ; Next dest byte
    bne chalp2                                                        ; 88b0: d0 f7       ..             ; Loop until X=0 (8 bytes copied)
    ldx #&0a                                                          ; 88b2: a2 0a       ..             ; X=&0A: data extent past attrs+addrs
; &88b4 referenced 2 times by &889d, &88d2
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 88b4: 20 4d 8d     M.            ; Append filename to cmd buffer
    ldy #&13                                                          ; 88b7: a0 13       ..             ; Y=&13: fn code for FCSAVE (write attrs)
    bne send_fs_cmd_v1                                                ; 88b9: d0 05       ..             ; ALWAYS branch to send command; ALWAYS branch

; &88bb referenced 1 time by &887a
.cha6
    jsr copy_filename                                                 ; 88bb: 20 4b 8d     K.            ; A=6: copy filename (delete)
    ldy #&14                                                          ; 88be: a0 14       ..             ; Y=&14: fn code for FCDEL (delete)
; &88c0 referenced 1 time by &88b9
.send_fs_cmd_v1
    bit tx_ctrl_upper                                                 ; 88c0: 2c 7e 83    ,~.            ; Set V=1 (BIT trick: &B3 has bit 6 set)
    jsr init_tx_ctrl_data                                             ; 88c3: 20 95 83     ..            ; Send via prepare_fs_cmd_v (V=1 path)
; &88c6 referenced 1 time by &887c
.check_attrib_result
    bcs attrib_error_exit                                             ; 88c6: b0 42       .B             ; C=1: &D6 not-found, skip to return
    bcc argsv_check_return                                            ; 88c8: 90 71       .q             ; C=0: success, copy reply to param block; ALWAYS branch

; &88ca referenced 1 time by &8884
.cha4
    jsr decode_attribs_6bit                                           ; 88ca: 20 ba 85     ..            ; A=4: encode attrs from param block
    sta fs_func_code                                                  ; 88cd: 8d 06 0f    ...            ; Store encoded attrs at &0F06
    ldx #2                                                            ; 88d0: a2 02       ..             ; X=2: data extent (1 attr byte + fn)
    bne copy_filename_to_cmd                                          ; 88d2: d0 e0       ..             ; ALWAYS branch to append filename; ALWAYS branch

; &88d4 referenced 1 time by &8880
.cha5
    ldx #1                                                            ; 88d4: a2 01       ..             ; X=1: filename only, no data extent
    jsr copy_string_to_cmd                                            ; 88d6: 20 4d 8d     M.            ; Copy filename to cmd buffer
    ldy #&12                                                          ; 88d9: a0 12       ..             ; Y=&12: fn code for FCEXAM (read info); Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88db: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_obj_type                                                   ; 88de: ad 11 0f    ...            ; Save object type from FS reply
    stx fs_obj_type                                                   ; 88e1: 8e 11 0f    ...            ; Clear reply byte (X=0 on success); X=0 on success, &D6 on not-found
    stx fs_len_clear                                                  ; 88e4: 8e 14 0f    ...            ; Clear length high byte in reply
    jsr decode_attribs_5bit                                           ; 88e7: 20 c4 85     ..            ; Decode 5-bit access byte from FS reply
    ldy #&0e                                                          ; 88ea: a0 0e       ..             ; Y=&0E: attrs offset in param block
    sta (fs_options),y                                                ; 88ec: 91 bb       ..             ; Store decoded attrs at param block +&0E
    dey                                                               ; 88ee: 88          .              ; Y=&0D: start copy below attrs; Y=&0d
    ldx #&0c                                                          ; 88ef: a2 0c       ..             ; X=&0C: copy from reply offset &0C down
; &88f1 referenced 1 time by &88f8
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 88f1: bd 05 0f    ...            ; Load reply byte (load/exec/length)
    sta (fs_options),y                                                ; 88f4: 91 bb       ..             ; Store to param block
    dey                                                               ; 88f6: 88          .              ; Next dest byte (descending)
    dex                                                               ; 88f7: ca          .              ; Next source byte
    bne copy_fs_reply_to_cb                                           ; 88f8: d0 f7       ..             ; Loop until X=0 (12 bytes copied)
    inx                                                               ; 88fa: e8          .              ; X=0 -> X=2 for length high copy
    inx                                                               ; 88fb: e8          .              ; INX again: X=2
    ldy #&11                                                          ; 88fc: a0 11       ..             ; Y=&11: length high dest in param block
; &88fe referenced 1 time by &8905
.cha5lp
    lda fs_access_level,x                                             ; 88fe: bd 12 0f    ...            ; Load length high byte from reply
    sta (fs_options),y                                                ; 8901: 91 bb       ..             ; Store to param block
    dey                                                               ; 8903: 88          .              ; Next dest byte (descending)
    dex                                                               ; 8904: ca          .              ; Next source byte
    bpl cha5lp                                                        ; 8905: 10 f7       ..             ; Loop for 3 length-high bytes
    lda fs_cmd_data                                                   ; 8907: ad 05 0f    ...            ; Return object type in A
; &890a referenced 1 time by &88c6
.attrib_error_exit
    bpl restore_xy_return                                             ; 890a: 10 4d       .M             ; A>=0: branch to restore_args_return
; ***************************************************************************************
; ARGSV handler (OSARGS entry point)
; 
;   A=0, Y=0: return filing system number (10 = network FS)
;   A=0, Y>0: read file pointer via FS command &0A (FCRDSE)
;   A=1, Y>0: write file pointer via FS command &14 (FCWRSE)
;   A>=3 (ensure): silently returns -- NFS has no local write buffer
;      to flush, since all data is sent to the fileserver immediately
; The handle in Y is converted via handle_to_mask_clc. For writes
; (A=1), the carry flag from the mask conversion is used to branch
; to save_args_handle, which records the handle for later use.
; 
; On Entry:
;     A: function code (0=query, 1=write ptr, >=3=ensure)
;     Y: file handle (0=FS-level query, >0=per-file)
; 
; On Exit:
;     A: filing system number if A=0/Y=0 query, else restored
;     X: restored
;     Y: restored
; ***************************************************************************************
.argsv_handler
    jsr save_fscv_args                                                ; 890c: 20 af 85     ..            ; Save A/X/Y registers for later restore
    cmp #3                                                            ; 890f: c9 03       ..             ; Function >= 3?
    bcs restore_args_return                                           ; 8911: b0 44       .D             ; A>=3 (ensure/flush): no-op for NFS
    cpy #0                                                            ; 8913: c0 00       ..             ; Test file handle
    beq argsv_dispatch_a                                              ; 8915: f0 47       .G             ; Y=0: FS-level query, not per-file
    jsr handle_to_mask_clc                                            ; 8917: 20 26 86     &.            ; Convert handle to bitmask
    sty fs_cmd_data                                                   ; 891a: 8c 05 0f    ...            ; Store bitmask as first cmd data byte
    lsr a                                                             ; 891d: 4a          J              ; LSR splits A: C=1 means write (A=1)
    sta fs_func_code                                                  ; 891e: 8d 06 0f    ...            ; Store function code to cmd data byte 2
    bcs save_args_handle                                              ; 8921: b0 1a       ..             ; C=1: write path, copy ptr from caller
    ldy #&0c                                                          ; 8923: a0 0c       ..             ; Y=&0C: FCRDSE (read sequential pointer); Y=function code for HDRFN
    ldx #2                                                            ; 8925: a2 02       ..             ; X=2: 3 data bytes in command; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8927: 20 94 83     ..            ; Build and send FS command; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 892a: 85 bd       ..             ; Clear last-byte flag on success; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 892c: a6 bb       ..             ; X = saved control block ptr low
    ldy #2                                                            ; 892e: a0 02       ..             ; Y=2: copy 3 bytes of file pointer
    sta zp_work_3,x                                                   ; 8930: 95 03       ..             ; Zero high byte of 3-byte pointer
; &8932 referenced 1 time by &8939
.copy_fileptr_reply
    lda fs_cmd_data,y                                                 ; 8932: b9 05 0f    ...            ; Read reply byte from FS cmd data
    sta zp_work_2,x                                                   ; 8935: 95 02       ..             ; Store to caller's control block
    dex                                                               ; 8937: ca          .              ; Next byte (descending)
    dey                                                               ; 8938: 88          .              ; Next source byte
    bpl copy_fileptr_reply                                            ; 8939: 10 f7       ..             ; Loop for all 3 bytes
; &893b referenced 1 time by &88c8
.argsv_check_return
    bcc restore_args_return                                           ; 893b: 90 1a       ..             ; C=0 (read): return to caller
; &893d referenced 1 time by &8921
.save_args_handle
    tya                                                               ; 893d: 98          .              ; Save bitmask for set_fs_flag later
    pha                                                               ; 893e: 48          H              ; Push bitmask
    ldy #3                                                            ; 893f: a0 03       ..             ; Y=3: copy 4 bytes of file pointer
; &8941 referenced 1 time by &8948
.copy_fileptr_to_cmd
    lda zp_work_3,x                                                   ; 8941: b5 03       ..             ; Read caller's pointer byte
    sta fs_data_count,y                                               ; 8943: 99 07 0f    ...            ; Store to FS command data area
    dex                                                               ; 8946: ca          .              ; Next source byte
    dey                                                               ; 8947: 88          .              ; Next destination byte
    bpl copy_fileptr_to_cmd                                           ; 8948: 10 f7       ..             ; Loop for all 4 bytes
    ldy #&0d                                                          ; 894a: a0 0d       ..             ; Y=&0D: FCWRSE (write sequential pointer); Y=function code for HDRFN
    ldx #5                                                            ; 894c: a2 05       ..             ; X=5: 6 data bytes in command; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 894e: 20 94 83     ..            ; Build and send FS command; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 8951: 86 bd       ..             ; Save not-found status from X; X=0 on success, &D6 on not-found
    pla                                                               ; 8953: 68          h              ; Recover bitmask for EOF hint update
    jsr set_fs_flag                                                   ; 8954: 20 5b 86     [.            ; Set EOF hint bit for this handle
; ***************************************************************************************
; Restore arguments and return
; 
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
; fs_block_offset (&BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; ***************************************************************************************
; &8957 referenced 7 times by &86f5, &87d3, &8911, &893b, &89ca, &8a1b, &8e25
.restore_args_return
    lda fs_last_byte_flag                                             ; 8957: a5 bd       ..             ; A = saved function code / command
; &8959 referenced 5 times by &890a, &896a, &8976, &89a1, &89ae
.restore_xy_return
    ldx fs_options                                                    ; 8959: a6 bb       ..             ; X = saved control block ptr low
    ldy fs_block_offset                                               ; 895b: a4 bc       ..             ; Y = saved control block ptr high
    rts                                                               ; 895d: 60          `              ; Return to MOS with registers restored

; &895e referenced 1 time by &8915
.argsv_dispatch_a
    cmp #2                                                            ; 895e: c9 02       ..             ; OSARGS A=2: read filing system
    beq halve_args_a                                                  ; 8960: f0 07       ..             ; A=2: halve to get FS number
    bcs return_a_zero                                                 ; 8962: b0 10       ..             ; A>2: unsupported, return zero
    tay                                                               ; 8964: a8          .              ; Y=A for block copy index
    bne osarg1                                                        ; 8965: d0 05       ..             ; A=1: read command context block
    lda #&0a                                                          ; 8967: a9 0a       ..             ; A=&0A: NFS filing system number
; &8969 referenced 1 time by &8960
.halve_args_a
    lsr a                                                             ; 8969: 4a          J              ; Shared: halve A (A=0 or A=2 paths)
    bne restore_xy_return                                             ; 896a: d0 ed       ..             ; Return with A = FS number or 1
; &896c referenced 2 times by &8965, &8972
.osarg1
    lda fs_cmd_context,y                                              ; 896c: b9 0a 0e    ...            ; Copy command context to caller's block
    sta (fs_options),y                                                ; 896f: 91 bb       ..             ; Store to caller's parameter block
    dey                                                               ; 8971: 88          .              ; Next byte (descending)
    bpl osarg1                                                        ; 8972: 10 f8       ..             ; Loop until all bytes copied
; ***************************************************************************************
; Return with A=0 via register restore
; 
; Loads A=0 and branches (always taken) to the common register
; restore exit at restore_args_return. Used as a shared exit
; point by ARGSV, FINDV, and GBPBV when an operation is
; unsupported or should return zero.
; ***************************************************************************************
; &8974 referenced 4 times by &8962, &8984, &8ab7, &8b54
.return_a_zero
    lda #0                                                            ; 8974: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl restore_xy_return                                             ; 8976: 10 e1       ..             ; ALWAYS branch

; ***************************************************************************************
; FINDV handler (OSFIND entry point)
; 
;   A=0: close file -- delegates to close_handle (&8986)
;   A>0: open file -- modes &40=read, &80=write/update, &C0=read/write
; For open: the mode byte is converted to the fileserver's two-flag
; format by flipping bit 7 (EOR #&80) and shifting. This produces
; Flag 1 (read/write direction) and Flag 2 (create/existing),
; matching the fileserver protocol. After a successful open, the
; new handle's bit is OR'd into the EOF hint byte (marks it as
; "might be at EOF, query the server"), and into the sequence
; number tracking byte for the byte-stream protocol.
; 
; On Entry:
;     A: operation (0=close, &40=read, &80=write, &C0=R/W)
;     X: filename pointer low (open)
;     Y: file handle (close) or filename pointer high (open)
; 
; On Exit:
;     A: handle on open, 0 on close-all, restored on close-one
;     X: restored
;     Y: restored
; ***************************************************************************************
.findv_handler
    jsr save_fscv_args_with_ptrs                                      ; 8978: 20 a5 85     ..            ; Save A/X/Y and set up pointers
    sec                                                               ; 897b: 38          8              ; SEC distinguishes open (A>0) from close
    jsr handle_to_mask                                                ; 897c: 20 27 86     '.            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 897f: aa          .              ; A=preserved
    beq close_handle                                                  ; 8980: f0 2e       ..             ; A=0: close file(s)
    and #&3f ; '?'                                                    ; 8982: 29 3f       )?             ; Valid open modes: &40, &80, &C0 only
    bne return_a_zero                                                 ; 8984: d0 ee       ..             ; Invalid mode bits: return
    txa                                                               ; 8986: 8a          .              ; A = original mode byte
    eor #&80                                                          ; 8987: 49 80       I.             ; Convert MOS mode to FS protocol flags
    asl a                                                             ; 8989: 0a          .              ; ASL: shift mode bits left
    sta fs_cmd_data                                                   ; 898a: 8d 05 0f    ...            ; Flag 1: read/write direction
    rol a                                                             ; 898d: 2a          *              ; ROL: Flag 2 into bit 0
    sta fs_func_code                                                  ; 898e: 8d 06 0f    ...            ; Flag 2: create vs existing file
    jsr parse_filename_gs                                             ; 8991: 20 c3 86     ..            ; Parse filename from command line
    ldx #2                                                            ; 8994: a2 02       ..             ; X=2: copy after 2-byte flags
    jsr copy_string_to_cmd                                            ; 8996: 20 4d 8d     M.            ; Copy filename to FS command buffer
    ldy #6                                                            ; 8999: a0 06       ..             ; Y=6: FS function code FCOPEN
    bit tx_ctrl_upper                                                 ; 899b: 2c 7e 83    ,~.            ; Set V flag from l83b3 bit 6
    jsr init_tx_ctrl_data                                             ; 899e: 20 95 83     ..            ; Build and send FS open command
    bcs restore_xy_return                                             ; 89a1: b0 b6       ..             ; Error: restore and return
    lda fs_cmd_data                                                   ; 89a3: ad 05 0f    ...            ; Load reply handle from FS
    tax                                                               ; 89a6: aa          .              ; X = new file handle
    jsr set_fs_flag                                                   ; 89a7: 20 5b 86     [.            ; Set EOF hint + sequence bits
    txa                                                               ; 89aa: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 89ab: 20 42 86     B.            ; Convert bitmask to handle number (FS2A)
    bne restore_xy_return                                             ; 89ae: d0 a9       ..             ; ALWAYS branch to restore and return
; ***************************************************************************************
; Close file handle(s) (CLOSE)
; 
;   Y=0: close all files — first calls OSBYTE &77 (close SPOOL and
;        EXEC files) to coordinate with the MOS before sending the
;        close-all command to the fileserver. This ensures locally-
;        managed file handles are released before the server-side
;        handles are invalidated, preventing the MOS from writing to
;        a closed spool file.
;   Y>0: close single handle — sends FS close command and clears
;        the handle's bit in both the EOF hint byte and the sequence
;        number tracking byte.
; ***************************************************************************************
; &89b0 referenced 1 time by &8980
.close_handle
    tya                                                               ; 89b0: 98          .              ; A = handle (Y preserved in A); Y=preserved
    bne close_single_handle                                           ; 89b1: d0 07       ..             ; Y>0: close single file
    lda #osbyte_close_spool_exec                                      ; 89b3: a9 77       .w             ; Close SPOOL/EXEC before FS close-all
    jsr osbyte                                                        ; 89b5: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 89b8: a0 00       ..             ; Y=0: close all handles on server
; &89ba referenced 1 time by &89b1
.close_single_handle
    sty fs_cmd_data                                                   ; 89ba: 8c 05 0f    ...            ; Handle byte in FS command buffer
    ldx #1                                                            ; 89bd: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 89bf: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89c1: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 89c4: ad 05 0f    ...            ; Reply handle for flag update
    jsr set_fs_flag                                                   ; 89c7: 20 5b 86     [.            ; Update EOF/sequence tracking bits
; &89ca referenced 1 time by &89ee
.close_opt_return
    bcc restore_args_return                                           ; 89ca: 90 8b       ..             ; C=0: restore A/X/Y and return
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; ***************************************************************************************
.fscv_0_opt
    cpx #4                                                            ; 89cc: e0 04       ..             ; Is it *OPT 4,Y?
    bne check_opt1                                                    ; 89ce: d0 04       ..             ; No: check for *OPT 1
    cpy #4                                                            ; 89d0: c0 04       ..             ; Y must be 0-3 for boot option
    bcc optl1                                                         ; 89d2: 90 0d       ..             ; Y < 4: valid boot option
; &89d4 referenced 1 time by &89ce
.check_opt1
    dex                                                               ; 89d4: ca          .              ; Not *OPT 4: check for *OPT 1
    bne opter1                                                        ; 89d5: d0 05       ..             ; Not *OPT 1 either: bad option
.set_messages_flag
    sty fs_messages_flag                                              ; 89d7: 8c 06 0e    ...            ; Set local messages flag (*OPT 1,Y)
    bcc opt_return                                                    ; 89da: 90 12       ..             ; Return via restore_args_return
; &89dc referenced 1 time by &89d5
.opter1
    lda #7                                                            ; 89dc: a9 07       ..             ; Error index 7 (Bad option)
    jmp nlisne                                                        ; 89de: 4c da 84    L..            ; Generate BRK error

; &89e1 referenced 1 time by &89d2
.optl1
    sty fs_cmd_data                                                   ; 89e1: 8c 05 0f    ...            ; Boot option value in FS command
    ldy #&16                                                          ; 89e4: a0 16       ..             ; Y=&16: FS function code FCOPT; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89e6: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 89e9: a4 bc       ..             ; Restore Y from saved value
    sty fs_boot_option                                                ; 89eb: 8c 05 0e    ...            ; Cache boot option locally
; &89ee referenced 1 time by &89da
.opt_return
    bcc close_opt_return                                              ; 89ee: 90 da       ..             ; Return via restore_args_return
; &89f0 referenced 1 time by &8aab
.adjust_addrs_9
    ldy #9                                                            ; 89f0: a0 09       ..             ; Y=9: adjust 9 address bytes
    jsr adjust_addrs_clc                                              ; 89f2: 20 f7 89     ..            ; Adjust with carry clear
; &89f5 referenced 1 time by &8b9b
.adjust_addrs_1
    ldy #1                                                            ; 89f5: a0 01       ..             ; Y=1: adjust 1 address byte
; &89f7 referenced 1 time by &89f2
.adjust_addrs_clc
    clc                                                               ; 89f7: 18          .              ; C=0 for address adjustment
; ***************************************************************************************
; Bidirectional 4-byte address adjustment
; 
; Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
;   If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
;   If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
; Starting offset X=&FC means it reads from &0E06-&0E09 area.
; Used to convert between absolute and relative file positions.
; ***************************************************************************************
; &89f8 referenced 2 times by &8ab1, &8ba7
.adjust_addrs
    ldx #&fc                                                          ; 89f8: a2 fc       ..             ; X=&FC: index into &0E06 area (wraps to 0)
; &89fa referenced 1 time by &8a0d
.adjust_addr_byte
    lda (fs_options),y                                                ; 89fa: b1 bb       ..             ; Load byte from param block
    bit fs_load_addr_2                                                ; 89fc: 24 b2       $.             ; Test sign of adjustment direction
    bmi subtract_adjust                                               ; 89fe: 30 06       0.             ; Negative: subtract instead
    adc fs_cmd_context,x                                              ; 8a00: 7d 0a 0e    }..            ; Add adjustment value
    jmp gbpbx                                                         ; 8a03: 4c 09 8a    L..            ; Skip to store result

; &8a06 referenced 1 time by &89fe
.subtract_adjust
    sbc fs_cmd_context,x                                              ; 8a06: fd 0a 0e    ...            ; Subtract adjustment value
; &8a09 referenced 1 time by &8a03
.gbpbx
    sta (fs_options),y                                                ; 8a09: 91 bb       ..             ; Store adjusted byte back
    iny                                                               ; 8a0b: c8          .              ; Next param block byte
    inx                                                               ; 8a0c: e8          .              ; Next adjustment byte (X wraps &FC->&00)
    bne adjust_addr_byte                                              ; 8a0d: d0 eb       ..             ; Loop 4 times (X=&FC,&FD,&FE,&FF,done)
    rts                                                               ; 8a0f: 60          `              ; Return (unsupported function)

; ***************************************************************************************
; GBPBV handler (OSGBPB entry point)
; 
;   A=1-4: file read/write operations (handle-based)
;   A=5-8: info queries (disc title, current dir, lib, filenames)
; Calls 1-4 are standard file data transfers via the fileserver.
; Calls 5-8 were a late addition to the MOS spec and are the only
; NFS operations requiring Tube data transfer -- described in the
; original source as "untidy but useful in theory." The data format
; uses length-prefixed strings (<name length><object name>) rather
; than the CR-terminated strings used elsewhere in the FS.
; 
; On Entry:
;     A: call number (1-8)
;     X: parameter block address low byte
;     Y: parameter block address high byte
; 
; On Exit:
;     A: 0 after FS operation, else restored
;     X: restored
;     Y: restored
; ***************************************************************************************
.gbpbv_handler
    jsr save_fscv_args                                                ; 8a10: 20 af 85     ..            ; Save A/X/Y to FS workspace
    tax                                                               ; 8a13: aa          .              ; X = call number for range check
    beq gbpb_invalid_exit                                             ; 8a14: f0 05       ..             ; A=0: invalid, restore and return
    dex                                                               ; 8a16: ca          .              ; Convert to 0-based (A=0..7)
    cpx #8                                                            ; 8a17: e0 08       ..             ; Range check: must be 0-7
    bcc gbpbx1                                                        ; 8a19: 90 03       ..             ; In range: continue to handler
; &8a1b referenced 1 time by &8a14
.gbpb_invalid_exit
    jmp restore_args_return                                           ; 8a1b: 4c 57 89    LW.            ; Out of range: restore args and return

; &8a1e referenced 1 time by &8a19
.gbpbx1
    txa                                                               ; 8a1e: 8a          .              ; Recover 0-based function code
    ldy #0                                                            ; 8a1f: a0 00       ..             ; Y=0: param block byte 0 (file handle)
    pha                                                               ; 8a21: 48          H              ; Save function code on stack
    cmp #4                                                            ; 8a22: c9 04       ..             ; A>=4: info queries, dispatch separately
    bcc gbpbe1                                                        ; 8a24: 90 03       ..             ; A<4: file read/write operations
    jmp osgbpb_info                                                   ; 8a26: 4c cf 8a    L..            ; Dispatch to OSGBPB 5-8 info handler

; &8a29 referenced 1 time by &8a24
.gbpbe1
    lda (fs_options),y                                                ; 8a29: b1 bb       ..             ; Get file handle from param block byte 0
    jsr handle_to_mask_a                                              ; 8a2b: 20 25 86     %.            ; Convert handle to bitmask for EOF flags
    sty fs_cmd_data                                                   ; 8a2e: 8c 05 0f    ...            ; Store handle in FS command data
    ldy #&0b                                                          ; 8a31: a0 0b       ..             ; Y=&0B: start at param block byte 11
    ldx #6                                                            ; 8a33: a2 06       ..             ; X=6: copy 6 bytes of transfer params
; &8a35 referenced 1 time by &8a41
.gbpbf1
    lda (fs_options),y                                                ; 8a35: b1 bb       ..             ; Load param block byte
    sta fs_func_code,x                                                ; 8a37: 9d 06 0f    ...            ; Store to FS command buffer at &0F06+X
    dey                                                               ; 8a3a: 88          .              ; Previous param block byte
    cpy #8                                                            ; 8a3b: c0 08       ..             ; Skip param block offset 8 (the handle)
    bne gbpbx0                                                        ; 8a3d: d0 01       ..             ; Not at handle offset: continue
    dey                                                               ; 8a3f: 88          .              ; Extra DEY to skip handle byte
; &8a40 referenced 1 time by &8a3d
.gbpbx0
.gbpbf2
    dex                                                               ; 8a40: ca          .              ; Decrement copy counter
    bne gbpbf1                                                        ; 8a41: d0 f2       ..             ; Loop for all 6 bytes
    pla                                                               ; 8a43: 68          h              ; Recover function code from stack
    lsr a                                                             ; 8a44: 4a          J              ; LSR: odd=read (C=1), even=write (C=0)
    pha                                                               ; 8a45: 48          H              ; Save function code again (need C later)
    bcc gbpbl1                                                        ; 8a46: 90 01       ..             ; Even (write): X stays 0
    inx                                                               ; 8a48: e8          .              ; Odd (read): X=1
; &8a49 referenced 1 time by &8a46
.gbpbl1
    stx fs_func_code                                                  ; 8a49: 8e 06 0f    ...            ; Store FS direction flag
    ldy #&0b                                                          ; 8a4c: a0 0b       ..             ; Y=&0B: command data extent
    ldx #&91                                                          ; 8a4e: a2 91       ..             ; Command &91=put, &92=get
    pla                                                               ; 8a50: 68          h              ; Recover function code
    pha                                                               ; 8a51: 48          H              ; Save again for later direction check
    beq gbpb_write_path                                               ; 8a52: f0 03       ..             ; Even (write): keep &91 and Y=&0B
    ldx #&92                                                          ; 8a54: a2 92       ..             ; Odd (read): use &92 (get) instead
    dey                                                               ; 8a56: 88          .              ; Read: one fewer data byte in command; Y=&0a
; &8a57 referenced 1 time by &8a52
.gbpb_write_path
    stx fs_cmd_urd                                                    ; 8a57: 8e 02 0f    ...            ; Store port to FS command URD field
    stx fs_error_ptr                                                  ; 8a5a: 86 b8       ..             ; Save port for error recovery
    ldx #8                                                            ; 8a5c: a2 08       ..             ; X=8: command data bytes
    lda fs_cmd_data                                                   ; 8a5e: ad 05 0f    ...            ; Load handle from FS command data
    jsr prepare_cmd_with_flag                                         ; 8a61: 20 84 83     ..            ; Build FS command with handle+flag
    lda fs_load_addr_3                                                ; 8a64: a5 b3       ..             ; Save seq# for byte-stream flow control
    sta fs_sequence_nos                                               ; 8a66: 8d 08 0e    ...            ; Store to FS sequence number workspace
    ldx #4                                                            ; 8a69: a2 04       ..             ; X=4: copy 4 address bytes
; &8a6b referenced 1 time by &8a7f
.gbpbl3
    lda (fs_options),y                                                ; 8a6b: b1 bb       ..             ; Set up source/dest from param block
    sta addr_work,y                                                   ; 8a6d: 99 af 00    ...            ; Store as source address
    sta txcb_pos,y                                                    ; 8a70: 99 c7 00    ...            ; Store as current transfer position
    jsr add_4_to_y                                                    ; 8a73: 20 e3 87     ..            ; Skip 4 bytes to reach transfer length
    adc (fs_options),y                                                ; 8a76: 71 bb       q.             ; Dest = source + length
    sta addr_work,y                                                   ; 8a78: 99 af 00    ...            ; Store as end address
    jsr sub_3_from_y                                                  ; 8a7b: 20 f6 87     ..            ; Back 3 to align for next iteration
    dex                                                               ; 8a7e: ca          .              ; Decrement byte counter
    bne gbpbl3                                                        ; 8a7f: d0 ea       ..             ; Loop for all 4 address bytes
    inx                                                               ; 8a81: e8          .              ; X=1 after loop
; &8a82 referenced 1 time by &8a89
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8a82: bd 03 0f    ...            ; Copy CSD data to command buffer
    sta fs_func_code,x                                                ; 8a85: 9d 06 0f    ...            ; Store at &0F06+X
    dex                                                               ; 8a88: ca          .              ; Decrement counter
    bpl gbpbf3                                                        ; 8a89: 10 f7       ..             ; Loop for X=1,0
    pla                                                               ; 8a8b: 68          h              ; Odd (read): send data to FS first
    bne gbpb_read_path                                                ; 8a8c: d0 08       ..             ; Non-zero: skip write path
    lda fs_cmd_urd                                                    ; 8a8e: ad 02 0f    ...            ; Load port for transfer setup
    jsr transfer_file_blocks                                          ; 8a91: 20 fa 87     ..            ; Transfer data blocks to fileserver
    bne wait_fs_reply                                                 ; 8a94: d0 03       ..             ; Non-zero: branch past error ptr
; &8a96 referenced 1 time by &8a8c
.gbpb_read_path
    jsr send_data_blocks                                              ; 8a96: 20 43 87     C.            ; Read path: receive data blocks from FS
; &8a99 referenced 1 time by &8a94
.wait_fs_reply
    jsr send_fs_reply_timed                                           ; 8a99: 20 c6 83     ..            ; Wait for FS reply command
    lda (fs_options,x)                                                ; 8a9c: a1 bb       ..             ; Load handle mask for EOF flag update
    bit fs_cmd_data                                                   ; 8a9e: 2c 05 0f    ,..            ; Check FS reply: bit 7 = not at EOF
    bmi skip_clear_flag                                               ; 8aa1: 30 03       0.             ; Bit 7 set: not EOF, skip clear
    jsr clear_fs_flag                                                 ; 8aa3: 20 60 86     `.            ; At EOF: clear EOF hint for this handle
; &8aa6 referenced 1 time by &8aa1
.skip_clear_flag
    jsr set_fs_flag                                                   ; 8aa6: 20 5b 86     [.            ; Set EOF hint flag (may be at EOF)
    stx fs_load_addr_2                                                ; 8aa9: 86 b2       ..             ; Direction=0: forward adjustment
    jsr adjust_addrs_9                                                ; 8aab: 20 f0 89     ..            ; Adjust param block addrs by +9 bytes
    dec fs_load_addr_2                                                ; 8aae: c6 b2       ..             ; Direction=&FF: reverse adjustment
    sec                                                               ; 8ab0: 38          8              ; SEC for reverse subtraction
    jsr adjust_addrs                                                  ; 8ab1: 20 f8 89     ..            ; Adjust param block addrs (reverse)
    asl fs_cmd_data                                                   ; 8ab4: 0e 05 0f    ...            ; Shift bit 7 into C for return flag
    jmp return_a_zero                                                 ; 8ab7: 4c 74 89    Lt.            ; Return via restore_args path

; &8aba referenced 1 time by &8aea
.get_disc_title
    ldy #&15                                                          ; 8aba: a0 15       ..             ; Y=&15: function code for disc title; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8abc: 20 94 83     ..            ; Build and send FS command; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8abf: ad 05 0e    ...            ; Load boot option from FS workspace
    sta fs_boot_data                                                  ; 8ac2: 8d 16 0f    ...            ; Store boot option in reply area
    stx fs_load_addr                                                  ; 8ac5: 86 b0       ..             ; X=0: reply data start offset; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8ac7: 86 b1       ..             ; Clear reply buffer high byte
    lda #&12                                                          ; 8ac9: a9 12       ..             ; A=&12: 18 bytes of reply data
    sta fs_load_addr_2                                                ; 8acb: 85 b2       ..             ; Store as byte count for copy
    bne copy_reply_to_caller                                          ; 8acd: d0 4e       .N             ; ALWAYS branch to copy_reply_to_caller; ALWAYS branch

; ***************************************************************************************
; OSGBPB 5-8 info handler (OSINFO)
; 
; Handles the "messy interface tacked onto OSGBPB" (original source).
; Checks whether the destination address is in Tube space by comparing
; the high bytes against TBFLAG. If in Tube space, data must be
; copied via the Tube FIFO registers (with delays to accommodate the
; slow 16032 co-processor) instead of direct memory access.
; ***************************************************************************************
; &8acf referenced 1 time by &8a26
.osgbpb_info
    ldy #4                                                            ; 8acf: a0 04       ..             ; Y=4: check param block byte 4
    lda tx_in_progress                                                ; 8ad1: ad 52 0d    .R.            ; Check if destination is in Tube space
    beq store_tube_flag                                               ; 8ad4: f0 07       ..             ; No Tube: skip Tube address check
    cmp (fs_options),y                                                ; 8ad6: d1 bb       ..             ; Compare Tube flag with addr byte 4
    bne store_tube_flag                                               ; 8ad8: d0 03       ..             ; Mismatch: not Tube space
    dey                                                               ; 8ada: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8adb: f1 bb       ..             ; Y=3: subtract addr byte 3 from flag
; &8add referenced 2 times by &8ad4, &8ad8
.store_tube_flag
    sta rom_svc_num                                                   ; 8add: 85 a9       ..             ; Non-zero = Tube transfer required
; &8adf referenced 1 time by &8ae5
.info2
    lda (fs_options),y                                                ; 8adf: b1 bb       ..             ; Copy param block bytes 1-4 to workspace
    sta fs_last_byte_flag,y                                           ; 8ae1: 99 bd 00    ...            ; Store to &BD+Y workspace area
    dey                                                               ; 8ae4: 88          .              ; Previous byte
    bne info2                                                         ; 8ae5: d0 f8       ..             ; Loop for bytes 3,2,1
    pla                                                               ; 8ae7: 68          h              ; Sub-function: AND #3 of (original A - 4)
    and #3                                                            ; 8ae8: 29 03       ).             ; Mask to 0-3 (OSGBPB 5-8 → 0-3)
    beq get_disc_title                                                ; 8aea: f0 ce       ..             ; A=0 (OSGBPB 5): read disc title
    lsr a                                                             ; 8aec: 4a          J              ; LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)
    beq gbpb6_read_name                                               ; 8aed: f0 02       ..             ; A=0 (OSGBPB 6): read CSD/LIB name
    bcs gbpb8_read_dir                                                ; 8aef: b0 66       .f             ; C=1 (OSGBPB 8): read filenames from dir
; &8af1 referenced 1 time by &8aed
.gbpb6_read_name
    tay                                                               ; 8af1: a8          .              ; Y=0 for CSD or carry for fn code select; Y=function code
    lda fs_csd_handle,y                                               ; 8af2: b9 03 0e    ...            ; Get CSD/LIB/URD handles for FS command
    sta fs_cmd_csd                                                    ; 8af5: 8d 03 0f    ...            ; Store CSD handle in command buffer
    lda fs_lib_handle                                                 ; 8af8: ad 04 0e    ...            ; Load LIB handle from workspace
    sta fs_cmd_lib                                                    ; 8afb: 8d 04 0f    ...            ; Store LIB handle in command buffer
    lda fs_urd_handle                                                 ; 8afe: ad 02 0e    ...            ; Load URD handle from workspace
    sta fs_cmd_urd                                                    ; 8b01: 8d 02 0f    ...            ; Store URD handle in command buffer
    ldx #&12                                                          ; 8b04: a2 12       ..             ; X=&12: buffer extent for command data; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8b06: 8e 01 0f    ...            ; Store X as function code in header
    lda #&0d                                                          ; 8b09: a9 0d       ..             ; &0D = 13 bytes of reply data expected
    sta fs_func_code                                                  ; 8b0b: 8d 06 0f    ...            ; Store reply length in command buffer
    sta fs_load_addr_2                                                ; 8b0e: 85 b2       ..             ; Store as byte count for copy loop
    lsr a                                                             ; 8b10: 4a          J              ; LSR: &0D >> 1 = 6; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8b11: 8d 05 0f    ...            ; Store as command data byte
    clc                                                               ; 8b14: 18          .              ; CLC for standard FS path
    jsr build_send_fs_cmd                                             ; 8b15: 20 ae 83     ..            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8b18: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8b1a: e8          .              ; INX: X=1 after build_send_fs_cmd
    stx fs_load_addr                                                  ; 8b1b: 86 b0       ..             ; Store X as reply start offset
; &8b1d referenced 2 times by &8acd, &8b90
.copy_reply_to_caller
    lda rom_svc_num                                                   ; 8b1d: a5 a9       ..             ; Copy FS reply to caller's buffer
    bne tube_transfer                                                 ; 8b1f: d0 11       ..             ; Non-zero: use Tube transfer path
    ldx fs_load_addr                                                  ; 8b21: a6 b0       ..             ; X = reply start offset
    ldy fs_load_addr_hi                                               ; 8b23: a4 b1       ..             ; Y = reply buffer high byte
; &8b25 referenced 1 time by &8b2e
.copy_reply_bytes
    lda fs_cmd_data,x                                                 ; 8b25: bd 05 0f    ...            ; Load reply data byte
    sta (fs_crc_lo),y                                                 ; 8b28: 91 be       ..             ; Store to caller's buffer
    inx                                                               ; 8b2a: e8          .              ; Next source byte
    iny                                                               ; 8b2b: c8          .              ; Next destination byte
    dec fs_load_addr_2                                                ; 8b2c: c6 b2       ..             ; Decrement remaining bytes
    bne copy_reply_bytes                                              ; 8b2e: d0 f5       ..             ; Loop until all bytes copied
    beq gbpb_done                                                     ; 8b30: f0 22       ."             ; ALWAYS branch to exit; ALWAYS branch

; &8b32 referenced 1 time by &8b1f
.tube_transfer
    jsr tube_claim_loop                                               ; 8b32: 20 ac 8b     ..            ; Claim Tube transfer channel
    lda #1                                                            ; 8b35: a9 01       ..             ; A=1: Tube claim type 1 (write)
    ldx fs_options                                                    ; 8b37: a6 bb       ..             ; X = param block address low
    ldy fs_block_offset                                               ; 8b39: a4 bc       ..             ; Y = param block address high
    inx                                                               ; 8b3b: e8          .              ; INX: advance past byte 0
    bne no_page_wrap                                                  ; 8b3c: d0 01       ..             ; No page wrap: keep Y
    iny                                                               ; 8b3e: c8          .              ; Page wrap: increment high byte
; &8b3f referenced 1 time by &8b3c
.no_page_wrap
    jsr tube_addr_claim                                               ; 8b3f: 20 06 04     ..            ; Claim Tube address for transfer
    ldx fs_load_addr                                                  ; 8b42: a6 b0       ..             ; X = reply data start offset
; &8b44 referenced 1 time by &8b4d
.tbcop1
    lda fs_cmd_data,x                                                 ; 8b44: bd 05 0f    ...            ; Load reply data byte
    sta tube_data_register_3                                          ; 8b47: 8d e5 fe    ...            ; Send byte to Tube via R3
    inx                                                               ; 8b4a: e8          .              ; Next source byte
    dec fs_load_addr_2                                                ; 8b4b: c6 b2       ..             ; Decrement remaining bytes
    bne tbcop1                                                        ; 8b4d: d0 f5       ..             ; Loop until all bytes sent to Tube
    lda #&83                                                          ; 8b4f: a9 83       ..             ; Release Tube after transfer complete
    jsr tube_addr_claim                                               ; 8b51: 20 06 04     ..            ; Release Tube address claim
; &8b54 referenced 2 times by &8b30, &8baa
.gbpb_done
    jmp return_a_zero                                                 ; 8b54: 4c 74 89    Lt.            ; Return via restore_args path

; &8b57 referenced 1 time by &8aef
.gbpb8_read_dir
    ldy #9                                                            ; 8b57: a0 09       ..             ; OSGBPB 8: read filenames from dir
    lda (fs_options),y                                                ; 8b59: b1 bb       ..             ; Byte 9: number of entries to read
    sta fs_func_code                                                  ; 8b5b: 8d 06 0f    ...            ; Store as reply count in command buffer
    ldy #5                                                            ; 8b5e: a0 05       ..             ; Y=5: byte 5 = starting entry number
    lda (fs_options),y                                                ; 8b60: b1 bb       ..             ; Load starting entry number
    sta fs_data_count                                                 ; 8b62: 8d 07 0f    ...            ; Store in command buffer
    ldx #&0d                                                          ; 8b65: a2 0d       ..             ; X=&0D: command data extent; X=preserved through header build
    stx fs_reply_cmd                                                  ; 8b67: 8e 08 0f    ...            ; Store extent in command buffer
    ldy #2                                                            ; 8b6a: a0 02       ..             ; Y=2: function code for dir read
    sty fs_load_addr                                                  ; 8b6c: 84 b0       ..             ; Store 2 as reply data start offset
    sty fs_cmd_data                                                   ; 8b6e: 8c 05 0f    ...            ; Store 2 as command data byte
    iny                                                               ; 8b71: c8          .              ; Y=3: function code for header read; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b72: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b75: 86 b1       ..             ; X=0 after FS command completes; X=0 on success, &D6 on not-found
    lda fs_func_code                                                  ; 8b77: ad 06 0f    ...            ; Load reply entry count
    sta (fs_options,x)                                                ; 8b7a: 81 bb       ..             ; Store at param block byte 0 (X=0)
    lda fs_cmd_data                                                   ; 8b7c: ad 05 0f    ...            ; Load entries-read count from reply
    ldy #9                                                            ; 8b7f: a0 09       ..             ; Y=9: param block byte 9
    adc (fs_options),y                                                ; 8b81: 71 bb       q.             ; Add to starting entry number
    sta (fs_options),y                                                ; 8b83: 91 bb       ..             ; Update param block with new position
    lda txcb_end                                                      ; 8b85: a5 c8       ..             ; Load total reply length
    sbc #7                                                            ; 8b87: e9 07       ..             ; Subtract header (7 bytes) from reply len
    sta fs_func_code                                                  ; 8b89: 8d 06 0f    ...            ; Store adjusted length in command buffer
    sta fs_load_addr_2                                                ; 8b8c: 85 b2       ..             ; Store as byte count for copy loop
    beq skip_copy_reply                                               ; 8b8e: f0 03       ..             ; Zero bytes: skip copy
    jsr copy_reply_to_caller                                          ; 8b90: 20 1d 8b     ..            ; Copy reply data to caller's buffer
; &8b93 referenced 1 time by &8b8e
.skip_copy_reply
    ldx #2                                                            ; 8b93: a2 02       ..             ; X=2: clear 3 bytes
; &8b95 referenced 1 time by &8b99
.zero_cmd_bytes
    sta fs_data_count,x                                               ; 8b95: 9d 07 0f    ...            ; Zero out &0F07+X area
    dex                                                               ; 8b98: ca          .              ; Next byte
    bpl zero_cmd_bytes                                                ; 8b99: 10 fa       ..             ; Loop for X=2,1,0
    jsr adjust_addrs_1                                                ; 8b9b: 20 f5 89     ..            ; Adjust pointer by +1 (one filename read)
    sec                                                               ; 8b9e: 38          8              ; SEC for reverse adjustment
    dec fs_load_addr_2                                                ; 8b9f: c6 b2       ..             ; Reverse adjustment for updated counter
    lda fs_cmd_data                                                   ; 8ba1: ad 05 0f    ...            ; Load entries-read count
    sta fs_func_code                                                  ; 8ba4: 8d 06 0f    ...            ; Store in command buffer
    jsr adjust_addrs                                                  ; 8ba7: 20 f8 89     ..            ; Adjust param block addresses
    beq gbpb_done                                                     ; 8baa: f0 a8       ..             ; Z=1: all done, exit
; &8bac referenced 3 times by &8b32, &8bb1, &8e0e
.tube_claim_loop
    lda #&c3                                                          ; 8bac: a9 c3       ..             ; A=&C3: Tube claim with retry
    jsr tube_addr_claim                                               ; 8bae: 20 06 04     ..            ; Request Tube address claim
    bcc tube_claim_loop                                               ; 8bb1: 90 f9       ..             ; C=0: claim failed, retry
    rts                                                               ; 8bb3: 60          `              ; Tube claimed successfully

; ***************************************************************************************
; FSCV 2/3/4: unrecognised * command handler (DECODE)
; 
; CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text
; against the table
; at &8BE2 using case-insensitive comparison with abbreviation
; support — commands can be shortened with '.' (e.g. "I." for
; "INFO"). The "I." entry is a special fudge placed first in the
; table: since "I." could match multiple commands, it jumps to
; forward_star_cmd to let the fileserver resolve the ambiguity.
; 
; The matching loop compares input characters against table
; entries. On mismatch, it skips to the next entry. On match
; of all table characters, or when '.' abbreviation is found,
; it dispatches via PHA/PHA/RTS to the entry's handler address.
; 
; After matching, adjusts fs_crc_lo/fs_crc_hi to point past
; the matched command text.
; ***************************************************************************************
; &8bb4 referenced 1 time by &827f
.fscv_3_star_cmd
    jsr save_fscv_args_with_ptrs                                      ; 8bb4: 20 a5 85     ..            ; Save A/X/Y and set up command ptr
    ldx #&ff                                                          ; 8bb7: a2 ff       ..             ; X=&FF: table index (pre-incremented)
    stx fs_crflag                                                     ; 8bb9: 86 b9       ..             ; Disable column formatting
; &8bbb referenced 1 time by &8bd6
.scan_cmd_table
    ldy #&ff                                                          ; 8bbb: a0 ff       ..             ; Y=&FF: input index (pre-incremented)
; &8bbd referenced 1 time by &8bc8
.decfir
    iny                                                               ; 8bbd: c8          .              ; Advance input pointer
    inx                                                               ; 8bbe: e8          .              ; Advance table pointer
; &8bbf referenced 1 time by &8bda
.decmor
    lda fs_cmd_match_table,x                                          ; 8bbf: bd e2 8b    ...            ; Load table character
    bmi dispatch_cmd                                                  ; 8bc2: 30 18       0.             ; Bit 7: end of name, dispatch
    eor (fs_crc_lo),y                                                 ; 8bc4: 51 be       Q.             ; XOR input char with table char
    and #&df                                                          ; 8bc6: 29 df       ).             ; Case-insensitive (clear bit 5)
    beq decfir                                                        ; 8bc8: f0 f3       ..             ; Match: continue comparing
    dex                                                               ; 8bca: ca          .              ; Mismatch: back up table pointer
; &8bcb referenced 1 time by &8bcf
.decmin
    inx                                                               ; 8bcb: e8          .              ; Skip to end of table entry
    lda fs_cmd_match_table,x                                          ; 8bcc: bd e2 8b    ...            ; Load table byte
    bpl decmin                                                        ; 8bcf: 10 fa       ..             ; Loop until bit 7 set (end marker)
    lda (fs_crc_lo),y                                                 ; 8bd1: b1 be       ..             ; Check input for '.' abbreviation
    inx                                                               ; 8bd3: e8          .              ; Skip past handler high byte
    cmp #&2e ; '.'                                                    ; 8bd4: c9 2e       ..             ; Is input '.' (abbreviation)?
    bne scan_cmd_table                                                ; 8bd6: d0 e3       ..             ; No: try next table entry
    iny                                                               ; 8bd8: c8          .              ; Yes: skip '.' in input
    dex                                                               ; 8bd9: ca          .              ; Back to handler high byte
    bcs decmor                                                        ; 8bda: b0 e3       ..             ; ALWAYS branch; dispatch via BMI
; &8bdc referenced 1 time by &8bc2
.dispatch_cmd
    pha                                                               ; 8bdc: 48          H              ; Push handler address high byte
    lda cmd_table_entry_1,x                                           ; 8bdd: bd e3 8b    ...            ; Load handler address low byte
    pha                                                               ; 8be0: 48          H              ; Push handler address low byte
    rts                                                               ; 8be1: 60          `              ; Dispatch via RTS (addr-1 on stack)

; ***************************************************************************************
; FS command match table (COMTAB)
; 
; Format: command letters (bit 7 clear), then dispatch address
; as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
; adds 1 to the stored (address-1). Matching is case-insensitive
; (AND &DF) and supports '.' abbreviation (standard Acorn pattern).
; 
; Entries:
;   "I."     → &80B4 (forward_star_cmd) — placed first as a fudge
;              to catch *I. abbreviation before matching *I AM
;   "I AM"   → &807E (i_am_handler: parse station.net, logon)
;   "EX"     → &8BF8 (ex_handler: extended catalogue)
;   "BYE"\r  → &838D (bye_handler: logoff)
;   <catch-all> → &80B4 (forward anything else to FS)
; ***************************************************************************************
; &8be2 referenced 2 times by &8bbf, &8bcc
.fs_cmd_match_table
cmd_table_entry_1 = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8be2: 49 2e       I.             ; Match last char against '.' for *I. abbreviation
; &8be3 referenced 1 time by &8bdd
    equb &80, &b3                                                     ; 8be4: 80 b3       ..
    equs "I AM"                                                       ; 8be6: 49 20 41... I A
    equb &80                                                          ; 8bea: 80          .
    equs "}EX"                                                        ; 8beb: 7d 45 58    }EX
    equb &8b, &f7                                                     ; 8bee: 8b f7       ..
    equs "BYE"                                                        ; 8bf0: 42 59 45    BYE
    equb &0d, &83, &8c, &80, &b3                                      ; 8bf3: 0d 83 8c... ...

; ***************************************************************************************
; *EX handler (extended catalogue)
; 
; Sets &B7=&01 and &B5=&03, then branches into fscv_5_cat at
; &8C0A, bypassing fscv_5_cat's default column setup. &B7=1
; gives one entry per line with full details (vs &B7=3 for *CAT
; which gives multiple files per line).
; ***************************************************************************************
.ex_handler
    ldx #1                                                            ; 8bf8: a2 01       ..             ; X=1: single-entry-per-line mode
    stx fs_work_7                                                     ; 8bfa: 86 b7       ..             ; Store column format selector
    lda #3                                                            ; 8bfc: a9 03       ..             ; A=3: FS function code for EX
    bne init_cat_params                                               ; 8bfe: d0 0a       ..             ; ALWAYS branch

; ***************************************************************************************
; *CAT handler (directory catalogue)
; 
; Sets column width &B6=&14 (20 columns, four files per 80-column
; line) and &B7=&03. The catalogue protocol is multi-step: first
; sends FCUSER (&15: read user environment) to get CSD, disc, and
; library names, then sends FCREAD (&12: examine) repeatedly to
; fetch entries in batches until zero are returned (end of dir).
; The receive buffer abuts the examine request buffer and ends at
; RXBUFE, allowing seamless data handling across request cycles.
; 
; The command code byte in the fileserver reply indicates FS type:
; zero means an old-format FS (client must format data locally),
; non-zero means new-format (server returns pre-formatted strings).
; This enables backward compatibility with older Acorn fileservers.
; 
; Display format:
;   - Station number in parentheses
;   - "Owner" or "Public" access level
;   - Boot option with name (Off/Load/Run/Exec)
;   - Current directory and library paths
;   - Directory entries: CRFLAG (&CF) cycles 0-3 for multi-column
;     layout; at count 0 a newline is printed, others get spaces.
;     *EX sets CRFLAG=&FF to force one entry per line.
; ***************************************************************************************
.fscv_5_cat
    ldx #3                                                            ; 8c00: a2 03       ..             ; X=3: column count for multi-column layout
    stx fs_work_7                                                     ; 8c02: 86 b7       ..             ; CRFLAG=3: first entry will trigger newline
    ldy #0                                                            ; 8c04: a0 00       ..             ; Y=0: initialise column counter
    sty fs_crflag                                                     ; 8c06: 84 b9       ..             ; Clear CRFLAG column counter
    lda #&0b                                                          ; 8c08: a9 0b       ..             ; A=&0B: examine argument count
; &8c0a referenced 1 time by &8bfe
.init_cat_params
    sta fs_work_5                                                     ; 8c0a: 85 b5       ..             ; Store examine argument count
    lda #6                                                            ; 8c0c: a9 06       ..             ; A=6: examine format type in command
    sta fs_cmd_data                                                   ; 8c0e: 8d 05 0f    ...            ; Store format type at &0F05
    jsr parse_filename_gs_y                                           ; 8c11: 20 c5 86     ..            ; Set up command parameter pointers
    ldx #1                                                            ; 8c14: a2 01       ..             ; X=1: copy dir name at cmd offset 1
    jsr copy_string_to_cmd                                            ; 8c16: 20 4d 8d     M.            ; Copy directory name to command buffer
    ldy #&12                                                          ; 8c19: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c1b: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c1e: a2 03       ..             ; X=3: start printing from reply offset 3
    jsr print_reply_bytes                                             ; 8c20: 20 ba 8d     ..            ; Print directory title (10 chars)
    jsr print_inline                                                  ; 8c23: 20 e2 85     ..            ; Print '('
    equs "("                                                          ; 8c26: 28          (

    lda fs_reply_stn                                                  ; 8c27: ad 13 0f    ...            ; Load station number from FS reply
    jsr print_decimal                                                 ; 8c2a: 20 86 8d     ..            ; Print station number as decimal
    jsr print_inline                                                  ; 8c2d: 20 e2 85     ..            ; Print ')     '
    equs ")     "                                                     ; 8c30: 29 20 20... )

    ldx fs_access_level                                               ; 8c36: ae 12 0f    ...            ; Load access level from reply
    bne print_public                                                  ; 8c39: d0 0b       ..             ; Non-zero: Public access
    jsr print_inline                                                  ; 8c3b: 20 e2 85     ..            ; Print 'Owner' + CR
    equs "Owner", &0d                                                 ; 8c3e: 4f 77 6e... Own

    bne cat_print_header                                              ; 8c44: d0 0a       ..             ; ALWAYS branch past 'Owner'
; &8c46 referenced 1 time by &8c39
.print_public
    jsr print_inline                                                  ; 8c46: 20 e2 85     ..            ; Print 'Public' + CR
    equs "Public", &0d                                                ; 8c49: 50 75 62... Pub

; &8c50 referenced 1 time by &8c44
.cat_print_header
    ldy #&15                                                          ; 8c50: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c52: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c55: e8          .              ; X=1: past command code byte
    ldy #&10                                                          ; 8c56: a0 10       ..             ; Y=&10: print 16 characters
    jsr print_reply_counted                                           ; 8c58: 20 bc 8d     ..            ; Print disc/CSD name from reply
    jsr print_inline                                                  ; 8c5b: 20 e2 85     ..            ; Print '    Option '
    equs "    Option "                                                ; 8c5e: 20 20 20...

    lda fs_boot_option                                                ; 8c69: ad 05 0e    ...            ; Load boot option from reply
    tax                                                               ; 8c6c: aa          .              ; X = boot option for name table lookup
    jsr print_hex                                                     ; 8c6d: 20 a5 8d     ..            ; Print boot option as hex digit
    jsr print_inline                                                  ; 8c70: 20 e2 85     ..            ; Print ' ('
    equs " ("                                                         ; 8c73: 20 28        (

    ldy boot_option_strings,x                                         ; 8c75: bc de 8c    ...            ; Y=string offset for this option
; &8c78 referenced 1 time by &8c81
.print_option_char
    lda boot_option_strings,y                                         ; 8c78: b9 de 8c    ...            ; Load next char of option name
    bmi done_option_name                                              ; 8c7b: 30 06       0.             ; Bit 7 set: end of option name
    jsr osasci                                                        ; 8c7d: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8c80: c8          .              ; Next character
    bne print_option_char                                             ; 8c81: d0 f5       ..             ; Continue printing option name
; &8c83 referenced 1 time by &8c7b
.done_option_name
    jsr print_inline                                                  ; 8c83: 20 e2 85     ..            ; Print ')' + CR + 'Dir. '
    equs ")", &0d, "Dir. "                                            ; 8c86: 29 0d 44... ).D

    ldx #&11                                                          ; 8c8d: a2 11       ..             ; X=&11: Dir. name offset in reply
    jsr print_reply_bytes                                             ; 8c8f: 20 ba 8d     ..            ; Print directory name (10 chars)
    jsr print_inline                                                  ; 8c92: 20 e2 85     ..            ; Print '     Lib. ' header
    equs "     Lib. "                                                 ; 8c95: 20 20 20...

    ldx #&1b                                                          ; 8c9f: a2 1b       ..             ; X=&1B: Lib. name offset in reply
    jsr print_reply_bytes                                             ; 8ca1: 20 ba 8d     ..            ; Print library name
    jsr print_inline                                                  ; 8ca4: 20 e2 85     ..            ; Print two CRs (blank line)
    equs &0d, &0d                                                     ; 8ca7: 0d 0d       ..

    sty fs_func_code                                                  ; 8ca9: 8c 06 0f    ...            ; Store next examine start offset
    sty fs_work_4                                                     ; 8cac: 84 b4       ..             ; Save start offset in zero page for loop
    ldx fs_work_5                                                     ; 8cae: a6 b5       ..             ; Load examine arg count for batch size
    stx fs_data_count                                                 ; 8cb0: 8e 07 0f    ...            ; Store as request count at &0F07
; &8cb3 referenced 1 time by &8cdc
.cat_examine_loop
    ldx fs_work_7                                                     ; 8cb3: a6 b7       ..             ; Load column count for display format
    stx fs_cmd_data                                                   ; 8cb5: 8e 05 0f    ...            ; Store column count in command data
    ldx #3                                                            ; 8cb8: a2 03       ..             ; X=3: copy directory name at offset 3
    jsr copy_string_to_cmd                                            ; 8cba: 20 4d 8d     M.            ; Append directory name to examine command
    ldy #3                                                            ; 8cbd: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cbf: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8cc2: ad 05 0f    ...            ; Load entry count from reply
    beq print_newline                                                 ; 8cc5: f0 64       .d             ; Zero entries returned: catalogue done
    ldx #2                                                            ; 8cc7: a2 02       ..             ; X=2: first entry offset in reply
    jsr print_dir_from_offset                                         ; 8cc9: 20 61 8d     a.            ; Print/format this directory entry
    clc                                                               ; 8ccc: 18          .              ; CLC for addition
    lda fs_work_4                                                     ; 8ccd: a5 b4       ..             ; Load current examine start offset
    adc fs_cmd_data                                                   ; 8ccf: 6d 05 0f    m..            ; Add entries returned this batch
    sta fs_func_code                                                  ; 8cd2: 8d 06 0f    ...            ; Update next examine start offset
    sta fs_work_4                                                     ; 8cd5: 85 b4       ..             ; Save updated start offset
    lda fs_work_5                                                     ; 8cd7: a5 b5       ..             ; Reload batch size for next request
    sta fs_data_count                                                 ; 8cd9: 8d 07 0f    ...            ; Store batch size in command buffer
    bne cat_examine_loop                                              ; 8cdc: d0 d5       ..             ; Loop for remaining characters
; Option name encoding: in 3.35, the boot option names ("Off",
; "Load", "Run", "Exec") are scattered through the code rather
; than stored as a contiguous table. They are addressed via
; base+offset from c8cde (&8CDE), whose first four bytes
; (starting with the ROR A opcode &6A) double as the offset table:
;   &6A→&8D48 "Off", &7D→&8D5B "Load",
;   &A5→&8D83 "Run", &18→&8CF6 "Exec"
; Each string is terminated by the next instruction's opcode
; having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).
; &8cde referenced 2 times by &8c75, &8c78
.boot_option_strings
    ror a                                                             ; 8cde: 6a          j              ; Boot option string offset table
    adc l18a5,x                                                       ; 8cdf: 7d a5 18    }..            ; Dual-purpose: offset data + code
    jmp l212e                                                         ; 8ce2: 4c 2e 21    L.!            ; Fallthrough (also boot string 'L.!')

; ***************************************************************************************
; Boot command strings for auto-boot
; 
; The four boot options use OSCLI strings at offsets within page &8C:
;   Option 0 (Off):  offset &F1 → &8CF1 = bare CR (empty command)
;   Option 1 (Load): offset &E2 → &8CE2 = "L.!BOOT" (dual-purpose:
;       the JMP &212E instruction at &8CE2 has opcode &4C='L' and
;       operand bytes &2E='.' &21='!', forming the string "L.!")
;   Option 2 (Run):  offset &E4 → &8CE4 = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset &EA → &8CEA = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the JMP instruction's
; bytes serve double duty as both executable code and ASCII text.
; ***************************************************************************************
.boot_cmd_strings
    equs "BOOT"                                                       ; 8ce5: 42 4f 4f... BOO
    equb &0d                                                          ; 8ce9: 0d          .
    equs "E.!BOOT"                                                    ; 8cea: 45 2e 21... E.!
    equb &0d                                                          ; 8cf1: 0d          .
; ***************************************************************************************
; Boot option → OSCLI string offset table
; 
; Four bytes indexed by the boot option value (0-3). Each byte
; is the low byte of a pointer into page &8C, where the OSCLI
; command string for that boot option lives. See boot_cmd_strings.
; ***************************************************************************************
; &8cf2 referenced 1 time by &8e3b
.boot_option_offsets
    equb &f1                                                          ; 8cf2: f1          .              ; Opt 0 (Off): bare CR
    equb &e2                                                          ; 8cf3: e2          .              ; Opt 1 (Load): L.!BOOT
    equb &e4                                                          ; 8cf4: e4          .              ; Opt 2 (Run): !BOOT
    equb &ea                                                          ; 8cf5: ea          .              ; Opt 3 (Exec): E.!BOOT
    equs "Exec"                                                       ; 8cf6: 45 78 65... Exe            ; Data bytes: boot_cmd_strings 'ec'

; ***************************************************************************************
; Print file catalogue line
; 
; Displays a formatted catalogue entry: filename (padded to 12
; chars with spaces), load address (4 hex bytes at offset 5-2),
; exec address (4 hex bytes at offset 9-6), and file length
; (3 hex bytes at offset &0C-&0A), followed by a newline.
; Data is read from (fs_crc_lo) for the filename and from
; (fs_options) for the numeric fields. Returns immediately
; if fs_messages_flag is zero (no info available).
; ***************************************************************************************
; &8cfa referenced 2 times by &8730, &87b0
.print_file_info
    ldy fs_messages_flag                                              ; 8cfa: ac 06 0e    ...            ; Check if messages enabled
    beq return_5                                                      ; 8cfd: f0 5b       .[             ; Zero: no info to display, return
    ldy #0                                                            ; 8cff: a0 00       ..             ; Y=0: start of filename
    ldx fs_cmd_csd                                                    ; 8d01: ae 03 0f    ...            ; Load CSD handle from reply
    beq next_filename_char                                            ; 8d04: f0 05       ..             ; Zero: no dir prefix needed
    jsr print_dir_from_offset                                         ; 8d06: 20 61 8d     a.            ; Print directory prefix
    bmi print_hex_fields                                              ; 8d09: 30 18       0.             ; ALWAYS: skip to hex field output
; &8d0b referenced 2 times by &8d04, &8d19
.next_filename_char
    lda (fs_crc_lo),y                                                 ; 8d0b: b1 be       ..             ; Load next filename character
    cmp #&0d                                                          ; 8d0d: c9 0d       ..             ; CR: end of filename
    beq pad_filename_spaces                                           ; 8d0f: f0 0a       ..             ; CR found: pad remaining with spaces
    cmp #&20 ; ' '                                                    ; 8d11: c9 20       .              ; Space: end of name field
    beq pad_filename_spaces                                           ; 8d13: f0 06       ..             ; Space found: pad with spaces
    jsr osasci                                                        ; 8d15: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8d18: c8          .              ; Advance to next character
    bne next_filename_char                                            ; 8d19: d0 f0       ..             ; Continue printing filename
; &8d1b referenced 3 times by &8d0f, &8d13, &8d21
.pad_filename_spaces
    jsr print_space                                                   ; 8d1b: 20 44 8d     D.            ; Print space for padding
    iny                                                               ; 8d1e: c8          .              ; Advance column counter
    cpy #&0c                                                          ; 8d1f: c0 0c       ..             ; Reached 12 columns?
    bcc pad_filename_spaces                                           ; 8d21: 90 f8       ..             ; No: continue padding
; &8d23 referenced 1 time by &8d09
.print_hex_fields
    ldy #5                                                            ; 8d23: a0 05       ..             ; Y=5: load address offset (4 bytes)
    jsr print_hex_bytes                                               ; 8d25: 20 39 8d     9.            ; Print load address
    jsr print_exec_and_len                                            ; 8d28: 20 2e 8d     ..            ; Print exec address and file length
; &8d2b referenced 1 time by &8cc5
.print_newline
    jmp osnewl                                                        ; 8d2b: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &8d2e referenced 1 time by &8d28
.print_exec_and_len
    ldy #9                                                            ; 8d2e: a0 09       ..             ; Y=9: exec address offset (4 bytes)
    jsr print_hex_bytes                                               ; 8d30: 20 39 8d     9.            ; Print exec address
    ldy #&0c                                                          ; 8d33: a0 0c       ..             ; Y=&0C: file length offset
    ldx #3                                                            ; 8d35: a2 03       ..             ; X=3: print 3 bytes (24-bit length)
    bne num01                                                         ; 8d37: d0 02       ..             ; ALWAYS branch

; &8d39 referenced 2 times by &8d25, &8d30
.print_hex_bytes
    ldx #4                                                            ; 8d39: a2 04       ..             ; X=4: print 4 hex bytes
; &8d3b referenced 2 times by &8d37, &8d42
.num01
    lda (fs_options),y                                                ; 8d3b: b1 bb       ..             ; Load byte from parameter block
    jsr print_hex                                                     ; 8d3d: 20 a5 8d     ..            ; Print as two hex digits
    dey                                                               ; 8d40: 88          .              ; Next byte (descending)
    dex                                                               ; 8d41: ca          .              ; Count down
    bne num01                                                         ; 8d42: d0 f7       ..             ; Loop until 4 bytes printed
; &8d44 referenced 1 time by &8d1b
.print_space
    lda #&20 ; ' '                                                    ; 8d44: a9 20       .              ; A=space character
    bne print_char_always                                             ; 8d46: d0 70       .p             ; ALWAYS branch

    equs "Off"                                                        ; 8d48: 4f 66 66    Off

; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
; &8d4b referenced 4 times by &80b4, &86f8, &88bb, &8dca
.copy_filename
    ldx #0                                                            ; 8d4b: a2 00       ..             ; Start writing at &0F05 (after cmd header)
; ***************************************************************************************
; Copy string to FS command buffer
; 
; Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
; to &0F05+X, stopping when a CR (&0D) is encountered. The CR
; itself is also copied. Returns with X pointing past the last
; byte written.
; ***************************************************************************************
; &8d4d referenced 6 times by &87a6, &88b4, &88d6, &8996, &8c16, &8cba
.copy_string_to_cmd
    ldy #0                                                            ; 8d4d: a0 00       ..             ; Start copying from offset 0
; &8d4f referenced 1 time by &8d58
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d4f: b1 be       ..             ; Load next byte from source string
    sta fs_cmd_data,x                                                 ; 8d51: 9d 05 0f    ...            ; Store to FS command buffer (&0F05+X)
    inx                                                               ; 8d54: e8          .              ; Advance write position
    iny                                                               ; 8d55: c8          .              ; Advance source pointer
    eor #&0d                                                          ; 8d56: 49 0d       I.             ; XOR with CR: result=0 if byte was CR
    bne copy_string_from_offset                                       ; 8d58: d0 f5       ..             ; Loop until CR copied
; &8d5a referenced 2 times by &8cfd, &8d64
.return_5
    rts                                                               ; 8d5a: 60          `              ; Return; X = next free position in buffer

    equs "Load"                                                       ; 8d5b: 4c 6f 61... Loa

; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by fscv_5_cat to display Dir. and Lib. paths.
; ***************************************************************************************
.fsreply_0_print_dir
    ldx #0                                                            ; 8d5f: a2 00       ..             ; X=0: start from first reply byte
; &8d61 referenced 3 times by &8cc9, &8d06, &8d81
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d61: bd 05 0f    ...            ; Load byte from FS reply buffer
    bmi return_5                                                      ; 8d64: 30 f4       0.             ; Bit 7 set: end of string, return
    bne infol2                                                        ; 8d66: d0 15       ..             ; Non-zero: print character
; ***************************************************************************************
; Print catalogue column separator or newline
; 
; Handles column formatting for *CAT display. On a null byte
; separator, advances the column counter modulo 4: prints a
; 2-space separator between columns, or a CR at column 0.
; Called from fsreply_0_print_dir.
; ***************************************************************************************
.cat_column_separator
    ldy fs_crflag                                                     ; 8d68: a4 b9       ..             ; Null byte: check column counter
    bmi print_cr_separator                                            ; 8d6a: 30 0f       0.             ; Negative: print CR (no columns)
    iny                                                               ; 8d6c: c8          .              ; Advance column counter
    tya                                                               ; 8d6d: 98          .              ; Transfer to A for modulo
    and #3                                                            ; 8d6e: 29 03       ).             ; Modulo 4 columns
    sta fs_crflag                                                     ; 8d70: 85 b9       ..             ; Update column counter
    beq print_cr_separator                                            ; 8d72: f0 07       ..             ; Column 0: start new line
    jsr print_inline                                                  ; 8d74: 20 e2 85     ..            ; Print 2-space column separator
    equs "  "                                                         ; 8d77: 20 20

    bne next_dir_entry                                                ; 8d79: d0 05       ..             ; More entries: skip final newline
; &8d7b referenced 2 times by &8d6a, &8d72
.print_cr_separator
    lda #&0d                                                          ; 8d7b: a9 0d       ..             ; A=CR: print newline separator
; &8d7d referenced 1 time by &8d66
.infol2
    jsr osasci                                                        ; 8d7d: 20 e3 ff     ..            ; Write character 13
; &8d80 referenced 1 time by &8d79
.next_dir_entry
    inx                                                               ; 8d80: e8          .              ; Next byte in reply buffer
    bne print_dir_from_offset                                         ; 8d81: d0 de       ..             ; Loop until end of buffer
    equs "Run"                                                        ; 8d83: 52 75 6e    Run

; ***************************************************************************************
; Print byte as 3-digit decimal number
; 
; Prints A as a decimal number using repeated subtraction
; for each digit position (100, 10, 1). Leading zeros are
; printed (no suppression). Used to display station numbers.
; 
; On Entry:
;     A: byte value to print
; 
; On Exit:
;     A: last digit character
;     X: corrupted
;     Y: 0 (remainder after last division)
; ***************************************************************************************
; &8d86 referenced 2 times by &8238, &8c2a
.print_decimal
    tay                                                               ; 8d86: a8          .              ; Y = value to print
    lda #&64 ; 'd'                                                    ; 8d87: a9 64       .d             ; Divisor = 100 (hundreds digit)
    jsr print_decimal_digit                                           ; 8d89: 20 93 8d     ..            ; Print hundreds digit
    lda #&0a                                                          ; 8d8c: a9 0a       ..             ; Divisor = 10 (tens digit)
    jsr print_decimal_digit                                           ; 8d8e: 20 93 8d     ..            ; Print tens digit
    lda #1                                                            ; 8d91: a9 01       ..             ; Divisor = 1; fall through to units
; ***************************************************************************************
; Print one decimal digit by repeated subtraction
; 
; Divides Y by A using repeated subtraction. Prints the
; quotient as an ASCII digit ('0'-'9') via OSASCI. Returns
; with the remainder in Y. X starts at &2F ('0'-1) and
; increments once per subtraction, giving the ASCII digit
; directly.
; 
; On Entry:
;     A: divisor (stored to &B8)
;     Y: dividend
; 
; On Exit:
;     Y: remainder
; ***************************************************************************************
; &8d93 referenced 2 times by &8d89, &8d8e
.print_decimal_digit
    sta fs_error_ptr                                                  ; 8d93: 85 b8       ..             ; Save divisor to workspace
    tya                                                               ; 8d95: 98          .              ; A = dividend (from Y)
    ldx #&2f ; '/'                                                    ; 8d96: a2 2f       ./             ; X = &2F = ASCII '0' - 1
    sec                                                               ; 8d98: 38          8              ; Prepare for subtraction
; &8d99 referenced 1 time by &8d9c
.divide_subtract
    inx                                                               ; 8d99: e8          .              ; Count one subtraction (next digit value)
    sbc fs_error_ptr                                                  ; 8d9a: e5 b8       ..             ; A = A - divisor
    bcs divide_subtract                                               ; 8d9c: b0 fb       ..             ; Loop while A >= 0 (borrow clear)
    adc fs_error_ptr                                                  ; 8d9e: 65 b8       e.             ; Undo last subtraction: A = remainder
    tay                                                               ; 8da0: a8          .              ; Y = remainder for caller
    txa                                                               ; 8da1: 8a          .              ; A = X = ASCII digit character
; &8da2 referenced 1 time by &8db8
.print_digit
    jmp osasci                                                        ; 8da2: 4c e3 ff    L..            ; Write character

; ***************************************************************************************
; Print byte as two hex digits
; 
; Prints the high nibble first (via 4× LSR), then the low
; nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
; and output via OSASCI.
; ***************************************************************************************
; &8da5 referenced 2 times by &8c6d, &8d3d
.print_hex
    pha                                                               ; 8da5: 48          H              ; Save byte for low nibble
    lsr a                                                             ; 8da6: 4a          J              ; Shift high nibble to low position
    lsr a                                                             ; 8da7: 4a          J              ; Shift high nibble to low position
    lsr a                                                             ; 8da8: 4a          J              ; Shift high nibble to low position
    lsr a                                                             ; 8da9: 4a          J              ; Shift high nibble to low position
    jsr print_hex_nibble                                              ; 8daa: 20 b0 8d     ..            ; Print high nibble as hex digit
    pla                                                               ; 8dad: 68          h              ; Restore original byte
    and #&0f                                                          ; 8dae: 29 0f       ).             ; Mask to low nibble
; &8db0 referenced 1 time by &8daa
.print_hex_nibble
    ora #&30 ; '0'                                                    ; 8db0: 09 30       .0             ; Convert to ASCII '0' base
    cmp #&3a ; ':'                                                    ; 8db2: c9 3a       .:             ; Above '9'?
    bcc print_char_always                                             ; 8db4: 90 02       ..             ; No: digit 0-9, skip adjustment
    adc #6                                                            ; 8db6: 69 06       i.             ; Add 7 (6+C) for 'A'-'F'
; &8db8 referenced 2 times by &8d46, &8db4
.print_char_always
    bne print_digit                                                   ; 8db8: d0 e8       ..             ; ALWAYS branch to print character
; ***************************************************************************************
; Print reply buffer bytes
; 
; Prints Y characters from the FS reply buffer (&0F05+X) to
; the screen via OSASCI. X = starting offset, Y = count.
; Used by fscv_5_cat to display directory and library names.
; ***************************************************************************************
; &8dba referenced 3 times by &8c20, &8c8f, &8ca1
.print_reply_bytes
    ldy #&0a                                                          ; 8dba: a0 0a       ..             ; Y=10: character count
; &8dbc referenced 2 times by &8c58, &8dc4
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8dbc: bd 05 0f    ...            ; Load byte from FS reply buffer
    jsr osasci                                                        ; 8dbf: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8dc2: e8          .              ; Next buffer offset
    dey                                                               ; 8dc3: 88          .              ; Decrement character counter
    bne print_reply_counted                                           ; 8dc4: d0 f6       ..             ; Loop until all chars printed
    rts                                                               ; 8dc6: 60          `              ; Return to caller

; ***************************************************************************************
; FSCV 2/4: */ (run) and *RUN handler
; 
; Parses the filename via parse_filename_gs and copies it into
; the command buffer, then falls through to fsreply_4_notify_exec
; to send the FS load-as-command request.
; ***************************************************************************************
.fscv_2_star_run
    jsr parse_filename_gs                                             ; 8dc7: 20 c3 86     ..            ; Parse filename from command line
    jsr copy_filename                                                 ; 8dca: 20 4b 8d     K.            ; Copy filename to FS command buffer
; ***************************************************************************************
; Send FS load-as-command and execute response
; 
; Sets up an FS command with function code &05 (FCCMND: load as
; command) using send_fs_examine. If a Tube co-processor is
; present (tx_in_progress != 0), transfers the response data
; to the Tube via tube_addr_claim. Otherwise jumps via the
; indirect pointer at (&0F09) to execute at the load address.
; ***************************************************************************************
.fsreply_4_notify_exec
    ldx #&0e                                                          ; 8dcd: a2 0e       ..             ; X=&0E: FS command buffer offset
    stx fs_block_offset                                               ; 8dcf: 86 bc       ..             ; Store block offset for FS command
    lda #&10                                                          ; 8dd1: a9 10       ..             ; A=&10: 16 bytes of command data
    sta fs_options                                                    ; 8dd3: 85 bb       ..             ; Store options byte
    sta fs_work_16                                                    ; 8dd5: 8d 16 0e    ...            ; Store to FS workspace
    ldx #&4a ; 'J'                                                    ; 8dd8: a2 4a       .J             ; X=&4A: TXCB size for load command
    ldy #5                                                            ; 8dda: a0 05       ..             ; Y=5: FCCMND (load as command)
    jsr send_fs_examine                                               ; 8ddc: 20 fd 86     ..            ; Send FS examine/load command
    ldy #0                                                            ; 8ddf: a0 00       ..             ; Y=0: init GSINIT string offset
    clc                                                               ; 8de1: 18          .              ; CLC: no flags for GSINIT
    jsr gsinit                                                        ; 8de2: 20 c2 ff     ..            ; Init string scanning state
; &8de5 referenced 1 time by &8de8
.gsread_scan_loop
    jsr gsread                                                        ; 8de5: 20 c5 ff     ..            ; Read next char via GSREAD
    bcc gsread_scan_loop                                              ; 8de8: 90 fb       ..             ; More chars: continue scanning
    dey                                                               ; 8dea: 88          .              ; Back up Y to last valid char
; &8deb referenced 1 time by &8df0
.skip_filename_spaces
    iny                                                               ; 8deb: c8          .              ; Advance past current position
    lda (os_text_ptr),y                                               ; 8dec: b1 f2       ..             ; Read char from command line
    cmp #&20 ; ' '                                                    ; 8dee: c9 20       .              ; Is it a space?
    beq skip_filename_spaces                                          ; 8df0: f0 f9       ..             ; Skip leading spaces in filename
    clc                                                               ; 8df2: 18          .              ; CLC for pointer addition
    tya                                                               ; 8df3: 98          .              ; A = Y (offset past spaces)
    adc os_text_ptr                                                   ; 8df4: 65 f2       e.             ; Add base pointer to get abs addr
    sta fs_cmd_context                                                ; 8df6: 8d 0a 0e    ...            ; Store filename pointer (low)
    lda os_text_ptr_hi                                                ; 8df9: a5 f3       ..             ; Load text pointer high byte
    adc #0                                                            ; 8dfb: 69 00       i.             ; Add carry from low byte addition
    sta fs_context_hi                                                 ; 8dfd: 8d 0b 0e    ...            ; Store filename pointer (high)
    sec                                                               ; 8e00: 38          8              ; SEC for address range test
    lda tx_in_progress                                                ; 8e01: ad 52 0d    .R.            ; Check for Tube co-processor
    beq exec_at_load_addr                                             ; 8e04: f0 14       ..             ; No Tube: execute locally
    adc fs_load_upper                                                 ; 8e06: 6d 0b 0f    m..            ; Check load address upper bytes
    adc fs_addr_check                                                 ; 8e09: 6d 0c 0f    m..            ; Continue address range check
    bcs exec_at_load_addr                                             ; 8e0c: b0 0c       ..             ; Carry set: not Tube space, exec locally
    jsr tube_claim_loop                                               ; 8e0e: 20 ac 8b     ..            ; Claim Tube transfer channel
    ldx #9                                                            ; 8e11: a2 09       ..             ; X=9: source offset in FS reply
    ldy #&0f                                                          ; 8e13: a0 0f       ..             ; Y=&0F: page &0F (FS command buffer)
    lda #4                                                            ; 8e15: a9 04       ..             ; A=4: Tube transfer type 4 (256-byte)
    jmp tube_addr_claim                                               ; 8e17: 4c 06 04    L..            ; Transfer data to Tube co-processor

; &8e1a referenced 2 times by &8e04, &8e0c
.exec_at_load_addr
    jmp (fs_load_vector)                                              ; 8e1a: 6c 09 0f    l..            ; Execute at load address via indirect JMP

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to JMP restore_args_return if Y is non-zero.
; ***************************************************************************************
.fsreply_5_set_lib
    sty fs_lib_handle                                                 ; 8e1d: 8c 04 0e    ...            ; Save library handle from FS reply
    bne jmp_restore_args                                              ; 8e20: d0 03       ..             ; Non-zero: jump to restore exit
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to JMP restore_args_return.
; ***************************************************************************************
.fsreply_3_set_csd
    sty fs_csd_handle                                                 ; 8e22: 8c 03 0e    ...            ; Store CSD handle from FS reply
; &8e25 referenced 2 times by &8e20, &8e36
.jmp_restore_args
    jmp restore_args_return                                           ; 8e25: 4c 57 89    LW.            ; Restore A/X/Y and return to caller

; ***************************************************************************************
; Copy FS reply handles to workspace and execute boot command
; 
; SEC entry (LOGIN): copies 4 bytes from &0F05-&0F08 (FS reply) to
; &0E02-&0E05 (URD, CSD, LIB handles and boot option), then
; looks up the boot option in boot_option_offsets to get the
; OSCLI command string and executes it via JMP oscli.
; The carry flag distinguishes LOGIN (SEC) from SDISC (CLC) — both
; share the handle-copying code, but only LOGIN executes the boot
; command. This use of the carry flag to select behaviour between
; two callers avoids duplicating the handle-copy loop.
; ***************************************************************************************
.fsreply_1_copy_handles_boot
    sec                                                               ; 8e28: 38          8              ; Set carry: LOGIN path (copy + boot)
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to jmp_restore_args.
; Called when the FS reply contains updated handle values
; but no boot action is needed.
; ***************************************************************************************
.fsreply_2_copy_handles
    ldx #3                                                            ; 8e29: a2 03       ..             ; Copy 4 bytes: boot option + 3 handles
    bcc copy_handles_loop                                             ; 8e2b: 90 06       ..             ; SDISC: skip boot option, copy handles only
; &8e2d referenced 1 time by &8e34
.logon2
    lda fs_cmd_data,x                                                 ; 8e2d: bd 05 0f    ...            ; Load from FS reply (&0F05+X)
    sta fs_urd_handle,x                                               ; 8e30: 9d 02 0e    ...            ; Store to handle workspace (&0E02+X)
; &8e33 referenced 1 time by &8e2b
.copy_handles_loop
    dex                                                               ; 8e33: ca          .              ; Next handle (descending)
    bpl logon2                                                        ; 8e34: 10 f7       ..             ; Loop while X >= 0
    bcc jmp_restore_args                                              ; 8e36: 90 ed       ..             ; SDISC: done, restore args and return
; ***************************************************************************************
; Execute boot command via OSCLI
; 
; Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
; path). Reads the boot option from fs_boot_option (&0E05),
; looks up the OSCLI command string offset from boot_option_offsets+1,
; and executes the boot command via JMP oscli with page &8D.
; ***************************************************************************************
.boot_cmd_execute
    ldy fs_boot_option                                                ; 8e38: ac 05 0e    ...            ; Y = boot option from FS workspace
    ldx boot_option_offsets,y                                         ; 8e3b: be f2 8c    ...            ; X = command string offset from table
    ldy #&8c                                                          ; 8e3e: a0 8c       ..             ; Y = &8D (high byte of command address)
    jmp oscli                                                         ; 8e40: 4c f7 ff    L..            ; Execute boot command string via OSCLI

; ***************************************************************************************
; *NET1: read file handle from received packet
; 
; Reads a file handle byte from offset &6F in the RX buffer
; (net_rx_ptr), stores it in &F0, then returns.
; ***************************************************************************************
.net_1_read_handle
    ldy #&6f ; 'o'                                                    ; 8e43: a0 6f       .o             ; Y=&6F: offset to handle byte in RX buf
    lda (net_rx_ptr),y                                                ; 8e45: b1 9c       ..             ; Load file handle from RX buffer
    sta osword_pb_ptr                                                 ; 8e47: 85 f0       ..             ; Store in parameter block pointer (&F0)
    rts                                                               ; 8e49: 60          `              ; Return to caller

; ***************************************************************************************
; Load handle from &F0 and calculate workspace offset
; 
; Loads the file handle byte from &F0, then falls through to
; calc_handle_offset which converts handle * 12 to a workspace
; byte offset. Validates offset < &48.
; ***************************************************************************************
; &8e4a referenced 2 times by &8e5e, &8e6e
.load_handle_calc_offset
    lda osword_pb_ptr                                                 ; 8e4a: a5 f0       ..             ; Load handle from &F0
; ***************************************************************************************
; Calculate handle workspace offset
; 
; Converts a file handle number (in A) to a byte offset (in Y)
; into the NFS handle workspace. The calculation is A*12:
;   ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
;   ADC stack (A*8 + A*4 = A*12).
; Validates that the offset is < &48 (max 6 handles × 12 bytes
; per handle entry = 72 bytes). If invalid (>= &48), returns
; with C set and Y=0, A=0 as an error indicator.
; ***************************************************************************************
; &8e4c referenced 3 times by &82f9, &8f7f, &8f98
.calc_handle_offset
    asl a                                                             ; 8e4c: 0a          .              ; A = handle * 2
    asl a                                                             ; 8e4d: 0a          .              ; A = handle * 4
    pha                                                               ; 8e4e: 48          H              ; Push handle*4 onto stack
    asl a                                                             ; 8e4f: 0a          .              ; A = handle * 8
    tsx                                                               ; 8e50: ba          .              ; X = stack pointer
    adc l0101,x                                                       ; 8e51: 7d 01 01    }..            ; A = handle*8 + handle*4 = handle*12
    tay                                                               ; 8e54: a8          .              ; Y = offset into handle workspace
    pla                                                               ; 8e55: 68          h              ; Clean up stack (discard handle*4)
    cmp #&48 ; 'H'                                                    ; 8e56: c9 48       .H             ; Offset >= &48? (6 handles max)
    bcc return_6                                                      ; 8e58: 90 03       ..             ; Valid: return with C clear
    ldy #0                                                            ; 8e5a: a0 00       ..             ; Invalid: Y = 0
    tya                                                               ; 8e5c: 98          .              ; A = 0, C set (error); A=&00
; &8e5d referenced 1 time by &8e58
.return_6
.return_calc_handle
    rts                                                               ; 8e5d: 60          `              ; Return after calculation

; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears fs_temp_ce on exit.
; ***************************************************************************************
.net_2_read_handle_entry
    jsr load_handle_calc_offset                                       ; 8e5e: 20 4a 8e     J.            ; Look up handle &F0 in workspace
    bcs rxpol2                                                        ; 8e61: b0 06       ..             ; Invalid handle: return 0
    lda (nfs_workspace),y                                             ; 8e63: b1 9e       ..             ; Load stored handle value
    cmp #&3f ; '?'                                                    ; 8e65: c9 3f       .?             ; &3F = unused/closed slot marker
    bne store_handle_return                                           ; 8e67: d0 02       ..             ; Slot in use: return actual value
; &8e69 referenced 2 times by &8e61, &8e71
.rxpol2
    lda #0                                                            ; 8e69: a9 00       ..             ; Return 0 for closed/invalid handle
; &8e6b referenced 1 time by &8e67
.store_handle_return
    sta osword_pb_ptr                                                 ; 8e6b: 85 f0       ..             ; Store result back to &F0
    rts                                                               ; 8e6d: 60          `              ; Return

; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears fs_temp_ce on exit.
; ***************************************************************************************
.net_3_close_handle
    jsr load_handle_calc_offset                                       ; 8e6e: 20 4a 8e     J.            ; Look up handle &F0 in workspace
    bcs rxpol2                                                        ; 8e71: b0 f6       ..             ; Invalid handle: return 0
    rol rx_flags                                                      ; 8e73: 2e 64 0d    .d.            ; Preserve carry via ROL
    lda #&3f ; '?'                                                    ; 8e76: a9 3f       .?             ; A=&3F: handle closed/unused marker
    sta (nfs_workspace),y                                             ; 8e78: 91 9e       ..             ; Mark handle as closed in workspace
; ***************************************************************************************
; Restore RX flags after close handle
; 
; Performs ROR on rx_flags to restore the carry flag state
; that was preserved by the matching ROL in net_3_close_handle.
; Falls through to osword_12_handler (clearing fs_temp_ce).
; ***************************************************************************************
.restore_rx_flags
osword_12_handler = restore_rx_flags+2
    ror rx_flags                                                      ; 8e7a: 6e 64 0d    nd.            ; Restore carry via ROR
; ***************************************************************************************
; OSWORD &12 handler: read/set state information (RS)
; 
; Dispatches on the sub-function code (0-9):
;   0: read FS station (FSLOCN at &0E00)
;   1: set FS station
;   2: read printer server station (PSLOCN)
;   3: set printer server station
;   4: read protection masks (LSTAT at &D63)
;   5: set protection masks
;   6: read context handles (URD/CSD/LIB, converted from
;      internal single-bit form back to handle numbers)
;   7: set context handles (converted to internal form)
;   8: read local station number
;   9: read JSR arguments buffer size
; Even-numbered sub-functions read; odd-numbered ones write.
; Uses the bidirectional copy at &8EB1 for station read/set.
; ***************************************************************************************
    rts                                                               ; 8e7d: 60          `              ; Return

; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at &8E88.
; ***************************************************************************************
.svc_8_osword
    lda osbyte_a_copy                                                 ; 8e7e: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8e80: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_7                                                      ; 8e82: 30 3b       0;             ; Outside our OSWORD range, exit
    cmp #5                                                            ; 8e84: c9 05       ..             ; Only OSWORDs &0F-&13 (index 0-4)
    bcs return_7                                                      ; 8e86: b0 37       .7             ; Index >= 5: not ours, return
; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
; at &8EA7 (low) / &8EAC (high).
; ***************************************************************************************
.fs_osword_dispatch
    tax                                                               ; 8e88: aa          .              ; X = sub-function code for table lookup
    lda #&8f                                                          ; 8e89: a9 8f       ..             ; Push return addr high (restore_args)
    pha                                                               ; 8e8b: 48          H              ; Push return addr high byte
    lda #&c6                                                          ; 8e8c: a9 c6       ..             ; Push return addr low (restore_args)
    pha                                                               ; 8e8e: 48          H              ; Push return addr low byte
    lda osword_0f_tbl_hi,x                                            ; 8e8f: bd ac 8e    ...            ; Load handler address high byte from table
    pha                                                               ; 8e92: 48          H              ; Push high byte for RTS dispatch
    lda osword_0f_tbl_lo,x                                            ; 8e93: bd a7 8e    ...            ; Load handler address low byte from table
    pha                                                               ; 8e96: 48          H              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    ldy #2                                                            ; 8e97: a0 02       ..             ; Y=2: save 3 bytes (&AA-&AC)
; &8e99 referenced 1 time by &8e9f
.save1
    lda osword_flag,y                                                 ; 8e99: b9 aa 00    ...            ; Load param block pointer byte
    sta (net_rx_ptr),y                                                ; 8e9c: 91 9c       ..             ; Save to NFS workspace via (net_rx_ptr)
    dey                                                               ; 8e9e: 88          .              ; Next byte (descending)
    bpl save1                                                         ; 8e9f: 10 f8       ..             ; Loop for all 3 bytes
    iny                                                               ; 8ea1: c8          .              ; Y=0 after BPL exit; INY makes Y=1
    lda (osword_pb_ptr),y                                             ; 8ea2: b1 f0       ..             ; Read sub-function code from (&F0)+1
    sty rom_svc_num                                                   ; 8ea4: 84 a9       ..             ; Store Y=1 to &A9
    rts                                                               ; 8ea6: 60          `              ; RTS dispatches to pushed handler address

; &8ea7 referenced 1 time by &8e93
.osword_0f_tbl_lo
    equb <(osword_0f_handler-1)                                       ; 8ea7: bf          .              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    equb <(osword_10_handler-1)                                       ; 8ea8: 6d          m
.fs_osword_tbl_lo
    equb <(osword_11_handler-1)                                       ; 8ea9: d9          .
    equb <(osword_12_dispatch-1)                                      ; 8eaa: fe          .
    equb <(econet_tx_rx-1)                                            ; 8eab: ec          .
; &8eac referenced 1 time by &8e8f
.osword_0f_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8eac: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb >(osword_10_handler-1)                                       ; 8ead: 8f          .
.fs_osword_tbl_hi
    equb >(osword_11_handler-1)                                       ; 8eae: 8e          .
    equb >(osword_12_dispatch-1)                                      ; 8eaf: 8e          .
    equb >(econet_tx_rx-1)                                            ; 8eb0: 8f          .

; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
; &8eb1 referenced 5 times by &8ebd, &8ed4, &8ee9, &8f1a, &8faf
.copy_param_block
    bcc load_workspace_byte                                           ; 8eb1: 90 04       ..             ; C=0: skip param-to-workspace copy
    lda (osword_pb_ptr),y                                             ; 8eb3: b1 f0       ..             ; Load byte from param block
    sta (ws_ptr_lo),y                                                 ; 8eb5: 91 ab       ..             ; Store to workspace
; &8eb7 referenced 1 time by &8eb1
.load_workspace_byte
    lda (ws_ptr_lo),y                                                 ; 8eb7: b1 ab       ..             ; Load byte from workspace
    sta (osword_pb_ptr),y                                             ; 8eb9: 91 f0       ..             ; Store to param block (no-op if C=1)
.copyl3
    iny                                                               ; 8ebb: c8          .              ; Advance to next byte
    dex                                                               ; 8ebc: ca          .              ; Decrement byte counter
    bpl copy_param_block                                              ; 8ebd: 10 f2       ..             ; Loop while X >= 0
; &8ebf referenced 2 times by &8e82, &8e86
.return_7
.logon3
.return_copy_param
    rts                                                               ; 8ebf: 60          `              ; Return after copy

; ***************************************************************************************
; OSWORD &0F handler: initiate transmit (CALLTX)
; 
; Checks the TX semaphore (TXCLR at &0D62) via ASL -- if carry is
; clear, a TX is already in progress and the call returns an error,
; preventing user code from corrupting a system transmit. Otherwise
; copies 16 bytes from the caller's OSWORD parameter block into the
; user TX control block (UTXCB) in static workspace. The TXCB
; pointer is copied to LTXCBP only after the semaphore is claimed,
; ensuring the low-level transmit code (BRIANX) sees a consistent
; pointer -- if copied before claiming, another transmitter could
; modify TXCBP between the copy and the claim.
; 
; On Entry:
;     X: parameter block address low byte
;     Y: parameter block address high byte
; 
; On Exit:
;     A: corrupted
;     X: corrupted
;     Y: &FF
; ***************************************************************************************
.osword_0f_handler
    asl tx_clear_flag                                                 ; 8ec0: 0e 62 0d    .b.            ; ASL: set C if TX in progress
    tya                                                               ; 8ec3: 98          .              ; Save param block high byte to A
    bcc readry                                                        ; 8ec4: 90 34       .4             ; C=0: read path
    lda net_rx_ptr_hi                                                 ; 8ec6: a5 9d       ..             ; User TX CB in workspace page (high byte)
    sta ws_ptr_hi                                                     ; 8ec8: 85 ac       ..             ; Set param block high byte
    sta nmi_tx_block_hi                                               ; 8eca: 85 a1       ..             ; Set LTXCBP high byte for low-level TX
    lda #&6f ; 'o'                                                    ; 8ecc: a9 6f       .o             ; &6F: offset into workspace for user TXCB
    sta ws_ptr_lo                                                     ; 8ece: 85 ab       ..             ; Set param block low byte
    sta nmi_tx_block                                                  ; 8ed0: 85 a0       ..             ; Set LTXCBP low byte for low-level TX
    ldx #&0f                                                          ; 8ed2: a2 0f       ..             ; X=15: copy 16 bytes (OSWORD param block)
    jsr copy_param_block                                              ; 8ed4: 20 b1 8e     ..            ; Copy param block to user TX control block
    jmp trampoline_tx_setup                                           ; 8ed7: 4c 60 96    L`.            ; Start user transmit via BRIANX

; ***************************************************************************************
; OSWORD &11 handler: read JSR arguments (READRA)
; 
; Copies the JSR (remote procedure call) argument buffer from the
; static workspace page back to the caller's OSWORD parameter block.
; Reads the buffer size from workspace offset JSRSIZ, then copies
; that many bytes. After the copy, clears the old LSTAT byte via
; CLRJSR to reset the protection status. Also provides READRB as
; a sub-entry (&8E6B) to return just the buffer size and args size
; without copying the data.
; ***************************************************************************************
.osword_11_handler
    lda net_rx_ptr_hi                                                 ; 8eda: a5 9d       ..             ; Set source high byte from workspace page
    sta ws_ptr_hi                                                     ; 8edc: 85 ac       ..             ; Store as copy source high byte in &AC
    ldy #&7f                                                          ; 8ede: a0 7f       ..             ; JSRSIZ at workspace offset &7F
    lda (net_rx_ptr),y                                                ; 8ee0: b1 9c       ..             ; Load buffer size from workspace
    iny                                                               ; 8ee2: c8          .              ; Y=&80: start of JSR argument data; Y=&80
    sty ws_ptr_lo                                                     ; 8ee3: 84 ab       ..             ; Store &80 as copy source low byte
    tax                                                               ; 8ee5: aa          .              ; X = buffer size (loop counter)
    dex                                                               ; 8ee6: ca          .              ; X = size-1 (0-based count for copy)
    ldy #0                                                            ; 8ee7: a0 00       ..             ; Y=0: start of destination param block
    jsr copy_param_block                                              ; 8ee9: 20 b1 8e     ..            ; Copy X+1 bytes from workspace to param
    jmp clear_jsr_protection                                          ; 8eec: 4c e9 92    L..            ; Clear JSR protection status (CLRJSR)

; &8eef referenced 1 time by &8f3e
.read_args_size
    ldy #&7f                                                          ; 8eef: a0 7f       ..             ; Y=&7F: JSRSIZ offset (READRB entry)
    lda (net_rx_ptr),y                                                ; 8ef1: b1 9c       ..             ; Load buffer size from workspace
    ldy #1                                                            ; 8ef3: a0 01       ..             ; Y=1: param block offset for size byte
    sta (osword_pb_ptr),y                                             ; 8ef5: 91 f0       ..             ; Store buffer size to (&F0)+1
    iny                                                               ; 8ef7: c8          .              ; Y=2: param block offset for args size; Y=&02
    lda #&80                                                          ; 8ef8: a9 80       ..             ; A=&80: argument data starts at offset &80
; &8efa referenced 1 time by &8ec4
.readry
    sta (osword_pb_ptr),y                                             ; 8efa: 91 f0       ..             ; Store args start offset to (&F0)+2
    rts                                                               ; 8efc: 60          `              ; Return

; &8efd referenced 1 time by &8f11
.osword_12_offsets
    equb &ff, 1                                                       ; 8efd: ff 01       ..

; ***************************************************************************************
; OSWORD &12 sub-function dispatcher
; 
; Dispatches sub-functions 0-9 for OSWORD &12 (read/set FS
; state). Functions 0-3 read/set station and printer server
; addresses; 4-5 read/set protection masks; 6-7 read/set
; context handles (URD/CSD/LIB); 8 reads local station;
; 9 reads JSR argument buffer size.
; ***************************************************************************************
.osword_12_dispatch
    cmp #6                                                            ; 8eff: c9 06       ..             ; Sub-function >= 6?
    bcs rsl1                                                          ; 8f01: b0 35       .5             ; Yes: jump to sub 6-9 handler
    cmp #4                                                            ; 8f03: c9 04       ..             ; Sub-function >= 4?
    bcs rssl1                                                         ; 8f05: b0 16       ..             ; Sub-function 4 or 5: read/set protection
    lsr a                                                             ; 8f07: 4a          J              ; LSR: 0->0, 1->0, 2->1, 3->1
    ldx #&0d                                                          ; 8f08: a2 0d       ..             ; X=&0D: default to static workspace page
    tay                                                               ; 8f0a: a8          .              ; Transfer LSR result to Y for indexing
    beq set_workspace_page                                            ; 8f0b: f0 02       ..             ; Y=0 (sub 0-1): use page &0D
    ldx nfs_workspace_hi                                              ; 8f0d: a6 9f       ..             ; Y=1 (sub 2-3): use dynamic workspace
; &8f0f referenced 1 time by &8f0b
.set_workspace_page
    stx ws_ptr_hi                                                     ; 8f0f: 86 ac       ..             ; Store workspace page in &AC (hi byte)
    lda osword_12_offsets,y                                           ; 8f11: b9 fd 8e    ...            ; Load offset: &FF (sub 0-1) or &01 (sub 2-3)
    sta ws_ptr_lo                                                     ; 8f14: 85 ab       ..             ; Store offset in &AB (lo byte)
    ldx #1                                                            ; 8f16: a2 01       ..             ; X=1: copy 2 bytes
    ldy #1                                                            ; 8f18: a0 01       ..             ; Y=1: start at param block offset 1
    jmp copy_param_block                                              ; 8f1a: 4c b1 8e    L..            ; Jump to read/write workspace path

; &8f1d referenced 1 time by &8f05
.rssl1
    lsr a                                                             ; 8f1d: 4a          J              ; LSR A: test bit 0 of sub-function
    iny                                                               ; 8f1e: c8          .              ; Y=1: offset for protection byte
    lda (osword_pb_ptr),y                                             ; 8f1f: b1 f0       ..             ; Load protection byte from param block
    bcs rssl2                                                         ; 8f21: b0 05       ..             ; C=1 (odd sub): set protection
    lda prot_status                                                   ; 8f23: ad 63 0d    .c.            ; C=0 (even sub): read current status
    sta (osword_pb_ptr),y                                             ; 8f26: 91 f0       ..             ; Return current value to param block
; &8f28 referenced 1 time by &8f21
.rssl2
    sta prot_status                                                   ; 8f28: 8d 63 0d    .c.            ; Update protection status
    sta saved_jsr_mask                                                ; 8f2b: 8d 65 0d    .e.            ; Also save as JSR mask backup
    rts                                                               ; 8f2e: 60          `              ; Return

; &8f2f referenced 1 time by &8f3a
.read_fs_handle
    ldy #&14                                                          ; 8f2f: a0 14       ..             ; Y=&14: RX buffer offset for FS handle
    lda (net_rx_ptr),y                                                ; 8f31: b1 9c       ..             ; Read FS reply handle from RX data
    ldy #1                                                            ; 8f33: a0 01       ..             ; Y=1: param block byte 1
    sta (osword_pb_ptr),y                                             ; 8f35: 91 f0       ..             ; Return handle to caller's param block
    rts                                                               ; 8f37: 60          `              ; Return

; &8f38 referenced 1 time by &8f01
.rsl1
    cmp #8                                                            ; 8f38: c9 08       ..             ; Sub-function 8: read FS handle
    beq read_fs_handle                                                ; 8f3a: f0 f3       ..             ; Match: read handle from RX buffer
    cmp #9                                                            ; 8f3c: c9 09       ..             ; Sub-function 9: read args size
    beq read_args_size                                                ; 8f3e: f0 af       ..             ; Match: read ARGS buffer info
    bpl return_last_error                                             ; 8f40: 10 19       ..             ; Sub >= 10 (bit 7 clear): read error
    ldy #3                                                            ; 8f42: a0 03       ..             ; Y=3: start from handle 3 (descending)
    lsr a                                                             ; 8f44: 4a          J              ; LSR: test read/write bit
    bcc readc1                                                        ; 8f45: 90 1b       ..             ; C=0: read handles from workspace
    sty nfs_temp                                                      ; 8f47: 84 a8       ..             ; Init loop counter at Y=3
; &8f49 referenced 1 time by &8f58
.copy_handles_to_ws
    ldy nfs_temp                                                      ; 8f49: a4 a8       ..             ; Reload loop counter
    lda (osword_pb_ptr),y                                             ; 8f4b: b1 f0       ..             ; Read handle from caller's param block
    jsr handle_to_mask_a                                              ; 8f4d: 20 25 86     %.            ; Convert handle number to bitmask
    tya                                                               ; 8f50: 98          .              ; TYA: get bitmask result
    ldy nfs_temp                                                      ; 8f51: a4 a8       ..             ; Reload loop counter
    sta fs_server_net,y                                               ; 8f53: 99 01 0e    ...            ; Store bitmask to FS server table
    dec nfs_temp                                                      ; 8f56: c6 a8       ..             ; Next handle (descending)
    bne copy_handles_to_ws                                            ; 8f58: d0 ef       ..             ; Loop for handles 3,2,1
    rts                                                               ; 8f5a: 60          `              ; Return

; &8f5b referenced 1 time by &8f40
.return_last_error
    iny                                                               ; 8f5b: c8          .              ; Y=1 (post-INY): param block byte 1
    lda fs_last_error                                                 ; 8f5c: ad 09 0e    ...            ; Read last FS error code
    sta (osword_pb_ptr),y                                             ; 8f5f: 91 f0       ..             ; Return error to caller's param block
    rts                                                               ; 8f61: 60          `              ; Return

; &8f62 referenced 2 times by &8f45, &8f6b
.readc1
    lda fs_server_net,y                                               ; 8f62: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8f65: 20 42 86     B.            ; Convert bitmask to handle number (FS2A)
    sta (osword_pb_ptr),y                                             ; 8f68: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8f6a: 88          .              ; Next handle (descending)
    bne readc1                                                        ; 8f6b: d0 f5       ..             ; Loop for handles 3,2,1
    rts                                                               ; 8f6d: 60          `              ; Return

; ***************************************************************************************
; OSWORD &10 handler: open/read RX control block (OPENRX)
; 
; If the first byte of the caller's parameter block is zero, scans
; for a free RXCB (flag byte = &3F = deleted) starting from RXCB #3
; (RXCBs 0-2 are dedicated: printer, remote, FS). Returns the RXCB
; number in the first byte, or zero if none free. If the first byte
; is non-zero, reads the specified RXCB's data back into the caller's
; parameter block (12 bytes) and then deletes the RXCB by setting
; its flag byte to &3F -- a consume-once semantic so user code reads
; received data and frees the CB in a single atomic operation,
; preventing double-reads. The low-level user RX flag (LFLAG) is
; temporarily disabled via ROR/ROL during the operation to prevent
; the interrupt-driven receive code from modifying a CB that is
; being read or opened.
; 
; On Entry:
;     X: parameter block address low byte
;     Y: parameter block address high byte
; 
; On Exit:
;     A: corrupted
;     X: corrupted
;     Y: &FF
; ***************************************************************************************
.osword_10_handler
    ldx nfs_workspace_hi                                              ; 8f6e: a6 9f       ..             ; Workspace page high byte
    stx ws_ptr_hi                                                     ; 8f70: 86 ac       ..             ; Set up pointer high byte in &AC
    sty ws_ptr_lo                                                     ; 8f72: 84 ab       ..             ; Save param block high byte in &AB
    ror rx_flags                                                      ; 8f74: 6e 64 0d    nd.            ; Disable user RX during CB operation
    lda (osword_pb_ptr),y                                             ; 8f77: b1 f0       ..             ; Read first byte of param block
    sta osword_flag                                                   ; 8f79: 85 aa       ..             ; Save: 0=open new, non-zero=read RXCB
.scan_or_read_rxcb
    bne read_rxcb                                                     ; 8f7b: d0 1b       ..             ; Non-zero: read specified RXCB
    lda #3                                                            ; 8f7d: a9 03       ..             ; Start scan from RXCB #3 (0-2 reserved)
; &8f7f referenced 1 time by &8f91
.scan0
    jsr calc_handle_offset                                            ; 8f7f: 20 4c 8e     L.            ; Convert RXCB number to workspace offset
    bcs openl4                                                        ; 8f82: b0 3d       .=             ; Invalid RXCB: return zero
    lsr a                                                             ; 8f84: 4a          J              ; LSR twice: byte offset / 4
    lsr a                                                             ; 8f85: 4a          J              ; Yields RXCB number from offset
    tax                                                               ; 8f86: aa          .              ; X = RXCB number for iteration
    lda (ws_ptr_lo),y                                                 ; 8f87: b1 ab       ..             ; Read flag byte from RXCB workspace
    beq openl4                                                        ; 8f89: f0 36       .6             ; Zero = end of CB list
    cmp #&3f ; '?'                                                    ; 8f8b: c9 3f       .?             ; &3F = deleted slot, free for reuse
    beq scan1                                                         ; 8f8d: f0 04       ..             ; Found free slot
    inx                                                               ; 8f8f: e8          .              ; Try next RXCB
    txa                                                               ; 8f90: 8a          .              ; A = next RXCB number
    bne scan0                                                         ; 8f91: d0 ec       ..             ; Continue scan (always branches)
; &8f93 referenced 1 time by &8f8d
.scan1
    txa                                                               ; 8f93: 8a          .              ; A = free RXCB number
    ldx #0                                                            ; 8f94: a2 00       ..             ; X=0 for indexed indirect store
    sta (osword_pb_ptr,x)                                             ; 8f96: 81 f0       ..             ; Return RXCB number to caller's byte 0
; &8f98 referenced 1 time by &8f7b
.read_rxcb
    jsr calc_handle_offset                                            ; 8f98: 20 4c 8e     L.            ; Convert RXCB number to workspace offset
    bcs openl4                                                        ; 8f9b: b0 24       .$             ; Invalid: write zero to param block
    dey                                                               ; 8f9d: 88          .              ; Y = offset-1: points to flag byte
    sty ws_ptr_lo                                                     ; 8f9e: 84 ab       ..             ; Set &AB = workspace ptr low byte
    lda #&c0                                                          ; 8fa0: a9 c0       ..             ; &C0: test mask for flag byte
    ldy #1                                                            ; 8fa2: a0 01       ..             ; Y=1: flag byte offset in RXCB
    ldx #&0b                                                          ; 8fa4: a2 0b       ..             ; Enable interrupts before transmit
    cpy osword_flag                                                   ; 8fa6: c4 aa       ..             ; Compare Y(1) with saved byte (open/read)
    adc (ws_ptr_lo),y                                                 ; 8fa8: 71 ab       q.             ; ADC flag: test if slot is in use
    beq openl6                                                        ; 8faa: f0 03       ..             ; Dest station = &FFFF (accept reply from any station)
    bmi openl7                                                        ; 8fac: 30 0e       0.             ; Negative: slot has received data
; &8fae referenced 1 time by &8fbe
.copy_rxcb_to_param
    clc                                                               ; 8fae: 18          .              ; C=0: workspace-to-param direction
; &8faf referenced 1 time by &8faa
.openl6
    jsr copy_param_block                                              ; 8faf: 20 b1 8e     ..            ; Copy RXCB data to param block
    bcs reenable_rx                                                   ; 8fb2: b0 0f       ..             ; Done: skip deletion on error
    lda #&3f ; '?'                                                    ; 8fb4: a9 3f       .?             ; Mark CB as consumed (consume-once)
    ldy #1                                                            ; 8fb6: a0 01       ..             ; Y=1: flag byte offset
    sta (ws_ptr_lo),y                                                 ; 8fb8: 91 ab       ..             ; Write &3F to mark slot deleted
    bne reenable_rx                                                   ; 8fba: d0 07       ..             ; Branch to exit (always taken); ALWAYS branch

; &8fbc referenced 1 time by &8fac
.openl7
    adc #1                                                            ; 8fbc: 69 01       i.             ; Advance through multi-byte field
    bne copy_rxcb_to_param                                            ; 8fbe: d0 ee       ..             ; Loop until all bytes processed
    dey                                                               ; 8fc0: 88          .              ; Y=-1 → Y=0 after STA below
; &8fc1 referenced 3 times by &8f82, &8f89, &8f9b
.openl4
    sta (osword_pb_ptr),y                                             ; 8fc1: 91 f0       ..             ; Return zero (no free RXCB found)
; &8fc3 referenced 2 times by &8fb2, &8fba
.reenable_rx
    rol rx_flags                                                      ; 8fc3: 2e 64 0d    .d.            ; Re-enable user RX
    rts                                                               ; 8fc6: 60          `              ; Return

    equb &a0, 2                                                       ; 8fc7: a0 02       ..             ; Y=2: copy 3 bytes (indices 2,1,0)
.rest1
    equb &b1, &9c, &99, &aa, 0, &88, &10, &f8, &60                    ; 8fc9: b1 9c 99... ...            ; Load saved arg from (net_rx_ptr)+Y; Restore saved OSWORD argument byte; Decrement byte counter; Loop for bytes 2,1,0; Return to caller

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &28. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &2C.
; ***************************************************************************************
; &8fd2 referenced 1 time by &9005
.setup_rx_buffer_ptrs
    ldy #&1c                                                          ; 8fd2: a0 1c       ..             ; Y=&1C: RXCB template offset
    lda osword_pb_ptr                                                 ; 8fd4: a5 f0       ..             ; A = base address low byte
    adc #1                                                            ; 8fd6: 69 01       i.             ; A = base + 1 (skip length byte)
    jsr store_16bit_at_y                                              ; 8fd8: 20 e3 8f     ..            ; Receive data blocks until command byte = &00 or &0D
    ldy #1                                                            ; 8fdb: a0 01       ..             ; Read data length from (&F0)+1
    lda (osword_pb_ptr),y                                             ; 8fdd: b1 f0       ..             ; A = data length byte
    ldy #&20 ; ' '                                                    ; 8fdf: a0 20       .              ; Workspace offset &20 = RX data end
    adc osword_pb_ptr                                                 ; 8fe1: 65 f0       e.             ; A = base + length = end address low
; &8fe3 referenced 1 time by &8fd8
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8fe3: 91 9e       ..             ; Store low byte of 16-bit address
    iny                                                               ; 8fe5: c8          .              ; Advance to high byte offset
    lda osword_pb_ptr_hi                                              ; 8fe6: a5 f1       ..             ; A = high byte of base address
    adc #0                                                            ; 8fe8: 69 00       i.             ; Add carry for 16-bit addition
    sta (nfs_workspace),y                                             ; 8fea: 91 9e       ..             ; Store high byte
    rts                                                               ; 8fec: 60          `              ; Return

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &8360
;      (zero entries substituted from NMI workspace &0DE6), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &9039).
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8fed: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs handle_tx_result                                              ; 8fef: b0 48       .H             ; A >= 1: handle TX result
    ldy #&23 ; '#'                                                    ; 8ff1: a0 23       .#             ; Y=&23: start of template (descending)
; &8ff3 referenced 1 time by &9000
.dofs01
    lda init_tx_ctrl_block,y                                          ; 8ff3: b9 60 83    .`.            ; Load from ROM template (zero = use NMI workspace value)
    bne store_txcb_byte                                               ; 8ff6: d0 03       ..             ; Non-zero = use ROM template byte as-is
    lda nmi_sub_table,y                                               ; 8ff8: b9 e6 0d    ...            ; Zero = substitute from NMI workspace
; &8ffb referenced 1 time by &8ff6
.store_txcb_byte
    sta (nfs_workspace),y                                             ; 8ffb: 91 9e       ..             ; Store to dynamic workspace
    dey                                                               ; 8ffd: 88          .              ; Descend through template
    cpy #&17                                                          ; 8ffe: c0 17       ..             ; Stop at offset &17
    bne dofs01                                                        ; 9000: d0 f1       ..             ; Loop until all bytes copied
    iny                                                               ; 9002: c8          .              ; Y=&18: TX block starts here
    sty net_tx_ptr                                                    ; 9003: 84 9a       ..             ; Point net_tx_ptr at workspace+&18
    jsr setup_rx_buffer_ptrs                                          ; 9005: 20 d2 8f     ..            ; Set up RX buffer start/end pointers
    ldy #2                                                            ; 9008: a0 02       ..             ; Y=2: port byte offset in RXCB
    lda #&90                                                          ; 900a: a9 90       ..             ; A=&90: FS reply port
    sta (osword_pb_ptr),y                                             ; 900c: 91 f0       ..             ; Store port &90 at (&F0)+2
    iny                                                               ; 900e: c8          .              ; Y=&03
    iny                                                               ; 900f: c8          .              ; Y=&04: advance to station address; Y=&04
; &9010 referenced 1 time by &9018
.copy_fs_addr
    lda fs_context_base,y                                             ; 9010: b9 fe 0d    ...            ; Copy FS station addr from workspace
    sta (osword_pb_ptr),y                                             ; 9013: 91 f0       ..             ; Store to RX param block
    iny                                                               ; 9015: c8          .              ; Next byte
    cpy #7                                                            ; 9016: c0 07       ..             ; Done 3 bytes (Y=4,5,6)?
    bne copy_fs_addr                                                  ; 9018: d0 f6       ..             ; No: continue copying
    lda nfs_workspace_hi                                              ; 901a: a5 9f       ..             ; High byte of workspace for TX ptr
    sta net_tx_ptr_hi                                                 ; 901c: 85 9b       ..             ; Store as TX pointer high byte
    cli                                                               ; 901e: 58          X              ; Enable interrupts before transmit
    jsr tx_poll_ff                                                    ; 901f: 20 71 86     q.            ; Transmit with full retry
    ldy #&20 ; ' '                                                    ; 9022: a0 20       .              ; Y=&20: RX end address offset
    lda #&ff                                                          ; 9024: a9 ff       ..             ; Dest station = &FFFF (accept reply from any station)
    sta (nfs_workspace),y                                             ; 9026: 91 9e       ..             ; Store end address low byte (&FF)
    iny                                                               ; 9028: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; 9029: 91 9e       ..             ; Store end address high byte (&FF)
    ldy #&19                                                          ; 902b: a0 19       ..             ; Y=&19: port byte in workspace RXCB
    lda #&90                                                          ; 902d: a9 90       ..             ; A=&90: FS reply port
    sta (nfs_workspace),y                                             ; 902f: 91 9e       ..             ; Store port to workspace RXCB
    dey                                                               ; 9031: 88          .              ; Y=&18
    lda #&7f                                                          ; 9032: a9 7f       ..             ; A=&7F: flag byte = waiting for reply
    sta (nfs_workspace),y                                             ; 9034: 91 9e       ..             ; Store flag byte to workspace RXCB
    jmp send_to_fs_star                                               ; 9036: 4c f8 84    L..            ; Jump to RX poll (BRIANX)

; &9039 referenced 1 time by &8fef
.handle_tx_result
    php                                                               ; 9039: 08          .              ; Save processor flags
    ldy #1                                                            ; 903a: a0 01       ..             ; Y=1: first data byte offset; Y=character to write
    lda (osword_pb_ptr),y                                             ; 903c: b1 f0       ..             ; Load first data byte from RX buffer
; ***************************************************************************************
; Fn 4: net write character (NWRCH)
; 
; Writes a character (passed in Y) to the screen via OSWRITCH.
; Before the write, uses TSX to reach into the stack and zero the
; carry flag in the caller's saved processor status byte -- ROR
; followed by ASL on the stacked P byte (&0106,X) shifts carry
; out and back in as zero. This ensures the calling code's PLP
; restores carry=0, signalling "character accepted" without needing
; a separate CLC/PHP sequence. A classic 6502 trick for modifying
; return flags without touching the actual processor status.
; 
; On Entry:
;     Y: character to write
; 
; On Exit:
;     A: &3F
;     X: 0
;     Y: 0
; ***************************************************************************************
.net_write_char
    tax                                                               ; 903e: aa          .              ; X = first data byte (command code)
    iny                                                               ; 903f: c8          .              ; Advance to next data byte
    lda (osword_pb_ptr),y                                             ; 9040: b1 f0       ..             ; Load station address high byte
    iny                                                               ; 9042: c8          .              ; Advance past station addr
    sty ws_ptr_lo                                                     ; 9043: 84 ab       ..             ; Save Y as data index
    ldy #&72 ; 'r'                                                    ; 9045: a0 72       .r             ; Store station addr hi at (net_rx_ptr)+&72
    sta (net_rx_ptr),y                                                ; 9047: 91 9c       ..             ; Store to workspace
    dey                                                               ; 9049: 88          .              ; Y=&71
    txa                                                               ; 904a: 8a          .              ; A = command code (from X)
    sta (net_rx_ptr),y                                                ; 904b: 91 9c       ..             ; Store station addr lo at (net_rx_ptr)+&71
    plp                                                               ; 904d: 28          (              ; Restore flags from earlier PHP
    bne dofs2                                                         ; 904e: d0 1d       ..             ; First call: adjust data length
; &9050 referenced 1 time by &906a
.send_data_bytes
    ldy ws_ptr_lo                                                     ; 9050: a4 ab       ..             ; Receive data blocks until command byte = &00 or &0D
    inc ws_ptr_lo                                                     ; 9052: e6 ab       ..             ; Advance data index for next iteration
    lda (osword_pb_ptr),y                                             ; 9054: b1 f0       ..             ; Load next data byte
    ldy #&7d ; '}'                                                    ; 9056: a0 7d       .}             ; Y=&7D: store byte for TX at offset &7D
    sta (net_rx_ptr),y                                                ; 9058: 91 9c       ..             ; Store data byte at (net_rx_ptr)+&7D for TX
    pha                                                               ; 905a: 48          H              ; Save data byte for &0D check after TX
    jsr ctrl_block_setup_alt                                          ; 905b: 20 6d 91     m.            ; Set up TX control block
    cli                                                               ; 905e: 58          X              ; Enable interrupts for TX
    jsr tx_poll_core                                                  ; 905f: 20 75 86     u.            ; Enable IRQs and transmit; Core transmit and poll routine (XMIT)
; &9062 referenced 1 time by &9063
.delay_between_tx
    dex                                                               ; 9062: ca          .              ; Short delay loop between TX packets
    bne delay_between_tx                                              ; 9063: d0 fd       ..             ; Spin until X reaches 0
    pla                                                               ; 9065: 68          h              ; Restore data byte for terminator check
    beq return_8                                                      ; 9066: f0 04       ..             ; Z=1: not intercepted, pass through
    eor #&0d                                                          ; 9068: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne send_data_bytes                                               ; 906a: d0 e4       ..             ; Not &0D: continue with next byte
; &906c referenced 1 time by &9066
.return_8
    rts                                                               ; 906c: 60          `              ; Return (data complete)

; &906d referenced 1 time by &904e
.dofs2
    jsr ctrl_block_setup_alt                                          ; 906d: 20 6d 91     m.            ; First-packet: set up control block
    ldy #&7b ; '{'                                                    ; 9070: a0 7b       .{             ; Y=&7B: data length offset
    lda (net_rx_ptr),y                                                ; 9072: b1 9c       ..             ; Load current data length
    adc #3                                                            ; 9074: 69 03       i.             ; Adjust data length by 3 for header bytes
    sta (net_rx_ptr),y                                                ; 9076: 91 9c       ..             ; Store adjusted length
; ***************************************************************************************
; Enable interrupts and transmit via tx_poll_ff
; 
; CLI to enable interrupts, then JMP tx_poll_ff. A short
; tail-call wrapper used after building the TX control block.
; ***************************************************************************************
.enable_irq_and_tx
    cli                                                               ; 9078: 58          X              ; Enable interrupts
.jmp_clear_svc_restore
    jmp tx_poll_ff                                                    ; 9079: 4c 71 86    Lq.            ; Transmit via tx_poll_ff

; ***************************************************************************************
; NETVEC dispatch handler (ENTRY)
; 
; Indirected from NETVEC at &0224. Saves all registers and flags,
; retrieves the reason code from the stacked A, and dispatches to
; one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
; &9095. Reason codes >= 9 are ignored.
; 
; Dispatch targets (from NFS09):
;   0:   no-op (RTS)
;   1-3: PRINT -- chars in printer buffer / Ctrl-B / Ctrl-C
;   4:   NWRCH -- write character to screen (net write char)
;   5:   SELECT -- printer selection changed
;   6:   no-op (net read char -- not implemented)
;   7:   NBYTE -- remote OSBYTE call
;   8:   NWORD -- remote OSWORD call
; 
; On Entry:
;     A: reason code (0-8)
; 
; On Exit:
;     A: preserved
;     X: preserved
;     Y: preserved
; ***************************************************************************************
.osword_dispatch
    php                                                               ; 907c: 08          .              ; Save processor status
    pha                                                               ; 907d: 48          H              ; Save A (reason code)
    txa                                                               ; 907e: 8a          .              ; Save X
    pha                                                               ; 907f: 48          H              ; Push X to stack
    tya                                                               ; 9080: 98          .              ; Save Y
    pha                                                               ; 9081: 48          H              ; Push Y to stack
    tsx                                                               ; 9082: ba          .              ; Get stack pointer for indexed access
    lda l0103,x                                                       ; 9083: bd 03 01    ...            ; Retrieve original A (function code) from stack
    cmp #9                                                            ; 9086: c9 09       ..             ; Reason codes 0-8 only
    bcs entry1                                                        ; 9088: b0 04       ..             ; Code >= 9: skip dispatch, restore regs
    tax                                                               ; 908a: aa          .              ; X = reason code for table lookup
    jsr osword_trampoline                                             ; 908b: 20 95 90     ..            ; Dispatch to handler via trampoline
; &908e referenced 1 time by &9088
.entry1
    pla                                                               ; 908e: 68          h              ; Restore Y
    tay                                                               ; 908f: a8          .              ; Transfer to Y register
    pla                                                               ; 9090: 68          h              ; Restore X
    tax                                                               ; 9091: aa          .              ; Transfer to X register
    pla                                                               ; 9092: 68          h              ; Restore A
    plp                                                               ; 9093: 28          (              ; Restore processor status flags
    rts                                                               ; 9094: 60          `              ; Return with all registers preserved

; &9095 referenced 1 time by &908b
.osword_trampoline
    lda osword_tbl_hi,x                                               ; 9095: bd a9 90    ...            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9098: 48          H              ; Push high byte of handler address
    lda osword_tbl_lo,x                                               ; 9099: bd a0 90    ...            ; Load handler low byte from table
    pha                                                               ; 909c: 48          H              ; Push low byte of handler address
    lda osbyte_a_copy                                                 ; 909d: a5 ef       ..             ; Load workspace byte &EF for handler
    rts                                                               ; 909f: 60          `              ; RTS dispatches to pushed handler

; &90a0 referenced 1 time by &9099
.osword_tbl_lo
    equb <(return_2-1)                                                ; 90a0: 75          u
    equb <(remote_print_handler-1)                                    ; 90a1: d8          .
    equb <(remote_print_handler-1)                                    ; 90a2: d8          .
    equb <(remote_print_handler-1)                                    ; 90a3: d8          .
    equb <(nwrch_handler-1)                                           ; 90a4: b1          .
    equb <(printer_select_handler-1)                                  ; 90a5: c8          .
    equb <(return_2-1)                                                ; 90a6: 75          u
    equb <(remote_cmd_dispatch-1)                                     ; 90a7: d7          .
    equb <(remote_cmd_data-1)                                         ; 90a8: 41          A
; &90a9 referenced 1 time by &9095
.osword_tbl_hi
    equb >(return_2-1)                                                ; 90a9: 81          .
    equb >(remote_print_handler-1)                                    ; 90aa: 91          .
    equb >(remote_print_handler-1)                                    ; 90ab: 91          .
    equb >(remote_print_handler-1)                                    ; 90ac: 91          .
    equb >(nwrch_handler-1)                                           ; 90ad: 90          .
    equb >(printer_select_handler-1)                                  ; 90ae: 91          .
    equb >(return_2-1)                                                ; 90af: 81          .
    equb >(remote_cmd_dispatch-1)                                     ; 90b0: 90          .
    equb >(remote_cmd_data-1)                                         ; 90b1: 91          .

; ***************************************************************************************
; NETVEC reason 4: write character to network (NWRCH)
; 
; Handles remote character output over the network. Clears
; carry in the stacked processor status (via ROR/ASL on the
; stack frame) to signal success to the MOS dispatcher.
; Stores the character from Y into workspace offset &DA,
; then falls through to setup_tx_and_send with A=0 to
; transmit the character to the remote terminal.
; ***************************************************************************************
.nwrch_handler
    tsx                                                               ; 90b2: ba          .              ; Get stack pointer for P register
    ror l0106,x                                                       ; 90b3: 7e 06 01    ~..            ; ROR/ASL on stacked P: zeros carry to signal success
    asl l0106,x                                                       ; 90b6: 1e 06 01    ...            ; ASL: restore P after ROR zeroed carry
    tya                                                               ; 90b9: 98          .              ; Y = character to write
    ldy #&da                                                          ; 90ba: a0 da       ..             ; Store character at workspace offset &DA
    sta (nfs_workspace),y                                             ; 90bc: 91 9e       ..             ; Store char at workspace offset &DA
    lda #0                                                            ; 90be: a9 00       ..             ; A=0: command type for net write char
; ***************************************************************************************
; Set up TX control block and send
; 
; Builds a TX control block at (nfs_workspace)+&0C from the current
; workspace state, then initiates transmission via the ADLC TX path.
; This is the common send routine used after command data has been
; prepared. The exact control block layout and field mapping need
; further analysis.
; ***************************************************************************************
; &90c0 referenced 3 times by &819d, &9107, &9168
.setup_tx_and_send
    ldy #&d9                                                          ; 90c0: a0 d9       ..             ; Y=&D9: command type offset
    sta (nfs_workspace),y                                             ; 90c2: 91 9e       ..             ; Store command type at ws+&D9
    lda #&80                                                          ; 90c4: a9 80       ..             ; Mark TX control block as active (&80)
    ldy #&0c                                                          ; 90c6: a0 0c       ..             ; Y=&0C: TXCB start offset
    sta (nfs_workspace),y                                             ; 90c8: 91 9e       ..             ; Set TX active flag at ws+&0C
    sty net_tx_ptr                                                    ; 90ca: 84 9a       ..             ; Redirect net_tx_ptr low to workspace
    ldx nfs_workspace_hi                                              ; 90cc: a6 9f       ..             ; Load workspace page high byte
    stx net_tx_ptr_hi                                                 ; 90ce: 86 9b       ..             ; Complete ptr redirect
    jsr tx_poll_ff                                                    ; 90d0: 20 71 86     q.            ; Transmit with full retry
    lda #&3f ; '?'                                                    ; 90d3: a9 3f       .?             ; Mark TXCB as deleted (&3F) after transmit
    sta (net_tx_ptr,x)                                                ; 90d5: 81 9a       ..             ; Write &3F to TXCB byte 0
    rts                                                               ; 90d7: 60          `              ; Return

; ***************************************************************************************
; Fn 7: remote OSBYTE handler (NBYTE)
; 
; Full RPC mechanism for OSBYTE calls across the network. When a
; machine is remoted, OSBYTE/OSWORD calls that affect terminal-side
; hardware (keyboard scanning, flash rates, etc.) must be indirected
; across the net. OSBYTE calls are classified into three categories:
;   Y>0 (NCTBPL table): executed on BOTH machines (flash rates etc.)
;   Y<0 (NCTBMI table): executed on terminal only, result sent back
;   Y=0: not recognised, passed through unhandled
; Results returned via stack manipulation: the saved processor status
; byte at &0106 has V-flag (bit 6) forced on to tell the MOS the
; call was claimed (preventing dispatch to other ROMs), and the I-bit
; (bit 2) forced on to disable interrupts during register restoration,
; preventing race conditions. The carry flag in the saved P is also
; manipulated via ROR/ASL to zero it, signaling success to the caller.
; OSBYTE &81 (INKEY) gets special handling as it must read the
; terminal's keyboard.
; ***************************************************************************************
.remote_cmd_dispatch
    ldy osword_pb_ptr_hi                                              ; 90d8: a4 f1       ..             ; Load original Y (OSBYTE secondary param)
    cmp #&81                                                          ; 90da: c9 81       ..             ; OSBYTE &81 (INKEY): always forward to terminal
    beq dispatch_remote_osbyte                                        ; 90dc: f0 13       ..             ; Forward &81 to terminal for keyboard read
    ldy #1                                                            ; 90de: a0 01       ..             ; Y=1: search NCTBPL table (execute on both)
    ldx #7                                                            ; 90e0: a2 07       ..             ; X=7: 8-entry NCTBPL table size
    jsr match_osbyte_code                                             ; 90e2: 20 2a 91     *.            ; Search for OSBYTE code in NCTBPL table
    beq dispatch_remote_osbyte                                        ; 90e5: f0 0a       ..             ; Match found: dispatch with Y=1 (both)
    dey                                                               ; 90e7: 88          .              ; Y=-1: search NCTBMI table (terminal only)
    dey                                                               ; 90e8: 88          .              ; Second DEY: Y=&FF (from 1 via 0)
    ldx #&0e                                                          ; 90e9: a2 0e       ..             ; X=&0E: 15-entry NCTBMI table size
    jsr match_osbyte_code                                             ; 90eb: 20 2a 91     *.            ; Search for OSBYTE code in NCTBMI table
    beq dispatch_remote_osbyte                                        ; 90ee: f0 01       ..             ; Match found: dispatch with Y=&FF (terminal)
    iny                                                               ; 90f0: c8          .              ; Y=0: OSBYTE not recognised, ignore
; &90f1 referenced 3 times by &90dc, &90e5, &90ee
.dispatch_remote_osbyte
    ldx #2                                                            ; 90f1: a2 02       ..             ; X=2 bytes to copy (default for RBYTE)
    tya                                                               ; 90f3: 98          .              ; A=Y: check table match result
    beq return_nbyte                                                  ; 90f4: f0 33       .3             ; Y=0: not recognised, return unhandled
    php                                                               ; 90f6: 08          .              ; Y>0 (NCTBPL): send only, no result expected
    bpl nbyte6                                                        ; 90f7: 10 01       ..             ; Y>0 (NCTBPL): no result expected, skip RX
    inx                                                               ; 90f9: e8          .              ; Y<0 (NCTBMI): X=3 bytes (result + P flags); X=&03
; &90fa referenced 1 time by &90f7
.nbyte6
    ldy #&dc                                                          ; 90fa: a0 dc       ..             ; Y=&DC: top of 3-byte stack frame region
; &90fc referenced 1 time by &9104
.nbyte1
    lda tube_claimed_id,y                                             ; 90fc: b9 15 00    ...            ; Copy OSBYTE args from stack frame to workspace
    sta (nfs_workspace),y                                             ; 90ff: 91 9e       ..             ; Store to NFS workspace for transmission
    dey                                                               ; 9101: 88          .              ; Next byte (descending)
    cpy #&da                                                          ; 9102: c0 da       ..             ; Copied all 3 bytes? (&DC, &DB, &DA)
    bpl nbyte1                                                        ; 9104: 10 f6       ..             ; Loop for remaining bytes
    txa                                                               ; 9106: 8a          .              ; A = byte count for setup_tx_and_send
    jsr setup_tx_and_send                                             ; 9107: 20 c0 90     ..            ; Build TXCB and transmit to terminal
    plp                                                               ; 910a: 28          (              ; Restore N flag from table match type
    bpl return_nbyte                                                  ; 910b: 10 1c       ..             ; Y was positive (NCTBPL): done, no result
    lda #&7f                                                          ; 910d: a9 7f       ..             ; Set up RX control block to wait for reply
    sta (net_tx_ptr,x)                                                ; 910f: 81 9a       ..             ; Write &7F to RXCB (wait for reply)
; &9111 referenced 1 time by &9113
.poll_rxcb_loop
    lda (net_tx_ptr,x)                                                ; 9111: a1 9a       ..             ; Poll RXCB for completion (bit7)
    bpl poll_rxcb_loop                                                ; 9113: 10 fc       ..             ; Bit7 clear: still waiting, poll again
    tsx                                                               ; 9115: ba          .              ; X = stack pointer for register restoration
    ldy #&dd                                                          ; 9116: a0 dd       ..             ; Y=&DD: saved P byte offset in workspace
    lda (nfs_workspace),y                                             ; 9118: b1 9e       ..             ; Load remote processor status from reply
    ora #&44 ; 'D'                                                    ; 911a: 09 44       .D             ; Force V=1 (claimed) and I=1 (no IRQ) in saved P
    bne nbyte5                                                        ; 911c: d0 04       ..             ; ALWAYS branch (ORA #&44 never zero); ALWAYS branch

; &911e referenced 1 time by &9127
.nbyte4
    dey                                                               ; 911e: 88          .              ; Previous workspace offset
    dex                                                               ; 911f: ca          .              ; Previous stack register slot
    lda (nfs_workspace),y                                             ; 9120: b1 9e       ..             ; Load next result byte (X, then Y)
; &9122 referenced 1 time by &911c
.nbyte5
    sta l0106,x                                                       ; 9122: 9d 06 01    ...            ; Write result bytes to stacked registers
    cpy #&da                                                          ; 9125: c0 da       ..             ; Copied all result bytes? (P at &DA)
    bne nbyte4                                                        ; 9127: d0 f5       ..             ; Loop for remaining result bytes
; &9129 referenced 2 times by &90f4, &910b
.return_nbyte
    rts                                                               ; 9129: 60          `              ; Return to OSBYTE dispatcher

; ***************************************************************************************
; Search remote OSBYTE table for match (NCALLP)
; 
; Searches remote_osbyte_table for OSBYTE code A. X indexes the
; last entry to check (table is scanned X..0). Returns Z=1 if
; found. Called twice by remote_cmd_dispatch:
; 
;   X=7  -> first 8 entries (NCTBPL: execute on both machines)
;   X=14 -> all 15 entries (NCTBMI: execute on terminal only)
; 
; The last 7 entries (&0B, &0C, &0F, &79, &7A, &E3, &E4) are terminal-only
; because they affect the local keyboard, buffers, or function keys.
; 
; On entry: A = OSBYTE code, X = table size - 1
; On exit:  Z=1 if match found, Z=0 if not
; ***************************************************************************************
; &912a referenced 3 times by &90e2, &90eb, &9130
.match_osbyte_code
    cmp remote_osbyte_table,x                                         ; 912a: dd 33 91    .3.            ; Compare OSBYTE code with table entry
    beq return_match_osbyte                                           ; 912d: f0 03       ..             ; Match found: return with Z=1
    dex                                                               ; 912f: ca          .              ; Next table entry (descending)
    bpl match_osbyte_code                                             ; 9130: 10 f8       ..             ; Loop for remaining entries
; &9132 referenced 2 times by &912d, &914a
.return_match_osbyte
    rts                                                               ; 9132: 60          `              ; Return; Z=1 if match, Z=0 if not

; &9133 referenced 1 time by &912a
.remote_osbyte_table
    equb 4                                                            ; 9133: 04          .              ; OSBYTE &04: cursor key status
    equb 9                                                            ; 9134: 09          .              ; OSBYTE &09: flash duration (1st colour)
    equb &0a                                                          ; 9135: 0a          .              ; OSBYTE &0A: flash duration (2nd colour)
    equb &14                                                          ; 9136: 14          .              ; OSBYTE &14: explode soft character RAM
    equb &9a                                                          ; 9137: 9a          .              ; OSBYTE &9A: video ULA control register
    equb &9b                                                          ; 9138: 9b          .              ; OSBYTE &9B: video ULA palette
    equb &9c                                                          ; 9139: 9c          .              ; OSBYTE &9C: ACIA control register
    equb &e2                                                          ; 913a: e2          .              ; OSBYTE &E2: function key &D0-&DF
    equb &0b                                                          ; 913b: 0b          .              ; OSBYTE &0B: auto-repeat delay
    equb &0c                                                          ; 913c: 0c          .              ; OSBYTE &0C: auto-repeat rate
    equb &0f                                                          ; 913d: 0f          .              ; OSBYTE &0F: flush buffer class
    equb &79                                                          ; 913e: 79          y              ; OSBYTE &79: keyboard scan from X
    equb &7a                                                          ; 913f: 7a          z              ; OSBYTE &7A: keyboard scan from &10
    equb &e3                                                          ; 9140: e3          .              ; OSBYTE &E3: function key &E0-&EF
    equb &e4                                                          ; 9141: e4          .              ; OSBYTE &E4: function key &F0-&FF

; ***************************************************************************************
; Fn 8: remote OSWORD handler (NWORD)
; 
; Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
; envelope). Unlike NBYTE which returns results, NWORD is entirely
; fire-and-forget -- no return path is implemented. The developer
; explicitly noted this was acceptable since sound/envelope commands
; don't return meaningful results. Copies up to 14 parameter bytes
; from the RX buffer to workspace, tags the message as RWORD, and
; transmits.
; ***************************************************************************************
.remote_cmd_data
    ldy #&0e                                                          ; 9142: a0 0e       ..             ; Y=14: max OSWORD parameter bytes
    cmp #7                                                            ; 9144: c9 07       ..             ; OSWORD 7 = make a sound
    beq copy_params_rword                                             ; 9146: f0 04       ..             ; OSWORD 7 (sound): handle via common path
    cmp #8                                                            ; 9148: c9 08       ..             ; OSWORD 8 = define an envelope
    bne return_match_osbyte                                           ; 914a: d0 e6       ..             ; Not OSWORD 7 or 8: ignore (BNE exits)
; &914c referenced 1 time by &9146
.copy_params_rword
    ldx #&db                                                          ; 914c: a2 db       ..             ; Point workspace to offset &DB for params
    stx nfs_workspace                                                 ; 914e: 86 9e       ..             ; Store workspace ptr offset &DB
; &9150 referenced 1 time by &9155
.copy_osword_params
    lda (osword_pb_ptr),y                                             ; 9150: b1 f0       ..             ; Load param byte from OSWORD param block
    sta (nfs_workspace),y                                             ; 9152: 91 9e       ..             ; Write param byte to workspace
    dey                                                               ; 9154: 88          .              ; Next byte (descending)
    bpl copy_osword_params                                            ; 9155: 10 f9       ..             ; Loop for all parameter bytes
    iny                                                               ; 9157: c8          .              ; Y=0 after loop
    dec nfs_workspace                                                 ; 9158: c6 9e       ..             ; Point workspace to offset &DA
    lda osbyte_a_copy                                                 ; 915a: a5 ef       ..             ; Load original OSWORD code
    sta (nfs_workspace),y                                             ; 915c: 91 9e       ..             ; Store OSWORD code at ws+0
    sty nfs_workspace                                                 ; 915e: 84 9e       ..             ; Reset workspace ptr to base
    ldy #&14                                                          ; 9160: a0 14       ..             ; Y=&14: command type offset
    lda #&e9                                                          ; 9162: a9 e9       ..             ; Tag as RWORD (port &E9)
    sta (nfs_workspace),y                                             ; 9164: 91 9e       ..             ; Store port tag at ws+&14
    lda #1                                                            ; 9166: a9 01       ..             ; A=1: single-byte TX
    jsr setup_tx_and_send                                             ; 9168: 20 c0 90     ..            ; Load template byte from ctrl_block_template[X]
    stx nfs_workspace                                                 ; 916b: 86 9e       ..             ; Restore workspace ptr
; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &837E to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &916d referenced 2 times by &905b, &906d
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 916d: a2 0d       ..             ; X=&0D: template offset for alt entry
    ldy #&7c ; '|'                                                    ; 916f: a0 7c       .|             ; Y=&7C: target workspace offset for alt entry
    bit tx_ctrl_upper                                                 ; 9171: 2c 7e 83    ,~.            ; BIT test: V flag = bit 6 of &837E
    bvs cbset2                                                        ; 9174: 70 05       p.             ; V=1: store to (net_rx_ptr) instead
; ***************************************************************************************
; Control block setup — main entry
; 
; Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
; Reads the template table at &91A2 indexed by X, storing each
; value into the target workspace at offset Y. Both X and Y
; are decremented on each iteration.
; 
; Template sentinel values:
;   &FE = stop (end of template for this entry path)
;   &FD = skip (leave existing value unchanged)
;   &FC = use page high byte of target pointer
; ***************************************************************************************
; &9176 referenced 1 time by &8499
.ctrl_block_setup
    ldy #&17                                                          ; 9176: a0 17       ..             ; Y=&17: workspace target offset (main entry)
    ldx #&1a                                                          ; 9178: a2 1a       ..             ; X=&1A: template table index (main entry)
; &917a referenced 1 time by &923e
.ctrl_block_setup_clv
    clv                                                               ; 917a: b8          .              ; V=0: target is (nfs_workspace)
; &917b referenced 2 times by &9174, &919c
.cbset2
    lda ctrl_block_template,x                                         ; 917b: bd a2 91    ...            ; Set up TX and send RWORD packet
    cmp #&fe                                                          ; 917e: c9 fe       ..             ; &FE = stop sentinel
    beq cb_template_tail                                              ; 9180: f0 1c       ..             ; End of template: jump to exit
    cmp #&fd                                                          ; 9182: c9 fd       ..             ; &FD = skip sentinel
    beq cb_template_main_start                                        ; 9184: f0 14       ..             ; Skip: don't store, just decrement Y
    cmp #&fc                                                          ; 9186: c9 fc       ..             ; &FC = page byte sentinel
    bne cbset3                                                        ; 9188: d0 08       ..             ; Not sentinel: store template value directly
    lda net_rx_ptr_hi                                                 ; 918a: a5 9d       ..             ; V=1: use (net_rx_ptr) page
    bvs rxcb_matched                                                  ; 918c: 70 02       p.             ; V=1: skip to net_rx_ptr page
    lda nfs_workspace_hi                                              ; 918e: a5 9f       ..             ; V=0: use (nfs_workspace) page
; &9190 referenced 1 time by &918c
.rxcb_matched
    sta net_tx_ptr_hi                                                 ; 9190: 85 9b       ..             ; PAGE byte → Y=&02 / Y=&74
; &9192 referenced 1 time by &9188
.cbset3
    bvs cbset4                                                        ; 9192: 70 04       p.             ; → Y=&04 / Y=&76
    sta (nfs_workspace),y                                             ; 9194: 91 9e       ..             ; PAGE byte → Y=&06 / Y=&78
    bvc cb_template_main_start                                        ; 9196: 50 02       P.             ; → Y=&08 / Y=&7A; ALWAYS branch

; &9198 referenced 1 time by &9192
.cbset4
    sta (net_rx_ptr),y                                                ; 9198: 91 9c       ..             ; Alt-path only → Y=&70
; &919a referenced 2 times by &9184, &9196
.cb_template_main_start
    dey                                                               ; 919a: 88          .              ; → Y=&0C (main only)
    dex                                                               ; 919b: ca          .              ; → Y=&0D (main only)
    bpl cbset2                                                        ; 919c: 10 dd       ..             ; Loop until all template bytes done
; &919e referenced 1 time by &9180
.cb_template_tail
    iny                                                               ; 919e: c8          .              ; → Y=&10 (main only)
    sty net_tx_ptr                                                    ; 919f: 84 9a       ..             ; Store final offset as net_tx_ptr
    rts                                                               ; 91a1: 60          `              ; → Y=&07 / Y=&79

; ***************************************************************************************
; Control block initialisation template
; 
; Read by the loop at &9168, indexed by X from a starting value
; down to 0. Values are stored into either (nfs_workspace) or
; (net_rx_ptr) at offset Y, depending on the V flag.
; 
; Two entry paths read different slices of this table:
;   ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
;   ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &837E
; 
; Sentinel values:
;   &FE = stop processing
;   &FD = skip this offset (decrement Y but don't store)
;   &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)
; ***************************************************************************************
; &91a2 referenced 1 time by &917b
.ctrl_block_template
    equb &85                                                          ; 91a2: 85          .              ; Alt-path only → Y=&6F
    equb 0                                                            ; 91a3: 00          .              ; Alt-path only → Y=&70
    equb &fd                                                          ; 91a4: fd          .              ; SKIP
    equb &fd                                                          ; 91a5: fd          .              ; SKIP
    equb &7d                                                          ; 91a6: 7d          }              ; → Y=&01 / Y=&73
    equb &fc                                                          ; 91a7: fc          .              ; PAGE byte → Y=&02 / Y=&74
    equb &ff                                                          ; 91a8: ff          .              ; → Y=&03 / Y=&75
    equb &ff                                                          ; 91a9: ff          .              ; → Y=&04 / Y=&76
    equb &7e                                                          ; 91aa: 7e          ~              ; → Y=&05 / Y=&77
    equb &fc                                                          ; 91ab: fc          .              ; PAGE byte → Y=&06 / Y=&78
    equb &ff                                                          ; 91ac: ff          .              ; → Y=&07 / Y=&79
    equb &ff                                                          ; 91ad: ff          .              ; → Y=&08 / Y=&7A
    equb 0                                                            ; 91ae: 00          .              ; → Y=&09 / Y=&7B
    equb 0                                                            ; 91af: 00          .              ; → Y=&0A / Y=&7C
    equb &fe                                                          ; 91b0: fe          .              ; STOP — main-path boundary
    equb &80                                                          ; 91b1: 80          .              ; → Y=&0C (main only)
    equb &93                                                          ; 91b2: 93          .              ; → Y=&0D (main only)
    equb &fd                                                          ; 91b3: fd          .              ; SKIP (main only)
    equb &fd                                                          ; 91b4: fd          .              ; SKIP (main only)
    equb &d9                                                          ; 91b5: d9          .              ; → Y=&10 (main only)
    equb &fc                                                          ; 91b6: fc          .              ; PAGE byte → Y=&11 (main only)
    equb &ff                                                          ; 91b7: ff          .              ; → Y=&12 (main only)
    equb &ff                                                          ; 91b8: ff          .              ; → Y=&13 (main only)
    equb &de                                                          ; 91b9: de          .              ; → Y=&14 (main only)
    equb &fc                                                          ; 91ba: fc          .              ; PAGE byte → Y=&15 (main only)
    equb &ff                                                          ; 91bb: ff          .              ; → Y=&16 (main only)
    equb &ff                                                          ; 91bc: ff          .              ; → Y=&17 (main only)
    equb &fe, &d1, &fd, &fd, &1f, &fd, &ff, &ff, &fd, &fd, &ff, &ff   ; 91bd: fe d1 fd... ...

; ***************************************************************************************
; Fn 5: printer selection changed (SELECT)
; 
; Called when the printer selection changes. Compares X against
; the network printer buffer number (&F0). If it matches,
; initialises the printer buffer pointer (&0D61 = &1F) and
; sets the initial flag byte (&0D60 = &41). Otherwise falls
; through to return.
; ***************************************************************************************
.printer_select_handler
    dex                                                               ; 91c9: ca          .              ; X-1: convert 1-based buffer to 0-based
    cpx osword_pb_ptr                                                 ; 91ca: e4 f0       ..             ; Is this the network printer buffer?
    bne setup1                                                        ; 91cc: d0 07       ..             ; No: skip printer init
    lda #&1f                                                          ; 91ce: a9 1f       ..             ; &1F = initial buffer pointer offset
    sta printer_buf_ptr                                               ; 91d0: 8d 61 0d    .a.            ; Reset printer buffer write position
    lda #&41 ; 'A'                                                    ; 91d3: a9 41       .A             ; &41 = initial PFLAGS (bit 6 set, bit 0 set)
; &91d5 referenced 1 time by &91cc
.setup1
    sta l0d60                                                         ; 91d5: 8d 60 0d    .`.            ; Store initial PFLAGS value
; &91d8 referenced 2 times by &91db, &91ef
.return_printer_select
    rts                                                               ; 91d8: 60          `              ; Return

; ***************************************************************************************
; Fn 1/2/3: network printer handler (PRINT)
; 
; Handles network printer output. Reason 1 = chars in buffer (extract
; from MOS buffer 3 and accumulate), reason 2 = Ctrl-B (start print),
; reason 3 = Ctrl-C (end print). The printer status byte PFLAGS uses:
;   bit 7 = sequence number (toggles per packet for dup detection)
;   bit 6 = always 1 (validity marker)
;   bit 0 = 0 when print active
; Print streams reuse the BSXMIT (byte-stream transmit) code with
; handle=0, which causes the AND SEQNOS to produce zero and sidestep
; per-file sequence tracking. After transmission, TXCB pointer bytes
; are filled with &FF to prevent stale values corrupting subsequent
; BGET/BPUT operations (a historically significant bug fix).
; N.B. The printer and REMOTE facility share the same dynamically
; allocated static workspace page via WORKP1 (&9E,&9F) — care must
; be taken to never leave the pointer corrupted, as corruption would
; cause one subsystem to overwrite the other's data.
; Only handles buffer 4 (network printer); others are ignored.
; ***************************************************************************************
.remote_print_handler
    cpy #4                                                            ; 91d9: c0 04       ..             ; Only handle buffer 4 (network printer)
    bne return_printer_select                                         ; 91db: d0 fb       ..             ; Not buffer 4: ignore
    txa                                                               ; 91dd: 8a          .              ; A = reason code
    dex                                                               ; 91de: ca          .              ; Reason 1? (DEX: 1->0)
    bne toggle_print_flag                                             ; 91df: d0 26       .&             ; Not reason 1: handle Ctrl-B/C
    tsx                                                               ; 91e1: ba          .              ; Get stack pointer for P register
    ora l0106,x                                                       ; 91e2: 1d 06 01    ...            ; Force I flag in stacked P to block IRQs
    sta l0106,x                                                       ; 91e5: 9d 06 01    ...            ; Write back modified P register
; &91e8 referenced 2 times by &91f7, &91fc
.prlp1
    lda #osbyte_read_buffer                                           ; 91e8: a9 91       ..             ; OSBYTE &91: extract char from MOS buffer
    ldx #buffer_printer                                               ; 91ea: a2 03       ..             ; X=3: printer buffer number
    jsr osbyte                                                        ; 91ec: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_printer_select                                         ; 91ef: b0 e7       ..             ; Buffer empty: return
    tya                                                               ; 91f1: 98          .              ; Y = extracted character; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91f2: 20 fe 91     ..            ; Store char in output buffer
    cpy #&6e ; 'n'                                                    ; 91f5: c0 6e       .n             ; Buffer nearly full? (&6E = threshold)
    bcc prlp1                                                         ; 91f7: 90 ef       ..             ; Not full: get next char
    jsr flush_output_block                                            ; 91f9: 20 2a 92     *.            ; Buffer full: flush to network
    bcc prlp1                                                         ; 91fc: 90 ea       ..             ; Continue after flush
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; ***************************************************************************************
; &91fe referenced 2 times by &91f2, &920b
.store_output_byte
    ldy printer_buf_ptr                                               ; 91fe: ac 61 0d    .a.            ; Y = current printer buffer offset
    sta (net_rx_ptr),y                                                ; 9201: 91 9c       ..             ; Store byte at current position
    inc printer_buf_ptr                                               ; 9203: ee 61 0d    .a.            ; Advance buffer pointer
    rts                                                               ; 9206: 60          `              ; Return; Y = buffer offset

; &9207 referenced 1 time by &91df
.toggle_print_flag
    pha                                                               ; 9207: 48          H              ; Save reason code
    txa                                                               ; 9208: 8a          .              ; A = reason code
    eor #1                                                            ; 9209: 49 01       I.             ; EOR #1: toggle print-active flag (bit 0)
    jsr store_output_byte                                             ; 920b: 20 fe 91     ..            ; Store toggled flag as output byte
    eor l0d60                                                         ; 920e: 4d 60 0d    M`.            ; XOR with current PFLAGS
    ror a                                                             ; 9211: 6a          j              ; Test if sequence changed (bit 7 mismatch)
    bcc pril1                                                         ; 9212: 90 07       ..             ; Sequence unchanged: skip flush
    rol a                                                             ; 9214: 2a          *              ; Undo ROR
    sta l0d60                                                         ; 9215: 8d 60 0d    .`.            ; Store toggled PFLAGS
    jsr flush_output_block                                            ; 9218: 20 2a 92     *.            ; Flush current output block
; &921b referenced 1 time by &9212
.pril1
    lda l0d60                                                         ; 921b: ad 60 0d    .`.            ; Reload current PFLAGS
    and #&f0                                                          ; 921e: 29 f0       ).             ; Extract upper nibble of PFLAGS
    ror a                                                             ; 9220: 6a          j              ; Shift for bit extraction
    tax                                                               ; 9221: aa          .              ; Save in X
    pla                                                               ; 9222: 68          h              ; Restore original reason code
    ror a                                                             ; 9223: 6a          j              ; Merge print-active bit from original A
    txa                                                               ; 9224: 8a          .              ; Retrieve shifted PFLAGS
    rol a                                                             ; 9225: 2a          *              ; Recombine into new PFLAGS value
    sta l0d60                                                         ; 9226: 8d 60 0d    .`.            ; Store recombined PFLAGS value
    rts                                                               ; 9229: 60          `              ; Return

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &922a referenced 2 times by &91f9, &9218
.flush_output_block
    ldy #8                                                            ; 922a: a0 08       ..             ; Store buffer length at workspace offset &08
    lda printer_buf_ptr                                               ; 922c: ad 61 0d    .a.            ; Current buffer fill position
    sta (nfs_workspace),y                                             ; 922f: 91 9e       ..             ; Write to workspace offset &08
    lda net_rx_ptr_hi                                                 ; 9231: a5 9d       ..             ; Store page high byte at offset &09
    iny                                                               ; 9233: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 9234: 91 9e       ..             ; Write page high byte at offset &09
    ldy #5                                                            ; 9236: a0 05       ..             ; Also store at offset &05
    sta (nfs_workspace),y                                             ; 9238: 91 9e       ..             ; (end address high byte)
    ldy #&0b                                                          ; 923a: a0 0b       ..             ; Y=&0B: flag byte offset
    ldx #&26 ; '&'                                                    ; 923c: a2 26       .&             ; X=&26: start from template entry &26
    jsr ctrl_block_setup_clv                                          ; 923e: 20 7a 91     z.            ; Reuse ctrl_block_setup with CLV entry
    dey                                                               ; 9241: 88          .              ; Y=&0A: sequence flag byte offset
    lda l0d60                                                         ; 9242: ad 60 0d    .`.            ; Load current PFLAGS
    pha                                                               ; 9245: 48          H              ; Save current PFLAGS
    rol a                                                             ; 9246: 2a          *              ; Carry = current sequence (bit 7)
    pla                                                               ; 9247: 68          h              ; Restore original PFLAGS
    eor #&80                                                          ; 9248: 49 80       I.             ; Toggle sequence number (bit 7 of PFLAGS)
    sta l0d60                                                         ; 924a: 8d 60 0d    .`.            ; Store toggled sequence number
    rol a                                                             ; 924d: 2a          *              ; Old sequence bit into bit 0
    sta (nfs_workspace),y                                             ; 924e: 91 9e       ..             ; Store sequence flag at offset &0A
    ldy #&1f                                                          ; 9250: a0 1f       ..             ; Y=&1F: buffer start offset
    sty printer_buf_ptr                                               ; 9252: 8c 61 0d    .a.            ; Reset printer buffer to start (&1F)
    lda #0                                                            ; 9255: a9 00       ..             ; A=0: printer output flag
    tax                                                               ; 9257: aa          .              ; X=0: workspace low byte; X=&00
    ldy nfs_workspace_hi                                              ; 9258: a4 9f       ..             ; Y = workspace page high byte
    cli                                                               ; 925a: 58          X              ; Enable interrupts before TX
; ***************************************************************************************
; Transmit with retry loop (XMITFS/XMITFY)
; 
; Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
; retries and FSDELY (&60 = 96) ms delay between attempts. On each
; iteration, checks the result code: zero means success, non-zero
; means retry. After all retries exhausted, reports a 'Net error'.
; Entry point XMITFY allows a custom delay in Y.
; ***************************************************************************************
; &925b referenced 2 times by &83e5, &841e
.econet_tx_retry
    stx net_tx_ptr                                                    ; 925b: 86 9a       ..             ; Set TX control block ptr low byte
    sty net_tx_ptr_hi                                                 ; 925d: 84 9b       ..             ; Set TX control block ptr high byte
    pha                                                               ; 925f: 48          H              ; Save A (handle bitmask) for later
    and fs_sequence_nos                                               ; 9260: 2d 08 0e    -..            ; Compute sequence bit from handle
    beq bsxl1                                                         ; 9263: f0 02       ..             ; Zero: no sequence bit set
    lda #1                                                            ; 9265: a9 01       ..             ; Non-zero: normalise to bit 0
; &9267 referenced 1 time by &9263
.bsxl1
    ldy #0                                                            ; 9267: a0 00       ..             ; Y=0: flag byte offset in TXCB
    ora (net_tx_ptr),y                                                ; 9269: 11 9a       ..             ; Merge sequence into existing flag byte
    pha                                                               ; 926b: 48          H              ; Save merged flag byte
    sta (net_tx_ptr),y                                                ; 926c: 91 9a       ..             ; Write flag+sequence to TXCB byte 0
    jsr tx_poll_ff                                                    ; 926e: 20 71 86     q.            ; Transmit with full retry
    lda #&ff                                                          ; 9271: a9 ff       ..             ; End address &FFFF = unlimited data length
    ldy #8                                                            ; 9273: a0 08       ..             ; Y=8: end address low offset in TXCB
    sta (net_tx_ptr),y                                                ; 9275: 91 9a       ..             ; Store &FF to end addr low
    iny                                                               ; 9277: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 9278: 91 9a       ..             ; Store &FF to end addr high (Y=9)
    pla                                                               ; 927a: 68          h              ; Recover merged flag byte
    tax                                                               ; 927b: aa          .              ; Save in X for sequence compare
    ldy #&d1                                                          ; 927c: a0 d1       ..             ; Y=&D1: printer port number
    pla                                                               ; 927e: 68          h              ; Recover saved handle bitmask
    pha                                                               ; 927f: 48          H              ; Re-save for later consumption
    beq bspsx                                                         ; 9280: f0 02       ..             ; A=0: port &D1 (print); A!=0: port &90 (FS)
    ldy #&90                                                          ; 9282: a0 90       ..             ; Y=&90: FS data port
; &9284 referenced 1 time by &9280
.bspsx
    tya                                                               ; 9284: 98          .              ; A = selected port number
    ldy #1                                                            ; 9285: a0 01       ..             ; Y=1: port byte offset in TXCB
    sta (net_tx_ptr),y                                                ; 9287: 91 9a       ..             ; Write port to TXCB byte 1
    txa                                                               ; 9289: 8a          .              ; A = saved flag byte (expected sequence)
    dey                                                               ; 928a: 88          .              ; Y=&00
    pha                                                               ; 928b: 48          H              ; Push expected sequence for retry loop
; &928c referenced 1 time by &9298
.bsxl0
    lda #&7f                                                          ; 928c: a9 7f       ..             ; Flag byte &7F = waiting for reply
    sta (net_tx_ptr),y                                                ; 928e: 91 9a       ..             ; Write to TXCB flag byte (Y=0)
    jsr send_to_fs_star                                               ; 9290: 20 f8 84     ..            ; Transmit and wait for reply (BRIANX)
    pla                                                               ; 9293: 68          h              ; Recover expected sequence
    pha                                                               ; 9294: 48          H              ; Keep on stack for next iteration
    eor (net_tx_ptr),y                                                ; 9295: 51 9a       Q.             ; Check if TX result matches expected sequence
    ror a                                                             ; 9297: 6a          j              ; Bit 0 to carry (sequence mismatch?)
    bcs bsxl0                                                         ; 9298: b0 f2       ..             ; C=1: mismatch, retry transmit
    pla                                                               ; 929a: 68          h              ; Clean up: discard expected sequence
    pla                                                               ; 929b: 68          h              ; Discard saved handle bitmask
    tax                                                               ; 929c: aa          .              ; Transfer count to X
    inx                                                               ; 929d: e8          .              ; Test for retry exhaustion
    beq return_bspsx                                                  ; 929e: f0 03       ..             ; X wrapped to 0: retries exhausted
    eor fs_sequence_nos                                               ; 92a0: 4d 08 0e    M..            ; Toggle sequence bit on success
; &92a3 referenced 1 time by &929e
.return_bspsx
    rts                                                               ; 92a3: 60          `              ; Return

; ***************************************************************************************
; Save palette and VDU state (CVIEW)
; 
; Part of the VIEW facility (second iteration, started 27/7/82).
; Uses dynamically allocated buffer store. The WORKP1 pointer
; (&9E,&9F) serves double duty: non-zero indicates data ready AND
; provides the buffer address — an efficient use of scarce zero-
; page space. This code must be user-transparent as the NFS may not
; be the dominant filing system.
; Reads all 16 palette entries using OSWORD &0B (read palette) and
; stores the results. Then reads cursor position (OSBYTE &85),
; shadow RAM allocation (OSBYTE &C2), and screen start address
; (OSBYTE &C3) using the 3-entry table at &9305 (osbyte_vdu_table).
; On completion, restores the JSR buffer protection bits (LSTAT)
; from OLDJSR to re-enable JSR reception, which was disabled during
; the screen data capture to prevent interference.
; ***************************************************************************************
.lang_2_save_palette_vdu
    lda table_idx                                                     ; 92a4: a5 ad       ..             ; Save current table index
    pha                                                               ; 92a6: 48          H              ; Push for later restore
    lda #&e9                                                          ; 92a7: a9 e9       ..             ; Point workspace to palette save area (&E9)
    sta nfs_workspace                                                 ; 92a9: 85 9e       ..             ; Set workspace low byte
    ldy #0                                                            ; 92ab: a0 00       ..             ; Y=0: first palette entry
    sty table_idx                                                     ; 92ad: 84 ad       ..             ; Clear table index counter
    lda l0350                                                         ; 92af: ad 50 03    .P.            ; Save current screen MODE to workspace
    sta (nfs_workspace),y                                             ; 92b2: 91 9e       ..             ; Store MODE at workspace[0]
    inc nfs_workspace                                                 ; 92b4: e6 9e       ..             ; Advance workspace pointer past MODE byte
    lda l0351                                                         ; 92b6: ad 51 03    .Q.            ; Read colour count (from &0351)
    pha                                                               ; 92b9: 48          H              ; Push for iteration count tracking
    tya                                                               ; 92ba: 98          .              ; A=0: logical colour number for OSWORD; A=&00
; &92bb referenced 1 time by &92da
.save_palette_entry
    sta (nfs_workspace),y                                             ; 92bb: 91 9e       ..             ; Store logical colour at workspace[0]
    ldx nfs_workspace                                                 ; 92bd: a6 9e       ..             ; X = workspace ptr low (param block addr)
    ldy nfs_workspace_hi                                              ; 92bf: a4 9f       ..             ; Y = workspace ptr high
    lda #osword_read_palette                                          ; 92c1: a9 0b       ..             ; OSWORD &0B: read palette for logical colour
    jsr osword                                                        ; 92c3: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92c6: 68          h              ; Recover colour count
    ldy #0                                                            ; 92c7: a0 00       ..             ; Y=0: access workspace[0]
    sta (nfs_workspace),y                                             ; 92c9: 91 9e       ..             ; Write colour count back to workspace[0]
    iny                                                               ; 92cb: c8          .              ; Y=1: access workspace[1] (palette result); Y=&01
    lda (nfs_workspace),y                                             ; 92cc: b1 9e       ..             ; Read palette value returned by OSWORD
    pha                                                               ; 92ce: 48          H              ; Push palette value for next iteration
    ldx nfs_workspace                                                 ; 92cf: a6 9e       ..             ; X = current workspace ptr low
    inc nfs_workspace                                                 ; 92d1: e6 9e       ..             ; Advance workspace pointer
    inc table_idx                                                     ; 92d3: e6 ad       ..             ; Increment table index
    dey                                                               ; 92d5: 88          .              ; Y=0 for next store; Y=&00
    lda table_idx                                                     ; 92d6: a5 ad       ..             ; Load table index as logical colour
    cpx #&f9                                                          ; 92d8: e0 f9       ..             ; Loop until workspace wraps past &F9
    bne save_palette_entry                                            ; 92da: d0 df       ..             ; Continue for all 16 palette entries
    pla                                                               ; 92dc: 68          h              ; Discard last palette value from stack
    sty table_idx                                                     ; 92dd: 84 ad       ..             ; Reset table index to 0
    inc nfs_workspace                                                 ; 92df: e6 9e       ..             ; Advance workspace past palette data
    jsr save_vdu_state                                                ; 92e1: 20 f0 92     ..            ; Save cursor pos and OSBYTE state values
    inc nfs_workspace                                                 ; 92e4: e6 9e       ..             ; Advance workspace past VDU state data
    pla                                                               ; 92e6: 68          h              ; Recover saved table index
    sta table_idx                                                     ; 92e7: 85 ad       ..             ; Restore table index
; &92e9 referenced 4 times by &847d, &84a5, &84cc, &8eec
.clear_jsr_protection
    lda saved_jsr_mask                                                ; 92e9: ad 65 0d    .e.            ; Restore LSTAT from saved OLDJSR value
    sta prot_status                                                   ; 92ec: 8d 63 0d    .c.            ; Write to protection status
    rts                                                               ; 92ef: 60          `              ; Return

; ***************************************************************************************
; Save VDU workspace state
; 
; Stores the cursor position value from &0355 into NFS workspace,
; then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
; and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
; each result into consecutive workspace bytes.
; ***************************************************************************************
; &92f0 referenced 1 time by &92e1
.save_vdu_state
    lda l0355                                                         ; 92f0: ad 55 03    .U.            ; Read cursor editing state
    sta (nfs_workspace),y                                             ; 92f3: 91 9e       ..             ; Store to workspace[Y]
    tax                                                               ; 92f5: aa          .              ; Preserve in X for OSBYTE
    jsr read_vdu_osbyte                                               ; 92f6: 20 03 93     ..            ; OSBYTE &85: read cursor position
    inc nfs_workspace                                                 ; 92f9: e6 9e       ..             ; Advance workspace pointer
    tya                                                               ; 92fb: 98          .              ; Y result from OSBYTE &85
    sta (nfs_workspace,x)                                             ; 92fc: 81 9e       ..             ; Store Y pos to workspace (X=0)
    jsr read_vdu_osbyte_x0                                            ; 92fe: 20 01 93     ..            ; Self-call trick: executes twice
; &9301 referenced 1 time by &92fe
.read_vdu_osbyte_x0
    ldx #0                                                            ; 9301: a2 00       ..             ; X=0 for (zp,X) addressing
; &9303 referenced 1 time by &92f6
.read_vdu_osbyte
    ldy table_idx                                                     ; 9303: a4 ad       ..             ; Index into OSBYTE number table
    inc table_idx                                                     ; 9305: e6 ad       ..             ; Next table entry next time
    inc nfs_workspace                                                 ; 9307: e6 9e       ..             ; Advance workspace pointer
    lda osbyte_vdu_table,y                                            ; 9309: b9 17 93    ...            ; Read OSBYTE number from table
    ldy #&ff                                                          ; 930c: a0 ff       ..             ; Y=&FF: read current value
    jsr osbyte                                                        ; 930e: 20 f4 ff     ..            ; Call OSBYTE
    txa                                                               ; 9311: 8a          .              ; Result in X to A
    ldx #0                                                            ; 9312: a2 00       ..             ; X=0 for indexed indirect store
    sta (nfs_workspace,x)                                             ; 9314: 81 9e       ..             ; Store result to workspace
    rts                                                               ; 9316: 60          `              ; Return after storing result

; 3-entry OSBYTE table for lang_2_save_palette_vdu (&92A4)
; &9317 referenced 1 time by &9309
.osbyte_vdu_table
    equb &85                                                          ; 9317: 85          .              ; OSBYTE &85: read cursor position
    equb &c2                                                          ; 9318: c2          .              ; OSBYTE &C2: read shadow RAM allocation
    equb &c3                                                          ; 9319: c3          .              ; OSBYTE &C3: read screen start address
; &931a referenced 1 time by &8144

    org &965f

    equb 0                                                            ; 965f: 00          .

; &9660 referenced 2 times by &868c, &8ed7
.trampoline_tx_setup
    jmp tx_begin                                                      ; 9660: 4c f3 9b    L..            ; Trampoline: forward to tx_begin

; &9663 referenced 1 time by &830d
.trampoline_adlc_init
    jmp adlc_init                                                     ; 9663: 4c 6f 96    Lo.            ; Trampoline: forward to adlc_init

.svc_12_nmi_release
    jmp wait_nmi_ready                                                ; 9666: 4c b1 96    L..            ; Trampoline: forward to NMI release

.svc_11_nmi_claim
    jmp restore_econet_state                                          ; 9669: 4c dc 96    L..            ; Trampoline: forward to NMI claim

.svc_5_unknown_irq
    jmp check_sr_irq                                                  ; 966c: 4c 61 9b    La.            ; Trampoline: forward to IRQ handler

; ***************************************************************************************
; ADLC initialisation
; 
; Reads station ID (INTOFF side effect), performs full ADLC reset,
; checks for Tube presence (OSBYTE &EA), then falls through to
; adlc_init_workspace.
; ***************************************************************************************
; &966f referenced 1 time by &9663
.adlc_init
    bit station_id_disable_net_nmis                                   ; 966f: 2c 18 fe    ,..            ; INTOFF: read station ID, disable NMIs
    jsr adlc_full_reset                                               ; 9672: 20 e6 96     ..            ; Full ADLC hardware reset
    lda #osbyte_read_tube_presence                                    ; 9675: a9 ea       ..             ; OSBYTE &EA: check Tube co-processor
    ldx #0                                                            ; 9677: a2 00       ..             ; X=0 for OSBYTE
    ldy #&ff                                                          ; 9679: a0 ff       ..             ; Y=&FF for OSBYTE
    jsr osbyte                                                        ; 967b: 20 f4 ff     ..            ; Read Tube present flag
    stx tx_in_progress                                                ; 967e: 8e 52 0d    .R.            ; X=value of Tube present flag
    lda #osbyte_issue_service_request                                 ; 9681: a9 8f       ..             ; OSBYTE &8F: issue service request
    ldx #&0c                                                          ; 9683: a2 0c       ..             ; X=&0C: NMI claim service
    ldy #&ff                                                          ; 9685: a0 ff       ..             ; Y=&FF: pass to adlc_init_workspace
; ***************************************************************************************
; Initialise NMI workspace
; 
; New in 3.35D: issues OSBYTE &8F with X=&0C (NMI claim service
; request) before copying the NMI shim. Sub-entry at &968A skips
; the service request for quick re-init. Then copies 32 bytes of
; NMI shim from ROM (&9FD9) to RAM (&0D00), patches the current
; ROM bank number into the shim's self-modifying code at &0D07,
; sets TX clear flag and econet_init_flag to &80, reads station ID
; from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
; and re-enables NMIs by reading &FE20 (INTON side effect).
; ***************************************************************************************
.adlc_init_workspace
    jsr osbyte                                                        ; 9687: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=12 - NMI claim
; ***************************************************************************************
; Initialise NMI workspace (skip service request)
; 
; Sub-entry of adlc_init_workspace that skips the OSBYTE &8F
; service request. Copies 32 bytes of NMI shim from ROM to
; &0D00, patches the ROM bank number, sets init flags, reads
; station ID, and re-enables NMIs.
; ***************************************************************************************
; &968a referenced 1 time by &96e3
.init_nmi_workspace
    ldy #&20 ; ' '                                                    ; 968a: a0 20       .              ; Copy 32 bytes of NMI shim from ROM to &0D00
; &968c referenced 1 time by &9693
.copy_nmi_shim
    lda nmi_shim_rom_src,y                                            ; 968c: b9 d9 9f    ...            ; Read byte from NMI shim ROM source
    sta l0cff,y                                                       ; 968f: 99 ff 0c    ...            ; Write to NMI shim RAM at &0D00
    dey                                                               ; 9692: 88          .              ; Next byte (descending)
    bne copy_nmi_shim                                                 ; 9693: d0 f7       ..             ; Loop until all 32 bytes copied
    lda romsel_copy                                                   ; 9695: a5 f4       ..             ; Patch current ROM bank into NMI shim
    sta nmi_shim_07                                                   ; 9697: 8d 07 0d    ...            ; Self-modifying code: ROM bank at &0D07
    lda #&80                                                          ; 969a: a9 80       ..             ; &80 = Econet initialised
    sta tx_clear_flag                                                 ; 969c: 8d 62 0d    .b.            ; Mark TX as complete (ready)
    sta econet_init_flag                                              ; 969f: 8d 66 0d    .f.            ; Mark Econet as initialised
    lda station_id_disable_net_nmis                                   ; 96a2: ad 18 fe    ...            ; Read station ID (&FE18 = INTOFF side effect)
    sta tx_src_stn                                                    ; 96a5: 8d 22 0d    .".            ; Store our station ID in TX scout
    lda #0                                                            ; 96a8: a9 00       ..             ; A=0: clear source network
    sta tx_src_net                                                    ; 96aa: 8d 23 0d    .#.            ; Clear TX source network byte
    bit video_ula_control                                             ; 96ad: 2c 20 fe    , .            ; INTON: re-enable NMIs (&FE20 read side effect)
    rts                                                               ; 96b0: 60          `              ; Return to caller

; ***************************************************************************************
; Wait for NMI subsystem ready and save Econet state
; 
; Clears the TX complete flag, then polls econet_init_flag
; until the NMI subsystem reports initialised. Validates the
; NMI jump vector points to the expected handler (&9700) by
; polling nmi_jmp_lo/hi in a tight loop. Once validated,
; disables NMIs via INTOFF and falls through to
; save_econet_state. Called from save_vdu_state during
; VDU state preservation.
; ***************************************************************************************
; &96b1 referenced 1 time by &9666
.wait_nmi_ready
    lda #0                                                            ; 96b1: a9 00       ..             ; A=0: clear TX complete flag
    sta tx_clear_flag                                                 ; 96b3: 8d 62 0d    .b.            ; Clear TX complete flag
.poll_nmi_ready
    bit econet_init_flag                                              ; 96b6: 2c 66 0d    ,f.            ; Poll Econet init status
    bpl jmp_rx_listen                                                 ; 96b9: 10 1e       ..             ; Not initialised: skip to RX listen
    sta econet_init_flag                                              ; 96bb: 8d 66 0d    .f.            ; Clear Econet init flag
; &96be referenced 2 times by &96c3, &96ca
.nmi_vec_lo_match
    lda nmi_jmp_lo                                                    ; 96be: ad 0c 0d    ...            ; Load NMI vector low byte
    cmp #0                                                            ; 96c1: c9 00       ..             ; Check if low byte is expected value
    bne nmi_vec_lo_match                                              ; 96c3: d0 f9       ..             ; Mismatch: keep polling
    lda nmi_jmp_hi                                                    ; 96c5: ad 0d 0d    ...            ; Load NMI vector high byte
    cmp #&97                                                          ; 96c8: c9 97       ..             ; Check if high byte is &97
    bne nmi_vec_lo_match                                              ; 96ca: d0 f2       ..             ; Mismatch: keep polling
    bit station_id_disable_net_nmis                                   ; 96cc: 2c 18 fe    ,..            ; BIT INTOFF: disable NMIs
; ***************************************************************************************
; Save Econet state to RX control block
; 
; Stores rx_status_flags, protection_mask, and tx_in_progress
; to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.
; ***************************************************************************************
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 96cf: 2c 18 fe    ,..            ; INTOFF: disable NMIs
    ldy #8                                                            ; 96d2: a0 08       ..             ; Y=8: RXCB offset for TX status
    lda tx_in_progress                                                ; 96d4: ad 52 0d    .R.            ; Load current TX status flag
    sta (net_rx_ptr),y                                                ; 96d7: 91 9c       ..             ; Save TX status in RXCB
; &96d9 referenced 1 time by &96b9
.jmp_rx_listen
    jmp adlc_rx_listen                                                ; 96d9: 4c f5 96    L..            ; Enter RX listen mode

; ***************************************************************************************
; Restore Econet TX state and re-enter RX listen
; 
; Loads the saved tx_in_progress flag from RXCB offset 8
; (previously stored by save_econet_state) and restores it.
; Then jumps to init_nmi_workspace to re-initialise the NMI
; handler and return to idle RX listen mode. Called from
; save_vdu_state during VDU state restoration.
; ***************************************************************************************
; &96dc referenced 1 time by &9669
.restore_econet_state
    ldy #8                                                            ; 96dc: a0 08       ..             ; Y=8: RXCB offset for TX status
    lda (net_rx_ptr),y                                                ; 96de: b1 9c       ..             ; Load saved TX status from RXCB
    sta tx_in_progress                                                ; 96e0: 8d 52 0d    .R.            ; Restore TX status flag
.enter_rx_listen
    jmp init_nmi_workspace                                            ; 96e3: 4c 8a 96    L..            ; Re-enter idle RX listen mode

; ***************************************************************************************
; ADLC full reset
; 
; Aborts all activity and returns to idle RX listen mode.
; ***************************************************************************************
; &96e6 referenced 3 times by &9672, &9748, &989e
.adlc_full_reset
    lda #&c1                                                          ; 96e6: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 96e8: 8d a0 fe    ...            ; Write CR1: full reset
    lda #&1e                                                          ; 96eb: a9 1e       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding
    sta econet_data_terminate_frame                                   ; 96ed: 8d a3 fe    ...            ; Write CR4 via ADLC reg 3 (AC=1)
    lda #0                                                            ; 96f0: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 96f2: 8d a1 fe    ...            ; Write CR3=0: clear loop-back/AEX/DTR
; ***************************************************************************************
; Enter RX listen mode
; 
; TX held in reset, RX active with interrupts. Clears all status.
; ***************************************************************************************
; &96f5 referenced 2 times by &96d9, &9a56
.adlc_rx_listen
    lda #&82                                                          ; 96f5: a9 82       ..             ; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 96f7: 8d a0 fe    ...            ; Write CR1: RIE | TX_RESET
    lda #&67 ; 'g'                                                    ; 96fa: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 96fc: 8d a1 fe    ...            ; Write CR2: listen mode config
    rts                                                               ; 96ff: 60          `              ; Return

; ***************************************************************************************
; NMI RX scout handler (initial byte)
; 
; Default NMI handler for incoming scout frames. Checks if the frame
; is addressed to us or is a broadcast. Installed as the NMI target
; during idle RX listen mode.
; Tests SR2 bit0 (AP = Address Present) to detect incoming data.
; Reads the first byte (destination station) from the RX FIFO and
; compares against our station ID. Reading &FE18 also disables NMIs
; (INTOFF side effect).
; ***************************************************************************************
; &9700 referenced 1 time by &9fe5
.nmi_rx_scout
    lda #1                                                            ; 9700: a9 01       ..             ; A=&01: mask for SR2 bit0 (AP = Address Present)
    bit econet_control23_or_status2                                   ; 9702: 2c a1 fe    ,..            ; BIT SR2: Z = A AND SR2 -- tests if AP is set
    beq scout_error                                                   ; 9705: f0 3a       .:             ; AP not set, no incoming data -- check for errors
    lda econet_data_continue_frame                                    ; 9707: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 970a: cd 18 fe    ...            ; Compare to our station ID (&FE18 read = INTOFF, disables NMIs)
    beq accept_frame                                                  ; 970d: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 970f: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 9711: d0 1a       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 9713: a9 40       .@             ; Flag &40 = broadcast frame
    sta tx_flags                                                      ; 9715: 8d 4a 0d    .J.            ; Store broadcast flag in TX flags
; &9718 referenced 1 time by &970d
.accept_frame
    lda #&1f                                                          ; 9718: a9 1f       ..             ; Install next NMI handler at &971F (RX scout net byte)
    ldy #&97                                                          ; 971a: a0 97       ..             ; High byte of scout net handler
    jmp set_nmi_vector                                                ; 971c: 4c 0e 0d    L..            ; Install next handler and RTI

; ***************************************************************************************
; RX scout second byte handler
; 
; Reads the second byte of an incoming scout (destination network).
; Checks for network match: 0 = local network (accept), &FF = broadcast
; (accept and flag), anything else = reject.
; Installs the scout data reading loop handler at &9751.
; ***************************************************************************************
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 971f: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 9722: 10 1d       ..             ; No RDA -- check errors
    lda econet_data_continue_frame                                    ; 9724: ad a2 fe    ...            ; Read destination network byte
    beq accept_local_net                                              ; 9727: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 9729: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq accept_scout_net                                              ; 972b: f0 0b       ..             ; Broadcast network -- accept
; &972d referenced 1 time by &9711
.scout_reject
    lda #&a2                                                          ; 972d: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 972f: 8d a0 fe    ...            ; Write CR1 to discontinue RX
    jmp install_rx_scout_handler                                      ; 9732: 4c 59 9a    LY.            ; Return to idle scout listening

; &9735 referenced 1 time by &9727
.accept_local_net
    sta tx_flags                                                      ; 9735: 8d 4a 0d    .J.            ; Network = 0 (local): clear tx_flags
; &9738 referenced 1 time by &972b
.accept_scout_net
    sta port_buf_len                                                  ; 9738: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&51 ; 'Q'                                                    ; 973a: a9 51       .Q             ; Install scout data reading loop at &9751
    ldy #&97                                                          ; 973c: a0 97       ..             ; High byte of scout data handler
    jmp set_nmi_vector                                                ; 973e: 4c 0e 0d    L..            ; Install scout data loop and RTI

; ***************************************************************************************
; Scout error/discard handler
; 
; Reached when the scout data loop sees no RDA (BPL at &9756) or
; when scout completion finds unexpected SR2 state.
; Reads SR2 and tests AP|RDA bits. If non-zero, performs full
; ADLC reset and discards. If zero (clean end), discards via scout_discard.
; This path is a common landing for any unexpected ADLC state during
; scout reception.
; ***************************************************************************************
; &9741 referenced 5 times by &9705, &9722, &9756, &978a, &978c
.scout_error
    lda econet_control23_or_status2                                   ; 9741: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 9744: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 9746: f0 06       ..             ; Neither set -- clean end, discard via &974E
    jsr adlc_full_reset                                               ; 9748: 20 e6 96     ..            ; Unexpected data/status: full ADLC reset
    jmp install_rx_scout_handler                                      ; 974b: 4c 59 9a    LY.            ; Discard and return to idle

; &974e referenced 1 time by &9746
.scout_discard
    jmp discard_listen                                                ; 974e: 4c 56 9a    LV.            ; Gentle discard: RX_DISCONTINUE

; ***************************************************************************************
; Scout data reading loop
; 
; Reads the body of a scout frame, two bytes per iteration. Stores
; bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
; Between each pair it checks SR2:
;   - SR2 read at entry (&9753)
;     - No RDA (BPL) -> error (&9741)
;     - RDA set (BMI) -> read byte
;   - After first byte (&975F): full SR2 tested
;     - SR2 non-zero (BNE) -> scout completion (&977B)
;       This is the FV detection point: when FV is set (by inline refill
;       of the last byte during the preceding RX FIFO read), SR2 is
;       non-zero and the branch is taken.
;     - SR2 = 0 -> read second byte and loop
;   - After second byte (&9773): re-test SR2 for next pair
;     - RDA set (BMI) -> loop back to &9758
;     - Neither set -> RTI, wait for next NMI
; The loop ends at Y=&0C (12 bytes max in scout buffer).
; ***************************************************************************************
.scout_data_loop
    ldy port_buf_len                                                  ; 9751: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 9753: ad a1 fe    ...            ; Read SR2
; &9756 referenced 1 time by &9776
.scout_loop_rda
    bpl scout_error                                                   ; 9756: 10 e9       ..             ; No RDA -- error handler &9741
    lda econet_data_continue_frame                                    ; 9758: ad a2 fe    ...            ; Read data byte from RX FIFO
    sta rx_src_stn,y                                                  ; 975b: 99 3d 0d    .=.            ; Store at &0D3D+Y (scout buffer)
    iny                                                               ; 975e: c8          .              ; Advance buffer index
    lda econet_control23_or_status2                                   ; 975f: ad a1 fe    ...            ; Read SR2 again (FV detection point)
    bmi scout_loop_second                                             ; 9762: 30 02       0.             ; RDA set -- more data, read second byte
    bne scout_complete                                                ; 9764: d0 15       ..             ; SR2 non-zero (FV or other) -- scout completion
; &9766 referenced 1 time by &9762
.scout_loop_second
    lda econet_data_continue_frame                                    ; 9766: ad a2 fe    ...            ; Read second byte of pair
    sta rx_src_stn,y                                                  ; 9769: 99 3d 0d    .=.            ; Store at &0D3D+Y
    iny                                                               ; 976c: c8          .              ; Advance and check buffer limit
    cpy #&0c                                                          ; 976d: c0 0c       ..             ; Copied all 12 scout bytes?
    beq scout_complete                                                ; 976f: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 9771: 84 a2       ..             ; Save final buffer offset
    lda econet_control23_or_status2                                   ; 9773: ad a1 fe    ...            ; Read SR2 for next pair
    bne scout_loop_rda                                                ; 9776: d0 de       ..             ; SR2 non-zero -- loop back for more bytes
    jmp nmi_rti                                                       ; 9778: 4c 14 0d    L..            ; SR2 = 0 -- RTI, wait for next NMI

; ***************************************************************************************
; Scout completion handler
; 
; Reached from the scout data loop when SR2 is non-zero (FV detected).
; Disables PSE to allow individual SR2 bit testing:
;   CR1=&00 (clear all enables)
;   CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
; Then checks FV (bit1) and RDA (bit7):
;   - No FV (BEQ) -> error &9741 (not a valid frame end)
;   - FV set, no RDA (BPL) -> error &9741 (missing last byte)
;   - FV set, RDA set -> read last byte, process scout
; After reading the last byte, the complete scout buffer (&0D3D-&0D48)
; contains: src_stn, src_net, ctrl, port [, extra_data...].
; The port byte at &0D40 determines further processing:
;   - Port = 0 -> immediate operation (&9A59)
;   - Port non-zero -> check if it matches an open receive block
; ***************************************************************************************
; &977b referenced 2 times by &9764, &976f
.scout_complete
    lda #0                                                            ; 977b: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 977d: 8d a0 fe    ...            ; Write CR1
    lda #&84                                                          ; 9780: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 9782: 8d a1 fe    ...            ; Write CR2
    lda #2                                                            ; 9785: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9787: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 978a: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 978c: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 978e: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9791: 99 3d 0d    .=.            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 9794: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 9796: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda rx_port                                                       ; 9799: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 979c: d0 06       ..             ; Port non-zero -- look for matching receive block
    jmp immediate_op                                                  ; 979e: 4c 6f 9a    Lo.            ; Port = 0 -- immediate operation handler

; &97a1 referenced 3 times by &97ec, &97f1, &9823
.scout_no_match
    jmp nmi_error_dispatch                                            ; 97a1: 4c 94 98    L..            ; Port = 0 -- immediate operation handler

; &97a4 referenced 1 time by &979c
.scout_match_port
    bit tx_flags                                                      ; 97a4: 2c 4a 0d    ,J.            ; Check if broadcast (bit6 of tx_flags)
    bvc scan_port_list                                                ; 97a7: 50 05       P.             ; Not broadcast -- skip CR2 setup
    lda #7                                                            ; 97a9: a9 07       ..             ; CR2=&07: broadcast prep
    sta econet_control23_or_status2                                   ; 97ab: 8d a1 fe    ...            ; Write CR2: broadcast frame prep
; &97ae referenced 1 time by &97a7
.scan_port_list
    bit rx_flags                                                      ; 97ae: 2c 64 0d    ,d.            ; Check if RX port list active (bit7)
    bpl scout_network_match                                           ; 97b1: 10 3b       .;             ; No active ports -- try NFS workspace
    lda #&c0                                                          ; 97b3: a9 c0       ..             ; Start scanning port list at page &C0
.scan_nfs_port_list
    sta port_ws_offset                                                ; 97b5: 85 a6       ..             ; Store page to workspace pointer low
    lda #0                                                            ; 97b7: a9 00       ..             ; A=0: no NFS workspace offset yet
    sta rx_buf_offset                                                 ; 97b9: 85 a7       ..             ; Clear NFS workspace search flag
; &97bb referenced 1 time by &97e8
.check_port_slot
    ldy #0                                                            ; 97bb: a0 00       ..             ; Y=0: read control byte from start of slot
; &97bd referenced 1 time by &97fb
.scout_ctrl_check
    lda (port_ws_offset),y                                            ; 97bd: b1 a6       ..             ; Read port control byte from slot
    beq scout_station_check                                           ; 97bf: f0 29       .)             ; Zero = end of port list, no match
    cmp #&7f                                                          ; 97c1: c9 7f       ..             ; &7F = any-port wildcard
    bne next_port_slot                                                ; 97c3: d0 1c       ..             ; Not wildcard -- check specific port match
    iny                                                               ; 97c5: c8          .              ; Y=1: advance to port byte in slot
    lda (port_ws_offset),y                                            ; 97c6: b1 a6       ..             ; Read port number from slot (offset 1)
    beq check_station_filter                                          ; 97c8: f0 05       ..             ; Zero port in slot = match any port
    cmp rx_port                                                       ; 97ca: cd 40 0d    .@.            ; Check if port matches this slot
    bne next_port_slot                                                ; 97cd: d0 12       ..             ; Port mismatch -- try next slot
; &97cf referenced 1 time by &97c8
.check_station_filter
    iny                                                               ; 97cf: c8          .              ; Y=2: advance to station byte
    lda (port_ws_offset),y                                            ; 97d0: b1 a6       ..             ; Read station filter from slot (offset 2)
    beq scout_port_match                                              ; 97d2: f0 05       ..             ; Zero station = match any station, accept
    cmp rx_src_stn                                                    ; 97d4: cd 3d 0d    .=.            ; Check if source station matches
    bne next_port_slot                                                ; 97d7: d0 08       ..             ; Station mismatch -- try next slot
; &97d9 referenced 1 time by &97d2
.scout_port_match
    iny                                                               ; 97d9: c8          .              ; Y=3: advance to network byte
    lda (port_ws_offset),y                                            ; 97da: b1 a6       ..             ; Read network filter from slot (offset 3)
    cmp rx_src_net                                                    ; 97dc: cd 3e 0d    .>.            ; Check if source network matches
    beq scout_accept                                                  ; 97df: f0 1c       ..             ; Network matches or zero = accept
; &97e1 referenced 3 times by &97c3, &97cd, &97d7
.next_port_slot
    lda port_ws_offset                                                ; 97e1: a5 a6       ..             ; Check if NFS workspace search pending
    clc                                                               ; 97e3: 18          .              ; CLC for 12-byte slot advance
    adc #&0c                                                          ; 97e4: 69 0c       i.             ; Advance to next 12-byte port slot
    sta port_ws_offset                                                ; 97e6: 85 a6       ..             ; Update workspace pointer to next slot
    bcc check_port_slot                                               ; 97e8: 90 d1       ..             ; Always branches (page &C0 won't overflow)
; &97ea referenced 1 time by &97bf
.scout_station_check
    lda rx_buf_offset                                                 ; 97ea: a5 a7       ..             ; Check if NFS workspace already searched
    bne scout_no_match                                                ; 97ec: d0 b3       ..             ; Already searched: no match found
; &97ee referenced 1 time by &97b1
.scout_network_match
    bit rx_flags                                                      ; 97ee: 2c 64 0d    ,d.            ; Try NFS workspace if paged list exhausted
    bvc scout_no_match                                                ; 97f1: 50 ae       P.             ; No NFS workspace RX (bit6 clear) -- discard
    lda nfs_workspace_hi                                              ; 97f3: a5 9f       ..             ; Get NFS workspace page number
    sta rx_buf_offset                                                 ; 97f5: 85 a7       ..             ; Mark NFS workspace as search target
    ldy #0                                                            ; 97f7: a0 00       ..             ; Y=0: start at offset 0 in workspace
    sty port_ws_offset                                                ; 97f9: 84 a6       ..             ; Reset slot pointer to start
    beq scout_ctrl_check                                              ; 97fb: f0 c0       ..             ; ALWAYS branch

; &97fd referenced 1 time by &97df
.scout_accept
    bit tx_flags                                                      ; 97fd: 2c 4a 0d    ,J.            ; Check broadcast flag (bit 6)
    bvc ack_scout_match                                               ; 9800: 50 03       P.             ; Not broadcast: ACK and set up RX
    jmp copy_scout_fields                                             ; 9802: 4c 60 9a    L`.            ; Broadcast: copy scout fields directly

; &9805 referenced 2 times by &9800, &9adb
.ack_scout_match
    lda #3                                                            ; 9805: a9 03       ..             ; Match found: set scout_status = 3
    sta scout_status                                                  ; 9807: 8d 5c 0d    .\.            ; Record match for completion handler
    lda nmi_tx_block                                                  ; 980a: a5 a0       ..             ; Save current TX block ptr (low)
    pha                                                               ; 980c: 48          H              ; Push TX block low on stack
    lda nmi_tx_block_hi                                               ; 980d: a5 a1       ..             ; Save current TX block ptr (high)
    pha                                                               ; 980f: 48          H              ; Push TX block high on stack
    lda port_ws_offset                                                ; 9810: a5 a6       ..             ; Use port slot as temp RXCB ptr (lo)
    sta nmi_tx_block                                                  ; 9812: 85 a0       ..             ; Set RXCB low for tx_calc_transfer
    lda rx_buf_offset                                                 ; 9814: a5 a7       ..             ; Use workspace page as temp RXCB (hi)
    sta nmi_tx_block_hi                                               ; 9816: 85 a1       ..             ; Set RXCB high for tx_calc_transfer
    jsr tx_calc_transfer                                              ; 9818: 20 6a 9f     j.            ; Calculate transfer parameters
    pla                                                               ; 981b: 68          h              ; Restore original TX block (high)
    sta nmi_tx_block_hi                                               ; 981c: 85 a1       ..             ; Restore TX block ptr (high)
    pla                                                               ; 981e: 68          h              ; Restore original TX block (low)
    sta nmi_tx_block                                                  ; 981f: 85 a0       ..             ; Restore TX block ptr (low)
    bcs send_data_rx_ack                                              ; 9821: b0 03       ..             ; Transfer OK: send data ACK
    jmp scout_no_match                                                ; 9823: 4c a1 97    L..            ; Broadcast: different completion path

; &9826 referenced 2 times by &9821, &9ad0
.send_data_rx_ack
    lda #&44 ; 'D'                                                    ; 9826: a9 44       .D             ; CR1=&44: RX_RESET | TIE
    sta econet_control1_or_status1                                    ; 9828: 8d a0 fe    ...            ; Write CR1: TX mode for ACK
    lda #&a7                                                          ; 982b: a9 a7       ..             ; CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE
    sta econet_control23_or_status2                                   ; 982d: 8d a1 fe    ...            ; Write CR2: enable TX with PSE
    lda #&37 ; '7'                                                    ; 9830: a9 37       .7             ; Install data_rx_setup at &97DC
    ldy #&98                                                          ; 9832: a0 98       ..             ; High byte of data_rx_setup handler
    jmp ack_tx_write_dest                                             ; 9834: 4c 7e 99    L~.            ; Send ACK with data_rx_setup as next NMI

.data_rx_setup
    lda #&82                                                          ; 9837: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 9839: 8d a0 fe    ...            ; Write CR1: switch to RX for data frame
    lda #&43 ; 'C'                                                    ; 983c: a9 43       .C             ; Install nmi_data_rx at &9843
    ldy #&98                                                          ; 983e: a0 98       ..             ; High byte of nmi_data_rx handler
    jmp set_nmi_vector                                                ; 9840: 4c 0e 0d    L..            ; Install nmi_data_rx and return from NMI

; ***************************************************************************************
; Data frame RX handler (four-way handshake)
; 
; Receives the data frame after the scout ACK has been sent.
; First checks AP (Address Present) for the start of the data frame.
; Reads and validates the first two address bytes (dest_stn, dest_net)
; against our station address, then installs continuation handlers
; to read the remaining data payload into the open port buffer.
; 
; Handler chain: &9843 (AP+addr check) -> &9859 (net=0 check) ->
; &986F (skip ctrl+port) -> &98A4 (bulk data read) -> &98D8 (completion)
; ***************************************************************************************
.nmi_data_rx
    lda #1                                                            ; 9843: a9 01       ..             ; A=&01: mask for AP (Address Present)
    bit econet_control23_or_status2                                   ; 9845: 2c a1 fe    ,..            ; BIT SR2: test AP bit
    beq nmi_error_dispatch                                            ; 9848: f0 4a       .J             ; No AP: wrong frame or error
    lda econet_data_continue_frame                                    ; 984a: ad a2 fe    ...            ; Read first byte (dest station)
    cmp station_id_disable_net_nmis                                   ; 984d: cd 18 fe    ...            ; Compare to our station ID (INTOFF)
    bne nmi_error_dispatch                                            ; 9850: d0 42       .B             ; Not for us: error path
    lda #&59 ; 'Y'                                                    ; 9852: a9 59       .Y             ; Install net check handler at &9859
    ldy #&98                                                          ; 9854: a0 98       ..             ; High byte of nmi_data_rx handler
    jmp set_nmi_vector                                                ; 9856: 4c 0e 0d    L..            ; Set NMI vector via RAM shim

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 9859: 2c a1 fe    ,..            ; Validate source network = 0
    bpl nmi_error_dispatch                                            ; 985c: 10 36       .6             ; SR2 bit7 clear: no data ready -- error
    lda econet_data_continue_frame                                    ; 985e: ad a2 fe    ...            ; Read dest network byte
    bne nmi_error_dispatch                                            ; 9861: d0 31       .1             ; Network != 0: wrong network -- error
    lda #&6f ; 'o'                                                    ; 9863: a9 6f       .o             ; Install skip handler at &986F
    ldy #&98                                                          ; 9865: a0 98       ..             ; High byte of &986F handler
    bit econet_control1_or_status1                                    ; 9867: 2c a0 fe    ,..            ; SR1 bit7: IRQ, data already waiting
    bmi nmi_data_rx_skip                                              ; 986a: 30 03       0.             ; Data ready: skip directly, no RTI
    jmp set_nmi_vector                                                ; 986c: 4c 0e 0d    L..            ; Install handler and return via RTI

; &986f referenced 1 time by &986a
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 986f: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl nmi_error_dispatch                                            ; 9872: 10 20       .              ; SR2 bit7 clear: error
    lda econet_data_continue_frame                                    ; 9874: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 9877: ad a2 fe    ...            ; Discard port byte
; ***************************************************************************************
; Install data RX bulk or Tube handler
; 
; Selects either the normal bulk RX handler (&98A4) or the Tube
; RX handler (&9901) based on the Tube transfer flag in tx_flags,
; and installs the appropriate NMI handler.
; ***************************************************************************************
; &987a referenced 1 time by &9f3e
.install_data_rx_handler
    lda #2                                                            ; 987a: a9 02       ..             ; A=2: Tube transfer flag mask
    bit tx_flags                                                      ; 987c: 2c 4a 0d    ,J.            ; Check if Tube transfer active
    bne install_tube_rx                                               ; 987f: d0 0c       ..             ; Tube active: use Tube RX path
    lda #&a4                                                          ; 9881: a9 a4       ..             ; Install bulk read at &9843
    ldy #&98                                                          ; 9883: a0 98       ..             ; High byte of &9843 handler
    bit econet_control1_or_status1                                    ; 9885: 2c a0 fe    ,..            ; SR1 bit7: more data already waiting?
    bmi nmi_data_rx_bulk                                              ; 9888: 30 1a       0.             ; Yes: enter bulk read directly
    jmp set_nmi_vector                                                ; 988a: 4c 0e 0d    L..            ; No: install handler and RTI

; &988d referenced 1 time by &987f
.install_tube_rx
    lda #1                                                            ; 988d: a9 01       ..             ; Tube: install Tube RX at &9901
    ldy #&99                                                          ; 988f: a0 99       ..             ; High byte of &9901 handler
    jmp set_nmi_vector                                                ; 9891: 4c 0e 0d    L..            ; Install Tube handler and RTI

; ***************************************************************************************
; NMI error handler dispatch
; 
; Common error/abort entry used by 12 call sites. Checks
; tx_flags bit 7: if clear, does a full ADLC reset and returns
; to idle listen (RX error path); if set, jumps to tx_result_fail
; (TX not-listening path).
; ***************************************************************************************
; &9894 referenced 12 times by &97a1, &9848, &9850, &985c, &9861, &9872, &98b7, &98e9, &98ef, &993a, &99c2, &9aa2
.nmi_error_dispatch
    lda tx_flags                                                      ; 9894: ad 4a 0d    .J.            ; Check tx_flags for error path
    bpl rx_error                                                      ; 9897: 10 05       ..             ; Bit7 clear: RX error path
    lda #&41 ; 'A'                                                    ; 9899: a9 41       .A             ; A=&41: 'not listening' error
    jmp tx_store_result                                               ; 989b: 4c 4e 9f    LN.            ; Bit7 set: TX result = not listening

; &989e referenced 1 time by &9897
.rx_error
.rx_error_reset
    jsr adlc_full_reset                                               ; 989e: 20 e6 96     ..            ; Full ADLC reset on RX error
    jmp discard_reset_listen                                          ; 98a1: 4c 4a 9a    LJ.            ; Discard and return to idle listen

; ***************************************************************************************
; Data frame bulk read loop
; 
; Reads data payload bytes from the RX FIFO and stores them into
; the open port buffer at (open_port_buf),Y. Reads bytes in pairs
; (like the scout data loop), checking SR2 between each pair.
; SR2 non-zero (FV or other) -> frame completion at &98D8.
; SR2 = 0 -> RTI, wait for next NMI to continue.
; ***************************************************************************************
; &98a4 referenced 1 time by &9888
.nmi_data_rx_bulk
    ldy port_buf_len                                                  ; 98a4: a4 a2       ..             ; Y = buffer offset, resume from last position
    lda econet_control23_or_status2                                   ; 98a6: ad a1 fe    ...            ; Read SR2 for next pair
; &98a9 referenced 1 time by &98d3
.data_rx_loop
    bpl data_rx_complete                                              ; 98a9: 10 2d       .-             ; SR2 bit7 clear: frame complete (FV)
    lda econet_data_continue_frame                                    ; 98ab: ad a2 fe    ...            ; Read first byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 98ae: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 98b0: c8          .              ; Advance buffer offset
    bne read_sr2_between_pairs                                        ; 98b1: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 98b3: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 98b5: c6 a3       ..             ; Decrement remaining page count
    beq nmi_error_dispatch                                            ; 98b7: f0 db       ..             ; No pages left: handle as complete
; &98b9 referenced 1 time by &98b1
.read_sr2_between_pairs
    lda econet_control23_or_status2                                   ; 98b9: ad a1 fe    ...            ; Read SR2 between byte pairs
    bmi read_second_rx_byte                                           ; 98bc: 30 02       0.             ; SR2 bit7 set: more data available
    bne data_rx_complete                                              ; 98be: d0 18       ..             ; SR2 non-zero, bit7 clear: frame done
; &98c0 referenced 1 time by &98bc
.read_second_rx_byte
    lda econet_data_continue_frame                                    ; 98c0: ad a2 fe    ...            ; Read second byte of pair from RX FIFO
    sta (open_port_buf),y                                             ; 98c3: 91 a4       ..             ; Store byte to buffer
    iny                                                               ; 98c5: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 98c6: 84 a2       ..             ; Save updated buffer position
    bne check_sr2_loop_again                                          ; 98c8: d0 06       ..             ; Y != 0: no page boundary crossing
    inc open_port_buf_hi                                              ; 98ca: e6 a5       ..             ; Crossed page: increment buffer high byte
    dec port_buf_len_hi                                               ; 98cc: c6 a3       ..             ; Decrement remaining page count
    beq data_rx_complete                                              ; 98ce: f0 08       ..             ; No pages left: frame complete
; &98d0 referenced 1 time by &98c8
.check_sr2_loop_again
    lda econet_control23_or_status2                                   ; 98d0: ad a1 fe    ...            ; Read SR2 for next iteration
    bne data_rx_loop                                                  ; 98d3: d0 d4       ..             ; SR2 non-zero: more data, loop back
    jmp nmi_rti                                                       ; 98d5: 4c 14 0d    L..            ; SR2=0: no more data yet, wait for NMI

; ***************************************************************************************
; Data frame completion
; 
; Reached when SR2 non-zero during data RX (FV detected).
; Same pattern as scout completion (&977B): disables PSE (CR1=&00,
; CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
; If extra data available and buffer space remains, stores it.
; Proceeds to send the final ACK via &9968.
; ***************************************************************************************
; &98d8 referenced 3 times by &98a9, &98be, &98ce
.data_rx_complete
    lda #0                                                            ; 98d8: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 98da: 8d a0 fe    ...            ; Write CR1
    lda #&84                                                          ; 98dd: a9 84       ..             ; CR2=&84: disable PSE for individual bit testing
    sta econet_control23_or_status2                                   ; 98df: 8d a1 fe    ...            ; Write CR2
    sty port_buf_len                                                  ; 98e2: 84 a2       ..             ; Save Y (byte count from data RX loop)
    lda #2                                                            ; 98e4: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 98e6: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq nmi_error_dispatch                                            ; 98e9: f0 a9       ..             ; No FV -- error
    bpl send_ack                                                      ; 98eb: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 98ed: a5 a3       ..             ; Check if buffer space remains
.read_last_rx_byte
    beq nmi_error_dispatch                                            ; 98ef: f0 a3       ..             ; No buffer space: error/discard frame
    lda econet_data_continue_frame                                    ; 98f1: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 98f4: a4 a2       ..             ; Y = current buffer write offset
    sta (open_port_buf),y                                             ; 98f6: 91 a4       ..             ; Store last byte in port receive buffer
    inc port_buf_len                                                  ; 98f8: e6 a2       ..             ; Advance buffer write offset
    bne send_ack                                                      ; 98fa: d0 02       ..             ; No page wrap: proceed to send ACK
    inc open_port_buf_hi                                              ; 98fc: e6 a5       ..             ; Page boundary: advance buffer page
; &98fe referenced 2 times by &98eb, &98fa
.send_ack
    jmp ack_tx                                                        ; 98fe: 4c 68 99    Lh.            ; Send ACK frame to complete handshake

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 9901: ad a1 fe    ...            ; Read SR2 for Tube data receive path
; &9904 referenced 1 time by &9935
.rx_tube_data
    bpl data_rx_tube_complete                                         ; 9904: 10 37       .7             ; RDA clear: no more data, frame complete
    lda econet_data_continue_frame                                    ; 9906: ad a2 fe    ...            ; Read data byte from ADLC RX FIFO
    inc port_buf_len                                                  ; 9909: e6 a2       ..             ; Advance Tube transfer byte count
    sta tube_data_register_3                                          ; 990b: 8d e5 fe    ...            ; Send byte to Tube data register 3
    bne rx_update_buf                                                 ; 990e: d0 0c       ..             ; No overflow: read second byte
    inc port_buf_len_hi                                               ; 9910: e6 a3       ..             ; Carry to transfer count byte 2
    bne rx_update_buf                                                 ; 9912: d0 08       ..             ; No overflow: read second byte
    inc open_port_buf                                                 ; 9914: e6 a4       ..             ; Carry to transfer count byte 3
    bne rx_update_buf                                                 ; 9916: d0 04       ..             ; No overflow: read second byte
    inc open_port_buf_hi                                              ; 9918: e6 a5       ..             ; Carry to transfer count byte 4
    beq data_rx_tube_error                                            ; 991a: f0 1e       ..             ; All bytes zero: overflow error
; &991c referenced 3 times by &990e, &9912, &9916
.rx_update_buf
    lda econet_data_continue_frame                                    ; 991c: ad a2 fe    ...            ; Read second data byte (paired transfer)
    sta tube_data_register_3                                          ; 991f: 8d e5 fe    ...            ; Send second byte to Tube
    inc port_buf_len                                                  ; 9922: e6 a2       ..             ; Advance count after second byte
    bne rx_check_error                                                ; 9924: d0 0c       ..             ; No overflow: check for more data
    inc port_buf_len_hi                                               ; 9926: e6 a3       ..             ; Carry to count byte 2
    bne rx_check_error                                                ; 9928: d0 08       ..             ; No overflow: check for more data
    inc open_port_buf                                                 ; 992a: e6 a4       ..             ; Carry to count byte 3
    bne rx_check_error                                                ; 992c: d0 04       ..             ; No overflow: check for more data
    inc open_port_buf_hi                                              ; 992e: e6 a5       ..             ; Carry to count byte 4
    beq data_rx_tube_complete                                         ; 9930: f0 0b       ..             ; Zero: Tube transfer complete
; &9932 referenced 3 times by &9924, &9928, &992c
.rx_check_error
    lda econet_control23_or_status2                                   ; 9932: ad a1 fe    ...            ; Re-read SR2 for next byte pair
    bne rx_tube_data                                                  ; 9935: d0 cd       ..             ; More data available: continue loop
    jmp nmi_rti                                                       ; 9937: 4c 14 0d    L..            ; Return from NMI, wait for data

; &993a referenced 3 times by &991a, &994c, &9958
.data_rx_tube_error
    jmp nmi_error_dispatch                                            ; 993a: 4c 94 98    L..            ; Unexpected end: return from NMI

; &993d referenced 2 times by &9904, &9930
.data_rx_tube_complete
    lda #0                                                            ; 993d: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 993f: 8d a0 fe    ...            ; Write CR1 for individual bit testing
    lda #&84                                                          ; 9942: a9 84       ..             ; CR2=&84: disable PSE
    sta econet_control23_or_status2                                   ; 9944: 8d a1 fe    ...            ; Write CR2: same pattern as main path
    lda #2                                                            ; 9947: a9 02       ..             ; A=&02: FV mask for Tube completion
    bit econet_control23_or_status2                                   ; 9949: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq data_rx_tube_error                                            ; 994c: f0 ec       ..             ; No FV: incomplete frame, error
    bpl ack_tx                                                        ; 994e: 10 18       ..             ; FV set, no RDA: proceed to ACK
    lda port_buf_len                                                  ; 9950: a5 a2       ..             ; Check if any buffer was allocated
    ora port_buf_len_hi                                               ; 9952: 05 a3       ..             ; OR all 4 buffer pointer bytes together
    ora open_port_buf                                                 ; 9954: 05 a4       ..             ; Check buffer low byte
    ora open_port_buf_hi                                              ; 9956: 05 a5       ..             ; Check buffer high byte
    beq data_rx_tube_error                                            ; 9958: f0 e0       ..             ; All zero (null buffer): error
    lda econet_data_continue_frame                                    ; 995a: ad a2 fe    ...            ; Read extra trailing byte from FIFO
    sta rx_extra_byte                                                 ; 995d: 8d 5d 0d    .].            ; Save extra byte at &0D5D for later use
    lda #&20 ; ' '                                                    ; 9960: a9 20       .              ; Bit5 = extra data byte available flag
    ora tx_flags                                                      ; 9962: 0d 4a 0d    .J.            ; Set extra byte flag in tx_flags
    sta tx_flags                                                      ; 9965: 8d 4a 0d    .J.            ; Store updated flags
; ***************************************************************************************
; ACK transmission
; 
; Sends a scout ACK or final ACK frame as part of the four-way handshake.
; If bit7 of &0D4A is set, this is a final ACK -> completion (&9F48).
; Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
; frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
; The ACK frame has no data payload -- just address bytes.
; 
; After writing the address bytes to the TX FIFO, installs the next
; NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
; and sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
; &9968 referenced 2 times by &98fe, &994e
.ack_tx
    lda tx_flags                                                      ; 9968: ad 4a 0d    .J.            ; Load TX flags to check ACK type
    bpl ack_tx_configure                                              ; 996b: 10 03       ..             ; Bit7 clear: normal scout ACK
    jmp tx_result_ok                                                  ; 996d: 4c 48 9f    LH.            ; Jump to TX success result

; &9970 referenced 1 time by &996b
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 9970: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 9972: 8d a0 fe    ...            ; Write CR1: switch to TX mode
    lda #&a7                                                          ; 9975: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9977: 8d a1 fe    ...            ; Write CR2: enable TX with status clear
    lda #&c5                                                          ; 997a: a9 c5       ..             ; Install saved next handler (&99C5 for scout ACK)
    ldy #&99                                                          ; 997c: a0 99       ..             ; High byte of post-ACK handler
; &997e referenced 2 times by &9834, &9b25
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 997e: 8d 4b 0d    .K.            ; Store next handler low byte
    sty nmi_next_hi                                                   ; 9981: 8c 4c 0d    .L.            ; Store next handler high byte
    lda rx_src_stn                                                    ; 9984: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 9987: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc tdra_error                                                    ; 998a: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 998c: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 998f: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9992: 8d a2 fe    ...            ; Write dest net byte to FIFO
    lda #&9c                                                          ; 9995: a9 9c       ..             ; Install nmi_ack_tx_src at &999C
    ldy #&99                                                          ; 9997: a0 99       ..             ; High byte of nmi_ack_tx_src
    jmp set_nmi_vector                                                ; 9999: 4c 0e 0d    L..            ; Set NMI vector to ack_tx_src handler

; ***************************************************************************************
; ACK TX continuation
; 
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 999c: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 999f: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc tdra_error                                                    ; 99a2: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 99a4: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 99a7: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 99a9: 8d a2 fe    ...            ; Write network=0 (local) to TX FIFO
    lda tx_flags                                                      ; 99ac: ad 4a 0d    .J.            ; Check tx_flags for data phase
    bmi start_data_tx                                                 ; 99af: 30 0e       0.             ; bit7 set: start data TX phase
    lda #&3f ; '?'                                                    ; 99b1: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 99b3: 8d a1 fe    ...            ; Write CR2 to clear status after ACK TX
    lda nmi_next_lo                                                   ; 99b6: ad 4b 0d    .K.            ; Install saved handler from &0D4B/&0D4C
    ldy nmi_next_hi                                                   ; 99b9: ac 4c 0d    .L.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 99bc: 4c 0e 0d    L..            ; Install next NMI handler

; &99bf referenced 1 time by &99af
.start_data_tx
    jmp data_tx_begin                                                 ; 99bf: 4c 4a 9e    LJ.            ; Jump to start data TX phase

; &99c2 referenced 2 times by &998a, &99a2
.tdra_error
    jmp nmi_error_dispatch                                            ; 99c2: 4c 94 98    L..            ; TDRA error: jump to error handler

; ***************************************************************************************
; Post-ACK scout processing
; 
; Called after the scout ACK has been transmitted. Processes the
; received scout data stored in the buffer at &0D3D-&0D48.
; Checks the port byte (&0D40) against open receive blocks to
; find a matching listener. If a match is found, sets up the
; data RX handler chain for the four-way handshake data phase.
; If no match, discards the frame.
; ***************************************************************************************
.post_ack_scout
    lda rx_port                                                       ; 99c5: ad 40 0d    .@.            ; Check port byte from scout
    bne advance_rx_buffer_ptr                                         ; 99c8: d0 0a       ..             ; Non-zero port: advance RX buffer
    ldy rx_ctrl                                                       ; 99ca: ac 3f 0d    .?.            ; Load control byte from scout
    cpy #&82                                                          ; 99cd: c0 82       ..             ; Is ctrl &82 (immediate peek)?
    beq advance_rx_buffer_ptr                                         ; 99cf: f0 03       ..             ; Yes: advance RX buffer for peek
.dispatch_nmi_error
    jmp imm_op_build_reply                                            ; 99d1: 4c 28 9b    L(.            ; Jump to error handler

; ***************************************************************************************
; Advance RX buffer pointer after transfer
; 
; Adds the transfer count to the RXCB buffer pointer (4-byte
; addition). If a Tube transfer is active, re-claims the Tube
; address and sends the extra RX byte via R3, incrementing the
; Tube pointer by 1.
; ***************************************************************************************
; &99d4 referenced 2 times by &99c8, &99cf
.advance_rx_buffer_ptr
    lda #2                                                            ; 99d4: a9 02       ..             ; A=2: test bit1 of tx_flags
    bit tx_flags                                                      ; 99d6: 2c 4a 0d    ,J.            ; BIT tx_flags: check data transfer bit
    beq add_buf_to_base                                               ; 99d9: f0 3d       .=             ; Bit1 clear: no transfer -- return
    clc                                                               ; 99db: 18          .              ; CLC: init carry for 4-byte add
    php                                                               ; 99dc: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 99dd: a0 08       ..             ; Y=8: RXCB high pointer offset
; &99df referenced 1 time by &99eb
.add_rxcb_ptr
    lda (port_ws_offset),y                                            ; 99df: b1 a6       ..             ; Load RXCB[Y] (buffer pointer byte)
    plp                                                               ; 99e1: 28          (              ; Restore carry from stack
    adc net_tx_ptr,y                                                  ; 99e2: 79 9a 00    y..            ; Add transfer count byte
    sta (port_ws_offset),y                                            ; 99e5: 91 a6       ..             ; Store updated pointer back to RXCB
    iny                                                               ; 99e7: c8          .              ; Next byte
    php                                                               ; 99e8: 08          .              ; Save carry for next iteration
    cpy #&0c                                                          ; 99e9: c0 0c       ..             ; Done 4 bytes? (Y reaches &0C)
    bcc add_rxcb_ptr                                                  ; 99eb: 90 f2       ..             ; No: continue adding
    plp                                                               ; 99ed: 28          (              ; Discard final carry
    lda #&20 ; ' '                                                    ; 99ee: a9 20       .              ; A=&20: test bit5 of tx_flags
    bit tx_flags                                                      ; 99f0: 2c 4a 0d    ,J.            ; BIT tx_flags: check Tube bit
    beq skip_buf_ptr_update                                           ; 99f3: f0 35       .5             ; No Tube: skip Tube update
    txa                                                               ; 99f5: 8a          .              ; Save X on stack
    pha                                                               ; 99f6: 48          H              ; Push X
    lda #8                                                            ; 99f7: a9 08       ..             ; A=8: offset for Tube address
    clc                                                               ; 99f9: 18          .              ; CLC for address calculation
    adc port_ws_offset                                                ; 99fa: 65 a6       e.             ; Add workspace base offset
    tax                                                               ; 99fc: aa          .              ; X = address low for Tube claim
    ldy rx_buf_offset                                                 ; 99fd: a4 a7       ..             ; Y = address high for Tube claim
    lda #1                                                            ; 99ff: a9 01       ..             ; A=1: Tube claim type (read)
    jsr tube_addr_claim                                               ; 9a01: 20 06 04     ..            ; Claim Tube address for transfer
    lda rx_extra_byte                                                 ; 9a04: ad 5d 0d    .].            ; Load extra RX data byte
    sta tube_data_register_3                                          ; 9a07: 8d e5 fe    ...            ; Send to Tube via R3
    pla                                                               ; 9a0a: 68          h              ; Restore X from stack
    tax                                                               ; 9a0b: aa          .              ; Transfer to X register
    ldy #8                                                            ; 9a0c: a0 08       ..             ; Y=8: RXCB buffer ptr offset
    lda (port_ws_offset),y                                            ; 9a0e: b1 a6       ..             ; Load current RXCB buffer ptr lo
    sec                                                               ; 9a10: 38          8              ; SEC for ADC #0 = add carry
    adc #0                                                            ; 9a11: 69 00       i.             ; Increment by 1 (Tube extra byte)
    sta (port_ws_offset),y                                            ; 9a13: 91 a6       ..             ; Store updated ptr back to RXCB
.jmp_store_rxcb
    jmp skip_buf_ptr_update                                           ; 9a15: 4c 2a 9a    L*.            ; Other port-0 ops: immediate dispatch

; &9a18 referenced 1 time by &99d9
.add_buf_to_base
    lda port_buf_len                                                  ; 9a18: a5 a2       ..             ; Load buffer bytes remaining
    clc                                                               ; 9a1a: 18          .              ; CLC for address add
    adc open_port_buf                                                 ; 9a1b: 65 a4       e.             ; Add to buffer base address
    bcc store_buf_ptr_lo                                              ; 9a1d: 90 02       ..             ; No carry: skip high byte increment
.inc_rxcb_buf_hi
    inc open_port_buf_hi                                              ; 9a1f: e6 a5       ..             ; Carry: increment buffer high byte
; &9a21 referenced 1 time by &9a1d
.store_buf_ptr_lo
    ldy #8                                                            ; 9a21: a0 08       ..             ; Y=8: store updated buffer position
.store_rxcb_buf_ptr
store_rxcb_byte = store_rxcb_buf_ptr+1
    sta (port_ws_offset),y                                            ; 9a23: 91 a6       ..             ; Store updated low byte to RXCB
; &9a24 referenced 1 time by &9a9d
    iny                                                               ; 9a25: c8          .              ; Y=9: buffer high byte offset
.load_rxcb_buf_hi
    lda open_port_buf_hi                                              ; 9a26: a5 a5       ..             ; Load updated buffer high byte
.store_rxcb_buf_hi
    sta (port_ws_offset),y                                            ; 9a28: 91 a6       ..             ; Store high byte to RXCB
; &9a2a referenced 3 times by &99f3, &9a15, &9a6c
.skip_buf_ptr_update
rx_port_operand = skip_buf_ptr_update+2
    lda rx_port                                                       ; 9a2a: ad 40 0d    .@.            ; Check port byte again
; &9a2c referenced 1 time by &9a99
    beq discard_reset_listen                                          ; 9a2d: f0 1b       ..             ; Port=0: immediate op, discard+listen
; ***************************************************************************************
; Store RXCB completion fields from scout buffer
; 
; Writes source network, source station, port, and control
; byte from the scout buffer into the active RXCB. Sets
; bit 7 of the control byte to mark reception complete.
; ***************************************************************************************
.store_rxcb_completion
    lda rx_src_net                                                    ; 9a2f: ad 3e 0d    .>.            ; Load source network from scout buffer
    ldy #3                                                            ; 9a32: a0 03       ..             ; Y=3: RXCB source network offset
    sta (port_ws_offset),y                                            ; 9a34: 91 a6       ..             ; Store source network to RXCB
    dey                                                               ; 9a36: 88          .              ; Y=2: source station offset; Y=&02
    lda rx_src_stn                                                    ; 9a37: ad 3d 0d    .=.            ; Load source station from scout buffer
    sta (port_ws_offset),y                                            ; 9a3a: 91 a6       ..             ; Store source station to RXCB
    dey                                                               ; 9a3c: 88          .              ; Y=1: port byte offset; Y=&01
    lda rx_port                                                       ; 9a3d: ad 40 0d    .@.            ; Load port byte
    sta (port_ws_offset),y                                            ; 9a40: 91 a6       ..             ; Store port to RXCB
    dey                                                               ; 9a42: 88          .              ; Y=0: control/flag byte offset; Y=&00
    lda rx_ctrl                                                       ; 9a43: ad 3f 0d    .?.            ; Load control byte from scout
    ora #&80                                                          ; 9a46: 09 80       ..             ; Set bit7 = reception complete flag
    sta (port_ws_offset),y                                            ; 9a48: 91 a6       ..             ; Store to RXCB (marks CB as complete)
; ***************************************************************************************
; Discard with full ADLC reset
; 
; Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
; then falls through to install_rx_scout_handler. Used when the ADLC is
; in an unexpected state and needs a hard reset before returning
; to idle listen mode. 5 references — the main error recovery path.
; ***************************************************************************************
; &9a4a referenced 4 times by &98a1, &9a2d, &9ea2, &9f57
.discard_reset_listen
    lda #2                                                            ; 9a4a: a9 02       ..             ; Tube flag bit 1 AND tx_flags bit 1
    bit tx_flags                                                      ; 9a4c: 2c 4a 0d    ,J.            ; Test tx_flags for Tube transfer
    beq discard_listen                                                ; 9a4f: f0 05       ..             ; No Tube transfer active -- skip release
    lda #&82                                                          ; 9a51: a9 82       ..             ; A=&82: Tube release claim type
    jsr tube_addr_claim                                               ; 9a53: 20 06 04     ..            ; Release Tube claim before discarding
; ***************************************************************************************
; Discard frame (gentle)
; 
; Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
; current frame reception without a full reset, then falls through
; to install_rx_scout_handler. Used for clean rejection of frames
; that are correctly formatted but not for us (wrong station/network).
; ***************************************************************************************
; &9a56 referenced 3 times by &974e, &9a4f, &9b5e
.discard_listen
    jsr adlc_rx_listen                                                ; 9a56: 20 f5 96     ..            ; Re-enter idle RX listen mode
; ***************************************************************************************
; Install RX scout NMI handler
; 
; Installs nmi_rx_scout (&9700) as the NMI handler via
; set_nmi_vector, without first calling adlc_rx_listen.
; Used when the ADLC is already in the correct RX mode.
; ***************************************************************************************
; &9a59 referenced 2 times by &9732, &974b
.install_rx_scout_handler
    lda #0                                                            ; 9a59: a9 00       ..             ; Install nmi_rx_scout (&9700) as NMI handler
    ldy #&97                                                          ; 9a5b: a0 97       ..             ; High byte of nmi_rx_scout
    jmp set_nmi_vector                                                ; 9a5d: 4c 0e 0d    L..            ; Set NMI vector and return

; &9a60 referenced 1 time by &9802
.copy_scout_fields
    ldy #4                                                            ; 9a60: a0 04       ..             ; Y=4: start at RX CB offset 4
; &9a62 referenced 1 time by &9a6a
.copy_scout_loop
    lda rx_src_stn,y                                                  ; 9a62: b9 3d 0d    .=.            ; Load scout field (stn/net/ctrl/port)
    sta (port_ws_offset),y                                            ; 9a65: 91 a6       ..             ; Store to port workspace buffer
    iny                                                               ; 9a67: c8          .              ; Advance buffer pointer
    cpy #&0c                                                          ; 9a68: c0 0c       ..             ; All 8 fields copied?
    bne copy_scout_loop                                               ; 9a6a: d0 f6       ..             ; No: continue copy loop
    jmp skip_buf_ptr_update                                           ; 9a6c: 4c 2a 9a    L*.            ; Jump to completion handler

; ***************************************************************************************
; Immediate operation handler (port = 0)
; 
; Handles immediate (non-data-transfer) operations received via
; scout frames with port byte = 0. The control byte (&0D3F)
; determines the operation type:
;   &81 = PEEK (read memory)
;   &82 = POKE (write memory)
;   &83 = JSR (remote procedure call)
;   &84 = user procedure
;   &85 = OS procedure
;   &86 = HALT
;   &87 = CONTINUE
; The protection mask (LSTAT at &D63) controls which operations
; are permitted — each bit enables or disables an operation type.
; If the operation is not permitted by the mask, it is silently
; ignored. LSTAT can be read/set via OSWORD &12 sub-functions 4/5.
; ***************************************************************************************
; &9a6f referenced 1 time by &979e
.immediate_op
    ldy rx_ctrl                                                       ; 9a6f: ac 3f 0d    .?.            ; Control byte &81-&88 range check
    cpy #&81                                                          ; 9a72: c0 81       ..             ; Below &81: not an immediate op
    bcc imm_op_out_of_range                                           ; 9a74: 90 2c       .,             ; Out of range low: jump to discard
    cpy #&89                                                          ; 9a76: c0 89       ..             ; Above &88: not an immediate op
    bcs imm_op_out_of_range                                           ; 9a78: b0 28       .(             ; Out of range high: jump to discard
    cpy #&87                                                          ; 9a7a: c0 87       ..             ; HALT(&87)/CONTINUE(&88) skip protection
    bcs imm_op_dispatch                                               ; 9a7c: b0 18       ..             ; Ctrl >= &87: dispatch without mask check
    lda rx_src_stn                                                    ; 9a7e: ad 3d 0d    .=.            ; Load source station number
    cmp #&f0                                                          ; 9a81: c9 f0       ..             ; Station >= &F0? (privileged)
    bcs imm_op_dispatch                                               ; 9a83: b0 11       ..             ; Privileged: skip protection check
    tya                                                               ; 9a85: 98          .              ; Convert ctrl byte to 0-based index for mask
    sec                                                               ; 9a86: 38          8              ; SEC for subtract
    sbc #&81                                                          ; 9a87: e9 81       ..             ; A = ctrl - &81 (0-based operation index)
    tay                                                               ; 9a89: a8          .              ; Y = index for mask rotation count
    lda prot_status                                                   ; 9a8a: ad 63 0d    .c.            ; Load protection mask from LSTAT
; &9a8d referenced 1 time by &9a8f
.rotate_prot_mask
    ror a                                                             ; 9a8d: 6a          j              ; Rotate mask right by control byte index
    dey                                                               ; 9a8e: 88          .              ; Decrement rotation counter
    bpl rotate_prot_mask                                              ; 9a8f: 10 fc       ..             ; Loop until bit aligned
    bcc imm_op_dispatch                                               ; 9a91: 90 03       ..             ; Carry clear: operation permitted
    jmp imm_op_discard                                                ; 9a93: 4c 5e 9b    L^.            ; Operation blocked by LSTAT mask

; &9a96 referenced 3 times by &9a7c, &9a83, &9a91
.imm_op_dispatch
    ldy rx_ctrl                                                       ; 9a96: ac 3f 0d    .?.            ; Reload ctrl byte for dispatch table
    lda rx_port_operand,y                                             ; 9a99: b9 2c 9a    .,.            ; Look up handler address high byte
    pha                                                               ; 9a9c: 48          H              ; Push handler address high
    lda store_rxcb_byte,y                                             ; 9a9d: b9 24 9a    .$.            ; Load handler low byte from jump table
    pha                                                               ; 9aa0: 48          H              ; Push handler address low
    rts                                                               ; 9aa1: 60          `              ; RTS dispatches to handler

; &9aa2 referenced 2 times by &9a74, &9a78
.imm_op_out_of_range
    jmp nmi_error_dispatch                                            ; 9aa2: 4c 94 98    L..            ; Jump to discard handler

    equb <(rx_imm_peek-1)                                             ; 9aa5: f0          .
    equb <(rx_imm_poke-1)                                             ; 9aa6: d2          .
    equb <(rx_imm_exec-1)                                             ; 9aa7: b4          .
    equb <(rx_imm_exec-1)                                             ; 9aa8: b4          .
    equb <(rx_imm_exec-1)                                             ; 9aa9: b4          .
    equb <(rx_imm_halt_cont-1)                                        ; 9aaa: 16          .
    equb <(rx_imm_halt_cont-1)                                        ; 9aab: 16          .
    equb <(rx_imm_machine_type-1)                                     ; 9aac: dd          .
    equb >(rx_imm_peek-1)                                             ; 9aad: 9a          .
    equb >(rx_imm_poke-1)                                             ; 9aae: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9aaf: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9ab0: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9ab1: 9a          .
    equb >(rx_imm_halt_cont-1)                                        ; 9ab2: 9b          .
    equb >(rx_imm_halt_cont-1)                                        ; 9ab3: 9b          .
    equb >(rx_imm_machine_type-1)                                     ; 9ab4: 9a          .

; ***************************************************************************************
; RX immediate: JSR/UserProc/OSProc setup
; 
; Sets up the port buffer to receive remote procedure data.
; Copies the 4-byte remote address from rx_remote_addr into
; the execution address workspace at &0D58, then jumps to
; the common receive path at c9826. Used for operation types
; &83 (JSR), &84 (UserProc), and &85 (OSProc).
; ***************************************************************************************
.rx_imm_exec
    lda #0                                                            ; 9ab5: a9 00       ..             ; Buffer start lo = &00
    sta open_port_buf                                                 ; 9ab7: 85 a4       ..             ; Set port buffer lo
    lda #&82                                                          ; 9ab9: a9 82       ..             ; Buffer length lo = &82
    sta port_buf_len                                                  ; 9abb: 85 a2       ..             ; Set buffer length lo
    lda #1                                                            ; 9abd: a9 01       ..             ; Buffer length hi = 1
    sta port_buf_len_hi                                               ; 9abf: 85 a3       ..             ; Set buffer length hi
    lda net_rx_ptr_hi                                                 ; 9ac1: a5 9d       ..             ; Load RX page hi for buffer
    sta open_port_buf_hi                                              ; 9ac3: 85 a5       ..             ; Set port buffer hi
    ldy #3                                                            ; 9ac5: a0 03       ..             ; Y=3: copy 4 bytes (3 down to 0)
; &9ac7 referenced 1 time by &9ace
.copy_addr_loop
    lda rx_remote_addr,y                                              ; 9ac7: b9 41 0d    .A.            ; Load remote address byte
    sta l0d58,y                                                       ; 9aca: 99 58 0d    .X.            ; Store to exec address workspace
    dey                                                               ; 9acd: 88          .              ; Next byte (descending)
    bpl copy_addr_loop                                                ; 9ace: 10 f7       ..             ; Loop until all 4 bytes copied
    jmp send_data_rx_ack                                              ; 9ad0: 4c 26 98    L&.            ; Enter common data-receive path

; ***************************************************************************************
; RX immediate: POKE setup
; 
; Sets up workspace offsets for receiving POKE data.
; port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
; the common data-receive path at c9805.
; ***************************************************************************************
.rx_imm_poke
    lda #&3d ; '='                                                    ; 9ad3: a9 3d       .=             ; Port workspace offset = &3D
    sta port_ws_offset                                                ; 9ad5: 85 a6       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 9ad7: a9 0d       ..             ; RX buffer page = &0D
    sta rx_buf_offset                                                 ; 9ad9: 85 a7       ..             ; Store workspace offset hi
    jmp ack_scout_match                                               ; 9adb: 4c 05 98    L..            ; Enter POKE data-receive path

; ***************************************************************************************
; RX immediate: machine type query
; 
; Sets up a buffer at &7F21 (length #&01FC) for the machine
; type query response, then jumps to the query handler at
; c9b0f. Returns system identification data to the remote
; station.
; ***************************************************************************************
.rx_imm_machine_type
    lda #1                                                            ; 9ade: a9 01       ..             ; Buffer length hi = 1
    sta port_buf_len_hi                                               ; 9ae0: 85 a3       ..             ; Set buffer length hi
    lda #&fc                                                          ; 9ae2: a9 fc       ..             ; Buffer length lo = &FC
    sta port_buf_len                                                  ; 9ae4: 85 a2       ..             ; Set buffer length lo
    lda #&21 ; '!'                                                    ; 9ae6: a9 21       .!             ; Buffer start lo = &21
    sta open_port_buf                                                 ; 9ae8: 85 a4       ..             ; Set port buffer lo
    lda #&7f                                                          ; 9aea: a9 7f       ..             ; Buffer hi = &7F (below screen)
    sta open_port_buf_hi                                              ; 9aec: 85 a5       ..             ; Set port buffer hi
    jmp set_tx_reply_flag                                             ; 9aee: 4c 0f 9b    L..            ; Enter reply build path

; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Saves the current TX block pointer, replaces it with a
; pointer to &0D3D, and prepares to send the PEEK response
; data back to the requesting station.
; ***************************************************************************************
.rx_imm_peek
    lda nmi_tx_block                                                  ; 9af1: a5 a0       ..             ; Save current TX block low byte
    pha                                                               ; 9af3: 48          H              ; Push to stack
    lda nmi_tx_block_hi                                               ; 9af4: a5 a1       ..             ; Save current TX block high byte
    pha                                                               ; 9af6: 48          H              ; Push to stack
; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Writes &0D3D to port_ws_offset/rx_buf_offset, sets
; scout_status=2, then calls tx_calc_transfer to send the
; PEEK response data back to the requesting station.
; Uses workspace offsets (&A6/&A7) for nmi_tx_block.
; ***************************************************************************************
.rx_imm_peek_setup
    lda #&3d ; '='                                                    ; 9af7: a9 3d       .=             ; Port workspace offset = &3D
    sta nmi_tx_block                                                  ; 9af9: 85 a0       ..             ; Store workspace offset lo
    lda #&0d                                                          ; 9afb: a9 0d       ..             ; RX buffer page = &0D
    sta nmi_tx_block_hi                                               ; 9afd: 85 a1       ..             ; Store workspace offset hi
    lda #2                                                            ; 9aff: a9 02       ..             ; Scout status = 2 (PEEK response)
    sta scout_status                                                  ; 9b01: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9b04: 20 6a 9f     j.            ; Calculate transfer size for response
    pla                                                               ; 9b07: 68          h              ; Restore saved nmi_tx_block_hi
    sta nmi_tx_block_hi                                               ; 9b08: 85 a1       ..             ; Restore workspace ptr hi byte
    pla                                                               ; 9b0a: 68          h              ; Restore saved nmi_tx_block
    sta nmi_tx_block                                                  ; 9b0b: 85 a0       ..             ; Restore workspace ptr lo byte
    bcc imm_op_discard                                                ; 9b0d: 90 4f       .O             ; C=0: transfer not set up, discard
; &9b0f referenced 1 time by &9aee
.set_tx_reply_flag
    lda tx_flags                                                      ; 9b0f: ad 4a 0d    .J.            ; Mark TX flags bit 7 (reply pending)
    ora #&80                                                          ; 9b12: 09 80       ..             ; Set reply pending flag
    sta tx_flags                                                      ; 9b14: 8d 4a 0d    .J.            ; Store updated TX flags
.rx_imm_halt_cont
    lda #&44 ; 'D'                                                    ; 9b17: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    sta econet_control1_or_status1                                    ; 9b19: 8d a0 fe    ...            ; Write CR1: enable TX interrupts
.tx_cr2_setup
tx_cr2_operand = tx_cr2_setup+1
    lda #&a7                                                          ; 9b1c: a9 a7       ..             ; CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE
; &9b1d referenced 1 time by &9b9b
    sta econet_control23_or_status2                                   ; 9b1e: 8d a1 fe    ...            ; Write CR2 for TX setup
.tx_nmi_setup
tx_nmi_lo_operand = tx_nmi_setup+1
    lda #&3e ; '>'                                                    ; 9b21: a9 3e       .>             ; NMI handler lo byte (self-modifying)
; &9b22 referenced 1 time by &9b97
.tx_nmi_dispatch_page
    ldy #&9b                                                          ; 9b23: a0 9b       ..             ; Y=&9B: dispatch table page
    jmp ack_tx_write_dest                                             ; 9b25: 4c 7e 99    L~.            ; Acknowledge and write TX dest

; ***************************************************************************************
; Build immediate operation reply header
; 
; Stores data length, source station/network, and control byte
; into the RX buffer header area for port-0 immediate operations.
; Then disables SR interrupts and configures the VIA shift
; register for shift-in mode before returning to
; idle listen.
; ***************************************************************************************
; &9b28 referenced 1 time by &99d1
.imm_op_build_reply
    lda port_buf_len                                                  ; 9b28: a5 a2       ..             ; Get buffer position for reply header
    clc                                                               ; 9b2a: 18          .              ; Clear carry for offset addition
    adc #&80                                                          ; 9b2b: 69 80       i.             ; Data offset = buf_len + &80 (past header)
    ldy #&7f                                                          ; 9b2d: a0 7f       ..             ; Y=&7F: reply data length slot
    sta (net_rx_ptr),y                                                ; 9b2f: 91 9c       ..             ; Store reply data length in RX buffer
    ldy #&80                                                          ; 9b31: a0 80       ..             ; Y=&80: source station slot
    lda rx_src_stn                                                    ; 9b33: ad 3d 0d    .=.            ; Load requesting station number
    sta (net_rx_ptr),y                                                ; 9b36: 91 9c       ..             ; Store source station in reply header
    iny                                                               ; 9b38: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9b39: ad 3e 0d    .>.            ; Load requesting network number
    sta (net_rx_ptr),y                                                ; 9b3c: 91 9c       ..             ; Store source network in reply header
    lda rx_ctrl                                                       ; 9b3e: ad 3f 0d    .?.            ; Load control byte from received frame
    sta tx_work_57                                                    ; 9b41: 8d 57 0d    .W.            ; Save ctrl byte for TX response
    lda #&84                                                          ; 9b44: a9 84       ..             ; IER bit 2: disable SR interrupt
    sta system_via_ier                                                ; 9b46: 8d 4e fe    .N.            ; Write IER to disable SR
    lda system_via_acr                                                ; 9b49: ad 4b fe    .K.            ; Read ACR for shift register config
    and #&1c                                                          ; 9b4c: 29 1c       ).             ; Isolate shift register mode bits (2-4)
    sta tx_work_51                                                    ; 9b4e: 8d 51 0d    .Q.            ; Save original SR mode for later restore
    lda system_via_acr                                                ; 9b51: ad 4b fe    .K.            ; Reload ACR for modification
    and #&e3                                                          ; 9b54: 29 e3       ).             ; Clear SR mode bits (keep other bits)
    ora #8                                                            ; 9b56: 09 08       ..             ; SR mode 2: shift in under φ2
    sta system_via_acr                                                ; 9b58: 8d 4b fe    .K.            ; Apply new shift register mode
    bit system_via_sr                                                 ; 9b5b: 2c 4a fe    ,J.            ; Read SR to clear pending interrupt
; &9b5e referenced 2 times by &9a93, &9b0d
.imm_op_discard
    jmp discard_listen                                                ; 9b5e: 4c 56 9a    LV.            ; Return to idle listen mode

; &9b61 referenced 1 time by &966c
.check_sr_irq
    lda #4                                                            ; 9b61: a9 04       ..             ; A=&04: IFR bit 2 (SR) mask
    bit system_via_ifr                                                ; 9b63: 2c 4d fe    ,M.            ; Test SR interrupt pending
    bne tx_done_error                                                 ; 9b66: d0 03       ..             ; SR fired: handle TX completion
    lda #5                                                            ; 9b68: a9 05       ..             ; A=5: no SR, return status 5
    rts                                                               ; 9b6a: 60          `              ; Return (no SR interrupt)

; &9b6b referenced 1 time by &9b66
.tx_done_error
    txa                                                               ; 9b6b: 8a          .              ; Save X
    pha                                                               ; 9b6c: 48          H              ; Push X
    tya                                                               ; 9b6d: 98          .              ; Save Y
    pha                                                               ; 9b6e: 48          H              ; Push Y
    lda system_via_acr                                                ; 9b6f: ad 4b fe    .K.            ; Read ACR for shift register mode
    and #&e3                                                          ; 9b72: 29 e3       ).             ; Clear SR mode bits (2-4)
    ora tx_work_51                                                    ; 9b74: 0d 51 0d    .Q.            ; Restore original SR mode
    sta system_via_acr                                                ; 9b77: 8d 4b fe    .K.            ; Write updated ACR
    lda system_via_sr                                                 ; 9b7a: ad 4a fe    .J.            ; Read SR to clear pending interrupt
    lda #4                                                            ; 9b7d: a9 04       ..             ; A=&04: SR bit mask
    sta system_via_ifr                                                ; 9b7f: 8d 4d fe    .M.            ; Clear SR in IFR
    sta system_via_ier                                                ; 9b82: 8d 4e fe    .N.            ; Disable SR in IER
    ldy tx_work_57                                                    ; 9b85: ac 57 0d    .W.            ; Load ctrl byte for dispatch
    cpy #&86                                                          ; 9b88: c0 86       ..             ; Ctrl >= &86? (HALT/CONTINUE)
    bcs tx_done_classify                                              ; 9b8a: b0 0b       ..             ; Yes: skip protection mask save
    lda prot_status                                                   ; 9b8c: ad 63 0d    .c.            ; Load current protection mask
    sta saved_jsr_mask                                                ; 9b8f: 8d 65 0d    .e.            ; Save mask before JSR modification
    ora #&1c                                                          ; 9b92: 09 1c       ..             ; Enable bits 2-4 (allow JSR ops)
    sta prot_status                                                   ; 9b94: 8d 63 0d    .c.            ; Store modified protection mask
; &9b97 referenced 1 time by &9b8a
.tx_done_classify
    lda tx_nmi_lo_operand,y                                           ; 9b97: b9 22 9b    .".            ; Load handler addr hi from table
    pha                                                               ; 9b9a: 48          H              ; Push handler hi
    lda tx_cr2_operand,y                                              ; 9b9b: b9 1d 9b    ...            ; Load handler addr lo from table
    pha                                                               ; 9b9e: 48          H              ; Push handler lo
    rts                                                               ; 9b9f: 60          `              ; Dispatch via RTS (addr-1 on stack)

    equb <(tx_done_jsr-1)                                             ; 9ba0: a9          .
    equb <(tx_done_user_proc-1)                                       ; 9ba1: b2          .
    equb <(tx_done_os_proc-1)                                         ; 9ba2: c0          .
    equb <(tx_done_halt-1)                                            ; 9ba3: cc          .
    equb <(tx_done_continue-1)                                        ; 9ba4: e3          .
    equb >(tx_done_jsr-1)                                             ; 9ba5: 9b          .
    equb >(tx_done_user_proc-1)                                       ; 9ba6: 9b          .
    equb >(tx_done_os_proc-1)                                         ; 9ba7: 9b          .
    equb >(tx_done_halt-1)                                            ; 9ba8: 9b          .
    equb >(tx_done_continue-1)                                        ; 9ba9: 9b          .

; ***************************************************************************************
; TX done: remote JSR execution
; 
; Pushes address &9BEB on the stack (so RTS returns to
; tx_done_exit), then does JMP (l0d58) to call the remote
; JSR target routine. When that routine returns via RTS,
; control resumes at tx_done_exit.
; ***************************************************************************************
.tx_done_jsr
    lda #&9b                                                          ; 9baa: a9 9b       ..             ; Push hi of (tx_done_exit-1)
    pha                                                               ; 9bac: 48          H              ; Push hi byte on stack
    lda #&eb                                                          ; 9bad: a9 eb       ..             ; Push lo of (tx_done_exit-1)
    pha                                                               ; 9baf: 48          H              ; Push lo byte on stack
    jmp (l0d58)                                                       ; 9bb0: 6c 58 0d    lX.            ; Call remote JSR; RTS to tx_done_exit

; ***************************************************************************************
; TX done: UserProc event
; 
; Generates a network event (event 8) via OSEVEN with
; X=l0d58, A=l0d59 (the remote address). This notifies
; the user program that a UserProc operation has completed.
; ***************************************************************************************
.tx_done_user_proc
    ldy #event_network_error                                          ; 9bb3: a0 08       ..             ; Y=8: network event type
    ldx l0d58                                                         ; 9bb5: ae 58 0d    .X.            ; X = remote address lo
    lda l0d59                                                         ; 9bb8: ad 59 0d    .Y.            ; A = remote address hi
    jsr oseven                                                        ; 9bbb: 20 bf ff     ..            ; Generate event Y='Network error'
    jmp tx_done_exit                                                  ; 9bbe: 4c ec 9b    L..            ; Exit TX done handler

; ***************************************************************************************
; TX done: OSProc call
; 
; Calls the ROM entry point at &8000 (rom_header) with
; X=l0d58, Y=l0d59. This invokes an OS-level procedure
; on behalf of the remote station.
; ***************************************************************************************
.tx_done_os_proc
    ldx l0d58                                                         ; 9bc1: ae 58 0d    .X.            ; X = remote address lo
    ldy l0d59                                                         ; 9bc4: ac 59 0d    .Y.            ; Y = remote address hi
    jsr rom_header                                                    ; 9bc7: 20 00 80     ..            ; Call ROM entry point at &8000
    jmp tx_done_exit                                                  ; 9bca: 4c ec 9b    L..            ; Exit TX done handler

; ***************************************************************************************
; TX done: HALT
; 
; Sets bit 2 of rx_flags (&0D64), enables interrupts, and
; spin-waits until bit 2 is cleared (by a CONTINUE from the
; remote station). If bit 2 is already set, skips to exit.
; ***************************************************************************************
.tx_done_halt
    lda #4                                                            ; 9bcd: a9 04       ..             ; A=&04: bit 2 mask for rx_flags
    bit rx_flags                                                      ; 9bcf: 2c 64 0d    ,d.            ; Test if already halted
    bne tx_done_exit                                                  ; 9bd2: d0 18       ..             ; Already halted: skip to exit
    ora rx_flags                                                      ; 9bd4: 0d 64 0d    .d.            ; Set bit 2 in rx_flags
    sta rx_flags                                                      ; 9bd7: 8d 64 0d    .d.            ; Store halt flag
    lda #4                                                            ; 9bda: a9 04       ..             ; A=4: re-load halt bit mask
    cli                                                               ; 9bdc: 58          X              ; Enable interrupts during halt wait
; &9bdd referenced 1 time by &9be0
.halt_spin_loop
    bit rx_flags                                                      ; 9bdd: 2c 64 0d    ,d.            ; Test halt flag
    bne halt_spin_loop                                                ; 9be0: d0 fb       ..             ; Still halted: keep spinning
    beq tx_done_exit                                                  ; 9be2: f0 08       ..             ; ALWAYS branch

; ***************************************************************************************
; TX done: CONTINUE
; 
; Clears bit 2 of rx_flags (&0D64), releasing any station
; that is halted and spinning in tx_done_halt.
; ***************************************************************************************
.tx_done_continue
    lda rx_flags                                                      ; 9be4: ad 64 0d    .d.            ; Load current RX flags
    and #&fb                                                          ; 9be7: 29 fb       ).             ; Clear bit 2: release halted station
    sta rx_flags                                                      ; 9be9: 8d 64 0d    .d.            ; Store updated flags
; &9bec referenced 4 times by &9bbe, &9bca, &9bd2, &9be2
.tx_done_exit
    pla                                                               ; 9bec: 68          h              ; Restore Y from stack
    tay                                                               ; 9bed: a8          .              ; Transfer to Y register
    pla                                                               ; 9bee: 68          h              ; Restore X from stack
    tax                                                               ; 9bef: aa          .              ; Transfer to X register
    lda #0                                                            ; 9bf0: a9 00       ..             ; A=0: success status
    rts                                                               ; 9bf2: 60          `              ; Return with A=0 (success)

; ***************************************************************************************
; Begin TX operation
; 
; Main TX initiation entry point (called via trampoline at &06CE).
; Copies dest station/network from the TXCB to the scout buffer,
; dispatches to immediate op setup (ctrl >= &81) or normal data
; transfer, calculates transfer sizes, copies extra parameters,
; then enters the INACTIVE polling loop.
; ***************************************************************************************
; &9bf3 referenced 1 time by &9660
.tx_begin
    txa                                                               ; 9bf3: 8a          .              ; Save X on stack
    pha                                                               ; 9bf4: 48          H              ; Push X
    ldy #2                                                            ; 9bf5: a0 02       ..             ; Y=2: TXCB offset for dest station
    lda (nmi_tx_block),y                                              ; 9bf7: b1 a0       ..             ; Load dest station from TX control block
    sta tx_dst_stn                                                    ; 9bf9: 8d 20 0d    . .            ; Store to TX scout buffer
    iny                                                               ; 9bfc: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9bfd: b1 a0       ..             ; Load dest network from TX control block
    sta tx_dst_net                                                    ; 9bff: 8d 21 0d    .!.            ; Store to TX scout buffer
    ldy #0                                                            ; 9c02: a0 00       ..             ; Y=0: first byte of TX control block
    lda (nmi_tx_block),y                                              ; 9c04: b1 a0       ..             ; Load control/flag byte
    bmi tx_imm_op_setup                                               ; 9c06: 30 03       0.             ; Bit7 set: immediate operation ctrl byte
    jmp tx_active_start                                               ; 9c08: 4c 93 9c    L..            ; Bit7 clear: normal data transfer

; &9c0b referenced 1 time by &9c06
.tx_imm_op_setup
    sta tx_ctrl_byte                                                  ; 9c0b: 8d 24 0d    .$.            ; Store control byte to TX scout buffer
    tax                                                               ; 9c0e: aa          .              ; X = control byte for range checks
    iny                                                               ; 9c0f: c8          .              ; Y=1: port byte offset
    lda (nmi_tx_block),y                                              ; 9c10: b1 a0       ..             ; Load port byte from TX control block
    sta tx_port                                                       ; 9c12: 8d 25 0d    .%.            ; Store port byte to TX scout buffer
    bne tx_line_idle_check                                            ; 9c15: d0 2f       ./             ; Port != 0: skip immediate op setup
    cpx #&83                                                          ; 9c17: e0 83       ..             ; Ctrl < &83: PEEK/POKE need address calc
    bcs check_imm_range                                               ; 9c19: b0 1b       ..             ; Ctrl >= &83: skip to range check
    sec                                                               ; 9c1b: 38          8              ; SEC: init borrow for 4-byte subtract
    php                                                               ; 9c1c: 08          .              ; Save carry on stack for loop
    ldy #8                                                            ; 9c1d: a0 08       ..             ; Y=8: high pointer offset in TXCB
; &9c1f referenced 1 time by &9c33
.calc_peek_poke_size
    lda (nmi_tx_block),y                                              ; 9c1f: b1 a0       ..             ; Load TXCB[Y] (end addr byte)
    dey                                                               ; 9c21: 88          .              ; Y -= 4: back to start addr offset
    dey                                                               ; 9c22: 88          .              ; (Y -= 4: reach start addr offset)
    dey                                                               ; 9c23: 88          .              ; (continued)
    dey                                                               ; 9c24: 88          .              ; (continued)
    plp                                                               ; 9c25: 28          (              ; Restore borrow from stack
    sbc (nmi_tx_block),y                                              ; 9c26: f1 a0       ..             ; end - start = transfer size byte
    sta tx_data_start,y                                               ; 9c28: 99 26 0d    .&.            ; Store result to tx_data_start
    iny                                                               ; 9c2b: c8          .              ; (Y += 5: advance to next end byte)
    iny                                                               ; 9c2c: c8          .              ; (continued)
    iny                                                               ; 9c2d: c8          .              ; (continued)
    iny                                                               ; 9c2e: c8          .              ; (continued)
    iny                                                               ; 9c2f: c8          .              ; (continued)
    php                                                               ; 9c30: 08          .              ; Save borrow for next byte
    cpy #&0c                                                          ; 9c31: c0 0c       ..             ; Done all 4 bytes? (Y reaches &0C)
    bcc calc_peek_poke_size                                           ; 9c33: 90 ea       ..             ; No: next byte pair
    plp                                                               ; 9c35: 28          (              ; Discard final borrow
; &9c36 referenced 1 time by &9c19
.check_imm_range
    cpx #&89                                                          ; 9c36: e0 89       ..             ; Ctrl >= &89: out of immediate range
    bcs tx_active_start                                               ; 9c38: b0 59       .Y             ; Above range: normal data transfer
    ldy #&0c                                                          ; 9c3a: a0 0c       ..             ; Y=&0C: start of extra data in TXCB
; &9c3c referenced 1 time by &9c44
.copy_imm_params
    lda (nmi_tx_block),y                                              ; 9c3c: b1 a0       ..             ; Load extra parameter byte from TXCB
    sta nmi_shim_1a,y                                                 ; 9c3e: 99 1a 0d    ...            ; Copy to NMI shim workspace at &0D1A+Y
    iny                                                               ; 9c41: c8          .              ; Next byte
    cpy #&10                                                          ; 9c42: c0 10       ..             ; Done 4 bytes? (Y reaches &10)
    bcc copy_imm_params                                               ; 9c44: 90 f6       ..             ; No: continue copying
; &9c46 referenced 1 time by &9c15
.tx_line_idle_check
    lda #&20 ; ' '                                                    ; 9c46: a9 20       .              ; A=&20: mask for SR2 INACTIVE bit
    bit econet_control23_or_status2                                   ; 9c48: 2c a1 fe    ,..            ; BIT SR2: test if line is idle
    bne tx_no_clock_error                                             ; 9c4b: d0 56       .V             ; Line not idle: handle as line jammed
    lda #&fd                                                          ; 9c4d: a9 fd       ..             ; A=&FD: high byte of timeout counter
    pha                                                               ; 9c4f: 48          H              ; Push timeout high byte to stack
    lda #6                                                            ; 9c50: a9 06       ..             ; Scout frame = 6 address+ctrl bytes
    sta tx_length                                                     ; 9c52: 8d 50 0d    .P.            ; Store scout frame length
    lda #0                                                            ; 9c55: a9 00       ..             ; A=0: init low byte of timeout counter
; ***************************************************************************************
; INACTIVE polling loop
; 
; Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
; attempting transmission. Uses a 3-byte timeout counter on the stack.
; The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
; never appears.
; The CTS check at &9C75-&9C7A works because CR2=&67 has RTS=0, so
; cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.
; ***************************************************************************************
.inactive_poll
    sta tx_index                                                      ; 9c57: 8d 4f 0d    .O.            ; Save TX index
    pha                                                               ; 9c5a: 48          H              ; Push timeout byte 1 on stack
    pha                                                               ; 9c5b: 48          H              ; Push timeout byte 2 on stack
    ldy #&e7                                                          ; 9c5c: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9c5e referenced 3 times by &9c84, &9c89, &9c8e
.test_inactive_retry
    lda #4                                                            ; 9c5e: a9 04       ..             ; A=&04: INACTIVE mask for SR2 bit2
    php                                                               ; 9c60: 08          .              ; Save interrupt state
    sei                                                               ; 9c61: 78          x              ; Disable interrupts for ADLC access
; ***************************************************************************************
; Disable NMIs and test INACTIVE
; 
; Mid-instruction label within the INACTIVE polling loop. The
; address &9BE2 is referenced as a constant for self-modifying
; code. Disables NMIs twice (belt-and-braces) then tests SR2
; for INACTIVE before proceeding with TX.
; ***************************************************************************************
; &9c62 referenced 1 time by &9cde
.intoff_test_inactive
    bit station_id_disable_net_nmis                                   ; 9c62: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
    bit station_id_disable_net_nmis                                   ; 9c65: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.test_line_idle
sr2_test_operand = test_line_idle+2
    bit econet_control23_or_status2                                   ; 9c68: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
; &9c6a referenced 1 time by &9cda
    beq inactive_retry                                                ; 9c6b: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9c6d: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9c70: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9c72: 8d a1 fe    ...            ; Write CR2: clear status, prepare TX
    lda #&10                                                          ; 9c75: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9c77: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9c7a: d0 35       .5             ; CTS set -- clock hardware detected, start TX
; &9c7c referenced 1 time by &9c6b
.inactive_retry
    bit video_ula_control                                             ; 9c7c: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 9c7f: 28          (              ; Restore interrupt state
    tsx                                                               ; 9c80: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c81: fe 01 01    ...            ; Increment timeout counter byte 1
    bne test_inactive_retry                                           ; 9c84: d0 d8       ..             ; Not overflowed: retry INACTIVE test
    inc l0102,x                                                       ; 9c86: fe 02 01    ...            ; Increment timeout counter byte 2
    bne test_inactive_retry                                           ; 9c89: d0 d3       ..             ; Not overflowed: retry INACTIVE test
    inc l0103,x                                                       ; 9c8b: fe 03 01    ...            ; Increment timeout counter byte 3
    bne test_inactive_retry                                           ; 9c8e: d0 ce       ..             ; Not overflowed: retry INACTIVE test
    jmp tx_line_jammed                                                ; 9c90: 4c 97 9c    L..            ; All 3 bytes overflowed: line jammed

; TX_ACTIVE branch (A=&44 = CR1 value for TX active)
; &9c93 referenced 2 times by &9c08, &9c38
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c93: a9 44       .D             ; CR1=&44: TIE | TX_LAST_DATA
    bne store_tx_error                                                ; 9c95: d0 0e       ..             ; ALWAYS branch

; ***************************************************************************************
; TX timeout error handler (Line Jammed)
; 
; Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
; timeout loop's state), then stores error code &40 ("Line
; Jammed") into the TX control block and signals completion.
; ***************************************************************************************
; &9c97 referenced 1 time by &9c90
.tx_line_jammed
    lda #7                                                            ; 9c97: a9 07       ..             ; CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 9c99: 8d a1 fe    ...            ; Write CR2 to abort TX
    pla                                                               ; 9c9c: 68          h              ; Clean 3 bytes of timeout loop state
    pla                                                               ; 9c9d: 68          h              ; Pop saved register
    pla                                                               ; 9c9e: 68          h              ; Pop saved register
    lda #&40 ; '@'                                                    ; 9c9f: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne store_tx_error                                                ; 9ca1: d0 02       ..             ; ALWAYS branch to shared error handler; ALWAYS branch

; &9ca3 referenced 1 time by &9c4b
.tx_no_clock_error
    lda #&43 ; 'C'                                                    ; 9ca3: a9 43       .C             ; Error &43 = 'No Clock'
; &9ca5 referenced 2 times by &9c95, &9ca1
.store_tx_error
    ldy #0                                                            ; 9ca5: a0 00       ..             ; Offset 0 = error byte in TX control block
    sta (nmi_tx_block),y                                              ; 9ca7: 91 a0       ..             ; Store error code in TX CB byte 0
    lda #&80                                                          ; 9ca9: a9 80       ..             ; &80 = TX complete flag
    sta tx_clear_flag                                                 ; 9cab: 8d 62 0d    .b.            ; Signal TX operation complete
    pla                                                               ; 9cae: 68          h              ; Restore X saved by caller
    tax                                                               ; 9caf: aa          .              ; Move to X register
    rts                                                               ; 9cb0: 60          `              ; Return to TX caller

; ***************************************************************************************
; TX preparation
; 
; Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
; installs NMI TX handler at &9D4C, and re-enables NMIs.
; ***************************************************************************************
; &9cb1 referenced 1 time by &9c7a
.tx_prepare
    sty econet_control23_or_status2                                   ; 9cb1: 8c a1 fe    ...            ; Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 9cb4: a2 44       .D             ; CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 9cb6: 8e a0 fe    ...            ; Write to ADLC CR1
    ldx #&5b ; '['                                                    ; 9cb9: a2 5b       .[             ; Install NMI handler at &9D5B (nmi_tx_data)
    ldy #&9d                                                          ; 9cbb: a0 9d       ..             ; High byte of NMI handler address
    stx nmi_jmp_lo                                                    ; 9cbd: 8e 0c 0d    ...            ; Write NMI vector low byte directly
    sty nmi_jmp_hi                                                    ; 9cc0: 8c 0d 0d    ...            ; Write NMI vector high byte directly
    bit video_ula_control                                             ; 9cc3: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 9cc6: ad 25 0d    .%.            ; Load destination port number
    bne setup_data_xfer                                               ; 9cc9: d0 5a       .Z             ; Port != 0: standard data transfer
    ldy tx_ctrl_byte                                                  ; 9ccb: ac 24 0d    .$.            ; Port 0: load control byte for table lookup
    lda tube_tx_byte4_operand,y                                       ; 9cce: b9 e1 9e    ...            ; Look up tx_flags from table
    sta tx_flags                                                      ; 9cd1: 8d 4a 0d    .J.            ; Store operation flags
    lda tube_tx_byte2_operand,y                                       ; 9cd4: b9 d9 9e    ...            ; Look up tx_length from table
    sta tx_length                                                     ; 9cd7: 8d 50 0d    .P.            ; Store expected transfer length
    lda sr2_test_operand,y                                            ; 9cda: b9 6a 9c    .j.            ; Load handler from dispatch table
    pha                                                               ; 9cdd: 48          H              ; Push high byte for PHA/PHA/RTS dispatch
    lda intoff_test_inactive,y                                        ; 9cde: b9 62 9c    .b.            ; Look up handler address low from table
    pha                                                               ; 9ce1: 48          H              ; Push low byte for PHA/PHA/RTS dispatch
    rts                                                               ; 9ce2: 60          `              ; RTS dispatches to control-byte handler

    equb <(tx_ctrl_peek-1)                                            ; 9ce3: f6          .
    equb <(tx_ctrl_poke-1)                                            ; 9ce4: fa          .
    equb <(tx_ctrl_proc-1)                                            ; 9ce5: 19          .
    equb <(tx_ctrl_proc-1)                                            ; 9ce6: 19          .
    equb <(tx_ctrl_proc-1)                                            ; 9ce7: 19          .
    equb <(tx_ctrl_exit-1)                                            ; 9ce8: 53          S
    equb <(tx_ctrl_exit-1)                                            ; 9ce9: 53          S
    equb <(imm_op_status3-1)                                          ; 9cea: f2          .
    equb >(tx_ctrl_peek-1)                                            ; 9ceb: 9c          .
    equb >(tx_ctrl_poke-1)                                            ; 9cec: 9c          .
    equb >(tx_ctrl_proc-1)                                            ; 9ced: 9d          .
    equb >(tx_ctrl_proc-1)                                            ; 9cee: 9d          .
    equb >(tx_ctrl_proc-1)                                            ; 9cef: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cf0: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cf1: 9d          .
    equb >(imm_op_status3-1)                                          ; 9cf2: 9c          .

.imm_op_status3
    lda #3                                                            ; 9cf3: a9 03       ..             ; A=3: scout_status for PEEK
    bne store_status_calc_xfer                                        ; 9cf5: d0 25       .%             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: PEEK transfer setup
; 
; Sets scout_status=3, then performs a 4-byte addition of
; bytes from the TX block into the transfer parameter
; workspace at &0D1E-&0D21 (with carry propagation).
; Calls tx_calc_transfer to finalise, then exits via
; tx_ctrl_exit.
; ***************************************************************************************
.tx_ctrl_peek
    lda #3                                                            ; 9cf7: a9 03       ..             ; A=3: scout_status for PEEK op
    bne store_status_add4                                             ; 9cf9: d0 02       ..             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: POKE transfer setup
; 
; Sets scout_status=2 and shares the 4-byte addition and
; transfer calculation path with tx_ctrl_peek.
; ***************************************************************************************
.tx_ctrl_poke
    lda #2                                                            ; 9cfb: a9 02       ..             ; Scout status = 2 (POKE transfer)
; &9cfd referenced 1 time by &9cf9
.store_status_add4
    sta scout_status                                                  ; 9cfd: 8d 5c 0d    .\.            ; Store scout status
    clc                                                               ; 9d00: 18          .              ; Clear carry for 4-byte addition
    php                                                               ; 9d01: 08          .              ; Save carry on stack
    ldy #&0c                                                          ; 9d02: a0 0c       ..             ; Y=&0C: start at offset 12
; &9d04 referenced 1 time by &9d11
.add_bytes_loop
    lda l0d1e,y                                                       ; 9d04: b9 1e 0d    ...            ; Load workspace address byte
    plp                                                               ; 9d07: 28          (              ; Restore carry from previous byte
    adc (nmi_tx_block),y                                              ; 9d08: 71 a0       q.             ; Add TXCB address byte
    sta l0d1e,y                                                       ; 9d0a: 99 1e 0d    ...            ; Store updated address byte
    iny                                                               ; 9d0d: c8          .              ; Next byte
    php                                                               ; 9d0e: 08          .              ; Save carry for next addition
; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_add_done
    cpy #&10                                                          ; 9d0f: c0 10       ..             ; Compare Y with 16-byte boundary
    bcc add_bytes_loop                                                ; 9d11: 90 f1       ..             ; Below boundary: continue addition
    plp                                                               ; 9d13: 28          (              ; Restore processor flags
    jsr tx_calc_transfer                                              ; 9d14: 20 6a 9f     j.            ; Calculate transfer byte count
    jmp tx_ctrl_exit                                                  ; 9d17: 4c 54 9d    LT.            ; Jump to TX control exit

; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_proc
    lda #2                                                            ; 9d1a: a9 02       ..             ; A=2: scout_status for procedure ops
; &9d1c referenced 1 time by &9cf5
.store_status_calc_xfer
    sta scout_status                                                  ; 9d1c: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9d1f: 20 6a 9f     j.            ; Calculate transfer parameters
    jmp tx_ctrl_exit                                                  ; 9d22: 4c 54 9d    LT.            ; Exit TX ctrl setup

; &9d25 referenced 1 time by &9cc9
.setup_data_xfer
    lda tx_dst_stn                                                    ; 9d25: ad 20 0d    . .            ; Load dest station for broadcast check
    and tx_dst_net                                                    ; 9d28: 2d 21 0d    -!.            ; AND with dest network
    cmp #&ff                                                          ; 9d2b: c9 ff       ..             ; Both &FF = broadcast address?
    bne setup_unicast_xfer                                            ; 9d2d: d0 18       ..             ; Not broadcast: unicast path
    lda #&0e                                                          ; 9d2f: a9 0e       ..             ; Broadcast scout: 14 bytes total
    sta tx_length                                                     ; 9d31: 8d 50 0d    .P.            ; Store broadcast scout length
    lda #&40 ; '@'                                                    ; 9d34: a9 40       .@             ; A=&40: broadcast flag
    sta tx_flags                                                      ; 9d36: 8d 4a 0d    .J.            ; Set broadcast flag in tx_flags
    ldy #4                                                            ; 9d39: a0 04       ..             ; Y=4: start of address data in TXCB
; &9d3b referenced 1 time by &9d43
.copy_bcast_addr
    lda (nmi_tx_block),y                                              ; 9d3b: b1 a0       ..             ; Copy TXCB address bytes to scout buffer
    sta tx_src_stn,y                                                  ; 9d3d: 99 22 0d    .".            ; Store to TX source/data area
    iny                                                               ; 9d40: c8          .              ; Next byte
    cpy #&0c                                                          ; 9d41: c0 0c       ..             ; Done 8 bytes? (Y reaches &0C)
    bcc copy_bcast_addr                                               ; 9d43: 90 f6       ..             ; No: continue copying
    bcs tx_ctrl_exit                                                  ; 9d45: b0 0d       ..             ; ALWAYS branch

; &9d47 referenced 1 time by &9d2d
.setup_unicast_xfer
    lda #0                                                            ; 9d47: a9 00       ..             ; A=0: clear flags for unicast
    sta tx_flags                                                      ; 9d49: 8d 4a 0d    .J.            ; Clear tx_flags
.proc_op_status2
    lda #2                                                            ; 9d4c: a9 02       ..             ; scout_status=2: data transfer pending
.store_status_copy_ptr
    sta scout_status                                                  ; 9d4e: 8d 5c 0d    .\.            ; Store scout status
    jsr tx_calc_transfer                                              ; 9d51: 20 6a 9f     j.            ; Calculate transfer size from RXCB
; &9d54 referenced 3 times by &9d17, &9d22, &9d45
.tx_ctrl_exit
    plp                                                               ; 9d54: 28          (              ; Restore processor status from stack
    pla                                                               ; 9d55: 68          h              ; Restore stacked registers (4 PLAs)
    pla                                                               ; 9d56: 68          h              ; Second PLA
    pla                                                               ; 9d57: 68          h              ; Third PLA
    pla                                                               ; 9d58: 68          h              ; Fourth PLA
    tax                                                               ; 9d59: aa          .              ; Restore X from A
    rts                                                               ; 9d5a: 60          `              ; Return to caller

; ***************************************************************************************
; NMI TX data handler
; 
; Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
; BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
; After writing 2 bytes, checks if the frame is complete. If more data,
; tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
; without returning from NMI (tight loop). Otherwise returns via RTI.
; ***************************************************************************************
.nmi_tx_data
    ldy tx_index                                                      ; 9d5b: ac 4f 0d    .O.            ; Load TX buffer index
    bit econet_control1_or_status1                                    ; 9d5e: 2c a0 fe    ,..            ; BIT SR1: V=bit6(TDRA), N=bit7(IRQ)
; &9d61 referenced 1 time by &9d7c
.tx_fifo_write
    bvc tx_fifo_not_ready                                             ; 9d61: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9d63: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9d66: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9d69: c8          .              ; Next TX buffer byte
    lda tx_dst_stn,y                                                  ; 9d6a: b9 20 0d    . .            ; Load second byte from TX buffer
    iny                                                               ; 9d6d: c8          .              ; Advance TX index past second byte
    sty tx_index                                                      ; 9d6e: 8c 4f 0d    .O.            ; Save updated TX buffer index
    sta econet_data_continue_frame                                    ; 9d71: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9d74: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9d77: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9d79: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi tx_fifo_write                                                 ; 9d7c: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9d7e: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9d81 referenced 1 time by &9dc6
.tx_error
    lda #&42 ; 'B'                                                    ; 9d81: a9 42       .B             ; Error &42
    bne tx_store_error                                                ; 9d83: d0 07       ..             ; ALWAYS branch

; &9d85 referenced 1 time by &9d61
.tx_fifo_not_ready
    lda #&67 ; 'g'                                                    ; 9d85: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9d87: 8d a1 fe    ...            ; Write CR2: clear status, idle listen
    lda #&41 ; 'A'                                                    ; 9d8a: a9 41       .A             ; Error &41 (TDRA not ready)
; &9d8c referenced 1 time by &9d83
.tx_store_error
    ldy station_id_disable_net_nmis                                   ; 9d8c: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d8f referenced 1 time by &9d92
.delay_nmi_disable
    pha                                                               ; 9d8f: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d90: 68          h              ; PHA/PLA delay (~7 cycles each)
    iny                                                               ; 9d91: c8          .              ; Increment delay counter
    bne delay_nmi_disable                                             ; 9d92: d0 fb       ..             ; Loop 256 times for NMI disable
    jmp tx_store_result                                               ; 9d94: 4c 4e 9f    LN.            ; Store error and return to idle

; ***************************************************************************************
; TX_LAST_DATA and frame completion
; 
; Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
; the TX completion NMI handler at &9D94 which switches to RX mode.
; CR2=&3F = 0011_1111:
;   bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
;   bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
;   bit3: FLAG_IDLE -- send flags/idle after frame
;   bit2: FC_TDRA -- force clear TDRA
;   bit1: 2_1_BYTE -- two-byte transfer mode
;   bit0: PSE -- prioritised status enable
; Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)
; ***************************************************************************************
; &9d97 referenced 1 time by &9d77
.tx_last_data
    lda #&3f ; '?'                                                    ; 9d97: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 9d99: 8d a1 fe    ...            ; Write to ADLC CR2
    lda #&a3                                                          ; 9d9c: a9 a3       ..             ; Install NMI handler at &9DA3 (nmi_tx_complete)
    ldy #&9d                                                          ; 9d9e: a0 9d       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9da0: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; TX completion: switch to RX mode
; 
; Called via NMI after the frame (including CRC and closing flag) has been
; fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
; CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
; Checks workspace flags to decide next action:
;   - bit6 set at &0D4A -> completion at &9F48
;   - bit0 set at &0D4A -> four-way handshake data phase at &9EEC
;   - Otherwise -> install RX reply handler at &9DB2
; ***************************************************************************************
.nmi_tx_complete
    lda #&82                                                          ; 9da3: a9 82       ..             ; CR1=&82: TX_RESET | RIE (now in RX mode)
    sta econet_control1_or_status1                                    ; 9da5: 8d a0 fe    ...            ; Write CR1 to switch from TX to RX
    bit tx_flags                                                      ; 9da8: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc check_handshake_bit                                           ; 9dab: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9dad: 4c 48 9f    LH.            ; bit6 set -- TX completion

; &9db0 referenced 1 time by &9dab
.check_handshake_bit
    lda #1                                                            ; 9db0: a9 01       ..             ; A=1: mask for bit0 test
    bit tx_flags                                                      ; 9db2: 2c 4a 0d    ,J.            ; Test tx_flags bit0 (handshake)
    beq install_reply_scout                                           ; 9db5: f0 03       ..             ; bit0 clear: install reply handler
    jmp handshake_await_ack                                           ; 9db7: 4c ec 9e    L..            ; bit0 set -- four-way handshake data phase

; &9dba referenced 1 time by &9db5
.install_reply_scout
    lda #&c1                                                          ; 9dba: a9 c1       ..             ; Install nmi_reply_scout at &9DC1
    ldy #&9d                                                          ; 9dbc: a0 9d       ..             ; High byte of nmi_reply_scout addr
    jmp set_nmi_vector                                                ; 9dbe: 4c 0e 0d    L..            ; Install handler and RTI

; ***************************************************************************************
; RX reply scout handler
; 
; Handles reception of the reply scout frame after transmission.
; Checks SR2 bit0 (AP) for incoming data, reads the first byte
; (destination station) and compares to our station ID via &FE18
; (which also disables NMIs as a side effect).
; ***************************************************************************************
.nmi_reply_scout
    lda #1                                                            ; 9dc1: a9 01       ..             ; A=&01: AP mask for SR2
    bit econet_control23_or_status2                                   ; 9dc3: 2c a1 fe    ,..            ; BIT SR2: test AP (Address Present)
    beq tx_error                                                      ; 9dc6: f0 b9       ..             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9dc8: ad a2 fe    ...            ; Read first RX byte (destination station)
    cmp station_id_disable_net_nmis                                   ; 9dcb: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne reply_error                                                   ; 9dce: d0 1d       ..             ; Not our station -- error/reject
    lda #&d7                                                          ; 9dd0: a9 d7       ..             ; Install nmi_reply_cont at &9DD7
    ldy #&9d                                                          ; 9dd2: a0 9d       ..             ; High byte of nmi_reply_cont
    jmp set_nmi_vector                                                ; 9dd4: 4c 0e 0d    L..            ; Install continuation handler

; ***************************************************************************************
; RX reply continuation handler
; 
; Reads the second byte of the reply scout (destination network) and
; validates it is zero (local network). Installs &9DF2 for the
; remaining two bytes (source station and network).
; Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DE8.
; If IRQ is still set, falls through directly to &9DF2 without an RTI,
; avoiding NMI re-entry overhead for short frames where all bytes arrive
; in quick succession.
; ***************************************************************************************
.nmi_reply_cont
    bit econet_control23_or_status2                                   ; 9dd7: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl reply_error                                                   ; 9dda: 10 11       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9ddc: ad a2 fe    ...            ; Read destination network byte
    bne reply_error                                                   ; 9ddf: d0 0c       ..             ; Non-zero -- network mismatch, error
    lda #&f2                                                          ; 9de1: a9 f2       ..             ; Install nmi_reply_validate at &9D5B
    ldy #&9d                                                          ; 9de3: a0 9d       ..             ; High byte of nmi_reply_validate
    bit econet_control1_or_status1                                    ; 9de5: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9de8: 30 08       0.             ; IRQ set -- fall through to &9D5B without RTI
    jmp set_nmi_vector                                                ; 9dea: 4c 0e 0d    L..            ; IRQ not set -- install handler and RTI

; &9ded referenced 7 times by &9dce, &9dda, &9ddf, &9df5, &9dfd, &9e05, &9e0c
.reply_error
    lda #&41 ; 'A'                                                    ; 9ded: a9 41       .A             ; A=&41: 'not listening' error code
.reject_reply
    jmp tx_store_result                                               ; 9def: 4c 4e 9f    LN.            ; Store error and return to idle

; ***************************************************************************************
; RX reply validation (Path 2 for FV/PSE interaction)
; 
; Reads the source station and source network from the reply scout and
; validates them against the original TX destination (&0D20/&0D21).
; Sequence:
;   1. Check SR2 bit7 (RDA) at &9DF2 -- must see data available
;   2. Read source station at &9DF7, compare to &0D20 (tx_dst_stn)
;   3. Read source network at &9DFF, compare to &0D21 (tx_dst_net)
;   4. Check SR2 bit1 (FV) at &9E09 -- must see frame complete
; If all checks pass, the reply scout is valid and the ROM proceeds
; to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).
; ***************************************************************************************
; &9df2 referenced 1 time by &9de8
.nmi_reply_validate
    bit econet_control23_or_status2                                   ; 9df2: 2c a1 fe    ,..            ; BIT SR2: test RDA (bit7). Must be set for valid reply.
    bpl reply_error                                                   ; 9df5: 10 f6       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 9df7: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9dfa: cd 20 0d    . .            ; Compare to original TX destination station (&0D20)
    bne reply_error                                                   ; 9dfd: d0 ee       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 9dff: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9e02: cd 21 0d    .!.            ; Compare to original TX destination network (&0D21)
    bne reply_error                                                   ; 9e05: d0 e6       ..             ; Mismatch -- error
    lda #2                                                            ; 9e07: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9e09: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq reply_error                                                   ; 9e0c: f0 df       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 9e0e: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 9e10: 8d a1 fe    ...            ; Write CR2: enable RTS for TX handshake
    lda #&44 ; 'D'                                                    ; 9e13: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9e15: 8d a0 fe    ...            ; Write CR1: reset RX, enable TX interrupt
    lda #&ec                                                          ; 9e18: a9 ec       ..             ; Install next handler at &9EEC into &0D4B/&0D4C
    ldy #&9e                                                          ; 9e1a: a0 9e       ..             ; High byte &9E of next handler address
    sta nmi_next_lo                                                   ; 9e1c: 8d 4b 0d    .K.            ; Store low byte to nmi_next_lo
    sty nmi_next_hi                                                   ; 9e1f: 8c 4c 0d    .L.            ; Store high byte to nmi_next_hi
    lda tx_dst_stn                                                    ; 9e22: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9e25: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc data_tx_error                                                 ; 9e28: 50 73       Ps             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e2a: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9e2d: ad 21 0d    .!.            ; Load dest network for scout ACK TX
    sta econet_data_continue_frame                                    ; 9e30: 8d a2 fe    ...            ; Write dest network to TX FIFO
    lda #&3a ; ':'                                                    ; 9e33: a9 3a       .:             ; Install nmi_scout_ack_src at &9DA3
    ldy #&9e                                                          ; 9e35: a0 9e       ..             ; High byte &9D of handler address
    jmp set_nmi_vector                                                ; 9e37: 4c 0e 0d    L..            ; Set NMI vector and return

; ***************************************************************************************
; TX scout ACK: write source address
; 
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9e3a: ad 18 fe    ...            ; Read our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9e3d: 2c a0 fe    ,..            ; BIT SR1: check TDRA before writing
    bvc data_tx_error                                                 ; 9e40: 50 5b       P[             ; TDRA not ready: TX error
    sta econet_data_continue_frame                                    ; 9e42: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9e45: a9 00       ..             ; Network = 0 (local network)
    sta econet_data_continue_frame                                    ; 9e47: 8d a2 fe    ...            ; Write network byte to TX FIFO
; &9e4a referenced 1 time by &99bf
.data_tx_begin
    lda #2                                                            ; 9e4a: a9 02       ..             ; Test bit 1 of tx_flags
    bit tx_flags                                                      ; 9e4c: 2c 4a 0d    ,J.            ; Check if immediate-op or data-transfer
    bne install_imm_data_nmi                                          ; 9e4f: d0 07       ..             ; Bit 1 set: immediate op, use alt handler
    lda #&5f ; '_'                                                    ; 9e51: a9 5f       ._             ; Install nmi_data_tx at &9E5F
    ldy #&9e                                                          ; 9e53: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9e55: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; &9e58 referenced 1 time by &9e4f
.install_imm_data_nmi
    lda #&b3                                                          ; 9e58: a9 b3       ..             ; Install nmi_data_tx_tube at &9EB3
    ldy #&9e                                                          ; 9e5a: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9e5c: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; TX data phase: send payload
; 
; Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
; Same pattern as the NMI TX handler at &9D4C but reads from the port
; buffer instead of the TX workspace. Writes two bytes per iteration,
; checking SR1 IRQ between pairs for tight looping.
; ***************************************************************************************
.nmi_data_tx
    ldy port_buf_len                                                  ; 9e5f: a4 a2       ..             ; Y = buffer offset, resume from last position
    bit econet_control1_or_status1                                    ; 9e61: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &9e64 referenced 1 time by &9e87
.data_tx_check_fifo
    bvc data_tx_error                                                 ; 9e64: 50 37       P7             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9e66: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9e68: 8d a2 fe    ...            ; Write first byte of pair to FIFO
    iny                                                               ; 9e6b: c8          .              ; Advance buffer offset
    bne write_second_tx_byte                                          ; 9e6c: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 9e6e: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 9e70: f0 1a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 9e72: e6 a5       ..             ; Increment buffer high byte
; &9e74 referenced 1 time by &9e6c
.write_second_tx_byte
    lda (open_port_buf),y                                             ; 9e74: b1 a4       ..             ; Load second byte of pair
    sta econet_data_continue_frame                                    ; 9e76: 8d a2 fe    ...            ; Write second byte to FIFO
    iny                                                               ; 9e79: c8          .              ; Advance buffer offset
    sty port_buf_len                                                  ; 9e7a: 84 a2       ..             ; Save updated buffer position
    bne check_irq_loop                                                ; 9e7c: d0 06       ..             ; No page crossing
    dec port_buf_len_hi                                               ; 9e7e: c6 a3       ..             ; Page crossing: decrement page count
    beq data_tx_last                                                  ; 9e80: f0 0a       ..             ; No pages left: send last data
    inc open_port_buf_hi                                              ; 9e82: e6 a5       ..             ; Increment buffer high byte
; &9e84 referenced 1 time by &9e7c
.check_irq_loop
    bit econet_control1_or_status1                                    ; 9e84: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) for tight loop
    bmi data_tx_check_fifo                                            ; 9e87: 30 db       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 9e89: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; &9e8c referenced 4 times by &9e70, &9e80, &9ecc, &9ee2
.data_tx_last
    lda #&3f ; '?'                                                    ; 9e8c: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9e8e: 8d a1 fe    ...            ; Write CR2 to close frame
    lda tx_flags                                                      ; 9e91: ad 4a 0d    .J.            ; Check tx_flags for next action
    bpl install_saved_handler                                         ; 9e94: 10 14       ..             ; Bit7 clear: error, install saved handler
    lda #&4a ; 'J'                                                    ; 9e96: a9 4a       .J             ; Install discard_reset_listen at &9A4A
    ldy #&9a                                                          ; 9e98: a0 9a       ..             ; High byte of &9A4A handler
    jmp set_nmi_vector                                                ; 9e9a: 4c 0e 0d    L..            ; Set NMI vector and return

; &9e9d referenced 4 times by &9e28, &9e40, &9e64, &9eb6
.data_tx_error
    lda tx_flags                                                      ; 9e9d: ad 4a 0d    .J.            ; Load saved next handler low byte
    bpl nmi_tx_not_listening                                          ; 9ea0: 10 03       ..             ; bit7 clear: error path
    jmp discard_reset_listen                                          ; 9ea2: 4c 4a 9a    LJ.            ; ADLC reset and return to idle

; &9ea5 referenced 1 time by &9ea0
.nmi_tx_not_listening
    lda #&41 ; 'A'                                                    ; 9ea5: a9 41       .A             ; A=&41: 'not listening' error
.jmp_tx_result_fail
    jmp tx_store_result                                               ; 9ea7: 4c 4e 9f    LN.            ; Store result and return to idle

; &9eaa referenced 1 time by &9e94
.install_saved_handler
    lda nmi_next_lo                                                   ; 9eaa: ad 4b 0d    .K.            ; Load saved handler low byte
    ldy nmi_next_hi                                                   ; 9ead: ac 4c 0d    .L.            ; Load saved next handler high byte
    jmp set_nmi_vector                                                ; 9eb0: 4c 0e 0d    L..            ; Install saved handler and return

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9eb3: 2c a0 fe    ,..            ; Tube TX: BIT SR1 test TDRA
; &9eb6 referenced 1 time by &9ee7
.tube_tx_fifo_write
    bvc data_tx_error                                                 ; 9eb6: 50 e5       P.             ; TDRA not ready -- error
    lda tube_data_register_3                                          ; 9eb8: ad e5 fe    ...            ; Read byte from Tube R3
    sta econet_data_continue_frame                                    ; 9ebb: 8d a2 fe    ...            ; Write to TX FIFO
    inc port_buf_len                                                  ; 9ebe: e6 a2       ..             ; Increment 4-byte buffer counter
    bne write_second_tube_byte                                        ; 9ec0: d0 0c       ..             ; Low byte didn't wrap
    inc port_buf_len_hi                                               ; 9ec2: e6 a3       ..             ; Carry into second byte
    bne write_second_tube_byte                                        ; 9ec4: d0 08       ..             ; No further carry
    inc open_port_buf                                                 ; 9ec6: e6 a4       ..             ; Carry into third byte
    bne write_second_tube_byte                                        ; 9ec8: d0 04       ..             ; No further carry
    inc open_port_buf_hi                                              ; 9eca: e6 a5       ..             ; Carry into fourth byte
    beq data_tx_last                                                  ; 9ecc: f0 be       ..             ; Counter wrapped to zero: last data
; &9ece referenced 3 times by &9ec0, &9ec4, &9ec8
.write_second_tube_byte
    lda tube_data_register_3                                          ; 9ece: ad e5 fe    ...            ; Read second Tube byte from R3
    sta econet_data_continue_frame                                    ; 9ed1: 8d a2 fe    ...            ; Write second byte to TX FIFO
    inc port_buf_len                                                  ; 9ed4: e6 a2       ..             ; Increment 4-byte counter (second byte)
    bne check_tube_irq_loop                                           ; 9ed6: d0 0c       ..             ; Low byte didn't wrap
.tube_tx_inc_byte2
tube_tx_byte2_operand = tube_tx_inc_byte2+1
    inc port_buf_len_hi                                               ; 9ed8: e6 a3       ..             ; Carry into second byte
; &9ed9 referenced 1 time by &9cd4
    bne check_tube_irq_loop                                           ; 9eda: d0 08       ..             ; No further carry
.tube_tx_inc_byte3
    inc open_port_buf                                                 ; 9edc: e6 a4       ..             ; Carry into third byte
    bne check_tube_irq_loop                                           ; 9ede: d0 04       ..             ; No further carry
.tube_tx_inc_byte4
tube_tx_byte4_operand = tube_tx_inc_byte4+1
    inc open_port_buf_hi                                              ; 9ee0: e6 a5       ..             ; Carry into fourth byte
; &9ee1 referenced 1 time by &9cce
    beq data_tx_last                                                  ; 9ee2: f0 a8       ..             ; Counter wrapped to zero: last data
; &9ee4 referenced 3 times by &9ed6, &9eda, &9ede
.check_tube_irq_loop
    bit econet_control1_or_status1                                    ; 9ee4: 2c a0 fe    ,..            ; BIT SR1: test IRQ for tight loop
    bmi tube_tx_fifo_write                                            ; 9ee7: 30 cd       0.             ; IRQ still set: write 2 more bytes
    jmp nmi_rti                                                       ; 9ee9: 4c 14 0d    L..            ; No IRQ: return, wait for next NMI

; ***************************************************************************************
; Four-way handshake: switch to RX for final ACK
; 
; After the data frame TX completes, switches to RX mode (CR1=&82)
; and installs &9EE9 to receive the final ACK from the remote station.
; ***************************************************************************************
; &9eec referenced 1 time by &9db7
.handshake_await_ack
    lda #&82                                                          ; 9eec: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9eee: 8d a0 fe    ...            ; Write to ADLC CR1
    lda #&f8                                                          ; 9ef1: a9 f8       ..             ; Install nmi_final_ack at &9E5C
    ldy #&9e                                                          ; 9ef3: a0 9e       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9ef5: 4c 0e 0d    L..            ; Install and return via set_nmi_vector

; ***************************************************************************************
; RX final ACK handler
; 
; Receives the final ACK in a four-way handshake. Same validation
; pattern as the reply scout handler (&9DC1-&9DF2):
;   &9EF8: Check AP, read dest_stn, compare to our station
;   &9F0E: Check RDA, read dest_net, validate = 0
;   &9F24: Check RDA, read src_stn/net, compare to TX dest
;   &9F41: Check FV for frame completion
; On success, stores result=0 at &9F48. On any failure, error &41.
; ***************************************************************************************
.nmi_final_ack
    lda #1                                                            ; 9ef8: a9 01       ..             ; A=&01: AP mask
    bit econet_control23_or_status2                                   ; 9efa: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 9efd: f0 4d       .M             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9eff: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 9f02: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 9f05: d0 45       .E             ; Not our station -- error
    lda #&0e                                                          ; 9f07: a9 0e       ..             ; Install nmi_final_ack_net at &9E70
    ldy #&9f                                                          ; 9f09: a0 9f       ..             ; High byte of handler address
    jmp set_nmi_vector                                                ; 9f0b: 4c 0e 0d    L..            ; Install continuation handler

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9f0e: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f11: 10 39       .9             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f13: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9f16: d0 34       .4             ; Non-zero -- network mismatch, error
    lda #&24 ; '$'                                                    ; 9f18: a9 24       .$             ; Install nmi_final_ack_validate at &9E84
    ldy #&9f                                                          ; 9f1a: a0 9f       ..             ; High byte of handler address
    bit econet_control1_or_status1                                    ; 9f1c: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9f1f: 30 03       0.             ; IRQ set -- fall through to &9E84 without RTI
    jmp set_nmi_vector                                                ; 9f21: 4c 0e 0d    L..            ; Install handler and RTI

; ***************************************************************************************
; Final ACK validation
; 
; Reads and validates src_stn and src_net against original TX dest.
; Then checks FV for frame completion.
; ***************************************************************************************
; &9f24 referenced 1 time by &9f1f
.nmi_final_ack_validate
    bit econet_control23_or_status2                                   ; 9f24: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f27: 10 23       .#             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f29: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9f2c: cd 20 0d    . .            ; Compare to TX dest station (&0D20)
    bne tx_result_fail                                                ; 9f2f: d0 1b       ..             ; Mismatch -- error
    lda econet_data_continue_frame                                    ; 9f31: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9f34: cd 21 0d    .!.            ; Compare to TX dest network (&0D21)
    bne tx_result_fail                                                ; 9f37: d0 13       ..             ; Mismatch -- error
    lda tx_flags                                                      ; 9f39: ad 4a 0d    .J.            ; Load TX flags for next action
    bpl check_fv_final_ack                                            ; 9f3c: 10 03       ..             ; bit7 clear: no data phase
    jmp install_data_rx_handler                                       ; 9f3e: 4c 7a 98    Lz.            ; Install data RX handler

; &9f41 referenced 1 time by &9f3c
.check_fv_final_ack
    lda #2                                                            ; 9f41: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9f43: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 9f46: f0 04       ..             ; No FV -- error
; ***************************************************************************************
; TX completion handler
; 
; Stores result code 0 (success) into the first byte of the TX control
; block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
; and calls full ADLC reset + idle listen via &9A34.
; ***************************************************************************************
; &9f48 referenced 2 times by &996d, &9dad
.tx_result_ok
    lda #0                                                            ; 9f48: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 9f4a: f0 02       ..             ; BEQ: always taken (A=0); ALWAYS branch

; ***************************************************************************************
; TX failure: not listening
; 
; Loads error code &41 (not listening) and falls through to
; tx_store_result. The most common TX error path — reached from
; 11 sites across the final-ACK validation chain when the remote
; station doesn't respond or the frame is malformed.
; ***************************************************************************************
; &9f4c referenced 8 times by &9efd, &9f05, &9f11, &9f16, &9f27, &9f2f, &9f37, &9f46
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9f4c: a9 41       .A             ; A=&41: not listening error code
; ***************************************************************************************
; TX error handler
; 
; Stores error code (A) into the TX control block, sets &0D3A bit7
; for completion, and returns to idle via &9A34.
; Error codes: &00=success, &40=line jammed, &41=not listening,
; &42=net error.
; ***************************************************************************************
; &9f4e referenced 5 times by &989b, &9d94, &9def, &9ea7, &9f4a
.tx_store_result
    ldy #0                                                            ; 9f4e: a0 00       ..             ; Y=0: index into TX control block
    sta (nmi_tx_block),y                                              ; 9f50: 91 a0       ..             ; Store result/error code at (nmi_tx_block),0
    lda #&80                                                          ; 9f52: a9 80       ..             ; &80: completion flag for &0D3A
    sta tx_clear_flag                                                 ; 9f54: 8d 62 0d    .b.            ; Signal TX complete
    jmp discard_reset_listen                                          ; 9f57: 4c 4a 9a    LJ.            ; Full ADLC reset and return to idle listen

; Unreferenced data block (purpose unknown)
    equb &0e, &0e, &0a, &0a, &0a, 6, 6, &0a, &81, 0, 0, 0, 0, 1, 1    ; 9f5a: 0e 0e 0a... ...
    equb &81                                                          ; 9f69: 81          .

; ***************************************************************************************
; Calculate transfer size
; 
; Computes the number of bytes actually transferred during a data
; frame reception. Subtracts the low pointer (LPTR, offset 4 in
; the RXCB) from the current buffer position to get the byte count,
; and stores it back into the RXCB's high pointer field (HPTR,
; offset 8). This tells the caller how much data was received.
; ***************************************************************************************
; &9f6a referenced 5 times by &9818, &9b04, &9d14, &9d1f, &9d51
.tx_calc_transfer
    ldy #6                                                            ; 9f6a: a0 06       ..             ; Load RXCB[6] (buffer addr byte 2)
    lda (nmi_tx_block),y                                              ; 9f6c: b1 a0       ..             ; Load TX block byte at offset 6
    iny                                                               ; 9f6e: c8          .              ; Y=&07
    and (nmi_tx_block),y                                              ; 9f6f: 31 a0       1.             ; AND with TX block[7] (byte 3)
    cmp #&ff                                                          ; 9f71: c9 ff       ..             ; Both &FF = no buffer?
    beq fallback_calc_transfer                                        ; 9f73: f0 41       .A             ; Yes: fallback path
    lda tx_in_progress                                                ; 9f75: ad 52 0d    .R.            ; Tube transfer in progress?
    beq fallback_calc_transfer                                        ; 9f78: f0 3c       .<             ; No: fallback path
    lda tx_flags                                                      ; 9f7a: ad 4a 0d    .J.            ; Load TX flags for transfer setup
    ora #2                                                            ; 9f7d: 09 02       ..             ; Set bit 1 (transfer complete)
    sta tx_flags                                                      ; 9f7f: 8d 4a 0d    .J.            ; Store with bit 1 set (Tube xfer)
    sec                                                               ; 9f82: 38          8              ; Init borrow for 4-byte subtract
    php                                                               ; 9f83: 08          .              ; Save carry on stack
    ldy #4                                                            ; 9f84: a0 04       ..             ; Y=4: start at RXCB offset 4
; &9f86 referenced 1 time by &9f98
.calc_transfer_size
    lda (nmi_tx_block),y                                              ; 9f86: b1 a0       ..             ; Load RXCB[Y] (current ptr byte)
    iny                                                               ; 9f88: c8          .              ; Y += 4: advance to RXCB[Y+4]
    iny                                                               ; 9f89: c8          .              ; Y += 4: advance to high ptr offset
    iny                                                               ; 9f8a: c8          .              ; (continued)
    iny                                                               ; 9f8b: c8          .              ; (continued)
    plp                                                               ; 9f8c: 28          (              ; Restore borrow from previous byte
    sbc (nmi_tx_block),y                                              ; 9f8d: f1 a0       ..             ; Subtract RXCB[Y+4] (start ptr byte)
    sta net_tx_ptr,y                                                  ; 9f8f: 99 9a 00    ...            ; Store result byte
    dey                                                               ; 9f92: 88          .              ; Y -= 3: next source byte
    dey                                                               ; 9f93: 88          .              ; Y -= 3: back to next low ptr byte
    dey                                                               ; 9f94: 88          .              ; (continued)
    php                                                               ; 9f95: 08          .              ; Save borrow for next byte
    cpy #8                                                            ; 9f96: c0 08       ..             ; Done all 4 bytes?
    bcc calc_transfer_size                                            ; 9f98: 90 ec       ..             ; No: next byte pair
    plp                                                               ; 9f9a: 28          (              ; Discard final borrow
    txa                                                               ; 9f9b: 8a          .              ; A = saved X
    pha                                                               ; 9f9c: 48          H              ; Save X
    lda #4                                                            ; 9f9d: a9 04       ..             ; Compute address of RXCB+4
    clc                                                               ; 9f9f: 18          .              ; CLC for base pointer addition
    adc nmi_tx_block                                                  ; 9fa0: 65 a0       e.             ; Add RXCB base to get RXCB+4 addr
    tax                                                               ; 9fa2: aa          .              ; X = low byte of RXCB+4
    ldy nmi_tx_block_hi                                               ; 9fa3: a4 a1       ..             ; Y = high byte of RXCB ptr
    lda #&c2                                                          ; 9fa5: a9 c2       ..             ; Tube claim type &C2
    jsr tube_addr_claim                                               ; 9fa7: 20 06 04     ..            ; Claim Tube transfer address
    bcc restore_x_and_return                                          ; 9faa: 90 07       ..             ; No Tube: skip reclaim
    lda scout_status                                                  ; 9fac: ad 5c 0d    .\.            ; Tube: reclaim with scout status
    jsr tube_addr_claim                                               ; 9faf: 20 06 04     ..            ; Reclaim with scout status type
    sec                                                               ; 9fb2: 38          8              ; C=1: Tube address claimed
; &9fb3 referenced 1 time by &9faa
.restore_x_and_return
    pla                                                               ; 9fb3: 68          h              ; Restore X
    tax                                                               ; 9fb4: aa          .              ; Restore X from stack
    rts                                                               ; 9fb5: 60          `              ; Return with C = transfer status

; &9fb6 referenced 2 times by &9f73, &9f78
.fallback_calc_transfer
    ldy #4                                                            ; 9fb6: a0 04       ..             ; Y=4: RXCB current pointer offset
    lda (nmi_tx_block),y                                              ; 9fb8: b1 a0       ..             ; Load RXCB[4] (current ptr lo)
    ldy #8                                                            ; 9fba: a0 08       ..             ; Y=8: RXCB start address offset
    sec                                                               ; 9fbc: 38          8              ; Set carry for subtraction
    sbc (nmi_tx_block),y                                              ; 9fbd: f1 a0       ..             ; Subtract RXCB[8] (start ptr lo)
    sta port_buf_len                                                  ; 9fbf: 85 a2       ..             ; Store transfer size lo
    ldy #5                                                            ; 9fc1: a0 05       ..             ; Y=5: current ptr hi offset
    lda (nmi_tx_block),y                                              ; 9fc3: b1 a0       ..             ; Load RXCB[5] (current ptr hi)
    sbc #0                                                            ; 9fc5: e9 00       ..             ; Propagate borrow from lo subtraction
    sta open_port_buf_hi                                              ; 9fc7: 85 a5       ..             ; Temp store adjusted current ptr hi
    ldy #8                                                            ; 9fc9: a0 08       ..             ; Y=8: start address lo offset
    lda (nmi_tx_block),y                                              ; 9fcb: b1 a0       ..             ; Copy RXCB[8] to open port buffer lo
    sta open_port_buf                                                 ; 9fcd: 85 a4       ..             ; Store to scratch (side effect)
    ldy #9                                                            ; 9fcf: a0 09       ..             ; Y=9: start address hi offset
    lda (nmi_tx_block),y                                              ; 9fd1: b1 a0       ..             ; Load RXCB[9] (start ptr hi)
    sec                                                               ; 9fd3: 38          8              ; Set carry for subtraction
    sbc open_port_buf_hi                                              ; 9fd4: e5 a5       ..             ; start_hi - adjusted current_hi
    sta port_buf_len_hi                                               ; 9fd6: 85 a3       ..             ; Store transfer size hi
    sec                                                               ; 9fd8: 38          8              ; Return with C=1
; &9fd9 referenced 1 time by &968c
.nmi_shim_rom_src
    rts                                                               ; 9fd9: 60          `              ; Return with C=1 (success)

; ***************************************************************************************
; Bootstrap NMI entry point (in ROM)
; 
; An alternate NMI handler that lives in the ROM itself rather than
; in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
; self-modifying JMP to dispatch to different handlers), this one
; hardcodes JMP nmi_rx_scout (&9700). Used as the initial NMI handler
; before the workspace has been properly set up during initialisation.
; Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
; LDA romsel, STA &FE30, JMP &9700.
; ***************************************************************************************
.nmi_bootstrap_entry
    bit station_id_disable_net_nmis                                   ; 9fda: 2c 18 fe    ,..            ; INTOFF: disable NMIs while switching ROM
    pha                                                               ; 9fdd: 48          H              ; Save A
    tya                                                               ; 9fde: 98          .              ; Transfer Y to A
    pha                                                               ; 9fdf: 48          H              ; Save Y (via A)
    lda #0                                                            ; 9fe0: a9 00       ..             ; ROM bank 0 (patched during init for actual bank)
    sta romsel                                                        ; 9fe2: 8d 30 fe    .0.            ; Select Econet ROM bank via ROMSEL
    jmp nmi_rx_scout                                                  ; 9fe5: 4c 00 97    L..            ; Jump to scout handler in ROM

; ***************************************************************************************
; ROM copy of set_nmi_vector + nmi_rti
; 
; A version of the NMI vector-setting subroutine and RTI sequence
; that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the
; one normally used at runtime; this ROM copy is used during early
; initialisation before the RAM workspace has been set up, and as
; the source for the initial copy to RAM.
; ***************************************************************************************
.rom_set_nmi_vector
    sty nmi_jmp_hi                                                    ; 9fe8: 8c 0d 0d    ...            ; Store handler high byte at &0D0D
    sta nmi_jmp_lo                                                    ; 9feb: 8d 0c 0d    ...            ; Store handler low byte at &0D0C
    lda romsel_copy                                                   ; 9fee: a5 f4       ..             ; Restore NFS ROM bank
    sta romsel                                                        ; 9ff0: 8d 30 fe    .0.            ; Page in via hardware latch
    pla                                                               ; 9ff3: 68          h              ; Restore Y from stack
    tay                                                               ; 9ff4: a8          .              ; Transfer ROM bank to Y
    pla                                                               ; 9ff5: 68          h              ; Restore A from stack
    bit video_ula_control                                             ; 9ff6: 2c 20 fe    , .            ; INTON: re-enable NMIs
    rti                                                               ; 9ff9: 40          @              ; Return from interrupt

.rom_nmi_tail
    equb &ad, &4a, &0d, 9, 2, &8d                                     ; 9ffa: ad 4a 0d... .J.            ; Load current TX flags; Set bit 1 (transfer mode flag); Store updated TX flags
.pydis_end

    assert <(dispatch_net_cmd-1) == &68
    assert <(econet_tx_rx-1) == &ec
    assert <(fscv_0_opt-1) == &cb
    assert <(fscv_1_eof-1) == &50
    assert <(fscv_2_star_run-1) == &c6
    assert <(fscv_3_star_cmd-1) == &b3
    assert <(fscv_5_cat-1) == &ff
    assert <(fscv_6_shutdown-1) == &40
    assert <(fscv_7_read_handles-1) == &55
    assert <(fsreply_0_print_dir-1) == &5e
    assert <(fsreply_1_copy_handles_boot-1) == &27
    assert <(fsreply_2_copy_handles-1) == &28
    assert <(fsreply_3_set_csd-1) == &21
    assert <(fsreply_4_notify_exec-1) == &cc
    assert <(fsreply_5_set_lib-1) == &1c
    assert <(imm_op_status3-1) == &f2
    assert <(l0128) == &28
    assert <(lang_0_insert_remote_key-1) == &c4
    assert <(lang_1_remote_boot-1) == &76
    assert <(lang_2_save_palette_vdu-1) == &a3
    assert <(lang_3_execute_at_0100-1) == &a4
    assert <(lang_4_remote_validated-1) == &b4
    assert <(net_1_read_handle-1) == &42
    assert <(net_2_read_handle_entry-1) == &5d
    assert <(net_3_close_handle-1) == &6d
    assert <(net_4_resume_remote-1) == &89
    assert <(nwrch_handler-1) == &b1
    assert <(osword_0f_handler-1) == &bf
    assert <(osword_10_handler-1) == &6d
    assert <(osword_11_handler-1) == &d9
    assert <(osword_12_dispatch-1) == &fe
    assert <(printer_select_handler-1) == &c8
    assert <(remote_cmd_data-1) == &41
    assert <(remote_cmd_dispatch-1) == &d7
    assert <(remote_print_handler-1) == &d8
    assert <(return_2-1) == &75
    assert <(rx_imm_exec-1) == &b4
    assert <(rx_imm_halt_cont-1) == &16
    assert <(rx_imm_machine_type-1) == &dd
    assert <(rx_imm_peek-1) == &f0
    assert <(rx_imm_poke-1) == &d2
    assert <(svc_11_nmi_claim-1) == &68
    assert <(svc_12_nmi_release-1) == &65
    assert <(svc_1_abs_workspace-1) == &ab
    assert <(svc_2_private_workspace-1) == &b4
    assert <(svc_3_autoboot-1) == &0c
    assert <(svc_4_star_command-1) == &82
    assert <(svc_5_unknown_irq-1) == &6b
    assert <(svc_8_osword-1) == &7d
    assert <(svc_9_help-1) == &f6
    assert <(tx_ctrl_exit-1) == &53
    assert <(tx_ctrl_peek-1) == &f6
    assert <(tx_ctrl_poke-1) == &fa
    assert <(tx_ctrl_proc-1) == &19
    assert <(tx_done_continue-1) == &e3
    assert <(tx_done_halt-1) == &cc
    assert <(tx_done_jsr-1) == &a9
    assert <(tx_done_os_proc-1) == &c0
    assert <(tx_done_user_proc-1) == &b2
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(fscv_0_opt-1) == &89
    assert >(fscv_1_eof-1) == &88
    assert >(fscv_2_star_run-1) == &8d
    assert >(fscv_3_star_cmd-1) == &8b
    assert >(fscv_5_cat-1) == &8b
    assert >(fscv_6_shutdown-1) == &83
    assert >(fscv_7_read_handles-1) == &86
    assert >(fsreply_0_print_dir-1) == &8d
    assert >(fsreply_1_copy_handles_boot-1) == &8e
    assert >(fsreply_2_copy_handles-1) == &8e
    assert >(fsreply_3_set_csd-1) == &8e
    assert >(fsreply_4_notify_exec-1) == &8d
    assert >(fsreply_5_set_lib-1) == &8e
    assert >(imm_op_status3-1) == &9c
    assert >(l0128) == &01
    assert >(lang_0_insert_remote_key-1) == &84
    assert >(lang_1_remote_boot-1) == &84
    assert >(lang_2_save_palette_vdu-1) == &92
    assert >(lang_3_execute_at_0100-1) == &84
    assert >(lang_4_remote_validated-1) == &84
    assert >(net_1_read_handle-1) == &8e
    assert >(net_2_read_handle_entry-1) == &8e
    assert >(net_3_close_handle-1) == &8e
    assert >(net_4_resume_remote-1) == &81
    assert >(nwrch_handler-1) == &90
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8f
    assert >(osword_11_handler-1) == &8e
    assert >(osword_12_dispatch-1) == &8e
    assert >(printer_select_handler-1) == &91
    assert >(remote_cmd_data-1) == &91
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_print_handler-1) == &91
    assert >(return_2-1) == &81
    assert >(rx_imm_exec-1) == &9a
    assert >(rx_imm_halt_cont-1) == &9b
    assert >(rx_imm_machine_type-1) == &9a
    assert >(rx_imm_peek-1) == &9a
    assert >(rx_imm_poke-1) == &9a
    assert >(svc_11_nmi_claim-1) == &96
    assert >(svc_12_nmi_release-1) == &96
    assert >(svc_1_abs_workspace-1) == &82
    assert >(svc_2_private_workspace-1) == &82
    assert >(svc_3_autoboot-1) == &82
    assert >(svc_4_star_command-1) == &81
    assert >(svc_5_unknown_irq-1) == &96
    assert >(svc_8_osword-1) == &8e
    assert >(svc_9_help-1) == &81
    assert >(tx_ctrl_exit-1) == &9d
    assert >(tx_ctrl_peek-1) == &9c
    assert >(tx_ctrl_poke-1) == &9c
    assert >(tx_ctrl_proc-1) == &9d
    assert >(tx_done_continue-1) == &9b
    assert >(tx_done_halt-1) == &9b
    assert >(tx_done_jsr-1) == &9b
    assert >(tx_done_os_proc-1) == &9b
    assert >(tx_done_user_proc-1) == &9b
    assert copyright - rom_header == &0c
    assert tube_osargs == &058c
    assert tube_osbget == &0550
    assert tube_osbput == &0543
    assert tube_osbyte_long == &0638
    assert tube_osbyte_short == &0623
    assert tube_oscli == &05c5
    assert tube_osfile == &05d8
    assert tube_osfind == &0569
    assert tube_osgbpb == &0602
    assert tube_osrdch == &055b
    assert tube_osword == &065a
    assert tube_osword_rdln == &06a0
    assert tube_release_return == &053d
    assert tube_restore_regs == &04ef

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           53
;     econet_control23_or_status2:             45
;     fs_options:                              43
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             35
;     net_rx_ptr:                              34
;     econet_control1_or_status1:              31
;     nmi_tx_block:                            29
;     osword_pb_ptr:                           27
;     tx_flags:                                26
;     net_tx_ptr:                              24
;     port_ws_offset:                          24
;     osbyte:                                  23
;     set_nmi_vector:                          22
;     tube_read_r2:                            22
;     port_buf_len:                            20
;     tube_send_r2:                            17
;     open_port_buf_hi:                        16
;     rx_flags:                                16
;     fs_func_code:                            15
;     fs_load_addr_2:                          15
;     station_id_disable_net_nmis:             15
;     nfs_temp:                                14
;     open_port_buf:                           14
;     print_inline:                            14
;     fs_load_addr:                            13
;     port_buf_len_hi:                         13
;     ws_ptr_lo:                               13
;     nmi_error_dispatch:                      12
;     prepare_fs_cmd:                          12
;     tube_data_register_2:                    12
;     fs_error_ptr:                            11
;     tube_status_register_2:                  11
;     nfs_workspace_hi:                        10
;     rom_svc_num:                             10
;     tube_addr_claim:                         10
;     nmi_tx_block_hi:                          9
;     rx_src_stn:                               9
;     tube_data_register_3:                     9
;     txcb_end:                                 9
;     fs_work_4:                                8
;     table_idx:                                8
;     tube_status_1_and_tube_control:           8
;     tx_result_fail:                           8
;     txcb_start:                               8
;     zp_ptr_lo:                                8
;     fs_cmd_csd:                               7
;     fs_cmd_urd:                               7
;     fs_crc_lo:                                7
;     l0d60:                                    7
;     prot_status:                              7
;     reply_error:                              7
;     restore_args_return:                      7
;     return_1:                                 7
;     tx_clear_flag:                            7
;     tx_dst_stn:                               7
;     copy_string_to_cmd:                       6
;     fs_block_offset:                          6
;     fs_last_byte_flag:                        6
;     fs_load_addr_hi:                          6
;     net_rx_ptr_hi:                            6
;     net_tx_ptr_hi:                            6
;     nmi_rti:                                  6
;     os_text_ptr:                              6
;     osasci:                                   6
;     rx_buf_offset:                            6
;     scout_status:                             6
;     tube_main_loop:                           6
;     tx_in_progress:                           6
;     zp_temp_10:                               6
;     copy_param_block:                         5
;     dispatch:                                 5
;     fs_boot_option:                           5
;     fs_data_count:                            5
;     fs_load_addr_3:                           5
;     l0100:                                    5
;     l0106:                                    5
;     printer_buf_ptr:                          5
;     restore_xy_return:                        5
;     rx_ctrl:                                  5
;     rx_port:                                  5
;     scout_error:                              5
;     set_fs_flag:                              5
;     system_via_acr:                           5
;     tube_reply_byte:                          5
;     tube_send_r1:                             5
;     tube_send_r4:                             5
;     tx_calc_transfer:                         5
;     tx_dst_net:                               5
;     tx_store_result:                          5
;     zp_ptr_hi:                                5
;     zp_temp_11:                               5
;     clear_jsr_protection:                     4
;     copy_filename:                            4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     fs_cmd_context:                           4
;     fs_crflag:                                4
;     fs_eof_flags:                             4
;     fs_sequence_nos:                          4
;     fs_server_net:                            4
;     fs_work_7:                                4
;     init_tx_ctrl_block:                       4
;     l0101:                                    4
;     l0d58:                                    4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     osbyte_a_copy:                            4
;     osrdsc_ptr:                               4
;     restore_ay_return:                        4
;     return_2:                                 4
;     return_a_zero:                            4
;     rx_src_net:                               4
;     tube_claimed_id:                          4
;     tx_done_exit:                             4
;     tx_length:                                4
;     tx_poll_ff:                               4
;     txcb_ctrl:                                4
;     txcb_port:                                4
;     video_ula_control:                        4
;     ws_ptr_hi:                                4
;     addr_work:                                3
;     adlc_full_reset:                          3
;     calc_handle_offset:                       3
;     check_tube_irq_loop:                      3
;     clear_fs_flag:                            3
;     data_rx_complete:                         3
;     data_rx_tube_error:                       3
;     discard_listen:                           3
;     dispatch_remote_osbyte:                   3
;     econet_init_flag:                         3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_messages_flag:                         3
;     fs_reply_cmd:                             3
;     fs_reply_poll:                            3
;     fs_server_stn:                            3
;     fs_spool0:                                3
;     fs_spool_handle:                          3
;     fs_urd_handle:                            3
;     fs_work_5:                                3
;     handle_to_mask_a:                         3
;     imm_op_dispatch:                          3
;     match_osbyte_code:                        3
;     next_port_slot:                           3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     openl4:                                   3
;     oscli:                                    3
;     osword:                                   3
;     osword_flag:                              3
;     pad_filename_spaces:                      3
;     print_dir_from_offset:                    3
;     print_reply_bytes:                        3
;     romsel_copy:                              3
;     rx_check_error:                           3
;     rx_update_buf:                            3
;     save_fscv_args:                           3
;     save_fscv_args_with_ptrs:                 3
;     saved_jsr_mask:                           3
;     scout_no_match:                           3
;     send_to_fs_star:                          3
;     setup_tx_and_send:                        3
;     skip_buf_ptr_update:                      3
;     test_inactive_retry:                      3
;     tube_claim_flag:                          3
;     tube_claim_loop:                          3
;     tube_data_register_1:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tx_ctrl_exit:                             3
;     tx_ctrl_upper:                            3
;     tx_index:                                 3
;     write_second_tube_byte:                   3
;     ack_scout_match:                          2
;     ack_tx:                                   2
;     ack_tx_write_dest:                        2
;     adjust_addrs:                             2
;     adlc_rx_listen:                           2
;     advance_rx_buffer_ptr:                    2
;     beginr:                                   2
;     binary_version:                           2
;     boot_option_strings:                      2
;     brk_ptr:                                  2
;     call_fscv_shutdown:                       2
;     cb_template_main_start:                   2
;     cbset2:                                   2
;     check_escape:                             2
;     cmd_name_matched:                         2
;     compare_addresses:                        2
;     copy_filename_to_cmd:                     2
;     copy_load_addr_from_params:               2
;     copy_reply_to_caller:                     2
;     copy_reply_to_params:                     2
;     ctrl_block_setup_alt:                     2
;     data_rx_tube_complete:                    2
;     decode_attribs_5bit:                      2
;     decode_attribs_6bit:                      2
;     econet_tx_retry:                          2
;     escape_flag:                              2
;     exec_at_load_addr:                        2
;     execute_downloaded:                       2
;     fallback_calc_transfer:                   2
;     flush_output_block:                       2
;     fs_access_level:                          2
;     fs_cmd_match_table:                       2
;     fs_cmd_y_param:                           2
;     fs_crc_hi:                                2
;     fs_error_flags:                           2
;     fs_file_len_3:                            2
;     fs_filename_buf:                          2
;     fs_handle_mask:                           2
;     fs_last_error:                            2
;     fs_lib_handle:                            2
;     fs_load_vector:                           2
;     fs_obj_type:                              2
;     fs_putb_buf:                              2
;     fs_state_deb:                             2
;     gbpb_done:                                2
;     gsinit:                                   2
;     gsread:                                   2
;     handle_mask_exit:                         2
;     handle_to_mask_clc:                       2
;     imm_op_discard:                           2
;     imm_op_out_of_range:                      2
;     init_tx_ctrl_data:                        2
;     install_rx_scout_handler:                 2
;     jmp_restore_args:                         2
;     l0102:                                    2
;     l0103:                                    2
;     l0128:                                    2
;     l0700:                                    2
;     l0d1e:                                    2
;     l0d59:                                    2
;     language_entry:                           2
;     load_handle_calc_offset:                  2
;     logon3:                                   2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     msdely:                                   2
;     next_filename_char:                       2
;     nlisne:                                   2
;     nmi_vec_lo_match:                         2
;     no_dot_exit:                              2
;     num01:                                    2
;     nvwrch:                                   2
;     os_text_ptr_hi:                           2
;     osarg1:                                   2
;     osfind:                                   2
;     osnewl:                                   2
;     osword_pb_ptr_hi:                         2
;     parse_decimal:                            2
;     parse_filename_gs:                        2
;     poll_r2_reply:                            2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_char_always:                        2
;     print_cr_separator:                       2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_file_info:                          2
;     print_hex:                                2
;     print_hex_bytes:                          2
;     print_reply_counted:                      2
;     prlp1:                                    2
;     pydis_start:                              2
;     read_station_id:                          2
;     readc1:                                   2
;     reenable_rx:                              2
;     remot1:                                   2
;     restore_y_return:                         2
;     return_3:                                 2
;     return_4:                                 2
;     return_5:                                 2
;     return_7:                                 2
;     return_copy_param:                        2
;     return_match_osbyte:                      2
;     return_nbyte:                             2
;     return_printer_select:                    2
;     return_tube_init:                         2
;     return_tube_xfer:                         2
;     rom_header:                               2
;     romsel:                                   2
;     run_fscv_cmd:                             2
;     rx_extra_byte:                            2
;     rxpol2:                                   2
;     scan_for_colon:                           2
;     scout_complete:                           2
;     send_ack:                                 2
;     send_data_blocks:                         2
;     send_data_rx_ack:                         2
;     send_fs_reply_timed:                      2
;     send_reply_ok:                            2
;     send_rom_byte:                            2
;     send_to_fs:                               2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     store_tube_flag:                          2
;     store_tx_error:                           2
;     sub_3_from_y:                             2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     tdra_error:                               2
;     terminate_filename:                       2
;     trampoline_tx_setup:                      2
;     transfer_file_blocks:                     2
;     tube_data_ptr:                            2
;     tube_dispatch_table:                      2
;     tube_enter_main_loop:                     2
;     tube_osbyte_send_x:                       2
;     tube_osword_read_lp:                      2
;     tube_status_register_4_and_cpu_control:   2
;     tube_transfer_addr:                       2
;     tube_xfer_page:                           2
;     tx_active_start:                          2
;     tx_ctrl_byte:                             2
;     tx_not_listening:                         2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
;     tx_work_51:                               2
;     tx_work_57:                               2
;     zp_work_3:                                2
;     accept_frame:                             1
;     accept_local_net:                         1
;     accept_new_claim:                         1
;     accept_scout_net:                         1
;     access_bit_table:                         1
;     ack_tx_configure:                         1
;     add_4_to_y:                               1
;     add_5_to_y:                               1
;     add_buf_to_base:                          1
;     add_bytes_loop:                           1
;     add_rxcb_ptr:                             1
;     addr_claim_external:                      1
;     adjust_addr_byte:                         1
;     adjust_addrs_1:                           1
;     adjust_addrs_9:                           1
;     adjust_addrs_clc:                         1
;     adlc_init:                                1
;     argsv_check_return:                       1
;     argsv_dispatch_a:                         1
;     argsw:                                    1
;     attrib_error_exit:                        1
;     attrib_shift_bits:                        1
;     begink:                                   1
;     bgetv_shared_jsr:                         1
;     block_addr_loop:                          1
;     boot_option_offsets:                      1
;     bspsx:                                    1
;     bsxl0:                                    1
;     bsxl1:                                    1
;     build_send_fs_cmd:                        1
;     bytex:                                    1
;     c955f:                                    1
;     calc_peek_poke_size:                      1
;     calc_transfer_size:                       1
;     cat_examine_loop:                         1
;     cat_print_header:                         1
;     cb_template_tail:                         1
;     cbset3:                                   1
;     cbset4:                                   1
;     cha4:                                     1
;     cha5:                                     1
;     cha5lp:                                   1
;     cha6:                                     1
;     chalp1:                                   1
;     chalp2:                                   1
;     check_attrib_result:                      1
;     check_fs_error:                           1
;     check_fv_final_ack:                       1
;     check_handshake_bit:                      1
;     check_imm_range:                          1
;     check_irq_loop:                           1
;     check_opt1:                               1
;     check_port_slot:                          1
;     check_sr2_loop_again:                     1
;     check_sr_irq:                             1
;     check_station_filter:                     1
;     check_svc_12:                             1
;     check_svc_high:                           1
;     clamp_dest_addr:                          1
;     clamp_dest_setup:                         1
;     clear_osbyte_ce_cf:                       1
;     clear_osbyte_masks:                       1
;     cloop:                                    1
;     close_handle:                             1
;     close_opt_return:                         1
;     close_single_handle:                      1
;     close_spool_exec:                         1
;     cmd_table_entry_1:                        1
;     compare_addr_byte:                        1
;     copy_addr_loop:                           1
;     copy_attr_loop:                           1
;     copy_bcast_addr:                          1
;     copy_block_addrs:                         1
;     copy_dir_handles:                         1
;     copy_error_message:                       1
;     copy_error_to_brk:                        1
;     copy_filename_ptr:                        1
;     copy_fileptr_reply:                       1
;     copy_fileptr_to_cmd:                      1
;     copy_fs_addr:                             1
;     copy_fs_reply_to_cb:                      1
;     copy_handles_loop:                        1
;     copy_handles_to_ws:                       1
;     copy_imm_params:                          1
;     copy_load_end_addr:                       1
;     copy_nmi_shim:                            1
;     copy_nmi_workspace:                       1
;     copy_osword_params:                       1
;     copy_params_rword:                        1
;     copy_reply_bytes:                         1
;     copy_rxcb_to_param:                       1
;     copy_save_params:                         1
;     copy_scout_fields:                        1
;     copy_scout_loop:                          1
;     copy_string_from_offset:                  1
;     copyright_offset:                         1
;     ctrl_block_setup:                         1
;     ctrl_block_setup_clv:                     1
;     ctrl_block_template:                      1
;     data_rx_loop:                             1
;     data_tx_begin:                            1
;     data_tx_check_fifo:                       1
;     decfir:                                   1
;     decmin:                                   1
;     decmor:                                   1
;     delay_between_tx:                         1
;     delay_nmi_disable:                        1
;     direct_attr_copy:                         1
;     dispatch_0_hi-1:                          1
;     dispatch_0_lo-1:                          1
;     dispatch_cmd:                             1
;     dispatch_fs_error:                        1
;     dispatch_service:                         1
;     divide_subtract:                          1
;     dofs01:                                   1
;     dofs2:                                    1
;     dofsl5:                                   1
;     dofsl7:                                   1
;     done_option_name:                         1
;     econet_data_terminate_frame:              1
;     entry1:                                   1
;     error1:                                   1
;     error_code_clamped:                       1
;     error_msg_table:                          1
;     error_not_listening:                      1
;     error_offsets:                            1
;     file1:                                    1
;     filev:                                    1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     floop:                                    1
;     flush_r3_nmi_check:                       1
;     forward_star_cmd:                         1
;     fs2al1:                                   1
;     fs_addr_check:                            1
;     fs_boot_data:                             1
;     fs_cmd_lib:                               1
;     fs_cmd_ptr:                               1
;     fs_cmd_type:                              1
;     fs_context_base:                          1
;     fs_context_hi:                            1
;     fs_error_buf:                             1
;     fs_file_attrs:                            1
;     fs_file_len:                              1
;     fs_len_clear:                             1
;     fs_load_upper:                            1
;     fs_reply_data:                            1
;     fs_reply_stn:                             1
;     fs_vector_addrs:                          1
;     fs_wait_cleanup:                          1
;     fs_work_16:                               1
;     fscv:                                     1
;     fscv_3_star_cmd:                          1
;     fsdiel:                                   1
;     fstxl1:                                   1
;     fstxl2:                                   1
;     gbpb6_read_name:                          1
;     gbpb8_read_dir:                           1
;     gbpb_invalid_exit:                        1
;     gbpb_read_path:                           1
;     gbpb_write_path:                          1
;     gbpbe1:                                   1
;     gbpbf1:                                   1
;     gbpbf2:                                   1
;     gbpbf3:                                   1
;     gbpbl1:                                   1
;     gbpbl3:                                   1
;     gbpbx:                                    1
;     gbpbx0:                                   1
;     gbpbx1:                                   1
;     get_disc_title:                           1
;     get_file_protection:                      1
;     gsread_scan_loop:                         1
;     halt_spin_loop:                           1
;     halve_args_a:                             1
;     handle_bput_bget:                         1
;     handle_to_mask:                           1
;     handle_tx_result:                         1
;     handshake_await_ack:                      1
;     imm_op_build_reply:                       1
;     immediate_op:                             1
;     inactive_retry:                           1
;     info2:                                    1
;     infol2:                                   1
;     init_cat_params:                          1
;     init_fs_vectors:                          1
;     init_nmi_workspace:                       1
;     init_rxcb_entries:                        1
;     init_tx_ctrl_port:                        1
;     init_tx_reply_port:                       1
;     init_vector_copy_loop:                    1
;     init_vector_loop:                         1
;     init_vectors_and_copy:                    1
;     initl:                                    1
;     install_data_rx_handler:                  1
;     install_imm_data_nmi:                     1
;     install_reply_scout:                      1
;     install_saved_handler:                    1
;     install_tube_rx:                          1
;     intoff_test_inactive:                     1
;     issue_vectors_claimed:                    1
;     jmp_rx_listen:                            1
;     jump_via_addr:                            1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l0cff:                                    1
;     l0e11:                                    1
;     l18a5:                                    1
;     l212e:                                    1
;     l945f:                                    1
;     lang_entry_dispatch:                      1
;     lang_entry_hi:                            1
;     lang_entry_lo:                            1
;     language_handler:                         1
;     load_workspace_byte:                      1
;     loadop:                                   1
;     lodchk:                                   1
;     lodfil:                                   1
;     lodrl1:                                   1
;     lodrl2:                                   1
;     logon2:                                   1
;     map_attrib_bits:                          1
;     match_net_cmd:                            1
;     match_next_char:                          1
;     mj:                                       1
;     nbyte1:                                   1
;     nbyte4:                                   1
;     nbyte5:                                   1
;     nbyte6:                                   1
;     netv:                                     1
;     next_block:                               1
;     next_dir_entry:                           1
;     nlistn:                                   1
;     nmi_data_rx_bulk:                         1
;     nmi_data_rx_skip:                         1
;     nmi_final_ack_validate:                   1
;     nmi_reply_validate:                       1
;     nmi_rx_scout:                             1
;     nmi_shim_07:                              1
;     nmi_shim_1a:                              1
;     nmi_shim_rom_src:                         1
;     nmi_sub_table:                            1
;     nmi_tx_not_listening:                     1
;     nmi_workspace_start:                      1
;     no_page_wrap:                             1
;     not_svc_12_nfs:                           1
;     nvrdch:                                   1
;     openl6:                                   1
;     openl7:                                   1
;     opt_return:                               1
;     opter1:                                   1
;     optl1:                                    1
;     osargs:                                   1
;     osbget:                                   1
;     osbput:                                   1
;     osbyte_vdu_table:                         1
;     oseven:                                   1
;     osfile:                                   1
;     osgbpb:                                   1
;     osgbpb_info:                              1
;     osrdch:                                   1
;     osrdsc_ptr_hi:                            1
;     osword_0f_tbl_hi:                         1
;     osword_0f_tbl_lo:                         1
;     osword_12_offsets:                        1
;     osword_tbl_hi:                            1
;     osword_tbl_lo:                            1
;     osword_trampoline:                        1
;     oswrch:                                   1
;     parse_decimal_rts:                        1
;     parse_filename_gs_y:                      1
;     poll_r2_osword_result:                    1
;     poll_r3_ready:                            1
;     poll_r4_copro_ack:                        1
;     poll_rxcb_loop:                           1
;     poll_txcb_status:                         1
;     prepare_cmd_with_flag:                    1
;     pril1:                                    1
;     print_digit:                              1
;     print_exec_and_len:                       1
;     print_hex_fields:                         1
;     print_hex_nibble:                         1
;     print_inline_char:                        1
;     print_newline:                            1
;     print_next_char:                          1
;     print_option_char:                        1
;     print_public:                             1
;     print_space:                              1
;     print_station_info:                       1
;     quote1:                                   1
;     rchex:                                    1
;     read_args_size:                           1
;     read_fs_handle:                           1
;     read_gbpb_params:                         1
;     read_osargs_params:                       1
;     read_rdln_ctrl_block:                     1
;     read_remote_cmd_line:                     1
;     read_rxcb:                                1
;     read_second_rx_byte:                      1
;     read_sr2_between_pairs:                   1
;     read_vdu_osbyte:                          1
;     read_vdu_osbyte_x0:                       1
;     readry:                                   1
;     release_claim_restart:                    1
;     reloc_p4_src:                             1
;     reloc_zp_src:                             1
;     remote_osbyte_table:                      1
;     restore_econet_state:                     1
;     restore_x_and_return:                     1
;     restore_y_check_svc:                      1
;     return_6:                                 1
;     return_8:                                 1
;     return_bspsx:                             1
;     return_calc_handle:                       1
;     return_compare:                           1
;     return_dofsl7:                            1
;     return_last_error:                        1
;     return_lodchk:                            1
;     rom_type:                                 1
;     rom_ws_table:                             1
;     rotate_prot_mask:                         1
;     rsl1:                                     1
;     rssl1:                                    1
;     rssl2:                                    1
;     rx_error:                                 1
;     rx_error_reset:                           1
;     rx_port_operand:                          1
;     rx_remote_addr:                           1
;     rx_tube_data:                             1
;     rxcb_matched:                             1
;     savchk:                                   1
;     save1:                                    1
;     save_args_handle:                         1
;     save_palette_entry:                       1
;     save_vdu_state:                           1
;     saveop:                                   1
;     savsiz:                                   1
;     scan0:                                    1
;     scan1:                                    1
;     scan_cmd_table:                           1
;     scan_copyright_end:                       1
;     scan_decimal_digit:                       1
;     scan_port_list:                           1
;     scout_accept:                             1
;     scout_ctrl_check:                         1
;     scout_discard:                            1
;     scout_loop_rda:                           1
;     scout_loop_second:                        1
;     scout_match_port:                         1
;     scout_network_match:                      1
;     scout_port_match:                         1
;     scout_reject:                             1
;     scout_station_check:                      1
;     select_nfs:                               1
;     send_block:                               1
;     send_block_loop:                          1
;     send_data_bytes:                          1
;     send_fs_cmd_v1:                           1
;     send_fs_examine:                          1
;     send_fs_reply:                            1
;     send_fs_reply_cmd:                        1
;     send_gbpb_params:                         1
;     send_osargs_result:                       1
;     send_osfile_ctrl_blk:                     1
;     send_xfer_addr_bytes:                     1
;     service_entry:                            1
;     service_handler:                          1
;     service_handler_entry:                    1
;     set_listen_offset:                        1
;     set_tx_reply_flag:                        1
;     set_workspace_page:                       1
;     setup1:                                   1
;     setup_data_transfer:                      1
;     setup_data_xfer:                          1
;     setup_rom_ptrs_netv:                      1
;     setup_rx_buffer_ptrs:                     1
;     setup_unicast_xfer:                       1
;     skip_clear_flag:                          1
;     skip_cmd_spaces:                          1
;     skip_copy_reply:                          1
;     skip_filename_spaces:                     1
;     skip_iam_spaces:                          1
;     skip_kbd_reenable:                        1
;     skip_lodfil:                              1
;     skip_no_clock_msg:                        1
;     skip_param_read:                          1
;     skip_set_attrib_bit:                      1
;     skpspi:                                   1
;     sr2_test_operand:                         1
;     start_data_tx:                            1
;     store_16bit_at_y:                         1
;     store_buf_ptr_lo:                         1
;     store_fs_error:                           1
;     store_fs_flag:                            1
;     store_fs_hdr_clc:                         1
;     store_fs_hdr_fn:                          1
;     store_handle_return:                      1
;     store_retry_count:                        1
;     store_rxcb_byte:                          1
;     store_station_net:                        1
;     store_status_add4:                        1
;     store_status_calc_xfer:                   1
;     store_txcb_byte:                          1
;     store_xfer_end_addr:                      1
;     string_buf_done:                          1
;     strnh:                                    1
;     sub_4_from_y:                             1
;     subtract_adjust:                          1
;     svc_entry_lo:                             1
;     tbcop1:                                   1
;     toggle_print_flag:                        1
;     trampoline_adlc_init:                     1
;     tube_begin:                               1
;     tube_brk_handler:                         1
;     tube_brk_send_loop:                       1
;     tube_code_page4:                          1
;     tube_code_page6:                          1
;     tube_data_ptr_hi:                         1
;     tube_data_register_4:                     1
;     tube_dispatch_ptr_lo:                     1
;     tube_escape_check:                        1
;     tube_handle_wrch:                         1
;     tube_osbyte_send_y:                       1
;     tube_osfind_close:                        1
;     tube_osword_read:                         1
;     tube_osword_write:                        1
;     tube_osword_write_lp:                     1
;     tube_poll_r2:                             1
;     tube_post_init:                           1
;     tube_rdln_send_line:                      1
;     tube_rdln_send_loop:                      1
;     tube_return_main:                         1
;     tube_setup_transfer:                      1
;     tube_status_register_3:                   1
;     tube_transfer:                            1
;     tube_tx_byte2_operand:                    1
;     tube_tx_byte4_operand:                    1
;     tube_tx_fifo_write:                       1
;     tube_xfer_addr_2:                         1
;     tube_xfer_addr_3:                         1
;     tube_xfer_ctrl_bits:                      1
;     tx_begin:                                 1
;     tx_cr2_operand:                           1
;     tx_ctrl_template:                         1
;     tx_data_start:                            1
;     tx_done_classify:                         1
;     tx_done_error:                            1
;     tx_error:                                 1
;     tx_fifo_not_ready:                        1
;     tx_fifo_write:                            1
;     tx_imm_op_setup:                          1
;     tx_last_data:                             1
;     tx_line_idle_check:                       1
;     tx_line_jammed:                           1
;     tx_nmi_lo_operand:                        1
;     tx_no_clock_error:                        1
;     tx_poll_core:                             1
;     tx_prepare:                               1
;     tx_retry:                                 1
;     tx_semaphore_spin:                        1
;     tx_src_net:                               1
;     tx_store_error:                           1
;     tx_success:                               1
;     txcb_dest:                                1
;     txcb_pos:                                 1
;     update_sequence_return:                   1
;     userv:                                    1
;     wait_fs_reply:                            1
;     wait_nmi_ready:                           1
;     work_ae:                                  1
;     wrch_echo_reply:                          1
;     write_second_tx_byte:                     1
;     y2fsl2:                                   1
;     y2fsl5:                                   1
;     zero_cmd_bytes:                           1
;     zero_exec_header:                         1
;     zp_work_2:                                1

; Automatically generated labels:
;     c955f
;     l0100
;     l0101
;     l0102
;     l0103
;     l0104
;     l0106
;     l0128
;     l0350
;     l0351
;     l0355
;     l0700
;     l0cff
;     l0d1e
;     l0d58
;     l0d59
;     l0d60
;     l0e11
;     l18a5
;     l212e
;     l945f

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7580 bytes (93%)
;     Data                     = 612 bytes (7%)
;
;     Number of instructions   = 3658
;     Number of data bytes     = 362 bytes
;     Number of data words     = 28 bytes
;     Number of string bytes   = 222 bytes
;     Number of strings        = 35
