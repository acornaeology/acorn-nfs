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
osbyte_acknowledge_escape                   = 126
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
zp_63                                   = &0063
escapable                               = &0097
need_release_tube                       = &0098
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
userv                                   = &0200
filev                                   = &0212
fscv                                    = &021e
netv                                    = &0224
l0350                                   = &0350
l0351                                   = &0351
l0355                                   = &0355
l0700                                   = &0700
l078d                                   = &078d
l0cff                                   = &0cff
nmi_shim_07                             = &0d07
nmi_jmp_lo                              = &0d0c
nmi_jmp_hi                              = &0d0d
set_nmi_vector                          = &0d0e
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
l0de6                                   = &0de6
fs_state_deb                            = &0deb
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
l0e11                                   = &0e11
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
l7dfd                                   = &7dfd
l85bf                                   = &85bf
la260                                   = &a260
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

    org &9315

.c9315

; Move 1: &9315 to &16 for length 69
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
; &9315 referenced 1 time by &813d
.nmi_workspace_start
.tube_brk_handler
    lda #&ff                                                          ; 9315: a9 ff       ..  :0016[1]
    jsr tube_send_r4                                                  ; 9317: 20 d9 06     .. :0018[1]
    lda tube_data_register_2                                          ; 931a: ad e3 fe    ... :001b[1]
    lda #0                                                            ; 931d: a9 00       ..  :001e[1]
    jsr tube_send_r2                                                  ; 931f: 20 d0 06     .. :0020[1]
    tay                                                               ; 9322: a8          .   :0023[1]
    lda (l00fd),y                                                     ; 9323: b1 fd       ..  :0024[1]
    jsr tube_send_r2                                                  ; 9325: 20 d0 06     .. :0026[1]
; &9328 referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 9328: c8          .   :0029[1]
    lda (l00fd),y                                                     ; 9329: b1 fd       ..  :002a[1]
    jsr tube_send_r2                                                  ; 932b: 20 d0 06     .. :002c[1]
    tax                                                               ; 932e: aa          .   :002f[1]
    bne tube_brk_send_loop                                            ; 932f: d0 f7       ..  :0030[1]
.tube_reset_stack
    ldx #&ff                                                          ; 9331: a2 ff       ..  :0032[1]
    txs                                                               ; 9333: 9a          .   :0034[1]
    cli                                                               ; 9334: 58          X   :0035[1]
; &9335 referenced 2 times by &04ec[2], &053a[3]
.c0036
    stx zp_temp_11                                                    ; 9335: 86 11       ..  :0036[1]
    sty zp_temp_10                                                    ; 9337: 84 10       ..  :0038[1]
; &9339 referenced 7 times by &0048[1], &05ae[3], &05d5[3], &0623[4], &0638[4], &06a0[4], &06cd[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 9339: 2c e0 fe    ,.. :003a[1]
    bpl tube_poll_r2                                                  ; 933c: 10 06       ..  :003d[1]
; &933e referenced 1 time by &004d[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 933e: ad e1 fe    ... :003f[1]
    jsr nvwrch                                                        ; 9341: 20 cb ff     .. :0042[1]   ; Write character
; &9344 referenced 1 time by &003d[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9344: 2c e2 fe    ,.. :0045[1]
    bpl tube_main_loop                                                ; 9347: 10 f0       ..  :0048[1]
    bit tube_status_1_and_tube_control                                ; 9349: 2c e0 fe    ,.. :004a[1]
    bmi tube_handle_wrch                                              ; 934c: 30 f0       0.  :004d[1]
    ldx tube_data_register_2                                          ; 934e: ae e3 fe    ... :004f[1]
    stx l0055                                                         ; 9351: 86 55       .U  :0052[1]
.tube_dispatch_cmd
l0055 = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 9353: 6c 00 05    l.. :0054[1]

; &9354 referenced 1 time by &0052[1]
; &9356 referenced 2 times by &0478[2], &0493[2]
.tube_transfer_addr
    equb 0                                                            ; 9356: 00          .   :0057[1]
; &9357 referenced 2 times by &047c[2], &0498[2]
.l0058
    equb &80                                                          ; 9357: 80          .   :0058[1]
; &9358 referenced 1 time by &04a2[2]
.l0059
    equb 0                                                            ; 9358: 00          .   :0059[1]
; &9359 referenced 1 time by &04a0[2]
.l005a
    equb 0                                                            ; 9359: 00          .   :005a[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, c9315

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &005b

    ; Set the program counter to the next position in the binary file.
    org c9315 + (* - nmi_workspace_start)

.c935a

; Move 2: &935a to &0400 for length 256
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
; &935a referenced 1 time by &8123
.tube_code_page4
    jmp c0473                                                         ; 935a: 4c 73 04    Ls. :0400[2]

.tube_escape_entry
    jmp tube_escape_check                                             ; 935d: 4c e2 06    L.. :0403[2]

; &9360 referenced 10 times by &04bc[2], &04e4[2], &8b41, &8b53, &8bb0, &8e0f, &9a01, &9a53, &9fa7, &9faf
.tube_addr_claim
    cmp #&80                                                          ; 9360: c9 80       ..  :0406[2]
    bcc c0426                                                         ; 9362: 90 1c       ..  :0408[2]
    cmp #&c0                                                          ; 9364: c9 c0       ..  :040a[2]
    bcs c0419                                                         ; 9366: b0 0b       ..  :040c[2]
    ora #&40 ; '@'                                                    ; 9368: 09 40       .@  :040e[2]
    cmp l0015                                                         ; 936a: c5 15       ..  :0410[2]
    bne return_tube_init                                              ; 936c: d0 11       ..  :0412[2]
; &936e referenced 1 time by &8135
.tube_post_init
    lda #&80                                                          ; 936e: a9 80       ..  :0414[2]
    sta l0014                                                         ; 9370: 85 14       ..  :0416[2]
    rts                                                               ; 9372: 60          `   :0418[2]

; &9373 referenced 1 time by &040c[2]
.c0419
    asl l0014                                                         ; 9373: 06 14       ..  :0419[2]
    bcs c0423                                                         ; 9375: b0 06       ..  :041b[2]
    cmp l0015                                                         ; 9377: c5 15       ..  :041d[2]
    beq return_tube_init                                              ; 9379: f0 04       ..  :041f[2]
    clc                                                               ; 937b: 18          .   :0421[2]
    rts                                                               ; 937c: 60          `   :0422[2]

; &937d referenced 1 time by &041b[2]
.c0423
    sta l0015                                                         ; 937d: 85 15       ..  :0423[2]
; &937f referenced 2 times by &0412[2], &041f[2]
.return_tube_init
    rts                                                               ; 937f: 60          `   :0425[2]

; &9380 referenced 1 time by &0408[2]
.c0426
    sty l0013                                                         ; 9380: 84 13       ..  :0426[2]
    stx l0012                                                         ; 9382: 86 12       ..  :0428[2]
    jsr tube_send_r4                                                  ; 9384: 20 d9 06     .. :042a[2]
    tax                                                               ; 9387: aa          .   :042d[2]
    ldy #3                                                            ; 9388: a0 03       ..  :042e[2]
; &938a referenced 1 time by &0436[2]
.loop_c0430
    lda (l0012),y                                                     ; 938a: b1 12       ..  :0430[2]
    jsr tube_send_r4                                                  ; 938c: 20 d9 06     .. :0432[2]
    dey                                                               ; 938f: 88          .   :0435[2]
    bpl loop_c0430                                                    ; 9390: 10 f8       ..  :0436[2]
    jsr tube_send_r4                                                  ; 9392: 20 d9 06     .. :0438[2]
    ldy #&18                                                          ; 9395: a0 18       ..  :043b[2]
    sty tube_status_1_and_tube_control                                ; 9397: 8c e0 fe    ... :043d[2]
    lda l046b,x                                                       ; 939a: bd 6b 04    .k. :0440[2]
    sta tube_status_1_and_tube_control                                ; 939d: 8d e0 fe    ... :0443[2]
    lsr a                                                             ; 93a0: 4a          J   :0446[2]
    lsr a                                                             ; 93a1: 4a          J   :0447[2]
; &93a2 referenced 1 time by &044b[2]
.loop_c0448
    bit tube_status_register_4_and_cpu_control                        ; 93a2: 2c e6 fe    ,.. :0448[2]
    bvc loop_c0448                                                    ; 93a5: 50 fb       P.  :044b[2]
    bcs c045c                                                         ; 93a7: b0 0d       ..  :044d[2]
    cpx #4                                                            ; 93a9: e0 04       ..  :044f[2]
    bne return_tube_xfer                                              ; 93ab: d0 17       ..  :0451[2]
    pla                                                               ; 93ad: 68          h   :0453[2]
    pla                                                               ; 93ae: 68          h   :0454[2]
; &93af referenced 1 time by &04b8[2]
.c0455
    lda #&80                                                          ; 93af: a9 80       ..  :0455[2]
    sta l0014                                                         ; 93b1: 85 14       ..  :0457[2]
    jmp tube_reply_byte                                               ; 93b3: 4c cd 05    L.. :0459[2]

; &93b6 referenced 1 time by &044d[2]
.c045c
    bit tube_data_register_3                                          ; 93b6: 2c e5 fe    ,.. :045c[2]
    bit tube_data_register_3                                          ; 93b9: 2c e5 fe    ,.. :045f[2]
    lsr a                                                             ; 93bc: 4a          J   :0462[2]
    bcc return_tube_xfer                                              ; 93bd: 90 05       ..  :0463[2]
    ldy #&88                                                          ; 93bf: a0 88       ..  :0465[2]
    sty tube_status_1_and_tube_control                                ; 93c1: 8c e0 fe    ... :0467[2]
; &93c4 referenced 2 times by &0451[2], &0463[2]
.return_tube_xfer
    rts                                                               ; 93c4: 60          `   :046a[2]

; &93c5 referenced 1 time by &0440[2]
.l046b
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; 93c5: 86 88 96... ... :046b[2]

; &93cd referenced 1 time by &0400[2]
.c0473
    cli                                                               ; 93cd: 58          X   :0473[2]
    php                                                               ; 93ce: 08          .   :0474[2]
    pha                                                               ; 93cf: 48          H   :0475[2]
    ldy #0                                                            ; 93d0: a0 00       ..  :0476[2]
    sty tube_transfer_addr                                            ; 93d2: 84 57       .W  :0478[2]
    lda #&80                                                          ; 93d4: a9 80       ..  :047a[2]
    sta l0058                                                         ; 93d6: 85 58       .X  :047c[2]
    sta l0001                                                         ; 93d8: 85 01       ..  :047e[2]
    lda #&20 ; ' '                                                    ; 93da: a9 20       .   :0480[2]
    and rom_type                                                      ; 93dc: 2d 06 80    -.. :0482[2]
    beq c04a0                                                         ; 93df: f0 19       ..  :0485[2]
    ldx copyright_offset                                              ; 93e1: ae 07 80    ... :0487[2]
; &93e4 referenced 1 time by &048e[2]
.loop_c048a
    inx                                                               ; 93e4: e8          .   :048a[2]
    lda rom_header,x                                                  ; 93e5: bd 00 80    ... :048b[2]
    bne loop_c048a                                                    ; 93e8: d0 fa       ..  :048e[2]
    lda l8001,x                                                       ; 93ea: bd 01 80    ... :0490[2]
    sta tube_transfer_addr                                            ; 93ed: 85 57       .W  :0493[2]
    lda l8002,x                                                       ; 93ef: bd 02 80    ... :0495[2]
    sta l0058                                                         ; 93f2: 85 58       .X  :0498[2]
    ldy service_entry,x                                               ; 93f4: bc 03 80    ... :049a[2]
    lda l8004,x                                                       ; 93f7: bd 04 80    ... :049d[2]
; &93fa referenced 1 time by &0485[2]
.c04a0
    sta l005a                                                         ; 93fa: 85 5a       .Z  :04a0[2]
    sty l0059                                                         ; 93fc: 84 59       .Y  :04a2[2]
    pla                                                               ; 93fe: 68          h   :04a4[2]
    plp                                                               ; 93ff: 28          (   :04a5[2]
    bcs beginr                                                        ; 9400: b0 12       ..  :04a6[2]
    tax                                                               ; 9402: aa          .   :04a8[2]
    bne begink                                                        ; 9403: d0 03       ..  :04a9[2]
    jmp tube_reply_ack                                                ; 9405: 4c cb 05    L.. :04ab[2]

; &9408 referenced 1 time by &04a9[2]
.begink
    ldx #0                                                            ; 9408: a2 00       ..  :04ae[2]
    ldy #&ff                                                          ; 940a: a0 ff       ..  :04b0[2]
    lda #osbyte_read_write_last_break_type                            ; 940c: a9 fd       ..  :04b2[2]
    jsr osbyte                                                        ; 940e: 20 f4 ff     .. :04b4[2]   ; Read type of last reset
    txa                                                               ; 9411: 8a          .   :04b7[2]   ; X=value of type of last reset
    beq c0455                                                         ; 9412: f0 9b       ..  :04b8[2]
; &9414 referenced 2 times by &04a6[2], &04bf[2]
.beginr
    lda #&ff                                                          ; 9414: a9 ff       ..  :04ba[2]
    jsr tube_addr_claim                                               ; 9416: 20 06 04     .. :04bc[2]
    bcc beginr                                                        ; 9419: 90 f9       ..  :04bf[2]
    lda #1                                                            ; 941b: a9 01       ..  :04c1[2]
    jsr tube_setup_transfer                                           ; 941d: 20 e0 04     .. :04c3[2]
    ldy #0                                                            ; 9420: a0 00       ..  :04c6[2]
    sty l0000                                                         ; 9422: 84 00       ..  :04c8[2]
    ldx #&40 ; '@'                                                    ; 9424: a2 40       .@  :04ca[2]
; &9426 referenced 2 times by &04d7[2], &04dc[2]
.c04cc
    lda (l0000),y                                                     ; 9426: b1 00       ..  :04cc[2]
    sta tube_data_register_3                                          ; 9428: 8d e5 fe    ... :04ce[2]
; &942b referenced 1 time by &04d4[2]
.loop_c04d1
    bit tube_status_register_3                                        ; 942b: 2c e4 fe    ,.. :04d1[2]
    bvc loop_c04d1                                                    ; 942e: 50 fb       P.  :04d4[2]
    iny                                                               ; 9430: c8          .   :04d6[2]
    bne c04cc                                                         ; 9431: d0 f3       ..  :04d7[2]
    inc l0001                                                         ; 9433: e6 01       ..  :04d9[2]
    dex                                                               ; 9435: ca          .   :04db[2]
    bne c04cc                                                         ; 9436: d0 ee       ..  :04dc[2]
    lda #4                                                            ; 9438: a9 04       ..  :04de[2]
; &943a referenced 1 time by &04c3[2]
.tube_setup_transfer
    ldy #0                                                            ; 943a: a0 00       ..  :04e0[2]
    ldx #&57 ; 'W'                                                    ; 943c: a2 57       .W  :04e2[2]
    jmp tube_addr_claim                                               ; 943e: 4c 06 04    L.. :04e4[2]

.tube_rdch_handler
    lda #1                                                            ; 9441: a9 01       ..  :04e7[2]
    jsr tube_send_r2                                                  ; 9443: 20 d0 06     .. :04e9[2]
    jmp c0036                                                         ; 9446: 4c 36 00    L6. :04ec[2]

.tube_restore_regs
    ldy zp_temp_10                                                    ; 9449: a4 10       ..  :04ef[2]
    ldx zp_temp_11                                                    ; 944b: a6 11       ..  :04f1[2]
    jsr tube_read_r2                                                  ; 944d: 20 f7 04     .. :04f3[2]
    asl a                                                             ; 9450: 0a          .   :04f6[2]
; &9451 referenced 22 times by &04f3[2], &04fa[2], &0543[3], &0547[3], &0550[3], &0569[3], &0580[3], &058c[3], &0592[3], &059b[3], &05b5[3], &05da[3], &05eb[3], &0604[4], &060c[4], &0626[4], &062a[4], &063b[4], &063f[4], &0643[4], &065d[4], &06a5[4]
.tube_read_r2
    bit tube_status_register_2                                        ; 9451: 2c e2 fe    ,.. :04f7[2]
    bpl tube_read_r2                                                  ; 9454: 10 fb       ..  :04fa[2]
    lda tube_data_register_2                                          ; 9456: ad e3 fe    ... :04fc[2]
    rts                                                               ; 9459: 60          `   :04ff[2]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, c935a

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &0500

    ; Set the program counter to the next position in the binary file.
    org c935a + (* - tube_code_page4)

.l945a

; Move 3: &945a to &0500 for length 256
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
; &945a referenced 2 times by &0054[1], &8129
.tube_dispatch_table
    equb &5b, 5, &c5, 5, &26, 6, &3b, 6, &5d, 6, &a3, 6, &ef, 4       ; 945a: 5b 05 c5... [.. :0500[3]
    equb &3d, 5, &8c, 5, &50, 5, &43, 5, &69, 5, &d8, 5,   2, 6       ; 9468: 3d 05 8c... =.. :050e[3]

.tube_wrch_handler
    pha                                                               ; 9476: 48          H   :051c[3]
    lda #0                                                            ; 9477: a9 00       ..  :051d[3]
.tube_send_and_poll
    jsr tube_send_r2                                                  ; 9479: 20 d0 06     .. :051f[3]
; &947c referenced 2 times by &052a[3], &0532[3]
.c0522
    bit tube_status_register_2                                        ; 947c: 2c e2 fe    ,.. :0522[3]
    bvs c0535                                                         ; 947f: 70 0e       p.  :0525[3]
.tube_poll_r1_wrch
    bit tube_status_1_and_tube_control                                ; 9481: 2c e0 fe    ,.. :0527[3]
    bpl c0522                                                         ; 9484: 10 f6       ..  :052a[3]
    lda tube_data_register_1                                          ; 9486: ad e1 fe    ... :052c[3]
    jsr nvwrch                                                        ; 9489: 20 cb ff     .. :052f[3]   ; Write character
.tube_resume_poll
    jmp c0522                                                         ; 948c: 4c 22 05    L". :0532[3]

; &948f referenced 1 time by &0525[3]
.c0535
    pla                                                               ; 948f: 68          h   :0535[3]
    sta tube_data_register_2                                          ; 9490: 8d e3 fe    ... :0536[3]
    pha                                                               ; 9493: 48          H   :0539[3]
    jmp c0036                                                         ; 9494: 4c 36 00    L6. :053a[3]

.tube_release_return
    ldx zp_temp_11                                                    ; 9497: a6 11       ..  :053d[3]
    ldy zp_temp_10                                                    ; 9499: a4 10       ..  :053f[3]
    pla                                                               ; 949b: 68          h   :0541[3]
    rts                                                               ; 949c: 60          `   :0542[3]

.tube_osbput
    jsr tube_read_r2                                                  ; 949d: 20 f7 04     .. :0543[3]
    tay                                                               ; 94a0: a8          .   :0546[3]
    jsr tube_read_r2                                                  ; 94a1: 20 f7 04     .. :0547[3]
    jsr osbput                                                        ; 94a4: 20 d4 ff     .. :054a[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 94a7: 4c cb 05    L.. :054d[3]

.tube_osbget
    jsr tube_read_r2                                                  ; 94aa: 20 f7 04     .. :0550[3]
    tay                                                               ; 94ad: a8          .   :0553[3]   ; Y=file handle
    jsr osbget                                                        ; 94ae: 20 d7 ff     .. :0554[3]   ; Read a single byte from an open file Y
    pha                                                               ; 94b1: 48          H   :0557[3]
    jmp c055f                                                         ; 94b2: 4c 5f 05    L_. :0558[3]

.tube_osrdch
    jsr nvrdch                                                        ; 94b5: 20 c8 ff     .. :055b[3]   ; Read a character from the current input stream
    pha                                                               ; 94b8: 48          H   :055e[3]   ; A=character read
; &94b9 referenced 1 time by &0558[3]
.c055f
    ora #&80                                                          ; 94b9: 09 80       ..  :055f[3]
.tube_rdch_reply
    ror a                                                             ; 94bb: 6a          j   :0561[3]
    jsr tube_send_r2                                                  ; 94bc: 20 d0 06     .. :0562[3]
    pla                                                               ; 94bf: 68          h   :0565[3]
    jmp tube_reply_byte                                               ; 94c0: 4c cd 05    L.. :0566[3]

.tube_osfind
    jsr tube_read_r2                                                  ; 94c3: 20 f7 04     .. :0569[3]
    beq tube_osfind_close                                             ; 94c6: f0 12       ..  :056c[3]
    pha                                                               ; 94c8: 48          H   :056e[3]
    jsr tube_read_string                                              ; 94c9: 20 b1 05     .. :056f[3]
    pla                                                               ; 94cc: 68          h   :0572[3]
    jsr osfind                                                        ; 94cd: 20 ce ff     .. :0573[3]   ; Open or close file(s)
    pha                                                               ; 94d0: 48          H   :0576[3]
    lda #&ff                                                          ; 94d1: a9 ff       ..  :0577[3]
    jsr tube_send_r2                                                  ; 94d3: 20 d0 06     .. :0579[3]
    pla                                                               ; 94d6: 68          h   :057c[3]
    jmp tube_reply_byte                                               ; 94d7: 4c cd 05    L.. :057d[3]

; &94da referenced 1 time by &056c[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; 94da: 20 f7 04     .. :0580[3]
    tay                                                               ; 94dd: a8          .   :0583[3]
    lda #osfind_close                                                 ; 94de: a9 00       ..  :0584[3]
    jsr osfind                                                        ; 94e0: 20 ce ff     .. :0586[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94e3: 4c cb 05    L.. :0589[3]

.tube_osargs
    jsr tube_read_r2                                                  ; 94e6: 20 f7 04     .. :058c[3]
    tay                                                               ; 94e9: a8          .   :058f[3]
.tube_read_params
    ldx #3                                                            ; 94ea: a2 03       ..  :0590[3]
; &94ec referenced 1 time by &0598[3]
.loop_c0592
    jsr tube_read_r2                                                  ; 94ec: 20 f7 04     .. :0592[3]
    sta l0000,x                                                       ; 94ef: 95 00       ..  :0595[3]
    dex                                                               ; 94f1: ca          .   :0597[3]
    bpl loop_c0592                                                    ; 94f2: 10 f8       ..  :0598[3]
    inx                                                               ; 94f4: e8          .   :059a[3]
    jsr tube_read_r2                                                  ; 94f5: 20 f7 04     .. :059b[3]
    jsr osargs                                                        ; 94f8: 20 da ff     .. :059e[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 94fb: 20 d0 06     .. :05a1[3]
    ldx #3                                                            ; 94fe: a2 03       ..  :05a4[3]
; &9500 referenced 1 time by &05ac[3]
.loop_c05a6
    lda l0000,x                                                       ; 9500: b5 00       ..  :05a6[3]
    jsr tube_send_r2                                                  ; 9502: 20 d0 06     .. :05a8[3]
    dex                                                               ; 9505: ca          .   :05ab[3]
    bpl loop_c05a6                                                    ; 9506: 10 f8       ..  :05ac[3]
    jmp tube_main_loop                                                ; 9508: 4c 3a 00    L:. :05ae[3]

; &950b referenced 3 times by &056f[3], &05c5[3], &05e2[3]
.tube_read_string
    ldx #0                                                            ; 950b: a2 00       ..  :05b1[3]
    ldy #0                                                            ; 950d: a0 00       ..  :05b3[3]
; &950f referenced 1 time by &05c0[3]
.strnh
    jsr tube_read_r2                                                  ; 950f: 20 f7 04     .. :05b5[3]
    sta l0700,y                                                       ; 9512: 99 00 07    ... :05b8[3]
    iny                                                               ; 9515: c8          .   :05bb[3]
    beq c05c2                                                         ; 9516: f0 04       ..  :05bc[3]
    cmp #&0d                                                          ; 9518: c9 0d       ..  :05be[3]
    bne strnh                                                         ; 951a: d0 f3       ..  :05c0[3]
; &951c referenced 1 time by &05bc[3]
.c05c2
    ldy #7                                                            ; 951c: a0 07       ..  :05c2[3]
    rts                                                               ; 951e: 60          `   :05c4[3]

.tube_oscli
    jsr tube_read_string                                              ; 951f: 20 b1 05     .. :05c5[3]
    jsr oscli                                                         ; 9522: 20 f7 ff     .. :05c8[3]
; &9525 referenced 3 times by &04ab[2], &054d[3], &0589[3]
.tube_reply_ack
    lda #&7f                                                          ; 9525: a9 7f       ..  :05cb[3]
; &9527 referenced 5 times by &0459[2], &0566[3], &057d[3], &05d0[3], &06b8[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 9527: 2c e2 fe    ,.. :05cd[3]
    bvc tube_reply_byte                                               ; 952a: 50 fb       P.  :05d0[3]
    sta tube_data_register_2                                          ; 952c: 8d e3 fe    ... :05d2[3]
; &952f referenced 1 time by &0600[4]
.mj
    jmp tube_main_loop                                                ; 952f: 4c 3a 00    L:. :05d5[3]

.tube_osfile
    ldx #&10                                                          ; 9532: a2 10       ..  :05d8[3]
; &9534 referenced 1 time by &05e0[3]
.argsw
    jsr tube_read_r2                                                  ; 9534: 20 f7 04     .. :05da[3]
    sta l0001,x                                                       ; 9537: 95 01       ..  :05dd[3]
    dex                                                               ; 9539: ca          .   :05df[3]
    bne argsw                                                         ; 953a: d0 f8       ..  :05e0[3]
    jsr tube_read_string                                              ; 953c: 20 b1 05     .. :05e2[3]
    stx l0000                                                         ; 953f: 86 00       ..  :05e5[3]
    sty l0001                                                         ; 9541: 84 01       ..  :05e7[3]
    ldy #0                                                            ; 9543: a0 00       ..  :05e9[3]
    jsr tube_read_r2                                                  ; 9545: 20 f7 04     .. :05eb[3]
    jsr osfile                                                        ; 9548: 20 dd ff     .. :05ee[3]
    ora #&80                                                          ; 954b: 09 80       ..  :05f1[3]
    jsr tube_send_r2                                                  ; 954d: 20 d0 06     .. :05f3[3]
    ldx #&10                                                          ; 9550: a2 10       ..  :05f6[3]
; &9552 referenced 1 time by &05fe[3]
.loop_c05f8
    lda l0001,x                                                       ; 9552: b5 01       ..  :05f8[3]
    jsr tube_send_r2                                                  ; 9554: 20 d0 06     .. :05fa[3]
    dex                                                               ; 9557: ca          .   :05fd[3]
    bne loop_c05f8                                                    ; 9558: d0 f8       ..  :05fe[3]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_dispatch_table, *, l945a

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_dispatch_table, &0600

    ; Set the program counter to the next position in the binary file.
    org l945a + (* - tube_dispatch_table)

.c955a

; Move 4: &955a to &0600 for length 256
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
; &955a referenced 1 time by &812f
.tube_code_page6
    beq mj                                                            ; 955a: f0 d3       ..  :0600[4]
.tube_osgbpb
    ldx #&0c                                                          ; 955c: a2 0c       ..  :0602[4]
; &955e referenced 1 time by &060a[4]
.loop_c0604
    jsr tube_read_r2                                                  ; 955e: 20 f7 04     .. :0604[4]
    sta l0000,x                                                       ; 9561: 95 00       ..  :0607[4]
    dex                                                               ; 9563: ca          .   :0609[4]
    bpl loop_c0604                                                    ; 9564: 10 f8       ..  :060a[4]
    jsr tube_read_r2                                                  ; 9566: 20 f7 04     .. :060c[4]
    inx                                                               ; 9569: e8          .   :060f[4]
    ldy #0                                                            ; 956a: a0 00       ..  :0610[4]
    jsr osgbpb                                                        ; 956c: 20 d1 ff     .. :0612[4]   ; Read or write multiple bytes to an open file
    ror a                                                             ; 956f: 6a          j   :0615[4]   ; 3.35K fix: send carry result to co-processor.
; 3.35D had PHA here (never sent, never popped).
    jsr tube_send_r2                                                  ; 9570: 20 d0 06     .. :0616[4]
    ldx #&0c                                                          ; 9573: a2 0c       ..  :0619[4]
; &9575 referenced 1 time by &0621[4]
.loop_c061b
    lda l0000,x                                                       ; 9575: b5 00       ..  :061b[4]
    jsr tube_send_r2                                                  ; 9577: 20 d0 06     .. :061d[4]
    dex                                                               ; 957a: ca          .   :0620[4]
    bpl loop_c061b                                                    ; 957b: 10 f8       ..  :0621[4]
    jmp tube_main_loop                                                ; 957d: 4c 3a 00    L:. :0623[4]

.tube_osbyte_short
    jsr tube_read_r2                                                  ; 9580: 20 f7 04     .. :0626[4]
    tax                                                               ; 9583: aa          .   :0629[4]
    jsr tube_read_r2                                                  ; 9584: 20 f7 04     .. :062a[4]
    jsr osbyte                                                        ; 9587: 20 f4 ff     .. :062d[4]
; &958a referenced 2 times by &0633[4], &065b[4]
.tube_osbyte_send_x
    bit tube_status_register_2                                        ; 958a: 2c e2 fe    ,.. :0630[4]
    bvc tube_osbyte_send_x                                            ; 958d: 50 fb       P.  :0633[4]
    stx tube_data_register_2                                          ; 958f: 8e e3 fe    ... :0635[4]
; &9592 referenced 1 time by &064b[4]
.bytex
    jmp tube_main_loop                                                ; 9592: 4c 3a 00    L:. :0638[4]

.tube_osbyte_long
    jsr tube_read_r2                                                  ; 9595: 20 f7 04     .. :063b[4]
    tax                                                               ; 9598: aa          .   :063e[4]
    jsr tube_read_r2                                                  ; 9599: 20 f7 04     .. :063f[4]
    tay                                                               ; 959c: a8          .   :0642[4]
    jsr tube_read_r2                                                  ; 959d: 20 f7 04     .. :0643[4]
    jsr osbyte                                                        ; 95a0: 20 f4 ff     .. :0646[4]
    eor #&9d                                                          ; 95a3: 49 9d       I.  :0649[4]
    beq bytex                                                         ; 95a5: f0 eb       ..  :064b[4]
    lda #&40 ; '@'                                                    ; 95a7: a9 40       .@  :064d[4]
    ror a                                                             ; 95a9: 6a          j   :064f[4]
    jsr tube_send_r2                                                  ; 95aa: 20 d0 06     .. :0650[4]
; &95ad referenced 1 time by &0656[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 95ad: 2c e2 fe    ,.. :0653[4]
    bvc tube_osbyte_send_y                                            ; 95b0: 50 fb       P.  :0656[4]
    sty tube_data_register_2                                          ; 95b2: 8c e3 fe    ... :0658[4]
    bvs tube_osbyte_send_x                                            ; 95b5: 70 d3       p.  :065b[4]   ; ALWAYS branch

.tube_osword
    jsr tube_read_r2                                                  ; 95b7: 20 f7 04     .. :065d[4]
    tay                                                               ; 95ba: a8          .   :0660[4]
; &95bb referenced 1 time by &0664[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 95bb: 2c e2 fe    ,.. :0661[4]
    bpl tube_osword_read                                              ; 95be: 10 fb       ..  :0664[4]
    ldx tube_data_register_2                                          ; 95c0: ae e3 fe    ... :0666[4]
    dex                                                               ; 95c3: ca          .   :0669[4]
    bmi c067b                                                         ; 95c4: 30 0f       0.  :066a[4]
; &95c6 referenced 2 times by &066f[4], &0678[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 95c6: 2c e2 fe    ,.. :066c[4]
    bpl tube_osword_read_lp                                           ; 95c9: 10 fb       ..  :066f[4]
    lda tube_data_register_2                                          ; 95cb: ad e3 fe    ... :0671[4]
    sta l0128,x                                                       ; 95ce: 9d 28 01    .(. :0674[4]
    dex                                                               ; 95d1: ca          .   :0677[4]
    bpl tube_osword_read_lp                                           ; 95d2: 10 f2       ..  :0678[4]
    tya                                                               ; 95d4: 98          .   :067a[4]
; &95d5 referenced 1 time by &066a[4]
.c067b
    ldx #<(l0128)                                                     ; 95d5: a2 28       .(  :067b[4]
    ldy #>(l0128)                                                     ; 95d7: a0 01       ..  :067d[4]
    jsr osword                                                        ; 95d9: 20 f1 ff     .. :067f[4]
    lda #&ff                                                          ; 95dc: a9 ff       ..  :0682[4]
    jsr tube_send_r2                                                  ; 95de: 20 d0 06     .. :0684[4]
; &95e1 referenced 1 time by &068a[4]
.loop_c0687
    bit tube_status_register_2                                        ; 95e1: 2c e2 fe    ,.. :0687[4]
    bpl loop_c0687                                                    ; 95e4: 10 fb       ..  :068a[4]
    ldx tube_data_register_2                                          ; 95e6: ae e3 fe    ... :068c[4]
    dex                                                               ; 95e9: ca          .   :068f[4]
    bmi tube_return_main                                              ; 95ea: 30 0e       0.  :0690[4]
; &95ec referenced 1 time by &069e[4]
.tube_osword_write
    ldy l0128,x                                                       ; 95ec: bc 28 01    .(. :0692[4]
; &95ef referenced 1 time by &0698[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95ef: 2c e2 fe    ,.. :0695[4]
    bvc tube_osword_write_lp                                          ; 95f2: 50 fb       P.  :0698[4]
    sty tube_data_register_2                                          ; 95f4: 8c e3 fe    ... :069a[4]
    dex                                                               ; 95f7: ca          .   :069d[4]
    bpl tube_osword_write                                             ; 95f8: 10 f2       ..  :069e[4]
; &95fa referenced 1 time by &0690[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95fa: 4c 3a 00    L:. :06a0[4]

.tube_osword_rdln
    ldx #4                                                            ; 95fd: a2 04       ..  :06a3[4]
; &95ff referenced 1 time by &06ab[4]
.loop_c06a5
    jsr tube_read_r2                                                  ; 95ff: 20 f7 04     .. :06a5[4]
    sta l0000,x                                                       ; 9602: 95 00       ..  :06a8[4]
    dex                                                               ; 9604: ca          .   :06aa[4]
    bpl loop_c06a5                                                    ; 9605: 10 f8       ..  :06ab[4]
    inx                                                               ; 9607: e8          .   :06ad[4]
    ldy #0                                                            ; 9608: a0 00       ..  :06ae[4]
    txa                                                               ; 960a: 8a          .   :06b0[4]
    jsr osword                                                        ; 960b: 20 f1 ff     .. :06b1[4]
    bcc tube_rdln_send_line                                           ; 960e: 90 05       ..  :06b4[4]
    lda #&ff                                                          ; 9610: a9 ff       ..  :06b6[4]
    jmp tube_reply_byte                                               ; 9612: 4c cd 05    L.. :06b8[4]

; &9615 referenced 1 time by &06b4[4]
.tube_rdln_send_line
    ldx #0                                                            ; 9615: a2 00       ..  :06bb[4]
    lda #&7f                                                          ; 9617: a9 7f       ..  :06bd[4]
    jsr tube_send_r2                                                  ; 9619: 20 d0 06     .. :06bf[4]
; &961c referenced 1 time by &06cb[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 961c: bd 00 07    ... :06c2[4]
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 961f: 20 d0 06     .. :06c5[4]
    inx                                                               ; 9622: e8          .   :06c8[4]
    cmp #&0d                                                          ; 9623: c9 0d       ..  :06c9[4]
    bne tube_rdln_send_loop                                           ; 9625: d0 f5       ..  :06cb[4]
    jmp tube_main_loop                                                ; 9627: 4c 3a 00    L:. :06cd[4]

; &962a referenced 18 times by &0020[1], &0026[1], &002c[1], &04e9[2], &051f[3], &0562[3], &0579[3], &05a1[3], &05a8[3], &05f3[3], &05fa[3], &0616[4], &061d[4], &0650[4], &0684[4], &06bf[4], &06c5[4], &06d3[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 962a: 2c e2 fe    ,.. :06d0[4]
    bvc tube_send_r2                                                  ; 962d: 50 fb       P.  :06d3[4]
    sta tube_data_register_2                                          ; 962f: 8d e3 fe    ... :06d5[4]
    rts                                                               ; 9632: 60          `   :06d8[4]

; &9633 referenced 5 times by &0018[1], &042a[2], &0432[2], &0438[2], &06dc[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 9633: 2c e6 fe    ,.. :06d9[4]
    bvc tube_send_r4                                                  ; 9636: 50 fb       P.  :06dc[4]
    sta tube_data_register_4                                          ; 9638: 8d e7 fe    ... :06de[4]
    rts                                                               ; 963b: 60          `   :06e1[4]

; &963c referenced 1 time by &0403[2]
.tube_escape_check
    lda l00ff                                                         ; 963c: a5 ff       ..  :06e2[4]
    sec                                                               ; 963e: 38          8   :06e4[4]
    ror a                                                             ; 963f: 6a          j   :06e5[4]
    bmi tube_send_r1                                                  ; 9640: 30 0f       0.  :06e6[4]
.tube_event_handler
    pha                                                               ; 9642: 48          H   :06e8[4]
    lda #0                                                            ; 9643: a9 00       ..  :06e9[4]
    jsr tube_send_r1                                                  ; 9645: 20 f7 06     .. :06eb[4]
    tya                                                               ; 9648: 98          .   :06ee[4]
    jsr tube_send_r1                                                  ; 9649: 20 f7 06     .. :06ef[4]
    txa                                                               ; 964c: 8a          .   :06f2[4]
    jsr tube_send_r1                                                  ; 964d: 20 f7 06     .. :06f3[4]
    pla                                                               ; 9650: 68          h   :06f6[4]
; &9651 referenced 5 times by &06e6[4], &06eb[4], &06ef[4], &06f3[4], &06fa[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9651: 2c e0 fe    ,.. :06f7[4]
    bvc tube_send_r1                                                  ; 9654: 50 fb       P.  :06fa[4]
    sta tube_data_register_1                                          ; 9656: 8d e1 fe    ... :06fc[4]
    rts                                                               ; 9659: 60          `   :06ff[4]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page6, *, c955a

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page6, &0700

    ; Set the program counter to the next position in the binary file.
    org c955a + (* - tube_code_page6)


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
;   &9700: RX scout (idle listen, default handler)
;   &9C57: INACTIVE polling (pre-TX, waits for idle line)
;   &9D5B: TX data (2 bytes per NMI, tight loop if IRQ persists)
;   &9D97: TX_LAST_DATA (close frame)
;   &9DA3: TX completion (switch to RX: CR1=&82)
;   &9DC1: RX reply scout (check AP, read dest_stn)
;   &9DD7: RX reply continuation (read dest_net, validate)
;   &9DF2: RX reply validation (read src_stn/net, check FV)
;   &9E24: TX scout ACK (write dest/src addr, TX_LAST_DATA)
;   &9EEC: Four-way handshake data phase
; 
; NMI handler chain for inbound reception (scout -> data):
;   &9700: RX scout (idle listen)
;   &971F: RX scout second byte (dest_net, install &9747)
;   &9747: Scout data loop (read body in pairs, detect FV)
;   &977B: Scout completion (disable PSE, read last byte)
;   &9968: TX scout ACK
;   &9843: RX data frame (AP check, validate dest_stn/net)
;   &9859: RX data frame (validate src_net=0)
;   &986F: RX data frame (skip ctrl/port bytes)
;   &98A4: RX data bulk read (read payload into buffer)
;   &98D8: RX data completion (disable PSE, check FV, read last)
;   &9968: TX final ACK
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
; &8000 referenced 2 times by &048b[2], &9bc7
.pydis_start
.rom_header
.language_entry
l8001 = rom_header+1
l8002 = rom_header+2
    jmp language_handler                                              ; 8000: 4c d4 80    L..

; &8001 referenced 1 time by &0490[2]
; &8002 referenced 1 time by &0495[2]
; &8003 referenced 1 time by &049a[2]
.service_entry
l8004 = service_entry+1
    jmp service_handler                                               ; 8003: 4c ea 80    L..

; &8004 referenced 1 time by &049d[2]
; &8006 referenced 1 time by &0482[2]
.rom_type
    equb &82                                                          ; 8006: 82          .
; &8007 referenced 1 time by &0487[2]
.copyright_offset
    equb copyright - rom_header                                       ; 8007: 0c          .
; &8008 referenced 2 times by &81d4, &81dd
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
.l800d
l8014 = l800d+7
    equs "(C)ROFF", 0                                                 ; 800d: 28 43 29... (C)
; &8014 referenced 1 time by &84d0
    equb &0d, &18                                                     ; 8015: 0d 18       ..
    equs "'1119E"                                                     ; 8017: 27 31 31... '11
    equb 1, 0, &35                                                    ; 801d: 01 00 35    ..5
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at &80DA.
; See dispatch_hi (&8044) for the corresponding high bytes.
; Indexed by service number (1-13), language reason (14-18),
; or *NET command (33-36), with a base offset added by the caller.
; &8020 referenced 1 time by &80e3
.dispatch_lo
    equb 3                                                            ; 8020: 03          .
    equb <(return_2-1)                                                ; 8021: 6b          k
    equb <(svc_abs_workspace-1)                                       ; 8022: a1          .
    equb <(sub_c82ab-1)                                               ; 8023: aa          .
    equb <(svc_autoboot-1)                                            ; 8024: 02          .
    equb <(sub_c8179-1)                                               ; 8025: 78          x
    equb <(svc_unknown_irq-1)                                         ; 8026: 6b          k
    equb <(return_2-1)                                                ; 8027: 6b          k
    equb <(dispatch_net_cmd-1)                                        ; 8028: 68          h
    equb <(osword_fs_entry-1)                                         ; 8029: 75          u
    equb <(svc_help-1)                                                ; 802a: ec          .
    equb <(return_2-1)                                                ; 802b: 6b          k
    equb <(svc_nmi_claim-1)                                           ; 802c: 68          h
    equb <(svc_nmi_release-1)                                         ; 802d: 65          e
    equb <(insert_remote_key-1)                                       ; 802e: b7          .
    equb <(remote_boot_handler-1)                                     ; 802f: 69          i
    equb <(save_palette_vdu-1)                                        ; 8030: 9e          .
    equb <(execute_at_0100-1)                                         ; 8031: 97          .
    equb <(remote_validated-1)                                        ; 8032: a7          .
    equb <(opt_handler-1)                                             ; 8033: c9          .
    equb <(eof_handler-1)                                             ; 8034: 4b          K
    equb <(sub_c8dbf-1)                                               ; 8035: be          .
    equb <(fscv_star_handler-1)                                       ; 8036: b5          .
    equb <(sub_c8dbf-1)                                               ; 8037: be          .
    equb <(cat_handler-1)                                             ; 8038: 01          .
    equb <(fscv_shutdown-1)                                           ; 8039: 36          6
    equb <(fscv_read_handles-1)                                       ; 803a: 4b          K
    equb <(sub_c8d57-1)                                               ; 803b: 56          V
    equb <(copy_handles_and_boot-1)                                   ; 803c: 1f          .
    equb <(copy_handles-1)                                            ; 803d: 20
    equb <(sub_c8e1a-1)                                               ; 803e: 19          .
    equb <(notify_and_exec-1)                                         ; 803f: c4          .
    equb <(sub_c8e15-1)                                               ; 8040: 14          .
    equb <(net1_read_handle-1)                                        ; 8041: 3a          :
    equb <(sub_c8e56-1)                                               ; 8042: 55          U
    equb <(sub_c8e66-1)                                               ; 8043: 65          e
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_lo (&8020). Together they form a table of
; 37 handler addresses, used via the PHA/PHA/RTS trick at &80DA.
; &8044 referenced 1 time by &80df
.dispatch_hi
    equb <(resume_after_remote-1)                                     ; 8044: 7f          .
    equb >(return_2-1)                                                ; 8045: 81          .
    equb >(svc_abs_workspace-1)                                       ; 8046: 82          .
    equb >(sub_c82ab-1)                                               ; 8047: 82          .
    equb >(svc_autoboot-1)                                            ; 8048: 82          .
    equb >(sub_c8179-1)                                               ; 8049: 81          .
    equb >(svc_unknown_irq-1)                                         ; 804a: 96          .
    equb >(return_2-1)                                                ; 804b: 81          .
    equb >(dispatch_net_cmd-1)                                        ; 804c: 80          .
    equb >(osword_fs_entry-1)                                         ; 804d: 8e          .
    equb >(svc_help-1)                                                ; 804e: 81          .
    equb >(return_2-1)                                                ; 804f: 81          .
    equb >(svc_nmi_claim-1)                                           ; 8050: 96          .
    equb >(svc_nmi_release-1)                                         ; 8051: 96          .
    equb >(insert_remote_key-1)                                       ; 8052: 84          .
    equb >(remote_boot_handler-1)                                     ; 8053: 84          .
    equb >(save_palette_vdu-1)                                        ; 8054: 92          .
    equb >(execute_at_0100-1)                                         ; 8055: 84          .
    equb >(remote_validated-1)                                        ; 8056: 84          .
    equb >(opt_handler-1)                                             ; 8057: 89          .
    equb >(eof_handler-1)                                             ; 8058: 88          .
    equb >(sub_c8dbf-1)                                               ; 8059: 8d          .
    equb >(fscv_star_handler-1)                                       ; 805a: 8b          .
    equb >(sub_c8dbf-1)                                               ; 805b: 8d          .
    equb >(cat_handler-1)                                             ; 805c: 8c          .
    equb >(fscv_shutdown-1)                                           ; 805d: 83          .
    equb >(fscv_read_handles-1)                                       ; 805e: 86          .
    equb >(sub_c8d57-1)                                               ; 805f: 8d          .
    equb >(copy_handles_and_boot-1)                                   ; 8060: 8e          .
    equb >(copy_handles-1)                                            ; 8061: 8e          .
    equb >(sub_c8e1a-1)                                               ; 8062: 8e          .
    equb >(notify_and_exec-1)                                         ; 8063: 8d          .
    equb >(sub_c8e15-1)                                               ; 8064: 8e          .
    equb >(net1_read_handle-1)                                        ; 8065: 8e          .
    equb >(sub_c8e56-1)                                               ; 8066: 8e          .
    equb >(sub_c8e66-1)                                               ; 8067: 8e          .
    equb >(resume_after_remote-1)                                     ; 8068: 81          .

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
; *NET1 (&8E3B): read file handle from received
; packet (net1_read_handle)
; 
; *NET2 (&8DC2): read handle entry from workspace
; (net2_read_handle_entry)
; 
; *NET3 (&8DE0): close handle / mark as unused
; (net3_close_handle)
; 
; *NET4 (&8DEB): resume after remote operation
; (net4_resume_remote)
; ***************************************************************************************
.dispatch_net_cmd
    lda l00ef                                                         ; 8069: a5 ef       ..             ; Read command character following *NET
    sbc #&31 ; '1'                                                    ; 806b: e9 31       .1             ; Subtract ASCII '1' to get 0-based command index
    bmi return_1                                                      ; 806d: 30 7a       0z
    cmp #4                                                            ; 806f: c9 04       ..
    bcs return_1                                                      ; 8071: b0 76       .v
    tax                                                               ; 8073: aa          .
    lda #0                                                            ; 8074: a9 00       ..
    sta rom_svc_num                                                   ; 8076: 85 ce       ..
    tya                                                               ; 8078: 98          .
    ldy #&20 ; ' '                                                    ; 8079: a0 20       .              ; Y=&20: base offset for *NET commands (index 33+)
    bne dispatch                                                      ; 807b: d0 5d       .]             ; ALWAYS branch

; &807d referenced 1 time by &8082
.loop_c807d
    iny                                                               ; 807d: c8          .
; ***************************************************************************************
; "I AM" command handler
; 
; Dispatched from the command match table when the user types
; "*I AM <station>" or "*I AM <station>.<network>". Also used as
; the station number parser for "*NET <station>[.<network>]".
; Skips leading spaces, then parses a decimal station number (and
; optional network number after '.') via parse_decimal. Stores
; the results in &0E00 (station) and &0E01 (network). If a colon
; follows, reads interactive input via OSRDCH and appends it to
; the command buffer. Finally jumps to forward_star_cmd.
; ***************************************************************************************
.i_am_handler
    lda (fs_options),y                                                ; 807e: b1 bb       ..
    cmp #&20 ; ' '                                                    ; 8080: c9 20       .
    beq loop_c807d                                                    ; 8082: f0 f9       ..
    cmp #&41 ; 'A'                                                    ; 8084: c9 41       .A
    bcs c8099                                                         ; 8086: b0 11       ..
    lda #0                                                            ; 8088: a9 00       ..
    jsr parse_decimal                                                 ; 808a: 20 f3 85     ..            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc c8093                                                         ; 808d: 90 04       ..
    iny                                                               ; 808f: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8090: 20 f3 85     ..            ; Parse decimal number from (fs_options),Y (DECIN)
; &8093 referenced 1 time by &808d
.c8093
    sta fs_server_stn                                                 ; 8093: 8d 00 0e    ...            ; A=parsed value (accumulated in &B2)
    stx fs_server_net                                                 ; 8096: 8e 01 0e    ...            ; X=corrupted
; &8099 referenced 2 times by &8086, &80a2
.c8099
    iny                                                               ; 8099: c8          .
    lda (fs_options),y                                                ; 809a: b1 bb       ..
    cmp #&0d                                                          ; 809c: c9 0d       ..
    beq forward_star_cmd                                              ; 809e: f0 14       ..
    cmp #&3a ; ':'                                                    ; 80a0: c9 3a       .:
    bne c8099                                                         ; 80a2: d0 f5       ..
    jsr oswrch                                                        ; 80a4: 20 ee ff     ..            ; Write character
; &80a7 referenced 1 time by &80af
.loop_c80a7
    jsr osrdch                                                        ; 80a7: 20 e0 ff     ..            ; Read a character from the current input stream
    sta (fs_options),y                                                ; 80aa: 91 bb       ..             ; A=character read
    iny                                                               ; 80ac: c8          .
    cmp #&0d                                                          ; 80ad: c9 0d       ..
    bne loop_c80a7                                                    ; 80af: d0 f6       ..
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
; and catch-all entries in the command match table at &8BE4, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; ***************************************************************************************
; &80b4 referenced 1 time by &809e
.forward_star_cmd
    jsr sub_c8d43                                                     ; 80b4: 20 43 8d     C.
    tay                                                               ; 80b7: a8          .              ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 80b8: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    ldx fs_cmd_csd                                                    ; 80bb: ae 03 0f    ...            ; X=depends on function
    beq return_1                                                      ; 80be: f0 29       .)
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
    jsr l859c                                                         ; 80c7: 20 9c 85     ..            ; Store A/X/Y in FS workspace
    cmp #8                                                            ; 80ca: c9 08       ..
    bcs return_1                                                      ; 80cc: b0 1b       ..             ; Function code >= 8? Return (unsupported)
    tax                                                               ; 80ce: aa          .
    tya                                                               ; 80cf: 98          .
    ldy #&12                                                          ; 80d0: a0 12       ..             ; Y=&12: base offset for FSCV dispatch (indices 19+)
    bne dispatch                                                      ; 80d2: d0 06       ..             ; ALWAYS branch

; ***************************************************************************************
; Language entry dispatcher
; 
; Called when the NFS ROM is entered as a language. X = reason code
; (0-4). Dispatches via table indices 14-18 (base offset Y=&0D).
; ***************************************************************************************
; &80d4 referenced 1 time by &8000
.language_handler
    cpx #5                                                            ; 80d4: e0 05       ..
    bcs return_1                                                      ; 80d6: b0 11       ..
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
; &80da referenced 5 times by &807b, &80c5, &80d2, &80dc, &8160
.dispatch
    inx                                                               ; 80da: e8          .              ; Add base offset Y to index X (loop: X += Y+1)
    dey                                                               ; 80db: 88          .
    bpl dispatch                                                      ; 80dc: 10 fc       ..
    tay                                                               ; 80de: a8          .
    lda dispatch_hi,x                                                 ; 80df: bd 44 80    .D.            ; Load high byte of (handler - 1) from table
    pha                                                               ; 80e2: 48          H              ; Push high byte onto stack
    lda dispatch_lo,x                                                 ; 80e3: bd 20 80    . .            ; Load low byte of (handler - 1) from table
    pha                                                               ; 80e6: 48          H              ; Push low byte onto stack
    ldx fs_options                                                    ; 80e7: a6 bb       ..             ; Restore X (fileserver options) for use by handler
; &80e9 referenced 6 times by &806d, &8071, &80be, &80cc, &80d6, &80f2
.return_1
    rts                                                               ; 80e9: 60          `              ; RTS pops address, adds 1, jumps to handler

; ***************************************************************************************
; Service handler entry
; 
; Dispatches service calls. 3.35K removes the per-ROM disable
; flag check at &0DF0+X that was present in 3.35D.
;   &FE: Tube init -- explode character definitions (OSBYTE &14, X=6)
;   &FF: Full init -- table-driven vector setup, copy NMI handler
;        code from ROM to RAM pages &04-&06, copy workspace init to
;        &0016-&0076, then fall through to select NFS.
;   &12 with Y=5: Select NFS as active filing system.
; All other service calls < &0D dispatch via c80da.
; ***************************************************************************************
; &80ea referenced 1 time by &8003
.service_handler
    cmp #&fe                                                          ; 80ea: c9 fe       ..
    bcc c8146                                                         ; 80ec: 90 58       .X
    bne init_vectors_and_copy                                         ; 80ee: d0 13       ..
    cpy #0                                                            ; 80f0: c0 00       ..
    beq return_1                                                      ; 80f2: f0 f5       ..
    stx zp_temp_11                                                    ; 80f4: 86 11       ..
    sty zp_temp_10                                                    ; 80f6: 84 10       ..
    ldx #6                                                            ; 80f8: a2 06       ..
    lda #osbyte_explode_chars                                         ; 80fa: a9 14       ..
    jsr osbyte                                                        ; 80fc: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
    ldx zp_temp_11                                                    ; 80ff: a6 11       ..
    bne c8142                                                         ; 8101: d0 3f       .?
; ***************************************************************************************
; NFS initialisation (service &FF: full reset)
; 
; New in 3.35D: table-driven vector initialisation replaces
; the hardcoded LDA/STA pairs of 3.34B. Reads 4 triplets from
; the data table at &816D (low byte, high byte, vector offset)
; and stores each 16-bit value at &0200+offset:
;   EVNTV (&0220) = &06E8   BRKV  (&0202) = &0016
;   RDCHV (&0210) = &04E7   WRCHV (&020E) = &051C
; Then writes &8E to Tube control register (&FEE0) and copies
; 3 pages of Tube host code from ROM (&935A/&945A/&955A)
; to RAM (&0400/&0500/&0600), calls tube_post_init (&0414),
; and copies 97 bytes of workspace init from ROM (&9315) to
; &0016-&0076.
; ***************************************************************************************
; &8103 referenced 1 time by &80ee
.init_vectors_and_copy
    sty zp_temp_10                                                    ; 8103: 84 10       ..
    ldy #&0c                                                          ; 8105: a0 0c       ..
; &8107 referenced 1 time by &8119
.loop_c8107
    ldx return_2,y                                                    ; 8107: be 6c 81    .l.
    dey                                                               ; 810a: 88          .
    lda return_2,y                                                    ; 810b: b9 6c 81    .l.
    sta userv+1,x                                                     ; 810e: 9d 01 02    ...
    dey                                                               ; 8111: 88          .
    lda return_2,y                                                    ; 8112: b9 6c 81    .l.
    sta userv,x                                                       ; 8115: 9d 00 02    ...
    dey                                                               ; 8118: 88          .
    bne loop_c8107                                                    ; 8119: d0 ec       ..
    lda #&8e                                                          ; 811b: a9 8e       ..
    sta tube_status_1_and_tube_control                                ; 811d: 8d e0 fe    ...
; Copy NMI handler code from ROM to RAM pages &04-&06
; &8120 referenced 1 time by &8133
.cloop
    lda c935a,y                                                       ; 8120: b9 5a 93    .Z.
    sta tube_code_page4,y                                             ; 8123: 99 00 04    ...
    lda l945a,y                                                       ; 8126: b9 5a 94    .Z.
    sta tube_dispatch_table,y                                         ; 8129: 99 00 05    ...
    lda c955a,y                                                       ; 812c: b9 5a 95    .Z.
    sta tube_code_page6,y                                             ; 812f: 99 00 06    ...
    dey                                                               ; 8132: 88          .
    bne cloop                                                         ; 8133: d0 eb       ..
    jsr tube_post_init                                                ; 8135: 20 14 04     ..
    ldx #&60 ; '`'                                                    ; 8138: a2 60       .`
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &813a referenced 1 time by &8140
.loop_c813a
    lda c9315,x                                                       ; 813a: bd 15 93    ...
    sta nmi_workspace_start,x                                         ; 813d: 95 16       ..
    dex                                                               ; 813f: ca          .
    bpl loop_c813a                                                    ; 8140: 10 f8       ..
; &8142 referenced 1 time by &8101
.c8142
    ldy zp_temp_10                                                    ; 8142: a4 10       ..
    lda #0                                                            ; 8144: a9 00       ..
; &8146 referenced 1 time by &80ec
.c8146
    cmp #&12                                                          ; 8146: c9 12       ..
    bne c814e                                                         ; 8148: d0 04       ..
    cpy #5                                                            ; 814a: c0 05       ..
    beq select_nfs                                                    ; 814c: f0 67       .g
; &814e referenced 1 time by &8148
.c814e
    cmp #&0d                                                          ; 814e: c9 0d       ..
    bcs return_2                                                      ; 8150: b0 1a       ..
    tax                                                               ; 8152: aa          .
    lda rom_svc_num                                                   ; 8153: a5 ce       ..
    pha                                                               ; 8155: 48          H
    lda nfs_temp                                                      ; 8156: a5 cd       ..
    pha                                                               ; 8158: 48          H
    stx rom_svc_num                                                   ; 8159: 86 ce       ..
    sty nfs_temp                                                      ; 815b: 84 cd       ..
    tya                                                               ; 815d: 98          .
    ldy #0                                                            ; 815e: a0 00       ..
    jsr dispatch                                                      ; 8160: 20 da 80     ..
    ldx rom_svc_num                                                   ; 8163: a6 ce       ..
    pla                                                               ; 8165: 68          h
    sta nfs_temp                                                      ; 8166: 85 cd       ..
; ***************************************************************************************
; Service 4: unrecognised * command
; 
; Matches the command text against ROM string table entries.
; Both entries reuse bytes from the ROM header to save space:
; 
;   X=8: matches "ROFF" at &8010 — the suffix of the
;        copyright string "(C)ROFF" → *ROFF (Remote Off,
;        end remote session) — jumps to resume_after_remote
; 
;   X=1: matches "NET" at &8009 — the ROM title string
;        → *NET (select NFS) — falls through to select_nfs
; 
; If neither matches, returns with the service call
; unclaimed.
; ***************************************************************************************
.svc_star_command
    pla                                                               ; 8168: 68          h
    sta rom_svc_num                                                   ; 8169: 85 ce       ..
    txa                                                               ; 816b: 8a          .
; &816c referenced 4 times by &8107, &810b, &8112, &8150
.return_2
    rts                                                               ; 816c: 60          `

    equb &1c, 5, &0e, &e7, 4, &10, &16, 0, 2, &e8, 6, &20             ; 816d: 1c 05 0e... ...

.sub_c8179
    ldx #8                                                            ; 8179: a2 08       ..
    jsr match_rom_string                                              ; 817b: 20 cc 81     ..
    bne c81ae                                                         ; 817e: d0 2e       ..
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
.resume_after_remote
    ldy #4                                                            ; 8180: a0 04       ..
    lda (net_rx_ptr),y                                                ; 8182: b1 9c       ..
    beq c81a7                                                         ; 8184: f0 21       .!
    lda #0                                                            ; 8186: a9 00       ..
    tax                                                               ; 8188: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 8189: 91 9c       ..
    tay                                                               ; 818b: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 818c: a9 c9       ..
    jsr osbyte                                                        ; 818e: 20 f4 ff     ..            ; Enable keyboard (for Econet)
    lda #&0a                                                          ; 8191: a9 0a       ..
    jsr setup_tx_and_send                                             ; 8193: 20 b8 90     ..
; &8196 referenced 1 time by &8489
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 8196: 86 9e       ..
    lda #&ce                                                          ; 8198: a9 ce       ..
; &819a referenced 1 time by &81a5
.loop_c819a
    ldx nfs_workspace                                                 ; 819a: a6 9e       ..
    ldy #&7f                                                          ; 819c: a0 7f       ..
    jsr osbyte                                                        ; 819e: 20 f4 ff     ..
    adc #1                                                            ; 81a1: 69 01       i.
    cmp #&d0                                                          ; 81a3: c9 d0       ..
    beq loop_c819a                                                    ; 81a5: f0 f3       ..
; &81a7 referenced 1 time by &8184
.c81a7
    lda #0                                                            ; 81a7: a9 00       ..
    sta rom_svc_num                                                   ; 81a9: 85 ce       ..
    sta nfs_workspace                                                 ; 81ab: 85 9e       ..
    rts                                                               ; 81ad: 60          `

; &81ae referenced 1 time by &817e
.c81ae
    ldx #1                                                            ; 81ae: a2 01       ..
    jsr match_rom_string                                              ; 81b0: 20 cc 81     ..
    bne c81fb                                                         ; 81b3: d0 46       .F
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
; &81b5 referenced 1 time by &814c
.select_nfs
    jsr call_fscv_shutdown                                            ; 81b5: 20 fe 81     ..
    sec                                                               ; 81b8: 38          8
    ror nfs_temp                                                      ; 81b9: 66 cd       f.
    jsr issue_vectors_claimed                                         ; 81bb: 20 61 82     a.
    ldy #&1d                                                          ; 81be: a0 1d       ..
; &81c0 referenced 1 time by &81c8
.initl
    lda (net_rx_ptr),y                                                ; 81c0: b1 9c       ..
    sta fs_state_deb,y                                                ; 81c2: 99 eb 0d    ...
    dey                                                               ; 81c5: 88          .
    cpy #&14                                                          ; 81c6: c0 14       ..
    bne initl                                                         ; 81c8: d0 f6       ..
    beq c824a                                                         ; 81ca: f0 7e       .~             ; ALWAYS branch

; ***************************************************************************************
; Match command text against ROM string table
; 
; Compares characters from (os_text_ptr)+Y against bytes starting
; at binary_version+X (&8008+X). Input is uppercased via AND &DF.
; Returns with Z=1 if the ROM string's NUL terminator was reached
; (match), or Z=0 if a mismatch was found. On match, Y points
; past the matched text; on return, skips trailing spaces.
; ***************************************************************************************
; &81cc referenced 2 times by &817b, &81b0
.match_rom_string
    ldy nfs_temp                                                      ; 81cc: a4 cd       ..
; &81ce referenced 1 time by &81db
.loop_c81ce
    lda (os_text_ptr),y                                               ; 81ce: b1 f2       ..
    and #&df                                                          ; 81d0: 29 df       ).
    beq cmd_name_matched                                              ; 81d2: f0 09       ..
    cmp binary_version,x                                              ; 81d4: dd 08 80    ...
    bne cmd_name_matched                                              ; 81d7: d0 04       ..
    iny                                                               ; 81d9: c8          .
    inx                                                               ; 81da: e8          .
    bne loop_c81ce                                                    ; 81db: d0 f1       ..
; &81dd referenced 2 times by &81d2, &81d7
.cmd_name_matched
    lda binary_version,x                                              ; 81dd: bd 08 80    ...
    beq skip_cmd_spaces                                               ; 81e0: f0 02       ..
    rts                                                               ; 81e2: 60          `

; &81e3 referenced 1 time by &81e8
.skpspi
    iny                                                               ; 81e3: c8          .
; &81e4 referenced 1 time by &81e0
.skip_cmd_spaces
    lda (os_text_ptr),y                                               ; 81e4: b1 f2       ..
    cmp #&20 ; ' '                                                    ; 81e6: c9 20       .
    beq skpspi                                                        ; 81e8: f0 f9       ..
    eor #&0d                                                          ; 81ea: 49 0d       I.
    rts                                                               ; 81ec: 60          `

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_help
    jsr print_inline                                                  ; 81ed: 20 d9 85     ..
    equs &0d, "NFS 3.35K", &0d                                        ; 81f0: 0d 4e 46... .NF

; &81fb referenced 2 times by &81b3, &8210
.c81fb
    ldy nfs_temp                                                      ; 81fb: a4 cd       ..
    rts                                                               ; 81fd: 60          `

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &81fe referenced 2 times by &81b5, &8203
.call_fscv_shutdown
    lda #6                                                            ; 81fe: a9 06       ..
    jmp (fscv)                                                        ; 8200: 6c 1e 02    l..

; ***************************************************************************************
; Service 3: auto-boot
; 
; Notifies current FS of shutdown via FSCV A=6. Scans keyboard
; (OSBYTE &7A): if no key is pressed, auto-boot proceeds; if the
; 'N' key is pressed (matrix address &55), the boot is declined
; and the key is forgotten via OSBYTE &78. Any other key also
; declines. Prints "Econet Station <n>" and checks the ADLC SR2
; for the network clock signal — prints "No Clock" if absent (no
; network communication possible without it). Then falls through
; to set up NFS vectors (selecting NFS as the filing system).
; ***************************************************************************************
.svc_autoboot
    jsr call_fscv_shutdown                                            ; 8203: 20 fe 81     ..
    lda #osbyte_scan_keyboard_from_16                                 ; 8206: a9 7a       .z
    jsr osbyte                                                        ; 8208: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 820b: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi c8218                                                         ; 820c: 30 0a       0.
; ***************************************************************************************
; Set up filing system vectors
; 
; Copies 14 bytes from fs_vector_addrs (&8280) into FILEV-FSCV (&0212).
; These set all 7 filing system vectors to the standard extended vector
; dispatch addresses (&FF1B, &FF1E, &FF21, &FF24, &FF27, &FF2A, &FF2D).
; Then calls setup_rom_ptrs_netv to install the extended vector table
; entries with the actual NFS handler addresses, and issues service
; requests to notify other ROMs.
; ***************************************************************************************
.setup_fs_vectors
    eor #&55 ; 'U'                                                    ; 820e: 49 55       IU             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
    bne c81fb                                                         ; 8210: d0 e9       ..
    tay                                                               ; 8212: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 8213: a9 78       .x
    jsr osbyte                                                        ; 8215: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; &8218 referenced 1 time by &820c
.c8218
    jsr print_inline                                                  ; 8218: 20 d9 85     ..
    equs "Econet Station "                                            ; 821b: 45 63 6f... Eco

    ldy #&14                                                          ; 822a: a0 14       ..
    lda (net_rx_ptr),y                                                ; 822c: b1 9c       ..
    jsr print_decimal                                                 ; 822e: 20 7e 8d     ~.
    lda #&20 ; ' '                                                    ; 8231: a9 20       .
    bit econet_control23_or_status2                                   ; 8233: 2c a1 fe    ,..
    beq c8245                                                         ; 8236: f0 0d       ..
    jsr print_inline                                                  ; 8238: 20 d9 85     ..
    equs " No Clock"                                                  ; 823b: 20 4e 6f...  No

    nop                                                               ; 8244: ea          .
; &8245 referenced 1 time by &8236
.c8245
    jsr print_inline                                                  ; 8245: 20 d9 85     ..
    equs &0d, &0d                                                     ; 8248: 0d 0d       ..

; &824a referenced 1 time by &81ca
.c824a
    ldy #&0d                                                          ; 824a: a0 0d       ..
; &824c referenced 1 time by &8253
.dofsl1
    lda fs_vector_addrs,y                                             ; 824c: b9 80 82    ...
    sta filev,y                                                       ; 824f: 99 12 02    ...
    dey                                                               ; 8252: 88          .
    bpl dofsl1                                                        ; 8253: 10 f7       ..
    jsr setup_rom_ptrs_netv                                           ; 8255: 20 0b 83     ..
    ldy #&1b                                                          ; 8258: a0 1b       ..
    ldx #7                                                            ; 825a: a2 07       ..
    jsr store_rom_ptr_pair                                            ; 825c: 20 1f 83     ..
    stx rom_svc_num                                                   ; 825f: 86 ce       ..
; ***************************************************************************************
; Issue 'vectors claimed' service and optionally auto-boot
; 
; Issues service &0F (vectors claimed) via OSBYTE &8F, then
; service &0A. If nfs_temp is zero (auto-boot not inhibited),
; sets up the command string "I .BOOT" at &8246 and jumps to
; the FSCV 3 unrecognised-command handler (which matches against
; the command table at &8BE4). The "I." prefix triggers the
; catch-all entry which forwards the command to the fileserver.
; ***************************************************************************************
; &8261 referenced 1 time by &81bb
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 8261: a9 8f       ..
    ldx #&0f                                                          ; 8263: a2 0f       ..
    jsr osbyte                                                        ; 8265: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 8268: a2 0a       ..
    jsr osbyte                                                        ; 826a: 20 f4 ff     ..
    ldx nfs_temp                                                      ; 826d: a6 cd       ..
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
.svc_private_workspace
    bne return_3                                                      ; 826f: d0 37       .7
    ldx #&78 ; 'x'                                                    ; 8271: a2 78       .x
; &8273 referenced 2 times by &831f, &8325
.c8273
    ldy #&82                                                          ; 8273: a0 82       ..
    jmp fscv_star_handler                                             ; 8275: 4c b6 8b    L..

    equs "I .BOOT"                                                    ; 8278: 49 20 2e... I .
    equb &0d                                                          ; 827f: 0d          .
; &8280 referenced 1 time by &824c
.fs_vector_addrs
    equb &1b, &ff, &1e, &ff, &21, &ff, &24, &ff, &27, &ff, &2a, &ff   ; 8280: 1b ff 1e... ...
    equb &2d, &ff, &de, &86, &4a,   7, &89, &44, &2e, &85, &57, &dc   ; 828c: 2d ff de... -..
    equb &83, &42, &0e, &8a, &41, &6f, &89, &52, &c7, &80             ; 8298: 83 42 0e... .B.

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; ***************************************************************************************
.svc_abs_workspace
    cpy #&10                                                          ; 82a2: c0 10       ..
    bcs return_3                                                      ; 82a4: b0 02       ..
    ldy #&10                                                          ; 82a6: a0 10       ..
; &82a8 referenced 2 times by &826f, &82a4
.return_3
    rts                                                               ; 82a8: 60          `

    equb &74, &90                                                     ; 82a9: 74 90       t.

.sub_c82ab
    sty net_rx_ptr_hi                                                 ; 82ab: 84 9d       ..
    iny                                                               ; 82ad: c8          .
    sty nfs_workspace_hi                                              ; 82ae: 84 9f       ..
    lda #0                                                            ; 82b0: a9 00       ..
    ldy #4                                                            ; 82b2: a0 04       ..
    sta (net_rx_ptr),y                                                ; 82b4: 91 9c       ..
    ldy #&ff                                                          ; 82b6: a0 ff       ..
    sta net_rx_ptr                                                    ; 82b8: 85 9c       ..
    sta nfs_workspace                                                 ; 82ba: 85 9e       ..
    sta nfs_temp                                                      ; 82bc: 85 cd       ..
    sta tx_clear_flag                                                 ; 82be: 8d 62 0d    .b.
    tax                                                               ; 82c1: aa          .              ; X=&00
    lda #osbyte_read_write_last_break_type                            ; 82c2: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 82c4: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 82c7: 8a          .              ; X=value of type of last reset
    beq c82fc                                                         ; 82c8: f0 32       .2             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 82ca: a0 15       ..
    lda #&fe                                                          ; 82cc: a9 fe       ..
    sta fs_server_stn                                                 ; 82ce: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 82d1: 91 9c       ..
    lda #0                                                            ; 82d3: a9 00       ..
    sta fs_server_net                                                 ; 82d5: 8d 01 0e    ...
    sta prot_status                                                   ; 82d8: 8d 63 0d    .c.
    sta fs_messages_flag                                              ; 82db: 8d 06 0e    ...
    sta fs_boot_option                                                ; 82de: 8d 05 0e    ...
    iny                                                               ; 82e1: c8          .              ; Y=&16
    sta (net_rx_ptr),y                                                ; 82e2: 91 9c       ..
    ldy #3                                                            ; 82e4: a0 03       ..
    sta (nfs_workspace),y                                             ; 82e6: 91 9e       ..
    dey                                                               ; 82e8: 88          .              ; Y=&02
    lda #&eb                                                          ; 82e9: a9 eb       ..
    sta (nfs_workspace),y                                             ; 82eb: 91 9e       ..
; &82ed referenced 1 time by &82fa
.loop_c82ed
    lda nfs_temp                                                      ; 82ed: a5 cd       ..
    jsr calc_handle_offset                                            ; 82ef: 20 44 8e     D.
    bcs c82fc                                                         ; 82f2: b0 08       ..
    lda #&3f ; '?'                                                    ; 82f4: a9 3f       .?
    sta (nfs_workspace),y                                             ; 82f6: 91 9e       ..
    inc nfs_temp                                                      ; 82f8: e6 cd       ..
    bne loop_c82ed                                                    ; 82fa: d0 f1       ..
; &82fc referenced 2 times by &82c8, &82f2
.c82fc
    lda station_id_disable_net_nmis                                   ; 82fc: ad 18 fe    ...            ; Read station ID (also INTOFF)
    ldy #&14                                                          ; 82ff: a0 14       ..
    sta (net_rx_ptr),y                                                ; 8301: 91 9c       ..
    jsr trampoline_adlc_init                                          ; 8303: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 8306: a9 40       .@
    sta rx_flags                                                      ; 8308: 8d 64 0d    .d.
; ***************************************************************************************
; Set up ROM pointer table and NETV
; 
; Reads the ROM pointer table base address via OSBYTE &A8, stores
; it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
; one 3-byte extended vector entry (addr=&9074, rom=current) into
; the ROM pointer table at offset &36, installing osword_dispatch
; as the NETV handler.
; ***************************************************************************************
; &830b referenced 1 time by &8255
.setup_rom_ptrs_netv
    lda #osbyte_read_rom_ptr_table_low                                ; 830b: a9 a8       ..
    ldx #0                                                            ; 830d: a2 00       ..
    ldy #&ff                                                          ; 830f: a0 ff       ..
    jsr osbyte                                                        ; 8311: 20 f4 ff     ..            ; Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 8314: 86 f6       ..             ; X=value of address of ROM pointer table (low byte)
    sty l00f7                                                         ; 8316: 84 f7       ..             ; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 8318: a0 36       .6
    sty netv                                                          ; 831a: 8c 24 02    .$.
    ldx #1                                                            ; 831d: a2 01       ..
; &831f referenced 2 times by &825c, &8331
.store_rom_ptr_pair
    lda c8273,y                                                       ; 831f: b9 73 82    .s.
    sta (osrdsc_ptr),y                                                ; 8322: 91 f6       ..
    iny                                                               ; 8324: c8          .
    lda c8273,y                                                       ; 8325: b9 73 82    .s.
    sta (osrdsc_ptr),y                                                ; 8328: 91 f6       ..
    iny                                                               ; 832a: c8          .
    lda romsel_copy                                                   ; 832b: a5 f4       ..
    sta (osrdsc_ptr),y                                                ; 832d: 91 f6       ..
    iny                                                               ; 832f: c8          .
    dex                                                               ; 8330: ca          .
    bne store_rom_ptr_pair                                            ; 8331: d0 ec       ..
    ldy nfs_workspace_hi                                              ; 8333: a4 9f       ..
    iny                                                               ; 8335: c8          .
    rts                                                               ; 8336: 60          `

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
.fscv_shutdown
    ldy #&1d                                                          ; 8337: a0 1d       ..
; &8339 referenced 1 time by &8341
.fsdiel
    lda fs_state_deb,y                                                ; 8339: b9 eb 0d    ...
    sta (net_rx_ptr),y                                                ; 833c: 91 9c       ..
    dey                                                               ; 833e: 88          .
    cpy #&14                                                          ; 833f: c0 14       ..
    bne fsdiel                                                        ; 8341: d0 f6       ..
    lda #osbyte_printer_driver_going_dormant                          ; 8343: a9 7b       .{
    jmp osbyte                                                        ; 8345: 4c f4 ff    L..            ; Printer driver going dormant

; &8348 referenced 1 time by &83bb
.sub_c8348
    lda #&90                                                          ; 8348: a9 90       ..
; &834a referenced 1 time by &883b
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 834a: 20 56 83     V.
    sta l00c1                                                         ; 834d: 85 c1       ..
    lda #3                                                            ; 834f: a9 03       ..
    sta l00c4                                                         ; 8351: 85 c4       ..
    dec l00c0                                                         ; 8353: c6 c0       ..
    rts                                                               ; 8355: 60          `

; ***************************************************************************************
; Initialise TX control block at &00C0 from template
; 
; Copies 12 bytes from tx_ctrl_template (&836E) to &00C0.
; For the first 2 bytes (Y=0,1), also copies the fileserver
; station/network from &0E00/&0E01 to &00C2/&00C3.
; The template sets up: control=&80, port=&99 (FS command port),
; command data length=&0F, plus padding bytes.
; ***************************************************************************************
; &8356 referenced 4 times by &834a, &83aa, &83f5, &8feb
.init_tx_ctrl_block
    pha                                                               ; 8356: 48          H
    ldy #&0b                                                          ; 8357: a0 0b       ..
; &8359 referenced 1 time by &836a
.fstxl1
    lda tx_ctrl_template,y                                            ; 8359: b9 6e 83    .n.
    sta l00c0,y                                                       ; 835c: 99 c0 00    ...
    cpy #2                                                            ; 835f: c0 02       ..
    bpl fstxl2                                                        ; 8361: 10 06       ..
    lda fs_server_stn,y                                               ; 8363: b9 00 0e    ...
    sta l00c2,y                                                       ; 8366: 99 c2 00    ...
; &8369 referenced 1 time by &8361
.fstxl2
    dey                                                               ; 8369: 88          .
    bpl fstxl1                                                        ; 836a: 10 ed       ..
    pla                                                               ; 836c: 68          h
    rts                                                               ; 836d: 60          `

; ***************************************************************************************
; TX control block template (TXTAB, 12 bytes)
; 
; &00C0: &80 (control flag)    &00C1: &99 (port — FS command port)
; &00C2: server station        &00C3: server network
; &00C4: &00 (data low)        &00C5: &0F (data high — buffer page)
; &00C6-&00CB: &FF (FILLER)
; The &FF padding in the address fields is a recurring pattern:
; Econet control blocks use 4-byte addresses but NFS only needs
; 2-byte addresses, so the upper two bytes are filled with &FF.
; ***************************************************************************************
; &836e referenced 1 time by &8359
.tx_ctrl_template
    equb &80, &99, 0, 0, 0, &0f                                       ; 836e: 80 99 00... ...
; &8374 referenced 3 times by &88bb, &8992, &916c
.l8374
    equb &ff, &ff, &ff, &0f, &ff, &ff                                 ; 8374: ff ff ff... ...

; &837a referenced 1 time by &8a5f
.prepare_cmd_with_flag
    pha                                                               ; 837a: 48          H
    lda #&2a ; '*'                                                    ; 837b: a9 2a       .*
    sec                                                               ; 837d: 38          8
    bcs c8394                                                         ; 837e: b0 14       ..             ; ALWAYS branch

; &8380 referenced 2 times by &86fb, &87a4
.prepare_cmd_clv
    clv                                                               ; 8380: b8          .
    bvc c8393                                                         ; 8381: 50 10       P.             ; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8BE4 for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 8383: a9 77       .w
    jsr osbyte                                                        ; 8385: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #&17                                                          ; 8388: a0 17       ..             ; Y=function code for HDRFN
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
; &838a referenced 12 times by &80b8, &8860, &88d6, &8922, &8949, &89bf, &89e4, &8abe, &8b74, &8c1d, &8c54, &8cc1
.prepare_fs_cmd
    clv                                                               ; 838a: b8          .
; &838b referenced 2 times by &88be, &8995
.init_tx_ctrl_data
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 838b: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 838e: 8d 02 0f    ...
    lda #&2a ; '*'                                                    ; 8391: a9 2a       .*
; &8393 referenced 1 time by &8381
.c8393
    clc                                                               ; 8393: 18          .
; &8394 referenced 1 time by &837e
.c8394
    sty fs_cmd_y_param                                                ; 8394: 8c 01 0f    ...
    sta fs_error_ptr                                                  ; 8397: 85 b8       ..
    ldy #1                                                            ; 8399: a0 01       ..
; &839b referenced 1 time by &83a2
.loop_c839b
    lda fs_csd_handle,y                                               ; 839b: b9 03 0e    ...            ; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 839e: 99 03 0f    ...
    dey                                                               ; 83a1: 88          .              ; Y=function code
    bpl loop_c839b                                                    ; 83a2: 10 f7       ..
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
; &83a4 referenced 1 time by &8b17
.build_send_fs_cmd
    php                                                               ; 83a4: 08          .
    lda #&90                                                          ; 83a5: a9 90       ..
    sta fs_cmd_type                                                   ; 83a7: 8d 00 0f    ...
    jsr init_tx_ctrl_block                                            ; 83aa: 20 56 83     V.
    txa                                                               ; 83ad: 8a          .
    adc #5                                                            ; 83ae: 69 05       i.
    sta l00c8                                                         ; 83b0: 85 c8       ..
    plp                                                               ; 83b2: 28          (
    bcs dofsl5                                                        ; 83b3: b0 1c       ..
    php                                                               ; 83b5: 08          .
    jsr setup_tx_ptr_c0                                               ; 83b6: 20 60 86     `.
    plp                                                               ; 83b9: 28          (
; &83ba referenced 2 times by &87b4, &8a9b
.send_fs_reply_cmd
    php                                                               ; 83ba: 08          .
    jsr sub_c8348                                                     ; 83bb: 20 48 83     H.
    lda fs_error_ptr                                                  ; 83be: a5 b8       ..
    jsr send_to_fs                                                    ; 83c0: 20 ed 84     ..
    plp                                                               ; 83c3: 28          (
; &83c4 referenced 1 time by &83da
.dofsl7
    iny                                                               ; 83c4: c8          .
    lda (l00c4),y                                                     ; 83c5: b1 c4       ..
    tax                                                               ; 83c7: aa          .
    beq return_dofsl7                                                 ; 83c8: f0 06       ..
    bvc c83ce                                                         ; 83ca: 50 02       P.
    adc #&2a ; '*'                                                    ; 83cc: 69 2a       i*
; &83ce referenced 1 time by &83ca
.c83ce
    bne store_fs_error                                                ; 83ce: d0 73       .s
; &83d0 referenced 1 time by &83c8
.return_dofsl7
    rts                                                               ; 83d0: 60          `

; &83d1 referenced 1 time by &83b3
.dofsl5
    pla                                                               ; 83d1: 68          h
    ldx #&c0                                                          ; 83d2: a2 c0       ..
    iny                                                               ; 83d4: c8          .
    jsr econet_tx_retry                                               ; 83d5: 20 56 92     V.
    sta l00b3                                                         ; 83d8: 85 b3       ..
    bcc dofsl7                                                        ; 83da: 90 e8       ..
.bputv_handler
    clc                                                               ; 83dc: 18          .
; ***************************************************************************************
; Handle BPUT/BGET file byte I/O
; 
; BPUTV enters at &83DC (CLC; fall through) and BGETV enters
; at &852E (SEC; JSR here). The carry flag is preserved via
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
; &83dd referenced 1 time by &852f
.handle_bput_bget
    pha                                                               ; 83dd: 48          H
    sta l0fdf                                                         ; 83de: 8d df 0f    ...
    txa                                                               ; 83e1: 8a          .
    pha                                                               ; 83e2: 48          H
    tya                                                               ; 83e3: 98          .
    pha                                                               ; 83e4: 48          H
    php                                                               ; 83e5: 08          .
    sty l00ba                                                         ; 83e6: 84 ba       ..
    jsr handle_to_mask_clc                                            ; 83e8: 20 1c 86     ..
    sty l0fde                                                         ; 83eb: 8c de 0f    ...
    sty l00cf                                                         ; 83ee: 84 cf       ..
    ldy #&90                                                          ; 83f0: a0 90       ..
    sty fs_putb_buf                                                   ; 83f2: 8c dc 0f    ...
    jsr init_tx_ctrl_block                                            ; 83f5: 20 56 83     V.
    lda #&dc                                                          ; 83f8: a9 dc       ..
    sta l00c4                                                         ; 83fa: 85 c4       ..
    lda #&e0                                                          ; 83fc: a9 e0       ..
    sta l00c8                                                         ; 83fe: 85 c8       ..
    iny                                                               ; 8400: c8          .
    ldx #9                                                            ; 8401: a2 09       ..
    plp                                                               ; 8403: 28          (
    bcc store_retry_count                                             ; 8404: 90 01       ..
    dex                                                               ; 8406: ca          .              ; X=&08
; &8407 referenced 1 time by &8404
.store_retry_count
    stx fs_getb_buf                                                   ; 8407: 8e dd 0f    ...
    lda l0fde                                                         ; 840a: ad de 0f    ...
    ldx #&c0                                                          ; 840d: a2 c0       ..
    jsr econet_tx_retry                                               ; 840f: 20 56 92     V.
    ldx fs_getb_buf                                                   ; 8412: ae dd 0f    ...
    beq update_sequence_return                                        ; 8415: f0 4a       .J
    ldy #&1f                                                          ; 8417: a0 1f       ..
; &8419 referenced 1 time by &8420
.error1
    lda fs_putb_buf,y                                                 ; 8419: b9 dc 0f    ...
    sta l0fe0,y                                                       ; 841c: 99 e0 0f    ...
    dey                                                               ; 841f: 88          .
    bpl error1                                                        ; 8420: 10 f7       ..
    tax                                                               ; 8422: aa          .              ; X=File handle
    lda #osbyte_read_write_exec_file_handle                           ; 8423: a9 c6       ..
    jsr osbyte                                                        ; 8425: 20 f4 ff     ..            ; Read/Write *EXEC file handle
    lda #&ea                                                          ; 8428: a9 ea       ..
    cpy l00ba                                                         ; 842a: c4 ba       ..             ; Y=value of *SPOOL file handle
    bne c8430                                                         ; 842c: d0 02       ..
    lda #&e4                                                          ; 842e: a9 e4       ..
; &8430 referenced 1 time by &842c
.c8430
    cpx l00ba                                                         ; 8430: e4 ba       ..             ; X=value of *EXEC file handle
    bne c8436                                                         ; 8432: d0 02       ..
    lda #&e8                                                          ; 8434: a9 e8       ..
; &8436 referenced 1 time by &8432
.c8436
    tax                                                               ; 8436: aa          .
    ldy #&84                                                          ; 8437: a0 84       ..
    jsr oscli                                                         ; 8439: 20 f7 ff     ..
    lda #&e0                                                          ; 843c: a9 e0       ..
    sta l00c4                                                         ; 843e: 85 c4       ..
    ldx fs_getb_buf                                                   ; 8440: ae dd 0f    ...
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
; &8443 referenced 1 time by &83ce
.store_fs_error
    stx fs_last_error                                                 ; 8443: 8e 09 0e    ...
    ldy #1                                                            ; 8446: a0 01       ..
    cpx #&a8                                                          ; 8448: e0 a8       ..
    bcs c8450                                                         ; 844a: b0 04       ..
    lda #&a8                                                          ; 844c: a9 a8       ..
    sta (l00c4),y                                                     ; 844e: 91 c4       ..
; &8450 referenced 1 time by &844a
.c8450
    ldy #&ff                                                          ; 8450: a0 ff       ..
; &8452 referenced 1 time by &845a
.loop_c8452
    iny                                                               ; 8452: c8          .
    lda (l00c4),y                                                     ; 8453: b1 c4       ..
    sta l0100,y                                                       ; 8455: 99 00 01    ...
    eor #&0d                                                          ; 8458: 49 0d       I.
    bne loop_c8452                                                    ; 845a: d0 f6       ..
    sta l0100,y                                                       ; 845c: 99 00 01    ...
    beq c84a5                                                         ; 845f: f0 44       .D             ; ALWAYS branch

; &8461 referenced 1 time by &8415
.update_sequence_return
    sta fs_sequence_nos                                               ; 8461: 8d 08 0e    ...
    pla                                                               ; 8464: 68          h
    tay                                                               ; 8465: a8          .
    pla                                                               ; 8466: 68          h
    tax                                                               ; 8467: aa          .
    pla                                                               ; 8468: 68          h
.return_remote_cmd
    rts                                                               ; 8469: 60          `

; ***************************************************************************************
; Remote boot/execute handler
; 
; Checks byte 4 of the RX control block (remote status flag).
; If zero (not currently remoted), falls through to remot1 to
; set up a new remote session. If non-zero (already remoted),
; jumps to clear_jsr_protection and returns.
; ***************************************************************************************
.remote_boot_handler
    ldy #4                                                            ; 846a: a0 04       ..
    lda (net_rx_ptr),y                                                ; 846c: b1 9c       ..
    beq remot1                                                        ; 846e: f0 03       ..
; &8470 referenced 1 time by &84b6
.rchex
    jmp clear_jsr_protection                                          ; 8470: 4c e4 92    L..

; &8473 referenced 2 times by &846e, &84ac
.remot1
    ora #9                                                            ; 8473: 09 09       ..
    sta (net_rx_ptr),y                                                ; 8475: 91 9c       ..
    ldx #&80                                                          ; 8477: a2 80       ..
    ldy #&80                                                          ; 8479: a0 80       ..
    lda (net_rx_ptr),y                                                ; 847b: b1 9c       ..
    pha                                                               ; 847d: 48          H
    iny                                                               ; 847e: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 847f: b1 9c       ..
    ldy #&0f                                                          ; 8481: a0 0f       ..
    sta (nfs_workspace),y                                             ; 8483: 91 9e       ..
    dey                                                               ; 8485: 88          .              ; Y=&0e
    pla                                                               ; 8486: 68          h
    sta (nfs_workspace),y                                             ; 8487: 91 9e       ..
    jsr clear_osbyte_ce_cf                                            ; 8489: 20 96 81     ..
    jsr ctrl_block_setup                                              ; 848c: 20 71 91     q.
    ldx #1                                                            ; 848f: a2 01       ..
    ldy #0                                                            ; 8491: a0 00       ..
    lda #osbyte_read_write_econet_keyboard_disable                    ; 8493: a9 c9       ..
    jsr osbyte                                                        ; 8495: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute code at &0100
; 
; Clears JSR protection, zeroes &0100-&0102 (creating a BRK
; instruction at &0100 as a safe default), then JMP &0100 to
; execute code received over the network. If no code was loaded,
; the BRK triggers an error handler.
; ***************************************************************************************
.execute_at_0100
    jsr clear_jsr_protection                                          ; 8498: 20 e4 92     ..
    ldx #2                                                            ; 849b: a2 02       ..
    lda #0                                                            ; 849d: a9 00       ..
; &849f referenced 1 time by &84a3
.loop_c849f
    sta l0100,x                                                       ; 849f: 9d 00 01    ...
    dex                                                               ; 84a2: ca          .
    bpl loop_c849f                                                    ; 84a3: 10 fa       ..
; &84a5 referenced 2 times by &845f, &84de
.c84a5
    jmp l0100                                                         ; 84a5: 4c 00 01    L..

; ***************************************************************************************
; Remote operation with source validation
; 
; Validates that the source station in the received packet matches
; the controlling station stored in the NFS workspace. If byte 4 of
; the RX control block is zero (not currently remoted), allows the
; new remote session via remot1. If non-zero, compares the source
; station at RX offset &80 against workspace offset &0E -- rejects
; mismatched stations via clear_jsr_protection, accepts matching
; stations by falling through to insert_remote_key.
; ***************************************************************************************
.remote_validated
    ldy #4                                                            ; 84a8: a0 04       ..
    lda (net_rx_ptr),y                                                ; 84aa: b1 9c       ..
    beq remot1                                                        ; 84ac: f0 c5       ..
    ldy #&80                                                          ; 84ae: a0 80       ..
    lda (net_rx_ptr),y                                                ; 84b0: b1 9c       ..
    ldy #&0e                                                          ; 84b2: a0 0e       ..
    cmp (nfs_workspace),y                                             ; 84b4: d1 9e       ..
    bne rchex                                                         ; 84b6: d0 b8       ..
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.insert_remote_key
    ldy #&82                                                          ; 84b8: a0 82       ..
    lda (net_rx_ptr),y                                                ; 84ba: b1 9c       ..
    tay                                                               ; 84bc: a8          .
    ldx #0                                                            ; 84bd: a2 00       ..
    jsr clear_jsr_protection                                          ; 84bf: 20 e4 92     ..
    lda #osbyte_insert_input_buffer                                   ; 84c2: a9 99       ..
    jmp osbyte                                                        ; 84c4: 4c f4 ff    L..            ; Insert character Y into input buffer X

; &84c7 referenced 1 time by &851a
.c84c7
    lda #8                                                            ; 84c7: a9 08       ..
    bne set_listen_offset                                             ; 84c9: d0 04       ..             ; ALWAYS branch

; &84cb referenced 1 time by &86a9
.nlistn
    lda (net_tx_ptr,x)                                                ; 84cb: a1 9a       ..
; &84cd referenced 2 times by &852c, &89dc
.nlisne
    and #7                                                            ; 84cd: 29 07       ).
; &84cf referenced 1 time by &84c9
.set_listen_offset
    tax                                                               ; 84cf: aa          .
    ldy l8014,x                                                       ; 84d0: bc 14 80    ...
    ldx #0                                                            ; 84d3: a2 00       ..
    stx l0100                                                         ; 84d5: 8e 00 01    ...
; &84d8 referenced 1 time by &84e2
.loop_c84d8
    lda error_msg_table,y                                             ; 84d8: b9 4d 85    .M.
    sta l0101,x                                                       ; 84db: 9d 01 01    ...
    beq c84a5                                                         ; 84de: f0 c5       ..
    inx                                                               ; 84e0: e8          .
    iny                                                               ; 84e1: c8          .
    bne loop_c84d8                                                    ; 84e2: d0 f4       ..
    equs "SP."                                                        ; 84e4: 53 50 2e    SP.
    equb &0d, &45, &2e, &0d                                           ; 84e7: 0d 45 2e... .E.

; &84eb referenced 3 times by &8754, &902e, &928b
.send_to_fs_star
    lda #&2a ; '*'                                                    ; 84eb: a9 2a       .*
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
; &84ed referenced 2 times by &83c0, &8847
.send_to_fs
    pha                                                               ; 84ed: 48          H
    lda rx_flags                                                      ; 84ee: ad 64 0d    .d.
    pha                                                               ; 84f1: 48          H
    ora #&80                                                          ; 84f2: 09 80       ..
    sta rx_flags                                                      ; 84f4: 8d 64 0d    .d.
    lda #0                                                            ; 84f7: a9 00       ..
    pha                                                               ; 84f9: 48          H
    pha                                                               ; 84fa: 48          H
    tay                                                               ; 84fb: a8          .              ; Y=&00
    tsx                                                               ; 84fc: ba          .
; &84fd referenced 3 times by &8507, &850c, &8511
.c84fd
    jsr check_escape                                                  ; 84fd: 20 1d 85     ..
.incpx
    lda (net_tx_ptr),y                                                ; 8500: b1 9a       ..
    bmi fs_wait_cleanup                                               ; 8502: 30 0f       0.
    dec l0101,x                                                       ; 8504: de 01 01    ...
    bne c84fd                                                         ; 8507: d0 f4       ..
    dec l0102,x                                                       ; 8509: de 02 01    ...
    bne c84fd                                                         ; 850c: d0 ef       ..
    dec l0104,x                                                       ; 850e: de 04 01    ...
    bne c84fd                                                         ; 8511: d0 ea       ..
; &8513 referenced 1 time by &8502
.fs_wait_cleanup
    pla                                                               ; 8513: 68          h
    pla                                                               ; 8514: 68          h
    pla                                                               ; 8515: 68          h
    sta rx_flags                                                      ; 8516: 8d 64 0d    .d.
    pla                                                               ; 8519: 68          h
    beq c84c7                                                         ; 851a: f0 ab       ..
    rts                                                               ; 851c: 60          `

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
; 
; 3.35K restructures the SPOOL/EXEC close logic: both handles
; are always checked (3.35D skipped EXEC if SPOOL matched),
; and OSCLI is always called (with a harmless "." default if
; neither matched).
; ***************************************************************************************
; &851d referenced 2 times by &84fd, &8690
.check_escape
    lda #osbyte_acknowledge_escape                                    ; 851d: a9 7e       .~
    bit l00ff                                                         ; 851f: 24 ff       $.
    bpl return_4                                                      ; 8521: 10 29       .)
    jsr osbyte                                                        ; 8523: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
; 3.35K fix: initialise Y=0 before the indexed store.
; In 3.35D, Y could hold any value here after the
; OSBYTE escape acknowledge call.
    ldy #0                                                            ; 8526: a0 00       ..
    lsr a                                                             ; 8528: 4a          J
    sta (net_tx_ptr),y                                                ; 8529: 91 9a       ..
    asl a                                                             ; 852b: 0a          .
    bne nlisne                                                        ; 852c: d0 9f       ..
.bgetv_handler
    sec                                                               ; 852e: 38          8
    jsr handle_bput_bget                                              ; 852f: 20 dd 83     ..            ; Handle BPUT/BGET file byte I/O
    sec                                                               ; 8532: 38          8
    lda #&fe                                                          ; 8533: a9 fe       ..
    bit l0fdf                                                         ; 8535: 2c df 0f    ,..
    bvs return_4                                                      ; 8538: 70 12       p.
; 3.35K fix: EOF hint clear/set are now mutually
; exclusive. In 3.35D, both clear_fs_flag and
; set_fs_flag were called when N=0, with the clear
; immediately undone by the set — making the EOF
; hint always set regardless of file position.
    clc                                                               ; 853a: 18          .
    bmi c8544                                                         ; 853b: 30 07       0.
    lda l00cf                                                         ; 853d: a5 cf       ..
    jsr clear_fs_flag                                                 ; 853f: 20 51 86     Q.
    bcc c8549                                                         ; 8542: 90 05       ..
; &8544 referenced 1 time by &853b
.c8544
    lda l00cf                                                         ; 8544: a5 cf       ..
    jsr l8659                                                         ; 8546: 20 59 86     Y.
; &8549 referenced 1 time by &8542
.c8549
    lda l0fde                                                         ; 8549: ad de 0f    ...
; &854c referenced 2 times by &8521, &8538
.return_4
    rts                                                               ; 854c: 60          `

; Econet error message table (ERRTAB, 8 entries).
; Each entry: error number byte followed by NUL-terminated string.
;   &A0: "Line Jammed"     &A1: "Net Error"
;   &A2: "Not listening"   &A3: "No Clock"
;   &A4: "Bad Txcb"        &11: "Escape"
;   &CB: "Bad Option"      &A5: "No reply"
; Indexed by the low 3 bits of the TXCB flag byte (AND #&07),
; which encode the specific Econet failure reason. The NREPLY
; and NLISTN routines build a MOS BRK error block at &100 on the
; stack page: NREPLY fires when the fileserver does not respond
; within the timeout period; NLISTN fires when the destination
; station actively refused the connection.
; Indexed via the error dispatch at c8424/c842c.
; &854d referenced 1 time by &84d8
.error_msg_table
    equb &a0                                                          ; 854d: a0          .
    equs "Line Jam"                                                   ; 854e: 4c 69 6e... Lin
    equb &6d                                                          ; 8556: 6d          m
    equs "ed", 0                                                      ; 8557: 65 64 00    ed.
    equb &a1                                                          ; 855a: a1          .
    equs "Net Error", 0                                               ; 855b: 4e 65 74... Net
    equb &a2                                                          ; 8565: a2          .
    equs "Not listening", 0                                           ; 8566: 4e 6f 74... Not
    equb &a3                                                          ; 8574: a3          .
    equs "No Clock", 0                                                ; 8575: 4e 6f 20... No
    equb &11                                                          ; 857e: 11          .
    equs "Escape", 0                                                  ; 857f: 45 73 63... Esc
    equb &cb                                                          ; 8586: cb          .
    equs "Bad Option", 0                                              ; 8587: 42 61 64... Bad
    equb &a5                                                          ; 8592: a5          .
    equs "No reply", 0                                                ; 8593: 4e 6f 20... No
; overlapping: stx os_text_ptr                                        ; 859c: 86 f2       ..
; &859c referenced 3 times by &80c7, &896f, &8bb6
.l859c
    equb &86                                                          ; 859c: 86          .
.l859d
save_fscv_args = l859d+9
decode_attribs_6bit = l859d+20
decode_attribs_5bit = l859d+30
    equs &f2, &84, &f3, &8e, &10, &0e, &8c, &11, &0e, &85, &bd, &86   ; 859d: f2 84 f3... ...
    equs &bb, &84, &bc, &86, &be, &84, &bf, "`", &a0, &0e, &b1, &bb   ; 85a9: bb 84 bc... ...
    equs ")?", &a2, 4, &d0, 4, ")", &1f, &a2, &ff, &85, &b8, &a9, 0   ; 85b5: 29 3f a2... )?.
; overlapping: sty l00f3                                              ; 859e: 84 f3       ..
; overlapping: stx fs_cmd_ptr                                         ; 85a0: 8e 10 0e    ...
; overlapping: sty l0e11                                              ; 85a3: 8c 11 0e    ...
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
; overlapping: sta fs_last_byte_flag                                  ; 85a6: 85 bd       ..
; &85a6 referenced 2 times by &8907, &8a0e
; overlapping: stx fs_options                                         ; 85a8: 86 bb       ..
; overlapping: sty fs_block_offset                                    ; 85aa: 84 bc       ..
; overlapping: stx fs_crc_lo                                          ; 85ac: 86 be       ..
; overlapping: sty fs_crc_hi                                          ; 85ae: 84 bf       ..
; overlapping: rts                                                    ; 85b0: 60          `
; ***************************************************************************************
; Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)
; 
; Reads attribute byte at offset &0E from the parameter block,
; masks to 6 bits, then falls through to the shared bitmask
; builder. Converts fileserver protection format (5-6 bits) to
; BBC OSFILE attribute format (8 bits) via the lookup table at
; &85CE. The two formats use different bit layouts for file
; protection attributes.
; ***************************************************************************************
; overlapping: ldy #&0e                                               ; 85b1: a0 0e       ..
; &85b1 referenced 2 times by &889a, &88c5
; overlapping: lda (fs_options),y                                     ; 85b3: b1 bb       ..
; overlapping: and #&3f ; '?'                                         ; 85b5: 29 3f       )?
; overlapping: ldx #4                                                 ; 85b7: a2 04       ..
; overlapping: bne l85bf                                              ; 85b9: d0 04       ..
; ***************************************************************************************
; Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)
; 
; Masks A to 5 bits and builds an access bitmask via the
; lookup table at &85CE. Each input bit position maps to a
; different output bit via the table. The conversion is done
; by iterating through the source bits and OR-ing in the
; corresponding destination bits from the table, translating
; between BBC (8-bit) and fileserver (5-bit) protection formats.
; ***************************************************************************************
; overlapping: and #&1f                                               ; 85bb: 29 1f       ).
; &85bb referenced 2 times by &87bf, &88e2
; overlapping: ldx #&ff                                               ; 85bd: a2 ff       ..
; overlapping: sta fs_error_ptr                                       ; 85bf: 85 b8       ..
; overlapping: lda #0                                                 ; 85c1: a9 00       ..

; &85c3 referenced 1 time by &85cb
.loop_c85c3
    inx                                                               ; 85c3: e8          .
    lsr fs_error_ptr                                                  ; 85c4: 46 b8       F.
    bcc c85cb                                                         ; 85c6: 90 03       ..
    ora access_bit_table,x                                            ; 85c8: 1d ce 85    ...
; &85cb referenced 1 time by &85c6
.c85cb
    bne loop_c85c3                                                    ; 85cb: d0 f6       ..
    rts                                                               ; 85cd: 60          `

; &85ce referenced 1 time by &85c8
.access_bit_table
    equb &50, &20, 5, 2, &88, 4, 8, &80, &10, 1, 2                    ; 85ce: 50 20 05... P .

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
; &85d9 referenced 14 times by &81ed, &8218, &8238, &8245, &8c25, &8c2f, &8c3d, &8c48, &8c5d, &8c72, &8c85, &8c94, &8ca6, &8d6c
.print_inline
    pla                                                               ; 85d9: 68          h              ; Pop return address (low) — points to last byte of JSR
    sta fs_load_addr                                                  ; 85da: 85 b0       ..
    pla                                                               ; 85dc: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 85dd: 85 b1       ..
    ldy #0                                                            ; 85df: a0 00       ..
; &85e1 referenced 1 time by &85ee
.loop_c85e1
    inc fs_load_addr                                                  ; 85e1: e6 b0       ..             ; Advance pointer past return address / to next char
    bne c85e7                                                         ; 85e3: d0 02       ..
    inc fs_load_addr_hi                                               ; 85e5: e6 b1       ..
; &85e7 referenced 1 time by &85e3
.c85e7
    lda (fs_load_addr),y                                              ; 85e7: b1 b0       ..             ; Load next byte from inline string
    bmi c85f0                                                         ; 85e9: 30 05       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 85eb: 20 e3 ff     ..            ; Write character
    bne loop_c85e1                                                    ; 85ee: d0 f1       ..
; &85f0 referenced 1 time by &85e9
.c85f0
    jmp (fs_load_addr)                                                ; 85f0: 6c b0 00    l..            ; Jump to address of high-bit byte (resumes code after string)

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
;     X: corrupted
;     Y: offset past last digit parsed
; ***************************************************************************************
; &85f3 referenced 2 times by &808a, &8090
.parse_decimal
    tax                                                               ; 85f3: aa          .
    lda #0                                                            ; 85f4: a9 00       ..
    sta fs_load_addr_2                                                ; 85f6: 85 b2       ..
; &85f8 referenced 1 time by &8615
.loop_c85f8
    lda (fs_options),y                                                ; 85f8: b1 bb       ..
    cmp #&40 ; '@'                                                    ; 85fa: c9 40       .@
    bcs c8617                                                         ; 85fc: b0 19       ..
    cmp #&2e ; '.'                                                    ; 85fe: c9 2e       ..
    beq c8618                                                         ; 8600: f0 16       ..
    bmi c8617                                                         ; 8602: 30 13       0.
    and #&0f                                                          ; 8604: 29 0f       ).
    sta l00b3                                                         ; 8606: 85 b3       ..
    asl fs_load_addr_2                                                ; 8608: 06 b2       ..
    lda fs_load_addr_2                                                ; 860a: a5 b2       ..
    asl a                                                             ; 860c: 0a          .
    asl a                                                             ; 860d: 0a          .
    adc fs_load_addr_2                                                ; 860e: 65 b2       e.
    adc l00b3                                                         ; 8610: 65 b3       e.
    sta fs_load_addr_2                                                ; 8612: 85 b2       ..
    iny                                                               ; 8614: c8          .
    bne loop_c85f8                                                    ; 8615: d0 e1       ..
; &8617 referenced 2 times by &85fc, &8602
.c8617
    clc                                                               ; 8617: 18          .
; &8618 referenced 1 time by &8600
.c8618
    lda fs_load_addr_2                                                ; 8618: a5 b2       ..
    rts                                                               ; 861a: 60          `

; &861b referenced 3 times by &884e, &8a29, &8f45
.handle_to_mask_a
    tay                                                               ; 861b: a8          .
; &861c referenced 2 times by &83e8, &8912
.handle_to_mask_clc
    clc                                                               ; 861c: 18          .
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
; Three entry points: &861D (direct), &861C (CLC first), &861B (TAY first).
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
; &861d referenced 1 time by &8973
.handle_to_mask
    pha                                                               ; 861d: 48          H
    txa                                                               ; 861e: 8a          .
    pha                                                               ; 861f: 48          H
    tya                                                               ; 8620: 98          .
    bcc y2fsl5                                                        ; 8621: 90 02       ..
    beq c8634                                                         ; 8623: f0 0f       ..
; &8625 referenced 1 time by &8621
.y2fsl5
    sec                                                               ; 8625: 38          8
    sbc #&1f                                                          ; 8626: e9 1f       ..
    tax                                                               ; 8628: aa          .
    lda #1                                                            ; 8629: a9 01       ..
; &862b referenced 1 time by &862d
.y2fsl2
    asl a                                                             ; 862b: 0a          .
    dex                                                               ; 862c: ca          .
    bne y2fsl2                                                        ; 862d: d0 fc       ..
    ror a                                                             ; 862f: 6a          j
    tay                                                               ; 8630: a8          .
    bne c8634                                                         ; 8631: d0 01       ..
    dey                                                               ; 8633: 88          .
; &8634 referenced 2 times by &8623, &8631
.c8634
    pla                                                               ; 8634: 68          h
    tax                                                               ; 8635: aa          .
    pla                                                               ; 8636: 68          h
    rts                                                               ; 8637: 60          `

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
; &8638 referenced 2 times by &89a9, &8f5d
.mask_to_handle
    ldx #&1f                                                          ; 8638: a2 1f       ..
; &863a referenced 1 time by &863c
.fs2al1
    inx                                                               ; 863a: e8          .
    lsr a                                                             ; 863b: 4a          J
    bne fs2al1                                                        ; 863c: d0 fc       ..
    txa                                                               ; 863e: 8a          .
    rts                                                               ; 863f: 60          `

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
; &8640 referenced 2 times by &873a, &87f6
.compare_addresses
    ldx #4                                                            ; 8640: a2 04       ..
; &8642 referenced 1 time by &8649
.loop_c8642
    lda l00af,x                                                       ; 8642: b5 af       ..
    eor l00b3,x                                                       ; 8644: 55 b3       U.
    bne return_compare                                                ; 8646: d0 03       ..
    dex                                                               ; 8648: ca          .
    bne loop_c8642                                                    ; 8649: d0 f7       ..
; &864b referenced 1 time by &8646
.return_compare
    rts                                                               ; 864b: 60          `

.fscv_read_handles
    ldx #&20 ; ' '                                                    ; 864c: a2 20       .
    ldy #&27 ; '''                                                    ; 864e: a0 27       .'
.return_fscv_handles
    rts                                                               ; 8650: 60          `

; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
; the specified bits. Falls through to store the result.
; ***************************************************************************************
; &8651 referenced 3 times by &853f, &8869, &8aa5
.clear_fs_flag
    eor #&ff                                                          ; 8651: 49 ff       I.
    and fs_eof_flags                                                  ; 8653: 2d 07 0e    -..
    jmp l865c                                                         ; 8656: 4c 5c 86    L\.

; overlapping: ora fs_eof_flags                                       ; 8659: 0d 07 0e    ...
; &8659 referenced 5 times by &8546, &894f, &899e, &89c5, &8aa8
.l8659
    equb &0d, 7                                                       ; 8659: 0d 07       ..

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
.set_fs_flag
l865c = set_fs_flag+1
    asl l078d                                                         ; 865b: 0e 8d 07    ...
; overlapping: sta fs_eof_flags                                       ; 865c: 8d 07 0e    ...
; &865c referenced 1 time by &8656
; overlapping: asl la260                                              ; 865e: 0e 60 a2    .`.
    equb &0e                                                          ; 865e: 0e          .

    rts                                                               ; 865f: 60          `

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &8660 referenced 2 times by &83b6, &8836
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8660: a2 c0       ..
; overlapping: cpy #&86                                               ; 8661: c0 86       ..
    stx net_tx_ptr                                                    ; 8662: 86 9a       ..
; overlapping: txs                                                    ; 8663: 9a          .
    ldx #0                                                            ; 8664: a2 00       ..
    stx net_tx_ptr_hi                                                 ; 8666: 86 9b       ..
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &8668 referenced 4 times by &9017, &9071, &90c8, &9269
.tx_poll_ff
    lda #&ff                                                          ; 8668: a9 ff       ..
.tx_poll_timeout
    ldy #&60 ; '`'                                                    ; 866a: a0 60       .`             ; Y=timeout parameter (&60 = standard)
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
; Two entry points: setup_tx_ptr_c0 (&8660) always uses the
; standard TXCB; tx_poll_core (&866C) is general-purpose.
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
; &866c referenced 1 time by &9057
.tx_poll_core
    pha                                                               ; 866c: 48          H
    tya                                                               ; 866d: 98          .
    pha                                                               ; 866e: 48          H
    ldx #0                                                            ; 866f: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 8671: a1 9a       ..
; &8673 referenced 1 time by &86a6
.c8673
    sta (net_tx_ptr,x)                                                ; 8673: 81 9a       ..
    pha                                                               ; 8675: 48          H
; &8676 referenced 1 time by &8679
.loop_c8676
    asl tx_clear_flag                                                 ; 8676: 0e 62 0d    .b.
    bcc loop_c8676                                                    ; 8679: 90 fb       ..
    lda net_tx_ptr                                                    ; 867b: a5 9a       ..
    sta nmi_tx_block                                                  ; 867d: 85 a0       ..
    lda net_tx_ptr_hi                                                 ; 867f: a5 9b       ..
    sta nmi_tx_block_hi                                               ; 8681: 85 a1       ..
    jsr trampoline_tx_setup                                           ; 8683: 20 60 96     `.
; &8686 referenced 1 time by &8688
.l4
    lda (net_tx_ptr,x)                                                ; 8686: a1 9a       ..
    bmi l4                                                            ; 8688: 30 fc       0.
    asl a                                                             ; 868a: 0a          .              ; A=function code (&FF=load, &00=save, &01-&06=attrs)
; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Saves A/X/Y, copies the filename pointer from the parameter block
; to os_text_ptr, then uses GSINIT/GSREAD (via parse_filename_gs at
; &86BA) to parse the filename into &0E30+. Sets fs_crc_lo/hi to
; point at the parsed filename buffer.
; Dispatches by function code A:
;   A=&FF: load file (send_fs_examine at &86F4)
;   A=&00: save file (filev_save at &876A)
;   A=&01-&06: attribute operations (filev_attrib_dispatch at &8870)
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
    bpl c86ac                                                         ; 868b: 10 1f       ..
    asl a                                                             ; 868d: 0a          .
    beq c86a8                                                         ; 868e: f0 18       ..
    jsr check_escape                                                  ; 8690: 20 1d 85     ..
    pla                                                               ; 8693: 68          h
    tax                                                               ; 8694: aa          .
    pla                                                               ; 8695: 68          h
    tay                                                               ; 8696: a8          .
    pla                                                               ; 8697: 68          h
    beq c86a8                                                         ; 8698: f0 0e       ..
    sbc #1                                                            ; 869a: e9 01       ..
    pha                                                               ; 869c: 48          H
    tya                                                               ; 869d: 98          .
    pha                                                               ; 869e: 48          H
    txa                                                               ; 869f: 8a          .
; &86a0 referenced 2 times by &86a1, &86a4
.c86a0
    dex                                                               ; 86a0: ca          .
    bne c86a0                                                         ; 86a1: d0 fd       ..
    dey                                                               ; 86a3: 88          .
    bne c86a0                                                         ; 86a4: d0 fa       ..
    beq c8673                                                         ; 86a6: f0 cb       ..             ; ALWAYS branch

; &86a8 referenced 2 times by &868e, &8698
.c86a8
    tax                                                               ; 86a8: aa          .
    jmp nlistn                                                        ; 86a9: 4c cb 84    L..

; &86ac referenced 1 time by &868b
.c86ac
    pla                                                               ; 86ac: 68          h
    pla                                                               ; 86ad: 68          h
    pla                                                               ; 86ae: 68          h
    rts                                                               ; 86af: 60          `

    equb &a0, 1                                                       ; 86b0: a0 01       ..
.file1
    equb &b1, &bb, &99, &f2, 0, &88, &10, &f8                         ; 86b2: b1 bb 99... ...

; ***************************************************************************************
; Parse filename using GSINIT/GSREAD into &0E30
; 
; Uses the MOS GSINIT/GSREAD API to parse a filename string from
; (os_text_ptr),Y, handling quoted strings and |-escaped characters.
; Stores the parsed result CR-terminated at &0E30 and sets up
; fs_crc_lo/hi to point to that buffer. Sub-entry at &86C5 allows
; a non-zero starting Y offset.
; Note: the code uses overlapping bytes with send_fs_examine --
; the BCS at &86F4 and the INX/STA at &86D2 share the same bytes
; depending on the entry path.
; 
; On Entry:
;     Y: offset into (os_text_ptr) buffer (0 at &86C3)
; 
; On Exit:
;     X: length of parsed string
;     Y: preserved
; ***************************************************************************************
; &86ba referenced 2 times by &8988, &8dbf
.parse_filename_gs
    ldy #0                                                            ; 86ba: a0 00       ..
; &86bc referenced 1 time by &8c13
.sub_c86bc
    ldx #&ff                                                          ; 86bc: a2 ff       ..
    clc                                                               ; 86be: 18          .
    jsr gsinit                                                        ; 86bf: 20 c2 ff     ..
    beq c86cf                                                         ; 86c2: f0 0b       ..
; &86c4 referenced 1 time by &86cd
.delay_1ms
.quote1
    jsr gsread                                                        ; 86c4: 20 c5 ff     ..
    bcs c86cf                                                         ; 86c7: b0 06       ..
    inx                                                               ; 86c9: e8          .
    sta l0e30,x                                                       ; 86ca: 9d 30 0e    .0.
    bcc delay_1ms                                                     ; 86cd: 90 f5       ..             ; ALWAYS branch

; &86cf referenced 2 times by &86c2, &86c7
.c86cf
    inx                                                               ; 86cf: e8          .
    lda #&0d                                                          ; 86d0: a9 0d       ..
    sta l0e30,x                                                       ; 86d2: 9d 30 0e    .0.
    lda #&30 ; '0'                                                    ; 86d5: a9 30       .0
    sta fs_crc_lo                                                     ; 86d7: 85 be       ..
    lda #&0e                                                          ; 86d9: a9 0e       ..
    sta fs_crc_hi                                                     ; 86db: 85 bf       ..
    rts                                                               ; 86dd: 60          `

    equb &20, &a6, &85, &20, &b0, &86, &a5, &bd, &10, &7d, &c9, &ff   ; 86de: 20 a6 85...  ..
    equb &f0,   3, &4c, &52, &89                                      ; 86ea: f0 03 4c... ..L
.loadop
    equb &20, &43, &8d, &a0, 2                                        ; 86ef: 20 43 8d...  C.

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
; &86f4 referenced 1 time by &8dd4
.send_fs_examine
    lda #&92                                                          ; 86f4: a9 92       ..
    sta fs_cmd_urd                                                    ; 86f6: 8d 02 0f    ...
    lda #&2a ; '*'                                                    ; 86f9: a9 2a       .*
    jsr prepare_cmd_clv                                               ; 86fb: 20 80 83     ..
    ldy #6                                                            ; 86fe: a0 06       ..
    lda (fs_options),y                                                ; 8700: b1 bb       ..
    bne lodfil                                                        ; 8702: d0 08       ..
    jsr copy_load_addr_from_params                                    ; 8704: 20 d1 87     ..
    jsr copy_reply_to_params                                          ; 8707: 20 e3 87     ..
    bcc c8712                                                         ; 870a: 90 06       ..
; &870c referenced 1 time by &8702
.lodfil
    jsr copy_reply_to_params                                          ; 870c: 20 e3 87     ..
    jsr copy_load_addr_from_params                                    ; 870f: 20 d1 87     ..
; &8712 referenced 1 time by &870a
.c8712
    ldy #4                                                            ; 8712: a0 04       ..
; &8714 referenced 1 time by &871f
.loop_c8714
    lda fs_load_addr,x                                                ; 8714: b5 b0       ..
    sta l00c8,x                                                       ; 8716: 95 c8       ..
    adc l0f0d,x                                                       ; 8718: 7d 0d 0f    }..
    sta l00b4,x                                                       ; 871b: 95 b4       ..
    inx                                                               ; 871d: e8          .
    dey                                                               ; 871e: 88          .
    bne loop_c8714                                                    ; 871f: d0 f3       ..
    sec                                                               ; 8721: 38          8
    sbc l0f10                                                         ; 8722: ed 10 0f    ...
    sta l00b7                                                         ; 8725: 85 b7       ..
    jsr print_file_info                                               ; 8727: 20 fc 8c     ..
    jsr send_data_blocks                                              ; 872a: 20 3a 87     :.
    ldx #2                                                            ; 872d: a2 02       ..
; &872f referenced 1 time by &8736
.floop
    lda l0f10,x                                                       ; 872f: bd 10 0f    ...
    sta fs_cmd_data,x                                                 ; 8732: 9d 05 0f    ...
    dex                                                               ; 8735: ca          .
    bpl floop                                                         ; 8736: 10 f7       ..
    bmi c87b0                                                         ; 8738: 30 76       0v             ; ALWAYS branch

; ***************************************************************************************
; Send file data in multi-block chunks
; 
; Repeatedly sends &80-byte (128-byte) blocks of file data to the
; fileserver using command &7F. Compares current address (&C8-&CB)
; against end address (&B4-&B7) via compare_addresses, and loops
; until the entire file has been transferred. Each block is sent
; via send_to_fs_star.
; ***************************************************************************************
; &873a referenced 2 times by &872a, &8a94
.send_data_blocks
    jsr compare_addresses                                             ; 873a: 20 40 86     @.            ; Compare two 4-byte addresses
    beq return_lodchk                                                 ; 873d: f0 25       .%
    lda #&92                                                          ; 873f: a9 92       ..
    sta l00c1                                                         ; 8741: 85 c1       ..
; &8743 referenced 1 time by &875f
.loop_c8743
    ldx #3                                                            ; 8743: a2 03       ..
; &8745 referenced 1 time by &874e
.loop_c8745
    lda l00c8,x                                                       ; 8745: b5 c8       ..
    sta l00c4,x                                                       ; 8747: 95 c4       ..
    lda l00b4,x                                                       ; 8749: b5 b4       ..
    sta l00c8,x                                                       ; 874b: 95 c8       ..
    dex                                                               ; 874d: ca          .
    bpl loop_c8745                                                    ; 874e: 10 f5       ..
    lda #&7f                                                          ; 8750: a9 7f       ..
    sta l00c0                                                         ; 8752: 85 c0       ..
    jsr send_to_fs_star                                               ; 8754: 20 eb 84     ..
    ldy #3                                                            ; 8757: a0 03       ..
; &8759 referenced 1 time by &8762
.lodchk
    lda l00c8,y                                                       ; 8759: b9 c8 00    ...
    eor l00b4,y                                                       ; 875c: 59 b4 00    Y..
    bne loop_c8743                                                    ; 875f: d0 e2       ..
    dey                                                               ; 8761: 88          .
    bpl lodchk                                                        ; 8762: 10 f5       ..
; &8764 referenced 1 time by &873d
.return_lodchk
    rts                                                               ; 8764: 60          `

.saveop
    beq filev_save                                                    ; 8765: f0 03       ..
    jmp filev_attrib_dispatch                                         ; 8767: 4c 70 88    Lp.

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
; &876a referenced 1 time by &8765
.filev_save
    ldx #4                                                            ; 876a: a2 04       ..
    ldy #&0e                                                          ; 876c: a0 0e       ..
; &876e referenced 1 time by &8788
.savsiz
    lda (fs_options),y                                                ; 876e: b1 bb       ..
    sta port_ws_offset,y                                              ; 8770: 99 a6 00    ...
    jsr sub_4_from_y                                                  ; 8773: 20 f0 87     ..
    sbc (fs_options),y                                                ; 8776: f1 bb       ..
    sta fs_cmd_csd,y                                                  ; 8778: 99 03 0f    ...
    pha                                                               ; 877b: 48          H
    lda (fs_options),y                                                ; 877c: b1 bb       ..
    sta port_ws_offset,y                                              ; 877e: 99 a6 00    ...
    pla                                                               ; 8781: 68          h
    sta (fs_options),y                                                ; 8782: 91 bb       ..
    jsr add_5_to_y                                                    ; 8784: 20 dd 87     ..
    dex                                                               ; 8787: ca          .
    bne savsiz                                                        ; 8788: d0 e4       ..
    ldy #9                                                            ; 878a: a0 09       ..
; &878c referenced 1 time by &8792
.loop_c878c
    lda (fs_options),y                                                ; 878c: b1 bb       ..
    sta fs_cmd_csd,y                                                  ; 878e: 99 03 0f    ...
    dey                                                               ; 8791: 88          .
    bne loop_c878c                                                    ; 8792: d0 f8       ..
    lda #&91                                                          ; 8794: a9 91       ..
    sta fs_cmd_urd                                                    ; 8796: 8d 02 0f    ...
    sta fs_error_ptr                                                  ; 8799: 85 b8       ..
    ldx #&0b                                                          ; 879b: a2 0b       ..
    jsr sub_c8d45                                                     ; 879d: 20 45 8d     E.
    ldy #1                                                            ; 87a0: a0 01       ..
    lda #&14                                                          ; 87a2: a9 14       ..
    jsr prepare_cmd_clv                                               ; 87a4: 20 80 83     ..
    jsr print_file_info                                               ; 87a7: 20 fc 8c     ..
    lda fs_cmd_data                                                   ; 87aa: ad 05 0f    ...
    jsr transfer_file_blocks                                          ; 87ad: 20 f5 87     ..
; &87b0 referenced 1 time by &8738
.c87b0
    lda #&2a ; '*'                                                    ; 87b0: a9 2a       .*
    sta fs_error_ptr                                                  ; 87b2: 85 b8       ..
    jsr send_fs_reply_cmd                                             ; 87b4: 20 ba 83     ..
    stx l0f08                                                         ; 87b7: 8e 08 0f    ...
    ldy #&0e                                                          ; 87ba: a0 0e       ..
    lda fs_cmd_data                                                   ; 87bc: ad 05 0f    ...
    jsr decode_attribs_5bit                                           ; 87bf: 20 bb 85     ..
    beq c87c7                                                         ; 87c2: f0 03       ..
; &87c4 referenced 1 time by &87cc
.loop_c87c4
    lda l0ef7,y                                                       ; 87c4: b9 f7 0e    ...
; &87c7 referenced 1 time by &87c2
.c87c7
    sta (fs_options),y                                                ; 87c7: 91 bb       ..
    iny                                                               ; 87c9: c8          .
    cpy #&12                                                          ; 87ca: c0 12       ..
    bne loop_c87c4                                                    ; 87cc: d0 f6       ..
    jmp restore_args_return                                           ; 87ce: 4c 52 89    LR.

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &87d1 referenced 2 times by &8704, &870f
.copy_load_addr_from_params
    ldy #5                                                            ; 87d1: a0 05       ..
; &87d3 referenced 1 time by &87db
.lodrl1
    lda (fs_options),y                                                ; 87d3: b1 bb       ..
    sta l00ae,y                                                       ; 87d5: 99 ae 00    ...
    dey                                                               ; 87d8: 88          .
    cpy #2                                                            ; 87d9: c0 02       ..
    bcs lodrl1                                                        ; 87db: b0 f6       ..
; &87dd referenced 1 time by &8784
.add_5_to_y
    iny                                                               ; 87dd: c8          .
; &87de referenced 1 time by &8a71
.add_4_to_y
    iny                                                               ; 87de: c8          .
    iny                                                               ; 87df: c8          .
    iny                                                               ; 87e0: c8          .
    iny                                                               ; 87e1: c8          .
    rts                                                               ; 87e2: 60          `

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; ***************************************************************************************
; &87e3 referenced 2 times by &8707, &870c
.copy_reply_to_params
    ldy #&0d                                                          ; 87e3: a0 0d       ..
    txa                                                               ; 87e5: 8a          .
; &87e6 referenced 1 time by &87ee
.lodrl2
    sta (fs_options),y                                                ; 87e6: 91 bb       ..
    lda fs_cmd_urd,y                                                  ; 87e8: b9 02 0f    ...
    dey                                                               ; 87eb: 88          .
    cpy #2                                                            ; 87ec: c0 02       ..
    bcs lodrl2                                                        ; 87ee: b0 f6       ..
; &87f0 referenced 1 time by &8773
.sub_4_from_y
    dey                                                               ; 87f0: 88          .
; &87f1 referenced 2 times by &8888, &8a79
.sub_3_from_y
    dey                                                               ; 87f1: 88          .
    dey                                                               ; 87f2: 88          .
    dey                                                               ; 87f3: 88          .
    rts                                                               ; 87f4: 60          `

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
; &87f5 referenced 2 times by &87ad, &8a8f
.transfer_file_blocks
    pha                                                               ; 87f5: 48          H
    jsr compare_addresses                                             ; 87f6: 20 40 86     @.            ; Compare two 4-byte addresses
    beq c886c                                                         ; 87f9: f0 71       .q
; &87fb referenced 1 time by &884a
.c87fb
    ldx #0                                                            ; 87fb: a2 00       ..
    ldy #4                                                            ; 87fd: a0 04       ..
    stx l0f08                                                         ; 87ff: 8e 08 0f    ...
    stx l0f09                                                         ; 8802: 8e 09 0f    ...
    clc                                                               ; 8805: 18          .
; &8806 referenced 1 time by &8813
.loop_c8806
    lda fs_load_addr,x                                                ; 8806: b5 b0       ..
    sta l00c4,x                                                       ; 8808: 95 c4       ..
    adc l0f06,x                                                       ; 880a: 7d 06 0f    }..
    sta l00c8,x                                                       ; 880d: 95 c8       ..
    sta fs_load_addr,x                                                ; 880f: 95 b0       ..
    inx                                                               ; 8811: e8          .
    dey                                                               ; 8812: 88          .
    bne loop_c8806                                                    ; 8813: d0 f1       ..
    bcs c8824                                                         ; 8815: b0 0d       ..
    sec                                                               ; 8817: 38          8
; &8818 referenced 1 time by &8820
.savchk
    lda fs_load_addr,y                                                ; 8818: b9 b0 00    ...
    sbc l00b4,y                                                       ; 881b: f9 b4 00    ...
    iny                                                               ; 881e: c8          .
    dex                                                               ; 881f: ca          .
    bne savchk                                                        ; 8820: d0 f6       ..
    bcc c882d                                                         ; 8822: 90 09       ..
; &8824 referenced 1 time by &8815
.c8824
    ldx #3                                                            ; 8824: a2 03       ..
; &8826 referenced 1 time by &882b
.loop_c8826
    lda l00b4,x                                                       ; 8826: b5 b4       ..
    sta l00c8,x                                                       ; 8828: 95 c8       ..
    dex                                                               ; 882a: ca          .
    bpl loop_c8826                                                    ; 882b: 10 f9       ..
; &882d referenced 1 time by &8822
.c882d
    pla                                                               ; 882d: 68          h
    pha                                                               ; 882e: 48          H
    php                                                               ; 882f: 08          .
    sta l00c1                                                         ; 8830: 85 c1       ..
    lda #&80                                                          ; 8832: a9 80       ..
    sta l00c0                                                         ; 8834: 85 c0       ..
    jsr setup_tx_ptr_c0                                               ; 8836: 20 60 86     `.
    lda fs_error_ptr                                                  ; 8839: a5 b8       ..
    jsr init_tx_ctrl_port                                             ; 883b: 20 4a 83     J.
    plp                                                               ; 883e: 28          (
    bcs c886c                                                         ; 883f: b0 2b       .+
    lda #&91                                                          ; 8841: a9 91       ..
    sta l00c1                                                         ; 8843: 85 c1       ..
    lda #&2a ; '*'                                                    ; 8845: a9 2a       .*
    jsr send_to_fs                                                    ; 8847: 20 ed 84     ..
    bne c87fb                                                         ; 884a: d0 af       ..
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
.eof_handler
    pha                                                               ; 884c: 48          H
    txa                                                               ; 884d: 8a          .
    jsr handle_to_mask_a                                              ; 884e: 20 1b 86     ..
    tya                                                               ; 8851: 98          .
    and fs_eof_flags                                                  ; 8852: 2d 07 0e    -..
    tax                                                               ; 8855: aa          .
    beq c886c                                                         ; 8856: f0 14       ..
    pha                                                               ; 8858: 48          H
    sty fs_cmd_data                                                   ; 8859: 8c 05 0f    ...
    ldy #&11                                                          ; 885c: a0 11       ..             ; Y=function code for HDRFN
    ldx #1                                                            ; 885e: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8860: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8863: 68          h
    ldx fs_cmd_data                                                   ; 8864: ae 05 0f    ...
    bne c886c                                                         ; 8867: d0 03       ..
    jsr clear_fs_flag                                                 ; 8869: 20 51 86     Q.
; &886c referenced 4 times by &87f9, &883f, &8856, &8867
.c886c
    pla                                                               ; 886c: 68          h
    ldy fs_block_offset                                               ; 886d: a4 bc       ..
    rts                                                               ; 886f: 60          `

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
; &8870 referenced 1 time by &8767
.filev_attrib_dispatch
    sta fs_cmd_data                                                   ; 8870: 8d 05 0f    ...
    cmp #6                                                            ; 8873: c9 06       ..
    beq cha6                                                          ; 8875: f0 3f       .?
    bcs c88c1                                                         ; 8877: b0 48       .H
    cmp #5                                                            ; 8879: c9 05       ..
    beq cha5                                                          ; 887b: f0 52       .R
    cmp #4                                                            ; 887d: c9 04       ..
    beq cha4                                                          ; 887f: f0 44       .D
    cmp #1                                                            ; 8881: c9 01       ..
    beq get_file_protection                                           ; 8883: f0 15       ..
    asl a                                                             ; 8885: 0a          .
    asl a                                                             ; 8886: 0a          .
    tay                                                               ; 8887: a8          .
    jsr sub_3_from_y                                                  ; 8888: 20 f1 87     ..
    ldx #3                                                            ; 888b: a2 03       ..
; &888d referenced 1 time by &8894
.chalp1
    lda (fs_options),y                                                ; 888d: b1 bb       ..
    sta l0f06,x                                                       ; 888f: 9d 06 0f    ...
    dey                                                               ; 8892: 88          .
    dex                                                               ; 8893: ca          .
    bpl chalp1                                                        ; 8894: 10 f7       ..
    ldx #5                                                            ; 8896: a2 05       ..
    bne copy_filename_to_cmd                                          ; 8898: d0 15       ..             ; ALWAYS branch

; &889a referenced 1 time by &8883
.get_file_protection
    jsr decode_attribs_6bit                                           ; 889a: 20 b1 85     ..
    sta l0f0e                                                         ; 889d: 8d 0e 0f    ...
    ldy #9                                                            ; 88a0: a0 09       ..
    ldx #8                                                            ; 88a2: a2 08       ..
; &88a4 referenced 1 time by &88ab
.chalp2
    lda (fs_options),y                                                ; 88a4: b1 bb       ..
    sta fs_cmd_data,x                                                 ; 88a6: 9d 05 0f    ...
    dey                                                               ; 88a9: 88          .
    dex                                                               ; 88aa: ca          .
    bne chalp2                                                        ; 88ab: d0 f7       ..
    ldx #&0a                                                          ; 88ad: a2 0a       ..
; &88af referenced 2 times by &8898, &88cd
.copy_filename_to_cmd
    jsr sub_c8d45                                                     ; 88af: 20 45 8d     E.
    ldy #&13                                                          ; 88b2: a0 13       ..
    bne c88bb                                                         ; 88b4: d0 05       ..             ; ALWAYS branch

; &88b6 referenced 1 time by &8875
.cha6
    jsr sub_c8d43                                                     ; 88b6: 20 43 8d     C.
    ldy #&14                                                          ; 88b9: a0 14       ..
; &88bb referenced 1 time by &88b4
.c88bb
    bit l8374                                                         ; 88bb: 2c 74 83    ,t.
    jsr init_tx_ctrl_data                                             ; 88be: 20 8b 83     ..
; &88c1 referenced 1 time by &8877
.c88c1
    bcs c8905                                                         ; 88c1: b0 42       .B
    bcc c8936                                                         ; 88c3: 90 71       .q             ; ALWAYS branch

; &88c5 referenced 1 time by &887f
.cha4
    jsr decode_attribs_6bit                                           ; 88c5: 20 b1 85     ..
    sta l0f06                                                         ; 88c8: 8d 06 0f    ...
    ldx #2                                                            ; 88cb: a2 02       ..
    bne copy_filename_to_cmd                                          ; 88cd: d0 e0       ..             ; ALWAYS branch

; &88cf referenced 1 time by &887b
.cha5
    ldx #1                                                            ; 88cf: a2 01       ..
    jsr sub_c8d45                                                     ; 88d1: 20 45 8d     E.
    ldy #&12                                                          ; 88d4: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88d6: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    lda l0f11                                                         ; 88d9: ad 11 0f    ...
    stx l0f11                                                         ; 88dc: 8e 11 0f    ...            ; X=0 on success, &D6 on not-found
    stx l0f14                                                         ; 88df: 8e 14 0f    ...
    jsr decode_attribs_5bit                                           ; 88e2: 20 bb 85     ..
    ldy #&0e                                                          ; 88e5: a0 0e       ..
    sta (fs_options),y                                                ; 88e7: 91 bb       ..
    dey                                                               ; 88e9: 88          .              ; Y=&0d
    ldx #&0c                                                          ; 88ea: a2 0c       ..
; &88ec referenced 1 time by &88f3
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 88ec: bd 05 0f    ...
    sta (fs_options),y                                                ; 88ef: 91 bb       ..
    dey                                                               ; 88f1: 88          .
    dex                                                               ; 88f2: ca          .
    bne copy_fs_reply_to_cb                                           ; 88f3: d0 f7       ..
    inx                                                               ; 88f5: e8          .
    inx                                                               ; 88f6: e8          .
    ldy #&11                                                          ; 88f7: a0 11       ..
; &88f9 referenced 1 time by &8900
.cha5lp
    lda l0f12,x                                                       ; 88f9: bd 12 0f    ...
    sta (fs_options),y                                                ; 88fc: 91 bb       ..
    dey                                                               ; 88fe: 88          .
    dex                                                               ; 88ff: ca          .
    bpl cha5lp                                                        ; 8900: 10 f7       ..
    lda fs_cmd_data                                                   ; 8902: ad 05 0f    ...
; &8905 referenced 1 time by &88c1
.c8905
    bpl c8954                                                         ; 8905: 10 4d       .M
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
    jsr save_fscv_args                                                ; 8907: 20 a6 85     ..
    cmp #3                                                            ; 890a: c9 03       ..
    bcs restore_args_return                                           ; 890c: b0 44       .D
    cpy #0                                                            ; 890e: c0 00       ..
    beq c8959                                                         ; 8910: f0 47       .G
    jsr handle_to_mask_clc                                            ; 8912: 20 1c 86     ..
    sty fs_cmd_data                                                   ; 8915: 8c 05 0f    ...
    lsr a                                                             ; 8918: 4a          J
    sta l0f06                                                         ; 8919: 8d 06 0f    ...
    bcs save_args_handle                                              ; 891c: b0 1a       ..
    ldy #&0c                                                          ; 891e: a0 0c       ..             ; Y=function code for HDRFN
    ldx #2                                                            ; 8920: a2 02       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8922: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 8925: 85 bd       ..             ; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 8927: a6 bb       ..
    ldy #2                                                            ; 8929: a0 02       ..
    sta l0003,x                                                       ; 892b: 95 03       ..
; &892d referenced 1 time by &8934
.loop_c892d
    lda fs_cmd_data,y                                                 ; 892d: b9 05 0f    ...
    sta l0002,x                                                       ; 8930: 95 02       ..
    dex                                                               ; 8932: ca          .
    dey                                                               ; 8933: 88          .
    bpl loop_c892d                                                    ; 8934: 10 f7       ..
; &8936 referenced 1 time by &88c3
.c8936
    bcc restore_args_return                                           ; 8936: 90 1a       ..
; &8938 referenced 1 time by &891c
.save_args_handle
    tya                                                               ; 8938: 98          .
    pha                                                               ; 8939: 48          H
    ldy #3                                                            ; 893a: a0 03       ..
; &893c referenced 1 time by &8943
.loop_c893c
    lda l0003,x                                                       ; 893c: b5 03       ..
    sta l0f07,y                                                       ; 893e: 99 07 0f    ...
    dex                                                               ; 8941: ca          .
    dey                                                               ; 8942: 88          .
    bpl loop_c893c                                                    ; 8943: 10 f7       ..
    ldy #&0d                                                          ; 8945: a0 0d       ..             ; Y=function code for HDRFN
    ldx #5                                                            ; 8947: a2 05       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8949: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 894c: 86 bd       ..             ; X=0 on success, &D6 on not-found
    pla                                                               ; 894e: 68          h
    jsr l8659                                                         ; 894f: 20 59 86     Y.
; ***************************************************************************************
; Restore arguments and return
; 
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
; fs_block_offset (&BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; ***************************************************************************************
; &8952 referenced 7 times by &87ce, &890c, &8936, &8961, &89c8, &8a19, &8e1d
.restore_args_return
    lda fs_last_byte_flag                                             ; 8952: a5 bd       ..
; &8954 referenced 5 times by &8905, &895e, &896d, &8998, &89ac
.c8954
    ldx fs_options                                                    ; 8954: a6 bb       ..
    ldy fs_block_offset                                               ; 8956: a4 bc       ..
    rts                                                               ; 8958: 60          `

; &8959 referenced 1 time by &8910
.c8959
    tay                                                               ; 8959: a8          .
    bne c8960                                                         ; 895a: d0 04       ..
    lda #5                                                            ; 895c: a9 05       ..
    bne c8954                                                         ; 895e: d0 f4       ..             ; ALWAYS branch

; &8960 referenced 1 time by &895a
.c8960
    lsr a                                                             ; 8960: 4a          J
    bne restore_args_return                                           ; 8961: d0 ef       ..
; &8963 referenced 1 time by &8969
.osarg1
    lda fs_cmd_context,y                                              ; 8963: b9 0a 0e    ...
    sta (fs_options),y                                                ; 8966: 91 bb       ..
    dey                                                               ; 8968: 88          .
    bpl osarg1                                                        ; 8969: 10 f8       ..
; &896b referenced 3 times by &897b, &8ab9, &8b56
.c896b
    lda #0                                                            ; 896b: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl c8954                                                         ; 896d: 10 e5       ..             ; ALWAYS branch

; ***************************************************************************************
; FINDV handler (OSFIND entry point)
; 
;   A=0: close file -- delegates to close_handle (&89AE)
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
    jsr l859c                                                         ; 896f: 20 9c 85     ..
    sec                                                               ; 8972: 38          8
    jsr handle_to_mask                                                ; 8973: 20 1d 86     ..            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 8976: aa          .              ; A=preserved
    beq close_handle                                                  ; 8977: f0 35       .5
    and #&3f ; '?'                                                    ; 8979: 29 3f       )?
    bne c896b                                                         ; 897b: d0 ee       ..
    txa                                                               ; 897d: 8a          .
    eor #&80                                                          ; 897e: 49 80       I.
    asl a                                                             ; 8980: 0a          .
    sta fs_cmd_data                                                   ; 8981: 8d 05 0f    ...
    rol a                                                             ; 8984: 2a          *
    sta l0f06                                                         ; 8985: 8d 06 0f    ...
    jsr parse_filename_gs                                             ; 8988: 20 ba 86     ..
    ldx #2                                                            ; 898b: a2 02       ..
    jsr sub_c8d45                                                     ; 898d: 20 45 8d     E.
    ldy #6                                                            ; 8990: a0 06       ..
    bit l8374                                                         ; 8992: 2c 74 83    ,t.
    jsr init_tx_ctrl_data                                             ; 8995: 20 8b 83     ..
    bcs c8954                                                         ; 8998: b0 ba       ..
    lda fs_cmd_data                                                   ; 899a: ad 05 0f    ...
    tax                                                               ; 899d: aa          .
    jsr l8659                                                         ; 899e: 20 59 86     Y.
; 3.35K fix: OR handle bit into fs_sequence_nos
; (&0E08). Without this, a newly opened file could
; inherit a stale sequence number from a previous
; file using the same handle, causing byte-stream
; protocol errors.
    txa                                                               ; 89a1: 8a          .
    ora fs_sequence_nos                                               ; 89a2: 0d 08 0e    ...
    sta fs_sequence_nos                                               ; 89a5: 8d 08 0e    ...
    txa                                                               ; 89a8: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 89a9: 20 38 86     8.            ; Convert bitmask to handle number (FS2A)
    bne c8954                                                         ; 89ac: d0 a6       ..
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
; &89ae referenced 1 time by &8977
.close_handle
    tya                                                               ; 89ae: 98          .              ; Y=preserved
    bne close_single_handle                                           ; 89af: d0 07       ..
    lda #osbyte_close_spool_exec                                      ; 89b1: a9 77       .w
    jsr osbyte                                                        ; 89b3: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 89b6: a0 00       ..
; &89b8 referenced 1 time by &89af
.close_single_handle
    sty fs_cmd_data                                                   ; 89b8: 8c 05 0f    ...
    ldx #1                                                            ; 89bb: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 89bd: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89bf: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 89c2: ad 05 0f    ...
    jsr l8659                                                         ; 89c5: 20 59 86     Y.
; &89c8 referenced 1 time by &89ec
.c89c8
    bcc restore_args_return                                           ; 89c8: 90 88       ..
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; ***************************************************************************************
.opt_handler
    cpx #4                                                            ; 89ca: e0 04       ..
    bne c89d2                                                         ; 89cc: d0 04       ..
    cpy #4                                                            ; 89ce: c0 04       ..
    bcc optl1                                                         ; 89d0: 90 0d       ..
; &89d2 referenced 1 time by &89cc
.c89d2
    dex                                                               ; 89d2: ca          .
    bne opter1                                                        ; 89d3: d0 05       ..
    sty fs_messages_flag                                              ; 89d5: 8c 06 0e    ...
    bcc c89ec                                                         ; 89d8: 90 12       ..
; &89da referenced 1 time by &89d3
.opter1
    lda #7                                                            ; 89da: a9 07       ..
    jmp nlisne                                                        ; 89dc: 4c cd 84    L..

; &89df referenced 1 time by &89d0
.optl1
    sty fs_cmd_data                                                   ; 89df: 8c 05 0f    ...
    ldy #&16                                                          ; 89e2: a0 16       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89e4: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 89e7: a4 bc       ..
    sty fs_boot_option                                                ; 89e9: 8c 05 0e    ...
; &89ec referenced 1 time by &89d8
.c89ec
    bcc c89c8                                                         ; 89ec: 90 da       ..
; &89ee referenced 1 time by &8aad
.adjust_addrs_9
    ldy #9                                                            ; 89ee: a0 09       ..
    jsr adjust_addrs_clc                                              ; 89f0: 20 f5 89     ..
; &89f3 referenced 1 time by &8b9d
.adjust_addrs_1
    ldy #1                                                            ; 89f3: a0 01       ..
; &89f5 referenced 1 time by &89f0
.adjust_addrs_clc
    clc                                                               ; 89f5: 18          .
; ***************************************************************************************
; Bidirectional 4-byte address adjustment
; 
; Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
;   If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
;   If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
; Starting offset X=&FC means it reads from &0E06-&0E09 area.
; Used to convert between absolute and relative file positions.
; ***************************************************************************************
; &89f6 referenced 2 times by &8ab3, &8ba9
.adjust_addrs
    ldx #&fc                                                          ; 89f6: a2 fc       ..
; &89f8 referenced 1 time by &8a0b
.loop_c89f8
    lda (fs_options),y                                                ; 89f8: b1 bb       ..
    bit fs_load_addr_2                                                ; 89fa: 24 b2       $.
    bmi c8a04                                                         ; 89fc: 30 06       0.
    adc fs_cmd_context,x                                              ; 89fe: 7d 0a 0e    }..
    jmp gbpbx                                                         ; 8a01: 4c 07 8a    L..

; &8a04 referenced 1 time by &89fc
.c8a04
    sbc fs_cmd_context,x                                              ; 8a04: fd 0a 0e    ...
; &8a07 referenced 1 time by &8a01
.gbpbx
    sta (fs_options),y                                                ; 8a07: 91 bb       ..
    iny                                                               ; 8a09: c8          .
    inx                                                               ; 8a0a: e8          .
    bne loop_c89f8                                                    ; 8a0b: d0 eb       ..
    rts                                                               ; 8a0d: 60          `

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
    jsr save_fscv_args                                                ; 8a0e: 20 a6 85     ..
    tax                                                               ; 8a11: aa          .
    beq c8a19                                                         ; 8a12: f0 05       ..
    dex                                                               ; 8a14: ca          .
    cpx #8                                                            ; 8a15: e0 08       ..
    bcc gbpbx1                                                        ; 8a17: 90 03       ..
; &8a19 referenced 1 time by &8a12
.c8a19
    jmp restore_args_return                                           ; 8a19: 4c 52 89    LR.

; &8a1c referenced 1 time by &8a17
.gbpbx1
    txa                                                               ; 8a1c: 8a          .
    ldy #0                                                            ; 8a1d: a0 00       ..
    pha                                                               ; 8a1f: 48          H
    cmp #4                                                            ; 8a20: c9 04       ..
    bcc gbpbe1                                                        ; 8a22: 90 03       ..
    jmp osgbpb_info                                                   ; 8a24: 4c d1 8a    L..

; &8a27 referenced 1 time by &8a22
.gbpbe1
    lda (fs_options),y                                                ; 8a27: b1 bb       ..
    jsr handle_to_mask_a                                              ; 8a29: 20 1b 86     ..
    sty fs_cmd_data                                                   ; 8a2c: 8c 05 0f    ...
    ldy #&0b                                                          ; 8a2f: a0 0b       ..
    ldx #6                                                            ; 8a31: a2 06       ..
; &8a33 referenced 1 time by &8a3f
.gbpbf1
    lda (fs_options),y                                                ; 8a33: b1 bb       ..
    sta l0f06,x                                                       ; 8a35: 9d 06 0f    ...
    dey                                                               ; 8a38: 88          .
    cpy #8                                                            ; 8a39: c0 08       ..
    bne gbpbx0                                                        ; 8a3b: d0 01       ..
    dey                                                               ; 8a3d: 88          .
; &8a3e referenced 1 time by &8a3b
.gbpbx0
.gbpbf2
    dex                                                               ; 8a3e: ca          .
    bne gbpbf1                                                        ; 8a3f: d0 f2       ..
    pla                                                               ; 8a41: 68          h
    lsr a                                                             ; 8a42: 4a          J
    pha                                                               ; 8a43: 48          H
    bcc gbpbl1                                                        ; 8a44: 90 01       ..
    inx                                                               ; 8a46: e8          .
; &8a47 referenced 1 time by &8a44
.gbpbl1
    stx l0f06                                                         ; 8a47: 8e 06 0f    ...
    ldy #&0b                                                          ; 8a4a: a0 0b       ..
    ldx #&91                                                          ; 8a4c: a2 91       ..
    pla                                                               ; 8a4e: 68          h
    pha                                                               ; 8a4f: 48          H
    beq c8a55                                                         ; 8a50: f0 03       ..
    ldx #&92                                                          ; 8a52: a2 92       ..
    dey                                                               ; 8a54: 88          .              ; Y=&0a
; &8a55 referenced 1 time by &8a50
.c8a55
    stx fs_cmd_urd                                                    ; 8a55: 8e 02 0f    ...
    stx fs_error_ptr                                                  ; 8a58: 86 b8       ..
    ldx #8                                                            ; 8a5a: a2 08       ..
    lda fs_cmd_data                                                   ; 8a5c: ad 05 0f    ...
    jsr prepare_cmd_with_flag                                         ; 8a5f: 20 7a 83     z.
    lda l00b3                                                         ; 8a62: a5 b3       ..
    sta fs_sequence_nos                                               ; 8a64: 8d 08 0e    ...
    ldx #4                                                            ; 8a67: a2 04       ..
; &8a69 referenced 1 time by &8a7d
.gbpbl3
    lda (fs_options),y                                                ; 8a69: b1 bb       ..
    sta l00af,y                                                       ; 8a6b: 99 af 00    ...
    sta l00c7,y                                                       ; 8a6e: 99 c7 00    ...
    jsr add_4_to_y                                                    ; 8a71: 20 de 87     ..
    adc (fs_options),y                                                ; 8a74: 71 bb       q.
    sta l00af,y                                                       ; 8a76: 99 af 00    ...
    jsr sub_3_from_y                                                  ; 8a79: 20 f1 87     ..
    dex                                                               ; 8a7c: ca          .
    bne gbpbl3                                                        ; 8a7d: d0 ea       ..
    inx                                                               ; 8a7f: e8          .
; &8a80 referenced 1 time by &8a87
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8a80: bd 03 0f    ...
    sta l0f06,x                                                       ; 8a83: 9d 06 0f    ...
    dex                                                               ; 8a86: ca          .
    bpl gbpbf3                                                        ; 8a87: 10 f7       ..
    pla                                                               ; 8a89: 68          h
    bne c8a94                                                         ; 8a8a: d0 08       ..
    lda fs_cmd_urd                                                    ; 8a8c: ad 02 0f    ...
    jsr transfer_file_blocks                                          ; 8a8f: 20 f5 87     ..
    bne c8a97                                                         ; 8a92: d0 03       ..
; &8a94 referenced 1 time by &8a8a
.c8a94
    jsr send_data_blocks                                              ; 8a94: 20 3a 87     :.
; &8a97 referenced 1 time by &8a92
.c8a97
    lda #&2a ; '*'                                                    ; 8a97: a9 2a       .*
    sta fs_error_ptr                                                  ; 8a99: 85 b8       ..
    jsr send_fs_reply_cmd                                             ; 8a9b: 20 ba 83     ..
    lda (fs_options,x)                                                ; 8a9e: a1 bb       ..
    bit fs_cmd_data                                                   ; 8aa0: 2c 05 0f    ,..
    bmi c8aa8                                                         ; 8aa3: 30 03       0.
    jsr clear_fs_flag                                                 ; 8aa5: 20 51 86     Q.
; &8aa8 referenced 1 time by &8aa3
.c8aa8
    jsr l8659                                                         ; 8aa8: 20 59 86     Y.
    stx fs_load_addr_2                                                ; 8aab: 86 b2       ..
    jsr adjust_addrs_9                                                ; 8aad: 20 ee 89     ..
    dec fs_load_addr_2                                                ; 8ab0: c6 b2       ..
    sec                                                               ; 8ab2: 38          8
    jsr adjust_addrs                                                  ; 8ab3: 20 f6 89     ..
    asl fs_cmd_data                                                   ; 8ab6: 0e 05 0f    ...
    jmp c896b                                                         ; 8ab9: 4c 6b 89    Lk.

; &8abc referenced 1 time by &8aec
.c8abc
    ldy #&15                                                          ; 8abc: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8abe: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8ac1: ad 05 0e    ...
    sta l0f16                                                         ; 8ac4: 8d 16 0f    ...
    stx fs_load_addr                                                  ; 8ac7: 86 b0       ..             ; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8ac9: 86 b1       ..
    lda #&12                                                          ; 8acb: a9 12       ..
    sta fs_load_addr_2                                                ; 8acd: 85 b2       ..
    bne copy_reply_to_caller                                          ; 8acf: d0 4e       .N             ; ALWAYS branch

; ***************************************************************************************
; OSGBPB 5-8 info handler (OSINFO)
; 
; Handles the "messy interface tacked onto OSGBPB" (original source).
; Checks whether the destination address is in Tube space by comparing
; the high bytes against TBFLAG. If in Tube space, data must be
; copied via the Tube FIFO registers (with delays to accommodate the
; slow 16032 co-processor) instead of direct memory access.
; ***************************************************************************************
; &8ad1 referenced 1 time by &8a24
.osgbpb_info
    ldy #4                                                            ; 8ad1: a0 04       ..
    lda tx_in_progress                                                ; 8ad3: ad 52 0d    .R.
    beq c8adf                                                         ; 8ad6: f0 07       ..
    cmp (fs_options),y                                                ; 8ad8: d1 bb       ..
    bne c8adf                                                         ; 8ada: d0 03       ..
    dey                                                               ; 8adc: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8add: f1 bb       ..
; &8adf referenced 2 times by &8ad6, &8ada
.c8adf
    sta rom_svc_num                                                   ; 8adf: 85 ce       ..
; &8ae1 referenced 1 time by &8ae7
.info2
    lda (fs_options),y                                                ; 8ae1: b1 bb       ..
    sta fs_last_byte_flag,y                                           ; 8ae3: 99 bd 00    ...
    dey                                                               ; 8ae6: 88          .
    bne info2                                                         ; 8ae7: d0 f8       ..
    pla                                                               ; 8ae9: 68          h
    and #3                                                            ; 8aea: 29 03       ).
    beq c8abc                                                         ; 8aec: f0 ce       ..
    lsr a                                                             ; 8aee: 4a          J
    beq c8af3                                                         ; 8aef: f0 02       ..
    bcs c8b59                                                         ; 8af1: b0 66       .f
; &8af3 referenced 1 time by &8aef
.c8af3
    tay                                                               ; 8af3: a8          .              ; Y=function code
    lda fs_csd_handle,y                                               ; 8af4: b9 03 0e    ...
    sta fs_cmd_csd                                                    ; 8af7: 8d 03 0f    ...
    lda fs_lib_handle                                                 ; 8afa: ad 04 0e    ...
    sta fs_cmd_lib                                                    ; 8afd: 8d 04 0f    ...
    lda fs_urd_handle                                                 ; 8b00: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8b03: 8d 02 0f    ...
    ldx #&12                                                          ; 8b06: a2 12       ..             ; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8b08: 8e 01 0f    ...
    lda #&0d                                                          ; 8b0b: a9 0d       ..
    sta l0f06                                                         ; 8b0d: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b10: 85 b2       ..
    lsr a                                                             ; 8b12: 4a          J              ; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8b13: 8d 05 0f    ...
    clc                                                               ; 8b16: 18          .
    jsr build_send_fs_cmd                                             ; 8b17: 20 a4 83     ..            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8b1a: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8b1c: e8          .
    stx fs_load_addr                                                  ; 8b1d: 86 b0       ..
; &8b1f referenced 2 times by &8acf, &8b92
.copy_reply_to_caller
    lda rom_svc_num                                                   ; 8b1f: a5 ce       ..
    bne c8b34                                                         ; 8b21: d0 11       ..
    ldx fs_load_addr                                                  ; 8b23: a6 b0       ..
    ldy fs_load_addr_hi                                               ; 8b25: a4 b1       ..
; &8b27 referenced 1 time by &8b30
.loop_c8b27
    lda fs_cmd_data,x                                                 ; 8b27: bd 05 0f    ...
    sta (fs_crc_lo),y                                                 ; 8b2a: 91 be       ..
    inx                                                               ; 8b2c: e8          .
    iny                                                               ; 8b2d: c8          .
    dec fs_load_addr_2                                                ; 8b2e: c6 b2       ..
    bne loop_c8b27                                                    ; 8b30: d0 f5       ..
    beq c8b56                                                         ; 8b32: f0 22       ."             ; ALWAYS branch

; &8b34 referenced 1 time by &8b21
.c8b34
    jsr tube_claim_loop                                               ; 8b34: 20 ae 8b     ..
    lda #1                                                            ; 8b37: a9 01       ..
    ldx fs_options                                                    ; 8b39: a6 bb       ..
    ldy fs_block_offset                                               ; 8b3b: a4 bc       ..
    inx                                                               ; 8b3d: e8          .
    bne c8b41                                                         ; 8b3e: d0 01       ..
    iny                                                               ; 8b40: c8          .
; &8b41 referenced 1 time by &8b3e
.c8b41
    jsr tube_addr_claim                                               ; 8b41: 20 06 04     ..
    ldx fs_load_addr                                                  ; 8b44: a6 b0       ..
; &8b46 referenced 1 time by &8b4f
.tbcop1
    lda fs_cmd_data,x                                                 ; 8b46: bd 05 0f    ...
    sta tube_data_register_3                                          ; 8b49: 8d e5 fe    ...
    inx                                                               ; 8b4c: e8          .
    dec fs_load_addr_2                                                ; 8b4d: c6 b2       ..
    bne tbcop1                                                        ; 8b4f: d0 f5       ..
    lda #&83                                                          ; 8b51: a9 83       ..
    jsr tube_addr_claim                                               ; 8b53: 20 06 04     ..
; &8b56 referenced 2 times by &8b32, &8bac
.c8b56
    jmp c896b                                                         ; 8b56: 4c 6b 89    Lk.

; &8b59 referenced 1 time by &8af1
.c8b59
    ldy #9                                                            ; 8b59: a0 09       ..
    lda (fs_options),y                                                ; 8b5b: b1 bb       ..
    sta l0f06                                                         ; 8b5d: 8d 06 0f    ...
    ldy #5                                                            ; 8b60: a0 05       ..
    lda (fs_options),y                                                ; 8b62: b1 bb       ..
    sta l0f07                                                         ; 8b64: 8d 07 0f    ...
    ldx #&0d                                                          ; 8b67: a2 0d       ..             ; X=preserved through header build
    stx l0f08                                                         ; 8b69: 8e 08 0f    ...
    ldy #2                                                            ; 8b6c: a0 02       ..
    sty fs_load_addr                                                  ; 8b6e: 84 b0       ..
    sty fs_cmd_data                                                   ; 8b70: 8c 05 0f    ...
    iny                                                               ; 8b73: c8          .              ; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b74: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b77: 86 b1       ..             ; X=0 on success, &D6 on not-found
    lda l0f06                                                         ; 8b79: ad 06 0f    ...
    sta (fs_options,x)                                                ; 8b7c: 81 bb       ..
    lda fs_cmd_data                                                   ; 8b7e: ad 05 0f    ...
    ldy #9                                                            ; 8b81: a0 09       ..
    adc (fs_options),y                                                ; 8b83: 71 bb       q.
    sta (fs_options),y                                                ; 8b85: 91 bb       ..
    lda l00c8                                                         ; 8b87: a5 c8       ..
    sbc #7                                                            ; 8b89: e9 07       ..
    sta l0f06                                                         ; 8b8b: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b8e: 85 b2       ..
    beq c8b95                                                         ; 8b90: f0 03       ..
    jsr copy_reply_to_caller                                          ; 8b92: 20 1f 8b     ..
; &8b95 referenced 1 time by &8b90
.c8b95
    ldx #2                                                            ; 8b95: a2 02       ..
; &8b97 referenced 1 time by &8b9b
.loop_c8b97
    sta l0f07,x                                                       ; 8b97: 9d 07 0f    ...
    dex                                                               ; 8b9a: ca          .
    bpl loop_c8b97                                                    ; 8b9b: 10 fa       ..
    jsr adjust_addrs_1                                                ; 8b9d: 20 f3 89     ..
    sec                                                               ; 8ba0: 38          8
    dec fs_load_addr_2                                                ; 8ba1: c6 b2       ..
    lda fs_cmd_data                                                   ; 8ba3: ad 05 0f    ...
    sta l0f06                                                         ; 8ba6: 8d 06 0f    ...
    jsr adjust_addrs                                                  ; 8ba9: 20 f6 89     ..
    beq c8b56                                                         ; 8bac: f0 a8       ..
; &8bae referenced 3 times by &8b34, &8bb3, &8e06
.tube_claim_loop
    lda #&c3                                                          ; 8bae: a9 c3       ..
    jsr tube_addr_claim                                               ; 8bb0: 20 06 04     ..
    bcc tube_claim_loop                                               ; 8bb3: 90 f9       ..
    rts                                                               ; 8bb5: 60          `

; ***************************************************************************************
; FSCV 2/3/4: unrecognised * command handler (DECODE)
; 
; CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text
; against the table
; at &8BE4 using case-insensitive comparison with abbreviation
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
; &8bb6 referenced 1 time by &8275
.fscv_star_handler
    jsr l859c                                                         ; 8bb6: 20 9c 85     ..
    ldx #&ff                                                          ; 8bb9: a2 ff       ..
    stx l00b9                                                         ; 8bbb: 86 b9       ..
; &8bbd referenced 1 time by &8bd8
.loop_c8bbd
    ldy #&ff                                                          ; 8bbd: a0 ff       ..
; &8bbf referenced 1 time by &8bca
.decfir
    iny                                                               ; 8bbf: c8          .
    inx                                                               ; 8bc0: e8          .
; &8bc1 referenced 1 time by &8bdc
.decmor
    lda fs_cmd_match_table,x                                          ; 8bc1: bd e4 8b    ...
    bmi c8bde                                                         ; 8bc4: 30 18       0.
    eor (fs_crc_lo),y                                                 ; 8bc6: 51 be       Q.
    and #&df                                                          ; 8bc8: 29 df       ).
    beq decfir                                                        ; 8bca: f0 f3       ..
    dex                                                               ; 8bcc: ca          .
; &8bcd referenced 1 time by &8bd1
.decmin
    inx                                                               ; 8bcd: e8          .
    lda fs_cmd_match_table,x                                          ; 8bce: bd e4 8b    ...
    bpl decmin                                                        ; 8bd1: 10 fa       ..
    lda (fs_crc_lo),y                                                 ; 8bd3: b1 be       ..
    inx                                                               ; 8bd5: e8          .
    cmp #&2e ; '.'                                                    ; 8bd6: c9 2e       ..
    bne loop_c8bbd                                                    ; 8bd8: d0 e3       ..
    iny                                                               ; 8bda: c8          .
    dex                                                               ; 8bdb: ca          .
    bcs decmor                                                        ; 8bdc: b0 e3       ..
; &8bde referenced 1 time by &8bc4
.c8bde
    pha                                                               ; 8bde: 48          H
    lda l8be5,x                                                       ; 8bdf: bd e5 8b    ...
    pha                                                               ; 8be2: 48          H
    rts                                                               ; 8be3: 60          `

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
;   "EX"     → &8BFA (ex_handler: extended catalogue)
;   "BYE"\r  → &8383 (bye_handler: logoff)
;   <catch-all> → &80B4 (forward anything else to FS)
; ***************************************************************************************
; &8be4 referenced 2 times by &8bc1, &8bce
.fs_cmd_match_table
l8be5 = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8be4: 49 2e       I.
; &8be5 referenced 1 time by &8bdf
    equb &80, &b3                                                     ; 8be6: 80 b3       ..
    equs "I AM"                                                       ; 8be8: 49 20 41... I A
    equb &80                                                          ; 8bec: 80          .
    equs "}EX"                                                        ; 8bed: 7d 45 58    }EX
    equb &8b, &f9                                                     ; 8bf0: 8b f9       ..
    equs "BYE"                                                        ; 8bf2: 42 59 45    BYE
    equb &0d, &83, &82, &80, &b3                                      ; 8bf5: 0d 83 82... ...

; ***************************************************************************************
; *EX handler (extended catalogue)
; 
; Sets &B7=&01 and &B5=&03, then branches into cat_handler at
; &8C0A, bypassing cat_handler's default column setup. &B7=1
; gives one entry per line with full details (vs &B7=3 for *CAT
; which gives multiple files per line).
; ***************************************************************************************
.ex_handler
    ldx #1                                                            ; 8bfa: a2 01       ..
    stx l00b7                                                         ; 8bfc: 86 b7       ..
    lda #3                                                            ; 8bfe: a9 03       ..
    bne c8c0c                                                         ; 8c00: d0 0a       ..             ; ALWAYS branch

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
.cat_handler
    ldx #3                                                            ; 8c02: a2 03       ..
    stx l00b7                                                         ; 8c04: 86 b7       ..
    ldy #0                                                            ; 8c06: a0 00       ..
    sty l00b9                                                         ; 8c08: 84 b9       ..
    lda #&0b                                                          ; 8c0a: a9 0b       ..
; &8c0c referenced 1 time by &8c00
.c8c0c
    sta l00b5                                                         ; 8c0c: 85 b5       ..
    lda #6                                                            ; 8c0e: a9 06       ..
    sta fs_cmd_data                                                   ; 8c10: 8d 05 0f    ...
    jsr sub_c86bc                                                     ; 8c13: 20 bc 86     ..
    ldx #1                                                            ; 8c16: a2 01       ..
    jsr sub_c8d45                                                     ; 8c18: 20 45 8d     E.
    ldy #&12                                                          ; 8c1b: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c1d: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c20: a2 03       ..
    jsr sub_c8db2                                                     ; 8c22: 20 b2 8d     ..
    jsr print_inline                                                  ; 8c25: 20 d9 85     ..
    equs "("                                                          ; 8c28: 28          (

    lda l0f13                                                         ; 8c29: ad 13 0f    ...
    jsr print_decimal                                                 ; 8c2c: 20 7e 8d     ~.
    jsr print_inline                                                  ; 8c2f: 20 d9 85     ..
    equs ")     "                                                     ; 8c32: 29 20 20... )

    ldx l0f12                                                         ; 8c38: ae 12 0f    ...
    bne c8c48                                                         ; 8c3b: d0 0b       ..
    jsr print_inline                                                  ; 8c3d: 20 d9 85     ..
    equs "Owner", &0d                                                 ; 8c40: 4f 77 6e... Own

    bne c8c52                                                         ; 8c46: d0 0a       ..
; &8c48 referenced 1 time by &8c3b
.c8c48
    jsr print_inline                                                  ; 8c48: 20 d9 85     ..
    equs "Public", &0d                                                ; 8c4b: 50 75 62... Pub

; &8c52 referenced 1 time by &8c46
.c8c52
    ldy #&15                                                          ; 8c52: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c54: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c57: e8          .
    ldy #&10                                                          ; 8c58: a0 10       ..
    jsr print_reply_counted                                           ; 8c5a: 20 b4 8d     ..
    jsr print_inline                                                  ; 8c5d: 20 d9 85     ..
    equs "    Option "                                                ; 8c60: 20 20 20...

    lda fs_boot_option                                                ; 8c6b: ad 05 0e    ...
    tax                                                               ; 8c6e: aa          .
    jsr print_hex                                                     ; 8c6f: 20 9d 8d     ..
    jsr print_inline                                                  ; 8c72: 20 d9 85     ..
    equs " ("                                                         ; 8c75: 20 28        (

    ldy return_9,x                                                    ; 8c77: bc e0 8c    ...
; &8c7a referenced 1 time by &8c83
.loop_c8c7a
    lda return_9,y                                                    ; 8c7a: b9 e0 8c    ...
    bmi c8c85                                                         ; 8c7d: 30 06       0.
    jsr osasci                                                        ; 8c7f: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8c82: c8          .
    bne loop_c8c7a                                                    ; 8c83: d0 f5       ..
; &8c85 referenced 1 time by &8c7d
.c8c85
    jsr print_inline                                                  ; 8c85: 20 d9 85     ..
    equs ")", &0d, "Dir. "                                            ; 8c88: 29 0d 44... ).D

    ldx #&11                                                          ; 8c8f: a2 11       ..
    jsr sub_c8db2                                                     ; 8c91: 20 b2 8d     ..
    jsr print_inline                                                  ; 8c94: 20 d9 85     ..
    equs "     Lib. "                                                 ; 8c97: 20 20 20...

    ldx #&1b                                                          ; 8ca1: a2 1b       ..
    jsr sub_c8db2                                                     ; 8ca3: 20 b2 8d     ..
    jsr print_inline                                                  ; 8ca6: 20 d9 85     ..
    equs &0d, &0d                                                     ; 8ca9: 0d 0d       ..

    sty l0f06                                                         ; 8cab: 8c 06 0f    ...
    sty l00b4                                                         ; 8cae: 84 b4       ..
    ldx l00b5                                                         ; 8cb0: a6 b5       ..
    stx l0f07                                                         ; 8cb2: 8e 07 0f    ...
; &8cb5 referenced 1 time by &8cde
.c8cb5
    ldx l00b7                                                         ; 8cb5: a6 b7       ..
    stx fs_cmd_data                                                   ; 8cb7: 8e 05 0f    ...
    ldx #3                                                            ; 8cba: a2 03       ..
    jsr sub_c8d45                                                     ; 8cbc: 20 45 8d     E.
    ldy #3                                                            ; 8cbf: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cc1: 20 8a 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8cc4: ad 05 0f    ...
    beq c8d23                                                         ; 8cc7: f0 5a       .Z
    ldx #2                                                            ; 8cc9: a2 02       ..
    jsr c8d59                                                         ; 8ccb: 20 59 8d     Y.
    clc                                                               ; 8cce: 18          .
    lda l00b4                                                         ; 8ccf: a5 b4       ..
    adc fs_cmd_data                                                   ; 8cd1: 6d 05 0f    m..
    sta l0f06                                                         ; 8cd4: 8d 06 0f    ...
    sta l00b4                                                         ; 8cd7: 85 b4       ..
    lda l00b5                                                         ; 8cd9: a5 b5       ..
    sta l0f07                                                         ; 8cdb: 8d 07 0f    ...
    bne c8cb5                                                         ; 8cde: d0 d5       ..
; &8ce0 referenced 2 times by &8c77, &8c7a
.return_9
    rts                                                               ; 8ce0: 60          `

    equb &73, &9b, &18                                                ; 8ce1: 73 9b 18    s..
    equs "L.!"                                                        ; 8ce4: 4c 2e 21    L.!
; ***************************************************************************************
; Boot command strings for auto-boot
; 
; The four boot options use OSCLI strings at offsets within page &8C:
;   Option 0 (Off):  offset &F6 → &8CFA = bare CR (empty command)
;   Option 1 (Load): offset &E7 → &8CE8 = "L.!BOOT" (dual-purpose:
;       the JMP &212E instruction at &8CE8 has opcode &4C='L' and
;       operand bytes &2E='.' &21='!', forming the string "L.!")
;   Option 2 (Run):  offset &E9 → &8CE7 = "!BOOT" (bare filename = *RUN)
;   Option 3 (Exec): offset &EF → &8CF0 = "E.!BOOT"
; 
; This is a classic BBC ROM space optimisation: the JMP instruction's
; bytes serve double duty as both executable code and ASCII text.
; ***************************************************************************************
.boot_cmd_strings
    equs "BOOT"                                                       ; 8ce7: 42 4f 4f... BOO
    equb &0d                                                          ; 8ceb: 0d          .
    equs "E.!BOO"                                                     ; 8cec: 45 2e 21... E.!
; ***************************************************************************************
; Boot option → OSCLI string offset table
; 
; Four bytes indexed by the boot option value (0-3). Each byte
; is the low byte of a pointer into page &8C, where the OSCLI
; command string for that boot option lives. See boot_cmd_strings.
; ***************************************************************************************
.boot_option_offsets
    equb &54, &0d                                                     ; 8cf2: 54 0d       T.
; &8cf4 referenced 1 time by &8e33
.l8cf4
    equb &f3, &e4, &e6, &ec, &45, &78                                 ; 8cf4: f3 e4 e6... ...

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to c8cff (JMP c892c) if Y is non-zero.
; ***************************************************************************************
.set_lib_handle
    adc zp_63                                                         ; 8cfa: 65 63       ec
; ***************************************************************************************
; Print file catalogue line
; 
; Displays a formatted catalogue entry: filename (padded to 12
; chars with spaces), load address (4 hex bytes at offset 5-2),
; exec address (4 hex bytes at offset 9-6), and file length
; (3 hex bytes at offset &0C-&0A), followed by a newline.
; Data is read from (fs_crc_lo) for the filename and from
; (fs_options) for the numeric fields. Returns immediately
; if fs_work_0e06 is zero (no info available).
; ***************************************************************************************
; &8cfc referenced 2 times by &8727, &87a7
.print_file_info
    ldy fs_messages_flag                                              ; 8cfc: ac 06 0e    ...
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to c8cff (JMP c892c).
; ***************************************************************************************
.set_csd_handle
    beq return_5                                                      ; 8cff: f0 51       .Q
    ldy #0                                                            ; 8d01: a0 00       ..
; &8d03 referenced 1 time by &8d11
.loop_c8d03
    lda (fs_crc_lo),y                                                 ; 8d03: b1 be       ..
    cmp #&0d                                                          ; 8d05: c9 0d       ..
    beq pad_filename_spaces                                           ; 8d07: f0 0a       ..
    cmp #&20 ; ' '                                                    ; 8d09: c9 20       .
    beq pad_filename_spaces                                           ; 8d0b: f0 06       ..
    jsr osasci                                                        ; 8d0d: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8d10: c8          .
    bne loop_c8d03                                                    ; 8d11: d0 f0       ..
; &8d13 referenced 3 times by &8d07, &8d0b, &8d19
.pad_filename_spaces
    jsr print_space                                                   ; 8d13: 20 3c 8d     <.
    iny                                                               ; 8d16: c8          .
    cpy #&0c                                                          ; 8d17: c0 0c       ..
    bcc pad_filename_spaces                                           ; 8d19: 90 f8       ..
    ldy #5                                                            ; 8d1b: a0 05       ..
    jsr print_hex_bytes                                               ; 8d1d: 20 31 8d     1.
    jsr print_exec_and_len                                            ; 8d20: 20 26 8d     &.
; &8d23 referenced 1 time by &8cc7
.c8d23
    jmp osnewl                                                        ; 8d23: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &8d26 referenced 1 time by &8d20
.print_exec_and_len
    ldy #9                                                            ; 8d26: a0 09       ..
    jsr print_hex_bytes                                               ; 8d28: 20 31 8d     1.
    ldy #&0c                                                          ; 8d2b: a0 0c       ..
    ldx #3                                                            ; 8d2d: a2 03       ..
    bne num01                                                         ; 8d2f: d0 02       ..             ; ALWAYS branch

; &8d31 referenced 2 times by &8d1d, &8d28
.print_hex_bytes
    ldx #4                                                            ; 8d31: a2 04       ..
; ***************************************************************************************
; Option name strings
; 
; Null-terminated strings for the four boot option names:
;   "Off", "Load", "Run", "Exec"
; Used by cat_handler to display the current boot option setting.
; ***************************************************************************************
; &8d33 referenced 2 times by &8d2f, &8d3a
.num01
.option_name_strings
    lda (fs_options),y                                                ; 8d33: b1 bb       ..
    jsr print_hex                                                     ; 8d35: 20 9d 8d     ..
    dey                                                               ; 8d38: 88          .
    dex                                                               ; 8d39: ca          .
    bne num01                                                         ; 8d3a: d0 f7       ..
; &8d3c referenced 1 time by &8d13
.print_space
    lda #&20 ; ' '                                                    ; 8d3c: a9 20       .
    bne c8db0                                                         ; 8d3e: d0 70       .p             ; ALWAYS branch

    equs "Off"                                                        ; 8d40: 4f 66 66    Off

; &8d43 referenced 3 times by &80b4, &88b6, &8dc2
.sub_c8d43
    ldx #0                                                            ; 8d43: a2 00       ..
; &8d45 referenced 6 times by &879d, &88af, &88d1, &898d, &8c18, &8cbc
.sub_c8d45
    ldy #0                                                            ; 8d45: a0 00       ..
; &8d47 referenced 1 time by &8d50
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d47: b1 be       ..
    sta fs_cmd_data,x                                                 ; 8d49: 9d 05 0f    ...
; ***************************************************************************************
; Option name offsets
; 
; Four-byte table of offsets into option_name_strings:
;   0, 4, 9, &0D — one per boot option value (0-3).
; ***************************************************************************************
.option_name_offsets
    inx                                                               ; 8d4c: e8          .
    iny                                                               ; 8d4d: c8          .
    eor #&0d                                                          ; 8d4e: 49 0d       I.
; ***************************************************************************************
; Print reply buffer bytes
; 
; Prints Y characters from the FS reply buffer (&0F05+X) to
; the screen via OSASCI. X = starting offset, Y = count.
; Used by cat_handler to display directory and library names.
; ***************************************************************************************
.print_reply_bytes
    bne copy_string_from_offset                                       ; 8d50: d0 f5       ..
; &8d52 referenced 2 times by &8cff, &8d5c
.return_5
    rts                                                               ; 8d52: 60          `

    equs "Load"                                                       ; 8d53: 4c 6f 61... Loa

.sub_c8d57
    ldx #0                                                            ; 8d57: a2 00       ..
; &8d59 referenced 2 times by &8ccb, &8d79
.c8d59
    lda fs_cmd_data,x                                                 ; 8d59: bd 05 0f    ...
; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
.copy_filename
print_spaces = copy_filename+1
    bmi return_5                                                      ; 8d5c: 30 f4       0.
; ***************************************************************************************
; Print spaces
; 
; Prints X space characters via print_space. Used by cat_handler
; to align columns in the directory listing.
; ***************************************************************************************
; ***************************************************************************************
; Copy string to FS command buffer
; 
; Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
; to &0F05+X, stopping when a CR (&0D) is encountered. The CR
; itself is also copied. Returns with X pointing past the last
; byte written.
; ***************************************************************************************
.copy_string_to_cmd
    bne infol2                                                        ; 8d5e: d0 15       ..
    ldy l00b9                                                         ; 8d60: a4 b9       ..
    bmi c8d73                                                         ; 8d62: 30 0f       0.
    iny                                                               ; 8d64: c8          .
    tya                                                               ; 8d65: 98          .
    and #3                                                            ; 8d66: 29 03       ).
    sta l00b9                                                         ; 8d68: 85 b9       ..
    beq c8d73                                                         ; 8d6a: f0 07       ..
; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by cat_handler to display Dir. and Lib. paths.
; ***************************************************************************************
.print_dir_name
    jsr print_inline                                                  ; 8d6c: 20 d9 85     ..
    equs "  "                                                         ; 8d6f: 20 20

    bne c8d78                                                         ; 8d71: d0 05       ..
; &8d73 referenced 2 times by &8d62, &8d6a
.c8d73
    lda #&0d                                                          ; 8d73: a9 0d       ..
; &8d75 referenced 1 time by &8d5e
.infol2
    jsr osasci                                                        ; 8d75: 20 e3 ff     ..            ; Write character 13
; &8d78 referenced 1 time by &8d71
.c8d78
    inx                                                               ; 8d78: e8          .
    bne c8d59                                                         ; 8d79: d0 de       ..
    equs "Run"                                                        ; 8d7b: 52 75 6e    Run

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
; &8d7e referenced 2 times by &822e, &8c2c
.print_decimal
    tay                                                               ; 8d7e: a8          .
    lda #&64 ; 'd'                                                    ; 8d7f: a9 64       .d
    jsr print_decimal_digit                                           ; 8d81: 20 8b 8d     ..
    lda #&0a                                                          ; 8d84: a9 0a       ..
    jsr print_decimal_digit                                           ; 8d86: 20 8b 8d     ..
    lda #1                                                            ; 8d89: a9 01       ..
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
; &8d8b referenced 2 times by &8d81, &8d86
.print_decimal_digit
    sta fs_error_ptr                                                  ; 8d8b: 85 b8       ..
    tya                                                               ; 8d8d: 98          .
    ldx #&2f ; '/'                                                    ; 8d8e: a2 2f       ./
    sec                                                               ; 8d90: 38          8
; &8d91 referenced 1 time by &8d94
.loop_c8d91
    inx                                                               ; 8d91: e8          .
    sbc fs_error_ptr                                                  ; 8d92: e5 b8       ..
    bcs loop_c8d91                                                    ; 8d94: b0 fb       ..
    adc fs_error_ptr                                                  ; 8d96: 65 b8       e.
    tay                                                               ; 8d98: a8          .
    txa                                                               ; 8d99: 8a          .
; &8d9a referenced 1 time by &8db0
.loop_c8d9a
    jmp osasci                                                        ; 8d9a: 4c e3 ff    L..            ; Write character

; ***************************************************************************************
; Print byte as two hex digits
; 
; Prints the high nibble first (via 4× LSR), then the low
; nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
; and output via OSASCI.
; ***************************************************************************************
; &8d9d referenced 2 times by &8c6f, &8d35
.print_hex
    pha                                                               ; 8d9d: 48          H
    lsr a                                                             ; 8d9e: 4a          J
    lsr a                                                             ; 8d9f: 4a          J
    lsr a                                                             ; 8da0: 4a          J
    lsr a                                                             ; 8da1: 4a          J
    jsr print_hex_nibble                                              ; 8da2: 20 a8 8d     ..
    pla                                                               ; 8da5: 68          h
    and #&0f                                                          ; 8da6: 29 0f       ).
; &8da8 referenced 1 time by &8da2
.print_hex_nibble
    ora #&30 ; '0'                                                    ; 8da8: 09 30       .0
    cmp #&3a ; ':'                                                    ; 8daa: c9 3a       .:
    bcc c8db0                                                         ; 8dac: 90 02       ..
    adc #6                                                            ; 8dae: 69 06       i.
; &8db0 referenced 2 times by &8d3e, &8dac
.c8db0
    bne loop_c8d9a                                                    ; 8db0: d0 e8       ..
; &8db2 referenced 3 times by &8c22, &8c91, &8ca3
.sub_c8db2
    ldy #&0a                                                          ; 8db2: a0 0a       ..
; &8db4 referenced 2 times by &8c5a, &8dbc
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8db4: bd 05 0f    ...
    jsr osasci                                                        ; 8db7: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8dba: e8          .
    dey                                                               ; 8dbb: 88          .
    bne print_reply_counted                                           ; 8dbc: d0 f6       ..
    rts                                                               ; 8dbe: 60          `

.sub_c8dbf
    jsr parse_filename_gs                                             ; 8dbf: 20 ba 86     ..
; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears rom_svc_num on exit.
; ***************************************************************************************
.net2_read_handle_entry
    jsr sub_c8d43                                                     ; 8dc2: 20 43 8d     C.
; ***************************************************************************************
; Send FS load-as-command and execute response
; 
; Sets up an FS command with function code &05 (FCCMND: load as
; command) using send_fs_examine. If a Tube co-processor is
; present (tx_in_progress != 0), transfers the response data
; to the Tube via tube_addr_claim. Otherwise jumps via the
; indirect pointer at (&0F09) to execute at the load address.
; ***************************************************************************************
.notify_and_exec
    ldx #&0e                                                          ; 8dc5: a2 0e       ..
    stx fs_block_offset                                               ; 8dc7: 86 bc       ..
    lda #&10                                                          ; 8dc9: a9 10       ..
    sta fs_options                                                    ; 8dcb: 85 bb       ..
    sta l0e16                                                         ; 8dcd: 8d 16 0e    ...
    ldx #&4a ; 'J'                                                    ; 8dd0: a2 4a       .J
    ldy #5                                                            ; 8dd2: a0 05       ..
    jsr send_fs_examine                                               ; 8dd4: 20 f4 86     ..
    ldy #0                                                            ; 8dd7: a0 00       ..
    clc                                                               ; 8dd9: 18          .
    jsr gsinit                                                        ; 8dda: 20 c2 ff     ..
; &8ddd referenced 1 time by &8de0
.loop_c8ddd
    jsr gsread                                                        ; 8ddd: 20 c5 ff     ..
; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.
; ***************************************************************************************
.net3_close_handle
    bcc loop_c8ddd                                                    ; 8de0: 90 fb       ..
    dey                                                               ; 8de2: 88          .
; &8de3 referenced 1 time by &8de8
.loop_c8de3
    iny                                                               ; 8de3: c8          .
    lda (os_text_ptr),y                                               ; 8de4: b1 f2       ..
    cmp #&20 ; ' '                                                    ; 8de6: c9 20       .
    beq loop_c8de3                                                    ; 8de8: f0 f9       ..
    clc                                                               ; 8dea: 18          .
; ***************************************************************************************
; *NET4: resume after remote operation
; 
; Calls resume_after_remote (&8180) to re-enable the keyboard
; and send a completion notification. The BVC always branches
; to c8dda (clear rom_svc_num) since resume_after_remote
; returns with V clear (from CLV in prepare_cmd_clv).
; ***************************************************************************************
.net4_resume_remote
    tya                                                               ; 8deb: 98          .
    adc os_text_ptr                                                   ; 8dec: 65 f2       e.
    sta fs_cmd_context                                                ; 8dee: 8d 0a 0e    ...
    lda l00f3                                                         ; 8df1: a5 f3       ..
    adc #0                                                            ; 8df3: 69 00       i.
    sta l0e0b                                                         ; 8df5: 8d 0b 0e    ...
    sec                                                               ; 8df8: 38          8
    lda tx_in_progress                                                ; 8df9: ad 52 0d    .R.
    beq c8e12                                                         ; 8dfc: f0 14       ..
    adc l0f0b                                                         ; 8dfe: 6d 0b 0f    m..
    adc l0f0c                                                         ; 8e01: 6d 0c 0f    m..
    bcs c8e12                                                         ; 8e04: b0 0c       ..
    jsr tube_claim_loop                                               ; 8e06: 20 ae 8b     ..
    ldx #9                                                            ; 8e09: a2 09       ..
    ldy #&0f                                                          ; 8e0b: a0 0f       ..
    lda #4                                                            ; 8e0d: a9 04       ..
    jmp tube_addr_claim                                               ; 8e0f: 4c 06 04    L..

; &8e12 referenced 2 times by &8dfc, &8e04
.c8e12
    jmp (l0f09)                                                       ; 8e12: 6c 09 0f    l..

.sub_c8e15
    sty fs_lib_handle                                                 ; 8e15: 8c 04 0e    ...
    bne c8e1d                                                         ; 8e18: d0 03       ..
.sub_c8e1a
    sty fs_csd_handle                                                 ; 8e1a: 8c 03 0e    ...
; &8e1d referenced 2 times by &8e18, &8e2e
.c8e1d
    jmp restore_args_return                                           ; 8e1d: 4c 52 89    LR.

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
.copy_handles_and_boot
    sec                                                               ; 8e20: 38          8
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to c8cff.
; Called when the FS reply contains updated handle values
; but no boot action is needed.
; ***************************************************************************************
.copy_handles
    ldx #3                                                            ; 8e21: a2 03       ..
    bcc c8e2b                                                         ; 8e23: 90 06       ..
; &8e25 referenced 1 time by &8e2c
.logon2
    lda fs_cmd_data,x                                                 ; 8e25: bd 05 0f    ...
    sta fs_urd_handle,x                                               ; 8e28: 9d 02 0e    ...
; &8e2b referenced 1 time by &8e23
.c8e2b
    dex                                                               ; 8e2b: ca          .
    bpl logon2                                                        ; 8e2c: 10 f7       ..
    bcc c8e1d                                                         ; 8e2e: 90 ed       ..
    ldy fs_boot_option                                                ; 8e30: ac 05 0e    ...
    ldx l8cf4,y                                                       ; 8e33: be f4 8c    ...
    ldy #&8c                                                          ; 8e36: a0 8c       ..
    jmp oscli                                                         ; 8e38: 4c f7 ff    L..

; ***************************************************************************************
; *NET1: read file handle from received packet
; 
; Reads a file handle byte from offset &6F in the RX buffer
; (net_rx_ptr), stores it in &F0, then falls through to the
; common handle workspace cleanup at c8dda (clear rom_svc_num).
; ***************************************************************************************
.net1_read_handle
    ldy #&6f ; 'o'                                                    ; 8e3b: a0 6f       .o
    lda (net_rx_ptr),y                                                ; 8e3d: b1 9c       ..
    sta l00f0                                                         ; 8e3f: 85 f0       ..
    rts                                                               ; 8e41: 60          `

; &8e42 referenced 2 times by &8e56, &8e66
.sub_c8e42
    lda l00f0                                                         ; 8e42: a5 f0       ..
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
; &8e44 referenced 3 times by &82ef, &8f77, &8f90
.calc_handle_offset
    asl a                                                             ; 8e44: 0a          .
    asl a                                                             ; 8e45: 0a          .
    pha                                                               ; 8e46: 48          H
    asl a                                                             ; 8e47: 0a          .
    tsx                                                               ; 8e48: ba          .
    adc l0101,x                                                       ; 8e49: 7d 01 01    }..
    tay                                                               ; 8e4c: a8          .
    pla                                                               ; 8e4d: 68          h
    cmp #&48 ; 'H'                                                    ; 8e4e: c9 48       .H
    bcc return_6                                                      ; 8e50: 90 03       ..
    ldy #0                                                            ; 8e52: a0 00       ..
    tya                                                               ; 8e54: 98          .              ; A=&00
; &8e55 referenced 1 time by &8e50
.return_6
.return_calc_handle
    rts                                                               ; 8e55: 60          `

.sub_c8e56
    jsr sub_c8e42                                                     ; 8e56: 20 42 8e     B.
    bcs rxpol2                                                        ; 8e59: b0 06       ..
    lda (nfs_workspace),y                                             ; 8e5b: b1 9e       ..
    cmp #&3f ; '?'                                                    ; 8e5d: c9 3f       .?
    bne c8e63                                                         ; 8e5f: d0 02       ..
; &8e61 referenced 2 times by &8e59, &8e69
.rxpol2
    lda #0                                                            ; 8e61: a9 00       ..
; &8e63 referenced 1 time by &8e5f
.c8e63
    sta l00f0                                                         ; 8e63: 85 f0       ..
    rts                                                               ; 8e65: 60          `

.sub_c8e66
    jsr sub_c8e42                                                     ; 8e66: 20 42 8e     B.
    bcs rxpol2                                                        ; 8e69: b0 f6       ..
    rol rx_flags                                                      ; 8e6b: 2e 64 0d    .d.
    lda #&3f ; '?'                                                    ; 8e6e: a9 3f       .?
    sta (nfs_workspace),y                                             ; 8e70: 91 9e       ..
    ror rx_flags                                                      ; 8e72: 6e 64 0d    nd.
    rts                                                               ; 8e75: 60          `

; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at &8E80.
; ***************************************************************************************
.osword_fs_entry
    lda l00ef                                                         ; 8e76: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8e78: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_7                                                      ; 8e7a: 30 3b       0;
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
.osword_12_handler
    cmp #5                                                            ; 8e7c: c9 05       ..
    bcs return_7                                                      ; 8e7e: b0 37       .7
; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
; at &8E9F (low) / &8EA4 (high).
; ***************************************************************************************
.fs_osword_dispatch
    tax                                                               ; 8e80: aa          .
    lda #&8f                                                          ; 8e81: a9 8f       ..
    pha                                                               ; 8e83: 48          H
    lda #&be                                                          ; 8e84: a9 be       ..
    pha                                                               ; 8e86: 48          H
    lda fs_osword_tbl_hi,x                                            ; 8e87: bd a4 8e    ...
    pha                                                               ; 8e8a: 48          H
    lda fs_osword_tbl_lo,x                                            ; 8e8b: bd 9f 8e    ...
    pha                                                               ; 8e8e: 48          H
    ldy #2                                                            ; 8e8f: a0 02       ..
; &8e91 referenced 1 time by &8e97
.save1
    lda fs_last_byte_flag,y                                           ; 8e91: b9 bd 00    ...
    sta (net_rx_ptr),y                                                ; 8e94: 91 9c       ..
    dey                                                               ; 8e96: 88          .
    bpl save1                                                         ; 8e97: 10 f8       ..
    iny                                                               ; 8e99: c8          .
    lda (l00f0),y                                                     ; 8e9a: b1 f0       ..
    sty rom_svc_num                                                   ; 8e9c: 84 ce       ..
    rts                                                               ; 8e9e: 60          `

; &8e9f referenced 1 time by &8e8b
.fs_osword_tbl_lo
    equb <(osword_0f_handler-1)                                       ; 8e9f: b7          .              ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
    equb <(osword_10_handler-1)                                       ; 8ea0: 65          e
    equb <(osword_11_handler-1)                                       ; 8ea1: d1          .
    equb <(sub_c8ef7-1)                                               ; 8ea2: f6          .
    equb <(econet_tx_rx-1)                                            ; 8ea3: e4          .
; &8ea4 referenced 1 time by &8e87
.fs_osword_tbl_hi
    equb >(osword_0f_handler-1)                                       ; 8ea4: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb >(osword_10_handler-1)                                       ; 8ea5: 8f          .
    equb >(osword_11_handler-1)                                       ; 8ea6: 8e          .
    equb >(sub_c8ef7-1)                                               ; 8ea7: 8e          .
    equb >(econet_tx_rx-1)                                            ; 8ea8: 8f          .

; &8ea9 referenced 5 times by &8eb5, &8ecc, &8ee1, &8f12, &8fa7
.c8ea9
    bcc c8eaf                                                         ; 8ea9: 90 04       ..
    lda (l00f0),y                                                     ; 8eab: b1 f0       ..
    sta (fs_crc_lo),y                                                 ; 8ead: 91 be       ..
; &8eaf referenced 1 time by &8ea9
.c8eaf
    lda (fs_crc_lo),y                                                 ; 8eaf: b1 be       ..
; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
.copy_param_block
    sta (l00f0),y                                                     ; 8eb1: 91 f0       ..
.copyl3
    iny                                                               ; 8eb3: c8          .
    dex                                                               ; 8eb4: ca          .
    bpl c8ea9                                                         ; 8eb5: 10 f2       ..
; &8eb7 referenced 2 times by &8e7a, &8e7e
.return_7
.logon3
.return_copy_param
    rts                                                               ; 8eb7: 60          `

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
    asl tx_clear_flag                                                 ; 8eb8: 0e 62 0d    .b.
    tya                                                               ; 8ebb: 98          .
    bcc readry                                                        ; 8ebc: 90 34       .4
    lda net_rx_ptr_hi                                                 ; 8ebe: a5 9d       ..
    sta fs_crc_hi                                                     ; 8ec0: 85 bf       ..
    sta nmi_tx_block_hi                                               ; 8ec2: 85 a1       ..
    lda #&6f ; 'o'                                                    ; 8ec4: a9 6f       .o
    sta fs_crc_lo                                                     ; 8ec6: 85 be       ..
    sta nmi_tx_block                                                  ; 8ec8: 85 a0       ..
    ldx #&0f                                                          ; 8eca: a2 0f       ..
    jsr c8ea9                                                         ; 8ecc: 20 a9 8e     ..
    jmp trampoline_tx_setup                                           ; 8ecf: 4c 60 96    L`.

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
    lda net_rx_ptr_hi                                                 ; 8ed2: a5 9d       ..
    sta fs_crc_hi                                                     ; 8ed4: 85 bf       ..
    ldy #&7f                                                          ; 8ed6: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8ed8: b1 9c       ..
    iny                                                               ; 8eda: c8          .              ; Y=&80
    sty fs_crc_lo                                                     ; 8edb: 84 be       ..
    tax                                                               ; 8edd: aa          .
    dex                                                               ; 8ede: ca          .
    ldy #0                                                            ; 8edf: a0 00       ..
    jsr c8ea9                                                         ; 8ee1: 20 a9 8e     ..
    jmp clear_jsr_protection                                          ; 8ee4: 4c e4 92    L..

; &8ee7 referenced 1 time by &8f36
.read_args_size
    ldy #&7f                                                          ; 8ee7: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8ee9: b1 9c       ..
    ldy #1                                                            ; 8eeb: a0 01       ..
    sta (l00f0),y                                                     ; 8eed: 91 f0       ..
    iny                                                               ; 8eef: c8          .              ; Y=&02
    lda #&80                                                          ; 8ef0: a9 80       ..
; &8ef2 referenced 1 time by &8ebc
.readry
    sta (l00f0),y                                                     ; 8ef2: 91 f0       ..
    rts                                                               ; 8ef4: 60          `

; &8ef5 referenced 1 time by &8f09
.l8ef5
    equb &ff, 1                                                       ; 8ef5: ff 01       ..

.sub_c8ef7
    cmp #6                                                            ; 8ef7: c9 06       ..
    bcs rsl1                                                          ; 8ef9: b0 35       .5
    cmp #4                                                            ; 8efb: c9 04       ..
    bcs rssl1                                                         ; 8efd: b0 16       ..
    lsr a                                                             ; 8eff: 4a          J
    ldx #&0d                                                          ; 8f00: a2 0d       ..
    tay                                                               ; 8f02: a8          .
    beq c8f07                                                         ; 8f03: f0 02       ..
    ldx nfs_workspace_hi                                              ; 8f05: a6 9f       ..
; &8f07 referenced 1 time by &8f03
.c8f07
    stx fs_crc_hi                                                     ; 8f07: 86 bf       ..
    lda l8ef5,y                                                       ; 8f09: b9 f5 8e    ...
    sta fs_crc_lo                                                     ; 8f0c: 85 be       ..
    ldx #1                                                            ; 8f0e: a2 01       ..
    ldy #1                                                            ; 8f10: a0 01       ..
    jmp c8ea9                                                         ; 8f12: 4c a9 8e    L..

; &8f15 referenced 1 time by &8efd
.rssl1
    lsr a                                                             ; 8f15: 4a          J
    iny                                                               ; 8f16: c8          .
    lda (l00f0),y                                                     ; 8f17: b1 f0       ..
    bcs rssl2                                                         ; 8f19: b0 05       ..
    lda prot_status                                                   ; 8f1b: ad 63 0d    .c.
    sta (l00f0),y                                                     ; 8f1e: 91 f0       ..
; &8f20 referenced 1 time by &8f19
.rssl2
    sta prot_status                                                   ; 8f20: 8d 63 0d    .c.
    sta saved_jsr_mask                                                ; 8f23: 8d 65 0d    .e.
    rts                                                               ; 8f26: 60          `

; &8f27 referenced 1 time by &8f32
.loop_c8f27
    ldy #&14                                                          ; 8f27: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8f29: b1 9c       ..
    ldy #1                                                            ; 8f2b: a0 01       ..
    sta (l00f0),y                                                     ; 8f2d: 91 f0       ..
    rts                                                               ; 8f2f: 60          `

; &8f30 referenced 1 time by &8ef9
.rsl1
    cmp #8                                                            ; 8f30: c9 08       ..
    beq loop_c8f27                                                    ; 8f32: f0 f3       ..
    cmp #9                                                            ; 8f34: c9 09       ..
    beq read_args_size                                                ; 8f36: f0 af       ..
    bpl c8f53                                                         ; 8f38: 10 19       ..
    ldy #3                                                            ; 8f3a: a0 03       ..
    lsr a                                                             ; 8f3c: 4a          J
    bcc readc1                                                        ; 8f3d: 90 1b       ..
    sty nfs_temp                                                      ; 8f3f: 84 cd       ..
; &8f41 referenced 1 time by &8f50
.loop_c8f41
    ldy nfs_temp                                                      ; 8f41: a4 cd       ..
    lda (l00f0),y                                                     ; 8f43: b1 f0       ..
    jsr handle_to_mask_a                                              ; 8f45: 20 1b 86     ..
    tya                                                               ; 8f48: 98          .
    ldy nfs_temp                                                      ; 8f49: a4 cd       ..
    sta fs_server_net,y                                               ; 8f4b: 99 01 0e    ...
    dec nfs_temp                                                      ; 8f4e: c6 cd       ..
    bne loop_c8f41                                                    ; 8f50: d0 ef       ..
    rts                                                               ; 8f52: 60          `

; &8f53 referenced 1 time by &8f38
.c8f53
    iny                                                               ; 8f53: c8          .
    lda fs_last_error                                                 ; 8f54: ad 09 0e    ...
    sta (l00f0),y                                                     ; 8f57: 91 f0       ..
    rts                                                               ; 8f59: 60          `

; &8f5a referenced 2 times by &8f3d, &8f63
.readc1
    lda fs_server_net,y                                               ; 8f5a: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8f5d: 20 38 86     8.            ; Convert bitmask to handle number (FS2A)
    sta (l00f0),y                                                     ; 8f60: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8f62: 88          .
    bne readc1                                                        ; 8f63: d0 f5       ..
    rts                                                               ; 8f65: 60          `

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
    ldx nfs_workspace_hi                                              ; 8f66: a6 9f       ..
    stx fs_crc_hi                                                     ; 8f68: 86 bf       ..
    sty fs_crc_lo                                                     ; 8f6a: 84 be       ..
    ror rx_flags                                                      ; 8f6c: 6e 64 0d    nd.
    lda (l00f0),y                                                     ; 8f6f: b1 f0       ..
    sta fs_last_byte_flag                                             ; 8f71: 85 bd       ..             ; Load from ROM template (zero = use NMI workspace value)
    bne c8f90                                                         ; 8f73: d0 1b       ..
    lda #3                                                            ; 8f75: a9 03       ..
; &8f77 referenced 1 time by &8f89
.scan0
    jsr calc_handle_offset                                            ; 8f77: 20 44 8e     D.
    bcs openl4                                                        ; 8f7a: b0 3d       .=
    lsr a                                                             ; 8f7c: 4a          J
    lsr a                                                             ; 8f7d: 4a          J
    tax                                                               ; 8f7e: aa          .
    lda (fs_crc_lo),y                                                 ; 8f7f: b1 be       ..
    beq openl4                                                        ; 8f81: f0 36       .6
    cmp #&3f ; '?'                                                    ; 8f83: c9 3f       .?
    beq scan1                                                         ; 8f85: f0 04       ..
    inx                                                               ; 8f87: e8          .
    txa                                                               ; 8f88: 8a          .
    bne scan0                                                         ; 8f89: d0 ec       ..
; &8f8b referenced 1 time by &8f85
.scan1
    txa                                                               ; 8f8b: 8a          .
    ldx #0                                                            ; 8f8c: a2 00       ..
    sta (l00f0,x)                                                     ; 8f8e: 81 f0       ..
; &8f90 referenced 1 time by &8f73
.c8f90
    jsr calc_handle_offset                                            ; 8f90: 20 44 8e     D.
    bcs openl4                                                        ; 8f93: b0 24       .$
    dey                                                               ; 8f95: 88          .
    sty fs_crc_lo                                                     ; 8f96: 84 be       ..
    lda #&c0                                                          ; 8f98: a9 c0       ..
    ldy #1                                                            ; 8f9a: a0 01       ..
    ldx #&0b                                                          ; 8f9c: a2 0b       ..             ; Enable interrupts before transmit
    cpy fs_last_byte_flag                                             ; 8f9e: c4 bd       ..
    adc (fs_crc_lo),y                                                 ; 8fa0: 71 be       q.
    beq openl6                                                        ; 8fa2: f0 03       ..             ; Dest station = &FFFF (accept reply from any station)
    bmi openl7                                                        ; 8fa4: 30 0e       0.
; &8fa6 referenced 1 time by &8fb6
.loop_c8fa6
    clc                                                               ; 8fa6: 18          .
; &8fa7 referenced 1 time by &8fa2
.openl6
    jsr c8ea9                                                         ; 8fa7: 20 a9 8e     ..
    bcs c8fbb                                                         ; 8faa: b0 0f       ..
    lda #&3f ; '?'                                                    ; 8fac: a9 3f       .?
    ldy #1                                                            ; 8fae: a0 01       ..
    sta (fs_crc_lo),y                                                 ; 8fb0: 91 be       ..
    bne c8fbb                                                         ; 8fb2: d0 07       ..             ; ALWAYS branch

; &8fb4 referenced 1 time by &8fa4
.openl7
    adc #1                                                            ; 8fb4: 69 01       i.             ; Initiate receive with timeout
    bne loop_c8fa6                                                    ; 8fb6: d0 ee       ..
    dey                                                               ; 8fb8: 88          .
; &8fb9 referenced 3 times by &8f7a, &8f81, &8f93
.openl4
    sta (l00f0),y                                                     ; 8fb9: 91 f0       ..
; &8fbb referenced 2 times by &8faa, &8fb2
.c8fbb
    rol rx_flags                                                      ; 8fbb: 2e 64 0d    .d.
    rts                                                               ; 8fbe: 60          `

    equb &a0, 2                                                       ; 8fbf: a0 02       ..
.rest1
    equb &b1, &9c, &99, &bd, 0, &88, &10, &f8, &60                    ; 8fc1: b1 9c 99... ...

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &28. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &2C.
; ***************************************************************************************
; &8fca referenced 1 time by &8ffd
.setup_rx_buffer_ptrs
    ldy #&1c                                                          ; 8fca: a0 1c       ..
    lda l00f0                                                         ; 8fcc: a5 f0       ..
    adc #1                                                            ; 8fce: 69 01       i.
    jsr store_16bit_at_y                                              ; 8fd0: 20 db 8f     ..            ; Receive data blocks until command byte = &00 or &0D
    ldy #1                                                            ; 8fd3: a0 01       ..
    lda (l00f0),y                                                     ; 8fd5: b1 f0       ..
    ldy #&20 ; ' '                                                    ; 8fd7: a0 20       .
    adc l00f0                                                         ; 8fd9: 65 f0       e.
; &8fdb referenced 1 time by &8fd0
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8fdb: 91 9e       ..
    iny                                                               ; 8fdd: c8          .
    lda l00f1                                                         ; 8fde: a5 f1       ..
    adc #0                                                            ; 8fe0: 69 00       i.
    sta (nfs_workspace),y                                             ; 8fe2: 91 9e       ..
    rts                                                               ; 8fe4: 60          `

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &834A
;      (zero entries substituted from NMI workspace &0DDA), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &8F49).
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8fe5: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs c9031                                                         ; 8fe7: b0 48       .H
    ldy #&23 ; '#'                                                    ; 8fe9: a0 23       .#
; &8feb referenced 1 time by &8ff8
.dofs01
    lda init_tx_ctrl_block,y                                          ; 8feb: b9 56 83    .V.
    bne c8ff3                                                         ; 8fee: d0 03       ..
    lda l0de6,y                                                       ; 8ff0: b9 e6 0d    ...
; &8ff3 referenced 1 time by &8fee
.c8ff3
    sta (nfs_workspace),y                                             ; 8ff3: 91 9e       ..
    dey                                                               ; 8ff5: 88          .
    cpy #&17                                                          ; 8ff6: c0 17       ..
    bne dofs01                                                        ; 8ff8: d0 f1       ..
    iny                                                               ; 8ffa: c8          .
    sty net_tx_ptr                                                    ; 8ffb: 84 9a       ..
    jsr setup_rx_buffer_ptrs                                          ; 8ffd: 20 ca 8f     ..
    ldy #2                                                            ; 9000: a0 02       ..
    lda #&90                                                          ; 9002: a9 90       ..
    sta (l00f0),y                                                     ; 9004: 91 f0       ..
    iny                                                               ; 9006: c8          .              ; Y=&03
    iny                                                               ; 9007: c8          .              ; Retrieve original A (function code) from stack; Y=&04
; &9008 referenced 1 time by &9010
.loop_c9008
    lda l0dfe,y                                                       ; 9008: b9 fe 0d    ...
    sta (l00f0),y                                                     ; 900b: 91 f0       ..
    iny                                                               ; 900d: c8          .
    cpy #7                                                            ; 900e: c0 07       ..
    bne loop_c9008                                                    ; 9010: d0 f6       ..
    lda nfs_workspace_hi                                              ; 9012: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; 9014: 85 9b       ..
    cli                                                               ; 9016: 58          X
    jsr tx_poll_ff                                                    ; 9017: 20 68 86     h.
    ldy #&20 ; ' '                                                    ; 901a: a0 20       .
    lda #&ff                                                          ; 901c: a9 ff       ..
    sta (nfs_workspace),y                                             ; 901e: 91 9e       ..
    iny                                                               ; 9020: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; 9021: 91 9e       ..
    ldy #&19                                                          ; 9023: a0 19       ..
    lda #&90                                                          ; 9025: a9 90       ..
    sta (nfs_workspace),y                                             ; 9027: 91 9e       ..
    dey                                                               ; 9029: 88          .              ; Y=&18
    lda #&7f                                                          ; 902a: a9 7f       ..
    sta (nfs_workspace),y                                             ; 902c: 91 9e       ..
    jmp send_to_fs_star                                               ; 902e: 4c eb 84    L..

; &9031 referenced 1 time by &8fe7
.c9031
    php                                                               ; 9031: 08          .
    ldy #1                                                            ; 9032: a0 01       ..             ; Y=character to write
    lda (l00f0),y                                                     ; 9034: b1 f0       ..
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
    tax                                                               ; 9036: aa          .
    iny                                                               ; 9037: c8          .              ; ROR/ASL on stacked P: zeros carry to signal success
    lda (l00f0),y                                                     ; 9038: b1 f0       ..
    iny                                                               ; 903a: c8          .
    sty fs_crc_lo                                                     ; 903b: 84 be       ..
    ldy #&72 ; 'r'                                                    ; 903d: a0 72       .r
    sta (net_rx_ptr),y                                                ; 903f: 91 9c       ..
    dey                                                               ; 9041: 88          .              ; Y=&71
    txa                                                               ; 9042: 8a          .
    sta (net_rx_ptr),y                                                ; 9043: 91 9c       ..
    plp                                                               ; 9045: 28          (
    bne dofs2                                                         ; 9046: d0 1d       ..
; &9048 referenced 1 time by &9062
.loop_c9048
    ldy fs_crc_lo                                                     ; 9048: a4 be       ..
    inc fs_crc_lo                                                     ; 904a: e6 be       ..
    lda (l00f0),y                                                     ; 904c: b1 f0       ..
    ldy #&7d ; '}'                                                    ; 904e: a0 7d       .}
    sta (net_rx_ptr),y                                                ; 9050: 91 9c       ..
    pha                                                               ; 9052: 48          H
    jsr ctrl_block_setup_alt                                          ; 9053: 20 68 91     h.
    cli                                                               ; 9056: 58          X
    jsr tx_poll_core                                                  ; 9057: 20 6c 86     l.            ; Core transmit and poll routine (XMIT)
; &905a referenced 1 time by &905b
.loop_c905a
    dex                                                               ; 905a: ca          .
    bne loop_c905a                                                    ; 905b: d0 fd       ..
    pla                                                               ; 905d: 68          h
    beq return_8                                                      ; 905e: f0 04       ..
    eor #&0d                                                          ; 9060: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne loop_c9048                                                    ; 9062: d0 e4       ..
; &9064 referenced 1 time by &905e
.return_8
    rts                                                               ; 9064: 60          `

; &9065 referenced 1 time by &9046
.dofs2
    jsr ctrl_block_setup_alt                                          ; 9065: 20 68 91     h.
    ldy #&7b ; '{'                                                    ; 9068: a0 7b       .{
    lda (net_rx_ptr),y                                                ; 906a: b1 9c       ..
    adc #3                                                            ; 906c: 69 03       i.
    sta (net_rx_ptr),y                                                ; 906e: 91 9c       ..
    cli                                                               ; 9070: 58          X
    jmp tx_poll_ff                                                    ; 9071: 4c 68 86    Lh.

; ***************************************************************************************
; NETVEC dispatch handler (ENTRY)
; 
; Indirected from NETVEC at &0224. Saves all registers and flags,
; retrieves the reason code from the stacked A, and dispatches to
; one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
; &908D. Reason codes >= 9 are ignored.
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
    php                                                               ; 9074: 08          .
    pha                                                               ; 9075: 48          H
    txa                                                               ; 9076: 8a          .
    pha                                                               ; 9077: 48          H
    tya                                                               ; 9078: 98          .
    pha                                                               ; 9079: 48          H
    tsx                                                               ; 907a: ba          .
    lda l0103,x                                                       ; 907b: bd 03 01    ...
    cmp #9                                                            ; 907e: c9 09       ..
    bcs entry1                                                        ; 9080: b0 04       ..
    tax                                                               ; 9082: aa          .
    jsr osword_trampoline                                             ; 9083: 20 8d 90     ..
; &9086 referenced 1 time by &9080
.entry1
    pla                                                               ; 9086: 68          h
    tay                                                               ; 9087: a8          .
    pla                                                               ; 9088: 68          h
    tax                                                               ; 9089: aa          .
    pla                                                               ; 908a: 68          h
    plp                                                               ; 908b: 28          (
    rts                                                               ; 908c: 60          `

; &908d referenced 1 time by &9083
.osword_trampoline
    lda osword_tbl_hi,x                                               ; 908d: bd a1 90    ...            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9090: 48          H
    lda osword_tbl_lo,x                                               ; 9091: bd 98 90    ...
    pha                                                               ; 9094: 48          H
    lda l00ef                                                         ; 9095: a5 ef       ..
    rts                                                               ; 9097: 60          `

; &9098 referenced 1 time by &9091
.osword_tbl_lo
    equb <(return_2-1)                                                ; 9098: 6b          k
    equb <(remote_print_handler-1)                                    ; 9099: d3          .
    equb <(remote_print_handler-1)                                    ; 909a: d3          .
    equb <(remote_print_handler-1)                                    ; 909b: d3          .
    equb <(sub_c90aa-1)                                               ; 909c: a9          .
    equb <(remote_display_setup-1)                                    ; 909d: c3          .
    equb <(return_2-1)                                                ; 909e: 6b          k
    equb <(remote_cmd_dispatch-1)                                     ; 909f: cf          .
    equb <(sub_c913a-1)                                               ; 90a0: 39          9
; &90a1 referenced 1 time by &908d
.osword_tbl_hi
    equb >(return_2-1)                                                ; 90a1: 81          .
    equb >(remote_print_handler-1)                                    ; 90a2: 91          .
    equb >(remote_print_handler-1)                                    ; 90a3: 91          .
    equb >(remote_print_handler-1)                                    ; 90a4: 91          .
    equb >(sub_c90aa-1)                                               ; 90a5: 90          .
    equb >(remote_display_setup-1)                                    ; 90a6: 91          .
    equb >(return_2-1)                                                ; 90a7: 81          .
    equb >(remote_cmd_dispatch-1)                                     ; 90a8: 90          .
    equb >(sub_c913a-1)                                               ; 90a9: 91          .

.sub_c90aa
    tsx                                                               ; 90aa: ba          .
    ror l0106,x                                                       ; 90ab: 7e 06 01    ~..
    asl l0106,x                                                       ; 90ae: 1e 06 01    ...
    tya                                                               ; 90b1: 98          .
    ldy #&da                                                          ; 90b2: a0 da       ..
    sta (nfs_workspace),y                                             ; 90b4: 91 9e       ..
    lda #0                                                            ; 90b6: a9 00       ..
; ***************************************************************************************
; Set up TX control block and send
; 
; Builds a TX control block at (nfs_workspace)+&0C from the current
; workspace state, then initiates transmission via the ADLC TX path.
; This is the common send routine used after command data has been
; prepared. The exact control block layout and field mapping need
; further analysis.
; ***************************************************************************************
; &90b8 referenced 3 times by &8193, &90ff, &9160
.setup_tx_and_send
    ldy #&d9                                                          ; 90b8: a0 d9       ..
    sta (nfs_workspace),y                                             ; 90ba: 91 9e       ..
    lda #&80                                                          ; 90bc: a9 80       ..
    ldy #&0c                                                          ; 90be: a0 0c       ..
    sta (nfs_workspace),y                                             ; 90c0: 91 9e       ..
    sty net_tx_ptr                                                    ; 90c2: 84 9a       ..
    ldx nfs_workspace_hi                                              ; 90c4: a6 9f       ..
    stx net_tx_ptr_hi                                                 ; 90c6: 86 9b       ..
    jsr tx_poll_ff                                                    ; 90c8: 20 68 86     h.
    lda #&3f ; '?'                                                    ; 90cb: a9 3f       .?
    sta (net_tx_ptr,x)                                                ; 90cd: 81 9a       ..
    rts                                                               ; 90cf: 60          `

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
    ldy l00f1                                                         ; 90d0: a4 f1       ..
    cmp #&81                                                          ; 90d2: c9 81       ..
    beq c90e9                                                         ; 90d4: f0 13       ..
    ldy #1                                                            ; 90d6: a0 01       ..
    ldx #7                                                            ; 90d8: a2 07       ..
    jsr match_osbyte_code                                             ; 90da: 20 22 91     ".
    beq c90e9                                                         ; 90dd: f0 0a       ..
    dey                                                               ; 90df: 88          .
    dey                                                               ; 90e0: 88          .
    ldx #&0e                                                          ; 90e1: a2 0e       ..
    jsr match_osbyte_code                                             ; 90e3: 20 22 91     ".
    beq c90e9                                                         ; 90e6: f0 01       ..
    iny                                                               ; 90e8: c8          .
; &90e9 referenced 3 times by &90d4, &90dd, &90e6
.c90e9
    ldx #2                                                            ; 90e9: a2 02       ..
    tya                                                               ; 90eb: 98          .
    beq return_nbyte                                                  ; 90ec: f0 33       .3
    php                                                               ; 90ee: 08          .
    bpl nbyte6                                                        ; 90ef: 10 01       ..
    inx                                                               ; 90f1: e8          .              ; X=&03
; &90f2 referenced 1 time by &90ef
.nbyte6
    ldy #&dc                                                          ; 90f2: a0 dc       ..
; &90f4 referenced 1 time by &90fc
.nbyte1
    lda l0015,y                                                       ; 90f4: b9 15 00    ...
    sta (nfs_workspace),y                                             ; 90f7: 91 9e       ..
    dey                                                               ; 90f9: 88          .
    cpy #&da                                                          ; 90fa: c0 da       ..
    bpl nbyte1                                                        ; 90fc: 10 f6       ..
    txa                                                               ; 90fe: 8a          .
    jsr setup_tx_and_send                                             ; 90ff: 20 b8 90     ..
    plp                                                               ; 9102: 28          (
    bpl return_nbyte                                                  ; 9103: 10 1c       ..
    lda #&7f                                                          ; 9105: a9 7f       ..
    sta (net_tx_ptr,x)                                                ; 9107: 81 9a       ..
; &9109 referenced 1 time by &910b
.loop_c9109
    lda (net_tx_ptr,x)                                                ; 9109: a1 9a       ..
    bpl loop_c9109                                                    ; 910b: 10 fc       ..
    tsx                                                               ; 910d: ba          .
    ldy #&dd                                                          ; 910e: a0 dd       ..
    lda (nfs_workspace),y                                             ; 9110: b1 9e       ..
    ora #&44 ; 'D'                                                    ; 9112: 09 44       .D
    bne nbyte5                                                        ; 9114: d0 04       ..             ; ALWAYS branch

; &9116 referenced 1 time by &911f
.nbyte4
    dey                                                               ; 9116: 88          .
    dex                                                               ; 9117: ca          .
    lda (nfs_workspace),y                                             ; 9118: b1 9e       ..
; &911a referenced 1 time by &9114
.nbyte5
    sta l0106,x                                                       ; 911a: 9d 06 01    ...
    cpy #&da                                                          ; 911d: c0 da       ..
    bne nbyte4                                                        ; 911f: d0 f5       ..
; &9121 referenced 2 times by &90ec, &9103
.return_nbyte
    rts                                                               ; 9121: 60          `

; &9122 referenced 3 times by &90da, &90e3, &9128
.match_osbyte_code
    cmp l912b,x                                                       ; 9122: dd 2b 91    .+.
    beq return_match_osbyte                                           ; 9125: f0 03       ..
    dex                                                               ; 9127: ca          .
    bpl match_osbyte_code                                             ; 9128: 10 f8       ..
; &912a referenced 2 times by &9125, &9142
.return_match_osbyte
    rts                                                               ; 912a: 60          `

; &912b referenced 1 time by &9122
.l912b
    equb   4,   9, &0a, &14, &9a, &9b, &9c, &e2, &0b, &0c, &0f, &79   ; 912b: 04 09 0a... ...
    equb &7a, &e3, &e4                                                ; 9137: 7a e3 e4    z..

.sub_c913a
    ldy #&0e                                                          ; 913a: a0 0e       ..
    cmp #7                                                            ; 913c: c9 07       ..
    beq c9144                                                         ; 913e: f0 04       ..
    cmp #8                                                            ; 9140: c9 08       ..
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
    bne return_match_osbyte                                           ; 9142: d0 e6       ..
; &9144 referenced 1 time by &913e
.c9144
    ldx #&db                                                          ; 9144: a2 db       ..
    stx nfs_workspace                                                 ; 9146: 86 9e       ..
; &9148 referenced 1 time by &914d
.loop_c9148
    lda (l00f0),y                                                     ; 9148: b1 f0       ..
    sta (nfs_workspace),y                                             ; 914a: 91 9e       ..
    dey                                                               ; 914c: 88          .
    bpl loop_c9148                                                    ; 914d: 10 f9       ..
    iny                                                               ; 914f: c8          .
    dec nfs_workspace                                                 ; 9150: c6 9e       ..
    lda l00ef                                                         ; 9152: a5 ef       ..
    sta (nfs_workspace),y                                             ; 9154: 91 9e       ..
    sty nfs_workspace                                                 ; 9156: 84 9e       ..
    ldy #&14                                                          ; 9158: a0 14       ..
    lda #&e9                                                          ; 915a: a9 e9       ..
    sta (nfs_workspace),y                                             ; 915c: 91 9e       ..
    lda #1                                                            ; 915e: a9 01       ..
    jsr setup_tx_and_send                                             ; 9160: 20 b8 90     ..            ; Load template byte from ctrl_block_template[X]
    stx nfs_workspace                                                 ; 9163: 86 9e       ..
    jmp ctrl_block_setup_alt                                          ; 9165: 4c 68 91    Lh.

; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &833B to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &9168 referenced 3 times by &9053, &9065, &9165
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 9168: a2 0d       ..
    ldy #&7c ; '|'                                                    ; 916a: a0 7c       .|
    bit l8374                                                         ; 916c: 2c 74 83    ,t.
    bvs cbset2                                                        ; 916f: 70 05       p.
; ***************************************************************************************
; Control block setup — main entry
; 
; Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
; Reads the template table at &919D indexed by X, storing each
; value into the target workspace at offset Y. Both X and Y
; are decremented on each iteration.
; 
; Template sentinel values:
;   &FE = stop (end of template for this entry path)
;   &FD = skip (leave existing value unchanged)
;   &FC = use page high byte of target pointer
; ***************************************************************************************
; &9171 referenced 1 time by &848c
.ctrl_block_setup
    ldy #&17                                                          ; 9171: a0 17       ..
    ldx #&1a                                                          ; 9173: a2 1a       ..
; &9175 referenced 1 time by &9239
.ctrl_block_setup_clv
    clv                                                               ; 9175: b8          .
; &9176 referenced 2 times by &916f, &9197
.cbset2
    lda ctrl_block_template,x                                         ; 9176: bd 9d 91    ...
    cmp #&fe                                                          ; 9179: c9 fe       ..
    beq c9199                                                         ; 917b: f0 1c       ..
    cmp #&fd                                                          ; 917d: c9 fd       ..
    beq c9195                                                         ; 917f: f0 14       ..
    cmp #&fc                                                          ; 9181: c9 fc       ..
    bne cbset3                                                        ; 9183: d0 08       ..
    lda net_rx_ptr_hi                                                 ; 9185: a5 9d       ..
    bvs c918b                                                         ; 9187: 70 02       p.
    lda nfs_workspace_hi                                              ; 9189: a5 9f       ..
; &918b referenced 1 time by &9187
.c918b
    sta net_tx_ptr_hi                                                 ; 918b: 85 9b       ..
; &918d referenced 1 time by &9183
.cbset3
    bvs cbset4                                                        ; 918d: 70 04       p.
    sta (nfs_workspace),y                                             ; 918f: 91 9e       ..
    bvc c9195                                                         ; 9191: 50 02       P.             ; ALWAYS branch

; &9193 referenced 1 time by &918d
.cbset4
    sta (net_rx_ptr),y                                                ; 9193: 91 9c       ..
; &9195 referenced 2 times by &917f, &9191
.c9195
    dey                                                               ; 9195: 88          .
    dex                                                               ; 9196: ca          .
    bpl cbset2                                                        ; 9197: 10 dd       ..
; &9199 referenced 1 time by &917b
.c9199
    iny                                                               ; 9199: c8          .
    sty net_tx_ptr                                                    ; 919a: 84 9a       ..
    rts                                                               ; 919c: 60          `

; ***************************************************************************************
; Control block initialisation template
; 
; Read by the loop at &9176, indexed by X from a starting value
; down to 0. Values are stored into either (nfs_workspace) or
; (net_rx_ptr) at offset Y, depending on the V flag.
; 
; Two entry paths read different slices of this table:
;   ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
;   ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &833B
; 
; Sentinel values:
;   &FE = stop processing
;   &FD = skip this offset (decrement Y but don't store)
;   &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)
; ***************************************************************************************
; &919d referenced 1 time by &9176
.ctrl_block_template
    sta l0000                                                         ; 919d: 85 00       ..
    sbc l7dfd,x                                                       ; 919f: fd fd 7d    ..}
    equb &fc, &ff, &ff, &7e, &fc, &ff, &ff,   0,   0, &fe, &80, &93   ; 91a2: fc ff ff... ...
    equb &fd, &fd, &d9, &fc, &ff, &ff, &de, &fc, &ff, &ff, &fe, &d1   ; 91ae: fd fd d9... ...
    equb &fd, &fd, &1f, &fd, &ff, &ff, &fd, &fd, &ff, &ff             ; 91ba: fd fd 1f... ...

; ***************************************************************************************
; Fn 5: printer selection changed (SELECT)
; 
; Called when the printer selection changes. Compares X against
; the network printer buffer number (&F0). If it matches,
; initialises the printer buffer pointer (&0D61 = &1F) and
; sets the initial flag byte (&0D60 = &41). Otherwise falls
; through to return.
; ***************************************************************************************
.remote_display_setup
    dex                                                               ; 91c4: ca          .
    cpx l00f0                                                         ; 91c5: e4 f0       ..
    bne setup1                                                        ; 91c7: d0 07       ..
    lda #&1f                                                          ; 91c9: a9 1f       ..
    sta printer_buf_ptr                                               ; 91cb: 8d 61 0d    .a.
    lda #&41 ; 'A'                                                    ; 91ce: a9 41       .A
; &91d0 referenced 1 time by &91c7
.setup1
    sta l0d60                                                         ; 91d0: 8d 60 0d    .`.
; &91d3 referenced 2 times by &91d6, &91ea
.return_display_setup
    rts                                                               ; 91d3: 60          `

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
    cpy #4                                                            ; 91d4: c0 04       ..
    bne return_display_setup                                          ; 91d6: d0 fb       ..
    txa                                                               ; 91d8: 8a          .
    dex                                                               ; 91d9: ca          .
    bne c9202                                                         ; 91da: d0 26       .&
    tsx                                                               ; 91dc: ba          .
    ora l0106,x                                                       ; 91dd: 1d 06 01    ...
    sta l0106,x                                                       ; 91e0: 9d 06 01    ...
; &91e3 referenced 2 times by &91f2, &91f7
.prlp1
    lda #osbyte_read_buffer                                           ; 91e3: a9 91       ..
    ldx #buffer_printer                                               ; 91e5: a2 03       ..
    jsr osbyte                                                        ; 91e7: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_display_setup                                          ; 91ea: b0 e7       ..
    tya                                                               ; 91ec: 98          .              ; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91ed: 20 f9 91     ..
    cpy #&6e ; 'n'                                                    ; 91f0: c0 6e       .n
    bcc prlp1                                                         ; 91f2: 90 ef       ..
    jsr flush_output_block                                            ; 91f4: 20 25 92     %.
    bcc prlp1                                                         ; 91f7: 90 ea       ..
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; ***************************************************************************************
; &91f9 referenced 2 times by &91ed, &9206
.store_output_byte
    ldy printer_buf_ptr                                               ; 91f9: ac 61 0d    .a.
    sta (net_rx_ptr),y                                                ; 91fc: 91 9c       ..
    inc printer_buf_ptr                                               ; 91fe: ee 61 0d    .a.
    rts                                                               ; 9201: 60          `

; &9202 referenced 1 time by &91da
.c9202
    pha                                                               ; 9202: 48          H
    txa                                                               ; 9203: 8a          .
    eor #1                                                            ; 9204: 49 01       I.
    jsr store_output_byte                                             ; 9206: 20 f9 91     ..
    eor l0d60                                                         ; 9209: 4d 60 0d    M`.
    ror a                                                             ; 920c: 6a          j
    bcc c9216                                                         ; 920d: 90 07       ..
    rol a                                                             ; 920f: 2a          *
    sta l0d60                                                         ; 9210: 8d 60 0d    .`.
    jsr flush_output_block                                            ; 9213: 20 25 92     %.
; &9216 referenced 1 time by &920d
.c9216
    lda l0d60                                                         ; 9216: ad 60 0d    .`.
    and #&f0                                                          ; 9219: 29 f0       ).
    ror a                                                             ; 921b: 6a          j
    tax                                                               ; 921c: aa          .
    pla                                                               ; 921d: 68          h
    ror a                                                             ; 921e: 6a          j
    txa                                                               ; 921f: 8a          .
    rol a                                                             ; 9220: 2a          *
    sta l0d60                                                         ; 9221: 8d 60 0d    .`.
    rts                                                               ; 9224: 60          `

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &9225 referenced 2 times by &91f4, &9213
.flush_output_block
    ldy #8                                                            ; 9225: a0 08       ..
    lda printer_buf_ptr                                               ; 9227: ad 61 0d    .a.
    sta (nfs_workspace),y                                             ; 922a: 91 9e       ..
    lda net_rx_ptr_hi                                                 ; 922c: a5 9d       ..
    iny                                                               ; 922e: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 922f: 91 9e       ..
    ldy #5                                                            ; 9231: a0 05       ..
    sta (nfs_workspace),y                                             ; 9233: 91 9e       ..
    ldy #&0b                                                          ; 9235: a0 0b       ..
    ldx #&26 ; '&'                                                    ; 9237: a2 26       .&
    jsr ctrl_block_setup_clv                                          ; 9239: 20 75 91     u.
    dey                                                               ; 923c: 88          .
    lda l0d60                                                         ; 923d: ad 60 0d    .`.
    pha                                                               ; 9240: 48          H
    rol a                                                             ; 9241: 2a          *
    pla                                                               ; 9242: 68          h
    eor #&80                                                          ; 9243: 49 80       I.
    sta l0d60                                                         ; 9245: 8d 60 0d    .`.
    rol a                                                             ; 9248: 2a          *
    sta (nfs_workspace),y                                             ; 9249: 91 9e       ..
    ldy #&1f                                                          ; 924b: a0 1f       ..
    sty printer_buf_ptr                                               ; 924d: 8c 61 0d    .a.
    lda #0                                                            ; 9250: a9 00       ..
    tax                                                               ; 9252: aa          .              ; X=&00
    ldy nfs_workspace_hi                                              ; 9253: a4 9f       ..
    cli                                                               ; 9255: 58          X
; ***************************************************************************************
; Transmit with retry loop (XMITFS/XMITFY)
; 
; Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
; retries and FSDELY (&60 = 96) ms delay between attempts. On each
; iteration, checks the result code: zero means success, non-zero
; means retry. After all retries exhausted, reports a 'Net error'.
; Entry point XMITFY allows a custom delay in Y.
; ***************************************************************************************
; &9256 referenced 2 times by &83d5, &840f
.econet_tx_retry
    stx net_tx_ptr                                                    ; 9256: 86 9a       ..
    sty net_tx_ptr_hi                                                 ; 9258: 84 9b       ..
    pha                                                               ; 925a: 48          H
    and fs_sequence_nos                                               ; 925b: 2d 08 0e    -..
    beq bsxl1                                                         ; 925e: f0 02       ..
    lda #1                                                            ; 9260: a9 01       ..
; &9262 referenced 1 time by &925e
.bsxl1
    ldy #0                                                            ; 9262: a0 00       ..
    ora (net_tx_ptr),y                                                ; 9264: 11 9a       ..
    pha                                                               ; 9266: 48          H
    sta (net_tx_ptr),y                                                ; 9267: 91 9a       ..
    jsr tx_poll_ff                                                    ; 9269: 20 68 86     h.
    lda #&ff                                                          ; 926c: a9 ff       ..
    ldy #8                                                            ; 926e: a0 08       ..
    sta (net_tx_ptr),y                                                ; 9270: 91 9a       ..
    iny                                                               ; 9272: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 9273: 91 9a       ..
    pla                                                               ; 9275: 68          h
    tax                                                               ; 9276: aa          .
    ldy #&d1                                                          ; 9277: a0 d1       ..
    pla                                                               ; 9279: 68          h
    pha                                                               ; 927a: 48          H
    beq bspsx                                                         ; 927b: f0 02       ..
    ldy #&90                                                          ; 927d: a0 90       ..
; &927f referenced 1 time by &927b
.bspsx
    tya                                                               ; 927f: 98          .
    ldy #1                                                            ; 9280: a0 01       ..
    sta (net_tx_ptr),y                                                ; 9282: 91 9a       ..
    txa                                                               ; 9284: 8a          .
    dey                                                               ; 9285: 88          .              ; Y=&00
    pha                                                               ; 9286: 48          H
; &9287 referenced 1 time by &9293
.bsxl0
    lda #&7f                                                          ; 9287: a9 7f       ..
    sta (net_tx_ptr),y                                                ; 9289: 91 9a       ..
    jsr send_to_fs_star                                               ; 928b: 20 eb 84     ..
    pla                                                               ; 928e: 68          h
    pha                                                               ; 928f: 48          H
    eor (net_tx_ptr),y                                                ; 9290: 51 9a       Q.
    ror a                                                             ; 9292: 6a          j
    bcs bsxl0                                                         ; 9293: b0 f2       ..
    pla                                                               ; 9295: 68          h
    pla                                                               ; 9296: 68          h
    tax                                                               ; 9297: aa          .
    inx                                                               ; 9298: e8          .
    beq return_bspsx                                                  ; 9299: f0 03       ..
    eor fs_sequence_nos                                               ; 929b: 4d 08 0e    M..
; &929e referenced 1 time by &9299
.return_bspsx
    rts                                                               ; 929e: 60          `

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
; (OSBYTE &C3) using the 3-entry table at &9312 (osbyte_vdu_table).
; On completion, restores the JSR buffer protection bits (LSTAT)
; from OLDJSR to re-enable JSR reception, which was disabled during
; the screen data capture to prevent interference.
; ***************************************************************************************
.save_palette_vdu
    lda fs_load_addr_2                                                ; 929f: a5 b2       ..
    pha                                                               ; 92a1: 48          H
    lda #&e9                                                          ; 92a2: a9 e9       ..
    sta nfs_workspace                                                 ; 92a4: 85 9e       ..
    ldy #0                                                            ; 92a6: a0 00       ..
    sty fs_load_addr_2                                                ; 92a8: 84 b2       ..
    lda l0350                                                         ; 92aa: ad 50 03    .P.
    sta (nfs_workspace),y                                             ; 92ad: 91 9e       ..
    inc nfs_workspace                                                 ; 92af: e6 9e       ..
    lda l0351                                                         ; 92b1: ad 51 03    .Q.
    pha                                                               ; 92b4: 48          H
    tya                                                               ; 92b5: 98          .              ; A=&00
; &92b6 referenced 1 time by &92d5
.loop_c92b6
    sta (nfs_workspace),y                                             ; 92b6: 91 9e       ..
    ldx nfs_workspace                                                 ; 92b8: a6 9e       ..
    ldy nfs_workspace_hi                                              ; 92ba: a4 9f       ..
    lda #osword_read_palette                                          ; 92bc: a9 0b       ..
    jsr osword                                                        ; 92be: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92c1: 68          h
    ldy #0                                                            ; 92c2: a0 00       ..
    sta (nfs_workspace),y                                             ; 92c4: 91 9e       ..
    iny                                                               ; 92c6: c8          .              ; Y=&01
    lda (nfs_workspace),y                                             ; 92c7: b1 9e       ..
    pha                                                               ; 92c9: 48          H
    ldx nfs_workspace                                                 ; 92ca: a6 9e       ..
    inc nfs_workspace                                                 ; 92cc: e6 9e       ..
    inc fs_load_addr_2                                                ; 92ce: e6 b2       ..
    dey                                                               ; 92d0: 88          .              ; Y=&00
    lda fs_load_addr_2                                                ; 92d1: a5 b2       ..
    cpx #&f9                                                          ; 92d3: e0 f9       ..
    bne loop_c92b6                                                    ; 92d5: d0 df       ..
    pla                                                               ; 92d7: 68          h
    sty fs_load_addr_2                                                ; 92d8: 84 b2       ..
    inc nfs_workspace                                                 ; 92da: e6 9e       ..
    jsr save_vdu_state                                                ; 92dc: 20 eb 92     ..
    inc nfs_workspace                                                 ; 92df: e6 9e       ..
    pla                                                               ; 92e1: 68          h
    sta fs_load_addr_2                                                ; 92e2: 85 b2       ..
; &92e4 referenced 4 times by &8470, &8498, &84bf, &8ee4
.clear_jsr_protection
    lda saved_jsr_mask                                                ; 92e4: ad 65 0d    .e.
    sta prot_status                                                   ; 92e7: 8d 63 0d    .c.
    rts                                                               ; 92ea: 60          `

; ***************************************************************************************
; Save VDU workspace state
; 
; Stores the cursor position value from &0355 into NFS workspace,
; then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
; and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
; each result into consecutive workspace bytes.
; ***************************************************************************************
; &92eb referenced 1 time by &92dc
.save_vdu_state
    lda l0355                                                         ; 92eb: ad 55 03    .U.
    sta (nfs_workspace),y                                             ; 92ee: 91 9e       ..
    tax                                                               ; 92f0: aa          .
    jsr read_vdu_osbyte                                               ; 92f1: 20 fe 92     ..
    inc nfs_workspace                                                 ; 92f4: e6 9e       ..
    tya                                                               ; 92f6: 98          .
    sta (nfs_workspace,x)                                             ; 92f7: 81 9e       ..
    jsr read_vdu_osbyte_x0                                            ; 92f9: 20 fc 92     ..
; &92fc referenced 1 time by &92f9
.read_vdu_osbyte_x0
    ldx #0                                                            ; 92fc: a2 00       ..
; &92fe referenced 1 time by &92f1
.read_vdu_osbyte
    ldy fs_load_addr_2                                                ; 92fe: a4 b2       ..
    inc fs_load_addr_2                                                ; 9300: e6 b2       ..
    inc nfs_workspace                                                 ; 9302: e6 9e       ..
    lda osbyte_vdu_table,y                                            ; 9304: b9 12 93    ...
    ldy #&ff                                                          ; 9307: a0 ff       ..
    jsr osbyte                                                        ; 9309: 20 f4 ff     ..
    txa                                                               ; 930c: 8a          .
    ldx #0                                                            ; 930d: a2 00       ..
    sta (nfs_workspace,x)                                             ; 930f: 81 9e       ..
    rts                                                               ; 9311: 60          `

; Table of 3 OSBYTE codes used by save_palette_vdu_state (&929F):
;   &85 = read cursor position
;   &C2 = read shadow RAM allocation
;   &C3 = read screen start address
; &9312 referenced 1 time by &9304
.osbyte_vdu_table
    equb &85, &c2, &c3                                                ; 9312: 85 c2 c3    ...
; &9315 referenced 1 time by &813a

    org &965a

    equb &e5, &e5, &e5, &e5, &e5, &e5                                 ; 965a: e5 e5 e5... ...

; &9660 referenced 2 times by &8683, &8ecf
.trampoline_tx_setup
    jmp c9bf3                                                         ; 9660: 4c f3 9b    L..

; &9663 referenced 1 time by &8303
.trampoline_adlc_init
    jmp adlc_init                                                     ; 9663: 4c 6f 96    Lo.

.svc_nmi_release
    jmp c96b1                                                         ; 9666: 4c b1 96    L..

.svc_nmi_claim
    jmp c96dc                                                         ; 9669: 4c dc 96    L..

.svc_unknown_irq
    jmp c9b61                                                         ; 966c: 4c 61 9b    La.

; ***************************************************************************************
; ADLC initialisation
; 
; Reads station ID (INTOFF side effect), performs full ADLC reset,
; checks for Tube presence (OSBYTE &EA), then falls through to
; adlc_init_workspace.
; ***************************************************************************************
; &966f referenced 1 time by &9663
.adlc_init
    bit station_id_disable_net_nmis                                   ; 966f: 2c 18 fe    ,..
    jsr adlc_full_reset                                               ; 9672: 20 e6 96     ..
    lda #osbyte_read_tube_presence                                    ; 9675: a9 ea       ..
    ldx #0                                                            ; 9677: a2 00       ..
    ldy #&ff                                                          ; 9679: a0 ff       ..
    jsr osbyte                                                        ; 967b: 20 f4 ff     ..            ; Read Tube present flag
    stx tx_in_progress                                                ; 967e: 8e 52 0d    .R.            ; X=value of Tube present flag
    lda #osbyte_issue_service_request                                 ; 9681: a9 8f       ..
    ldx #&0c                                                          ; 9683: a2 0c       ..
    ldy #&ff                                                          ; 9685: a0 ff       ..
; ***************************************************************************************
; Initialise NMI workspace
; 
; New in 3.35D: issues OSBYTE &8F with X=&0C (NMI claim service
; request) before copying the NMI shim. Sub-entry at &968A skips
; the service request for quick re-init. Then copies 32 bytes of
; NMI shim from ROM (&9FE8) to RAM (&0D00), patches the current
; ROM bank number into the shim's self-modifying code at &0D07,
; sets TX clear flag and econet_init_flag to &80, reads station ID
; from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
; and re-enables NMIs by reading &FE20 (INTON side effect).
; ***************************************************************************************
.adlc_init_workspace
    jsr osbyte                                                        ; 9687: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=12 - NMI claim
; &968a referenced 1 time by &96e3
.c968a
    ldy #&20 ; ' '                                                    ; 968a: a0 20       .
; &968c referenced 1 time by &9693
.loop_c968c
    lda nmi_shim_rom_src,y                                            ; 968c: b9 d9 9f    ...
    sta l0cff,y                                                       ; 968f: 99 ff 0c    ...
    dey                                                               ; 9692: 88          .
    bne loop_c968c                                                    ; 9693: d0 f7       ..
    lda romsel_copy                                                   ; 9695: a5 f4       ..
    sta nmi_shim_07                                                   ; 9697: 8d 07 0d    ...
    lda #&80                                                          ; 969a: a9 80       ..
    sta tx_clear_flag                                                 ; 969c: 8d 62 0d    .b.
    sta econet_init_flag                                              ; 969f: 8d 66 0d    .f.
    lda station_id_disable_net_nmis                                   ; 96a2: ad 18 fe    ...
    sta tx_src_stn                                                    ; 96a5: 8d 22 0d    .".
    lda #0                                                            ; 96a8: a9 00       ..
    sta tx_src_net                                                    ; 96aa: 8d 23 0d    .#.
    bit video_ula_control                                             ; 96ad: 2c 20 fe    , .
    rts                                                               ; 96b0: 60          `

; &96b1 referenced 1 time by &9666
.c96b1
    lda #0                                                            ; 96b1: a9 00       ..
    sta tx_clear_flag                                                 ; 96b3: 8d 62 0d    .b.
    bit econet_init_flag                                              ; 96b6: 2c 66 0d    ,f.
    bpl c96d9                                                         ; 96b9: 10 1e       ..
    sta econet_init_flag                                              ; 96bb: 8d 66 0d    .f.
; &96be referenced 2 times by &96c3, &96ca
.c96be
    lda nmi_jmp_lo                                                    ; 96be: ad 0c 0d    ...
    cmp #0                                                            ; 96c1: c9 00       ..
    bne c96be                                                         ; 96c3: d0 f9       ..
    lda nmi_jmp_hi                                                    ; 96c5: ad 0d 0d    ...
    cmp #&97                                                          ; 96c8: c9 97       ..
    bne c96be                                                         ; 96ca: d0 f2       ..
    bit station_id_disable_net_nmis                                   ; 96cc: 2c 18 fe    ,..
; ***************************************************************************************
; Save Econet state to RX control block
; 
; Stores rx_status_flags, protection_mask, and tx_in_progress
; to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.
; ***************************************************************************************
.save_econet_state
    bit station_id_disable_net_nmis                                   ; 96cf: 2c 18 fe    ,..
    ldy #8                                                            ; 96d2: a0 08       ..
    lda tx_in_progress                                                ; 96d4: ad 52 0d    .R.
    sta (net_rx_ptr),y                                                ; 96d7: 91 9c       ..
; &96d9 referenced 1 time by &96b9
.c96d9
    jmp adlc_rx_listen                                                ; 96d9: 4c f5 96    L..

; &96dc referenced 1 time by &9669
.c96dc
    ldy #8                                                            ; 96dc: a0 08       ..
    lda (net_rx_ptr),y                                                ; 96de: b1 9c       ..
    sta tx_in_progress                                                ; 96e0: 8d 52 0d    .R.
    jmp c968a                                                         ; 96e3: 4c 8a 96    L..

; ***************************************************************************************
; ADLC full reset
; 
; Aborts all activity and returns to idle RX listen mode.
; ***************************************************************************************
; &96e6 referenced 3 times by &9672, &9748, &989e
.adlc_full_reset
    lda #&c1                                                          ; 96e6: a9 c1       ..             ; CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)
    sta econet_control1_or_status1                                    ; 96e8: 8d a0 fe    ...
    lda #&1e                                                          ; 96eb: a9 1e       ..
    sta econet_data_terminate_frame                                   ; 96ed: 8d a3 fe    ...
    lda #0                                                            ; 96f0: a9 00       ..             ; CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR
    sta econet_control23_or_status2                                   ; 96f2: 8d a1 fe    ...
; ***************************************************************************************
; Enter RX listen mode
; 
; TX held in reset, RX active with interrupts. Clears all status.
; ***************************************************************************************
; &96f5 referenced 2 times by &96d9, &9a56
.adlc_rx_listen
    lda #&82                                                          ; 96f5: a9 82       ..             ; CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding; CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)
    sta econet_control1_or_status1                                    ; 96f7: 8d a0 fe    ...
    lda #&67 ; 'g'                                                    ; 96fa: a9 67       .g             ; CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 96fc: 8d a1 fe    ...
    rts                                                               ; 96ff: 60          `

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
    beq c9718                                                         ; 970d: f0 09       ..             ; Match -- accept frame
    cmp #&ff                                                          ; 970f: c9 ff       ..             ; Check for broadcast address (&FF)
    bne scout_reject                                                  ; 9711: d0 1a       ..             ; Neither our address nor broadcast -- reject frame
    lda #&40 ; '@'                                                    ; 9713: a9 40       .@             ; Flag &40 = broadcast frame
    sta tx_flags                                                      ; 9715: 8d 4a 0d    .J.
; &9718 referenced 1 time by &970d
.c9718
    lda #&1f                                                          ; 9718: a9 1f       ..             ; Install next NMI handler at &9715 (RX scout second byte)
    ldy #&97                                                          ; 971a: a0 97       ..
    jmp set_nmi_vector                                                ; 971c: 4c 0e 0d    L..

; ***************************************************************************************
; RX scout second byte handler
; 
; Reads the second byte of an incoming scout (destination network).
; Checks for network match: 0 = local network (accept), &FF = broadcast
; (accept and flag), anything else = reject.
; Installs the scout data reading loop handler at &9747.
; ***************************************************************************************
.nmi_rx_scout_net
    bit econet_control23_or_status2                                   ; 971f: 2c a1 fe    ,..            ; BIT SR2: test for RDA (bit7 = data available)
    bpl scout_error                                                   ; 9722: 10 1d       ..             ; No RDA -- check errors
    lda econet_data_continue_frame                                    ; 9724: ad a2 fe    ...            ; Read destination network byte
    beq c9735                                                         ; 9727: f0 0c       ..             ; Network = 0 -- local network, accept
    eor #&ff                                                          ; 9729: 49 ff       I.             ; EOR &FF: test if network = &FF (broadcast)
    beq c9738                                                         ; 972b: f0 0b       ..             ; Broadcast network -- accept
; &972d referenced 1 time by &9711
.scout_reject
    lda #&a2                                                          ; 972d: a9 a2       ..             ; Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE
    sta econet_control1_or_status1                                    ; 972f: 8d a0 fe    ...
    jmp c9a59                                                         ; 9732: 4c 59 9a    LY.

; &9735 referenced 1 time by &9727
.c9735
    sta tx_flags                                                      ; 9735: 8d 4a 0d    .J.            ; Network = &FF broadcast: clear &0D4A
; &9738 referenced 1 time by &972b
.c9738
    sta port_buf_len                                                  ; 9738: 85 a2       ..             ; Store Y offset for scout data buffer
    lda #&51 ; 'Q'                                                    ; 973a: a9 51       .Q             ; Install scout data reading loop at &9747
    ldy #&97                                                          ; 973c: a0 97       ..
    jmp set_nmi_vector                                                ; 973e: 4c 0e 0d    L..

; ***************************************************************************************
; Scout error/discard handler
; 
; Reached when the scout data loop sees no RDA (BPL at &9756) or
; when scout completion finds unexpected SR2 state.
; If SR2 & &81 is non-zero (AP or RDA still active), performs full
; ADLC reset and discards. If zero (clean end), discards via &9A56.
; This path is a common landing for any unexpected ADLC state during
; scout reception.
; ***************************************************************************************
; &9741 referenced 5 times by &9705, &9722, &9756, &978a, &978c
.scout_error
    lda econet_control23_or_status2                                   ; 9741: ad a1 fe    ...            ; Read SR2
    and #&81                                                          ; 9744: 29 81       ).             ; Test AP (b0) | RDA (b7)
    beq scout_discard                                                 ; 9746: f0 06       ..             ; Neither set -- clean end, discard via &9A40
    jsr adlc_full_reset                                               ; 9748: 20 e6 96     ..            ; Unexpected data/status: full ADLC reset
    jmp c9a59                                                         ; 974b: 4c 59 9a    LY.            ; Discard and return to idle

; &974e referenced 1 time by &9746
.scout_discard
    jmp discard_listen                                                ; 974e: 4c 56 9a    LV.

; ***************************************************************************************
; Scout data reading loop
; 
; Reads the body of a scout frame, two bytes per iteration. Stores
; bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
; Between each pair it checks SR2:
;   - SR2 & &81 tested at entry (&974A): AP|RDA bits
;     - Neither set (BEQ) -> discard (&974E -> &9A56)
;     - AP without RDA (BPL) -> error (&9741)
;     - RDA set (BMI) -> read byte
;   - After first byte (&9755): full SR2 tested
;     - SR2 non-zero (BNE) -> scout completion (&977B)
;       This is the FV detection point: when FV is set (by inline refill
;       of the last byte during the preceding RX FIFO read), SR2 is
;       non-zero and the branch is taken.
;     - SR2 = 0 -> read second byte and loop
;   - After second byte (&9769): re-test SR2 & &81 for next pair
;     - RDA set (BMI) -> loop back to &974E
;     - Neither set -> RTI, wait for next NMI
; The loop ends at Y=&0C (12 bytes max in scout buffer).
; ***************************************************************************************
    ldy port_buf_len                                                  ; 9751: a4 a2       ..             ; Y = buffer offset
    lda econet_control23_or_status2                                   ; 9753: ad a1 fe    ...            ; Read SR2
; &9756 referenced 1 time by &9776
.scout_loop_rda
    bpl scout_error                                                   ; 9756: 10 e9       ..             ; No RDA -- error handler &9737
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
    cpy #&0c                                                          ; 976d: c0 0c       ..
    beq scout_complete                                                ; 976f: f0 0a       ..             ; Buffer full (Y=12) -- force completion
    sty port_buf_len                                                  ; 9771: 84 a2       ..
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
;   - Port = 0 -> immediate operation (&9A6F)
;   - Port non-zero -> check if it matches an open receive block
; ***************************************************************************************
; &977b referenced 2 times by &9764, &976f
.scout_complete
    lda #0                                                            ; 977b: a9 00       ..             ; Save Y for next iteration; CR1=&00: disable all interrupts
    sta econet_control1_or_status1                                    ; 977d: 8d a0 fe    ...
    lda #&84                                                          ; 9780: a9 84       ..             ; CR2=&84: disable PSE, enable RDA_SUPPRESS_FV
    sta econet_control23_or_status2                                   ; 9782: 8d a1 fe    ...
    lda #2                                                            ; 9785: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9787: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq scout_error                                                   ; 978a: f0 b5       ..             ; No FV -- not a valid frame end, error
    bpl scout_error                                                   ; 978c: 10 b3       ..             ; FV set but no RDA -- missing last byte, error
    lda econet_data_continue_frame                                    ; 978e: ad a2 fe    ...            ; Read last byte from RX FIFO
    sta rx_src_stn,y                                                  ; 9791: 99 3d 0d    .=.            ; Store last byte at &0D3D+Y
    lda #&44 ; 'D'                                                    ; 9794: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX for ACK)
    sta econet_control1_or_status1                                    ; 9796: 8d a0 fe    ...
    lda rx_port                                                       ; 9799: ad 40 0d    .@.            ; Check port byte: 0 = immediate op, non-zero = data transfer
    bne scout_match_port                                              ; 979c: d0 06       ..             ; Port non-zero -- look for matching receive block
    jmp immediate_op                                                  ; 979e: 4c 6f 9a    Lo.            ; Port = 0 -- immediate operation handler

; &97a1 referenced 3 times by &97ec, &97f1, &9823
.scout_no_match
    jmp c9894                                                         ; 97a1: 4c 94 98    L..

; &97a4 referenced 1 time by &979c
.scout_match_port
    bit tx_flags                                                      ; 97a4: 2c 4a 0d    ,J.
    bvc c97ae                                                         ; 97a7: 50 05       P.
    lda #7                                                            ; 97a9: a9 07       ..
    sta econet_control23_or_status2                                   ; 97ab: 8d a1 fe    ...
; &97ae referenced 1 time by &97a7
.c97ae
    bit rx_flags                                                      ; 97ae: 2c 64 0d    ,d.
    bpl c97ee                                                         ; 97b1: 10 3b       .;
    lda #&c0                                                          ; 97b3: a9 c0       ..
    sta port_ws_offset                                                ; 97b5: 85 a6       ..
    lda #0                                                            ; 97b7: a9 00       ..
    sta rx_buf_offset                                                 ; 97b9: 85 a7       ..
; &97bb referenced 1 time by &97e8
.c97bb
    ldy #0                                                            ; 97bb: a0 00       ..
; &97bd referenced 1 time by &97fb
.c97bd
    lda (port_ws_offset),y                                            ; 97bd: b1 a6       ..
    beq c97ea                                                         ; 97bf: f0 29       .)
    cmp #&7f                                                          ; 97c1: c9 7f       ..
    bne c97e1                                                         ; 97c3: d0 1c       ..
    iny                                                               ; 97c5: c8          .
    lda (port_ws_offset),y                                            ; 97c6: b1 a6       ..
    beq c97cf                                                         ; 97c8: f0 05       ..
    cmp rx_port                                                       ; 97ca: cd 40 0d    .@.
    bne c97e1                                                         ; 97cd: d0 12       ..
; &97cf referenced 1 time by &97c8
.c97cf
    iny                                                               ; 97cf: c8          .
    lda (port_ws_offset),y                                            ; 97d0: b1 a6       ..
    beq c97d9                                                         ; 97d2: f0 05       ..
    cmp rx_src_stn                                                    ; 97d4: cd 3d 0d    .=.
    bne c97e1                                                         ; 97d7: d0 08       ..
; &97d9 referenced 1 time by &97d2
.c97d9
    iny                                                               ; 97d9: c8          .
    lda (port_ws_offset),y                                            ; 97da: b1 a6       ..
    cmp rx_src_net                                                    ; 97dc: cd 3e 0d    .>.
    beq c97fd                                                         ; 97df: f0 1c       ..
; &97e1 referenced 3 times by &97c3, &97cd, &97d7
.c97e1
    lda port_ws_offset                                                ; 97e1: a5 a6       ..
    clc                                                               ; 97e3: 18          .
    adc #&0c                                                          ; 97e4: 69 0c       i.
    sta port_ws_offset                                                ; 97e6: 85 a6       ..
    bcc c97bb                                                         ; 97e8: 90 d1       ..
; &97ea referenced 1 time by &97bf
.c97ea
    lda rx_buf_offset                                                 ; 97ea: a5 a7       ..
    bne scout_no_match                                                ; 97ec: d0 b3       ..
; &97ee referenced 1 time by &97b1
.c97ee
    bit rx_flags                                                      ; 97ee: 2c 64 0d    ,d.
    bvc scout_no_match                                                ; 97f1: 50 ae       P.
    lda nfs_workspace_hi                                              ; 97f3: a5 9f       ..
    sta rx_buf_offset                                                 ; 97f5: 85 a7       ..
    ldy #0                                                            ; 97f7: a0 00       ..
    sty port_ws_offset                                                ; 97f9: 84 a6       ..
    beq c97bd                                                         ; 97fb: f0 c0       ..             ; ALWAYS branch

; &97fd referenced 1 time by &97df
.c97fd
    bit tx_flags                                                      ; 97fd: 2c 4a 0d    ,J.
    bvc c9805                                                         ; 9800: 50 03       P.
    jmp c9a60                                                         ; 9802: 4c 60 9a    L`.

; &9805 referenced 2 times by &9800, &9adb
.c9805
    lda #3                                                            ; 9805: a9 03       ..
    sta scout_status                                                  ; 9807: 8d 5c 0d    .\.
    lda nmi_tx_block                                                  ; 980a: a5 a0       ..
    pha                                                               ; 980c: 48          H
    lda nmi_tx_block_hi                                               ; 980d: a5 a1       ..
    pha                                                               ; 980f: 48          H
    lda port_ws_offset                                                ; 9810: a5 a6       ..
    sta nmi_tx_block                                                  ; 9812: 85 a0       ..
    lda rx_buf_offset                                                 ; 9814: a5 a7       ..
    sta nmi_tx_block_hi                                               ; 9816: 85 a1       ..
    jsr tx_calc_transfer                                              ; 9818: 20 6a 9f     j.
    pla                                                               ; 981b: 68          h
    sta nmi_tx_block_hi                                               ; 981c: 85 a1       ..
    pla                                                               ; 981e: 68          h
    sta nmi_tx_block                                                  ; 981f: 85 a0       ..
    bcs c9826                                                         ; 9821: b0 03       ..
    jmp scout_no_match                                                ; 9823: 4c a1 97    L..

; &9826 referenced 2 times by &9821, &9ad0
.c9826
    lda #&44 ; 'D'                                                    ; 9826: a9 44       .D
    sta econet_control1_or_status1                                    ; 9828: 8d a0 fe    ...
    lda #&a7                                                          ; 982b: a9 a7       ..
    sta econet_control23_or_status2                                   ; 982d: 8d a1 fe    ...
    lda #&37 ; '7'                                                    ; 9830: a9 37       .7
    ldy #&98                                                          ; 9832: a0 98       ..
    jmp ack_tx_write_dest                                             ; 9834: 4c 7e 99    L~.

.data_rx_setup
    lda #&82                                                          ; 9837: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for data frame)
    sta econet_control1_or_status1                                    ; 9839: 8d a0 fe    ...
    lda #&43 ; 'C'                                                    ; 983c: a9 43       .C
    ldy #&98                                                          ; 983e: a0 98       ..
    jmp set_nmi_vector                                                ; 9840: 4c 0e 0d    L..

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
    lda #1                                                            ; 9843: a9 01       ..             ; Read SR2 for AP check
    bit econet_control23_or_status2                                   ; 9845: 2c a1 fe    ,..
    beq c9894                                                         ; 9848: f0 4a       .J
    lda econet_data_continue_frame                                    ; 984a: ad a2 fe    ...
    cmp station_id_disable_net_nmis                                   ; 984d: cd 18 fe    ...
    bne c9894                                                         ; 9850: d0 42       .B
    lda #&59 ; 'Y'                                                    ; 9852: a9 59       .Y
    ldy #&98                                                          ; 9854: a0 98       ..
    jmp set_nmi_vector                                                ; 9856: 4c 0e 0d    L..

.nmi_data_rx_net
    bit econet_control23_or_status2                                   ; 9859: 2c a1 fe    ,..            ; Validate source network = 0
    bpl c9894                                                         ; 985c: 10 36       .6
    lda econet_data_continue_frame                                    ; 985e: ad a2 fe    ...
    bne c9894                                                         ; 9861: d0 31       .1
    lda #&6f ; 'o'                                                    ; 9863: a9 6f       .o
    ldy #&98                                                          ; 9865: a0 98       ..
    bit econet_control1_or_status1                                    ; 9867: 2c a0 fe    ,..
    bmi nmi_data_rx_skip                                              ; 986a: 30 03       0.
    jmp set_nmi_vector                                                ; 986c: 4c 0e 0d    L..

; &986f referenced 1 time by &986a
.nmi_data_rx_skip
    bit econet_control23_or_status2                                   ; 986f: 2c a1 fe    ,..            ; Skip control and port bytes (already known from scout)
    bpl c9894                                                         ; 9872: 10 20       .
    lda econet_data_continue_frame                                    ; 9874: ad a2 fe    ...            ; Discard control byte
    lda econet_data_continue_frame                                    ; 9877: ad a2 fe    ...            ; Discard port byte
; &987a referenced 1 time by &9f3e
.c987a
    lda #2                                                            ; 987a: a9 02       ..
    bit tx_flags                                                      ; 987c: 2c 4a 0d    ,J.
    bne c988d                                                         ; 987f: d0 0c       ..
    lda #&a4                                                          ; 9881: a9 a4       ..
    ldy #&98                                                          ; 9883: a0 98       ..
    bit econet_control1_or_status1                                    ; 9885: 2c a0 fe    ,..
    bmi nmi_data_rx_bulk                                              ; 9888: 30 1a       0.
    jmp set_nmi_vector                                                ; 988a: 4c 0e 0d    L..

; &988d referenced 1 time by &987f
.c988d
    lda #1                                                            ; 988d: a9 01       ..
    ldy #&99                                                          ; 988f: a0 99       ..
    jmp set_nmi_vector                                                ; 9891: 4c 0e 0d    L..

; &9894 referenced 12 times by &97a1, &9848, &9850, &985c, &9861, &9872, &98b7, &98e9, &98ef, &993a, &99c2, &9aa2
.c9894
    lda tx_flags                                                      ; 9894: ad 4a 0d    .J.
    bpl rx_error                                                      ; 9897: 10 05       ..
    lda #&41 ; 'A'                                                    ; 9899: a9 41       .A
    jmp tx_store_result                                               ; 989b: 4c 4e 9f    LN.

; &989e referenced 1 time by &9897
.rx_error
.rx_error_reset
    jsr adlc_full_reset                                               ; 989e: 20 e6 96     ..
    jmp discard_reset_listen                                          ; 98a1: 4c 4a 9a    LJ.

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
.c98a9
    bpl data_rx_complete                                              ; 98a9: 10 2d       .-
    lda econet_data_continue_frame                                    ; 98ab: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 98ae: 91 a4       ..
    iny                                                               ; 98b0: c8          .
    bne c98b9                                                         ; 98b1: d0 06       ..
    inc open_port_buf_hi                                              ; 98b3: e6 a5       ..
    dec port_buf_len_hi                                               ; 98b5: c6 a3       ..
    beq c9894                                                         ; 98b7: f0 db       ..
; &98b9 referenced 1 time by &98b1
.c98b9
    lda econet_control23_or_status2                                   ; 98b9: ad a1 fe    ...
    bmi c98c0                                                         ; 98bc: 30 02       0.
    bne data_rx_complete                                              ; 98be: d0 18       ..
; &98c0 referenced 1 time by &98bc
.c98c0
    lda econet_data_continue_frame                                    ; 98c0: ad a2 fe    ...
    sta (open_port_buf),y                                             ; 98c3: 91 a4       ..
    iny                                                               ; 98c5: c8          .
    sty port_buf_len                                                  ; 98c6: 84 a2       ..
    bne c98d0                                                         ; 98c8: d0 06       ..
    inc open_port_buf_hi                                              ; 98ca: e6 a5       ..
    dec port_buf_len_hi                                               ; 98cc: c6 a3       ..
    beq data_rx_complete                                              ; 98ce: f0 08       ..
; &98d0 referenced 1 time by &98c8
.c98d0
    lda econet_control23_or_status2                                   ; 98d0: ad a1 fe    ...
    bne c98a9                                                         ; 98d3: d0 d4       ..
    jmp nmi_rti                                                       ; 98d5: 4c 14 0d    L..

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
    sta econet_control1_or_status1                                    ; 98da: 8d a0 fe    ...
    lda #&84                                                          ; 98dd: a9 84       ..             ; CR2=&84: disable PSE for individual bit testing
    sta econet_control23_or_status2                                   ; 98df: 8d a1 fe    ...
    sty port_buf_len                                                  ; 98e2: 84 a2       ..
    lda #2                                                            ; 98e4: a9 02       ..             ; A=&02: FV mask
    bit econet_control23_or_status2                                   ; 98e6: 2c a1 fe    ,..            ; BIT SR2: test FV (Z) and RDA (N)
    beq c9894                                                         ; 98e9: f0 a9       ..             ; No FV -- error
    bpl c98fe                                                         ; 98eb: 10 11       ..             ; FV set, no RDA -- proceed to ACK
    lda port_buf_len_hi                                               ; 98ed: a5 a3       ..
    beq c9894                                                         ; 98ef: f0 a3       ..
    lda econet_data_continue_frame                                    ; 98f1: ad a2 fe    ...            ; FV+RDA: read and store last data byte
    ldy port_buf_len                                                  ; 98f4: a4 a2       ..
    sta (open_port_buf),y                                             ; 98f6: 91 a4       ..
    inc port_buf_len                                                  ; 98f8: e6 a2       ..
    bne c98fe                                                         ; 98fa: d0 02       ..
    inc open_port_buf_hi                                              ; 98fc: e6 a5       ..
; &98fe referenced 2 times by &98eb, &98fa
.c98fe
    jmp ack_tx                                                        ; 98fe: 4c 68 99    Lh.

.nmi_data_rx_tube
    lda econet_control23_or_status2                                   ; 9901: ad a1 fe    ...
; &9904 referenced 1 time by &9935
.c9904
    bpl data_rx_tube_complete                                         ; 9904: 10 37       .7
    lda econet_data_continue_frame                                    ; 9906: ad a2 fe    ...
    inc port_buf_len                                                  ; 9909: e6 a2       ..
    sta tube_data_register_3                                          ; 990b: 8d e5 fe    ...
    bne c991c                                                         ; 990e: d0 0c       ..
    inc port_buf_len_hi                                               ; 9910: e6 a3       ..
    bne c991c                                                         ; 9912: d0 08       ..
    inc open_port_buf                                                 ; 9914: e6 a4       ..
    bne c991c                                                         ; 9916: d0 04       ..
    inc open_port_buf_hi                                              ; 9918: e6 a5       ..
    beq data_rx_tube_error                                            ; 991a: f0 1e       ..
; &991c referenced 3 times by &990e, &9912, &9916
.c991c
    lda econet_data_continue_frame                                    ; 991c: ad a2 fe    ...
    sta tube_data_register_3                                          ; 991f: 8d e5 fe    ...
    inc port_buf_len                                                  ; 9922: e6 a2       ..
    bne c9932                                                         ; 9924: d0 0c       ..
    inc port_buf_len_hi                                               ; 9926: e6 a3       ..
    bne c9932                                                         ; 9928: d0 08       ..
    inc open_port_buf                                                 ; 992a: e6 a4       ..
    bne c9932                                                         ; 992c: d0 04       ..
    inc open_port_buf_hi                                              ; 992e: e6 a5       ..
    beq data_rx_tube_complete                                         ; 9930: f0 0b       ..
; &9932 referenced 3 times by &9924, &9928, &992c
.c9932
    lda econet_control23_or_status2                                   ; 9932: ad a1 fe    ...
    bne c9904                                                         ; 9935: d0 cd       ..
    jmp nmi_rti                                                       ; 9937: 4c 14 0d    L..

; &993a referenced 3 times by &991a, &994c, &9958
.data_rx_tube_error
    jmp c9894                                                         ; 993a: 4c 94 98    L..

; &993d referenced 2 times by &9904, &9930
.data_rx_tube_complete
    lda #0                                                            ; 993d: a9 00       ..
    sta econet_control1_or_status1                                    ; 993f: 8d a0 fe    ...
    lda #&84                                                          ; 9942: a9 84       ..
    sta econet_control23_or_status2                                   ; 9944: 8d a1 fe    ...
    lda #2                                                            ; 9947: a9 02       ..
    bit econet_control23_or_status2                                   ; 9949: 2c a1 fe    ,..
    beq data_rx_tube_error                                            ; 994c: f0 ec       ..
    bpl ack_tx                                                        ; 994e: 10 18       ..
    lda port_buf_len                                                  ; 9950: a5 a2       ..
    ora port_buf_len_hi                                               ; 9952: 05 a3       ..
    ora open_port_buf                                                 ; 9954: 05 a4       ..
    ora open_port_buf_hi                                              ; 9956: 05 a5       ..
    beq data_rx_tube_error                                            ; 9958: f0 e0       ..
    lda econet_data_continue_frame                                    ; 995a: ad a2 fe    ...
    sta rx_extra_byte                                                 ; 995d: 8d 5d 0d    .].
    lda #&20 ; ' '                                                    ; 9960: a9 20       .
    ora tx_flags                                                      ; 9962: 0d 4a 0d    .J.
    sta tx_flags                                                      ; 9965: 8d 4a 0d    .J.
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
    lda tx_flags                                                      ; 9968: ad 4a 0d    .J.
    bpl ack_tx_configure                                              ; 996b: 10 03       ..
    jmp tx_result_ok                                                  ; 996d: 4c 48 9f    LH.

; &9970 referenced 1 time by &996b
.ack_tx_configure
    lda #&44 ; 'D'                                                    ; 9970: a9 44       .D             ; CR1=&44: RX_RESET | TIE (switch to TX mode)
    sta econet_control1_or_status1                                    ; 9972: 8d a0 fe    ...
    lda #&a7                                                          ; 9975: a9 a7       ..             ; CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9977: 8d a1 fe    ...
    lda #&c5                                                          ; 997a: a9 c5       ..             ; Install saved next handler (&99BB for scout ACK)
    ldy #&99                                                          ; 997c: a0 99       ..
; &997e referenced 2 times by &9834, &9b25
.ack_tx_write_dest
    sta nmi_next_lo                                                   ; 997e: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9981: 8c 4c 0d    .L.
    lda rx_src_stn                                                    ; 9984: ad 3d 0d    .=.            ; Load dest station from RX scout buffer
    bit econet_control1_or_status1                                    ; 9987: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc c99c2                                                         ; 998a: 50 36       P6             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 998c: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda rx_src_net                                                    ; 998f: ad 3e 0d    .>.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9992: 8d a2 fe    ...
    lda #&9c                                                          ; 9995: a9 9c       ..             ; Install handler at &9992 (write src addr)
    ldy #&99                                                          ; 9997: a0 99       ..
    jmp set_nmi_vector                                                ; 9999: 4c 0e 0d    L..

; ***************************************************************************************
; ACK TX continuation
; 
; Writes source station and network to TX FIFO, completing the 4-byte
; ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.
; ***************************************************************************************
.nmi_ack_tx_src
    lda station_id_disable_net_nmis                                   ; 999c: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 999f: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc c99c2                                                         ; 99a2: 50 1e       P.             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 99a4: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 99a7: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 99a9: 8d a2 fe    ...
    lda tx_flags                                                      ; 99ac: ad 4a 0d    .J.
    bmi c99bf                                                         ; 99af: 30 0e       0.
    lda #&3f ; '?'                                                    ; 99b1: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE
    sta econet_control23_or_status2                                   ; 99b3: 8d a1 fe    ...
    lda nmi_next_lo                                                   ; 99b6: ad 4b 0d    .K.            ; Install saved handler from &0D4B/&0D4C
    ldy nmi_next_hi                                                   ; 99b9: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 99bc: 4c 0e 0d    L..

; &99bf referenced 1 time by &99af
.c99bf
    jmp data_tx_begin                                                 ; 99bf: 4c 4a 9e    LJ.

; &99c2 referenced 2 times by &998a, &99a2
.c99c2
    jmp c9894                                                         ; 99c2: 4c 94 98    L..

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
    lda rx_port                                                       ; 99c5: ad 40 0d    .@.
    bne c99d4                                                         ; 99c8: d0 0a       ..
    ldy rx_ctrl                                                       ; 99ca: ac 3f 0d    .?.
    cpy #&82                                                          ; 99cd: c0 82       ..
    beq c99d4                                                         ; 99cf: f0 03       ..
    jmp c9b28                                                         ; 99d1: 4c 28 9b    L(.

; &99d4 referenced 2 times by &99c8, &99cf
.c99d4
    lda #2                                                            ; 99d4: a9 02       ..
    bit tx_flags                                                      ; 99d6: 2c 4a 0d    ,J.
    beq c9a18                                                         ; 99d9: f0 3d       .=
    clc                                                               ; 99db: 18          .
    php                                                               ; 99dc: 08          .
    ldy #8                                                            ; 99dd: a0 08       ..
; &99df referenced 1 time by &99eb
.loop_c99df
    lda (port_ws_offset),y                                            ; 99df: b1 a6       ..
    plp                                                               ; 99e1: 28          (
    adc net_tx_ptr,y                                                  ; 99e2: 79 9a 00    y..
    sta (port_ws_offset),y                                            ; 99e5: 91 a6       ..
    iny                                                               ; 99e7: c8          .
    php                                                               ; 99e8: 08          .
    cpy #&0c                                                          ; 99e9: c0 0c       ..
    bcc loop_c99df                                                    ; 99eb: 90 f2       ..
    plp                                                               ; 99ed: 28          (
    lda #&20 ; ' '                                                    ; 99ee: a9 20       .
    bit tx_flags                                                      ; 99f0: 2c 4a 0d    ,J.
    beq c9a2a                                                         ; 99f3: f0 35       .5
    txa                                                               ; 99f5: 8a          .
    pha                                                               ; 99f6: 48          H
    lda #8                                                            ; 99f7: a9 08       ..
    clc                                                               ; 99f9: 18          .
    adc port_ws_offset                                                ; 99fa: 65 a6       e.
    tax                                                               ; 99fc: aa          .
    ldy rx_buf_offset                                                 ; 99fd: a4 a7       ..
    lda #1                                                            ; 99ff: a9 01       ..
    jsr tube_addr_claim                                               ; 9a01: 20 06 04     ..
    lda rx_extra_byte                                                 ; 9a04: ad 5d 0d    .].
    sta tube_data_register_3                                          ; 9a07: 8d e5 fe    ...
    pla                                                               ; 9a0a: 68          h
    tax                                                               ; 9a0b: aa          .
    ldy #8                                                            ; 9a0c: a0 08       ..
    lda (port_ws_offset),y                                            ; 9a0e: b1 a6       ..
    sec                                                               ; 9a10: 38          8
    adc #0                                                            ; 9a11: 69 00       i.
    sta (port_ws_offset),y                                            ; 9a13: 91 a6       ..
    jmp c9a2a                                                         ; 9a15: 4c 2a 9a    L*.

; &9a18 referenced 1 time by &99d9
.c9a18
    lda port_buf_len                                                  ; 9a18: a5 a2       ..
    clc                                                               ; 9a1a: 18          .
    adc open_port_buf                                                 ; 9a1b: 65 a4       e.
    bcc c9a21                                                         ; 9a1d: 90 02       ..
    inc open_port_buf_hi                                              ; 9a1f: e6 a5       ..
; &9a21 referenced 1 time by &9a1d
.c9a21
    ldy #8                                                            ; 9a21: a0 08       ..
.sub_c9a23
l9a24 = sub_c9a23+1
    sta (port_ws_offset),y                                            ; 9a23: 91 a6       ..
; &9a24 referenced 1 time by &9a9d
    iny                                                               ; 9a25: c8          .              ; Y=&09
    lda open_port_buf_hi                                              ; 9a26: a5 a5       ..
    sta (port_ws_offset),y                                            ; 9a28: 91 a6       ..
; &9a2a referenced 3 times by &99f3, &9a15, &9a6c
.c9a2a
l9a2c = c9a2a+2
    lda rx_port                                                       ; 9a2a: ad 40 0d    .@.
; &9a2c referenced 1 time by &9a99
    beq discard_reset_listen                                          ; 9a2d: f0 1b       ..
    lda rx_src_net                                                    ; 9a2f: ad 3e 0d    .>.
    ldy #3                                                            ; 9a32: a0 03       ..
    sta (port_ws_offset),y                                            ; 9a34: 91 a6       ..
    dey                                                               ; 9a36: 88          .              ; Y=&02
    lda rx_src_stn                                                    ; 9a37: ad 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 9a3a: 91 a6       ..
    dey                                                               ; 9a3c: 88          .              ; Y=&01
    lda rx_port                                                       ; 9a3d: ad 40 0d    .@.
    sta (port_ws_offset),y                                            ; 9a40: 91 a6       ..
    dey                                                               ; 9a42: 88          .              ; Y=&00
    lda rx_ctrl                                                       ; 9a43: ad 3f 0d    .?.
    ora #&80                                                          ; 9a46: 09 80       ..
    sta (port_ws_offset),y                                            ; 9a48: 91 a6       ..
; ***************************************************************************************
; Discard with full ADLC reset
; 
; Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
; then falls through to discard_after_reset. Used when the ADLC is
; in an unexpected state and needs a hard reset before returning
; to idle listen mode. 5 references — the main error recovery path.
; ***************************************************************************************
; &9a4a referenced 4 times by &98a1, &9a2d, &9ea2, &9f57
.discard_reset_listen
    lda #2                                                            ; 9a4a: a9 02       ..
    bit tx_flags                                                      ; 9a4c: 2c 4a 0d    ,J.
    beq discard_listen                                                ; 9a4f: f0 05       ..
    lda #&82                                                          ; 9a51: a9 82       ..
    jsr tube_addr_claim                                               ; 9a53: 20 06 04     ..
; ***************************************************************************************
; Discard frame (gentle)
; 
; Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
; current frame reception without a full reset, then falls through
; to discard_after_reset. Used for clean rejection of frames that
; are correctly formatted but not for us (wrong station/network).
; ***************************************************************************************
; &9a56 referenced 3 times by &974e, &9a4f, &9b5e
.discard_listen
    jsr adlc_rx_listen                                                ; 9a56: 20 f5 96     ..
; &9a59 referenced 2 times by &9732, &974b
.c9a59
    lda #0                                                            ; 9a59: a9 00       ..
    ldy #&97                                                          ; 9a5b: a0 97       ..
    jmp set_nmi_vector                                                ; 9a5d: 4c 0e 0d    L..

; &9a60 referenced 1 time by &9802
.c9a60
    ldy #4                                                            ; 9a60: a0 04       ..
; &9a62 referenced 1 time by &9a6a
.loop_c9a62
    lda rx_src_stn,y                                                  ; 9a62: b9 3d 0d    .=.
    sta (port_ws_offset),y                                            ; 9a65: 91 a6       ..
    iny                                                               ; 9a67: c8          .
    cpy #&0c                                                          ; 9a68: c0 0c       ..
    bne loop_c9a62                                                    ; 9a6a: d0 f6       ..
    jmp c9a2a                                                         ; 9a6c: 4c 2a 9a    L*.

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
; Return to idle listen after reset/discard
; 
; Just calls adlc_rx_listen (CR1=&82, CR2=&67) to re-enter idle
; RX mode, then RTI. The simplest of the three discard paths —
; used as the tail of both discard_reset_listen and discard_listen.
; ***************************************************************************************
; &9a6f referenced 1 time by &979e
.immediate_op
.discard_after_reset
    ldy rx_ctrl                                                       ; 9a6f: ac 3f 0d    .?.
    cpy #&81                                                          ; 9a72: c0 81       ..
    bcc c9aa2                                                         ; 9a74: 90 2c       .,
    cpy #&89                                                          ; 9a76: c0 89       ..
    bcs c9aa2                                                         ; 9a78: b0 28       .(
    cpy #&87                                                          ; 9a7a: c0 87       ..
    bcs c9a96                                                         ; 9a7c: b0 18       ..
    lda rx_src_stn                                                    ; 9a7e: ad 3d 0d    .=.
    cmp #&f0                                                          ; 9a81: c9 f0       ..
    bcs c9a96                                                         ; 9a83: b0 11       ..
    tya                                                               ; 9a85: 98          .
    sec                                                               ; 9a86: 38          8
    sbc #&81                                                          ; 9a87: e9 81       ..
    tay                                                               ; 9a89: a8          .
    lda prot_status                                                   ; 9a8a: ad 63 0d    .c.
; &9a8d referenced 1 time by &9a8f
.loop_c9a8d
    ror a                                                             ; 9a8d: 6a          j
    dey                                                               ; 9a8e: 88          .
    bpl loop_c9a8d                                                    ; 9a8f: 10 fc       ..
    bcc c9a96                                                         ; 9a91: 90 03       ..
    jmp c9b5e                                                         ; 9a93: 4c 5e 9b    L^.

; &9a96 referenced 3 times by &9a7c, &9a83, &9a91
.c9a96
    ldy rx_ctrl                                                       ; 9a96: ac 3f 0d    .?.
    lda l9a2c,y                                                       ; 9a99: b9 2c 9a    .,.
    pha                                                               ; 9a9c: 48          H
    lda l9a24,y                                                       ; 9a9d: b9 24 9a    .$.
    pha                                                               ; 9aa0: 48          H
    rts                                                               ; 9aa1: 60          `

; &9aa2 referenced 2 times by &9a74, &9a78
.c9aa2
    jmp c9894                                                         ; 9aa2: 4c 94 98    L..

    equb <(rx_imm_peek-1)                                             ; 9aa5: f0          .
    equb <(rx_imm_poke-1)                                             ; 9aa6: d2          .
    equb <(rx_imm_exec-1)                                             ; 9aa7: b4          .
    equb <(rx_imm_exec-1)                                             ; 9aa8: b4          .
    equb <(rx_imm_exec-1)                                             ; 9aa9: b4          .
    equb <(sub_c9b17-1)                                               ; 9aaa: 16          .
    equb <(sub_c9b17-1)                                               ; 9aab: 16          .
    equb <(rx_imm_machine_type-1)                                     ; 9aac: dd          .
    equb >(rx_imm_peek-1)                                             ; 9aad: 9a          .
    equb >(rx_imm_poke-1)                                             ; 9aae: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9aaf: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9ab0: 9a          .
    equb >(rx_imm_exec-1)                                             ; 9ab1: 9a          .
    equb >(sub_c9b17-1)                                               ; 9ab2: 9b          .
    equb >(sub_c9b17-1)                                               ; 9ab3: 9b          .
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
    lda #0                                                            ; 9ab5: a9 00       ..
    sta open_port_buf                                                 ; 9ab7: 85 a4       ..
    lda #&82                                                          ; 9ab9: a9 82       ..
    sta port_buf_len                                                  ; 9abb: 85 a2       ..
    lda #1                                                            ; 9abd: a9 01       ..
    sta port_buf_len_hi                                               ; 9abf: 85 a3       ..
    lda net_rx_ptr_hi                                                 ; 9ac1: a5 9d       ..
    sta open_port_buf_hi                                              ; 9ac3: 85 a5       ..
    ldy #3                                                            ; 9ac5: a0 03       ..
; &9ac7 referenced 1 time by &9ace
.loop_c9ac7
    lda rx_remote_addr,y                                              ; 9ac7: b9 41 0d    .A.
    sta l0d58,y                                                       ; 9aca: 99 58 0d    .X.
    dey                                                               ; 9acd: 88          .
    bpl loop_c9ac7                                                    ; 9ace: 10 f7       ..
    jmp c9826                                                         ; 9ad0: 4c 26 98    L&.

; ***************************************************************************************
; RX immediate: POKE setup
; 
; Sets up workspace offsets for receiving POKE data.
; port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
; the common data-receive path at c9805.
; ***************************************************************************************
.rx_imm_poke
    lda #&3d ; '='                                                    ; 9ad3: a9 3d       .=
    sta port_ws_offset                                                ; 9ad5: 85 a6       ..
    lda #&0d                                                          ; 9ad7: a9 0d       ..
    sta rx_buf_offset                                                 ; 9ad9: 85 a7       ..
    jmp c9805                                                         ; 9adb: 4c 05 98    L..

; ***************************************************************************************
; RX immediate: machine type query
; 
; Sets up a buffer at &7F21 (length #&01FC) for the machine
; type query response, then jumps to the query handler at
; c9b0f. Returns system identification data to the remote
; station.
; ***************************************************************************************
.rx_imm_machine_type
    lda #1                                                            ; 9ade: a9 01       ..
    sta port_buf_len_hi                                               ; 9ae0: 85 a3       ..
    lda #&fc                                                          ; 9ae2: a9 fc       ..
    sta port_buf_len                                                  ; 9ae4: 85 a2       ..
    lda #&21 ; '!'                                                    ; 9ae6: a9 21       .!
    sta open_port_buf                                                 ; 9ae8: 85 a4       ..
    lda #&7f                                                          ; 9aea: a9 7f       ..
    sta open_port_buf_hi                                              ; 9aec: 85 a5       ..
    jmp c9b0f                                                         ; 9aee: 4c 0f 9b    L..

; ***************************************************************************************
; RX immediate: PEEK setup
; 
; Saves the current TX block pointer, replaces it with a
; pointer to &0D3D, and prepares to send the PEEK response
; data back to the requesting station.
; ***************************************************************************************
.rx_imm_peek
    lda nmi_tx_block                                                  ; 9af1: a5 a0       ..
    pha                                                               ; 9af3: 48          H
    lda nmi_tx_block_hi                                               ; 9af4: a5 a1       ..
    pha                                                               ; 9af6: 48          H
    lda #&3d ; '='                                                    ; 9af7: a9 3d       .=
    sta nmi_tx_block                                                  ; 9af9: 85 a0       ..
    lda #&0d                                                          ; 9afb: a9 0d       ..
    sta nmi_tx_block_hi                                               ; 9afd: 85 a1       ..
    lda #2                                                            ; 9aff: a9 02       ..
    sta scout_status                                                  ; 9b01: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 9b04: 20 6a 9f     j.
    pla                                                               ; 9b07: 68          h
    sta nmi_tx_block_hi                                               ; 9b08: 85 a1       ..
    pla                                                               ; 9b0a: 68          h
    sta nmi_tx_block                                                  ; 9b0b: 85 a0       ..
    bcc c9b5e                                                         ; 9b0d: 90 4f       .O
; &9b0f referenced 1 time by &9aee
.c9b0f
    lda tx_flags                                                      ; 9b0f: ad 4a 0d    .J.
    ora #&80                                                          ; 9b12: 09 80       ..
    sta tx_flags                                                      ; 9b14: 8d 4a 0d    .J.
.sub_c9b17
    lda #&44 ; 'D'                                                    ; 9b17: a9 44       .D
    sta econet_control1_or_status1                                    ; 9b19: 8d a0 fe    ...
.sub_c9b1c
l9b1d = sub_c9b1c+1
    lda #&a7                                                          ; 9b1c: a9 a7       ..
; &9b1d referenced 1 time by &9b9b
    sta econet_control23_or_status2                                   ; 9b1e: 8d a1 fe    ...
.sub_c9b21
l9b22 = sub_c9b21+1
    lda #&3e ; '>'                                                    ; 9b21: a9 3e       .>
; &9b22 referenced 1 time by &9b97
    ldy #&9b                                                          ; 9b23: a0 9b       ..
    jmp ack_tx_write_dest                                             ; 9b25: 4c 7e 99    L~.

; &9b28 referenced 1 time by &99d1
.c9b28
    lda port_buf_len                                                  ; 9b28: a5 a2       ..
    clc                                                               ; 9b2a: 18          .
    adc #&80                                                          ; 9b2b: 69 80       i.
    ldy #&7f                                                          ; 9b2d: a0 7f       ..
    sta (net_rx_ptr),y                                                ; 9b2f: 91 9c       ..
    ldy #&80                                                          ; 9b31: a0 80       ..
    lda rx_src_stn                                                    ; 9b33: ad 3d 0d    .=.
    sta (net_rx_ptr),y                                                ; 9b36: 91 9c       ..
    iny                                                               ; 9b38: c8          .              ; Y=&81
    lda rx_src_net                                                    ; 9b39: ad 3e 0d    .>.
    sta (net_rx_ptr),y                                                ; 9b3c: 91 9c       ..
    lda rx_ctrl                                                       ; 9b3e: ad 3f 0d    .?.
    sta tx_work_57                                                    ; 9b41: 8d 57 0d    .W.
    lda #&84                                                          ; 9b44: a9 84       ..
    sta system_via_ier                                                ; 9b46: 8d 4e fe    .N.
    lda system_via_acr                                                ; 9b49: ad 4b fe    .K.
    and #&1c                                                          ; 9b4c: 29 1c       ).
    sta tx_work_51                                                    ; 9b4e: 8d 51 0d    .Q.
    lda system_via_acr                                                ; 9b51: ad 4b fe    .K.
    and #&e3                                                          ; 9b54: 29 e3       ).
    ora #8                                                            ; 9b56: 09 08       ..
    sta system_via_acr                                                ; 9b58: 8d 4b fe    .K.
    bit system_via_sr                                                 ; 9b5b: 2c 4a fe    ,J.
; &9b5e referenced 2 times by &9a93, &9b0d
.c9b5e
    jmp discard_listen                                                ; 9b5e: 4c 56 9a    LV.

; &9b61 referenced 1 time by &966c
.c9b61
    lda #4                                                            ; 9b61: a9 04       ..
    bit system_via_ifr                                                ; 9b63: 2c 4d fe    ,M.
    bne c9b6b                                                         ; 9b66: d0 03       ..
    lda #5                                                            ; 9b68: a9 05       ..
    rts                                                               ; 9b6a: 60          `

; &9b6b referenced 1 time by &9b66
.c9b6b
    txa                                                               ; 9b6b: 8a          .
    pha                                                               ; 9b6c: 48          H
    tya                                                               ; 9b6d: 98          .
    pha                                                               ; 9b6e: 48          H
    lda system_via_acr                                                ; 9b6f: ad 4b fe    .K.
    and #&e3                                                          ; 9b72: 29 e3       ).
    ora tx_work_51                                                    ; 9b74: 0d 51 0d    .Q.
    sta system_via_acr                                                ; 9b77: 8d 4b fe    .K.
    lda system_via_sr                                                 ; 9b7a: ad 4a fe    .J.
    lda #4                                                            ; 9b7d: a9 04       ..
    sta system_via_ifr                                                ; 9b7f: 8d 4d fe    .M.
    sta system_via_ier                                                ; 9b82: 8d 4e fe    .N.
    ldy tx_work_57                                                    ; 9b85: ac 57 0d    .W.
    cpy #&86                                                          ; 9b88: c0 86       ..
    bcs c9b97                                                         ; 9b8a: b0 0b       ..
    lda prot_status                                                   ; 9b8c: ad 63 0d    .c.
    sta saved_jsr_mask                                                ; 9b8f: 8d 65 0d    .e.
    ora #&1c                                                          ; 9b92: 09 1c       ..
    sta prot_status                                                   ; 9b94: 8d 63 0d    .c.
; &9b97 referenced 1 time by &9b8a
.c9b97
    lda l9b22,y                                                       ; 9b97: b9 22 9b    .".
    pha                                                               ; 9b9a: 48          H
    lda l9b1d,y                                                       ; 9b9b: b9 1d 9b    ...
    pha                                                               ; 9b9e: 48          H
    rts                                                               ; 9b9f: 60          `

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
    lda #&9b                                                          ; 9baa: a9 9b       ..
    pha                                                               ; 9bac: 48          H
    lda #&eb                                                          ; 9bad: a9 eb       ..
    pha                                                               ; 9baf: 48          H
    jmp (l0d58)                                                       ; 9bb0: 6c 58 0d    lX.

; ***************************************************************************************
; TX done: UserProc event
; 
; Generates a network event (event 8) via OSEVEN with
; X=l0d58, A=l0d59 (the remote address). This notifies
; the user program that a UserProc operation has completed.
; ***************************************************************************************
.tx_done_user_proc
    ldy #event_network_error                                          ; 9bb3: a0 08       ..
    ldx l0d58                                                         ; 9bb5: ae 58 0d    .X.
    lda l0d59                                                         ; 9bb8: ad 59 0d    .Y.
    jsr oseven                                                        ; 9bbb: 20 bf ff     ..            ; Generate event Y='Network error'
    jmp tx_done_exit                                                  ; 9bbe: 4c ec 9b    L..

; ***************************************************************************************
; TX done: OSProc call
; 
; Calls the ROM entry point at &8000 (rom_header) with
; X=l0d58, Y=l0d59. This invokes an OS-level procedure
; on behalf of the remote station.
; ***************************************************************************************
.tx_done_os_proc
    ldx l0d58                                                         ; 9bc1: ae 58 0d    .X.
    ldy l0d59                                                         ; 9bc4: ac 59 0d    .Y.
    jsr rom_header                                                    ; 9bc7: 20 00 80     ..
    jmp tx_done_exit                                                  ; 9bca: 4c ec 9b    L..

; ***************************************************************************************
; TX done: HALT
; 
; Sets bit 2 of rx_flags (&0D64), enables interrupts, and
; spin-waits until bit 2 is cleared (by a CONTINUE from the
; remote station). If bit 2 is already set, skips to exit.
; ***************************************************************************************
.tx_done_halt
    lda #4                                                            ; 9bcd: a9 04       ..
    bit rx_flags                                                      ; 9bcf: 2c 64 0d    ,d.
    bne tx_done_exit                                                  ; 9bd2: d0 18       ..
    ora rx_flags                                                      ; 9bd4: 0d 64 0d    .d.
    sta rx_flags                                                      ; 9bd7: 8d 64 0d    .d.
    lda #4                                                            ; 9bda: a9 04       ..
    cli                                                               ; 9bdc: 58          X
; &9bdd referenced 1 time by &9be0
.loop_c9bdd
    bit rx_flags                                                      ; 9bdd: 2c 64 0d    ,d.
    bne loop_c9bdd                                                    ; 9be0: d0 fb       ..
    beq tx_done_exit                                                  ; 9be2: f0 08       ..             ; ALWAYS branch

; ***************************************************************************************
; TX done: CONTINUE
; 
; Clears bit 2 of rx_flags (&0D64), releasing any station
; that is halted and spinning in tx_done_halt.
; ***************************************************************************************
.tx_done_continue
    lda rx_flags                                                      ; 9be4: ad 64 0d    .d.
    and #&fb                                                          ; 9be7: 29 fb       ).
    sta rx_flags                                                      ; 9be9: 8d 64 0d    .d.
; &9bec referenced 4 times by &9bbe, &9bca, &9bd2, &9be2
.tx_done_exit
    pla                                                               ; 9bec: 68          h
    tay                                                               ; 9bed: a8          .
    pla                                                               ; 9bee: 68          h
    tax                                                               ; 9bef: aa          .
    lda #0                                                            ; 9bf0: a9 00       ..
    rts                                                               ; 9bf2: 60          `

; &9bf3 referenced 1 time by &9660
.c9bf3
    txa                                                               ; 9bf3: 8a          .
    pha                                                               ; 9bf4: 48          H
    ldy #2                                                            ; 9bf5: a0 02       ..
    lda (nmi_tx_block),y                                              ; 9bf7: b1 a0       ..
    sta tx_dst_stn                                                    ; 9bf9: 8d 20 0d    . .
    iny                                                               ; 9bfc: c8          .              ; Y=&03
    lda (nmi_tx_block),y                                              ; 9bfd: b1 a0       ..
    sta tx_dst_net                                                    ; 9bff: 8d 21 0d    .!.
    ldy #0                                                            ; 9c02: a0 00       ..
    lda (nmi_tx_block),y                                              ; 9c04: b1 a0       ..
    bmi c9c0b                                                         ; 9c06: 30 03       0.
    jmp tx_active_start                                               ; 9c08: 4c 93 9c    L..

; &9c0b referenced 1 time by &9c06
.c9c0b
    sta tx_ctrl_byte                                                  ; 9c0b: 8d 24 0d    .$.
    tax                                                               ; 9c0e: aa          .
    iny                                                               ; 9c0f: c8          .
    lda (nmi_tx_block),y                                              ; 9c10: b1 a0       ..
    sta tx_port                                                       ; 9c12: 8d 25 0d    .%.
    bne c9c46                                                         ; 9c15: d0 2f       ./
    cpx #&83                                                          ; 9c17: e0 83       ..
    bcs c9c36                                                         ; 9c19: b0 1b       ..
    sec                                                               ; 9c1b: 38          8
    php                                                               ; 9c1c: 08          .
    ldy #8                                                            ; 9c1d: a0 08       ..
; &9c1f referenced 1 time by &9c33
.loop_c9c1f
    lda (nmi_tx_block),y                                              ; 9c1f: b1 a0       ..
    dey                                                               ; 9c21: 88          .
    dey                                                               ; 9c22: 88          .
    dey                                                               ; 9c23: 88          .
    dey                                                               ; 9c24: 88          .
    plp                                                               ; 9c25: 28          (
    sbc (nmi_tx_block),y                                              ; 9c26: f1 a0       ..
    sta tx_data_start,y                                               ; 9c28: 99 26 0d    .&.
    iny                                                               ; 9c2b: c8          .
    iny                                                               ; 9c2c: c8          .
    iny                                                               ; 9c2d: c8          .
    iny                                                               ; 9c2e: c8          .
    iny                                                               ; 9c2f: c8          .
    php                                                               ; 9c30: 08          .
    cpy #&0c                                                          ; 9c31: c0 0c       ..
    bcc loop_c9c1f                                                    ; 9c33: 90 ea       ..
    plp                                                               ; 9c35: 28          (
; &9c36 referenced 1 time by &9c19
.c9c36
    cpx #&89                                                          ; 9c36: e0 89       ..
    bcs tx_active_start                                               ; 9c38: b0 59       .Y
    ldy #&0c                                                          ; 9c3a: a0 0c       ..
; &9c3c referenced 1 time by &9c44
.loop_c9c3c
    lda (nmi_tx_block),y                                              ; 9c3c: b1 a0       ..
    sta nmi_shim_1a,y                                                 ; 9c3e: 99 1a 0d    ...
    iny                                                               ; 9c41: c8          .
    cpy #&10                                                          ; 9c42: c0 10       ..
    bcc loop_c9c3c                                                    ; 9c44: 90 f6       ..
; &9c46 referenced 1 time by &9c15
.c9c46
    lda #&20 ; ' '                                                    ; 9c46: a9 20       .
    bit econet_control23_or_status2                                   ; 9c48: 2c a1 fe    ,..
    bne c9ca3                                                         ; 9c4b: d0 56       .V
    lda #&fd                                                          ; 9c4d: a9 fd       ..
    pha                                                               ; 9c4f: 48          H
    lda #6                                                            ; 9c50: a9 06       ..
    sta tx_length                                                     ; 9c52: 8d 50 0d    .P.
    lda #0                                                            ; 9c55: a9 00       ..
; ***************************************************************************************
; INACTIVE polling loop
; 
; Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
; attempting transmission. Uses a 3-byte timeout counter on the stack.
; The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
; never appears.
; The CTS check at &9C66-&9C6B works because CR2=&67 has RTS=0, so
; cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.
; ***************************************************************************************
.inactive_poll
    sta tx_index                                                      ; 9c57: 8d 4f 0d    .O.
    pha                                                               ; 9c5a: 48          H
    pha                                                               ; 9c5b: 48          H
    ldy #&e7                                                          ; 9c5c: a0 e7       ..             ; Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
; &9c5e referenced 3 times by &9c84, &9c89, &9c8e
.c9c5e
    lda #4                                                            ; 9c5e: a9 04       ..             ; A=&04: INACTIVE mask for SR2 bit2
    php                                                               ; 9c60: 08          .
    sei                                                               ; 9c61: 78          x
; &9c62 referenced 1 time by &9cde
.c9c62
    bit station_id_disable_net_nmis                                   ; 9c62: 2c 18 fe    ,..            ; INTOFF -- disable NMIs
    bit station_id_disable_net_nmis                                   ; 9c65: 2c 18 fe    ,..            ; INTOFF again (belt-and-braces)
.sub_c9c68
l9c6a = sub_c9c68+2
    bit econet_control23_or_status2                                   ; 9c68: 2c a1 fe    ,..            ; BIT SR2: Z = &04 AND SR2 -- tests INACTIVE
; &9c6a referenced 1 time by &9cda
    beq c9c7c                                                         ; 9c6b: f0 0f       ..             ; INACTIVE not set -- re-enable NMIs and loop
    lda econet_control1_or_status1                                    ; 9c6d: ad a0 fe    ...            ; Read SR1 (acknowledge pending interrupt)
    lda #&67 ; 'g'                                                    ; 9c70: a9 67       .g             ; CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE
    sta econet_control23_or_status2                                   ; 9c72: 8d a1 fe    ...
    lda #&10                                                          ; 9c75: a9 10       ..             ; A=&10: CTS mask for SR1 bit4
    bit econet_control1_or_status1                                    ; 9c77: 2c a0 fe    ,..            ; BIT SR1: tests CTS present
    bne tx_prepare                                                    ; 9c7a: d0 35       .5             ; CTS set -- clock hardware detected, start TX
; &9c7c referenced 1 time by &9c6b
.c9c7c
    bit video_ula_control                                             ; 9c7c: 2c 20 fe    , .            ; INTON -- re-enable NMIs (&FE20 read)
    plp                                                               ; 9c7f: 28          (
    tsx                                                               ; 9c80: ba          .              ; 3-byte timeout counter on stack
    inc l0101,x                                                       ; 9c81: fe 01 01    ...
    bne c9c5e                                                         ; 9c84: d0 d8       ..
    inc l0102,x                                                       ; 9c86: fe 02 01    ...
    bne c9c5e                                                         ; 9c89: d0 d3       ..
    inc l0103,x                                                       ; 9c8b: fe 03 01    ...
    bne c9c5e                                                         ; 9c8e: d0 ce       ..
    jmp tx_line_jammed                                                ; 9c90: 4c 97 9c    L..

; TX_ACTIVE branch (A=&44 = CR1 value for TX active)
; &9c93 referenced 2 times by &9c08, &9c38
.tx_active_start
    lda #&44 ; 'D'                                                    ; 9c93: a9 44       .D
    bne c9ca5                                                         ; 9c95: d0 0e       ..             ; ALWAYS branch

; ***************************************************************************************
; Timeout error: writes CR2=&07 to abort, cleans stack,
; 
; returns error &40 ("Line Jammed").
; ***************************************************************************************
; &9c97 referenced 1 time by &9c90
.tx_line_jammed
    lda #7                                                            ; 9c97: a9 07       ..             ; CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)
    sta econet_control23_or_status2                                   ; 9c99: 8d a1 fe    ...
    pla                                                               ; 9c9c: 68          h
    pla                                                               ; 9c9d: 68          h
    pla                                                               ; 9c9e: 68          h
    lda #&40 ; '@'                                                    ; 9c9f: a9 40       .@             ; Error &40 = 'Line Jammed'
    bne c9ca5                                                         ; 9ca1: d0 02       ..             ; ALWAYS branch

; &9ca3 referenced 1 time by &9c4b
.c9ca3
    lda #&43 ; 'C'                                                    ; 9ca3: a9 43       .C
; &9ca5 referenced 2 times by &9c95, &9ca1
.c9ca5
    ldy #0                                                            ; 9ca5: a0 00       ..
    sta (nmi_tx_block),y                                              ; 9ca7: 91 a0       ..
    lda #&80                                                          ; 9ca9: a9 80       ..
    sta tx_clear_flag                                                 ; 9cab: 8d 62 0d    .b.
    pla                                                               ; 9cae: 68          h
    tax                                                               ; 9caf: aa          .
    rts                                                               ; 9cb0: 60          `

; ***************************************************************************************
; TX preparation
; 
; Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
; installs NMI TX handler at &9D5B, and re-enables NMIs.
; ***************************************************************************************
; &9cb1 referenced 1 time by &9c7a
.tx_prepare
    sty econet_control23_or_status2                                   ; 9cb1: 8c a1 fe    ...            ; Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
    ldx #&44 ; 'D'                                                    ; 9cb4: a2 44       .D             ; CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)
    stx econet_control1_or_status1                                    ; 9cb6: 8e a0 fe    ...
    ldx #&5b ; '['                                                    ; 9cb9: a2 5b       .[             ; Install NMI handler at &9D4C (TX data handler)
    ldy #&9d                                                          ; 9cbb: a0 9d       ..
    stx nmi_jmp_lo                                                    ; 9cbd: 8e 0c 0d    ...
    sty nmi_jmp_hi                                                    ; 9cc0: 8c 0d 0d    ...
    bit video_ula_control                                             ; 9cc3: 2c 20 fe    , .            ; INTON -- NMIs now fire for TDRA (&FE20 read)
    lda tx_port                                                       ; 9cc6: ad 25 0d    .%.
    bne c9d25                                                         ; 9cc9: d0 5a       .Z
    ldy tx_ctrl_byte                                                  ; 9ccb: ac 24 0d    .$.
    lda l9ee1,y                                                       ; 9cce: b9 e1 9e    ...
    sta tx_flags                                                      ; 9cd1: 8d 4a 0d    .J.
    lda l9ed9,y                                                       ; 9cd4: b9 d9 9e    ...
    sta tx_length                                                     ; 9cd7: 8d 50 0d    .P.
    lda l9c6a,y                                                       ; 9cda: b9 6a 9c    .j.
    pha                                                               ; 9cdd: 48          H
    lda c9c62,y                                                       ; 9cde: b9 62 9c    .b.
    pha                                                               ; 9ce1: 48          H
    rts                                                               ; 9ce2: 60          `

    equb <(tx_ctrl_peek-1)                                            ; 9ce3: f6          .
    equb <(tx_ctrl_poke-1)                                            ; 9ce4: fa          .
    equb <(tx_ctrl_proc-1)                                            ; 9ce5: 19          .
    equb <(tx_ctrl_proc-1)                                            ; 9ce6: 19          .
    equb <(tx_ctrl_proc-1)                                            ; 9ce7: 19          .
    equb <(tx_ctrl_exit-1)                                            ; 9ce8: 53          S
    equb <(tx_ctrl_exit-1)                                            ; 9ce9: 53          S
    equb <(sub_c9cf3-1)                                               ; 9cea: f2          .
    equb >(tx_ctrl_peek-1)                                            ; 9ceb: 9c          .
    equb >(tx_ctrl_poke-1)                                            ; 9cec: 9c          .
    equb >(tx_ctrl_proc-1)                                            ; 9ced: 9d          .
    equb >(tx_ctrl_proc-1)                                            ; 9cee: 9d          .
    equb >(tx_ctrl_proc-1)                                            ; 9cef: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cf0: 9d          .
    equb >(tx_ctrl_exit-1)                                            ; 9cf1: 9d          .
    equb >(sub_c9cf3-1)                                               ; 9cf2: 9c          .

.sub_c9cf3
    lda #3                                                            ; 9cf3: a9 03       ..
    bne c9d1c                                                         ; 9cf5: d0 25       .%             ; ALWAYS branch

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
    lda #3                                                            ; 9cf7: a9 03       ..
    bne c9cfd                                                         ; 9cf9: d0 02       ..             ; ALWAYS branch

; ***************************************************************************************
; TX ctrl: POKE transfer setup
; 
; Sets scout_status=2 and shares the 4-byte addition and
; transfer calculation path with tx_ctrl_peek.
; ***************************************************************************************
.tx_ctrl_poke
    lda #2                                                            ; 9cfb: a9 02       ..
; &9cfd referenced 1 time by &9cf9
.c9cfd
    sta scout_status                                                  ; 9cfd: 8d 5c 0d    .\.
    clc                                                               ; 9d00: 18          .
    php                                                               ; 9d01: 08          .
    ldy #&0c                                                          ; 9d02: a0 0c       ..
; &9d04 referenced 1 time by &9d11
.loop_c9d04
    lda l0d1e,y                                                       ; 9d04: b9 1e 0d    ...
    plp                                                               ; 9d07: 28          (
    adc (nmi_tx_block),y                                              ; 9d08: 71 a0       q.
    sta l0d1e,y                                                       ; 9d0a: 99 1e 0d    ...
    iny                                                               ; 9d0d: c8          .
    php                                                               ; 9d0e: 08          .
    cpy #&10                                                          ; 9d0f: c0 10       ..
    bcc loop_c9d04                                                    ; 9d11: 90 f1       ..
    plp                                                               ; 9d13: 28          (
    jsr tx_calc_transfer                                              ; 9d14: 20 6a 9f     j.
    jmp tx_ctrl_exit                                                  ; 9d17: 4c 54 9d    LT.

; ***************************************************************************************
; TX ctrl: JSR/UserProc/OSProc setup
; 
; Sets scout_status=2 and calls tx_calc_transfer directly
; (no 4-byte address addition needed for procedure calls).
; Shared by operation types &83-&85.
; ***************************************************************************************
.tx_ctrl_proc
    lda #2                                                            ; 9d1a: a9 02       ..
; &9d1c referenced 1 time by &9cf5
.c9d1c
    sta scout_status                                                  ; 9d1c: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 9d1f: 20 6a 9f     j.
    jmp tx_ctrl_exit                                                  ; 9d22: 4c 54 9d    LT.

; &9d25 referenced 1 time by &9cc9
.c9d25
    lda tx_dst_stn                                                    ; 9d25: ad 20 0d    . .
    and tx_dst_net                                                    ; 9d28: 2d 21 0d    -!.
    cmp #&ff                                                          ; 9d2b: c9 ff       ..
    bne c9d47                                                         ; 9d2d: d0 18       ..
    lda #&0e                                                          ; 9d2f: a9 0e       ..
    sta tx_length                                                     ; 9d31: 8d 50 0d    .P.
    lda #&40 ; '@'                                                    ; 9d34: a9 40       .@
    sta tx_flags                                                      ; 9d36: 8d 4a 0d    .J.
    ldy #4                                                            ; 9d39: a0 04       ..
; &9d3b referenced 1 time by &9d43
.loop_c9d3b
    lda (nmi_tx_block),y                                              ; 9d3b: b1 a0       ..
    sta tx_src_stn,y                                                  ; 9d3d: 99 22 0d    .".
    iny                                                               ; 9d40: c8          .
    cpy #&0c                                                          ; 9d41: c0 0c       ..
    bcc loop_c9d3b                                                    ; 9d43: 90 f6       ..
    bcs tx_ctrl_exit                                                  ; 9d45: b0 0d       ..             ; ALWAYS branch

; &9d47 referenced 1 time by &9d2d
.c9d47
    lda #0                                                            ; 9d47: a9 00       ..
    sta tx_flags                                                      ; 9d49: 8d 4a 0d    .J.
    lda #2                                                            ; 9d4c: a9 02       ..
    sta scout_status                                                  ; 9d4e: 8d 5c 0d    .\.
    jsr tx_calc_transfer                                              ; 9d51: 20 6a 9f     j.
; &9d54 referenced 3 times by &9d17, &9d22, &9d45
.tx_ctrl_exit
    plp                                                               ; 9d54: 28          (
    pla                                                               ; 9d55: 68          h
    pla                                                               ; 9d56: 68          h
    pla                                                               ; 9d57: 68          h
    pla                                                               ; 9d58: 68          h
    tax                                                               ; 9d59: aa          .
    rts                                                               ; 9d5a: 60          `

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
.loop_c9d61
    bvc c9d85                                                         ; 9d61: 50 22       P"             ; TDRA not set -- TX error
    lda tx_dst_stn,y                                                  ; 9d63: b9 20 0d    . .            ; Load byte from TX buffer
    sta econet_data_continue_frame                                    ; 9d66: 8d a2 fe    ...            ; Write to TX_DATA (continue frame)
    iny                                                               ; 9d69: c8          .
    lda tx_dst_stn,y                                                  ; 9d6a: b9 20 0d    . .
    iny                                                               ; 9d6d: c8          .
    sty tx_index                                                      ; 9d6e: 8c 4f 0d    .O.
    sta econet_data_continue_frame                                    ; 9d71: 8d a2 fe    ...            ; Write second byte to TX_DATA
    cpy tx_length                                                     ; 9d74: cc 50 0d    .P.            ; Compare index to TX length
    bcs tx_last_data                                                  ; 9d77: b0 1e       ..             ; Frame complete -- go to TX_LAST_DATA
    bit econet_control1_or_status1                                    ; 9d79: 2c a0 fe    ,..            ; Check if we can send another pair
    bmi loop_c9d61                                                    ; 9d7c: 30 e3       0.             ; IRQ set -- send 2 more bytes (tight loop)
    jmp nmi_rti                                                       ; 9d7e: 4c 14 0d    L..            ; RTI -- wait for next NMI

; TX error path
; &9d81 referenced 1 time by &9dc6
.tx_error
    lda #&42 ; 'B'                                                    ; 9d81: a9 42       .B             ; Error &42
    bne c9d8c                                                         ; 9d83: d0 07       ..             ; ALWAYS branch

; &9d85 referenced 1 time by &9d61
.c9d85
    lda #&67 ; 'g'                                                    ; 9d85: a9 67       .g             ; CR2=&67: clear status, return to listen
    sta econet_control23_or_status2                                   ; 9d87: 8d a1 fe    ...
    lda #&41 ; 'A'                                                    ; 9d8a: a9 41       .A             ; Error &41 (TDRA not ready)
; &9d8c referenced 1 time by &9d83
.c9d8c
    ldy station_id_disable_net_nmis                                   ; 9d8c: ac 18 fe    ...            ; INTOFF (also loads station ID)
; &9d8f referenced 1 time by &9d92
.loop_c9d8f
    pha                                                               ; 9d8f: 48          H              ; PHA/PLA delay loop (256 iterations for NMI disable)
    pla                                                               ; 9d90: 68          h
    iny                                                               ; 9d91: c8          .
    bne loop_c9d8f                                                    ; 9d92: d0 fb       ..
    jmp tx_store_result                                               ; 9d94: 4c 4e 9f    LN.

; ***************************************************************************************
; TX_LAST_DATA and frame completion
; 
; Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
; the TX completion NMI handler at &9DA3 which switches to RX mode.
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
    sta econet_control23_or_status2                                   ; 9d99: 8d a1 fe    ...
    lda #&a3                                                          ; 9d9c: a9 a3       ..             ; Install NMI handler at &9D94 (TX completion)
    ldy #&9d                                                          ; 9d9e: a0 9d       ..
    jmp set_nmi_vector                                                ; 9da0: 4c 0e 0d    L..

; ***************************************************************************************
; TX completion: switch to RX mode
; 
; Called via NMI after the frame (including CRC and closing flag) has been
; fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
; CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
; Checks workspace flags to decide next action:
;   - bit6 set at &0D4A -> completion at &9F48
;   - bit0 set at &0D4A -> four-way handshake data phase at &9EEC
;   - Otherwise -> install RX reply handler at &9DC1
; ***************************************************************************************
.nmi_tx_complete
    lda #&82                                                          ; 9da3: a9 82       ..             ; Jump to error handler; CR1=&82: TX_RESET | RIE (now in RX mode)
    sta econet_control1_or_status1                                    ; 9da5: 8d a0 fe    ...
    bit tx_flags                                                      ; 9da8: 2c 4a 0d    ,J.            ; Test workspace flags
    bvc c9db0                                                         ; 9dab: 50 03       P.             ; bit6 not set -- check bit0
    jmp tx_result_ok                                                  ; 9dad: 4c 48 9f    LH.            ; bit6 set -- TX completion

; &9db0 referenced 1 time by &9dab
.c9db0
    lda #1                                                            ; 9db0: a9 01       ..
    bit tx_flags                                                      ; 9db2: 2c 4a 0d    ,J.
    beq c9dba                                                         ; 9db5: f0 03       ..
    jmp handshake_await_ack                                           ; 9db7: 4c ec 9e    L..            ; bit0 set -- four-way handshake data phase

; &9dba referenced 1 time by &9db5
.c9dba
    lda #&c1                                                          ; 9dba: a9 c1       ..             ; Install RX reply handler at &9DB2
    ldy #&9d                                                          ; 9dbc: a0 9d       ..
    jmp set_nmi_vector                                                ; 9dbe: 4c 0e 0d    L..

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
    lda econet_data_continue_frame                                    ; 9dc8: ad a2 fe    ...
    cmp station_id_disable_net_nmis                                   ; 9dcb: cd 18 fe    ...            ; Compare to our station ID (INTOFF side effect)
    bne reply_error                                                   ; 9dce: d0 1d       ..             ; Not our station -- error/reject
    lda #&d7                                                          ; 9dd0: a9 d7       ..             ; Install next handler at &9DC8 (reply continuation)
    ldy #&9d                                                          ; 9dd2: a0 9d       ..
    jmp set_nmi_vector                                                ; 9dd4: 4c 0e 0d    L..

; ***************************************************************************************
; RX reply continuation handler
; 
; Reads the second byte of the reply scout (destination network) and
; validates it is zero (local network). Installs &9DF2 for the
; remaining two bytes (source station and network).
; Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DD9.
; If IRQ is still set, falls through directly to &9DF2 without an RTI,
; avoiding NMI re-entry overhead for short frames where all bytes arrive
; in quick succession.
; ***************************************************************************************
.nmi_reply_cont
    bit econet_control23_or_status2                                   ; 9dd7: 2c a1 fe    ,..            ; Read RX byte (destination station); BIT SR2: test for RDA (bit7 = data available)
    bpl reply_error                                                   ; 9dda: 10 11       ..             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9ddc: ad a2 fe    ...            ; Read destination network byte
    bne reply_error                                                   ; 9ddf: d0 0c       ..             ; Non-zero -- network mismatch, error
    lda #&f2                                                          ; 9de1: a9 f2       ..             ; Install next handler at &9DE3 (reply validation)
    ldy #&9d                                                          ; 9de3: a0 9d       ..
    bit econet_control1_or_status1                                    ; 9de5: 2c a0 fe    ,..            ; BIT SR1: test IRQ (N=bit7) -- more data ready?
    bmi nmi_reply_validate                                            ; 9de8: 30 08       0.             ; IRQ set -- fall through to &9DE3 without RTI
    jmp set_nmi_vector                                                ; 9dea: 4c 0e 0d    L..            ; IRQ not set -- install handler and RTI

; &9ded referenced 7 times by &9dce, &9dda, &9ddf, &9df5, &9dfd, &9e05, &9e0c
.reply_error
    lda #&41 ; 'A'                                                    ; 9ded: a9 41       .A
    jmp tx_store_result                                               ; 9def: 4c 4e 9f    LN.

; ***************************************************************************************
; RX reply validation (Path 2 for FV/PSE interaction)
; 
; Reads the source station and source network from the reply scout and
; validates them against the original TX destination (&0D20/&0D21).
; Sequence:
;   1. Check SR2 bit7 (RDA) at &9DF2 -- must see data available
;   2. Read source station at &9DE8, compare to &0D20 (tx_dst_stn)
;   3. Read source network at &9DF0, compare to &0D21 (tx_dst_net)
;   4. Check SR2 bit1 (FV) at &9DFA -- must see frame complete
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
    sta econet_control23_or_status2                                   ; 9e10: 8d a1 fe    ...
    lda #&44 ; 'D'                                                    ; 9e13: a9 44       .D             ; CR1=&44: RX_RESET | TIE (TX active for scout ACK)
    sta econet_control1_or_status1                                    ; 9e15: 8d a0 fe    ...
    lda #&ec                                                          ; 9e18: a9 ec       ..             ; Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C
    ldy #&9e                                                          ; 9e1a: a0 9e       ..
    sta nmi_next_lo                                                   ; 9e1c: 8d 4b 0d    .K.
    sty nmi_next_hi                                                   ; 9e1f: 8c 4c 0d    .L.
    lda tx_dst_stn                                                    ; 9e22: ad 20 0d    . .            ; Load dest station for scout ACK TX
    bit econet_control1_or_status1                                    ; 9e25: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
    bvc data_tx_error                                                 ; 9e28: 50 73       Ps             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e2a: 8d a2 fe    ...            ; Write dest station to TX FIFO
    lda tx_dst_net                                                    ; 9e2d: ad 21 0d    .!.            ; Write dest network to TX FIFO
    sta econet_data_continue_frame                                    ; 9e30: 8d a2 fe    ...
    lda #&3a ; ':'                                                    ; 9e33: a9 3a       .:             ; Install handler at &9E2B (write src addr for scout ACK)
    ldy #&9e                                                          ; 9e35: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e37: 4c 0e 0d    L..

; ***************************************************************************************
; TX scout ACK: write source address
; 
; Writes our station ID and network=0 to TX FIFO, completing the
; 4-byte scout ACK frame. Then proceeds to send the data frame.
; ***************************************************************************************
.nmi_scout_ack_src
    lda station_id_disable_net_nmis                                   ; 9e3a: ad 18 fe    ...            ; Load our station ID (also INTOFF)
    bit econet_control1_or_status1                                    ; 9e3d: 2c a0 fe    ,..            ; BIT SR1: test TDRA
    bvc data_tx_error                                                 ; 9e40: 50 5b       P[             ; TDRA not ready -- error
    sta econet_data_continue_frame                                    ; 9e42: 8d a2 fe    ...            ; Write our station to TX FIFO
    lda #0                                                            ; 9e45: a9 00       ..             ; Write network=0 to TX FIFO
    sta econet_data_continue_frame                                    ; 9e47: 8d a2 fe    ...
; &9e4a referenced 1 time by &99bf
.data_tx_begin
    lda #2                                                            ; 9e4a: a9 02       ..
    bit tx_flags                                                      ; 9e4c: 2c 4a 0d    ,J.
    bne c9e58                                                         ; 9e4f: d0 07       ..
    lda #&5f ; '_'                                                    ; 9e51: a9 5f       ._
    ldy #&9e                                                          ; 9e53: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e55: 4c 0e 0d    L..

; &9e58 referenced 1 time by &9e4f
.c9e58
    lda #&b3                                                          ; 9e58: a9 b3       ..
    ldy #&9e                                                          ; 9e5a: a0 9e       ..
    jmp set_nmi_vector                                                ; 9e5c: 4c 0e 0d    L..

; ***************************************************************************************
; TX data phase: send payload
; 
; Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
; Same pattern as the NMI TX handler at &9D5B but reads from the port
; buffer instead of the TX workspace. Writes two bytes per iteration,
; checking SR1 IRQ between pairs for tight looping.
; ***************************************************************************************
.nmi_data_tx
    ldy port_buf_len                                                  ; 9e5f: a4 a2       ..             ; Y = buffer offset, resume from last position
    bit econet_control1_or_status1                                    ; 9e61: 2c a0 fe    ,..            ; BIT SR1: test TDRA (V=bit6)
; &9e64 referenced 1 time by &9e87
.c9e64
    bvc data_tx_error                                                 ; 9e64: 50 37       P7             ; TDRA not ready -- error
    lda (open_port_buf),y                                             ; 9e66: b1 a4       ..             ; Write data byte to TX FIFO
    sta econet_data_continue_frame                                    ; 9e68: 8d a2 fe    ...
    iny                                                               ; 9e6b: c8          .
    bne c9e74                                                         ; 9e6c: d0 06       ..
    dec port_buf_len_hi                                               ; 9e6e: c6 a3       ..
    beq data_tx_last                                                  ; 9e70: f0 1a       ..
    inc open_port_buf_hi                                              ; 9e72: e6 a5       ..
; &9e74 referenced 1 time by &9e6c
.c9e74
    lda (open_port_buf),y                                             ; 9e74: b1 a4       ..
    sta econet_data_continue_frame                                    ; 9e76: 8d a2 fe    ...
    iny                                                               ; 9e79: c8          .
    sty port_buf_len                                                  ; 9e7a: 84 a2       ..
    bne c9e84                                                         ; 9e7c: d0 06       ..
    dec port_buf_len_hi                                               ; 9e7e: c6 a3       ..
    beq data_tx_last                                                  ; 9e80: f0 0a       ..
    inc open_port_buf_hi                                              ; 9e82: e6 a5       ..
; &9e84 referenced 1 time by &9e7c
.c9e84
    bit econet_control1_or_status1                                    ; 9e84: 2c a0 fe    ,..
    bmi c9e64                                                         ; 9e87: 30 db       0.
    jmp nmi_rti                                                       ; 9e89: 4c 14 0d    L..

; &9e8c referenced 4 times by &9e70, &9e80, &9ecc, &9ee2
.data_tx_last
    lda #&3f ; '?'                                                    ; 9e8c: a9 3f       .?             ; CR2=&3F: TX_LAST_DATA (close data frame)
    sta econet_control23_or_status2                                   ; 9e8e: 8d a1 fe    ...
    lda tx_flags                                                      ; 9e91: ad 4a 0d    .J.
    bpl install_saved_handler                                         ; 9e94: 10 14       ..
    lda #&4a ; 'J'                                                    ; 9e96: a9 4a       .J
    ldy #&9a                                                          ; 9e98: a0 9a       ..
    jmp set_nmi_vector                                                ; 9e9a: 4c 0e 0d    L..

; &9e9d referenced 4 times by &9e28, &9e40, &9e64, &9eb6
.data_tx_error
    lda tx_flags                                                      ; 9e9d: ad 4a 0d    .J.
    bpl c9ea5                                                         ; 9ea0: 10 03       ..
    jmp discard_reset_listen                                          ; 9ea2: 4c 4a 9a    LJ.

; &9ea5 referenced 1 time by &9ea0
.c9ea5
    lda #&41 ; 'A'                                                    ; 9ea5: a9 41       .A
    jmp tx_store_result                                               ; 9ea7: 4c 4e 9f    LN.

; &9eaa referenced 1 time by &9e94
.install_saved_handler
    lda nmi_next_lo                                                   ; 9eaa: ad 4b 0d    .K.
    ldy nmi_next_hi                                                   ; 9ead: ac 4c 0d    .L.
    jmp set_nmi_vector                                                ; 9eb0: 4c 0e 0d    L..

.nmi_data_tx_tube
    bit econet_control1_or_status1                                    ; 9eb3: 2c a0 fe    ,..
; &9eb6 referenced 1 time by &9ee7
.c9eb6
    bvc data_tx_error                                                 ; 9eb6: 50 e5       P.
    lda tube_data_register_3                                          ; 9eb8: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9ebb: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9ebe: e6 a2       ..
    bne c9ece                                                         ; 9ec0: d0 0c       ..
    inc port_buf_len_hi                                               ; 9ec2: e6 a3       ..
    bne c9ece                                                         ; 9ec4: d0 08       ..
    inc open_port_buf                                                 ; 9ec6: e6 a4       ..
    bne c9ece                                                         ; 9ec8: d0 04       ..
    inc open_port_buf_hi                                              ; 9eca: e6 a5       ..
    beq data_tx_last                                                  ; 9ecc: f0 be       ..
; &9ece referenced 3 times by &9ec0, &9ec4, &9ec8
.c9ece
    lda tube_data_register_3                                          ; 9ece: ad e5 fe    ...
    sta econet_data_continue_frame                                    ; 9ed1: 8d a2 fe    ...
    inc port_buf_len                                                  ; 9ed4: e6 a2       ..
    bne c9ee4                                                         ; 9ed6: d0 0c       ..
.sub_c9ed8
l9ed9 = sub_c9ed8+1
    inc port_buf_len_hi                                               ; 9ed8: e6 a3       ..
; &9ed9 referenced 1 time by &9cd4
    bne c9ee4                                                         ; 9eda: d0 08       ..
    inc open_port_buf                                                 ; 9edc: e6 a4       ..
    bne c9ee4                                                         ; 9ede: d0 04       ..
.sub_c9ee0
l9ee1 = sub_c9ee0+1
    inc open_port_buf_hi                                              ; 9ee0: e6 a5       ..
; &9ee1 referenced 1 time by &9cce
    beq data_tx_last                                                  ; 9ee2: f0 a8       ..
; &9ee4 referenced 3 times by &9ed6, &9eda, &9ede
.c9ee4
    bit econet_control1_or_status1                                    ; 9ee4: 2c a0 fe    ,..
    bmi c9eb6                                                         ; 9ee7: 30 cd       0.
    jmp nmi_rti                                                       ; 9ee9: 4c 14 0d    L..

; ***************************************************************************************
; Four-way handshake: switch to RX for final ACK
; 
; After the data frame TX completes, switches to RX mode (CR1=&82)
; and installs &9EF8 to receive the final ACK from the remote station.
; ***************************************************************************************
; &9eec referenced 1 time by &9db7
.handshake_await_ack
    lda #&82                                                          ; 9eec: a9 82       ..             ; CR1=&82: TX_RESET | RIE (switch to RX for final ACK)
    sta econet_control1_or_status1                                    ; 9eee: 8d a0 fe    ...
    lda #&f8                                                          ; 9ef1: a9 f8       ..             ; Install handler at &9EE9 (RX final ACK)
    ldy #&9e                                                          ; 9ef3: a0 9e       ..
    jmp set_nmi_vector                                                ; 9ef5: 4c 0e 0d    L..

; ***************************************************************************************
; RX final ACK handler
; 
; Receives the final ACK in a four-way handshake. Same validation
; pattern as the reply scout handler (&9DC1-&9DF2):
;   &9EF8: Check AP, read dest_stn, compare to our station
;   &9F0E: Check RDA, read dest_net, validate = 0
;   &9F24: Check RDA, read src_stn/net, compare to TX dest
;   &9F32: Check FV for frame completion
; On success, stores result=0 at &9F48. On any failure, error &41.
; ***************************************************************************************
.nmi_final_ack
    lda #1                                                            ; 9ef8: a9 01       ..             ; A=&01: AP mask
    bit econet_control23_or_status2                                   ; 9efa: 2c a1 fe    ,..            ; BIT SR2: test AP
    beq tx_result_fail                                                ; 9efd: f0 4d       .M             ; No AP -- error
    lda econet_data_continue_frame                                    ; 9eff: ad a2 fe    ...            ; Read dest station
    cmp station_id_disable_net_nmis                                   ; 9f02: cd 18 fe    ...            ; Compare to our station (INTOFF side effect)
    bne tx_result_fail                                                ; 9f05: d0 45       .E             ; Not our station -- error
    lda #&0e                                                          ; 9f07: a9 0e       ..             ; Install handler at &9EFF (final ACK continuation)
    ldy #&9f                                                          ; 9f09: a0 9f       ..
    jmp set_nmi_vector                                                ; 9f0b: 4c 0e 0d    L..

.nmi_final_ack_net
    bit econet_control23_or_status2                                   ; 9f0e: 2c a1 fe    ,..            ; BIT SR2: test RDA
    bpl tx_result_fail                                                ; 9f11: 10 39       .9             ; No RDA -- error
    lda econet_data_continue_frame                                    ; 9f13: ad a2 fe    ...            ; Read dest network
    bne tx_result_fail                                                ; 9f16: d0 34       .4             ; Non-zero -- network mismatch, error
    lda #&24 ; '$'                                                    ; 9f18: a9 24       .$             ; Install handler at &9F15 (final ACK validation)
    ldy #&9f                                                          ; 9f1a: a0 9f       ..
    bit econet_control1_or_status1                                    ; 9f1c: 2c a0 fe    ,..            ; BIT SR1: test IRQ -- more data ready?
    bmi nmi_final_ack_validate                                        ; 9f1f: 30 03       0.             ; IRQ set -- fall through to &9F15 without RTI
    jmp set_nmi_vector                                                ; 9f21: 4c 0e 0d    L..

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
    lda tx_flags                                                      ; 9f39: ad 4a 0d    .J.
    bpl c9f41                                                         ; 9f3c: 10 03       ..
    jmp c987a                                                         ; 9f3e: 4c 7a 98    Lz.

; &9f41 referenced 1 time by &9f3c
.c9f41
    lda #2                                                            ; 9f41: a9 02       ..             ; A=&02: FV mask for SR2 bit1
    bit econet_control23_or_status2                                   ; 9f43: 2c a1 fe    ,..            ; BIT SR2: test FV -- frame must be complete
    beq tx_result_fail                                                ; 9f46: f0 04       ..             ; No FV -- error
; ***************************************************************************************
; TX completion handler
; 
; Stores result code 0 (success) into the first byte of the TX control
; block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
; and calls full ADLC reset + idle listen via &9A4A.
; ***************************************************************************************
; &9f48 referenced 2 times by &996d, &9dad
.tx_result_ok
    lda #0                                                            ; 9f48: a9 00       ..             ; A=0: success result code
    beq tx_store_result                                               ; 9f4a: f0 02       ..             ; BEQ: always taken (A=0); ALWAYS branch

; &9f4c referenced 8 times by &9efd, &9f05, &9f11, &9f16, &9f27, &9f2f, &9f37, &9f46
.tx_result_fail
    lda #&41 ; 'A'                                                    ; 9f4c: a9 41       .A
; ***************************************************************************************
; TX error handler
; 
; Stores error code (A) into the TX control block, sets &0D3A bit7
; for completion, and returns to idle via &9A4A.
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
    ldy #6                                                            ; 9f6a: a0 06       ..
    lda (nmi_tx_block),y                                              ; 9f6c: b1 a0       ..
    iny                                                               ; 9f6e: c8          .              ; Y=&07
    and (nmi_tx_block),y                                              ; 9f6f: 31 a0       1.
    cmp #&ff                                                          ; 9f71: c9 ff       ..
    beq c9fb6                                                         ; 9f73: f0 41       .A
    lda tx_in_progress                                                ; 9f75: ad 52 0d    .R.
    beq c9fb6                                                         ; 9f78: f0 3c       .<
    lda tx_flags                                                      ; 9f7a: ad 4a 0d    .J.
    ora #2                                                            ; 9f7d: 09 02       ..
    sta tx_flags                                                      ; 9f7f: 8d 4a 0d    .J.
    sec                                                               ; 9f82: 38          8
    php                                                               ; 9f83: 08          .
    ldy #4                                                            ; 9f84: a0 04       ..
; &9f86 referenced 1 time by &9f98
.loop_c9f86
    lda (nmi_tx_block),y                                              ; 9f86: b1 a0       ..
    iny                                                               ; 9f88: c8          .
    iny                                                               ; 9f89: c8          .
    iny                                                               ; 9f8a: c8          .
    iny                                                               ; 9f8b: c8          .
    plp                                                               ; 9f8c: 28          (
    sbc (nmi_tx_block),y                                              ; 9f8d: f1 a0       ..
    sta net_tx_ptr,y                                                  ; 9f8f: 99 9a 00    ...
    dey                                                               ; 9f92: 88          .
    dey                                                               ; 9f93: 88          .
    dey                                                               ; 9f94: 88          .
    php                                                               ; 9f95: 08          .
    cpy #8                                                            ; 9f96: c0 08       ..
    bcc loop_c9f86                                                    ; 9f98: 90 ec       ..
    plp                                                               ; 9f9a: 28          (
    txa                                                               ; 9f9b: 8a          .
    pha                                                               ; 9f9c: 48          H
    lda #4                                                            ; 9f9d: a9 04       ..
    clc                                                               ; 9f9f: 18          .
    adc nmi_tx_block                                                  ; 9fa0: 65 a0       e.
    tax                                                               ; 9fa2: aa          .
    ldy nmi_tx_block_hi                                               ; 9fa3: a4 a1       ..
    lda #&c2                                                          ; 9fa5: a9 c2       ..
    jsr tube_addr_claim                                               ; 9fa7: 20 06 04     ..
    bcc c9fb3                                                         ; 9faa: 90 07       ..
    lda scout_status                                                  ; 9fac: ad 5c 0d    .\.
    jsr tube_addr_claim                                               ; 9faf: 20 06 04     ..
    sec                                                               ; 9fb2: 38          8
; &9fb3 referenced 1 time by &9faa
.c9fb3
    pla                                                               ; 9fb3: 68          h
    tax                                                               ; 9fb4: aa          .
    rts                                                               ; 9fb5: 60          `

; &9fb6 referenced 2 times by &9f73, &9f78
.c9fb6
    ldy #4                                                            ; 9fb6: a0 04       ..
    lda (nmi_tx_block),y                                              ; 9fb8: b1 a0       ..
    ldy #8                                                            ; 9fba: a0 08       ..
    sec                                                               ; 9fbc: 38          8
    sbc (nmi_tx_block),y                                              ; 9fbd: f1 a0       ..
    sta port_buf_len                                                  ; 9fbf: 85 a2       ..
    ldy #5                                                            ; 9fc1: a0 05       ..
    lda (nmi_tx_block),y                                              ; 9fc3: b1 a0       ..
    sbc #0                                                            ; 9fc5: e9 00       ..
    sta open_port_buf_hi                                              ; 9fc7: 85 a5       ..
    ldy #8                                                            ; 9fc9: a0 08       ..
    lda (nmi_tx_block),y                                              ; 9fcb: b1 a0       ..
    sta open_port_buf                                                 ; 9fcd: 85 a4       ..
    ldy #9                                                            ; 9fcf: a0 09       ..
    lda (nmi_tx_block),y                                              ; 9fd1: b1 a0       ..
    sec                                                               ; 9fd3: 38          8
    sbc open_port_buf_hi                                              ; 9fd4: e5 a5       ..
    sta port_buf_len_hi                                               ; 9fd6: 85 a3       ..
    sec                                                               ; 9fd8: 38          8
; &9fd9 referenced 1 time by &968c
.nmi_shim_rom_src
    rts                                                               ; 9fd9: 60          `

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
    bit station_id_disable_net_nmis                                   ; 9fda: 2c 18 fe    ,..
    pha                                                               ; 9fdd: 48          H
    tya                                                               ; 9fde: 98          .
    pha                                                               ; 9fdf: 48          H
    lda #0                                                            ; 9fe0: a9 00       ..
    sta romsel                                                        ; 9fe2: 8d 30 fe    .0.
    jmp nmi_rx_scout                                                  ; 9fe5: 4c 00 97    L..

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
    sty nmi_jmp_hi                                                    ; 9fe8: 8c 0d 0d    ...
    sta nmi_jmp_lo                                                    ; 9feb: 8d 0c 0d    ...
    lda romsel_copy                                                   ; 9fee: a5 f4       ..
    sta romsel                                                        ; 9ff0: 8d 30 fe    .0.
    pla                                                               ; 9ff3: 68          h
    tay                                                               ; 9ff4: a8          .
    pla                                                               ; 9ff5: 68          h
    bit video_ula_control                                             ; 9ff6: 2c 20 fe    , .
    rti                                                               ; 9ff9: 40          @

    equb &ad, &4a, &0d, 9, 2, &8d                                     ; 9ffa: ad 4a 0d... .J.
.pydis_end

    assert <(cat_handler-1) == &01
    assert <(copy_handles-1) == &20
    assert <(copy_handles_and_boot-1) == &1f
    assert <(dispatch_net_cmd-1) == &68
    assert <(econet_tx_rx-1) == &e4
    assert <(eof_handler-1) == &4b
    assert <(execute_at_0100-1) == &97
    assert <(fscv_read_handles-1) == &4b
    assert <(fscv_shutdown-1) == &36
    assert <(fscv_star_handler-1) == &b5
    assert <(insert_remote_key-1) == &b7
    assert <(l0128) == &28
    assert <(net1_read_handle-1) == &3a
    assert <(notify_and_exec-1) == &c4
    assert <(opt_handler-1) == &c9
    assert <(osword_0f_handler-1) == &b7
    assert <(osword_10_handler-1) == &65
    assert <(osword_11_handler-1) == &d1
    assert <(osword_fs_entry-1) == &75
    assert <(remote_boot_handler-1) == &69
    assert <(remote_cmd_dispatch-1) == &cf
    assert <(remote_display_setup-1) == &c3
    assert <(remote_print_handler-1) == &d3
    assert <(remote_validated-1) == &a7
    assert <(resume_after_remote-1) == &7f
    assert <(return_2-1) == &6b
    assert <(rx_imm_exec-1) == &b4
    assert <(rx_imm_machine_type-1) == &dd
    assert <(rx_imm_peek-1) == &f0
    assert <(rx_imm_poke-1) == &d2
    assert <(save_palette_vdu-1) == &9e
    assert <(sub_c8179-1) == &78
    assert <(sub_c82ab-1) == &aa
    assert <(sub_c8d57-1) == &56
    assert <(sub_c8dbf-1) == &be
    assert <(sub_c8e15-1) == &14
    assert <(sub_c8e1a-1) == &19
    assert <(sub_c8e56-1) == &55
    assert <(sub_c8e66-1) == &65
    assert <(sub_c8ef7-1) == &f6
    assert <(sub_c90aa-1) == &a9
    assert <(sub_c913a-1) == &39
    assert <(sub_c9b17-1) == &16
    assert <(sub_c9cf3-1) == &f2
    assert <(svc_abs_workspace-1) == &a1
    assert <(svc_autoboot-1) == &02
    assert <(svc_help-1) == &ec
    assert <(svc_nmi_claim-1) == &68
    assert <(svc_nmi_release-1) == &65
    assert <(svc_unknown_irq-1) == &6b
    assert <(tx_ctrl_exit-1) == &53
    assert <(tx_ctrl_peek-1) == &f6
    assert <(tx_ctrl_poke-1) == &fa
    assert <(tx_ctrl_proc-1) == &19
    assert <(tx_done_continue-1) == &e3
    assert <(tx_done_halt-1) == &cc
    assert <(tx_done_jsr-1) == &a9
    assert <(tx_done_os_proc-1) == &c0
    assert <(tx_done_user_proc-1) == &b2
    assert >(cat_handler-1) == &8c
    assert >(copy_handles-1) == &8e
    assert >(copy_handles_and_boot-1) == &8e
    assert >(dispatch_net_cmd-1) == &80
    assert >(econet_tx_rx-1) == &8f
    assert >(eof_handler-1) == &88
    assert >(execute_at_0100-1) == &84
    assert >(fscv_read_handles-1) == &86
    assert >(fscv_shutdown-1) == &83
    assert >(fscv_star_handler-1) == &8b
    assert >(insert_remote_key-1) == &84
    assert >(l0128) == &01
    assert >(net1_read_handle-1) == &8e
    assert >(notify_and_exec-1) == &8d
    assert >(opt_handler-1) == &89
    assert >(osword_0f_handler-1) == &8e
    assert >(osword_10_handler-1) == &8f
    assert >(osword_11_handler-1) == &8e
    assert >(osword_fs_entry-1) == &8e
    assert >(remote_boot_handler-1) == &84
    assert >(remote_cmd_dispatch-1) == &90
    assert >(remote_display_setup-1) == &91
    assert >(remote_print_handler-1) == &91
    assert >(remote_validated-1) == &84
    assert >(resume_after_remote-1) == &81
    assert >(return_2-1) == &81
    assert >(rx_imm_exec-1) == &9a
    assert >(rx_imm_machine_type-1) == &9a
    assert >(rx_imm_peek-1) == &9a
    assert >(rx_imm_poke-1) == &9a
    assert >(save_palette_vdu-1) == &92
    assert >(sub_c8179-1) == &81
    assert >(sub_c82ab-1) == &82
    assert >(sub_c8d57-1) == &8d
    assert >(sub_c8dbf-1) == &8d
    assert >(sub_c8e15-1) == &8e
    assert >(sub_c8e1a-1) == &8e
    assert >(sub_c8e56-1) == &8e
    assert >(sub_c8e66-1) == &8e
    assert >(sub_c8ef7-1) == &8e
    assert >(sub_c90aa-1) == &90
    assert >(sub_c913a-1) == &91
    assert >(sub_c9b17-1) == &9b
    assert >(sub_c9cf3-1) == &9c
    assert >(svc_abs_workspace-1) == &82
    assert >(svc_autoboot-1) == &82
    assert >(svc_help-1) == &81
    assert >(svc_nmi_claim-1) == &96
    assert >(svc_nmi_release-1) == &96
    assert >(svc_unknown_irq-1) == &96
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

save pydis_start, pydis_end

; Label references by decreasing frequency:
;     nfs_workspace:                           53
;     econet_control23_or_status2:             45
;     fs_options:                              40
;     econet_data_continue_frame:              37
;     fs_cmd_data:                             35
;     net_rx_ptr:                              34
;     econet_control1_or_status1:              31
;     nmi_tx_block:                            29
;     l00f0:                                   27
;     tx_flags:                                26
;     net_tx_ptr:                              24
;     port_ws_offset:                          24
;     fs_load_addr_2:                          23
;     osbyte:                                  23
;     set_nmi_vector:                          22
;     tube_read_r2:                            22
;     port_buf_len:                            20
;     fs_crc_lo:                               19
;     tube_send_r2:                            18
;     open_port_buf_hi:                        16
;     rx_flags:                                16
;     l0f06:                                   15
;     station_id_disable_net_nmis:             15
;     nfs_temp:                                14
;     open_port_buf:                           14
;     print_inline:                            14
;     fs_load_addr:                            13
;     port_buf_len_hi:                         13
;     c9894:                                   12
;     prepare_fs_cmd:                          12
;     tube_data_register_2:                    12
;     fs_error_ptr:                            11
;     tube_status_register_2:                  11
;     nfs_workspace_hi:                        10
;     rom_svc_num:                             10
;     tube_addr_claim:                         10
;     l0000:                                    9
;     l00c8:                                    9
;     nmi_tx_block_hi:                          9
;     rx_src_stn:                               9
;     tube_data_register_3:                     9
;     l00b4:                                    8
;     l00c4:                                    8
;     tube_status_1_and_tube_control:           8
;     tx_result_fail:                           8
;     fs_cmd_urd:                               7
;     fs_last_byte_flag:                        7
;     l0d60:                                    7
;     prot_status:                              7
;     reply_error:                              7
;     restore_args_return:                      7
;     tube_main_loop:                           7
;     tx_clear_flag:                            7
;     tx_dst_stn:                               7
;     fs_cmd_csd:                               6
;     fs_load_addr_hi:                          6
;     fs_sequence_nos:                          6
;     net_rx_ptr_hi:                            6
;     net_tx_ptr_hi:                            6
;     nmi_rti:                                  6
;     osasci:                                   6
;     return_1:                                 6
;     rx_buf_offset:                            6
;     scout_status:                             6
;     sub_c8d45:                                6
;     tx_in_progress:                           6
;     zp_temp_10:                               6
;     c8954:                                    5
;     c8ea9:                                    5
;     dispatch:                                 5
;     fs_block_offset:                          5
;     fs_boot_option:                           5
;     fs_crc_hi:                                5
;     l0001:                                    5
;     l00b3:                                    5
;     l0100:                                    5
;     l0106:                                    5
;     l0f07:                                    5
;     l8659:                                    5
;     printer_buf_ptr:                          5
;     rx_ctrl:                                  5
;     rx_port:                                  5
;     scout_error:                              5
;     system_via_acr:                           5
;     tube_reply_byte:                          5
;     tube_send_r1:                             5
;     tube_send_r4:                             5
;     tx_calc_transfer:                         5
;     tx_dst_net:                               5
;     tx_store_result:                          5
;     zp_temp_11:                               5
;     c886c:                                    4
;     clear_jsr_protection:                     4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     fs_cmd_context:                           4
;     fs_server_net:                            4
;     init_tx_ctrl_block:                       4
;     l0015:                                    4
;     l00b7:                                    4
;     l00b9:                                    4
;     l00c0:                                    4
;     l00c1:                                    4
;     l00ef:                                    4
;     l0101:                                    4
;     l0d58:                                    4
;     nmi_next_hi:                              4
;     nmi_next_lo:                              4
;     os_text_ptr:                              4
;     osrdsc_ptr:                               4
;     return_2:                                 4
;     rx_src_net:                               4
;     tx_done_exit:                             4
;     tx_length:                                4
;     tx_poll_ff:                               4
;     video_ula_control:                        4
;     adlc_full_reset:                          3
;     c84fd:                                    3
;     c896b:                                    3
;     c90e9:                                    3
;     c97e1:                                    3
;     c991c:                                    3
;     c9932:                                    3
;     c9a2a:                                    3
;     c9a96:                                    3
;     c9c5e:                                    3
;     c9ece:                                    3
;     c9ee4:                                    3
;     calc_handle_offset:                       3
;     clear_fs_flag:                            3
;     ctrl_block_setup_alt:                     3
;     data_rx_complete:                         3
;     data_rx_tube_error:                       3
;     discard_listen:                           3
;     econet_init_flag:                         3
;     fs_csd_handle:                            3
;     fs_getb_buf:                              3
;     fs_messages_flag:                         3
;     fs_server_stn:                            3
;     fs_urd_handle:                            3
;     handle_to_mask_a:                         3
;     l0014:                                    3
;     l00af:                                    3
;     l00b5:                                    3
;     l00ba:                                    3
;     l00cf:                                    3
;     l0f08:                                    3
;     l0fde:                                    3
;     l8374:                                    3
;     l859c:                                    3
;     match_osbyte_code:                        3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     openl4:                                   3
;     oscli:                                    3
;     osword:                                   3
;     pad_filename_spaces:                      3
;     romsel_copy:                              3
;     saved_jsr_mask:                           3
;     scout_no_match:                           3
;     send_to_fs_star:                          3
;     setup_tx_and_send:                        3
;     sub_c8d43:                                3
;     sub_c8db2:                                3
;     tube_claim_loop:                          3
;     tube_data_register_1:                     3
;     tube_read_string:                         3
;     tube_reply_ack:                           3
;     tx_ctrl_exit:                             3
;     tx_index:                                 3
;     ack_tx:                                   2
;     ack_tx_write_dest:                        2
;     adjust_addrs:                             2
;     adlc_rx_listen:                           2
;     beginr:                                   2
;     binary_version:                           2
;     c0036:                                    2
;     c04cc:                                    2
;     c0522:                                    2
;     c8099:                                    2
;     c81fb:                                    2
;     c8273:                                    2
;     c82fc:                                    2
;     c84a5:                                    2
;     c8617:                                    2
;     c8634:                                    2
;     c86a0:                                    2
;     c86a8:                                    2
;     c86cf:                                    2
;     c8adf:                                    2
;     c8b56:                                    2
;     c8d59:                                    2
;     c8d73:                                    2
;     c8db0:                                    2
;     c8e12:                                    2
;     c8e1d:                                    2
;     c8fbb:                                    2
;     c9195:                                    2
;     c96be:                                    2
;     c9805:                                    2
;     c9826:                                    2
;     c98fe:                                    2
;     c99c2:                                    2
;     c99d4:                                    2
;     c9a59:                                    2
;     c9aa2:                                    2
;     c9b5e:                                    2
;     c9ca5:                                    2
;     c9fb6:                                    2
;     call_fscv_shutdown:                       2
;     cbset2:                                   2
;     check_escape:                             2
;     cmd_name_matched:                         2
;     compare_addresses:                        2
;     copy_filename_to_cmd:                     2
;     copy_load_addr_from_params:               2
;     copy_reply_to_caller:                     2
;     copy_reply_to_params:                     2
;     data_rx_tube_complete:                    2
;     decode_attribs_5bit:                      2
;     decode_attribs_6bit:                      2
;     econet_tx_retry:                          2
;     flush_output_block:                       2
;     fs_cmd_match_table:                       2
;     fs_cmd_y_param:                           2
;     fs_eof_flags:                             2
;     fs_last_error:                            2
;     fs_lib_handle:                            2
;     fs_putb_buf:                              2
;     fs_state_deb:                             2
;     gsinit:                                   2
;     gsread:                                   2
;     handle_to_mask_clc:                       2
;     init_tx_ctrl_data:                        2
;     l0003:                                    2
;     l0012:                                    2
;     l0058:                                    2
;     l00f1:                                    2
;     l00fd:                                    2
;     l00ff:                                    2
;     l0102:                                    2
;     l0103:                                    2
;     l0128:                                    2
;     l0700:                                    2
;     l0d1e:                                    2
;     l0d59:                                    2
;     l0e30:                                    2
;     l0f09:                                    2
;     l0f10:                                    2
;     l0f11:                                    2
;     l0f12:                                    2
;     l0fdf:                                    2
;     language_entry:                           2
;     logon3:                                   2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     nlisne:                                   2
;     num01:                                    2
;     nvwrch:                                   2
;     option_name_strings:                      2
;     osfind:                                   2
;     osnewl:                                   2
;     parse_decimal:                            2
;     parse_filename_gs:                        2
;     prepare_cmd_clv:                          2
;     prepare_fs_cmd_v:                         2
;     print_decimal:                            2
;     print_decimal_digit:                      2
;     print_file_info:                          2
;     print_hex:                                2
;     print_hex_bytes:                          2
;     print_reply_counted:                      2
;     prlp1:                                    2
;     pydis_start:                              2
;     readc1:                                   2
;     remot1:                                   2
;     return_3:                                 2
;     return_4:                                 2
;     return_5:                                 2
;     return_7:                                 2
;     return_9:                                 2
;     return_copy_param:                        2
;     return_display_setup:                     2
;     return_match_osbyte:                      2
;     return_nbyte:                             2
;     return_tube_init:                         2
;     return_tube_xfer:                         2
;     rom_header:                               2
;     romsel:                                   2
;     rx_extra_byte:                            2
;     rxpol2:                                   2
;     save_fscv_args:                           2
;     scout_complete:                           2
;     send_data_blocks:                         2
;     send_fs_reply_cmd:                        2
;     send_to_fs:                               2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     sub_3_from_y:                             2
;     sub_c8e42:                                2
;     system_via_ier:                           2
;     system_via_ifr:                           2
;     system_via_sr:                            2
;     trampoline_tx_setup:                      2
;     transfer_file_blocks:                     2
;     tube_dispatch_table:                      2
;     tube_osbyte_send_x:                       2
;     tube_osword_read_lp:                      2
;     tube_status_register_4_and_cpu_control:   2
;     tube_transfer_addr:                       2
;     tx_active_start:                          2
;     tx_ctrl_byte:                             2
;     tx_port:                                  2
;     tx_result_ok:                             2
;     tx_src_stn:                               2
;     tx_work_51:                               2
;     tx_work_57:                               2
;     access_bit_table:                         1
;     ack_tx_configure:                         1
;     add_4_to_y:                               1
;     add_5_to_y:                               1
;     adjust_addrs_1:                           1
;     adjust_addrs_9:                           1
;     adjust_addrs_clc:                         1
;     adlc_init:                                1
;     argsw:                                    1
;     begink:                                   1
;     bspsx:                                    1
;     bsxl0:                                    1
;     bsxl1:                                    1
;     build_send_fs_cmd:                        1
;     bytex:                                    1
;     c0419:                                    1
;     c0423:                                    1
;     c0426:                                    1
;     c0455:                                    1
;     c045c:                                    1
;     c0473:                                    1
;     c04a0:                                    1
;     c0535:                                    1
;     c055f:                                    1
;     c05c2:                                    1
;     c067b:                                    1
;     c8093:                                    1
;     c8142:                                    1
;     c8146:                                    1
;     c814e:                                    1
;     c81a7:                                    1
;     c81ae:                                    1
;     c8218:                                    1
;     c8245:                                    1
;     c824a:                                    1
;     c8393:                                    1
;     c8394:                                    1
;     c83ce:                                    1
;     c8430:                                    1
;     c8436:                                    1
;     c8450:                                    1
;     c84c7:                                    1
;     c8544:                                    1
;     c8549:                                    1
;     c85cb:                                    1
;     c85e7:                                    1
;     c85f0:                                    1
;     c8618:                                    1
;     c8673:                                    1
;     c86ac:                                    1
;     c8712:                                    1
;     c87b0:                                    1
;     c87c7:                                    1
;     c87fb:                                    1
;     c8824:                                    1
;     c882d:                                    1
;     c88bb:                                    1
;     c88c1:                                    1
;     c8905:                                    1
;     c8936:                                    1
;     c8959:                                    1
;     c8960:                                    1
;     c89c8:                                    1
;     c89d2:                                    1
;     c89ec:                                    1
;     c8a04:                                    1
;     c8a19:                                    1
;     c8a55:                                    1
;     c8a94:                                    1
;     c8a97:                                    1
;     c8aa8:                                    1
;     c8abc:                                    1
;     c8af3:                                    1
;     c8b34:                                    1
;     c8b41:                                    1
;     c8b59:                                    1
;     c8b95:                                    1
;     c8bde:                                    1
;     c8c0c:                                    1
;     c8c48:                                    1
;     c8c52:                                    1
;     c8c85:                                    1
;     c8cb5:                                    1
;     c8d23:                                    1
;     c8d78:                                    1
;     c8e2b:                                    1
;     c8e63:                                    1
;     c8eaf:                                    1
;     c8f07:                                    1
;     c8f53:                                    1
;     c8f90:                                    1
;     c8ff3:                                    1
;     c9031:                                    1
;     c9144:                                    1
;     c918b:                                    1
;     c9199:                                    1
;     c9202:                                    1
;     c9216:                                    1
;     c9315:                                    1
;     c935a:                                    1
;     c955a:                                    1
;     c968a:                                    1
;     c96b1:                                    1
;     c96d9:                                    1
;     c96dc:                                    1
;     c9718:                                    1
;     c9735:                                    1
;     c9738:                                    1
;     c97ae:                                    1
;     c97bb:                                    1
;     c97bd:                                    1
;     c97cf:                                    1
;     c97d9:                                    1
;     c97ea:                                    1
;     c97ee:                                    1
;     c97fd:                                    1
;     c987a:                                    1
;     c988d:                                    1
;     c98a9:                                    1
;     c98b9:                                    1
;     c98c0:                                    1
;     c98d0:                                    1
;     c9904:                                    1
;     c99bf:                                    1
;     c9a18:                                    1
;     c9a21:                                    1
;     c9a60:                                    1
;     c9b0f:                                    1
;     c9b28:                                    1
;     c9b61:                                    1
;     c9b6b:                                    1
;     c9b97:                                    1
;     c9bf3:                                    1
;     c9c0b:                                    1
;     c9c36:                                    1
;     c9c46:                                    1
;     c9c62:                                    1
;     c9c7c:                                    1
;     c9ca3:                                    1
;     c9cfd:                                    1
;     c9d1c:                                    1
;     c9d25:                                    1
;     c9d47:                                    1
;     c9d85:                                    1
;     c9d8c:                                    1
;     c9db0:                                    1
;     c9dba:                                    1
;     c9e58:                                    1
;     c9e64:                                    1
;     c9e74:                                    1
;     c9e84:                                    1
;     c9ea5:                                    1
;     c9eb6:                                    1
;     c9f41:                                    1
;     c9fb3:                                    1
;     cbset3:                                   1
;     cbset4:                                   1
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
;     decfir:                                   1
;     decmin:                                   1
;     decmor:                                   1
;     delay_1ms:                                1
;     discard_after_reset:                      1
;     dispatch_hi:                              1
;     dispatch_lo:                              1
;     dofs01:                                   1
;     dofs2:                                    1
;     dofsl1:                                   1
;     dofsl5:                                   1
;     dofsl7:                                   1
;     econet_data_terminate_frame:              1
;     entry1:                                   1
;     error1:                                   1
;     error_msg_table:                          1
;     filev:                                    1
;     filev_attrib_dispatch:                    1
;     filev_save:                               1
;     floop:                                    1
;     forward_star_cmd:                         1
;     fs2al1:                                   1
;     fs_cmd_lib:                               1
;     fs_cmd_type:                              1
;     fs_osword_tbl_hi:                         1
;     fs_osword_tbl_lo:                         1
;     fs_vector_addrs:                          1
;     fs_wait_cleanup:                          1
;     fscv:                                     1
;     fscv_star_handler:                        1
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
;     handle_bput_bget:                         1
;     handle_to_mask:                           1
;     handshake_await_ack:                      1
;     immediate_op:                             1
;     info2:                                    1
;     infol2:                                   1
;     init_tx_ctrl_port:                        1
;     init_vectors_and_copy:                    1
;     initl:                                    1
;     install_saved_handler:                    1
;     issue_vectors_claimed:                    1
;     l0002:                                    1
;     l0013:                                    1
;     l0055:                                    1
;     l0059:                                    1
;     l005a:                                    1
;     l00ae:                                    1
;     l00c2:                                    1
;     l00c7:                                    1
;     l00f3:                                    1
;     l00f7:                                    1
;     l0104:                                    1
;     l0350:                                    1
;     l0351:                                    1
;     l0355:                                    1
;     l046b:                                    1
;     l078d:                                    1
;     l0cff:                                    1
;     l0de6:                                    1
;     l0dfe:                                    1
;     l0e0b:                                    1
;     l0e16:                                    1
;     l0ef7:                                    1
;     l0f0b:                                    1
;     l0f0c:                                    1
;     l0f0d:                                    1
;     l0f0e:                                    1
;     l0f13:                                    1
;     l0f14:                                    1
;     l0f16:                                    1
;     l0fe0:                                    1
;     l4:                                       1
;     l7dfd:                                    1
;     l8001:                                    1
;     l8002:                                    1
;     l8004:                                    1
;     l8014:                                    1
;     l865c:                                    1
;     l8be5:                                    1
;     l8cf4:                                    1
;     l8ef5:                                    1
;     l912b:                                    1
;     l945a:                                    1
;     l9a24:                                    1
;     l9a2c:                                    1
;     l9b1d:                                    1
;     l9b22:                                    1
;     l9c6a:                                    1
;     l9ed9:                                    1
;     l9ee1:                                    1
;     language_handler:                         1
;     lodchk:                                   1
;     lodfil:                                   1
;     lodrl1:                                   1
;     lodrl2:                                   1
;     logon2:                                   1
;     loop_c0430:                               1
;     loop_c0448:                               1
;     loop_c048a:                               1
;     loop_c04d1:                               1
;     loop_c0592:                               1
;     loop_c05a6:                               1
;     loop_c05f8:                               1
;     loop_c0604:                               1
;     loop_c061b:                               1
;     loop_c0687:                               1
;     loop_c06a5:                               1
;     loop_c807d:                               1
;     loop_c80a7:                               1
;     loop_c8107:                               1
;     loop_c813a:                               1
;     loop_c819a:                               1
;     loop_c81ce:                               1
;     loop_c82ed:                               1
;     loop_c839b:                               1
;     loop_c8452:                               1
;     loop_c849f:                               1
;     loop_c84d8:                               1
;     loop_c85c3:                               1
;     loop_c85e1:                               1
;     loop_c85f8:                               1
;     loop_c8642:                               1
;     loop_c8676:                               1
;     loop_c8714:                               1
;     loop_c8743:                               1
;     loop_c8745:                               1
;     loop_c878c:                               1
;     loop_c87c4:                               1
;     loop_c8806:                               1
;     loop_c8826:                               1
;     loop_c892d:                               1
;     loop_c893c:                               1
;     loop_c89f8:                               1
;     loop_c8b27:                               1
;     loop_c8b97:                               1
;     loop_c8bbd:                               1
;     loop_c8c7a:                               1
;     loop_c8d03:                               1
;     loop_c8d91:                               1
;     loop_c8d9a:                               1
;     loop_c8ddd:                               1
;     loop_c8de3:                               1
;     loop_c8f27:                               1
;     loop_c8f41:                               1
;     loop_c8fa6:                               1
;     loop_c9008:                               1
;     loop_c9048:                               1
;     loop_c905a:                               1
;     loop_c9109:                               1
;     loop_c9148:                               1
;     loop_c92b6:                               1
;     loop_c968c:                               1
;     loop_c99df:                               1
;     loop_c9a62:                               1
;     loop_c9a8d:                               1
;     loop_c9ac7:                               1
;     loop_c9bdd:                               1
;     loop_c9c1f:                               1
;     loop_c9c3c:                               1
;     loop_c9d04:                               1
;     loop_c9d3b:                               1
;     loop_c9d61:                               1
;     loop_c9d8f:                               1
;     loop_c9f86:                               1
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
;     nmi_shim_rom_src:                         1
;     nmi_workspace_start:                      1
;     nvrdch:                                   1
;     openl6:                                   1
;     openl7:                                   1
;     opter1:                                   1
;     optl1:                                    1
;     osarg1:                                   1
;     osargs:                                   1
;     osbget:                                   1
;     osbput:                                   1
;     osbyte_vdu_table:                         1
;     oseven:                                   1
;     osfile:                                   1
;     osgbpb:                                   1
;     osgbpb_info:                              1
;     osrdch:                                   1
;     osword_tbl_hi:                            1
;     osword_tbl_lo:                            1
;     osword_trampoline:                        1
;     oswrch:                                   1
;     prepare_cmd_with_flag:                    1
;     print_exec_and_len:                       1
;     print_hex_nibble:                         1
;     print_space:                              1
;     quote1:                                   1
;     rchex:                                    1
;     read_args_size:                           1
;     read_vdu_osbyte:                          1
;     read_vdu_osbyte_x0:                       1
;     readry:                                   1
;     return_6:                                 1
;     return_8:                                 1
;     return_bspsx:                             1
;     return_calc_handle:                       1
;     return_compare:                           1
;     return_dofsl7:                            1
;     return_lodchk:                            1
;     rom_type:                                 1
;     rsl1:                                     1
;     rssl1:                                    1
;     rssl2:                                    1
;     rx_error:                                 1
;     rx_error_reset:                           1
;     rx_remote_addr:                           1
;     savchk:                                   1
;     save1:                                    1
;     save_args_handle:                         1
;     save_vdu_state:                           1
;     savsiz:                                   1
;     scan0:                                    1
;     scan1:                                    1
;     scout_discard:                            1
;     scout_loop_rda:                           1
;     scout_loop_second:                        1
;     scout_match_port:                         1
;     scout_reject:                             1
;     select_nfs:                               1
;     send_fs_examine:                          1
;     service_entry:                            1
;     service_handler:                          1
;     set_listen_offset:                        1
;     setup1:                                   1
;     setup_rom_ptrs_netv:                      1
;     setup_rx_buffer_ptrs:                     1
;     skip_cmd_spaces:                          1
;     skpspi:                                   1
;     store_16bit_at_y:                         1
;     store_fs_error:                           1
;     store_retry_count:                        1
;     strnh:                                    1
;     sub_4_from_y:                             1
;     sub_c8348:                                1
;     sub_c86bc:                                1
;     tbcop1:                                   1
;     trampoline_adlc_init:                     1
;     tube_brk_handler:                         1
;     tube_brk_send_loop:                       1
;     tube_code_page4:                          1
;     tube_code_page6:                          1
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
;     tube_return_main:                         1
;     tube_setup_transfer:                      1
;     tube_status_register_3:                   1
;     tx_ctrl_template:                         1
;     tx_data_start:                            1
;     tx_error:                                 1
;     tx_last_data:                             1
;     tx_line_jammed:                           1
;     tx_poll_core:                             1
;     tx_prepare:                               1
;     tx_src_net:                               1
;     update_sequence_return:                   1
;     userv:                                    1
;     y2fsl2:                                   1
;     y2fsl5:                                   1
;     zp_63:                                    1

; Automatically generated labels:
;     c0036
;     c0419
;     c0423
;     c0426
;     c0455
;     c045c
;     c0473
;     c04a0
;     c04cc
;     c0522
;     c0535
;     c055f
;     c05c2
;     c067b
;     c8093
;     c8099
;     c8142
;     c8146
;     c814e
;     c81a7
;     c81ae
;     c81fb
;     c8218
;     c8245
;     c824a
;     c8273
;     c82fc
;     c8393
;     c8394
;     c83ce
;     c8430
;     c8436
;     c8450
;     c84a5
;     c84c7
;     c84fd
;     c8544
;     c8549
;     c85cb
;     c85e7
;     c85f0
;     c8617
;     c8618
;     c8634
;     c8673
;     c86a0
;     c86a8
;     c86ac
;     c86cf
;     c8712
;     c87b0
;     c87c7
;     c87fb
;     c8824
;     c882d
;     c886c
;     c88bb
;     c88c1
;     c8905
;     c8936
;     c8954
;     c8959
;     c8960
;     c896b
;     c89c8
;     c89d2
;     c89ec
;     c8a04
;     c8a19
;     c8a55
;     c8a94
;     c8a97
;     c8aa8
;     c8abc
;     c8adf
;     c8af3
;     c8b34
;     c8b41
;     c8b56
;     c8b59
;     c8b95
;     c8bde
;     c8c0c
;     c8c48
;     c8c52
;     c8c85
;     c8cb5
;     c8d23
;     c8d59
;     c8d73
;     c8d78
;     c8db0
;     c8e12
;     c8e1d
;     c8e2b
;     c8e63
;     c8ea9
;     c8eaf
;     c8f07
;     c8f53
;     c8f90
;     c8fbb
;     c8ff3
;     c9031
;     c90e9
;     c9144
;     c918b
;     c9195
;     c9199
;     c9202
;     c9216
;     c9315
;     c935a
;     c955a
;     c968a
;     c96b1
;     c96be
;     c96d9
;     c96dc
;     c9718
;     c9735
;     c9738
;     c97ae
;     c97bb
;     c97bd
;     c97cf
;     c97d9
;     c97e1
;     c97ea
;     c97ee
;     c97fd
;     c9805
;     c9826
;     c987a
;     c988d
;     c9894
;     c98a9
;     c98b9
;     c98c0
;     c98d0
;     c98fe
;     c9904
;     c991c
;     c9932
;     c99bf
;     c99c2
;     c99d4
;     c9a18
;     c9a21
;     c9a2a
;     c9a59
;     c9a60
;     c9a96
;     c9aa2
;     c9b0f
;     c9b28
;     c9b5e
;     c9b61
;     c9b6b
;     c9b97
;     c9bf3
;     c9c0b
;     c9c36
;     c9c46
;     c9c5e
;     c9c62
;     c9c7c
;     c9ca3
;     c9ca5
;     c9cfd
;     c9d1c
;     c9d25
;     c9d47
;     c9d85
;     c9d8c
;     c9db0
;     c9dba
;     c9e58
;     c9e64
;     c9e74
;     c9e84
;     c9ea5
;     c9eb6
;     c9ece
;     c9ee4
;     c9f41
;     c9fb3
;     c9fb6
;     l0000
;     l0001
;     l0002
;     l0003
;     l0012
;     l0013
;     l0014
;     l0015
;     l0055
;     l0058
;     l0059
;     l005a
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
;     l046b
;     l0700
;     l078d
;     l0cff
;     l0d1e
;     l0d58
;     l0d59
;     l0d60
;     l0de6
;     l0dfe
;     l0e0b
;     l0e11
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
;     l7dfd
;     l8001
;     l8002
;     l8004
;     l800d
;     l8014
;     l8374
;     l859c
;     l859d
;     l85bf
;     l8659
;     l865c
;     l8be5
;     l8cf4
;     l8ef5
;     l912b
;     l945a
;     l9a24
;     l9a2c
;     l9b1d
;     l9b22
;     l9c6a
;     l9ed9
;     l9ee1
;     la260
;     loop_c0430
;     loop_c0448
;     loop_c048a
;     loop_c04d1
;     loop_c0592
;     loop_c05a6
;     loop_c05f8
;     loop_c0604
;     loop_c061b
;     loop_c0687
;     loop_c06a5
;     loop_c807d
;     loop_c80a7
;     loop_c8107
;     loop_c813a
;     loop_c819a
;     loop_c81ce
;     loop_c82ed
;     loop_c839b
;     loop_c8452
;     loop_c849f
;     loop_c84d8
;     loop_c85c3
;     loop_c85e1
;     loop_c85f8
;     loop_c8642
;     loop_c8676
;     loop_c8714
;     loop_c8743
;     loop_c8745
;     loop_c878c
;     loop_c87c4
;     loop_c8806
;     loop_c8826
;     loop_c892d
;     loop_c893c
;     loop_c89f8
;     loop_c8b27
;     loop_c8b97
;     loop_c8bbd
;     loop_c8c7a
;     loop_c8d03
;     loop_c8d91
;     loop_c8d9a
;     loop_c8ddd
;     loop_c8de3
;     loop_c8f27
;     loop_c8f41
;     loop_c8fa6
;     loop_c9008
;     loop_c9048
;     loop_c905a
;     loop_c9109
;     loop_c9148
;     loop_c92b6
;     loop_c968c
;     loop_c99df
;     loop_c9a62
;     loop_c9a8d
;     loop_c9ac7
;     loop_c9bdd
;     loop_c9c1f
;     loop_c9c3c
;     loop_c9d04
;     loop_c9d3b
;     loop_c9d61
;     loop_c9d8f
;     loop_c9f86
;     sub_c8179
;     sub_c82ab
;     sub_c8348
;     sub_c86bc
;     sub_c8d43
;     sub_c8d45
;     sub_c8d57
;     sub_c8db2
;     sub_c8dbf
;     sub_c8e15
;     sub_c8e1a
;     sub_c8e42
;     sub_c8e56
;     sub_c8e66
;     sub_c8ef7
;     sub_c90aa
;     sub_c913a
;     sub_c9a23
;     sub_c9b17
;     sub_c9b1c
;     sub_c9b21
;     sub_c9c68
;     sub_c9cf3
;     sub_c9ed8
;     sub_c9ee0

; Stats:
;     Total size (Code + Data) = 8192 bytes
;     Code                     = 7505 bytes (92%)
;     Data                     = 687 bytes (8%)
;
;     Number of instructions   = 3621
;     Number of data bytes     = 427 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 260 bytes
;     Number of strings        = 37
