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
l0078                                   = &0078
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
nfs_temp                                = &00a8
rom_svc_num                             = &00a9
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
fs_temp_cd                              = &00cd
fs_temp_ce                              = &00ce
l00cf                                   = &00cf
l00e2                                   = &00e2
l00ea                                   = &00ea
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
l18a5                                   = &18a5
l212e                                   = &212e
l7dfd                                   = &7dfd
l85c8                                   = &85c8
la560                                   = &a560
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

.c931a

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
    lda #&ff                                                          ; 931a: a9 ff       ..  :0016[1]
    jsr tube_send_r4                                                  ; 931c: 20 d6 06     .. :0018[1]
    lda tube_data_register_2                                          ; 931f: ad e3 fe    ... :001b[1]
    lda #0                                                            ; 9322: a9 00       ..  :001e[1]
    jsr tube_send_r2                                                  ; 9324: 20 cd 06     .. :0020[1]
    tay                                                               ; 9327: a8          .   :0023[1]
    lda (l00fd),y                                                     ; 9328: b1 fd       ..  :0024[1]
    jsr tube_send_r2                                                  ; 932a: 20 cd 06     .. :0026[1]
; &932d referenced 1 time by &0030[1]
.tube_brk_send_loop
    iny                                                               ; 932d: c8          .   :0029[1]
    lda (l00fd),y                                                     ; 932e: b1 fd       ..  :002a[1]
    jsr tube_send_r2                                                  ; 9330: 20 cd 06     .. :002c[1]
    tax                                                               ; 9333: aa          .   :002f[1]
    bne tube_brk_send_loop                                            ; 9334: d0 f7       ..  :0030[1]
.tube_reset_stack
    ldx #&ff                                                          ; 9336: a2 ff       ..  :0032[1]
    txs                                                               ; 9338: 9a          .   :0034[1]
    cli                                                               ; 9339: 58          X   :0035[1]
; &933a referenced 2 times by &04ec[2], &053a[3]
.c0036
    stx zp_temp_11                                                    ; 933a: 86 11       ..  :0036[1]
    sty zp_temp_10                                                    ; 933c: 84 10       ..  :0038[1]
; &933e referenced 6 times by &0048[1], &05ae[3], &05d5[3], &0635[4], &069d[4], &06ca[4]
.tube_main_loop
    bit tube_status_1_and_tube_control                                ; 933e: 2c e0 fe    ,.. :003a[1]
    bpl tube_poll_r2                                                  ; 9341: 10 06       ..  :003d[1]
; &9343 referenced 1 time by &004d[1]
.tube_handle_wrch
    lda tube_data_register_1                                          ; 9343: ad e1 fe    ... :003f[1]
    jsr nvwrch                                                        ; 9346: 20 cb ff     .. :0042[1]   ; Write character
; &9349 referenced 1 time by &003d[1]
.tube_poll_r2
    bit tube_status_register_2                                        ; 9349: 2c e2 fe    ,.. :0045[1]
    bpl tube_main_loop                                                ; 934c: 10 f0       ..  :0048[1]
    bit tube_status_1_and_tube_control                                ; 934e: 2c e0 fe    ,.. :004a[1]
    bmi tube_handle_wrch                                              ; 9351: 30 f0       0.  :004d[1]
    ldx tube_data_register_2                                          ; 9353: ae e3 fe    ... :004f[1]
    stx l0055                                                         ; 9356: 86 55       .U  :0052[1]
.tube_dispatch_cmd
l0055 = tube_dispatch_cmd+1
    jmp (tube_dispatch_table)                                         ; 9358: 6c 00 05    l.. :0054[1]

; &9359 referenced 1 time by &0052[1]
; &935b referenced 2 times by &0478[2], &0493[2]
.tube_transfer_addr
    equb 0                                                            ; 935b: 00          .   :0057[1]
; &935c referenced 2 times by &047c[2], &0498[2]
.l0058
    equb &80                                                          ; 935c: 80          .   :0058[1]
; &935d referenced 1 time by &04a2[2]
.l0059
    equb 0                                                            ; 935d: 00          .   :0059[1]
; &935e referenced 1 time by &04a0[2]
.l005a
    equb 0                                                            ; 935e: 00          .   :005a[1]

    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock nmi_workspace_start, *, c931a

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear nmi_workspace_start, &005b

    ; Set the program counter to the next position in the binary file.
    org c931a + (* - nmi_workspace_start)

.c935f

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
    jmp c0473                                                         ; 935f: 4c 73 04    Ls. :0400[2]

.tube_escape_entry
    jmp tube_escape_check                                             ; 9362: 4c df 06    L.. :0403[2]

; &9365 referenced 10 times by &04bc[2], &04e4[2], &8b3f, &8b51, &8bae, &8e17, &9a01, &9a53, &9fa7, &9faf
.tube_addr_claim
    cmp #&80                                                          ; 9365: c9 80       ..  :0406[2]
    bcc c0426                                                         ; 9367: 90 1c       ..  :0408[2]
    cmp #&c0                                                          ; 9369: c9 c0       ..  :040a[2]
    bcs c0419                                                         ; 936b: b0 0b       ..  :040c[2]
    ora #&40 ; '@'                                                    ; 936d: 09 40       .@  :040e[2]
    cmp l0015                                                         ; 936f: c5 15       ..  :0410[2]
    bne return_tube_init                                              ; 9371: d0 11       ..  :0412[2]
; &9373 referenced 1 time by &813f
.tube_post_init
    lda #&80                                                          ; 9373: a9 80       ..  :0414[2]
    sta l0014                                                         ; 9375: 85 14       ..  :0416[2]
    rts                                                               ; 9377: 60          `   :0418[2]

; &9378 referenced 1 time by &040c[2]
.c0419
    asl l0014                                                         ; 9378: 06 14       ..  :0419[2]
    bcs c0423                                                         ; 937a: b0 06       ..  :041b[2]
    cmp l0015                                                         ; 937c: c5 15       ..  :041d[2]
    beq return_tube_init                                              ; 937e: f0 04       ..  :041f[2]
    clc                                                               ; 9380: 18          .   :0421[2]
    rts                                                               ; 9381: 60          `   :0422[2]

; &9382 referenced 1 time by &041b[2]
.c0423
    sta l0015                                                         ; 9382: 85 15       ..  :0423[2]
; &9384 referenced 2 times by &0412[2], &041f[2]
.return_tube_init
    rts                                                               ; 9384: 60          `   :0425[2]

; &9385 referenced 1 time by &0408[2]
.c0426
    sty l0013                                                         ; 9385: 84 13       ..  :0426[2]
    stx l0012                                                         ; 9387: 86 12       ..  :0428[2]
    jsr tube_send_r4                                                  ; 9389: 20 d6 06     .. :042a[2]
    tax                                                               ; 938c: aa          .   :042d[2]
    ldy #3                                                            ; 938d: a0 03       ..  :042e[2]
; &938f referenced 1 time by &0436[2]
.loop_c0430
    lda (l0012),y                                                     ; 938f: b1 12       ..  :0430[2]
    jsr tube_send_r4                                                  ; 9391: 20 d6 06     .. :0432[2]
    dey                                                               ; 9394: 88          .   :0435[2]
    bpl loop_c0430                                                    ; 9395: 10 f8       ..  :0436[2]
    jsr tube_send_r4                                                  ; 9397: 20 d6 06     .. :0438[2]
    ldy #&18                                                          ; 939a: a0 18       ..  :043b[2]
    sty tube_status_1_and_tube_control                                ; 939c: 8c e0 fe    ... :043d[2]
    lda l046b,x                                                       ; 939f: bd 6b 04    .k. :0440[2]
    sta tube_status_1_and_tube_control                                ; 93a2: 8d e0 fe    ... :0443[2]
    lsr a                                                             ; 93a5: 4a          J   :0446[2]
    lsr a                                                             ; 93a6: 4a          J   :0447[2]
; &93a7 referenced 1 time by &044b[2]
.loop_c0448
    bit tube_status_register_4_and_cpu_control                        ; 93a7: 2c e6 fe    ,.. :0448[2]
    bvc loop_c0448                                                    ; 93aa: 50 fb       P.  :044b[2]
    bcs c045c                                                         ; 93ac: b0 0d       ..  :044d[2]
    cpx #4                                                            ; 93ae: e0 04       ..  :044f[2]
    bne return_tube_xfer                                              ; 93b0: d0 17       ..  :0451[2]
    pla                                                               ; 93b2: 68          h   :0453[2]
    pla                                                               ; 93b3: 68          h   :0454[2]
; &93b4 referenced 1 time by &04b8[2]
.c0455
    lda #&80                                                          ; 93b4: a9 80       ..  :0455[2]
    sta l0014                                                         ; 93b6: 85 14       ..  :0457[2]
    jmp tube_reply_byte                                               ; 93b8: 4c cd 05    L.. :0459[2]

; &93bb referenced 1 time by &044d[2]
.c045c
    bit tube_data_register_3                                          ; 93bb: 2c e5 fe    ,.. :045c[2]
    bit tube_data_register_3                                          ; 93be: 2c e5 fe    ,.. :045f[2]
    lsr a                                                             ; 93c1: 4a          J   :0462[2]
    bcc return_tube_xfer                                              ; 93c2: 90 05       ..  :0463[2]
    ldy #&88                                                          ; 93c4: a0 88       ..  :0465[2]
    sty tube_status_1_and_tube_control                                ; 93c6: 8c e0 fe    ... :0467[2]
; &93c9 referenced 2 times by &0451[2], &0463[2]
.return_tube_xfer
    rts                                                               ; 93c9: 60          `   :046a[2]

; &93ca referenced 1 time by &0440[2]
.l046b
    equb &86, &88, &96, &98, &18, &18, &82, &18                       ; 93ca: 86 88 96... ... :046b[2]

; &93d2 referenced 1 time by &0400[2]
.c0473
    cli                                                               ; 93d2: 58          X   :0473[2]
    php                                                               ; 93d3: 08          .   :0474[2]
    pha                                                               ; 93d4: 48          H   :0475[2]
    ldy #0                                                            ; 93d5: a0 00       ..  :0476[2]
    sty tube_transfer_addr                                            ; 93d7: 84 57       .W  :0478[2]
    lda #&80                                                          ; 93d9: a9 80       ..  :047a[2]
    sta l0058                                                         ; 93db: 85 58       .X  :047c[2]
    sta l0001                                                         ; 93dd: 85 01       ..  :047e[2]
    lda #&20 ; ' '                                                    ; 93df: a9 20       .   :0480[2]
    and rom_type                                                      ; 93e1: 2d 06 80    -.. :0482[2]
    beq c04a0                                                         ; 93e4: f0 19       ..  :0485[2]
    ldx copyright_offset                                              ; 93e6: ae 07 80    ... :0487[2]
; &93e9 referenced 1 time by &048e[2]
.loop_c048a
    inx                                                               ; 93e9: e8          .   :048a[2]
    lda rom_header,x                                                  ; 93ea: bd 00 80    ... :048b[2]
    bne loop_c048a                                                    ; 93ed: d0 fa       ..  :048e[2]
.sub_c0490
    lda l8001,x                                                       ; 93ef: bd 01 80    ... :0490[2]
    sta tube_transfer_addr                                            ; 93f2: 85 57       .W  :0493[2]
    lda l8002,x                                                       ; 93f4: bd 02 80    ... :0495[2]
    sta l0058                                                         ; 93f7: 85 58       .X  :0498[2]
    ldy service_entry,x                                               ; 93f9: bc 03 80    ... :049a[2]
    lda l8004,x                                                       ; 93fc: bd 04 80    ... :049d[2]
; &93ff referenced 1 time by &0485[2]
.c04a0
    sta l005a                                                         ; 93ff: 85 5a       .Z  :04a0[2]
    sty l0059                                                         ; 9401: 84 59       .Y  :04a2[2]
    pla                                                               ; 9403: 68          h   :04a4[2]
    plp                                                               ; 9404: 28          (   :04a5[2]
    bcs beginr                                                        ; 9405: b0 12       ..  :04a6[2]
    tax                                                               ; 9407: aa          .   :04a8[2]
    bne begink                                                        ; 9408: d0 03       ..  :04a9[2]
    jmp tube_reply_ack                                                ; 940a: 4c cb 05    L.. :04ab[2]

; &940d referenced 1 time by &04a9[2]
.begink
    ldx #0                                                            ; 940d: a2 00       ..  :04ae[2]
    ldy #&ff                                                          ; 940f: a0 ff       ..  :04b0[2]
    lda #osbyte_read_write_last_break_type                            ; 9411: a9 fd       ..  :04b2[2]
    jsr osbyte                                                        ; 9413: 20 f4 ff     .. :04b4[2]   ; Read type of last reset
    txa                                                               ; 9416: 8a          .   :04b7[2]   ; X=value of type of last reset
    beq c0455                                                         ; 9417: f0 9b       ..  :04b8[2]
; &9419 referenced 2 times by &04a6[2], &04bf[2]
.beginr
    lda #&ff                                                          ; 9419: a9 ff       ..  :04ba[2]
    jsr tube_addr_claim                                               ; 941b: 20 06 04     .. :04bc[2]
    bcc beginr                                                        ; 941e: 90 f9       ..  :04bf[2]
    lda #1                                                            ; 9420: a9 01       ..  :04c1[2]
    jsr tube_setup_transfer                                           ; 9422: 20 e0 04     .. :04c3[2]
    ldy #0                                                            ; 9425: a0 00       ..  :04c6[2]
    sty l0000                                                         ; 9427: 84 00       ..  :04c8[2]
    ldx #&40 ; '@'                                                    ; 9429: a2 40       .@  :04ca[2]
; &942b referenced 2 times by &04d7[2], &04dc[2]
.c04cc
    lda (l0000),y                                                     ; 942b: b1 00       ..  :04cc[2]
    sta tube_data_register_3                                          ; 942d: 8d e5 fe    ... :04ce[2]
; &9430 referenced 1 time by &04d4[2]
.loop_c04d1
    bit tube_status_register_3                                        ; 9430: 2c e4 fe    ,.. :04d1[2]
    bvc loop_c04d1                                                    ; 9433: 50 fb       P.  :04d4[2]
    iny                                                               ; 9435: c8          .   :04d6[2]
    bne c04cc                                                         ; 9436: d0 f3       ..  :04d7[2]
    inc l0001                                                         ; 9438: e6 01       ..  :04d9[2]
    dex                                                               ; 943a: ca          .   :04db[2]
    bne c04cc                                                         ; 943b: d0 ee       ..  :04dc[2]
    lda #4                                                            ; 943d: a9 04       ..  :04de[2]
; &943f referenced 1 time by &04c3[2]
.tube_setup_transfer
    ldy #0                                                            ; 943f: a0 00       ..  :04e0[2]
    ldx #&57 ; 'W'                                                    ; 9441: a2 57       .W  :04e2[2]
    jmp tube_addr_claim                                               ; 9443: 4c 06 04    L.. :04e4[2]

.tube_rdch_handler
    lda #1                                                            ; 9446: a9 01       ..  :04e7[2]
    jsr tube_send_r2                                                  ; 9448: 20 cd 06     .. :04e9[2]
    jmp c0036                                                         ; 944b: 4c 36 00    L6. :04ec[2]

.tube_restore_regs
    ldy zp_temp_10                                                    ; 944e: a4 10       ..  :04ef[2]
    ldx zp_temp_11                                                    ; 9450: a6 11       ..  :04f1[2]
    jsr tube_read_r2                                                  ; 9452: 20 f7 04     .. :04f3[2]
    asl a                                                             ; 9455: 0a          .   :04f6[2]
; &9456 referenced 22 times by &04f3[2], &04fa[2], &0543[3], &0547[3], &0550[3], &0569[3], &0580[3], &058c[3], &0592[3], &059b[3], &05b5[3], &05da[3], &05eb[3], &0604[4], &060c[4], &0623[4], &0627[4], &0638[4], &063c[4], &0640[4], &065a[4], &06a2[4]
.tube_read_r2
    bit tube_status_register_2                                        ; 9456: 2c e2 fe    ,.. :04f7[2]
    bpl tube_read_r2                                                  ; 9459: 10 fb       ..  :04fa[2]
    lda tube_data_register_2                                          ; 945b: ad e3 fe    ... :04fc[2]
    rts                                                               ; 945e: 60          `   :04ff[2]


    ; Copy the newly assembled block of code back to it's proper place in the binary
    ; file.
    ; (Note the parameter order: 'copyblock <start>,<end>,<dest>')
    copyblock tube_code_page4, *, c935f

    ; Clear the area of memory we just temporarily used to assemble the new block,
    ; allowing us to assemble there again if needed
    clear tube_code_page4, &0500

    ; Set the program counter to the next position in the binary file.
    org c935f + (* - tube_code_page4)

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
    equb &5b, 5, &c5, 5, &23, 6, &38, 6, &5a, 6, &a0, 6, &ef, 4       ; 945f: 5b 05 c5... [.. :0500[3]
    equb &3d, 5, &8c, 5, &50, 5, &43, 5, &69, 5, &d8, 5,   2, 6       ; 946d: 3d 05 8c... =.. :050e[3]

.tube_wrch_handler
    pha                                                               ; 947b: 48          H   :051c[3]
    lda #0                                                            ; 947c: a9 00       ..  :051d[3]
.tube_send_and_poll
    jsr tube_send_r2                                                  ; 947e: 20 cd 06     .. :051f[3]
; &9481 referenced 2 times by &052a[3], &0532[3]
.c0522
    bit tube_status_register_2                                        ; 9481: 2c e2 fe    ,.. :0522[3]
    bvs c0535                                                         ; 9484: 70 0e       p.  :0525[3]
.tube_poll_r1_wrch
    bit tube_status_1_and_tube_control                                ; 9486: 2c e0 fe    ,.. :0527[3]
    bpl c0522                                                         ; 9489: 10 f6       ..  :052a[3]
    lda tube_data_register_1                                          ; 948b: ad e1 fe    ... :052c[3]
    jsr nvwrch                                                        ; 948e: 20 cb ff     .. :052f[3]   ; Write character
.tube_resume_poll
    jmp c0522                                                         ; 9491: 4c 22 05    L". :0532[3]

; &9494 referenced 1 time by &0525[3]
.c0535
    pla                                                               ; 9494: 68          h   :0535[3]
    sta tube_data_register_2                                          ; 9495: 8d e3 fe    ... :0536[3]
    pha                                                               ; 9498: 48          H   :0539[3]
    jmp c0036                                                         ; 9499: 4c 36 00    L6. :053a[3]

.tube_release_return
    ldx zp_temp_11                                                    ; 949c: a6 11       ..  :053d[3]
    ldy zp_temp_10                                                    ; 949e: a4 10       ..  :053f[3]
    pla                                                               ; 94a0: 68          h   :0541[3]
    rts                                                               ; 94a1: 60          `   :0542[3]

.tube_osbput
    jsr tube_read_r2                                                  ; 94a2: 20 f7 04     .. :0543[3]
    tay                                                               ; 94a5: a8          .   :0546[3]
    jsr tube_read_r2                                                  ; 94a6: 20 f7 04     .. :0547[3]
    jsr osbput                                                        ; 94a9: 20 d4 ff     .. :054a[3]   ; Write a single byte A to an open file Y
    jmp tube_reply_ack                                                ; 94ac: 4c cb 05    L.. :054d[3]

.tube_osbget
    jsr tube_read_r2                                                  ; 94af: 20 f7 04     .. :0550[3]
    tay                                                               ; 94b2: a8          .   :0553[3]   ; Y=file handle
    jsr osbget                                                        ; 94b3: 20 d7 ff     .. :0554[3]   ; Read a single byte from an open file Y
    pha                                                               ; 94b6: 48          H   :0557[3]
    jmp c055f                                                         ; 94b7: 4c 5f 05    L_. :0558[3]

.tube_osrdch
    jsr nvrdch                                                        ; 94ba: 20 c8 ff     .. :055b[3]   ; Read a character from the current input stream
    pha                                                               ; 94bd: 48          H   :055e[3]   ; A=character read
; &94be referenced 2 times by &0558[3], &0620[4]
.c055f
    ora #&80                                                          ; 94be: 09 80       ..  :055f[3]
.tube_rdch_reply
    ror a                                                             ; 94c0: 6a          j   :0561[3]
    jsr tube_send_r2                                                  ; 94c1: 20 cd 06     .. :0562[3]
    pla                                                               ; 94c4: 68          h   :0565[3]
    jmp tube_reply_byte                                               ; 94c5: 4c cd 05    L.. :0566[3]

.tube_osfind
    jsr tube_read_r2                                                  ; 94c8: 20 f7 04     .. :0569[3]
    beq tube_osfind_close                                             ; 94cb: f0 12       ..  :056c[3]
    pha                                                               ; 94cd: 48          H   :056e[3]
    jsr tube_read_string                                              ; 94ce: 20 b1 05     .. :056f[3]
    pla                                                               ; 94d1: 68          h   :0572[3]
    jsr osfind                                                        ; 94d2: 20 ce ff     .. :0573[3]   ; Open or close file(s)
    pha                                                               ; 94d5: 48          H   :0576[3]
    lda #&ff                                                          ; 94d6: a9 ff       ..  :0577[3]
    jsr tube_send_r2                                                  ; 94d8: 20 cd 06     .. :0579[3]
    pla                                                               ; 94db: 68          h   :057c[3]
    jmp tube_reply_byte                                               ; 94dc: 4c cd 05    L.. :057d[3]

; &94df referenced 1 time by &056c[3]
.tube_osfind_close
    jsr tube_read_r2                                                  ; 94df: 20 f7 04     .. :0580[3]
    tay                                                               ; 94e2: a8          .   :0583[3]
    lda #osfind_close                                                 ; 94e3: a9 00       ..  :0584[3]
    jsr osfind                                                        ; 94e5: 20 ce ff     .. :0586[3]   ; Close one or all files
    jmp tube_reply_ack                                                ; 94e8: 4c cb 05    L.. :0589[3]

.tube_osargs
    jsr tube_read_r2                                                  ; 94eb: 20 f7 04     .. :058c[3]
    tay                                                               ; 94ee: a8          .   :058f[3]
.tube_read_params
    ldx #3                                                            ; 94ef: a2 03       ..  :0590[3]
; &94f1 referenced 1 time by &0598[3]
.loop_c0592
    jsr tube_read_r2                                                  ; 94f1: 20 f7 04     .. :0592[3]
    sta l0000,x                                                       ; 94f4: 95 00       ..  :0595[3]
    dex                                                               ; 94f6: ca          .   :0597[3]
    bpl loop_c0592                                                    ; 94f7: 10 f8       ..  :0598[3]
    inx                                                               ; 94f9: e8          .   :059a[3]
    jsr tube_read_r2                                                  ; 94fa: 20 f7 04     .. :059b[3]
    jsr osargs                                                        ; 94fd: 20 da ff     .. :059e[3]   ; Read or write a file's attributes
    jsr tube_send_r2                                                  ; 9500: 20 cd 06     .. :05a1[3]
    ldx #3                                                            ; 9503: a2 03       ..  :05a4[3]
; &9505 referenced 1 time by &05ac[3]
.loop_c05a6
    lda l0000,x                                                       ; 9505: b5 00       ..  :05a6[3]
    jsr tube_send_r2                                                  ; 9507: 20 cd 06     .. :05a8[3]
    dex                                                               ; 950a: ca          .   :05ab[3]
    bpl loop_c05a6                                                    ; 950b: 10 f8       ..  :05ac[3]
    jmp tube_main_loop                                                ; 950d: 4c 3a 00    L:. :05ae[3]

; &9510 referenced 3 times by &056f[3], &05c5[3], &05e2[3]
.tube_read_string
    ldx #0                                                            ; 9510: a2 00       ..  :05b1[3]
    ldy #0                                                            ; 9512: a0 00       ..  :05b3[3]
; &9514 referenced 1 time by &05c0[3]
.strnh
    jsr tube_read_r2                                                  ; 9514: 20 f7 04     .. :05b5[3]
    sta l0700,y                                                       ; 9517: 99 00 07    ... :05b8[3]
    iny                                                               ; 951a: c8          .   :05bb[3]
    beq c05c2                                                         ; 951b: f0 04       ..  :05bc[3]
    cmp #&0d                                                          ; 951d: c9 0d       ..  :05be[3]
    bne strnh                                                         ; 951f: d0 f3       ..  :05c0[3]
; &9521 referenced 1 time by &05bc[3]
.c05c2
    ldy #7                                                            ; 9521: a0 07       ..  :05c2[3]
    rts                                                               ; 9523: 60          `   :05c4[3]

.tube_oscli
    jsr tube_read_string                                              ; 9524: 20 b1 05     .. :05c5[3]
    jsr oscli                                                         ; 9527: 20 f7 ff     .. :05c8[3]
; &952a referenced 3 times by &04ab[2], &054d[3], &0589[3]
.tube_reply_ack
    lda #&7f                                                          ; 952a: a9 7f       ..  :05cb[3]
; &952c referenced 5 times by &0459[2], &0566[3], &057d[3], &05d0[3], &06b5[4]
.tube_reply_byte
    bit tube_status_register_2                                        ; 952c: 2c e2 fe    ,.. :05cd[3]
    bvc tube_reply_byte                                               ; 952f: 50 fb       P.  :05d0[3]
    sta tube_data_register_2                                          ; 9531: 8d e3 fe    ... :05d2[3]
; &9534 referenced 1 time by &0600[4]
.mj
    jmp tube_main_loop                                                ; 9534: 4c 3a 00    L:. :05d5[3]

.tube_osfile
    ldx #&10                                                          ; 9537: a2 10       ..  :05d8[3]
; &9539 referenced 1 time by &05e0[3]
.argsw
    jsr tube_read_r2                                                  ; 9539: 20 f7 04     .. :05da[3]
    sta l0001,x                                                       ; 953c: 95 01       ..  :05dd[3]
    dex                                                               ; 953e: ca          .   :05df[3]
    bne argsw                                                         ; 953f: d0 f8       ..  :05e0[3]
    jsr tube_read_string                                              ; 9541: 20 b1 05     .. :05e2[3]
    stx l0000                                                         ; 9544: 86 00       ..  :05e5[3]
    sty l0001                                                         ; 9546: 84 01       ..  :05e7[3]
    ldy #0                                                            ; 9548: a0 00       ..  :05e9[3]
    jsr tube_read_r2                                                  ; 954a: 20 f7 04     .. :05eb[3]
    jsr osfile                                                        ; 954d: 20 dd ff     .. :05ee[3]
    ora #&80                                                          ; 9550: 09 80       ..  :05f1[3]
    jsr tube_send_r2                                                  ; 9552: 20 cd 06     .. :05f3[3]
    ldx #&10                                                          ; 9555: a2 10       ..  :05f6[3]
; &9557 referenced 1 time by &05fe[3]
.loop_c05f8
    lda l0001,x                                                       ; 9557: b5 01       ..  :05f8[3]
    jsr tube_send_r2                                                  ; 9559: 20 cd 06     .. :05fa[3]
    dex                                                               ; 955c: ca          .   :05fd[3]
    bne loop_c05f8                                                    ; 955d: d0 f8       ..  :05fe[3]

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
    beq mj                                                            ; 955f: f0 d3       ..  :0600[4]
.tube_osgbpb
    ldx #&0c                                                          ; 9561: a2 0c       ..  :0602[4]
; &9563 referenced 1 time by &060a[4]
.loop_c0604
    jsr tube_read_r2                                                  ; 9563: 20 f7 04     .. :0604[4]
    sta l0000,x                                                       ; 9566: 95 00       ..  :0607[4]
    dex                                                               ; 9568: ca          .   :0609[4]
    bpl loop_c0604                                                    ; 9569: 10 f8       ..  :060a[4]
    jsr tube_read_r2                                                  ; 956b: 20 f7 04     .. :060c[4]
    inx                                                               ; 956e: e8          .   :060f[4]
    ldy #0                                                            ; 956f: a0 00       ..  :0610[4]
    jsr osgbpb                                                        ; 9571: 20 d1 ff     .. :0612[4]   ; Read or write multiple bytes to an open file
    pha                                                               ; 9574: 48          H   :0615[4]
    ldx #&0c                                                          ; 9575: a2 0c       ..  :0616[4]
; &9577 referenced 1 time by &061e[4]
.loop_c0618
    lda l0000,x                                                       ; 9577: b5 00       ..  :0618[4]
    jsr tube_send_r2                                                  ; 9579: 20 cd 06     .. :061a[4]
    dex                                                               ; 957c: ca          .   :061d[4]
    bpl loop_c0618                                                    ; 957d: 10 f8       ..  :061e[4]
    jmp c055f                                                         ; 957f: 4c 5f 05    L_. :0620[4]

.tube_osbyte_short
    jsr tube_read_r2                                                  ; 9582: 20 f7 04     .. :0623[4]
    tax                                                               ; 9585: aa          .   :0626[4]
    jsr tube_read_r2                                                  ; 9586: 20 f7 04     .. :0627[4]
    jsr osbyte                                                        ; 9589: 20 f4 ff     .. :062a[4]
; &958c referenced 2 times by &0630[4], &0658[4]
.tube_osbyte_send_x
    bit tube_status_register_2                                        ; 958c: 2c e2 fe    ,.. :062d[4]
    bvc tube_osbyte_send_x                                            ; 958f: 50 fb       P.  :0630[4]
    stx tube_data_register_2                                          ; 9591: 8e e3 fe    ... :0632[4]
; &9594 referenced 1 time by &0648[4]
.bytex
    jmp tube_main_loop                                                ; 9594: 4c 3a 00    L:. :0635[4]

.tube_osbyte_long
    jsr tube_read_r2                                                  ; 9597: 20 f7 04     .. :0638[4]
    tax                                                               ; 959a: aa          .   :063b[4]
    jsr tube_read_r2                                                  ; 959b: 20 f7 04     .. :063c[4]
    tay                                                               ; 959e: a8          .   :063f[4]
    jsr tube_read_r2                                                  ; 959f: 20 f7 04     .. :0640[4]
    jsr osbyte                                                        ; 95a2: 20 f4 ff     .. :0643[4]
    eor #&9d                                                          ; 95a5: 49 9d       I.  :0646[4]
    beq bytex                                                         ; 95a7: f0 eb       ..  :0648[4]
    lda #&40 ; '@'                                                    ; 95a9: a9 40       .@  :064a[4]
    ror a                                                             ; 95ab: 6a          j   :064c[4]
    jsr tube_send_r2                                                  ; 95ac: 20 cd 06     .. :064d[4]
; &95af referenced 1 time by &0653[4]
.tube_osbyte_send_y
    bit tube_status_register_2                                        ; 95af: 2c e2 fe    ,.. :0650[4]
    bvc tube_osbyte_send_y                                            ; 95b2: 50 fb       P.  :0653[4]
    sty tube_data_register_2                                          ; 95b4: 8c e3 fe    ... :0655[4]
    bvs tube_osbyte_send_x                                            ; 95b7: 70 d3       p.  :0658[4]   ; ALWAYS branch

.tube_osword
    jsr tube_read_r2                                                  ; 95b9: 20 f7 04     .. :065a[4]
    tay                                                               ; 95bc: a8          .   :065d[4]
; &95bd referenced 1 time by &0661[4]
.tube_osword_read
    bit tube_status_register_2                                        ; 95bd: 2c e2 fe    ,.. :065e[4]
    bpl tube_osword_read                                              ; 95c0: 10 fb       ..  :0661[4]
    ldx tube_data_register_2                                          ; 95c2: ae e3 fe    ... :0663[4]
    dex                                                               ; 95c5: ca          .   :0666[4]
    bmi c0678                                                         ; 95c6: 30 0f       0.  :0667[4]
; &95c8 referenced 2 times by &066c[4], &0675[4]
.tube_osword_read_lp
    bit tube_status_register_2                                        ; 95c8: 2c e2 fe    ,.. :0669[4]
    bpl tube_osword_read_lp                                           ; 95cb: 10 fb       ..  :066c[4]
    lda tube_data_register_2                                          ; 95cd: ad e3 fe    ... :066e[4]
    sta l0128,x                                                       ; 95d0: 9d 28 01    .(. :0671[4]
    dex                                                               ; 95d3: ca          .   :0674[4]
    bpl tube_osword_read_lp                                           ; 95d4: 10 f2       ..  :0675[4]
    tya                                                               ; 95d6: 98          .   :0677[4]
; &95d7 referenced 1 time by &0667[4]
.c0678
    ldx #<(l0128)                                                     ; 95d7: a2 28       .(  :0678[4]
    ldy #>(l0128)                                                     ; 95d9: a0 01       ..  :067a[4]
    jsr osword                                                        ; 95db: 20 f1 ff     .. :067c[4]
    lda #&ff                                                          ; 95de: a9 ff       ..  :067f[4]
    jsr tube_send_r2                                                  ; 95e0: 20 cd 06     .. :0681[4]
; &95e3 referenced 1 time by &0687[4]
.loop_c0684
    bit tube_status_register_2                                        ; 95e3: 2c e2 fe    ,.. :0684[4]
    bpl loop_c0684                                                    ; 95e6: 10 fb       ..  :0687[4]
    ldx tube_data_register_2                                          ; 95e8: ae e3 fe    ... :0689[4]
    dex                                                               ; 95eb: ca          .   :068c[4]
    bmi tube_return_main                                              ; 95ec: 30 0e       0.  :068d[4]
; &95ee referenced 1 time by &069b[4]
.tube_osword_write
    ldy l0128,x                                                       ; 95ee: bc 28 01    .(. :068f[4]
; &95f1 referenced 1 time by &0695[4]
.tube_osword_write_lp
    bit tube_status_register_2                                        ; 95f1: 2c e2 fe    ,.. :0692[4]
    bvc tube_osword_write_lp                                          ; 95f4: 50 fb       P.  :0695[4]
    sty tube_data_register_2                                          ; 95f6: 8c e3 fe    ... :0697[4]
    dex                                                               ; 95f9: ca          .   :069a[4]
    bpl tube_osword_write                                             ; 95fa: 10 f2       ..  :069b[4]
; &95fc referenced 1 time by &068d[4]
.tube_return_main
    jmp tube_main_loop                                                ; 95fc: 4c 3a 00    L:. :069d[4]

.tube_osword_rdln
    ldx #4                                                            ; 95ff: a2 04       ..  :06a0[4]
; &9601 referenced 1 time by &06a8[4]
.loop_c06a2
    jsr tube_read_r2                                                  ; 9601: 20 f7 04     .. :06a2[4]
    sta l0000,x                                                       ; 9604: 95 00       ..  :06a5[4]
    dex                                                               ; 9606: ca          .   :06a7[4]
    bpl loop_c06a2                                                    ; 9607: 10 f8       ..  :06a8[4]
    inx                                                               ; 9609: e8          .   :06aa[4]
    ldy #0                                                            ; 960a: a0 00       ..  :06ab[4]
    txa                                                               ; 960c: 8a          .   :06ad[4]
    jsr osword                                                        ; 960d: 20 f1 ff     .. :06ae[4]
    bcc tube_rdln_send_line                                           ; 9610: 90 05       ..  :06b1[4]
    lda #&ff                                                          ; 9612: a9 ff       ..  :06b3[4]
    jmp tube_reply_byte                                               ; 9614: 4c cd 05    L.. :06b5[4]

; &9617 referenced 1 time by &06b1[4]
.tube_rdln_send_line
    ldx #0                                                            ; 9617: a2 00       ..  :06b8[4]
    lda #&7f                                                          ; 9619: a9 7f       ..  :06ba[4]
    jsr tube_send_r2                                                  ; 961b: 20 cd 06     .. :06bc[4]
; &961e referenced 1 time by &06c8[4]
.tube_rdln_send_loop
    lda l0700,x                                                       ; 961e: bd 00 07    ... :06bf[4]
.tube_rdln_send_byte
    jsr tube_send_r2                                                  ; 9621: 20 cd 06     .. :06c2[4]
    inx                                                               ; 9624: e8          .   :06c5[4]
    cmp #&0d                                                          ; 9625: c9 0d       ..  :06c6[4]
    bne tube_rdln_send_loop                                           ; 9627: d0 f5       ..  :06c8[4]
    jmp tube_main_loop                                                ; 9629: 4c 3a 00    L:. :06ca[4]

; &962c referenced 17 times by &0020[1], &0026[1], &002c[1], &04e9[2], &051f[3], &0562[3], &0579[3], &05a1[3], &05a8[3], &05f3[3], &05fa[3], &061a[4], &064d[4], &0681[4], &06bc[4], &06c2[4], &06d0[4]
.tube_send_r2
    bit tube_status_register_2                                        ; 962c: 2c e2 fe    ,.. :06cd[4]
    bvc tube_send_r2                                                  ; 962f: 50 fb       P.  :06d0[4]
    sta tube_data_register_2                                          ; 9631: 8d e3 fe    ... :06d2[4]
    rts                                                               ; 9634: 60          `   :06d5[4]

; &9635 referenced 5 times by &0018[1], &042a[2], &0432[2], &0438[2], &06d9[4]
.tube_send_r4
    bit tube_status_register_4_and_cpu_control                        ; 9635: 2c e6 fe    ,.. :06d6[4]
    bvc tube_send_r4                                                  ; 9638: 50 fb       P.  :06d9[4]
    sta tube_data_register_4                                          ; 963a: 8d e7 fe    ... :06db[4]
    rts                                                               ; 963d: 60          `   :06de[4]

; &963e referenced 1 time by &0403[2]
.tube_escape_check
    lda l00ff                                                         ; 963e: a5 ff       ..  :06df[4]
    sec                                                               ; 9640: 38          8   :06e1[4]
    ror a                                                             ; 9641: 6a          j   :06e2[4]
    bmi tube_send_r1                                                  ; 9642: 30 0f       0.  :06e3[4]
.tube_event_handler
    pha                                                               ; 9644: 48          H   :06e5[4]
    lda #0                                                            ; 9645: a9 00       ..  :06e6[4]
    jsr tube_send_r1                                                  ; 9647: 20 f4 06     .. :06e8[4]
    tya                                                               ; 964a: 98          .   :06eb[4]
    jsr tube_send_r1                                                  ; 964b: 20 f4 06     .. :06ec[4]
    txa                                                               ; 964e: 8a          .   :06ef[4]
    jsr tube_send_r1                                                  ; 964f: 20 f4 06     .. :06f0[4]
    pla                                                               ; 9652: 68          h   :06f3[4]
; &9653 referenced 5 times by &06e3[4], &06e8[4], &06ec[4], &06f0[4], &06f7[4]
.tube_send_r1
    bit tube_status_1_and_tube_control                                ; 9653: 2c e0 fe    ,.. :06f4[4]
    bvc tube_send_r1                                                  ; 9656: 50 fb       P.  :06f7[4]
    sta tube_data_register_1                                          ; 9658: 8d e1 fe    ... :06f9[4]
    rts                                                               ; 965b: 60          `   :06fc[4]

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
;   &96F6: RX scout (idle listen, default handler)
;   &9C48: INACTIVE polling (pre-TX, waits for idle line)
;   &9D4C: TX data (2 bytes per NMI, tight loop if IRQ persists)
;   &9D88: TX_LAST_DATA (close frame)
;   &9D94: TX completion (switch to RX: CR1=&82)
;   &9DB2: RX reply scout (check AP, read dest_stn)
;   &9DC8: RX reply continuation (read dest_net, validate)
;   &9DE3: RX reply validation (read src_stn/net, check FV)
;   &9E24: TX scout ACK (write dest/src addr, TX_LAST_DATA)
;   &9EDD: Four-way handshake data phase
; 
; NMI handler chain for inbound reception (scout -> data):
;   &96F6: RX scout (idle listen)
;   &9715: RX scout second byte (dest_net, install &9747)
;   &9747: Scout data loop (read body in pairs, detect FV)
;   &9771: Scout completion (disable PSE, read last byte)
;   &995E: TX scout ACK
;   &9839: RX data frame (AP check, validate dest_stn/net)
;   &984F: RX data frame (validate src_net=0)
;   &9865: RX data frame (skip ctrl/port bytes)
;   &989A: RX data bulk read (read payload into buffer)
;   &98CE: RX data completion (disable PSE, check FV, read last)
;   &995E: TX final ACK
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
.l800d
l8014 = l800d+7
    equs "(C)ROFF", 0                                                 ; 800d: 28 43 29... (C)
; &8014 referenced 1 time by &84dd
    equb &0d, &18                                                     ; 8015: 0d 18       ..
    equs "'1119E"                                                     ; 8017: 27 31 31... '11
    equb 1, 0, &35                                                    ; 801d: 01 00 35    ..5
; Dispatch table: low bytes of (handler_address - 1)
; Each entry stores the low byte of a handler address minus 1,
; for use with the PHA/PHA/RTS dispatch trick at &809F.
; See dispatch_hi (&8044) for the corresponding high bytes.
; Indexed by service number (1-13), language reason (14-18),
; or *NET command (33-36), with a base offset added by the caller.
; &8020 referenced 1 time by &80e3
.dispatch_lo
    equb 3                                                            ; 8020: 03          .
    equb <(return_2-1)                                                ; 8021: 75          u
    equb <(svc_abs_workspace-1)                                       ; 8022: ab          .
    equb <(svc_private_workspace-1)                                   ; 8023: b4          .
    equb <(svc_autoboot-1)                                            ; 8024: 0c          .
    equb <(sub_c8183-1)                                               ; 8025: 82          .
    equb <(svc_unknown_irq-1)                                         ; 8026: 6b          k
    equb <(return_2-1)                                                ; 8027: 75          u
    equb <(dispatch_net_cmd-1)                                        ; 8028: 68          h
    equb <(osword_fs_entry-1)                                         ; 8029: 7d          }
    equb <(svc_help-1)                                                ; 802a: f6          .
    equb <(return_2-1)                                                ; 802b: 75          u
    equb <(svc_nmi_claim-1)                                           ; 802c: 68          h
    equb <(svc_nmi_release-1)                                         ; 802d: 65          e
    equb <(insert_remote_key-1)                                       ; 802e: c4          .
    equb <(remote_boot_handler-1)                                     ; 802f: 76          v
    equb <(save_palette_vdu-1)                                        ; 8030: a3          .
    equb <(execute_at_0100-1)                                         ; 8031: a4          .
    equb <(remote_validated-1)                                        ; 8032: b4          .
    equb <(opt_handler-1)                                             ; 8033: cb          .
    equb <(eof_handler-1)                                             ; 8034: 50          P
    equb <(sub_c8dc7-1)                                               ; 8035: c6          .
    equb <(fscv_star_handler-1)                                       ; 8036: b3          .
    equb <(sub_c8dc7-1)                                               ; 8037: c6          .
    equb <(cat_handler-1)                                             ; 8038: ff          .
    equb <(fscv_shutdown-1)                                           ; 8039: 40          @
    equb <(fscv_read_handles-1)                                       ; 803a: 55          U
    equb <(print_dir_name-1)                                          ; 803b: 5e          ^
    equb <(copy_handles_and_boot-1)                                   ; 803c: 27          '
    equb <(copy_handles-1)                                            ; 803d: 28          (
    equb <(set_csd_handle-1)                                          ; 803e: 21          !
    equb <(notify_and_exec-1)                                         ; 803f: cc          .
    equb <(set_lib_handle-1)                                          ; 8040: 1c          .
    equb <(net1_read_handle-1)                                        ; 8041: 42          B
    equb <(sub_c8e5e-1)                                               ; 8042: 5d          ]
    equb <(sub_c8e6e-1)                                               ; 8043: 6d          m
