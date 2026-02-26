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
handle_base                                 = 32
osbyte_acknowledge_escape                   = 126
osbyte_close_spool_exec                     = 119
osbyte_explode_chars                        = 20
osbyte_insert_input_buffer                  = 153
osbyte_issue_service_request                = 143
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
l0000                                   = &0000
l0001                                   = &0001
l0002                                   = &0002
l0003                                   = &0003
zp_temp_10                              = &0010
zp_temp_11                              = &0011
l0012                                   = &0012
l0013                                   = &0013
l0014                                   = &0014
l0015                                   = &0015
zp_63                                   = &005f
escapable                               = &0097
need_release_tube                       = &0098
l0099                                   = &0099
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
l00a8                                   = &00a8
l00a9                                   = &00a9
l00aa                                   = &00aa
l00ab                                   = &00ab
l00ac                                   = &00ac
l00ad                                   = &00ad
l00ae                                   = &00ae
l00af                                   = &00af
fs_load_addr                            = &00b0
fs_load_addr_hi                         = &00b1
fs_load_addr_2                          = &00b2
l00b3                                   = &00b3
l00b4                                   = &00b4
l00b5                                   = &00b5
l00b7                                   = &00b7
fs_error_ptr                            = &00b8
l00b9                                   = &00b9
l00ba                                   = &00ba
fs_options                              = &00bb
fs_block_offset                         = &00bc
fs_last_byte_flag                       = &00bd
fs_crc_lo                               = &00be
fs_crc_hi                               = &00bf
l00c0                                   = &00c0
l00c1                                   = &00c1
l00c2                                   = &00c2
l00c4                                   = &00c4
l00c7                                   = &00c7
l00c8                                   = &00c8
nfs_temp                                = &00cd
rom_svc_num                             = &00ce
l00cf                                   = &00cf
l00ef                                   = &00ef
l00f0                                   = &00f0
l00f1                                   = &00f1
os_text_ptr                             = &00f2
l00f3                                   = &00f3
romsel_copy                             = &00f4
osrdsc_ptr                              = &00f6
l00f7                                   = &00f7
l00fd                                   = &00fd
l00ff                                   = &00ff
l0100                                   = &0100
l0101                                   = &0101
l0102                                   = &0102
l0103                                   = &0103
l0104                                   = &0104
l0106                                   = &0106
l0128                                   = &0128
brkv                                    = &0202
filev                                   = &0212
fscv                                    = &021e
evntv                                   = &0220
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
l0d11                                   = &0d11
nmi_rti                                 = &0d14
nmi_shim_1a                             = &0d1a
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
scout_status                            = &0d5c
rx_extra_byte                           = &0d5d
printer_buf_ptr                         = &0d61
tx_clear_flag                           = &0d62
prot_status                             = &0d63
rx_flags                                = &0d64
saved_jsr_mask                          = &0d65
econet_init_flag                        = &0d66
tube_flag                               = &0d67
l0de6                                   = &0de6
fs_state_deb                            = &0deb
l0df0                                   = &0df0
l0dfe                                   = &0dfe
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
l0e0b                                   = &0e0b
fs_reply_status                         = &0e0d
fs_target_stn                           = &0e0e
fs_cmd_ptr                              = &0e10
l0e16                                   = &0e16
l0e30                                   = &0e30
l0ef7                                   = &0ef7
fs_cmd_type                             = &0f00
fs_cmd_y_param                          = &0f01
fs_cmd_urd                              = &0f02
fs_cmd_csd                              = &0f03
fs_cmd_lib                              = &0f04
fs_cmd_data                             = &0f05
l0f06                                   = &0f06
l0f07                                   = &0f07
l0f08                                   = &0f08
l0f09                                   = &0f09
l0f0b                                   = &0f0b
l0f0c                                   = &0f0c
l0f0d                                   = &0f0d
l0f0e                                   = &0f0e
l0f10                                   = &0f10
l0f11                                   = &0f11
l0f12                                   = &0f12
l0f13                                   = &0f13
l0f14                                   = &0f14
l0f16                                   = &0f16
fs_putb_buf                             = &0fdc
fs_getb_buf                             = &0fdd
l0fde                                   = &0fde
l0fdf                                   = &0fdf
l0fe0                                   = &0fe0
c9630                                   = &9630
sub_c9633                               = &9633
sub_c9636                               = &9636
sub_c9639                               = &9639
sub_c963c                               = &963c
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
tube_data_register_3                    = &fee5
tube_status_register_4_and_cpu_control  = &fee6
tube_data_register_4                    = &fee7
gsinit                                  = &ffc2
gsread                                  = &ffc5
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

    org &9321

.c9321

; Move 1: &9321 to &16 for length 65
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
; 12-entry table at &0500). The R2 command byte is stored at &51
; (self-modifying the JMP indirect low byte) before dispatch.
; ***************************************************************************************
; &9321 referenced 1 time by &817c
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 9321: a9 ff       ..  :0016[1]   ; A=&FF: signal error to co-processor via R4
    jsr tube_send_r4                                                  ; 9323: 20 9e 06     .. :0018[1]
    lda tube_data_register_2                                          ; 9326: ad e3 fe    ... :001b[1]   ; Flush any pending R2 byte
    lda #0                                                            ; 9329: a9 00       ..  :001e[1]
    jsr tube_send_r2                                                  ; 932b: 20 95 06     .. :0020[1]
    tay                                                               ; 932e: a8          .   :0023[1]   ; Y=0: start of error block at (&FD)
    lda (l00fd),y                                                     ; 932f: b1 fd       ..  :0024[1]
    jsr tube_send_r2                                                  ; 9331: 20 95 06     .. :0026[1]
; &9334 referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 9334: c8          .   :0029[1]
; &9335 referenced 1 time by &053d[3]
.c002a
    lda (l00fd),y                                                     ; 9335: b1 fd       ..  :002a[1]
    jsr tube_send_r2                                                  ; 9337: 20 95 06     .. :002c[1]
    tax                                                               ; 933a: aa          .   :002f[1]   ; Zero byte = end of error string
    bne tube_brk_send_loop                                            ; 933b: d0 f7       ..  :0030[1]
; &933d referenced 1 time by &0477[2]
.tube_reset_stack
    ldx #&ff                                                          ; 933d: a2 ff       ..  :0032[1]
    txs                                                               ; 933f: 9a          .   :0034[1]
    cli                                                               ; 9340: 58          X   :0035[1]
; &9341 referenced 6 times by &0044[1], &057f[3], &05a6[3], &0604[4], &0665[4], &0692[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 9341: 2c e0 fe    ,.. :0036[1]
    bpl tube_poll_r2                                                  ; 9344: 10 06       ..  :0039[1]
; &9346 referenced 1 time by &0049[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 9346: ad e1 fe    ... :003b[1]
    jsr oswrch                                                        ; 9349: 20 ee ff     .. :003e[1]   ; Write character
; &934c referenced 1 time by &0039[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 934c: 2c e2 fe    ,.. :0041[1]
    bpl tube_main_loop                                                ; 934f: 10 f0       ..  :0044[1]
    bit tube_status_1_and_tube_control                                ; 9351: 2c e0 fe    ,.. :0046[1]   ; Re-check R1: WRCH has priority over R2
    bmi tube_handle_wrch                                              ; 9354: 30 f0       0.  :0049[1]
    ldx tube_data_register_2                                          ; 9356: ae e3 fe    ... :004b[1]
    stx l0051                                                         ; 9359: 86 51       .Q  :004e[1]   ; Self-modify JMP low byte for dispatch
.tube_dispatch_cmd
l0051 = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 935b: 6c 00 05    l.. :0050[1]

; &935c referenced 1 time by &004e[1]
; &935e referenced 2 times by &04de[2], &04ee[2]
.tube_transfer_addr
    equb 0                                                            ; 935e: 00          .   :0053[1]
; &935f referenced 3 times by &04b6[2], &04d4[2], &04f3[2]
.l0054
    equb &80                                                          ; 935f: 80          .   :0054[1]
; &9360 referenced 2 times by &04ba[2], &04fd[2]
.l0055
    equb 0                                                            ; 9360: 00          .   :0055[1]
; &9361 referenced 2 times by &04be[2], &04fb[2]
.l0056
    equb 0                                                            ; 9361: 00          .   :0056[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, c9321

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &0057

    ; Set the program counter to the next position in the binary file.
    org c9321 + (* - nmi_workspace_start)

.c9362

; Move 2: &9362 to &0400 for length 256
    org &0400
; ***************************************************************************************
; Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)
; 
; Copied from ROM at &9362 during init. The first 28 bytes (&0400-&041B)
; overlap with the end of the ZP block (the same ROM bytes serve both
; the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
;   &0400: JMP &0484 (BEGIN — startup/CLI entry, break type check)
;   &0403: JMP &06E2 (tube_escape_check)
;   &0406: tube_addr_claim — Tube address claim (ADRR protocol)
;   &0414: sub_c0414 — release address claim via R4 command 5
;   &0421: tube_post_init — reset claimed-address state to &80
;   &0435: data transfer setup (SENDW protocol) — &0435-&0483
;   &0484: BEGIN — startup entry, sends ROM contents to Tube
; Rewritten in 3.40: RDCHV handler (&04E7 in 3.34) removed,
; replaced by relocation address extraction from ROM header.
; tube_restore_regs and tube_read_r2 also removed.
; ***************************************************************************************
; &9362 referenced 1 time by &8162
.tube_code_page4
    jmp c0484                                                         ; 9362: 4c 84 04    L.. :0400[2]

.tube_escape_entry
    jmp tube_escape_check                                             ; 9365: 4c a7 06    L.. :0403[2]

; &9368 referenced 10 times by &049a[2], &04cf[2], &8ba1, &8bb8, &8c15, &8e26, &997b, &9a31, &9f07, &9f0f
.tube_addr_claim
    cmp #&80                                                          ; 9368: c9 80       ..  :0406[2]   ; A>=&80: address claim; A<&80: data transfer
    bcc c0435                                                         ; 936a: 90 2b       .+  :0408[2]
    cmp #&c0                                                          ; 936c: c9 c0       ..  :040a[2]   ; A>=&C0: new address claim from another host
    bcs c0428                                                         ; 936e: b0 1a       ..  :040c[2]
    ora #&40 ; '@'                                                    ; 9370: 09 40       .@  :040e[2]   ; Map &80-&BF range to &C0-&FF for comparison
    cmp l0015                                                         ; 9372: c5 15       ..  :0410[2]   ; Is this for our currently-claimed address?
    bne return_tube_init                                              ; 9374: d0 20       .   :0412[2]
; &9376 referenced 1 time by &0471[2]
.sub_c0414
    php                                                               ; 9376: 08          .   :0414[2]
    sei                                                               ; 9377: 78          x   :0415[2]
    lda #5                                                            ; 9378: a9 05       ..  :0416[2]   ; R4 cmd 5: release our address claim
    jsr tube_send_r4                                                  ; 937a: 20 9e 06     .. :0418[2]
    lda l0015                                                         ; 937d: a5 15       ..  :041b[2]
    jsr tube_send_r4                                                  ; 937f: 20 9e 06     .. :041d[2]
    plp                                                               ; 9382: 28          (   :0420[2]
; &9383 referenced 1 time by &8174
.tube_post_init
    lda #&80                                                          ; 9383: a9 80       ..  :0421[2]
    sta l0015                                                         ; 9385: 85 15       ..  :0423[2]   ; &80 sentinel = no address currently claimed
    sta l0014                                                         ; 9387: 85 14       ..  :0425[2]
    rts                                                               ; 9389: 60          `   :0427[2]

; &938a referenced 1 time by &040c[2]
.c0428
    asl l0014                                                         ; 938a: 06 14       ..  :0428[2]   ; Another host claiming; check if we're owner
    bcs c0432                                                         ; 938c: b0 06       ..  :042a[2]
    cmp l0015                                                         ; 938e: c5 15       ..  :042c[2]
    beq return_tube_init                                              ; 9390: f0 04       ..  :042e[2]
    clc                                                               ; 9392: 18          .   :0430[2]   ; Not ours: CLC = we don't own this address
    rts                                                               ; 9393: 60          `   :0431[2]

; &9394 referenced 1 time by &042a[2]
.c0432
    sta l0015                                                         ; 9394: 85 15       ..  :0432[2]   ; Accept new claim: update our address
; &9396 referenced 2 times by &0412[2], &042e[2]
.return_tube_init
    rts                                                               ; 9396: 60          `   :0434[2]

; &9397 referenced 1 time by &0408[2]
.c0435
    php                                                               ; 9397: 08          .   :0435[2]
    sei                                                               ; 9398: 78          x   :0436[2]
    sty l0013                                                         ; 9399: 84 13       ..  :0437[2]   ; Save 16-bit transfer address from (X,Y)
    stx l0012                                                         ; 939b: 86 12       ..  :0439[2]
    jsr tube_send_r4                                                  ; 939d: 20 9e 06     .. :043b[2]   ; Send transfer type byte to co-processor
    tax                                                               ; 93a0: aa          .   :043e[2]
    ldy #3                                                            ; 93a1: a0 03       ..  :043f[2]
    lda l0015                                                         ; 93a3: a5 15       ..  :0441[2]   ; Send our claimed address + 4-byte xfer addr
    jsr tube_send_r4                                                  ; 93a5: 20 9e 06     .. :0443[2]
; &93a8 referenced 1 time by &044c[2]
.loop_c0446
    lda (l0012),y                                                     ; 93a8: b1 12       ..  :0446[2]
    jsr tube_send_r4                                                  ; 93aa: 20 9e 06     .. :0448[2]
    dey                                                               ; 93ad: 88          .   :044b[2]
    bpl loop_c0446                                                    ; 93ae: 10 f8       ..  :044c[2]
    ldy #&18                                                          ; 93b0: a0 18       ..  :044e[2]
    sty tube_status_1_and_tube_control                                ; 93b2: 8c e0 fe    ... :0450[2]   ; Enable Tube interrupt generation
    lda l0518,x                                                       ; 93b5: bd 18 05    ... :0453[2]   ; Look up Tube control bits for this xfer type
    sta tube_status_1_and_tube_control                                ; 93b8: 8d e0 fe    ... :0456[2]
    lsr a                                                             ; 93bb: 4a          J   :0459[2]
    lsr a                                                             ; 93bc: 4a          J   :045a[2]
    bcc c0463                                                         ; 93bd: 90 06       ..  :045b[2]
    bit tube_data_register_3                                          ; 93bf: 2c e5 fe    ,.. :045d[2]   ; Dummy R3 reads: flush for 2-byte transfers
    bit tube_data_register_3                                          ; 93c2: 2c e5 fe    ,.. :0460[2]
; &93c5 referenced 1 time by &045b[2]
.c0463
    jsr tube_send_r4                                                  ; 93c5: 20 9e 06     .. :0463[2]   ; Trigger co-processor ack via R4
; &93c8 referenced 1 time by &0469[2]
.loop_c0466
    bit tube_status_register_4_and_cpu_control                        ; 93c8: 2c e6 fe    ,.. :0466[2]
    bvc loop_c0466                                                    ; 93cb: 50 fb       P.  :0469[2]
    bcs c047a                                                         ; 93cd: b0 0d       ..  :046b[2]   ; R4 bit 7: co-processor acknowledged transfer
    cpx #4                                                            ; 93cf: e0 04       ..  :046d[2]   ; Type 4 = SENDW (host-to-parasite word xfer)
    bne c0482                                                         ; 93d1: d0 11       ..  :046f[2]
; &93d3 referenced 1 time by &0496[2]
.c0471
    jsr sub_c0414                                                     ; 93d3: 20 14 04     .. :0471[2]   ; SENDW complete: release, sync, restart
    jsr tube_send_r2                                                  ; 93d6: 20 95 06     .. :0474[2]
    jmp tube_reset_stack                                              ; 93d9: 4c 32 00    L2. :0477[2]

; &93dc referenced 1 time by &046b[2]
.c047a
    lsr a                                                             ; 93dc: 4a          J   :047a[2]
    bcc c0482                                                         ; 93dd: 90 05       ..  :047b[2]
    ldy #&88                                                          ; 93df: a0 88       ..  :047d[2]   ; Release Tube NMI (transfer used interrupts)
    sty tube_status_1_and_tube_control                                ; 93e1: 8c e0 fe    ... :047f[2]
; &93e4 referenced 2 times by &046f[2], &047b[2]
.c0482
    plp                                                               ; 93e4: 28          (   :0482[2]
.return_tube_xfer
    rts                                                               ; 93e5: 60          `   :0483[2]

; &93e6 referenced 1 time by &0400[2]
.c0484
    cli                                                               ; 93e6: 58          X   :0484[2]   ; BEGIN: enable interrupts for Tube host code
    bcs c0498                                                         ; 93e7: b0 11       ..  :0485[2]
    bne c048c                                                         ; 93e9: d0 03       ..  :0487[2]
    jmp tube_reply_ack                                                ; 93eb: 4c 9c 05    L.. :0489[2]   ; Z=1 from C=0 path: just acknowledge

; &93ee referenced 1 time by &0487[2]
.c048c
    ldx #0                                                            ; 93ee: a2 00       ..  :048c[2]
    ldy #&ff                                                          ; 93f0: a0 ff       ..  :048e[2]
    lda #osbyte_read_write_last_break_type                            ; 93f2: a9 fd       ..  :0490[2]   ; OSBYTE &FD: what type of reset was this?
    jsr osbyte                                                        ; 93f4: 20 f4 ff     .. :0492[2]   ; Read type of last reset
    txa                                                               ; 93f7: 8a          .   :0495[2]   ; X=value of type of last reset
    beq c0471                                                         ; 93f8: f0 d9       ..  :0496[2]   ; Soft break (X=0): re-init Tube and restart
; &93fa referenced 2 times by &0485[2], &049d[2]
.c0498
    lda #&ff                                                          ; 93fa: a9 ff       ..  :0498[2]   ; Claim address &FF (startup = highest prio)
    jsr tube_addr_claim                                               ; 93fc: 20 06 04     .. :049a[2]
    bcc c0498                                                         ; 93ff: 90 f9       ..  :049d[2]
    jsr sub_c04d2                                                     ; 9401: 20 d2 04     .. :049f[2]
; &9404 referenced 1 time by &04c4[2]
.c04a2
    lda #7                                                            ; 9404: a9 07       ..  :04a2[2]   ; R4 cmd 7: SENDW to send ROM to parasite
    jsr sub_c04cb                                                     ; 9406: 20 cb 04     .. :04a4[2]
    ldy #0                                                            ; 9409: a0 00       ..  :04a7[2]
    sty l0000                                                         ; 940b: 84 00       ..  :04a9[2]
; &940d referenced 1 time by &04b4[2]
.loop_c04ab
    lda (l0000),y                                                     ; 940d: b1 00       ..  :04ab[2]   ; Send 256-byte page via R3, byte at a time
    sta tube_data_register_3                                          ; 940f: 8d e5 fe    ... :04ad[2]
    nop                                                               ; 9412: ea          .   :04b0[2]   ; Timing delay: Tube data register needs NOPs
    nop                                                               ; 9413: ea          .   :04b1[2]
    nop                                                               ; 9414: ea          .   :04b2[2]
    iny                                                               ; 9415: c8          .   :04b3[2]
    bne loop_c04ab                                                    ; 9416: d0 f5       ..  :04b4[2]
    inc l0054                                                         ; 9418: e6 54       .T  :04b6[2]   ; Increment 24-bit destination addr
    bne c04c0                                                         ; 941a: d0 06       ..  :04b8[2]
    inc l0055                                                         ; 941c: e6 55       .U  :04ba[2]
    bne c04c0                                                         ; 941e: d0 02       ..  :04bc[2]
    inc l0056                                                         ; 9420: e6 56       .V  :04be[2]
; &9422 referenced 2 times by &04b8[2], &04bc[2]
.c04c0
    inc l0001                                                         ; 9422: e6 01       ..  :04c0[2]
    bit l0001                                                         ; 9424: 24 01       $.  :04c2[2]   ; Bit 6 set = all pages transferred
    bvc c04a2                                                         ; 9426: 50 dc       P.  :04c4[2]
    jsr sub_c04d2                                                     ; 9428: 20 d2 04     .. :04c6[2]
    lda #4                                                            ; 942b: a9 04       ..  :04c9[2]
; &942d referenced 1 time by &04a4[2]
.sub_c04cb
    ldy #0                                                            ; 942d: a0 00       ..  :04cb[2]
    ldx #&53 ; 'S'                                                    ; 942f: a2 53       .S  :04cd[2]
    jmp tube_addr_claim                                               ; 9431: 4c 06 04    L.. :04cf[2]

; &9434 referenced 2 times by &049f[2], &04c6[2]
.sub_c04d2
    lda #&80                                                          ; 9434: a9 80       ..  :04d2[2]   ; Init: start sending from &8000
    sta l0054                                                         ; 9436: 85 54       .T  :04d4[2]
    sta l0001                                                         ; 9438: 85 01       ..  :04d6[2]
    lda #&20 ; ' '                                                    ; 943a: a9 20       .   :04d8[2]
    and rom_type                                                      ; 943c: 2d 06 80    -.. :04da[2]   ; ROM type bit 5: reloc address in header?
    tay                                                               ; 943f: a8          .   :04dd[2]
    sty tube_transfer_addr                                            ; 9440: 84 53       .S  :04de[2]
    beq c04fb                                                         ; 9442: f0 19       ..  :04e0[2]
    ldx copyright_offset                                              ; 9444: ae 07 80    ... :04e2[2]   ; Skip past copyright string to find reloc addr
; &9447 referenced 1 time by &04e9[2]
.loop_c04e5
    inx                                                               ; 9447: e8          .   :04e5[2]
    lda rom_header,x                                                  ; 9448: bd 00 80    ... :04e6[2]
    bne loop_c04e5                                                    ; 944b: d0 fa       ..  :04e9[2]
    lda l8001,x                                                       ; 944d: bd 01 80    ... :04eb[2]   ; Read 4-byte reloc address from ROM header
    sta tube_transfer_addr                                            ; 9450: 85 53       .S  :04ee[2]
    lda l8002,x                                                       ; 9452: bd 02 80    ... :04f0[2]
    sta l0054                                                         ; 9455: 85 54       .T  :04f3[2]
    ldy service_entry,x                                               ; 9457: bc 03 80    ... :04f5[2]
    lda l8004,x                                                       ; 945a: bd 04 80    ... :04f8[2]
; &945d referenced 1 time by &04e0[2]
.c04fb
    sta l0056                                                         ; 945d: 85 56       .V  :04fb[2]
    sty l0055                                                         ; 945f: 84 55       .U  :04fd[2]
    rts                                                               ; 9461: 60          `   :04ff[2]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, c9362

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &0500

    ; Set the program counter to the next position in the binary file.
    org c9362 + (* - tube_code_page4)

.l9462

; Move 3: &9462 to &0500 for length 256
    org &0500
; ***************************************************************************************
; Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)
; 
; Copied from ROM at &9462 during init. Rewritten in 3.40 (was 14
; entries in 3.34, now 12 — tube_restore_regs/tube_release_return
; entries removed). Contains:
;   &0500: 12-entry dispatch table (&0500-&0517)
;   &0518: 8-byte Tube control register value table
;   &0520: tube_osbput — write byte to file
;   &052D: tube_osbget — read byte from file
;   &0537: tube_osrdch — read character
;   &053A: tube_rdch_reply — send carry+data as reply
;   &0542: tube_osfind — open/close file
;   &055E: tube_osargs — file argument read/write
;   &0582: tube_read_string — read string from R2 into &0700
;   &0596: tube_oscli — execute * command
;   &059C: tube_reply_ack — send &7F acknowledge
;   &05A9: tube_osfile — whole file operation
;   &05D1: tube_osgbpb — multi-byte file read/write
; Code continues seamlessly into page 6 (tube_osbyte_short at &05F2
; straddles the page boundary with a BVC at &05FF/&0600).
; ***************************************************************************************
; &9462 referenced 2 times by &0050[1], &8168
.tube_dispatch_table
    equb &37, 5, &96, 5, &f2, 5,   7, 6, &27, 6, &68, 6, &5e, 5       ; 9462: 37 05 96... 7.. :0500[3]
    equb &2d, 5, &20, 5, &42, 5, &a9, 5, &d1, 5                       ; 9470: 2d 05 20... -.  :050e[3]
; &947a referenced 1 time by &0453[2]
.l0518
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; 947a: 86 88 96... ... :0518[3]

.tube_osbput
    jsr c06c5                                                         ; 9482: 20 c5 06     .. :0520[3]
    tay                                                               ; 9485: a8          .   :0523[3]   ; Y=channel handle from R2
    jsr c06c5                                                         ; 9486: 20 c5 06     .. :0524[3]
.tube_poll_r1_wrch
    jsr osbput                                                        ; 9489: 20 d4 ff     .. :0527[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 948c: 4c 9c 05    L.. :052a[3]

.tube_osbget
    jsr c06c5                                                         ; 948f: 20 c5 06     .. :052d[3]
    tay                                                               ; 9492: a8          .   :0530[3]   ; Y=channel handle for OSBGET; Y=file handle
    jsr osbget                                                        ; 9493: 20 d7 ff     .. :0531[3]   ; Read a single byte from an open file Y
    jmp tube_rdch_reply                                               ; 9496: 4c 3a 05    L:. :0534[3]

.tube_osrdch
    jsr osrdch                                                        ; 9499: 20 e0 ff     .. :0537[3]   ; Read a character from the current input stream
; &949c referenced 2 times by &0534[3], &05ef[3]
.tube_rdch_reply
    ror a                                                             ; 949c: 6a          j   :053a[3]   ; ROR A: encode carry (error flag) into bit 7
; Overlapping code: bytes &053B-&053D (20 95 06) are
; JSR tube_send_r2 when falling through from ROR A
; above. In 3.34, dispatch entry 7 jumped to &053D
; where &06 became ASL; that entry was removed in 3.40
; so tube_release_return is now dead code.
    equb &20, &95                                                     ; 949d: 20 95        .  :053b[3]   ; = JSR tube_send_r2 (overlaps &053D entry)

.tube_release_return
    asl c002a                                                         ; 949f: 06 2a       .*  :053d[3]
    jmp tube_reply_byte                                               ; 94a1: 4c 9e 05    L.. :053f[3]

.tube_osfind
    jsr c06c5                                                         ; 94a4: 20 c5 06     .. :0542[3]
    beq tube_osfind_close                                             ; 94a7: f0 0b       ..  :0545[3]   ; A=0: close file, else open with filename
    pha                                                               ; 94a9: 48          H   :0547[3]   ; Save open mode while reading filename
    jsr tube_read_string                                              ; 94aa: 20 82 05     .. :0548[3]
    pla                                                               ; 94ad: 68          h   :054b[3]
    jsr osfind                                                        ; 94ae: 20 ce ff     .. :054c[3]   ; Open or close file(s)
    jmp tube_reply_byte                                               ; 94b1: 4c 9e 05    L.. :054f[3]

; &94b4 referenced 1 time by &0545[3]
.tube_osfind_close
    jsr c06c5                                                         ; 94b4: 20 c5 06     .. :0552[3]
    tay                                                               ; 94b7: a8          .   :0555[3]   ; Y=handle to close
    lda #osfind_close                                                 ; 94b8: a9 00       ..  :0556[3]
    jsr osfind                                                        ; 94ba: 20 ce ff     .. :0558[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94bd: 4c 9c 05    L.. :055b[3]

.tube_osargs
    jsr c06c5                                                         ; 94c0: 20 c5 06     .. :055e[3]
    tay                                                               ; 94c3: a8          .   :0561[3]   ; Y=file handle for OSARGS
.tube_read_params
    ldx #4                                                            ; 94c4: a2 04       ..  :0562[3]   ; Read 4-byte arg + reason from R2 into ZP
; &94c6 referenced 1 time by &056a[3]
.loop_c0564
    jsr c06c5                                                         ; 94c6: 20 c5 06     .. :0564[3]
    sta l00ff,x                                                       ; 94c9: 95 ff       ..  :0567[3]   ; Params stored at &00-&03 (little-endian)
    dex                                                               ; 94cb: ca          .   :0569[3]
    bne loop_c0564                                                    ; 94cc: d0 f8       ..  :056a[3]
    jsr c06c5                                                         ; 94ce: 20 c5 06     .. :056c[3]
    jsr osargs                                                        ; 94d1: 20 da ff     .. :056f[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 94d4: 20 95 06     .. :0572[3]   ; Send result A back to co-processor
    ldx #3                                                            ; 94d7: a2 03       ..  :0575[3]   ; Return 4-byte result from ZP &00-&03
; &94d9 referenced 1 time by &057d[3]
.loop_c0577
    lda l0000,x                                                       ; 94d9: b5 00       ..  :0577[3]
    jsr tube_send_r2                                                  ; 94db: 20 95 06     .. :0579[3]
    dex                                                               ; 94de: ca          .   :057c[3]
    bpl loop_c0577                                                    ; 94df: 10 f8       ..  :057d[3]
    jmp tube_main_loop                                                ; 94e1: 4c 36 00    L6. :057f[3]

; &94e4 referenced 3 times by &0548[3], &0596[3], &05b3[3]
.tube_read_string
    ldx #0                                                            ; 94e4: a2 00       ..  :0582[3]
    ldy #0                                                            ; 94e6: a0 00       ..  :0584[3]   ; X=0, Y=0: buffer at &0700, offset 0
; &94e8 referenced 1 time by &0591[3]
.strnh
    jsr c06c5                                                         ; 94e8: 20 c5 06     .. :0586[3]
    sta l0700,y                                                       ; 94eb: 99 00 07    ... :0589[3]
    iny                                                               ; 94ee: c8          .   :058c[3]
    beq c0593                                                         ; 94ef: f0 04       ..  :058d[3]   ; Y overflow: string too long, truncate
    cmp #&0d                                                          ; 94f1: c9 0d       ..  :058f[3]
    bne strnh                                                         ; 94f3: d0 f3       ..  :0591[3]
; &94f5 referenced 1 time by &058d[3]
.c0593
    ldy #7                                                            ; 94f5: a0 07       ..  :0593[3]   ; Y=7: set XY=&0700 for OSCLI/OSFIND
    rts                                                               ; 94f7: 60          `   :0595[3]

.tube_oscli
    jsr tube_read_string                                              ; 94f8: 20 82 05     .. :0596[3]
    jsr oscli                                                         ; 94fb: 20 f7 ff     .. :0599[3]
; &94fe referenced 3 times by &0489[2], &052a[3], &055b[3]
.tube_reply_ack
    lda #&7f                                                          ; 94fe: a9 7f       ..  :059c[3]   ; &7F = success acknowledgement
; &9500 referenced 4 times by &053f[3], &054f[3], &05a1[3], &067d[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 9500: 2c e2 fe    ,.. :059e[3]
    bvc tube_reply_byte                                               ; 9503: 50 fb       P.  :05a1[3]
    sta tube_data_register_2                                          ; 9505: 8d e3 fe    ... :05a3[3]
; &9508 referenced 1 time by &05cf[3]
.mj
    jmp tube_main_loop                                                ; 9508: 4c 36 00    L6. :05a6[3]

.tube_osfile
    ldx #&10                                                          ; 950b: a2 10       ..  :05a9[3]   ; Read 16-byte OSFILE control block from R2
; &950d referenced 1 time by &05b1[3]
.argsw
    jsr c06c5                                                         ; 950d: 20 c5 06     .. :05ab[3]
    sta l0001,x                                                       ; 9510: 95 01       ..  :05ae[3]
    dex                                                               ; 9512: ca          .   :05b0[3]
    bne argsw                                                         ; 9513: d0 f8       ..  :05b1[3]
    jsr tube_read_string                                              ; 9515: 20 82 05     .. :05b3[3]
    stx l0000                                                         ; 9518: 86 00       ..  :05b6[3]   ; XY=&0700: filename pointer for OSFILE
    sty l0001                                                         ; 951a: 84 01       ..  :05b8[3]
    ldy #0                                                            ; 951c: a0 00       ..  :05ba[3]
    jsr c06c5                                                         ; 951e: 20 c5 06     .. :05bc[3]
    jsr osfile                                                        ; 9521: 20 dd ff     .. :05bf[3]
    jsr tube_send_r2                                                  ; 9524: 20 95 06     .. :05c2[3]   ; Send result A (object type) to co-processor
    ldx #&10                                                          ; 9527: a2 10       ..  :05c5[3]   ; Return 16-byte control block to co-processor
; &9529 referenced 1 time by &05cd[3]
.loop_c05c7
    lda l0001,x                                                       ; 9529: b5 01       ..  :05c7[3]
    jsr tube_send_r2                                                  ; 952b: 20 95 06     .. :05c9[3]
    dex                                                               ; 952e: ca          .   :05cc[3]
    bne loop_c05c7                                                    ; 952f: d0 f8       ..  :05cd[3]
    beq mj                                                            ; 9531: f0 d5       ..  :05cf[3]   ; ALWAYS branch

    ldx #&0d                                                          ; 9533: a2 0d       ..  :05d1[3]   ; Read 13-byte OSGBPB control block from R2
; &9535 referenced 1 time by &05d9[3]
.loop_c05d3
    jsr c06c5                                                         ; 9535: 20 c5 06     .. :05d3[3]
    sta l00ff,x                                                       ; 9538: 95 ff       ..  :05d6[3]
    dex                                                               ; 953a: ca          .   :05d8[3]
    bne loop_c05d3                                                    ; 953b: d0 f8       ..  :05d9[3]
    jsr c06c5                                                         ; 953d: 20 c5 06     .. :05db[3]
    ldy #0                                                            ; 9540: a0 00       ..  :05de[3]
    jsr osgbpb                                                        ; 9542: 20 d1 ff     .. :05e0[3]   ; Read or write multiple bytes to an open file
    pha                                                               ; 9545: 48          H   :05e3[3]   ; Save A (completion status) for later
    ldx #&0c                                                          ; 9546: a2 0c       ..  :05e4[3]   ; Return 13-byte result block to co-processor
; &9548 referenced 1 time by &05ec[3]
.loop_c05e6
    lda l0000,x                                                       ; 9548: b5 00       ..  :05e6[3]
    jsr tube_send_r2                                                  ; 954a: 20 95 06     .. :05e8[3]
    dex                                                               ; 954d: ca          .   :05eb[3]
    bpl loop_c05e6                                                    ; 954e: 10 f8       ..  :05ec[3]
    pla                                                               ; 9550: 68          h   :05ee[3]
    jmp tube_rdch_reply                                               ; 9551: 4c 3a 05    L:. :05ef[3]

    jsr c06c5                                                         ; 9554: 20 c5 06     .. :05f2[3]
    tax                                                               ; 9557: aa          .   :05f5[3]
    jsr c06c5                                                         ; 9558: 20 c5 06     .. :05f6[3]
    jsr osbyte                                                        ; 955b: 20 f4 ff     .. :05f9[3]
; &955e referenced 2 times by &05ff[3], &0625[4]
.c05fc
    bit tube_status_register_2                                        ; 955e: 2c e2 fe    ,.. :05fc[3]
    equb &50                                                          ; 9561: 50          P   :05ff[3]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_dispatch_table, *, l9462

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org l9462 + (* - tube_dispatch_table)

.l9562

; Move 4: &9562 to &0600 for length 256
    org &0600
; &9562 referenced 1 time by &816e
.l0600
    equb &fb                                                          ; 9562: fb          .   :0600[4]

    stx tube_data_register_2                                          ; 9563: 8e e3 fe    ... :0601[4]   ; Send X result for 2-param OSBYTE
; &9566 referenced 1 time by &0617[4]
.bytex
    jmp tube_main_loop                                                ; 9566: 4c 36 00    L6. :0604[4]

.tube_osbyte_long
    jsr c06c5                                                         ; 9569: 20 c5 06     .. :0607[4]   ; Read X, Y, A from R2 for 3-param OSBYTE
    tax                                                               ; 956c: aa          .   :060a[4]
    jsr c06c5                                                         ; 956d: 20 c5 06     .. :060b[4]
    tay                                                               ; 9570: a8          .   :060e[4]
    jsr c06c5                                                         ; 9571: 20 c5 06     .. :060f[4]
    jsr osbyte                                                        ; 9574: 20 f4 ff     .. :0612[4]
    eor #&9d                                                          ; 9577: 49 9d       I.  :0615[4]   ; 3.35K fix: send carry result to co-processor.
; 3.35D had PHA here (never sent, never popped).
    beq bytex                                                         ; 9579: f0 eb       ..  :0617[4]   ; OSBYTE &9D (fast Tube BPUT): no result needed
    ror a                                                             ; 957b: 6a          j   :0619[4]   ; Encode carry (error flag) into bit 7
    jsr tube_send_r2                                                  ; 957c: 20 95 06     .. :061a[4]
; &957f referenced 1 time by &0620[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 957f: 2c e2 fe    ,.. :061d[4]
    bvc tube_osbyte_send_y                                            ; 9582: 50 fb       P.  :0620[4]
    sty tube_data_register_2                                          ; 9584: 8c e3 fe    ... :0622[4]   ; Send Y result, then fall through to send X
.tube_osbyte_short
    bvs c05fc                                                         ; 9587: 70 d5       p.  :0625[4]   ; BVS &05FC: overlapping code — loops back to page 5 R2 poll to send X after Y
    jsr c06c5                                                         ; 9589: 20 c5 06     .. :0627[4]   ; Overlapping entry: &20 = JSR c06c5 (OSWORD)
    tay                                                               ; 958c: a8          .   :062a[4]
; &958d referenced 1 time by &062e[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 958d: 2c e2 fe    ,.. :062b[4]
    bpl tube_osword_read                                              ; 9590: 10 fb       ..  :062e[4]
.tube_osbyte_send_x
    ldx tube_data_register_2                                          ; 9592: ae e3 fe    ... :0630[4]   ; Read param block length from R2
    dex                                                               ; 9595: ca          .   :0633[4]   ; DEX: length 0 means no params to read
    bmi c0645                                                         ; 9596: 30 0f       0.  :0634[4]
; &9598 referenced 2 times by &0639[4], &0642[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 9598: 2c e2 fe    ,.. :0636[4]
    bpl tube_osword_read_lp                                           ; 959b: 10 fb       ..  :0639[4]
    lda tube_data_register_2                                          ; 959d: ad e3 fe    ... :063b[4]
    sta l0128,x                                                       ; 95a0: 9d 28 01    .(. :063e[4]   ; Store param bytes into block at &0128
    dex                                                               ; 95a3: ca          .   :0641[4]
    bpl tube_osword_read_lp                                           ; 95a4: 10 f2       ..  :0642[4]
    tya                                                               ; 95a6: 98          .   :0644[4]   ; Restore OSWORD number from Y
; &95a7 referenced 1 time by &0634[4]
.c0645
    ldx #<(l0128)                                                     ; 95a7: a2 28       .(  :0645[4]   ; XY=&0128: param block address for OSWORD
    ldy #>(l0128)                                                     ; 95a9: a0 01       ..  :0647[4]
    jsr osword                                                        ; 95ab: 20 f1 ff     .. :0649[4]
; &95ae referenced 1 time by &064f[4]
.loop_c064c
    bit tube_status_register_2                                        ; 95ae: 2c e2 fe    ,.. :064c[4]
    bpl loop_c064c                                                    ; 95b1: 10 fb       ..  :064f[4]
    ldx tube_data_register_2                                          ; 95b3: ae e3 fe    ... :0651[4]   ; Read result block length from R2
    dex                                                               ; 95b6: ca          .   :0654[4]
    bmi tube_return_main                                              ; 95b7: 30 0e       0.  :0655[4]   ; No results to send: return to main loop
; &95b9 referenced 1 time by &0663[4]
.tube_osword_write
    ldy l0128,x                                                       ; 95b9: bc 28 01    .(. :0657[4]   ; Send result block bytes from &0128 via R2
; &95bc referenced 1 time by &065d[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95bc: 2c e2 fe    ,.. :065a[4]
    bvc tube_osword_write_lp                                          ; 95bf: 50 fb       P.  :065d[4]
    sty tube_data_register_2                                          ; 95c1: 8c e3 fe    ... :065f[4]
    dex                                                               ; 95c4: ca          .   :0662[4]
    bpl tube_osword_write                                             ; 95c5: 10 f2       ..  :0663[4]
; &95c7 referenced 1 time by &0655[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95c7: 4c 36 00    L6. :0665[4]

.tube_osword_rdln
    ldx #4                                                            ; 95ca: a2 04       ..  :0668[4]   ; Read 5-byte OSWORD 0 control block from R2
; &95cc referenced 1 time by &0670[4]
.loop_c066a
    jsr c06c5                                                         ; 95cc: 20 c5 06     .. :066a[4]
    sta l0000,x                                                       ; 95cf: 95 00       ..  :066d[4]
    dex                                                               ; 95d1: ca          .   :066f[4]
    bpl loop_c066a                                                    ; 95d2: 10 f8       ..  :0670[4]
    inx                                                               ; 95d4: e8          .   :0672[4]   ; X=0 after loop, A=0 for OSWORD 0 (read line)
    ldy #0                                                            ; 95d5: a0 00       ..  :0673[4]
    txa                                                               ; 95d7: 8a          .   :0675[4]
    jsr osword                                                        ; 95d8: 20 f1 ff     .. :0676[4]
    bcc tube_rdln_send_line                                           ; 95db: 90 05       ..  :0679[4]   ; C=0: line read OK; C=1: escape pressed
    lda #&ff                                                          ; 95dd: a9 ff       ..  :067b[4]   ; &FF = escape/error signal to co-processor
    jmp tube_reply_byte                                               ; 95df: 4c 9e 05    L.. :067d[4]

; &95e2 referenced 1 time by &0679[4]
.tube_rdln_send_line
    ldx #0                                                            ; 95e2: a2 00       ..  :0680[4]
    lda #&7f                                                          ; 95e4: a9 7f       ..  :0682[4]   ; &7F = line read successfully
    jsr tube_send_r2                                                  ; 95e6: 20 95 06     .. :0684[4]
; &95e9 referenced 1 time by &0690[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 95e9: bd 00 07    ... :0687[4]
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 95ec: 20 95 06     .. :068a[4]
    inx                                                               ; 95ef: e8          .   :068d[4]
    cmp #&0d                                                          ; 95f0: c9 0d       ..  :068e[4]   ; Loop until CR terminator sent
    bne tube_rdln_send_loop                                           ; 95f2: d0 f5       ..  :0690[4]
    jmp tube_main_loop                                                ; 95f4: 4c 36 00    L6. :0692[4]

; &95f7 referenced 13 times by &0020[1], &0026[1], &002c[1], &0474[2], &0572[3], &0579[3], &05c2[3], &05c9[3], &05e8[3], &061a[4], &0684[4], &068a[4], &0698[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 95f7: 2c e2 fe    ,.. :0695[4]
    bvc tube_send_r2                                                  ; 95fa: 50 fb       P.  :0698[4]
    sta tube_data_register_2                                          ; 95fc: 8d e3 fe    ... :069a[4]
    rts                                                               ; 95ff: 60          `   :069d[4]

; &9600 referenced 8 times by &0018[1], &0418[2], &041d[2], &043b[2], &0443[2], &0448[2], &0463[2], &06a1[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 9600: 2c e6 fe    ,.. :069e[4]
    bvc tube_send_r4                                                  ; 9603: 50 fb       P.  :06a1[4]
    sta tube_data_register_4                                          ; 9605: 8d e7 fe    ... :06a3[4]
    rts                                                               ; 9608: 60          `   :06a6[4]

; &9609 referenced 1 time by &0403[2]
.tube_escape_check
    lda l00ff                                                         ; 9609: a5 ff       ..  :06a7[4]   ; Check OS escape flag at &FF
    sec                                                               ; 960b: 38          8   :06a9[4]   ; SEC+ROR: put bit 7 of &FF into carry+bit 7
    ror a                                                             ; 960c: 6a          j   :06aa[4]
    bmi tube_send_r1                                                  ; 960d: 30 0f       0.  :06ab[4]   ; Escape set: forward to co-processor via R1
.tube_event_handler
    pha                                                               ; 960f: 48          H   :06ad[4]   ; EVNTV: forward event A, Y, X to co-processor
    lda #0                                                            ; 9610: a9 00       ..  :06ae[4]   ; Send &00 prefix (event notification)
    jsr tube_send_r1                                                  ; 9612: 20 bc 06     .. :06b0[4]
    tya                                                               ; 9615: 98          .   :06b3[4]
    jsr tube_send_r1                                                  ; 9616: 20 bc 06     .. :06b4[4]
    txa                                                               ; 9619: 8a          .   :06b7[4]
    jsr tube_send_r1                                                  ; 961a: 20 bc 06     .. :06b8[4]
    pla                                                               ; 961d: 68          h   :06bb[4]
; &961e referenced 5 times by &06ab[4], &06b0[4], &06b4[4], &06b8[4], &06bf[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 961e: 2c e0 fe    ,.. :06bc[4]
    bvc tube_send_r1                                                  ; 9621: 50 fb       P.  :06bf[4]
    sta tube_data_register_1                                          ; 9623: 8d e1 fe    ... :06c1[4]
    rts                                                               ; 9626: 60          `   :06c4[4]

; &9627 referenced 21 times by &0520[3], &0524[3], &052d[3], &0542[3], &0552[3], &055e[3], &0564[3], &056c[3], &0586[3], &05ab[3], &05bc[3], &05d3[3], &05db[3], &05f2[3], &05f6[3], &0607[4], &060b[4], &060f[4], &0627[4], &066a[4], &06c8[4]
.c06c5
    bit tube_status_register_2                                        ; 9627: 2c e2 fe    ,.. :06c5[4]
    bpl c06c5                                                         ; 962a: 10 fb       ..  :06c8[4]
    lda tube_data_register_2                                          ; 962c: ad e3 fe    ... :06ca[4]
    rts                                                               ; 962f: 60          `   :06cd[4]

.trampoline_tx_setup
    jmp c9b6e                                                         ; 9630: 4c 6e 9b    Ln. :06ce[4]

.trampoline_adlc_init
    jmp adlc_init                                                     ; 9633: 4c 7a 96    Lz. :06d1[4]

.svc_12_nmi_release
    jmp c9f57                                                         ; 9636: 4c 57 9f    LW. :06d4[4]

.svc_11_nmi_claim
    jmp c9698                                                         ; 9639: 4c 98 96    L.. :06d7[4]

    lda #4                                                            ; 963c: a9 04       ..  :06da[4]
    bit system_via_ifr                                                ; 963e: 2c 4d fe    ,M. :06dc[4]
    bne c06e4                                                         ; 9641: d0 03       ..  :06df[4]
    lda #5                                                            ; 9643: a9 05       ..  :06e1[4]
    rts                                                               ; 9645: 60          `   :06e3[4]

; &9646 referenced 1 time by &06df[4]
.c06e4
    txa                                                               ; 9646: 8a          .   :06e4[4]
    pha                                                               ; 9647: 48          H   :06e5[4]
    tya                                                               ; 9648: 98          .   :06e6[4]
    pha                                                               ; 9649: 48          H   :06e7[4]
    lda system_via_acr                                                ; 964a: ad 4b fe    .K. :06e8[4]
    and #&e3                                                          ; 964d: 29 e3       ).  :06eb[4]
    ora tx_work_51                                                    ; 964f: 0d 51 0d    .Q. :06ed[4]
    sta system_via_acr                                                ; 9652: 8d 4b fe    .K. :06f0[4]
    lda system_via_sr                                                 ; 9655: ad 4a fe    .J. :06f3[4]
    lda #4                                                            ; 9658: a9 04       ..  :06f6[4]
    sta system_via_ifr                                                ; 965a: 8d 4d fe    .M. :06f8[4]
    sta system_via_ier                                                ; 965d: 8d 4e fe    .N. :06fb[4]
    equb &ac, &57                                                     ; 9660: ac 57       .W  :06fe[4]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock l0600, *, l9562

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear l0600, &0700

    ; Set the program counter to the next position in the binary file.
    org l9562 + (* - l0600)


    org &8000

; Sideways ROM header
; NFS ROM 3.34B disassembly (Acorn Econet filing system)
; 
; NMI handler architecture
; ========================
; The NFS ROM uses self-modifying code to implement a state
; machine for ADLC communication. An NMI workspace shim is
; copied to &0D00 at init.
; 
; NMI entry (&0D00):
;   BIT &FE18       ; INTOFF -- immediately disable further NMIs
;   PHA / TYA / PHA ; save A, Y
;   LDA #$nn        ; page in NFS ROM bank (self-modified)
;   STA &FE30
;   JMP $xxxx       ; self-modifying target at &0D0C/&0D0D
; 
; set_nmi_vector (&0D0E): stores A->&0D0C (low), Y->&0D0D (high)
;   Falls through to nmi_rti.
; 
; nmi_rti (&0D14):
;   LDA &F4         ; restore original ROM bank
;   STA &FE30
;   PLA / TAY / PLA ; restore Y, A
;   BIT &FE20       ; INTON -- re-enable NMIs
;   RTI
; 
; NMI handler chain for outbound TX (four-way handshake):
;   &96BF: RX scout (idle listen, default handler)
;   &9BD6: INACTIVE polling (pre-TX, waits for idle line)
;   &9CCC: TX data (2 bytes per NMI, tight loop if IRQ persists)
;   &9D08: TX_LAST_DATA (close frame)
;   &9D14: TX completion (switch to RX: CR1=&82)
;   &9D30: RX reply scout (check AP, read dest_stn)
;   &9D44: RX reply continuation (read dest_net, validate)
;   &9D5B: RX reply validation (read src_stn/net, check FV)
;   &9DA3: TX scout ACK (write dest/src addr, TX_LAST_DATA)
;   &9E50: Four-way handshake data phase
; 
; NMI handler chain for inbound reception (scout -> data):
;   &96BF: RX scout (idle listen)
;   &96DC: RX scout second byte (dest_net, install &970E)
;   &970E: Scout data loop (read body in pairs, detect FV)
;   &9738: Scout completion (disable PSE, read last byte)
;   &98EE: TX scout ACK
;   &97E6: RX data frame (AP check, validate dest_stn/net)
;   &9843: RX data bulk read (read payload into buffer)
;   &9877: RX data completion (disable PSE, check FV, read last)
;   &98EE: TX final ACK
; 
; Key ADLC register values:
;   CR1=&C1: full reset (TX_RESET|RX_RESET|AC)
;   CR1=&82: RX listen (TX_RESET|RIE)
;   CR1=&44: TX active (RX_RESET|TIE)
; 
;   CR2 values (all set FC_TDRA|2_1_BYTE|PSE):
;   &67: clear status  CLR_TX_ST|CLR_RX_ST
;   &E7: TX prepare    RTS|CLR_TX_ST|CLR_RX_ST
;   &3F: TX last data  CLR_RX_ST|TX_LAST_DATA|FLAG_IDLE
;   &A7: TX handshake  RTS|CLR_TX_ST
; &8000 referenced 1 time by &04e6[2]
.pydis_start
.rom_header
.language_entry
l8001 = rom_header+1
l8002 = rom_header+2
    jmp language_handler                                              ; 8000: 4c e1 80    L..

; &8001 referenced 1 time by &04eb[2]
; &8002 referenced 1 time by &04f0[2]
; &8003 referenced 1 time by &04f5[2]
.service_entry
l8004 = service_entry+1
    jmp service_handler                                               ; 8003: 4c f7 80    L..

; &8004 referenced 1 time by &04f8[2]
; &8006 referenced 1 time by &04da[2]
.rom_type
    equb &82                                                          ; 8006: 82          .
; &8007 referenced 1 time by &04e2[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 10          .
; &8008 referenced 2 times by &836e, &8377
.binary_version
    equb &83                                                          ; 8008: 83          .
.title
    equs "    NET"                                                    ; 8009: 20 20 20...
.copyright
    equb 0                                                            ; 8010: 00          .
; The 'ROFF' suffix at &8014 is reused by the *ROFF
; command matcher (svc_star_command) — a space-saving
; trick that shares ROM bytes between the copyright
; string and the star command table.
.copyright_string
    equs "(C)ROFF"                                                    ; 8011: 28 43 29... (C)
; Error message offset table (9 entries).
; Each byte is a Y offset into error_msg_table.
; Entry 0 (Y=0, "Line Jammed") doubles as the
; copyright string null terminator.
; Indexed by TXCB status (AND #7), or hardcoded 8.
; &8018 referenced 1 time by &8515
.error_offsets
    equb 0                                                            ; 8018: 00          .              ; "Line Jammed"
    equb &0d                                                          ; 8019: 0d          .              ; "Net Error"
    equb &18                                                          ; 801a: 18          .              ; "Not listening"
    equb &27                                                          ; 801b: 27          '              ; "No Clock"
    equb &31                                                          ; 801c: 31          1              ; "Escape"
    equb &31                                                          ; 801d: 31          1              ; "Escape"
    equb &31                                                          ; 801e: 31          1              ; "Escape"
    equb &39                                                          ; 801f: 39          9              ; "Bad Option"
    equb &45                                                          ; 8020: 45          E              ; "No reply"
; Four bytes with unknown purpose.
    equb 1                                                            ; 8021: 01          .              ; Purpose unknown
    equb 0                                                            ; 8022: 00          .              ; Purpose unknown
    equb &60                                                          ; 8023: 60          `              ; Purpose unknown
; &8024 referenced 1 time by &80f0
    equb 3                                                            ; 8024: 03          .              ; Purpose unknown
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at &80E7.
; See dispatch_0_hi (&804A) for the corresponding high bytes.
; 
; Five callers share this table via different Y base offsets:
;   Y=&00  Service calls 0-12       (indices 0-13)
;   Y=&0E  Language entry reasons    (indices 14-18)
;   Y=&13  FSCV codes 0-7           (indices 19-26)
;   Y=&17  FS reply handlers        (indices 27-32)
;   Y=&21  *NET1-4 sub-commands     (indices 33-36)
; 
; Lo bytes for the last 6 entries (indices 31-36) occupy
; &8044-&8049, immediately before the hi bytes. Their hi
; bytes are at &8069-&806E, after dispatch_0_hi.
.dispatch_0_lo
    equb <(return_1-1)                                                ; 8025: f5          .              ; lo - Svc 0: already claimed (no-op)
    equb <(svc_1_abs_workspace-1)                                     ; 8026: bb          .              ; lo - Svc 1: absolute workspace
    equb <(svc_2_private_workspace-1)                                 ; 8027: c4          .              ; lo - Svc 2: private workspace
    equb <(svc_3_autoboot-1)                                          ; 8028: 1c          .              ; lo - Svc 3: auto-boot
    equb <(svc_4_star_command-1)                                      ; 8029: b4          .              ; lo - Svc 4: unrecognised star command
    equb <(sub_c963c-1)                                               ; 802a: 3b          ;              ; lo - Svc 5: unrecognised interrupt
    equb <(return_1-1)                                                ; 802b: f5          .              ; lo - Svc 6: BRK (no-op)
    equb <(dispatch_net_cmd-1)                                        ; 802c: 6e          n              ; lo - Svc 7: unrecognised OSBYTE
    equb <(svc_8_osword-1)                                            ; 802d: 86          .              ; lo - Svc 8: unrecognised OSWORD
    equb <(svc_9_help-1)                                              ; 802e: 07          .              ; lo - Svc 9: *HELP
    equb <(return_1-1)                                                ; 802f: f5          .              ; lo - Svc 10: static workspace (no-op)
    equb <(sub_c9639-1)                                               ; 8030: 38          8              ; lo - Svc 11: NMI release (reclaim NMIs)
    equb <(sub_c9636-1)                                               ; 8031: 35          5              ; lo - Svc 12: NMI claim (save NMI state)
    equb <(svc_13_select_nfs-1)                                       ; 8032: f0          .              ; lo - Svc 13: select NFS (intercepted before dispatch)
    equb <(lang_0_insert_remote_key-1)                                ; 8033: fc          .              ; lo - Lang 0: no language / Tube
    equb <(lang_1_remote_boot-1)                                      ; 8034: ae          .              ; lo - Lang 1: normal startup
    equb <(lang_2_save_palette_vdu-1)                                 ; 8035: aa          .              ; lo - Lang 2: softkey byte (Electron)
    equb <(lang_3_execute_at_0100-1)                                  ; 8036: dc          .              ; lo - Lang 3: softkey length (Electron)
    equb <(lang_4_remote_validated-1)                                 ; 8037: ec          .              ; lo - Lang 4: remote validated
    equb <(fscv_0_opt_entry-1)                                        ; 8038: 2b          +              ; lo - FSCV 0: *OPT
    equb <(fscv_1_eof-1)                                              ; 8039: ac          .              ; lo - FSCV 1: EOF check
    equb <(fscv_2_star_run-1)                                         ; 803a: db          .              ; lo - FSCV 2: */ (run)
    equb <(fscv_3_star_cmd-1)                                         ; 803b: 1a          .              ; lo - FSCV 3: unrecognised star command
    equb <(fscv_2_star_run-1)                                         ; 803c: db          .              ; lo - FSCV 4: *RUN
    equb <(fscv_5_cat-1)                                              ; 803d: 66          f              ; lo - FSCV 5: *CAT
    equb <(fscv_6_shutdown-1)                                         ; 803e: 50          P              ; lo - FSCV 6: shutdown
    equb <(fscv_7_read_handles-1)                                     ; 803f: ca          .              ; lo - FSCV 7: read handle range
    equb <(fsreply_0_print_dir-1)                                     ; 8040: 95          .              ; lo - FS reply: print directory name
    equb <(fsreply_1_copy_handles_boot-1)                             ; 8041: 37          7              ; lo - FS reply: copy handles + boot
    equb <(fsreply_2_copy_handles-1)                                  ; 8042: 38          8              ; lo - FS reply: copy handles
    equb <(fsreply_3_set_csd-1)                                       ; 8043: 31          1              ; lo - FS reply: set CSD handle
    equb <(fsreply_4_notify_exec-1)                                   ; 8044: e1          .              ; lo - FS reply: notify + execute
    equb <(fsreply_5_set_lib-1)                                       ; 8045: 2c          ,              ; lo - FS reply: set library handle
    equb <(net_1_read_handle-1)                                       ; 8046: 66          f              ; lo - *NET1: read handle from packet
    equb <(net_2_read_handle_entry-1)                                 ; 8047: 6c          l              ; lo - *NET2: read handle from workspace
    equb <(net_3_close_handle-1)                                      ; 8048: 7c          |              ; lo - *NET3: close handle
; &8049 referenced 1 time by &80ec
    equb <(net_4_resume_remote-1)                                     ; 8049: bb          .              ; lo - *NET4: resume remote
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_0_lo (&8025). Together they form a table
; of 37 handler addresses, used via the PHA/PHA/RTS trick at
; &80E7.
.dispatch_0_hi
    equb >(return_1-1)                                                ; 804a: 80          .              ; hi - Svc 0: already claimed (no-op)
    equb >(svc_1_abs_workspace-1)                                     ; 804b: 82          .              ; hi - Svc 1: absolute workspace
    equb >(svc_2_private_workspace-1)                                 ; 804c: 82          .              ; hi - Svc 2: private workspace
    equb >(svc_3_autoboot-1)                                          ; 804d: 82          .              ; hi - Svc 3: auto-boot
    equb >(svc_4_star_command-1)                                      ; 804e: 81          .              ; hi - Svc 4: unrecognised star command
    equb >(sub_c963c-1)                                               ; 804f: 96          .              ; hi - Svc 5: unrecognised interrupt
    equb >(return_1-1)                                                ; 8050: 80          .              ; hi - Svc 6: BRK (no-op)
    equb >(dispatch_net_cmd-1)                                        ; 8051: 80          .              ; hi - Svc 7: unrecognised OSBYTE
    equb >(svc_8_osword-1)                                            ; 8052: 8e          .              ; hi - Svc 8: unrecognised OSWORD
    equb >(svc_9_help-1)                                              ; 8053: 82          .              ; hi - Svc 9: *HELP
    equb >(return_1-1)                                                ; 8054: 80          .              ; hi - Svc 10: static workspace (no-op)
    equb >(sub_c9639-1)                                               ; 8055: 96          .              ; hi - Svc 11: NMI release (reclaim NMIs)
    equb >(sub_c9636-1)                                               ; 8056: 96          .              ; hi - Svc 12: NMI claim (save NMI state)
    equb >(svc_13_select_nfs-1)                                       ; 8057: 81          .              ; hi - Svc 13: select NFS (intercepted before dispatch)
    equb >(lang_0_insert_remote_key-1)                                ; 8058: 84          .              ; hi - Lang 0: no language / Tube
    equb >(lang_1_remote_boot-1)                                      ; 8059: 84          .              ; hi - Lang 1: normal startup
    equb >(lang_2_save_palette_vdu-1)                                 ; 805a: 92          .              ; hi - Lang 2: softkey byte (Electron)
    equb >(lang_3_execute_at_0100-1)                                  ; 805b: 84          .              ; hi - Lang 3: softkey length (Electron)
    equb >(lang_4_remote_validated-1)                                 ; 805c: 84          .              ; hi - Lang 4: remote validated
    equb >(fscv_0_opt_entry-1)                                        ; 805d: 8a          .              ; hi - FSCV 0: *OPT
    equb >(fscv_1_eof-1)                                              ; 805e: 88          .              ; hi - FSCV 1: EOF check
    equb >(fscv_2_star_run-1)                                         ; 805f: 8d          .              ; hi - FSCV 2: */ (run)
    equb >(fscv_3_star_cmd-1)                                         ; 8060: 8c          .              ; hi - FSCV 3: unrecognised star command
    equb >(fscv_2_star_run-1)                                         ; 8061: 8d          .              ; hi - FSCV 4: *RUN
    equb >(fscv_5_cat-1)                                              ; 8062: 8c          .              ; hi - FSCV 5: *CAT
    equb >(fscv_6_shutdown-1)                                         ; 8063: 83          .              ; hi - FSCV 6: shutdown
    equb >(fscv_7_read_handles-1)                                     ; 8064: 86          .              ; hi - FSCV 7: read handle range
    equb >(fsreply_0_print_dir-1)                                     ; 8065: 8d          .              ; hi - FS reply: print directory name
    equb >(fsreply_1_copy_handles_boot-1)                             ; 8066: 8e          .              ; hi - FS reply: copy handles + boot
    equb >(fsreply_2_copy_handles-1)                                  ; 8067: 8e          .              ; hi - FS reply: copy handles
    equb >(fsreply_3_set_csd-1)                                       ; 8068: 8e          .              ; hi - FS reply: set CSD handle
    equb >(fsreply_4_notify_exec-1)                                   ; 8069: 8d          .              ; hi - FS reply: notify + execute
    equb >(fsreply_5_set_lib-1)                                       ; 806a: 8e          .              ; hi - FS reply: set library handle
    equb >(net_1_read_handle-1)                                       ; 806b: 8e          .              ; hi - *NET1: read handle from packet
    equb >(net_2_read_handle_entry-1)                                 ; 806c: 8e          .              ; hi - *NET2: read handle from workspace
    equb >(net_3_close_handle-1)                                      ; 806d: 8e          .              ; hi - *NET3: close handle
    equb >(net_4_resume_remote-1)                                     ; 806e: 81          .              ; hi - *NET4: resume remote

; ***************************************************************************************
; *NET command dispatcher
; 
; Parses the character after *NET as '1'-'4', maps to table
; indices 33-36 via base offset Y=&21, and dispatches via &80E7.
; Characters outside '1'-'4' fall through to return_1 (RTS).
; 
; These are internal sub-commands used only by the ROM itself,
; not user-accessible star commands. The MOS command parser
; requires a space or terminator after 'NET', so *NET1 typed
; at the command line does not match; these are reached only
; via OSCLI calls within the ROM.
; 
; *NET1 (&8E59): read file handle from received
; packet (net_1_read_handle)
; 
; *NET2 (&8E5F): read handle entry from workspace
; (net_2_read_handle_entry)
; 
; *NET3 (&8E6F): close handle / mark as unused
; (net_3_close_handle)
; 
; *NET4 (&81B8): resume after remote operation
; (net_4_resume_remote)
; ***************************************************************************************
.dispatch_net_cmd
    lda l00ef                                                         ; 806f: a5 ef       ..             ; Read command character following *NET
    sbc #&31 ; '1'                                                    ; 8071: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    cmp #4                                                            ; 8073: c9 04       ..
    bcs c80e3                                                         ; 8075: b0 6c       .l
    tax                                                               ; 8077: aa          .
    lda #0                                                            ; 8078: a9 00       ..
    sta l00a9                                                         ; 807a: 85 a9       ..
    tya                                                               ; 807c: 98          .
    ldy #&21 ; '!'                                                    ; 807d: a0 21       .!             ; Y=&21: base offset for *NET commands (index 33+)
    bne dispatch                                                      ; 807f: d0 66       .f             ; ALWAYS branch

; &8081 referenced 1 time by &8086
.loop_c8081
    iny                                                               ; 8081: c8          .
; ***************************************************************************************
; "I AM" command handler
; 
; Dispatched from the command match table when the user types
; "*I AM <station>" or "*I AM <network>.<station>". Also used as
; the station number parser for "*NET <network>.<station>".
; Skips leading spaces, then calls parse_decimal for the first
; number. If a dot separator was found (carry set), it stores the
; result directly as the network (&0E01) and calls parse_decimal
; again for the station (&0E00). With a single number, it is stored
; as the station and the network defaults to 0 (local). If a colon
; follows, reads interactive input via OSRDCH and appends it to
; the command buffer. Finally jumps to forward_star_cmd.
; ***************************************************************************************
.i_am_handler
    lda (fs_options),y                                                ; 8082: b1 bb       ..
    cmp #&20 ; ' '                                                    ; 8084: c9 20       .
    beq loop_c8081                                                    ; 8086: f0 f9       ..
    cmp #&3a ; ':'                                                    ; 8088: c9 3a       .:             ; Colon = interactive remote command prefix
    bcs c809d                                                         ; 808a: b0 11       ..
    jsr parse_decimal                                                 ; 808c: 20 77 86     w.            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc c8098                                                         ; 808f: 90 07       ..             ; C=1: dot found, first number was network
    sta fs_server_net                                                 ; 8091: 8d 01 0e    ...            ; Store network number (n.s = network.station); A=parsed value (accumulated in &B2)
    iny                                                               ; 8094: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8095: 20 77 86     w.            ; Parse decimal number from (fs_options),Y (DECIN)
; &8098 referenced 1 time by &808f
.c8098
    beq c809d                                                         ; 8098: f0 03       ..             ; Z=1: no station parsed (empty or non-numeric)
    sta fs_server_stn                                                 ; 809a: 8d 00 0e    ...            ; A=parsed value (accumulated in &B2)
; &809d referenced 2 times by &808a, &8098
.c809d
    jsr infol2                                                        ; 809d: 20 82 8d     ..
; &80a0 referenced 2 times by &80a8, &80bf
.c80a0
    dey                                                               ; 80a0: 88          .              ; Scan backward for ':' (interactive prefix)
    beq c80c5                                                         ; 80a1: f0 22       ."
    lda fs_cmd_data,y                                                 ; 80a3: b9 05 0f    ...
    cmp #&3a ; ':'                                                    ; 80a6: c9 3a       .:
    bne c80a0                                                         ; 80a8: d0 f6       ..
    jsr oswrch                                                        ; 80aa: 20 ee ff     ..            ; Echo colon, then read user input from keyboard; Write character
; &80ad referenced 1 time by &80ba
.loop_c80ad
    jsr sub_c84a1                                                     ; 80ad: 20 a1 84     ..
    jsr osrdch                                                        ; 80b0: 20 e0 ff     ..            ; Read a character from the current input stream
    sta fs_cmd_data,y                                                 ; 80b3: 99 05 0f    ...            ; Append typed character to command buffer; A=character read
    iny                                                               ; 80b6: c8          .
    inx                                                               ; 80b7: e8          .
    cmp #&0d                                                          ; 80b8: c9 0d       ..
    bne loop_c80ad                                                    ; 80ba: d0 f1       ..
    jsr osnewl                                                        ; 80bc: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
    bne c80a0                                                         ; 80bf: d0 df       ..
; ***************************************************************************************
; Forward unrecognised * command to fileserver (COMERR)
; 
; Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
; prepares an FS command with function code 0, and sends it to the
; fileserver to request decoding. The server returns a command code
; indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
; 5=load-as-command). This mechanism allows the fileserver to extend
; the client's command set without ROM updates. Called from the "I."
; and catch-all entries in the command match table at &8C4B, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; ***************************************************************************************
.forward_star_cmd
    jsr infol2                                                        ; 80c1: 20 82 8d     ..
    tay                                                               ; 80c4: a8          .              ; Y=function code for HDRFN
; &80c5 referenced 1 time by &80a1
.c80c5
    jsr prepare_fs_cmd                                                ; 80c5: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    ldx fs_cmd_csd                                                    ; 80c8: ae 03 0f    ...            ; X=depends on function
    beq return_1                                                      ; 80cb: f0 29       .)
    lda fs_cmd_data                                                   ; 80cd: ad 05 0f    ...            ; A=function code (0-7)
    ldy #&17                                                          ; 80d0: a0 17       ..             ; Y=depends on function
    bne dispatch                                                      ; 80d2: d0 13       ..             ; ALWAYS branch

; ***************************************************************************************
; FSCV dispatch entry
; 
; Entered via the extended vector table when the MOS calls FSCV.
; Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
; and dispatches codes 0-7 via the shared dispatch table at &8024
; with base offset Y=&13 (table indices 20-27).
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
    jsr save_fscv_args_with_ptrs                                      ; 80d4: 20 49 86     I.            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 80d7: c9 08       ..
    bcs return_1                                                      ; 80d9: b0 1b       ..             ; Function code >= 8? Return (unsupported)
    tax                                                               ; 80db: aa          .
    tya                                                               ; 80dc: 98          .
    ldy #&13                                                          ; 80dd: a0 13       ..             ; Y=&13: base offset for FSCV dispatch (indices 20+)
    bne dispatch                                                      ; 80df: d0 06       ..             ; ALWAYS branch

; ***************************************************************************************
; Language entry dispatcher
; 
; Called when the NFS ROM is entered as a language. Although rom_type
; (&82) does not set the language bit, the MOS enters this point
; after NFS claims service &FE (Tube post-init). X = reason code
; (0-4). Dispatches via table indices 15-19 (base offset Y=&0E).
; ***************************************************************************************
; &80e1 referenced 1 time by &8000
.language_handler
    cpx #5                                                            ; 80e1: e0 05       ..
; &80e3 referenced 1 time by &8075
.c80e3
    bcs return_1                                                      ; 80e3: b0 11       ..
    ldy #&0e                                                          ; 80e5: a0 0e       ..             ; Y=&0E: base offset for language handlers (index 15+)
; ***************************************************************************************
; PHA/PHA/RTS computed dispatch
; 
; X = command index within caller's group (e.g. service number)
; Y = base offset into dispatch table (0, &0E, &13, &21, etc.)
; The loop adds Y+1 to X, so final X = command index + base + 1.
; Then high and low bytes of (handler-1) are pushed onto the stack,
; and RTS pops them and jumps to handler_address.
; 
; This is a standard 6502 trick: RTS increments the popped address
; by 1 before jumping, so the table stores (address - 1) to
; compensate. Multiple callers share one table via different Y
; base offsets.
; ***************************************************************************************
; &80e7 referenced 5 times by &807f, &80d2, &80df, &80e9, &81a1
.dispatch
    inx                                                               ; 80e7: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80e8: 88          .
    bpl dispatch                                                      ; 80e9: 10 fc       ..
    tay                                                               ; 80eb: a8          .
    lda dispatch_0_hi-1,x                                             ; 80ec: bd 49 80    .I.            ; Load high byte of (handler - 1) from table
    pha                                                               ; 80ef: 48          H              ; Push high byte onto stack
    lda dispatch_0_lo-1,x                                             ; 80f0: bd 24 80    .$.            ; Load low byte of (handler - 1) from table
    pha                                                               ; 80f3: 48          H              ; Push low byte onto stack
    ldx fs_options                                                    ; 80f4: a6 bb       ..             ; Restore X (fileserver options) for use by handler
; &80f6 referenced 3 times by &80cb, &80d9, &80e3
.return_1
    rts                                                               ; 80f6: 60          `              ; RTS pops address, adds 1, jumps to handler

; &80f7 referenced 1 time by &8003
.service_handler
    nop                                                               ; 80f7: ea          .              ; 9 NOPs: bus settling time for ADLC probe
    nop                                                               ; 80f8: ea          .
    nop                                                               ; 80f9: ea          .
    nop                                                               ; 80fa: ea          .
    nop                                                               ; 80fb: ea          .
    nop                                                               ; 80fc: ea          .
    nop                                                               ; 80fd: ea          .
    nop                                                               ; 80fe: ea          .
    nop                                                               ; 80ff: ea          .
    pha                                                               ; 8100: 48          H
    cmp #1                                                            ; 8101: c9 01       ..             ; Only probe ADLC on service 1 (workspace claim)
    bne c811a                                                         ; 8103: d0 15       ..
    lda econet_control1_or_status1                                    ; 8105: ad a0 fe    ...            ; Probe ADLC SR1: non-zero = already initialised
    and #&ed                                                          ; 8108: 29 ed       ).
    bne c8113                                                         ; 810a: d0 07       ..
    lda econet_control23_or_status2                                   ; 810c: ad a1 fe    ...            ; Probe ADLC SR2 if SR1 was all zeros
    and #&db                                                          ; 810f: 29 db       ).
    beq c811a                                                         ; 8111: f0 07       ..
; &8113 referenced 1 time by &810a
.c8113
    rol l0df0,x                                                       ; 8113: 3e f0 0d    >..            ; Set bit 7 of per-ROM workspace = disable flag
    sec                                                               ; 8116: 38          8
    ror l0df0,x                                                       ; 8117: 7e f0 0d    ~..
; &811a referenced 2 times by &8103, &8111
.c811a
    lda l0df0,x                                                       ; 811a: bd f0 0d    ...            ; Read back flag; ASL puts bit 7 into carry
    asl a                                                             ; 811d: 0a          .
    pla                                                               ; 811e: 68          h
    bmi c8123                                                         ; 811f: 30 02       0.             ; Service >= &80: always handle (Tube/init)
    bcs c8191                                                         ; 8121: b0 6e       .n             ; C=1 (ADLC active): duplicate ROM, skip
; ***************************************************************************************
; Service handler entry
; 
; Preamble at &80F7 (9 NOPs + ADLC probe): on service 1 only,
; probes ADLC status registers &FEA0/&FEA1 to detect whether
; Econet hardware has already been initialised by another ROM.
; If active ADLC bits found, sets bit 7 of per-ROM workspace
; as a disable flag. For services < &80, the flag causes an
; early return (disabling this ROM as a duplicate). Services
; >= &80 (&FE, &FF) are always handled regardless of flag.
; 
; Intercepts three service calls before normal dispatch:
;   &FE: Tube init — explode character definitions
;   &FF: Full init — vector setup, copy code to RAM, select NFS
;   &12 (Y=5): Select NFS as active filing system
; All other service calls < &0D dispatch via c8146.
; 
; 3.40 change: replaced 3.35D's per-ROM disable flag at &80EA
; with ADLC register probing (3.35K had removed the check
; entirely). The 9 NOPs at &80F7 provide bus settling time.
; ***************************************************************************************
; &8123 referenced 1 time by &811f
.c8123
    cmp #&fe                                                          ; 8123: c9 fe       ..
    bcc c8183                                                         ; 8125: 90 5c       .\
    bne init_vectors_and_copy                                         ; 8127: d0 1b       ..
    cpy #0                                                            ; 8129: c0 00       ..
    beq c8183                                                         ; 812b: f0 56       .V
    ldx #6                                                            ; 812d: a2 06       ..
    lda #osbyte_explode_chars                                         ; 812f: a9 14       ..
    jsr osbyte                                                        ; 8131: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
; &8134 referenced 2 times by &8137, &8141
.c8134
    bit tube_status_1_and_tube_control                                ; 8134: 2c e0 fe    ,..
    bpl c8134                                                         ; 8137: 10 fb       ..
    lda tube_data_register_1                                          ; 8139: ad e1 fe    ...
    beq c8181                                                         ; 813c: f0 43       .C
    jsr oswrch                                                        ; 813e: 20 ee ff     ..            ; Write character
    jmp c8134                                                         ; 8141: 4c 34 81    L4.

; &8144 referenced 1 time by &8127
.init_vectors_and_copy
    lda #&ad                                                          ; 8144: a9 ad       ..
    sta evntv                                                         ; 8146: 8d 20 02    . .
    lda #6                                                            ; 8149: a9 06       ..
    sta evntv+1                                                       ; 814b: 8d 21 02    .!.
    lda #&16                                                          ; 814e: a9 16       ..
    sta brkv                                                          ; 8150: 8d 02 02    ...
    lda #0                                                            ; 8153: a9 00       ..
    sta brkv+1                                                        ; 8155: 8d 03 02    ...
    lda #&8e                                                          ; 8158: a9 8e       ..
    sta tube_status_1_and_tube_control                                ; 815a: 8d e0 fe    ...
    ldy #0                                                            ; 815d: a0 00       ..
; Copy NMI handler code from ROM to RAM pages &04-&06
; &815f referenced 1 time by &8172
.cloop
    lda c9362,y                                                       ; 815f: b9 62 93    .b.
    sta tube_code_page4,y                                             ; 8162: 99 00 04    ...
    lda l9462,y                                                       ; 8165: b9 62 94    .b.
    sta tube_dispatch_table,y                                         ; 8168: 99 00 05    ...
    lda l9562,y                                                       ; 816b: b9 62 95    .b.
    sta l0600,y                                                       ; 816e: 99 00 06    ...
    dey                                                               ; 8171: 88          .
    bne cloop                                                         ; 8172: d0 eb       ..
    jsr tube_post_init                                                ; 8174: 20 21 04     !.
    ldx #&60 ; '`'                                                    ; 8177: a2 60       .`
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &8179 referenced 1 time by &817f
.loop_c8179
    lda c9321,x                                                       ; 8179: bd 21 93    .!.
    sta nmi_workspace_start,x                                         ; 817c: 95 16       ..
    dex                                                               ; 817e: ca          .
    bpl loop_c8179                                                    ; 817f: 10 f8       ..
; &8181 referenced 1 time by &813c
.c8181
    lda #0                                                            ; 8181: a9 00       ..
; &8183 referenced 2 times by &8125, &812b
.c8183
    cmp #&12                                                          ; 8183: c9 12       ..
    bne c818f                                                         ; 8185: d0 08       ..
    cpy #5                                                            ; 8187: c0 05       ..
    bne c818f                                                         ; 8189: d0 04       ..
    lda #&0d                                                          ; 818b: a9 0d       ..
    bne c8193                                                         ; 818d: d0 04       ..             ; ALWAYS branch

; &818f referenced 2 times by &8185, &8189
.c818f
    cmp #&0d                                                          ; 818f: c9 0d       ..
; &8191 referenced 1 time by &8121
.c8191
    bcs return_2                                                      ; 8191: b0 1c       ..
; &8193 referenced 1 time by &818d
.c8193
    tax                                                               ; 8193: aa          .
    lda l00a9                                                         ; 8194: a5 a9       ..
    pha                                                               ; 8196: 48          H
    lda l00a8                                                         ; 8197: a5 a8       ..
    pha                                                               ; 8199: 48          H
    stx l00a9                                                         ; 819a: 86 a9       ..
    sty l00a8                                                         ; 819c: 84 a8       ..
    tya                                                               ; 819e: 98          .
    ldy #0                                                            ; 819f: a0 00       ..
    jsr dispatch                                                      ; 81a1: 20 e7 80     ..
    ldx l00a9                                                         ; 81a4: a6 a9       ..
    pla                                                               ; 81a6: 68          h
    sta l00a8                                                         ; 81a7: 85 a8       ..
; ***************************************************************************************
; Service 4: unrecognised * command
; 
; The first 7 bytes (&81A5-&81AB) are the service handler epilogue:
; PLA/STA restores &A9, TXA/LDX retrieves romsel_copy, then RTS.
; This is the return path reached after any dispatched service
; handler completes.
; 
; The service 4 handler itself is dispatched via the table to
; &81B1 (after 5 NOPs of padding). It makes two match_rom_string
; calls against the ROM header, reusing header bytes as command
; strings:
; 
;   X=&0C: matches "ROFF" at &8014 — the suffix of the
;          copyright string "(C)ROFF" → *ROFF (Remote Off,
;          end remote session) — falls through to net_4_resume_remote
; 
;   X=5: matches "NET" at &800D — the ROM title suffix
;        → *NET (select NFS) — falls through to svc_13_select_nfs
; 
; If neither matches, returns with the service call
; unclaimed.
; ***************************************************************************************
.svc_star_command
    pla                                                               ; 81a9: 68          h
    sta l00a9                                                         ; 81aa: 85 a9       ..
    txa                                                               ; 81ac: 8a          .
    ldx romsel_copy                                                   ; 81ad: a6 f4       ..
; &81af referenced 1 time by &8191
.return_2
    rts                                                               ; 81af: 60          `

    nop                                                               ; 81b0: ea          .
    nop                                                               ; 81b1: ea          .
    nop                                                               ; 81b2: ea          .
    nop                                                               ; 81b3: ea          .
    nop                                                               ; 81b4: ea          .
.svc_4_star_command
    ldx #&0c                                                          ; 81b5: a2 0c       ..
    jsr match_rom_string                                              ; 81b7: 20 62 83     b.
    bne c81ea                                                         ; 81ba: d0 2e       ..
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
    ldy #4                                                            ; 81bc: a0 04       ..
    lda (net_rx_ptr),y                                                ; 81be: b1 9c       ..
    beq c81e3                                                         ; 81c0: f0 21       .!
    lda #0                                                            ; 81c2: a9 00       ..
    tax                                                               ; 81c4: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 81c5: 91 9c       ..
    tay                                                               ; 81c7: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 81c8: a9 c9       ..
    jsr osbyte                                                        ; 81ca: 20 f4 ff     ..            ; Enable keyboard (for Econet)
    lda #&0a                                                          ; 81cd: a9 0a       ..
    jsr setup_tx_and_send                                             ; 81cf: 20 c4 90     ..
; &81d2 referenced 1 time by &84ce
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 81d2: 86 9e       ..
    lda #&ce                                                          ; 81d4: a9 ce       ..
; &81d6 referenced 1 time by &81e1
.loop_c81d6
    ldx nfs_workspace                                                 ; 81d6: a6 9e       ..
    ldy #&7f                                                          ; 81d8: a0 7f       ..
    jsr osbyte                                                        ; 81da: 20 f4 ff     ..
    adc #1                                                            ; 81dd: 69 01       i.
    cmp #&d0                                                          ; 81df: c9 d0       ..
.cmd_name_matched
    beq loop_c81d6                                                    ; 81e1: f0 f3       ..
; &81e3 referenced 1 time by &81c0
.c81e3
    lda #0                                                            ; 81e3: a9 00       ..
    sta l00a9                                                         ; 81e5: 85 a9       ..
.skpspi
    sta nfs_workspace                                                 ; 81e7: 85 9e       ..
    rts                                                               ; 81e9: 60          `

; &81ea referenced 1 time by &81ba
.c81ea
    ldx #5                                                            ; 81ea: a2 05       ..
    jsr match_rom_string                                              ; 81ec: 20 62 83     b.
    bne c8215                                                         ; 81ef: d0 24       .$
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
; claimed) to notify other ROMs. If nfs_temp is zero (auto-boot
; not inhibited), injects the synthetic command "I .BOOT" through
; the command decoder to trigger auto-boot login.
; ***************************************************************************************
.svc_13_select_nfs
    jsr call_fscv_shutdown                                            ; 81f1: 20 18 82     ..
    sec                                                               ; 81f4: 38          8
    ror l00a8                                                         ; 81f5: 66 a8       f.
    jsr issue_vectors_claimed                                         ; 81f7: 20 7b 82     {.
    ldy #&1d                                                          ; 81fa: a0 1d       ..
; &81fc referenced 1 time by &8204
.initl
    lda (net_rx_ptr),y                                                ; 81fc: b1 9c       ..
    sta fs_state_deb,y                                                ; 81fe: 99 eb 0d    ...
    dey                                                               ; 8201: 88          .
    cpy #&14                                                          ; 8202: c0 14       ..
    bne initl                                                         ; 8204: d0 f6       ..
    beq init_fs_vectors                                               ; 8206: f0 5c       .\             ; ALWAYS branch

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_9_help
    jsr print_inline                                                  ; 8208: 20 5c 86     \.
    equs &0d, "NFS 3.60", &0d                                         ; 820b: 0d 4e 46... .NF

; &8215 referenced 2 times by &81ef, &822a
.c8215
    ldy l00a8                                                         ; 8215: a4 a8       ..
    rts                                                               ; 8217: 60          `

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &8218 referenced 2 times by &81f1, &821d
.call_fscv_shutdown
    lda #6                                                            ; 8218: a9 06       ..
    jmp (fscv)                                                        ; 821a: 6c 1e 02    l..

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
    jsr call_fscv_shutdown                                            ; 821d: 20 18 82     ..
    lda #osbyte_scan_keyboard_from_16                                 ; 8220: a9 7a       .z
    jsr osbyte                                                        ; 8222: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 8225: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi print_station_info                                            ; 8226: 30 0a       0.
; ***************************************************************************************
; Check boot key
; 
; Checks if the pressed key (in A) is 'N' (matrix address &55). If
; not 'N', returns to the MOS without claiming the service call
; (another ROM may boot instead). If 'N', forgets the keypress via
; OSBYTE &78 and falls through to print_station_info.
; ***************************************************************************************
.check_boot_key
    eor #&55 ; 'U'                                                    ; 8228: 49 55       IU
    bne c8215                                                         ; 822a: d0 e9       ..
    tay                                                               ; 822c: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 822d: a9 78       .x
    jsr osbyte                                                        ; 822f: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; ***************************************************************************************
; Print station identification
; 
; Prints "Econet Station <n>" using the station number from the net
; receive buffer, then tests ADLC SR2 for the network clock signal —
; prints " No Clock" if absent. Falls through to init_fs_vectors.
; ***************************************************************************************
; &8232 referenced 1 time by &8226
.print_station_info
    jsr print_inline                                                  ; 8232: 20 5c 86     \.
    equs "Econet Station "                                            ; 8235: 45 63 6f... Eco

    ldy #&14                                                          ; 8244: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8246: b1 9c       ..
    jsr print_decimal                                                 ; 8248: 20 bd 8d     ..
    lda #&20 ; ' '                                                    ; 824b: a9 20       .              ; BIT trick: bit 5 of SR2 = clock present
    bit econet_control23_or_status2                                   ; 824d: 2c a1 fe    ,..
.dofsl1
    beq c825f                                                         ; 8250: f0 0d       ..
    jsr print_inline                                                  ; 8252: 20 5c 86     \.
    equs " No Clock"                                                  ; 8255: 20 4e 6f...  No

    nop                                                               ; 825e: ea          .
; &825f referenced 1 time by &8250
.c825f
    jsr print_inline                                                  ; 825f: 20 5c 86     \.
    equs &0d, &0d                                                     ; 8262: 0d 0d       ..

; ***************************************************************************************
; Initialise filing system vectors
; 
; Copies 14 bytes from l829a (&829A) into FILEV-FSCV (&0212),
; setting all 7 filing system vectors to the extended vector dispatch
; addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
; ROM pointer table entries with the actual NFS handler addresses. Also
; reached directly from svc_13_select_nfs, bypassing the station display.
; Falls through to issue_vectors_claimed.
; ***************************************************************************************
; &8264 referenced 1 time by &8206
.init_fs_vectors
    ldy #&0d                                                          ; 8264: a0 0d       ..             ; Copy 14 bytes: FS vector addresses to FILEV-FSCV
; &8266 referenced 1 time by &826d
.loop_c8266
    lda l829a,y                                                       ; 8266: b9 9a 82    ...
    sta filev,y                                                       ; 8269: 99 12 02    ...
    dey                                                               ; 826c: 88          .
    bpl loop_c8266                                                    ; 826d: 10 f7       ..
    jsr setup_rom_ptrs_netv                                           ; 826f: 20 25 83     %.
    ldy #&1b                                                          ; 8272: a0 1b       ..             ; Install 7 handler entries in ROM ptr table
    ldx #7                                                            ; 8274: a2 07       ..
    jsr store_rom_ptr_pair                                            ; 8276: 20 39 83     9.
    stx l00a9                                                         ; 8279: 86 a9       ..             ; X=0 after loop; store as workspace offset
; ***************************************************************************************
; Issue 'vectors claimed' service and optionally auto-boot
; 
; Issues service &0F (vectors claimed) via OSBYTE &8F, then
; service &0A. If l00a8 is zero (soft break — RXCBs already
; initialised), sets up the command string "I .BOOT" at &828E
; and jumps to the FSCV 3 unrecognised-command handler (which
; matches against the command table at &8C4B). The "I." prefix
; triggers the catch-all entry which forwards the command to
; the fileserver. Falls through to run_fscv_cmd.
; ***************************************************************************************
; &827b referenced 1 time by &81f7
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 827b: a9 8f       ..
    ldx #&0f                                                          ; 827d: a2 0f       ..
    jsr osbyte                                                        ; 827f: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 8282: a2 0a       ..
    jsr osbyte                                                        ; 8284: 20 f4 ff     ..            ; Issue service &0A
    ldx l00a8                                                         ; 8287: a6 a8       ..             ; Non-zero after hard reset: skip auto-boot
    bne return_3                                                      ; 8289: d0 37       .7
    ldx #&92                                                          ; 828b: a2 92       ..             ; X = lo byte of auto-boot string at &8292
; ***************************************************************************************
; Run FSCV command from ROM
; 
; Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
; to execute the command string at (X, Y). X is pre-loaded by the
; caller with the low byte of the string address. Also used as a
; data base address by store_rom_ptr_pair for Y-indexed access to
; the handler address table.
; ***************************************************************************************
; &828d referenced 2 times by &8339, &833f
.run_fscv_cmd
    equb &a0                                                          ; 828d: a0          .
; Synthetic auto-boot command string. "I " does not match any
; entry in NFS's local command table — "I." requires a dot, and
; "I AM" requires 'A' after the space — so fscv_3_star_cmd
; forwards the entire string to the fileserver, which executes
; the .BOOT file.
    equs &82, "L", &1b, &8c, "I .B"                                   ; 828e: 82 4c 1b... .L.
    equb &4f, &4f                                                     ; 8296: 4f 4f       OO             ; Auto-boot string tail / NETV handler data
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
.fs_vector_addrs
    equb &54, &0d                                                     ; 8298: 54 0d       T.             ; Auto-boot string tail / NETV handler data
; &829a referenced 1 time by &8266
.l829a
    equb &1b, &ff                                                     ; 829a: 1b ff       ..             ; FILEV dispatch (&FF1B)
    equb &1e, &ff                                                     ; 829c: 1e ff       ..             ; ARGSV dispatch (&FF1E)
    equb &21, &ff                                                     ; 829e: 21 ff       !.             ; BGETV dispatch (&FF21)
    equb &24, &ff                                                     ; 82a0: 24 ff       $.             ; BPUTV dispatch (&FF24)
    equb &27, &ff                                                     ; 82a2: 27 ff       '.             ; GBPBV dispatch (&FF27)
    equb &2a, &ff                                                     ; 82a4: 2a ff       *.             ; FINDV dispatch (&FF2A)
    equb &2d, &ff                                                     ; 82a6: 2d ff       -.             ; FSCV dispatch (&FF2D)
    equb &0c                                                          ; 82a8: 0c          .              ; FILEV handler lo (&870C)
    equb &87                                                          ; 82a9: 87          .              ; FILEV handler hi
    equb &4a                                                          ; 82aa: 4a          J              ; (ROM bank — not read)
    equb &68                                                          ; 82ab: 68          h              ; ARGSV handler lo (&8968)
    equb &89                                                          ; 82ac: 89          .              ; ARGSV handler hi
    equb &44                                                          ; 82ad: 44          D              ; (ROM bank — not read)
    equb &63                                                          ; 82ae: 63          c              ; BGETV handler lo (&8563)
    equb &85                                                          ; 82af: 85          .              ; BGETV handler hi
    equb &57                                                          ; 82b0: 57          W              ; (ROM bank — not read)
    equb &13                                                          ; 82b1: 13          .              ; BPUTV handler lo (&8413)
    equb &84                                                          ; 82b2: 84          .              ; BPUTV handler hi
    equb &42                                                          ; 82b3: 42          B              ; (ROM bank — not read)
    equb &72                                                          ; 82b4: 72          r              ; GBPBV handler lo (&8A72)
    equb &8a                                                          ; 82b5: 8a          .              ; GBPBV handler hi
    equb &41                                                          ; 82b6: 41          A              ; (ROM bank — not read)
    equb &d8                                                          ; 82b7: d8          .              ; FINDV handler lo (&89D8)
    equb &89                                                          ; 82b8: 89          .              ; FINDV handler hi
    equb &52                                                          ; 82b9: 52          R              ; (ROM bank — not read)
    equb &d4                                                          ; 82ba: d4          .              ; FSCV handler lo (&80D4)
    equb &80                                                          ; 82bb: 80          .              ; FSCV handler hi

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; ***************************************************************************************
.svc_1_abs_workspace
    cpy #&10                                                          ; 82bc: c0 10       ..
    bcs return_3                                                      ; 82be: b0 02       ..
    ldy #&10                                                          ; 82c0: a0 10       ..
; &82c2 referenced 2 times by &8289, &82be
.return_3
    rts                                                               ; 82c2: 60          `

    equb &80, &90                                                     ; 82c3: 80 90       ..

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
;   - Sets FS server station to &FE (no server selected)
;   - Sets printer server station to &FE (no server selected)
;   - Clears FS handles, OPT byte, message flag, SEQNOS
;   - Initialises all RXCBs with &3F flag (available)
; In both cases: reads station ID from &FE18 (only valid during
; reset), calls adlc_init, enables user-level RX (LFLAG=&40).
; ***************************************************************************************
.svc_2_private_workspace
    sty net_rx_ptr_hi                                                 ; 82c5: 84 9d       ..
    iny                                                               ; 82c7: c8          .
    sty nfs_workspace_hi                                              ; 82c8: 84 9f       ..
    lda #0                                                            ; 82ca: a9 00       ..
    ldy #4                                                            ; 82cc: a0 04       ..
    sta (net_rx_ptr),y                                                ; 82ce: 91 9c       ..             ; Clear status byte in net receive buffer
    ldy #&ff                                                          ; 82d0: a0 ff       ..
    sta net_rx_ptr                                                    ; 82d2: 85 9c       ..
    sta nfs_workspace                                                 ; 82d4: 85 9e       ..
    sta l00a8                                                         ; 82d6: 85 a8       ..
    sta tx_clear_flag                                                 ; 82d8: 8d 62 0d    .b.
    tax                                                               ; 82db: aa          .              ; X=&00
    lda #osbyte_read_write_last_break_type                            ; 82dc: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 82de: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 82e1: 8a          .              ; X=value of type of last reset
    beq c8316                                                         ; 82e2: f0 32       .2             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 82e4: a0 15       ..
    lda #&fe                                                          ; 82e6: a9 fe       ..
    sta fs_server_stn                                                 ; 82e8: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 82eb: 91 9c       ..
    lda #0                                                            ; 82ed: a9 00       ..
    sta fs_server_net                                                 ; 82ef: 8d 01 0e    ...
    sta prot_status                                                   ; 82f2: 8d 63 0d    .c.
    sta fs_messages_flag                                              ; 82f5: 8d 06 0e    ...
    sta fs_boot_option                                                ; 82f8: 8d 05 0e    ...
    iny                                                               ; 82fb: c8          .              ; Y=&16
    sta (net_rx_ptr),y                                                ; 82fc: 91 9c       ..
    ldy #3                                                            ; 82fe: a0 03       ..             ; Init printer server: station &FE, net 0
    sta (nfs_workspace),y                                             ; 8300: 91 9e       ..
    dey                                                               ; 8302: 88          .              ; Y=&02
    lda #&fe                                                          ; 8303: a9 fe       ..
    sta (nfs_workspace),y                                             ; 8305: 91 9e       ..
; &8307 referenced 1 time by &8314
.loop_c8307
    lda l00a8                                                         ; 8307: a5 a8       ..
    jsr calc_handle_offset                                            ; 8309: 20 55 8e     U.
    bcs c8316                                                         ; 830c: b0 08       ..
    lda #&3f ; '?'                                                    ; 830e: a9 3f       .?             ; Mark RXCB as available
    sta (nfs_workspace),y                                             ; 8310: 91 9e       ..
    inc l00a8                                                         ; 8312: e6 a8       ..
    bne loop_c8307                                                    ; 8314: d0 f1       ..
; &8316 referenced 2 times by &82e2, &830c
.c8316
    lda station_id_disable_net_nmis                                   ; 8316: ad 18 fe    ...            ; Read station ID (also INTOFF)
    ldy #&14                                                          ; 8319: a0 14       ..
    sta (net_rx_ptr),y                                                ; 831b: 91 9c       ..
    jsr sub_c9633                                                     ; 831d: 20 33 96     3.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 8320: a9 40       .@             ; Enable user-level RX (LFLAG=&40)
    sta rx_flags                                                      ; 8322: 8d 64 0d    .d.
; ***************************************************************************************
; Set up ROM pointer table and NETV
; 
; Reads the ROM pointer table base address via OSBYTE &A8, stores
; it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
; one 3-byte extended vector entry (addr=&9080, rom=current) into
; the ROM pointer table at offset &36, installing osword_dispatch
; as the NETV handler.
; ***************************************************************************************
; &8325 referenced 1 time by &826f
.setup_rom_ptrs_netv
    lda #osbyte_read_rom_ptr_table_low                                ; 8325: a9 a8       ..
    ldx #0                                                            ; 8327: a2 00       ..
    ldy #&ff                                                          ; 8329: a0 ff       ..
    jsr osbyte                                                        ; 832b: 20 f4 ff     ..            ; Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 832e: 86 f6       ..             ; X=value of address of ROM pointer table (low byte)
    sty l00f7                                                         ; 8330: 84 f7       ..             ; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 8332: a0 36       .6             ; NETV extended vector offset in ROM ptr table
    sty netv                                                          ; 8334: 8c 24 02    .$.
    ldx #1                                                            ; 8337: a2 01       ..             ; Install 1 entry (NETV) in ROM ptr table
; &8339 referenced 2 times by &8276, &834b
.store_rom_ptr_pair
    lda run_fscv_cmd,y                                                ; 8339: b9 8d 82    ...
    sta (osrdsc_ptr),y                                                ; 833c: 91 f6       ..
    iny                                                               ; 833e: c8          .
    lda run_fscv_cmd,y                                                ; 833f: b9 8d 82    ...
    sta (osrdsc_ptr),y                                                ; 8342: 91 f6       ..
    iny                                                               ; 8344: c8          .
    lda romsel_copy                                                   ; 8345: a5 f4       ..             ; Write current ROM bank number
    sta (osrdsc_ptr),y                                                ; 8347: 91 f6       ..
    iny                                                               ; 8349: c8          .
    dex                                                               ; 834a: ca          .
    bne store_rom_ptr_pair                                            ; 834b: d0 ec       ..
    ldy nfs_workspace_hi                                              ; 834d: a4 9f       ..             ; Y = next workspace page for MOS
    iny                                                               ; 834f: c8          .
    rts                                                               ; 8350: 60          `

; ***************************************************************************************
; FSCV 6: Filing system shutdown / save state (FSDIE)
; 
; Called when another filing system (e.g. DFS) is selected. Saves
; the current NFS context (FSLOCN station number, URD/CSD/LIB
; handles, OPT byte, etc.) from page &0E into the dynamic workspace
; backup area. This allows the state to be restored when *NET is
; re-issued later, without losing the login session. Finally calls
; OSBYTE &77 (FXSPEX: close SPOOL and EXEC files) to avoid leaving
; dangling file handles across the FS switch.
; ***************************************************************************************
.fscv_6_shutdown
    ldy #&1d                                                          ; 8351: a0 1d       ..             ; Copy 10 bytes: FS state to workspace backup
; &8353 referenced 1 time by &835b
.fsdiel
    lda fs_state_deb,y                                                ; 8353: b9 eb 0d    ...
    sta (net_rx_ptr),y                                                ; 8356: 91 9c       ..
    dey                                                               ; 8358: 88          .
    cpy #&14                                                          ; 8359: c0 14       ..             ; Offsets &15-&1D: server, handles, OPT, etc.
    bne fsdiel                                                        ; 835b: d0 f6       ..
    lda #osbyte_close_spool_exec                                      ; 835d: a9 77       .w
    jmp osbyte                                                        ; 835f: 4c f4 ff    L..            ; Close any *SPOOL and *EXEC files

; &8362 referenced 2 times by &81b7, &81ec
.match_rom_string
    ldy l00a8                                                         ; 8362: a4 a8       ..             ; Y = saved text pointer offset
; &8364 referenced 1 time by &8375
.loop_c8364
    lda (os_text_ptr),y                                               ; 8364: b1 f2       ..             ; Load next input character
    cmp #&2e ; '.'                                                    ; 8366: c9 2e       ..             ; Is it a '.' (abbreviation)?
    beq c837d                                                         ; 8368: f0 13       ..             ; Yes: skip to space skipper (match)
    and #&df                                                          ; 836a: 29 df       ).             ; Force uppercase (clear bit 5)
    beq c8377                                                         ; 836c: f0 09       ..             ; Input char is NUL/space: check ROM byte
    cmp binary_version,x                                              ; 836e: dd 08 80    ...            ; Compare with ROM string byte
    bne c8377                                                         ; 8371: d0 04       ..             ; Mismatch: check if ROM string ended
    iny                                                               ; 8373: c8          .              ; Advance input pointer
    inx                                                               ; 8374: e8          .              ; Advance ROM string pointer
    bne loop_c8364                                                    ; 8375: d0 ed       ..             ; Continue matching (always taken)
; &8377 referenced 2 times by &836c, &8371
.c8377
    lda binary_version,x                                              ; 8377: bd 08 80    ...            ; Load ROM string byte at match point
    beq c837e                                                         ; 837a: f0 02       ..             ; Zero = end of ROM string = full match
    rts                                                               ; 837c: 60          `              ; Non-zero = partial/no match; Z=0

; &837d referenced 2 times by &8368, &8382
.c837d
    iny                                                               ; 837d: c8          .              ; Skip this space
; &837e referenced 2 times by &837a, &8ded
.c837e
    lda (os_text_ptr),y                                               ; 837e: b1 f2       ..             ; Load next input character
    cmp #&20 ; ' '                                                    ; 8380: c9 20       .              ; Is it a space?
    beq c837d                                                         ; 8382: f0 f9       ..             ; Yes: keep skipping
    eor #&0d                                                          ; 8384: 49 0d       I.             ; XOR with CR: Z=1 if end of line
    rts                                                               ; 8386: 60          `

; &8387 referenced 1 time by &83f4
.sub_c8387
    lda #&90                                                          ; 8387: a9 90       ..
; &8389 referenced 1 time by &889c
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8389: 20 95 83     ..
    sta l00c1                                                         ; 838c: 85 c1       ..
    lda #3                                                            ; 838e: a9 03       ..
    sta l00c4                                                         ; 8390: 85 c4       ..
    dec l00c0                                                         ; 8392: c6 c0       ..
    rts                                                               ; 8394: 60          `

; ***************************************************************************************
; Initialise TX control block at &00C0 from template
; 
; Copies 12 bytes from tx_ctrl_template (&83AD) to &00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from &0E00/&0E01 to &00C2/&00C3.
; The template sets up: control=&80, port=&99 (FS command port),
; command data length=&0F, plus padding bytes.
; ***************************************************************************************
; &8395 referenced 4 times by &8389, &83e3, &842f, &8ff6
.init_tx_ctrl_block
    pha                                                               ; 8395: 48          H
    ldy #&0b                                                          ; 8396: a0 0b       ..
; &8398 referenced 1 time by &83a9
.fstxl1
    lda tx_ctrl_template,y                                            ; 8398: b9 ad 83    ...
    sta l00c0,y                                                       ; 839b: 99 c0 00    ...
    cpy #2                                                            ; 839e: c0 02       ..             ; Y < 2: also copy FS server station/network
    bpl fstxl2                                                        ; 83a0: 10 06       ..
    lda fs_server_stn,y                                               ; 83a2: b9 00 0e    ...
    sta l00c2,y                                                       ; 83a5: 99 c2 00    ...
; &83a8 referenced 1 time by &83a0
.fstxl2
    dey                                                               ; 83a8: 88          .
    bpl fstxl1                                                        ; 83a9: 10 ed       ..
    pla                                                               ; 83ab: 68          h
    rts                                                               ; 83ac: 60          `

; ***************************************************************************************
; TX control block template (TXTAB, 12 bytes)
; 
; 12-byte template copied to &00C0 by init_tx_ctrl. Defines the
; TX control block for FS commands: control flag, port, station/
; network, and data buffer pointers (&0F00-&0FFF). The 4-byte
; Econet addresses use only the low 2 bytes; upper bytes are &FF.
; ***************************************************************************************
; &83ad referenced 1 time by &8398
.tx_ctrl_template
    equb &80, &99, 0, 0, 0, &0f                                       ; 83ad: 80 99 00... ...
; &83b3 referenced 3 times by &891c, &89fb, &9183
.l83b3
    equb &ff, &ff, &ff, &0f, &ff, &ff                                 ; 83b3: ff ff ff... ...

; &83b9 referenced 1 time by &8ac3
.prepare_cmd_with_flag
    pha                                                               ; 83b9: 48          H
    sec                                                               ; 83ba: 38          8
    bcs c83cf                                                         ; 83bb: b0 12       ..             ; ALWAYS branch

; &83bd referenced 2 times by &8729, &87cf
.prepare_cmd_clv
    clv                                                               ; 83bd: b8          .
    bvc c83ce                                                         ; 83be: 50 0e       P.             ; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8C4B for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 83c0: a9 77       .w
    jsr osbyte                                                        ; 83c2: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #&17                                                          ; 83c5: a0 17       ..             ; Y=function code for HDRFN
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
; &83c7 referenced 12 times by &80c5, &88c1, &8937, &8983, &89aa, &8a21, &8a48, &8b1e, &8bd9, &8c85, &8cbc, &8d27
.prepare_fs_cmd
    clv                                                               ; 83c7: b8          .              ; V=0: standard FS command path
; &83c8 referenced 2 times by &891f, &89fe
.init_tx_ctrl_data
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 83c8: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 83cb: 8d 02 0f    ...
; &83ce referenced 1 time by &83be
.c83ce
    clc                                                               ; 83ce: 18          .
; &83cf referenced 1 time by &83bb
.c83cf
    sty fs_cmd_y_param                                                ; 83cf: 8c 01 0f    ...
    ldy #1                                                            ; 83d2: a0 01       ..
; &83d4 referenced 1 time by &83db
.loop_c83d4
    lda fs_csd_handle,y                                               ; 83d4: b9 03 0e    ...            ; Copy CSD and LIB handles to command buffer
    sta fs_cmd_csd,y                                                  ; 83d7: 99 03 0f    ...
    dey                                                               ; 83da: 88          .              ; Y=function code
    bpl loop_c83d4                                                    ; 83db: 10 f7       ..
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
;     C: 0 for standard FS path, 1 for byte-stream (BSXMIT)
; 
; On Exit:
;     A: 0 on success
;     X: 0 on success, &D6 on not-found
;     Y: 1 (offset past command code in reply)
; ***************************************************************************************
; &83dd referenced 1 time by &8b77
.build_send_fs_cmd
    php                                                               ; 83dd: 08          .
    lda #&90                                                          ; 83de: a9 90       ..             ; Reply port &90 (PREPLY)
    sta fs_cmd_type                                                   ; 83e0: 8d 00 0f    ...
    jsr init_tx_ctrl_block                                            ; 83e3: 20 95 83     ..
    txa                                                               ; 83e6: 8a          .
    adc #5                                                            ; 83e7: 69 05       i.             ; HPTR = header (5) + data (X) bytes to send
    sta l00c8                                                         ; 83e9: 85 c8       ..
    plp                                                               ; 83eb: 28          (
    bcs dofsl5                                                        ; 83ec: b0 1a       ..             ; C=1: byte-stream path (BSXMIT)
    php                                                               ; 83ee: 08          .
    jsr setup_tx_ptr_c0                                               ; 83ef: 20 f7 85     ..
    plp                                                               ; 83f2: 28          (
; &83f3 referenced 2 times by &87dc, &8afb
.send_fs_reply_cmd
    php                                                               ; 83f3: 08          .
    jsr sub_c8387                                                     ; 83f4: 20 87 83     ..
    jsr c8530                                                         ; 83f7: 20 30 85     0.
    plp                                                               ; 83fa: 28          (
; &83fb referenced 1 time by &8411
.dofsl7
    iny                                                               ; 83fb: c8          .
    lda (l00c4),y                                                     ; 83fc: b1 c4       ..
    tax                                                               ; 83fe: aa          .
    beq return_dofsl7                                                 ; 83ff: f0 06       ..
    bvc c8405                                                         ; 8401: 50 02       P.
    adc #&2a ; '*'                                                    ; 8403: 69 2a       i*
; &8405 referenced 1 time by &8401
.c8405
    bne store_fs_error                                                ; 8405: d0 73       .s
; &8407 referenced 1 time by &83ff
.return_dofsl7
    rts                                                               ; 8407: 60          `

; &8408 referenced 1 time by &83ec
.dofsl5
    pla                                                               ; 8408: 68          h
    ldx #&c0                                                          ; 8409: a2 c0       ..
    iny                                                               ; 840b: c8          .
    jsr econet_tx_retry                                               ; 840c: 20 66 92     f.
    sta l00b3                                                         ; 840f: 85 b3       ..
    bcc dofsl7                                                        ; 8411: 90 e8       ..
.bputv_handler
    clc                                                               ; 8413: 18          .
; &8414 referenced 1 time by &8564
.sub_c8414
    jsr c8657                                                         ; 8414: 20 57 86     W.
; ***************************************************************************************
; Handle BPUT/BGET file byte I/O
; 
; BPUTV enters at &8413 (CLC; fall through) and BGETV enters
; at &8563 (SEC; JSR here). The carry flag is preserved via
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
.handle_bput_bget
    pha                                                               ; 8417: 48          H
    sta l0fdf                                                         ; 8418: 8d df 0f    ...
    txa                                                               ; 841b: 8a          .
    pha                                                               ; 841c: 48          H
    tya                                                               ; 841d: 98          .
    pha                                                               ; 841e: 48          H
    php                                                               ; 841f: 08          .
    sty l00ba                                                         ; 8420: 84 ba       ..             ; Save handle for SPOOL/EXEC comparison later
    jsr handle_to_mask_clc                                            ; 8422: 20 9b 86     ..
    sty l0fde                                                         ; 8425: 8c de 0f    ...
    sty l00cf                                                         ; 8428: 84 cf       ..
    ldy #&90                                                          ; 842a: a0 90       ..             ; &90 = data port (PREPLY)
    sty fs_putb_buf                                                   ; 842c: 8c dc 0f    ...
    jsr init_tx_ctrl_block                                            ; 842f: 20 95 83     ..
    lda #&dc                                                          ; 8432: a9 dc       ..             ; CB reply buffer at &0FDC
    sta l00c4                                                         ; 8434: 85 c4       ..
    lda #&e0                                                          ; 8436: a9 e0       ..             ; Error buffer at &0FE0
    sta l00c8                                                         ; 8438: 85 c8       ..
    iny                                                               ; 843a: c8          .
    ldx #9                                                            ; 843b: a2 09       ..
    plp                                                               ; 843d: 28          (              ; Restore C: selects BPUT (0) vs BGET (1)
    bcc store_retry_count                                             ; 843e: 90 01       ..
    dex                                                               ; 8440: ca          .              ; X=&08
; &8441 referenced 1 time by &843e
.store_retry_count
    stx fs_getb_buf                                                   ; 8441: 8e dd 0f    ...
    lda l00cf                                                         ; 8444: a5 cf       ..
    ldx #&c0                                                          ; 8446: a2 c0       ..
    jsr econet_tx_retry                                               ; 8448: 20 66 92     f.
    ldx fs_getb_buf                                                   ; 844b: ae dd 0f    ...
    beq update_sequence_return                                        ; 844e: f0 48       .H             ; Zero reply = success, skip error handling
    ldy #&1f                                                          ; 8450: a0 1f       ..             ; Copy 32-byte reply to error buffer at &0FE0
; &8452 referenced 1 time by &8459
.error1
    lda fs_putb_buf,y                                                 ; 8452: b9 dc 0f    ...
    sta l0fe0,y                                                       ; 8455: 99 e0 0f    ...
    dey                                                               ; 8458: 88          .
    bpl error1                                                        ; 8459: 10 f7       ..
    tax                                                               ; 845b: aa          .              ; X=File handle
    lda #osbyte_read_write_exec_file_handle                           ; 845c: a9 c6       ..             ; Returns X=EXEC handle, Y=SPOOL handle
    jsr osbyte                                                        ; 845e: 20 f4 ff     ..            ; Read/Write *EXEC file handle
    lda #&29 ; ')'                                                    ; 8461: a9 29       .)             ; ')': offset into "SP." string at &8529
    cpy l00ba                                                         ; 8463: c4 ba       ..             ; Y=value of *SPOOL file handle
    beq c846d                                                         ; 8465: f0 06       ..
    lda #&2d ; '-'                                                    ; 8467: a9 2d       .-             ; '-': offset into "E." string at &852D
    cpx l00ba                                                         ; 8469: e4 ba       ..             ; X=value of *EXEC file handle
    bne c8473                                                         ; 846b: d0 06       ..
; &846d referenced 1 time by &8465
.c846d
    tax                                                               ; 846d: aa          .
    ldy #&85                                                          ; 846e: a0 85       ..             ; Y=&85: high byte of OSCLI string in ROM
    jsr oscli                                                         ; 8470: 20 f7 ff     ..            ; Close SPOOL/EXEC via "*SP." or "*E."
; &8473 referenced 1 time by &846b
.c8473
    lda #&e0                                                          ; 8473: a9 e0       ..             ; Reset CB pointer to error buffer at &0FE0
    sta l00c4                                                         ; 8475: 85 c4       ..
    ldx fs_getb_buf                                                   ; 8477: ae dd 0f    ...
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
; &847a referenced 1 time by &8405
.store_fs_error
    stx fs_last_error                                                 ; 847a: 8e 09 0e    ...
    ldy #1                                                            ; 847d: a0 01       ..
    cpx #&a8                                                          ; 847f: e0 a8       ..             ; Clamp FS errors below &A8 to standard &A8
    bcs c8487                                                         ; 8481: b0 04       ..
    lda #&a8                                                          ; 8483: a9 a8       ..
    sta (l00c4),y                                                     ; 8485: 91 c4       ..
; &8487 referenced 1 time by &8481
.c8487
    ldy #&ff                                                          ; 8487: a0 ff       ..
; &8489 referenced 1 time by &8491
.loop_c8489
    iny                                                               ; 8489: c8          .
    lda (l00c4),y                                                     ; 848a: b1 c4       ..             ; Copy reply buffer to &0100 for BRK execution
    sta l0100,y                                                       ; 848c: 99 00 01    ...
    eor #&0d                                                          ; 848f: 49 0d       I.             ; Scan for CR terminator (&0D)
    bne loop_c8489                                                    ; 8491: d0 f6       ..
    sta l0100,y                                                       ; 8493: 99 00 01    ...            ; Replace CR with zero = BRK error block end
    beq c84ea                                                         ; 8496: f0 52       .R             ; Execute as BRK error block at &0100; ALWAYS branch

; &8498 referenced 1 time by &844e
.update_sequence_return
    sta fs_sequence_nos                                               ; 8498: 8d 08 0e    ...
    pla                                                               ; 849b: 68          h
    tay                                                               ; 849c: a8          .
    pla                                                               ; 849d: 68          h
    tax                                                               ; 849e: aa          .
    pla                                                               ; 849f: 68          h
; &84a0 referenced 1 time by &84a5
.return_remote_cmd
    rts                                                               ; 84a0: 60          `

; &84a1 referenced 2 times by &80ad, &8627
.sub_c84a1
    lda l00ff                                                         ; 84a1: a5 ff       ..
    and escapable                                                     ; 84a3: 25 97       %.
    bpl return_remote_cmd                                             ; 84a5: 10 f9       ..
    lda #osbyte_acknowledge_escape                                    ; 84a7: a9 7e       .~
    jsr osbyte                                                        ; 84a9: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
    jmp nlisne                                                        ; 84ac: 4c 12 85    L..

; ***************************************************************************************
; Remote boot/execute handler
; 
; Checks byte 4 of the RX control block (remote status flag).
; If zero (not currently remoted), falls through to remot1 to
; set up a new remote session. If non-zero (already remoted),
; jumps to clear_jsr_protection and returns.
; ***************************************************************************************
.lang_1_remote_boot
    ldy #4                                                            ; 84af: a0 04       ..
    lda (net_rx_ptr),y                                                ; 84b1: b1 9c       ..
    beq remot1                                                        ; 84b3: f0 03       ..
; &84b5 referenced 1 time by &84fb
.rchex
    jmp clear_jsr_protection                                          ; 84b5: 4c f0 92    L..

; &84b8 referenced 2 times by &84b3, &84f1
.remot1
    ora #9                                                            ; 84b8: 09 09       ..             ; Set remote status: bits 0+3 (ORA #9)
    sta (net_rx_ptr),y                                                ; 84ba: 91 9c       ..
    ldx #&80                                                          ; 84bc: a2 80       ..
    ldy #&80                                                          ; 84be: a0 80       ..
    lda (net_rx_ptr),y                                                ; 84c0: b1 9c       ..             ; Read source station lo from RX data at &80
    pha                                                               ; 84c2: 48          H
    iny                                                               ; 84c3: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 84c4: b1 9c       ..             ; Read source station hi from RX data at &81
    ldy #&0f                                                          ; 84c6: a0 0f       ..             ; Save controlling station to workspace &0E/&0F
    sta (nfs_workspace),y                                             ; 84c8: 91 9e       ..
    dey                                                               ; 84ca: 88          .              ; Y=&0e
    pla                                                               ; 84cb: 68          h
    sta (nfs_workspace),y                                             ; 84cc: 91 9e       ..
    jsr clear_osbyte_ce_cf                                            ; 84ce: 20 d2 81     ..
    jsr ctrl_block_setup                                              ; 84d1: 20 88 91     ..
    ldx #1                                                            ; 84d4: a2 01       ..
    ldy #0                                                            ; 84d6: a0 00       ..
    lda #osbyte_read_write_econet_keyboard_disable                    ; 84d8: a9 c9       ..             ; Disable keyboard for remote session
    jsr osbyte                                                        ; 84da: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute code at &0100
; 
; Clears JSR protection, zeroes &0100-&0102 (creating a BRK
; instruction at &0100 as a safe default), then JMP &0100 to
; execute code received over the network. If no code was loaded,
; the BRK triggers an error handler.
; ***************************************************************************************
.lang_3_execute_at_0100
    jsr clear_jsr_protection                                          ; 84dd: 20 f0 92     ..
    ldx #2                                                            ; 84e0: a2 02       ..
    lda #0                                                            ; 84e2: a9 00       ..
; &84e4 referenced 1 time by &84e8
.loop_c84e4
    sta l0100,x                                                       ; 84e4: 9d 00 01    ...
    dex                                                               ; 84e7: ca          .
    bpl loop_c84e4                                                    ; 84e8: 10 fa       ..
; &84ea referenced 2 times by &8496, &8523
.c84ea
    jmp l0100                                                         ; 84ea: 4c 00 01    L..

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
    ldy #4                                                            ; 84ed: a0 04       ..
    lda (net_rx_ptr),y                                                ; 84ef: b1 9c       ..
    beq remot1                                                        ; 84f1: f0 c5       ..
    ldy #&80                                                          ; 84f3: a0 80       ..             ; Read source station from RX data at &80
    lda (net_rx_ptr),y                                                ; 84f5: b1 9c       ..
    ldy #&0e                                                          ; 84f7: a0 0e       ..             ; Compare against controlling station at &0E
    cmp (nfs_workspace),y                                             ; 84f9: d1 9e       ..
    bne rchex                                                         ; 84fb: d0 b8       ..             ; Reject: source != controlling station
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.lang_0_insert_remote_key
    ldy #&82                                                          ; 84fd: a0 82       ..             ; Read keypress from RX data at &82
    lda (net_rx_ptr),y                                                ; 84ff: b1 9c       ..
    tay                                                               ; 8501: a8          .
    ldx #0                                                            ; 8502: a2 00       ..
    jsr clear_jsr_protection                                          ; 8504: 20 f0 92     ..            ; Release JSR protection before inserting key
    lda #osbyte_insert_input_buffer                                   ; 8507: a9 99       ..
    jmp osbyte                                                        ; 8509: 4c f4 ff    L..            ; Insert character Y into input buffer X

; &850c referenced 1 time by &8560
.c850c
    lda #8                                                            ; 850c: a9 08       ..
    bne set_listen_offset                                             ; 850e: d0 04       ..             ; ALWAYS branch

; &8510 referenced 1 time by &8640
.nlistn
    lda (net_tx_ptr,x)                                                ; 8510: a1 9a       ..
; &8512 referenced 2 times by &84ac, &8a40
.nlisne
    and #7                                                            ; 8512: 29 07       ).
; &8514 referenced 1 time by &850e
.set_listen_offset
    tax                                                               ; 8514: aa          .
    ldy error_offsets,x                                               ; 8515: bc 18 80    ...
    ldx #0                                                            ; 8518: a2 00       ..
    stx l0100                                                         ; 851a: 8e 00 01    ...
; &851d referenced 1 time by &8527
.loop_c851d
    lda error_msg_table,y                                             ; 851d: b9 80 85    ...
    sta l0101,x                                                       ; 8520: 9d 01 01    ...
    beq c84ea                                                         ; 8523: f0 c5       ..
    iny                                                               ; 8525: c8          .
    inx                                                               ; 8526: e8          .
    bne loop_c851d                                                    ; 8527: d0 f4       ..
    equs "SP."                                                        ; 8529: 53 50 2e    SP.
    equb &0d, &45, &2e, &0d                                           ; 852c: 0d 45 2e... .E.

; &8530 referenced 5 times by &83f7, &877f, &88a8, &903b, &929b
.c8530
    lda #&2a ; '*'                                                    ; 8530: a9 2a       .*
; ***************************************************************************************
; Send command to fileserver and handle reply (WAITFS)
; 
; Performs a complete FS transaction: transmit then wait for reply.
; Sets bit 7 of rx_flags (mark FS transaction in progress),
; builds a TX frame from the data at (net_tx_ptr), and transmits
; it. The system RX flag (LFLAG bit 7) is only set when receiving
; into the page-zero control block — if RXCBP's high byte is
; non-zero, setting the system flag would interfere with other RX
; operations. The timeout counter uses the stack (indexed via TSX)
; rather than memory to avoid bus conflicts with Econet hardware
; during the tight polling loop. Handles multi-block replies and
; checks for escape conditions between blocks.
; ***************************************************************************************
.send_to_fs
    pha                                                               ; 8532: 48          H
.send_to_fs_star
    lda rx_flags                                                      ; 8533: ad 64 0d    .d.
    pha                                                               ; 8536: 48          H
    ldx net_tx_ptr_hi                                                 ; 8537: a6 9b       ..             ; Only flag rx_flags if using page-zero CB
    bne c8540                                                         ; 8539: d0 05       ..
    ora #&80                                                          ; 853b: 09 80       ..
    sta rx_flags                                                      ; 853d: 8d 64 0d    .d.
; &8540 referenced 1 time by &8539
.c8540
    lda #0                                                            ; 8540: a9 00       ..             ; Push two zero bytes as timeout counters
    pha                                                               ; 8542: 48          H
    pha                                                               ; 8543: 48          H
    tay                                                               ; 8544: a8          .              ; Y=&00
    tsx                                                               ; 8545: ba          .              ; TSX: index stack-based timeout via X
; &8546 referenced 3 times by &854d, &8552, &8557
.incpx
    lda (net_tx_ptr),y                                                ; 8546: b1 9a       ..
    bmi fs_wait_cleanup                                               ; 8548: 30 0f       0.             ; Bit 7 set = reply received
    dec l0101,x                                                       ; 854a: de 01 01    ...            ; Three-stage nested timeout: inner loop
    bne incpx                                                         ; 854d: d0 f7       ..
    dec l0102,x                                                       ; 854f: de 02 01    ...            ; Middle timeout loop
    bne incpx                                                         ; 8552: d0 f2       ..
    dec l0104,x                                                       ; 8554: de 04 01    ...            ; Outer timeout loop (slowest)
    bne incpx                                                         ; 8557: d0 ed       ..
; &8559 referenced 1 time by &8548
.fs_wait_cleanup
    pla                                                               ; 8559: 68          h
    pla                                                               ; 855a: 68          h
    pla                                                               ; 855b: 68          h
    sta rx_flags                                                      ; 855c: 8d 64 0d    .d.            ; Restore saved rx_flags from stack
    pla                                                               ; 855f: 68          h
    beq c850c                                                         ; 8560: f0 aa       ..             ; A=saved func code; zero would mean no reply
; ***************************************************************************************
; Check and handle escape condition (ESC)
; 
; Stub: bare RTS in 3.60. In earlier versions (3.34-3.35K), this
; contained the full two-level escape gating logic (MOS escape flag
; ANDed with the ESCAP software enable). In 3.60 the escape check
; is inlined into the callers (sub_c84a1 at &84A1 and the
; tx_poll_core retry loop), leaving this as a no-op placeholder
; that preserves the fall-through entry point for bgetv_handler.
; ***************************************************************************************
.check_escape
    rts                                                               ; 8562: 60          `

.bgetv_handler
    sec                                                               ; 8563: 38          8
    jsr sub_c8414                                                     ; 8564: 20 14 84     ..
    sec                                                               ; 8567: 38          8
    lda #&fe                                                          ; 8568: a9 fe       ..
    bit l0fdf                                                         ; 856a: 2c df 0f    ,..
    bvs return_4                                                      ; 856d: 70 10       p.
    clc                                                               ; 856f: 18          .
    php                                                               ; 8570: 08          .
    lda l00cf                                                         ; 8571: a5 cf       ..
    plp                                                               ; 8573: 28          (
    bmi l8579                                                         ; 8574: 30 03       0.
    jsr clear_fs_flag                                                 ; 8576: 20 d5 86     ..
; &8579 referenced 1 time by &8574
.l8579
    equb &20                                                          ; 8579: 20
.l857a
return_4 = l857a+5
error_msg_table = l857a+6
    equs &d0, &86, &ad, &de, &0f, "`", &a0, "Line Jammed", 0          ; 857a: d0 86 ad... ...
; &857f referenced 1 time by &856d
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
; Indexed via c850c/nlistn/nlisne at &850C-&8514.
; &8580 referenced 1 time by &851d
    equb &a1                                                          ; 858d: a1          .
    equs "Net Error", 0                                               ; 858e: 4e 65 74... Net
    equb &a2                                                          ; 8598: a2          .
    equs "Not listening", 0                                           ; 8599: 4e 6f 74... Not
    equb &a3                                                          ; 85a7: a3          .
    equs "No Clock", 0                                                ; 85a8: 4e 6f 20... No
    equb &11                                                          ; 85b1: 11          .
    equs "Escape", 0                                                  ; 85b2: 45 73 63... Esc
    equb &cb                                                          ; 85b9: cb          .
    equs "Bad Option", 0                                              ; 85ba: 42 61 64... Bad
    equb &a5                                                          ; 85c5: a5          .
    equs "No reply", 0                                                ; 85c6: 4e 6f 20... No

; ***************************************************************************************
; Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)
; 
; Reads attribute byte at offset &0E from the parameter block,
; masks to 6 bits, then falls through to the shared bitmask
; builder. Converts fileserver protection format (5-6 bits) to
; BBC OSFILE attribute format (8 bits) via the lookup table at
; &85EC. The two formats use different bit layouts for file
; protection attributes.
; ***************************************************************************************
; &85cf referenced 2 times by &88fb, &8926
.decode_attribs_6bit
    ldy #&0e                                                          ; 85cf: a0 0e       ..
    lda (fs_options),y                                                ; 85d1: b1 bb       ..
    and #&3f ; '?'                                                    ; 85d3: 29 3f       )?
    ldx #4                                                            ; 85d5: a2 04       ..             ; X=4: skip first 4 table entries (BBC→FS half)
    bne c85dd                                                         ; 85d7: d0 04       ..             ; ALWAYS branch

; ***************************************************************************************
; Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)
; 
; Masks A to 5 bits and builds an access bitmask via the
; lookup table at &85EC. Each input bit position maps to a
; different output bit via the table. The conversion is done
; by iterating through the source bits and OR-ing in the
; corresponding destination bits from the table, translating
; between BBC (8-bit) and fileserver (5-bit) protection formats.
; ***************************************************************************************
; &85d9 referenced 2 times by &881f, &8943
.decode_attribs_5bit
    and #&1f                                                          ; 85d9: 29 1f       ).
    ldx #&ff                                                          ; 85db: a2 ff       ..             ; X=&FF: INX makes 0; start from table index 0
; &85dd referenced 1 time by &85d7
.c85dd
    sta fs_error_ptr                                                  ; 85dd: 85 b8       ..             ; Temp storage for source bitmask to shift out
    lda #0                                                            ; 85df: a9 00       ..
; &85e1 referenced 1 time by &85e9
.loop_c85e1
    inx                                                               ; 85e1: e8          .
    lsr fs_error_ptr                                                  ; 85e2: 46 b8       F.             ; Shift out source bits one at a time
    bcc c85e9                                                         ; 85e4: 90 03       ..
    ora access_bit_table,x                                            ; 85e6: 1d ec 85    ...            ; OR in destination bit from lookup table
; &85e9 referenced 1 time by &85e4
.c85e9
    bne loop_c85e1                                                    ; 85e9: d0 f6       ..
    rts                                                               ; 85eb: 60          `

; &85ec referenced 1 time by &85e6
.access_bit_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 85ec: 50 20 05... P .

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &85f7 referenced 2 times by &83ef, &8897
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 85f7: a2 c0       ..
    stx net_tx_ptr                                                    ; 85f9: 86 9a       ..
    ldx #0                                                            ; 85fb: a2 00       ..
    stx net_tx_ptr_hi                                                 ; 85fd: 86 9b       ..
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &85ff referenced 4 times by &9024, &907d, &90da, &9279
.tx_poll_ff
    lda #&ff                                                          ; 85ff: a9 ff       ..
.tx_poll_timeout
    ldy #&60 ; '`'                                                    ; 8601: a0 60       .`             ; Y=timeout parameter (&60 = standard)
; ***************************************************************************************
; Core transmit and poll routine (XMIT)
; 
; Claims the TX semaphore (tx_clear_flag) via ASL -- a busy-wait
; spinlock where carry=0 means the semaphore is held by another
; operation. Only after claiming the semaphore is the TX pointer
; copied to nmi_tx_block, ensuring the low-level transmit code
; sees a consistent pointer. Then calls the ADLC TX setup routine
; and polls the control byte for completion:
;   bit 7 set = still busy (loop)
;   bit 6 set = error (check escape or report)
;   bit 6 clear = success (clean return)
; On error, checks for escape condition and handles retries.
; Two entry points: setup_tx_ptr_c0 (&85F7) always uses the
; standard TXCB; tx_poll_core (&8603) is general-purpose.
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
.tx_poll_core
    pha                                                               ; 8603: 48          H              ; Save retry count and timeout on stack
    tya                                                               ; 8604: 98          .
    pha                                                               ; 8605: 48          H
    ldx #0                                                            ; 8606: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 8608: a1 9a       ..             ; Read control byte from TX block
; &860a referenced 1 time by &863d
.c860a
    sta (net_tx_ptr,x)                                                ; 860a: 81 9a       ..             ; Write back control byte (re-arm for TX)
    pha                                                               ; 860c: 48          H
; &860d referenced 1 time by &8610
.loop_c860d
    asl tx_clear_flag                                                 ; 860d: 0e 62 0d    .b.            ; Spin until TX semaphore is free (C=1)
    bcc loop_c860d                                                    ; 8610: 90 fb       ..
    lda net_tx_ptr                                                    ; 8612: a5 9a       ..             ; Copy TX pointer to NMI block while locked
    sta nmi_tx_block                                                  ; 8614: 85 a0       ..
    lda net_tx_ptr_hi                                                 ; 8616: a5 9b       ..
    sta nmi_tx_block_hi                                               ; 8618: 85 a1       ..
    jsr c9630                                                         ; 861a: 20 30 96     0.            ; Initiate ADLC transmission
; &861d referenced 1 time by &861f
.l4
    lda (net_tx_ptr,x)                                                ; 861d: a1 9a       ..             ; Poll: wait for bit 7 to clear (TX done)
    bmi l4                                                            ; 861f: 30 fc       0.
    asl a                                                             ; 8621: 0a          .              ; Bit 6 into sign: 0=success, 1=error
    bpl c8643                                                         ; 8622: 10 1f       ..             ; Success: clean up stack and exit
    asl a                                                             ; 8624: 0a          .              ; Bit 5: escape condition?
    beq c863f                                                         ; 8625: f0 18       ..             ; Yes (Z=1): abort via nlistn
    jsr sub_c84a1                                                     ; 8627: 20 a1 84     ..            ; Check for escape key pressed
    pla                                                               ; 862a: 68          h              ; Recover saved control byte
    tax                                                               ; 862b: aa          .
    pla                                                               ; 862c: 68          h              ; Recover timeout parameter
    tay                                                               ; 862d: a8          .
    pla                                                               ; 862e: 68          h              ; Recover retry count
    beq c863f                                                         ; 862f: f0 0e       ..             ; Retries exhausted: abort via nlistn
    sbc #1                                                            ; 8631: e9 01       ..             ; Decrement retry count (C=1 from CMP)
    pha                                                               ; 8633: 48          H              ; Re-push retry count and timeout for retry
    tya                                                               ; 8634: 98          .
    pha                                                               ; 8635: 48          H
    txa                                                               ; 8636: 8a          .
; &8637 referenced 2 times by &8638, &863b
.c8637
    dex                                                               ; 8637: ca          .              ; Delay loop: X*Y iterations before retry
    bne c8637                                                         ; 8638: d0 fd       ..
    dey                                                               ; 863a: 88          .
    bne c8637                                                         ; 863b: d0 fa       ..
    beq c860a                                                         ; 863d: f0 cb       ..             ; ALWAYS branch

; &863f referenced 2 times by &8625, &862f
.c863f
    tax                                                               ; 863f: aa          .
    jmp nlistn                                                        ; 8640: 4c 10 85    L..

; &8643 referenced 1 time by &8622
.c8643
    pla                                                               ; 8643: 68          h              ; Success: discard 3 saved bytes from stack
    pla                                                               ; 8644: 68          h
    pla                                                               ; 8645: 68          h
    jmp c8657                                                         ; 8646: 4c 57 86    LW.

; ***************************************************************************************
; Save FSCV arguments with text pointers
; 
; Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
; Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
; falls through to save_fscv_args to store A/X/Y in the FS
; workspace.
; ***************************************************************************************
; &8649 referenced 3 times by &80d4, &89d8, &8c1b
.save_fscv_args_with_ptrs
    stx os_text_ptr                                                   ; 8649: 86 f2       ..
    sty l00f3                                                         ; 864b: 84 f3       ..
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
; &864d referenced 3 times by &870c, &8968, &8a72
.save_fscv_args
    sta fs_last_byte_flag                                             ; 864d: 85 bd       ..
    stx fs_options                                                    ; 864f: 86 bb       ..
    sty fs_block_offset                                               ; 8651: 84 bc       ..
    stx fs_crc_lo                                                     ; 8653: 86 be       ..
    sty fs_crc_hi                                                     ; 8655: 84 bf       ..
; &8657 referenced 2 times by &8414, &8646
.c8657
    php                                                               ; 8657: 08          .              ; Clear escapable flag, preserving processor flags
    lsr escapable                                                     ; 8658: 46 97       F.
    plp                                                               ; 865a: 28          (
    rts                                                               ; 865b: 60          `

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
; &865c referenced 13 times by &8208, &8232, &8252, &825f, &8c8d, &8c97, &8ca5, &8cb0, &8cc5, &8cda, &8ced, &8cfc, &8dab
.print_inline
    pla                                                               ; 865c: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 865d: 85 b0       ..
    pla                                                               ; 865f: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 8660: 85 b1       ..
    ldy #0                                                            ; 8662: a0 00       ..
; &8664 referenced 1 time by &8671
.loop_c8664
    inc fs_load_addr                                                  ; 8664: e6 b0       ..             ; Advance pointer past return address / to next char
    bne c866a                                                         ; 8666: d0 02       ..
    inc fs_load_addr_hi                                               ; 8668: e6 b1       ..
; &866a referenced 1 time by &8666
.c866a
    lda (fs_load_addr),y                                              ; 866a: b1 b0       ..             ; Load next byte from inline string
    bmi c8674                                                         ; 866c: 30 06       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 866e: 20 e3 ff     ..            ; Write character
    jmp loop_c8664                                                    ; 8671: 4c 64 86    Ld.

; &8674 referenced 1 time by &866c
.c8674
    jmp (fs_load_addr)                                                ; 8674: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

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
;     X: preserved
;     Y: offset past last digit parsed
; ***************************************************************************************
; &8677 referenced 2 times by &808c, &8095
.parse_decimal
    lda #0                                                            ; 8677: a9 00       ..             ; Zero accumulator
    sta fs_load_addr_2                                                ; 8679: 85 b2       ..
; &867b referenced 1 time by &8694
.loop_c867b
    lda (fs_options),y                                                ; 867b: b1 bb       ..             ; Load next char from buffer
    cmp #&2e ; '.'                                                    ; 867d: c9 2e       ..             ; Dot separator?
    beq c8697                                                         ; 867f: f0 16       ..             ; Yes: exit with C=1 (dot found)
    bcc c8696                                                         ; 8681: 90 13       ..             ; Control char or space: done
    and #&0f                                                          ; 8683: 29 0f       ).             ; Mask ASCII digit to 0-9
    sta l00b3                                                         ; 8685: 85 b3       ..             ; Save new digit
    asl fs_load_addr_2                                                ; 8687: 06 b2       ..             ; Running total * 2
    lda fs_load_addr_2                                                ; 8689: a5 b2       ..             ; A = running total * 2
    asl a                                                             ; 868b: 0a          .              ; A = running total * 4
    asl a                                                             ; 868c: 0a          .              ; A = running total * 8
    adc fs_load_addr_2                                                ; 868d: 65 b2       e.             ; + total*2 = total * 10
    adc l00b3                                                         ; 868f: 65 b3       e.             ; + digit = total*10 + digit
    sta fs_load_addr_2                                                ; 8691: 85 b2       ..             ; Store new running total
    iny                                                               ; 8693: c8          .              ; Advance to next char
    bne loop_c867b                                                    ; 8694: d0 e5       ..             ; Loop (always: Y won't wrap to 0)
; &8696 referenced 1 time by &8681
.c8696
    clc                                                               ; 8696: 18          .              ; No dot found: C=0
; &8697 referenced 1 time by &867f
.c8697
    lda fs_load_addr_2                                                ; 8697: a5 b2       ..             ; Return result in A
    rts                                                               ; 8699: 60          `

; ***************************************************************************************
; Convert handle in A to bitmask
; 
; Transfers A to Y via TAY, then falls through to
; handle_to_mask_clc to clear carry and convert.
; ***************************************************************************************
; &869a referenced 3 times by &88af, &8a8d, &8f5b
.handle_to_mask_a
    tay                                                               ; 869a: a8          .
; ***************************************************************************************
; Convert handle to bitmask (carry cleared)
; 
; Clears carry to ensure handle_to_mask converts
; unconditionally. Falls through to handle_to_mask.
; ***************************************************************************************
; &869b referenced 2 times by &8422, &8973
.handle_to_mask_clc
    clc                                                               ; 869b: 18          .
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
; &869c referenced 1 time by &89dc
.handle_to_mask
    pha                                                               ; 869c: 48          H              ; Save A (will be restored on exit)
    txa                                                               ; 869d: 8a          .              ; Save X (will be restored on exit)
    pha                                                               ; 869e: 48          H              ;   (second half of X save)
    tya                                                               ; 869f: 98          .              ; A = handle from Y
    bcc y2fsl5                                                        ; 86a0: 90 02       ..             ; C=0: always convert
    beq c86b3                                                         ; 86a2: f0 0f       ..             ; C=1 and Y=0: skip (handle 0 = none)
; &86a4 referenced 1 time by &86a0
.y2fsl5
    sec                                                               ; 86a4: 38          8              ; C=1 and Y!=0: convert
    sbc #&1f                                                          ; 86a5: e9 1f       ..             ; A = handle - &1F (1-based bit position)
    tax                                                               ; 86a7: aa          .              ; X = shift count
    lda #1                                                            ; 86a8: a9 01       ..             ; Start with bit 0 set
; &86aa referenced 1 time by &86ac
.y2fsl2
    asl a                                                             ; 86aa: 0a          .              ; Shift bit left
    dex                                                               ; 86ab: ca          .              ; Count down
    bne y2fsl2                                                        ; 86ac: d0 fc       ..             ; Loop until correct position
    ror a                                                             ; 86ae: 6a          j              ; Undo final extra shift
    tay                                                               ; 86af: a8          .              ; Y = resulting bitmask
    bne c86b3                                                         ; 86b0: d0 01       ..             ; Non-zero: valid mask, skip to exit
    dey                                                               ; 86b2: 88          .              ; Zero: invalid handle, set Y=&FF
; &86b3 referenced 2 times by &86a2, &86b0
.c86b3
    pla                                                               ; 86b3: 68          h              ; Restore X
    tax                                                               ; 86b4: aa          .
    pla                                                               ; 86b5: 68          h              ; Restore A
    rts                                                               ; 86b6: 60          `

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
; &86b7 referenced 2 times by &8a0b, &8f73
.mask_to_handle
    ldx #&1f                                                          ; 86b7: a2 1f       ..             ; X = &1F (handle base - 1)
; &86b9 referenced 1 time by &86bb
.fs2al1
    inx                                                               ; 86b9: e8          .              ; Count this bit position
    lsr a                                                             ; 86ba: 4a          J              ; Shift mask right; C=0 when done
    bne fs2al1                                                        ; 86bb: d0 fc       ..             ; Loop until all bits shifted out
    txa                                                               ; 86bd: 8a          .              ; A = X = &1F + bit position = handle
    rts                                                               ; 86be: 60          `

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
; &86bf referenced 2 times by &8765, &8854
.compare_addresses
    ldx #4                                                            ; 86bf: a2 04       ..
; &86c1 referenced 1 time by &86c8
.loop_c86c1
    lda l00af,x                                                       ; 86c1: b5 af       ..
    eor l00b3,x                                                       ; 86c3: 55 b3       U.
    bne return_compare                                                ; 86c5: d0 03       ..
    dex                                                               ; 86c7: ca          .
    bne loop_c86c1                                                    ; 86c8: d0 f7       ..
; &86ca referenced 1 time by &86c5
.return_compare
    rts                                                               ; 86ca: 60          `

.fscv_7_read_handles
    ldx #&20 ; ' '                                                    ; 86cb: a2 20       .
    ldy #&27 ; '''                                                    ; 86cd: a0 27       .'
.return_fscv_handles
    rts                                                               ; 86cf: 60          `

; &86d0 referenced 4 times by &89b0, &8a07, &8a27, &8b08
.sub_c86d0
    ora fs_eof_flags                                                  ; 86d0: 0d 07 0e    ...
    bne store_fs_flag                                                 ; 86d3: d0 05       ..
; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then falls through to set_fs_flag which
; ANDs the result into fs_eof_flags to clear the specified bits.
; ***************************************************************************************
; &86d5 referenced 3 times by &8576, &88ca, &8b05
.clear_fs_flag
    eor #&ff                                                          ; 86d5: 49 ff       I.
; ***************************************************************************************
; AND mask into FS flags (&0E07)
; 
; ANDs A into fs_eof_flags (&0E07), then stores the result.
; Despite the name (retained from 3.34 where it used ORA), this
; entry point performs AND -- it is used by clear_fs_flag to
; mask out bits. In 3.60, bit-setting is handled by sub_c86d0
; which ORs A into the flags and branches directly to
; store_fs_flag, bypassing this AND step.
; Each bit represents one of up to 8 open file handles. When
; clear, the file is definitely NOT at EOF. When set, the
; fileserver must be queried to confirm EOF status. This
; negative-cache optimisation avoids expensive network
; round-trips for the common case. The hint is cleared when
; the file pointer is updated (since seeking away from EOF
; invalidates the hint) and set after BGET/OPEN/EOF operations
; that might have reached the end.
; ***************************************************************************************
.set_fs_flag
    and fs_eof_flags                                                  ; 86d7: 2d 07 0e    -..
; &86da referenced 1 time by &86d3
.store_fs_flag
    sta fs_eof_flags                                                  ; 86da: 8d 07 0e    ...
    rts                                                               ; 86dd: 60          `

; &86de referenced 1 time by &870f
.sub_c86de
    ldy #1                                                            ; 86de: a0 01       ..
; &86e0 referenced 1 time by &86e6
.file1
    lda (fs_options),y                                                ; 86e0: b1 bb       ..
    sta os_text_ptr,y                                                 ; 86e2: 99 f2 00    ...
    dey                                                               ; 86e5: 88          .
    bpl file1                                                         ; 86e6: 10 f8       ..
; ***************************************************************************************
; Parse filename using GSINIT/GSREAD into &0E30
; 
; Uses the MOS GSINIT/GSREAD API to parse a filename string from
; (os_text_ptr),Y, handling quoted strings and |-escaped characters.
; Stores the parsed result CR-terminated at &0E30 and sets up
; fs_crc_lo/hi to point to that buffer. Sub-entry at &86EA allows
; a non-zero starting Y offset.
; 
; On Entry:
;     Y: offset into (os_text_ptr) buffer (0 at &86E8)
; 
; On Exit:
;     X: length of parsed string
;     Y: preserved
; ***************************************************************************************
; &86e8 referenced 2 times by &89f1, &8ddc
.parse_filename_gs
    ldy #0                                                            ; 86e8: a0 00       ..
; &86ea referenced 1 time by &8c7b
.sub_c86ea
    ldx #&ff                                                          ; 86ea: a2 ff       ..             ; X=&FF: INX will make X=0 (first char index)
    clc                                                               ; 86ec: 18          .              ; C=0 for GSINIT: parse from current position
    jsr gsinit                                                        ; 86ed: 20 c2 ff     ..
    beq c86fd                                                         ; 86f0: f0 0b       ..             ; Empty string: skip to CR terminator
; &86f2 referenced 1 time by &86fb
.delay_1ms
.quote1
    jsr gsread                                                        ; 86f2: 20 c5 ff     ..
    bcs c86fd                                                         ; 86f5: b0 06       ..             ; C=1 from GSREAD: end of string reached
    inx                                                               ; 86f7: e8          .
    sta l0e30,x                                                       ; 86f8: 9d 30 0e    .0.
    bcc delay_1ms                                                     ; 86fb: 90 f5       ..             ; ALWAYS branch

; &86fd referenced 2 times by &86f0, &86f5
.c86fd
    inx                                                               ; 86fd: e8          .              ; Terminate parsed string with CR
    lda #&0d                                                          ; 86fe: a9 0d       ..
    sta l0e30,x                                                       ; 8700: 9d 30 0e    .0.
    lda #&30 ; '0'                                                    ; 8703: a9 30       .0             ; Point fs_crc_lo/hi at &0E30 parse buffer
    sta fs_crc_lo                                                     ; 8705: 85 be       ..
    lda #&0e                                                          ; 8707: a9 0e       ..
    sta fs_crc_hi                                                     ; 8709: 85 bf       ..
    rts                                                               ; 870b: 60          `

; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Calls save_fscv_args (&864D) to preserve A/X/Y, then JSR &86DE
; to copy the 2-byte filename pointer from the parameter block to
; os_text_ptr and fall through to parse_filename_gs (&86E8) which
; parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
; the parsed filename buffer.
; Dispatches by function code A:
;   A=&FF: load file (send_fs_examine at &8722)
;   A=&00: save file (filev_save at &8795)
;   A=&01-&06: attribute operations (filev_attrib_dispatch at &88D1)
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
    jsr save_fscv_args                                                ; 870c: 20 4d 86     M.
    jsr sub_c86de                                                     ; 870f: 20 de 86     ..            ; Copy filename ptr from param block to os_text_ptr
    lda fs_last_byte_flag                                             ; 8712: a5 bd       ..             ; Recover function code from saved A
    bpl saveop                                                        ; 8714: 10 7a       .z             ; A >= 0: save (&00) or attribs (&01-&06)
    cmp #&ff                                                          ; 8716: c9 ff       ..             ; A=&FF? Only &FF is valid for load
    beq loadop                                                        ; 8718: f0 03       ..
    jmp restore_args_return                                           ; 871a: 4c b3 89    L..            ; Unknown negative code: no-op return

; &871d referenced 1 time by &8718
.loadop
    jsr infol2                                                        ; 871d: 20 82 8d     ..
    ldy #2                                                            ; 8720: a0 02       ..
; ***************************************************************************************
; Send FS examine command
; 
; Sends an FS examine/load command to the fileserver. The function
; code in Y is set by the caller (Y=2 for load, Y=5 for examine).
; Overwrites fs_cmd_urd (&0F02) with &92 (PLDATA port number) to
; repurpose the URD header field for the data transfer port. Sets
; escapable to &92 so escape checking is active during the transfer.
; Calls prepare_cmd_clv to build the FS header (which skips the
; normal URD copy, preserving &92). The FS reply contains load/exec
; addresses and file length used to set up the data transfer.
; Byte 6 of the parameter block selects load address handling:
; non-zero uses the address from the FS reply (load to file's own
; address); zero uses the caller-supplied address.
; ***************************************************************************************
; &8722 referenced 1 time by &8e0d
.send_fs_examine
    lda #&92                                                          ; 8722: a9 92       ..             ; Port &92 = PLDATA (data transfer port)
    sta escapable                                                     ; 8724: 85 97       ..             ; Mark transfer as escapable
    sta fs_cmd_urd                                                    ; 8726: 8d 02 0f    ...            ; Overwrite URD field with data port number
    jsr prepare_cmd_clv                                               ; 8729: 20 bd 83     ..
    ldy #6                                                            ; 872c: a0 06       ..
    lda (fs_options),y                                                ; 872e: b1 bb       ..             ; Byte 6: use file's own load address?
    bne lodfil                                                        ; 8730: d0 08       ..             ; Non-zero: use FS reply address (lodfil)
    jsr copy_load_addr_from_params                                    ; 8732: 20 2f 88     /.            ; Zero: copy caller's load addr first
    jsr copy_reply_to_params                                          ; 8735: 20 41 88     A.
    bcc c8740                                                         ; 8738: 90 06       ..             ; Carry clear from prepare_cmd_clv: skip lodfil
; &873a referenced 1 time by &8730
.lodfil
    jsr copy_reply_to_params                                          ; 873a: 20 41 88     A.
    jsr copy_load_addr_from_params                                    ; 873d: 20 2f 88     /.
; &8740 referenced 1 time by &8738
.c8740
    ldy #4                                                            ; 8740: a0 04       ..             ; Compute end address = load + file length
; &8742 referenced 1 time by &874d
.loop_c8742
    lda fs_load_addr,x                                                ; 8742: b5 b0       ..
    sta l00c8,x                                                       ; 8744: 95 c8       ..
    adc l0f0d,x                                                       ; 8746: 7d 0d 0f    }..
    sta l00b4,x                                                       ; 8749: 95 b4       ..
    inx                                                               ; 874b: e8          .
    dey                                                               ; 874c: 88          .
    bne loop_c8742                                                    ; 874d: d0 f3       ..
    sec                                                               ; 874f: 38          8              ; Adjust high byte for 3-byte length overflow
    sbc l0f10                                                         ; 8750: ed 10 0f    ...
    sta l00b7                                                         ; 8753: 85 b7       ..
    jsr send_data_blocks                                              ; 8755: 20 65 87     e.            ; Transfer file data in &80-byte blocks
    ldx #2                                                            ; 8758: a2 02       ..             ; Copy 3-byte file length to FS reply cmd buffer
; &875a referenced 1 time by &8761
.floop
    lda l0f10,x                                                       ; 875a: bd 10 0f    ...
    sta fs_cmd_data,x                                                 ; 875d: 9d 05 0f    ...
    dex                                                               ; 8760: ca          .
    bpl floop                                                         ; 8761: 10 f7       ..
    bmi c87d8                                                         ; 8763: 30 73       0s             ; ALWAYS branch

; ***************************************************************************************
; Send file data in multi-block chunks
; 
; Repeatedly sends &80-byte (128-byte) blocks of file data to the
; fileserver using command &7F. Compares current address (&C8-&CB)
; against end address (&B4-&B7) via compare_addresses, and loops
; until the entire file has been transferred. Each block is sent
; via send_to_fs_star.
; ***************************************************************************************
; &8765 referenced 2 times by &8755, &8af8
.send_data_blocks
    jsr compare_addresses                                             ; 8765: 20 bf 86     ..            ; Compare two 4-byte addresses
    beq return_lodchk                                                 ; 8768: f0 25       .%             ; Addresses match: transfer complete
    lda #&92                                                          ; 876a: a9 92       ..             ; Port &92 for data block transfer
    sta l00c1                                                         ; 876c: 85 c1       ..
; &876e referenced 1 time by &878a
.loop_c876e
    ldx #3                                                            ; 876e: a2 03       ..             ; Set up next &80-byte block for transfer
; &8770 referenced 1 time by &8779
.loop_c8770
    lda l00c8,x                                                       ; 8770: b5 c8       ..             ; Swap: current addr -> source, end -> current
    sta l00c4,x                                                       ; 8772: 95 c4       ..
    lda l00b4,x                                                       ; 8774: b5 b4       ..
    sta l00c8,x                                                       ; 8776: 95 c8       ..
    dex                                                               ; 8778: ca          .
    bpl loop_c8770                                                    ; 8779: 10 f5       ..
    lda #&7f                                                          ; 877b: a9 7f       ..             ; Command &7F = data block transfer
    sta l00c0                                                         ; 877d: 85 c0       ..
    jsr c8530                                                         ; 877f: 20 30 85     0.            ; Send this block to the fileserver
    ldy #3                                                            ; 8782: a0 03       ..
; &8784 referenced 1 time by &878d
.lodchk
    lda l00c8,y                                                       ; 8784: b9 c8 00    ...            ; Compare current vs end address (4 bytes)
    eor l00b4,y                                                       ; 8787: 59 b4 00    Y..
    bne loop_c876e                                                    ; 878a: d0 e2       ..             ; Not equal: more blocks to send
    dey                                                               ; 878c: 88          .
    bpl lodchk                                                        ; 878d: 10 f5       ..
; &878f referenced 1 time by &8768
.return_lodchk
    rts                                                               ; 878f: 60          `

; &8790 referenced 1 time by &8714
.saveop
    beq filev_save                                                    ; 8790: f0 03       ..
    jmp filev_attrib_dispatch                                         ; 8792: 4c d1 88    L..

; ***************************************************************************************
; OSFILE save handler (A=&00)
; 
; Copies 4-byte load/exec/length addresses from the parameter block
; to the FS command buffer, along with the filename. The savsiz loop
; computes data-end minus data-start for each address byte to derive
; the transfer length, saving both the original address and the
; difference. Sends FS command with port &91, function code Y=1,
; and the filename via copy_string_to_cmd. After transfer_file_blocks
; sends the data, calls send_fs_reply_cmd for the final handshake.
; If fs_messages_flag is set, prints the catalogue line inline:
; filename (padded to 12 chars), load address, exec address, and
; file length. Finally decodes the FS attributes and copies the
; reply data back into the caller's parameter block.
; ***************************************************************************************
; &8795 referenced 1 time by &8790
.filev_save
    ldx #4                                                            ; 8795: a2 04       ..             ; Process 4 address bytes (load/exec/start/end)
    ldy #&0e                                                          ; 8797: a0 0e       ..             ; Y=&0E: start from end-address in param block
; &8799 referenced 1 time by &87b3
.savsiz
    lda (fs_options),y                                                ; 8799: b1 bb       ..             ; Read end-address byte from param block
    sta port_ws_offset,y                                              ; 879b: 99 a6 00    ...            ; Save to port workspace for transfer setup
    jsr sub_4_from_y                                                  ; 879e: 20 4e 88     N.
    sbc (fs_options),y                                                ; 87a1: f1 bb       ..             ; end - start = transfer length byte
    sta fs_cmd_csd,y                                                  ; 87a3: 99 03 0f    ...            ; Store length byte in FS command buffer
    pha                                                               ; 87a6: 48          H
    lda (fs_options),y                                                ; 87a7: b1 bb       ..             ; Read corresponding start-address byte
    sta port_ws_offset,y                                              ; 87a9: 99 a6 00    ...            ; Save to port workspace
    pla                                                               ; 87ac: 68          h
    sta (fs_options),y                                                ; 87ad: 91 bb       ..             ; Replace param block entry with length
    jsr add_5_to_y                                                    ; 87af: 20 3b 88     ;.
    dex                                                               ; 87b2: ca          .
    bne savsiz                                                        ; 87b3: d0 e4       ..
    ldy #9                                                            ; 87b5: a0 09       ..             ; Copy load/exec addresses to FS command buffer
; &87b7 referenced 1 time by &87bd
.loop_c87b7
    lda (fs_options),y                                                ; 87b7: b1 bb       ..
    sta fs_cmd_csd,y                                                  ; 87b9: 99 03 0f    ...
    dey                                                               ; 87bc: 88          .
    bne loop_c87b7                                                    ; 87bd: d0 f8       ..
    lda #&91                                                          ; 87bf: a9 91       ..             ; Port &91 for save command
    sta escapable                                                     ; 87c1: 85 97       ..             ; Mark as escapable during save
    sta fs_cmd_urd                                                    ; 87c3: 8d 02 0f    ...            ; Overwrite URD field with port number
    sta fs_error_ptr                                                  ; 87c6: 85 b8       ..
    ldx #&0b                                                          ; 87c8: a2 0b       ..             ; Append filename at offset &0B in cmd buffer
    jsr copy_string_to_cmd                                            ; 87ca: 20 84 8d     ..
    ldy #1                                                            ; 87cd: a0 01       ..             ; Y=1: function code for save
    jsr prepare_cmd_clv                                               ; 87cf: 20 bd 83     ..
    lda fs_cmd_data                                                   ; 87d2: ad 05 0f    ...            ; Read FS reply command code for transfer type
    jsr transfer_file_blocks                                          ; 87d5: 20 53 88     S.            ; Send file data blocks to server
; &87d8 referenced 1 time by &8763
.c87d8
    lda fs_cmd_csd                                                    ; 87d8: ad 03 0f    ...            ; Save CSD from reply for catalogue display
    pha                                                               ; 87db: 48          H
    jsr send_fs_reply_cmd                                             ; 87dc: 20 f3 83     ..            ; Send final reply acknowledgement
    pla                                                               ; 87df: 68          h
    ldy fs_messages_flag                                              ; 87e0: ac 06 0e    ...            ; Check if file info messages enabled
    beq c8817                                                         ; 87e3: f0 32       .2             ; Messages off: skip catalogue display
    ldy #0                                                            ; 87e5: a0 00       ..
    tax                                                               ; 87e7: aa          .
    beq c87ef                                                         ; 87e8: f0 05       ..
    jsr print_dir_from_offset                                         ; 87ea: 20 98 8d     ..
    bmi c8803                                                         ; 87ed: 30 14       0.
; &87ef referenced 2 times by &87e8, &87f9
.c87ef
    lda (fs_crc_lo),y                                                 ; 87ef: b1 be       ..
    cmp #&21 ; '!'                                                    ; 87f1: c9 21       .!
    bcc c87fb                                                         ; 87f3: 90 06       ..
    jsr osasci                                                        ; 87f5: 20 e3 ff     ..            ; Write character
    iny                                                               ; 87f8: c8          .
    bne c87ef                                                         ; 87f9: d0 f4       ..
; &87fb referenced 2 times by &87f3, &8801
.c87fb
    jsr print_space                                                   ; 87fb: 20 7b 8d     {.
    iny                                                               ; 87fe: c8          .
    cpy #&0c                                                          ; 87ff: c0 0c       ..
    bcc c87fb                                                         ; 8801: 90 f8       ..
; &8803 referenced 1 time by &87ed
.c8803
    ldy #5                                                            ; 8803: a0 05       ..
    jsr print_hex_bytes                                               ; 8805: 20 70 8d     p.
    ldy #9                                                            ; 8808: a0 09       ..
    jsr print_hex_bytes                                               ; 880a: 20 70 8d     p.
    ldy #&0c                                                          ; 880d: a0 0c       ..
    ldx #3                                                            ; 880f: a2 03       ..
    jsr num01                                                         ; 8811: 20 72 8d     r.
    jsr osnewl                                                        ; 8814: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
; &8817 referenced 1 time by &87e3
.c8817
    stx l0f08                                                         ; 8817: 8e 08 0f    ...
    ldy #&0e                                                          ; 881a: a0 0e       ..
    lda fs_cmd_data                                                   ; 881c: ad 05 0f    ...
    jsr decode_attribs_5bit                                           ; 881f: 20 d9 85     ..
; &8822 referenced 1 time by &882a
.loop_c8822
    sta (fs_options),y                                                ; 8822: 91 bb       ..
    iny                                                               ; 8824: c8          .
    lda l0ef7,y                                                       ; 8825: b9 f7 0e    ...
    cpy #&12                                                          ; 8828: c0 12       ..
    bne loop_c8822                                                    ; 882a: d0 f6       ..
    jmp restore_args_return                                           ; 882c: 4c b3 89    L..

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &882f referenced 2 times by &8732, &873d
.copy_load_addr_from_params
    ldy #5                                                            ; 882f: a0 05       ..
; &8831 referenced 1 time by &8839
.lodrl1
    lda (fs_options),y                                                ; 8831: b1 bb       ..
    sta l00ae,y                                                       ; 8833: 99 ae 00    ...
    dey                                                               ; 8836: 88          .
    cpy #2                                                            ; 8837: c0 02       ..
    bcs lodrl1                                                        ; 8839: b0 f6       ..
; &883b referenced 1 time by &87af
.add_5_to_y
    iny                                                               ; 883b: c8          .
; &883c referenced 1 time by &8ad5
.add_4_to_y
    iny                                                               ; 883c: c8          .
    iny                                                               ; 883d: c8          .
    iny                                                               ; 883e: c8          .
    iny                                                               ; 883f: c8          .
    rts                                                               ; 8840: 60          `

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; ***************************************************************************************
; &8841 referenced 2 times by &8735, &873a
.copy_reply_to_params
    ldy #&0d                                                          ; 8841: a0 0d       ..
    txa                                                               ; 8843: 8a          .
; &8844 referenced 1 time by &884c
.lodrl2
    sta (fs_options),y                                                ; 8844: 91 bb       ..
    lda fs_cmd_urd,y                                                  ; 8846: b9 02 0f    ...
    dey                                                               ; 8849: 88          .
    cpy #2                                                            ; 884a: c0 02       ..
    bcs lodrl2                                                        ; 884c: b0 f6       ..
; &884e referenced 1 time by &879e
.sub_4_from_y
    dey                                                               ; 884e: 88          .
; &884f referenced 2 times by &88e9, &8add
.sub_3_from_y
    dey                                                               ; 884f: 88          .
    dey                                                               ; 8850: 88          .
    dey                                                               ; 8851: 88          .
    rts                                                               ; 8852: 60          `

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
; &8853 referenced 2 times by &87d5, &8af3
.transfer_file_blocks
    pha                                                               ; 8853: 48          H
    jsr compare_addresses                                             ; 8854: 20 bf 86     ..            ; Compare two 4-byte addresses
    beq c88cd                                                         ; 8857: f0 74       .t             ; Addresses equal: nothing to transfer
; &8859 referenced 1 time by &88ab
.c8859
    lda #0                                                            ; 8859: a9 00       ..
    pha                                                               ; 885b: 48          H              ; Push 4-byte block size: 0, 0, hi, lo
    pha                                                               ; 885c: 48          H
    tax                                                               ; 885d: aa          .              ; X=&00
    lda l0f07                                                         ; 885e: ad 07 0f    ...
    pha                                                               ; 8861: 48          H
    lda l0f06                                                         ; 8862: ad 06 0f    ...
    pha                                                               ; 8865: 48          H
    ldy #4                                                            ; 8866: a0 04       ..
    clc                                                               ; 8868: 18          .
; &8869 referenced 1 time by &8876
.loop_c8869
    lda fs_load_addr,x                                                ; 8869: b5 b0       ..             ; Source = current position
    sta l00c4,x                                                       ; 886b: 95 c4       ..
    pla                                                               ; 886d: 68          h
    adc fs_load_addr,x                                                ; 886e: 75 b0       u.             ; Dest = current pos + block size
    sta l00c8,x                                                       ; 8870: 95 c8       ..
    sta fs_load_addr,x                                                ; 8872: 95 b0       ..             ; Advance current position
    inx                                                               ; 8874: e8          .
    dey                                                               ; 8875: 88          .
    bne loop_c8869                                                    ; 8876: d0 f1       ..
    sec                                                               ; 8878: 38          8
; &8879 referenced 1 time by &8881
.savchk
    lda fs_load_addr,y                                                ; 8879: b9 b0 00    ...            ; Check if new pos overshot end addr
    sbc l00b4,y                                                       ; 887c: f9 b4 00    ...
    iny                                                               ; 887f: c8          .
    dex                                                               ; 8880: ca          .
    bne savchk                                                        ; 8881: d0 f6       ..
    bcc c888e                                                         ; 8883: 90 09       ..
    ldx #3                                                            ; 8885: a2 03       ..             ; Overshot: clamp dest to end address
; &8887 referenced 1 time by &888c
.loop_c8887
    lda l00b4,x                                                       ; 8887: b5 b4       ..
    sta l00c8,x                                                       ; 8889: 95 c8       ..
    dex                                                               ; 888b: ca          .
    bpl loop_c8887                                                    ; 888c: 10 f9       ..
; &888e referenced 1 time by &8883
.c888e
    pla                                                               ; 888e: 68          h              ; Recover original FS command byte
    pha                                                               ; 888f: 48          H
    php                                                               ; 8890: 08          .
    sta l00c1                                                         ; 8891: 85 c1       ..
    lda #&80                                                          ; 8893: a9 80       ..             ; 128-byte block size for data transfer
    sta l00c0                                                         ; 8895: 85 c0       ..
    jsr setup_tx_ptr_c0                                               ; 8897: 20 f7 85     ..
    lda fs_error_ptr                                                  ; 889a: a5 b8       ..             ; ACK port for flow control
    jsr init_tx_ctrl_port                                             ; 889c: 20 89 83     ..
    plp                                                               ; 889f: 28          (
    bcs c88cd                                                         ; 88a0: b0 2b       .+
    lda #&91                                                          ; 88a2: a9 91       ..             ; Command &91 = data block transfer
    sta l00c1                                                         ; 88a4: 85 c1       ..
    inc l00c4                                                         ; 88a6: e6 c4       ..             ; Skip command code byte in TX buffer
    jsr c8530                                                         ; 88a8: 20 30 85     0.
    bne c8859                                                         ; 88ab: d0 ac       ..             ; More blocks? Loop back
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
    pha                                                               ; 88ad: 48          H
    txa                                                               ; 88ae: 8a          .
    jsr handle_to_mask_a                                              ; 88af: 20 9a 86     ..
    tya                                                               ; 88b2: 98          .
    and fs_eof_flags                                                  ; 88b3: 2d 07 0e    -..            ; Local hint: is EOF possible for this handle?
    tax                                                               ; 88b6: aa          .
    beq c88cd                                                         ; 88b7: f0 14       ..             ; Hint clear: definitely not at EOF
    pha                                                               ; 88b9: 48          H
    sty fs_cmd_data                                                   ; 88ba: 8c 05 0f    ...
    ldy #&11                                                          ; 88bd: a0 11       ..             ; Y=function code for HDRFN
    ldx #1                                                            ; 88bf: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 88c1: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    pla                                                               ; 88c4: 68          h
    ldx fs_cmd_data                                                   ; 88c5: ae 05 0f    ...            ; FS reply: non-zero = at EOF
    bne c88cd                                                         ; 88c8: d0 03       ..
    jsr clear_fs_flag                                                 ; 88ca: 20 d5 86     ..            ; Not at EOF: clear the hint bit
; &88cd referenced 4 times by &8857, &88a0, &88b7, &88c8
.c88cd
    pla                                                               ; 88cd: 68          h
    ldy fs_block_offset                                               ; 88ce: a4 bc       ..
    rts                                                               ; 88d0: 60          `

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
; &88d1 referenced 1 time by &8792
.filev_attrib_dispatch
    sta fs_cmd_data                                                   ; 88d1: 8d 05 0f    ...
    cmp #6                                                            ; 88d4: c9 06       ..
    beq cha6                                                          ; 88d6: f0 3f       .?
    bcs c8922                                                         ; 88d8: b0 48       .H             ; A>=7: unsupported, fall through to return
    cmp #5                                                            ; 88da: c9 05       ..
    beq cha5                                                          ; 88dc: f0 52       .R
    cmp #4                                                            ; 88de: c9 04       ..
    beq cha4                                                          ; 88e0: f0 44       .D
    cmp #1                                                            ; 88e2: c9 01       ..
    beq get_file_protection                                           ; 88e4: f0 15       ..
    asl a                                                             ; 88e6: 0a          .              ; A=2 or 3: convert to param block offset
    asl a                                                             ; 88e7: 0a          .
    tay                                                               ; 88e8: a8          .
    jsr sub_3_from_y                                                  ; 88e9: 20 4f 88     O.            ; Y = A*4 - 3 (load addr offset for A=2)
    ldx #3                                                            ; 88ec: a2 03       ..
; &88ee referenced 1 time by &88f5
.chalp1
    lda (fs_options),y                                                ; 88ee: b1 bb       ..
    sta l0f06,x                                                       ; 88f0: 9d 06 0f    ...
    dey                                                               ; 88f3: 88          .
    dex                                                               ; 88f4: ca          .
    bpl chalp1                                                        ; 88f5: 10 f7       ..
    ldx #5                                                            ; 88f7: a2 05       ..
    bne copy_filename_to_cmd                                          ; 88f9: d0 15       ..             ; ALWAYS branch

; &88fb referenced 1 time by &88e4
.get_file_protection
    jsr decode_attribs_6bit                                           ; 88fb: 20 cf 85     ..            ; A=1: encode protection from param block
    sta l0f0e                                                         ; 88fe: 8d 0e 0f    ...
    ldy #9                                                            ; 8901: a0 09       ..
    ldx #8                                                            ; 8903: a2 08       ..
; &8905 referenced 1 time by &890c
.chalp2
    lda (fs_options),y                                                ; 8905: b1 bb       ..
    sta fs_cmd_data,x                                                 ; 8907: 9d 05 0f    ...
    dey                                                               ; 890a: 88          .
    dex                                                               ; 890b: ca          .
    bne chalp2                                                        ; 890c: d0 f7       ..
    ldx #&0a                                                          ; 890e: a2 0a       ..
; &8910 referenced 2 times by &88f9, &892e
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 8910: 20 84 8d     ..
    ldy #&13                                                          ; 8913: a0 13       ..
    bne c891c                                                         ; 8915: d0 05       ..             ; ALWAYS branch

; &8917 referenced 1 time by &88d6
.cha6
    jsr infol2                                                        ; 8917: 20 82 8d     ..
    ldy #&14                                                          ; 891a: a0 14       ..
; &891c referenced 1 time by &8915
.c891c
    bit l83b3                                                         ; 891c: 2c b3 83    ,..
    jsr init_tx_ctrl_data                                             ; 891f: 20 c8 83     ..
; &8922 referenced 1 time by &88d8
.c8922
    bcs c8966                                                         ; 8922: b0 42       .B
    bcc c8997                                                         ; 8924: 90 71       .q             ; ALWAYS branch

; &8926 referenced 1 time by &88e0
.cha4
    jsr decode_attribs_6bit                                           ; 8926: 20 cf 85     ..
    sta l0f06                                                         ; 8929: 8d 06 0f    ...
    ldx #2                                                            ; 892c: a2 02       ..
    bne copy_filename_to_cmd                                          ; 892e: d0 e0       ..             ; ALWAYS branch

; &8930 referenced 1 time by &88dc
.cha5
    ldx #1                                                            ; 8930: a2 01       ..
    jsr copy_string_to_cmd                                            ; 8932: 20 84 8d     ..
    ldy #&12                                                          ; 8935: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8937: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    lda l0f11                                                         ; 893a: ad 11 0f    ...            ; Save object type from FS reply
    stx l0f11                                                         ; 893d: 8e 11 0f    ...            ; X=0 on success, &D6 on not-found
    stx l0f14                                                         ; 8940: 8e 14 0f    ...
    jsr decode_attribs_5bit                                           ; 8943: 20 d9 85     ..            ; Decode 5-bit access byte from FS reply
    ldy #&0e                                                          ; 8946: a0 0e       ..
    sta (fs_options),y                                                ; 8948: 91 bb       ..             ; Store decoded attrs at param block +&0E
    dey                                                               ; 894a: 88          .              ; Y=&0d
    ldx #&0c                                                          ; 894b: a2 0c       ..
; &894d referenced 1 time by &8954
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 894d: bd 05 0f    ...
    sta (fs_options),y                                                ; 8950: 91 bb       ..
    dey                                                               ; 8952: 88          .
    dex                                                               ; 8953: ca          .
    bne copy_fs_reply_to_cb                                           ; 8954: d0 f7       ..
    inx                                                               ; 8956: e8          .
    inx                                                               ; 8957: e8          .
    ldy #&11                                                          ; 8958: a0 11       ..
; &895a referenced 1 time by &8961
.cha5lp
    lda l0f12,x                                                       ; 895a: bd 12 0f    ...
    sta (fs_options),y                                                ; 895d: 91 bb       ..
    dey                                                               ; 895f: 88          .
    dex                                                               ; 8960: ca          .
    bpl cha5lp                                                        ; 8961: 10 f7       ..
    lda fs_cmd_data                                                   ; 8963: ad 05 0f    ...            ; Return object type in A
; &8966 referenced 1 time by &8922
.c8966
    bpl c89b5                                                         ; 8966: 10 4d       .M
; ***************************************************************************************
; ARGSV handler (OSARGS entry point)
; 
;   A=0, Y=0: return filing system number (5 = network FS)
;   A=0, Y>0: read file pointer via FS command &0C (FCRDSE)
;   A=1, Y>0: write file pointer via FS command &0D (FCWRSE)
;   A=2, Y=0: return &01 (command-line tail supported)
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
    jsr save_fscv_args                                                ; 8968: 20 4d 86     M.
    cmp #3                                                            ; 896b: c9 03       ..
    bcs restore_args_return                                           ; 896d: b0 44       .D             ; A>=3 (ensure/flush): no-op for NFS
    cpy #0                                                            ; 896f: c0 00       ..
    beq c89ba                                                         ; 8971: f0 47       .G
    jsr handle_to_mask_clc                                            ; 8973: 20 9b 86     ..
    sty fs_cmd_data                                                   ; 8976: 8c 05 0f    ...
    lsr a                                                             ; 8979: 4a          J              ; LSR splits A: C=1 means write (A=1)
    sta l0f06                                                         ; 897a: 8d 06 0f    ...
    bcs save_args_handle                                              ; 897d: b0 1a       ..             ; C=1: write path, copy ptr from caller
    ldy #&0c                                                          ; 897f: a0 0c       ..             ; Y=function code for HDRFN
    ldx #2                                                            ; 8981: a2 02       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8983: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 8986: 85 bd       ..             ; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 8988: a6 bb       ..
    ldy #2                                                            ; 898a: a0 02       ..
    sta l0003,x                                                       ; 898c: 95 03       ..             ; Zero high byte of 3-byte pointer
; &898e referenced 1 time by &8995
.loop_c898e
    lda fs_cmd_data,y                                                 ; 898e: b9 05 0f    ...
    sta l0002,x                                                       ; 8991: 95 02       ..
    dex                                                               ; 8993: ca          .
    dey                                                               ; 8994: 88          .
    bpl loop_c898e                                                    ; 8995: 10 f7       ..
; &8997 referenced 1 time by &8924
.c8997
    bcc restore_args_return                                           ; 8997: 90 1a       ..
; &8999 referenced 1 time by &897d
.save_args_handle
    tya                                                               ; 8999: 98          .
    pha                                                               ; 899a: 48          H
    ldy #3                                                            ; 899b: a0 03       ..
; &899d referenced 1 time by &89a4
.loop_c899d
    lda l0003,x                                                       ; 899d: b5 03       ..
    sta l0f07,y                                                       ; 899f: 99 07 0f    ...
    dex                                                               ; 89a2: ca          .
    dey                                                               ; 89a3: 88          .
    bpl loop_c899d                                                    ; 89a4: 10 f7       ..
    ldy #&0d                                                          ; 89a6: a0 0d       ..             ; Y=function code for HDRFN
    ldx #5                                                            ; 89a8: a2 05       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 89aa: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 89ad: 86 bd       ..             ; X=0 on success, &D6 on not-found
    pla                                                               ; 89af: 68          h
    jsr sub_c86d0                                                     ; 89b0: 20 d0 86     ..
; ***************************************************************************************
; Restore arguments and return
; 
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
; fs_block_offset (&BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; ***************************************************************************************
; &89b3 referenced 7 times by &871a, &882c, &896d, &8997, &8a2a, &8a7d, &8e35
.restore_args_return
    lda fs_last_byte_flag                                             ; 89b3: a5 bd       ..
; &89b5 referenced 5 times by &8966, &89c6, &89d6, &8a01, &8a0e
.c89b5
    ldx fs_options                                                    ; 89b5: a6 bb       ..
    ldy fs_block_offset                                               ; 89b7: a4 bc       ..
    rts                                                               ; 89b9: 60          `

; &89ba referenced 1 time by &8971
.c89ba
    cmp #2                                                            ; 89ba: c9 02       ..             ; Y=0: FS-level queries (no file handle)
    beq c89c5                                                         ; 89bc: f0 07       ..
    bcs c89d4                                                         ; 89be: b0 14       ..
    tay                                                               ; 89c0: a8          .
    bne osarg1                                                        ; 89c1: d0 05       ..
    lda #&0a                                                          ; 89c3: a9 0a       ..             ; FS number 5 (loaded as &0A, LSR'd)
; &89c5 referenced 1 time by &89bc
.c89c5
    lsr a                                                             ; 89c5: 4a          J              ; Shared: A=0->&05, A=2->&01
    bne c89b5                                                         ; 89c6: d0 ed       ..
; &89c8 referenced 2 times by &89c1, &89ce
.osarg1
    lda fs_cmd_context,y                                              ; 89c8: b9 0a 0e    ...            ; Copy command context to caller's block
    sta (fs_options),y                                                ; 89cb: 91 bb       ..
    dey                                                               ; 89cd: 88          .
    bpl osarg1                                                        ; 89ce: 10 f8       ..
    sty l0002,x                                                       ; 89d0: 94 02       ..
    sty l0003,x                                                       ; 89d2: 94 03       ..
; &89d4 referenced 4 times by &89be, &89e4, &8b19, &8bbb
.c89d4
    lda #0                                                            ; 89d4: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl c89b5                                                         ; 89d6: 10 dd       ..             ; ALWAYS branch

; ***************************************************************************************
; FINDV handler (OSFIND entry point)
; 
;   A=0: close file -- delegates to close_handle (&8A10)
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
    jsr save_fscv_args_with_ptrs                                      ; 89d8: 20 49 86     I.
    sec                                                               ; 89db: 38          8              ; SEC distinguishes open (A>0) from close
    jsr handle_to_mask                                                ; 89dc: 20 9c 86     ..            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 89df: aa          .              ; A=preserved
    beq close_handle                                                  ; 89e0: f0 2e       ..
    and #&3f ; '?'                                                    ; 89e2: 29 3f       )?             ; Valid open modes: &40, &80, &C0 only
    bne c89d4                                                         ; 89e4: d0 ee       ..
    txa                                                               ; 89e6: 8a          .
    eor #&80                                                          ; 89e7: 49 80       I.             ; Convert MOS mode to FS protocol flags
    asl a                                                             ; 89e9: 0a          .
    sta fs_cmd_data                                                   ; 89ea: 8d 05 0f    ...            ; Flag 1: read/write direction
    rol a                                                             ; 89ed: 2a          *
    sta l0f06                                                         ; 89ee: 8d 06 0f    ...            ; Flag 2: create vs existing file
    jsr parse_filename_gs                                             ; 89f1: 20 e8 86     ..
    ldx #2                                                            ; 89f4: a2 02       ..
    jsr copy_string_to_cmd                                            ; 89f6: 20 84 8d     ..
    ldy #6                                                            ; 89f9: a0 06       ..
    bit l83b3                                                         ; 89fb: 2c b3 83    ,..
    jsr init_tx_ctrl_data                                             ; 89fe: 20 c8 83     ..
    bcs c89b5                                                         ; 8a01: b0 b2       ..
    lda fs_cmd_data                                                   ; 8a03: ad 05 0f    ...
    tax                                                               ; 8a06: aa          .
    jsr sub_c86d0                                                     ; 8a07: 20 d0 86     ..
; 3.35K fix: OR handle bit into fs_sequence_nos
; (&0E08). Without this, a newly opened file could
; inherit a stale sequence number from a previous
; file using the same handle, causing byte-stream
; protocol errors.
    txa                                                               ; 8a0a: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8a0b: 20 b7 86     ..            ; Convert bitmask to handle number (FS2A)
    bne c89b5                                                         ; 8a0e: d0 a5       ..
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
; &8a10 referenced 1 time by &89e0
.close_handle
    tya                                                               ; 8a10: 98          .              ; Y=preserved
    bne close_single_handle                                           ; 8a11: d0 07       ..
    lda #osbyte_close_spool_exec                                      ; 8a13: a9 77       .w
    jsr osbyte                                                        ; 8a15: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 8a18: a0 00       ..
; &8a1a referenced 1 time by &8a11
.close_single_handle
    sty fs_cmd_data                                                   ; 8a1a: 8c 05 0f    ...
    ldx #1                                                            ; 8a1d: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 8a1f: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8a21: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8a24: ad 05 0f    ...
    jsr sub_c86d0                                                     ; 8a27: 20 d0 86     ..
; &8a2a referenced 1 time by &8a50
.c8a2a
    bcc restore_args_return                                           ; 8a2a: 90 87       ..
.fscv_0_opt_entry
    beq c8a39                                                         ; 8a2c: f0 0b       ..
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; ***************************************************************************************
.fscv_0_opt
    cpx #4                                                            ; 8a2e: e0 04       ..
    bne c8a36                                                         ; 8a30: d0 04       ..
    cpy #4                                                            ; 8a32: c0 04       ..
    bcc optl1                                                         ; 8a34: 90 0d       ..
; &8a36 referenced 1 time by &8a30
.c8a36
    dex                                                               ; 8a36: ca          .              ; Not *OPT 4: check for *OPT 1
    bne opter1                                                        ; 8a37: d0 05       ..
; &8a39 referenced 1 time by &8a2c
.c8a39
    sty fs_messages_flag                                              ; 8a39: 8c 06 0e    ...            ; Set local messages flag (*OPT 1,Y)
    bcc c8a50                                                         ; 8a3c: 90 12       ..
; &8a3e referenced 1 time by &8a37
.opter1
    lda #7                                                            ; 8a3e: a9 07       ..
    jmp nlisne                                                        ; 8a40: 4c 12 85    L..

; &8a43 referenced 1 time by &8a34
.optl1
    sty fs_cmd_data                                                   ; 8a43: 8c 05 0f    ...
    ldy #&16                                                          ; 8a46: a0 16       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8a48: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 8a4b: a4 bc       ..
    sty fs_boot_option                                                ; 8a4d: 8c 05 0e    ...            ; Cache boot option locally
; &8a50 referenced 1 time by &8a3c
.c8a50
    bcc c8a2a                                                         ; 8a50: 90 d8       ..
; &8a52 referenced 1 time by &8b0d
.adjust_addrs_9
    ldy #9                                                            ; 8a52: a0 09       ..
    jsr adjust_addrs_clc                                              ; 8a54: 20 59 8a     Y.
; &8a57 referenced 1 time by &8c02
.adjust_addrs_1
    ldy #1                                                            ; 8a57: a0 01       ..
; &8a59 referenced 1 time by &8a54
.adjust_addrs_clc
    clc                                                               ; 8a59: 18          .
; ***************************************************************************************
; Bidirectional 4-byte address adjustment
; 
; Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
;   If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
;   If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
; Starting offset X=&FC means it reads from &0E06-&0E09 area.
; Used to convert between absolute and relative file positions.
; ***************************************************************************************
; &8a5a referenced 2 times by &8b13, &8c0e
.adjust_addrs
    ldx #&fc                                                          ; 8a5a: a2 fc       ..             ; X=&FC: index into &0E06 area (wraps to 0)
; &8a5c referenced 1 time by &8a6f
.loop_c8a5c
    lda (fs_options),y                                                ; 8a5c: b1 bb       ..             ; Load byte from param block
    bit fs_load_addr_2                                                ; 8a5e: 24 b2       $.             ; Test sign of adjustment direction
    bmi c8a68                                                         ; 8a60: 30 06       0.             ; Negative: subtract instead
    adc fs_cmd_context,x                                              ; 8a62: 7d 0a 0e    }..            ; Add adjustment value
    jmp gbpbx                                                         ; 8a65: 4c 6b 8a    Lk.            ; Skip to store result

; &8a68 referenced 1 time by &8a60
.c8a68
    sbc fs_cmd_context,x                                              ; 8a68: fd 0a 0e    ...            ; Subtract adjustment value
; &8a6b referenced 1 time by &8a65
.gbpbx
    sta (fs_options),y                                                ; 8a6b: 91 bb       ..             ; Store adjusted byte back
    iny                                                               ; 8a6d: c8          .              ; Next param block byte
    inx                                                               ; 8a6e: e8          .              ; Next adjustment byte (X wraps &FC->&00)
    bne loop_c8a5c                                                    ; 8a6f: d0 eb       ..             ; Loop 4 times (X=&FC,&FD,&FE,&FF,done)
    rts                                                               ; 8a71: 60          `

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
    jsr save_fscv_args                                                ; 8a72: 20 4d 86     M.
    tax                                                               ; 8a75: aa          .
    beq c8a7d                                                         ; 8a76: f0 05       ..
    dex                                                               ; 8a78: ca          .              ; Convert to 0-based (A=0..7)
    cpx #8                                                            ; 8a79: e0 08       ..
    bcc gbpbx1                                                        ; 8a7b: 90 03       ..
; &8a7d referenced 1 time by &8a76
.c8a7d
    jmp restore_args_return                                           ; 8a7d: 4c b3 89    L..

; &8a80 referenced 1 time by &8a7b
.gbpbx1
    txa                                                               ; 8a80: 8a          .
    ldy #0                                                            ; 8a81: a0 00       ..
    pha                                                               ; 8a83: 48          H
    cmp #4                                                            ; 8a84: c9 04       ..             ; A>=4: info queries, dispatch separately
    bcc gbpbe1                                                        ; 8a86: 90 03       ..
    jmp osgbpb_info                                                   ; 8a88: 4c 31 8b    L1.

; &8a8b referenced 1 time by &8a86
.gbpbe1
    lda (fs_options),y                                                ; 8a8b: b1 bb       ..             ; Get file handle from param block byte 0
    jsr handle_to_mask_a                                              ; 8a8d: 20 9a 86     ..
    sty fs_cmd_data                                                   ; 8a90: 8c 05 0f    ...
    ldy #&0b                                                          ; 8a93: a0 0b       ..
    ldx #6                                                            ; 8a95: a2 06       ..
; &8a97 referenced 1 time by &8aa3
.gbpbf1
    lda (fs_options),y                                                ; 8a97: b1 bb       ..
    sta l0f06,x                                                       ; 8a99: 9d 06 0f    ...
    dey                                                               ; 8a9c: 88          .
    cpy #8                                                            ; 8a9d: c0 08       ..             ; Skip param block offset 8 (the handle)
    bne gbpbx0                                                        ; 8a9f: d0 01       ..
    dey                                                               ; 8aa1: 88          .
; &8aa2 referenced 1 time by &8a9f
.gbpbx0
.gbpbf2
    dex                                                               ; 8aa2: ca          .
    bne gbpbf1                                                        ; 8aa3: d0 f2       ..
    pla                                                               ; 8aa5: 68          h
    lsr a                                                             ; 8aa6: 4a          J              ; LSR: odd=read (C=1), even=write (C=0)
    pha                                                               ; 8aa7: 48          H
    bcc gbpbl1                                                        ; 8aa8: 90 01       ..
    inx                                                               ; 8aaa: e8          .
; &8aab referenced 1 time by &8aa8
.gbpbl1
    stx l0f06                                                         ; 8aab: 8e 06 0f    ...            ; Store FS direction flag
    ldy #&0b                                                          ; 8aae: a0 0b       ..
    ldx #&91                                                          ; 8ab0: a2 91       ..             ; Command &91=put, &92=get
    pla                                                               ; 8ab2: 68          h
    pha                                                               ; 8ab3: 48          H
    beq c8ab9                                                         ; 8ab4: f0 03       ..
    ldx #&92                                                          ; 8ab6: a2 92       ..
    dey                                                               ; 8ab8: 88          .              ; Read: one fewer data byte in command; Y=&0a
; &8ab9 referenced 1 time by &8ab4
.c8ab9
    stx fs_cmd_urd                                                    ; 8ab9: 8e 02 0f    ...
    stx fs_error_ptr                                                  ; 8abc: 86 b8       ..
    ldx #8                                                            ; 8abe: a2 08       ..
    lda fs_cmd_data                                                   ; 8ac0: ad 05 0f    ...
    jsr prepare_cmd_with_flag                                         ; 8ac3: 20 b9 83     ..
    lda l00b3                                                         ; 8ac6: a5 b3       ..             ; Save seq# for byte-stream flow control
    sta fs_sequence_nos                                               ; 8ac8: 8d 08 0e    ...
    ldx #4                                                            ; 8acb: a2 04       ..
; &8acd referenced 1 time by &8ae1
.gbpbl3
    lda (fs_options),y                                                ; 8acd: b1 bb       ..             ; Set up source/dest from param block
    sta l00af,y                                                       ; 8acf: 99 af 00    ...
    sta l00c7,y                                                       ; 8ad2: 99 c7 00    ...
    jsr add_4_to_y                                                    ; 8ad5: 20 3c 88     <.            ; Skip 4 bytes to reach transfer length
    adc (fs_options),y                                                ; 8ad8: 71 bb       q.             ; Dest = source + length
    sta l00af,y                                                       ; 8ada: 99 af 00    ...
    jsr sub_3_from_y                                                  ; 8add: 20 4f 88     O.
    dex                                                               ; 8ae0: ca          .
    bne gbpbl3                                                        ; 8ae1: d0 ea       ..
    inx                                                               ; 8ae3: e8          .
; &8ae4 referenced 1 time by &8aeb
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8ae4: bd 03 0f    ...
    sta l0f06,x                                                       ; 8ae7: 9d 06 0f    ...
    dex                                                               ; 8aea: ca          .
    bpl gbpbf3                                                        ; 8aeb: 10 f7       ..
    pla                                                               ; 8aed: 68          h              ; Odd (read): send data to FS first
    bne c8af8                                                         ; 8aee: d0 08       ..
    lda fs_cmd_urd                                                    ; 8af0: ad 02 0f    ...
    jsr transfer_file_blocks                                          ; 8af3: 20 53 88     S.            ; Transfer data blocks to fileserver
    bcs c8afb                                                         ; 8af6: b0 03       ..
; &8af8 referenced 1 time by &8aee
.c8af8
    jsr send_data_blocks                                              ; 8af8: 20 65 87     e.
; &8afb referenced 1 time by &8af6
.c8afb
    jsr send_fs_reply_cmd                                             ; 8afb: 20 f3 83     ..
    lda (fs_options,x)                                                ; 8afe: a1 bb       ..
    bit fs_cmd_data                                                   ; 8b00: 2c 05 0f    ,..            ; Check FS reply: bit 7 = not at EOF
    bmi c8b08                                                         ; 8b03: 30 03       0.
    jsr clear_fs_flag                                                 ; 8b05: 20 d5 86     ..            ; At EOF: clear EOF hint for this handle
; &8b08 referenced 1 time by &8b03
.c8b08
    jsr sub_c86d0                                                     ; 8b08: 20 d0 86     ..
    stx fs_load_addr_2                                                ; 8b0b: 86 b2       ..             ; Direction=0: forward adjustment
    jsr adjust_addrs_9                                                ; 8b0d: 20 52 8a     R.
    dec fs_load_addr_2                                                ; 8b10: c6 b2       ..             ; Direction=&FF: reverse adjustment
    sec                                                               ; 8b12: 38          8
    jsr adjust_addrs                                                  ; 8b13: 20 5a 8a     Z.
    asl fs_cmd_data                                                   ; 8b16: 0e 05 0f    ...            ; Shift bit 7 into C for return flag
    jmp c89d4                                                         ; 8b19: 4c d4 89    L..

; &8b1c referenced 1 time by &8b4c
.c8b1c
    ldy #&15                                                          ; 8b1c: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8b1e: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8b21: ad 05 0e    ...
    sta l0f16                                                         ; 8b24: 8d 16 0f    ...
    stx fs_load_addr                                                  ; 8b27: 86 b0       ..             ; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8b29: 86 b1       ..
    lda #&12                                                          ; 8b2b: a9 12       ..
    sta fs_load_addr_2                                                ; 8b2d: 85 b2       ..
    bne copy_reply_to_caller                                          ; 8b2f: d0 4e       .N             ; ALWAYS branch

; ***************************************************************************************
; OSGBPB 5-8 info handler (OSINFO)
; 
; Handles the "messy interface tacked onto OSGBPB" (original source).
; Checks whether the destination address is in Tube space by comparing
; the high bytes against TBFLAG. If in Tube space, data must be
; copied via the Tube FIFO registers (with delays to accommodate the
; slow 16032 co-processor) instead of direct memory access.
; ***************************************************************************************
; &8b31 referenced 1 time by &8a88
.osgbpb_info
    ldy #4                                                            ; 8b31: a0 04       ..
    lda tube_flag                                                     ; 8b33: ad 67 0d    .g.            ; Check if destination is in Tube space
    beq c8b3f                                                         ; 8b36: f0 07       ..
    cmp (fs_options),y                                                ; 8b38: d1 bb       ..
    bne c8b3f                                                         ; 8b3a: d0 03       ..
    dey                                                               ; 8b3c: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8b3d: f1 bb       ..
; &8b3f referenced 2 times by &8b36, &8b3a
.c8b3f
    sta l00a9                                                         ; 8b3f: 85 a9       ..             ; Non-zero = Tube transfer required
; &8b41 referenced 1 time by &8b47
.info2
    lda (fs_options),y                                                ; 8b41: b1 bb       ..             ; Copy param block bytes 1-4 to workspace
    sta fs_last_byte_flag,y                                           ; 8b43: 99 bd 00    ...
    dey                                                               ; 8b46: 88          .
    bne info2                                                         ; 8b47: d0 f8       ..
    pla                                                               ; 8b49: 68          h              ; Sub-function: AND #3 of (original A - 4)
    and #3                                                            ; 8b4a: 29 03       ).
    beq c8b1c                                                         ; 8b4c: f0 ce       ..             ; A=0 (OSGBPB 5): read disc title
    lsr a                                                             ; 8b4e: 4a          J
    beq c8b53                                                         ; 8b4f: f0 02       ..
    bcs c8bbe                                                         ; 8b51: b0 6b       .k
; &8b53 referenced 1 time by &8b4f
.c8b53
    tay                                                               ; 8b53: a8          .              ; Y=function code
    lda fs_csd_handle,y                                               ; 8b54: b9 03 0e    ...            ; Get CSD/LIB/URD handles for FS command
    sta fs_cmd_csd                                                    ; 8b57: 8d 03 0f    ...
    lda fs_lib_handle                                                 ; 8b5a: ad 04 0e    ...
    sta fs_cmd_lib                                                    ; 8b5d: 8d 04 0f    ...
    lda fs_urd_handle                                                 ; 8b60: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8b63: 8d 02 0f    ...
    ldx #&12                                                          ; 8b66: a2 12       ..             ; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8b68: 8e 01 0f    ...
    lda #&0d                                                          ; 8b6b: a9 0d       ..             ; &0D = 13 bytes of reply data expected
    sta l0f06                                                         ; 8b6d: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b70: 85 b2       ..
    lsr a                                                             ; 8b72: 4a          J
    sta fs_cmd_data                                                   ; 8b73: 8d 05 0f    ...
    clc                                                               ; 8b76: 18          .
    jsr build_send_fs_cmd                                             ; 8b77: 20 dd 83     ..            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8b7a: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8b7c: e8          .
    stx fs_load_addr                                                  ; 8b7d: 86 b0       ..
; &8b7f referenced 2 times by &8b2f, &8bf7
.copy_reply_to_caller
    lda l00a9                                                         ; 8b7f: a5 a9       ..             ; Copy FS reply to caller's buffer
    bne c8b94                                                         ; 8b81: d0 11       ..             ; Non-zero: use Tube transfer path
    ldx fs_load_addr                                                  ; 8b83: a6 b0       ..
    ldy fs_load_addr_hi                                               ; 8b85: a4 b1       ..
; &8b87 referenced 1 time by &8b90
.loop_c8b87
    lda fs_cmd_data,x                                                 ; 8b87: bd 05 0f    ...
    sta (fs_crc_lo),y                                                 ; 8b8a: 91 be       ..
    inx                                                               ; 8b8c: e8          .
    iny                                                               ; 8b8d: c8          .
    dec fs_load_addr_2                                                ; 8b8e: c6 b2       ..
    bne loop_c8b87                                                    ; 8b90: d0 f5       ..
    beq c8bbb                                                         ; 8b92: f0 27       .'             ; ALWAYS branch

; &8b94 referenced 1 time by &8b81
.c8b94
    jsr tube_claim_loop                                               ; 8b94: 20 13 8c     ..
    lda #1                                                            ; 8b97: a9 01       ..
    ldx fs_options                                                    ; 8b99: a6 bb       ..
    ldy fs_block_offset                                               ; 8b9b: a4 bc       ..
    inx                                                               ; 8b9d: e8          .
    bne c8ba1                                                         ; 8b9e: d0 01       ..
    iny                                                               ; 8ba0: c8          .
; &8ba1 referenced 1 time by &8b9e
.c8ba1
    jsr tube_addr_claim                                               ; 8ba1: 20 06 04     ..
    ldx fs_load_addr                                                  ; 8ba4: a6 b0       ..
; &8ba6 referenced 1 time by &8bb4
.tbcop1
    lda fs_cmd_data,x                                                 ; 8ba6: bd 05 0f    ...
    sta tube_data_register_3                                          ; 8ba9: 8d e5 fe    ...
    inx                                                               ; 8bac: e8          .
    ldy #6                                                            ; 8bad: a0 06       ..             ; Delay loop for slow Tube co-processor
; &8baf referenced 1 time by &8bb0
.loop_c8baf
    dey                                                               ; 8baf: 88          .
    bne loop_c8baf                                                    ; 8bb0: d0 fd       ..
    dec fs_load_addr_2                                                ; 8bb2: c6 b2       ..
    bne tbcop1                                                        ; 8bb4: d0 f0       ..
    lda #&83                                                          ; 8bb6: a9 83       ..             ; Release Tube after transfer complete
    jsr tube_addr_claim                                               ; 8bb8: 20 06 04     ..
; &8bbb referenced 2 times by &8b92, &8c11
.c8bbb
    jmp c89d4                                                         ; 8bbb: 4c d4 89    L..

; &8bbe referenced 1 time by &8b51
.c8bbe
    ldy #9                                                            ; 8bbe: a0 09       ..             ; OSGBPB 8: read filenames from dir
    lda (fs_options),y                                                ; 8bc0: b1 bb       ..
    sta l0f06                                                         ; 8bc2: 8d 06 0f    ...
    ldy #5                                                            ; 8bc5: a0 05       ..
    lda (fs_options),y                                                ; 8bc7: b1 bb       ..
    sta l0f07                                                         ; 8bc9: 8d 07 0f    ...
    ldx #&0d                                                          ; 8bcc: a2 0d       ..             ; X=preserved through header build
    stx l0f08                                                         ; 8bce: 8e 08 0f    ...
    ldy #2                                                            ; 8bd1: a0 02       ..
    sty fs_load_addr                                                  ; 8bd3: 84 b0       ..
    sty fs_cmd_data                                                   ; 8bd5: 8c 05 0f    ...
    iny                                                               ; 8bd8: c8          .              ; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8bd9: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8bdc: 86 b1       ..             ; X=0 on success, &D6 on not-found
    lda l0f06                                                         ; 8bde: ad 06 0f    ...
    sta (fs_options,x)                                                ; 8be1: 81 bb       ..
    lda fs_cmd_data                                                   ; 8be3: ad 05 0f    ...
    ldy #9                                                            ; 8be6: a0 09       ..
    adc (fs_options),y                                                ; 8be8: 71 bb       q.
    sta (fs_options),y                                                ; 8bea: 91 bb       ..
    lda l00c8                                                         ; 8bec: a5 c8       ..
    sbc #7                                                            ; 8bee: e9 07       ..             ; Subtract header (7 bytes) from reply len
    sta l0f06                                                         ; 8bf0: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8bf3: 85 b2       ..
    beq c8bfa                                                         ; 8bf5: f0 03       ..
    jsr copy_reply_to_caller                                          ; 8bf7: 20 7f 8b     ..
; &8bfa referenced 1 time by &8bf5
.c8bfa
    ldx #2                                                            ; 8bfa: a2 02       ..
; &8bfc referenced 1 time by &8c00
.loop_c8bfc
    sta l0f07,x                                                       ; 8bfc: 9d 07 0f    ...
    dex                                                               ; 8bff: ca          .
    bpl loop_c8bfc                                                    ; 8c00: 10 fa       ..
    jsr adjust_addrs_1                                                ; 8c02: 20 57 8a     W.            ; Adjust pointer by +1 (one filename read)
    sec                                                               ; 8c05: 38          8
    dec fs_load_addr_2                                                ; 8c06: c6 b2       ..             ; Reverse adjustment for updated counter
    lda fs_cmd_data                                                   ; 8c08: ad 05 0f    ...
    sta l0f06                                                         ; 8c0b: 8d 06 0f    ...
    jsr adjust_addrs                                                  ; 8c0e: 20 5a 8a     Z.
    beq c8bbb                                                         ; 8c11: f0 a8       ..
; &8c13 referenced 3 times by &8b94, &8c18, &8e1d
.tube_claim_loop
    lda #&c3                                                          ; 8c13: a9 c3       ..
    jsr tube_addr_claim                                               ; 8c15: 20 06 04     ..
    bcc tube_claim_loop                                               ; 8c18: 90 f9       ..
    rts                                                               ; 8c1a: 60          `

; ***************************************************************************************
; FSCV 2/3/4: unrecognised * command handler (DECODE)
; 
; CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text
; against the table
; at &8C4B using case-insensitive comparison with abbreviation
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
.fscv_3_star_cmd
    jsr save_fscv_args_with_ptrs                                      ; 8c1b: 20 49 86     I.
    ldx #&ff                                                          ; 8c1e: a2 ff       ..
    stx l00b9                                                         ; 8c20: 86 b9       ..
    stx escapable                                                     ; 8c22: 86 97       ..
; &8c24 referenced 1 time by &8c3f
.loop_c8c24
    ldy #&ff                                                          ; 8c24: a0 ff       ..
; &8c26 referenced 1 time by &8c31
.decfir
    iny                                                               ; 8c26: c8          .
    inx                                                               ; 8c27: e8          .
; &8c28 referenced 1 time by &8c43
.decmor
    lda fs_cmd_match_table,x                                          ; 8c28: bd 4b 8c    .K.
    bmi c8c45                                                         ; 8c2b: 30 18       0.
    eor (fs_crc_lo),y                                                 ; 8c2d: 51 be       Q.
    and #&df                                                          ; 8c2f: 29 df       ).
    beq decfir                                                        ; 8c31: f0 f3       ..
    dex                                                               ; 8c33: ca          .
; &8c34 referenced 1 time by &8c38
.decmin
    inx                                                               ; 8c34: e8          .
    lda fs_cmd_match_table,x                                          ; 8c35: bd 4b 8c    .K.
    bpl decmin                                                        ; 8c38: 10 fa       ..
    lda (fs_crc_lo),y                                                 ; 8c3a: b1 be       ..
    inx                                                               ; 8c3c: e8          .
    cmp #&2e ; '.'                                                    ; 8c3d: c9 2e       ..
    bne loop_c8c24                                                    ; 8c3f: d0 e3       ..
    iny                                                               ; 8c41: c8          .
    dex                                                               ; 8c42: ca          .
    bcs decmor                                                        ; 8c43: b0 e3       ..
; &8c45 referenced 1 time by &8c2b
.c8c45
    pha                                                               ; 8c45: 48          H
    lda l8c4c,x                                                       ; 8c46: bd 4c 8c    .L.
    pha                                                               ; 8c49: 48          H
    rts                                                               ; 8c4a: 60          `

; ***************************************************************************************
; FS command match table (COMTAB)
; 
; Format: command letters (bit 7 clear), then dispatch address
; as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
; adds 1 to the stored (address-1). Matching is case-insensitive
; (AND &DF) and supports '.' abbreviation (standard Acorn pattern).
; 
; Entries:
;   "I."     → &80C1 (forward_star_cmd) — placed first as a fudge
;              to catch *I. abbreviation before matching *I AM
;   "I AM"   → &8082 (i_am_handler: parse station.net, logon)
;   "EX"     → &8C61 (ex_handler: embedded in table tail)
;   "BYE"\r  → &83C0 (bye_handler: logoff)
;   <catch-all> → &80C1 (forward anything else to FS)
; ***************************************************************************************
; &8c4b referenced 2 times by &8c28, &8c35
.fs_cmd_match_table
l8c4c = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8c4b: 49 2e       I.
; &8c4c referenced 1 time by &8c46
    equb &80, &c0                                                     ; 8c4d: 80 c0       ..
    equs "I AM"                                                       ; 8c4f: 49 20 41... I A
    equb &80, &81, &45, &58, &8c                                      ; 8c53: 80 81 45... ..E
    equs "`BYE"                                                       ; 8c58: 60 42 59... `BY
    equb &0d, &83, &bf, &80, &c0                                      ; 8c5c: 0d 83 bf... ...

.ex_handler
    ldx #1                                                            ; 8c61: a2 01       ..
    lda #3                                                            ; 8c63: a9 03       ..
    bne c8c72                                                         ; 8c65: d0 0b       ..             ; ALWAYS branch

; ***************************************************************************************
; *CAT handler (directory catalogue)
; 
; Initialises &B5=&0B (examine arg count) and &B7=&03 (column
; count). The catalogue protocol is multi-step: first sends
; FCREAD (&12: examine) to get the directory header, then sends
; FCUSER (&15: read user environment) to get CSD, disc, and
; library names, then sends FC &03 (examine entries) repeatedly
; to fetch entries in batches until zero are returned (end of dir).
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
;   - Directory entries: CRFLAG (&B9) cycles 0-3 for multi-column
;     layout; at count 0 a newline is printed, others get spaces.
;     *EX sets CRFLAG=&FF to force one entry per line.
; ***************************************************************************************
.fscv_5_cat
    ldx #3                                                            ; 8c67: a2 03       ..
    stx l00b9                                                         ; 8c69: 86 b9       ..             ; CRFLAG=3: first entry will trigger newline
    ldy #&ff                                                          ; 8c6b: a0 ff       ..
    sty escapable                                                     ; 8c6d: 84 97       ..
    iny                                                               ; 8c6f: c8          .              ; Y=&00
    lda #&0b                                                          ; 8c70: a9 0b       ..
; &8c72 referenced 1 time by &8c65
.c8c72
    sta l00b5                                                         ; 8c72: 85 b5       ..
    stx l00b7                                                         ; 8c74: 86 b7       ..
    lda #6                                                            ; 8c76: a9 06       ..
    sta fs_cmd_data                                                   ; 8c78: 8d 05 0f    ...
    jsr sub_c86ea                                                     ; 8c7b: 20 ea 86     ..
    ldx #1                                                            ; 8c7e: a2 01       ..
    jsr copy_string_to_cmd                                            ; 8c80: 20 84 8d     ..
    ldy #&12                                                          ; 8c83: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c85: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c88: a2 03       ..
    jsr print_reply_bytes                                             ; 8c8a: 20 47 8d     G.
    jsr print_inline                                                  ; 8c8d: 20 5c 86     \.
    equs "("                                                          ; 8c90: 28          (

    lda l0f13                                                         ; 8c91: ad 13 0f    ...
    jsr print_decimal                                                 ; 8c94: 20 bd 8d     ..
    jsr print_inline                                                  ; 8c97: 20 5c 86     \.
    equs ")     "                                                     ; 8c9a: 29 20 20... )

    ldy l0f12                                                         ; 8ca0: ac 12 0f    ...            ; Access level byte: 0=Owner, non-zero=Public
    bne c8cb0                                                         ; 8ca3: d0 0b       ..
    jsr print_inline                                                  ; 8ca5: 20 5c 86     \.
    equs "Owner", &0d                                                 ; 8ca8: 4f 77 6e... Own

    bne c8cba                                                         ; 8cae: d0 0a       ..
; &8cb0 referenced 1 time by &8ca3
.c8cb0
    jsr print_inline                                                  ; 8cb0: 20 5c 86     \.
    equs "Public", &0d                                                ; 8cb3: 50 75 62... Pub

; &8cba referenced 1 time by &8cae
.c8cba
    ldy #&15                                                          ; 8cba: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cbc: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8cbf: e8          .
    ldy #&10                                                          ; 8cc0: a0 10       ..
    jsr print_reply_counted                                           ; 8cc2: 20 49 8d     I.
    jsr print_inline                                                  ; 8cc5: 20 5c 86     \.
    equs "    Option "                                                ; 8cc8: 20 20 20...

    lda fs_boot_option                                                ; 8cd3: ad 05 0e    ...
    tax                                                               ; 8cd6: aa          .
    jsr print_hex                                                     ; 8cd7: 20 9d 9f     ..
    jsr print_inline                                                  ; 8cda: 20 5c 86     \.
    equs " ("                                                         ; 8cdd: 20 28        (

    ldy l8d54,x                                                       ; 8cdf: bc 54 8d    .T.
; &8ce2 referenced 1 time by &8ceb
.loop_c8ce2
    lda l8d54,y                                                       ; 8ce2: b9 54 8d    .T.
    bmi c8ced                                                         ; 8ce5: 30 06       0.
    jsr osasci                                                        ; 8ce7: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8cea: c8          .
    bne loop_c8ce2                                                    ; 8ceb: d0 f5       ..
; &8ced referenced 1 time by &8ce5
.c8ced
    jsr print_inline                                                  ; 8ced: 20 5c 86     \.
    equs ")", &0d, "Dir. "                                            ; 8cf0: 29 0d 44... ).D

    ldx #&11                                                          ; 8cf7: a2 11       ..
    jsr print_reply_bytes                                             ; 8cf9: 20 47 8d     G.
    jsr print_inline                                                  ; 8cfc: 20 5c 86     \.
    equs "     Lib. "                                                 ; 8cff: 20 20 20...

    ldx #&1b                                                          ; 8d09: a2 1b       ..
    jsr print_reply_bytes                                             ; 8d0b: 20 47 8d     G.
    jsr osnewl                                                        ; 8d0e: 20 e7 ff     ..            ; Write newline (characters 10 and 13)
; &8d11 referenced 1 time by &8d45
.c8d11
    sty l0f06                                                         ; 8d11: 8c 06 0f    ...
    sty l00b4                                                         ; 8d14: 84 b4       ..
    ldx l00b5                                                         ; 8d16: a6 b5       ..
    stx l0f07                                                         ; 8d18: 8e 07 0f    ...
    ldx l00b7                                                         ; 8d1b: a6 b7       ..
    stx fs_cmd_data                                                   ; 8d1d: 8e 05 0f    ...
    ldx #3                                                            ; 8d20: a2 03       ..
    jsr copy_string_to_cmd                                            ; 8d22: 20 84 8d     ..
    ldy #3                                                            ; 8d25: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8d27: 20 c7 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8d2a: e8          .
    lda fs_cmd_data                                                   ; 8d2b: ad 05 0f    ...
    bne c8d33                                                         ; 8d2e: d0 03       ..             ; Zero entries returned = end of directory
    jmp osnewl                                                        ; 8d30: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &8d33 referenced 1 time by &8d2e
.c8d33
    pha                                                               ; 8d33: 48          H
; &8d34 referenced 1 time by &8d38
.loop_c8d34
    iny                                                               ; 8d34: c8          .
    lda fs_cmd_data,y                                                 ; 8d35: b9 05 0f    ...
    bpl loop_c8d34                                                    ; 8d38: 10 fa       ..
    sta fs_cmd_lib,y                                                  ; 8d3a: 99 04 0f    ...
    jsr sub_c8d9f                                                     ; 8d3d: 20 9f 8d     ..
    pla                                                               ; 8d40: 68          h
    clc                                                               ; 8d41: 18          .
    adc l00b4                                                         ; 8d42: 65 b4       e.
    tay                                                               ; 8d44: a8          .
    bne c8d11                                                         ; 8d45: d0 ca       ..
; &8d47 referenced 3 times by &8c8a, &8cf9, &8d0b
.print_reply_bytes
    ldy #&0a                                                          ; 8d47: a0 0a       ..
; &8d49 referenced 2 times by &8cc2, &8d51
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8d49: bd 05 0f    ...
    jsr osasci                                                        ; 8d4c: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8d4f: e8          .
    dey                                                               ; 8d50: 88          .
    bne print_reply_counted                                           ; 8d51: d0 f6       ..
; Option name encoding: the boot option names ("Off", "Load",
; "Run", "Exec") are scattered through the code rather than
; stored as a contiguous table. They are addressed via base+offset
; from l8d54 (&8D54), whose four bytes are offsets into page &8D:
;   &2B→&8D7F "Off", &3E→&8D92 "Load",
;   &66→&8DBA "Run", &18→&8D6C "Exec"
; Each string is terminated by the next instruction's opcode
; having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).
.return_9
    rts                                                               ; 8d53: 60          `

; &8d54 referenced 2 times by &8cdf, &8ce2
.l8d54
    equs "+>f"                                                        ; 8d54: 2b 3e 66    +>f
    equb &18                                                          ; 8d57: 18          .
    equs "L.!"                                                        ; 8d58: 4c 2e 21    L.!
; ***************************************************************************************
; Boot command strings for auto-boot
; 
; The four boot options use OSCLI strings at offsets within page &8D.
; The offset table at boot_option_offsets+1 (&8D68) is indexed by
; the boot option value (0-3); each byte is the low byte of the
; string address, with the page high byte &8D loaded separately:
;   Option 0 (Off):  offset &67 → &8D67 = bare CR (empty command)
;   Option 1 (Load): offset &58 → &8D58 = "L.!BOOT" (the bytes
;       &4C='L', &2E='.', &21='!' precede "BOOT" + CR at &8D5F)
;   Option 2 (Run):  offset &5A → &8D5A = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset &60 → &8D60 = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the string data
; overlaps with other byte sequences to save space. The &0D byte
; at &8D67 terminates "E.!BOOT" AND doubles as the bare-CR
; command for boot option 0.
; ***************************************************************************************
.boot_cmd_strings
    equs "BOOT"                                                       ; 8d5b: 42 4f 4f... BOO
    equb &0d                                                          ; 8d5f: 0d          .
    equs "E.!BOOT"                                                    ; 8d60: 45 2e 21... E.!
; ***************************************************************************************
; Boot option → OSCLI string offset table
; 
; Five bytes: the first byte (&0D) is the bare-CR target for boot
; option 0; bytes 1-4 are the offset table indexed by boot option
; (0-3). Each offset is the low byte of a pointer into page &8D.
; The code reads from boot_option_offsets+1 (&8D68) via
; LDX l8d68,Y with Y=boot_option, then LDY #&8D, JMP oscli.
; See boot_cmd_strings for the target strings.
; ***************************************************************************************
.boot_option_offsets
    equb &0d                                                          ; 8d67: 0d          .
; &8d68 referenced 1 time by &8e4b
.l8d68
    equb &67                                                          ; 8d68: 67          g              ; Opt 0 (Off): bare CR at &8D67
    equb &58                                                          ; 8d69: 58          X              ; Opt 1 (Load): L.!BOOT at &8D58
    equb &5a                                                          ; 8d6a: 5a          Z              ; Opt 2 (Run): !BOOT at &8D5A
    equb &60                                                          ; 8d6b: 60          `              ; Opt 3 (Exec): E.!BOOT at &8D60
    equs "Exec"                                                       ; 8d6c: 45 78 65... Exe

; &8d70 referenced 2 times by &8805, &880a
.print_hex_bytes
    ldx #4                                                            ; 8d70: a2 04       ..
; &8d72 referenced 2 times by &8811, &8d79
.num01
    lda (fs_options),y                                                ; 8d72: b1 bb       ..
    jsr print_hex                                                     ; 8d74: 20 9d 9f     ..
    dey                                                               ; 8d77: 88          .
    dex                                                               ; 8d78: ca          .
    bne num01                                                         ; 8d79: d0 f7       ..
; &8d7b referenced 1 time by &87fb
.print_space
    lda #&20 ; ' '                                                    ; 8d7b: a9 20       .
    bne c8dd9                                                         ; 8d7d: d0 5a       .Z             ; ALWAYS branch

    equs "Off"                                                        ; 8d7f: 4f 66 66    Off

; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
; &8d82 referenced 5 times by &809d, &80c1, &871d, &8917, &8ddf
.infol2
.copy_filename
    ldx #0                                                            ; 8d82: a2 00       ..
; ***************************************************************************************
; Copy string to FS command buffer
; 
; Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
; to &0F05+X, stopping when a CR (&0D) is encountered. The CR
; itself is also copied. Returns with X pointing past the last
; byte written.
; ***************************************************************************************
; &8d84 referenced 6 times by &87ca, &8910, &8932, &89f6, &8c80, &8d22
.copy_string_to_cmd
    ldy #0                                                            ; 8d84: a0 00       ..
; &8d86 referenced 1 time by &8d8f
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d86: b1 be       ..
    sta fs_cmd_data,x                                                 ; 8d88: 9d 05 0f    ...
    inx                                                               ; 8d8b: e8          .
    iny                                                               ; 8d8c: c8          .
    eor #&0d                                                          ; 8d8d: 49 0d       I.             ; XOR with CR: result=0 if byte was CR
    bne copy_string_from_offset                                       ; 8d8f: d0 f5       ..
; &8d91 referenced 1 time by &8d9b
.return_5
    rts                                                               ; 8d91: 60          `

    equs "Load"                                                       ; 8d92: 4c 6f 61... Loa

; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by fscv_5_cat to display Dir. and Lib. paths.
; ***************************************************************************************
.fsreply_0_print_dir
    ldx #0                                                            ; 8d96: a2 00       ..
; &8d98 referenced 2 times by &87ea, &8db8
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d98: bd 05 0f    ...
    bmi return_5                                                      ; 8d9b: 30 f4       0.
    bne c8db4                                                         ; 8d9d: d0 15       ..
; &8d9f referenced 1 time by &8d3d
.sub_c8d9f
    ldy l00b9                                                         ; 8d9f: a4 b9       ..
    bmi c8db2                                                         ; 8da1: 30 0f       0.
    iny                                                               ; 8da3: c8          .
    tya                                                               ; 8da4: 98          .
    and #3                                                            ; 8da5: 29 03       ).
    sta l00b9                                                         ; 8da7: 85 b9       ..
    beq c8db2                                                         ; 8da9: f0 07       ..
    jsr print_inline                                                  ; 8dab: 20 5c 86     \.
    equs "  "                                                         ; 8dae: 20 20

    bne c8db7                                                         ; 8db0: d0 05       ..
; &8db2 referenced 2 times by &8da1, &8da9
.c8db2
    lda #&0d                                                          ; 8db2: a9 0d       ..
; &8db4 referenced 1 time by &8d9d
.c8db4
    jsr osasci                                                        ; 8db4: 20 e3 ff     ..            ; Write character 13
; &8db7 referenced 1 time by &8db0
.c8db7
    inx                                                               ; 8db7: e8          .
    bne print_dir_from_offset                                         ; 8db8: d0 de       ..
    equs "Run"                                                        ; 8dba: 52 75 6e    Run

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
; &8dbd referenced 2 times by &8248, &8c94
.print_decimal
    tay                                                               ; 8dbd: a8          .
    lda #&64 ; 'd'                                                    ; 8dbe: a9 64       .d
    jsr print_decimal_digit                                           ; 8dc0: 20 ca 8d     ..
    lda #&0a                                                          ; 8dc3: a9 0a       ..
    jsr print_decimal_digit                                           ; 8dc5: 20 ca 8d     ..
    lda #1                                                            ; 8dc8: a9 01       ..
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
; &8dca referenced 2 times by &8dc0, &8dc5
.print_decimal_digit
    sta fs_error_ptr                                                  ; 8dca: 85 b8       ..
    tya                                                               ; 8dcc: 98          .
    ldx #&2f ; '/'                                                    ; 8dcd: a2 2f       ./
    sec                                                               ; 8dcf: 38          8
; &8dd0 referenced 1 time by &8dd3
.loop_c8dd0
    inx                                                               ; 8dd0: e8          .
    sbc fs_error_ptr                                                  ; 8dd1: e5 b8       ..
    bcs loop_c8dd0                                                    ; 8dd3: b0 fb       ..
    adc fs_error_ptr                                                  ; 8dd5: 65 b8       e.
    tay                                                               ; 8dd7: a8          .
    txa                                                               ; 8dd8: 8a          .
; &8dd9 referenced 1 time by &8d7d
.c8dd9
    jmp osasci                                                        ; 8dd9: 4c e3 ff    L..            ; Write character

; ***************************************************************************************
; FSCV 2/4: */ (run) and *RUN handler
; 
; Parses the filename via parse_filename_gs and calls infol2,
; then falls through to fsreply_4_notify_exec to set up and
; send the FS load-as-command request.
; ***************************************************************************************
.fscv_2_star_run
    jsr parse_filename_gs                                             ; 8ddc: 20 e8 86     ..
    jsr infol2                                                        ; 8ddf: 20 82 8d     ..
; ***************************************************************************************
; FS reply 4: send FS load-as-command and execute response
; 
; Initialises a GS reader to skip past the filename and
; calculate the command context address, then sets up an FS
; command with function code &05 (FCCMND: load as command)
; using send_fs_examine. If a Tube co-processor is present
; (tube_flag != 0), transfers the response data to the Tube
; via tube_addr_claim. Otherwise jumps via the indirect
; pointer at (&0F09) to execute at the load address.
; ***************************************************************************************
.fsreply_4_notify_exec
    ldy #0                                                            ; 8de2: a0 00       ..
    clc                                                               ; 8de4: 18          .
    jsr gsinit                                                        ; 8de5: 20 c2 ff     ..            ; GSINIT/GSREAD: skip past the filename
; &8de8 referenced 1 time by &8deb
.loop_c8de8
    jsr gsread                                                        ; 8de8: 20 c5 ff     ..
    bcc loop_c8de8                                                    ; 8deb: 90 fb       ..
    jsr c837e                                                         ; 8ded: 20 7e 83     ~.
    clc                                                               ; 8df0: 18          .              ; Calculate context addr = text ptr + Y
    tya                                                               ; 8df1: 98          .
    adc os_text_ptr                                                   ; 8df2: 65 f2       e.
    sta fs_cmd_context                                                ; 8df4: 8d 0a 0e    ...
    lda l00f3                                                         ; 8df7: a5 f3       ..
    adc #0                                                            ; 8df9: 69 00       i.
    sta l0e0b                                                         ; 8dfb: 8d 0b 0e    ...
    ldx #&0e                                                          ; 8dfe: a2 0e       ..
    stx fs_block_offset                                               ; 8e00: 86 bc       ..
    lda #&10                                                          ; 8e02: a9 10       ..
    sta fs_options                                                    ; 8e04: 85 bb       ..
    sta l0e16                                                         ; 8e06: 8d 16 0e    ...
    ldx #&4a ; 'J'                                                    ; 8e09: a2 4a       .J
    ldy #5                                                            ; 8e0b: a0 05       ..
    jsr send_fs_examine                                               ; 8e0d: 20 22 87     ".
    lda tube_flag                                                     ; 8e10: ad 67 0d    .g.            ; Check for Tube co-processor
    beq c8e29                                                         ; 8e13: f0 14       ..
    adc l0f0b                                                         ; 8e15: 6d 0b 0f    m..
    adc l0f0c                                                         ; 8e18: 6d 0c 0f    m..
    bcs c8e29                                                         ; 8e1b: b0 0c       ..
    jsr tube_claim_loop                                               ; 8e1d: 20 13 8c     ..
    ldx #9                                                            ; 8e20: a2 09       ..
    ldy #&0f                                                          ; 8e22: a0 0f       ..
    lda #4                                                            ; 8e24: a9 04       ..
    jmp tube_addr_claim                                               ; 8e26: 4c 06 04    L..

; &8e29 referenced 2 times by &8e13, &8e1b
.c8e29
    rol a                                                             ; 8e29: 2a          *
    jmp (l0f09)                                                       ; 8e2a: 6c 09 0f    l..

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to JMP restore_args_return if Y is non-zero.
; ***************************************************************************************
.fsreply_5_set_lib
    sty fs_lib_handle                                                 ; 8e2d: 8c 04 0e    ...
    bcc c8e35                                                         ; 8e30: 90 03       ..
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to JMP restore_args_return.
; ***************************************************************************************
.fsreply_3_set_csd
    sty fs_csd_handle                                                 ; 8e32: 8c 03 0e    ...
; &8e35 referenced 2 times by &8e30, &8e46
.c8e35
    jmp restore_args_return                                           ; 8e35: 4c b3 89    L..

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
    sec                                                               ; 8e38: 38          8
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to
; restore_args_return via c8e27. Called when the FS reply contains
; updated handle values but no boot action is needed.
; ***************************************************************************************
.fsreply_2_copy_handles
    ldx #3                                                            ; 8e39: a2 03       ..
    bcc c8e43                                                         ; 8e3b: 90 06       ..
; &8e3d referenced 1 time by &8e44
.logon2
    lda fs_cmd_data,x                                                 ; 8e3d: bd 05 0f    ...
    sta fs_urd_handle,x                                               ; 8e40: 9d 02 0e    ...
; &8e43 referenced 1 time by &8e3b
.c8e43
    dex                                                               ; 8e43: ca          .
    bpl logon2                                                        ; 8e44: 10 f7       ..
    bcc c8e35                                                         ; 8e46: 90 ed       ..
; ***************************************************************************************
; Execute boot command via OSCLI
; 
; Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
; path). Reads the boot option from fs_boot_option (&0E05),
; looks up the OSCLI command string offset from boot_option_offsets+1,
; and executes the boot command via JMP oscli with page &8D.
; ***************************************************************************************
.boot_cmd_execute
    ldy fs_boot_option                                                ; 8e48: ac 05 0e    ...
    ldx l8d68,y                                                       ; 8e4b: be 68 8d    .h.
    ldy #&8d                                                          ; 8e4e: a0 8d       ..
    jmp oscli                                                         ; 8e50: 4c f7 ff    L..

; &8e53 referenced 2 times by &8e6d, &8e7d
.sub_c8e53
    lda l00f0                                                         ; 8e53: a5 f0       ..
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
; &8e55 referenced 3 times by &8309, &8f8d, &8fa6
.calc_handle_offset
    asl a                                                             ; 8e55: 0a          .              ; A = handle * 2
    asl a                                                             ; 8e56: 0a          .              ; A = handle * 4
    pha                                                               ; 8e57: 48          H              ; Push handle*4 onto stack
    asl a                                                             ; 8e58: 0a          .              ; A = handle * 8
    tsx                                                               ; 8e59: ba          .
    adc l0101,x                                                       ; 8e5a: 7d 01 01    }..            ; A = handle*8 + handle*4 = handle*12
    tay                                                               ; 8e5d: a8          .              ; Y = offset into handle workspace
    pla                                                               ; 8e5e: 68          h              ; Clean up stack (discard handle*4)
    cmp #&48 ; 'H'                                                    ; 8e5f: c9 48       .H             ; Offset >= &48? (6 handles max)
    bcc return_6                                                      ; 8e61: 90 03       ..             ; Valid: return with C clear
    ldy #0                                                            ; 8e63: a0 00       ..
    tya                                                               ; 8e65: 98          .              ; A=0, C set = error indicator; A=&00
; &8e66 referenced 1 time by &8e61
.return_6
.return_calc_handle
    rts                                                               ; 8e66: 60          `

; *NET1: read file handle from received packet.
; Reads a byte from offset &6F of the RX buffer (net_rx_ptr)
; and falls through to net_2_read_handle_entry's common path.
.net_1_read_handle
    ldy #&6f ; 'o'                                                    ; 8e67: a0 6f       .o
    lda (net_rx_ptr),y                                                ; 8e69: b1 9c       ..
    bcc c8e7a                                                         ; 8e6b: 90 0d       ..
; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears rom_svc_num on exit.
; ***************************************************************************************
.net_2_read_handle_entry
    jsr sub_c8e53                                                     ; 8e6d: 20 53 8e     S.
    bcs rxpol2                                                        ; 8e70: b0 06       ..
    lda (nfs_workspace),y                                             ; 8e72: b1 9e       ..
    cmp #&3f ; '?'                                                    ; 8e74: c9 3f       .?
    bne c8e7a                                                         ; 8e76: d0 02       ..
; &8e78 referenced 2 times by &8e70, &8e80
.rxpol2
    lda #0                                                            ; 8e78: a9 00       ..
; &8e7a referenced 2 times by &8e6b, &8e76
.c8e7a
    sta l00f0                                                         ; 8e7a: 85 f0       ..
    rts                                                               ; 8e7c: 60          `

; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Returns via RTS (earlier versions preserved the
; carry flag across the write using ROL/ROR on rx_flags, but
; 3.60 simplified this).
; ***************************************************************************************
.net_3_close_handle
    jsr sub_c8e53                                                     ; 8e7d: 20 53 8e     S.
    bcs rxpol2                                                        ; 8e80: b0 f6       ..
    lda #&3f ; '?'                                                    ; 8e82: a9 3f       .?
    sta (nfs_workspace),y                                             ; 8e84: 91 9e       ..
    rts                                                               ; 8e86: 60          `

; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the range
; check and dispatch at osword_12_handler (&8E8D).
; ***************************************************************************************
.svc_8_osword
    lda l00ef                                                         ; 8e87: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8e89: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_7                                                      ; 8e8b: 30 2a       0*
; ***************************************************************************************
; OSWORD range check, dispatch, and register restore
; 
; Reached by fall-through from svc_8_osword with A = OSWORD
; number minus &0F. Rejects indices >= 5 (only OSWORDs &0F-&13
; are handled). Dispatches to the appropriate handler via
; fs_osword_dispatch, then on return copies 3 bytes from
; (net_rx_ptr)+0..2 back to &AA-&AC (restoring the param block
; pointer that was saved by fs_osword_dispatch before dispatch).
; 
; The actual OSWORD &12 sub-function dispatch (read/set station,
; protection, handles etc.) lives in sub_c8f01.
; ***************************************************************************************
.osword_12_handler
    cmp #5                                                            ; 8e8d: c9 05       ..
    bcs return_7                                                      ; 8e8f: b0 26       .&
    jsr fs_osword_dispatch                                            ; 8e91: 20 9f 8e     ..
    ldy #2                                                            ; 8e94: a0 02       ..
; &8e96 referenced 1 time by &8e9c
.loop_c8e96
    lda (net_rx_ptr),y                                                ; 8e96: b1 9c       ..
    sta l00aa,y                                                       ; 8e98: 99 aa 00    ...
    dey                                                               ; 8e9b: 88          .
    bpl loop_c8e96                                                    ; 8e9c: 10 f8       ..
    rts                                                               ; 8e9e: 60          `

; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; Saves the param block pointer (&AA-&AC) to (net_rx_ptr) and
; reads the sub-function code from (&F0)+1, then dispatches via
; the 5-entry table at &8EB8 (low) / &8EBD (high) using
; PHA/PHA/RTS. The RTS at the end of the dispatched handler
; returns here, after which the caller restores &AA-&AC.
; ***************************************************************************************
; &8e9f referenced 1 time by &8e91
.fs_osword_dispatch
    tax                                                               ; 8e9f: aa          .
    lda fs_osword_tbl_hi,x                                            ; 8ea0: bd bd 8e    ...
    pha                                                               ; 8ea3: 48          H
    lda l8eb8,x                                                       ; 8ea4: bd b8 8e    ...
.fs_osword_tbl_lo
    pha                                                               ; 8ea7: 48          H              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    ldy #2                                                            ; 8ea8: a0 02       ..
; &8eaa referenced 1 time by &8eb0
.save1
    lda l00aa,y                                                       ; 8eaa: b9 aa 00    ...
    sta (net_rx_ptr),y                                                ; 8ead: 91 9c       ..
    dey                                                               ; 8eaf: 88          .
    bpl save1                                                         ; 8eb0: 10 f8       ..
    iny                                                               ; 8eb2: c8          .
    lda (l00f0),y                                                     ; 8eb3: b1 f0       ..
    sty l00a9                                                         ; 8eb5: 84 a9       ..
; &8eb7 referenced 2 times by &8e8b, &8e8f
.return_7
    rts                                                               ; 8eb7: 60          `

; &8eb8 referenced 1 time by &8ea4
.l8eb8
    equb <(osword_0f_handler-1)                                       ; 8eb8: c1          .
    equb <(osword_10_handler-1)                                       ; 8eb9: 7b          {
    equb <(osword_11_handler-1)                                       ; 8eba: db          .
    equb <(sub_c8f01-1)                                               ; 8ebb: 00          .
    equb <(econet_tx_rx-1)                                            ; 8ebc: ef          .
; &8ebd referenced 1 time by &8ea0
.fs_osword_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8ebd: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb >(osword_10_handler-1)                                       ; 8ebe: 8f          .
    equb >(osword_11_handler-1)                                       ; 8ebf: 8e          .
    equb >(sub_c8f01-1)                                               ; 8ec0: 8f          .
    equb >(econet_tx_rx-1)                                            ; 8ec1: 8f          .

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
    asl tx_clear_flag                                                 ; 8ec2: 0e 62 0d    .b.            ; ASL TXCLR: C=1 means TX free to claim
    tya                                                               ; 8ec5: 98          .
    bcc readry                                                        ; 8ec6: 90 34       .4             ; C=0: TX busy, return error status
    lda net_rx_ptr_hi                                                 ; 8ec8: a5 9d       ..
    sta l00ac                                                         ; 8eca: 85 ac       ..
    sta nmi_tx_block_hi                                               ; 8ecc: 85 a1       ..
    lda #&6f ; 'o'                                                    ; 8ece: a9 6f       .o
    sta l00ab                                                         ; 8ed0: 85 ab       ..
    sta nmi_tx_block                                                  ; 8ed2: 85 a0       ..
    ldx #&0f                                                          ; 8ed4: a2 0f       ..
    jsr c8f1c                                                         ; 8ed6: 20 1c 8f     ..
    jmp c9630                                                         ; 8ed9: 4c 30 96    L0.

; ***************************************************************************************
; OSWORD &11 handler: read JSR arguments (READRA)
; 
; Copies the JSR (remote procedure call) argument buffer from the
; static workspace page back to the caller's OSWORD parameter block.
; Reads the buffer size from workspace offset JSRSIZ, then copies
; that many bytes. After the copy, clears the old LSTAT byte via
; CLRJSR to reset the protection status. Also provides READRB as
; a sub-entry (&8EE7) to return just the buffer size and args size
; without copying the data.
; ***************************************************************************************
.osword_11_handler
    lda net_rx_ptr_hi                                                 ; 8edc: a5 9d       ..
    sta l00ac                                                         ; 8ede: 85 ac       ..
    ldy #&7f                                                          ; 8ee0: a0 7f       ..             ; JSRSIZ at workspace offset &7F
    lda (net_rx_ptr),y                                                ; 8ee2: b1 9c       ..
    iny                                                               ; 8ee4: c8          .              ; Y=&80: start of JSR argument data; Y=&80
    sty l00ab                                                         ; 8ee5: 84 ab       ..
    tax                                                               ; 8ee7: aa          .
    dex                                                               ; 8ee8: ca          .
    ldy #0                                                            ; 8ee9: a0 00       ..
    jsr c8f1c                                                         ; 8eeb: 20 1c 8f     ..
    jmp clear_jsr_protection                                          ; 8eee: 4c f0 92    L..

; &8ef1 referenced 1 time by &8f4c
.read_args_size
    ldy #&7f                                                          ; 8ef1: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8ef3: b1 9c       ..
    ldy #1                                                            ; 8ef5: a0 01       ..
    sta (l00f0),y                                                     ; 8ef7: 91 f0       ..
    iny                                                               ; 8ef9: c8          .              ; Y=&02
    lda #&80                                                          ; 8efa: a9 80       ..
; &8efc referenced 1 time by &8ec6
.readry
    sta (l00f0),y                                                     ; 8efc: 91 f0       ..
    rts                                                               ; 8efe: 60          `

; &8eff referenced 1 time by &8f13
.l8eff
    equb &ff, 1                                                       ; 8eff: ff 01       ..

.sub_c8f01
    cmp #6                                                            ; 8f01: c9 06       ..
    bcs rsl1                                                          ; 8f03: b0 41       .A
    cmp #4                                                            ; 8f05: c9 04       ..
    bcs rssl1                                                         ; 8f07: b0 22       ."
    lsr a                                                             ; 8f09: 4a          J
    ldx #&0d                                                          ; 8f0a: a2 0d       ..
    tay                                                               ; 8f0c: a8          .
    beq c8f11                                                         ; 8f0d: f0 02       ..
    ldx nfs_workspace_hi                                              ; 8f0f: a6 9f       ..
; &8f11 referenced 1 time by &8f0d
.c8f11
    stx l00ac                                                         ; 8f11: 86 ac       ..
    lda l8eff,y                                                       ; 8f13: b9 ff 8e    ...
    sta l00ab                                                         ; 8f16: 85 ab       ..
    ldx #1                                                            ; 8f18: a2 01       ..
    ldy #1                                                            ; 8f1a: a0 01       ..
; &8f1c referenced 4 times by &8ed6, &8eeb, &8f28, &8fbd
.c8f1c
    bcc c8f22                                                         ; 8f1c: 90 04       ..             ; C=0: skip param-to-workspace copy
    lda (l00f0),y                                                     ; 8f1e: b1 f0       ..
    sta (l00ab),y                                                     ; 8f20: 91 ab       ..
; &8f22 referenced 1 time by &8f1c
.c8f22
    lda (l00ab),y                                                     ; 8f22: b1 ab       ..
; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (&AB),Y (param to workspace)
; C=0: copy X+1 bytes from (&AB),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
.copy_param_block
    sta (l00f0),y                                                     ; 8f24: 91 f0       ..             ; Store to param block (no-op if C=1)
    iny                                                               ; 8f26: c8          .
    dex                                                               ; 8f27: ca          .
    bpl c8f1c                                                         ; 8f28: 10 f2       ..
.logon3
.return_copy_param
    rts                                                               ; 8f2a: 60          `

; &8f2b referenced 1 time by &8f07
.rssl1
    lsr a                                                             ; 8f2b: 4a          J
    iny                                                               ; 8f2c: c8          .
    lda (l00f0),y                                                     ; 8f2d: b1 f0       ..
    bcs rssl2                                                         ; 8f2f: b0 05       ..
    lda prot_status                                                   ; 8f31: ad 63 0d    .c.
    sta (l00f0),y                                                     ; 8f34: 91 f0       ..
; &8f36 referenced 1 time by &8f2f
.rssl2
    sta prot_status                                                   ; 8f36: 8d 63 0d    .c.
    sta saved_jsr_mask                                                ; 8f39: 8d 65 0d    .e.
    rts                                                               ; 8f3c: 60          `

; &8f3d referenced 1 time by &8f48
.loop_c8f3d
    ldy #&14                                                          ; 8f3d: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8f3f: b1 9c       ..
    ldy #1                                                            ; 8f41: a0 01       ..
    sta (l00f0),y                                                     ; 8f43: 91 f0       ..
    rts                                                               ; 8f45: 60          `

; &8f46 referenced 1 time by &8f03
.rsl1
    cmp #8                                                            ; 8f46: c9 08       ..
    beq loop_c8f3d                                                    ; 8f48: f0 f3       ..
    cmp #9                                                            ; 8f4a: c9 09       ..
    beq read_args_size                                                ; 8f4c: f0 a3       ..
    bpl c8f69                                                         ; 8f4e: 10 19       ..
    ldy #3                                                            ; 8f50: a0 03       ..
    lsr a                                                             ; 8f52: 4a          J
    bcc readc1                                                        ; 8f53: 90 1b       ..
    sty l00a8                                                         ; 8f55: 84 a8       ..
; &8f57 referenced 1 time by &8f66
.loop_c8f57
    ldy l00a8                                                         ; 8f57: a4 a8       ..
    lda (l00f0),y                                                     ; 8f59: b1 f0       ..
    jsr handle_to_mask_a                                              ; 8f5b: 20 9a 86     ..
    tya                                                               ; 8f5e: 98          .
    ldy l00a8                                                         ; 8f5f: a4 a8       ..
    sta fs_server_net,y                                               ; 8f61: 99 01 0e    ...
    dec l00a8                                                         ; 8f64: c6 a8       ..
    bne loop_c8f57                                                    ; 8f66: d0 ef       ..
    rts                                                               ; 8f68: 60          `

; &8f69 referenced 1 time by &8f4e
.c8f69
    iny                                                               ; 8f69: c8          .
    lda fs_last_error                                                 ; 8f6a: ad 09 0e    ...
    sta (l00f0),y                                                     ; 8f6d: 91 f0       ..
    rts                                                               ; 8f6f: 60          `

; &8f70 referenced 2 times by &8f53, &8f79
.readc1
    lda fs_server_net,y                                               ; 8f70: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8f73: 20 b7 86     ..            ; Convert bitmask to handle number (FS2A)
    sta (l00f0),y                                                     ; 8f76: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8f78: 88          .
    bne readc1                                                        ; 8f79: d0 f5       ..
    rts                                                               ; 8f7b: 60          `

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
    ldx nfs_workspace_hi                                              ; 8f7c: a6 9f       ..
    stx l00ac                                                         ; 8f7e: 86 ac       ..
    sty l00ab                                                         ; 8f80: 84 ab       ..
    ror rx_flags                                                      ; 8f82: 6e 64 0d    nd.            ; Disable user RX during CB operation
    lda (l00f0),y                                                     ; 8f85: b1 f0       ..
    sta l00aa                                                         ; 8f87: 85 aa       ..
    bne c8fa6                                                         ; 8f89: d0 1b       ..
    lda #3                                                            ; 8f8b: a9 03       ..             ; Start scan from RXCB #3 (0-2 reserved)
; &8f8d referenced 1 time by &8f9f
.scan0
    jsr calc_handle_offset                                            ; 8f8d: 20 55 8e     U.
    bcs openl4                                                        ; 8f90: b0 3d       .=
    lsr a                                                             ; 8f92: 4a          J
    lsr a                                                             ; 8f93: 4a          J
    tax                                                               ; 8f94: aa          .
    lda (l00ab),y                                                     ; 8f95: b1 ab       ..
    beq openl4                                                        ; 8f97: f0 36       .6
    cmp #&3f ; '?'                                                    ; 8f99: c9 3f       .?             ; &3F = deleted slot, free for reuse
    beq scan1                                                         ; 8f9b: f0 04       ..
    inx                                                               ; 8f9d: e8          .
    txa                                                               ; 8f9e: 8a          .
    bne scan0                                                         ; 8f9f: d0 ec       ..
; &8fa1 referenced 1 time by &8f9b
.scan1
    txa                                                               ; 8fa1: 8a          .
    ldx #0                                                            ; 8fa2: a2 00       ..
    sta (l00f0,x)                                                     ; 8fa4: 81 f0       ..
; &8fa6 referenced 1 time by &8f89
.c8fa6
    jsr calc_handle_offset                                            ; 8fa6: 20 55 8e     U.
    bcs openl4                                                        ; 8fa9: b0 24       .$
    dey                                                               ; 8fab: 88          .
    sty l00ab                                                         ; 8fac: 84 ab       ..
    lda #&c0                                                          ; 8fae: a9 c0       ..
    ldy #1                                                            ; 8fb0: a0 01       ..
    ldx #&0b                                                          ; 8fb2: a2 0b       ..
    cpy l00aa                                                         ; 8fb4: c4 aa       ..
    adc (l00ab),y                                                     ; 8fb6: 71 ab       q.
    beq openl6                                                        ; 8fb8: f0 03       ..
    bmi openl7                                                        ; 8fba: 30 0e       0.
; &8fbc referenced 1 time by &8fcc
.loop_c8fbc
    clc                                                               ; 8fbc: 18          .
; &8fbd referenced 1 time by &8fb8
.openl6
    jsr c8f1c                                                         ; 8fbd: 20 1c 8f     ..
    bcs c8fd1                                                         ; 8fc0: b0 0f       ..
    lda #&3f ; '?'                                                    ; 8fc2: a9 3f       .?             ; Mark CB as consumed (consume-once)
    ldy #1                                                            ; 8fc4: a0 01       ..
    sta (l00ab),y                                                     ; 8fc6: 91 ab       ..
    bne c8fd1                                                         ; 8fc8: d0 07       ..             ; ALWAYS branch

; &8fca referenced 1 time by &8fba
.openl7
    adc #1                                                            ; 8fca: 69 01       i.
    bne loop_c8fbc                                                    ; 8fcc: d0 ee       ..
    dey                                                               ; 8fce: 88          .
; &8fcf referenced 3 times by &8f90, &8f97, &8fa9
.openl4
    sta (l00f0),y                                                     ; 8fcf: 91 f0       ..
; &8fd1 referenced 2 times by &8fc0, &8fc8
.c8fd1
    rol rx_flags                                                      ; 8fd1: 2e 64 0d    .d.            ; Re-enable user RX
    rts                                                               ; 8fd4: 60          `

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &1C. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &20.
; ***************************************************************************************
; &8fd5 referenced 1 time by &9008
.setup_rx_buffer_ptrs
    ldy #&1c                                                          ; 8fd5: a0 1c       ..
    lda l00f0                                                         ; 8fd7: a5 f0       ..
    adc #1                                                            ; 8fd9: 69 01       i.
    jsr store_16bit_at_y                                              ; 8fdb: 20 e6 8f     ..
    ldy #1                                                            ; 8fde: a0 01       ..
    lda (l00f0),y                                                     ; 8fe0: b1 f0       ..
    ldy #&20 ; ' '                                                    ; 8fe2: a0 20       .
    adc l00f0                                                         ; 8fe4: 65 f0       e.
; &8fe6 referenced 1 time by &8fdb
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8fe6: 91 9e       ..
    iny                                                               ; 8fe8: c8          .
    lda l00f1                                                         ; 8fe9: a5 f1       ..
    adc #0                                                            ; 8feb: 69 00       i.
    sta (nfs_workspace),y                                             ; 8fed: 91 9e       ..
    rts                                                               ; 8fef: 60          `

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &8395
;      (init_tx_ctrl_block+Y, zero entries substituted from NMI
;      workspace &0DE6), transmit it, set up RX control block,
;      and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &903E).
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8ff0: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs c903e                                                         ; 8ff2: b0 4a       .J
    ldy #&23 ; '#'                                                    ; 8ff4: a0 23       .#
; &8ff6 referenced 1 time by &9003
.dofs01
    lda init_tx_ctrl_block,y                                          ; 8ff6: b9 95 83    ...
    bne c8ffe                                                         ; 8ff9: d0 03       ..             ; Non-zero = use ROM template byte as-is
    lda l0de6,y                                                       ; 8ffb: b9 e6 0d    ...            ; Zero = substitute from NMI workspace
; &8ffe referenced 1 time by &8ff9
.c8ffe
    sta (nfs_workspace),y                                             ; 8ffe: 91 9e       ..
    dey                                                               ; 9000: 88          .
    cpy #&17                                                          ; 9001: c0 17       ..
    bne dofs01                                                        ; 9003: d0 f1       ..
    iny                                                               ; 9005: c8          .
    sty net_tx_ptr                                                    ; 9006: 84 9a       ..
    jsr setup_rx_buffer_ptrs                                          ; 9008: 20 d5 8f     ..
    ldy #2                                                            ; 900b: a0 02       ..
    lda #&90                                                          ; 900d: a9 90       ..
    sta escapable                                                     ; 900f: 85 97       ..
    sta (l00f0),y                                                     ; 9011: 91 f0       ..
    iny                                                               ; 9013: c8          .              ; Y=&03
    iny                                                               ; 9014: c8          .              ; Y=&04
; &9015 referenced 1 time by &901d
.loop_c9015
    lda l0dfe,y                                                       ; 9015: b9 fe 0d    ...
    sta (l00f0),y                                                     ; 9018: 91 f0       ..
    iny                                                               ; 901a: c8          .
    cpy #7                                                            ; 901b: c0 07       ..
    bne loop_c9015                                                    ; 901d: d0 f6       ..
    lda nfs_workspace_hi                                              ; 901f: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; 9021: 85 9b       ..
    cli                                                               ; 9023: 58          X              ; Enable interrupts before transmit
    jsr tx_poll_ff                                                    ; 9024: 20 ff 85     ..
    ldy #&20 ; ' '                                                    ; 9027: a0 20       .
    lda #&ff                                                          ; 9029: a9 ff       ..             ; Set RX end address to &FFFF (accept any length)
    sta (nfs_workspace),y                                             ; 902b: 91 9e       ..
    iny                                                               ; 902d: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; 902e: 91 9e       ..
    ldy #&19                                                          ; 9030: a0 19       ..
    lda #&90                                                          ; 9032: a9 90       ..
    sta (nfs_workspace),y                                             ; 9034: 91 9e       ..
    dey                                                               ; 9036: 88          .              ; Y=&18
    lda #&7f                                                          ; 9037: a9 7f       ..
    sta (nfs_workspace),y                                             ; 9039: 91 9e       ..
    jmp c8530                                                         ; 903b: 4c 30 85    L0.

; &903e referenced 1 time by &8ff2
.c903e
    php                                                               ; 903e: 08          .
    ldy #1                                                            ; 903f: a0 01       ..
    lda (l00f0),y                                                     ; 9041: b1 f0       ..
; ***************************************************************************************
; FS response data relay (DOFS)
; 
; Entered from the econet_tx_rx response handler at &903E after
; loading the first data byte from the RX buffer. Saves the
; command byte and station address from the received packet into
; (net_rx_ptr)+&71/&72, then iterates through remaining data
; bytes. Each byte is stored at (net_rx_ptr)+&7D, the control
; block is set up via ctrl_block_setup_alt, and the packet is
; transmitted. Loops until a &0D terminator or &00 null is found.
; The branch at &9053 (BNE dofs2) handles the first-packet case
; where the data length field at (net_rx_ptr)+&7B is adjusted.
; ***************************************************************************************
.net_write_char
    tax                                                               ; 9043: aa          .
    iny                                                               ; 9044: c8          .
    lda (l00f0),y                                                     ; 9045: b1 f0       ..
    iny                                                               ; 9047: c8          .
    sty l00ab                                                         ; 9048: 84 ab       ..
    ldy #&72 ; 'r'                                                    ; 904a: a0 72       .r             ; Store station addr hi at (net_rx_ptr)+&72
    sta (net_rx_ptr),y                                                ; 904c: 91 9c       ..
    dey                                                               ; 904e: 88          .              ; Y=&71
    txa                                                               ; 904f: 8a          .
    sta (net_rx_ptr),y                                                ; 9050: 91 9c       ..             ; Store station addr lo at (net_rx_ptr)+&71
    plp                                                               ; 9052: 28          (
    bne dofs2                                                         ; 9053: d0 1c       ..
; &9055 referenced 1 time by &906e
.loop_c9055
    ldy l00ab                                                         ; 9055: a4 ab       ..
    inc l00ab                                                         ; 9057: e6 ab       ..
    lda (l00f0),y                                                     ; 9059: b1 f0       ..
    beq return_8                                                      ; 905b: f0 13       ..
    ldy #&7d ; '}'                                                    ; 905d: a0 7d       .}
    sta (net_rx_ptr),y                                                ; 905f: 91 9c       ..             ; Store data byte at (net_rx_ptr)+&7D for TX
    pha                                                               ; 9061: 48          H
    jsr ctrl_block_setup_alt                                          ; 9062: 20 7f 91     ..
    jsr sub_c907c                                                     ; 9065: 20 7c 90     |.
; &9068 referenced 1 time by &9069
.loop_c9068
    dex                                                               ; 9068: ca          .
    bne loop_c9068                                                    ; 9069: d0 fd       ..
    pla                                                               ; 906b: 68          h
    eor #&0d                                                          ; 906c: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne loop_c9055                                                    ; 906e: d0 e5       ..
; &9070 referenced 1 time by &905b
.return_8
    rts                                                               ; 9070: 60          `

; &9071 referenced 1 time by &9053
.dofs2
    jsr ctrl_block_setup_alt                                          ; 9071: 20 7f 91     ..
    ldy #&7b ; '{'                                                    ; 9074: a0 7b       .{
    lda (net_rx_ptr),y                                                ; 9076: b1 9c       ..
    adc #3                                                            ; 9078: 69 03       i.             ; Adjust data length by 3 for header bytes
    sta (net_rx_ptr),y                                                ; 907a: 91 9c       ..
; &907c referenced 1 time by &9065
.sub_c907c
    cli                                                               ; 907c: 58          X
    jmp tx_poll_ff                                                    ; 907d: 4c ff 85    L..

; ***************************************************************************************
; NETVEC dispatch handler (ENTRY)
; 
; Indirected from NETVEC at &0224. Saves all registers and flags,
; retrieves the reason code from the stacked A, and dispatches to
; one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
; &9099. Reason codes >= 9 are ignored.
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
    php                                                               ; 9080: 08          .
    pha                                                               ; 9081: 48          H
    txa                                                               ; 9082: 8a          .
    pha                                                               ; 9083: 48          H
    tya                                                               ; 9084: 98          .
    pha                                                               ; 9085: 48          H
    tsx                                                               ; 9086: ba          .
    lda l0103,x                                                       ; 9087: bd 03 01    ...            ; Retrieve original A (reason code) from stack
    cmp #9                                                            ; 908a: c9 09       ..
    bcs entry1                                                        ; 908c: b0 04       ..
    tax                                                               ; 908e: aa          .
    jsr osword_trampoline                                             ; 908f: 20 99 90     ..
; &9092 referenced 1 time by &908c
.entry1
    pla                                                               ; 9092: 68          h
    tay                                                               ; 9093: a8          .
    pla                                                               ; 9094: 68          h
    tax                                                               ; 9095: aa          .
    pla                                                               ; 9096: 68          h
    plp                                                               ; 9097: 28          (
    rts                                                               ; 9098: 60          `

; &9099 referenced 1 time by &908f
.osword_trampoline
    lda osword_tbl_hi,x                                               ; 9099: bd ad 90    ...            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 909c: 48          H
    lda osword_tbl_lo,x                                               ; 909d: bd a4 90    ...
    pha                                                               ; 90a0: 48          H
    lda l00ef                                                         ; 90a1: a5 ef       ..
    rts                                                               ; 90a3: 60          `

; &90a4 referenced 1 time by &909d
.osword_tbl_lo
    equb <(return_1-1)                                                ; 90a4: f5          .
    equb <(remote_print_handler-1)                                    ; 90a5: e9          .
    equb <(remote_print_handler-1)                                    ; 90a6: e9          .
    equb <(remote_print_handler-1)                                    ; 90a7: e9          .
    equb <(sub_c90b6-1)                                               ; 90a8: b5          .
    equb <(printer_select_handler-1)                                  ; 90a9: da          .
    equb <(return_1-1)                                                ; 90aa: f5          .
    equb <(remote_cmd_dispatch-1)                                     ; 90ab: e7          .
    equb <(sub_c9154-1)                                               ; 90ac: 53          S
; &90ad referenced 1 time by &9099
.osword_tbl_hi
    equb >(return_1-1)                                                ; 90ad: 80          .
    equb >(remote_print_handler-1)                                    ; 90ae: 91          .
    equb >(remote_print_handler-1)                                    ; 90af: 91          .
    equb >(remote_print_handler-1)                                    ; 90b0: 91          .
    equb >(sub_c90b6-1)                                               ; 90b1: 90          .
    equb >(printer_select_handler-1)                                  ; 90b2: 91          .
    equb >(return_1-1)                                                ; 90b3: 80          .
    equb >(remote_cmd_dispatch-1)                                     ; 90b4: 90          .
    equb >(sub_c9154-1)                                               ; 90b5: 91          .

.sub_c90b6
    tsx                                                               ; 90b6: ba          .
    ror l0106,x                                                       ; 90b7: 7e 06 01    ~..            ; ROR/ASL on stacked P: zeros carry to signal success
    asl l0106,x                                                       ; 90ba: 1e 06 01    ...
    tya                                                               ; 90bd: 98          .
    ldy #&da                                                          ; 90be: a0 da       ..             ; Store character at workspace offset &DA
    sta (nfs_workspace),y                                             ; 90c0: 91 9e       ..
    lda #0                                                            ; 90c2: a9 00       ..
; ***************************************************************************************
; Set up TX control block and send
; 
; Stores A at workspace offset &D9 (command type), then sets byte
; &0C to &80 (TX active flag). Saves the current net_tx_ptr,
; temporarily redirects it to (nfs_workspace)+&0C so tx_poll_ff
; transmits from the workspace TX control block. After transmission
; completes, writes &3F (TX deleted) at (net_tx_ptr)+&00 to mark
; the control block as free, then restores net_tx_ptr to its
; original value.
; ***************************************************************************************
; &90c4 referenced 3 times by &81cf, &9117, &917a
.setup_tx_and_send
    ldy #&d9                                                          ; 90c4: a0 d9       ..
    sta (nfs_workspace),y                                             ; 90c6: 91 9e       ..
    lda #&80                                                          ; 90c8: a9 80       ..             ; Mark TX control block as active (&80)
    ldy #&0c                                                          ; 90ca: a0 0c       ..
    sta (nfs_workspace),y                                             ; 90cc: 91 9e       ..
    lda net_tx_ptr                                                    ; 90ce: a5 9a       ..             ; Save net_tx_ptr; redirect to workspace TXCB
    pha                                                               ; 90d0: 48          H
    lda net_tx_ptr_hi                                                 ; 90d1: a5 9b       ..
    pha                                                               ; 90d3: 48          H
    sty net_tx_ptr                                                    ; 90d4: 84 9a       ..
    ldx nfs_workspace_hi                                              ; 90d6: a6 9f       ..
    stx net_tx_ptr_hi                                                 ; 90d8: 86 9b       ..
    jsr tx_poll_ff                                                    ; 90da: 20 ff 85     ..
    lda #&3f ; '?'                                                    ; 90dd: a9 3f       .?             ; Mark TXCB as deleted (&3F) after transmit
    sta (net_tx_ptr,x)                                                ; 90df: 81 9a       ..
    pla                                                               ; 90e1: 68          h
    sta net_tx_ptr_hi                                                 ; 90e2: 85 9b       ..
    pla                                                               ; 90e4: 68          h
    sta net_tx_ptr                                                    ; 90e5: 85 9a       ..
    rts                                                               ; 90e7: 60          `

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
    ldy l00f1                                                         ; 90e8: a4 f1       ..             ; Load original Y (OSBYTE secondary param)
    cmp #&81                                                          ; 90ea: c9 81       ..             ; OSBYTE &81 (INKEY): always forward to terminal
    beq c9101                                                         ; 90ec: f0 13       ..
    ldy #1                                                            ; 90ee: a0 01       ..             ; Y=1: search NCTBPL table (execute on both)
    ldx #9                                                            ; 90f0: a2 09       ..
    jsr match_osbyte_code                                             ; 90f2: 20 3c 91     <.
    beq c9101                                                         ; 90f5: f0 0a       ..
    dey                                                               ; 90f7: 88          .              ; Y=-1: search NCTBMI table (terminal only)
    dey                                                               ; 90f8: 88          .
    ldx #&0e                                                          ; 90f9: a2 0e       ..
    jsr match_osbyte_code                                             ; 90fb: 20 3c 91     <.
    beq c9101                                                         ; 90fe: f0 01       ..
    iny                                                               ; 9100: c8          .              ; Y=0: OSBYTE not recognised, ignore
; &9101 referenced 3 times by &90ec, &90f5, &90fe
.c9101
    ldx #2                                                            ; 9101: a2 02       ..             ; X=2 bytes to copy (default for RBYTE)
    tya                                                               ; 9103: 98          .
    beq return_nbyte                                                  ; 9104: f0 35       .5
    php                                                               ; 9106: 08          .              ; Y>0 (NCTBPL): send only, no result expected
    bpl nbyte6                                                        ; 9107: 10 01       ..
    inx                                                               ; 9109: e8          .              ; Y<0 (NCTBMI): X=3 bytes (result + P flags); X=&03
; &910a referenced 1 time by &9107
.nbyte6
    ldy #&dc                                                          ; 910a: a0 dc       ..
; &910c referenced 1 time by &9114
.nbyte1
    lda l0015,y                                                       ; 910c: b9 15 00    ...            ; Copy OSBYTE args from stack frame to workspace
    sta (nfs_workspace),y                                             ; 910f: 91 9e       ..
    dey                                                               ; 9111: 88          .
    cpy #&da                                                          ; 9112: c0 da       ..
    bpl nbyte1                                                        ; 9114: 10 f6       ..
    txa                                                               ; 9116: 8a          .
    jsr setup_tx_and_send                                             ; 9117: 20 c4 90     ..
    plp                                                               ; 911a: 28          (
    bpl return_nbyte                                                  ; 911b: 10 1e       ..
    lda #&7f                                                          ; 911d: a9 7f       ..             ; Set up RX control block to wait for reply
    ldy #&0c                                                          ; 911f: a0 0c       ..
    sta (nfs_workspace),y                                             ; 9121: 91 9e       ..
; &9123 referenced 1 time by &9125
.loop_c9123
    lda (nfs_workspace),y                                             ; 9123: b1 9e       ..             ; Poll for TX completion (wait for bit 7 set)
    bpl loop_c9123                                                    ; 9125: 10 fc       ..
    tsx                                                               ; 9127: ba          .
    ldy #&dd                                                          ; 9128: a0 dd       ..
    lda (nfs_workspace),y                                             ; 912a: b1 9e       ..
    ora #&44 ; 'D'                                                    ; 912c: 09 44       .D             ; Force V=1 (claimed) and I=1 (no IRQ) in saved P
    bne nbyte5                                                        ; 912e: d0 04       ..             ; ALWAYS branch (ORA #&44 never zero); ALWAYS branch

; &9130 referenced 1 time by &9139
.nbyte4
    dey                                                               ; 9130: 88          .
    dex                                                               ; 9131: ca          .
    lda (nfs_workspace),y                                             ; 9132: b1 9e       ..
; &9134 referenced 1 time by &912e
.nbyte5
    sta l0106,x                                                       ; 9134: 9d 06 01    ...            ; Write result bytes to stacked registers
    cpy #&da                                                          ; 9137: c0 da       ..
    bne nbyte4                                                        ; 9139: d0 f5       ..
; &913b referenced 2 times by &9104, &911b
.return_nbyte
    rts                                                               ; 913b: 60          `

; &913c referenced 3 times by &90f2, &90fb, &9142
.match_osbyte_code
    cmp l9145,x                                                       ; 913c: dd 45 91    .E.
    beq return_match_osbyte                                           ; 913f: f0 03       ..
    dex                                                               ; 9141: ca          .
    bpl match_osbyte_code                                             ; 9142: 10 f8       ..
; &9144 referenced 2 times by &913f, &915c
.return_match_osbyte
    rts                                                               ; 9144: 60          `

; &9145 referenced 1 time by &913c
.l9145
    equb   4,   9, &0a, &15, &9a, &9b, &e1, &e2, &e3, &e4, &0b, &0c   ; 9145: 04 09 0a... ...
    equb &0f, &79, &7a                                                ; 9151: 0f 79 7a    .yz

.sub_c9154
    ldy #&0e                                                          ; 9154: a0 0e       ..             ; Y=&0E: max 14 parameter bytes for OSWORD
    cmp #7                                                            ; 9156: c9 07       ..             ; OSWORD 7 = make a sound
    beq c915e                                                         ; 9158: f0 04       ..
    cmp #8                                                            ; 915a: c9 08       ..             ; OSWORD 8 = define an envelope
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
    bne return_match_osbyte                                           ; 915c: d0 e6       ..             ; Not OSWORD 7 or 8: ignore (BNE exits)
; &915e referenced 1 time by &9158
.c915e
    ldx #&db                                                          ; 915e: a2 db       ..             ; Point workspace to offset &DB for params
    stx nfs_workspace                                                 ; 9160: 86 9e       ..
; &9162 referenced 1 time by &9167
.loop_c9162
    lda (l00f0),y                                                     ; 9162: b1 f0       ..             ; Copy parameter bytes from RX buffer
    sta (nfs_workspace),y                                             ; 9164: 91 9e       ..
    dey                                                               ; 9166: 88          .
    bpl loop_c9162                                                    ; 9167: 10 f9       ..
    iny                                                               ; 9169: c8          .
    dec nfs_workspace                                                 ; 916a: c6 9e       ..
    lda l00ef                                                         ; 916c: a5 ef       ..             ; Store original OSBYTE code at workspace+0
    sta (nfs_workspace),y                                             ; 916e: 91 9e       ..
    sty nfs_workspace                                                 ; 9170: 84 9e       ..
    ldy #&14                                                          ; 9172: a0 14       ..
    lda #&e9                                                          ; 9174: a9 e9       ..             ; Tag as RWORD (port &E9)
    sta (nfs_workspace),y                                             ; 9176: 91 9e       ..
    lda #1                                                            ; 9178: a9 01       ..
    jsr setup_tx_and_send                                             ; 917a: 20 c4 90     ..
    stx nfs_workspace                                                 ; 917d: 86 9e       ..
; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &83B3 to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &917f referenced 2 times by &9062, &9071
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 917f: a2 0d       ..
    ldy #&7c ; '|'                                                    ; 9181: a0 7c       .|
    bit l83b3                                                         ; 9183: 2c b3 83    ,..
    bvs cbset2                                                        ; 9186: 70 05       p.
; ***************************************************************************************
; Control block setup — main entry
; 
; Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
; Reads the template table at &91B4 indexed by X, storing each
; value into the target workspace at offset Y. Both X and Y
; are decremented on each iteration.
; 
; Template sentinel values:
;   &FE = stop (end of template for this entry path)
;   &FD = skip (leave existing value unchanged)
;   &FC = use page high byte of target pointer
; ***************************************************************************************
; &9188 referenced 1 time by &84d1
.ctrl_block_setup
    ldy #&17                                                          ; 9188: a0 17       ..
    ldx #&1a                                                          ; 918a: a2 1a       ..
; &918c referenced 1 time by &924b
.ctrl_block_setup_clv
    clv                                                               ; 918c: b8          .
; &918d referenced 1 time by &9186
.cbset2
    lda ctrl_block_template,x                                         ; 918d: bd b4 91    ...            ; Load template byte from ctrl_block_template[X]
    cmp #&fe                                                          ; 9190: c9 fe       ..
    beq l91b0                                                         ; 9192: f0 1c       ..
    cmp #&fd                                                          ; 9194: c9 fd       ..
    beq l91ac                                                         ; 9196: f0 14       ..
    cmp #&fc                                                          ; 9198: c9 fc       ..
    bne cbset3                                                        ; 919a: d0 08       ..
    equb &a5                                                          ; 919c: a5          .
    equb &9d                                                          ; 919d: 9d          .
    equb &70                                                          ; 919e: 70          p
    equb 2                                                            ; 919f: 02          .
    equb &a5                                                          ; 91a0: a5          .
    equb &9f                                                          ; 91a1: 9f          .
    equb &85                                                          ; 91a2: 85          .              ; PAGE byte → Y=&02 / Y=&74
    equb &9b                                                          ; 91a3: 9b          .              ; → Y=&03 / Y=&75
; &91a4 referenced 1 time by &919a
.cbset3
    equb &70                                                          ; 91a4: 70          p              ; → Y=&04 / Y=&76
    equb 4                                                            ; 91a5: 04          .              ; → Y=&05 / Y=&77
    equb &91                                                          ; 91a6: 91          .              ; PAGE byte → Y=&06 / Y=&78
    equb &9e                                                          ; 91a7: 9e          .
    equb &50                                                          ; 91a8: 50          P              ; → Y=&08 / Y=&7A
    equb 2                                                            ; 91a9: 02          .              ; → Y=&09 / Y=&7B
.cbset4
    equb &91                                                          ; 91aa: 91          .              ; Alt-path only → Y=&70; → Y=&0A / Y=&7C
    equb &9c                                                          ; 91ab: 9c          .              ; STOP — main-path boundary
; &91ac referenced 1 time by &9196
.l91ac
    equb &88                                                          ; 91ac: 88          .              ; SKIP; → Y=&0C (main only)
    equb &ca                                                          ; 91ad: ca          .              ; → Y=&01 / Y=&73; → Y=&0D (main only)
    equb &10                                                          ; 91ae: 10          .
    equb &dd                                                          ; 91af: dd          .              ; SKIP (main only)
; &91b0 referenced 1 time by &9192
.l91b0
    equb &c8                                                          ; 91b0: c8          .              ; → Y=&10 (main only)
    equb &84                                                          ; 91b1: 84          .
    equb &9a                                                          ; 91b2: 9a          .
    equb &60                                                          ; 91b3: 60          `              ; → Y=&07 / Y=&79
; ***************************************************************************************
; Control block initialisation template
; 
; Read by the loop at &918D, indexed by X from a starting value
; down to 0. Values are stored into either (nfs_workspace) or
; (net_rx_ptr) at offset Y, depending on the V flag.
; 
; Two entry paths read different slices of this table:
;   ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
;   ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &83B3
; 
; Sentinel values:
;   &FE = stop processing
;   &FD = skip this offset (decrement Y but don't store)
;   &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)
; ***************************************************************************************
; &91b4 referenced 1 time by &918d
.ctrl_block_template
    equb &85                                                          ; 91b4: 85          .              ; Alt-path only → Y=&6F
    equb 0                                                            ; 91b5: 00          .              ; PAGE byte → Y=&15 (main only)
    equb &fd                                                          ; 91b6: fd          .              ; SKIP; → Y=&16 (main only)
    equb &fd                                                          ; 91b7: fd          .
    equb &7d, &fc, &ff, &ff, &7e, &fc, &ff, &ff,   0,   0, &fe, &80   ; 91b8: 7d fc ff... }..
    equb &93, &fd, &fd, &d9, &fc, &ff, &ff, &de, &fc, &ff, &ff, &fe   ; 91c4: 93 fd fd... ...
    equb &d1, &fd, &fd, &1f, &fd, &ff, &ff, &fd, &fd, &ff, &ff        ; 91d0: d1 fd fd... ...

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
    dex                                                               ; 91db: ca          .
    cpx l00f0                                                         ; 91dc: e4 f0       ..
    bne setup1                                                        ; 91de: d0 07       ..
    lda #&1f                                                          ; 91e0: a9 1f       ..
    sta printer_buf_ptr                                               ; 91e2: 8d 61 0d    .a.
    lda #&41 ; 'A'                                                    ; 91e5: a9 41       .A
; &91e7 referenced 1 time by &91de
.setup1
    sta l0099                                                         ; 91e7: 85 99       ..
; &91e9 referenced 2 times by &91ec, &9200
.return_printer_select
    rts                                                               ; 91e9: 60          `

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
    cpy #4                                                            ; 91ea: c0 04       ..             ; Only handle buffer 4 (network printer)
    bne return_printer_select                                         ; 91ec: d0 fb       ..
    txa                                                               ; 91ee: 8a          .
    dex                                                               ; 91ef: ca          .
    bne c9218                                                         ; 91f0: d0 26       .&
    tsx                                                               ; 91f2: ba          .
    ora l0106,x                                                       ; 91f3: 1d 06 01    ...            ; Force I flag in stacked P to block IRQs
    sta l0106,x                                                       ; 91f6: 9d 06 01    ...
; &91f9 referenced 2 times by &9208, &920d
.prlp1
    lda #osbyte_read_buffer                                           ; 91f9: a9 91       ..             ; OSBYTE &91: extract char from MOS buffer
    ldx #buffer_printer                                               ; 91fb: a2 03       ..
    jsr osbyte                                                        ; 91fd: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_printer_select                                         ; 9200: b0 e7       ..
    tya                                                               ; 9202: 98          .              ; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 9203: 20 0f 92     ..
    cpy #&6e ; 'n'                                                    ; 9206: c0 6e       .n             ; Buffer nearly full? (&6E = threshold)
    bcc prlp1                                                         ; 9208: 90 ef       ..
    jsr flush_output_block                                            ; 920a: 20 37 92     7.
    bcc prlp1                                                         ; 920d: 90 ea       ..
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; ***************************************************************************************
; &920f referenced 2 times by &9203, &921c
.store_output_byte
    ldy printer_buf_ptr                                               ; 920f: ac 61 0d    .a.
    sta (net_rx_ptr),y                                                ; 9212: 91 9c       ..
    inc printer_buf_ptr                                               ; 9214: ee 61 0d    .a.
    rts                                                               ; 9217: 60          `

; &9218 referenced 1 time by &91f0
.c9218
    pha                                                               ; 9218: 48          H
    txa                                                               ; 9219: 8a          .
    eor #1                                                            ; 921a: 49 01       I.             ; EOR #1: toggle print-active flag (bit 0)
    jsr store_output_byte                                             ; 921c: 20 0f 92     ..
    eor l0099                                                         ; 921f: 45 99       E.
    ror a                                                             ; 9221: 6a          j              ; Test if sequence changed (bit 7 mismatch)
    bcc c922a                                                         ; 9222: 90 06       ..
    rol a                                                             ; 9224: 2a          *
    sta l0099                                                         ; 9225: 85 99       ..
    jsr flush_output_block                                            ; 9227: 20 37 92     7.
; &922a referenced 1 time by &9222
.c922a
    lda l0099                                                         ; 922a: a5 99       ..
    and #&f0                                                          ; 922c: 29 f0       ).             ; Extract upper nibble of PFLAGS
    ror a                                                             ; 922e: 6a          j
    tax                                                               ; 922f: aa          .
    pla                                                               ; 9230: 68          h
    ror a                                                             ; 9231: 6a          j              ; Merge print-active bit from original A
    txa                                                               ; 9232: 8a          .
    rol a                                                             ; 9233: 2a          *              ; Recombine into new PFLAGS value
    sta l0099                                                         ; 9234: 85 99       ..
    rts                                                               ; 9236: 60          `

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &9237 referenced 2 times by &920a, &9227
.flush_output_block
    ldy #8                                                            ; 9237: a0 08       ..             ; Store buffer length at workspace offset &08
    lda printer_buf_ptr                                               ; 9239: ad 61 0d    .a.
    sta (nfs_workspace),y                                             ; 923c: 91 9e       ..
    lda net_rx_ptr_hi                                                 ; 923e: a5 9d       ..             ; Store page high byte at offset &09
    iny                                                               ; 9240: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 9241: 91 9e       ..
    ldy #5                                                            ; 9243: a0 05       ..
    sta (nfs_workspace),y                                             ; 9245: 91 9e       ..
    ldy #&0b                                                          ; 9247: a0 0b       ..
    ldx #&26 ; '&'                                                    ; 9249: a2 26       .&             ; X=&26: start from template entry &26
    jsr ctrl_block_setup_clv                                          ; 924b: 20 8c 91     ..            ; Reuse ctrl_block_setup with CLV entry
    dey                                                               ; 924e: 88          .
    lda l0099                                                         ; 924f: a5 99       ..
    pha                                                               ; 9251: 48          H
    rol a                                                             ; 9252: 2a          *
    pla                                                               ; 9253: 68          h
    eor #&80                                                          ; 9254: 49 80       I.             ; Toggle sequence number (bit 7 of PFLAGS)
    sta l0099                                                         ; 9256: 85 99       ..
    rol a                                                             ; 9258: 2a          *
    sta (nfs_workspace),y                                             ; 9259: 91 9e       ..
    ldy #&1f                                                          ; 925b: a0 1f       ..
    sty printer_buf_ptr                                               ; 925d: 8c 61 0d    .a.            ; Reset printer buffer to start (&1F)
    lda #0                                                            ; 9260: a9 00       ..
    tax                                                               ; 9262: aa          .              ; X=&00
    ldy nfs_workspace_hi                                              ; 9263: a4 9f       ..
    cli                                                               ; 9265: 58          X
; ***************************************************************************************
; Byte-stream transmit (BSXMIT/BSPSX)
; 
; Transmits a data packet over econet with sequence number tracking.
; Sets up the TX control block pointer from X/Y, computes the
; sequence bit from A AND fs_sequence_nos (handle-based tracking),
; merges it into the flag byte at (net_tx_ptr)+0, then initiates
; transmit via tx_poll_ff. Sets end addresses (offsets 8/9) to
; &FF to allow unlimited data. Selects port byte &D1 (print) or
; &90 (FS) based on the original A value. Polls the TX result in
; a loop via BRIANX (c8530), retrying while the result bit
; differs from the expected sequence. On success, toggles the
; sequence tracking bit in fs_sequence_nos.
; ***************************************************************************************
; &9266 referenced 2 times by &840c, &8448
.econet_tx_retry
    stx net_tx_ptr                                                    ; 9266: 86 9a       ..
    sty net_tx_ptr_hi                                                 ; 9268: 84 9b       ..
    pha                                                               ; 926a: 48          H
    and fs_sequence_nos                                               ; 926b: 2d 08 0e    -..            ; Compute sequence bit from handle
    beq bsxl1                                                         ; 926e: f0 02       ..
    lda #1                                                            ; 9270: a9 01       ..
; &9272 referenced 1 time by &926e
.bsxl1
    ldy #0                                                            ; 9272: a0 00       ..
    ora (net_tx_ptr),y                                                ; 9274: 11 9a       ..             ; Merge sequence into existing flag byte
    pha                                                               ; 9276: 48          H
    sta (net_tx_ptr),y                                                ; 9277: 91 9a       ..
    jsr tx_poll_ff                                                    ; 9279: 20 ff 85     ..
    lda #&ff                                                          ; 927c: a9 ff       ..             ; End address &FFFF = unlimited data length
    ldy #8                                                            ; 927e: a0 08       ..
    sta (net_tx_ptr),y                                                ; 9280: 91 9a       ..
    iny                                                               ; 9282: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 9283: 91 9a       ..
    pla                                                               ; 9285: 68          h
    tax                                                               ; 9286: aa          .
    ldy #&d1                                                          ; 9287: a0 d1       ..
    pla                                                               ; 9289: 68          h
    pha                                                               ; 928a: 48          H
    beq bspsx                                                         ; 928b: f0 02       ..             ; A=0: port &D1 (print); A!=0: port &90 (FS)
    ldy #&90                                                          ; 928d: a0 90       ..
; &928f referenced 1 time by &928b
.bspsx
    tya                                                               ; 928f: 98          .
    ldy #1                                                            ; 9290: a0 01       ..
    sta (net_tx_ptr),y                                                ; 9292: 91 9a       ..
    txa                                                               ; 9294: 8a          .
    dey                                                               ; 9295: 88          .              ; Y=&00
    pha                                                               ; 9296: 48          H
; &9297 referenced 1 time by &92a3
.bsxl0
    lda #&7f                                                          ; 9297: a9 7f       ..
    sta (net_tx_ptr),y                                                ; 9299: 91 9a       ..
    jsr c8530                                                         ; 929b: 20 30 85     0.
    pla                                                               ; 929e: 68          h
    pha                                                               ; 929f: 48          H
    eor (net_tx_ptr),y                                                ; 92a0: 51 9a       Q.             ; Check if TX result matches expected sequence
    ror a                                                             ; 92a2: 6a          j
    bcs bsxl0                                                         ; 92a3: b0 f2       ..
    pla                                                               ; 92a5: 68          h
    pla                                                               ; 92a6: 68          h
    eor fs_sequence_nos                                               ; 92a7: 4d 08 0e    M..            ; Toggle sequence bit on success
.return_bspsx
    rts                                                               ; 92aa: 60          `

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
; (OSBYTE &C3) using the 3-entry table at &931E.
; On completion, restores the JSR buffer protection bits (LSTAT)
; from OLDJSR to re-enable JSR reception, which was disabled during
; the screen data capture to prevent interference.
; ***************************************************************************************
.lang_2_save_palette_vdu
    lda l00ad                                                         ; 92ab: a5 ad       ..
    pha                                                               ; 92ad: 48          H
    lda #&e9                                                          ; 92ae: a9 e9       ..             ; Point workspace to palette save area (&E9)
    sta nfs_workspace                                                 ; 92b0: 85 9e       ..
    ldy #0                                                            ; 92b2: a0 00       ..
    sty l00ad                                                         ; 92b4: 84 ad       ..
    lda l0350                                                         ; 92b6: ad 50 03    .P.            ; Save current screen MODE to workspace
    sta (nfs_workspace),y                                             ; 92b9: 91 9e       ..
    inc nfs_workspace                                                 ; 92bb: e6 9e       ..
    lda l0351                                                         ; 92bd: ad 51 03    .Q.
    pha                                                               ; 92c0: 48          H
    tya                                                               ; 92c1: 98          .              ; A=&00
; &92c2 referenced 1 time by &92e1
.loop_c92c2
    sta (nfs_workspace),y                                             ; 92c2: 91 9e       ..
    ldx nfs_workspace                                                 ; 92c4: a6 9e       ..
    ldy nfs_workspace_hi                                              ; 92c6: a4 9f       ..
    lda #osword_read_palette                                          ; 92c8: a9 0b       ..             ; OSWORD &0B: read palette for logical colour
    jsr osword                                                        ; 92ca: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92cd: 68          h
    ldy #0                                                            ; 92ce: a0 00       ..
    sta (nfs_workspace),y                                             ; 92d0: 91 9e       ..
    iny                                                               ; 92d2: c8          .              ; Y=&01
    lda (nfs_workspace),y                                             ; 92d3: b1 9e       ..
    pha                                                               ; 92d5: 48          H
    ldx nfs_workspace                                                 ; 92d6: a6 9e       ..
    inc nfs_workspace                                                 ; 92d8: e6 9e       ..
    inc l00ad                                                         ; 92da: e6 ad       ..
    dey                                                               ; 92dc: 88          .              ; Y=&00
    lda l00ad                                                         ; 92dd: a5 ad       ..
    cpx #&f9                                                          ; 92df: e0 f9       ..             ; Loop until workspace wraps past &F9
    bne loop_c92c2                                                    ; 92e1: d0 df       ..
    pla                                                               ; 92e3: 68          h
    sty l00ad                                                         ; 92e4: 84 ad       ..
    inc nfs_workspace                                                 ; 92e6: e6 9e       ..
    jsr save_vdu_state                                                ; 92e8: 20 f7 92     ..            ; Save cursor pos and OSBYTE state values
    inc nfs_workspace                                                 ; 92eb: e6 9e       ..
    pla                                                               ; 92ed: 68          h
    sta l00ad                                                         ; 92ee: 85 ad       ..
; &92f0 referenced 4 times by &84b5, &84dd, &8504, &8eee
.clear_jsr_protection
    lda saved_jsr_mask                                                ; 92f0: ad 65 0d    .e.            ; Restore LSTAT from saved OLDJSR value
    sta prot_status                                                   ; 92f3: 8d 63 0d    .c.
    rts                                                               ; 92f6: 60          `

; ***************************************************************************************
; Save VDU workspace state
; 
; Stores the cursor position value from &0355 into NFS workspace,
; then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
; and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
; each result into consecutive workspace bytes.
; ***************************************************************************************
; &92f7 referenced 1 time by &92e8
.save_vdu_state
    lda l0355                                                         ; 92f7: ad 55 03    .U.
    sta (nfs_workspace),y                                             ; 92fa: 91 9e       ..
    tax                                                               ; 92fc: aa          .
    jsr read_vdu_osbyte                                               ; 92fd: 20 0a 93     ..
    inc nfs_workspace                                                 ; 9300: e6 9e       ..
    tya                                                               ; 9302: 98          .
    sta (nfs_workspace,x)                                             ; 9303: 81 9e       ..
    jsr read_vdu_osbyte_x0                                            ; 9305: 20 08 93     ..
; &9308 referenced 1 time by &9305
.read_vdu_osbyte_x0
    ldx #0                                                            ; 9308: a2 00       ..
; &930a referenced 1 time by &92fd
.read_vdu_osbyte
    ldy l00ad                                                         ; 930a: a4 ad       ..
    inc l00ad                                                         ; 930c: e6 ad       ..
    inc nfs_workspace                                                 ; 930e: e6 9e       ..
    lda l931e,y                                                       ; 9310: b9 1e 93    ...
    ldy #&ff                                                          ; 9313: a0 ff       ..
    jsr osbyte                                                        ; 9315: 20 f4 ff     ..
    txa                                                               ; 9318: 8a          .
    ldx #0                                                            ; 9319: a2 00       ..
    sta (nfs_workspace,x)                                             ; 931b: 81 9e       ..
    rts                                                               ; 931d: 60          `

; &931e referenced 1 time by &9310
.l931e
    equb &85, &c2, &c3                                                ; 931e: 85 c2 c3    ...
; &9321 referenced 1 time by &8179

    org &9662

    equb &0d                                                          ; 9662: 0d          .

    cpy #&86                                                          ; 9663: c0 86       ..
    bcs c9672                                                         ; 9665: b0 0b       ..
    lda prot_status                                                   ; 9667: ad 63 0d    .c.
    sta saved_jsr_mask                                                ; 966a: 8d 65 0d    .e.
    ora #&1c                                                          ; 966d: 09 1c       ..
    sta prot_status                                                   ; 966f: 8d 63 0d    .c.
; &9672 referenced 1 time by &9665
.c9672
    lda #&9b                                                          ; 9672: a9 9b       ..
    pha                                                               ; 9674: 48          H
    lda l9a9d,y                                                       ; 9675: b9 9d 9a    ...
    pha                                                               ; 9678: 48          H
.svc_5_unknown_irq
    rts                                                               ; 9679: 60          `

; ***************************************************************************************
; ADLC initialisation
; 
; Reads station ID (INTOFF side effect), performs full ADLC reset,
; checks for Tube presence (OSBYTE &EA), then falls through to
; adlc_init_workspace.
; ***************************************************************************************
; &967a referenced 1 time by &06d1[4]
.adlc_init
    bit station_id_disable_net_nmis                                   ; 967a: 2c 18 fe    ,..
    jsr adlc_full_reset                                               ; 967d: 20 3d 9f     =.
    lda #osbyte_read_tube_presence                                    ; 9680: a9 ea       ..
    ldx #0                                                            ; 9682: a2 00       ..
    stx econet_init_flag                                              ; 9684: 8e 66 0d    .f.
    ldy #&ff                                                          ; 9687: a0 ff       ..
    jsr osbyte                                                        ; 9689: 20 f4 ff     ..            ; Read Tube present flag
    stx tube_flag                                                     ; 968c: 8e 67 0d    .g.            ; X=value of Tube present flag
    lda #osbyte_issue_service_request                                 ; 968f: a9 8f       ..
    ldx #&0c                                                          ; 9691: a2 0c       ..
    ldy #&ff                                                          ; 9693: a0 ff       ..
; ***************************************************************************************
; Initialise NMI workspace
; 
; New in 3.35D: issues OSBYTE &8F with X=&0C (NMI claim service
; request) before copying the NMI shim. Sub-entry at &9698 skips
; the service request for quick re-init. Then copies 32 bytes of
; NMI shim from ROM (&9F7D) to RAM (&0D00), patches the current
; ROM bank number into the shim's self-modifying code at &0D07,
; sets TX clear flag and econet_init_flag to &80, reads station ID
; from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
; and re-enables NMIs by reading &FE20 (INTON side effect).
; ***************************************************************************************
.adlc_init_workspace
    jsr osbyte                                                        ; 9695: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=12 - NMI claim
; &9698 referenced 1 time by &06d7[4]
.c9698
    ldy #&20 ; ' '                                                    ; 9698: a0 20       .              ; Copy 32 bytes of NMI shim from ROM to &0D00
; &969a referenced 1 time by &96a1
.loop_c969a
    lda l9f7c,y                                                       ; 969a: b9 7c 9f    .|.
    sta l0cff,y                                                       ; 969d: 99 ff 0c    ...
    dey                                                               ; 96a0: 88          .
    bne loop_c969a                                                    ; 96a1: d0 f7       ..
    lda romsel_copy                                                   ; 96a3: a5 f4       ..             ; Patch current ROM bank into NMI shim
    sta nmi_shim_07                                                   ; 96a5: 8d 07 0d    ...
    lda #&80                                                          ; 96a8: a9 80       ..             ; &80 = Econet initialised
    sta tx_clear_flag                                                 ; 96aa: 8d 62 0d    .b.
    sta econet_init_flag                                              ; 96ad: 8d 66 0d    .f.
    lda station_id_disable_net_nmis                                   ; 96b0: ad 18 fe    ...            ; Read station ID (&FE18 = INTOFF side effect)
    sta tx_src_stn                                                    ; 96b3: 8d 22 0d    .".
    sty tx_src_net                                                    ; 96b6: 8c 23 0d    .#.            ; Y=0 after copy loop: net = local
    sty need_release_tube                                             ; 96b9: 84 98       ..             ; Clear Tube release flag
    bit video_ula_control                                             ; 96bb: 2c 20 fe    , .            ; INTON: re-enable NMIs (&FE20 read side effect)
    rts                                                               ; 96be: 60          `

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
; &96bf referenced 1 time by &9f88
.nmi_rx_scout
    lda #1                                                            ; 96bf: a9 01       ..             ; A=&01: mask for SR2 bit0 (AP = Address Present)
    bit econet_control23_or_status2                                   ; 96c1: 2c a1 fe    ,..            ; BIT SR2: Z = A AND SR2 -- tests if AP is set
    beq scout_error                                                   ; 96c4: f0 38       .8             ; AP not set, no incoming data -- check for errors
    lda econet_data_continue_frame                                    ; 96c6: ad a2 fe    ...            ; Read first RX byte (destination station address)
    cmp station_id_disable_net_nmis                                   ; 96c9: cd 18 fe    ...            ; Compare to our station ID (&FE18 read = INTOFF, disables NMIs)
    beq c96d7                                                         ; 96cc: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 96ce: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 96d0: d0 18       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 96d2: a9 40       .@             ; Flag &40 = broadcast frame
    sta tx_flags                                                      ; 96d4: 8d 4a 0d    .J.
; &96d7 referenced 1 time by &96cc
.c96d7
    lda #&dc                                                          ; 96d7: a9 dc       ..             ; Install next NMI handler at &96DC (RX scout net byte)
    jmp l0d11                                                         ; 96d9: 4c 11 0d    L..

; ***************************************************************************************
; RX scout second byte handler
; 
; Reads the second byte of an incoming scout (destination network).
; Checks for network match: 0 = local network (accept), &FF = broadcast
; (accept and flag), anything else = reject.
; Installs the scout data reading loop handler at &970E.
; ***************************************************************************************
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 96dc: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 96df: 10 1d       ..             ; No RDA -- check errors
    lda econet_data_continue_frame                                    ; 96e1: ad a2 fe    ...            ; Read destination network byte
    beq c96f2                                                         ; 96e4: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 96e6: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq c96f5                                                         ; 96e8: f0 0b       ..             ; Broadcast network -- accept
; &96ea referenced 1 time by &96d0
.scout_reject
    lda #&a2                                                          ; 96ea: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 96ec: 8d a0 fe    ...
    jmp c99eb                                                         ; 96ef: 4c eb 99    L..

; &96f2 referenced 1 time by &96e4
.c96f2
    sta tx_flags                                                      ; 96f2: 8d 4a 0d    .J.            ; Network = 0 (local): clear tx_flags
; &96f5 referenced 1 time by &96e8
.c96f5
    sta port_buf_len                                                  ; 96f5: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&0e                                                          ; 96f7: a9 0e       ..             ; Install scout data reading loop at &970E
    ldy #&97                                                          ; 96f9: a0 97       ..
    jmp set_nmi_vector                                                ; 96fb: 4c 0e 0d    L..

; ***************************************************************************************
; Scout error/discard handler
; 
; Reached when the scout data loop sees no RDA (BPL at &9713) or
; when scout completion finds unexpected SR2 state.
; If SR2 & &81 is non-zero (AP or RDA still active), performs full
; ADLC reset and discards. If zero (clean end), discards via &99E8.
; This path is a common landing for any unexpected ADLC state during
; scout reception.
; ***************************************************************************************
; &96fe referenced 5 times by &96c4, &96df, &9713, &9747, &9749
.scout_error
    lda econet_control23_or_status2                                   ; 96fe: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 9701: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 9703: f0 06       ..             ; Neither set -- clean end, discard via &99E8
    jsr adlc_full_reset                                               ; 9705: 20 3d 9f     =.            ; Unexpected data/status: full ADLC reset
    jmp c99eb                                                         ; 9708: 4c eb 99    L..            ; Discard and return to idle

; &970b referenced 1 time by &9703
.scout_discard
    jmp discard_listen                                                ; 970b: 4c e8 99    L..

; ***************************************************************************************
; Scout data reading loop
; 
; Reads the body of a scout frame, two bytes per iteration. Stores
; bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
; Between each pair it checks SR2:
;   - At entry (&9710): SR2 read, BPL tests RDA (bit7)
;     - No RDA (BPL) -> error (&96FE)
;     - RDA set (BMI) -> read byte
;   - After first byte (&971C): full SR2 tested
;     - SR2 non-zero (BNE) -> scout completion (&9738)
;       This is the FV detection point: when FV is set (by inline refill
;       of the last byte during the preceding RX FIFO read), SR2 is
;       non-zero and the branch is taken.
;     - SR2 = 0 -> read second byte and loop
;   - After second byte (&9730): re-test full SR2
;     - SR2 non-zero (BNE) -> loop back to &9713
;     - SR2 = 0 -> RTI, wait for next NMI
; The loop ends at Y=&0C (12 bytes max in scout buffer).
; ***************************************************************************************
    ldy port_buf_len                                                  ; 970e: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 9710: ad a1 fe    ...            ; Read SR2
; &9713 referenced 1 time by &9733
.scout_loop_rda
    bpl scout_error                                                   ; 9713: 10 e9       ..             ; No RDA -- error handler &96FE
    lda econet_data_continue_frame                                    ; 9715: ad a2 fe    ...            ; Read data byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9718: 99 3d 0d    .=.            ; Store at &0D3D+Y (scout buffer)
    iny                                                               ; 971b: c8          .              ; Advance buffer index
    lda econet_control23_or_status2                                   ; 971c: ad a1 fe    ...            ; Read SR2 again (FV detection point)
    bmi scout_loop_second                                             ; 971f: 30 02       0.             ; RDA set -- more data, read second byte
    bne scout_complete                                                ; 9721: d0 15       ..             ; SR2 non-zero (FV or other) -- scout completion
; &9723 referenced 1 time by &971f
.scout_loop_second
    lda econet_data_continue_frame                                    ; 9723: ad a2 fe    ...            ; Read second byte of pair
    sta rx_src_stn,y                                                  ; 9726: 99 3d 0d    .=.            ; Store at &0D3D+Y
    iny                                                               ; 9729: c8          .              ; Advance and check buffer limit
    cpy #&0c                                                          ; 972a: c0 0c       ..
    beq scout_complete                                                ; 972c: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 972e: 84 a2       ..
    lda econet_control23_or_status2                                   ; 9730: ad a1 fe    ...            ; Read SR2 for next pair
    bne scout_loop_rda                                                ; 9733: d0 de       ..             ; SR2 non-zero -- loop back for more bytes
    jmp nmi_rti                                                       ; 9735: 4c 14 0d    L..            ; SR2 = 0 -- RTI, wait for next NMI

; ***************************************************************************************
; Scout completion handler
; 
; Reached from the scout data loop when SR2 is non-zero (FV detected).
; Disables PSE to allow individual SR2 bit testing:
;   CR1=&00 (clear all enables)
;   CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
; Then checks FV (bit1) and RDA (bit7):
;   - No FV (BEQ) -> error &96FE (not a valid frame end)
;   - FV set, no RDA (BPL) -> error &96FE (missing last byte)
;   - FV set, RDA set -> read last byte, process scout
; After reading the last byte, the complete scout buffer (&0D3D-&0D48)
; contains: src_stn, src_net, ctrl, port [, extra_data...].
; The port byte at &0D40 determines further processing:
;   - Port = 0 -> immediate operation (&9A46)
;   - Port non-zero -> check if it matches an open receive block
; ***************************************************************************************
; &9738 referenced 2 times by &9721, &972c
.scout_complete
    lda #0                                                            ; 9738: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 973a: 8d a0 fe    ...
    lda #&84                                                          ; 973d: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 973f: 8d a1 fe    ...
    lda #2                                                            ; 9742: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9744: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 9747: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 9749: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 974b: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 974e: 99 3d 0d    .=.            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 9751: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 9753: 8d a0 fe    ...
    sec                                                               ; 9756: 38          8              ; Set bit7 of need_release_tube flag
    ror need_release_tube                                             ; 9757: 66 98       f.
    lda rx_port                                                       ; 9759: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 975c: d0 03       ..             ; Port non-zero -- look for matching receive block
.scout_no_match
    jmp immediate_op                                                  ; 975e: 4c 46 9a    LF.            ; Port = 0 -- immediate operation handler

; &9761 referenced 1 time by &975c
.scout_match_port
    bit tx_flags                                                      ; 9761: 2c 4a 0d    ,J.            ; Check if broadcast (bit6 of tx_flags)
    bvc c976b                                                         ; 9764: 50 05       P.
    lda #7                                                            ; 9766: a9 07       ..             ; CR2=&07: broadcast prep
    sta econet_control23_or_status2                                   ; 9768: 8d a1 fe    ...
; &976b referenced 1 time by &9764
.c976b
    bit rx_flags                                                      ; 976b: 2c 64 0d    ,d.            ; Check if RX port list active (bit7)
    bpl c97ae                                                         ; 976e: 10 3e       .>             ; No active ports -- try NFS workspace
    lda #&c0                                                          ; 9770: a9 c0       ..             ; Start scanning port list at page &C0
    ldy #0                                                            ; 9772: a0 00       ..
; &9774 referenced 1 time by &97b7
.c9774
    sta port_ws_offset                                                ; 9774: 85 a6       ..
    sty rx_buf_offset                                                 ; 9776: 84 a7       ..
; &9778 referenced 1 time by &97a9
.c9778
    ldy #0                                                            ; 9778: a0 00       ..
    lda (port_ws_offset),y                                            ; 977a: b1 a6       ..             ; Read port control byte from slot
    beq c97ab                                                         ; 977c: f0 2d       .-             ; Zero = end of port list, no match
    cmp #&7f                                                          ; 977e: c9 7f       ..             ; &7F = any-port wildcard
    bne c979e                                                         ; 9780: d0 1c       ..
    iny                                                               ; 9782: c8          .              ; Y=&01
    lda (port_ws_offset),y                                            ; 9783: b1 a6       ..
    beq c978c                                                         ; 9785: f0 05       ..
    cmp rx_port                                                       ; 9787: cd 40 0d    .@.            ; Check if port matches this slot
    bne c979e                                                         ; 978a: d0 12       ..
; &978c referenced 1 time by &9785
.c978c
    iny                                                               ; 978c: c8          .
    lda (port_ws_offset),y                                            ; 978d: b1 a6       ..
    beq c97b9                                                         ; 978f: f0 28       .(
    cmp rx_src_stn                                                    ; 9791: cd 3d 0d    .=.            ; Check if source station matches
    bne c979e                                                         ; 9794: d0 08       ..
    iny                                                               ; 9796: c8          .
    lda (port_ws_offset),y                                            ; 9797: b1 a6       ..
    cmp rx_src_net                                                    ; 9799: cd 3e 0d    .>.            ; Check if source network matches
    beq c97b9                                                         ; 979c: f0 1b       ..
; &979e referenced 3 times by &9780, &978a, &9794
.c979e
    lda rx_buf_offset                                                 ; 979e: a5 a7       ..
    beq c97ae                                                         ; 97a0: f0 0c       ..
    lda port_ws_offset                                                ; 97a2: a5 a6       ..
    clc                                                               ; 97a4: 18          .
    adc #&0c                                                          ; 97a5: 69 0c       i.             ; Advance to next 12-byte port slot
    sta port_ws_offset                                                ; 97a7: 85 a6       ..
    bcc c9778                                                         ; 97a9: 90 cd       ..
; &97ab referenced 2 times by &977c, &97b1
.c97ab
    jmp c9835                                                         ; 97ab: 4c 35 98    L5.

; &97ae referenced 2 times by &976e, &97a0
.c97ae
    bit rx_flags                                                      ; 97ae: 2c 64 0d    ,d.            ; Try NFS workspace if paged list exhausted
    bvc c97ab                                                         ; 97b1: 50 f8       P.
    lda #0                                                            ; 97b3: a9 00       ..
    ldy nfs_workspace_hi                                              ; 97b5: a4 9f       ..             ; NFS workspace high byte for port list
    bne c9774                                                         ; 97b7: d0 bb       ..
; &97b9 referenced 2 times by &978f, &979c
.c97b9
    lda #3                                                            ; 97b9: a9 03       ..             ; Match found: set scout_status = 3
    sta scout_status                                                  ; 97bb: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 97be: 20 ca 9e     ..            ; Calculate transfer parameters
    bcc c9835                                                         ; 97c1: 90 72       .r
    bit tx_flags                                                      ; 97c3: 2c 4a 0d    ,J.
    bvc c97cb                                                         ; 97c6: 50 03       P.
    jmp c99f2                                                         ; 97c8: 4c f2 99    L..

; &97cb referenced 1 time by &97c6
.c97cb
    lda #&44 ; 'D'                                                    ; 97cb: a9 44       .D             ; CR1=&44: RX_RESET | TIE
    sta econet_control1_or_status1                                    ; 97cd: 8d a0 fe    ...
    lda #&a7                                                          ; 97d0: a9 a7       ..             ; CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE
    sta econet_control23_or_status2                                   ; 97d2: 8d a1 fe    ...
    lda #&dc                                                          ; 97d5: a9 dc       ..             ; Install data_rx_setup at &97DC
    ldy #&97                                                          ; 97d7: a0 97       ..
    jmp ack_tx_write_dest                                             ; 97d9: 4c 07 99    L..

.data_rx_setup
    lda #&82                                                          ; 97dc: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 97de: 8d a0 fe    ...
    lda #&e6                                                          ; 97e1: a9 e6       ..             ; Install nmi_data_rx at &97E6
    jmp l0d11                                                         ; 97e3: 4c 11 0d    L..

; ***************************************************************************************
; Data frame RX handler (four-way handshake)
; 
; Receives the data frame after the scout ACK has been sent.
; First checks AP (Address Present) for the start of the data frame.
; Reads and validates the first two address bytes (dest_stn, dest_net)
; against our station address, then installs continuation handlers
; to read the remaining data payload into the open port buffer.
; 
; Handler chain: &97E6 (AP+addr check) -> &97FA (net=0 check) ->
; &9810 (skip ctrl+port) -> &9843 (bulk data read) -> &9877 (completion)
; ***************************************************************************************
.nmi_data_rx
    lda #1                                                            ; 97e6: a9 01       ..             ; A=&01: mask for AP (Address Present)
    bit econet_control23_or_status2                                   ; 97e8: 2c a1 fe    ,..
    beq c9835                                                         ; 97eb: f0 48       .H
    lda econet_data_continue_frame                                    ; 97ed: ad a2 fe    ...
    cmp station_id_disable_net_nmis                                   ; 97f0: cd 18 fe    ...
    bne c9835                                                         ; 97f3: d0 40       .@
    lda #&fa                                                          ; 97f5: a9 fa       ..             ; Install net check handler at &97FA
    jmp l0d11                                                         ; 97f7: 4c 11 0d    L..

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 97fa: 2c a1 fe    ,..            ; Validate source network = 0
    bpl c9835                                                         ; 97fd: 10 36       .6
    lda econet_data_continue_frame                                    ; 97ff: ad a2 fe    ...
    bne c9835                                                         ; 9802: d0 31       .1
    lda #&10                                                          ; 9804: a9 10       ..             ; Install skip handler at &9810
    ldy #&98                                                          ; 9806: a0 98       ..
    bit econet_control1_or_status1                                    ; 9808: 2c a0 fe    ,..            ; SR1 bit7: IRQ, data already waiting
    bmi nmi_data_rx_skip                                              ; 980b: 30 03       0.
    jmp set_nmi_vector                                                ; 980d: 4c 0e 0d    L..

; &9810 referenced 1 time by &980b
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 9810: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl c9835                                                         ; 9813: 10 20       .
    lda econet_data_continue_frame                                    ; 9815: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 9818: ad a2 fe    ...            ; Discard port byte
; &981b referenced 1 time by &9e9e
.c981b
    lda #2                                                            ; 981b: a9 02       ..
    bit tx_flags                                                      ; 981d: 2c 4a 0d    ,J.
    bne c982e                                                         ; 9820: d0 0c       ..
    lda #&43 ; 'C'                                                    ; 9822: a9 43       .C
    ldy #&98                                                          ; 9824: a0 98       ..
    bit econet_control1_or_status1                                    ; 9826: 2c a0 fe    ,..
    bmi nmi_data_rx_bulk                                              ; 9829: 30 18       0.
    jmp set_nmi_vector                                                ; 982b: 4c 0e 0d    L..

; &982e referenced 1 time by &9820
.c982e
    lda #&a0                                                          ; 982e: a9 a0       ..
    ldy #&98                                                          ; 9830: a0 98       ..
    jmp set_nmi_vector                                                ; 9832: 4c 0e 0d    L..

; &9835 referenced 12 times by &97ab, &97c1, &97eb, &97f3, &97fd, &9802, &9813, &9856, &9888, &988e, &994b, &9a76
.c9835
    lda tx_flags                                                      ; 9835: ad 4a 0d    .J.
    bpl rx_error                                                      ; 9838: 10 03       ..
    jmp tx_result_fail                                                ; 983a: 4c ac 9e    L..

; &983d referenced 1 time by &9838
.rx_error
.rx_error_reset
    jsr adlc_full_reset                                               ; 983d: 20 3d 9f     =.
    jmp discard_reset_listen                                          ; 9840: 4c db 99    L..

; ***************************************************************************************
; Data frame bulk read loop
; 
; Reads data payload bytes from the RX FIFO and stores them into
; the open port buffer at (open_port_buf),Y. Reads bytes in pairs
; (like the scout data loop), checking SR2 between each pair.
; SR2 non-zero (FV or other) -> frame completion at &9877.
; SR2 = 0 -> RTI, wait for next NMI to continue.
; ***************************************************************************************
; &9843 referenced 1 time by &9829
.nmi_data_rx_bulk
    ldy port_buf_len                                                  ; 9843: a4 a2       ..             ; Y = buffer offset, resume from last position
    lda econet_control23_or_status2                                   ; 9845: ad a1 fe    ...            ; Read SR2 for next pair
; &9848 referenced 1 time by &9872
.c9848
    bpl data_rx_complete                                              ; 9848: 10 2d       .-
    lda econet_data_continue_frame                                    ; 984a: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 984d: 91 a4       ..
    iny                                                               ; 984f: c8          .
    bne c9858                                                         ; 9850: d0 06       ..
    inc open_port_buf_hi                                              ; 9852: e6 a5       ..
    dec port_buf_len_hi                                               ; 9854: c6 a3       ..
    beq c9835                                                         ; 9856: f0 dd       ..
; &9858 referenced 1 time by &9850
.c9858
    lda econet_control23_or_status2                                   ; 9858: ad a1 fe    ...
    bmi c985f                                                         ; 985b: 30 02       0.
    bne data_rx_complete                                              ; 985d: d0 18       ..
; &985f referenced 1 time by &985b
.c985f
    lda econet_data_continue_frame                                    ; 985f: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 9862: 91 a4       ..
    iny                                                               ; 9864: c8          .
    sty port_buf_len                                                  ; 9865: 84 a2       ..
    bne c986f                                                         ; 9867: d0 06       ..
    inc open_port_buf_hi                                              ; 9869: e6 a5       ..
    dec port_buf_len_hi                                               ; 986b: c6 a3       ..
    beq data_rx_complete                                              ; 986d: f0 08       ..
; &986f referenced 1 time by &9867
.c986f
    lda econet_control23_or_status2                                   ; 986f: ad a1 fe    ...
    bne c9848                                                         ; 9872: d0 d4       ..
    jmp nmi_rti                                                       ; 9874: 4c 14 0d    L..

; ***************************************************************************************
; Data frame completion
; 
; Reached when SR2 non-zero during data RX (FV detected).
; Same pattern as scout completion (&9738): disables PSE (CR2=&84,
; CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.
; If extra data available and buffer space remains, stores it.
; Proceeds to send the final ACK via &98EE.
; ***************************************************************************************
; &9877 referenced 3 times by &9848, &985d, &986d
.data_rx_complete
    lda #&84                                                          ; 9877: a9 84       ..             ; CR2=&84: disable PSE for individual bit testing
    sta econet_control23_or_status2                                   ; 9879: 8d a1 fe    ...
    lda #0                                                            ; 987c: a9 00       ..             ; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 987e: 8d a0 fe    ...
    sty port_buf_len                                                  ; 9881: 84 a2       ..
    lda #2                                                            ; 9883: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 9885: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq c9835                                                         ; 9888: f0 ab       ..             ; No FV -- error
    bpl c989d                                                         ; 988a: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 988c: a5 a3       ..
; &988e referenced 3 times by &98ab, &98d2, &98de
.c988e
    beq c9835                                                         ; 988e: f0 a5       ..
    lda econet_data_continue_frame                                    ; 9890: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 9893: a4 a2       ..
    sta (open_port_buf),y                                             ; 9895: 91 a4       ..
    inc port_buf_len                                                  ; 9897: e6 a2       ..
    bne c989d                                                         ; 9899: d0 02       ..
    inc open_port_buf_hi                                              ; 989b: e6 a5       ..
; &989d referenced 2 times by &988a, &9899
.c989d
    jmp ack_tx                                                        ; 989d: 4c ee 98    L..

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 98a0: ad a1 fe    ...
; &98a3 referenced 1 time by &98be
.loop_c98a3
    bpl data_rx_tube_complete                                         ; 98a3: 10 1e       ..
    lda econet_data_continue_frame                                    ; 98a5: ad a2 fe    ...
    jsr sub_c9a37                                                     ; 98a8: 20 37 9a     7.
    beq c988e                                                         ; 98ab: f0 e1       ..
    sta tube_data_register_3                                          ; 98ad: 8d e5 fe    ...
    lda econet_data_continue_frame                                    ; 98b0: ad a2 fe    ...
    sta tube_data_register_3                                          ; 98b3: 8d e5 fe    ...
    jsr sub_c9a37                                                     ; 98b6: 20 37 9a     7.
    beq data_rx_tube_complete                                         ; 98b9: f0 08       ..
    lda econet_control23_or_status2                                   ; 98bb: ad a1 fe    ...
    bne loop_c98a3                                                    ; 98be: d0 e3       ..
.data_rx_tube_error
    jmp nmi_rti                                                       ; 98c0: 4c 14 0d    L..

; &98c3 referenced 2 times by &98a3, &98b9
.data_rx_tube_complete
    lda #0                                                            ; 98c3: a9 00       ..
    sta econet_control1_or_status1                                    ; 98c5: 8d a0 fe    ...
    lda #&84                                                          ; 98c8: a9 84       ..
    sta econet_control23_or_status2                                   ; 98ca: 8d a1 fe    ...
    lda #2                                                            ; 98cd: a9 02       ..
    bit econet_control23_or_status2                                   ; 98cf: 2c a1 fe    ,..
    beq c988e                                                         ; 98d2: f0 ba       ..
    bpl ack_tx                                                        ; 98d4: 10 18       ..
    lda port_buf_len                                                  ; 98d6: a5 a2       ..
    ora port_buf_len_hi                                               ; 98d8: 05 a3       ..
    ora open_port_buf                                                 ; 98da: 05 a4       ..
    ora open_port_buf_hi                                              ; 98dc: 05 a5       ..
    beq c988e                                                         ; 98de: f0 ae       ..
    lda econet_data_continue_frame                                    ; 98e0: ad a2 fe    ...
    sta rx_extra_byte                                                 ; 98e3: 8d 5d 0d    .].
    lda #&20 ; ' '                                                    ; 98e6: a9 20       .
    ora tx_flags                                                      ; 98e8: 0d 4a 0d    .J.
    sta tx_flags                                                      ; 98eb: 8d 4a 0d    .J.
; ***************************************************************************************
; ACK transmission
; 
; Sends a scout ACK or final ACK frame as part of the four-way handshake.
; If bit7 of &0D4A is set, this is a final ACK -> completion (&9EA8).
; Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
; frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
; The ACK frame has no data payload -- just address bytes.
; 
; After writing the address bytes to the TX FIFO, installs the next
; NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
; and sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
; &98ee referenced 2 times by &989d, &98d4
.ack_tx
    lda tx_flags                                                      ; 98ee: ad 4a 0d    .J.
    bpl ack_tx_configure                                              ; 98f1: 10 06       ..
    jsr sub_c994e                                                     ; 98f3: 20 4e 99     N.
    jmp tx_result_ok                                                  ; 98f6: 4c a8 9e    L..

; &98f9 referenced 1 time by &98f1
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 98f9: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 98fb: 8d a0 fe    ...
    lda #&a7                                                          ; 98fe: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9900: 8d a1 fe    ...
    lda #&95                                                          ; 9903: a9 95       ..             ; Save &9995 (post-ACK port check) in &0D4B/&0D4C
    ldy #&99                                                          ; 9905: a0 99       ..
; &9907 referenced 1 time by &97d9
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 9907: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 990a: 8c 4c 0d    .L.
    lda rx_src_stn                                                    ; 990d: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 9910: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc c994b                                                         ; 9913: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9915: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 9918: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 991b: 8d a2 fe    ...
    lda #&25 ; '%'                                                    ; 991e: a9 25       .%             ; Install nmi_ack_tx_src at &9925
    ldy #&99                                                          ; 9920: a0 99       ..
    jmp set_nmi_vector                                                ; 9922: 4c 0e 0d    L..

; ***************************************************************************************
; ACK TX continuation
; 
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 9925: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9928: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc c994b                                                         ; 992b: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 992d: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9930: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9932: 8d a2 fe    ...
    lda tx_flags                                                      ; 9935: ad 4a 0d    .J.
    bmi c9948                                                         ; 9938: 30 0e       0.
    lda #&3f ; '?'                                                    ; 993a: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | PSE
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
    sta econet_control23_or_status2                                   ; 993c: 8d a1 fe    ...
    lda nmi_next_lo                                                   ; 993f: ad 4b 0d    .K.            ; Install saved handler from &0D4B/&0D4C
    ldy nmi_next_hi                                                   ; 9942: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 9945: 4c 0e 0d    L..

; &9948 referenced 1 time by &9938
.c9948
    jmp data_tx_begin                                                 ; 9948: 4c b3 9d    L..

; &994b referenced 2 times by &9913, &992b
.c994b
    jmp c9835                                                         ; 994b: 4c 35 98    L5.

; &994e referenced 2 times by &98f3, &99a4
.sub_c994e
    lda #2                                                            ; 994e: a9 02       ..
    bit tx_flags                                                      ; 9950: 2c 4a 0d    ,J.
    beq return_10                                                     ; 9953: f0 3f       .?
    clc                                                               ; 9955: 18          .
    php                                                               ; 9956: 08          .
    ldy #8                                                            ; 9957: a0 08       ..
; &9959 referenced 1 time by &9965
.loop_c9959
    lda (port_ws_offset),y                                            ; 9959: b1 a6       ..
    plp                                                               ; 995b: 28          (
    adc net_tx_ptr,y                                                  ; 995c: 79 9a 00    y..
    sta (port_ws_offset),y                                            ; 995f: 91 a6       ..
    iny                                                               ; 9961: c8          .
    php                                                               ; 9962: 08          .
    cpy #&0c                                                          ; 9963: c0 0c       ..
    bcc loop_c9959                                                    ; 9965: 90 f2       ..
    plp                                                               ; 9967: 28          (
    lda #&20 ; ' '                                                    ; 9968: a9 20       .
    bit tx_flags                                                      ; 996a: 2c 4a 0d    ,J.
    beq c9992                                                         ; 996d: f0 23       .#
    txa                                                               ; 996f: 8a          .
    pha                                                               ; 9970: 48          H
    lda #8                                                            ; 9971: a9 08       ..
    clc                                                               ; 9973: 18          .
    adc port_ws_offset                                                ; 9974: 65 a6       e.
    tax                                                               ; 9976: aa          .
    ldy rx_buf_offset                                                 ; 9977: a4 a7       ..
    lda #1                                                            ; 9979: a9 01       ..
    jsr tube_addr_claim                                               ; 997b: 20 06 04     ..
    lda rx_extra_byte                                                 ; 997e: ad 5d 0d    .].
    sta tube_data_register_3                                          ; 9981: 8d e5 fe    ...
    sec                                                               ; 9984: 38          8
    ldy #8                                                            ; 9985: a0 08       ..
; &9987 referenced 1 time by &998e
.loop_c9987
    lda #0                                                            ; 9987: a9 00       ..
    adc (port_ws_offset),y                                            ; 9989: 71 a6       q.
    sta (port_ws_offset),y                                            ; 998b: 91 a6       ..
    iny                                                               ; 998d: c8          .
    bcs loop_c9987                                                    ; 998e: b0 f7       ..
    pla                                                               ; 9990: 68          h
    tax                                                               ; 9991: aa          .
; &9992 referenced 1 time by &996d
.c9992
    lda #&ff                                                          ; 9992: a9 ff       ..
; &9994 referenced 1 time by &9953
.return_10
    rts                                                               ; 9994: 60          `

    lda rx_port                                                       ; 9995: ad 40 0d    .@.
    bne c99a4                                                         ; 9998: d0 0a       ..
    ldy rx_ctrl                                                       ; 999a: ac 3f 0d    .?.
    cpy #&82                                                          ; 999d: c0 82       ..
    beq c99a4                                                         ; 999f: f0 03       ..
    jmp c9ae7                                                         ; 99a1: 4c e7 9a    L..

; &99a4 referenced 3 times by &9998, &999f, &9a16
.c99a4
    jsr sub_c994e                                                     ; 99a4: 20 4e 99     N.
    bne c99bb                                                         ; 99a7: d0 12       ..
    lda port_buf_len                                                  ; 99a9: a5 a2       ..
    clc                                                               ; 99ab: 18          .
    adc open_port_buf                                                 ; 99ac: 65 a4       e.
    bcc c99b2                                                         ; 99ae: 90 02       ..
    inc open_port_buf_hi                                              ; 99b0: e6 a5       ..
; &99b2 referenced 1 time by &99ae
.c99b2
    ldy #8                                                            ; 99b2: a0 08       ..
    sta (port_ws_offset),y                                            ; 99b4: 91 a6       ..
    iny                                                               ; 99b6: c8          .              ; Y=&09
    lda open_port_buf_hi                                              ; 99b7: a5 a5       ..
    sta (port_ws_offset),y                                            ; 99b9: 91 a6       ..
; &99bb referenced 1 time by &99a7
.c99bb
    lda rx_port                                                       ; 99bb: ad 40 0d    .@.
    beq discard_reset_listen                                          ; 99be: f0 1b       ..
    lda rx_src_net                                                    ; 99c0: ad 3e 0d    .>.
    ldy #3                                                            ; 99c3: a0 03       ..
    sta (port_ws_offset),y                                            ; 99c5: 91 a6       ..
    dey                                                               ; 99c7: 88          .              ; Y=&02
    lda rx_src_stn                                                    ; 99c8: ad 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 99cb: 91 a6       ..
    dey                                                               ; 99cd: 88          .              ; Y=&01
    lda rx_port                                                       ; 99ce: ad 40 0d    .@.
    sta (port_ws_offset),y                                            ; 99d1: 91 a6       ..
    dey                                                               ; 99d3: 88          .              ; Y=&00
    lda rx_ctrl                                                       ; 99d4: ad 3f 0d    .?.
    ora #&80                                                          ; 99d7: 09 80       ..
    sta (port_ws_offset),y                                            ; 99d9: 91 a6       ..
; ***************************************************************************************
; Discard with Tube release
; 
; Conditionally releases the Tube co-processor before discarding.
; If tx_flags bit 1 is set (Tube transfer was active), calls
; sub_c9a2b to release the Tube claim, then falls through to
; discard_listen. The main teardown path for RX operations that
; used the Tube.
; ***************************************************************************************
; &99db referenced 4 times by &9840, &99be, &9e4d, &9eb7
.discard_reset_listen
    lda #2                                                            ; 99db: a9 02       ..             ; Tube flag bit 1 AND tx_flags bit 1
    and tube_flag                                                     ; 99dd: 2d 67 0d    -g.
    bit tx_flags                                                      ; 99e0: 2c 4a 0d    ,J.
    beq discard_listen                                                ; 99e3: f0 03       ..             ; No Tube transfer active -- skip release
    jsr sub_c9a2b                                                     ; 99e5: 20 2b 9a     +.            ; Release Tube claim before discarding
; ***************************************************************************************
; Discard frame and return to idle listen
; 
; Calls adlc_rx_listen to re-enter idle RX mode (CR1=&82, CR2=&67),
; then installs nmi_rx_scout (&96BF) as the NMI handler via
; set_nmi_vector. Returns to the caller's NMI context. Used as
; the common discard tail for both gentle rejection (wrong
; station/network) and error recovery paths.
; ***************************************************************************************
; &99e8 referenced 4 times by &970b, &99e3, &9a61, &9b1d
.discard_listen
    jsr adlc_rx_listen                                                ; 99e8: 20 4c 9f     L.
; &99eb referenced 2 times by &96ef, &9708
.c99eb
    lda #&bf                                                          ; 99eb: a9 bf       ..             ; Install nmi_rx_scout (&96BF) as NMI handler
    ldy #&96                                                          ; 99ed: a0 96       ..
    jmp set_nmi_vector                                                ; 99ef: 4c 0e 0d    L..

; &99f2 referenced 1 time by &97c8
.c99f2
    txa                                                               ; 99f2: 8a          .
    pha                                                               ; 99f3: 48          H
    ldx #4                                                            ; 99f4: a2 04       ..
    lda #2                                                            ; 99f6: a9 02       ..
; &99f8 referenced 1 time by &9a69
.c99f8
    bit tx_flags                                                      ; 99f8: 2c 4a 0d    ,J.
    bne c9a19                                                         ; 99fb: d0 1c       ..
    ldy port_buf_len                                                  ; 99fd: a4 a2       ..
; &99ff referenced 1 time by &9a12
.loop_c99ff
    lda rx_src_stn,x                                                  ; 99ff: bd 3d 0d    .=.
    sta (open_port_buf),y                                             ; 9a02: 91 a4       ..
    iny                                                               ; 9a04: c8          .
    bne c9a0d                                                         ; 9a05: d0 06       ..
    inc open_port_buf_hi                                              ; 9a07: e6 a5       ..
    dec port_buf_len_hi                                               ; 9a09: c6 a3       ..
    beq c9a6e                                                         ; 9a0b: f0 61       .a
; &9a0d referenced 1 time by &9a05
.c9a0d
    inx                                                               ; 9a0d: e8          .
    sty port_buf_len                                                  ; 9a0e: 84 a2       ..
    cpx #&0c                                                          ; 9a10: e0 0c       ..
    bne loop_c99ff                                                    ; 9a12: d0 eb       ..
; &9a14 referenced 2 times by &9a29, &9a72
.c9a14
    pla                                                               ; 9a14: 68          h
    tax                                                               ; 9a15: aa          .
    jmp c99a4                                                         ; 9a16: 4c a4 99    L..

; &9a19 referenced 2 times by &99fb, &9a27
.c9a19
    lda rx_src_stn,x                                                  ; 9a19: bd 3d 0d    .=.
    sta tube_data_register_3                                          ; 9a1c: 8d e5 fe    ...
    jsr sub_c9a37                                                     ; 9a1f: 20 37 9a     7.
    beq c9a70                                                         ; 9a22: f0 4c       .L
    inx                                                               ; 9a24: e8          .
    cpx #&0c                                                          ; 9a25: e0 0c       ..
    bne c9a19                                                         ; 9a27: d0 f0       ..
    beq c9a14                                                         ; 9a29: f0 e9       ..             ; ALWAYS branch

; &9a2b referenced 2 times by &99e5, &9f12
.sub_c9a2b
    bit need_release_tube                                             ; 9a2b: 24 98       $.
    bmi c9a34                                                         ; 9a2d: 30 05       0.
    lda #&82                                                          ; 9a2f: a9 82       ..
    jsr tube_addr_claim                                               ; 9a31: 20 06 04     ..
; &9a34 referenced 1 time by &9a2d
.c9a34
    lsr need_release_tube                                             ; 9a34: 46 98       F.
    rts                                                               ; 9a36: 60          `

; &9a37 referenced 3 times by &98a8, &98b6, &9a1f
.sub_c9a37
    inc port_buf_len                                                  ; 9a37: e6 a2       ..
    bne return_inc_port_buf                                           ; 9a39: d0 0a       ..
    inc port_buf_len_hi                                               ; 9a3b: e6 a3       ..
    bne return_inc_port_buf                                           ; 9a3d: d0 06       ..
    inc open_port_buf                                                 ; 9a3f: e6 a4       ..
    bne return_inc_port_buf                                           ; 9a41: d0 02       ..
    inc open_port_buf_hi                                              ; 9a43: e6 a5       ..
; &9a45 referenced 3 times by &9a39, &9a3d, &9a41
.return_inc_port_buf
    rts                                                               ; 9a45: 60          `

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
; Discard with immediate operation dispatch
; 
; Co-located with immediate_op. After the scout ACK is sent for a
; port-0 frame, this entry dispatches on the control byte via the
; jump table at c99f8. Also reached as a discard path when the
; immediate operation is not permitted by the protection mask.
; ***************************************************************************************
; &9a46 referenced 1 time by &975e
.immediate_op
.discard_after_reset
    ldy rx_ctrl                                                       ; 9a46: ac 3f 0d    .?.            ; Control byte &81-&88 range check
    cpy #&81                                                          ; 9a49: c0 81       ..
    bcc c9a76                                                         ; 9a4b: 90 29       .)
    cpy #&89                                                          ; 9a4d: c0 89       ..
    bcs c9a76                                                         ; 9a4f: b0 25       .%
    cpy #&87                                                          ; 9a51: c0 87       ..
    bcs c9a63                                                         ; 9a53: b0 0e       ..
    tya                                                               ; 9a55: 98          .              ; Convert ctrl byte to 0-based index for mask
    sec                                                               ; 9a56: 38          8
    sbc #&81                                                          ; 9a57: e9 81       ..
    tay                                                               ; 9a59: a8          .
    lda prot_status                                                   ; 9a5a: ad 63 0d    .c.            ; Load protection mask from LSTAT
; &9a5d referenced 1 time by &9a5f
.loop_c9a5d
    ror a                                                             ; 9a5d: 6a          j              ; Rotate mask right by control byte index
    dey                                                               ; 9a5e: 88          .
    bpl loop_c9a5d                                                    ; 9a5f: 10 fc       ..
    bcs discard_listen                                                ; 9a61: b0 85       ..             ; Bit set = operation disabled, discard
; &9a63 referenced 1 time by &9a53
.c9a63
    ldy rx_ctrl                                                       ; 9a63: ac 3f 0d    .?.
    lda #&9a                                                          ; 9a66: a9 9a       ..             ; PHA hi byte / PHA lo byte / RTS dispatch
    pha                                                               ; 9a68: 48          H
    lda c99f8,y                                                       ; 9a69: b9 f8 99    ...
    pha                                                               ; 9a6c: 48          H
    rts                                                               ; 9a6d: 60          `

; &9a6e referenced 1 time by &9a0b
.c9a6e
    inc port_buf_len                                                  ; 9a6e: e6 a2       ..
; &9a70 referenced 1 time by &9a22
.c9a70
    cpx #&0b                                                          ; 9a70: e0 0b       ..
    beq c9a14                                                         ; 9a72: f0 a0       ..
    pla                                                               ; 9a74: 68          h
    tax                                                               ; 9a75: aa          .
; &9a76 referenced 2 times by &9a4b, &9a4f
.c9a76
    jmp c9835                                                         ; 9a76: 4c 35 98    L5.

    equb &bb, &9e, &80, &80, &80, &d5, &d5                            ; 9a79: bb 9e 80... ...
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
    equb &a9, &a9,   0, &85, &a4, &a9, &82, &85, &a2, &a9,   1, &85   ; 9a80: a9 a9 00... ...
    equb &a3, &a5, &9d, &85, &a5, &a0,   3, &b9, &41, &0d, &99, &58   ; 9a8c: a3 a5 9d... ...
    equb &0d, &88, &10, &f7, &4c                                      ; 9a98: 0d 88 10... ...
; &9a9d referenced 1 time by &9675
.l9a9d
    equb &cb, &97                                                     ; 9a9d: cb 97       ..
; ***************************************************************************************
; RX immediate: POKE setup
; 
; Sets up workspace offsets for receiving POKE data.
; port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
; the common data-receive path at c9805.
; ***************************************************************************************
.rx_imm_poke
    equb &a9, &3d, &85, &a6, &a9, &0d, &85, &a7, &4c, &b9, &97        ; 9a9f: a9 3d 85... .=.
; ***************************************************************************************
; RX immediate: machine type query
; 
; Sets up a buffer at &7F21 (length #&01FC) for the machine
; type query response, then jumps to the query handler at
; c9b0f. Returns system identification data to the remote
; station.
; ***************************************************************************************
.rx_imm_machine_type
    equb &a9,   1, &85, &a3, &a9, &fc, &85, &a2, &a9, &25, &85, &a4   ; 9aaa: a9 01 85... ...
    equb &a9, &7f, &85, &a5, &d0, &12                                 ; 9ab6: a9 7f 85... ...
; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Writes &0D3D to port_ws_offset/rx_buf_offset, sets
; scout_status=2, then calls tx_calc_transfer to send the
; PEEK response data back to the requesting station.
; Rewritten in 3.40 to use workspace offsets (&A6/&A7)
; instead of saving/restoring nmi_tx_block (&A0/&A1).
; ***************************************************************************************
.rx_imm_peek
    equb &a9, &3d, &85, &a6, &a9, &0d, &85, &a7, &a9,   2, &8d, &5c   ; 9abc: a9 3d 85... .=.
    equb &0d, &20, &ca, &9e, &90, &4f, &ad, &4a, &0d,   9, &80, &8d   ; 9ac8: 0d 20 ca... . .
    equb &4a, &0d, &a9, &44, &8d, &a0, &fe, &a9, &a7, &8d, &a1, &fe   ; 9ad4: 4a 0d a9... J..
    equb &a9, &fd, &a0, &9a, &4c,   7, &99                            ; 9ae0: a9 fd a0... ...

; &9ae7 referenced 1 time by &99a1
.c9ae7
    lda port_buf_len                                                  ; 9ae7: a5 a2       ..
    clc                                                               ; 9ae9: 18          .
    adc #&80                                                          ; 9aea: 69 80       i.
    ldy #&7f                                                          ; 9aec: a0 7f       ..
    sta (net_rx_ptr),y                                                ; 9aee: 91 9c       ..
    ldy #&80                                                          ; 9af0: a0 80       ..
    lda rx_src_stn                                                    ; 9af2: ad 3d 0d    .=.
    sta (net_rx_ptr),y                                                ; 9af5: 91 9c       ..
    iny                                                               ; 9af7: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9af8: ad 3e 0d    .>.
    sta (net_rx_ptr),y                                                ; 9afb: 91 9c       ..
    lda rx_ctrl                                                       ; 9afd: ad 3f 0d    .?.
    sta tx_work_57                                                    ; 9b00: 8d 57 0d    .W.
    lda #&84                                                          ; 9b03: a9 84       ..
    sta system_via_ier                                                ; 9b05: 8d 4e fe    .N.
    lda system_via_acr                                                ; 9b08: ad 4b fe    .K.
    and #&1c                                                          ; 9b0b: 29 1c       ).
    sta tx_work_51                                                    ; 9b0d: 8d 51 0d    .Q.
    lda system_via_acr                                                ; 9b10: ad 4b fe    .K.
    and #&e3                                                          ; 9b13: 29 e3       ).
    ora #8                                                            ; 9b15: 09 08       ..
    sta system_via_acr                                                ; 9b17: 8d 4b fe    .K.
    bit system_via_sr                                                 ; 9b1a: 2c 4a fe    ,J.
    jmp discard_listen                                                ; 9b1d: 4c e8 99    L..

    equs "$-;G^"                                                      ; 9b20: 24 2d 3b... $-;
; ***************************************************************************************
; TX done: remote JSR execution
; 
; Pushes address &9BEB on the stack (so RTS returns to
; tx_done_exit), then does JMP (l0d58) to call the remote
; JSR target routine. When that routine returns via RTS,
; control resumes at tx_done_exit.
; ***************************************************************************************
.tx_done_jsr
    equb &a9, &9b, &48, &a9                                           ; 9b25: a9 9b 48... ..H
    equs "fHlX"                                                       ; 9b29: 66 48 6c... fHl
    equb &0d                                                          ; 9b2d: 0d          .
; ***************************************************************************************
; TX done: UserProc event
; 
; Generates a network event (event 8) via OSEVEN with
; X=l0d58, A=l0d59 (the remote address). This notifies
; the user program that a UserProc operation has completed.
; ***************************************************************************************
.tx_done_user_proc
    equb &a0,   8, &ae, &58, &0d, &ad, &59, &0d, &20, &bf, &ff, &4c   ; 9b2e: a0 08 ae... ...
    equb &67, &9b                                                     ; 9b3a: 67 9b       g.
; ***************************************************************************************
; TX done: OSProc call
; 
; Calls the ROM entry point at &8000 (rom_header) with
; X=l0d58, Y=l0d59. This invokes an OS-level procedure
; on behalf of the remote station.
; ***************************************************************************************
.tx_done_os_proc
    equb &ae, &58, &0d, &ac, &59, &0d, &20, 0, &80, &4c, &67, &9b     ; 9b3c: ae 58 0d... .X.
; ***************************************************************************************
; TX done: HALT
; 
; Sets bit 2 of rx_flags (&0D64), enables interrupts, and
; spin-waits until bit 2 is cleared (by a CONTINUE from the
; remote station). If bit 2 is already set, skips to exit.
; ***************************************************************************************
.tx_done_halt
    equb &a9,   4, &2c, &64, &0d, &d0, &18, &0d, &64, &0d, &8d, &64   ; 9b48: a9 04 2c... ..,
    equb &0d, &a9,   4                                                ; 9b54: 0d a9 04    ...
    equs "X,d"                                                        ; 9b57: 58 2c 64    X,d
    equb &0d, &d0, &fb, &f0, 8                                        ; 9b5a: 0d d0 fb... ...
; ***************************************************************************************
; TX done: CONTINUE
; 
; Clears bit 2 of rx_flags (&0D64), releasing any station
; that is halted and spinning in tx_done_halt.
; ***************************************************************************************
.tx_done_continue
    equb &ad, &64, &0d, &29, &fb, &8d, &64, &0d                       ; 9b5f: ad 64 0d... .d.
.tx_done_exit
    equb &68, &a8, &68, &aa, &a9, 0, &60                              ; 9b67: 68 a8 68... h.h

; &9b6e referenced 1 time by &06ce[4]
.c9b6e
    txa                                                               ; 9b6e: 8a          .
    pha                                                               ; 9b6f: 48          H
    ldy #2                                                            ; 9b70: a0 02       ..
    lda (nmi_tx_block),y                                              ; 9b72: b1 a0       ..
    sta tx_dst_stn                                                    ; 9b74: 8d 20 0d    . .
    iny                                                               ; 9b77: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9b78: b1 a0       ..
    sta tx_dst_net                                                    ; 9b7a: 8d 21 0d    .!.
    ldy #0                                                            ; 9b7d: a0 00       ..
    lda (nmi_tx_block),y                                              ; 9b7f: b1 a0       ..
    bmi c9b86                                                         ; 9b81: 30 03       0.
    jmp tx_active_start                                               ; 9b83: 4c 11 9c    L..

; &9b86 referenced 1 time by &9b81
.c9b86
    sta tx_ctrl_byte                                                  ; 9b86: 8d 24 0d    .$.
    tax                                                               ; 9b89: aa          .
    iny                                                               ; 9b8a: c8          .
    lda (nmi_tx_block),y                                              ; 9b8b: b1 a0       ..
    sta tx_port                                                       ; 9b8d: 8d 25 0d    .%.
    bne c9bc5                                                         ; 9b90: d0 33       .3
    cpx #&83                                                          ; 9b92: e0 83       ..
    bcs c9bb1                                                         ; 9b94: b0 1b       ..
    sec                                                               ; 9b96: 38          8
    php                                                               ; 9b97: 08          .
    ldy #8                                                            ; 9b98: a0 08       ..
; &9b9a referenced 1 time by &9bae
.loop_c9b9a
    lda (nmi_tx_block),y                                              ; 9b9a: b1 a0       ..
    dey                                                               ; 9b9c: 88          .
    dey                                                               ; 9b9d: 88          .
    dey                                                               ; 9b9e: 88          .
    dey                                                               ; 9b9f: 88          .
    plp                                                               ; 9ba0: 28          (
    sbc (nmi_tx_block),y                                              ; 9ba1: f1 a0       ..
    sta tx_data_start,y                                               ; 9ba3: 99 26 0d    .&.
    iny                                                               ; 9ba6: c8          .
    iny                                                               ; 9ba7: c8          .
    iny                                                               ; 9ba8: c8          .
    iny                                                               ; 9ba9: c8          .
    iny                                                               ; 9baa: c8          .
    php                                                               ; 9bab: 08          .
    cpy #&0c                                                          ; 9bac: c0 0c       ..
    bcc loop_c9b9a                                                    ; 9bae: 90 ea       ..
    plp                                                               ; 9bb0: 28          (
; &9bb1 referenced 1 time by &9b94
.c9bb1
    cpx #&81                                                          ; 9bb1: e0 81       ..
    bcc tx_active_start                                               ; 9bb3: 90 5c       .\
    cpx #&89                                                          ; 9bb5: e0 89       ..
    bcs tx_active_start                                               ; 9bb7: b0 58       .X
    ldy #&0c                                                          ; 9bb9: a0 0c       ..
; &9bbb referenced 1 time by &9bc3
.loop_c9bbb
    lda (nmi_tx_block),y                                              ; 9bbb: b1 a0       ..
    sta nmi_shim_1a,y                                                 ; 9bbd: 99 1a 0d    ...
    iny                                                               ; 9bc0: c8          .
    cpy #&10                                                          ; 9bc1: c0 10       ..
    bcc loop_c9bbb                                                    ; 9bc3: 90 f6       ..
; &9bc5 referenced 1 time by &9b90
.c9bc5
    lda #&20 ; ' '                                                    ; 9bc5: a9 20       .
    bit econet_control23_or_status2                                   ; 9bc7: 2c a1 fe    ,..
    bne c9c21                                                         ; 9bca: d0 55       .U
    lda #&fd                                                          ; 9bcc: a9 fd       ..
    pha                                                               ; 9bce: 48          H
    lda #6                                                            ; 9bcf: a9 06       ..
    sta tx_length                                                     ; 9bd1: 8d 50 0d    .P.
    lda #0                                                            ; 9bd4: a9 00       ..
; ***************************************************************************************
; INACTIVE polling loop
; 
; Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
; attempting transmission. Uses a 3-byte timeout counter on the stack.
; The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
; never appears.
; The CTS check at &9BF4-&9BF9 works because CR2=&67 has RTS=0, so
; cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.
; ***************************************************************************************
.inactive_poll
    sta tx_index                                                      ; 9bd6: 8d 4f 0d    .O.
    pha                                                               ; 9bd9: 48          H
    pha                                                               ; 9bda: 48          H
    ldy #&e7                                                          ; 9bdb: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9bdd referenced 3 times by &9c03, &9c08, &9c0d
.c9bdd
    lda #4                                                            ; 9bdd: a9 04       ..             ; A=&04: INACTIVE mask for SR2 bit2
    php                                                               ; 9bdf: 08          .
    sei                                                               ; 9be0: 78          x
.sub_c9be1
l9be2 = sub_c9be1+1
    bit station_id_disable_net_nmis                                   ; 9be1: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
; &9be2 referenced 1 time by &9c5e
    bit station_id_disable_net_nmis                                   ; 9be4: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
    bit econet_control23_or_status2                                   ; 9be7: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
    beq c9bfb                                                         ; 9bea: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9bec: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9bef: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9bf1: 8d a1 fe    ...
    lda #&10                                                          ; 9bf4: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9bf6: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9bf9: d0 34       .4             ; CTS set -- clock hardware detected, start TX
; &9bfb referenced 1 time by &9bea
.c9bfb
    bit video_ula_control                                             ; 9bfb: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 9bfe: 28          (
    tsx                                                               ; 9bff: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c00: fe 01 01    ...
    bne c9bdd                                                         ; 9c03: d0 d8       ..
    inc l0102,x                                                       ; 9c05: fe 02 01    ...
    bne c9bdd                                                         ; 9c08: d0 d3       ..
    inc l0103,x                                                       ; 9c0a: fe 03 01    ...
    bne c9bdd                                                         ; 9c0d: d0 ce       ..
    beq tx_line_jammed                                                ; 9c0f: f0 04       ..             ; ALWAYS branch

; TX_ACTIVE branch (A=&44 = CR1 value for TX active)
; &9c11 referenced 3 times by &9b83, &9bb3, &9bb7
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c11: a9 44       .D
    bne c9c23                                                         ; 9c13: d0 0e       ..             ; ALWAYS branch

; ***************************************************************************************
; TX timeout error handler (Line Jammed)
; 
; Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
; timeout loop's state), then stores error code &40 ("Line
; Jammed") into the TX control block and signals completion.
; ***************************************************************************************
; &9c15 referenced 1 time by &9c0f
.tx_line_jammed
    lda #7                                                            ; 9c15: a9 07       ..             ; CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 9c17: 8d a1 fe    ...
    pla                                                               ; 9c1a: 68          h
    pla                                                               ; 9c1b: 68          h
    pla                                                               ; 9c1c: 68          h
    lda #&40 ; '@'                                                    ; 9c1d: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne c9c23                                                         ; 9c1f: d0 02       ..             ; ALWAYS branch

; &9c21 referenced 1 time by &9bca
.c9c21
    lda #&43 ; 'C'                                                    ; 9c21: a9 43       .C
; &9c23 referenced 2 times by &9c13, &9c1f
.c9c23
    ldy #0                                                            ; 9c23: a0 00       ..
    sta (nmi_tx_block),y                                              ; 9c25: 91 a0       ..
    lda #&80                                                          ; 9c27: a9 80       ..
    sta tx_clear_flag                                                 ; 9c29: 8d 62 0d    .b.
    pla                                                               ; 9c2c: 68          h
    tax                                                               ; 9c2d: aa          .
    rts                                                               ; 9c2e: 60          `

; ***************************************************************************************
; TX preparation
; 
; Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
; installs NMI TX handler at &9CCC (nmi_tx_data), and re-enables NMIs.
; For port-0 (immediate) operations, dispatches via a lookup table indexed
; by control byte to set tx_flags, tx_length, and a per-operation handler.
; For port non-zero, branches to c9c8e for standard data transfer setup.
; ***************************************************************************************
; &9c2f referenced 1 time by &9bf9
.tx_prepare
    sty econet_control23_or_status2                                   ; 9c2f: 8c a1 fe    ...            ; Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 9c32: a2 44       .D             ; CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 9c34: 8e a0 fe    ...
    ldx #&cc                                                          ; 9c37: a2 cc       ..             ; Install NMI handler at &9CCC (nmi_tx_data)
    ldy #&9c                                                          ; 9c39: a0 9c       ..
    stx nmi_jmp_lo                                                    ; 9c3b: 8e 0c 0d    ...
    sty nmi_jmp_hi                                                    ; 9c3e: 8c 0d 0d    ...
    sec                                                               ; 9c41: 38          8              ; Set need_release_tube flag (SEC/ROR = bit7)
    ror need_release_tube                                             ; 9c42: 66 98       f.
    bit video_ula_control                                             ; 9c44: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 9c47: ad 25 0d    .%.
    bne c9c8e                                                         ; 9c4a: d0 42       .B
    ldy tx_ctrl_byte                                                  ; 9c4c: ac 24 0d    .$.
    lda l9e41,y                                                       ; 9c4f: b9 41 9e    .A.
    sta tx_flags                                                      ; 9c52: 8d 4a 0d    .J.
    lda l9e39,y                                                       ; 9c55: b9 39 9e    .9.
    sta tx_length                                                     ; 9c58: 8d 50 0d    .P.
    lda #&9c                                                          ; 9c5b: a9 9c       ..
    pha                                                               ; 9c5d: 48          H
    lda l9be2,y                                                       ; 9c5e: b9 e2 9b    ...
    pha                                                               ; 9c61: 48          H
    rts                                                               ; 9c62: 60          `

    equb &6e, &72, &b4, &b4, &b4, &c4, &c4, &6a, &a9, 3, &d0, &48     ; 9c63: 6e 72 b4... nr.
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
    equb &a9, 3, &d0, 2                                               ; 9c6f: a9 03 d0... ...
; ***************************************************************************************
; TX ctrl: POKE transfer setup
; 
; Sets scout_status=2 and shares the 4-byte addition and
; transfer calculation path with tx_ctrl_peek.
; ***************************************************************************************
.tx_ctrl_poke
    equb &a9,   2, &8d, &5c, &0d, &18,   8, &a0, &0c, &b9, &1e, &0d   ; 9c73: a9 02 8d... ...
    equb &28, &71, &a0, &99, &1e, &0d, &c8,   8                       ; 9c7f: 28 71 a0... (q.
; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_proc
    equb &c0, &10, &90, &f1, &28, &d0, &2c                            ; 9c87: c0 10 90... ...

; &9c8e referenced 1 time by &9c4a
.c9c8e
    lda tx_dst_stn                                                    ; 9c8e: ad 20 0d    . .
    and tx_dst_net                                                    ; 9c91: 2d 21 0d    -!.
    cmp #&ff                                                          ; 9c94: c9 ff       ..
    bne c9cb0                                                         ; 9c96: d0 18       ..
    lda #&0e                                                          ; 9c98: a9 0e       ..
    sta tx_length                                                     ; 9c9a: 8d 50 0d    .P.
    lda #&40 ; '@'                                                    ; 9c9d: a9 40       .@
    sta tx_flags                                                      ; 9c9f: 8d 4a 0d    .J.
    ldy #4                                                            ; 9ca2: a0 04       ..
; &9ca4 referenced 1 time by &9cac
.loop_c9ca4
    lda (nmi_tx_block),y                                              ; 9ca4: b1 a0       ..
    sta tx_src_stn,y                                                  ; 9ca6: 99 22 0d    .".
    iny                                                               ; 9ca9: c8          .
    cpy #&0c                                                          ; 9caa: c0 0c       ..
    bcc loop_c9ca4                                                    ; 9cac: 90 f6       ..
    bcs tx_ctrl_exit                                                  ; 9cae: b0 15       ..             ; ALWAYS branch

; &9cb0 referenced 1 time by &9c96
.c9cb0
    lda #0                                                            ; 9cb0: a9 00       ..
    sta tx_flags                                                      ; 9cb2: 8d 4a 0d    .J.
    lda #2                                                            ; 9cb5: a9 02       ..
    sta scout_status                                                  ; 9cb7: 8d 5c 0d    .\.
    lda nmi_tx_block                                                  ; 9cba: a5 a0       ..
    sta port_ws_offset                                                ; 9cbc: 85 a6       ..
    lda nmi_tx_block_hi                                               ; 9cbe: a5 a1       ..
    sta rx_buf_offset                                                 ; 9cc0: 85 a7       ..
    jsr tx_calc_transfer                                              ; 9cc2: 20 ca 9e     ..
; &9cc5 referenced 1 time by &9cae
.tx_ctrl_exit
    plp                                                               ; 9cc5: 28          (
    pla                                                               ; 9cc6: 68          h
    pla                                                               ; 9cc7: 68          h
    pla                                                               ; 9cc8: 68          h
    pla                                                               ; 9cc9: 68          h
    tax                                                               ; 9cca: aa          .
    rts                                                               ; 9ccb: 60          `

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
    ldy tx_index                                                      ; 9ccc: ac 4f 0d    .O.            ; Load TX buffer index
    bit econet_control1_or_status1                                    ; 9ccf: 2c a0 fe    ,..            ; BIT SR1: V=bit6(TDRA), N=bit7(IRQ)
; &9cd2 referenced 1 time by &9ced
.loop_c9cd2
    bvc c9cf6                                                         ; 9cd2: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9cd4: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9cd7: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9cda: c8          .
    lda tx_dst_stn,y                                                  ; 9cdb: b9 20 0d    . .
    iny                                                               ; 9cde: c8          .
    sty tx_index                                                      ; 9cdf: 8c 4f 0d    .O.
    sta econet_data_continue_frame                                    ; 9ce2: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9ce5: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9ce8: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9cea: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi loop_c9cd2                                                    ; 9ced: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9cef: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9cf2 referenced 1 time by &9d35
.tx_error
    lda #&42 ; 'B'                                                    ; 9cf2: a9 42       .B             ; Error &42
    bne c9cfd                                                         ; 9cf4: d0 07       ..             ; ALWAYS branch

; &9cf6 referenced 1 time by &9cd2
.c9cf6
    lda #&67 ; 'g'                                                    ; 9cf6: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9cf8: 8d a1 fe    ...
    lda #&41 ; 'A'                                                    ; 9cfb: a9 41       .A             ; Error &41 (TDRA not ready)
; &9cfd referenced 1 time by &9cf4
.c9cfd
    ldy station_id_disable_net_nmis                                   ; 9cfd: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d00 referenced 1 time by &9d03
.loop_c9d00
    pha                                                               ; 9d00: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d01: 68          h
    iny                                                               ; 9d02: c8          .
    bne loop_c9d00                                                    ; 9d03: d0 fb       ..
    jmp tx_store_result                                               ; 9d05: 4c ae 9e    L..

; ***************************************************************************************
; TX_LAST_DATA and frame completion
; 
; Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
; the TX completion NMI handler at &9D14 (nmi_tx_complete).
; CR2=&3F = 0011_1111:
;   bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
;   bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
;   bit3: FLAG_IDLE -- send flags/idle after frame
;   bit2: FC_TDRA -- force clear TDRA
;   bit1: 2_1_BYTE -- two-byte transfer mode
;   bit0: PSE -- prioritised status enable
; Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)
; ***************************************************************************************
; &9d08 referenced 1 time by &9ce8
.tx_last_data
    lda #&3f ; '?'                                                    ; 9d08: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 9d0a: 8d a1 fe    ...
    lda #&14                                                          ; 9d0d: a9 14       ..             ; Install NMI handler at &9D14 (nmi_tx_complete)
    ldy #&9d                                                          ; 9d0f: a0 9d       ..
    jmp set_nmi_vector                                                ; 9d11: 4c 0e 0d    L..

; ***************************************************************************************
; TX completion: switch to RX mode
; 
; Called via NMI after the frame (including CRC and closing flag) has been
; fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
; CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
; Checks workspace flags to decide next action:
;   - bit6 set at &0D4A -> tx_result_ok at &9EA8
;   - bit0 set at &0D4A -> handshake_await_ack at &9E50
;   - Otherwise -> install nmi_reply_scout at &9D30
; ***************************************************************************************
.nmi_tx_complete
    lda #&82                                                          ; 9d14: a9 82       ..             ; CR1=&82: TX_RESET | RIE (now in RX mode)
    sta econet_control1_or_status1                                    ; 9d16: 8d a0 fe    ...
    bit tx_flags                                                      ; 9d19: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc c9d21                                                         ; 9d1c: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9d1e: 4c a8 9e    L..            ; bit6 set -- TX completion

; &9d21 referenced 1 time by &9d1c
.c9d21
    lda #1                                                            ; 9d21: a9 01       ..
    bit tx_flags                                                      ; 9d23: 2c 4a 0d    ,J.
    beq c9d2b                                                         ; 9d26: f0 03       ..
    jmp handshake_await_ack                                           ; 9d28: 4c 50 9e    LP.            ; bit0 set -- four-way handshake data phase

; &9d2b referenced 1 time by &9d26
.c9d2b
    lda #&30 ; '0'                                                    ; 9d2b: a9 30       .0             ; Install nmi_reply_scout at &9D30
    jmp l0d11                                                         ; 9d2d: 4c 11 0d    L..

; ***************************************************************************************
; RX reply scout handler
; 
; Handles reception of the reply scout frame after transmission.
; Checks SR2 bit0 (AP) for incoming data, reads the first byte
; (destination station) and compares to our station ID via &FE18
; (which also disables NMIs as a side effect).
; ***************************************************************************************
.nmi_reply_scout
    lda #1                                                            ; 9d30: a9 01       ..             ; A=&01: AP mask for SR2
    bit econet_control23_or_status2                                   ; 9d32: 2c a1 fe    ,..            ; BIT SR2: test AP (Address Present)
    beq tx_error                                                      ; 9d35: f0 bb       ..             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9d37: ad a2 fe    ...            ; Read first RX byte (destination station)
    cmp station_id_disable_net_nmis                                   ; 9d3a: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne c9d58                                                         ; 9d3d: d0 19       ..             ; Not our station -- error/reject
    lda #&44 ; 'D'                                                    ; 9d3f: a9 44       .D             ; Install nmi_reply_cont at &9D44
    jmp l0d11                                                         ; 9d41: 4c 11 0d    L..

; ***************************************************************************************
; RX reply continuation handler
; 
; Reads the second byte of the reply scout (destination network) and
; validates it is zero (local network). Installs nmi_reply_validate
; (&9D5B) for the remaining two bytes (source station and network).
; Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9D53.
; If IRQ is still set, falls through directly to &9D5B without an RTI,
; avoiding NMI re-entry overhead for short frames where all bytes arrive
; in quick succession.
; ***************************************************************************************
.nmi_reply_cont
    bit econet_control23_or_status2                                   ; 9d44: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl c9d58                                                         ; 9d47: 10 0f       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9d49: ad a2 fe    ...            ; Read destination network byte
    bne c9d58                                                         ; 9d4c: d0 0a       ..             ; Non-zero -- network mismatch, error
    lda #&5b ; '['                                                    ; 9d4e: a9 5b       .[             ; Install nmi_reply_validate at &9D5B
    bit econet_control1_or_status1                                    ; 9d50: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9d53: 30 06       0.             ; IRQ set -- fall through to &9D5B without RTI
    jmp l0d11                                                         ; 9d55: 4c 11 0d    L..            ; IRQ not set -- install handler and RTI

; &9d58 referenced 7 times by &9d3d, &9d47, &9d4c, &9d5e, &9d66, &9d6e, &9d75
.c9d58
    jmp tx_result_fail                                                ; 9d58: 4c ac 9e    L..

; ***************************************************************************************
; RX reply validation (Path 2 for FV/PSE interaction)
; 
; Reads the source station and source network from the reply scout and
; validates them against the original TX destination (&0D20/&0D21).
; Sequence:
;   1. Check SR2 bit7 (RDA) at &9D5B -- must see data available
;   2. Read source station at &9D60, compare to &0D20 (tx_dst_stn)
;   3. Read source network at &9D68, compare to &0D21 (tx_dst_net)
;   4. Check SR2 bit1 (FV) at &9D72 -- must see frame complete
; If all checks pass, the reply scout is valid and the ROM proceeds
; to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).
; ***************************************************************************************
; &9d5b referenced 1 time by &9d53
.nmi_reply_validate
    bit econet_control23_or_status2                                   ; 9d5b: 2c a1 fe    ,..            ; BIT SR2: test RDA (bit7). Must be set for valid reply.
    bpl c9d58                                                         ; 9d5e: 10 f8       ..             ; No RDA -- error (FV masking RDA via PSE would cause this)
    lda econet_data_continue_frame                                    ; 9d60: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9d63: cd 20 0d    . .            ; Compare to original TX destination station (&0D20)
    bne c9d58                                                         ; 9d66: d0 f0       ..             ; Mismatch -- not the expected reply, error
    lda econet_data_continue_frame                                    ; 9d68: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9d6b: cd 21 0d    .!.            ; Compare to original TX destination network (&0D21)
    bne c9d58                                                         ; 9d6e: d0 e8       ..             ; Mismatch -- error
    lda #2                                                            ; 9d70: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9d72: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq c9d58                                                         ; 9d75: f0 e1       ..             ; No FV -- incomplete frame, error
    lda #&a7                                                          ; 9d77: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)
    sta econet_control23_or_status2                                   ; 9d79: 8d a1 fe    ...
    lda #&44 ; 'D'                                                    ; 9d7c: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9d7e: 8d a0 fe    ...
    lda #&50 ; 'P'                                                    ; 9d81: a9 50       .P             ; Save handshake_await_ack (&9E50) in &0D4B/&0D4C
    ldy #&9e                                                          ; 9d83: a0 9e       ..
    sta nmi_next_lo                                                   ; 9d85: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9d88: 8c 4c 0d    .L.
    lda tx_dst_stn                                                    ; 9d8b: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9d8e: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc c9dcd                                                         ; 9d91: 50 3a       P:             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9d93: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9d96: ad 21 0d    .!.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9d99: 8d a2 fe    ...
    lda #&a3                                                          ; 9d9c: a9 a3       ..             ; Install nmi_scout_ack_src at &9DA3
    ldy #&9d                                                          ; 9d9e: a0 9d       ..
    jmp set_nmi_vector                                                ; 9da0: 4c 0e 0d    L..

; ***************************************************************************************
; TX scout ACK: write source address
; 
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9da3: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9da6: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc c9dcd                                                         ; 9da9: 50 22       P"             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9dab: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9dae: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9db0: 8d a2 fe    ...
; &9db3 referenced 1 time by &9948
.data_tx_begin
    lda #2                                                            ; 9db3: a9 02       ..
    bit tx_flags                                                      ; 9db5: 2c 4a 0d    ,J.
    bne c9dc1                                                         ; 9db8: d0 07       ..
    lda #&c8                                                          ; 9dba: a9 c8       ..
    ldy #&9d                                                          ; 9dbc: a0 9d       ..
    jmp set_nmi_vector                                                ; 9dbe: 4c 0e 0d    L..

; &9dc1 referenced 1 time by &9db8
.c9dc1
    lda #&0f                                                          ; 9dc1: a9 0f       ..
    ldy #&9e                                                          ; 9dc3: a0 9e       ..
    jmp set_nmi_vector                                                ; 9dc5: 4c 0e 0d    L..

; ***************************************************************************************
; TX data phase: send payload
; 
; Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
; Same pattern as the NMI TX handler at &9CCC but reads from the port
; buffer instead of the TX workspace. Writes two bytes per iteration,
; checking SR1 IRQ between pairs for tight looping.
; ***************************************************************************************
.nmi_data_tx
    ldy port_buf_len                                                  ; 9dc8: a4 a2       ..             ; Y = buffer offset, resume from last position
    bit econet_control1_or_status1                                    ; 9dca: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &9dcd referenced 3 times by &9d91, &9da9, &9df0
.c9dcd
    bvc c9e48                                                         ; 9dcd: 50 79       Py             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9dcf: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9dd1: 8d a2 fe    ...
    iny                                                               ; 9dd4: c8          .
    bne c9ddd                                                         ; 9dd5: d0 06       ..
    dec port_buf_len_hi                                               ; 9dd7: c6 a3       ..
    beq data_tx_last                                                  ; 9dd9: f0 1a       ..
    inc open_port_buf_hi                                              ; 9ddb: e6 a5       ..
; &9ddd referenced 1 time by &9dd5
.c9ddd
    lda (open_port_buf),y                                             ; 9ddd: b1 a4       ..
    sta econet_data_continue_frame                                    ; 9ddf: 8d a2 fe    ...
    iny                                                               ; 9de2: c8          .
    sty port_buf_len                                                  ; 9de3: 84 a2       ..
    bne c9ded                                                         ; 9de5: d0 06       ..
    dec port_buf_len_hi                                               ; 9de7: c6 a3       ..
    beq data_tx_last                                                  ; 9de9: f0 0a       ..
    inc open_port_buf_hi                                              ; 9deb: e6 a5       ..
; &9ded referenced 1 time by &9de5
.c9ded
    bit econet_control1_or_status1                                    ; 9ded: 2c a0 fe    ,..
    bmi c9dcd                                                         ; 9df0: 30 db       0.
    jmp nmi_rti                                                       ; 9df2: 4c 14 0d    L..

; &9df5 referenced 4 times by &9dd9, &9de9, &9e28, &9e3e
.data_tx_last
    lda #&3f ; '?'                                                    ; 9df5: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9df7: 8d a1 fe    ...
    lda tx_flags                                                      ; 9dfa: ad 4a 0d    .J.
    bpl data_tx_error                                                 ; 9dfd: 10 07       ..
    lda #&db                                                          ; 9dff: a9 db       ..
    ldy #&99                                                          ; 9e01: a0 99       ..
    jmp set_nmi_vector                                                ; 9e03: 4c 0e 0d    L..

; &9e06 referenced 1 time by &9dfd
.data_tx_error
.install_saved_handler
    lda nmi_next_lo                                                   ; 9e06: ad 4b 0d    .K.
    ldy nmi_next_hi                                                   ; 9e09: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 9e0c: 4c 0e 0d    L..

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9e0f: 2c a0 fe    ,..
; &9e12 referenced 1 time by &9e43
.c9e12
    bvc c9e48                                                         ; 9e12: 50 34       P4
    lda tube_data_register_3                                          ; 9e14: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9e17: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9e1a: e6 a2       ..
    bne c9e2a                                                         ; 9e1c: d0 0c       ..
    inc port_buf_len_hi                                               ; 9e1e: e6 a3       ..
    bne c9e2a                                                         ; 9e20: d0 08       ..
    inc open_port_buf                                                 ; 9e22: e6 a4       ..
    bne c9e2a                                                         ; 9e24: d0 04       ..
    inc open_port_buf_hi                                              ; 9e26: e6 a5       ..
    beq data_tx_last                                                  ; 9e28: f0 cb       ..
; &9e2a referenced 3 times by &9e1c, &9e20, &9e24
.c9e2a
    lda tube_data_register_3                                          ; 9e2a: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9e2d: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9e30: e6 a2       ..
    bne c9e40                                                         ; 9e32: d0 0c       ..
    inc port_buf_len_hi                                               ; 9e34: e6 a3       ..
    bne c9e40                                                         ; 9e36: d0 08       ..
.sub_c9e38
l9e39 = sub_c9e38+1
    inc open_port_buf                                                 ; 9e38: e6 a4       ..
; &9e39 referenced 1 time by &9c55
    bne c9e40                                                         ; 9e3a: d0 04       ..
    inc open_port_buf_hi                                              ; 9e3c: e6 a5       ..
    beq data_tx_last                                                  ; 9e3e: f0 b5       ..
; &9e40 referenced 3 times by &9e32, &9e36, &9e3a
.c9e40
l9e41 = c9e40+1
    bit econet_control1_or_status1                                    ; 9e40: 2c a0 fe    ,..
; &9e41 referenced 1 time by &9c4f
    bmi c9e12                                                         ; 9e43: 30 cd       0.
    jmp nmi_rti                                                       ; 9e45: 4c 14 0d    L..

; &9e48 referenced 2 times by &9dcd, &9e12
.c9e48
    lda tx_flags                                                      ; 9e48: ad 4a 0d    .J.
    bpl tx_result_fail                                                ; 9e4b: 10 5f       ._
    jmp discard_reset_listen                                          ; 9e4d: 4c db 99    L..

; ***************************************************************************************
; Four-way handshake: switch to RX for final ACK
; 
; After the data frame TX completes, switches to RX mode (CR1=&82)
; and installs &9EF8 to receive the final ACK from the remote station.
; ***************************************************************************************
; &9e50 referenced 1 time by &9d28
.handshake_await_ack
    lda #&82                                                          ; 9e50: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9e52: 8d a0 fe    ...
    lda #&5c ; '\'                                                    ; 9e55: a9 5c       .\             ; Install nmi_final_ack at &9E5C
    ldy #&9e                                                          ; 9e57: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e59: 4c 0e 0d    L..

; ***************************************************************************************
; RX final ACK handler
; 
; Receives the final ACK in a four-way handshake. Same validation
; pattern as the reply scout handler (&9D30-&9D5B):
;   &9E5C: Check AP, read dest_stn, compare to our station
;   &9E70: Check RDA, read dest_net, validate = 0
;   &9E84: Check RDA, read src_stn/net, compare to TX dest
;   &9EA3: Check FV for frame completion
; On success, stores result=0 at tx_result_ok. On failure, error &41.
; ***************************************************************************************
.nmi_final_ack
    lda #1                                                            ; 9e5c: a9 01       ..             ; A=&01: AP mask
    bit econet_control23_or_status2                                   ; 9e5e: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 9e61: f0 49       .I             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9e63: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 9e66: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 9e69: d0 41       .A             ; Not our station -- error
    lda #&70 ; 'p'                                                    ; 9e6b: a9 70       .p             ; Install nmi_final_ack_net at &9E70
    jmp l0d11                                                         ; 9e6d: 4c 11 0d    L..

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9e70: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9e73: 10 37       .7             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9e75: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9e78: d0 32       .2             ; Non-zero -- network mismatch, error
    lda #&84                                                          ; 9e7a: a9 84       ..             ; Install nmi_final_ack_validate at &9E84
    bit econet_control1_or_status1                                    ; 9e7c: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9e7f: 30 03       0.             ; IRQ set -- fall through to &9E84 without RTI
    jmp l0d11                                                         ; 9e81: 4c 11 0d    L..

; ***************************************************************************************
; Final ACK validation
; 
; Reads and validates src_stn and src_net against original TX dest.
; Then checks FV for frame completion.
; ***************************************************************************************
; &9e84 referenced 1 time by &9e7f
.nmi_final_ack_validate
    bit econet_control23_or_status2                                   ; 9e84: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9e87: 10 23       .#             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9e89: ad a2 fe    ...            ; Read source station
    cmp tx_dst_stn                                                    ; 9e8c: cd 20 0d    . .            ; Compare to TX dest station (&0D20)
    bne tx_result_fail                                                ; 9e8f: d0 1b       ..             ; Mismatch -- error
    lda econet_data_continue_frame                                    ; 9e91: ad a2 fe    ...            ; Read source network
    cmp tx_dst_net                                                    ; 9e94: cd 21 0d    .!.            ; Compare to TX dest network (&0D21)
    bne tx_result_fail                                                ; 9e97: d0 13       ..             ; Mismatch -- error
    lda tx_flags                                                      ; 9e99: ad 4a 0d    .J.
    bpl c9ea1                                                         ; 9e9c: 10 03       ..
    jmp c981b                                                         ; 9e9e: 4c 1b 98    L..

; &9ea1 referenced 1 time by &9e9c
.c9ea1
    lda #2                                                            ; 9ea1: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9ea3: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 9ea6: f0 04       ..             ; No FV -- error
; ***************************************************************************************
; TX completion handler
; 
; Stores result code 0 (success) into the first byte of the TX control
; block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
; and calls discard_reset_listen to return to idle.
; ***************************************************************************************
; &9ea8 referenced 2 times by &98f6, &9d1e
.tx_result_ok
    lda #0                                                            ; 9ea8: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 9eaa: f0 02       ..             ; BEQ: always taken (A=0); ALWAYS branch

; &9eac referenced 11 times by &983a, &9d58, &9e4b, &9e61, &9e69, &9e73, &9e78, &9e87, &9e8f, &9e97, &9ea6
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9eac: a9 41       .A
; ***************************************************************************************
; TX error handler
; 
; Stores error code (A) into the TX control block, sets &0D3A bit7
; for completion, and returns to idle via discard_reset_listen.
; Error codes: &00=success, &40=line jammed, &41=not listening,
; &42=net error.
; ***************************************************************************************
; &9eae referenced 2 times by &9d05, &9eaa
.tx_store_result
    ldy #0                                                            ; 9eae: a0 00       ..             ; Y=0: index into TX control block
    sta (nmi_tx_block),y                                              ; 9eb0: 91 a0       ..             ; Store result/error code at (nmi_tx_block),0
    lda #&80                                                          ; 9eb2: a9 80       ..             ; &80: completion flag for &0D3A
    sta tx_clear_flag                                                 ; 9eb4: 8d 62 0d    .b.            ; Signal TX complete
    jmp discard_reset_listen                                          ; 9eb7: 4c db 99    L..            ; Full ADLC reset and return to idle listen

; Unreferenced data block (purpose unknown)
    equb &0e, &0e, &0a, &0a, &0a, 6, 6, &0a, &81, 0, 0, 0, 0, 1, 1    ; 9eba: 0e 0e 0a... ...
    equb &81                                                          ; 9ec9: 81          .

; ***************************************************************************************
; Calculate transfer size
; 
; Computes the number of bytes actually transferred during a data
; frame reception. Subtracts the low pointer (LPTR, offset 4 in
; the RXCB) from the current buffer position to get the byte count,
; and stores it back into the RXCB's high pointer field (HPTR,
; offset 8). This tells the caller how much data was received.
; ***************************************************************************************
; &9eca referenced 2 times by &97be, &9cc2
.tx_calc_transfer
    ldy #6                                                            ; 9eca: a0 06       ..             ; Load RXCB[6] (buffer addr byte 2)
    lda (port_ws_offset),y                                            ; 9ecc: b1 a6       ..
    iny                                                               ; 9ece: c8          .              ; Y=&07
    and (port_ws_offset),y                                            ; 9ecf: 31 a6       1.             ; AND with RXCB[7] (byte 3)
    cmp #&ff                                                          ; 9ed1: c9 ff       ..             ; Both &FF = no buffer?
    beq c9f19                                                         ; 9ed3: f0 44       .D             ; Yes: fallback path
    lda tube_flag                                                     ; 9ed5: ad 67 0d    .g.            ; Tube transfer in progress?
    beq c9f19                                                         ; 9ed8: f0 3f       .?             ; No: fallback path
    lda tx_flags                                                      ; 9eda: ad 4a 0d    .J.
    ora #2                                                            ; 9edd: 09 02       ..             ; Set bit 1 (transfer complete)
    sta tx_flags                                                      ; 9edf: 8d 4a 0d    .J.
    sec                                                               ; 9ee2: 38          8              ; Init borrow for 4-byte subtract
    php                                                               ; 9ee3: 08          .              ; Save carry on stack
    ldy #4                                                            ; 9ee4: a0 04       ..             ; Y=4: start at RXCB offset 4
; &9ee6 referenced 1 time by &9ef8
.loop_c9ee6
    lda (port_ws_offset),y                                            ; 9ee6: b1 a6       ..             ; Load RXCB[Y] (current ptr byte)
    iny                                                               ; 9ee8: c8          .              ; Y += 4: advance to RXCB[Y+4]
    iny                                                               ; 9ee9: c8          .
    iny                                                               ; 9eea: c8          .
    iny                                                               ; 9eeb: c8          .
    plp                                                               ; 9eec: 28          (              ; Restore borrow from previous byte
    sbc (port_ws_offset),y                                            ; 9eed: f1 a6       ..             ; Subtract RXCB[Y+4] (start ptr byte)
    sta net_tx_ptr,y                                                  ; 9eef: 99 9a 00    ...            ; Store result byte
    dey                                                               ; 9ef2: 88          .              ; Y -= 3: next source byte
    dey                                                               ; 9ef3: 88          .
    dey                                                               ; 9ef4: 88          .
    php                                                               ; 9ef5: 08          .              ; Save borrow for next byte
    cpy #8                                                            ; 9ef6: c0 08       ..             ; Done all 4 bytes?
    bcc loop_c9ee6                                                    ; 9ef8: 90 ec       ..             ; No: next byte pair
    plp                                                               ; 9efa: 28          (              ; Discard final borrow
    txa                                                               ; 9efb: 8a          .              ; A = saved X
    pha                                                               ; 9efc: 48          H              ; Save X
    lda #4                                                            ; 9efd: a9 04       ..             ; Compute address of RXCB+4
    clc                                                               ; 9eff: 18          .
    adc port_ws_offset                                                ; 9f00: 65 a6       e.
    tax                                                               ; 9f02: aa          .              ; X = low byte of RXCB+4
    ldy rx_buf_offset                                                 ; 9f03: a4 a7       ..             ; Y = high byte of RXCB ptr
    lda #&c2                                                          ; 9f05: a9 c2       ..             ; Tube claim type &C2
    jsr tube_addr_claim                                               ; 9f07: 20 06 04     ..
    bcc c9f16                                                         ; 9f0a: 90 0a       ..             ; No Tube: skip reclaim
    lda scout_status                                                  ; 9f0c: ad 5c 0d    .\.            ; Tube: reclaim with scout status
    jsr tube_addr_claim                                               ; 9f0f: 20 06 04     ..
    jsr sub_c9a2b                                                     ; 9f12: 20 2b 9a     +.
    sec                                                               ; 9f15: 38          8              ; C=1: Tube address claimed
; &9f16 referenced 1 time by &9f0a
.c9f16
    pla                                                               ; 9f16: 68          h              ; Restore X
    tax                                                               ; 9f17: aa          .
    rts                                                               ; 9f18: 60          `

; &9f19 referenced 2 times by &9ed3, &9ed8
.c9f19
    ldy #4                                                            ; 9f19: a0 04       ..
    lda (port_ws_offset),y                                            ; 9f1b: b1 a6       ..             ; Load RXCB[4] (current ptr lo)
    ldy #8                                                            ; 9f1d: a0 08       ..
    sec                                                               ; 9f1f: 38          8
    sbc (port_ws_offset),y                                            ; 9f20: f1 a6       ..             ; Subtract RXCB[8] (start ptr lo)
    sta port_buf_len                                                  ; 9f22: 85 a2       ..             ; Store transfer size lo
    ldy #5                                                            ; 9f24: a0 05       ..
    lda (port_ws_offset),y                                            ; 9f26: b1 a6       ..             ; Load RXCB[5] (current ptr hi)
    equb &e9,   0, &85, &a5, &a0, 8, &b1, &a6, &85, &a4, &a0, 9, &b1  ; 9f28: e9 00 85... ...            ; Propagate borrow only
    equb &a6, &38, &e5                                                ; 9f35: a6 38 e5    .8.
    equb &a5                                                          ; 9f38: a5          .

    sta port_buf_len_hi                                               ; 9f39: 85 a3       ..             ; Store transfer size hi
    sec                                                               ; 9f3b: 38          8              ; Return with C=1
.nmi_shim_rom_src
    rts                                                               ; 9f3c: 60          `

; ***************************************************************************************
; ADLC full reset
; 
; Aborts all activity and returns to idle RX listen mode.
; ***************************************************************************************
; &9f3d referenced 3 times by &967d, &9705, &983d
.adlc_full_reset
    lda #&c1                                                          ; 9f3d: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 9f3f: 8d a0 fe    ...
    lda #&1e                                                          ; 9f42: a9 1e       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding
    sta econet_data_terminate_frame                                   ; 9f44: 8d a3 fe    ...
    lda #0                                                            ; 9f47: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 9f49: 8d a1 fe    ...
; ***************************************************************************************
; Enter RX listen mode
; 
; TX held in reset, RX active with interrupts. Clears all status.
; ***************************************************************************************
; &9f4c referenced 2 times by &99e8, &9f7a
.adlc_rx_listen
    lda #&82                                                          ; 9f4c: a9 82       ..             ; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 9f4e: 8d a0 fe    ...
    lda #&67 ; 'g'                                                    ; 9f51: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 9f53: 8d a1 fe    ...
    rts                                                               ; 9f56: 60          `

; &9f57 referenced 1 time by &06d4[4]
.c9f57
    bit econet_init_flag                                              ; 9f57: 2c 66 0d    ,f.            ; Econet not initialised -- skip to adlc_rx_listen
    bpl c9f7a                                                         ; 9f5a: 10 1e       ..
; &9f5c referenced 2 times by &9f61, &9f68
.c9f5c
    lda nmi_jmp_lo                                                    ; 9f5c: ad 0c 0d    ...            ; Spin until NMI handler = &96BF (nmi_rx_scout)
    cmp #&bf                                                          ; 9f5f: c9 bf       ..
    bne c9f5c                                                         ; 9f61: d0 f9       ..
    lda nmi_jmp_hi                                                    ; 9f63: ad 0d 0d    ...
    cmp #&96                                                          ; 9f66: c9 96       ..
    bne c9f5c                                                         ; 9f68: d0 f2       ..
    bit station_id_disable_net_nmis                                   ; 9f6a: 2c 18 fe    ,..            ; INTOFF before clearing state
; ***************************************************************************************
; Reset Econet flags and enter RX listen
; 
; Disables NMIs via INTOFF (BIT &FE18), clears tx_clear_flag and
; econet_init_flag to zero, then falls through to adlc_rx_listen
; with Y=5.
; ***************************************************************************************
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 9f6d: 2c 18 fe    ,..
    lda #0                                                            ; 9f70: a9 00       ..
    sta tx_clear_flag                                                 ; 9f72: 8d 62 0d    .b.
    sta econet_init_flag                                              ; 9f75: 8d 66 0d    .f.
    ldy #5                                                            ; 9f78: a0 05       ..
; &9f7a referenced 1 time by &9f5a
.c9f7a
l9f7c = c9f7a+2
    jmp adlc_rx_listen                                                ; 9f7a: 4c 4c 9f    LL.

; &9f7c referenced 1 time by &969a
; ***************************************************************************************
; Bootstrap NMI entry point (in ROM)
; 
; An alternate NMI handler that lives in the ROM itself rather than
; in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
; self-modifying JMP to dispatch to different handlers), this one
; hardcodes JMP nmi_rx_scout (&96BF). Used as the initial NMI handler
; before the workspace has been properly set up during initialisation.
; Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
; LDA romsel, STA &FE30, JMP &96BF.
; ***************************************************************************************
.nmi_bootstrap_entry
    bit station_id_disable_net_nmis                                   ; 9f7d: 2c 18 fe    ,..
    pha                                                               ; 9f80: 48          H
    tya                                                               ; 9f81: 98          .
    pha                                                               ; 9f82: 48          H
    lda #0                                                            ; 9f83: a9 00       ..             ; ROM bank 0 (patched during init for actual bank)
    sta romsel                                                        ; 9f85: 8d 30 fe    .0.
    jmp nmi_rx_scout                                                  ; 9f88: 4c bf 96    L..

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
    sty nmi_jmp_hi                                                    ; 9f8b: 8c 0d 0d    ...
    sta nmi_jmp_lo                                                    ; 9f8e: 8d 0c 0d    ...
    lda romsel_copy                                                   ; 9f91: a5 f4       ..
    sta romsel                                                        ; 9f93: 8d 30 fe    .0.
    pla                                                               ; 9f96: 68          h
    tay                                                               ; 9f97: a8          .
    pla                                                               ; 9f98: 68          h
    bit video_ula_control                                             ; 9f99: 2c 20 fe    , .
    rti                                                               ; 9f9c: 40          @

; ***************************************************************************************
; Print byte as two hex digits
; 
; Prints the high nibble first (via 4x LSR), then the low
; nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
; and output via OSASCI. Returns with carry set.
; ***************************************************************************************
; &9f9d referenced 2 times by &8cd7, &8d74
.print_hex
    pha                                                               ; 9f9d: 48          H
    lsr a                                                             ; 9f9e: 4a          J
    lsr a                                                             ; 9f9f: 4a          J
    lsr a                                                             ; 9fa0: 4a          J
    lsr a                                                             ; 9fa1: 4a          J
    jsr print_hex_nibble                                              ; 9fa2: 20 a6 9f     ..
    pla                                                               ; 9fa5: 68          h
; ***************************************************************************************
; Print single hex nibble
; 
; Converts the low nibble of A to ASCII hex ('0'-'9' or 'A'-'F')
; and prints via OSASCI. Returns with carry set.
; ***************************************************************************************
; &9fa6 referenced 1 time by &9fa2
.print_hex_nibble
    and #&0f                                                          ; 9fa6: 29 0f       ).
    cmp #&0a                                                          ; 9fa8: c9 0a       ..
    bcc c9fae                                                         ; 9faa: 90 02       ..
    adc #6                                                            ; 9fac: 69 06       i.             ; A-F: ADC #6 + ADC #&30 + C = &41-&46
; &9fae referenced 1 time by &9faa
.c9fae
    adc #&30 ; '0'                                                    ; 9fae: 69 30       i0
    jsr osasci                                                        ; 9fb0: 20 e3 ff     ..            ; Write character
    sec                                                               ; 9fb3: 38          8              ; C=1: callers use SEC as sentinel
    rts                                                               ; 9fb4: 60          `

    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9fb5: ff ff ff... ...
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9fc1: ff ff ff... ...
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9fcd: ff ff ff... ...
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9fd9: ff ff ff... ...
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9fe5: ff ff ff... ...
    equb &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff, &ff   ; 9ff1: ff ff ff... ...
    equb &ff, &ff, &ff                                                ; 9ffd: ff ff ff    ...
.pydis_end

    assert <(dispatch_net_cmd-1) == &6e
    assert <(econet_tx_rx-1) == &ef
    assert <(fscv_0_opt_entry-1) == &2b
    assert <(fscv_1_eof-1) == &ac
    assert <(fscv_2_star_run-1) == &db
    assert <(fscv_3_star_cmd-1) == &1a
    assert <(fscv_5_cat-1) == &66
    assert <(fscv_6_shutdown-1) == &50
    assert <(fscv_7_read_handles-1) == &ca
    assert <(fsreply_0_print_dir-1) == &95
    assert <(fsreply_1_copy_handles_boot-1) == &37
    assert <(fsreply_2_copy_handles-1) == &38
    assert <(fsreply_3_set_csd-1) == &31
    assert <(fsreply_4_notify_exec-1) == &e1
    assert <(fsreply_5_set_lib-1) == &2c
    assert <(l0128) == &28
    assert <(lang_0_insert_remote_key-1) == &fc
    assert <(lang_1_remote_boot-1) == &ae
    assert <(lang_2_save_palette_vdu-1) == &aa
    assert <(lang_3_execute_at_0100-1) == &dc
    assert <(lang_4_remote_validated-1) == &ec
    assert <(net_1_read_handle-1) == &66
    assert <(net_2_read_handle_entry-1) == &6c
    assert <(net_3_close_handle-1) == &7c
    assert <(net_4_resume_remote-1) == &bb
    assert <(osword_0f_handler-1) == &c1
    assert <(osword_10_handler-1) == &7b
    assert <(osword_11_handler-1) == &db
    assert <(printer_select_handler-1) == &da
    assert <(remote_cmd_dispatch-1) == &e7
    assert <(remote_print_handler-1) == &e9
    assert <(return_1-1) == &f5
    assert <(sub_c8f01-1) == &00
    assert <(sub_c90b6-1) == &b5
    assert <(sub_c9154-1) == &53
    assert <(sub_c9636-1) == &35
    assert <(sub_c9639-1) == &38
    assert <(sub_c963c-1) == &3b
    assert <(svc_13_select_nfs-1) == &f0
    assert <(svc_1_abs_workspace-1) == &bb
    assert <(svc_2_private_workspace-1) == &c4
    assert <(svc_3_autoboot-1) == &1c
    assert <(svc_4_star_command-1) == &b4
    assert <(svc_8_osword-1) == &86
    assert <(svc_9_help-1) == &07
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(fscv_0_opt_entry-1) == &8a
    assert >(fscv_1_eof-1) == &88
    assert >(fscv_2_star_run-1) == &8d
    assert >(fscv_3_star_cmd-1) == &8c
    assert >(fscv_5_cat-1) == &8c
    assert >(fscv_6_shutdown-1) == &83
    assert >(fscv_7_read_handles-1) == &86
    assert >(fsreply_0_print_dir-1) == &8d
    assert >(fsreply_1_copy_handles_boot-1) == &8e
    assert >(fsreply_2_copy_handles-1) == &8e
    assert >(fsreply_3_set_csd-1) == &8e
    assert >(fsreply_4_notify_exec-1) == &8d
    assert >(fsreply_5_set_lib-1) == &8e
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
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8f
    assert >(osword_11_handler-1) == &8e
    assert >(printer_select_handler-1) == &91
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_print_handler-1) == &91
    assert >(return_1-1) == &80
    assert >(sub_c8f01-1) == &8f
    assert >(sub_c90b6-1) == &90
    assert >(sub_c9154-1) == &91
    assert >(sub_c9636-1) == &96
    assert >(sub_c9639-1) == &96
    assert >(sub_c963c-1) == &96
    assert >(svc_13_select_nfs-1) == &81
    assert >(svc_1_abs_workspace-1) == &82
    assert >(svc_2_private_workspace-1) == &82
    assert >(svc_3_autoboot-1) == &82
    assert >(svc_4_star_command-1) == &81
    assert >(svc_8_osword-1) == &8e
    assert >(svc_9_help-1) == &82
    assert copyright - rom_header == &10

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           54
;     econet_control23_or_status2:             45
;     fs_options:                              41
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             37
;     net_rx_ptr:                              32
;     econet_control1_or_status1:              31
;     port_ws_offset:                          29
;     l00f0:                                   26
;     tx_flags:                                25
;     osbyte:                                  23
;     net_tx_ptr:                              22
;     c06c5:                                   21
;     port_buf_len:                            20
;     fs_load_addr_2:                          15
;     station_id_disable_net_nmis:             15
;     fs_load_addr:                            14
;     l00a8:                                   14
;     l0f06:                                   14
;     set_nmi_vector:                          14
;     l00ab:                                   13
;     nmi_tx_block:                            13
;     print_inline:                            13
;     tube_send_r2:                            13
;     c9835:                                   12
;     open_port_buf_hi:                        12
;     prepare_fs_cmd:                          12
;     open_port_buf:                           11
;     port_buf_len_hi:                         11
;     tube_data_register_2:                    11
;     tx_result_fail:                          11
;     l00a9:                                   10
;     tube_addr_claim:                         10
;     tube_data_register_3:                    10
;     tube_status_register_2:                  10
;     l00c4:                                    9
;     l00c8:                                    9
;     nfs_workspace_hi:                         9
;     rx_src_stn:                               9
;     fs_error_ptr:                             8
;     l00ad:                                    8
;     l0d11:                                    8
;     net_tx_ptr_hi:                            8
;     rx_flags:                                 8
;     tube_send_r4:                             8
;     tube_status_1_and_tube_control:           8
;     c9d58:                                    7
;     escapable:                                7
;     fs_cmd_csd:                               7
;     fs_cmd_urd:                               7
;     fs_crc_lo:                                7
;     l0015:                                    7
;     l0099:                                    7
;     l00b4:                                    7
;     osasci:                                   7
;     prot_status:                              7
;     restore_args_return:                      7
;     tx_clear_flag:                            7
;     tx_dst_stn:                               7
;     copy_string_to_cmd:                       6
;     fs_block_offset:                          6
;     fs_last_byte_flag:                        6
;     fs_load_addr_hi:                          6
;     l0000:                                    6
;     l0001:                                    6
;     nmi_rti:                                  6
;     tube_main_loop:                           6
;     c8530:                                    5
;     c89b5:                                    5
;     copy_filename:                            5
;     dispatch:                                 5
;     fs_boot_option:                           5
;     infol2:                                   5
;     l00b3:                                    5
;     l0100:                                    5
;     l0106:                                    5
;     l0f07:                                    5
;     need_release_tube:                        5
;     os_text_ptr:                              5
;     printer_buf_ptr:                          5
;     rx_buf_offset:                            5
;     rx_ctrl:                                  5
;     rx_port:                                  5
;     scout_error:                              5
;     system_via_acr:                           5
;     tube_flag:                                5
;     tube_send_r1:                             5
;     tx_dst_net:                               5
;     c88cd:                                    4
;     c89d4:                                    4
;     c8f1c:                                    4
;     clear_jsr_protection:                     4
;     data_tx_last:                             4
;     discard_listen:                           4
;     discard_reset_listen:                     4
;     econet_init_flag:                         4
;     fs_cmd_context:                           4
;     fs_eof_flags:                             4
;     fs_sequence_nos:                          4
;     fs_server_net:                            4
;     init_tx_ctrl_block:                       4
;     l00aa:                                    4
;     l00ac:                                    4
;     l00b9:                                    4
;     l00c0:                                    4
;     l00c1:                                    4
;     l00ef:                                    4
;     l00ff:                                    4
;     l0101:                                    4
;     net_rx_ptr_hi:                            4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     osnewl:                                   4
;     osrdsc_ptr:                               4
;     romsel_copy:                              4
;     rx_src_net:                               4
;     sub_c86d0:                                4
;     tube_reply_byte:                          4
;     tx_length:                                4
;     tx_poll_ff:                               4
;     video_ula_control:                        4
;     adlc_full_reset:                          3
;     c9101:                                    3
;     c979e:                                    3
;     c988e:                                    3
;     c99a4:                                    3
;     c9bdd:                                    3
;     c9dcd:                                    3
;     c9e2a:                                    3
;     c9e40:                                    3
;     calc_handle_offset:                       3
;     clear_fs_flag:                            3
;     data_rx_complete:                         3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_messages_flag:                         3
;     fs_server_stn:                            3
;     fs_urd_handle:                            3
;     handle_to_mask_a:                         3
;     incpx:                                    3
;     l0003:                                    3
;     l0054:                                    3
;     l00af:                                    3
;     l00b7:                                    3
;     l00ba:                                    3
;     l00cf:                                    3
;     l0df0:                                    3
;     l83b3:                                    3
;     match_osbyte_code:                        3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     nmi_tx_block_hi:                          3
;     openl4:                                   3
;     oscli:                                    3
;     osword:                                   3
;     oswrch:                                   3
;     print_reply_bytes:                        3
;     return_1:                                 3
;     return_inc_port_buf:                      3
;     save_fscv_args:                           3
;     save_fscv_args_with_ptrs:                 3
;     saved_jsr_mask:                           3
;     scout_status:                             3
;     setup_tx_and_send:                        3
;     sub_c9a37:                                3
;     tube_claim_loop:                          3
;     tube_data_register_1:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tx_active_start:                          3
;     tx_index:                                 3
;     ack_tx:                                   2
;     adjust_addrs:                             2
;     adlc_rx_listen:                           2
;     binary_version:                           2
;     c0482:                                    2
;     c0498:                                    2
;     c04c0:                                    2
;     c05fc:                                    2
;     c809d:                                    2
;     c80a0:                                    2
;     c811a:                                    2
;     c8134:                                    2
;     c8183:                                    2
;     c818f:                                    2
;     c8215:                                    2
;     c8316:                                    2
;     c8377:                                    2
;     c837d:                                    2
;     c837e:                                    2
;     c84ea:                                    2
;     c8637:                                    2
;     c863f:                                    2
;     c8657:                                    2
;     c86b3:                                    2
;     c86fd:                                    2
;     c87ef:                                    2
;     c87fb:                                    2
;     c8b3f:                                    2
;     c8bbb:                                    2
;     c8db2:                                    2
;     c8e29:                                    2
;     c8e35:                                    2
;     c8e7a:                                    2
;     c8fd1:                                    2
;     c9630:                                    2
;     c97ab:                                    2
;     c97ae:                                    2
;     c97b9:                                    2
;     c989d:                                    2
;     c994b:                                    2
;     c99eb:                                    2
;     c9a14:                                    2
;     c9a19:                                    2
;     c9a76:                                    2
;     c9c23:                                    2
;     c9e48:                                    2
;     c9f19:                                    2
;     c9f5c:                                    2
;     call_fscv_shutdown:                       2
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
;     flush_output_block:                       2
;     fs_cmd_lib:                               2
;     fs_cmd_match_table:                       2
;     fs_cmd_y_param:                           2
;     fs_crc_hi:                                2
;     fs_last_error:                            2
;     fs_lib_handle:                            2
;     fs_putb_buf:                              2
;     fs_state_deb:                             2
;     gsinit:                                   2
;     gsread:                                   2
;     handle_to_mask_clc:                       2
;     init_tx_ctrl_data:                        2
;     l0002:                                    2
;     l0012:                                    2
;     l0014:                                    2
;     l0055:                                    2
;     l0056:                                    2
;     l00b5:                                    2
;     l00f1:                                    2
;     l00f3:                                    2
;     l00fd:                                    2
;     l0102:                                    2
;     l0103:                                    2
;     l0128:                                    2
;     l0700:                                    2
;     l0e30:                                    2
;     l0f08:                                    2
;     l0f10:                                    2
;     l0f11:                                    2
;     l0f12:                                    2
;     l0fdf:                                    2
;     l8d54:                                    2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     nlisne:                                   2
;     num01:                                    2
;     osarg1:                                   2
;     osfind:                                   2
;     osrdch:                                   2
;     parse_decimal:                            2
;     parse_filename_gs:                        2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_dir_from_offset:                    2
;     print_hex:                                2
;     print_hex_bytes:                          2
;     print_reply_counted:                      2
;     prlp1:                                    2
;     readc1:                                   2
;     remot1:                                   2
;     return_3:                                 2
;     return_7:                                 2
;     return_match_osbyte:                      2
;     return_nbyte:                             2
;     return_printer_select:                    2
;     return_tube_init:                         2
;     romsel:                                   2
;     run_fscv_cmd:                             2
;     rx_extra_byte:                            2
;     rxpol2:                                   2
;     scout_complete:                           2
;     send_data_blocks:                         2
;     send_fs_reply_cmd:                        2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     sub_3_from_y:                             2
;     sub_c04d2:                                2
;     sub_c84a1:                                2
;     sub_c8e53:                                2
;     sub_c994e:                                2
;     sub_c9a2b:                                2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     transfer_file_blocks:                     2
;     tube_dispatch_table:                      2
;     tube_osword_read_lp:                      2
;     tube_rdch_reply:                          2
;     tube_status_register_4_and_cpu_control:   2
;     tube_transfer_addr:                       2
;     tx_calc_transfer:                         2
;     tx_ctrl_byte:                             2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
;     tx_store_result:                          2
;     tx_work_51:                               2
;     tx_work_57:                               2
;     access_bit_table:                         1
;     ack_tx_configure:                         1
;     ack_tx_write_dest:                        1
;     add_4_to_y:                               1
;     add_5_to_y:                               1
;     adjust_addrs_1:                           1
;     adjust_addrs_9:                           1
;     adjust_addrs_clc:                         1
;     adlc_init:                                1
;     argsw:                                    1
;     brkv:                                     1
;     bspsx:                                    1
;     bsxl0:                                    1
;     bsxl1:                                    1
;     build_send_fs_cmd:                        1
;     bytex:                                    1
;     c002a:                                    1
;     c0428:                                    1
;     c0432:                                    1
;     c0435:                                    1
;     c0463:                                    1
;     c0471:                                    1
;     c047a:                                    1
;     c0484:                                    1
;     c048c:                                    1
;     c04a2:                                    1
;     c04fb:                                    1
;     c0593:                                    1
;     c0645:                                    1
;     c06e4:                                    1
;     c8098:                                    1
;     c80c5:                                    1
;     c80e3:                                    1
;     c8113:                                    1
;     c8123:                                    1
;     c8181:                                    1
;     c8191:                                    1
;     c8193:                                    1
;     c81e3:                                    1
;     c81ea:                                    1
;     c825f:                                    1
;     c83ce:                                    1
;     c83cf:                                    1
;     c8405:                                    1
;     c846d:                                    1
;     c8473:                                    1
;     c8487:                                    1
;     c850c:                                    1
;     c8540:                                    1
;     c85dd:                                    1
;     c85e9:                                    1
;     c860a:                                    1
;     c8643:                                    1
;     c866a:                                    1
;     c8674:                                    1
;     c8696:                                    1
;     c8697:                                    1
;     c8740:                                    1
;     c87d8:                                    1
;     c8803:                                    1
;     c8817:                                    1
;     c8859:                                    1
;     c888e:                                    1
;     c891c:                                    1
;     c8922:                                    1
;     c8966:                                    1
;     c8997:                                    1
;     c89ba:                                    1
;     c89c5:                                    1
;     c8a2a:                                    1
;     c8a36:                                    1
;     c8a39:                                    1
;     c8a50:                                    1
;     c8a68:                                    1
;     c8a7d:                                    1
;     c8ab9:                                    1
;     c8af8:                                    1
;     c8afb:                                    1
;     c8b08:                                    1
;     c8b1c:                                    1
;     c8b53:                                    1
;     c8b94:                                    1
;     c8ba1:                                    1
;     c8bbe:                                    1
;     c8bfa:                                    1
;     c8c45:                                    1
;     c8c72:                                    1
;     c8cb0:                                    1
;     c8cba:                                    1
;     c8ced:                                    1
;     c8d11:                                    1
;     c8d33:                                    1
;     c8db4:                                    1
;     c8db7:                                    1
;     c8dd9:                                    1
;     c8e43:                                    1
;     c8f11:                                    1
;     c8f22:                                    1
;     c8f69:                                    1
;     c8fa6:                                    1
;     c8ffe:                                    1
;     c903e:                                    1
;     c915e:                                    1
;     c9218:                                    1
;     c922a:                                    1
;     c9321:                                    1
;     c9362:                                    1
;     c9672:                                    1
;     c9698:                                    1
;     c96d7:                                    1
;     c96f2:                                    1
;     c96f5:                                    1
;     c976b:                                    1
;     c9774:                                    1
;     c9778:                                    1
;     c978c:                                    1
;     c97cb:                                    1
;     c981b:                                    1
;     c982e:                                    1
;     c9848:                                    1
;     c9858:                                    1
;     c985f:                                    1
;     c986f:                                    1
;     c9948:                                    1
;     c9992:                                    1
;     c99b2:                                    1
;     c99bb:                                    1
;     c99f2:                                    1
;     c99f8:                                    1
;     c9a0d:                                    1
;     c9a34:                                    1
;     c9a63:                                    1
;     c9a6e:                                    1
;     c9a70:                                    1
;     c9ae7:                                    1
;     c9b6e:                                    1
;     c9b86:                                    1
;     c9bb1:                                    1
;     c9bc5:                                    1
;     c9bfb:                                    1
;     c9c21:                                    1
;     c9c8e:                                    1
;     c9cb0:                                    1
;     c9cf6:                                    1
;     c9cfd:                                    1
;     c9d21:                                    1
;     c9d2b:                                    1
;     c9dc1:                                    1
;     c9ddd:                                    1
;     c9ded:                                    1
;     c9e12:                                    1
;     c9ea1:                                    1
;     c9f16:                                    1
;     c9f57:                                    1
;     c9f7a:                                    1
;     c9fae:                                    1
;     cbset2:                                   1
;     cbset3:                                   1
;     cha4:                                     1
;     cha5:                                     1
;     cha5lp:                                   1
;     cha6:                                     1
;     chalp1:                                   1
;     chalp2:                                   1
;     clear_osbyte_ce_cf:                       1
;     cloop:                                    1
;     close_handle:                             1
;     close_single_handle:                      1
;     copy_fs_reply_to_cb:                      1
;     copy_string_from_offset:                  1
;     copyright_offset:                         1
;     ctrl_block_setup:                         1
;     ctrl_block_setup_clv:                     1
;     ctrl_block_template:                      1
;     data_tx_begin:                            1
;     data_tx_error:                            1
;     decfir:                                   1
;     decmin:                                   1
;     decmor:                                   1
;     delay_1ms:                                1
;     discard_after_reset:                      1
;     dispatch_0_hi-1:                          1
;     dispatch_0_lo-1:                          1
;     dofs01:                                   1
;     dofs2:                                    1
;     dofsl5:                                   1
;     dofsl7:                                   1
;     econet_data_terminate_frame:              1
;     entry1:                                   1
;     error1:                                   1
;     error_msg_table:                          1
;     error_offsets:                            1
;     evntv:                                    1
;     file1:                                    1
;     filev:                                    1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     floop:                                    1
;     fs2al1:                                   1
;     fs_cmd_type:                              1
;     fs_osword_dispatch:                       1
;     fs_osword_tbl_hi:                         1
;     fs_wait_cleanup:                          1
;     fscv:                                     1
;     fsdiel:                                   1
;     fstxl1:                                   1
;     fstxl2:                                   1
;     gbpbe1:                                   1
;     gbpbf1:                                   1
;     gbpbf2:                                   1
;     gbpbf3:                                   1
;     gbpbl1:                                   1
;     gbpbl3:                                   1
;     gbpbx:                                    1
;     gbpbx0:                                   1
;     gbpbx1:                                   1
;     get_file_protection:                      1
;     handle_to_mask:                           1
;     handshake_await_ack:                      1
;     immediate_op:                             1
;     info2:                                    1
;     init_fs_vectors:                          1
;     init_tx_ctrl_port:                        1
;     init_vectors_and_copy:                    1
;     initl:                                    1
;     install_saved_handler:                    1
;     issue_vectors_claimed:                    1
;     l0013:                                    1
;     l0051:                                    1
;     l00ae:                                    1
;     l00c2:                                    1
;     l00c7:                                    1
;     l00f7:                                    1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l0518:                                    1
;     l0600:                                    1
;     l0cff:                                    1
;     l0de6:                                    1
;     l0dfe:                                    1
;     l0e0b:                                    1
;     l0e16:                                    1
;     l0ef7:                                    1
;     l0f09:                                    1
;     l0f0b:                                    1
;     l0f0c:                                    1
;     l0f0d:                                    1
;     l0f0e:                                    1
;     l0f13:                                    1
;     l0f14:                                    1
;     l0f16:                                    1
;     l0fde:                                    1
;     l0fe0:                                    1
;     l4:                                       1
;     l8001:                                    1
;     l8002:                                    1
;     l8004:                                    1
;     l829a:                                    1
;     l8579:                                    1
;     l8c4c:                                    1
;     l8d68:                                    1
;     l8eb8:                                    1
;     l8eff:                                    1
;     l9145:                                    1
;     l91ac:                                    1
;     l91b0:                                    1
;     l931e:                                    1
;     l9462:                                    1
;     l9562:                                    1
;     l9a9d:                                    1
;     l9be2:                                    1
;     l9e39:                                    1
;     l9e41:                                    1
;     l9f7c:                                    1
;     language_entry:                           1
;     language_handler:                         1
;     loadop:                                   1
;     lodchk:                                   1
;     lodfil:                                   1
;     lodrl1:                                   1
;     lodrl2:                                   1
;     logon2:                                   1
;     loop_c0446:                               1
;     loop_c0466:                               1
;     loop_c04ab:                               1
;     loop_c04e5:                               1
;     loop_c0564:                               1
;     loop_c0577:                               1
;     loop_c05c7:                               1
;     loop_c05d3:                               1
;     loop_c05e6:                               1
;     loop_c064c:                               1
;     loop_c066a:                               1
;     loop_c8081:                               1
;     loop_c80ad:                               1
;     loop_c8179:                               1
;     loop_c81d6:                               1
;     loop_c8266:                               1
;     loop_c8307:                               1
;     loop_c8364:                               1
;     loop_c83d4:                               1
;     loop_c8489:                               1
;     loop_c84e4:                               1
;     loop_c851d:                               1
;     loop_c85e1:                               1
;     loop_c860d:                               1
;     loop_c8664:                               1
;     loop_c867b:                               1
;     loop_c86c1:                               1
;     loop_c8742:                               1
;     loop_c876e:                               1
;     loop_c8770:                               1
;     loop_c87b7:                               1
;     loop_c8822:                               1
;     loop_c8869:                               1
;     loop_c8887:                               1
;     loop_c898e:                               1
;     loop_c899d:                               1
;     loop_c8a5c:                               1
;     loop_c8b87:                               1
;     loop_c8baf:                               1
;     loop_c8bfc:                               1
;     loop_c8c24:                               1
;     loop_c8ce2:                               1
;     loop_c8d34:                               1
;     loop_c8dd0:                               1
;     loop_c8de8:                               1
;     loop_c8e96:                               1
;     loop_c8f3d:                               1
;     loop_c8f57:                               1
;     loop_c8fbc:                               1
;     loop_c9015:                               1
;     loop_c9055:                               1
;     loop_c9068:                               1
;     loop_c9123:                               1
;     loop_c9162:                               1
;     loop_c92c2:                               1
;     loop_c969a:                               1
;     loop_c98a3:                               1
;     loop_c9959:                               1
;     loop_c9987:                               1
;     loop_c99ff:                               1
;     loop_c9a5d:                               1
;     loop_c9b9a:                               1
;     loop_c9bbb:                               1
;     loop_c9ca4:                               1
;     loop_c9cd2:                               1
;     loop_c9d00:                               1
;     loop_c9ee6:                               1
;     mj:                                       1
;     nbyte1:                                   1
;     nbyte4:                                   1
;     nbyte5:                                   1
;     nbyte6:                                   1
;     netv:                                     1
;     nlistn:                                   1
;     nmi_data_rx_bulk:                         1
;     nmi_data_rx_skip:                         1
;     nmi_final_ack_validate:                   1
;     nmi_reply_validate:                       1
;     nmi_rx_scout:                             1
;     nmi_shim_07:                              1
;     nmi_shim_1a:                              1
;     nmi_workspace_start:                      1
;     openl6:                                   1
;     openl7:                                   1
;     opter1:                                   1
;     optl1:                                    1
;     osargs:                                   1
;     osbget:                                   1
;     osbput:                                   1
;     osfile:                                   1
;     osgbpb:                                   1
;     osgbpb_info:                              1
;     osword_tbl_hi:                            1
;     osword_tbl_lo:                            1
;     osword_trampoline:                        1
;     prepare_cmd_with_flag:                    1
;     print_hex_nibble:                         1
;     print_space:                              1
;     print_station_info:                       1
;     pydis_start:                              1
;     quote1:                                   1
;     rchex:                                    1
;     read_args_size:                           1
;     read_vdu_osbyte:                          1
;     read_vdu_osbyte_x0:                       1
;     readry:                                   1
;     return_10:                                1
;     return_2:                                 1
;     return_4:                                 1
;     return_5:                                 1
;     return_6:                                 1
;     return_8:                                 1
;     return_calc_handle:                       1
;     return_compare:                           1
;     return_dofsl7:                            1
;     return_lodchk:                            1
;     return_remote_cmd:                        1
;     rom_header:                               1
;     rom_type:                                 1
;     rsl1:                                     1
;     rssl1:                                    1
;     rssl2:                                    1
;     rx_error:                                 1
;     rx_error_reset:                           1
;     savchk:                                   1
;     save1:                                    1
;     save_args_handle:                         1
;     save_vdu_state:                           1
;     saveop:                                   1
;     savsiz:                                   1
;     scan0:                                    1
;     scan1:                                    1
;     scout_discard:                            1
;     scout_loop_rda:                           1
;     scout_loop_second:                        1
;     scout_match_port:                         1
;     scout_reject:                             1
;     send_fs_examine:                          1
;     service_entry:                            1
;     service_handler:                          1
;     set_listen_offset:                        1
;     setup1:                                   1
;     setup_rom_ptrs_netv:                      1
;     setup_rx_buffer_ptrs:                     1
;     store_16bit_at_y:                         1
;     store_fs_error:                           1
;     store_fs_flag:                            1
;     store_retry_count:                        1
;     strnh:                                    1
;     sub_4_from_y:                             1
;     sub_c0414:                                1
;     sub_c04cb:                                1
;     sub_c8387:                                1
;     sub_c8414:                                1
;     sub_c86de:                                1
;     sub_c86ea:                                1
;     sub_c8d9f:                                1
;     sub_c907c:                                1
;     sub_c9633:                                1
;     tbcop1:                                   1
;     tube_brk_handler:                         1
;     tube_brk_send_loop:                       1
;     tube_code_page4:                          1
;     tube_data_register_4:                     1
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
;     tube_reset_stack:                         1
;     tube_return_main:                         1
;     tx_ctrl_exit:                             1
;     tx_ctrl_template:                         1
;     tx_data_start:                            1
;     tx_error:                                 1
;     tx_last_data:                             1
;     tx_line_jammed:                           1
;     tx_prepare:                               1
;     tx_src_net:                               1
;     update_sequence_return:                   1
;     y2fsl2:                                   1
;     y2fsl5:                                   1

; Automatically generated labels:
;     c002a
;     c0428
;     c0432
;     c0435
;     c0463
;     c0471
;     c047a
;     c0482
;     c0484
;     c048c
;     c0498
;     c04a2
;     c04c0
;     c04fb
;     c0593
;     c05fc
;     c0645
;     c06c5
;     c06e4
;     c8098
;     c809d
;     c80a0
;     c80c5
;     c80e3
;     c8113
;     c811a
;     c8123
;     c8134
;     c8181
;     c8183
;     c818f
;     c8191
;     c8193
;     c81e3
;     c81ea
;     c8215
;     c825f
;     c8316
;     c8377
;     c837d
;     c837e
;     c83ce
;     c83cf
;     c8405
;     c846d
;     c8473
;     c8487
;     c84ea
;     c850c
;     c8530
;     c8540
;     c85dd
;     c85e9
;     c860a
;     c8637
;     c863f
;     c8643
;     c8657
;     c866a
;     c8674
;     c8696
;     c8697
;     c86b3
;     c86fd
;     c8740
;     c87d8
;     c87ef
;     c87fb
;     c8803
;     c8817
;     c8859
;     c888e
;     c88cd
;     c891c
;     c8922
;     c8966
;     c8997
;     c89b5
;     c89ba
;     c89c5
;     c89d4
;     c8a2a
;     c8a36
;     c8a39
;     c8a50
;     c8a68
;     c8a7d
;     c8ab9
;     c8af8
;     c8afb
;     c8b08
;     c8b1c
;     c8b3f
;     c8b53
;     c8b94
;     c8ba1
;     c8bbb
;     c8bbe
;     c8bfa
;     c8c45
;     c8c72
;     c8cb0
;     c8cba
;     c8ced
;     c8d11
;     c8d33
;     c8db2
;     c8db4
;     c8db7
;     c8dd9
;     c8e29
;     c8e35
;     c8e43
;     c8e7a
;     c8f11
;     c8f1c
;     c8f22
;     c8f69
;     c8fa6
;     c8fd1
;     c8ffe
;     c903e
;     c9101
;     c915e
;     c9218
;     c922a
;     c9321
;     c9362
;     c9630
;     c9672
;     c9698
;     c96d7
;     c96f2
;     c96f5
;     c976b
;     c9774
;     c9778
;     c978c
;     c979e
;     c97ab
;     c97ae
;     c97b9
;     c97cb
;     c981b
;     c982e
;     c9835
;     c9848
;     c9858
;     c985f
;     c986f
;     c988e
;     c989d
;     c9948
;     c994b
;     c9992
;     c99a4
;     c99b2
;     c99bb
;     c99eb
;     c99f2
;     c99f8
;     c9a0d
;     c9a14
;     c9a19
;     c9a34
;     c9a63
;     c9a6e
;     c9a70
;     c9a76
;     c9ae7
;     c9b6e
;     c9b86
;     c9bb1
;     c9bc5
;     c9bdd
;     c9bfb
;     c9c21
;     c9c23
;     c9c8e
;     c9cb0
;     c9cf6
;     c9cfd
;     c9d21
;     c9d2b
;     c9d58
;     c9dc1
;     c9dcd
;     c9ddd
;     c9ded
;     c9e12
;     c9e2a
;     c9e40
;     c9e48
;     c9ea1
;     c9f16
;     c9f19
;     c9f57
;     c9f5c
;     c9f7a
;     c9fae
;     l0000
;     l0001
;     l0002
;     l0003
;     l0012
;     l0013
;     l0014
;     l0015
;     l0051
;     l0054
;     l0055
;     l0056
;     l0099
;     l00a8
;     l00a9
;     l00aa
;     l00ab
;     l00ac
;     l00ad
;     l00ae
;     l00af
;     l00b3
;     l00b4
;     l00b5
;     l00b7
;     l00b9
;     l00ba
;     l00c0
;     l00c1
;     l00c2
;     l00c4
;     l00c7
;     l00c8
;     l00cf
;     l00ef
;     l00f0
;     l00f1
;     l00f3
;     l00f7
;     l00fd
;     l00ff
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
;     l0518
;     l0600
;     l0700
;     l0cff
;     l0d11
;     l0de6
;     l0df0
;     l0dfe
;     l0e0b
;     l0e16
;     l0e30
;     l0ef7
;     l0f06
;     l0f07
;     l0f08
;     l0f09
;     l0f0b
;     l0f0c
;     l0f0d
;     l0f0e
;     l0f10
;     l0f11
;     l0f12
;     l0f13
;     l0f14
;     l0f16
;     l0fde
;     l0fdf
;     l0fe0
;     l8001
;     l8002
;     l8004
;     l829a
;     l83b3
;     l8579
;     l857a
;     l8c4c
;     l8d54
;     l8d68
;     l8eb8
;     l8eff
;     l9145
;     l91ac
;     l91b0
;     l931e
;     l9462
;     l9562
;     l9a9d
;     l9be2
;     l9e39
;     l9e41
;     l9f7c
;     loop_c0446
;     loop_c0466
;     loop_c04ab
;     loop_c04e5
;     loop_c0564
;     loop_c0577
;     loop_c05c7
;     loop_c05d3
;     loop_c05e6
;     loop_c064c
;     loop_c066a
;     loop_c8081
;     loop_c80ad
;     loop_c8179
;     loop_c81d6
;     loop_c8266
;     loop_c8307
;     loop_c8364
;     loop_c83d4
;     loop_c8489
;     loop_c84e4
;     loop_c851d
;     loop_c85e1
;     loop_c860d
;     loop_c8664
;     loop_c867b
;     loop_c86c1
;     loop_c8742
;     loop_c876e
;     loop_c8770
;     loop_c87b7
;     loop_c8822
;     loop_c8869
;     loop_c8887
;     loop_c898e
;     loop_c899d
;     loop_c8a5c
;     loop_c8b87
;     loop_c8baf
;     loop_c8bfc
;     loop_c8c24
;     loop_c8ce2
;     loop_c8d34
;     loop_c8dd0
;     loop_c8de8
;     loop_c8e96
;     loop_c8f3d
;     loop_c8f57
;     loop_c8fbc
;     loop_c9015
;     loop_c9055
;     loop_c9068
;     loop_c9123
;     loop_c9162
;     loop_c92c2
;     loop_c969a
;     loop_c98a3
;     loop_c9959
;     loop_c9987
;     loop_c99ff
;     loop_c9a5d
;     loop_c9b9a
;     loop_c9bbb
;     loop_c9ca4
;     loop_c9cd2
;     loop_c9d00
;     loop_c9ee6
;     sub_c0414
;     sub_c04cb
;     sub_c04d2
;     sub_c8387
;     sub_c8414
;     sub_c84a1
;     sub_c86d0
;     sub_c86de
;     sub_c86ea
;     sub_c8d9f
;     sub_c8e53
;     sub_c8f01
;     sub_c907c
;     sub_c90b6
;     sub_c9154
;     sub_c9633
;     sub_c9636
;     sub_c9639
;     sub_c963c
;     sub_c994e
;     sub_c9a2b
;     sub_c9a37
;     sub_c9be1
;     sub_c9e38

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7283 bytes (89%)
;     Data                     = 909 bytes (11%)
;
;     Number of instructions   = 3535
;     Number of data bytes     = 666 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 243 bytes
;     Number of strings        = 37