; Dispatch table: high bytes of (handler_address - 1)
; Paired with dispatch_lo (&8020). Together they form a table of
; 37 handler addresses, used via the PHA/PHA/RTS trick at &809F.
; &8044 referenced 1 time by &80df
.dispatch_hi
    equb <(resume_after_remote-1)                                     ; 8044: 89          .
    equb >(return_2-1)                                                ; 8045: 81          .
    equb >(svc_abs_workspace-1)                                       ; 8046: 82          .
    equb >(svc_private_workspace-1)                                   ; 8047: 82          .
    equb >(svc_autoboot-1)                                            ; 8048: 82          .
    equb >(sub_c8183-1)                                               ; 8049: 81          .
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
    equb >(sub_c8dc7-1)                                               ; 8059: 8d          .
    equb >(fscv_star_handler-1)                                       ; 805a: 8b          .
    equb >(sub_c8dc7-1)                                               ; 805b: 8d          .
    equb >(cat_handler-1)                                             ; 805c: 8b          .
    equb >(fscv_shutdown-1)                                           ; 805d: 83          .
    equb >(fscv_read_handles-1)                                       ; 805e: 86          .
    equb >(print_dir_name-1)                                          ; 805f: 8d          .
    equb >(copy_handles_and_boot-1)                                   ; 8060: 8e          .
    equb >(copy_handles-1)                                            ; 8061: 8e          .
    equb >(set_csd_handle-1)                                          ; 8062: 8e          .
    equb >(notify_and_exec-1)                                         ; 8063: 8d          .
    equb >(set_lib_handle-1)                                          ; 8064: 8e          .
    equb >(net1_read_handle-1)                                        ; 8065: 8e          .
    equb >(sub_c8e5e-1)                                               ; 8066: 8e          .
    equb >(sub_c8e6e-1)                                               ; 8067: 8e          .
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
; *NET1 (&8E43): read file handle from received
; packet (net1_read_handle)
; 
; *NET2 (&8DCA): read handle entry from workspace
; (net2_read_handle_entry)
; 
; *NET3 (&8DE0): close handle / mark as unused
; (net3_close_handle)
; 
; *NET4 (&8DF3): resume after remote operation
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
    sta rom_svc_num                                                   ; 8076: 85 a9       ..
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
    jsr parse_decimal                                                 ; 808a: 20 fd 85     ..            ; Parse decimal number from (fs_options),Y (DECIN)
    bcc c8093                                                         ; 808d: 90 04       ..
    iny                                                               ; 808f: c8          .              ; Y=offset into (fs_options) buffer
    jsr parse_decimal                                                 ; 8090: 20 fd 85     ..            ; Parse decimal number from (fs_options),Y (DECIN)
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
; and catch-all entries in the command match table at &8BD7, and
; from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
; in), returns without sending.
; ***************************************************************************************
; &80b4 referenced 1 time by &809e
.forward_star_cmd
    jsr copy_filename                                                 ; 80b4: 20 4b 8d     K.
    tay                                                               ; 80b7: a8          .              ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 80b8: 20 94 83     ..            ; Prepare FS command buffer (12 references)
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
    jsr l85a5                                                         ; 80c7: 20 a5 85     ..            ; Store A/X/Y in FS workspace
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
; &80da referenced 5 times by &807b, &80c5, &80d2, &80dc, &816a
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
    pha                                                               ; 80ea: 48          H
    lda l0df0,x                                                       ; 80eb: bd f0 0d    ...
    asl a                                                             ; 80ee: 0a          .
    pla                                                               ; 80ef: 68          h
    bmi c80f4                                                         ; 80f0: 30 02       0.
    bcs return_1                                                      ; 80f2: b0 f5       ..
; &80f4 referenced 1 time by &80f0
.c80f4
    cmp #&fe                                                          ; 80f4: c9 fe       ..
    bcc c8150                                                         ; 80f6: 90 58       .X
    bne init_vectors_and_copy                                         ; 80f8: d0 13       ..
    cpy #0                                                            ; 80fa: c0 00       ..
    beq return_1                                                      ; 80fc: f0 eb       ..
    stx zp_temp_11                                                    ; 80fe: 86 11       ..
    sty zp_temp_10                                                    ; 8100: 84 10       ..
    ldx #6                                                            ; 8102: a2 06       ..
    lda #osbyte_explode_chars                                         ; 8104: a9 14       ..
    jsr osbyte                                                        ; 8106: 20 f4 ff     ..            ; Explode character definition RAM (six extra pages), can redefine all characters 32-255 (X=6)
    ldx zp_temp_11                                                    ; 8109: a6 11       ..
    bne c814c                                                         ; 810b: d0 3f       .?
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
    sty zp_temp_10                                                    ; 810d: 84 10       ..
    ldy #&0c                                                          ; 810f: a0 0c       ..
; &8111 referenced 1 time by &8123
.loop_c8111
    ldx return_2,y                                                    ; 8111: be 76 81    .v.
    dey                                                               ; 8114: 88          .
    lda return_2,y                                                    ; 8115: b9 76 81    .v.
    sta userv+1,x                                                     ; 8118: 9d 01 02    ...
    dey                                                               ; 811b: 88          .
    lda return_2,y                                                    ; 811c: b9 76 81    .v.
    sta userv,x                                                       ; 811f: 9d 00 02    ...
    dey                                                               ; 8122: 88          .
    bne loop_c8111                                                    ; 8123: d0 ec       ..
    lda #&8e                                                          ; 8125: a9 8e       ..
    sta tube_status_1_and_tube_control                                ; 8127: 8d e0 fe    ...
; Copy NMI handler code from ROM to RAM pages &04-&06
; &812a referenced 1 time by &813d
.cloop
    lda c935f,y                                                       ; 812a: b9 5f 93    ._.
    sta tube_code_page4,y                                             ; 812d: 99 00 04    ...
    lda l945f,y                                                       ; 8130: b9 5f 94    ._.
    sta tube_dispatch_table,y                                         ; 8133: 99 00 05    ...
    lda c955f,y                                                       ; 8136: b9 5f 95    ._.
    sta tube_code_page6,y                                             ; 8139: 99 00 06    ...
    dey                                                               ; 813c: 88          .
    bne cloop                                                         ; 813d: d0 eb       ..
    jsr tube_post_init                                                ; 813f: 20 14 04     ..
    ldx #&60 ; '`'                                                    ; 8142: a2 60       .`
; Copy NMI workspace initialiser from ROM to &0016-&0076
; &8144 referenced 1 time by &814a
.loop_c8144
    lda c931a,x                                                       ; 8144: bd 1a 93    ...
    sta nmi_workspace_start,x                                         ; 8147: 95 16       ..
    dex                                                               ; 8149: ca          .
    bpl loop_c8144                                                    ; 814a: 10 f8       ..
; &814c referenced 1 time by &810b
.c814c
    ldy zp_temp_10                                                    ; 814c: a4 10       ..
    lda #0                                                            ; 814e: a9 00       ..
; &8150 referenced 1 time by &80f6
.c8150
    cmp #&12                                                          ; 8150: c9 12       ..
    bne c8158                                                         ; 8152: d0 04       ..
    cpy #5                                                            ; 8154: c0 05       ..
    beq select_nfs                                                    ; 8156: f0 67       .g
; &8158 referenced 1 time by &8152
.c8158
    cmp #&0d                                                          ; 8158: c9 0d       ..
    bcs return_2                                                      ; 815a: b0 1a       ..
    tax                                                               ; 815c: aa          .
    lda rom_svc_num                                                   ; 815d: a5 a9       ..
    pha                                                               ; 815f: 48          H
    lda nfs_temp                                                      ; 8160: a5 a8       ..
    pha                                                               ; 8162: 48          H
    stx rom_svc_num                                                   ; 8163: 86 a9       ..
    sty nfs_temp                                                      ; 8165: 84 a8       ..
    tya                                                               ; 8167: 98          .
    ldy #0                                                            ; 8168: a0 00       ..
    jsr dispatch                                                      ; 816a: 20 da 80     ..
    ldx rom_svc_num                                                   ; 816d: a6 a9       ..
    pla                                                               ; 816f: 68          h
    sta nfs_temp                                                      ; 8170: 85 a8       ..
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
    pla                                                               ; 8172: 68          h
    sta rom_svc_num                                                   ; 8173: 85 a9       ..
    txa                                                               ; 8175: 8a          .
; &8176 referenced 4 times by &8111, &8115, &811c, &815a
.return_2
    rts                                                               ; 8176: 60          `

    equb &1c, 5, &0e, &e7, 4, &10, &16, 0, 2, &e5, 6, &20             ; 8177: 1c 05 0e... ...

.sub_c8183
    ldx #8                                                            ; 8183: a2 08       ..
    jsr match_rom_string                                              ; 8185: 20 d6 81     ..
    bne c81b8                                                         ; 8188: d0 2e       ..
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
    ldy #4                                                            ; 818a: a0 04       ..
    lda (net_rx_ptr),y                                                ; 818c: b1 9c       ..
    beq c81b1                                                         ; 818e: f0 21       .!
    lda #0                                                            ; 8190: a9 00       ..
    tax                                                               ; 8192: aa          .              ; X=&00
    sta (net_rx_ptr),y                                                ; 8193: 91 9c       ..
    tay                                                               ; 8195: a8          .              ; Y=&00
    lda #osbyte_read_write_econet_keyboard_disable                    ; 8196: a9 c9       ..
    jsr osbyte                                                        ; 8198: 20 f4 ff     ..            ; Enable keyboard (for Econet)
    lda #&0a                                                          ; 819b: a9 0a       ..
    jsr setup_tx_and_send                                             ; 819d: 20 c0 90     ..
; &81a0 referenced 1 time by &8496
.clear_osbyte_ce_cf
    stx nfs_workspace                                                 ; 81a0: 86 9e       ..
    lda #&ce                                                          ; 81a2: a9 ce       ..
; &81a4 referenced 1 time by &81af
.loop_c81a4
    ldx nfs_workspace                                                 ; 81a4: a6 9e       ..
    ldy #&7f                                                          ; 81a6: a0 7f       ..
    jsr osbyte                                                        ; 81a8: 20 f4 ff     ..
    adc #1                                                            ; 81ab: 69 01       i.
    cmp #&d0                                                          ; 81ad: c9 d0       ..
    beq loop_c81a4                                                    ; 81af: f0 f3       ..
; &81b1 referenced 1 time by &818e
.c81b1
    lda #0                                                            ; 81b1: a9 00       ..
    sta rom_svc_num                                                   ; 81b3: 85 a9       ..
    sta nfs_workspace                                                 ; 81b5: 85 9e       ..
    rts                                                               ; 81b7: 60          `

; &81b8 referenced 1 time by &8188
.c81b8
    ldx #1                                                            ; 81b8: a2 01       ..
    jsr match_rom_string                                              ; 81ba: 20 d6 81     ..
    bne c8205                                                         ; 81bd: d0 46       .F
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
    jsr call_fscv_shutdown                                            ; 81bf: 20 08 82     ..
    sec                                                               ; 81c2: 38          8
    ror nfs_temp                                                      ; 81c3: 66 a8       f.
    jsr issue_vectors_claimed                                         ; 81c5: 20 6b 82     k.
    ldy #&1d                                                          ; 81c8: a0 1d       ..
; &81ca referenced 1 time by &81d2
.initl
    lda (net_rx_ptr),y                                                ; 81ca: b1 9c       ..
    sta fs_state_deb,y                                                ; 81cc: 99 eb 0d    ...
    dey                                                               ; 81cf: 88          .
    cpy #&14                                                          ; 81d0: c0 14       ..
    bne initl                                                         ; 81d2: d0 f6       ..
    beq c8254                                                         ; 81d4: f0 7e       .~             ; ALWAYS branch

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
    ldy nfs_temp                                                      ; 81d6: a4 a8       ..
; &81d8 referenced 1 time by &81e5
.loop_c81d8
    lda (os_text_ptr),y                                               ; 81d8: b1 f2       ..
    and #&df                                                          ; 81da: 29 df       ).
    beq cmd_name_matched                                              ; 81dc: f0 09       ..
    cmp binary_version,x                                              ; 81de: dd 08 80    ...
    bne cmd_name_matched                                              ; 81e1: d0 04       ..
    iny                                                               ; 81e3: c8          .
    inx                                                               ; 81e4: e8          .
    bne loop_c81d8                                                    ; 81e5: d0 f1       ..
; &81e7 referenced 2 times by &81dc, &81e1
.cmd_name_matched
    lda binary_version,x                                              ; 81e7: bd 08 80    ...
    beq skip_cmd_spaces                                               ; 81ea: f0 02       ..
    rts                                                               ; 81ec: 60          `

; &81ed referenced 1 time by &81f2
.skpspi
    iny                                                               ; 81ed: c8          .
; &81ee referenced 1 time by &81ea
.skip_cmd_spaces
    lda (os_text_ptr),y                                               ; 81ee: b1 f2       ..
    cmp #&20 ; ' '                                                    ; 81f0: c9 20       .
    beq skpspi                                                        ; 81f2: f0 f9       ..
    eor #&0d                                                          ; 81f4: 49 0d       I.
    rts                                                               ; 81f6: 60          `

; ***************************************************************************************
; Service 9: *HELP
; 
; Prints the ROM identification string using print_inline.
; ***************************************************************************************
.svc_help
    jsr print_inline                                                  ; 81f7: 20 e2 85     ..
    equs &0d, "NFS 3.35d", &0d                                        ; 81fa: 0d 4e 46... .NF

; &8205 referenced 2 times by &81bd, &821a
.c8205
    ldy nfs_temp                                                      ; 8205: a4 a8       ..
    rts                                                               ; 8207: 60          `

; ***************************************************************************************
; Notify filing system of shutdown
; 
; Loads A=6 (FS shutdown notification) and JMP (FSCV).
; The FSCV handler's RTS returns to the caller of this routine
; (JSR/JMP trick saves one level of stack).
; ***************************************************************************************
; &8208 referenced 2 times by &81bf, &820d
.call_fscv_shutdown
    lda #6                                                            ; 8208: a9 06       ..
    jmp (fscv)                                                        ; 820a: 6c 1e 02    l..

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
    jsr call_fscv_shutdown                                            ; 820d: 20 08 82     ..
    lda #osbyte_scan_keyboard_from_16                                 ; 8210: a9 7a       .z
    jsr osbyte                                                        ; 8212: 20 f4 ff     ..            ; Keyboard scan starting from key 16
    txa                                                               ; 8215: 8a          .              ; X is key number if key is pressed, or &ff otherwise
    bmi c8222                                                         ; 8216: 30 0a       0.
; ***************************************************************************************
; Set up filing system vectors
; 
; Copies 14 bytes from fs_vector_addrs (&828A) into FILEV-FSCV (&0212).
; These set all 7 filing system vectors to the standard extended vector
; dispatch addresses (&FF1B, &FF1E, &FF21, &FF24, &FF27, &FF2A, &FF2D).
; Then calls setup_rom_ptrs_netv to install the extended vector table
; entries with the actual NFS handler addresses, and issues service
; requests to notify other ROMs.
; ***************************************************************************************
.setup_fs_vectors
    eor #&55 ; 'U'                                                    ; 8218: 49 55       IU             ; Copy 14 bytes: FS vector addresses → FILEV-FSCV
    bne c8205                                                         ; 821a: d0 e9       ..
    tay                                                               ; 821c: a8          .              ; Y=key
    lda #osbyte_write_keys_pressed                                    ; 821d: a9 78       .x
    jsr osbyte                                                        ; 821f: 20 f4 ff     ..            ; Write current keys pressed (X and Y)
; &8222 referenced 1 time by &8216
.c8222
    jsr print_inline                                                  ; 8222: 20 e2 85     ..
    equs "Econet Station "                                            ; 8225: 45 63 6f... Eco

    ldy #&14                                                          ; 8234: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8236: b1 9c       ..
    jsr print_decimal                                                 ; 8238: 20 86 8d     ..
    lda #&20 ; ' '                                                    ; 823b: a9 20       .
    bit econet_control23_or_status2                                   ; 823d: 2c a1 fe    ,..
    beq c824f                                                         ; 8240: f0 0d       ..
    jsr print_inline                                                  ; 8242: 20 e2 85     ..
    equs " No Clock"                                                  ; 8245: 20 4e 6f...  No

    nop                                                               ; 824e: ea          .
; &824f referenced 1 time by &8240
.c824f
    jsr print_inline                                                  ; 824f: 20 e2 85     ..
    equs &0d, &0d                                                     ; 8252: 0d 0d       ..

; &8254 referenced 1 time by &81d4
.c8254
    ldy #&0d                                                          ; 8254: a0 0d       ..
; &8256 referenced 1 time by &825d
.loop_c8256
    lda fs_vector_addrs,y                                             ; 8256: b9 8a 82    ...
    sta filev,y                                                       ; 8259: 99 12 02    ...
    dey                                                               ; 825c: 88          .
    bpl loop_c8256                                                    ; 825d: 10 f7       ..
    jsr setup_rom_ptrs_netv                                           ; 825f: 20 15 83     ..
    ldy #&1b                                                          ; 8262: a0 1b       ..
    ldx #7                                                            ; 8264: a2 07       ..
    jsr store_rom_ptr_pair                                            ; 8266: 20 29 83     ).
    stx rom_svc_num                                                   ; 8269: 86 a9       ..
; ***************************************************************************************
; Issue 'vectors claimed' service and optionally auto-boot
; 
; Issues service &0F (vectors claimed) via OSBYTE &8F, then
; service &0A. If fs_temp_cd is zero (auto-boot not inhibited),
; sets up the command string "I .BOOT" at &8246 and jumps to
; the FSCV 3 unrecognised-command handler (which matches against
; the command table at &8BD7). The "I." prefix triggers the
; catch-all entry which forwards the command to the fileserver.
; ***************************************************************************************
; &826b referenced 1 time by &81c5
.issue_vectors_claimed
    lda #osbyte_issue_service_request                                 ; 826b: a9 8f       ..
    ldx #&0f                                                          ; 826d: a2 0f       ..
    jsr osbyte                                                        ; 826f: 20 f4 ff     ..            ; Issue paged ROM service call, Reason X=15 - Vectors claimed
    ldx #&0a                                                          ; 8272: a2 0a       ..
    jsr osbyte                                                        ; 8274: 20 f4 ff     ..
    ldx nfs_temp                                                      ; 8277: a6 a8       ..
    bne return_3                                                      ; 8279: d0 37       .7
    ldx #&82                                                          ; 827b: a2 82       ..
; &827d referenced 2 times by &8329, &832f
.c827d
    ldy #&82                                                          ; 827d: a0 82       ..
    jmp fscv_star_handler                                             ; 827f: 4c b4 8b    L..

    equs "I .BOOT"                                                    ; 8282: 49 20 2e... I .
    equb &0d                                                          ; 8289: 0d          .
; ***************************************************************************************
; FS vector dispatch and handler addresses (34 bytes)
; 
; Bytes 0-13: extended vector dispatch addresses, copied to
; FILEV-FSCV (&0212) by setup_fs_vectors. Each 2-byte pair is
; a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
; the handler in the ROM pointer table.
; 
; Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
; Each entry has addr_lo, addr_hi, then a padding byte that is
; overwritten with the current ROM bank number at runtime. The
; last entry (FSCV) has no padding byte.
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
    equb &4a                                                          ; 829a: 4a          J              ; (ROM bank — overwritten)
    equb &0c                                                          ; 829b: 0c          .              ; ARGSV handler lo (&890C)
    equb &89                                                          ; 829c: 89          .              ; ARGSV handler hi
    equb &44                                                          ; 829d: 44          D              ; (ROM bank — overwritten)
    equb &39                                                          ; 829e: 39          9              ; BGETV handler lo (&8539)
    equb &85                                                          ; 829f: 85          .              ; BGETV handler hi
    equb &57                                                          ; 82a0: 57          W              ; (ROM bank — overwritten)
    equb &ec                                                          ; 82a1: ec          .              ; BPUTV handler lo (&83EC)
    equb &83                                                          ; 82a2: 83          .              ; BPUTV handler hi
    equb &42                                                          ; 82a3: 42          B              ; (ROM bank — overwritten)
    equb &10                                                          ; 82a4: 10          .              ; GBPBV handler lo (&8A10)
    equb &8a                                                          ; 82a5: 8a          .              ; GBPBV handler hi
    equb &41                                                          ; 82a6: 41          A              ; (ROM bank — overwritten)
    equb &78                                                          ; 82a7: 78          x              ; FINDV handler lo (&8978)
    equb &89                                                          ; 82a8: 89          .              ; FINDV handler hi
    equb &52                                                          ; 82a9: 52          R              ; (ROM bank — overwritten)
    equb &c7                                                          ; 82aa: c7          .              ; FSCV handler lo (&80C7)
    equb &80                                                          ; 82ab: 80          .              ; FSCV handler hi

; ***************************************************************************************
; Service 1: claim absolute workspace
; 
; Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
; and FS command buffer (&0F). If Y >= &10, workspace already
; allocated — returns unchanged.
; ***************************************************************************************
.svc_abs_workspace
    cpy #&10                                                          ; 82ac: c0 10       ..
    bcs return_3                                                      ; 82ae: b0 02       ..
    ldy #&10                                                          ; 82b0: a0 10       ..
; &82b2 referenced 2 times by &8279, &82ae
.return_3
    rts                                                               ; 82b2: 60          `

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
.svc_private_workspace
    sty net_rx_ptr_hi                                                 ; 82b5: 84 9d       ..
    iny                                                               ; 82b7: c8          .
    sty nfs_workspace_hi                                              ; 82b8: 84 9f       ..
    lda #0                                                            ; 82ba: a9 00       ..
    ldy #4                                                            ; 82bc: a0 04       ..
    sta (net_rx_ptr),y                                                ; 82be: 91 9c       ..
    ldy #&ff                                                          ; 82c0: a0 ff       ..
    sta net_rx_ptr                                                    ; 82c2: 85 9c       ..
    sta nfs_workspace                                                 ; 82c4: 85 9e       ..
    sta nfs_temp                                                      ; 82c6: 85 a8       ..
    sta tx_clear_flag                                                 ; 82c8: 8d 62 0d    .b.
    tax                                                               ; 82cb: aa          .              ; X=&00
    lda #osbyte_read_write_last_break_type                            ; 82cc: a9 fd       ..             ; OSBYTE &FD: read type of last reset
    jsr osbyte                                                        ; 82ce: 20 f4 ff     ..            ; Read type of last reset
    txa                                                               ; 82d1: 8a          .              ; X=value of type of last reset
    beq c8306                                                         ; 82d2: f0 32       .2             ; Soft break (X=0): skip FS init
    ldy #&15                                                          ; 82d4: a0 15       ..
    lda #&fe                                                          ; 82d6: a9 fe       ..
    sta fs_server_stn                                                 ; 82d8: 8d 00 0e    ...            ; Station &FE = no server selected
    sta (net_rx_ptr),y                                                ; 82db: 91 9c       ..
    lda #0                                                            ; 82dd: a9 00       ..
    sta fs_server_net                                                 ; 82df: 8d 01 0e    ...
    sta prot_status                                                   ; 82e2: 8d 63 0d    .c.
    sta fs_messages_flag                                              ; 82e5: 8d 06 0e    ...
    sta fs_boot_option                                                ; 82e8: 8d 05 0e    ...
    iny                                                               ; 82eb: c8          .              ; Y=&16
    sta (net_rx_ptr),y                                                ; 82ec: 91 9c       ..
    ldy #3                                                            ; 82ee: a0 03       ..
    sta (nfs_workspace),y                                             ; 82f0: 91 9e       ..
    dey                                                               ; 82f2: 88          .              ; Y=&02
    lda #&eb                                                          ; 82f3: a9 eb       ..
    sta (nfs_workspace),y                                             ; 82f5: 91 9e       ..
; &82f7 referenced 1 time by &8304
.loop_c82f7
    lda nfs_temp                                                      ; 82f7: a5 a8       ..
    jsr calc_handle_offset                                            ; 82f9: 20 4c 8e     L.
    bcs c8306                                                         ; 82fc: b0 08       ..
    lda #&3f ; '?'                                                    ; 82fe: a9 3f       .?
    sta (nfs_workspace),y                                             ; 8300: 91 9e       ..
    inc nfs_temp                                                      ; 8302: e6 a8       ..
    bne loop_c82f7                                                    ; 8304: d0 f1       ..
; &8306 referenced 2 times by &82d2, &82fc
.c8306
    lda station_id_disable_net_nmis                                   ; 8306: ad 18 fe    ...            ; Read station ID (also INTOFF)
    ldy #&14                                                          ; 8309: a0 14       ..
    sta (net_rx_ptr),y                                                ; 830b: 91 9c       ..
    jsr trampoline_adlc_init                                          ; 830d: 20 63 96     c.            ; Initialise ADLC hardware
    lda #&40 ; '@'                                                    ; 8310: a9 40       .@
    sta rx_flags                                                      ; 8312: 8d 64 0d    .d.
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
    lda #osbyte_read_rom_ptr_table_low                                ; 8315: a9 a8       ..
    ldx #0                                                            ; 8317: a2 00       ..
    ldy #&ff                                                          ; 8319: a0 ff       ..
    jsr osbyte                                                        ; 831b: 20 f4 ff     ..            ; Read address of ROM pointer table
    stx osrdsc_ptr                                                    ; 831e: 86 f6       ..             ; X=value of address of ROM pointer table (low byte)
    sty l00f7                                                         ; 8320: 84 f7       ..             ; Y=value of address of ROM pointer table (high byte)
    ldy #&36 ; '6'                                                    ; 8322: a0 36       .6
    sty netv                                                          ; 8324: 8c 24 02    .$.
    ldx #1                                                            ; 8327: a2 01       ..
; &8329 referenced 2 times by &8266, &833b
.store_rom_ptr_pair
    lda c827d,y                                                       ; 8329: b9 7d 82    .}.
    sta (osrdsc_ptr),y                                                ; 832c: 91 f6       ..
    iny                                                               ; 832e: c8          .
    lda c827d,y                                                       ; 832f: b9 7d 82    .}.
    sta (osrdsc_ptr),y                                                ; 8332: 91 f6       ..
    iny                                                               ; 8334: c8          .
    lda romsel_copy                                                   ; 8335: a5 f4       ..
    sta (osrdsc_ptr),y                                                ; 8337: 91 f6       ..
    iny                                                               ; 8339: c8          .
    dex                                                               ; 833a: ca          .
    bne store_rom_ptr_pair                                            ; 833b: d0 ec       ..
    ldy nfs_workspace_hi                                              ; 833d: a4 9f       ..
    iny                                                               ; 833f: c8          .
    rts                                                               ; 8340: 60          `

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
    ldy #&1d                                                          ; 8341: a0 1d       ..
; &8343 referenced 1 time by &834b
.fsdiel
    lda fs_state_deb,y                                                ; 8343: b9 eb 0d    ...
    sta (net_rx_ptr),y                                                ; 8346: 91 9c       ..
    dey                                                               ; 8348: 88          .
    cpy #&14                                                          ; 8349: c0 14       ..
    bne fsdiel                                                        ; 834b: d0 f6       ..
    lda #osbyte_printer_driver_going_dormant                          ; 834d: a9 7b       .{
    jmp osbyte                                                        ; 834f: 4c f4 ff    L..            ; Printer driver going dormant

; &8352 referenced 1 time by &83cb
.sub_c8352
    lda #&90                                                          ; 8352: a9 90       ..
; &8354 referenced 1 time by &8840
.init_tx_ctrl_port
    jsr init_tx_ctrl_block                                            ; 8354: 20 60 83     `.
    sta l00c1                                                         ; 8357: 85 c1       ..
    lda #3                                                            ; 8359: a9 03       ..
    sta l00c4                                                         ; 835b: 85 c4       ..
    dec l00c0                                                         ; 835d: c6 c0       ..
    rts                                                               ; 835f: 60          `

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
    pha                                                               ; 8360: 48          H
    ldy #&0b                                                          ; 8361: a0 0b       ..
; &8363 referenced 1 time by &8374
.fstxl1
    lda tx_ctrl_template,y                                            ; 8363: b9 78 83    .x.
    sta l00c0,y                                                       ; 8366: 99 c0 00    ...
    cpy #2                                                            ; 8369: c0 02       ..
    bpl fstxl2                                                        ; 836b: 10 06       ..
    lda fs_server_stn,y                                               ; 836d: b9 00 0e    ...
    sta l00c2,y                                                       ; 8370: 99 c2 00    ...
; &8373 referenced 1 time by &836b
.fstxl2
    dey                                                               ; 8373: 88          .
    bpl fstxl1                                                        ; 8374: 10 ed       ..
    pla                                                               ; 8376: 68          h
    rts                                                               ; 8377: 60          `

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
.l837e
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
    pha                                                               ; 8384: 48          H
    lda #&2a ; '*'                                                    ; 8385: a9 2a       .*
    sec                                                               ; 8387: 38          8
    bcs c839e                                                         ; 8388: b0 14       ..             ; ALWAYS branch

; &838a referenced 2 times by &8704, &87ad
.prepare_cmd_clv
    clv                                                               ; 838a: b8          .
    bvc c839d                                                         ; 838b: 50 10       P.             ; ALWAYS branch

; ***************************************************************************************
; *BYE handler (logoff)
; 
; Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
; then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
; Dispatched from the command match table at &8BD7 for "BYE".
; ***************************************************************************************
.bye_handler
    lda #osbyte_close_spool_exec                                      ; 838d: a9 77       .w
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
    clv                                                               ; 8394: b8          .
; &8395 referenced 2 times by &88c3, &899e
.init_tx_ctrl_data
.prepare_fs_cmd_v
    lda fs_urd_handle                                                 ; 8395: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8398: 8d 02 0f    ...
    lda #&2a ; '*'                                                    ; 839b: a9 2a       .*
; &839d referenced 1 time by &838b
.c839d
    clc                                                               ; 839d: 18          .
; &839e referenced 1 time by &8388
.c839e
    sty fs_cmd_y_param                                                ; 839e: 8c 01 0f    ...
    sta fs_error_ptr                                                  ; 83a1: 85 b8       ..
    ldy #1                                                            ; 83a3: a0 01       ..
; &83a5 referenced 1 time by &83ac
.loop_c83a5
    lda fs_csd_handle,y                                               ; 83a5: b9 03 0e    ...            ; A=timeout period for FS reply
    sta fs_cmd_csd,y                                                  ; 83a8: 99 03 0f    ...
    dey                                                               ; 83ab: 88          .              ; Y=function code
    bpl loop_c83a5                                                    ; 83ac: 10 f7       ..
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
    php                                                               ; 83ae: 08          .
    lda #&90                                                          ; 83af: a9 90       ..
    sta fs_cmd_type                                                   ; 83b1: 8d 00 0f    ...
    jsr init_tx_ctrl_block                                            ; 83b4: 20 60 83     `.
    txa                                                               ; 83b7: 8a          .
    adc #5                                                            ; 83b8: 69 05       i.
    sta l00c8                                                         ; 83ba: 85 c8       ..
    plp                                                               ; 83bc: 28          (
    bcs dofsl5                                                        ; 83bd: b0 22       ."
    php                                                               ; 83bf: 08          .
    jsr setup_tx_ptr_c0                                               ; 83c0: 20 69 86     i.
    plp                                                               ; 83c3: 28          (
    bcc send_fs_reply_cmd                                             ; 83c4: 90 04       ..
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
    lda #&2a ; '*'                                                    ; 83c6: a9 2a       .*
    sta fs_error_ptr                                                  ; 83c8: 85 b8       ..
; &83ca referenced 1 time by &83c4
.send_fs_reply_cmd
    php                                                               ; 83ca: 08          .
    jsr sub_c8352                                                     ; 83cb: 20 52 83     R.
    lda fs_error_ptr                                                  ; 83ce: a5 b8       ..
    jsr send_to_fs                                                    ; 83d0: 20 fa 84     ..
    plp                                                               ; 83d3: 28          (
; &83d4 referenced 1 time by &83ea
.dofsl7
    iny                                                               ; 83d4: c8          .
    lda (l00c4),y                                                     ; 83d5: b1 c4       ..
    tax                                                               ; 83d7: aa          .
    beq return_dofsl7                                                 ; 83d8: f0 06       ..
    bvc c83de                                                         ; 83da: 50 02       P.
    adc #&2a ; '*'                                                    ; 83dc: 69 2a       i*
; &83de referenced 1 time by &83da
.c83de
    bne store_fs_error                                                ; 83de: d0 70       .p
; &83e0 referenced 1 time by &83d8
.return_dofsl7
    rts                                                               ; 83e0: 60          `

; &83e1 referenced 1 time by &83bd
.dofsl5
    pla                                                               ; 83e1: 68          h
    ldx #&c0                                                          ; 83e2: a2 c0       ..
    iny                                                               ; 83e4: c8          .
    jsr econet_tx_retry                                               ; 83e5: 20 5b 92     [.
    sta l00b3                                                         ; 83e8: 85 b3       ..
    bcc dofsl7                                                        ; 83ea: 90 e8       ..
.bputv_handler
    clc                                                               ; 83ec: 18          .
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
    pha                                                               ; 83ed: 48          H
    sta l0fdf                                                         ; 83ee: 8d df 0f    ...
    txa                                                               ; 83f1: 8a          .
    pha                                                               ; 83f2: 48          H
    tya                                                               ; 83f3: 98          .
    pha                                                               ; 83f4: 48          H
    php                                                               ; 83f5: 08          .
    sty l00ba                                                         ; 83f6: 84 ba       ..
    jsr handle_to_mask_clc                                            ; 83f8: 20 26 86     &.
    sty l0fde                                                         ; 83fb: 8c de 0f    ...
    sty l00cf                                                         ; 83fe: 84 cf       ..
    ldy #&90                                                          ; 8400: a0 90       ..
    sty fs_putb_buf                                                   ; 8402: 8c dc 0f    ...
    jsr init_tx_ctrl_block                                            ; 8405: 20 60 83     `.
    lda #&dc                                                          ; 8408: a9 dc       ..
    sta l00c4                                                         ; 840a: 85 c4       ..
    lda #&e0                                                          ; 840c: a9 e0       ..
    sta l00c8                                                         ; 840e: 85 c8       ..
    iny                                                               ; 8410: c8          .
    ldx #9                                                            ; 8411: a2 09       ..
    plp                                                               ; 8413: 28          (
    bcc store_retry_count                                             ; 8414: 90 01       ..
    dex                                                               ; 8416: ca          .              ; X=&08
; &8417 referenced 1 time by &8414
.store_retry_count
    stx fs_getb_buf                                                   ; 8417: 8e dd 0f    ...
    lda l00cf                                                         ; 841a: a5 cf       ..
    ldx #&c0                                                          ; 841c: a2 c0       ..
    jsr econet_tx_retry                                               ; 841e: 20 5b 92     [.
    ldx fs_getb_buf                                                   ; 8421: ae dd 0f    ...
    beq update_sequence_return                                        ; 8424: f0 48       .H
    ldy #&1f                                                          ; 8426: a0 1f       ..
; &8428 referenced 1 time by &842f
.error1
    lda fs_putb_buf,y                                                 ; 8428: b9 dc 0f    ...
    sta l0fe0,y                                                       ; 842b: 99 e0 0f    ...
    dey                                                               ; 842e: 88          .
    bpl error1                                                        ; 842f: 10 f7       ..
    tax                                                               ; 8431: aa          .              ; X=File handle
    lda #osbyte_read_write_exec_file_handle                           ; 8432: a9 c6       ..
    jsr osbyte                                                        ; 8434: 20 f4 ff     ..            ; Read/Write *EXEC file handle
    lda #&f1                                                          ; 8437: a9 f1       ..
    cpy l00ba                                                         ; 8439: c4 ba       ..             ; Y=value of *SPOOL file handle
    beq c8443                                                         ; 843b: f0 06       ..
    lda #&f5                                                          ; 843d: a9 f5       ..
    cpx l00ba                                                         ; 843f: e4 ba       ..             ; X=value of *EXEC file handle
    bne c8449                                                         ; 8441: d0 06       ..
; &8443 referenced 1 time by &843b
.c8443
    tax                                                               ; 8443: aa          .
    ldy #&84                                                          ; 8444: a0 84       ..
    jsr oscli                                                         ; 8446: 20 f7 ff     ..
; &8449 referenced 1 time by &8441
.c8449
    lda #&e0                                                          ; 8449: a9 e0       ..
    sta l00c4                                                         ; 844b: 85 c4       ..
    ldx fs_getb_buf                                                   ; 844d: ae dd 0f    ...
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
    stx fs_last_error                                                 ; 8450: 8e 09 0e    ...
    ldy #1                                                            ; 8453: a0 01       ..
    cpx #&a8                                                          ; 8455: e0 a8       ..
    bcs c845d                                                         ; 8457: b0 04       ..
    lda #&a8                                                          ; 8459: a9 a8       ..
    sta (l00c4),y                                                     ; 845b: 91 c4       ..
; &845d referenced 1 time by &8457
.c845d
    ldy #&ff                                                          ; 845d: a0 ff       ..
; &845f referenced 1 time by &8467
.loop_c845f
    iny                                                               ; 845f: c8          .
    lda (l00c4),y                                                     ; 8460: b1 c4       ..
    sta l0100,y                                                       ; 8462: 99 00 01    ...
    eor #&0d                                                          ; 8465: 49 0d       I.
    bne loop_c845f                                                    ; 8467: d0 f6       ..
    sta l0100,y                                                       ; 8469: 99 00 01    ...
    beq c84b2                                                         ; 846c: f0 44       .D             ; ALWAYS branch

; &846e referenced 1 time by &8424
.update_sequence_return
    sta fs_sequence_nos                                               ; 846e: 8d 08 0e    ...
    pla                                                               ; 8471: 68          h
    tay                                                               ; 8472: a8          .
    pla                                                               ; 8473: 68          h
    tax                                                               ; 8474: aa          .
    pla                                                               ; 8475: 68          h
.return_remote_cmd
    rts                                                               ; 8476: 60          `

; ***************************************************************************************
; Remote boot/execute handler
; 
; Checks byte 4 of the RX control block (remote status flag).
; If zero (not currently remoted), falls through to remot1 to
; set up a new remote session. If non-zero (already remoted),
; jumps to clear_jsr_protection and returns.
; ***************************************************************************************
.remote_boot_handler
    ldy #4                                                            ; 8477: a0 04       ..
    lda (net_rx_ptr),y                                                ; 8479: b1 9c       ..
    beq remot1                                                        ; 847b: f0 03       ..
; &847d referenced 1 time by &84c3
.rchex
    jmp clear_jsr_protection                                          ; 847d: 4c e9 92    L..

; &8480 referenced 2 times by &847b, &84b9
.remot1
    ora #9                                                            ; 8480: 09 09       ..
    sta (net_rx_ptr),y                                                ; 8482: 91 9c       ..
    ldx #&80                                                          ; 8484: a2 80       ..
    ldy #&80                                                          ; 8486: a0 80       ..
    lda (net_rx_ptr),y                                                ; 8488: b1 9c       ..
    pha                                                               ; 848a: 48          H
    iny                                                               ; 848b: c8          .              ; Y=&81
    lda (net_rx_ptr),y                                                ; 848c: b1 9c       ..
    ldy #&0f                                                          ; 848e: a0 0f       ..
    sta (nfs_workspace),y                                             ; 8490: 91 9e       ..
    dey                                                               ; 8492: 88          .              ; Y=&0e
    pla                                                               ; 8493: 68          h
    sta (nfs_workspace),y                                             ; 8494: 91 9e       ..
    jsr clear_osbyte_ce_cf                                            ; 8496: 20 a0 81     ..
    jsr ctrl_block_setup                                              ; 8499: 20 76 91     v.
    ldx #1                                                            ; 849c: a2 01       ..
    ldy #0                                                            ; 849e: a0 00       ..
    lda #osbyte_read_write_econet_keyboard_disable                    ; 84a0: a9 c9       ..
    jsr osbyte                                                        ; 84a2: 20 f4 ff     ..            ; Disable keyboard (for Econet)
; ***************************************************************************************
; Execute code at &0100
; 
; Clears JSR protection, zeroes &0100-&0102 (creating a BRK
; instruction at &0100 as a safe default), then JMP &0100 to
; execute code received over the network. If no code was loaded,
; the BRK triggers an error handler.
; ***************************************************************************************
.execute_at_0100
    jsr clear_jsr_protection                                          ; 84a5: 20 e9 92     ..
    ldx #2                                                            ; 84a8: a2 02       ..
    lda #0                                                            ; 84aa: a9 00       ..
; &84ac referenced 1 time by &84b0
.loop_c84ac
    sta l0100,x                                                       ; 84ac: 9d 00 01    ...
    dex                                                               ; 84af: ca          .
    bpl loop_c84ac                                                    ; 84b0: 10 fa       ..
; &84b2 referenced 2 times by &846c, &84eb
.c84b2
    jmp l0100                                                         ; 84b2: 4c 00 01    L..

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
    ldy #4                                                            ; 84b5: a0 04       ..
    lda (net_rx_ptr),y                                                ; 84b7: b1 9c       ..
    beq remot1                                                        ; 84b9: f0 c5       ..
    ldy #&80                                                          ; 84bb: a0 80       ..
    lda (net_rx_ptr),y                                                ; 84bd: b1 9c       ..
    ldy #&0e                                                          ; 84bf: a0 0e       ..
    cmp (nfs_workspace),y                                             ; 84c1: d1 9e       ..
    bne rchex                                                         ; 84c3: d0 b8       ..
; ***************************************************************************************
; Insert remote keypress
; 
; Reads a character from RX block offset &82 and inserts it into
; keyboard input buffer 0 via OSBYTE &99.
; ***************************************************************************************
.insert_remote_key
    ldy #&82                                                          ; 84c5: a0 82       ..
    lda (net_rx_ptr),y                                                ; 84c7: b1 9c       ..
    tay                                                               ; 84c9: a8          .
    ldx #0                                                            ; 84ca: a2 00       ..
    jsr clear_jsr_protection                                          ; 84cc: 20 e9 92     ..
    lda #osbyte_insert_input_buffer                                   ; 84cf: a9 99       ..
    jmp osbyte                                                        ; 84d1: 4c f4 ff    L..            ; Insert character Y into input buffer X

; &84d4 referenced 1 time by &8527
.c84d4
    lda #8                                                            ; 84d4: a9 08       ..
    bne set_listen_offset                                             ; 84d6: d0 04       ..             ; ALWAYS branch

; &84d8 referenced 1 time by &86b2
.nlistn
    lda (net_tx_ptr,x)                                                ; 84d8: a1 9a       ..
; &84da referenced 2 times by &8537, &89de
.nlisne
    and #7                                                            ; 84da: 29 07       ).
; &84dc referenced 1 time by &84d6
.set_listen_offset
    tax                                                               ; 84dc: aa          .
    ldy l8014,x                                                       ; 84dd: bc 14 80    ...
    ldx #0                                                            ; 84e0: a2 00       ..
    stx l0100                                                         ; 84e2: 8e 00 01    ...
; &84e5 referenced 1 time by &84ef
.loop_c84e5
    lda error_msg_table,y                                             ; 84e5: b9 56 85    .V.
    sta l0101,x                                                       ; 84e8: 9d 01 01    ...
    beq c84b2                                                         ; 84eb: f0 c5       ..
    iny                                                               ; 84ed: c8          .
    inx                                                               ; 84ee: e8          .
    bne loop_c84e5                                                    ; 84ef: d0 f4       ..
    equs "SP."                                                        ; 84f1: 53 50 2e    SP.
    equb &0d, &45, &2e, &0d                                           ; 84f4: 0d 45 2e... .E.

; &84f8 referenced 3 times by &875d, &9036, &9290
.c84f8
    lda #&2a ; '*'                                                    ; 84f8: a9 2a       .*
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
    pha                                                               ; 84fa: 48          H
    lda rx_flags                                                      ; 84fb: ad 64 0d    .d.
    pha                                                               ; 84fe: 48          H
    ora #&80                                                          ; 84ff: 09 80       ..
    sta rx_flags                                                      ; 8501: 8d 64 0d    .d.
    lda #0                                                            ; 8504: a9 00       ..
    pha                                                               ; 8506: 48          H
    pha                                                               ; 8507: 48          H
    tay                                                               ; 8508: a8          .              ; Y=&00
    tsx                                                               ; 8509: ba          .
; &850a referenced 3 times by &8514, &8519, &851e
.c850a
    jsr check_escape                                                  ; 850a: 20 2a 85     *.
.incpx
    lda (net_tx_ptr),y                                                ; 850d: b1 9a       ..
    bmi fs_wait_cleanup                                               ; 850f: 30 0f       0.
    dec l0101,x                                                       ; 8511: de 01 01    ...
    bne c850a                                                         ; 8514: d0 f4       ..
    dec l0102,x                                                       ; 8516: de 02 01    ...
    bne c850a                                                         ; 8519: d0 ef       ..
    dec l0104,x                                                       ; 851b: de 04 01    ...
    bne c850a                                                         ; 851e: d0 ea       ..
; &8520 referenced 1 time by &850f
.fs_wait_cleanup
    pla                                                               ; 8520: 68          h
    pla                                                               ; 8521: 68          h
    pla                                                               ; 8522: 68          h
    sta rx_flags                                                      ; 8523: 8d 64 0d    .d.
    pla                                                               ; 8526: 68          h
    beq c84d4                                                         ; 8527: f0 ab       ..
    rts                                                               ; 8529: 60          `

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
    lda #osbyte_acknowledge_escape                                    ; 852a: a9 7e       .~
    bit l00ff                                                         ; 852c: 24 ff       $.
    bpl return_4                                                      ; 852e: 10 25       .%
    jsr osbyte                                                        ; 8530: 20 f4 ff     ..            ; Clear escape condition and perform escape effects
    lsr a                                                             ; 8533: 4a          J
    sta (net_tx_ptr),y                                                ; 8534: 91 9a       ..
    asl a                                                             ; 8536: 0a          .
    bne nlisne                                                        ; 8537: d0 a1       ..
.bgetv_handler
    sec                                                               ; 8539: 38          8
    jsr handle_bput_bget                                              ; 853a: 20 ed 83     ..            ; Handle BPUT/BGET file byte I/O
    sec                                                               ; 853d: 38          8
    lda #&fe                                                          ; 853e: a9 fe       ..
    bit l0fdf                                                         ; 8540: 2c df 0f    ,..
    bvs return_4                                                      ; 8543: 70 10       p.
    clc                                                               ; 8545: 18          .
    php                                                               ; 8546: 08          .
    lda l00cf                                                         ; 8547: a5 cf       ..
    plp                                                               ; 8549: 28          (
    bmi c854f                                                         ; 854a: 30 03       0.
    jsr clear_fs_flag                                                 ; 854c: 20 60 86     `.
; &854f referenced 1 time by &854a
.c854f
    jsr set_fs_flag                                                   ; 854f: 20 5b 86     [.
    lda l0fde                                                         ; 8552: ad de 0f    ...
; &8555 referenced 2 times by &852e, &8543
.return_4
    rts                                                               ; 8555: 60          `

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
; overlapping: stx os_text_ptr                                        ; 85a5: 86 f2       ..
; &85a5 referenced 3 times by &80c7, &8978, &8bb4
.l85a5
    equb &86                                                          ; 85a5: 86          .
.l85a6
save_fscv_args = l85a6+9
decode_attribs_6bit = l85a6+20
decode_attribs_5bit = l85a6+30
    equs &f2, &84, &f3, &8e, &10, &0e, &8c, &11, &0e, &85, &bd, &86   ; 85a6: f2 84 f3... ...
    equs &bb, &84, &bc, &86, &be, &84, &bf, "`", &a0, &0e, &b1, &bb   ; 85b2: bb 84 bc... ...
    equs ")?", &a2, 4, &d0, 4, ")", &1f, &a2, &ff, &85, &b8, &a9, 0   ; 85be: 29 3f a2... )?.
; overlapping: sty l00f3                                              ; 85a7: 84 f3       ..
; overlapping: stx fs_cmd_ptr                                         ; 85a9: 8e 10 0e    ...
; overlapping: sty l0e11                                              ; 85ac: 8c 11 0e    ...
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
; overlapping: sta fs_last_byte_flag                                  ; 85af: 85 bd       ..
; &85af referenced 2 times by &890c, &8a10
; overlapping: stx fs_options                                         ; 85b1: 86 bb       ..
; overlapping: sty fs_block_offset                                    ; 85b3: 84 bc       ..
; overlapping: stx fs_crc_lo                                          ; 85b5: 86 be       ..
; overlapping: sty fs_crc_hi                                          ; 85b7: 84 bf       ..
; overlapping: rts                                                    ; 85b9: 60          `
; ***************************************************************************************
; Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)
; 
; Reads attribute byte at offset &0E from the parameter block,
; masks to 6 bits, then falls through to the shared bitmask
; builder. Converts fileserver protection format (5-6 bits) to
; BBC OSFILE attribute format (8 bits) via the lookup table at
; &8531. The two formats use different bit layouts for file
; protection attributes.
; ***************************************************************************************
; overlapping: ldy #&0e                                               ; 85ba: a0 0e       ..
; &85ba referenced 2 times by &889f, &88ca
; overlapping: lda (fs_options),y                                     ; 85bc: b1 bb       ..
; overlapping: and #&3f ; '?'                                         ; 85be: 29 3f       )?
; overlapping: ldx #4                                                 ; 85c0: a2 04       ..
; overlapping: bne l85c8                                              ; 85c2: d0 04       ..
; ***************************************************************************************
; Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)
; 
; Masks A to 5 bits and builds an access bitmask via the
; lookup table at &8531. Each input bit position maps to a
; different output bit via the table. The conversion is done
; by iterating through the source bits and OR-ing in the
; corresponding destination bits from the table, translating
; between BBC (8-bit) and fileserver (5-bit) protection formats.
; ***************************************************************************************
; overlapping: and #&1f                                               ; 85c4: 29 1f       ).
; &85c4 referenced 2 times by &87c4, &88e7
; overlapping: ldx #&ff                                               ; 85c6: a2 ff       ..
; overlapping: sta fs_error_ptr                                       ; 85c8: 85 b8       ..
; overlapping: lda #0                                                 ; 85ca: a9 00       ..

; &85cc referenced 1 time by &85d4
.loop_c85cc
    inx                                                               ; 85cc: e8          .
    lsr fs_error_ptr                                                  ; 85cd: 46 b8       F.
    bcc c85d4                                                         ; 85cf: 90 03       ..
    ora access_bit_table,x                                            ; 85d1: 1d d7 85    ...
; &85d4 referenced 1 time by &85cf
.c85d4
    bne loop_c85cc                                                    ; 85d4: d0 f6       ..
    rts                                                               ; 85d6: 60          `

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
    sta fs_load_addr                                                  ; 85e3: 85 b0       ..
    pla                                                               ; 85e5: 68          h              ; Pop return address (high)
    sta fs_load_addr_hi                                               ; 85e6: 85 b1       ..
    ldy #0                                                            ; 85e8: a0 00       ..
; &85ea referenced 1 time by &85f7
.loop_c85ea
    inc fs_load_addr                                                  ; 85ea: e6 b0       ..             ; Advance pointer past return address / to next char
    bne c85f0                                                         ; 85ec: d0 02       ..
    inc fs_load_addr_hi                                               ; 85ee: e6 b1       ..
; &85f0 referenced 1 time by &85ec
.c85f0
    lda (fs_load_addr),y                                              ; 85f0: b1 b0       ..             ; Load next byte from inline string
    bmi c85fa                                                         ; 85f2: 30 06       0.             ; Bit 7 set? Done — this byte is the next opcode
    jsr osasci                                                        ; 85f4: 20 e3 ff     ..            ; Write character
    jmp loop_c85ea                                                    ; 85f7: 4c ea 85    L..

; &85fa referenced 1 time by &85f2
.c85fa
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
;     X: corrupted
;     Y: offset past last digit parsed
; ***************************************************************************************
; &85fd referenced 2 times by &808a, &8090
.parse_decimal
    tax                                                               ; 85fd: aa          .
    lda #0                                                            ; 85fe: a9 00       ..
    sta fs_load_addr_2                                                ; 8600: 85 b2       ..
; &8602 referenced 1 time by &861f
.loop_c8602
    lda (fs_options),y                                                ; 8602: b1 bb       ..
    cmp #&40 ; '@'                                                    ; 8604: c9 40       .@
    bcs c8621                                                         ; 8606: b0 19       ..
    cmp #&2e ; '.'                                                    ; 8608: c9 2e       ..
    beq c8622                                                         ; 860a: f0 16       ..
    bmi c8621                                                         ; 860c: 30 13       0.
    and #&0f                                                          ; 860e: 29 0f       ).
    sta l00b3                                                         ; 8610: 85 b3       ..
    asl fs_load_addr_2                                                ; 8612: 06 b2       ..
    lda fs_load_addr_2                                                ; 8614: a5 b2       ..
    asl a                                                             ; 8616: 0a          .
    asl a                                                             ; 8617: 0a          .
    adc fs_load_addr_2                                                ; 8618: 65 b2       e.
    adc l00b3                                                         ; 861a: 65 b3       e.
    sta fs_load_addr_2                                                ; 861c: 85 b2       ..
    iny                                                               ; 861e: c8          .
    bne loop_c8602                                                    ; 861f: d0 e1       ..
; &8621 referenced 2 times by &8606, &860c
.c8621
    clc                                                               ; 8621: 18          .
; &8622 referenced 1 time by &860a
.c8622
    lda fs_load_addr_2                                                ; 8622: a5 b2       ..
    rts                                                               ; 8624: 60          `

; &8625 referenced 3 times by &8853, &8a2b, &8f4d
.handle_to_mask_a
    tay                                                               ; 8625: a8          .
; &8626 referenced 2 times by &83f8, &8917
.handle_to_mask_clc
    clc                                                               ; 8626: 18          .
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
; Three entry points: &858B (direct), &858A (CLC first), &8589 (TAY first).
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
    pha                                                               ; 8627: 48          H
    txa                                                               ; 8628: 8a          .
    pha                                                               ; 8629: 48          H
    tya                                                               ; 862a: 98          .
    bcc y2fsl5                                                        ; 862b: 90 02       ..
    beq c863e                                                         ; 862d: f0 0f       ..
; &862f referenced 1 time by &862b
.y2fsl5
    sec                                                               ; 862f: 38          8
    sbc #&1f                                                          ; 8630: e9 1f       ..
    tax                                                               ; 8632: aa          .
    lda #1                                                            ; 8633: a9 01       ..
; &8635 referenced 1 time by &8637
.y2fsl2
    asl a                                                             ; 8635: 0a          .
    dex                                                               ; 8636: ca          .
    bne y2fsl2                                                        ; 8637: d0 fc       ..
    ror a                                                             ; 8639: 6a          j
    tay                                                               ; 863a: a8          .
    bne c863e                                                         ; 863b: d0 01       ..
    dey                                                               ; 863d: 88          .
; &863e referenced 2 times by &862d, &863b
.c863e
    pla                                                               ; 863e: 68          h
    tax                                                               ; 863f: aa          .
    pla                                                               ; 8640: 68          h
    rts                                                               ; 8641: 60          `

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
    ldx #&1f                                                          ; 8642: a2 1f       ..
; &8644 referenced 1 time by &8646
.fs2al1
    inx                                                               ; 8644: e8          .
    lsr a                                                             ; 8645: 4a          J
    bne fs2al1                                                        ; 8646: d0 fc       ..
    txa                                                               ; 8648: 8a          .
    rts                                                               ; 8649: 60          `

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
    ldx #4                                                            ; 864a: a2 04       ..
; &864c referenced 1 time by &8653
.loop_c864c
    lda l00af,x                                                       ; 864c: b5 af       ..
    eor l00b3,x                                                       ; 864e: 55 b3       U.
    bne return_compare                                                ; 8650: d0 03       ..
    dex                                                               ; 8652: ca          .
    bne loop_c864c                                                    ; 8653: d0 f7       ..
; &8655 referenced 1 time by &8650
.return_compare
    rts                                                               ; 8655: 60          `

.fscv_read_handles
    ldx #&20 ; ' '                                                    ; 8656: a2 20       .
    ldy #&27 ; '''                                                    ; 8658: a0 27       .'
.return_fscv_handles
    rts                                                               ; 865a: 60          `

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
    ora fs_eof_flags                                                  ; 865b: 0d 07 0e    ...
    bne c8665                                                         ; 865e: d0 05       ..
; ***************************************************************************************
; Clear bit(s) in FS flags (&0E07)
; 
; Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
; the specified bits. Falls through to store the result.
; ***************************************************************************************
; &8660 referenced 3 times by &854c, &886e, &8aa3
.clear_fs_flag
    eor #&ff                                                          ; 8660: 49 ff       I.
    and fs_eof_flags                                                  ; 8662: 2d 07 0e    -..
; &8665 referenced 1 time by &865e
.c8665
    sta fs_eof_flags                                                  ; 8665: 8d 07 0e    ...
    rts                                                               ; 8668: 60          `

; ***************************************************************************************
; Set up TX pointer to control block at &00C0
; 
; Points net_tx_ptr to &00C0 where the TX control block has
; been built by init_tx_ctrl_block. Falls through to tx_poll_ff
; to initiate transmission with full retry.
; ***************************************************************************************
; &8669 referenced 2 times by &83c0, &883b
.setup_tx_ptr_c0
    ldx #&c0                                                          ; 8669: a2 c0       ..
    stx net_tx_ptr                                                    ; 866b: 86 9a       ..
    ldx #0                                                            ; 866d: a2 00       ..
    stx net_tx_ptr_hi                                                 ; 866f: 86 9b       ..
; ***************************************************************************************
; Transmit and poll for result (full retry)
; 
; Sets A=&FF (retry count) and Y=&60 (timeout parameter).
; Falls through to tx_poll_core.
; ***************************************************************************************
; &8671 referenced 4 times by &901f, &9079, &90d0, &926e
.tx_poll_ff
    lda #&ff                                                          ; 8671: a9 ff       ..
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
; Two entry points: setup_tx_ptr_c0 (&8645) always uses the
; standard TXCB; tx_poll_core (&8651) is general-purpose.
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
    pha                                                               ; 8675: 48          H
    tya                                                               ; 8676: 98          .
    pha                                                               ; 8677: 48          H
    ldx #0                                                            ; 8678: a2 00       ..
    lda (net_tx_ptr,x)                                                ; 867a: a1 9a       ..
; &867c referenced 1 time by &86af
.c867c
    sta (net_tx_ptr,x)                                                ; 867c: 81 9a       ..
    pha                                                               ; 867e: 48          H
; &867f referenced 1 time by &8682
.loop_c867f
    asl tx_clear_flag                                                 ; 867f: 0e 62 0d    .b.
    bcc loop_c867f                                                    ; 8682: 90 fb       ..
    lda net_tx_ptr                                                    ; 8684: a5 9a       ..
    sta nmi_tx_block                                                  ; 8686: 85 a0       ..
    lda net_tx_ptr_hi                                                 ; 8688: a5 9b       ..
    sta nmi_tx_block_hi                                               ; 868a: 85 a1       ..
    jsr trampoline_tx_setup                                           ; 868c: 20 60 96     `.
; &868f referenced 1 time by &8691
.l4
    lda (net_tx_ptr,x)                                                ; 868f: a1 9a       ..
    bmi l4                                                            ; 8691: 30 fc       0.
    asl a                                                             ; 8693: 0a          .              ; A=function code (&FF=load, &00=save, &01-&06=attrs)
; ***************************************************************************************
; FILEV handler (OSFILE entry point)
; 
; Saves A/X/Y, copies the filename pointer from the parameter block
; to os_text_ptr, then uses GSINIT/GSREAD (via parse_filename_gs at
; &86C3) to parse the filename into &0E30+. Sets fs_crc_lo/hi to
; point at the parsed filename buffer.
; Dispatches by function code A:
;   A=&FF: load file (send_fs_examine at &86D1)
;   A=&00: save file (filev_save at &8747)
;   A=&01-&06: attribute operations (filev_attrib_dispatch at &8845)
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
    bpl c86b5                                                         ; 8694: 10 1f       ..
    asl a                                                             ; 8696: 0a          .
    beq c86b1                                                         ; 8697: f0 18       ..
    jsr check_escape                                                  ; 8699: 20 2a 85     *.
    pla                                                               ; 869c: 68          h
    tax                                                               ; 869d: aa          .
    pla                                                               ; 869e: 68          h
    tay                                                               ; 869f: a8          .
    pla                                                               ; 86a0: 68          h
    beq c86b1                                                         ; 86a1: f0 0e       ..
    sbc #1                                                            ; 86a3: e9 01       ..
    pha                                                               ; 86a5: 48          H
    tya                                                               ; 86a6: 98          .
    pha                                                               ; 86a7: 48          H
    txa                                                               ; 86a8: 8a          .
; &86a9 referenced 2 times by &86aa, &86ad
.c86a9
    dex                                                               ; 86a9: ca          .
    bne c86a9                                                         ; 86aa: d0 fd       ..
    dey                                                               ; 86ac: 88          .
    bne c86a9                                                         ; 86ad: d0 fa       ..
    beq c867c                                                         ; 86af: f0 cb       ..             ; ALWAYS branch

; &86b1 referenced 2 times by &8697, &86a1
.c86b1
    tax                                                               ; 86b1: aa          .
    jmp nlistn                                                        ; 86b2: 4c d8 84    L..

; &86b5 referenced 1 time by &8694
.c86b5
    pla                                                               ; 86b5: 68          h
    pla                                                               ; 86b6: 68          h
    pla                                                               ; 86b7: 68          h
    rts                                                               ; 86b8: 60          `

    equb &a0, 1                                                       ; 86b9: a0 01       ..
.file1
    equb &b1, &bb, &99, &f2, 0, &88, &10, &f8                         ; 86bb: b1 bb 99... ...

; ***************************************************************************************
; Parse filename using GSINIT/GSREAD into &0E30
; 
; Uses the MOS GSINIT/GSREAD API to parse a filename string from
; (os_text_ptr),Y, handling quoted strings and |-escaped characters.
; Stores the parsed result CR-terminated at &0E30 and sets up
; fs_crc_lo/hi to point to that buffer. Sub-entry at &86C5 allows
; a non-zero starting Y offset.
; Note: the code uses overlapping bytes with send_fs_examine --
; the BCS at &86D0 and the INX/STA at &86D2 share the same bytes
; depending on the entry path.
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
    ldy #0                                                            ; 86c3: a0 00       ..
; &86c5 referenced 1 time by &8c11
.sub_c86c5
    ldx #&ff                                                          ; 86c5: a2 ff       ..
    clc                                                               ; 86c7: 18          .
    jsr gsinit                                                        ; 86c8: 20 c2 ff     ..
    beq c86d8                                                         ; 86cb: f0 0b       ..
; &86cd referenced 1 time by &86d6
.delay_1ms
.quote1
    jsr gsread                                                        ; 86cd: 20 c5 ff     ..
    bcs c86d8                                                         ; 86d0: b0 06       ..
    inx                                                               ; 86d2: e8          .
    sta l0e30,x                                                       ; 86d3: 9d 30 0e    .0.
    bcc delay_1ms                                                     ; 86d6: 90 f5       ..             ; ALWAYS branch

; &86d8 referenced 2 times by &86cb, &86d0
.c86d8
    inx                                                               ; 86d8: e8          .
    lda #&0d                                                          ; 86d9: a9 0d       ..
    sta l0e30,x                                                       ; 86db: 9d 30 0e    .0.
    lda #&30 ; '0'                                                    ; 86de: a9 30       .0
    sta fs_crc_lo                                                     ; 86e0: 85 be       ..
    lda #&0e                                                          ; 86e2: a9 0e       ..
    sta fs_crc_hi                                                     ; 86e4: 85 bf       ..
    rts                                                               ; 86e6: 60          `

    equb &20, &af, &85, &20, &b9, &86, &a5, &bd, &10, &7d, &c9, &ff   ; 86e7: 20 af 85...  ..
    equb &f0,   3, &4c, &57, &89                                      ; 86f3: f0 03 4c... ..L
.loadop
    equb &20, &4b, &8d, &a0, 2                                        ; 86f8: 20 4b 8d...  K.

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
    lda #&92                                                          ; 86fd: a9 92       ..
    sta fs_cmd_urd                                                    ; 86ff: 8d 02 0f    ...
    lda #&2a ; '*'                                                    ; 8702: a9 2a       .*
    jsr prepare_cmd_clv                                               ; 8704: 20 8a 83     ..
    ldy #6                                                            ; 8707: a0 06       ..
    lda (fs_options),y                                                ; 8709: b1 bb       ..
    bne lodfil                                                        ; 870b: d0 08       ..
    jsr copy_load_addr_from_params                                    ; 870d: 20 d6 87     ..
    jsr copy_reply_to_params                                          ; 8710: 20 e8 87     ..
    bcc c871b                                                         ; 8713: 90 06       ..
; &8715 referenced 1 time by &870b
.lodfil
    jsr copy_reply_to_params                                          ; 8715: 20 e8 87     ..
    jsr copy_load_addr_from_params                                    ; 8718: 20 d6 87     ..
; &871b referenced 1 time by &8713
.c871b
    ldy #4                                                            ; 871b: a0 04       ..
; &871d referenced 1 time by &8728
.loop_c871d
    lda fs_load_addr,x                                                ; 871d: b5 b0       ..
    sta l00c8,x                                                       ; 871f: 95 c8       ..
    adc l0f0d,x                                                       ; 8721: 7d 0d 0f    }..
    sta l00b4,x                                                       ; 8724: 95 b4       ..
    inx                                                               ; 8726: e8          .
    dey                                                               ; 8727: 88          .
    bne loop_c871d                                                    ; 8728: d0 f3       ..
    sec                                                               ; 872a: 38          8
    sbc l0f10                                                         ; 872b: ed 10 0f    ...
    sta l00b7                                                         ; 872e: 85 b7       ..
    jsr print_file_info                                               ; 8730: 20 fa 8c     ..
    jsr send_data_blocks                                              ; 8733: 20 43 87     C.
    ldx #2                                                            ; 8736: a2 02       ..
; &8738 referenced 1 time by &873f
.floop
    lda l0f10,x                                                       ; 8738: bd 10 0f    ...
    sta fs_cmd_data,x                                                 ; 873b: 9d 05 0f    ...
    dex                                                               ; 873e: ca          .
    bpl floop                                                         ; 873f: 10 f7       ..
    bmi c87b9                                                         ; 8741: 30 76       0v             ; ALWAYS branch

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
    beq return_lodchk                                                 ; 8746: f0 25       .%
    lda #&92                                                          ; 8748: a9 92       ..
    sta l00c1                                                         ; 874a: 85 c1       ..
; &874c referenced 1 time by &8768
.loop_c874c
    ldx #3                                                            ; 874c: a2 03       ..
; &874e referenced 1 time by &8757
.loop_c874e
    lda l00c8,x                                                       ; 874e: b5 c8       ..
    sta l00c4,x                                                       ; 8750: 95 c4       ..
    lda l00b4,x                                                       ; 8752: b5 b4       ..
    sta l00c8,x                                                       ; 8754: 95 c8       ..
    dex                                                               ; 8756: ca          .
    bpl loop_c874e                                                    ; 8757: 10 f5       ..
    lda #&7f                                                          ; 8759: a9 7f       ..
    sta l00c0                                                         ; 875b: 85 c0       ..
    jsr c84f8                                                         ; 875d: 20 f8 84     ..
    ldy #3                                                            ; 8760: a0 03       ..
; &8762 referenced 1 time by &876b
.lodchk
    lda l00c8,y                                                       ; 8762: b9 c8 00    ...
    eor l00b4,y                                                       ; 8765: 59 b4 00    Y..
    bne loop_c874c                                                    ; 8768: d0 e2       ..
    dey                                                               ; 876a: 88          .
    bpl lodchk                                                        ; 876b: 10 f5       ..
; &876d referenced 1 time by &8746
.return_lodchk
    rts                                                               ; 876d: 60          `

.saveop
    beq filev_save                                                    ; 876e: f0 03       ..
    jmp filev_attrib_dispatch                                         ; 8770: 4c 75 88    Lu.

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
    ldx #4                                                            ; 8773: a2 04       ..
    ldy #&0e                                                          ; 8775: a0 0e       ..
; &8777 referenced 1 time by &8791
.savsiz
    lda (fs_options),y                                                ; 8777: b1 bb       ..
    sta port_ws_offset,y                                              ; 8779: 99 a6 00    ...
    jsr sub_4_from_y                                                  ; 877c: 20 f5 87     ..
    sbc (fs_options),y                                                ; 877f: f1 bb       ..
    sta fs_cmd_csd,y                                                  ; 8781: 99 03 0f    ...
    pha                                                               ; 8784: 48          H
    lda (fs_options),y                                                ; 8785: b1 bb       ..
    sta port_ws_offset,y                                              ; 8787: 99 a6 00    ...
    pla                                                               ; 878a: 68          h
    sta (fs_options),y                                                ; 878b: 91 bb       ..
    jsr add_5_to_y                                                    ; 878d: 20 e2 87     ..
    dex                                                               ; 8790: ca          .
    bne savsiz                                                        ; 8791: d0 e4       ..
    ldy #9                                                            ; 8793: a0 09       ..
; &8795 referenced 1 time by &879b
.loop_c8795
    lda (fs_options),y                                                ; 8795: b1 bb       ..
    sta fs_cmd_csd,y                                                  ; 8797: 99 03 0f    ...
    dey                                                               ; 879a: 88          .
    bne loop_c8795                                                    ; 879b: d0 f8       ..
    lda #&91                                                          ; 879d: a9 91       ..
    sta fs_cmd_urd                                                    ; 879f: 8d 02 0f    ...
    sta fs_error_ptr                                                  ; 87a2: 85 b8       ..
    ldx #&0b                                                          ; 87a4: a2 0b       ..
    jsr copy_string_to_cmd                                            ; 87a6: 20 4d 8d     M.
    ldy #1                                                            ; 87a9: a0 01       ..
    lda #&14                                                          ; 87ab: a9 14       ..
    jsr prepare_cmd_clv                                               ; 87ad: 20 8a 83     ..
    jsr print_file_info                                               ; 87b0: 20 fa 8c     ..
    lda fs_cmd_data                                                   ; 87b3: ad 05 0f    ...
    jsr transfer_file_blocks                                          ; 87b6: 20 fa 87     ..
; &87b9 referenced 1 time by &8741
.c87b9
    jsr send_fs_reply_timed                                           ; 87b9: 20 c6 83     ..
    stx l0f08                                                         ; 87bc: 8e 08 0f    ...
    ldy #&0e                                                          ; 87bf: a0 0e       ..
    lda fs_cmd_data                                                   ; 87c1: ad 05 0f    ...
    jsr decode_attribs_5bit                                           ; 87c4: 20 c4 85     ..
    beq c87cc                                                         ; 87c7: f0 03       ..
; &87c9 referenced 1 time by &87d1
.loop_c87c9
    lda l0ef7,y                                                       ; 87c9: b9 f7 0e    ...
; &87cc referenced 1 time by &87c7
.c87cc
    sta (fs_options),y                                                ; 87cc: 91 bb       ..
    iny                                                               ; 87ce: c8          .
    cpy #&12                                                          ; 87cf: c0 12       ..
    bne loop_c87c9                                                    ; 87d1: d0 f6       ..
    jmp restore_args_return                                           ; 87d3: 4c 57 89    LW.

; ***************************************************************************************
; Copy load address from parameter block
; 
; Copies 4 bytes from (fs_options)+2..5 (the load address in the
; OSFILE parameter block) to &AE-&B3 (local workspace).
; ***************************************************************************************
; &87d6 referenced 2 times by &870d, &8718
.copy_load_addr_from_params
    ldy #5                                                            ; 87d6: a0 05       ..
; &87d8 referenced 1 time by &87e0
.lodrl1
    lda (fs_options),y                                                ; 87d8: b1 bb       ..
    sta l00ae,y                                                       ; 87da: 99 ae 00    ...
    dey                                                               ; 87dd: 88          .
    cpy #2                                                            ; 87de: c0 02       ..
    bcs lodrl1                                                        ; 87e0: b0 f6       ..
; &87e2 referenced 1 time by &878d
.add_5_to_y
    iny                                                               ; 87e2: c8          .
; &87e3 referenced 1 time by &8a73
.add_4_to_y
    iny                                                               ; 87e3: c8          .
    iny                                                               ; 87e4: c8          .
    iny                                                               ; 87e5: c8          .
    iny                                                               ; 87e6: c8          .
    rts                                                               ; 87e7: 60          `

; ***************************************************************************************
; Copy FS reply data to parameter block
; 
; Copies bytes from the FS command reply buffer (&0F02+) into the
; parameter block at (fs_options)+2..13. Used to fill in the OSFILE
; parameter block with information returned by the fileserver.
; ***************************************************************************************
; &87e8 referenced 2 times by &8710, &8715
.copy_reply_to_params
    ldy #&0d                                                          ; 87e8: a0 0d       ..
    txa                                                               ; 87ea: 8a          .
; &87eb referenced 1 time by &87f3
.lodrl2
    sta (fs_options),y                                                ; 87eb: 91 bb       ..
    lda fs_cmd_urd,y                                                  ; 87ed: b9 02 0f    ...
    dey                                                               ; 87f0: 88          .
    cpy #2                                                            ; 87f1: c0 02       ..
    bcs lodrl2                                                        ; 87f3: b0 f6       ..
; &87f5 referenced 1 time by &877c
.sub_4_from_y
    dey                                                               ; 87f5: 88          .
; &87f6 referenced 2 times by &888d, &8a7b
.sub_3_from_y
    dey                                                               ; 87f6: 88          .
    dey                                                               ; 87f7: 88          .
    dey                                                               ; 87f8: 88          .
    rts                                                               ; 87f9: 60          `

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
    pha                                                               ; 87fa: 48          H
    jsr compare_addresses                                             ; 87fb: 20 4a 86     J.            ; Compare two 4-byte addresses
    beq c8871                                                         ; 87fe: f0 71       .q
; &8800 referenced 1 time by &884f
.c8800
    ldx #0                                                            ; 8800: a2 00       ..
    ldy #4                                                            ; 8802: a0 04       ..
    stx l0f08                                                         ; 8804: 8e 08 0f    ...
    stx l0f09                                                         ; 8807: 8e 09 0f    ...
    clc                                                               ; 880a: 18          .
; &880b referenced 1 time by &8818
.loop_c880b
    lda fs_load_addr,x                                                ; 880b: b5 b0       ..
    sta l00c4,x                                                       ; 880d: 95 c4       ..
    adc l0f06,x                                                       ; 880f: 7d 06 0f    }..
    sta l00c8,x                                                       ; 8812: 95 c8       ..
    sta fs_load_addr,x                                                ; 8814: 95 b0       ..
    inx                                                               ; 8816: e8          .
    dey                                                               ; 8817: 88          .
    bne loop_c880b                                                    ; 8818: d0 f1       ..
    bcs c8829                                                         ; 881a: b0 0d       ..
    sec                                                               ; 881c: 38          8
; &881d referenced 1 time by &8825
.savchk
    lda fs_load_addr,y                                                ; 881d: b9 b0 00    ...
    sbc l00b4,y                                                       ; 8820: f9 b4 00    ...
    iny                                                               ; 8823: c8          .
    dex                                                               ; 8824: ca          .
    bne savchk                                                        ; 8825: d0 f6       ..
    bcc c8832                                                         ; 8827: 90 09       ..
; &8829 referenced 1 time by &881a
.c8829
    ldx #3                                                            ; 8829: a2 03       ..
; &882b referenced 1 time by &8830
.loop_c882b
    lda l00b4,x                                                       ; 882b: b5 b4       ..
    sta l00c8,x                                                       ; 882d: 95 c8       ..
    dex                                                               ; 882f: ca          .
    bpl loop_c882b                                                    ; 8830: 10 f9       ..
; &8832 referenced 1 time by &8827
.c8832
    pla                                                               ; 8832: 68          h
    pha                                                               ; 8833: 48          H
    php                                                               ; 8834: 08          .
    sta l00c1                                                         ; 8835: 85 c1       ..
    lda #&80                                                          ; 8837: a9 80       ..
    sta l00c0                                                         ; 8839: 85 c0       ..
    jsr setup_tx_ptr_c0                                               ; 883b: 20 69 86     i.
    lda fs_error_ptr                                                  ; 883e: a5 b8       ..
    jsr init_tx_ctrl_port                                             ; 8840: 20 54 83     T.
    plp                                                               ; 8843: 28          (
    bcs c8871                                                         ; 8844: b0 2b       .+
    lda #&91                                                          ; 8846: a9 91       ..
    sta l00c1                                                         ; 8848: 85 c1       ..
    lda #&2a ; '*'                                                    ; 884a: a9 2a       .*
    jsr send_to_fs                                                    ; 884c: 20 fa 84     ..
    bne c8800                                                         ; 884f: d0 af       ..
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
    pha                                                               ; 8851: 48          H
    txa                                                               ; 8852: 8a          .
    jsr handle_to_mask_a                                              ; 8853: 20 25 86     %.
    tya                                                               ; 8856: 98          .
    and fs_eof_flags                                                  ; 8857: 2d 07 0e    -..
    tax                                                               ; 885a: aa          .
    beq c8871                                                         ; 885b: f0 14       ..
    pha                                                               ; 885d: 48          H
    sty fs_cmd_data                                                   ; 885e: 8c 05 0f    ...
    ldy #&11                                                          ; 8861: a0 11       ..             ; Y=function code for HDRFN
    ldx #1                                                            ; 8863: a2 01       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8865: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    pla                                                               ; 8868: 68          h
    ldx fs_cmd_data                                                   ; 8869: ae 05 0f    ...
    bne c8871                                                         ; 886c: d0 03       ..
    jsr clear_fs_flag                                                 ; 886e: 20 60 86     `.
; &8871 referenced 4 times by &87fe, &8844, &885b, &886c
.c8871
    pla                                                               ; 8871: 68          h
    ldy fs_block_offset                                               ; 8872: a4 bc       ..
    rts                                                               ; 8874: 60          `

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
    sta fs_cmd_data                                                   ; 8875: 8d 05 0f    ...
    cmp #6                                                            ; 8878: c9 06       ..
    beq cha6                                                          ; 887a: f0 3f       .?
    bcs c88c6                                                         ; 887c: b0 48       .H
    cmp #5                                                            ; 887e: c9 05       ..
    beq cha5                                                          ; 8880: f0 52       .R
    cmp #4                                                            ; 8882: c9 04       ..
    beq cha4                                                          ; 8884: f0 44       .D
    cmp #1                                                            ; 8886: c9 01       ..
    beq get_file_protection                                           ; 8888: f0 15       ..
    asl a                                                             ; 888a: 0a          .
    asl a                                                             ; 888b: 0a          .
    tay                                                               ; 888c: a8          .
    jsr sub_3_from_y                                                  ; 888d: 20 f6 87     ..
    ldx #3                                                            ; 8890: a2 03       ..
; &8892 referenced 1 time by &8899
.chalp1
    lda (fs_options),y                                                ; 8892: b1 bb       ..
    sta l0f06,x                                                       ; 8894: 9d 06 0f    ...
    dey                                                               ; 8897: 88          .
    dex                                                               ; 8898: ca          .
    bpl chalp1                                                        ; 8899: 10 f7       ..
    ldx #5                                                            ; 889b: a2 05       ..
    bne copy_filename_to_cmd                                          ; 889d: d0 15       ..             ; ALWAYS branch

; &889f referenced 1 time by &8888
.get_file_protection
    jsr decode_attribs_6bit                                           ; 889f: 20 ba 85     ..
    sta l0f0e                                                         ; 88a2: 8d 0e 0f    ...
    ldy #9                                                            ; 88a5: a0 09       ..
    ldx #8                                                            ; 88a7: a2 08       ..
; &88a9 referenced 1 time by &88b0
.chalp2
    lda (fs_options),y                                                ; 88a9: b1 bb       ..
    sta fs_cmd_data,x                                                 ; 88ab: 9d 05 0f    ...
    dey                                                               ; 88ae: 88          .
    dex                                                               ; 88af: ca          .
    bne chalp2                                                        ; 88b0: d0 f7       ..
    ldx #&0a                                                          ; 88b2: a2 0a       ..
; &88b4 referenced 2 times by &889d, &88d2
.copy_filename_to_cmd
    jsr copy_string_to_cmd                                            ; 88b4: 20 4d 8d     M.
    ldy #&13                                                          ; 88b7: a0 13       ..
    bne c88c0                                                         ; 88b9: d0 05       ..             ; ALWAYS branch

; &88bb referenced 1 time by &887a
.cha6
    jsr copy_filename                                                 ; 88bb: 20 4b 8d     K.
    ldy #&14                                                          ; 88be: a0 14       ..
; &88c0 referenced 1 time by &88b9
.c88c0
    bit l837e                                                         ; 88c0: 2c 7e 83    ,~.
    jsr init_tx_ctrl_data                                             ; 88c3: 20 95 83     ..
; &88c6 referenced 1 time by &887c
.c88c6
    bcs c890a                                                         ; 88c6: b0 42       .B
    bcc c893b                                                         ; 88c8: 90 71       .q             ; ALWAYS branch

; &88ca referenced 1 time by &8884
.cha4
    jsr decode_attribs_6bit                                           ; 88ca: 20 ba 85     ..
    sta l0f06                                                         ; 88cd: 8d 06 0f    ...
    ldx #2                                                            ; 88d0: a2 02       ..
    bne copy_filename_to_cmd                                          ; 88d2: d0 e0       ..             ; ALWAYS branch

; &88d4 referenced 1 time by &8880
.cha5
    ldx #1                                                            ; 88d4: a2 01       ..
    jsr copy_string_to_cmd                                            ; 88d6: 20 4d 8d     M.
    ldy #&12                                                          ; 88d9: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 88db: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda l0f11                                                         ; 88de: ad 11 0f    ...
    stx l0f11                                                         ; 88e1: 8e 11 0f    ...            ; X=0 on success, &D6 on not-found
    stx l0f14                                                         ; 88e4: 8e 14 0f    ...
    jsr decode_attribs_5bit                                           ; 88e7: 20 c4 85     ..
    ldy #&0e                                                          ; 88ea: a0 0e       ..
    sta (fs_options),y                                                ; 88ec: 91 bb       ..
    dey                                                               ; 88ee: 88          .              ; Y=&0d
    ldx #&0c                                                          ; 88ef: a2 0c       ..
; &88f1 referenced 1 time by &88f8
.copy_fs_reply_to_cb
    lda fs_cmd_data,x                                                 ; 88f1: bd 05 0f    ...
    sta (fs_options),y                                                ; 88f4: 91 bb       ..
    dey                                                               ; 88f6: 88          .
    dex                                                               ; 88f7: ca          .
    bne copy_fs_reply_to_cb                                           ; 88f8: d0 f7       ..
    inx                                                               ; 88fa: e8          .
    inx                                                               ; 88fb: e8          .
    ldy #&11                                                          ; 88fc: a0 11       ..
; &88fe referenced 1 time by &8905
.cha5lp
    lda l0f12,x                                                       ; 88fe: bd 12 0f    ...
    sta (fs_options),y                                                ; 8901: 91 bb       ..
    dey                                                               ; 8903: 88          .
    dex                                                               ; 8904: ca          .
    bpl cha5lp                                                        ; 8905: 10 f7       ..
    lda fs_cmd_data                                                   ; 8907: ad 05 0f    ...
; &890a referenced 1 time by &88c6
.c890a
    bpl c8959                                                         ; 890a: 10 4d       .M
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
    jsr save_fscv_args                                                ; 890c: 20 af 85     ..
    cmp #3                                                            ; 890f: c9 03       ..
    bcs restore_args_return                                           ; 8911: b0 44       .D
    cpy #0                                                            ; 8913: c0 00       ..
    beq c895e                                                         ; 8915: f0 47       .G
    jsr handle_to_mask_clc                                            ; 8917: 20 26 86     &.
    sty fs_cmd_data                                                   ; 891a: 8c 05 0f    ...
    lsr a                                                             ; 891d: 4a          J
    sta l0f06                                                         ; 891e: 8d 06 0f    ...
    bcs save_args_handle                                              ; 8921: b0 1a       ..
    ldy #&0c                                                          ; 8923: a0 0c       ..             ; Y=function code for HDRFN
    ldx #2                                                            ; 8925: a2 02       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 8927: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    sta fs_last_byte_flag                                             ; 892a: 85 bd       ..             ; A=0 on success (from build_send_fs_cmd)
    ldx fs_options                                                    ; 892c: a6 bb       ..
    ldy #2                                                            ; 892e: a0 02       ..
    sta l0003,x                                                       ; 8930: 95 03       ..
; &8932 referenced 1 time by &8939
.loop_c8932
    lda fs_cmd_data,y                                                 ; 8932: b9 05 0f    ...
    sta l0002,x                                                       ; 8935: 95 02       ..
    dex                                                               ; 8937: ca          .
    dey                                                               ; 8938: 88          .
    bpl loop_c8932                                                    ; 8939: 10 f7       ..
; &893b referenced 1 time by &88c8
.c893b
    bcc restore_args_return                                           ; 893b: 90 1a       ..
; &893d referenced 1 time by &8921
.save_args_handle
    tya                                                               ; 893d: 98          .
    pha                                                               ; 893e: 48          H
    ldy #3                                                            ; 893f: a0 03       ..
; &8941 referenced 1 time by &8948
.loop_c8941
    lda l0003,x                                                       ; 8941: b5 03       ..
    sta l0f07,y                                                       ; 8943: 99 07 0f    ...
    dex                                                               ; 8946: ca          .
    dey                                                               ; 8947: 88          .
    bpl loop_c8941                                                    ; 8948: 10 f7       ..
    ldy #&0d                                                          ; 894a: a0 0d       ..             ; Y=function code for HDRFN
    ldx #5                                                            ; 894c: a2 05       ..             ; X=preserved through header build
    jsr prepare_fs_cmd                                                ; 894e: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_last_byte_flag                                             ; 8951: 86 bd       ..             ; X=0 on success, &D6 on not-found
    pla                                                               ; 8953: 68          h
    jsr set_fs_flag                                                   ; 8954: 20 5b 86     [.
; ***************************************************************************************
; Restore arguments and return
; 
; Common exit point for FS vector handlers. Reloads A from
; fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
; fs_block_offset (&BC) — the values saved at entry by
; save_fscv_args — and returns to the caller.
; ***************************************************************************************
; &8957 referenced 6 times by &87d3, &8911, &893b, &89ca, &8a1b, &8e25
.restore_args_return
    lda fs_last_byte_flag                                             ; 8957: a5 bd       ..
; &8959 referenced 5 times by &890a, &896a, &8976, &89a1, &89ae
.c8959
    ldx fs_options                                                    ; 8959: a6 bb       ..
    ldy fs_block_offset                                               ; 895b: a4 bc       ..
    rts                                                               ; 895d: 60          `

; &895e referenced 1 time by &8915
.c895e
    cmp #2                                                            ; 895e: c9 02       ..
    beq c8969                                                         ; 8960: f0 07       ..
    bcs c8974                                                         ; 8962: b0 10       ..
    tay                                                               ; 8964: a8          .
    bne osarg1                                                        ; 8965: d0 05       ..
    lda #&0a                                                          ; 8967: a9 0a       ..
; &8969 referenced 1 time by &8960
.c8969
    lsr a                                                             ; 8969: 4a          J
    bne c8959                                                         ; 896a: d0 ed       ..
; &896c referenced 2 times by &8965, &8972
.osarg1
    lda fs_cmd_context,y                                              ; 896c: b9 0a 0e    ...
    sta (fs_options),y                                                ; 896f: 91 bb       ..
    dey                                                               ; 8971: 88          .
    bpl osarg1                                                        ; 8972: 10 f8       ..
; &8974 referenced 4 times by &8962, &8984, &8ab7, &8b54
.c8974
    lda #0                                                            ; 8974: a9 00       ..             ; A=operation (0=close, &40=read, &80=write, &C0=R/W)
    bpl c8959                                                         ; 8976: 10 e1       ..             ; ALWAYS branch

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
    jsr l85a5                                                         ; 8978: 20 a5 85     ..
    sec                                                               ; 897b: 38          8
    jsr handle_to_mask                                                ; 897c: 20 27 86     '.            ; Convert file handle to bitmask (Y2FS)
    tax                                                               ; 897f: aa          .              ; A=preserved
    beq close_handle                                                  ; 8980: f0 2e       ..
    and #&3f ; '?'                                                    ; 8982: 29 3f       )?
    bne c8974                                                         ; 8984: d0 ee       ..
    txa                                                               ; 8986: 8a          .
    eor #&80                                                          ; 8987: 49 80       I.
    asl a                                                             ; 8989: 0a          .
    sta fs_cmd_data                                                   ; 898a: 8d 05 0f    ...
    rol a                                                             ; 898d: 2a          *
    sta l0f06                                                         ; 898e: 8d 06 0f    ...
    jsr parse_filename_gs                                             ; 8991: 20 c3 86     ..
    ldx #2                                                            ; 8994: a2 02       ..
    jsr copy_string_to_cmd                                            ; 8996: 20 4d 8d     M.
    ldy #6                                                            ; 8999: a0 06       ..
    bit l837e                                                         ; 899b: 2c 7e 83    ,~.
    jsr init_tx_ctrl_data                                             ; 899e: 20 95 83     ..
    bcs c8959                                                         ; 89a1: b0 b6       ..
    lda fs_cmd_data                                                   ; 89a3: ad 05 0f    ...
    tax                                                               ; 89a6: aa          .
    jsr set_fs_flag                                                   ; 89a7: 20 5b 86     [.
    txa                                                               ; 89aa: 8a          .              ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 89ab: 20 42 86     B.            ; Convert bitmask to handle number (FS2A)
    bne c8959                                                         ; 89ae: d0 a9       ..
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
    tya                                                               ; 89b0: 98          .              ; Y=preserved
    bne close_single_handle                                           ; 89b1: d0 07       ..
    lda #osbyte_close_spool_exec                                      ; 89b3: a9 77       .w
    jsr osbyte                                                        ; 89b5: 20 f4 ff     ..            ; Close any *SPOOL and *EXEC files
    ldy #0                                                            ; 89b8: a0 00       ..
; &89ba referenced 1 time by &89b1
.close_single_handle
    sty fs_cmd_data                                                   ; 89ba: 8c 05 0f    ...
    ldx #1                                                            ; 89bd: a2 01       ..             ; X=preserved through header build
    ldy #7                                                            ; 89bf: a0 07       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89c1: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 89c4: ad 05 0f    ...
    jsr set_fs_flag                                                   ; 89c7: 20 5b 86     [.
; &89ca referenced 1 time by &89ee
.c89ca
    bcc restore_args_return                                           ; 89ca: 90 8b       ..
; ***************************************************************************************
; FSCV 0: *OPT handler (OPTION)
; 
; Handles *OPT X,Y to set filing system options:
;   *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
;   *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
; Other combinations generate error &CB (OPTER: "bad option").
; ***************************************************************************************
.opt_handler
    cpx #4                                                            ; 89cc: e0 04       ..
    bne c89d4                                                         ; 89ce: d0 04       ..
    cpy #4                                                            ; 89d0: c0 04       ..
    bcc optl1                                                         ; 89d2: 90 0d       ..
; &89d4 referenced 1 time by &89ce
.c89d4
    dex                                                               ; 89d4: ca          .
    bne opter1                                                        ; 89d5: d0 05       ..
    sty fs_messages_flag                                              ; 89d7: 8c 06 0e    ...
    bcc c89ee                                                         ; 89da: 90 12       ..
; &89dc referenced 1 time by &89d5
.opter1
    lda #7                                                            ; 89dc: a9 07       ..
    jmp nlisne                                                        ; 89de: 4c da 84    L..

; &89e1 referenced 1 time by &89d2
.optl1
    sty fs_cmd_data                                                   ; 89e1: 8c 05 0f    ...
    ldy #&16                                                          ; 89e4: a0 16       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 89e6: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    ldy fs_block_offset                                               ; 89e9: a4 bc       ..
    sty fs_boot_option                                                ; 89eb: 8c 05 0e    ...
; &89ee referenced 1 time by &89da
.c89ee
    bcc c89ca                                                         ; 89ee: 90 da       ..
; &89f0 referenced 1 time by &8aab
.adjust_addrs_9
    ldy #9                                                            ; 89f0: a0 09       ..
    jsr adjust_addrs_clc                                              ; 89f2: 20 f7 89     ..
; &89f5 referenced 1 time by &8b9b
.adjust_addrs_1
    ldy #1                                                            ; 89f5: a0 01       ..
; &89f7 referenced 1 time by &89f2
.adjust_addrs_clc
    clc                                                               ; 89f7: 18          .
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
    ldx #&fc                                                          ; 89f8: a2 fc       ..
; &89fa referenced 1 time by &8a0d
.loop_c89fa
    lda (fs_options),y                                                ; 89fa: b1 bb       ..
    bit fs_load_addr_2                                                ; 89fc: 24 b2       $.
    bmi c8a06                                                         ; 89fe: 30 06       0.
    adc fs_cmd_context,x                                              ; 8a00: 7d 0a 0e    }..
    jmp gbpbx                                                         ; 8a03: 4c 09 8a    L..

; &8a06 referenced 1 time by &89fe
.c8a06
    sbc fs_cmd_context,x                                              ; 8a06: fd 0a 0e    ...
; &8a09 referenced 1 time by &8a03
.gbpbx
    sta (fs_options),y                                                ; 8a09: 91 bb       ..
    iny                                                               ; 8a0b: c8          .
    inx                                                               ; 8a0c: e8          .
    bne loop_c89fa                                                    ; 8a0d: d0 eb       ..
    rts                                                               ; 8a0f: 60          `

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
    jsr save_fscv_args                                                ; 8a10: 20 af 85     ..
    tax                                                               ; 8a13: aa          .
    beq c8a1b                                                         ; 8a14: f0 05       ..
    dex                                                               ; 8a16: ca          .
    cpx #8                                                            ; 8a17: e0 08       ..
    bcc gbpbx1                                                        ; 8a19: 90 03       ..
; &8a1b referenced 1 time by &8a14
.c8a1b
    jmp restore_args_return                                           ; 8a1b: 4c 57 89    LW.

; &8a1e referenced 1 time by &8a19
.gbpbx1
    txa                                                               ; 8a1e: 8a          .
    ldy #0                                                            ; 8a1f: a0 00       ..
    pha                                                               ; 8a21: 48          H
    cmp #4                                                            ; 8a22: c9 04       ..
    bcc gbpbe1                                                        ; 8a24: 90 03       ..
    jmp osgbpb_info                                                   ; 8a26: 4c cf 8a    L..

; &8a29 referenced 1 time by &8a24
.gbpbe1
    lda (fs_options),y                                                ; 8a29: b1 bb       ..
    jsr handle_to_mask_a                                              ; 8a2b: 20 25 86     %.
    sty fs_cmd_data                                                   ; 8a2e: 8c 05 0f    ...
    ldy #&0b                                                          ; 8a31: a0 0b       ..
    ldx #6                                                            ; 8a33: a2 06       ..
; &8a35 referenced 1 time by &8a41
.gbpbf1
    lda (fs_options),y                                                ; 8a35: b1 bb       ..
    sta l0f06,x                                                       ; 8a37: 9d 06 0f    ...
    dey                                                               ; 8a3a: 88          .
    cpy #8                                                            ; 8a3b: c0 08       ..
    bne gbpbx0                                                        ; 8a3d: d0 01       ..
    dey                                                               ; 8a3f: 88          .
; &8a40 referenced 1 time by &8a3d
.gbpbx0
.gbpbf2
    dex                                                               ; 8a40: ca          .
    bne gbpbf1                                                        ; 8a41: d0 f2       ..
    pla                                                               ; 8a43: 68          h
    lsr a                                                             ; 8a44: 4a          J
    pha                                                               ; 8a45: 48          H
    bcc gbpbl1                                                        ; 8a46: 90 01       ..
    inx                                                               ; 8a48: e8          .
; &8a49 referenced 1 time by &8a46
.gbpbl1
    stx l0f06                                                         ; 8a49: 8e 06 0f    ...
    ldy #&0b                                                          ; 8a4c: a0 0b       ..
    ldx #&91                                                          ; 8a4e: a2 91       ..
    pla                                                               ; 8a50: 68          h
    pha                                                               ; 8a51: 48          H
    beq c8a57                                                         ; 8a52: f0 03       ..
    ldx #&92                                                          ; 8a54: a2 92       ..
    dey                                                               ; 8a56: 88          .              ; Y=&0a
; &8a57 referenced 1 time by &8a52
.c8a57
    stx fs_cmd_urd                                                    ; 8a57: 8e 02 0f    ...
    stx fs_error_ptr                                                  ; 8a5a: 86 b8       ..
    ldx #8                                                            ; 8a5c: a2 08       ..
    lda fs_cmd_data                                                   ; 8a5e: ad 05 0f    ...
    jsr prepare_cmd_with_flag                                         ; 8a61: 20 84 83     ..
    lda l00b3                                                         ; 8a64: a5 b3       ..
    sta fs_sequence_nos                                               ; 8a66: 8d 08 0e    ...
    ldx #4                                                            ; 8a69: a2 04       ..
; &8a6b referenced 1 time by &8a7f
.gbpbl3
    lda (fs_options),y                                                ; 8a6b: b1 bb       ..
    sta l00af,y                                                       ; 8a6d: 99 af 00    ...
    sta l00c7,y                                                       ; 8a70: 99 c7 00    ...
    jsr add_4_to_y                                                    ; 8a73: 20 e3 87     ..
    adc (fs_options),y                                                ; 8a76: 71 bb       q.
    sta l00af,y                                                       ; 8a78: 99 af 00    ...
    jsr sub_3_from_y                                                  ; 8a7b: 20 f6 87     ..
    dex                                                               ; 8a7e: ca          .
    bne gbpbl3                                                        ; 8a7f: d0 ea       ..
    inx                                                               ; 8a81: e8          .
; &8a82 referenced 1 time by &8a89
.gbpbf3
    lda fs_cmd_csd,x                                                  ; 8a82: bd 03 0f    ...
    sta l0f06,x                                                       ; 8a85: 9d 06 0f    ...
    dex                                                               ; 8a88: ca          .
    bpl gbpbf3                                                        ; 8a89: 10 f7       ..
    pla                                                               ; 8a8b: 68          h
    bne c8a96                                                         ; 8a8c: d0 08       ..
    lda fs_cmd_urd                                                    ; 8a8e: ad 02 0f    ...
    jsr transfer_file_blocks                                          ; 8a91: 20 fa 87     ..
    bne c8a99                                                         ; 8a94: d0 03       ..
; &8a96 referenced 1 time by &8a8c
.c8a96
    jsr send_data_blocks                                              ; 8a96: 20 43 87     C.
; &8a99 referenced 1 time by &8a94
.c8a99
    jsr send_fs_reply_timed                                           ; 8a99: 20 c6 83     ..
    lda (fs_options,x)                                                ; 8a9c: a1 bb       ..
    bit fs_cmd_data                                                   ; 8a9e: 2c 05 0f    ,..
    bmi c8aa6                                                         ; 8aa1: 30 03       0.
    jsr clear_fs_flag                                                 ; 8aa3: 20 60 86     `.
; &8aa6 referenced 1 time by &8aa1
.c8aa6
    jsr set_fs_flag                                                   ; 8aa6: 20 5b 86     [.
    stx fs_load_addr_2                                                ; 8aa9: 86 b2       ..
    jsr adjust_addrs_9                                                ; 8aab: 20 f0 89     ..
    dec fs_load_addr_2                                                ; 8aae: c6 b2       ..
    sec                                                               ; 8ab0: 38          8
    jsr adjust_addrs                                                  ; 8ab1: 20 f8 89     ..
    asl fs_cmd_data                                                   ; 8ab4: 0e 05 0f    ...
    jmp c8974                                                         ; 8ab7: 4c 74 89    Lt.

; &8aba referenced 1 time by &8aea
.c8aba
    ldy #&15                                                          ; 8aba: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8abc: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_boot_option                                                ; 8abf: ad 05 0e    ...
    sta l0f16                                                         ; 8ac2: 8d 16 0f    ...
    stx fs_load_addr                                                  ; 8ac5: 86 b0       ..             ; X=0 on success, &D6 on not-found
    stx fs_load_addr_hi                                               ; 8ac7: 86 b1       ..
    lda #&12                                                          ; 8ac9: a9 12       ..
    sta fs_load_addr_2                                                ; 8acb: 85 b2       ..
    bne copy_reply_to_caller                                          ; 8acd: d0 4e       .N             ; ALWAYS branch

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
    ldy #4                                                            ; 8acf: a0 04       ..
    lda tx_in_progress                                                ; 8ad1: ad 52 0d    .R.
    beq c8add                                                         ; 8ad4: f0 07       ..
    cmp (fs_options),y                                                ; 8ad6: d1 bb       ..
    bne c8add                                                         ; 8ad8: d0 03       ..
    dey                                                               ; 8ada: 88          .              ; Y=&03
    sbc (fs_options),y                                                ; 8adb: f1 bb       ..
; &8add referenced 2 times by &8ad4, &8ad8
.c8add
    sta rom_svc_num                                                   ; 8add: 85 a9       ..
; &8adf referenced 1 time by &8ae5
.info2
    lda (fs_options),y                                                ; 8adf: b1 bb       ..
    sta fs_last_byte_flag,y                                           ; 8ae1: 99 bd 00    ...
    dey                                                               ; 8ae4: 88          .
    bne info2                                                         ; 8ae5: d0 f8       ..
    pla                                                               ; 8ae7: 68          h
    and #3                                                            ; 8ae8: 29 03       ).
    beq c8aba                                                         ; 8aea: f0 ce       ..
    lsr a                                                             ; 8aec: 4a          J
    beq c8af1                                                         ; 8aed: f0 02       ..
    bcs c8b57                                                         ; 8aef: b0 66       .f
; &8af1 referenced 1 time by &8aed
.c8af1
    tay                                                               ; 8af1: a8          .              ; Y=function code
    lda fs_csd_handle,y                                               ; 8af2: b9 03 0e    ...
    sta fs_cmd_csd                                                    ; 8af5: 8d 03 0f    ...
    lda fs_lib_handle                                                 ; 8af8: ad 04 0e    ...
    sta fs_cmd_lib                                                    ; 8afb: 8d 04 0f    ...
    lda fs_urd_handle                                                 ; 8afe: ad 02 0e    ...
    sta fs_cmd_urd                                                    ; 8b01: 8d 02 0f    ...
    ldx #&12                                                          ; 8b04: a2 12       ..             ; X=buffer extent (command-specific data bytes)
    stx fs_cmd_y_param                                                ; 8b06: 8e 01 0f    ...
    lda #&0d                                                          ; 8b09: a9 0d       ..
    sta l0f06                                                         ; 8b0b: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b0e: 85 b2       ..
    lsr a                                                             ; 8b10: 4a          J              ; A=timeout period for FS reply
    sta fs_cmd_data                                                   ; 8b11: 8d 05 0f    ...
    clc                                                               ; 8b14: 18          .
    jsr build_send_fs_cmd                                             ; 8b15: 20 ae 83     ..            ; Build and send FS command (DOFSOP)
    stx fs_load_addr_hi                                               ; 8b18: 86 b1       ..             ; X=0 on success, &D6 on not-found
    inx                                                               ; 8b1a: e8          .
    stx fs_load_addr                                                  ; 8b1b: 86 b0       ..
; &8b1d referenced 2 times by &8acd, &8b90
.copy_reply_to_caller
    lda rom_svc_num                                                   ; 8b1d: a5 a9       ..
    bne c8b32                                                         ; 8b1f: d0 11       ..
    ldx fs_load_addr                                                  ; 8b21: a6 b0       ..
    ldy fs_load_addr_hi                                               ; 8b23: a4 b1       ..
; &8b25 referenced 1 time by &8b2e
.loop_c8b25
    lda fs_cmd_data,x                                                 ; 8b25: bd 05 0f    ...
    sta (fs_crc_lo),y                                                 ; 8b28: 91 be       ..
    inx                                                               ; 8b2a: e8          .
    iny                                                               ; 8b2b: c8          .
    dec fs_load_addr_2                                                ; 8b2c: c6 b2       ..
    bne loop_c8b25                                                    ; 8b2e: d0 f5       ..
    beq c8b54                                                         ; 8b30: f0 22       ."             ; ALWAYS branch

; &8b32 referenced 1 time by &8b1f
.c8b32
    jsr tube_claim_loop                                               ; 8b32: 20 ac 8b     ..
    lda #1                                                            ; 8b35: a9 01       ..
    ldx fs_options                                                    ; 8b37: a6 bb       ..
    ldy fs_block_offset                                               ; 8b39: a4 bc       ..
    inx                                                               ; 8b3b: e8          .
    bne c8b3f                                                         ; 8b3c: d0 01       ..
    iny                                                               ; 8b3e: c8          .
; &8b3f referenced 1 time by &8b3c
.c8b3f
    jsr tube_addr_claim                                               ; 8b3f: 20 06 04     ..
    ldx fs_load_addr                                                  ; 8b42: a6 b0       ..
; &8b44 referenced 1 time by &8b4d
.tbcop1
    lda fs_cmd_data,x                                                 ; 8b44: bd 05 0f    ...
    sta tube_data_register_3                                          ; 8b47: 8d e5 fe    ...
    inx                                                               ; 8b4a: e8          .
    dec fs_load_addr_2                                                ; 8b4b: c6 b2       ..
    bne tbcop1                                                        ; 8b4d: d0 f5       ..
    lda #&83                                                          ; 8b4f: a9 83       ..
    jsr tube_addr_claim                                               ; 8b51: 20 06 04     ..
; &8b54 referenced 2 times by &8b30, &8baa
.c8b54
    jmp c8974                                                         ; 8b54: 4c 74 89    Lt.

; &8b57 referenced 1 time by &8aef
.c8b57
    ldy #9                                                            ; 8b57: a0 09       ..
    lda (fs_options),y                                                ; 8b59: b1 bb       ..
    sta l0f06                                                         ; 8b5b: 8d 06 0f    ...
    ldy #5                                                            ; 8b5e: a0 05       ..
    lda (fs_options),y                                                ; 8b60: b1 bb       ..
    sta l0f07                                                         ; 8b62: 8d 07 0f    ...
    ldx #&0d                                                          ; 8b65: a2 0d       ..             ; X=preserved through header build
    stx l0f08                                                         ; 8b67: 8e 08 0f    ...
    ldy #2                                                            ; 8b6a: a0 02       ..
    sty fs_load_addr                                                  ; 8b6c: 84 b0       ..
    sty fs_cmd_data                                                   ; 8b6e: 8c 05 0f    ...
    iny                                                               ; 8b71: c8          .              ; Y=function code for HDRFN; Y=&03
    jsr prepare_fs_cmd                                                ; 8b72: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    stx fs_load_addr_hi                                               ; 8b75: 86 b1       ..             ; X=0 on success, &D6 on not-found
    lda l0f06                                                         ; 8b77: ad 06 0f    ...
    sta (fs_options,x)                                                ; 8b7a: 81 bb       ..
    lda fs_cmd_data                                                   ; 8b7c: ad 05 0f    ...
    ldy #9                                                            ; 8b7f: a0 09       ..
    adc (fs_options),y                                                ; 8b81: 71 bb       q.
    sta (fs_options),y                                                ; 8b83: 91 bb       ..
    lda l00c8                                                         ; 8b85: a5 c8       ..
    sbc #7                                                            ; 8b87: e9 07       ..
    sta l0f06                                                         ; 8b89: 8d 06 0f    ...
    sta fs_load_addr_2                                                ; 8b8c: 85 b2       ..
    beq c8b93                                                         ; 8b8e: f0 03       ..
    jsr copy_reply_to_caller                                          ; 8b90: 20 1d 8b     ..
; &8b93 referenced 1 time by &8b8e
.c8b93
    ldx #2                                                            ; 8b93: a2 02       ..
; &8b95 referenced 1 time by &8b99
.loop_c8b95
    sta l0f07,x                                                       ; 8b95: 9d 07 0f    ...
    dex                                                               ; 8b98: ca          .
    bpl loop_c8b95                                                    ; 8b99: 10 fa       ..
    jsr adjust_addrs_1                                                ; 8b9b: 20 f5 89     ..
    sec                                                               ; 8b9e: 38          8
    dec fs_load_addr_2                                                ; 8b9f: c6 b2       ..
    lda fs_cmd_data                                                   ; 8ba1: ad 05 0f    ...
    sta l0f06                                                         ; 8ba4: 8d 06 0f    ...
    jsr adjust_addrs                                                  ; 8ba7: 20 f8 89     ..
    beq c8b54                                                         ; 8baa: f0 a8       ..
; &8bac referenced 3 times by &8b32, &8bb1, &8e0e
.tube_claim_loop
    lda #&c3                                                          ; 8bac: a9 c3       ..
    jsr tube_addr_claim                                               ; 8bae: 20 06 04     ..
    bcc tube_claim_loop                                               ; 8bb1: 90 f9       ..
    rts                                                               ; 8bb3: 60          `

; ***************************************************************************************
; FSCV 2/3/4: unrecognised * command handler (DECODE)
; 
; CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text
; against the table
; at &8BD7 using case-insensitive comparison with abbreviation
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
.fscv_star_handler
    jsr l85a5                                                         ; 8bb4: 20 a5 85     ..
    ldx #&ff                                                          ; 8bb7: a2 ff       ..
    stx l00b9                                                         ; 8bb9: 86 b9       ..
; &8bbb referenced 1 time by &8bd6
.loop_c8bbb
    ldy #&ff                                                          ; 8bbb: a0 ff       ..
; &8bbd referenced 1 time by &8bc8
.decfir
    iny                                                               ; 8bbd: c8          .
    inx                                                               ; 8bbe: e8          .
; &8bbf referenced 1 time by &8bda
.decmor
    lda fs_cmd_match_table,x                                          ; 8bbf: bd e2 8b    ...
    bmi c8bdc                                                         ; 8bc2: 30 18       0.
    eor (fs_crc_lo),y                                                 ; 8bc4: 51 be       Q.
    and #&df                                                          ; 8bc6: 29 df       ).
    beq decfir                                                        ; 8bc8: f0 f3       ..
    dex                                                               ; 8bca: ca          .
; &8bcb referenced 1 time by &8bcf
.decmin
    inx                                                               ; 8bcb: e8          .
    lda fs_cmd_match_table,x                                          ; 8bcc: bd e2 8b    ...
    bpl decmin                                                        ; 8bcf: 10 fa       ..
    lda (fs_crc_lo),y                                                 ; 8bd1: b1 be       ..
    inx                                                               ; 8bd3: e8          .
    cmp #&2e ; '.'                                                    ; 8bd4: c9 2e       ..
    bne loop_c8bbb                                                    ; 8bd6: d0 e3       ..
    iny                                                               ; 8bd8: c8          .
    dex                                                               ; 8bd9: ca          .
    bcs decmor                                                        ; 8bda: b0 e3       ..
; &8bdc referenced 1 time by &8bc2
.c8bdc
    pha                                                               ; 8bdc: 48          H
    lda l8be3,x                                                       ; 8bdd: bd e3 8b    ...
    pha                                                               ; 8be0: 48          H
    rts                                                               ; 8be1: 60          `

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
l8be3 = fs_cmd_match_table+1
    eor #&2e ; '.'                                                    ; 8be2: 49 2e       I.
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
; Sets &B7=&01 and &B5=&03, then branches into cat_handler at
; &8C0A, bypassing cat_handler's default column setup. &B7=1
; gives one entry per line with full details (vs &B7=3 for *CAT
; which gives multiple files per line).
; ***************************************************************************************
.ex_handler
    ldx #1                                                            ; 8bf8: a2 01       ..
    stx l00b7                                                         ; 8bfa: 86 b7       ..
    lda #3                                                            ; 8bfc: a9 03       ..
    bne c8c0a                                                         ; 8bfe: d0 0a       ..             ; ALWAYS branch

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
    ldx #3                                                            ; 8c00: a2 03       ..
    stx l00b7                                                         ; 8c02: 86 b7       ..
    ldy #0                                                            ; 8c04: a0 00       ..
    sty l00b9                                                         ; 8c06: 84 b9       ..
    lda #&0b                                                          ; 8c08: a9 0b       ..
; &8c0a referenced 1 time by &8bfe
.c8c0a
    sta l00b5                                                         ; 8c0a: 85 b5       ..
    lda #6                                                            ; 8c0c: a9 06       ..
    sta fs_cmd_data                                                   ; 8c0e: 8d 05 0f    ...
    jsr sub_c86c5                                                     ; 8c11: 20 c5 86     ..
    ldx #1                                                            ; 8c14: a2 01       ..
    jsr copy_string_to_cmd                                            ; 8c16: 20 4d 8d     M.
    ldy #&12                                                          ; 8c19: a0 12       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c1b: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    ldx #3                                                            ; 8c1e: a2 03       ..
    jsr print_reply_bytes                                             ; 8c20: 20 ba 8d     ..
    jsr print_inline                                                  ; 8c23: 20 e2 85     ..
    equs "("                                                          ; 8c26: 28          (

    lda l0f13                                                         ; 8c27: ad 13 0f    ...
    jsr print_decimal                                                 ; 8c2a: 20 86 8d     ..
    jsr print_inline                                                  ; 8c2d: 20 e2 85     ..
    equs ")     "                                                     ; 8c30: 29 20 20... )

    ldx l0f12                                                         ; 8c36: ae 12 0f    ...
    bne c8c46                                                         ; 8c39: d0 0b       ..
    jsr print_inline                                                  ; 8c3b: 20 e2 85     ..
    equs "Owner", &0d                                                 ; 8c3e: 4f 77 6e... Own

    bne c8c50                                                         ; 8c44: d0 0a       ..
; &8c46 referenced 1 time by &8c39
.c8c46
    jsr print_inline                                                  ; 8c46: 20 e2 85     ..
    equs "Public", &0d                                                ; 8c49: 50 75 62... Pub

; &8c50 referenced 1 time by &8c44
.c8c50
    ldy #&15                                                          ; 8c50: a0 15       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8c52: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    inx                                                               ; 8c55: e8          .
    ldy #&10                                                          ; 8c56: a0 10       ..
    jsr print_reply_counted                                           ; 8c58: 20 bc 8d     ..
    jsr print_inline                                                  ; 8c5b: 20 e2 85     ..
    equs "    Option "                                                ; 8c5e: 20 20 20...

    lda fs_boot_option                                                ; 8c69: ad 05 0e    ...
    tax                                                               ; 8c6c: aa          .
    jsr print_hex                                                     ; 8c6d: 20 a5 8d     ..
    jsr print_inline                                                  ; 8c70: 20 e2 85     ..
    equs " ("                                                         ; 8c73: 20 28        (

    ldy c8cde,x                                                       ; 8c75: bc de 8c    ...
; &8c78 referenced 1 time by &8c81
.loop_c8c78
    lda c8cde,y                                                       ; 8c78: b9 de 8c    ...
    bmi c8c83                                                         ; 8c7b: 30 06       0.
    jsr osasci                                                        ; 8c7d: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8c80: c8          .
    bne loop_c8c78                                                    ; 8c81: d0 f5       ..
; &8c83 referenced 1 time by &8c7b
.c8c83
    jsr print_inline                                                  ; 8c83: 20 e2 85     ..
    equs ")", &0d, "Dir. "                                            ; 8c86: 29 0d 44... ).D

    ldx #&11                                                          ; 8c8d: a2 11       ..
    jsr print_reply_bytes                                             ; 8c8f: 20 ba 8d     ..
    jsr print_inline                                                  ; 8c92: 20 e2 85     ..
    equs "     Lib. "                                                 ; 8c95: 20 20 20...

    ldx #&1b                                                          ; 8c9f: a2 1b       ..
    jsr print_reply_bytes                                             ; 8ca1: 20 ba 8d     ..
    jsr print_inline                                                  ; 8ca4: 20 e2 85     ..
    equs &0d, &0d                                                     ; 8ca7: 0d 0d       ..

    sty l0f06                                                         ; 8ca9: 8c 06 0f    ...
    sty l00b4                                                         ; 8cac: 84 b4       ..
    ldx l00b5                                                         ; 8cae: a6 b5       ..
    stx l0f07                                                         ; 8cb0: 8e 07 0f    ...
; &8cb3 referenced 1 time by &8cdc
.c8cb3
    ldx l00b7                                                         ; 8cb3: a6 b7       ..
    stx fs_cmd_data                                                   ; 8cb5: 8e 05 0f    ...
    ldx #3                                                            ; 8cb8: a2 03       ..
    jsr copy_string_to_cmd                                            ; 8cba: 20 4d 8d     M.
    ldy #3                                                            ; 8cbd: a0 03       ..             ; Y=function code for HDRFN
    jsr prepare_fs_cmd                                                ; 8cbf: 20 94 83     ..            ; Prepare FS command buffer (12 references)
    lda fs_cmd_data                                                   ; 8cc2: ad 05 0f    ...
    beq c8d2b                                                         ; 8cc5: f0 64       .d
    ldx #2                                                            ; 8cc7: a2 02       ..
    jsr print_dir_from_offset                                         ; 8cc9: 20 61 8d     a.
    clc                                                               ; 8ccc: 18          .
    lda l00b4                                                         ; 8ccd: a5 b4       ..
    adc fs_cmd_data                                                   ; 8ccf: 6d 05 0f    m..
    sta l0f06                                                         ; 8cd2: 8d 06 0f    ...
    sta l00b4                                                         ; 8cd5: 85 b4       ..
    lda l00b5                                                         ; 8cd7: a5 b5       ..
    sta l0f07                                                         ; 8cd9: 8d 07 0f    ...
    bne c8cb3                                                         ; 8cdc: d0 d5       ..
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
.c8cde
    ror a                                                             ; 8cde: 6a          j
    adc l18a5,x                                                       ; 8cdf: 7d a5 18    }..
    jmp l212e                                                         ; 8ce2: 4c 2e 21    L.!

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
; overlapping: sbc (l00e2),y                                          ; 8cf2: f1 e2       ..
; &8cf2 referenced 1 time by &8e3b
.boot_option_offsets
    equb &f1                                                          ; 8cf2: f1          .              ; Opt 0 (Off): bare CR
    equb &e2                                                          ; 8cf3: e2          .              ; Opt 1 (Load): L.!BOOT
; overlapping: cpx l00ea                                              ; 8cf4: e4 ea       ..
    equb &e4                                                          ; 8cf4: e4          .              ; Opt 2 (Run): !BOOT
    equb &ea                                                          ; 8cf5: ea          .              ; Opt 3 (Exec): E.!BOOT
; overlapping: eor l0078                                              ; 8cf6: 45 78       Ex
    equs "Exec"                                                       ; 8cf6: 45 78 65... Exe
; overlapping: adc zp_63                                              ; 8cf8: 65 63       ec

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
    ldy fs_messages_flag                                              ; 8cfa: ac 06 0e    ...
    beq return_5                                                      ; 8cfd: f0 5b       .[
    ldy #0                                                            ; 8cff: a0 00       ..
    ldx fs_cmd_csd                                                    ; 8d01: ae 03 0f    ...
    beq c8d0b                                                         ; 8d04: f0 05       ..
    jsr print_dir_from_offset                                         ; 8d06: 20 61 8d     a.
    bmi c8d23                                                         ; 8d09: 30 18       0.
; &8d0b referenced 2 times by &8d04, &8d19
.c8d0b
    lda (fs_crc_lo),y                                                 ; 8d0b: b1 be       ..
    cmp #&0d                                                          ; 8d0d: c9 0d       ..
    beq pad_filename_spaces                                           ; 8d0f: f0 0a       ..
    cmp #&20 ; ' '                                                    ; 8d11: c9 20       .
    beq pad_filename_spaces                                           ; 8d13: f0 06       ..
    jsr osasci                                                        ; 8d15: 20 e3 ff     ..            ; Write character
    iny                                                               ; 8d18: c8          .
    bne c8d0b                                                         ; 8d19: d0 f0       ..
; &8d1b referenced 3 times by &8d0f, &8d13, &8d21
.pad_filename_spaces
    jsr print_space                                                   ; 8d1b: 20 44 8d     D.
    iny                                                               ; 8d1e: c8          .
    cpy #&0c                                                          ; 8d1f: c0 0c       ..
    bcc pad_filename_spaces                                           ; 8d21: 90 f8       ..
; &8d23 referenced 1 time by &8d09
.c8d23
    ldy #5                                                            ; 8d23: a0 05       ..
    jsr print_hex_bytes                                               ; 8d25: 20 39 8d     9.
    jsr print_exec_and_len                                            ; 8d28: 20 2e 8d     ..
; &8d2b referenced 1 time by &8cc5
.c8d2b
    jmp osnewl                                                        ; 8d2b: 4c e7 ff    L..            ; Write newline (characters 10 and 13)

; &8d2e referenced 1 time by &8d28
.print_exec_and_len
    ldy #9                                                            ; 8d2e: a0 09       ..
    jsr print_hex_bytes                                               ; 8d30: 20 39 8d     9.
    ldy #&0c                                                          ; 8d33: a0 0c       ..
    ldx #3                                                            ; 8d35: a2 03       ..
    bne num01                                                         ; 8d37: d0 02       ..             ; ALWAYS branch

; &8d39 referenced 2 times by &8d25, &8d30
.print_hex_bytes
    ldx #4                                                            ; 8d39: a2 04       ..
; &8d3b referenced 2 times by &8d37, &8d42
.num01
    lda (fs_options),y                                                ; 8d3b: b1 bb       ..
    jsr print_hex                                                     ; 8d3d: 20 a5 8d     ..
    dey                                                               ; 8d40: 88          .
    dex                                                               ; 8d41: ca          .
    bne num01                                                         ; 8d42: d0 f7       ..
; &8d44 referenced 1 time by &8d1b
.print_space
    lda #&20 ; ' '                                                    ; 8d44: a9 20       .
    bne c8db8                                                         ; 8d46: d0 70       .p             ; ALWAYS branch

    equs "Off"                                                        ; 8d48: 4f 66 66    Off

; ***************************************************************************************
; Copy filename to FS command buffer
; 
; Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
; Used to place a filename into the FS command buffer before
; sending to the fileserver. Falls through to copy_string_to_cmd.
; ***************************************************************************************
; &8d4b referenced 3 times by &80b4, &88bb, &8dca
.copy_filename
    ldx #0                                                            ; 8d4b: a2 00       ..
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
    ldy #0                                                            ; 8d4d: a0 00       ..
; &8d4f referenced 1 time by &8d58
.copy_string_from_offset
    lda (fs_crc_lo),y                                                 ; 8d4f: b1 be       ..
    sta fs_cmd_data,x                                                 ; 8d51: 9d 05 0f    ...
    inx                                                               ; 8d54: e8          .
    iny                                                               ; 8d55: c8          .
    eor #&0d                                                          ; 8d56: 49 0d       I.
    bne copy_string_from_offset                                       ; 8d58: d0 f5       ..
; &8d5a referenced 2 times by &8cfd, &8d64
.return_5
    rts                                                               ; 8d5a: 60          `

    equs "Load"                                                       ; 8d5b: 4c 6f 61... Loa

; ***************************************************************************************
; Print directory name from reply buffer
; 
; Prints characters from the FS reply buffer (&0F05+X onwards).
; Null bytes (&00) are replaced with CR (&0D) for display.
; Stops when a byte with bit 7 set is encountered (high-bit
; terminator). Used by cat_handler to display Dir. and Lib. paths.
; ***************************************************************************************
.print_dir_name
    ldx #0                                                            ; 8d5f: a2 00       ..
; &8d61 referenced 3 times by &8cc9, &8d06, &8d81
.print_dir_from_offset
    lda fs_cmd_data,x                                                 ; 8d61: bd 05 0f    ...
    bmi return_5                                                      ; 8d64: 30 f4       0.
    bne infol2                                                        ; 8d66: d0 15       ..
    ldy l00b9                                                         ; 8d68: a4 b9       ..
    bmi c8d7b                                                         ; 8d6a: 30 0f       0.
    iny                                                               ; 8d6c: c8          .
    tya                                                               ; 8d6d: 98          .
    and #3                                                            ; 8d6e: 29 03       ).
    sta l00b9                                                         ; 8d70: 85 b9       ..
    beq c8d7b                                                         ; 8d72: f0 07       ..
    jsr print_inline                                                  ; 8d74: 20 e2 85     ..
    equs "  "                                                         ; 8d77: 20 20

    bne c8d80                                                         ; 8d79: d0 05       ..
; &8d7b referenced 2 times by &8d6a, &8d72
.c8d7b
    lda #&0d                                                          ; 8d7b: a9 0d       ..
; &8d7d referenced 1 time by &8d66
.infol2
    jsr osasci                                                        ; 8d7d: 20 e3 ff     ..            ; Write character 13
; &8d80 referenced 1 time by &8d79
.c8d80
    inx                                                               ; 8d80: e8          .
    bne print_dir_from_offset                                         ; 8d81: d0 de       ..
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
    tay                                                               ; 8d86: a8          .
    lda #&64 ; 'd'                                                    ; 8d87: a9 64       .d
    jsr print_decimal_digit                                           ; 8d89: 20 93 8d     ..
    lda #&0a                                                          ; 8d8c: a9 0a       ..
    jsr print_decimal_digit                                           ; 8d8e: 20 93 8d     ..
    lda #1                                                            ; 8d91: a9 01       ..
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
    sta fs_error_ptr                                                  ; 8d93: 85 b8       ..
    tya                                                               ; 8d95: 98          .
    ldx #&2f ; '/'                                                    ; 8d96: a2 2f       ./
    sec                                                               ; 8d98: 38          8
; &8d99 referenced 1 time by &8d9c
.loop_c8d99
    inx                                                               ; 8d99: e8          .
    sbc fs_error_ptr                                                  ; 8d9a: e5 b8       ..
    bcs loop_c8d99                                                    ; 8d9c: b0 fb       ..
    adc fs_error_ptr                                                  ; 8d9e: 65 b8       e.
    tay                                                               ; 8da0: a8          .
    txa                                                               ; 8da1: 8a          .
; &8da2 referenced 1 time by &8db8
.loop_c8da2
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
    pha                                                               ; 8da5: 48          H
    lsr a                                                             ; 8da6: 4a          J
    lsr a                                                             ; 8da7: 4a          J
    lsr a                                                             ; 8da8: 4a          J
    lsr a                                                             ; 8da9: 4a          J
    jsr print_hex_nibble                                              ; 8daa: 20 b0 8d     ..
    pla                                                               ; 8dad: 68          h
    and #&0f                                                          ; 8dae: 29 0f       ).
; &8db0 referenced 1 time by &8daa
.print_hex_nibble
    ora #&30 ; '0'                                                    ; 8db0: 09 30       .0
    cmp #&3a ; ':'                                                    ; 8db2: c9 3a       .:
    bcc c8db8                                                         ; 8db4: 90 02       ..
    adc #6                                                            ; 8db6: 69 06       i.
; &8db8 referenced 2 times by &8d46, &8db4
.c8db8
    bne loop_c8da2                                                    ; 8db8: d0 e8       ..
; ***************************************************************************************
; Print reply buffer bytes
; 
; Prints Y characters from the FS reply buffer (&0F05+X) to
; the screen via OSASCI. X = starting offset, Y = count.
; Used by cat_handler to display directory and library names.
; ***************************************************************************************
; &8dba referenced 3 times by &8c20, &8c8f, &8ca1
.print_reply_bytes
    ldy #&0a                                                          ; 8dba: a0 0a       ..
; &8dbc referenced 2 times by &8c58, &8dc4
.print_reply_counted
    lda fs_cmd_data,x                                                 ; 8dbc: bd 05 0f    ...
    jsr osasci                                                        ; 8dbf: 20 e3 ff     ..            ; Write character
    inx                                                               ; 8dc2: e8          .
    dey                                                               ; 8dc3: 88          .
    bne print_reply_counted                                           ; 8dc4: d0 f6       ..
    rts                                                               ; 8dc6: 60          `

.sub_c8dc7
    jsr parse_filename_gs                                             ; 8dc7: 20 c3 86     ..
; ***************************************************************************************
; *NET2: read handle entry from workspace
; 
; Looks up the handle in &F0 via calc_handle_offset. If the
; workspace slot contains &3F ('?', meaning unused/closed),
; returns 0. Otherwise returns the stored handle value.
; Clears fs_temp_ce on exit.
; ***************************************************************************************
.net2_read_handle_entry
    jsr copy_filename                                                 ; 8dca: 20 4b 8d     K.
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
    ldx #&0e                                                          ; 8dcd: a2 0e       ..
    stx fs_block_offset                                               ; 8dcf: 86 bc       ..
    lda #&10                                                          ; 8dd1: a9 10       ..
    sta fs_options                                                    ; 8dd3: 85 bb       ..
    sta l0e16                                                         ; 8dd5: 8d 16 0e    ...
    ldx #&4a ; 'J'                                                    ; 8dd8: a2 4a       .J
    ldy #5                                                            ; 8dda: a0 05       ..
    jsr send_fs_examine                                               ; 8ddc: 20 fd 86     ..
; overlapping: ldy #0                                                 ; 8ddf: a0 00       ..
    equb &a0                                                          ; 8ddf: a0          .

; ***************************************************************************************
; *NET3: close handle (mark as unused)
; 
; Looks up the handle in &F0 via calc_handle_offset. Writes
; &3F ('?') to mark the handle slot as closed in the NFS
; workspace. Preserves the carry flag state across the write
; using ROL/ROR on rx_status_flags. Clears fs_temp_ce on exit.
; ***************************************************************************************
.net3_close_handle
    brk                                                               ; 8de0: 00          .

    clc                                                               ; 8de1: 18          .
    jsr gsinit                                                        ; 8de2: 20 c2 ff     ..
; &8de5 referenced 1 time by &8de8
.loop_c8de5
    jsr gsread                                                        ; 8de5: 20 c5 ff     ..
    bcc loop_c8de5                                                    ; 8de8: 90 fb       ..
    dey                                                               ; 8dea: 88          .
; &8deb referenced 1 time by &8df0
.loop_c8deb
    iny                                                               ; 8deb: c8          .
    lda (os_text_ptr),y                                               ; 8dec: b1 f2       ..
    cmp #&20 ; ' '                                                    ; 8dee: c9 20       .
    beq loop_c8deb                                                    ; 8df0: f0 f9       ..
    clc                                                               ; 8df2: 18          .
; ***************************************************************************************
; *NET4: resume after remote operation
; 
; Calls resume_after_remote (&8146) to re-enable the keyboard
; and send a completion notification. The BVC always branches
; to c8dda (clear fs_temp_ce) since resume_after_remote
; returns with V clear (from CLV in prepare_cmd_clv).
; ***************************************************************************************
.net4_resume_remote
    tya                                                               ; 8df3: 98          .
    adc os_text_ptr                                                   ; 8df4: 65 f2       e.
    sta fs_cmd_context                                                ; 8df6: 8d 0a 0e    ...
    lda l00f3                                                         ; 8df9: a5 f3       ..
    adc #0                                                            ; 8dfb: 69 00       i.
    sta l0e0b                                                         ; 8dfd: 8d 0b 0e    ...
    sec                                                               ; 8e00: 38          8
    lda tx_in_progress                                                ; 8e01: ad 52 0d    .R.
    beq c8e1a                                                         ; 8e04: f0 14       ..
    adc l0f0b                                                         ; 8e06: 6d 0b 0f    m..
    adc l0f0c                                                         ; 8e09: 6d 0c 0f    m..
    bcs c8e1a                                                         ; 8e0c: b0 0c       ..
    jsr tube_claim_loop                                               ; 8e0e: 20 ac 8b     ..
    ldx #9                                                            ; 8e11: a2 09       ..
    ldy #&0f                                                          ; 8e13: a0 0f       ..
    lda #4                                                            ; 8e15: a9 04       ..
    jmp tube_addr_claim                                               ; 8e17: 4c 06 04    L..

; &8e1a referenced 2 times by &8e04, &8e0c
.c8e1a
    jmp (l0f09)                                                       ; 8e1a: 6c 09 0f    l..

; ***************************************************************************************
; Set library handle
; 
; Stores Y into &0E04 (library directory handle in FS workspace).
; Falls through to JMP restore_args_return if Y is non-zero.
; ***************************************************************************************
.set_lib_handle
    sty fs_lib_handle                                                 ; 8e1d: 8c 04 0e    ...
    bne c8e25                                                         ; 8e20: d0 03       ..
; ***************************************************************************************
; Set CSD handle
; 
; Stores Y into &0E03 (current selected directory handle).
; Falls through to JMP restore_args_return.
; ***************************************************************************************
.set_csd_handle
    sty fs_csd_handle                                                 ; 8e22: 8c 03 0e    ...
; &8e25 referenced 2 times by &8e20, &8e36
.c8e25
    jmp restore_args_return                                           ; 8e25: 4c 57 89    LW.

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
    sec                                                               ; 8e28: 38          8
; ***************************************************************************************
; Copy FS reply handles to workspace (no boot)
; 
; CLC entry (SDISC): copies handles only, then jumps to c8cff.
; Called when the FS reply contains updated handle values
; but no boot action is needed.
; ***************************************************************************************
.copy_handles
    ldx #3                                                            ; 8e29: a2 03       ..
    bcc c8e33                                                         ; 8e2b: 90 06       ..
; &8e2d referenced 1 time by &8e34
.logon2
    lda fs_cmd_data,x                                                 ; 8e2d: bd 05 0f    ...
    sta fs_urd_handle,x                                               ; 8e30: 9d 02 0e    ...
; &8e33 referenced 1 time by &8e2b
.c8e33
    dex                                                               ; 8e33: ca          .
    bpl logon2                                                        ; 8e34: 10 f7       ..
    bcc c8e25                                                         ; 8e36: 90 ed       ..
    ldy fs_boot_option                                                ; 8e38: ac 05 0e    ...
    ldx boot_option_offsets,y                                         ; 8e3b: be f2 8c    ...
    ldy #&8c                                                          ; 8e3e: a0 8c       ..
    jmp oscli                                                         ; 8e40: 4c f7 ff    L..

; ***************************************************************************************
; *NET1: read file handle from received packet
; 
; Reads a file handle byte from offset &6F in the RX buffer
; (net_rx_ptr), stores it in &F0, then falls through to the
; common handle workspace cleanup at c8dda (clear fs_temp_ce).
; ***************************************************************************************
.net1_read_handle
    ldy #&6f ; 'o'                                                    ; 8e43: a0 6f       .o
    lda (net_rx_ptr),y                                                ; 8e45: b1 9c       ..
    sta l00f0                                                         ; 8e47: 85 f0       ..
    rts                                                               ; 8e49: 60          `

; &8e4a referenced 2 times by &8e5e, &8e6e
.sub_c8e4a
    lda l00f0                                                         ; 8e4a: a5 f0       ..
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
    asl a                                                             ; 8e4c: 0a          .
    asl a                                                             ; 8e4d: 0a          .
    pha                                                               ; 8e4e: 48          H
    asl a                                                             ; 8e4f: 0a          .
    tsx                                                               ; 8e50: ba          .
    adc l0101,x                                                       ; 8e51: 7d 01 01    }..
    tay                                                               ; 8e54: a8          .
    pla                                                               ; 8e55: 68          h
    cmp #&48 ; 'H'                                                    ; 8e56: c9 48       .H
    bcc return_6                                                      ; 8e58: 90 03       ..
    ldy #0                                                            ; 8e5a: a0 00       ..
    tya                                                               ; 8e5c: 98          .              ; A=&00
; &8e5d referenced 1 time by &8e58
.return_6
.return_calc_handle
    rts                                                               ; 8e5d: 60          `

.sub_c8e5e
    jsr sub_c8e4a                                                     ; 8e5e: 20 4a 8e     J.
    bcs rxpol2                                                        ; 8e61: b0 06       ..
    lda (nfs_workspace),y                                             ; 8e63: b1 9e       ..
    cmp #&3f ; '?'                                                    ; 8e65: c9 3f       .?
    bne c8e6b                                                         ; 8e67: d0 02       ..
; &8e69 referenced 2 times by &8e61, &8e71
.rxpol2
    lda #0                                                            ; 8e69: a9 00       ..
; &8e6b referenced 1 time by &8e67
.c8e6b
    sta l00f0                                                         ; 8e6b: 85 f0       ..
    rts                                                               ; 8e6d: 60          `

.sub_c8e6e
    jsr sub_c8e4a                                                     ; 8e6e: 20 4a 8e     J.
    bcs rxpol2                                                        ; 8e71: b0 f6       ..
    rol rx_flags                                                      ; 8e73: 2e 64 0d    .d.
    lda #&3f ; '?'                                                    ; 8e76: a9 3f       .?
    sta (nfs_workspace),y                                             ; 8e78: 91 9e       ..
.sub_c8e7a
osword_12_handler = sub_c8e7a+2
    ror rx_flags                                                      ; 8e7a: 6e 64 0d    nd.
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
; Uses the bidirectional copy at &8E23 for station read/set.
; ***************************************************************************************
; overlapping: ora la560                                              ; 8e7c: 0d 60 a5    .`.
    rts                                                               ; 8e7d: 60          `

; ***************************************************************************************
; Filing system OSWORD entry
; 
; Subtracts &0F from the command code in &EF, giving a 0-4 index
; for OSWORD calls &0F-&13 (15-19). Falls through to the
; PHA/PHA/RTS dispatch at &8E02.
; ***************************************************************************************
.osword_fs_entry
    lda l00ef                                                         ; 8e7e: a5 ef       ..             ; Command code from &EF
    sbc #&0f                                                          ; 8e80: e9 0f       ..             ; Subtract &0F: OSWORD &0F-&13 become indices 0-4
    bmi return_7                                                      ; 8e82: 30 3b       0;
    cmp #5                                                            ; 8e84: c9 05       ..
    bcs return_7                                                      ; 8e86: b0 37       .7
; ***************************************************************************************
; PHA/PHA/RTS dispatch for filing system OSWORDs
; 
; X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
; at &8EA7 (low) / &8EAC (high).
; ***************************************************************************************
.fs_osword_dispatch
    tax                                                               ; 8e88: aa          .
    lda #&8f                                                          ; 8e89: a9 8f       ..
    pha                                                               ; 8e8b: 48          H
    lda #&c6                                                          ; 8e8c: a9 c6       ..
    pha                                                               ; 8e8e: 48          H
    lda l8eac,x                                                       ; 8e8f: bd ac 8e    ...
    pha                                                               ; 8e92: 48          H
    lda l8ea7,x                                                       ; 8e93: bd a7 8e    ...
    pha                                                               ; 8e96: 48          H
    ldy #2                                                            ; 8e97: a0 02       ..
; &8e99 referenced 1 time by &8e9f
.save1
    lda l00aa,y                                                       ; 8e99: b9 aa 00    ...
    sta (net_rx_ptr),y                                                ; 8e9c: 91 9c       ..
    dey                                                               ; 8e9e: 88          .
    bpl save1                                                         ; 8e9f: 10 f8       ..
    iny                                                               ; 8ea1: c8          .
    lda (l00f0),y                                                     ; 8ea2: b1 f0       ..
    sty rom_svc_num                                                   ; 8ea4: 84 a9       ..
    rts                                                               ; 8ea6: 60          `

; &8ea7 referenced 1 time by &8e93
.l8ea7
    equb &bf, &6d                                                     ; 8ea7: bf 6d       .m             ; Dispatch table: low bytes for OSWORD &0F-&13 handlers
.fs_osword_tbl_lo
    equb <(osword_11_handler-1)                                       ; 8ea9: d9          .
    equb <(sub_c8eff-1)                                               ; 8eaa: fe          .
    equb <(econet_tx_rx-1)                                            ; 8eab: ec          .
; &8eac referenced 1 time by &8e8f
.l8eac
    equb <(sub_c908f-1)                                               ; 8eac: 8e          .              ; Dispatch table: high bytes for OSWORD &0F-&13 handlers
    equb <(sub_c0490-1)                                               ; 8ead: 8f          .
.fs_osword_tbl_hi
    equb >(osword_11_handler-1)                                       ; 8eae: 8e          .
    equb >(sub_c8eff-1)                                               ; 8eaf: 8e          .
    equb >(econet_tx_rx-1)                                            ; 8eb0: 8f          .
; ***************************************************************************************
; Bidirectional block copy between OSWORD param block and workspace.
; 
; C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
; C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)
; ***************************************************************************************
; overlapping: bcc sub_c8eb7                                          ; 8eb1: 90 04       ..
; &8eb1 referenced 5 times by &8ebd, &8ed4, &8ee9, &8f1a, &8faf
.copy_param_block
    equb >(sub_c908f-1)                                               ; 8eb1: 90          .
    equb >(sub_c0490-1)                                               ; 8eb2: 04          .

    lda (l00f0),y                                                     ; 8eb3: b1 f0       ..
    sta (l00ab),y                                                     ; 8eb5: 91 ab       ..
.sub_c8eb7
    lda (l00ab),y                                                     ; 8eb7: b1 ab       ..
    sta (l00f0),y                                                     ; 8eb9: 91 f0       ..
.copyl3
    iny                                                               ; 8ebb: c8          .
    dex                                                               ; 8ebc: ca          .
    bpl copy_param_block                                              ; 8ebd: 10 f2       ..
; &8ebf referenced 2 times by &8e82, &8e86
.return_7
.logon3
.return_copy_param
    rts                                                               ; 8ebf: 60          `

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
    asl tx_clear_flag                                                 ; 8ec0: 0e 62 0d    .b.
    tya                                                               ; 8ec3: 98          .
    bcc readry                                                        ; 8ec4: 90 34       .4
    lda net_rx_ptr_hi                                                 ; 8ec6: a5 9d       ..
    sta l00ac                                                         ; 8ec8: 85 ac       ..
    sta nmi_tx_block_hi                                               ; 8eca: 85 a1       ..
    lda #&6f ; 'o'                                                    ; 8ecc: a9 6f       .o
    sta l00ab                                                         ; 8ece: 85 ab       ..
    sta nmi_tx_block                                                  ; 8ed0: 85 a0       ..
    ldx #&0f                                                          ; 8ed2: a2 0f       ..
    jsr copy_param_block                                              ; 8ed4: 20 b1 8e     ..
    jmp trampoline_tx_setup                                           ; 8ed7: 4c 60 96    L`.

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
    lda net_rx_ptr_hi                                                 ; 8eda: a5 9d       ..
    sta l00ac                                                         ; 8edc: 85 ac       ..
    ldy #&7f                                                          ; 8ede: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8ee0: b1 9c       ..
    iny                                                               ; 8ee2: c8          .              ; Y=&80
    sty l00ab                                                         ; 8ee3: 84 ab       ..
    tax                                                               ; 8ee5: aa          .
    dex                                                               ; 8ee6: ca          .
    ldy #0                                                            ; 8ee7: a0 00       ..
    jsr copy_param_block                                              ; 8ee9: 20 b1 8e     ..
    jmp clear_jsr_protection                                          ; 8eec: 4c e9 92    L..

; &8eef referenced 1 time by &8f3e
.read_args_size
    ldy #&7f                                                          ; 8eef: a0 7f       ..
    lda (net_rx_ptr),y                                                ; 8ef1: b1 9c       ..
    ldy #1                                                            ; 8ef3: a0 01       ..
    sta (l00f0),y                                                     ; 8ef5: 91 f0       ..
    iny                                                               ; 8ef7: c8          .              ; Y=&02
    lda #&80                                                          ; 8ef8: a9 80       ..
; &8efa referenced 1 time by &8ec4
.readry
    sta (l00f0),y                                                     ; 8efa: 91 f0       ..
    rts                                                               ; 8efc: 60          `

; &8efd referenced 1 time by &8f11
.l8efd
    equb &ff, 1                                                       ; 8efd: ff 01       ..

.sub_c8eff
    cmp #6                                                            ; 8eff: c9 06       ..
    bcs rsl1                                                          ; 8f01: b0 35       .5
    cmp #4                                                            ; 8f03: c9 04       ..
    bcs rssl1                                                         ; 8f05: b0 16       ..
    lsr a                                                             ; 8f07: 4a          J
    ldx #&0d                                                          ; 8f08: a2 0d       ..
    tay                                                               ; 8f0a: a8          .
    beq c8f0f                                                         ; 8f0b: f0 02       ..
    ldx nfs_workspace_hi                                              ; 8f0d: a6 9f       ..
; &8f0f referenced 1 time by &8f0b
.c8f0f
    stx l00ac                                                         ; 8f0f: 86 ac       ..
    lda l8efd,y                                                       ; 8f11: b9 fd 8e    ...
    sta l00ab                                                         ; 8f14: 85 ab       ..
    ldx #1                                                            ; 8f16: a2 01       ..
    ldy #1                                                            ; 8f18: a0 01       ..
    jmp copy_param_block                                              ; 8f1a: 4c b1 8e    L..

; &8f1d referenced 1 time by &8f05
.rssl1
    lsr a                                                             ; 8f1d: 4a          J
    iny                                                               ; 8f1e: c8          .
    lda (l00f0),y                                                     ; 8f1f: b1 f0       ..
    bcs rssl2                                                         ; 8f21: b0 05       ..
    lda prot_status                                                   ; 8f23: ad 63 0d    .c.
    sta (l00f0),y                                                     ; 8f26: 91 f0       ..
; &8f28 referenced 1 time by &8f21
.rssl2
    sta prot_status                                                   ; 8f28: 8d 63 0d    .c.
    sta saved_jsr_mask                                                ; 8f2b: 8d 65 0d    .e.
    rts                                                               ; 8f2e: 60          `

; &8f2f referenced 1 time by &8f3a
.loop_c8f2f
    ldy #&14                                                          ; 8f2f: a0 14       ..
    lda (net_rx_ptr),y                                                ; 8f31: b1 9c       ..
    ldy #1                                                            ; 8f33: a0 01       ..
    sta (l00f0),y                                                     ; 8f35: 91 f0       ..
    rts                                                               ; 8f37: 60          `

; &8f38 referenced 1 time by &8f01
.rsl1
    cmp #8                                                            ; 8f38: c9 08       ..
    beq loop_c8f2f                                                    ; 8f3a: f0 f3       ..
    cmp #9                                                            ; 8f3c: c9 09       ..
    beq read_args_size                                                ; 8f3e: f0 af       ..
    bpl c8f5b                                                         ; 8f40: 10 19       ..
    ldy #3                                                            ; 8f42: a0 03       ..
    lsr a                                                             ; 8f44: 4a          J
    bcc readc1                                                        ; 8f45: 90 1b       ..
    sty nfs_temp                                                      ; 8f47: 84 a8       ..
; &8f49 referenced 1 time by &8f58
.loop_c8f49
    ldy nfs_temp                                                      ; 8f49: a4 a8       ..
    lda (l00f0),y                                                     ; 8f4b: b1 f0       ..
    jsr handle_to_mask_a                                              ; 8f4d: 20 25 86     %.
    tya                                                               ; 8f50: 98          .
    ldy nfs_temp                                                      ; 8f51: a4 a8       ..
    sta fs_server_net,y                                               ; 8f53: 99 01 0e    ...
    dec nfs_temp                                                      ; 8f56: c6 a8       ..
    bne loop_c8f49                                                    ; 8f58: d0 ef       ..
    rts                                                               ; 8f5a: 60          `

; &8f5b referenced 1 time by &8f40
.c8f5b
    iny                                                               ; 8f5b: c8          .
    lda fs_last_error                                                 ; 8f5c: ad 09 0e    ...
    sta (l00f0),y                                                     ; 8f5f: 91 f0       ..
    rts                                                               ; 8f61: 60          `

; &8f62 referenced 2 times by &8f45, &8f6b
.readc1
    lda fs_server_net,y                                               ; 8f62: b9 01 0e    ...            ; A=single-bit bitmask
    jsr mask_to_handle                                                ; 8f65: 20 42 86     B.            ; Convert bitmask to handle number (FS2A)
    sta (l00f0),y                                                     ; 8f68: 91 f0       ..             ; A=handle number (&20-&27); Y=preserved
    dey                                                               ; 8f6a: 88          .
    bne readc1                                                        ; 8f6b: d0 f5       ..
    rts                                                               ; 8f6d: 60          `

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
    ldx nfs_workspace_hi                                              ; 8f6e: a6 9f       ..
    stx l00ac                                                         ; 8f70: 86 ac       ..
    sty l00ab                                                         ; 8f72: 84 ab       ..
    ror rx_flags                                                      ; 8f74: 6e 64 0d    nd.
    lda (l00f0),y                                                     ; 8f77: b1 f0       ..
    sta l00aa                                                         ; 8f79: 85 aa       ..             ; Load from ROM template (zero = use NMI workspace value)
    bne c8f98                                                         ; 8f7b: d0 1b       ..
    lda #3                                                            ; 8f7d: a9 03       ..
; &8f7f referenced 1 time by &8f91
.scan0
    jsr calc_handle_offset                                            ; 8f7f: 20 4c 8e     L.
    bcs openl4                                                        ; 8f82: b0 3d       .=
    lsr a                                                             ; 8f84: 4a          J
    lsr a                                                             ; 8f85: 4a          J
    tax                                                               ; 8f86: aa          .
    lda (l00ab),y                                                     ; 8f87: b1 ab       ..
    beq openl4                                                        ; 8f89: f0 36       .6
    cmp #&3f ; '?'                                                    ; 8f8b: c9 3f       .?
    beq scan1                                                         ; 8f8d: f0 04       ..
    inx                                                               ; 8f8f: e8          .
    txa                                                               ; 8f90: 8a          .
    bne scan0                                                         ; 8f91: d0 ec       ..
; &8f93 referenced 1 time by &8f8d
.scan1
    txa                                                               ; 8f93: 8a          .
    ldx #0                                                            ; 8f94: a2 00       ..
    sta (l00f0,x)                                                     ; 8f96: 81 f0       ..
; &8f98 referenced 1 time by &8f7b
.c8f98
    jsr calc_handle_offset                                            ; 8f98: 20 4c 8e     L.
    bcs openl4                                                        ; 8f9b: b0 24       .$
    dey                                                               ; 8f9d: 88          .
    sty l00ab                                                         ; 8f9e: 84 ab       ..
    lda #&c0                                                          ; 8fa0: a9 c0       ..
    ldy #1                                                            ; 8fa2: a0 01       ..
    ldx #&0b                                                          ; 8fa4: a2 0b       ..             ; Enable interrupts before transmit
    cpy l00aa                                                         ; 8fa6: c4 aa       ..
    adc (l00ab),y                                                     ; 8fa8: 71 ab       q.
    beq openl6                                                        ; 8faa: f0 03       ..             ; Dest station = &FFFF (accept reply from any station)
    bmi openl7                                                        ; 8fac: 30 0e       0.
; &8fae referenced 1 time by &8fbe
.loop_c8fae
    clc                                                               ; 8fae: 18          .
; &8faf referenced 1 time by &8faa
.openl6
    jsr copy_param_block                                              ; 8faf: 20 b1 8e     ..
    bcs c8fc3                                                         ; 8fb2: b0 0f       ..
    lda #&3f ; '?'                                                    ; 8fb4: a9 3f       .?
    ldy #1                                                            ; 8fb6: a0 01       ..
    sta (l00ab),y                                                     ; 8fb8: 91 ab       ..
    bne c8fc3                                                         ; 8fba: d0 07       ..             ; ALWAYS branch

; &8fbc referenced 1 time by &8fac
.openl7
    adc #1                                                            ; 8fbc: 69 01       i.             ; Initiate receive with timeout
    bne loop_c8fae                                                    ; 8fbe: d0 ee       ..
    dey                                                               ; 8fc0: 88          .
; &8fc1 referenced 3 times by &8f82, &8f89, &8f9b
.openl4
    sta (l00f0),y                                                     ; 8fc1: 91 f0       ..
; &8fc3 referenced 2 times by &8fb2, &8fba
.c8fc3
    rol rx_flags                                                      ; 8fc3: 2e 64 0d    .d.
    rts                                                               ; 8fc6: 60          `

    equb &a0, 2                                                       ; 8fc7: a0 02       ..
.rest1
    equb &b1, &9c, &99, &aa, 0, &88, &10, &f8, &60                    ; 8fc9: b1 9c 99... ...

; ***************************************************************************************
; Set up RX buffer pointers in NFS workspace
; 
; Calculates the start address of the RX data area (&F0+1) and stores
; it at workspace offset &28. Also reads the data length from (&F0)+1
; and adds it to &F0 to compute the end address at offset &2C.
; ***************************************************************************************
; &8fd2 referenced 1 time by &9005
.setup_rx_buffer_ptrs
    ldy #&1c                                                          ; 8fd2: a0 1c       ..
    lda l00f0                                                         ; 8fd4: a5 f0       ..
    adc #1                                                            ; 8fd6: 69 01       i.
    jsr store_16bit_at_y                                              ; 8fd8: 20 e3 8f     ..            ; Receive data blocks until command byte = &00 or &0D
    ldy #1                                                            ; 8fdb: a0 01       ..
    lda (l00f0),y                                                     ; 8fdd: b1 f0       ..
    ldy #&20 ; ' '                                                    ; 8fdf: a0 20       .
    adc l00f0                                                         ; 8fe1: 65 f0       e.
; &8fe3 referenced 1 time by &8fd8
.store_16bit_at_y
    sta (nfs_workspace),y                                             ; 8fe3: 91 9e       ..
    iny                                                               ; 8fe5: c8          .
    lda l00f1                                                         ; 8fe6: a5 f1       ..
    adc #0                                                            ; 8fe8: 69 00       i.
    sta (nfs_workspace),y                                             ; 8fea: 91 9e       ..
    rts                                                               ; 8fec: 60          `

; ***************************************************************************************
; Econet transmit/receive handler
; 
; A=0: Initialise TX control block from ROM template at &8311
;      (zero entries substituted from NMI workspace &0DDA), transmit
;      it, set up RX control block, and receive reply.
; A>=1: Handle transmit result (branch to cleanup at &8F49).
; ***************************************************************************************
.econet_tx_rx
    cmp #1                                                            ; 8fed: c9 01       ..             ; A=0: set up and transmit; A>=1: handle result
    bcs c9039                                                         ; 8fef: b0 48       .H
    ldy #&23 ; '#'                                                    ; 8ff1: a0 23       .#
; &8ff3 referenced 1 time by &9000
.dofs01
    lda init_tx_ctrl_block,y                                          ; 8ff3: b9 60 83    .`.
    bne c8ffb                                                         ; 8ff6: d0 03       ..
    lda l0de6,y                                                       ; 8ff8: b9 e6 0d    ...
; &8ffb referenced 1 time by &8ff6
.c8ffb
    sta (nfs_workspace),y                                             ; 8ffb: 91 9e       ..
    dey                                                               ; 8ffd: 88          .
    cpy #&17                                                          ; 8ffe: c0 17       ..
    bne dofs01                                                        ; 9000: d0 f1       ..
    iny                                                               ; 9002: c8          .
    sty net_tx_ptr                                                    ; 9003: 84 9a       ..
    jsr setup_rx_buffer_ptrs                                          ; 9005: 20 d2 8f     ..
    ldy #2                                                            ; 9008: a0 02       ..
    lda #&90                                                          ; 900a: a9 90       ..
    sta (l00f0),y                                                     ; 900c: 91 f0       ..
    iny                                                               ; 900e: c8          .              ; Y=&03
    iny                                                               ; 900f: c8          .              ; Retrieve original A (function code) from stack; Y=&04
; &9010 referenced 1 time by &9018
.loop_c9010
    lda l0dfe,y                                                       ; 9010: b9 fe 0d    ...
    sta (l00f0),y                                                     ; 9013: 91 f0       ..
    iny                                                               ; 9015: c8          .
    cpy #7                                                            ; 9016: c0 07       ..
    bne loop_c9010                                                    ; 9018: d0 f6       ..
    lda nfs_workspace_hi                                              ; 901a: a5 9f       ..
    sta net_tx_ptr_hi                                                 ; 901c: 85 9b       ..
    cli                                                               ; 901e: 58          X
    jsr tx_poll_ff                                                    ; 901f: 20 71 86     q.
    ldy #&20 ; ' '                                                    ; 9022: a0 20       .
    lda #&ff                                                          ; 9024: a9 ff       ..
    sta (nfs_workspace),y                                             ; 9026: 91 9e       ..
    iny                                                               ; 9028: c8          .              ; Y=&21
    sta (nfs_workspace),y                                             ; 9029: 91 9e       ..
    ldy #&19                                                          ; 902b: a0 19       ..
    lda #&90                                                          ; 902d: a9 90       ..
    sta (nfs_workspace),y                                             ; 902f: 91 9e       ..
    dey                                                               ; 9031: 88          .              ; Y=&18
    lda #&7f                                                          ; 9032: a9 7f       ..
    sta (nfs_workspace),y                                             ; 9034: 91 9e       ..
    jmp c84f8                                                         ; 9036: 4c f8 84    L..

; &9039 referenced 1 time by &8fef
.c9039
    php                                                               ; 9039: 08          .
    ldy #1                                                            ; 903a: a0 01       ..             ; Y=character to write
    lda (l00f0),y                                                     ; 903c: b1 f0       ..
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
    tax                                                               ; 903e: aa          .
    iny                                                               ; 903f: c8          .              ; ROR/ASL on stacked P: zeros carry to signal success
    lda (l00f0),y                                                     ; 9040: b1 f0       ..
    iny                                                               ; 9042: c8          .
    sty l00ab                                                         ; 9043: 84 ab       ..
    ldy #&72 ; 'r'                                                    ; 9045: a0 72       .r
    sta (net_rx_ptr),y                                                ; 9047: 91 9c       ..
    dey                                                               ; 9049: 88          .              ; Y=&71
    txa                                                               ; 904a: 8a          .
    sta (net_rx_ptr),y                                                ; 904b: 91 9c       ..
    plp                                                               ; 904d: 28          (
    bne dofs2                                                         ; 904e: d0 1d       ..
; &9050 referenced 1 time by &906a
.loop_c9050
    ldy l00ab                                                         ; 9050: a4 ab       ..
    inc l00ab                                                         ; 9052: e6 ab       ..
    lda (l00f0),y                                                     ; 9054: b1 f0       ..
    ldy #&7d ; '}'                                                    ; 9056: a0 7d       .}
    sta (net_rx_ptr),y                                                ; 9058: 91 9c       ..
    pha                                                               ; 905a: 48          H
    jsr ctrl_block_setup_alt                                          ; 905b: 20 6d 91     m.
    cli                                                               ; 905e: 58          X
    jsr tx_poll_core                                                  ; 905f: 20 75 86     u.            ; Core transmit and poll routine (XMIT)
; &9062 referenced 1 time by &9063
.loop_c9062
    dex                                                               ; 9062: ca          .
    bne loop_c9062                                                    ; 9063: d0 fd       ..
    pla                                                               ; 9065: 68          h
    beq return_8                                                      ; 9066: f0 04       ..
    eor #&0d                                                          ; 9068: 49 0d       I.             ; Test for end-of-data marker (&0D)
    bne loop_c9050                                                    ; 906a: d0 e4       ..
; &906c referenced 1 time by &9066
.return_8
    rts                                                               ; 906c: 60          `

; &906d referenced 1 time by &904e
.dofs2
    jsr ctrl_block_setup_alt                                          ; 906d: 20 6d 91     m.
    ldy #&7b ; '{'                                                    ; 9070: a0 7b       .{
    lda (net_rx_ptr),y                                                ; 9072: b1 9c       ..
    adc #3                                                            ; 9074: 69 03       i.
    sta (net_rx_ptr),y                                                ; 9076: 91 9c       ..
    cli                                                               ; 9078: 58          X
    jmp tx_poll_ff                                                    ; 9079: 4c 71 86    Lq.

; ***************************************************************************************
; NETVEC dispatch handler (ENTRY)
; 
; Indirected from NETVEC at &0224. Saves all registers and flags,
; retrieves the reason code from the stacked A, and dispatches to
; one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
; &9021. Reason codes >= 9 are ignored.
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
    php                                                               ; 907c: 08          .
    pha                                                               ; 907d: 48          H
    txa                                                               ; 907e: 8a          .
    pha                                                               ; 907f: 48          H
    tya                                                               ; 9080: 98          .
    pha                                                               ; 9081: 48          H
    tsx                                                               ; 9082: ba          .
    lda l0103,x                                                       ; 9083: bd 03 01    ...
    cmp #9                                                            ; 9086: c9 09       ..
    bcs entry1                                                        ; 9088: b0 04       ..
    tax                                                               ; 908a: aa          .
    jsr osword_trampoline                                             ; 908b: 20 95 90     ..
; &908e referenced 1 time by &9088
.entry1
    pla                                                               ; 908e: 68          h
.sub_c908f
    tay                                                               ; 908f: a8          .
    pla                                                               ; 9090: 68          h
    tax                                                               ; 9091: aa          .
    pla                                                               ; 9092: 68          h
    plp                                                               ; 9093: 28          (
    rts                                                               ; 9094: 60          `

; &9095 referenced 1 time by &908b
.osword_trampoline
    lda osword_tbl_hi,x                                               ; 9095: bd a9 90    ...            ; PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it
    pha                                                               ; 9098: 48          H
    lda osword_tbl_lo,x                                               ; 9099: bd a0 90    ...
    pha                                                               ; 909c: 48          H
    lda l00ef                                                         ; 909d: a5 ef       ..
    rts                                                               ; 909f: 60          `

; &90a0 referenced 1 time by &9099
.osword_tbl_lo
    equb <(return_2-1)                                                ; 90a0: 75          u
    equb <(remote_print_handler-1)                                    ; 90a1: d8          .
    equb <(remote_print_handler-1)                                    ; 90a2: d8          .
    equb <(remote_print_handler-1)                                    ; 90a3: d8          .
    equb <(sub_c90b2-1)                                               ; 90a4: b1          .
    equb <(remote_display_setup-1)                                    ; 90a5: c8          .
    equb <(return_2-1)                                                ; 90a6: 75          u
    equb <(remote_cmd_dispatch-1)                                     ; 90a7: d7          .
    equb <(remote_cmd_data-1)                                         ; 90a8: 41          A
; &90a9 referenced 1 time by &9095
.osword_tbl_hi
    equb >(return_2-1)                                                ; 90a9: 81          .
    equb >(remote_print_handler-1)                                    ; 90aa: 91          .
    equb >(remote_print_handler-1)                                    ; 90ab: 91          .
    equb >(remote_print_handler-1)                                    ; 90ac: 91          .
    equb >(sub_c90b2-1)                                               ; 90ad: 90          .
    equb >(remote_display_setup-1)                                    ; 90ae: 91          .
    equb >(return_2-1)                                                ; 90af: 81          .
    equb >(remote_cmd_dispatch-1)                                     ; 90b0: 90          .
    equb >(remote_cmd_data-1)                                         ; 90b1: 91          .

.sub_c90b2
    tsx                                                               ; 90b2: ba          .
    ror l0106,x                                                       ; 90b3: 7e 06 01    ~..
    asl l0106,x                                                       ; 90b6: 1e 06 01    ...
    tya                                                               ; 90b9: 98          .
    ldy #&da                                                          ; 90ba: a0 da       ..
    sta (nfs_workspace),y                                             ; 90bc: 91 9e       ..
    lda #0                                                            ; 90be: a9 00       ..
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
    ldy #&d9                                                          ; 90c0: a0 d9       ..
    sta (nfs_workspace),y                                             ; 90c2: 91 9e       ..
    lda #&80                                                          ; 90c4: a9 80       ..
    ldy #&0c                                                          ; 90c6: a0 0c       ..
    sta (nfs_workspace),y                                             ; 90c8: 91 9e       ..
    sty net_tx_ptr                                                    ; 90ca: 84 9a       ..
    ldx nfs_workspace_hi                                              ; 90cc: a6 9f       ..
    stx net_tx_ptr_hi                                                 ; 90ce: 86 9b       ..
    jsr tx_poll_ff                                                    ; 90d0: 20 71 86     q.
    lda #&3f ; '?'                                                    ; 90d3: a9 3f       .?
    sta (net_tx_ptr,x)                                                ; 90d5: 81 9a       ..
    rts                                                               ; 90d7: 60          `

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
    ldy l00f1                                                         ; 90d8: a4 f1       ..
    cmp #&81                                                          ; 90da: c9 81       ..
    beq c90f1                                                         ; 90dc: f0 13       ..
    ldy #1                                                            ; 90de: a0 01       ..
    ldx #7                                                            ; 90e0: a2 07       ..
    jsr match_osbyte_code                                             ; 90e2: 20 2a 91     *.
    beq c90f1                                                         ; 90e5: f0 0a       ..
    dey                                                               ; 90e7: 88          .
    dey                                                               ; 90e8: 88          .
    ldx #&0e                                                          ; 90e9: a2 0e       ..
    jsr match_osbyte_code                                             ; 90eb: 20 2a 91     *.
    beq c90f1                                                         ; 90ee: f0 01       ..
    iny                                                               ; 90f0: c8          .
; &90f1 referenced 3 times by &90dc, &90e5, &90ee
.c90f1
    ldx #2                                                            ; 90f1: a2 02       ..
    tya                                                               ; 90f3: 98          .
    beq return_nbyte                                                  ; 90f4: f0 33       .3
    php                                                               ; 90f6: 08          .
    bpl nbyte6                                                        ; 90f7: 10 01       ..
    inx                                                               ; 90f9: e8          .              ; X=&03
; &90fa referenced 1 time by &90f7
.nbyte6
    ldy #&dc                                                          ; 90fa: a0 dc       ..
; &90fc referenced 1 time by &9104
.nbyte1
    lda l0015,y                                                       ; 90fc: b9 15 00    ...
    sta (nfs_workspace),y                                             ; 90ff: 91 9e       ..
    dey                                                               ; 9101: 88          .
    cpy #&da                                                          ; 9102: c0 da       ..
    bpl nbyte1                                                        ; 9104: 10 f6       ..
    txa                                                               ; 9106: 8a          .
    jsr setup_tx_and_send                                             ; 9107: 20 c0 90     ..
    plp                                                               ; 910a: 28          (
    bpl return_nbyte                                                  ; 910b: 10 1c       ..
    lda #&7f                                                          ; 910d: a9 7f       ..
    sta (net_tx_ptr,x)                                                ; 910f: 81 9a       ..
; &9111 referenced 1 time by &9113
.loop_c9111
    lda (net_tx_ptr,x)                                                ; 9111: a1 9a       ..
    bpl loop_c9111                                                    ; 9113: 10 fc       ..
    tsx                                                               ; 9115: ba          .
    ldy #&dd                                                          ; 9116: a0 dd       ..
    lda (nfs_workspace),y                                             ; 9118: b1 9e       ..
    ora #&44 ; 'D'                                                    ; 911a: 09 44       .D
    bne nbyte5                                                        ; 911c: d0 04       ..             ; ALWAYS branch

; &911e referenced 1 time by &9127
.nbyte4
    dey                                                               ; 911e: 88          .
    dex                                                               ; 911f: ca          .
    lda (nfs_workspace),y                                             ; 9120: b1 9e       ..
; &9122 referenced 1 time by &911c
.nbyte5
    sta l0106,x                                                       ; 9122: 9d 06 01    ...
    cpy #&da                                                          ; 9125: c0 da       ..
    bne nbyte4                                                        ; 9127: d0 f5       ..
; &9129 referenced 2 times by &90f4, &910b
.return_nbyte
    rts                                                               ; 9129: 60          `

; &912a referenced 3 times by &90e2, &90eb, &9130
.match_osbyte_code
    cmp l9133,x                                                       ; 912a: dd 33 91    .3.
    beq return_match_osbyte                                           ; 912d: f0 03       ..
    dex                                                               ; 912f: ca          .
    bpl match_osbyte_code                                             ; 9130: 10 f8       ..
; &9132 referenced 2 times by &912d, &914a
.return_match_osbyte
    rts                                                               ; 9132: 60          `

; &9133 referenced 1 time by &912a
.l9133
    equb   4,   9, &0a, &14, &9a, &9b, &9c, &e2, &0b, &0c, &0f, &79   ; 9133: 04 09 0a... ...
    equb &7a, &e3, &e4                                                ; 913f: 7a e3 e4    z..

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
    ldy #&0e                                                          ; 9142: a0 0e       ..
    cmp #7                                                            ; 9144: c9 07       ..
    beq c914c                                                         ; 9146: f0 04       ..
    cmp #8                                                            ; 9148: c9 08       ..
    bne return_match_osbyte                                           ; 914a: d0 e6       ..
; &914c referenced 1 time by &9146
.c914c
    ldx #&db                                                          ; 914c: a2 db       ..
    stx nfs_workspace                                                 ; 914e: 86 9e       ..
; &9150 referenced 1 time by &9155
.loop_c9150
    lda (l00f0),y                                                     ; 9150: b1 f0       ..
    sta (nfs_workspace),y                                             ; 9152: 91 9e       ..
    dey                                                               ; 9154: 88          .
    bpl loop_c9150                                                    ; 9155: 10 f9       ..
    iny                                                               ; 9157: c8          .
    dec nfs_workspace                                                 ; 9158: c6 9e       ..
    lda l00ef                                                         ; 915a: a5 ef       ..
    sta (nfs_workspace),y                                             ; 915c: 91 9e       ..
    sty nfs_workspace                                                 ; 915e: 84 9e       ..
    ldy #&14                                                          ; 9160: a0 14       ..
    lda #&e9                                                          ; 9162: a9 e9       ..
    sta (nfs_workspace),y                                             ; 9164: 91 9e       ..
    lda #1                                                            ; 9166: a9 01       ..
    jsr setup_tx_and_send                                             ; 9168: 20 c0 90     ..            ; Load template byte from ctrl_block_template[X]
    stx nfs_workspace                                                 ; 916b: 86 9e       ..
; ***************************************************************************************
; Alternate entry into control block setup
; 
; Sets X=&0D, Y=&7C. Tests bit 6 of &837E to choose target:
;   V=0 (bit 6 clear): stores to (nfs_workspace)
;   V=1 (bit 6 set):   stores to (net_rx_ptr)
; ***************************************************************************************
; &916d referenced 2 times by &905b, &906d
.ctrl_block_setup_alt
    ldx #&0d                                                          ; 916d: a2 0d       ..
    ldy #&7c ; '|'                                                    ; 916f: a0 7c       .|
    bit l837e                                                         ; 9171: 2c 7e 83    ,~.
    bvs cbset2                                                        ; 9174: 70 05       p.
; ***************************************************************************************
; Control block setup — main entry
; 
; Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
; Reads the template table at &918F indexed by X, storing each
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
    ldy #&17                                                          ; 9176: a0 17       ..
    ldx #&1a                                                          ; 9178: a2 1a       ..
; &917a referenced 1 time by &923e
.ctrl_block_setup_clv
    clv                                                               ; 917a: b8          .
; &917b referenced 2 times by &9174, &919c
.cbset2
    lda ctrl_block_template,x                                         ; 917b: bd a2 91    ...
    cmp #&fe                                                          ; 917e: c9 fe       ..
    beq c919e                                                         ; 9180: f0 1c       ..
    cmp #&fd                                                          ; 9182: c9 fd       ..
    beq c919a                                                         ; 9184: f0 14       ..
    cmp #&fc                                                          ; 9186: c9 fc       ..
    bne cbset3                                                        ; 9188: d0 08       ..
    lda net_rx_ptr_hi                                                 ; 918a: a5 9d       ..
    bvs c9190                                                         ; 918c: 70 02       p.
    lda nfs_workspace_hi                                              ; 918e: a5 9f       ..
; &9190 referenced 1 time by &918c
.c9190
    sta net_tx_ptr_hi                                                 ; 9190: 85 9b       ..
; &9192 referenced 1 time by &9188
.cbset3
    bvs cbset4                                                        ; 9192: 70 04       p.
    sta (nfs_workspace),y                                             ; 9194: 91 9e       ..
    bvc c919a                                                         ; 9196: 50 02       P.             ; ALWAYS branch

; &9198 referenced 1 time by &9192
.cbset4
    sta (net_rx_ptr),y                                                ; 9198: 91 9c       ..
; &919a referenced 2 times by &9184, &9196
.c919a
    dey                                                               ; 919a: 88          .
    dex                                                               ; 919b: ca          .
    bpl cbset2                                                        ; 919c: 10 dd       ..
; &919e referenced 1 time by &9180
.c919e
    iny                                                               ; 919e: c8          .
    sty net_tx_ptr                                                    ; 919f: 84 9a       ..
    rts                                                               ; 91a1: 60          `

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
; overlapping: sta l0000                                              ; 91a2: 85 00       ..
; &91a2 referenced 1 time by &917b
.ctrl_block_template
    equb &85                                                          ; 91a2: 85          .              ; Alt-path only → Y=&6F
    equb 0                                                            ; 91a3: 00          .              ; Alt-path only → Y=&70
; overlapping: sbc l7dfd,x                                            ; 91a4: fd fd 7d    ..}
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
.remote_display_setup
    dex                                                               ; 91c9: ca          .
    cpx l00f0                                                         ; 91ca: e4 f0       ..
    bne setup1                                                        ; 91cc: d0 07       ..
    lda #&1f                                                          ; 91ce: a9 1f       ..
    sta printer_buf_ptr                                               ; 91d0: 8d 61 0d    .a.
    lda #&41 ; 'A'                                                    ; 91d3: a9 41       .A
; &91d5 referenced 1 time by &91cc
.setup1
    sta l0d60                                                         ; 91d5: 8d 60 0d    .`.
; &91d8 referenced 2 times by &91db, &91ef
.return_display_setup
    rts                                                               ; 91d8: 60          `

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
    cpy #4                                                            ; 91d9: c0 04       ..
    bne return_display_setup                                          ; 91db: d0 fb       ..
    txa                                                               ; 91dd: 8a          .
    dex                                                               ; 91de: ca          .
    bne c9207                                                         ; 91df: d0 26       .&
    tsx                                                               ; 91e1: ba          .
    ora l0106,x                                                       ; 91e2: 1d 06 01    ...
    sta l0106,x                                                       ; 91e5: 9d 06 01    ...
; &91e8 referenced 2 times by &91f7, &91fc
.prlp1
    lda #osbyte_read_buffer                                           ; 91e8: a9 91       ..
    ldx #buffer_printer                                               ; 91ea: a2 03       ..
    jsr osbyte                                                        ; 91ec: 20 f4 ff     ..            ; Get character from input buffer (C is set if the buffer is empty, otherwise Y=extracted character)
    bcs return_display_setup                                          ; 91ef: b0 e7       ..
    tya                                                               ; 91f1: 98          .              ; Y is the character extracted from the buffer
    jsr store_output_byte                                             ; 91f2: 20 fe 91     ..
    cpy #&6e ; 'n'                                                    ; 91f5: c0 6e       .n
    bcc prlp1                                                         ; 91f7: 90 ef       ..
    jsr flush_output_block                                            ; 91f9: 20 2a 92     *.
    bcc prlp1                                                         ; 91fc: 90 ea       ..
; ***************************************************************************************
; Store output byte to network buffer
; 
; Stores byte A at the current output offset in the RX buffer
; pointed to by (net_rx_ptr). Advances the offset counter and
; triggers a flush if the buffer is full.
; ***************************************************************************************
; &91fe referenced 2 times by &91f2, &920b
.store_output_byte
    ldy printer_buf_ptr                                               ; 91fe: ac 61 0d    .a.
    sta (net_rx_ptr),y                                                ; 9201: 91 9c       ..
    inc printer_buf_ptr                                               ; 9203: ee 61 0d    .a.
    rts                                                               ; 9206: 60          `

; &9207 referenced 1 time by &91df
.c9207
    pha                                                               ; 9207: 48          H
    txa                                                               ; 9208: 8a          .
    eor #1                                                            ; 9209: 49 01       I.
    jsr store_output_byte                                             ; 920b: 20 fe 91     ..
    eor l0d60                                                         ; 920e: 4d 60 0d    M`.
    ror a                                                             ; 9211: 6a          j
    bcc c921b                                                         ; 9212: 90 07       ..
    rol a                                                             ; 9214: 2a          *
    sta l0d60                                                         ; 9215: 8d 60 0d    .`.
    jsr flush_output_block                                            ; 9218: 20 2a 92     *.
; &921b referenced 1 time by &9212
.c921b
    lda l0d60                                                         ; 921b: ad 60 0d    .`.
    and #&f0                                                          ; 921e: 29 f0       ).
    ror a                                                             ; 9220: 6a          j
    tax                                                               ; 9221: aa          .
    pla                                                               ; 9222: 68          h
    ror a                                                             ; 9223: 6a          j
    txa                                                               ; 9224: 8a          .
    rol a                                                             ; 9225: 2a          *
    sta l0d60                                                         ; 9226: 8d 60 0d    .`.
    rts                                                               ; 9229: 60          `

; ***************************************************************************************
; Flush output block
; 
; Sends the accumulated output block over the network, resets the
; buffer pointer, and prepares for the next block of output data.
; ***************************************************************************************
; &922a referenced 2 times by &91f9, &9218
.flush_output_block
    ldy #8                                                            ; 922a: a0 08       ..
    lda printer_buf_ptr                                               ; 922c: ad 61 0d    .a.
    sta (nfs_workspace),y                                             ; 922f: 91 9e       ..
    lda net_rx_ptr_hi                                                 ; 9231: a5 9d       ..
    iny                                                               ; 9233: c8          .              ; Y=&09
    sta (nfs_workspace),y                                             ; 9234: 91 9e       ..
    ldy #5                                                            ; 9236: a0 05       ..
    sta (nfs_workspace),y                                             ; 9238: 91 9e       ..
    ldy #&0b                                                          ; 923a: a0 0b       ..
    ldx #&26 ; '&'                                                    ; 923c: a2 26       .&
    jsr ctrl_block_setup_clv                                          ; 923e: 20 7a 91     z.
    dey                                                               ; 9241: 88          .
    lda l0d60                                                         ; 9242: ad 60 0d    .`.
    pha                                                               ; 9245: 48          H
    rol a                                                             ; 9246: 2a          *
    pla                                                               ; 9247: 68          h
    eor #&80                                                          ; 9248: 49 80       I.
    sta l0d60                                                         ; 924a: 8d 60 0d    .`.
    rol a                                                             ; 924d: 2a          *
    sta (nfs_workspace),y                                             ; 924e: 91 9e       ..
    ldy #&1f                                                          ; 9250: a0 1f       ..
    sty printer_buf_ptr                                               ; 9252: 8c 61 0d    .a.
    lda #0                                                            ; 9255: a9 00       ..
    tax                                                               ; 9257: aa          .              ; X=&00
    ldy nfs_workspace_hi                                              ; 9258: a4 9f       ..
    cli                                                               ; 925a: 58          X
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
    stx net_tx_ptr                                                    ; 925b: 86 9a       ..
    sty net_tx_ptr_hi                                                 ; 925d: 84 9b       ..
    pha                                                               ; 925f: 48          H
    and fs_sequence_nos                                               ; 9260: 2d 08 0e    -..
    beq bsxl1                                                         ; 9263: f0 02       ..
    lda #1                                                            ; 9265: a9 01       ..
; &9267 referenced 1 time by &9263
.bsxl1
    ldy #0                                                            ; 9267: a0 00       ..
    ora (net_tx_ptr),y                                                ; 9269: 11 9a       ..
    pha                                                               ; 926b: 48          H
    sta (net_tx_ptr),y                                                ; 926c: 91 9a       ..
    jsr tx_poll_ff                                                    ; 926e: 20 71 86     q.
    lda #&ff                                                          ; 9271: a9 ff       ..
    ldy #8                                                            ; 9273: a0 08       ..
    sta (net_tx_ptr),y                                                ; 9275: 91 9a       ..
    iny                                                               ; 9277: c8          .              ; Y=&09
    sta (net_tx_ptr),y                                                ; 9278: 91 9a       ..
    pla                                                               ; 927a: 68          h
    tax                                                               ; 927b: aa          .
    ldy #&d1                                                          ; 927c: a0 d1       ..
    pla                                                               ; 927e: 68          h
    pha                                                               ; 927f: 48          H
    beq bspsx                                                         ; 9280: f0 02       ..
    ldy #&90                                                          ; 9282: a0 90       ..
; &9284 referenced 1 time by &9280
.bspsx
    tya                                                               ; 9284: 98          .
    ldy #1                                                            ; 9285: a0 01       ..
    sta (net_tx_ptr),y                                                ; 9287: 91 9a       ..
    txa                                                               ; 9289: 8a          .
    dey                                                               ; 928a: 88          .              ; Y=&00
    pha                                                               ; 928b: 48          H
; &928c referenced 1 time by &9298
.bsxl0
    lda #&7f                                                          ; 928c: a9 7f       ..
    sta (net_tx_ptr),y                                                ; 928e: 91 9a       ..
    jsr c84f8                                                         ; 9290: 20 f8 84     ..
    pla                                                               ; 9293: 68          h
    pha                                                               ; 9294: 48          H
    eor (net_tx_ptr),y                                                ; 9295: 51 9a       Q.
    ror a                                                             ; 9297: 6a          j
    bcs bsxl0                                                         ; 9298: b0 f2       ..
    pla                                                               ; 929a: 68          h
    pla                                                               ; 929b: 68          h
    tax                                                               ; 929c: aa          .
    inx                                                               ; 929d: e8          .
    beq return_bspsx                                                  ; 929e: f0 03       ..
    eor fs_sequence_nos                                               ; 92a0: 4d 08 0e    M..
; &92a3 referenced 1 time by &929e
.return_bspsx
    rts                                                               ; 92a3: 60          `

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
.save_palette_vdu
    lda l00ad                                                         ; 92a4: a5 ad       ..
    pha                                                               ; 92a6: 48          H
    lda #&e9                                                          ; 92a7: a9 e9       ..
    sta nfs_workspace                                                 ; 92a9: 85 9e       ..
    ldy #0                                                            ; 92ab: a0 00       ..
    sty l00ad                                                         ; 92ad: 84 ad       ..
    lda l0350                                                         ; 92af: ad 50 03    .P.
    sta (nfs_workspace),y                                             ; 92b2: 91 9e       ..
    inc nfs_workspace                                                 ; 92b4: e6 9e       ..
    lda l0351                                                         ; 92b6: ad 51 03    .Q.
    pha                                                               ; 92b9: 48          H
    tya                                                               ; 92ba: 98          .              ; A=&00
; &92bb referenced 1 time by &92da
.loop_c92bb
    sta (nfs_workspace),y                                             ; 92bb: 91 9e       ..
    ldx nfs_workspace                                                 ; 92bd: a6 9e       ..
    ldy nfs_workspace_hi                                              ; 92bf: a4 9f       ..
    lda #osword_read_palette                                          ; 92c1: a9 0b       ..
    jsr osword                                                        ; 92c3: 20 f1 ff     ..            ; Read palette
    pla                                                               ; 92c6: 68          h
    ldy #0                                                            ; 92c7: a0 00       ..
    sta (nfs_workspace),y                                             ; 92c9: 91 9e       ..
    iny                                                               ; 92cb: c8          .              ; Y=&01
    lda (nfs_workspace),y                                             ; 92cc: b1 9e       ..
    pha                                                               ; 92ce: 48          H
    ldx nfs_workspace                                                 ; 92cf: a6 9e       ..
    inc nfs_workspace                                                 ; 92d1: e6 9e       ..
    inc l00ad                                                         ; 92d3: e6 ad       ..
    dey                                                               ; 92d5: 88          .              ; Y=&00
    lda l00ad                                                         ; 92d6: a5 ad       ..
    cpx #&f9                                                          ; 92d8: e0 f9       ..
    bne loop_c92bb                                                    ; 92da: d0 df       ..
    pla                                                               ; 92dc: 68          h
    sty l00ad                                                         ; 92dd: 84 ad       ..
    inc nfs_workspace                                                 ; 92df: e6 9e       ..
    jsr save_vdu_state                                                ; 92e1: 20 f0 92     ..
    inc nfs_workspace                                                 ; 92e4: e6 9e       ..
    pla                                                               ; 92e6: 68          h
    sta l00ad                                                         ; 92e7: 85 ad       ..
; &92e9 referenced 4 times by &847d, &84a5, &84cc, &8eec
.clear_jsr_protection
    lda saved_jsr_mask                                                ; 92e9: ad 65 0d    .e.
    sta prot_status                                                   ; 92ec: 8d 63 0d    .c.
    rts                                                               ; 92ef: 60          `

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
    lda l0355                                                         ; 92f0: ad 55 03    .U.
    sta (nfs_workspace),y                                             ; 92f3: 91 9e       ..
    tax                                                               ; 92f5: aa          .
    jsr read_vdu_osbyte                                               ; 92f6: 20 03 93     ..
    inc nfs_workspace                                                 ; 92f9: e6 9e       ..
    tya                                                               ; 92fb: 98          .
    sta (nfs_workspace,x)                                             ; 92fc: 81 9e       ..
    jsr read_vdu_osbyte_x0                                            ; 92fe: 20 01 93     ..
; &9301 referenced 1 time by &92fe
.read_vdu_osbyte_x0
    ldx #0                                                            ; 9301: a2 00       ..
; &9303 referenced 1 time by &92f6
.read_vdu_osbyte
    ldy l00ad                                                         ; 9303: a4 ad       ..
    inc l00ad                                                         ; 9305: e6 ad       ..
    inc nfs_workspace                                                 ; 9307: e6 9e       ..
    lda osbyte_vdu_table,y                                            ; 9309: b9 17 93    ...
    ldy #&ff                                                          ; 930c: a0 ff       ..
    jsr osbyte                                                        ; 930e: 20 f4 ff     ..
    txa                                                               ; 9311: 8a          .
    ldx #0                                                            ; 9312: a2 00       ..
    sta (nfs_workspace,x)                                             ; 9314: 81 9e       ..
    rts                                                               ; 9316: 60          `

; 3-entry OSBYTE table for save_palette_vdu (&92A4)
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
    jmp c9bf3                                                         ; 9660: 4c f3 9b    L..

; &9663 referenced 1 time by &830d
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
; NMI shim from ROM (&9FD9) to RAM (&0D00), patches the current
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
; Reached when the scout data loop sees no RDA (BPL at &974C) or
; when scout completion finds unexpected SR2 state.
; If SR2 & &81 is non-zero (AP or RDA still active), performs full
; ADLC reset and discards. If zero (clean end), discards via &9A40.
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
;     - Neither set (BEQ) -> discard (&9744 -> &9A40)
;     - AP without RDA (BPL) -> error (&9737)
;     - RDA set (BMI) -> read byte
;   - After first byte (&9755): full SR2 tested
;     - SR2 non-zero (BNE) -> scout completion (&9771)
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
;   - No FV (BEQ) -> error &9737 (not a valid frame end)
;   - FV set, no RDA (BPL) -> error &9737 (missing last byte)
;   - FV set, RDA set -> read last byte, process scout
; After reading the last byte, the complete scout buffer (&0D3D-&0D48)
; contains: src_stn, src_net, ctrl, port [, extra_data...].
; The port byte at &0D40 determines further processing:
;   - Port = 0 -> immediate operation (&9A59)
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
; Handler chain: &9839 (AP+addr check) -> &984F (net=0 check) ->
; &9865 (skip ctrl+port) -> &989A (bulk data read) -> &98CE (completion)
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
; SR2 non-zero (FV or other) -> frame completion at &98CE.
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
; Same pattern as scout completion (&9771): disables PSE (CR1=&00,
; CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
; If extra data available and buffer space remains, stores it.
; Proceeds to send the final ACK via &995E.
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
; If bit7 of &0D4A is set, this is a final ACK -> completion (&9F39).
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
; installs NMI TX handler at &9D4C, and re-enables NMIs.
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
;   - bit6 set at &0D4A -> completion at &9F39
;   - bit0 set at &0D4A -> four-way handshake data phase at &9EDD
;   - Otherwise -> install RX reply handler at &9DB2
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
; validates it is zero (local network). Installs &9DE3 for the
; remaining two bytes (source station and network).
; Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DD9.
; If IRQ is still set, falls through directly to &9DE3 without an RTI,
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
;   1. Check SR2 bit7 (RDA) at &9DE3 -- must see data available
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
; Same pattern as the NMI TX handler at &9D4C but reads from the port
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
; and installs &9EE9 to receive the final ACK from the remote station.
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
; pattern as the reply scout handler (&9DB2-&9DE3):
;   &9EE9: Check AP, read dest_stn, compare to our station
;   &9EFF: Check RDA, read dest_net, validate = 0
;   &9F15: Check RDA, read src_stn/net, compare to TX dest
;   &9F32: Check FV for frame completion
; On success, stores result=0 at &9F39. On any failure, error &41.
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
; and calls full ADLC reset + idle listen via &9A34.
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
; hardcodes JMP nmi_rx_scout (&96F6). Used as the initial NMI handler
; before the workspace has been properly set up during initialisation.
; Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
; LDA romsel, STA &FE30, JMP &96F6.
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

    assert <(cat_handler-1) == &ff
    assert <(copy_handles-1) == &28
    assert <(copy_handles_and_boot-1) == &27
    assert <(dispatch_net_cmd-1) == &68
    assert <(econet_tx_rx-1) == &ec
    assert <(eof_handler-1) == &50
    assert <(execute_at_0100-1) == &a4
    assert <(fscv_read_handles-1) == &55
    assert <(fscv_shutdown-1) == &40
    assert <(fscv_star_handler-1) == &b3
    assert <(insert_remote_key-1) == &c4
    assert <(l0128) == &28
    assert <(net1_read_handle-1) == &42
    assert <(notify_and_exec-1) == &cc
    assert <(opt_handler-1) == &cb
    assert <(osword_11_handler-1) == &d9
    assert <(osword_fs_entry-1) == &7d
    assert <(print_dir_name-1) == &5e
    assert <(remote_boot_handler-1) == &76
    assert <(remote_cmd_data-1) == &41
    assert <(remote_cmd_dispatch-1) == &d7
    assert <(remote_display_setup-1) == &c8
    assert <(remote_print_handler-1) == &d8
    assert <(remote_validated-1) == &b4
    assert <(resume_after_remote-1) == &89
    assert <(return_2-1) == &75
    assert <(rx_imm_exec-1) == &b4
    assert <(rx_imm_machine_type-1) == &dd
    assert <(rx_imm_peek-1) == &f0
    assert <(rx_imm_poke-1) == &d2
    assert <(save_palette_vdu-1) == &a3
    assert <(set_csd_handle-1) == &21
    assert <(set_lib_handle-1) == &1c
    assert <(sub_c0490-1) == &8f
    assert <(sub_c8183-1) == &82
    assert <(sub_c8dc7-1) == &c6
    assert <(sub_c8e5e-1) == &5d
    assert <(sub_c8e6e-1) == &6d
    assert <(sub_c8eff-1) == &fe
    assert <(sub_c908f-1) == &8e
    assert <(sub_c90b2-1) == &b1
    assert <(sub_c9b17-1) == &16
    assert <(sub_c9cf3-1) == &f2
    assert <(svc_abs_workspace-1) == &ab
    assert <(svc_autoboot-1) == &0c
    assert <(svc_help-1) == &f6
    assert <(svc_nmi_claim-1) == &68
    assert <(svc_nmi_release-1) == &65
    assert <(svc_private_workspace-1) == &b4
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
    assert >(cat_handler-1) == &8b
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
    assert >(osword_11_handler-1) == &8e
    assert >(osword_fs_entry-1) == &8e
    assert >(print_dir_name-1) == &8d
    assert >(remote_boot_handler-1) == &84
    assert >(remote_cmd_data-1) == &91
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
    assert >(set_csd_handle-1) == &8e
    assert >(set_lib_handle-1) == &8e
    assert >(sub_c0490-1) == &04
    assert >(sub_c8183-1) == &81
    assert >(sub_c8dc7-1) == &8d
    assert >(sub_c8e5e-1) == &8e
    assert >(sub_c8e6e-1) == &8e
    assert >(sub_c8eff-1) == &8e
    assert >(sub_c908f-1) == &90
    assert >(sub_c90b2-1) == &90
    assert >(sub_c9b17-1) == &9b
    assert >(sub_c9cf3-1) == &9c
    assert >(svc_abs_workspace-1) == &82
    assert >(svc_autoboot-1) == &82
    assert >(svc_help-1) == &81
    assert >(svc_nmi_claim-1) == &96
    assert >(svc_nmi_release-1) == &96
    assert >(svc_private_workspace-1) == &82
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
;     osbyte:                                  23
;     set_nmi_vector:                          22
;     tube_read_r2:                            22
;     port_buf_len:                            20
;     tube_send_r2:                            17
;     open_port_buf_hi:                        16
;     rx_flags:                                16
;     fs_load_addr_2:                          15
;     l0f06:                                   15
;     station_id_disable_net_nmis:             15
;     nfs_temp:                                14
;     open_port_buf:                           14
;     print_inline:                            14
;     fs_load_addr:                            13
;     l00ab:                                   13
;     port_buf_len_hi:                         13
;     c9894:                                   12
;     prepare_fs_cmd:                          12
;     tube_data_register_2:                    12
;     tube_status_register_2:                  11
;     fs_error_ptr:                            10
;     nfs_workspace_hi:                        10
;     rom_svc_num:                             10
;     tube_addr_claim:                         10
;     l00c8:                                    9
;     nmi_tx_block_hi:                          9
;     rx_src_stn:                               9
;     tube_data_register_3:                     9
;     l0000:                                    8
;     l00ad:                                    8
;     l00b4:                                    8
;     l00c4:                                    8
;     tube_status_1_and_tube_control:           8
;     tx_result_fail:                           8
;     fs_cmd_csd:                               7
;     fs_cmd_urd:                               7
;     l0d60:                                    7
;     prot_status:                              7
;     reply_error:                              7
;     return_1:                                 7
;     tx_clear_flag:                            7
;     tx_dst_stn:                               7
;     copy_string_to_cmd:                       6
;     fs_crc_lo:                                6
;     fs_load_addr_hi:                          6
;     net_rx_ptr_hi:                            6
;     net_tx_ptr_hi:                            6
;     nmi_rti:                                  6
;     osasci:                                   6
;     restore_args_return:                      6
;     rx_buf_offset:                            6
;     scout_status:                             6
;     tube_main_loop:                           6
;     tx_in_progress:                           6
;     zp_temp_10:                               6
;     c8959:                                    5
;     copy_param_block:                         5
;     dispatch:                                 5
;     fs_block_offset:                          5
;     fs_boot_option:                           5
;     l0001:                                    5
;     l00b3:                                    5
;     l0100:                                    5
;     l0106:                                    5
;     l0f07:                                    5
;     printer_buf_ptr:                          5
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
;     zp_temp_11:                               5
;     c8871:                                    4
;     c8974:                                    4
;     clear_jsr_protection:                     4
;     data_tx_error:                            4
;     data_tx_last:                             4
;     discard_reset_listen:                     4
;     fs_cmd_context:                           4
;     fs_eof_flags:                             4
;     fs_last_byte_flag:                        4
;     fs_sequence_nos:                          4
;     fs_server_net:                            4
;     init_tx_ctrl_block:                       4
;     l0015:                                    4
;     l00ac:                                    4
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
;     c84f8:                                    3
;     c850a:                                    3
;     c90f1:                                    3
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
;     copy_filename:                            3
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
;     l00aa:                                    3
;     l00af:                                    3
;     l00b5:                                    3
;     l00ba:                                    3
;     l00cf:                                    3
;     l0f08:                                    3
;     l837e:                                    3
;     l85a5:                                    3
;     match_osbyte_code:                        3
;     nmi_jmp_hi:                               3
;     nmi_jmp_lo:                               3
;     openl4:                                   3
;     oscli:                                    3
;     osword:                                   3
;     pad_filename_spaces:                      3
;     print_dir_from_offset:                    3
;     print_reply_bytes:                        3
;     romsel_copy:                              3
;     saved_jsr_mask:                           3
;     scout_no_match:                           3
;     setup_tx_and_send:                        3
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
;     c055f:                                    2
;     c8099:                                    2
;     c8205:                                    2
;     c827d:                                    2
;     c8306:                                    2
;     c84b2:                                    2
;     c8621:                                    2
;     c863e:                                    2
;     c86a9:                                    2
;     c86b1:                                    2
;     c86d8:                                    2
;     c8add:                                    2
;     c8b54:                                    2
;     c8cde:                                    2
;     c8d0b:                                    2
;     c8d7b:                                    2
;     c8db8:                                    2
;     c8e1a:                                    2
;     c8e25:                                    2
;     c8fc3:                                    2
;     c919a:                                    2
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
;     ctrl_block_setup_alt:                     2
;     data_rx_tube_complete:                    2
;     decode_attribs_5bit:                      2
;     decode_attribs_6bit:                      2
;     econet_tx_retry:                          2
;     flush_output_block:                       2
;     fs_cmd_match_table:                       2
;     fs_cmd_y_param:                           2
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
;     l0fde:                                    2
;     l0fdf:                                    2
;     language_entry:                           2
;     logon3:                                   2
;     mask_to_handle:                           2
;     match_rom_string:                         2
;     nlisne:                                   2
;     num01:                                    2
;     nvwrch:                                   2
;     osarg1:                                   2
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
;     send_fs_reply_timed:                      2
;     send_to_fs:                               2
;     setup_tx_ptr_c0:                          2
;     store_output_byte:                        2
;     store_rom_ptr_pair:                       2
;     sub_3_from_y:                             2
;     sub_c8e4a:                                2
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
;     boot_option_offsets:                      1
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
;     c05c2:                                    1
;     c0678:                                    1
;     c8093:                                    1
;     c80f4:                                    1
;     c814c:                                    1
;     c8150:                                    1
;     c8158:                                    1
;     c81b1:                                    1
;     c81b8:                                    1
;     c8222:                                    1
;     c824f:                                    1
;     c8254:                                    1
;     c839d:                                    1
;     c839e:                                    1
;     c83de:                                    1
;     c8443:                                    1
;     c8449:                                    1
;     c845d:                                    1
;     c84d4:                                    1
;     c854f:                                    1
;     c85d4:                                    1
;     c85f0:                                    1
;     c85fa:                                    1
;     c8622:                                    1
;     c8665:                                    1
;     c867c:                                    1
;     c86b5:                                    1
;     c871b:                                    1
;     c87b9:                                    1
;     c87cc:                                    1
;     c8800:                                    1
;     c8829:                                    1
;     c8832:                                    1
;     c88c0:                                    1
;     c88c6:                                    1
;     c890a:                                    1
;     c893b:                                    1
;     c895e:                                    1
;     c8969:                                    1
;     c89ca:                                    1
;     c89d4:                                    1
;     c89ee:                                    1
;     c8a06:                                    1
;     c8a1b:                                    1
;     c8a57:                                    1
;     c8a96:                                    1
;     c8a99:                                    1
;     c8aa6:                                    1
;     c8aba:                                    1
;     c8af1:                                    1
;     c8b32:                                    1
;     c8b3f:                                    1
;     c8b57:                                    1
;     c8b93:                                    1
;     c8bdc:                                    1
;     c8c0a:                                    1
;     c8c46:                                    1
;     c8c50:                                    1
;     c8c83:                                    1
;     c8cb3:                                    1
;     c8d23:                                    1
;     c8d2b:                                    1
;     c8d80:                                    1
;     c8e33:                                    1
;     c8e6b:                                    1
;     c8f0f:                                    1
;     c8f5b:                                    1
;     c8f98:                                    1
;     c8ffb:                                    1
;     c9039:                                    1
;     c914c:                                    1
;     c9190:                                    1
;     c919e:                                    1
;     c9207:                                    1
;     c921b:                                    1
;     c931a:                                    1
;     c935f:                                    1
;     c955f:                                    1
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
;     fs_crc_hi:                                1
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
;     l0cff:                                    1
;     l0de6:                                    1
;     l0df0:                                    1
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
;     l18a5:                                    1
;     l212e:                                    1
;     l4:                                       1
;     l8001:                                    1
;     l8002:                                    1
;     l8004:                                    1
;     l8014:                                    1
;     l8be3:                                    1
;     l8ea7:                                    1
;     l8eac:                                    1
;     l8efd:                                    1
;     l9133:                                    1
;     l945f:                                    1
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
;     loop_c0618:                               1
;     loop_c0684:                               1
;     loop_c06a2:                               1
;     loop_c807d:                               1
;     loop_c80a7:                               1
;     loop_c8111:                               1
;     loop_c8144:                               1
;     loop_c81a4:                               1
;     loop_c81d8:                               1
;     loop_c8256:                               1
;     loop_c82f7:                               1
;     loop_c83a5:                               1
;     loop_c845f:                               1
;     loop_c84ac:                               1
;     loop_c84e5:                               1
;     loop_c85cc:                               1
;     loop_c85ea:                               1
;     loop_c8602:                               1
;     loop_c864c:                               1
;     loop_c867f:                               1
;     loop_c871d:                               1
;     loop_c874c:                               1
;     loop_c874e:                               1
;     loop_c8795:                               1
;     loop_c87c9:                               1
;     loop_c880b:                               1
;     loop_c882b:                               1
;     loop_c8932:                               1
;     loop_c8941:                               1
;     loop_c89fa:                               1
;     loop_c8b25:                               1
;     loop_c8b95:                               1
;     loop_c8bbb:                               1
;     loop_c8c78:                               1
;     loop_c8d99:                               1
;     loop_c8da2:                               1
;     loop_c8de5:                               1
;     loop_c8deb:                               1
;     loop_c8f2f:                               1
;     loop_c8f49:                               1
;     loop_c8fae:                               1
;     loop_c9010:                               1
;     loop_c9050:                               1
;     loop_c9062:                               1
;     loop_c9111:                               1
;     loop_c9150:                               1
;     loop_c92bb:                               1
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
;     send_fs_reply_cmd:                        1
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
;     sub_c8352:                                1
;     sub_c86c5:                                1
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
;     c0678
;     c8093
;     c8099
;     c80f4
;     c814c
;     c8150
;     c8158
;     c81b1
;     c81b8
;     c8205
;     c8222
;     c824f
;     c8254
;     c827d
;     c8306
;     c839d
;     c839e
;     c83de
;     c8443
;     c8449
;     c845d
;     c84b2
;     c84d4
;     c84f8
;     c850a
;     c854f
;     c85d4
;     c85f0
;     c85fa
;     c8621
;     c8622
;     c863e
;     c8665
;     c867c
;     c86a9
;     c86b1
;     c86b5
;     c86d8
;     c871b
;     c87b9
;     c87cc
;     c8800
;     c8829
;     c8832
;     c8871
;     c88c0
;     c88c6
;     c890a
;     c893b
;     c8959
;     c895e
;     c8969
;     c8974
;     c89ca
;     c89d4
;     c89ee
;     c8a06
;     c8a1b
;     c8a57
;     c8a96
;     c8a99
;     c8aa6
;     c8aba
;     c8add
;     c8af1
;     c8b32
;     c8b3f
;     c8b54
;     c8b57
;     c8b93
;     c8bdc
;     c8c0a
;     c8c46
;     c8c50
;     c8c83
;     c8cb3
;     c8cde
;     c8d0b
;     c8d23
;     c8d2b
;     c8d7b
;     c8d80
;     c8db8
;     c8e1a
;     c8e25
;     c8e33
;     c8e6b
;     c8f0f
;     c8f5b
;     c8f98
;     c8fc3
;     c8ffb
;     c9039
;     c90f1
;     c914c
;     c9190
;     c919a
;     c919e
;     c9207
;     c921b
;     c931a
;     c935f
;     c955f
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
;     l0078
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
;     l00e2
;     l00ea
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
;     l0cff
;     l0d1e
;     l0d58
;     l0d59
;     l0d60
;     l0de6
;     l0df0
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
;     l18a5
;     l212e
;     l7dfd
;     l8001
;     l8002
;     l8004
;     l800d
;     l8014
;     l837e
;     l85a5
;     l85a6
;     l85c8
;     l8be3
;     l8ea7
;     l8eac
;     l8efd
;     l9133
;     l945f
;     l9a24
;     l9a2c
;     l9b1d
;     l9b22
;     l9c6a
;     l9ed9
;     l9ee1
;     la560
;     loop_c0430
;     loop_c0448
;     loop_c048a
;     loop_c04d1
;     loop_c0592
;     loop_c05a6
;     loop_c05f8
;     loop_c0604
;     loop_c0618
;     loop_c0684
;     loop_c06a2
;     loop_c807d
;     loop_c80a7
;     loop_c8111
;     loop_c8144
;     loop_c81a4
;     loop_c81d8
;     loop_c8256
;     loop_c82f7
;     loop_c83a5
;     loop_c845f
;     loop_c84ac
;     loop_c84e5
;     loop_c85cc
;     loop_c85ea
;     loop_c8602
;     loop_c864c
;     loop_c867f
;     loop_c871d
;     loop_c874c
;     loop_c874e
;     loop_c8795
;     loop_c87c9
;     loop_c880b
;     loop_c882b
;     loop_c8932
;     loop_c8941
;     loop_c89fa
;     loop_c8b25
;     loop_c8b95
;     loop_c8bbb
;     loop_c8c78
;     loop_c8d99
;     loop_c8da2
;     loop_c8de5
;     loop_c8deb
;     loop_c8f2f
;     loop_c8f49
;     loop_c8fae
;     loop_c9010
;     loop_c9050
;     loop_c9062
;     loop_c9111
;     loop_c9150
;     loop_c92bb
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
;     sub_c0490
;     sub_c8183
;     sub_c8352
;     sub_c86c5
;     sub_c8dc7
;     sub_c8e4a
;     sub_c8e5e
;     sub_c8e6e
;     sub_c8e7a
;     sub_c8eb7
;     sub_c8eff
;     sub_c908f
;     sub_c90b2
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
;     Code                     = 7506 bytes (92%)
;     Data                     = 686 bytes (8%)
;
;     Number of instructions   = 3624
;     Number of data bytes     = 420 bytes
;     Number of data words     = 0 bytes
;     Number of string bytes   = 266 bytes
;     Number of strings        = 37
